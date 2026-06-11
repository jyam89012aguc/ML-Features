# f10_candle_sequence_patterns_base_001_075_gemini.py
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

def f10csp_green_streak_ratio_3d_v001_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of green candles over 3 days."""
    res = _color_streak_ratio(open, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_green_streak_ratio_5d_v002_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of green candles over 5 days."""
    res = _color_streak_ratio(open, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_green_streak_ratio_10d_v003_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of green candles over 10 days."""
    res = _color_streak_ratio(open, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_green_streak_ratio_21d_v004_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of green candles over 21 days."""
    res = _color_streak_ratio(open, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_green_streak_ratio_63d_v005_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of green candles over 63 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _color_streak_ratio(open * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_green_streak_ratio_126d_v006_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of green candles over 126 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _color_streak_ratio(open * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_green_streak_ratio_252d_v007_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of green candles over 252 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _color_streak_ratio(open * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_3d_v008_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of red candles over 3 days."""
    res = 1.0 - _color_streak_ratio(open, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_5d_v009_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of red candles over 5 days."""
    res = 1.0 - _color_streak_ratio(open, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_10d_v010_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of red candles over 10 days."""
    res = 1.0 - _color_streak_ratio(open, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_21d_v011_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of red candles over 21 days."""
    res = 1.0 - _color_streak_ratio(open, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_63d_v012_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of red candles over 63 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = 1.0 - _color_streak_ratio(open * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_126d_v013_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of red candles over 126 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = 1.0 - _color_streak_ratio(open * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_red_streak_ratio_252d_v014_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Ratio of red candles over 252 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = 1.0 - _color_streak_ratio(open * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_3d_v015_signal(close: pd.Series) -> pd.Series:
    """Frequency of higher closes over 3 days."""
    res = _higher_move_streak(close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_5d_v016_signal(close: pd.Series) -> pd.Series:
    """Frequency of higher closes over 5 days."""
    res = _higher_move_streak(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_10d_v017_signal(close: pd.Series) -> pd.Series:
    """Frequency of higher closes over 10 days."""
    res = _higher_move_streak(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_21d_v018_signal(close: pd.Series) -> pd.Series:
    """Frequency of higher closes over 21 days."""
    res = _higher_move_streak(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_63d_v019_signal(closeadj: pd.Series) -> pd.Series:
    """Frequency of higher closes over 63 days with adjusted close."""
    res = _higher_move_streak(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_126d_v020_signal(closeadj: pd.Series) -> pd.Series:
    """Frequency of higher closes over 126 days with adjusted close."""
    res = _higher_move_streak(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_higher_move_streak_252d_v021_signal(closeadj: pd.Series) -> pd.Series:
    """Frequency of higher closes over 252 days with adjusted close."""
    res = _higher_move_streak(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_3d_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 3 days."""
    res = _pattern_occurrence_rate(open, high, low, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_5d_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 5 days."""
    res = _pattern_occurrence_rate(open, high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_10d_v024_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 10 days."""
    res = _pattern_occurrence_rate(open, high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_21d_v025_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 21 days."""
    res = _pattern_occurrence_rate(open, high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_63d_v026_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 63 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _pattern_occurrence_rate(open * adj, high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_126d_v027_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 126 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _pattern_occurrence_rate(open * adj, high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10csp_hhhl_persistence_252d_v028_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Frequency of HH/HL over 252 days with adjusted prices."""
    adj = closeadj / close.replace(0, np.nan)
    res = _pattern_occurrence_rate(open * adj, high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

















































SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}
BASE_NAMES = [f for f in globals() if f.startswith("f10csp_") and f.endswith("_signal")]
F10_CANDLE_SEQUENCE_PATTERNS_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE, "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN, "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}
if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({"open": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+105, "low": np.random.randn(sz).cumsum()+95, "close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F10_CANDLE_SEQUENCE_PATTERNS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]}); assert isinstance(r, pd.Series)
    print("base 001-075 OK")
