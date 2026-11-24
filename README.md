# Type Faster This Time

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Jr-kenny/type-faster-this-time/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Jr-kenny/type-faster-this-time/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One honest error message for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) competition on make.fun.

## The line

> Your session expired while you were thinking, and the form took your answers with it. Log in again, and type faster this time.

126 characters, one line, no apology in generalities. It names the real failure (the session timed out and the form data went with it), tells the user exactly what to do next (log in again), and lands the joke on a single read.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt`, deterministically, with no network and no randomness.

## License

MIT. See [LICENSE](LICENSE).
