# Exercise 01: Trades → 1-minute candles

Every trading chart you've seen is built from this function. DataPulse will need it in Phase 1.

## The task

You get a list of trades. Each trade is a tuple `(timestamp, price, qty)`:
- `timestamp`: int, seconds since epoch
- `price`: float
- `qty`: float

Return a list of 1-minute **candles** (OHLCV), oldest first. Each candle is a dict:

```python
{"start": 60, "open": 99.0, "high": 99.0, "low": 99.0, "close": 99.0, "volume": 1.0}
```

- `start`: the minute's start timestamp (a multiple of 60)
- `open`: price of the first trade in that minute
- `high` / `low`: max / min price in that minute
- `close`: price of the last trade in that minute
- `volume`: sum of qty in that minute

## Levels

**Level 1** (`build_candles`): trades arrive sorted by timestamp. Minutes with no trades are simply absent.

**Level 2** (`build_candles_filled`): same, but minutes with no trades between the first and last trade must appear as a "flat" candle: open/high/low/close all equal the previous candle's close, and volume is 0. Charts need this, or they get gaps.

**Level 3** (no tests, think about it and write your answer as a comment at the bottom of `candles.py`): real feeds deliver trades **out of order** and occasionally **duplicated**. What changes? What would you need from the exchange to detect a duplicate?

## How to do it

1. Follow the 5-step method in [PRACTICE.md](../../PRACTICE.md). Write the examples and comments **before** any code.
2. Only edit `candles.py`.
3. Run the tests from this folder:
   ```
   python test_candles.py
   ```
4. No AI autocomplete, no searching "python ohlc candles." Looking up Python syntax (e.g. "python integer division") is fine.
5. When it passes, do the refactor pass, then send it to me for review.

Hint, only if stuck for over 10 minutes: what does `timestamp // 60 * 60` give you?
