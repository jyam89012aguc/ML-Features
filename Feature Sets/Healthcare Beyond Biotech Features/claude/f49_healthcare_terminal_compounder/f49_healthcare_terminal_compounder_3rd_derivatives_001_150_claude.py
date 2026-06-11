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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f49_quality_composite(roic, fcf, revenue, w):
    q = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    g_fcf = fcf.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    g_rev = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    return q + g_fcf + g_rev


def _f49_compounder_score(roic, ebitdamargin, w):
    q = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    m = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return q * m


def _f49_terminal_quality(fcf, revenue, roic, w):
    fcfm = (fcf / revenue.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()
    q = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    g = revenue.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    return fcfm * q + g



# ===== features =====

def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_5d_jerk_v001_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 5), 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_5d_jerk_v002_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 5), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_5d_jerk_v003_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 5), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_10d_jerk_v004_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 10), 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_10d_jerk_v005_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 10), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_10d_jerk_v006_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 10), 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_21d_jerk_v007_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 21), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_21d_jerk_v008_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 21), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_21d_jerk_v009_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 21), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_42d_jerk_v010_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 42), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_42d_jerk_v011_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 42), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_42d_jerk_v012_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 42), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_63d_jerk_v013_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 63), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_63d_jerk_v014_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 63), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_63d_jerk_v015_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 63), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_126d_jerk_v016_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 126), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_126d_jerk_v017_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 126), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_126d_jerk_v018_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 126), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_189d_jerk_v019_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 189), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_189d_jerk_v020_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 189), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_189d_jerk_v021_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 189), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_252d_jerk_v022_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 252), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_252d_jerk_v023_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 252), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_252d_jerk_v024_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 252), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_378d_jerk_v025_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 378), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_378d_jerk_v026_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 378), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_378d_jerk_v027_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 378), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_504d_jerk_v028_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 504), 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_504d_jerk_v029_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 504), 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_504d_jerk_v030_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 504), 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_5d_jerk_v031_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 5), 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_5d_jerk_v032_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 5), 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_5d_jerk_v033_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 5), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_10d_jerk_v034_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 10), 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_10d_jerk_v035_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 10), 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_10d_jerk_v036_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 10), 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_21d_jerk_v037_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 21), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_21d_jerk_v038_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 21), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_21d_jerk_v039_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 21), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_42d_jerk_v040_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 42), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_42d_jerk_v041_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 42), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_42d_jerk_v042_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 42), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_63d_jerk_v043_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 63), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_63d_jerk_v044_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 63), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_63d_jerk_v045_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 63), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_126d_jerk_v046_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 126), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_126d_jerk_v047_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 126), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_126d_jerk_v048_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 126), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_189d_jerk_v049_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 189), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_189d_jerk_v050_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 189), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_189d_jerk_v051_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 189), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_252d_jerk_v052_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 252), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_252d_jerk_v053_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 252), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_252d_jerk_v054_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 252), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_378d_jerk_v055_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 378), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_378d_jerk_v056_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 378), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_378d_jerk_v057_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 378), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_504d_jerk_v058_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 504), 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_504d_jerk_v059_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 504), 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_504d_jerk_v060_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 504), 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_5d_jerk_v061_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 5), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_5d_jerk_v062_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 5), 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_5d_jerk_v063_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 5), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_10d_jerk_v064_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 10), 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_10d_jerk_v065_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 10), 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_10d_jerk_v066_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 10), 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_21d_jerk_v067_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 21), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_21d_jerk_v068_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 21), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_21d_jerk_v069_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 21), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_42d_jerk_v070_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 42), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_42d_jerk_v071_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 42), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_42d_jerk_v072_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 42), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_63d_jerk_v073_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 63), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_63d_jerk_v074_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 63), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_63d_jerk_v075_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 63), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_126d_jerk_v076_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 126), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_126d_jerk_v077_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 126), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_126d_jerk_v078_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 126), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_189d_jerk_v079_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 189), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_189d_jerk_v080_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 189), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_189d_jerk_v081_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 189), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_252d_jerk_v082_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 252), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_252d_jerk_v083_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 252), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_252d_jerk_v084_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 252), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_378d_jerk_v085_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 378), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_378d_jerk_v086_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 378), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_378d_jerk_v087_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 378), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_504d_jerk_v088_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 504), 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_504d_jerk_v089_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 504), 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_504d_jerk_v090_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 504), 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_5d_jerk_v091_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 5), 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_5d_jerk_v092_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 5), 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_5d_jerk_v093_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 5), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_10d_jerk_v094_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 10), 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_10d_jerk_v095_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 10), 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_10d_jerk_v096_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 10), 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_21d_jerk_v097_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 21), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_21d_jerk_v098_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 21), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_21d_jerk_v099_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 21), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_42d_jerk_v100_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 42), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_42d_jerk_v101_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 42), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_42d_jerk_v102_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 42), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_63d_jerk_v103_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 63), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_63d_jerk_v104_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 63), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_63d_jerk_v105_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 63), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_126d_jerk_v106_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 126), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_126d_jerk_v107_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 126), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_126d_jerk_v108_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 126), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_189d_jerk_v109_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 189), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_189d_jerk_v110_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 189), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_189d_jerk_v111_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 189), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_252d_jerk_v112_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 252), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_252d_jerk_v113_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 252), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_252d_jerk_v114_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 252), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_378d_jerk_v115_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 378), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_378d_jerk_v116_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 378), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_378d_jerk_v117_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 378), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_504d_jerk_v118_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 504), 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_504d_jerk_v119_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 504), 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_504d_jerk_v120_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 504), 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_5d_jerk_v121_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 5), 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_5d_jerk_v122_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 5), 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_5d_jerk_v123_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 5), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_10d_jerk_v124_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 10), 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_10d_jerk_v125_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 10), 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_10d_jerk_v126_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 10), 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_21d_jerk_v127_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 21), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_21d_jerk_v128_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 21), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_21d_jerk_v129_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 21), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_42d_jerk_v130_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 42), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_42d_jerk_v131_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 42), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_42d_jerk_v132_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 42), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_63d_jerk_v133_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 63), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_63d_jerk_v134_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 63), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_63d_jerk_v135_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 63), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_126d_jerk_v136_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 126), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_126d_jerk_v137_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 126), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_126d_jerk_v138_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 126), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_189d_jerk_v139_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 189), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_189d_jerk_v140_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 189), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_189d_jerk_v141_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 189), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_252d_jerk_v142_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 252), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_252d_jerk_v143_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 252), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_252d_jerk_v144_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 252), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_378d_jerk_v145_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 378), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_378d_jerk_v146_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 378), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_378d_jerk_v147_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 378), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_504d_jerk_v148_signal(roic, fcf, revenue, closeadj):
    result = (_jerk(_f49_quality_composite(roic, fcf, revenue, 504), 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_504d_jerk_v149_signal(roic, ebitdamargin, closeadj):
    result = (_jerk(_f49_compounder_score(roic, ebitdamargin, 504), 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_504d_jerk_v150_signal(fcf, revenue, roic, closeadj):
    result = (_jerk(_f49_terminal_quality(fcf, revenue, roic, 504), 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_5d_jerk_v001_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_5d_jerk_v002_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_5d_jerk_v003_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_10d_jerk_v004_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_10d_jerk_v005_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_10d_jerk_v006_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_21d_jerk_v007_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_21d_jerk_v008_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_21d_jerk_v009_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_42d_jerk_v010_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_42d_jerk_v011_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_42d_jerk_v012_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_63d_jerk_v013_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_63d_jerk_v014_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_63d_jerk_v015_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_126d_jerk_v016_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_126d_jerk_v017_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_126d_jerk_v018_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_189d_jerk_v019_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_189d_jerk_v020_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_189d_jerk_v021_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_252d_jerk_v022_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_252d_jerk_v023_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_252d_jerk_v024_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_378d_jerk_v025_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_378d_jerk_v026_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_378d_jerk_v027_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_504d_jerk_v028_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_504d_jerk_v029_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_504d_jerk_v030_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_5d_jerk_v031_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_5d_jerk_v032_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_5d_jerk_v033_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_10d_jerk_v034_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_10d_jerk_v035_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_10d_jerk_v036_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_21d_jerk_v037_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_21d_jerk_v038_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_21d_jerk_v039_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_42d_jerk_v040_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_42d_jerk_v041_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_42d_jerk_v042_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_63d_jerk_v043_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_63d_jerk_v044_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_63d_jerk_v045_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_126d_jerk_v046_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_126d_jerk_v047_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_126d_jerk_v048_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_189d_jerk_v049_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_189d_jerk_v050_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_189d_jerk_v051_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_252d_jerk_v052_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_252d_jerk_v053_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_252d_jerk_v054_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_378d_jerk_v055_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_378d_jerk_v056_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_378d_jerk_v057_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_504d_jerk_v058_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_504d_jerk_v059_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_504d_jerk_v060_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_5d_jerk_v061_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_5d_jerk_v062_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_5d_jerk_v063_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_10d_jerk_v064_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_10d_jerk_v065_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_10d_jerk_v066_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_21d_jerk_v067_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_21d_jerk_v068_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_21d_jerk_v069_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_42d_jerk_v070_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_42d_jerk_v071_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_42d_jerk_v072_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_63d_jerk_v073_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_63d_jerk_v074_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_63d_jerk_v075_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_126d_jerk_v076_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_126d_jerk_v077_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_126d_jerk_v078_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_189d_jerk_v079_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_189d_jerk_v080_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_189d_jerk_v081_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_252d_jerk_v082_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_252d_jerk_v083_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_252d_jerk_v084_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_378d_jerk_v085_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_378d_jerk_v086_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_378d_jerk_v087_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_504d_jerk_v088_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_504d_jerk_v089_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_504d_jerk_v090_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_5d_jerk_v091_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_5d_jerk_v092_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_5d_jerk_v093_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_10d_jerk_v094_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_10d_jerk_v095_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_10d_jerk_v096_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_21d_jerk_v097_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_21d_jerk_v098_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_21d_jerk_v099_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_42d_jerk_v100_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_42d_jerk_v101_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_42d_jerk_v102_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_63d_jerk_v103_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_63d_jerk_v104_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_63d_jerk_v105_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_126d_jerk_v106_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_126d_jerk_v107_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_126d_jerk_v108_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_189d_jerk_v109_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_189d_jerk_v110_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_189d_jerk_v111_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_252d_jerk_v112_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_252d_jerk_v113_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_252d_jerk_v114_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_378d_jerk_v115_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_378d_jerk_v116_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_378d_jerk_v117_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose5_504d_jerk_v118_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose5_504d_jerk_v119_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose5_504d_jerk_v120_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_5d_jerk_v121_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_5d_jerk_v122_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_5d_jerk_v123_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_10d_jerk_v124_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_10d_jerk_v125_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_10d_jerk_v126_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_21d_jerk_v127_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_21d_jerk_v128_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_21d_jerk_v129_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_42d_jerk_v130_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_42d_jerk_v131_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_42d_jerk_v132_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_63d_jerk_v133_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_63d_jerk_v134_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_63d_jerk_v135_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_126d_jerk_v136_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_126d_jerk_v137_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_126d_jerk_v138_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_189d_jerk_v139_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_189d_jerk_v140_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_189d_jerk_v141_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_252d_jerk_v142_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_252d_jerk_v143_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_252d_jerk_v144_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_378d_jerk_v145_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_378d_jerk_v146_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_378d_jerk_v147_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose126_504d_jerk_v148_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose126_504d_jerk_v149_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose126_504d_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_HEALTHCARE_TERMINAL_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f49_quality_composite", "_f49_compounder_score", "_f49_terminal_quality")
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
    print(f"OK f49_healthcare_terminal_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")
