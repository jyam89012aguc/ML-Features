# f18_parkinson_garman_klass_estimators_base_001_075_gemini.py
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
    # Sum(log(h/c)*log(h/o) + log(l/c)*log(l/o)) / w
    rs = (np.log(h / c.replace(0, np.nan)) * np.log(h / o.replace(0, np.nan)) + 
          np.log(l / c.replace(0, np.nan)) * np.log(l / o.replace(0, np.nan)))
    return np.sqrt(rs.rolling(w).mean().abs())

def _std(c, w):
    # Standard deviation of log returns
    log_ret = np.log(c / c.shift(1).replace(0, np.nan))
    return log_ret.rolling(w).std()

def _vol_efficiency_ratio(vol_est, vol_std):
    return vol_est / vol_std.replace(0, np.nan)

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _z(s, w):
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

# Parkinson volatility estimator over 5 days
def f18pkg_parkinson_vol_5d_v001_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 10 days
def f18pkg_parkinson_vol_10d_v002_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 21 days
def f18pkg_parkinson_vol_21d_v003_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    res = _parkinson(high, low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 42 days using adjusted prices
def f18pkg_parkinson_vol_42d_v004_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 63 days using adjusted prices
def f18pkg_parkinson_vol_63d_v005_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 126 days using adjusted prices
def f18pkg_parkinson_vol_126d_v006_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 252 days using adjusted prices
def f18pkg_parkinson_vol_252d_v007_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility estimator over 504 days using adjusted prices
def f18pkg_parkinson_vol_504d_v008_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _parkinson(high * adj, low * adj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 5 days
def f18pkg_garman_klass_vol_5d_v009_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 10 days
def f18pkg_garman_klass_vol_10d_v010_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 21 days
def f18pkg_garman_klass_vol_21d_v011_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _garman_klass(open, high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 42 days using adjusted prices
def f18pkg_garman_klass_vol_42d_v012_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 63 days using adjusted prices
def f18pkg_garman_klass_vol_63d_v013_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 126 days using adjusted prices
def f18pkg_garman_klass_vol_126d_v014_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 252 days using adjusted prices
def f18pkg_garman_klass_vol_252d_v015_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility estimator over 504 days using adjusted prices
def f18pkg_garman_klass_vol_504d_v016_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _garman_klass(open * adj, high * adj, low * adj, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 5 days
def f18pkg_rogers_satchell_vol_5d_v017_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 10 days
def f18pkg_rogers_satchell_vol_10d_v018_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 21 days
def f18pkg_rogers_satchell_vol_21d_v019_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _rogers_satchell(open, high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 42 days using adjusted prices
def f18pkg_rogers_satchell_vol_42d_v020_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 63 days using adjusted prices
def f18pkg_rogers_satchell_vol_63d_v021_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 126 days using adjusted prices
def f18pkg_rogers_satchell_vol_126d_v022_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 252 days using adjusted prices
def f18pkg_rogers_satchell_vol_252d_v023_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility estimator over 504 days using adjusted prices
def f18pkg_rogers_satchell_vol_504d_v024_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (5d)
def f18pkg_efficiency_ratio_parkinson_5d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _parkinson(high, low, 5)
    vol_std = _std(close, 5)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (10d)
def f18pkg_efficiency_ratio_parkinson_10d_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _parkinson(high, low, 10)
    vol_std = _std(close, 10)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (21d)
def f18pkg_efficiency_ratio_parkinson_21d_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _parkinson(high, low, 21)
    vol_std = _std(close, 21)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (42d)
def f18pkg_efficiency_ratio_parkinson_42d_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _parkinson(high * adj, low * adj, 42)
    vol_std = _std(closeadj, 42)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (63d)
def f18pkg_efficiency_ratio_parkinson_63d_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _parkinson(high * adj, low * adj, 63)
    vol_std = _std(closeadj, 63)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (126d)
def f18pkg_efficiency_ratio_parkinson_126d_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _parkinson(high * adj, low * adj, 126)
    vol_std = _std(closeadj, 126)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (252d)
def f18pkg_efficiency_ratio_parkinson_252d_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _parkinson(high * adj, low * adj, 252)
    vol_std = _std(closeadj, 252)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Parkinson volatility to standard close-to-close volatility (504d)
def f18pkg_efficiency_ratio_parkinson_504d_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _parkinson(high * adj, low * adj, 504)
    vol_std = _std(closeadj, 504)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (5d)
def f18pkg_efficiency_ratio_garman_klass_5d_v033_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _garman_klass(open, high, low, close, 5)
    vol_std = _std(close, 5)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (10d)
def f18pkg_efficiency_ratio_garman_klass_10d_v034_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _garman_klass(open, high, low, close, 10)
    vol_std = _std(close, 10)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (21d)
def f18pkg_efficiency_ratio_garman_klass_21d_v035_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _garman_klass(open, high, low, close, 21)
    vol_std = _std(close, 21)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (42d)
def f18pkg_efficiency_ratio_garman_klass_42d_v036_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42)
    vol_std = _std(closeadj, 42)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (63d)
def f18pkg_efficiency_ratio_garman_klass_63d_v037_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    vol_std = _std(closeadj, 63)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (126d)
def f18pkg_efficiency_ratio_garman_klass_126d_v038_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126)
    vol_std = _std(closeadj, 126)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (252d)
def f18pkg_efficiency_ratio_garman_klass_252d_v039_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252)
    vol_std = _std(closeadj, 252)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Garman-Klass volatility to standard close-to-close volatility (504d)
def f18pkg_efficiency_ratio_garman_klass_504d_v040_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _garman_klass(open * adj, high * adj, low * adj, closeadj, 504)
    vol_std = _std(closeadj, 504)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (5d)
def f18pkg_efficiency_ratio_rogers_satchell_5d_v041_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _rogers_satchell(open, high, low, close, 5)
    vol_std = _std(close, 5)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (10d)
def f18pkg_efficiency_ratio_rogers_satchell_10d_v042_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _rogers_satchell(open, high, low, close, 10)
    vol_std = _std(close, 10)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (21d)
def f18pkg_efficiency_ratio_rogers_satchell_21d_v043_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    vol_est = _rogers_satchell(open, high, low, close, 21)
    vol_std = _std(close, 21)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (42d)
def f18pkg_efficiency_ratio_rogers_satchell_42d_v044_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42)
    vol_std = _std(closeadj, 42)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (63d)
def f18pkg_efficiency_ratio_rogers_satchell_63d_v045_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    vol_std = _std(closeadj, 63)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (126d)
def f18pkg_efficiency_ratio_rogers_satchell_126d_v046_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126)
    vol_std = _std(closeadj, 126)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (252d)
