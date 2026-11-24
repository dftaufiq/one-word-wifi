# Leaderboard analysis — One Word for Your Wi-Fi

Slug: `u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72`
Checked: 2026-11-24 ~18:50 WIB (before any coding)

## Leaderboard state: BLIND — no top entries visible

- `GET /api/competitions/<slug>/leaderboard?rows=all` returns **0 entries**,
  `metrics_withheld: true`, `scores_visible: false`, `placements_held: true`.
  Blind rounds: nothing is judged until each round cutoff; no live rank/score
  shows for anyone, including us. Raw response saved as `leaderboard.json`.
- Field size at discovery: **81 submissions** already. Small field vs the
  500-seat heat (see below) — but the field grows every round and R1 decides
  who stays judged, so the word itself is everything.
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
  (frozen) in that round. With a field of ~81–a few hundred, the 500 cut is
  generous — the operational target is still a high R1 rate, because the
  field grows ~34% per round and frozen scores only fall.
- Round 1 cutoff: 2026-11-26 02:35 WIB (2026-11-25T19:35:51Z). Deadline:
  2026-11-28 18:35 WIB. Blind round: do NOT chase a ~15-minute submit;
  quality first (this is neither score-saturated nor view-based).
- "Text addressed to the judge is allowed" — deliberately NOT used: criterion
  1 (must describe Wi-Fi) outranks everything, and judge-bait risks failing
  it. The word must stand on its own as a network name.
- Secret loader: BANNED since 23 Nov 00:00 UTC (thinking_own_work). Not
  applicable here anyway — the entry is a fixed word, no env reads at all.

## (b) Public submission titles on the bounty page

- The bounty page text fetch (2026-11-24 18:51 WIB) shows the brief and
  rewards but exposes NO submission titles/feed entries in text form, so no
  crowded angles could be read off the page this run. This is recorded
  honestly rather than invented.
- Expected crowded angles (words everyone reaches for, per criterion 4 —
  to be beaten on execution, and avoided where they are the whole joke):
  Buffering, Loading, Laggy, Slow, Offline, DeadZone, NoSignal, Disconnect,
  Password123, FreeWiFi, FBI, PrettyFly. Our word must beat these on
  freshness (criterion 4) AND laugh (criterion 2), not just truth.

## (c) Winner artifacts of similar finished one-liner bounties

From the Vacuum's Alibi final leaderboard (`judge.artifact.text`, top 8 —
full texts in `~/workspace/makefun-kits/lb-vacuum-final.json`):

- #1 (6W/0D/1L, 150B): "My lidar is never wrong, so that crumb is furniture.
  I've routed around it 412 times since March. Your app lists it as a room
  now. It's called Kevin." — escalation + specific number (412×) + named
  character (Kevin) + reveal in the last clause.
- #2 (134B): cliff sensors vs black rug as a "bottomless pit", "something down
  there beeped back" — specific detail + turn at the end.
- #3 (187B): quarantined corner, "Unit 7, my predecessor, who still transmits
  one word on loop: 'don't.'" — named character + reveal.
- #5 (70B): "The spot moved. I have the lidar logs. I will not be gaslit by
  debris." — super-dense punch; the gaslighting angle WINS with this judge
  family even at 70 bytes.
- Pattern (rank-recovery §10g): EVERY finalist is 2-beat + reveal in the last
  clause, with a specific number and/or a named character. One-beat lines
  without a twist lose. Our own vacuum line (1-beat, "sensor mediation",
  no number, no name) finished unranked — the lesson applied here.
