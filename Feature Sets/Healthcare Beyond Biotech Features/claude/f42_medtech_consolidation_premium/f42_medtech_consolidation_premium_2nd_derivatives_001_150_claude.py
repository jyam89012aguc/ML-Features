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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


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

# v001: _slope_pct window 5 of evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_slope_v001_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: _slope_diff_norm window 21 of evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_slope_v002_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: _diff window 63 of evdyn_21d
def f42mcp_f42_medtech_consolidation_premium_evdyn_21d_slope_v003_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: _slope_pct window 5 of evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_slope_v004_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: _slope_diff_norm window 21 of evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_slope_v005_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: _diff window 63 of evdyn_63d
def f42mcp_f42_medtech_consolidation_premium_evdyn_63d_slope_v006_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: _slope_pct window 5 of evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_slope_v007_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: _slope_diff_norm window 21 of evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_slope_v008_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: _diff window 63 of evdyn_126d
def f42mcp_f42_medtech_consolidation_premium_evdyn_126d_slope_v009_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: _slope_pct window 5 of evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_slope_v010_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: _slope_diff_norm window 21 of evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_slope_v011_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: _diff window 63 of evdyn_252d
def f42mcp_f42_medtech_consolidation_premium_evdyn_252d_slope_v012_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: _slope_pct window 5 of evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_slope_v013_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: _slope_diff_norm window 21 of evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_slope_v014_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: _diff window 63 of evdyn_504d
def f42mcp_f42_medtech_consolidation_premium_evdyn_504d_slope_v015_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: _slope_pct window 5 of premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_slope_v016_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: _slope_diff_norm window 21 of premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_slope_v017_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: _diff window 63 of premprox_21d
def f42mcp_f42_medtech_consolidation_premium_premprox_21d_slope_v018_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: _slope_pct window 5 of premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_slope_v019_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: _slope_diff_norm window 21 of premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_slope_v020_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: _diff window 63 of premprox_63d
def f42mcp_f42_medtech_consolidation_premium_premprox_63d_slope_v021_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: _slope_pct window 5 of premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_slope_v022_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: _slope_diff_norm window 21 of premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_slope_v023_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: _diff window 63 of premprox_126d
def f42mcp_f42_medtech_consolidation_premium_premprox_126d_slope_v024_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: _slope_pct window 5 of premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_slope_v025_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: _slope_diff_norm window 21 of premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_slope_v026_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: _diff window 63 of premprox_252d
def f42mcp_f42_medtech_consolidation_premium_premprox_252d_slope_v027_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: _slope_pct window 5 of premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_slope_v028_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: _slope_diff_norm window 21 of premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_slope_v029_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: _diff window 63 of premprox_504d
def f42mcp_f42_medtech_consolidation_premium_premprox_504d_slope_v030_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: _slope_pct window 5 of consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_slope_v031_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: _slope_diff_norm window 21 of consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_slope_v032_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: _diff window 63 of consol_21d
def f42mcp_f42_medtech_consolidation_premium_consol_21d_slope_v033_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: _slope_pct window 5 of consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_slope_v034_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: _slope_diff_norm window 21 of consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_slope_v035_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: _diff window 63 of consol_63d
def f42mcp_f42_medtech_consolidation_premium_consol_63d_slope_v036_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: _slope_pct window 5 of consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_slope_v037_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: _slope_diff_norm window 21 of consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_slope_v038_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: _diff window 63 of consol_126d
def f42mcp_f42_medtech_consolidation_premium_consol_126d_slope_v039_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: _slope_pct window 5 of consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_slope_v040_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: _slope_diff_norm window 21 of consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_slope_v041_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: _diff window 63 of consol_252d
def f42mcp_f42_medtech_consolidation_premium_consol_252d_slope_v042_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: _slope_pct window 5 of consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_slope_v043_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: _slope_diff_norm window 21 of consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_slope_v044_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: _diff window 63 of consol_504d
def f42mcp_f42_medtech_consolidation_premium_consol_504d_slope_v045_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: _slope_pct window 5 of evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_slope_v046_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: _slope_diff_norm window 21 of evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_slope_v047_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: _diff window 63 of evxprem_21d
def f42mcp_f42_medtech_consolidation_premium_evxprem_21d_slope_v048_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_premium_proxy(evebitda, ebitdamargin, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: _slope_pct window 5 of evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_slope_v049_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: _slope_diff_norm window 21 of evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_slope_v050_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: _diff window 63 of evxprem_63d
def f42mcp_f42_medtech_consolidation_premium_evxprem_63d_slope_v051_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_premium_proxy(evebitda, ebitdamargin, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: _slope_pct window 5 of evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_slope_v052_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: _slope_diff_norm window 21 of evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_slope_v053_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: _diff window 63 of evxprem_252d
def f42mcp_f42_medtech_consolidation_premium_evxprem_252d_slope_v054_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_premium_proxy(evebitda, ebitdamargin, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: _slope_pct window 5 of evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_slope_v055_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: _slope_diff_norm window 21 of evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_slope_v056_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: _diff window 63 of evxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_slope_v057_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: _slope_pct window 5 of evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_slope_v058_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: _slope_diff_norm window 21 of evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_slope_v059_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: _diff window 63 of evxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_slope_v060_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: _slope_pct window 5 of evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_slope_v061_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: _slope_diff_norm window 21 of evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_slope_v062_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: _diff window 63 of evxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_slope_v063_signal(evebitda, ev, ebitda, revenue, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: _slope_pct window 5 of premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_slope_v064_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: _slope_diff_norm window 21 of premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_slope_v065_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: _diff window 63 of premxconsol_21d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_slope_v066_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _f42_consolidation_signal(ev, ebitda, revenue, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: _slope_pct window 5 of premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_slope_v067_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: _slope_diff_norm window 21 of premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_slope_v068_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: _diff window 63 of premxconsol_63d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_slope_v069_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _f42_consolidation_signal(ev, ebitda, revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: _slope_pct window 5 of premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_slope_v070_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: _slope_diff_norm window 21 of premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_slope_v071_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: _diff window 63 of premxconsol_252d
def f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_slope_v072_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _f42_consolidation_signal(ev, ebitda, revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: _slope_pct window 5 of evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_slope_v073_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: _slope_diff_norm window 21 of evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_slope_v074_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: _diff window 63 of evdynema_21d
def f42mcp_f42_medtech_consolidation_premium_evdynema_21d_slope_v075_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: _slope_pct window 5 of evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_slope_v076_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: _slope_diff_norm window 21 of evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_slope_v077_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: _diff window 63 of evdynema_63d
def f42mcp_f42_medtech_consolidation_premium_evdynema_63d_slope_v078_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: _slope_pct window 5 of evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_slope_v079_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: _slope_diff_norm window 21 of evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_slope_v080_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: _diff window 63 of evdynema_252d
def f42mcp_f42_medtech_consolidation_premium_evdynema_252d_slope_v081_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: _slope_pct window 5 of premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_slope_v082_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: _slope_diff_norm window 21 of premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_slope_v083_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: _diff window 63 of premproxema_21d
def f42mcp_f42_medtech_consolidation_premium_premproxema_21d_slope_v084_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: _slope_pct window 5 of premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_slope_v085_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: _slope_diff_norm window 21 of premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_slope_v086_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: _diff window 63 of premproxema_63d
def f42mcp_f42_medtech_consolidation_premium_premproxema_63d_slope_v087_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: _slope_pct window 5 of premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_slope_v088_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: _slope_diff_norm window 21 of premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_slope_v089_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: _diff window 63 of premproxema_252d
def f42mcp_f42_medtech_consolidation_premium_premproxema_252d_slope_v090_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: _slope_pct window 5 of consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_slope_v091_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: _slope_diff_norm window 21 of consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_slope_v092_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: _diff window 63 of consolema_21d
def f42mcp_f42_medtech_consolidation_premium_consolema_21d_slope_v093_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: _slope_pct window 5 of consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_slope_v094_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: _slope_diff_norm window 21 of consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_slope_v095_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: _diff window 63 of consolema_63d
def f42mcp_f42_medtech_consolidation_premium_consolema_63d_slope_v096_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: _slope_pct window 5 of consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_slope_v097_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: _slope_diff_norm window 21 of consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_slope_v098_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: _diff window 63 of consolema_252d
def f42mcp_f42_medtech_consolidation_premium_consolema_252d_slope_v099_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: _slope_pct window 5 of evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_slope_v100_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: _slope_diff_norm window 21 of evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_slope_v101_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: _diff window 63 of evdyncum_21d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_slope_v102_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: _slope_pct window 5 of evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_slope_v103_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: _slope_diff_norm window 21 of evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_slope_v104_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: _diff window 63 of evdyncum_63d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_slope_v105_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: _slope_pct window 5 of evdyncum_126d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_slope_v106_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: _slope_diff_norm window 21 of evdyncum_126d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_slope_v107_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: _diff window 63 of evdyncum_126d
def f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_slope_v108_signal(evebitda, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: _slope_pct window 5 of premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_slope_v109_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: _slope_diff_norm window 21 of premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_slope_v110_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: _diff window 63 of premproxcum_21d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_slope_v111_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: _slope_pct window 5 of premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_slope_v112_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: _slope_diff_norm window 21 of premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_slope_v113_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: _diff window 63 of premproxcum_63d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_slope_v114_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: _slope_pct window 5 of premproxcum_126d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_slope_v115_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: _slope_diff_norm window 21 of premproxcum_126d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_slope_v116_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: _diff window 63 of premproxcum_126d
def f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_slope_v117_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: _slope_pct window 5 of consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_slope_v118_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: _slope_diff_norm window 21 of consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_slope_v119_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: _diff window 63 of consolcum_21d
def f42mcp_f42_medtech_consolidation_premium_consolcum_21d_slope_v120_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: _slope_pct window 5 of consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_slope_v121_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: _slope_diff_norm window 21 of consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_slope_v122_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: _diff window 63 of consolcum_63d
def f42mcp_f42_medtech_consolidation_premium_consolcum_63d_slope_v123_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: _slope_pct window 5 of consolcum_126d
def f42mcp_f42_medtech_consolidation_premium_consolcum_126d_slope_v124_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: _slope_diff_norm window 21 of consolcum_126d
def f42mcp_f42_medtech_consolidation_premium_consolcum_126d_slope_v125_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: _diff window 63 of consolcum_126d
def f42mcp_f42_medtech_consolidation_premium_consolcum_126d_slope_v126_signal(ev, ebitda, revenue, closeadj):
    base = _f42_consolidation_signal(ev, ebitda, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: _slope_pct window 5 of composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_slope_v127_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: _slope_diff_norm window 21 of composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_slope_v128_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: _diff window 63 of composite_63d
def f42mcp_f42_medtech_consolidation_premium_composite_63d_slope_v129_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 63), 252) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 63), 252) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 63), 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: _slope_pct window 5 of composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_slope_v130_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: _slope_diff_norm window 21 of composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_slope_v131_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: _diff window 63 of composite_252d
def f42mcp_f42_medtech_consolidation_premium_composite_252d_slope_v132_signal(evebitda, ebitdamargin, ev, ebitda, revenue, closeadj):
    base = (_z(_f42_evebitda_dynamics(evebitda, 252), 504) + _z(_f42_premium_proxy(evebitda, ebitdamargin, 252), 504) + _z(_f42_consolidation_signal(ev, ebitda, revenue, 252), 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: _slope_pct window 5 of evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_slope_v133_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: _slope_diff_norm window 21 of evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_slope_v134_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: _diff window 63 of evdynxmargin_21d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_slope_v135_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 21) * _mean(ebitdamargin, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: _slope_pct window 5 of evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_slope_v136_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: _slope_diff_norm window 21 of evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_slope_v137_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: _diff window 63 of evdynxmargin_63d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_slope_v138_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 63) * _mean(ebitdamargin, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: _slope_pct window 5 of evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_slope_v139_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: _slope_diff_norm window 21 of evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_slope_v140_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: _diff window 63 of evdynxmargin_252d
def f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_slope_v141_signal(evebitda, ebitdamargin, closeadj):
    base = _f42_evebitda_dynamics(evebitda, 252) * _mean(ebitdamargin, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: _slope_pct window 5 of premproxxev_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_slope_v142_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _mean(ev, 21) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: _slope_diff_norm window 21 of premproxxev_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_slope_v143_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _mean(ev, 21) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: _diff window 63 of premproxxev_21d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_slope_v144_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 21) * _mean(ev, 21) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: _slope_pct window 5 of premproxxev_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_slope_v145_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _mean(ev, 63) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: _slope_diff_norm window 21 of premproxxev_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_slope_v146_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _mean(ev, 63) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: _diff window 63 of premproxxev_63d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_slope_v147_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 63) * _mean(ev, 63) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: _slope_pct window 5 of premproxxev_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_slope_v148_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _mean(ev, 252) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: _slope_diff_norm window 21 of premproxxev_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_slope_v149_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _mean(ev, 252) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: _diff window 63 of premproxxev_252d
def f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_slope_v150_signal(evebitda, ebitdamargin, ev, closeadj):
    base = _f42_premium_proxy(evebitda, ebitdamargin, 252) * _mean(ev, 252) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_slope_v001_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_slope_v002_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_21d_slope_v003_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_slope_v004_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_slope_v005_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_63d_slope_v006_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_slope_v007_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_slope_v008_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_126d_slope_v009_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_slope_v010_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_slope_v011_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_252d_slope_v012_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_slope_v013_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_slope_v014_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyn_504d_slope_v015_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_slope_v016_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_slope_v017_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_21d_slope_v018_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_slope_v019_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_slope_v020_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_63d_slope_v021_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_slope_v022_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_slope_v023_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_126d_slope_v024_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_slope_v025_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_slope_v026_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_252d_slope_v027_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_slope_v028_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_slope_v029_signal,
    f42mcp_f42_medtech_consolidation_premium_premprox_504d_slope_v030_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_slope_v031_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_slope_v032_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_21d_slope_v033_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_slope_v034_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_slope_v035_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_63d_slope_v036_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_slope_v037_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_slope_v038_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_126d_slope_v039_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_slope_v040_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_slope_v041_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_252d_slope_v042_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_slope_v043_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_slope_v044_signal,
    f42mcp_f42_medtech_consolidation_premium_consol_504d_slope_v045_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_slope_v046_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_slope_v047_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_21d_slope_v048_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_slope_v049_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_slope_v050_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_63d_slope_v051_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_slope_v052_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_slope_v053_signal,
    f42mcp_f42_medtech_consolidation_premium_evxprem_252d_slope_v054_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_slope_v055_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_slope_v056_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_21d_slope_v057_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_slope_v058_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_slope_v059_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_63d_slope_v060_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_slope_v061_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_slope_v062_signal,
    f42mcp_f42_medtech_consolidation_premium_evxconsol_252d_slope_v063_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_slope_v064_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_slope_v065_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_21d_slope_v066_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_slope_v067_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_slope_v068_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_63d_slope_v069_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_slope_v070_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_slope_v071_signal,
    f42mcp_f42_medtech_consolidation_premium_premxconsol_252d_slope_v072_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_slope_v073_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_slope_v074_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_21d_slope_v075_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_slope_v076_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_slope_v077_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_63d_slope_v078_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_slope_v079_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_slope_v080_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynema_252d_slope_v081_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_slope_v082_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_slope_v083_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_21d_slope_v084_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_slope_v085_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_slope_v086_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_63d_slope_v087_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_slope_v088_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_slope_v089_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxema_252d_slope_v090_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_slope_v091_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_slope_v092_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_21d_slope_v093_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_slope_v094_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_slope_v095_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_63d_slope_v096_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_slope_v097_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_slope_v098_signal,
    f42mcp_f42_medtech_consolidation_premium_consolema_252d_slope_v099_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_slope_v100_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_slope_v101_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_21d_slope_v102_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_slope_v103_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_slope_v104_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_63d_slope_v105_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_slope_v106_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_slope_v107_signal,
    f42mcp_f42_medtech_consolidation_premium_evdyncum_126d_slope_v108_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_slope_v109_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_slope_v110_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_21d_slope_v111_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_slope_v112_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_slope_v113_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_63d_slope_v114_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_slope_v115_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_slope_v116_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxcum_126d_slope_v117_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_slope_v118_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_slope_v119_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_21d_slope_v120_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_slope_v121_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_slope_v122_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_63d_slope_v123_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_126d_slope_v124_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_126d_slope_v125_signal,
    f42mcp_f42_medtech_consolidation_premium_consolcum_126d_slope_v126_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_slope_v127_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_slope_v128_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_63d_slope_v129_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_slope_v130_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_slope_v131_signal,
    f42mcp_f42_medtech_consolidation_premium_composite_252d_slope_v132_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_slope_v133_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_slope_v134_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_21d_slope_v135_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_slope_v136_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_slope_v137_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_63d_slope_v138_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_slope_v139_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_slope_v140_signal,
    f42mcp_f42_medtech_consolidation_premium_evdynxmargin_252d_slope_v141_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_slope_v142_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_slope_v143_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_21d_slope_v144_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_slope_v145_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_slope_v146_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_63d_slope_v147_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_slope_v148_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_slope_v149_signal,
    f42mcp_f42_medtech_consolidation_premium_premproxxev_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_MEDTECH_CONSOLIDATION_PREMIUM_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f42_medtech_consolidation_premium_2nd_derivatives_001_150_claude: {n_features} features pass")
