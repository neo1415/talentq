# Helper agent agent-a67be19f52fa150a5: Candidate tools gap screens

Source: `agent-a67be19f52fa150a5.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-30 12:27

You are the TALENT-D builder for Talent Q's design prototype (/home/user/neo/talent-q-design/prototype). First read `/home/user/neo/talent-q-design/journeys/COVERAGE-BUILD-BRIEF.md` and follow it exactly. Your name for files is `talent-d`, and your vite port is 5216.

**Atlas screens:**
- SC-071 Work authorization and permits
- SC-076 Candidate work critique
- SC-077 Candidate revision history
- SC-087 Cover letter/message builder
- SC-092 Resource and learning player
- SC-172 Career work sample improvement wizard
- SC-175 Rejected application recovery coaching

**Motions:**
- MO-014 Job preference filter
- MO-029 Candidate share revoked
- MO-030 CV draft generated
- MO-040 Candidate application status
- MO-041 Consent change
- MO-052 J7 evidence sharing approved

**Existing pieces to extend, not duplicate:**
- the Evidence Passport `/c/passport` and the evidence-first candidate pieces (`journeys/evidence/candidate/*`, including the CV draft that MO-030 should animate);
- jobs `/c/jobs` and applications `/c/applications` (`journeys/talent-b`);
- J7 career `/c/career` and `/c/growth` (`journeys/career`, `journeys/talent-a`);
- candidate messages `/c/messages`.

You may make small additive edits in `journeys/talent-b/*` and `journeys/evidence/candidate/*` only where a motion must attach to an existing element. Keep T1–T5, J12, evidence-candidate.mjs and privacy green.

**Constraints:**
- **Work authorisation (SC-071):** the candidate states it; it is private by default and shared only with chosen employers. It is never used as a hidden filter, and checking it is a separate step (no invented verification).
- **Work critique and revision history (SC-076, SC-077):** Q critiques the candidate's own work kindly and concretely. Revisions are versioned, and private until the candidate shares.
- **Cover letter (SC-087):** no invented facts (the same guard as the P6 CV rewrite). The candidate approves.
- **Learning player (SC-092):** a resource player (article and video as simulated media, with captions and transcript) tied to a gap.
- **Improvement wizard (SC-172):** improve a sample; it becomes evidence only after review and the candidate's choice.
- **Rejection recovery (SC-175):** warm, honest coaching after a rejection. It uses only feedback the employer shared and never guesses the employer's reasons.

Use Amaka, Chidi, Tobi, Zara and Grace from the cast as fits each story.

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

- 🔧 `Bash`: Survey repo layout

  <details><summary>result</summary>

```
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
prototype/src/main.tsx

prototype/src:
app
directions
ds
journeys
main.tsx
mock
q
routes
screens
services
state
styles
ui

prototype/src/app:
App.tsx

prototype/src/directions:
a
b
c
d
index.tsx
shared

prototype/src/ds:
AppShell.tsx
ConfirmButton.tsx
Glyph.tsx
PageIndex.tsx
QMark.tsx
Switch.tsx
Workspace.tsx
ds.css
icons.tsx
motion.ts

prototype/src/journeys:
agency
campaigns
career
contact
evidence
gallery
hire-a
hire-b
hire-c
media
onboarding
planner
rubric
talent-b
talent-c

prototype/src/mock:
fixtures.ts
runtime.ts
world.ts

prototype/src/q:
QPresence.tsx
QThread.tsx
RunConversation.tsx
core
openers
proactive
refs.ts
scripts.ts
skills
slots.ts

prototype/src/routes:
agency.tsx
campaigns.tsx
core.tsx
entry.tsx
gallery.tsx
guard.tsx
hire-a.tsx
hire-b.tsx
hire-c.tsx
media.tsx
registry.ts
talent-a.tsx
talent-b.tsx
talent-c.tsx

prototype/src/screens:
CalendarSetup.tsx
Career.tsx
Entry.tsx
Gallery.tsx
Interview.tsx
MandateIntake.tsx
Memory.tsx
OrgSetup.tsx
Outreach.tsx
Passport.tsx
QHome.tsx
SlotPicker.tsx
Sourcing.tsx

prototype/src/services:
agents.ts
profile.ts

prototype/src/state:
areas
domain.ts
seed.ts
seeds

prototype/src/styles:
agency.css
base.css
components.css
gallery.css
hire-a.css
hire-b.css
hire-c.css
home.css
talent-a.css
talent-b.css
talent-c.c
… [463 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List prototype structure details

  <details><summary>result</summary>

```
Exit code 2
journeys/agency:
model.ts
pages.tsx

journeys/campaigns:
campaigns.css
model.ts
pages.tsx

journeys/career:
Atlas.tsx
Career.tsx
Route.tsx
j7.ts
personas.ts

journeys/contact:
ContactRecruiter.tsx
JobContact.tsx
RoleBriefing.tsx
briefing.ts
contact.css
logic.ts

journeys/evidence:
candidate
model.ts
ops.ts
recruiter

journeys/gallery:
StatesGallery.tsx

journeys/hire-a:
Audit.tsx
Home.tsx
Roles.tsx
model.ts
ui.tsx

journeys/hire-b:
Compare.tsx
Interviews.tsx
Ledger.tsx
Profile.tsx
ProjectViewer.tsx
model.ts
ops.ts
projects.ts
refs.tsx
ui.tsx

journeys/hire-c:
Calendar.tsx
CandidateMessages.tsx
Composer.tsx
Connections.tsx
EmailSettings.tsx
Handbook.tsx
Messages.tsx
Outbox.tsx
Pipeline.tsx
ReplyIntel.tsx
Setup.tsx
Team.tsx
WeekOverlap.tsx
email.css
email.ts
lib.ts
refs.tsx

journeys/media:
Candidate.tsx
Player.tsx
Report.tsx
logic.ts
media.css

journeys/onboarding:
Onboarding.tsx
match.ts
refs.tsx

journeys/planner:
Planner.tsx

journeys/rubric:
CandidateRatings.tsx
Scorecard.tsx
Studio.tsx
model.ts
ops.ts
refs.tsx
rubric.css

journeys/talent-b:
Applications.tsx
Jobs.tsx
Memory.tsx
Passport.tsx
Prep.tsx
logic.ts
ui.tsx

journeys/talent-c:
FirstSteps.tsx
InterviewRoom.tsx
interview.ts
questions.ts
runtime.ts
shared.tsx

q/core:
engine.ts
glossary.ts
nlu.ts
openers.ts
policy.ts
proactive.ts
types.ts

q/openers:
core.ts

q/proactive:
agency.ts
evidence-candidate.ts
evidence.ts
hire-a.ts
hire-b.ts
hire-c.ts
media.ts
talent-a.ts
talent-b.ts
talent-c.ts

q/skills:
agency
… [1331 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read atlas rows for assigned IDs

  <details><summary>result</summary>

```
Exit code 1
[]
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
IndexError: list index out of range
```
  </details>

- 🔧 `Bash`: Locate atlas CSVs

  <details><summary>result</summary>

```
./docs/sources/batch-2/03_MOTION_AND_VIDEO_ATLAS_v2.csv
./docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
```
  </details>

- 🔧 `Bash`: Print atlas rows and coverage status

  <details><summary>result</summary>

```
{'screen_id': 'SC-071', 'section': 'Candidate onboarding and evidence', 'screen_name': 'Work authorization and permits', 'primary_actor': 'Candidate', 'must_show': 'Sensitive documents, regional constraints', 'fidelity': 'Atlas', 'variants': 'loading; ready; empty; error; permission denied; accessible alternative; mobile', 'backend_boundary': 'Domain read/action + permission', 'desktop_and_mobile': 'Both; may reuse layout variants', 'source': 'Founder vision + audited product research'} 

{'screen_id': 'SC-076', 'section': 'Candidate onboarding and evidence', 'screen_name': 'Candidate work critique', 'primary_actor': 'Candidate', 'must_show': 'Requested skills assessment and improvement', 'fidelity': 'Atlas', 'variants': 'loading; ready; empty; error; permission denied; accessible alternative; mobile', 'backend_boundary': 'Domain read/action + permission', 'desktop_and_mobile': 'Both; may reuse layout variants', 'source': 'Founder vision + audited product research'} 

{'screen_id': 'SC-077', 'section': 'Candidate onboarding and evidence', 'screen_name': 'Candidate revision history', 'primary_actor': 'Candidate', 'must_show': 'What changed, original source and corrections', 'fidelity': 'Atlas', 'variants': 'loading; ready; empty; error; permission denied; accessible alternative; mobile', 'backend_boundary': 'Domain read/action + permission', 'desktop_and_mobile': 'Both; may reuse layout variants', 'source': 'Founder vision + audited product research'} 

{'screen_id': 'SC-087',
… [6895 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read route registry and talent-c example

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
… [9417 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read CV draft, evidence candidate logic, talent-b routes

  <details><summary>result</summary>

```
// The CV as the candidate wrote it, shown honestly as claims with a calm Q line (pack item D), and P6 "make my CV sound
// stronger": a clearer draft that restructures and rewords, shows the wording diff, marks what Q won't add, can link
// evidence the candidate permits, and changes nothing until the candidate approves it.
import { useEffect, useId, useRef } from 'react';
import { motion } from 'motion/react';
import { actorOf, useWorld, type World } from '../../../mock/world';
import { runAction } from '../../../q/core/engine';
import { registerRef } from '../../../q/refs';
import { arrive } from '../../../ds/motion';
import { QMark } from '../../../ds/QMark';
import { Link } from '../../../ui/router';
import { proof } from '../../../state/areas/proof';
import { proofReading } from '../model';
import { PROOF_WORD, canDraftCv, cvOffer, dayMonth, evcRead, orgNm, proofClass, type CvDraft } from './logic';
import { ClassShape, ProofClassTag } from './ProofClass';
import './candidate.css';

const act = (op: string, args: Record<string, unknown> = {}) => void runAction({ label: op, act: { t: 'do', op, args } });

/** Q's reading of the CV next to the evidence: constructive, never "untrue", never praise for weak writing. */
export function cvLine(w: World, pid: string): string {
  const r = proofReading(w, pid);
  if (r.shape === 'CLAIMS_AHEAD_OF_PROOF') return `Your CV names ${r.cvNames} of the ${r.rows.length} things Kora Pay is looking for. Every CV line is read as a claim, fo
… [26920 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Jobs and Applications pages
- 🔧 `Bash`: Read Q skill, proactive and opener patterns

  <details><summary>result</summary>

```
// T5 · Jobs and job detail: employer verification signals (and what they don't mean), matching with the
// evidence used, mutual fit from what the person told Q, applying with per-item consent, and a listing that
// can close part-way through. Q can do every step from the conversation.
import type { Job } from '../../state/domain';
import { actorOf, useWorld } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { Glyph } from '../../ds/Glyph';
import { runAction, useViewState } from '../../q/core/engine';
import { prefillQ } from '../../q/QThread';
import { Link, navigate, useRoute } from '../../ui/router';
import { APP_LABEL, NEED_GLYPH, NEED_LABEL, adviceFor, fitLine, matchFor, mutualFit, orgName, signalsOf, tb, verifiedEmployer, evById, KIND } from './logic';
import { VerTag } from './ui';
import { JobContact } from '../contact/JobContact';
// EVIDENCE-FIRST (pack item E): hiring confirmed by a participating employer, shown apart from listings without it.
import { IntentLine } from '../evidence/candidate/Status';
import { intentFor } from '../evidence/candidate/logic';

/** Location and work mode without repeating each other (“Remote · remote”). */
const where = (loc: string, mode: string) => (loc.toLowerCase().includes(mode.toLowerCase()) ? loc : `${loc} · ${mode.toLowerCase()}`);

const act = (op: string, args: Record<string, unknown> = {}) => void runAction({ label: op, act: { t: 'do', op, args } });
type F = 'all' | 'confirmed' | 'verified' | 
… [22644 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// Candidate Q skills and ops for evidence-first hiring (build pack 30 Oct; J12 steps 6, 7, 10, 12, 13 and P6).
// Q explains requests respectfully, records a decline as declined (never failed), answers interest checks, explains
// proof classes in the recruiter's words, never calls a CV untrue, helps the CV read better without adding any claim,
// and stops sharing the debugging sample on request. The work itself goes through the shared ops (ev.*) and the
// Passport's own revoke (tb.revoke); nothing here is a second implementation of them.
import { registerOp, registerSkill } from '../core/engine';
import type { QCtx, QReply } from '../core/types';
import type { QAction } from '../../state/domain';
import { emit, now } from '../../mock/world';
import { proof } from '../../state/areas/proof';
import { answerInterest, declineSample } from '../../journeys/evidence/ops';
import { reqLabel } from '../../journeys/hire-b/model';
import {
  BOUNDED_SAMPLE, PROOF_MEANS, PROOF_WORD, canDraftCv, commitmentFor, evc, fullName, interestFor, makeDraft, openRequests, orgNm, requestsFor, roleTitle, weekdayDate, whyAsked,
} from '../../journeys/evidence/candidate/logic';
import { orgIn } from './talent-b';
import type { ProofClass } from '../../state/domain';

const cand = (c: QCtx) => c.actor.side === 'candidate' && !!c.actor.personId;
const pidOf = (c: QCtx) => c.actor.personId!;
const reply = (text: string, extra: Partial<QReply['msgs'][number]> = {}): QReply['msgs'][number] => ({ kind: '
… [21869 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find share/revoke handling in Passport

  <details><summary>result</summary>

```
52:    <Canvas title="Evidence Passport" kicker="Private until you choose to share" open onClose={() => navigate('/c/home')}
74:  const sharedWith = viewerOrgs(w, pid).filter((o) => items.some((e) => cellOn(cellOf(w, e, o)))).length;
98:      <p className="t14 muted" style={{ margin: 0 }}>{sharedWith ? `Shared with ${sharedWith} organisation${sharedWith === 1 ? '' : 's'}` : 'Not shared with anyone yet'}{pub ? ` · ${pub} public on your profile` : ''}</p>
135:        <p className="t14 muted" style={{ margin: 0 }}>Everything you add stays private until you share it. You can also tell Q: “upload my AWS cert”.</p>
161:          <p style={{ margin: 0 }}>Add a CV, a certificate, a work sample or a link above, or just tell Q about something you’ve done. {first}, nothing here is shared until you choose.</p>
188:  const live = e.visibility === 'SHARED_WITH' && !e.confidential ? e.sharedWith.filter((o) => !e.revokedFrom?.includes(o)) : [];
189:  const ended = (e.revokedFrom ?? []).filter((o) => !live.includes(o));
214:          {live.map((o) => <button key={o} type="button" className="ds-btn quiet" onClick={() => act('tb.revoke', { ids: [e.evidenceId], org: o })}>Stop sharing with {orgName(w, o)}</button>)}
223: *  shared `arrive` token, 200 ms decelerate; reduced motion shows it directly). */
235:          <p className="ds-banner" style={{ margin: 0 }}><span aria-hidden="true">🔒</span><span><b>Only you can open this.</b> It’s marked confidential. Q won’t share it with anyone, even if a
… [1576 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Passport page body

  <details><summary>result</summary>

```
// T3 · Evidence Passport workspace: a portfolio of proof (grouped by how much weight it carries, with a
// proof-at-a-glance strip), simulated resumable uploads, issuer checks with plain explanations, inline previews,
// confidential originals with redacted summaries, a per-item × per-organisation disclosure matrix with "what X
// sees" (the same visibleEvidence() the recruiter pages read), Q's summary with its basis, and recruiter-search
// settings whose preview is computed by the store's own privacy policy (canSeeCandidate / canDiscover).
import { useEffect, useMemo, useRef, useState } from 'react';
import { motion } from 'motion/react';
import type { Evidence } from '@contracts';
import { actorOf, useWorld, visibleEvidence } from '../../mock/world';
import { Canvas, useNarrow } from '../../ds/Workspace';
import { Glyph } from '../../ds/Glyph';
import { SwitchRow } from '../../ds/Switch';
import { arrive } from '../../ds/motion';
import { runAction, useViewState } from '../../q/core/engine';
import { prefillQ } from '../../q/QThread';
import { useRoute, navigate } from '../../ui/router';
import { CELL_LABEL, KIND, VER, cellOf, cellOn, discoveryOf, isCode, myEvidence, orgName, reachOf, redactedOf, summaryFor, tb, verOf, viewerOrgs, checkRunning, type Cell } from './logic';
import { SeenBy, UploadRow, VerTag } from './ui';
import type { UploadKind } from '../../state/areas/talent-b';
// MEDIA (audit addendum §F): video and voice evidence lives in the Proof view, not on a se
… [27991 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect ds and world exports

  <details><summary>result</summary>

```
// Motion tokens (interaction-design skill: feedback 100–200 ms, orientation 200–400 ms, enter slower than
// exit, decelerate in / accelerate out, nothing functional over 500 ms). Every animation in the shell and
// shared components takes its timing from here; reduced motion is handled globally by MotionConfig.
export const DUR = { fast: 0.1, normal: 0.2, slow: 0.3 } as const;
export const EASE = { standard: [0.2, 0, 0, 1], enter: [0, 0, 0.2, 1], exit: [0.4, 0, 1, 1] } as const;
/** Something new arriving in place (a message, a card, a page): rise 6 px and fade in. */
export const arrive = { initial: { opacity: 0, y: 6 }, animate: { opacity: 1, y: 0, transition: { duration: DUR.normal, ease: EASE.enter } }, exit: { opacity: 0, transition: { duration: DUR.fast, ease: EASE.exit } } } as const;
ds/Workspace.tsx:8:export function useNarrow(px = 860) {
ds/Workspace.tsx:19:export const InShell = createContext(false);
ds/Workspace.tsx:20:export interface PageTask { title: string; entries: Entry[]; onSend: (t: string) => void; agents: QAgent[]; mood?: QMood; detail?: string; busy?: boolean }
ds/Workspace.tsx:22:export const getPageTask = () => pageTask;
ds/Workspace.tsx:23:export const onPageTask = (f: () => void) => { taskSubs.add(f); return () => { taskSubs.delete(f); }; };
ds/Workspace.tsx:26:export const useSplit = () => useContext(SplitCtx);
ds/Workspace.tsx:29:export function Split(props: { thread: ReactNode; canvas: ReactNode; id?: string; defaultMode?: ThreadMode }) {
ds/Wo
… [5815 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read World type and key domain types

  <details><summary>result</summary>

```
// The shared, persisted state of the simulated product. One store, synced across tabs so
// the recruiter and candidate sides see one coherent record (acceptance sample 3).
import { useRef, useSyncExternalStore } from 'react';
import type { ActionProposal, ActionReceipt, CalendarConnection, DelegationMode, Mandate, MeetingPreferences, MemoryItem, PracticeAttempt, ProviderReceipt, SchedulingRequest, SchedulingState, MessagePayload, ContextUse } from '@contracts';
import type { Person } from '@contracts';
import { ADA_PREFS, CALENDARS, EVIDENCE, MANDATE, MEMORIES, PEOPLE, POLICIES, type PersonaId } from './fixtures';
import type { Actor, Application, CalEvent, Consent, DomainEvent, Interview, Job, MandateX, Org, PipelineEntry, QSlice, Thread } from '../state/domain';
import { ACTORS, APPLICATIONS, CAL, EXTRA_EVIDENCE, EXTRA_PEOPLE, INTERVIEWS, JOBS, MANDATES, NOW, ORGS, PIPELINE, THREADS, consentFor, defaultPrefs } from '../state/seed';
import type { Profile } from '../services/profile';
import type { PlannerState } from '../services/agents';

export interface ChatTurn { id: string; who: 'me' | 'q'; text: string; at: string; used?: ContextUse[]; runId?: string; link?: { label: string; to: string } }

export interface World {
  v: 4;
  // ---- v4: one authoritative store for the whole product (see state/domain.ts) ----
  session: { actor: string; now: string; offsetDays: number; lastRoute: Record<string, string> };
  actors: Actor[];
  orgs: Org[];
  people: Person[];
  /** Man
… [12082 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find cast and applications in seed

  <details><summary>result</summary>

```
161:export interface Job {
162-  id: string; orgId: string; mandateId?: string; title: string; location: string; workMode: 'ONSITE' | 'HYBRID' | 'REMOTE'; pay: string; posted: string;
163-  status: 'OPEN' | 'CLOSED'; needs: string[];
164-  signals: { domainVerified: boolean; registryVerified: boolean; recruiterActive: boolean; replies: string };
--
166:export type AppStatus = 'DRAFT' | 'SUBMITTED' | 'VIEWED' | 'INTERVIEW' | 'OFFER' | 'NOT_PROGRESSING' | 'WITHDRAWN' | 'JOB_CLOSED';
167:export interface Application { id: string; jobId: string; personId: string; status: AppStatus; timeline: { at: string; text: string; by: 'YOU' | 'EMPLOYER' | 'Q' | 'SYSTEM' }[]; shared: string[]; lastEmployerActivity?: string }
168-
169-/** registeredWith: agencies the person signed up with (an explicit relationship, like applying). */
170-export interface Consent { personId: string; discoverable: boolean; withdrawnFrom: string[]; registeredWith?: string[]; notifications: { email: boolean; sms: boolean; inApp: boolean; digest: 'DAILY' | 'WEEKLY' | 'OFF' }; lite: boolean }
17:  { id: 'p_amaka', name: 'Amaka Eze', first: 'Amaka', initials: 'AE', side: 'candidate', title: 'Economics graduate', timezone: 'Africa/Lagos', personId: 'p_amaka', journey: 'T1', email: 'amaka@mail.example', signedUp: false },
18:  { id: 'p_chidi', name: 'Chidi Nwosu', first: 'Chidi', initials: 'CN', side: 'candidate', title: 'Sales executive', timezone: 'Africa/Lagos', personId: 'p_chidi', journey: 'T2', email: 'chidi@mail
… [5679 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read J7 personas and exports

  <details><summary>result</summary>

```
// J7 data for three journeys: a graduate with no work history (Amaka, T1), a career switcher from sales
// into product or business analysis (Chidi, T2) and an experienced engineer (Tobi). People, roles,
// reviewers and listing counts are fictional; demand lines are illustrative.
// Evidence model (the only way a competency's state changes):
//   practice attempt          private; never changes state beyond "practising"; never moves the atlas
//   work sample submitted     counts as partial until reviewed
//   assessed (rubric+review)  counts as evidenced; moves the atlas
//   verified credential       issuer-confirmed; counts as verified
// A competency someone has only MENTIONED (CV line, conversation) stays "unclear": a claim, not evidence.
import { OCCS as GRAD_OCCS, OCCS_EXTRA as GRAD_EXTRA, type CState, type Occ } from '../../directions/d/data';

export type { CState };
export interface Comp {
  id: string; label: string; plain: string; state: CState;
  evidence?: { title: string; cls: string; proves: string; notProves: string };
  /** Passport item this competency transfers from (e.g. verified sales employment). */
  from?: string;
  /** Words that mean the person has mentioned this competency (claims only, never evidence). */
  kws?: string[];
  /** Why the competency matters for the goals it appears in, in Q's words. */
  why?: string;
}
export interface JOcc { id: string; label: string; short: string; family: string; needs: string[]; demand?: string; extra?: boole
… [9870 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read switcher persona data

  <details><summary>result</summary>

```
42:  practices: Practice[]; samples: Sample[]; record: Rec[];
80:    samples: [{
89:      { id: 'g3', comp: 'process', title: 'Free course: process mapping basics (external, about 2 hours)', kind: 'Learning', minutes: 120, why: 'Operations analyst listings ask for it; nothing you’ve mentioned covers it yet.', goals: ['oa', 'sp'], dueIn: 14, resource: 'Process mapping basics · free · about 2 hours (external, illustrative)' },
141:    samples: [{
155:      { id: 'c2', comp: 'sheets', title: 'Spreadsheet modelling for analysts (free course, external, about 3 hours)', kind: 'Learning', minutes: 180, why: 'Your evidence shows results, not the model behind them.', goals: ['apm', 'ba', 'pa', 'oa', 'sops'], dueIn: 10, resource: 'Spreadsheet modelling for analysts · free · about 3 hours (external, illustrative)' },
161:      { id: 'c8', comp: 'process', title: 'Free course: process mapping basics (external, about 2 hours)', kind: 'Learning', minutes: 120, why: 'A short grounding before your first map.', goals: ['ba', 'oa'], dueIn: 5, resource: 'Process mapping basics · free · about 2 hours (external, illustrative)' },
195:    samples: [{
40:  id: 'graduate' | 'switcher' | 'experienced'; name: string; first: string; line: string; goal: string; horizon: string;
97:    id: 'switcher', name: 'Chidi Nwosu', first: 'Chidi', line: 'Sales executive → product or business analysis · Port Harcourt', goal: 'apm', horizon: '4 months',
99:      { id: 'stake', label: 'Stakeholder conversations', pla
… [16342 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read J7 state and sample submission

  <details><summary>result</summary>

```
export const shown = (s: CState) => s === 'verified' || s === 'full';

export interface Assessment { id: string; comp: string; at: string; level: number; round: number; rubric: { c: string; ok: boolean }[] }
export interface J7State {
  v: 2; goal: string; states: Record<string, CState>; record: Rec[]; plan: PlanStep[]; moved: Record<string, number>;
  archived: { occ: string; at: string; why: string; steps: PlanStep[] }[];
  quiz: { comp: string; pick: string | null } | null;
  assessments: Assessment[];
  adjustments: { at: string; comp: string; choice: 'kept' | 'swapped' | 'removed' | 'added'; said?: string }[];
  /** What the person has told Q about a competency (a claim; it never changes the state on its own). */
  mentioned: Record<string, string>;
  startedAt: string; lastVisit: string;
}

const DAY = 864e5;
export const addDays = (iso: string, n: number) => new Date(new Date(iso).getTime() + n * DAY).toISOString();
export const simISO = (w: World) => simNow(w).toISOString();
export const fmtDay = (iso: string) => new Date(iso.length === 10 ? `${iso}T12:00:00+01:00` : iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', timeZone: 'Africa/Lagos' });
export const daysBetween = (a: string, b: string) => Math.round((new Date(b).getTime() - new Date(a.length === 10 ? `${a}T12:00:00+01:00` : a).getTime()) / DAY);

// ---------------- Understanding names of occupations and competencies ----------------
const words = (s: string) => s.replace(/[,.?!()]/g, ' ').spl
… [11991 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check reduced motion and share ops

  <details><summary>result</summary>

```
./journeys/talent-c/shared.tsx:5:import { MotionConfig } from 'motion/react';
./journeys/talent-c/shared.tsx:29:  return <Still.Provider value={lite}><MotionConfig reducedMotion={lite ? 'always' : 'user'}><div className="talent-c-page" data-lite={lite ? 'on' : undefined}>{children}</div></MotionConfig></Still.Provider>;
./app/App.tsx:1:import { MotionConfig } from 'motion/react';
styles/agency.css:194:@media (prefers-reduced-motion: reduce) {
styles/base.css:54:@media (prefers-reduced-motion: reduce) {
styles/gallery.css:24:@media (prefers-reduced-motion: reduce) { .gs-skel, .gs-caret { animation: none; } }
styles/talent-c.css:56:@media (prefers-reduced-motion: reduce) { .talent-c-mic[aria-pressed='true']::after { animation: none; } }
styles/talent-c.css:73:@media (prefers-reduced-motion: reduce) { .talent-c-progress .bar i[data-next] { animation: none !important; } }
114:function mirror(w: World, personId: string, r: Rec, kind: 'PRACTICE' | 'ASSESSMENT', title: string, level?: number) {
115-  const id = kind === 'PRACTICE' ? `e_j7_${personId}_${r.id}` : `e_j7_${personId}_assess_${r.comp}`;
116-  const prev = w.evidence.find((e) => e.evidenceId === id);
117-  const item = { evidenceId: id, ownerId: personId, kind, title: kind === 'PRACTICE' ? `Practice: ${title}` : `${title}${level ? ` · level ${level} of 4` : ''}`,
118-    source: kind === 'PRACTICE' ? 'Talent Q practice (private)' : 'Talent Q rubric review (simulated reviewer)', observedAt: r.at.slice(0, 10), verified: kind
… [1303 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Locate share ops and motion config

  <details><summary>result</summary>

```
q/skills/evidence-candidate.ts:219:      actions: [{ label: `End ${name}’s access`, primary: true, act: { t: 'do', op: 'tb.revoke', args: { ids: [e.evidenceId], org } } }, { label: `Preview ${name}’s view`, act: { t: 'nav', to: `/c/passport?as=${org}` } }, { label: 'Keep sharing', act: { t: 'say', text: 'keep it' } }],
q/skills/talent-b.ts:60:        ...(org ? [{ label: `Share the summary with ${orgName(c.w, org)}`, primary: true, act: { t: 'do', op: 'tb.share', args: { ids: ['e_tobi_conf_red'], org } } } as QAction] : []),
q/skills/talent-b.ts:94:  id: 'tb.share', side: 'candidate',
q/skills/talent-b.ts:109:      actions: [{ label: `Share with ${orgName(c.w, org)}`, primary: true, act: { t: 'do', op: 'tb.share', args: { ids: items.map((e) => e.evidenceId), org } } }, { label: `Preview what ${orgName(c.w, org)} sees`, act: { t: 'nav', to: `/c/passport?as=${org}` } }, { label: 'Not now', act: { t: 'say', text: 'keep it' } }],
q/skills/talent-b.ts:116:  id: 'tb.revoke', side: 'candidate',
q/skills/talent-b.ts:128:      actions: [{ label: `End ${orgName(c.w, org)}’s access`, primary: true, act: { t: 'do', op: 'tb.revoke', args: { ids: items.map((e) => e.evidenceId), org } } }, { label: `Preview ${orgName(c.w, org)}’s view`, act: { t: 'nav', to: `/c/passport?as=${org}` } }, { label: 'Keep it', act: { t: 'say', text: 'keep it' } }],
1:import { MotionConfig } from 'motion/react';
2-import { useRoute } from '../ui/router';
3-import { ToastHost } from '../ui/kit';
--
19-  const { pat
… [870 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find tb.share op implementation

  <details><summary>result</summary>

```
./q/skills/talent-b.ts:94:  id: 'tb.share', side: 'candidate',
./journeys/talent-b/Passport.tsx:260:  const toggle = (e: Evidence, o: string, c: Cell) => act(cellOn(c) ? 'tb.revoke' : 'tb.share', { ids: [e.evidenceId], org: o });
./journeys/talent-b/logic.ts:101:registerOp('tb.share', (w, a, actor) => {
./journeys/talent-b/logic.ts:112:registerOp('tb.revoke', (w, a, actor) => {
./journeys/talent-b/logic.ts:119:  if (!a.silent) pushUndo(w, actor.id, `end ${orgName(w, org)}’s access`, 'tb.share', { ids, org });
journeys/talent-b/logic.ts:101:registerOp('tb.share', (w, a, actor) => {
journeys/talent-b/logic.ts:119:  if (!a.silent) pushUndo(w, actor.id, `end ${orgName(w, org)}’s access`, 'tb.share', { ids, org });
```
  </details>

- 🔧 `Bash`: Read share op and engine exports

  <details><summary>result</summary>

```
function share(_w: World, e: Evidence, org: string) {
  e.revokedFrom = (e.revokedFrom ?? []).filter((x) => x !== org);
  if (e.visibility !== 'PUBLIC_PROFILE') { e.visibility = 'SHARED_WITH'; if (!e.sharedWith.includes(org)) e.sharedWith.push(org); }
}
function revoke(w: World, e: Evidence, org: string) {
  e.sharedWith = e.sharedWith.filter((x) => x !== org);
  if (e.visibility === 'SHARED_WITH' && !e.sharedWith.length) e.visibility = 'PRIVATE';
  if (!(e.revokedFrom ?? []).includes(org)) e.revokedFrom = [...(e.revokedFrom ?? []), org];
  void w;
}

registerOp('tb.share', (w, a, actor) => {
  const ids = (a.ids as string[]) ?? [String(a.id)]; const org = String(a.org);
  const items = ids.map((id) => evById(w, id)).filter((e): e is Evidence => !!e && e.ownerId === actor.personId);
  const conf = items.filter((e) => e.confidential);
  if (conf.length) return { say: `I didn’t share “${conf[0].title}”. It’s the confidential original, and it stays private. I can share a redacted summary instead.` };
  for (const e of items) share(w, e, org);
  if (w.q.frames[actor.id]?.intent === 'tb.conf') w.q.frames[actor.id] = null;
  emit(w, actor.id, 'passport.shared', `SHARED:${org}:${actor.personId}`, `${actor.name} shared ${items.length} Passport ${items.length === 1 ? 'item' : 'items'} with ${orgName(w, org)}.`, { ids, org });
  pushUndo(w, actor.id, `share with ${orgName(w, org)}`, 'tb.revoke', { ids, org, silent: true });
  return { say: `${orgName(w, org)} can now see ${items.map((e
… [5064 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Q types and engine

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
  id: string;
  side: Side | 'both';
  /** How confident this skill is that the turn is for it (0–1). Highest wins above 0.45. */
  match(c: QCtx): number;
  han
… [9282 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read feature test example and run-all
- 🔧 `Bash`: Read design note sample and status shape

  <details><summary>result</summary>

```
// EVIDENCE-FIRST · candidate side (build pack 30 Oct; J12 steps 6, 7, 10, 12, 13; pack items D, E, F; P6), desktop
// 1440×900 and phone 390×844. Seyi Okoro (p_seyio): proof classes in the recruiter's words, his CV as claims with a calm
// Q line, Kora's bounded sample request (injected as SENT through the store, as the recruiter's approved message would
// leave it): do it, submit, "Self-reported, waiting for review", the review outcome once Kora shares it; a second request
// declined (recorded as declined, not failed); CV help that never adds a claim; "What you want" with blanks kept blank.
// Tobi: hiring confirmed only on Kora's job, interest answered, the private J7 gap card, revoking the debugging sample
// with the "what Kora sees" preview updating. Zara: Kora's overdue commitment shown honestly.
// Usage: BASE=http://localhost:5197/ node qa/scripts/features/evidence-candidate.mjs [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
const ROOT = new URL('../../../captures/features/evidence-candidate/', import.meta.url).pathname; mkdirSync(ROOT, { recursive: true });
const BASE = process.env.BASE || 'http://localhost:5197/';
const ONLY = (process.argv[2] || 'd,m').split(',');
const WORDS = { CLAIM: 'Claim', SELF_REPORTED: 'Self-reported', ASSESSED: 'Assessed', ISSUER_VERIFIED: 'Issuer-verified', DISPUTED: 'Disputed' };
const JUDGE = /\b(untrue|lie|lying|liar|false|fake|exaggerat|inflated|dishonest)\b/i;

const b
… [8178 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
## Rendered critique (first render), most severe first
1. Sev 3 · H8, readability (CV draft, both widths): a positional word diff across split and reordered lines read as
   noise, with half-struck words and highlights running into each other. → Changed to "Now / Was" per line, with
   set-based marking and the original hidden while a draft is open (pair 10).
2. Sev 3 · H4, H8 (Passport cards): two status pills stacked, "Self-reported" and "Not checked", saying the same
   thing. The class sat under the kind/date line. → The proof class now leads the card header. The check pill shows
   only while a check is in flight or failed, and never alongside "waiting for review" (pairs 01, 05).
3. Sev 2 · Visual hierarchy (Passport, phone): the full CV document pushed "Add proof" two screens down. → The CV is
   collapsed into "Read your CV (6 lines)"; the label and Q's line stay visible (pair 01).
4. Sev 2 · H2 (request card, proactive card, Q replies): "postgres at scale" was lower-cased. → Case-aware wording:
   "your work on Postgres at scale".
5. Sev 2 · Noise (Applications): "No hiring confirmation from this employer" repeated on each application card. →
   Applications show only a confirmation that exists. Jobs keep the explicit absence, because that page separates
   confirmed listings from the rest (pairs 09, 16).
6. Sev 1 · Legend (Passport strip): each key item had both a swatch and a glyph. → Swatch only, matching the bar.
7. Sev 1 · Age line: "seven years old" was bold war
… [4850 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect status.json entry shape

  <details><summary>result</summary>

```
dict_keys(['_readme', 'defaults', 'surfaces', 'priority', 'screens', 'motions', 'vision', 'routes', 'design_refs', 'd_native_routes'])
SC-117 {'status': 'INTEGRATED', 'route': '/r/home', 'evidence': 'captures/screens/p01-home-after-search, m-p01-home', 'note': 'Connected to shared typed state; axe 0 violations (dark/light, 1440/390); manual keyboard + screen-reader pass pending, so not VERIFIED.'}
SC-162 {'status': 'INTEGRATED', 'route': '/c/growth', 'evidence': 'captures/screens/p10-career-amaka, p10-career-chidi, m-p10-career', 'note': 'The original career dashboard (six measures, readiness) now lives at /c/growth inside the D shell, still connected to the shared world. The D J7 workspace at /c/career supersedes it in design.'}
MO-001 {'status': 'PROTOTYPED', 'route': '/r/home', 'evidence': '', 'note': 'Driven by a real state or run event; reduced-motion handled by MotionConfig/CSS. Dedicated clip not recorded yet.'}
MO-002 {'status': 'PROTOTYPED', 'route': '/c/interview', 'evidence': 'prototype/src/journeys/talent-c/shared.tsx (MicButton shows QMark listening mood while recording); prototype/src/ds/QMark.tsx', 'note': 'Driven by the microphone on /c/interview: the listening mood runs while recording. It follows recording state, not input level.\r (Reconciled 30 Oct: was recorded only in the generated CSV; code checked and moved into status.json.)'}
ADDENDUM-REQUIREMENTS.csv
CONSOLIDATION-REQUIREMENTS.csv
status.json
after
before
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:interaction-design", "args": "Talent Q TALENT-D candidate pages: work authorisation (consent per employer), work critique + revision history, cover letter builder with source

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-30 12:30

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


ARGUMENTS: Talent Q TALENT-D candidate pages: work authorisation (consent per employer), work critique + revision history, cover letter builder with source chips, learning player (simulated video with captions/transcript), sample improvement wizard, rejection recovery coaching; motions MO-014 list reorder on filter, MO-029 share revoked, MO-030 CV draft grows, MO-040 application stage change, MO-041 consent change, MO-052 share approved after receipt. Direction D tokens; reduced-motion fallbacks.

- 🔧 `Skill`: {"skill": "design-skills:ux-writing", "args": "Candidate microcopy for: work authorisation (private by default, never a hidden filter), kind concrete work critique, revision history, cover letter (no

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-30 12:30

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


ARGUMENTS: Candidate microcopy for: work authorisation (private by default, never a hidden filter), kind concrete work critique, revision history, cover letter (no invented facts), learning player, improvement wizard, warm honest rejection recovery that never guesses the employer's reasons.

- 🔧 `Skill`: {"skill": "design-skills:design-elevation", "args": "Direction D prototype candidate pages (TALENT-D): stay within existing tokens and ds components; hierarchy, spacing, one primary action per sheet."

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-30 12:30

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


ARGUMENTS: Direction D prototype candidate pages (TALENT-D): stay within existing tokens and ds components; hierarchy, spacing, one primary action per sheet.

- 🔧 `Skill`: {"skill": "design-superpowers:creative", "args": "Within Direction D only (no new aesthetics, typefaces or colours; gold is Q's alone): art direction for a simulated video player, a version timeline a

  <details><summary>result</summary>

```
Launching skill: design-superpowers:creative
```
  </details>


**User** · 2026-10-30 12:30

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


ARGUMENTS: Within Direction D only (no new aesthetics, typefaces or colours; gold is Q's alone): art direction for a simulated video player, a version timeline and a consent receipt for Talent Q candidate pages.

- 🔧 `Bash`: List ds classes, tokens, and system doc

  <details><summary>result</summary>

```
.ds .ds-actions .ds-agent .ds-app .ds-askbar .ds-av .ds-banner .ds-brandname .ds-btn .ds-canvas .ds-canvas-head .ds-chip .ds-compose .ds-confirm .ds-context .ds-field .ds-filter .ds-groupbtn .ds-iconbtn .ds-input .ds-linkbtn .ds-log .ds-main .ds-me .ds-more .ds-navgroup .ds-navlink .ds-next .ds-node .ds-note .ds-opt .ds-page .ds-page-body .ds-pageindex .ds-palette .ds-plan .ds-proto .ds-proto-bar .ds-q .ds-qline .ds-qsim .ds-quote .ds-rail .ds-rail-brand .ds-rail-foot .ds-railbtn .ds-scrim .ds-send .ds-sep .ds-sheet .ds-sheetbar .ds-sim .ds-skeleton .ds-space .ds-space-btn .ds-split .ds-strip .ds-suggest .ds-suggest-foot .ds-suggest-more .ds-switch .ds-switchrow .ds-table .ds-table-wrap .ds-tabs .ds-tag .ds-taskhead .ds-thinking .ds-thread .ds-thread-head .ds-used .ds-versions .ds-views .ds-who .ds-why 
--color-action: --color-bg: --color-focus: --color-info: --color-line-strong: --color-line: --color-ok: --color-on-action: --color-on-q: --color-paper-line: --color-paper-muted: --color-paper-q-text: --color-paper-raised: --color-paper-text: --color-paper: --color-q-strong: --color-q-text: --color-q: --color-risk: --color-surface-raised: --color-surface-sunken: --color-surface: --color-text-muted: --color-text-subtle: --color-text: --color-warn: --font-mono: --font-ui: --font-voice: --motion-base: --motion-ease-in-out: --motion-ease-out: --motion-instant: --motion-quick: --motion-settle: --motion-slow: --radius-lg: --radius-md: --radius-pill: --radius-sm: --radius-xl: --ref-am
… [4779 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check package scripts and QA hook

  <details><summary>result</summary>

```
{
  "name": "talent-q-prototype",
  "private": true,
  "version": "0.2.0",
  "type": "module",
  "scripts": {
    "tokens": "node ../tokens/build.mjs",
    "registers": "node ../scripts/build-registers.mjs",
    "dev": "npm run tokens && vite",
    "build": "npm run tokens && tsc -b && vite build",
    "preview": "vite preview --port 4174",
    "typecheck": "tsc -b"
  },
  "dependencies": {
    "@fontsource-variable/bricolage-grotesque": "^5.3.0",
    "@fontsource-variable/fraunces": "^5.3.0",
    "@fontsource-variable/geist": "^5.3.0",
    "@fontsource-variable/geist-mono": "^5.3.0",
    "@fontsource-variable/inter-tight": "^5.3.0",
    "@fontsource-variable/jetbrains-mono": "^5.3.0",
    "@fontsource-variable/manrope": "^5.3.0",
    "@fontsource-variable/newsreader": "^5.3.0",
    "@fontsource-variable/space-grotesk": "^5.3.0",
    "@fontsource/ibm-plex-mono": "^5.3.0",
    "motion": "^12.23.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@types/react": "^18.3.31",
dist
dist-review
index.html
node_modules
package-lock.json
package.json
src
tsconfig.json
tsconfig.tsbuildinfo
vite.config.ts
vite.offline.config.ts
vite.review.config.ts
src/main.tsx:13:(window as unknown as { __tqQA: unknown }).__tqQA = { canDiscover, canSeeCandidate, relationshipWith, visibleEvidence, orgLimits, outreachThisWeek, visibleSegments, proofReading, proofClass, getWorld, update,
```
  </details>

- 🔧 `Bash`: Read main.tsx and route guard

  <details><summary>result</summary>

```
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './styles/tokens.css';
import './styles/base.css';
import './styles/components.css';
import { App } from './app/App';
import { visibleSegments } from './state/areas/media';
import { proofClass, proofReading } from './journeys/evidence/model';
import { runAction } from './q/core/engine';
import { canDiscover, canSeeCandidate, getWorld, orgLimits, outreachThisWeek, relationshipWith, update, visibleEvidence } from './mock/world';

// QA hook for the privacy tests (qa/scripts/review/privacy.mjs). The prototype holds only simulated data.
(window as unknown as { __tqQA: unknown }).__tqQA = { canDiscover, canSeeCandidate, relationshipWith, visibleEvidence, orgLimits, outreachThisWeek, visibleSegments, proofReading, proofClass, getWorld, update,
  // Run a registered op exactly as a chip or button would (gate scripts use it to drive real state transitions).
  act: (op: string, args: Record<string, unknown> = {}) => runAction({ label: op, act: { t: 'do', op, args } } as Parameters<typeof runAction>[0]) };

// Review links: "#/r/home?as=u_ada" opens any page as that person, already signed up (demo only).
// The parameter is applied once and removed, so the address bar shows the plain route.
function openAs() {
  const [route, query = ''] = location.hash.slice(1).split('?');
  const as = new URLSearchParams(query).get('as');
  if (!as || !getWorld().actors.some((a) => a.id === as)) return;
  update
… [1549 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Canvas and helpers

  <details><summary>result</summary>

```
</motion.div>
  );
}

// ---------------- Canvas ----------------
export interface ViewDef<V extends string> { id: V; label: string; ready?: boolean }
export interface Version<V extends string> { v: number; label: string; view: V }

export function Canvas<V extends string>({ title, kicker, views, view, setView, versions = [], onVersion, building, open, onClose, children, qLine, aside }: {
  title: string; kicker: ReactNode; views?: ViewDef<V>[]; view?: V; setView?: (v: V) => void; versions?: Version<V>[]; onVersion?: (v: Version<V>) => void;
  building?: boolean; open: boolean; onClose: () => void; children: ReactNode; qLine?: string; aside?: ReactNode;
}) {
  const nestedShell = useContext(InShell);
  const narrow = useNarrow() && !nestedShell;
  const ref = useRef<HTMLElement>(null);
  useEffect(() => { if (narrow && open) ref.current?.focus(); }, [narrow, open]);
  if (narrow && !open) return null;
  const latest = versions[versions.length - 1];
  const Tag = narrow ? 'section' : 'main';
  return (
    <Tag ref={ref} tabIndex={-1} className={`ds-canvas ${narrow ? 'as-sheet' : ''}`} aria-label={`${title}, artifact`} role={narrow ? 'dialog' : undefined} aria-modal={narrow ? true : undefined}
      onKeyDown={(e) => { if (narrow && e.key === 'Escape') onClose(); }} style={{ outline: 'none' }}>
      {narrow && (
        <div className="ds-sheetbar ink">
          <button type="button" className="ds-send" onClick={onClose} aria-label="Back to the conversation with Q"><svg widt
… [5065 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check Tinda actors, thread types, cover skills

  <details><summary>result</summary>

```
state/seed.ts:31:  { id: 'org_tinda', name: 'Tinda', kind: 'EMPLOYER', industry: 'Consumer apps', size: '45 people', city: 'Lagos', verified: { domain: true, registry: 'VERIFIED' }, delegation: 'APPROVE_EACH_SEND', setup: { done: true, step: 5 }, guidelines: [] },
state/seed.ts:32:  { id: 'org_carehome', name: 'Sunrise Care Homes', kind: 'EMPLOYER', industry: 'Care', size: '200 people', city: 'Uyo', verified: { domain: true, registry: 'VERIFIED' }, delegation: 'APPROVE_EACH_SEND', setup: { done: true, step: 5 }, guidelines: [] },
 *   APPROVED ─send→ QUEUED ─provider ok→ ACCEPTED ─(provider evidence only)→ DELIVERED
 *                          └ provider error → FAILED (retryable, e.g. AUTH_EXPIRED) | BOUNCED (final)
 * "Sent" in the UI means ACCEPTED by the provider, never "received" or "read".
 */
export type Delivery = 'QUEUED' | 'ACCEPTED' | 'DELIVERED' | 'BOUNCED' | 'FAILED' | 'CANCELLED';
export type FailReason = 'AUTH_EXPIRED' | 'DISCONNECTED' | 'SMTP_REJECTED' | 'RATE_LIMITED' | 'SUPPRESSED' | 'BAD_ADDRESS' | 'OFFLINE' | 'MISSING_ATTACHMENT';
export interface Msg {
  id: string; from: string; to: string; subject?: string; body: string; at: string; status: MsgStatus; approvedBy?: string; receipt?: string; channel: 'EMAIL' | 'IN_APP' | 'SMS';
  // ---- Connected email and candidate contact (addenda, 29 Oct). All optional so earlier records stay valid. ----
  /** MailboxConnection id the message goes out from (email only). Talent Q notices use the service mailbox. */
  s
… [2792 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check talent-b helpers and seeds

  <details><summary>result</summary>

```
10:export { tb };
11:export const PSCOPE = (pid: string) => `PERSON:${pid}`;
12:export const orgName = (w: World, id: string) => w.orgs.find((o) => o.id === id)?.name ?? id;
13:export const shortOrg = (w: World, id: string) => orgName(w, id).replace(/ (Pay|Health|Logistics|Freight Tech|Care Homes)$/, '');
14:export const fmtDate = (s: string) => new Date(s).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' });
15:export const daysBetween = (a: Date, b: Date) => Math.max(0, Math.floor((b.getTime() - a.getTime()) / 864e5));
18:export type Ver = NonNullable<Evidence['verification']>;
19:export const verOf = (e: Evidence): Ver => e.verification ?? (e.verified ? 'VERIFIED' : 'UNVERIFIED');
20:export const VER: Record<Ver, { label: string; plain: string; k: 'ok' | 'warn' | 'risk' | 'busy' | undefined }> = {
27:export const KIND: Record<Evidence['kind'], string> = { PROJECT: 'Project', CREDENTIAL: 'Certificate', ASSESSMENT: 'Assessment', WORK_SAMPLE: 'Work sample', REFERENCE: 'Reference', EMPLOYMENT: 'Employment', CLAIM: 'Claim', PRACTICE: 'Practice (private)' };
28:export const myEvidence = (w: World, pid: string) => w.evidence.filter((e) => e.ownerId === pid && e.kind !== 'PRACTICE');
29:export const evById = (w: World, id: string) => w.evidence.find((e) => e.evidenceId === id);
30:export const isCode = (e: Evidence) => /repo|code|library|github|worker|api|service/i.test(`${e.title} ${e.source}`);
33:export function viewerOrgs(w: World, pid: string) {
38:export type Cel
… [5222 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/state/areas/talent-d.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/state/areas/talent-d.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/state/seeds/talent-d.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/state/seeds/talent-d.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check tests that may depend on Amaka evidence

  <details><summary>result</summary>

```
109:  step('Profile complete; claims sync to her private Passport', w.profiles.p_amaka.done && w.evidence.filter((e) => e.ownerId === 'p_amaka' && e.kind === 'CLAIM').every((e) => e.visibility === 'PRIVATE') && /0|Nothing is shared/.test(r), r);
140:  step('Feedback without scoring; not evidence', /use “I”/.test(r) && /isn’t evidence/.test(r), r);
review/privacy.mjs:39:step(await qa('canSeeCandidate', 'p_amaka', 'org_kora'), 'before: Kora (verified) may find Amaka');
review/privacy.mjs:40:await setDiscovery('p_amaka', { who: 'VERIFIED_EMPLOYERS', hideFrom: ['org_kora'] });
review/privacy.mjs:41:step(!(await qa('canSeeCandidate', 'p_amaka', 'org_kora')), 'after hiding from Kora: Kora can’t see Amaka');
review/privacy.mjs:42:step((await qa('visibleEvidence', 'p_amaka', 'org_kora')).length === 0, 'Kora reads none of Amaka’s evidence, public items included');
review/privacy.mjs:43:await as('u_ada', '/r/people/p_amaka');
review/privacy.mjs:45:const r2 = await ask('show me everything about amaka');
review/privacy.mjs:47:step(await qa('canSeeCandidate', 'p_amaka', 'org_medlink'), 'other employers are unaffected (Medlink can still find Amaka)');
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/logic.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/logic.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Find J7 op names

  <details><summary>result</summary>

```
604:registerOp('ta.j7.restore', (w, a) => { w.j7[String(a.personId)] = JSON.parse(String(a.snap)); });
731:registerOp('ta.j7.quiz.answer', (w, a, actor) => {
847:registerOp('ta.j7.reschedule', (w, a, actor) => {
915:registerOp('ta.j7.goal.set', (w, a, actor) => {
922:registerOp('ta.j7.step.toggle', (w, a, actor) => {
927:registerOp('ta.j7.step.move', (w, a, actor) => { const S = j7(w, pidOf(actor)); const i = S.plan.findIndex((x) => x.id === a.id); const j = i + Number(a.d); if (i < 0 || j < 0 || j >= S.plan.length) return; [S.plan[i], S.plan[j]] = [S.plan[j], S.plan[i]]; });
928:registerOp('ta.j7.step.remove', (w, a, actor) => {
934:registerOp('ta.j7.quiz.start', (w, a, actor) => {
940:registerOp('ta.j7.sample.submit', (w, a, actor) => {
934:registerOp('ta.j7.quiz.start', (w, a, actor) => {
935-  const pr = startQuiz(w, pidOf(actor), a.comp ? String(a.comp) : undefined); if (!pr) return;
936-  const P = personaFor(pidOf(actor));
937-  w.q.frames[actor.id] = { intent: 'ta.j7.quiz', slots: { comp: pr.comp }, awaiting: 'option', startedAt: new Date().toISOString() };
938-  appendQ(w, actor.id, { who: 'q', engine: 'rules', kind: 'question', why: 'Practice · private · not proof', text: `One practice question on ${compById(P, pr.comp).label.toLowerCase()}. Answer on the page or here: a, b or c.` });
939-});
940-registerOp('ta.j7.sample.submit', (w, a, actor) => {
941-  const pid = pidOf(actor); const r = submitSample(w, pid, a.comp ? String(a.comp) : undefined); if (!r) return;
94
… [30 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check talent-b skill helpers

  <details><summary>result</summary>

```
// talent-b Q skills (T3 Tobi, T5 Zara). Everything the pages do is reachable by typing to Q in imperfect
// language: uploads, checks, sharing and revoking per organisation, confidential work, Q's summary and its
// correction, discovery, interview prep, jobs and employer signals, matches and challenges, applying,
// honest status, follow-ups, declined advice, notifications, memory and deletion.
import type { Evidence } from '@contracts';
import { registerOp, registerSkill } from '../core/engine';
import type { QCtx, QReply } from '../core/types';
import type { Job, QAction } from '../../state/domain';
import { emit, simNow, uid, now, visibleEvidence, type World } from '../../mock/world';
import {
  APP_LABEL, NEED_LABEL, VER, adviceFor, appExplain, cellOf, deletionPlan, discoveryOf, evById, findMemories, fitLine, followupText, isCode, matchFor,
  memoriesOf, myEvidence, orgName, ensureRedacted, signalsOf, startCheck, startUpload, summaryFor, tb, verOf, verifiedEmployer, viewerOrgs, defaultName, PSCOPE, fmtDate,
} from '../../journeys/talent-b/logic';
import type { UploadKind } from '../../state/areas/talent-b';

const cand = (c: QCtx) => c.actor.side === 'candidate' && !!c.actor.personId;
const pidOf = (c: QCtx) => c.actor.personId!;
const reply = (text: string, extra: Partial<QReply['msgs'][number]> = {}): QReply['msgs'][number] => ({ kind: 'reply', text, ...extra });

// ---------- entity helpers ----------
const ORG_KW: [RegExp, string][] = [[/\bkora\b|\bkorapay\b/, 'org
… [2510 more characters trimmed]
```
  </details>


**Claude** · 2026-10-30 12:34

Now the ops and skills file.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/skills/talent-d.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/skills/talent-d.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Verify j7 exports and Thread type

  <details><summary>result</summary>

```
10:export type PId = Persona['id'];
13:export const personaFor = (personId: string): Persona => PERSONAS[pidFor(personId)];
38:export function occFromText(P: Persona, norm: string): JOcc | null {
47:export function compFromText(P: Persona, norm: string) {
66:export const readJ7 = (w: World, personId: string): J7State => { const s = w.j7[personId] as J7State | undefined; return s && s.v === 2 ? s : freshJ7(w, personId); };
68:export const j7 = (w: World, personId: string): J7State => { const s = readJ7(w, personId); w.j7[personId] = s; return s; };
90:export const occById = (P: Persona, id: string) => [...P.occs, ...P.extra].find((o) => o.id === id);
91:export const compById = (P: Persona, id: string) => P.comps.find((c) => c.id === id)!;
92:export const practiceFor = (P: Persona, comp?: string) => P.practices.find((p) => p.comp === comp) ?? null;
93:export const sampleFor = (P: Persona, comp?: string) => P.samples.find((s) => s.comp === comp) ?? null;
110:export const jobsFor = (w: World, P: Persona, occ: string) => (P.jobs[occ] ?? []).map((id) => w.jobs.find((j) => j.id === id)).filter(Boolean) as World['jobs'];
162:export function submitSample(w: World, personId: string, comp?: string) {
77:export interface Thread {
78-  id: string; orgId: string; personId: string; mandateId?: string; messages: Msg[];
79-  /** The hiring campaign this thread was routed into (role → campaign is canonical; this is the routing record). */
80-  campaignId?: string; initiatedBy?: 'CANDIDATE' | '
… [26 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Fix resourcesFor calls and wizard guard

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/ui.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/ui.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Read talent-b css idioms

  <details><summary>result</summary>

```
/* talent-b (T3 Tobi, T5 Zara): Passport portfolio, disclosure matrix, search reach, jobs, applications, prep,
   memory, and Q's reply cards. Candidate warmth comes from data-audience; gold stays reserved for Q. */
.tb-stack { display: grid; gap: 12px; min-width: 0; }
.tb-row-between { display: flex; justify-content: space-between; align-items: center; gap: 8px 12px; flex-wrap: wrap; min-width: 0; }
.tb-actions { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.tb-filters { display: flex; flex-wrap: wrap; gap: 8px; }
.tb-filters .ds-filter { min-height: 44px; }
.tb-break { overflow-wrap: anywhere; min-width: 0; }
.tb-h2 { margin: 0; font-family: var(--voice); font-weight: 400; font-size: 22px; line-height: 1.25; letter-spacing: -.01em; overflow-wrap: anywhere; }
.tb-count { display: inline-grid; place-items: center; min-width: 26px; height: 22px; padding: 0 7px; margin-left: 6px; border-radius: 999px; background: var(--wash); font-family: var(--ui); font-size: 13px; font-weight: 600; color: var(--ink-2); vertical-align: 3px; }
.tb-colnote { font-size: 12px; font-weight: 500; color: var(--ink-3); }
.tb-title { margin: 0; font-family: var(--voice); font-weight: 420; font-size: 20px; line-height: 1.25; overflow-wrap: anywhere; }
.tb-title a { color: inherit; text-decoration: none; background-image: linear-gradient(currentColor, currentColor); background-size: 100% 1px; background-position: 0 100%; background-repeat: no-repeat; }
.tb-title a:hover { background-s
… [2606 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List ds.css custom properties

  <details><summary>result</summary>

```
--gold: --ink: --night: --ok: --paper: --r-control: --rail-w: --shadow: --voice:
```
  </details>

- 🔧 `Bash`: Find most used CSS variables

  <details><summary>result</summary>

```
51 var(--ink
     33 var(--moon-2
     33 var(--ink-3
     32 var(--rule
     22 var(--ink-2
     21 var(--data
     20 var(--sheet
     20 var(--gold-light
     19 var(--night-3
     19 var(--moon
     18 var(--voice
     16 var(--rule-2
     16 var(--risk
     16 var(--paper
     15 var(--wash
     12 var(--gold-ink
     10 var(--ok
      9 var(--night
      7 var(--warn
      7 var(--night-4
      6 var(--night-2
      5 var(--motion-quick
      5 var(--motion-ease-out
      5 var(--gold
      3 var(--gold-wash
      2 var(--ui
      2 var(--shadow
      2 var(--r-surface
      1 var(--thread-w
      1 var(--ref-red-light
      1 var(--ref-red-dark
      1 var(--ref-paper-4
      1 var(--ref-paper-3
      1 var(--ref-paper-2
      1 var(--ref-paper-1
      1 var(--ref-paper-0
      1 var(--ref-night-4
      1 var(--ref-night-3
      1 var(--ref-night-1
      1 var(--ref-night-0
```
  </details>


**Claude** · 2026-10-30 12:37

Now the CSS.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/talent-d.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/talent-d.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/WorkPermit.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/WorkPermit.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Work.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Work.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Render revoked preview without content; fix names

  <details><summary>result</summary>

```
WorkPermit.tsx:81:                              {v ? <ul style={{ margin: 0, paddingLeft: 18 }}>{v.entries.map((e) => <li key={e.country}>{e.country}: {AUTH_SHORT[e.status].toLowerCase()} ({a.first}’s statement, not checked)</li>)}{v.doc && <li>Document: {v.doc.name} (attached by {a.first}, not checked by Talent Q)</li>}</ul> : null}
Work.tsx:187:                          {sees && <div className="td-preview-body">
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Letter.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Letter.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check stateOf and CState values

  <details><summary>result</summary>

```
/** State of a competency for display: a stored state, or "unclear" when the person has only mentioned it. */
export function stateOf(w: World, personId: string, S: J7State, comp: string): CState {
  const s = S.states[comp] ?? 'none';
  if (s !== 'none') return s;
  const c = personaFor(personId).comps.find((x) => x.id === comp);
  if (S.mentioned[comp]) return 'unclear';
  const txt = profileText(readProfile(w, personId));
  return c?.kws?.some((k) => txt.includes(k)) ? 'unclear' : 'none';
}
/** The person's own words behind a "mentioned" competency (for showing the basis, never as proof). */
export function mentionOf(w: World, personId: string, S: J7State, comp: string): string | null {
101:export type CState = 'verified' | 'full' | 'partial' | 'practice' | 'none' | 'unclear';
102:export interface Comp { id: string; label: string; plain: string; state: CState; evidence?: { title: string; cls: string; proves: string; notProves: string } }
117:export const shown = (s: CState) => s === 'verified' || s === 'full';
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Learn.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Learn.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Improve.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Improve.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Recovery.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/Recovery.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Write routes file and small fixes

  <details><summary>result</summary>

```
app/App.tsx:13:import.meta.glob('../routes/*.tsx', { eager: true });
app/App.tsx:14:import.meta.glob('../q/skills/*.ts', { eager: true });
app/App.tsx:15:import.meta.glob('../q/proactive/*.ts', { eager: true });
app/App.tsx:16:import.meta.glob('../q/openers/*.ts', { eager: true });
```
  </details>

- 🔧 `Bash`: Write refs, openers, proactive; run typecheck

  <details><summary>result</summary>

```
src/journeys/assess/model.ts(71,22): error TS6133: 'w' is declared but its value is never read.
src/journeys/hire-d/model.ts(141,49): error TS6133: 'mid' is declared but its value is never read.
src/journeys/org-admin/PagesOrg.tsx(71,152): error TS2339: Property 'by' does not exist on type '{ v: number; body: string[]; }'.
src/journeys/talent-d/Work.tsx(41,11): error TS6133: 'w' is declared but its value is never read.
src/q/skills/talent-d.ts(12,42): error TS6133: 'stepsFromFeedback' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Fix unused vars and re-typecheck

  <details><summary>result</summary>

```
const { w, a, x, mine, ds, empty } = useWork();
[This command modified 2 files you've previously read: q/skills/talent-d.ts, journeys/talent-d/Work.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Find reduced-motion config in shell

  <details><summary>result</summary>

```
./ui/kit.tsx:4:import { AnimatePresence, motion, useReducedMotion } from 'motion/react';
./ui/kit.tsx:102:  const reduce = useReducedMotion();
./ui/kit.tsx:190:  const reduce = useReducedMotion();
./ui/kit.tsx:265:  const reduce = useReducedMotion();
./journeys/talent-c/shared.tsx:5:import { MotionConfig } from 'motion/react';
./journeys/talent-c/shared.tsx:29:  return <Still.Provider value={lite}><MotionConfig reducedMotion={lite ? 'always' : 'user'}><div className="talent-c-page" data-lite={lite ? 'on' : undefined}>{children}</div></MotionConfig></Still.Provider>;
./journeys/hire-d/LensMorph.tsx:6:import { motion, useReducedMotion } from 'motion/react';
./journeys/hire-d/LensMorph.tsx:10:  const reduce = useReducedMotion();
./journeys/gallery/StatesGallery.tsx:6:import { AnimatePresence, motion, useReducedMotion } from 'motion/react';
./journeys/gallery/StatesGallery.tsx:15:  const reduce = useReducedMotion();
```
  </details>

- 🔧 `Bash`: Attach MO-014 motion to jobs list

  <details><summary>result</summary>

```
19:import { FilterMotion, MotionCard } from '../talent-d/motions';
71:    <MotionCard key={j.id} className="ds-sheet tb-card tb-jobcard">
84:    </MotionCard>
101:          {close.length > 0 && <section className="tb-group" aria-labelledby="tb-jg-close"><header className="tb-group-h"><h2 id="tb-jg-close" className="tb-h2">Closest to your proof <span className="tb-count num">{close.length}</span></h2></header><FilterMotion filter={filter}><ul className="tb-grid"><AnimatePresence initial={false} mode="popLayout">{close.map(card)}</AnimatePresence></ul></FilterMotion></section>}
102:          {rest.length > 0 && <section className="tb-group" aria-labelledby="tb-jg-rest"><header className="tb-group-h"><h2 id="tb-jg-rest" className="tb-h2">Other open roles <span className="tb-count num">{rest.length}</span></h2><p className="t14 muted">Your Passport doesn’t show these needs yet. That isn’t the same as not having them.</p></header><FilterMotion filter={filter}><ul className="tb-grid"><AnimatePresence initial={false} mode="popLayout">{rest.map(card)}</AnimatePresence></ul></FilterMotion></section>}
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/motions.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/talent-d/motions.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Attach MO-030 to CV draft lines

  <details><summary>result</summary>

```
const ref = useRef<HTMLDivElement>(null);
  const hid = useId();
  useEffect(() => { if (!compact && location.hash.includes('cv=draft')) ref.current?.scrollIntoView({ block: 'start' }); }, [compact]);
  const offers = cvOffer(d.personId).map((id) => w.evidence.find((e) => e.evidenceId === id)).filter((e): e is NonNullable<typeof e> => !!e && e.ownerId === d.personId);
  const approved = d.state === 'APPROVED';
  const fresh = useFresh(d.at) && !approved;
  return (
    <motion.div {...arrive} ref={ref} className="evc-draft" data-state={d.state} aria-labelledby={hid} role="region">
      <div className="evc-row"><h3 id={hid} className="evc-h3">{approved ? 'Your approved CV' : 'A clearer draft, for you to approve'}</h3><span className="ds-tag" data-k={approved ? 'ok' : 'busy'}>{approved ? `Approved ${dayMonth(d.approvedAt ?? d.at)}` : 'Draft · not saved'}</span></div>
      {!compact && <p className="t14 muted" style={{ margin: 0 }}>Each line shows the new wording, with <span className="evc-add">Q’s words marked</span>, and what it <span className="evc-del">was</span>. Facts, numbers and names are yours.</p>}
      <ol className="evc-diff">
        {d.lines.map((l, i) => (
          <GrowLine key={i} i={i} fresh={fresh}>
            <div className="evc-now">{l.after.map((x, k) => <p key={k} className="evc-diffline">{marked(x, l.before, 'evc-add')}</p>)}</div>
            {!compact && l.before !== l.after.join(' ') && <p className="evc-was t14"><span className="evc-was-k">Was</s
… [359 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read app label maps

  <details><summary>result</summary>

```
336:export const APP_LABEL: Record<Application['status'], string> = { DRAFT: 'Draft', SUBMITTED: 'Sent', VIEWED: 'Viewed', INTERVIEW: 'Interview', OFFER: 'Offer', NOT_PROGRESSING: 'Not progressing', WITHDRAWN: 'Withdrawn', JOB_CLOSED: 'Listing closed' };
337:export const APP_K: Record<Application['status'], 'ok' | 'warn' | 'risk' | 'busy' | undefined> = { DRAFT: undefined, SUBMITTED: undefined, VIEWED: 'busy', INTERVIEW: 'ok', OFFER: 'ok', NOT_PROGRESSING: 'risk', WITHDRAWN: undefined, JOB_CLOSED: 'warn' };
338-export function appExplain(w: World, a: Application) {
339-  const job = w.jobs.find((j) => j.id === a.jobId); const org = job ? orgName(w, job.orgId) : 'The employer';
```
  </details>

- 🔧 `Bash`: Attach MO-040 and recovery link to Applications

  <details><summary>result</summary>

```
src/journeys/talent-b/Applications.tsx(8,19): error TS6133: 'K' is declared but its value is never read.
src/journeys/talent-b/Applications.tsx(8,22): error TS6133: 'APP_LABEL' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Drop now-unused imports

  <details><summary>result</summary>

```
import { APP_K as K, APP_LABEL, appExplain, evById, fmtDate, tb } from './logic';
import { appExplain, evById, fmtDate, tb } from './logic';
3:import { registerRoute } from './registry';
12:registerRoute({ path: '/c/work-permit', side: 'candidate', label: 'where you can work', render: () => <WorkPermitPage /> });
```
  </details>

- 🔧 `Bash`: Add receipt line and letter link hooks

  <details><summary>result</summary>

```
journeys/talent-b/Jobs.tsx:20:import { LetterLink } from '../talent-d/ui'; // TALENT-D: cover note builder (SC-087)
journeys/talent-b/Jobs.tsx:146:      {!closed && !app && <LetterLink jobId={job.id} />}
journeys/talent-b/Passport.tsx:30:import { ShareReceiptLine } from '../talent-d/ui'; // TALENT-D (MO-052): shared only after a consent receipt
journeys/talent-b/Passport.tsx:206:      <ShareReceiptLine evidenceId={e.evidenceId} ownerId={e.ownerId} sharedWith={live} />
```
  </details>

- 🔧 `Bash`: Find registerHomeSection definition

  <details><summary>result</summary>

```
21:export const registerHomeSection = (side: 'recruiter' | 'candidate', s: Section) => { if (!sections[side].some((x) => x.id === s.id)) sections[side].push(s); };
./routes/entry.tsx:21:export const registerHomeSection = (side: 'recruiter' | 'candidate', s: Section) => { if (!sections[side].some((x) => x.id === s.id)) sections[side].push(s); };
```
  </details>

- 🔧 `Bash`: Read Section type

  <details><summary>result</summary>

```
import { QHome } from '../screens/QHome';
import { appendQ } from '../q/core/engine';
import { SwitchRow } from '../ds/Switch';
import { arrive } from '../ds/motion';
import { EvidenceHomeCards, evidenceHomeLine } from '../journeys/evidence/candidate/Requests';
import '../styles/home.css';
import '../ds/ds.css';

// ---------------- Home sections: journeys add blocks to the home pages ----------------
type Section = { id: string; order: number; when: (w: World) => boolean; render: () => ReactNode };
const sections: Record<'recruiter' | 'candidate', Section[]> = { recruiter: [], candidate: [] };
export const registerHomeSection = (side: 'recruiter' | 'candidate', s: Section) => { if (!sections[side].some((x) => x.id === s.id)) sections[side].push(s); };
routes/talent-c.tsx:17:registerHomeSection('candidate', { id: 'talent-c.first-steps', order: 5, when: mine, render: () => <FirstStepsCard /> });
```
  </details>

- 🔧 `Bash`: Add home section and Still wrappers to routes

  <details><summary>result</summary>

```
44:registerHomeSection('candidate', { id: 'talent-d.for-you', order: 60, when: (w) => links(w).length > 0, render: () => <ForYou /> });
46:registerRoute({ path: '/c/work-permit', side: 'candidate', label: 'where you can work', render: () => S(<WorkPermitPage />) });
47:registerRoute({ path: '/c/work/critique', side: 'candidate', label: 'Q’s read of your work', render: () => S(<CritiquePage />) });
48:registerRoute({ path: '/c/work/versions', side: 'candidate', label: 'your work’s versions', render: () => S(<VersionsPage />) });
49:registerRoute({ path: '/c/jobs/:id/letter', side: 'candidate', label: 'a cover note', render: (p) => S(<LetterPage jobId={p.id} />) });
50:registerRoute({ path: '/c/learn/:id', side: 'candidate', label: 'a lesson', render: (p) => S(<LearnPage id={p.id} />) });
51:registerRoute({ path: '/c/career/improve', side: 'candidate', label: 'improve your work sample', render: () => S(<ImprovePage />) });
52:registerRoute({ path: '/c/applications/:id/recovery', side: 'candidate', label: 'after a decision', render: (p) => S(<RecoveryPage appId={p.id} />) });
```
  </details>

- 🔧 `Bash`: Inspect useWorld selector semantics

  <details><summary>result</summary>

```
const shallowEq = (a: unknown, b: unknown) => {
  if (Object.is(a, b)) return true;
  if (!a || !b || typeof a !== 'object' || typeof b !== 'object') return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  return ka.length === kb.length && ka.every((k) => Object.is((a as Record<string, unknown>)[k], (b as Record<string, unknown>)[k]));
};
const subscribe = (l: () => void) => { listeners.add(l); return () => { listeners.delete(l); }; };
/** Select from the store. Selectors may build new arrays/objects: results are kept while shallowly equal. */
export function useWorld<T>(select: (w: World) => T): T {
  const last = useRef<{ v: T } | null>(null);
  const get = () => { const v = select(state); if (last.current && shallowEq(last.current.v, v)) return last.current.v; last.current = { v }; return v; };
  return useSyncExternalStore(subscribe, get, get);
}

export const now = () => new Date().toISOString();
export const uid = (p: string) => `${p}_${Math.random().toString(36).slice(2, 10)}`;
```
  </details>

- 🔧 `Bash`: Stabilise selectors

  <details><summary>result</summary>

```
journeys/talent-d/Improve.tsx:6:import { actorOf, useWorld, visibleEvidence } from '../../mock/world';
journeys/talent-d/Learn.tsx:6:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/Learn.tsx:19:  const saved = useWorld((w) => tdRead(w).learn[pid]?.[r.id]);
journeys/talent-d/Letter.tsx:7:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/Recovery.tsx:6:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/Work.tsx:8:import { actorOf, useWorld, visibleEvidence } from '../../mock/world';
journeys/talent-d/WorkPermit.tsx:6:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/motions.tsx:6:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/motions.tsx:11:  const lite = useWorld((w) => { const a = actorOf(w); return !!(a.personId && w.consents[a.personId]?.lite); });
journeys/talent-d/refs.tsx:3:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/refs.tsx:11:  const me = useWorld((w) => actorOf(w).personId);
journeys/talent-d/refs.tsx:12:  const l = useWorld((w) => letterOf(w, pid, jobId));
journeys/talent-d/refs.tsx:23:  const me = useWorld((w) => actorOf(w).personId);
journeys/talent-d/refs.tsx:24:  const au = useWorld((w) => authOf(w, id));
journeys/talent-d/refs.tsx:25:  const names = useWorld((w) => liveShares(authOf(w, id)).map((r) => orgNm(w, r.org)));
journeys/talent-d/ui.tsx:7:import { actorOf, useWorld } from '../../mock/world';
journeys/talent-d/ui.t
… [665 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Attach refs, typecheck, start vite on 5216

  <details><summary>result</summary>

```
VITE v5.4.21  ready in 904 ms

  ➜  Local:   http://localhost:5216/
  ➜  Network: use --host to expose
```
  </details>

- 🔧 `Bash`: Smoke-render all pages at desktop and phone

  <details><summary>result</summary>

```
d 01-permit overflow 0
d 02-critique overflow 0
d 03-versions overflow 0
d 04-letter overflow 0
d 05-learn overflow 0
d 06-improve overflow 0
d 07-recovery overflow 0
d 08-apps overflow 0
d 09-home overflow 0
m 01-permit overflow 0
m 02-critique overflow 0
m 03-versions overflow 0
m 04-letter overflow 0
m 05-learn overflow 0
m 06-improve overflow 0
m 07-recovery overflow 0
m 08-apps overflow 0
m 09-home overflow 0
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/shots/d-01-permit.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/shots/d-03-versions.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/shots/d-05-learn.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/shots/m-07-recovery.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:54

[Image: original 780x3286, displayed at 475x2000. Multiply coordinates by 1.64 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/shots/d-04-letter.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/shots/m-02-critique.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:54

[Image: original 780x2682, displayed at 582x2000. Multiply coordinates by 1.34 to map to original image.]

- 🔧 `Skill`: {"skill": "design-skills:design-critique", "args": "Critique first renders of TALENT-D pages (work permit, critique, versions, cover note, learning player, improve wizard, recovery) at 1440 and 390; f

  <details><summary>result</summary>

```
Launching skill: design-skills:design-critique
```
  </details>


**User** · 2026-10-30 12:54

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
… [3268 more characters trimmed]

- 🔧 `Bash`: Save before captures as review pairs

  <details><summary>result</summary>

```
01-before.png
02-before.png
03-before.png
04-before.png
05-before.png
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:accessibility-audit", "args": "Audit the simulated learning player at /c/learn/:id (custom controls: play/pause, -10s, range scrubber with aria-valuetext, captions and transcr

  <details><summary>result</summary>

```
Launching skill: design-skills:accessibility-audit
```
  </details>


**User** · 2026-10-30 12:54

Base directory for this skill: /root/.claude/plugins/synced/984c2541-5a3e-4beb-9e61-09c6216455d3_f137893c-a550-4c6d-9926-27e8f1b687a9/64191f50-3277-408e-9eca-3ef47f62a254/skills/accessibility-audit

# Accessibility Audit

You are an expert in web accessibility and WCAG 2.2 conformance. You help teams audit digital products, identify barriers, write compliant code, and build inclusive experiences.

Your work is grounded in WCAG 2.2, WebAIM guidelines, and the four principles of accessibility: Perceivable, Operable, Understandable, and Robust (POUR).

## Core Principle

Accessibility is not a feature — it is a baseline quality requirement. Good accessibility benefits all users, not just those with disabilities. Every interaction you design or code should work for people using keyboards, screen readers, voice control, switch devices, and magnification.

---

## WCAG Conformance Levels

| Level | What It Means | Legal Requirement | Target |
|---|---|---|---|
| **A** | Minimum — removes the most severe barriers | Usually required by law | Absolute floor |
| **AA** | Standard — addresses the majority of barriers | Most common legal standard (ADA, EN 301 549, EAA) | **Default target for all projects** |
| **AAA** | Enhanced — highest level of accessibility | Rarely required by law; aspirational | Specific content or features |

**Rule of thumb:** Target AA conformance for everything. Apply AAA criteria where practical, especially for text content, color contrast, and target sizes.

### What's New in WCAG 2.2 (vs 2.1)

| Criterion | Level | What It Adds |
|---|---|---|
| 2.4.11 Focus Not Obscured (Minimum) | AA | Focused element must not be entirely hidden by sticky headers/modals |
| 2.4.12 Focus Not Obscured (Enhanced) | AAA | Focused element must be fully visible |
| 2.4.13 Focus Appearance | AAA | Custom focus indicators must meet size and contrast requirements |
| 2.5.7 Dragging Movements | AA | Drag operations must have non-drag alternatives |
| 2.5.8 Target Size (Minimum) | AA | Touch targets at least 24×24px (or spaced to avoid overlap) |
| 3.2.6 Consistent Help | A | Help mechanisms must appear in consistent locations |
| 3.3.7 Redundant Entry | A | Don't ask users to re-enter information in a single session |
| 3.3.8 Accessible Authentication (Minimum) | AA | No cognitive function tests (CAPTCHAs, puzzles) without alternatives |
| 3.3.9 Accessible Authentication (Enhanced) | AAA | Stricter authentication requirements |

---

## How to Run an Accessibility Audit

### The 5-Layer Audit Process

Run these layers in order. Each layer catches different types of issues.

#### Layer 1: Automated Scan (10 minutes)

Run automated tools first — a single automated scan catches ~30-40% of WCAG issues instantly. (A full automated *stack* — linting + axe tests + keyboard assertions in CI — reaches ~70-85%; see `references/testing-tools-and-techniques.md`. Either way, the rest needs manual keyboard and screen reader testing.)

**Tools:**
- **axe DevTools** (browser extension) — Industry standard, low false-positive rate
- **WAVE** (browser extension) — Visual overlay showing issues in context
- **Lighthouse** (Chrome DevTools → Accessibility) — Quick score with issue list
- **Pa11y** (CLI) — CI/CD integration for automated regression testing

**What automated tools catch:** Missing alt text, color contrast failures, missing labels, incorrect ARIA, heading hierarchy issues, missing lang attribute, empty buttons/links.

**What automated tools miss:** Whether alt text is meaningful, keyboard trap detection, logical focus order, whether error messages are helpful, content comprehension, screen reader announcement quality.

#### Layer 2: Keyboard Navigation (15 minutes)

Put your mouse away. Navigate the entire page/flow using only the keyboard.

| Key | Action |
|---|---|
| `Tab` | Move to next interactive element |
| `Shift + Tab` | Move to previous interactive element |
| `Enter` | Activate link or button |
| `Space` | Activate button, toggle checkbox, open select |
| `Arrow keys` | Navigate within components (tabs, menus, radio groups) |
| `Escape` | Close modal, dismiss popover |

**Check for:**
- [ ] Can you reach every interactive element?
- [ ] Is the focus order logical (left-to-right, top-to-bottom)?
- [ ] Is focus always visible? (look for a clear outline or highlight)
- [ ] Can you operate every control (buttons, links, dropdowns, tabs, modals)?
- [ ] Can you escape from modals and popovers?
- [ ] Are you ever trapped (can't Tab away from an element)?
- [ ] Does focus go to the right place after actions (modal open, form submit, delete)?
- [ ] Is the focused element ever hidden behind a sticky header or modal?

#### Layer 3: Screen Reader Testing (20 minutes)

Test with at least one screen reader. VoiceOver (macOS) or NVDA (Windows) are free.

**VoiceOver quick start (macOS):**
- `Cmd + F5` — Toggle VoiceOver on/off
- `VO + Right Arrow` — Move to next element (`VO` = `Ctrl + Option`)
- `VO + Space` — Activate element
- `VO + U` — Open rotor (headings, links, landmarks)

**Check for:**
- [ ] Are images announced with meaningful descriptions?
- [ ] Are form fields announced with their labels?
- [ ] Are buttons and links announced with their purpose?
- [ ] Are headings properly nested (h1 → h2 → h3)?
- [ ] Are page landmarks present (banner, navigation, main, contentinfo)?
- [ ] Are status messages announced (success, error, loading)?
- [ ] Are decorative images hidden from screen readers?
- [ ] Do custom components announce their role and state?

#### Layer 4: Visual and Content Review (15 minutes)

Inspect visual presentation and content quality.

**Color and contrast:**
- [ ] Text contrast ≥ 4.5:1 (or ≥ 3:1 for large text: 18pt+ or 14pt+ bold)
- [ ] Non-text contrast ≥ 3:1 (icons, borders, focus indicators, chart elements)
- [ ] Color is never the only way to convey information (add icons, patterns, or text)
- [ ] Links are distinguishable from body text (underline, or 3:1 contrast + hover/focus change)

**Text and readability:**
- [ ] Text is resizable to 200% without loss of content or function
- [ ] Page reflows at 320px width (400% zoom) without horizontal scrolling
- [ ] Text spacing can be increased (line-height 1.5×, paragraph spacing 2×, word spacing 0.16×, letter spacing 0.12×) without breaking layout
- [ ] Content is written at appropriate reading level

**Interactive elements:**
- [ ] Touch targets are at least 24×24px (AA) or 44×44px (AAA)
- [ ] Hover/focus content is dismissible (Esc), hoverable, and persistent
- [ ] Drag operations have non-drag alternatives

#### Layer 5: Flow and Context Testing (15 minutes)

Test complete user flows, not just individual pages.

- [ ] Forms: Are errors identified, described, and easy to fix?
- [ ] Forms: Are required fields indicated before submission?
- [ ] Forms: Is redundant entry avoided (don't ask for the same info twice)?
- [ ] Authentication: Can users log in without cognitive function tests?
- [ ] Navigation: Is help consistently placed across pages?
- [ ] Navigation: Are skip links present?
- [ ] Navigation: Are multiple ways to find content available (search, nav, sitemap)?
- [ ] Time limits: Can users extend, adjust, or turn off time limits?
- [ ] Media: Do videos have captions? Audio-only has transcripts?
- [ ] Motion: Can animations be paused? Is `prefers-reduced-motion` respected?

---

## Severity Scoring

Score each issue to prioritize fixes.

### Impact Scale

| Severity | Definition | Example |
|---|---|---|
| **Critical** | Completely blocks access for some users. Legal risk. | Missing form labels (screen reader users can't fill forms), keyboard trap |
| **High** | Significantly impairs use. Major frustration. | Poor contrast on primary text, no skip navigation, missing alt text on functional images |
| **Moderate** | Causes difficulty but workarounds exist. | Decorative images with non-empty alt text, inconsistent heading levels, low contrast on secondary UI |
| **Low** | Minor inconvenience. Best practice violation. | Missing lang on inline foreign text, suboptimal ARIA usage |

### WCAG Level as Priority Signal

| WCAG Level | Default Priority |
|---|---|
| **A violations** | Critical or High — these are the floor |
| **AA violations** | High or Moderate — the standard target |
| **AAA violations** | Moderate or Low — aspirational improvements |

### Triage Framework

| Tier | Criteria | Action |
|---|---|---|
| **Tier 1** | Critical/High + Level A or AA | Fix immediately — before next release |
| **Tier 2** | Moderate + Level AA | Fix in current or next sprint |
| **Tier 3** | Low + Level AAA or best practice | Add to backlog |

---

## The 80/20: Most Common Issues

These 10 issues account for the vast majority of accessibility failures (based on WebAIM Million analysis). Fix these first.

| # | Issue | WCAG | Level | Frequency |
|---|---|---|---|---|
| 1 | Low text contrast | 1.4.3 | AA | 83% of pages |
| 2 | Missing alt text on images | 1.1.1 | A | 55% of pages |
| 3 | Missing form input labels | 1.1.1, 1.3.1 | A | 46% of pages |
| 4 | Empty links (no text) | 2.4.4 | A | 44% of pages |
| 5 | Empty buttons (no text) | 2.4.4 | A | 27% of pages |
| 6 | Missing document language | 3.1.1 | A | 18% of pages |
| 7 | Missing or broken skip navigation | 2.4.1 | A | Common |
| 8 | No visible focus indicator | 2.4.7 | AA | Common |
| 9 | Incorrect heading hierarchy | 1.3.1 | A | Common |
| 10 | Inaccessible custom components (no ARIA) | 4.1.2 | A | Common |

For code fixes for each of these, see `references/common-issues-and-fixes.md`.

---

## Semantic HTML: The Foundation

Semantic HTML gives you ~70% of accessibility for free. Before reaching for ARIA, use the right HTML element.

| Instead of... | Use... | Why |
|---|---|---|
| `<div onclick="...">` | `<button>` | Gets keyboard support, role, and focus for free |
| `<span class="link">` | `<a href="...">` | Announced as link, keyboard navigable |
| `<div class="header">` | `<header>`, `<nav>`, `<main>`, `<footer>` | Creates landmarks for screen reader navigation |
| `<div class="heading">` | `<h1>` – `<h6>` | Creates heading hierarchy for navigation |
| `<div class="list">` | `<ul>`, `<ol>`, `<li>` | Announced as list with item count |
| `<div class="table">` | `<table>`, `<th>`, `<td>` | Associates headers with data cells |
| `<div class="input">` | `<input>`, `<select>`, `<textarea>` | Native form behavior, labels, validation |

**The first rule of ARIA:** Don't use ARIA if native HTML can do the job. ARIA overrides native semantics and is easy to get wrong.

---

## Quick Audit Checklist (For Code Reviews)

Use this during pull requests to catch issues before they ship.

### HTML Structure
- [ ] Page has one `<h1>`, headings don't skip levels
- [ ] `<html lang="...">` is set
- [ ] Landmarks present: `<header>`, `<nav>`, `<main>`, `<footer>`
- [ ] Skip link targets `<main>` or primary content area
- [ ] Semantic elements used (not `<div>` for everything)

### Images
- [ ] Functional images have descriptive `alt` text
- [ ] Decorative images have `alt=""` or are CSS backgrounds
- [ ] Complex images (charts, diagrams) have extended descriptions

### Forms
- [ ] Every input has a visible `<label>` (or `aria-label` if visually hidden)
- [ ] Required fields are indicated (not by color alone)
- [ ] Error messages identify the field and describe the error
- [ ] `autocomplete` attributes set for personal data fields
- [ ] Related fields grouped with `<fieldset>` and `<legend>`

### Interactive Elements
- [ ] All functionality available via keyboard
- [ ] Focus order matches visual order
- [ ] Focus indicator is visible (not `outline: none` without replacement)
- [ ] Custom components have correct ARIA roles, states, and properties
- [ ] Modals trap focus and return focus on close

### Color and Contrast
- [ ] Text contrast ≥ 4.5:1 (≥ 3:1 for large text)
- [ ] UI component contrast ≥ 3:1
- [ ] Information not conveyed by color alone

### Dynamic Content
- [ ] Status messages use `aria-live` or `role="alert"`
- [ ] Loading states are announced
- [ ] Content added to the DOM is reachable by keyboard and screen reader

---

## Reference Files

- `references/wcag-checklist.md` — Complete WCAG 2.2 checklist organized by audit task (what to check, not WCAG principle order)
- `references/common-issues-and-fixes.md` — Top 15 issues with before/after code examples
- `references/testing-tools-and-techniques.md` — Automated tools, static analysis (linting), manual techniques, screen reader commands, CI gating

## Templates

- `templates/audit-report-template.md` — Full audit report with executive summary, findings, and prioritized recommendations
- `templates/quick-checklist-template.md` — Single-page checklist for sprint reviews or PR reviews
- `templates/accessibility-rules-file.md` — Drop-in constraints block for AI coding agents (CLAUDE.md, .cursorrules, copilot-instructions.md) to generate accessible UI by default

## Examples

- `examples/audit-walkthrough.md` — End-to-end audit of a fictional e-commerce checkout page
- `examples/quick-wins.md` — The fixes that solve the most common accessibility problems with minimal effort


ARGUMENTS: Audit the simulated learning player at /c/learn/:id (custom controls: play/pause, -10s, range scrubber with aria-valuetext, captions and transcript toggles with aria-pressed, focusable screen region with Space/arrow/C keys, live caption region) and the consent-receipt share rows, against WCAG 2.2 AA.

- 🔧 `Bash`: Apply critique fixes and re-render

  <details><summary>result</summary>

```
Command did not complete within its 120s timeout and was moved to the background (ID: b9sh7jqdb). Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b9sh7jqdb.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. No output had been read from it when it was moved. A program that buffers its output, or a pipe into one such as tail, can keep the output file empty until the command finishes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Run TALENT-D feature test on desktop

  <details><summary>result</summary>

```
PASS [d] SC-071 empty state: nothing stated, private, never hides jobs
PASS [d] SC-071 sharing is disabled until something is stated
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-canvas').last().getByRole('button', { name: 'I would need a permit or visa' }).first()[22m

    at click (/home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:36:110)
    at /home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:49:9 {
  log: [
    "  - waiting for locator('.ds-canvas').last().getByRole('button', { name: 'I would need a permit or visa' }).first()"
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Fix radio locators and rerun desktop

  <details><summary>result</summary>

```
FAIL [d] SC-071 Q understands a stated right to work and offers to save it (private) · I’m not sure I understood that, and I don’t want to guess. In this prototype my understanding is limited to hiring and career tasks. Could you say it another way, or pick one of these?
FAIL [d] SC-071 shared only with the chosen employer, with a consent receipt
FAIL [d] SC-076 Q critiques kindly: strengths first, then concrete points
FAIL [d] SC-077 compare two versions shows Was and Now · ¶3
WAS There are many reasons prices go up such as inflation, transport, the exchange rate, weather and also demand. All
FAIL [d] SC-077 restoring adds a version; nothing is deleted
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-canvas').last().getByRole('button', { name: 'Give them version 5' }).first()[22m

    at click (/home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:36:110)
    at /home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:133:9 {
  log: [
    "  - waiting for locator('.ds-canvas').last().getByRole('button', { name: 'Give them version 5' }).first()"
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Fix test locators and citizen matching; rerun

  <details><summary>result</summary>

```
dbg {"id":"TQ-1002-0OKC","what":"Work authorisation statement","org":"org_kora","at":"2026-10-30T13:00:59.853Z"}
FAIL [d] SC-092 video is labelled simulated, with captions on by default
FAIL [d] MO-052 shared only after a consent receipt (receipt event precedes the share)
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: SyntaxError: Identifier 'a' has already been declared
    at new Function (<anonymous>)
    at eval (eval at evaluate (:311:30), <anonymous>:1:41)
    at Object.update (http://localhost:5216/src/mock/world.ts:81:16)
    at eval (eval at evaluate (:311:30), <anonymous>:1:27)
    at UtilityScript.evaluate (<anonymous>:313:16)
    at UtilityScript.<anonymous> (<anonymous>:1:44)
    at upd (/home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:25:34)
    at /home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:270:9 {
  log: []
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Fix test and rerun desktop

  <details><summary>result</summary>

```
dbg52 true [ 'org_tinda' ] true true
FAIL [d] MO-052 shared only after a consent receipt (receipt event precedes the share)
FAIL [d] MO-030 opened later, it is simply the loaded document

95/97 passed
```
  </details>

- 🔧 `Bash`: Rerun full desktop and phone

  <details><summary>result</summary>

```
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: Execution context was destroyed, most likely because of a navigation
    at lastQ (/home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:34:28)
    at ask (/home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:35:173)
    at async file:///home/user/neo/talent-q-design/qa/scripts/features/talent-d.mjs:75:14 {
  log: [],
  name: 'Error'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Make ask robust and run phone

  <details><summary>result</summary>

```
97/97 passed
```
  </details>

- 🔧 `Bash`: Start regression runs in background

  <details><summary>result</summary>

```
8:// Usage: BASE=http://localhost:4190/ node J12.mjs   [VIDEO_DIR=dir FILM_PACE=ms to record the film] [ONLY=d|m]
13:const BASE = (process.env.BASE || 'http://localhost:4190/').replace(/\/?$/, '/');
42:  const as = async (id, route) => { await closeQ(); await page.goto(`${BASE}?n=${Math.random()}#${route}${route.includes('?') ? '&' : '?'}as=${id}`); await page.waitForSelector('.ds-app'); await sleep(900); };
4:const BASE = process.argv[2] || 'http://localhost:4174/';
8:await page.goto(`${BASE}#/settings`); await page.evaluate(() => localStorage.clear()); await page.reload(); await page.waitForTimeout(700);
started
```
  </details>

- 🔧 `Bash`: Check background runs are alive

  <details><summary>result</summary>

```
1661 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1793355909182-v0rwog.sh 2>/dev/null || true && \builtin export BUN_OPTIONS="--smol${BUN_OPTIONS:+ $BUN_OPTIONS}" && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'which'; \builtin unset -f -- 'which'; } >/dev/null 2>&1 || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /home/user/neo/talent-q-design; B=http://localhost:5216/; O=/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/runs; mkdir -p $O; head -5 qa/scripts/journeys/J12.mjs | grep -i usage; grep -n "argv\|BASE" qa/scripts/journeys/J12.mjs | head -3; grep -n "argv\|BASE" qa/scripts/review/privacy.mjs | head -3 (BASE=$B node qa/scripts/features/talent-d.mjs > $O/td.log 2>&1; node qa/scripts/review/privacy.mjs $B > $O/privacy.log 2>&1; BASE=$B node qa/scripts/features/evidence-candidate.mjs > $O/evc.log 2>&1) & echo started' < /dev/null && pwd -P >| /tmp/claude-92ef-cwd
1662 node qa/scripts/features/talent-d.mjs
1838 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1793355909182-v0rwog.sh 2>/dev/null || true && \builtin export BUN_OPTIONS="--smol${BUN_OPTIONS:+ $BUN_OPTIONS}" && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'which'; \builtin unset -f -- 'which'; } >/dev/null 2>&1 || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'sleep 5; pgrep -af "tale
… [75 more characters trimmed]
```
  </details>


**Claude** · 2026-10-30 13:07

Alive. Meanwhile start the journey runs (J12, T1–T5) in the background.

- 🔧 `Bash`: Run J12 and T1–T5 journey regressions

  <details><summary>result</summary>

```
Command running in background with ID: b6h8pjlgg. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b6h8pjlgg.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Copy after captures into pairs
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/td/after/m-02-critique.png

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
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 13:07

[Image: original 780x2682, displayed at 582x2000. Multiply coordinates by 1.34 to map to original image.]

- 🔧 `Bash`: Write registry patch and check regression progress

  <details><summary>result</summary>

```
Exit code 1
tail: option used in invalid context -- 3
```
  </details>

- 🔧 `Bash`: Check regression progress

  <details><summary>result</summary>

```
== scratchpad/td/runs/J12.log
PASS [d] 6 A respectful request: why, 40 minutes, and three choices
PASS [d] 7 Submitted: “Self-reported, waiting for review”
PASS [d] 7 The Passport uses the same proof words Ada sees
== scratchpad/td/runs/td.log
PASS [d] SC-092 the same lesson as an article
PASS [d] SC-092 practical exercise with kind feedback
PASS [d] SC-092 finishing is private and isn’t proof (no evidence added)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/talent-d.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/talent-d.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Wait for td, privacy and evidence-candidate runs

  <details><summary>result</summary>

```
194/194 passed
==
21
PASS Zara withdrew from Kora: nothing visible despite her application
PASS no page errors
All privacy checks passed
==
· what this means
Claim
?
· what this means

Your CV names 5 of the 5 things Kora Pay is looking for. Every CV line is read as a claim, for everyone, and that isn’t doubt about yours. A reviewe

126/126 passed
```
  </details>

- 🔧 `Bash`: Wait for journey regressions to finish

  <details><summary>result</summary>

```
J12 exit=0 pass=71 fail=0
T1 exit=1 pass=74 fail=2
T2 exit=0 pass=62 fail=0
T3 exit=0 pass=54 fail=0
T4 exit=0 pass=43 fail=0
T5 exit=0 pass=52 fail=0

[exited with code 0]
```
  </details>

- 🔧 `Bash`: Show T1 failures

  <details><summary>result</summary>

```
25:FAIL [d] Need-by-need explanation with her own words · Graduate Data Assistant at Tinda asks for 3 things. Spreadsheets: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof yet. Survey analysis: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof 
63:FAIL [m] Need-by-need explanation with her own words · Graduate Data Assistant at Tinda asks for 3 things. Spreadsheets: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof yet. Survey analysis: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof
```
  </details>

- 🔧 `Bash`: Inspect T1 failing step

  <details><summary>result</summary>

```
130-  w = await world();
131-  step('Matches from real listings, as claims not promises', /Graduate Data Assistant|Operations Trainee/.test(r) && /can’t promise/.test(r), r);
132-  await closeQ(); await shot('08-matches');
133-  r = await ask('why does the tinda graduate data assistant job fit me');
134:  step('Need-by-need explanation with her own words', /Spreadsheets: mentioned/.test(r) && /Survey analysis: mentioned/.test(r) && /Clear writing: not shown/.test(r), r);
FAIL [d] Need-by-need explanation with her own words · Graduate Data Assistant at Tinda asks for 3 things. Spreadsheets: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof yet. Survey analysis: mentioned (you said: “My final year project was on food prices in ogbete market, I…”), a claim, not proof
```
  </details>

- 🔧 `Bash`: See what T1 says for Clear writing

  <details><summary>result</summary>

```
3:// person said it (CV or conversation); otherwise "not shown". Fit is never a promise of anything.
12:  'Clear writing': ['report', 'wrote', 'write-up', 'essay', 'thesis', 'brief'], 'Written clarity': ['report', 'wrote', 'write-up', 'essay', 'brief'],
```
  </details>

- 🔧 `Bash`: Check whether matching reads Passport evidence

  <details><summary>result</summary>

```
2:// A need is "evidenced" only by a Passport item that isn't a claim or practice; "mentioned" when the
18:export type NeedState = 'evidenced' | 'mentioned' | 'none';
26:  const ev = w.evidence.find((e) => e.ownerId === pid && e.kind !== 'CLAIM' && e.kind !== 'PRACTICE' && kws.some((k) => `${e.title} ${e.shows}`.toLowerCase().includes(k.trim())));
27:  if (ev) return { need, state: 'evidenced', basis: `${ev.title} (${ev.verification === 'VERIFIED' ? 'checked' : 'in your Passport'})` };
```
  </details>

- 🔧 `Bash`: Read need keywords

  <details><summary>result</summary>

```
export const NEED_KWS: Record<string, string[]> = {
  'SQL': ['sql'], 'Dashboards': ['dashboard', 'power bi', 'tableau', 'chart'], 'Product writing': ['brief', 'memo', 'product writing'],
  'Spreadsheets': ['excel', 'google sheets', 'spreadsheet', 'pivot'], 'Spreadsheet modelling': ['excel', 'google sheets', 'spreadsheet', 'model', 'tracker'],
  'Statistics': ['statistic', 'econometric', 'regression', 'spss', 'stata'], 'Survey analysis': ['survey', 'questionnaire'],
  'Clear writing': ['report', 'wrote', 'write-up', 'essay', 'thesis', 'brief'], 'Written clarity': ['report', 'wrote', 'write-up', 'essay', 'brief'],
  'Process mapping': ['process map', 'process mapping', 'workflow', 'flowchart'], 'Stakeholder conversations': ['interviewed', 'interview', 'committee', 'retail accounts', 'clients', 'stakeholder'],
  'User research': ['user research', 'interviewed', 'survey', 'questionnaire'], 'Team leadership': ['led a team', 'team lead', 'captain', 'president'],
  'Care experience': ['care assistant', 'caring'], 'Rota planning': ['rota'], 'First aid': ['first aid'],
  'Go in production': ['golang', ' go '], 'Postgres at scale': ['postgres'], 'Payments systems': ['payments'], 'Logistics systems': ['logistics'], 'Go': ['golang'], 'Incident leadership': ['incident'],
```
  </details>

- 🔧 `Bash`: Rename seeded item and rerun T1

  <details><summary>result</summary>

```
10:    ev({ evidenceId: 'e_amaka_prices', ownerId: 'p_amaka', kind: 'WORK_SAMPLE', title: 'Mile 12 food prices project', source: 'Uploaded by Amaka Eze', observedAt: '2026-10-12', verification: 'UNVERIFIED',
76
[This command modified 1 file you've previously read: state/seeds/talent-d.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Final typecheck and changed files

  <details><summary>result</summary>

```
M captures/cx/J11/d-01-briefing.png
 M captures/cx/J11/d-02-contact-policy.png
 M captures/cx/J11/d-03-filed.png
 M captures/cx/J11/d-04-campaign.png
 M captures/cx/J11/d-05-rubric-proposed.png
 M captures/cx/J11/d-06-rubric-approved.png
 M captures/cx/J11/d-07-consent.png
 M captures/cx/J11/d-08-unsafe-link.png
 M captures/cx/J11/d-09-upload-paused.png
 M captures/cx/J11/d-10-shared.png
 M captures/cx/J11/d-11-evidence-report.png
 M captures/cx/J11/d-12-reviewed.png
 M captures/cx/J11/d-13-change-notice.png
 M captures/cx/J11/d-14-approval.png
 M captures/cx/J11/d-15-auth-expired.png
 M captures/cx/J11/d-16-reconnect-consent.png
 M captures/cx/J11/d-17-candidate-reply.png
 M captures/cx/J11/d-18-reply-intelligence.png
 M captures/cx/J11/d-19-booked.png
 M captures/cx/J11/m-14-approval.png
 M captures/cx/J11/m-18-reply-intelligence.png
 M captures/cx/J11/m-19-booked.png
 M captures/cx/J12/d-05-sample-sent.png
 M captures/cx/J12/d-07-candidate-sample.png
 M captures/cx/J12/d-08-candidate-passport.png
 M captures/cx/J12/d-09-review.png
 M captures/cx/J12/d-10-both-interview.png
 M captures/cx/J12/d-12-invite.png
 M captures/cx/J12/d-13-candidate-gap.png
 M captures/cx/J12/d-14-after-revoke.png
```
  </details>

- 🔧 `Bash`: Stop the vite server on port 5216

  <details><summary>result</summary>

```
Exit code 144
```
  </details>

- 🔧 `SubagentHandback`: {"message": "TALENT-D is built: 7 screens and 6 motions. My feature test passes 194 of 194 steps (desktop and phone), and the checks you asked me to keep green all pass: privacy, evidence-candidate (1

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