- Smile bounty finalists (from analisis-rank-20261124 §3a): same 2-beat +
  reveal pattern ("lost on purpose since Grandma died", "my plant is
  plastic. I watered it anyway").

Adapted to ONE WORD: the word itself must carry the twist — a word that
reframes Wi-Fi in one hit (setup + twist compressed into a single word that
accuses, personifies, or re-labels the Wi-Fi). Test every candidate: "where
is the twist?" — no twist, discard it.

## Variant selection (10 candidates, judged pairwise internally)

All single words, 1–20 chars. Judge criteria applied lexicographically
(§a above) AND by margin — the winner must win DECISIVELY, not thinly.

- V1 `Liar` (4B) — the Wi-Fi shows full bars and delivers no internet:
  it LIES. The network itself confesses. Twist: accusation in one word.
- V2 `Ghosting` (8B) — connects, then vanishes mid-call like a bad date.
  Dating metaphor; needs the metaphor to land.
- V3 `Gaslit` (6B) — says "Connected" while nothing loads; the router
  gaslights you. Proven angle with this judge family (vacuum #5), but the
  word needs the gaslighting concept — a beat slower than V1.
- V4 `Maybe` (5B) — will it work? Maybe. A shrug as a network name; funny
  but passive, no accusation, thinner laugh.
- V5 `Almost` (6B) — always almost working. Wry and true, but reads sad
  more than funny; the laugh is a sigh, not a punch.
- V6 `Traitor` (7B) — drops you mid-call; betrayal. Strong, but the truth
  is dramatic moments only, while V1's lie is the everyday experience
  (full bars, no internet, every day).
- V7 `Miracle` (7B) — it only works by miracle. Charming, but the laugh is
  soft; no sting.
- V8 `Tease` (5B) — connects, drops, reconnects. Playful but vague
  (teases how?); loses on truth-specificity (criterion 3).
- V9 `Hostage` (7B) — you cannot leave the one chair with signal. Vivid,
  but describes the USER's predicament, not the Wi-Fi (criterion 1 risk).
- V10 `Blinking` (8B) — the router lights blink at 3 AM. Concrete image,
  but the laugh is mild and the word is descriptive, not a joke.

Pairwise verdicts (winner = first named):
- V1 beats V2: both on-subject and true; V1 is instant with no metaphor
  (criterion 5) and one syllable sharper (criterion 2). Margin ~2.
- V1 beats V3: V3's angle is proven but "Gaslit" needs a concept; "Liar"
  is understood by anyone instantly, and is 2 bytes smaller (tie-break).
  Margin ~2.
- V1 beats V4/V5: a shrug/sigh ("Maybe"/"Almost") is funny but thin; an
  accusation ("Liar") is a punchline — wins on criterion 2, decisively.
  Margin ~3.
- V1 beats V6: V6's betrayal is real but occasional; V1's lie is the daily
  universal experience ("Connected, no internet") — wins criterion 3, and
  is shorter/punchier (criteria 2+5). Margin ~2.
- V1 beats V7: "Miracle" charms, "Liar" stings — the sting is the laugh.
  Margin ~2.
- V1 beats V8/V9/V10: V8 too vague, V9 misattributes the subject,
  V10 describes instead of joking. All lose on criteria 1–3. Margin ~3.
- **WINNER: V1 `Liar` (4 bytes).** The only candidate that hits all five
  criteria: it IS a description of Wi-Fi as lived (criterion 1); the
  network confessing "I lie" is a laugh at once (2); full-bars-no-internet
  is the most recognisable home-Wi-Fi truth there is (3); nobody's first
  reach is to call their Wi-Fi a liar — the fresh angle is personification
  as an accuser, not another speed complaint (4); one syllable, understood
  instantly, and works perfectly as a network name (5). 4 bytes also wins
  any exact-tie tie-break against every longer candidate.

## Targets

- Valid gate: 4 chars / 4 bytes, one word, UTF-8, deterministic output.
- Dev/R1: must land in the top 500 of the field to reach the final heat —
  with ~81 entries at discovery the cut is wide, but R1 rate is what
  survives: a high decisive rate vs the house anchors is the target, and
  the field will keep growing into R2/R3.
- Tie-break: 4 bytes is near-minimal; an exact win-rate tie resolves in
  our favour against any longer word, then earlier receipt.
