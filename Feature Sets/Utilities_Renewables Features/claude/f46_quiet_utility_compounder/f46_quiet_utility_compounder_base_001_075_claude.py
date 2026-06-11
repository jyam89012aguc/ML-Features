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
def f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_base_v001_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_base_v002_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_base_v003_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_base_v004_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_base_v005_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_base_v006_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_base_v007_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_base_v008_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_base_v009_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_base_v010_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_base_v011_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_base_v012_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_base_v013_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_base_v014_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_base_v015_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_base_v016_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_base_v017_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_base_v018_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_base_v019_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_base_v020_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_base_v021_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_base_v022_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_base_v023_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_base_v024_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_base_v025_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_base_v026_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_base_v027_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_base_v028_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_base_v029_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_base_v030_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_base_v031_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_base_v032_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_base_v033_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_base_v034_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_base_v035_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_base_v036_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_base_v037_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_base_v038_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_base_v039_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_base_v040_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_base_v041_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_base_v042_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_base_v043_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_base_v044_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_base_v045_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_base_v046_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_base_v047_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_base_v048_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_base_v049_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_base_v050_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_126d_s00_base_v051_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_126d_s00_base_v052_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_126d_s00_base_v053_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_126d_s00_base_v054_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_126d_s00_base_v055_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_126d_s00_base_v056_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_147d_s00_base_v057_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_147d_s00_base_v058_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_147d_s00_base_v059_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_147d_s00_base_v060_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_147d_s00_base_v061_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_147d_s00_base_v062_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_147d_s00_base_v063_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_168d_s00_base_v064_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_168d_s00_base_v065_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_168d_s00_base_v066_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_168d_s00_base_v067_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_168d_s00_base_v068_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ebitda_168d_s00_base_v069_signal(closeadj, ebitda):
    base = _f46_compounder_composite(closeadj, ebitda, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_eps_168d_s00_base_v070_signal(closeadj, eps):
    base = _f46_compounder_composite(closeadj, eps, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_lv_close_189d_s00_base_v071_signal(closeadj, netinc):
    base = _f46_low_vol_signal(closeadj, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_netinc_189d_s00_base_v072_signal(netinc, closeadj):
    base = _f46_steady_growth(netinc, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_ebitda_189d_s00_base_v073_signal(ebitda, closeadj):
    base = _f46_steady_growth(ebitda, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_sg_eps_189d_s00_base_v074_signal(eps, closeadj):
    base = _f46_steady_growth(eps, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f46quc_f46_quiet_utility_compounder_cc_ni_189d_s00_base_v075_signal(closeadj, netinc):
    base = _f46_compounder_composite(closeadj, netinc, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46quc_f46_quiet_utility_compounder_lv_close_5d_s00_base_v001_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_5d_s00_base_v002_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_5d_s00_base_v003_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_5d_s00_base_v004_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_5d_s00_base_v005_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_5d_s00_base_v006_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_5d_s00_base_v007_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_10d_s00_base_v008_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_10d_s00_base_v009_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_10d_s00_base_v010_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_10d_s00_base_v011_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_10d_s00_base_v012_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_10d_s00_base_v013_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_10d_s00_base_v014_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_21d_s00_base_v015_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_21d_s00_base_v016_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_21d_s00_base_v017_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_21d_s00_base_v018_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_21d_s00_base_v019_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_21d_s00_base_v020_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_21d_s00_base_v021_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_42d_s00_base_v022_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_42d_s00_base_v023_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_42d_s00_base_v024_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_42d_s00_base_v025_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_42d_s00_base_v026_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_42d_s00_base_v027_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_42d_s00_base_v028_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_63d_s00_base_v029_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_63d_s00_base_v030_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_63d_s00_base_v031_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_63d_s00_base_v032_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_63d_s00_base_v033_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_63d_s00_base_v034_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_63d_s00_base_v035_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_84d_s00_base_v036_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_84d_s00_base_v037_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_84d_s00_base_v038_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_84d_s00_base_v039_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_84d_s00_base_v040_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_84d_s00_base_v041_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_84d_s00_base_v042_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_105d_s00_base_v043_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_105d_s00_base_v044_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_105d_s00_base_v045_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_105d_s00_base_v046_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_105d_s00_base_v047_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_105d_s00_base_v048_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_105d_s00_base_v049_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_126d_s00_base_v050_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_126d_s00_base_v051_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_126d_s00_base_v052_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_126d_s00_base_v053_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_126d_s00_base_v054_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_126d_s00_base_v055_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_126d_s00_base_v056_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_147d_s00_base_v057_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_147d_s00_base_v058_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_147d_s00_base_v059_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_147d_s00_base_v060_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_147d_s00_base_v061_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_147d_s00_base_v062_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_147d_s00_base_v063_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_168d_s00_base_v064_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_168d_s00_base_v065_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_168d_s00_base_v066_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_168d_s00_base_v067_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_168d_s00_base_v068_signal,
    f46quc_f46_quiet_utility_compounder_cc_ebitda_168d_s00_base_v069_signal,
    f46quc_f46_quiet_utility_compounder_cc_eps_168d_s00_base_v070_signal,
    f46quc_f46_quiet_utility_compounder_lv_close_189d_s00_base_v071_signal,
    f46quc_f46_quiet_utility_compounder_sg_netinc_189d_s00_base_v072_signal,
    f46quc_f46_quiet_utility_compounder_sg_ebitda_189d_s00_base_v073_signal,
    f46quc_f46_quiet_utility_compounder_sg_eps_189d_s00_base_v074_signal,
    f46quc_f46_quiet_utility_compounder_cc_ni_189d_s00_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_UTILITY_COMPOUNDER_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f46_quiet_utility_compounder_base_001_075_claude: {n_features} features pass")
