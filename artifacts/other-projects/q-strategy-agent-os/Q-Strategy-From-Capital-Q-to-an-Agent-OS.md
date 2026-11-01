# Q Strategy: From Capital Q to an Agent OS

Oct 11, 2026 · @Ademola Daniel

## Executive summary

Q is already a live, unusually well-governed AI runtime; adding the 12 Craft engines lets it do real professional work on real files, and generalising it turns it into the kernel of an Agent OS where anyone — even a 15-year-old with a guardian — can build and run a business. The path costs little money for the first two months and most of its risk is fixable this week.

### Where Q stands

- **Live and real.** Capital Q runs on Railway with 109 tools, \~143 approval-governed actions, voice, a meeting bot, a document studio and a bounded agent workforce; the investor demo passed end to end on 11 October.
- **Strong brakes, weak hands.** Its safety machinery (context firewall, approval engine bound to exact payloads, audit, spend caps) is its best asset. It cannot yet read spreadsheet formulas or scanned PDFs, exports documents only as PDF, and is closed to outside tools.
- **One domain.** Everything is wired to private capital; that is a focus today and a ceiling tomorrow.

### The three moves

1. **Supercharge Capital Q (weeks).** Plug GridCraft and PDFCraft into Q's existing sandbox: recalculated financial models, OCR, data-room integrity checks, editable Word and Excel outputs. Both engines are proven here: GridCraft matched an independent IRR calculation to about 13 significant digits.
2. **Make Q a platform (months).** Close the security gaps, wire the driver interface, replace finance-only enums with loadable domain packs, and let the agent-workforce project plug in as governed agents.
3. **Build the Agent OS (within a year).** One country, one regulation pack reviewed by lawyers, guardian accounts for minors, business blueprints and a partner marketplace for the steps the law reserves for humans.

### What it takes

- **Quick wins:** six, all CPU-only or switch-on work (repo lock-down, model formulas, OCR, data-room checks, Word exports, payments).
- **Big bets:** multi-domain kernel, autonomous workforce, Agent OS first market.
- **What costs money:** AI usage (the largest variable cost), KYC checks, payment fees, legal opinions per market, licensed partners, a penetration test, and people. The Craft engines are free (MIT/Apache) and need no GPUs for documents.
- **What to fix first:** the Q repository is public and contains real user interview transcripts and personal email addresses, and database traffic bypasses row-level security. Both must be closed before any expansion.

### Decisions needed

- Make the Q repository private (or purge it) this week.
- Pick the Agent OS's first market and its legal partner.
- Confirm Capital Q's prices and switch on payments, including a local rail for Nigeria.

## What Q is today

Q is a live, governed AI runtime with unusually strong safety machinery, wrapped around one domain: private capital. Its brakes are better than its engine — governance scores 4.5 of 5 as an OS kernel, while connectors (2) and autonomy (2.5) are the weakest parts. Assessed from `neo1415/q` branch `build/int-rc` at commit `668ee838` (11 October 2026), the branch that deploys; `main` is 2,793 commits behind.

### The product

- **CapitalQ by FDN Capital Partners**: 'AI-native investment intelligence operating system for private capital', for founders, investors and fund teams in Nigeria, the UK/Europe and the Gulf.
- **Live on Railway** (web, api, q-api, workers) with 201 database migrations; the cold investor demo (Discover → open → explain → compare) passed end to end on 11 October.
- **Built surfaces**: Q-led onboarding by text and voice, discovery and fit ranking, company research, readiness, data room, capital rounds, deal tracking, a meeting bot that joins Google Meet, pitch rehearsals with AI personas, the 'Q room' with voice, a daily briefing, a personal morning newspaper, a documents studio (decks, one-pagers, memos), GateQ investor intake, profiles and an operator console.
- **Billing built, not switched on**: Founder Pro, Investor Pro and Fund plans exist with feature gates; Stripe is off and there is no local payment rail.

### The brain

