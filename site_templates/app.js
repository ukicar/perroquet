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
