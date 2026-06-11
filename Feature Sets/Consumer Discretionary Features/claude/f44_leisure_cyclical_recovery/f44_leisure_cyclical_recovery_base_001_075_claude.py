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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


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


def f44lcr_f44_leisure_cyclical_recovery_rrec_5d_base_v001_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_10d_base_v002_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_21d_base_v003_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_42d_base_v004_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_63d_base_v005_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_126d_base_v006_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_189d_base_v007_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_252d_base_v008_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_378d_base_v009_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrec_504d_base_v010_signal(revenue, closeadj):
    result = _f44_revenue_recovery(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_base_v011_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 5)
    result = _ema(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_base_v012_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 10)
    result = _ema(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_base_v013_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 21)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_base_v014_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 42)
    result = _ema(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_base_v015_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _ema(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_base_v016_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 126)
    result = _ema(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_base_v017_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 189)
    result = _ema(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_base_v018_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 252)
    result = _ema(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_base_v019_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 378)
    result = _ema(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_base_v020_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 504)
    result = _ema(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_5d_base_v021_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_10d_base_v022_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_21d_base_v023_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_42d_base_v024_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_63d_base_v025_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_126d_base_v026_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_189d_base_v027_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_252d_base_v028_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_378d_base_v029_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrec_504d_base_v030_signal(ebitdamargin, closeadj):
    result = _f44_margin_recovery(ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_base_v031_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 5)
    result = _ema(m, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_base_v032_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 10)
    result = _ema(m, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_base_v033_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 21)
    result = _ema(m, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_base_v034_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 42)
    result = _ema(m, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_base_v035_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _ema(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_base_v036_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 126)
    result = _ema(m, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_base_v037_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 189)
    result = _ema(m, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_base_v038_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 252)
    result = _ema(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_base_v039_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 378)
    result = _ema(m, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_base_v040_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 504)
    result = _ema(m, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_5d_base_v041_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_10d_base_v042_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_21d_base_v043_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_42d_base_v044_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_63d_base_v045_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_126d_base_v046_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_189d_base_v047_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_252d_base_v048_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_378d_base_v049_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstr_504d_base_v050_signal(revenue, ebitda, closeadj):
    result = _f44_recovery_strength(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_5d_base_v051_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 5)
    result = _ema(r, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_10d_base_v052_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 10)
    result = _ema(r, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_21d_base_v053_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 21)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_42d_base_v054_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 42)
    result = _ema(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_63d_base_v055_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 63)
    result = _ema(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_126d_base_v056_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 126)
    result = _ema(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_189d_base_v057_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 189)
    result = _ema(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_252d_base_v058_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 252)
    result = _ema(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_378d_base_v059_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 378)
    result = _ema(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rstrema_504d_base_v060_signal(revenue, ebitda, closeadj):
    r = _f44_recovery_strength(revenue, ebitda, 504)
    result = _ema(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_21d_base_v061_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_42d_base_v062_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_63d_base_v063_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_126d_base_v064_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_189d_base_v065_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_252d_base_v066_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_378d_base_v067_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_rrecz_504d_base_v068_signal(revenue, closeadj):
    r = _f44_revenue_recovery(revenue, 63)
    result = _z(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_21d_base_v069_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_42d_base_v070_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_63d_base_v071_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_126d_base_v072_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_189d_base_v073_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_252d_base_v074_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f44lcr_f44_leisure_cyclical_recovery_mrecz_378d_base_v075_signal(ebitdamargin, closeadj):
    m = _f44_margin_recovery(ebitdamargin, 63)
    result = _z(m, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44lcr_f44_leisure_cyclical_recovery_rrec_5d_base_v001_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_10d_base_v002_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_21d_base_v003_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_42d_base_v004_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_63d_base_v005_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_126d_base_v006_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_189d_base_v007_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_252d_base_v008_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_378d_base_v009_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrec_504d_base_v010_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_5d_base_v011_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_10d_base_v012_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_21d_base_v013_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_42d_base_v014_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_63d_base_v015_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_126d_base_v016_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_189d_base_v017_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_252d_base_v018_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_378d_base_v019_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecema_504d_base_v020_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_5d_base_v021_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_10d_base_v022_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_21d_base_v023_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_42d_base_v024_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_63d_base_v025_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_126d_base_v026_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_189d_base_v027_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_252d_base_v028_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_378d_base_v029_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrec_504d_base_v030_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_5d_base_v031_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_10d_base_v032_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_21d_base_v033_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_42d_base_v034_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_63d_base_v035_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_126d_base_v036_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_189d_base_v037_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_252d_base_v038_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_378d_base_v039_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecema_504d_base_v040_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_5d_base_v041_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_10d_base_v042_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_21d_base_v043_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_42d_base_v044_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_63d_base_v045_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_126d_base_v046_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_189d_base_v047_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_252d_base_v048_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_378d_base_v049_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstr_504d_base_v050_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_5d_base_v051_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_10d_base_v052_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_21d_base_v053_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_42d_base_v054_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_63d_base_v055_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_126d_base_v056_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_189d_base_v057_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_252d_base_v058_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_378d_base_v059_signal,
    f44lcr_f44_leisure_cyclical_recovery_rstrema_504d_base_v060_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_21d_base_v061_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_42d_base_v062_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_63d_base_v063_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_126d_base_v064_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_189d_base_v065_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_252d_base_v066_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_378d_base_v067_signal,
    f44lcr_f44_leisure_cyclical_recovery_rrecz_504d_base_v068_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_21d_base_v069_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_42d_base_v070_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_63d_base_v071_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_126d_base_v072_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_189d_base_v073_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_252d_base_v074_signal,
    f44lcr_f44_leisure_cyclical_recovery_mrecz_378d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_LEISURE_CYCLICAL_RECOVERY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK leisure_cyclical_recovery_base_001_075_claude: {n_features} features pass")