| Part | What it does | Where |
| --- | --- | --- |
| **Run engine** | Every request becomes a run: firewall → retrieval → answer → prepare action → human approval, checkpointed in Postgres and streamed live | q-runtime, q-orchestrator |
| **Context firewall** | Decides what each run may see before any model call | q-firewall |
| **Tools** | 109 typed tools plus generated ones, offered per turn (up to 127), 2 rounds and 10 calls a turn | q-tools, model-gateway |
| **Actions** | \~143 declared app actions; 103 require human approval, bound to a hash of the exact payload | app-actions, q-actions |
| **Workforce** | A lead Q plans bounded jobs for roles with USD budgets; 6 roles have executors | q-orchestrator/workforce |
| **Standing instructions** | Q acts on its own on schedules and events, inside hard limits (10 sends a day, unsend window) | instructions |
| **Knowledge** | Hybrid search, versioned facts, contradictions, a memory notebook | q-knowledge |
| **Research** | Bounded web research with source tracking and injection scanning | q-research |
| **Models** | OpenAI primary, Gemini and Groq fallback; per-request budgets, daily spend caps, usage ledger | model-gateway |
| **Senses** | Voice in/out, screen vision in meetings, document parsing in a sandbox, image generation | q-api voice, workers, deck-render |
| **Quality** | \~10,200 tests, 132 database tests, CI on format/lint/types/tests; evals exist but are not in CI | q-evals, CI |

&#91;embedded content: kernel readiness scores · code review of neo1415/q build/int-rc @ 668ee838\]

The two lowest scores are exactly what the Craft engines and the agent-workforce project need: a wired driver interface and real autonomy.

### Where vision and code part

1. **The autonomous workforce has not started as a slice**: the plan exists; DOCUMENTS, WRITER and DILIGENCE roles lack real executors.
2. **Q often has little to say**: deck extractions and embeddings were at zero live on 7 October; there is no approved scoring methodology for InvestIQ yet.
3. **It is closed to the outside**: an MCP client exists but nothing uses it, the MCP server is off, and integrations stop at Google, Recall and Cloudflare.
4. **It cannot work on real files**: spreadsheet formulas are never evaluated, there is no OCR, documents export as PDF only, no artifact events stream to the user.
5. **It is wired to one domain**: subject kinds, firewall task classes, knowledge scopes and workforce roles all name companies, investors and capital.
6. **It is not yet hardened**: database traffic bypasses row-level security, orchestration runs inside the API process, a single replica holds in-memory state, and three 4,500–6,500-line files carry most of the logic.

## The asset base

You already hold three of the four pieces an agent platform needs: a governed brain (Q), a full suite of headless production engines (the 12 Craft apps), and a planned agent workforce. The missing piece is the layer that lets them work together.

| Asset | What it is | What it contributes | State today |
| --- | --- | --- | --- |
| **Q (Capital Q repo, `neo1415/q`)** | TypeScript monorepo: governed AI runtime + investment-intelligence product | The brain and the governance: identity, tenancy, context firewall, approval engine, audit, evidence, model gateway, evals | Live on Railway; 109 tools, \~143 approval-governed actions; private-capital only |
| **VectorCraft** | Illustrator-class vector editor | Logos, brand marks, icons, charts, print artwork | MCP verified working (logo built and exported) |
| **GridCraft** | Excel-class spreadsheet | Financial models, budgets, cap tables, forecasts | MCP verified working (NPV/IRR exact to reference) |
| **DeckCraft** | PowerPoint-class presentations | Pitch decks, board packs, investor updates | MCP implemented, upstream-tested |
| **WordCraft** | Word-class documents | Business plans, memos, policies, contracts drafts | MCP implemented, upstream-tested |
| **PDFCraft** | Acrobat-class PDF engine | Forms, filings, redaction, e-signature, compare, OCR | 145 MCP tools, strongest test suite |
| **DesignCraft** | InDesign-class layout | One-pagers, brochures, print-ready PDF/X | MCP implemented |
| **PhotoCraft / LightCraft** | Photoshop / Lightroom class | Product photos, team photos, social images | MCP implemented |
| **FilmCraft / EffectCraft** | Premiere / After Effects class | Pitch videos, ads, animated explainers, templated video | MCP implemented; heavy compute |
| **SoundCraft** | Pro Tools class | Voice-overs, podcast and ad audio | MCP implemented |
| **CADCraft** | AutoCAD class | Floor plans, product drawings, site layouts | MCP implemented |
| **artcraft (platform)** | Hosted AI generation (image, video, 3D) | Generative media via third-party models | Hosted API only; data leaves your control |
| **Agent-workforce project** | Agents organised as a company's departments | The 'employees' that run work end to end | Not yet integrated; treated here as a future module |

All 12 Craft apps are MIT OR Apache-2.0, run headless on a CPU, and expose MCP servers, so they can be used as production engines without licence fees. The ArtCraft name and logos are trademarks and cannot be used in your products.

## Making Capital Q a super beast

