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
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f082_netinc_sign(netinc, w):
    # smoothed sign-like indicator using netinc relative to its rolling mean
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    return (netinc - m) / (netinc.abs() + m.abs()).replace(0, np.nan)


def _f082_breakeven_cross(netinc, w):
    # breakeven proxy: distance of netinc from zero relative to its rolling std
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    return netinc / sd.replace(0, np.nan)


def _f082_profitability_ignition(netinc, w):
    # profitability ignition proxy: smoothed positive-mass weighted by netinc growth
    base_m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    gr = (netinc - base_m) / base_m.abs().replace(0, np.nan)
    return gr * netinc.abs()


def f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v001_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v002_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v003_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v004_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v005_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v006_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v007_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v008_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v009_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v010_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v011_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v012_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v013_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v014_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v015_signal(netinc, closeadj):
    base_pre = _f082_netinc_sign(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v016_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v017_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v018_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v019_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v020_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 21), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v021_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v022_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v023_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v024_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v025_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 63), 126)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v026_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v027_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v028_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v029_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v030_signal(netinc, closeadj):
    base_pre = _z(_f082_netinc_sign(netinc, 252), 504)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v031_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v032_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v033_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v034_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v035_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v036_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v037_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v038_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v039_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v040_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v041_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v042_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v043_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v044_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v045_signal(netinc, closeadj):
    base_pre = _ema(_f082_netinc_sign(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v046_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v047_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v048_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v049_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v050_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v051_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v052_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v053_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v054_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v055_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v056_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v057_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v058_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v059_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v060_signal(netinc, closeadj):
    base_pre = _f082_breakeven_cross(netinc, 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v061_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v062_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v063_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v064_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v065_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v066_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v067_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v068_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v069_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v070_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v071_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v072_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v073_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v074_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v075_signal(netinc, closeadj):
    base_pre = _mean(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v076_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v077_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v078_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v079_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v080_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 21), 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v081_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v082_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v083_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v084_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v085_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 63), 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v086_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v087_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v088_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v089_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v090_signal(netinc, closeadj):
    base_pre = _ema(_f082_breakeven_cross(netinc, 252), 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v091_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v092_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v093_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v094_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v095_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v096_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v097_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v098_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v099_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v100_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v101_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v102_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v103_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v104_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v105_signal(netinc, closeadj):
    base_pre = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v106_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v107_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v108_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v109_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v110_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 21)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v111_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v112_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v113_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v114_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v115_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 63)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v116_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v117_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v118_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v119_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v120_signal(netinc, revenue, closeadj):
    raw = _f082_profitability_ignition(netinc, 252)
    base_pre = raw / revenue.abs().replace(0, np.nan)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v121_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 21)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v122_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 21)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v123_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 21)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v124_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 21)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v125_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 21)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v126_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v127_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v128_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v129_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v130_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v131_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 252)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v132_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 252)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v133_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 252)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v134_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 252)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v135_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _ema(raw, 252)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v136_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v137_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v138_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v139_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v140_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 21) / netinc.abs().rolling(63, min_periods=max(1, 21//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 63)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v141_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 126)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v142_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 126)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v143_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 126)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v144_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 126)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v145_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 63) / netinc.abs().rolling(126, min_periods=max(1, 63//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 126)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v146_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 504)
    base = base_pre * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v147_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 504)
    base = base_pre * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v148_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 504)
    base = base_pre * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v149_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 504)
    base = base_pre * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v150_signal(netinc, closeadj):
    raw = _f082_profitability_ignition(netinc, 252) / netinc.abs().rolling(504, min_periods=max(1, 252//2)).mean().replace(0, np.nan)
    base_pre = _z(raw, 504)
    base = base_pre * closeadj
    result = _jerk(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v001_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v002_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v003_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v004_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_jerk_v005_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v006_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v007_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v008_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v009_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_jerk_v010_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v011_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v012_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v013_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v014_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_jerk_v015_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v016_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v017_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v018_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v019_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_jerk_v020_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v021_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v022_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v023_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v024_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_jerk_v025_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v026_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v027_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v028_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v029_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_jerk_v030_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v031_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v032_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v033_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v034_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_jerk_v035_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v036_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v037_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v038_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v039_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_jerk_v040_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v041_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v042_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v043_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v044_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_jerk_v045_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v046_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v047_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v048_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v049_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_jerk_v050_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v051_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v052_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v053_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v054_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_jerk_v055_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v056_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v057_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v058_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v059_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_jerk_v060_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v061_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v062_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v063_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v064_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_jerk_v065_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v066_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v067_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v068_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v069_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_jerk_v070_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v071_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v072_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v073_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v074_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_jerk_v075_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v076_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v077_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v078_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v079_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_21d_jerk_v080_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v081_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v082_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v083_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v084_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_63d_jerk_v085_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v086_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v087_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v088_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v089_signal,
    f082bcf_f082_breakeven_crossing_flag_bxce_252d_jerk_v090_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v091_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v092_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v093_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v094_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_21d_jerk_v095_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v096_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v097_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v098_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v099_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_63d_jerk_v100_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v101_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v102_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v103_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v104_signal,
    f082bcf_f082_breakeven_crossing_flag_pig_252d_jerk_v105_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v106_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v107_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v108_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v109_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_21d_jerk_v110_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v111_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v112_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v113_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v114_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_63d_jerk_v115_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v116_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v117_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v118_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v119_signal,
    f082bcf_f082_breakeven_crossing_flag_pigr_252d_jerk_v120_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v121_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v122_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v123_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v124_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_21d_jerk_v125_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v126_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v127_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v128_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v129_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_63d_jerk_v130_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v131_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v132_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v133_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v134_signal,
    f082bcf_f082_breakeven_crossing_flag_pige_252d_jerk_v135_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v136_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v137_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v138_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v139_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_21d_jerk_v140_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v141_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v142_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v143_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v144_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_63d_jerk_v145_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v146_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v147_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v148_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v149_signal,
    f082bcf_f082_breakeven_crossing_flag_pigz_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F082_BREAKEVEN_CROSSING_FLAG_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    equity  = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
        "fcf": fcf, "ncfo": ncfo, "cashneq": cashneq, "debt": debt, "equity": equity,
        "sharesbas": sharesbas, "shareswa": shareswa, "marketcap": marketcap,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f082_netinc_sign", "_f082_breakeven_cross", "_f082_profitability_ignition")
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
    print(f"OK f082_breakeven_crossing_flag_3rd_derivatives_001_150_claude: {n_features} features pass")
