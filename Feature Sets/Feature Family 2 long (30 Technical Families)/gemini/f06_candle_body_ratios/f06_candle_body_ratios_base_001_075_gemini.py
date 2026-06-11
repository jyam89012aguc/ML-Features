# f06_candle_body_ratios_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _body_pct(o, h, l, c):
    return (c - o).abs() / (h - l).abs().replace(0, np.nan)

def _upper_wick_pct(o, h, l, c):
    body_top = np.maximum(o, c)
    return (h - body_top) / (h - l).abs().replace(0, np.nan)

def _lower_wick_pct(o, h, l, c):
    body_bot = np.minimum(o, c)
    return (body_bot - l) / (h - l).abs().replace(0, np.nan)

# Feature 1: Current Body Percentage
def f06cbr_f06_candle_body_ratios_body_pct_v001_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 2: SMA 5 of Body Percentage
def f06cbr_f06_candle_body_ratios_body_pct_sma_5d_v002_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 3: SMA 10 of Body Percentage
def f06cbr_f06_candle_body_ratios_body_pct_sma_10d_v003_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 4: SMA 21 of Body Percentage
def f06cbr_f06_candle_body_ratios_body_pct_sma_21d_v004_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 5: SMA 63 of Body Percentage
def f06cbr_f06_candle_body_ratios_body_pct_sma_63d_v005_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 6: Current Upper Wick Percentage
def f06cbr_f06_candle_body_ratios_upper_wick_pct_v006_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 7: SMA 5 of Upper Wick Percentage
def f06cbr_f06_candle_body_ratios_upper_wick_pct_sma_5d_v007_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 8: SMA 10 of Upper Wick Percentage
def f06cbr_f06_candle_body_ratios_upper_wick_pct_sma_10d_v008_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 9: SMA 21 of Upper Wick Percentage
def f06cbr_f06_candle_body_ratios_upper_wick_pct_sma_21d_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 10: SMA 63 of Upper Wick Percentage
def f06cbr_f06_candle_body_ratios_upper_wick_pct_sma_63d_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 11: Current Lower Wick Percentage
def f06cbr_f06_candle_body_ratios_lower_wick_pct_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _lower_wick_pct(open, high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 12: SMA 5 of Lower Wick Percentage
def f06cbr_f06_candle_body_ratios_lower_wick_pct_sma_5d_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 13: SMA 10 of Lower Wick Percentage
def f06cbr_f06_candle_body_ratios_lower_wick_pct_sma_10d_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 14: SMA 21 of Lower Wick Percentage
def f06cbr_f06_candle_body_ratios_lower_wick_pct_sma_21d_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 15: SMA 63 of Lower Wick Percentage
def f06cbr_f06_candle_body_ratios_lower_wick_pct_sma_63d_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_lower_wick_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 16: Current Total Wick Percentage
def f06cbr_f06_candle_body_ratios_total_wick_pct_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = 1 - _body_pct(open, high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 17: SMA 5 of Total Wick Percentage
def f06cbr_f06_candle_body_ratios_total_wick_pct_sma_5d_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 18: SMA 10 of Total Wick Percentage
def f06cbr_f06_candle_body_ratios_total_wick_pct_sma_10d_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 19: SMA 21 of Total Wick Percentage
def f06cbr_f06_candle_body_ratios_total_wick_pct_sma_21d_v019_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 20: SMA 63 of Total Wick Percentage
def f06cbr_f06_candle_body_ratios_total_wick_pct_sma_63d_v020_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(1 - _body_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 21: Body to Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_wick_ratio_v021_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    wick = 1 - body
    res = body / wick.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 22: SMA 5 of Body to Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_wick_ratio_sma_5d_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    wick = 1 - body
    res = _sma(body / wick.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 23: SMA 10 of Body to Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_wick_ratio_sma_10d_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    wick = 1 - body
    res = _sma(body / wick.replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 24: SMA 21 of Body to Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_wick_ratio_sma_21d_v024_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    wick = 1 - body
    res = _sma(body / wick.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 25: SMA 63 of Body to Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_wick_ratio_sma_63d_v025_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    wick = 1 - body
    res = _sma(body / wick.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 26: Upper to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_upper_to_lower_wick_ratio_v026_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 27: SMA 5 of Upper to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_upper_to_lower_wick_ratio_sma_5d_v027_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 28: SMA 10 of Upper to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_upper_to_lower_wick_ratio_sma_10d_v028_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 29: SMA 21 of Upper to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_upper_to_lower_wick_ratio_sma_21d_v029_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 30: SMA 63 of Upper to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_upper_to_lower_wick_ratio_sma_63d_v030_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_upper_wick_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 31: Body to Upper Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_upper_wick_ratio_v031_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close) / _upper_wick_pct(open, high, low, close).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 32: SMA 5 of Body to Upper Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_upper_wick_ratio_sma_5d_v032_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _upper_wick_pct(open, high, low, close).replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 33: SMA 10 of Body to Upper Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_upper_wick_ratio_sma_10d_v033_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _upper_wick_pct(open, high, low, close).replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 34: SMA 21 of Body to Upper Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_upper_wick_ratio_sma_21d_v034_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _upper_wick_pct(open, high, low, close).replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 35: SMA 63 of Body to Upper Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_upper_wick_ratio_sma_63d_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _upper_wick_pct(open, high, low, close).replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 36: Body to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_lower_wick_ratio_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _body_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 37: SMA 5 of Body to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_lower_wick_ratio_sma_5d_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 38: SMA 10 of Body to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_lower_wick_ratio_sma_10d_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 39: SMA 21 of Body to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_lower_wick_ratio_sma_21d_v039_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 40: SMA 63 of Body to Lower Wick Ratio
def f06cbr_f06_candle_body_ratios_body_to_lower_wick_ratio_sma_63d_v040_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma(_body_pct(open, high, low, close) / _lower_wick_pct(open, high, low, close).replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 41: Relative Body Size (current body / SMA 21 body)
def f06cbr_f06_candle_body_ratios_rel_body_size_v041_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = body_abs / _sma(body_abs, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 42: SMA 5 of Relative Body Size
def f06cbr_f06_candle_body_ratios_rel_body_size_sma_5d_v042_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = _sma(body_abs / _sma(body_abs, 21).replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 43: SMA 10 of Relative Body Size
def f06cbr_f06_candle_body_ratios_rel_body_size_sma_10d_v043_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = _sma(body_abs / _sma(body_abs, 21).replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 44: SMA 21 of Relative Body Size
def f06cbr_f06_candle_body_ratios_rel_body_size_sma_21d_v044_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = _sma(body_abs / _sma(body_abs, 21).replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 45: SMA 63 of Relative Body Size
def f06cbr_f06_candle_body_ratios_rel_body_size_sma_63d_v045_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = _sma(body_abs / _sma(body_abs, 21).replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 46: Relative Range Size (current range / SMA 21 range)
def f06cbr_f06_candle_body_ratios_rel_range_size_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 47: SMA 5 of Relative Range Size
def f06cbr_f06_candle_body_ratios_rel_range_size_sma_5d_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = _sma(range_abs / _sma(range_abs, 21).replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 48: SMA 10 of Relative Range Size
def f06cbr_f06_candle_body_ratios_rel_range_size_sma_10d_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = _sma(range_abs / _sma(range_abs, 21).replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 49: SMA 21 of Relative Range Size
def f06cbr_f06_candle_body_ratios_rel_range_size_sma_21d_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = _sma(range_abs / _sma(range_abs, 21).replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 50: SMA 63 of Relative Range Size
def f06cbr_f06_candle_body_ratios_rel_range_size_sma_63d_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    res = _sma(range_abs / _sma(range_abs, 21).replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 51: Doji Score (1 - body_pct)

# Feature 52: SMA 5 of Doji Score

# Feature 53: SMA 10 of Doji Score

# Feature 54: SMA 21 of Doji Score

# Feature 55: SMA 63 of Doji Score

# Feature 56: Hammer Score (lower wick / (body + upper wick))
def f06cbr_f06_candle_body_ratios_hammer_score_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = l_wick / (body + u_wick + 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 57: SMA 5 of Hammer Score
def f06cbr_f06_candle_body_ratios_hammer_score_sma_5d_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(l_wick / (body + u_wick + 0.01), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 58: SMA 10 of Hammer Score
def f06cbr_f06_candle_body_ratios_hammer_score_sma_10d_v058_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(l_wick / (body + u_wick + 0.01), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 59: SMA 21 of Hammer Score
def f06cbr_f06_candle_body_ratios_hammer_score_sma_21d_v059_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(l_wick / (body + u_wick + 0.01), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 60: SMA 63 of Hammer Score
def f06cbr_f06_candle_body_ratios_hammer_score_sma_63d_v060_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(l_wick / (body + u_wick + 0.01), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 61: Shooting Star Score (upper wick / (body + lower wick))
def f06cbr_f06_candle_body_ratios_shooting_star_score_v061_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = u_wick / (body + l_wick + 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 62: SMA 5 of Shooting Star Score
def f06cbr_f06_candle_body_ratios_shooting_star_score_sma_5d_v062_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(u_wick / (body + l_wick + 0.01), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 63: SMA 10 of Shooting Star Score
def f06cbr_f06_candle_body_ratios_shooting_star_score_sma_10d_v063_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(u_wick / (body + l_wick + 0.01), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 64: SMA 21 of Shooting Star Score
def f06cbr_f06_candle_body_ratios_shooting_star_score_sma_21d_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(u_wick / (body + l_wick + 0.01), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 65: SMA 63 of Shooting Star Score
def f06cbr_f06_candle_body_ratios_shooting_star_score_sma_63d_v065_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _sma(u_wick / (body + l_wick + 0.01), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 66: Marubozu Score (body_pct) - EMA 5
def f06cbr_f06_candle_body_ratios_marubozu_score_ema_5d_v066_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_body_pct(open, high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 67: Marubozu Score (body_pct) - EMA 10
def f06cbr_f06_candle_body_ratios_marubozu_score_ema_10d_v067_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_body_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 68: Marubozu Score (body_pct) - EMA 21
def f06cbr_f06_candle_body_ratios_marubozu_score_ema_21d_v068_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_body_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 69: Marubozu Score (body_pct) - EMA 63
def f06cbr_f06_candle_body_ratios_marubozu_score_ema_63d_v069_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(_body_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 70: Body Directionality (Close - Open) / (High - Low)
def f06cbr_f06_candle_body_ratios_body_dir_v070_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = (close - open) / (high - low).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 71: SMA 5 of Body Directionality
def f06cbr_f06_candle_body_ratios_body_dir_sma_5d_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 72: SMA 10 of Body Directionality
def f06cbr_f06_candle_body_ratios_body_dir_sma_10d_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 73: SMA 21 of Body Directionality
def f06cbr_f06_candle_body_ratios_body_dir_sma_21d_v073_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 74: SMA 63 of Body Directionality
def f06cbr_f06_candle_body_ratios_body_dir_sma_63d_v074_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 75: Wick Balance (Upper Wick % - Lower Wick %)
def f06cbr_f06_candle_body_ratios_wick_balance_v075_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f06cbr_") and f.endswith("_signal")]

F06_CANDLE_BODY_RATIOS_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
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
    # Ensure high is highest and low is lowest
    d["high"] = d[["open", "close", "high"]].max(axis=1) + 1
    d["low"] = d[["open", "close", "low"]].min(axis=1) - 1
    
    for n, c in F06_CANDLE_BODY_RATIOS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
