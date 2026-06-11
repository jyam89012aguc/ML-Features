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
def _f46_low_vol_signal(closeadj, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std()
    return -vol * closeadj


def _f46_steady_growth(netinc, w):
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = netinc.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f46_compounder_composite(closeadj, netinc, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    m = netinc.rolling(w, min_periods=max(1, w // 2)).mean()
    return (m / vol) * np.sign(closeadj)


# ===== features =====
def f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_sw21_slope_v001_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_sw63_slope_v002_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_sw126_slope_v003_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_sw21_slope_v004_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_sw63_slope_v005_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_sw126_slope_v006_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_sw21_slope_v007_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_sw63_slope_v008_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_sw126_slope_v009_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_sw21_slope_v010_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_sw63_slope_v011_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_sw126_slope_v012_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_sw21_slope_v013_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_sw63_slope_v014_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_sw126_slope_v015_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_sw21_slope_v016_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_sw63_slope_v017_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_sw126_slope_v018_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_sw21_slope_v019_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_sw63_slope_v020_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_sw126_slope_v021_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_sw21_slope_v022_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_sw63_slope_v023_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_sw126_slope_v024_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_sw21_slope_v025_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_sw63_slope_v026_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_sw126_slope_v027_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_sw21_slope_v028_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_sw63_slope_v029_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_sw126_slope_v030_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_sw21_slope_v031_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_sw63_slope_v032_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_sw126_slope_v033_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_sw21_slope_v034_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_sw63_slope_v035_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_sw126_slope_v036_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_sw21_slope_v037_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_sw63_slope_v038_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_sw126_slope_v039_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_sw21_slope_v040_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_sw63_slope_v041_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_sw126_slope_v042_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_sw21_slope_v043_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_sw63_slope_v044_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_sw126_slope_v045_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_sw21_slope_v046_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_sw63_slope_v047_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_sw126_slope_v048_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_sw21_slope_v049_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_sw63_slope_v050_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_sw126_slope_v051_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_sw21_slope_v052_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_sw63_slope_v053_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_sw126_slope_v054_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_sw21_slope_v055_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_sw63_slope_v056_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_sw126_slope_v057_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_sw21_slope_v058_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_sw63_slope_v059_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_sw126_slope_v060_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_sw21_slope_v061_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_sw63_slope_v062_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_sw126_slope_v063_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_sw21_slope_v064_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_sw63_slope_v065_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_sw126_slope_v066_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_sw21_slope_v067_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_sw63_slope_v068_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 42)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_sw126_slope_v069_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 42)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_sw21_slope_v070_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_sw63_slope_v071_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_sw126_slope_v072_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_sw21_slope_v073_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_sw63_slope_v074_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 42)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_sw126_slope_v075_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 42)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_sw21_slope_v076_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_sw63_slope_v077_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_sw126_slope_v078_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_sw21_slope_v079_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_sw63_slope_v080_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 42)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_sw126_slope_v081_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 42)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_sw21_slope_v082_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_sw63_slope_v083_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_sw126_slope_v084_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_sw21_slope_v085_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_sw63_slope_v086_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_sw126_slope_v087_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_sw21_slope_v088_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_sw63_slope_v089_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_sw126_slope_v090_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_sw21_slope_v091_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_sw63_slope_v092_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_sw126_slope_v093_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_sw21_slope_v094_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_sw63_slope_v095_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_sw126_slope_v096_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_sw21_slope_v097_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_sw63_slope_v098_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_sw126_slope_v099_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_sw21_slope_v100_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_sw63_slope_v101_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_sw126_slope_v102_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_sw21_slope_v103_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_sw63_slope_v104_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_sw126_slope_v105_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_sw21_slope_v106_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_sw63_slope_v107_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_sw126_slope_v108_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_sw21_slope_v109_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 84)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_sw63_slope_v110_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 84)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_sw126_slope_v111_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 84)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_sw21_slope_v112_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_sw63_slope_v113_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_sw126_slope_v114_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_sw21_slope_v115_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 84)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_sw63_slope_v116_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 84)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_sw126_slope_v117_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 84)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_sw21_slope_v118_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_sw63_slope_v119_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_sw126_slope_v120_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_sw21_slope_v121_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 84)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_sw63_slope_v122_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 84)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_sw126_slope_v123_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 84)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_sw21_slope_v124_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_sw63_slope_v125_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_sw126_slope_v126_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_sw21_slope_v127_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_sw63_slope_v128_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_sw126_slope_v129_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_sw21_slope_v130_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 105)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_sw63_slope_v131_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 105)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_sw126_slope_v132_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 105)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_sw21_slope_v133_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_sw63_slope_v134_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_sw126_slope_v135_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_sw21_slope_v136_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 105)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_sw63_slope_v137_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 105)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_sw126_slope_v138_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 105)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_sw21_slope_v139_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_sw63_slope_v140_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_sw126_slope_v141_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_sw21_slope_v142_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 105)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_sw63_slope_v143_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 105)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_sw126_slope_v144_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 105)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_sw21_slope_v145_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_sw63_slope_v146_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_sw126_slope_v147_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_sw21_slope_v148_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_sw63_slope_v149_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_sw126_slope_v150_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_sw21_slope_v001_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_sw63_slope_v002_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_sw126_slope_v003_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_sw21_slope_v004_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_sw63_slope_v005_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_sw126_slope_v006_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_sw21_slope_v007_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_sw63_slope_v008_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_sw126_slope_v009_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_sw21_slope_v010_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_sw63_slope_v011_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_sw126_slope_v012_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_sw21_slope_v013_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_sw63_slope_v014_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_sw126_slope_v015_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_sw21_slope_v016_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_sw63_slope_v017_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_sw126_slope_v018_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_sw21_slope_v019_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_sw63_slope_v020_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_sw126_slope_v021_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_sw21_slope_v022_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_sw63_slope_v023_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_sw126_slope_v024_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_sw21_slope_v025_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_sw63_slope_v026_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_sw126_slope_v027_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_sw21_slope_v028_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_sw63_slope_v029_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_sw126_slope_v030_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_sw21_slope_v031_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_sw63_slope_v032_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_sw126_slope_v033_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_sw21_slope_v034_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_sw63_slope_v035_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_sw126_slope_v036_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_sw21_slope_v037_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_sw63_slope_v038_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_sw126_slope_v039_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_sw21_slope_v040_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_sw63_slope_v041_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_sw126_slope_v042_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_sw21_slope_v043_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_sw63_slope_v044_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_sw126_slope_v045_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_sw21_slope_v046_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_sw63_slope_v047_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_sw126_slope_v048_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_sw21_slope_v049_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_sw63_slope_v050_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_sw126_slope_v051_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_sw21_slope_v052_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_sw63_slope_v053_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_sw126_slope_v054_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_sw21_slope_v055_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_sw63_slope_v056_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_sw126_slope_v057_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_sw21_slope_v058_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_sw63_slope_v059_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_sw126_slope_v060_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_sw21_slope_v061_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_sw63_slope_v062_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_sw126_slope_v063_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_sw21_slope_v064_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_sw63_slope_v065_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_sw126_slope_v066_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_sw21_slope_v067_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_sw63_slope_v068_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_sw126_slope_v069_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_sw21_slope_v070_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_sw63_slope_v071_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_sw126_slope_v072_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_sw21_slope_v073_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_sw63_slope_v074_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_sw126_slope_v075_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_sw21_slope_v076_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_sw63_slope_v077_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_sw126_slope_v078_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_sw21_slope_v079_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_sw63_slope_v080_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_sw126_slope_v081_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_sw21_slope_v082_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_sw63_slope_v083_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_sw126_slope_v084_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_sw21_slope_v085_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_sw63_slope_v086_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_sw126_slope_v087_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_sw21_slope_v088_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_sw63_slope_v089_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_sw126_slope_v090_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_sw21_slope_v091_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_sw63_slope_v092_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_sw126_slope_v093_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_sw21_slope_v094_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_sw63_slope_v095_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_sw126_slope_v096_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_sw21_slope_v097_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_sw63_slope_v098_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_sw126_slope_v099_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_sw21_slope_v100_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_sw63_slope_v101_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_sw126_slope_v102_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_sw21_slope_v103_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_sw63_slope_v104_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_sw126_slope_v105_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_sw21_slope_v106_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_sw63_slope_v107_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_sw126_slope_v108_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_sw21_slope_v109_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_sw63_slope_v110_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_sw126_slope_v111_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_sw21_slope_v112_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_sw63_slope_v113_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_sw126_slope_v114_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_sw21_slope_v115_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_sw63_slope_v116_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_sw126_slope_v117_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_sw21_slope_v118_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_sw63_slope_v119_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_sw126_slope_v120_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_sw21_slope_v121_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_sw63_slope_v122_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_sw126_slope_v123_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_sw21_slope_v124_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_sw63_slope_v125_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_sw126_slope_v126_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_sw21_slope_v127_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_sw63_slope_v128_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_sw126_slope_v129_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_sw21_slope_v130_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_sw63_slope_v131_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_sw126_slope_v132_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_sw21_slope_v133_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_sw63_slope_v134_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_sw126_slope_v135_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_sw21_slope_v136_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_sw63_slope_v137_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_sw126_slope_v138_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_sw21_slope_v139_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_sw63_slope_v140_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_sw126_slope_v141_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_sw21_slope_v142_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_sw63_slope_v143_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_sw126_slope_v144_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_sw21_slope_v145_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_sw63_slope_v146_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_sw126_slope_v147_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_sw21_slope_v148_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_sw63_slope_v149_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_sw126_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_UTILITY_COMPOUNDER_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    cols = {"closeadj": closeadj, "ebitda": ebitda, "eps": eps, "netinc": netinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_low_vol_signal", "_f46_steady_growth", "_f46_compounder_composite",)
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
    print(f"OK f46_quiet_utility_compounder_2nd_derivatives_001_150_claude: {n_features} features pass")
