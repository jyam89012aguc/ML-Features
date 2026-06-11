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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====
def _f48_revenue_bottom(revenue, w):
    mn = revenue.rolling(w, min_periods=max(1, w // 2)).min()
    return (revenue - mn) / mn.replace(0, np.nan).abs()


def _f48_margin_bottom(ebitdamargin, w):
    mn = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    return ebitdamargin - mn


def _f48_regime_bottom_score(revenue, ebitda, fcf, w):
    rb = (revenue - revenue.rolling(w, min_periods=max(1, w // 2)).min())
    eb = (ebitda - ebitda.rolling(w, min_periods=max(1, w // 2)).min())
    fb = (fcf - fcf.rolling(w, min_periods=max(1, w // 2)).min())
    return rb + eb + fb


# ===== features =====
def f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_base_v001_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_base_v002_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_5d_s00_base_v003_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_base_v004_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_base_v005_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_10d_s00_base_v006_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_base_v007_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_base_v008_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_21d_s00_base_v009_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_base_v010_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_base_v011_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_42d_s00_base_v012_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_base_v013_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_base_v014_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_63d_s00_base_v015_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_base_v016_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_base_v017_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_84d_s00_base_v018_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_base_v019_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_base_v020_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_105d_s00_base_v021_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_base_v022_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_base_v023_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_126d_s00_base_v024_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_base_v025_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_base_v026_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_147d_s00_base_v027_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_base_v028_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_base_v029_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_168d_s00_base_v030_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_base_v031_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_base_v032_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_189d_s00_base_v033_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_base_v034_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_base_v035_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_210d_s00_base_v036_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_base_v037_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_base_v038_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_231d_s00_base_v039_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_base_v040_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_base_v041_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_252d_s00_base_v042_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_base_v043_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_base_v044_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_294d_s00_base_v045_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_base_v046_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_base_v047_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_336d_s00_base_v048_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_base_v049_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_base_v050_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_378d_s00_base_v051_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_420d_s00_base_v052_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_420d_s00_base_v053_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_420d_s00_base_v054_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_462d_s00_base_v055_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_462d_s00_base_v056_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_462d_s00_base_v057_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_504d_s00_base_v058_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_504d_s00_base_v059_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rs_full_504d_s00_base_v060_signal(revenue, ebitda, fcf, closeadj):
    base = _f48_regime_bottom_score(revenue, ebitda, fcf, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v061_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v062_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v063_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v064_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v065_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v068_signal(revenue, ebitdamargin, closeadj):
    base = _f48_revenue_bottom(revenue, 5)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v069_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v070_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v071_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v072_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v073_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v074_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v075_signal(ebitdamargin, revenue, closeadj):
    base = _f48_margin_bottom(ebitdamargin, 5)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s00_base_v001_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s00_base_v002_signal,
    f48urb_f48_utility_regime_bottom_rs_full_5d_s00_base_v003_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_10d_s00_base_v004_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_10d_s00_base_v005_signal,
    f48urb_f48_utility_regime_bottom_rs_full_10d_s00_base_v006_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_21d_s00_base_v007_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_21d_s00_base_v008_signal,
    f48urb_f48_utility_regime_bottom_rs_full_21d_s00_base_v009_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_42d_s00_base_v010_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_42d_s00_base_v011_signal,
    f48urb_f48_utility_regime_bottom_rs_full_42d_s00_base_v012_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_63d_s00_base_v013_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_63d_s00_base_v014_signal,
    f48urb_f48_utility_regime_bottom_rs_full_63d_s00_base_v015_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_84d_s00_base_v016_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_84d_s00_base_v017_signal,
    f48urb_f48_utility_regime_bottom_rs_full_84d_s00_base_v018_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_105d_s00_base_v019_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_105d_s00_base_v020_signal,
    f48urb_f48_utility_regime_bottom_rs_full_105d_s00_base_v021_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_126d_s00_base_v022_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_126d_s00_base_v023_signal,
    f48urb_f48_utility_regime_bottom_rs_full_126d_s00_base_v024_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_147d_s00_base_v025_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_147d_s00_base_v026_signal,
    f48urb_f48_utility_regime_bottom_rs_full_147d_s00_base_v027_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_168d_s00_base_v028_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_168d_s00_base_v029_signal,
    f48urb_f48_utility_regime_bottom_rs_full_168d_s00_base_v030_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_189d_s00_base_v031_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_189d_s00_base_v032_signal,
    f48urb_f48_utility_regime_bottom_rs_full_189d_s00_base_v033_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_210d_s00_base_v034_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_210d_s00_base_v035_signal,
    f48urb_f48_utility_regime_bottom_rs_full_210d_s00_base_v036_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_231d_s00_base_v037_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_231d_s00_base_v038_signal,
    f48urb_f48_utility_regime_bottom_rs_full_231d_s00_base_v039_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_252d_s00_base_v040_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_252d_s00_base_v041_signal,
    f48urb_f48_utility_regime_bottom_rs_full_252d_s00_base_v042_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_294d_s00_base_v043_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_294d_s00_base_v044_signal,
    f48urb_f48_utility_regime_bottom_rs_full_294d_s00_base_v045_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_336d_s00_base_v046_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_336d_s00_base_v047_signal,
    f48urb_f48_utility_regime_bottom_rs_full_336d_s00_base_v048_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_378d_s00_base_v049_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_378d_s00_base_v050_signal,
    f48urb_f48_utility_regime_bottom_rs_full_378d_s00_base_v051_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_420d_s00_base_v052_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_420d_s00_base_v053_signal,
    f48urb_f48_utility_regime_bottom_rs_full_420d_s00_base_v054_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_462d_s00_base_v055_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_462d_s00_base_v056_signal,
    f48urb_f48_utility_regime_bottom_rs_full_462d_s00_base_v057_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_504d_s00_base_v058_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_504d_s00_base_v059_signal,
    f48urb_f48_utility_regime_bottom_rs_full_504d_s00_base_v060_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v061_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v062_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v063_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v064_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v065_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v066_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v067_signal,
    f48urb_f48_utility_regime_bottom_rb_rev_5d_s01_base_v068_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v069_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v070_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v071_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v072_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v073_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v074_signal,
    f48urb_f48_utility_regime_bottom_mb_marg_5d_s01_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_UTILITY_REGIME_BOTTOM_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "ebitda": ebitda, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_revenue_bottom", "_f48_margin_bottom", "_f48_regime_bottom_score",)
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
    print(f"OK f48_utility_regime_bottom_base_001_075_claude: {n_features} features pass")