def f18pkg_efficiency_ratio_rogers_satchell_252d_v047_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252)
    vol_std = _std(closeadj, 252)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Efficiency ratio of Rogers-Satchell volatility to standard close-to-close volatility (504d)
def f18pkg_efficiency_ratio_rogers_satchell_504d_v048_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    vol_est = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 504)
    vol_std = _std(closeadj, 504)
    res = _vol_efficiency_ratio(vol_est, vol_std)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (5d)
def f18pkg_vol_bias_gk_park_5d_v049_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 5)
    v_park = _parkinson(high, low, 5)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (10d)
def f18pkg_vol_bias_gk_park_10d_v050_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 10)
    v_park = _parkinson(high, low, 10)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (21d)
def f18pkg_vol_bias_gk_park_21d_v051_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_gk = _garman_klass(open, high, low, close, 21)
    v_park = _parkinson(high, low, 21)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (42d)
def f18pkg_vol_bias_gk_park_42d_v052_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 42)
    v_park = _parkinson(high * adj, low * adj, 42)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (63d)
def f18pkg_vol_bias_gk_park_63d_v053_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    v_park = _parkinson(high * adj, low * adj, 63)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (126d)
def f18pkg_vol_bias_gk_park_126d_v054_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 126)
    v_park = _parkinson(high * adj, low * adj, 126)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (252d)
def f18pkg_vol_bias_gk_park_252d_v055_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 252)
    v_park = _parkinson(high * adj, low * adj, 252)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Garman-Klass volatility to Parkinson volatility (504d)
