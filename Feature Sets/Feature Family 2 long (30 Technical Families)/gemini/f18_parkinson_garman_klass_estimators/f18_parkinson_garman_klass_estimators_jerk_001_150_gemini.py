# f18_parkinson_garman_klass_estimators_jerk_001_150_gemini.py
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

def _vol_efficiency_ratio(vol_est, vol_std):
    return vol_est / vol_std.replace(0, np.nan)

# Jerk of 5-day Parkinson volatility over 5 days
def f18pkg_parkinson_vol_5d_jerk_v001_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 10-day Parkinson volatility over 5 days
def f18pkg_parkinson_vol_10d_jerk_v002_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 21-day Parkinson volatility over 5 days
def f18pkg_parkinson_vol_21d_jerk_v003_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 42-day Parkinson volatility over 21 days
def f18pkg_parkinson_vol_42d_jerk_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 42).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63-day Parkinson volatility over 21 days
def f18pkg_parkinson_vol_63d_jerk_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126-day Parkinson volatility over 21 days
def f18pkg_parkinson_vol_126d_jerk_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252-day Parkinson volatility over 63 days
def f18pkg_parkinson_vol_252d_jerk_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504-day Parkinson volatility over 63 days
def f18pkg_parkinson_vol_504d_jerk_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 504).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 5-day Garman-Klass volatility over 5 days
def f18pkg_garman_klass_vol_5d_jerk_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 10-day Garman-Klass volatility over 5 days
def f18pkg_garman_klass_vol_10d_jerk_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 21-day Garman-Klass volatility over 5 days
def f18pkg_garman_klass_vol_21d_jerk_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 42-day Garman-Klass volatility over 21 days
def f18pkg_garman_klass_vol_42d_jerk_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63-day Garman-Klass volatility over 21 days
def f18pkg_garman_klass_vol_63d_jerk_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126-day Garman-Klass volatility over 21 days
def f18pkg_garman_klass_vol_126d_jerk_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252-day Garman-Klass volatility over 63 days
def f18pkg_garman_klass_vol_252d_jerk_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504-day Garman-Klass volatility over 63 days
def f18pkg_garman_klass_vol_504d_jerk_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 504).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 5-day Rogers-Satchell volatility over 5 days
def f18pkg_rogers_satchell_vol_5d_jerk_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 5).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 10-day Rogers-Satchell volatility over 5 days
def f18pkg_rogers_satchell_vol_10d_jerk_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 10).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 21-day Rogers-Satchell volatility over 5 days
def f18pkg_rogers_satchell_vol_21d_jerk_v019_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 21).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 42-day Rogers-Satchell volatility over 21 days
def f18pkg_rogers_satchell_vol_42d_jerk_v020_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63-day Rogers-Satchell volatility over 21 days
def f18pkg_rogers_satchell_vol_63d_jerk_v021_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126-day Rogers-Satchell volatility over 21 days
def f18pkg_rogers_satchell_vol_126d_jerk_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 252-day Rogers-Satchell volatility over 63 days
def f18pkg_rogers_satchell_vol_252d_jerk_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 504-day Rogers-Satchell volatility over 63 days
def f18pkg_rogers_satchell_vol_504d_jerk_v024_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 504).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 5d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_parkinson_5d_jerk_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _parkinson(high, low, 5)
    v_std = _std(close, 5)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 10d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_parkinson_10d_jerk_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _parkinson(high, low, 10)
    v_std = _std(close, 10)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 21d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_parkinson_21d_jerk_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _parkinson(high, low, 21)
    v_std = _std(close, 21)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 42d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_parkinson_42d_jerk_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _parkinson(high * adj, low * adj, 42)
    v_std = _std(closeadj, 42)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 63d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_parkinson_63d_jerk_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _parkinson(high * adj, low * adj, 63)
    v_std = _std(closeadj, 63)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 126d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_parkinson_126d_jerk_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _parkinson(high * adj, low * adj, 126)
    v_std = _std(closeadj, 126)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 252d vol efficiency ratio over 63 days
def f18pkg_efficiency_ratio_parkinson_252d_jerk_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _parkinson(high * adj, low * adj, 252)
    v_std = _std(closeadj, 252)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Parkinson 504d vol efficiency ratio over 63 days
