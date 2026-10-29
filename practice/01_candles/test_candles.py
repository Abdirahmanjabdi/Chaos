"""Run with: python test_candles.py"""

from candles import build_candles, build_candles_filled


def candle(start, o, h, l, c, v):
    return {"start": start, "open": o, "high": h, "low": l, "close": c, "volume": v}


def expect(got, want):
    if got != want:
        raise AssertionError(f"\n        got:  {got}\n        want: {want}")


# ---------- Level 1 ----------

def test_empty():
    expect(build_candles([]), [])


def test_single_trade():
    expect(build_candles([(5, 100.0, 2.0)]), [candle(0, 100.0, 100.0, 100.0, 100.0, 2.0)])


def test_one_minute_many_trades():
    trades = [(0, 100.0, 1.0), (10, 103.0, 1.0), (20, 98.0, 2.0), (59, 101.0, 0.5)]
    expect(build_candles(trades), [candle(0, 100.0, 103.0, 98.0, 101.0, 4.5)])


def test_two_minutes():
    trades = [(0, 100.0, 1.0), (30, 101.0, 2.0), (65, 99.0, 1.0)]
    expect(build_candles(trades), [
        candle(0, 100.0, 101.0, 100.0, 101.0, 3.0),
        candle(60, 99.0, 99.0, 99.0, 99.0, 1.0),
    ])


def test_minute_boundary_belongs_to_next_minute():
    trades = [(59, 100.0, 1.0), (60, 200.0, 1.0)]
    expect(build_candles(trades), [
        candle(0, 100.0, 100.0, 100.0, 100.0, 1.0),
        candle(60, 200.0, 200.0, 200.0, 200.0, 1.0),
    ])


def test_gap_minutes_are_absent():
    trades = [(0, 100.0, 1.0), (185, 110.0, 1.0)]
    expect(build_candles(trades), [
        candle(0, 100.0, 100.0, 100.0, 100.0, 1.0),
        candle(180, 110.0, 110.0, 110.0, 110.0, 1.0),
    ])


def test_realistic_timestamps():
    t = 1_760_000_000  # a real epoch second, 20s into its minute
    trades = [(t, 50_000.0, 0.5), (t + 1, 50_010.0, 0.25), (t + 30, 49_990.0, 0.25)]
    expect(build_candles(trades), [
        candle(t - 20, 50_000.0, 50_010.0, 49_990.0, 49_990.0, 1.0),
    ])


# ---------- Level 2 ----------

def test_filled_empty():
    expect(build_candles_filled([]), [])


def test_filled_no_gaps_is_same_as_level_1():
    trades = [(0, 100.0, 1.0), (30, 101.0, 2.0), (65, 99.0, 1.0)]
    expect(build_candles_filled(trades), [
        candle(0, 100.0, 101.0, 100.0, 101.0, 3.0),
        candle(60, 99.0, 99.0, 99.0, 99.0, 1.0),
    ])


def test_filled_gap_uses_previous_close():
    trades = [(0, 100.0, 1.0), (10, 105.0, 1.0), (185, 110.0, 1.0)]
    expect(build_candles_filled(trades), [
        candle(0, 100.0, 105.0, 100.0, 105.0, 2.0),
        candle(60, 105.0, 105.0, 105.0, 105.0, 0),
        candle(120, 105.0, 105.0, 105.0, 105.0, 0),
        candle(180, 110.0, 110.0, 110.0, 110.0, 1.0),
    ])


# ---------- runner ----------

if __name__ == "__main__":
    tests = [(name, fn) for name, fn in list(globals().items()) if name.startswith("test_")]
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except Exception as e:
            print(f"FAIL  {name}")
            print(f"      {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(tests)} passed")
