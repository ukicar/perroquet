"""Generate agent-specific wrappers from the agent-neutral procedures in methode/.

methode/commandes/<cmd>.md  →  .claude/skills/<cmd>/SKILL.md   (Claude Code)
                               .opencode/commands/<cmd>.md     (OpenCode)
methode/roles/<role>.md     →  .claude/agents/<role>.md        (Claude Code sub-agents)
                               .opencode/agents/<role>.md      (OpenCode sub-agents)
Edit only methode/; run `./pq adapters` after any change."""
import os, glob, shutil
import yaml
from .model import REPO, parse_file

HEADER = "<!-- GÉNÉRÉ par `./pq adapters` depuis {src} : ne pas modifier ici, modifier {src}. -->\n\n"


def _front(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000) + "---\n"


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run():
    for d in (".claude/skills", ".claude/agents", ".opencode/commands", ".opencode/agents"):
        p = os.path.join(REPO, d)
        if os.path.isdir(p):
            shutil.rmtree(p)
    n = 0
    for src in sorted(glob.glob(os.path.join(REPO, "methode", "commandes", "*.md"))):
        name = os.path.splitext(os.path.basename(src))[0]
        meta, body = parse_file(src)
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
