# Lists the user's own messages from a session transcript, including ones sent while Claude was mid-turn.
import json, sys
msgs = {}
skip = ("<", "Stop hook", "This session is being continued", "[Request interrupted")
for raw in open(sys.argv[1], encoding="utf-8"):
    try: e = json.loads(raw)
    except Exception: continue
    s = None
    if e.get("type") == "queue-operation" and e.get("operation") == "enqueue" and isinstance(e.get("content"), str): s = e["content"]
    elif e.get("type") == "user" and not (e.get("isMeta") or e.get("isCompactSummary") or e.get("isSidechain")):
        c = e.get("message", {}).get("content")
        s = c if isinstance(c, str) else " ".join(b.get("text","") for b in (c or []) if isinstance(b, dict) and b.get("type") == "text")
    s = (s or "").strip()
    if not s or s.startswith(skip) or "stop hook" in s[:200].lower(): continue
    msgs.setdefault(s, e.get("timestamp", ""))
out = ["# Every message you sent in this conversation", "", "Only your own words, in order, without Claude's replies or automatic notices. The full conversation is in `readable/MAIN-CONVERSATION.md`.", ""]
for s, ts in sorted(msgs.items(), key=lambda kv: kv[1]): out += [f"## {ts[:16].replace('T',' ')} UTC", "", s, ""]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out)); print(len(msgs))
