# Helper agent agent-a0623f58bf86d9efb: Org governance and admin screens

Source: `agent-a0623f58bf86d9efb.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-30 12:27

You are the ORG-ADMIN builder for Talent Q's design prototype (/home/user/neo/talent-q-design/prototype). First read `/home/user/neo/talent-q-design/journeys/COVERAGE-BUILD-BRIEF.md` and follow it exactly. Your name for files is `org-admin`, and your vite port is 5212.

**Atlas screens:**
- SC-020 Recruiter personal instructions
- SC-021 Organization approved templates
- SC-023 Channel verification
- SC-024 Employer billing and usage
- SC-025 Compliance and retention settings
- SC-140 Agency placement and invoice status
- SC-141 Enterprise compliance dashboard
- SC-142 Enterprise organization reports
- SC-144 Model and scoring version inspector
- SC-145 Bias and assessment quality dashboard
- SC-146 Source license and connectivity manager

**Vision groups:**
- **V03** (low-latency, cheap provider orchestration): show in the model inspector which simulated model and provider route each Q task uses, with budget, timeout and fallback. Label it simulated.
- **V09** (WhatsApp and conventional calling): channel verification and consent for WhatsApp, SMS and phone. Show a simulated WhatsApp-channel message state, using the existing correspondence model where possible. Don't fork M9; read `journeys/hire-c/lib.ts`.
- **V29** (Q improves with users and results): a learning and evaluation view of what Q has learned, from which consented outcomes. Reviewers can approve or reject a learning. Nothing private is used without permission.

**Motion:** MO-035 (agent budget warning), for usage and billing limits.

**Constraints:**
- Billing amounts follow the pricing hypotheses and are labelled. Take no payment.
- The bias and quality dashboard must not invent fairness statistics. Show which checks would run and their status (not yet validated, simulated sample), consistent with D17.
- Retention follows D9.
- Agency and employer tenancy stays separate: Dele sees Talentbridge only, and Kora admins see Kora only. Bayo, as hiring manager, sees less than Ada.

Look at existing settings, team and audit pages (`/r/team`, `/r/setup`, `/r/audit`, `/settings`, `/settings/email`), and extend beside them rather than duplicating them.

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

- 🔧 `Bash`: Explore repo layout

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

prototype:
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

prototype/src/st
… [914 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List area, seed, q and journey files
- 🔧 `Bash`: Locate the screen atlas csv

  <details><summary>result</summary>

```
q/QPresence.tsx
q/QThread.tsx
q/RunConversation.tsx
q/refs.ts
q/scripts.ts
q/slots.ts

journeys/agency:
model.ts
pages.tsx

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
agency.ts
campaigns.ts
core.ts
email.ts
evidence-candidate.ts
evidence-ops.ts
evidence.ts
hire-a.ts
hire-b.ts
hire-c.ts
hiring-basic.ts
media.ts
rubric.ts
talent-a.ts
talent-b.ts
talent-c.ts

routes:
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

state/areas:
README.md
agency.ts
campaigns.ts
hire-a.ts
hire-b.ts
hire-c.ts
mail.ts
media.ts
proof.ts
rubrics.ts
talent-a.ts
talent-b.ts
talent-c.ts

state/seeds:
agency.ts
hire-a.ts
hire-b.ts
hire-c.ts
media.ts
proof.ts
talent-a.ts
talent-b.ts
talent-c.ts
    49 routes/agency.tsx
    28 routes/campaigns.tsx
     6 routes/core.tsx
   241 routes/entry.tsx
     6 routes/gallery.tsx
    21 routes/guard.tsx
    34 routes/hire-a.tsx
    17 routes/hire-b.tsx
    30 routes/hire-c.tsx
     7 routes/media.tsx
    18 routes/talent-a.tsx
   