Capital Q already reads, ranks, interviews, meets and drafts; what it cannot yet do is work on real files the way a professional does. The Craft engines close exactly the gaps the codebase has today: spreadsheet formulas are never evaluated, scanned PDFs cannot be read (no OCR), documents export only as PDF, decks support four chart types, and nothing edits video.

### Use cases, by the gap they close

| Use case | Today in Capital Q | With the Craft engines | Engine | Effort |
| --- | --- | --- | --- | --- |
| **Read a founder's real financial model** | Reads cached cell values only; formulas ignored | Recalculates the model, checks the formulas, runs 'what if revenue grows 20% slower' | GridCraft (verified) | Low |
| **Read scanned decks and contracts** | No OCR; scanned pages contribute nothing | Text from scanned PDFs, so deck reading and diligence see every page | PDFCraft | Low |
| **Safe data-room sharing** | Data room shares files as uploaded | Before sharing: detect hidden metadata and fake redactions, redact for real, watermark per investor | PDFCraft | Low–medium |
| **Compare document versions** | Versions stored; no diff | 'What changed in the term sheet since Tuesday' as a marked-up PDF | PDFCraft | Low |
| **Editable investor memos** | Memos and briefs export as PDF only | Word files investors can edit and redline | WordCraft | Low |
| **Investor-grade financial outputs** | Results export as CSV | Real XLSX models: cap table, use of funds, projections with live formulas | GridCraft | Medium |
| **Richer decks** | Editable PPTX via pptxgenjs, 4 chart types | More chart kinds, native tables, print-ready PDF/X one-pagers | DeckCraft, DesignCraft | Medium |
| **Brand on day one** | Brand kit suggested from a website | Logo, colour system and brand guide generated as editable vector files | VectorCraft (verified), DesignCraft | Medium |
| **Pitch videos** | Uploads go to Cloudflare Stream as-is | 60-second templated pitch video with captions and voice-over, before upload | EffectCraft, FilmCraft, SoundCraft | High |
| **Forms and signatures** | KYB is manual | Pre-filled KYB and onboarding forms, signed PDFs | PDFCraft | Medium |

### Founder journey: 'get me investor-ready'

1. Kemi uploads her deck (scanned), her model (XLSX) and her incorporation documents.
2. Q reads every page (PDFCraft OCR), recalculates the model (GridCraft) and flags that her deck's growth figure does not match the model's formula.
3. Q's readiness check lists three blockers: no cap table, unclear use of funds, deck/model mismatch.
4. Kemi says 'fix it'. Q prepares a corrected model, a cap table and a use-of-funds sheet (GridCraft), a revised deck (DeckCraft) and a one-pager (DesignCraft). She approves each one.
5. Before her data room opens, Q strips hidden metadata and checks redactions (PDFCraft).
6. She rehearses with an AI investor persona; Q drafts a 60-second video version of her pitch for the gateway (EffectCraft).

### Investor journey: 'should we take this meeting?'

1. Tunde opens Discover and sees three companies that fit his mandate.
2. He asks Q to compare two. Q answers from evidence, recalculating each company's own model rather than trusting the deck's headline numbers.
3. He asks 'what changed since their last update?'. Q returns a redline of the new deck against the old (PDFCraft compare).
4. After the call (meeting brain), Q drafts an investment memo as an editable Word file and an IC deck with the company's real charts (WordCraft, DeckCraft). Tunde edits and shares with his partners.

### Fund journey: 'run our pipeline'

1. The fund publishes a GateQ gateway; applicants are interviewed and scored without the team lifting a finger.
2. Each qualified applicant arrives with a standardised pack: extracted financials, a recalculated model and a one-page summary (GridCraft, DesignCraft).
3. Every Monday, Q produces the pipeline report as a deck and a workbook; the partners approve it before it goes to the investment committee.

## Q beyond Capital Q

The same governed brain plus the Craft engines fits any business whose work ends in documents, numbers and media — which is most of them. The strongest next markets are the ones where Q's governance (evidence, approvals, audit) is itself the selling point.

