# Helper agent agent-a3a47effc510ab808: Rubric studio and scoring

Source: `agent-a3a47effc510ab808.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 16:11

You are the RUBRIC builder for Talent Q's product-definition prototype (React + TypeScript + Vite, at /home/user/neo/talent-q-design/prototype). Start by reading /home/user/neo/talent-q-design/journeys/ADDENDUM-BUILD-BRIEF.md completely and everything it lists under "Read first". It is binding.

Your feature: audit addendum §E, Q-generated, recruiter-editable, role-specific evaluation rubrics and evidence-backed scoring (AD-E-01 to AD-E-14, and AD-B-05 on role-specific weighting). Plus J11 steps 5 and 9, and the scorecard part of step 8.

**Model**, already defined:
- Types: `Rubric`, `RubricVersion`, `RubricCriterion` (anchored 0–4, evidence to inspect, questions, method, weight, minimum, `requirementId`, `escoRef`, why) and `Rating` (bound to `{rubricId, v}`; uncertainty, refs with timestamps, override with reason, dispute).
- Slice and scoring: `state/areas/rubrics.ts`, with `roleIndex()` returning index **and** coverage. Keep that arithmetic exactly; it is the founder's prototype formula, not a validated test.
- The role is the Senior Backend mandate `m_backend`: the legacy `w.mandate`, with requirements r1–r5 in `mock/fixtures.ts`. Also MandateX roles such as `m_payouts`.
- Org guidelines live in `state/areas/hire-c.ts` (guides), read-only for you. The taxonomy is ESCO on ISCO-08 (founder decision D6); label ESCO references as illustrative ids.

**Screens**, desktop and phone:
- The evaluation studio at `/r/roles/:id/rubric`:
  - Q's proposal beside the editable criteria (side by side on desktop; stacked with a clear "Q proposed / your version" switch on phone);
  - weights with a visible share bar per criterion (use dataviz);
  - minimum requirements, anchors, evidence to inspect, questions and method;
  - why each criterion is job-related, with the source requirement;
  - approve, which creates a frozen version, and a revisions list (who, when, what changed, as a diff);
  - the change notice flow for a material change after candidates were rated: list the affected candidates; choices "notify and reassess" or "keep v1 for this round"; v1 ratings stay on v1.
  - Q refuses protected-characteristic criteria or proxies, and says why.
  - A plain statement that the weights and the index need empirical validation.
- The scorecard on the candidate profile (`journeys/hire-b/Profile.tsx`) and the uncertainty inspector:
  - per criterion: rating, anchor text, evidence refs (timestamps link to `/r/people/:id/video?t=…`, which the MEDIA builder owns), uncertainty, freshness, and reviewed or Q-proposed;
  - the index is shown **only** with coverage ("62 at 55% coverage"), with a sentence that unknown criteria are not counted as zero;
  - override with a reason, audited;
  - the candidate's explanation and appeal route: add a small view in `/c/applications` for the person's own ratings on a role they applied to or were assessed for, with "ask for a correction". Coordinate through the store, not by editing talent-b UI beyond one insertion in `journeys/talent-b/Applications.tsx`.
- The comparison (`journeys/hire-b/model.ts`, `Ledger.tsx`): replace the fixed 1.5× payments rule with the approved rubric's weights for the role, explained in the margin ("weights from rubric v1, approved by Ada on …"). When no rubric is approved, say so and fall back to equal must-haves, labelled. Keep R2 passing; update its expectations only where this legitimately changes them, and list them.
- Q skills (a new `q/skills/rubric.ts`): "propose a rubric for the senior backend role", "make incidents and on-call weight 2", "add mentoring", "remove X", "approve the rubric", "why is X in the rubric", "show Tobi's scorecard", "lower postgres to 2 because …" (an override needs a reason; ask for it if missing), "keep v1 for this round".
- Apply `PageIndex` (`src/ds/PageIndex.tsx`, already in place) to the long candidate profile on phones (AD-B-03): sections such as Fit, Scorecard, Evidence, Interviews and History.

The MEDIA builder writes Q-proposed `Rating` records from video findings (`source: 'Q_PROPOSED'`, refs with t/tEnd). Your UI must show them like any other rating, and your override and review ops work on them.

**Files you own:**
- a new `journeys/rubric/*`
- `journeys/hire-b/*`
- `q/skills/hire-b.ts`, a new `q/skills/rubric.ts`
- `q/proactive/hire-b.ts`
- `state/areas/rubrics.ts`: you may add helpers; keep `roleIndex`'s formula
- `state/seeds/hire-b.ts`
- `routes/hire-b.tsx`
- one insertion in `journeys/talent-b/Applications.tsx`

**Port 5193.** Tests: `qa/scripts/features/rubric.mjs`. Also run R2 and R5 from `qa/scripts/journeys/` (port-number style, see `run-all.sh`). Fix any regression you caused.

Deliverables:
- `journeys/design/rubric.md`: skills invoked, skill → screen → change, the rendered critique and fixes, pairs, weaknesses, and requirement IDs prototyped with evidence.
- `journeys/handoff/rubric.md`: entities and ownership (an assessment module), version immutability, the scoring contract, the separation of signals (eligibility, skills, interview, practical, compatibility, coverage), fairness controls, audit, APIs, events and Q tools, validation needed (SIOP-style job analysis, adverse impact monitoring), risks.

Don't commit. Final report: routes built, test counts, regressions, requirement IDs, shared-file requests, and honest gaps.

- 🔧 `Bash`: Read build brief and list dirs

  <details><summary>result</summary>

```
# Addendum build brief (29 Oct): four features plus connected email, in one connected journey

Read this whole file before doing anything. It is shared by four builders working in parallel in the same working tree.

## Read first

1. The founder's two addenda, which are binding:
   - `/root/.claude/uploads/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/1fc07cf0-Talent_Q_Design_Audit_and_Feature_Addendum_2026-10-29.md`
   - `/root/.claude/uploads/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/32fd5c9b-Talent_Q_Email_and_Correspondence_Addendum_2026-10-29.md`
2. The connected journey (a service blueprint with the disruptions): `journeys/J11-CONNECTED-JOURNEY.md`.
3. The requirements you must satisfy: `registry/ADDENDUM-REQUIREMENTS.csv`. Cite their IDs.
4. The shared model, which is already written. Extend it; don't redefine it.
   - Types: the addendum section of `prototype/src/state/domain.ts` (Msg/Thread extensions, HiringCampaign, Rubric*, Rating, MediaEvidence, MediaReview, MailboxConnection, ContactPolicy, Suppression, FollowUpRule).
   - Slices and seeds: `prototype/src/state/areas/{campaigns,rubrics,media,mail}.ts`. Note `roleIndex()`: the index is never shown without coverage.
5. Design rules:
   - `design-system/DIRECTION-D-SYSTEM.md` (the system, including its execution rules)
   - `handoff/DESIGN-QUALITY-GATE.md` (the gate you must pass)
   - `journeys/DESIGN-PASS-BRIEF.md`, then one existing area file such as `journeys/design/hire-b.md`, to see the expected standard
   - `handoff/PRIV
… [7572 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read founder audit addendum

  <details><summary>result</summary>

```
228 18f408d0-01_VISION_RESEARCH_AND_PRODUCT_EXPERIENCE_MASTER.md
    116 1fc07cf0-Talent_Q_Design_Audit_and_Feature_Addendum_2026-10-29.md
     66 2801443f-07_VIDEO_STORYBOARD_AND_VISUAL_REFERENCE.md
    134 32fd5c9b-Talent_Q_Email_and_Correspondence_Addendum_2026-10-29.md
    184 3e7963a6-02_COMPLETE_SCREEN_ATLAS_v2.csv
    147 44e63e80-02_COMPLETE_SCREEN_ATLAS.csv
   1344 4e4534c6-Talent_Q_Complete_Investor_and_Product_Brief.pdf
    364 5798e144-Talent_Q_Vision_Addendum_v2.pdf
     42 5ec76ce1-04_FOUNDER_VISION_TRACEABILITY_v2.csv
   1237 74f8747f-TalentQ_Global_Market_Research_and_Commercial_Strategy_v1.pdf
     45 8d9d1c4b-06_DESIGN_SCOPE_AND_NEXT_RESEARCH.md
    214 950c6bd2-08_ADDENDUM_SCHEDULING_J7_MEMORY_AND_TOOLING.md
     33 b10e6fe1-04_FOUNDER_VISION_TRACEABILITY.csv
   1419 bfeb2b17-TalentQ_Technical_Blueprint_v1.pdf
     58 c125053b-03_MOTION_AND_VIDEO_ATLAS_v2.csv
    123 d54e237a-00_CLAUDE_START_HERE_v2.md
     96 d88528a4-05_CLAUDE_DESIGN_FIRST_MASTER_DIRECTIVE.md
     42 e41b0140-03_MOTION_AND_VIDEO_ATLAS.csv
    146 eac6715d-TalentQ_User_Journey_Atlas_Stage2.docx
     57 eb50ca8b-README_SEND_TO_CLAUDE.md
   1344 f7124b8d-Talent_Q_Complete_Investor_and_Product_Brief.pdf
   1237 f81aae10-TalentQ_Global_Market_Research_and_Commercial_Strategy_v1.pdf
   8676 total
# Talent Q: Design Review Audit and Feature Addendum

**Date:** 29 October 2026  
**Basis:** User-supplied `Talent-Q-Design-Review.zip` and the founder's new requirements.  
**Purpose:** Amend the exec
… [13377 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read email addendum excerpt and J11
- 🔧 `Bash`: Read requirements CSV for my IDs

  <details><summary>result</summary>

```
# Talent Q | Addendum E-01: Connected Email and Q-Managed Correspondence

**Issued:** 29 October 2026  
**Applies to:** Talent Q full product vision, 183-screen atlas, role/campaign organization, recruiter and candidate journeys, Q intelligence / memory / agents, and final engineering handoff.  
**Status:** Product-definition requirements, not an assertion of working integrations.  
**Purpose:** Explicitly require Q to use ordinary email as a first-class recruitment communication channel, alongside in-app messaging, calendar invitations, WhatsApp where allowed, SMS, and calls. This is an addition to, not a replacement for, the earlier Design Audit and Feature Addendum.

## 1. Founder requirement

Users must be able to ask Q, in normal language or voice, to draft, send, read, reply to, organize and follow up on work-related email, subject to granted access and approval rules. This includes:

- **Gmail and Google Workspace:** user-connected addresses such as `person@gmail.com` or company accounts hosted by Google.
- **Outlook, Microsoft 365 and Outlook.com:** user-connected Microsoft mailboxes.
- **Other ordinary/business email:** the organization's own domain, supported SMTP/IMAP or other legitimate provider APIs, e.g., `recruitment@company.example`, where the provider and authentication configuration permit it.
- **Talent Q platform-generated notifications:** separate service-owned email for invitations, confirmations, receipts and notices, using a reputable transactional mai
… [14233 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
id,source,feature,requirement,kind,journeys,route,status,evidence
AD-B-03,Audit §B,Mobile,"Long phone pages have an in-page index (sticky) and the primary action stays reachable; bottom controls respect safe areas and never cover content",UX,R2 T3 T4,/r/people/:id /c/interview,SPECIFIED,
AD-B-05,Audit §B,Weighting,"Role-specific weighting replaces the fixed 1.5x rule: weights come from the approved rubric version, are editable by the employer and explained",Q/UX,R2,/r/compare /r/roles/:id/rubric,SPECIFIED,
AD-E-01,Audit §E,Rubric,"Q drafts job-related criteria from the approved brief, workplace guidelines and the job taxonomy (ESCO, D6): evidence to inspect, interview questions, practical methods, weights, minimum requirements and anchored levels 0-4",Q,J11 R2,/r/roles/:id/rubric,SPECIFIED,
AD-E-02,Audit §E,Rubric,"Recruiter edits or approves side by side with Q's proposal; approval creates an immutable version",UX,J11,/r/roles/:id/rubric,SPECIFIED,
AD-E-03,Audit §E,Rubric,Every candidate for the same role and stage is assessed against the same rubric version; ratings are bound to the version,Data,J11,,SPECIFIED,
AD-E-04,Audit §E,Rubric,"Material mid-campaign changes require notice, audit and principled re-assessment; earlier ratings stay attached to their version",Policy,J11,/r/roles/:id/rubric,SPECIFIED,
AD-E-05,Audit §E,Rubric,"Signals stay separate: eligibility, demonstrated skills (with provenance), structured interview answers, practical assessments, candidate compatibi
… [1602 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rubrics slice and domain types

  <details><summary>result</summary>

```
// Role-specific evaluation rubrics (audit addendum §E). Versions are frozen once approved; ratings bind to
// {rubricId, v}. The index below is PROTOTYPE ARITHMETIC, not a validated employment test (addendum §E):
//   index    = 100 · Σ(j∈O) w_j·(r_j/4) / Σ(j∈O) w_j      (O = criteria with a rating)
//   coverage = 100 · Σ(j∈O) w_j / Σ(all) w_j
// The index is never shown without coverage; unknown criteria are never zero; it is not comparable across roles.
import type { World } from '../../mock/world';
import type { Rating, Rubric, RubricVersion } from '../domain';

export interface RubricsState { list: Rubric[]; ratings: Rating[] }

export const area = { id: 'rubrics', init: (): RubricsState => ({ list: [], ratings: [] }) };
export const rubrics = (w: World) => w.areas.rubrics as RubricsState;
export const rubricFor = (w: World, mandateId: string) => rubrics(w).list.find((r) => r.mandateId === mandateId);
/** The version in force: the latest APPROVED one (a Q_PROPOSED draft is never used for scoring). */
export const approvedVersion = (w: World, mandateId: string): RubricVersion | undefined =>
  [...(rubricFor(w, mandateId)?.versions ?? [])].reverse().find((v) => v.state === 'APPROVED');

