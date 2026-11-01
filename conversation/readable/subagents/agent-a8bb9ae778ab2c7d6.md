# Helper agent agent-a8bb9ae778ab2c7d6: Design pass R2 pages

Source: `agent-a8bb9ae778ab2c7d6.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 12:20

Run the design pass for area `hire-b` (journey R2 Ada, a non-technical recruiter hiring technical people) in /home/user/neo/talent-q-design/prototype.

First read /home/user/neo/talent-q-design/journeys/DESIGN-PASS-BRIEF.md and follow it exactly, including loading the named skills with the Skill tool and applying them. Also read /home/user/neo/talent-q-design/journeys/BUILD-BRIEF.md for the contracts and your file ownership. You own the same `hire-b` files as before.

Your dev server port is 5182. Use `npx vite --port 5182 --strictPort`, and don't run `npm run build`.

Your pages:
- `/r/people/:id`: the candidate profile, evidence presentation, the safe project viewer, GitHub outage and cached states, and the permission and withdrawn states. The lead already made the title the person's name, with Q's evidence summary as a lede. Refine that.
- `/r/compare`: the comparison ledger. Use the `dataviz` skill seriously here. The marks, criteria, weighting and "what changed" notes must be understandable to a non-technical recruiter at a glance.
- `/r/interviews` and `/r/interviews/:id`: the live copilot with rubric and follow-ups, and the feedback form.
- Every Q reply card your skills produce.

Interview and assessment interfaces and evidence presentation are founder priorities. Make them excellent on desktop and phone.

R2.mjs must keep passing. Also run qa/scripts/review/privacy.mjs against your server.

- 🔧 `Bash`: Read design pass brief

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
… [3818 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read build brief and status

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
… [7362 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Locate hire-b owned files

  <details><summary>result</summary>

```
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

src/state/seeds:
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
    424 src/q/skills/hire-b.ts
     52 src/q/proactive/hire-b.ts
wc: src/journeys/hire-b: Is a directory
      0 src/journeys/hire-b
     63 src/styles/hire-b.css
     25 src/state/seeds/hire-b.ts
     36 src/state/areas/hire-b.ts
     13 src/routes/hire-b.tsx
    613 total
```
  </details>

- 🔧 `Bash`: Show hire-b journey files

  <details><summary>result</summary>

```
69 src/journeys/hire-b/projects.ts
  160 src/journeys/hire-b/Profile.tsx
   98 src/journeys/hire-b/ProjectViewer.tsx
  230 src/journeys/hire-b/model.ts
  139 src/journeys/hire-b/ops.ts
   26 src/journeys/hire-b/ui.tsx
  166 src/journeys/hire-b/Interviews.tsx
  888 total
// Routes for R2 (Ada). Owned by this area (see journeys/BUILD-BRIEF.md).
import { registerRoute } from './registry';
import { OrgOnly } from './guard';
import { Compare } from '../screens/Compare';
import { Profile } from '../journeys/hire-b/Profile';
import { Interviews, InterviewRoom } from '../journeys/hire-b/Interviews';
import '../journeys/hire-b/ops';
import '../styles/hire-b.css';