def f18pkg_vol_bias_gk_park_504d_v056_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_gk = _garman_klass(open * adj, high * adj, low * adj, closeadj, 504)
    v_park = _parkinson(high * adj, low * adj, 504)
    res = v_gk / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (5d)
def f18pkg_vol_bias_rs_park_5d_v057_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rs = _rogers_satchell(open, high, low, close, 5)
    v_park = _parkinson(high, low, 5)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (10d)
def f18pkg_vol_bias_rs_park_10d_v058_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rs = _rogers_satchell(open, high, low, close, 10)
    v_park = _parkinson(high, low, 10)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (21d)
def f18pkg_vol_bias_rs_park_21d_v059_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v_rs = _rogers_satchell(open, high, low, close, 21)
    v_park = _parkinson(high, low, 21)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (42d)
def f18pkg_vol_bias_rs_park_42d_v060_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 42)
    v_park = _parkinson(high * adj, low * adj, 42)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (63d)
def f18pkg_vol_bias_rs_park_63d_v061_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    v_park = _parkinson(high * adj, low * adj, 63)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (126d)
def f18pkg_vol_bias_rs_park_126d_v062_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 126)
    v_park = _parkinson(high * adj, low * adj, 126)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (252d)
def f18pkg_vol_bias_rs_park_252d_v063_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 252)
    v_park = _parkinson(high * adj, low * adj, 252)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Volatility bias: ratio of Rogers-Satchell volatility to Parkinson volatility (504d)
def f18pkg_vol_bias_rs_park_504d_v064_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v_rs = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 504)
    v_park = _parkinson(high * adj, low * adj, 504)
    res = v_rs / v_park.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility relative to its 21-day moving average (5d)
def f18pkg_parkinson_vol_rel_ma_5d_21d_v065_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = v / _sma(v, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility relative to its 63-day moving average (21d)
def f18pkg_parkinson_vol_rel_ma_21d_63d_v066_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 21)
    res = v / _sma(v, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Parkinson volatility relative to its 252-day moving average (63d)
def f18pkg_parkinson_vol_rel_ma_63d_252d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _parkinson(high * adj, low * adj, 63)
    res = v / _sma(v, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility relative to its 21-day moving average (5d)
def f18pkg_garman_klass_vol_rel_ma_5d_21d_v068_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 5)
    res = v / _sma(v, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility relative to its 63-day moving average (21d)
def f18pkg_garman_klass_vol_rel_ma_21d_63d_v069_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 21)
    res = v / _sma(v, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Garman-Klass volatility relative to its 252-day moving average (63d)
def f18pkg_garman_klass_vol_rel_ma_63d_252d_v070_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _garman_klass(open * adj, high * adj, low * adj, closeadj, 63)
    res = v / _sma(v, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility relative to its 21-day moving average (5d)
def f18pkg_rogers_satchell_vol_rel_ma_5d_21d_v071_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 5)
    res = v / _sma(v, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility relative to its 63-day moving average (21d)
def f18pkg_rogers_satchell_vol_rel_ma_21d_63d_v072_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _rogers_satchell(open, high, low, close, 21)
    res = v / _sma(v, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Rogers-Satchell volatility relative to its 252-day moving average (63d)
def f18pkg_rogers_satchell_vol_rel_ma_63d_252d_v073_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    v = _rogers_satchell(open * adj, high * adj, low * adj, closeadj, 63)
    res = v / _sma(v, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of Parkinson volatility over 21 days (5d window for estimation)
def f18pkg_parkinson_vol_zscore_5d_21d_v074_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    v = _parkinson(high, low, 5)
    res = _z(v, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of Garman-Klass volatility over 63 days (21d window for estimation)
def f18pkg_garman_klass_vol_zscore_21d_63d_v075_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = _garman_klass(open, high, low, close, 21)
    res = _z(v, 63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "open"]}

BASE_NAMES = [f for f in globals() if f.startswith("f18pkg_") and f.endswith("_signal")]

F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_BASE_REGISTRY_001_075 = {
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
    for n, c in F18_PARKINSON_GARMAN_KLASS_ESTIMATORS_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
