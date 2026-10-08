"""pq — outil en ligne de commande de Perroquet. Usage : ./pq <commande> [options]  (./pq -h)"""
import argparse, os, subprocess, sys, webbrowser
from .model import Base, REPO


def cmd_check(args, audit=False):
    from .check import check
    rep = check(Base())
    errs, warns = rep.errors(), rep.warnings()
    for e in errs:
        print(f"ERREUR  {e['fichier']} : {e['message']}")
    if audit or args.verbose:
        for w in warns:
            print(f"AVERT.  {w['fichier']} : {w['message']}")
    print(f"\n{len(errs)} erreur(s), {len(warns)} avertissement(s)" + ("" if audit or args.verbose else " (./pq audit pour les voir)"))
    return 1 if errs else 0


def cmd_sync(args):
    def git(*a, check=True):
        return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True, check=check)
    git("add", "-A")
    if cmd_check(args) and not args.force:
        print("Synchronisation annulée : corriger les erreurs (ou --force).")
        return 1
    if git("diff", "--cached", "--quiet", check=False).returncode:
        changed = git("diff", "--cached", "--name-only").stdout.split()
        msg = args.message or f"Recherche : {len(changed)} fichier(s) — " + ", ".join(os.path.basename(c)[:-3] for c in changed[:6])
        git("commit", "-m", msg)
        print(f"Commit : {msg}")
    remote = git("remote", check=False).stdout.strip()
    if not remote:
        print("Pas de dépôt distant configuré : commit local seulement.")
        return 0
    p = git("pull", "--rebase", "--autostash", check=False)
    if p.returncode:
        print(p.stdout + p.stderr)
        print("Conflit pendant la fusion : demandez à l'agent de le résoudre (git status).")
        return 1
    print("Récupéré : " + (p.stdout.strip().splitlines()[-1] if p.stdout.strip() else "à jour"))
    q = git("push", check=False)
    print("Envoyé." if q.returncode == 0 else q.stderr)
    cmd_check(args)
    return q.returncode


def main(argv=None):
    ap = argparse.ArgumentParser(prog="pq", description="Perroquet : base de recherche historique.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check", help="valider la base (erreurs bloquantes)"); p.add_argument("-v", "--verbose", action="store_true")
    p = sub.add_parser("audit", help="validation + avertissements de méthode"); p.add_argument("-v", "--verbose", action="store_true")
    p = sub.add_parser("build", help="générer le site HTML dans site/"); p.add_argument("--publish", action="store_true", help="version pour lien claude.ai (site_publish/)")
    sub.add_parser("view", help="générer et ouvrir le site")
    p = sub.add_parser("score", help="scores ACH d'une ou toutes les questions"); p.add_argument("ids", nargs="*")
    p = sub.add_parser("search", help="chercher dans Gallica / archive.org / fichiers locaux (consigné)")
    p.add_argument("outil", choices=["gallica", "gallica-texte", "archive", "archive-texte", "local"])
    p.add_argument("termes", nargs="+")
    p.add_argument("--index", default="gallica", help="index SRU Gallica : gallica, text, dc.title, dc.creator…")
    p.add_argument("--cql", help="requête CQL Gallica brute")
    p.add_argument("--max", type=int, default=20)
    p.add_argument("--hyp", help="id de la question concernée")
    p.add_argument("--objet", help="objet de la recherche, en clair")
    p.add_argument("--no-log", action="store_true", help="ne pas consigner (exploration)")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("fetch", help="télécharger les fichiers lourds manquants dans cache/")
    p.add_argument("sources", nargs="*"); p.add_argument("--status", action="store_true"); p.add_argument("--verifier", action="store_true")
    p = sub.add_parser("hash", help="empreinte sha256 d'un fichier"); p.add_argument("chemin")
    p = sub.add_parser("fiche", help="créer une fiche")
    p.add_argument("type"); p.add_argument("nom"); p.add_argument("--id"); p.add_argument("--force", action="store_true")
    sub.add_parser("adapters", help="régénérer les commandes pour Claude Code et OpenCode")
    sub.add_parser("aide", help="liste des commandes à taper dans l'agent")
    p = sub.add_parser("sync", help="valider, commit, pull --rebase, push")
    p.add_argument("-m", "--message"); p.add_argument("--force", action="store_true"); p.add_argument("-v", "--verbose", action="store_true")
    sub.add_parser("stats", help="chiffres de la base")
    args = ap.parse_args(argv)

    if args.cmd == "check":
        return cmd_check(args)
    if args.cmd == "audit":
        return cmd_check(args, audit=True)
    if args.cmd in ("build", "view"):
        from .build import build
        out = build(Base(), publish=getattr(args, "publish", False))
        if args.cmd == "view":
            webbrowser.open("file://" + os.path.join(out, "index.html"))
        return 0
    if args.cmd == "score":
        from .ach import format_score
        b = Base()
        for fi in b.of_type("hypothese"):
            if not args.ids or fi.id in args.ids:
                print(format_score(b, fi) + "\n")
        return 0
    if args.cmd == "search":
        from .search import run
        run(args); return 0
    if args.cmd == "fetch":
        from .fetch import run
        run(Base(), args); return 0
    if args.cmd == "hash":
        from .fetch import sha256
        print(sha256(args.chemin)); return 0
    if args.cmd == "fiche":
        from .fiche import run
        run(Base(), args); return 0
    if args.cmd == "aide":
        from .adapters import aide_text
        print(aide_text()); return 0
    if args.cmd == "adapters":
        from .adapters import run
        run(); return 0
    if args.cmd == "sync":
        return cmd_sync(args)
    if args.cmd == "stats":
        b = Base()
        for t in b.schema.types:
            print(f"{t:12} {len(b.of_type(t))}")
        print(f"{'assertions':12} {len(b.claims)}")
        print(f"{'relations':12} {len(b.edges())}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
