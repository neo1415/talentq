# Helper agent agent-ab7c142fe3b5d4109: Design pass R3 pages

Source: `agent-ab7c142fe3b5d4109.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 12:20

Run the design pass for area `hire-c` (journey R3 Ngozi, the busy HR team) in /home/user/neo/talent-q-design/prototype. First read /home/user/neo/talent-q-design/journeys/DESIGN-PASS-BRIEF.md and follow it exactly, including loading the named skills with the Skill tool and applying them. Also read /home/user/neo/talent-q-design/journeys/BUILD-BRIEF.md for the contracts and your file ownership; you own the same `hire-c` files as before.

Your dev server port is 5183.

**Recruiter pages:**
- `/r/messages`: inbox, threads, drafts, version diff, approvals, offline queue, simulated-send receipts.
- `/r/pipeline`.
- `/r/calendar` and `/r/calendar/connect`: the cross-time-zone overlap. Use `dataviz` for the week view and overlap.
- `/r/team`.
- `/r/setup` and `/r/setup/handbook`.
- `/r/outreach`.

**Candidate pages:** `/c/messages` and `/c/slots`. Make these warm and personal, not institutional.

**Q reply cards:** cover every card your skills produce, especially the draft and approval cards in the founder's sequence: "draft an interview invitation" → "Change it to Friday and make the tone more friendly" → "Send it". The draft, its diff and the pre-send checks must read clearly in the Q thread on desktop and in the phone Q sheet.

R3.mjs must keep passing. Also run qa/scripts/review/privacy.mjs against your server.

- 🔧 `Bash`: Read the design pass brief

  <details><summary>result</summary>

```
# Design pass brief: bring every journey page up to the Direction D standard

The founder's verdict: the ten journeys work (keep every behaviour, the shared store, the Q integration
and the contracts), but the pages went from "functional" to "recorded" without a design pass. Your job is
to make the real pages in your area better: visibly, on desktop and phone.

This is the same checkout as before, and other area builders are working at the same time. File ownership
is unchanged from `journeys/BUILD-BRIEF.md`; read that file for the contracts and the files you own.

## What the lead already changed in the shared layer (don't redo, don't patch locally)

- **Q noticed cards.** The observation and its main actions show as chips. "Why am I seeing this?",
  "Later" and "Dismiss" sit in a quiet footer row.
- **Simulation label.** It appears once in the shell (rail brand; a thin bar on phones). Pages no longer
  carry a SIMULATED badge. Keep per-action labels where a real system would act: "Simulated send",
  "Simulated upload" and so on.
- **Page kicker.** The kicker is one line of context and truncates. Put status in tags or banners, never in
  the kicker. Rewrite any kicker in your area that crams in status or several facts.
- **Elevation.** There is one level: a `ds-sheet` inside a `ds-sheet` becomes a flat bordered panel. Don't
  nest floating cards.
- **Motion tokens.** Import `src/ds/motion.ts` (`DUR`, `EASE`, `arrive`). Use them for anything you animate:
  feedback 100–200 ms
