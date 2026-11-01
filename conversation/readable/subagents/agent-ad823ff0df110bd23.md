# Helper agent agent-ad823ff0df110bd23: Design pass T1+T2 pages

Source: `agent-ad823ff0df110bd23.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 12:20

Run the design pass for area `talent-a` (journeys T1 Amaka, a first-time graduate, and T2 Chidi, moving from sales to product management or business analysis) in /home/user/neo/talent-q-design/prototype.

First read /home/user/neo/talent-q-design/journeys/DESIGN-PASS-BRIEF.md and follow it exactly, including loading the named skills with the Skill tool and applying them. Also read /home/user/neo/talent-q-design/journeys/BUILD-BRIEF.md for the contracts and your file ownership. You own the same `talent-a` files as before, including src/journeys/onboarding and src/journeys/career.

Your dev server port is 5185.

Your pages are:
- `/c/welcome`: the profile, built by chat, CV or form.
- `/c/career`: the J7 career workspace. This covers the atlas, list, your skills, the role sheet, plan, progress, record and openings, plus the "3 weeks later" return.
- `/c/growth`: readiness to apply.
- Every Q reply card your skills produce.

J7 and candidate development are founder priorities.

Use the `dataviz` skill seriously on the atlas, progress and readiness views. Improve the information architecture, so that a person can tell at a glance:
- where they are;
- what's between them and the goal;
- what counts as proof and what is only practice.

Don't just restyle the lines.

Use `design-superpowers:creative` to make the candidate experience personal and encouraging within Direction D.

T1.mjs and T2.mjs must keep passing.

- 🔧 `Bash`: Read design pass brief and list directories

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
… [4154 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read build brief and git status
- 🔧 `Skill`: {"skill": "design-skills:design-critique"}

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
… [7883 more characters trimmed]
```
  </details>


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

- 🔧 `Skill`: {"skill": "design-superpowers:creative"}

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

