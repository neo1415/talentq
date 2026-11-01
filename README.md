# Talent Q archive

This is everything from the Claude Code session that produced the Talent Q product and design blueprint (26 October – 1 November 2026). It's here so the work can carry on from a different Claude account that has none of this history.

The code, specs, tests and films are **not** copied here. They're in the repository **`neo1415/neo`** on branch **`claude/blissful-allen-0jweaf`**, in the folder `talent-q-design/`. Start with `talent-q-design/PRODUCT-DEFINITION-PACKAGE.md` there.

## What's in this archive

| Folder | What it is |
|---|---|
| `conversation/YOUR-MESSAGES.md` | Every message you sent, in order, and nothing else. It's the quickest way to recall what was asked and decided. |
| `conversation/readable/MAIN-CONVERSATION.md` | The whole conversation as readable text: your messages, Claude's replies, one line per tool call and the start of each tool result. |
| `conversation/readable/subagents/` | The same for each of the 29 helper agents. Each file's title says what that agent built. |
| `conversation/raw/` | The original session files, untouched (main transcript, helper agents and saved tool outputs), compressed and split into parts under GitHub's 100 MB limit. |
| `artifacts/talent-q-design-review/` | The published review gallery. Open `index.html`; it works offline. |
| `artifacts/talent-q-directions/` | The page comparing directions A, B, C and D. |
| `artifacts/talent-q-design-directions-canvas/` | The early design canvas: three directions, desktop and phone. The `project/*.dc.html` files hold the content. |
| `artifacts/other-projects/` | The other ten pages published from this Claude account (SongScribe, Capital Q, NEM, salvage, Tavus). Two were Claude Docs and are saved as Markdown. |
| `founder-uploads/` | Every file you uploaded during the session: briefs, atlases, addenda and the 30 October build pack. |

## Restoring the raw transcripts

```bash
cat conversation/raw/session-transcripts.tar.xz.part-* | xz -d | tar -x
```

This recreates the folder `-home-user-neo/`. It holds `<session-id>.jsonl` (the main conversation) and `<session-id>/subagents/*.jsonl` (the helper agents). Those are standard Claude Code transcript files.

## Picking the work up in a new account

1. Connect GitHub in the new Claude account and give it access to `neo1415/neo` and this repository.
2. Start a session on `neo1415/neo`, branch `claude/blissful-allen-0jweaf`.
3. Tell Claude to read, in this order:
   - `talent-q-design/PRODUCT-DEFINITION-PACKAGE.md`;
   - `talent-q-design/handoff/PRODUCTION-VERTICAL-SLICE.md`, whose §8 lists the first ten build tasks;
   - `conversation/YOUR-MESSAGES.md` from this archive.
4. The published pages from the old account stop working once it closes. The copies here are the record:

| Page | Old link |
|---|---|
| Talent Q Design Review | https://claude.ai/artifact/BAb3TPDkQFaq6qBHVCHxGn |
| Talent Q Directions | https://claude.ai/artifact/G8kYmDwwdE4b3jUeTTC9Dd |
| Talent Q Design Directions (canvas) | https://claude.ai/artifact/MmkpWffDt1d8FhAR9kTFZc |

## Privacy

The transcripts include your email address, file paths and the full text of every document you uploaded. Keep this repository private. No access keys or passwords were found: a scan matched only random strings inside embedded images.