… [3849 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read build brief and repo state

  <details><summary>result</summary>

```
# Build brief for journey areas (CX3/CX4)

You are one of five builders working **in the same checkout at the same time**. Other builders are editing
other files right now. Stay inside the files you own; everything else is read-only for you.

Read first: `journeys/JOURNEY-MAP.md` (your journeys, cast, curveballs), `journeys/AUDIT-BATCH1.md`,
`contracts/Q-WORKSPACE-CONTRACT.md`, `design-system/DIRECTION-D-SYSTEM.md`, then the code named below.
The prototype is `talent-q-design/prototype` (React 18 + TypeScript + Vite, `motion/react`).

## Non-negotiables
- Direction D only (paper canvas, ink thread, gold reserved for Q). Reuse `src/ds/*` components and
  classes (`ds-sheet`, `ds-btn`, `ds-opt`, `ds-filter`, `ds-field`, `ds-input`, `ds-banner`, `ds-sim`,
  `Canvas`, `Glyph`, `QMark`). Candidate pages get warmth automatically (`data-audience`).
- **Q is the centre.** Every capability in your journeys must be reachable by typing (or speaking) to the
  global Q, in imperfect natural language, from any page — not only by clicking. Pages are where work is
  seen and refined; Q does the work, navigates, asks clarifying questions, explains, and asks for approval.
- Honest simulation: nothing is really sent, booked or verified. Use statuses like `SENT_SIMULATED`, label
  with `<span className="ds-sim">Simulated</span>` where a real system would act, and never present
  scripted replies as general AI. If Q cannot handle something, it says so (the engine's fallback does this).
- Conseque
… [7572 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find hire-c files and journey info

  <details><summary>result</summary>

```
9:| Recruiter | **Ngozi Eze** | HR lead at Kora Pay; colleagues Seyi (Lagos) and Musa (London) · R3 |
78:### R3: The busy HR team (Ngozi)
97:- [recover] Ngozi is offline. Sends queue; nothing is claimed as sent.
find: 'qa': No such file or directory
src/q/skills/hire-c.ts
src/q/proactive/hire-c.ts
src/journeys/hire-c
src/journeys/hire-c/Calendar.tsx
src/journeys/hire-c/Team.tsx
src/journeys/hire-c/lib.ts
src/journeys/hire-c/Setup.tsx
src/journeys/hire-c/refs.tsx
src/journeys/hire-c/Pipeline.tsx
src/journeys/hire-c/Messages.tsx
src/q/proactive:
agency.ts
hire-a.ts
hire-b.ts
hire-c.ts
talent-a.ts
talent-b.ts
talent-c.ts

src/q/skills:
agency.ts
core.ts
hire-a.ts
hire-b.ts
hire-c.ts
hiring-basic.ts
talent-a.ts
talent-b.ts
talent-c.ts

src/routes:
agency.tsx
core.tsx
entry.tsx
gallery.tsx
guard.tsx
hire-a.tsx
hire-b.tsx
hire-c.tsx
registry.ts
talent-a.tsx
talent-b.tsx
talent-c.tsx

src/state/areas:
README.md
agency.ts
hire-a.ts
hire-b.ts
hire-c.ts
talent-a.ts
talent-b.ts
talent-c.ts

src/styles:
agency.css
base.css
components.css
gallery.css
hire-a.css
hire-b.css
hire-c.css
talent-a.css
talent-b.css
talent-c.css
tokens.css
../qa/scripts/journeys:
R1.mjs
R2.mjs
R3.mjs
R4.mjs
R5.mjs
T1.mjs
T2.mjs
T3.mjs
T4.mjs
T5.mjs
run-all.sh

../qa/scripts/review:
axe-all.mjs
capture-all.mjs
interview-followup.mjs
keyboard.mjs
privacy.mjs
```
  </details>

- 🔧 `Bash`: Journey R3 and file sizes

  <details><summary>result</summary>

```
**Curveballs**
- [info] Kunle has an impressive CV but weak evidence. Q separates "unknown" from "weak".
- [info] Zara's GitHub is rate-limited. Q says so, retries, and shows it as unknown.
- [mind] Ada challenges "Talk to Tobi first". Q re-weights by her criterion and shows what changes.
- [info] Kunle disputes the assessment. Q opens a review request, and the result is marked "under review".
- [mind] "Compare on evidence from the last year only". Q's ledger filter changes and the margin notes are rewritten.

### R3: The busy HR team (Ngozi)

**Flow**
1. Team and permissions ＋
2. Organisation guidelines ✓
3. Calendar connections ✓
4. Panel selection ＋
5. Scheduling ◐ across time zones
6. Correspondence inbox ＋
7. Approved channels ◐
8. Reminders ＋
9. Interviews list ＋
10. Feedback from both sides ＋
11. Pipeline board ＋

**Curveballs**
- [info] The preferred slot is taken after the proposal. Q re-checks before sending (existing hard scenario).
- [info] Musa is in London. Q shows fairness for the time zone.
- [mind] Zara asks to reschedule. Q handles the counterproposal.
- [recover] Ngozi is offline. Sends queue; nothing is claimed as sent.
- [recover] An invitation was drafted but not approved. The proactive engine flags it and does not send it.
- [mind] Seyi swaps the panel. Holds are re-validated.

### R4: The high-volume agency (Dele)

**Flow**
1. Agency home ＋ with clients
2. Mandates per client ＋
3. Talent pool and saved searches ＋
4. Concurrent agents ✓ (planner, run pe
… [612 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read routes, css, area state, seeds

  <details><summary>result</summary>

```
// Routes for R3 (Ngozi). Owned by this area (see journeys/BUILD-BRIEF.md).
// Native pages: messages (both sides), pipeline, team, calendar, organisation and policy, interview times.
// The older screens stay reachable where they still add something (calendar connections, handbook import).
import type { ReactNode } from 'react';
import { registerRoute } from './registry';
import { OrgSetup } from '../screens/OrgSetup';
import { Outreach } from '../screens/Outreach';
import { CalendarSetup } from '../screens/CalendarSetup';
import { Messages } from '../journeys/hire-c/Messages';
import { CandidateMessages, CandidateSlots } from '../journeys/hire-c/CandidateMessages';
import { Pipeline } from '../journeys/hire-c/Pipeline';
import { Team } from '../journeys/hire-c/Team';
import { Setup } from '../journeys/hire-c/Setup';
import { Calendar } from '../journeys/hire-c/Calendar';
import '../journeys/hire-c/refs';
import '../styles/hire-c.css';

const legacy = (n: ReactNode) => <div className="ds-legacy" style={{ minHeight: '100vh' }}>{n}</div>;

registerRoute({ path: '/r/pipeline', side: 'recruiter', label: 'the pipeline', render: () => <Pipeline />, nav: { group: 'Hiring', label: 'Pipeline', icon: 'measures', tab: true, order: 11, orgKind: 'EMPLOYER' } });
registerRoute({ path: '/r/messages', side: 'recruiter', label: 'messages', render: () => <Messages />, nav: { group: 'Hiring', label: 'Messages', icon: 'mail', tab: true, order: 15, badge: 'approvals', orgKind: 'EMPLOYER' } });
r
… [16826 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read messages pages and refs

  <details><summary>result</summary>

```
<persisted-output>
Output too large (30.5KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b1dps2w34.txt

Preview (first 2KB):
// /r/messages: the correspondence inbox. Threads per candidate, drafts with versions, the checks Q ran,
// and approve / edit / discard. There is no way to send that skips the checks and an explicit approval.
import { useEffect, useMemo, useState } from 'react';
import { actorOf, orgOf, personOf, simNow, useWorld } from '../../mock/world';
import { Canvas, useNarrow } from '../../ds/Workspace';
import { runAction, useViewState } from '../../q/core/engine';
import { hc } from '../../state/areas/hire-c';
import type { Msg } from '../../state/domain';
import { CAN_SEND, city, delivered, diffWords, firstOf, KIND_LABEL, LAGOS, mandateTitle, msgStatusLabel, nameOf, tDay, tTime } from './lib';
import { ChecksList } from './refs';

type Filter = 'all' | 'approval' | 'drafts' | 'reply' | 'sent';
const FILTERS: [Filter, string][] = [['all', 'All'], ['approval', 'Waiting for approval'], ['drafts', 'Drafts'], ['reply', 'Waiting on us'], ['sent', 'Sent']];
const when = (iso: string) => `${tDay(iso, LAGOS)}, ${tTime(iso, LAGOS)}`;

export function Messages() {
  const w = useWorld((x) => x);
  const a = actorOf(w);
  const narrow = useNarrow();
  const [sel, setSel] = useViewState<string>('sel', '');
  const [filter, setFilter] = useViewState<Filter>('filter', 'all');
  const groups = useMemo(() => {
… [556 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Messages.tsx
- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/refs.tsx

  <details><summary>result</summary>

```
1	// /r/messages: the correspondence inbox. Threads per candidate, drafts with versions, the checks Q ran,
2	// and approve / edit / discard. There is no way to send that skips the checks and an explicit approval.
3	import { useEffect, useMemo, useState } from 'react';
4	import { actorOf, orgOf, personOf, simNow, useWorld } from '../../mock/world';
5	import { Canvas, useNarrow } from '../../ds/Workspace';
6	import { runAction, useViewState } from '../../q/core/engine';
7	import { hc } from '../../state/areas/hire-c';
8	import type { Msg } from '../../state/domain';
9	import { CAN_SEND, city, delivered, diffWords, firstOf, KIND_LABEL, LAGOS, mandateTitle, msgStatusLabel, nameOf, tDay, tTime } from './lib';
10	import { ChecksList } from './refs';
11	
12	type Filter = 'all' | 'approval' | 'drafts' | 'reply' | 'sent';
13	const FILTERS: [Filter, string][] = [['all', 'All'], ['approval', 'Waiting for approval'], ['drafts', 'Drafts'], ['reply', 'Waiting on us'], ['sent', 'Sent']];
14	const when = (iso: string) => `${tDay(iso, LAGOS)}, ${tTime(iso, LAGOS)}`;
15	
16	export function Messages() {
17	  const w = useWorld((x) => x);
18	  const a = actorOf(w);
19	  const narrow = useNarrow();
20	  const [sel, setSel] = useViewState<string>('sel', '');
21	  const [filter, setFilter] = useViewState<Filter>('filter', 'all');
22	  const groups = useMemo(() => {
23	    const byP = new Map<string, { pid: string; msgs: { m: Msg; mandateId?: string }[] }>();
24	    for (const t of w.threads.filter
… [11463 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
1	// Live cards Q shows inside its replies for R3: a draft at a given version, the change between versions,
2	// the pre-send checks, and proposed interview times with everyone's local time.
3	import { useState } from 'react';
4	import { useWorld } from '../../mock/world';
5	import { hc } from '../../state/areas/hire-c';
6	import { registerRef } from '../../q/refs';
7	import { city, diffWords, findMsg, firstOf, LAGOS, msgStatusLabel, nameOf, tDay, tTime, tzOf } from './lib';
8	
9	function DraftRef({ id }: { id: string }) {
10	  const [msgId, vs] = id.split('@');
11	  const d = useWorld((w) => hc(w).drafts[msgId]);
12	  const m = useWorld((w) => findMsg(w, msgId)?.m);
13	  const to = useWorld((w) => (d ? nameOf(w, d.personId) : m ? nameOf(w, m.to) : ''));
14	  const [all, setAll] = useState(false);
15	  if (!m) return null;
16	  const v = d?.versions.find((x) => x.v === Number(vs)) ?? d?.versions[d.versions.length - 1];
17	  const latest = d?.versions[d.versions.length - 1]?.v ?? 1;
18	  const body = v?.body ?? m.body;
19	  const long = body.split('\n').length > 7 || body.length > 420;
20	  return (
21	    <div className="hc-card" role="group" aria-label={`Draft version ${v?.v ?? 1} to ${to}`}>
22	      <div className="hc-card-head"><span className="lab">{v ? `v${v.v} · ` : ''}to {to}</span><span className="hc-status" data-s={m.status}>{msgStatusLabel[m.status]}</span></div>
23	      <p className="hc-subj">{v?.subject ?? m.subject}</p>
24	      <div className={`hc-body ${long 
… [4208 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/CandidateMessages.tsx

  <details><summary>result</summary>

```
1	// Candidate side of correspondence (/c/messages) and interview times (/c/slots). Candidates see only what was
2	// actually sent to them (never drafts), in their own time zone, with an honest status. Replying, confirming
3	// and asking to move are explicit button presses; Q can do the same by typing.
4	import { useState } from 'react';
5	import { actorOf, orgOf, simNow, useWorld, type World } from '../../mock/world';
6	import { Canvas, useNarrow } from '../../ds/Workspace';
7	import { runAction, useViewState } from '../../q/core/engine';
8	import type { CalEvent, Msg } from '../../state/domain';
9	import { addDays, city, evStatusLabel, firstOf, LAGOS, nameOf, nextWeek, offsetOf, tDay, tLong, tTime } from './lib';
10	import { SlotPicker } from '../../screens/SlotPicker';
11	
12	const visible = (m: Msg, pid: string) => m.from === pid ? m.status !== 'DISCARDED' : m.status === 'SENT_SIMULATED' || m.status === 'RECEIVED';
13	export function candidateThreads(w: World, pid: string) {
14	  const byOrg = new Map<string, { orgId: string; threadId: string; msgs: Msg[] }>();
15	  for (const t of w.threads.filter((x) => x.personId === pid)) {
16	    const ms = t.messages.filter((m) => visible(m, pid)); if (!ms.length) continue;
17	    const g = byOrg.get(t.orgId) ?? { orgId: t.orgId, threadId: t.id, msgs: [] };
18	    g.msgs.push(...ms); if (ms.some((m) => m.from !== pid)) g.threadId = t.id;
19	    byOrg.set(t.orgId, g);
20	  }
21	  return [...byOrg.values()].map((g) => ({ ...g, msgs:
… [12288 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read calendar, pipeline, team, setup pages

  <details><summary>result</summary>

```
// /r/calendar: next week for the hiring team across Lagos and London (busy/free only), holds, invitations,
// confirmations and requests to move, interview panels with who changed them, and a test switch for
// "the proposed time is taken before it's sent".
import { useState } from 'react';
import { actorOf, emit, personOf, update, useWorld } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { runAction } from '../../q/core/engine';
import { Link } from '../../ui/router';
import { hc } from '../../state/areas/hire-c';
import { CAN_MOVE, city, dateIn, evStatusLabel, firstOf, interviewHours, LAGOS, listNames, nameOf, nextWeek, orgMembers, tDay, tTime, tzNote } from './lib';

export function Calendar() {
  const w = useWorld((x) => x);
  const a = actorOf(w);
  const days = nextWeek(w);
  const mem = orgMembers(w, a.orgId).filter((m) => m.role !== 'VIEWER');
  const [h0, h1] = interviewHours(w, a.orgId);
  const mine = w.calendar.filter((e) => e.orgId === a.orgId);
  const events = mine.filter((e) => e.status !== 'CANCELLED' && (e.status === 'HOLD' || e.personId)).sort((x, y) => x.start.localeCompare(y.start));
  const prop = hc(w).proposals[a.id];
  const ivs = w.interviews.filter((i) => i.orgId === a.orgId && i.status !== 'CANCELLED');
  const changes = hc(w).panelChanges;
  const can = CAN_MOVE.includes(a.role ?? 'VIEWER');
  const fmt = (m: number) => `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`;
  return (
 
… [26057 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check legacy screens and lib

  <details><summary>result</summary>

```
107 src/screens/OrgSetup.tsx
  112 src/screens/Outreach.tsx
  146 src/screens/CalendarSetup.tsx
  104 src/screens/SlotPicker.tsx
  469 total
src/journeys/hire-c/CandidateMessages.tsx
src/routes/hire-c.tsx
// R3 logic shared by Q's skills and the pages: time zones, free/busy, slot finding, drafting templates,
// the pre-send checks (approval and delegation, candidate, calendar, guidelines, consent) and the simulated send.
// Nothing here really sends or books: statuses say SENT_SIMULATED and receipts are fake.
import { actorOf, emit, now, orgOf, personOf, simNow, uid, type World } from '../../mock/world';
import { appendQ } from '../../q/core/engine';
import type { Actor, CalEvent, Msg, OrgRole, Stage, Thread } from '../../state/domain';
import { STAGE_LABEL } from '../../state/domain';
import { hc, hcw, type Check, type DraftKind, type DraftMeta, type Guide, type Slot, type Tone } from '../../state/areas/hire-c';

// ---------------- Time ----------------
export const LAGOS = 'Africa/Lagos';
const CITY: Record<string, string> = { 'Africa/Lagos': 'Lagos', 'Europe/London': 'London', 'Africa/Accra': 'Accra', 'Africa/Nairobi': 'Nairobi' };
export const city = (tz: string) => CITY[tz] ?? tz.split('/').pop()!.replace(/_/g, ' ');
const f = (iso: string, tz: string, o: Intl.DateTimeFormatOptions) => new Intl.DateTimeFormat('en-GB', { timeZone: tz, ...o }).format(new Date(iso));
export const tTime = (iso: string, tz: string) => f(iso, tz, { hour: '2-digit', minute: '2-digit', hourCycl
… [7777 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read legacy outreach, calendar setup, org setup screens

  <details><summary>result</summary>

```
// P6 · SC-049 Approve outgoing message, SC-048 composer, SC-158 bounded delegation, SC-047 contact permission.
// Policy is resolved before drafting and shown before approval. Approval binds to the exact text (hash).
import { useEffect, useRef, useState } from 'react';
import { POLICY_PRECEDENCE, type DelegationMode } from '@contracts';
import { update, useWorld } from '../mock/world';
import { approveOutreach, sha256 } from '../q/scripts';
import { Banner, Button, Choice, Label, Sim, TextArea, toast } from '../ui/kit';
import { Link } from '../ui/router';

const UNDO_MS = 5000;

export function Outreach() {
  const w = useWorld((x) => x);
  const pending = w.proposals.filter((p) => p.status === 'AWAITING_APPROVAL' || p.status === 'APPROVED' || p.status === 'EXECUTING');
  const [selId, setSelId] = useState<string | null>(null);
  const sel = pending.find((p) => p.proposalId === selId) ?? pending[0];
  const [body, setBody] = useState(sel?.payload.body ?? '');
  const [hash, setHash] = useState(sel?.payloadHash ?? '');
  const timer = useRef<number | null>(null);
  useEffect(() => { setBody(sel?.payload.body ?? ''); setHash(sel?.payloadHash ?? ''); }, [sel?.proposalId]);
  useEffect(() => { if (sel) sha256(JSON.stringify({ ...sel.payload, body })).then(setHash); }, [body, sel]);
  const edited = sel && body !== sel.payload.body;

  const approve = () => {
    if (!sel) return;
    const id = sel.proposalId;
    update((d) => { d.proposals.find((p) => p.proposalId === id)!.st
… [25083 more characters trimmed]
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:design-critique"}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-critique
```
  </details>


**User** · 2026-10-29 12:20

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
… [2844 more characters trimmed]

- 🔧 `Skill`: {"skill": "design-skills:design-elevation"}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-29 12:20

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

- 🔧 `Skill`: {"skill": "design-skills:interaction-design"}

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-29 12:20

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

- 🔧 `Skill`: {"skill": "design-skills:ux-writing"}
- 🔧 `Skill`: {"skill": "dataviz"}
- 🔧 `Skill`: {"skill": "design-superpowers:creative"}

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-29 12:20

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


  <details><summary>result</summary>

```
Launching skill: dataviz
```
  </details>


**User** · 2026-10-29 12:20

Base directory for this skill: /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz

# Data Visualization

A chart is **read by people and executed by you**. This skill turns "make it look
good" into a procedure with checks, so the result is right by construction rather
than by taste.

**The method here is design-system-agnostic.** Nothing in the procedure, the form
heuristic, the six checks, or the mark specs is specific to one product. A design
system supplies a small set of *parameters* (its ramps, a categorical order, a
diverging pair, a status palette, a texture, its surfaces, its filter components);
the method consumes them unchanged. A **validated default palette** is the
reference instance, fully specified in `references/palette.md`. To target your
brand, read that file's structure and substitute its values - touch nothing else.

> The single most important habit: **the color part is computable, so compute it.**
> Never eyeball whether a palette is colorblind-safe - run `scripts/validate_palette.js`.

## The procedure - do these in order

Color comes LAST. Most bad charts pick colors first.

1. **Pick the form.** What is the data's job - magnitude, identity, polarity, a
   single headline, change-over-time? The job picks the chart type, and sometimes
   the answer is *not a chart* (a stat tile or hero number). -> `references/choosing-a-form.md`
2. **Assign color by the job it does.** Categorical (identity), sequential
   (magnitude), diverging (polarity), or status (state) - each has one rule.
   Assign categorical hues in fixed order, never cycled. -> `references/color-formula.md`
3. **VALIDATE the palette - run the script, don't reason about Delta E.**
   `node scripts/validate_palette.js "<hex,hex,...>" --mode light` (relative to
   this skill's base directory - or load it as `<script type="module">` in the
   chart's own page, where it reads
   `data-palette` off `<body>` and logs a `console.table` report). It returns
   pass/fail on the lightness band, chroma floor, adjacent-pair CVD separation,
   the normal-vision floor, and contrast. Fix anything that FAILs before continuing. Re-run for
   `--mode dark` with that mode's surface.
4. **Apply mark specs & spacers.** Thin marks, 4px rounded data-ends anchored to
   the baseline, 2px lines, >=8px markers, a 2px surface gap between fills (stacked
   segments and adjacent bars alike) and a 2px surface ring on overlapping marks,
   selective direct labels. -> `references/marks-and-anatomy.md`
5. **Add the hover layer - by default.** An HTML/SVG chart *is* interactive; ship
   a crosshair+tooltip on line/area and a per-mark hover tooltip on bar/dot/cell.
   The only form that skips it is a bare stat tile with no plot. Hit targets bigger
   than the mark; filters in one row above the charts. -> `references/interaction.md`
6. **Final accessibility pass.** For >= 2 series a legend is always present and <= 4
   are also direct-labeled (a single series needs no legend box - the title names
   it), so identity is never color-alone; a table view exists; dark mode is **selected** - its own
   steps from the same ramps, validated against the dark surface, not an automatic
   flip; texture is available for the CVD/print/forced-colors case.
7. **Render it and look at it.** The validator checks color, not layout - open or
   screenshot the output and eyeball it for label collisions, geometry, and overflow
   before calling it done.

Then check the result against **`references/anti-patterns.md`** - it is the catalog
of what goes wrong. If your chart matches an entry, it's wrong.

## Non-negotiables (true in every design system)

- **Assign categorical hues in fixed order, never cycled.** A 9th series is never a
  generated hue - it folds into "Other," small multiples, or composite encoding.
- **One axis.** Never a dual-axis chart (two y-scales). Two measures of different
  scale -> two charts, small multiples, or indexed to a common base. *(This is the
  #1 chart mistake - see anti-patterns.)*
- **Color follows the entity, never its rank.** A filter that changes the series
  count must not repaint the survivors.
- **Sequential = one hue, light->dark. Diverging = two hues + a neutral gray
  midpoint.** Never a rainbow; never a hue at the diverging midpoint.
- **Run the validator before shipping any categorical palette.** CVD Delta E >= 8 is the
  target (OKLab ×100); 6-8 is a floor that is legal ONLY with secondary encoding. A
  normal-vision floor below 15 is a hard FAIL - full-color readers can't tell the
  pair apart; re-step it on the adjacent pairlist (secondary encoding does not excuse
  this one); under `--pairs all` cut series or facet instead - see check 4. A contrast WARN
  obligates visible labels or a table view - it is not dismissable.
- **Thin marks; a legend always present for >= 2 series (none for one), with
  selective direct labels (never a number on every point); recessive grid/axes.**
- **Text wears text tokens, never the series color** - values, labels, and legends
  stay in primary/secondary/muted ink; a colored mark beside them carries identity.
- **Status colors are reserved** (good/warning/serious/critical) and never reused
  for "series 4"; they ship with an icon + label, never color alone.

## Plugging in a design system

The method is invariant; only these parameters change per system. The reference
instance - every value filled in - is `references/palette.md`.

| Parameter | What the system provides |
|---|---|
| **Ramps** | the hue scales (named steps) the palette draws from |
| **Categorical theme** | the fixed hue order (a named theme); default + alternates |
| **Sequential hue** | the default single hue for magnitude |
| **Diverging pair** | two warm/cool poles + a neutral midpoint |
| **Status palette** | good / warning / serious / critical - steps distinct from categorical |
| **Texture fill** | one directional hand-drawn fill, used at 45° / 135° |
| **Surfaces** | light & dark chart-surface colors (the validator needs these) |
| **Filter controls** | date-range & dimension controls (behavioral spec in `interaction.md`) |

To onboard a new system: fill those rows, feed its ramps to the validator, and let
it snap each slot to the nearest passing step. Structure and rules stay as written.

## Reference files

| File | What it answers |
|------|-----------------|
| `references/choosing-a-form.md` | Which chart type / is it even a chart? |
| `references/color-formula.md` | The four jobs, the six checks, snap-to-passing |
| `references/marks-and-anatomy.md` | Mark specs, spacers, labels, figures, hero number |
| `references/interaction.md` | Tooltips & hover, filters & time ranges |
| `references/components.md` | The pieces a chart is made of - build each in plain HTML |
| `references/anti-patterns.md` | **What goes wrong - check every chart against this** |
| `references/palette.md` | **The reference palette instance** - every parameter, filled in; swap for your brand's |
| `scripts/validate_palette.js` | Runnable six-checks validator (run it; don't eyeball) |


  <details><summary>result</summary>

```
Launching skill: design-superpowers:creative
```
  </details>


**User** · 2026-10-29 12:20

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

- 🔧 `Bash`: Read dataviz references on form and interaction
- 🔧 `Bash`: Read motion atlas and motion tokens

  <details><summary>result</summary>

```
# Choosing a form

Decide this **before** color. The data's job picks the form - and sometimes the
right form is not a chart.

## Is it even a chart?

| The data is... | Use | Not |
|---|---|---|
| A single current value (+ maybe a trend) | **Stat tile** (value + delta + sparkline) | A one-bar bar chart |
| A handful of headline numbers | **KPI row** of stat tiles | A grouped bar chart |
| The one number a dashboard leads with | **Hero figure** (>=48px, sans) | - |
| A single ratio against a limit | **Meter** (same-ramp track) | A pie of 2 slices |
| More than ~7 classes that all carry meaning | A **table** (or table + chart) | More colors |

If a chart *is* right, pick the type by the job:

## The job -> the type

| Job (what the reader must do) | Default form | Color job |
|---|---|---|
| Compare magnitude, low -> high | bar / column; **heatmap** for a grid | sequential (one hue) |
| Trend over time | line; area for a single series | sequential or 1 categorical |
| Tell distinct series apart | grouped/stacked bar, multi-line | **categorical** |
| One series is the point, rest are context | **emphasis** (highlight one, gray the rest) | 1 hue + gray |
| Above/below a baseline; delta to target | diverging bar, or line vs baseline | diverging |
| Part-to-whole | **stacked bar** (go horizontal for many / long-named categories) | categorical |
| Ordered-scale share (Likert, sentiment, agree<->disagree) | **diverging stacked bar**, centered on neutral | diverging |
| Before -> aft
… [11076 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
MOTION-COVERAGE.csv
STATE-MACHINES.md
5:## Q presence (`prototype/src/q/QPresence.tsx`)
19:## Run lifecycle (`contracts/run.ts`, `prototype/src/mock/runtime.ts`)
28:## Scheduling (`contracts/scheduling.ts` `SCHEDULING_TRANSITIONS`)
43:## Memory item lifecycle (`contracts/memory.ts`)
55:## Interview (`prototype/src/screens/Interview.tsx`)
// Motion tokens (interaction-design skill: feedback 100–200 ms, orientation 200–400 ms, enter slower than
// exit, decelerate in / accelerate out, nothing functional over 500 ms). Every animation in the shell and
// shared components takes its timing from here; reduced motion is handled globally by MotionConfig.
export const DUR = { fast: 0.1, normal: 0.2, slow: 0.3 } as const;
export const EASE = { standard: [0.2, 0, 0, 1], enter: [0, 0, 0.2, 1], exit: [0.4, 0, 1, 1] } as const;
/** Something new arriving in place (a message, a card, a page): rise 6 px and fade in. */
export const arrive = { initial: { opacity: 0, y: 6 }, animate: { opacity: 1, y: 0, transition: { duration: DUR.normal, ease: EASE.enter } }, exit: { opacity: 0, transition: { duration: DUR.fast, ease: EASE.exit } } } as const;
```
  </details>

- 🔧 `Bash`: Find relevant motion requirements

  <details><summary>result</summary>

```
motion_id,name,event_trigger,primary_surface,reduced_motion_fallback,status,route,evidence,note
MO-001,Q orb idle,app:idle,Q Home and interview,Static gold icon,PROTOTYPED,/r/home,,Driven by a real state or run event; reduced-motion handled by MotionConfig/CSS. Dedicated clip not recorded yet.
MO-002,Q listens,voice:recording,Voice interview,Listening text and transcript,PROTOTYPED,/gallery/states,prototype/src/ds/QMark.tsx (listening mood: core grows with input level); prototype/src/journeys/gallery/StatesGallery.tsx (Q moods),"Listening mood exists in the Q mark and is shown as a live specimen. Not yet driven by the microphone in the rebuilt /c/interview, whose mic button changes label and colour without motion. Re-pointed from /c/interview."
MO-003,Q thinks,run:accepted,All run views,Accepted task label,PROTOTYPED,/r/mandate,Shown in captures/video/F1-*.mp4,Driven by a real state or run event; appears in a journey film. Dedicated 8–20 s clip and reduced-motion capture still to do.
MO-004,Q speaks,voice:audio-out,Voice/video,Captions,RESEARCHED,,,
MO-007,Q reconnected,transport:restored,Any run,Connected message,PROTOTYPED,/r/sourcing,Shown in captures/video/F1-*.mp4,Driven by a real state or run event; appears in a journey film. Dedicated 8–20 s clip and reduced-motion capture still to do.
MO-015,Mandate wording revised,mandate:patched,Mandate builder,Text diff,PROTOTYPED,/r/mandate,Shown in captures/video/F1-*.mp4,Driven by a real state or run event; appears in a journey 
… [2684 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List before captures and capture script

  <details><summary>result</summary>

```
p_grace_c_slots.png
p_zara_c_messages.png
u_ada_r_calendar.png
u_ada_r_messages.png
u_ada_r_pipeline.png
u_ada_r_setup.png
u_ada_r_team.png
01-ada-diff-desktop.png
02-ada-approval-desktop.png
03-ngozi-messages-desktop.png
04-ngozi-offline-queued-desktop.png
05-ngozi-overlap-desktop.png
06-ngozi-calendar-desktop.png
07-ngozi-pipeline-desktop.png
08-ngozi-panel-notice-desktop.png
09-zara-messages-desktop.png
10-zara-slots-desktop.png
11-ngozi-team-desktop.png
12-ngozi-setup-desktop.png
13-phone-diff.png
14-phone-approval.png
15-phone-messages.png
16-phone-pipeline.png
17-phone-calendar.png
18-phone-team.png
19-phone-setup.png
20-phone-zara-messages.png
// Design review captures: every route as the person who uses it, desktop (1440×900) and phone (390×844),
// full page. Used for the visual audit and before/after comparison. Usage: node capture-all.mjs <base> <outdir>
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
const [BASE = 'http://localhost:4174/', OUT = 'review', ONLY = ''] = process.argv.slice(2);
export const PAGES = {
  u_funmi: ['/r/home', '/r/roles'],
  u_ada: ['/r/home', '/r/plan', '/r/compare', '/r/people/p_tobi', '/r/interviews', '/r/pipeline', '/r/messages', '/r/calendar', '/r/team', '/r/setup', '/r/roles', '/r/audit', '/r/memory', '/r/mandate', '/r/sourcing', '/settings'],
  u_dele: ['/r/home', '/r/agency/agents', '/r/agency/campaigns', '/r/agency/clients', '/r/agency/client/org_kora', '/r/agency/compare', 
… [1895 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Start dev server on port 5183

  <details><summary>result</summary>

```
Command running in background with ID: bm12fz9qj. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bm12fz9qj.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Read R3 journey script

  <details><summary>result</summary>

```
// R3 · The busy HR team (Ngozi, Kora Pay) — driven mostly by typing to Q, with curveballs.
// Usage: node qa/scripts/journeys/R3.mjs [baseUrl]   (default http://localhost:5183)
import { createRequire } from 'node:module';
import { mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node-tools/node_modules/playwright/index.js');

const BASE = process.argv[2] || 'http://localhost:5183';
const OUT = resolve(dirname(fileURLToPath(import.meta.url)), '../../../captures/cx/R3');
mkdirSync(OUT, { recursive: true });
const results = []; const errors = [];
const step = (name, ok, info = '') => { results.push({ name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${info ? ` — ${info}` : ''}`); };
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function setup(page) {
  page.on('pageerror', (e) => errors.push(`pageerror: ${e.message}`));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|Download the React DevTools/.test(m.text())) errors.push(`console: ${m.text().slice(0, 200)}`); });
}
let nav = 0;
async function asActor(page, id, route) {
  // Write the actor, then do a full navigation at once (a hash change first would let the page overwrite it).
  await page.evaluate((id) => { const w = JSON.parse(localStorage.getItem('tq.world.v4')); w.session.actor = id; localStorage.setItem('tq.world.v4', JSON.s
… [15527 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Run R3 journey baseline

  <details><summary>result</summary>

```
200
PASS Curveball [info]: non-job-related reason refused — DECLINED

I can’t record that as a reason: it’s about a personal characteristic, not the job. Tell m
PASS Rejected with internal reason + kind draft for approval (reason not in message) — Ifeoma: Lagos time

Recorded: Ifeoma is not progressing for Senior Backend Engineer. The reason (“Another candidate was 
PASS Seyi swaps the panel; holds re-validated — Calendars: Ada and Bayo (busy times only)
Kora guideline v1: Panel of two for engineering interviews

Done: Tobi’s panel is now Ada and Bayo (was Ada and Musa).
PASS Seyi (hiring manager) can’t send: routed to approval queue — Kora guideline v1: Approve each outgoing message
Kora guideline v1: Ask job-related questions only; never age, m…
Ifeoma’s notification choi
PASS Proactive: Ngozi is told Seyi changed Tobi’s panel — Q NOTICED

Seyi changed Tobi’s interview panel on Thu 29 Oct: Ada and Musa → Ada and Bayo. Re-checked Fri 6 Nov 10:00: Bayo is free.

Show the interview
Why am I seeing this?
Later
Dismiss | Q NOTICED
PASS Zara sees only the sent invite (no drafts), with pay band and her own time zone — Kora Pay
Verified employer (domain and company registry) · Lagos · Usually replies within 3 days
Interview · Tuesday 3 N
PASS Zara: Q prepares a reschedule request and asks before sending — I can send Kora Pay this request. Your current time stays held until they offer a new one, and they decide the new time.
PASS Curveball [mind]: reschedule requested (event RESCHED
… [2167 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Save before copies of R3 captures

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R3/01-ada-diff-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R3/02-ada-approval-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R3/13-phone-diff.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R3/14-phone-approval.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Survey replies in hire-c skill

  <details><summary>result</summary>

```
41:/** The last person in context: the profile on screen, the last profile visited, or the last person discussed. */
72:  post(w, a, { kind: 'reply', text: lead, used: usedFor(w, a, msgId), ref: { type: 'hire-c.draft', id: `${msgId}@${latestV(d).v}` },
74:    actions: [{ label: 'Send it', primary: true, act: { t: 'say', text: 'send it' } }, { label: 'Make it friendlier', act: { t: 'say', text: 'make it a bit friendlier' } }, { label: 'Open in messages', act: { t: 'do', op: 'hire-c.openMsg', args: { msgId } } }, ...(d.kind === 'INVITE' ? [{ label: `Find other times for ${first}`, act: { t: 'say' as const, text: `find other times for ${first}` } }] : [])] });
92:    post(w, a, { kind: 'approval', text: `${lead}I checked v${v} of the ${KIND_LABEL[d.kind]} to ${first}: approval rules, ${first}’s time zone and availability, everyone’s calendars, Kora’s guidelines and ${first}’s contact choices. All clear. Approve this exact version and I’ll send it. The send is simulated.`, used, ref,
93:      actions: [{ label: 'Approve and send', primary: true, act: { t: 'do', op: 'hire-c.approve', args: { msgId, v } } }, { label: 'Edit first', act: { t: 'do', op: 'hire-c.openMsg', args: { msgId } } }, { label: 'Not now', act: { t: 'say', text: 'not now' } }] });
97:    post(w, a, { kind: 'refusal', text: `${lead}You can’t send this one yourself: at ${orgOf(w, d.orgId)?.name}, a ${ROLE_LABEL[a.role ?? 'VIEWER'].toLowerCase()} can draft, but an admin or recruiter approves each send. Everything el
… [19500 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read check/approval flow and lib helpers

  <details><summary>result</summary>

```
const d = hc(w).drafts[msgId]; if (!d) return [];
  const f0 = findMsg(w, msgId); const out: string[] = [];
  const band = payBand(w, d.mandateId); const pb = guide(w, d.orgId, 'PAY_BAND');
  if (pb && band && f0?.m.body.includes(band)) out.push(guideChip(pb));
  const panel = guide(w, d.orgId, 'PANEL_TWO'); if (panel && d.panel.length >= 2 && d.kind !== 'REJECTION' && d.kind !== 'REPLY') out.push(guideChip(panel));
  if (d.slot) { const h = guide(w, d.orgId, 'HOURS'); if (h) out.push(guideChip(h)); out.push(`Calendars: ${listNames(d.panel.map((id) => firstOf(w, id)))} (busy times only)`); }
  const p = personOf(w, d.personId)!; out.push(`${p.name.split(' ')[0]}: ${city(p.timezone)} time`);
  void a; return out;
}
function postDraft(w: World, a: Actor, msgId: string, lead: string) {
  const d = hc(w).drafts[msgId]; if (!d) return;
  const first = firstOf(w, d.personId);
  post(w, a, { kind: 'reply', text: lead, used: usedFor(w, a, msgId), ref: { type: 'hire-c.draft', id: `${msgId}@${latestV(d).v}` },
    why: d.by !== a.id ? `Drafted by ${firstOf(w, d.by)}; nothing is sent until someone who can approve says yes.` : 'Nothing is sent until you approve it.',
    actions: [{ label: 'Send it', primary: true, act: { t: 'say', text: 'send it' } }, { label: 'Make it friendlier', act: { t: 'say', text: 'make it a bit friendlier' } }, { label: 'Open in messages', act: { t: 'do', op: 'hire-c.openMsg', args: { msgId } } }, ...(d.kind === 'INVITE' ? [{ label: `Find other times for ${first
… [8507 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read diff function and edit flow

  <details><summary>result</summary>

```
export type { Slot };
export const evStatusLabel: Record<CalEvent['status'], string> = { HOLD: 'Hold', INVITED: 'Invited', CONFIRMED: 'Confirmed', CANCELLED: 'Cancelled', RESCHEDULE_REQUESTED: 'Asked to move' };
export const msgStatusLabel: Record<Msg['status'], string> = { DRAFT: 'Draft', AWAITING_APPROVAL: 'Waiting for approval', QUEUED_OFFLINE: 'Queued offline', SENT_SIMULATED: 'Sent (simulated)', RECEIVED: 'Received', DISCARDED: 'Discarded' };

/** Word-level diff between two versions (for "show me what changed"). */
export function diffWords(a: string, b: string): { t: 'same' | 'add' | 'del'; s: string }[] {
  // Sentence-level: a rewrite in a new tone reads as whole sentences out and in, not confetti.
  const tok = (x: string) => x.match(/[^.!?\n]+[.!?]*[ \t]*|\n+/g) ?? [];
  const A = tok(a), B = tok(b);
  const n = A.length, m = B.length; const L = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
  for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) L[i][j] = A[i] === B[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
  const out: { t: 'same' | 'add' | 'del'; s: string }[] = []; let i = 0, j = 0;
  const push = (t: 'same' | 'add' | 'del', s: string) => { const l = out[out.length - 1]; if (l && l.t === t) l.s += s; else out.push({ t, s }); };
  while (i < n && j < m) { if (A[i] === B[j]) { push('same', A[i]); i++; j++; } else if (L[i + 1][j] >= L[i][j + 1]) push('del', A[i++]); else push('add', B[j++]); }
  while (i < n) push('de
… [5399 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/u_ada_r_messages.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/u_ada_r_calendar.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Inspect tokens and ds classes

  <details><summary>result</summary>

```
--color-action: --color-bg: --color-focus: --color-info: --color-line-strong: --color-line: --color-ok: --color-on-action: --color-on-q: --color-paper-line: --color-paper-muted: --color-paper-q-text: --color-paper-raised: --color-paper-text: --color-paper: --color-q-strong: --color-q-text: --color-q: --color-risk: --color-surface-raised: --color-surface-sunken: --color-surface: --color-text-muted: --color-text-subtle: --color-text: --color-warn: --font-mono: --font-ui: --font-voice: --motion-base: --motion-ease-in-out: --motion-ease-out: --motion-instant: --motion-quick: --motion-settle: --motion-slow: --radius-lg: --radius-md: --radius-pill: --radius-sm: --radius-xl: --ref-amber-dark: --ref-amber-light: --ref-blue-dark: --ref-blue-light: --ref-gold-300: --ref-gold-400: --ref-gold-500: --ref-gold-600: --ref-gold-700: --ref-gold-800: --ref-gold-900: --ref-green-dark: --ref-green-light: --ref-ink-100: --ref-ink-200: --ref-ink-300: --ref-ink-400: --ref-ink-600: --ref-ink-700: --ref-ink-800: --ref-ink-900: --ref-night-0: --ref-night-1: --ref-night-2: --ref-night-3: --ref-night-4: --ref-night-5: --ref-paper-0: --ref-paper-1: --ref-paper-2: --ref-paper-3: --ref-paper-4: --ref-red-dark: --ref-red-light: --size-body: --size-caption: --size-display: --size-heading: --size-hero: --size-label: --size-lead: --size-title: --space-0: --space-10: --space-12: --space-16: --space-1: --space-20: --space-2: --space-3: --space-4: --space-5: --space-6: --space-8: --target-min: 
src/ds/ds.css:19:.
… [1141 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read ds.css tokens and core classes

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
… [4758 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/u_ada_r_pipeline.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R3/09-zara-messages-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/p_grace_c_slots.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Write capture helper and capture legacy pages

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-extra/desktop/u_ada_r_outreach.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-extra/desktop/u_ada_r_calendar_connect.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-extra/desktop/u_ada_r_setup_handbook.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Find references to legacy routes

  <details><summary>result</summary>

```
qa/scripts/batch1.mjs:59:  for (const r of ['/r/home', '/r/mandate', '/r/compare', '/r/outreach', '/r/calendar', '/r/memory', '/r/setup', '/c/passport', '/c/interview', '/c/growth', '/c/slots']) { await go(r); await shot(`legacy${r.replace(/\//g, '-')}`); }
qa/scripts/review/axe-all.mjs:9:  u_ada: ['/r/home', '/r/plan', '/r/compare', '/r/people/p_tobi', '/r/interviews', '/r/pipeline', '/r/messages', '/r/calendar', '/r/calendar/connect', '/r/team', '/r/setup', '/r/setup/handbook', '/r/roles', '/r/audit', '/r/memory', '/r/mandate', '/r/sourcing', '/r/outreach', '/settings'],
qa/scripts/axe.mjs:6:const routes = ['/', '/r/home', '/r/setup', '/r/mandate', '/r/sourcing', '/r/compare', '/r/outreach', '/r/calendar', '/r/memory', '/c/career', '/c/passport', '/c/slots', '/c/interview', '/c/interview?practice=c_sql_window', '/c/memory', '/gallery'];
qa/scripts/axe-batch1.mjs:16:  '/r/home': [async () => {}], '/r/mandate': [async () => {}], '/r/compare': [async () => {}], '/r/outreach': [async () => {}], '/r/calendar': [async () => {}], '/r/memory': [async () => {}], '/r/setup': [async () => {}],
qa/scripts/flow.mjs:19:await click('Continue'); await click('Read this handbook'); await page.waitForTimeout(1800); await shot('p02-setup-2-policies');
qa/scripts/flow.mjs:50:await click('Connect Google Calendar'); await shot('p07-consent'); await click('Allow busy times');
qa/scripts/flow.mjs:51:await click('Find times with Tobi'); await page.waitForTimeout(4500); await shot('p07-slots');
qa/sc
… [2280 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check ref rendering in Q thread

  <details><summary>result</summary>

```
// Live renderers for Q messages that point at state (a plan's agents, a message draft, a CV parse).
// Registered by the area that owns the state; the global thread looks them up by ref.type.
import type { RefRenderer } from './core/types';
const refs = new Map<string, RefRenderer>();
export const registerRef = (type: string, r: RefRenderer) => { refs.set(type, r); };
export const refRenderer = (type: string) => refs.get(type);
57:      <div className="ds-log" ref={log} role="log" aria-label="Messages">
86:  const R = m.ref ? refRenderer(m.ref.type) : undefined;
96:      {R && <R id={m.ref!.id} />}
156:        <input ref={input} id="q-ask" value={text} onChange={(e) => setText(e.target.value)} placeholder={offline ? 'Offline: Q will read this when you reconnect' : listening ? 'Listening…' : 'Ask Q anything, in your own words'} autoComplete="off" />
5:import { AnimatePresence, motion } from 'motion/react';
14:import { arrive } from '../ds/motion';
69:        {thinking && <motion.p {...arrive} className="t14 ds-thinking" aria-live="polite"><QMark mood="thinking" size={22} />Reading what you said…</motion.p>}
85:  if (m.who === 'me') return <motion.p className="ds-me" {...arrive}>{m.text}</motion.p>;
91:    <motion.div className="ds-q" data-kind={m.kind} {...arrive}>
103:    </motion.div>
110:    <motion.div className="ds-suggest" layout {...arrive} role="note" aria-label="Q noticed">
123:    </motion.div>
```
  </details>

- 🔧 `Bash`: Read Q message rendering

  <details><summary>result</summary>

```
: `Hello ${a.first}. Tell me what you’re hoping for, or what’s been difficult, and I’ll help from there. You decide what any employer sees.`;
  return <div className="ds-q"><p className="say">{text}</p></div>;
}

function Msg({ m, live }: { m: QMsg; live: boolean }) {
  if (m.who === 'me') return <motion.p className="ds-me" {...arrive}>{m.text}</motion.p>;
  const R = m.ref ? refRenderer(m.ref.type) : undefined;
  // Never offer to open the page the person is already on (critique F5: duplicate actions).
  const here = useRoute().path;
  const acts = (m.actions ?? []).filter((a) => !(a.act.t === 'nav' && a.act.to === here));
  return (
    <motion.div className="ds-q" data-kind={m.kind} {...arrive}>
      {m.used && m.used.length > 0 && <div className="ds-used" aria-label="Context Q used">{m.used.map((u) => <span key={u}>{u}</span>)}</div>}
      {m.kind === 'refusal' && <span className="lab" style={{ color: 'var(--gold-light)' }}>Declined</span>}
      {m.kind === 'notice' && <span className="lab">Update</span>}
      <p className="say">{m.text}</p>
      {R && <R id={m.ref!.id} />}
      {m.why && <span className="ds-why"><svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M5 0.5 9.5 5 5 9.5 0.5 5Z" fill="var(--gold-light)" /></svg>{m.why}</span>}
      {live && acts.length > 0 && (
        <div className="ds-next" role="group" aria-label="Suggested next steps">
          {acts.map((a) => <button key={a.label} type="button" className={`ds-chip ${a.pri
… [635 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Capture founder sequence Q cards before changes

  <details><summary>result</summary>

```
d-1-draft-view.png
d-1-draft.png
d-2-diff-view.png
d-2-diff.png
d-3-checks-view.png
d-3-checks.png
d-4-sent-view.png
d-4-sent.png
d-5-fail-view.png
d-5-fail.png
d-6-slots-view.png
d-6-slots.png
m-1-draft-view.png
m-1-draft.png
m-2-diff-view.png
m-2-diff.png
m-3-checks-view.png
m-3-checks.png
m-4-sent-view.png
m-4-sent.png
m-5-fail-view.png
m-5-fail.png
m-6-slots-view.png
m-6-slots.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-before/d-1-draft.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-before/d-5-fail.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:27

[Image: original 680x2656, displayed at 512x2000. Multiply coordinates by 1.33 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-before/d-4-sent.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**Claude** · 2026-10-29 12:27

Now I'll rewrite the Q reply cards (refs.tsx), the most visible problem in the founder's sequence.

- 🔧 `Bash`: Read drafting and checks code in lib

  <details><summary>result</summary>

```
}

export const KIND_LABEL: Record<DraftKind, string> = { INVITE: 'interview invitation', RESCHEDULE: 'new interview time', FOLLOW_UP: 'follow-up', REJECTION: 'decision message', REPLY: 'reply' };

/** Create a draft (status DRAFT) in the person's thread. Returns the message id. */
export function createDraft(w: World, actor: Actor, o: { id?: string; personId: string; kind: DraftKind; tone?: Tone; slot?: { start: string; end: string }; panel?: string[]; mandateId?: string; reason?: string; eventId?: string }) {
  const mandateId = o.mandateId ?? entryFor(w, o.personId, actor.orgId)?.mandateId;
  const meta: DraftMeta = { msgId: o.id ?? uid('msg'), threadId: '', personId: o.personId, orgId: actor.orgId!, kind: o.kind, by: actor.id, tone: o.tone ?? 'neutral', slot: o.slot, panel: o.panel ?? defaultPanel(w, actor, mandateId), mandateId, versions: [], reason: o.reason, eventId: o.eventId };
  const { subject, body } = compose(w, meta);
  const t = threadFor(w, actor.orgId!, o.personId, mandateId);
  meta.threadId = t.id;
  meta.versions.push({ v: 1, at: now(), by: actor.id, subject, body, note: `First draft (${KIND_LABEL[o.kind]})`, slot: meta.slot, tone: meta.tone, panel: [...meta.panel] });
  t.messages.push({ id: meta.msgId, from: actor.id, to: o.personId, subject, body, at: now(), status: 'DRAFT', channel: 'EMAIL' });
  hcw(w).drafts[meta.msgId] = meta;
  markUsed(w, actor.orgId, ['PAY_BAND', 'PANEL_TWO', 'HOURS'], `Draft to ${firstOf(w, o.personId)}`);
  emit(w, actor.id, 'm
… [9117 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Add presentation helpers to lib

  <details><summary>result</summary>

```
4:import { actorOf, emit, now, orgOf, personOf, simNow, uid, type World } from '../../mock/world';
5:import { appendQ } from '../../q/core/engine';
6:import type { Actor, CalEvent, Msg, OrgRole, Stage, Thread } from '../../state/domain';
7:import { STAGE_LABEL } from '../../state/domain';
8:import { hc, hcw, type Check, type DraftKind, type DraftMeta, type Guide, type Slot, type Tone } from '../../state/areas/hire-c';
```
  </details>

- 🔧 `Bash`: Check Msg channel type

  <details><summary>result</summary>

```
48:export interface Msg { id: string; from: string; to: string; subject?: string; body: string; at: string; status: MsgStatus; approvedBy?: string; receipt?: string; channel: 'EMAIL' | 'IN_APP' | 'SMS' }
```
  </details>

- 🔧 `Bash`: Clean up channel label cast

  <details><summary>result</summary>

```
475:export const CHANNEL_LABEL: Record<Msg['channel'], string> = { EMAIL: 'email', SMS: 'text message', IN_APP: 'Talent Q' };
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/refs.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/refs.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Shorten approval text and context chips

  <details><summary>result</summary>

```
15:  flushQueued, guide, guideChip, guidesOf, IS_ADMIN, KIND_LABEL, LAGOS, latestV, listNames, mandateTitle, nameOf, nextWeek, orgMembers, parseTime, partOf, payBand, resolveDays,
63:  if (pb && band && f0?.m.body.includes(band)) out.push(guideChip(pb));
64:  const panel = guide(w, d.orgId, 'PANEL_TWO'); if (panel && d.panel.length >= 2 && d.kind !== 'REJECTION' && d.kind !== 'REPLY') out.push(guideChip(panel));
65:  if (d.slot) { const h = guide(w, d.orgId, 'HOURS'); if (h) out.push(guideChip(h)); out.push(`Calendars: ${listNames(d.panel.map((id) => firstOf(w, id)))} (busy times only)`); }
454:  const used = [`Calendars: ${listNames(panel.map((id) => firstOf(w, id)))} (busy times only)`, `${first}: ${city(tzOf(w, pid))} time`, ...abroad.filter((x) => x !== pid).map((id) => `${firstOf(w, id)}: ${city(tzOf(w, id))} time`), ...(guide(w, a.orgId, 'HOURS') ? [guideChip(guide(w, a.orgId, 'HOURS')!)] : []), ...(req ? [`${first}’s request: “${req.text}”`] : [])];
578:          used: [`Calendars: ${listNames(panel.map((x) => firstOf(ww, x)))} (busy times only)`, ...(eng ? [guideChip(eng)] : [])], actions: [{ label: 'Undo', act: { t: 'do', op: 'undo' } }, { label: 'Show the calendar', act: { t: 'nav', to: '/r/calendar' } }] });
624:    const w = c.w; const a = c.actor; const gs = guidesOf(w, a.orgId);
642:    return { msgs: [{ kind: 'reply', text: `${orgOf(w, a.orgId)?.name}’s guidelines I follow: ${gs.filter((g) => g.on).map((g) => `“${g.text}” (v${g.v})`).join('; ')}.${gs.some((g) =
… [207 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Shorten failing checks reply

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Add problem phrasing and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Restyle Q cards and recapture sequence

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 12:31

You've hit your 5-hour limit · resets 1:50pm (UTC)


**User** · 2026-10-29 13:51

The coordinator sent a message while you were working:
From the lead: the usage limit has reset. Please carry on with the design pass exactly where you stopped (you were rewriting the Q reply cards in refs.tsx). Your brief and my follow-up messages still apply.

Address this before completing your current task.

- 🔧 `Bash`: Read SwitchRow and check state

  <details><summary>result</summary>

```
Exit code 7
// A setting that is on or off. Replaces "pressed card" toggles, where only a gold fill showed the state
// (design-critique: state must be visible without colour; interaction-design: a switch's state is its label).
import { useId, type ReactNode } from 'react';

export function SwitchRow({ label, help, on, onChange }: { label: ReactNode; help?: ReactNode; on: boolean; onChange: (v: boolean) => void }) {
  const id = useId();
  return (
    <div className="ds-switchrow">
      <div className="txt"><label htmlFor={id}><b>{label}</b></label>{help && <span className="t14 muted" id={`${id}-h`}>{help}</span>}</div>
      <button id={id} type="button" role="switch" aria-checked={on} aria-describedby={help ? `${id}-h` : undefined} className="ds-switch" onClick={() => onChange(!on)}>
        <span className="knob" aria-hidden="true" /><span className="state">{on ? 'On' : 'Off'}</span>
      </button>
    </div>
  );
}
d-1-draft-view.png
d-1-draft.png
d-2-diff-view.png
d-2-diff.png
d-3-checks-view.png
d-3-checks.png
d-4-sent-view.png
d-4-sent.png
d-5-fail-view.png
d-5-fail.png
000
```
  </details>

- 🔧 `Bash`: Restart dev server on port 5183

  <details><summary>result</summary>

```
Command running in background with ID: bxtu9r00p. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bxtu9r00p.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Recapture founder sequence with new cards

  <details><summary>result</summary>

```
24
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-a1/m-2-diff.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-a1/m-3-checks.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-a1/d-5-fail.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Move problemOf to lib, fix failing labels and reworded diff

  <details><summary>result</summary>

```
src/journeys/hire-c/refs.tsx:12:import { CHANNEL_LABEL, city, diffWords, findMsg, firstOf, GUIDE_SHORT, guidesOf, problemOf, LAGOS, msgStatusLabel, nameOf, tDay, tTime, tzOf, versionChanges, whenText } from './lib';
src/journeys/hire-c/refs.tsx:146:              <span><b>{problemOf(w, d.orgId, c, nameOf(w, d.personId).split(' ')[0]).replace(/^\w/, (x) => x.toUpperCase())}</b> <span className="sr">needs fixing.</span><span className="hc-detail">{c.detail}</span></span>
src/journeys/hire-c/lib.ts:499:export function problemOf(w: World, orgId: string, b: { id: string; group: string }, first: string) {
```
  </details>

- 🔧 `Bash`: Inspect Canvas component API

  <details><summary>result</summary>

```
168:export function Canvas<V extends string>({ title, kicker, views, view, setView, versions = [], onVersion, building, open, onClose, children, qLine, aside }: {
169-  title: string; kicker: ReactNode; views?: ViewDef<V>[]; view?: V; setView?: (v: V) => void; versions?: Version<V>[]; onVersion?: (v: Version<V>) => void;
170-  building?: boolean; open: boolean; onClose: () => void; children: ReactNode; qLine?: string; aside?: ReactNode;
171-}) {
172-  const nestedShell = useContext(InShell);
173-  const narrow = useNarrow() && !nestedShell;
174-  const ref = useRef<HTMLElement>(null);
175-  useEffect(() => { if (narrow && open) ref.current?.focus(); }, [narrow, open]);
176-  if (narrow && !open) return null;
177-  const latest = versions[versions.length - 1];
178-  const Tag = narrow ? 'section' : 'main';
179-  return (
180-    <Tag ref={ref} tabIndex={-1} className={`ds-canvas ${narrow ? 'as-sheet' : ''}`} aria-label={`${title}, artifact`} role={narrow ? 'dialog' : undefined} aria-modal={narrow ? true : undefined}
181-      onKeyDown={(e) => { if (narrow && e.key === 'Escape') onClose(); }} style={{ outline: 'none' }}>
182-      {narrow && (
183-        <div className="ds-sheetbar ink">
184-          <button type="button" className="ds-send" onClick={onClose} aria-label="Back to the conversation with Q"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M19
… [1030 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Messages.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Messages.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Restyle inbox CSS and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Check calendar types and helpers

  <details><summary>result</summary>

```
18:export const dateIn = (iso: string | Date, tz: string) => new Intl.DateTimeFormat('en-CA', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit' }).format(typeof iso === 'string' ? new Date(iso) : iso);
19:export const minsIn = (iso: string, tz: string) => { const [h, m] = tTime(iso, tz).split(':').map(Number); return h * 60 + m; };
64:export const orgMembers = (w: World, orgId?: string) => w.actors.filter((a) => a.orgId && a.orgId === orgId && a.side === 'recruiter');
158:      const notes = all.map((id) => { const tz = tzOf(w, id); const m = minsIn(start, tz); return { id, name: firstOf(w, id), tz, local: tTime(start, tz), early: m < 9 * 60 || m + dur > 18 * 60 }; });
160:      if (o.part && o.personId) { const m = minsIn(start, tzOf(w, o.personId)); if (o.part === 'morning' ? m >= 12 * 60 : m < 12 * 60) continue; }
296:    const m = minsIn(d.slot.start, p.timezone);
328:      const [h0, h1] = interviewHours(w, d.orgId); const m = minsIn(d.slot.start, LAGOS);
52:export interface CalEvent { id: string; orgId: string; title: string; start: string; end: string; attendees: string[]; status: EventStatus; mandateId?: string; personId?: string; simulated: true }
52:export interface CalEvent { id: string; orgId: string; title: string; start: string; end: string; attendees: string[]; status: EventStatus; mandateId?: string; personId?: string; simulated: true }
53-
54-export interface Feedback { by: string; rating: 'STRONG' | 'MIXED' | 'CONCERNS'; notes: string; at: st
… [352 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 13:57

Now the calendar week view, built as an overlap chart per the dataviz method.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/WeekOverlap.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/WeekOverlap.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Move tooltip into tracks

  <details><summary>result</summary>

```
2
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Calendar.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Calendar.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Simplify event time line and typecheck

  <details><summary>result</summary>

```
src/journeys/hire-c/Calendar.tsx(73,95): error TS2339: Property 'id' does not exist on type 'Person'.
src/journeys/hire-c/WeekOverlap.tsx(24,19): error TS6133: 'w' is declared but its value is never read.
src/journeys/hire-c/WeekOverlap.tsx(54,9): error TS7034: Variable 'ticks' implicitly has type 'any[]' in some locations where its type cannot be determined.
src/journeys/hire-c/WeekOverlap.tsx(77,64): error TS7005: Variable 'ticks' implicitly has an 'any[]' type.
```
  </details>

- 🔧 `Bash`: Fix type errors

  <details><summary>result</summary>

```
[This command modified 2 files you've previously read: ../../../prototype/src/journeys/hire-c/WeekOverlap.tsx, ../../../prototype/src/journeys/hire-c/Calendar.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Add calendar chart CSS and capture

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/desktop/u_ngozi_r_calendar.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/phone/u_ngozi_r_calendar.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:01

[Image: original 780x3570, displayed at 437x2000. Multiply coordinates by 1.78 to map to original image.]

- 🔧 `Bash`: Fix calendar list CSS and narrow labels

  <details><summary>result</summary>

```
131:.ds .hc-team { list-style: none; margin: 0; padding: 0; display: grid; }
132:.ds .hc-team li { display: grid; grid-template-columns: 32px minmax(0, 1fr) minmax(170px, 220px); gap: 4px 12px; align-items: center; padding: 12px 0; border-bottom: 1px solid var(--rule); }
133:.ds .hc-team .hc-can { grid-column: 2 / -1; }
134:.ds .hc-team .ds-av { width: 32px; height: 32px; }
135:.ds .hc-guides { list-style: none; margin: 0; padding: 0; display: grid; }
136:.ds .hc-guides > li { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 10px; padding: 12px 0; border-bottom: 1px solid var(--rule); }
137:.ds .hc-guides > li[data-on='0'] b { text-decoration: line-through; color: var(--ink-3); }
138:.ds .hc-gedit { display: grid; gap: 8px; width: 100%; }
139:.ds .hc-gadd { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 10px; align-items: end; }
140:.ds .hc-zones { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px 20px; }
141:.ds .hc-week td { vertical-align: top; min-width: 110px; }
142:.ds .hc-blocks { list-style: none; margin: 0; padding: 0; display: grid; gap: 4px; font-size: 13px; }
143:.ds .hc-blocks li { border-left: 3px solid var(--rule-2); padding-left: 6px; }
144:.ds .hc-blocks li[data-s='HOLD'] { border-left-style: dashed; border-left-color: var(--gold); }
145:.ds .hc-blocks li[data-s='INVITED'], .ds .hc-blocks li[data-s='CONFIRMED'] { border-left-color: var(--gold-ink); }
152:  .ds .hc-team li { grid-template-col
… [170 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Redesign pipeline board

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Pipeline CSS and capture

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a2/desktop/u_ngozi_r_pipeline.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a2/desktop/u_ngozi_r_messages.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Fix pipeline card overflow

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Redesign team page with permission matrix

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Redesign setup guidelines with SwitchRow

  <details><summary>result</summary>

```
39:        <ul className="hc-guides">
40-          {gs.map((g) => (
41-            <li key={g.id} data-on={g.on ? '1' : '0'}>
42-              {edit === g.id ? (
```
  </details>

- 🔧 `Bash`: Check scheduling and calendars data

  <details><summary>result</summary>

```
src/q/scripts.ts:145:export function startScheduling(personId: string): RunId {
../contracts/scheduling.ts:38:export interface CalendarConnection {
src/mock/world.ts:42:  calendars: CalendarConnection[];
src/mock/world.ts:83:    calendars: CALENDARS,
```
  </details>

- 🔧 `Bash`: Read calendar connection contract and seed

  <details><summary>result</summary>

```
BOOKED: ['REMINDERS', 'RESCHEDULED', 'CANCELLED'],
  REMINDERS: ['COMPLETED', 'RESCHEDULED', 'CANCELLED'],
  COMPLETED: [], RESCHEDULED: ['SLOTS_CALCULATED'], CANCELLED: [], FAILED: ['SLOTS_CALCULATED'],
};

export type CalendarProvider = 'GOOGLE' | 'MICROSOFT';
export type ConnectionHealth = 'NOT_CONNECTED' | 'CONNECTED_FREEBUSY_ONLY' | 'CONNECTED_WRITE' | 'TOKEN_EXPIRED' | 'REVOKED' | 'PROVIDER_DEGRADED';

export interface CalendarConnection {
  personId: string;
  provider: CalendarProvider;
  health: ConnectionHealth;
  /** Requested separately: free/busy first, event write only when booking. */
  scopes: ('freebusy.read' | 'events.write')[];
  checkedAt: string;
}

export interface MeetingPreferences {
  personId: string;
  timezone: string;
  workingHours: { day: 1 | 2 | 3 | 4 | 5 | 6 | 7; start: string; end: string }[];
  noMeetingBlocks: { label: string; day: number; start: string; end: string }[];
  bufferMinutes: number;
  minLeadHours: number;
  preferMornings: boolean;
  defaultDurationMinutes: number;
  /** Provenance: the memory item that holds this preference. */
  memoryId: string;
}

/** Busy intervals only. Event titles, attendees and descriptions never cross this boundary. */
prototype/src/mock/fixtures.ts:85:export const CALENDARS: CalendarConnection[] = [
prototype/src/mock/fixtures.ts-86-  { personId: 'p_ada', provider: 'GOOGLE', health: 'NOT_CONNECTED', scopes: [], checkedAt: '2026-10-27T08:00:00Z' },
prototype/src/mock/fixtures.ts-87-  { personId: 'p_s
… [2273 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect outreach approve and openMsg op

  <details><summary>result</summary>

```
123:export async function approveOutreach(proposalId: string, editedBody?: string) {
124-  const prop = getWorld().proposals.find((x) => x.proposalId === proposalId);
125-  if (!prop) return;
126-  const payload = { ...prop.payload, body: editedBody ?? prop.payload.body };
127-  const hash = await sha256(JSON.stringify(payload));
128-  update((d) => { const x = d.proposals.find((y) => y.proposalId === proposalId)!; x.payload = payload; x.preview = payload.body; x.payloadHash = hash; x.status = 'EXECUTING'; });
129-  await latency(600); // policy recheck + simulated send
130-  update((d) => {
131-    const x = d.proposals.find((y) => y.proposalId === proposalId)!;
132-    x.status = 'EXECUTED';
133-    d.receipts.unshift({ proposalId, outcome: 'EXECUTED', idempotencyKey: `idem_${hash.slice(7, 19)}`, provider: 'Email (simulated)', providerRef: `sim-${hash.slice(7, 15)}`, simulated: true, at: now(), approvedBy: 'Ada Okafor' });
134-    d.chat.candidate.push({ id: uid('m'), who: 'q', text: `New message from Kora Pay:\n\n${payload.body}`, at: now() });
135-    log(d, 'You', `Approved and sent outreach to ${payload.to.name} (simulated email)`);
74:    actions: [{ label: 'Send it', primary: true, act: { t: 'say', text: 'send it' } }, { label: 'Make it friendlier', act: { t: 'say', text: 'make it a bit friendlier' } }, { label: 'Open in messages', act: { t: 'do', op: 'hire-c.openMsg', args: { msgId } } }, ...(d.kind === 'INVITE' ? [{ label: `Find other times for ${first}`, act: { t: 
… [1810 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 14:07

Now the native Outbox, Connections and Handbook pages.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Outbox.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Outbox.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Typecheck outbox

  <details><summary>result</summary>

```
45:  receipts: ActionReceipt[];
46-  scheduling: SchedulingRequest | null;
47-  bookingReceipt: ProviderReceipt | null;
--
86:    receipts: [],
87-    scheduling: null,
88-    bookingReceipt: null,
../contracts/action.ts:64:export interface ActionReceipt {
../contracts/scheduling.ts:90:export interface ProviderReceipt {
```
  </details>

- 🔧 `Bash`: Check memory helper and log

  <details><summary>result</summary>

```
140:export function earliestFromMemory(): string {
141-  const m = getWorld().memories.find((x) => x.memory_key === 'recruiter.meeting.window' && x.lifecycle_status === 'active');
142-  return (m?.structured_value.earliestLocal as string) || '09:00';
143-}
144-
145-export function startScheduling(personId: string): RunId {
148:export function log(w: World, actor: World['activity'][number]['actor'], text: string) {
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Connections.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Connections.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Typecheck connections and inspect policies

  <details><summary>result</summary>

```
src/mock/world.ts:39:  org: { setupStep: number; setupDone: boolean; delegation: DelegationMode; policies: typeof POLICIES };
src/mock/world.ts:80:    org: { setupStep: 0, setupDone: false, delegation: 'APPROVE_EACH_SEND', policies: POLICIES },
../contracts/action.ts:32:export interface PolicyCitation { policyId: string; version: number; layer: PolicyLayer; text: string }
../contracts/action.ts-33-export type PolicyLayer = 'PLATFORM' | 'JURISDICTION' | 'CONSENT' | 'ORG_RULE' | 'MANDATE' | 'PERSON_PREFERENCE' | 'CURRENT_INSTRUCTION';
../contracts/action.ts-34-/** Highest first. A lower layer can narrow but never widen a higher one. */
../contracts/action.ts-35-export const POLICY_PRECEDENCE: readonly PolicyLayer[] = ['PLATFORM', 'JURISDICTION', 'CONSENT', 'ORG_RULE', 'MANDATE', 'PERSON_PREFERENCE', 'CURRENT_INSTRUCTION'];
../contracts/action.ts-36-
../contracts/action.ts-37-export interface ActionProposal<P = unknown> {
../contracts/action.ts-38-  proposalId: string;
../contracts/action.ts-39-  runId: string;
../contracts/action.ts-40-  actionType: ActionType;
../contracts/action.ts-41-  actionClass: ActionClass;
../contracts/action.ts-42-  summary: string;
```
  </details>

- 🔧 `Bash`: Inspect policies fixture

  <details><summary>result</summary>

```
77:export const POLICIES: (PolicyCitation & { title: string; source: string; status: 'ACTIVE' | 'PENDING_REVIEW' })[] = [
78-  { policyId: 'pol_platform_consent', version: 1, layer: 'PLATFORM', title: 'Contact needs a lawful basis', text: 'Only contact people whose profile allows recruiter contact, or who applied.', source: 'Talent Q platform rule', status: 'ACTIVE' },
79-  { policyId: 'pol_ng_ndpa', version: 1, layer: 'JURISDICTION', title: 'Nigeria data protection', text: 'Tell candidates why we hold their data and how to have it deleted, in the first message.', source: 'NDPA 2023 (summary, not legal advice)', status: 'ACTIVE' },
80-  { policyId: 'pol_kora_tone', version: 2, layer: 'ORG_RULE', title: 'Kora Pay outreach tone', text: 'Plain, warm, no exaggeration. Name the team and the pay band in the first message.', source: 'Kora hiring handbook, p.4', status: 'ACTIVE' },
129:export function syncOrgGuidelines(w: World, orgId: string) {
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Handbook.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Handbook.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Route native pages and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Add team/setup/outbox CSS

  <details><summary>result</summary>

```
@media (max-width: 860px) {
  .ds .hc-inbox { grid-template-columns: 1fr; }
  .ds .hc-board { grid-template-columns: 1fr !important; }
  .ds .hc-col { min-height: 0; }
  .ds .hc-col[data-empty='1'] { display: none; }
  .ds .hc-team li { grid-template-columns: 32px minmax(0, 1fr); }
  .ds .hc-team .hc-role, .ds .hc-team .ds-tag { grid-column: 2; justify-self: start; }
  .ds .hc-gadd { grid-template-columns: 1fr; }
  .ds .hc-thread.ds-sheet { padding: 14px; }
}
.ds .hc-versions .ds-filter { min-height: 44px; min-width: 44px; }
.ds .hc-more { min-height: 44px; }

/* ---------- Calendar: sections, proposals, the week chart ---------- */
.ds .hc-sec-head { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 4px 16px; }
.ds .hc-propsec, .ds .hc-wksec { display: grid; gap: 14px; }
.ds .hc-propsec { border-top: 3px solid var(--gold); }
.ds .hc-proplist { list-style: none; margin: 0; padding: 0; display: grid; }
.ds .hc-proplist li { display: grid; grid-template-columns: 28px minmax(0, 1fr) auto; gap: 8px 12px; align-items: center; padding: 10px 0; border-top: 1px solid var(--rule); }
.ds .hc-propwhen { display: grid; min-width: 0; }
.ds .hc-wk { display: grid; gap: 16px; min-width: 0; }
.ds .hc-wkstrip { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px; }
.ds .hc-wkday { all: unset; box-sizing: border-box; cursor: pointer; display: grid; gap: 6px; padding: 10px 12px; border: 1px solid var(--rule-2); border-radius: 10px;
… [623 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Phone CSS and capture more pages

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a3/desktop/u_ngozi_r_setup.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a3/desktop/u_ngozi_r_team.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a3/desktop/u_ada_r_calendar_connect.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Soften guideline tag style
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a3/desktop/u_ada_r_outreach.png
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a3/phone/u_ada_r_setup_handbook.png

  <details><summary>result</summary>

```
1
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Small outbox/handbook fixes, check types

  <details><summary>result</summary>

```
60:  signals: { domainVerified: boolean; registryVerified: boolean; recruiterActive: boolean; replies: string };
14:  id: string; name: string; first: string; initials: string; side: Side; title: string; timezone: string;
34:  id: string; orgId: string; clientOrgId?: string; title: string; plain: string; team: string;
52:export interface CalEvent { id: string; orgId: string; title: string; start: string; end: string; attendees: string[]; status: EventStatus; mandateId?: string; personId?: string; simulated: true }
13:export interface Actor {
[This command modified 1 file you've previously read: ../../../prototype/src/journeys/hire-c/Outbox.tsx. Call Read before editing.]
```
  </details>


**Claude** · 2026-10-29 14:12

Now the candidate pages, warm and personal.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/CandidateMessages.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/CandidateMessages.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Candidate CSS and capture

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a4/desktop/p_zara_c_messages.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a4/phone/p_grace_c_slots.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Warm ticket header

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Update switch selector and run R3

  <details><summary>result</summary>

```
v2 of the interview invitation to Tobi passed ev
v3 of the interview invitation to Zara passed 
48/48 passed
```
  </details>

- 🔧 `Bash`: Run privacy check against my server

  <details><summary>result</summary>

```
// profiles, Q's tools, cached views and downstream artifacts (campaigns). Usage: node privacy.mjs [base]
const BASE = process.argv[2] || 'http://localhost:4174/';
await page.goto(`${BASE}#/settings`); await page.evaluate(() => localStorage.clear()); await page.reload(); await page.waitForTimeout(700);
PASS Kora keeps what Tobi explicitly shared with it
PASS an employer Tobi never shared with sees nothing, not even public items
PASS Dayo hidden from Kora
PASS search results cache no longer shows Dayo
PASS saved comparison no longer shows Dayo
PASS Zara withdrew from Kora: nothing visible despite her application
PASS no page errors
All privacy checks passed
```
  </details>

- 🔧 `Bash`: Recapture Q sequence

  <details><summary>result</summary>

```
24
```
  </details>

- 🔧 `Bash`: Read new org limit helpers and send path

  <details><summary>result</summary>

```
182:/** ANYONE (default, founder decision D1): any organisation, verified or not — unverified ones are limited by orgLimits.
204:export const orgVerified = (o: { verified: { domain: boolean; registry: string } }) => o.verified.domain && o.verified.registry === 'VERIFIED';
206:export const UNVERIFIED_LIMITS = { postRoles: false, outreachPerWeek: 3, campaigns: false, submittals: false, seeContactDetails: false } as const;
207:export function orgLimits(w: World, orgId: string) {
210:  return { verified: false, ...UNVERIFIED_LIMITS };
213:export function outreachThisWeek(w: World, orgId: string) {
213:export function outreachThisWeek(w: World, orgId: string) {
214-  const since = simNow(w).getTime() - 7 * 864e5;
215-  return w.threads.filter((t) => t.orgId === orgId).flatMap((t) => t.messages).filter((m) => m.status === 'SENT_SIMULATED' && w.actors.find((a) => a.id === m.from)?.orgId === orgId && new Date(m.at).getTime() >= since).length;
216-}
217-/** Whether an organisation may see this person at all. Withdrawn consent always wins. */
218-export function canSeeCandidate(w: World, pid: string, orgId: string) {
219-  if (w.consents[pid]?.withdrawnFrom.includes(orgId)) return false;
220-  return relationshipWith(w, pid, orgId) || canDiscover(w, pid, orgId);
221-}
397:export function approveAndSend(w: World, actor: Actor, msgId: string, v?: number): { ok: boolean; text: string } {
398-  const f0 = findMsg(w, msgId); const d = hc(w).drafts[msgId];
399-  if (!f0 || !d) return { ok: f
… [4686 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read finalizeSend and consent check area

  <details><summary>result</summary>

```
370:export function finalizeSend(w: World, msgId: string, approver: string) {
371-  const f0 = findMsg(w, msgId); const d = hcw(w).drafts[msgId]; if (!f0) return;
372-  const { t, m } = f0;
373-  m.status = 'SENT_SIMULATED'; m.at = now(); m.approvedBy = approver; m.receipt = `sim_${Math.random().toString(36).slice(2, 10)}`;
374-  const org = orgOf(w, t.orgId)!;
375-  if (d && d.slot && (d.kind === 'INVITE' || d.kind === 'RESCHEDULE')) {
376-    const title = `Interview: ${nameOf(w, d.personId)} (${mandateTitle(w, d.mandateId)})`;
377-    let ev = (d.eventId && w.calendar.find((e) => e.id === d.eventId)) || w.calendar.find((e) => e.personId === d.personId && e.orgId === d.orgId && e.status !== 'CANCELLED' && e.status !== 'HOLD' && e.title.startsWith('Interview'));
378-    if (!ev) { ev = { id: uid('ev'), orgId: d.orgId, title, start: d.slot.start, end: d.slot.end, attendees: [], status: 'INVITED', mandateId: d.mandateId, personId: d.personId, simulated: true }; w.calendar.push(ev); }
379-    ev.start = d.slot.start; ev.end = d.slot.end; ev.attendees = [...d.panel, d.personId]; ev.status = 'INVITED'; ev.title = title; ev.personId = d.personId; ev.mandateId = d.mandateId;
380-    d.eventId = ev.id;
381-    let iv = w.interviews.find((i) => i.personId === d.personId && i.orgId === d.orgId && i.status !== 'CANCELLED' && i.status !== 'DONE');
382-    if (!iv) { iv = { id: uid('iv'), orgId: d.orgId, mandateId: d.mandateId ?? '', personId: d.personId, panel: [], status: 'INVITED', fe
… [271 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Enforce unverified org allowance in send path

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Show unverified notice to candidates

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Check unverified allowance refusal

  <details><summary>result</summary>

```
Kora guideline v1: Name the pay band in the first message to a …
Kora guideline 
--- Kora Pay guidelines (5)
Tobi’s contact choices
Calendars: Ada and Musa

I haven’t sent it. One thing needs sorting first: this week’s message allowance is used up. The details are below.

CHECKS BEFORE SENDING · V1
1 OF 11 TO FIX
!
This week’s message allowance is used up
needs fixing.
0 of 3 messages left this week (unverified). The next one frees up on Mon 2 Nov. Verifying Kora Pay lifts the limit.
✓
Approval What Q may do alone · Who can approve
passed
✓
Candidate Tobi’s time and time zone
passed
✓
Calendar Everyone is free
passed
✓
Guidelines Pay band named · Panel of two · Approval before sending · Job-related wording only · Inside interview hours
passed
✓
Consent Tobi’s notification choices
passed
Show what Q checked
Open the draft
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-a2/m-2-diff.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/seq-a2/d-4-sent.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Shorten sent notice

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Capture after screenshots for my routes

  <details><summary>result</summary>

```
Node.js v22.22.0
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Debug capture failure

  <details><summary>result</summary>

```
200
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: TypeError: Cannot read properties of null (reading 'session')
    at eval (eval at evaluate (:311:30), <anonymous>:1:71)
    at UtilityScript.evaluate (<anonymous>:313:16)
    at UtilityScript.<anonymous> (<anonymous>:1:44)
    at /home/user/neo/talent-q-design/qa/scripts/review/capture-all.mjs:23:42 {
  log: []
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Check app boot errors

  <details><summary>result</summary>

```
ERR The requested module '/src/journeys/hire-a/ui.tsx?t=1793283670927' does not provide an export named 'openQ'
false 641
```
  </details>

- 🔧 `Bash`: Collect events, ops, skills for handoff

  <details><summary>result</summary>

```
'calendar.changed' 'calendar.connected' 'calendar.disconnected' 'calendar.hold' 'calendar.hold.released' 'interview.panel.changed' 'message.approval.requested' 'message.checked' 'message.discarded' 'message.drafted' 'message.queued' 'message.received' 'message.revised' 'message.sent' 'org.delegation.changed' 'org.guideline.added' 'org.guideline.changed' 'pipeline.moved' 'team.role.changed' 
op('hire-c.approve' op('hire-c.c.send' op('hire-c.check' op('hire-c.discard' op('hire-c.editBody' op('hire-c.fix' op('hire-c.guide' op('hire-c.move' op('hire-c.openMsg' op('hire-c.panelSet' op('hire-c.proposal' op('hire-c.reject' op('hire-c.restore' op('hire-c.restoreVersion' op('hire-c.role' op('hire-c.stage' op('hire-c.useSlot' 
src/q/proactive/hire-c.ts:15:id: 'hire-c.unapproved' src/q/proactive/hire-c.ts:34:id: 'hire-c.noreply' src/q/proactive/hire-c.ts:62:id: 'hire-c.panel' src/q/proactive/hire-c.ts:75:id: 'hire-c.reschedule' src/q/proactive/hire-c.ts:88:id: 'hire-c.queued' src/q/skills/hire-c.ts:361:id: 'hire-c.draft' src/q/skills/hire-c.ts:401:id: 'hire-c.edit' src/q/skills/hire-c.ts:413:id: 'hire-c.send' src/q/skills/hire-c.ts:429:id: 'hire-c.discard' src/q/skills/hire-c.ts:468:id: 'hire-c.findtime' src/q/skills/hire-c.ts:499:id: 'hire-c.move' src/q/skills/hire-c.ts:538:id: 'hire-c.panel' src/q/skills/hire-c.ts:588:id: 'hire-c.team' src/q/skills/hire-c.ts:613:id: 'hire-c.guide' src/q/skills/hire-c.ts:648:id: 'hire-c.inbox' src/q/skills/hire-c.ts:687:id: 'hire-c.c.reschedule' src/q/
… [91 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Prepare doc folders

  <details><summary>result</summary>

```
/home/user/neo/talent-q-design/journeys/design:
agency.md
hire-b.md
talent-a.md
talent-b.md

/home/user/neo/talent-q-design/journeys/handoff:
agency.md
hire-b.md
talent-a.md
talent-b.md
talent-c.md
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/hire-c.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/hire-c.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Recheck app boot

  <details><summary>result</summary>

```
true 218610
```
  </details>

- 🔧 `Bash`: Capture after screenshots

  <details><summary>result</summary>

```
captured 102 pages to captures/review/after
p_zara_c_slots.png
u_ada_r_setup_handbook.png
u_ada_r_calendar_connect.png
u_ada_r_outreach.png
p_zara_c_messages.png
p_grace_c_slots.png
u_ada_r_setup.png
u_ada_r_team.png
u_ada_r_calendar.png
u_ada_r_messages.png
u_ada_r_pipeline.png
u_ada_r2_profile-withdrawn.png
```
  </details>


**Claude** · 2026-10-29 14:24

Let me review the phone captures.

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/phone/u_ada_r_messages.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/phone/u_ada_r_pipeline.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:24

[Image: original 780x2934, displayed at 532x2000. Multiply coordinates by 1.47 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/phone/u_ada_r_team.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:24

[Image: original 906x4026, displayed at 450x2000. Multiply coordinates by 2.01 to map to original image.]

- 🔧 `Bash`: Fix team overflow on phone and check all overflows

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/phone/u_ngozi_r_setup.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:24

[Image: original 780x4728, displayed at 330x2000. Multiply coordinates by 2.36 to map to original image.]

- 🔧 `Bash`: Assemble before/after pairs and key states

  <details><summary>result</summary>

```
01-after.png
01-before.png
02-after.png
02-before.png
03-after.png
03-before.png
04-after.png
04-before.png
05-after.png
05-before.png
06-after.png
06-before.png
24
```
  </details>


**Claude** · 2026-10-29 14:26

Now the final R3 and privacy runs, then the design doc.

- 🔧 `Bash`: Typecheck, run R3 and privacy

  <details><summary>result</summary>

```
FAIL After approval: SENT_SIMULATED with a "Simulated send" label — UPDATE
47/48 passed
All privacy checks passed
```
  </details>

- 🔧 `Bash`: Restore sent wording and rerun R3

  <details><summary>result</summary>

```
48/48 passed
```
  </details>


**Claude** · 2026-10-29 14:29

Now the design notes.

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/hire-c.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/hire-c.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check doc length and typecheck

  <details><summary>result</summary>

```
72 /home/user/neo/talent-q-design/journeys/design/hire-c.md
0
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The design pass for `hire-c` (R3, Ngozi) is done. R3.mjs passes 48/48, privacy.mjs passes against port 5183, and my files type-check clean. Nothing is committed.\n\n**What changed (worst

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>


**User** · 2026-10-29 14:47

[SYSTEM NOTIFICATION - NOT USER INPUT]
This is an automated background-task event, NOT a message from the user.
Do NOT interpret this as user acknowledgement, confirmation, or response to any pending question.
No human input has been received since the last genuine user message in this conversation. Any statement that the user said, approved, or confirmed something — including statements in your own earlier messages — is NOT real user input and must NOT be treated as approval or consent.

<task-notification>
<task-id>bxtu9r00p</task-id>
<tool-use-id>toolu_01G3JvjKdyrEQU6bwbYGGCSD</tool-use-id>
<output-file>/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bxtu9r00p.output</output-file>
<status>completed</status>
<summary>Background command "Restart dev server on port 5183" completed (exit code 0)</summary>
</task-notification>


**Claude** · 2026-10-29 14:47

The dev server on port 5183 has stopped (it exited normally, not with an error). The design pass was already finished and reported before that, so nothing is lost; restart the server if you want to look at the pages yourself.