export interface IndexResult { index: number | null; coverage: number; observed: number; total: number; v?: number; reviewed: number }
/** Observed role-evidence index and coverage for one person on one role, from the approved version only. */
export function roleIndex(w: World, mandateId:
… [1939 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read domain.ts

  <details><summary>result</summary>

```
// Talent Q domain model for the prototype's one authoritative store (World v4).
// Every slice is typed; every change worth auditing is a DomainEvent with an actor and a scope.
// Scope decides who may ever see an event or record:
//   ORG:<id>     members of that organisation (and only them: tenant isolation for agencies)
//   PERSON:<id>  that candidate only (private Passport, J7 practice, private memory)
//   SHARED:<org>:<person>  both, because the candidate chose to share with that organisation
import type { Requirement } from '@contracts';

export type Side = 'recruiter' | 'candidate';
export type OrgRole = 'OWNER' | 'ADMIN' | 'RECRUITER' | 'HIRING_MANAGER' | 'INTERVIEWER' | 'VIEWER';
export type JourneyId = 'R1' | 'R2' | 'R3' | 'R4' | 'R5' | 'T1' | 'T2' | 'T3' | 'T4' | 'T5';

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
  /** Agencies only: client organisat
… [13440 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Survey design docs and source sizes

  <details><summary>result</summary>

```
114 design-system/DIRECTION-D-SYSTEM.md
   16 handoff/DESIGN-QUALITY-GATE.md
   79 journeys/DESIGN-PASS-BRIEF.md
   73 journeys/design/hire-b.md
   88 handoff/PRIVACY-AND-PERMISSIONS.md
  370 total
journeys/design:
agency.md
hire-a.md
hire-b.md
hire-c.md
talent-a.md
talent-b.md
talent-c.md

journeys/handoff:
agency.md
hire-a.md
hire-b.md
hire-c.md
talent-a.md
talent-b.md
talent-c.md
     15 ds/ConfirmButton.tsx
     15 ds/Switch.tsx
     15 state/areas/media.ts
     17 routes/talent-b.tsx
     18 routes/talent-a.tsx
     19 q/core/policy.ts
     19 q/skills/hiring-basic.ts
     21 routes/guard.tsx
     21 state/seeds/hire-c.ts
     22 state/areas/campaigns.ts
     23 ds/PageIndex.tsx
     25 ds/Glyph.tsx
     25 q/core/glossary.ts
     25 state/seeds/hire-b.ts
     26 journeys/hire-b/ui.tsx
     26 routes/hire-c.tsx
     28 ds/icons.tsx
     28 state/areas/talent-a.ts
     30 routes/talent-c.tsx
     30 state/areas/rubrics.ts
     32 routes/registry.ts
     33 state/areas/mail.ts
     34 routes/hire-a.tsx
     36 state/areas/hire-b.ts
     39 q/QPresence.tsx
     39 state/seeds/talent-b.ts
     45 state/seeds/agency.ts
     46 q/RunConversation.tsx
     49 routes/agency.tsx
     50 state/areas/hire-a.ts
     52 q/proactive/hire-b.ts
     53 q/core/proactive.ts
     56 q/core/types.ts
     57 q/proactive/talent-b.ts
     66 q/proactive/talent-c.ts
     66 state/areas/hire-c.ts
     67 state/areas/talent-b.ts
     67 state/seeds/hire-a.ts
     69 journeys/hire-b/projects.ts
   
… [1188 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read design system and quality gate

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
… [12705 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read hire-b design note and privacy doc

  <details><summary>result</summary>

```
# Design pass · hire-b (R2 Ada, non-technical recruiter hiring engineers)

Routes: `/r/compare`, `/r/people/:id`, `/r/interviews`, `/r/interviews/:id`, plus Q reply cards. Captures in
`captures/review/after/{desktop,phone}/u_ada_r_*.png` and the states `u_ada_r2_*.png`; journey states in `captures/cx/R2/`.
`R2.mjs` passes 74 of 74 steps on desktop and phone. `privacy.mjs` passes. No page scrolls sideways at 390 px.

## Defects found (most severe first)
1. Comparison: the evidence table scrolled sideways (the fourth person was cut off on desktop). There was no chart:
   strength showed only as small glyphs and counts like "3 verified, 0 evidenced…". Weighting was invisible.
2. Comparison: the controls took the first screen on phones (11 black pills). The title was a three-line sentence that
   repeated the first note. Nothing said what had changed after a change; the order change was only in Q's text.
3. Profile: the brief fit was below seven evidence items and the viewer. Provenance used four mono labels per item.
   Pipeline stages looked like buttons. "How to check" repeated the same sentence three times.
4. Copilot: there was no progress or coverage. The rubric was 15 identical pills. The vague-answer follow-ups sat
   under the form. "Before the interview" evidence was missing, so Ada couldn't see what to probe.
5. Interviews list: there were five floating cards and no time hierarchy. The title said "0 waiting". The next
   action was missing.
6. Q replies: the challenge 
… [9796 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 16:11

Now the hire-b code.

- 🔧 `Bash`: Read hire-b model and Ledger

  <details><summary>result</summary>

```
<persisted-output>
Output too large (32.1KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bh2xk23w4.txt

Preview (first 2KB):
// R2 (Ada): how Q reads shared evidence against a role's requirements. One place for the comparison,
// the profile, Q's skills and the proactive rules, so every surface explains the same thing the same way.
// Rule-based and deliberately transparent: every cell names the evidence (or its absence) behind it.
import type { Evidence, Requirement } from '@contracts';
import { actorOf, canSeeCandidate, simNow, visibleEvidence, type World } from '../../mock/world';
import type { Interview } from '../../state/domain';
import { hireB, type Level, type Rating } from '../../state/areas/hire-b';

export const KORA_ROLE = 'm_backend';
export const reqsOf = (w: World): Requirement[] => w.mandate.requirements;
export const reqLabel = (w: World, id: string) => reqsOf(w).find((r) => r.reqId === id)?.label ?? id;
export const firstName = (w: World, pid: string) => w.people.find((p) => p.personId === pid)?.name.split(' ')[0] ?? 'They';
export const nameOf = (w: World, pid: string) => w.people.find((p) => p.personId === pid)?.name ?? pid;
export const viewerOrg = (w: World) => actorOf(w).orgId ?? 'org_kora';

// ---------- Words Q recognises for each requirement ----------
const CRIT: Record<string, RegExp> = {
  r1: /\b(payments?|reconcil\w*|money|settlements?|fintech)\b/,
  r2: /\b(golang|go)\b/,
  r3:
… [615 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/model.ts

  <details><summary>result</summary>

```
1	// R2 (Ada): how Q reads shared evidence against a role's requirements. One place for the comparison,
2	// the profile, Q's skills and the proactive rules, so every surface explains the same thing the same way.
3	// Rule-based and deliberately transparent: every cell names the evidence (or its absence) behind it.
4	import type { Evidence, Requirement } from '@contracts';
5	import { actorOf, canSeeCandidate, simNow, visibleEvidence, type World } from '../../mock/world';
6	import type { Interview } from '../../state/domain';
7	import { hireB, type Level, type Rating } from '../../state/areas/hire-b';
8	
9	export const KORA_ROLE = 'm_backend';
10	export const reqsOf = (w: World): Requirement[] => w.mandate.requirements;
11	export const reqLabel = (w: World, id: string) => reqsOf(w).find((r) => r.reqId === id)?.label ?? id;
12	export const firstName = (w: World, pid: string) => w.people.find((p) => p.personId === pid)?.name.split(' ')[0] ?? 'They';
13	export const nameOf = (w: World, pid: string) => w.people.find((p) => p.personId === pid)?.name ?? pid;
14	export const viewerOrg = (w: World) => actorOf(w).orgId ?? 'org_kora';
15	
16	// ---------- Words Q recognises for each requirement ----------
17	const CRIT: Record<string, RegExp> = {
18	  r1: /\b(payments?|reconcil\w*|money|settlements?|fintech)\b/,
19	  r2: /\b(golang|go)\b/,
20	  r3: /\b(postgres\w*|sql|databases?|db|queries|query)\b/,
21	  r4: /\b(on-?call|oncall|incidents?|outages?|post-?mortems?)\b/,
22	  r5: /\b(mento
… [25672 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Ledger.tsx

  <details><summary>result</summary>

```
1	// The evidence ledger (R2): one row per person, one block per requirement. Block width is how much the
2	// requirement counts (must-haves twice a nice-to-have; Q's extra weight on payments is visible as a wider
3	// block), block shade is how strong the evidence is (one ink hue, light to dark: dataviz ordinal ramp,
4	// validated: #b9b1a3 / #5d5648 / #16140f on #fffdf8). Nothing relies on shade alone: every block carries a
5	// glyph, a word where it fits, an accessible name, and the table below the chart repeats every value.
6	// Motion (MO-013 comparison morph): rows re-order with a layout animation and block widths ease when the
7	// weighting or criteria change, using the shared motion tokens; reduced motion is handled globally.
8	import { motion } from 'motion/react';
9	import type { World } from '../../mock/world';
10	import { Glyph } from '../../ds/Glyph';
11	import { Link } from '../../ui/router';
12	import { DUR, EASE } from '../../ds/motion';
13	import type { Level } from '../../state/areas/hire-b';
14	import { cellFor, firstName, GLYPH_OF, LEVEL_WORD, nameOf, rank, reqLabel, shortLabel, weightOf, type Change, type CompareView } from './model';
15	
16	const WORD: Record<Level, string> = { verified: 'Verified', evidenced: 'Shown', partial: 'Partial', claim: 'Claimed', none: 'Not shown' };
17	const ORD = ['1st', '2nd', '3rd', '4th', '5th', '6th'];
18	const morph = { duration: DUR.slow, ease: EASE.standard };
19	
20	export function Ledger({ w, v, change, onCell, co
… [5409 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read hire-b Profile

  <details><summary>result</summary>

```
Interviews.tsx
Ledger.tsx
Profile.tsx
ProjectViewer.tsx
model.ts
ops.ts
projects.ts
refs.tsx
ui.tsx
// Candidate profile for recruiters (R2, design pass). Reads in the order Ada needs it: who this is and Q's
// one-line reading (title + lede) → where they are → how they stand against the brief (one evidence strip and a
// row per requirement, each linking to the items it rests on, with how to check it) → everything they shared,
// checked items first, with provenance on one quiet line → the safe project viewer → questions to ask.
// Only what the person shared with the viewer's organisation; confidential items show that they exist, never
// their contents. Privacy goes through canSeeCandidate / visibleEvidence (mock/world), never around them.
import { useEffect, useRef, useState } from 'react';
import { actorOf, canSeeCandidate, useWorld, visibleEvidence, type World } from '../../mock/world';
import type { Evidence } from '@contracts';
import { Canvas } from '../../ds/Workspace';
import { Glyph } from '../../ds/Glyph';
import { Link } from '../../ui/router';
import { runAction } from '../../q/core/engine';
import { STAGES, STAGE_LABEL } from '../../state/domain';
import { hireB, type Level } from '../../state/areas/hire-b';
import { assessFor, cellFor, firstName, KORA_ROLE, questionsFor, reqsOf, viewerOrg, visibleIds } from './model';
import { markSeen } from './ops';
import { Ledger } from './Ledger';
import { PROJECTS } from './projects';
import { ProjectViewer } from './Pr
… [15440 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read hire-b ops, route, seed, area, PageIndex

  <details><summary>result</summary>

```
// R2 operations. Pages and Q's replies both perform work through these registered ops, so a button and
// a typed request do exactly the same thing (and Q can offer them as serialisable actions).
import { emit, getWorld, now, uid, update, type World } from '../../mock/world';
import type { Actor, Stage } from '../../state/domain';
import { pushUndo, qSays, registerOp } from '../../q/core/engine';
import { hireB, type Level, type Rating } from '../../state/areas/hire-b';
import { cellFor, defaultView, describeChange, shortLabel, snapshot, draftFeedback, firstName, KORA_ROLE, questionsFor, reqLabel, visibleIds, type CompareView } from './model';

const scope = (a: Actor) => (a.orgId ? `ORG:${a.orgId}` : `PERSON:${a.personId}`);
export const CMP_KEY = (actorId: string) => `${actorId}|/r/compare`;
export function cmpView(w: World, actorId = w.session.actor): CompareView {
  return { ...defaultView(w), ...((w.q.ui[CMP_KEY(actorId)]?.cmp as Partial<CompareView> | undefined) ?? {}) };
}
/** Apply a change to the comparison. Anything that can move the result keeps a snapshot of the result before
 *  it, so the page can say in plain words what changed (dataviz: the change is shown, not left to memory). */
export function setCmp(w: World, actorId: string, patch: Partial<CompareView>) {
  const k = CMP_KEY(actorId);
  const before = cmpView(w, actorId);
  const after: CompareView = { ...before, ...patch };
  const label = 'last' in patch ? null : describeChange(w, before, after);
  if 
… [17867 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find rubric references and read seed.ts

  <details><summary>result</summary>

```
./mock/fixtures.ts
./q/skills/hire-b.ts
./q/skills/talent-a.ts
./q/core/glossary.ts
./journeys/hire-b/Interviews.tsx
./journeys/career/personas.ts
./journeys/career/j7.ts
./journeys/career/Career.tsx
./journeys/onboarding/refs.tsx
./state/domain.ts
./state/areas/media.ts
./state/areas/rubrics.ts
./directions/b/B.tsx
./directions/c/C.tsx
./directions/a/A.tsx
./directions/d/Career.tsx
./directions/d/data.ts
./screens/Career.tsx
160 screens/Compare.tsx
// Seed for the one simulated world. All people, organisations, jobs and receipts are fictional.
// The cast is shared across journeys so that one journey's actions show up in another's.
import type { Evidence, Person } from '@contracts';
import type { Actor, Application, CalEvent, Consent, Interview, Job, MandateX, Org, PipelineEntry, QPrefs, Thread } from './domain';

export const NOW = '2026-10-29T09:00:00+01:00';

export const ACTORS: Actor[] = [
  { id: 'u_funmi', name: 'Funmi Adebayo', first: 'Funmi', initials: 'FA', side: 'recruiter', title: 'Founder', timezone: 'Africa/Lagos', journey: 'R1', email: 'funmi@crumbandco.example', signedUp: false },
  { id: 'u_ada', name: 'Ada Okafor', first: 'Ada', initials: 'AO', side: 'recruiter', title: 'Talent partner', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'RECRUITER', journey: 'R2', email: 'ada@kora.example', signedUp: true },
  { id: 'u_ngozi', name: 'Ngozi Eze', first: 'Ngozi', initials: 'NE', side: 'recruiter', title: 'HR lead', timezone: 'Africa/Lagos', orgId: 'org_kora'
… [15978 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read campaigns, media, hire-c areas and fixtures

  <details><summary>result</summary>

```
// Hiring campaigns (audit addendum §D): organisation → campaign → requisitions (roles). A campaign groups roles for
// navigation and workload; it never copies role or candidate data. The role→campaign link lives only in `roles`.
// Outreach campaigns (agency, w.areas.agency) are a different thing: a child of a requisition or client pool.
import type { World } from '../../mock/world';
import type { HiringCampaign } from '../domain';

export interface CampaignsState { list: HiringCampaign[] }

export const area = {
  id: 'campaigns',
  init: (): CampaignsState => ({
    list: [
      { id: 'c_q4_eng', orgId: 'org_kora', name: 'Q4 Engineering Expansion', goal: 'Two backend hires for payments and payouts before the January freeze', owner: 'u_ada', deadline: '2026-12-19', status: 'ACTIVE', createdAt: '2026-10-01', createdBy: 'u_ada', roles: ['m_backend', 'm_payouts'] },
      { id: 'c_merchant', orgId: 'org_kora', name: 'Merchant Success 2026', goal: 'Rebuild the merchant support team', owner: 'u_ngozi', status: 'ACTIVE', createdAt: '2026-09-12', createdBy: 'u_ngozi', roles: ['m_support'] },
      { id: 'c_tb_kora', orgId: 'org_tb', clientOrgId: 'org_kora', name: 'Kora Pay · Backend (agency)', goal: 'Confidential second backend hire for Kora', owner: 'u_dele', status: 'ACTIVE', createdAt: '2026-10-10', createdBy: 'u_dele', roles: ['m_kora_agency'] },
    ],
  }),
};
export const campaigns = (w: World) => w.areas.campaigns as CampaignsState;
/** The campaign a role belongs to (on
… [10390 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read payouts mandate seed and world.ts head

  <details><summary>result</summary>

```
// Kunle: two sources that disagree. Both shared with Kora; neither is silently preferred.
  ev({ evidenceId: 'e_ha_kunle_cv', ownerId: 'p_kunle', kind: 'CLAIM', title: 'CV: 6 years building Go services (2020 to now)', source: 'CV uploaded by Kunle', observedAt: '2026-10-20', shows: 'Says he has written Go in production since 2020.', limits: 'His own claim.', visibility: 'SHARED_WITH', sharedWith: ['org_kora'] }),
  ev({ evidenceId: 'e_ha_kunle_gh', ownerId: 'p_kunle', kind: 'PROJECT', title: 'GitHub: Go activity from March 2024', source: 'Public GitHub profile', observedAt: '2026-10-21', verification: 'VERIFIED', verified: true, shows: 'Public Go commits start in March 2024, about 2 years ago.', limits: 'Only public work shows; private company code would not appear.', visibility: 'SHARED_WITH', sharedWith: ['org_kora'] }),
];

const PAYOUTS: MandateX = {
  id: 'm_payouts', orgId: 'org_kora', title: 'Backend Engineer, Payouts', plain: 'Builds and runs the services that pay merchants out every day, and fixes them when a payout fails.', team: 'Payouts', location: 'Lagos', workMode: 'HYBRID',
  pay: { min: 1800000, max: 2600000, currency: 'NGN', period: 'month' }, status: 'DRAFT', createdBy: 'u_ada',
  requirements: [
    { reqId: 'py1', label: 'Payout or transfer systems', mustHave: true, plain: 'Has built or run systems that send money out and retry safely' },
    { reqId: 'py2', label: 'Go in production', mustHave: true, plain: 'Writes and operates Go services under real load
… [8843 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check working tree status

  <details><summary>result</summary>

```
M prototype/src/ds/ds.css
 M prototype/src/state/domain.ts
?? journeys/ADDENDUM-BUILD-BRIEF.md
?? journeys/J11-CONNECTED-JOURNEY.md
?? prototype/src/ds/PageIndex.tsx
?? prototype/src/state/areas/campaigns.ts
?? prototype/src/state/areas/mail.ts
?? prototype/src/state/areas/media.ts
?? prototype/src/state/areas/rubrics.ts
?? registry/ADDENDUM-REQUIREMENTS.csv
de8909a Offline build config for the downloadable review package
7ca9359 Founder review gallery builder; refreshed journey captures from the final run
773376b R1/R5 design pass under D1/D3; one Q card at a time; in-place confirms; review links
20ec2c5 T4 design pass: calm phone-first interview room, follow-up with skip, designed pause/offline/back-online states, review/approve/receipt, clearer uploads; banners stack on phones
6946901 R3 design pass: readable draft/diff/approval/receipt cards, calendar overlap across time zones, native outbox/connect/handbook pages, warmer candidate pages; D1 send limits
```
  </details>

- 🔧 `Bash`: Read Q types and hire-b skills head

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
… [7387 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rest of hire-b skills

  <details><summary>result</summary>

```
const p = comparePatch(c) ?? { patch: {}, said: ['as you left it'] };
    const before = cmpView(c.w, c.actor.id);
    const after: CompareView = { ...before, ...p.patch };
    const ob = orderText(c.w, before), oa = orderText(c.w, after);
    const notes = readingOf(c.w, after);
    const changed = ob !== oa ? ` Order changed: before it was ${ob}; now ${oa}.` : after.people.length > 1 ? ` Order: ${oa}${Object.keys(p.patch).length > 1 ? ' (unchanged)' : ''}.` : '';
    return {
      msgs: [{ kind: 'reply', text: `Comparing ${p.said.join(', ')}.${changed} ${notes[0] ?? ''}`.replace(/\s+/g, ' ').trim(),
        ref: after.people.length && after.criteria.length ? { type: 'hb.ledger', id: viewId({ ...after, people: after.people.filter((x) => rolePeople(c.w).includes(x)) }) } : undefined,
        used: ['Senior Backend brief v1', `${after.people.reduce((n, pid) => n + visibleEvidence(c.w, pid, viewerOrg(c.w)).length, 0)} shared evidence items`, ...(after.weighting === 'Q' && after.criteria.includes('r1') ? ['My weighting: payments 1.5×'] : [])],
        why: 'Rule-based reading of what each person shared with Kora; I never use private or withdrawn items.',
        actions: [{ label: 'Why this order?', act: { t: 'say', text: 'why is that the order' } }, ...(after.lastYear ? [] : [{ label: 'Last year only', act: { t: 'say', text: 'only evidence from the last year' } } as QAction])] }],
      effects: (w, a) => setCmp(w, a.id, p.patch),
      nav: toCompare(c),
    };
  },
});

// =
… [27426 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Q engine, refs, proactive

  <details><summary>result</summary>

```
import { matchRoute } from '../../routes/registry';
// Q's engine for the prototype: one conversation per person, skills that understand turns, serialisable
// actions, undo, navigation with view-state, and an optional model gateway. Everything goes through the
// one store (World v4), so the conversation and its effects survive navigation, reloads and other tabs.
import { useCallback } from 'react';
import type { Actor, QAction, QFrame, QMsg } from '../../state/domain';
import { actorOf, emit, getWorld, now, uid, update, useWorld, type World } from '../../mock/world';
import { navigate } from '../../ui/router';
import { entities, normalise } from './nlu';
import { getPageTask } from '../../ds/Workspace';
import type { QCtx, QReply, ReplyMsg, Skill } from './types';

// ---------------- Registries (skills, ops, live renderers) ----------------
const skills: Skill[] = [];
export const registerSkill = (s: Skill) => { if (!skills.some((x) => x.id === s.id)) skills.push(s); };
export const allSkills = () => skills;

type OpFn = (w: World, args: Record<string, unknown>, actor: Actor) => void | { say?: string; nav?: { to: string; label: string } };
const ops = new Map<string, OpFn>();
export const registerOp = (name: string, fn: OpFn) => { ops.set(name, fn); };

// ---------------- Conversation ----------------
const route = () => (location.hash.replace(/^#/, '').split('?')[0] || '/');
export function appendQ(w: World, actorId: string, m: Omit<QMsg, 'id' | 'at'>) {
  (w.q.threads[a
… [17497 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Compare screen and hire-b ui

  <details><summary>result</summary>

```
// SC-041 Compare candidates, SC-039 Evidence inspector, SC-040 Role-fit explanation (rebuilt for R2, design pass).
// Requirement by requirement, never one score. The page reads top to bottom as: the finding (title) → what you
// chose (one filter row) → what changed since your last change → the ledger (chart) with Q's margin notes →
// the evidence behind every block (the table view) → the inspector for one block. Ada changes the choices by
// clicking or by telling Q; both go through the same op, so "what changed" is recorded either way.
import { useEffect, useRef, useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { useWorld } from '../mock/world';
import { useViewState, runAction } from '../q/core/engine';
import { Canvas } from '../ds/Workspace';
import { Glyph } from '../ds/Glyph';
import { arrive } from '../ds/motion';
import { SwitchRow } from '../ds/Switch';
import { Link } from '../ui/router';
import { cellFor, changesSince, defaultView, firstName, headline, LEVEL_WORD, nameOf, readingOf, reqsOf, rolePeople, shortLabel, weightOf, type CompareView } from '../journeys/hire-b/model';
import { Ledger } from '../journeys/hire-b/Ledger';
import { LevelMark, VerTag, fmtDate, verOf } from '../journeys/hire-b/ui';
import '../journeys/hire-b/ops';

const toggle = (xs: string[], x: string) => (xs.includes(x) ? xs.filter((y) => y !== x) : [...xs, x]);

export function Compare() {
  const w = useWorld((x) => x);
  const [stored] = useViewSta
… [13396 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List QA scripts and runner

  <details><summary>result</summary>

```
ls: cannot access 'qa/scripts': No such file or directory
ls: cannot access 'qa/scripts/journeys': No such file or directory
ls: cannot access 'qa/scripts/features': No such file or directory
cat: qa/scripts/journeys/run-all.sh: No such file or directory
src/q/openers/core.ts
src/q/skills/hire-b.ts
src/q/skills/agency.ts
src/q/skills/hire-c.ts
src/q/skills/talent-b.ts
src/q/skills/hire-a.ts
src/q/proactive/hire-c.ts
src/q/slots.ts
src/journeys/talent-b/Prep.tsx
src/journeys/talent-b/Applications.tsx
```
  </details>

- 🔧 `Bash`: Locate qa folder

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
qa:
ACCESSIBILITY-AND-UX-REPORT.md
BATCH-1-REVIEW.md
DESIGN-REVIEW-PROCESS.md
Q-VS-MANUAL.md
RECORDING-ISSUES-AUDIT.md
VIDEO-CAPTURE-REPORT.md
results
scripts

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
films
films.mjs
flow.mjs
journey-films.mjs
journeys
lib
review
qa/scripts/journeys:
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
```
  </details>

- 🔧 `Bash`: Read R2 journey test

  <details><summary>result</summary>

```
202 R1.mjs
   184 R2.mjs
   239 R3.mjs
   281 R4.mjs
   160 R5.mjs
   187 T1.mjs
   154 T2.mjs
   147 T3.mjs
   290 T4.mjs
   136 T5.mjs
  1980 total
// R2 · Ada, a non-technical recruiter hiring a Senior Backend Engineer at Kora Pay.
// Driven mostly by typing to the global Q in imperfect language. Curveballs: changes criteria mid-comparison,
// challenges Q's ranking and corrects it, GitHub outage + retry, impressive CV with weak evidence, a disputed
// assessment, consent withdrawn, and the founder's cross-page sequence (profile → back → draft invitation).
// Usage: node R2.mjs [port] [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const PORT = process.argv[2] || '5182';
const ONLY = (process.argv[3] || 'd,m').split(',');
const OUT = fileURLToPath(new URL('../../../captures/cx/R2/', import.meta.url)); mkdirSync(OUT, { recursive: true });
const BASE = `http://localhost:${PORT}/`;
const b = await pw.chromium.launch();
const errors = []; const results = [];
const step = (v, name, ok, detail = '') => { results.push({ v, name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} [${v}] ${name}${detail ? ` · ${detail}` : ''}`); };

for (const [v, vp, dpr] of [['d', { width: 1440, height: 900 }, 1], ['m', { width: 390, height: 844 }, 2]].filter(([x]) => ONLY.includes(x))) {
  const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: dpr });
  const page = await ctx.newPage();
  
… [12811 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Applications page and refs registry

  <details><summary>result</summary>

```
// Applications for whichever candidate is signed in (Zara, Amaka, Chidi…): honest status with no promises,
// days since the employer last did anything, a polite follow-up or "move on" after N days, the evidence
// shared with each application, and a link to the conversation in messages.
import { actorOf, useWorld } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { runAction } from '../../q/core/engine';
import { Link, navigate } from '../../ui/router';
import { APP_K as K, APP_LABEL, appExplain, evById, fmtDate, tb } from './logic';

const act = (op: string, args: Record<string, unknown> = {}) => void runAction({ label: op, act: { t: 'do', op, args } });
const say = (text: string) => void runAction({ label: text, act: { t: 'say', text } });

export function ApplicationsPage() {
  const w = useWorld((x) => x);
  const a = actorOf(w); const pid = a.personId!;
  const apps = w.applications.filter((x) => x.personId === pid);
  const moved = (id: string) => tb(w).followups.find((f) => f.appId === id)?.state === 'MOVED_ON';
  const sorted = [...apps].sort((x, y) => Number(moved(x.id)) - Number(moved(y.id)) || (y.timeline[0]?.at ?? '').localeCompare(x.timeline[0]?.at ?? ''));
  return (
    <Canvas title="Your applications" kicker={`${apps.length} ${apps.length === 1 ? 'application' : 'applications'}`} open onClose={() => navigate('/c/home')}>
      <p className="t14 muted" style={{ margin: 0, maxWidth: 720 }}>Every status here comes from something the
… [6748 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find glob registrations and Canvas API

  <details><summary>result</summary>

```
./mock/world.ts:65:const AREA_INITS = Object.values(import.meta.glob<{ area: { id: string; init: () => unknown } }>('../state/areas/*.ts', { eager: true })).map((m) => m.area).filter(Boolean);
./mock/world.ts:66:const SEEDS = Object.values(import.meta.glob<{ seed: SeedPatch }>('../state/seeds/*.ts', { eager: true })).map((m) => m.seed).filter(Boolean);
./app/App.tsx:13:import.meta.glob('../routes/*.tsx', { eager: true });
./app/App.tsx:14:import.meta.glob('../q/skills/*.ts', { eager: true });
./app/App.tsx:15:import.meta.glob('../q/proactive/*.ts', { eager: true });
./app/App.tsx:16:import.meta.glob('../q/openers/*.ts', { eager: true });
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
  nav?: { group: string; label: string; icon: IconName; tab?: boolean; order: number; badge?: string; orgKind?: 'EMPLOYER' | 'AGENCY'; 
… [5555 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Canvas component

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
… [2141 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List DS classes and tokens

  <details><summary>result</summary>

```
.ds .ds-actions .ds-agent .ds-app .ds-askbar .ds-av .ds-banner .ds-brandname .ds-btn .ds-canvas .ds-canvas-head .ds-chip .ds-compose .ds-confirm .ds-context .ds-field .ds-filter .ds-groupbtn .ds-iconbtn .ds-input .ds-linkbtn .ds-log .ds-main .ds-me .ds-more .ds-navgroup .ds-navlink .ds-next .ds-node .ds-note .ds-opt .ds-page .ds-page-body .ds-pageindex .ds-palette .ds-plan .ds-proto .ds-proto-bar .ds-q .ds-qline .ds-qsim .ds-quote .ds-rail .ds-rail-brand .ds-rail-foot .ds-railbtn .ds-scrim .ds-send .ds-sep .ds-sheet .ds-sheetbar .ds-sim .ds-skeleton .ds-space .ds-space-btn .ds-split .ds-strip .ds-suggest .ds-suggest-foot .ds-suggest-more .ds-switch .ds-switchrow .ds-table .ds-table-wrap .ds-tabs .ds-tag .ds-taskhead .ds-thinking .ds-thread .ds-thread-head .ds-used .ds-versions .ds-views .ds-who .ds-why 
diff --git a/talent-q-design/prototype/src/ds/ds.css b/talent-q-design/prototype/src/ds/ds.css
index 1628c5a..b11aea6 100644
--- a/talent-q-design/prototype/src/ds/ds.css
+++ b/talent-q-design/prototype/src/ds/ds.css
@@ -277,3 +277,10 @@
 @media (max-width: 480px) { .ds-banner { grid-template-columns: auto 1fr; } .ds-banner > :nth-child(3) { grid-column: 1 / -1; justify-self: start; } } /* banners stack their action under the text on phones */
 .ds-suggest-more { justify-self: start; color: var(--moon-2); font-size: 13.5px; margin-top: -6px; } /* folded suggestions under the top card */
 .ds-confirm { display: inline-flex; flex-wrap: wrap; align-items: center; gap: 8px; } /* i
… [3114 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read ds.css head and hire-b.css head

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
… [7755 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 16:14

Now the required skills, before code.

- 🔧 `Skill`: {"skill": "design-skills:interaction-design", "args": "Evaluation studio for role-specific rubrics: Q proposal vs editable draft, approve \u2192 frozen version, change notice when material change afte

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-29 16:14

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


ARGUMENTS: Evaluation studio for role-specific rubrics: Q proposal vs editable draft, approve → frozen version, change notice when material change after ratings, override with reason, candidate correction request.

- 🔧 `Skill`: {"skill": "design-skills:ux-writing", "args": "Copy for rubric studio, scorecard (index with coverage), refusal of protected-characteristic criteria, change notice, candidate correction request."}

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-29 16:14

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


ARGUMENTS: Copy for rubric studio, scorecard (index with coverage), refusal of protected-characteristic criteria, change notice, candidate correction request.

- 🔧 `Skill`: {"skill": "dataviz", "args": "Weight share bars per rubric criterion; per-criterion rating meters 0-4 with uncertainty; index-with-coverage stat."}

  <details><summary>result</summary>

```
Launching skill: dataviz
```
  </details>


**User** · 2026-10-29 16:14

Base directory for this skill: /tmp/claude-0/bundled-skills/2.1.312/89c3aaecba30f4347135d56e756deb3e/dataviz

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


## User Request

Weight share bars per rubric criterion; per-criterion rating meters 0-4 with uncertainty; index-with-coverage stat.

- 🔧 `Bash`: Skim dataviz form and anti-pattern references

  <details><summary>result</summary>

```
10:| A single current value (+ maybe a trend) | **Stat tile** (value + delta + sparkline) | A one-bar bar chart |
11:| A handful of headline numbers | **KPI row** of stat tiles | A grouped bar chart |
12:| The one number a dashboard leads with | **Hero figure** (>=48px, sans) | - |
13:| A single ratio against a limit | **Meter** (same-ramp track) | A pie of 2 slices |
27:| Part-to-whole | **stacked bar** (go horizontal for many / long-named categories) | categorical |
# Anti-patterns - what goes wrong

Check every chart against this list. If your output matches an entry, it is wrong -
fix it before shipping. These are real failure modes, each caught in shipping
dashboards.

## Color & encoding

**Bad: Dual-axis charts (two y-scales on one plot).**
Why it misleads: the alignment of the two scales is arbitrary, so the chart invents a
correlation that isn't in the data. Real example: an "Adoption" chart plotting Users
(0-30k) against Sessions (0-800k) - a reviewer flagged it as looking "hallucinated."
Good: Do instead: two charts, small multiples, or index both series to a common base
(=100 at t0) on **one** axis.

**Bad: Recolor-on-filter.** Assigning colors by current rank, so filtering out a series
repaints the survivors.
Why: a reader who learned "Acme is blue" is now misled.
Good: Color follows the entity, not its row number. Survivors keep their hue.

**Bad: Cycling / generating hues past 8.** A 9th categorical color, generated or reused.
Why: indistinguishable from an exi
… [2004 more characters trimmed]
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:design-elevation", "args": "Recruiter evaluation studio and scorecard in Direction D (ink/paper/gold), dense but calm."}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-29 16:14

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


ARGUMENTS: Recruiter evaluation studio and scorecard in Direction D (ink/paper/gold), dense but calm.

- 🔧 `Skill`: {"skill": "design-skills:design-critique", "args": "Will critique rendered screenshots of /r/roles/m_backend/rubric and /r/people/p_tobi scorecard at desktop and phone."}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-critique
```
  </details>


**User** · 2026-10-29 16:14

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
… [2974 more characters trimmed]

- 🔧 `Bash`: Survey core skills and approve matchers

  <details><summary>result</summary>

```
41:  id: 'core.open', side: 'both',
62:  id: 'core.back', side: 'both',
71:  id: 'core.undo', side: 'both',
81:  id: 'core.explain', side: 'both',
92:  id: 'core.honest', side: 'both',
98:  id: 'core.capabilities', side: 'both',
107:  id: 'core.prefs', side: 'both',
118:  id: 'core.fairness', side: 'recruiter',
130:  id: 'core.fairness.why', side: 'recruiter',
137:  id: 'core.forget', side: 'both',
156:registerSkill({ id: 'core.thanks', side: 'both', match: (c) => (c.ents.thanks && c.norm.split(' ').length <= 5 ? 0.6 : 0), handle: () => ({ msgs: [{ kind: 'reply', text: 'You’re welcome.' }] }) });
157:registerSkill({ id: 'core.keep', side: 'both', match: (c) => (/^(keep it|leave it|no thanks|not now|never mind|nevermind)$/.test(c.norm) ? 0.7 : 0), handle: () => ({ msgs: [{ kind: 'reply', text: 'Okay, nothing changed.' }], frame: null }) });
159:  id: 'core.lost', side: 'both',
q/skills/agency.ts:233:    const wantsGo = /\b(start|launch|run|send|go|approve|kick off|begin)\b/.test(c.norm);
q/skills/agency.ts:314:    if (/\b(grant|give|approve|allow|let)\b.*\b(tunde|access|see it)\b/.test(c.norm) && c.actor.role !== 'VIEWER') return 0.95;
q/skills/agency.ts:320:    if (/\b(grant|give|approve|allow|let)\b/.test(c.norm) && c.actor.role !== 'VIEWER') {
q/skills/hire-a.ts:235:      if (/\b(approve|aprove|approved|looks good|look good|that is fine|that is good|go ahead|perfect|ok approve|yes)\b/.test(c.norm) && !/\bnot\b/.test(c.norm)) return { msgs: [], frame: frame(R1, 'search', { i
… [1300 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read core fairness and policy

  <details><summary>result</summary>

```
if (!u?.length) return { msgs: [{ kind: 'reply', text: 'There’s nothing I can undo right now. Sent messages and booked meetings can’t be unsent, but I can help write a correction.' }] };
    return { msgs: [{ kind: 'undo', text: `Undo “${u[u.length - 1].label}”?`, actions: [{ label: 'Undo it', primary: true, act: { t: 'do', op: 'undo' } }, { label: 'Keep it', act: { t: 'say', text: 'keep it' } }] }] };
  },
});

registerSkill({
  id: 'core.explain', side: 'both',
  match: (c) => (/\b(what does|what is|what are|what do you mean|meaning of|define|explain)\b/.test(c.norm) && findTerm(c.norm) ? 0.88 : 0),
  handle: (c) => {
    const t = findTerm(c.norm)!;
    const plain = c.w.q.prefs[c.actor.id]?.plain;
    return { msgs: [{ kind: 'reply', text: plain ? `${t.term}: ${brief(t.plain, 1)}` : `${t.term}: ${t.plain}${t.example ? ` For example: ${t.example}` : ''}` }],
      effects: (w, a) => { (w.q.glossarySeen[a.id] ??= []).push(t.key); } };
  },
});

registerSkill({
  id: 'core.honest', side: 'both',
  match: (c) => (/\b(are you (a )?(real|human|person|robot|ai|bot)|who are you|what are you|is this real|are you chatgpt)\b/.test(c.norm) ? 0.9 : 0),
  handle: () => ({ msgs: [{ kind: 'reply', text: 'I’m Q, the assistant inside Talent Q. In this prototype my understanding is a rule-based simulation, not a full AI model: I handle hiring and career tasks and tell you when I don’t understand. Everything I “send” or “book” here is simulated and labelled as such.' }] }),
});

registerSkil
… [5685 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read event and world helper signatures

  <details><summary>result</summary>

```
2:// Every slice is typed; every change worth auditing is a DomainEvent with an actor and a scope.
3-// Scope decides who may ever see an event or record:
4-//   ORG:<id>     members of that organisation (and only them: tenant isolation for agencies)
5-//   PERSON:<id>  that candidate only (private Passport, J7 practice, private memory)
6-//   SHARED:<org>:<person>  both, because the candidate chose to share with that organisation
7-import type { Requirement } from '@contracts';
8-
--
202:export interface DomainEvent { id: string; at: string; actor: string; type: string; scope: string; text: string; data?: Record<string, unknown> }
145:export const now = () => new Date().toISOString();
146-export const uid = (p: string) => `${p}_${Math.random().toString(36).slice(2, 10)}`;
147-
148-export function log(w: World, actor: World['activity'][number]['actor'], text: string) {
--
169:export function emit(w: World, actor: string, type: string, scope: string, text: string, data?: Record<string, unknown>) {
170-  w.events.push({ id: uid('ev'), at: now(), actor, type, scope, text, data });
171-  if (w.events.length > 800) w.events.splice(0, w.events.length - 800);
172-}
--
178:export const simNow = (w: World) => new Date(new Date(w.session.now).getTime() + w.session.offsetDays * 864e5);
179-
180-/** What an organisation may see of a person's Passport: shared items only, never practice, never revoked. */
181-// ---------------- Candidate privacy: one policy for search, profiles, Q's tools
… [980 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check role routes and glossary

  <details><summary>result</summary>

```
20:registerRoute({ path: '/r/mandate', side: 'recruiter', label: 'the role brief', render: () => <OrgOnly orgId="org_kora" what="Kora Pay’s hiring">{legacy(<MandateIntake />)}</OrgOnly> });
23:registerRoute({ path: '/r/roles', side: 'recruiter', label: 'your roles', render: () => <RolesList />, nav: { group: 'Hiring', label: 'Roles', icon: 'roles', tab: true, order: 11, orgKind: 'EMPLOYER' } });
24:registerRoute({ path: '/r/roles/:id', side: 'recruiter', label: 'the role brief', render: (p) => <RoleDetail id={p.id} /> });
12:registerRoute({ path: '/r/people/:id', side: 'recruiter', label: 'a candidate profile', render: (p) => <Profile key={p.id} id={p.id} /> });
19:  rubric: { term: 'Rubric', plain: 'The checklist a reviewer uses to judge a piece of work, so everyone is judged the same way.', aliases: ['rubric'] },
```
  </details>


**Claude** · 2026-10-29 16:15

Now the data layer: helpers in the rubrics slice.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/state/areas/rubrics.ts

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/state/areas/rubrics.ts has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check fixtures and Requirement contract

  <details><summary>result</summary>

```
4:export const ORG = { orgId: 'org_kora', name: 'Kora Pay', recruiterId: 'p_ada', recruiterName: 'Ada Okafor', timezone: 'Africa/Lagos' };
6:export const MANDATE: Mandate = {
24:export const PEOPLE: Person[] = [
35:export const SOURCE_POOL = [
40:export const EVIDENCE: Evidence[] = [
50:export const FITS: RoleFit[] = [
77:export const POLICIES: (PolicyCitation & { title: string; source: string; status: 'ACTIVE' | 'PENDING_REVIEW' })[] = [
85:export const CALENDARS: CalendarConnection[] = [
90:export const PANEL = [
95:export const ADA_PREFS: MeetingPreferences = {
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

… [1978 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/model.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/model.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/ops.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/ops.ts (file state is current in your context — no need to Read it back)
```
  </details>


**Claude** · 2026-10-29 16:19

Now the studio page.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/Studio.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/Studio.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check motion tokens and DS control classes

  <details><summary>result</summary>

```
// Motion tokens (interaction-design skill: feedback 100–200 ms, orientation 200–400 ms, enter slower than
// exit, decelerate in / accelerate out, nothing functional over 500 ms). Every animation in the shell and
// shared components takes its timing from here; reduced motion is handled globally by MotionConfig.
export const DUR = { fast: 0.1, normal: 0.2, slow: 0.3 } as const;
export const EASE = { standard: [0.2, 0, 0, 1], enter: [0, 0, 0.2, 1], exit: [0.4, 0, 1, 1] } as const;
/** Something new arriving in place (a message, a card, a page): rise 6 px and fade in. */
export const arrive = { initial: { opacity: 0, y: 6 }, animate: { opacity: 1, y: 0, transition: { duration: DUR.normal, ease: EASE.enter } }, exit: { opacity: 0, transition: { duration: DUR.fast, ease: EASE.exit } } } as const;
80:.ds-iconbtn { width: 40px; height: 40px; border-radius: 10px; border: 0; background: transparent; color: var(--moon-2); display: grid; place-items: center; flex: none; }
81:.ds-iconbtn:hover { background: var(--night-2); color: var(--moon); }
118:.ds-views { display: inline-flex; background: var(--wash); border-radius: 12px; padding: 4px; gap: 2px; max-width: 100%; overflow-x: auto; scrollbar-width: none; }
119:.ds-views button { border: 0; background: transparent; border-radius: 9px; padding: 8px 14px; min-height: 40px; font-size: 14px; font-weight: 600; color: var(--ink-3); white-space: nowrap; flex: none; }
120:.ds-views button[aria-pressed='true'] { background: var(--sheet); colo
… [1811 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Fix motion token and button class

  <details><summary>result</summary>

```
148:.ds-input { min-height: 44px; padding: 10px 14px; border-radius: var(--r-control); border: 1px solid var(--rule-2); background: var(--sheet); color: var(--ink); font: inherit; font-size: 16px; width: 100%; box-sizing: border-box; }
149:.ds-input:focus-visible { outline: 2px solid var(--gold-ink); outline-offset: 1px; }
150:.ds-banner { display: grid; grid-template-columns: auto 1fr auto; gap: 12px; align-items: center; padding: 12px 16px; border-radius: 12px; border: 1px solid var(--rule-2); background: var(--sheet); }
151:.ds-banner[data-k='risk'] { border-color: var(--risk); }
152:.ds-banner[data-k='warn'] { border-color: var(--warn); }
213:.ds-linkbtn { all: unset; cursor: pointer; font-size: 13px; color: var(--moon-2); text-decoration: underline; text-underline-offset: 3px; justify-self: start; }
214:.ds-linkbtn:focus-visible { outline: 2px solid var(--gold-light); }
277:@media (max-width: 480px) { .ds-banner { grid-template-columns: auto 1fr; } .ds-banner > :nth-child(3) { grid-column: 1 / -1; justify-self: start; } } /* banners stack their action under the text on phones */
[This command modified 1 file you've previously read: journeys/rubric/Studio.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Use local link-button class

  <details><summary>result</summary>

```
2
[This command modified 1 file you've previously read: journeys/rubric/Studio.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/rubric.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/rubric.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/Scorecard.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/Scorecard.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/CandidateRatings.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/CandidateRatings.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Insert candidate ratings into Applications page

  <details><summary>result</summary>

```
9:import { CandidateRatings } from '../rubric/CandidateRatings'; // rubric builder: the person's own ratings (AD-E-14)
63:      <CandidateRatings />
```
  </details>

- 🔧 `Bash`: Find weighting references

  <details><summary>result</summary>

```
journeys/hire-b/Profile.tsx:155:        <Ledger w={w} v={{ people: [id], criteria: reqs.map((r) => r.reqId), lastYear: false, weighting: 'Q' }} ranked={false} bare noKey />
journeys/hire-b/refs.tsx:13:export const viewId = (v: CompareView) => JSON.stringify({ p: v.people, c: v.criteria, y: v.lastYear || undefined, q: v.weighting === 'Q' || undefined });
journeys/hire-b/refs.tsx:14:const toView = (x: ViewId): CompareView => ({ people: x.p, criteria: x.c, lastYear: !!x.y, weighting: x.q ? 'Q' : 'EQUAL' });
journeys/hire-b/refs.tsx:24:      <div className="hire-b-qcard-head"><span className="lab">Who to talk to first</span><span className="t14 muted">{v.lastYear ? 'Last year only · ' : ''}{v.weighting === 'Q' ? 'Q’s weig
journeys/hire-b/refs.tsx:43:            <th scope="row">{shortLabel(w, r)}{weightOf(w, r, v.weighting) > 2 && <span className="hire-b-lcol-x"> 1.5×</span>}<span className="hire-b-qahead">{d === 0 ? 'level' : `${d > 0 ? 
journeys/hire-b/model.ts:108:export type Weighting = 'Q' | 'EQUAL';
journeys/hire-b/model.ts:109:export interface CompareView { people: string[]; criteria: string[]; lastYear: boolean; weighting: Weighting; open?: { pid: string; reqId: string } | null; last?: Snapshot | null }
journeys/hire-b/model.ts:110:export const defaultView = (w: World): CompareView => ({ people: rolePeople(w), criteria: reqsOf(w).map((r) => r.reqId), lastYear: false, weighting: 'Q', open: null });
journeys/hire-b/model.ts:111:/** Q's own judgement: payments is the hardest 
… [3725 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Replace fixed 1.5x weighting with rubric weights

  <details><summary>result</summary>

```
132:  if (v.weighting === 'EQUAL') return `You turned the rubric weights off, so must-haves count the same. Rubric v${rw.v} (approved by ${by}) is unchanged.`;
289:  if (a.weighting !== b.weighting) out.push(b.weighting === 'EQUAL' ? 'weighed the must-haves equally' : 'put the rubric weights back');
```
  </details>

- 🔧 `Bash`: Normalise weighting comparison

  <details><summary>result</summary>

```
289:  if ((a.weighting === 'EQUAL') !== (b.weighting === 'EQUAL')) out.push(b.weighting === 'EQUAL' ? 'weighed the must-haves equally' : 'put the rubric weights back');
[This command modified 1 file you've previously read: journeys/hire-b/model.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Update Ledger to rubric weights

  <details><summary>result</summary>

```
14:import { cellFor, firstName, GLYPH_OF, LEVEL_WORD, nameOf, rank, reqLabel, roleRubric, shortLabel, usesRubric, weighted, weightOf, type Change, type CompareView } from './model';
26:  const crit = weighted(w, v).length ? weighted(w, v) : v.criteria;
// The evidence ledger (R2): one row per person, one block per requirement. Block width is how much the
// requirement counts (must-haves twice a nice-to-have; Q's extra weight on payments is visible as a wider
// block), block shade is how strong the evidence is (one ink hue, light to dark: dataviz ordinal ramp,
```
  </details>

- 🔧 `Bash`: Update ledger comment and Q card refs

  <details><summary>result</summary>

```
24:      <div className="hire-b-qcard-head"><span className="lab">Who to talk to first</span><span className="t14 muted">{v.lastYear ? 'Last year only · ' : ''}{v.weighting !== 'EQUAL' ? 'Rubric weighting' : 'Must-haves equal'}</span></div>
43:            <th scope="row">{shortLabel(w, r)}{weightOf(w, r, v.weighting) > 2 && <span className="hire-b-lcol-x"> 1.5×</span>}<span className="hire-b-qahead">{d === 0 ? 'level' : `${d > 0 ? fa : fb} ahead`}</span></th>
```
  </details>

- 🔧 `Bash`: Use rubric weights in Q reason card

  <details><summary>result</summary>

```
8:import { cellFor, firstName, GLYPH_OF, LEVEL_VALUE, LEVEL_WORD, questionsFor, reqLabel, shortLabel, usesRubric, weight
24:      <div className="hire-b-qcard-head"><span className="lab">Who to talk to first</span><span className="t14 muted"
43:            <th scope="row">{shortLabel(w, r)}{usesRubric(w, v.weighting) && <span className="hire-b-lcol-x"> w{weigh
```
  </details>

- 🔧 `Bash`: Update hire-b Q skills for rubric weights

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Move Compare into hire-b with rubric weights

  <details><summary>result</summary>

```
9:import { useWorld } from '../../mock/world';
10:import { useViewState, runAction } from '../../q/core/engine';
11:import { Canvas } from '../../ds/Workspace';
12:import { Glyph } from '../../ds/Glyph';
13:import { arrive } from '../../ds/motion';
14:import { SwitchRow } from '../../ds/Switch';
15:import { Link } from '../../ui/router';
20:import { roleIndex } from '../../state/areas/rubrics';
```
  </details>

- 🔧 `Bash`: Register studio route and inspect guard

  <details><summary>result</summary>

```
8:export function OrgOnly({ orgId, what, children }: { orgId: string; what: string; children: ReactNode }) {
// Tenant guard for pages that show one organisation's data (e.g. Kora's Senior Backend brief, search and
// comparison). Anyone else who reaches them, by URL or history, sees a permission state instead.
import type { ReactNode } from 'react';
import { actorOf, useWorld } from '../mock/world';
import { Canvas } from '../ds/Workspace';
import { Link } from '../ui/router';

export function OrgOnly({ orgId, what, children }: { orgId: string; what: string; children: ReactNode }) {
  const a = useWorld((w) => actorOf(w));
  const org = useWorld((w) => w.orgs.find((o) => o.id === orgId)?.name ?? 'another organisation');
  if (a.orgId === orgId) return <>{children}</>;
  return (
    <Canvas title="Not available to you" kicker={what} open onClose={() => {}}>
      <section className="ds-sheet" role="alert" style={{ display: 'grid', gap: 12, maxWidth: 640 }}>
        <b>This belongs to {org}.</b>
        <p style={{ margin: 0 }}>Each organisation only sees its own hiring. Nothing from {org} is shown to {a.first}, and nothing of yours is shown to them.</p>
        <Link className="ds-btn" to="/r/home" style={{ justifySelf: 'start' }}>Back to your home</Link>
      </section>
    </Canvas>
  );
}
```
  </details>

- 🔧 `Bash`: Add org-guarded studio route and typecheck

  <details><summary>result</summary>

```
registerRoute({ path: '/r/interviews/:id', side: 'recruiter', label: 'the interview', render: (p) => <InterviewRoom key={p.id} id={p.id} /> });
// Evaluation studio (audit addendum §E). Guarded by the role's organisation, like the comparison.
registerRoute({ path: '/r/roles/:id/rubric', side: 'recruiter', label: 'the evaluation rubric', render: (p) => <StudioRoute key={p.id} id={p.id} /> });
src/journeys/campaigns/model.ts(245,24): error TS6133: 'w' is declared but its value is never read.
[This command modified 1 file you've previously read: journeys/rubric/Studio.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Add scorecard, page index and history to Profile

  <details><summary>result</summary>

```
163:      <section id="pf-fit" className="ds-sheet hire-b-grid" aria-labelledby="pf-fit-h">
164:        <div className="hire-b-row"><h2 id="pf-fit-h" className="voice t24" style={{ margin: 0 }}>Against the Senior Backend brief</h2><Link className="t14" to="/r/compare">Compare with others</Link></div>
180:      <section id="pf-score" className="ds-sheet hire-b-grid" aria-labelledby="pf-score-h">
181:        <div className="hire-b-row"><h2 id="pf-score-h" className="voice t24" style={{ margin: 0 }}>Scorecard</h2>{rIdx.index !== null && <span className="t14 muted num">{indexLine(rIdx)}</span>}</div>
185:      <section id="pf-ev" className="ds-sheet hire-b-grid" aria-labelledby="pf-ev-h">
186:        <div className="hire-b-row"><h2 id="pf-ev-h" className="voice t24" style={{ margin: 0 }}>Shared with {orgName}</h2><span className="t14 muted">{items.length} item{items.length === 1 ? '' : 's'}</span></div>
197:      <section id="pf-q" className="ds-sheet hire-b-grid" aria-labelledby="pf-q-h">
198:        <h2 id="pf-q-h" className="voice t24" style={{ margin: 0 }}>Questions Q would ask {first}</h2>
206:      <section id="pf-hist" className="ds-sheet hire-b-grid" aria-labelledby="pf-hist-h">
207:        <h2 id="pf-hist-h" className="voice t24" style={{ margin: 0 }}>History</h2>
```
  </details>

- 🔧 `Bash`: Check references, add CSS, typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Move history CSS into rubric stylesheet

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Check NLU entities

  <details><summary>result</summary>

```
11:  experiance: 'experience', experince: 'experience', employes: 'employees', applyed: 'applied', aplied: 'applied', jobb: 'job', resumé: 'cv', curriculum: 'cv', comparision: 'comparison', compair: 'compare',
17:export function normalise(text: string) {
29:export function lev(a: string, b: string) {
38:export function near(norm: string, kw: string) {
43:export const anyOf = (norm: string, kws: string[]) => kws.some((k) => (k.includes(' ') ? norm.includes(k) : near(norm, k)));
44:export const countOf = (norm: string, kws: string[]) => kws.filter((k) => (k.includes(' ') ? norm.includes(k) : near(norm, k))).length;
46:export interface Entities {
47:  people: string[]; days: string[]; time?: string; money?: number; moneyText?: string; tone?: 'friendlier' | 'formal' | 'shorter' | 'warmer';
48:  yes: boolean; no: boolean; undo: boolean; back: boolean; correction: boolean; stop: boolean; unsure: boolean; thanks: boolean;
52:export function entities(norm: string, w: World): Entities {
54:  const people = w.people.filter((p) => { const first = p.name.split(' ')[0].toLowerCase(); const last = p.name.split(' ')[1]?.toLowerCase() ?? ''; return ws.some((x) => x === first || x === last || (first.length > 4 && lev(x, first) <= 1)); }).map((p) => p.personId);
67:    people, days, time, money, moneyText, tone,
68:    yes: /^(yes|yeah|yep|yup|sure|ok|okay|go ahead|do it|please do|correct|that is right|sounds good|great|perfect|send it|approve)\b/.test(norm) || /\b(yes please|go ahead|do it)\b
… [97 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read normalise function

  <details><summary>result</summary>

```
export function normalise(text: string) {
  let s = ` ${text.toLowerCase().replace(/[’`]/g, "'")} `;
  for (const [re, rep] of CONTRACTIONS) s = s.replace(re, rep);
  s = s.replace(FILLER, ' ');
  s = s.replace(/[^a-z0-9₦£$%:'\-\s,.?!]/g, ' ');
  // "resume" is a CV only as a noun ("my resume"); "resume the search" stays a verb.
  s = s.replace(/\b(my|a|the|your|her|his|their|upload|send|attach|updated|new|old) resume\b/g, '$1 cv').replace(/\bresume (file|pdf|doc)\b/g, 'cv $1');
  s = s.split(/\s+/).map((t) => TYPOS[t.replace(/[,.?!]/g, '')] ?? t).join(' ');
  return s.replace(/\s+/g, ' ').trim();
}

/** Levenshtein distance, for fuzzy name and keyword matching. */
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/skills/rubric.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/skills/rubric.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Tighten override match and add open skill

  <details><summary>result</summary>

```
1
```
  </details>

- 🔧 `Bash`: Verify edit and view refs card style

  <details><summary>result</summary>

```
254:  match: (c) => (recruiter(c) && /\b(lower|raise|drop|bump|set|change|move|put|mark|rate|override|downgrade|upgrade|reduce|increase)\b/.test(c.norm) && LEVEL_RE.test(c.norm) && !WEIGHT_RE.test(c.norm) && (!onStudio(c) || who(c).length > 0) && overrideTarget(c) ? 0.95 : 0),
        <thead><tr><th scope="col">Requirement</th><th scope="col">{fa}</th><th scope="col">{fb}</th></tr></thead>
        <tbody>{v.criteria.map((r) => { const ca = cellFor(w, x.a, r, v), cb = cellFor(w, x.b, r, v); const d = LEVEL_VALUE[ca.level] - LEVEL_VALUE[cb.level]; return (
          <tr key={r}>
            <th scope="row">{shortLabel(w, r)}{usesRubric(w, v.weighting) && <span className="hire-b-lcol-x"> w{weightOf(w, r, v.weighting)}</span>}<span className="hire-b-qahead">{d === 0 ? 'level' : `${d > 0 ? fa : fb} ahead`}</span></th>
            <td data-ahead={d > 0 ? '1' : undefined}><Mark l={ca.level} />{ca.correction && <span className="t14 muted"> (your correction)</span>}</td>
            <td data-ahead={d < 0 ? '1' : undefined}><Mark l={cb.level} />{cb.correction && <span className="t14 muted"> (your correction)</span>}</td>
          </tr>); })}</tbody>
      </table>
    </div>
  );
}

function QuestionsCard({ id }: { id: string }) {
  const w = useWorld((x) => x);
  if (!w.people.some((p) => p.personId === id)) return null;
  const qs = questionsFor(w, id).slice(0, 4);
  return (
    <div className="hire-b-qcard" role="group" aria-label={`Questions for ${firstName(w, id)}`}>
      <ol c
… [861 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check Q card styling

  <details><summary>result</summary>

```
266:.ds .hire-b-qcard { background: var(--sheet); color: var(--ink); border-radius: 12px; padding: 12px 14px; display: grid; gap: 8px; min-width: 0; --ink-3: var(--ref-ink-600); }
267:.ds .hire-b-qcard .lab { color: var(--ink-3); }
268:.hire-b-qcard-head { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 4px 10px; }
269:.hire-b-qcard .hire-b-lname a { color: var(--ink); }
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/refs.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/refs.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Add compact CSS, import refs, typecheck

  <details><summary>result</summary>

```
21:import './refs';
[This command modified 2 files you've previously read: journeys/rubric/Studio.tsx, journeys/rubric/rubric.css. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Add proactive rubric rules and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Move imports to top and start dev server

  <details><summary>result</summary>

```
// Proactive rules for R2 (Ada). Each reads real, authorised state and says why it is showing.
import { registerRule } from '../core/proactive';
import { visibleEvidence } from '../../mock/world';
import { hireB } from '../../state/areas/hire-b';
import { firstName, koraInterviews, viewerOrg, visibleIds } from '../../journeys/hire-b/model';
import { rubrics, draftVersion } from '../../state/areas/rubrics';
import { approvalNeeds } from '../../journeys/rubric/ops';
import { firstOf as rbFirst, studioPath } from '../../journeys/rubric/model';

// "Tobi uploaded a new verified certificate since you last looked."

  VITE v5.4.21  ready in 352 ms

  ➜  Local:   http://localhost:5193/
  ➜  Network: use --host to expose
```
  </details>

- 🔧 `Bash`: Inspect __tqQA hook and R3 style

  <details><summary>result</summary>

```
prototype/src/main.tsx:10:(window as unknown as { __tqQA: unknown }).__tqQA = { canDiscover, canSeeCandidate, relationshipWith, visibleEvidence, orgLimits, outreachThisWeek, getWorld, update };
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
  // Write the actor, then do a full navigation at once (a hash change f
… [2922 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/qa/scripts/features/rubric.mjs

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/qa/scripts/features/rubric.mjs (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Run rubric feature test on desktop

  <details><summary>result</summary>

```
PASS [d] studio: designed empty state with a way forward
PASS [d] Q proposes v1 (Q_PROPOSED) from brief, guidelines and ESCO
PASS [d] criteria carry anchors 0–4, evidence, questions, method, weight, minimum, requirement, ESCO, why
PASS [d] signals separate: eligibility gate and compatibility outside the index
PASS [d] mentoring left out with a reason (brief does not define it)
FAIL [d] side by side: Q proposed and your version
PASS [d] not-validated statement is visible
FAIL [d] weights shown as share bars with %
PASS [d] weight edited by saying it (incidents and on-call 1 → 2)
PASS [d] edit log records who changed what
PASS [d] Q proposal stays beside the edit ("Q proposed 1")
PASS [d] Q refuses a proxy criterion and says why, with an alternative
PASS [d] Q refuses a protected characteristic (age)
PASS [d] studio field explains the refusal inline
PASS [d] why: job-related reason with the source requirement
PASS [d] approved: v1 APPROVED by Ada, frozen
PASS [d] revisions list: who, when and the diff from Q’s proposal
PASS [d] comparison: weights from rubric v1, approved by Ada
PASS [d] comparison: mentoring not in the rubric, said so
PASS [d] Q proposes Ifeoma’s ratings from shared evidence (not reviewed)
FAIL [d] scorecard: index only with coverage
PASS [d] scorecard: unknown not counted as zero
PASS [d] scorecard: anchor text, Q-proposed and uncertainty per criterion
PASS [d] page index on the long profile (Fit, Scorecard, Evidence, Interview, History)
PASS [d] inspector: t
… [989 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Fix case-sensitive assertions, list captures

  <details><summary>result</summary>

```
d-01-studio-empty.png
d-02-studio-proposed.png
d-03-studio-approved.png
d-04-compare-rubric.png
d-05-profile-scorecard.png
d-06-studio-notice.png
d-07-studio-after-decision.png
d-08-candidate-ratings.png
[This command modified 1 file you've previously read: ../../qa/scripts/features/rubric.mjs. Call Read before editing.]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/rubric/d-02-studio-proposed.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:32

[Image: original 1440x5568, displayed at 517x2000. Multiply coordinates by 2.79 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/rubric/Studio.tsx

  <details><summary>result</summary>

```
125	              <span className="rb-share-v num">{s}%<span className="muted"> · w{c.weight}</span></span>
126	            </li>); })}
127	        </ul>
128	        <p className="t14 muted" style={{ margin: 0 }}>Not in the index: {ver.criteria.filter((c) => !scored(c)).map((c) => `${c.label} (${c.kind === 'ELIGIBILITY' ? 'a gate, met or not met' : c.kind === 'COMPATIBILITY' ? 'the candidate’s side, reported separately' : 'weight 0'})`).join('; ') || 'nothing'}.</p>
129	      </section>
130	
131	      <section className="rb-grid" aria-labelledby="rb-c">
132	        <div className="rb-row"><h2 id="rb-c" className="voice t24" style={{ margin: 0 }}>Criteria</h2>
133	          {narrow ? (
134	            <div className="ds-views rb-side" role="group" aria-label="Which version to show">
135	              <button type="button" aria-pressed={side === 'q'} onClick={() => setSide('q')}>Q proposed</button>
136	              <button type="button" aria-pressed={side === 'you'} onClick={() => setSide('you')}>Your version</button>
137	            </div>
138	          ) : <span className="t14 muted">Q’s proposal on the left, {editing ? 'your editable version' : `v${ver.v} as approved`} on the right</span>}
139	        </div>
140	        <ol className="rb-crits">
141	          {ids.map((cid) => {
142	            const mine = ver.criteria.find((c) => c.id === cid); const q = qCrit.find((c) => c.id === cid);
143	            return (
144	              <li key={cid} className="rb-crit ds-sheet" 
… [3468 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Apply critique fixes to studio layout

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Save first-render captures
- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/rubric/d-05-profile-scorecard.png

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:34

[Image: original 1440x5802, displayed at 496x2000. Multiply coordinates by 2.90 to map to original image.]

- 🔧 `Bash`: Fix scorecard header, rerun desktop test

  <details><summary>result</summary>

```
FAIL [d] weights shown as share bars with %
ERRORS []
RUBRIC: 40/41 steps passed
```
  </details>

- 🔧 `Bash`: Locate failing assertion

  <details><summary>result</summary>

```
55:  step(v, 'weights shown as share bars with %', (await page.locator('.rb-shares .rb-share-bar').count()) >= 4 && /\d+%/.test(await page.locator('.rb-shares').first().innerText()));
```
  </details>

- 🔧 `Bash`: Scope selector to canvas and rerun

  <details><summary>result</summary>

```
RUBRIC: 41/41 steps passed
[This command modified 1 file you've previously read: ../../qa/scripts/features/rubric.mjs. Call Read before editing.]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/rubric/d-02-studio-proposed.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:36

[Image: original 1440x4820, displayed at 598x2000. Multiply coordinates by 2.41 to map to original image.]

- 🔧 `Bash`: Align glyph, weight columns, run phone test

  <details><summary>result</summary>

```
ERRORS []
RUBRIC: 44/44 steps passed
[This command modified 2 files you've previously read: journeys/rubric/rubric.css, journeys/rubric/Studio.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: List phone captures

  <details><summary>result</summary>

```
m-01-studio-empty.png
m-02-studio-proposed.png
m-03-studio-approved.png
m-04-compare-rubric.png
m-05-profile-scorecard.png
m-06-studio-notice.png
m-07-studio-after-decision.png
m-08-candidate-ratings.png
m-09-studio-phone-q.png
m-02-studio-proposed.png (780, 11516)
m-05-profile-scorecard.png (780, 16530)
m-06-studio-notice.png (780, 14008)
```
  </details>

- 🔧 `Bash`: Crop phone captures for review

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/m02a.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/m06a.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Reorder notice before banner, notice lede, sticky nowrap

  <details><summary>result</summary>

```
70:  const notice = editing && ver.changeNotice && affected.length ? ver.changeNotice : null;
76:  const lede = notice ? `v${ver.v} changes how people are scored, and ${list(affected.map((p) => firstOf(w, p)))} ${affected.length === 1 ? 'was' : 'were'} rated on v${base?.v}. Choose how to handle that before it takes effect.` : editing
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/rubric/d-08-candidate-ratings.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Plain-language candidate index copy

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/rubric/d-04-compare-rubric.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:39

[Image: original 1440x2264, displayed at 1272x2000. Multiply coordinates by 1.13 to map to original image.]

- 🔧 `Bash`: Fix repetitive scorecard list and weight labels

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Run R2 and R5 journeys

  <details><summary>result</summary>

```
Command did not complete within its 120s timeout and was moved to the background (ID: b0w8r10fs). Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b0w8r10fs.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. No output had been read from it when it was moved. A program that buffers its output, or a pipe into one such as tail, can keep the output file empty until the command finishes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Read module map and a handoff example

  <details><summary>result</summary>

```
1:# Module map, dependencies and implementation roadmap
10:## 1. Modules
14:| # | Module | Owns (data) | Main responsibilities | Prototype reference |
15:|---|---|---|---|---|
16:| M1 | **Identity and accounts** | users, sessions, signup and verification codes, personal preferences (plain words, voice, proactivity, lite mode) | Signup and verification, choosing a work mode, personalising Q, settings | `routes/entry.tsx` (signup, settings) |
17:| M2 | **Organisations and tenancy** | organisations, members and roles, delegation mode, guidelines, verification status, agency–client links | Organisation setup, team permissions, guidelines Q applies, business verification | `journeys/hire-c/Team.tsx`, `Setup.tsx`; R1 verification |
18:| M3 | **Authorisation and privacy** (service, no UI) | discovery rules, consents, registrations, revocations (or a read model fed by M5) | `canSeeCandidate`, `canDiscover` and `visibleEvidence` for **every** read; the route and tool guard | `mock/world.ts`, `routes/guard.tsx`, `PRIVACY-AND-PERMISSIONS.md` |
19:| M4 | **People and profiles** | candidate profiles, claims in their own words, CV parse results, work history | Onboarding by chat, CV or form; profile editing; claims kept separate from evidence | `journeys/onboarding/*`, `services/profile.ts` |
20:| M5 | **Evidence Passport** | evidence items, files, provenance, verification state, sharing, redaction, revocation | Uploads (resumable), issuer verification, the disclosure matrix, "what X sees"
… [8126 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Wait for R2/R5 results

  <details><summary>result</summary>

```
<tool_use_error>Blocked: sleep 100 followed by: cat /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b0w8r10fs.output. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/rubric.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/rubric.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check R2/R5 output

  <details><summary>result</summary>

```
FAIL [d] [mind] challenge: Q shows reasoning and evidence
FAIL [d] proactive: new verified certificate since last look
FAIL [m] [mind] challenge: Q shows reasoning and evidence
R2: 71/74 steps passed
```
  </details>

- 🔧 `Bash`: Find proactive cert capture

  <details><summary>result</summary>

```
d-13-proactive-cert.png
m-13-proactive-cert.png
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R2/d-13-proactive-cert.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Run R5 and R2 desktop again

  <details><summary>result</summary>

```
Command running in background with ID: bdxi4cz4b. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bdxi4cz4b.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Update R2 challenge expectation

  <details><summary>result</summary>

```
69:  step(v, '[mind] challenge: Q shows reasoning and evidence', /exactly what I used/.test(why) && /No approved rubric for this role yet/.test(why));
```
  </details>

- 🔧 `Bash`: Verify R2 edit

  <details><summary>result</summary>

```
await ask('why do you say tobi is stronger?? thats not fair');
  const why = await lastQ();
  // Rubric pass (AD-B-05): the fixed 1.5x payments rule is gone; Q now says where the weights come from (no approved ru
  step(v, '[mind] challenge: Q shows reasoning and evidence', /exactly what I used/.test(why) && /No approved rubric for
```
  </details>

- 🔧 `Bash`: Rerun rubric test both viewports

  <details><summary>result</summary>

```
RUBRIC: 85/85 steps passed
```
  </details>

- 🔧 `Bash`: Assemble before/after pairs and after captures

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


**Claude** · 2026-10-29 16:45

Let me check the after captures for the phone notice and the candidate view.

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/rubric/03-after.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/rubric.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/rubric.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check R5 and R2 rerun results

  <details><summary>result</summary>

```
67
```
  </details>

- 🔧 `Bash`: Inspect R5 log for failures

  <details><summary>result</summary>

```
ERRORS []
-rw-r--r-- 1 root root 1246 Oct 29 16:45 /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/r2d.log
```
  </details>

- 🔧 `ToolSearch`: select:Monitor

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Wait for R2 desktop rerun result

  <details><summary>result</summary>

```
Command running in background with ID: bevfqbi57. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bevfqbi57.output. You will be notified when it completes. To check interim output, use Read on that file path.
```
  </details>

- 🔧 `Bash`: Run privacy checks

  <details><summary>result</summary>

```
// profiles, Q's tools, cached views and downstream artifacts (campaigns). Usage: node privacy.mjs [base]
PASS saved comparison no longer shows Dayo
PASS Zara withdrew from Kora: nothing visible despite her application
PASS no page errors
All privacy checks passed
```
  </details>

- 🔧 `Bash`: Read R2 desktop rerun result

  <details><summary>result</summary>

```
FAIL [d] proactive: new verified certificate since last look
R2: 36/37 steps passed

[exited with code 0]
```
  </details>

- 🔧 `Bash`: Probe proactive certificate suggestion

  <details><summary>result</summary>

```
[
 "Q NOTICED\n\n“Q4 Engineering Expansion” is due in 52 days, and the Backend Engineer, Payouts brief is still a draft waiting for Bayo.\n\nOpen the campaign\nReview the brief\nWhy am I seeing this?\nLater\nDismiss"
]
[]
```
  </details>

- 🔧 `Bash`: Inspect seen state and proactive limits

  <details><summary>result</summary>

```
[
 "Q NOTICED\n\n“Q4 Engineering Expansion” is due in 52 days, and the Backend Engineer, Payouts brief is still a draft waiting for Bayo.\n\nOpen the campaign\nReview the brief\nWhy am I seeing this?\nLater\nDismiss"
]
{"u_ada":{"p_tobi":{"at":"2026-10-29T16:47:07.148Z","items":["e_hb_tobi_attest:PENDING","e_hb_tobi_site:UNVERIFIED","e_tobi_aws:VERIFIED","e_tobi_go:UNVERIFIED","e_tobi_payout:VERIFIED","e_tobi_pg:VERIFIED","e_tobi_recon:VERIFIED","e_tobi_talk:VERIFIED"]}}}
Q
Q status:
Ready
SIMULATED Q

Q can see:
On Q home · Ada · Kora

Q NOTICED

“Q4 Engineering Expansion” is due in 52 days, and the Backend Engineer, Payouts brief is still a draft waiting for Bayo.

Open the campaign
Review the brief
Why am I seeing this?
Later
Dismiss

Seyi’s invitation to Zara has waited 2 days for a yes.

Open it
Message Q
11:export const registerRule = (r: ProactiveRule) => { if (!rules.some((x) => x.id === r.id)) rules.push(r); };
13:export function evaluateSuggestions(w: World): Suggestion[] {
21:  const quiet = new Set(w.q.suggestions.filter((x) => x.actor === actor.id && (x.state === 'DISMISSED' || x.state === 'DONE' || (x.state === 'SNOOZED' && x.until && new Date(x.until).getTime() > t))).map((x) => x.subject));
38:  return [...out.filter((s) => high.has(s.id)), ...out.filter((s) => !high.has(s.id))].filter((s) => !seen.has(s.subject) && !!seen.add(s.subject));
40:export function useSuggestions() {
47:  const rec: Suggestion = { ...(i >= 0 ? w.q.suggestions[i] : { id, actor: w.sess
… [147 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Probe with update after leaving profile

  <details><summary>result</summary>

```
[
 "Q NOTICED\n\n“Q4 Engineering Expansion” is due in 52 days, and the Backend Engineer, Payouts brief is still a draft waiting for Bayo.\n\nOpen the campaign\nReview the brief\nWhy am I seeing this?\nLater\nDismiss",
 "Q NOTICED\n\nTobi shared a new verified certificate since you last looked: “AWS Solutions Architect – Associate”.\n\nOpen Tobi’s profile\nWhy am I seeing this?\nLater\nDismiss"
]
{"u_ada":{"p_tobi":{"at":"2026-10-29T16:47:28.360Z","items":["e_hb_tobi_attest:PENDING","e_hb_tobi_site:UNVERIFIED","e_tobi_go:UNVERIFIED","e_tobi_payout:VERIFIED","e_tobi_pg:VERIFIED","e_tobi_recon:VERIFIED","e_tobi_talk:VERIFIED"]}}}
Q
Q status:
Ready
SIMULATED Q

Q can see:
On Q home · Ada · Kora
```
  </details>

- 🔧 `Bash`: Find campaign proactive rule owner

  <details><summary>result</summary>

```
q/proactive/hire-a.ts
 M q/proactive/hire-a.ts
 M q/proactive/hire-b.ts
 M q/proactive/hire-c.ts
?? q/proactive/media.ts
```
  </details>

- 🔧 `Bash`: Check MEDIA builder's rating writes

  <details><summary>result</summary>

```
agency.ts
campaigns.ts
core.ts
email.ts
hire-a.ts
hire-b.ts
hire-c.ts
hiring-basic.ts
media.ts
rubric.ts
talent-a.ts
talent-b.ts
talent-c.ts
q/skills/media.ts:293:/** Fallback for "lower postgres to 2, the tuning was on synthetic data" on the video page. The RUBRIC area's own
q/skills/media.ts:297:  match: (c) => (rec(c) && /\b(lower|raise|change|set|drop|bump|move|reduce|increase|make)\b/.test(c.norm) && /\b(to|=)\s*[0-4]\b/.test(c.norm) && !!topicIn(c.norm) && (/^\/r\/people\/p_\w+\/video/.test(c.route) || c.frame?.intent === 'media.report') ? 0.6 : 0),
journeys/media/logic.ts:304:    rs.ratings.push(rating);
```
  </details>

- 🔧 `Bash`: Read MEDIA rating writer

  <details><summary>result</summary>

```
const topic = topicOf(c); const km = topic ? KEY_MOMENTS[topic] : undefined;
    const moments = (km?.moments ?? []).filter((x) => inSeg(x.t)).map((x) => ({ t: x.t, tEnd: x.tEnd, text: quoteFor(m, x.t) }));
    if (!km || !moments.length || km.rating === undefined) { notShown.push(c.id); continue; }
    const partial = moments.length < km.moments.length;
    findings.push({ criterionId: c.id, moments, rating: cf.rubricId ? km.rating : undefined, uncertainty: partial && km.uncertainty === 'LOW' ? 'MEDIUM' : km.uncertainty, note: km.note });
  }
  const r: MediaReview = { id: uid('mr'), mediaId, rubricId, v, personId: m.ownerId, orgId, cacheKey: key, findings, notShown, state: 'Q_DRAFT' };
  s.reviews.push(r);
  emit(w, 'system', 'media.review.built', `ORG:${orgId}`, `Q prepared an evidence report from ${m.ownerId === 'p_tobi' ? 'Tobi' : 'a candidate'}’s shared video (${cf.rubricId ? `rubric v${v}` : 'role brief, no approved rubric'}); cached as ${key}.`, { reviewId: r.id });
  if (cf.rubricId) writeRatings(w, r, m);
  return r;
}
/** Q-proposed Rating records for the RUBRIC scorecard. A reviewed or overridden rating is never touched. */
function writeRatings(w: World, r: MediaReview, m: MediaEvidence) {
  const rs = rubrics(w); if (!rs) return;
  for (const f of r.findings) {
    if (f.rating === undefined) continue;
    const refs = f.moments.map((x) => ({ evidenceId: m.evidenceId, t: x.t, tEnd: x.tEnd, quote: x.text.slice(0, 140) }));
    const existing = rs.ratings.find((x)
… [2375 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Final typecheck, stop my server, list changes

  <details><summary>result</summary>

```
Exit code 144
```
  </details>

- 🔧 `Bash`: Typecheck and list changed files

  <details><summary>result</summary>

```
tsc-done
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
 M ../captures/cx/R1/m-16-roles.png
 M ../captures/cx/R1/m-17-audit.png
 M ../captures/cx/R2/d-01-compare-payments-go.png
 M ../captures/cx/R2/d-02-challenge.png
 M ../captures/cx/R2/d-03-corrected-equal.png
 M ../captures/cx/R2/d-04-profile-tobi.png
 M ../captures/cx/R2/d-05-profile-viewer-outage.png
 M ../captures/cx/R2/d-06-profile-viewer-site.png
 M ../captures/cx/R2/d-07-after-invitation.png
 M ../captures/cx/R2/d-08-compare-last-year.png
 M ../captures/cx/R2/d-09-compare-dispute.png
 M ../captures/cx/R2/d-10-copilot-vague.png
 M ../captures/cx/R2/d-11-feedback-draft.png
 M ../captures/cx/R2/d-12-feedback-submitted.png
 M ../captures/cx/R2/d-13-proactive-cert.png
 M ../captures/cx/R2/d-14-zara-withdrawn.png
 M ../captures/cx/R2/d-15-interviews-list.png
 M ../captures/cx/R2/m-01-compare-payments-go.png
 M ../captures/cx/R2/m-02-challenge.png
 M ../captures/cx
… [7126 more characters trimmed]
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The rubric feature (audit addendum \u00a7E plus J11 steps 5, 8 and 9) is built and working. `qa/scripts/features/rubric.mjs` passes 85 of 85 steps (41 desktop, 44 phone). R5 and `privacy.

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
