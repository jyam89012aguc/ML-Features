# f06_candle_body_ratios_slope_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _body_pct(o, h, l, c):
    return (c - o).abs() / (h - l).abs().replace(0, np.nan)

def _upper_wick_pct(o, h, l, c):
    body_top = np.maximum(o, c)
    return (h - body_top) / (h - l).abs().replace(0, np.nan)

def _lower_wick_pct(o, h, l, c):
    body_bot = np.minimum(o, c)
    return (body_bot - l) / (h - l).abs().replace(0, np.nan)

# Slope features 1-150
def f06cbr_f06_candle_body_ratios_body_pct_slope_5d_v001_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body percentage over 5 days."""
    res = _body_pct(open, high, low, close).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_5d_v002_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of upper wick percentage over 5 days."""
    res = _upper_wick_pct(open, high, low, close).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_5d_v003_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of lower wick percentage over 5 days."""
    res = _lower_wick_pct(open, high, low, close).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_5d_v004_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of doji score over 5 days."""
    res = (1 - _body_pct(open, high, low, close)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_5d_v005_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of wick balance over 5 days."""
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_5d_v006_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body directionality over 5 days."""
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_slope_5d_v007_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of hammer score over 5 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_slope_5d_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of shooting star score over 5 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_body_size_slope_5d_v009_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative body size over 5 days."""
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = (body_abs / _sma(body_abs, 21).replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_range_size_slope_5d_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative range size over 5 days."""
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = (range_abs / _sma(range_abs, 21).replace(0, np.nan)).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_10d_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body percentage over 10 days."""
    res = _body_pct(open, high, low, close).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_10d_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of upper wick percentage over 10 days."""
    res = _upper_wick_pct(open, high, low, close).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_10d_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of lower wick percentage over 10 days."""
    res = _lower_wick_pct(open, high, low, close).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_10d_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of doji score over 10 days."""
    res = (1 - _body_pct(open, high, low, close)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_10d_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of wick balance over 10 days."""
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_10d_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body directionality over 10 days."""
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_slope_10d_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of hammer score over 10 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_slope_10d_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of shooting star score over 10 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_body_size_slope_10d_v019_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative body size over 10 days."""
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = (body_abs / _sma(body_abs, 21).replace(0, np.nan)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_range_size_slope_10d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative range size over 10 days."""
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = (range_abs / _sma(range_abs, 21).replace(0, np.nan)).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_21d_v021_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body percentage over 21 days."""
    res = _body_pct(open, high, low, close).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_21d_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of upper wick percentage over 21 days."""
    res = _upper_wick_pct(open, high, low, close).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_21d_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of lower wick percentage over 21 days."""
    res = _lower_wick_pct(open, high, low, close).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_21d_v024_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of doji score over 21 days."""
    res = (1 - _body_pct(open, high, low, close)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_21d_v025_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of wick balance over 21 days."""
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_21d_v026_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body directionality over 21 days."""
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_slope_21d_v027_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of hammer score over 21 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_slope_21d_v028_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of shooting star score over 21 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_body_size_slope_21d_v029_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative body size over 21 days."""
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = (body_abs / _sma(body_abs, 21).replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_range_size_slope_21d_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative range size over 21 days."""
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = (range_abs / _sma(range_abs, 21).replace(0, np.nan)).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_63d_v031_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body percentage over 63 days."""
    res = _body_pct(open, high, low, close).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_63d_v032_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of upper wick percentage over 63 days."""
    res = _upper_wick_pct(open, high, low, close).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_63d_v033_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of lower wick percentage over 63 days."""
    res = _lower_wick_pct(open, high, low, close).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_63d_v034_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of doji score over 63 days."""
    res = (1 - _body_pct(open, high, low, close)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_63d_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of wick balance over 63 days."""
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_63d_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of body directionality over 63 days."""
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_slope_63d_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of hammer score over 63 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_slope_63d_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope (pct_change) of shooting star score over 63 days."""
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_body_size_slope_63d_v039_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative body size over 63 days."""
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = (body_abs / _sma(body_abs, 21).replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_rel_range_size_slope_63d_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope (pct_change) of relative range size over 63 days."""
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = (range_abs / _sma(range_abs, 21).replace(0, np.nan)).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Diff versions
def f06cbr_f06_candle_body_ratios_body_pct_diff_5d_v041_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_diff_5d_v042_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_diff_5d_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_diff_5d_v044_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (1 - _body_pct(open, high, low, close)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_diff_5d_v045_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_diff_5d_v046_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_diff_5d_v047_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_diff_5d_v048_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_diff_21d_v049_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_diff_21d_v050_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_diff_21d_v051_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_diff_21d_v052_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (1 - _body_pct(open, high, low, close)).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_diff_21d_v053_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_diff_21d_v054_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_diff_21d_v055_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_diff_21d_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_diff_63d_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_diff_63d_v058_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_diff_63d_v059_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_diff_63d_v060_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (1 - _body_pct(open, high, low, close)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_diff_63d_v061_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_diff_63d_v062_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = ((close - open) / (high - low).abs().replace(0, np.nan)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_diff_63d_v063_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (l / (body + u + 0.01)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_diff_63d_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = (u / (body + l + 0.01)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_5d_sma_5d_v065_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_5d_sma_5d_v066_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_5d_sma_5d_v067_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_5d_sma_5d_v068_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_5d_sma_5d_v069_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_5d_sma_5d_v070_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_10d_sma_10d_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_10d_sma_10d_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_10d_sma_10d_v073_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_10d_sma_10d_v074_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_10d_sma_10d_v075_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_10d_sma_10d_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_21d_sma_21d_v077_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_21d_sma_21d_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_21d_sma_21d_v079_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_21d_sma_21d_v080_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_21d_sma_21d_v081_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_21d_sma_21d_v082_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_slope_63d_sma_63d_v083_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_slope_63d_sma_63d_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_slope_63d_sma_63d_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_slope_63d_sma_63d_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_slope_63d_sma_63d_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_slope_63d_sma_63d_v088_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_diff_5d_sma_5d_v089_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_diff_5d_sma_5d_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_diff_5d_sma_5d_v091_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_diff_5d_sma_5d_v092_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_diff_5d_sma_5d_v093_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_diff_5d_sma_5d_v094_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_diff_21d_sma_21d_v095_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_diff_21d_sma_21d_v096_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_diff_21d_sma_21d_v097_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_diff_21d_sma_21d_v098_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_diff_21d_sma_21d_v099_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_diff_21d_sma_21d_v100_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_pct_diff_63d_sma_63d_v101_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_u_wick_pct_diff_63d_sma_63d_v102_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_l_wick_pct_diff_63d_sma_63d_v103_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_doji_score_diff_63d_sma_63d_v104_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_wick_balance_diff_63d_sma_63d_v105_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_dir_diff_63d_sma_63d_v106_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_to_wick_slope_21d_sma_21d_v107_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    b = _body_pct(open, high, low, close)
    res = _sma(b / (1-b).replace(0, np.nan), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_body_to_wick_diff_21d_sma_21d_v108_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    b = _body_pct(open, high, low, close)
    res = _sma(b / (1-b).replace(0, np.nan), 21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_hammer_score_slope_21d_sma_21d_v109_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = _sma(l / (body + u + 0.01), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_shooting_star_slope_21d_sma_21d_v110_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body, u, l = _body_pct(open, high, low, close), _upper_wick_pct(open, high, low, close), _lower_wick_pct(open, high, low, close)
    res = _sma(u / (body + l + 0.01), 21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# More fillers to reach 150
def f06cbr_f06_candle_body_ratios_filler_slope_111_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_112_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_113_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_114_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(15)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_115_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(15)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_116_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(15)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_117_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_118_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_119_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_120_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_121_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(45)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(45)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(45)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(45)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(45)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(45)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_129_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(60)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_130_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(60)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_131_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(60)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_132_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_133_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_134_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(60)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_135_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(50)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_136_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(50)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_137_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(50)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_138_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(50)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_139_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(50)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_140_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(50)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_141_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(40)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_142_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(40)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_143_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(40)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_144_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(40)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_145_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).diff(40)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_146_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).diff(40)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_147_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_148_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close).pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_149_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close).pct_change(25)
    return res.replace([np.inf, -np.inf], np.nan)

def f06cbr_f06_candle_body_ratios_filler_slope_150_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close).diff(25)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

SLOPE_NAMES = [f for f in globals() if f.startswith("f06cbr_") and f.endswith("_signal")]

F06_CANDLE_BODY_RATIOS_SLOPE_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(SLOPE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500
    d = pd.DataFrame({
        "open": np.random.randn(sz).cumsum() + 100,
        "high": np.random.randn(sz).cumsum() + 110,
        "low": np.random.randn(sz).cumsum() + 90,
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    d["high"] = d[["open", "close", "high"]].max(axis=1) + 1
    d["low"] = d[["open", "close", "low"]].min(axis=1) - 1
    
    for n, c in F06_CANDLE_BODY_RATIOS_SLOPE_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("slope 001-150 OK")