registerRoute({ path: '/r/compare', side: 'recruiter', label: 'the comparison', render: () => <OrgOnly orgId="org_kora" what="Kora Pay’s hiring"><Compare /></OrgOnly>, nav: { group: 'Hiring', label: 'Compare', icon: 'people', order: 14, orgKind: 'EMPLOYER', orgIds: ['org_kora'] } });
registerRoute({ path: '/r/people/:id', side: 'recruiter', label: 'a candidate profile', render: (p) => <Profile key={p.id} id={p.id} /> });
registerRoute({ path: '/r/interviews', side: 'recruiter', label: 'interviews', render: () => <Interviews />, nav: { group: 'Hiring', label: 'Interviews', icon: 'interview', order: 16, orgKind: 'EMPLOYER' } });
registerRoute({ path: '/r/interviews/:id', side: 'recruiter', label: 'the interview', render: (p) => <InterviewRoom key={p.id} id={p.id} /> });
/* R2 (Ada) pages: candidate profile, safe project viewer
… [10306 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find hire-b ownership details

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Search ownership and Compare history

  <details><summary>result</summary>

```
8:| Recruiter | **Ada Okafor** | Talent partner at Kora Pay, not technical · R2 |
56:### R2: The non-technical technical recruiter (Ada)
d441e1a R2 (Ada): candidate profile with provenance and safe project viewer, criteria comparison, assessments, interview copilot and feedback
0b4d78e Talent Q design workspace: tokens, typed contracts, mock Q runtime, 12 priority screens connected
CalendarSetup.tsx
Career.tsx
Compare.tsx
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
131 src/screens/Compare.tsx
```
  </details>

- 🔧 `Bash`: Show R2 commit file list and journey

  <details><summary>result</summary>

```
commit d441e1a7e8a7ea7d7503836fdda0390fe17830dd
Author: Claude <noreply@anthropic.com>
Date:   Thu Oct 29 09:21:15 2026 +0000

    R2 (Ada): candidate profile with provenance and safe project viewer, criteria comparison, assessments, interview copilot and feedback
    
    - /r/people/:id, /r/interviews, /r/interviews/:id; Compare rebuilt in Direction D without its own conversation
    - 13 Q skills and 3 proactive rules; curveballs: criteria change, challenge to Q, GitHub outage,
      weak evidence, disputed assessment, consent withdrawn (R2.mjs: 74/74 steps, desktop and phone)
    - labelFor falls back to registered route labels and names interviews
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_017VXjy49wegbhYVM8d4ZvYb

 .../captures/cx/R2/d-01-compare-payments-go.png    | Bin 0 -> 284031 bytes
 talent-q-design/captures/cx/R2/d-02-challenge.png  | Bin 0 -> 309206 bytes
 .../captures/cx/R2/d-03-corrected-equal.png        | Bin 0 -> 275395 bytes
 .../captures/cx/R2/d-04-profile-tobi.png           | Bin 0 -> 310363 bytes
 .../captures/cx/R2/d-05-profile-viewer-outage.png  | Bin 0 -> 303401 bytes
 .../captures/cx/R2/d-06-profile-viewer-site.png    | Bin 0 -> 287932 bytes
 .../captures/cx/R2/d-07-after-invitation.png       | Bin 0 -> 264540 bytes
 .../captures/cx/R2/d-08-compare-last-year.png      | Bin 0 -> 277917 bytes
 .../captures/cx/R2/d-09-compare-dispute.png        | Bin 0 -> 258499 bytes
 .../captures
… [4173 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:20

Now load the skills as mandated.

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

- 🔧 `Bash`: Read dataviz form reference

  <details><summary>result</summary>

```
119 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/anti-patterns.md
   55 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/choosing-a-form.md
  139 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/color-formula.md
   37 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/components.md
   60 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/interaction.md
   96 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/marks-and-anatomy.md
  198 /tmp/claude-0/bundled-skills/2.1.312/a705954bb982e986ec0effc9ba3caa5b/dataviz/references/palette.md
  704 total
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

## The job
… [2373 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read anti-patterns, marks, interaction

  <details><summary>result</summary>

```
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
Why: indistinguishable from an existing slot under CVD; breaks the order check.
Good: Fold the tail into "Other," facet into small multiples, or use composite encoding.

**Bad: Eyeballing colorblind-safety.** "These look different enough."
Good: Run `scripts/validate_palette.js`. Adjacent Delta E >= 8 (OKLab ×100), or 6-8 WITH secondary encoding.

**Bad: A value-ramp on nominal categories.** Coloring each bar darker-where-bigger
when the categories have no natural order (products, teams, endpoints).
Wh
… [14486 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read motion tokens and atlas

  <details><summary>result</summary>

```
// Motion tokens (interaction-design skill: feedback 100–200 ms, orientation 200–400 ms, enter slower than
// exit, decelerate in / accelerate out, nothing functional over 500 ms). Every animation in the shell and
// shared components takes its timing from here; reduced motion is handled globally by MotionConfig.
export const DUR = { fast: 0.1, normal: 0.2, slow: 0.3 } as const;
export const EASE = { standard: [0.2, 0, 0, 1], enter: [0, 0, 0.2, 1], exit: [0.4, 0, 1, 1] } as const;
/** Something new arriving in place (a message, a card, a page): rise 6 px and fade in. */
export const arrive = { initial: { opacity: 0, y: 6 }, animate: { opacity: 1, y: 0, transition: { duration: DUR.normal, ease: EASE.enter } }, exit: { opacity: 0, transition: { duration: DUR.fast, ease: EASE.exit } } } as const;
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
MOTION-COVERAGE.csv
STATE-MACHINES.md
```
  </details>

- 🔧 `Bash`: Find relevant motion requirements

  <details><summary>result</summary>

```
motion_id,name,event_trigger,primary_surface,reduced_motion_fallback,status,route,evidence,note
MO-001,Q orb idle,app:idle,Q Home and interview,Static gold icon,PROTOTYPED,/r/home,,Driven by a real state or run event; reduced-motion handled by MotionConfig/CSS. Dedicated clip not recorded yet.
MO-002,Q listens,voice:recording,Voice interview,Listening text and transcript,PROTOTYPED,/gallery/states,prototype/src/ds/QMark.tsx (listening mood: core grows with input level); prototype/src/journeys/gallery/StatesGallery.tsx (Q moods),"Listening mood exists in the Q mark and is shown as a live specimen. Not yet driven by the microphone in the rebuilt /c/interview, whose mic button changes label and colour without motion. Re-pointed from /c/interview."
motion_id,name,event_trigger,primary_surface,reduced_motion_fallback,status,route,evidence,note
MO-001,Q orb idle,app:idle,Q Home and interview,Static gold icon,PROTOTYPED,/r/home,,Driven by a real state or run event; reduced-motion handled by MotionConfig/CSS. Dedicated clip not recorded yet.
MO-002,Q listens,voice:recording,Voice interview,Listening text and transcript,PROTOTYPED,/gallery/states,prototype/src/ds/QMark.tsx (listening mood: core grows with input level); prototype/src/journeys/gallery/StatesGallery.tsx (Q moods),"Listening mood exists in the Q mark and is shown as a live specimen. Not yet driven by the microphone in the rebuilt /c/interview, whose mic button changes label and colour without motion. Re-pointed from /c/in
… [3076 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read model and ui helpers
- 🔧 `Bash`: Read Profile and ProjectViewer
- 🔧 `Bash`: Read Compare and Interviews

  <details><summary>result</summary>

```
// Candidate profile for recruiters (R2): only what the person shared with the viewer's organisation,
// with provenance per item, their place in the pipeline, a safe project viewer, and how Q would check
// each requirement. Confidential items show that they exist, never their contents.
import { useEffect, useRef } from 'react';
import { actorOf, canSeeCandidate, useWorld, visibleEvidence } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { Glyph } from '../../ds/Glyph';
import { Link } from '../../ui/router';
import { runAction } from '../../q/core/engine';
import { STAGES, STAGE_LABEL } from '../../state/domain';
import { hireB } from '../../state/areas/hire-b';
import { assessFor, cellFor, firstName, KORA_ROLE, questionsFor, reqsOf, viewerOrg, visibleIds } from './model';
import { markSeen } from './ops';
import { ProjectViewer } from './ProjectViewer';
import { KIND, LevelMark, ORIGIN, VerTag, fmtDate, verOf } from './ui';

export function Profile({ id }: { id: string }) {
  const w = useWorld((x) => x);
  const me = actorOf(w);
  const person = w.people.find((p) => p.personId === id);
  const org = viewerOrg(w);
  const orgName = w.orgs.find((o) => o.id === org)?.name ?? 'your organisation';
  const prevSeen = useRef<{ at: string; items: string[] } | null | undefined>(undefined);
  if (prevSeen.current === undefined) prevSeen.current = hireB(w).seen[me.id]?.[id] ?? null;
  useEffect(() => { if (person) markSeen(id); }, [id, person, w.evidence
… [17407 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
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
  r3: /\b(postgres\w*|sql|databases?|db|queries|query)\b/,
  r4: /\b(on-?call|oncall|incidents?|outages?|post-?mortems?)\b/,
  r5: /\b(mentor\w*|coach\w*|juniors?)\b/,
};
/** Strip phrases where "g
… [21879 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// SC-041 Compare candidates, SC-039 Evidence inspector, SC-040 Role-fit explanation (rebuilt for R2).
// Requirement by requirement, never one score. Ada chooses the people and the criteria (by clicking or by
// telling Q); Q's margin notes are rewritten from state whenever anything changes. The global Q thread is
// the only conversation. View state survives navigation, so "go back to the comparison" restores it exactly.
import { useWorld } from '../mock/world';
import { useViewState, runAction } from '../q/core/engine';
import { Canvas } from '../ds/Workspace';
import { Glyph, GlyphKey } from '../ds/Glyph';
import { Link } from '../ui/router';
import { cellFor, defaultView, firstName, nameOf, rank, readingOf, reqsOf, rolePeople, weightOf, type CompareView } from '../journeys/hire-b/model';
import { LevelMark, VerTag, fmtDate, verOf } from '../journeys/hire-b/ui';
import '../journeys/hire-b/ops';

const toggle = (xs: string[], x: string) => (xs.includes(x) ? xs.filter((y) => y !== x) : [...xs, x]);

export function Compare() {
  const w = useWorld((x) => x);
  const [stored] = useViewState<Partial<CompareView> | undefined>('cmp', undefined);
  const v: CompareView = { ...defaultView(w), ...(stored ?? {}) };
  const set = (patch: Partial<CompareView>) => void runAction({ label: 'Update comparison', act: { t: 'do', op: 'hb.cmp.set', args: patch } });
  const pool = rolePeople(w);
  const reqs = reqsOf(w);
  const people = v.people.filter((p) => pool.includes(p));
  const crit
… [24792 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read ops, skill reply kinds, proactive

  <details><summary>result</summary>

```
// R2 operations. Pages and Q's replies both perform work through these registered ops, so a button and
// a typed request do exactly the same thing (and Q can offer them as serialisable actions).
import { emit, getWorld, now, uid, update, type World } from '../../mock/world';
import type { Actor, Stage } from '../../state/domain';
import { pushUndo, qSays, registerOp } from '../../q/core/engine';
import { hireB, type Level, type Rating } from '../../state/areas/hire-b';
import { cellFor, defaultView, draftFeedback, firstName, KORA_ROLE, questionsFor, reqLabel, visibleIds, type CompareView } from './model';

const scope = (a: Actor) => (a.orgId ? `ORG:${a.orgId}` : `PERSON:${a.personId}`);
export const CMP_KEY = (actorId: string) => `${actorId}|/r/compare`;
export function cmpView(w: World, actorId = w.session.actor): CompareView {
  return { ...defaultView(w), ...((w.q.ui[CMP_KEY(actorId)]?.cmp as Partial<CompareView> | undefined) ?? {}) };
}
export function setCmp(w: World, actorId: string, patch: Partial<CompareView>) {
  const k = CMP_KEY(actorId);
  (w.q.ui[k] ??= {}).cmp = { ...cmpView(w, actorId), ...patch };
}

// ---------- GitHub (simulated connector) ----------
let ghTimer: number | undefined;
/** Retry the simulated GitHub connector. The outage clears on the second retry: the first honestly fails. */
export function ghRetry(w: World, actor: Actor) {
  const g = hireB(w).github;
  if (g.status === 'CHECKING') return g.tries;
  g.status = 'CHECKING'; g.tries += 1;
 
… [22074 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect Q ref card mechanism

  <details><summary>result</summary>

```
// Live renderers for Q messages that point at state (a plan's agents, a message draft, a CV parse).
// Registered by the area that owns the state; the global thread looks them up by ref.type.
import type { RefRenderer } from './core/types';
const refs = new Map<string, RefRenderer>();
export const registerRef = (type: string, r: RefRenderer) => { refs.set(type, r); };
export const refRenderer = (type: string) => refs.get(type);
./journeys/talent-b/ui.tsx:44:registerRef('tb.evidence', ({ id }) => {
./journeys/talent-b/ui.tsx:56:registerRef('tb.uploads', ({ id }) => {
./journeys/talent-b/ui.tsx:62:registerRef('tb.summary', ({ id }) => {
./journeys/talent-b/ui.tsx:67:registerRef('tb.match', ({ id }) => {
./journeys/talent-b/ui.tsx:79:registerRef('tb.apps', ({ id }) => {
./journeys/hire-c/refs.tsx:90:registerRef('hire-c.draft', DraftRef);
./journeys/hire-c/refs.tsx:91:registerRef('hire-c.diff', DiffRef);
./journeys/hire-c/refs.tsx:92:registerRef('hire-c.checks', ChecksRef);
./journeys/hire-c/refs.tsx:93:registerRef('hire-c.slots', SlotsRef);
./journeys/onboarding/refs.tsx:55:registerRef('ta.matches', Matches);
```
  </details>

- 🔧 `Bash`: Inspect a ref card example

  <details><summary>result</summary>

```
56:export type RefRenderer = (props: { id: string }) => JSX.Element | null;
// Live cards Q shows inside its replies for R3: a draft at a given version, the change between versions,
// the pre-send checks, and proposed interview times with everyone's local time.
import { useState } from 'react';
import { useWorld } from '../../mock/world';
import { hc } from '../../state/areas/hire-c';
import { registerRef } from '../../q/refs';
import { city, diffWords, findMsg, firstOf, LAGOS, msgStatusLabel, nameOf, tDay, tTime, tzOf } from './lib';

function DraftRef({ id }: { id: string }) {
  const [msgId, vs] = id.split('@');
  const d = useWorld((w) => hc(w).drafts[msgId]);
  const m = useWorld((w) => findMsg(w, msgId)?.m);
  const to = useWorld((w) => (d ? nameOf(w, d.personId) : m ? nameOf(w, m.to) : ''));
  const [all, setAll] = useState(false);
  if (!m) return null;
  const v = d?.versions.find((x) => x.v === Number(vs)) ?? d?.versions[d.versions.length - 1];
  const latest = d?.versions[d.versions.length - 1]?.v ?? 1;
  const body = v?.body ?? m.body;
  const long = body.split('\n').length > 7 || body.length > 420;
  return (
    <div className="hc-card" role="group" aria-label={`Draft version ${v?.v ?? 1} to ${to}`}>
      <div className="hc-card-head"><span className="lab">{v ? `v${v.v} · ` : ''}to {to}</span><span className="hc-status" data-s={m.status}>{msgStatusLabel[m.status]}</span></div>
      <p className="hc-subj">{v?.subject ?? m.subject}</p>
      <div className={`hc
… [4481 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read capture script and before list

  <details><summary>result</summary>

```
// Design review captures: every route as the person who uses it, desktop (1440×900) and phone (390×844),
// full page. Used for the visual audit and before/after comparison. Usage: node capture-all.mjs <base> <outdir>
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
const [BASE = 'http://localhost:4174/', OUT = 'review', ONLY = ''] = process.argv.slice(2);
export const PAGES = {
  u_funmi: ['/r/home', '/r/roles'],
  u_ada: ['/r/home', '/r/plan', '/r/compare', '/r/people/p_tobi', '/r/interviews', '/r/pipeline', '/r/messages', '/r/calendar', '/r/team', '/r/setup', '/r/roles', '/r/audit', '/r/memory', '/r/mandate', '/r/sourcing', '/settings'],
  u_dele: ['/r/home', '/r/agency/agents', '/r/agency/campaigns', '/r/agency/clients', '/r/agency/client/org_kora', '/r/agency/compare', '/r/agency/docs', '/r/agency/mandate/m_ops', '/r/agency/notes', '/r/agency/pools', '/r/agency/reports', '/r/agency/searches', '/r/agency/submittals'],
  p_amaka: ['/c/home', '/c/welcome', '/c/jobs'],
  p_chidi: ['/c/career', '/c/growth'],
  p_tobi: ['/c/passport', '/c/jobs/j_kora_backend', '/c/prep', '/c/memory', '/c/interview'],
  p_grace: ['/c/home', '/c/start', '/c/interview', '/c/slots'],
  p_zara: ['/c/jobs', '/c/applications', '/c/messages', '/settings'],
  public: ['/signup', '/gallery/states'],
};
const b = await pw.chromium.launch();
for (const [vp, size] of [['d', { width: 1440, height: 900 }], ['m', { width: 390, height: 844 }]]) {
  const 
… [1627 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Start vite dev server on 5182

  <details><summary>result</summary>

```
VITE v5.4.21  ready in 1189 ms

  ➜  Local:   http://localhost:5182/
  ➜  Network: use --host to expose
```
  </details>

- 🔧 `Bash`: Capture current pages of my area

  <details><summary>result</summary>

```
Node.js v22.22.0
u_ada_r_compare.png
u_ada_r_interviews.png
u_ada_r_people_p_tobi.png
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_interviews.png (1440, 900)
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_people_p_tobi.png (1440, 900)
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_compare.png (1440, 900)
```
  </details>

- 🔧 `Bash`: See capture error output

  <details><summary>result</summary>

```
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur
```
  </details>

- 🔧 `Bash`: List captures

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur:
desktop
phone

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop:
u_ada_r_compare.png
u_ada_r_interviews.png
u_ada_r_people_p_tobi.png

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/phone:
u_ada_r_compare.png
u_ada_r_interviews.png
u_ada_r_people_p_tobi.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_compare.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_people_p_tobi.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:23

[Image: original 1440x4020, displayed at 716x2000. Multiply coordinates by 2.01 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_interviews.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R2/d-10-copilot-vague.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R2/d-11-feedback-draft.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Check phone capture sizes

  <details><summary>result</summary>

```
u_ada_r_compare (780, 7058)
u_ada_r_people_p_tobi (780, 11962)
u_ada_r_interviews (780, 2588)
```
  </details>

- 🔧 `Bash`: Create tall-image splitter and split compare phone

  <details><summary>result</summary>

```
1
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/pc-0.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:24

[Image: original 2380x2400, displayed at 1916x1932. Multiply coordinates by 1.24 to map to original image.]

- 🔧 `Bash`: List ds classes and tokens

  <details><summary>result</summary>

```
.ds-actions .ds-agent .ds-app .ds-askbar .ds-av .ds-banner .ds-brandname .ds-btn .ds-canvas .ds-canvas-head .ds-chip .ds-compose .ds-context .ds-field .ds-filter .ds-groupbtn .ds-iconbtn .ds-input .ds-linkbtn .ds-log .ds-main .ds-me .ds-more .ds-navgroup .ds-navlink .ds-next .ds-node .ds-note .ds-opt .ds-page .ds-page-body .ds-palette .ds-plan .ds-proto .ds-proto-bar .ds-q .ds-qline .ds-qsim .ds-quote .ds-rail .ds-rail-brand .ds-rail-foot .ds-railbtn .ds-scrim .ds-send .ds-sep .ds-sheet .ds-sheetbar .ds-sim .ds-skeleton .ds-space .ds-space-btn .ds-split .ds-strip .ds-suggest .ds-suggest-foot .ds-table .ds-table-wrap .ds-tabs .ds-tag .ds-taskhead .ds-thinking .ds-thread .ds-thread-head .ds-used .ds-versions .ds-views .ds-who .ds-why 
3:  --ref-gold-300: #f0d395;
4:  --ref-gold-400: #e3c27d;
5:  --ref-gold-500: #d9b56b;
6:  --ref-gold-600: #b8892a;
7:  --ref-gold-700: #9a7220;
8:  --ref-gold-800: #7a5a17;
9:  --ref-gold-900: #4f3a0e;
10:  --ref-night-0: #121110;
11:  --ref-night-1: #1c1a17;
12:  --ref-night-2: #24211d;
13:  --ref-night-3: #2a2723;
14:  --ref-night-4: #34302a;
15:  --ref-night-5: #433d34;
16:  --ref-paper-0: #f5f1e8;
17:  --ref-paper-1: #fffdf8;
18:  --ref-paper-2: #ece5d6;
19:  --ref-paper-3: #dcd2bf;
20:  --ref-paper-4: #c3b8a3;
21:  --ref-ink-100: #ece6da;
22:  --ref-ink-200: #c9c1b2;
23:  --ref-ink-300: #b9b1a3;
24:  --ref-ink-400: #8f887b;
25:  --ref-ink-600: #5d5648;
26:  --ref-ink-700: #3c372d;
27:  --ref-ink-800: #2b2720;
28:  --ref-ink-900: #16140f;
29:
… [966 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Semantic tokens and some ds classes

  <details><summary>result</summary>

```
1:  --size-heading: 30px;
2:  --size-display: 38px;
3:  --size-hero: 46px;
4:  --motion-instant: 80ms;
5:  --motion-quick: 160ms;
6:  --motion-base: 240ms;
7:  --motion-slow: 420ms;
8:  --motion-settle: 700ms;
9:  --motion-ease-out: cubic-bezier(0.2, 0.7, 0.2, 1);
10:  --motion-ease-in-out: cubic-bezier(0.6, 0, 0.3, 1);
11:  --target-min: 44px;
13::root, [data-theme="dark"] {
14:  --color-bg: var(--ref-night-0);
15:  --color-surface: var(--ref-night-1);
16:  --color-surface-raised: var(--ref-night-2);
17:  --color-surface-sunken: var(--ref-night-0);
18:  --color-line: var(--ref-night-3);
19:  --color-line-strong: var(--ref-night-5);
20:  --color-text: var(--ref-ink-100);
21:  --color-text-muted: var(--ref-ink-300);
22:  --color-text-subtle: var(--ref-ink-400);
23:  --color-q: var(--ref-gold-500);
24:  --color-q-strong: var(--ref-gold-300);
25:  --color-q-text: var(--ref-gold-500);
26:  --color-on-q: var(--ref-night-0);
27:  --color-action: var(--ref-gold-500);
28:  --color-on-action: var(--ref-night-0);
29:  --color-focus: var(--ref-gold-300);
30:  --color-ok: var(--ref-green-dark);
31:  --color-warn: var(--ref-amber-dark);
32:  --color-risk: var(--ref-red-dark);
33:  --color-info: var(--ref-blue-dark);
34:  --color-paper: var(--ref-paper-0);
35:  --color-paper-raised: var(--ref-paper-1);
36:  --color-paper-line: var(--ref-paper-3);
37:  --color-paper-text: var(--ref-ink-900);
38:  --color-paper-muted: var(--ref-ink-700);
39:  --color-paper-q-text: var(--ref-gold-800);
41:@me
… [2953 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find short design variable definitions

  <details><summary>result</summary>

```
ds/ds.css:7:  --paper: var(--ref-paper-0); --sheet: var(--ref-paper-1); --wash: var(--ref-paper-2); --rule: var(--ref-paper-3); --rule-2: var(--ref-paper-4);
ds/ds.css:8:  --ink: var(--ref-ink-900); --ink-2: var(--ref-ink-700); --ink-3: var(--ref-ink-600);
ds/ds.css:10:  --gold: var(--ref-gold-600); --gold-ink: var(--ref-gold-800); --gold-light: var(--ref-gold-400); --gold-wash: #f1e3bf;
ds/ds.css:11:  --ok: var(--ref-green-light); --warn: var(--ref-amber-light); --risk: var(--ref-red-light);
139:.ds-filter { border: 1px solid var(--rule-2); background: transparent; border-radius: 999px; padding: 6px 12px; min-height: 36px; font-size: 14px; color: var(--ink-2); }
140:.ds-filter[aria-pressed='true'] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
ds/ds.css:24:.ds .sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
ds/ds.css:25:.ds .lab { font-family: var(--data); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); font-weight: 500; }
ds/ds.css:26:.ds .ink .lab { color: var(--moon-2); }
ds/ds.css:27:.ds .num { font-variant-numeric: tabular-nums; }
ds/ds.css:28:.ds .voice { font-family: var(--voice); font-weight: 380; letter-spacing: -.01em; }
ds/ds.css:31:.ds .t24 { font-size: 24px; line-height: 1.2; }
ds/ds.css:33:.ds .t14 { font-size: 14px; line-height: 1.45; }
ds/ds.css:34:.ds .muted { color: var(--ink-3); }
ds/ds.css:35:.ds .ink .muted { color: var(--m
… [87 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Validate ordinal ink ramp

  <details><summary>result</summary>

```
unknown flag: --help

Palette (light, surface #fffdf8, ordinal ramp): 4 slots
  [PASS] Lightness monotone     steps read light→dark
  [PASS] Adjacent ΔL            all gaps >= 0.06
  [FAIL] Light-end contrast     #ece5d6 at 1.23:1 vs surface — below 2:1 floor
  [PASS] Single hue             hue spread 7°

  → FAILED — fix the marked checks  (ordinal: one hue, monotone L, visible step gaps, light end clears surface)
```
  </details>

- 🔧 `Bash`: Validate candidate 3-step ramps

  <details><summary>result</summary>

```
Palette (light, surface #fffdf8, ordinal ramp): 3 slots
  [PASS] Lightness monotone     steps read light→dark
  [PASS] Adjacent ΔL            all gaps >= 0.06
  [PASS] Light-end contrast     #b9b1a3 at 2.09:1 vs surface
  [PASS] Single hue             hue spread 7°
  → ALL CHECKS PASS  (ordinal: one hue, monotone L, visible step gaps, light end clears surface)
Palette (light, surface #fffdf8, ordinal ramp): 3 slots
  [PASS] Lightness monotone     steps read light→dark
  [PASS] Adjacent ΔL            all gaps >= 0.06
  [FAIL] Light-end contrast     #c3b8a3 at 1.93:1 vs surface — below 2:1 floor
  [PASS] Single hue             hue spread 2°
  → FAILED — fix the marked checks  (ordinal: one hue, monotone L, visible step gaps, light end clears surface)
Palette (light, surface #fffdf8, ordinal ramp): 3 slots
  [PASS] Lightness monotone     steps read light→dark
  [PASS] Adjacent ΔL            all gaps >= 0.06
  [PASS] Light-end contrast     #a39a8a at 2.74:1 vs surface
  [PASS] Single hue             hue spread 7°
  → ALL CHECKS PASS  (ordinal: one hue, monotone L, visible step gaps, light end clears surface)
```
  </details>

- 🔧 `Bash`: Read Canvas component API

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
… [2026 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read R2 journey script

  <details><summary>result</summary>

```
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
  page.on('pageerror', (e) => errors.push(`${v}: ${e}`));
  page.on('console', (m) => { if (m.type() === 'error' && !/favicon|Failed to load resource/.t
… [12085 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R2/d-02-challenge.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Read skills file part 1
- 🔧 `Bash`: Read skills file part 2

  <details><summary>result</summary>

```
registerSkill({
  id: 'hire-b.correct', side: 'recruiter',
  match: (c) => (kora(c) && who(c).length >= 1 && criteriaIn(c.norm).length >= 1 && (DOWN.test(c.norm) || UP.test(c.norm)) ? 0.94 : 0),
  handle: (c) => {
    const pid = who(c)[0]; const reqId = criteriaIn(c.norm)[0];
    const v = cmpView(c.w, c.actor.id);
    const cur = cellFor(c.w, pid, reqId, v).level;
    const down = DOWN.test(c.norm);
    const order: Level[] = ['none', 'partial', 'evidenced', 'verified'];
    const idx = Math.max(0, order.indexOf(cur === 'claim' ? 'none' : cur));
    const level: Level = down ? order[Math.max(0, idx - 1)] : order[Math.min(2, idx + 1)];
    if (level === cur) return { msgs: [{ kind: 'reply', text: down ? `I already read ${fn(c.w, pid)}’s ${reqLabel(c.w, reqId)} as “${LEVEL_WORD[cur].toLowerCase()}”, so there’s nothing lower to move it to.` : `I can’t raise ${fn(c.w, pid)}’s ${reqLabel(c.w, reqId)} above “evidenced” on anyone’s word: only a check at the source makes it verified. I can ask ${fn(c.w, pid)} for something checkable.` }] };
    const note = down ? (/library/.test(c.norm) ? 'A library, not production experience' : `Counts for less than Q said`) : 'Counts more than Q said';
    const before = orderText(c.w, v);
    const sim = structuredClone(c.w); addCorrection(sim, c.actor, pid, reqId, level, note);
    const after = orderText(sim, v);
    return {
      msgs: [{ kind: 'reply', text: `Accepted. I now read ${fn(c.w, pid)}’s ${reqLabel(c.w, reqId)} as “${LEVEL_WORD[l
… [22636 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// Q skills for R2 (Ada, a non-technical recruiter hiring engineers). Everything on the R2 pages can be
// asked for in plain, imperfect language: compare by chosen criteria, explain and defend a ranking and
// accept corrections, separate CV claims from evidence, retry an unavailable integration, recommend
// assessments, generate interview questions from gaps, adaptive follow-ups during an interview, feedback,
// and assessment disputes. Rule-based and honest about it (see core.honest).
import { actorOf, emit, visibleEvidence, type World } from '../../mock/world';
import type { Actor, QAction } from '../../state/domain';
import { registerSkill } from '../core/engine';
import type { QCtx, QReply } from '../core/types';
import { hireB, type Level, type Rating } from '../../state/areas/hire-b';
import { ASSESS, KORA_ROLE, LEVEL_VALUE, LEVEL_WORD, assessFor, cellFor, criteriaIn, disputedEvidence, firstName, followUpsFor, isVague, koraInterviews, nameOf, peopleIn, personInFocus, questionsFor, rank, readingOf, reqLabel, reqsOf, rolePeople, viewerOrg, weightOf, type CompareView } from '../../journeys/hire-b/model';
import { addCorrection, cmpView, finishInterview, ghRetry, live, setCmp, startInterview } from '../../journeys/hire-b/ops';
import { PROJECTS } from '../../journeys/hire-b/projects';

const kora = (c: QCtx) => c.actor.orgId === 'org_kora' && c.actor.side === 'recruiter';
const who = (c: QCtx) => peopleIn(c.norm, c.ents.people).filter((p) => c.w.people.some((x) => x.pers
… [10281 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check ref card styling context

  <details><summary>result</summary>

```
4:.ds .hc-card { background: var(--sheet); color: var(--ink); border-radius: 12px; padding: 12px 14px; display: grid; gap: 8px; min-width: 0; --ink-3: var(--ref-ink-600); }
5:.ds .hc-card .lab { color: var(--ink-3); }
6:.ds .hc-card-head { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 6px 10px; }
8:.ds .hc-card .ds-sim { color: var(--ink-3); border-color: var(--rule-2); }
16:.ds .hc-card ins, .ds .hc-card del { font-style: normal; }
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
      {m.kind === 'notice' && <span className="lab">Up
… [807 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Add ledger helpers to model

  <details><summary>result</summary>

```
109:export interface CompareView { people: string[]; criteria: string[]; lastYear: boolean; weighting: Weighting; open?: { pid: string; reqId: string } | null }
```
  </details>

- 🔧 `Bash`: Record snapshots on comparison changes

  <details><summary>result</summary>

```
7:import { cellFor, defaultView, describeChange, shortLabel, snapshot, draftFeedback, firstName, KORA_ROLE, questionsFor, reqLabel, visibleIds, type CompareView } from './model';
```
  </details>

- 🔧 `Bash`: Clear correction snapshot on undo

  <details><summary>result</summary>

```
55:  pushUndo(w, actor.id, `your correction to ${firstName(w, pid)}’s ${reqLabel(w, reqId)}`, 'hb.correct.remove', { id });
59:registerOp('hb.correct.remove', (w, a, actor) => { const s = hireB(w); s.corrections = s.corrections.filter((c) => c.id !== a.id); const v = w.q.ui[CMP_KEY(actor.id)]?.cmp as CompareView | undefined; if (v?.last?.label.startsWith('You corrected')) v.last = null; });
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Ledger.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Ledger.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Tidy Ledger helper code

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/screens/Compare.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/screens/Compare.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: List text size classes

  <details><summary>result</summary>

```
.ds .t14 .ds .t19 .ds .t24 .ds .t30 .ds .t46
```
  </details>


**Claude** · 2026-10-29 12:28

Now the CSS for the ledger, filters and compare.

- 🔧 `Bash`: Add ledger and compare styles

  <details><summary>result</summary>

```
[This command modified 1 file you've previously read: screens/Compare.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Fix phone header and typecheck

  <details><summary>result</summary>

```
--night: var(--ref-night-0); --night-2: var(--ref-night-1); --night-3: var(--ref-night-3); --night-4: var(--ref-night-4); --moon: var(--ref-ink-100); --moon-2: var(--ref-ink-300);
```
  </details>

- 🔧 `Bash`: Capture redesigned compare

  <details><summary>result</summary>

```
1
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/desktop/u_ada_r_compare.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/pc-0.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:30

[Image: original 2380x2400, displayed at 1916x1932. Multiply coordinates by 1.24 to map to original image.]

- 🔧 `Bash`: Container query for margin notes

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Check projects and stages

  <details><summary>result</summary>

```
// Read-only snapshots of shared projects for the safe project viewer. Fictional code and pages.
// Nothing here is executed: code is shown as text, pages render in a sandboxed frame with scripts off.
export interface ProjectSnapshot {
  kind: 'code' | 'page';
  where: string;
  github?: boolean;
  files?: { path: string; code: string }[];
  html?: string;
  links: string[];
  explain: { summary: string; shows: string[]; doesNot: string[] };
}

export const PROJECTS: Record<string, ProjectSnapshot> = {
  e_tobi_go: {
    kind: 'code', where: 'github.com/tobi-adeyemi/idem', github: true,
    links: ['https://github.com/tobi-adeyemi/idem', 'https://pkg.go.dev/github.com/tobi-adeyemi/idem'],
    files: [
      { path: 'idem.go', code: `// Package idem makes a payment request safe to retry.\npackage idem\n\n// Do runs fn once per key. A retry with the same key returns\n// the first result instead of paying twice.\nfunc (s *Store) Do(ctx context.Context, key string, fn func() (Result, error)) (Result, error) {\n\tif r, ok, err := s.get(ctx, key); err != nil {\n\t\treturn Result{}, fmt.Errorf("idem: lookup %q: %w", key, err)\n\t} else if ok {\n\t\treturn r, nil // already done: don't run fn again\n\t}\n\tunlock, err := s.lock(ctx, key)\n\tif err != nil {\n\t\treturn Result{}, ErrInFlight\n\t}\n\tdefer unlock()\n\tr, err := fn()\n\tif err != nil {\n\t\treturn Result{}, err // not saved, so a retry can try again\n\t}\n\treturn r, s.put(ctx, key, r)\n}` },
      { path: 'idem_test.go'
… [2042 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Add bare mode to Ledger

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Profile.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Profile.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>


**Claude** · 2026-10-29 12:31

You've hit your 5-hour limit · resets 1:50pm (UTC)


**User** · 2026-10-29 13:51

The coordinator sent a message while you were working:
From the lead: the usage limit has reset. Please pick up the design pass exactly where you stopped. Your brief and my two follow-up messages (the handoff doc and SwitchRow) still apply.

Address this before completing your current task.

- 🔧 `Bash`: Read shared SwitchRow component

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
258:.ds-switchrow { display: grid; grid-template-columns: 1fr auto; gap: 16px; align-items: center; padding: 14px 0; border-top: 1px solid var(--rule); }
259:.ds-switchrow:first-of-type { border-top: 0; }
260:.ds-switchrow .txt { display: grid; gap: 2px; min-width: 0; }
261:.ds-switch { all: unset; box-sizing: border-box; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; min-height: 44px; padding: 0 2px; font-size: 14px; color: var(--ink-2); }
262:.ds-switch .knob { width: 44px; height: 26px; border-radius: 999px; background: var(--rule-2); position:
… [648 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Use SwitchRow and update script helper

  <details><summary>result</summary>

```
43:  const pressed = async (name) => { const f = page.locator('.ds-canvas button.ds-filter', { hasText: name }); if (await f.count()) return f.first().getAttribute('aria-pressed'); return page.locator('.ds-canvas').getByRole('switch', { name, includeHidden: true }).first().getAttribute('aria-checked'); };
```
  </details>

- 🔧 `Bash`: Make viewer selection controllable, add arrival

  <details><summary>result</summary>

```
56:      <div className="hire-b-viewer">
57:        <motion.div key={`${cur.evidenceId}:${file}:${gh.status}`} {...arrive} className="hire-b-frame" aria-busy={checking || undefined}>
69:        </motion.div>
```
  </details>

- 🔧 `Bash`: Add profile styles and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Capture profile and compare

  <details><summary>result</summary>

```
2
(1440, 4343)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a2/dp1.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 13:54

[Image: original 828x2171, displayed at 763x2000. Multiply coordinates by 1.09 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a2/dp2.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 13:54

[Image: original 828x2172, displayed at 762x2000. Multiply coordinates by 1.09 to map to original image.]

- 🔧 `Bash`: Find banner lines

  <details><summary>result</summary>

```
32:  const down = ghItems.length > 0 && gh.status !== 'OK';
46:      {down && (
53:      {ghItems.length > 0 && gh.status === 'OK' && <p className="t14 muted" role="status" style={{ margin: 0 }}>GitHub answered {gh.checkedAt ? fmtTime(gh.checkedAt) : ''}. Showing the current copy (simulated).</p>}
54:      <p className="t14 muted" style={{ margin: 0 }}>{p.where}{p.github ? ` · ${down ? `cached ${fmtDate(gh.cachedAt)}` : 'live copy'}` : ''} · {cur.title}</p>
```
  </details>

- 🔧 `Bash`: Contextual GitHub banner, minutes fix

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a2/pp-0.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 13:54

[Image: original 3180x2600, displayed at 2000x1635. Multiply coordinates by 1.59 to map to original image.]

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Interviews.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/Interviews.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Interview styles and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/refs.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/hire-b/refs.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Attach ref cards to skill replies

  <details><summary>result</summary>

```
state/domain.ts:76:  ref?: { type: string; id: string };
5
src/q/skills/hire-b.ts(115,11): error TS6133: 'lines' is declared but its value is never read.
src/q/skills/hire-b.ts(268,11): error TS6133: 'qs' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Remove unused variables

  <details><summary>result</summary>

```
src/q/skills/hire-b.ts(11,29): error TS6133: 'LEVEL_VALUE' is declared but its value is never read.
src/q/skills/hire-b.ts(11,259): error TS6133: 'weightOf' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Drop unused imports

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 14:02

Now card CSS, then run R2.

- 🔧 `Bash`: Add card styles and run R2 journey

  <details><summary>result</summary>

```
PASS [d] [info] withdrawn consent: permission state with reason
PASS [m] starts as Ada
PASS [m] role research in plain words
PASS [m] compare by criteria navigates
PASS [m] only Tobi and Zara, payments and Go
PASS [m] [mind] criteria changed mid-comparison
PASS [m] [mind] challenge: Q shows reasoning and evidence
PASS [m] [mind] Q accepts the correction
PASS [m] weighting changed by typing
PASS [m] profile opens from Q
PASS [m] profile: only shared evidence with provenance
PASS [m] profile: confidential exists, contents hidden
PASS [m] profile: pipeline position
PASS [m] [info] GitHub outage shown honestly with cache date
PASS [m] safe viewer: sandboxed, read-only
PASS [m] [info] retry #1 still down, said honestly
PASS [m] [info] retry #2 recovers
PASS [m] page preview sandboxed (scripts off)
PASS [m] external link shows domain before opening
PASS [m] go back restores the comparison exactly
PASS [m] draft invitation handled (hire-c skill) without breaking R2 · I took that to mean Tobi, from the profile you just viewed. Here’s a draft interview invit
PASS [m] [info] CV vs evidence: unknown separated from weak
PASS [m] [mind] last-year filter on, notes rewritten
PASS [m] [info] proactive: dispute raised from real state
PASS [m] [info] Q explains the dispute
PASS [m] review needs approval
PASS [m] [info] disputed result excluded from comparison
PASS [m] assessment recommended with reasons
PASS [m] interview questions from evidence gaps
PASS [m] copilot started
PASS [m] vague ans
… [393 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R2/d-03-corrected-equal.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R2/d-10-copilot-vague.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Short rail labels; montage feedback states

  <details><summary>result</summary>

```
[This command modified 1 file you've previously read: ../../../prototype/src/journeys/hire-b/Interviews.tsx. Call Read before editing.]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/fb3.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:04

[Image: original 2484x900, displayed at 2000x725. Multiply coordinates by 1.24 to map to original image.]

- 🔧 `Bash`: Fix rating check, date block, success mark

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 14:06

Now phone states: compare, copilot, feedback.

- 🔧 `Bash`: Montage phone journey states

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/m5.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:06

[Image: original 3980x1688, displayed at 2000x848. Multiply coordinates by 1.99 to map to original image.]

- 🔧 `Bash`: Merge change descriptions into one clause

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Run privacy review script

  <details><summary>result</summary>

```
// Privacy: candidates' discovery rules hold everywhere a recruiter can reach them — search and pools,
// profiles, Q's tools, cached views and downstream artifacts (campaigns). Usage: node privacy.mjs [base]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
const BASE = process.argv[2] || 'http://localhost:4174/';
let fails = 0; const step = (ok, n, x = '') => { if (!ok) fails++; console.log(`${ok ? 'PASS' : 'FAIL'} ${n}${x ? ` · ${String(x).slice(0, 140)}` : ''}`); };
const b = await pw.chromium.launch(); const page = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
const errors = []; page.on('pageerror', (e) => errors.push(e.message));
await page.goto(`${BASE}#/settings`); await page.evaluate(() => localStorage.clear()); await page.reload(); await page.waitForTimeout(700);
const qa = (fn, ...args) => page.evaluate(([f, a]) => { const q = window.__tqQA; return q[f](q.getWorld(), ...a); }, [fn, args]);
// Switch person through the app's own store (writing localStorage directly races with the app's own saves).
const as = async (actor, route) => { await page.evaluate((a) => window.__tqQA.update((w) => { w.session.actor = a; w.actors.find((x) => x.id === a).signedUp = true; }), actor); await page.evaluate((r) => { location.hash = r; }, route); await page.waitForTimeout(900); const now = await page.evaluate(() => window.__tqQA.getWorld().session.actor); if (now !== actor) throw new Error(`actor is ${now}, expected ${actor}`); };

… [1487 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Capture key R2 states

  <details><summary>result</summary>

```
done
```
  </details>

- 🔧 `Bash`: Montage desktop states

  <details><summary>result</summary>

```
r2_compare-inspector (1440, 2216)
r2_profile-kunle-cv (1440, 3143)
r2_interview-brief-planning (1440, 991)
r2_interview-kunle-done (1440, 1142)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/d3.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:08

[Image: original 2484x900, displayed at 2000x725. Multiply coordinates by 1.24 to map to original image.]

- 🔧 `Bash`: Done-interview title and plan copy

  <details><summary>result</summary>

```
128:  const doneElsewhere = l.step === 'BRIEF' && i.status === 'DONE';
129:  const title = doneElsewhere ? `${first}’s interview is done` : l.step === 'BRIEF' ? `Interview with ${first}: ${unknowns ? `${unknowns} thing${unknowns === 1 ? '' : 's'} to find out` : 'go deeper on what’s checked'}`
159:          <h2 id="iv-plan" className="voice t24" style={{ margin: 0 }}>{doneElsewhere ? 'Questions for a next round' : 'Questions from the evidence'}</h2>
```
  </details>

- 🔧 `Bash`: Correct question-order copy

  <details><summary>result</summary>

```
journeys/hire-b/Profile.tsx:1
q/skills/hire-b.ts:1
```
  </details>


**Claude** · 2026-10-29 14:08

Now phone states and the inspector.

- 🔧 `Bash`: Montage phone states and inspector crop

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/p4.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:08

[Image: original 3180x1688, displayed at 2000x1062. Multiply coordinates by 1.59 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/insp.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Fix list grammar in Q notes

  <details><summary>result</summary>

```
4
```
  </details>

- 🔧 `Bash`: Run R2, after captures, state captures

  <details><summary>result</summary>

```
PASS [m] [info] withdrawn consent: permission state with reason
ERRORS []
R2: 74/74 steps passed
captured 102 pages to captures/review/after
done
u_ada_r2_compare-inspector.png
u_ada_r2_copilot-live.png
u_ada_r2_interview-brief-planning.png
u_ada_r2_interview-kunle-done.png
u_ada_r2_interviews-empty-feedback.png
u_ada_r2_profile-kunle-cv.png
u_ada_r2_profile-missing.png
u_ada_r2_profile-withdrawn.png
u_ada_r_compare.png
u_ada_r_interviews.png
u_ada_r_people_p_tobi.png
```
  </details>

- 🔧 `Bash`: Montage interview states

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/iv3.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:13

[Image: original 2484x900, displayed at 2000x725. Multiply coordinates by 1.24 to map to original image.]

- 🔧 `Bash`: Probe faded canvas opacity

  <details><summary>result</summary>

```
/r/interviews/i_hb_tobi []
/r/interviews/i_hb_kunle []
```
  </details>

- 🔧 `Bash`: Recapture states with longer wait

  <details><summary>result</summary>

```
done
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/tb.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Copy states and build before/after pairs

  <details><summary>result</summary>

```
captures/review/pairs/hire-b/01-after.png   1440 x 1977, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/01-before.png  1440 x 1934, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/02-after.png   780 x 5660, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/02-before.png  780 x 7074, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/03-after.png   1440 x 900, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/03-before.png  1440 x 900, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/04-after.png   1440 x 900, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/04-before.png  1440 x 900, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/05-after.png   1440 x 4279, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/05-before.png  1440 x 4018, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/06-after.png   1440 x 940, 8-bit/color RGB, non-interlaced
captures/review/pairs/hire-b/06-before.png  1440 x 1037, 8-bit/color RGB, non-interlaced
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/hire-b/03-after.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Check existing design/handoff docs

  <details><summary>result</summary>

```
design:
agency.md
talent-a.md
talent-b.md

handoff:
agency.md
talent-a.md
talent-b.md
talent-c.md
==> handoff/agency.md <==
# Engineering handoff · agency (R4 Dele at Talentbridge; Tunde is a Viewer)

Specification only. The prototype is the behavioural and design blueprint, not the implementation. Every
"Prototype:" reference is to `prototype/src/`. Lines marked **PROD ≠ SIM** say where production must differ from the
simulation. Journey proof: `qa/scripts/journeys/R4.mjs`; privacy proof: `qa/scripts/review/privacy.mjs`.
Code map: model/rules `journeys/agency/model.ts`, pages `journeys/agency/pages.tsx`, routes `routes/agency.tsx`,
state and seed `state/areas/agency.ts`, `state/seeds/agency.ts`, Q `q/skills/agency.ts` (ids `agency.*`),
proactive `q/proactive/agency.ts`.

## 0. Defaults every feature inherits
- **Tenancy is two levels.** The *agency* (`org_tb`) is the tenant. The *client* (`org_kora`, `org_medlink`) is a
  hard partition inside it: every record (pool, search, campaign, submittal, note, run, doc, report, access request)
  carries `clientOrgId`. Every read takes the client in focus (`poolsFor(w, client)` etc. in model.ts). No API returns
  a cross-client list except agency home and agents, which return per-client groups. **PROD:** enforce this with row-level
  security on `(agency_id, client_org_id)`, not in the UI. A query without a client predicate fails closed.
- **Candidate privacy is central.** The agency sees only people with a relationship (registered wi
… [3695 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/hire-b.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/hire-b.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Read sanitiser and privacy helpers

  <details><summary>result</summary>

```
},
  },
};

/** Make a page snapshot inert: no scripts, no live links, no outside requests. */
export function inertHtml(html: string) {
  const csp = `<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data:">`;
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/\son\w+="[^"]*"/gi, '')
    .replace(/<a\b[^>]*>([\s\S]*?)<\/a>/gi, '<span style="text-decoration:underline">$1</span>')
    .replace(/<head>/i, `<head>${csp}`);
}
export const scriptCount = (html: string) => (html.match(/<script/gi) ?? []).length;
export const domainOf = (url: string) => { try { return new URL(url).hostname; } catch { return url; } };
201:export function canSeeCandidate(w: World, pid: string, orgId: string) {
202-  if (w.consents[pid]?.withdrawnFrom.includes(orgId)) return false;
203-  return relationshipWith(w, pid, orgId) || canDiscover(w, pid, orgId);
204-}
205-/** What an organisation may read. Shared items follow the explicit share; public items need canSeeCandidate. */
206:export function visibleEvidence(w: World, personId: string, viewerOrgId: string) {
207-  if (w.consents[personId]?.withdrawnFrom.includes(viewerOrgId)) return [];
208-  const seen = canSeeCandidate(w, personId, viewerOrgId);
209-  return w.evidence.filter((e) => e.ownerId === personId && e.kind !== 'PRACTICE' && !e.revokedFrom?.includes(viewerOrgId)
210-    && ((e.visibility === 'PUBLIC_PROFILE' && seen) || (e.visibility === 'SHARED_WITH' && e.s
… [102 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/hire-b.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/hire-b.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Final typecheck, stop server, list changes

  <details><summary>result</summary>

```
Exit code 144
0
```
  </details>

- 🔧 `Bash`: List changed files

  <details><summary>result</summary>

```
M talent-q-design/prototype/src/journeys/hire-a/Audit.tsx
 M talent-q-design/prototype/src/journeys/hire-a/Home.tsx
 M talent-q-design/prototype/src/journeys/hire-a/Roles.tsx
 M talent-q-design/prototype/src/journeys/hire-a/model.ts
 M talent-q-design/prototype/src/journeys/hire-a/ui.tsx
 M talent-q-design/prototype/src/journeys/hire-b/Interviews.tsx
 M talent-q-design/prototype/src/journeys/hire-b/Profile.tsx
 M talent-q-design/prototype/src/journeys/hire-b/ProjectViewer.tsx
 M talent-q-design/prototype/src/journeys/hire-b/model.ts
 M talent-q-design/prototype/src/journeys/hire-b/ops.ts
 M talent-q-design/prototype/src/journeys/hire-c/Calendar.tsx
 M talent-q-design/prototype/src/journeys/hire-c/CandidateMessages.tsx
 M talent-q-design/prototype/src/journeys/hire-c/Messages.tsx
 M talent-q-design/prototype/src/journeys/hire-c/Pipeline.tsx
 M talent-q-design/prototype/src/journeys/hire-c/Setup.tsx
 M talent-q-design/prototype/src/journeys/hire-c/Team.tsx
 M talent-q-design/prototype/src/journeys/hire-c/lib.ts
 M talent-q-design/prototype/src/journeys/hire-c/refs.tsx
 M talent-q-design/prototype/src/journeys/talent-b/Passport.tsx
 M talent-q-design/prototype/src/journeys/talent-b/logic.ts
 M talent-q-design/prototype/src/journeys/talent-c/FirstSteps.tsx
 M talent-q-design/prototype/src/journeys/talent-c/InterviewRoom.tsx
 M talent-q-design/prototype/src/journeys/talent-c/shared.tsx
 M talent-q-design/prototype/src/mock/world.ts
 M talent-q-design/prototype/src/q/skills/hire-a.
… [258 more characters trimmed]
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The design pass for hire-b (R2 Ada) is finished. R2.mjs passes 74 of 74 steps on desktop and phone with no page errors, `privacy.mjs` passes on port 5182, and none of my pages scroll side

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
