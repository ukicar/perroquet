// Copy-to-clipboard for command buttons: the viewer pastes the command into Claude Code / OpenCode.
document.addEventListener("click", (ev) => {
  const b = ev.target.closest("button.cmd");
  if (!b) return;
  const text = b.dataset.cmd;
  const done = () => { const t = b.textContent; b.classList.add("done"); b.textContent = "Copié : " + text;
    setTimeout(() => { b.classList.remove("done"); b.textContent = t; }, 1600); };
  const fallback = () => {
    const ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta);
    ta.select(); try { document.execCommand("copy"); done(); } catch (e) { /* the text stays selected */ }
    ta.remove();
  };
  try { navigator.clipboard.writeText(text).then(done, fallback); } catch (e) { fallback(); }
});

// Biography margin notes: on wide screens, put each note level with its marker, pushed down only as far as
// needed to clear the note above (CSS floats alone let the notes drift further and further below their text).
(() => {
  const bio = document.querySelector(".bio");
  if (!bio) return;
  const wide = window.matchMedia("(min-width: 1001px)");
  const place = () => {
    const notes = bio.querySelectorAll(".sn");
    bio.classList.toggle("bio-js", wide.matches);
    if (!wide.matches) { notes.forEach((n) => { n.style.top = ""; }); bio.style.minHeight = ""; return; }
    const top0 = bio.getBoundingClientRect().top;
    let floor = 0;
    notes.forEach((n) => {
      const m = n.previousElementSibling && n.previousElementSibling.previousElementSibling;
      const y = m ? m.getBoundingClientRect().top - top0 - 4 : floor;
      const t = Math.max(y, floor);
      n.style.top = t + "px";
      floor = t + n.offsetHeight + 8;
    });
    bio.style.minHeight = floor + "px";
  };
  place();
  addEventListener("resize", place);
  wide.addEventListener("change", place);
  if (document.fonts) document.fonts.ready.then(place);
})();
