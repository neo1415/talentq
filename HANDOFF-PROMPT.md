You're taking over Talent Q from a previous Claude session in another account. Nothing from that account carries over except what's on GitHub, so read before you build.

## What Talent Q is

Talent Q is evidence-first hiring. Candidates are judged on proof of work, not on how polished their CV is. Q is the one AI assistant behind the whole product: one conversational interface on every page, for employers, agencies and candidates. It's proactive, remembers things, asks for approval before it acts, and works by voice, text or form. Its runtime comes from Capital Q (`neo1415/q`), a separate product by the same founder.

## Where everything is

1. **`neo1415/neo`, branch `claude/blissful-allen-0jweaf`, folder `talent-q-design/`.** The finished product and design blueprint lives here:
   - a clickable React, TypeScript and Vite prototype (`prototype/`);
   - specs, registers and the design system;
   - engineering handoff (`handoff/`);
   - tests (`qa/scripts/`);
   - films (`captures/films/`).
   Work on that branch; don't open a pull request unless asked.
2. **`neo1415/talentq`, the archive.** It holds the full history of the previous session:
   - `conversation/YOUR-MESSAGES.md` is every message the founder sent, in order. **Read all of it.** It's the source of truth for what was asked and decided.
   - `conversation/readable/MAIN-CONVERSATION.md` is the whole conversation; search it when you need detail.
   - `founder-uploads/` holds the founder's original briefs, atlases and addenda.
   - `artifacts/` holds copies of the published pages, including the review gallery. The old `claude.ai/artifact` links will stop working.
3. **`neo1415/q`, Capital Q.** It's read-only: do not change it unless the founder explicitly says so.

## Read these first, in order

1. `talent-q-design/PRODUCT-DEFINITION-PACKAGE.md`: the index, coverage and known weaknesses.
2. `neo1415/talentq/conversation/YOUR-MESSAGES.md`.
3. `talent-q-design/handoff/PRODUCTION-VERTICAL-SLICE.md`. It covers how Talent Q consumes Capital Q's runtime, the entities, events and migrations, and in §8 the first ten build tasks.
4. `talent-q-design/handoff/DECISION-REGISTER.md` and `handoff/CONSOLIDATION-MERGE-LEDGER.md`: the decisions already made. Don't reopen them.
5. `talent-q-design/handoff/MODULE-MAP-AND-ROADMAP.md`, `Q-INTELLIGENCE-SPEC.md` and `PRIVACY-AND-PERMISSIONS.md`.

## Where things stand (as of 2 November 2026)

The product and design blueprint is finished and delivered:
- **Screens:** all 183 screen concepts are represented, 82 as their own pages and 101 as states or sections.
- **Motions:** all 57 are built, each with a reduced-motion version.
- **Vision groups:** all 41 founder vision groups are covered.
- **Tests:** 27 test suites all passed on one build. That's 12 journeys (R1–R5, T1–T5, J11, J12), the privacy suite, the quality gates and 13 feature suites.
- **Films:** master films A (recruiter) and B (candidate) exist for desktop and phone.

The founder's rule was: **finish the blueprint first, then build the real app.** The blueprint is done, so the next phase is the production build. Before writing production code (database, tenancy, API, backend, workers, infrastructure), confirm with the founder that they accept the blueprint and want to start. If they do, begin with task 1 in `PRODUCTION-VERTICAL-SLICE.md` §8.

## Open items the founder may raise

- **LinkedIn import.** It was discussed but not designed. Sign in with LinkedIn gives only name, email and photo. Full-profile APIs need LinkedIn's partner approval, or are limited to EU members. The suggested path is that the candidate uploads LinkedIn's own data export (Settings → Get a copy of your data) and Q turns each claim into evidence marked as self-reported until proven. Adding it to onboarding and the Passport was offered but not yet approved.
- **Known weaknesses** (listed in the package):
  - Q's search is rule-based, not semantic.
  - Exercises, sends, payments and calendar writes are simulated.
  - The Passport preview still shows the old "Verified" tag.
  - WhatsApp messages sit beside the thread rather than inside it.
  - Some meters are seeded.
  - There has been no screen-reader or real-user testing.

## Working rules the founder set

- **No real sends, payments or calendar writes in the prototype.** Simulate them and label them as simulated.
- **No duplicate modules and no second Q brain.** Extend what exists.
- **Use the design skills for interface work** (interaction-design, design-critique, ux-writing, design-elevation, accessibility-audit, dataviz) and record them honestly in `DESIGN-SKILL-AUDIT.md`. Never claim a skill you didn't invoke.
- **Run the tests after any change.** The suites must stay green.
- **Commit and push finished work.** Keep model names out of the repository.
- **Report plainly.** Say what's done, what isn't and what's simulated.

## Running it

```bash
cd talent-q-design/prototype && npm install && npm run build && npm run preview   # serves on :4174
# Open any page as any person: http://localhost:4174/#/<route>?as=<actorId>
bash ../qa/scripts/journeys/run-all.sh http://localhost:4174/                      # R1–R5, T1–T5
node ../qa/scripts/journeys/J11.mjs; node ../qa/scripts/journeys/J12.mjs          # check each script's header for how it takes the address
# Feature suites are in qa/scripts/features/, gates in qa/scripts/gates/
```

Start by reading the files above. Then reply to the founder with a short summary of where things stand and what you propose to do first, and wait for their go-ahead before starting the production build.
