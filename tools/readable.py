# Turns a Claude Code session transcript (.jsonl) into a readable Markdown conversation.
# Keeps user messages and Claude's replies in full; tool calls as one line each; tool results trimmed; images dropped.
import json, sys
src, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
def clip(s, n): s = s.strip(); return s if len(s) <= n else s[:n] + f"\n… [{len(s)-n} more characters trimmed]"
lines = [f"# {title}", "", f"Source: `{src.split('/')[-1]}`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.", ""]
for raw in open(src, encoding="utf-8"):
    try: e = json.loads(raw)
    except Exception: continue
    t = e.get("type")
    if t == "summary" or (t == "user" and e.get("isCompactSummary")):
        c = e.get("message", {}).get("content") if t == "user" else e.get("summary")
        if isinstance(c, list): c = " ".join(b.get("text", "") for b in c if isinstance(b, dict))
        lines += ["", "---", f"### Context summary ({e.get('timestamp','')[:16]})", "", clip(str(c), 20000), ""]; continue
    if t not in ("user", "assistant"): continue
    m = e.get("message", {}); c = m.get("content"); ts = e.get("timestamp", "")[:16].replace("T", " ")
    blocks = [{"type": "text", "text": c}] if isinstance(c, str) else (c or [])
    for b in blocks:
        if not isinstance(b, dict): continue
        bt = b.get("type")
        if bt == "text" and b.get("text", "").strip():
            who = "User" if t == "user" else "Claude"
            txt = b["text"]
            if t == "user" and txt.lstrip().startswith("<system-reminder>"): continue
            lines += ["", f"**{who}** · {ts}", "", txt.strip() if who == "Claude" else clip(txt, 30000), ""]
        elif bt == "tool_use":
            inp = b.get("input", {}); d = inp.get("description") or inp.get("command") or inp.get("file_path") or inp.get("prompt") or inp.get("query") or json.dumps(inp)[:200]
            lines.append(f"- 🔧 `{b.get('name')}`: {clip(str(d).replace(chr(10),' '), 300)}")
        elif bt == "tool_result":
            rc = b.get("content")
            if isinstance(rc, list): rc = "\n".join(x.get("text", "[image]") if isinstance(x, dict) else str(x) for x in rc)
            rc = str(rc or "")
            if rc.strip(): lines += ["", "  <details><summary>result</summary>", "", "```", clip(rc, 1500).replace("```", "ʼʼʼ"), "```", "  </details>", ""]
open(out, "w", encoding="utf-8").write("\n".join(lines))