def f18pkg_efficiency_ratio_parkinson_504d_jerk_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _parkinson(high * adj, low * adj, 504)
    v_std = _std(closeadj, 504)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 5d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_garman_klass_5d_jerk_v033_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _garman_klass(open, high, low, close, 5)
    v_std = _std(close, 5)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 10d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_garman_klass_10d_jerk_v034_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _garman_klass(open, high, low, close, 10)
    v_std = _std(close, 10)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 21d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_garman_klass_21d_jerk_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _garman_klass(open, high, low, close, 21)
    v_std = _std(close, 21)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 42d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_garman_klass_42d_jerk_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42)
    v_std = _std(closeadj, 42)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 63d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_garman_klass_63d_jerk_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    v_std = _std(closeadj, 63)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 126d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_garman_klass_126d_jerk_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126)
    v_std = _std(closeadj, 126)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 252d vol efficiency ratio over 63 days
def f18pkg_efficiency_ratio_garman_klass_252d_jerk_v039_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252)
    v_std = _std(closeadj, 252)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Garman-Klass 504d vol efficiency ratio over 63 days
def f18pkg_efficiency_ratio_garman_klass_504d_jerk_v040_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 504)
    v_std = _std(closeadj, 504)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 5d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_rogers_satchell_5d_jerk_v041_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _rogers_satchell(open, high, low, close, 5)
    v_std = _std(close, 5)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 10d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_rogers_satchell_10d_jerk_v042_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _rogers_satchell(open, high, low, close, 10)
    v_std = _std(close, 10)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 21d vol efficiency ratio over 5 days
def f18pkg_efficiency_ratio_rogers_satchell_21d_jerk_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _rogers_satchell(open, high, low, close, 21)
    v_std = _std(close, 21)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 42d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_rogers_satchell_42d_jerk_v044_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42)
    v_std = _std(closeadj, 42)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 63d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_rogers_satchell_63d_jerk_v045_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    v_std = _std(closeadj, 63)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 126d vol efficiency ratio over 21 days
def f18pkg_efficiency_ratio_rogers_satchell_126d_jerk_v046_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126)
    v_std = _std(closeadj, 126)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 252d vol efficiency ratio over 63 days
def f18pkg_efficiency_ratio_rogers_satchell_252d_jerk_v047_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252)
    v_std = _std(closeadj, 252)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Rogers-Satchell 504d vol efficiency ratio over 63 days
def f18pkg_efficiency_ratio_rogers_satchell_504d_jerk_v048_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 504)
    v_std = _std(closeadj, 504)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of volatility bias (GK / Park 5d) over 5 days
def f18pkg_vol_bias_gk_park_5d_jerk_v049_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 5)
    v_park = _parkinson(high, low, 5)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of volatility bias (GK / Park 10d) over 5 days
def f18pkg_vol_bias_gk_park_10d_jerk_v050_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 10)
    v_park = _parkinson(high, low, 10)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson Jerk Variations (v051-v080)
