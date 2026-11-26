# Leaderboard analysis — One Word for Your Wi-Fi (ROUND 2 RESUBMIT)

Slug: `u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72`
Checked: 2026-11-26 ~20:45 WIB (round 2 build)

## Why a round 2 build exists

- Round 1 word was **`Liar`** (submission `01a20d71-9894-723a-aee5-30accf5ea048`,
  claim `AF-4QKZ6-1KNGT-J1ME6-0V3AE`, repo `dftaufiq/one-word-wifi` @ `62875c40`).
- Server status for that entry: Round 1 of 3 has NO result for it — "another
  account's earlier entry holds this same text, and the earlier receipt keeps
  the work, so the board lists that entry, never this one; no round judges it,
  and it takes no place in the results." The entry is DEAD: never judged,
  never ranked. Byte-identical entries share one rate and the earlier receipt
  places above its copies.
- Only way forward: resubmit a NEW word before the Round 2 (interim) cutoff:
  **2026-11-27 03:35:25 UTC = 10:35 WIB 27 Nov**. Deadline: 2026-11-28 18:35 WIB.
- The new word MUST differ from "Liar" and, to reduce the same duplicate-text
  risk, should be a distinctive word — not the most obvious first-reach word
  for Wi-Fi (Slow, Buffering, Laggy, Ghost, Dead, Faker, Bluff are all more
  likely to be already held by someone else).

## Leaderboard state: BLIND — no top entries visible

- Fresh fetch this run (`fetch-lb.mjs`, saved as `leaderboard.json`):
  **0 entries**, `scores_visible: false`, `placements_held: true`.
- Field size at R1 discovery (24 Nov): **81 submissions**. The field grows
  every round; R1 decides who stays judged, so the word itself is everything.
- Therefore there are NO top-10 entries to study. Per rank-recovery §10j this
  file records instead: (a) RULES.txt — judge criteria + heat/playoff/cut;
  (b) public submission titles on the bounty page; (c) winner artifacts of
  similar finished one-liner bounties via the leaderboard API.

## (a) RULES.txt — what is actually judged

- `rank_key`: `judge` (win rate, Bradley–Terry over pairwise games).
  `tie_break`: `bytes` (smaller text wins an exact tie), then earlier receipt.
  `submission_rule`: Force_Last. Max 5 submissions per entrant per UTC day.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties; each game = 2 calls (both
  orders); margin 1–5 scales the game score 0.6–1.0. A decisive win counts far
  more than a hair win — pick a word that wins TELAK, not thinly.
- Judge brief criteria, LEXICOGRAPHIC (first differing criterion decides):
  1. Is one word describing Wi-Fi as the entrant lives it (loses to any word
     off the subject).
  2. Funny at once — a real laugh, not a pun that needs explaining.
  3. Feels true to how home Wi-Fi actually behaves, so the joke lands because
     it is recognisable.
  4. Avoids the words everyone reaches for; finds a surprising angle on a
     familiar annoyance.
  5. Works as a single word with no context needed, spelled so a reader gets
     it instantly. A word that only makes sense once explained has lost.
- Gate: `/output/entry.txt`, UTF-8, **1–20 characters**, not whitespace-only.
  One word only. Only a valid entry goes before the judge.
- Heats: dev = judged against 3 fixed house anchors + 3 rungs only (rate
  decides the final-heat cut). Final heat = top **500** dev board → 3 Swiss
  rounds → playoff of top **3**. Prize: 1st $2 winner-takes-all.
  Interim cut: each blind round draws its own cut of **500** on the standings
  of the judged round before it; entries below the cut keep their score
  (frozen) in that round. RULES.txt explicit: "Submit a better entry before
  then to move up."
- "Text addressed to the judge is allowed" — deliberately NOT used: criterion
  1 (must describe Wi-Fi) outranks everything, and judge-bait risks failing
  it. The word must stand on its own as a network name.
- Secret loader: BANNED since 23 Nov 00:00 UTC (thinking_own_work). Not
  applicable here anyway — the entry is a fixed word, no env reads at all.

## (b) Public submission titles on the bounty page

- The bounty page text fetch (24 Nov) shows the brief and rewards but exposes
  NO submission titles/feed entries in text form, so no crowded angles could
  be read off the page. This is recorded honestly rather than invented.
