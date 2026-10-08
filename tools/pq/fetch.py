"""Large files (scans, PDFs) are never in git. Each source lists them under `fichiers:`
  - {chemin: cache/…, url: …, sha256: …, recuperation: auto|manuel, note: …}
`pq fetch` downloads the missing `auto` files and prints instructions for the `manuel` ones."""
import os, time, hashlib
import requests
from .model import REPO, as_list
from .search import UA


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url, path, tries=3):
    for i in range(tries):
        try:
            with requests.get(url, headers=UA, stream=True, timeout=600) as r:
                r.raise_for_status()
                with open(path + ".part", "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            os.replace(path + ".part", path)
            return
        except Exception:
            if os.path.exists(path + ".part"):
                os.remove(path + ".part")
            if i == tries - 1:
                raise
            time.sleep(3 * (i + 1))


def entries(base, only=None):
    for fi in base.of_type("source"):
        if only and fi.id not in only:
            continue
        for e in as_list(fi.get("fichiers")):
            if isinstance(e, dict) and e.get("chemin"):
                yield fi, e


def run(base, args):
    missing_manual, failed = [], []
    n_ok = n_dl = 0
    for fi, e in entries(base, args.sources or None):
        path = os.path.join(REPO, e["chemin"])
        if os.path.exists(path):
            n_ok += 1
            if args.verifier and e.get("sha256") and sha256(path) != e["sha256"]:
                print(f"! {e['chemin']} : empreinte sha256 différente")
            continue
        if e.get("recuperation") == "auto" and e.get("url"):
            if args.status:
                print(f"- manquant (auto) {e['chemin']}  ← {e['url']}")
                continue
            print(f"↓ {e['chemin']}  ← {e['url']}")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            try:
                download(e["url"], path)
            except Exception as err:
                print(f"  ! échec : {err}")
                failed.append((fi, e, err))
                continue
            if e.get("sha256") and sha256(path) != e["sha256"]:
                print("  (empreinte différente de celle enregistrée : autre résolution ou fichier modifié)")
            n_dl += 1
        else:
            missing_manual.append((fi, e))
    print(f"{n_ok} fichier(s) présent(s), {n_dl} téléchargé(s), {len(failed)} échec(s), {len(missing_manual)} à récupérer à la main.")
    for fi, e, err in failed:
        print(f"\n• échec {e['chemin']} (source : {fi.id}) — réessayer plus tard : ./pq fetch {fi.id}")
    for fi, e in missing_manual:
        print(f"\n• {e['chemin']}  (source : {fi.id})")
        if e.get("url"):
            print(f"  page : {e['url']}")
        if e.get("note"):
            print(f"  {e['note']}")
