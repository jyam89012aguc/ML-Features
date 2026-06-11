# f18_parkinson_garman_klass_estimators_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _parkinson(h, l, w):
    const = 1.0 / (4.0 * np.log(2.0))
    range_sq = np.log(h / l.replace(0, np.nan))**2
    return np.sqrt(range_sq.rolling(w).mean() * const)

def _garman_klass(o, h, l, c, w):
    term1 = 0.5 * np.log(h / l.replace(0, np.nan))**2
    term2 = (2.0 * np.log(2.0) - 1.0) * np.log(c / o.replace(0, np.nan))**2
    return np.sqrt((term1 - term2).rolling(w).mean().abs())

def _rogers_satchell(o, h, l, c, w):
    rs = (np.log(h / c.replace(0, np.nan)) * np.log(h / o.replace(0, np.nan)) + 
          np.log(l / c.replace(0, np.nan)) * np.log(l / o.replace(0, np.nan)))
    return np.sqrt(rs.rolling(w).mean().abs())

def _std(c, w):
    log_ret = np.log(c / c.shift(1).replace(0, np.nan))
    return log_ret.rolling(w).std()

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _z(s, w):
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

# Z-score of Rogers-Satchell volatility over 63 days (21d estimation)
def f18pkg_rogers_satchell_vol_zscore_21d_63d_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 21)
    res = _z(v, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 5-day Parkinson volatility to 63-day Parkinson volatility
def f18pkg_parkinson_vol_ratio_5d_63d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v5 = _parkinson(high, low, 5)
    adj = closeadj / close.replace(0, np.nan)
    v63 = _parkinson(high * adj, low * adj, 63)
    res = v5 / v63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 5-day Garman-Klass volatility to 63-day Garman-Klass volatility
def f18pkg_garman_klass_vol_ratio_5d_63d_v078_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v5 = _garman_klass(open, high, low, close, 5)
    adj = closeadj / close.replace(0, np.nan)
    v63 = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    res = v5 / v63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 5-day Rogers-Satchell volatility to 63-day Rogers-Satchell volatility
def f18pkg_rogers_satchell_vol_ratio_5d_63d_v079_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v5 = _rogers_satchell(open, high, low, close, 5)
    adj = closeadj / close.replace(0, np.nan)
    v63 = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    res = v5 / v63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 21-day Parkinson volatility to 252-day Parkinson volatility
def f18pkg_parkinson_vol_ratio_21d_252d_v080_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v21 = _parkinson(high, low, 21)
    adj = closeadj / close.replace(0, np.nan)
    v252 = _parkinson(high * adj, low * adj, 252)
    res = v21 / v252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day rate of change of Parkinson 21-day volatility
def f18pkg_parkinson_vol_roc_5d_v081_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = v.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# 5-day rate of change of Garman-Klass 21-day volatility
def f18pkg_garman_klass_vol_roc_5d_v082_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 21)
    res = v.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day rate of change of Parkinson 63-day volatility
def f18pkg_parkinson_vol_roc_21d_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _parkinson(high * adj, low * adj, 63)
    res = v.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# 21-day rate of change of Garman-Klass 63-day volatility
def f18pkg_garman_klass_vol_roc_21d_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    res = v.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson 5d vol relative to high-low range over 5 days
def f18pkg_parkinson_vol_rel_range_5d_v085_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    rng = (high - low) / low.replace(0, np.nan)
    res = v / rng.rolling(5).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass 5d vol relative to high-low range over 5 days
def f18pkg_garman_klass_vol_rel_range_5d_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 5)
    rng = (high - low) / low.replace(0, np.nan)
    res = v / rng.rolling(5).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson 21d vol relative to ATR 21d
def f18pkg_parkinson_vol_rel_atr_21d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(21).mean()
    res = v / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 5d Z-score over 252 days
def f18pkg_parkinson_vol_zscore_5d_252d_v088_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass vol 5d Z-score over 252 days
def f18pkg_garman_klass_vol_zscore_5d_252d_v089_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 5)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell vol 5d Z-score over 252 days
def f18pkg_rogers_satchell_vol_zscore_5d_252d_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 5)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA 5 of Parkinson 21d vol
def f18pkg_parkinson_vol_sma5_21d_v091_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = _sma(v, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA 21 of Parkinson 21d vol
def f18pkg_parkinson_vol_sma21_21d_v092_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = _sma(v, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson 10d vol using 2-day shifts to check stability
def f18pkg_parkinson_vol_10d_shift2_v093_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 10)
    res = (v + v.shift(2)) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 42d scaled by inverse of 5d vol
def f18pkg_parkinson_vol_scaled_42d_5d_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v42 = _parkinson(high * adj, low * adj, 42)
    v5 = _parkinson(high, low, 5)
    res = v42 / v5.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 126d Z-score
def f18pkg_parkinson_vol_zscore_126d_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _parkinson(high * adj, low * adj, 126)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 5d relative to its 10d max
def f18pkg_parkinson_vol_rel_max_5d_10d_v096_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = v / v.rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 5d relative to its 10d min
def f18pkg_parkinson_vol_rel_min_5d_10d_v097_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = v / v.rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 21d relative to its 63d max
def f18pkg_parkinson_vol_rel_max_21d_63d_v098_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = v / v.rolling(63).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson vol 21d relative to its 63d min
def f18pkg_parkinson_vol_rel_min_21d_63d_v099_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = v / v.rolling(63).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass 5d vol relative to its 10d max
def f18pkg_garman_klass_vol_rel_max_5d_10d_v100_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 5)
    res = v / v.rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# [Functions v101-v150 omitted for brevity in this thought but will be included in the tool call]
