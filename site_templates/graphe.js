// Network graph in the spirit of nodegoat: typed coloured nodes sized by degree, legend that
// toggles types, search, side panel of in/out links, and a time window with playback.
(function () {
  const G = window.GRAPH;
  const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const STRONG = new Set(["etabli", "probable"]);
  const hidden = new Set();
  // label only the best-connected non-source nodes by default (about the top 25)
  const degs = G.nodes.filter((n) => n.type !== "source").map((n) => n.deg).sort((a, b) => b - a);
  const LABEL_DEG = Math.max(3, degs[Math.min(24, degs.length - 1)] || 0);

  const elements = [
    ...G.nodes.map((n) => ({ data: { ...n, size: 9 + 5 * Math.sqrt(n.deg) } })),
    ...G.edges.map((e) => ({ data: e })),
  ];

  function style() {
    const ink = css("--ink"), ink2 = css("--ink-2"), rule = css("--rule"), surface = css("--surface");
    return [
      { selector: "node", style: {
        "background-color": (n) => css("--t-" + n.data("type")) || "#888",
        width: "data(size)", height: "data(size)", label: "data(label)",
        "font-family": "Alegreya Sans, system-ui, sans-serif", "font-size": 11, color: ink,
        "text-valign": "center", "text-halign": "right", "text-margin-x": 4,
        "text-outline-color": surface, "text-outline-width": 2,
        "min-zoomed-font-size": 9, "border-width": 1.5, "border-color": surface,
        "text-opacity": (n) => (document.getElementById("labels").checked || G.nodes.length < 60 ||
          (n.data("type") !== "source" && n.data("deg") >= LABEL_DEG) ? 1 : 0),
      }},
      { selector: "node[type = 'hypothese']", style: { shape: "diamond" } },
      { selector: "node[type = 'source']", style: { shape: "round-rectangle" } },
      { selector: "node[type = 'evenement']", style: { shape: "round-triangle" } },
      { selector: "node:selected, node.focus", style: { "border-color": ink, "border-width": 3, "text-opacity": 1, "z-index": 10 } },
      { selector: "node.nb", style: { "text-opacity": 1 } },
      { selector: "edge", style: {
        width: 1.2, "line-color": ink2, opacity: 0.55, "curve-style": "bezier",
        "target-arrow-shape": "none",
      }},
      { selector: "edge[kind = 'relation'][conf = 'plausible'], edge[kind = 'relation'][conf = 'possible'], edge[kind = 'relation'][conf = 'improbable']",
        style: { "line-style": "dashed", "line-dash-pattern": [6, 4] } },
      { selector: "edge[?hyp]", style: { "line-color": css("--t-hypothese"), "line-style": "dashed", "line-dash-pattern": [2, 3], opacity: 0.8 } },
      { selector: "edge[conf = 'refute']", style: { "line-color": css("--gueules"), opacity: 0.4 } },
      { selector: "edge[kind = 'mention']", style: { "line-color": rule, width: 1, opacity: 0.9 } },
      { selector: "edge[kind = 'question']", style: { "line-color": css("--t-hypothese"), width: 1, opacity: 0.6 } },
      { selector: "edge.focus", style: { opacity: 1, width: 2.2, label: "data(label)", "font-size": 10, color: ink2,
        "text-rotation": "autorotate", "text-background-color": surface, "text-background-opacity": 1, "text-background-padding": 2 } },
      { selector: ".faded", style: { opacity: 0.12, "text-opacity": 0 } },
    ];
  }

  const cy = cytoscape({
    container: document.getElementById("cy"), elements, style: style(),
    layout: { name: "preset" },
    minZoom: 0.15, maxZoom: 4,
  });
  window.cy = cy;
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => cy.style(style()));
  new MutationObserver(() => cy.style(style())).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });

  // legend counts and type toggles
  document.querySelectorAll("[data-count]").forEach((el) => {
    el.textContent = G.nodes.filter((n) => n.type === el.dataset.count).length;
  });
  document.getElementById("legend").addEventListener("click", (ev) => {
    const b = ev.target.closest("button"); if (!b) return;
    const t = b.dataset.type;
    hidden.has(t) ? hidden.delete(t) : hidden.add(t);
    b.classList.toggle("off", hidden.has(t));
    apply();
  });

  // time window
  const years = G.nodes.flatMap((n) => [n.a, n.b]).filter((y) => y);
  const minY = years.length ? Math.min(...years) : 1500, maxY = years.length ? Math.max(...years) : 1700;
  const y0 = document.getElementById("y0"), y1 = document.getElementById("y1"), yrs = document.getElementById("yrs");
  for (const r of [y0, y1]) { r.min = minY; r.max = maxY; r.step = 1; }
  y0.value = minY; y1.value = maxY;
  const undated = document.getElementById("undated");
  const isolated = document.getElementById("isolated");

  function apply() {
    let a = +y0.value, b = +y1.value;
    if (a > b) [a, b] = [b, a];
    yrs.textContent = `${a} – ${b}`;
    const facts = document.getElementById("facts").checked;
    const showMentions = document.getElementById("mentions").checked;
    cy.batch(() => {
      cy.nodes().forEach((n) => {
        const d = n.data();
        let vis = !hidden.has(d.type);
        if (vis && d.a) vis = d.a <= b && (d.b || d.a) >= a;
        else if (vis && !d.a && (d.type !== "source" && d.type !== "hypothese")) vis = undated.checked;
        if (facts && d.type === "hypothese") vis = false;
        if (vis && !isolated.checked && d.deg === 0) vis = false;
        n.style("display", vis ? "element" : "none");
      });
      cy.edges().forEach((e) => {
        const d = e.data();
        let vis = e.source().style("display") !== "none" && e.target().style("display") !== "none";
        if (vis && d.kind === "mention") vis = showMentions;
        if (vis && facts && d.kind === "relation") vis = STRONG.has(d.conf) && !d.hyp;
        if (vis && d.a) vis = d.a <= b && (d.b || d.a) >= a;
        e.style("display", vis ? "element" : "none");
      });
    });
  }
  for (const el of [y0, y1, undated, isolated, document.getElementById("facts"), document.getElementById("mentions")]) el.addEventListener("input", apply);
  document.getElementById("labels").addEventListener("change", () => cy.style(style()));
  document.getElementById("reset").addEventListener("click", () => { y0.value = minY; y1.value = maxY; stop(); apply(); });

  let timer = null;
  const play = document.getElementById("play");
  function stop() { clearInterval(timer); timer = null; play.textContent = "▶ Défiler"; }
  play.addEventListener("click", () => {
    if (timer) return stop();
    const width = Math.max(3, Math.min(10, Math.round((maxY - minY) / 12)));
    let cur = minY;
    play.textContent = "❚❚ Pause";
    timer = setInterval(() => {
      y0.value = cur; y1.value = Math.min(maxY, cur + width); apply();
      cur += 1; if (cur + width > maxY + 1) stop();
    }, 450);
  });

  // side panel
  const info = document.getElementById("info");
  const typeLabel = { personne: "Personne", famille: "Famille", lieu: "Lieu", evenement: "Événement", institution: "Institution", source: "Source", hypothese: "Question" };
  function focus(n) {
    cy.elements().removeClass("focus faded nb");
    const hood = n.closedNeighborhood();
    cy.elements().not(hood).addClass("faded");
    hood.edges().addClass("focus"); hood.nodes().addClass("nb"); n.addClass("focus");
    const d = n.data();
    const outs = {}, ins = {};
    n.connectedEdges().forEach((e) => {
      const o = e.source().id() === d.id;
      const key = o ? e.data("label") : e.data("inverse");
      const bucket = o ? outs : ins;
      (bucket[key] = bucket[key] || []).push(o ? e.target() : e.source());
    });
    const block = (title, obj) => {
      const ks = Object.keys(obj); if (!ks.length) return "";
      return `<div><b class="small">${title}</b><div class="links">${ks.map((k) => `<span>${esc(k)}</span><span class="n">${obj[k].length}</span>`).join("")}</div>
        <ul>${ks.flatMap((k) => obj[k].map((m) => `<li><a data-go="${esc(m.id())}">${esc(m.data("label"))}</a> <span class="muted">${esc(k)}</span></li>`)).join("")}</ul></div>`;
    };
    const span = d.a ? `<span class="locus">${d.a}${d.b && d.b !== d.a ? "–" + d.b : ""}</span>` : "";
    info.innerHTML = `<div class="eyebrow"><span class="chip type-${d.type}"><span class="dot"></span><span style="color:var(--ink-2)">${typeLabel[d.type] || d.type}</span></span> ${span}</div>
      <div style="font-family:var(--display);font-size:22px;line-height:1.2">${esc(d.label)}</div>
      <a href="${esc(d.url)}">Ouvrir la fiche</a>
      ${block("Liens sortants", outs)}${block("Liens entrants", ins)}`;
  }
  info.addEventListener("click", (ev) => {
    const a = ev.target.closest("[data-go]"); if (!a) return;
    const n = cy.getElementById(a.dataset.go); select(n);
  });
  function select(n) {
    if (!n || n.empty()) return;
    cy.nodes().unselect(); n.select(); focus(n);
    cy.animate({ center: { eles: n }, zoom: Math.max(cy.zoom(), 1.1) }, { duration: 300 });
  }
  cy.on("tap", "node", (ev) => focus(ev.target));
  cy.on("dbltap", "node", (ev) => { location.href = ev.target.data("url"); });
  cy.on("tap", (ev) => { if (ev.target === cy) { cy.elements().removeClass("focus faded nb"); } });

  // search
  const dl = document.getElementById("names");
  dl.innerHTML = G.nodes.map((n) => `<option value="${esc(n.label)}"></option>`).join("");
  document.getElementById("q").addEventListener("change", (ev) => {
    const v = ev.target.value.toLowerCase();
    const n = cy.nodes().filter((x) => x.data("label").toLowerCase() === v)[0] || cy.nodes().filter((x) => x.data("label").toLowerCase().includes(v))[0];
    if (n) select(cy.getElementById(n.id()));
  });

  apply();
  cy.elements(":visible").layout({ name: "cose", animate: false, randomize: true, nodeRepulsion: () => 12000,
    idealEdgeLength: () => 80, edgeElasticity: () => 90, gravity: 0.5, numIter: 3000, padding: 30 }).run();
  cy.fit(cy.elements(":visible"), 30);
  window.addEventListener("load", () => { cy.resize(); cy.fit(cy.elements(":visible"), 30); });
  function fromHash() {
    const id = decodeURIComponent(location.hash.slice(1));
    if (id && !cy.getElementById(id).empty()) setTimeout(() => select(cy.getElementById(id)), 60);
  }
  window.addEventListener("hashchange", fromHash);
  window.addEventListener("load", fromHash);
})();
