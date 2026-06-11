# f10_candle_sequence_patterns_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _color_streak_ratio(o: pd.Series, c: pd.Series, w: int) -> pd.Series:
    """Calculates the ratio of green candles within a rolling window."""
    is_green = (c > o).astype(float)
    return is_green.rolling(w, min_periods=min(w, 5)).mean()

def _higher_move_streak(c: pd.Series, w: int) -> pd.Series:
    """Calculates the frequency of periods where the close price is higher than the previous close."""
    up = (c > c.shift(1)).astype(float)
    return up.rolling(w, min_periods=min(w, 5)).sum() / w

def _pattern_occurrence_rate(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series, w: int) -> pd.Series:
    """Calculates the frequency of a generic pattern match within a rolling window."""
    pattern = ((h > h.shift(1)) & (l > l.shift(1))).astype(float)
    return pattern.rolling(w, min_periods=min(w, 5)).mean()

def f10csp_jerk_v001_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 6)."""
    res = _pattern_occurrence_rate(open, high, low, close, 6).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v002_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 7)."""
    res = _pattern_occurrence_rate(open, high, low, close, 7).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v003_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 8)."""
    res = _pattern_occurrence_rate(open, high, low, close, 8).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v004_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 9)."""
    res = _pattern_occurrence_rate(open, high, low, close, 9).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v005_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 10)."""
    res = _pattern_occurrence_rate(open, high, low, close, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v006_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 11)."""
    res = _pattern_occurrence_rate(open, high, low, close, 11).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v007_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 12)."""
    res = _pattern_occurrence_rate(open, high, low, close, 12).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 13)."""
    res = _pattern_occurrence_rate(open, high, low, close, 13).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 14)."""
    res = _pattern_occurrence_rate(open, high, low, close, 14).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 15)."""
    res = _pattern_occurrence_rate(open, high, low, close, 15).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 16)."""
    res = _pattern_occurrence_rate(open, high, low, close, 16).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 17)."""
    res = _pattern_occurrence_rate(open, high, low, close, 17).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 18)."""
    res = _pattern_occurrence_rate(open, high, low, close, 18).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 19)."""
    res = _pattern_occurrence_rate(open, high, low, close, 19).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 20)."""
    res = _pattern_occurrence_rate(open, high, low, close, 20).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 21)."""
    res = _pattern_occurrence_rate(open, high, low, close, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 22)."""
    res = _pattern_occurrence_rate(open, high, low, close, 22).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 23)."""
    res = _pattern_occurrence_rate(open, high, low, close, 23).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v019_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 24)."""
    res = _pattern_occurrence_rate(open, high, low, close, 24).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v020_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 25)."""
    res = _pattern_occurrence_rate(open, high, low, close, 25).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_jerk_v021_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Jerk (2nd derivative) of pattern frequency (window 5)."""
    res = _pattern_occurrence_rate(open, high, low, close, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)



































































































































SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}
JERK_NAMES = [f for f in globals() if f.startswith("f10csp_") and f.endswith("_signal")]
F10_CANDLE_SEQUENCE_PATTERNS_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE, "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN, "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}
if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({"open": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+105, "low": np.random.randn(sz).cumsum()+95, "close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F10_CANDLE_SEQUENCE_PATTERNS_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]}); assert isinstance(r, pd.Series)
    print("jerk OK")