- 🔧 `Bash`: Read dataviz form and anti-pattern references

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
… [7733 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read marks reference and creative direction knowledge

  <details><summary>result</summary>

```
# Marks & anatomy

The quiet, considered look is a few fixed specs plus two pieces of negative space.
The data is the only thing allowed to be loud.

## Mark specs (fixed across every chart)

| Mark | Spec |
|---|---|
| Bar / column | **<= 24px thick** (cap it - never fill the slot; let the band's leftover be air); **4px rounded data-end, square at the baseline**; grows from a single baseline |
| Line | **2px**, round join/cap |
| Marker / end-dot | **>= 8px** (r >= 4), filled with the series color |
| Area fill | the series hue at **~10% opacity** (a wash, never a saturated block) |
| Gridlines / axes | one-step-off-surface gray, **hairline (1px), solid** (never dashed), recessive |

## The two spacers (white doing the separating)

- **Surface gap.** A **2px gap** in the surface color separates touching marks - every
  segment of a stacked bar, and every adjacent (touching) bar, the same width. Keep it
  one consistent width across a stack; neighbors one step apart read distinct because of
  the gap, not a stroke drawn around them.
- **Surface ring.** Dots and end-markers carry a **2px ring in the surface color**,
  so they stay legible where they cross a line or overlap each other. The ring is part
  of the mark's hover/hit target, not just spacing - see `interaction.md` (small dots
  are easy to under-size for hover).

Never draw a border around a mark to separate it. The gap and the ring are the
mechanism; a stroke adds data-weight ink that isn't data.

## Labels & legend
… [15622 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List area files

  <details><summary>result</summary>

```
155 journeys/talent-b/Jobs.tsx
   239 journeys/talent-b/Passport.tsx
    71 journeys/talent-b/Prep.tsx
    83 journeys/talent-b/ui.tsx
    76 journeys/talent-b/Applications.tsx
   474 journeys/talent-b/logic.ts
    61 journeys/talent-b/Memory.tsx
    69 journeys/hire-b/projects.ts
   160 journeys/hire-b/Profile.tsx
    98 journeys/hire-b/ProjectViewer.tsx
   230 journeys/hire-b/model.ts
   139 journeys/hire-b/ops.ts
    26 journeys/hire-b/ui.tsx
   166 journeys/hire-b/Interviews.tsx
    84 journeys/talent-c/interview.ts
   207 journeys/talent-c/FirstSteps.tsx
   117 journeys/talent-c/shared.tsx
    38 journeys/talent-c/questions.ts
   205 journeys/talent-c/InterviewRoom.tsx
   220 journeys/talent-c/runtime.ts
   236 journeys/planner/Planner.tsx
    93 journeys/hire-c/Calendar.tsx
    48 journeys/hire-c/Team.tsx
   472 journeys/hire-c/lib.ts
    72 journeys/hire-c/Setup.tsx
    93 journeys/hire-c/refs.tsx
    95 journeys/hire-c/Pipeline.tsx
   156 journeys/hire-c/Messages.tsx
   146 journeys/hire-c/CandidateMessages.tsx
   213 journeys/career/personas.ts
   201 journeys/career/j7.ts
   343 journeys/career/Career.tsx
   213 journeys/career/Atlas.tsx
   173 journeys/gallery/StatesGallery.tsx
   236 journeys/onboarding/Onboarding.tsx
    71 journeys/onboarding/match.ts
    57 journeys/onboarding/refs.tsx
   405 journeys/agency/model.ts
   532 journeys/agency/pages.tsx
    79 journeys/hire-a/Audit.tsx
    83 journeys/hire-a/Home.tsx
   228 journeys/hire-a/Roles.tsx
   264 journeys
… [998 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read routes and Career page

  <details><summary>result</summary>

```
<persisted-output>
Output too large (29.5KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bemibraqh.txt

Preview (first 2KB):
// Routes for T1 (Amaka) and T2 (Chidi). Owned by this area (see journeys/BUILD-BRIEF.md).
// The global Q drives both pages through src/q/skills/talent-a.ts; the pages are canvases only.
import type { ReactNode } from 'react';
import { registerRoute } from './registry';
import { InShell } from '../ds/Workspace';
import { Career } from '../screens/Career';
import { Onboarding } from '../journeys/onboarding/Onboarding';
import { J7 } from '../journeys/career/Career';
import '../journeys/onboarding/refs';
import '../styles/talent-a.css';

// On phones the shell has no Split, so a Canvas would otherwise render as a sheet with a dead back button.
// These pages are full pages beside the global Q (the "Ask Q" bar), so they render inline everywhere.
const page = (n: ReactNode) => <InShell.Provider value>{n}</InShell.Provider>;

registerRoute({ path: '/c/welcome', side: 'candidate', label: 'your profile', render: () => page(<Onboarding />), nav: { group: 'Q', label: 'Your profile', icon: 'welcome', order: 3 } });
registerRoute({ path: '/c/career', side: 'candidate', label: 'your career atlas', render: () => page(<J7 />), nav: { group: 'Grow', label: 'Career atlas', icon: 'atlas', tab: true, order: 11 } });
registerRoute({ path: '/c/growth', side: 'candidate', label: 'readiness to apply', render
… [667 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/career/Career.tsx

  <details><summary>result</summary>

```
1	// J7 Career Intelligence (career atlas). The global Q drives it (see q/skills/talent-a.ts): discovery,
2	// transferable skills, evidence vs gaps, a plan with practice, work samples and learning, assessment and
3	// reassessment, goal changes, and openings from real listings. This canvas shows and refines the work;
4	// buttons here act through Q's operations so the conversation records what happened.
5	// Evidence model: practice is private and never moves the map; only reviewed work or a verified credential does.
6	import { useEffect, useState } from 'react';
7	import { AnimatePresence, motion } from 'motion/react';
8	import { Glyph, GLYPH_LABEL, type GlyphKind } from '../../ds/Glyph';
9	import { Canvas, useNarrow, type ViewDef } from '../../ds/Workspace';
10	import { Link } from '../../ui/router';
11	import { actorOf, simNow, update, useWorld, type World } from '../../mock/world';
12	import { runAction, useViewState } from '../../q/core/engine';
13	import type { QAction } from '../../state/domain';
14	import { BandAtlas, OccList, RadialAtlas } from './Atlas';
15	import { compById, daysBetween, mentionOf, employerView, fmtDay, gapsFor, j7, jobsFor, occById, overdue, personaFor, readJ7, sampleFor, shown, simISO, stateOf, type J7State } from './j7';
16	import type { CState, Persona, RecClass } from './personas';
17	
18	type View = 'atlas' | 'list' | 'skills' | 'role' | 'plan' | 'progress' | 'record' | 'opps';
19	const CLS_GLYPH: Record<RecClass, CState> = { 'Practice attem
… [28582 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/career/Atlas.tsx
- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/career/j7.ts

  <details><summary>result</summary>

```
1	// J7 career state and the operations Q (and the atlas page) perform on it. One store (World v4): each
2	// person's J7 lives at w.j7[personId] and is PERSON-scoped. Practice and assessments are mirrored into the
3	// Passport as PRIVATE items; nothing here ever widens who can see anything. Sharing is a separate,
4	// explicitly approved act (see the talent-a skills).
5	import { emit, simNow, visibleEvidence, type World } from '../../mock/world';
6	import { anyOf, near } from '../../q/core/nlu';
7	import { profileText, readProfile } from '../../services/profile';
8	import { PERSONAS, type CState, type JOcc, type Persona, type PlanStep, type Practice, type Rec, type Sample } from './personas';
9	
10	export type PId = Persona['id'];
11	export const PERSON_OF: Record<PId, string> = { graduate: 'p_amaka', switcher: 'p_chidi', experienced: 'p_tobi' };
12	export const pidFor = (personId: string): PId => (personId === 'p_chidi' ? 'switcher' : personId === 'p_tobi' ? 'experienced' : 'graduate');
13	export const personaFor = (personId: string): Persona => PERSONAS[pidFor(personId)];
14	export const shown = (s: CState) => s === 'verified' || s === 'full';
15	
16	export interface Assessment { id: string; comp: string; at: string; level: number; round: number; rubric: { c: string; ok: boolean }[] }
17	export interface J7State {
18	  v: 2; goal: string; states: Record<string, CState>; record: Rec[]; plan: PlanStep[]; moved: Record<string, number>;
19	  archived: { occ: string; at: strin
… [14260 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
1	// J7 atlas views. Desktop: a radial atlas (distance from you = competencies not yet shown), with
2	// collision-aware labels and family collapse at scale. Phones: distance BANDS (below), because a radial
3	// chart at 340px can only be glanced at; bands keep every name readable and tappable.
4	import { useState } from 'react';
5	import { motion } from 'motion/react';
6	import { useWidth } from '../../ds/Workspace';
7	import type { CState, Comp, JOcc } from './personas';
8	
9	export const shown = (s: CState) => s === 'verified' || s === 'full';
10	export const gapsOf = (o: JOcc, st: (id: string) => CState) => o.needs.filter((n) => !shown(st(n)));
11	
12	export function RadialAtlas({ occs, st, sel, onSel, reach, setReach, large, openFam, setOpenFam, moved, fams, goal }: {
13	  fams: string[]; goal: string; occs: JOcc[]; st: (id: string) => CState; sel: string | null; onSel: (id: string) => void; reach: boolean; setReach: (v: boolean) => void;
14	  large: boolean; openFam: string | null; setOpenFam: (f: string | null) => void; moved: Record<string, number>;
15	}) {
16	  const [ref, w] = useWidth<HTMLDivElement>(720);
17	  const [hot, setHot] = useState<string | null>(null);
18	  const narrow = w < 560;
19	  const H = narrow ? w + 20 : Math.min(640, Math.max(500, w * 0.74));
20	  const cx = w / 2, cy = H / 2 + 6;
21	  const maxR = Math.min(w / 2 - (narrow ? 22 : 150), H / 2 - 40);
22	  const r0 = maxR * 0.2, step = (maxR - r0) / 4;
23	  const rad = (g: number) => r0 + Math.min
… [17495 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read onboarding, refs, css
- 🔧 `Bash`: Read growth screen

  <details><summary>result</summary>

```
<persisted-output>
Output too large (29.9KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bgzftuo99.txt

Preview (first 2KB):
// Your profile (T1). The global Q drives set-up by conversation; this canvas shows the profile being built,
// and offers the same three ways in: talk to Q, upload a CV (simulated parse) or a short form, switchable
// at any time. Everything shown here is a CLAIM in the person's own words until evidence backs it up.
import { useMemo } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { Glyph } from '../../ds/Glyph';
import { Canvas } from '../../ds/Workspace';
import { Link } from '../../ui/router';
import { actorOf, update, useWorld } from '../../mock/world';
import { runAction, useViewState } from '../../q/core/engine';
import { QUESTIONS, SECTIONS, editProfile, missingOf, readProfile, samplesFor, validateForm, type FormDraft, type Profile, type Section } from '../../services/profile';
import { entryMatches, type Match } from './match';
import { taRead } from '../../state/areas/talent-a';
import { draftCv } from '../../q/skills/talent-a';
import type { QAction } from '../../state/domain';

type View = 'profile' | 'form' | 'jobs' | 'cv';
const act = (a: QAction) => void runAction(a);
const say = (text: string) => act({ label: text, act: { t: 'say', text } });
const op = (name: string, args: Record<string, unknown> = {}) => act({ label: name, act: { t: 'do', o
… [681 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// Readiness to apply (SC-162/165/176), rebuilt on the one store: six separate measures read from the
// person's own career space (J7) and profile, each with its basis. No overall score anywhere (addendum 08 §3).
// Private to the person; nothing here is shown to employers.
import { useEffect } from 'react';
import { Canvas } from '../ds/Workspace';
import { Glyph } from '../ds/Glyph';
import { actorOf, update, useWorld } from '../mock/world';
import { runAction } from '../q/core/engine';
import { compById, gapsFor, j7, occById, personaFor, readJ7, shown, stateOf, fmtDay } from '../journeys/career/j7';
import { missingOf, readProfile } from '../services/profile';
import { taRead } from '../state/areas/talent-a';

export function Career() {
  const w = useWorld((x) => x);
  const a = actorOf(w); const pid = a.personId ?? 'p_amaka';
  useEffect(() => { if (!w.j7[pid]) update((d) => { j7(d, pid); }); }, [w.j7, pid]);
  const P = personaFor(pid); const S = readJ7(w, pid); const goal = occById(P, S.goal)!;
  const p = readProfile(w, pid); const cv = taRead(w).cv[pid];
  const g = gapsFor(w, pid, S, goal);
  const practice = S.record.filter((r) => r.cls === 'Practice attempt');
  const done = S.plan.filter((s) => s.done).length;
  const checklist = [
    { item: 'Profile set up (claims in your words)', done: p.done },
    { item: 'Where you can work is filled in', done: !missingOf(p).includes('location') },
    { item: 'CV lines approved', done: cv?.status === 'APPROVED' },
    { 
… [3924 more characters trimmed]
```
  </details>

- 🔧 `Read`: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bgzftuo99.txt

  <details><summary>result</summary>

```
1	// Your profile (T1). The global Q drives set-up by conversation; this canvas shows the profile being built,
2	// and offers the same three ways in: talk to Q, upload a CV (simulated parse) or a short form, switchable
3	// at any time. Everything shown here is a CLAIM in the person's own words until evidence backs it up.
4	import { useMemo } from 'react';
5	import { AnimatePresence, motion } from 'motion/react';
6	import { Glyph } from '../../ds/Glyph';
7	import { Canvas } from '../../ds/Workspace';
8	import { Link } from '../../ui/router';
9	import { actorOf, update, useWorld } from '../../mock/world';
10	import { runAction, useViewState } from '../../q/core/engine';
11	import { QUESTIONS, SECTIONS, editProfile, missingOf, readProfile, samplesFor, validateForm, type FormDraft, type Profile, type Section } from '../../services/profile';
12	import { entryMatches, type Match } from './match';
13	import { taRead } from '../../state/areas/talent-a';
14	import { draftCv } from '../../q/skills/talent-a';
15	import type { QAction } from '../../state/domain';
16	
17	type View = 'profile' | 'form' | 'jobs' | 'cv';
18	const act = (a: QAction) => void runAction(a);
19	const say = (text: string) => act({ label: text, act: { t: 'say', text } });
20	const op = (name: string, args: Record<string, unknown> = {}) => act({ label: name, act: { t: 'do', op: name, args } });
21	
22	export function Onboarding() {
23	  const w = useWorld((x) => x);
24	  const a = actorOf(w);
25	  const pid = a.pe
… [30401 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List captures and capture script

  <details><summary>result</summary>

```
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png
captures/cx/T1:
d-01-signup.png
d-02-profile-start.png
d-03-cv-unreadable.png
d-04-form-mistake.png
d-05-profile-built.png
d-05b-proactive.png
d-06-atlas.png
d-07-skills.png
d-08-matches.png
d-09-rehearsal.png
d-10-cv-draft.png
d-11-applied.png
d-12-jobs-applied.png
d-13-cv-saved.png
d-14-thread.png
m-01-signup.png
m-02-profile-start.png
m-03-cv-unreadable.png
m-04-form-mistake.png
m-05-profile-built.png
m-05b-proactive.png
m-06-atlas.png
m-07-skills.png
m-08-matches.png
m-09-rehearsal.png
m-10-cv-draft.png
m-11-applied.png
m-12-jobs-applied.png
m-13-cv-saved.png
m-14-thread.png

captures/cx/T2:
d-01-atlas.png
d-02-transferable.png
d-03-plan-pm.png
d-04-plan-ba.png
d-05-adjusted.png
d-06-practice-not-proof.png
d-07-assessed.png
d-08-three-weeks-later.png
d-09-what-changed.png
d-10-progress.png
d-11-openings.png
d-12-record.png
d-13-plan-final.png
d-14-readiness.png
m-01-atlas.png
m-02-transferable.png
m-03-plan-pm.png
m-04-plan-ba.png
m-05-adjusted.png
m-06-practice-not-proof.png
m-07-assessed.png
m-08-three-weeks-later.png
m-09-what-changed.png
m-10-progress.png
m-11-openings.png
m-12-record.png
m-13-plan-final.png
m-14-readiness.png
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
// Design review captures: every route as the person who uses it, desktop (1440×900) and phone (390×844),
// full page. Used for the visual audit and before/after comparison. Usage: node capture-all.mjs
… [2534 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:21

Let me start the dev server and look at the current state captures.

- 🔧 `Bash`: Start dev server on port 5185
- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-01-atlas.png

  <details><summary>result</summary>

```
Command running in background with ID: bsc1ib5lb. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bsc1ib5lb.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/prototype/src; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Capture current pages of my area

  <details><summary>result</summary>

```
200
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/desktop:
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/phone:
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png
```
  </details>

- 🔧 `Bash`: Check dev server failure

  <details><summary>result</summary>

```
error when starting dev server:
Error: Port 5185 is already in use
    at Server.onError (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:45596:18)
    at Server.emit (node:events:519:28)
    at emitErrorNT (node:net:1976:8)
    at process.processTicksAndRejections (node:internal/process/task_queues:90:21)

[exited with code 1]
5
root     10130  0.0  0.0   4476  3416 ?        Ss   12:21   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1793261910654-oc4bgy.sh 2>/dev/null || true && \builtin export BUN_OPTIONS="--smol${BUN_OPTIONS:+ $BUN_OPTIONS}" && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cat /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bsc1ib5lb.output; ps aux | grep -c "vite --port 5185"; ps aux | grep "5185" | head -3' < /dev/null && pwd -P >| /tmp/claude-af80-cwd
root     10135  0.0  0.0   3548  1936 ?        S    12:21   0:00 grep 5185
root     12253  0.0  0.4 1199124 77324 ?       Sl   09:14   0:00 npm exec vite --port 5185 --strictPort
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/desktop/p_chidi_c_career.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/desktop/p_chidi_c_growth.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/desktop/p_amaka_c_welcome.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/phone/p_chidi_c_career.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:22

[Image: original 780x2706, displayed at 576x2000. Multiply coordinates by 1.35 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-07-assessed.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-10-progress.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-02-transferable.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-12-record.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-03-plan-pm.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-06-practice-not-proof.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-08-three-weeks-later.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T1/d-05-profile-built.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Read DS motion, workspace exports, tokens

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
… [3629 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read Canvas, Glyph, base tokens

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
… [4865 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read DS base tokens and class names

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
… [3395 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:22

Now the T2 test script to know what selectors I must keep.

- 🔧 `Bash`: Find selectors used in T2 test

  <details><summary>result</summary>

```
16:for (const [v, vp, dpr] of [['d', { width: 1440, height: 900 }, 1], ['m', { width: 390, height: 844 }, 2]].filter(([x]) => ONLY.includes(x))) {
23:  const shot = async (n) => { await page.waitForTimeout(350); await page.screenshot({ path: `${ROOT}${v}-${n}.png` }); };
26:  const openQ = async () => { if (!phone) return; if (await page.locator('#q-ask').isVisible().catch(() => false)) return; await page.locator('.ds-askbar button').first().click(); await page.locator('#q-ask').waitFor(); };
27:  const closeQ = async () => { if (!phone) return; const x = page.getByRole('button', { name: 'Close Q' }); if (await x.isVisible().catch(() => false)) await x.click(); await page.waitForTimeout(250); };
30:    for (let i = 0; i < 40; i++) { const th = (await world()).q.threads.p_chidi ?? []; const k = th.map((m) => m.text).lastIndexOf(t); if (k >= 0 && th.slice(k + 1).some((m) => m.who !== 'me')) break; await page.waitForTimeout(100); }
31:    await page.waitForTimeout(wait);
35:  const chip = async (re, wait = 650) => { await openQ(); await page.locator('.ds-chip').filter({ hasText: re }).last().click(); await page.waitForTimeout(wait); };
37:  const canvas = () => page.locator('.ds-canvas').first().innerText();
40:  const visible = async (org) => { const w = await world(); return w.evidence.filter((e) => e.ownerId === 'p_chidi' && e.kind !== 'PRACTICE' && !(e.revokedFrom ?? []).includes(org) && (e.visibility === 'PUBLIC_PROFILE' || (e.visibility === 'SHARED_WITH' && e.sharedWith.in
… [1311 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Show T2 step assertions
- 🔧 `Bash`: Show T1 selectors

  <details><summary>result</summary>

```
6:  step('Discovery: atlas opens from sales, goal is Associate PM', /From sales, the closest roles/.test(r) && /Associate Product Manager/.test(r) && (await page.evaluate(() => location.hash)).includes('/c/career'), r);
11:  step('Transferable skills come from the verified sales evidence', /verified sales work/.test(r) && /stakeholder conversations/.test(r) && /working with numbers and targets, verified/.test(r), r);
13:  step('Skills view shows the verified source and evidence vs gaps', /Bole Distributors/.test(await canvas()) && /Transferable, partial/.test(await canvas()));
17:  step('Evidence vs gaps, competency by competency', /Partly shown \(transferable, not the same thing\): Stakeholder conversations/.test(r) && /Not shown yet: Product writing and User research/.test(r) && /not that you can’t do it/.test(r), r);
21:  step('Plan with practice, work sample and learning steps', /practice/.test(r) && /work sample/.test(r) && /learning/.test(r), r);
23:  step('Progress: a practice step is marked done (private)', (await J()).plan.find((s) => s.id === 'c1')?.done === true && /Marked done/.test(r), r);
25:  step('Progress: the learning step is half done', (await J()).plan.find((s) => s.id === 'c2')?.progress === 50, r);
31:  step('Curveball [mind]: goal changes to BA, PM archived', j.goal === 'ba' && j.archived[0]?.occ === 'apm' && /Business Analyst is your goal now/.test(r), r);
32:  step('Shared progress carried over (discovery notes done, course 50%)', j.plan.find((s) => s
… [3727 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
25:  const openQ = async () => { if (!phone) return; if (await page.locator('#q-ask').isVisible().catch(() => false)) return; await page.locator('.ds-askbar button').first().click(); await page.locator('#q-ask').waitFor(); };
26:  const closeQ = async () => { if (!phone) return; const x = page.getByRole('button', { name: 'Close Q' }); if (await x.isVisible().catch(() => false)) await x.click(); await page.waitForTimeout(250); };
37:  const chip = async (re, wait = 650) => { await openQ(); const c = page.locator('.ds-chip').filter({ hasText: re }).last(); await c.click(); await page.waitForTimeout(wait); };
38:  const canvas = () => page.locator('.ds-canvas').first().innerText();
45:  step('Starts signed out on sign-up', /Create your account/.test(await page.locator('body').innerText()));
47:  await page.getByRole('button', { name: 'Continue', exact: true }).click();
48:  await page.fill('#su-code', '123456'); await page.getByRole('button', { name: 'Verify' }).click();
49:  await page.getByRole('button', { name: /looking for work/ }).click(); await page.getByRole('button', { name: 'Continue', exact: true }).click();
50:  await page.getByRole('button', { name: 'Start' }).click(); await page.waitForTimeout(700);
96:  step('Switches to the short form', /short form/.test(r) && /The short form/.test(await canvas()), r);
100:  await page.getByRole('button', { name: 'Save', exact: true }).click(); await page.waitForTimeout(700);
102:  step('Curveball [recover]: form mistake explained
… [1130 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read T2 header and runner

  <details><summary>result</summary>

```
// T2 · Chidi, a sales executive moving into product or business analysis. The career atlas (J7) in depth,
// driven by typing to Q, desktop 1440×900 and phone 390×844: discovery → transferable skills from his verified
// sales evidence → evidence vs gaps → plan (practice, work sample, learning, progress) → assessment →
// three weeks later → reassessment → openings → an explicit, approved share.
// Curveballs: he switches goal from PM to BA and shared progress carries over [mind]; he disagrees with a step
// and Q explains, then adjusts [mind]; he passes a quiz but has no practical evidence, and his
// recruiter-visible profile stays unchanged [info]; he returns three weeks later (simulated) [recover];
// he says "undo" after a change [recover]. Usage: node T2.mjs [d,m]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
import { mkdirSync } from 'node:fs';
const ROOT = new URL('../../../captures/cx/T2/', import.meta.url).pathname; mkdirSync(ROOT, { recursive: true });
const BASE = process.env.BASE || 'http://localhost:5185/';
const ONLY = (process.argv[2] || 'd,m').split(',');
const b = await pw.chromium.launch();
const results = []; const errors = [];
for (const [v, vp, dpr] of [['d', { width: 1440, height: 900 }, 1], ['m', { width: 390, height: 844 }, 2]].filter(([x]) => ONLY.includes(x))) {
  const ctx = await b.newContext({ viewport: vp, deviceScaleFactor: dpr });
  const page = await ctx.newPage();
  page.on('pageerror', (e) => errors.push(`${v}: ${e.mes
… [935 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Save before captures and run baseline tests

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t2-base.log:31
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t1-base.log:38
```
  </details>

- 🔧 `Bash`: Refresh before captures from baseline run
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/T2/d-14-readiness.png

  <details><summary>result</summary>

```
d-01-atlas.png
d-02-transferable.png
d-03-plan-pm.png
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Read persona types

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
… [1685 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Look for motion atlas requirement ids

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
MO-001,Q orb idle,app:idle,Q Home and interview,Static gold icon,PROTOTYPED,/r/home,,D
MO-002,Q listens,voice:recording,Voice interview,Listening text and transcript,PROTOTY
MO-003,Q thinks,run:accepted,All run views,Accepted task label,PROTOTYPED,/r/mandate,S
MO-004,Q speaks,voice:audio-out,Voice/video,Captions,RESEARCHED,,,
MO-005,Q interrupted,voice:interrupted,Voice/video,State text,RESEARCHED,,,
MO-006,Q disconnected,transport:lost,Any run,Connection lost banner,PROTOTYPED,/r/sour
MO-007,Q reconnected,transport:restored,Any run,Connected message,PROTOTYPED,/r/sourci
MO-008,Task plan grows,plan:created,Q planner,Static checklist,PROTOTYPED,/r/plan,capt
MO-009,Parallel agents start,task:spawned,Run explorer,Task list,PROTOTYPED,/r/sourcin
MO-010,Research source found,source:retrieved,Research explorer,Source list update,PRO
MO-011,First candidate arrives,candidate:retrieved,Explore Talent,Instant card,PROTOTY
MO-012,Candidate evidence loaded,evidence:ready,Candidate deep profile,Evidence text,P
MO-013,Candidate comparison morph,compare:changed,Compare candidates,Direct table redr
MO-014,Job preference filter,filter:changed,Explore Jobs,Direct redraw,RESEARCHED,,,
MO-015,Mandate wording revised,mandate:patched,Mandate builder,Text
… [2169 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find motion ids relevant to J7

  <details><summary>result</summary>

```
motion_id,name,event_trigger,primary_surface,reduced_motion_fallback,status,route,evidence,note
MO-012,Candidate evidence loaded,evidence:ready,Candidate deep profile,Evidence text,PROTOTYPED,/r/plan,captures/journeys/f6-*,Findings arrive one by one as the evidence agent finishes each check.
MO-016,Uploaded file accepted,file:received,Uploader,Percentage text,PROTOTYPED,/c/welcome,prototype/src/journeys/onboarding/Onboarding.tsx (view transition); prototype/src/styles/talent-b.css (.tb-ba
MO-022,Interview progress,interview:coverage-updated,Interview room,Text x of y,RESEARCHED,,,
MO-036,Model/provider error,run:failed,Run explorer,Error explanation,PROTOTYPED,/r/calendar/connect,prototype/src/screens/CalendarSetup.tsx (legacy bridge); shown in captures/video/F1-*.mp4,"Re-point
MO-048,J7 career path explored,career:path_selected,Career map,Linear roadmap,PROTOTYPED,/c/career,captures/journeys/j7-*,Atlas/bands: selection and role sheet open; family collapse/expand at 48 occup
MO-049,J7 gap evidence expanded,career:gap_open,Gap view,Expandable details,PROTOTYPED,/c/career,captures/journeys/j7-*,Evidence expands in place (proves / does not prove).
MO-050,J7 practice feedback arrived,practice:feedback_ready,Practice,Plain feedback sections,PROTOTYPED,/c/career,prototype/src/journeys/career/Career.tsx (competency glyph keyed by state scales in; r
MO-051,J7 comparable growth trend,career:progress_loaded,Career progress,Table of attempts,PROTOTYPED,/c/career,captures/journeys/j7-*,P
… [551 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/career/Route.tsx

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/prototype/src/journeys/career/Route.tsx (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Edit radial atlas: rings, labels, route line, legend

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Rewrite phone band atlas

  <details><summary>result</summary>

```
142:      {narrow && (
```
  </details>

- 🔧 `Bash`: Tweak list view copy and targets

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Check step kinds and view ids used by Q

  <details><summary>result</summary>

```
1 kind: 'Credential'
      3 kind: 'Learning'
      5 kind: 'Practice'
      8 kind: 'Work sample'
48:    actions: [say('I don’t know what to write', 'i dont know what to write'), say('Skip this one', 'skip this'), op('Upload a CV instead', 'ta.cv.choose'), op('Use the short form', 'ta.view', { route: '/c/welcome', view: 'form', say: 'Here’s the short form. Fill in what you like; I’ll check it when you save.' })] })];
198:        actions: [...samplesFor(pid).filter((s) => s.kind === 'pdf').map((s) => op(`Upload ${s.file} instead`, 'ta.cv.read', { file: s.file, kind: 'pdf' }, true)), say('Tell Q instead', 'set up my profile'), op('Fill in the short form', 'ta.view', { route: '/c/welcome', view: 'form', say: 'Here’s the short form. Fill in what you like; I’ll check it when you save.' })] });
214:registerOp('ta.view', (w, a, actor) => {
      1 view: 'cv'
      3 view: 'form'
      1 view: 'jobs'
      1 view: 'opps'
      1 view: 'plan'
      6 view: 'profile'
```
  </details>

- 🔧 `Bash`: Rewrite J7 shell: kicker, tabs, route, map/list

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Rewrite skills view and role sheet

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Rewrite plan, progress, record views; typecheck

  <details><summary>result</summary>

```
src/journeys/career/Career.tsx(17,137): error TS6133: 'shown' is declared but its value is never read.
src/journeys/career/Career.tsx(22,7): error TS6133: 'LADDER' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Remove unused symbols and recheck types

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Add CSS for new J7 patterns

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 12:31

You've hit your 5-hour limit · resets 1:50pm (UTC)


**User** · 2026-10-29 13:51

The coordinator sent a message while you were working:
From the lead: the usage limit has reset. Please carry on with the design pass from exactly where you stopped. Your brief and my follow-up messages (handoff doc, SwitchRow) still apply. Note that src/journeys/career/Career.tsx currently fails to type-check (unused imports and a prop mismatch), probably mid-edit. Finish that first.

Address this before completing your current task.

- 🔧 `Bash`: Recheck types and read SwitchRow

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
 M src/journeys/career/Atlas.tsx
 M src/journeys/career/Career.tsx
 M src/styles/talent-a.css
?? src/journeys/career/Route.tsx
```
  </details>

- 🔧 `Bash`: Capture each J7 tab desktop and phone

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v1/d-Atlas.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v1/d-Your_skills.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v1/d-Plan.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v1/m-Atlas.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 13:53

[Image: original 390x2089, displayed at 373x2000. Multiply coordinates by 1.05 to map to original image.]

- 🔧 `Bash`: Route copy, alignment, toggle placement

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Rebuild readiness page

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Profile section marks, progress, kicker

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Add level pips to assessment Q card

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Run T1 and T2 journeys after changes
- 🔧 `Bash`: Capture growth, career tabs, welcome

  <details><summary>result</summary>

```
Command running in background with ID: bl8maak10. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bl8maak10.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>


  <details><summary>result</summary>

```
01-landing.png
02-landing-2.png
03-landing-3.png
04-start.png
05-start-mic.png
06-signin.png
07-workspace.png
08-hire-start.png
09-brief.png
10-feas.png
11-brief2.png
12-night.png
13-morning.png
14-person-lens.png
15-list-lens.png
16-draft.png
17-yes.png
18-live.png
19-observe.png
20-decide.png
21-offer-sent.png
22-accepted.png
d-Assoc_PM.png
d-Atlas.png
d-Progress.png
d-Record.png
d-x.png
m-Assoc_PM.png
m-Atlas.png
m-Progress.png
m-Record.png
m-x.png
s1.jpg
s2.jpg
s3.jpg
s4.jpg
s5.jpg
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v2/d-x.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v2/d-Assoc_PM.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v2/d-Record.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/v2w/m-Profile.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: List Q skills, ops, rules and service exports

  <details><summary>result</summary>

```
q/skills/talent-a.ts:registerOp('ta.apply.submit'
q/skills/talent-a.ts:registerOp('ta.apply.withdraw'
q/skills/talent-a.ts:registerOp('ta.cv.approve'
q/skills/talent-a.ts:registerOp('ta.cv.choose'
q/skills/talent-a.ts:registerOp('ta.cv.read'
q/skills/talent-a.ts:registerOp('ta.form.fix'
q/skills/talent-a.ts:registerOp('ta.form.save'
q/skills/talent-a.ts:registerOp('ta.j7.goal.set'
q/skills/talent-a.ts:registerOp('ta.j7.quiz.answer'
q/skills/talent-a.ts:registerOp('ta.j7.quiz.start'
q/skills/talent-a.ts:registerOp('ta.j7.reschedule'
q/skills/talent-a.ts:registerOp('ta.j7.restore'
q/skills/talent-a.ts:registerOp('ta.j7.sample.submit'
q/skills/talent-a.ts:registerOp('ta.j7.step.move'
q/skills/talent-a.ts:registerOp('ta.j7.step.remove'
q/skills/talent-a.ts:registerOp('ta.j7.step.toggle'
q/skills/talent-a.ts:registerOp('ta.share.do'
q/skills/talent-a.ts:registerOp('ta.share.undo'
q/skills/talent-a.ts:registerOp('ta.time.skip'
q/skills/talent-a.ts:registerOp('ta.view'
services/profile.ts:7:export type Track = 'graduate' | 'switcher' | 'experienced';
services/profile.ts:8:export type Confidence = 'sure' | 'check';
services/profile.ts:9:export interface Claim { id: string; text: string; source: 'CV' | 'CONVERSATION' | 'YOU'; confidence: Confidence; flagged?: string }
services/profile.ts:10:export type ExpKind = 'job' | 'project' | 'volunteer' | 'course';
services/profile.ts:11:export interface Experience { id: string; kind: ExpKind; title: string; org: string; when: string; claims: C
… [5894 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read skill ids, rules, matching and CV parse

  <details><summary>result</summary>

```
22:const reg = (s: Skill) => registerSkill({ ...s, match: (c) => { const v = s.match(c); return v <= 0 ? 0 : OWN.has(c.actor.personId ?? '') ? Math.min(0.99, v 
11:  id: 'ta.plan.overdue', side: 'candidate', priority: 'normal',
24:  id: 'ta.jobs.new', side: 'candidate', priority: 'normal',
39:  id: 'ta.commitment.due', side: 'candidate', priority: 'high',
52:  id: 'ta.j7.back', side: 'candidate', priority: 'normal',
64:  id: 'ta.profile.missing', side: 'candidate', priority: 'normal',
export interface Match { job: Job; org: string; needs: NeedFit[]; fit: number; notes: string[]; applied?: string; isNew: boolean }

export const isEntry = (j: Job) => j.status === 'OPEN' && !/\b(senior|lead|staff|head|principal)\b/i.test(j.title) && (/\b(junior|graduate|trainee|assistant|associate|analyst)\b/i.test(j.title) || /\bI\b/.test(j.title));

export function needStatus(w: World, pid: string, need: string): NeedFit {
  const kws = NEED_KWS[need] ?? [need.toLowerCase()];
  const ev = w.evidence.find((e) => e.ownerId === pid && e.kind !== 'CLAIM' && e.kind !== 'PRACTICE' && kws.some((k) => `${e.title} ${e.shows}`.toLowerCase().includes(k.trim())));
  if (ev) return { need, state: 'evidenced', basis: `${ev.title} (${ev.verification === 'VERIFIED' ? 'checked' : 'in your Passport'})` };
  const p = readProfile(w, pid);
  const txt = ` ${profileText(p)} `;
  const k = kws.find((x) => txt.includes(x));
  if (k) {
    const claim = p.experience.flatMap((e) => e.claims).find((c) => c.text.toLower
… [3255 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read skill list, CV drafting, apply and share ops

  <details><summary>result</summary>

```
const reg = (s: Skill) => registerSkill({ ...s, match: (c) => { const v = s.match(c); return v <= 0 ? 0 : OWN.has(c.actor.personId ?? '') ? Math.min(0.99, v + 0.06) : v * 0.85; } });
const cand = (c: QCtx) => c.actor.side === 'candidate' && !!c.actor.personId;
const pidOf = (a: Actor) => a.personId!;
const reply = (text: string, extra: Partial<ReplyMsg> = {}): ReplyMsg => ({ kind: 'reply', text, ...extra });
const say = (label: string, text: string, primary = false): QAction => ({ label, primary, act: { t: 'say', text } });
const nav = (label: string, to: string, primary = false): QAction => ({ label, primary, act: { t: 'nav', to } });
const op = (label: string, name: string, args: Record<string, unknown> = {}, primary = false): QAction => ({ label, primary, act: { t: 'do', op: name, args } });
const ui = (w: World, actorId: string, route: string, patch: Record<string, unknown>) => Object.assign((w.q.ui[`${actorId}|${route}`] ??= {}), patch);
const list = (xs: string[]) => (xs.length <= 1 ? xs.join('') : `${xs.slice(0, -1).join(', ')} and ${xs[xs.length - 1]}`);
448:export function draftCv(p: Profile): CvLine[] {
449-  const lines: CvLine[] = [];
450-  if (p.study) lines.push({ id: 'l_study', text: `${p.study.replace(/,?\s*\bi (finished|graduated|completed|left)\b.*$/i, '').replace(/\.$/, '')}${p.year && !p.study.includes(`(${p.year})`) && !/\b(19|20)\d{2}\b/.tes
451-  for (const e of p.experience) for (const cl of e.claims) {
452-    const body = polish(cl.text);
453-    con
… [3736 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List skill ids

  <details><summary>result</summary>

```
69:reg({
159:reg({
160:  id: 'ta.nowork', side: 'candidate',
176:reg({
177:  id: 'ta.cv.upload', side: 'candidate',
219:reg({
220:  id: 'ta.form', side: 'candidate',
250:reg({
251:  id: 'ta.formfix', side: 'candidate',
276:reg({
277:  id: 'ta.profile.add', side: 'candidate',
325:reg({
326:  id: 'ta.jobs', side: 'candidate',
339:reg({
340:  id: 'ta.jobs.why', side: 'candidate',
353:reg({
354:  id: 'ta.apply', side: 'candidate',
401:reg({
402:  id: 'ta.rehearse', side: 'candidate',
426:reg({
427:  id: 'ta.rehearse.again', side: 'candidate',
461:reg({
462:  id: 'ta.cv', side: 'candidate',
490:reg({
491:  id: 'ta.cv.invent', side: 'candidate',
519:reg({
520:  id: 'ta.j7.discover', side: 'candidate',
533:reg({
534:  id: 'ta.j7.skills', side: 'candidate',
552:reg({
553:  id: 'ta.j7.gaps', side: 'candidate',
565:reg({
566:  id: 'ta.j7.role', side: 'candidate',
582:reg({
583:  id: 'ta.j7.goal', side: 'candidate',
606:reg({
607:  id: 'ta.j7.plan', side: 'candidate',
619:reg({
620:  id: 'ta.j7.step', side: 'candidate',
656:reg({
34
id: 'ta.apply' id: 'ta.commit' id: 'ta.commit.drop' id: 'ta.cv' id: 'ta.cv.invent' id: 'ta.cv.upload' id: 'ta.form' id: 'ta.formfix' id: 'ta.j7.changes' id: 'ta.j7.disagree' id: 'ta.j7.discover' id: 'ta.j7.gaps' id: 'ta.j7.goal' id: 'ta.j7.learn' id: 'ta.j7.notproof' id: 'ta.j7.plan' id: 'ta.j7.quiz' id: 'ta.j7.role' id: 'ta.j7.sample' id: 'ta.j7.skills' id: 'ta.j7.step' id: 'ta.j7.view' id: 'ta.jobs' id: 'ta.jobs.why' id: 'ta.nowork' id: 'ta.privacy' id: 't
… [85 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check journey test progress

  <details><summary>result</summary>

```
<tool_use_error>Blocked: sleep 60 followed by: cat /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bl8maak10.output S=/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad tail -3 $S/t2-a.log $S/t1-a.log. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```
  </details>

- 🔧 `Bash`: Check journey test progress

  <details><summary>result</summary>

```
53
```
  </details>

- 🔧 `Bash`: Check handoff dir and proactive rules

  <details><summary>result</summary>

```
AUDIT-BATCH1.md
BUILD-BRIEF.md
DESIGN-PASS-BRIEF.md
JOURNEY-MAP.md
193:export function canDiscover(w: World, pid: string, orgId: string) {
201:export function canSeeCandidate(w: World, pid: string, orgId: string) {
206:export function visibleEvidence(w: World, personId: string, viewerOrgId: string) {
24:  id: 'ta.jobs.new', side: 'candidate', priority: 'normal',
25-  evaluate: (w, a) => {
26-    if (!a.personId || personaFor(a.personId).id !== 'graduate') return [];
27-    const p = readProfile(w, a.personId); if (!p.answered.length) return [];
28-    const seen = taRead(w).seenJobs[a.personId] ?? [];
29-    const m = entryMatches(w, a.personId).find((x) => x.isNew && !x.applied && !seen.includes(x.job.id));
30-    if (!m) return [];
--
52:  id: 'ta.j7.back', side: 'candidate', priority: 'normal',
53-  evaluate: (w, a) => {
54-    if (!a.personId || !w.j7[a.personId]) return [];
55-    const S = readJ7(w, a.personId); const gap = daysBetween(S.lastVisit, simISO(w));
56-    if (gap < 14) return [];
57-    return [{ subject: S.lastVisit.slice(0, 10), text: `Welcome back. It’s been ${Math.round(gap / 7)} weeks since you last looked at your career plan. Want a summary of what changed?`,
58-      why: `Your last visit to your plan was ${fmtDay(S.lastVisit)}. Since then, dates have passed and practice has aged.`,
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/talent-a.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/talent-a.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check test status

  <details><summary>result</summary>

```
62
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t1-a.log
37
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-10-progress.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/d-07-assessed.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/m-07-assessed.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/m-14-readiness.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Move practice lane label; wrap key on phones

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Put practice lane label in the axis column

  <details><summary>result</summary>

```
1
```
  </details>

- 🔧 `Bash`: Simplify lane label, explain in caption

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Read test results

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t2-a.log:62
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t1-a.log:76

[exited with code 0]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T1/d-05-profile-built.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T1/d-06-atlas.png
- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T1/m-07-skills.png

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

- 🔧 `Bash`: Truncate quoted claims at word boundary

  <details><summary>result</summary>

```
99:  if (m) { const t = m.replace(/\.$/, ''); const cut = t.length > 90 ? `${t.slice(0, 90).replace(/\s+\S*$/, '')}…` : t; return `You said: “${cut}”. A claim until it’s shown.`; }
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/m-13-plan-final.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T2/m-12-record.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Capture after screens for my routes

  <details><summary>result</summary>

```
Exit code 2
captured 102 pages to captures/review/after
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png
```
  </details>

- 🔧 `Bash`: Create before/after pairs

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
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/talent-a/04-after.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Shorten route subline, recapture, fix pair 04

  <details><summary>result</summary>

```
done
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/phone/p_chidi_c_career.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:04

[Image: original 780x4150, displayed at 376x2000. Multiply coordinates by 2.07 to map to original image.]

- 🔧 `Bash`: Rerun T1 and T2 after final edits
- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/talent-a.md

  <details><summary>result</summary>

```
Command running in background with ID: b3peyfj1f. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b3peyfj1f.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>


  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/talent-a.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `ToolSearch`: select:Monitor

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Monitor`: T1/T2 journey rerun result

  <details><summary>result</summary>

```
Monitor started (task b0ymorxcj, expires in 30m unless the source ends first; you get one notice at expiry — re-arm if you still need the watch). You will be notified on each event. Keep working — do not poll or sleep. Events may arrive while you are waiting for the user — an event is not their reply.
```
  </details>

- 🔧 `Bash`: Check privacy script usage

  <details><summary>result</summary>

```
// Privacy: candidates' discovery rules hold everywhere a recruiter can reach them — search and pools,
// profiles, Q's tools, cached views and downstream artifacts (campaigns). Usage: node privacy.mjs [base]
import pw from '/opt/node-tools/node_modules/playwright/index.js';
const BASE = process.argv[2] || 'http://localhost:4174/';
let fails = 0; const step = (ok, n, x = '') => { if (!ok) fails++; console.log(`${ok ? 'PASS' : 'FAIL'} ${n}${x ? ` · ${String(x).slice(0, 140)}` : ''}`); };
```
  </details>

- 🔧 `Bash`: Run privacy review script

  <details><summary>result</summary>

```
21
```
  </details>

- 🔧 `Bash`: Wait for the journey rerun to finish

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t2-b.log:62
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t1-b.log:76
tail: option used in invalid context -- 2

[exited with code 1]
```
  </details>

- 🔧 `Bash`: Confirm no failures or page errors

  <details><summary>result</summary>

```
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t2-b.log:0
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/t1-b.log:0

62/62 steps passed
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The talent-a design pass is finished. T1 passes 76/76 and T2 passes 62/62, desktop and phone, with no page errors. `privacy.mjs` passes 21/21. My files type-check cleanly. Nothing is comm

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
