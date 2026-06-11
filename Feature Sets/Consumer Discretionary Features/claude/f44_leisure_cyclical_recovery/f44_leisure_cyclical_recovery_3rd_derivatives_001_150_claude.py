import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


def _f44_revenue_recovery(revenue, w):
    trough = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - trough) / trough.replace(0, np.nan).abs()


def _f44_margin_recovery(ebitdamargin, w):
    trough = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - trough


def _f44_recovery_strength(revenue, ebitda, w):
    rev_t = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    ebt_t = ebitda.rolling(w, min_periods=max(1, w // 2)).min()
    return ((revenue - rev_t) / rev_t.replace(0, np.nan).abs()
            + (ebitda - ebt_t) / ebt_t.replace(0, np.nan).abs())


def f44lcr_f44_leisure_cyclical_recovery_rrec_5d_jerk_v001_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_5d_jerk_v002_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_5d_jerk_v003_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_10d_jerk_v004_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_10d_jerk_v005_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_10d_jerk_v006_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_21d_jerk_v007_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_21d_jerk_v008_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_21d_jerk_v009_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_42d_jerk_v010_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_42d_jerk_v011_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_42d_jerk_v012_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_63d_jerk_v013_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_63d_jerk_v014_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_63d_jerk_v015_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_126d_jerk_v016_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_126d_jerk_v017_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_126d_jerk_v018_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_189d_jerk_v019_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_189d_jerk_v020_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_189d_jerk_v021_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_252d_jerk_v022_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_252d_jerk_v023_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_252d_jerk_v024_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_378d_jerk_v025_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_378d_jerk_v026_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_378d_jerk_v027_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_504d_jerk_v028_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_504d_jerk_v029_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_504d_jerk_v030_signal(revenue, closeadj):
    base = _f44_revenue_recovery(revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_jerk_v031_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 5)
    base = _ema(r, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_jerk_v032_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 5)
    base = _ema(r, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_jerk_v033_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 5)
    base = _ema(r, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_jerk_v034_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 10)
    base = _ema(r, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_jerk_v035_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 10)
    base = _ema(r, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_jerk_v036_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 10)
    base = _ema(r, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_jerk_v037_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 21)
    base = _ema(r, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_jerk_v038_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 21)
    base = _ema(r, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_jerk_v039_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 21)
    base = _ema(r, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_jerk_v040_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 42)
    base = _ema(r, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_jerk_v041_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 42)
    base = _ema(r, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_jerk_v042_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 42)
    base = _ema(r, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_jerk_v043_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    base = _ema(r, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_jerk_v044_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    base = _ema(r, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_jerk_v045_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    base = _ema(r, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_jerk_v046_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 126)
    base = _ema(r, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_jerk_v047_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 126)
    base = _ema(r, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_jerk_v048_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 126)
    base = _ema(r, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_jerk_v049_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 189)
    base = _ema(r, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_jerk_v050_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 189)
    base = _ema(r, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_jerk_v051_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 189)
    base = _ema(r, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_jerk_v052_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    base = _ema(r, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_jerk_v053_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    base = _ema(r, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_jerk_v054_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    base = _ema(r, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_jerk_v055_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 378)
    base = _ema(r, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_jerk_v056_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 378)
    base = _ema(r, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_jerk_v057_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 378)
    base = _ema(r, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_jerk_v058_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    base = _ema(r, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_jerk_v059_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    base = _ema(r, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_jerk_v060_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    base = _ema(r, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_5d_jerk_v061_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_5d_jerk_v062_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_5d_jerk_v063_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_10d_jerk_v064_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_10d_jerk_v065_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_10d_jerk_v066_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_21d_jerk_v067_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_21d_jerk_v068_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_21d_jerk_v069_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_42d_jerk_v070_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_42d_jerk_v071_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_42d_jerk_v072_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_63d_jerk_v073_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_63d_jerk_v074_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_63d_jerk_v075_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_126d_jerk_v076_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_126d_jerk_v077_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_126d_jerk_v078_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_189d_jerk_v079_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_189d_jerk_v080_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_189d_jerk_v081_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_252d_jerk_v082_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_252d_jerk_v083_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_252d_jerk_v084_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_378d_jerk_v085_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_378d_jerk_v086_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_378d_jerk_v087_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_504d_jerk_v088_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_504d_jerk_v089_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_504d_jerk_v090_signal(ebitdamargin, closeadj):
    base = _f44_margin_recovery(ebitdamargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_jerk_v091_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 5)
    base = _ema(m, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_jerk_v092_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 5)
    base = _ema(m, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_jerk_v093_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 5)
    base = _ema(m, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_jerk_v094_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 10)
    base = _ema(m, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_jerk_v095_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 10)
    base = _ema(m, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_jerk_v096_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 10)
    base = _ema(m, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_jerk_v097_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 21)
    base = _ema(m, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_jerk_v098_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 21)
    base = _ema(m, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_jerk_v099_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 21)
    base = _ema(m, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_jerk_v100_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 42)
    base = _ema(m, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_jerk_v101_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 42)
    base = _ema(m, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_jerk_v102_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 42)
    base = _ema(m, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_jerk_v103_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    base = _ema(m, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_jerk_v104_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    base = _ema(m, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_jerk_v105_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    base = _ema(m, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_jerk_v106_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 126)
    base = _ema(m, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_jerk_v107_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 126)
    base = _ema(m, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_jerk_v108_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 126)
    base = _ema(m, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_jerk_v109_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 189)
    base = _ema(m, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_jerk_v110_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 189)
    base = _ema(m, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_jerk_v111_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 189)
    base = _ema(m, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_jerk_v112_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    base = _ema(m, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_jerk_v113_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    base = _ema(m, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_jerk_v114_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    base = _ema(m, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_jerk_v115_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 378)
    base = _ema(m, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_jerk_v116_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 378)
    base = _ema(m, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_jerk_v117_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 378)
    base = _ema(m, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_jerk_v118_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 504)
    base = _ema(m, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_jerk_v119_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 504)
    base = _ema(m, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_jerk_v120_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 504)
    base = _ema(m, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_5d_jerk_v121_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_5d_jerk_v122_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_5d_jerk_v123_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_10d_jerk_v124_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_10d_jerk_v125_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_10d_jerk_v126_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_21d_jerk_v127_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_21d_jerk_v128_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_21d_jerk_v129_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_42d_jerk_v130_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_42d_jerk_v131_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_42d_jerk_v132_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_63d_jerk_v133_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_63d_jerk_v134_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_63d_jerk_v135_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_126d_jerk_v136_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_126d_jerk_v137_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_126d_jerk_v138_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_189d_jerk_v139_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_189d_jerk_v140_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_189d_jerk_v141_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_252d_jerk_v142_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_252d_jerk_v143_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_252d_jerk_v144_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_378d_jerk_v145_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_378d_jerk_v146_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_378d_jerk_v147_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_504d_jerk_v148_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_504d_jerk_v149_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_504d_jerk_v150_signal(revenue, ebitda, closeadj):
    base = _f44_recovery_strength(revenue, ebitda, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44lcr_f44_leisure_cyclical_recovery_rrec_5d_jerk_v001_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_5d_jerk_v002_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_5d_jerk_v003_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_10d_jerk_v004_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_10d_jerk_v005_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_10d_jerk_v006_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_21d_jerk_v007_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_21d_jerk_v008_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_21d_jerk_v009_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_42d_jerk_v010_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_42d_jerk_v011_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_42d_jerk_v012_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_63d_jerk_v013_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_63d_jerk_v014_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_63d_jerk_v015_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_126d_jerk_v016_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_126d_jerk_v017_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_126d_jerk_v018_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_189d_jerk_v019_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_189d_jerk_v020_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_189d_jerk_v021_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_252d_jerk_v022_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_252d_jerk_v023_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_252d_jerk_v024_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_378d_jerk_v025_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_378d_jerk_v026_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_378d_jerk_v027_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_504d_jerk_v028_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_504d_jerk_v029_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_504d_jerk_v030_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_jerk_v031_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_jerk_v032_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_jerk_v033_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_jerk_v034_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_jerk_v035_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_jerk_v036_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_jerk_v037_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_jerk_v038_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_jerk_v039_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_jerk_v040_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_jerk_v041_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_jerk_v042_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_jerk_v043_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_jerk_v044_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_jerk_v045_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_jerk_v046_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_jerk_v047_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_jerk_v048_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_jerk_v049_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_jerk_v050_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_jerk_v051_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_jerk_v052_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_jerk_v053_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_jerk_v054_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_jerk_v055_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_jerk_v056_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_jerk_v057_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_jerk_v058_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_jerk_v059_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_jerk_v060_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_5d_jerk_v061_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_5d_jerk_v062_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_5d_jerk_v063_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_10d_jerk_v064_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_10d_jerk_v065_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_10d_jerk_v066_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_21d_jerk_v067_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_21d_jerk_v068_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_21d_jerk_v069_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_42d_jerk_v070_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_42d_jerk_v071_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_42d_jerk_v072_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_63d_jerk_v073_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_63d_jerk_v074_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_63d_jerk_v075_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_126d_jerk_v076_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_126d_jerk_v077_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_126d_jerk_v078_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_189d_jerk_v079_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_189d_jerk_v080_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_189d_jerk_v081_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_252d_jerk_v082_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_252d_jerk_v083_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_252d_jerk_v084_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_378d_jerk_v085_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_378d_jerk_v086_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_378d_jerk_v087_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_504d_jerk_v088_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_504d_jerk_v089_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_504d_jerk_v090_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_jerk_v091_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_jerk_v092_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_jerk_v093_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_jerk_v094_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_jerk_v095_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_jerk_v096_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_jerk_v097_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_jerk_v098_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_jerk_v099_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_jerk_v100_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_jerk_v101_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_jerk_v102_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_jerk_v103_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_jerk_v104_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_jerk_v105_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_jerk_v106_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_jerk_v107_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_jerk_v108_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_jerk_v109_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_jerk_v110_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_jerk_v111_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_jerk_v112_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_jerk_v113_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_jerk_v114_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_jerk_v115_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_jerk_v116_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_jerk_v117_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_jerk_v118_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_jerk_v119_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_jerk_v120_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_5d_jerk_v121_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_5d_jerk_v122_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_5d_jerk_v123_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_10d_jerk_v124_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_10d_jerk_v125_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_10d_jerk_v126_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_21d_jerk_v127_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_21d_jerk_v128_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_21d_jerk_v129_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_42d_jerk_v130_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_42d_jerk_v131_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_42d_jerk_v132_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_63d_jerk_v133_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_63d_jerk_v134_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_63d_jerk_v135_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_126d_jerk_v136_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_126d_jerk_v137_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_126d_jerk_v138_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_189d_jerk_v139_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_189d_jerk_v140_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_189d_jerk_v141_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_252d_jerk_v142_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_252d_jerk_v143_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_252d_jerk_v144_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_378d_jerk_v145_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_378d_jerk_v146_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_378d_jerk_v147_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_504d_jerk_v148_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_504d_jerk_v149_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_LEISURE_CYCLICAL_RECOVERY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series((closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))).values, name="high")
    low = pd.Series((closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))).values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = { "closeadj": closeadj, "high": high, "low": low, "volume": volume, "revenue": revenue, "ebitda": ebitda, "ebitdamargin": ebitdamargin }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f44_revenue_recovery", "_f44_margin_recovery", "_f44_recovery_strength")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK leisure_cyclical_recovery_3rd_derivatives_001_150_claude: {n_features} features pass")
