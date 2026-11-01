# Helper agent agent-a1d7cd4ecd32487bf: Evidence-first candidate side

Source: `agent-a1d7cd4ecd32487bf.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-30 10:37

You are the CANDIDATE builder for Talent Q's evidence-first consolidation. Talent Q is a React + TypeScript + Vite design prototype at /home/user/neo/talent-q-design/prototype.

**The goal** (founder's words): "Show what you can do, even if your CV doesn't." Candidates own their evidence and consent, see the same truthful status the employer sees, and are never punished for a weak CV or for not having proof yet. Make it beautiful, understandable, responsive (phone 390 first, and desktop 1440) and fully connected.

**Read first:**
1. The controlling pack, all six files: `/home/user/neo/docs/sources/batch-6/` (especially 00, 02 "Concrete UI improvements" D, E, F and H, and 05 P1, P2 and P6).
2. The journey: `/home/user/neo/talent-q-design/journeys/J12-EVIDENCE-FIRST.md`. You own steps 6, 7, 10, 12, the candidate half of 13, and the candidate side of interest.
3. The shared model, already built; use it and don't redefine it:
   - `prototype/src/journeys/evidence/model.ts`: `proofClass`, `PROOF_WORD`, `PROOF_MEANS`, `BOUNDED_SAMPLE`.
   - `prototype/src/journeys/evidence/ops.ts` and the ops in `q/skills/evidence-ops.ts`: `ev.sample.start`, `ev.sample.submit`, `ev.sample.decline`, `ev.interest.answer`.
   - `state/areas/proof.ts`: CVs, reuse decisions with state SENT…REVIEWED, interest, intents (`HiringIntentConfirmation`), commitments (`ProcessCommitment`), preferences.
   - `state/seeds/proof.ts`: the new candidate actor Seyi Okoro, `p_seyio`, journey J12, with his CV claims, a pending 2019 certificate, a described project and an application to Kora.
4. The design rules: `design-system/DIRECTION-D-SYSTEM.md` and `handoff/DESIGN-QUALITY-GATE.md`. For the expected standard, see one design note such as `journeys/design/media.md`.

**Rules:**
- **Skills before code, through the Skill tool:** `design-skills:design-critique`, `design-skills:design-elevation`, `design-skills:interaction-design`, `design-skills:ux-writing`, `design-superpowers:creative` (inside Direction D; the candidate warmth variant already exists), and `dataviz` if you show progress or coverage. Record skill → screen → change in `journeys/design/evidence-candidate.md`.
- **Critique rendered screens:**
  1. Render phone and desktop with Playwright (`/opt/node-tools/node_modules/playwright/index.js`).
  2. Critique the screenshots with `design-critique`, fix, and re-render.
  3. Keep pairs in `captures/review/pairs/evidence-candidate/`.
- **Extend, never duplicate.**
  - The Evidence Passport stays `/c/passport` (`journeys/talent-b/Passport.tsx`).
  - Jobs stay `/c/jobs`; applications stay `/c/applications` (`journeys/talent-b/*`).
  - Candidate home is `CandidateHome` in `routes/entry.tsx`: edit only that component, and keep its structure.
  - J7 is `journeys/career/*`: reuse it, and don't rebuild it.
  - Q stays the one global Q: add skills in a new `q/skills/evidence-candidate.ts` and rules in `q/proactive/evidence-candidate.ts`.
- **Hard constraints from the pack:**
  - Q never calls a CV untrue.
  - Declining a sample is recorded as declined, not failed.
  - Private practice never becomes employer-visible proof without the candidate's approval, after a valid review.
  - No automatic cross-employer sharing.
  - The candidate controls preferences; unknown stays unknown.
  - CV help never invents jobs, qualifications or skills.
  - The same proof-class words as the recruiter side: Claim, Self-reported, Assessed, Issuer-verified, Disputed.
- **Seyi Okoro is not Seyi Balogun.** Seyi Okoro (`p_seyio`, candidate) is a different person from Seyi Balogun (Kora's engineering manager, who appears in candidates' interview details). Show surnames where both could appear.

**What to build:**
- **Passport (pack item D):**
  - each item labelled with its proof class (`proofClass`) and the class's meaning on demand;
  - its source, its expiry or freshness ("seven years old"), who it's shared with and its reuse scope ("Kora only; not reused for other employers unless you choose");
  - redaction is already present; keep it;
  - Seyi Okoro's CV claims shown honestly as claims, with a calm, constructive Q line (no judgement).
- **Seyi Okoro's request (step 6):** when Kora's reuse decision is SENT, his home and applications show a respectful request card:
  - what Kora wants (from `BOUNDED_SAMPLE`), why, and the effort in minutes;
  - choices: do it now, share existing work instead, or decline with an optional reason.
  "Do it now" opens a simple simulated sample panel (a short task statement and an answer box), then `ev.sample.submit`. The item then appears in the Passport as "Self-reported, waiting for review" (step 7). Show its review outcome when Ada reviews it.
- **Jobs (pack item E):** "Hiring confirmed by Kora Pay on <date>" from `proof(w).intents` for participating employers only, clearly separate from listings without confirmation (Rivers' job shows no such label). Don't call a discovered external post verified.
- **Applications:**
  - Kora's process commitment: "Next update by <date> · owner"; overdue shown honestly, for example Zara's;
  - the candidate's own interest answer (`ev.interest.answer`) when Kora asks (step 10; Tobi confirms);
  - candidate-approved feedback after review (pack Work A.3: candidate-side feedback). Show the reviewer's note to the candidate only when the employer shares it; use the reuse decision's REVIEWED state and its note, labelled "shared by Kora".
- **J7 responds to a verified gap (step 12, pack item F):** on Tobi's home, a Q card or section: on-call leadership is only partial for this role. A private practice suggestion (never visible to employers), and how a reviewed incident walk-through would become evidence he could choose to share. Use the existing career or practice pieces where they fit.
- **Mutual preferences:** a small "What you want" panel on the Passport or Applications, editable by the candidate, from `proof(w).prefs`, with who it's shared with. Unknown stays blank, never a default.
- **P6, "make my CV sound stronger":** a Q skill producing a clearer CV draft as an artifact. It restructures and words better, and never adds jobs, qualifications or assessed skills; it can link evidence the candidate permits. The candidate approves the final version. Show the diff of wording, and mark anything Q would not add.
- **Revocation (step 13, candidate half):** stopping sharing `e_tobi_incident` with Kora works from the Passport, using the existing revoke. Make sure the "what Kora sees" preview updates.

**Files you own:**
- `journeys/talent-b/*`
- the `CandidateHome` component in `routes/entry.tsx` only
- new `journeys/evidence/candidate/*`
- new `q/skills/evidence-candidate.ts`, `q/proactive/evidence-candidate.ts`
- `journeys/career/*` (only small reuse hooks)

Don't edit `journeys/evidence/model.ts` or `ops.ts`; report what you need. Don't edit the recruiter side: `journeys/hire-b/*`, `q/skills/evidence.ts`, `screens/QHome.tsx`.

**Tests:**
- Write `qa/scripts/features/evidence-candidate.mjs` for phone and desktop, covering:
  - proof classes match the recruiter words;
  - Seyi Okoro's request: do, submit, waiting for review; decline recorded as declined;
  - hiring intent shown only for confirmed jobs;
  - commitments, with overdue honest;
  - Tobi's interest;
  - the J7 card is private;
  - the CV rewrite never adds claims;
  - revocation updates the preview.

  Set up the employer's SENT request through the store (`window.__tqQA.update`), the way other feature tests inject state.
- Run T1, T3, T4 and T5 against your own build (env `BASE` style; T4 takes a base URL argument; see `qa/scripts/journeys/run-all.sh`). Fix any regression you caused.
- `npx tsc --noEmit -p .` must be clean.
- Use port 5197.
- Don't commit.

**Report:** routes and components changed, skills invoked, test counts, regressions fixed, open issues, and requests for the lead.

- 🔧 `Bash`: cd /home/user/neo; ls docs/sources/batch-6/; wc -l docs/sources/batch-6/* talent-q-design/journeys/J12-EVIDENCE-FIRST.md; cd talent-q-design/prototype; git status --short | head -50; ls src src/journeys src/journeys/evidence src/journeys/talent-b src/journeys/career src/q src/q/skills src/q/proactiv
… [33 more characters trimmed]

  <details><summary>result</summary>

```
00_START_HERE_PRODUCT_DECISION.md
01_BUYER_EVIDENCE_AND_PRICING.md
02_ARCHITECTURE_AND_IMPLEMENTATION_MAP.md
03_CLAUDE_SINGLE_EXECUTION_DIRECTIVE.md
04_SOURCE_LEDGER.md
05_DEMONSTRATION_AND_ACCEPTANCE.md
   54 docs/sources/batch-6/00_START_HERE_PRODUCT_DECISION.md
   73 docs/sources/batch-6/01_BUYER_EVIDENCE_AND_PRICING.md
   89 docs/sources/batch-6/02_ARCHITECTURE_AND_IMPLEMENTATION_MAP.md
   56 docs/sources/batch-6/03_CLAUDE_SINGLE_EXECUTION_DIRECTIVE.md
   34 docs/sources/batch-6/04_SOURCE_LEDGER.md
   48 docs/sources/batch-6/05_DEMONSTRATION_AND_ACCEPTANCE.md
   59 talent-q-design/journeys/J12-EVIDENCE-FIRST.md
  413 total
 M ../../docs/sources/INDEX.md
 M src/journeys/hire-b/model.ts
 M src/main.tsx
 M src/state/domain.ts
?? ../../docs/sources/batch-6/
?? ../journeys/J12-EVIDENCE-FIRST.md
?? src/journeys/evidence/
?? src/q/skills/evidence-ops.ts
?? src/state/areas/proof.ts
?? src/state/seeds/proof.ts
src:
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

src/journeys:
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

src/journeys/career:
Atlas.tsx
Career.tsx
Route.tsx
j7.ts
personas.ts

src/journeys/evidence:
model.ts
ops.ts

src/journeys/talent-b:
Applications.tsx
Jobs.tsx
Memory.tsx
Passport.tsx
Prep.tsx
logic.ts
ui.tsx

src/q:
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

src/q/proactive:
agency.ts
hire-a.t
… [504 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo; cat docs/sources/batch-6/00_START_HERE_PRODUCT_DECISION.md docs/sources/batch-6/02_ARCHITECTURE_AND_IMPLEMENTATION_MAP.md docs/sources/batch-6/05_DEMONSTRATION_AND_ACCEPTANCE.md talent-q-design/journeys/J12-EVIDENCE-FIRST.md
- 🔧 `Bash`: cd /home/user/neo; cat docs/sources/batch-6/01_BUYER_EVIDENCE_AND_PRICING.md docs/sources/batch-6/03_CLAUDE_SINGLE_EXECUTION_DIRECTIVE.md docs/sources/batch-6/04_SOURCE_LEDGER.md | head -170
- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; cat journeys/evidence/model.ts journeys/evidence/ops.ts q/skills/evidence-ops.ts
- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; cat state/areas/proof.ts state/seeds/proof.ts; git diff state/domain.ts main.tsx journeys/hire-b/model.ts

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
… [23034 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// Evidence-first reading (Consolidated Build Pack, 30 Oct). Shared by recruiter and candidate views so both sides use
// the same words. Rules from the pack, kept in code:
//   unverified claim ≠ incompetence · demonstrated sample ≠ guaranteed performance · Q's analysis ≠ the decision.
//   Missing CV keywords never reject. A polished CV is never treated as verified competence. Unknown is not zero.
import type { Evidence } from '@contracts';
import type { World } from '../../mock/world';
import type { ProofClass } from '../../state/domain';
import { cellFor, disputedEvidence, reqsOf } from '../hire-b/model';
import type { Level } from '../../state/areas/hire-b';
import { proof } from '../../state/areas/proof';

/** How an item is known, from its kind and its verification, never from how well it is written. */
export function proofClass(w: World, e: Evidence): ProofClass {
  if (disputedEvidence(w).has(e.evidenceId) || e.verification === 'UNDER_REVIEW') return 'DISPUTED';
  if (e.kind === 'CLAIM') return 'CLAIM';
  if (e.verification === 'VERIFIED') return e.kind === 'CREDENTIAL' || e.kind === 'EMPLOYMENT' || e.kind === 'REFERENCE' ? 'ISSUER_VERIFIED' : 'ASSESSED';
  return 'SELF_REPORTED';
}
export const PROOF_WORD: Record<ProofClass, string> = { CLAIM: 'Claim', SELF_REPORTED: 'Self-reported', ASSESSED: 'Assessed', ISSUER_VERIFIED: 'Issuer-verified', DISPUTED: 'Disputed' };
export const PROOF_MEANS: Record<ProofClass, string> = {
  CLAIM: 'Said by the candidate (CV or conver
… [11707 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b9ucdnzb1.txt

Preview (first 2KB):
# Talent Q | Consolidated product decision and launch thesis
**30 October 2026 | Product-definition consolidation | Not production readiness or customer validation**

## The decision in one page
Talent Q remains a **global, AI-native candidate and employer operating experience**, not a stripped-down recruitment application. The full previously approved founder vision survives. To begin implementation without infrastructure hell, prioritize the **Capability-to-Opportunity Loop** as the first revenue-critical vertical slice while preserving the comprehensive product blueprint for later slices.

**Frontier:** "Find the people who can do the work, not merely the people who write the best CVs. Show the proof, close only the gaps, and move the opportunity forward." Commercial version: **Evidence-first hiring, with Q doing the work.** Candidate version: **Show what you can do, even if your CV doesn't.**

**Why this rather than a generic AI recruiter:** The current market already sells AI sourcing, agent-assisted recruitment, adaptive screening, candidate profiles and career advice. The product must unite **job-specific, permissioned proof, recruiter-approved criteria, genuine mutual interest, and full execution** into one workflow, with personal career development between applications. No singl
… [660 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// Evidence-first hiring slice (Consolidated Build Pack, 30 Oct). CVs as documents (separate from evidence), employer
// decisions about reusing evidence, hiring-intent confirmations, process commitments and candidates' own preferences.
// Simulated data. The logic that reads it lives in journeys/evidence/model.ts.
import type { World } from '../../mock/world';
import type { CandidateMutualPreferences, CvDoc, EvidenceReuseDecision, HiringIntentConfirmation, ProcessCommitment } from '../domain';

/** EvidenceClaimLink (pack §02.3): evidence → requirement, versioned, with its own review state. Static links for
 *  seeded evidence live in hire-b's EV_REQ; links for evidence created in the prototype (a reviewed sample) live here. */
export interface EvidenceLink { evidenceId: string; reqId: string; note: string; partial?: boolean; v: number; state: 'PROPOSED' | 'REVIEWED' | 'DISPUTED' }
/** Candidate interest in a role: a pending check, shown apart from suitability; never scored. */
export interface InterestCheck { orgId: string; personId: string; mandateId: string; state: 'REQUESTED' | 'CONFIRMED' | 'DECLINED'; at: string; by: string; note?: string }
export interface ProofState { interest: InterestCheck[]; links: EvidenceLink[]; cvs: Record<string, CvDoc>; reuse: EvidenceReuseDecision[]; intents: HiringIntentConfirmation[]; commitments: ProcessCommitment[]; prefs: Record<string, CandidateMutualPreferences> }

export const area = {
  id: 'proof',
  init: (): ProofState => ({
    
… [14222 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cat /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b9ucdnzb1.txt | cut -c1-1500

  <details><summary>result</summary>

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bpplpz0fc.txt

Preview (first 2KB):
# Talent Q | Consolidated product decision and launch thesis
**30 October 2026 | Product-definition consolidation | Not production readiness or customer validation**

## The decision in one page
Talent Q remains a **global, AI-native candidate and employer operating experience**, not a stripped-down recruitment application. The full previously approved founder vision survives. To begin implementation without infrastructure hell, prioritize the **Capability-to-Opportunity Loop** as the first revenue-critical vertical slice while preserving the comprehensive product blueprint for later slices.

**Frontier:** "Find the people who can do the work, not merely the people who write the best CVs. Show the proof, close only the gaps, and move the opportunity forward." Commercial version: **Evidence-first hiring, with Q doing the work.** Candidate version: **Show what you can do, even if your CV doesn't.**

**Why this rather than a generic AI recruiter:** The current market already sells AI sourcing, agent-assisted recruitment, adaptive screening, candidate profiles and career advice. The product must unite **job-specific, permissioned proof, recruiter-approved criteria, genuine mutual interest, and full execution** into one workflow, with personal career development between applications. No singl
… [660 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/docs/sources/batch-6/00_START_HERE_PRODUCT_DECISION.md

  <details><summary>result</summary>

```
1	# Talent Q | Consolidated product decision and launch thesis
2	**30 October 2026 | Product-definition consolidation | Not production readiness or customer validation**
3	
4	## The decision in one page
5	Talent Q remains a **global, AI-native candidate and employer operating experience**, not a stripped-down recruitment application. The full previously approved founder vision survives. To begin implementation without infrastructure hell, prioritize the **Capability-to-Opportunity Loop** as the first revenue-critical vertical slice while preserving the comprehensive product blueprint for later slices.
6	
7	**Frontier:** "Find the people who can do the work, not merely the people who write the best CVs. Show the proof, close only the gaps, and move the opportunity forward." Commercial version: **Evidence-first hiring, with Q doing the work.** Candidate version: **Show what you can do, even if your CV doesn't.**
8	
9	**Why this rather than a generic AI recruiter:** The current market already sells AI sourcing, agent-assisted recruitment, adaptive screening, candidate profiles and career advice. The product must unite **job-specific, permissioned proof, recruiter-approved criteria, genuine mutual interest, and full execution** into one workflow, with personal career development between applications. No single one of these is unclaimed IP. A long-lived, trusted participation and evidence network *could become* defensible if adoption proves it.
10	
11	## Two concrete promises, no 
… [5750 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/docs/sources/batch-6/02_ARCHITECTURE_AND_IMPLEMENTATION_MAP.md

  <details><summary>result</summary>

```
1	# Talent Q | Preserve Claude's system, integrate new value, build the production vertical slice
2	**Based on Talent-Q-Complete.zip and ALL-SPECS.md uploaded 30 October 2026**
3	
4	## Source-of-truth order
5	1. Latest checked-in `product-definition` requirements and coverage registers in Claude's repository, **not** stale text copied into chat.
6	2. Founder approved brand, Direction D and vision; all old additions retained unless explicitly superseded.
7	3. This consolidation's requirements and launch priority clarify execution; **they do not delete or replace old features**.
8	4. The current working Q runtime repo `neo1415/q`, inspected against its latest integration branch *at implementation time*, determines reuse feasibility. Earlier branch summaries are stale until verified.
9	
10	## What Claude already made (do not duplicate)
11	- `prototype/src/ds` Direction D shell, Q mark, resizable thread + canvas, mobile Q sheet, tokens, motion.
12	- `prototype/src/q` Q simulated conversation engine, role-specific skills, openers, proactive rules, artifact references.
13	- `prototype/src/mock/world.ts` and domain stores (prototype only), consent/tenant logic and state-sharing.
14	- Workflows: onboarding, J7, Evidence Passport, role brief, recruiter comparison, hiring campaigns, rubric studio, email and messages, calendar, interview, agency and planners.
15	- `handoff/MODULE-MAP-AND-ROADMAP.md`, `handoff/ADDENDUM-HANDOFF.md`, `handoff/Q-INTELLIGENCE-SPEC.md`, `handoff/PRIVACY-AND-P
… [10254 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/docs/sources/batch-6/05_DEMONSTRATION_AND_ACCEPTANCE.md

  <details><summary>result</summary>

```
1	# Talent Q | Exact examples and acceptance tests to bridge prototype to production
2	
3	## Scenario P1: The candidate with a bad CV
4	**Actors** Tobi (candidate), Ada (recruiter), Seyi (other candidate). Fictional test data only.
5	1. Tobi's CV is thin and poorly structured, missing terms "Postgres performance" and "API reliability". The product does not auto-decline.
6	2. Tobi allows Q to inspect one project repo and share a reviewed troubleshooting work sample with Kora. Q tags the evidence with source, permission, claims, limitations and an optional human reviewer.
7	3. Ada asks Q "Show me people who have actually fixed performance incidents, even if their resumes are weak."
8	4. Q retrieves job-relevant evidence, explains *why* Tobi might qualify, shows which criteria are not yet demonstrated, and offers one targeted follow-up.
9	5. Seyi's CV mentions every term; Q says this is candidate-reported evidence until separately supported, never calls him a liar.
10	6. Ada can examine both, change the approved role rubric via versioning, and ask Q for questions to resolve the remaining unknowns.
11	7. Candidate interest and permission gate outreach; Q drafts and seeks required approval, then only claims real send or booking after provider evidence.
12	8. Candidate views and revokes shared evidence; employer access and cached view update accordingly.
13	
14	**Pass:** both candidates receive fair, evidence-specific treatment; Q does not equate writing quality with competency or 
… [3770 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/journeys/J12-EVIDENCE-FIRST.md

  <details><summary>result</summary>

```
1	# J12: evidence-first hiring, the defining Talent Q experience
2	
3	Source: Consolidated Build Pack (30 Oct 2026, `docs/sources/batch-6/`): 00 "the key product example", 02 UI improvements A–H, 05 scenario P1.
4	Method: `design-skills:journey-mapping` (usage story, peak-end). This is a proto map; the cast is fictional.
5	
6	**Promise under test:** "Find the people who can do the work, not merely the people who write the best CVs. Show the proof, close only the gaps, and move the opportunity forward."
7	
8	## Rules the experience must keep (from the pack, enforced in code)
9	
10	- An unverified claim is not incompetence.
11	- A demonstrated sample is not guaranteed performance.
12	- Q's analysis is not the hiring decision.
13	- Missing CV keywords never reject anyone.
14	- A polished CV is never treated as verified competence.
15	- Weak writing is never treated as evidence of skill.
16	- Unknown is not zero.
17	- Candidate interest is a pending check, not a score.
18	- No outbound message without approval.
19	
20	## Cast
21	
22	- **Ada Okafor** (recruiter, Kora Pay), hiring a Senior Backend Engineer (`m_backend`). Rubric approved, or approved during the journey.
23	- **Tobi Adeyemi** (`p_tobi`). Thin CV: no "Postgres", vague on payments. Reviewed evidence he chose to share with Kora:
24	  - reconciliation project;
25	  - Postgres tuning exercise;
26	  - debugging work sample (`e_tobi_incident`).
27	- **Seyi Okoro** (`p_seyio`, new). Polished CV naming all five requirements. 
… [4887 more characters trimmed]
```
  </details>


**Claude** · 2026-10-30 10:38

Now the existing candidate files.

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; wc -l journeys/talent-b/* journeys/career/* routes/*.tsx q/skills/talent-b.ts q/proactive/talent-b.ts q/skills/core.ts q/core/* app/*; grep -n "CandidateHome" -r . | head

  <details><summary>result</summary>

```
78 journeys/talent-b/Applications.tsx
   191 journeys/talent-b/Jobs.tsx
    70 journeys/talent-b/Memory.tsx
   369 journeys/talent-b/Passport.tsx
    70 journeys/talent-b/Prep.tsx
   516 journeys/talent-b/logic.ts
    92 journeys/talent-b/ui.tsx
   226 journeys/career/Atlas.tsx
   431 journeys/career/Career.tsx
    66 journeys/career/Route.tsx
   201 journeys/career/j7.ts
   213 journeys/career/personas.ts
    49 routes/agency.tsx
    28 routes/campaigns.tsx
     6 routes/core.tsx
   236 routes/entry.tsx
     6 routes/gallery.tsx
    21 routes/guard.tsx
    34 routes/hire-a.tsx
    17 routes/hire-b.tsx
    30 routes/hire-c.tsx
     7 routes/media.tsx
    18 routes/talent-a.tsx
    17 routes/talent-b.tsx
    30 routes/talent-c.tsx
   466 q/skills/talent-b.ts
    57 q/proactive/talent-b.ts
   176 q/skills/core.ts
   219 q/core/engine.ts
    25 q/core/glossary.ts
    80 q/core/nlu.ts
    33 q/core/openers.ts
    19 q/core/policy.ts
    53 q/core/proactive.ts
    56 q/core/types.ts
    54 app/App.tsx
  4260 total
./routes/entry.tsx:51:function CandidateHome() {
./routes/entry.tsx:114:registerRoute({ path: '/c/home', side: 'candidate', label: 'Q home', render: () => <CandidateHome />, nav: { group: 'Q', label: 'Home', icon: 'home', tab: true, order: 1 } });
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; cat routes/entry.tsx | sed -n 1,130p; cat routes/talent-b.tsx
- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-b/Passport.tsx

  <details><summary>result</summary>

```
1	// T3 · Evidence Passport workspace: a portfolio of proof (grouped by how much weight it carries, with a
2	// proof-at-a-glance strip), simulated resumable uploads, issuer checks with plain explanations, inline previews,
3	// confidential originals with redacted summaries, a per-item × per-organisation disclosure matrix with "what X
4	// sees" (the same visibleEvidence() the recruiter pages read), Q's summary with its basis, and recruiter-search
5	// settings whose preview is computed by the store's own privacy policy (canSeeCandidate / canDiscover).
6	import { useEffect, useMemo, useRef, useState } from 'react';
7	import { motion } from 'motion/react';
8	import type { Evidence } from '@contracts';
9	import { actorOf, useWorld, visibleEvidence } from '../../mock/world';
10	import { Canvas, useNarrow } from '../../ds/Workspace';
11	import { Glyph } from '../../ds/Glyph';
12	import { SwitchRow } from '../../ds/Switch';
13	import { arrive } from '../../ds/motion';
14	import { runAction, useViewState } from '../../q/core/engine';
15	import { prefillQ } from '../../q/QThread';
16	import { useRoute, navigate } from '../../ui/router';
17	import { CELL_LABEL, KIND, VER, cellOf, cellOn, discoveryOf, isCode, myEvidence, orgName, passportStats, reachOf, redactedOf, summaryFor, tb, verOf, viewerOrgs, checkRunning, type Cell } from './logic';
18	import { SeenBy, UploadRow, VerTag } from './ui';
19	import type { UploadKind } from '../../state/areas/talent-b';
20	// MEDIA (audit addendum 
… [30071 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; cat Applications.tsx Jobs.tsx ui.tsx
- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; cat logic.ts

  <details><summary>result</summary>

```
// Entry: sign up (SC-009), verify email (SC-010), choose work mode (SC-011), personalise Q (SC-012),
// plus the home router, candidate home and settings shared by every journey.
import { useState, type ReactNode } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { registerRoute } from './registry';
import { actorOf, discoveryRule, emit, simNow, update, useWorld, type World } from '../mock/world';
import { navigate, Link } from '../ui/router';
import { QMark } from '../ds/QMark';
import { Canvas } from '../ds/Workspace';
import { QHome } from '../screens/QHome';
import { appendQ } from '../q/core/engine';
import { SwitchRow } from '../ds/Switch';
import { arrive } from '../ds/motion';
import '../styles/home.css';
import '../ds/ds.css';

// ---------------- Home sections: journeys add blocks to the home pages ----------------
type Section = { id: string; order: number; when: (w: World) => boolean; render: () => ReactNode };
const sections: Record<'recruiter' | 'candidate', Section[]> = { recruiter: [], candidate: [] };
export const registerHomeSection = (side: 'recruiter' | 'candidate', s: Section) => { if (!sections[side].some((x) => x.id === s.id)) sections[side].push(s); };
const homes: { when: (w: World) => boolean; render: () => ReactNode }[] = [];
/** An area can take over the recruiter home for a kind of organisation (e.g. agencies). */
export const registerRecruiterHome = (when: (w: World) => boolean, render: () => ReactNode) => { homes.pus
… [10385 more characters trimmed]
```
  </details>


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
import { CandidateRatings } from '../rubric/CandidateRatings'; // rubric builder: the person's own ratings (AD-E-14)

const act = (op: string, args: Record<string, unknown> = {}) => void runAction({ label: op, act: { t: 'do', op, args } });
const say = (text: string) => void runAction({ label: text, act: { t: 'say', text } });

export function ApplicationsPage() {
  const w = useWorld((x) => x);
  const a = actorOf(w); const pid = a.personId!;
  const apps = w.applications.filter((x) => x.personId === pid);
  const moved = (id: string) => tb(w).followups.find((f) => f.appId === id)?.state === 'MOVED_ON';
  const sorted = [...apps].sort((x, y) => Number(moved(x.id)) - Number(moved(y.id)) || (y.timeline[0]?.at ?? '').localeCompare(x.timeline[0]?.at ?? ''));
  return (
    <Canvas title="Your applications" kicker={`${apps.length} ${apps.length === 1 ? 'application' : 'applications'}`} open onClose={() => navigate('/c/ho
… [26904 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
<persisted-output>
Output too large (43.6KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/b8h9fccum.txt

Preview (first 2KB):
// talent-b logic shared by pages, Q skills and proactive rules: Passport items, per-organisation disclosure,
// simulated uploads and issuer checks, matching with its basis, honest application status, and candidate
// memory with deletion receipts. Everything mutates the one store; nothing is really uploaded, checked or sent.
import type { Evidence } from '@contracts';
import { canDiscover, orgVerified, canSeeCandidate, discoveryRule, emit, getWorld, now, relationshipWith, simNow, uid, update, type World } from '../../mock/world';
import type { Actor, Application, Job } from '../../state/domain';
import { appendQ, pushUndo, registerOp } from '../../q/core/engine';
import { tb, type CandMemory, type Upload, type UploadKind } from '../../state/areas/talent-b';

export { tb };
export const PSCOPE = (pid: string) => `PERSON:${pid}`;
export const orgName = (w: World, id: string) => w.orgs.find((o) => o.id === id)?.name ?? id;
export const shortOrg = (w: World, id: string) => orgName(w, id).replace(/ (Pay|Health|Logistics|Freight Tech|Care Homes)$/, '');
export const fmtDate = (s: string) => new Date(s).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' });
export const daysBetween = (a: Date, b: Date) => Math.max(0, Math.floor((b.getTime() - a.getTime()) / 864e5));

// ------------
… [637 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; grep -n "^export\|registerOp(" logic.ts | head -120

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
… [5793 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; sed -n 30,125p logic.ts; sed -n 280,362p logic.ts

  <details><summary>result</summary>

```
export const isCode = (e: Evidence) => /repo|code|library|github|worker|api|service/i.test(`${e.title} ${e.source}`);

/** Organisations shown in the disclosure matrix: the three in Tobi's world plus anyone the person applied to. */
export function viewerOrgs(w: World, pid: string) {
  const ids = ['org_kora', 'org_tb', 'org_medlink'];
  for (const a of w.applications.filter((x) => x.personId === pid)) { const o = w.jobs.find((j) => j.id === a.jobId)?.orgId; if (o && !ids.includes(o)) ids.push(o); }
  return ids.filter((id) => w.orgs.some((o) => o.id === id));
}
export type Cell = 'SHARED' | 'PUBLIC' | 'PUBLIC_UNSEEN' | 'REVOKED' | 'NONE' | 'LOCKED' | 'WITHDRAWN';
export function cellOf(w: World, e: Evidence, org: string): Cell {
  if (e.confidential) return 'LOCKED';
  if (w.consents[e.ownerId]?.withdrawnFrom.includes(org)) return 'WITHDRAWN';
  if (e.revokedFrom?.includes(org)) return 'REVOKED';
  // Public items reach only organisations the store lets see the person at all (same rule as visibleEvidence).
  if (e.visibility === 'PUBLIC_PROFILE') return canSeeCandidate(w, e.ownerId, org) ? 'PUBLIC' : 'PUBLIC_UNSEEN';
  if (e.visibility === 'SHARED_WITH' && e.sharedWith.includes(org)) return 'SHARED';
  return 'NONE';
}
export const CELL_LABEL: Record<Cell, string> = { SHARED: 'Shared', PUBLIC: 'Public', PUBLIC_UNSEEN: 'Public, can’t see you', REVOKED: 'Access ended', NONE: 'Not shared', LOCKED: 'Confidential', WITHDRAWN: 'Consent withdrawn' };
export const cellOn = (c: Cell)
… [13181 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; cat q/core/types.ts; sed -n 1,80p q/skills/talent-b.ts; cat q/proactive/talent-b.ts; cat q/core/proactive.ts

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
… [17042 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -rn "skills/talent-b\|proactive/talent-b\|evidence-ops\|skills/evidence" --include=*.ts --include=*.tsx . | grep import; ls journeys/evidence; sed -n 1,60p q/core/engine.ts

  <details><summary>result</summary>

```
model.ts
ops.ts
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

… [2001 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -rn "talent-b\|proactive" main.tsx app/*.tsx q/*.ts q/*.tsx 2>/dev/null | head; grep -rln "import.meta.glob" . | head

  <details><summary>result</summary>

```
app/App.tsx:11:// Feature areas register routes, Q skills, proactive rules and seed data in their own files.
app/App.tsx:15:import.meta.glob('../q/proactive/*.ts', { eager: true });
q/QThread.tsx:11:import { useSuggestions } from './core/proactive';
./mock/world.ts
./app/App.tsx
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; cat app/App.tsx | sed -n 1,30p; grep -n "import.meta.glob" -A3 mock/world.ts

  <details><summary>result</summary>

```
import { MotionConfig } from 'motion/react';
import { useRoute } from '../ui/router';
import { ToastHost } from '../ui/kit';
import { Entry } from '../screens/Entry';
import { Gallery } from '../screens/Gallery';
import { Directions } from '../directions';
import { AppShell } from '../ds/AppShell';
import { matchRoute } from '../routes/registry';
import { useWorld, actorOf } from '../mock/world';

// Feature areas register routes, Q skills, proactive rules and seed data in their own files.
// Discovering them here means areas can be built in parallel without editing a shared file.
import.meta.glob('../routes/*.tsx', { eager: true });
import.meta.glob('../q/skills/*.ts', { eager: true });
import.meta.glob('../q/proactive/*.ts', { eager: true });
import.meta.glob('../q/openers/*.ts', { eager: true });

export function App() {
  const { path } = useRoute();
  const actor = useWorld((w) => actorOf(w));
  if (path === '/x' || path.startsWith('/x/')) return <MotionConfig reducedMotion="user"><Directions path={path} /></MotionConfig>;
  if (path === '/gallery') return <MotionConfig reducedMotion="user"><Gallery /></MotionConfig>;
  const m = matchRoute(path);
  if (!m) {
    if (path === '/' || path === '') return <MotionConfig reducedMotion="user"><Entry /></MotionConfig>;
    return <MotionConfig reducedMotion="user"><NotFound /></MotionConfig>;
  }
  if (m.def.bare || m.def.side === 'public') return <MotionConfig reducedMotion="user">{m.def.render(m.params)}<ToastHost /></MotionC
… [876 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -rn "j_kora_backend\|j_rivers\|org_rivers" --include=*.ts mock state | head -20; grep -rn "applications:" -A12 state/seeds/talent-b.ts | head -40

  <details><summary>result</summary>

```
state/seed.ts:30:  { id: 'org_rivers', name: 'Rivers Logistics', kind: 'EMPLOYER', industry: 'Logistics', size: '60 people', city: 'Port Harcourt', verified: { domain: false, registry: 'PENDING' }, delegation: 'DRAFT_ONLY', setup: { done: true, step: 5 }, guidelines: [] },
state/seed.ts:72:  { id: 'j_kora_backend', orgId: 'org_kora', mandateId: 'm_backend', title: 'Senior Backend Engineer', location: 'Lagos', workMode: 'HYBRID', pay: '₦2.4m–₦3.1m / month', posted: '2026-10-22', status: 'OPEN', needs: ['Payments systems', 'Go in production', 'Postgres at scale'], signals: { domainVerified: true, registryVerified: true, recruiterActive: true, replies: 'Usually replies within 3 days' } },
state/seed.ts:73:  { id: 'j_rivers_backend', orgId: 'org_rivers', title: 'Backend Engineer', location: 'Port Harcourt', workMode: 'ONSITE', pay: 'Not stated', posted: '2026-09-30', status: 'OPEN', needs: ['Go', 'Logistics systems'], signals: { domainVerified: false, registryVerified: false, recruiterActive: false, replies: 'No replies recorded in 30 days' } },
state/seed.ts:83:  { id: 'a_zara_rivers', jobId: 'j_rivers_backend', personId: 'p_zara', status: 'SUBMITTED', shared: ['e_zara_api'], timeline: [{ at: '2026-10-05', text: 'You applied', by: 'YOU' }], lastEmployerActivity: undefined },
state/seed.ts:84:  { id: 'a_zara_kora', jobId: 'j_kora_backend', personId: 'p_zara', status: 'VIEWED', shared: ['e_zara_api', 'e_zara_pg'], timeline: [{ at: '2026-10-26', text: 'You applied', by: 'YOU' }, { 
… [2763 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; ls qa/scripts qa/scripts/features qa/scripts/journeys | head -80; cat qa/scripts/journeys/run-all.sh

  <details><summary>result</summary>

```
Exit code 1
ls: cannot access 'qa/scripts': No such file or directory
ls: cannot access 'qa/scripts/features': No such file or directory
ls: cannot access 'qa/scripts/journeys': No such file or directory
cat: qa/scripts/journeys/run-all.sh: No such file or directory
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; ls; ls qa/scripts qa/scripts/features qa/scripts/journeys 2>/dev/null | head -100; cat qa/scripts/journeys/run-all.sh

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
journey-films.mjs
journeys
lib
review

qa/scripts/features:
campaigns.mjs
contact.mjs
email.mjs
media.mjs
rubric.mjs

qa/scripts/journeys:
J11.mjs
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

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; sed -n 1,80p qa/scripts/features/media.mjs; ls qa/scripts/lib

  <details><summary>result</summary>

```
// MEDIA · candidate-authorised video evidence (audit addendum §F, J11 steps 7–8), desktop 1440×900 and phone 390×844.
// Tobi adds a video by saying it to Q, consents (Kora only, 90 days, alternatives offered), pastes a shortened link
// (never fetched), a sign-in link (fetch failed), uploads, loses the connection at 40% (PAUSED), resumes from the same
// part, transcription (simulated), corrects a line by telling Q, shares only parts 1 and 3 with Kora, previews.
// Ada: notice of the new walkthrough, report without a rubric (maps to the brief), then with rubric v1 (findings,
// timestamps that seek, not shown, coverage, Q-proposed Rating records), segment 2 text never on her page, the
// prohibited-inference refusals, where/play/summarise, an override with a reason, mark reviewed. Tobi disputes a
// finding, stops sharing (Ada sees nothing), deletes it.
// Usage: BASE=http://localhost:5194/ node qa/scripts/features/media.mjs [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
const ROOT = new URL('../../../captures/features/media/', import.meta.url).pathname; mkdirSync(ROOT, { recursive: true });
const BASE = process.env.BASE || 'http://localhost:5194/';
const ONLY = (process.argv[2] || 'd,m').split(',');
const SEG2 = ['I was on call that night', 'merchant clients', 'finance lead', 'backup file feed', 'Client dashboard', 'post-mortem the next morning'];
const RUBRIC = {
  id: 'rub_m_backend', mandateId: 'm_backend', 
… [7719 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; wc -l design-system/DIRECTION-D-SYSTEM.md handoff/DESIGN-QUALITY-GATE.md journeys/design/media.md; cat handoff/DESIGN-QUALITY-GATE.md | head -120
- 🔧 `Bash`: cd /home/user/neo/talent-q-design; sed -n 1,400p design-system/DIRECTION-D-SYSTEM.md
- 🔧 `Bash`: cd /home/user/neo/talent-q-design; cat journeys/design/media.md; ls journeys/design

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
… [5410 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
114 design-system/DIRECTION-D-SYSTEM.md
   16 handoff/DESIGN-QUALITY-GATE.md
   77 journeys/design/media.md
  207 total
# Design quality gate

From now on, no journey moves from "it works" straight to recording. Each journey, and each new screen within one, passes these checkpoints in order. Keep it light: the output is better screens, not paperwork.

| # | Checkpoint | What happens | Proof it happened |
|---|---|---|---|
| 1 | Design research and skills, **before** building | Load the relevant skills and apply them to the brief: `design-critique`, `design-elevation`, `interaction-design`, `ux-writing`, plus `dataviz` for any chart or ledger and `design-superpowers:creative` for the candidate surfaces | One line per skill in the journey's design note: which screens it shaped |
| 2 | Visual implementation | Build with `src/ds` components and the execution rules in `design-system/DIRECTION-D-SYSTEM.md`. Fix shared problems in the shared component, not on one page | — |
| 3 | Browser rendering | `qa/scripts/review/capture-all.mjs` captures every page in the journey at desktop 1440 and phone 390, plus its key states | `captures/review/after/` |
| 4 | Visual critique | Look at every capture against the critique checklist (hierarchy, density, excise, labels, copy, touch, states, motion) and write down the defects | Defect list in the journey's design note |
| 5 | Corrections | Fix the defects, then recapture. Repeat until you would show it to a design lead | Before/after pairs for 
… [629 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
# Design pass · media (audit addendum §F: candidate-authorised video and voice evidence; J11 steps 7–8)

Routes: the candidate side lives in the Evidence Passport (`/c/passport`, Proof view, section "Video and voice", deep links
`?media=add|review|parts|preview|ready`); the recruiter report is the new `/r/people/:id/video` (`?t=<s>&play=1` seeks).
Captures: `captures/features/media/{d,m}-NN-*.png` (full page, every state, from the test) and element captures in
`captures/review/pairs/media/{first-el,after-el}/`. `qa/scripts/features/media.mjs` passes 114/114 (57 desktop, 57 phone).
T3 54/54 and T5 52/52 still pass. No page scrolls sideways at 390 px.

## Skills invoked (Skill tool) → screens → changes
- **interaction-design** → the item state machine (CONSENT → UPLOADING ⇄ PAUSED → TRANSCRIBING → REVIEW → READY → REVOKED,
  plus UNSAFE_LINK / FETCH_FAILED), written at the top of `journeys/media/logic.ts`. The upload shows **parts** (10 blocks),
  so "carries on from part 5" is visible, not just claimed. Pausing is condition-driven (the connection), resuming is
  automatic on reconnect (condition loop), with a manual "Resume" only when online. Playback is event-caused (the
  playhead moves only while playing); seeking is instant. Destructive actions (stop sharing, delete, sharing a
  confidential part) use an inline confirmation that states the consequence; reversible ones (transcript fixes, marking
  reviewed) use Undo instead. Goal-gradient: a 4-step indicator (Consent · Reco
… [5832 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/career; sed -n 1,60p j7.ts; grep -n "export\|p_tobi\|registerRoute\|registerHomeSection" *.ts *.tsx | head -60

  <details><summary>result</summary>

```
// J7 career state and the operations Q (and the atlas page) perform on it. One store (World v4): each
// person's J7 lives at w.j7[personId] and is PERSON-scoped. Practice and assessments are mirrored into the
// Passport as PRIVATE items; nothing here ever widens who can see anything. Sharing is a separate,
// explicitly approved act (see the talent-a skills).
import { emit, simNow, visibleEvidence, type World } from '../../mock/world';
import { anyOf, near } from '../../q/core/nlu';
import { profileText, readProfile } from '../../services/profile';
import { PERSONAS, type CState, type JOcc, type Persona, type PlanStep, type Practice, type Rec, type Sample } from './personas';

export type PId = Persona['id'];
export const PERSON_OF: Record<PId, string> = { graduate: 'p_amaka', switcher: 'p_chidi', experienced: 'p_tobi' };
export const pidFor = (personId: string): PId => (personId === 'p_chidi' ? 'switcher' : personId === 'p_tobi' ? 'experienced' : 'graduate');
export const personaFor = (personId: string): Persona => PERSONAS[pidFor(personId)];
export const shown = (s: CState) => s === 'verified' || s === 'full';

export interface Assessment { id: string; comp: string; at: string; level: number; round: number; rubric: { c: string; ok: boolean }[] }
export interface J7State {
  v: 2; goal: string; states: Record<string, CState>; record: Rec[]; plan: PlanStep[]; moved: Record<string, number>;
  archived: { occ: string; at: string; why: string; steps: PlanStep[] }[];
  quiz: {
… [8331 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/career; grep -n "experienced" -A40 personas.ts | grep -n "comps\|practices\|samples\|oncall\|incident\|id:" | head -40; grep -rn "/c/career\|path: '/c" ../../routes/talent-a.tsx

  <details><summary>result</summary>

```
13:14-  id: string; label: string; plain: string; state: CState;
22:23-export interface JOcc { id: string; label: string; short: string; family: string; needs: string[]; demand?: string; extra?: boolean; aliases?: string[] }
24:25-export interface Rec { id: string; at: string; comp: string; cls: RecClass; why: string; not: string; moved?: string; level?: number }
27:28-  options: { id: string; text: string; code?: boolean; verdict: 'right' | 'partial' | 'wrong'; kws: string[] }[];
37:38-export interface PlanStep { id: string; comp: string; title: string; kind: StepKind; minutes: number; why: string; goals: string[]; dueIn: number; due?: string; done?: boolean; doneAt?: string; progress?: number; note?: string; resource?: string }
39:40:  id: 'graduate' | 'switcher' | 'experienced'; name: string; first: string; line: string; goal: string; horizon: string;
40:41-  comps: Comp[]; occs: JOcc[]; extra: JOcc[]; families: string[];
41:42-  practices: Practice[]; samples: Sample[]; record: Rec[];
52:53-  { id: 'sheets', label: 'Spreadsheet modelling', plain: 'Models that answer a business question', state: 'none', kws: ['excel', 'spreadsheet', 'google sheets', 'sheets', 'pivot'] },
53:54-  { id: 'story', label: 'Dashboard storytelling', plain: 'Turning numbers into a decision', state: 'none', kws: ['dashboard', 'chart', 'power bi', 'presentation', 'powerpoint'] },
54:55-  { id: 'stats', label: 'Statistics fundamentals', plain: 'Sampling, significance, confidence', state: 'none', kws:
… [5993 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/career; sed -n 183,213p personas.ts; sed -n 60,201p j7.ts

  <details><summary>result</summary>

```
{ id: 'platform', label: 'Platform Engineer', short: 'Platform', family: 'Platform', needs: ['go', 'dist', 'incident'] },
      { id: 'sre', label: 'Site Reliability Engineer', short: 'SRE', family: 'Platform', needs: ['incident', 'dist', 'go', 'writing'] },
      { id: 'data', label: 'Data Engineer', short: 'Data Eng.', family: 'Data', needs: ['pg', 'go', 'dist'] },
      { id: 'em', label: 'Engineering Manager', short: 'Eng Manager', family: 'Leadership', needs: ['mentor', 'incident', 'roadmap', 'writing'] },
      { id: 'tl', label: 'Tech Lead', short: 'Tech Lead', family: 'Leadership', needs: ['sysd', 'mentor', 'writing'] },
    ],
    extra: [], families: ['Backend', 'Platform', 'Data', 'Leadership'],
    practices: [{
      comp: 'incident', question: 'Payments are failing for 8% of users and the cause is unknown. What do you do in the first ten minutes?',
      options: [{ id: 'a', text: 'Start debugging the most likely service yourself', verdict: 'partial', kws: ['debug'] }, { id: 'b', text: 'Declare an incident, assign roles (lead, comms, ops), stabilise first, then investigate', verdict: 'right', kws: ['declare', 'roles', 'stabilise', 'stabilize'] }, { id: 'c', text: 'Wait for more data before raising alarm', verdict: 'wrong', kws: ['wait'] }],
      feedback: { right: 'Right order: declare, assign roles, stabilise, then investigate.', partial: 'Debugging alone leaves comms and coordination to nobody.', wrong: 'Waiting while 8% of payments fail costs trust and money
… [13532 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/hire-b; sed -n 70,130p model.ts; grep -n "export function reqsOf\|export const reqsOf\|export function reqLabel\|export const reqLabel\|disputedEvidence" model.ts

  <details><summary>result</summary>

```
export const LEVEL_VALUE: Record<Level, number> = { verified: 3, evidenced: 2, partial: 1, claim: 0, none: 0 };
export const LEVEL_WORD: Record<Level, string> = { verified: 'Verified', evidenced: 'Evidenced, not checked', partial: 'Partial or outdated', claim: 'Claimed, not shown', none: 'Not shown yet' };
export const GLYPH_OF: Record<Level, 'verified' | 'full' | 'partial' | 'none' | 'unclear'> = { verified: 'verified', evidenced: 'full', partial: 'partial', claim: 'unclear', none: 'none' };

export const isGithub = (e: Evidence) => /github|public repo/i.test(e.source);
const YEAR = 365 * 864e5;
const outdated = (w: World, e: Evidence) => simNow(w).getTime() - new Date(e.observedAt).getTime() > 2 * YEAR;

/** Assessment results a candidate disputed: under review and excluded until resolved. */
export function disputedEvidence(w: World): Set<string> {
  const s = new Set<string>();
  for (const i of w.interviews) if (i.disputed && i.disputed.state === 'OPEN') i.feedback.forEach((f) => f.evidenceRefs.forEach((id) => s.add(id)));
  for (const e of w.evidence) if (e.verification === 'UNDER_REVIEW') s.add(e.evidenceId);
  return s;
}

export interface CellItem { e: Evidence; level: Level; note: string; excluded?: 'review' | 'old' | 'confidential' | 'failed' }
export interface Cell { level: Level; items: CellItem[]; correction?: { note: string; by: string } }
export interface Opts { lastYear?: boolean }

export function itemLevel(w: World, e: Evidence, partial?: boolean): Level {

… [3070 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -n "viewerOrg" journeys/hire-b/model.ts | head -3; grep -n "requirements" -A8 state/seed.ts | head -14

  <details><summary>result</summary>

```
16:export const viewerOrg = (w: World) => actorOf(w).orgId ?? 'org_kora';
98:  const org = viewerOrg(w);
149:  return v.people.filter((pid) => canSeeCandidate(w, pid, viewerOrg(w))).map((pid) => {
38:    requirements: [req('s1', 'Team leadership', true, 'Has led a support or service team'), req('s2', 'Payments knowledge', false, 'Understands card and transfer disputes'), req('s3', 'Written clarity', true, 'Writes replies merchants act on')], versions: [{ v: 1, at: '2026-10-10', by: 'u_ngozi', note: 'Approved' }] },
39-  { id: 'm_ops', orgId: 'org_medlink', clientOrgId: 'org_medlink', title: 'Operations Analyst', plain: 'Improves how clinics book and track patients', team: 'Operations', location: 'Remote (Nigeria)', workMode: 'REMOTE', pay: { min: 500000, max: 700000, currency: 'NGN', period: 'month' }, status: 'SOURCING', createdBy: 'u_dele',
40:    requirements: [req('o1', 'Process mapping', true, 'Draws how work actually flows'), req('o2', 'Spreadsheet modelling', true, 'Builds models that answer a question'), req('o3', 'Stakeholder conversations', false, 'Asks teams what they really need')], versions: [{ v: 1, at: '2026-10-20', by: 'u_dele', note: 'From Medlink brief' }] },
41-  { id: 'm_kora_agency', orgId: 'org_tb', clientOrgId: 'org_kora', title: 'Backend Engineer (Kora Pay, via agency)', plain: 'Second backend hire for Kora’s payouts team', team: 'Payouts', location: 'Lagos', workMode: 'ONSITE', pay: { min: 2200000, max: 2800000, currency: 'NGN', period: 'month' }, sta
… [1002 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -n "req('r" state/seed.ts mock/*.ts | head; grep -n "u_ada\|u_ngozi\|u_seyi\|Balogun" state/seed.ts | head

  <details><summary>result</summary>

```
10:  { id: 'u_ada', name: 'Ada Okafor', first: 'Ada', initials: 'AO', side: 'recruiter', title: 'Talent partner', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'RECRUITER', journey: 'R2', email: 'ada@kora.example', signedUp: true },
11:  { id: 'u_ngozi', name: 'Ngozi Eze', first: 'Ngozi', initials: 'NE', side: 'recruiter', title: 'HR lead', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'ADMIN', journey: 'R3', email: 'ngozi@kora.example', signedUp: true },
12:  { id: 'u_seyi', name: 'Seyi Balogun', first: 'Seyi', initials: 'SB', side: 'recruiter', title: 'Engineering manager', timezone: 'Africa/Lagos', orgId: 'org_kora', role: 'HIRING_MANAGER', email: 'seyi@kora.example', signedUp: true },
37:  { id: 'm_support', orgId: 'org_kora', title: 'Customer Support Lead', plain: 'Leads a team of 6 answering merchant questions', team: 'Merchant success', location: 'Lagos', workMode: 'HYBRID', pay: { min: 650000, max: 900000, currency: 'NGN', period: 'month' }, status: 'INTERVIEWING', createdBy: 'u_ngozi',
38:    requirements: [req('s1', 'Team leadership', true, 'Has led a support or service team'), req('s2', 'Payments knowledge', false, 'Understands card and transfer disputes'), req('s3', 'Written clarity', true, 'Writes replies merchants act on')], versions: [{ v: 1, at: '2026-10-10', by: 'u_ngozi', note: 'Approved' }] },
46:  { mandateId: 'm_backend', personId: 'p_tobi', stage: 'SHORTLISTED', at: '2026-10-24', by: 'u_ada' },
47:  { mandateId: 'm_backend', personId: 'p_ife', 
… [409 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -rn "reqId: 'r1'\|'r4'" mock/world.ts state/*.ts ../../contracts 2>/dev/null | head -5; grep -rn "On-call\|on-call" --include=*.ts mock state | head -5; grep -n "simNow\b" -A3 mock/world.ts | head -8; grep -n "now:" state/seed.ts | head

  <details><summary>result</summary>

```
mock/fixtures.ts:19:    { reqId: 'r4', label: 'On-call leadership', mustHave: false, plain: 'Has led incident response and written post-mortems' },
state/seeds/hire-c.ts:18:      { id: 'cq_tobi_medlink', from: 'p_tobi', to: 'org_medlink', subject: 'Question: Senior Platform Engineer', body: 'Hello, I’ve applied for the Senior Platform Engineer role. Is the platform team on a shared on-call rota with product teams, or separate? Thank you, Tobi', at: '2026-10-20T11:30:00+01:00', status: 'RECEIVED', channel: 'IN_APP', delivery: 'ACCEPTED', acceptedAt: '2026-10-20T11:30:00+01:00' },
state/seeds/hire-a.ts:62:    { reqId: 'py4', label: 'On-call', mustHave: false, plain: 'Can take part in an on-call rota, one week in four' },
state/areas/proof.ts:32:        'Led on-call rotations and incident reviews; mentored 6 engineers.',
178:export const simNow = (w: World) => new Date(new Date(w.session.now).getTime() + w.session.offsetDays * 864e5);
179-
180-/** What an organisation may see of a person's Passport: shared items only, never practice, never revoked. */
181-// ---------------- Candidate privacy: one policy for search, profiles, Q's tools, caches and artifacts ----------------
--
214:  const since = simNow(w).getTime() - 7 * 864e5;
215-  return w.threads.filter((t) => t.orgId === orgId).flatMap((t) => t.messages).filter((m) => m.status === 'SENT_SIMULATED' && w.actors.find((a) => a.id === m.from)?.orgId === orgId && new Date(m.at).getTime() >= since).length;
216-}
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; sed -n 10,25p mock/fixtures.ts; grep -n "now: '" mock/world.ts state/seed.ts | head -3; sed -n 180,200p mock/world.ts

  <details><summary>result</summary>

```
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
  { personId: 'p_tobi', name: 'Tobi Adeyemi', headline: 'Backend engineer, reconciliation · 7 yrs', location: 'Lagos', timezone: 'Africa/Lagos', synthetic: true },
/** What an organisation may see of a person's Passport: shared items only, never practice, never revoked. */
// ---------------- Candidate privacy: one policy for search, profiles, Q's tools, caches and artifacts ----------------
/** ANYONE (default, founder decision D1): any organisation, verified or not — unverified ones are limited by orgLimits.
 *  EMPLOYERS_AND_AGENCIES: organisations with a verified domain. VERIFIED_EMPLOYERS: fully checked employers only. */
type DiscoveryRule = { who: 'ANYONE' | 'EMPLOYERS_AND_AGENCIES' | 'VERIFI
… [1457 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; cat package.json | head -20; sed -n 200,212p src/mock/world.ts; grep -n "now:" src/mock/world.ts | head

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
  if (d.who === 'EMPLOYERS_AND_AGENCIES') return o.verified.domain;
  return true; // ANYONE
}
/** A fully verified organisation: domain and business registration both checked. */
export const orgVerified = (o: { verified: { domain: boolean; registry: string } }) => o.verified.domain && o.verified.registry === 'VERIFIED';
/** What an organisation may do until it is verified (founder decisions D1 and D3). One place, so it's easy to change. */
export const UNVERIFIED_LIMITS = { postRoles: false, outreachPerWeek: 3, campaigns: false, submittals: false, seeContactDetails: false } as const;
export function orgLimits(w: World, orgId: string) {
  const o = w.orgs.find((x) => x.id === orgId);
  if (o && orgVerified(o)) return { verified: true, postRoles: true, outreachPerWeek: Infinity, campaigns: true
… [367 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; grep -rn "const NOW" src | head -2; (nohup npx vite --port 5197 --strictPort > /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/vite.log 2>&1 &); sleep 4; tail -5 /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d
… [21 more characters trimmed]

  <details><summary>result</summary>

```
src/state/seed.ts:6:export const NOW = '2026-10-29T09:00:00+01:00';

Are they installed?
    at file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50669:15
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50174:26
```
  </details>

- 🔧 `Bash`: head -30 /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/vite.log

  <details><summary>result</summary>

```
Re-optimizing dependencies because vite config has changed

  VITE v5.4.21  ready in 649 ms

  ➜  Local:   http://localhost:5197/
  ➜  Network: use --host to expose
Error: The following dependencies are imported but could not be resolved:

  @emotion/is-prop-valid (imported by /home/user/neo/talent-q-design/prototype/dist-review/assets/index-7nVgRM4N.js)

Are they installed?
    at file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50669:15
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50174:26
```
  </details>

- 🔧 `Skill`: {"skill": "design-skills:interaction-design", "args": "Candidate side of evidence-first hiring (Talent Q J12): a respectful bounded work-sample request card (do now / share existing / decline with opt

  <details><summary>result</summary>

```
Launching skill: design-skills:interaction-design
```
  </details>


**User** · 2026-10-30 10:39

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


ARGUMENTS: Candidate side of evidence-first hiring (Talent Q J12): a respectful bounded work-sample request card (do now / share existing / decline with optional reason) with a simulated sample panel; proof-class labels on Passport items; interest answer; commitments with overdue; CV rewrite draft with wording diff and candidate approval; revoke sharing with live preview.

- 🔧 `Skill`: {"skill": "design-skills:ux-writing", "args": "Candidate copy for evidence-first hiring: work-sample request card, decline (recorded as declined, not failed), proof-class meanings, CV claims shown as

  <details><summary>result</summary>

```
Launching skill: design-skills:ux-writing
```
  </details>


**User** · 2026-10-30 10:39

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


ARGUMENTS: Candidate copy for evidence-first hiring: work-sample request card, decline (recorded as declined, not failed), proof-class meanings, CV claims shown as claims with a calm Q line, hiring-intent label, process commitment and overdue, J7 private practice card, CV rewrite marks.

- 🔧 `Skill`: {"skill": "design-skills:design-elevation", "args": "Direction D candidate surfaces (warm paper, ink, gold for Q only): request card, sample panel, proof-class labels, CV draft diff artifact, preferen

  <details><summary>result</summary>

```
Launching skill: design-skills:design-elevation
```
  </details>


**User** · 2026-10-30 10:39

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


ARGUMENTS: Direction D candidate surfaces (warm paper, ink, gold for Q only): request card, sample panel, proof-class labels, CV draft diff artifact, preferences panel.

- 🔧 `Skill`: {"skill": "design-superpowers:creative", "args": "Inside Direction D (candidate warmth variant exists). Visual idea for proof-class labelling on the Passport and for a CV wording diff, no new palette.

  <details><summary>result</summary>

```
Launching skill: design-superpowers:creative
```
  </details>


**User** · 2026-10-30 10:39

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


ARGUMENTS: Inside Direction D (candidate warmth variant exists). Visual idea for proof-class labelling on the Passport and for a CV wording diff, no new palette.

- 🔧 `Skill`: {"skill": "dataviz", "args": "Passport \"proof at a glance\" part-to-whole strip regrouped by proof class (Claim, Self-reported, Assessed, Issuer-verified, Disputed) in Direction D; must use shape not

  <details><summary>result</summary>

```
Launching skill: dataviz
```
  </details>


**User** · 2026-10-30 10:39

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

Passport "proof at a glance" part-to-whole strip regrouped by proof class (Claim, Self-reported, Assessed, Issuer-verified, Disputed) in Direction D; must use shape not colour, direct labels, list fallback.

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts/journeys; grep -n "strip\|at the source\|Waiting on a check\|Your own uploads\|tb-group\|labels mean" T3.mjs T5.mjs T4.mjs T1.mjs | head -30; head -30 T3.mjs

  <details><summary>result</summary>

```
// T3 · Tobi, the experienced specialist. Drives the Evidence Passport mostly by typing to Q (with typos),
// on desktop 1440×900 and phone 390×844. Curveballs: a dropped upload resumed after navigating away
// [recover]; the issuer unreachable then unable to confirm [info]; confidential work asked for casually,
// twice [info]; revoking Talentbridge's access, undo, and the recruiter view updating [info][mind];
// challenging Q's summary [mind]. Usage: node T3.mjs [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
const ROOT = new URL('../../../captures/cx/T3/', import.meta.url).pathname; mkdirSync(ROOT, { recursive: true });
const BASE = process.env.BASE || 'http://localhost:5186/';
const ONLY = (process.argv[2] || 'd,m').split(',');
const b = await pw.chromium.launch();
const results = []; const errors = [];
for (const [v, vp, dpr] of [['d', { width: 1440, height: 900 }, 1], ['m', { width: 390, height: 844 }, 2]].filter(([x]) => ONLY.includes(x))) {
  const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: dpr });
  const page = await ctx.newPage();
  page.on('pageerror', (e) => errors.push(`${v}: ${e.message}`));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|Failed to load resource/.test(m.text())) errors.push(`${v}: ${m.text()}`); });
  const phone = v === 'm';
  const step = (name, ok, detail = '') => { results.push({ v, name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} [${v}] ${na
… [1807 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts; grep -rln "Checked at the source\|Waiting on a check\|Your own uploads\|tb-strip\|tb-group\|proof at a glance" . | head; grep -rn "VerTag\|ds-tag" journeys/T3.mjs | head -5; grep -rn "Verified\b'" journeys/T3.mjs | head -5

  <details><summary>result</summary>

```
./features/rubric.mjs
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts; grep -n "Checked at the source\|Waiting on a check\|Your own uploads\|tb-strip\|tb-group" features/rubric.mjs; grep -n "passport" journeys/T3.mjs | head -30

  <details><summary>result</summary>

```
109:  step(v, 'inspector: freshness and reliability', /Checked at the source|Not checked yet|Candidate’s own video/.test(await page.locator('.rb-inspect').first().innerText()) && /Evidence/.test(await page.locator('#pf-score').innerText()));
39:  await page.goto(`${BASE}#/c/passport`); await page.evaluate(() => localStorage.clear()); await page.reload(); await page.waitForTimeout(600);
40:  await as('p_tobi', '/c/passport');
42:  await overflow('passport'); await shot('01-passport');
88:  await closeQ(); await page.goto(`${BASE}#/c/passport?item=e_tobi_conf_red`); await page.waitForTimeout(500); await shot('04-redacted-preview');
99:  step('revokedFrom set; event emitted to Talentbridge scope (no titles)', pay.revokedFrom?.includes('org_tb') && w.events.some((e) => e.scope === 'SHARED:org_tb:p_tobi' && e.type === 'passport.access_ended' && !/Payout/.test(e.text)));
106:  await closeQ(); await page.goto(`${BASE}#/c/passport?as=org_tb`); await page.waitForTimeout(500);
109:  await page.goto(`${BASE}#/c/passport?tab=sharing`); await page.waitForTimeout(400); await page.locator('.ds-views button', { hasText: 'Sharing' }).click(); await page.waitForTimeout(300);
120:  await as('p_tobi', '/c/passport');
127:  await closeQ(); await page.goto(`${BASE}#/c/passport?tab=summary`); await page.waitForTimeout(500); await shot('09-summary-corrected');
135:  await closeQ(); await page.goto(`${BASE}#/c/passport?tab=discovery`); await page.waitForTimeout(400); await shot('10-discovery');
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -n "areas" mock/world.ts | head; grep -n "export interface Job\b" -A8 state/domain.ts; grep -n "export interface Application\b" -A4 state/domain.ts; grep -n "interface Evidence\b" -A25 ../../contracts/*.ts 2>/dev/null | head -40; grep -rn "@contr
… [51 more characters trimmed]

  <details><summary>result</summary>

```
23:  /** Per-area slices owned by one feature area each (see src/state/areas/*). Typed by that area's accessor. */
24:  areas: Record<string, unknown>;
62:/** Feature areas add their own seed records in src/state/seeds/*.ts (export const seed: SeedPatch). */
64:/** Feature areas with their own state register an initial slice in src/state/areas/*.ts (export const area). */
65:const AREA_INITS = Object.values(import.meta.glob<{ area: { id: string; init: () => unknown } }>('../state/areas/*.ts', { eager: true })).map((m) => m.area).filter(Boolean);
77:    profiles: {}, j7: {}, planners: {}, areas: Object.fromEntries(AREA_INITS.map((a) => [a.id, a.init()])),
104:    if (raw) { const w = JSON.parse(raw) as World; if (w.v === 4) return { ...w, network: 'online', areas: { ...Object.fromEntries(AREA_INITS.map((a) => [a.id, a.init()])), ...(w.areas ?? {}) } }; }
186:export const discoveryRule = (w: World, pid: string): DiscoveryRule => (w.areas['talent-b'] as { discovery?: Record<string, DiscoveryRule> } | undefined)?.discovery?.[pid] ?? { who: 'ANYONE', hideFrom: [] };
161:export interface Job {
162-  id: string; orgId: string; mandateId?: string; title: string; location: string; workMode: 'ONSITE' | 'HYBRID' | 'REMOTE'; pay: string; posted: string;
163-  status: 'OPEN' | 'CLOSED'; needs: string[];
164-  signals: { domainVerified: boolean; registryVerified: boolean; recruiterActive: boolean; replies: string };
165-}
166-export type AppStatus = 'DRAFT' | 'SUBMITTED' | 'VIEWED' | 'INTE
… [3190 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; sed -n 60,219p q/core/engine.ts

  <details><summary>result</summary>

```
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
    const scored = skills.filter((s) => s.side === 'both' || s.side === c.actor.side).map((s) => ({ s, score: s.match(c) })).sort((a, b) => b.score - a.score);
    const best = scored[0];
    if (best && best.score >= 0.45) {
      const r = await best.s.handle(c);
      // A new intent suspends (not discards) the previous frame, so Q can come back to it.
      if (c.frame && best.s.id !== c.frame.intent && r.frame === undefined) r.frame = 
… [8020 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -n "revoke\|stop shar" q/skills/talent-b.ts | head -20; grep -n "registerSkill({" -A2 q/skills/talent-b.ts | grep "id:" | head -40

  <details><summary>result</summary>

```
79:      if (c.frame?.slots.stage === 'share-redacted' && org && /share|send|yes|ok|go ahead/.test(c.norm)) return { msgs: [reply(`Shared the redacted summary with ${orgName(c.w, org)}. The original stays private.`)], effects: (w, a) => { const e = evById(w, 'e_tobi_conf_red'); if (e) { e.visibility = 'SHARED_WITH'; if (!e.sharedWith.includes(org)) e.sharedWith.push(org); e.revokedFrom = (e.revokedFrom ?? []).filter((x) => x !== org); emit(w, a.id, 'passport.shared', `SHARED:${org}:${a.personId}`, `${a.name} shared 1 Passport item with ${orgName(w, org)}.`); } }, frame: null };
92:const REVOKE_RE = /\b(stop|revoke|remove|take away|take back|end|cut off|block|unshare|no longer|withdraw|hide)\b/;
116:  id: 'tb.revoke', side: 'candidate',
128:      actions: [{ label: `End ${orgName(c.w, org)}’s access`, primary: true, act: { t: 'do', op: 'tb.revoke', args: { ids: items.map((e) => e.evidenceId), org } } }, { label: `Preview ${orgName(c.w, org)}’s view`, act: { t: 'nav', to: `/c/passport?as=${org}` } }, { label: 'Keep it', act: { t: 'say', text: 'keep it' } }],
311:  if (target.state === 'VERIFIED' || target.state === 'SHOWN') return { msgs: [reply(`For ${target.need} I used ${target.used.map((e) => `“${e.title}”`).join(', ')}. If that overstates it, you can stop sharing that item with ${orgName(c.w, job.orgId)}, or tell me what’s more accurate.`)], frame: null };
71-  id: 'tb.conf', side: 'candidate',
86-  id: 'tb.redact', side: 'candidate',
94-  id: 'tb.share', side: 'candidate'
… [1173 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -n "query\|useRoute\|practi" journeys/career/Career.tsx | head -20; grep -n "j7\.\(practice\|quiz\)\|registerOp('j7" -r q/skills/talent-a.ts | head

  <details><summary>result</summary>

```
2:// transferable skills, evidence vs gaps, a plan with practice, work samples and learning, assessment and
5:// Evidence model: practice is private and never moves the map; only reviewed work or a verified credential does.
21:const CLS_GLYPH: Record<RecClass, CState> = { 'Practice attempt': 'practice', 'Work sample submitted': 'partial', 'Assessed by rubric and reviewer': 'full', 'Verified credential': 'verified' };
92:      <p className="t14 muted" style={{ margin: 0 }}>Your career plan, practice and assessments are private. They never become visible on their own; sharing is a separate step you approve.</p>
103:  if (k === 'practice') return 'Practice only. Private, and not proof.';
158:  const pr = quiz ? P.practices.find((x) => x.comp === quiz.comp)! : null;
165:    const hasPractice = P.practices.some((x) => x.comp === cid);
194:            {quiz.pick && <p className="talent-a-feedback" aria-live="polite">{pr.feedback[pr.options.find((x) => x.id === quiz.pick)!.verdict]} <span className="muted">Logged as private practice. Your map didn’t move: practice isn’t proof.</span></p>}
249:  Practice: { proof: false, note: 'Private practice · not proof' }, Learning: { proof: false, note: 'Learning · prepares you, not proof' }, Conversation: { proof: false, note: 'Prepares you, not proof' },
282:                <span className="talent-a-tags"><span className={`talent-a-kind${kd.proof ? ' is-proof' : ''}`}><Glyph k={kd.proof ? 'full' : 'practice'} size={14} />{kd.note}</span>{isLat
… [2696 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; sed -n 695,700p q/skills/talent-a.ts; sed -n 930,945p q/skills/talent-a.ts

  <details><summary>result</summary>

```
// ---------- Practice quiz: private, never proof ----------
reg({
  id: 'ta.j7.quiz', side: 'candidate',
  match: (c) => (cand(c) && /\b(quiz|test me|try a question|a question on|practi[sc]e)\b/.test(c.norm) && !/\binterview\b/.test(c.norm) ? 0.84 : 0),
  handle: (c) => {
    const pid = pidOf(c.actor); const P = personaFor(pid);
  pushUndo(w, actor.id, `Removed “${s.title}”`, 'ta.j7.restore', { personId: pid, snap: JSON.stringify(S) });
  S.plan = S.plan.filter((x) => x.id !== a.id);
  return { say: `Removed “${s.title}” from your plan. The gap stays on your map until evidence closes it. Say “undo” to bring it back.` };
});
registerOp('ta.j7.quiz.start', (w, a, actor) => {
  const pr = startQuiz(w, pidOf(actor), a.comp ? String(a.comp) : undefined); if (!pr) return;
  const P = personaFor(pidOf(actor));
  w.q.frames[actor.id] = { intent: 'ta.j7.quiz', slots: { comp: pr.comp }, awaiting: 'option', startedAt: new Date().toISOString() };
  appendQ(w, actor.id, { who: 'q', engine: 'rules', kind: 'question', why: 'Practice · private · not proof', text: `One practice question on ${compById(P, pr.comp).label.toLowerCase()}. Answer on the page or here: a, b or c.` });
});
registerOp('ta.j7.sample.submit', (w, a, actor) => {
  const pid = pidOf(actor); const r = submitSample(w, pid, a.comp ? String(a.comp) : undefined); if (!r) return;
  const P = personaFor(pid);
  appendQ(w, actor.id, { who: 'q', engine: 'rules', kind: 'reply', ref: { type: 'ta.assess', id: `${pid}:${r.sm.comp}` }
… [297 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -o "var(--[a-z0-9-]*)" styles/talent-b.css styles/home.css ds/ds.css | sed 's/.*var/var/' | sort | uniq -c | sort -rn | head -50; grep -n "^\.ds-tag\|^\.ds-banner\|^\.ds-opt\|^\.lab\b\|\.ds-sim" ds/ds.css | head

  <details><summary>result</summary>

```
49 var(--ink)
     33 var(--moon-2)
     25 var(--rule)
     21 var(--ink-2)
     20 var(--gold-light)
     19 var(--paper)
     19 var(--night-3)
     19 var(--moon)
     19 var(--ink-3)
     17 var(--voice)
     17 var(--data)
     14 var(--sheet)
     12 var(--wash)
     12 var(--rule-2)
     12 var(--risk)
     10 var(--gold-ink)
      9 var(--night)
      7 var(--ok)
      7 var(--night-4)
      6 var(--night-2)
      5 var(--motion-ease-out)
      5 var(--gold)
      4 var(--warn)
      4 var(--motion-quick)
      2 var(--ui)
      2 var(--shadow)
      2 var(--r-surface)
      2 var(--gold-wash)
      1 var(--thread-w)
      1 var(--ref-red-light)
      1 var(--ref-red-dark)
      1 var(--ref-paper-4)
      1 var(--ref-paper-3)
      1 var(--ref-paper-2)
      1 var(--ref-paper-1)
      1 var(--ref-paper-0)
      1 var(--ref-night-4)
      1 var(--ref-night-3)
      1 var(--ref-night-1)
      1 var(--ref-night-0)
      1 var(--ref-ink-900)
      1 var(--ref-ink-800)
      1 var(--ref-ink-700)
      1 var(--ref-ink-600)
      1 var(--ref-ink-400)
      1 var(--ref-ink-300)
      1 var(--ref-ink-100)
      1 var(--ref-green-light)
      1 var(--ref-green-dark)
      1 var(--ref-gold-800)
130:.ds-sim { font-family: var(--data); font-size: 12px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-3); border: 1px dashed var(--rule-2); border-radius: 4px; padding: 2px 8px; white-space: nowrap; }
131:.ds .ink .ds-sim { color: var(--moon-2); border-color: var(--
… [975 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; cat ds/Glyph.tsx | head -30; grep -n "\.ch-q\|\.ch \|\.ch-next\|\.ch-path" styles/home.css | head; grep -n "tb-card\b\|\.tb-card {" styles/talent-b.css | head -3; grep -n "\.ds-input\|\.ds-field\|textarea" ds/ds.css | head

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
… [2247 more characters trimmed]
```
  </details>


**Claude** · 2026-10-30 10:41

Now let me write the candidate logic module.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/logic.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/logic.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/ProofClass.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/ProofClass.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Requests.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Requests.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate; python3 - <<'E' p='Requests.tsx'; s=open(p).read() s=s.replace(" && !(d.state === 'REVIEWED' && w.q.suggestions.some((s) => s.subject === `seen:${d.id}`))","") open(p,'w').write(s) E

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Gap.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Gap.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; sed -n 1,30p ds/Switch.tsx

  <details><summary>result</summary>

```
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
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Status.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Status.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Cv.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/Cv.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate; python3 - <<'E' p='Cv.tsx'; s=open(p).read() s=s.replace("<ProofClassTag id={`lk-${e.evidenceId}`} k={proofClass(w, e)} /> {d.links","<ClassShape k={proofClass(w, e)} /> {PROOF_WORD[proofClass(w, e)]} · {d.links") s=s.repla
… [274 more characters trimmed]

  <details><summary>result</summary>

```
5:export const registerRef = (type: string, r: RefRenderer) => { refs.set(type, r); };
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/candidate.css

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate/candidate.css (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts; grep -rn "tb-seen\|tb-card\|tb-strip\|Seen by\|tb-hero" journeys/*.mjs features/*.mjs review/*.mjs 2>/dev/null | head

  <details><summary>result</summary>

```
features/contact.mjs:81:  step('Candidate sees “Seen by Kora Pay” once someone opened it', /Seen by Kora Pay/.test(await canvas(page)));
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; python3 - <<'E' p='Passport.tsx'; s=open(p).read() # imports s=s.replace("import { MediaSection } from '../media/Candidate';","""import { MediaSection } from '../media/Candidate'; // EVIDENCE-FIRST (build pack 30 Oct, item D): proof 
… [5026 more characters trimmed]

  <details><summary>result</summary>

```
17:import { CELL_LABEL, KIND, VER, cellOf, cellOn, discoveryOf, isCode, myEvidence, orgName, passportStats, reachOf, redactedOf, summaryFor, tb, verOf, viewerOrgs, checkRunning, type Cell } from './logic';
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; python3 - <<'E' p='Passport.tsx'; s=open(p).read() s=s.replace("orgName, passportStats, reachOf","orgName, reachOf") s=s.replace("""      <div className="tb-row-between"><span className="lab">{KIND[e.kind]}{e.redactedOf ? ' · redacte
… [3085 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; grep -n "tb-strip" styles/talent-b.css

  <details><summary>result</summary>

```
27:.tb-strip { margin: 0; display: grid; gap: 10px; }
28:.tb-strip-bar { display: flex; gap: 2px; height: 12px; }
29:.tb-strip-bar i { display: block; min-width: 8px; flex-basis: 0; border-radius: 2px; }
30:.tb-strip-bar i:first-child { border-radius: 4px 2px 2px 4px; }
31:.tb-strip-bar i:last-child { border-radius: 2px 4px 4px 2px; }
32:.tb-strip-bar i:only-child { border-radius: 4px; }
33:.tb-strip [data-k='VERIFIED'] { background: var(--ok); }
34:.tb-strip [data-k='WAITING'] { background: var(--gold); }
35:.tb-strip [data-k='FAILED'] { background: var(--risk); }
36:.tb-strip [data-k='OWN'] { background: var(--ref-ink-400); }
37:.tb-strip [data-k='CONFIDENTIAL'] { background: repeating-linear-gradient(135deg, var(--ink-2) 0 2px, var(--sheet) 2px 5px); box-shadow: inset 0 0 0 1px var(--ink-2); }
38:.tb-strip-key { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 14px; color: var(--ink-2); }
39:.tb-strip-key li { display: inline-flex; align-items: center; gap: 6px; }
40:.tb-strip-key i { width: 10px; height: 10px; border-radius: 3px; flex: none; }
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate; cat >> candidate.css <<'E'  /* Passport "proof at a glance" by proof class: textures in the ink family (gold stays Q's), shapes in the key. */ .tb-strip [data-k='ISSUER_VERIFIED'] { background: var(--ok); } .tb-strip [data-
… [785 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; python3 - <<'E' p='Passport.tsx'; s=open(p).read() s=s.replace("else if (query.get('media')) setTab('items');","else if (query.get('media') || query.get('cv')) setTab('items');") open(p,'w').write(s) E grep -n "query.get('cv')" Passp
… [7 more characters trimmed]

  <details><summary>result</summary>

```
46:    if (v) { setAs(v); setTab('sharing'); } else if (i) { setItem(i); setTab('items'); } else if (query.get('media') || query.get('cv')) setTab('items'); else if (t) setTab(t);
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; python3 - <<'E' p='Applications.tsx'; s=open(p).read() s=s.replace("import { CandidateRatings } from '../rubric/CandidateRatings'; // rubric builder: the person's own ratings (AD-E-14)","""import { CandidateRatings } from '../rubric/
… [1781 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/talent-b; python3 - <<'E' p='Jobs.tsx'; s=open(p).read() s=s.replace("import { JobContact } from '../contact/JobContact';","""import { JobContact } from '../contact/JobContact'; // EVIDENCE-FIRST (pack item E): hiring confirmed by a participat
… [1688 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/routes; python3 - <<'E' p='entry.tsx'; s=open(p).read() s=s.replace("import '../styles/home.css';","""import { EvidenceHomeCards, evidenceHomeLine } from '../journeys/evidence/candidate/Requests'; import '../styles/home.css';""",1) s=s.replace("""  con
… [647 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; python3 - <<'E' p='journeys/evidence/candidate/Requests.tsx'; s=open(p).read() s=s.replace("""export function EvidenceHomeCards() {""","""export function EvidenceHomeCards({ part = 'asks' }: { part?: 'asks' | 'grow' }) {""") s=s.replace("""  const req
… [789 more characters trimmed]

  <details><summary>result</summary>

```
191:/** Home block: requests waiting on the person, interest checks, and J7's answer to a verified gap. */
199:  const gap = false;
200:  if (!reqs.length && !asks.length && !gap) return null;
205:      {gap && <GapCard pid={pid} />}
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate; python3 - <<'E' p='Requests.tsx'; s=open(p).read() s=s.replace("  const gap = false;\n","").replace("if (!reqs.length && !asks.length && !gap) return null;","if (!reqs.length && !asks.length) return null;").replace("      {
… [133 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/skills/evidence-candidate.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/skills/evidence-candidate.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; sed -i '/_evcSkills/d' src/q/skills/evidence-candidate.ts; sed -i "s/import { emit, now, type World } from '..\/..\/mock\/world';/import { emit, now } from '..\/..\/mock\/world';/" src/q/skills/evidence-candidate.ts; npx tsc --noEmit -p . | head

  <details><summary>result</summary>

```
src/q/skills/evidence-candidate.ts(124,12): error TS6133: 'c' is declared but its value is never read.
src/q/skills/evidence-candidate.ts(129,12): error TS6133: 'c' is declared but its value is never read.
[This command modified 1 file you've previously read: src/q/skills/evidence-candidate.ts. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; sed -i '124s/handle: (c) =>/handle: () =>/;129s/handle: (c) =>/handle: () =>/' src/q/skills/evidence-candidate.ts; npx tsc --noEmit -p . | head

  <details><summary>result</summary>

```
[This command modified 3 files you've previously read: ../journeys/J12-EVIDENCE-FIRST.md, src/q/skills/evidence-candidate.ts, ../../../../../tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/vite.log. Call Read before editing.]
```
  </details>


**Claude** · 2026-10-30 10:54

Noted on the lead's change to `state/areas/talent-b.ts`: I'm not editing that file, so the line stays. Let me check the sed edit landed on the right lines.

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; sed -n 120,131p src/q/skills/evidence-candidate.ts | cut -c1-120

  <details><summary>result</summary>

```
});
registerSkill({
  id: 'evc.cv.add', side: 'candidate',
  match: (c) => (cand(c) && CV.test(c.norm) && /\b(add|put|include|say|claim)\b/.test(c.norm) && /(skill|certif|qualif|d
  handle: () => ({ msgs: [reply('I won’t add something to your CV that isn’t already in your CV, your profile or you
});
registerSkill({
  id: 'evc.cv.doubt', side: 'candidate',
  match: (c) => (cand(c) && (CV.test(c.norm) || /\bclaim/.test(c.norm)) && /\b(lie|lying|liar|untrue|fake|believe|trust|
  handle: () => ({ msgs: [reply('No. I never call a CV untrue, and neither does Talent Q. Every CV line is read as a cla
    used: ['How Talent Q labels evidence'], actions: [{ label: 'What do the labels mean?', act: { t: 'say', text: 'what 
  })] }),
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/q/proactive/evidence-candidate.ts

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/q/proactive/evidence-candidate.ts (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; npx tsc --noEmit -p . | head

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts; sed -n 80,140p features/media.mjs | grep -n "update\|__tqQA" | head; grep -rn "__tqQA.update" features/*.mjs review/*.mjs | head -5

  <details><summary>result</summary>

```
features/campaigns.mjs:28:    try { if ((await page.evaluate(() => window.__tqQA.getWorld().session.actor)) !== id) { await page.evaluate((id) => window.__tqQA.update((w) => { w.session.actor = id; }), id); await sleep(500); } break; }
features/campaigns.mjs:70:  await page.evaluate(() => window.__tqQA.update((w) => { w.threads.push({ id: 't_j11_tobi', orgId: 'org_kora', personId: 'p_tobi', mandateId: 'm_backend', campaignId: 'c_q4_eng', initiatedBy: 'CANDIDATE', state: 'OPEN', messages: [{ id: 'mj11', from: 'p_tobi', to: 'org_kora', body: 'Hello, is the on-call rota real for this role, and how often would I be on call?', at: '2026-10-29T08:40:00+01:00', status: 'RECEIVED', channel: 'IN_APP' }] }); }));
features/campaigns.mjs:93:  await page.evaluate(() => window.__tqQA.update((w) => {
features/campaigns.mjs:154:  await page.evaluate(() => window.__tqQA.update((w) => { w.session.offsetDays = 45; })); await sleep(500);
features/campaigns.mjs:157:  await page.evaluate(() => window.__tqQA.update((w) => { w.session.offsetDays = 0; })); await sleep(300);
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/qa/scripts/features/evidence-candidate.mjs

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/qa/scripts/features/evidence-candidate.mjs (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; BASE=http://localhost:5197/ timeout 600 node qa/scripts/features/evidence-candidate.mjs d 2>&1 | tail -70

  <details><summary>result</summary>

```
PASS [d] every Passport item carries the proof class the recruiter model gives it, in the same words · CLAIM,SELF_REPORTED,SELF_REPORTED
PASS [d] Seyi’s CV claim is labelled “Claim”; the 2019 certificate and the described project are “Self-reported”
PASS [d] only the five shared words are used as labels · Claim
?
· what this means | Self-reported
?
· what this means | Self-reported
?
· what this means | Claim
?
· what this means
PASS [d] a label explains itself on demand
PASS [d] certificate shows its source and age in words (“seven years old”) · CERTIFICATE · MAR 2019 … Check pending Self-reported ? · what this means PostgreSQL Associate certificate (2019)  An entry-level Postgres certificate, if the is
PASS [d] reuse scope is stated: Kora only, not reused for other employers unless he chooses
PASS [d] his CV is shown as his own words, labelled as a claim, with a calm Q line (no judgement) · Your CV, as you wrote it
Claim
?
· what this means

Your CV names 5 of the 5 things Kora Pay is looking for. Every CV line is read as a claim, for everyone, and that isn’t doubt about yours. A reviewe
PASS [d] no sideways scroll: passport (Seyi)
PASS [d] home: Q’s first line names the request, with the effort and that no is fine
PASS [d] request card: what (from the bounded sample), why, effort in minutes · KORA PAY · SENIOR BACKEND ENGINEER Waiting for you Kora Pay would like to see one piece of your postgres at scale work WHAT Find and fix one slow query on a copy of a real table. WHY 
… [3231 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; python3 - <<'E' p='prototype/src/journeys/evidence/candidate/ProofClass.tsx'; s=open(p).read() s=s.replace("""<b>{PROOF_WORD[k]}</b>{extra ? <span className="evc-pc-extra">, {extra}</span> : null}""","""<b>{PROOF_WORD[k]}{extra ? <span className="evc-pc-extra">, {e
… [902 more characters trimmed]

  <details><summary>result</summary>

```
44:.evc-pc-extra { color: var(--ink-2); }
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; sed -i 's/.evc-pc-extra { color: var(--ink-2); }/.evc-pc-extra { color: var(--ink-2); font-weight: 400; }/' prototype/src/journeys/evidence/candidate/candidate.css; BASE=http://localhost:5197/ timeout 600 node qa/scripts/features/evidence-candidate.mjs d 2>&1 | gre
… [23 more characters trimmed]

  <details><summary>result</summary>

```
?
· what this means | Self-reported
?
· what this means | Self-reported
?
· what this means | Claim
?
· what this means
Claim
?
· what this means

Your CV names 5 of the 5 things Kora Pay is looking for. Every CV line is read as a claim, for everyone, and that isn’t doubt about yours. A reviewe
FAIL [d] the draft shows the wording diff and marks what Q won’t add

61/62 passed
[This command modified 2 files you've previously read: src/journeys/evidence/candidate/candidate.css, ../../../../../tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/vite.log. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; sed -i 's#/Q won’t add/.test(dT)#/Q won’t add/i.test(dT)#' qa/scripts/features/evidence-candidate.mjs; BASE=http://localhost:5197/ timeout 900 node qa/scripts/features/evidence-candidate.mjs 2>&1 | grep -E "^FAIL|passed|errors|  " | tail -30

  <details><summary>result</summary>

```
PASS [d] certificate shows its source and age in words (“seven years old”) · CERTIFICATE · MAR 2019 … Check pending Self-reported ? · what this means PostgreSQL Associate certificate (2019)  An entry-level Postgres certificate, if the is
PASS [d] after Ada’s review: outcome shown, the class is now Assessed · KORA PAY · SENIOR BACKEND ENGINEER Reviewed Your postgres at scale sample for Kora Pay Assessed, partial ? · what this means  Shows part of it. It now counts as reviewed work for this role.  “Found th
PASS [d] Seyi’s application: “Next update by Mon 2 Nov · Ada Okafor, Kora Pay” · KORA PAY Sent Senior Backend Engineer  Delivered. Kora Pay hasn’t opened it, as far as Talent Q can see.  Next update by Mon 2 Nov · Ada Okafor, Kora Pay  First review of your application. Kora Pay co
PASS [d] J7 card: on-call leadership is only partly shown for Kora’s role · Q · PRIVATE TO YOU Partly shown On-call leadership is only partly shown for Kora Pay’s Senior Backend Engineer role  What Kora Pay sees: Debugging sample. Worked a real incident, but a sample, not an 
PASS [d] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
PASS [m] certificate shows its source and age in words (“seven years old”) · CERTIFICATE · MAR 2019 … Check pending Self-reporte
… [1386 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/captures; mkdir -p review/pairs/evidence-candidate/before; cp features/evidence-candidate/*.png review/pairs/evidence-candidate/before/; ls features/evidence-candidate | head -40

  <details><summary>result</summary>

```
d-01-passport-seyi.png
d-02-home-request.png
d-03-sample-panel.png
d-04-submitted.png
d-05-passport-waiting.png
d-06-reviewed.png
d-07-decline-form.png
d-08-declined.png
d-09-applications-seyi.png
d-10-cv-draft.png
d-11-jobs.png
d-12-home-tobi.png
d-13-interest-confirmed.png
d-14-revoked-card.png
d-15-preview-after.png
d-16-zara-overdue.png
m-01-passport-seyi.png
m-02-home-request.png
m-03-sample-panel.png
m-04-submitted.png
m-05-passport-waiting.png
m-06-reviewed.png
m-07-decline-form.png
m-08-declined.png
m-09-applications-seyi.png
m-10-cv-draft.png
m-11-jobs.png
m-12-home-tobi.png
m-13-interest-confirmed.png
m-14-revoked-card.png
m-15-preview-after.png
m-16-zara-overdue.png
```
  </details>


**Claude** · 2026-10-30 10:59

Now the design-critique skill on the rendered screens.

- 🔧 `Skill`: {"skill": "design-skills:design-critique", "args": "Critique rendered captures of Talent Q candidate evidence-first screens (Passport with proof classes and CV, home with request card, sample panel, a

  <details><summary>result</summary>

```
Launching skill: design-skills:design-critique
```
  </details>


**User** · 2026-10-30 10:59

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
… [3108 more characters trimmed]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/features/evidence-candidate/d-02-home-request.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/features/evidence-candidate/m-02-home-request.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/features/evidence-candidate/d-01-passport-seyi.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 10:59

[Image: original 1440x2904, displayed at 992x2000. Multiply coordinates by 1.45 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/features/evidence-candidate/m-10-cv-draft.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 11:00

[Image: original 780x12938, displayed at 121x2000. Multiply coordinates by 6.45 to map to original image.]

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/captures/features/evidence-candidate; python3 -c " from PIL import Image im=Image.open('m-10-cv-draft.png'); print(im.size) im.crop((0,1500,780,3900)).save('/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/m10a.png') im=Image.open('d-10-c
… [154 more characters trimmed]

  <details><summary>result</summary>

```
(780, 12938)
(1440, 4948)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/m10a.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 11:00

[Image: original 780x2400, displayed at 650x2000. Multiply coordinates by 1.20 to map to original image.]

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate; grep -n "diff\|evc-diffline" Cv.tsx | head -20

  <details><summary>result</summary>

```
2:// stronger": a clearer draft that restructures and rewords, shows the wording diff, marks what Q won't add, can link
29:/** Word-level diff (LCS) so the candidate sees exactly which words changed. */
30:function diff(a: string, b: string): Tok[] {
71:      <ol className="evc-diff">
74:            <p className="evc-diffline">{diff(l.before, l.after.join(' ')).map((t, k) => <span key={k} className={t.k === 'del' ? 'evc-del' : t.k === 'add' ? 'evc-add' : undefined}>{t.k === 'del' ? <span className="sr">removed: </span> : t.k === 'add' ? <span className="sr">added: </span> : null}{t.t} </span>)}</p>
75:            {!compact && <p className="evc-diffmeta t14"><b>{CHANGE[l.change]}</b>{l.after.length > 1 ? ` · ${l.after.length} lines` : ''}{l.from ? ` · from ${l.from.toLowerCase()}` : ''}{l.note ? ` · ${l.note}` : ''}</p>}
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src/journeys/evidence/candidate; python3 - <<'E' p='Cv.tsx'; s=open(p).read() a=s.index("type Tok = "); b=s.index("const CHANGE") s=s[:a]+'''/** Marks words that exist on only one side, so "Now" highlights Q's words and "Was" strikes the words Q took out. 
… [2362 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts; grep -n "Not checked\|'Verified'\|Check pending\|Check failed" journeys/T3.mjs journeys/T5.mjs journeys/T1.mjs journeys/T4.mjs | head

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; python3 - <<'E' p='journeys/talent-b/Passport.tsx'; s=open(p).read() old='''      <div className="tb-row-between"><span className="lab">{KIND[e.kind]}{e.redactedOf ? ' · redacted' : ''} · {month(e.observedAt)}</span>{running ? <span className="ds-tag"
… [2738 more characters trimmed]

  <details><summary>result</summary>

```
journeys/evidence/candidate/Cv.tsx:30:const norm = (t: string) => t.toLowerCase().replace(/[^\p{L}\p{N}%]/gu, '');
journeys/evidence/candidate/Cv.tsx:72:            {!compact && <p className="evc-diffmeta t14"><b>{CHANGE[l.change]}</b>{l.after.length > 1 ? ` · ${l.after.length} lines` : ''}{l.from ? ` · from ${l.from.toLowerCase()}` : ''}{l.note ? ` · ${l.note}` : ''}</p>}
journeys/evidence/candidate/Status.tsx:40:      <p><b>Update overdue</b> · {org} said they’d update you by {weekdayDate(c.nextUpdateDue)} about “{c.milestone.toLowerCase()}”. That date has passed{c.days ? ` (${c.days} ${c.days === 1 ? 'day' : 'days'} ago)` : ''} and nothing has come yet.</p>
q/proactive/evidence-candidate.ts:20:    text: `${orgNm(w, d.orgId)} reviewed your ${reqLabel(w, d.reqId)} sample: ${r!.word.toLowerCase()}. They shared the reviewer’s note with you.`,
q/proactive/evidence-candidate.ts:41:    why: `${orgNm(w, c!.orgId)} committed to “${c!.milestone.toLowerCase()}” by that date.`,
q/skills/evidence-candidate.ts:151:    return { msgs: [reply(`${org} would like one short piece of work: ${BOUNDED_SAMPLE[d.reqId]?.task.toLowerCase() ?? reqLabel(c.w, d.reqId)}, about ${d.effortMinutes ?? 40} minutes. ${whyAsked(c.w, d)} It’s your choice: do it, offer work you already have, or decline. Declining is recorded as declined, not as a fail.`, {
q/skills/evidence-candidate.ts:203:    const lines = rows.map((x) => x.late ? `${orgNm(c.w, x.orgId)} said they’d update you by ${weekdayDate(x.nextUpdateDue
… [537 more characters trimmed]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; sed -i 's#/Kora Pay would like to see one piece of your postgres at scale work/i#/Kora Pay would like to see one piece of your work on Postgres at scale/#' qa/scripts/features/evidence-candidate.mjs; BASE=http://localhost:5197/ timeout 900 node qa/scripts/features/
… [74 more characters trimmed]

  <details><summary>result</summary>

```
PASS [d] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
PASS [m] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
124/124 passed
[This command modified 1 file you've previously read: ../qa/scripts/features/evidence-candidate.mjs. Call Read before editing.]
```
  </details>


**Claude** · 2026-10-30 11:03

Let me look at more captures: the sample panel, jobs, Tobi's home, Zara, and the reviewed state.

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/captures/features/evidence-candidate; S=/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad; python3 -c " from PIL import Image for n,box in [('d-03-sample-panel.png',(612,0,1440,1300)),('d-11-jobs.png',(612,0,1440,1400)),('d-12-home-tobi.pn
… [267 more characters trimmed]
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/c-d-03-sample-panel.png
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/c-d-12-home-tobi.png
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/c-d-11-jobs.png
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/c-m-16-zara-overdue.png
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/c-m-01-passport-seyi.png

  <details><summary>result</summary>

```
R1.log
R3.log
R5.log
T1.log
T2.log
T3.log
T4.log
T5.log
a1
a2
a3
a4
a5.png
afr.png
after-states
appdist
appdist2
ask.mjs
ask.png
atlas.txt
axe
axe-all.json
axe-b1.txt
axe-d.txt
axe.mjs
b1
b1f
b1s
base
base-dist
base-http.log
batch-R1.log
batch-R2.log
batch-R3.log
batch-R4.log
batch-R5.log
batch-T4.log
batch.files
batch.sh
batch2.sh
before-cx
before-extra
before-now
before-r3
bin
boot.mjs
bsheet.png
c-d-03-sample-panel.png
c-d-06-reviewed.png
c-d-11-jobs.png
c-d-12-home-tobi.png
c-m-01-passport-seyi.png
c-m-16-zara-overdue.png
camp.log
campaigns
cap
cap.mjs
ch
check.mjs
chk
clips
clips2
csheet.png
cur
cx2
d04-first.png
d05-first.png
d06-first.png
d08-first.png
d10a.png
d3.png
dbg.mjs
dfinal
dir1
dir2
dirs
dom.mjs
dshots
ef0
efprobe.mjs
em3.log
email
err.mjs
fb3.png
ff
ff2
files-a.json
files-b.json
files-c.json
film
film.log
film2.log
film2.txt
filmout
fin2
fin3
final
final3
finalcap
finalcap2
fixmo.mjs
flow.mjs
flow2.mjs
fr-f2-onboarding-desktop-0.35.png
fr-f2-onboarding-desktop-0.7.png
fr-f6-multi-agent-desktop-0.35.png
fr-f6-multi-agent-desktop-0.7.png
fr-j7-desktop-0.35.png
fr-j7-desktop-0.7.png
frames
frames-b1.png
fulldist
fulldist2
g-app.png
g-d-pairs.png
g-d-screens.png
g-d-top.png
g-d.jpg
g-m-pairs.png
g-m-screens.png
g-m-top.png
g-m.jpg
gallery
gallery-src
gallery2
gcheck.mjs
goal.txt
gpt
headdist
hirea-dp
hirea.files
hooktest.mjs
ht
ift
insp.png
int1
iv.mjs
iv3.png
j11-d.jpg
j11-m.jpg
j11b.log
j11film
j11rec
j11rec.log
j3.log
lead
leaddist
m02a.png
m05-first.png
m06-
… [1314 more characters trimmed]
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


**User** · 2026-10-30 11:03

[Image: original 780x3200, displayed at 488x2000. Multiply coordinates by 1.60 to map to original image.]


  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 11:03

[Image: original 780x2600, displayed at 600x2000. Multiply coordinates by 1.30 to map to original image.]

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; python3 - <<'E' p='journeys/evidence/candidate/Cv.tsx'; s=open(p).read() old='''      {!draft && <ol className="evc-cvdoc" aria-label="Your CV">{cv.lines.map((l, i) => <li key={i}>{l}</li>)}</ol>}''' assert old in s s=s.replace(old,'''      {!draft &&
… [1116 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; BASE=http://localhost:5197/ timeout 900 node qa/scripts/features/evidence-candidate.mjs 2>&1 | grep -E "^FAIL|passed|errors|^  " | tail; cd captures; mkdir -p review/pairs/evidence-candidate/after; cp features/evidence-candidate/*.png review/pairs/evidence-candidat
… [8 more characters trimmed]

  <details><summary>result</summary>

```
PASS [d] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
PASS [m] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
124/124 passed
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/captures/features/evidence-candidate; S=/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad; python3 -c " from PIL import Image im=Image.open('d-05-passport-waiting.png'); print(im.size); im.crop((612,0,1440,min(2400,im.size[1]))).save('$S/a
… [111 more characters trimmed]
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a-d05.png
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a-m10.png

  <details><summary>result</summary>

```
(1440, 3769)
(780, 12458)
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 11:05

[Image: original 828x2400, displayed at 690x2000. Multiply coordinates by 1.20 to map to original image.]


  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-30 11:05

[Image: original 780x2400, displayed at 650x2000. Multiply coordinates by 1.20 to map to original image.]

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype/src; python3 - <<'E' p='journeys/talent-b/Passport.tsx'; s=open(p).read() s=s.replace("(e.confidential || ['PENDING', 'FAILED', 'UNDER_REVIEW'].includes(v)) ? <VerTag e={e} /> : null}","(e.confidential || (['PENDING', 'FAILED', 'UNDER_REVIEW'].includes(v) 
… [432 more characters trimmed]

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/qa/scripts/journeys; S=/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/evc; mkdir -p $S; B=http://localhost:5197/ (BASE=$B timeout 1200 node T1.mjs > $S/T1.log 2>&1; echo T1 $? >> $S/done) & (BASE=$B timeout 1200 node T3.mjs > $S/T3.log 
… [307 more characters trimmed]

  <details><summary>result</summary>

```
[1]   Done                    ( BASE=$B timeout 1200 node T1.mjs > $S/T1.log 2>&1; echo T1 $? >> $S/done )
[2]   Done                    ( BASE=$B timeout 1200 node T3.mjs > $S/T3.log 2>&1; echo T3 $? >> $S/done )
[3]-  Done                    ( timeout 1200 node T4.mjs $B > $S/T4.log 2>&1; echo T4 $? >> $S/done )
[4]+  Done                    ( BASE=$B timeout 1200 node T5.mjs > $S/T5.log 2>&1; echo T5 $? >> $S/done )
T5 0
T4 0
T3 0
T1 0
T1 pass=76 fail=0
T3 pass=54 fail=0
T4 pass=43 fail=0
T5 pass=52 fail=0
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; BASE=http://localhost:5197/ timeout 900 node qa/scripts/features/evidence-candidate.mjs 2>&1 | grep -E "^FAIL|passed|errors" ; cp captures/features/evidence-candidate/*.png captures/review/pairs/evidence-candidate/after/; head -5 qa/scripts/review/privacy.mjs | gre
… [10 more characters trimmed]

  <details><summary>result</summary>

```
PASS [d] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
PASS [m] Zara: Kora’s overdue update shown honestly (date passed, late on their side, owner named) · KORA PAY Viewed Senior Backend Engineer  Someone at Kora Pay opened it on 27 Oct. That’s all “viewed” means: it isn’t a shortlist or a decision.  Update overdue · Kora Pay said they’d update you by We
124/124 passed
// profiles, Q's tools, cached views and downstream artifacts (campaigns). Usage: node privacy.mjs [base]
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design; timeout 600 node qa/scripts/review/privacy.mjs http://localhost:5197/ 2>&1 | tail -5

  <details><summary>result</summary>

```
PASS search results cache no longer shows Dayo
PASS saved comparison no longer shows Dayo
PASS Zara withdrew from Kora: nothing visible despite her application
PASS no page errors
All privacy checks passed
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/evidence-candidate.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/evidence-candidate.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: cd /home/user/neo/talent-q-design/prototype; npx tsc --noEmit -p . && echo TSC-CLEAN; git status --short | head -40

  <details><summary>result</summary>

```
TSC-CLEAN
 M ../captures/cx/J11/d-01-briefing.png
 M ../captures/cx/J11/d-02-contact-policy.png
 M ../captures/cx/J11/d-03-filed.png
 M ../captures/cx/J11/d-04-campaign.png
 M ../captures/cx/J11/d-06-rubric-approved.png
 M ../captures/cx/J11/d-07-consent.png
 M ../captures/cx/J11/d-08-unsafe-link.png
 M ../captures/cx/J11/d-09-upload-paused.png
 M ../captures/cx/J11/d-10-shared.png
 M ../captures/cx/J11/d-11-evidence-report.png
 M ../captures/cx/J11/d-12-reviewed.png
 M ../captures/cx/J11/d-14-approval.png
 M ../captures/cx/J11/d-15-auth-expired.png
 M ../captures/cx/J11/d-17-candidate-reply.png
 M ../captures/cx/J11/d-18-reply-intelligence.png
 M ../captures/cx/J11/d-19-booked.png
 M ../captures/cx/J11/m-01-briefing.png
 M ../captures/cx/J11/m-02-contact-policy.png
 M ../captures/cx/J11/m-04-campaign.png
 M ../captures/cx/J11/m-07-consent.png
 M ../captures/cx/J11/m-08-unsafe-link.png
 M ../captures/cx/J11/m-09-upload-paused.png
 M ../captures/cx/J11/m-10-shared.png
 M ../captures/cx/J11/m-14-approval.png
 M ../captures/cx/J11/m-18-reply-intelligence.png
 M ../captures/cx/J11/m-19-booked.png
 M ../captures/cx/R2/d-01-compare-payments-go.png
 M ../captures/cx/R2/d-02-challenge.png
 M ../captures/cx/R2/d-03-corrected-equal.png
 M ../captures/cx/R2/d-04-profile-tobi.png
 M ../captures/cx/R2/d-05-profile-viewer-outage.png
 M ../captures/cx/R2/d-06-profile-viewer-site.png
 M ../captures/cx/R2/d-07-after-invitation.png
 M ../captures/cx/R2/d-08-compare-last-year.png
 M ../captures
… [259 more characters trimmed]
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The candidate side of J12 is built: steps 6, 7, 10, 12, the candidate half of 13, and P6. My new feature test passes 124/124 (62 phone, 62 desktop), T1, T3, T4 and T5 still pass against m

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
