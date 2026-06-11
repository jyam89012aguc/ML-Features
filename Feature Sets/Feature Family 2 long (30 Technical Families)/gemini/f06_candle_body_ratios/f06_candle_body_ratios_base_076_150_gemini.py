# f06_candle_body_ratios_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _zscore(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _body_pct(o, h, l, c):
    return (c - o).abs() / (h - l).abs().replace(0, np.nan)

def _upper_wick_pct(o, h, l, c):
    body_top = np.maximum(o, c)
    return (h - body_top) / (h - l).abs().replace(0, np.nan)

def _lower_wick_pct(o, h, l, c):
    body_bot = np.minimum(o, c)
    return (body_bot - l) / (h - l).abs().replace(0, np.nan)

# Feature 76: Body Percentage Z-score 10d
def f06cbr_f06_candle_body_ratios_body_pct_zscore_10d_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_body_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 77: Body Percentage Z-score 21d
def f06cbr_f06_candle_body_ratios_body_pct_zscore_21d_v077_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_body_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 78: Body Percentage Z-score 63d
def f06cbr_f06_candle_body_ratios_body_pct_zscore_63d_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_body_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 79: Body Percentage Z-score 126d
def f06cbr_f06_candle_body_ratios_body_pct_zscore_126d_v079_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_body_pct(open, high, low, close), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 80: Body Percentage Z-score 252d
def f06cbr_f06_candle_body_ratios_body_pct_zscore_252d_v080_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_body_pct(open, high, low, close), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 81: Upper Wick Percentage Z-score 10d
def f06cbr_f06_candle_body_ratios_upper_wick_pct_zscore_10d_v081_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_upper_wick_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 82: Upper Wick Percentage Z-score 21d
def f06cbr_f06_candle_body_ratios_upper_wick_pct_zscore_21d_v082_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_upper_wick_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 83: Upper Wick Percentage Z-score 63d
def f06cbr_f06_candle_body_ratios_upper_wick_pct_zscore_63d_v083_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_upper_wick_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 84: Upper Wick Percentage Z-score 126d
def f06cbr_f06_candle_body_ratios_upper_wick_pct_zscore_126d_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_upper_wick_pct(open, high, low, close), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 85: Upper Wick Percentage Z-score 252d
def f06cbr_f06_candle_body_ratios_upper_wick_pct_zscore_252d_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_upper_wick_pct(open, high, low, close), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 86: Lower Wick Percentage Z-score 10d
def f06cbr_f06_candle_body_ratios_lower_wick_pct_zscore_10d_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_lower_wick_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 87: Lower Wick Percentage Z-score 21d
def f06cbr_f06_candle_body_ratios_lower_wick_pct_zscore_21d_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_lower_wick_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 88: Lower Wick Percentage Z-score 63d
def f06cbr_f06_candle_body_ratios_lower_wick_pct_zscore_63d_v088_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_lower_wick_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 89: Lower Wick Percentage Z-score 126d
def f06cbr_f06_candle_body_ratios_lower_wick_pct_zscore_126d_v089_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_lower_wick_pct(open, high, low, close), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 90: Lower Wick Percentage Z-score 252d
def f06cbr_f06_candle_body_ratios_lower_wick_pct_zscore_252d_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore(_lower_wick_pct(open, high, low, close), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 91: Wick Balance Z-score 10d
def f06cbr_f06_candle_body_ratios_wick_balance_zscore_10d_v091_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _zscore(balance, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 92: Wick Balance Z-score 21d
def f06cbr_f06_candle_body_ratios_wick_balance_zscore_21d_v092_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _zscore(balance, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 93: Wick Balance Z-score 63d
def f06cbr_f06_candle_body_ratios_wick_balance_zscore_63d_v093_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _zscore(balance, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 94: Wick Balance Z-score 126d
def f06cbr_f06_candle_body_ratios_wick_balance_zscore_126d_v094_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _zscore(balance, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 95: Wick Balance Z-score 252d
def f06cbr_f06_candle_body_ratios_wick_balance_zscore_252d_v095_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _zscore(balance, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 96: Relative Body Size SMA 126d
def f06cbr_f06_candle_body_ratios_rel_body_size_sma_126d_v096_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = _sma(body_abs / _sma(body_abs, 21).replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 97: Relative Body Size SMA 252d
def f06cbr_f06_candle_body_ratios_rel_body_size_sma_252d_v097_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    res = _sma(body_abs / _sma(body_abs, 21).replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 98: Relative Body Size Z-score 21d
def f06cbr_f06_candle_body_ratios_rel_body_size_zscore_21d_v098_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    rel_size = body_abs / _sma(body_abs, 21).replace(0, np.nan)
    res = _zscore(rel_size, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 99: Relative Body Size Z-score 63d
def f06cbr_f06_candle_body_ratios_rel_body_size_zscore_63d_v099_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    rel_size = body_abs / _sma(body_abs, 21).replace(0, np.nan)
    res = _zscore(rel_size, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 100: Relative Body Size Z-score 126d
def f06cbr_f06_candle_body_ratios_rel_body_size_zscore_126d_v100_signal(open: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    rel_size = body_abs / _sma(body_abs, 21).replace(0, np.nan)
    res = _zscore(rel_size, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 101: Doji Score EMA 5d
def f06cbr_f06_candle_body_ratios_doji_score_ema_5d_v101_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(1 - _body_pct(open, high, low, close), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 102: Doji Score EMA 10d
def f06cbr_f06_candle_body_ratios_doji_score_ema_10d_v102_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(1 - _body_pct(open, high, low, close), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 103: Doji Score EMA 21d
def f06cbr_f06_candle_body_ratios_doji_score_ema_21d_v103_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(1 - _body_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 104: Doji Score EMA 63d
def f06cbr_f06_candle_body_ratios_doji_score_ema_63d_v104_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(1 - _body_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 105: Doji Score EMA 126d
def f06cbr_f06_candle_body_ratios_doji_score_ema_126d_v105_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _ema(1 - _body_pct(open, high, low, close), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 106: Hammer Score EMA 5d
def f06cbr_f06_candle_body_ratios_hammer_score_ema_5d_v106_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(l_wick / (body + u_wick + 0.01), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 107: Hammer Score EMA 10d
def f06cbr_f06_candle_body_ratios_hammer_score_ema_10d_v107_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(l_wick / (body + u_wick + 0.01), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 108: Hammer Score EMA 21d
def f06cbr_f06_candle_body_ratios_hammer_score_ema_21d_v108_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(l_wick / (body + u_wick + 0.01), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 109: Hammer Score EMA 63d
def f06cbr_f06_candle_body_ratios_hammer_score_ema_63d_v109_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(l_wick / (body + u_wick + 0.01), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 110: Hammer Score EMA 126d
def f06cbr_f06_candle_body_ratios_hammer_score_ema_126d_v110_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(l_wick / (body + u_wick + 0.01), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 111: Shooting Star Score EMA 5d
def f06cbr_f06_candle_body_ratios_shooting_star_score_ema_5d_v111_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(u_wick / (body + l_wick + 0.01), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 112: Shooting Star Score EMA 10d
def f06cbr_f06_candle_body_ratios_shooting_star_score_ema_10d_v112_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(u_wick / (body + l_wick + 0.01), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 113: Shooting Star Score EMA 21d
def f06cbr_f06_candle_body_ratios_shooting_star_score_ema_21d_v113_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(u_wick / (body + l_wick + 0.01), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 114: Shooting Star Score EMA 63d
def f06cbr_f06_candle_body_ratios_shooting_star_score_ema_63d_v114_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(u_wick / (body + l_wick + 0.01), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 115: Shooting Star Score EMA 126d
def f06cbr_f06_candle_body_ratios_shooting_star_score_ema_126d_v115_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    body = _body_pct(open, high, low, close)
    u_wick = _upper_wick_pct(open, high, low, close)
    l_wick = _lower_wick_pct(open, high, low, close)
    res = _ema(u_wick / (body + l_wick + 0.01), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 116: Body Directionality SMA 126d
def f06cbr_f06_candle_body_ratios_body_dir_sma_126d_v116_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 117: Body Directionality SMA 252d
def f06cbr_f06_candle_body_ratios_body_dir_sma_252d_v117_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _sma((close - open) / (high - low).abs().replace(0, np.nan), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 118: Body Directionality Z-score 21d
def f06cbr_f06_candle_body_ratios_body_dir_zscore_21d_v118_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore((close - open) / (high - low).abs().replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 119: Body Directionality Z-score 63d
def f06cbr_f06_candle_body_ratios_body_dir_zscore_63d_v119_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore((close - open) / (high - low).abs().replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 120: Body Directionality Z-score 126d
def f06cbr_f06_candle_body_ratios_body_dir_zscore_126d_v120_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _zscore((close - open) / (high - low).abs().replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 121: Body Pct * Rel Range SMA 5d
def f06cbr_f06_candle_body_ratios_body_pct_times_rel_range_sma_5d_v121_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_body_pct(open, high, low, close) * rel_range, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 122: Body Pct * Rel Range SMA 10d
def f06cbr_f06_candle_body_ratios_body_pct_times_rel_range_sma_10d_v122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_body_pct(open, high, low, close) * rel_range, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 123: Body Pct * Rel Range SMA 21d
def f06cbr_f06_candle_body_ratios_body_pct_times_rel_range_sma_21d_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_body_pct(open, high, low, close) * rel_range, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 124: Body Pct * Rel Range SMA 63d
def f06cbr_f06_candle_body_ratios_body_pct_times_rel_range_sma_63d_v124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_body_pct(open, high, low, close) * rel_range, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 125: Body Pct * Rel Range SMA 126d
def f06cbr_f06_candle_body_ratios_body_pct_times_rel_range_sma_126d_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_body_pct(open, high, low, close) * rel_range, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 126: Upper Wick Pct * Rel Range SMA 5d
def f06cbr_f06_candle_body_ratios_u_wick_pct_times_rel_range_sma_5d_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_upper_wick_pct(open, high, low, close) * rel_range, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 127: Upper Wick Pct * Rel Range SMA 10d
def f06cbr_f06_candle_body_ratios_u_wick_pct_times_rel_range_sma_10d_v127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_upper_wick_pct(open, high, low, close) * rel_range, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 128: Upper Wick Pct * Rel Range SMA 21d
def f06cbr_f06_candle_body_ratios_u_wick_pct_times_rel_range_sma_21d_v128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_upper_wick_pct(open, high, low, close) * rel_range, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 129: Upper Wick Pct * Rel Range SMA 63d
def f06cbr_f06_candle_body_ratios_u_wick_pct_times_rel_range_sma_63d_v129_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_upper_wick_pct(open, high, low, close) * rel_range, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 130: Upper Wick Pct * Rel Range SMA 126d
def f06cbr_f06_candle_body_ratios_u_wick_pct_times_rel_range_sma_126d_v130_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_upper_wick_pct(open, high, low, close) * rel_range, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 131: Lower Wick Pct * Rel Range SMA 5d
def f06cbr_f06_candle_body_ratios_l_wick_pct_times_rel_range_sma_5d_v131_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_lower_wick_pct(open, high, low, close) * rel_range, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 132: Lower Wick Pct * Rel Range SMA 10d
def f06cbr_f06_candle_body_ratios_l_wick_pct_times_rel_range_sma_10d_v132_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_lower_wick_pct(open, high, low, close) * rel_range, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 133: Lower Wick Pct * Rel Range SMA 21d
def f06cbr_f06_candle_body_ratios_l_wick_pct_times_rel_range_sma_21d_v133_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_lower_wick_pct(open, high, low, close) * rel_range, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 134: Lower Wick Pct * Rel Range SMA 63d
def f06cbr_f06_candle_body_ratios_l_wick_pct_times_rel_range_sma_63d_v134_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_lower_wick_pct(open, high, low, close) * rel_range, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 135: Lower Wick Pct * Rel Range SMA 126d
def f06cbr_f06_candle_body_ratios_l_wick_pct_times_rel_range_sma_126d_v135_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    range_abs = (high * adj - low * adj).abs()
    rel_range = range_abs / _sma(range_abs, 21).replace(0, np.nan)
    res = _sma(_lower_wick_pct(open, high, low, close) * rel_range, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 136: Ratio of Body Abs to ATR 21d - SMA 5d
def f06cbr_f06_candle_body_ratios_body_to_atr_21d_sma_5d_v136_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    tr = pd.concat([(high * adj - low * adj), (high * adj - close.shift(1) * adj).abs(), (low * adj - close.shift(1) * adj).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    res = _sma(body_abs / atr.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 137: Ratio of Body Abs to ATR 21d - SMA 10d
def f06cbr_f06_candle_body_ratios_body_to_atr_21d_sma_10d_v137_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    tr = pd.concat([(high * adj - low * adj), (high * adj - close.shift(1) * adj).abs(), (low * adj - close.shift(1) * adj).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    res = _sma(body_abs / atr.replace(0, np.nan), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 138: Ratio of Body Abs to ATR 21d - SMA 21d
def f06cbr_f06_candle_body_ratios_body_to_atr_21d_sma_21d_v138_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    tr = pd.concat([(high * adj - low * adj), (high * adj - close.shift(1) * adj).abs(), (low * adj - close.shift(1) * adj).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    res = _sma(body_abs / atr.replace(0, np.nan), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 139: Ratio of Body Abs to ATR 21d - SMA 63d
def f06cbr_f06_candle_body_ratios_body_to_atr_21d_sma_63d_v139_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    tr = pd.concat([(high * adj - low * adj), (high * adj - close.shift(1) * adj).abs(), (low * adj - close.shift(1) * adj).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    res = _sma(body_abs / atr.replace(0, np.nan), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 140: Ratio of Body Abs to ATR 21d - SMA 126d
def f06cbr_f06_candle_body_ratios_body_to_atr_21d_sma_126d_v140_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    body_abs = (close * adj - open * adj).abs()
    tr = pd.concat([(high * adj - low * adj), (high * adj - close.shift(1) * adj).abs(), (low * adj - close.shift(1) * adj).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    res = _sma(body_abs / atr.replace(0, np.nan), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 141: Standard Deviation of Body Percentage 21d
def f06cbr_f06_candle_body_ratios_body_pct_std_21d_v141_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _std(_body_pct(open, high, low, close), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 142: Standard Deviation of Body Percentage 63d
def f06cbr_f06_candle_body_ratios_body_pct_std_63d_v142_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _std(_body_pct(open, high, low, close), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 143: Standard Deviation of Body Percentage 126d
def f06cbr_f06_candle_body_ratios_body_pct_std_126d_v143_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _std(_body_pct(open, high, low, close), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 144: Standard Deviation of Wick Balance 21d
def f06cbr_f06_candle_body_ratios_wick_balance_std_21d_v144_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _std(balance, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 145: Standard Deviation of Wick Balance 63d
def f06cbr_f06_candle_body_ratios_wick_balance_std_63d_v145_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    balance = _upper_wick_pct(open, high, low, close) - _lower_wick_pct(open, high, low, close)
    res = _std(balance, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 146: Large Candle Frequency (Body Pct > 0.8) SMA 10d
def f06cbr_f06_candle_body_ratios_large_candle_freq_sma_10d_v146_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    large = (_body_pct(open, high, low, close) > 0.8).astype(float)
    res = _sma(large, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 147: Large Candle Frequency (Body Pct > 0.8) SMA 21d
def f06cbr_f06_candle_body_ratios_large_candle_freq_sma_21d_v147_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    large = (_body_pct(open, high, low, close) > 0.8).astype(float)
    res = _sma(large, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 148: Large Candle Frequency (Body Pct > 0.8) SMA 63d
def f06cbr_f06_candle_body_ratios_large_candle_freq_sma_63d_v148_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    large = (_body_pct(open, high, low, close) > 0.8).astype(float)
    res = _sma(large, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 149: Large Candle Frequency (Body Pct > 0.8) SMA 126d
def f06cbr_f06_candle_body_ratios_large_candle_freq_sma_126d_v149_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    large = (_body_pct(open, high, low, close) > 0.8).astype(float)
    res = _sma(large, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 150: Large Candle Frequency (Body Pct > 0.8) SMA 252d
def f06cbr_f06_candle_body_ratios_large_candle_freq_sma_252d_v150_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    large = (_body_pct(open, high, low, close) > 0.8).astype(float)
    res = _sma(large, 252)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f06cbr_") and f.endswith("_signal")]

F06_CANDLE_BODY_RATIOS_BASE_REGISTRY_076_150 = {
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
    
    for n, c in F06_CANDLE_BODY_RATIOS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
