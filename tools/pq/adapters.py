"""Generate agent-specific wrappers from the agent-neutral procedures in methode/.

methode/commandes/<cmd>.md  →  .claude/skills/<cmd>/SKILL.md   (Claude Code)
                               .opencode/commands/<cmd>.md     (OpenCode)
methode/roles/<role>.md     →  .claude/agents/<role>.md        (Claude Code sub-agents)
                               .opencode/agents/<role>.md      (OpenCode sub-agents)
methode/aide.md             →  /aide, and the command list in README.md and METHODE.md
Edit only methode/; run `./pq adapters` after any change."""
import os, re, glob, shutil
import yaml
from .model import REPO, parse_file

HEADER = "<!-- GÉNÉRÉ par `./pq adapters` depuis {src} : ne pas modifier ici, modifier {src}. -->\n\n"


def _front(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000) + "---\n"


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


AIDE_RE = re.compile(r"<!-- aide:debut -->.*?<!-- aide:fin -->", re.S)


def aide_text():
    """methode/aide.md without its title: the single source of the command list."""
    with open(os.path.join(REPO, "methode", "aide.md"), encoding="utf-8") as f:
        return f.read().split("\n", 1)[1].strip()


def sync_docs():
    """Copy the command list into README.md and METHODE.md between the aide markers."""
    block = "<!-- aide:debut -->\n" + aide_text() + "\n<!-- aide:fin -->"
    for name in ("README.md", "METHODE.md"):
        p = os.path.join(REPO, name)
        with open(p, encoding="utf-8") as f:
            s = f.read()
        if AIDE_RE.search(s):
            with open(p, "w", encoding="utf-8") as f:
                f.write(AIDE_RE.sub(lambda m: block, s))


def run():
    sync_docs()
    for d in (".claude/skills", ".claude/agents", ".opencode/commands", ".opencode/agents"):
        p = os.path.join(REPO, d)
        if os.path.isdir(p):
            shutil.rmtree(p)
    n = 0
    for src in sorted(glob.glob(os.path.join(REPO, "methode", "commandes", "*.md"))):
        name = os.path.splitext(os.path.basename(src))[0]
        meta, body = parse_file(src)
        body = body.replace("{{AIDE}}", aide_text())
        rel = os.path.relpath(src, REPO)
        head = HEADER.format(src=rel)
        claude = {"name": name, "description": meta["description"]}
        if meta.get("argument"):
            claude["argument-hint"] = meta["argument"]
        _write(os.path.join(REPO, ".claude", "skills", name, "SKILL.md"), _front(claude) + head + body)
        _write(os.path.join(REPO, ".opencode", "commands", f"{name}.md"),
               _front({"description": meta["description"]}) + head + body)
        n += 1
    r = 0
    for src in sorted(glob.glob(os.path.join(REPO, "methode", "roles", "*.md"))):
        name = os.path.splitext(os.path.basename(src))[0]
        meta, body = parse_file(src)
        head = HEADER.format(src=os.path.relpath(src, REPO))
        _write(os.path.join(REPO, ".claude", "agents", f"{name}.md"),
               _front({"name": name, "description": meta["description"]}) + head + body)
        _write(os.path.join(REPO, ".opencode", "agents", f"{name}.md"),
               _front({"description": meta["description"], "mode": "subagent"}) + head + body)
        r += 1
    print(f"{n} commande(s) et {r} rôle(s) générés pour Claude Code (.claude/) et OpenCode (.opencode/).")