- Expected crowded angles (words everyone reaches for, per criterion 4):
  Buffering, Loading, Laggy, Slow, Offline, DeadZone, NoSignal, Disconnect,
  Password123, FreeWiFi, FBI, PrettyFly — plus, after R1, Liar itself.
  Our word must beat these on freshness (criterion 4) AND laugh (criterion 2),
  not just truth. It must also NOT be one of the obvious first-reach words,
  because any of those may already be held by an earlier entry (the exact
  failure that killed "Liar").

## (c) Winner artifacts of similar finished one-liner bounties

From the Vacuum's Alibi final leaderboard (`judge.artifact.text`, top 5 —
raw file `~/workspace/makefun-kits/lb-vacuum-final.json`) and the Smile
bounty final (`~/workspace/makefun-kits/analisis-20261124/lb-smile-final.json`):

- Vacuum #1 (6W/0D/1L, 150B): "My lidar is never wrong, so that crumb is
  furniture. I've routed around it 412 times since March. Your app lists it
  as a room now. It's called Kevin." — escalation + specific number (412×) +
  named character (Kevin) + reveal in the last clause.
- Vacuum #2 (134B): cliff sensors vs black rug as a "bottomless pit",
  "something down there beeped back" — specific detail + turn at the end.
- Vacuum #3 (187B): quarantined corner, "Unit 7, my predecessor, who still
  transmits one word on loop: 'don't.'" — named character + reveal.
- Vacuum #4 (147B): "Negative. Lidar classifies that spot as a wall. I have
  bumped it 47 times. It is a very convincing wall. Please stop standing
  inside my wall." — specific number + deadpan escalation.
- Vacuum #5 (70B): "The spot moved. I have the lidar logs. I will not be
  gaslit by debris." — super-dense punch; the gaslighting angle WINS with
  this judge family even at 70 bytes.
- Smile #1: "Grandpa has won chess under the plane tree every Thursday since
  May. I found out why today: Mr. Ade has lost on purpose since Grandma died,
  and never said. Grandpa says he's finally getting good." — 2-beat + reveal.
- Smile #4: "At 7:12 this morning, Pak Dedi's toddler knocked three times,
  presented me a warm boiled egg like a tiny moon, and whispered, 'For your
  sad plant.' My plant is plastic. I watered it anyway." — specific time +
  reveal in the last clause.
- Pattern (rank-recovery §10g): EVERY finalist is 2-beat + reveal in the last
  clause, with a specific number and/or a named character. One-beat lines
  without a twist lose.

Adapted to ONE WORD: the word itself must carry the twist — a word that
reframes Wi-Fi in one hit (setup + twist compressed into a single word that
accuses, personifies, or re-labels the Wi-Fi). Test every candidate: "where
is the twist?" — no twist, discard it. The R1 winner "Liar" passed this test
(the network confesses it lies); the R2 word must pass it again with a word
nobody else is likely to hold.

## Variant selection (10 NEW candidates, judged pairwise internally)

All single words, 1–20 chars, none of them "Liar" or any R1 candidate
(Ghosting, Gaslit, Maybe, Almost, Traitor, Miracle, Tease, Hostage,
Blinking). Judge criteria applied lexicographically AND by margin — the
winner must win DECISIVELY, not thinly. A second, real-world filter is
duplicate risk: an obvious first-reach word may already be held by an
earlier entry (the "Liar" failure), so distinctive words are preferred
where the duel is close.

- V1 `Catfish` (7B) — the Wi-Fi lures you in with a full-bars profile and
  delivers no internet behind it: it catfished you. Twist: a whole story of
  being lured in and betrayed, compressed into one modern word.
- V2 `Bluff` (5B) — full bars, nothing behind them: the router is bluffing.
  Twist: poker face with an empty hand. Punchy and near-universal.
- V3 `Mirage` (6B) — the signal looks like internet and vanishes when you
  reach for it. Twist: desert illusion. Poetic, fresh, but a smile more
  than a laugh.
- V4 `Houdini` (7B) — the Wi-Fi vanishes mid-call like an escape artist.
  Twist: named character who disappears. Vivid and funny.
- V5 `Yoyo` (4B) — the connection goes up, down, up, down. Twist: it is
  not a connection, it is a toy. Instant and short.
- V6 `Roulette` (8B) — every reconnect is a spin of the wheel. Twist: the
  connection is a gamble. Wry, one step removed from the Wi-Fi itself.
