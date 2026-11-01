# Helper agent agent-acf12ef519c3f981b: Design pass R1+R5 pages

Source: `agent-acf12ef519c3f981b.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 12:20

Run the design pass for area `hire-a` (journeys R1 Funmi and R5 Bayo) in /home/user/neo/talent-q-design/prototype. First read /home/user/neo/talent-q-design/journeys/DESIGN-PASS-BRIEF.md and follow it exactly, including loading the named skills with the Skill tool and applying them. Also read /home/user/neo/talent-q-design/journeys/BUILD-BRIEF.md for the contracts and your file ownership; you own the same `hire-a` files as before.

Your dev server port is 5181 (`npx vite --port 5181 --strictPort`; don't run `npm run build`).

Your pages:
- founder home (Funmi, `/r/home` via registerRecruiterHome)
- `/r/roles` and `/r/roles/:id`
- `/r/audit`
- `/r/memory` (legacy src/screens/Memory.tsx, also used by `/c/memory` history; keep the candidate viewer working)
- `/r/mandate` and `/r/sourcing` (Kora's brief and search)
- every Q reply card and suggestion your skills produce

**Correctness blocker to fix in R1.** The store now enforces candidate privacy. `canSeeCandidate` in mock/world.ts is used by `poolFor` in journeys/hire-a/model.ts. A newly created, unverified business (Crumb & Co) therefore cannot find anyone, so R1's search returns nobody and R1.mjs fails at "simulated search finds bookkeepers only". That is the correct product rule.

Design a proper, honest "verify your business" step:
- Q explains plainly why verification is needed before search.
- Funmi gives a business registration number or confirms the email domain. This is simulated and clearly labelled, and can fail once as a curveball.
- On success the org becomes `verified: { domain: true, registry: 'VERIFIED' }`.
- Until then, Q offers what's possible: posting the role so people can apply, which creates a relationship.

Then the search works. Update R1.mjs to exercise it, without weakening any step. R5 must keep passing. Also run qa/scripts/review/privacy.mjs against your server.

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

- 🔧 `Bash`: Find hire-a files

  <details><summary>result</summary>

```
src/journeys/hire-a
src/journeys/hire-a/Audit.tsx
src/journeys/hire-a/Home.tsx
src/journeys/hire-a/Roles.tsx
src/journeys/hire-a/model.ts
src/journeys/hire-a/ui.tsx
src/q/proactive/hire-a.ts
src/q/skills/hire-a.ts
src/routes/hire-a.tsx
src/state/areas/hire-a.ts
src/state/seeds/hire-a.ts
src/styles/hire-a.css
src/journeys/hire-a/Audit.tsx
src/journeys/hire-a/Home.tsx
src/journeys/hire-a/Roles.tsx
src/journeys/hire-a/model.ts
src/journeys/hire-a/ui.tsx
src/q/proactive/hire-a.ts
src/q/skills/hire-a.ts
src/routes/hire-a.tsx
src/screens/MandateIntake.tsx
src/screens/Sourcing.tsx
src/state/areas/hire-a.ts
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
1:# Journey coverage map: R1–R5 and T1–T5
7:| Recruiter | **Funmi Adebayo** | Founder, Crumb & Co bakery (new signup) · R1 |
11:| Recruiter | **Bayo Ojo** | Kora engineering manager, sceptical · R5 |
30:### R1: The confused first-time employer (Funmi)
121:### R5: The difficult, sceptical recruiter (Bayo)
```
  </details>

- 🔧 `Bash`: Read journey map and sizes

  <details><summary>result</summary>

```
# Journey coverage map: R1–R5 and T1–T5

One product, one simulated world, one cast:

| Side | Who | Organisation or situation |
|---|---|---|
| Recruiter | **Funmi Adebayo** | Founder, Crumb & Co bakery (new signup) · R1 |
| Recruiter | **Ada Okafor** | Talent partner at Kora Pay, not technical · R2 |
| Recruiter | **Ngozi Eze** | HR lead at Kora Pay; colleagues Seyi (Lagos) and Musa (London) · R3 |
| Recruiter | **Dele Martins** | Talentbridge agency; clients Kora Pay and Medlink · R4 |
| Recruiter | **Bayo Ojo** | Kora engineering manager, sceptical · R5 |
| Candidate | **Amaka Eze** | Graduate · T1 |
| Candidate | **Chidi Nwosu** | Sales rep → product or business analyst · T2 |
| Candidate | **Tobi Adeyemi** | Senior backend engineer, private · T3 |
| Candidate | **Grace Okon** | Care assistant on a phone with a weak connection · T4 |
| Candidate | **Zara Mensah** | Backend engineer, sceptical · T5 |

**Legend.**
- ✓ exists and is reused.
- ◐ exists, but is extended or rebuilt.
- ＋ is new in this phase.

Every curveball is listed with its category:
- **[mind]**: the user changes their mind.
- **[info]**: information is unavailable, conflicting, missing or revoked.
- **[recover]**: interruption, navigation, permission or execution recovery.

## Recruiter journeys

### R1: The confused first-time employer (Funmi)

