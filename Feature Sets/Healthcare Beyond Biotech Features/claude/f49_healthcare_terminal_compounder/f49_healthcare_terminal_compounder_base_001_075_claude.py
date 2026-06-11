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

def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_5d_base_v001_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_5d_base_v002_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_5d_base_v003_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_10d_base_v004_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_10d_base_v005_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_10d_base_v006_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_21d_base_v007_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_21d_base_v008_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_21d_base_v009_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_42d_base_v010_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_42d_base_v011_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_42d_base_v012_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_63d_base_v013_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_63d_base_v014_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_63d_base_v015_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_126d_base_v016_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_126d_base_v017_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_126d_base_v018_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_189d_base_v019_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_189d_base_v020_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_189d_base_v021_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_252d_base_v022_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_252d_base_v023_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_252d_base_v024_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_378d_base_v025_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_378d_base_v026_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_378d_base_v027_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_504d_base_v028_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_504d_base_v029_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_504d_base_v030_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_5d_base_v031_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_5d_base_v032_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_5d_base_v033_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_10d_base_v034_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_10d_base_v035_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_10d_base_v036_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_21d_base_v037_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_21d_base_v038_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_21d_base_v039_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_42d_base_v040_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_42d_base_v041_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_42d_base_v042_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_63d_base_v043_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_63d_base_v044_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_63d_base_v045_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_126d_base_v046_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_126d_base_v047_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_126d_base_v048_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_189d_base_v049_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_189d_base_v050_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_189d_base_v051_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_252d_base_v052_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_252d_base_v053_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_252d_base_v054_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_378d_base_v055_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_378d_base_v056_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_378d_base_v057_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_504d_base_v058_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_504d_base_v059_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_504d_base_v060_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_5d_base_v061_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_5d_base_v062_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_5d_base_v063_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 5)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_10d_base_v064_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_10d_base_v065_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_10d_base_v066_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 10)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_21d_base_v067_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_21d_base_v068_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_21d_base_v069_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 21)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_42d_base_v070_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_42d_base_v071_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_42d_base_v072_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 42)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_63d_base_v073_signal(roic, fcf, revenue, closeadj):
    result = (_f49_quality_composite(roic, fcf, revenue, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_63d_base_v074_signal(roic, ebitdamargin, closeadj):
    result = (_f49_compounder_score(roic, ebitdamargin, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_63d_base_v075_signal(fcf, revenue, roic, closeadj):
    result = (_f49_terminal_quality(fcf, revenue, roic, 63)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_5d_base_v001_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_5d_base_v002_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_5d_base_v003_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_10d_base_v004_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_10d_base_v005_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_10d_base_v006_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_21d_base_v007_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_21d_base_v008_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_21d_base_v009_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_42d_base_v010_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_42d_base_v011_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_42d_base_v012_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_63d_base_v013_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_63d_base_v014_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_63d_base_v015_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_126d_base_v016_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_126d_base_v017_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_126d_base_v018_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_189d_base_v019_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_189d_base_v020_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_189d_base_v021_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_252d_base_v022_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_252d_base_v023_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_252d_base_v024_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_378d_base_v025_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_378d_base_v026_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_378d_base_v027_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose_504d_base_v028_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose_504d_base_v029_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose_504d_base_v030_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_5d_base_v031_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_5d_base_v032_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_5d_base_v033_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_10d_base_v034_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_10d_base_v035_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_10d_base_v036_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_21d_base_v037_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_21d_base_v038_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_21d_base_v039_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_42d_base_v040_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_42d_base_v041_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_42d_base_v042_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_63d_base_v043_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_63d_base_v044_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_63d_base_v045_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_126d_base_v046_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_126d_base_v047_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_126d_base_v048_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_189d_base_v049_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_189d_base_v050_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_189d_base_v051_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_252d_base_v052_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_252d_base_v053_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_252d_base_v054_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_378d_base_v055_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_378d_base_v056_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_378d_base_v057_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclosemean_504d_base_v058_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclosemean_504d_base_v059_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclosemean_504d_base_v060_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_5d_base_v061_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_5d_base_v062_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_5d_base_v063_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_10d_base_v064_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_10d_base_v065_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_10d_base_v066_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_21d_base_v067_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_21d_base_v068_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_21d_base_v069_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_42d_base_v070_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_42d_base_v071_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_42d_base_v072_signal,
    f49htc_f49_healthcare_terminal_compounder_p1_raw_xclose63_63d_base_v073_signal,
    f49htc_f49_healthcare_terminal_compounder_p2_raw_xclose63_63d_base_v074_signal,
    f49htc_f49_healthcare_terminal_compounder_p3_raw_xclose63_63d_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_HEALTHCARE_TERMINAL_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f49_healthcare_terminal_compounder_base_001_075_claude: {n_features} features pass")