def f18pkg_parkinson_vol_15d_jerk_5d_v051_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 15).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_30d_jerk_10d_v052_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 30).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_60d_jerk_21d_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 60).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_90d_jerk_21d_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 90).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_120d_jerk_21d_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 120).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_180d_jerk_63d_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 180).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_252d_jerk_21d_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 252).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_378d_jerk_63d_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 378).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_504d_jerk_21d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 504).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_5d_jerk_1d_v060_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 5).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_10d_jerk_1d_v061_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 10).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_21d_jerk_1d_v062_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 21).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_42d_jerk_5d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 42).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_63d_jerk_5d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 63).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_126d_jerk_5d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 126).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_252d_jerk_5d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 252).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_5d_jerk_3d_v067_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 5).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_10d_jerk_3d_v068_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 10).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_21d_jerk_3d_v069_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 21).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_42d_jerk_10d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 42).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_63d_jerk_10d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 63).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_126d_jerk_10d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 126).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_252d_jerk_10d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 252).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_5d_jerk_10d_v074_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 5).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_21d_jerk_21d_v075_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 21).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_63d_jerk_63d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 63).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_parkinson_vol_126d_jerk_63d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 126).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f18pkg_parkinson_vol_21d_jerk_42d_v080_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 21).pct_change(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass Jerk Variations (v081-v110)
def f18pkg_garman_klass_vol_15d_jerk_5d_v081_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 15).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_30d_jerk_10d_v082_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 30).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_60d_jerk_21d_v083_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 60).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_90d_jerk_21d_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 90).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_120d_jerk_21d_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 120).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_180d_jerk_63d_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 180).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_252d_jerk_21d_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_378d_jerk_63d_v088_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 378).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_504d_jerk_21d_v089_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 504).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_5d_jerk_1d_v090_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 5).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_10d_jerk_1d_v091_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 10).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_21d_jerk_1d_v092_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 21).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_42d_jerk_5d_v093_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_63d_jerk_5d_v094_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_126d_jerk_5d_v095_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_252d_jerk_5d_v096_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_5d_jerk_3d_v097_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 5).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_10d_jerk_3d_v098_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 10).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_21d_jerk_3d_v099_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 21).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_42d_jerk_10d_v100_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_63d_jerk_10d_v101_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_126d_jerk_10d_v102_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_252d_jerk_10d_v103_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_5d_jerk_10d_v104_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 5).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_21d_jerk_21d_v105_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 21).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_63d_jerk_63d_v106_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_garman_klass_vol_126d_jerk_63d_v107_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f18pkg_garman_klass_vol_21d_jerk_42d_v110_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 21).pct_change(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell Jerk Variations (v111-v130)
def f18pkg_rogers_satchell_vol_15d_jerk_5d_v111_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 15).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_30d_jerk_10d_v112_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 30).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_60d_jerk_21d_v113_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 60).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_90d_jerk_21d_v114_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 90).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_120d_jerk_21d_v115_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 120).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_180d_jerk_63d_v116_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 180).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_252d_jerk_21d_v117_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_378d_jerk_63d_v118_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 378).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_504d_jerk_21d_v119_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 504).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_5d_jerk_1d_v120_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 5).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_10d_jerk_1d_v121_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 10).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_21d_jerk_1d_v122_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 21).pct_change(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_42d_jerk_5d_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_63d_jerk_5d_v124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_126d_jerk_5d_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_252d_jerk_5d_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_5d_jerk_3d_v127_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 5).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_10d_jerk_3d_v128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 10).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_21d_jerk_3d_v129_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 21).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_rogers_satchell_vol_42d_jerk_10d_v130_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency Ratio Jerk Variations (v131-v140)
def f18pkg_efficiency_ratio_parkinson_15d_jerk_5d_v131_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _parkinson(high, low, 15)
    v_std = _std(close, 15)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_efficiency_ratio_garman_klass_15d_jerk_5d_v132_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _garman_klass(open, high, low, close, 15)
    v_std = _std(close, 15)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_efficiency_ratio_rogers_satchell_15d_jerk_5d_v133_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_est = _rogers_satchell(open, high, low, close, 15)
    v_std = _std(close, 15)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_efficiency_ratio_parkinson_30d_jerk_10d_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _parkinson(high * adj, low * adj, 30)
    v_std = _std(closeadj, 30)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_efficiency_ratio_garman_klass_30d_jerk_10d_v135_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 30)
    v_std = _std(closeadj, 30)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_efficiency_ratio_rogers_satchell_30d_jerk_10d_v136_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 30)
    v_std = _std(closeadj, 30)
    res = _vol_efficiency_ratio(v_est, v_std).pct_change(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)





# Volatility Bias Jerk Variations (v141-v150)
def f18pkg_vol_bias_gk_park_21d_jerk_5d_v141_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 21)
    v_park = _parkinson(high, low, 21)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_rs_park_21d_jerk_5d_v142_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rs = _rogers_satchell(open, high, low, close, 21)
    v_park = _parkinson(high, low, 21)
    res = (v_rs / v_park.replace(0, np.nan)).pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_gk_park_63d_jerk_21d_v143_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    v_park = _parkinson(high * adj, low * adj, 63)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_rs_park_63d_jerk_21d_v144_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    v_park = _parkinson(high * adj, low * adj, 63)
    res = (v_rs / v_park.replace(0, np.nan)).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_gk_park_126d_jerk_21d_v145_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126)
    v_park = _parkinson(high * adj, low * adj, 126)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_rs_park_126d_jerk_21d_v146_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126)
    v_park = _parkinson(high * adj, low * adj, 126)
    res = (v_rs / v_park.replace(0, np.nan)).pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_gk_park_252d_jerk_63d_v147_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252)
    v_park = _parkinson(high * adj, low * adj, 252)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_rs_park_252d_jerk_63d_v148_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252)
    v_park = _parkinson(high * adj, low * adj, 252)
    res = (v_rs / v_park.replace(0, np.nan)).pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_gk_park_5d_jerk_3d_v149_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 5)
    v_park = _parkinson(high, low, 5)
    res = (v_gk / v_park.replace(0, np.nan)).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f18pkg_vol_bias_rs_park_5d_jerk_3d_v150_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rs = _rogers_satchell(open, high, low, close, 5)
    v_park = _parkinson(high, low, 5)
    res = (v_rs / v_park.replace(0, np.nan)).pct_change(3).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "open"]}

JERK_NAMES = [f for f in globals() if f.startswith("f18pkg_") and f.endswith("_signal")]

F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
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
    for n, c in F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk OK")
