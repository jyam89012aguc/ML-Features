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

def _f11_revenue_per_asset(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f11_ebitda_per_asset(ebitda, assets):
    return ebitda / assets.replace(0, np.nan)


def _f11_unit_econ_score(revenue, ebitda, assets, w):
    rpa = revenue / assets.replace(0, np.nan)
    epa = ebitda / assets.replace(0, np.nan)
    rpa_m = rpa.rolling(w, min_periods=max(1, w // 2)).mean()
    epa_m = epa.rolling(w, min_periods=max(1, w // 2)).mean()
    return rpa_m * 0.5 + epa_m * 0.5


# ===== features =====

def f11rue_f11_restaurant_unit_economics_rpa_w5_5d_jerk_v001_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w5_10d_jerk_v002_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w5_21d_jerk_v003_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w5_42d_jerk_v004_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w5_63d_jerk_v005_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w10_5d_jerk_v006_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w10_10d_jerk_v007_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w10_21d_jerk_v008_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w10_42d_jerk_v009_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w10_63d_jerk_v010_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w21_5d_jerk_v011_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w21_10d_jerk_v012_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w21_21d_jerk_v013_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w21_42d_jerk_v014_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w21_63d_jerk_v015_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w42_5d_jerk_v016_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w42_10d_jerk_v017_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w42_21d_jerk_v018_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w42_42d_jerk_v019_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w42_63d_jerk_v020_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w63_5d_jerk_v021_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w63_10d_jerk_v022_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w63_21d_jerk_v023_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w63_42d_jerk_v024_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w63_63d_jerk_v025_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w126_5d_jerk_v026_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w126_10d_jerk_v027_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w126_21d_jerk_v028_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w126_42d_jerk_v029_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w126_63d_jerk_v030_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w189_5d_jerk_v031_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w189_10d_jerk_v032_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w189_21d_jerk_v033_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w189_42d_jerk_v034_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w189_63d_jerk_v035_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w252_5d_jerk_v036_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w252_10d_jerk_v037_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w252_21d_jerk_v038_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w252_42d_jerk_v039_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w252_63d_jerk_v040_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w378_5d_jerk_v041_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w378_10d_jerk_v042_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w378_21d_jerk_v043_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w378_42d_jerk_v044_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w378_63d_jerk_v045_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w504_5d_jerk_v046_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w504_10d_jerk_v047_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w504_21d_jerk_v048_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w504_42d_jerk_v049_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_rpa_w504_63d_jerk_v050_signal(revenue, assets, closeadj):
    result = _jerk(_mean(_f11_revenue_per_asset(revenue, assets), 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w5_5d_jerk_v051_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w5_10d_jerk_v052_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w5_21d_jerk_v053_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w5_42d_jerk_v054_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w5_63d_jerk_v055_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w10_5d_jerk_v056_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w10_10d_jerk_v057_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w10_21d_jerk_v058_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w10_42d_jerk_v059_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w10_63d_jerk_v060_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w21_5d_jerk_v061_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w21_10d_jerk_v062_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w21_21d_jerk_v063_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w21_42d_jerk_v064_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w21_63d_jerk_v065_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w42_5d_jerk_v066_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w42_10d_jerk_v067_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w42_21d_jerk_v068_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w42_42d_jerk_v069_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w42_63d_jerk_v070_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w63_5d_jerk_v071_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w63_10d_jerk_v072_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w63_21d_jerk_v073_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w63_42d_jerk_v074_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w63_63d_jerk_v075_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w126_5d_jerk_v076_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w126_10d_jerk_v077_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w126_21d_jerk_v078_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w126_42d_jerk_v079_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w126_63d_jerk_v080_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w189_5d_jerk_v081_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w189_10d_jerk_v082_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w189_21d_jerk_v083_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w189_42d_jerk_v084_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w189_63d_jerk_v085_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w252_5d_jerk_v086_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w252_10d_jerk_v087_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w252_21d_jerk_v088_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w252_42d_jerk_v089_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w252_63d_jerk_v090_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w378_5d_jerk_v091_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w378_10d_jerk_v092_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w378_21d_jerk_v093_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w378_42d_jerk_v094_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w378_63d_jerk_v095_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w504_5d_jerk_v096_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w504_10d_jerk_v097_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w504_21d_jerk_v098_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w504_42d_jerk_v099_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_epa_w504_63d_jerk_v100_signal(ebitda, assets, closeadj):
    result = _jerk(_mean(_f11_ebitda_per_asset(ebitda, assets), 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w5_5d_jerk_v101_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 5), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w5_10d_jerk_v102_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 5), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w5_21d_jerk_v103_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 5), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w5_42d_jerk_v104_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 5), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w5_63d_jerk_v105_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 5), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w10_5d_jerk_v106_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 10), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w10_10d_jerk_v107_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 10), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w10_21d_jerk_v108_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 10), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w10_42d_jerk_v109_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 10), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w10_63d_jerk_v110_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 10), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w21_5d_jerk_v111_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 21), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w21_10d_jerk_v112_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 21), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w21_21d_jerk_v113_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 21), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w21_42d_jerk_v114_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 21), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w21_63d_jerk_v115_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 21), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w42_5d_jerk_v116_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 42), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w42_10d_jerk_v117_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 42), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w42_21d_jerk_v118_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 42), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w42_42d_jerk_v119_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 42), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w42_63d_jerk_v120_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w63_5d_jerk_v121_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 63), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w63_10d_jerk_v122_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 63), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w63_21d_jerk_v123_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 63), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w63_42d_jerk_v124_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 63), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w63_63d_jerk_v125_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 63), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w126_5d_jerk_v126_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 126), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w126_10d_jerk_v127_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 126), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w126_21d_jerk_v128_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w126_42d_jerk_v129_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 126), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w126_63d_jerk_v130_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 126), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w189_5d_jerk_v131_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 189), 5) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w189_10d_jerk_v132_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 189), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w189_21d_jerk_v133_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 189), 21) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w189_42d_jerk_v134_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 189), 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w189_63d_jerk_v135_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 189), 63) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w252_5d_jerk_v136_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 252), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w252_10d_jerk_v137_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 252), 10) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w252_21d_jerk_v138_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 252), 21) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w252_42d_jerk_v139_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 252), 42) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w252_63d_jerk_v140_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w378_5d_jerk_v141_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 378), 5) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w378_10d_jerk_v142_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 378), 10) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w378_21d_jerk_v143_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 378), 21) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w378_42d_jerk_v144_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 378), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w378_63d_jerk_v145_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 378), 63) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w504_5d_jerk_v146_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 504), 5) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w504_10d_jerk_v147_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 504), 10) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w504_21d_jerk_v148_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 504), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w504_42d_jerk_v149_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 504), 42) * _z(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f11rue_f11_restaurant_unit_economics_ues_w504_63d_jerk_v150_signal(revenue, ebitda, assets, closeadj):
    result = _jerk(_f11_unit_econ_score(revenue, ebitda, assets, 504), 63) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f11rue_f11_restaurant_unit_economics_rpa_w5_5d_jerk_v001_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w5_10d_jerk_v002_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w5_21d_jerk_v003_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w5_42d_jerk_v004_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w5_63d_jerk_v005_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w10_5d_jerk_v006_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w10_10d_jerk_v007_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w10_21d_jerk_v008_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w10_42d_jerk_v009_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w10_63d_jerk_v010_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w21_5d_jerk_v011_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w21_10d_jerk_v012_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w21_21d_jerk_v013_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w21_42d_jerk_v014_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w21_63d_jerk_v015_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w42_5d_jerk_v016_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w42_10d_jerk_v017_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w42_21d_jerk_v018_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w42_42d_jerk_v019_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w42_63d_jerk_v020_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w63_5d_jerk_v021_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w63_10d_jerk_v022_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w63_21d_jerk_v023_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w63_42d_jerk_v024_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w63_63d_jerk_v025_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w126_5d_jerk_v026_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w126_10d_jerk_v027_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w126_21d_jerk_v028_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w126_42d_jerk_v029_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w126_63d_jerk_v030_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w189_5d_jerk_v031_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w189_10d_jerk_v032_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w189_21d_jerk_v033_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w189_42d_jerk_v034_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w189_63d_jerk_v035_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w252_5d_jerk_v036_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w252_10d_jerk_v037_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w252_21d_jerk_v038_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w252_42d_jerk_v039_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w252_63d_jerk_v040_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w378_5d_jerk_v041_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w378_10d_jerk_v042_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w378_21d_jerk_v043_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w378_42d_jerk_v044_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w378_63d_jerk_v045_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w504_5d_jerk_v046_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w504_10d_jerk_v047_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w504_21d_jerk_v048_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w504_42d_jerk_v049_signal,
    f11rue_f11_restaurant_unit_economics_rpa_w504_63d_jerk_v050_signal,
    f11rue_f11_restaurant_unit_economics_epa_w5_5d_jerk_v051_signal,
    f11rue_f11_restaurant_unit_economics_epa_w5_10d_jerk_v052_signal,
    f11rue_f11_restaurant_unit_economics_epa_w5_21d_jerk_v053_signal,
    f11rue_f11_restaurant_unit_economics_epa_w5_42d_jerk_v054_signal,
    f11rue_f11_restaurant_unit_economics_epa_w5_63d_jerk_v055_signal,
    f11rue_f11_restaurant_unit_economics_epa_w10_5d_jerk_v056_signal,
    f11rue_f11_restaurant_unit_economics_epa_w10_10d_jerk_v057_signal,
    f11rue_f11_restaurant_unit_economics_epa_w10_21d_jerk_v058_signal,
    f11rue_f11_restaurant_unit_economics_epa_w10_42d_jerk_v059_signal,
    f11rue_f11_restaurant_unit_economics_epa_w10_63d_jerk_v060_signal,
    f11rue_f11_restaurant_unit_economics_epa_w21_5d_jerk_v061_signal,
    f11rue_f11_restaurant_unit_economics_epa_w21_10d_jerk_v062_signal,
    f11rue_f11_restaurant_unit_economics_epa_w21_21d_jerk_v063_signal,
    f11rue_f11_restaurant_unit_economics_epa_w21_42d_jerk_v064_signal,
    f11rue_f11_restaurant_unit_economics_epa_w21_63d_jerk_v065_signal,
    f11rue_f11_restaurant_unit_economics_epa_w42_5d_jerk_v066_signal,
    f11rue_f11_restaurant_unit_economics_epa_w42_10d_jerk_v067_signal,
    f11rue_f11_restaurant_unit_economics_epa_w42_21d_jerk_v068_signal,
    f11rue_f11_restaurant_unit_economics_epa_w42_42d_jerk_v069_signal,
    f11rue_f11_restaurant_unit_economics_epa_w42_63d_jerk_v070_signal,
    f11rue_f11_restaurant_unit_economics_epa_w63_5d_jerk_v071_signal,
    f11rue_f11_restaurant_unit_economics_epa_w63_10d_jerk_v072_signal,
    f11rue_f11_restaurant_unit_economics_epa_w63_21d_jerk_v073_signal,
    f11rue_f11_restaurant_unit_economics_epa_w63_42d_jerk_v074_signal,
    f11rue_f11_restaurant_unit_economics_epa_w63_63d_jerk_v075_signal,
    f11rue_f11_restaurant_unit_economics_epa_w126_5d_jerk_v076_signal,
    f11rue_f11_restaurant_unit_economics_epa_w126_10d_jerk_v077_signal,
    f11rue_f11_restaurant_unit_economics_epa_w126_21d_jerk_v078_signal,
    f11rue_f11_restaurant_unit_economics_epa_w126_42d_jerk_v079_signal,
    f11rue_f11_restaurant_unit_economics_epa_w126_63d_jerk_v080_signal,
    f11rue_f11_restaurant_unit_economics_epa_w189_5d_jerk_v081_signal,
    f11rue_f11_restaurant_unit_economics_epa_w189_10d_jerk_v082_signal,
    f11rue_f11_restaurant_unit_economics_epa_w189_21d_jerk_v083_signal,
    f11rue_f11_restaurant_unit_economics_epa_w189_42d_jerk_v084_signal,
    f11rue_f11_restaurant_unit_economics_epa_w189_63d_jerk_v085_signal,
    f11rue_f11_restaurant_unit_economics_epa_w252_5d_jerk_v086_signal,
    f11rue_f11_restaurant_unit_economics_epa_w252_10d_jerk_v087_signal,
    f11rue_f11_restaurant_unit_economics_epa_w252_21d_jerk_v088_signal,
    f11rue_f11_restaurant_unit_economics_epa_w252_42d_jerk_v089_signal,
    f11rue_f11_restaurant_unit_economics_epa_w252_63d_jerk_v090_signal,
    f11rue_f11_restaurant_unit_economics_epa_w378_5d_jerk_v091_signal,
    f11rue_f11_restaurant_unit_economics_epa_w378_10d_jerk_v092_signal,
    f11rue_f11_restaurant_unit_economics_epa_w378_21d_jerk_v093_signal,
    f11rue_f11_restaurant_unit_economics_epa_w378_42d_jerk_v094_signal,
    f11rue_f11_restaurant_unit_economics_epa_w378_63d_jerk_v095_signal,
    f11rue_f11_restaurant_unit_economics_epa_w504_5d_jerk_v096_signal,
    f11rue_f11_restaurant_unit_economics_epa_w504_10d_jerk_v097_signal,
    f11rue_f11_restaurant_unit_economics_epa_w504_21d_jerk_v098_signal,
    f11rue_f11_restaurant_unit_economics_epa_w504_42d_jerk_v099_signal,
    f11rue_f11_restaurant_unit_economics_epa_w504_63d_jerk_v100_signal,
    f11rue_f11_restaurant_unit_economics_ues_w5_5d_jerk_v101_signal,
    f11rue_f11_restaurant_unit_economics_ues_w5_10d_jerk_v102_signal,
    f11rue_f11_restaurant_unit_economics_ues_w5_21d_jerk_v103_signal,
    f11rue_f11_restaurant_unit_economics_ues_w5_42d_jerk_v104_signal,
    f11rue_f11_restaurant_unit_economics_ues_w5_63d_jerk_v105_signal,
    f11rue_f11_restaurant_unit_economics_ues_w10_5d_jerk_v106_signal,
    f11rue_f11_restaurant_unit_economics_ues_w10_10d_jerk_v107_signal,
    f11rue_f11_restaurant_unit_economics_ues_w10_21d_jerk_v108_signal,
    f11rue_f11_restaurant_unit_economics_ues_w10_42d_jerk_v109_signal,
    f11rue_f11_restaurant_unit_economics_ues_w10_63d_jerk_v110_signal,
    f11rue_f11_restaurant_unit_economics_ues_w21_5d_jerk_v111_signal,
    f11rue_f11_restaurant_unit_economics_ues_w21_10d_jerk_v112_signal,
    f11rue_f11_restaurant_unit_economics_ues_w21_21d_jerk_v113_signal,
    f11rue_f11_restaurant_unit_economics_ues_w21_42d_jerk_v114_signal,
    f11rue_f11_restaurant_unit_economics_ues_w21_63d_jerk_v115_signal,
    f11rue_f11_restaurant_unit_economics_ues_w42_5d_jerk_v116_signal,
    f11rue_f11_restaurant_unit_economics_ues_w42_10d_jerk_v117_signal,
    f11rue_f11_restaurant_unit_economics_ues_w42_21d_jerk_v118_signal,
    f11rue_f11_restaurant_unit_economics_ues_w42_42d_jerk_v119_signal,
    f11rue_f11_restaurant_unit_economics_ues_w42_63d_jerk_v120_signal,
    f11rue_f11_restaurant_unit_economics_ues_w63_5d_jerk_v121_signal,
    f11rue_f11_restaurant_unit_economics_ues_w63_10d_jerk_v122_signal,
    f11rue_f11_restaurant_unit_economics_ues_w63_21d_jerk_v123_signal,
    f11rue_f11_restaurant_unit_economics_ues_w63_42d_jerk_v124_signal,
    f11rue_f11_restaurant_unit_economics_ues_w63_63d_jerk_v125_signal,
    f11rue_f11_restaurant_unit_economics_ues_w126_5d_jerk_v126_signal,
    f11rue_f11_restaurant_unit_economics_ues_w126_10d_jerk_v127_signal,
    f11rue_f11_restaurant_unit_economics_ues_w126_21d_jerk_v128_signal,
    f11rue_f11_restaurant_unit_economics_ues_w126_42d_jerk_v129_signal,
    f11rue_f11_restaurant_unit_economics_ues_w126_63d_jerk_v130_signal,
    f11rue_f11_restaurant_unit_economics_ues_w189_5d_jerk_v131_signal,
    f11rue_f11_restaurant_unit_economics_ues_w189_10d_jerk_v132_signal,
    f11rue_f11_restaurant_unit_economics_ues_w189_21d_jerk_v133_signal,
    f11rue_f11_restaurant_unit_economics_ues_w189_42d_jerk_v134_signal,
    f11rue_f11_restaurant_unit_economics_ues_w189_63d_jerk_v135_signal,
    f11rue_f11_restaurant_unit_economics_ues_w252_5d_jerk_v136_signal,
    f11rue_f11_restaurant_unit_economics_ues_w252_10d_jerk_v137_signal,
    f11rue_f11_restaurant_unit_economics_ues_w252_21d_jerk_v138_signal,
    f11rue_f11_restaurant_unit_economics_ues_w252_42d_jerk_v139_signal,
    f11rue_f11_restaurant_unit_economics_ues_w252_63d_jerk_v140_signal,
    f11rue_f11_restaurant_unit_economics_ues_w378_5d_jerk_v141_signal,
    f11rue_f11_restaurant_unit_economics_ues_w378_10d_jerk_v142_signal,
    f11rue_f11_restaurant_unit_economics_ues_w378_21d_jerk_v143_signal,
    f11rue_f11_restaurant_unit_economics_ues_w378_42d_jerk_v144_signal,
    f11rue_f11_restaurant_unit_economics_ues_w378_63d_jerk_v145_signal,
    f11rue_f11_restaurant_unit_economics_ues_w504_5d_jerk_v146_signal,
    f11rue_f11_restaurant_unit_economics_ues_w504_10d_jerk_v147_signal,
    f11rue_f11_restaurant_unit_economics_ues_w504_21d_jerk_v148_signal,
    f11rue_f11_restaurant_unit_economics_ues_w504_42d_jerk_v149_signal,
    f11rue_f11_restaurant_unit_economics_ues_w504_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RESTAURANT_UNIT_ECONOMICS_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f11_revenue_per_asset", "_f11_ebitda_per_asset", "_f11_unit_econ_score")
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
    print(f"OK f11_restaurant_unit_economics_3rd_derivatives_001_150_claude: {n_features} features pass")
