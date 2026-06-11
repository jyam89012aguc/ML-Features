"""f18 jerk features 001-150 (1st/2nd diff of base v001-v150).
Each feature uses construction helpers (_park/_gk/_rs/_yz/_atr/_bipow)
analogous to f01's _sma/_ema helpers, then applies inline diff(k) or
b - 2*b.shift(k) + b.shift(2k). k follows the ROC bracket of the base
feature primary window: <=5:5; 6-21:5 or 10; 22-63:10 or 21;
64-200:21 or 63; >200:63.
"""
import numpy as np
import pandas as pd

# --- Vol-estimator construction helpers (used by feature functions below).
# Each helper builds one named estimator at window n. These are utility
# constructors (analogous to _sma/_ema in f01); each feature function uses
# them as building blocks and applies the slope/jerk transform inline.

_LN2 = np.log(2.0)
_GK_CO_COEF = 2.0 * _LN2 - 1.0


def _park(h, l, n):
    return ((np.log(h / l) ** 2).rolling(n, min_periods=n).mean() / (4.0 * _LN2)) ** 0.5


def _gk(o, h, l, c, n):
    v = (0.5 * np.log(h / l) ** 2 - _GK_CO_COEF * np.log(c / o) ** 2).rolling(n, min_periods=n).mean()
    return v.clip(lower=0.0) ** 0.5


def _rs(o, h, l, c, n):
    v = (np.log(h / c) * np.log(h / o) + np.log(l / c) * np.log(l / o)).rolling(n, min_periods=n).mean()
    return v.clip(lower=0.0) ** 0.5


def _yz(o, h, l, c, n):
    on = np.log(o / c.shift(1)); oc = np.log(c / o)
    von = on.rolling(n, min_periods=n).var(ddof=1); voc = oc.rolling(n, min_periods=n).var(ddof=1)
    vrs = (np.log(h / c) * np.log(h / o) + np.log(l / c) * np.log(l / o)).rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    return (von + k * voc + (1 - k) * vrs).clip(lower=0.0) ** 0.5


def _tr(h, l, c):
    return pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)


def _atr_w(h, l, c, n):
    return _tr(h, l, c).ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _atr_s(h, l, c, n):
    return _tr(h, l, c).rolling(n, min_periods=n).mean()


def _bipow(c, n):
    r = np.log(c / c.shift(1)).abs()
    return (r * r.shift(1) * (np.pi / 2.0)).rolling(n, min_periods=n).sum() ** 0.5


def _rv(c, n):
    return ((np.log(c / c.shift(1)) ** 2).rolling(n, min_periods=n).mean()) ** 0.5


