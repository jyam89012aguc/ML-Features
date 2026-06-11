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

def _f15_revenue_compound(revenue, w):
    return revenue.pct_change(periods=w)


def _f15_compounding_smoothness(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    rgsd = rg.rolling(w, min_periods=max(1, w // 2)).std()
    return (rg + eg) / rgsd.replace(0, np.nan)


def _f15_synergy_score(revenue, ebitdamargin, w):
    rg = revenue.pct_change(periods=w)
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    emsd = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).std()
    return rg * em / emsd.replace(0, np.nan)


# ===== features =====

def f15mbs_f15_multi_brand_synergy_rc_w5_5d_slope_v001_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w5_10d_slope_v002_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w5_21d_slope_v003_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w5_42d_slope_v004_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w5_63d_slope_v005_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w10_5d_slope_v006_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w10_10d_slope_v007_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w10_21d_slope_v008_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w10_42d_slope_v009_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w10_63d_slope_v010_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w21_5d_slope_v011_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w21_10d_slope_v012_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w21_21d_slope_v013_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w21_42d_slope_v014_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w21_63d_slope_v015_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w42_5d_slope_v016_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w42_10d_slope_v017_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w42_21d_slope_v018_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w42_42d_slope_v019_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w42_63d_slope_v020_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w63_5d_slope_v021_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w63_10d_slope_v022_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w63_21d_slope_v023_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w63_42d_slope_v024_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w63_63d_slope_v025_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w126_5d_slope_v026_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w126_10d_slope_v027_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w126_21d_slope_v028_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w126_42d_slope_v029_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w126_63d_slope_v030_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w189_5d_slope_v031_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w189_10d_slope_v032_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w189_21d_slope_v033_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w189_42d_slope_v034_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w189_63d_slope_v035_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w252_5d_slope_v036_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w252_10d_slope_v037_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w252_21d_slope_v038_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w252_42d_slope_v039_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w252_63d_slope_v040_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w378_5d_slope_v041_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w378_10d_slope_v042_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w378_21d_slope_v043_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w378_42d_slope_v044_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w378_63d_slope_v045_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w504_5d_slope_v046_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w504_10d_slope_v047_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w504_21d_slope_v048_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w504_42d_slope_v049_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_rc_w504_63d_slope_v050_signal(revenue, closeadj):
    result = _slope_diff_norm(_f15_revenue_compound(revenue, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w5_5d_slope_v051_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w5_10d_slope_v052_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w5_21d_slope_v053_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w5_42d_slope_v054_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w5_63d_slope_v055_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w10_5d_slope_v056_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w10_10d_slope_v057_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w10_21d_slope_v058_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w10_42d_slope_v059_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w10_63d_slope_v060_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w21_5d_slope_v061_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w21_10d_slope_v062_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w21_21d_slope_v063_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w21_42d_slope_v064_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w21_63d_slope_v065_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w42_5d_slope_v066_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w42_10d_slope_v067_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w42_21d_slope_v068_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w42_42d_slope_v069_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w42_63d_slope_v070_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w63_5d_slope_v071_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w63_10d_slope_v072_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w63_21d_slope_v073_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w63_42d_slope_v074_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w63_63d_slope_v075_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w126_5d_slope_v076_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w126_10d_slope_v077_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w126_21d_slope_v078_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w126_42d_slope_v079_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w126_63d_slope_v080_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w189_5d_slope_v081_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w189_10d_slope_v082_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w189_21d_slope_v083_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w189_42d_slope_v084_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w189_63d_slope_v085_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w252_5d_slope_v086_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w252_10d_slope_v087_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w252_21d_slope_v088_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w252_42d_slope_v089_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w252_63d_slope_v090_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w378_5d_slope_v091_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w378_10d_slope_v092_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w378_21d_slope_v093_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w378_42d_slope_v094_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w378_63d_slope_v095_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w504_5d_slope_v096_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w504_10d_slope_v097_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w504_21d_slope_v098_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w504_42d_slope_v099_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_cs_w504_63d_slope_v100_signal(revenue, ebitda, closeadj):
    result = _slope_diff_norm(_f15_compounding_smoothness(revenue, ebitda, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w5_5d_slope_v101_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w5_10d_slope_v102_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w5_21d_slope_v103_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w5_42d_slope_v104_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w5_63d_slope_v105_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w10_5d_slope_v106_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w10_10d_slope_v107_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w10_21d_slope_v108_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w10_42d_slope_v109_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w10_63d_slope_v110_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w21_5d_slope_v111_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w21_10d_slope_v112_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w21_21d_slope_v113_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w21_42d_slope_v114_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w21_63d_slope_v115_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w42_5d_slope_v116_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w42_10d_slope_v117_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w42_21d_slope_v118_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w42_42d_slope_v119_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w42_63d_slope_v120_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w63_5d_slope_v121_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w63_10d_slope_v122_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w63_21d_slope_v123_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w63_42d_slope_v124_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w63_63d_slope_v125_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w126_5d_slope_v126_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w126_10d_slope_v127_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w126_21d_slope_v128_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w126_42d_slope_v129_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w126_63d_slope_v130_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w189_5d_slope_v131_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w189_10d_slope_v132_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w189_21d_slope_v133_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w189_42d_slope_v134_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w189_63d_slope_v135_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w252_5d_slope_v136_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w252_10d_slope_v137_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w252_21d_slope_v138_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w252_42d_slope_v139_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w252_63d_slope_v140_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w378_5d_slope_v141_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w378_10d_slope_v142_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w378_21d_slope_v143_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w378_42d_slope_v144_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w378_63d_slope_v145_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w504_5d_slope_v146_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w504_10d_slope_v147_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w504_21d_slope_v148_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w504_42d_slope_v149_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f15mbs_f15_multi_brand_synergy_ss_w504_63d_slope_v150_signal(revenue, ebitdamargin, closeadj):
    result = _slope_diff_norm(_f15_synergy_score(revenue, ebitdamargin, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f15mbs_f15_multi_brand_synergy_rc_w5_5d_slope_v001_signal,
    f15mbs_f15_multi_brand_synergy_rc_w5_10d_slope_v002_signal,
    f15mbs_f15_multi_brand_synergy_rc_w5_21d_slope_v003_signal,
    f15mbs_f15_multi_brand_synergy_rc_w5_42d_slope_v004_signal,
    f15mbs_f15_multi_brand_synergy_rc_w5_63d_slope_v005_signal,
    f15mbs_f15_multi_brand_synergy_rc_w10_5d_slope_v006_signal,
    f15mbs_f15_multi_brand_synergy_rc_w10_10d_slope_v007_signal,
    f15mbs_f15_multi_brand_synergy_rc_w10_21d_slope_v008_signal,
    f15mbs_f15_multi_brand_synergy_rc_w10_42d_slope_v009_signal,
    f15mbs_f15_multi_brand_synergy_rc_w10_63d_slope_v010_signal,
    f15mbs_f15_multi_brand_synergy_rc_w21_5d_slope_v011_signal,
    f15mbs_f15_multi_brand_synergy_rc_w21_10d_slope_v012_signal,
    f15mbs_f15_multi_brand_synergy_rc_w21_21d_slope_v013_signal,
    f15mbs_f15_multi_brand_synergy_rc_w21_42d_slope_v014_signal,
    f15mbs_f15_multi_brand_synergy_rc_w21_63d_slope_v015_signal,
    f15mbs_f15_multi_brand_synergy_rc_w42_5d_slope_v016_signal,
    f15mbs_f15_multi_brand_synergy_rc_w42_10d_slope_v017_signal,
    f15mbs_f15_multi_brand_synergy_rc_w42_21d_slope_v018_signal,
    f15mbs_f15_multi_brand_synergy_rc_w42_42d_slope_v019_signal,
    f15mbs_f15_multi_brand_synergy_rc_w42_63d_slope_v020_signal,
    f15mbs_f15_multi_brand_synergy_rc_w63_5d_slope_v021_signal,
    f15mbs_f15_multi_brand_synergy_rc_w63_10d_slope_v022_signal,
    f15mbs_f15_multi_brand_synergy_rc_w63_21d_slope_v023_signal,
    f15mbs_f15_multi_brand_synergy_rc_w63_42d_slope_v024_signal,
    f15mbs_f15_multi_brand_synergy_rc_w63_63d_slope_v025_signal,
    f15mbs_f15_multi_brand_synergy_rc_w126_5d_slope_v026_signal,
    f15mbs_f15_multi_brand_synergy_rc_w126_10d_slope_v027_signal,
    f15mbs_f15_multi_brand_synergy_rc_w126_21d_slope_v028_signal,
    f15mbs_f15_multi_brand_synergy_rc_w126_42d_slope_v029_signal,
    f15mbs_f15_multi_brand_synergy_rc_w126_63d_slope_v030_signal,
    f15mbs_f15_multi_brand_synergy_rc_w189_5d_slope_v031_signal,
    f15mbs_f15_multi_brand_synergy_rc_w189_10d_slope_v032_signal,
    f15mbs_f15_multi_brand_synergy_rc_w189_21d_slope_v033_signal,
    f15mbs_f15_multi_brand_synergy_rc_w189_42d_slope_v034_signal,
    f15mbs_f15_multi_brand_synergy_rc_w189_63d_slope_v035_signal,
    f15mbs_f15_multi_brand_synergy_rc_w252_5d_slope_v036_signal,
    f15mbs_f15_multi_brand_synergy_rc_w252_10d_slope_v037_signal,
    f15mbs_f15_multi_brand_synergy_rc_w252_21d_slope_v038_signal,
    f15mbs_f15_multi_brand_synergy_rc_w252_42d_slope_v039_signal,
    f15mbs_f15_multi_brand_synergy_rc_w252_63d_slope_v040_signal,
    f15mbs_f15_multi_brand_synergy_rc_w378_5d_slope_v041_signal,
    f15mbs_f15_multi_brand_synergy_rc_w378_10d_slope_v042_signal,
    f15mbs_f15_multi_brand_synergy_rc_w378_21d_slope_v043_signal,
    f15mbs_f15_multi_brand_synergy_rc_w378_42d_slope_v044_signal,
    f15mbs_f15_multi_brand_synergy_rc_w378_63d_slope_v045_signal,
    f15mbs_f15_multi_brand_synergy_rc_w504_5d_slope_v046_signal,
    f15mbs_f15_multi_brand_synergy_rc_w504_10d_slope_v047_signal,
    f15mbs_f15_multi_brand_synergy_rc_w504_21d_slope_v048_signal,
    f15mbs_f15_multi_brand_synergy_rc_w504_42d_slope_v049_signal,
    f15mbs_f15_multi_brand_synergy_rc_w504_63d_slope_v050_signal,
    f15mbs_f15_multi_brand_synergy_cs_w5_5d_slope_v051_signal,
    f15mbs_f15_multi_brand_synergy_cs_w5_10d_slope_v052_signal,
    f15mbs_f15_multi_brand_synergy_cs_w5_21d_slope_v053_signal,
    f15mbs_f15_multi_brand_synergy_cs_w5_42d_slope_v054_signal,
    f15mbs_f15_multi_brand_synergy_cs_w5_63d_slope_v055_signal,
    f15mbs_f15_multi_brand_synergy_cs_w10_5d_slope_v056_signal,
    f15mbs_f15_multi_brand_synergy_cs_w10_10d_slope_v057_signal,
    f15mbs_f15_multi_brand_synergy_cs_w10_21d_slope_v058_signal,
    f15mbs_f15_multi_brand_synergy_cs_w10_42d_slope_v059_signal,
    f15mbs_f15_multi_brand_synergy_cs_w10_63d_slope_v060_signal,
    f15mbs_f15_multi_brand_synergy_cs_w21_5d_slope_v061_signal,
    f15mbs_f15_multi_brand_synergy_cs_w21_10d_slope_v062_signal,
    f15mbs_f15_multi_brand_synergy_cs_w21_21d_slope_v063_signal,
    f15mbs_f15_multi_brand_synergy_cs_w21_42d_slope_v064_signal,
    f15mbs_f15_multi_brand_synergy_cs_w21_63d_slope_v065_signal,
    f15mbs_f15_multi_brand_synergy_cs_w42_5d_slope_v066_signal,
    f15mbs_f15_multi_brand_synergy_cs_w42_10d_slope_v067_signal,
    f15mbs_f15_multi_brand_synergy_cs_w42_21d_slope_v068_signal,
    f15mbs_f15_multi_brand_synergy_cs_w42_42d_slope_v069_signal,
    f15mbs_f15_multi_brand_synergy_cs_w42_63d_slope_v070_signal,
    f15mbs_f15_multi_brand_synergy_cs_w63_5d_slope_v071_signal,
    f15mbs_f15_multi_brand_synergy_cs_w63_10d_slope_v072_signal,
    f15mbs_f15_multi_brand_synergy_cs_w63_21d_slope_v073_signal,
    f15mbs_f15_multi_brand_synergy_cs_w63_42d_slope_v074_signal,
    f15mbs_f15_multi_brand_synergy_cs_w63_63d_slope_v075_signal,
    f15mbs_f15_multi_brand_synergy_cs_w126_5d_slope_v076_signal,
    f15mbs_f15_multi_brand_synergy_cs_w126_10d_slope_v077_signal,
    f15mbs_f15_multi_brand_synergy_cs_w126_21d_slope_v078_signal,
    f15mbs_f15_multi_brand_synergy_cs_w126_42d_slope_v079_signal,
    f15mbs_f15_multi_brand_synergy_cs_w126_63d_slope_v080_signal,
    f15mbs_f15_multi_brand_synergy_cs_w189_5d_slope_v081_signal,
    f15mbs_f15_multi_brand_synergy_cs_w189_10d_slope_v082_signal,
    f15mbs_f15_multi_brand_synergy_cs_w189_21d_slope_v083_signal,
    f15mbs_f15_multi_brand_synergy_cs_w189_42d_slope_v084_signal,
    f15mbs_f15_multi_brand_synergy_cs_w189_63d_slope_v085_signal,
    f15mbs_f15_multi_brand_synergy_cs_w252_5d_slope_v086_signal,
    f15mbs_f15_multi_brand_synergy_cs_w252_10d_slope_v087_signal,
    f15mbs_f15_multi_brand_synergy_cs_w252_21d_slope_v088_signal,
    f15mbs_f15_multi_brand_synergy_cs_w252_42d_slope_v089_signal,
    f15mbs_f15_multi_brand_synergy_cs_w252_63d_slope_v090_signal,
    f15mbs_f15_multi_brand_synergy_cs_w378_5d_slope_v091_signal,
    f15mbs_f15_multi_brand_synergy_cs_w378_10d_slope_v092_signal,
    f15mbs_f15_multi_brand_synergy_cs_w378_21d_slope_v093_signal,
    f15mbs_f15_multi_brand_synergy_cs_w378_42d_slope_v094_signal,
    f15mbs_f15_multi_brand_synergy_cs_w378_63d_slope_v095_signal,
    f15mbs_f15_multi_brand_synergy_cs_w504_5d_slope_v096_signal,
    f15mbs_f15_multi_brand_synergy_cs_w504_10d_slope_v097_signal,
    f15mbs_f15_multi_brand_synergy_cs_w504_21d_slope_v098_signal,
    f15mbs_f15_multi_brand_synergy_cs_w504_42d_slope_v099_signal,
    f15mbs_f15_multi_brand_synergy_cs_w504_63d_slope_v100_signal,
    f15mbs_f15_multi_brand_synergy_ss_w5_5d_slope_v101_signal,
    f15mbs_f15_multi_brand_synergy_ss_w5_10d_slope_v102_signal,
    f15mbs_f15_multi_brand_synergy_ss_w5_21d_slope_v103_signal,
    f15mbs_f15_multi_brand_synergy_ss_w5_42d_slope_v104_signal,
    f15mbs_f15_multi_brand_synergy_ss_w5_63d_slope_v105_signal,
    f15mbs_f15_multi_brand_synergy_ss_w10_5d_slope_v106_signal,
    f15mbs_f15_multi_brand_synergy_ss_w10_10d_slope_v107_signal,
    f15mbs_f15_multi_brand_synergy_ss_w10_21d_slope_v108_signal,
    f15mbs_f15_multi_brand_synergy_ss_w10_42d_slope_v109_signal,
    f15mbs_f15_multi_brand_synergy_ss_w10_63d_slope_v110_signal,
    f15mbs_f15_multi_brand_synergy_ss_w21_5d_slope_v111_signal,
    f15mbs_f15_multi_brand_synergy_ss_w21_10d_slope_v112_signal,
    f15mbs_f15_multi_brand_synergy_ss_w21_21d_slope_v113_signal,
    f15mbs_f15_multi_brand_synergy_ss_w21_42d_slope_v114_signal,
    f15mbs_f15_multi_brand_synergy_ss_w21_63d_slope_v115_signal,
    f15mbs_f15_multi_brand_synergy_ss_w42_5d_slope_v116_signal,
    f15mbs_f15_multi_brand_synergy_ss_w42_10d_slope_v117_signal,
    f15mbs_f15_multi_brand_synergy_ss_w42_21d_slope_v118_signal,
    f15mbs_f15_multi_brand_synergy_ss_w42_42d_slope_v119_signal,
    f15mbs_f15_multi_brand_synergy_ss_w42_63d_slope_v120_signal,
    f15mbs_f15_multi_brand_synergy_ss_w63_5d_slope_v121_signal,
    f15mbs_f15_multi_brand_synergy_ss_w63_10d_slope_v122_signal,
    f15mbs_f15_multi_brand_synergy_ss_w63_21d_slope_v123_signal,
    f15mbs_f15_multi_brand_synergy_ss_w63_42d_slope_v124_signal,
    f15mbs_f15_multi_brand_synergy_ss_w63_63d_slope_v125_signal,
    f15mbs_f15_multi_brand_synergy_ss_w126_5d_slope_v126_signal,
    f15mbs_f15_multi_brand_synergy_ss_w126_10d_slope_v127_signal,
    f15mbs_f15_multi_brand_synergy_ss_w126_21d_slope_v128_signal,
    f15mbs_f15_multi_brand_synergy_ss_w126_42d_slope_v129_signal,
    f15mbs_f15_multi_brand_synergy_ss_w126_63d_slope_v130_signal,
    f15mbs_f15_multi_brand_synergy_ss_w189_5d_slope_v131_signal,
    f15mbs_f15_multi_brand_synergy_ss_w189_10d_slope_v132_signal,
    f15mbs_f15_multi_brand_synergy_ss_w189_21d_slope_v133_signal,
    f15mbs_f15_multi_brand_synergy_ss_w189_42d_slope_v134_signal,
    f15mbs_f15_multi_brand_synergy_ss_w189_63d_slope_v135_signal,
    f15mbs_f15_multi_brand_synergy_ss_w252_5d_slope_v136_signal,
    f15mbs_f15_multi_brand_synergy_ss_w252_10d_slope_v137_signal,
    f15mbs_f15_multi_brand_synergy_ss_w252_21d_slope_v138_signal,
    f15mbs_f15_multi_brand_synergy_ss_w252_42d_slope_v139_signal,
    f15mbs_f15_multi_brand_synergy_ss_w252_63d_slope_v140_signal,
    f15mbs_f15_multi_brand_synergy_ss_w378_5d_slope_v141_signal,
    f15mbs_f15_multi_brand_synergy_ss_w378_10d_slope_v142_signal,
    f15mbs_f15_multi_brand_synergy_ss_w378_21d_slope_v143_signal,
    f15mbs_f15_multi_brand_synergy_ss_w378_42d_slope_v144_signal,
    f15mbs_f15_multi_brand_synergy_ss_w378_63d_slope_v145_signal,
    f15mbs_f15_multi_brand_synergy_ss_w504_5d_slope_v146_signal,
    f15mbs_f15_multi_brand_synergy_ss_w504_10d_slope_v147_signal,
    f15mbs_f15_multi_brand_synergy_ss_w504_21d_slope_v148_signal,
    f15mbs_f15_multi_brand_synergy_ss_w504_42d_slope_v149_signal,
    f15mbs_f15_multi_brand_synergy_ss_w504_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_MULTI_BRAND_SYNERGY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "capex": capex,
        "assets": assets, "ppnenet": ppnenet,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_revenue_compound", "_f15_compounding_smoothness", "_f15_synergy_score")
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
    print(f"OK f15_multi_brand_synergy_2nd_derivatives_001_150_claude: {n_features} features pass")
