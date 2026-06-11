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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f50_quality_composite(roic, fcf, revenue, w):
    q = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    g_fcf = fcf.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    g_rev = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    return q * g_fcf + g_rev


def _f50_idiosyncratic_signal(close, revenue, w):
    r = close.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    g = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    return g / vol * close


def _f50_alpha_score(roic, ebitdamargin, w):
    q = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return q + m



# ===== features =====

def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_5d_slope_v001_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 5), 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_5d_slope_v002_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 5), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_5d_slope_v003_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_10d_slope_v004_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 10), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_10d_slope_v005_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 10), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_10d_slope_v006_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 10), 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_21d_slope_v007_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 21), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_21d_slope_v008_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 21), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_21d_slope_v009_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_42d_slope_v010_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 42), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_42d_slope_v011_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 42), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_42d_slope_v012_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 42), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_63d_slope_v013_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 63), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_63d_slope_v014_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 63), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_63d_slope_v015_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_126d_slope_v016_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 126), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_126d_slope_v017_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 126), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_126d_slope_v018_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 126), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_189d_slope_v019_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 189), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_189d_slope_v020_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 189), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_189d_slope_v021_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 189), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_252d_slope_v022_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 252), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_252d_slope_v023_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 252), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_252d_slope_v024_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_378d_slope_v025_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 378), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_378d_slope_v026_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 378), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_378d_slope_v027_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 378), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_504d_slope_v028_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 504), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_504d_slope_v029_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 504), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_504d_slope_v030_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 504), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_5d_slope_v031_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 5), 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_5d_slope_v032_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 5), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_5d_slope_v033_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 5), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_10d_slope_v034_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 10), 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_10d_slope_v035_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 10), 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_10d_slope_v036_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 10), 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_21d_slope_v037_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 21), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_21d_slope_v038_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 21), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_21d_slope_v039_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 21), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_42d_slope_v040_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 42), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_42d_slope_v041_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 42), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_42d_slope_v042_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 42), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_63d_slope_v043_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 63), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_63d_slope_v044_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 63), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_63d_slope_v045_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 63), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_126d_slope_v046_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 126), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_126d_slope_v047_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 126), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_126d_slope_v048_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 126), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_189d_slope_v049_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 189), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_189d_slope_v050_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 189), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_189d_slope_v051_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 189), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_252d_slope_v052_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 252), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_252d_slope_v053_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 252), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_252d_slope_v054_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 252), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_378d_slope_v055_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 378), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_378d_slope_v056_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 378), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_378d_slope_v057_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 378), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_504d_slope_v058_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 504), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_504d_slope_v059_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 504), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_504d_slope_v060_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 504), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_5d_slope_v061_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 5), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_5d_slope_v062_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 5), 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_5d_slope_v063_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 5), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_10d_slope_v064_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 10), 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_10d_slope_v065_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 10), 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_10d_slope_v066_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 10), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_21d_slope_v067_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 21), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_21d_slope_v068_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 21), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_21d_slope_v069_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 21), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_42d_slope_v070_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 42), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_42d_slope_v071_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 42), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_42d_slope_v072_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 42), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_63d_slope_v073_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 63), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_63d_slope_v074_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 63), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_63d_slope_v075_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 63), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_126d_slope_v076_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 126), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_126d_slope_v077_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 126), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_126d_slope_v078_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 126), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_189d_slope_v079_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 189), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_189d_slope_v080_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 189), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_189d_slope_v081_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 189), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_252d_slope_v082_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 252), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_252d_slope_v083_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 252), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_252d_slope_v084_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 252), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_378d_slope_v085_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 378), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_378d_slope_v086_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 378), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_378d_slope_v087_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 378), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_504d_slope_v088_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 504), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_504d_slope_v089_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 504), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_504d_slope_v090_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 504), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_5d_slope_v091_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 5), 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_5d_slope_v092_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 5), 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_5d_slope_v093_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 5), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_10d_slope_v094_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 10), 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_10d_slope_v095_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 10), 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_10d_slope_v096_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 10), 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_21d_slope_v097_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 21), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_21d_slope_v098_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 21), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_21d_slope_v099_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 21), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_42d_slope_v100_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 42), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_42d_slope_v101_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 42), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_42d_slope_v102_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 42), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_63d_slope_v103_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 63), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_63d_slope_v104_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 63), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_63d_slope_v105_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 63), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_126d_slope_v106_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 126), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_126d_slope_v107_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 126), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_126d_slope_v108_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 126), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_189d_slope_v109_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 189), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_189d_slope_v110_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 189), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_189d_slope_v111_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 189), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_252d_slope_v112_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 252), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_252d_slope_v113_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 252), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_252d_slope_v114_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 252), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_378d_slope_v115_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 378), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_378d_slope_v116_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 378), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_378d_slope_v117_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 378), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_504d_slope_v118_signal(roic, fcf, revenue, closeadj):
    result = (_slope_pct(_f50_quality_composite(roic, fcf, revenue, 504), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_504d_slope_v119_signal(closeadj, revenue):
    result = (_slope_pct(_f50_idiosyncratic_signal(closeadj, revenue, 504), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_504d_slope_v120_signal(roic, ebitdamargin, closeadj):
    result = (_slope_pct(_f50_alpha_score(roic, ebitdamargin, 504), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_5d_slope_v121_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 5), 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_5d_slope_v122_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 5), 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_5d_slope_v123_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 5), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_10d_slope_v124_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 10), 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_10d_slope_v125_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 10), 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_10d_slope_v126_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 10), 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_21d_slope_v127_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 21), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_21d_slope_v128_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 21), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_21d_slope_v129_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 21), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_42d_slope_v130_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 42), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_42d_slope_v131_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 42), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_42d_slope_v132_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 42), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_63d_slope_v133_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 63), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_63d_slope_v134_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 63), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_63d_slope_v135_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 63), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_126d_slope_v136_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 126), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_126d_slope_v137_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 126), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_126d_slope_v138_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 126), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_189d_slope_v139_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 189), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_189d_slope_v140_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 189), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_189d_slope_v141_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 189), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_252d_slope_v142_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 252), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_252d_slope_v143_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 252), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_252d_slope_v144_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 252), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_378d_slope_v145_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 378), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_378d_slope_v146_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 378), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_378d_slope_v147_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 378), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_504d_slope_v148_signal(roic, fcf, revenue, closeadj):
    result = (_slope_diff_norm(_f50_quality_composite(roic, fcf, revenue, 504), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_504d_slope_v149_signal(closeadj, revenue):
    result = (_slope_diff_norm(_f50_idiosyncratic_signal(closeadj, revenue, 504), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_504d_slope_v150_signal(roic, ebitdamargin, closeadj):
    result = (_slope_diff_norm(_f50_alpha_score(roic, ebitdamargin, 504), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_5d_slope_v001_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_5d_slope_v002_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_5d_slope_v003_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_10d_slope_v004_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_10d_slope_v005_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_10d_slope_v006_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_21d_slope_v007_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_21d_slope_v008_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_21d_slope_v009_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_42d_slope_v010_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_42d_slope_v011_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_42d_slope_v012_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_63d_slope_v013_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_63d_slope_v014_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_63d_slope_v015_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_126d_slope_v016_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_126d_slope_v017_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_126d_slope_v018_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_189d_slope_v019_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_189d_slope_v020_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_189d_slope_v021_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_252d_slope_v022_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_252d_slope_v023_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_252d_slope_v024_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_378d_slope_v025_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_378d_slope_v026_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_378d_slope_v027_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose_504d_slope_v028_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose_504d_slope_v029_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose_504d_slope_v030_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_5d_slope_v031_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_5d_slope_v032_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_5d_slope_v033_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_10d_slope_v034_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_10d_slope_v035_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_10d_slope_v036_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_21d_slope_v037_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_21d_slope_v038_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_21d_slope_v039_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_42d_slope_v040_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_42d_slope_v041_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_42d_slope_v042_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_63d_slope_v043_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_63d_slope_v044_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_63d_slope_v045_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_126d_slope_v046_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_126d_slope_v047_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_126d_slope_v048_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_189d_slope_v049_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_189d_slope_v050_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_189d_slope_v051_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_252d_slope_v052_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_252d_slope_v053_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_252d_slope_v054_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_378d_slope_v055_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_378d_slope_v056_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_378d_slope_v057_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclosemean_504d_slope_v058_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclosemean_504d_slope_v059_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclosemean_504d_slope_v060_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_5d_slope_v061_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_5d_slope_v062_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_5d_slope_v063_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_10d_slope_v064_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_10d_slope_v065_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_10d_slope_v066_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_21d_slope_v067_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_21d_slope_v068_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_21d_slope_v069_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_42d_slope_v070_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_42d_slope_v071_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_42d_slope_v072_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_63d_slope_v073_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_63d_slope_v074_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_63d_slope_v075_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_126d_slope_v076_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_126d_slope_v077_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_126d_slope_v078_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_189d_slope_v079_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_189d_slope_v080_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_189d_slope_v081_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_252d_slope_v082_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_252d_slope_v083_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_252d_slope_v084_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_378d_slope_v085_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_378d_slope_v086_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_378d_slope_v087_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose63_504d_slope_v088_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose63_504d_slope_v089_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose63_504d_slope_v090_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_5d_slope_v091_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_5d_slope_v092_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_5d_slope_v093_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_10d_slope_v094_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_10d_slope_v095_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_10d_slope_v096_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_21d_slope_v097_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_21d_slope_v098_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_21d_slope_v099_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_42d_slope_v100_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_42d_slope_v101_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_42d_slope_v102_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_63d_slope_v103_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_63d_slope_v104_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_63d_slope_v105_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_126d_slope_v106_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_126d_slope_v107_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_126d_slope_v108_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_189d_slope_v109_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_189d_slope_v110_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_189d_slope_v111_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_252d_slope_v112_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_252d_slope_v113_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_252d_slope_v114_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_378d_slope_v115_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_378d_slope_v116_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_378d_slope_v117_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose5_504d_slope_v118_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose5_504d_slope_v119_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose5_504d_slope_v120_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_5d_slope_v121_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_5d_slope_v122_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_5d_slope_v123_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_10d_slope_v124_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_10d_slope_v125_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_10d_slope_v126_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_21d_slope_v127_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_21d_slope_v128_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_21d_slope_v129_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_42d_slope_v130_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_42d_slope_v131_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_42d_slope_v132_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_63d_slope_v133_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_63d_slope_v134_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_63d_slope_v135_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_126d_slope_v136_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_126d_slope_v137_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_126d_slope_v138_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_189d_slope_v139_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_189d_slope_v140_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_189d_slope_v141_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_252d_slope_v142_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_252d_slope_v143_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_252d_slope_v144_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_378d_slope_v145_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_378d_slope_v146_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_378d_slope_v147_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p1_raw_xclose126_504d_slope_v148_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p2_raw_xclose126_504d_slope_v149_signal,
    f50mia_f50_medtech_idiosyncratic_alpha_p3_raw_xclose126_504d_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_MEDTECH_IDIOSYNCRATIC_ALPHA_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f50_quality_composite", "_f50_idiosyncratic_signal", "_f50_alpha_score")
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
    print(f"OK f50_medtech_idiosyncratic_alpha_2nd_derivatives_001_150_claude: {n_features} features pass")