def f18pg_f18_parkinson_garman_klass_estimators_park_5d_jerk_v001_signal(high, low):
    b = _park(high, low, 5)
    return (b - 2.0 * b.shift(5) + b.shift(2 * 5)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_log_21d_jerk_v002_signal(high, low):
    b = np.log(_park(high, low, 21).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_63d_jerk_v003_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 63)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_252d_jerk_v004_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 252)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_10d_jerk_v005_signal(open, high, low, close):
    b = _gk(open, high, low, close, 10)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_log_30d_jerk_v006_signal(open, high, low, close, closeadj):
    _ = closeadj; b = np.log(_gk(open, high, low, close, 30).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_14d_jerk_v007_signal(open, high, low, close):
    b = _rs(open, high, low, close, 14)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_60d_jerk_v008_signal(open, high, low, closeadj):
    b = _rs(open, high, low, closeadj, 60)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_21d_jerk_v009_signal(open, high, low, close):
    b = _yz(open, high, low, close, 21)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_63d_jerk_v010_signal(open, high, low, closeadj):
    b = _yz(open, high, low, closeadj, 63)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_gk_ratio_21d_jerk_v011_signal(open, high, low, close):
    p = _park(high, low, 21); g = _gk(open, high, low, close, 21)
    b = p / g.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_rs_ratio_30d_jerk_v012_signal(open, high, low, closeadj):
    p = _park(high, low, 30); r = _rs(open, high, low, closeadj, 30)
    b = p / r.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_rs_diff_21d_jerk_v013_signal(open, high, low, close):
    g = _gk(open, high, low, close, 21); r = _rs(open, high, low, close, 21)
    b = (g - r) / g.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_minus_realized_log_63d_jerk_v014_signal(closeadj, high, low):
    p = _park(high, low, 63); rv = _rv(closeadj, 63)
    b = np.log(p.replace(0.0, np.nan)) - np.log(rv.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_realized_ratio_21d_jerk_v015_signal(high, low, close):
    b = _park(high, low, 21) / _rv(close, 21).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_wilder_14d_jerk_v016_signal(high, low, close):
    b = _atr_w(high, low, close, 14) / close
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_sma_50d_jerk_v017_signal(high, low, closeadj):
    b = _atr_s(high, low, closeadj, 50) / closeadj
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_sma_8d_jerk_v018_signal(high, low):
    b = np.log(high / low).rolling(8).mean()
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_z_60_252_jerk_v019_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 60); m = p.rolling(252, min_periods=126).mean(); sd = p.rolling(252, min_periods=126).std(ddof=0)
    b = (p - m) / sd.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_q90_dist_120d_jerk_v020_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); q90 = p.rolling(120, min_periods=60).quantile(0.9)
    b = (p - q90) / p.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_z_21_252_jerk_v021_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 21); m = r.rolling(252, min_periods=126).mean(); sd = r.rolling(252, min_periods=126).std(ddof=0)
    b = (r - m) / sd.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_pctrank_252d_jerk_v022_signal(high, low, closeadj):
    base = _atr_s(high, low, closeadj, 21) / closeadj
    b = base.rolling(252, min_periods=126).rank(pct=True)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_park_log_ratio_60d_jerk_v023_signal(open, high, low, closeadj):
    g = _gk(open, high, low, closeadj, 60); p = _park(high, low, 60)
    b = np.log(g / p.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_term_5_21_jerk_v024_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 5) / _park(high, low, 21).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_term_log_21_63_jerk_v025_signal(closeadj, high, low):
    _ = closeadj; b = np.log(_park(high, low, 21) / _park(high, low, 63).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_park_cross_21d_jerk_v026_signal(open, high, low, close):
    yz = _yz(open, high, low, close, 21); p = _park(high, low, 21)
    b = np.log(yz / p.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_slope_21d_jerk_v027_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); m = p.abs().rolling(21, min_periods=10).mean()
    b = (p - p.shift(21)) / m.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(2 * 5)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_slope_30d_jerk_v028_signal(open, high, low, close):
    g = _gk(open, high, low, close, 10); b = g - g.shift(30)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_accel_21d_jerk_v029_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); b = p - 2.0 * p.shift(21) + p.shift(42)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_bipower_21d_jerk_v030_signal(close):
    b = _bipow(close, 21)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_bipower_realized_ratio_60d_jerk_v031_signal(closeadj):
    r = np.log(closeadj / closeadj.shift(1))
    bp = r.abs() * r.abs().shift(1) * (np.pi / 2.0)
    b = bp.rolling(60).sum() / (r ** 2).rolling(60).sum().replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_share_30d_jerk_v032_signal(open, closeadj):
    on = np.log(open / closeadj.shift(1)); oc = np.log(closeadj / open)
    von = on.rolling(30).var(ddof=1); voc = oc.rolling(30).var(ddof=1)
    b = von / (von + voc).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_oc_var_21d_jerk_v033_signal(open, close):
    b = np.log(close / open).rolling(21).var(ddof=1)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_p90_flag_252d_jerk_v034_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); q90 = p.rolling(252, min_periods=126).quantile(0.9)
    b = (p > q90).astype(float).where(p.notna() & q90.notna())
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_iqr_60d_jerk_v035_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 5)
    b = p.rolling(60, min_periods=30).quantile(0.75) - p.rolling(60, min_periods=30).quantile(0.25)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_dayssince_parkp95_252d_jerk_v036_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); q = p.rolling(252, min_periods=126).quantile(0.95)
    b = (p - q) / q.replace(0.0, np.nan)
    j = b - 2.0 * b.shift(63) + b.shift(2 * 63); nrm = b.abs().rolling(63, min_periods=63).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_std_21d_jerk_v037_signal(open, high, low, close):
    p = _park(high, low, 21); g = _gk(open, high, low, close, 21); r = _rs(open, high, low, close, 21)
    b = pd.concat([p, g, r], axis=1).std(axis=1, ddof=0)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_range_30d_jerk_v038_signal(open, high, low, closeadj):
    p = _park(high, low, 30); g = _gk(open, high, low, closeadj, 30); r = _rs(open, high, low, closeadj, 30)
    stk = pd.concat([p, g, r], axis=1); b = stk.max(axis=1) - stk.min(axis=1)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_agree_count_21d_jerk_v039_signal(open, high, low, close):
    p = _park(high, low, 21); g = _gk(open, high, low, close, 21); r = _rs(open, high, low, close, 21)
    a = (p > p.rolling(63, min_periods=32).median()).astype(float)
    c2 = (g > g.rolling(63, min_periods=32).median()).astype(float)
    c3 = (r > r.rolling(63, min_periods=32).median()).astype(float)
    b = (a + c2 + c3).where(p.notna() & g.notna() & r.notna())
    return (b - 2.0 * b.shift(5) + b.shift(2 * 5)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_arctan_zscore_21_60_jerk_v040_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); m = p.rolling(60, min_periods=30).mean(); sd = p.rolling(60, min_periods=30).std(ddof=0)
    b = np.arctan((p - m) / sd.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_tanh_z_14_63_jerk_v041_signal(high, low, close):
    a = _atr_w(high, low, close, 14) / close
    z = (a - a.rolling(63, min_periods=32).mean()) / a.rolling(63, min_periods=32).std(ddof=0).replace(0.0, np.nan)
    b = np.tanh(z)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_sigmoid_pct_60d_jerk_v042_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 60); pct = r.rolling(252, min_periods=126).rank(pct=True)
    b = (1.0 / (1.0 + np.exp(-(pct - 0.5) * 6.0))).where(pct.notna())
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_hl_range_sq_smooth_10d_jerk_v043_signal(high, low):
    b = ((high - low) ** 2 / (4.0 * np.log(2.0))).rolling(10).mean()
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_close_open_skew_60d_jerk_v044_signal(open, close):
    b = np.log(close / open).rolling(60).skew()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_streak_below_q25_jerk_v045_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); q = p.rolling(252, min_periods=126).quantile(0.25)
    b = (q - p) / p.replace(0.0, np.nan)
    j = b - 2.0 * b.shift(63) + b.shift(2 * 63); nrm = b.abs().rolling(63, min_periods=63).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_max_min_ratio_21d_jerk_v046_signal(open, high, low, close):
    p = _park(high, low, 21); g = _gk(open, high, low, close, 21); r = _rs(open, high, low, close, 21)
    stk = pd.concat([p, g, r], axis=1); b = stk.max(axis=1) / stk.min(axis=1).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(5) + b.shift(2 * 5)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_gk_corr_60d_jerk_v047_signal(open, high, low, close):
    lp = np.log(_park(high, low, 5).replace(0.0, np.nan))
    lg = np.log(_gk(open, high, low, close, 5).replace(0.0, np.nan))
    b = lp.rolling(60, min_periods=30).corr(lg)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_max_30d_jerk_v048_signal(open, high, low, closeadj):
    p = _park(high, low, 30); g = _gk(open, high, low, closeadj, 30); r = _rs(open, high, low, closeadj, 30)
    b = pd.concat([p, g, r], axis=1).max(axis=1)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_jump_co_threshold_count_21d_jerk_v049_signal(open, close):
    oc = np.log(close / open); s = oc.rolling(21).std(ddof=0)
    b = (oc.abs() > 2.0 * s).astype(float).where(oc.notna() & s.notna()).rolling(21).sum()
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_wide_bar_park_ratio_30d_jerk_v050_signal(closeadj, high, low):
    _ = closeadj; lr = np.log(high / low); p = _park(high, low, 21)
    b = (lr > 2.0 * p).astype(float).where(lr.notna() & p.notna()).rolling(30).sum()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_close_open_abs_60d_jerk_v051_signal(open, closeadj):
    b = np.log(closeadj / open).abs().rolling(60).mean()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rv_park_gap_42d_jerk_v052_signal(close, high, low):
    b = _rv(close, 42) - _park(high, low, 42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_kurtosis_120d_jerk_v053_signal(open, high, low, closeadj):
    g = _gk(open, high, low, closeadj, 5); b = g.rolling(120, min_periods=60).kurt()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_vol_of_vol_42d_jerk_v054_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 5).rolling(42).std(ddof=0)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_skew_60d_jerk_v055_signal(closeadj, high, low):
    _ = closeadj; b = (np.log(high / low) ** 2).rolling(60).skew()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_streak_above_median_jerk_v056_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 5).rolling(252, min_periods=126).rank(pct=True)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_sign_above_long_jerk_v057_signal(closeadj, high, low):
    _ = closeadj; b = np.sign(_park(high, low, 21) - _park(high, low, 63))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_realized_ratio_60d_jerk_v058_signal(open, closeadj):
    on = np.log(open / closeadj.shift(1)); oc = np.log(closeadj / open)
    b = on.rolling(60).var(ddof=1) / oc.rolling(60).var(ddof=1).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_z_60_252_jerk_v059_signal(high, low, closeadj):
    a = _atr_s(high, low, closeadj, 60) / closeadj
    b = (a - a.rolling(252, min_periods=126).mean()) / a.rolling(252, min_periods=126).std(ddof=0).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_park_ratio_21d_jerk_v060_signal(high, low, close):
    a = _atr_w(high, low, close, 14) / close; p = _park(high, low, 21)
    b = a / p.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_kurt_120d_jerk_v061_signal(open, high, low, closeadj):
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    b = rs.rolling(120).kurt()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_pct_decile_high_flag_120d_jerk_v062_signal(open, high, low, closeadj):
    g = _gk(open, high, low, closeadj, 30); q = g.rolling(120, min_periods=60).quantile(0.8)
    b = (g > q).astype(float).where(g.notna() & q.notna())
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_low_decile_flag_252d_jerk_v063_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 60); q = r.rolling(252, min_periods=126).quantile(0.1)
    b = (r < q).astype(float).where(r.notna() & q.notna())
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_mad_42d_jerk_v064_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 5); med = p.rolling(42).median()
    b = (p - med).abs().rolling(42).median()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_autocorr_21d_jerk_v065_signal(open, high, low, close):
    g = 0.5 * np.log(high / low) ** 2 - (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    m1 = g.rolling(60).mean(); sd = g.rolling(60).std(ddof=0)
    b = ((g * g.shift(1)).rolling(60).mean() - m1 * m1) / (sd * sd).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_overnight_jump_count_60d_jerk_v066_signal(open, closeadj):
    on = np.log(open / closeadj.shift(1)); s = on.rolling(60).std(ddof=0)
    b = (on.abs() > 2.0 * s).astype(float).where(on.notna() & s.notna()).rolling(60).sum()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_dispersion_5_21_63_jerk_v067_signal(closeadj, high, low):
    _ = closeadj
    lp5 = np.log(_park(high, low, 5)); lp21 = np.log(_park(high, low, 21)); lp63 = np.log(_park(high, low, 63))
    b = pd.concat([lp5, lp21, lp63], axis=1).std(axis=1, ddof=0)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_z_8_42_jerk_v068_signal(high, low):
    lr = np.log(high / low)
    b = (lr - lr.rolling(42).mean()) / lr.rolling(42).std(ddof=0).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_park_diff_42d_jerk_v069_signal(open, high, low, closeadj):
    b = _rs(open, high, low, closeadj, 42) - _park(high, low, 42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_log_30d_jerk_v070_signal(high, low, closeadj):
    b = np.log((_atr_s(high, low, closeadj, 30) / closeadj).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_skew_252d_jerk_v071_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 21).rolling(252, min_periods=126).skew()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_bipower_park_ratio_21d_jerk_v072_signal(close, high, low):
    b = _bipow(close, 21) / (_park(high, low, 21) * (21 ** 0.5)).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_pctrank_120d_jerk_v073_signal(open, high, low, closeadj):
    yz = _yz(open, high, low, closeadj, 21); b = yz.rolling(120, min_periods=60).rank(pct=True)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_intraday_oc_std_30d_jerk_v074_signal(open, close):
    b = np.log(close / open).rolling(30).std(ddof=0)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_arctan_slope_42d_jerk_v075_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21)
    b = np.arctan((p - p.shift(42)) / p.abs().rolling(42, min_periods=21).mean().replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_42d_jerk_v076_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_120d_jerk_v077_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 120)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_42d_jerk_v078_signal(open, high, low, closeadj):
    g = _gk(open, high, low, closeadj, 42)
    b = (g / g.rolling(120, min_periods=60).mean().replace(0.0, np.nan)) - 1.0
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_120d_jerk_v079_signal(open, high, low, closeadj):
    b = _rs(open, high, low, closeadj, 120)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_42d_jerk_v080_signal(open, high, low, closeadj):
    b = _yz(open, high, low, closeadj, 42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_rs_signed_diff_60d_jerk_v081_signal(open, high, low, closeadj):
    b = _park(high, low, 60) - _rs(open, high, low, closeadj, 60)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_rs_log_42d_jerk_v082_signal(open, high, low, closeadj):
    g = _gk(open, high, low, closeadj, 42); r = _rs(open, high, low, closeadj, 42)
    b = np.log(g / r.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_gk_diff_30d_jerk_v083_signal(open, high, low, closeadj):
    b = _yz(open, high, low, closeadj, 30) - _gk(open, high, low, closeadj, 30)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_centered_diff_5_42_jerk_v084_signal(closeadj, high, low):
    _ = closeadj; p5 = _park(high, low, 5); p42 = _park(high, low, 42)
    b = (p5 - p42) / p42.replace(0.0, np.nan)
    j = b - 2.0 * b.shift(21) + b.shift(2 * 21); nrm = b.abs().rolling(21, min_periods=21).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_inverse_60d_jerk_v085_signal(closeadj, high, low):
    _ = closeadj; b = 1.0 / _park(high, low, 60).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_negativity_share_42d_jerk_v086_signal(open, high, low, closeadj):
    d = 0.5 * np.log(high / low) ** 2 - (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    b = (d < 0.0).astype(float).where(d.notna()).rolling(42).mean()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_term_21_120_jerk_v087_signal(closeadj, high, low):
    _ = closeadj; b = _park(high, low, 21) - _park(high, low, 120)
    j = b - 2.0 * b.shift(21) + b.shift(2 * 21); nrm = b.abs().rolling(21, min_periods=21).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_term_log_30_120_jerk_v088_signal(open, high, low, closeadj):
    g30 = _gk(open, high, low, closeadj, 30); g120 = _gk(open, high, low, closeadj, 120)
    b = np.log(g30 / g120.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_slope_42d_jerk_v089_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 21); b = r - r.shift(42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_slope_30d_jerk_v090_signal(high, low, closeadj):
    a = _atr_s(high, low, closeadj, 30) / closeadj; b = a - a.shift(30)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_accel_42d_jerk_v091_signal(open, high, low, closeadj):
    yz = _yz(open, high, low, closeadj, 21); b = yz - 2.0 * yz.shift(21) + yz.shift(42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_park_rank_diff_63d_jerk_v092_signal(open, high, low, closeadj):
    p = _park(high, low, 21); g = _gk(open, high, low, closeadj, 21)
    b = g.rolling(63, min_periods=32).rank(pct=True) - p.rolling(63, min_periods=32).rank(pct=True)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_cv_60d_jerk_v093_signal(open, high, low, closeadj):
    p = _park(high, low, 60); g = _gk(open, high, low, closeadj, 60); r = _rs(open, high, low, closeadj, 60)
    a = _atr_s(high, low, closeadj, 60) / closeadj
    stk = pd.concat([p, g, r, a], axis=1); b = stk.std(axis=1, ddof=0) / stk.mean(axis=1).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_above_long_count_60d_jerk_v094_signal(closeadj, high, low):
    _ = closeadj; p5 = _park(high, low, 5); p60 = _park(high, low, 60)
    b = (p5 > p60).astype(float).where(p5.notna() & p60.notna()).rolling(60).sum()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_high_low_streak_diff_jerk_v095_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 30); q90 = r.rolling(252, min_periods=126).quantile(0.9); q10 = r.rolling(252, min_periods=126).quantile(0.1)
    b = (r - 0.5 * (q90 + q10)) / (q90 - q10).replace(0.0, np.nan)
    j = b - 2.0 * b.shift(63) + b.shift(2 * 63); nrm = b.abs().rolling(63, min_periods=63).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_realized_corr_60d_jerk_v096_signal(close, high, low):
    b = np.log(high / low).rolling(60, min_periods=30).corr(np.log(close / close.shift(1)).abs())
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_realized_corr_120d_jerk_v097_signal(closeadj, high, low):
    p5 = np.log(_park(high, low, 5).replace(0.0, np.nan)); rv5 = np.log(_rv(closeadj, 5).replace(0.0, np.nan))
    b = p5.rolling(120, min_periods=60).corr(rv5)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_overnight_share_pctrank_120d_jerk_v098_signal(open, high, low, closeadj):
    on = np.log(open / closeadj.shift(1)); oc = np.log(closeadj / open)
    von = on.rolling(30).var(ddof=1); voc = oc.rolling(30).var(ddof=1)
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs.rolling(30).mean(); k = 0.34 / (1.34 + 31.0 / 29.0)
    yzv = (von + k * voc + (1 - k) * vrs).clip(lower=0.0)
    b = (von / yzv.replace(0.0, np.nan)).rolling(120, min_periods=60).rank(pct=True)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_above_park_streak_jerk_v099_signal(open, high, low, close):
    g = _gk(open, high, low, close, 21); p = _park(high, low, 21)
    b = np.log(g.replace(0.0, np.nan)) - np.log(p.replace(0.0, np.nan))
    return (b - 2.0 * b.shift(5) + b.shift(2 * 5)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_dayssince_atr_high_252d_jerk_v100_signal(high, low, closeadj):
    base = _atr_s(high, low, closeadj, 21) / closeadj; q = base.rolling(252, min_periods=126).quantile(0.9)
    b = (base - q) / q.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_mean_252d_jerk_v101_signal(closeadj, high, low):
    _ = closeadj; b = np.log(high / low).rolling(252, min_periods=126).mean()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_skew_120d_jerk_v102_signal(high, low):
    b = np.log(high / low).rolling(120, min_periods=60).skew()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_kurt_120d_jerk_v103_signal(high, low):
    b = np.log(high / low).rolling(120, min_periods=60).kurt()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_oc_log_kurt_120d_jerk_v104_signal(open, closeadj):
    b = np.log(closeadj / open).rolling(120, min_periods=60).kurt()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_bipower_42d_jerk_v105_signal(closeadj):
    b = _bipow(closeadj, 42)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_jump_share_21d_jerk_v106_signal(close):
    r = np.log(close / close.shift(1)); bp = r.abs() * r.abs().shift(1) * (np.pi / 2.0)
    b = (1.0 - bp.rolling(21).sum() / (r ** 2).rolling(21).sum().replace(0.0, np.nan)).clip(lower=0.0)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_bipower_park_diff_30d_jerk_v107_signal(closeadj, high, low):
    b = _bipow(closeadj, 30) - _park(high, low, 30) * (30 ** 0.5)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_ema_60d_jerk_v108_signal(high, low, closeadj):
    tr = _tr(high, low, closeadj)
    b = tr.ewm(span=60, adjust=False, min_periods=60).mean() / closeadj
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_30d_jerk_v109_signal(high, low, closeadj):
    base = _atr_w(high, low, closeadj, 14) / closeadj; b = (base / base.shift(30)) - 1.0
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_truerange_gap_share_60d_jerk_v110_signal(high, low, closeadj):
    gap = pd.concat([(high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    b = (gap / (high - low).replace(0.0, np.nan)).rolling(60, min_periods=30).mean()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_range_vs_absret_5d_jerk_v111_signal(close, high, low):
    b = (np.log(high / low) - np.log(close / close.shift(1)).abs()).rolling(5).mean()
    return (b - 2.0 * b.shift(5) + b.shift(2 * 5)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_efficiency_30d_jerk_v112_signal(closeadj, high, low):
    b = np.log(closeadj / closeadj.shift(30)).abs() / np.log(high / low).rolling(30).sum().replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_hl_sq_share_in_gk_30d_jerk_v113_signal(open, high, low, closeadj):
    hl_part = (0.5 * np.log(high / low) ** 2).rolling(30).mean()
    gk_var = (0.5 * np.log(high / low) ** 2 - (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2).rolling(30).mean()
    b = hl_part / gk_var.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_co_sq_in_park_42d_jerk_v114_signal(closeadj, open, high, low):
    co_sq = (np.log(closeadj / open) ** 2).rolling(42).mean()
    pv = (np.log(high / low) ** 2).rolling(42).mean() / (4.0 * np.log(2.0))
    b = co_sq / pv.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_sign_park_change_30d_jerk_v115_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); b = np.sign(p - p.shift(30))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_sign_gk_minus_park_42d_jerk_v116_signal(open, high, low, closeadj):
    b = np.sign(_gk(open, high, low, closeadj, 42) - _park(high, low, 42))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_park_logratio_60d_jerk_v117_signal(high, low, closeadj):
    a = _atr_w(high, low, closeadj, 14) / closeadj; p = _park(high, low, 14)
    b = (np.log(a.replace(0.0, np.nan)) - np.log(p.replace(0.0, np.nan))).rolling(60).mean()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_logvol_tanh_zscore_252d_jerk_v118_signal(closeadj, high, low):
    _ = closeadj; lp = np.log(_park(high, low, 63).replace(0.0, np.nan))
    b = np.tanh((lp - lp.rolling(252, min_periods=126).mean()) / lp.rolling(252, min_periods=126).std(ddof=0).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_sigmoid_pctrank_120d_jerk_v119_signal(open, high, low, closeadj):
    pct = _gk(open, high, low, closeadj, 42).rolling(120, min_periods=60).rank(pct=True)
    b = (1.0 / (1.0 + np.exp(-(pct - 0.5) * 8.0))).where(pct.notna())
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_arctan_pctchange_60d_jerk_v120_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 30); b = np.arctan((r / r.shift(60)) - 1.0)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_autocorr_120d_jerk_v121_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 5)
    m1 = p.rolling(120).mean(); sd = p.rolling(120).std(ddof=0)
    b = ((p * p.shift(1)).rolling(120).mean() - m1 * m1) / (sd * sd).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_autocorr_lag5_60d_jerk_v122_signal(open, high, low, close):
    rs = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    m1 = rs.rolling(60).mean(); sd = rs.rolling(60).std(ddof=0)
    b = ((rs * rs.shift(5)).rolling(60).mean() - m1 * m1) / (sd * sd).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_demean_42d_jerk_v123_signal(high, low):
    lr = np.log(high / low); m = lr.rolling(42).mean(); b = (lr - m) * m.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_logsq_acf_lag10_60d_jerk_v124_signal(closeadj, high, low):
    _ = closeadj; lp = np.log(_park(high, low, 5).replace(0.0, np.nan))
    m = lp.rolling(60).mean(); sd = lp.rolling(60).std(ddof=0)
    b = ((lp * lp.shift(10)).rolling(60).mean() - m * m) / (sd * sd).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_q75_q25_ratio_120d_jerk_v125_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 5)
    b = p.rolling(120, min_periods=60).quantile(0.75) / p.rolling(120, min_periods=60).quantile(0.25).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_median_252d_jerk_v126_signal(high, low, closeadj):
    b = (_atr_s(high, low, closeadj, 21) / closeadj).rolling(252, min_periods=126).median()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_252d_jerk_v127_signal(open, high, low, closeadj):
    b = _rs(open, high, low, closeadj, 252)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_120d_jerk_v128_signal(open, high, low, closeadj):
    b = _yz(open, high, low, closeadj, 120)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_log_velocity_42d_jerk_v129_signal(closeadj, high, low):
    _ = closeadj; lp = np.log(_park(high, low, 42).replace(0.0, np.nan)); b = lp - lp.shift(10)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_velocity_30_5d_jerk_v130_signal(open, high, low, close):
    g = _gk(open, high, low, close, 10); b = g - g.shift(5)
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_above_120d_median_flag_jerk_v131_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 42)
    b = (p > p.rolling(120, min_periods=60).median()).astype(float).where(p.notna())
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_in_quintile_252d_jerk_v132_signal(high, low, closeadj):
    base = _atr_s(high, low, closeadj, 21) / closeadj
    b = np.floor(base.rolling(252, min_periods=126).rank(pct=True) * 5.0).clip(upper=4.0)
    j = b - 2.0 * b.shift(21) + b.shift(2 * 21); nrm = b.abs().rolling(21, min_periods=21).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_z_30_252_jerk_v133_signal(open, high, low, closeadj):
    yz = _yz(open, high, low, closeadj, 30)
    b = (yz - yz.rolling(252, min_periods=126).mean()) / yz.rolling(252, min_periods=126).std(ddof=0).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_z_42_120_jerk_v134_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 42)
    b = (r - r.rolling(120, min_periods=60).mean()) / r.rolling(120, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_weighted_estimator_30d_jerk_v135_signal(open, high, low, closeadj):
    p = _park(high, low, 30); g = _gk(open, high, low, closeadj, 30); r = _rs(open, high, low, closeadj, 30)
    w = 0.4 * p + 0.3 * g + 0.3 * r
    b = (w / w.rolling(60, min_periods=30).mean().replace(0.0, np.nan)) - 1.0
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_estimator_logspread_30d_jerk_v136_signal(open, high, low, closeadj):
    p = _park(high, low, 30); g = _gk(open, high, low, closeadj, 30); r = _rs(open, high, low, closeadj, 30)
    stk = pd.concat([p, g, r], axis=1)
    b = np.log(stk.max(axis=1).replace(0.0, np.nan)) - np.log(stk.min(axis=1).replace(0.0, np.nan))
    return (b - 2.0 * b.shift(10) + b.shift(2 * 10)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_overnight_skew_120d_jerk_v137_signal(open, closeadj):
    b = np.log(open / closeadj.shift(1)).rolling(120, min_periods=60).skew()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_var_ratio_60d_jerk_v138_signal(open, closeadj):
    on = np.log(open / closeadj.shift(1)); oc = np.log(closeadj / open)
    b = np.log(on.rolling(60).var(ddof=1).replace(0.0, np.nan)) - np.log(oc.rolling(60).var(ddof=1).replace(0.0, np.nan))
    j = b - 2.0 * b.shift(10) + b.shift(2 * 10); nrm = b.abs().rolling(10, min_periods=10).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_concavity_5_21_63_jerk_v139_signal(closeadj, high, low):
    _ = closeadj
    lp5 = np.log(_park(high, low, 5).replace(0.0, np.nan))
    lp21 = np.log(_park(high, low, 21).replace(0.0, np.nan))
    lp63 = np.log(_park(high, low, 63).replace(0.0, np.nan))
    b = lp21 - 0.5 * (lp5 + lp63)
    j = b - 2.0 * b.shift(10) + b.shift(2 * 10); nrm = b.abs().rolling(10, min_periods=10).mean()
    return (j / nrm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_term_30_120_jerk_v140_signal(open, high, low, closeadj):
    b = _rs(open, high, low, closeadj, 30) / _rs(open, high, low, closeadj, 120).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_logrange_mad_60d_jerk_v141_signal(high, low):
    lr = np.log(high / low); med = lr.rolling(60).median()
    b = (lr - med).abs().rolling(60).median()
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_co_logsq_mean_120d_jerk_v142_signal(open, closeadj):
    b = (np.log(closeadj / open) ** 2).rolling(120, min_periods=60).mean()
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_corr_120d_jerk_v143_signal(open, closeadj):
    on = np.log(open / closeadj.shift(1)); oc = np.log(closeadj / open)
    b = on.rolling(120, min_periods=60).corr(oc)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_pct_change_120d_jerk_v144_signal(closeadj, high, low):
    _ = closeadj; p = _park(high, low, 21); b = (p / p.shift(120)) - 1.0
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_60d_jerk_v145_signal(high, low, closeadj):
    base = _atr_s(high, low, closeadj, 21) / closeadj; b = (base / base.shift(60)) - 1.0
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_rs_pct_change_arctan_60d_jerk_v146_signal(open, high, low, closeadj):
    r = _rs(open, high, low, closeadj, 60); b = np.arctan(((r / r.shift(60)) - 1.0) * 5.0)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_yz_oc_share_42d_jerk_v147_signal(open, high, low, closeadj):
    on = np.log(open / closeadj.shift(1)); oc = np.log(closeadj / open)
    von = on.rolling(42).var(ddof=1); voc = oc.rolling(42).var(ddof=1)
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs.rolling(42).mean(); k = 0.34 / (1.34 + 43.0 / 41.0)
    yzv = (von + k * voc + (1 - k) * vrs).clip(lower=0.0)
    b = (k * voc) / yzv.replace(0.0, np.nan)
    return (b - 2.0 * b.shift(21) + b.shift(2 * 21)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_bipower_z_30_120_jerk_v148_signal(closeadj):
    base = _bipow(closeadj, 30)
    b = (base - base.rolling(120, min_periods=60).mean()) / base.rolling(120, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_park_atr_log_pctrank_120d_jerk_v149_signal(high, low, closeadj):
    p = _park(high, low, 5); a = _atr_w(high, low, closeadj, 14) / closeadj
    b = (np.log(p.replace(0.0, np.nan)) - np.log(a.replace(0.0, np.nan))).rolling(120, min_periods=60).rank(pct=True)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

def f18pg_f18_parkinson_garman_klass_estimators_gk_rs_corr_120d_jerk_v150_signal(open, high, low, closeadj):
    lg = np.log(_gk(open, high, low, closeadj, 5).replace(0.0, np.nan))
    lr = np.log(_rs(open, high, low, closeadj, 5).replace(0.0, np.nan))
    b = lg.rolling(120, min_periods=60).corr(lr)
    return (b - 2.0 * b.shift(63) + b.shift(2 * 63)).replace([np.inf, -np.inf], np.nan)

f18_parkinson_garman_klass_estimators_jerk_001_150_REGISTRY = {}
def _add(f, *cols): f18_parkinson_garman_klass_estimators_jerk_001_150_REGISTRY[f.__name__] = {"inputs": list(cols), "func": f}
_add(f18pg_f18_parkinson_garman_klass_estimators_park_5d_jerk_v001_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_log_21d_jerk_v002_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_63d_jerk_v003_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_252d_jerk_v004_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_10d_jerk_v005_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_log_30d_jerk_v006_signal,"open","high","low","close","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_14d_jerk_v007_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_60d_jerk_v008_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_21d_jerk_v009_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_63d_jerk_v010_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_gk_ratio_21d_jerk_v011_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_rs_ratio_30d_jerk_v012_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_rs_diff_21d_jerk_v013_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_minus_realized_log_63d_jerk_v014_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_realized_ratio_21d_jerk_v015_signal,"high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_wilder_14d_jerk_v016_signal,"high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_sma_50d_jerk_v017_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_sma_8d_jerk_v018_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_z_60_252_jerk_v019_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_q90_dist_120d_jerk_v020_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_z_21_252_jerk_v021_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_pctrank_252d_jerk_v022_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_park_log_ratio_60d_jerk_v023_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_term_5_21_jerk_v024_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_term_log_21_63_jerk_v025_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_park_cross_21d_jerk_v026_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_slope_21d_jerk_v027_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_slope_30d_jerk_v028_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_accel_21d_jerk_v029_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_bipower_21d_jerk_v030_signal,"close")
_add(f18pg_f18_parkinson_garman_klass_estimators_bipower_realized_ratio_60d_jerk_v031_signal,"closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_share_30d_jerk_v032_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_oc_var_21d_jerk_v033_signal,"open","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_p90_flag_252d_jerk_v034_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_iqr_60d_jerk_v035_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_dayssince_parkp95_252d_jerk_v036_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_std_21d_jerk_v037_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_range_30d_jerk_v038_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_agree_count_21d_jerk_v039_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_arctan_zscore_21_60_jerk_v040_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_tanh_z_14_63_jerk_v041_signal,"high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_sigmoid_pct_60d_jerk_v042_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_hl_range_sq_smooth_10d_jerk_v043_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_close_open_skew_60d_jerk_v044_signal,"open","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_streak_below_q25_jerk_v045_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_max_min_ratio_21d_jerk_v046_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_gk_corr_60d_jerk_v047_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_max_30d_jerk_v048_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_jump_co_threshold_count_21d_jerk_v049_signal,"open","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_wide_bar_park_ratio_30d_jerk_v050_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_close_open_abs_60d_jerk_v051_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rv_park_gap_42d_jerk_v052_signal,"close","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_kurtosis_120d_jerk_v053_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_vol_of_vol_42d_jerk_v054_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_skew_60d_jerk_v055_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_streak_above_median_jerk_v056_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_sign_above_long_jerk_v057_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_realized_ratio_60d_jerk_v058_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_z_60_252_jerk_v059_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_park_ratio_21d_jerk_v060_signal,"high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_kurt_120d_jerk_v061_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_pct_decile_high_flag_120d_jerk_v062_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_low_decile_flag_252d_jerk_v063_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_mad_42d_jerk_v064_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_autocorr_21d_jerk_v065_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_overnight_jump_count_60d_jerk_v066_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_dispersion_5_21_63_jerk_v067_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_z_8_42_jerk_v068_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_park_diff_42d_jerk_v069_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_log_30d_jerk_v070_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_skew_252d_jerk_v071_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_bipower_park_ratio_21d_jerk_v072_signal,"close","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_pctrank_120d_jerk_v073_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_intraday_oc_std_30d_jerk_v074_signal,"open","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_arctan_slope_42d_jerk_v075_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_42d_jerk_v076_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_120d_jerk_v077_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_42d_jerk_v078_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_120d_jerk_v079_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_42d_jerk_v080_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_rs_signed_diff_60d_jerk_v081_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_rs_log_42d_jerk_v082_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_gk_diff_30d_jerk_v083_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_centered_diff_5_42_jerk_v084_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_inverse_60d_jerk_v085_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_negativity_share_42d_jerk_v086_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_term_21_120_jerk_v087_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_term_log_30_120_jerk_v088_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_slope_42d_jerk_v089_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_slope_30d_jerk_v090_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_accel_42d_jerk_v091_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_park_rank_diff_63d_jerk_v092_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_cv_60d_jerk_v093_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_above_long_count_60d_jerk_v094_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_high_low_streak_diff_jerk_v095_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_realized_corr_60d_jerk_v096_signal,"close","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_realized_corr_120d_jerk_v097_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_overnight_share_pctrank_120d_jerk_v098_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_above_park_streak_jerk_v099_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_dayssince_atr_high_252d_jerk_v100_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_mean_252d_jerk_v101_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_skew_120d_jerk_v102_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_kurt_120d_jerk_v103_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_oc_log_kurt_120d_jerk_v104_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_bipower_42d_jerk_v105_signal,"closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_jump_share_21d_jerk_v106_signal,"close")
_add(f18pg_f18_parkinson_garman_klass_estimators_bipower_park_diff_30d_jerk_v107_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_ema_60d_jerk_v108_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_30d_jerk_v109_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_truerange_gap_share_60d_jerk_v110_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_range_vs_absret_5d_jerk_v111_signal,"close","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_efficiency_30d_jerk_v112_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_hl_sq_share_in_gk_30d_jerk_v113_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_co_sq_in_park_42d_jerk_v114_signal,"closeadj","open","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_sign_park_change_30d_jerk_v115_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_sign_gk_minus_park_42d_jerk_v116_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_park_logratio_60d_jerk_v117_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_logvol_tanh_zscore_252d_jerk_v118_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_sigmoid_pctrank_120d_jerk_v119_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_arctan_pctchange_60d_jerk_v120_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_autocorr_120d_jerk_v121_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_autocorr_lag5_60d_jerk_v122_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_demean_42d_jerk_v123_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_logsq_acf_lag10_60d_jerk_v124_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_q75_q25_ratio_120d_jerk_v125_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_median_252d_jerk_v126_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_252d_jerk_v127_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_120d_jerk_v128_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_log_velocity_42d_jerk_v129_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_velocity_30_5d_jerk_v130_signal,"open","high","low","close")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_above_120d_median_flag_jerk_v131_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_in_quintile_252d_jerk_v132_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_z_30_252_jerk_v133_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_z_42_120_jerk_v134_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_weighted_estimator_30d_jerk_v135_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_estimator_logspread_30d_jerk_v136_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_overnight_skew_120d_jerk_v137_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_var_ratio_60d_jerk_v138_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_concavity_5_21_63_jerk_v139_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_term_30_120_jerk_v140_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_logrange_mad_60d_jerk_v141_signal,"high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_co_logsq_mean_120d_jerk_v142_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_overnight_intraday_corr_120d_jerk_v143_signal,"open","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_pct_change_120d_jerk_v144_signal,"closeadj","high","low")
_add(f18pg_f18_parkinson_garman_klass_estimators_atr_pct_change_60d_jerk_v145_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_rs_pct_change_arctan_60d_jerk_v146_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_yz_oc_share_42d_jerk_v147_signal,"open","high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_bipower_z_30_120_jerk_v148_signal,"closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_park_atr_log_pctrank_120d_jerk_v149_signal,"high","low","closeadj")
_add(f18pg_f18_parkinson_garman_klass_estimators_gk_rs_corr_120d_jerk_v150_signal,"open","high","low","closeadj")
REG = f18_parkinson_garman_klass_estimators_jerk_001_150_REGISTRY


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in REG.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b2 in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b2}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
