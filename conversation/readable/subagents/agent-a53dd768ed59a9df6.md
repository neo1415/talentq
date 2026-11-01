# Helper agent agent-a53dd768ed59a9df6: Design pass T4 pages

Source: `agent-a53dd768ed59a9df6.jsonl`. Tool results are trimmed to 1,500 characters and images are left out; the raw transcript has everything.


**User** · 2026-10-29 12:20

Run the design pass for area `talent-c` (journey T4: Grace, a low-confidence care worker on a low-bandwidth phone) in /home/user/neo/talent-q-design/prototype.

Before anything else:
1. Read /home/user/neo/talent-q-design/journeys/DESIGN-PASS-BRIEF.md and follow it exactly. That includes loading the named skills with the Skill tool and applying them.
2. Read /home/user/neo/talent-q-design/journeys/BUILD-BRIEF.md for the contracts and your file ownership (the same `talent-c` files as before).

Use dev server port 5187.

Your pages and states, phone-first at 390×844:
- `/c/start`: first steps by voice, typing or form.
- The resumable certificate upload: progress, failure, offline pause, resume, and "welcome back".
- `/c/interview`, the interview room, in both practice and real mode:
  - the question card, simpler wording and "say it again";
  - voice and its fallbacks;
  - pause;
  - lost connection mid-interview;
  - the adaptive follow-up for technical and practice questions, recently restored, with "Skip this follow-up";
  - the review of exactly what the employer will see;
  - the approval and the simulated receipt.
- Lite mode.
- Every Q reply card your skills produce.

The interview interface is a founder priority. Make it calm, clear, legible and touch-friendly. Motion must be meaningful but never delay anything, and lite mode must stay lighter.

T4.mjs and qa/scripts/review/interview-followup.mjs must keep passing.

- 🔧 `Bash`: Read design pass brief and size of build brief

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

- 🔧 `Bash`: Read build brief and list journeys dir

  <details><summary>result</summary>

```
Exit code 2
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
  scripted replies as general AI. If Q cannot handle something, it says so (the engine's fallback does this)
… [5861 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find talent-c files and status

  <details><summary>result</summary>

```
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
 M ../captures/cx/R2/m-03-corrected-equal.png
 M ../captures/cx/R2/m-04-profile-tobi.png
 M ../captures/cx/R2/m-05-profile-viewer-outage.png
 M ../captures/cx/R2/m-06-profile-viewer-site.png
 M ../captures/cx/R2/m-07-after-invitation.png
 M ../captures/cx/R2/m-08-compare-last-year.png
 M src/ds/AppShel
