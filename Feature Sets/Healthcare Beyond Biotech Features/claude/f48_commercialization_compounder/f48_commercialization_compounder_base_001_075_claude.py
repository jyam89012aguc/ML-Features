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


# ===== folder domain primitives =====
def _f48_revenue_trajectory(revenue, w):
    g = revenue.pct_change(periods=w)
    accel = g.diff(periods=w)
    smooth = g.rolling(w, min_periods=max(1, w // 2)).mean()
    return smooth + accel


def _f48_margin_trajectory(ebitdamargin, w):
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    slope = ebitdamargin.diff(periods=w)
    return m + slope


def _f48_commercialization_score(revenue, ebitdamargin, w):
    g = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return g * m



# ===== features =====

def f48cco_f48_commercialization_compounder_p1_raw_xclose_5d_base_v001_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_5d_base_v002_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_5d_base_v003_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_10d_base_v004_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_10d_base_v005_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_10d_base_v006_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_21d_base_v007_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_21d_base_v008_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_21d_base_v009_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_42d_base_v010_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_42d_base_v011_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_42d_base_v012_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_63d_base_v013_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_63d_base_v014_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_63d_base_v015_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_126d_base_v016_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_126d_base_v017_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_126d_base_v018_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_189d_base_v019_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_189d_base_v020_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_189d_base_v021_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_252d_base_v022_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_252d_base_v023_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_252d_base_v024_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_378d_base_v025_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_378d_base_v026_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_378d_base_v027_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose_504d_base_v028_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose_504d_base_v029_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose_504d_base_v030_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_5d_base_v031_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_5d_base_v032_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_5d_base_v033_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_10d_base_v034_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_10d_base_v035_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_10d_base_v036_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_21d_base_v037_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_21d_base_v038_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_21d_base_v039_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_42d_base_v040_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_42d_base_v041_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_42d_base_v042_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_63d_base_v043_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_63d_base_v044_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_63d_base_v045_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_126d_base_v046_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_126d_base_v047_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_126d_base_v048_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_189d_base_v049_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_189d_base_v050_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_189d_base_v051_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_252d_base_v052_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_252d_base_v053_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_252d_base_v054_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_378d_base_v055_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_378d_base_v056_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_378d_base_v057_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclosemean_504d_base_v058_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclosemean_504d_base_v059_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclosemean_504d_base_v060_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose63_5d_base_v061_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose63_5d_base_v062_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose63_5d_base_v063_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose63_10d_base_v064_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose63_10d_base_v065_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose63_10d_base_v066_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose63_21d_base_v067_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose63_21d_base_v068_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose63_21d_base_v069_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose63_42d_base_v070_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose63_42d_base_v071_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose63_42d_base_v072_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p1_raw_xclose63_63d_base_v073_signal(revenue, closeadj):
    result = (_f48_revenue_trajectory(revenue, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p2_raw_xclose63_63d_base_v074_signal(ebitdamargin, closeadj):
    result = (_f48_margin_trajectory(ebitdamargin, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f48cco_f48_commercialization_compounder_p3_raw_xclose63_63d_base_v075_signal(revenue, ebitdamargin, closeadj):
    result = (_f48_commercialization_score(revenue, ebitdamargin, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48cco_f48_commercialization_compounder_p1_raw_xclose_5d_base_v001_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_5d_base_v002_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_5d_base_v003_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_10d_base_v004_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_10d_base_v005_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_10d_base_v006_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_21d_base_v007_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_21d_base_v008_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_21d_base_v009_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_42d_base_v010_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_42d_base_v011_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_42d_base_v012_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_63d_base_v013_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_63d_base_v014_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_63d_base_v015_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_126d_base_v016_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_126d_base_v017_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_126d_base_v018_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_189d_base_v019_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_189d_base_v020_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_189d_base_v021_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_252d_base_v022_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_252d_base_v023_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_252d_base_v024_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_378d_base_v025_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_378d_base_v026_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_378d_base_v027_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose_504d_base_v028_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose_504d_base_v029_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose_504d_base_v030_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_5d_base_v031_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_5d_base_v032_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_5d_base_v033_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_10d_base_v034_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_10d_base_v035_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_10d_base_v036_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_21d_base_v037_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_21d_base_v038_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_21d_base_v039_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_42d_base_v040_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_42d_base_v041_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_42d_base_v042_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_63d_base_v043_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_63d_base_v044_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_63d_base_v045_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_126d_base_v046_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_126d_base_v047_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_126d_base_v048_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_189d_base_v049_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_189d_base_v050_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_189d_base_v051_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_252d_base_v052_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_252d_base_v053_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_252d_base_v054_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_378d_base_v055_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_378d_base_v056_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_378d_base_v057_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclosemean_504d_base_v058_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclosemean_504d_base_v059_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclosemean_504d_base_v060_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose63_5d_base_v061_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose63_5d_base_v062_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose63_5d_base_v063_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose63_10d_base_v064_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose63_10d_base_v065_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose63_10d_base_v066_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose63_21d_base_v067_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose63_21d_base_v068_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose63_21d_base_v069_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose63_42d_base_v070_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose63_42d_base_v071_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose63_42d_base_v072_signal,
    f48cco_f48_commercialization_compounder_p1_raw_xclose63_63d_base_v073_signal,
    f48cco_f48_commercialization_compounder_p2_raw_xclose63_63d_base_v074_signal,
    f48cco_f48_commercialization_compounder_p3_raw_xclose63_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_COMMERCIALIZATION_COMPOUNDER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_revenue_trajectory", "_f48_margin_trajectory", "_f48_commercialization_score")
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
    print(f"OK f48_commercialization_compounder_base_001_075_claude: {n_features} features pass")
