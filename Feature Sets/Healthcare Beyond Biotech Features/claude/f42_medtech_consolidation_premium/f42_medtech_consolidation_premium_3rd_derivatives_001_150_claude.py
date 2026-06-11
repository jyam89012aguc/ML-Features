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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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

# v001: jerk window 5 of evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_jerk_v001_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: jerk window 21 of evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_jerk_v002_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: jerk window 63 of evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_jerk_v003_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: jerk window 5 of evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_jerk_v004_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: jerk window 21 of evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_jerk_v005_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: jerk window 63 of evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_jerk_v006_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: jerk window 5 of evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_jerk_v007_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: jerk window 21 of evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_jerk_v008_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: jerk window 63 of evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_jerk_v009_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: jerk window 5 of evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_jerk_v010_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: jerk window 21 of evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_jerk_v011_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: jerk window 63 of evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_jerk_v012_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: jerk window 5 of evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_jerk_v013_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: jerk window 21 of evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_jerk_v014_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: jerk window 63 of evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_jerk_v015_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: jerk window 5 of premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_jerk_v016_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: jerk window 21 of premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_jerk_v017_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: jerk window 63 of premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_jerk_v018_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: jerk window 5 of premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_jerk_v019_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: jerk window 21 of premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_jerk_v020_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: jerk window 63 of premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_jerk_v021_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: jerk window 5 of premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_jerk_v022_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: jerk window 21 of premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_jerk_v023_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: jerk window 63 of premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_jerk_v024_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: jerk window 5 of premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_jerk_v025_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: jerk window 21 of premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_jerk_v026_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: jerk window 63 of premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_jerk_v027_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: jerk window 5 of premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_jerk_v028_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: jerk window 21 of premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_jerk_v029_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: jerk window 63 of premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_jerk_v030_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: jerk window 5 of consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_jerk_v031_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: jerk window 21 of consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_jerk_v032_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: jerk window 63 of consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_jerk_v033_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: jerk window 5 of consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_jerk_v034_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: jerk window 21 of consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_jerk_v035_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: jerk window 63 of consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_jerk_v036_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: jerk window 5 of consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_jerk_v037_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: jerk window 21 of consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_jerk_v038_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: jerk window 63 of consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_jerk_v039_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: jerk window 5 of consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_jerk_v040_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: jerk window 21 of consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_jerk_v041_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: jerk window 63 of consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_jerk_v042_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: jerk window 5 of consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_jerk_v043_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: jerk window 21 of consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_jerk_v044_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: jerk window 63 of consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_jerk_v045_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: jerk window 5 of evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_jerk_v046_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: jerk window 21 of evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_jerk_v047_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: jerk window 63 of evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_jerk_v048_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: jerk window 5 of evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_jerk_v049_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: jerk window 21 of evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_jerk_v050_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: jerk window 63 of evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_jerk_v051_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: jerk window 5 of evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_jerk_v052_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: jerk window 21 of evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_jerk_v053_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: jerk window 63 of evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_jerk_v054_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: jerk window 5 of evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_jerk_v055_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: jerk window 21 of evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_jerk_v056_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: jerk window 63 of evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_jerk_v057_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: jerk window 5 of evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_jerk_v058_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: jerk window 21 of evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_jerk_v059_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: jerk window 63 of evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_jerk_v060_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: jerk window 5 of evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_jerk_v061_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: jerk window 21 of evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_jerk_v062_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: jerk window 63 of evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_jerk_v063_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: jerk window 5 of premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_jerk_v064_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: jerk window 21 of premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_jerk_v065_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: jerk window 63 of premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_jerk_v066_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: jerk window 5 of premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_jerk_v067_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: jerk window 21 of premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_jerk_v068_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: jerk window 63 of premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_jerk_v069_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: jerk window 5 of premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_jerk_v070_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: jerk window 21 of premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_jerk_v071_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: jerk window 63 of premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_jerk_v072_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: jerk window 5 of evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_jerk_v073_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: jerk window 21 of evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_jerk_v074_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: jerk window 63 of evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_jerk_v075_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: jerk window 5 of evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_jerk_v076_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: jerk window 21 of evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_jerk_v077_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: jerk window 63 of evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_jerk_v078_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: jerk window 5 of evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_jerk_v079_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: jerk window 21 of evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_jerk_v080_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: jerk window 63 of evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_jerk_v081_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: jerk window 5 of premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_jerk_v082_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: jerk window 21 of premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_jerk_v083_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: jerk window 63 of premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_jerk_v084_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: jerk window 5 of premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_jerk_v085_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: jerk window 21 of premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_jerk_v086_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: jerk window 63 of premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_jerk_v087_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: jerk window 5 of premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_jerk_v088_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: jerk window 21 of premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_jerk_v089_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: jerk window 63 of premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_jerk_v090_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: jerk window 5 of consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_jerk_v091_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: jerk window 21 of consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_jerk_v092_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: jerk window 63 of consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_jerk_v093_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: jerk window 5 of consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_jerk_v094_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: jerk window 21 of consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_jerk_v095_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: jerk window 63 of consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_jerk_v096_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: jerk window 5 of consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_jerk_v097_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: jerk window 21 of consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_jerk_v098_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: jerk window 63 of consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_jerk_v099_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: jerk window 5 of evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_jerk_v100_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: jerk window 21 of evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_jerk_v101_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: jerk window 63 of evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_jerk_v102_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: jerk window 5 of evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_jerk_v103_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: jerk window 21 of evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_jerk_v104_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: jerk window 63 of evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_jerk_v105_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: jerk window 5 of evdyncum_126d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_jerk_v106_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: jerk window 21 of evdyncum_126d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_jerk_v107_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: jerk window 63 of evdyncum_126d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_jerk_v108_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: jerk window 5 of premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_jerk_v109_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: jerk window 21 of premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_jerk_v110_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: jerk window 63 of premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_jerk_v111_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: jerk window 5 of premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_jerk_v112_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: jerk window 21 of premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_jerk_v113_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: jerk window 63 of premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_jerk_v114_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: jerk window 5 of premproxcum_126d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_jerk_v115_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: jerk window 21 of premproxcum_126d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_jerk_v116_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: jerk window 63 of premproxcum_126d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_jerk_v117_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: jerk window 5 of consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_jerk_v118_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: jerk window 21 of consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_jerk_v119_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: jerk window 63 of consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_jerk_v120_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: jerk window 5 of consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_jerk_v121_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: jerk window 21 of consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_jerk_v122_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: jerk window 63 of consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_jerk_v123_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: jerk window 5 of consolcum_126d
def f42mcp_f42_medtech_consolidation_premium_consolcum_126d_jerk_v124_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: jerk window 21 of consolcum_126d
def f42mcp_f42_medtech_consolidation_premium_consolcum_126d_jerk_v125_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: jerk window 63 of consolcum_126d
def f42mcp_f42_medtech_consolidation_premium_consolcum_126d_jerk_v126_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: jerk window 5 of composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_jerk_v127_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: jerk window 21 of composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_jerk_v128_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: jerk window 63 of composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_jerk_v129_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: jerk window 5 of composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_jerk_v130_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: jerk window 21 of composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_jerk_v131_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: jerk window 63 of composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_jerk_v132_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: jerk window 5 of evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_jerk_v133_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: jerk window 21 of evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_jerk_v134_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: jerk window 63 of evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_jerk_v135_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: jerk window 5 of evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_jerk_v136_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: jerk window 21 of evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_jerk_v137_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: jerk window 63 of evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_jerk_v138_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: jerk window 5 of evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_jerk_v139_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: jerk window 21 of evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_jerk_v140_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: jerk window 63 of evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_jerk_v141_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: jerk window 5 of premproxxev_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_jerk_v142_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _mean(ev, 21) * closeadj / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: jerk window 21 of premproxxev_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_jerk_v143_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _mean(ev, 21) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: jerk window 63 of premproxxev_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_jerk_v144_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _mean(ev, 21) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: jerk window 5 of premproxxev_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_jerk_v145_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _mean(ev, 63) * closeadj / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: jerk window 21 of premproxxev_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_jerk_v146_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _mean(ev, 63) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: jerk window 63 of premproxxev_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_jerk_v147_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _mean(ev, 63) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: jerk window 5 of premproxxev_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_jerk_v148_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _mean(ev, 252) * closeadj / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: jerk window 21 of premproxxev_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_jerk_v149_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _mean(ev, 252) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: jerk window 63 of premproxxev_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_jerk_v150_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _mean(ev, 252) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_jerk_v001_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_jerk_v002_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_jerk_v003_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_jerk_v004_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_jerk_v005_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_jerk_v006_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_jerk_v007_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_jerk_v008_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_jerk_v009_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_jerk_v010_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_jerk_v011_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_jerk_v012_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_jerk_v013_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_jerk_v014_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_jerk_v015_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_jerk_v016_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_jerk_v017_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_jerk_v018_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_jerk_v019_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_jerk_v020_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_jerk_v021_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_jerk_v022_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_jerk_v023_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_jerk_v024_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_jerk_v025_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_jerk_v026_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_jerk_v027_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_jerk_v028_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_jerk_v029_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_jerk_v030_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_jerk_v031_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_jerk_v032_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_jerk_v033_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_jerk_v034_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_jerk_v035_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_jerk_v036_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_jerk_v037_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_jerk_v038_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_jerk_v039_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_jerk_v040_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_jerk_v041_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_jerk_v042_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_jerk_v043_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_jerk_v044_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_jerk_v045_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_jerk_v046_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_jerk_v047_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_jerk_v048_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_jerk_v049_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_jerk_v050_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_jerk_v051_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_jerk_v052_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_jerk_v053_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_jerk_v054_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_jerk_v055_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_jerk_v056_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_jerk_v057_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_jerk_v058_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_jerk_v059_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_jerk_v060_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_jerk_v061_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_jerk_v062_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_jerk_v063_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_jerk_v064_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_jerk_v065_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_jerk_v066_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_jerk_v067_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_jerk_v068_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_jerk_v069_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_jerk_v070_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_jerk_v071_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_jerk_v072_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_jerk_v073_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_jerk_v074_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_jerk_v075_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_jerk_v076_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_jerk_v077_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_jerk_v078_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_jerk_v079_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_jerk_v080_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_jerk_v081_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_jerk_v082_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_jerk_v083_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_jerk_v084_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_jerk_v085_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_jerk_v086_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_jerk_v087_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_jerk_v088_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_jerk_v089_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_jerk_v090_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_jerk_v091_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_jerk_v092_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_jerk_v093_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_jerk_v094_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_jerk_v095_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_jerk_v096_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_jerk_v097_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_jerk_v098_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_jerk_v099_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_jerk_v100_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_jerk_v101_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_jerk_v102_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_jerk_v103_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_jerk_v104_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_jerk_v105_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_jerk_v106_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_jerk_v107_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_jerk_v108_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_jerk_v109_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_jerk_v110_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_jerk_v111_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_jerk_v112_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_jerk_v113_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_jerk_v114_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_jerk_v115_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_jerk_v116_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_jerk_v117_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_jerk_v118_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_jerk_v119_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_jerk_v120_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_jerk_v121_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_jerk_v122_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_jerk_v123_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_126d_jerk_v124_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_126d_jerk_v125_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_126d_jerk_v126_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_jerk_v127_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_jerk_v128_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_jerk_v129_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_jerk_v130_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_jerk_v131_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_jerk_v132_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_jerk_v133_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_jerk_v134_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_jerk_v135_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_jerk_v136_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_jerk_v137_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_jerk_v138_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_jerk_v139_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_jerk_v140_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_jerk_v141_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_jerk_v142_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_jerk_v143_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_jerk_v144_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_jerk_v145_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_jerk_v146_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_jerk_v147_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_jerk_v148_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_jerk_v149_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_MEDTECH_CONSOLIDATION_PREMIUM_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f42_medtech_consolidation_premium_3rd_derivatives_001_150_claude: {n_features} features pass")
