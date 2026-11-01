# Capital Q Demo Script

Oct 9, 2026 · @Ademola Daniel

A 10-minute run through Capital Q, built only from journeys we have seen work. Rehearse every step on production the day before; anything that misbehaves in rehearsal comes out of the script.

## Before you go on stage

Do these the morning of the demo; each one takes under a minute.

- [ ] Sign in as **Zino** in Chrome on a normal (non-hotel-captive) network. GPT-Live only runs for your four allowlisted accounts.
- [ ] Check OpenAI credit has at least $10 left. GPT-Live is $0.05 a minute; Q Brain and the fallback voice share the same key.
- [ ] Use a headset or earbuds with a mic. Speakers feed Q's voice back into the mic.
- [ ] Open /home once and wait 10 seconds before the audience is watching: the briefing loads in the background so the first call opens with it.
- [ ] Do one 30-second practice call, say "what needs my attention", and hang up. If it answers in under 5 seconds, you are ready.
- [ ] Keep one tab only. Close any other Capital Q tab, so only one voice can ever play.
- [ ] Tell me the demo time: I will not deploy anything in the 6 hours before it.

## The demo, step by step

Seven beats, about 10 minutes, all on voice from /home. Speak naturally; you do not need these exact words, they are what we tested.

| # | You say or do | What the room sees and hears | How sure we are |
| --- | --- | --- | --- |
| 1 | Open /home and press the Q button. | Q greets you by name and gives the lowdown: what your agents did and how many things need you, naming the top two or three. Cards sit beside Q. | Seen live in production on your 07:29 call. |
| 2 | "What needs my attention?" | Q names the real items (a reply waiting, an approval, a held draft) and says plainly if a source could not be checked. Never a fake "all clear". | Seen live in production on your 07:29 call. |
| 3 | "Show me the three best companies for my mandate." | Exactly three company cards. Each shows mandate fit out of 10, how many of the 7 measures are known, and its sources. Q says when scores are tied and why. | Browser-tested 3 of 3 runs. Speed fix deployed today: rehearse it. |
| 4 | "Tell me more about the second one." | Q keeps the reference and talks about the second company, not a new list. | Browser-tested 3 of 3; also heard in the real GPT-Live recording. |
| 5 | Interrupt Q mid-sentence: "Wait, just the short version." | Q stops at once and gives the one-line version. | Real GPT-Live recording (scenario 4). |
| 6 | Make a joke, or say "you can laugh at that". | Q laughs lightly and carries on. No forced laughter on its own. | Real GPT-Live recording (founder retest). |
| 7 | "Open Discover." | The page moves before Q finishes its sentence. | Browser-tested 6 of 6; the voice fix ships today: rehearse it. |

If you want an eighth beat for investors in the room: say a sentence in Pidgin ("Guy, how far?"). Q understands and answers in natural English. Heard in the real recordings.

## Wow moments

Pause after each of these and let the room react.

1. **Q briefs you before you ask** (beat 1). Point out that nobody typed anything: Q already knows what happened and what needs a decision.
2. **It sounds like a person** (beats 5 and 6). Interrupt it, change your mind, make it laugh. Say: "That is the voice an investor talks to all day."
3. **Evidence, not opinion** (beat 3). Point at "5 of 7 measures known" and "no source documents yet": Q says what it does not know instead of inventing a score.
4. **It acts, not just talks** (beat 7). The screen moves while Q is still speaking.

## If something goes wrong

| What happens | What to do on stage |
| --- | --- |
| Q is quiet for more than 5 seconds after a question | Say "take your time" and wait; Q says one progress line and then answers. If nothing after 20 seconds, type the same question in the Q box: the cards come the same way. |
| The voice changes to a different-sounding one | GPT-Live could not connect and Q fell back to the standard voice. Carry on: everything else works the same. |
| A page does not open by voice | Say it again with the page name first ("Discover, open it"), or click it. |
| Cards do not appear | Ask "show me the cards"; they are also on the Board (one tap). |
| Q mishears a company name | Say the name once more, slowly; it learns your companies' names from your records. |

## Do not demo yet

These are built and pass automated tests, but nobody has watched them work end to end. Leave them out unless a rehearsal on production goes cleanly.

- **Onboarding by voice with GPT-Live.** Wired in; never run in a browser, because the test data has no account mid-onboarding.
- **Card spotlight** (the company being discussed grows, the rest shrink). Built and browser-tested locally; deploying after today's checks. Rehearse before relying on it.
- **Work agents acting on their own** (follow-ups, reminders under a standing instruction). The new rules are unit-tested only; show the approval card, not an agent sending on its own.
- **Documents and decks made by Q.** Not part of this week's verification.
- **Long calls over 15 minutes.** The session renewal is unit-tested only.

## How each step was proven

| Level | What it means | Steps |
| --- | --- | --- |
| Seen live in production | Happened on your own calls on the live app | 1, 2 |
| Real GPT-Live recording | Real gpt-live-1 voice; your side was synthetic speech | 4, 5, 6, the Pidgin beat |
| Browser-tested | Real Chromium against the full app, with scripted AI answers, repeated 3 or more times | 3, 4, 7 |
| Unit-tested only | Code tests, no browser | Everything under Do not demo yet |

Nothing here has been tested with a real microphone on a stage network. The rehearsal on production is the final test: run beats 1 to 7 once, the day before.