**Flow**
1. Signup ＋ and verify ＋
2. Work mode ＋
3. Q personalisation ＋
4. Organisation setup ◐ (from the conversation, not a form-first flow)
5. Policies ◐
6. Co
… [3080 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:20

Now loading the mandated skills.

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

- 🔧 `Bash`: Read skill reference files

  <details><summary>result</summary>

```
# Error Prevention and Recovery

Error prevention hierarchy, undo patterns, inline validation, empty states, loading patterns, and recovery flows. Based on Cooper's About Face and Saffer's Microinteractions.

---

## The Error Prevention Hierarchy

Address errors in this order — prevention is always cheaper than recovery:

| Level | Approach | Example | Cost to User |
|-------|----------|---------|-------------|
| **1. Eliminate** | Remove the possibility of the error entirely | Auto-save eliminates "forgot to save." Dropdown eliminates misspelled country names | Zero |
| **2. Prevent** | Design inputs that make errors impossible | Date picker prevents invalid dates. Slider prevents out-of-range values | Zero |
| **3. Detect early** | Catch errors as they happen, before submission | Inline validation on field blur. Real-time format checking | Low |
| **4. Recover gracefully** | When errors occur, make recovery easy and painless | Undo after delete. Auto-correct with "Did you mean...?" | Medium |
| **5. Explain clearly** | If recovery requires user action, explain exactly what to do | Inline error with specific message + highlight + fix suggestion | Medium-High |
| **6. Diagnose** | Help users understand what went wrong and why | Detailed error page with troubleshooting steps | High |

Never design at Level 5-6 when you could design at Level 1-2.

---

## Inline Validation

### When to Validate

| Timing | How It Works | Best For |
|--------|-------------|----------|
| **On bl
… [11016 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:20

Now the code. Let me read my area files.

- 🔧 `Bash`: Read hire-a model and routes

  <details><summary>result</summary>

```
<persisted-output>
Output too large (36.7KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bldqp5ebl.txt

Preview (first 2KB):
// Routes for R1 (Funmi) and R5 (Bayo). Owned by this area (see journeys/BUILD-BRIEF.md).
import type { ReactNode } from 'react';
import { registerRoute } from './registry';
import { OrgOnly } from './guard';
import { registerHomeSection, registerRecruiterHome } from './entry';
import { actorOf } from '../mock/world';
import { registerRef } from '../q/refs';
import { MandateIntake } from '../screens/MandateIntake';
import { Sourcing } from '../screens/Sourcing';
import { Memory } from '../screens/Memory';
import { RoleDetail, RolesList } from '../journeys/hire-a/Roles';
import { Audit } from '../journeys/hire-a/Audit';
import { FounderHome, WaitingOnYou } from '../journeys/hire-a/Home';
import { BriefRef, ConflictRef, MemoryRef } from '../journeys/hire-a/ui';
import { isFounder } from '../journeys/hire-a/model';
import '../styles/hire-a.css';

const legacy = (n: ReactNode) => <div className="ds-legacy" style={{ minHeight: '100vh' }}>{n}</div>;

registerRoute({ path: '/r/mandate', side: 'recruiter', label: 'the role brief', render: () => <OrgOnly orgId="org_kora" what="Kora Pay’s hiring">{legacy(<MandateIntake />)}</OrgOnly> });
registerRoute({ path: '/r/sourcing', side: 'recruiter', label: 'the search', render: () => <OrgOnly orgId="org_kora" what="Kora Pay’s hiring">{legacy(<Sourcing />
… [708 more characters trimmed]
```
  </details>

- 🔧 `Read`: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bldqp5ebl.txt

  <details><summary>result</summary>

```
1	// Routes for R1 (Funmi) and R5 (Bayo). Owned by this area (see journeys/BUILD-BRIEF.md).
2	import type { ReactNode } from 'react';
3	import { registerRoute } from './registry';
4	import { OrgOnly } from './guard';
5	import { registerHomeSection, registerRecruiterHome } from './entry';
6	import { actorOf } from '../mock/world';
7	import { registerRef } from '../q/refs';
8	import { MandateIntake } from '../screens/MandateIntake';
9	import { Sourcing } from '../screens/Sourcing';
10	import { Memory } from '../screens/Memory';
11	import { RoleDetail, RolesList } from '../journeys/hire-a/Roles';
12	import { Audit } from '../journeys/hire-a/Audit';
13	import { FounderHome, WaitingOnYou } from '../journeys/hire-a/Home';
14	import { BriefRef, ConflictRef, MemoryRef } from '../journeys/hire-a/ui';
15	import { isFounder } from '../journeys/hire-a/model';
16	import '../styles/hire-a.css';
17	
18	const legacy = (n: ReactNode) => <div className="ds-legacy" style={{ minHeight: '100vh' }}>{n}</div>;
19	
20	registerRoute({ path: '/r/mandate', side: 'recruiter', label: 'the role brief', render: () => <OrgOnly orgId="org_kora" what="Kora Pay’s hiring">{legacy(<MandateIntake />)}</OrgOnly> });
21	registerRoute({ path: '/r/sourcing', side: 'recruiter', label: 'the search', render: () => <OrgOnly orgId="org_kora" what="Kora Pay’s hiring">{legacy(<Sourcing />)}</OrgOnly>, nav: { group: 'Hiring', label: 'Search', icon: 'search', order: 13, orgKind: 'EMPLOYER', orgIds: ['org_kora'] } });
22	regis
… [37511 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find privacy functions

  <details><summary>result</summary>

```
90:    evidence: merged('evidence', [...EVIDENCE.map((e) => ({ ...e, origin: 'SEED' as const, verification: e.verified ? 'VERIFIED' as const : 'UNVERIFIED' as const })), ...EXTRA_EVIDENCE]),
183:/** The candidate's discovery rule (set on their Passport; default: verified employers only, no agencies). */
186:export function relationshipWith(w: World, pid: string, orgId: string) {
193:export function canDiscover(w: World, pid: string, orgId: string) {
197:  if (d.who === 'VERIFIED_EMPLOYERS') return o.kind === 'EMPLOYER' && o.verified.domain && o.verified.registry === 'VERIFIED';
198:  return o.verified.domain;
201:export function canSeeCandidate(w: World, pid: string, orgId: string) {
203:  return relationshipWith(w, pid, orgId) || canDiscover(w, pid, orgId);
205:/** What an organisation may read. Shared items follow the explicit share; public items need canSeeCandidate. */
208:  const seen = canSeeCandidate(w, personId, viewerOrgId);
state/domain.ts:22:export interface Org {
state/domain.ts:24:  verified: { domain: boolean; registry: 'VERIFIED' | 'PENDING' | 'NONE' };
../../contracts/talent.ts:38:  verified: boolean;
24:  verified: { domain: boolean; registry: 'VERIFIED' | 'PENDING' | 'NONE' };
```
  </details>

- 🔧 `Bash`: Read privacy rules

  <details><summary>result</summary>

```
export const personOf = (w: World, id: string) => w.people.find((p) => p.personId === id);
export const useActor = () => useWorld((w) => actorOf(w));
/** Simulated "now" (the clock can be moved forward for "three weeks later"). */
export const simNow = (w: World) => new Date(new Date(w.session.now).getTime() + w.session.offsetDays * 864e5);

/** What an organisation may see of a person's Passport: shared items only, never practice, never revoked. */
// ---------------- Candidate privacy: one policy for search, profiles, Q's tools, caches and artifacts ----------------
type DiscoveryRule = { who: 'ANYONE_VERIFIED' | 'VERIFIED_EMPLOYERS' | 'NOBODY'; hideFrom: string[] };
/** The candidate's discovery rule (set on their Passport; default: verified employers only, no agencies). */
export const discoveryRule = (w: World, pid: string): DiscoveryRule => (w.areas['talent-b'] as { discovery?: Record<string, DiscoveryRule> } | undefined)?.discovery?.[pid] ?? { who: 'VERIFIED_EMPLOYERS', hideFrom: [] };
/** An explicit relationship the candidate created: applied, shared something, or registered with an agency. */
export function relationshipWith(w: World, pid: string, orgId: string) {
  const c = w.consents[pid];
  if (c?.registeredWith?.includes(orgId)) return true;
  if (w.applications.some((a) => a.personId === pid && w.jobs.find((j) => j.id === a.jobId)?.orgId === orgId)) return true;
  return w.evidence.some((e) => e.ownerId === pid && e.visibility === 'SHARED_WITH' && e.sharedWith
… [3385 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check consent defaults

  <details><summary>result</summary>

```
31:  consents: Record<string, Consent>;
76:    consents: Object.fromEntries(people.map((p) => { const c = consentFor(p.personId); const reg = SEEDS.flatMap((x) => x.registrations ?? []).filter((r) => r.personId === p.personId).map((r) => r.orgId); return [p.personId, reg.length ? { ...c, registeredWith: reg } : c]; })),
187:  const c = w.consents[pid];
194:  if (!w.consents[pid]?.discoverable) return false;
202:  if (w.consents[pid]?.withdrawnFrom.includes(orgId)) return false;
207:  if (w.consents[personId]?.withdrawnFrom.includes(viewerOrgId)) return [];
mock/world.ts:194:  if (!w.consents[pid]?.discoverable) return false;
state/seed.ts:106:export const consentFor = (personId: string): Consent => ({ personId, discoverable: personId !== 'p_grace', withdrawnFrom: [], notifications: { email: true, sms: personId === 'p_grace', inApp: true, digest: 'WEEKLY' }, lite: false });
state/domain.ts:66:export interface Consent { personId: string; discoverable: boolean; withdrawnFrom: string[]; registeredWith?: string[]; notifications: { email: boolean; sms: boolean; inApp: boolean; digest: 'DAILY' | 'WEEKLY' | 'OFF' }; lite: boolean }
export interface Interview { id: string; orgId: string; mandateId: string; personId: string; eventId?: string; panel: string[]; status: 'PLANNING' | 'INVITED' | 'CONFIRMED' | 'DONE' | 'CANCELLED'; feedback: Feedback[]; candidateFeedback?: string; disputed?: { by: string; reason: string; state: 'OPEN' | 'RESOLVED' } }

export interface Job {
  id: string; o
… [426 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Outline skills file

  <details><summary>result</summary>

```
7:import { allSkills, appendQ, pushUndo, registerOp, registerSkill } from '../core/engine';
15:  POOL, revertTo, revise, ROLE_LABEL, ROLES, rolesIn, round5k, runSearch, scopeOf, simIso, startSourcingWithQ, titleFor, whoCan, dayLabel, timeLabel, poolFor, levelOf,
34:const setIntake = (w: World, a: Actor, patch: Partial<HAIntake>) => { const s = hireA(w); s.intake[a.id] = { ...(s.intake[a.id] ?? { step: 'business', updatedAt: '' }), ...patch, updatedAt: simIso(w) }; };
39:function rolesFrom(text: string): RoleKey[] {
47:function parseHours(norm: string): { hours?: 'FULL' | 'PART'; days?: number } {
57:function question(step: IntakeStep, st: HAIntake): ReplyMsg | null {
67:function proposeText(_st: HAIntake, r: RoleKey) {
72:function createOrg(w: World, a: Actor, text: string, norm: string) {
79:  if (!w.orgs.some((o) => o.id === id)) w.orgs.push({ id, name, kind: 'EMPLOYER', industry, size: '1–10 people', city, verified: { domain: false, registry: 'NONE' }, delegation: 'APPROVE_EACH_SEND', setup: { done: true, step: 5 }, guidelines: ['Approve each outgoing message', 'Ask job-related questions only'] });
87:function draftNow(w: World, a: Actor, st: HAIntake, id: string): { frame: QFrame } {
96:    setIntake(w, a, { step: 'budgetfix' });
105:  setIntake(w, a, { step: 'review' });
109:function reviewMsg(w: World, a: Actor, m: MandateX, lead: string) {
115:function applyBudget(w: World, a: Actor, id: string, how: string, amount?: number) {
122:  setIntake(w, a, { step: 'review', ho
… [8898 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read skills file part 1

  <details><summary>result</summary>

```
// Q skills for the hire-a area: R1 (Funmi, a first-time employer who doesn't know what she needs) and
// R5 (Bayo, a sceptical hiring manager), plus Kora's Senior Backend intake moved out of the old embedded
// conversation on /r/mandate and /r/sourcing. Everything here is reachable by typing to the global Q in
// imperfect language; pages only show and refine the same state.
import { actorOf, emit, now, orgOf, personOf, simNow, uid, visibleEvidence, type World } from '../../mock/world';
import type { Actor, CalEvent, MandateX, Msg, QAction, QFrame, QMsg, Thread } from '../../state/domain';
import { allSkills, appendQ, pushUndo, registerOp, registerSkill } from '../core/engine';
import { findTerm, GLOSSARY } from '../core/glossary';
import { anyOf, near } from '../core/nlu';
import type { QCtx, QReply, ReplyMsg } from '../core/types';
import { hireA, readA, type HAIntake, type IntakeStep, type RoleKey } from '../../state/areas/hire-a';
import { MANDATE } from '../../mock/fixtures';
import {
  actorName, band, can, createDraft, curV, ensureSeed, firstName, hoursText, isFounder, k, LEVEL_LABEL, listNames, naira, orgMandates, payText, pickMandate,
  POOL, revertTo, revise, ROLE_LABEL, ROLES, rolesIn, round5k, runSearch, scopeOf, simIso, startSourcingWithQ, titleFor, whoCan, dayLabel, timeLabel, poolFor, levelOf,
} from '../../journeys/hire-a/model';

type Out = Omit<QMsg, 'id' | 'at' | 'who'>;
const qsay = (w: World, a: Actor, m: Omit<Out, 'engine'>) => appendQ(w, a.id, { who: 
… [10856 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read skills file part 2

  <details><summary>result</summary>

```
<persisted-output>
Output too large (31.5KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bjnz0b6wp.txt

Preview (first 2KB):
function applyChange(c: QCtx): QReply | null {
  const st = intakeOf(c.w, c.actor);
  const roles = rolesFrom(c.norm).filter((r) => r !== st.roleKey);
  const hrs = parseHours(c.norm);
  const money = c.ents.money;
  const place = c.text.match(/\bin ([A-Z][a-zA-Z]+)/)?.[1];
  if (!roles.length && !hrs.hours && !money && !place) return null;
  const role = roles[0] ?? st.roleKey;
  const next: Partial<HAIntake> = { prevRoleKey: roles.length ? st.roleKey : st.prevRoleKey, roleKey: role, ...(hrs.hours ? hrs : {}), ...(money ? { budget: money } : {}) };
  if (role && roles.length && !hrs.hours && !ROLES[role].partOk) next.hours = 'FULL';
  const merged = { ...st, ...next };
  const kept = [st.city && `${st.city}`, merged.hours && hoursText(merged.hours, merged.days), merged.budget && `${naira(merged.budget)} a month`].filter(Boolean) as string[];
  const lead = roles.length ? `No problem: switching from ${st.roleKey ? `a ${ROLES[st.roleKey].label}` : 'that'} to a ${ROLES[role!].label}. I’ve kept what still applies${kept.length ? ` (${kept.join(', ')})` : ''}.` : 'Got it, I’ve changed that.';
  // No draft yet: carry on the intake from wherever it is.
  if (!st.mandateId || !findM(c.w, st.mandateId)) {
    const step: IntakeStep = !merged.roleKey ? 'role' : !merged.hours && ROLES[merged.roleK
… [713 more characters trimmed]
```
  </details>

- 🔧 `Read`: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bjnz0b6wp.txt

  <details><summary>result</summary>

```
1	function applyChange(c: QCtx): QReply | null {
2	  const st = intakeOf(c.w, c.actor);
3	  const roles = rolesFrom(c.norm).filter((r) => r !== st.roleKey);
4	  const hrs = parseHours(c.norm);
5	  const money = c.ents.money;
6	  const place = c.text.match(/\bin ([A-Z][a-zA-Z]+)/)?.[1];
7	  if (!roles.length && !hrs.hours && !money && !place) return null;
8	  const role = roles[0] ?? st.roleKey;
9	  const next: Partial<HAIntake> = { prevRoleKey: roles.length ? st.roleKey : st.prevRoleKey, roleKey: role, ...(hrs.hours ? hrs : {}), ...(money ? { budget: money } : {}) };
10	  if (role && roles.length && !hrs.hours && !ROLES[role].partOk) next.hours = 'FULL';
11	  const merged = { ...st, ...next };
12	  const kept = [st.city && `${st.city}`, merged.hours && hoursText(merged.hours, merged.days), merged.budget && `${naira(merged.budget)} a month`].filter(Boolean) as string[];
13	  const lead = roles.length ? `No problem: switching from ${st.roleKey ? `a ${ROLES[st.roleKey].label}` : 'that'} to a ${ROLES[role!].label}. I’ve kept what still applies${kept.length ? ` (${kept.join(', ')})` : ''}.` : 'Got it, I’ve changed that.';
14	  // No draft yet: carry on the intake from wherever it is.
15	  if (!st.mandateId || !findM(c.w, st.mandateId)) {
16	    const step: IntakeStep = !merged.roleKey ? 'role' : !merged.hours && ROLES[merged.roleKey].partOk ? 'hours' : !merged.budget ? 'budget' : 'review';
17	    if (step === 'review') {
18	      const id = uid('m');
19	      return { msgs: [], ef
… [31847 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read R1 script and review scripts

  <details><summary>result</summary>

```
// R1 · Funmi, a confused first-time employer (Crumb & Co bakery). Starts signed out, signs up, and works out
// who to hire entirely by typing to the global Q in imperfect language. Curveballs: changes the role midway
// (shop assistant → part-time bookkeeper), doesn't know "mandate", budget below market, clicks "Discard draft"
// by mistake then says "undo that", leaves and comes back the next day ("where was I?"), and checks that
// Kora Pay's pipeline stays invisible. Usage: node R1.mjs [port] [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const PORT = process.argv[2] || '5181';
const ONLY = (process.argv[3] || 'd,m').split(',');
const OUT = fileURLToPath(new URL('../../../captures/cx/R1/', import.meta.url)); mkdirSync(OUT, { recursive: true });
const BASE = `http://localhost:${PORT}/`;
const b = await pw.chromium.launch();
const errors = []; const results = [];
const step = (v, name, ok, detail = '') => { results.push({ v, name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} [${v}] ${name}${detail && !ok ? ` · ${detail}` : ''}`); };

for (const [v, vp, dpr] of [['d', { width: 1440, height: 900 }, 1], ['m', { width: 390, height: 844 }, 2]].filter(([x]) => ONLY.includes(x))) {
  const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: dpr });
  const page = await ctx.newPage();
  page.on('pageerror', (e) => errors.push(`${v}: ${e}`));
  page.on('console', (m) => {
… [19635 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Start dev server on 5181
- 🔧 `Bash`: Run R1 and R5 baseline (desktop)

  <details><summary>result</summary>

```
200
```
  </details>


  <details><summary>result</summary>

```
PASS [d] versions view lists v1–v3
PASS [d] old version stays readable
PASS [d] [recover] wrong click discards the draft
PASS [d] Q confirms what will be undone
PASS [d] [recover] undo restores the draft exactly
PASS [d] home shows where she is
PASS [d] [recover] Q resumes from where she stopped
PASS [d] proactive: draft unapproved for over a day
PASS [d] approved after explicit approval
FAIL [d] simulated search finds bookkeepers only
PASS [d] Kora pipeline invisible to Crumb & Co
FAIL [d] shortlist by name
FAIL [d] Q proposes times and asks for approval · Nobody is on the shortlist yet. Pick who you want to meet first, for example “shortlist the top 2”.
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-thread .ds-chip').filter({ hasText: /Hold the times/ }).last()[22m

    at chip (/home/user/neo/talent-q-design/qa/scripts/journeys/R1.mjs:33:133)
    at async file:///home/user/neo/talent-q-design/qa/scripts/journeys/R1.mjs:131:3 {
  log: [
    "  - waiting for locator('.ds-thread .ds-chip').filter({ hasText: /Hold the times/ }).last()"
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
PASS [d] his choice recorded; both sources kept
PASS [d] who changed the panel → Ngozi, with when
PASS [d] audit filtered to the panel change
PASS [d] what did you do yesterday → Q’s own actions
PASS [d] audit filtered to Q, yesterday
PASS [d] audit is Kora-only (no Crumb & Co)
ERRORS []
PA
… [25 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Capture current pages

  <details><summary>result</summary>

```
p_tobi_c_memory.png
u_ada_r_audit.png
u_ada_r_mandate.png
u_ada_r_memory.png
u_ada_r_roles.png
u_ada_r_sourcing.png
u_dele_r_agency_mandate_m_ops.png
u_funmi_r_home.png
u_funmi_r_roles.png
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/pc-0.png

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop:
p_tobi_c_memory.png
u_ada_r_audit.png
u_ada_r_compare.png
u_ada_r_interviews.png
u_ada_r_mandate.png
u_ada_r_memory.png
u_ada_r_people_p_tobi.png
u_ada_r_roles.png
u_ada_r_sourcing.png
u_funmi_r_home.png
u_funmi_r_roles.png

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/phone:
p_tobi_c_memory.png
u_ada_r_audit.png
u_ada_r_compare.png
u_ada_r_interviews.png
u_ada_r_mandate.png
u_ada_r_memory.png
u_ada_r_people_p_tobi.png
u_ada_r_roles.png
u_ada_r_sourcing.png
u_funmi_r_home.png
u_funmi_r_roles.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_funmi_r_home.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_roles.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_audit.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_memory.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:25

[Image: original 1440x2572, displayed at 1120x2000. Multiply coordinates by 1.29 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_mandate.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/desktop/u_ada_r_sourcing.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Read Mandate and Sourcing screens

  <details><summary>result</summary>

```
// P3 · SC-027 Create mandate, SC-028 Hiring intake, SC-029 Structured editor.
// The brief is the canvas. Q's intake questions now live in the one global conversation (skill
// hire-a.kora.intake); this page shows and edits the same mandate. Approval binds to this exact version.
import { update, useWorld, actorOf, log, emit } from '../mock/world';
import { Canvas } from '../ds/Workspace';
import { Glyph } from '../ds/Glyph';
import { Field, Label, Segmented } from '../ui/kit';
import { Link } from '../ui/router';
import { runAction } from '../q/core/engine';
import { prefillQ } from '../q/QThread';
import { openQ } from '../journeys/hire-a/ui';
import type { Mandate } from '@contracts';

export function MandateIntake() {
  const m = useWorld((w) => w.mandate);
  const a = useWorld((w) => actorOf(w));
  const intake = useWorld((w) => (w.areas['hire-a'] as { koraIntake?: { step: string } } | undefined)?.koraIntake?.step);
  if (a.orgId !== 'org_kora') return (
    <Canvas title="Your role briefs live in Roles" kicker="Role brief" open onClose={openQ}>
      <section className="ds-sheet hire-a-empty"><p style={{ margin: 0 }}>This page holds another organisation’s brief, so it isn’t shown to you. Your own briefs are in Roles.</p><Link to="/r/roles" className="ds-btn primary">Open your roles</Link></section>
    </Canvas>
  );
  const approved = m.status !== 'DRAFT';
  const set = (patch: Partial<Mandate>) => update((d) => { Object.assign(d.mandate, patch); emit(d, a.id, 'mandate
… [11307 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/u_ada_r_mandate.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Read Home, ui, css

  <details><summary>result</summary>

```
// Founder home (R1): where Funmi is in hiring, in plain steps, with the one next thing to do. It reads the
// same state Q uses for "where was I?", so leaving and coming back always lands in the right place.
// Plus a "waiting on you" block on Kora's home for hiring managers (R5): drafts to approve, sources to check.
import { useEffect } from 'react';
import { actorOf, useWorld } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { Glyph } from '../../ds/Glyph';
import { Link } from '../../ui/router';
import { runAction } from '../../q/core/engine';
import { readA } from '../../state/areas/hire-a';
import { curV, dayLabel, ensureSeeded, orgMandates, payText } from './model';
import { openQ } from './ui';

const say = (text: string) => void runAction({ label: text, act: { t: 'say', text } });

export function FounderHome() {
  const w = useWorld((x) => x);
  const a = actorOf(w);
  const org = w.orgs.find((o) => o.id === a.orgId);
  const st = readA(w).intake[a.id];
  const m = st?.mandateId ? w.mandates.find((x) => x.id === st.mandateId) : orgMandates(w, a)[0];
  const found = m ? readA(w).search[m.id]?.found.length ?? 0 : 0;
  const sl = m ? w.pipeline.filter((e) => e.mandateId === m.id && e.stage === 'SHORTLISTED').length : 0;
  const holds = m ? w.calendar.filter((e) => e.mandateId === m.id && e.status === 'HOLD').length : 0;
  const steps = [
    { label: 'Tell Q about your business', done: !!org, detail: org ? `${org.name} · ${org.city}` : 'One
… [13150 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Roles and Audit

  <details><summary>result</summary>

```
// /r/roles and /r/roles/:id: an organisation's role briefs (mandates), scoped to the signed-in person's
// organisation. The brief reads in plain language; versions stay readable; approve, discard and undo go
// through the same Q ops as the conversation, so the page and Q never disagree.
import { useEffect, useState } from 'react';
import { actorOf, personOf, useWorld, visibleEvidence, type World } from '../../mock/world';
import { Canvas } from '../../ds/Workspace';
import { Glyph } from '../../ds/Glyph';
import { Link } from '../../ui/router';
import { runAction, useViewState } from '../../q/core/engine';
import { prefillQ } from '../../q/QThread';
import { readA } from '../../state/areas/hire-a';
import type { MandateX } from '../../state/domain';
import { STAGE_LABEL } from '../../state/domain';
import { activeLevel, actorName, band, can, curV, dayLabel, ensureSeeded, hoursText, LEVEL_LABEL, naira, orgMandates, payText, POOL, STATUS_PLAIN, levelOf, ROLE_LABEL, whoCan } from './model';
import { evidenceGlyph, openQ } from './ui';
import { CONFLICTS } from '../../q/skills/hire-a';

const say = (text: string) => void runAction({ label: text, act: { t: 'say', text } });
const doOp = (label: string, op: string, args: Record<string, unknown>) => void runAction({ label, act: { t: 'do', op, args } });

export function RolesList() {
  useEffect(() => { ensureSeeded(); }, []);
  const w = useWorld((x) => x);
  const a = actorOf(w);
  const org = w.orgs.find((o) => o.id === a.orgI
… [22598 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read motion tokens, Canvas, ds classes

  <details><summary>result</summary>

```
// Motion tokens (interaction-design skill: feedback 100–200 ms, orientation 200–400 ms, enter slower than
// exit, decelerate in / accelerate out, nothing functional over 500 ms). Every animation in the shell and
// shared components takes its timing from here; reduced motion is handled globally by MotionConfig.
export const DUR = { fast: 0.1, normal: 0.2, slow: 0.3 } as const;
export const EASE = { standard: [0.2, 0, 0, 1], enter: [0, 0, 0.2, 1], exit: [0.4, 0, 1, 1] } as const;
/** Something new arriving in place (a message, a card, a page): rise 6 px and fade in. */
export const arrive = { initial: { opacity: 0, y: 6 }, animate: { opacity: 1, y: 0, transition: { duration: DUR.normal, ease: EASE.enter } }, exit: { opacity: 0, transition: { duration: DUR.fast, ease: EASE.exit } } } as const;
168:export function Canvas<V extends string>({ title, kicker, views, view, setView, versions = [], onVersion, building, open, onClose, children, qLine, aside }: {
169-  title: string; kicker: ReactNode; views?: ViewDef<V>[]; view?: V; setView?: (v: V) => void; versions?: Version<V>[]; onVersion?: (v: Version<V>) => void;
170-  building?: boolean; open: boolean; onClose: () => void; children: ReactNode; qLine?: string; aside?: ReactNode;
171-}) {
172-  const nestedShell = useContext(InShell);
173-  const narrow = useNarrow() && !nestedShell;
174-  const ref = useRef<HTMLElement>(null);
175-  useEffect(() => { if (narrow && open) ref.current?.focus(); }, [narrow, open]);
176-  if (narrow 
… [3157 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:25

Now let me look at the journey-state captures (people, propose) and phone captures.

- 🔧 `Bash`: List R1/R5 captures

  <details><summary>result</summary>

```
d-01-signup.png
d-02-home-welcome.png
d-03-draft-v1.png
d-04-draft-v1-canvas.png
d-05-budget-below.png
d-06-version-v1.png
d-07-back-next-day.png
d-08-people.png
d-09-people-canvas.png
d-10-propose.png
d-11-handoff.png
d-12-roles.png
d-13-audit.png
m-01-signup.png
m-02-home-welcome.png
m-03-draft-v1.png
m-04-draft-v1-canvas.png
m-05-budget-below.png
m-06-version-v1.png
m-07-back-next-day.png
m-08-people.png
m-09-people-canvas.png
m-10-propose.png
m-11-handoff.png
m-12-roles.png
m-13-audit.png
d-01-home.png
d-02-kora-brief.png
d-03-kora-search.png
d-04-contradiction.png
d-05-refusal-offer.png
d-06-memory-source.png
d-07-memory-page.png
d-08-conflict.png
d-09-people.png
d-10-audit-panel.png
d-11-audit-q.png
d-12-audit-all.png
m-01-home.png
m-02-kora-brief.png
m-03-kora-search.png
m-04-contradiction.png
m-05-refusal-offer.png
m-06-memory-source.png
m-07-memory-page.png
m-08-conflict.png
m-09-people.png
m-10-audit-panel.png
m-11-audit-q.png
m-12-audit-all.png
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-04-draft-v1-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R5/d-09-people.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-05-budget-below.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Compose phone captures into contact sheet

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/phone-sheet.png

  <details><summary>result</summary>

```
File does not exist. Note: your current working directory is /home/user/neo/talent-q-design/prototype/src.
```
  </details>

- 🔧 `Bash`: List scratchpad

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/:
R1.log
R5.log
afr.png
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
batch-R1.log
batch-R2.log
batch-R3.log
batch-R4.log
batch-R5.log
batch-T4.log
batch.files
before-cx
before-extra
before-now
before-r3
bin
bsheet.png
cap
cap.mjs
ch
check.mjs
csheet.png
cur
cx2
dfinal
dir1
dir2
dirs
dom.mjs
dshots
ff
ff2
film
film.log
film2.log
film2.txt
filmout
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
goal.txt
hirea.files
hooktest.mjs
ht
ift
iv.mjs
man
man.mjs
nlu.test.ts
now
ok.mjs
p2.mjs
preview.log
preview4174.log
probe.mjs
probe.png
pv.mjs
r1.out
r4
rec
rec.log
record.txt
restart.sh
review
routes.txt
run.txt
serve.mjs
shared
shot.mjs
shots
shots.mjs
t1-base.log
t2-base.log
talent-b
tb
test-clip.mp4
testreview.mjs
tq2
update_status.py
v2
v3
v4
v5
vf
vf2
vite.hire-a.config.mjs
vite.hirec.mjs
vite.log
vite2.log
vite3.log
ws.mjs
ws2.mjs
wt
wt2
wtdist
wtdist2

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur:
desktop
pc-0.png
phone
phone-sheet.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/cur/phone-sheet.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Read Memory screen

  <details><summary>result</summary>

```
// P12 · SC-133 memory viewer and correction, SC-177 what/why/sources, SC-178 correct/challenge/revoke,
// SC-179 context pack for a task, SC-183 candidate proof of non-sharing.
import { useState } from 'react';
import { MEMORY_LAYERS, MEMORY_LAYER_LABELS, type MemoryItem } from '@contracts';
import { actorOf, emit, log, now, uid, update, useWorld, visibleMemories, type World } from '../mock/world';
import type { Actor } from '../state/domain';
import { Banner, Button, Label, Segmented, Sheet, TextArea, toast } from '../ui/kit';
import { Link } from '../ui/router';

/** What someone said is shown as their words, in sentence case and quoted; everything else as written (critique F8). */
const shown = (m: MemoryItem) => { const t = m.content.trim(); const c = t.charAt(0).toUpperCase() + t.slice(1); return m.truth_class === 'STATED_BY_USER' ? `“${c}”` : c; };
const TRUTH: Record<MemoryItem['truth_class'], string> = { STATED_BY_USER: 'You said this', VERIFIED_FACT: 'Verified', THIRD_PARTY_CLAIM: 'Someone else’s claim', INFERENCE: 'Q inferred this', ORG_POLICY: 'Organisation rule' };
const SCOPE: Record<MemoryItem['visibility_scope'], string> = { PERSONAL_PRIVATE: 'Only you', TEAM: 'Your hiring team', ORGANIZATION: 'Everyone at Kora Pay', SHARED_WITH_EMPLOYER: 'Shared with an employer', CANDIDATE_PRIVATE_PRACTICE: 'Private practice, only the candidate' };

type Task = 'schedule' | 'outreach' | 'compare';
const TASKS: Record<Task, { label: string; keys: string[] }> = {
  schedule: {
… [11718 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find /c/memory route

  <details><summary>result</summary>

```
./q/skills/core.ts:34:  { side: 'candidate', kws: ['memory', 'what you remember', 'what you know about me'], to: '/c/memory', label: 'what Q remembers' },
./q/skills/core.ts:144:        actions: hits.length ? [{ label: 'Forget it', primary: true, act: { t: 'do', op: 'memory.forget', args: { ids: hits.map((h) => h.memory_id) } } }, { label: 'Keep it', act: { t: 'say', text: 'keep it' } }] : [{ label: 'Show what you remember', act: { t: 'nav', to: c.actor.side === 'recruiter' ? '/r/memory' : '/c/memory' } }] }],
./q/skills/talent-b.ts:414:  return { msgs: [reply(`Understood. I won’t suggest ${label} again, for this job or any other. That’s your call to make. I’ve noted it in What Q remembers, where you can remove it if you change your mind.`, { used: ['What Q remembers'], actions: [{ label: 'See what you remember', act: { t: 'nav', to: '/c/memory' } }] })],
./q/skills/talent-b.ts:448:    if (!ms.length) return { msgs: [reply('I can’t find anything I remember that matches that. Here’s everything I keep about you, so you can check.', { actions: [{ label: 'What you remember', act: { t: 'nav', to: '/c/memory' } }] })] };
./q/skills/talent-b.ts:460:    return { msgs: [reply(`I remember ${ms.length} things you’ve told me${ms.length ? `, including: ${ms.slice(0, 3).map((m) => m.text.replace(/\.$/, '')).join('; ')}` : ''}. None of it is shared with employers unless you choose. You can delete any of it.`, { used: ['What Q remembers'] })], nav: { to: '/c/memory', label: 'what Q remembers
… [756 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check candidate memory page usage

  <details><summary>result</summary>

```
10:export function CandidateMemoryPage() {
```
  </details>

- 🔧 `Bash`: Check R5 selectors

  <details><summary>result</summary>

```
44:  step(v, 'home shows what is waiting on Bayo', /Waiting on you/i.test(await page.locator('#ds-content').innerText()) && /Backend Engineer, Payouts/.test(await page.locator('#ds-content').innerText()));
46:  step(v, 'proactive: draft waiting on him for over a day', await page.locator('.ds-suggest').filter({ hasText: /Payouts.*has been a draft since/ }).count() > 0);
53:  step(v, 'no second conversation on the brief page', (await page.locator('.split-conv, .ds-canvas .ds-compose').count()) === 0);
76:  let c = await canvas();
82:  c = await canvas();
124:  c = await page.locator('#ds-content').innerText();
142:  c = await canvas();
147:  c = await canvas();
151:  await page.getByRole('button', { name: 'Clear filters' }).click().catch(() => {});
152:  c = await canvas();
```
  </details>

- 🔧 `Bash`: Read R5 assertions

  <details><summary>result</summary>

```
await ask('ok find people for payouts', 900);
  w = await world();
  step(v, 'search for Payouts runs (Kora pool)', (w.areas['hire-a'].search.m_payouts?.found ?? []).length === 7 && (await route()) === '/r/roles/m_payouts');

  // ---- [mind] Contradictory instructions ----
  await ask('only seniors pls');
  let c = await canvas();
  step(v, 'only seniors applied and visible', !/Emeka Nnadi/.test(c) && /hidden by your “only seniors”/.test(c));
  await ask('why are there no juniors??');
  step(v, '[mind] Q points out the contradiction and asks which to keep', /contradicts that/.test(await lastQ()) && (await lastKind()) === 'question');
  await shot('contradiction', true);
  await ask('ok include them');
  c = await canvas();
  step(v, 'his choice is applied (juniors back, by level)', /Emeka Nnadi/.test(c) && /Junior/.test(c));
  await ask('i want someone really senior but cheap');
  step(v, '[mind] senior-but-cheap trade-off named', /pull against each other/.test(await lastQ()));
  await chip(/Senior, keep the pay band/);

  // ---- [recover] Actions outside his role ----
  await ask('send tobi an offer today');
  step(v, '[recover] offer refused, names who can', (await lastKind()) === 'refusal' && /Ada Okafor \(recruiter\)/.test(await lastQ()) && /Ngozi Eze \(admin\)/.test(await lastQ()), await lastQ());
  await shot('refusal-offer', true);
  await chip(/^Ask Ada$|^Ask Ngozi$/);
  w = await world();
  step(v, 'request reaches the colleague’s Q', w.areas['hire-a'].requests.len
… [4717 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check Funmi actor and signup

  <details><summary>result</summary>

```
state/seed.ts:9:  { id: 'u_funmi', name: 'Funmi Adebayo', first: 'Funmi', initials: 'FA', side: 'recruiter', title: 'Founder', timezone: 'Africa/Lagos', journey: 'R1', email: 'funmi@crumbandco.example', signedUp: false },
state/seed.ts:107:export const defaultPrefs = (a: Actor): QPrefs => ({ proactive: 'NORMAL', voice: a.id !== 'p_grace', plain: a.id === 'u_funmi' || a.id === 'p_grace' });
142:        <ol aria-label="Steps" style={{ display: 'flex', gap: 6, listStyle: 'none', padding: 0, margin: 0 }}>{['Account', 'Verify', 'You', 'Q'].map((s, i) => <li key={s} className="t14" style={{ flex: 1, borderTop: `3px solid ${['account', 'verify', 'mode', 'q'].indexOf(step) >= i ? 'var(--ink)' : 'var(--rule)'}`, paddingTop: 6 }}>{s}</li>)}</ol>
159:                <div className="ds-field"><label htmlFor="su-code">Code</label><input id="su-code" className="ds-input" inputMode="numeric" value={code} onChange={(e) => setCode(e.target.value)} aria-invalid={!!err} aria-describedby={err ? 'su-err2' : undefined} autoComplete="one-time-code" />{err && <span id="su-err2" className="t14" style={{ color: 'var(--risk)' }} role="alert">{err}</span>}</div>
160:                <button type="submit" className="ds-btn primary">Verify</button>
```
  </details>

- 🔧 `Bash`: Read proactive rules and refs

  <details><summary>result</summary>

```
// Proactive rules for R1 and R5, read from real state, each with a stated reason.
//  · a draft brief left unapproved for a day or more (for its author, or for a hiring manager it waits on)
//  · a budget below the usual range for the role and hours (high priority)
//  · a shortlist ready but no interview times proposed
//  · two sources disagreeing about a shortlisted person (hiring managers)
import { simNow, type World } from '../../mock/world';
import type { Actor } from '../../state/domain';
import { registerRule } from '../core/proactive';
import { readA } from '../../state/areas/hire-a';
import { band, can, curV, dayLabel, ensureSeeded, isFounder, lastAt, naira, needsSeed, orgMandates, ROLES, hoursText } from '../../journeys/hire-a/model';

// Kora's history (audit events, Bayo's remembered preference) is added once to whatever world is loaded,
// including after "Reset the demo". The suggestions engine evaluates on every change, so it notices first.
let pending = false;
const seedSoon = (w: World) => { if (!pending && needsSeed(w)) { pending = true; queueMicrotask(() => { pending = false; ensureSeeded(); }); } };

registerRule({
  id: 'hire-a.draft-stale', side: 'recruiter', priority: 'normal',
  evaluate: (w: World, a: Actor) => {
    seedSoon(w);
    const t = simNow(w).getTime();
    return orgMandates(w, a).filter((m) => m.status === 'DRAFT' && can(a, 'approve_brief') && (isFounder(a) ? m.createdBy === a.id : a.role === 'HIRING_MANAGER' && m.createdBy !== a.id) &&
… [3852 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check Job seed format and reply types

  <details><summary>result</summary>

```
72:  { id: 'j_kora_backend', orgId: 'org_kora', mandateId: 'm_backend', title: 'Senior Backend Engineer', location: 'Lagos', workMode: 'HYBRID', pay: '₦2.4m–₦3.1m / month', posted: '2026-10-22', status: 'OPEN', needs: ['Payments systems', 'Go in production', 'Postgres at scale'], signals: { domainVerified: true, registryVerified: true, recruiterActive: true, replies: 'Usually replies within 3 days' } },
84:  { id: 'a_zara_kora', jobId: 'j_kora_backend', personId: 'p_zara', status: 'VIEWED', shared: ['e_zara_api', 'e_zara_pg'], timeline: [{ at: '2026-10-26', text: 'You applied', by: 'YOU' }, { at: '2026-10-27', text: 'Kora Pay viewed your application', by: 'EMPLOYER' }], lastEmployerActivity: '2026-10-27' },
22:export type ReplyMsg = Omit<QMsg, 'id' | 'at' | 'who' | 'engine'> & { who?: 'q' | 'system' };
23-
24-export interface QReply {
25:  msgs: ReplyMsg[];
26-  /** Mutations applied in the same store update as the reply (atomic). */
27-  effects?: (w: World, actor: Actor) => void;
28-  /** Navigate after replying. Label is used for "go back" and the nav history. */
29-  nav?: { to: string; label: string };
30-  /** undefined: keep the current frame; null: clear it; QFrame: replace it. */
31-  frame?: QFrame | null;
```
  </details>

- 🔧 `Bash`: Find motion atlas IDs

  <details><summary>result</summary>

```
MOTION-COVERAGE.csv
STATE-MACHINES.md
MO-001,Q orb idle,app:idle,Q Home and interview,Static gold icon,PROTOTYPED,/r/home,,Driven by a
MO-002,Q listens,voice:recording,Voice interview,Listening text and transcript,PROTOTYPED,/galle
MO-003,Q thinks,run:accepted,All run views,Accepted task label,PROTOTYPED,/r/mandate,Shown in ca
MO-004,Q speaks,voice:audio-out,Voice/video,Captions,RESEARCHED,,,
MO-005,Q interrupted,voice:interrupted,Voice/video,State text,RESEARCHED,,,
MO-006,Q disconnected,transport:lost,Any run,Connection lost banner,PROTOTYPED,/r/sourcing,Shown
MO-007,Q reconnected,transport:restored,Any run,Connected message,PROTOTYPED,/r/sourcing,Shown i
MO-008,Task plan grows,plan:created,Q planner,Static checklist,PROTOTYPED,/r/plan,captures/journ
MO-009,Parallel agents start,task:spawned,Run explorer,Task list,PROTOTYPED,/r/sourcing,,Driven 
MO-010,Research source found,source:retrieved,Research explorer,Source list update,PROTOTYPED,/r
MO-011,First candidate arrives,candidate:retrieved,Explore Talent,Instant card,PROTOTYPED,/r/sou
MO-012,Candidate evidence loaded,evidence:ready,Candidate deep profile,Evidence text,PROTOTYPED,
MO-013,Candidate comparison morph,compare:changed,Compare candidates,Direct table redraw,RESEARC
MO-014,Job preference filter,filter:changed,Explore Jobs,Direct redraw,RESEARCHED,,,
MO-015,Mandate wording revised,mandate:patched,Mandate builder,Text diff,PROTOTYPED,/r/mandate,S
MO-016,Uploaded file accepted,file:received,Uploader,Percentage text,P
… [2260 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check glyphs, tag styles, tokens

  <details><summary>result</summary>

```
3:export type GlyphKind = 'verified' | 'full' | 'partial' | 'practice' | 'none' | 'unclear';
4-/** One evidence-strength vocabulary for hiring and careers. Strength is carried by SHAPE, never by shade. */
5-export const GLYPH_LABEL: Record<GlyphKind, string> = { verified: 'Verified', full: 'Evidenced', partial: 'Partial or outdated', practice: 'Practising (private)', none: 'Not shown yet', unclear: 'Unclear' };
6-export function Glyph({ k, size = 20, title }: { k: GlyphKind; size?: number; title?: string }) {
122:.ds-sheet { background: var(--sheet); border-radius: var(--r-surface); box-shadow: var(--shadow); padding: clamp(16px, 2.2vw, 28px); min-width: 0; }
134:.ds-tag { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; border-radius: 999px; padding: 3px 10px; border: 1px solid var(--rule-2); color: var(--ink-2); white-space: nowrap; }
135:.ds-tag[data-k='ok'] { border-color: var(--ok); color: var(--ok); }
136:.ds-tag[data-k='busy'] { border-color: var(--gold); color: var(--gold-ink); }
137:.ds-tag[data-k='risk'] { border-color: var(--risk); color: var(--risk); }
138:.ds-tag[data-k='warn'] { border-color: var(--warn); color: var(--warn); }
150:.ds-banner { display: grid; grid-template-columns: auto 1fr auto; gap: 12px; align-items: center; padding: 12px 16px; border-radius: 12px; border: 1px solid var(--rule-2); background: var(--sheet); }
151:.ds-banner[data-k='risk'] { border-color: var(--risk); }
152:.ds-banner[data-k='warn'] { border-color: var(--war
… [2177 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Add verify/posted state to hire-a area

  <details><summary>result</summary>

```
31:  verify: Record<string, VerifyState>;
40:  init: (): HireAState => ({ intake: {}, orgs: [], snapshots: {}, meta: {}, discarded: {}, search: {}, instructions: {}, conflicts: {}, requests: [], forwarded: [], verify: {}, posted: {} }),
```
  </details>

- 🔧 `Bash`: Add verification and posting to model

  <details><summary>result</summary>

```
110:export const scopeOf = (a: Actor) => (a.orgId ? `ORG:${a.orgId}` : `PERSON:${a.personId ?? a.id}`);
118:export const payText = (m: Pick<MandateX, 'pay'>) => (m.pay.min && m.pay.min !== m.pay.max ? `${naira(m.pay.min)}–${naira(m.pay.max)} a ${m.pay.period}` : `Up to ${naira(m.pay.max)} a ${m.pay.period}`);
145:  emit(w, a.id, 'mandate.created', scopeOf(a), `Q drafted the “${m.title}” role brief (v1) from ${a.first}’s conversation.`, { mandateId: m.id });
174:  emit(w, a.id, 'mandate.revised', scopeOf(a), `Changed the “${m.title}” brief to v${v}: ${note}.`, { mandateId: id, v });
```
  </details>

- 🔧 `Bash`: Verify regex escaping

  <details><summary>result</summary>

```
192:const FREE_MAIL = /@(gmail|googlemail|yahoo|ymail|outlook|hotmail|live|icloud|me|aol|proton|protonmail)\./i;
197:  const m = text.match(/\b(rc|bn)\s*[-:.#]?\s*(?:no\.?|number)?\s*(\d{3,10})\b/i) ?? text.match(/\b()(\d{5,10})\b/);
202:  const digits = num.replace(/\D/g, '');
```
  </details>

- 🔧 `Bash`: Add verify and post skills

  <details><summary>result</summary>

```
src/q/skills/hire-a.ts(238,10): error TS2678: Type '"verify"' is not comparable to type '"search" | IntakeStep | "propose" | undefined'.
src/q/skills/hire-a.ts(481,12): error TS6133: 'c' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Fix type cast and view line 481

  <details><summary>result</summary>

```
registerSkill({
  id: 'hire-a.why-verify', side: 'recruiter',
  match: (c) => (c.actor.orgId && isFounder(c.actor) && /\bwhy\b/.test(c.norm) && /\b(verify|verified|verification|cac|can(not|'t)? (you )?search|no one|nobody)\b/.test(c.norm) && !isVerified(c.w, c.actor.orgId) ? 0.9 : 0),
  handle: (c) => ({ msgs: [{ kind: 'reply', used: ['Candidates’ privacy settings'], text: 'Because people on Talent Q decide who can find them, and most choose “verified employers only”. It stops fake employers from collecting people’s details. Once your business is verified, they can be found by you; until then, only people who apply to a posted role share their profile with you.', actions: [ask('Verify my business')] }] }),
});

function postAsk(c: QCtx, m?: MandateX): QReply {
```
  </details>

- 🔧 `Bash`: Fix unused param and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Read SwitchRow component

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

- 🔧 `Bash`: Check switch css and motion imports

  <details><summary>result</summary>

```
258:.ds-switchrow { display: grid; grid-template-columns: 1fr auto; gap: 16px; align-items: center; padding: 14px 0; border-top: 1px solid var(--rule); }
259:.ds-switchrow:first-of-type { border-top: 0; }
260:.ds-switchrow .txt { display: grid; gap: 2px; min-width: 0; }
journeys/career/Route.tsx:7:import { motion } from 'motion/react';
journeys/career/Career.tsx:7:import { AnimatePresence, motion } from 'motion/react';
journeys/career/Atlas.tsx:5:import { motion } from 'motion/react';
ds/QMark.tsx:13:import { motion, useReducedMotion } from 'motion/react';
ds/Workspace.tsx:5:import { motion } from 'motion/react';
ds/AppShell.tsx:10:import { AnimatePresence, MotionConfig, motion } from 'motion/react';
```
  </details>

- 🔧 `Bash`: Rewrite Q cards and add PayRange, verify components

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 12:31

You've hit your 5-hour limit · resets 1:50pm (UTC)


**User** · 2026-10-29 13:51

The coordinator sent a message while you were working:
From the lead: the usage limit has reset. Please continue the design pass exactly where you stopped. Your brief and my two follow-up messages (handoff doc, SwitchRow) still apply.

Address this before completing your current task.

- 🔧 `Bash`: Register VerifyRef and typecheck

  <details><summary>result</summary>

```
200
```
  </details>

- 🔧 `Bash`: Add design-pass CSS

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Check which semantic tokens exist

  <details><summary>result</summary>

```
--paper
```
  </details>

- 🔧 `Bash`: Find token definitions

  <details><summary>result</summary>

```
--data: --gold-light: --ink-2: --ink-3: --moon-2: --moon: --night-2: --night-3: --night-4: --rule-2: --sheet: --wash:
```
  </details>

- 🔧 `Bash`: Fix invalid font shorthand

  <details><summary>result</summary>

```
77:.hire-a-range .lbl { position: absolute; bottom: 24px; left: 50%; transform: translateX(-50%); white-space: nowrap; font-size: 12px; font-weight: 600; line-height: 1; color: var(--ink); font-variant-numeric: tabular-nums; }
```
  </details>

- 🔧 `Bash`: Redesign Roles list, brief, people

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Add paybox CSS

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Redesign founder home

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Redesign audit log

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Redesign Kora brief and search screens

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Verify screen edits

  <details><summary>result</summary>

```
screens/Sourcing.tsx:31:    <Canvas title={done ? `${w.sourcing.found.length} people to compare` : runId ? `Searching · ${found.length} found so far` : notStarted ? 'Search hasn’t started' : 'Search for Senior Backend'} kicker={<>Search · {w.mandate.title}</>} open onClose={openQ}
screens/Sourcing.tsx:75:    <Canvas title={ms.length ? 'Search for your roles' : 'Search'} kicker="Search" open onClose={openQ}>
screens/MandateIntake.tsx:20:    <Canvas title="Your role briefs live in Roles" kicker="Role brief" open onClose={openQ}>
screens/MandateIntake.tsx:28:    <Canvas title={m.title} kicker={<>Role brief · {m.team}</>} aside={<span className="ds-tag" data-k={approved ? 'ok' : 'busy'}><span className="num">v{m.version}</span> · {approved ? 'Approved' : 'Draft'}</span>} open onClose={openQ}
7:import { Field, Label, Segmented } from '../ui/kit';
48:            <Label as="h2">Requirements, hardest first</Label>
37:        <fieldset disabled={approved} className="stack gap-6" style={{ border: 0, padding: 0, margin: 0 }}>
57:        </fieldset>
```
  </details>

- 🔧 `Bash`: Redesign memory page on Canvas

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Capture redesigned pages

  <details><summary>result</summary>

```
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1
u_ada_r_audit.png
u_ada_r_mandate.png
u_ada_r_memory.png
u_ada_r_roles.png
u_ada_r_sourcing.png
u_funmi_r_home.png
u_funmi_r_roles.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1/desktop/u_funmi_r_home.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1/desktop/u_ada_r_roles.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1/desktop/u_ada_r_audit.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1/desktop/u_ada_r_memory.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:02

[Image: original 1440x2069, displayed at 1392x2000. Multiply coordinates by 1.03 to map to original image.]

- 🔧 `Bash`: Fix memory copy and roles tag spacing

  <details><summary>result</summary>

```
49:      aside={ms.length ? <span className="hire-a-summary">{drafts > 0 && <span className="ds-tag" data-k="busy">{drafts} waiting for approval</span>}<span className="ds-tag num">{`${ms.length} ${ms.length === 1 ? "role" : "roles"}`}</span></span> : undefined}>
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1/desktop/u_ada_r_mandate.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/a1/desktop/u_ada_r_sourcing.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Simplify requirement switch copy, list numbers

  <details><summary>result</summary>

```
1
```
  </details>

- 🔧 `Bash`: Update R1 for verification and run desktop

  <details><summary>result</summary>

```
FAIL [d] simulated search finds bookkeepers only
FAIL [d] shortlist by name
FAIL [d] Q proposes times and asks for approval · Nobody is on the shortlist yet. Pick who you want to meet first, for example “shortlist the top 2”.
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.click: Timeout 30000ms exceeded.
Call log:
[2m  - waiting for locator('.ds-thread .ds-chip').filter({ hasText: /Hold the times/ }).last()[22m

    at chip (/home/user/neo/talent-q-design/qa/scripts/journeys/R1.mjs:33:133)
    at async file:///home/user/neo/talent-q-design/qa/scripts/journeys/R1.mjs:163:3 {
  log: [
    "  - waiting for locator('.ds-thread .ds-chip').filter({ hasText: /Hold the times/ }).last()"
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Debug search step

  <details><summary>result</summary>

```
FAIL [d] simulated search finds bookkeepers only ·  / Found it: BN 3124567 is Crumb & Co on the business register (simulated check). Crumb & Co is now a verified employer, so people who allow verified employers can be found. Shall I search for “Part-time bookkeeper (2 days a week)” now? I won’t contact anyone. || Welcome back. Crumb & Co is set up, with you as the owner. Your brief is “Part-time bookkeeper (2 days a week)”, v3, approved. Next is finding people for it.
```
  </details>

- 🔧 `Bash`: Fix intent collision and rerun R1

  <details><summary>result</summary>

```
ERRORS []
```
  </details>

- 🔧 `Bash`: Run R1 and R5 on both viewports

  <details><summary>result</summary>

```
ERRORS []
PASS R1: 80/80 steps passed
ERRORS []
PASS R5: 66/66 steps passed
```
  </details>

- 🔧 `Bash`: Run privacy review script

  <details><summary>result</summary>

```
PASS Dayo hidden from Kora
PASS search results cache no longer shows Dayo
PASS saved comparison no longer shows Dayo
PASS Zara withdrew from Kora: nothing visible despite her application
PASS no page errors
All privacy checks passed
```
  </details>


**Claude** · 2026-10-29 14:11

Now let me look at the journey-state captures.

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-09-verify-ask.png

  <details><summary>result</summary>

```
File does not exist. Note: your current working directory is /home/user/neo/talent-q-design/qa/scripts/journeys.
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-10-verify-canvas.png

  <details><summary>result</summary>

```
File does not exist. Note: your current working directory is /home/user/neo/talent-q-design/qa/scripts/journeys.
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-11-verify-failed.png

  <details><summary>result</summary>

```
File does not exist. Note: your current working directory is /home/user/neo/talent-q-design/qa/scripts/journeys.
```
  </details>

- 🔧 `Bash`: List R1 desktop captures

  <details><summary>result</summary>

```
d-01-signup.png
d-02-home-welcome.png
d-03-draft-v1.png
d-04-draft-v1-canvas.png
d-05-budget-below.png
d-06-version-v1.png
d-07-back-next-day.png
d-08-people.png
d-08-verify-ask.png
d-09-people-canvas.png
d-09-verify-canvas.png
d-10-propose.png
d-10-verify-failed.png
d-11-handoff.png
d-11-people.png
d-12-people-canvas.png
d-12-roles.png
d-13-audit.png
d-13-propose.png
d-14-handoff.png
d-15-roles.png
d-16-audit.png
```
  </details>

- 🔧 `Bash`: Remove superseded R1 captures

  <details><summary>result</summary>

```
32
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-08-verify-ask.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-09-verify-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Shorten verify copy, fix card contrast, caption

  <details><summary>result</summary>

```
418:  const emailOk = businessEmail(a.email);
421:    + (emailOk ? ` Your business email is already confirmed from sign-up.` : ` Your sign-up email is a personal address (${emailDomain(a.email)}), so you’ll also need one at your business’s own website.`)
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-12-people-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/m-10-verify-failed.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Fix people sheet padding

  <details><summary>result</summary>

```
119:.hire-a-people.ds-sheet { gap: 0; padding: 4px clamp(16px, 2.2vw, 28px); }
```
  </details>

- 🔧 `Bash`: Recapture and build phone contact sheet

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/phone-a2.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Create before worktree and serve on 5191

  <details><summary>result</summary>

```
Exit code 7
README.md
docs
index.html
package-lock.json
package.json
src
talent-q-design
video
vite.config.js
ln: failed to create symbolic link '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/wtb/prototype/node_modules': No such file or directory
/bin/bash: line 1: cd: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/wtb/prototype: No such file or directory
000
```
  </details>

- 🔧 `Bash`: Serve before worktree on 5191

  <details><summary>result</summary>

```
0ff8835 T3/T5 design pass: Passport as a portfolio, honest search and sharing previews from the enforced policy, clearer jobs/applications/prep/memory
200
```
  </details>

- 🔧 `Bash`: Run old R1 to capture before states

  <details><summary>result</summary>

```
FAIL [d] simulated search finds bookkeepers only
FAIL [d] shortlist by name
FAIL [d] Q proposes times and asks for approval · Nobody is on the shortlist yet. Pick who you want to meet first, for example “shortlist the top 2”.
d-01-signup.png
d-02-home-welcome.png
d-03-draft-v1.png
d-04-draft-v1-canvas.png
d-05-budget-below.png
d-06-version-v1.png
d-07-back-next-day.png
d-08-people.png
d-09-people-canvas.png
d-10-propose.png
d-11-handoff.png
d-12-roles.png
d-13-audit.png
m-01-signup.png
m-02-home-welcome.png
m-03-draft-v1.png
m-04-draft-v1-canvas.png
m-05-budget-below.png
m-06-version-v1.png
m-07-back-next-day.png
m-08-people.png
m-09-people-canvas.png
m-10-propose.png
m-11-handoff.png
m-12-roles.png
m-13-audit.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/hirea-dp/wtb/talent-q-design/captures/cx/R1/d-09-people-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Rerun R1 after fixes

  <details><summary>result</summary>

```
ERRORS []
PASS R1: 80/80 steps passed
```
  </details>

- 🔧 `Bash`: Check for orgLimits in store

  <details><summary>result</summary>

```
182:/** ANYONE (default, founder decision D1): any organisation, verified or not — unverified ones are limited by orgLimits.
183- *  EMPLOYERS_AND_AGENCIES: organisations with a verified domain. VERIFIED_EMPLOYERS: fully checked employers only. */
184:type DiscoveryRule = { who: 'ANYONE' | 'EMPLOYERS_AND_AGENCIES' | 'VERIFIED_EMPLOYERS' | 'NOBODY'; hideFrom: string[] };
185-/** The candidate's discovery rule (set on their Passport; default: verified employers only, no agencies). */
186:export const discoveryRule = (w: World, pid: string): DiscoveryRule => (w.areas['talent-b'] as { discovery?: Record<string, DiscoveryRule> } | undefined)?.discovery?.[pid] ?? { who: 'ANYONE', hideFrom: [] };
187-/** An explicit relationship the candidate created: applied, shared something, or registered with an agency. */
188-export function relationshipWith(w: World, pid: string, orgId: string) {
189-  const c = w.consents[pid];
--
201:  return true; // ANYONE
202-}
203-/** A fully verified organisation: domain and business registration both checked. */
204-export const orgVerified = (o: { verified: { domain: boolean; registry: string } }) => o.verified.domain && o.verified.registry === 'VERIFIED';
--
207:export function orgLimits(w: World, orgId: string) {
208-  const o = w.orgs.find((x) => x.id === orgId);
209-  if (o && orgVerified(o)) return { verified: true, postRoles: true, outreachPerWeek: Infinity, campaigns: true, submittals: true, seeContactDetails: true };
210-  return { verified: f
… [29 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read orgLimits and uses

  <details><summary>result</summary>

```
export const discoveryRule = (w: World, pid: string): DiscoveryRule => (w.areas['talent-b'] as { discovery?: Record<string, DiscoveryRule> } | undefined)?.discovery?.[pid] ?? { who: 'ANYONE', hideFrom: [] };
/** An explicit relationship the candidate created: applied, shared something, or registered with an agency. */
export function relationshipWith(w: World, pid: string, orgId: string) {
  const c = w.consents[pid];
  if (c?.registeredWith?.includes(orgId)) return true;
  if (w.applications.some((a) => a.personId === pid && w.jobs.find((j) => j.id === a.jobId)?.orgId === orgId)) return true;
  return w.evidence.some((e) => e.ownerId === pid && e.visibility === 'SHARED_WITH' && e.sharedWith.includes(orgId) && !e.revokedFrom?.includes(orgId));
}
/** Whether an organisation may find this person without a relationship (search, sourcing, pools, campaigns). */
export function canDiscover(w: World, pid: string, orgId: string) {
  if (!w.consents[pid]?.discoverable) return false;
  const d = discoveryRule(w, pid); const o = w.orgs.find((x) => x.id === orgId);
  if (!o || d.who === 'NOBODY' || d.hideFrom.includes(orgId)) return false;
  if (d.who === 'VERIFIED_EMPLOYERS') return o.kind === 'EMPLOYER' && orgVerified(o);
  if (d.who === 'EMPLOYERS_AND_AGENCIES') return o.verified.domain;
  return true; // ANYONE
}
/** A fully verified organisation: domain and business registration both checked. */
export const orgVerified = (o: { verified: { domain: boolean; registry: string } }) => o
… [1699 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read propose functions

  <details><summary>result</summary>

```
609:function proposeReply(c: QCtx, m: MandateX): QReply {
610-  const sl = c.w.pipeline.filter((e) => e.mandateId === m.id && e.stage === 'SHORTLISTED').map((e) => e.personId);
611-  if (!sl.length) return { msgs: [{ kind: 'reply', text: 'Nobody is on the shortlist yet. Pick who you want to meet first, for example “shortlist the top 2”.' }] };
612-  const slots = slotsFrom(c.w, c.norm, sl.length);
613-  const plan = sl.map((pid, i) => ({ pid, start: slots[i] }));
614-  const tz = c.actor.timezone;
615-  return { msgs: [{ kind: 'approval', used: ['Your shortlist', 'Weekdays, 10:00 and 14:00 (you can change this)'],
616-    text: `Here’s a plan: ${plan.map((p) => `${personOf(c.w, p.pid)!.name}, ${dayLabel(p.start, tz)} at ${timeLabel(p.start, tz)}`).join('; ')}. I’ll hold these times on your calendar and draft an invitation to each person. Nothing is sent or booked: the holds are only on your side, and each invitation waits for your approval. Go ahead?`,
617-    why: 'Holds stop you double-booking while people reply. They are simulated in this prototype.',
618-    actions: [op('Hold the times and draft invitations', 'hire-a.propose', { id: m.id, plan }, true), ask('Afternoons instead'), ask('What’s a hold?')] }],
619-    frame: frame(R1, 'propose', { id: m.id, plan: JSON.stringify(plan) }) };
620-}
621-function proposeIn(w: World, a: Actor, id: string, plan: { pid: string; start: string }[]) {
622-  const m = findM(w, id); if (!m) return;
623-  const org = orgOf(w, a.orgId)?.na
… [2192 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Look for unverified send label in shared code

  <details><summary>result</summary>

```
./q/skills/hire-b.ts:154:      msgs: [{ kind: 'reply', text: `Accepted. I now read ${fn(c.w, pid)}’s ${reqLabel(c.w, reqId)} as “${LEVEL_WORD[level].toLowerCase()}”, labelled as your correction rather than a check.${!down ? ' It still isn’t verified.' : ''} ${before === after ? `The order stays ${after}, but the margin is ${down ? 'narrower' : 'wider'}.` : `Order before: ${before}. Now: ${after}.`}`, why: 'Corrections are recorded with your name in the audit trail. Say “undo” to restore my reading.',
./q/skills/talent-b.ts:346:      msgs: [reply(`I’ve started your application to ${jobName(c.w, job)}. I’d share ${items.length ? items.map((e) => `“${e.title}”`).join(' and ') : 'nothing yet (your Passport has no matching proof)'}, nothing else. ${unv ? 'This employer isn’t verified, so I’d share as little as possible. ' : ''}Nothing is sent until you confirm.`, {
./journeys/talent-b/Jobs.tsx:135:          <p className="t14" style={{ margin: 0 }}>Choose exactly what {orgName(w, job.orgId)} sees. Nothing else in your Passport is shared.{!verifiedEmployer(w, job) && ' This employer isn’t verified: share as little as you can.'}</p>
./journeys/gallery/StatesGallery.tsx:110:    {s === 'why' && <p className="t14" style={{ margin: 0, color: 'var(--moon-2)' }}>You applied on 17 Oct. Most employers reply within 10 days, and Rivers Tech isn’t verified yet.</p>}
./journeys/onboarding/match.ts:50:    if (!job.signals.domainVerified) notes.push('Employer not verified yet.');
```
  </details>

- 🔧 `Bash`: Model: limits from store, posting gated

  <details><summary>result</summary>

```
6:import { actorOf, canSeeCandidate, emit, getWorld, orgLimits, orgOf, outreachThisWeek, simNow, uid, update, type World } from '../../mock/world';
190:// store (orgLimits in mock/world.ts); never hard-code them here. Verification needs a business email domain and a
194:  const l = orgLimits(w, orgId ?? '');
```
  </details>

- 🔧 `Bash`: Rework R1 skills for D1/D3 limits

  <details><summary>result</summary>

```
src/q/skills/hire-a.ts(419,9): error TS6133: 'posted' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: View verifyIntro lines

  <details><summary>result</summary>

```
const a = c.actor; const o = orgOf(c.w, a.orgId);
  if (!o) return { msgs: [{ kind: 'reply', text: 'Tell me about your business first, and I’ll set it up with you.' }] };
  if (isVerified(c.w, o.id)) return { msgs: [{ kind: 'reply', ref: { type: 'hire-a.verify', id: o.id }, text: `${o.name} is already verified, so I can search for people.`, actions: m ? [op('Find people', 'hire-a.search', { id: m.id }, true)] : [] }] };
  const emailOk = businessEmail(a.email);
  const posted = m ? postedJob(c.w, m.id) : undefined;
  const lim = limitsFor(c.w, o.id);
  const text = `To verify ${o.name}, Talent Q checks that it’s a real business. Until then you can search and shortlist, but you can’t post roles, you can message up to ${lim.outreachPerWeek} people a week, and each message says you’re not verified yet.`
```
  </details>

- 🔧 `Bash`: Remove unused var, update already-verified text

  <details><summary>result</summary>

```
if (isVerified(c.w, o.id)) return { msgs: [{ kind: 'reply', ref: { type: 'hire-a.verify', id: o.id }, text: `${o.name} is already verified: you can post roles and message as many people as you need.`, actions: m && m.status !== 'DRAFT' && !postedJob(c.w, m.id) ? [ask('Post the role')] : [] }] };
```
  </details>

- 🔧 `Bash`: Limits panel UI, roles updates

  <details><summary>result</summary>

```
src/journeys/hire-a/Audit.tsx(10,10): error TS2305: Module '"./ui"' has no exported member 'openQ'.
src/journeys/hire-a/Home.tsx(14,10): error TS2305: Module '"./ui"' has no exported member 'openQ'.
src/journeys/hire-a/Roles.tsx(17,16): error TS2305: Module '"./ui"' has no exported member 'evidenceGlyph'.
src/journeys/hire-a/Roles.tsx(17,44): error TS2305: Module '"./ui"' has no exported member 'openQ'.
src/journeys/hire-a/ui.tsx(164,36): error TS2304: Cannot find name 'evidenceGlyph'.
src/screens/MandateIntake.tsx(12,10): error TS2305: Module '"../journeys/hire-a/ui"' has no exported member 'openQ'.
src/screens/Memory.tsx(10,10): error TS2305: Module '"../journeys/hire-a/ui"' has no exported member 'openQ'.
src/screens/Sourcing.tsx(13,10): error TS2305: Module '"../journeys/hire-a/ui"' has no exported member 'openQ'.
```
  </details>

- 🔧 `Bash`: Restore openQ and evidenceGlyph

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Limits CSS and home step reorder

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: View R1 middle section

  <details><summary>result</summary>

```
108:  await openQ();
109:  step(v, 'proactive: draft unapproved for over a day', await page.locator('.ds-suggest').filter({ hasText: /has been a draft since/ }).count() > 0);
110:  await shot('back-next-day');
111:  await closeQ();
112:
113:  // ---- Approve, search, shortlist ----
114:  await chip(/^Approve v3$/);
115:  m = await mandate();
116:  step(v, 'approved after explicit approval', m?.status === 'APPROVED', m?.status);
117:  // ---- [info] Search is gated on verification: privacy rules hide everyone from an unverified business ----
118:  await ask('yes go ahead and look for people', 900);
119:  w = await world();
120:  step(v, '[info] Q explains why verification comes before search', /checks that Crumb & Co is a real business/.test(await lastQ()) && /CAC registration number/.test(await lastQ()) && !w.areas['hire-a'].search[m.id], await lastQ());
121:  step(v, 'business email confirmed from sign-up; registry not yet', w.orgs.find((o) => o.id === 'org_crumb').verified.domain === true && w.orgs.find((o) => o.id === 'org_crumb').verified.registry !== 'VERIFIED');
122:  await shot('verify-ask', true);
123:  await go(`/r/roles/${m.id}`);
124:  await page.getByRole('button', { name: /^People/ }).click(); await page.waitForTimeout(300);
125:  step(v, 'People view shows the verification step, not an empty search', /Verify Crumb & Co to find people/.test(await canvas()) && /Business registration \(CAC\)/.test(await canvas()));
126:  await shot('verify-canvas');
127:
128:  // -
… [4208 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Rewrite R1 middle for D1/D3

  <details><summary>result</summary>

```
188:  // ---- Isolation and audit ----
/home/user/neo/talent-q-design/prototype/src/main.tsx:10:(window as unknown as { __tqQA: unknown }).__tqQA = { canDiscover, canSeeCandidate, relationshipWith, visibleEvidence, getWorld, update };
```
  </details>

- 🔧 `Bash`: Run updated R1 desktop

  <details><summary>result</summary>

```
FAIL [d] People view shows the weekly message cap
FAIL [d] [recover] outreach cap hit: 3 planned, the 4th left out and named · Here’s a plan: Kemi Alade, Mon 2 Nov at 10:00; Halima Bello, Mon 2 Nov at 14:00; Yusuf Garba, Tue 3 Nov at 10:00. I’ll hold these times on your calendar and draft an invitation to each person. Nothing is sent or booked: the holds are only on your side, and each invitation waits for your approval. Until Crumb & Co is verified you can message 3 people a week (0 used), and each invitation says you’re not verified yet. So I’ve left out Tope; verify to invite them now. Go ahead?
ERRORS []
FAIL R1: 45/47 steps passed
```
  </details>

- 🔧 `Bash`: Fix test regexes and rerun R1 both viewports

  <details><summary>result</summary>

```
ERRORS []
PASS R1: 94/94 steps passed
```
  </details>

- 🔧 `Bash`: Run R5, privacy; list R1 captures

  <details><summary>result</summary>

```
ERRORS []
PASS R5: 66/66 steps passed
All privacy checks passed
d-01-signup.png
d-02-home-welcome.png
d-03-draft-v1.png
d-04-draft-v1-canvas.png
d-05-budget-below.png
d-06-version-v1.png
d-07-back-next-day.png
d-08-people.png
d-08-verify-ask.png
d-09-people-canvas.png
d-09-verify-canvas.png
d-10-propose.png
d-10-verify-failed.png
d-11-handoff.png
d-11-people.png
d-12-people-canvas.png
d-12-post-refused.png
d-13-propose.png
d-13-verify-ask.png
d-14-handoff.png
d-14-verify-failed.png
d-15-roles.png
d-15-verified-canvas.png
d-16-audit.png
d-16-roles.png
d-17-audit.png
```
  </details>

- 🔧 `Bash`: Remove stale R1 captures

  <details><summary>result</summary>

```
d-01-signup.png d-02-home-welcome.png d-03-draft-v1.png d-04-draft-v1-canvas.png d-05-budget-below.png d-06-version-v1.png d-07-back-next-day.png d-08-people.png d-09-people-canvas.png d-10-propose.png d-11-handoff.png d-12-post-refused.png d-13-verify-ask.png d-14-verify-failed.png d-15-verified-canvas.png d-16-roles.png d-17-audit.png m-01-signup.png m-02-home-welcome.png m-03-draft-v1.png m-04-draft-v1-canvas.png m-05-budget-below.png m-06-version-v1.png m-07-back-next-day.png m-08-people.png m-09-people-canvas.png m-10-propose.png m-11-handoff.png m-12-post-refused.png m-13-verify-ask.png m-14-verify-failed.png m-15-verified-canvas.png m-16-roles.png m-17-audit.png
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-09-people-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-12-post-refused.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/m-09-people-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Count drafts against cap; allowance shows drafted

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Update cap wording and rerun R1

  <details><summary>result</summary>

```
1
1
ERRORS []
PASS R1: 94/94 steps passed
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-15-verified-canvas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/m-12-post-refused.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Distinguish post chip labels

  <details><summary>result</summary>

```
2
175:  await chip(/^Post it as a job$/);
```
  </details>

- 🔧 `Bash`: Final R1 run and after captures

  <details><summary>result</summary>

```
ERRORS []
PASS R1: 94/94 steps passed
captured 102 pages to captures/review/after
u_ada_r_audit.png
u_ada_r_mandate.png
u_ada_r_memory.png
u_ada_r_roles.png
u_ada_r_sourcing.png
u_funmi_r_home.png
u_funmi_r_roles.png
```
  </details>

- 🔧 `Bash`: Copy key journey states into after captures

  <details><summary>result</summary>

```
16
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R1/d-07-back-next-day.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Inspect Glyph markup

  <details><summary>result</summary>

```
export function Glyph({ k, size = 20, title }: { k: GlyphKind; size?: number; title?: string }) {
  return (
    <svg width={size} height={size} viewBox="0 0 20 20" role={title ? 'img' : undefined} aria-label={title} aria-hidden={title ? undefined : true} style={{ flex: 'none' }}>
      {k === 'verified' && <><circle cx="10" cy="10" r="8.5" fill="none" stroke="currentColor" strokeWidth="1.5" /><circle cx="10" cy="10" r="5" fill="currentColor" /></>}
      {k === 'full' && <circle cx="10" cy="10" r="6.5" fill="currentColor" />}
      {k === 'partial' && <><circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" strokeWidth="1.5" /><path d="M10 4 A6 6 0 0 0 10 16 Z" fill="currentColor" /></>}
      {k === 'none' && <circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" strokeWidth="1.5" />}
      {k === 'unclear' && <circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" strokeWidth="1.5" strokeDasharray="2.4 2.4" />}
      {k === 'practice' && <circle cx="10" cy="10" r="5" fill="none" stroke="currentColor" strokeWidth="1.6" strokeDasharray="0.1 3" strokeLinecap="round" />}
    </svg>
  );
}
export function GlyphKey({ kinds }: { kinds: GlyphKind[] }) {
  return (
    <ul aria-label="Key" style={{ display: 'flex', flexWrap: 'wrap', gap: '6px 16px', listStyle: 'none', margin: 0, padding: 0 }}>
      {kinds.map((k) => <li key={k} className="t14" style={{ display: 'inline-flex', alignItems: 'center', gap: 6, color: 'var(--ink-2)' }}><Glyph k={k} size={16} />
… [40 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inline glyph in pay caption

  <details><summary>result</summary>

```
82:.hire-a-range figcaption svg, .hire-a-posted svg { display: inline-block; vertical-align: -2px; margin-right: 4px; }
```
  </details>

- 🔧 `Bash`: Refresh states and build before/after pairs

  <details><summary>result</summary>

```
PASS R1: 94/94 steps passed
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
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/hire-a/02-after.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/phone/u_ada_r_audit.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:38

[Image: original 780x3776, displayed at 413x2000. Multiply coordinates by 1.89 to map to original image.]

- 🔧 `Bash`: Check existing design/handoff docs

  <details><summary>result</summary>

```
design:
agency.md
hire-b.md
hire-c.md
talent-a.md
talent-b.md
talent-c.md

handoff:
agency.md
hire-b.md
hire-c.md
talent-a.md
talent-b.md
talent-c.md
==> design/agency.md <==
# Design pass: agency (R4, Dele at Talentbridge; Tunde is a Viewer)

Pages: agency home, `/r/agency/clients` (and `/clients/:id`), `clients/mandate/:id`, `clients/notes`, `clients/docs`,
`pools`, `pools/searches`, `pools/compare`, `submittals`, `campaigns`, `agents`, `reports`. Old flat paths redirect.
Code: `prototype/src/journeys/agency/pages.tsx`, `model.ts`, `src/routes/agency.tsx`, `src/styles/agency.css`.

## Defects found (most severe first)
1. **Two navigation systems.** An 11-item pill bar repeated the rail on every page, wrapped to two rows on desktop and
   scrolled sideways on phones. The rail didn't mark secondary pages. (IA, Jakob, excise)
2. **Agent monitoring didn't scan.** Each run was a tall card with five equal buttons. State showed only as a small
   tag plus colour. Interrupted looked the same as paused, and nothing showed where a resumed run had picked up again.
   There was no overview of slots or states. (H1, Von Restorff, Hick)
3. **Client isolation was a row of filter chips with a grey sentence.** It looked like a filter, not like a workspace boundary.
4. **Privacy leaks in the agency area.** Saved searches, the Medlink ops mandate, the seeded submittal and the campaign
   approval text named Chidi, Amaka or Zara. Excluded campaign rows named Zara with a privacy reason.
5. **Poo
… [1841 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/hire-a.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/hire-a.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check doc lengths and handoff format

  <details><summary>result</summary>

```
75 design/hire-a.md
# Engineering handoff · hire-b (R2 Ada, a non-technical recruiter hiring a Senior Backend Engineer at Kora Pay)

Specification only. The prototype is the behavioural and design blueprint, not the implementation. Every
"Prototype:" path is under `prototype/src/`. Lines marked **PROD ≠ SIM** say where production must differ.
Journey proof: `qa/scripts/journeys/R2.mjs` (74 steps, desktop + phone). Privacy proof: `qa/scripts/review/privacy.mjs`.
Code map: rules `journeys/hire-b/model.ts`, ops `journeys/hire-b/ops.ts`, pages `screens/Compare.tsx`,
`journeys/hire-b/{Profile,ProjectViewer,Interviews,Ledger}.tsx`, Q cards `journeys/hire-b/refs.tsx`, skills
`q/skills/hire-b.ts` (ids `hire-b.*`), proactive `q/proactive/hire-b.ts`, state `state/areas/hire-b.ts`, seed `state/seeds/hire-b.ts`.

## 0. Defaults every feature inherits
- **Tenancy.** The employer org (`org_kora`) is the tenant. Every hire-b record (corrections, plans, live notes, ratings,
  feedback, reviews, "seen" markers) carries `orgId` and the actor. **PROD:** use row-level security on `org_id`.
  A query without the predicate fails closed.
- **Candidate privacy is central and read-time.** All candidate reads go through `canSeeCandidate`,
  `visibleEvidence` and `relationshipWith` (`mock/world.ts`). Withdrawn consent → nothing. Revoked item → not shown,
  only counted ("ended access to 1 item"). PRACTICE is never visible. Saved views (comparison people, interview plans)
  are caches: `rank()` re-check
… [3239 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read perm and fairness skills

  <details><summary>result</summary>

```
id: 'hire-a.perm', side: 'recruiter',
  match: (c) => {
    if (!c.actor.orgId || isFounder(c.actor)) return 0;
    if (OFFER.test(c.norm) && !/\bwho can\b/.test(c.norm)) return 0.93;
    if (POLICY.test(c.norm)) return 0.9;
    if (BULK.test(c.norm)) return 0.9;
    return 0;
  },
  handle: (c) => {
    const a = c.actor; const org = orgOf(c.w, a.orgId)!;
    if (BULK.test(c.norm) && !OFFER.test(c.norm)) {
      const m = pickMandate(c.w, a, c.norm, c.route);
      let pids = m ? c.w.pipeline.filter((e) => e.mandateId === m.id && e.stage === 'SHORTLISTED').map((e) => e.personId) : [];
      let title = m?.title ?? '';
      if (!pids.length && a.orgId === 'org_kora') { pids = c.w.pipeline.filter((e) => e.mandateId === 'm_backend' && e.stage === 'SHORTLISTED').map((e) => e.personId); title = 'Senior Backend Engineer'; }
      const approvers = whoCan(c.w, a, 'approve_send');
      if (!pids.length) return { msgs: [{ kind: 'reply', text: 'There’s nobody on a shortlist to message yet.' }] };
      return { msgs: [{ kind: 'refusal', used: [`${org.name}: ${org.delegation === 'APPROVE_EACH_SEND' ? 'approve each send' : org.delegation.toLowerCase()}`, `Your role: ${ROLE_LABEL[a.role!]}`],
        text: `I can’t send them all now. ${org.name} approves every message one at a time, and there’s no “send all” that skips that${can(a, 'approve_send') ? '' : `; as ${ROLE_LABEL[a.role!]} you can’t approve sends either`}. What I’ve done instead: prepared ${pids.length} drafts (to ${listNames
… [3976 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/hire-a.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/hire-a.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Verify event names cited

  <details><summary>result</summary>

```
emit(w, actor.id, 'evidence.conflict.handled'
emit(w, actor.id, 'job.closed'
emit(w, actor.id, 'mandate.discarded'
emit(w, actor.id, 'mandate.restored'
emit(w, actor.id, 'mandate.unapproved'
emit(w, actor.id, 'memory.forgotten'
emit(w, actor.id, 'request.created'
emit(w, actor.id, 'search.instruction'
801-  emit(w, actor.id, 'request.created', scopeOf(actor), `${actor.name} asked ${target.name} to ${what}.`);
```
  </details>

- 🔧 `Bash`: Final checks and clean up worktree

  <details><summary>result</summary>

```
Exit code 144
PASS R5: 66/66 steps passed
All privacy checks passed
```
  </details>

- 🔧 `Bash`: Typecheck and check before server

  <details><summary>result</summary>

```
Exit code 7
5191:000
```
  </details>

- 🔧 `Bash`: Remove worktree and list changed files

  <details><summary>result</summary>

```
removed
 M talent-q-design/prototype/src/journeys/hire-a/Audit.tsx
 M talent-q-design/prototype/src/journeys/hire-a/Home.tsx
 M talent-q-design/prototype/src/journeys/hire-a/Roles.tsx
 M talent-q-design/prototype/src/journeys/hire-a/model.ts
 M talent-q-design/prototype/src/journeys/hire-a/ui.tsx
 M talent-q-design/prototype/src/q/core/proactive.ts
 M talent-q-design/prototype/src/q/skills/hire-a.ts
 M talent-q-design/prototype/src/routes/hire-a.tsx
 M talent-q-design/prototype/src/screens/MandateIntake.tsx
 M talent-q-design/prototype/src/screens/Memory.tsx
 M talent-q-design/prototype/src/screens/Sourcing.tsx
 M talent-q-design/prototype/src/state/areas/hire-a.ts
 M talent-q-design/prototype/src/styles/hire-a.css
 M talent-q-design/prototype/tsconfig.tsbuildinfo
 M talent-q-design/qa/results/R1.log
 M talent-q-design/qa/results/R3.log
 M talent-q-design/qa/results/T3.log
 M talent-q-design/qa/results/T4.log
 M talent-q-design/qa/results/T5.log
 M talent-q-design/qa/results/summary.txt
 M talent-q-design/qa/scripts/journeys/R1.mjs
 M talent-q-design/qa/scripts/review/capture-all.mjs
?? talent-q-design/journeys/DESIGN-PASS-BRIEF.md
?? talent-q-design/journeys/design/hire-a.md
?? talent-q-design/journeys/handoff/hire-a.md
5181:200
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The hire-a design pass is done and R1 is fixed under the new rules (D1/D3). R1.mjs passes 94/94 steps, R5.mjs 66/66 (both on desktop and phone), and `privacy.mjs` passes on port 5181. My

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