# Actually I MUST include ALL functions in the tool call.

def f18pkg_garman_klass_vol_rel_min_5d_10d_v101_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 5)
    res = v / v.rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_rel_max_5d_10d_v102_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 5)
    res = v / v.rolling(10).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_rel_min_5d_10d_v103_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 5)
    res = v / v.rolling(10).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)


def f18pkg_parkinson_vol_15d_v105_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_30d_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_90d_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 90)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_15d_v108_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_30d_v109_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_15d_v110_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_30d_v111_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_zscore_10d_21d_v112_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 10)
    res = _z(v, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_zscore_21d_126d_v113_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = _z(v, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_zscore_10d_21d_v114_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 10)
    res = _z(v, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_zscore_21d_126d_v115_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 21)
    res = _z(v, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_zscore_10d_21d_v116_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 10)
    res = _z(v, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_zscore_21d_126d_v117_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 21)
    res = _z(v, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_rel_ma_10d_42d_v118_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 10)
    res = v / _sma(v, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_rel_ma_10d_42d_v119_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 10)
    res = v / _sma(v, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_rel_ma_10d_42d_v120_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 10)
    res = v / _sma(v, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_ratio_10d_126d_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v10 = _parkinson(high, low, 10)
    adj = closeadj / close.replace(0, np.nan)
    v126 = _parkinson(high * adj, low * adj, 126)
    res = v10 / v126.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_ratio_10d_126d_v122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v10 = _garman_klass(open, high, low, close, 10)
    adj = closeadj / close.replace(0, np.nan)
    v126 = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126)
    res = v10 / v126.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_ratio_10d_126d_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v10 = _rogers_satchell(open, high, low, close, 10)
    adj = closeadj / close.replace(0, np.nan)
    v126 = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126)
    res = v10 / v126.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_roc_10d_v124_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 10)
    res = v.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_roc_10d_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 10)
    res = v.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_roc_10d_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 10)
    res = v.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_rel_range_21d_v127_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    rng = (high - low) / low.replace(0, np.nan)
    res = v / rng.rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_rel_range_21d_v128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 21)
    rng = (high - low) / low.replace(0, np.nan)
    res = v / rng.rolling(21).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_rel_atr_5d_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(5).mean()
    res = v / (atr / close.replace(0, np.nan)).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_zscore_21d_252d_v130_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_zscore_21d_252d_v131_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 21)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_zscore_21d_252d_v132_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 21)
    res = _z(v, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_ema5_21d_v133_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = v.ewm(span=5, adjust=False).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_ema21_21d_v134_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = v.ewm(span=21, adjust=False).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_5d_shift1_v135_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = (v + v.shift(1)) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_scaled_63d_21d_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v63 = _parkinson(high * adj, low * adj, 63)
    v21 = _parkinson(high, low, 21)
    res = v63 / v21.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_zscore_504d_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _parkinson(high * adj, low * adj, 504)
    res = _z(v, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_rel_max_10d_21d_v138_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 10)
    res = v / v.rolling(21).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_rel_min_10d_21d_v139_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 10)
    res = v / v.rolling(21).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_rel_max_10d_21d_v140_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 10)
    res = v / v.rolling(21).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_rel_min_10d_21d_v141_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 10)
    res = v / v.rolling(21).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_rel_max_10d_21d_v142_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 10)
    res = v / v.rolling(21).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_rel_min_10d_21d_v143_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 10)
    res = v / v.rolling(21).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_ratio_5d_21d_v144_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v5 = _parkinson(high, low, 5)
    v21 = _parkinson(high, low, 21)
    res = v5 / v21.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_ratio_5d_21d_v145_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v5 = _garman_klass(open, high, low, close, 5)
    v21 = _garman_klass(open, high, low, close, 21)
    res = v5 / v21.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_ratio_5d_21d_v146_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v5 = _rogers_satchell(open, high, low, close, 5)
    v21 = _rogers_satchell(open, high, low, close, 21)
    res = v5 / v21.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_ratio_21d_63d_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v21 = _parkinson(high, low, 21)
    adj = closeadj / close.replace(0, np.nan)
    v63 = _parkinson(high * adj, low * adj, 63)
    res = v21 / v63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_ratio_21d_63d_v148_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v21 = _garman_klass(open, high, low, close, 21)
    adj = closeadj / close.replace(0, np.nan)
    v63 = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    res = v21 / v63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_ratio_21d_63d_v149_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    v21 = _rogers_satchell(open, high, low, close, 21)
    adj = closeadj / close.replace(0, np.nan)
    v63 = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    res = v21 / v63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_5d_zscore_10d_v150_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = _z(v, 10)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "open"]}

BASE_NAMES = [f for f in globals() if f.startswith("f18pkg_") and f.endswith("_signal")]

F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_BASE_REGISTRY_076_150 = {
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
    sz = 500; d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum()+100, 
        "closeadj": np.random.randn(sz).cumsum()+100, 
        "high": np.random.randn(sz).cumsum()+110, 
        "low": np.random.randn(sz).cumsum()+90, 
        "open": np.random.randn(sz).cumsum()+100,
        "ticker": ["T"]*sz, 
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