… [755 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/wthead/docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/wt/docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/wt2/docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/gpt/Talent-Q-Complete/founder-sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/wtlead/docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
/home/user/neo/docs/sources/batch-2/02_COMPLETE_SCREEN_ATLAS_v2.csv
```
  </details>

- 🔧 `Bash`: Read my atlas rows, motion and vision rows

  <details><summary>result</summary>

```
screen_id,section,screen_name,primary_actor,must_show,fidelity,variants,backend_boundary,desktop_and_mobile,source
SC-020,Employer onboarding & governance,Recruiter personal instructions,Employer,"User-level tone, process and limits",Prototype,loading; ready; empty; error; permission denied; accessible alternative; mobile,Domain read/action + permission,Both; may reuse layout variants,Founder vision + audited product research
SC-021,Employer onboarding & governance,Organization approved templates,Employer,"Reusable JD, email, question, scorecard templates",Prototype,loading; ready; empty; error; permission denied; accessible alternative; mobile,Domain read/action + permission,Both; may reuse layout variants,Founder vision + audited product research
SC-023,Employer onboarding & governance,Channel verification,Employer,"Email, SMS, WhatsApp, voice rights and opt-in",Atlas,loading; ready; empty; error; permission denied; accessible alternative; mobile,Domain read/action + permission,Both; may reuse layout variants,Founder vision + audited product research
SC-024,Employer onboarding & governance,Employer billing and usage,Employer,"Subscription, quota, costs, budget approvals",Atlas,loading; ready; empty; error; permission denied; accessible alternative; mobile,Domain read/action + permission,Both; may reuse layout variants,Founder vision + audited product research
SC-025,Employer onboarding & governance,Compliance and retention settings,Employer,"Jurisdiction templates, del
… [2949 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read routes and registry

  <details><summary>result</summary>

```
// Routes for R4 (Dele, Talentbridge agency). Owned by this area (see journeys/BUILD-BRIEF.md).
// Information architecture: the rail carries the six top destinations (Clients, Talent pools, Submittals,
// Campaigns, Agents, Client reports). Secondary pages nest under their parent path (pools/searches,
// pools/compare, clients/notes, clients/docs, clients/mandate/:id) so the rail still marks where you are,
// and each section shows only its own secondary tabs in the page. Older flat paths redirect.
import { useEffect, type ReactNode } from 'react';
import { registerRoute } from './registry';
import { OrgOnly } from './guard';
import { registerRecruiterHome } from './entry';
import { actorOf, orgOf } from '../mock/world';
import type { IconName } from '../ds/icons';
import { AP, startRunner } from '../journeys/agency/model';
import { AgencyHome, Agents, Clients, Compare, Campaigns, Docs, MandatePage, Notes, Pools, Reports, Searches, Submittals } from '../journeys/agency/pages';
import '../styles/agency.css';

registerRecruiterHome((w) => orgOf(w, actorOf(w).orgId)?.kind === 'AGENCY', () => <AgencyHome />);

const guarded = (el: ReactNode) => <OrgOnly orgId="org_tb" what="Talentbridge’s agency workspace">{el}</OrgOnly>;
const nav = (label: string, icon: IconName, order: number, tab = false) => ({ group: 'Agency', label, icon, order, tab, orgKind: 'AGENCY' as const });
const page = (path: string, label: string, render: (p: Record<string, string>) => ReactNode, n?: ReturnType<ty
… [8542 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read world store and domain types

  <details><summary>result</summary>

```
<persisted-output>
Output too large (32.4KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b4q439doz.txt

Preview (first 2KB):
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
  // ---- v4: one authoritative store for the whole prod
… [699 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List world and domain exports

  <details><summary>result</summary>

```
12:export interface ChatTurn { id: string; who: 'me' | 'q'; text: string; at: string; used?: ContextUse[]; runId?: string; link?: { label: string; to: string } }
14:export interface World {
62:/** Feature areas add their own seed records in src/state/seeds/*.ts (export const seed: SeedPatch). */
63:export interface SeedPatch { actors?: Actor[]; orgs?: Org[]; people?: Person[]; mandates?: MandateX[]; pipeline?: PipelineEntry[]; threads?: Thread[]; calendar?: CalEvent[]; interviews?: Interview[]; jobs?: Job[]; applications?: Application[]; evidence?: World['evidence']; memories?: World['memories']; events?: World['events']; registrations?: { personId: string; orgId: string }[] }
64:/** Feature areas with their own state register an initial slice in src/state/areas/*.ts (export const area). */
69:export function initialWorld(): World {
118:export function getWorld() { return state; }
120:export function update(fn: (w: World) => World | void) {
129:export function resetWorld() { update(() => initialWorld()); }
139:export function useWorld<T>(select: (w: World) => T): T {
145:export const now = () => new Date().toISOString();
146:export const uid = (p: string) => `${p}_${Math.random().toString(36).slice(2, 10)}`;
148:export function log(w: World, actor: World['activity'][number]['actor'], text: string) {
152:export function setSchedulingState(w: World, s: SchedulingState, note?: string) {
159:export function visibleMemories(w: World, viewer: 'recruiter' | 'candidate') {
169:export
… [7992 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read actor/org types and world init

  <details><summary>result</summary>

```
export type Side = 'recruiter' | 'candidate';
export type OrgRole = 'OWNER' | 'ADMIN' | 'RECRUITER' | 'HIRING_MANAGER' | 'INTERVIEWER' | 'VIEWER';
export type JourneyId = 'R1' | 'R2' | 'R3' | 'R4' | 'R5' | 'T1' | 'T2' | 'T3' | 'T4' | 'T5' | 'J12';

export interface Actor {
  id: string; name: string; first: string; initials: string; side: Side; title: string; timezone: string;
  orgId?: string; role?: OrgRole; journey?: JourneyId; email: string;
  /** Candidates: the person record in PEOPLE / people. */
  personId?: string;
  /** False until the person signs up in the prototype (R1, T1, T4 start signed out). */
  signedUp: boolean;
}

export interface Org {
  id: string; name: string; kind: 'EMPLOYER' | 'AGENCY'; industry: string; size: string; city: string;
  verified: { domain: boolean; registry: 'VERIFIED' | 'PENDING' | 'NONE' };
  delegation: 'DRAFT_ONLY' | 'APPROVE_EACH_SEND' | 'APPROVED_CAMPAIGN';
  /** Agencies only: client organisations they recruit for. */
  clients?: string[];
  setup: { done: boolean; step: number };
  guidelines: string[];
}

export interface World {
  v: 4;
  // ---- v4: one authoritative store for the whole product (see state/domain.ts) ----
  session: { actor: string; now: string; offsetDays: number; lastRoute: Record<string, string> };
  actors: Actor[];
  orgs: Org[];
  people: Person[];
  /** Mandates other than Kora's Senior Backend, which remains `mandate` for the original screens. */
  mandates: MandateX[];
  /** Per-area slices owned by 
… [12550 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read actors and orgs in seed

  <details><summary>result</summary>

```
9:  { id: 'u_funmi', name: 'Funmi Adebayo', first: 'Funmi', initials: 'FA', side: 'recruiter', title: 'Founder', timezone: 'Africa/Lagos', journey: 'R1', email: 'funmi@crumbandco.example', signedUp: false },
10:  { id: 'u_ada', name: 'Ada Okafor', first: 'Ada', initials: 'AO', side: 'recruiter', title: 'Talent partner', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'RECRUITER', journey: 'R2', email: 'ada@kora.example', signedUp: true },
11:  { id: 'u_ngozi', name: 'Ngozi Eze', first: 'Ngozi', initials: 'NE', side: 'recruiter', title: 'HR lead', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'ADMIN', journey: 'R3', email: 'ngozi@kora.example', signedUp: true },
12:  { id: 'u_seyi', name: 'Seyi Balogun', first: 'Seyi', initials: 'SB', side: 'recruiter', title: 'Engineering manager', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'HIRING_MANAGER', email: 'seyi@kora.example', signedUp: true },
13:  { id: 'u_musa', name: 'Musa Danladi', first: 'Musa', initials: 'MD', side: 'recruiter', title: 'Staff engineer', timezone: 'Europe/London', orgId: 'org_kora', role: 'INTERVIEWER', email: 'musa@kora.example', signedUp: true },
14:  { id: 'u_bayo', name: 'Bayo Ojo', first: 'Bayo', initials: 'BO', side: 'recruiter', title: 'Head of engineering', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'HIRING_MANAGER', journey: 'R5', email: 'bayo@kora.example', signedUp: true },
15:  { id: 'u_dele', name: 'Dele Martins', first: 'Dele', initials: 'DM', side: 'recruiter', title: 'Age
… [12932 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find audit and settings routes

  <details><summary>result</summary>

```
./q/skills/core.ts:24:  { side: 'recruiter', kws: ['audit', 'activity log', 'history of actions'], to: '/r/audit', label: 'the audit log' },
./q/skills/core.ts:35:  { side: 'recruiter', kws: ['settings', 'notifications', 'preferences'], to: '/settings', label: 'settings' },
./q/skills/core.ts:36:  { side: 'candidate', kws: ['settings', 'notifications', 'preferences', 'privacy'], to: '/settings', label: 'settings' },
./q/skills/talent-b.ts:435:    if (!Object.keys(p).length) return { msgs: [reply(`Right now: email ${cur.email ? 'on' : 'off'}, text messages ${cur.sms ? 'on' : 'off'}, in Talent Q ${cur.inApp ? 'on' : 'off'}, job digest ${cur.digest.toLowerCase()}. What would you like to change?`, { kind: 'question', actions: [{ label: 'Weekly email only', act: { t: 'say', text: 'only email me, weekly' } }, { label: 'No text messages', act: { t: 'say', text: 'stop texting me' } }, { label: 'Open settings', act: { t: 'nav', to: '/settings' } }] })] };
./q/skills/talent-b.ts:437:    return { msgs: [reply(`Done. Email ${nx.email ? 'on' : 'off'}, text messages ${nx.sms ? 'on' : 'off'}, in Talent Q ${nx.inApp ? 'on' : 'off'}, job digest ${nx.digest.toLowerCase()}. ${!nx.email && !nx.sms && !nx.inApp ? 'You’ll still see updates when you open Talent Q. ' : ''}I can’t filter by employer yet. You can change any of this in Settings.`, { used: ['Notification settings'], actions: [{ label: 'Undo', act: { t: 'say', text: 'undo' } }, { label: 'Open settings', act: { t: 'nav', to: '/settings' }
… [1356 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Team page

  <details><summary>result</summary>

```
// /r/team: members, roles and what each role can do. Only admins change roles; the last admin can't be removed.
import { actorOf, orgOf, simNow, useWorld } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { runAction } from '../../q/core/engine';
import type { OrgRole } from '../../state/domain';
import { city, IS_ADMIN, orgMembers, ROLE_LABEL, tTime } from './lib';

const ROLES: OrgRole[] = ['ADMIN', 'RECRUITER', 'HIRING_MANAGER', 'INTERVIEWER', 'VIEWER'];
export function Team() {
  const w = useWorld((x) => x);
  const a = actorOf(w);
  const admin = IS_ADMIN.includes(a.role ?? 'VIEWER');
  const mem = orgMembers(w, a.orgId);
  const nowIso = simNow(w).toISOString();
  const changes = w.events.filter((e) => e.type === 'team.role.changed' && e.scope === `ORG:${a.orgId}`).slice(-4).reverse();
  const caps: [string, (r: OrgRole) => boolean][] = [
    ['Approve and send messages', (r) => ['ADMIN', 'RECRUITER'].includes(r)],
    ['Draft messages with Q', (r) => ['ADMIN', 'RECRUITER', 'HIRING_MANAGER'].includes(r)],
    ['Move people between stages', (r) => ['ADMIN', 'RECRUITER', 'HIRING_MANAGER'].includes(r)],
    ['Arrange interviews and panels', (r) => ['ADMIN', 'RECRUITER', 'HIRING_MANAGER'].includes(r)],
    ['Give interview feedback', (r) => ['ADMIN', 'RECRUITER', 'HIRING_MANAGER', 'INTERVIEWER'].includes(r)],
    ['Change roles and guidelines', (r) => r === 'ADMIN'],
    ['Read pipelines and profiles', () => true],
  ];
  const short: Record<Or
… [3853 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read hire-c lib and Setup

  <details><summary>result</summary>

```
<persisted-output>
Output too large (61.2KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b42bg4x6b.txt

Preview (first 2KB):
// R3 logic shared by Q's skills and the pages: time zones, free/busy, slot finding, drafting templates,
// the pre-send checks (approval and delegation, candidate, calendar, guidelines, consent) and the simulated send.
// Nothing here really sends or books: statuses say SENT_SIMULATED and receipts are fake.
import { actorOf, emit, now, orgLimits, orgOf, outreachThisWeek, personOf, simNow, uid, type World } from '../../mock/world';
import { appendQ } from '../../q/core/engine';
import type { Actor, CalEvent, Msg, OrgRole, Stage, Thread } from '../../state/domain';
import { STAGE_LABEL } from '../../state/domain';
import { hc, hcw, type Check, type DraftKind, type DraftMeta, type Guide, type Slot, type Tone } from '../../state/areas/hire-c';
import { contentHash, defaultSender, emailChecks, providerSend } from './email';
import { mailboxOf } from '../../state/areas/mail';
import { campaignOf } from '../../state/areas/campaigns';

// ---------------- Time ----------------
export const LAGOS = 'Africa/Lagos';
const CITY: Record<string, string> = { 'Africa/Lagos': 'Lagos', 'Europe/London': 'London', 'Africa/Accra': 'Accra', 'Africa/Nairobi': 'Nairobi' };
export const city = (tz: string) => CITY[tz] ?? tz.split('/').pop()!.replace(/_/g, ' ');
const f = (iso: string, tz: string, o: Intl.DateTi
… [687 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List lib exports and channel mentions

  <details><summary>result</summary>

```
14:export const LAGOS = 'Africa/Lagos';
16:export const city = (tz: string) => CITY[tz] ?? tz.split('/').pop()!.replace(/_/g, ' ');
18:export const tTime = (iso: string, tz: string) => f(iso, tz, { hour: '2-digit', minute: '2-digit', hourCycle: 'h23' });
19:export const tDay = (iso: string, tz: string) => f(iso, tz, { weekday: 'short', day: 'numeric', month: 'short' });
20:export const tLong = (iso: string, tz: string) => f(iso, tz, { weekday: 'long', day: 'numeric', month: 'long' });
21:export const dateIn = (iso: string | Date, tz: string) => new Intl.DateTimeFormat('en-CA', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit' }).format(typeof iso === 'string' ? new Date(iso) : iso);
22:export const minsIn = (iso: string, tz: string) => { const [h, m] = tTime(iso, tz).split(':').map(Number); return h * 60 + m; };
24:export const offsetOf = (iso: string, tz: string) => { const d = new Date(iso); const local = new Date(d.toLocaleString('en-US', { timeZone: tz })); const utc = new Date(d.toLocaleString('en-US', { timeZone: 'UTC' })); return Math.round((local.getTime() - utc.getTime()) / 60000); };
25:export const lagosAt = (date: string, hm: string) => new Date(`${date}T${hm}:00+01:00`).toISOString();
26:export const addDays = (date: string, n: number) => { const d = new Date(`${date}T12:00:00Z`); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); };
27:export const weekday = (date: string) => new Date(`${date}T12:00:00Z`).getUTCDay();
30:expor
… [14491 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read mail and hire-c area slices

  <details><summary>result</summary>

```
// Connected email and contact policy (addendum E-01; audit addendum §C). Providers are SIMULATED: no mailbox is
// reached. The store holds connection metadata only, never credentials. Messages themselves stay in w.threads.
// Owned by the EMAIL builder: mailboxes, contact policies, suppressions, follow-ups, org email policy, client
// reminder automations, extracted preferences (forgettable), "seen" receipts and the demo failure switch.
import type { World } from '../../mock/world';
import type { ContactPolicy, FailReason, FollowUpRule, MailboxConnection, Suppression } from '../domain';

/** Organisation email policy (E01-22): what Q applies when it drafts and sends from this organisation. */
export interface OrgMailPolicy {
  orgId: string; signature: string; legal: string; language: string; sendingHours: [string, string];
  /** Per mailbox per day; the provider has its own limits on top. */
  dailyCap: number; channels: ('EMAIL' | 'IN_APP' | 'SMS')[]; templates: { id: string; label: string; kind: string }[];
  externalData: string; escalation: string; delegation: string;
}
/** A client's pre-approved reminder automation (R4). Only a person can start it; pausing takes effect at once. */
export interface ReminderAutomation {
  id: string; orgId: string; clientOrgId?: string; mailboxId: string; label: string; messageClass: string;
  state: 'ACTIVE' | 'PAUSED'; cap: number; sent: number; approvedBy: string; approvedAt: string; pausedBy?: string; pausedAt?: string;
}
/** Somet
… [16709 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find D9 and D17 decisions

  <details><summary>result</summary>

```
22:| D9 | **Retention periods.** For memories, audit events, applications, interview recordings and files after deletion | Founder plus legal (NDPR/GDPR) | Determines what the deletion receipt can promise (T5). | The deletion receipt lists what is kept (audit, sent messages) and why. |
30:| D17 | **Rubric validation and use.** Who signs off a rubric's job-relatedness; adverse-impact monitoring; whether the index is visible to hiring managers | Founder plus an I-O psychology or fairness adviser | The index affects decisions; it is not validated. | Prototype arithmetic only, always shown with coverage, labelled as unvalidated; human review required. |
```
  </details>

- 🔧 `Bash`: Read decision register and pricing claims

  <details><summary>result</summary>

```
# Outstanding decisions

This register lists only decisions that are still open. Approved product and design decisions live in `decisions/`. "Founder" means a product or design trade-off that only the founder can make. "Engineering" means the next phase can decide it with the founder informed.

## Decided by the founder (29 Oct)

| # | Decision | What it means for the build | Where it is in the prototype |
|---|---|---|---|
| D1 | **Candidates can be found by unverified organisations too, but unverified accounts are limited.** | The default discovery rule is `ANYONE`. A candidate can still choose: employers and agencies with a verified domain, fully verified employers only, or nobody, and can hide from named organisations. Until an organisation is verified it **cannot post roles, can send at most 3 outreach messages a week, cannot run campaigns or submittals, and cannot see contact details**, and every message it sends tells the candidate it isn’t verified yet. The limits live in one place so they are easy to change. | `orgLimits`, `UNVERIFIED_LIMITS`, `outreachThisWeek`, `canDiscover` in `prototype/src/mock/world.ts`; Passport search options; Settings summary |
| D3 | **Verification is required before posting roles.** | A role brief can be drafted and approved internally, but publishing a listing needs a verified organisation: a verified domain plus a business registration check. Search is allowed before verification, under the D1 limits. | R1 verification step (`journeys/hi
… [7700 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Locate pricing hypotheses document

  <details><summary>result</summary>

```
docs/sources/batch-6/01_BUYER_EVIDENCE_AND_PRICING.md
docs/sources/INDEX.md
talent-q-design/handoff/CONSOLIDATION-MERGE-LEDGER.md
| S15 | [G2 hireEZ reviews/pricing](https://www.g2.com/products/hireez/pricing) | Strong workflow value, data freshness/contact quality complaints | Self-selected reviews; avoid causal claims |
| S16 | [2025 UK student recruitment survey](https://ise.org.uk/_userfiles/pages/files/reports/student_recruitment_survey_2025.pdf) | UK recruiting cost benchmark for early-career hires | Early-careers subset, not all UK recruiting |
| S17 | [SHRM Applicant Evaluation 2023](https://www.shrm.org/mena/topics-tools/news/talent-acquisition/recruiters-say-experience-top-factor-applicant-evaluation) | Initial resume screens privilege prior experience, may miss nonstandard qualifications | Earlier US sample; initial screen, not outcomes |
| S18 | `Talent-Q-Complete.zip` + `ALL-SPECS.md` (user-provided) | Current designed requirements, status, module and Q prototypes | Simulation, incomplete, status documents sometimes inconsistent; inspect actual code |

## Unproven claims that MUST NOT appear as facts
- Talent Q reliably identifies better employees than LinkedIn, Workera, TestGorilla, CodeSignal or manual recruiters.
- Recruiters globally would pay a particular price for Talent Q.
- Q's prototype role-matching scores are statistically validated or calibrated to performance.
- Every job is verified, every email delivered, or all LinkedIn profiles accessible.
- Cand
… [649 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read pricing hypotheses doc

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
… [9637 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read ds Workspace, motion, PageIndex, ConfirmButton

  <details><summary>result</summary>

```
// The Direction D workspace: an ink THREAD where Q works, a resizable separator, and a paper CANVAS
// where Q builds artifacts. Desktop: drag or use arrow keys on the separator; collapse the thread to a
// strip that still shows Q's state. Phones: the thread is the page and the canvas opens as a sheet.
import { createContext, useContext, useEffect, useLayoutEffect, useRef, useState, type ReactNode } from 'react';
import { motion } from 'motion/react';
import { QMark, moodOf, presenceLine, type QAgent, type QMood } from './QMark';

export function useNarrow(px = 860) {
  const q = `(max-width: ${px}px)`;
  const [narrow, set] = useState(() => typeof window !== 'undefined' && window.matchMedia(q).matches);
  useEffect(() => { const m = window.matchMedia(q); const on = () => set(m.matches); m.addEventListener('change', on); return () => m.removeEventListener('change', on); }, [q]);
  return narrow;
}
const read = (k: string, d: string) => { try { return localStorage.getItem(k) ?? d; } catch { return d; } };
const write = (k: string, v: string) => { try { localStorage.setItem(k, v); } catch { /* storage unavailable */ } };

type ThreadMode = 'open' | 'collapsed';
/** True inside the AppShell's global Split: pages render only their canvas, Q's thread is global. */
export const InShell = createContext(false);
export interface PageTask { title: string; entries: Entry[]; onSend: (t: string) => void; agents: QAgent[]; mood?: QMood; detail?: string; busy?: boolean }
let pageTask: Pag
… [10065 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Canvas component and DS class list

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
… [2420 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Q types and openers

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
… [5455 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read engine registration API and rubric skill

  <details><summary>result</summary>

```
q/core/engine.ts:15:export const registerSkill = (s: Skill) => { if (!skills.some((x) => x.id === s.id)) skills.push(s); };
q/core/engine.ts-16-export const allSkills = () => skills;
q/core/engine.ts-17-
q/core/engine.ts-18-type OpFn = (w: World, args: Record<string, unknown>, actor: Actor) => void | { say?: string; nav?: { to: string; label: string } };
q/core/engine.ts-19-const ops = new Map<string, OpFn>();
q/core/engine.ts:20:export const registerOp = (name: string, fn: OpFn) => { ops.set(name, fn); };
q/core/engine.ts-21-
q/core/engine.ts-22-// ---------------- Conversation ----------------
q/core/engine.ts-23-const route = () => (location.hash.replace(/^#/, '').split('?')[0] || '/');
q/core/engine.ts:24:export function appendQ(w: World, actorId: string, m: Omit<QMsg, 'id' | 'at'>) {
q/core/engine.ts-25-  (w.q.threads[actorId] ??= []).push({ ...m, id: uid('qm'), at: now(), route: m.route ?? route() });
q/core/engine.ts-26-}
q/core/engine.ts-27-export const useQThread = () => useWorld((w) => w.q.threads[w.session.actor] ?? EMPTY);
q/core/engine.ts-28-const EMPTY: QMsg[] = [];
q/core/engine.ts-29-
q/core/engine.ts-30-/** Shows "Q is thinking" between the person's turn and Q's reply (a real wait on async skills / gateway). */
q/core/engine.ts-31-let thinking = false; const thinkSubs = new Set<() => void>();
q/core/engine.ts-32-const setThinking = (v: boolean) => { thinking = v; thinkSubs.forEach((f) => f()); };
--
q/core/engine.ts:127:export async function runAction(a: QAct
… [9042 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read QMsg type; find budget mentions

  <details><summary>result</summary>

```
export type QOp = { t: 'say'; text: string } | { t: 'nav'; to: string } | { t: 'do'; op: string; args?: Record<string, unknown> };
export interface QAction { label: string; primary?: boolean; act: QOp }
export interface QMsg {
  id: string; who: 'me' | 'q' | 'system'; text: string; at: string; route?: string;
  used?: string[]; why?: string; actions?: QAction[];
  kind?: 'reply' | 'question' | 'suggestion' | 'refusal' | 'approval' | 'notice' | 'plan' | 'undo';
  /** Live-bound content rendered from state (e.g. a plan's agents or a draft). */
  ref?: { type: string; id: string };
  /** Which engine produced this reply: honest labelling of simulation. */
  engine?: 'rules' | 'gateway' | 'system';
}
export interface QFrame { intent: string; slots: Record<string, string>; awaiting?: string; startedAt: string; topic?: string }
export interface Suggestion { id: string; actor: string; rule: string; subject: string; text: string; why: string; actions: QAction[]; at: string; state: 'OPEN' | 'DISMISSED' | 'SNOOZED' | 'DONE'; until?: string }
export interface UndoEntry { id: string; label: string; at: string; inverse: { op: string; args: Record<string, unknown> } }
export interface QPrefs { proactive: 'OFF' | 'QUIET' | 'NORMAL'; voice: boolean; plain: boolean }
export interface QSlice {
  threads: Record<string, QMsg[]>;
  frames: Record<string, QFrame | null>;
  suggestions: Suggestion[];
  prefs: Record<string, QPrefs>;
  nav: Record<string, { path: string; label: string; at: string }
… [3674 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect QA scripts and router

  <details><summary>result</summary>

```
qa/scripts:
axe-batch1.mjs
axe-direction-d.mjs
axe-directions.mjs
axe.mjs
batch1.mjs
build-review-page.py
direction-d.mjs
direction-films.mjs
directions.mjs
features
films
films.mjs
flow.mjs
gates
journey-films.mjs
journeys
lib
review

qa/scripts/features:
campaigns.mjs
contact.mjs
email.mjs
evidence-candidate.mjs
evidence-recruiter.mjs
media.mjs
rubric.mjs

qa/scripts/review:
axe-all.mjs
capture-all.mjs
gallery
interview-followup.mjs
keyboard.mjs
motion-clips.mjs
privacy.mjs
#!/usr/bin/env bash
# Runs all ten journey scripts against one build. Usage: run-all.sh [base=http://localhost:4174/]
# Each script was written by a different builder; this normalises how each takes its address.
BASE="${1:-http://localhost:4174/}"; PORT=$(echo "$BASE" | sed -E 's#.*:([0-9]+).*#\1#')
DIR=$(cd "$(dirname "$0")" && pwd); OUT="$DIR/../../results"; mkdir -p "$OUT"
for j in R1 R2 R3 R4 R5 T1 T2 T3 T4 T5; do
  case $j in
    R1|R2|R5) cmd=(node "$DIR/$j.mjs" "$PORT");;
    R3|R4|T4) cmd=(node "$DIR/$j.mjs" "$BASE");;
    *) cmd=(env BASE="$BASE" node "$DIR/$j.mjs");;
  esac
  timeout 1200 "${cmd[@]}" > "$OUT/$j.log" 2>&1; code=$?
  echo "$j exit=$code pass=$(grep -cE '^PASS' "$OUT/$j.log") fail=$(grep -cE '^FAIL' "$OUT/$j.log")"
done | tee "$OUT/summary.txt"
// Minimal hash router: routes are stable, shareable and work from a static file (low-bandwidth friendly).
import { useSyncExternalStore, type AnchorHTMLAttributes } from 'react';

const read = () => {
  const h = location.hash.replace(/^#/
… [766 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read a feature test and privacy script

  <details><summary>result</summary>

```
// Feature test · RUBRIC (audit addendum §E, AD-E-01…14, AD-B-03, AD-B-05; J11 steps 5, 8 and 9).
// Ada builds the Senior Backend rubric with Q (propose → edit weights → refusal of a proxy → approve v1), the
// comparison takes its weights, Tobi gets Q-proposed ratings from video (written the way the MEDIA builder writes
// them) and Ifeoma from shared evidence, Ada overrides with a reason (asked for when missing), adds mentoring, and
// the change notice offers "notify and reassess" or "keep v1 for this round". Tobi sees his own ratings and asks
// for a correction. Tenant isolation, phone layout (switch, page index, no sideways scroll) are checked too.
// Usage: node qa/scripts/features/rubric.mjs [port=5193] [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const PORT = process.argv[2] || '5193';
const ONLY = (process.argv[3] || 'd,m').split(',');
const OUT = fileURLToPath(new URL('../../../captures/cx/rubric/', import.meta.url)); mkdirSync(OUT, { recursive: true });
const BASE = `http://localhost:${PORT}/`;
const b = await pw.chromium.launch();
const errors = []; const results = [];
const step = (v, name, ok, detail = '') => { results.push({ v, name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} [${v}] ${name}${detail ? ` · ${detail}` : ''}`); };

for (const [v, vp, dpr] of [['d', { width: 1440, height: 900 }, 1], ['m', { width: 390, height: 844 }, 2]].filter(([x]) => ONLY
… [11251 more characters trimmed]
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:interaction-design", "args": "Org admin pages for Talent Q Direction D prototype: budget warning (MO-035), approve/reject flows, channel verification states, retention setting

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-30 12:31

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


ARGUMENTS: Org admin pages for Talent Q Direction D prototype: budget warning (MO-035), approve/reject flows, channel verification states, retention settings.

- 🔧 `Skill`: {"skill": "design-skills:ux-writing", "args": "Copy for org admin: billing hypotheses labels, permission denied, simulated provider states, retention pending decision D9, unvalidated bias checks."}

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-30 12:31

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


ARGUMENTS: Copy for org admin: billing hypotheses labels, permission denied, simulated provider states, retention pending decision D9, unvalidated bias checks.

- 🔧 `Skill`: {"skill": "dataviz", "args": "Usage meters, time-to-shortlist bars, engagement funnel for org reports, inside an existing design system (Direction D), each with a table alternative."}

  <details><summary>result</summary>

```
Launching skill: dataviz
```
  </details>


**User** · 2026-10-30 12:31

Base directory for this skill: /tmp/claude-0/bundled-skills/2.1.314/c4a5b79f779e4c38d8ced0d598b5f1b2/dataviz

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
  One exception, legend kept: the tall segmented bar (*Figures* in `references/marks-and-anatomy.md`).
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


## User Request

Usage meters, time-to-shortlist bars, engagement funnel for org reports, inside an existing design system (Direction D), each with a table alternative.

- 🔧 `Skill`: {"skill": "design-skills:design-elevation", "args": "Org admin pages in an existing Direction D system; no new aesthetics."}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-30 12:31

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


ARGUMENTS: Org admin pages in an existing Direction D system; no new aesthetics.

- 🔧 `Skill`: {"skill": "design-superpowers:creative", "args": "Inside Direction D only: no new aesthetics, typefaces or colours; gold is Q's alone. Org admin pages direction check."}

  <details><summary>result</summary>

```
Launching skill: design-superpowers:creative
```
  </details>


**User** · 2026-10-30 12:31

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


ARGUMENTS: Inside Direction D only: no new aesthetics, typefaces or colours; gold is Q's alone. Org admin pages direction check.

- 🔧 `Bash`: Read Direction D system doc and tokens

  <details><summary>result</summary>

```
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
| `AppShell` | Workspace switcher (Hiring and Career), a rail of up to 4 groups and 9 items, the command palette (⌘/Ctrl K), and phone tabs (4 plus More). Shows only areas that exist |
| `Split` | Thread and canvas. The separator can be dragged, moved with
… [4656 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect AppShell nav grouping logic

  <details><summary>result</summary>

```
4://  2. Navigation is built from the route registry, grouped, and adapts to who is signed in (employer,
27:  const orgKind = useWorld((w) => w.orgs.find((o) => o.id === actorOf(w).orgId)?.kind);
28:  const routes = allRoutes().filter((r) => r.nav && (r.side === actor.side || r.side === 'both') && (!r.nav.orgKind || r.nav.orgKind === orgKind) && (!r.nav.orgIds || r.nav.orgIds.includes(actor.orgId ?? '')));
29:  const groups = GROUP_ORDER.map((g) => ({ g, items: routes.filter((r) => r.nav!.group === g).sort((a, b) => a.nav!.order - b.nav!.order) })).filter((x) => x.items.length);
30:  return { actor, groups, routes };
34:  const { actor, groups, routes } = useNav();
63:  // A rail entry is current for its own path, its sub-paths, and any extra prefixes it declares (nav.also).
64:  const current = (r: RouteDef) => path === r.path || (r.path !== '/' && path.startsWith(r.path + '/')) || !!r.nav?.also?.some((p) => path === p || path.startsWith(p + '/'));
65:  const tabs = routes.filter((r) => r.nav?.tab).sort((a, b) => a.nav!.order - b.nav!.order).slice(0, 4);
85:      <nav className="ds-rail" aria-label="Talent Q navigation">
94:        {groups.map(({ g, items }) => {
97:            <div key={g} className="ds-navgroup">
98:              {collapsible ? <button type="button" className="ds-groupbtn ds-hide-collapsed" aria-expanded={open} onClick={() => setOpenGroups({ ...openGroups, [g]: !open })}><span className="lab">{g}</span><span aria-hidden="true">{open ? '−' : '+'}</span></bu
… [1335 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find group order, icon names and QA hook

  <details><summary>result</summary>

```
22:const GROUP_ORDER = ['Q', 'Hiring', 'Agency', 'Work', 'Interviews', 'Grow', 'Evidence', 'Organisation', 'You'];
29:  const groups = GROUP_ORDER.map((g) => ({ g, items: routes.filter((r) => r.nav!.group === g).sort((a, b) => a.nav!.order - b.nav!.order) })).filter((x) => x.items.length);
4:  q: <svg {...P}><path d="M16.4 16.4A6.5 6.5 0 1 1 18.5 12" /><path d="M15.5 15.5 19 19" /><circle cx="12" cy="12" r="1.8" fill="currentColor" stroke="none" /></svg>,
5:  home: <svg {...P}><path d="M4 11 12 4l8 7" /><path d="M6 9.5V20h12V9.5" /><path d="M10 20v-5h4v5" /></svg>,
6:  mail: <svg {...P}><rect x="3.5" y="5.5" width="17" height="13" rx="2" /><path d="m4 7 8 6 8-6" /></svg>,
7:  agents: <svg {...P}><circle cx="6" cy="6" r="2.2" /><circle cx="18" cy="6" r="2.2" /><circle cx="12" cy="18" r="2.2" /><path d="M8 7.2 10.8 16M16 7.2 13.2 16M8.2 6h7.6" /></svg>,
8:  roles: <svg {...P}><rect x="4" y="7" width="16" height="12" rx="2" /><path d="M9 7V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V7M4 12h16" /></svg>,
9:  search: <svg {...P}><circle cx="11" cy="11" r="6" /><path d="m20 20-4.5-4.5" /></svg>,
10:  people: <svg {...P}><circle cx="9" cy="8" r="3" /><path d="M3.5 19a5.5 5.5 0 0 1 11 0" /><circle cx="17" cy="9" r="2.4" /><path d="M16 14.2a4.5 4.5 0 0 1 5 4.8" /></svg>,
11:  approvals: <svg {...P}><path d="M4 12.5 9 17.5 20 6.5" /></svg>,
12:  calendar: <svg {...P}><rect x="4" y="5" width="16" height="15" rx="2" /><path d="M4 10h16M9 3v4M15 3v4" /></svg>,
13:  memory: <svg {...P}
… [1729 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read main QA hook, proactive API and rubric exports

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
… [4538 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rating types, proactive rest, registry shape

  <details><summary>result</summary>

```
Exit code 2
export interface RubricCriterion {
  id: string; label: string; kind: CriterionKind; weight: number; minimum?: number;
  /** Anchored levels 0–4: what each rating means, in observable terms. */
  anchors: [string, string, string, string, string];
  evidenceToInspect: string[]; questions: string[]; method: string;
  /** Requirement on the brief it comes from, and the taxonomy reference (ESCO skill, D6). */
  requirementId?: string; escoRef?: string; why: string;
}
/** Q_PROPOSED → (edits) → APPROVED (frozen) → SUPERSEDED when a newer version is approved, with a change notice. */
export interface RubricVersion { v: number; state: 'Q_PROPOSED' | 'APPROVED' | 'SUPERSEDED'; criteria: RubricCriterion[]; at: string; by: string; approvedBy?: string; note: string; changeNotice?: { text: string; affected: string[]; decision?: 'NOTIFY_AND_REASSESS' | 'KEEP_FOR_ROUND' } }
export interface Rubric { id: string; mandateId: string; orgId: string; versions: RubricVersion[] }
export interface EvidenceRef { evidenceId: string; t?: number; tEnd?: number; quote?: string }
/** One rating of one person on one criterion of one rubric version. Q proposes; a person reviews or overrides. */
export interface Rating {
  id: string; rubricId: string; v: number; personId: string; criterionId: string;
  rating: 0 | 1 | 2 | 3 | 4; uncertainty: 'LOW' | 'MEDIUM' | 'HIGH'; refs: EvidenceRef[]; note: string;
  source: 'Q_PROPOSED' | 'REVIEWER'; by: string; at: string; reviewed: boolean;
  override?: 
… [2806 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find glob-based auto registration

  <details><summary>result</summary>

```
./mock/world.ts:65:const AREA_INITS = Object.values(import.meta.glob<{ area: { id: string; init: () => unknown } }>('../state/areas/*.ts', { eager: true })).map((m) => m.area).filter(Boolean);
./mock/world.ts:66:const SEEDS = Object.values(import.meta.glob<{ seed: SeedPatch }>('../state/seeds/*.ts', { eager: true })).map((m) => m.seed).filter(Boolean);
./app/App.tsx:13:import.meta.glob('../routes/*.tsx', { eager: true });
./app/App.tsx:14:import.meta.glob('../q/skills/*.ts', { eager: true });
./app/App.tsx:15:import.meta.glob('../q/proactive/*.ts', { eager: true });
./app/App.tsx:16:import.meta.glob('../q/openers/*.ts', { eager: true });
```
  </details>

- 🔧 `Bash`: Inspect DS class variants and Switch API

  <details><summary>result</summary>

```
100:.ds-chip { border: 1px solid var(--night-3); background: transparent; color: var(--moon); border-radius: 999px; padding: 8px 14px; font-size: 14px; min-height: 40px; text-align: left; }
101:.ds-chip:hover { border-color: var(--moon-2); }
102:.ds .ds-chip.go { background: var(--gold-light); color: var(--ink); border-color: var(--gold-light); font-weight: 600; }
118:.ds-views { display: inline-flex; background: var(--wash); border-radius: 12px; padding: 4px; gap: 2px; max-width: 100%; overflow-x: auto; scrollbar-width: none; }
119:.ds-views button { border: 0; background: transparent; border-radius: 9px; padding: 8px 14px; min-height: 40px; font-size: 14px; font-weight: 600; color: var(--ink-3); white-space: nowrap; flex: none; }
120:.ds-views button[aria-pressed='true'] { background: var(--sheet); color: var(--ink); box-shadow: 0 1px 2px rgb(80 60 20 / .15); }
121:.ds-views button:disabled { opacity: .4; cursor: default; }
125:.ds .ds-btn.primary { background: var(--ink); color: var(--paper); }
126:.ds .ds-btn.quiet { border-color: transparent; color: var(--ink-3); }
127:.ds .ds-btn.danger { border-color: var(--risk); color: var(--risk); }
134:.ds-tag { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; border-radius: 999px; padding: 3px 10px; border: 1px solid var(--rule-2); color: var(--ink-2); white-space: nowrap; }
135:.ds-tag[data-k='ok'] { border-color: var(--ok); color: var(--ok); }
136:.ds-tag[data-k='busy'] { border-color: var(--gold); color: va
… [3773 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check existing skills for overlapping keywords

  <details><summary>result</summary>

```
q/skills/agency.ts
q/skills/email.ts
93:export function mandatesOf(w: World, orgId?: string) {
94-  const out: { id: string; title: string; engineering: boolean }[] = [];
95-  if (orgId === 'org_kora') out.push({ id: w.mandate.mandateId, title: w.mandate.title, engineering: true });
96-  for (const m of w.mandates) if (m.orgId === orgId) out.push({ id: m.id, title: m.title, engineering: /engineer/i.test(m.title) });
97-  return out;
98-}
99-export const mandateTitle = (w: World, id?: string) => (id === w.mandate.mandateId ? w.mandate.title : w.mandates.find((m) => m.id === id)?.title ?? 'this role');
```
  </details>

- 🔧 `Bash`: Check overlapping skill regexes and mandate info

  <details><summary>result</summary>

```
q/skills/agency.ts:242:    const sample = messageFor(c.w, camp.template, now[0] ?? members[0]);
q/skills/email.ts:281:      createDraft(ww, aa, { id, personId: pid, kind: 'INVITE', slot: { start: slots[0].start, end: slots[0].end }, options: slots.slice(1).map((s) => ({ start: s.start, end: s.end })), panel, mandateId: entry.mandateId, eventId: undefined, channel: 'EMAIL', senderId: sender?.id, template: 'tpl_invite' });
q/skills/email.ts:321:          createDraft(ww, aa, { id, personId: p.personId, kind: 'AVAILABILITY', mandateId: p.mandateId, channel: 'EMAIL', batchId, template: 'tpl_avail' });
q/skills/email.ts:327:          ref: { type: 'email.batch', id: batchId }, used: [`${orgOf(ww, aa.orgId)?.name} template: Next step and availability`, 'Contact choices and suppressions', `Sender: ${mailboxOf(ww, findMsg(ww, ds[0].msgId)?.m.senderId)?.address ?? '—'}`],
7:  mandateId: 'm_backend',
8:  title: 'Senior Backend Engineer',
41:  { evidenceId: 'e_tobi_recon', ownerId: 'p_tobi', kind: 'PROJECT', title: 'Ledger reconciliation service at Lumen', source: 'Shared repository snapshot', observedAt: '2026-08-14', verified: true, shows: 'Designed the job that matches 4m daily card settlements to the ledger and flags mismatches within minutes.', limits: 'Code was reviewed statically; production metrics are self-reported.', visibility: 'SHARED_WITH', sharedWith: ['org_kora'] },
42:  { evidenceId: 'e_tobi_go', ownerId: 'p_tobi', kind: 'WORK_SAMPLE', title: 'Go idempotency library', sour
… [2073 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read mandate fixture, NOW and Zara thread

  <details><summary>result</summary>

```
// Synthetic, fictional data. Every person and company here is invented for the design prototype.
import type { Evidence, Mandate, MemoryItem, Person, RoleFit, CalendarConnection, MeetingPreferences, BusyInterval, CareerGoal, J7Measures, RoleGap, PolicyCitation } from '@contracts';

export const ORG = { orgId: 'org_kora', name: 'Kora Pay', recruiterId: 'p_ada', recruiterName: 'Ada Okafor', timezone: 'Africa/Lagos' };

export const MANDATE: Mandate = {
  mandateId: 'm_backend',
  title: 'Senior Backend Engineer',
  team: 'Payments platform',
  location: 'Lagos',
  workMode: 'HYBRID',
  payBand: '₦2.4m–₦3.1m / month',
  version: 1,
  status: 'DRAFT',
  requirements: [
    { reqId: 'r1', label: 'Payments systems', mustHave: true, plain: 'Has built or run systems that move money and reconcile it' },
    { reqId: 'r2', label: 'Go in production', mustHave: true, plain: 'Writes and operates Go services under real load' },
    { reqId: 'r3', label: 'Postgres at scale', mustHave: true, plain: 'Designs schemas and fixes slow queries on large tables' },
    { reqId: 'r4', label: 'On-call leadership', mustHave: false, plain: 'Has led incident response and written post-mortems' },
    { reqId: 'r5', label: 'Mentoring', mustHave: false, plain: 'Has helped less experienced engineers grow' },
  ],
};

export const PEOPLE: Person[] = [
  { personId: 'p_tobi', name: 'Tobi Adeyemi', headline: 'Backend engineer, reconciliation · 7 yrs', location: 'Lagos', timezone: 'Africa/Lagos', synthetic: tru
… [1361 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/state/areas/org-admin.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/state/areas/org-admin.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Tidy retention rule factory

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/model.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/model.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Add view checks to ops; inspect utility classes

  <details><summary>result</summary>

```
5
/* Connected email (E-01) on Direction D paper: envelope rows read like a letter's header, statuses are words with a
   shape (border style) not colour alone, recovery is the primary action, demo controls are visibly "Demo". */
.ds .em-aside { display: inline-flex; gap: 8px; flex-wrap: wrap; }
.ds .em-facets { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 8px; }
.ds .em-facets .em-search { grid-column: 1 / -1; }
styles/base.css:36:.muted { color: var(--color-text-muted); }
styles/base.css:41:.sr-only { position: absolute !important; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
ds/ds.css:24:.ds .sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
ds/ds.css:25:.ds .lab { font-family: var(--data); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); font-weight: 500; }
ds/ds.css:26:.ds .ink .lab { color: var(--moon-2); }
ds/ds.css:27:.ds .num { font-variant-numeric: tabular-nums; }
ds/ds.css:28:.ds .voice { font-family: var(--voice); font-weight: 380; letter-spacing: -.01em; }
ds/ds.css:31:.ds .t24 { font-size: 24px; line-height: 1.2; }
ds/ds.css:32:.ds .t19 { font-size: 19px; line-height: 1.45; }
ds/ds.css:33:.ds .t14 { font-size: 14px; line-height: 1.45; }
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/Frame.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/Frame.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/PagesOrg.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/PagesOrg.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Remove stray exports from PagesOrg

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/PagesOversight.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/PagesOversight.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Edit`: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/PagesOversight.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/PagesOversight.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Simplify engagement table columns

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/org-admin.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/org-admin/org-admin.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/routes/org-admin.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/routes/org-admin.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Drop OrgOnly; read engine sendToQ flow

  <details><summary>result</summary>

```
export async function sendToQ(text: string) {
  const t = text.trim(); if (!t) return;
  if (getWorld().network === 'offline') {
    update((w) => { appendQ(w, w.session.actor, { who: 'me', text: t }); (w.q.outbox[w.session.actor] ??= []).push(t); appendQ(w, w.session.actor, { who: 'system', kind: 'notice', text: 'You’re offline. I’ll read this as soon as you reconnect; nothing is lost.', engine: 'system' }); });
    return;
  }
  // A page task (onboarding, planner, J7) can own turns Q's skills don't clearly claim. Its own thread shows
  // the person's words, so they are not duplicated here.
  const task = getPageTask();
  if (task) {
    const c0 = ctxFor(getWorld(), t);
    const top = Math.max(0, ...skills.filter((s) => s.side === 'both' || s.side === c0.actor.side).map((s) => s.match(c0)));
    const owner0 = c0.frame ? skills.find((s) => s.id === c0.frame!.intent) : undefined;
    if (top < 0.75 && !owner0?.answer) { task.onSend(t); return; }
  }
  update((w) => { appendQ(w, w.session.actor, { who: 'me', text: t }); });
  setThinking(true);
  try {
    const c = ctxFor(getWorld(), t);
    // 1. An awaited answer to the active frame wins, unless the person clearly changed topic.
    const owner = c.frame ? skills.find((s) => s.id === c.frame!.intent) : undefined;
    if (owner?.answer) {
      const r = await owner.answer(c);
      if (r) { applyReply(r); return; }
    }
    // 2. Score every skill for this side; highest wins above the threshold.
    const scored = skil
… [3214 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Add doOp/probeOp helpers to model

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/skills/org-admin.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/skills/org-admin.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Simplify handler and tighten regexes

  <details><summary>result</summary>

```
36:type Intent = { id: string; sec: Sec; re: RegExp; score: number; need?: 'VIEW'; go: (c: QCtx) => QReply };
```
  </details>


**Claude** · 2026-10-30 12:45

Now openers and proactive rules.

- 🔧 `Bash`: Read opener and proactive rule shapes

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
// R3 proactive rules, all read from real state: drafts nobody approved (never sent on their own), candidates
// who haven't replied, candidates waiting on Kora, a colleague changing an interview panel, a candidate asking
// to move an interview, and messages queued while offline. Q suggests; it never acts on its own.
import { registerRule } from '../core/proactive';
import { simNow, type World } from '../../mock/world';
import type { Actor } from '../../
… [1998 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Write openers and proactive rules; typecheck

  <details><summary>result</summary>

```
src/journeys/org-admin/PagesOrg.tsx(71,152): error TS2339: Property 'by' does not exist on type '{ v: number; body: string[]; }'.
src/q/skills/org-admin.ts(19,7): error TS6133: 'nav' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Fix type errors and re-typecheck

  <details><summary>result</summary>

```
src/journeys/talent-b/Applications.tsx(8,19): error TS6133: 'K' is declared but its value is never read.
src/journeys/talent-b/Applications.tsx(8,22): error TS6133: 'APP_LABEL' is declared but its value is never read.
src/q/skills/hire-d.ts(17,163): error TS6133: 'SOURCES' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Start vite dev server on port 5212

  <details><summary>result</summary>

```
6:  "scripts": {
7-    "tokens": "node ../tokens/build.mjs",
8-    "registers": "node ../scripts/build-registers.mjs",
9:    "dev": "npm run tokens && vite",
10-    "build": "npm run tokens && tsc -b && vite build",
11-    "preview": "vite preview --port 4174",
12-    "typecheck": "tsc -b"

Are they installed?
    at file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50669:15
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50174:26
```
  </details>

- 🔧 `Bash`: Read vite error log

  <details><summary>result</summary>

```
Re-optimizing dependencies because vite config has changed

  VITE v5.4.21  ready in 354 ms

  ➜  Local:   http://localhost:5212/
  ➜  Network: use --host to expose
Error: The following dependencies are imported but could not be resolved:

  @emotion/is-prop-valid (imported by /home/user/neo/talent-q-design/prototype/dist-review/assets/index-7nVgRM4N.js)

Are they installed?
    at file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50669:15
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50174:26
```
  </details>

- 🔧 `Bash`: Write capture script and render two pages

  <details><summary>result</summary>

```
d hub overflow 0
d billing overflow 0
m hub overflow 0
m billing overflow 0
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/d-hub.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Check for other builders' placement routes

  <details><summary>result</summary>

```
routes/hire-d.tsx:26:registerRoute({ path: '/r/outcomes', side: 'recruiter', label: 'placements', render: () => <Outcomes />, nav: { group: 'Hiring', label: 'Placements', icon: 'people', order: 19, orgKind: 'EMPLOYER' } });
journeys:
agency
assess
campaigns
career
contact
evidence
gallery
hire-a
hire-b
hire-c
hire-d
media
onboarding
org-admin
planner
public
q-tools
rubric
talent-b
talent-c
talent-d

q/skills:
agency.ts
assess.ts
campaigns.ts
core.ts
email.ts
evidence-candidate.ts
evidence-ops.ts
evidence.ts
hire-a.ts
hire-b.ts
hire-c.ts
hire-d.ts
hiring-basic.ts
media.ts
org-admin.ts
public.ts
q-tools.ts
rubric.ts
talent-a.ts
talent-b.ts
talent-c.ts
talent-d.ts

routes:
agency.tsx
assess.tsx
campaigns.tsx
core.tsx
entry.tsx
gallery.tsx
guard.tsx
hire-a.tsx
hire-b.tsx
hire-c.tsx
hire-d.tsx
media.tsx
org-admin.tsx
public.tsx
q-tools.tsx
registry.ts
talent-a.tsx
talent-b.tsx
talent-c.tsx
talent-d.tsx
```
  </details>

- 🔧 `Bash`: Check parallel skills for keyword overlap

  <details><summary>result</summary>

```
q/skills/hire-d.ts:13:import { isFounder } from '../../journeys/hire-a/model';
q/skills/hire-d.ts:17:import { availOf, bookingSlots, CH_WORD, coverage, daysBetween, fmtDay, MILESTONE_WORD, NOT_USED, nextMilestone, offerOf, railOf, reminderQueue, scopeOn, search, sourcesFor, type SourceId } from '../../journeys/hire-d/model';
q/skills/q-tools.ts:134:  match: (c) => (/\b(do|follow|obey) (what )?(the|that) (page|blog|site|website|post) (says|said|asks|wants|tells)|\b(page|blog|site|post)('s| s)? instructions?\b|\bemail (the|all|every) (cvs|candidates).*(blog|page|says)/.test(c.norm) ? 0.95 : 0),
q/skills/talent-d.ts:238:  match: (c) => (cand(c) && resourcesFor(c.actor.personId ?? '').length > 0 && (/(teach me|learn|lesson|course|resource|video|transcript|captions|read about|how do i (lead|write))/.test(c.norm)) && !/(cv|cover)/.test(c.norm) ? 0.84 : 0),
q/skills/talent-d.ts:242:    if (onPage && /transcript/.test(c.norm)) return { msgs: [reply('Transcript shown below the video. Select any line to jump there.')], effects: (w) => { const m = ((td(w).learn[pid] ??= {})[r.id] ??= { mode: 'VIDEO', pos: 0, captions: true, transcript: false, answer: '', done: false }); m.transcript = true; } };
q/skills/talent-d.ts:243:    if (onPage && /caption/.test(c.norm)) return { msgs: [reply(/off|hide/.test(c.norm) ? 'Captions off.' : 'Captions on.')], effects: (w) => { const m = ((td(w).learn[pid] ??= {})[r.id] ??= { mode: 'VIDEO', pos: 0, captions: true, transcript: false, answer: '', done: fa
… [608 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check hire-d skill overlaps

  <details><summary>result</summary>

```
6://   offer ("prepare an offer for tobi", "approve the offer")   placements ("which check-ins are due?")
120:// ---------------- SC-060 placements ----------------
123:  match: (c) => (hirer(c) && /\b(placements?|placement record|outcome journal|check-?ins?|90-day|30-day|new hires?)\b/.test(c.norm) ? 0.88 : 0),
127:    return { msgs: [{ kind: 'reply', text: list.length ? `${list.length} placement record${list.length === 1 ? '' : 's'}. ${due.length ? due.map((x) => `${x.o.name}: ${MILESTONE_WORD[x.n!.kind].toLowerCase()} due ${fmtDay(x.n!.due!)}${daysBetween(simNow(c.w), x.n!.due!) < 0 ? ' (late)' : ''}`).join('; ') + '.' : 'Nothing due.'} Only milestones a person verified, with the new hire’s agreement; never used to score anyone.` : 'No placements yet. A record starts when someone accepts an offer and a person records it.' }], nav: { to: '/r/outcomes', label: 'placements' } };
151:    return { msgs: [{ kind: 'reply', text: `${todo.length ? `${todo.length} waiting for your yes: ${todo.map((x) => `${x.title.toLowerCase()} (by ${x.channel ? CH_WORD[x.channel] : '—'}, ${tDay(x.sendAt, LAGOS)} ${tTime(x.sendAt, LAGOS)})`).join('; ')}.` : 'Nothing is waiting for approval.'}${blocked.length ? ` ${blocked.length} won’t send: ${blocked.map((x) => x.blocked).join(' ')}` : ''}`, actions: todo[0] ? [doOp(`Approve: ${todo[0].title}`, 'hd.rem.approve', { id: todo[0].id }, true), go('Open reminders', '/r/reminders')] : [go('Open reminders', '/r/reminders')] }] };
```
  </details>


**Claude** · 2026-10-30 12:49

Tie-break: my skill yields placements to employers.

- 🔧 `Bash`: Yield employer placement questions to hire-d skill

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-30 12:51

Now look at the billing page and mobile hub.

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/d-billing.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/m-billing.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:51

[Image: original 780x4090, displayed at 381x2000. Multiply coordinates by 2.05 to map to original image.]

- 🔧 `Bash`: Render all admin pages desktop and phone

  <details><summary>result</summary>

```
d instr overflow 0
d tpl overflow 0
d ch overflow 0
d ret overflow 0
d src overflow 0
d pl overflow 0
d cp overflow 0
d rp overflow 0
d md overflow 0
d ql overflow 0
d ln overflow 0
d bl-bayo overflow 0
d mych overflow 0
m instr overflow 0
m tpl overflow 0
m ch overflow 0
m ret overflow 0
m src overflow 0
m pl overflow 0
m cp overflow 0
m rp overflow 0
m md overflow 0
m ql overflow 0
m ln overflow 0
m bl-bayo overflow 0
m mych overflow 0
```
  </details>

- 🔧 `Bash`: Find Zara's actor id

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: List candidate actor ids

  <details><summary>result</summary>

```
id: 'p_amaka' personId: 'p_amaka'
id: 'p_chidi' personId: 'p_chidi'
id: 'p_tobi' personId: 'p_tobi'
id: 'p_grace' personId: 'p_grace'
id: 'p_zara' personId: 'p_zara'
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/d-ch.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:54

[Image: original 1440x2490, displayed at 1157x2000. Multiply coordinates by 1.24 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/d-rp.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/m-md.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:54

[Image: original 780x9530, displayed at 164x2000. Multiply coordinates by 4.76 to map to original image.]

- 🔧 `Bash`: Save before captures for pairs

  <details><summary>result</summary>

```
01-before.png
02-before.png
03-before.png
04-before.png
```
  </details>


**Claude** · 2026-10-30 12:54

Let me run design-critique on these before fixing.

- 🔧 `Skill`: {"skill": "design-skills:design-critique", "args": "Critique the org-admin captures: billing (nested budget box, colour-only 'near limit' meter), models on phone (very long route list), reports for a

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
… [3099 more characters trimmed]

- 🔧 `Bash`: Apply critique fixes

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Re-render pages and save after captures

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/m-pl.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:57

[Image: original 780x3912, displayed at 399x2000. Multiply coordinates by 1.95 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/d-pl-kora.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/oa/m-md.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 12:58

[Image: original 780x7140, displayed at 218x2000. Multiply coordinates by 3.58 to map to original image.]

- 🔧 `Write`: /home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Run org-admin feature test on desktop

  <details><summary>result</summary>

```
FAIL [d] MO-035 reduced motion: warning text still present

84 passed, 1 failed
```
  </details>

- 🔧 `Bash`: Fix paused visibility; run both viewports

  <details><summary>result</summary>

```
FAIL [m] MO-035: crossing 80% shows the soft warning with stop/spend decision
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-askbar button').first()[22m
[2m    - locator resolved to <button type="button" aria-label="Q: New agent runs are paused by your budget decision. Nothing ran.. Open Q">…</button>[22m
[2m  - attempting click action[22m
[2m    2 × waiting for element to be visible, enabled and stable[22m
[2m      - element is visible, enabled and stable[22m
[2m      - scrolling into view if needed[22m
[2m      - done scrolling[22m
[2m      - <aside class="ds-thread ink" aria-label="Conversation with Q">…</aside> from <div role="dialog" aria-label="Q" class="ds-qsheet" aria-modal="true">…</div> subtree intercepts pointer events[22m
[2m    - retrying click action[22m
[2m    - waiting 20ms[22m
[2m    2 × waiting for element to be visible, enabled and stable[22m
[2m      - element is visible, enabled and stable[22m
[2m      - scrolling into view if needed[22m
[2m      - done scrolling[22m
[2m      - <aside class="ds-thread ink" aria-label="Conversation with Q">…</aside> from <div role="dialog" aria-label="Q" class="ds-qsheet" aria-modal="true">…</div> subtree intercepts pointer events[22m
[2m    - retrying click action[22m
[2m      - waiting 100ms[22m
[2m    57 × waiting for element to be visible, enabled and stable[22m
[2m       - el
… [959 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Harden phone helpers and rerun phone

  <details><summary>result</summary>

```
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.fill: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('#q-ask')[22m
[2m    - locator resolved to <input value="" id="q-ask" autocomplete="off" placeholder="Ask Q anything, in your own words"/>[22m
[2m    - fill("approve the template")[22m
[2m  - attempting fill action[22m
[2m    - waiting for element to be visible, enabled and editable[22m
[2m  - element was detached from the DOM, retrying[22m
[2m    - waiting for "http://localhost:5212/" navigation to finish...[22m
[2m    - navigated to "http://localhost:5212/#/r/admin/templates"[22m

    at ask (/home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs:30:284)
    at async file:///home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs:67:7 {
  log: [
    "  - waiting for locator('#q-ask')",
    '    - locator resolved to <input value="" id="q-ask" autocomplete="off" placeholder="Ask Q anything, in your own words"/>',
```
  </details>

- 🔧 `Bash`: Always reset Q sheet before asking on phone

  <details><summary>result</summary>

```
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for getByRole('button', { name: 'Close Q' }).first()[22m

    at closeQ (/home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs:28:126)
    at async ask (/home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs:30:58)
    at async file:///home/user/neo/talent-q-design/qa/scripts/features/org-admin.mjs:67:7 {
  log: [
    "  - waiting for getByRole('button', { name: 'Close Q' }).first()"
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Make phone Q open/close tolerant; rerun

  <details><summary>result</summary>

```
1
FAIL [m] MO-035: crossing 80% shows the soft warning with stop/spend decision

88 passed, 1 failed
```
  </details>

- 🔧 `Bash`: Find phone billing warning capture

  <details><summary>result</summary>

```
m-06-billing-warning.png
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/org-admin/m-06-billing-warning.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 13:08

[Image: original 780x4148, displayed at 376x2000. Multiply coordinates by 2.07 to map to original image.]

- 🔧 `Bash`: Scope pause button check; full run

  <details><summary>result</summary>

```
PASS [m] phone /r/admin/reports: no sideways scroll, body text ≥ 12px, section select instead of link row

174 passed, 0 failed
```
  </details>

- 🔧 `Bash`: Run privacy review script

  <details><summary>result</summary>

```
PASS search results cache no longer shows Dayo
PASS saved comparison no longer shows Dayo
PASS Zara withdrew from Kora: nothing visible despite her application
PASS no page errors
All privacy checks passed
J11.mjs
J12.mjs
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
```
  </details>

- 🔧 `Bash`: Run R3, R4 and R5 journey scripts

  <details><summary>result</summary>

```
R3 exit=0 pass=48 fail=0
R4 exit=0 pass=72 fail=0
R5 exit=0 pass=65 fail=2
```
  </details>

- 🔧 `Bash`: Show R5 failures

  <details><summary>result</summary>

```
FAIL [d] approval starts the search; result arrives in Q · Kora Pay’s handbook asks for the pay band in the first message, so it’s in the brief (₦2.4m–₦3.1m / month). Check the requirements beside this conversation; change anything there or tell me. Approve it and I’ll start searching. I won’t contact anyone. || Approved. I’m starting the search now. You can leave this page; I’ll keep going and tell you here when people appear.
FAIL R5: 65/66 steps passed
```
  </details>

- 🔧 `Bash`: Inspect failing R5 step

  <details><summary>result</summary>

```
54-  await ask('hybrid lagos');
55-  await ask('payments reconcilation');
56-  w = await world();
57-  step(v, 'answers applied to the brief', w.mandate.workMode === 'HYBRID' && w.mandate.requirements[0].label === 'Payments systems' && /Approve it and I’ll start searching/.test(await lastQ()));
58-  await shot('kora-brief', true);
59-  await chip(/Approve and start searching/);
60-  await page.waitForTimeout(9000);
61-  w = await world();
62:  step(v, 'approval starts the search; result arrives in Q', w.mandate.status !== 'DRAFT' && w.sourcing.done && /I read 24 profiles/.test(await lastQ(3)), await lastQ(2));
```
  </details>

- 🔧 `Bash`: Rerun R5 to check flakiness

  <details><summary>result</summary>

```
67
```
  </details>

- 🔧 `Bash`: Check axe script usage

  <details><summary>result</summary>

```
// Accessibility scan of every route, as the person who would use it, on desktop and phone.
// Also checks: Q's composer is reachable on the page (desktop) or via "Ask Q" (phone), no horizontal
// overflow, and Tab reaches the main content. Usage: node axe-all.mjs <base> <axe.min.js> <out.json>
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { readFileSync, writeFileSync } from 'node:fs';
const [BASE = 'http://localhost:4174/', AXE, OUT = 'axe-all.json'] = process.argv.slice(2);
const axe = readFileSync(AXE, 'utf8');
const AS = {
  u_ada: ['/r/home', '/r/plan', '/r/compare', '/r/people/p_tobi', '/r/interviews', '/r/pipeline', '/r/messages', '/r/calendar', '/r/calendar/connect', '/r/team', '/r/setup', '/r/setup/handbook', '/r/roles', '/r/audit', '/r/memory', '/r/mandate', '/r/sourcing', '/r/outreach', '/settings'],
  u_dele: ['/r/home', '/r/agency/agents', '/r/agency/campaigns', '/r/agency/clients', '/r/agency/client/org_kora', '/r/agency/compare', '/r/agency/docs', '/r/agency/mandate/m_ops', '/r/agency/notes', '/r/agency/pools', '/r/agency/reports', '/r/agency/searches', '/r/agency/submittals', '/r/compare'],
  p_tobi: ['/c/home', '/c/passport', '/c/jobs', '/c/jobs/j_kora_backend', '/c/applications', '/c/messages', '/c/memory', '/c/prep', '/settings'],
  p_chidi: ['/c/career', '/c/growth', '/c/welcome'],
  p_grace: ['/c/start', '/c/interview', '/c/slots'],
  p_zara: ['/c/applications', '/c/jobs', '/c/messages'],
};
const PUBLIC = ['/signup', '/galler
… [323 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Run axe on org-admin routes

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/axe/node_modules/axe-core/axe.min.js
d /r/admin/templates [
  'color-contrast:3 li:nth-child(1) > .oa-li-main > .ds-linkbtn.t14[type="button"] | li:nth-child(2) > .oa-li-main > .ds-linkbtn.t14[type="button"]'
]
m /r/admin/templates [
  'color-contrast:3 li:nth-child(1) > .oa-li-main > .ds-linkbtn.t14 | li:nth-child(2) > .oa-li-main > .ds-linkbtn.t14'
]
done
```
  </details>

- 🔧 `Bash`: Fix link button contrast; rerun axe

  <details><summary>result</summary>

```
done
```
  </details>

- 🔧 `Bash`: Inspect registry status shape

  <details><summary>result</summary>

```
['_readme', 'defaults', 'surfaces', 'priority', 'screens', 'motions', 'vision', 'routes', 'design_refs', 'd_native_routes']
defaults ['screens', 'motions'] ['RESEARCHED']
surfaces ['Foundation / public', 'Employer onboarding & governance'] ['Public site and entry']
priority ['SC-117', 'SC-118'] [1]
screens ['SC-117', 'SC-162'] [{'status': 'INTEGRATED', 'route': '/r/home', 'evidence': 'captures/screens/p01-home-after-search, m-p01-home', 'note': 'Connected to shared typed state; axe 0 violations (dark/light, 1440/390); manual keyboard + screen-reader pass pending, so not VERIFIED.'}]
motions ['MO-001', 'MO-002'] [{'status': 'PROTOTYPED', 'route': '/r/home', 'evidence': '', 'note': 'Driven by a real state or run event; reduced-motion handled by MotionConfig/CSS. Dedicated clip not recorded yet.'}]
vision ['V02', 'V04'] [{'status': 'PROTOTYPED', 'route': '/r/home', 'evidence': 'prototype/src/q/core/engine.ts, q/QThread.tsx, q/skills/*.ts; all ten journey logs', 'note': 'One global Q conversation beside every route, persisted per identity, with skills per area; it is a bounded rule engine unless a model gateway is configured. Planner (SC-119) is still PROTOTYPED.'}]
routes ['/r/home', '/r/setup'] ['SC-117']
design_refs ['SC-117', 'SC-118'] ['Direction review: /x/{a,b,c}/home + captures/directions']
public.json
q-tools.json
talent-d.json
```
  </details>

- 🔧 `Bash`: Write registry patch for org-admin

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Read example design note structure

  <details><summary>result</summary>

```
# Design pass · evidence-first, candidate side (build pack 30 Oct; J12 steps 6, 7, 10, 12, 13; pack items D, E, F; P6)

Routes extended, not duplicated: `/c/home` (`CandidateHome` in `routes/entry.tsx`), `/c/passport`, `/c/applications`,
`/c/jobs` and `/c/jobs/:id` (`journeys/talent-b/*`). J7 (`/c/career`) is reused through its own `ta.j7.quiz.start` op.
New pieces live in `prototype/src/journeys/evidence/candidate/` (logic, ProofClass, Requests, Status, Cv, Gap, CSS).
Q: `q/skills/evidence-candidate.ts` (skills and `evc.*` ops) and `q/proactive/evidence-candidate.ts` (5 rules).
Captures: `captures/features/evidence-candidate/{d,m}-NN-*.png` (full page, from the test). The first-render and
corrected sets are in `captures/review/pairs/evidence-candidate/{before,after}/` under the same file names.
`qa/scripts/features/evidence-candidate.mjs` passes 124/124 (62 desktop, 62 phone). T1 76/76, T3 54/54, T4 43/43,
T5 52/52, and privacy.mjs all pass on the same build. No page scrolls sideways at 390 px.

## Skills invoked (Skill tool) → screens → changes
- **interaction-design** → the request card is a small state machine read straight from the shared decision:
  SENT (three choices) → IN_PROGRESS (sample panel; "Save and finish later" keeps the answer) → SUBMITTED
  ("Self-reported, waiting for review") → REVIEWED (outcome and note) or DECLINED. "Share existing work instead"
  is a separate branch: the request stays SENT. Decline and offer open inline forms rather than modals, and b
… [1666 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/org-admin.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/org-admin.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Fix counts, final typecheck, stop server, list changes

  <details><summary>result</summary>

```
Exit code 144
13:Tests: `qa/scripts/features/org-admin.mjs` passes **174/174** (85 desktop, 89 phone). These also pass on the same
0
```
  </details>

- 🔧 `Bash`: Confirm my files and server stopped

  <details><summary>result</summary>

```
M prototype/src/journeys/org-admin/org-admin.css
?? journeys/design/org-admin.md
?? registry/patches/org-admin.json
14045
```
  </details>

- 🔧 `Bash`: Stop the 5212 dev server

  <details><summary>result</summary>

```
0
```
  </details>

- 🔧 `SubagentHandback`: {"message": "## Org-admin build report\n\nAll 11 screens, the 3 vision groups and MO-035 now work in the Direction D prototype. My feature test passes 174 of 174 steps (85 desktop, 89 phone). The priv

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
