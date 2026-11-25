# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/ahmed1813544/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/ahmed1813544/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for [The 3AM Fridge Text](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
on make.fun: a program that writes the one line a smart fridge
texts its owner at 3am to `/output/entry.txt`.

## The line

> 3am. You've opened me four times tonight. Nothing new has appeared. Go to bed.

## How it works

`main.py` (stdlib-only Python) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
The output is a single line of 78 characters — well inside the
competition's 1–140 character gate. The program is deterministic:
repeated runs produce byte-identical output.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