… [897 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read T4 journey, list files and captures

  <details><summary>result</summary>

```
- [info] His best work is confidential. Q suggests a redacted summary plus a reference attestation.
- [info] The certification issuer is unreachable. Shown as "verification pending", not as failed.
- [info] Revokes Kora's access to a portfolio item. Ada's view updates live and Q tells Ada only that access ended.
- [mind] Challenges Q's analysis. Q shows the basis and corrects it.
- [recover] Different visibility for Kora and the agency, with a per-viewer preview.

### T4: The low-confidence, low-bandwidth user (Grace)

**Flow**: phone-first, with simple language, voice/text/form alternatives, large targets, Lite mode ＋, resumable upload ＋, interrupted session ＋, interview with reconnect ✓.

**Curveballs**
- [info] Doesn't understand "evidence". Q rephrases ("proof of what you did").
- [recover] Voice is unavailable. Text and form alternatives.
- [recover] An upload fails at 60%. Resume from 60%.
- [recover] Accidentally leaves the app. She returns where she was.
- [recover] Connection drops in the interview. Answers are kept and she reconnects.

### T5: The sceptical job seeker (Zara)

**Flow**: job discovery ＋ with employer verification signals ＋ → job detail ＋ → mutual fit ＋ → application ＋ → tracking ＋ → interview prep ✓ → status visibility ＋ → correspondence ＋ → evidence explanation ✓ → consent ＋ → memory review ✓ → deletion ＋.

**Curveballs**
- [info] A saved job closes. Q proactively says so and offers similar jobs.
- [info] The recruiter doesn't respond. Q shows the ho
… [2118 more characters trimmed]
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

- 🔧 `Skill`: {"skill": "dataviz"}
- 🔧 `Skill`: {"skill": "design-superpowers:creative"}

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

- 🔧 `Bash`: Read talent-c route, shared, first steps, css

  <details><summary>result</summary>

```
<persisted-output>
Output too large (32.2KB). Full output saved to: /root/.claude/projects/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tool-results/bj4farigj.txt

Preview (first 2KB):
// Routes for T4 (Grace). Owned by this area (see journeys/BUILD-BRIEF.md).
import { registerRoute } from './registry';
import { registerHomeSection } from './entry';
import { Link } from '../ui/router';
import { actorOf, useWorld, type World } from '../mock/world';
import { readPersonC } from '../state/areas/talent-c';
import { Interview } from '../screens/Interview';
import { FirstSteps } from '../journeys/talent-c/FirstSteps';
import { uploadPct } from '../journeys/talent-c/runtime';
import '../styles/talent-c.css';

registerRoute({ path: '/c/interview', side: 'candidate', label: 'practice and interviews', render: () => <Interview />, nav: { group: 'Interviews', label: 'Interview room', icon: 'practice', order: 42 } });
// Reached from home, Q ("help me start") and proactive suggestions; kept out of the rail (nine-item limit).
registerRoute({ path: '/c/start', side: 'candidate', label: 'your first steps', render: () => <FirstSteps /> });

const mine = (w: World) => { const a = actorOf(w); return a.side === 'candidate' && !!a.personId && (!!w.q.prefs[a.id]?.plain || !!readPersonC(w, a.personId).place); };
registerHomeSection('candidate', { id: 'talent-c.first-steps', order: 5, when: mine, render: () => <FirstStepsCard /> });

function FirstStepsCard() {
  const s = useWorld((w) => { co
… [714 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rest of the output

  <details><summary>result</summary>

```
// Shared pieces for T4 pages: the person's slice, lite mode, "where you were", voice with honest fallback,
// the answer-mode switch (type, speak, form) and the demo controls a reviewer uses on a phone.
import { useEffect, useRef, useState, type ReactNode } from 'react';
import { MotionConfig } from 'motion/react';
import { actorOf, update, useWorld } from '../../mock/world';
import { personC, readPersonC, type AnswerMode, type PersonState, type VoiceState } from '../../state/areas/talent-c';
import { SID, welcomeBack } from './runtime';

export function useMe() {
  const actor = useWorld((w) => actorOf(w));
  const pid = actor.personId ?? actor.id;
  const me = useWorld((w) => readPersonC(w, pid));
  const plain = useWorld((w) => !!w.q.prefs[actor.id]?.plain);
  const lite = useWorld((w) => !!(actor.personId && w.consents[actor.personId]?.lite));
  const offline = useWorld((w) => w.network === 'offline');
  return { actor, pid, me, plain, lite, offline };
}
export const patchMe = (pid: string, fn: (p: PersonState) => void) => update((w) => fn(personC(w, pid)));

/** Lite mode: no motion at all, bigger targets, no decorative images (CSS keys off data-lite on the shell). */
export function LiteWrap({ lite, children }: { lite: boolean; children: ReactNode }) {
  return <MotionConfig reducedMotion={lite ? 'always' : 'user'}><div className="talent-c-page" data-lite={lite ? 'on' : undefined}>{children}</div></MotionConfig>;
}

/** Pages that are mounted right now. Leaving is deci
… [26713 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read InterviewRoom and check Interview screen

  <details><summary>result</summary>

```
/* Home card */
.talent-c-home { display: grid; gap: 10px; justify-items: start; padding: 16px; border-radius: 16px; background: var(--paper); border: 1px solid var(--rule-2); margin-top: 4px; }

/* Demo controls (phones have no rail, so "Simulate offline" lives here too) */
.talent-c-demo { border-top: 1px dashed var(--rule-2); padding-top: 12px; font-size: 14px; color: var(--ink-3); }
.talent-c-demo summary { cursor: pointer; min-height: 44px; display: flex; gap: 10px; align-items: center; }
.talent-c-demo-row { display: flex; flex-wrap: wrap; gap: 8px; padding-top: 8px; }
.talent-c-demo-row .ds-btn { font-size: 14px; min-height: 44px; }
.talent-c-demo-row .ds-btn[aria-pressed='true'] { background: var(--wash); border-style: dashed; }

@media (max-width: 480px) {
  .talent-c-steps button { min-height: 72px; padding: 10px; font-size: 13px; }
  .talent-c-actions .ds-btn { flex: 1 1 100%; }
  .talent-c-actions .ds-btn.quiet { flex: 0 1 auto; }
  .talent-c-mic { justify-self: stretch; justify-content: center; }
}

/* Lite mode: fewer pictures, no motion, bigger targets and text. */
.ds-app[data-lite='on'] .talent-c-pic { display: none; }
.ds-app[data-lite='on'] .talent-c-page *, .talent-c-page[data-lite='on'] * { transition: none !important; animation: none !important; }
.ds-app[data-lite='on'] .talent-c-page .ds-btn, .talent-c-page[data-lite='on'] .ds-btn,
.talent-c-page[data-lite='on'] .talent-c-modes button, .talent-c-page[data-lite='on'] .talent-c-steps button { min-height:
… [16216 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read CSS middle, interview logic, questions, area state

  <details><summary>result</summary>

```
.talent-c-progress .bar i[data-on] { background: var(--ink); border-color: var(--ink); }
.talent-c-progress[data-s='FAILED'] .bar i:not([data-on]):first-of-type, .talent-c-progress[data-s='FAILED'] .bar i[data-on] + i:not([data-on]) { border-color: var(--risk); border-style: dashed; }
.talent-c-progress[data-s='PAUSED'] .bar i[data-on] + i:not([data-on]) { border-style: dashed; }

/* Interview */
.talent-c-question { border-left: 4px solid var(--gold); }
.talent-c-qtext { font-size: clamp(22px, 5.4vw, 28px); line-height: 1.3; margin: 0; font-weight: 400; }
.talent-c-who { margin: 0; padding: 12px 16px; border-radius: 14px; border: 1px dashed var(--rule-2); background: var(--sheet); font-size: 15px; }
.talent-c-who[data-k='real'] { border-style: solid; border-color: var(--ink); }
.talent-c-who summary { cursor: pointer; min-height: 32px; display: flex; align-items: center; }
.talent-c-who ul { margin: 8px 0; padding-left: 20px; display: grid; gap: 4px; }
.talent-c-list { margin: 0; padding-left: 20px; display: grid; gap: 6px; font-size: 16px; }
.talent-c-review { margin: 0; padding-left: 20px; display: grid; gap: 14px; }
.talent-c-review li { display: grid; gap: 4px; }
.talent-c-confirm { display: grid; gap: 10px; padding: 14px; border: 2px solid var(--ink); border-radius: 14px; width: 100%; }
.talent-c-confirm .ds-btn { justify-self: start; }

===
// Interview room logic shared by the page and Q's skills (so everything can be done by talking to Q).
import { emit, getWorld, no
… [16115 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read runtime, proactive rules, seed
- 🔧 `Bash`: Read Q skills for talent-c

  <details><summary>result</summary>

```
// Q skills for T4 (Grace): plain explanations (including care-sector words), first steps, the resumable
// certificate upload, voice/text/form switching with an honest voice fallback, lite mode, "where was I",
// and the interview room (repeat, simpler words, pause, what the employer sees, send with approval).
// Everything here works by typing or speaking to the global Q, from any page, in imperfect language.
import { emit } from '../../mock/world';
import type { Actor, QAction } from '../../state/domain';
import { pushUndo, registerOp, registerSkill } from '../core/engine';
import { GLOSSARY, findTerm } from '../core/glossary';
import type { QCtx, QReply } from '../core/types';
import { personC, readPersonC, roomC } from '../../state/areas/talent-c';
import { kick, partsLine, resumeIn, uploadPct, whereLine, STEP_LABEL } from '../../journeys/talent-c/runtime';
import { bankOfRoom, current, qText, startRoom, submitReal } from '../../journeys/talent-c/interview';
import { bankFor, timeText, whenText } from '../../journeys/talent-c/questions';

const pidOf = (a: Actor) => a.personId ?? a.id;
const scope = (a: Actor) => `PERSON:${pidOf(a)}`;
const plainFor = (c: QCtx) => !!c.w.q.prefs[c.actor.id]?.plain;
const onInterview = (c: QCtx) => c.route.startsWith('/c/interview');

// ---------------- Plain words (one or two sentences), including care-sector terms ----------------
const PLAIN: Record<string, { plain: string; simpler: string }> = {
  evidence: { plain: 'Evidence means pr
… [26170 more characters trimmed]
```
  </details>


  <details><summary>result</summary>

```
// T4 runtime: the resumable certificate upload, network watching and "where you were" for returning people.
// The upload sends a file in parts; progress counts parts the (simulated) server acknowledged, never a timer.
// It survives the connection dropping (pauses, then carries on from the last safe part when back online),
// navigation (it keeps going in the background) and the page closing (paused; carries on from the last
// safe part when she says so). Everything is kept in the area slice, so it survives reloads.
import { emit, getWorld, now, uid, update, type World } from '../../mock/world';
import { appendQ } from '../../q/core/engine';
import { personC, readPersonC, type PersonState, type TalentCState, type UploadState } from '../../state/areas/talent-c';

export const CHUNK_KB = 240;
/** This page load. A saved place with a different id means she closed or reloaded the app since. */
export const SID = uid('sid');
const files = new Map<string, File>();
let timer: number | undefined;

const peopleOf = (w: World) => (w.areas['talent-c'] as TalentCState | undefined)?.people ?? {};
const actorIdFor = (w: World, personId: string) => w.actors.find((a) => a.personId === personId)?.id ?? personId;
const pct = (u: UploadState) => Math.round((u.done / u.chunks) * 100);
export const partsLine = (u: UploadState) => `${u.done} of ${u.chunks} parts (${pct(u)}%)`;
export { pct as uploadPct };

function qNote(w: World, personId: string, text: string, actions?: Parameters<typeof appe
… [17256 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read tests and motion tokens

  <details><summary>result</summary>

```
// Regression for SC-099: the interview room asks one adaptive follow-up when an answer lacks the detail
// the question needs, keeps both answers together, can be skipped, and doesn't ask when the answer is full.
import pw from '/opt/node-tools/node_modules/playwright/index.js';
const BASE = process.argv[2] || 'http://localhost:4174/';
let fails = 0; const step = (ok, n, x = '') => { if (!ok) fails++; console.log(`${ok ? 'PASS' : 'FAIL'} ${n}${x ? ` · ${x}` : ''}`); };
const b = await pw.chromium.launch(); const page = await (await b.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
await page.goto(`${BASE}#/settings`); await page.evaluate(() => localStorage.clear()); await page.reload(); await page.waitForTimeout(600);
await page.evaluate(() => { const w = JSON.parse(localStorage.getItem('tq.world.v4')); w.session.actor = 'p_tobi'; localStorage.setItem('tq.world.v4', JSON.stringify(w)); });
await page.goto(`${BASE}#/c/interview`); await page.reload(); await page.waitForTimeout(900);
await page.getByRole('button', { name: 'Start practising' }).click(); await page.waitForTimeout(600);
const q = () => page.locator('#iv-q').innerText();
const q1 = await q();
step(/reconciliation|mismatch/i.test(q1), 'backend practice starts at question 1', q1.slice(0, 60));
await page.locator('#iv-draft').fill('We compare records.'); await page.getByRole('button', { name: /Save answer/ }).click(); await page.waitForTimeout(400);
const f1 = await q();
step(/first minute/i.test(f
… [6787 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read rest of T4 journey script

  <details><summary>result</summary>

```
await page.goto(`${BASE}#/r/home`);
  await page.evaluate(() => localStorage.clear());
  await page.reload(); await sleep(900);
  if (await world(page)) break;
  console.log('… app not booting yet, retrying'); await sleep(15000);
}
errors.length = 0;
await page.evaluate(() => { const w = JSON.parse(localStorage.getItem('tq.world.v4')); w.session.actor = 'p_grace'; localStorage.setItem('tq.world.v4', JSON.stringify(w)); localStorage.setItem('tq.test.mic', 'none'); });
await page.goto(`${BASE}#/signup`); await page.reload(); await sleep(500);

// ---------- 1. Signup with plain words ----------
await page.getByRole('button', { name: 'Continue', exact: true }).click();
await page.locator('#su-code').fill('123456');
await page.getByRole('button', { name: 'Verify' }).click();
await page.getByRole('button', { name: 'Continue', exact: true }).click();
const plainPressed = await page.getByRole('button', { name: /Use plain, simple words/ }).getAttribute('aria-pressed');
await shot(page, 'phone-01-signup-plain');
await page.getByRole('button', { name: 'Start' }).click(); await sleep(500);
let w = await world(page);
step('Signup sets plain words for Grace', plainPressed === 'true' && w.q.prefs.p_grace.plain === true && w.actors.find((a) => a.id === 'p_grace').signedUp, await route(page));
await page.getByText('First steps', { exact: false }).first().waitFor({ timeout: 4000 }).catch(() => {});
step('Home offers first steps', await page.locator('.talent-c-home').isVisible());
await shot(p
… [15951 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Start dev server on port 5187

  <details><summary>result</summary>

```
Error: Port 5187 is already in use
    at Server.onError (file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:45596:18)
    at Server.emit (node:events:519:28)
    at emitErrorNT (node:net:1976:8)
    at process.processTicksAndRejections (node:internal/process/task_queues:90:21)
```
  </details>

- 🔧 `Bash`: Check existing server on 5187

  <details><summary>result</summary>

```
root      4818  0.0  0.4 1198280 76872 ?       Sl   09:01   0:00 npm exec vite --port 5187 --strictPort
root      4831  0.0  0.0   2820  1968 ?        S    09:01   0:00 sh -c vite --port 5187 --strictPort
root      4832  0.4  1.2 23471720 207912 ?     Sl   09:01   0:56 node /home/user/neo/talent-q-design/prototype/node_modules/.bin/vite --port 5187 --strictPort
root      5044  0.0  0.0   4476  3384 ?        Ss   11:52   0:00 /bin/bash -c source /root/.claude/shell-snapshots/snapshot-bash-1793261910654-oc4bgy.sh 2>/dev/null || true && \builtin export BUN_OPTIONS="--smol${BUN_OPTIONS:+ $BUN_OPTIONS}" && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'cd /home/user/neo/talent-q-design/prototype && npx vite preview --port 4174 --strictPort' < /dev/null && pwd -P >| /tmp/claude-e035-cwd
root      5045  0.0  0.4 1198808 77436 ?       Sl   11:52   0:00 npm exec vite preview --port 4174 --strictPort
root      5076  0.0  0.0   2820  1984 ?        S    11:52   0:00 sh -c vite preview --port 4174 --strictPort
root      5077  0.1  0.5 22340488 94684 ?      Sl   11:52   0:03 node /home/user/neo/talent-q-design/prototype/node_modules/.bin/vite preview --port 4174 --strictPort
root      9088  4.9  0.5 1214672 85992 ?       Sl   12:21   0:00 npm exec vite --port 5184 --strictPort
root      9102  0.0  0.0   2820  1980 ?        S    12:21   0:00 sh -c vite --port 5184 --strictPort
root      9103  5.9 
… [142 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Back up captures and run T4 baseline

  <details><summary>result</summary>

```
PASS Signup sets plain words for Grace · /c/home
PASS Home offers first steps
PASS Q: "where do i start pls" opens first steps · Let’s do it in three small steps: your work, your certificate, your interview. Y
PASS Explains "passport" in plain words · Your Evidence Passport is your private folder of proof about your work, like your certificates. You choose which employer can see each thing.
PASS Rephrases when still unclear · Put simply: Think of it as a folder on your phone for your certificates. Nobody sees it unless you say yes.
PASS Explains "evidence" as proof of what you did · Evidence means proof of what you did, like a certificate or a photo of your work.
PASS Explains a care-sector term (safeguarding) · Safeguarding means keeping the people you care for safe from harm, and speaking up if something is wrong.
PASS Q closes the explanation when she understands · Good. Ask me about any other word, any time.
PASS “dont understand” on a step explains the step simply · This step is just: tell us what work you’ve done. One line is enough, like “care assistant, 4 years”. Type it, say it, or use the small form.
PASS Switching type ↔ form keeps both answers
PASS Voice unavailable falls back to typing, words kept
PASS Q: "my mic not working" switches to typing · That’s fine. I’ve switched this step to typing, and anything you already said is kept. Short answers are fine. You can also use the simple form, with one small box per question.
PASS Q switches to the simple form on requ
… [3711 more characters trimmed]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-10-practice-q1.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-11-interview-offline.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-05-upload-failed.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Inspect Canvas component

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
… [2038 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Read capture-all script header

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
… [1319 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Find owner of /c/slots and /c/home

  <details><summary>result</summary>

```
routes/entry.tsx:111:registerRoute({ path: '/c/home', side: 'candidate', label: 'Q home', render: () => <CandidateHome />, nav: { group: 'Q', label: 'Home', icon: 'home', tab: true, order: 1 } });
routes/entry.tsx:134:    navigate(mode === 'recruiter' ? '/r/home' : '/c/home');
routes/hire-c.tsx:29:registerRoute({ path: '/c/slots', side: 'candidate', label: 'interview times', render: () => <CandidateSlots />, nav: { group: 'Interviews', label: 'Pick a time', icon: 'calendar', order: 43 } });
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/phone/p_grace_c_start.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 12:23

[Image: original 780x2158, displayed at 723x2000. Multiply coordinates by 1.08 to map to original image.]

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/before/desktop/p_grace_c_interview.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Capture current state of my pages

  <details><summary>result</summary>

```
captured 102 pages to /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now
/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/desktop:
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png
p_grace_c_home.png
p_grace_c_interview.png
p_grace_c_start.png
u_dele_r_agency_agents.png
u_dele_r_agency_campaigns.png
u_dele_r_home.png

/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/phone:
p_amaka_c_welcome.png
p_chidi_c_career.png
p_chidi_c_growth.png
p_grace_c_home.png
p_grace_c_interview.png
p_grace_c_start.png
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/now/phone/p_grace_c_interview.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Locate motion atlas

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
MO-002,Q listens,voice:recording,Voice interview,Listening text and transcript,PROTOTYPED,/gallery/states,prototype/src/ds/QMark.tsx (listening mood: core grows with input level); prototype/src/journeys/gallery/StatesGallery.tsx (Q moods),"Listening mood exists in the Q mark and is shown as a live specimen. Not yet driven by the microphone in the rebuilt /c/interview, whose mic button changes label and colour without motion. Re-pointed from /c/in
… [6204 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Inspect QMark, Glyph and DS classes

  <details><summary>result</summary>

```
ds/QMark.tsx:15:export type QMood = 'idle' | 'listening' | 'thinking' | 'working' | 'waiting' | 'blocked' | 'done' | 'offline';
ds/QMark.tsx:16:export interface QAgent { label: string; done: number; total: number; failed?: boolean }
ds/QMark.tsx:18:export const MOOD_LABEL: Record<QMood, string> = {
ds/QMark.tsx:26:export function QMark({ mood = 'idle', agents = [], size = 36, level = 0, title }: { mood?: QMood; agents?: QAgent[]; size?: number; level?: number; title?: string }) {
ds/QMark.tsx:60:export function moodOf({ agents = [], thinking, waiting, blocked, done, offline }: { agents?: QAgent[]; thinking?: boolean; waiting?: boolean; blocked?: boolean; done?: boolean; offline?: boolean }): QMood {
ds/QMark.tsx:71:export function presenceLine(mood: QMood, agents: QAgent[] = [], detail?: string) {
ds/Glyph.tsx:3:export type GlyphKind = 'verified' | 'full' | 'partial' | 'practice' | 'none' | 'unclear';
ds/Glyph.tsx:5:export const GLYPH_LABEL: Record<GlyphKind, string> = { verified: 'Verified', full: 'Evidenced', partial: 'Partial or outdated', practice: 'Practising (private)', none: 'Not shown yet', unclear: 'Unclear' };
ds/Glyph.tsx:6:export function Glyph({ k, size = 20, title }: { k: GlyphKind; size?: number; title?: string }) {
ds/Glyph.tsx:18:export function GlyphKey({ kinds }: { kinds: GlyphKind[] }) {
26:export function QMark({ mood = 'idle', agents = [], size = 36, level = 0, title }: { mood?: QMood; agents?: QAgent[]; size?: number; level?: number; title?: string }) {
… [3638 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List tokens and key DS classes

  <details><summary>result</summary>

```
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
29:  --ref-green-dark: #93c39c;
30:  --ref-green-light: #2f6b3a;
31:  --ref-amber-dark: #e6b366;
32:  --ref-amber-light: #8a5a00;
33:  --ref-red-dark: #e78d7f;
34:  --ref-red-light: #a33a2b;
35:  --ref-blue-dark: #9bb8e0;
36:  --ref-blue-light: #2f5a94;
37:  --space-0: 0;
38:  --space-1: 4px;
39:  --space-2: 8px;
40:  --space-3: 12px;
41:  --space-4: 16px;
42:  --space-5: 20px;
43:  --space-6: 24px;
44:  --space-8: 32px;
45:  --space-10: 40px;
46:  --space-12: 48px;
47:  --space-16: 64px;
48:  --space-20: 80px;
49:  --radius-sm: 8px;
50:  --radius-md: 12px;
51:  --radius-lg: 16px;
52:  --radius-xl: 22px;
53:  --radius-pill: 999px;
54:  --font-voice: 'Fraunces Variable', Georgia, serif;
55:  --font-ui: 'Inter Tight Variable', system-ui, 
… [675 more characters trimmed]
```
  </details>

- 🔧 `Bash`: List semantic tokens

  <details><summary>result</summary>

```
ds/ds.css:7:  --paper: var(--ref-paper-0); --sheet: var(--ref-paper-1); --wash: var(--ref-paper-2); --rule: var(--ref-paper-3); --rule-2: var(--ref-paper-4);
ds/ds.css:8:  --ink: var(--ref-ink-900); --ink-2: var(--ref-ink-700); --ink-3: var(--ref-ink-600);
ds/ds.css:10:  --gold: var(--ref-gold-600); --gold-ink: var(--ref-gold-800); --gold-light: var(--ref-gold-400); --gold-wash: #f1e3bf;
ds/ds.css:11:  --ok: var(--ref-green-light); --warn: var(--ref-amber-light); --risk: var(--ref-red-light);
ds/ds.css:12:  --voice: var(--font-voice); --ui: var(--font-ui); --data: var(--font-mono);
ds/ds.css:25:.ds .lab { font-family: var(--data); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-3); font-weight: 500; }
ds/ds.css:26:.ds .ink .lab { color: var(--moon-2); }
ds/ds.css:50:.ds-navgroup > .lab { padding: 4px 10px; color: var(--moon-2); }
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-c/InterviewRoom.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/talent-c/InterviewRoom.tsx has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Add Icon, update ModeSwitch and MicButton

  <details><summary>result</summary>

```
130:      <summary>Demo controls <span className="ds-sim">Simulated</span></summary>
131-      <div className="talent-c-demo-row">
132-        <button type="button" className="ds-btn" aria-pressed={offline} onClick={() => update((w) => { w.network = w.network === 'online' ? 'offline' : 'online'; })}>{offline ? 'Reconnect' : 'Simulate losing connection'}</button>
133-        <button type="button" className="ds-btn" aria-pressed={me.slow} onClick={() => patchMe(pid, (p) => { p.slow = !p.slow; })}>{me.slow ? 'Connection back to normal' : 'Simulate a slow connection'}</button>
```
  </details>

- 🔧 `Bash`: Update FirstSteps header, stepper, banner

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Edit`: /home/user/neo/talent-q-design/prototype/src/journeys/talent-c/FirstSteps.tsx

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/journeys/talent-c/FirstSteps.tsx has been updated successfully.
```
  </details>

- 🔧 `Bash`: Upload tag, done note, typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/prototype/src/styles/talent-c.css

  <details><summary>result</summary>

```
The file /home/user/neo/talent-q-design/prototype/src/styles/talent-c.css has been updated successfully. (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Add lite-aware motion helpers

  <details><summary>result</summary>

```
47:        {offline && <motion.div {...enter} className="ds-banner talent-c-banner talent-c-state" data-k="warn" role="status"><span className="talent-c-state-icon" aria-hidden="true"><Icon k="alert" /></span><span><b>No connection.</b> You can keep going; everything is saved on this phone and sent when you’re back.</span></motion.div>}
163:              {u.status === 'DONE' && <motion.p className="talent-c-flashnote" initial={still ? false : { opacity: 0, y: 4 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: DUR.normal, ease: EASE.enter }}><Glyph k="unclear" size={16} /> Private to you. Waiting for a check with whoever gave it, which is normal.</motion.p>}
62:  const enter = useArrive();
164:  const enter = useArrive(); const still = useStill();
247:  const tips = tipsFor(room); const still = useStill();
267:  const enter = useArrive(); const still = useStill();
```
  </details>

- 🔧 `Bash`: Wire hooks and typecheck

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Fix lite context usage in top-level components

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Read home card

  <details><summary>result</summary>

```
const s = useWorld((w) => { const a = actorOf(w); const p = readPersonC(w, a.personId); return { done: p.stepsDone.length, step: Math.min(p.step, 2), up: p.upload && p.upload.status !== 'DONE' && p.upload.done ? uploadPct(p.upload) : null }; });
  if (s.done >= 3) return null;
  return (
    <div className="talent-c-home">
      <span className="lab">First steps · {s.done} of 3 done</span>
      <p className="voice t19" style={{ margin: 0 }}>{s.done === 0 ? 'Three small steps: your work, your certificate, your interview.' : `Next: step ${s.step + 1} of 3.${s.up !== null ? ` Your certificate is ${s.up}% sent.` : ''}`}</p>
      <Link className="ds-btn primary" to="/c/start">{s.done ? 'Carry on' : 'Start'}</Link>
    </div>
  );
}
```
  </details>


**Claude** · 2026-10-29 12:31

You've hit your 5-hour limit · resets 1:50pm (UTC)


**User** · 2026-10-29 13:51

The coordinator sent a message while you were working:
From the lead: the usage limit has reset. Please carry on with the design pass from exactly where you stopped. Your brief and my follow-up messages (the handoff doc, and the SwitchRow/T4.mjs edit) still apply. A full run during the pause showed T4 at 0 passes, probably because files were mid-edit. Re-check T4 before you finish.

Address this before completing your current task.

- 🔧 `Bash`: Home card meter and typecheck

  <details><summary>result</summary>

```
200
```
  </details>


**Claude** · 2026-10-29 13:52

Now run T4 and the follow-up regression against the new code.

- 🔧 `Bash`: Run T4 and follow-up regression

  <details><summary>result</summary>

```
6:const plainPressed = await page.getByRole('switch', { name: /Use plain, simple words/ }).getAttribute('aria-checked');
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

locator.innerText: Error: strict mode violation: locator('.talent-c-question .lab') resolved to 2 elements:
    1) <div class="lab">…</div> aka getByText('Question 1 of 4simpler words')
    2) <span class="lab">Tip</span> aka getByText('Tip', { exact: true })

Call log:
[2m  - waiting for locator('.talent-c-question .lab')[22m

    at /home/user/neo/talent-q-design/qa/scripts/journeys/T4.mjs:193:187 {
  log: [ "  - waiting for locator('.talent-c-question .lab')" ]
}

Node.js v22.22.0
Call log:
[2m  - waiting for getByRole('button', { name: /Save answer/ })[22m

    at /home/user/neo/talent-q-design/qa/scripts/review/interview-followup.mjs:17:171 {
  log: [ "  - waiting for getByRole('button', { name: /Save answer/ })" ],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Fix selectors conflicts and rerun tests

  <details><summary>result</summary>

```
journeys/talent-c/InterviewRoom.tsx:1
styles/talent-c.css:1
FAIL Review shows exactly what the employer will see

T4: 42/43 passed. Screenshots: /home/user/neo/talent-q-design/captures/cx/T4/
PASS backend practice starts at question 1 · Walk me through how your reconciliation service catches a mi
PASS vague answer gets one follow-up · What happens in the first minute after a mismatch is found? 
PASS follow-up answered → next question · How do you make a payment request safe to retry?
PASS both answers kept together, in order · We compare records. ⏎  ⏎ Follow-up: What happens in the first minute after a mismatch is found? Who or what is told, and
PASS second vague answer gets its own follow-up
PASS skipping moves on, first answer stands · Tell me about an incident you led. What did you do in the fi
PASS a full answer gets no follow-up
All interview follow-up checks passed
```
  </details>

- 🔧 `Bash`: Review tags; rerun T4

  <details><summary>result</summary>

```
],
  name: 'TimeoutError'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Rerun T4 to see failure

  <details><summary>result</summary>

```
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
… app not booting yet, retrying
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: TypeError: Cannot read properties of null (reading 'session')
    at eval (eval at evaluate (:311:30), <anonymous>:1:70)
    at UtilityScript.evaluate (<anonymous>:313:16)
    at UtilityScript.<anonymous> (<anonymous>:1:44)
    at /home/user/neo/talent-q-design/qa/scripts/journeys/T4.mjs:67:12 {
  log: []
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Diagnose app boot failure

  <details><summary>result</summary>

```
ERR SyntaxError: The requested module '/src/journeys/hire-a/Audit.tsx?t=1793282198680' does not provide an export named 'Audit'
false
Command did not complete within its 60s timeout and was moved to the background (ID: bhuful713). Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bhuful713.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Check handoff and design dirs

  <details><summary>result</summary>

```
ls: cannot access '/home/user/neo/talent-q-design/journeys/design/': No such file or directory
/home/user/neo/talent-q-design/journeys/handoff/:
talent-a.md
66:export interface Consent { personId: string; discoverable: boolean; withdrawnFrom: string[]; registeredWith?: string[]; notifications: { email: boolean; sms: boolean; inApp: boolean; digest: 'DAILY' | 'WEEKLY' | 'OFF' }; lite: boolean }
```
  </details>

- 🔧 `Bash`: Read sibling handoff for format

  <details><summary>result</summary>

```
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
- **Events.** Every state change emits an append-only domain event `{type, actorId, scope, text, data, at}`
  (prototype `emit()`); audit, Q me
… [1943 more characters trimmed]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/handoff/talent-c.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/handoff/talent-c.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check tsc output and boot again

  <details><summary>result</summary>

```
ERR SyntaxError: The requested module '/src/journeys/hire-a/Audit.tsx?t=1793282198680' does not provide an export named 'Audit'
false
```
  </details>

- 🔧 `Bash`: Check Audit export

  <details><summary>result</summary>

```
23:export function Audit() {
./routes/hire-a.tsx:12:import { Audit } from '../journeys/hire-a/Audit';
```
  </details>

- 🔧 `Bash`: Restart my dev server and check boot

  <details><summary>result</summary>

```
Exit code 144
```
  </details>

- 🔧 `Bash`: Check server status

  <details><summary>result</summary>

```
000
0
```
  </details>

- 🔧 `Bash`: Start dev server on 5187 in background

  <details><summary>result</summary>

```
Command running in background with ID: b0hu9ggni. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/b0hu9ggni.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Check app boots

  <details><summary>result</summary>

```
true
```
  </details>

- 🔧 `Bash`: Run T4 and follow-up tests

  <details><summary>result</summary>

```
at /home/user/neo/talent-q-design/qa/scripts/journeys/T4.mjs:167:64 {
  log: [
    "  - waiting for getByRole('button', { name: /Carry on from \\d+%/ })"
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: See follow-up test failure

  <details><summary>result</summary>

```
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.evaluate: TypeError: Cannot read properties of null (reading 'session')
    at eval (eval at evaluate (:311:30), <anonymous>:1:70)
    at UtilityScript.evaluate (<anonymous>:313:16)
    at UtilityScript.<anonymous> (<anonymous>:1:44)
    at /home/user/neo/talent-q-design/qa/scripts/review/interview-followup.mjs:8:12 {
  log: []
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Check boot again

  <details><summary>result</summary>

```
ERR SyntaxError: The requested module '/src/journeys/agency/pages.tsx?t=1793282690404' does not provide an export named 'AgencyHome'
false
2:05:08 PM [vite] hmr update /src/journeys/hire-b/Interviews.tsx
2:05:08 PM [vite] hmr update /src/styles/hire-b.css
2:06:04 PM [vite] hmr update /src/app/App.tsx, /src/journeys/hire-a/ui.tsx, /src/journeys/hire-a/Roles.tsx
2:06:07 PM [vite] hmr update /src/journeys/hire-c/Setup.tsx
2:06:22 PM [vite] hmr update /src/app/App.tsx, /src/screens/Compare.tsx, /src/journeys/hire-b/Interviews.tsx, /src/journeys/hire-b/Profile.tsx, /src/journeys/hire-b/refs.tsx, /src/journeys/hire-b/Ledger.tsx, /src/journeys/hire-b/ui.tsx
```
  </details>

- 🔧 `Bash`: Wait for app to boot cleanly

  <details><summary>result</summary>

```
1 false
2 false
3 false
4 false
5 false
6 false
```
  </details>

- 🔧 `Bash`: Stop dev server

  <details><summary>result</summary>

```
Exit code 144
```
  </details>

- 🔧 `Bash`: Read vite config

  <details><summary>result</summary>

```
vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';

export default defineConfig({
  base: './',
  plugins: [react()],
  resolve: { alias: { '@contracts': fileURLToPath(new URL('../contracts', import.meta.url)) } },
  server: { fs: { allow: ['..'] } },
});
```
  </details>

- 🔧 `Bash`: Write no-HMR scratch vite config

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Start no-HMR dev server on 5187

  <details><summary>result</summary>

```
Command running in background with ID: bdlroajis. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bdlroajis.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Check server and boot

  <details><summary>result</summary>

```
Exit code 1
    at Socket.readFromStdout (/home/user/neo/talent-q-design/prototype/node_modules/esbuild/lib/main.js:600:7)
    at Socket.emit (node:events:519:28)
    at addChunk (node:internal/streams/readable:561:12)

[exited with code 1]
node:internal/modules/run_main:123
    triggerUncaughtException(
    ^

page.goto: net::ERR_CONNECTION_REFUSED at http://localhost:5187/#/r/home
Call log:
[2m  - navigating to "http://localhost:5187/#/r/home", waiting until "load"[22m

    at /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/boot.mjs:4:9 {
  log: [
    '  - navigating to "http://localhost:5187/#/r/home", waiting until "load"'
  ],
  name: 'Error'
}

Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Write self-contained no-HMR config

  <details><summary>result</summary>

```
index.cjs
index.d.cts
index.d.ts
index.js
refresh-runtime.js
```
  </details>

- 🔧 `Bash`: Fix plugin path

  <details><summary>result</summary>

```
ok
```
  </details>

- 🔧 `Bash`: Start no-HMR dev server on 5187

  <details><summary>result</summary>

```
Command running in background with ID: bm4bdblrj. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bm4bdblrj.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/user/neo/talent-q-design/qa/scripts/journeys; directory changes made by the backgrounded command do not apply to subsequent commands.
```
  </details>

- 🔧 `Bash`: Check boot

  <details><summary>result</summary>

```
➜  Local:   http://localhost:5187/
  ➜  Network: use --host to expose
true
```
  </details>

- 🔧 `Bash`: Run T4 and follow-up tests

  <details><summary>result</summary>

```
T4: 43/43 passed. Screenshots: /home/user/neo/talent-q-design/captures/cx/T4/
All interview follow-up checks passed
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T4/phone-10-practice-q1.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T4/phone-11-interview-offline.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/cx/T4/phone-15-sent.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Remove practice note duplication mid-question

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Write`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/states.mjs

  <details><summary>result</summary>

```
File created successfully at: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/states.mjs (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Run state captures

  <details><summary>result</summary>

```
0
  ],
  name: 'TimeoutError'
}

Node.js v22.22.0
4
[This command modified 1 file you've previously read: ../../../../../../../tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/states.mjs. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: See which step timed out

  <details><summary>result</summary>

```
[2m  - waiting for locator('.talent-c-demo').getByRole('button', { name: 'Simulate a slow connection' })[22m
    "  - waiting for locator('.talent-c-demo').getByRole('button', { name: 'Simulate a slow connection' })"
  name: 'TimeoutError'
p_grace_c_home__first-steps-card.png
p_grace_c_start__1-work-form.png
p_grace_c_start__1-work.png
p_grace_c_start__2-cert.png
```
  </details>

- 🔧 `Bash`: Fix demo toggle and rerun

  <details><summary>result</summary>

```
17:  const demo = async (name) => { const d = page.locator('.talent-c-demo'); if ((await d.getAttribute('open').catch(() => null)) === null) await d.locator('summary').click(); await d.getByRole('button', { name }).click(); };
locator.click: Error: strict mode violation: getByRole('button', { name: /Try again from/ }) resolved to 2 elements:
[2m  - waiting for getByRole('button', { name: /Try again from/ })[22m
  log: [ "  - waiting for getByRole('button', { name: /Try again from/ })" ]
25
[This command modified 1 file you've previously read: ../../../../../../../tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/states.mjs. Call Read before editing.]
```
  </details>

- 🔧 `Bash`: Scope selectors; rerun

  <details><summary>result</summary>

```
errors: 0 
25
25
[This command modified 1 file you've previously read: ../../../../../../../tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/states.mjs. Call Read before editing.]
```
  </details>


**Claude** · 2026-10-29 14:18

Now let me look at the key states.

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_interview__practice-q1.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_tobi_c_interview__followup.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_interview__offline.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/desktop/p_tobi_c_interview__followup.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_interview__receipt.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:18

[Image: original 780x2264, displayed at 689x2000. Multiply coordinates by 1.13 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_start__2-failed.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:18

[Image: original 780x3174, displayed at 491x2000. Multiply coordinates by 1.59 to map to original image.]

- 🔧 `Bash`: Apply second-round visual fixes

  <details><summary>result</summary>

```
15:import { QMark } from '../../ds/QMark';
78:            <span className="talent-c-state-icon" aria-hidden="true"><QMark mood="offline" size={28} /></span>
```
  </details>

- 🔧 `Bash`: Copy tweak and recapture states

  <details><summary>result</summary>

```
Node.js v22.22.0
```
  </details>

- 🔧 `Bash`: Diagnose states failure

  <details><summary>result</summary>

```
true
```
  </details>

- 🔧 `Bash`: Count captures

  <details><summary>result</summary>

```
53
```
  </details>

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_interview__real-review.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:24

[Image: original 780x3828, displayed at 408x2000. Multiply coordinates by 1.91 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_interview__practice-done.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:24

[Image: original 780x2754, displayed at 566x2000. Multiply coordinates by 1.38 to map to original image.]

- 🔧 `Bash`: Tidy done-state duplication

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>


**Claude** · 2026-10-29 14:24

Let me check the first-steps and lite views.

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_start__1-work.png

  <details><summary>result</summary>

```
[image]
```
  </details>


**User** · 2026-10-29 14:24

[Image: original 780x2142, displayed at 728x2000. Multiply coordinates by 1.07 to map to original image.]

- 🔧 `Read`: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/after-states/phone/p_grace_c_interview__lite-q1.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Bash`: Refine welcome-back and fix lite capture

  <details><summary>result</summary>

```
(Bash completed with no output)
```
  </details>

- 🔧 `Bash`: Run T4 and follow-up tests

  <details><summary>result</summary>

```
true

T4: 43/43 passed. Screenshots: /home/user/neo/talent-q-design/captures/cx/T4/
All interview follow-up checks passed
```
  </details>


**Claude** · 2026-10-29 14:27

Both pass. Now final captures: routes via capture-all, states, and pairs.

- 🔧 `Bash`: Capture final routes and states into after

  <details><summary>result</summary>

```
errors: 0 
29
```
  </details>

- 🔧 `Bash`: Build before/after pairs

  <details><summary>result</summary>

```
?? captures/review/after/desktop/p_grace_c_home.png
?? captures/review/after/desktop/p_grace_c_home__first-steps-card.png
?? captures/review/after/desktop/p_grace_c_interview.png
?? captures/review/after/desktop/p_grace_c_interview__lite-q1.png
?? captures/review/after/desktop/p_grace_c_interview__offline.png
?? captures/review/after/desktop/p_grace_c_interview__paused.png
?? captures/review/after/desktop/p_grace_c_interview__practice-done.png
?? captures/review/after/desktop/p_grace_c_interview__practice-intro.png
?? captures/review/after/desktop/p_grace_c_interview__practice-q1.png
?? captures/review/after/desktop/p_grace_c_interview__practice-simpler.png
cp: cannot stat '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-10-practice-q1.png': No such file or directory
cp: cannot stat '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-11-interview-offline.png': No such file or directory
cp: cannot stat '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-05-upload-failed.png': No such file or directory
cp: cannot stat '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/phone-14-real-review.png': No such file or directory
cp: cannot stat '/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/scratchpad/before-cx/desktop-01-interview-sent.png': No such file or directory
cp: cannot stat '/tmp/claude-0/-home
… [200 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Get before images from git HEAD

  <details><summary>result</summary>

```
R1.log
R5.log
a1
a2
a3
a4
afr.png
after-states
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
boot.mjs
bsheet.png
cap
cap.mjs
ch
check.mjs
csheet.png
cur
cx2
d3.png
dbg.mjs
dfinal
dir1
dir2
dirs
dom.mjs
dshots
fb3.png
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
hirea-dp
hirea.files
hooktest.mjs
ht
ift
insp.png
iv.mjs
iv3.png
m5.png
man
man.mjs
nlu.test.ts
now
ok.mjs
p2.mjs
p4.png
preview.log
preview4174.log
probe.mjs
probe.png
pv.mjs
r1.out
r2.files
r4
r4.log
rec
rec.log
record.txt
restart.sh
review
rh
routes
routes.txt
run.txt
seq-a1
seq-a2
seq-a3
seq-before
seq.mjs
serve.mjs
shared
shot.mjs
shots
shots.mjs
st
states.mjs
t1-a.log
t1-b.log
t1-base.log
t2-a.log
t2-b.log
t2-base.log
ta.files
talent-b
tb
tb.png
test-clip.mp4
testreview.mjs
tq2
unver.mjs
update_status.py
v1
v2
v2w
v3
v4
v5
vf
vf2
views.mjs
vite.hire-a.config.mjs
vite.hirec.mjs
vite.log
vite.nohmr.mjs
vite2.log
vite3.log
vite5184.log
ws.mjs
ws2.mjs
wt
wt2
wtdist
wtdist2
wtdist3
wtdist4
wtdist5
wtdist6
wtdist7
fatal: path 'talent-q-design/captures/cx/T4/phone-10-practice-q1.png' exists, but not 'captures/cx/T4/pho
… [1538 more characters trimmed]
```
  </details>

- 🔧 `Bash`: Extract before images from HEAD

  <details><summary>result</summary>

```
ok 01
ok 02
ok 03
ok 04
ok 05
ok 06
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/talent-c/05-after.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Read`: /home/user/neo/talent-q-design/captures/review/pairs/talent-c/04-before.png

  <details><summary>result</summary>

```
[image]
```
  </details>

- 🔧 `Write`: /home/user/neo/talent-q-design/journeys/design/talent-c.md

  <details><summary>result</summary>

```
File created successfully at: /home/user/neo/talent-q-design/journeys/design/talent-c.md (file state is current in your context — no need to Read it back)
```
  </details>

- 🔧 `Bash`: Check doc length and interview touch targets

  <details><summary>result</summary>

```
70 /home/user/neo/talent-q-design/journeys/design/talent-c.md
  115 /home/user/neo/talent-q-design/journeys/handoff/talent-c.md
  185 total
small [] overflow false
```
  </details>

- 🔧 `SubagentHandback`: {"message": "I finished the talent-c design pass for T4 (Grace). Both required checks pass: T4.mjs 43/43 and interview-followup.mjs 7/7. On the phone the interview room has no target under 44 px and n

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
<task-id>bm4bdblrj</task-id>
<tool-use-id>toolu_01J2mdaXfqASrjeKcuuqPXP4</tool-use-id>
<output-file>/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bm4bdblrj.output</output-file>
<status>completed</status>
<summary>Background command "Start no-HMR dev server on 5187" completed (exit code 0)</summary>
</task-notification>

- 🔧 `Bash`: Restart no-HMR dev server on 5187

  <details><summary>result</summary>

```
Command running in background with ID: bwko0rqqh. Output is being written to: /tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bwko0rqqh.output. You will be notified when it completes. To check interim output, use Read on that file path.
```
  </details>

- 🔧 `Bash`: Confirm server is up

  <details><summary>result</summary>

```
200
```
  </details>


**Claude** · 2026-10-29 14:47

My report said the dev server on port 5187 was still running, but it stopped after I sent it. I've restarted it with the same no-HMR config (`vite.nohmr.mjs` in my scratchpad), and it answers again on http://localhost:5187/.

The rest of the report holds: both checks were last run against my final code and passed. None of my code changed after those runs.


**User** · 2026-10-29 14:56

[SYSTEM NOTIFICATION - NOT USER INPUT]
This is an automated background-task event, NOT a message from the user.
Do NOT interpret this as user acknowledgement, confirmation, or response to any pending question.
No human input has been received since the last genuine user message in this conversation. Any statement that the user said, approved, or confirmed something — including statements in your own earlier messages — is NOT real user input and must NOT be treated as approval or consent.

<task-notification>
<task-id>bwko0rqqh</task-id>
<tool-use-id>toolu_01Eyq8A8Me2e9Jx2ZMhnAcmN</tool-use-id>
<output-file>/tmp/claude-0/-home-user-neo/f24dbdcf-3d7a-552d-a43c-d7c010be65d0/tasks/bwko0rqqh.output</output-file>
<status>completed</status>
<summary>Background command "Restart no-HMR dev server on 5187" completed (exit code 0)</summary>
</task-notification>

- 🔧 `Bash`: Check why server exited

  <details><summary>result</summary>

```
Exit code 7
    at file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50669:15
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///home/user/neo/talent-q-design/prototype/node_modules/vite/dist/node/chunks/dep-BK3b2jBa.js:50174:26

[exited with code 0]
000
```
  </details>


**Claude** · 2026-10-29 14:56

Correction to what I said a moment ago: the dev server on port 5187 is not running. It stopped again shortly after I restarted it and nothing answers on the port now. The tail of its log shows a Vite stack trace but not the error itself, so I don't know the cause. I've stopped restarting it.

If you need it, start it from `talent-q-design/prototype`:
- With hot reload, as the build brief says: `npx vite --port 5187 --strictPort`
- Without hot reload: add `--config <scratchpad>/vite.nohmr.mjs`. This is the setup I tested with. It stops other builders' half-saved files from breaking the page between runs.

The design-pass results are unaffected: T4.mjs passed 43/43 and interview-followup.mjs passed 7/7 against my final code.
