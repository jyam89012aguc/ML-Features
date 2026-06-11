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


def f082bcf_f082_breakeven_crossing_flag_nis_21d_xclose_base_v001_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_xrev_base_v002_signal(netinc, closeadj, revenue):
    base = _f082_netinc_sign(netinc, 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_xemac_base_v003_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_xmean_base_v004_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_21d_xclose2_base_v005_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_xclose_base_v006_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_xrev_base_v007_signal(netinc, closeadj, revenue):
    base = _f082_netinc_sign(netinc, 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_xemac_base_v008_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_xmean_base_v009_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_63d_xclose2_base_v010_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_xclose_base_v011_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_xrev_base_v012_signal(netinc, closeadj, revenue):
    base = _f082_netinc_sign(netinc, 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_xemac_base_v013_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_xmean_base_v014_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nis_252d_xclose2_base_v015_signal(netinc, closeadj):
    base = _f082_netinc_sign(netinc, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_xclose_base_v016_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 21), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_xrev_base_v017_signal(netinc, closeadj, revenue):
    base = _z(_f082_netinc_sign(netinc, 21), 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_xemac_base_v018_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 21), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_xmean_base_v019_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 21), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_21d_xclose2_base_v020_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 21), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_xclose_base_v021_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 63), 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_xrev_base_v022_signal(netinc, closeadj, revenue):
    base = _z(_f082_netinc_sign(netinc, 63), 126)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_xemac_base_v023_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 63), 126)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_xmean_base_v024_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 63), 126)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_63d_xclose2_base_v025_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 63), 126)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_xclose_base_v026_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 252), 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_xrev_base_v027_signal(netinc, closeadj, revenue):
    base = _z(_f082_netinc_sign(netinc, 252), 504)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_xemac_base_v028_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 252), 504)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_xmean_base_v029_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 252), 504)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nisz_252d_xclose2_base_v030_signal(netinc, closeadj):
    base = _z(_f082_netinc_sign(netinc, 252), 504)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_xclose_base_v031_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_xrev_base_v032_signal(netinc, closeadj, revenue):
    base = _ema(_f082_netinc_sign(netinc, 21), 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_xemac_base_v033_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_xmean_base_v034_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_21d_xclose2_base_v035_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_xclose_base_v036_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_xrev_base_v037_signal(netinc, closeadj, revenue):
    base = _ema(_f082_netinc_sign(netinc, 63), 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_xemac_base_v038_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_xmean_base_v039_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_63d_xclose2_base_v040_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_xclose_base_v041_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_xrev_base_v042_signal(netinc, closeadj, revenue):
    base = _ema(_f082_netinc_sign(netinc, 252), 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_xemac_base_v043_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_xmean_base_v044_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_nise_252d_xclose2_base_v045_signal(netinc, closeadj):
    base = _ema(_f082_netinc_sign(netinc, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_xclose_base_v046_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_xrev_base_v047_signal(netinc, closeadj, revenue):
    base = _f082_breakeven_cross(netinc, 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_xemac_base_v048_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_xmean_base_v049_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_21d_xclose2_base_v050_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_xclose_base_v051_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_xrev_base_v052_signal(netinc, closeadj, revenue):
    base = _f082_breakeven_cross(netinc, 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_xemac_base_v053_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_xmean_base_v054_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_63d_xclose2_base_v055_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_xclose_base_v056_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_xrev_base_v057_signal(netinc, closeadj, revenue):
    base = _f082_breakeven_cross(netinc, 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_xemac_base_v058_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_xmean_base_v059_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxc_252d_xclose2_base_v060_signal(netinc, closeadj):
    base = _f082_breakeven_cross(netinc, 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xclose_base_v061_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 21), 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xrev_base_v062_signal(netinc, closeadj, revenue):
    base = _mean(_f082_breakeven_cross(netinc, 21), 21)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xemac_base_v063_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 21), 21)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xmean_base_v064_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 21), 21)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xclose2_base_v065_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 21), 21)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xclose_base_v066_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 63), 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xrev_base_v067_signal(netinc, closeadj, revenue):
    base = _mean(_f082_breakeven_cross(netinc, 63), 63)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xemac_base_v068_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 63), 63)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xmean_base_v069_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 63), 63)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xclose2_base_v070_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 63), 63)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xclose_base_v071_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 252), 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xrev_base_v072_signal(netinc, closeadj, revenue):
    base = _mean(_f082_breakeven_cross(netinc, 252), 252)
    result = base * revenue / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xemac_base_v073_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 252), 252)
    result = base * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xmean_base_v074_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 252), 252)
    result = base * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xclose2_base_v075_signal(netinc, closeadj):
    base = _mean(_f082_breakeven_cross(netinc, 252), 252)
    result = base * closeadj * (1.0 + closeadj.pct_change(21).fillna(0))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f082bcf_f082_breakeven_crossing_flag_nis_21d_xclose_base_v001_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_xrev_base_v002_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_xemac_base_v003_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_xmean_base_v004_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_21d_xclose2_base_v005_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_xclose_base_v006_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_xrev_base_v007_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_xemac_base_v008_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_xmean_base_v009_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_63d_xclose2_base_v010_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_xclose_base_v011_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_xrev_base_v012_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_xemac_base_v013_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_xmean_base_v014_signal,
    f082bcf_f082_breakeven_crossing_flag_nis_252d_xclose2_base_v015_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_xclose_base_v016_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_xrev_base_v017_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_xemac_base_v018_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_xmean_base_v019_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_21d_xclose2_base_v020_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_xclose_base_v021_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_xrev_base_v022_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_xemac_base_v023_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_xmean_base_v024_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_63d_xclose2_base_v025_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_xclose_base_v026_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_xrev_base_v027_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_xemac_base_v028_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_xmean_base_v029_signal,
    f082bcf_f082_breakeven_crossing_flag_nisz_252d_xclose2_base_v030_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_xclose_base_v031_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_xrev_base_v032_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_xemac_base_v033_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_xmean_base_v034_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_21d_xclose2_base_v035_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_xclose_base_v036_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_xrev_base_v037_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_xemac_base_v038_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_xmean_base_v039_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_63d_xclose2_base_v040_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_xclose_base_v041_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_xrev_base_v042_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_xemac_base_v043_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_xmean_base_v044_signal,
    f082bcf_f082_breakeven_crossing_flag_nise_252d_xclose2_base_v045_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_xclose_base_v046_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_xrev_base_v047_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_xemac_base_v048_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_xmean_base_v049_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_21d_xclose2_base_v050_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_xclose_base_v051_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_xrev_base_v052_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_xemac_base_v053_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_xmean_base_v054_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_63d_xclose2_base_v055_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_xclose_base_v056_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_xrev_base_v057_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_xemac_base_v058_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_xmean_base_v059_signal,
    f082bcf_f082_breakeven_crossing_flag_bxc_252d_xclose2_base_v060_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xclose_base_v061_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xrev_base_v062_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xemac_base_v063_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xmean_base_v064_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_21d_xclose2_base_v065_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xclose_base_v066_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xrev_base_v067_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xemac_base_v068_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xmean_base_v069_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_63d_xclose2_base_v070_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xclose_base_v071_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xrev_base_v072_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xemac_base_v073_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xmean_base_v074_signal,
    f082bcf_f082_breakeven_crossing_flag_bxcm_252d_xclose2_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F082_BREAKEVEN_CROSSING_FLAG_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f082_breakeven_crossing_flag_base_001_075_claude: {n_features} features pass")
