# Helper agent agent-ab94016dc3fcc75bc: Design pass R4 agency pages

Source: `agent-ab94016dc3fcc75bc.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 12:20

Run the design pass for area `agency` (journey R4: Dele at Talentbridge; Tunde is a viewer) in /home/user/neo/talent-q-design/prototype.

**Setup**
- Read /home/user/neo/talent-q-design/journeys/DESIGN-PASS-BRIEF.md first and follow it exactly. That includes loading the named skills with the Skill tool and applying them.
- Read /home/user/neo/talent-q-design/journeys/BUILD-BRIEF.md for the contracts and your file ownership. You own the same `agency` files as before.
- Your dev server port is 5184.

**Pages to cover**
- The agency home.
- All 11 `/r/agency/*` pages: clients, client, mandate, pools, saved searches, pool comparison, campaigns, submittals, agents, notes, documents, reports.

**Known problems to fix**
- **Double navigation.** The in-page section bar duplicates the rail. Decide on one clear information architecture: the rail for the top destinations, in-page navigation only for what is genuinely secondary.
- **Agent monitoring.** Running, failed, paused, interrupted and resumed agents must be understandable at a glance. Use `dataviz` and `interaction-design` for this, including meaningful progress motion with the tokens.
- **Client isolation.** Keeping Kora's and Medlink's records apart must stay visibly obvious.

**Privacy change you must absorb**
The store now enforces candidate privacy (`canSeeCandidate` in mock/world.ts). Talentbridge sees only people who registered with it (seed `registrations`) or whose discovery rules allow agencies. As a result:
- Zara, Chidi and Amaka no longer appear in Talentbridge's pools. The pool shows an anonymous "N people aren't shown" note, which the lead added; make it read well.
- Pool sizes, rankings, comparisons, campaigns and reports change accordingly.
- Agency pages are now guarded by organisation.

Update R4.mjs so it reflects the new, correct behaviour without weakening what any step proves. It must pass. Also run qa/scripts/review/privacy.mjs against your server.

- 🔧 `Bash`: Read the design pass and build briefs

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
… [11032 more characters trimmed]
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

- 🔧 `Bash`: Survey agency files and repo state

  <details><summary>result</summary>

```
Exit code 2
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
src/q/skills/agency.ts
src/q/proactive/agency.ts
src/journeys/agency
src/styles/agency.css
src/state/seeds/agency.ts
src/state/areas/agency.ts
src/routes/agency.tsx
ls: cannot access 'qa/scripts/journeys': No such file or directory
ls: cannot access 'qa/scripts/review': No such file or directory
 M ../captures/cx/R1/d-01-signup.png
 M ../captures/cx/R1/d-02-home-welcome.png
 M ../captures/cx/R1/d-03-draft-v1.png
 M ../captures/cx/R1/d-04-draft-v1-canvas.png
 M ../captures/cx/R1/d-05-budget-below.png
 M ../captures/cx/R1/d-06-version-v1.png
 M ../captures/cx/R1/d-07-back-next-day.png
 M ../captures/cx/R1/d-08-people.png
 M ../captures/cx/R1/d-09-people-canvas.png
 M ../captures/cx/R1/d-10-propose.png
 M ../captures/cx/R2/d-01-compare-payments-go.png
 M ../captures/cx/R2/d-02-chall
… [1190 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List QA scripts and agency file sizes

  <details><summary>result</summary>

```
Exit code 2
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

qa/scripts/review:
axe-all.mjs
capture-all.mjs
interview-followup.mjs
keyboard.mjs
privacy.mjs
model.ts
pages.tsx
    27 prototype/src/routes/agency.tsx
   405 prototype/src/journeys/agency/model.ts
   532 prototype/src/journeys/agency/pages.tsx
    93 prototype/src/styles/agency.css
   490 prototype/src/q/skills/agency.ts
    77 prototype/src/q/proactive/agency.ts
   144 prototype/src/state/areas/agency.ts
    45 prototype/src/state/seeds/agency.ts
  1813 total
u_dele_r_agency_agents.png
u_dele_r_agency_campaigns.png
u_dele_r_agency_client_org_kora.png
u_dele_r_agency_clients.png
u_dele_r_agency_compare.png
u_dele_r_agency_docs.png
u_dele_r_agency_mandate_m_ops.png
u_dele_r_agency_notes.png
u_dele_r_agency_pools.png
u_dele_r_agency_reports.png
u_dele_r_agency_searches.png
u_dele_r_agency_submittals.png
ls: cannot access 'journeys/design': No such file or directory
```
  </details>

- 🔧 `Bash`: Read agency route, model and CSS
- 🔧 `Bash`: Read agency pages

  <details><summary>result</summary>

```
<persisted-output>
Output too large (45.7KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bvibdrazw.txt

Preview (first 2KB):
// Agency pages (R4). Every page shows ONE client at a time (the client in focus), except the agency home and
// the agents monitor, which show each client in its own separate section and never mix candidates.
// Q does the work: each page offers "say it to Q" shortcuts, and every button goes through Q's ops so the
// conversation records what happened.
import { useEffect, useRef, useState, type ReactNode } from 'react';
import { actorOf, update, useWorld, type World } from '../../mock/world';
import type { Actor, MandateX, QAction } from '../../state/domain';
import { STAGE_LABEL } from '../../state/domain';
import { Canvas } from '../../ds/Workspace';
import { Glyph, GLYPH_LABEL, type GlyphKind } from '../../ds/Glyph';
import { QMark, type QAgent } from '../../ds/QMark';
import { Link, navigate } from '../../ui/router';
import { runAction, sendToQ, useViewState } from '../../q/core/engine';
import { agency, type AgentRun, type ClientId, type FitMark, type Pool, type Report, type ReportSection } from '../../state/areas/agency';
import {
  lc, agencyMandates, briefSigned, campaignsFor, canAct, canSeeMandate, clientIds, clientName, clientShort, consentReason, consentState, deniedReason, docsFor, fitOf, fmtDay, focusOf, isolationCheck, isWithdrawn,
  mandateOf, messageFor, mustHavesShown, 
… [694 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
<persisted-output>
Output too large (47.7KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/br4gjdd4b.txt

Preview (first 2KB):
// Routes for R4 (Dele, Talentbridge agency). Owned by this area (see journeys/BUILD-BRIEF.md).
import { registerRoute } from './registry';
import { OrgOnly } from './guard';
import { registerRecruiterHome } from './entry';
import { actorOf, orgOf } from '../mock/world';
import type { IconName } from '../ds/icons';
import { startRunner } from '../journeys/agency/model';
import { AgencyHome, Agents, ClientPage, Clients, Compare, Campaigns, Docs, MandatePage, Notes, Pools, Reports, Searches, Submittals } from '../journeys/agency/pages';
import '../styles/agency.css';

registerRecruiterHome((w) => orgOf(w, actorOf(w).orgId)?.kind === 'AGENCY', () => <AgencyHome />);

const nav = (label: string, icon: IconName, order: number, tab = false) => ({ group: 'Agency', label, icon, order, tab, orgKind: 'AGENCY' as const });
registerRoute({ path: '/r/agency/clients', side: 'recruiter', label: 'clients and mandates', render: () => <OrgOnly orgId="org_tb" what="Talentbridge’s agency workspace"><Clients /></OrgOnly>, nav: nav('Clients', 'org', 11, true) });
registerRoute({ path: '/r/agency/client/:id', side: 'recruiter', label: 'a client', render: (p) => <OrgOnly orgId="org_tb" what="Talentbridge’s agency workspace"><ClientPage id={p.id} /></OrgOnly> });
registerRoute({ path: '/r/agency/mandate/:id', si
… [622 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/routes/agency.tsx
- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/agency/pages.tsx

  <details><summary>result</summary>

```
1	// Routes for R4 (Dele, Talentbridge agency). Owned by this area (see journeys/BUILD-BRIEF.md).
2	import { registerRoute } from './registry';
3	import { OrgOnly } from './guard';
4	import { registerRecruiterHome } from './entry';
5	import { actorOf, orgOf } from '../mock/world';
6	import type { IconName } from '../ds/icons';
7	import { startRunner } from '../journeys/agency/model';
8	import { AgencyHome, Agents, ClientPage, Clients, Compare, Campaigns, Docs, MandatePage, Notes, Pools, Reports, Searches, Submittals } from '../journeys/agency/pages';
9	import '../styles/agency.css';
10	
11	registerRecruiterHome((w) => orgOf(w, actorOf(w).orgId)?.kind === 'AGENCY', () => <AgencyHome />);
12	
13	const nav = (label: string, icon: IconName, order: number, tab = false) => ({ group: 'Agency', label, icon, order, tab, orgKind: 'AGENCY' as const });
14	registerRoute({ path: '/r/agency/clients', side: 'recruiter', label: 'clients and mandates', render: () => <OrgOnly orgId="org_tb" what="Talentbridge’s agency workspace"><Clients /></OrgOnly>, nav: nav('Clients', 'org', 11, true) });
15	registerRoute({ path: '/r/agency/client/:id', side: 'recruiter', label: 'a client', render: (p) => <OrgOnly orgId="org_tb" what="Talentbridge’s agency workspace"><ClientPage id={p.id} /></OrgOnly> });
16	registerRoute({ path: '/r/agency/mandate/:id', side: 'recruiter', label: 'a mandate', render: (p) => <OrgOnly orgId="org_tb" what="Talentbridge’s agency workspace"><MandatePage id={p.id} /></OrgOnly> })
… [1948 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
1	// Agency pages (R4). Every page shows ONE client at a time (the client in focus), except the agency home and
2	// the agents monitor, which show each client in its own separate section and never mix candidates.
3	// Q does the work: each page offers "say it to Q" shortcuts, and every button goes through Q's ops so the
4	// conversation records what happened.
5	import { useEffect, useRef, useState, type ReactNode } from 'react';
6	import { actorOf, update, useWorld, type World } from '../../mock/world';
7	import type { Actor, MandateX, QAction } from '../../state/domain';
8	import { STAGE_LABEL } from '../../state/domain';
9	import { Canvas } from '../../ds/Workspace';
10	import { Glyph, GLYPH_LABEL, type GlyphKind } from '../../ds/Glyph';
11	import { QMark, type QAgent } from '../../ds/QMark';
12	import { Link, navigate } from '../../ui/router';
13	import { runAction, sendToQ, useViewState } from '../../q/core/engine';
14	import { agency, type AgentRun, type ClientId, type FitMark, type Pool, type Report, type ReportSection } from '../../state/areas/agency';
15	import {
16	  lc, agencyMandates, briefSigned, campaignsFor, canAct, canSeeMandate, clientIds, clientName, clientShort, consentReason, consentState, deniedReason, docsFor, fitOf, fmtDay, focusOf, isolationCheck, isWithdrawn,
17	  mandateOf, messageFor, mustHavesShown, notesFor, peopleFor, personName, pipelineFor, poolsFor, PRIORITY, ranked, removedMembers, RUN_STATE, runsFor, searchesFor, setFocus, submittalsFor, to
… [47147 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/journeys/agency/model.ts
- 🔧 `Read`: /home/user/neo/talent-q-design/prototype/src/styles/agency.css

  <details><summary>result</summary>

```
1	/* Agency area (R4). Direction D: paper canvas, ink thread, gold only for Q. Classes prefixed .agency- */
2	.agency-subnav { position: relative; display: flex; flex-wrap: wrap; gap: 4px; margin: -4px 0 0; }
3	.agency-subnav a { flex: none; display: inline-flex; align-items: center; min-height: 44px; padding: 0 12px; border-radius: 999px; color: var(--ink-2); text-decoration: none; font-size: 14px; border: 1px solid transparent; }
4	.agency-subnav a:hover { border-color: var(--rule-2); }
5	.agency-subnav a[aria-current='page'] { background: var(--ink); color: var(--paper); }
6	.agency-switch { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
7	.agency-switch .ds-filter { min-height: 44px; }
8	.agency-only { flex-basis: 100%; }
9	.agency-aside { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; justify-content: flex-end; }
10	.agency-viewas { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
11	.agency-viewas .ds-filter { min-height: 44px; }
12	.agency-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 16px; }
13	.agency-row { display: flex; flex-wrap: wrap; gap: 8px 12px; align-items: center; justify-content: space-between; }
14	.agency-row > h2, .agency-row > h3 { margin: 0; }
15	.agency-client, .agency-card, .agency-pool, .agency-search, .agency-camp, .agency-sub, .agency-run { display: grid; gap: 12px; align-content: start; }
16	.agency-client p { margin: 0; }
17	.agency-client > 
… [6657 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
1	// Agency (R4) model: client-scoped selectors, mutations and the simulated multi-agent runner.
2	// Tenant isolation is enforced HERE, not in the views: every selector takes the client in focus and
3	// returns only that client's records, so pages, Q replies and reports cannot mix Kora and Medlink.
4	import { actorOf, canSeeCandidate, emit, getWorld, orgOf, simNow, uid, update, type World } from '../../mock/world';
5	import type { Actor, MandateX } from '../../state/domain';
6	import { agency, area, type AgencyState, type AgentRun, type ClientId, type FitMark, type Pool, type Report, type Submittal } from '../../state/areas/agency';
7	import { appendQ } from '../../q/core/engine';
8	
9	export const AGENCY_ID = 'org_tb';
10	/** Mutable slice inside an update() draft (creates it for worlds saved before this area existed). */
11	export const ag = (w: World): AgencyState => (w.areas.agency ??= area.init()) as AgencyState;
12	export { agency };
13	
14	export const isAgency = (w: World, a: Actor = actorOf(w)) => orgOf(w, a.orgId)?.kind === 'AGENCY';
15	export const clientIds = (w: World): ClientId[] => orgOf(w, AGENCY_ID)?.clients ?? [];
16	export const clientName = (w: World, id: ClientId) => orgOf(w, id)?.name ?? id;
17	export const clientShort = (w: World, id: ClientId) => clientName(w, id).split(' ')[0];
18	export const focusOf = (w: World, actorId = w.session.actor): ClientId => agency(w).focus[actorId] ?? clientIds(w)[0] ?? 'org_kora';
19	export const personName = (w: World
… [37464 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read motion tokens, registry, guard and privacy helpers

  <details><summary>result</summary>

```
// Motion tokens (interaction-design skill: feedback 100–200 ms, orientation 200–400 ms, enter slower than
// exit, decelerate in / accelerate out, nothing functional over 500 ms). Every animation in the shell and
// shared components takes its timing from here; reduced motion is handled globally by MotionConfig.
export const DUR = { fast: 0.1, normal: 0.2, slow: 0.3 } as const;
export const EASE = { standard: [0.2, 0, 0, 1], enter: [0, 0, 0.2, 1], exit: [0.4, 0, 1, 1] } as const;
/** Something new arriving in place (a message, a card, a page): rise 6 px and fade in. */
export const arrive = { initial: { opacity: 0, y: 6 }, animate: { opacity: 1, y: 0, transition: { duration: DUR.normal, ease: EASE.enter } }, exit: { opacity: 0, transition: { duration: DUR.fast, ease: EASE.exit } } } as const;
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
  /** Shown in the rail when set. Groups: 'Q' | 'Hiring' | 'Agency' | 'Knowledge' | 'Grow' | 
… [4667 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect rail nav and Canvas component

  <details><summary>result</summary>

```
4://  2. Navigation is built from the route registry, grouped, and adapts to who is signed in (employer,
27:  const orgKind = useWorld((w) => w.orgs.find((o) => o.id === actorOf(w).orgId)?.kind);
28:  const routes = allRoutes().filter((r) => r.nav && (r.side === actor.side || r.side === 'both') && (!r.nav.orgKind || r.nav.orgKind === orgKind) && (!r.nav.orgIds || r.nav.orgIds.includes(actor.orgId ?? '')));
29:  const groups = GROUP_ORDER.map((g) => ({ g, items: routes.filter((r) => r.nav!.group === g).sort((a, b) => a.nav!.order - b.nav!.order) })).filter((x) => x.items.length);
30:  return { actor, groups, routes };
34:  const { actor, groups, routes } = useNav();
64:  const tabs = routes.filter((r) => r.nav?.tab).sort((a, b) => a.nav!.order - b.nav!.order).slice(0, 4);
84:      <nav className="ds-rail" aria-label="Talent Q navigation">
93:        {groups.map(({ g, items }) => {
96:            <div key={g} className="ds-navgroup">
97:              {collapsible ? <button type="button" className="ds-groupbtn ds-hide-collapsed" aria-expanded={open} onClick={() => setOpenGroups({ ...openGroups, [g]: !open })}><span className="lab">{g}</span><span aria-hidden="true">{open ? '−' : '+'}</span></button> : <span className="lab ds-hide-collapsed">{g}</span>}
99:                <Link key={r.path} to={r.path} current={current(r)} className="ds-navlink" aria-label={rail === 'collapsed' ? r.nav!.label : undefined} title={rail === 'collapsed' ? r.nav!.label : undefined}>
100:              
… [3986 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read AppShell rail code

  <details><summary>result</summary>

```
// The Talent Q shell. Principles:
//  1. Q is present on every product page: the conversation sits beside the page on desktop (resizable,
//     collapsible) and is one tap away on phones (an "Ask Q" bar that opens Q as a sheet).
//  2. Navigation is built from the route registry, grouped, and adapts to who is signed in (employer,
//     agency or candidate). Groups past the first three are collapsible, so the rail never overwhelms.
//  3. Phones get four tabs plus More; Q is always reachable and shows its latest line as a peek.
//  4. The identity menu switches between the prototype's demo people (one per journey), each with
//     their own Q conversation, memory and preferences.
import { useEffect, useMemo, useRef, useState, type ReactNode } from 'react';
import { AnimatePresence, MotionConfig, motion } from 'motion/react';
import { Link, navigate } from '../ui/router';
import { actorOf, resetWorld, update, useWorld } from '../mock/world';
import { allRoutes, type RouteDef } from '../routes/registry';
import { QThread, useQMood } from '../q/QThread';
import { flushOutbox, useQThread } from '../q/core/engine';
import { ICONS } from './icons';
import { QMark } from './QMark';
import { arrive } from './motion';
import { InShell, Split, useNarrow } from './Workspace';
import './ds.css';

const GROUP_ORDER = ['Q', 'Hiring', 'Agency', 'Work', 'Interviews', 'Grow', 'Evidence', 'Organisation', 'You'];
const COLLAPSIBLE = new Set(['Organisation', 'You']);

function useNav() {
  co
… [9883 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read capture script and R4 journey script

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
… [18490 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Start dev server and inspect agency seed/registrations

  <details><summary>result</summary>

```
at Server.emit (node:events:519:28)
    at emitErrorNT (node:net:1976:8)
    at process.processTicksAndRejections (node:internal/process/task_queues:90:21)
// Seed records for R4 (Talentbridge agency, clients Kora Pay and Medlink Health). All fictional.
// Tunde (VIEWER) already exists in the base seed; this adds candidates, two client mandates with
// conflicting work modes for similar backend roles, and their pipelines.
import type { SeedPatch } from '../../mock/world';
import type { MandateX, PipelineEntry } from '../domain';

const P = (personId: string, name: string, headline: string, location: string) => ({ personId, name, headline, location, timezone: 'Africa/Lagos', synthetic: true as const });
const req = (reqId: string, label: string, mustHave: boolean, plain: string) => ({ reqId, label, mustHave, plain });

const mandates: MandateX[] = [
  { id: 'm_tb_kora_pay', orgId: 'org_tb', clientOrgId: 'org_kora', title: 'Payments Platform Engineer', plain: 'Builds the services that move merchants’ money for Kora Pay', team: 'Payments platform', location: 'Lagos (on-site, 4 days)', workMode: 'ONSITE',
    pay: { min: 2000000, max: 2600000, currency: 'NGN', period: 'month' }, status: 'SOURCING', createdBy: 'u_dele',
    requirements: [req('kp1', 'Go in production', true, 'Writes and runs Go services'), req('kp2', 'Payments systems', true, 'Has worked on money movement'), req('kp3', 'On-site in Lagos', true, 'Works from the Lagos office four days a week')],
    versions: [{ v: 
… [2770 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Check why vite failed

  <details><summary>result</summary>

```
error when starting dev server:
Error: Port 5187 is already in use
    at Server.onError (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:45596:18)
    at Server.emit (node:events:519:28)
    at emitErrorNT (node:net:1976:8)
    at process.processTicksAndRejections (node:internal/process/task_queues:90:21)
/bin/bash: line 1: ss: command not found
```
  </details>

- 🔧 `Bash`: Inspect vite config and port

  <details><summary>result</summary>

```
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';

export default defineConfig({
  base: './',
  plugins: [react()],
  resolve: { alias: { '@contracts': fileURLToPath(new URL('../contracts', import.meta.url)) } },
  server: { fs: { allow: ['..'] } },
});
200
```
  </details>

- 🔧 `Bash`: Verify existing server on 5184

  <details><summary>result</summary>

```
import __vite__cjsImport0_react_jsxDevRuntime from "/node_modules/.vite/deps/react_jsx-dev-runtime.js?v=ded3d131"; const jsxDEV = __vite__cjsImport0_react_jsxDevRuntime["jsxDEV"];
import { registerRoute } from "/src/routes/registry.ts";
import { OrgOnly } from "/src/routes/guard.tsx";
21
root      9088  2.9  0.5 1214672 85992 ?       Sl   12:21   0:00 npm exec vite --port 5184 --strictPort
root      9102  0.0  0.0   2820  1980 ?        S    12:21   0:00 sh -c vite --port 5184 --strictPort
root      9103 19.3  1.0 23451956 177964 ?     Rl   12:21   0:02 node /home/user/neo/talent-q-design/prototype/node_modules/.bin/vite --port 5184 --strictPort
root      9683  3.8  0.0   4476  3420 ?        Ss   12:21   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1793261910654-oc4bgy.sh 2>/dev/null || true && \builtin export BUN_OPTIONS="--smol${BUN_OPTIONS:+ $BUN_OPTIONS}" && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'curl -s http://localhost:5184/src/routes/agency.tsx | head -3; ps aux | grep -c "vite --port"; ps aux | grep "vite --port 5184" | head' < /dev/null && pwd -P >| /tmp/claude-7c67-cwd
root      9695  0.0  0.0   3548  1940 ?        S    12:21   0:00 grep vite --port 5184
```
  </details>

- 🔧 `Bash`: Run R4 journey on desktop as baseline

  <details><summary>result</summary>

```
PASS d 11 resume the paused Medlink work from where it stopped
PASS d 12 curveball [info] conflicting requirements: Kora on-site vs Medlink remote
PASS d 13 collaboration note @mentioning Tunde
PASS d 14 client report: Q drafts from Kora only, Dele edits, isolation check, share (simulated)
PASS d 15 curveball [recover] Tunde (Viewer) is denied the confidential Kora record and requests access
PASS d 16 Dele grants access; Tunde can now open the record
PASS d 17 pages render for each client (compare, docs, clients) without mixing

PASS d 1 agency home shows clients, mandates, agents and what needs Dele
PASS d 2 curveball [info] provider outage: agent fails, retries once, Q explains
PASS d 3 curveball [mind] interrupt: "stop the medlink search, kora is urgent"
PASS d 4 retry the failed provider; run recovers without losing work
PASS d 5 saved search re-run by typing, diff shows what is new (Kora only)
PASS d 6 isolation: Q refuses "show medlink's candidates on the kora report"
PASS d 7 submittal by typing: top 5 from the payments pool, consent checked per person
PASS d 8 curveball [info] consent withdrawn: Halima drops out with a visible reason; Q tells Dele
PASS d 9 change of mind: "actually only the top 3", then yes sends (simulated)
PASS d 10 campaign under approved-campaign delegation with limits; withdrawn excluded
PASS d 11 resume the paused Medlink work from where it stopped
PASS d 12 curveball [info] conflicting requirements: Kora on-site vs Medlink remote
PASS d 13 coll
… [626 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read agency area state

  <details><summary>result</summary>

```
// Agency area (R4, Dele at Talentbridge). Pools, saved searches, campaigns, submittals, collaboration notes,
// concurrent agent runs, documents, client reports and access requests. Tenant isolation: EVERY record
// carries clientOrgId, and every view, search, Q reply and report filters by the client in focus.
// Simulated: providers, sends and shares are fictional; statuses say so (SENT_SIMULATED, SHARED_SIMULATED).
import type { World } from '../../mock/world';

export type ClientId = 'org_kora' | 'org_medlink' | string;
export type FitMark = 'verified' | 'full' | 'partial' | 'none';

export interface Pool { id: string; clientOrgId: ClientId; name: string; mandateId: string; members: string[]; createdBy: string }
export interface SavedSearch {
  id: string; clientOrgId: ClientId; mandateId: string; name: string; query: string; keywords: string[];
  lastRunAt: string; results: string[]; newSinceLast: string[];
  /** The (simulated) market this search reads: who matches and since when. */
  universe: { personId: string; since: string }[]; runs: number;
}
export interface CampaignMsg { personId: string; status: 'QUEUED' | 'SENT_SIMULATED' | 'HELD' | 'EXCLUDED'; reason?: string; at?: string; receipt?: string; words: number }
export interface Campaign {
  id: string; clientOrgId: ClientId; poolId: string; mandateId: string; name: string; template: string;
  status: 'DRAFT' | 'RUNNING' | 'PAUSED' | 'DONE';
  limits: { perRun: number; perDay: number; maxWords: number; followUps: 
… [12797 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read privacy check script and m_ops seed refs

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

… [6120 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Run privacy check baseline

  <details><summary>result</summary>

```
PASS Zara (verified employers only) is invisible to Talentbridge
PASS Femi, registered with Talentbridge, is visible to it
PASS unverified employer (Rivers) cannot discover Zara
PASS agency pool hides Zara and says, without naming, that people are hidden · 
Payments engineers
For Payments Platform Engineer
1
Halima Musa
Go engineer, payouts and ledgers · 7 yrs
3 of 3 must-haves shown
Consent to
PASS agency opening Zara’s profile by URL gets a permission state, no data
PASS Q tool refuses for the agency, reveals nothing · I can’t show you Zara’s profile. They haven’t shared it with Talentbridge, and their privacy settings don’t let you find them. If they apply
PASS no campaign message to Zara is queued or sent
PASS Kora opening Talentbridge’s pools by URL sees a permission page, no pools
PASS before: Kora (verified) may find Amaka
PASS after hiding from Kora: Kora can’t see Amaka
PASS Kora reads none of Amaka’s evidence, public items included
PASS Kora profile by URL: permission state
PASS Q tool refuses for Kora · I can’t show you Amaka’s profile. They haven’t shared it with Kora Pay, and their privacy settings don’t let you find them. If they apply or
PASS other employers are unaffected (Medlink can still find Amaka)
PASS Kora keeps what Tobi explicitly shared with it
PASS an employer Tobi never shared with sees nothing, not even public items
PASS Dayo hidden from Kora
PASS search results cache no longer shows Dayo
PASS saved comparison no longer shows Dayo
PASS Zara withdre
… [98 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find person-naming and nav targets in agency skills

  <details><summary>result</summary>

```
11:  deniedReason, draftSubmittal, focusOf, fmtDay, interrupt, isAgency, isWithdrawn, isolationCheck, launchCampaign, mandateOf, messageFor, owners, pauseRun, peopleFor, personName, pipelineFor, poolsFor, prioritise,
52:const RECORDS = /\b(reports?|candidates?|people|pools?|submittals?|shortlists?|notes?|results|lists?|data|records?|pipelines?|names|cvs?|profiles?|searches|search)\b/;
61:      msgs: [{ kind: 'refusal', text: `I can’t do that. ${clientName(c.w, other)}’s candidates, notes and results stay inside ${short(c.w, other)}’s workspace, so I won’t put them in front of ${clientName(c.w, target)} or into anything ${short(c.w, target)} sees, including reports. That’s Talentbridge’s first rule (“Client data stays inside that client’s workspace”), and each candidate agreed to be put forward to a specific client. If someone from ${short(c.w, other)}’s side would also suit ${short(c.w, target)}, I can ask that person for consent to be considered for ${short(c.w, target)} as a separate record.`,
166:    const nowIds = s.universe.filter((u) => u.since <= t).map((u) => u.personId);
167:    const added = nowIds.filter((p) => !isWithdrawn(c.w, p) && !s.results.includes(p));
168:    const dropped = nowIds.filter((p) => isWithdrawn(c.w, p) && s.results.includes(p));
171:      msgs: [{ kind: 'reply', text: `I re-ran “${s.name}” for ${clientName(c.w, client)}. ${total} matches now; ${added.length ? `${added.length} new since ${fmtDay(s.lastRunAt)}: ${added.map((p) => personName(c.w, 
… [10191 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read skill sections that name people

  <details><summary>result</summary>

```
},
});

// ---------------- Saved searches: re-run and diff ----------------
registerSkill({
  id: 'agency.rerun', side: 'recruiter',
  match: (c) => (on(c) && ((/\b(run|rerun|re-run|refresh|redo|repeat|again)\b/.test(c.norm) && /\bsearch\w*\b/.test(c.norm)) || /\b(what is new|anything new|new matches|new people|who is new)\b/.test(c.norm)) && !STOP.test(c.norm) && !/\b(retry|try again)\b/.test(c.norm) ? 0.92 : 0),
  handle: (c) => {
    const client = clientOf(c); const s = findSearch(c.w, c.norm, client);
    if (!s) return say(`${short(c.w, client)} has no saved searches yet.`);
    const t = today(c.w);
    const nowIds = s.universe.filter((u) => u.since <= t).map((u) => u.personId);
    const added = nowIds.filter((p) => !isWithdrawn(c.w, p) && !s.results.includes(p));
    const dropped = nowIds.filter((p) => isWithdrawn(c.w, p) && s.results.includes(p));
    const total = nowIds.filter((p) => !isWithdrawn(c.w, p)).length;
    return {
      msgs: [{ kind: 'reply', text: `I re-ran “${s.name}” for ${clientName(c.w, client)}. ${total} matches now; ${added.length ? `${added.length} new since ${fmtDay(s.lastRunAt)}: ${added.map((p) => personName(c.w, p)).join(', ')}.` : `nothing new since ${fmtDay(s.lastRunAt)}.`}${dropped.length ? ` ${dropped.map((p) => personName(c.w, p)).join(', ')} no longer appear${dropped.length === 1 ? 's' : ''}: withdrew consent.` : ''} I only searched ${short(c.w, client)}’s criteria; nothing was contacted.`,
        used: [`Saved search · ${s.name}
… [8031 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read proactive rules and needsYou

  <details><summary>result</summary>

```
// Proactive help for the agency, from real state only: saved searches with new matches, clients who haven't
// replied to a submittal, failed agents, consent withdrawals, conflicting client requirements, access requests
// and mentions. Each suggestion names one client at a time (never mixes clients' candidates in one card).
import { actorOf, simNow } from '../../mock/world';
import { registerRule } from '../core/proactive';
import { agency } from '../../state/areas/agency';
import { clientName, clientShort, conflicts, fmtDay, isAgency, isWithdrawn, personName, today } from '../../journeys/agency/model';

const P = '/r/agency';

registerRule({
  id: 'agency.agent-failed', side: 'recruiter', priority: 'high',
  evaluate: (w, a) => (!isAgency(w, a) || a.role === 'VIEWER' ? [] : agency(w).runs.filter((r) => r.state === 'FAILED').map((r) => ({
    subject: `${r.id}:${r.attempts}`,
    text: `The ${clientShort(w, r.clientOrgId)} ${r.label.toLowerCase()} failed: ${r.provider} isn’t responding. ${r.done} of ${r.total} profiles are kept.`,
    why: `Agent status is “failed” after ${r.attempts} attempt${r.attempts === 1 ? '' : 's'}; other clients’ agents are still running.`,
    actions: [{ label: 'Retry now', primary: true, act: { t: 'do', op: 'agency.run.retry', args: { id: r.id } } }, { label: 'What happened?', act: { t: 'say', text: 'what happened to the failed search' } }],
  }))),
});

registerRule({
  id: 'agency.consent-withdrawn', side: 'recruiter', priority: 'high',
  evalu
… [12839 more characters trimmed]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/u_dele_r_home.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/u_dele_r_agency_agents.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Capture current agency pages to scratch

  <details><summary>result</summary>

```
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png
p_grace_c_home.png
p_grace_c_interview.png
p_grace_c_start.png
u_dele_r_agency_agents.png
u_dele_r_agency_campaigns.png
u_dele_r_agency_client_org_kora.png
u_dele_r_agency_clients.png
u_dele_r_agency_compare.png
u_dele_r_agency_docs.png
u_dele_r_agency_mandate_m_ops.png
u_dele_r_agency_notes.png
u_dele_r_agency_pools.png
u_dele_r_agency_reports.png
u_dele_r_agency_searches.png
u_dele_r_agency_submittals.png
u_dele_r_home.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/desktop/u_dele_r_agency_pools.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/phone/u_dele_r_agency_agents.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:25

[Image: original 780x3988, displayed at 391x2000. Multiply coordinates by 1.99 to map to original image.]

- 🔧 `Bash`: Inspect router, tag styles and tokens

  <details><summary>result</summary>

```
// Minimal hash router: routes are stable, shareable and work from a static file (low-bandwidth friendly).
import { useSyncExternalStore, type AnchorHTMLAttributes } from 'react';

const read = () => {
  const h = location.hash.replace(/^#/, '') || ((import.meta.env.VITE_START as string | undefined) ?? '/');
  const [path, query = ''] = h.split('?');
  return { path, query: new URLSearchParams(query) };
};
let current = read();
const subs = new Set<() => void>();
window.addEventListener('hashchange', () => { current = read(); subs.forEach((s) => s()); window.scrollTo(0, 0); });

export function useRoute() {
  return useSyncExternalStore((s) => { subs.add(s); return () => subs.delete(s); }, () => current);
}

export function navigate(to: string) { location.hash = to; }

export function Link({ to, current: isCurrent, ...rest }: AnchorHTMLAttributes<HTMLAnchorElement> & { to: string; current?: boolean }) {
  return <a href={`#${to}`} aria-current={isCurrent ? 'page' : undefined} {...rest} />;
}
134:.ds-tag { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; border-radius: 999px; padding: 3px 10px; border: 1px solid var(--rule-2); color: var(--ink-2); white-space: nowrap; }
135:.ds-tag[data-k='ok'] { border-color: var(--ok); color: var(--ok); }
136:.ds-tag[data-k='busy'] { border-color: var(--gold); color: var(--gold-ink); }
137:.ds-tag[data-k='risk'] { border-color: var(--risk); color: var(--risk); }
138:.ds-tag[data-k='warn'] { border-color: var(--warn); col
… [1742 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find other references to agency paths

  <details><summary>result</summary>

```
qa/scripts/review/privacy.mjs:21:await as('u_dele', '/r/agency/pools');
qa/scripts/review/privacy.mjs:34:await as('u_ada', '/r/agency/pools');
qa/scripts/review/capture-all.mjs:9:  u_dele: ['/r/home', '/r/agency/agents', '/r/agency/campaigns', '/r/agency/clients', '/r/agency/client/org_kora', '/r/agency/compare', '/r/agency/docs', '/r/agency/mandate/m_ops', '/r/agency/notes', '/r/agency/pools', '/r/agency/reports', '/r/agency/searches', '/r/agency/submittals'],
qa/scripts/review/axe-all.mjs:10:  u_dele: ['/r/home', '/r/agency/agents', '/r/agency/campaigns', '/r/agency/clients', '/r/agency/client/org_kora', '/r/agency/compare', '/r/agency/docs', '/r/agency/mandate/m_ops', '/r/agency/notes', '/r/agency/pools', '/r/agency/reports', '/r/agency/searches', '/r/agency/submittals', '/r/compare'],
```
  </details>

- 🔧 `Bash`: Check icons, glyph, QMark exports and motion CSS

  <details><summary>result</summary>

```
3:export const ICONS = {
28:export type IconName = keyof typeof ICONS;
q home mail agents roles search people approvals calendar memory org atlas measures passport practice interview welcome more command collapse expand offline reset 
ds/Glyph.tsx:3:export type GlyphKind = 'verified' | 'full' | 'partial' | 'practice' | 'none' | 'unclear';
ds/Glyph.tsx:5:export const GLYPH_LABEL: Record<GlyphKind, string> = { verified: 'Verified', full: 'Evidenced', partial: 'Partial or outdated', practice: 'Practising (private)', none: 'Not shown yet', unclear: 'Unclear' };
ds/Glyph.tsx:6:export function Glyph({ k, size = 20, title }: { k: GlyphKind; size?: number; title?: string }) {
ds/Glyph.tsx:18:export function GlyphKey({ kinds }: { kinds: GlyphKind[] }) {
ds/QMark.tsx:15:export type QMood = 'idle' | 'listening' | 'thinking' | 'working' | 'waiting' | 'blocked' | 'done' | 'offline';
ds/QMark.tsx:16:export interface QAgent { label: string; done: number; total: number; failed?: boolean }
ds/QMark.tsx:18:export const MOOD_LABEL: Record<QMood, string> = {
ds/QMark.tsx:26:export function QMark({ mood = 'idle', agents = [], size = 36, level = 0, title }: { mood?: QMood; agents?: QAgent[]; size?: number; level?: number; title?: string }) {
ds/QMark.tsx:60:export function moodOf({ agents = [], thinking, waiting, blocked, done, offline }: { agents?: QAgent[]; thinking?: boolean; waiting?: boolean; blocked?: boolean; done?: boolean; offline?: boolean }): QMood {
ds/QMark.tsx:71:export function pres
… [638 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Locate motion atlas MO requirements

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
MO-003,Q thinks,run:accepted,All run views,Accepted task label,PROTOTYPED,/r/mandate,Shown in captures/video/F1-*.mp4,Driven by a real state or run event; appears in a journey film. Dedicated 8–20 s clip and reduced-motion capture still to do.
MO-006,Q disconnected,transport:lost,Any run,Connection lost banner,PROTOTYPED,/r/sourcing,Shown in captures/video/F1-*.mp4,Driven by a real state or run event; appears in a journey film. Dedicated 8–20 s c
… [3881 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read dataviz guidance on meters and status
- 🔧 `Bash`: Read mark specs and anti-pattern headings
- 🔧 `Bash`: Read motion principles on progress and timing

  <details><summary>result</summary>

```
8-| The data is... | Use | Not |
9-|---|---|---|
10:| A single current value (+ maybe a trend) | **Stat tile** (value + delta + sparkline) | A one-bar bar chart |
11:| A handful of headline numbers | **KPI row** of stat tiles | A grouped bar chart |
12-| The one number a dashboard leads with | **Hero figure** (>=48px, sans) | - |
13:| A single ratio against a limit | **Meter** (same-ramp track) | A pie of 2 slices |
14-| More than ~7 classes that all carry meaning | A **table** (or table + chart) | More colors |
15-
16-If a chart *is* right, pick the type by the job:
17-
18-## The job -> the type
19-
20-| Job (what the reader must do) | Default form | Color job |
21-|---|---|---|
22-| Compare magnitude, low -> high | bar / column; **heatmap** for a grid | sequential (one hue) |
23-| Trend over time | line; area for a single series | sequential or 1 categorical |
24-| Tell distinct series apart | grouped/stacked bar, multi-line | **categorical** |
25-| One series is the point, rest are context | **emphasis** (highlight one, gray the rest) | 1 hue + gray |
16:| **Status** | state (good->critical) | a small fixed scale, reserved meaning, always icon+label |
17-
18-**Categorical or ordinal?** If swapping the category order would change the
19-meaning - funnel stages, size tiers (S/M/L), age bands, cohort buckets - it is
20-**ordinal** and takes a one-hue ramp so the reader sees the order in the color.
21-If swapping would not - product names, teams, regions, endpoints - it is
22-
… [1673 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
71:- **Stat tile** contract: `label` (sentence case, no trailing colon) · `value` (Sans
72-  semibold, auto-compact: 1,284 / 12.9K / $4.2M) · `delta` (optional; signed,
73-  vs a named period; color = direction × whether up is good) · `trend` (optional;
74-  12-point sparkline in the de-emphasis hue, current period in the accent).
75:- **Meter:** the fill carries severity (accent -> warning -> danger); the unfilled
76-  track is a **lighter step of the same ramp** (blue-on-blue, etc.) so state reads
77-  across the whole bar.
78-- **Hero figure.** The single number a dashboard leads with, >=48px, in the same
79-  sans as everything else (never a display or serif face - it reads as off-brand
80-  decoration). Exactly one per view.
81-- **Proportional figures for big numbers; tabular only in columns.** A large
82-  standalone value (hero figure, stat-tile value) uses the font's default
83-  proportional figures - `tabular-nums` gives every digit the width of a `0`, so a
84-  number like `121` looks loose at display sizes. Reserve
85-  `font-variant-numeric: tabular-nums` for columns of numbers that must align
86-  vertically (table rows, axis ticks).
87-
88-## Texture - the backup channel (opt-in)
89-
7:## Color & encoding
48:## Form
63:## Marks & chrome
103:## Interaction & accessibility
```
  </details>


  <details><summary>result</summary>

```
11:| Function | When to Use | Duration Range | Priority |
12-|----------|------------|----------------|----------|
13-| **Feedback** | Confirming a user action | 100-200ms | Highest — directly responds to input |
14-| **Orientation** | Showing spatial relationships, navigation | 200-400ms | High — helps users understand where they are |
15-| **Focus** | Directing attention to changes | 150-300ms | Medium — guides the eye to what matters |
16-| **Delight** | Brand personality, celebration | 300-600ms | Lowest — earn it sparingly |
17-
--
42:- **UI rule:** Animate one thing at a time. If multiple elements enter, stagger them (50-100ms delay between each). The most important element animates first.
43-
44-### 6. Arcs
45-Natural movement follows curved paths, not straight lines.
46-- **UI rule:** Elements that move across the screen should follow a slight curve, especially for longer distances. Short movements (button press, toggle) can be linear.
47-
48-### 7. Secondary Action
--
76:### Duration by Interaction Type
77-
78:| Interaction | Duration | Easing | Notes |
79-|------------|----------|--------|-------|
80-| Button press feedback | 50-100ms | ease-out | Fastest. Color change, scale |
81-| Toggle switch | 150-200ms | ease-in-out | State swap animation |
82-| Tooltip appear | 100-150ms | ease-out | Quick in, don't delay information |
83-| Tooltip disappear | 75-100ms | ease-in | Faster exit than enter |
84-| Dropdown open | 150-200ms | ease-out | Reveals content |
--
104:| 
… [1362 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find page routing table in skill

  <details><summary>result</summary>

```
405:const PAGES: [RegExp, string, string][] = [
406-  [/\bagents?|runs?|monitor\w*\b/, '/agents', 'agents'], [/\bsaved searches|searches\b/, '/searches', 'saved searches'], [/\bpools?\b/, '/pools', 'talent pools'], [/\bcampaigns?\b/, '/campaigns', 'campaigns'],
407-  [/\bsubmittals?\b/, '/submittals', 'submittals'], [/\b(documents?|docs|files|briefs?)\b/, '/docs', 'documents'], [/\breports?\b/, '/reports', 'client reports'], [/\bnotes?|mentions?\b/, '/notes', 'notes'], [/\bclients?\b/, '/clients', 'clients'], [/\bmandates?|roles\b/, '/clients', 'clients and mandates'],
408-];
409-registerSkill({
410-  id: 'agency.open', side: 'recruiter',
411-  match: (c) => {
412-    if (!on(c)) return 0;
413-    const verb = /\b(open|show|take me|go to|bring up|switch|view|see|back to|focus|look at)\b/.test(c.norm);
414:    if (verb && PAGES.some(([re]) => re.test(c.norm))) return 0.86;
415-    if (verb && clientsIn(c.norm).length === 1) return 0.84;
416-    return 0;
417-  },
418-  handle: (c) => {
419-    const client = clientsIn(c.norm)[0];
420:    const page = PAGES.find(([re]) => re.test(c.norm));
421-    const to = page ? `${PAGE}${page[1]}` : `${PAGE}/client/${client}`;
422-    const label = page ? page[2] : clientName(c.w, client!);
423-    return { msgs: [{ kind: 'reply', text: `${page ? `Opening ${label}` : `Switched to ${clientName(c.w, client!)}`}${client ? `, showing ${clientName(c.w, client)} only` : ''}.${client ? ' Other clients’ records stay out of this view.' : ''}` }],
42
… [1157 more characters trimmed]
```
  </details>


**Claude** · 2026-10-29 12:27

Now let me make the model changes (privacy filtering, run phases, canonical paths).

- 🔧 `Bash`: Apply privacy, run-phase and path changes to the model

  <details><summary>result</summary>

```
journeys/agency/model.ts:30:export const AP = {
journeys/agency/model.ts:63:export const mandateHidden = (w: World, mandateId: string) => w.pipeline.filter((p) => p.mandateId === mandateId && !allowed(w, p.personId) && !isWithdrawn(w, p.personId)).length;
journeys/agency/model.ts:184:  c.notShown = pool.members.filter((p) => !isWithdrawn(w, p) && !allowed(w, p)).length;
journeys/agency/model.ts:219:  r.state = 'PAUSED'; r.pausedReason = reason; r.resumedFrom = undefined; r.log.push({ at: new Date().toISOString(), text: `Paused by ${actor.first} at ${r.done} of ${r.total}. ${reason}`, k: 'decision' });
journeys/agency/model.ts:224:  r.state = 'QUEUED'; r.pausedReason = undefined; r.resumedFrom = r.done; r.log.push({ at: new Date().toISOString(), text: `Resumed by ${actor.first} from ${r.done} of ${r.total}; no finished work is repeated`, k: 'decision' });
journeys/agency/model.ts:408:    update((w) => { for (const r of ag(w).runs) if (r.state === 'RUNNING') { r.state = 'PAUSED'; r.resumedFrom = undefined; r.pausedReason = 'Interrupted when the page closed. Every finished unit was kept; resume continues from here.'; r.log.push({ at: at(), text: `Interrupted at ${r.done} of ${r.total} when the page closed`, k: 'issue' }); } });
journeys/agency/model.ts:420:export const phaseOf = (r: AgentRun): RunPhase => r.state === 'RUNNING' ? 'running' : r.state === 'QUEUED' ? 'waiting' : r.state === 'RETRYING' ? 'retrying' : r.state === 'FAILED' ? 'failed'
state/areas/agency.ts:24:  notShown
… [78 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Update skill and proactive nav paths and privacy filters

  <details><summary>result</summary>

```
1
q/skills/agency.ts:27:const setUi = (w: World, a: Actor, key: string, v: unknown) => { (w.q.ui[`${a.id}|${PAGE}`] ??= {})[key] = v; };
q/skills/agency.ts:21:const PAGE = '/r/agency';
q/skills/agency.ts:406:const PAGES: [RegExp, string, string][] = [
q/proactive/agency.ts:9:const P = '/r/agency';
```
  </details>

- 🔧 `Bash`: Check view state keying

  <details><summary>result</summary>

```
375:      effects: (w, a) => { setFocus(w, a.id, client); setUi(w, a, 'compare.pool', pool.id); }, nav: { to: AP.compare, label: 'the comparison' } };
194:export function useViewState<T>(key: string, initial: T): [T, (v: T) => void] {
195-  const k = `${useWorld((w) => w.session.actor)}|${route().split('/').slice(0, 3).join('/')}`;
196-  const v = useWorld((w) => (w.q.ui[k]?.[key] as T | undefined));
197-  const set = useCallback((nv: T) => update((w) => { (w.q.ui[k] ??= {})[key] = nv as unknown; }), [k, key]);
198-  return [v === undefined ? initial : v, set];
199-}
200-
201-/** Q says something without a user turn (proactive follow-ups, results of background work). */
202-export function qSays(text: string, extra: Partial<Omit<QMsg, 'id' | 'at' | 'who' | 'text'>> = {}) {
[This command modified 1 file you've previously read: q/proactive/agency.ts. Call Read before editing.]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/routes/agency.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/routes/agency.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>


**Claude** · 2026-10-29 12:28

Now the main rewrite of the pages file.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/agency/pages.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/agency/pages.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>


**Claude** · 2026-10-29 12:31

You've hit your 5-hour limit · resets 1:50pm (UTC)


**User** · 2026-10-29 13:51

The coordinator sent a message while you were working:
From the lead: the usage limit has reset. Please pick up the design pass where you stopped; you were rewriting the pages file. Your brief and my follow-up messages still apply.

Address this before completing your current task.


**Claude** · 2026-10-29 13:51

The pages file is written. Now the stylesheet.

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/styles/agency.css

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/styles/agency.css has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Type-check agency files

  <details><summary>result</summary>

```
done
```
  </details>

- 🔧 `Bash`: Scope paragraph rule and recapture agency pages

  <details><summary>result</summary>

```
8:.ds-canvas:has(> .agency-demo) p.t14, .ds-canvas:has(.agency-demo) p.t14 { margin: 0; }
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1
[This command modified 1 file you've previously read: ../../../prototype/src/styles/agency.css. Call Read before editing.]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/desktop/u_dele_r_agency_agents.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/desktop/u_dele_r_home.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/desktop/u_dele_r_agency_pools.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Tighten home facts, run gutter and pool row columns
- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/a1/phone/u_dele_r_agency_agents.png

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


**User** · 2026-10-29 13:55

[Image: original 780x3776, displayed at 413x2000. Multiply coordinates by 1.89 to map to original image.]

- 🔧 `Bash`: Get hidden people names and rename options button

  <details><summary>result</summary>

```
17:  { id: 'p_amaka', name: 'Amaka Eze', first: 'Amaka', initials: 'AE', side: 'candidate', title: 'Economics graduate', timezone: 'Africa/Lagos', personId: 'p_amaka', journey: 'T1', email: 'amaka@mail.example', signedUp: false },
18:  { id: 'p_chidi', name: 'Chidi Nwosu', first: 'Chidi', initials: 'CN', side: 'candidate', title: 'Sales executive', timezone: 'Africa/Lagos', personId: 'p_chidi', journey: 'T2', email: 'chidi@mail.example', signedUp: true },
21:  { id: 'p_zara', name: 'Zara Mensah', first: 'Zara', initials: 'ZM', side: 'candidate', title: 'Backend engineer', timezone: 'Africa/Accra', personId: 'p_zara', journey: 'T5', email: 'zara@mail.example', signedUp: true },
1
```
  </details>


**Claude** · 2026-10-29 13:55

Now updating R4.mjs for the new paths and the privacy behaviour.

- 🔧 `Bash`: Update R4.mjs paths and add privacy and IA assertions

  <details><summary>result</summary>

```
22:const P = { pools: '/r/agency/pools', searches: '/r/agency/pools/searches', compare: '/r/agency/pools/compare', notes: '/r/agency/clients/notes', docs: '/r/agency/clients/docs', clients: '/r/agency/clients', submittals: '/r/agency/submittals', campaigns: '/r/agency/campaigns', agents: '/r/agency/agents', mandate: (id) => `/r/agency/clients/mandate/${id}` };
```
  </details>

- 🔧 `Bash`: Run updated R4 on desktop

  <details><summary>result</summary>

```
ERRORS (2):
d: SyntaxError: The requested module '/src/journeys/hire-a/Audit.tsx?t=1793282198683' does not provide an export named 'Audit'
d: [hmr] Failed to reload /src/app/App.tsx. This could be due to syntax errors or importing non-existent modules. (see errors above)
R4: PASS
```
  </details>

- 🔧 `Bash`: Run updated R4 on phone

  <details><summary>result</summary>

```
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: TypeError: Cannot read properties of null (reading 'session')
    at eval (eval at evaluate (:311:30), <anonymous>:1:71)
    at UtilityScript.evaluate (<anonymous>:313:16)
    at UtilityScript.<anonymous> (<anonymous>:1:44)
    at setActor (/home/user/neo/talent-q-design/qa/scripts/journeys/R4.mjs:57:47)
    at /home/user/neo/talent-q-design/qa/scripts/journeys/R4.mjs:61:9 {
  log: []
}

Node.js v22.22.0
0
```
  </details>

- 🔧 `Bash`: Retry R4 on phone

  <details><summary>result</summary>

```
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: TypeError: Cannot read properties of null (reading 'session')
    at eval (eval at evaluate (:311:30), <anonymous>:1:71)
    at UtilityScript.evaluate (<anonymous>:313:16)
    at UtilityScript.<anonymous> (<anonymous>:1:44)
    at setActor (/home/user/neo/talent-q-design/qa/scripts/journeys/R4.mjs:57:47)
    at /home/user/neo/talent-q-design/qa/scripts/journeys/R4.mjs:61:9 {
  log: []
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Probe app load errors

  <details><summary>result</summary>

```
ERR The requested module '/src/journeys/hire-a/Audit.tsx?t=1793282198683' does not provide an export named 'Audit'
false
src/journeys/hire-c/Calendar.tsx(73,95): error TS2339: Property 'id' does not exist on type 'Person'.
src/journeys/hire-c/WeekOverlap.tsx(24,19): error TS6133: 'w' is declared but its value is never read.
src/journeys/hire-c/WeekOverlap.tsx(54,9): error TS7034: Variable 'ticks' implicitly has type 'any[]' in some locations where its type cannot be determined.
src/journeys/hire-c/WeekOverlap.tsx(77,64): error TS7005: Variable 'ticks' implicitly has an 'any[]' type.
src/q/skills/hire-b.ts(115,11): error TS6133: 'lines' is declared but its value is never read.
```
  </details>

- 🔧 `Bash`: Check the hire-a Audit export

  <details><summary>result</summary>

```
23:export function Audit() {
12:import { Audit } from '../journeys/hire-a/Audit';
```
  </details>

- 🔧 `Bash`: Restart my dev server and probe again

  <details><summary>result</summary>

```
Exit code 144
```
  </details>

- 🔧 `Bash`: Start dev server on 5184 and probe

  <details><summary>result</summary>

```
➜  Local:   http://localhost:5184/
  ➜  Network: use --host to expose
true
```
  </details>

- 🔧 `Bash`: Run full R4 on desktop and phone

  <details><summary>result</summary>

```
No page errors.
R4: PASS
0
```
  </details>

- 🔧 `Bash`: Run privacy checks

  <details><summary>result</summary>

```
All privacy checks passed
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R4/d-04-agents-interrupted.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R4/d-02-agents-failed.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Fix failed banner icon and disclosure; capture after screens

  <details><summary>result</summary>

```
captured 102 pages to captures/review/after
u_dele_r_agency_agents.png
u_dele_r_agency_campaigns.png
u_dele_r_agency_client_org_kora.png
u_dele_r_agency_clients.png
u_dele_r_agency_compare.png
u_dele_r_agency_docs.png
u_dele_r_agency_mandate_m_ops.png
u_dele_r_agency_notes.png
u_dele_r_agency_pools.png
u_dele_r_agency_reports.png
u_dele_r_agency_searches.png
u_dele_r_agency_submittals.png
u_dele_r_home.png
```
  </details>

- 🔧 `Bash`: Check whether other areas' captures were overwritten

  <details><summary>result</summary>

```
captures/review/after/desktop/talent-b_state_summary.png
captures/review/after/desktop/talent-b_state_passport-conf.png
captures/review/after/desktop/talent-b_state_memory-zara.png
captures/review/after/desktop/talent-b_state_passport-zara.png
captures/review/after/desktop/talent-b_state_passport.png
captures/review/after/desktop/talent-b_state_passport-code.png
captures/review/after/desktop/talent-b_state_discovery.png
captures/review/after/desktop/talent-b_state_prep.png
captures/review/after/desktop/talent-b_state_jobs.png
captures/review/after/desktop/talent-b_state_memory.png
5:const [BASE = 'http://localhost:4174/', OUT = 'review', ONLY = ''] = process.argv.slice(2);
25:      if (ONLY && !ONLY.split(',').some((o) => `${actor}${r}`.includes(o))) continue;
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/phone/u_dele_r_agency_pools.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:06

[Image: original 780x3812, displayed at 409x2000. Multiply coordinates by 1.91 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/after/desktop/u_dele_r_agency_campaigns.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Assemble before/after pairs

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
d-01-home.png d-02-agents-failed.png d-03-q-explains-outage.png d-04-agents-interrupted.png d-05-agents-recovered.png d-06-search-diff.png d-07-isolation-refusal.png d-08-submittal-draft.png d-09-submittal-withdrawn.png d-10-pool-removed.png d-10b-pool-hidden-medlink.png d-11-submittal-sent.png d-12-campaign.png d-12b-docs-uploaded.png d-13-agents-resumed.png d-14-conflict.png d-15-notes.png d-16-report-flagged.png d-17-report-shared.png d-18-tunde-denied.png d-19-tunde-granted.png d-20-r-agency-clients-docs.png d-20-r-agency-clients.png d-20-r-agency-compare.png d-20-r-agency-docs.png d-20-r-agency-pools-compare.png d-20-r-agency-pools-searches.png d-20-r-agency-pools.png d-20-r-agency-submittals.png d-21-home-end.png m-01-home.png m-02-agents-failed.png m-03-q-explains-outage.png m-04-agents-interrupted.png m-05-agents-recovered.png m-06-search-diff.png m-07-isolation-refusal.png m-08-submittal-draft.png m-09-submittal-withdrawn.png m-10-pool-removed.png m-10b-pool-hidden-medlink.png m-11-submittal-sent.png m-12-campaign.png m-12b-docs-uploaded.png m-13-agents-resumed.png m-14-conflict.png m-15-notes.png m-16-report-flagged.png m-17-report-shared.png m-18-tunde-denied.png m-19-tunde-granted.png m-20-r-agency-clients-docs.png m-20-r-agency-clients.png m-20-r-agency-compare.png m-20-r-agency-docs.png m-20-r-agency-pools-compare.png m-20-r-agen
… [92 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Remove stale captures and copy key states into after
- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/R4/d-13-agents-resumed.png

  <details><summary>result</summary>

```
19
```
  </details>


  <details><summary>result</summary>

```
[image]
```
  </details>


**Claude** · 2026-10-29 14:06

Now the design notes and the engineering handoff.

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/agency.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/agency.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Collect skills, ops and events for the handoff

  <details><summary>result</summary>

```
95 journeys/design/agency.md
id: 'agency.isolation' id: 'agency.interrupt' id: 'agency.resume' id: 'agency.priority' id: 'agency.cancel' id: 'agency.retry' id: 'agency.rerun' id: 'agency.submit' id: 'agency.campaign' id: 'agency.note' id: 'agency.report' id: 'agency.conflict' id: 'agency.access' id: 'agency.consent' id: 'agency.upload' id: 'agency.compare' id: 'agency.list' id: 'agency.status' id: 'agency.open' 
'agency.focus' 'agency.run.pause' 'agency.run.resume' 'agency.runs.resume' 'agency.run.cancel' 'agency.run.retry' 'agency.run.skip' 'agency.run.priority' 'agency.submittal.sendLatest' 'agency.submittal.send' 'agency.submittal.discard' 'agency.submittal.toggle' 'agency.submittal.nudge' 'agency.submittal.reply' 'agency.campaign.launch' 'agency.pool.add' 'agency.search.rerun' 'agency.note.delete' 'agency.note.read' 'agency.consent.withdraw' 'agency.access.request' 'agency.access.decide' 'agency.report.save' 'agency.report.share' 'agency.report.draft' 'agency.doc.upload' 'agency.actor' 
'agency.access.decided', SCOPE 'agency.access.denied', SCOPE 'agency.access.requested', SCOPE 'agency.campaign.approved', SCOPE 'agency.consent.withdrawn', SCOPE 'agency.doc.uploaded', SCOPE 'agency.isolation.declined', SCOPE 'agency.note.added', SCOPE 'agency.report.shared', SCOPE 'agency.role.declined', SCOPE 'agency.run.cancelled', SCOPE 'agency.run.paused', SCOPE 'agency.run.resumed', SCOPE 'agency.search.rerun', SCOPE 'agency.submittal.drafted', SCOPE 'agency.submittal.nudged', SCOPE 
… [86 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Condense design notes under 80 lines

  <details><summary>result</summary>

```
76 agency.md
```
  </details>

- 🔧 `Bash`: Read an existing handoff for format

  <details><summary>result</summary>

```
163 talent-a.md
  138 talent-b.md
  115 talent-c.md
  416 total
# Engineering handoff · talent-a (T1 Amaka, T2 Chidi)

Specification only. The prototype is the behavioural and design blueprint, not the implementation. Every
"Prototype:" reference is to `prototype/src/`. Lines marked **PROD ≠ SIM** say where production must differ
from the simulation. Journey proof: `qa/scripts/journeys/T1.mjs`, `T2.mjs`.

## 0. Defaults that every feature below inherits

- **Scope.** All talent-a data is `PERSON:<personId>` scoped and private by default. Nothing in this area ever
  widens visibility on its own. The only paths to an employer are (a) `apply` (shares the person's profile
  claims with that one org) and (b) `share` (one evidence item with one org). Both need an explicit approval.
  Visibility is decided only by the central policy (`mock/world.ts`: `canSeeCandidate`, `canDiscover`,
  `visibleEvidence`); services never re-implement it. Employers can never see J7 plans, practice, assessments
  that weren't shared, readiness or plan adherence.
- **Claims vs evidence.** Three tiers, never merged: *claim* (the person's words, any source), *practice*
  (private, never proof) and *evidence* (reviewed work sample or verified credential). Only evidence changes a
  competency to shown; only shown competencies change distance-to-role. This is a backend invariant, enforced
  in the write path, not a UI convention.
- **Events.** Every state change emits an append-only domain event `{type, acto
… [1943 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/agency.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/agency.md (file state is current in your context — no need to Read it back)
```
  </details>


**Claude** · 2026-10-29 14:08

Final type-check and R4 run after the last edits.

- 🔧 `Bash`: Final typecheck, R4 and privacy runs

  <details><summary>result</summary>

```
No page errors.
R4: PASS
All privacy checks passed
```
  </details>

- 🔧 `SubagentHandback`: {"message": "The agency design pass is finished: R4.mjs passes on desktop and phone with no page errors, and privacy.mjs passes against port 5184. Type-checking is clean for the agency files. I made n

  <details><summary>result</summary>

```
{"success":true,"message":"Report delivered to your caller."}
```
  </details>