| Domain | What Q would do | Craft engines used | Why Q wins | Regulatory sensitivity |
| --- | --- | --- | --- | --- |
| **Small-business back office** | Invoices, budgets, cash-flow forecasts, supplier contracts, monthly reports | GridCraft, WordCraft, PDFCraft | Daily briefing and standing instructions already track work and follow-ups | Medium (tax, consumer law) |
| **Accounting and advisory firms** | Client packs, management accounts, variance commentary, tax-form preparation | GridCraft, PDFCraft, WordCraft, DeckCraft | Evidence-linked numbers; human sign-off built in | High (professional standards) |
| **Law firms and in-house legal** | Contract comparison, redaction, bundles, filing forms, clause libraries | PDFCraft (compare, redact, forms, sign), WordCraft | PDFCraft's 145 tools cover most of Acrobat's legal workflow | High (privilege, confidentiality) |
| **Real estate and construction** | Floor plans, listing photos, brochures, valuation models, tender packs | CADCraft, LightCraft, DesignCraft, GridCraft | Few AI tools touch CAD at all | Medium |
| **Marketing and creative agencies** | Campaign assets end to end: brand, social, video, audio, print | All creative engines | One brief, every format, no Adobe seat costs | Low to medium (ad standards, IP) |
| **Education and training** | Courses: slides, workbooks, explainer videos, assessments | DeckCraft, WordCraft, EffectCraft, SoundCraft | Templated, repeatable production | Medium (minors' data) |
| **NGOs and public-sector suppliers** | Grant applications, tenders, compliance reports, impact decks | WordCraft, PDFCraft, DeckCraft, GridCraft | Evidence and audit trail suit funders and auditors | Medium (procurement rules) |
| **Founders outside fundraising** | Everything in the Agent OS journey | All | The feeder market for Capital Q | Varies; minors need guardians |

Healthcare, insurance underwriting and consumer lending are deliberately left out of the first wave: they carry the heaviest regulation and the highest cost of an AI error.

## Prioritised roadmap

Start with six quick wins that need almost no money and land in weeks: lock down the repo, then put GridCraft and PDFCraft behind Q's existing sandbox so Q can finally work on real files. Harden next, then take the big bets that turn Q into a platform.

&#91;embedded content: impact × effort assessment of 18 initiatives · from the repository analysis, 11 Oct 2026\]

The shaded corner holds the quick wins; everything right of the dashed line needs the hardening work (7–10) first.

| # | Initiative | What it costs money for | Depends on | Rough time (small team) |
| --- | --- | --- | --- | --- |
| 1 | Lock down public repo, rotate keys | Nothing beyond engineer time | — | Days |
| 2 | Evaluate model formulas (GridCraft, verified) | CPU only | Linux build + sandbox runner | 1–2 weeks |
| 3 | Data-room integrity check (PDFCraft) | CPU only | Same runner | 2 weeks |
| 4 | OCR for scanned files (PDFCraft) | CPU only; OCR model download | Same runner | 1–2 weeks |
| 5 | Word exports (WordCraft) | CPU only | — | 1–2 weeks |
| 6 | Switch on payments | Payment fees per transaction | Price decision, terms of service | 1–2 weeks |
| 7 | Row-level security in the request path | Nothing | ADR 0065 | 2–4 weeks |
| 8 | MCP client with stdio + approval executor | Nothing | 7 | 3–4 weeks |
| 9 | Artifact streaming and XLSX outputs | Nothing | Contract change | 2–3 weeks |
| 10 | KYC/KYB vendor | Per-check fees | Vendor choice | 3–4 weeks |
| 11 | Multi-domain kernel | Engineering team | 7, 8 | 2–3 months |
| 12 | Autonomous workforce executors | Model spend | 8, 9 | 2–3 months |
| 13 | Agent OS foundations (first market) | Legal opinions, partners | 10, 11, 12 | 4–6 months |
| 14 | Video pitch studio | Render workers | 9 | 1–2 months |

Times are rough engineering estimates, not commitments. Two things to avoid for now: CAD inside Capital Q (no fit with fundraising), and building your own payments or escrow (a regulated activity; Q's rule is that it never moves money).

## The Agent OS

The Agent OS is an operating system in the literal sense: it manages resources, isolates work, enforces permissions and gives every agent the same 'system calls' — except the resources are a business's money, documents, identity and legal obligations instead of CPU and disk. A 15-year-old types an idea; the OS turns it into a running business through governed agents, real production engines and licensed human partners at the points where the law requires a human.

### What 'OS' means here, part by part

| Classic OS concept | Agent OS equivalent | Built from |
| --- | --- | --- |
| Kernel | Governance runtime: identity, tenancy, permissions, approvals, audit, context firewall | Q's runtime (q-core, q-firewall, q-actions, audit) |
| Processes and scheduler | Agents and long-running jobs, queued, retried, time-boxed, killable | Q's orchestrator + worker queues; the agent-workforce project |
| System calls | Typed tools with declared risk, scope and approval rules | Q's tool and action registries |
| Device drivers | Production engines and outside services behind one interface | The 12 Craft engines (MCP), plus banks, registries, payments, email |
| File system | The business vault: every document, model, deck and decision, versioned and cited | Q's evidence and knowledge stores, Craft native formats |
| Memory | Business memory: facts, commitments, deadlines, relationships, with history | Q's knowledge store (versioned facts, memory notebook) and daily briefing |
| Security model | Capability-based permissions; humans approve anything consequential; guardians for minors | Q's approval engine, extended with guardian roles |
| Shell | Conversation, voice and a visual canvas that shows the business being built | Q's web app and presence layer |
| App store | 'Business blueprints': reusable playbooks for a bakery, a SaaS, an agency | New |
| Package manager | Versioned agents, tools and regulation packs per country | New |

### The 15-year-old founder journey

Amara, 15, wants to sell hand-made phone cases online. One evening she tells the OS her idea.

1. **Idea to plan (day 1).** A strategy agent asks ten questions, sizes the market from public data, and drafts a one-page plan (WordCraft) with the three biggest risks marked.
2. **The money (day 1).** A finance agent builds a unit-economics model and a 12-month budget (GridCraft): cost per case, price, break-even volume. Amara changes the price in plain words; the model recalculates live.
3. **Brand (day 2).** A brand agent proposes three names, checks domain and trademark availability, and draws logos (VectorCraft), product mock-ups (PhotoCraft) and a one-page brand guide (DesignCraft).
4. **Guardian gate (day 2).** Because Amara is a minor, the OS invites a parent or guardian. They review the plan and budget, and co-sign everything that creates an obligation. This is a hard gate, not a setting.
5. **Legal set-up (week 1).** A compliance agent assembles the country's 'regulation pack': the right business structure for her age and location, registration forms pre-filled (PDFCraft), tax registration steps, consumer-protection and data-privacy duties for an online shop. Filing goes through a licensed partner where the law requires one.
6. **Shop and payments (week 1).** An operations agent sets up the storefront, payment provider and bank account in the guardian's or the entity's name, with transaction limits.
7. **Launch (week 2).** A marketing agent produces social posts, a 15-second ad (EffectCraft templates, SoundCraft voice-over) and a launch calendar. Nothing is posted without Amara's approval.
8. **Running it (ongoing).** A daily briefing tells her what sold, what to reorder, which invoices are due and which deadline is next. Bookkeeping updates itself; the OS flags anything unusual.
9. **Growing it (month 6+).** When she wants to raise money, the OS hands her business record to Capital Q: a verified data room, a deck (DeckCraft), a financial model and introductions to suitable investors.

### Principles that make it safe enough for a teenager

- **The human decides, the OS prepares.** Every consequential step follows Q's existing rule: prepare, recommend, human approval, execute.
- **Age-aware by design.** Minor accounts carry a guardian role and hard limits on money, contracts and public posting.
- **Regulation as versioned data, not model memory.** Each country pack cites its laws, has an owner and a review date, and is checked by a licensed professional before release.
- **Show the working.** Every number traces to its source; every document keeps a version history.
- **Graduate to people.** The OS knows its limits and routes to accountants, lawyers and mentors rather than guessing.

## Agent OS architecture

The Agent OS is Q's runtime promoted to a kernel, the Craft engines and connectors as its drivers, and the agent workforce as its applications. Q already has most of the kernel; the work is making it domain-neutral, opening its driver interface, and moving long work out of the API process.

&#91;embedded content: Agent OS reference architecture · 6 layers\]

Agents never call drivers directly: every call goes through the kernel, which checks scope, budget and approval and writes the audit record.

### How one request flows

1. Amara says 'make me a budget for the case business'.
2. The shell sends it to the kernel as a run; the firewall decides which parts of the business vault the run may read.
3. The lead agent plans: the finance agent builds the model, the writer agent explains it.
4. The finance agent calls GridCraft through the driver interface; the kernel checks the tool's scope and the agent's budget, then runs the engine in a sandbox with only the job folder mounted.
5. The result (an XLSX and a summary) lands in the vault, versioned, and streams to the canvas as an artifact event.
6. Nothing has left the business yet, so no approval is needed. Sending the budget to a bank would be a consequential action and stop at the approval gate, with the guardian co-signing.

### Where each repo fits

| Repo / package | OS layer | Role |
| --- | --- | --- |
| `q` — q-runtime, q-orchestrator, q-firewall, q-actions, app-actions, audit, permissions, model-gateway, q-evals | Kernel | Runs, permissions, approvals, audit, model routing, quality gates |
| `q` — q-knowledge, evidence, q-research, billing, verification, q-daily, workers queues | System services | Vault, memory, research, billing, identity, scheduling |
| `q` — apps/web, voice, q-artifacts, deck-render | Shell | Conversation, voice, canvas, document studio |
| `q` — q-connectors, integrations | Driver interface | MCP client and server, Google, mail |
| `gridcraft`, `deckcraft`, `wordcraft`, `pdfcraft`, `designcraft`, `vectorcraft` | Drivers (documents) | The business's numbers, decks, documents, forms and brand |
| `photocraft`, `lightcraft`, `filmcraft`, `effectcraft`, `soundcraft` | Drivers (media) | Marketing images, video and audio, as queued jobs |
| `cadcraft` | Driver (drawings) | Floor plans and product drawings for physical businesses |
| `craft-launcher`, `craft-libs`, `craft-fonts` | Build inputs | Packaging, shared UI, fonts for the engines |
| `artcraft`, `artcraftx`, `cloud-worker` | Optional generative service | Image and video generation via hosted models; data leaves your control |
| Agent-workforce project | Agents and apps | The departments: finance, legal, marketing, operations, sales |

### What must change in Q to become the kernel

1. **Domain packs instead of enums.** Move subject kinds, firewall task classes, knowledge scopes, workforce roles and prompts into loadable packs ('capital', 'small business', 'legal'), so Capital Q becomes the first pack, not the whole system.
2. **A driver interface that is actually wired.** Add stdio transport to the MCP client, compose it in the API, and give the approval engine an MCP executor so drivers can write after approval.
3. **Runtime registration of tools and agents.** Today everything is compiled in; an OS needs installable, versioned, signed tools and agents.
4. **Orchestration out of the API process.** Run the graph on workers with durable state; remove the in-memory conversation maps and the single-replica assumption.
5. **Artifacts as first-class events.** A stream event for created and updated artifacts, so the canvas shows work as it happens.
6. **Guardian and partner roles.** New actor types in permissions and approvals: a guardian who co-signs, a licensed partner who reviews.
7. **Split the three 4,500–6,500-line files** (`answer.ts`, the model-gateway loop, `main.ts`) before more teams build on them.

### The contract with the agent-workforce project

When you integrate the workforce project, it should plug in as agents, not as a second brain: each agent declares its role, the tools it needs, its budget and its approval rules; Q's kernel enforces them. That keeps one audit trail, one permission model and one place where humans approve.

## Security, legal and regulatory risks

The biggest risk today is not the AI — it is that the `neo1415/q` repository is public and holds personal data and production details. Fix that first; then close the tenant-isolation gap before adding any tool that writes.

### Act now (this week)

| Risk | What was found | Action |
| --- | --- | --- |
| **Public repo exposes people's data** | Real user interview transcripts (`docs/handoff/fixtures/`), 3.1 MB of agent session logs, a founder's personal Gmail and aliases, other personal addresses, 10 real startups' seed data | Make the repo private, or move these files out and purge them from history; treat it as a possible personal-data incident and check notification duties |
| **Infrastructure details public** | Hosted Supabase project reference and production hostnames in docs | Rotate database and service credentials; restrict network access; the docs themselves say credentials once exposed in chat must be rotated |
| **Tenant isolation bypassed** | Server traffic connects as `postgres` with BYPASSRLS, so row-level security is not in the request path (audit A-02; ADR 0065 still 'Proposed') | Ship ADR 0065 before any multi-company or Agent OS rollout |
| **Prompt injection** | Untrusted web-research text is placed in system instructions (audit F-03) | Move it to a data message with an untrusted marker; this is the threat register's 'MUST' item |
| **Model data routing** | A demo attestation lets staging send any sensitivity level to an unreviewed model (audit S3) | Remove before real users' private data flows |

No live API keys or private keys were found in the public tree (pattern search, values not copied).

### Product and legal risks

| Risk | Why it matters | Mitigation |
| --- | --- | --- |
| **Unlicensed investment activity** | A success fee or deal facilitation can make the operator a broker or 'arranger' (the docs name US SEC broker-dealer and UK FCA rules) | Keep 'never moves money'; get legal opinions per market before any success fee |
| **Home-market regulation missing** | SEC Nigeria, CBN, Nigeria's Data Protection Act, and Qatar/UAE regulators do not appear in the docs, yet those are the target markets | A regulatory map per market, owned by counsel, before paid launch |
| **AI giving regulated advice** | Both Capital Q and the Agent OS touch legal, tax and investment questions | Q's rule already forbids advice; keep the 'prepare, recommend, human decides' line and route to licensed partners |
| **Minors (Agent OS)** | Minors usually cannot be company directors or sign binding contracts (UK minimum director age is 16; many countries require 18) | Guardian accounts, co-signing, spending limits, age-appropriate structures per country |
| **Wrong regulation** | A model's memory of a law can be outdated or invented | Regulation packs as versioned, cited data reviewed by professionals; Q never answers a legal duty from memory |
| **Identity and fraud** | KYB is manual with no vendor; fake investors soliciting fees is a named threat | Add a KYC/KYB vendor; never let the platform carry payment requests between users |
| **Profiling from public data** | Building profiles of people from web research raises GDPR Article 14 duties; meeting notetakers need consent | Notices, consent capture, retention limits |
| **Agent actions at scale** | 657 failed action events in the outbox (audit A-01); no global rate limiter; single replica with in-memory state | Fix reliability before granting agents write power |
| **Untrusted files and engines** | No malware scanner ships; native plug-ins (VST/CLAP, Photoshop-style) and PDF JavaScript exist in the Craft engines | Add a scanner; run Craft engines in containers with plug-ins, scripts and network disabled |
| **Brand and IP** | ArtCraft names and logos are trademarked; generated media can infringe | Attribute engines plainly; keep image provenance (Q already records model, prompt and cost) |

## Costs and business model

The software is largely paid for: Q's code is yours and the 12 Craft engines carry no licence fee. What costs money is AI usage, outside services that sit on the legal path (identity, payments, filings), licensed humans, and the security work needed before real customers' data scales up.

### What needs money

| Cost line | Driver | Size | Can it be reduced? |
| --- | --- | --- | --- |
| **AI model and voice usage** | Every answer, interview, document and voice minute (Gemini, Groq, OpenAI realtime, Deepgram, ElevenLabs, image generation) | Largest variable cost; grows with usage | Yes: cheaper models for drafts, caching, deterministic engines (Craft, GateQ, discovery) instead of model calls, Q's own cost ledger |
| **Hosting** | Railway (4 services), Supabase, Cloudflare Stream, worker capacity | Modest now; grows with users and stored media | Yes: Craft engines run on ordinary CPUs, no GPUs needed for documents |
| **Per-use outside services** | Meeting bots (Recall.ai), web research (Tavily, SerpApi, Bright Data), email | Per meeting, per search, per message | Partly: cap and meter them as paid features |
| **Identity and fraud (KYC/KYB)** | A verification vendor, charged per check | Per user verified | No: legally required once money or investors are involved |
| **Payments** | Stripe (built, switched off); a local rail such as Paystack or Flutterwave for NGN | Percentage of each payment | No |
| **Business set-up (Agent OS)** | Government registration fees, registered-agent or filing partners | Per business formed; varies by country | Passed through to the customer |
| **Licensed professionals** | Lawyers and accountants who review filings and regulation packs | Per review or retainer | Partner revenue share instead of salaries |
| **Legal opinions** | Broker-dealer and FCA 'arranging' opinions before any success fee; minors and consumer law for the Agent OS | One-off per market | No; required before launch in each market |
| **Security and assurance** | Penetration test, malware scanner, error monitoring, later SOC 2 audit, cyber insurance | One-off plus yearly | Phase it: pen test and monitoring first |
| **Video and heavy media** | FilmCraft / EffectCraft renders, generative video | Minutes of CPU per minute of video | Keep as a paid, queued feature |
| **People** | Engineering, a compliance owner, customer support | The largest fixed cost | Agents absorb routine support and operations |

Get written quotes for the vendor lines before setting prices; none are assumed here.

### How it makes money

| Product | Model | Basis |
| --- | --- | --- |
| **Capital Q** | Subscriptions: Founder Pro, Investor Pro (per seat), Fund | Already in Q's billing package; recommended prices in the docs are $49/month, $99/seat/month and $499/month for up to 10 seats, not yet confirmed |
| **Capital Q** | Usage credits for heavy features (AI images, research, rehearsals, Daily editions, GateQ gateways) | Already gated as feature keys |
| **Capital Q** | GateQ as software for investors' intake | Named in the docs as a revenue point |
| **Capital Q** | Advisory referrals (FDN Advisory) | Named in the docs |
| **Agent OS** | Free tier for students and first-time founders (guardian required for minors) | Builds the feeder market for Capital Q |
| **Agent OS** | 'Run my business' subscription per active business | Covers daily operations, bookkeeping, compliance reminders |
| **Agent OS** | Pass-through plus margin on formation, filings and professional reviews | The partner marketplace |
| **Agent OS** | White-label for schools, accelerators, banks and governments | Their brand, your engine; the largest contracts |
| **Both** | Media credits for video, audio and print-ready design | Priced above the compute it uses |

Avoid a success fee on fundraising until counsel signs off in each market; the docs already flag it as needing a legal opinion.

## Technical appendix

The build plan runs in five gated phases over about a year; the first two need almost no money and reuse code that already exists in Q and the Craft engines.

&#91;embedded content: phased build plan · 5 phases, 4 gates · rough timing for a small team\]

Timings are rough estimates for a small team; the gates, not the dates, decide when the next phase starts.

### Integration pattern for a Craft engine (proven twice)

1. **Build** `<app>-cli` on Linux from the pinned commit in the acquisition manifest (pure Rust, no GPU, no display).
2. **Run** it as a child process with no shell, a minimal environment, a private temp folder, a timeout and output limits — the same pattern as Q's `apps/workers/src/parser/sandbox.ts` — inside a container with no network.
3. **Talk** MCP over stdio: `initialize`, `tools/list`, then `tools/call` (the \~100-line client in `agent-integration/poc/mcp-stdio.mjs`).
4. **Wrap** each capability Q exposes as a typed Q tool (Zod in/out, risk class, scopes); read-only tools go in the registry, writes become approval-engine actions.
5. **Verify** outputs by their bytes (file signatures, recomputed values) and log provenance like Q already does for images.

Measured on this machine: VectorCraft and GridCraft start and answer `initialize` in 16–20 ms, and individual operations take 2–9 ms; GridCraft's NPV and IRR matched an independent calculation to about 13 significant digits.

### Team

| Role | Why | When |
| --- | --- | --- |
| Platform engineer (Rust + TypeScript) | Craft engine builds, sandbox, MCP driver interface | Phase 1 |
| Security engineer (part-time or contracted) | RLS, secrets, penetration test, prompt-injection defences | Phase 0–2 |
| Applied AI engineer | Evals, domain packs, workforce executors | Phase 1–3 |
| Compliance and legal owner | Regulatory map per market, legal opinions, partner contracts | Phase 2–4 |
| Product designer | Canvas, guardian experience, artifact review | Phase 2–4 |

### Metrics that tell you it is working

| Metric | Measures |
| --- | --- |
| Share of uploaded files Q can fully read | OCR and formula coverage |
| Founder time from sign-up to investor-ready pack | Capital Q value |
| Approval rate of Q-prepared artifacts without edits | Output quality |
| Cost per active business per month | Unit economics |
| Cross-tenant or approval-bypass incidents | Safety (target: zero) |
| Businesses formed and still active at 90 days | Agent OS value |

## Evidence and sources

Every statement about Q comes from reading `neo1415/q` at branch `build/int-rc`, commit `668ee838` (11 October 2026), read-only; every statement about the Craft engines comes from their source and, for two of them, from running them.

| Claim type | How it was established | Examples |
| --- | --- | --- |
| **Verified by running** | Built from source on Windows and driven over MCP; output checked byte by byte; upstream test suites run | VectorCraft (logo to SVG/PNG/PDF, 107 upstream tests passed); GridCraft (model with NPV/IRR/MOIC, XLSX reopened, 29 upstream tests passed) |
| **Read in code** | File and line references from the current Q branch and the Craft repos | Tool and action counts, model routing, approval engine, sandbox, MCP client state, artifact formats |
| **Read in Q's own docs and audit** | Q's specs, ADRs, status files and the 8 October forensic audit | Live deployment, cold investor demo, BYPASSRLS finding, billing plans and recommended prices |
| **Judgement** | This document's assessment | Impact and effort placement, timings, team, the Agent OS design |

- Q repository: [github.com/neo1415/q](https://github.com/neo1415/q) (branch `build/int-rc`)
- Craft engines and acquisition record: the private index [neo1415/artcraft-ecosystem-index](https://github.com/neo1415/artcraft-ecosystem-index) and forks under [github.com/neo1415](https://github.com/neo1415)
- Upstream Craft source: [github.com/storytold](https://github.com/storytold)

Regulatory statements are general and not legal advice; the only specific rule cited (minimum director age of 16 in the UK) should be confirmed by counsel along with every market's rules. Vendor costs are not quoted; get written quotes.
