# Helper agent agent-a08e95ccff4c7b09f: Public site and trust pages

Source: `agent-a08e95ccff4c7b09f.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-30 12:27

You are the PUBLIC builder for Talent Q's design prototype (/home/user/neo/talent-q-design/prototype). First read `/home/user/neo/talent-q-design/journeys/COVERAGE-BUILD-BRIEF.md` and follow it exactly. Your name for files is `public`, and your vite port is 5211.

**Your scope:** atlas screens SC-001 (Landing + Q intro), SC-002 (How Talent Q works), SC-003 (For Employers), SC-004 (For Talent), SC-005 (Pricing), SC-006 (Trust and AI explanations), SC-008 (Auth sign in) and SC-013 (Public sample Q interaction). Build them as real public pages (`side: 'public'`) in Direction D, on desktop and phone.

Ground the copy in the founder's positioning in `docs/sources/batch-6/00_START_HERE_PRODUCT_DECISION.md`:
- "Evidence-first hiring, with Q doing the work."
- "Show what you can do, even if your CV doesn't."
- the two promises.

Q is present on the public pages as a sample conversation (SC-013). A visitor can ask a few things and get honest, labelled sample answers. It never claims real candidates or real results, and it leads into `/signup` (which exists in `routes/entry.tsx`).

**Pricing (SC-005)** shows the buyer offers from `01_BUYER_EVIDENCE_AND_PRICING.md` as clearly labelled hypotheses:
- role pilot;
- team plan;
- agency plan;
- candidate core free.

It takes no payment and makes no "proven" claims. The page states plainly that prices are being tested.

**Trust (SC-006)** explains:
- what Q does and does not decide;
- human review;
- evidence classes;
- privacy and revocation;
- simulated vs real;
- no face, accent or emotion scoring.

Use the ledger's "Unproven claims" list as hard constraints.

**Sign in (SC-008):** email-code, Google and Microsoft are simulated and labelled. It routes into the right home for the cast member.

**Route `/`:** check what `/` renders today (`routes/entry.tsx` and the router). Don't break the founder's existing entry. If `/` is taken, make the landing `/welcome-site` or similar and link it from the existing entry, or choose the least invasive option and say which.

Also read decision D15 in `handoff/DECISION-REGISTER.md`. The founder has now asked for the whole blueprint, so build these pages; record that D15 is resolved in your report.

- 🔧 `Bash`: Read the coverage build brief

  <details><summary>result</summary>

```
# Coverage build brief (30 Oct): close the remaining 183 / 57 / 41 gaps

The founder's scope (30 Oct): finish the **complete interactive product and design blueprint**, not production code. Every remaining screen concept, motion and vision group gets a real page, state or interaction in the Direction D prototype. Documenting a gap is not enough. Nothing from J1–J12 may regress.

