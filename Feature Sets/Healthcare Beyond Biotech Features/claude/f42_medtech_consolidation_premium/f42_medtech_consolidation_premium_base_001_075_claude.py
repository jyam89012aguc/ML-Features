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


# ===== folder domain primitives =====
def _f42_evebitda_dynamics(evebitda, w):
    base = _mean(evebitda, max(2, w // 4))
    return base - base.shift(w)


def _f42_premium_proxy(evebitda, ebitdamargin, w):
    margin_z = _z(ebitdamargin, w)
    return evebitda * margin_z


def _f42_consolidation_signal(ev, ebitda, revenue, w):
    ev_per_rev = ev / revenue.replace(0, np.nan)
    eb_per_rev = ebitda / revenue.replace(0, np.nan)
    return ev_per_rev.rolling(w, min_periods=max(1, w // 2)).mean() - eb_per_rev.rolling(w, min_periods=max(1, w // 2)).mean()

# v001: evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_base_v001_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_base_v002_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_base_v003_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_base_v004_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_base_v005_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_base_v006_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_base_v007_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_base_v008_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_base_v009_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_base_v010_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_base_v011_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_base_v012_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_base_v013_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_base_v014_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_base_v015_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: evdynsq_21d
def f42mcp_f42_medtech_consolidation_premium_evdynsq_21d_base_v016_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21).pow(2).pipe(lambda s: s * np.sign(_f42_evebitda_dynamics(evebitda, 21))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: evdynsq_63d
def f42mcp_f42_medtech_consolidation_premium_evdynsq_63d_base_v017_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63).pow(2).pipe(lambda s: s * np.sign(_f42_evebitda_dynamics(evebitda, 63))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: evdynsq_252d
def f42mcp_f42_medtech_consolidation_premium_evdynsq_252d_base_v018_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252).pow(2).pipe(lambda s: s * np.sign(_f42_evebitda_dynamics(evebitda, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: evdynz_21d
def f42mcp_f42_medtech_consolidation_premium_evdynz_21d_base_v019_signal(evebitda, closeadj):
    result = _z(_f42_evebitda_dynamics(evebitda, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: evdynz_63d
def f42mcp_f42_medtech_consolidation_premium_evdynz_63d_base_v020_signal(evebitda, closeadj):
    result = _z(_f42_evebitda_dynamics(evebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: evdynz_252d
def f42mcp_f42_medtech_consolidation_premium_evdynz_252d_base_v021_signal(evebitda, closeadj):
    result = _z(_f42_evebitda_dynamics(evebitda, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: premproxz_21d
def f42mcp_f42_medtech_consolidation_premium_premproxz_21d_base_v022_signal(evebitda, ebitdamargin, closeadj):
    result = _z(_f42_premium_proxy(evebitda, ebitdamargin, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: premproxz_63d
def f42mcp_f42_medtech_consolidation_premium_premproxz_63d_base_v023_signal(evebitda, ebitdamargin, closeadj):
    result = _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: premproxz_252d
def f42mcp_f42_medtech_consolidation_premium_premproxz_252d_base_v024_signal(evebitda, ebitdamargin, closeadj):
    result = _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: consolz_21d
def f42mcp_f42_medtech_consolidation_premium_consolz_21d_base_v025_signal(ev, ebitda, revenue, closeadj):
    result = _z(_f42_consolidation_signal(ev, ebitda, revenue, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: consolz_63d
def f42mcp_f42_medtech_consolidation_premium_consolz_63d_base_v026_signal(ev, ebitda, revenue, closeadj):
    result = _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: consolz_252d
def f42mcp_f42_medtech_consolidation_premium_consolz_252d_base_v027_signal(ev, ebitda, revenue, closeadj):
    result = _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: evdynmean_21d
def f42mcp_f42_medtech_consolidation_premium_evdynmean_21d_base_v028_signal(evebitda, closeadj):
    result = _mean(_f42_evebitda_dynamics(evebitda, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: evdynmean_63d
def f42mcp_f42_medtech_consolidation_premium_evdynmean_63d_base_v029_signal(evebitda, closeadj):
    result = _mean(_f42_evebitda_dynamics(evebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: evdynmean_126d
def f42mcp_f42_medtech_consolidation_premium_evdynmean_126d_base_v030_signal(evebitda, closeadj):
    result = _mean(_f42_evebitda_dynamics(evebitda, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: evdynstd_21d
def f42mcp_f42_medtech_consolidation_premium_evdynstd_21d_base_v031_signal(evebitda, closeadj):
    result = _std(_f42_evebitda_dynamics(evebitda, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: evdynstd_63d
def f42mcp_f42_medtech_consolidation_premium_evdynstd_63d_base_v032_signal(evebitda, closeadj):
    result = _std(_f42_evebitda_dynamics(evebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: evdynstd_126d
def f42mcp_f42_medtech_consolidation_premium_evdynstd_126d_base_v033_signal(evebitda, closeadj):
    result = _std(_f42_evebitda_dynamics(evebitda, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_base_v034_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_base_v035_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_base_v036_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_base_v037_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038: premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_base_v038_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_base_v039_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_base_v040_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_base_v041_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_base_v042_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_base_v043_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_base_v044_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_base_v045_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_base_v046_signal(evebitda, ev, ebitda, revenue, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_base_v047_signal(evebitda, ev, ebitda, revenue, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_base_v048_signal(evebitda, ev, ebitda, revenue, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_base_v049_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_base_v050_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_base_v051_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: evdyn_5d_x
def f42mcp_f42_medtech_consolidation_premium_evdyn_5d_x_base_v052_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v053: evdyn_10d_x
def f42mcp_f42_medtech_consolidation_premium_evdyn_10d_x_base_v053_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v054: evdyn_42d_x
def f42mcp_f42_medtech_consolidation_premium_evdyn_42d_x_base_v054_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v055: evdyn_189d_x
def f42mcp_f42_medtech_consolidation_premium_evdyn_189d_x_base_v055_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v056: evdyn_378d_x
def f42mcp_f42_medtech_consolidation_premium_evdyn_378d_x_base_v056_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v057: premprox_5d_alt
def f42mcp_f42_medtech_consolidation_premium_premprox_5d_alt_base_v057_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v058: premprox_10d_alt
def f42mcp_f42_medtech_consolidation_premium_premprox_10d_alt_base_v058_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v059: premprox_42d_alt
def f42mcp_f42_medtech_consolidation_premium_premprox_42d_alt_base_v059_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v060: premprox_189d_alt
def f42mcp_f42_medtech_consolidation_premium_premprox_189d_alt_base_v060_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v061: composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_base_v061_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    result = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v062: composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_base_v062_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    result = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v063: composite_126d
def f42mcp_f42_medtech_consolidation_premium_composite_126d_base_v063_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    result = (_z(_f42_evebitda_dynamics(evebitda, 126), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 126), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 126), 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v064: evdynxprice2_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxprice2_21d_base_v064_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: evdynxprice2_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxprice2_63d_base_v065_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: evdynxprice2_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxprice2_252d_base_v066_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: premproxxprice2_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxprice2_21d_base_v067_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: premproxxprice2_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxprice2_63d_base_v068_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: premproxxprice2_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxprice2_252d_base_v069_signal(evebitda, ebitdamargin, closeadj):
    result = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: consolxprice2_21d
def f42mcp_f42_medtech_consolidation_premium_consolxprice2_21d_base_v070_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v071: consolxprice2_63d
def f42mcp_f42_medtech_consolidation_premium_consolxprice2_63d_base_v071_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v072: consolxprice2_252d
def f42mcp_f42_medtech_consolidation_premium_consolxprice2_252d_base_v072_signal(ev, ebitda, revenue, closeadj):
    result = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v073: evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_base_v073_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v074: evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_base_v074_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v075: evdyncum_252d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_252d_base_v075_signal(evebitda, closeadj):
    result = _f42_evebitda_dynamics(evebitda, 252).rolling(504, min_periods=168).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_base_v001_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_base_v002_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_base_v003_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_base_v004_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_base_v005_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_base_v006_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_base_v007_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_base_v008_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_base_v009_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_base_v010_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_base_v011_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_base_v012_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_base_v013_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_base_v014_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_base_v015_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynsq_21d_base_v016_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynsq_63d_base_v017_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynsq_252d_base_v018_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynz_21d_base_v019_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynz_63d_base_v020_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynz_252d_base_v021_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxz_21d_base_v022_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxz_63d_base_v023_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxz_252d_base_v024_signal,
    f42mcp_f42_medtech_consolidation_premium_consolz_21d_base_v025_signal,
    f42mcp_f42_medtech_consolidation_premium_consolz_63d_base_v026_signal,
    f42mcp_f42_medtech_consolidation_premium_consolz_252d_base_v027_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynmean_21d_base_v028_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynmean_63d_base_v029_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynmean_126d_base_v030_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynstd_21d_base_v031_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynstd_63d_base_v032_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynstd_126d_base_v033_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_base_v034_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_base_v035_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_base_v036_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_base_v037_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_base_v038_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_base_v039_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_base_v040_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_base_v041_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_base_v042_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_base_v043_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_base_v044_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_base_v045_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_base_v046_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_base_v047_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_base_v048_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_base_v049_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_base_v050_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_base_v051_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_5d_x_base_v052_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_10d_x_base_v053_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_42d_x_base_v054_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_189d_x_base_v055_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_378d_x_base_v056_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_5d_alt_base_v057_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_10d_alt_base_v058_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_42d_alt_base_v059_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_189d_alt_base_v060_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_base_v061_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_base_v062_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_126d_base_v063_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxprice2_21d_base_v064_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxprice2_63d_base_v065_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxprice2_252d_base_v066_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxprice2_21d_base_v067_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxprice2_63d_base_v068_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxprice2_252d_base_v069_signal,
    f42mcp_f42_medtech_consolidation_premium_consolxprice2_21d_base_v070_signal,
    f42mcp_f42_medtech_consolidation_premium_consolxprice2_63d_base_v071_signal,
    f42mcp_f42_medtech_consolidation_premium_consolxprice2_252d_base_v072_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_base_v073_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_base_v074_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_MEDTECH_CONSOLIDATION_PREMIUM_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    ev = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    evebitda = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")

    cols = {
        "closeadj": closeadj,
        "ebitda": ebitda,
        "ebitdamargin": ebitdamargin,
        "ev": ev,
        "evebitda": evebitda,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f42_evebitda_dynamics', '_f42_premium_proxy', '_f42_consolidation_signal',)
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
    print(f"OK f42_medtech_consolidation_premium_base_001_075_claude: {n_features} features pass")
