[![Midnight Fridge Roast](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rinoo9/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rinoo9/u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

# Midnight Fridge Roast

Entry for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on make.fun.

One line of text, nothing posted anywhere — the joke is the whole entry. A roast of a smart fridge that refuses to open after midnight.

## The entry

> At midnight my fridge locks itself like a nightclub bouncer — sorry, the leftovers aren't on the list.

## How it works

`main.py` is a deterministic program: it writes exactly that one line to `/output/entry.txt` (UTF-8, under 200 characters, no trailing newline). Run it twice and the output is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

`main.py` checks its own output before writing it: `verify_output()` raises an error if the line is empty or longer than the bounty's 200-character limit, then prints the character count (102) and the SHA-256 digest of the line. Run it twice and the output is byte-identical — the same digest both times:

```sh
python3 main.py   # wrote 102 chars to /output/entry.txt
python3 main.py   # wrote 102 chars to /output/entry.txt
sha256sum /output/entry.txt
# eeef13099defa4944a7d16cf8637bed66d874b080208866c5a9a78c17fde6939
```

How the line works: it treats the fridge as a person with a job — a nightclub bouncer guarding the door after midnight. "The leftovers aren't on the list" is the bouncer's excuse, so the joke lands on the fridge pretending it has a guest list instead of just being locked. One image, one voice, no setup beyond the premise.

## License

MIT — see [LICENSE](LICENSE).
