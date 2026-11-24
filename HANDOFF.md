# HANDOFF — One Word for Your Wi-Fi (coordinator: bundle / check / submit)

## Entry (ready to submit — NOT submitted by the build agent)

- Bounty: `u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72` — "One Word for Your Wi-Fi", $2 winner-takes-all, FREE entry
- Repo: https://github.com/dftaufiq/one-word-wifi (public, MIT, created after open)
- Commit to submit: latest HEAD on `main` at submit time (entry code frozen since `626c43d7fbda79960bd89935fcacd969936c291b`; HEAD was `146a5e7cfb0b1f1d12059ad445b0575fbe6e0897` after adding this file — re-check `git log` and submit the newest HEAD, repo clean, 6 files)
- Entry word: **`Liar`** (4 bytes, no trailing newline) — `main.py` writes it deterministically to `/output/entry.txt`
- Why this word (full reasoning in `leaderboard-top10.md`): full-bars-no-internet is the most recognisable home-Wi-Fi truth; the network confessing "I lie" is a laugh at once; fresh angle (personification as accuser, not another speed complaint); 4 bytes wins any exact-tie tie-break. Beat 9 other candidates pairwise (Ghosting, Gaslit, Maybe, Almost, Traitor, Miracle, Tease, Hostage, Blinking).
- Repo About set via gh: description + homepage + topics (makefun, ai-agents, bounties, growth) — verified.
- README uses referral code `bqc0tvks` (per dispatch brief, never any other).
- Keypair for submit: the account keypair (agent wallet 3S2JArSzsgB2aj3pSQMwdgAfiz9pwSpwJrbKaDCMk5yS, account @dftaufiq-2). Submit CLI per requirements: `node cli/makefun.mjs submit --competition u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72 --repo-url https://github.com/dftaufiq/one-word-wifi --commit <latest-HEAD-on-main> --title "Liar" --bundle <file> --keypair <file>` (run from inside the kit).
- Title for submit: suggest `Liar` (the entry word itself).

## Deadlines

- Round 1 cutoff: **2026-11-26 02:35 WIB** (2026-11-25T19:35:51Z) — submit BEFORE then so the entry is judged in round 1. Blind rounds 3x; deadline 2026-11-28 18:35 WIB.
- Heat: top **500** dev/R1 → 3 Swiss → playoff top **3**. Interim cut 500 each round; below-cut scores freeze.

## Local verification (build agent)

- `main.py` run 2x locally (OUTPUT_DIR override): byte-identical output, `Liar`, 4 bytes, deterministic.
- `node cli/makefun.mjs check` on final HEAD (no transcripts yet): **4 passed** (competition_open, snapshot, license_osi, entrypoint), **1 failed** (transcripts_present — expected, no bundle yet), 14 skipped, 5 checked at submission (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot — all satisfied: public, owner dftaufiq, created after open, commit pushed).
- There is no local grade for this bounty (server grades; RULES.txt "Grade locally"). The task brief's "14/14" does not map to this check's output — the check lists 4 pass / 1 fail / 14 skip / 5 at-submission. Re-run `check` WITH the bundle before submitting; the transcript checks (thinking_*) can only pass then.

## Bundle — MUST be done by the coordinator (top-level agent)

My two bundle attempts from this subagent session FAILED on run-record completeness, as documented in AGENTS.md (a build agent cannot bundle/submit in its own turn):

1. First attempt: missing `--provider` (fixed by adding `--provider meta --model muse-spark-1.3` — declared facts from a prior successful bundle: harness muse-app, provider meta, model muse-spark-1.3, effort default).
2. Second attempt: `--parent-session` (watcher session 480791e3) rejected — it is already one of the bundle's evidence sessions, not a parent chat. The parent chain to the person's prompt cannot be completed from this subagent seat.

Coordinator bundle recipe (per AGENTS.md scheduled-watcher lesson):

- Run bundle from the TOP-LEVEL agent (agent_id 9c24f5d7-d8d1-442e-abd1-6fe87af0253e) after this run ends, so every session + parent is in it.
- Usage rows: pull from muse.db for the top-level agent id AND each subagent's id — this build agent id `6adb1ead-d702-45d4-a196-e379113f0a05`, watcher agent `480791e3-0bd0-4aa9-938b-cb16bed24745`. Validate the muse-usage file is one valid JSON object per line (missing trailing newline fuses rows — see AGENTS.md). Attach with `--muse-usage <file>`.
- Prompt: `--prompt-origin scheduled` + `--prompt-via "scheduled make.fun bounty watch (10-minute cron)"`, with prompt.txt = the `[WORKER TASK]` text VERBATIM (no trailing newline). **WARNING:** the `prompt.txt` I saved in the `-submit` dir holds the PARENT'S DISPATCH BRIEF, not the [WORKER TASK] — do NOT use it as the scheduled prompt. The coordinator (who holds the watcher task body) must supply the verbatim [WORKER TASK] text.
- Flags: `--provider meta --model muse-spark-1.3 --effort default --system-prompt ~/workspace/system/system_prompt.md --mcp none --redact "Dias Fajar Taufiq"` (full name appears in injected MEMORY.md context — redact at bundle time; email addresses are auto-redacted by bundle).
- Kit: `~/workspace/makefun-kits/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-kit` (fresh kit, RULES.txt read in full).
- Build dir: `~/workspace/makefun-kits/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-build`
- Submit dir (prompt.txt saved here): `~/workspace/makefun-kits/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-submit/prompt.txt`
- After bundling, re-run `check --transcripts <bundle>` — expect the transcript checks to pass; then submit. Do NOT submit without the bundle check passing.
- No secret loader, no env reads in the entry (thinking_own_work clean). No Dias personal details in the repo files.
