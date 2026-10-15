"""Client for the sweet-bnf MCP server (Gallica API wrapper), usable from the shell by any agent:

  pq bnf <outil> '<arguments JSON>'
  pq bnf outils                                  list the tools and their arguments

Useful tools: advanced_search {query, max_results, start_record} (CQL), search_by_title, get_item_details {ark},
get_item_pages {ark, page_range}, get_page_text {ark, page} (OCR of one page), get_page_image {ark, page, size}.
It goes through Gallica too: when Gallica blocks us, this server is refused as well."""
import json
import requests

URL = "https://sweet-bnf.vercel.app/message"
HEAD = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}


def rpc(method, params=None):
    r = requests.post(URL, headers=HEAD, timeout=120,
                      json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}})
    r.raise_for_status()
    out = r.json()
    if "error" in out:
        raise RuntimeError(json.dumps(out["error"], ensure_ascii=False))
    return out["result"]


def call(tool, args):
    res = rpc("tools/call", {"name": tool, "arguments": args})
    return "\n".join(c.get("text", "") for c in res.get("content", []))


def run(args):
    if args.outil == "outils":
        for t in rpc("tools/list")["tools"]:
            props = ", ".join(t.get("inputSchema", {}).get("properties", {}))
            print(f"{t['name']}({props}) — {t.get('description', '').splitlines()[0][:110]}")
        return 0
    text = call(args.outil, json.loads(args.json or "{}"))
    print(text)
    return 2 if "403" in text[:200] and "blocked" in text[:200].lower() else 0