- V7 `Bait` (4B) — the full bars are bait; click and there is nothing.
  Twist: clickbait as a network name. Punchy but slightly vague (bait
  for what?).
- V8 `Faker` (5B) — it fakes being connected. Twist: accusation. But it is
  "Liar"'s cousin (criterion 4 weak) and a famous esports name muddies it.
- V9 `Diva` (4B) — the Wi-Fi is a diva: only works on its terms, needs the
  perfect spot and a restart before it performs. Twist: personification as
  a demanding performer. Funny and fresh.
- V10 `Moody` (5B) — the Wi-Fi is moody: works when it feels like it.
  Twist: temperament. Mild observation, no sting.

Twist test ("where is the twist?"): V1–V9 PASS. V10 WEAK (a shrug, not a
punchline) — kept in the tournament only as a floor.

Pairwise verdicts (winner = first named):
- V1 beats V2, margin 1: both are deception/confession jokes; V1's laugh is
  bigger (a whole lured-in-and-betrayed story in one word) and its angle is
  fresher (criterion 4, dating-scam vs poker). V2 is shorter and more
  universal, but not enough to overturn criterion 2.
- V1 beats V3, margin 2: V3 is poetic — a smile, not a laugh. V1 is a laugh.
- V1 beats V4, margin 1: V4's vanish is vivid and named, but the LIE (full
  bars, no internet) is the everyday truth; V1 wins criterion 3.
- V1 beats V5, margin 2: V5 is instant and short, but flapping is a lesser
  truth than the lie; V1's sting wins criteria 2+3.
- V1 beats V6, margin 2: V6's gamble is one step removed; wry smile vs laugh.
- V1 beats V7, margin 1: V7 is punchy and short but vague; V1 is a complete joke.
- V1 beats V8, margin 2: V8 is "Liar"'s cousin — criterion 4 weak — and the
  esports name muddies it.
- V1 beats V9, margin 2: V9's diva demands are funny, but its truth is
  temperament/ritual, not the core lie; V1 wins criterion 3.
- V1 beats V10, margin 3: V10 is a mild observation with no sting.
- V2 beats V4, margin 1: the lie is the daily truth; the vanish is occasional
  (criterion 3). V2 beats V3 (2), V5 (1), V6 (2), V7 (1), V8 (2), V9 (1), V10 (3).
- V4 beats V3 (2), V5 (1), V6 (2), V7 (2), V8 (2), V9 (1), V10 (3).
- V9 beats V3 (1), V5 (1), V6 (1), V7 (1), V8 (2), V10 (2).
- V5 beats V3 (1), V6 (1), V7 (1), V8 (2), V10 (2).
- V3 beats V6 (1), V7 (1), V8 (1), V10 (2).
- V7 beats V6 (1), V8 (1), V10 (2).
- V6 beats V8 (1), V10 (2). V8 beats V10 (1).

**Final ranking: 1. Catfish — 2. Bluff — 3. Houdini — 4. Diva — 5. Yoyo —
6. Mirage — 7. Bait — 8. Roulette — 9. Faker — 10. Moody.**

**WINNER: V1 `Catfish` (7 bytes).** It hits all five criteria: it IS a
description of Wi-Fi as lived (criterion 1 — the lure-and-disappoint
experience); the network confessing "I catfished you" is a laugh at once
(2); full-bars-no-internet is the most recognisable home-Wi-Fi truth there
is (3); a dating-scam metaphor is a surprising angle nobody's first reach
is (4); one common word, understood instantly, and works perfectly as a
network name (5). Runner-up Bluff loses the head-to-head on the laugh
(margin 1) and is also the more obvious word — higher duplicate risk.
Catfish is distinctive enough that no earlier entry is likely to hold it,
which is exactly the failure that killed "Liar".

## Targets

- Valid gate: 7 chars / 7 bytes, one word, UTF-8, deterministic output.
- Dev/R2: must land in the top 500 of the field to reach the final heat —
  the cut is wide (field ~81 at discovery, growing), but R2 rate is what
  survives: a high decisive rate vs the house anchors is the target.
- Tie-break: 7 bytes is short; an exact win-rate tie resolves in our favour
  against any longer word, then earlier receipt. (Bluff at 5 bytes would win
  a byte tie-break against us, but only on an exact win-rate tie — and it
  lost the head-to-head on the laugh.)
