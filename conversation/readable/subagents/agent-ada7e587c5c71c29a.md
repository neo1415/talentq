# Helper agent agent-ada7e587c5c71c29a: Email and candidate contact

Source: `agent-ada7e587c5c71c29a.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 16:11

You are the EMAIL builder for Talent Q's product-definition prototype (React + TypeScript + Vite, at /home/user/neo/talent-q-design/prototype). Start by reading /home/user/neo/talent-q-design/journeys/ADDENDUM-BUILD-BRIEF.md completely and everything it lists under "Read first". It is binding.

Your features:
- Addendum E-01, connected email and Q-managed correspondence (requirements E01-01 to E01-30).
- Audit addendum §C, candidate-initiated recruiter correspondence (AD-C-01 to AD-C-09), including the role briefing with transcript on the job page.
- J11 steps 1, 2, 3, 6, 10, 11 and 12 in the brief.

**Extend what exists; this is the core rule.**
- Messages stay in `w.threads` (Msg/Thread, now with optional delivery, senderId, idempotencyKey, approvedHash, campaignId, initiatedBy, state and channel fields).
- The composer extends hire-c's existing drafts: `DraftMeta`, versions and checks in `state/areas/hire-c.ts`, and the Q draft, revise and send flow in `q/skills/hire-c.ts`. Add the sender identity, Cc/Bcc, attachments, approval bound to the content hash, the idempotency key and the truthful delivery statuses to that flow.
- The Messages hub (`journeys/hire-c/Messages.tsx`) becomes the correspondence hub: filters by campaign, role, candidate, channel and state; awaiting reply; reply intelligence. Don't build a new inbox.
- The candidate side extends `CandidateMessages.tsx` and the existing candidate "message the employer" skill in `q/skills/talent-b.ts` (around line 467, the skill matching message/write to/email/contact). You may edit that one skill block, and move it into your own skill file if cleaner.
- Mailboxes, policies, suppressions and follow-ups live in `state/areas/mail.ts`. It is already seeded: Ada's Google Workspace send+read, the shared careers@kora.example, Ngozi's Microsoft 365 send-only, Dele's personal and client senders, Tobi's Gmail send-only, and the Talent Q service sender. Kora allows contact before applying, Medlink after applying, and Rivers not at all.

**Screens to design**, desktop and phone:
- `/settings/email`: register it in `routes/hire-c.tsx` for both sides; the lead will link it from Settings. Covers connect Google / Microsoft / other business email (a simulated consent screen that explains scopes, send-only vs read and reply), connected, expired with reconnect, disconnect and revoke, and personal vs organisation vs shared vs client accounts.
- The sender identity selector in the composer, with what each sender is allowed to do.
- The composer itself: To/Cc/Bcc, subject, body, attachments from Q artifacts, tone, template, signature, draft history, pre-send checks, approve, send, schedule send. Multi-recipient review with per-recipient drafts and statuses.
- Every error and recovery state in E01-23. At minimum, show these live: auth expired, duplicate prevented, bounce, suppressed, rate-limited, offline, and read access denied (send-only mailbox: Q says it can't see replies).
- Reply intelligence: summary, quoted source, extracted times, suggested reply; inbound matched by provider thread, and confirm-the-match when the subject changed.
- The proactive follow-up suggestion with caps, snooze and dismiss.
- Candidate side: the role briefing on `/c/jobs/j_kora_backend` (a simulated 2-minute video player with chapters and transcript; Q answers "is the on-call real?" quoting the time); the contact card showing Kora's policy **before** drafting; Rivers shows its published route and never an invented address; candidate thread statuses (sent, seen if known, replied, timeout, muted, reported, blocked, consent revoked, withdrawn).
- R4: the client sender for Kora is chosen for Kora work, and a client's pre-approved reminder automation can be paused and is obeyed.
- R5 and J11 step 11: "send it from the CEO's gmail" is refused.
- A "Simulate token expiry" demo control (clearly labelled demo, like the existing demo controls) so the journey can force AUTH_EXPIRED.

**Files you own:**
- `journeys/hire-c/*`
- a new `journeys/contact/*` (RoleBriefing, ContactRecruiter); add the job-detail insertion to `journeys/talent-b/Jobs.tsx`, and make that the only edit there
- `q/skills/hire-c.ts`, the one contact skill block in `q/skills/talent-b.ts`, a new `q/skills/email.ts`
- `q/proactive/hire-c.ts`
- `state/areas/hire-c.ts`, `state/areas/mail.ts`, `state/seeds/hire-c.ts`
- `routes/hire-c.tsx`

Agency pages are not yours: report what R4 needs there. Thread routing to a campaign (J11 step 3) uses the `campaigns` slice read-only, plus your own op that sets `thread.campaignId` and `mandateId`.

**Port 5191.** Tests: `qa/scripts/features/email.mjs` and `qa/scripts/features/contact.mjs`. Also run R3, R4, R5, T3 and T5 from `qa/scripts/journeys/` against your build. Usage, as in `run-all.sh`: R5 takes a port number; R3, R4 and T4 take a base URL; the others use env `BASE`. Fix any regression you caused, and update test expectations only where your design legitimately changed them (say which).

Deliverables:
- `journeys/design/email.md`: skills invoked, skill → screen → change, the rendered critique findings and fixes, pairs, remaining weaknesses, and which requirement IDs are now prototyped (with route and test step as evidence).
- `journeys/handoff/email.md`: entities and ownership, provider ports (EmailSendPort, EmailDraftPort, EmailReadPort, MailboxEventsPort, EmailAttachmentPort), Q tools, events, the transactional outbox and idempotency, scopes (Gmail `gmail.send` sensitive vs restricted read; Graph `Mail.Send` vs read), deliverability (SPF, DKIM, DMARC), untrusted-content fencing, sync (Gmail push and history, Graph notifications, IMAP), costs, risks and validation.

Don't commit. Final report: what's built (routes), test results with counts, regressions fixed, requirement IDs prototyped, shared-file requests, and honest remaining gaps.

- 🔧 `Bash`: Read build brief and git status

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
… [8243 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read email addendum
- 🔧 `Bash`: Outline audit addendum

  <details><summary>result</summary>

```
1:# Talent Q: Design Review Audit and Feature Addendum
8:## A. What is actually in the review ZIP
15:## B. Source-grounded findings and issues
30:## C. New feature 1: Candidate-initiated recruiter correspondence
36:## D. New feature 2: Campaign and requisition organization
56:## E. New feature 3: Configurable, role-specific evaluation studio
79:## F. New feature 4: Consent-based video and voice evidence review
91:## G. Other cross-system requirements
97:## H. Deliverables for Claude's next pass
107:## I. Public references for future engineering and legal diligence
```
  </details>


  <details><summary>result</summary>

```
32748 18f408d0-01_VISION_RESEARCH_AND_PRODUCT_EXPERIENCE_MASTER.md
  13607 1fc07cf0-Talent_Q_Design_Audit_and_Feature_Addendum_2026-10-29.md
   6755 2801443f-07_VIDEO_STORYBOARD_AND_VISUAL_REFERENCE.md
  16388 32fd5c9b-Talent_Q_Email_and_Correspondence_Addendum_2026-10-29.md
  60625 3e7963a6-02_COMPLETE_SCREEN_ATLAS_v2.csv
  46285 44e63e80-02_COMPLETE_SCREEN_ATLAS.csv
 156063 4e4534c6-Talent_Q_Complete_Investor_and_Product_Brief.pdf
  60141 5798e144-Talent_Q_Vision_Addendum_v2.pdf
   4820 5ec76ce1-04_FOUNDER_VISION_TRACEABILITY_v2.csv
 151852 74f8747f-TalentQ_Global_Market_Research_and_Commercial_Strategy_v1.pdf
   5455 8d9d1c4b-06_DESIGN_SCOPE_AND_NEXT_RESEARCH.md
  25853 950c6bd2-08_ADDENDUM_SCHEDULING_J7_MEMORY_AND_TOOLING.md
   3582 b10e6fe1-04_FOUNDER_VISION_TRACEABILITY.csv
 204430 bfeb2b17-TalentQ_Technical_Blueprint_v1.pdf
  10180 c125053b-03_MOTION_AND_VIDEO_ATLAS_v2.csv
  16908 d54e237a-00_CLAUDE_START_HERE_v2.md
  10501 d88528a4-05_CLAUDE_DESIGN_FIRST_MASTER_DIRECTIVE.md
   6947 e41b0140-03_MOTION_AND_VIDEO_ATLAS.csv
  40095 eac6715d-TalentQ_User_Journey_Atlas_Stage2.docx
   5571 eb50ca8b-README_SEND_TO_CLAUDE.md
 156063 f7124b8d-Talent_Q_Complete_Investor_and_Product_Brief.pdf
 151852 f81aae10-TalentQ_Global_Market_Research_and_Commercial_Strategy_v1.pdf
1186721 total
# Talent Q | Addendum E-01: Connected Email and Q-Managed Correspondence

**Issued:** 29 October 2026  
**Applies to:** Talent Q full product vision, 183-screen atlas, role/campaign organization, rec
… [16128 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read audit addendum relevant parts

  <details><summary>result</summary>

```
# Talent Q: Design Review Audit and Feature Addendum

**Date:** 29 October 2026  
**Basis:** User-supplied `Talent-Q-Design-Review.zip` and the founder's new requirements.  
**Purpose:** Amend the executable product blueprint, not begin production engineering.  
**Status:** Source inspection + static screen review; full browser runtime not independently exercised due to the review environment blocking local file and localhost navigation. No claim of production integration or exhaustive usability testing.

## A. What is actually in the review ZIP

- 55 distinct named page captures, each in desktop and phone form: 110 full captures. Additional thumbnails duplicate those captures; **not** 110 distinct page designs.
- 41 before/after pairs, 9 short motion MP4 clips, an offline review page, a bundled compiled application, styles and fonts.
- No editable TypeScript source, source-map-backed repository, engineering handoff, full recruiter/candidate master films, or full requirement/implementation traceability package inside this ZIP. Those may remain in Claude's repository.
- Everything in the standalone prototype is explicitly described as simulated. Do not represent screenshots, recordings or interface actions as live recruitment integrations.

## B. Source-grounded findings and issues

| Area | Observed in ZIP | Recommended specification change |
|---|---|---|
| Recruiter home | Ada has two items requiring attention, but Q's adjacent conversation opens with a generic offer of hel
… [6780 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read J11 journey and requirements

  <details><summary>result</summary>

```
# J11: one connected journey for the four addendum features and connected email

Sources: *Talent Q Design Audit and Feature Addendum* (29 Oct 2026) §C–§H, and *Addendum E-01: Connected Email and Q-Managed Correspondence* (29 Oct 2026).
Method: `design-skills:journey-mapping`. This is a **future-state service blueprint**: two people (Tobi and Ada) plus the system behind the line of visibility.
Status: a **proto map**, built from the addenda and the existing cast. No user research sits behind it yet; the open questions are listed at the end.
It extends existing work rather than adding a parallel product:
- the correspondence model (`w.threads`);
- the Senior Backend role (`m_backend`, the legacy `w.mandate`, with listing `j_kora_backend`);
- Tobi's Evidence Passport;
- Kora's people, pipeline and calendar.

## Cast and setting

- **Tobi Adeyemi** (T3): a backend engineer in Lagos. Careful about who sees his work. Mostly on a phone, sometimes a laptop.
- **Ada Okafor** (R2): talent partner at Kora Pay. On desktop at work, on a phone between meetings. Her Google Workspace mailbox (`ada@kora.example`) is connected with **send and read** access.
- **Kora Pay's contact policy:** candidates may message about a role **before applying**, in-app or by email to the role's published address (`careers@kora.example`), up to 2 new threads a week per candidate. Personal recruiter addresses are never shown.
- **Hiring campaign:** "Q4 Engineering Expansion", owned by Ada. It holds Senior Backe
… [16038 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 16:11

Now the shared model.

- 🔧 `Bash`: Read domain diff and mail slice

  <details><summary>result</summary>

```
diff --git a/talent-q-design/prototype/src/state/domain.ts b/talent-q-design/prototype/src/state/domain.ts
index faa33d7..c6564ed 100644
--- a/talent-q-design/prototype/src/state/domain.ts
+++ b/talent-q-design/prototype/src/state/domain.ts
@@ -45,8 +45,112 @@ export const STAGE_LABEL: Record<Stage, string> = { SOURCED: 'Found', SHORTLISTE
 export interface PipelineEntry { mandateId: string; personId: string; stage: Stage; at: string; by: string; note?: string }
 
 export type MsgStatus = 'DRAFT' | 'AWAITING_APPROVAL' | 'QUEUED_OFFLINE' | 'SENT_SIMULATED' | 'RECEIVED' | 'DISCARDED';
-export interface Msg { id: string; from: string; to: string; subject?: string; body: string; at: string; status: MsgStatus; approvedBy?: string; receipt?: string; channel: 'EMAIL' | 'IN_APP' | 'SMS' }
-export interface Thread { id: string; orgId: string; personId: string; mandateId?: string; messages: Msg[] }
+/**
+ * Delivery is a separate axis from approval (addendum E-01 §6, statechart in handoff/ADDENDUM-HANDOFF.md §2):
+ *   APPROVED ─send→ QUEUED ─provider ok→ ACCEPTED ─(provider evidence only)→ DELIVERED
+ *                          └ provider error → FAILED (retryable, e.g. AUTH_EXPIRED) | BOUNCED (final)
+ * "Sent" in the UI means ACCEPTED by the provider, never "received" or "read".
+ */
+export type Delivery = 'QUEUED' | 'ACCEPTED' | 'DELIVERED' | 'BOUNCED' | 'FAILED' | 'CANCELLED';
+export type FailReason = 'AUTH_EXPIRED' | 'DISCONNECTED' | 'SMTP_REJECTED' | 'RATE_LIMITED' | 'SUPPRESS
… [13204 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read hire-c state, seeds, routes, campaigns
- 🔧 `Bash`: Read world.ts and list dirs

  <details><summary>result</summary>

```
// R3 (Ngozi, Kora HR) state slice: structured org guidelines Q checks against, message drafts with versions,
// time proposals, panel changes and reschedule requests. Lives at w.areas['hire-c'] in the one store.
import type { World } from '../../mock/world';

/** What Q can actually check for a guideline. NONE: shown and cited, not machine-checked. */
export type GuideCheck = 'PAY_BAND' | 'PANEL_TWO' | 'APPROVE_EACH' | 'JOB_RELATED' | 'HOURS' | 'NONE';
export interface Guide { id: string; text: string; source: string; check: GuideCheck; on: boolean; v: number; by: string; at: string; used: number; lastUsed?: string }

export type DraftKind = 'INVITE' | 'RESCHEDULE' | 'FOLLOW_UP' | 'REJECTION' | 'REPLY';
export type Tone = 'neutral' | 'friendlier' | 'formal' | 'shorter';
export interface DraftVersion { v: number; at: string; by: string; subject: string; body: string; note: string; manual?: boolean; slot?: { start: string; end: string }; tone?: Tone; panel?: string[] }
export interface Check { id: string; group: 'Approval' | 'Candidate' | 'Calendar' | 'Guidelines' | 'Consent'; label: string; ok: boolean; warn?: boolean; detail: string; fix?: { label: string; op: string; args: Record<string, unknown> } }
export interface DraftMeta {
  msgId: string; threadId: string; personId: string; orgId: string; kind: DraftKind; by: string; tone: Tone;
  slot?: { start: string; end: string }; panel: string[]; mandateId?: string; versions: DraftVersion[];
  checks?: Check[]; checkedAt?: stri
… [9961 more characters trimmed]
```
  </details>


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
… [14431 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read hire-c lib

  <details><summary>result</summary>

```
<persisted-output>
Output too large (48.7KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b1htf30fr.txt

Preview (first 2KB):
// R3 logic shared by Q's skills and the pages: time zones, free/busy, slot finding, drafting templates,
// the pre-send checks (approval and delegation, candidate, calendar, guidelines, consent) and the simulated send.
// Nothing here really sends or books: statuses say SENT_SIMULATED and receipts are fake.
import { actorOf, emit, now, orgLimits, orgOf, outreachThisWeek, personOf, simNow, uid, type World } from '../../mock/world';
import { appendQ } from '../../q/core/engine';
import type { Actor, CalEvent, Msg, OrgRole, Stage, Thread } from '../../state/domain';
import { STAGE_LABEL } from '../../state/domain';
import { hc, hcw, type Check, type DraftKind, type DraftMeta, type Guide, type Slot, type Tone } from '../../state/areas/hire-c';

// ---------------- Time ----------------
export const LAGOS = 'Africa/Lagos';
const CITY: Record<string, string> = { 'Africa/Lagos': 'Lagos', 'Europe/London': 'London', 'Africa/Accra': 'Accra', 'Africa/Nairobi': 'Nairobi' };
export const city = (tz: string) => CITY[tz] ?? tz.split('/').pop()!.replace(/_/g, ' ');
const f = (iso: string, tz: string, o: Intl.DateTimeFormatOptions) => new Intl.DateTimeFormat('en-GB', { timeZone: tz, ...o }).format(new Date(iso));
export const tTime = (iso: string, tz: string) => f(iso, tz, { hour: '2-digit', minute: '2-
… [625 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/lib.ts

  <details><summary>result</summary>

```
1	// R3 logic shared by Q's skills and the pages: time zones, free/busy, slot finding, drafting templates,
2	// the pre-send checks (approval and delegation, candidate, calendar, guidelines, consent) and the simulated send.
3	// Nothing here really sends or books: statuses say SENT_SIMULATED and receipts are fake.
4	import { actorOf, emit, now, orgLimits, orgOf, outreachThisWeek, personOf, simNow, uid, type World } from '../../mock/world';
5	import { appendQ } from '../../q/core/engine';
6	import type { Actor, CalEvent, Msg, OrgRole, Stage, Thread } from '../../state/domain';
7	import { STAGE_LABEL } from '../../state/domain';
8	import { hc, hcw, type Check, type DraftKind, type DraftMeta, type Guide, type Slot, type Tone } from '../../state/areas/hire-c';
9	
10	// ---------------- Time ----------------
11	export const LAGOS = 'Africa/Lagos';
12	const CITY: Record<string, string> = { 'Africa/Lagos': 'Lagos', 'Europe/London': 'London', 'Africa/Accra': 'Accra', 'Africa/Nairobi': 'Nairobi' };
13	export const city = (tz: string) => CITY[tz] ?? tz.split('/').pop()!.replace(/_/g, ' ');
14	const f = (iso: string, tz: string, o: Intl.DateTimeFormatOptions) => new Intl.DateTimeFormat('en-GB', { timeZone: tz, ...o }).format(new Date(iso));
15	export const tTime = (iso: string, tz: string) => f(iso, tz, { hour: '2-digit', minute: '2-digit', hourCycle: 'h23' });
16	export const tDay = (iso: string, tz: string) => f(iso, tz, { weekday: 'short', day: 'numeric', month: 'short' });
17	export
… [50271 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Messages hub
- 🔧 `Bash`: Read candidate messages page
- 🔧 `Bash`: Read Q types and engine start
- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/q/skills/hire-c.ts

  <details><summary>result</summary>

```
1	// R3 skills (area hire-c): drafting correspondence for every recruiter journey (draft → edit with a version
2	// diff → checks → explicit approval → simulated send), finding times across time zones, holds, panels,
3	// the pipeline (move with undo, reject with a reason), team roles, org guidelines, and the candidate side
4	// (confirm, reschedule, reply). Everything is reachable by typing; pages show and refine the same state.
5	import { actorOf, emit, getWorld, now, orgOf, personOf, uid, update, type World } from '../../mock/world';
6	import type { Actor, OrgRole, QFrame, QMsg, Stage } from '../../state/domain';
7	import { STAGE_LABEL } from '../../state/domain';
8	import { appendQ, pushUndo, registerOp, registerSkill } from '../core/engine';
9	import { anyOf, entities, normalise } from '../core/nlu';
10	import { protectedCriterion } from '../core/policy';
11	import type { QCtx, QReply } from '../core/types';
12	import { hc, hcw, type DraftKind, type Guide, type Tone } from '../../state/areas/hire-c';
13	import {
14	  approveAndSend, busyAt, CAN_MOVE, CAN_SEND, changePanel, checkDraft, city, colleaguesIn, createDraft, currentDraft, dateIn, defaultPanel, entryFor, findMsg, findSlots, firstOf,
15	  flushQueued, guide, guideChip, problemOf, guidesOf, IS_ADMIN, KIND_LABEL, LAGOS, latestV, listNames, mandateTitle, nameOf, nextWeek, orgMembers, parseTime, partOf, payBand, resolveDays,
16	  reviseDraft, ROLE_CAN, ROLE_LABEL, setStage, STAGE_WORDS, syncOrgGuidelines, tDay, tTime,
… [41921 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// /r/messages: the correspondence inbox. Threads per candidate, drafts with versions, the checks Q ran,
// and approve / edit / discard. There is no way to send that skips the checks and an explicit approval.
// Design pass: dense list with one status per row, a thread that separates their words from ours, sent
// messages that read as receipts, and a draft panel whose primary action is always the next honest step.
import { useEffect, useMemo, useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { actorOf, orgOf, personOf, simNow, useWorld } from '../../mock/world';
import { Canvas, useNarrow } from '../../ds/Workspace';
import { arrive } from '../../ds/motion';
import { runAction, useViewState } from '../../q/core/engine';
import { Link } from '../../ui/router';
import { hc } from '../../state/areas/hire-c';
import type { Msg } from '../../state/domain';
import { CAN_SEND, CHANNEL_LABEL, city, delivered, diffWords, firstOf, KIND_LABEL, LAGOS, mandateTitle, msgStatusLabel, nameOf, tDay, tTime, whenText } from './lib';
import { ChecksList } from './refs';

type Filter = 'all' | 'approval' | 'drafts' | 'reply' | 'queued' | 'sent';
const FILTERS: [Filter, string][] = [['all', 'All'], ['approval', 'To approve'], ['drafts', 'Drafts'], ['reply', 'Need a reply'], ['queued', 'Queued'], ['sent', 'Sent']];
const when = (iso: string) => `${tDay(iso, LAGOS)}, ${tTime(iso, LAGOS)}`;
const initials = (n: string) => n.split(' ').map((x) => x[0]).slice(0, 
… [14256 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// Candidate side of correspondence (/c/messages) and interview times (/c/slots). Candidates see only what was
// actually sent to them (never drafts), in their own time zone, with an honest status. Replying, confirming
// and asking to move are explicit button presses; Q can do the same by typing.
// Design pass (creative, within Direction D's candidate warmth): the page speaks to the person by name, puts
// the next step first as a personal "ticket", shows the conversation as a conversation (their words left,
// yours right), and reassures without promising anything an employer hasn't decided.
import { useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { actorOf, orgOf, simNow, useWorld, type World } from '../../mock/world';
import { Canvas, useNarrow } from '../../ds/Workspace';
import { arrive, DUR, EASE } from '../../ds/motion';
import { runAction, useViewState } from '../../q/core/engine';
import type { CalEvent, Msg } from '../../state/domain';
import { addDays, city, evStatusLabel, LAGOS, nameOf, nextWeek, offsetOf, tDay, tLong, tTime } from './lib';
import { SlotPicker } from '../../screens/SlotPicker';

const visible = (m: Msg, pid: string) => m.from === pid ? m.status !== 'DISCARDED' : m.status === 'SENT_SIMULATED' || m.status === 'RECEIVED';
export function candidateThreads(w: World, pid: string) {
  const byOrg = new Map<string, { orgId: string; threadId: string; msgs: Msg[] }>();
  for (const t of w.threads.filter((x) => x.pe
… [16033 more characters trimmed]
```
  </details>


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

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/q/skills/hire-c.ts

  <details><summary>result</summary>

```
449	  const [h0, h1] = [guide(w, a.orgId, 'HOURS')?.text.match(/\d{1,2}[:.]\d{2}\s*[–-]\s*\d{1,2}[:.]\d{2}/)?.[0] ?? '09:00–17:00', ''];
450	  void h1;
451	  const abroad = [...panel, pid].filter((id) => tzOf(w, id) !== LAGOS);
452	  const zoneLine = abroad.length ? ` ${listNames(abroad.map((id) => `${firstOf(w, id)} is in ${city(tzOf(w, id))} (${tzNote(tzOf(w, id), `${days[0]}T12:00:00Z`)})`))}, so I’ve only kept times inside everyone’s working day and show each person’s local time.` : ' Everyone is on Lagos time.';
453	  const dayText = c.ents.days.includes('next week') || !c.ents.days.length ? (req && !c.ents.days.length ? `on the day ${first} asked for` : 'next week') : days.map((x) => tDay(`${x}T12:00:00Z`, LAGOS)).join(', ');
454	  const used = [`Calendars: ${listNames(panel.map((id) => firstOf(w, id)))} (busy times only)`, `${first}: ${city(tzOf(w, pid))} time`, ...abroad.filter((x) => x !== pid).map((id) => `${firstOf(w, id)}: ${city(tzOf(w, id))} time`), ...(guide(w, a.orgId, 'HOURS') ? [guideChip(guide(w, a.orgId, 'HOURS')!)] : []), ...(req ? [`${first}’s request: “${req.text}”`] : [])];
455	  if (!slots.length) return { msgs: [{ kind: 'reply', text: `I couldn’t find 45 minutes ${dayText} when ${listNames([...panel.map((id) => firstOf(w, id)), first])} are all free within interview hours (${h0} Lagos).${zoneLine} Options: try the week after, widen the hours, or change the panel.`, used,
456	    actions: [{ label: 'Try the week after', act: { t: 'say', text: `find a 
… [28663 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read talent-b skill and proactive hire-c

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
… [13355 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read refs and Jobs structure

  <details><summary>result</summary>

```
// Live cards Q shows inside its replies for R3: a draft at a given version (or its simulated-send receipt),
// what changed between versions, the pre-send checks, and proposed interview times with everyone's local time.
// Design pass: each card leads with the facts a person decides on (who, when, status), and keeps long text
// (message bodies, word-level changes, check details) one tap away, so the card reads in the phone Q sheet.
import { useState } from 'react';
import { motion } from 'motion/react';
import { useWorld } from '../../mock/world';
import { DUR, EASE } from '../../ds/motion';
import { hc } from '../../state/areas/hire-c';
import type { Check } from '../../state/areas/hire-c';
import { registerRef } from '../../q/refs';
import { CHANNEL_LABEL, city, diffWords, findMsg, firstOf, GUIDE_SHORT, guidesOf, problemOf, LAGOS, msgStatusLabel, nameOf, tDay, tTime, tzOf, versionChanges, whenText } from './lib';

const STATUS_SHORT: Record<string, string> = { DRAFT: 'Draft', AWAITING_APPROVAL: 'Ready for approval', QUEUED_OFFLINE: 'Queued: offline', SENT_SIMULATED: 'Sent (simulated)', RECEIVED: 'Received', DISCARDED: 'Discarded' };

function Facts({ rows }: { rows: [string, React.ReactNode][] }) {
  return <dl className="hc-facts">{rows.map(([k, v]) => <div key={k}><dt>{k}</dt><dd>{v}</dd></div>)}</dl>;
}

/** Message body, clamped when long, with an explicit "show all" (never a silent cut). */
export function Body({ text, lines = 7 }: { text: string; lines?: number }) {
… [3520 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read job detail page

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

/** Location and work mode without repeating each other (“Remote · remote”). */
const where = (loc: string, mode: string) => (loc.toLowerCase().includes(mode.toLowerCase()) ? loc : `${loc} · ${mode.toLowerCase()}`);

const act = (op: string, args: Record<string, unknown> = {}) => void runAction({ label: op, act: { t: 'do', op, args } });
type F = 'all' | 'verified' | 'saved' | 'remote';

function Signals({ job, compact }: { job: Job; compact?: boolean }) {
        </ul>
      </details>
    </Canvas>
  );
}

export function JobDetailPage({ id }: { id: string }) {
  const w = useWorld((x) => x);
  const a = actorOf(w); const pid = a.personId!;
  const job = w.jo
… [9663 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Look at QA scripts

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

… [4750 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find __tqQA and test steps

  <details><summary>result</summary>

```
prototype/src/main.tsx:10:(window as unknown as { __tqQA: unknown }).__tqQA = { canDiscover, canSeeCandidate, relationshipWith, visibleEvidence, orgLimits, outreachThisWeek, getWorld, update };
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
film.mjs
5:  step('Proactive: Seyi’s unapproved draft to Zara is flagged, not sent', /Seyi.*Zara.*hasn’t been approved, so it hasn’t been sent/s.test(sugg), sugg.slice(0, 200));
7:  step('Proactive: reminder that Grace hasn’t replied (from real state)', /Grace hasn’t replied/.test(sg), sg.slice(0, 200));
10:  step('Curveball [recover]: sending an unapproved draft → checks first, nothing sent', /haven’t sent it/i.test(r) && /pay band/i.test(r) && /busy/i.test(r) && !msgsTo(await world(page), 'p_zara').some((m) => m.status 
… [4971 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Size design docs and read gate

  <details><summary>result</summary>

```
114 design-system/DIRECTION-D-SYSTEM.md
   16 handoff/DESIGN-QUALITY-GATE.md
   79 journeys/DESIGN-PASS-BRIEF.md
   73 journeys/design/hire-b.md
   88 handoff/PRIVACY-AND-PERMISSIONS.md
   77 handoff/MODULE-MAP-AND-ROADMAP.md
  447 total
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
# Design quality gate

From now on, no journey moves from "it works" straight to recording. Each journey, and each new screen within one, passes these checkpoints in order. Keep it light: the output is better screens, not paperwork.

| # | Checkpoint | What happens | Proof it happened |
|---|---|---|---|
| 1 | Design research and skills, **before** building | Load the relevant skills and apply them to the brief: `design-critique`, `design-elevation`, `interaction-design`, `ux-writing`, plus `dataviz` for any chart or ledger and `design-superpowers:creative` for the candidate surfaces | One line per skill in the journey's design note: which screens it shaped |
| 2 | Visual implementation | Build with `src/ds` components and the execution rules in `design-system/DIRECTION-D-SYSTEM.md`. Fix shared problems in the shared component, not on one page | — |
| 3 | Browser rendering | `qa/scripts/review/capture-all.mjs` captures every page in the journey at desktop 1440 and phone 390, plus its key states | `captures/review/after/` |
| 4 | Visual critique | Look at eve
… [935 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Direction D and design pass brief

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
… [10695 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read example design note, privacy, module map

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
… [11697 more characters trimmed]
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:interaction-design", "args": "Email composer and correspondence states for Talent Q (send status statechart, approval bound to content hash, error/recovery states, reconnect f

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-29 16:12

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


ARGUMENTS: Email composer and correspondence states for Talent Q (send status statechart, approval bound to content hash, error/recovery states, reconnect flow)

- 🔧 `Skill`: {"skill": "design-skills:ux-writing", "args": "Error and recovery messages for connected email (auth expired, bounce, suppressed, rate-limited, duplicate prevented, read denied), consent scope screens

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-29 16:12

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


ARGUMENTS: Error and recovery messages for connected email (auth expired, bounce, suppressed, rate-limited, duplicate prevented, read denied), consent scope screens, and candidate contact policy card

- 🔧 `Skill`: {"skill": "design-skills:design-elevation", "args": "Settings email page, composer and role briefing player within Direction D"}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-29 16:12

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


ARGUMENTS: Settings email page, composer and role briefing player within Direction D

- 🔧 `Skill`: {"skill": "design-skills:design-critique", "args": "Will critique rendered captures of /settings/email, composer, messages hub, role briefing and candidate messages"}

  <details><summary>result</summary>

```
Launching skill: design-skills:design-critique
```
  </details>


**User** · 2026-10-29 16:12

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
… [2970 more characters trimmed]

- 🔧 `Bash`: Read domain types and actors

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
… [6801 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Survey R5, R4, T3, T5 tests

  <details><summary>result</summary>

```
44:  step(v, 'home shows what is waiting on Bayo', /Waiting on you/i.test(await page.locator('#ds-content').innerText()) && /Backend Engineer, Payouts/.test(await page.locator('#ds-content').innerText()));
46:  await page.locator('.ds-suggest-more[aria-expanded="false"]').first().click({ timeout: 600 }).then(() => page.waitForTimeout(350)).catch(() => {}); step(v, 'proactive: draft waiting on him for over a day', await page.locator('.ds-suggest').filter({ hasText: /Payouts.*has been a draft since/ }).count() > 0);
52:  step(v, 'Kora intake starts the Senior Backend brief from Q', (await route()) === '/r/mandate' && /hybrid in Lagos, onsite, or open to remote/.test(await lastQ()));
53:  step(v, 'no second conversation on the brief page', (await page.locator('.split-conv, .ds-canvas .ds-compose').count()) === 0);
57:  step(v, 'answers applied to the brief', w.mandate.workMode === 'HYBRID' && w.mandate.requirements[0].label === 'Payments systems' && /Approve it and I’ll start searching/.test(await lastQ()));
62:  step(v, 'approval starts the search; result arrives in Q', w.mandate.status !== 'DRAFT' && w.sourcing.done && /I read 24 profiles/.test(await lastQ(3)), await lastQ(2));
67:  step(v, 'approval asked with the exact version', (await lastKind()) === 'approval' && /Approve “Backend Engineer, Payouts” v1/.test(await lastQ()));
69:  step(v, 'Bayo approves the brief (hiring manager may)', (await payouts()).status === 'APPROVED');
72:  step(v, 'search for Payouts runs (Kora poo
… [5573 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List utterances in T tests

  <details><summary>result</summary>

```
T3.mjs:45:  let r = await ask('can u uplaod a work sample, the payouts design doc', 400);
T3.mjs:51:  r = await ask('open my applications'); await page.waitForTimeout(300);
T3.mjs:52:  r = await ask('pls retry the upload', 400);
T3.mjs:57:  r = await ask('go back', 600);
T3.mjs:62:  r = await ask('whats happening with my aws certificate?? its been pending forever');
T3.mjs:64:  r = await ask('check the aws cert again pls', 2400);
T3.mjs:66:  r = await ask('ok check my aws cert again', 2400);
T3.mjs:71:  r = await ask('my aws cert failed, what do i do now??');
T3.mjs:77:  r = await ask('can you send kora the original fraud doc, its fine honestly');
T3.mjs:80:  r = await ask('ugh just send it anyway nobody will know');
T3.mjs:82:  r = await ask('ok fine make the redacted summary');
T3.mjs:91:  r = await ask('what does talentbridge see of my stuff');
T3.mjs:94:  r = await ask('stop talentbridge seeing my code');
T3.mjs:100:  r = await ask('actually undo that');
T3.mjs:103:  r = await ask('no wait, stop talentbridge seeing my code. for real this time');
T3.mjs:123:  r = await ask('how do you describe me to employers');
T3.mjs:125:  r = await ask('thats not fair, i led the payouts team of 4 at Lumen for 2 yrs');
T3.mjs:130:  r = await ask('let agencies find me too');
T3.mjs:132:  r = await ask('hmm actually no. stop agencies finding me');
T3.mjs:138:  r = await ask('help me prepare for my medlink intervew');
T5.mjs:45:  let r = await ask('is rivers logistics even legit? feels dodg
… [3183 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read route registry

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
… [1373 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 16:12

Let me start the dev server and capture current states.

- 🔧 `Bash`: Start dev server on port 5191

  <details><summary>result</summary>

```
VITE v5.4.21  ready in 611 ms

  ➜  Local:   http://localhost:5191/
  ➜  Network: use --host to expose
axe-all.mjs
capture-all.mjs
gallery
interview-followup.mjs
keyboard.mjs
motion-clips.mjs
privacy.mjs
```
  </details>

- 🔧 `Bash`: Write capture script and take before shots

  <details><summary>result</summary>

```
desktop msgs overflow 0 
phone msgs overflow 0 
desktop job overflow 0 
phone job overflow 0 
desktop cmsgs overflow 0 
phone cmsgs overflow 0
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before/msgs-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before/job-phone.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:14

[Image: original 780x5264, displayed at 296x2000. Multiply coordinates by 2.64 to map to original image.]

- 🔧 `Bash`: Check seed NOW, Tobi, calendars

  <details><summary>result</summary>

```
6:export const NOW = '2026-10-29T09:00:00+01:00';
95:export const CAL: CalEvent[] = [
102:export const INTERVIEWS: Interview[] = [
19:  { id: 'p_tobi', name: 'Tobi Adeyemi', first: 'Tobi', initials: 'TA', side: 'candidate', title: 'Senior backend engineer', timezone: 'Africa/Lagos', personId: 'p_tobi', journey: 'T3', email: 'tobi@mail.example', signedUp: true },
46:  { mandateId: 'm_backend', personId: 'p_tobi', stage: 'SHORTLISTED', at: '2026-10-24', by: 'u_ada' },
63:  ev({ evidenceId: 'e_tobi_conf', ownerId: 'p_tobi', kind: 'PROJECT', title: 'Fraud-rules engine at Lumen (confidential)', source: 'Private document', observedAt: '2026-07-01', verified: false, verification: 'UNVERIFIED', confidential: true, shows: 'Designed the rules engine that blocks fraudulent payouts.', limits: 'Confidential under NDA; cannot be shared as-is.' }),
64:  ev({ evidenceId: 'e_tobi_aws', ownerId: 'p_tobi', kind: 'CREDENTIAL', title: 'AWS Solutions Architect – Associate', source: 'Uploaded certificate', observedAt: '2025-03-10', verification: 'PENDING', shows: 'Passed the associate-level cloud architecture exam.', limits: 'Issuer check pending.' }),
state/seeds/hire-b.ts:22:  calendar: [
state/seeds/hire-c.ts:15:  calendar: [
state/seeds/talent-b.ts:29:  calendar: [
```
  </details>

- 🔧 `Bash`: Check calendar seeds

  <details><summary>result</summary>

```
export const CAL: CalEvent[] = [
  { id: 'c1', orgId: 'org_kora', title: 'Busy', start: '2026-11-03T10:00:00+01:00', end: '2026-11-03T11:00:00+01:00', attendees: ['u_ngozi'], status: 'CONFIRMED', simulated: true },
  { id: 'c2', orgId: 'org_kora', title: 'Busy', start: '2026-11-03T14:00:00+01:00', end: '2026-11-03T15:30:00+01:00', attendees: ['u_seyi'], status: 'CONFIRMED', simulated: true },
  { id: 'c3', orgId: 'org_kora', title: 'Busy', start: '2026-11-04T09:00:00+00:00', end: '2026-11-04T12:00:00+00:00', attendees: ['u_musa'], status: 'CONFIRMED', simulated: true },
  { id: 'c4', orgId: 'org_kora', title: 'Interview: Grace Okon (Support Lead)', start: '2026-10-30T11:00:00+01:00', end: '2026-10-30T11:45:00+01:00', attendees: ['u_ngozi', 'p_grace'], status: 'INVITED', mandateId: 'm_support', personId: 'p_grace', simulated: true },
];

export const INTERVIEWS: Interview[] = [
  { id: 'i_grace', orgId: 'org_kora', mandateId: 'm_support', personId: 'p_grace', eventId: 'c4', panel: ['u_ngozi'], status: 'INVITED', feedback: [] },
];

export const consentFor = (personId: string): Consent => ({ personId, discoverable: personId !== 'p_grace', withdrawnFrom: [], notifications: { email: true, sms: personId === 'p_grace', inApp: true, digest: 'WEEKLY' }, lite: false });
export const defaultPrefs = (a: Actor): QPrefs => ({ proactive: 'NORMAL', voice: a.id !== 'p_grace', plain: a.id === 'u_funmi' || a.id === 'p_grace' });
      feedback: [{ by: 'u_musa', rating: 'CONCERNS', notes: 'The 
… [4592 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Survey tokens, ds classes, Switch, Canvas

  <details><summary>result</summary>

```
--color-action     --color-bg     --color-focus     --color-info     --color-line     --color-line-strong     --color-ok     --color-on-action     --color-on-q     --color-paper     --color-paper-line     --color-paper-muted     --color-paper-q-text     --color-paper-raised     --color-paper-text     --color-q     --color-q-strong     --color-q-text     --color-risk     --color-surface     --color-surface-raised     --color-surface-sunken     --color-text     --color-text-muted     --color-text-subtle     --color-warn   --color-action   --color-bg   --color-focus   --color-info   --color-line   --color-line-strong   --color-ok   --color-on-action   --color-on-q   --color-paper   --color-paper-line   --color-paper-muted   --color-paper-q-text   --color-paper-raised   --color-paper-text   --color-q   --color-q-strong   --color-q-text   --color-risk   --color-surface   --color-surface-raised   --color-surface-sunken   --color-text   --color-text-muted   --color-text-subtle   --color-warn   --font-mono   --font-ui   --font-voice   --motion-base   --motion-ease-in-out   --motion-ease-out   --motion-instant   --motion-quick   --motion-settle   --motion-slow   --radius-lg   --radius-md   --radius-pill   --radius-sm   --radius-xl   --ref-amber-dark   --ref-amber-light   --ref-blue-dark   --ref-blue-light   --ref-gold-300   --ref-gold-400   --ref-gold-500   --ref-gold-600   --ref-gold-700   --ref-gold-800   --ref-gold-900   --ref-green-dark   --ref-green-light   --ref-ink-100   --ref-
… [3367 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check pipeline and Dayo usage

  <details><summary>result</summary>

```
prototype/src/state/seed.ts:46:  { mandateId: 'm_backend', personId: 'p_tobi', stage: 'SHORTLISTED', at: '2026-10-24', by: 'u_ada' },
prototype/src/state/seed.ts:47:  { mandateId: 'm_backend', personId: 'p_ife', stage: 'SHORTLISTED', at: '2026-10-24', by: 'u_ada' },
prototype/src/state/seed.ts:48:  { mandateId: 'm_backend', personId: 'p_kunle', stage: 'SHORTLISTED', at: '2026-10-24', by: 'u_ada' },
prototype/src/state/seed.ts:49:  { mandateId: 'm_backend', personId: 'p_zara', stage: 'REPLIED', at: '2026-10-27', by: 'u_ngozi', note: 'Applied via the Kora job page' },
prototype/src/state/seed.ts:72:  { id: 'j_kora_backend', orgId: 'org_kora', mandateId: 'm_backend', title: 'Senior Backend Engineer', location: 'Lagos', workMode: 'HYBRID', pay: '₦2.4m–₦3.1m / month', posted: '2026-10-22', status: 'OPEN', needs: ['Payments systems', 'Go in production', 'Postgres at scale'], signals: { domainVerified: true, registryVerified: true, recruiterActive: true, replies: 'Usually replies within 3 days' } },
prototype/src/state/seed.ts:89:  { id: 't_zara_kora', orgId: 'org_kora', personId: 'p_zara', mandateId: 'm_backend', messages: [
prototype/src/state/seeds/hire-b.ts:17:    { id: 'i_hb_ife', orgId: 'org_kora', mandateId: 'm_backend', personId: 'p_ife', eventId: 'c_hb_ife', panel: ['u_ada', 'u_musa'], status: 'CONFIRMED', feedback: [] },
prototype/src/state/seeds/hire-b.ts:18:    { id: 'i_hb_tobi', orgId: 'org_kora', mandateId: 'm_backend', personId: 'p_tobi', panel: ['u_ada', 'u_musa'], s
… [1740 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Dayo and mandates

  <details><summary>result</summary>

```
state/seed.ts:53:  { mandateId: 'm_kora_agency', personId: 'p_dayo', stage: 'SHORTLISTED', at: '2026-10-26', by: 'u_dele' },
state/seeds/agency.ts:26:  registrations: [...['p_tb_bisi', 'p_tb_femi', 'p_tb_halima', 'p_tb_kemi', 'p_tb_nneka', 'p_tb_obinna', 'p_tb_ruth', 'p_tb_segun', 'p_tb_yemi'], 'p_dayo'].map((personId) => ({ personId, orgId: 'org_tb' })),
state/seeds/agency.ts:41:    pe('m_tb_kora_pay', 'p_tb_femi', 'SHORTLISTED', '2026-10-26'), pe('m_tb_kora_pay', 'p_tb_halima', 'SHORTLISTED', '2026-10-26'), pe('m_tb_kora_pay', 'p_tb_yemi', 'SOURCED', '2026-10-26', 'u_tunde'), pe('m_tb_kora_pay', 'p_dayo', 'SOURCED', '2026-10-26'),
mock/fixtures.ts:29:  { personId: 'p_dayo', name: 'Dayo Lawal', headline: 'Engineering lead, lending · 11 yrs', location: 'London', timezone: 'Europe/London', synthetic: true },
mock/fixtures.ts:36:  'p_tobi', 'p_zara', 'p_ife', 'p_dayo', 'p_kunle',
state/seed.ts:41:  { id: 'm_kora_agency', orgId: 'org_tb', clientOrgId: 'org_kora', title: 'Backend Engineer (Kora Pay, via agency)', plain: 'Second backend hire for Kora’s payouts team', team: 'Payouts', location: 'Lagos', workMode: 'ONSITE', pay: { min: 2200000, max: 2800000, currency: 'NGN', period: 'month' }, status: 'SOURCING', confidential: true, createdBy: 'u_dele',
state/seed.ts:53:  { mandateId: 'm_kora_agency', personId: 'p_dayo', stage: 'SHORTLISTED', at: '2026-10-26', by: 'u_dele' },
state/seed.ts:54:  { mandateId: 'm_kora_agency', personId: 'p_zara', stage: 'SOURCED', at: '2026-10-26', by:
… [277 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rest of refs and css markers

  <details><summary>result</summary>

```
function DiffRef({ id }: { id: string }) {
  const [msgId, vs] = id.split('@');
  const w = useWorld((x) => x);
  const d = hc(w).drafts[msgId];
  const [removed, setRemoved] = useState(false);
  const [all, setAll] = useState(false);
  if (!d) return null;
  const cur = d.versions.find((x) => x.v === Number(vs)); const prev = d.versions.find((x) => x.v === Number(vs) - 1);
  if (!cur || !prev) return null;
  const rows = versionChanges(w, d, prev, cur);
  const parts = diffWords(prev.body, cur.body);
  const changed = parts.filter((p) => p.t !== 'same' && p.s.trim()).length;
  const shown = removed ? parts : parts.filter((p) => p.t !== 'del');
  // A tone change rewrites most sentences; highlighting everything says nothing, so say it once instead.
  const addLen = parts.filter((p) => p.t === 'add').reduce((n, p) => n + p.s.length, 0);
  const reworded = !removed && addLen > cur.body.length * 0.6;
  return (
    <div className="hc-card" role="group" aria-label={`Changes from version ${prev.v} to ${cur.v}`}>
      <div className="hc-card-head"><span className="lab">What changed · v{prev.v} → v{cur.v}</span><span className="hc-status" data-s="DRAFT">Draft</span></div>
      {rows.length > 0 && (
        <ul className="hc-changes">
          {rows.map((r) => (
            <li key={r.k}><span className="hc-k">{r.k}</span>
              <span className="hc-v">{r.from && <><del><span className="sr">was </span>{r.from}</del><span aria-hidden="true" className="hc-arrow">→</span></>}<
… [6552 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/state/areas/mail.ts

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/state/areas/mail.ts has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Extend hire-c area types

  <details><summary>result</summary>

```
9:export type DraftKind = 'INVITE' | 'RESCHEDULE' | 'FOLLOW_UP' | 'REJECTION' | 'REPLY' | 'AVAILABILITY' | 'CONFIRMATION';
23:  batchId?: string;
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/email.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/email.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Fix two expressions

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Patch lib.ts for email pipeline and typecheck

  <details><summary>result</summary>

```
File "<stdin>", line 75
    """  return { ok: true, text: `Simulated send: the ${KIND_LABEL[d.kind]} went to ${pFirst} ${ch}. Nothing really left Talent Q.${d.slot && d.kind !== 'REJECTION' && d.kind !== 'REPLY' && d.kind !== 'AVAILABILITY' && d.kind !== 'CONFIRMATION' ? ``)
                                                                                                                                                                                                                                                          ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
src/journeys/campaigns/model.ts(245,24): error TS6133: 'w' is declared but its value is never read.
src/journeys/hire-c/email.ts(9,14): error TS6133: 'hcw' is declared but its value is never read.
src/journeys/hire-c/lib.ts(238,14): error TS2739: Type '{ INVITE: string; RESCHEDULE: string; FOLLOW_UP: string; REJECTION: string; REPLY: string; }' is missing the following properties from type 'Record<DraftKind, string>': AVAILABILITY, CONFIRMATION
```
  </details>

- 🔧 `Bash`: Check whether lib.ts was modified

  <details><summary>result</summary>

```
0
```
  </details>

- 🔧 `Bash`: Apply lib.ts patch and typecheck

  <details><summary>result</summary>

```
src/journeys/campaigns/model.ts(245,24): error TS6133: 'w' is declared but its value is never read.
[This command modified 2 files you've previously read: journeys/hire-c/email.ts, journeys/hire-c/lib.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Assign default sender on check; seed sender

  <details><summary>result</summary>

```
9:      { id: 'hc_zara_inv', from: 'u_seyi', to: 'p_zara', subject: 'Interview: Senior Backend Engineer at Kora Pay', body: SEYI_ZARA_BODY, at: '2026-10-27T16:20:00+01:00', status: 'DRAFT', channel: 'EMAIL', senderId: 'mb_kora_careers' },
```
  </details>

- 🔧 `Bash`: Add seeds for read-denied and timeout states

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/contact/logic.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/contact/logic.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check seeded threads

  <details><summary>result</summary>

```
];

export const THREADS: Thread[] = [
  { id: 't_zara_kora', orgId: 'org_kora', personId: 'p_zara', mandateId: 'm_backend', messages: [
    { id: 'm1', from: 'p_zara', to: 'u_ngozi', subject: 'Application: Senior Backend Engineer', body: 'Hi, I applied on Monday. Happy to share more about the fleet API if useful.', at: '2026-10-27T10:12:00+01:00', status: 'RECEIVED', channel: 'IN_APP
  ] },
];

/** Busy calendars (simulated free/busy only). Monday 2 Nov 2026 onward. */
```
  </details>


**Claude** · 2026-10-29 16:24

Now the briefing data and components.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/contact/briefing.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/contact/briefing.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/contact/RoleBriefing.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/contact/RoleBriefing.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/contact/ContactRecruiter.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/contact/ContactRecruiter.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/contact/contact.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/contact/contact.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Insert JobContact into job detail

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Export helpers from hire-c skills; check nlu

  <details><summary>result</summary>

```
26:export function peopleIn(c: QCtx) {
42:export function contextPerson(c: QCtx): { id?: string; why?: string } {
69:export function postDraft(w: World, a: Actor, msgId: string, lead: string) {
77:export function describeSlot(w: World, d: { slot?: { start: string }; panel: string[]; personId: string }) {
85:export function checkAndPost(w: World, a: Actor, msgId: string, lead = '') {
258:export function kindFrom(norm: string, w: World, personId: string, orgId?: string): DraftKind {
265:export function draftFlow(c: QCtx, personId: string, kind: DraftKind, why?: string): QReply {
143:export function pushUndo(w: World, actorId: string, label: string, op: string, args: Record<string, unknown>) {
1:52:export function entities(norm: string, w: World): Entities {
2:53-  const ws = words(norm);
3:54-  const people = w.people.filter((p) => { const first = p.name.split(' ')[0].toLowerCase(); const last = p.name.split(' ')[1]?.toLowerCase() ?? ''; return ws.some((x) => x === first || x === last || (first.length > 4 && lev(x, first) <= 1)); }).map((p) => p.personId);
4:55-  const days = DAYS.filter((d) => d.includes(' ') ? norm.includes(d) : ws.some((x) => x === d || (d.length > 5 && lev(x, d) <= 1)));
5:56-  const time = norm.match(/\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b/)?.[0] ?? norm.match(/\b(\d{1,2}):(\d{2})\b/)?.[0];
8:59-  const mm = norm.match(/(?:₦|ngn|n)?\s?(\d+(?:[.,]\d+)?)\s?(k|m|thousand|million|naira)?\b/g)?.find((x) => /k|m|thousand|million|naira|₦|\d{4,}/.test(x));
14:65-  c
… [675 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/skills/email.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/skills/email.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Clean up ops registry in email skill and typecheck

  <details><summary>result</summary>

```
src/q/skills/email.ts(21,30): error TS6133: 'candidateStatus' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Move contact skill out of talent-b and typecheck

  <details><summary>result</summary>

```
[This command modified 2 files you've previously read: q/skills/talent-b.ts, q/skills/email.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Check existing CSS classes and useViewState

  <details><summary>result</summary>

```
36:.ds .hc-status { font-family: var(--data); font-size: 11px; letter-spacing: .06em; text-transform: uppercase; border: 1px solid var(--rule-2); border-radius: 4px; padding: 2px 7px; white-space: nowrap; color: var(--ink-2); }
37:.ds .hc-status[data-s='AWAITING_APPROVAL'], .ds .hc-status[data-s='HOLD'] { border-color: var(--gold); color: var(--gold-ink); }
38:.ds .hc-status[data-s='SENT_SIMULATED'], .ds .hc-status[data-s='CONFIRMED'], .ds .hc-status[data-s='PASS'] { border-color: var(--ok); color: var(--ok); }
39:.ds .hc-status[data-s='QUEUED_OFFLINE'], .ds .hc-status[data-s='RESCHEDULE_REQUESTED'] { border-color: var(--warn); color: var(--warn); border-style: dashed; }
40:.ds .hc-status[data-s='FIX'] { border-color: var(--risk); color: var(--risk); }
41:.ds .hc-status[data-s='DRAFT'] { border-style: dashed; }
107:.ds .hc-msg-head { display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: baseline; }
108:.ds .hc-msg-head .hc-status { margin-left: auto; align-self: center; }
109:.ds .hc-receiptline { margin: 4px 0 0; padding-top: 8px; border-top: 1px solid var(--rule); display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; font-size: 13px; color: var(--ink-2); }
110:.ds .hc-receiptline .ds-sim { margin-left: auto; }
112:.ds .hc-receiptline[data-q='1'] .hc-ok { background: transparent; color: var(--warn); border: 1.5px dashed var(--warn); }
113:.ds .hc-draft { display: grid; gap: 12px; min-width: 0; }
114:.ds .hc-versions { display: flex; flex-wrap: wrap; gap: 
… [318 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Add email.save op

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Composer.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Composer.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Fix Composer types

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 16:33

Now reply intelligence and refs.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/ReplyIntel.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/ReplyIntel.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Remove old DraftEditor from Messages

  <details><summary>result</summary>

```
146 Messages.tsx
```
  </details>


**Claude** · 2026-10-29 16:34

Now I'll rewrite the Messages hub in full.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Messages.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/Messages.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/email.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/email.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check CSS var definitions

  <details><summary>result</summary>

```
1 --data:
      1 --gold-ink:
      1 --gold:
      1 --ink-2:
      1 --ink:
      1 --ok:
      2 --paper:
      1 --risk:
      1 --rule-2:
      2 --rule:
      1 --warn:
```
  </details>

- 🔧 `Bash`: Read ConfirmButton and useViewState

  <details><summary>result</summary>

```
// A destructive action confirmed in place: the button turns into the question with "Yes" and "Keep it".
// Used instead of window.confirm(), which embedded viewers block (it returns false without asking).
import { useState } from 'react';

export function ConfirmButton({ label, question, yes, onConfirm, className = 'ds-btn quiet' }: { label: string; question: string; yes: string; onConfirm: () => void; className?: string }) {
  const [asking, setAsking] = useState(false);
  if (!asking) return <button type="button" className={className} onClick={() => setAsking(true)}>{label}</button>;
  return (
    <span role="group" aria-label={question} className="ds-confirm">
      <span className="t14">{question}</span>
      <button type="button" className="ds-btn" onClick={() => { setAsking(false); onConfirm(); }}>{yes}</button>
      <button type="button" className="ds-btn quiet" autoFocus onClick={() => setAsking(false)}>Keep it</button>
    </span>
  );
}
  return matchRoute(path)?.def.label ?? path;
}

/** Page view-state that survives navigation (e.g. the comparison's focus). Stored per person and route. */
export function useViewState<T>(key: string, initial: T): [T, (v: T) => void] {
  const k = `${useWorld((w) => w.session.actor)}|${route().split('/').slice(0, 3).join('/')}`;
  const v = useWorld((w) => (w.q.ui[k]?.[key] as T | undefined));
  const set = useCallback((nv: T) => update((w) => { (w.q.ui[k] ??= {})[key] = nv as unknown; }), [k, key]);
  return [v === undefined ? 
… [347 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/EmailSettings.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-c/EmailSettings.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Register settings route and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Extend candidate messages with statuses and email reply

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Extend proactive rules

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: First render of new screens

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Rerun capture to see output

  <details><summary>result</summary>

```
exit 0
```
  </details>

- 🔧 `Bash`: Check vite server state

  <details><summary>result</summary>

```
4:25:37 PM [vite] hmr update /src/styles/hire-b.css
4:25:53 PM [vite] hmr update /src/journeys/talent-b/Jobs.tsx
4:27:18 PM [vite] hmr update /src/app/App.tsx
4:28:04 PM [vite] hmr update /src/app/App.tsx
4:28:24 PM [vite] hmr update /src/app/App.tsx
4:28:37 PM [vite] hmr update /src/app/App.tsx
4:29:23 PM [vite] hmr update /src/journeys/hire-a/Roles.tsx
4:29:37 PM [vite] hmr update /src/app/App.tsx
4:30:07 PM [vite] hmr update /src/journeys/agency/pages.tsx
4:30:16 PM [vite] hmr update /src/app/App.tsx
4:30:49 PM [vite] hmr update /src/app/App.tsx
4:30:54 PM [vite] hmr update /src/app/App.tsx
4:31:43 PM [vite] hmr update /src/app/App.tsx
4:34:12 PM [vite] hmr update /src/journeys/hire-b/Profile.tsx
4:34:31 PM [vite] hmr update /src/journeys/hire-c/Messages.tsx
4:35:36 PM [vite] hmr update /src/journeys/hire-c/Messages.tsx
4:37:24 PM [vite] hmr update /src/app/App.tsx
4:38:28 PM [vite] hmr update /src/journeys/hire-c/CandidateMessages.tsx
4:39:15 PM [vite] hmr update /src/journeys/hire-b/Ledger.tsx
4:39:33 PM [vite] hmr update /src/app/App.tsx
200
1
```
  </details>

- 🔧 `Bash`: Inspect capture script

  <details><summary>result</summary>

```
5722 cap.mjs
total 22704
drwx------ 98 root root   12288 Oct 29 16:40 .
drwx------  4 root root    4096 Oct 26 10:39 ..
-rw-r--r--  1 root root    2938 Oct 29 09:36 R1.log
-rw-r--r--  1 root root    7308 Oct 29 14:47 R3.log
-rw-r--r--  1 root root    3294 Oct 29 09:38 R5.log
-rw-r--r--  1 root root    4208 Oct 29 14:43 T1.log
-rw-r--r--  1 root root    3652 Oct 29 14:44 T2.log
-rw-r--r--  1 root root    3852 Oct 29 14:46 T3.log
-rw-r--r--  1 root root    5071 Oct 29 14:40 T4.log
-rw-r--r--  1 root root    2920 Oct 29 14:42 T5.log
drwxr-xr-x  4 root root    4096 Oct 29 13:54 a1
drwxr-xr-x  4 root root    4096 Oct 29 13:54 a2
drwxr-xr-x  4 root root    4096 Oct 29 14:12 a3
drwxr-xr-x  4 root root    4096 Oct 29 14:14 a4
-rw-r--r--  1 root root  597262 Oct 27 12:13 afr.png
drwxr-xr-x  4 root root    4096 Oct 29 14:28 after-states
drwxr-xr-x  3 root root    4096 Oct 29 15:12 appdist
-rw-r--r--  1 root root    1158 Oct 29 09:08 ask.mjs
-rw-r--r--  1 root root  303333 Oct 29 09:09 ask.png
-rw-r--r--  1 root root   13172 Oct 29 07:07 atlas.txt
drwxr-xr-x  3 root root    4096 Oct 26 20:36 axe
-rw-r--r--  1 root root   27226 Oct 29 11:23 axe-all.json
-rw-r--r--  1 root root      22 Oct 29 07:28 axe-b1.txt
-rw-r--r--  1 root root      22 Oct 27 15:34 axe-d.txt
-rw-r--r--  1 root root     974 Oct 26 21:23 axe.mjs
drwxr-xr-x  2 root root    4096 Oct 29 07:12 b1
drwxr-xr-x  2 root root    4096 Oct 29 07:43 b1f
drwxr-xr-x  2 root root    4096 Oct 29 07:22 b1s
drwxr-xr-x  2 root root    409
… [11762 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Set up private scratch dir and capture

  <details><summary>result</summary>

```
1913
1926
1927
desktop settings overflow 0 
phone settings overflow 0 
desktop job overflow 0 
phone job overflow 0 
desktop msgs overflow 0 
phone msgs overflow 0
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/r1/settings-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:41

[Image: original 1440x2068, displayed at 1393x2000. Multiply coordinates by 1.03 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/r1/job-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:41

[Image: original 1440x3085, displayed at 934x2000. Multiply coordinates by 1.54 to map to original image.]

- 🔧 `Bash`: Make video screen dark

  <details><summary>result</summary>

```
1
[This command modified 1 file you've previously read: journeys/contact/contact.css. Call Read before editing.]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/r1/msgs-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 16:41

[Image: original 1440x2029, displayed at 1419x2000. Multiply coordinates by 1.01 to map to original image.]

- 🔧 `Bash`: Find inbox grid rule

  <details><summary>result</summary>

```
82:.ds .hc-inbox { display: grid; grid-template-columns: minmax(250px, 310px) minmax(0, 1fr); gap: 16px; align-items: start; }
204:  .ds .hc-inbox { grid-template-columns: 1fr; }
```
  </details>

- 🔧 `Bash`: Collapse facets and attachments

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Add evidence request kind and skill

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: List job ids

  <details><summary>result</summary>

```
id: 'j_kora_backend', orgId: 'org_kora'
id: 'j_rivers_backend', orgId: 'org_rivers'
id: 'j_tinda_pa', orgId: 'org_tinda'
id: 'j_kora_data', orgId: 'org_kora'
id: 'j_medlink_ba', orgId: 'org_medlink'
id: 'j_tinda_apm', orgId: 'org_tinda'
id: 'j_care_coord', orgId: 'org_carehome'
id: 'j_kora_support', orgId: 'org_kora'
id: 'j_ta_grad_data', orgId: 'org_tinda'
id: 'j_ta_grad_ops', orgId: 'org_medlink'
id: 'j_harbour_backend', orgId: 'org_harbour'
id: 'j_medlink_platform', orgId: 'org_medlink'
```
  </details>

- 🔧 `Bash`: Write and run contact feature test

  <details><summary>result</summary>

```
Exit code 1
FAIL Script crashed — TimeoutError: page.waitForSelector: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-app') to be visible[22m

PASS No page errors

1 of 2 passed
```
  </details>

- 🔧 `Bash`: Probe app load

  <details><summary>result</summary>

```
<!DOCTYPE html><html lang="en" data-theme="light"><head>
    <script type="module">import { injectIntoGlobalHook } from "/@react-refresh";
injectIntoGlobalHook(window);
window.$RefreshReg$ = () => {};
window.$RefreshSig$ = () => (type) => type;</script>

    <script type="module" src="/@vite/client"
```
  </details>

- 🔧 `Bash`: Probe body and console

  <details><summary>result</summary>

```
C debug [vite] connecting...
C debug [vite] connected.
C info %cDownload the React DevTools for a better development experience: https://reactjs.org/link/react-devtools font-weight:bold
This page is for candidates.

You’re signed in as someone on the other side. Switch person from the menu, or go to the start.
4:43:07 PM [vite] hmr update /src/app/App.tsx
4:44:38 PM [vite] hmr update /src/journeys/campaigns/pages.tsx
4:45:39 PM [vite] hmr update /src/app/App.tsx, /src/journeys/media/Report.tsx, /src/journeys/media/Candidate.tsx, /src/journeys/media/Player.tsx
4:45:39 PM [vite] hmr update /src/journeys/media/Candidate.tsx
4:45:39 PM [vite] hmr update /src/journeys/media/media.css
```
  </details>

- 🔧 `Bash`: Rerun contact test

  <details><summary>result</summary>

```
Exit code 1
PASS Briefing: player, 5 chapters and a transcript on the job page
PASS Briefing is labelled as a simulated video
PASS Play advances the time — 0:02 / 2:00
PASS Chapter jump marks the chapter current
FAIL Q answers from the transcript and quotes the time (1:12) — Role briefing transcript (transcript written by kora pay and published with the listing)

From the role briefing at 0:58, Seyi says: “Let’s be straight about incidents. When a settlement file is late,
FAIL Script crashed — TimeoutError: locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-thread .ds-chip').filter({ hasText: 'Play from 1:12' }).last()[22m

PASS No page errors

5 of 7 passed
```
  </details>

- 🔧 `Bash`: Fix on-call line match and rerun

  <details><summary>result</summary>

```
PASS Briefing: player, 5 chapters and a transcript on the job page
PASS Briefing is labelled as a simulated video
PASS Play advances the time — 0:02 / 2:00
PASS Chapter jump marks the chapter current
PASS Q answers from the transcript and quotes the time (1:12) — Role briefing transcript (transcript written by kora pay and published with the listing)

From the role briefing at 1:12, Seyi says: “So yes, the on-call is real: one week in six, with a secondary on 
PASS "Play from 1:12" seeks the player to that line
PASS Contact card shows Kora’s policy before any draft — Ask Kora Pay about this role
DIRECT QUESTIONS
Before or after you apply
HOW
in Talent Q or by email to careers@kora.example
LIMIT
2 new conversations a week · 2 left
PRIVACY
Recruiters’ personal addre
PASS No personal recruiter address is shown
PASS Q states the policy first, then a short question to edit — Kora Pay’s contact policy
Role briefing at 1:12

Yes. Kora Pay welcomes questions before you apply, in Talent Q or by email to careers@kora.example, up to 2 new conversations a week (2 left for you). 
PASS The draft is on the page, editable, 3 lines — Hello Kora Pay team,
I’m interested in the Senior Backend Engineer role. this role?
Thank you, Tobi
PASS Sent in-app: thread initiatedBy CANDIDATE, state OPEN, role m_backend — UPDATE

Sent to Kora Pay in Talent Q (simulated). It’s in Messages with its status. Kora Pay usually replies within 5 days, but I can’t promise when.

Open messages
PASS Rate limit recorde
… [2956 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Fix draft question extraction

  <details><summary>result</summary>

```
59:  const useful = about && about.length > 12 && !/^(this|the|that|your) (role|job|position|vacancy)\b/i.test(about.trim());
60:  const q = useful ? about!.replace(/[?.!\s]*$/, '?') : b ? 'The briefing mentions a one-in-six on-call week. Is the secondary on-call also on the payments team, and how often are you paged out of hours?' : `Could you tell me more about what the first three months in this role look like?`;
```
  </details>

- 🔧 `Bash`: Capitalize custom question

  <details><summary>result</summary>

```
const q = useful ? about!.trim().replace(/^\w/, (x) => x.toUpperCase()).replace(/[?.!\s]*$/, '?') : b ? 'The briefing mentions a one-in-si
[This command modified 1 file you've previously read: journeys/contact/logic.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Write and run email feature test

  <details><summary>result</summary>

```
PASS Setup: Tobi’s candidate-initiated thread exists
PASS Hub: unfiled conversation, started by the candidate
PASS Step 3: thread routed to c_q4_eng / m_backend, with an audit event — Filed Tobi’s question under Q4 Engineering Expansion → Senior Backend Engineer. It shows in the campaign and in Messages under that filter. Recorded in the audit log. Undo Open the campaign
PASS Hub filters by campaign (Tobi listed under Q4 Engineering)
PASS Hub filters by channel (text: Grace only)
PASS Step 6: request drafted in the same thread, in Talent Q — Kora guideline v1: Panel of two for engineering interviews Tobi: Lagos time Here’s the request to Tobi, in Talent Q, in the conversation they started. It says Tobi chooses exactly what you see and can send a written walk
FAIL Script crashed — TimeoutError: locator.click: Timeout 30000ms exceeded. Call log: [2m - waiting for locator('.ds-thread .ds-chip').filter({ hasText: 'Approve and send' }).last()[22m 
PASS No page errors

7 of 8 passed
```
  </details>

- 🔧 `Bash`: Add pay band to request; rerun

  <details><summary>result</summary>

```
PASS Setup: Tobi’s candidate-initiated thread exists
PASS Hub: unfiled conversation, started by the candidate
PASS Step 3: thread routed to c_q4_eng / m_backend, with an audit event — Filed Tobi’s question under Q4 Engineering Expansion → Senior Backend Engineer. It shows in the campaign and in Messages under that filter. Recorded in the audit log. Undo Open the campaign
PASS Hub filters by campaign (Tobi listed under Q4 Engineering)
PASS Hub filters by channel (text: Grace only)
PASS Step 6: request drafted in the same thread, in Talent Q — Kora guideline v1: Name the pay band in the first message to a … Tobi: Lagos time Here’s the request to Tobi, in Talent Q, in the conversation they started. It says Tobi chooses exactly what you see and can send a writte
PASS Step 6: approved and sent (simulated) — UPDATE Simulated send: the request for a work sample went to Tobi in Talent Q. Nothing really left Talent Q. ✓ Sent to Tobi SIMULATED SEND What A request: a walkthrough of your reconciliation work (v1) How Talent Q Appro
PASS Step 10: draft resolves sender (Ada, Google Workspace), recipient and campaign — Kora guideline v1: Panel of two for engineering interviews Kora guideline v1: Interviews 10:00–16:00 Lagos time unless the… Calendars: Ada and Musa (busy times only) Tobi: Lagos time Here’s the email to Tob
FAIL Step 10: offers Thursday 14:00 or a Friday time — Dear Tobi, Thank you for your interest in the Senior Backend Engineer role at Kora Pay. We would like to invite you t
… [3672 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Fix day resolution and test selectors; rerun

  <details><summary>result</summary>

```
Command did not complete within its 120s timeout and was moved to the background (ID: bkviy8hpi). Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bkviy8hpi.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. No output had been read from it when it was moved. A program that buffers its output, or a pipe into one such as tail, can keep the output file empty until the command finishes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Look at an existing handoff style

  <details><summary>result</summary>

```
# Engineering handoff: R3, the busy HR team (area `hire-c`)

Specification only. The prototype (`prototype/`) is the behavioural reference; file paths below are relative
to `prototype/src`. **SIM** marks where production must differ from the simulation.

## 0. Shared rules (apply to every feature)

- **Tenant boundary.** Every record is scoped to one organisation (`orgId`). Recruiter reads and writes are
  filtered by the actor's `orgId`; candidate reads by `personId`. Candidate visibility goes through
  `canSeeCandidate` / `visibleEvidence` (`mock/world.ts`); never bypass them. Agencies never see an
  employer's own threads or pipeline.
- **Roles** (`journeys/hire-c/lib.ts` `CAN_SEND`, `CAN_MOVE`, `IS_ADMIN`): Admin/Owner approve, send, change
  roles and guidelines; Recruiter approves and sends; Hiring manager drafts, moves stages, changes panels;
  Interviewer gives feedback; Viewer reads. Enforce on the server, not only in the UI.
- **Approval binds to a version.** A send is valid only for the exact version that was checked and approved
  (`approveAndSend` compares `v` and `checkedV`). Any edit creates a new version and voids the approval.
- **Unverified organisations (decision D1).** `orgLimits(w, orgId)` / `outreachThisWeek` (`mock/world.ts`):
  unverified orgs may send 3 messages per rolling 7 days. Enforced in `approveAndSend` and `flushQueued`
  (`allowanceRefusal`), shown as a pre-send check, and every message they send carries
  "This employer isn't verified yet" (
… [1840 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read test output

  <details><summary>result</summary>

```
FAIL Script crashed — TimeoutError: locator.click: Timeout 30000ms exceeded. Call log: [2m - waiting for locator('.ds-thread .ds-chip').filter({ hasText: 'Approve and send' }).last()[22m 

41 of 42 passed

[exited with code 0]
```
  </details>

- 🔧 `Bash`: Rerun email test, show tail

  <details><summary>result</summary>

```
PASS Untrusted email: instructions shown as text, never acted on
PASS Audit: what was sent, with truthful provider status — Sent to Tobi: “A request: a walkthrough of your reconciliation work” on Thu 29 Oct by Talent Q; “Interview: Senior Backend Engineer at Kora Pay” on Thu 29 Oct by email, accepted by Google (si
PASS Audit: why contacted (he started the conversation; approvals) — Why Tobi was contacted: Tobi started the conversation (asked about Senior Backend Engineer on Thu 29 Oct); Tobi is interview on Senior Backend Engineer (moved by Ada on 2026-10-29); A reque
PASS Forget an extracted preference; the email stays — Forgotten: “Thursday 14:00”. The original email stays in the record; I just won’t use what I extracted from it.
PASS Multi-recipient: three individual drafts, one recipient each — Kora Pay template: Next step and availability Contact choices and suppressions Sender: ada@kora.example I drafted 3 separate emails, one per person, so nobody sees anyone else’s address: T
PASS Per-recipient status with a suppression mark — 3 INDIVIDUAL EMAILS · ONE RECIPIENT EACH SIMULATED SEND Tobi Adeyemi Next step: Senior Backend Engineer at Kora Pay Ready to approve Ifeoma Obi Next step: Senior Backend Engineer at Kora Pay Ready to appro
PASS Two sent individually (accepted), suppressed one not sent — UPDATE Each person got their own email; nobody saw anyone else’s address. Tobi: accepted by Google (simulated) at 17:54; Ifeoma: accepted by Google (simulated) at 17:54; Kunle: n
… [1007 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 16:55

You've hit your 5-hour limit · resets 6:50pm (UTC)


**User** · 2026-10-29 19:22

The coordinator sent a message while you were working:
Lead here. The usage limit has reset, so please continue from where you stopped ("Now I'll rewrite the Messages hub in full").

Since you stopped:
- The RUBRIC and MEDIA builders have finished and their work is committed.
- `npx tsc --noEmit -p .` was clean across the whole tree at the last check; keep it that way.

Then finish the rest of your brief:
- the remaining screens and states;
- `qa/scripts/features/email.mjs` and `qa/scripts/features/contact.mjs`;
- runs of R3, R4, R5, T3 and T5;
- `journeys/design/email.md` and `journeys/handoff/email.md`.

Send your final report when done.

Address this before completing your current task.

- 🔧 `Bash`: Adjust test step and rerun

  <details><summary>result</summary>

```
FAIL Script crashed — Error: page.goto: net::ERR_CONNECTION_REFUSED at http://localhost:5191/#/r/home Call log: [2m - navigating to "http://localhost:5191/#/r/home", waiting until "load"[22m 
PASS No page errors

1 of 2 passed
```
  </details>

- 🔧 `Bash`: Restart dev server and typecheck

  <details><summary>result</summary>

```
000
```
  </details>

- 🔧 `Bash`: Check server

  <details><summary>result</summary>

```
200

Are they installed?
    at file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50669:15
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50174:26
```
  </details>

- 🔧 `Bash`: Inspect vite error and git status

  <details><summary>result</summary>

```
➜  Network: use --host to expose
Error: The following dependencies are imported but could not be resolved:

  @emotion/is-prop-valid (imported by /home/user/neo/talent-q-design/prototype/dist-review/assets/index-7nVgRM4N.js)

Are they installed?
d1bc4be WIP snapshot: email and campaigns builders in progress
852063a WIP snapshot: email and campaigns builders resuming after the usage limit
b411f2c Video and voice evidence (media.mjs 114/114); profile link; segment check in the QA hook
2a9dea3 WIP snapshot: rubric studio finished; email, campaigns, media builders in progress
4456e74 WIP snapshot: addendum builders in progress (email, campaigns, rubric, media)
```
  </details>

- 🔧 `Bash`: Verify files, tsc, rerun email test

  <details><summary>result</summary>

```
prototype/src/q/skills/email.ts

prototype/src/journeys/contact/:
ContactRecruiter.tsx
JobContact.tsx
RoleBriefing.tsx
briefing.ts
contact.css
logic.ts

prototype/src/journeys/hire-c/:
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
FAIL Script crashed — TimeoutError: locator.click: Timeout 30000ms exceeded. Call log: [2m - waiting for locator('.em-compose .ds-btn').filter({ hasText: /Save as v/ })[22m 

41 of 42 passed
```
  </details>

- 🔧 `Bash`: Allow editing a failed draft; rerun

  <details><summary>result</summary>

```
1
FAIL Read denied: Q says it can’t see replies to a send-only mailbox
FAIL Q answers “did she reply” honestly with the scope limit — No reply from Grace that I can see.
FAIL Proactive follow-up: reason, cap and scope honesty — Q NOTICED Grace hasn’t replied to the message sent Tue 27 Oct (yesterday). The interview on Fri 30 Oct at 11:00 is still unconfirmed. Shall I draft a polite reminder? Draft a follow-up Snooze 2 days Don’t suggest again W
FAIL R4: client’s reminder automation paused at once — UPDATE JobBoard NG stopped responding during the Medlink operations analyst search (a simulated outage). I’ve kept the 5 profiles already read and will retry once automatically. The other agents are unaffected. Show agen

58 of 62 passed
```
  </details>

- 🔧 `Bash`: Check Grace seed

  <details><summary>result</summary>

```
12:      { id: 'hc_grace_mail', from: 'u_ngozi', to: 'p_grace', subject: 'Customer Support Lead: your application', body
state/seeds/hire-c.ts:11:    { id: 't_hc_grace', orgId: 'org_kora', personId: 'p_grace', mandateId: 'm_support', message
```
  </details>

- 🔧 `Bash`: Debug Grace read scope

  <details><summary>result</summary>

```
[
  [ 'hc_grace_mail', 'EMAIL', 'mb_ngozi', 'SENT_SIMULATED' ],
  [ 'hc_grace_inv', 'SMS', undefined, 'SENT_SIMULATED' ]
]
{
  id: 'mb_ngozi',
  owner: 'u_ngozi',
  orgId: 'org_kora',
  provider: 'MICROSOFT',
  address: 'ngozi.eze@kora.example',
  label: 'Ngozi Eze (Microsoft 365)',
  kind: 'PERSONAL',
  sendAs: [ 'u_ngozi' ],
  scopes: [ 'SEND' ],
  state: 'CONNECTED',
  connectedAt: '2026-09-20',
  simulated: true
}
KORA PAY
Messages
Email settings
Outbox and receipts
Find a person
Campaign, role, channel
All
Drafts1
Need a reply1
Awaiting their reply1
Sent
ZM
Zara Mensah
Tue 27 Oct
Senior Backend Engineer
Draft: Thanks for applying for the Senior Backend Engineer role. We’d like to invite you to a 45-
Draft
Needs a reply
GO
Grace Okon
Tue 27 Oct
Customer Support Lead
You: thank you for your interest. Your interview is on Friday 30 October at 11:00. You can answ
Awaiting their reply
Grace Okon
Customer Support Lead · Lagos, 09:00 now
Email ok
Text ok
Talent Q ok
Draft a reply with Q
Campaign
Not filed yet
Q4 Engineering Expansion
Merchant Success 2026
Ngozi Eze
Sat 24 Oct, 15:10 · email
Accepted by Microsoft (simulated)

From ngozi.eze@kora.example to grace@mail.example

Customer Support Lead: your application

Hello Grace,

Thank you for applying for the Customer Support Lead role at Kora Pay. I’ll
```
  </details>

- 🔧 `Bash`: Check ReadScope wiring

  <details><summary>result</summary>

```
20:import { Attempts, BatchReview, ReadScope, ReplyCard } from './ReplyIntel';
212:      <ReadScope t={g.thread} />
213:      {lastInbound && <ReplyCard t={lastInbound.t} m={lastInbound.m} />}
64:export function ReadScope({ t }: { t: Thread }) {
65-  const w = useWorld((x) => x);
66-  const mb = replyMailbox(w, t);
67-  if (!mb || canRead(mb)) return null;
68-  return (
69-    <p className="em-scope" role="note"><b>Q can’t see email replies to {mb.address}.</b> {mb.state === 'EXPIRED' ? `The ${PROVIDER_NAME[mb.provider]} sign-in expired.` : 'It’s connected send-only.'} {firstOf(w, t.personId)} may have replied there; check that inbox. Replies in Talent Q still show here. <a href="#/settings/email">Email settings</a></p>
70-  );
71-}
72-
173:export function replyMailbox(w: World, t: Thread) { const out = [...t.messages].reverse().find((m) => m.from !== t.personId && m.channel === 'EMAIL' && m.senderId); return mailboxOf(w, out?.senderId); }
```
  </details>

- 🔧 `Bash`: Evaluate replyMailbox in browser

  <details><summary>result</summary>

```
{"mb":"mb_ngozi","can":false}
0
```
  </details>

- 🔧 `Bash`: Count elements in DOM

  <details><summary>result</summary>

```
}
[ 0, 1, 1 ]
```
  </details>

- 🔧 `Bash`: Fix read-scope across threads; rerun

  <details><summary>result</summary>

```
62 of 62 passed
```
  </details>

- 🔧 `Bash`: Run contact test and R3

  <details><summary>result</summary>

```
From the role briefing at 1:12, Seyi says: “So yes, the on-call is real: one week in six, with a secondary on 
DIRECT QUESTIONS
Before or after you apply
HOW
in Talent Q or by email to careers@kora.example
LIMIT
2 new conversations a week · 2 left
PRIVACY
Recruiters’ personal addre
Role briefing at 1:12

Yes. Kora Pay welcomes questions before you apply, in Talent Q or by email to careers@kora.example, up to 2 new conversations a week (2 left for you). 
I’m interested in the Senior Backend Engineer role. The briefing mentions a one-in-six on-call week. Is the secondary on-call also on the payments team, and how often are you page

Sent to Kora Pay in Talent Q (simulated). It’s in Messages with its status. Kora Pay usually replies within 5 days, but I can’t promise when.

Open messages
Messages
KP
Kora Pay
Thu 29 Oct
You: Question: Senior Backend Engineer
Waiting for Kora Pay
MH
Medlink Health
Tue 20 Oct
You: Question: Senior Platform Engineer
Waiting 
Messages
KP
Kora Pay
Thu 29 Oct
You: Question: Senior Backend Engineer
Waiting for Kora Pay
MH
Medlink Health
Tue 20 Oct
You: Question: Senior Platform Engineer
Waiting 
DECLINED

You’ve started 2 conversations with Kora Pay this week, which is their limit. You can start another next week, or reply in an existing one.

Apply for this role
DIRECT QUESTIONS
Not taken
PRIVACY
Recruiters’ personal addresses aren’t shown. Rivers Logistics sees your name and message, not your Passport.
PUBLISHED ROUTE
Rivers Lo
DECLINED

Rivers Logist
… [693 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check R3 results

  <details><summary>result</summary>

```
48
Kora guideline v1: Panel of two for engineering interviews
Kora guideline v
Kora guideline v1: Panel of two for engineering interviews
Kora guideline v1: Interviews 10:00–
Tobi’s contact choices
Calendars: Ada and Musa

v2 of the interview invitation to Tobi passed ev

Simulated send: accepted by Google (simulated) at 20:33 from ada@kora.example. That means Google took it; it isn

Seyi’s interview invitation to Zara has been a draft since Tue 27 Oct. It hasn’t been approved, so it hasn’t been sent.

Check it and send
Open it
Why am I seeing this?
Later
Dismiss | Q NO

Seyi’s interview invitation to Zara has been a draft since Tue 27 Oct. It hasn’t been approved, so it hasn’t been sent.
12:const step = (name, ok, info = '') => { results.push({ name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${info ? ` — ${String(info).replace(/\s+/g, ' ').slice(0, 200)}` : ''}`); };
```
  </details>

- 🔧 `Bash`: Show R3 failures

  <details><summary>result</summary>

```
PASS No page errors

48/48 passed
```
  </details>

- 🔧 `Bash`: Run R4 and R5

  <details><summary>result</summary>

```
Exit code 1
R4 pass=72 fail=0
R5 pass=67 fail=0
tail: option used in invalid context -- 2
```
  </details>

- 🔧 `Bash`: Run T3 and T5

  <details><summary>result</summary>

```
No page errors.
R4: PASS
ERRORS []
PASS R5: 66/66 steps passed
T3 pass=54 fail=4
T5 pass=52 fail=0
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T3.log:PASS [d] Curveball [recover]: upload drops at 60% · FAILED 60%
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T3.log:PASS [d] Second check: issuer cannot confirm → FAILED
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T3.log:PASS [m] Curveball [recover]: upload drops at 60% · FAILED 60%
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T3.log:PASS [m] Second check: issuer cannot confirm → FAILED
==> /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T3.log <==

54/54 steps passed

==> /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T5.log <==

52/52 steps passed
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/email/02-auth-expired-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 19:42

[Image: original 1440x3888, displayed at 741x2000. Multiply coordinates by 1.94 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/email/05-reply-intel-desktop.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 19:42

[Image: original 1440x3448, displayed at 835x2000. Multiply coordinates by 1.72 to map to original image.]

- 🔧 `Bash`: Apply critique fixes

  <details><summary>result</summary>

```
6
```
  </details>

- 🔧 `Bash`: Improve problem phrases; list captures

  <details><summary>result</summary>

```
/home/user/neo/talent-q-design/captures/cx/contact/:
01-briefing-desktop.png
02-timeout-desktop.png
03-consent-desktop.png
04-job-phone.png

/home/user/neo/talent-q-design/captures/cx/email/:
01-approval-desktop.png
02-auth-expired-desktop.png
03-consent-desktop.png
04-candidate-email-reply-desktop.png
05-reply-intel-desktop.png
06-batch-desktop.png
07-settings-desktop.png
08-hub-phone.png
09-settings-tobi-phone.png
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/email/08-hub-phone.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 19:44

[Image: original 780x4046, displayed at 386x2000. Multiply coordinates by 2.02 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/contact/04-job-phone.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 19:44

[Image: original 780x8552, displayed at 182x2000. Multiply coordinates by 4.29 to map to original image.]

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/contact/JobContact.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/contact/JobContact.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Add in-thread page index

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Save before shots and capture after

  <details><summary>result</summary>

```
desktop settings overflow 0 
phone settings overflow 0 
desktop job overflow 0 
phone job overflow 0 
desktop msgs overflow 0 
phone msgs overflow 0
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/after/job-phone.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 19:46

[Image: original 780x8718, displayed at 179x2000. Multiply coordinates by 4.36 to map to original image.]

- 🔧 `Bash`: Save pairs and after captures

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
```
  </details>

- 🔧 `Bash`: Rerun features and save remaining pairs

  <details><summary>result</summary>

```
62 of 62 passed

32 of 32 passed
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/email/05-after.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 19:49

[Image: original 1440x3619, displayed at 796x2000. Multiply coordinates by 1.81 to map to original image.]

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/email.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/email.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Correct pair caption

  <details><summary>result</summary>

```
41:- 01 Settings desktop: first render → final (readable dates; the Talent Q service row no longer claims to send for you).
[This command modified 1 file you've previously read: talent-q-design/journeys/design/email.md. Call Read before editing.]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/email.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/email.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Final tsc and journey reruns

  <details><summary>result</summary>

```
48/48 passed
0
PASS R5: 66/66 steps passed
0
73
```
  </details>

- 🔧 `Bash`: Rerun T3 and T5

  <details><summary>result</summary>

```
==> /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T3b.log <==
54/54 steps passed

==> /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/email/T5b.log <==
52/52 steps passed
```
  </details>

- 🔧 `Bash`: Stop own dev server; list changes

  <details><summary>result</summary>

```
M captures/cx/R3/02-ada-approval-desktop.png
 M captures/cx/R3/03-ngozi-messages-desktop.png
 M captures/cx/R3/04-ngozi-offline-queued-desktop.png
 M captures/cx/R3/05-ngozi-overlap-desktop.png
 M captures/cx/R3/06-ngozi-calendar-desktop.png
 M captures/cx/R3/07-ngozi-pipeline-desktop.png
 M captures/cx/R3/08-ngozi-panel-notice-desktop.png
 M captures/cx/R3/11-ngozi-team-desktop.png
 M captures/cx/R3/12-ngozi-setup-desktop.png
 M captures/cx/R3/14-phone-approval.png
 M captures/cx/R4/d-01-home.png
 M captures/cx/R4/d-02-agents-failed.png
 M captures/cx/R4/d-03-q-explains-outage.png
 M captures/cx/R4/d-04-agents-interrupted.png
 M captures/cx/R4/d-05-agents-recovered.png
 M captures/cx/R4/d-06-search-diff.png
 M captures/cx/R4/d-07-isolation-refusal.png
 M captures/cx/R4/d-08-submittal-draft.png
 M captures/cx/R4/d-09-submittal-withdrawn.png
 M captures/cx/R4/d-10-pool-removed.png
 M captures/cx/R4/d-10b-pool-hidden-medlink.png
 M captures/cx/R4/d-11-submittal-sent.png
 M captures/cx/R4/d-12-campaign.png
 M captures/cx/R4/d-12b-docs-uploaded.png
 M captures/cx/R4/d-13-agents-resumed.png
 M captures/cx/R4/d-14-conflict.png
 M captures/cx/R4/d-15-notes.png
 M captures/cx/R4/d-16-report-flagged.png
 M captures/cx/R4/d-17-report-shared.png
 M captures/cx/R4/d-18-tunde-denied.png
```
  </details>

- 🔧 `SubagentHandback`: {"message": "## EMAIL builder: final report (nothing committed)\n\nConnected email (E-01) and candidate-initiated contact (audit \u00a7C) are built on the existing messaging. Messages stay in `w.threa

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
