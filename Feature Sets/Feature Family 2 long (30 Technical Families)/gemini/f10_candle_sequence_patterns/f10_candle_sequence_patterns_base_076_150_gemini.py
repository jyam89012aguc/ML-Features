# f10_candle_sequence_patterns_base_076_150_gemini.py
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

def f10csp_base_variation_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 76 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 18)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v077_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 77 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 19)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 78 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 20)
    return res.replace([np.inf, -np.inf], np.nan)


def f10csp_base_variation_v080_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 80 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v081_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 81 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v082_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 82 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v083_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 83 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 25)
    return res.replace([np.inf, -np.inf], np.nan)


def f10csp_base_variation_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 85 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 6)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 86 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 7)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 87 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v088_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 88 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 9)
    return res.replace([np.inf, -np.inf], np.nan)


def f10csp_base_variation_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 90 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 11)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v091_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 91 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 12)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v092_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 92 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 13)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v093_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 93 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v094_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 94 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v095_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 95 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 16)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_base_variation_v096_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Base feature variation 96 using pattern rate."""
    res = _pattern_occurrence_rate(open, high, low, close, 17)
    return res.replace([np.inf, -np.inf], np.nan)
























































SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}
BASE_NAMES = [f for f in globals() if f.startswith("f10csp_") and f.endswith("_signal")]
F10_CANDLE_SEQUENCE_PATTERNS_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE, "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN, "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}
if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({"open": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+105, "low": np.random.randn(sz).cumsum()+95, "close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F10_CANDLE_SEQUENCE_PATTERNS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]}); assert isinstance(r, pd.Series)
    print("base 076-150 OK")