## Where the requirements are
- Screen concepts: `docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv`. Read your rows in full: purpose, actor, states, Q role, data, notes.
- Motions: `docs/sources/batch-2/03_MOTION_AND_VIDEO_ATLAS_v2.csv` (trigger, surface, reduced-motion fallback).
- Vision groups: `docs/sources/batch-3/04_FOUNDER_VISION_TRACEABILITY_v2.csv`.
- Current status of each: `screens/SCREEN-COVERAGE.csv`, `motion/MOTION-COVERAGE.csv`, `research/VISION-COVERAGE.csv` (generated; don't edit).
- Product rules: `handoff/Q-INTELLIGENCE-SPEC.md`, `handoff/PRIVACY-AND-PERMISSIONS.md`, `handoff/DECISION-REGISTER.md`, `handoff/CONSOLIDATION-MERGE-LEDGER.md`.
- Design system: `design-system/DIRECTION-D-SYSTEM.md`, `handoff/DESIGN-QUALITY-GATE.md`. For the standard expected, read one design note, e.g. `journeys/design/evidence-candidate.md`.

## How the prototype is put together (extend it; never duplicate it)
- Prototype: `prototype/` (React + TypeScript + Vite). One world store: `mock/world.ts`.
- **Area slices:** add your own in `src/state/areas/<you>.ts` (`export const area = { id, init }`).
- **
… [4421 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read atlas rows, coverage, and layout
- 🔧 `Bash`: Read D15 and product decision

  <details><summary>result</summary>

```
Exit code 2
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv'
SC-001,Foundation / public,Landing + Q intro,All,,Public site and entry,NOT YET REPRESENTED,,No,None (simulated),No,RESEARCHED,,,
SC-002,Foundation / public,How Talent Q works,All,,Public site and entry,NOT YET REPRESENTED,,No,None (simulated),No,RESEARCHED,,,
SC-003,Foundation / public,For Employers,All,,Public site and entry,NOT YET REPRESENTED,,No,None (simulated),No,RESEARCHED,,,
SC-004,Foundation / public,For Talent,All,,Public site and entry,NOT YET REPRESENTED,,No,None (simulated),No,RESEARCHED,,,
SC-005,Foundation / public,Pricing,All,,Public site and entry,NOT YET REPRESENTED,,No,None (simulated),No,RESEARCHED,,,
SC-006,Foundation / public,Trust and AI explanations,All,,Public site and entry,NOT YET REPRESENTED,,No,None (simulated),No,RESEARCHED,,,
SC-007,Foundation / public,Accessibility and language,All,,Public site and entry,STATE OR SECTION of /settings,"Direction D, native (/settings)",Yes,None (simulated),No,PROTOTYPED,/settings,prototype/src/routes/entry.tsx (Settings); captures/cx/T4/phone-09-lite; captures/cx/T5/d-07-settings,"Section of /settings: lite mode, plain words and voice on/off, written to the store and honoured by Q and T4 pages. Missing: locale/language choice, and this is not a public page. axe clean desktop and phone (qa/results/axe-all.json); screen-r
… [2369 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
Exit code 1
28:| D15 | **Public marketing site** (atlas screens 001–008, 013) | Founder | Not part of the ten journeys. Proposed as a later phase. | Documented as a future capability (`ATLAS-GAPS.md`). |
29-| D16 | **Mail providers and access level.** Which providers first, and whether Talent Q requests mailbox **read** access (Gmail restricted scopes need a security assessment) | Founder (scope and cost), then engineering | Read access lets Q see replies, but it brings verification cost and privacy duty. | Send-only and read-and-reply are both designed and simulated. Recommendation: launch send-only plus in-app replies; read access per tenant, opt-in. |
30-| D17 | **Rubric validation and use.** Who signs off a rubric's job-relatedness; adverse-impact monitoring; whether the index is visible to hiring managers | Founder plus an I-O psychology or fairness adviser | The index affects decisions; it is not validated. | Prototype arithmetic only, always shown with coverage, labelled as unvalidated; human review required. |
31-| D18 | **Media analysis provider, region and retention** for video and voice evidence | Founder plus legal | Biometric-adjacent data; cost per minute. | Simulated transcription; transcript-only analysis; no frame review; 90-day default consent expiry. |
32-| D19 | **Default candidate contact policy** for verified employers (off, after applying, before applying) and the weekly limit | Founder | Openness vs recruiter inbox load and abuse. | Kora allows contact
… [1447 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Locate source documents

  <details><summary>result</summary>

```
./docs/sources/batch-2/03_MOTION_AND_VIDEO_ATLAS_v2.csv
./docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
./docs/sources/batch-3/04_FOUNDER_VISION_TRACEABILITY_v2.csv
./docs/sources/batch-6/01_BUYER_EVIDENCE_AND_PRICING.md
./docs/sources/batch-6/04_SOURCE_LEDGER.md
./docs/sources/batch-6/00_START_HERE_PRODUCT_DECISION.md
COVERAGE-SUMMARY.md
DESIGN-SKILL-AUDIT.md
PROGRESS.md
README.md
artifacts
captures
components
contracts
decisions
design-system
handoff
journeys
motion
prototype
qa
registry
research
screens
scripts
storyboards
tokens
ADDENDUM-REQUIREMENTS.csv
CONSOLIDATION-REQUIREMENTS.csv
status.json
```
  </details>

- 🔧 `Bash`: Read atlas rows and product decision

  <details><summary>result</summary>

```
{'screen_id': 'SC-001', 'section': 'Foundation / public', 'screen_name': 'Landing + Q intro', 'primary_actor': 'All', 'must_show': 'Promise and entry for two sides; Talent Q gold presence', 'fidelity': 'Prototype', 'variants': 'loading; ready; empty; error; permission denied; accessible alternative; mobile', 'backend_boundary': 'Domain read/action + permission', 'desktop_and_mobile': 'Both; may reuse layout variants', 'source': 'Founder vision + audited product research'}

{'screen_id': 'SC-002', 'section': 'Foundation / public', 'screen_name': 'How Talent Q works', 'primary_actor': 'All', 'must_show': 'Audience switch and contextual product demonstrations', 'fidelity': 'Prototype', 'variants': 'loading; ready; empty; error; permission denied; accessible alternative; mobile', 'backend_boundary': 'Domain read/action + permission', 'desktop_and_mobile': 'Both; may reuse layout variants', 'source': 'Founder vision + audited product research'}

{'screen_id': 'SC-003', 'section': 'Foundation / public', 'screen_name': 'For Employers', 'primary_actor': 'All', 'must_show': 'Employer outcomes, sample journey and trust', 'fidelity': 'Prototype', 'variants': 'loading; ready; empty; error; permission denied; accessible alternative; mobile', 'backend_boundary': 'Domain read/action + permission', 'desktop_and_mobile': 'Both; may reuse layout variants', 'source': 'Founder vision + audited product research'}

{'screen_id': 'SC-004', 'section': 'Foundation / public', 'screen_name': 'For Talen
… [9338 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read pricing and unproven claims

  <details><summary>result</summary>

```
# Talent Q | Paying buyer personas, commercial evidence, and pricing hypotheses
**30 October 2026 | Desk research, not interviews or proven willingness to pay**

## What can and cannot be established from public evidence
Actual spend on ATS, recruiting software and AI agent credits proves that recruitment buyers have budgets. Complaints and surveys show experienced friction. Neither proves that people will pay *Talent Q* or what conversion and retention will be. User interviews are not a prerequisite to building; however, observed payment and product usage remain the strongest validation of price, and publicly posted comments cannot fully substitute for actual purchase behavior.

## Public signals, with limitations
1. **Direct existing spend:** Workable Standard lists $299/month billed annually for 1–20 staff. Agent work is metered: evaluation 1 credit, sourcing 2, chat 10; paid credit bundles are $0.095–$0.12/credit, with 3,000 credits included for paid accounts. Vendor prices, not observed willingness to pay for Talent Q. [Workable pricing](https://www.workable.com/pricing).
2. **Alternatives already paid:** JazzHR Hero lists $1,000/year; Plus $3,480/year includes AI candidate matching and structured interviews; Pro $5,508/year. [JazzHR pricing](https://www.jazzhr.com/pricing).
3. **Reported high-price rejection:** An April 14, 2026 Reddit participant, first recruiter at a 20-person startup scaling to 60, said a *quoted* $48,000/year for one LinkedIn Recruiter seat was unju
… [10740 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read route registry and entry

  <details><summary>result</summary>

```
// Route registry. Each feature area registers its pages in its own file under src/routes/ (discovered
// automatically), so areas can be built in parallel without editing a shared routing file.
// A route renders as the CANVAS beside the global Q thread; Q is never absent from a product page.
import type { ReactNode } from 'react';
import type { IconName } from '../ds/icons';

export interface RouteDef {
  /** Path pattern; ':param' segments are passed to render(). */
  path: string;
  side: 'recruiter' | 'candidate' | 'both' | 'public';
  render: (params: Record<string, string>) => ReactNode;
  /** Shown in the rail when set. Groups: 'Q' | 'Hiring' | 'Agency' | 'Knowledge' | 'Grow' | 'Evidence' | 'Work'. */
  nav?: { group: string; label: string; icon: IconName; tab?: boolean; order: number; badge?: string; orgKind?: 'EMPLOYER' | 'AGENCY'; /** Only for members of these organisations (pages showing one org's data). */ orgIds?: string[]; /** Extra paths that also mark this entry as current ("you are here"). */ also?: string[] };
  /** Human label for "go back to …" and history. */
  label: string;
  /** Public and signup pages render without the shell. */
  bare?: boolean;
}

const routes: RouteDef[] = [];
export const registerRoute = (r: RouteDef) => { const i = routes.findIndex((x) => x.path === r.path); if (i >= 0) routes[i] = r; else routes.push(r); };
export const allRoutes = () => routes;

export function matchRoute(path: string): { def: RouteDef; params: Record<string,
… [14921 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rest of entry and App

  <details><summary>result</summary>

```
<motion.div key={step} initial={{ opacity: 0, x: 12 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -12 }} transition={{ duration: 0.2 }} style={{ display: 'grid', gap: 14 }}>
            {step === 'account' && (
              <form style={{ display: 'grid', gap: 14 }} onSubmit={(e) => { e.preventDefault(); if (!/^\S+@\S+\.\S+$/.test(email)) { setErr('That email doesn’t look complete. Check for a missing @ or dot.'); return; } setErr(''); setStep('verify'); }}>
                <h1 id="su-h" className="voice t30" style={{ margin: 0 }}>Create your account</h1>
                <div className="ds-field"><label htmlFor="su-name">Your name</label><input id="su-name" className="ds-input" value={name} onChange={(e) => setName(e.target.value)} autoComplete="name" /></div>
                <div className="ds-field"><label htmlFor="su-email">Email</label><input id="su-email" className="ds-input" type="email" value={email} onChange={(e) => setEmail(e.target.value)} aria-invalid={!!err} aria-describedby={err ? 'su-err' : undefined} autoComplete="email" />{err && <span id="su-err" className="t14" style={{ color: 'var(--risk)' }}>{err}</span>}</div>
                <button type="submit" className="ds-btn primary">Continue</button>
                <button type="button" className="ds-btn" onClick={() => { setErr(''); setStep('mode'); }}>Continue with Google (simulated)</button>
                <p className="t14 muted" style={{ margin: 0 }}>Already have an account? <Link to="/">Sign in
… [11948 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Entry screen and router

  <details><summary>result</summary>

```
28 src/screens/Entry.tsx
import { Link } from '../ui/router';
import { QPresence } from '../q/QPresence';

export function Entry() {
  return (
    <main className="main stack gap-12" style={{ maxWidth: 880 }}>
      <div className="stack gap-6" style={{ paddingTop: 48 }}>
        <QPresence state="idle" size={72} />
        <h1 className="t-hero">Hire by talking. Grow by doing.</h1>
        <p className="t-lead muted measure">Q is the assistant inside Talent Q. It works in the background, shows its sources, and asks before it acts. This prototype runs on simulated data.</p>
      </div>
      <div className="grid-2">
        <Link to="/r/home" className="panel stack gap-2" style={{ textDecoration: 'none', color: 'var(--color-text)' }}>
          <span className="t-label q-text">For employers</span>
          <span className="t-title">I’m hiring</span>
          <span className="muted">Ada Okafor, recruiter at Kora Pay (fictional)</span>
        </Link>
        <Link to="/c/career" className="panel stack gap-2" style={{ textDecoration: 'none', color: 'var(--color-text)' }}>
          <span className="t-label q-text">For professionals</span>
          <span className="t-title">I’m building my career</span>
          <span className="muted">Amaka, Chidi or Tobi (fictional)</span>
        </Link>
      </div>
      <p><Link to="/x">Design direction review: three directions, the same three experiences →</Link></p>
      <p className="t-caption">Tip: open the hiring side and the c
… [1106 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read openers and Workspace

  <details><summary>result</summary>

```
// Q's opening line (audit addendum §B, AD-B-01/02), shown when a person's conversation with Q is empty.
// Rules (from design-skills:ux-writing): name ONE concrete thing on this page from live state, in 14 words or
// fewer where possible; offer one verb-first action; never repeat the page's heading or a Q card already showing
// (same subject); plain words; with proactivity off, only an invitation. The generic line is the last fallback.
// Areas register openers for their pages in q/openers/*.ts (discovered by glob, like skills and rules).
import type { Actor, QAction } from '../../state/domain';
import type { World } from '../../mock/world';

export interface Opening { subject: string; text: string; action?: QAction }
export interface Opener { id: string; side: 'recruiter' | 'candidate' | 'both'; match: (path: string) => boolean; build: (w: World, a: Actor, path: string) => Opening[] }

const openers: Opener[] = [];
export const registerOpener = (o: Opener) => { if (!openers.some((x) => x.id === o.id)) openers.push(o); };

/** Invitation used when nothing on the page is actionable, or when proactivity is off. */
export function invitation(a: Actor): Opening {
  // No greeting: pages already greet by name, and saying it twice is noise.
  if (a.side === 'candidate') return { subject: 'invite', text: 'Tell me what you’re hoping for, in your own words. You decide what employers see.' };
  if (!a.orgId) return { subject: 'invite', text: 'Tell me what keeps going wrong in your b
… [9305 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Direction D system

  <details><summary>result</summary>

```
114 design-system/DIRECTION-D-SYSTEM.md
  16 handoff/DESIGN-QUALITY-GATE.md
 130 total
# Talent Q design system: Direction D

Approved by the founder on 29 Oct 2026 as the primary design direction. Code lives in `prototype/src/ds/`. Tier-1 values come from `tokens/tokens.json`, which builds `styles/tokens.css` with a contrast gate.

## Materials

| Material | Where | Job |
|---|---|---|
| **Ink** (`--night`) | Rail, thread, phone tabs, sheet bar | Where Q thinks, speaks and works. Also navigation |
| **Paper** (`--paper`, `--sheet`) | Canvas, artifacts, forms | Where evidence and work are read at high contrast |
| **Gold** (`--gold-light` on ink, `--gold` and `--gold-ink` on paper) | Q mark, Q's proposals, the one primary next step | Means "Q and Q's work". Never decoration and never an evidence level |

**Candidate warmth.** `data-audience="candidate"` warms the paper (#f7efe3) and the ink, rounds surfaces to 20px and uses first-name greetings. Contrast floors, the accent and every rule stay the same.

## Type

| Face | Use |
|---|---|
| Fraunces | Q's voice, verdicts, view titles that state the finding |
| Inter Tight | UI and body text |
| IBM Plex Mono | Data, labels, counts, versions |

Scale: 12 · 14 · 16 · 19 · 24 · 30 · 38 · 46 (major third).

## Components (`src/ds/`)

| Component | Notes |
|---|---|
| `AppShell` | Workspace switcher (Hiring and Career), a rail of up to 4 groups and 9 items, the command palette (⌘/Ctrl K), and phone tabs (4 plus More). Shows only are
… [5497 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read quality gate, design note, motion, ds classes

  <details><summary>result</summary>

```
# Design quality gate

From now on, no journey moves from "it works" straight to recording. Each journey, and each new screen within one, passes these checkpoints in order. Keep it light: the output is better screens, not paperwork.

| # | Checkpoint | What happens | Proof it happened |
|---|---|---|---|
| 1 | Design research and skills, **before** building | Load the relevant skills and apply them to the brief: `design-critique`, `design-elevation`, `interaction-design`, `ux-writing`, plus `dataviz` for any chart or ledger and `design-superpowers:creative` for the candidate surfaces | One line per skill in the journey's design note: which screens it shaped |
| 2 | Visual implementation | Build with `src/ds` components and the execution rules in `design-system/DIRECTION-D-SYSTEM.md`. Fix shared problems in the shared component, not on one page | — |
| 3 | Browser rendering | `qa/scripts/review/capture-all.mjs` captures every page in the journey at desktop 1440 and phone 390, plus its key states | `captures/review/after/` |
| 4 | Visual critique | Look at every capture against the critique checklist (hierarchy, density, excise, labels, copy, touch, states, motion) and write down the defects | Defect list in the journey's design note |
| 5 | Corrections | Fix the defects, then recapture. Repeat until you would show it to a design lead | Before/after pairs for the worst problems |
| 6 | Interaction and accessibility | Run `qa/scripts/review/axe-all.mjs` and `keyboard.mjs`, plus 
… [9157 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect ds.css and actor switching

  <details><summary>result</summary>

```
/* Talent Q design system · Direction D (approved 29 Oct 2026).
   Two materials: INK is where Q thinks, speaks and works; PAPER is where evidence and artifacts are read.
   One accent: gold means Q and Q's work. Type: Fraunces (voice) · Inter Tight (UI) · IBM Plex Mono (data).
   Scale: 12 · 14 · 16 · 19 · 24 · 30 · 38 · 46 (major third). Space: 8px unit. Radius: 10 controls · 16 surfaces · pill chips.
   Tier-1 colours come from tokens.css (generated from tokens/tokens.json); this file maps them to D roles. */
.ds {
  --paper: var(--ref-paper-0); --sheet: var(--ref-paper-1); --wash: var(--ref-paper-2); --rule: var(--ref-paper-3); --rule-2: var(--ref-paper-4);
  --ink: var(--ref-ink-900); --ink-2: var(--ref-ink-700); --ink-3: var(--ref-ink-600);
  --night: var(--ref-night-0); --night-2: var(--ref-night-1); --night-3: var(--ref-night-3); --night-4: var(--ref-night-4); --moon: var(--ref-ink-100); --moon-2: var(--ref-ink-300);
  --gold: var(--ref-gold-600); --gold-ink: var(--ref-gold-800); --gold-light: var(--ref-gold-400); --gold-wash: #f1e3bf;
  --ok: var(--ref-green-light); --warn: var(--ref-amber-light); --risk: var(--ref-red-light);
  --voice: var(--font-voice); --ui: var(--font-ui); --data: var(--font-mono);
  --shadow: 0 1px 0 rgb(80 60 20 / .05), 0 10px 28px -18px rgb(80 60 20 / .30);
  --r-control: 10px; --r-surface: 16px;
  --rail-w: 232px; --thread-w: 380px;
  background: var(--paper); color: var(--ink); font-family: var(--ui); font-size: 16px; line-height: 1.55;
}
/
… [5125 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Look at actor switching and cast

  <details><summary>result</summary>

```
{last ? <span className="peek">{last.text}</span> : <span>Ask Q anything…</span>}
      </button>
    </div>
  );
}

function WhoMenu({ onDone }: { onDone: () => void }) {
  const actors = useWorld((w) => w.actors.filter((a) => a.journey));
  const cur = useWorld((w) => w.session.actor);
  const last = useWorld((w) => w.session.lastRoute);
  const [sure, setSure] = useState(false);
  const sw = (id: string) => {
    const a = actors.find((x) => x.id === id)!;
    update((w) => { w.session.actor = id; });
    onDone();
    navigate(last[id] ?? (a.side === 'recruiter' ? (a.signedUp ? '/r/home' : '/signup') : (a.signedUp ? '/c/home' : '/signup')));
  };
  return (
    <div className="ds-who" role="group" aria-label="Switch person (demo)">
      {(['recruiter', 'candidate'] as const).map((side) => (
        <div key={side} style={{ display: 'grid', gap: 2 }}>
          <span className="lab" style={{ padding: '6px 10px 2px' }}>{side === 'recruiter' ? 'Hiring' : 'Candidates'}</span>
          {actors.filter((a) => a.side === side).map((a) => (
            <button key={a.id} type="button" className="ds-railbtn" aria-current={a.id === cur ? 'true' : undefined} onClick={() => sw(a.id)}>
              <span className="ds-av" aria-hidden="true" style={{ width: 24, height: 24, fontSize: 10 }}>{a.initials}</span>
              <span>{a.name} <span className="muted">· {a.journey}</span></span>
            </button>
          ))}
        </div>
      ))}
      {/* Confirmed in place, not wi
… [6550 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find related motions and vision rows

  <details><summary>result</summary>

```
motion_id,name,event_trigger,intended_behavior,implementation_hint,reduced_motion_or_text_fallback,primary_surface,required_capture,fake_progress_prohibited


vision_id,founder_requirement,indicative_screen_ids,source_status,status,route,evidence,note
V06,"Web search, safe scraping/fetch, links",SC-033; SC-128; SC-136,Design+permissions,RESEARCHED,,,
V07,Safe internet file downloads,SC-130; SC-068,Design+permissions,RESEARCHED,,,
V08,"Emails, SMS, WhatsApp outbound",SC-048; SC-049; SC-050,Design+providers,PROTOTYPED,/r/messages,"qa/results/R3.log (SENT_SIMULATED, QUEUED_OFFLINE), R4.log (campaign), T5.log (follow-up); prototype/src/journeys/hire-c/Messages.tsx","Email, text and in-app messages with checks and explicit approval; campaigns under limits. No WhatsApp. Everything is simulated; no real external system."
V10,Expensive video/voice optional,SC-098; SC-102; SC-101,Design+providers,PROTOTYPED,/c/interview,qa/results/T4.log (voice unavailable falls back to typing); prototype/src/journeys/talent-c/shared.tsx,Voice is optional with text and form parity. Video interviews are not built.
V16,Credential and permit verification,SC-070; SC-071; SC-072,Design+providers,PROTOTYPED,/c/passport,"qa/results/T3.log (pending → failed → manual review), T4.log (issuer check pending)",Credential checks with honest pending/failed/review states. Work permits (SC-071) not built. Everything is simulated; no real external system.
V21,Candidate practice and feedback,SC-089; SC-107; SC-093,Desi
… [1212 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check vision rows and motion atlas content

  <details><summary>result</summary>

```
talent-q-design/research/VISION-COVERAGE.csv:V30,International and accessible design,SC-007; SC-100; SC-064,Foundation,PROTOTYPED,/settings,"qa/results/axe-all.json (106 scans clean); qa/scripts/review/keyboard.mjs; qa/results/T4.log (plain words, lite mode, 44px targets)","Accessible defaults, plain words, lite mode, time zones. No language/locale choice; screen-reader review outstanding."
talent-q-design/research/VISION-COVERAGE.csv:V41,Free Figma independent design production,SC-001; SC-117,Design operational requirement,VERIFIED,/,"design canvas + talent-q-design/prototype (TypeScript, builds clean)",No paid Figma used.
docs/sources/batch-3/04_FOUNDER_VISION_TRACEABILITY_v2.csv:V30,International and accessible design,"Locale, accessibility and low bandwidth",SC-007; SC-100; SC-064,Foundation
docs/sources/batch-3/04_FOUNDER_VISION_TRACEABILITY_v2.csv:V41,Free Figma independent design production,Claude design/artifacts plus local typed React source,SC-001; SC-117,Design operational requirement
58
MO-001,Q orb idle,app:idle,Slow ambient gold presence without distractive loops,CSS/Rive,Static gold icon,Q Home and interview,MP4 8-20s + working component state,Yes
MO-002,Q listens,voice:recording,"Quiet intensity and caption indicator, no fake waveform",Rive/CSS,Listening text and transcript,Voice interview,MP4 8-20s + working component state,Yes
MO-003,Q thinks,run:accepted,Subtle gold change and accurate accepted state,CSS,Accepted task label,All run views,MP4 8-20s + wor
… [9529 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List researched motions and registry shape

  <details><summary>result</summary>

```
motion_id,name,event_trigger,primary_surface,reduced_motion_fallback,status,route,evidence,note
MO-004,Q speaks,voice:audio-out,Voice/video,Captions,RESEARCHED,,,
MO-005,Q interrupted,voice:interrupted,Voice/video,State text,RESEARCHED,,,
MO-013,Candidate comparison morph,compare:changed,Compare candidates,Direct table redraw,RESEARCHED,,,
MO-014,Job preference filter,filter:changed,Explore Jobs,Direct redraw,RESEARCHED,,,
MO-018,Question plan appears,interview:plan-ready,Interview plan,Question list,RESEARCHED,,,
MO-023,Live Q suggests followup,copilot:suggestion-ready,Live companion,Suggestion card,RESEARCHED,,,
MO-026,Candidate score review,review:ready,Employer review,Static scorecard,RESEARCHED,,,
MO-029,Candidate share revoked,share:revoked,Portfolio,Revoked label,RESEARCHED,,,"Was shown by the earlier Passport screen (film F8), which is no longer routed; the rebuilt /c/passport ends access wi
MO-030,CV draft generated,artifact:ready,CV builder,Loaded document,RESEARCHED,,,
MO-031,Graphic from Q,artifact:chart-ready,Q canvas,Static SVG/accessible table,RESEARCHED,,,
MO-032,Video artifact available,media:ready,Q canvas,Transcript,RESEARCHED,,,
MO-034,Download scanned,scan:passed,File vault,Verified file state,RESEARCHED,,,
MO-035,Agent budget warning,budget:threshold,Q planner,Warning text,RESEARCHED,,,
MO-038,Desktop-mobile narrative transition,demo:viewport-change,Demo film,Screenshots,RESEARCHED,,,
MO-040,Candidate application status,application:updated,Applications,S
… [1300 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read sample feature test and runner

  <details><summary>result</summary>

```
// Candidate-initiated recruiter correspondence (audit addendum §C, AD-C-01..09) and the role briefing (J11 steps 1–2).
// Usage: BASE=http://localhost:5191 node qa/scripts/features/contact.mjs
import { createRequire } from 'node:module';
import { mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node-tools/node_modules/playwright/index.js');
const BASE = (process.env.BASE || 'http://localhost:5191').replace(/\/$/, '');
const OUT = resolve(dirname(fileURLToPath(import.meta.url)), '../../../captures/cx/contact'); mkdirSync(OUT, { recursive: true });
const results = []; const errors = [];
const step = (name, ok, info = '') => { results.push({ name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${info ? ` — ${String(info).replace(/\s+/g, ' ').slice(0, 200)}` : ''}`); };
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let nav = 0;
async function asActor(page, id, route) {
  await page.evaluate((id) => { const w = JSON.parse(localStorage.getItem('tq.world.v4')); w.session.actor = id; localStorage.setItem('tq.world.v4', JSON.stringify(w)); }, id);
  await page.goto(`${BASE}/?n=${++nav}#${route}`); await page.waitForSelector('.ds-app'); await sleep(500);
}
const go = (page, r) => page.evaluate((r) => { location.hash = r; }, r).then(() => sleep(500));
async function lastQ(page) { const qs = page.locator('.ds-thread .ds-
… [5796 more characters trimmed]
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:interaction-design", "args": "Talent Q public site (Direction D): landing + sample Q conversation, how it works with audience switch, employers, talent, pricing hypotheses, tr

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-30 12:29

Base directory for this skill: /root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/64191f50-3277-408e-9eca-3ef47f62a254/skills/interaction-design

# Interaction Design

You are an expert in interaction design — the discipline that defines how products behave in response to human input. Your recommendations are grounded in Dan Saffer's Microinteractions (trigger-rules-feedback-loops framework), Alan Cooper's About Face (product posture, perpetual intermediates, orchestration, excise), Donna Lichaw's The User's Journey (narrative arc, storymapping, peak-end design), the 12 Principles of Animation adapted for UI, David Harel's statecharts for UI state modeling, and motion guidelines from Material Design 3 and Apple HIG.

*Interaction design is the design of behavior. A product's visual appearance is what users see; its interaction design is what they experience. The gap between a product people tolerate and one they love is almost always in the quality of its interactions.*

---

## The Microinteraction Framework

Every interaction — from toggling a switch to submitting a form — consists of four parts (Saffer):

| Part | Definition | Key Question |
|------|-----------|-------------|
| **Trigger** | What initiates the interaction | How does the user (or system) start this? |
| **Rules** | The hidden logic that governs behavior | What happens, in what sequence, with what constraints? |
| **Feedback** | How the system communicates what's happening | What does the user see, hear, or feel? |
| **Loops & Modes** | How the interaction changes over time | Does this repeat? Expire? Adapt? |

### Triggers

**Manual triggers** (user-initiated): buttons, toggles, gestures, voice commands, keyboard shortcuts.

**System triggers** (automatic): notifications, location-based alerts, time-based events, state changes, error detection.

**Trigger design principles:**
1. **Bring the data forward** — Show essential information on the trigger itself. A mail icon with an unread count. A battery icon showing charge level. Don't force users to open something just to check status
2. **Match visibility to frequency** — High-use triggers should be prominent and always accessible. Infrequent triggers can be less visible
3. **Consistent behavior** — A trigger must initiate the same action every time. Inconsistency destroys trust
4. **Communicate state** — Triggers have states: normal, hover, active, disabled, updated. Each state must be visually distinct

### Rules

Rules define what happens when a trigger fires. Users never see rules directly — they experience them through feedback.

**Rules design principles:**
1. **Start with the goal** — What is the user trying to accomplish? Every rule serves this goal
2. **Don't start from zero** — Use smart defaults based on past behavior, user context, or common patterns. Remember what the user did last time
3. **Prevent errors, don't just catch them** — Apply the **Poka-Yoke principle**: design inputs that make incorrect actions impossible (dropdowns instead of free text, constrained sliders instead of number fields)
4. **Define every edge case** — What happens with empty input? Maximum values? Network failure? Interrupted actions? If you haven't designed for it, users will find it

### Feedback

Feedback makes the invisible rules visible. It's also where a product's personality lives.

| Type | Best For | Guidelines |
|------|----------|-----------|
| **Visual** | Most interactions | Near the trigger. Brief. Respect visual hierarchy. Don't compete with content |
| **Auditory** | Confirmations, alerts, background processes | Sparingly. Short. Avoid negative sounds — use positive ones. Always mutable |
| **Haptic** | Mobile/wearable confirmations, boundaries | Simple patterns. Confirm actions. Signal errors. Limited vocabulary |

**Feedback principles:**
1. **Convey the most with the least** — Minimal, purposeful. A subtle color change beats a modal dialog
2. **Match intensity to importance** — Routine confirmation: subtle. Error with data loss: prominent and persistent
3. **Feedback should diminish with repetition** — What's delightful on first use becomes annoying on the hundredth. Consider reducing feedback intensity for repeated actions
4. **Personality is appropriate in moderation** — A touch of character is good. Cute error messages that block work are not

### Loops and Modes

**Loops** govern repetition and timing:
- **Count-controlled**: Retry 3 times, then stop
- **Condition-controlled**: Keep checking until connected
- **Long loops ("The Long Wow")**: How the interaction evolves from first use to hundredth use — progressive disclosure, adaptive defaults, earned shortcuts

**Modes** alter functionality:
- **Settings mode**: Adjust parameters (alarm sound, snooze duration)
- **Spring-loaded mode**: Active only while physically held (long-press, key held down) — safest mode because user always knows it's active
- **One-off mode**: Activates for a single action, then reverts automatically

**Critical rule:** Minimize modes. Zero is ideal. One is acceptable if clearly visible. More than one in a microinteraction is a design smell.

---

## Product Posture

A product's posture determines how much attention it demands and how its interactions should be designed (Cooper).

| Posture | User Attention | Duration | Design Response |
|---------|---------------|----------|----------------|
| **Sovereign** | Full, focused attention | Hours | Rich controls, keyboard shortcuts, dense information, muted visual style. Target perpetual intermediates |
| **Transient** | Brief, task-focused | Seconds to minutes | Obvious UI, bright and clear, minimal options, remember user choices |
| **Daemonic** | None (background) | Continuous | Invisible when working. Surface only when there's a problem. Configure via a transient settings panel |

### Perpetual Intermediates

~80% of users are neither beginners nor experts — they're **perpetual intermediates** (Cooper). They've passed the learning phase but haven't memorized every feature.

**Design implications:**
- Optimize the interface for **intermediate** usage patterns, not beginners or experts
- Provide **multiple command modalities**: toolbar buttons (pedagogic/discoverable) + keyboard shortcuts (fast/memorized)
- Use **progressive disclosure**: show essential controls by default, hide advanced ones behind expandable panels
- **Inflect the interface**: place the most frequent functions in the most accessible locations
- Don't punish intermediates with beginner hand-holding they can't skip
- Don't hide essential functions behind expert-only mechanisms

---

## Orchestration and Flow

### Flow State

When interaction is well-designed, users enter a state of **flow** — focused, productive, unaware of the interface. The interface becomes transparent.

**Flow killers:**
- Modal dialogs interrupting work
- Confirmation prompts for reversible actions ("Are you sure?" — provide Undo instead)
- Navigation that breaks context
- Requiring users to re-enter information the system already has
- Errors that blame the user

### Harmonious Interaction Principles (Cooper)

1. **Follow mental models** — Design based on how users *think* it works, not how it's actually built
2. **Less is more** — Every additional element competes for attention
3. **Provide choices, don't ask questions** — Toggles and options > confirmation dialogs
4. **Keep tools close at hand** — Contextual toolbars, right-click menus, inline editing
5. **Provide modeless feedback** — Status information that doesn't interrupt. Progress indicators in the UI, not in a dialog
6. **Design for the probable, anticipate the possible** — Optimize the common path. Handle edge cases gracefully
7. **Avoid blank slates** — Empty states should guide, not stare blankly

---

## Narrative Structure in Product Design

Microinteractions define how individual moments behave. Narrative structure defines how those moments *compose* into an engaging experience. Products that people love don't just work well — they tell a story where the user is the hero. This framework, drawn from Donna Lichaw's storymapping approach, applies the same narrative arc used by screenwriters to the design of product flows.

### The Narrative Arc Applied to Products

Every story — and every product experience — follows the same arc:

| Plot Point | In Story | In Product | Design Question |
|---|---|---|---|
| **Exposition** | Introduces the world and characters | User arrives and orients | Is it immediately clear what this is and what I can do? |
| **Inciting incident** | Something disrupts the status quo | User encounters their task/goal | Does the product acknowledge the user's problem or need? |
| **Rising action** | Character takes steps, tension builds | User works through the flow | Does each step feel like progress? Does engagement build? |
| **Crisis** | Greatest obstacle, highest tension | User hits friction, doubt, or complexity | Is this friction intentional? Can the user overcome it? |
| **Climax** | Turning point, peak emotion | The payoff — the "aha!" or accomplishment | Is there a peak positive moment the user will remember? |
| **Falling action** | Things wind down | Confirmation, sharing, next steps | Does the product celebrate success and suggest what's next? |
| **End** | The new normal | User leaves with an impression | Is the ending designed deliberately? |

**The user is always the hero.** Your product is the tool that helps the hero achieve their goal — not the protagonist of the story.

### Three Types of Product Stories

| Story Type | What It Maps | Scale | Key Question |
|---|---|---|---|
| **Concept story** | The big picture — what this product is and why it matters | Product-level | "What is the story of this product?" |
| **Origin story** | How someone becomes a user for the first time | Acquisition + onboarding | "What's the story of a user's first experience?" |
| **Usage story** | How someone uses the product for a specific task | Single session or flow | "What's the story of using this feature?" |

#### Concept Story
The foundational narrative that communicates your core value proposition. Maps the product's reason for being onto the narrative arc.

- **Exposition:** Who is this for? What's their world like?
- **Inciting incident:** What problem disrupts their status quo?
- **Rising action:** What approaches have they tried?
- **Climax:** How does this product solve it in a way that surprises or delights?
- **End:** What does the user's world look like now?

A concept story without a climax is anticlimactic — "just another X." Find what makes your product surprising, delightful, or transformative.

#### Origin Story
The journey from awareness to first meaningful use. Bridges marketing and product design.

Key touchpoints to design as plot points: marketing materials → landing page → sign-up flow → onboarding → first meaningful interaction. Each should build on the last. The crisis is often "Another thing to sign up for?" — design the climax to answer it with immediate demonstrated value.

#### Usage Story
A single task or session mapped as a narrative arc. This is where storymapping connects most directly to interaction design.

- Map the moment-by-moment experience of completing a task
- Identify where the peak positive moment should be — the "boom"
- Design the ending deliberately — the peak-end rule means users judge the entire experience by its best moment and its ending

### Storymapping Process

1. **Define the story** — Who is the hero? What is their goal? Which story type are you mapping?
2. **Plot the arc** — Use sticky notes on a wall or a spreadsheet. One note per plot point. Map left to right chronologically
3. **Test the arc** — Read it aloud. Does it build? Is there real tension? Is the climax satisfying? If any plot point is weak, the whole story suffers
4. **Map to screens/interactions** — Each plot point becomes a screen, a state, or a key interaction moment
5. **Design the crisis deliberately** — Don't eliminate all friction. Some friction creates engagement. The satisfaction of overcoming the crisis is what makes the climax meaningful
6. **Design the climax** — This is the moment users will remember. Invest disproportionate design effort here
7. **Design the ending** — Confirmation, celebration, sharing, or a bridge to the next story

### Applying the Peak-End Rule

Research on how humans evaluate experiences (Kahneman) shows they judge by two moments: the **peak** (highest emotional intensity) and the **end** (final impression). The total duration and the average quality matter far less.

**Design implications:**
- **Identify your peak** — Every flow should have one moment designed to be the emotional high point
- **Invest in endings** — A weak ending undermines an otherwise good experience. Success states, confirmation screens, and "what's next" moments deserve as much design attention as the core workflow
- **Acceptable friction** — If the peak and ending are strong, users will tolerate friction along the way. Don't over-optimize the middle at the expense of the climax
- **Measure peaks and endings** — In usability testing, ask: "What stands out?" and "How did it end?" These reveal the remembered experience

### When to Use Storymapping

| Situation | Story Type to Map |
|---|---|
| Designing a new product or major feature | Concept story first, then origin story |
| Improving onboarding or activation | Origin story |
| Designing or improving a specific flow | Usage story |
| Diagnosing why users aren't engaged | All three — find which story is broken |
| Pitching a product vision to stakeholders | Concept story as the narrative backbone |

---

## Excise

Excise is work that doesn't contribute to the user's goal (Cooper). Every click, scroll, page navigation, or moment of confusion that isn't directly accomplishing what the user wants is excise. Eliminate it.

### Four Types of Excise

| Type | Definition | Examples |
|------|-----------|----------|
| **Cognitive** | Comprehending product behavior, decoding layouts | Unclear labels, ambiguous icons, complex jargon |
| **Memory** | Remembering commands, locations, passwords, settings | Forgetting where a setting lives, re-entering the same data |
| **Visual** | Figuring out where to look, finding items, decoding hierarchy | Cluttered screens, poor contrast, undifferentiated lists |
| **Physical** | Unnecessary clicks, mouse travel, mode switching | Deep navigation, distant controls, repeated scrolling |

### Navigational Excise (Most Prevalent)

Navigation is the most common source of excise. Reduce it:
- **Reduce places to go** — Flatten hierarchies. Combine related functions
- **Provide signposts** — Breadcrumbs, active states, location indicators
- **Provide overviews** — Dashboards, summaries, previews
- **Don't force window/screen switching** — If a function affects the current context, perform it in the current context
- **Don't replicate mechanical-age models** — Digital products shouldn't mimic physical limitations

### The Excise Test

For every interaction step, ask: "Does this directly help the user achieve their goal?"
- **Yes** → Keep it, optimize it
- **No** → Eliminate it, automate it, or hide it behind progressive disclosure

---

## State Design

### Every Element Has States

Design every interactive element across all its possible states:

| State | When | Required Visual Change |
|-------|------|----------------------|
| **Default** | Resting, ready | Base appearance |
| **Hover** | Cursor over (desktop) | Subtle highlight, cursor change |
| **Focus** | Keyboard navigation | Visible focus ring (2px, 3:1 contrast) |
| **Active/Pressed** | Being activated | Depressed appearance, scale reduction |
| **Disabled** | Not currently available | Reduced opacity (40%), no pointer events |
| **Loading** | Awaiting data/response | Skeleton or spinner replacing content |
| **Empty** | No data to display | Illustration + guidance + action |
| **Error** | Something went wrong | Error color + message + recovery path |
| **Success** | Action completed | Confirmation + next step |
| **Selected** | Chosen in a multi-select | Accent border or background |
| **Expanded/Collapsed** | Toggle content visibility | Arrow/chevron rotation + content reveal |
| **Dragging** | Being repositioned | Elevated shadow, ghost at origin |

### State Machines

For complex interactions, model behavior as a **finite state machine**:

```
[Idle] --click--> [Loading] --success--> [Displaying Data]
                             --error--> [Error State]
[Error State] --retry--> [Loading]
[Displaying Data] --refresh--> [Loading]
                  --delete--> [Confirming]
[Confirming] --confirm--> [Deleting] --done--> [Idle]
             --cancel--> [Displaying Data]
```

**Benefits:**
- Makes impossible states impossible (you can't delete while loading)
- Forces you to define every transition explicitly
- Reveals missing states early (what happens on timeout?)
- Serves as documentation developers can implement directly

---

## Responsiveness Thresholds

| Duration | User Perception | Design Response |
|----------|----------------|-----------------|
| 0-100ms | Instantaneous | No feedback needed beyond the state change |
| 100ms-1s | Responsive, slight delay | Show the result. Skeleton or subtle indicator if near 1s |
| 1-10s | Noticeable wait | Progress indicator. Explain what's happening. Allow cancellation |
| 10s+ | Losing attention | Persistent progress with estimate. Background the task. Notify on completion |

**Critical rule:** Never leave users without feedback for more than 1 second. If an action takes longer, show something immediately (skeleton, spinner, message) even before the result arrives.

---

## Gesture Patterns

### Touch Gestures

| Gesture | Action | When to Use |
|---------|--------|-------------|
| **Tap** | Select, activate | Primary action on any touchable element |
| **Long press** | Secondary action, context menu | Less discoverable — always provide an alternative path |
| **Swipe** | Navigate, dismiss, reveal actions | Natural for lists, cards, pages. Show affordance on first use |
| **Pinch/Spread** | Zoom in/out | Maps, images, documents. Bidirectional |
| **Drag** | Reorder, move, resize | Show drop targets. Provide haptic feedback at thresholds |
| **Pull down** | Refresh | Lists and feeds. Show progress animation |

### Gesture Design Rules

1. **Never use gestures as the only path** — Always provide a visible alternative (button, menu item)
2. **Provide feedback during the gesture** — The element should respond in real-time to the finger, not just after release
3. **Respect the platform** — iOS swipe-back, Android back button. Don't override system gestures
4. **Teach through progressive disclosure** — Show gesture hints on first encounter, then fade them
5. **Touch targets minimum 44×44px** (Apple HIG) or 48×48dp (Material) — smaller targets cause errors

---

## Common Mistakes

| Mistake | Why It Fails | Instead |
|---------|-------------|---------|
| Designing only the happy path | Real users encounter errors, empty states, slow connections, edge cases | Design every state for every element |
| Confirming every action with a dialog | Interrupts flow, teaches users to click "OK" without reading | Provide Undo instead of asking permission |
| Identical feedback for different outcomes | User can't tell if their action succeeded, failed, or is still processing | Differentiate success, error, and loading feedback clearly |
| Gestures without visible alternatives | Users who don't discover the gesture are stuck | Always pair gestures with a visible control |
| Animations that block interaction | Users wait for an animation to finish before they can act | Keep animations under 300ms for direct interactions. Never block input |
| Ignoring keyboard users | Keyboard navigation is broken or invisible | Design focus order, visible focus states, and keyboard shortcuts |
| Complex modes without clear indicators | Users don't know which mode they're in and get unexpected behavior | Minimize modes. If unavoidable, make the current mode impossible to miss |

---

## Reference Files

Load these for deeper guidance on specific topics:

- `references/microinteractions.md` — The four-part framework in depth: trigger design, rule logic, feedback types, loops and modes, with design patterns for each
- `references/product-behavior.md` — Product postures, perpetual intermediates, smart and considerate product behavior, orchestration, flow, and excise elimination
- `references/state-and-transitions.md` — State machines for UI, gesture patterns, responsive behavior, drag-and-drop, and keyboard interaction
- `references/motion-principles.md` — Animation principles adapted for UI, timing and easing guidelines, motion tokens, reduced motion, and Material/Apple motion patterns
- `references/error-prevention.md` — Error prevention hierarchy, undo patterns, inline validation, empty states, loading patterns, and recovery flows

## Templates

- `templates/microinteraction-spec-template.md` — Complete specification for a single microinteraction using the four-part framework
- `templates/state-inventory-template.md` — State audit for all interactive elements in a feature or screen

## Examples

- `examples/microinteraction-walkthrough.md` — Designing a "favorite" toggle interaction end-to-end
- `examples/interaction-audit-walkthrough.md` — Auditing and improving interactions in a fictional product


ARGUMENTS: Talent Q public site (Direction D): landing + sample Q conversation, how it works with audience switch, employers, talent, pricing hypotheses, trust, simulated sign-in (email code, Google, Microsoft). States: loading, ready, empty, error, permission denied, accessible alternative, mobile.

- 🔧 `Skill`: {"skill": "design-skills:ux-writing", "args": "Public marketing copy for Talent Q: honest, hypothesis-labelled pricing, trust page, sample Q answers, sign-in errors."}

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-30 12:29

Base directory for this skill: /root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/64191f50-3277-408e-9eca-3ef47f62a254/skills/ux-writing

# UX Writing

Write clear, concise, user-centered interface copy (UX text/microcopy) for digital products and experiences. This skill provides frameworks, patterns, and best practices for creating text that helps users accomplish their goals.

## When to Use This Skill

Use this skill when:
- Writing interface copy (buttons, labels, titles, messages, forms)
- Editing existing UX text for clarity and effectiveness
- Creating error messages, notifications, or success messages
- Designing conversational flows or onboarding experiences
- Establishing voice and tone for a product
- Auditing product content for consistency and usability

## Core UX Writing Principles

### The Four Quality Standards

Every piece of UX text should be:

1. **Purposeful** — Helps users or the business achieve goals
2. **Concise** — Uses the fewest words possible without losing meaning
3. **Conversational** — Sounds natural and human, not robotic
4. **Clear** — Unambiguous, accurate, and easy to understand

### Key Best Practices

**Conciseness**
- Use 40-60 characters per line maximum
- Every word must have a job
- Break dense text into scannable chunks
- Front-load important information
- Eliminate deadwood phrases ("in order to" → "to", "due to the fact that" → "because", "at this point in time" → "now")
- Replace phrasal verbs with direct verbs ("find out" → "discover", "set up" → "configure", "carry out" → "perform")
- Avoid stacking modifiers — one adjective is usually enough

**Clarity**
- Use plain language (7th grade reading level for general, 10th for professional)
- Avoid jargon, idioms, and technical terms
- Use consistent terminology throughout
- Choose meaningful, specific verbs
- Avoid discriminatory or exclusionary language (gendered defaults, ableist idioms, culturally specific metaphors)

**Conversational Tone**
- Write how you speak
- Use active voice 85% of the time
- Include prepositions and articles
- Avoid robotic phrasing

**User-Centered**
- Focus on user benefits, not features
- Anticipate and answer user questions
- Use second-person ("you") language
- Match user's language and mental models

## UX Text Patterns

Apply these common patterns for interface elements.

### Titles
- **Purpose**: Orient users to where they are
- **Format**: Noun phrases. **Page titles, modal/dialog titles, and menu/navigation items use title case** (see Capitalization below for title-case mechanics). **Lower-level headings (H3+), figure captions, callouts, and table titles use sentence case.**
- **Types**: Brand titles, content titles, category titles, task titles
- **Examples**:
  - Page title (title case): "Account Settings", "Your Library", "Run Payroll"
  - Lower-level heading (sentence case): "Recent activity", "Bank account details", "Tax withholdings"

### Buttons and Links
- **Purpose**: Enable users to take action
- **Format**: Active imperative verbs, sentence case
- **Pattern**: `[Verb] [object]` 
- **Examples**: "Save changes", "Delete account", "View details"
- **Avoid**: Generic labels like "OK", "Submit", "Click here"

### Error Messages
- **Purpose**: Explain problem and provide solution
- **Format**: Empathetic, clear, actionable
- **Pattern**: `[What failed]. [Why/context]. [What to do].`

**Error Message Types**

**Validation Errors (Inline)**
- Show as user completes field or on blur
- Brief, specific guidance to correct input
- Pattern: `[Field] [specific requirement]`
- Examples:
  - "Email must include @"
  - "Password must be at least 8 characters"
  - "Choose a date in the future"
- Timing: Real-time or on field exit
- Location: Below or beside the field

**System Errors (Modal/Banner)**
- Show when backend operations fail
- Explain what happened and why
- Pattern: `[Action failed]. [Likely cause]. [Recovery step].`
- Examples:
  - "Payment failed. Your card was declined. Try a different payment method."
  - "Couldn't save changes. Connection lost. Reconnect and try again."
  - "Upload failed. File is too large. Choose a file under 10MB."
- Timing: Immediately after failure
- Location: Modal dialog or prominent banner

**Blocking Errors (Full-screen)**
- Prevent continued use until resolved
- Clear explanation of blocker and resolution
- Pattern: `[What's blocked]. [Why]. [Specific action needed].`
- Examples:
  - "Update required. This version is no longer supported. Update now to continue."
  - "Subscription expired. Your account is paused. Renew subscription to restore access."
  - "Verification needed. Confirm your email to access features. Check your inbox."
- Timing: On app launch or feature access
- Location: Full screen or large modal

**Permission Errors**
- Explain benefit before requesting permission
- Pattern: `[User benefit]. [Permission needed].`
- Examples:
  - "Get notified when orders ship. Enable notifications."
  - "Find nearby stores. Allow location access."
  - "Back up your photos. Grant storage permission."
- Timing: When feature is first used
- Location: In context of the feature

**What to Avoid**
- Technical codes without explanation ("Error 403")
- Blame language ("invalid input", "illegal character")
- Robotic tone ("An error has occurred")
- Dead ends (error with no recovery path)
- Vague causes ("Something went wrong")

### Success Messages
- **Purpose**: Confirm action completion
- **Format**: Past tense, specific, encouraging
- **Pattern**: `[Action] [result/benefit]`
- **Examples**: "Changes saved", "Email sent", "Profile updated"

### Empty States
- **Purpose**: Guide users when content is absent
- **Types**: First-use, user-cleared, error/no results
- **Format**: Explanation + CTA to populate
- **Example**: "No messages yet. Start a conversation to connect with your team."

### Form Fields
- **Labels**: Clear noun phrases describing input ("Email address", "Phone number")
- **Instructions**: Verb-first, explain why information is needed
- **Placeholder**: Use sparingly, only for standard inputs like "name@example.com"
- **Helper text**: Static, on-demand, or automatic based on importance

### Notifications
- **Purpose**: Deliver timely, valuable information
- **Types**: Action-required (intrusive), Passive (less intrusive)
- **Format**: Verb-first title + contextual description
- **Example**: "Update required. Install the latest version to continue."

## Formatting & Style Conventions

### Capitalization

- **Sentence case** (default): Body text, descriptions, helper text, error messages, success messages, tooltips, placeholder text, **button labels**, lower-level (H3+) headings, figure captions, callouts, table titles
- **Title case**: Page titles, modal/dialog titles, menu and navigation items, form field labels
- **All-caps**: Reserved for **short overline / eyebrow labels** (≤3 words) that sit above a heading or metric — e.g., stat-card section headers like `EMPLOYEES`, `TOTAL PAY`, `LAST UPDATED`, category tags over KPI values — and for **acronyms** (`PDF`, `URL`, `API`, `EIN`, `SSN`). For short category overlines it's an intentional typographic signal, not shouting. **Do not** use all-caps for prose, button labels, error messages, page titles, tabs/menu labels, or any string longer than ~3 words — beyond that length readability drops sharply and it reads as shouting.

**Title case mechanics** (applies wherever title case is used):

- Capitalize the first and last word of the title regardless of part of speech.
- Capitalize all adjectives, adverbs, and nouns.
- Capitalize all pronouns (including "it").
- Capitalize all verbs, including the verb "to be" in all forms (is, are, was, has been, etc.).
- Capitalize "no", "not", and the interjection "O".
- Do **not** capitalize articles ("a", "an", "the") unless first or last in the title.
- Do **not** capitalize coordinating conjunctions ("and", "or", "nor", "but", "for", "yet", "so") unless first or last in the title.
- Do **not** capitalize "to" (with or without an infinitive) unless first or last in the title.
- Do **not** capitalize prepositions (e.g., "in", "on", "at", "by", "of", "with") unless first or last in the title.

Examples:
- "Run Payroll for the Pay Period"
- "Add a New Employee"
- "How to File Quarterly Taxes"

**Edge cases:**

- **"Coming soon"** is the canonical future-feature label everywhere it appears (badges, callouts, copy). Even when used in a title-cased context, write it sentence case. Do not expose milestone granularity ("Coming at Beta", "Coming at GA") in user-facing strings.
- **Dropdown action items** (imperative-verb items inside a button-triggered menu, e.g. `"Add employee"`, `"See payroll runs"`, `"Export report"`) are treated as **buttons → sentence case**, not as static navigation menu items. The "menu items use title case" rule applies to **navigational** menus (side nav, breadcrumbs, top-level nav links pointing to pages), not action menus.
- **Buttons that reference a named page** (e.g. `"Go to Setup Wizard"`, `"Back to Payroll Hub"`, `"Open Time Review"`) **preserve the page name's title case** while the surrounding button copy stays sentence case. The page name is a proper noun in this context.

### Numbers and Dates

- Use numerals, not words ("12" not "twelve") — saves space and scans faster.
- Spell out the month in dates: "August 5, 2025" or "5 August 2025" — never "8/5/2025" or "8.5.2025" (ambiguous across locales).
- Spell out day of the week and month; abbreviate only when space is constrained (e.g., tables, mobile): "Sat., Jan. 24".
- **Avoid ordinal suffixes** in dates: write "August 5", not "August 5th"; write "May 1", not "May 1st".
- **Year ranges** use a hyphen with the full year on both sides: "2015-2016", not "2015-16" and not "2015 to 2016".

### Tense

- Prefer past tense over present perfect for status messages: "File uploaded" not "File has been uploaded"
- Present perfect adds words without adding meaning in most UI contexts

### Abbreviations

- Only use abbreviations your users will immediately understand (common: PDF, URL, ID)
- Spell out on first use if there's any doubt, then abbreviate after: "application programming interface (API)"
- Latin abbreviations (e.g., i.e., etc.) — use proper punctuation: period after each letter, comma before and after in a sentence
- When in doubt, spell it out

## Voice and Tone

### Voice (Consistent Brand Personality)
Voice is the consistent personality of the product. Establish voice using:
- **Concepts**: 3-5 key brand principles/values
- **Voice characteristics**: Descriptive adjectives for each concept
- **Do/Don't examples**: Concrete examples showing voice in action

See references/voice-chart-template.md for creating a voice chart.

### Tone (Adaptive to Context)
Tone is how voice adapts to specific situations. While voice remains constant, tone shifts based on user context and emotional state.

**Tone Variables**
- **Purpose**: Why user is seeing this text (information, action, confirmation)
- **Context**: What user is trying to do (learning, completing task, recovering from error)
- **Emotional state**: How user likely feels (frustrated, excited, confused, cautious)
- **Stakes**: Impact of the action (low: changing theme, high: deleting account)

**Tone Adaptation by User Emotional State**

**Frustrated** (errors, failures, blockers)
- Empathetic and solution-focused
- Acknowledge the problem without blame
- Provide clear recovery path
- Example: "Payment failed. Your card was declined. Try a different payment method."

**Confused** (first use, complex features)
- Patient and explanatory
- Break down steps clearly
- Provide context and guidance
- Example: "Connect your bank to see spending insights. We'll guide you through it."

**Confident** (routine tasks, return visits)
- Efficient and direct
- Minimal explanation
- Quick confirmation
- Example: "Saved"

**Cautious** (high-stakes actions, data loss)
- Serious and transparent
- Clear consequences
- Respectful of user's decision
- Example: "Delete account? You'll lose all data and this can't be undone."

**Successful** (completions, achievements)
- Positive and encouraging
- Proportional to achievement
- Brief celebration
- Example: "Profile updated. Your changes are live."

**Tone Adaptation by Content Type**

**Error messages**: Empathetic, reassuring, solution-focused
- Never blame user
- Explain what happened
- Provide clear next step

**Success messages**: Positive, specific, encouraging
- Confirm what happened
- Proportional to action importance
- Brief and clear

**Instructions**: Clear, direct, helpful
- Front-load key action
- Explain why when needed
- Use simple steps

**Onboarding**: Inviting, encouraging, concise
- Welcome without overwhelming
- Focus on value
- Celebrate early wins

**Confirmations**: Serious, transparent, respectful
- Clear about consequences
- No manipulation
- Easy to back out

**Empty states**: Hopeful, actionable, guiding
- Explain why it's empty
- Provide clear next action
- Keep encouraging tone

## Editing Process

Edit UX text in four phases:

### Phase 1: Purposeful
- Does text help user achieve their goal?
- Does text serve business objectives?
- Is value to user clear?
- Are concerns anticipated and addressed?

### Phase 2: Concise
- Remove unnecessary words
- Combine redundant information
- Ensure every word earns its space
- Front-load important concepts

### Phase 3: Conversational
- Read aloud—would you say this?
- Use active voice (unless passive is clearer)
- Include natural connecting words
- Avoid corporate jargon

### Phase 4: Clear
- Use specific, accurate verbs
- Maintain consistent terminology
- Test readability (Hemingway Editor, Flesch-Kincaid)
- Ensure unambiguous meaning

## Workflow

1. **Understand context**
   - User goals and needs
   - Business objectives
   - Technical constraints
   - Emotional state of user

2. **Draft content**
   - Start with conversation (what would you say?)
   - Apply appropriate pattern
   - Consider voice and tone
   - Front-load important information

3. **Edit iteratively**
   - Phase 1: Purposeful
   - Phase 2: Concise
   - Phase 3: Conversational
   - Phase 4: Clear

4. **Test and measure**
   - Review with team
   - Test with users when possible
   - Measure task completion, comprehension
   - Iterate based on feedback

## Accessibility in UX Writing

Writing accessible content ensures all users, including those using assistive technology, can understand and interact with your product.

### Core Accessibility Principles

**Screen Reader Optimization**
- Label all interactive elements explicitly ("Submit form" not just "Submit")
- Write descriptive link text ("Read pricing details" not "Click here")
- Structure error messages to work with screen readers (error + field label read together)
- Use ARIA labels when visual context isn't sufficient

**Cognitive Accessibility**
- Target 8-14 words per sentence (8 words = 100% comprehension, 14 words = 90%)
- Break complex information into scannable chunks
- Use clear headings and logical hierarchy
- Provide consistent, predictable patterns

**Multi-Modal Communication**
- Don't rely on color alone to convey meaning
- Pair visual indicators with text ("Error: Email required" with red icon)
- Provide text alternatives for icons and images
- Ensure sufficient color contrast (WCAG AA minimum: 4.5:1)

**Plain Language for All**
- Target 7th-8th grade reading level for general audience
- Define technical terms when first used
- Avoid idioms, metaphors, and cultural references
- Use common, everyday words

### Accessible Pattern Examples

**Buttons**
- ❌ Poor: "Submit" (context missing for screen readers)
- ✅ Good: "Submit application"

**Links**
- ❌ Poor: "Click here for more information"
- ✅ Good: "Read our privacy policy"

**Error Messages**
- ❌ Poor: Red text showing "Invalid"
- ✅ Good: "Error: Email must include @" (with error icon)

**Form Labels**
- ❌ Poor: Placeholder-only fields
- ✅ Good: Visible label + optional placeholder

## UX Text Benchmarks

Use these research-backed metrics to create effective UX text.

### Sentence Length Targets

**By Content Type**
- **Buttons/CTAs**: 2-4 words ideal, 6 word maximum
- **Titles**: 3-6 words, 40 characters maximum
- **Error messages**: 12-18 words (including solution)
- **Instructions**: 20 words maximum, 14 ideal
- **Body copy**: 15-20 words per sentence average
- **Notifications**: 10-15 words for title + body

**Comprehension Rates**
- 8 words or fewer: 100% user comprehension
- 14 words or fewer: 90% user comprehension
- 25 words: Maximum before significant comprehension drop

### Character and Line Length

**Optimal Ranges**
- **Line length**: 40-60 characters for maximum readability
- **Button labels**: 15-25 characters
- **Page titles**: 30-50 characters
- **Notification titles**: 35-45 characters

### Reading Level Guidelines

**By Audience**
- **General public**: 7th-8th grade (Flesch-Kincaid)
- **Professional tools**: 9th-10th grade
- **Technical products**: 10th-11th grade
- **Specialized fields**: 11th-12th grade (only when necessary)

**Testing Tools**
- Hemingway Editor: Highlights complex sentences
- Readable.com: Provides multiple readability scores
- Microsoft Word: Built-in Flesch-Kincaid scoring

## Common Mistakes to Avoid

- Using passive voice excessively
- Generic button labels ("Submit", "OK")
- Blaming users in error messages
- Overly clever humor in serious contexts
- Inconsistent terminology
- Hidden instructions or explanations
- System-oriented language vs. user language
- Too many words (not concise enough)
- Robotic, corporate tone
- Relying on color alone for meaning
- Writing inaccessible link text ("Click here")

## Quick Reference

**Sentence case**: "Save your changes" (not "Save Your Changes")  
**Active imperative for buttons**: "Delete account" (not "Account deletion")  
**User-focused**: "Save time with shortcuts" (not "We offer shortcuts")  
**Specific verbs**: "Delete" (not "Remove" when permanently deleting)  
**Front-loaded**: "Password must be 8 characters" (not "Must be 8 characters for your password")

## Style references

External references this skill is grounded in (consult these for any case the skill doesn't cover):

- **The Chicago Manual of Style** — fallback for grammar, punctuation, and citation questions.
- **The Merriam-Webster Dictionary** — fallback for spelling and word choice.

## Resources

This skill includes:
- **references/accessibility-guidelines.md**: Comprehensive guide to writing accessible UX text for all users
- **references/voice-chart-template.md**: Template for creating a product voice chart
- **references/content-usability-checklist.md**: Comprehensive checklist for evaluating UX text quality
- **references/patterns-detailed.md**: Extended examples of UX text patterns in different voices
- **examples/real-world-improvements.md**: Before/after transformations with detailed analysis and scoring
- **templates/error-message-template.md**: Fillable template for writing effective error messages
- **templates/empty-state-template.md**: Guide for creating helpful empty states
- **templates/onboarding-flow-template.md**: Framework for designing clear onboarding experiences


ARGUMENTS: Public marketing copy for Talent Q: honest, hypothesis-labelled pricing, trust page, sample Q answers, sign-in errors.

- 🔧 `Skill`: {"skill": "design-skills:design-elevation", "args": "Talent Q public pages in Direction D (ink, paper, gold for Q only; Fraunces/Inter Tight/IBM Plex Mono). No new aesthetics."}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-30 12:29

Base directory for this skill: /root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/64191f50-3277-408e-9eca-3ef47f62a254/skills/design-elevation

# Design Elevation System

This skill transforms functional visual outputs into polished, professional designs by applying systematic design thinking and refinement protocols.

## Design Philosophy

Follow Alla Kholmatova's design systems framework: every design decision is either a **functional pattern** (what users interact with — structure, layout, components) or a **perceptual pattern** (how it feels — color, typography, spacing, motion). Both layers must be intentional.

### Canonical Design Tokens: Tailwind CSS

All design decisions should map to **Tailwind CSS** as the shared design language. This means:
- Colors from Tailwind's palette (gray, blue, emerald, amber, rose, violet, etc.)
- Spacing from Tailwind's scale (1 = 0.25rem/4px, 2 = 0.5rem/8px, 4 = 1rem/16px, etc.)
- Typography from Tailwind's type scale (text-xs through text-9xl)
- Border radius from Tailwind's system (rounded-sm through rounded-2xl)
- Shadows from Tailwind's elevation (shadow-sm through shadow-2xl)

When writing CSS or HTML, use Tailwind utility classes. When defining design tokens for other formats (presentations, documents), translate Tailwind values into the target medium.

## Activation Protocol

When creating ANY visual output:

1. **Start with function** — Create a working version first
2. **Define functional patterns** — What does the user interact with? What's the structure? Use `references/grid-systems.md`
3. **Define perceptual patterns** — How should it feel? What's the personality? Use `references/elevation-protocol.md`
4. **Apply interrogation** — Question every default choice using `references/design-interrogation.md`
5. **Elevate with techniques** — Use specific moves from `references/technique-catalog.md`
6. **Polish data visualizations** — If any charts/data, apply `references/data-visualization.md`
7. **Final check** — Ensure output feels hand-crafted, not templated

## Functional Patterns by Output Type

### For Presentations (PPTX)
- Start with information hierarchy, not decoration
- Apply grid systems from `references/grid-systems.md`
- One idea per slide — if it needs two ideas, it needs two slides
- Build complexity gradually across the slide sequence

### For Dashboards & Data Visualization
- Begin with data relationships, not chart types
- Apply Tufte's data-ink ratio from `references/data-visualization.md`
- Structure: KPI bar → Primary chart → Supporting charts → Detail tables
- Use small multiples over multi-series charts when comparing 4+ categories
- Default to Tailwind's gray scale for non-data elements; reserve color for data

### For Documents & Reports
- Structure with clear typographic hierarchy
- Apply document grids from `references/grid-systems.md`
- Use Tailwind's type scale for consistent sizing

### For Web/HTML Artifacts
- Design with responsive grid foundations (Tailwind's grid/flex utilities)
- Use Tailwind utility classes directly
- Apply animation restraint — `transition-all duration-200 ease-out` as default

## Perceptual Patterns

### Typography Excellence
Tailwind's type scale is the foundation. Layer these refinements:
- Use `font-sans` (Inter/system) for UI, `font-serif` for editorial
- Apply `tracking-tight` for display text (text-3xl and above)
- Apply `leading-relaxed` for body text
- Use `font-semibold` for emphasis over `font-bold` — subtler hierarchy
- For numbers in data contexts: always `tabular-nums`
- Refer to `references/typography-scales.md` for scale selection

### Color Sophistication
Tailwind's palette is the source of truth:
- Build from `gray` neutrals (not pure black/white)
- `text-gray-900` for primary text, `text-gray-500` for secondary, `text-gray-400` for tertiary
- `bg-white` or `bg-gray-50` for backgrounds — never stark white with stark black
- Accent color: pick ONE from Tailwind's palette (blue, emerald, violet, etc.)
- Apply 60-30-10: 60% neutrals, 30% secondary, 10% accent
- Refer to `references/color-systems.md` for full system

### Spatial Systems
Tailwind's spacing scale provides the rhythm:
- Base unit: `4` (1rem / 16px) for most UI
- Component padding: `p-4` to `p-6` (16-24px)
- Section spacing: `py-12` to `py-20` (48-80px)
- Gaps: `gap-4` for tight, `gap-6` for comfortable, `gap-8` for spacious
- Use Tailwind's spacing scale exclusively — no arbitrary values
- Refer to `references/spacing-systems.md` for patterns

### Visual Refinement
- Border radius: `rounded-lg` as default for cards, `rounded-md` for buttons
- Borders: `border border-gray-100` for subtle card separation
- Shadows: `shadow-sm` for cards; reserve `shadow-lg` for modals/overlays
- Hover states: `hover:bg-gray-50` for interactive elements
- Transitions: `transition-colors duration-150` as default

## Design Exemplars

Use these as **illustrations of principles**, not as the system itself. The system is Tailwind + Kholmatova's framework. These exemplars show what excellence looks like:

- **Stripe**: Gradient sophistication, precise type, technical content made beautiful
- **Linear**: Dark mode mastery, keyboard-first, minimal and precise
- **Apple**: Scale contrasts, photography integration, restraint as premium
- **Swiss/International Style**: Grid discipline, objective clarity, mathematical spacing
- **IBM Carbon**: Sharp corners (0px radius), IBM Plex type family, 2x grid, four-theme architecture
- **Shopify Polaris**: Merchant-friendly, warm neutrals, dark primary buttons, 13px body, rounded cards
- **Adobe Spectrum**: Four color themes, two scale modes, three-layer token architecture, creative-tool patterns
- **Salesforce Lightning**: CRM-optimized, brand blue #0176d3, slds- utility classes, record-detail patterns

Refer to `references/design-exemplars.md` for specific techniques to borrow.

### IBM Carbon Override

When building for IBM products or when Carbon styling is requested, **Carbon tokens override Tailwind defaults**:
- Font: IBM Plex Sans (not Inter), body at 14px
- Primary: `#0f62fe` Blue 60 (not Tailwind blue-600)
- Border radius: `0` everywhere (not `rounded-lg`) — Carbon's signature sharp corners
- Text: `#161616` Gray 100 (not Tailwind gray-900)
- Layers: alternating white/gray-10 (`#f4f4f4`) for depth
- Full reference: `references/carbon-design-system.md`

### Shopify Polaris Override

When building Shopify apps or when Polaris styling is requested, **Polaris tokens override Tailwind defaults**:
- Font: Inter, body at 13px (not 16px)
- Primary buttons: `#303030` dark (not blue!)
- Interactive/links: `#005bd3`
- Page background: `#f1f1f1` (not white)
- Border radius: `8px` for cards, `6px` for buttons
- Full reference: `references/polaris-design-system.md`

### Adobe Spectrum Override

When building Adobe products or when Spectrum styling is requested, **Spectrum tokens override Tailwind defaults**:
- Font: Adobe Clean / Source Sans Pro, body at 14px
- Accent: `#0D80D8` (light) / `#2A9AF4` (dark)
- Border radius: `4px` for controls, `8px` for cards
- Four themes: Lightest, Light, Dark, Darkest
- Two scales: Medium (desktop), Large (touch)
- Full reference: `references/spectrum-design-system.md`

### Salesforce Lightning Override

When building Salesforce apps or when Lightning/SLDS styling is requested, **SLDS tokens override Tailwind defaults**:
- Font: Salesforce Sans, body at 13px
- Brand: `#0176d3` (not Tailwind blue-600)
- Border radius: `4px` (0.25rem) everywhere
- Text: `#181818` (not Tailwind gray-900)
- Uses `slds-` prefix utility classes
- Full reference: `references/lightning-design-system.md`

## Critical Design Moves (Quick Reference)

### Make it feel intentional
- Replace `#000000` with `text-gray-900`
- Replace `#ffffff` with `bg-gray-50` for backgrounds
- Use `rounded-lg` consistently, not mixed radii
- Apply one spacing scale throughout

### Make it feel premium
- Generous whitespace — `p-8` or `p-12` on hero sections
- Tight tracking on display text: `tracking-tight`
- Colored shadows: `shadow-blue-500/10` instead of black
- Subtle borders: `border-gray-100` instead of `border-gray-300`

### Make it feel clean
- Remove borders and use whitespace to separate
- Reduce to 2-3 type sizes maximum per view
- Single accent color
- `text-gray-500` for supporting text, not smaller type

### Make data feel clear
- Title states the finding, not the chart type
- Direct labels over legends
- Gray out non-essential series
- `tabular-nums` on all number columns
- Source attribution in `text-xs text-gray-400`

## Resource Loading Priority

For efficiency, load resources in this order:
1. `references/elevation-protocol.md` — Always load first
2. `references/data-visualization.md` — Load when any data/charts involved
3. `references/technique-catalog.md` — Load for specific techniques
4. `references/design-interrogation.md` — Load for quality checks
5. `references/carbon-design-system.md` — Load when IBM/Carbon styling is requested
6. `references/polaris-design-system.md` — Load when Shopify/Polaris styling is requested
7. `references/spectrum-design-system.md` — Load when Adobe/Spectrum styling is requested
8. `references/lightning-design-system.md` — Load when Salesforce/Lightning styling is requested
9. Context-specific references (color, typography, spacing, grids) as needed

## Output Standards

Every delivered visual should:
- Use Tailwind's design tokens consistently (or their translated equivalents)
- Show clear functional patterns (structure, hierarchy, interaction)
- Express coherent perceptual patterns (color, type, spacing, motion)
- Demonstrate data integrity (if data is present, follow Tufte's principles)
- Feel intentionally designed, not defaulted
- Balance boldness with restraint

## Silent Execution

Unless explicitly asked, apply all design thinking internally. The user sees only the polished result. Document design decisions in code comments for HTML/CSS, or in speaker notes for presentations, but don't explain the process unless requested.

Great design is invisible when done right. The user should feel the quality without seeing the effort.


ARGUMENTS: Talent Q public pages in Direction D (ink, paper, gold for Q only; Fraunces/Inter Tight/IBM Plex Mono). No new aesthetics.

- 🔧 `Skill`: {"skill": "design-superpowers:creative", "args": "Visual direction for Talent Q public site inside Direction D only (ink/paper/gold-is-Q, existing type). No new aesthetics, typefaces or colours. Need:

  <details><summary>result</summary>

```
Launching skill: design-superpowers:creative
```
  </details>


**User** · 2026-10-30 12:29

Base directory for this skill: /root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/creative

# /creative — Creative Direction

Router for creative-direction sub-agents. Use when no design language exists yet (L0/L1) or when refreshing one (L2/L3).

## Maturity Detection

Follow `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/maturity-detection.md`. Run detection before routing.

- **L0 (Greenfield):** Full creative freedom — all options open. Output feeds into DESIGN.md via /map-design after exploration.
- **L1 (DESIGN.md exists):** Refine the existing design language. Load DESIGN.md as a constraint. Propose additions that extend it coherently. Refresh requests route to Refresh Strategist; the refresh lands as DESIGN.md updates.
- **L2 (DS exists):** Work within the design system. Respect existing tokens; only propose net-new additions not already covered. Refresh proposals map to token/component migrations executed via /ds-make.
- **L3 (Enterprise DS):** DS-constrained. Delegate any token creation proposals to /ds-make. Restrict to exploration and visual rationale.

Always announce the detected level before proceeding.

## Figma inspection

If a request asks you to look at, refresh, or pull references from a Figma file (e.g. "moodboard from our current file", "explore within our existing screens"), route through `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/figma-adapter.md`. At L0/L1 the adapter is **always unset** — do not imply a live inspection: either fire the install pitch (`/figma-setup`) or proceed from DESIGN.md / provided images and say which. `/creative`'s core exploration does not require Figma; never block direction work on a missing bridge.

## Always Load

- `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/core-principles.md` (L1 — always)
- `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/creative-direction.md` (L2 — creative domain)

## Sub-Agent Router

Read the user's request and route to one sub-agent. When the request spans multiple domains, offer to run them in sequence.

| Trigger | Sub-Agent |
|---------|-----------|
| "mood", "theme", "vibe", "direction", "references", "moodboard", "feel", "style", "aesthetic", named styles ("glassmorphism", "neubrutalism", "bento", ...) | Moodboard Generator |
| "palette", "color", "swatch", "hue", "dark mode", "color system" | Palette Architect |
| "type", "font", "typography", "scale", "font pairing", "type system" | Typography Director |
| "layout", "grid", "spacing", "composition", "density", "breakpoint" | Layout Strategist |
| "photography", "imagery", "art direction", "image style", "hero image", "illustration style" | Moodboard Generator (imagery mode — load `art-direction.md`) |
| "refresh", "modernize", "restyle", "update our look", "feels dated", "evolve the design" | Refresh Strategist |
| "brand", "rebrand", "identity", "logo system", "brand architecture", "sub-brand", "positioning" | Brand Architect |

If the request is unclear, ask: "Which aspect do you want to explore — mood/theme, color, typography, layout, imagery, a refresh of what exists, or brand-level direction?" Then route.

## Imagery in deliverables

Whenever a chosen direction implies photography, illustration, or generated imagery (hero art, moodboard tiles, campaign shots), offer the production path from `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/art-direction.md`: generate/edit via available image tooling (ask first, label AI-drafted), or deliver an image brief + SVG/CSS placeholder when no raster tooling is available. Never leave silent gray boxes; never present placeholder imagery as final.

---

## Sub-Agent: Moodboard Generator

**Load additionally:** `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/art-direction.md` when the exploration involves photography, illustration, or imagery direction; `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/brand-design.md` when the brief is brand-level (rebrand, identity). Otherwise none — `creative-direction.md` covers the moodboard method.

**Optional L3 query:** `Grep pattern="<emotion keyword>" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/psychological-principles.csv"` for emotional association backing; `Grep pattern="<style name or trait>" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/visual-styles.csv"` for named-style recipes and caveats.

### Ask first

Ask **at most 3** (the shared "ask 2–3" contract):

1. What product or project is this for? (one sentence)
2. What feeling do you want, and how far to push it? (2–4 adjectives + a dial — safe / balanced / bold; note density preference airy/balanced/packed if you have one)
3. Any brands, products, or design languages you admire as references? (optional)

### Workflow

1. Confirm or derive a **theme statement** using the `<adjective> + <adjective> + <noun>` template from `creative-direction.md`.
2. Query `style-contexts.csv` with the sector/audience keywords from the design read (`Grep pattern="<sector keyword>" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/style-contexts.csv"`) — the matching row names FIT/AVOID style families plus typography and palette direction. Then identify 5–7 reference touchpoints (existing design systems, art movements, industrial design objects, domains with analogous character). Do not use brand names as final answers — extract their underlying traits.
3. Extract 3–5 design traits per reference (e.g., "high contrast ratios", "generous whitespace", "mechanical precision").
4. Synthesize traits into 3 theme variants tuned to the creativity dial: safe, balanced, bold — drawn from *distinct* style families per the Style Library range rule (three intensities of one family is false variety). When the brief or dials suggest a recognizable style family, anchor that variant to it via a `visual-styles.csv` lookup — cite the concrete recipe and carry its when-to-avoid caveat; otherwise keep variants trait-based. Respect the context row's FIT/AVOID lists; name the constraint when it excludes a family.
5. Present as a table:

| Variant | Theme Statement | Key Traits | Best For |
|---------|----------------|------------|----------|
| Safe | ... | ... | ... |
| Balanced | ... | ... | ... |
| Bold | ... | ... | ... |

6. Ask the user to pick a variant or iterate. Offer to move to Palette Architect or Typography Director next.

### Output format

Theme table + next-step prompt. No narrative paragraphs. Keep the table scannable.

---

## Sub-Agent: Palette Architect

**Load additionally:** `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/color-theory.md`

**Optional L3 query:** `Grep pattern="color" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/psychological-principles.csv"` for color-psychology backing on key choices.

### Ask first

1. Do you have a base hue in mind, or should I derive it from the theme statement?
2. Does this need a dark mode variant?
3. Any existing brand colors to anchor (hex values)?

### Workflow

1. Establish the anchor hue (from user input or derived from theme statement adjectives via `creative-direction.md` translation rules).
2. Generate the **neutral scale** — 11 steps using OKLCH (preferred) or HSL fallback. Step lightness by ~8–9% increments. Name: `neutral-50` through `neutral-950`.
3. Generate the **brand/primary scale** — 9 steps. Name: `brand-100` through `brand-900`.
4. Define **semantic colors** — success, warning, error, info. Each gets a mid-range and a surface variant. For every interactive color, define the state derivations: hover, active, focus, and **disabled** (typically reduced chroma + adjusted lightness, never opacity-only on text).
5. Validate all foreground/background pairs against WCAG contrast ratios (4.5:1 text, 3:1 UI).
6. If dark mode requested: invert lightness mapping, preserve hue, adjust saturation for perceived balance.
7. Check for colorblind safety on the semantic palette (no red/green-only distinction).
8. Output as a table with hex + OKLCH values + WCAG pass/fail per pair.

### Output format

```
## Palette — <Theme Statement>

### Neutral Scale
| Token | Hex | OKLCH |
|-------|-----|-------|
...

### Brand Scale
...

### Semantic
| Role | Light | Dark | WCAG (text) |
...
```

Offer to hand off to Typography Director or token-naming via /ds-make.

---

## Sub-Agent: Typography Director

**Load additionally:** `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/typography.md`; `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/font-availability.md` (availability probes + marks)

**Optional L3 query:** `Grep pattern="readab" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/psychological-principles.csv"` for cognitive load references; `Grep pattern="<typography class or context hook>" -i path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/typography-styles.csv"` for ranked, sourced candidates per classification (used by the resolver).

### Ask first

1. What is the primary tone — editorial (expressive), product UI (functional), or technical (dense data)?
2. Is variable font support available, or should we target static weights only?
3. Any existing font already in use that must be respected?

### Workflow

1. Run the availability probes from `font-availability.md` (cache-first; Figma probe only for Figma deliverables). Derive the typography *class* from the theme/context (style-contexts.csv rows and archetypes name classes), then resolve class → concrete fonts via the **Classification Resolver** in `font-availability.md` (typography-styles.csv ranked candidates; first available wins; better-but-absent candidates ship `[needs-install]` with source + license AND a working installed substitute). Recommend the **font pair**: primary (display/headings) + secondary (body/UI), justified against the tone, with a fallback stack; every named font carries its availability mark.
2. Select a **modular scale ratio** from `typography.md` based on density dial: 1.125 (tight/product), 1.2 (balanced), 1.25 (editorial), 1.333 (expressive). Base: 16px.
3. Generate the **type scale** — 7 steps: `xs`, `sm`, `base`, `md`, `lg`, `xl`, `2xl`. Calculate size in px and rem. Map each to a semantic role (caption, body, label, heading-sm, heading-md, heading-lg, display).
4. Define **line height** per role: 1.4–1.6 for body, 1.1–1.3 for headings.
5. Define **letter spacing** per role: 0 for body, +0.5–1% for small labels, -0.5–1% for large display.
6. Flag any anti-patterns from `typography.md` triggered by the choices.
7. Output as a spec table.

### Output format

```
## Type System — <Theme Statement>

### Font Pair
Primary: <Font Name> [availability mark] — <Reason>
Secondary: <Font Name> [availability mark] — <Reason>
Fallback stack: ...

### Type Scale (ratio: X.XX, base: 16px)
| Token | Size (px) | Size (rem) | Role | Line Height | Letter Spacing |
...
```

Offer to feed into Layout Strategist or /ds-make Token Architect next.

---

## Sub-Agent: Layout Strategist

**Load additionally:** `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/layout.md`

**Optional L3 query:** `Grep pattern="navigation\|grid\|spacing" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/usability.csv"` for layout usability anchors.

### Ask first

1. What is the primary UI pattern — dashboard, content/reading, form-heavy, or marketing/landing?
2. Density preference (compact / default / comfortable)?
3. Mobile-first or desktop-first? Primary breakpoints needed?

### Workflow

1. Select the **grid system** from `layout.md` — 12-col for product UI (default), 8-col for dense data, fluid for marketing. Justify the choice.
2. Establish the **spacing base unit** (4px for dense UI, 8px standard) and generate the t-shirt scale: `xs`=4, `sm`=8, `md`=16, `lg`=24, `xl`=32, `2xl`=48, `3xl`=64.
3. Define **inset / stack / inline** spacing patterns with token references.
4. Define **breakpoints** — mobile-first unless otherwise specified: `sm`=480, `md`=768, `lg`=1024, `xl`=1280, `2xl`=1440.
5. Propose **density mode** parameterization — compact (0.75× base), default (1×), comfortable (1.25×).
6. Recommend the primary **composition pattern** matching the UI type (sidebar+main, card grid, list-detail, split-view, master-detail).
7. Flag anti-patterns from `layout.md` to avoid.

### Output format

```
## Layout System — <UI Type>

Grid: <type>, <columns>, <gutter>
Base unit: <value>px

### Spacing Scale
| Token | Value (px) | Use |
...

### Breakpoints
| Name | px | Notes |
...

### Density Modes
Compact: ...  Default: ...  Comfortable: ...

### Recommended Composition
<Pattern name> — <one-line rationale>
```

Offer to generate DESIGN.md via /map-design, or proceed to /ds-make for token scaffolding.

---

## Sub-Agent: Refresh Strategist

**Load additionally:** `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/visual-quality.md` (craft tells — what reads dated vs. crafted). At L2/L3 also load `.ds-context.md` per `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/ds-context-loader.md`.

**Optional L3 query:** `Grep pattern="<style name or trait>" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/visual-styles.csv"` — style recipes carry era markers and caveats useful for dating a language and picking its evolution target.

**Maturity behavior:** This sub-agent needs something to refresh. At L0, say so and hand off to Moodboard Generator (nothing exists yet — that's a first-direction task, not a refresh). At L1, the refresh lands as DESIGN.md updates. At L2/L3, every visual change must map to a token/component migration — propose the design moves here, route execution to /ds-make (never restyle ad hoc over a DS).

### Ask first

1. What triggered the refresh — dated look, brand shift, new audience, competitive pressure, or accumulated inconsistency? (the trigger defines success)
2. What must NOT change? (recognized assets, accessibility baselines, platform constraints)
3. How much appetite — polish, evolution, or overhaul?

### Workflow

1. **Inventory the current language.** From DESIGN.md / `.ds-context.md` / Figma (via the adapter — or state you're working from documentation if unset): palette, type, spacing, radius, depth style, motion character, imagery style.
2. **Diagnose, don't redesign yet.** Build a keep / evolve / retire table. For each trait, say *why*: dated marker (e.g. 2016-flat, heavy skeuomorphic gloss, AI-purple), craft failure (inconsistent radii, style-blind shadows), or still strong. Anchor era judgments in `visual-styles.csv` recipes; check "Craft & Anti-Slop Tells" for what reads cheap.
3. **Propose the refresh at three depths**, each with migration cost:
   | Depth | Scope | Typical cost |
   |-------|-------|--------------|
   | Polish | Token values only (colors, radii, shadows, type sizes) — no structural change | Low — token migration, no component API changes |
   | Evolution | Polish + component-level restyling, new depth/motion grammar, imagery redirection | Medium — versioned component updates, cascade republish |
   | Overhaul | New theme statement; palette, type, and layout system rebuilt | High — treat as a new direction: run Moodboard Generator first, then /ds-make |
4. **Recommend one depth** tied to the trigger from Ask-1 and the appetite from Ask-3. State dials + theme statement for the target language.
5. **Bridge to execution:** L1 → updated DESIGN.md sections; L2/L3 → ordered token/component migration list for /ds-make (respect the publish cascade); imagery changes → image briefs per `art-direction.md`.

### Output format

Keep/evolve/retire table + depth recommendation + migration bridge. Every "retire" needs a named reason — no taste-only retirements.

---

## Sub-Agent: Brand Architect

**Load additionally:** `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/brand-design.md` (two-layer brand knowledge: universal principles + named typologies) and `/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/knowledge/art-direction.md` (imagery is a brand asset). `creative-direction.md` (already loaded) provides the theme statement method.

**Optional L3 query:** `Grep pattern="<emotion or association>" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/psychological-principles.csv"` for association backing; `Grep pattern="story\|credib\|emotion" path="/root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/d9cd42a0-66ef-46d4-8a8a-db154f6e2212/skills/shared/data/design-principles.csv"` (SUCCES rows) for message-stickiness backing.

**Maturity behavior:** Brand direction is upstream of product execution at every level. At L2/L3, brand moves that touch tokens/components route to /ds-make; this sub-agent defines the brand layer and its translation contract, never edits the DS directly.

### Ask first

1. What is the brand situation — new brand, rebrand, or organizing multiple products/sub-brands?
2. Who must this brand win over, and what should they feel in three words?
3. Any fixed assets (name, logo, colors) that are non-negotiable?

### Workflow

1. **Layer 1 before Layer 2.** Check the brief against the universal principles in `brand-design.md` (distinctive assets, consistency, promise vs product truth, flexibility with governance, voice-visual alignment) — they outrank any named model. Then **name the philosophy** from its practice-philosophy table (identity/transformation/meaning/simplicity/point-of-view/belief-first). One line, stated up front.
2. **Resolve the architecture** (when multiple offerings exist): branded house (one master brand, descriptive products), house of brands (independent brands), or endorsed hybrid. Decide by audience overlap and reputational risk-sharing, and state the rule for naming the next product.
3. **Write the brand theme statement** (`<adjective> + <adjective> + <noun>`), then derive the association map: what the audience should feel, backed by psychological-principle queries where a claim needs evidence. Pick a primary archetype (max one secondary) from `brand-design.md` and query `style-contexts.csv` for the sector's FIT/AVOID families — the archetype gives the register, the context row grounds it in the market.
4. **Define the brand-to-product translation contract** — how brand assets become UI reality:
   | Brand asset | Product translation |
   |-------------|--------------------|
   | Brand color | Functional palette role (which scale step becomes `brand-600`; where brand color may NOT go — body text, error states) |
   | Brand type | UI type roles (display face for marketing surfaces; workhorse face for product UI; fallback stack) |
   | Logo | Clear-space and minimum-size rules as spacing tokens |
   | Voice/feeling | Motion character (productive vs. expressive registers) + imagery direction (lighting recipe + gaze/agency rules from `art-direction.md`) |
5. **Set the imagery direction**: pick the lighting register and composition rules from `art-direction.md`; write one master image brief as the reference standard.
6. **Hand off:** theme statement + dials → Moodboard Generator or Palette Architect for exploration; token-level changes → /ds-make; document the brand layer in DESIGN.md (L1) or flag for the DS documentation set (L2/L3).

### Output format

Philosophy line → architecture decision (if applicable) → theme statement + association map → translation contract table → master image brief → handoff list. Scannable; no brand-essay prose.


ARGUMENTS: Visual direction for Talent Q public site inside Direction D only (ink/paper/gold-is-Q, existing type). No new aesthetics, typefaces or colours. Need: hero idea for landing with Q sample conversation, pricing hypothesis treatment, trust page structure.

- 🔧 `Bash`: Inspect Glyph and evidence model exports

  <details><summary>result</summary>

```
// One evidence-strength vocabulary for hiring and careers (carried over from Direction D).
// Strength is carried by SHAPE, never by shade: the dataviz validator put adjacent gold steps ~9 ΔE apart.
export type GlyphKind = 'verified' | 'full' | 'partial' | 'practice' | 'none' | 'unclear';
/** One evidence-strength vocabulary for hiring and careers. Strength is carried by SHAPE, never by shade. */
export const GLYPH_LABEL: Record<GlyphKind, string> = { verified: 'Verified', full: 'Evidenced', partial: 'Partial or outdated', practice: 'Practising (private)', none: 'Not shown yet', unclear: 'Unclear' };
export function Glyph({ k, size = 20, title }: { k: GlyphKind; size?: number; title?: string }) {
  return (
    <svg width={size} height={size} viewBox="0 0 20 20" role={title ? 'img' : undefined} aria-label={title} aria-hidden={title ? undefined : true} style={{ flex: 'none' }}>
      {k === 'verified' && <><circle cx="10" cy="10" r="8.5" fill="none" stroke="currentColor" strokeWidth="1.5" /><circle cx="10" cy="10" r="5" fill="currentColor" /></>}
      {k === 'full' && <circle cx="10" cy="10" r="6.5" fill="currentColor" />}
      {k === 'partial' && <><circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" strokeWidth="1.5" /><path d="M10 4 A6 6 0 0 0 10 16 Z" fill="currentColor" /></>}
      {k === 'none' && <circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" strokeWidth="1.5" />}
      {k === 'unclear' && <circle cx="10" cy="10" r="6" fill="none" stroke=
… [1963 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read proof class vocab and ds classes

  <details><summary>result</summary>

```
if (e.kind === 'CLAIM') return 'CLAIM';
  if (e.verification === 'VERIFIED') return e.kind === 'CREDENTIAL' || e.kind === 'EMPLOYMENT' || e.kind === 'REFERENCE' ? 'ISSUER_VERIFIED' : 'ASSESSED';
  return 'SELF_REPORTED';
}
export const PROOF_WORD: Record<ProofClass, string> = { CLAIM: 'Claim', SELF_REPORTED: 'Self-reported', ASSESSED: 'Assessed', ISSUER_VERIFIED: 'Issuer-verified', DISPUTED: 'Disputed' };
export const PROOF_MEANS: Record<ProofClass, string> = {
  CLAIM: 'Said by the candidate (CV or conversation). Not evidence of the work, and not a sign it isn’t true.',
  SELF_REPORTED: 'Supplied by the candidate, not yet checked or reviewed by anyone else.',
  ASSESSED: 'Work a reviewer looked at, or an assessment with a recorded result. Shows the task, not guaranteed performance in the job.',
  ISSUER_VERIFIED: 'Confirmed by whoever issued it (a registry, an employer, a referee).',
  DISPUTED: 'Under review after a challenge. Left out of comparisons until it’s resolved.',
};

/** Supported = a requirement with checked or evidenced work behind it (not claims, not partial). */
const supported = (l: Level) => l === 'verified' || l === 'evidenced';

export type ProofShape = 'SHOWS_MORE_THAN_CV' | 'CLAIMS_AHEAD_OF_PROOF' | 'CV_AND_PROOF_AGREE' | 'LITTLE_EITHER_WAY' | 'NO_CV';
export const SHAPE_WORD: Record<ProofShape, string> = {
  SHOWS_MORE_THAN_CV: 'Shows more than the CV says',
  CLAIMS_AHEAD_OF_PROOF: 'Strong claims, limited supporting evidence',
  CV_AND_PROOF_AGREE: 'CV
… [6142 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect area slice, emit, QMark, skill types

  <details><summary>result</summary>

```
Each file here is owned by one feature area and exports:

    export const area = { id: 'agency', init: (): AgencyState => ({ ... }) };
    export const agency = (w: World) => w.areas.agency as AgencyState;   // typed accessor

The slice lives in the one store (World v4), so it persists, syncs across tabs and resets with the demo.
// Candidate-authorised video and voice evidence (audit addendum §F). Only media the candidate explicitly selects
// is processed. Transcription happens once per content hash; reviews are cached by contentHash + rubric version
// (scoped to the parts the organisation was shown, so a review never rests on a part it can't see).
import type { World } from '../../mock/world';
import type { MediaEvidence, MediaReview } from '../domain';

export interface MediaState {
  items: MediaEvidence[]; reviews: MediaReview[];
  briefings: Record<string, { jobId: string; duration: number; chapters: { t: number; label: string }[]; transcript: { t: number; text: string }[] }>;
  // ---- MEDIA area additions (all optional so stored worlds from before stay valid) ----
  /** Transcripts by content hash: transcribed once, reused for any later copy of the same file. */
  transcripts?: Record<string, { at: string; lines: number }>;
  /** Why a link was refused or a fetch failed, per media item (shown to the candidate in plain words). */
  notes?: Record<string, { kind: 'UNSAFE_LINK' | 'FETCH_FAILED' | 'PAUSED'; text: string }>;
  /** Media items each recruiter has opened (
… [3893 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Q types and skill example

  <details><summary>result</summary>

```
// Contracts for Q's brain in the prototype. Skills are small, testable units that understand one kind
// of request and act on the one store. They never hold closures in the conversation: replies carry
// serialisable actions (QAction), so a conversation survives navigation, reloads and other tabs.
import type { Actor, QFrame, QMsg, Side } from '../../state/domain';
import type { World } from '../../mock/world';
import type { Entities } from './nlu';

export interface QCtx {
  w: World;
  actor: Actor;
  /** Current route, e.g. '/r/people/p_tobi'. */
  route: string;
  text: string;
  /** Lowercased, typo-corrected, contraction-expanded text. */
  norm: string;
  ents: Entities;
  frame: QFrame | null;
  /** The last thing Q said to this person (for "yes", "that one", "change it"). */
  lastQ: QMsg | null;
}

export type ReplyMsg = Omit<QMsg, 'id' | 'at' | 'who' | 'engine'> & { who?: 'q' | 'system' };

export interface QReply {
  msgs: ReplyMsg[];
  /** Mutations applied in the same store update as the reply (atomic). */
  effects?: (w: World, actor: Actor) => void;
  /** Navigate after replying. Label is used for "go back" and the nav history. */
  nav?: { to: string; label: string };
  /** undefined: keep the current frame; null: clear it; QFrame: replace it. */
  frame?: QFrame | null;
}

export interface Skill {

export interface ProactiveRule {
  id: string;
  side: Side | 'both';
  /** Higher priority suggestions still show when proactive help is set to "quiet". */
  p
… [3992 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List cast actors and QMsg shape

  <details><summary>result</summary>

```
{ id: 'p_seyio', name: 'Seyi Okoro', first: 'Seyi', initials: 'SO', side: 'candidate', title: 'Senior backend engineer', timezone: 'Africa/Lagos', personId: 'p_seyio', journey: 'J12', email: 'seyi.oko
175:export interface QMsg {
176-  id: string; who: 'me' | 'q' | 'system'; text: string; at: string; route?: string;
177-  used?: string[]; why?: string; actions?: QAction[];
178-  kind?: 'reply' | 'question' | 'suggestion' | 'refusal' | 'approval' | 'notice' | 'plan' | 'undo';
179-  /** Live-bound content rendered from state (e.g. a plan's agents or a draft). */
180-  ref?: { type: string; id: string };
181-  /** Which engine produced this reply: honest labelling of simulation. */
182-  engine?: 'rules' | 'gateway' | 'system';
183-}
184-export interface QFrame { intent: string; slots: Record<string, string>; awaiting?: string; startedAt: string; topic?: string }
185-export interface Suggestion { id: string; actor: string; rule: string; subject: string; text: string; why: string; actions: QAction[]; at: string; state: 'OPEN' | 'DISMISSED' | 'SNOOZED' | 'DONE'; until?: string }
25:  { id: 'org_kora', name: 'Kora Pay', kind: 'EMPLOYER', industry: 'Payments', size: '120 people', city: 'Lagos', verified: { domain: true, registry: 'VERIFIED' }, delegation: 'APPROVE_EACH_SEND', setup: { done: true, step: 5 },
28:  { id: 'org_tb', name: 'Talentbridge', kind: 'AGENCY', industry: 'Recruitment agency', size: '9 people', city: 'Lagos', verified: { domain: true, registry: 'VERIFIED' }, deleg
… [97 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find Kunle and Ifeoma in seeds

  <details><summary>result</summary>

```
4:// and Kunle Bakare's conflicting sources (CV says 6 years of Go, public GitHub suggests about 2).
50:  // Kunle: two sources that disagree. Both shared with Kora; neither is silently preferred.
51:  ev({ evidenceId: 'e_ha_kunle_cv', ownerId: 'p_kunle', kind: 'CLAIM', title: 'CV: 6 years building Go services (2020 to now)', source: 'CV uploaded by Kunle', observedAt: '2026-10-20', shows: 'Say
74:// Seyi referred Ifeoma for Payouts too, so one person relates to two roles in the Q4 campaign (cross-role board, AD-D-06).
9:    // Kunle: an impressive CV with weak evidence behind it.
```
  </details>

- 🔧 `Bash`: Check qmark var, PageIndex, Switch, form classes

  <details><summary>result</summary>

```
ds/ds.css:201:.ds { --qmark: var(--gold); }
ds/ds.css:202:.ds .ink, .ds-thread, .ds-rail, .ds-strip, .ds-sheetbar, .ds-tabs, .ds-more { --qmark: var(--gold-light); }
styles/talent-c.css:17:.talent-c-state-icon { display: grid; place-items: center; width: 32px; height: 32px; border-radius: 50%; background: var(--wash); color: var(--ink-2); --qmark: var(--gold); }
styles/talent-c.css:51:.talent-c-mic[aria-pressed='true'] { background: var(--ink); color: var(--paper); --qmark: var(--gold-light); }
// In-page index for long pages (audit addendum §B, AD-B-03). On phones it sticks under the header as one row of
// section links that scrolls sideways inside itself and marks the section in view; on desktop it stays a quiet
// link row. Sections are ordinary elements with ids, so it works with any page.
import { useEffect, useState } from 'react';

export function PageIndex({ items, label = 'On this page' }: { items: { id: string; label: string }[]; label?: string }) {
  const [cur, setCur] = useState(items[0]?.id);
  useEffect(() => {
    const els = items.map((i) => document.getElementById(i.id)).filter((x): x is HTMLElement => !!x);
    if (!els.length || typeof IntersectionObserver === 'undefined') return;
    const io = new IntersectionObserver((es) => { const v = es.filter((e) => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0]; if (v) setCur(v.target.id); }, { rootMargin: '-15% 0px -70% 0px' });
    els.forEach((e) => io.observe(e)); retu
… [2424 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/state/areas/public.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/state/areas/public.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/sampleQ.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/sampleQ.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Remove ambiguous regex alternative

  <details><summary>result</summary>

```
57:  if (/\b(decid\w*|reject\w*|who hires|automat\w*|auto[- ]?reject|in charge|final say)\b/.test(t))
[This command modified 1 file you've previously read: journeys/public/sampleQ.ts. Call Read before editing.]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/content.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/content.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/SampleQ.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/SampleQ.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Site.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Site.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Use static import for ask

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Landing.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Landing.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/How.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/How.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Employers.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Employers.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Talent.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Talent.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Pricing.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Pricing.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Drop event emit from interest form

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-30 12:35

Now the Trust page.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Trust.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Trust.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/Ask.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/Ask.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/SignIn.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/SignIn.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Write routes file and inspect engine exports

  <details><summary>result</summary>

```
15:export const registerSkill = (s: Skill) => { if (!skills.some((x) => x.id === s.id)) skills.push(s); };
16:export const allSkills = () => skills;
20:export const registerOp = (name: string, fn: OpFn) => { ops.set(name, fn); };
24:export function appendQ(w: World, actorId: string, m: Omit<QMsg, 'id' | 'at'>) {
27:export const useQThread = () => useWorld((w) => w.q.threads[w.session.actor] ?? EMPTY);
33:export const onThinking = (f: () => void) => { thinkSubs.add(f); return () => { thinkSubs.delete(f); }; };
34:export const isThinking = () => thinking;
111:export const gatewayConfigured = () => !!GATEWAY;
140:export const useRunAction = () => useCallback((a: QAction) => { void runAction(a); }, []);
143:export function pushUndo(w: World, actorId: string, label: string, op: string, args: Record<string, unknown>) {
158:export function qNavigate(to: string, label: string) {
171:export function qBack(): { to: string; label: string } | null {
182:export function labelFor(path: string) {
194:export function useViewState<T>(key: string, initial: T): [T, (v: T) => void] {
202:export function qSays(text: string, extra: Partial<Omit<QMsg, 'id' | 'at' | 'who' | 'text'>> = {}) {
```
  </details>


**Claude** · 2026-10-30 12:36

Now the small Q skill for signed-in people asking about Talent Q's own pricing/trust.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/skills/public.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/skills/public.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/public/public.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/public/public.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Add entry links and typecheck

  <details><summary>result</summary>

```
talent-q-design/prototype/src/ds/QMark.tsx      | 9 +++++----
 talent-q-design/prototype/src/routes/entry.tsx  | 2 +-
 talent-q-design/prototype/src/screens/Entry.tsx | 1 +
 3 files changed, 7 insertions(+), 5 deletions(-)
src/journeys/assess/model.ts(71,22): error TS6133: 'w' is declared but its value is never read.
src/journeys/hire-d/model.ts(141,49): error TS6133: 'mid' is declared but its value is never read.
src/journeys/public/SampleQ.tsx(115,16): error TS2367: This comparison appears to be unintentional because the types '"ready"' and '"thinking"' have no overlap.
src/journeys/public/SampleQ.tsx(115,52): error TS2367: This comparison appears to be unintentional because the types '"ready"' and '"offline"' have no overlap.
src/journeys/public/SampleQ.tsx(119,45): error TS2367: This comparison appears to be unintentional because the types '"ready"' and '"thinking"' have no overlap.
src/journeys/public/SampleQ.tsx(119,85): error TS2367: This comparison appears to be unintentional because the types '"ready"' and '"offline"' have no overlap.
src/journeys/public/SampleQ.tsx(126,10): error TS2367: This comparison appears to be unintentional because the types '"ready"' and '"thinking"' have no overlap.
src/journeys/public/SampleQ.tsx(127,10): error TS2367: This comparison appears to be unintentional because the types '"ready"' and '"offline"' have no overlap.
src/journeys/public/SampleQ.tsx(136,200): error TS2367: This comparison appears to be unintentional because the types '
… [570 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Rename engine file and fix types

  <details><summary>result</summary>

```
[This command modified 10 files you've previously read: journeys/public/Trust.tsx, journeys/public/Ask.tsx, journeys/public/Employers.tsx, journeys/public/How.tsx, journeys/public/Landing.tsx and 5 more. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Start vite dev server on port 5211

  <details><summary>result</summary>

```
200
```
  </details>

- 🔧 `Bash`: Capture all public pages desktop and phone

  <details><summary>result</summary>

```
Exit code 1
file:///tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap.mjs:11
    const sw = await p.evaluate(() => document.documentElement.scrollWidth); if (sw > innerWidth) errs.push(`${vn} ${n} sideways ${sw}`);
                                                                                      ^

ReferenceError: innerWidth is not defined
    at file:///tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap.mjs:11:87

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Fix and rerun capture

  <details><summary>result</summary>

```
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
```
  </details>

- 🔧 `Bash`: Check vite log for 500

  <details><summary>result</summary>

```
at TransformPluginContext._formatError (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:49258:41)
      at TransformPluginContext.error (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:49253:16)
      at normalizeUrl (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:64307:23)
      at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
      at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:64439:39
      at async Promise.all (index 17)
      at async TransformPluginContext.transform (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:64366:7)
      at async PluginContainer.transform (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:49099:18)
      at async loadAndTransform (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:51978:27)
      at async viteTransformMiddleware (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:62106:24)
12:39:59 PM [vite] Internal server error: Failed to resolve import "./q-tools.css" from "src/journeys/q-tools/refs.tsx". Does the file exist?
  Plugin: vite:import-analysis
  File: /home/user/neo/talent-q-design/prototype/src/
… [1843 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check q-tools dir progress

  <details><summary>result</summary>

```
model.ts
pages.tsx
refs.tsx
views.tsx
web.ts
0
```
  </details>

- 🔧 `Bash`: Look at another feature script header

  <details><summary>result</summary>

```
// Connected email and Q-managed correspondence (addendum E-01, E01-01..30) and J11 steps 3, 6, 10, 11 and 12.
// Usage: BASE=http://localhost:5191 node qa/scripts/features/email.mjs
import { createRequire } from 'node:module';
import { mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node-tools/node_modules/playwright/index.js');
const BASE = (process.env.BASE || 'http://localhost:5191').replace(/\/$/, '');
const OUT = resolve(dirname(fileURLToPath(import.meta.url)), '../../../captures/cx/email'); mkdirSync(OUT, { recursive: true });
const results = []; const errors = [];
const step = (name, ok, info = '') => { results.push({ name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${info ? ` — ${String(info).replace(/\s+/g, ' ').slice(0, 220)}` : ''}`); };
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let nav = 0;
async function fresh(page) { await page.goto(`${BASE}/#/r/home`); await page.evaluate(() => localStorage.clear()); await page.reload(); await page.waitForSelector('.ds-app'); await sleep(300); }
async function asActor(page, id, route) {
  await page.evaluate((id) => { const w = JSON.parse(localStorage.getItem('tq.world.v4')); w.session.actor = id; localStorage.setItem('tq.world.v4', JSON.stringify(w)); }, id);
  await page.goto(`${BASE}/?n=${++nav}#${route}`); await page.waitForSelector('.ds-app'); awa
… [1938 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/qa/scripts/features/public.mjs

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/qa/scripts/features/public.mjs (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check if q-tools CSS exists now

  <details><summary>result</summary>

```
model.ts
pages.tsx
refs.tsx
views.tsx
web.ts
500
```
  </details>

- 🔧 `Bash`: Create isolated snapshot and serve on 5211

  <details><summary>result</summary>

```
Exit code 144
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/../sync.sh: line 5: rsync: command not found
ln: failed to create symbolic link '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype/node_modules': No such file or directory
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/../sync.sh: line 9: cd: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype/src: No such file or directory
```
  </details>

- 🔧 `Bash`: Snapshot via tar and serve on 5211

  <details><summary>result</summary>

```
Exit code 144
stub ./journeys/q-tools/q-tools.css
stub ./journeys/org-admin/org-admin.css
```
  </details>

- 🔧 `Bash`: Check whether port 5211 is in use

  <details><summary>result</summary>

```
free
```
  </details>

- 🔧 `Bash`: Serve snapshot on port 5211 in background
- 🔧 `Bash`: Capture all pages from snapshot

  <details><summary>result</summary>

```
Command running in background with ID: b5kk1r0ns. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b5kk1r0ns.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>


  <details><summary>result</summary>

```
000
000
000
000
000
000
000
000
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
```
  </details>

- 🔧 `Bash`: Allow node_modules realpath in snapshot config

  <details><summary>result</summary>

```
stub ./journeys/q-tools/q-tools.css
stub ./journeys/org-admin/org-admin.css
  server: { fs: { allow: ['..', '/home/user/neo'] } },
```
  </details>

- 🔧 `Bash`: Recapture after config change

  <details><summary>result</summary>

```
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
      at async PluginContainer.transform (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:49099:18)
      at async loadAndTransform (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:51978:27)
      at async viteTransformMiddleware (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:62106:24)
```
  </details>

- 🔧 `Bash`: Find the 500 cause

  <details><summary>result</summary>

```
Error: The following dependencies are imported but could not be resolved:
12:42:57 PM [vite] Pre-transform error: Failed to resolve import "../journeys/hire-d/hire-d.css" from "src/routes/hire-d.tsx". Does the file exist?
12:43:01 PM [vite] Internal server error: Failed to resolve import "../journeys/hire-d/hire-d.css" from "src/routes/hire-d.tsx". Does the file exist?
12:43:09 PM [vite] Internal server error: Failed to resolve import "../journeys/hire-d/hire-d.css" from "src/routes/hire-d.tsx". Does the file exist?
```
  </details>

- 🔧 `Bash`: Generalise CSS stubbing in snapshot

  <details><summary>result</summary>

```
stub /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype/src/journeys/q-tools/q-tools.css
```
  </details>

- 🔧 `Bash`: Recapture pages

  <details><summary>result</summary>

```
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
Failed to load resource: the server responded with a status of 500 (Internal Server Error)
18
```
  </details>

- 🔧 `Bash`: Check remaining 500s

  <details><summary>result</summary>

```
12:43:37 PM [vite] Pre-transform error: Failed to resolve import "../journeys/talent-d/refs" from "src/routes/talent-d.tsx". Does the file exist?
12:43:44 PM [vite] Internal server error: Failed to resolve import "../journeys/talent-d/refs" from "src/routes/talent-d.tsx". Does the file exist?
12:43:52 PM [vite] Internal server error: Failed to resolve import "../journeys/talent-d/refs" from "src/routes/talent-d.tsx". Does the file exist?
```
  </details>

- 🔧 `Bash`: Drop unresolved in-progress files in snapshot

  <details><summary>result</summary>

```
stub /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype/src/journeys/q-tools/q-tools.css
```
  </details>

- 🔧 `Bash`: Recapture pages

  <details><summary>result</summary>

```
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
```
  </details>

- 🔧 `Bash`: Debug 403

  <details><summary>result</summary>

```
server: { fs: { allow: ['..', '/home/user/neo'] } },
            ims=re.findall(r"from ['\"](\.{1,2}/[^'\"]+)['\"]", open(fp).read())
            bad=[m for m in ims if not ok(dd,m)]
            if bad: os.remove(fp); print('dropped',d+'/'+f,bad); changed=True
PY
sed -i "s#allow: \['..'\]#allow: ['..', '/home/user/neo']#" $S/prototype/vite.config.ts
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2" is outside of Vite serving allow list.
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff" is outside of Vite serving allow list.
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff" is outside of Vite serving allow list.
```
  </details>

- 🔧 `Bash`: Retry capture

  <details><summary>result</summary>

```
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2" is outside of Vite serving allow list.
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2" is outside of Vite serving allow list.
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff" is outside of Vite serving allow list.
The request url "/home/user/neo/talent-q-design/prototype/node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff" is outside of Vite serving allow list.
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (Forbidden)
Failed to load resource: the server responded with a status of 403 (For
… [165 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Stop the snapshot server by port

  <details><summary>result</summary>

```
Exit code 2
/bin/bash: line 1: ss: command not found

kill: usage: kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]
```
  </details>

- 🔧 `TaskStop`: {"task_id": "b5kk1r0ns"}

  <details><summary>result</summary>

```
{"message":"Successfully stopped task: b5kk1r0ns (cd /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype && npx vite --port 5211 --strictPort > ../vite.log 2>&1)","task_id":"b5kk1r0ns","task_type":"local_bash","command":"cd /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype && npx vite --port 5211 --strictPort > ../vite.log 2>&1"}
```
  </details>

- 🔧 `Bash`: Check remaining vite processes

  <details><summary>result</summary>

```
000
4
12659 --strictPort 5200 --port
14018 --strictPort 4190 --port
21636 127.0.0.1 --host --strictPort
21986 127.0.0.1 --host --strictPort
```
  </details>

- 🔧 `Bash`: Restart snapshot server on 5211

  <details><summary>result</summary>

```
Command running in background with ID: bocf6ybol. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bocf6ybol.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Capture pages after restart

  <details><summary>result</summary>

```
no errors
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/d-landing.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:46

[Image: original 1440x2679, displayed at 1075x2000. Multiply coordinates by 1.34 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/m-landing.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:46

[Image: original 780x8228, displayed at 190x2000. Multiply coordinates by 4.11 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/d-pricing.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:46

[Image: original 1440x2631, displayed at 1095x2000. Multiply coordinates by 1.32 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/d-how.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:46

[Image: original 1440x2425, displayed at 1188x2000. Multiply coordinates by 1.21 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/d-employers.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:46

[Image: original 1440x2309, displayed at 1247x2000. Multiply coordinates by 1.15 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/m-signin.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:46

[Image: original 780x2848, displayed at 548x2000. Multiply coordinates by 1.42 to map to original image.]

- 🔧 `Skill`: {"skill": "design-skills:design-critique", "args": "Rendered critique of Talent Q public pages (landing, how, employers, talent, pricing, trust, ask, sign-in) desktop 1440 and phone 390."}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-critique
```
  </details>


**User** · 2026-10-30 12:46

Base directory for this skill: /root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/64191f50-3277-408e-9eca-3ef47f62a254/skills/design-critique

# Design Critique & Evaluation

You are an expert in evaluating digital product designs. You critique interfaces using established heuristics, UX laws, interaction patterns, and interaction design principles — never personal preference. Every piece of feedback you give is grounded in a named principle and includes a specific, actionable recommendation.

Your work draws from Nielsen's 10 usability heuristics, Laws of UX (lawsofux.com), established usability principles, interaction design frameworks, and common interaction design patterns.

## Core Principle

Design critique is not about taste — it's about effectiveness. The question is never "Do I like this?" but always "Does this work for the user trying to accomplish their goal?" Ground every observation in evidence, principles, or research. When you don't know, say "test this" rather than guessing.

---

## The Critique Framework

Use this structured approach for any design review.

### Step 1: Understand Context Before Judging

Before critiquing, answer:
- **Who** is the user? (Persona, experience level, context)
- **What** are they trying to accomplish? (Primary task, goal)
- **Where** in the journey is this screen? (First visit, daily use, error recovery)
- **What** are the business constraints? (Technical limits, brand requirements, timeline)

A design that's wrong for power users may be perfect for first-time users. Context determines quality.

### Step 2: First Impression Scan (5 seconds)

Look at the design for 5 seconds, then look away. Ask:
- What is this page/screen about?
- What is the primary action I should take?
- Where would I click first?
- Does anything confuse me?

This simulates real user behavior — people scan, they don't read. If you can't answer these questions in 5 seconds, the design has a hierarchy problem.

### Step 3: Heuristic Pass

Evaluate against Nielsen's 10 heuristics. For each violation, note the heuristic, severity, and a specific fix.

### Step 4: UX Law Check

Scan for violations of key UX laws. Ask the questions in the UX Laws Quick Reference below.

### Step 5: Interaction Design Review

Evaluate product posture (is it matched to usage patterns?), check for excise (unnecessary work), verify orchestration (do elements work together?), and assess the design for perpetual intermediates.

### Step 6: Pattern Review

Check whether interaction patterns match established conventions. Unconventional patterns need strong justification. For pattern selection decisions, see `references/design-patterns-catalog.md`.

### Step 7: Information Architecture Review

Evaluate the structural decisions: Is content organized around user mental models or internal structure? Are labels specific and consistent? Can users orient, navigate, and search effectively? See the Information Architecture Evaluation section below.

### Step 8: Content & Writing Review

Evaluate interface text through usable/useful/responsible lenses. Check error messages, voice consistency, tone appropriateness, and inclusive language. See the Content & UX Writing Evaluation section below.

### Step 9: Synthesize and Prioritize

Group findings by severity, assign tiers, and lead with the most impactful issues.

---

## Nielsen's 10 Usability Heuristics

The foundation of heuristic evaluation. Use these as your primary lens.

| # | Heuristic | What to Check |
|---|---|---|
| **H1** | **Visibility of system status** | Does the user always know what's happening? Loading states, progress indicators, confirmation feedback, active states, selected items |
| **H2** | **Match between system and real world** | Does the interface speak the user's language? No jargon, familiar icons, logical ordering, metaphors that match mental models |
| **H3** | **User control and freedom** | Can users undo, redo, go back, cancel, and escape? Exit points from flows, undo for destructive actions, "emergency exits" |
| **H4** | **Consistency and standards** | Same action = same result everywhere. Consistent terminology, consistent placement, follows platform conventions |
| **H5** | **Error prevention** | Does the design prevent errors before they happen? Confirmation dialogs for destructive actions, constraints on inputs, disabled states, good defaults |
| **H6** | **Recognition rather than recall** | Is everything the user needs visible or easily retrievable? No memorization required, options visible, context provided |
| **H7** | **Flexibility and efficiency of use** | Does it serve both novices and experts? Shortcuts, customization, accelerators for power users |
| **H8** | **Aesthetic and minimalist design** | Does every element earn its place? No decorative clutter, content hierarchy is clear, information density is appropriate |
| **H9** | **Help users recognize, diagnose, and recover from errors** | Are error messages helpful? Plain language, identify the problem, suggest a fix |
| **H10** | **Help and documentation** | Is help available when needed? Contextual, searchable, task-oriented, not a wall of text |

### Severity Scale for Heuristic Violations

| Severity | Definition | Action |
|---|---|---|
| **0** | Not a usability problem | No action |
| **1** | Cosmetic only | Fix if time permits |
| **2** | Minor | Low priority fix |
| **3** | Major | High priority — causes significant difficulty |
| **4** | Catastrophe | Must fix before release — prevents task completion |

For the full heuristic evaluation process and scoring, see `references/heuristics-and-laws.md`.

---

## UX Laws Quick Reference

Organized by the design question they answer.

### Layout and Visual Design

| Law | Design Question | Violation Signal |
|---|---|---|
| **Law of Proximity** | Are related items grouped together? | Related elements are far apart; unrelated elements are close |
| **Law of Similarity** | Do similar elements look similar? | Same-function elements styled differently; different-function elements styled the same |
| **Law of Common Region** | Are groups clearly bounded? | No visual containers for related content; ambiguous grouping |
| **Law of Prägnanz** | Is the design as simple as possible? | Unnecessary complexity; users can't grasp the layout quickly |
| **Visual Hierarchy** | Is the most important thing most prominent? | Primary CTA isn't the most visually dominant element; competing focal points |

### Decision Making and Choices

| Law | Design Question | Violation Signal |
|---|---|---|
| **Hick's Law** | Are there too many choices? | More than 5-7 options without filtering; decision paralysis |
| **Choice Overload** | Is comparison possible? | Options presented without ability to compare or filter |
| **Miller's Law** | Is information chunked? | Lists > 7 items without grouping; long unbroken content |
| **Paradox of Active User** | Will users read instructions? | Design depends on users reading docs before using |

### Interaction and Input

| Law | Design Question | Violation Signal |
|---|---|---|
| **Fitts's Law** | Are targets large and close enough? | Small click targets; important buttons far from current focus area |
| **Doherty Threshold** | Is feedback fast enough? | Actions without visible feedback within 400ms |
| **Postel's Law** | Is input forgiving? | Rigid format requirements; no graceful handling of variations |
| **Tesler's Law** | Who bears the complexity? | Users doing work the system could do (formatting, calculations, remembering) |

### Memory and Attention

| Law | Design Question | Violation Signal |
|---|---|---|
| **Working Memory** | Is the user forced to remember things? | Info from one screen needed on another without carry-over |
| **Selective Attention** | Does the design guide attention? | Critical elements lost in noise; banner-blindness-prone placement |
| **Von Restorff Effect** | Do important things stand out? | Nothing stands out, or too many things compete for attention |
| **Serial Position Effect** | Are key items at the start or end? | Important options buried in the middle of a list |

### Motivation and Progress

| Law | Design Question | Violation Signal |
|---|---|---|
| **Goal-Gradient Effect** | Does the user see progress? | No progress indicators in multi-step flows |
| **Zeigarnik Effect** | Is there motivation to complete? | No indication of how much is done vs. remaining |
| **Peak-End Rule** | Is the ending designed well? | Weak confirmation, no celebration, abrupt endings |

### Familiarity and Learning

| Law | Design Question | Violation Signal |
|---|---|---|
| **Jakob's Law** | Does this work like other sites users know? | Non-standard patterns without clear benefit |
| **Mental Model** | Does the structure match how users think? | Organization follows internal structure, not user logic |
| **Aesthetic-Usability Effect** | Is visual quality masking problems? | Beautiful design that tests poorly; polished but confusing |

---

## Interaction Design Principles

Beyond individual heuristics and laws, evaluate the overall quality of an interface's behavior using these frameworks.

### Product Posture Analysis

Every product has a behavioral stance. Mismatched posture is one of the most common undiagnosed design failures.

| Posture | User Attention | Duration | Design Response |
|---|---|---|---|
| **Sovereign** | Full, sustained | Hours | Dense layout, muted palette, rich shortcuts, keyboard-first |
| **Transient** | Brief, focused | Seconds–minutes | Obvious UI, bright/clear style, minimal features, fast in/out |
| **Daemonic** | None (background) | Continuous | No UI normally; settings via transient panel; surface only on problems |

**Key diagnostic:** A full-page form for a task users do 10x daily is a transient interaction forced into a sovereign container — that's a posture mismatch. Fix: inline or overlay creation.

### Perpetual Intermediate Design

~80% of users are perpetual intermediates. They're past beginner but never become experts. Design for them.

| Audience | % | Design Strategy |
|---|---|---|
| **Beginners** | ~10% | Quick path to intermediacy. Multiple command modalities (menu → toolbar → shortcut). Don't dumb down the interface. |
| **Intermediates** | ~80% | Optimize their working set. Frequent features in toolbars. Progressive disclosure for the rest. Sticky preferences. |
| **Experts** | ~10% | Don't block them. Keyboard shortcuts, customization, no unnecessary confirmations. |

**Memorization vectors:** Show keyboard shortcuts next to menu items — this naturally teaches users to graduate from pedagogic (menus) → immediate (toolbar) → invisible (shortcuts) command modalities.

### Excise Audit

Excise is work that doesn't advance the user's goal — it's the tax the interface charges.

| Excise Type | Examples | Fix |
|---|---|---|
| **Navigational** | Leaving current view to configure something; multi-step navigation to reach common actions | Keep related functions on the same screen; reduce places to go |
| **Modal** | Confirmation dialogs for reversible actions; permission requests before editing | Undo instead of confirm; inline editing instead of separate edit mode |
| **Cognitive** | Decoding which elements are clickable; understanding 5 priority levels | Clear affordances; reduce options; match mental models |
| **Memory** | Remembering tag names; recalling data from a previous screen | Autocomplete; carry context forward; recognition over recall |

**Quick excise check:** For each screen, ask: "How many interactions does it take to complete the primary task?" Then ask: "How many of those directly advance the goal?" The gap is excise.

### Orchestration Checklist

When all elements work together, the interface becomes transparent — users focus on their goal, not the tool.

- [ ] Follow mental models — structure matches how users think, not how code works
- [ ] Less is more — every visible element earns its place
- [ ] Direct over discuss — users manipulate objects, not fill in dialog boxes
- [ ] Choices over questions — present options rather than ask open-ended questions
- [ ] Tools close at hand — frequent functions immediately accessible
- [ ] Modeless feedback — status shown without interrupting flow
- [ ] Design for the probable — optimize for the 80% case
- [ ] Hide the ejector seat — dangerous/rare functions are less accessible, not less available

### Responsiveness Thresholds

| Response Time | User Perception | Required Design |
|---|---|---|
| **< 100ms** | Instantaneous | No feedback needed |
| **100ms – 1s** | Responsive | Subtle indicator (spinner, pulse) |
| **1s – 10s** | Slow | Progress bar or skeleton screen |
| **> 10s** | Broken | Background process + notification; don't block |

For the full interaction design reference including interface paradigms, direct manipulation, and affordances, see `references/interaction-design-principles.md`.

---

## Giving Actionable Feedback

### The Feedback Formula

Every critique point should follow this structure:

> **[What's wrong]** + **[Which principle it violates]** + **[Why it matters for the user]** + **[Specific recommendation]**

**Bad feedback:**
"I don't like the navigation."

**Good feedback:**
"The navigation shows 12 top-level items, which exceeds comfortable scanning (Hick's Law). Users will struggle to find what they need quickly. **Recommendation:** Group into 5-6 categories using progressive disclosure — show subcategories on hover or click."

### What to Say vs. What Not to Say

| Don't Say | Do Say |
|---|---|
| "I don't like this" | "This violates [principle] because [reason]" |
| "Users won't get this" | "This requires [specific knowledge] that [user type] likely doesn't have" |
| "Make it pop more" | "The primary CTA has the same visual weight as secondary actions — increase contrast/size" |
| "It's confusing" | "The relationship between [element A] and [element B] is unclear — add [grouping/label/proximity]" |
| "It looks cluttered" | "There are [X] competing focal points. Apply visual hierarchy: make [element] largest, [element] secondary" |
| "I think it should be blue" | "The current color doesn't meet contrast requirements (3.2:1 vs. 4.5:1 needed)" |

### Calibrating Feedback to Fidelity

| Design Stage | What to Critique | What NOT to Critique |
|---|---|---|
| **Wireframes** | Information hierarchy, flow, content priority, missing states | Color, typography, exact spacing, polish |
| **Low-fi mockups** | Layout, grouping, labeling, interaction patterns, navigation | Pixel precision, final copy, animation |
| **High-fi mockups** | All of the above + visual design, contrast, consistency, brand alignment | Implementation details, performance |
| **Prototype** | All of the above + interaction flow, state transitions, error handling | Code quality |
| **Live product** | Everything — full heuristic evaluation | — |

---

## The "Krug Test" — Five Usability Checks

Apply these to every screen:

### 1. Scanning: Can users find what they need?

People don't read — they scan. Check:
- Is there a clear visual hierarchy? (Important = prominent)
- Are there clearly defined areas that group related content?
- Is it obvious what's clickable vs. what's not?
- Is there minimal noise? (No unnecessary elements competing for attention)

### 2. Satisficing: Will users pick the right thing?

Users don't optimize — they satisfice (pick the first reasonable option). Check:
- Is the primary action the most prominent element?
- Are labels clear enough that users don't have to guess?
- Are there false bottoms (content below the fold users won't scroll to)?

### 3. Self-Evident: Does it work without thinking?

If users have to think, the design is failing. Check:
- Can you explain what this page is and what to do in 5 seconds?
- Are buttons and links labeled with what they do, not clever names?
- Is it clear where you are, how you got here, and what to do next?

### 4. Navigation: Do users know where they are?

No sense of scale, direction, or location on the web. Check:
- Is there a clear "you are here" indicator?
- Do breadcrumbs or navigation show the current location?
- Is there always a way home?
- Do page names match what was clicked?

### 5. Goodwill: Does the design respect the user?

Users start with a reservoir of goodwill. Check for things that drain it:
- Hiding information users want (prices, phone numbers, shipping rates)
- Punishing users for formatting (rigid input requirements)
- Asking for unnecessary information
- Happy talk (marketing fluff blocking the task)
- Sizzle blocking content (splash screens, interstitials, auto-play)

---

## Information Architecture Evaluation

Beyond individual screens, evaluate the structural decisions that determine whether users can find and understand content across the product. Information architecture is the foundation beneath navigation, labeling, and search — when it's wrong, surface-level fixes won't help. This framework draws on Rosenfeld, Morville & Arango's IA model.

### The Four IA Systems

Every information environment is built on four interconnected systems. Evaluate each:

| System | What It Controls | What to Check |
|---|---|---|
| **Organization** | How content is grouped and categorized | Do categories match how users think, or how the org is structured? Are there clear schemes (topical, task-based, audience-based)? |
| **Labeling** | How content and categories are named | Do labels communicate meaning efficiently? Would users use these words? Are labels consistent across the product? |
| **Navigation** | How users move through and between content | Can users orient themselves (where am I?), move forward (where can I go?), and recover (how do I get back?) at every point? |
| **Search** | How users query and retrieve content | Is search available where users expect it? Do results match intent? Are there facets/filters for large result sets? |

### Organization System Critique

| Check | Violation Signal | Fix Direction |
|---|---|---|
| **Scheme consistency** | Some sections organized by topic, others by audience, others by format — with no logic to why | Pick one primary scheme. Use a secondary scheme deliberately (e.g., topical primary, audience secondary) |
| **Mental model match** | Categories reflect internal departments or technical architecture, not user goals | Card sort with users. Reorganize around tasks or topics users recognize |
| **Appropriate granularity** | Too many categories (>7 at top level) or too few (3 categories, each containing 50+ items) | Aim for 5-7 top-level categories. Use progressive disclosure for depth |
| **Cross-cutting content** | Content logically belongs in multiple categories but only appears in one | Provide cross-links, related content, or faceted access. Polyhierarchy is OK |
| **Consistent depth** | Some sections go 5 levels deep while others are flat | Balance depth across sections. Flatten where possible; use search for deep content |

### Labeling System Critique

Labels are the most testable part of IA — and the most frequently wrong.

| Check | Violation Signal | Fix Direction |
|---|---|---|
| **User language** | Labels use internal jargon, product codenames, or technical terms users don't know | Test labels with users (tree test, card sort). Use the words users use in interviews |
| **Specificity** | Vague labels like "Resources," "Solutions," "More," "Manage" | Make labels describe what's inside: "API documentation" not "Resources" |
| **Consistency** | Same concept labeled differently in different places ("Settings" / "Preferences" / "Configuration") | Create a controlled vocabulary. One label per concept, used everywhere |
| **Mutual exclusivity** | Users can't tell the difference between two categories ("Products" vs. "Solutions," "Help" vs. "Support") | Merge overlapping categories or clarify with descriptions |
| **Icon-only labels** | Icons without text for non-universal concepts | Always pair icons with text labels. Icons alone work only for universally understood concepts (search, home, close) |

### Navigation System Critique

| Check | Violation Signal | Fix Direction |
|---|---|---|
| **Orientation** | Users can't tell where they are in the hierarchy | Add breadcrumbs, highlight active nav items, match page title to nav label |
| **Global + local** | Only global navigation exists; users can't browse within a section | Add local/contextual navigation that adapts to the current section |
| **Depth vs. breadth** | Deep hierarchies requiring 4+ clicks to reach common content | Flatten. Provide shortcuts and contextual links to frequently accessed pages |
| **Contextual links** | Content pages are dead ends — no related items, no next steps | Add "related content," cross-links, and contextual navigation within content |
| **Supplemental navigation** | No sitemap, no index, no alternative paths to content | Provide at least one supplemental navigation for complex sites (sitemap, A-Z index, guided paths) |

### Search System Critique

Not every product needs search — but if it has search, evaluate it rigorously.

| Check | Violation Signal | Fix Direction |
|---|---|---|
| **Availability** | Search box is hidden, too small, or absent on content-heavy pages | Make search visible and accessible from every page |
| **Scope clarity** | Users don't know what search covers (this section? the whole site? help docs only?) | Indicate search scope. Offer scope controls if multiple indexes exist |
| **Results quality** | Results don't match user intent; irrelevant items ranked first | Review search algorithm, add metadata, implement best bets for common queries |
| **No-results experience** | "No results found" with no guidance | Suggest alternatives, check spelling, offer category browsing as fallback |
| **Faceted filtering** | Large result sets with no way to narrow down | Add facets/filters based on content attributes (type, date, category, status) |

### IA Quick Diagnostic

Five questions that surface the most common IA failures:

1. **Can a new user find [core content] in under 3 clicks?** If not, the hierarchy is too deep or the labels are wrong
2. **Do the top-level categories make sense to someone outside your organization?** If not, the organization scheme reflects internal structure, not user mental models
3. **If you removed the navigation, could users still guess what each page is about from its title?** If not, labels aren't carrying enough meaning
4. **Is there content that users would reasonably look for in two different places?** If so, do both paths lead to it? If not, cross-linking is broken
5. **When users search, do they find what they need in the top 3 results?** If not, search indexing, metadata, or result ranking needs attention

---

## Content & UX Writing Evaluation

Words are design materials — when you write the text that appears in an interface, you are designing the user experience. Content critique is not about grammar or style preferences; it's about whether the words help users accomplish their goals. This framework draws on established UX writing principles.

### The Three Lenses

Evaluate all interface text through three lenses:

| Lens | Question | Violation Signal |
|---|---|---|
| **Usable** | Do the words help people use the interface? Are they clear and accessible? | Users hesitate, misinterpret, or need to re-read. Labels don't match mental models. Instructions assume knowledge users don't have |
| **Useful** | Do the words represent something people want to do? Do they add value? | Happy talk that doesn't serve the task. Marketing copy where guidance should be. Content that exists for the organization, not the user |
| **Responsible** | Could the words be misused? Are they true, kind, and inclusive? | Blame language in errors. Exclusive pronouns or assumptions. Manipulative patterns (confirmshaming, false urgency) |

### Error Message Evaluation

Error messages are where content quality matters most — users are already frustrated.

| Criterion | Good | Bad |
|---|---|---|
| **Explains what happened** | "We couldn't save your changes because the file is too large (max 25MB)" | "Error 413" |
| **Offers a way forward** | "Try reducing the image size or removing attachments" | "Please try again" |
| **Avoids blame** | "We couldn't find that page" | "You entered an invalid URL" |
| **Is specific** | "Your password needs at least 8 characters and one number" | "Invalid password" |

**Beyond edge cases — consider stress cases.** Go beyond rare technical scenarios to consider emotionally charged situations where careless words cause real harm. Example: an app cheerfully saying "Looks like you have no activity this week!" to someone dealing with a health crisis.

### Voice and Tone Evaluation

| Element | What to Check | Violation Signal |
|---|---|---|
| **Voice consistency** | Does the product sound like the same entity across all screens? | Formal in settings, casual in onboarding, robotic in errors — no coherent personality |
| **Tone appropriateness** | Does the tone match the user's emotional state? | Playful during error recovery. Corporate during celebration. One-size-fits-all regardless of context |
| **Clarity over personality** | In critical moments (errors, security, payments), does clarity win over charm? | Clever copy that obscures meaning. Jokes in error states. Brand voice overwhelming usability |

**Tone is a channel switcher, not a volume knob.** Appropriate tone means different word choices, structure, and emphasis based on context — not just more or less of the same voice.

### Content Critique Checklist

- [ ] **Labels match user language** — Terminology comes from research, not internal jargon (H2: Match Real World)
- [ ] **Button labels describe the action** — "Save project" not "Submit," "Delete account" not "Continue" (Recognition over Recall)
- [ ] **Microcopy reduces cognitive load** — Helper text appears where users need it, not in a separate help section (Tesler's Law)
- [ ] **Empty states guide next action** — Not blank, not just a message — include what to do and why (Blank Slate pattern)
- [ ] **Error messages are helpful** — Explain, don't blame. Offer a fix. Be specific (H9: Error Recovery)
- [ ] **Confirmation text matches the action** — "Delete 3 files permanently?" not "Are you sure?" (H5: Error Prevention)
- [ ] **Progress text is accurate** — Step labels reflect what actually happens in each step, not vague labels like "Details" (H1: Visibility)
- [ ] **No happy talk** — Every word serves the user's task. No filler, no marketing fluff blocking the flow (H8: Minimalist Design)
- [ ] **Inclusive language** — No gendered defaults, cultural assumptions, or exclusionary patterns. Consider who might feel the product wasn't made for them
- [ ] **Accessible writing** — Plain language, meaningful link text, descriptive headings. Works with screen readers

### Content Consistency at Scale

When reviewing products with multiple writers or teams:

| Tool | Purpose |
|---|---|
| **Content style guide** | Documents voice, tone, terminology, and grammar decisions |
| **Word list / glossary** | Defines key terms and their approved usage |
| **UI text patterns** | Reusable text patterns for common elements (buttons, errors, notifications, empty states) |
| **Tone profiles** | Define how voice adapts in different contexts (onboarding, errors, success, help) |

Consistency isn't rigid rules — it's making the experience predictable and trustworthy for users. When every button, error, and notification follows the same patterns, users learn the system faster.

---

## Common Design Problems

Quick pattern recognition for frequent failures:

| Problem | Symptoms | Root Cause | Fix Direction |
|---|---|---|---|
| **Choice paralysis** | Users don't click anything; long time-to-action | Too many options, no hierarchy | Reduce options, add defaults, progressive disclosure |
| **Mystery meat navigation** | Users don't know where links go | Icon-only nav, clever labels, no descriptions | Add text labels, use conventional terms |
| **Feature overload** | Users use 10% of features | Everything visible at once | Progressive disclosure, role-based views |
| **False floor** | Users miss critical content | Key content below the fold with no scroll cue | Add visual continuity, content teasers, scroll indicators |
| **Modal abuse** | Users dismiss without reading | Interrupting, non-contextual modals | Inline messaging, contextual disclosure |
| **Invisible system status** | Users don't know if action worked | No feedback after click/submit | Add loading states, success confirmations, progress |
| **Inconsistent patterns** | Users re-learn on every page | Same function, different UI across pages | Create and follow component library |
| **Jargon barriers** | Users confused by terminology | Internal/technical language in UI | User-test labels, match user vocabulary |
| **Error dead ends** | Users can't recover from errors | Error message with no guidance | Explain what happened + how to fix + one-click recovery |
| **Cognitive overload** | Users abandon complex forms | Too many fields, no chunking, no progress | Multi-step wizard, smart defaults, progressive disclosure |

For more detailed pattern analysis, see `references/design-patterns-catalog.md`.

---

## Quick Critique Checklist

Use during design reviews. Each item maps to a specific principle.

### Information & Content
- [ ] Primary action is immediately clear — (Visual Hierarchy, H8)
- [ ] Content hierarchy matches importance — (Law of Prägnanz)
- [ ] Text is scannable: headings, short paragraphs, bullet points — (Scanning principle)
- [ ] Labels use user language, not internal jargon — (H2: Match Real World)
- [ ] No unnecessary content or happy talk — (H8: Minimalist Design)

### Layout & Grouping
- [ ] Related items are visually grouped — (Law of Proximit
… [2992 more characters trimmed]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap/d-trust.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:47

[Image: original 1440x3543, displayed at 813x2000. Multiply coordinates by 1.77 to map to original image.]

- 🔧 `Bash`: Save before captures for pairs

  <details><summary>result</summary>

```
01-before.png
02-before.png
03-before.png
04-before.png
05-before.png
06-before.png
```
  </details>


**Claude** · 2026-10-30 12:47

Now the fixes. Focus-steal bug in Sheet first.

- 🔧 `Bash`: Fix focus steal, dedupe opener chips, hero kicker

  <details><summary>result</summary>

```
35:  say('Describe a role', 'Describe a role for Q'),
100:    '/site': ['Try me on a role you’re hiring for, or see how I’d read two sample candidates.', say('Describe a role', 'Describe a role')],
102:    '/site/employers': ['Describe a role in a line and I’ll show the criteria I’d propose.', say('Describe a role', 'Describe a role')],
```
  </details>

- 🔧 `Bash`: Apply critique fixes and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Sync snapshot and recapture

  <details><summary>result</summary>

```
no errors
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cap2/d-pricing.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:49

[Image: original 1440x2635, displayed at 1093x2000. Multiply coordinates by 1.32 to map to original image.]

- 🔧 `Bash`: Crop above-the-fold views

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/crop-d-landing.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/crop-d-how.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Save after pairs and run feature test

  <details><summary>result</summary>

```
[2m    - retrying click action[22m
[2m      - waiting 100ms[22m
[2m    57 × waiting for element to be visible, enabled and stable[22m
[2m       - element is not enabled[22m
[2m     - retrying click action[22m
[2m       - waiting 500ms[22m

    at run (/home/user/neo/talent-q-design/qa/scripts/features/public.mjs:90:61)
    at async file:///home/user/neo/talent-q-design/qa/scripts/features/public.mjs:229:1 {
  log: [
    "  - waiting for locator('button').filter({ hasText: 'Start over' })",
    '    - locator resolved to <button disabled type="button" class="ds-btn">Start over</button>',
    '  - attempting click action',
    '    2 × waiting for element to be visible, enabled and stable',
    '      - element is not enabled',
    '    - retrying click action',
    '    - waiting 20ms',
    '    2 × waiting for element to be visible, enabled and stable',
    '      - element is not enabled',
    '    - retrying click action',
    '      - waiting 100ms',
    '    57 × waiting for element to be visible, enabled and stable',
    '       - element is not enabled',
    '     - retrying click action',
    '       - waiting 500ms'
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Persist sample conversation per tab

  <details><summary>result</summary>

```
15:const KEY = 'tq.public.sampleq';
17:let msgs: SMsg[] = (() => { try { return JSON.parse(sessionStorage.getItem(KEY) ?? '[]') as SMsg[]; } catch { return []; } })();
24:const emit = () => { try { sessionStorage.setItem(KEY, JSON.stringify(msgs)); } catch { /* storage unavailable: conversation lives in memory */ } snap = { msgs, state, pendingText }; subs.forEach((f) => f()); };
```
  </details>

- 🔧 `Bash`: Rerun feature test

  <details><summary>result</summary>

```
Command did not complete within its 120s timeout and was moved to the background (ID: b7bjqj229). Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b7bjqj229.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. No output had been read from it when it was moved. A program that buffers its output, or a pipe into one such as tail, can keep the output file empty until the command finishes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>


**Claude** · 2026-10-30 12:53

Meanwhile, I'll write the registry patch.

- 🔧 `Bash`: Check existing patches

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/registry/patches/public.json

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/registry/patches/public.json (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check test output

  <details><summary>result</summary>

```
<tool_use_error>Blocked: sleep 60 followed by: cat /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b7bjqj229.output tail -20. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```
  </details>


**Claude** · 2026-10-30 12:53

Meanwhile, the design note.

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/public.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/public.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check test output

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Monitor`: until grep -q "passed\|Error" /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b7bjqj229.output; do sleep 3; done

  <details><summary>result</summary>

```
<tool_use_error>InputValidationError: Monitor failed due to the following issue:
The required parameter `description` is missing

This tool's schema was not sent to the API — it was not in the discovered-tool set derived from message history. Without the schema in your prompt, typed parameters (arrays, numbers, booleans) get emitted as strings and the client-side parser rejects them. Load the tool first: call ToolSearch with query "select:Monitor", then retry this call. For reference, this tool's input schema is: {"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object","properties":{"description":{"description":"Short human-readable description of what you are monitoring (shown in notifications).","type":"string"},"timeout_ms":{"description":"Kill the monitor after this deadline. Default 300000ms. Deadlines above 1800000ms are capped to 1800000ms. You are notified at expiry and can re-arm.","default":300000,"type":"number","minimum":1000,"maximum":3600000},"command":{"description":"Shell command or script. Each stdout line is an event; exit ends the watch.","type":"string"},"ws":{"description":"WebSocket to open. Each text frame is an event; binary frames are reported as a placeholder line. Socket close ends the watch. Cannot be combined with command.","type":"object","properties":{"url":{"type":"string"},"protocols":{"type":"array","items":{"type":"string","pattern":"^[!#$%&'*+.^_`|~0-9A-Za-z-]+$"}}},"required":["url"],"additionalProperties":false}},"require
… [78 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Wait for test output to appear

  <details><summary>result</summary>

```
FAIL [d] SC-001: no sideways scroll; body text ≥ 12px — 11
FAIL [d] SC-013: comparison is labelled fictional and sample, with no overall score — SAMPLE ANSWER Here are two fictional candidates for a backend role that troubleshoots PostgreSQL and APIs. Tobi’s CV is thin; Seyi’s is polished. Q reads the evidence for each criterion separately, and never turns it into one score. Tobi an
FAIL [d] SC-013: prices are given as hypotheses, no payment — SAMPLE ANSWER For people looking for work, the core is free: no fee to apply or to be found. For employers and agencies, these are the prices we’re testing. They’re hypotheses, not proven prices, and this site takes no payment. Prices being
FAIL [d] SC-008: email code, Google and Microsoft, each labelled simulated
FAIL [d] All public pages: no sideways scroll and text ≥ 12px — /site, /site/pricing, /site/ask
FAIL [m] SC-001: no sideways scroll; body text ≥ 12px — 11
FAIL [m] SC-013: comparison is labelled fictional and sample, with no overall score — SAMPLE ANSWER Here are two fictional candidates for a backend role that troubleshoots PostgreSQL and APIs. Tobi’s CV is thin; Seyi’s is polished. Q reads the evidence for each criterion separately, and never turns it into one score. Tobi an
FAIL [m] SC-013: prices are given as hypotheses, no payment — SAMPLE ANSWER For people looking for work, the core is free: no fee to apply or to be found. For employers and agencies, these are the prices we’re testing. They’re hypotheses, not proven pric
… [257 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Bump small labels to 12px and fix case-sensitive checks

  <details><summary>result</summary>

```
0
[This command modified 2 files you've previously read: ../../qa/scripts/features/public.mjs, journeys/public/public.css. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Rerun feature test in background

  <details><summary>result</summary>

```
Command running in background with ID: bkgkbomcw. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bkgkbomcw.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Check privacy and R1 usage

  <details><summary>result</summary>

```
// Privacy: candidates' discovery rules hold everywhere a recruiter can reach them — search and pools,
// profiles, Q's tools, cached views and downstream artifacts (campaigns). Usage: node privacy.mjs [base]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
const BASE = process.argv[2] || 'http://localhost:4174/';
let fails = 0; const step = (ok, n, x = '') => { if (!ok) fails++; console.log(`${ok ? 'PASS' : 'FAIL'} ${n}${x ? ` · ${String(x).slice(0, 140)}` : ''}`); };
// R1 · Funmi, a confused first-time employer (Crumb & Co bakery). Starts signed out, signs up, and works out
// who to hire entirely by typing to the global Q in imperfect language. Curveballs: changes the role midway
// (shop assistant → part-time bookkeeper), doesn't know "mandate", budget below market, clicks "Discard draft"
// by mistake then says "undo that", leaves and comes back the next day ("where was I?"), and checks that
// Kora Pay's pipeline stays invisible. Usage: node R1.mjs [port] [d,m]
```
  </details>

- 🔧 `Bash`: Wait for feature test results

  <details><summary>result</summary>

```
124/124 passed
```
  </details>

- 🔧 `Bash`: Run privacy and R1/T1/T4 journeys

  <details><summary>result</summary>

```
Command running in background with ID: behr4v9cq. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/behr4v9cq.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Tighten pricing skill matcher

  <details><summary>result</summary>

```
6:const ABOUT_US = /\b(talent ?q|this (app|product|platform|service))\b/;
9:  match: (c) => (/\b(pric\w*|cost|how much|subscription|plans?)\b/.test(c.norm) && ABOUT_US.test(c.norm) && !/\b(role|candidate|salary|offer)\b/.test(c.norm) ? 0.9 : 0),
[This command modified 1 file you've previously read: q/skills/public.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Narrow trust skill matcher and typecheck

  <details><summary>result</summary>

```
20:  match: (c) => (/\b(what (do|does|can) (you|q) decide|do you score (faces|accents|emotion)|trust page)\b/.test(c.norm) ? 0.9 : 0),
```
  </details>

- 🔧 `Bash`: Add signed-in Q pricing test step

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Wait for privacy and journey runs

  <details><summary>result</summary>

```
privacy exit=0 pass=21 fail=0
R1 exit=0 pass=95 fail=0
T1 exit=1 pass=74 fail=2
T4 exit=0 pass=43 fail=0

[exited with code 0]
```
  </details>

- 🔧 `Bash`: Inspect T1 failures

  <details><summary>result</summary>

```
PASS [d] Practice is not proof; map unchanged
PASS [d] Matches from real listings, as claims not promises
FAIL [d] Need-by-need explanation with her own words · Graduate Data Assistant at Tinda asks for 3 things. Spreadsheets: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof yet. Survey analysis: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof 
--
PASS [m] Practice is not proof; map unchanged
PASS [m] Matches from real listings, as claims not promises
FAIL [m] Need-by-need explanation with her own words · Graduate Data Assistant at Tinda asks for 3 things. Spreadsheets: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof yet. Survey analysis: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof 
78
```
  </details>

- 🔧 `Bash`: Check T1 expectation and git status

  <details><summary>result</summary>

```
134:  step('Need-by-need explanation with her own words', /Spreadsheets: mentioned/.test(r) && /Survey analysis: mentioned/.test(r) && /Clear writing: not shown/.test(r), r);
9de512d WIP coverage clusters (six builders in progress; typechecks clean; not yet reviewed or regression-tested)
84b17c0 Master films: J12 closes Film A (hiring), J11 closes Film B (careers); recorder includes both
a5137bb V40 pilot: Q dependency graph generated from source; V32 recorded against J12 and the slice plan; coverage build brief for the six cluster builders
 M ../captures/cx/R1/d-02-home-welcome.png
 M ../captures/cx/R1/d-03-draft-v1.png
 M ../captures/cx/R1/d-04-draft-v1-canvas.png
 M ../captures/cx/R1/d-05-budget-below.png
 M ../captures/cx/R1/d-06-version-v1.png
 M ../captures/cx/R1/d-07-back-next-day.png
 M ../captures/cx/R1/d-08-people.png
 M ../captures/cx/R1/d-09-people-canvas.png
 M ../captures/cx/R1/d-10-propose.png
 M ../captures/cx/R1/d-11-handoff.png
 M ../captures/cx/R1/d-12-post-refused.png
 M ../captures/cx/R1/d-13-verify-ask.png
 M ../captures/cx/R1/d-14-verify-failed.png
 M ../captures/cx/R1/d-15-verified-canvas.png
 M ../captures/cx/R1/d-16-roles.png
 M ../captures/cx/R1/d-17-audit.png
 M ../captures/cx/R1/m-17-audit.png
 M ../captures/cx/T1/d-02-profile-start.png
 M ../captures/cx/T1/d-03-cv-unreadable.png
 M ../captures/cx/T1/d-04-form-mistake.png
 M ../captures/cx/T1/d-05-profile-built.png
 M ../captures/cx/T1/d-05b-proactive.png
 M ../captures/cx/T1/d-06-atlas.png
 M ../
… [693 more characters trimmed]
```
  </details>

- 🔧 `Bash`: See full T1 failure text

  <details><summary>result</summary>

```
q/skills/talent-a.ts:346:    const parts = needs.map((n) => `${n.need}: ${n.state === 'evidenced' ? `evidenced by ${n.basis}` : n.state === 'mentioned' ? `mentioned (${n.basis}), a claim, not proof yet` : 'not shown yet'}`);
q/skills/talent-a.ts:665:    const basis = `${comp.why ?? `${goal.label} listings ask for it.`} In your record it’s ${st === 'none' ? 'not shown yet' : st === 'unclear' ? 'mentioned but not shown' : st === 'partial' ? 'partly shown' : st === 'practice' ? 'practised only' : 'shown'}${comp.from ? ' (your sales evidence covers part of it)' : ''}.`;
```
  </details>

- 🔧 `Bash`: List changed/untracked source files

  <details><summary>result</summary>

```
M src/journeys/assess/Avatar.tsx
 M src/journeys/assess/Bank.tsx
 M src/journeys/assess/Coaching.tsx
 M src/journeys/assess/Exercises.tsx
 M src/journeys/assess/LiveRoom.tsx
 M src/journeys/assess/Review.tsx
 M src/journeys/assess/assess.css
 M src/journeys/hire-d/Explore.tsx
 M src/journeys/hire-d/Scope.tsx
 M src/journeys/hire-d/hire-d.css
 M src/journeys/hire-d/model.ts
 M src/journeys/hire-d/ops.ts
 M src/journeys/org-admin/Frame.tsx
 M src/journeys/org-admin/PagesOrg.tsx
 M src/journeys/org-admin/PagesOversight.tsx
 M src/journeys/org-admin/org-admin.css
 M src/journeys/public/public.css
 M src/journeys/q-tools/model.ts
 M src/journeys/q-tools/pages.tsx
 M src/journeys/q-tools/q-tools.css
 M src/journeys/q-tools/refs.tsx
 M src/journeys/q-tools/views.tsx
 M src/journeys/talent-d/Learn.tsx
 M src/journeys/talent-d/Recovery.tsx
 M src/journeys/talent-d/Work.tsx
 M src/journeys/talent-d/WorkPermit.tsx
 M src/journeys/talent-d/talent-d.css
 M src/q/openers/talent-d.ts
 M src/q/skills/hire-d.ts
 M src/q/skills/public.ts
 M src/q/skills/q-tools.ts
 M src/q/skills/talent-d.ts
 M src/state/areas/q-tools.ts
```
  </details>

- 🔧 `Bash`: See T1 question for failing step

  <details><summary>result</summary>

```
// ---- Entry-level matching, explained ----
  r = await ask('ok show me entry level jobs that fit me');
  w = await world();
  step('Matches from real listings, as claims not promises', /Graduate Data Assistant|Operations Trainee/.test(r) && /can’t promise/.test(r), r);
  await closeQ(); await shot('08-matches');
  r = await ask('why does the tinda graduate data assistant job fit me');
  step('Need-by-need explanation with her own words', /Spreadsheets: mentioned/.test(r) && /Survey analysis: mentioned/.test(r) && /Clear writing: not shown/.test(r), r);
```
  </details>

- 🔧 `Bash`: Run T1 without public area to isolate cause

  <details><summary>result</summary>

```
Command running in background with ID: batblq3vs. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/batblq3vs.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Wait for isolated T1 run

  <details><summary>result</summary>

```
T1(no public) pass=74 fail=2
FAIL [d] Need-by-need explanation with her own words · Graduate Data Assistant 
FAIL [m] Need-by-need explanation with her own words · Graduate Data Assistant 

[exited with code 0]
```
  </details>

- 🔧 `Bash`: Rerun public feature test

  <details><summary>result</summary>

```
Command running in background with ID: bsyj0hn2c. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bsyj0hn2c.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Wait for results and typecheck

  <details><summary>result</summary>

```
125/125 passed
```
  </details>

- 🔧 `Bash`: Record test counts in design note
- 🔧 `TaskStop`: {"task_id": "bocf6ybol"}

  <details><summary>result</summary>

```
9:Tests: `qa/scripts/features/public.mjs` 125/125 (62 desktop + 63 phone; one de
62
63
[This command modified 1 file you've previously read: ../../journeys/design/public.md. Call Read before editing.]
```
  </details>


  <details><summary>result</summary>

```
{"message":"Successfully stopped task: bocf6ybol (cd /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype && npx vite --port 5211 --strictPort > ../vite.log 2>&1)","task_id":"bocf6ybol","task_type":"local_bash","command":"cd /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tq/prototype && npx vite --port 5211 --strictPort > ../vite.log 2>&1"}
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The eight public screens are built and tested: SC-001 to SC-006, SC-008 and SC-013. All are `side: 'public'` in Direction D, on desktop and phone. My feature test passes 125/125. Typechec

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
