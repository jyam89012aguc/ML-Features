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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff(s, w):
    return s.diff(periods=w) / (s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


def _jerk_diff(s, w):
    return _slope_diff(s, w).diff(periods=w)


# ===== folder domain primitives =====
def _f45_network_growth_compound(marketcap, w):
    return _diff(np.log(marketcap.replace(0, np.nan)), w) / float(w)


def _f45_network_growth_superlinear(marketcap, revenue, w):
    mg = _diff(np.log(marketcap.replace(0, np.nan)), w)
    rg = _diff(np.log(revenue.replace(0, np.nan)), w)
    return mg - rg


def _f45_network_growth_acceleration(marketcap, w):
    g = _diff(np.log(marketcap.replace(0, np.nan)), w)
    return _diff(g, w)


# 5d jerk of 21d compound × marketcap
def f45nge_f45_network_growth_engine_compound_21d_jerk_v001_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d compound × marketcap
def f45nge_f45_network_growth_engine_compound_21d_jerk_v002_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 21) * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d compound × marketcap
def f45nge_f45_network_growth_engine_compound_63d_jerk_v003_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 63) * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d compound × marketcap
def f45nge_f45_network_growth_engine_compound_63d_jerk_v004_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 63) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d compound × marketcap
def f45nge_f45_network_growth_engine_compound_126d_jerk_v005_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 126) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d compound × marketcap
def f45nge_f45_network_growth_engine_compound_126d_jerk_v006_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 126) * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d compound × marketcap
def f45nge_f45_network_growth_engine_compound_252d_jerk_v007_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d compound × marketcap
def f45nge_f45_network_growth_engine_compound_252d_jerk_v008_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 252) * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d compound × marketcap
def f45nge_f45_network_growth_engine_compound_504d_jerk_v009_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 504) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d compound × marketcap
def f45nge_f45_network_growth_engine_compound_504d_jerk_v010_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d superlinear × marketcap
def f45nge_f45_network_growth_engine_superlin_21d_jerk_v011_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d superlinear × marketcap
def f45nge_f45_network_growth_engine_superlin_63d_jerk_v012_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 63) * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d superlinear × marketcap
def f45nge_f45_network_growth_engine_superlin_252d_jerk_v013_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d superlinear × marketcap
def f45nge_f45_network_growth_engine_superlin_504d_jerk_v014_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d acceleration × ev
def f45nge_f45_network_growth_engine_accel_21d_jerk_v015_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 21) * ev
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d acceleration × ev
def f45nge_f45_network_growth_engine_accel_63d_jerk_v016_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 63) * ev
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d acceleration × ev
def f45nge_f45_network_growth_engine_accel_252d_jerk_v017_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 252) * ev
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d acceleration × ev
def f45nge_f45_network_growth_engine_accel_504d_jerk_v018_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 504) * ev
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ev compound × marketcap
def f45nge_f45_network_growth_engine_evcomp_21d_jerk_v019_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ev compound × marketcap
def f45nge_f45_network_growth_engine_evcomp_63d_jerk_v020_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 63) * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ev compound × marketcap
def f45nge_f45_network_growth_engine_evcomp_252d_jerk_v021_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d ev compound × marketcap
def f45nge_f45_network_growth_engine_evcomp_504d_jerk_v022_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d sf3a value compound × marketcap
def f45nge_f45_network_growth_engine_sf3acomp_21d_jerk_v023_signal(sf3a_value, marketcap):
    base = _f45_network_growth_compound(sf3a_value, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sf3a value compound × marketcap
def f45nge_f45_network_growth_engine_sf3acomp_252d_jerk_v024_signal(sf3a_value, marketcap):
    base = _f45_network_growth_compound(sf3a_value, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sf3b value compound × marketcap
def f45nge_f45_network_growth_engine_sf3bcomp_252d_jerk_v025_signal(sf3b_value, marketcap):
    base = _f45_network_growth_compound(sf3b_value, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d sf3b value compound × marketcap
def f45nge_f45_network_growth_engine_sf3bcomp_504d_jerk_v026_signal(sf3b_value, marketcap):
    base = _f45_network_growth_compound(sf3b_value, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ev superlinear × marketcap
def f45nge_f45_network_growth_engine_evsuperlin_21d_jerk_v027_signal(ev, revenue, marketcap):
    base = _f45_network_growth_superlinear(ev, revenue, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ev superlinear × marketcap
def f45nge_f45_network_growth_engine_evsuperlin_252d_jerk_v028_signal(ev, revenue, marketcap):
    base = _f45_network_growth_superlinear(ev, revenue, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d ev superlinear × marketcap
def f45nge_f45_network_growth_engine_evsuperlin_504d_jerk_v029_signal(ev, revenue, marketcap):
    base = _f45_network_growth_superlinear(ev, revenue, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d marketcap superlinear vs ebitda × marketcap
def f45nge_f45_network_growth_engine_mcvseb_21d_jerk_v030_signal(marketcap, ebitda):
    base = _f45_network_growth_superlinear(marketcap, ebitda, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d mcvseb × marketcap
def f45nge_f45_network_growth_engine_mcvseb_252d_jerk_v031_signal(marketcap, ebitda):
    base = _f45_network_growth_superlinear(marketcap, ebitda, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d mcvseb × marketcap
def f45nge_f45_network_growth_engine_mcvseb_504d_jerk_v032_signal(marketcap, ebitda):
    base = _f45_network_growth_superlinear(marketcap, ebitda, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d mcvsni × ev
def f45nge_f45_network_growth_engine_mcvsni_21d_jerk_v033_signal(marketcap, netinc, ev):
    base = _f45_network_growth_superlinear(marketcap, netinc, 21) * ev
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d mcvsni × ev
def f45nge_f45_network_growth_engine_mcvsni_252d_jerk_v034_signal(marketcap, netinc, ev):
    base = _f45_network_growth_superlinear(marketcap, netinc, 252) * ev
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d mcvsni × ev
def f45nge_f45_network_growth_engine_mcvsni_504d_jerk_v035_signal(marketcap, netinc, ev):
    base = _f45_network_growth_superlinear(marketcap, netinc, 504) * ev
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d mcvsfcf × ev
def f45nge_f45_network_growth_engine_mcvsfcf_21d_jerk_v036_signal(marketcap, fcf, ev):
    base = _f45_network_growth_superlinear(marketcap, fcf, 21) * ev
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d mcvsfcf × ev
def f45nge_f45_network_growth_engine_mcvsfcf_252d_jerk_v037_signal(marketcap, fcf, ev):
    base = _f45_network_growth_superlinear(marketcap, fcf, 252) * ev
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d mcvsfcf × ev
def f45nge_f45_network_growth_engine_mcvsfcf_504d_jerk_v038_signal(marketcap, fcf, ev):
    base = _f45_network_growth_superlinear(marketcap, fcf, 504) * ev
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d sf3a shares compound × marketcap
def f45nge_f45_network_growth_engine_sf3ashcomp_21d_jerk_v039_signal(sf3a_shares, marketcap):
    base = _f45_network_growth_compound(sf3a_shares, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sf3a shares compound × marketcap
def f45nge_f45_network_growth_engine_sf3ashcomp_252d_jerk_v040_signal(sf3a_shares, marketcap):
    base = _f45_network_growth_compound(sf3a_shares, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sf3b shares compound × marketcap
def f45nge_f45_network_growth_engine_sf3bshcomp_252d_jerk_v041_signal(sf3b_shares, marketcap):
    base = _f45_network_growth_compound(sf3b_shares, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d sf3b shares compound × marketcap
def f45nge_f45_network_growth_engine_sf3bshcomp_504d_jerk_v042_signal(sf3b_shares, marketcap):
    base = _f45_network_growth_compound(sf3b_shares, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d compound × ev
def f45nge_f45_network_growth_engine_compxev_21d_jerk_v043_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 21) * ev
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d compound × ev
def f45nge_f45_network_growth_engine_compxev_63d_jerk_v044_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 63) * ev
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d compound × ev
def f45nge_f45_network_growth_engine_compxev_252d_jerk_v045_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * ev
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d compound × ev
def f45nge_f45_network_growth_engine_compxev_504d_jerk_v046_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 504) * ev
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d superlinear squared × marketcap
def f45nge_f45_network_growth_engine_supsq_21d_jerk_v047_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 21)
    base = s * s.abs() * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d superlinear squared × marketcap
def f45nge_f45_network_growth_engine_supsq_63d_jerk_v048_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 63)
    base = s * s.abs() * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d superlinear squared × marketcap
def f45nge_f45_network_growth_engine_supsq_252d_jerk_v049_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 252)
    base = s * s.abs() * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of 504d superlinear squared × marketcap
def f45nge_f45_network_growth_engine_supsq_504d_jerk_v050_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 504)
    base = s * s.abs() * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of compound × log mc 21d
def f45nge_f45_network_growth_engine_compxlogmc_21d_jerk_v051_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 21) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compound × log mc 252d
def f45nge_f45_network_growth_engine_compxlogmc_252d_jerk_v052_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compound × log mc 504d
def f45nge_f45_network_growth_engine_compxlogmc_504d_jerk_v053_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 504) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of supxpe 21d
def f45nge_f45_network_growth_engine_supxpe_21d_jerk_v054_signal(marketcap, revenue, pe):
    base = _f45_network_growth_superlinear(marketcap, revenue, 21) * pe * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxpe 252d
def f45nge_f45_network_growth_engine_supxpe_252d_jerk_v055_signal(marketcap, revenue, pe):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * pe * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supxpe 504d
def f45nge_f45_network_growth_engine_supxpe_504d_jerk_v056_signal(marketcap, revenue, pe):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * pe * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of supxevebit 21d
def f45nge_f45_network_growth_engine_supxevebit_21d_jerk_v057_signal(marketcap, revenue, evebit):
    base = _f45_network_growth_superlinear(marketcap, revenue, 21) * evebit * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxevebit 252d
def f45nge_f45_network_growth_engine_supxevebit_252d_jerk_v058_signal(marketcap, revenue, evebit):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * evebit * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxevebitda 252d
def f45nge_f45_network_growth_engine_supxevebitda_252d_jerk_v059_signal(marketcap, revenue, evebitda):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * evebitda * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxpb 252d
def f45nge_f45_network_growth_engine_supxpb_252d_jerk_v060_signal(marketcap, revenue, pb):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * pb * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxps 252d
def f45nge_f45_network_growth_engine_supxps_252d_jerk_v061_signal(marketcap, revenue, ps):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * ps * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of compxrev 21d
def f45nge_f45_network_growth_engine_compxrev_21d_jerk_v062_signal(marketcap, revenue):
    base = _f45_network_growth_compound(marketcap, 21) * revenue
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxrev 252d
def f45nge_f45_network_growth_engine_compxrev_252d_jerk_v063_signal(marketcap, revenue):
    base = _f45_network_growth_compound(marketcap, 252) * revenue
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxrev 504d
def f45nge_f45_network_growth_engine_compxrev_504d_jerk_v064_signal(marketcap, revenue):
    base = _f45_network_growth_compound(marketcap, 504) * revenue
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxeb 252d
def f45nge_f45_network_growth_engine_compxeb_252d_jerk_v065_signal(marketcap, ebitda):
    base = _f45_network_growth_compound(marketcap, 252) * ebitda
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxeb 504d
def f45nge_f45_network_growth_engine_compxeb_504d_jerk_v066_signal(marketcap, ebitda):
    base = _f45_network_growth_compound(marketcap, 504) * ebitda
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxni 252d
def f45nge_f45_network_growth_engine_compxni_252d_jerk_v067_signal(marketcap, netinc):
    base = _f45_network_growth_compound(marketcap, 252) * netinc
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxfcf 504d
def f45nge_f45_network_growth_engine_compxfcf_504d_jerk_v068_signal(marketcap, fcf):
    base = _f45_network_growth_compound(marketcap, 504) * fcf
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of compEWM 63d
def f45nge_f45_network_growth_engine_compewm_63d_jerk_v069_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _jerk_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compEWM 252d
def f45nge_f45_network_growth_engine_compewm_252d_jerk_v070_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 252).ewm(span=126, adjust=False).mean() * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compEWM 504d
def f45nge_f45_network_growth_engine_compewm_504d_jerk_v071_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 504).ewm(span=252, adjust=False).mean() * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supEWM 252d
def f45nge_f45_network_growth_engine_supewm_252d_jerk_v072_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252).ewm(span=126, adjust=False).mean() * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supEWM 504d
def f45nge_f45_network_growth_engine_supewm_504d_jerk_v073_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504).ewm(span=252, adjust=False).mean() * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxsf3a 252d
def f45nge_f45_network_growth_engine_compxsf3a_252d_jerk_v074_signal(marketcap, sf3a_value):
    base = _f45_network_growth_compound(marketcap, 252) * _mean(sf3a_value, 252)
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxsf3b 504d
def f45nge_f45_network_growth_engine_compxsf3b_504d_jerk_v075_signal(marketcap, sf3b_value):
    base = _f45_network_growth_compound(marketcap, 504) * _mean(sf3b_value, 504)
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of compxpe 21d
def f45nge_f45_network_growth_engine_compxpe_21d_jerk_v076_signal(marketcap, pe):
    base = _f45_network_growth_compound(marketcap, 21) * pe * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxpe 252d
def f45nge_f45_network_growth_engine_compxpe_252d_jerk_v077_signal(marketcap, pe):
    base = _f45_network_growth_compound(marketcap, 252) * pe * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxevebit 252d
def f45nge_f45_network_growth_engine_compxevebit_252d_jerk_v078_signal(marketcap, evebit):
    base = _f45_network_growth_compound(marketcap, 252) * evebit * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxevebitda 252d
def f45nge_f45_network_growth_engine_compxevebitda_252d_jerk_v079_signal(marketcap, evebitda):
    base = _f45_network_growth_compound(marketcap, 252) * evebitda * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxpb 252d
def f45nge_f45_network_growth_engine_compxpb_252d_jerk_v080_signal(marketcap, pb):
    base = _f45_network_growth_compound(marketcap, 252) * pb * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxps 252d
def f45nge_f45_network_growth_engine_compxps_252d_jerk_v081_signal(marketcap, ps):
    base = _f45_network_growth_compound(marketcap, 252) * ps * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of accxmc 21d
def f45nge_f45_network_growth_engine_accxmc_21d_jerk_v082_signal(marketcap):
    base = _f45_network_growth_acceleration(marketcap, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accxmc 252d
def f45nge_f45_network_growth_engine_accxmc_252d_jerk_v083_signal(marketcap):
    base = _f45_network_growth_acceleration(marketcap, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accxmc 504d
def f45nge_f45_network_growth_engine_accxmc_504d_jerk_v084_signal(marketcap):
    base = _f45_network_growth_acceleration(marketcap, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of evaccxmc 21d
def f45nge_f45_network_growth_engine_evaccxmc_21d_jerk_v085_signal(ev, marketcap):
    base = _f45_network_growth_acceleration(ev, 21) * marketcap
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of evaccxmc 252d
def f45nge_f45_network_growth_engine_evaccxmc_252d_jerk_v086_signal(ev, marketcap):
    base = _f45_network_growth_acceleration(ev, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of evaccxmc 504d
def f45nge_f45_network_growth_engine_evaccxmc_504d_jerk_v087_signal(ev, marketcap):
    base = _f45_network_growth_acceleration(ev, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of sf3a accxmc 252d
def f45nge_f45_network_growth_engine_sf3aaccxmc_252d_jerk_v088_signal(sf3a_value, marketcap):
    base = _f45_network_growth_acceleration(sf3a_value, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of sf3b accxmc 504d
def f45nge_f45_network_growth_engine_sf3baccxmc_504d_jerk_v089_signal(sf3b_value, marketcap):
    base = _f45_network_growth_acceleration(sf3b_value, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of compxdebt 21d
def f45nge_f45_network_growth_engine_compxdebt_21d_jerk_v090_signal(marketcap, debt):
    base = _f45_network_growth_compound(marketcap, 21) * debt
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxdebt 252d
def f45nge_f45_network_growth_engine_compxdebt_252d_jerk_v091_signal(marketcap, debt):
    base = _f45_network_growth_compound(marketcap, 252) * debt
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxdebt 504d
def f45nge_f45_network_growth_engine_compxdebt_504d_jerk_v092_signal(marketcap, debt):
    base = _f45_network_growth_compound(marketcap, 504) * debt
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of compxeq 21d
def f45nge_f45_network_growth_engine_compxeq_21d_jerk_v093_signal(marketcap, equity):
    base = _f45_network_growth_compound(marketcap, 21) * equity
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxeq 252d
def f45nge_f45_network_growth_engine_compxeq_252d_jerk_v094_signal(marketcap, equity):
    base = _f45_network_growth_compound(marketcap, 252) * equity
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxeq 504d
def f45nge_f45_network_growth_engine_compxeq_504d_jerk_v095_signal(marketcap, equity):
    base = _f45_network_growth_compound(marketcap, 504) * equity
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxat 252d
def f45nge_f45_network_growth_engine_compxat_252d_jerk_v096_signal(marketcap, assets):
    base = _f45_network_growth_compound(marketcap, 252) * assets
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxat 504d
def f45nge_f45_network_growth_engine_compxat_504d_jerk_v097_signal(marketcap, assets):
    base = _f45_network_growth_compound(marketcap, 504) * assets
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxdebt 252d
def f45nge_f45_network_growth_engine_supxdebt_252d_jerk_v098_signal(marketcap, revenue, debt):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * debt
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxeq 252d
def f45nge_f45_network_growth_engine_supxeq_252d_jerk_v099_signal(marketcap, revenue, equity):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * equity
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxat 252d
def f45nge_f45_network_growth_engine_supxat_252d_jerk_v100_signal(marketcap, revenue, assets):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * assets
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of compxncfo 21d
def f45nge_f45_network_growth_engine_compxncfo_21d_jerk_v101_signal(marketcap, ncfo):
    base = _f45_network_growth_compound(marketcap, 21) * ncfo
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxncfo 252d
def f45nge_f45_network_growth_engine_compxncfo_252d_jerk_v102_signal(marketcap, ncfo):
    base = _f45_network_growth_compound(marketcap, 252) * ncfo
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxncfo 504d
def f45nge_f45_network_growth_engine_compxncfo_504d_jerk_v103_signal(marketcap, ncfo):
    base = _f45_network_growth_compound(marketcap, 504) * ncfo
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of evcompxev 21d
def f45nge_f45_network_growth_engine_evcompxev_21d_jerk_v104_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 21) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of evcompxev 252d
def f45nge_f45_network_growth_engine_evcompxev_252d_jerk_v105_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 252) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of evcompxev 504d
def f45nge_f45_network_growth_engine_evcompxev_504d_jerk_v106_signal(ev, marketcap):
    base = _f45_network_growth_compound(ev, 504) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxmcxrev 252d
def f45nge_f45_network_growth_engine_compxmcxrev_252d_jerk_v107_signal(marketcap, revenue):
    base = _f45_network_growth_compound(marketcap, 252) * marketcap * revenue / marketcap.replace(0, np.nan)
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supxmcxrev 504d
def f45nge_f45_network_growth_engine_supxmcxrev_504d_jerk_v108_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap * revenue / marketcap.replace(0, np.nan)
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accxev 252d
def f45nge_f45_network_growth_engine_accxev_252d_jerk_v109_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 252) * ev * marketcap / marketcap.replace(0, np.nan)
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accxev 504d
def f45nge_f45_network_growth_engine_accxev_504d_jerk_v110_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 504) * ev * marketcap / marketcap.replace(0, np.nan)
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxsf3ash 252d
def f45nge_f45_network_growth_engine_compxsf3ash_252d_jerk_v111_signal(marketcap, sf3a_shares):
    base = _f45_network_growth_compound(marketcap, 252) * _mean(sf3a_shares, 252)
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxsf3bsh 504d
def f45nge_f45_network_growth_engine_compxsf3bsh_504d_jerk_v112_signal(marketcap, sf3b_shares):
    base = _f45_network_growth_compound(marketcap, 504) * _mean(sf3b_shares, 504)
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxevxrev 252d
def f45nge_f45_network_growth_engine_compxevxrev_252d_jerk_v113_signal(marketcap, ev, revenue):
    base = _f45_network_growth_compound(marketcap, 252) * ev * revenue / 1e9
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supxevxrev 504d
def f45nge_f45_network_growth_engine_supxevxrev_504d_jerk_v114_signal(marketcap, revenue, ev):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * ev * revenue / 1e9
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of triplecomp 21d
def f45nge_f45_network_growth_engine_triplecomp_21d_jerk_v115_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 21) * marketcap * ev / 1e9
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of triplecomp 252d
def f45nge_f45_network_growth_engine_triplecomp_252d_jerk_v116_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * marketcap * ev / 1e9
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of triplecomp 504d
def f45nge_f45_network_growth_engine_triplecomp_504d_jerk_v117_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 504) * marketcap * ev / 1e9
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of complogev 252d
def f45nge_f45_network_growth_engine_complogev_252d_jerk_v118_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * ev
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of complogev 504d
def f45nge_f45_network_growth_engine_complogev_504d_jerk_v119_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 504) * np.log(marketcap.replace(0, np.nan)) * ev
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of supvsncfo 21d
def f45nge_f45_network_growth_engine_supvsncfo_21d_jerk_v120_signal(marketcap, ncfo, ev):
    base = _f45_network_growth_superlinear(marketcap, ncfo, 21) * ev
    result = _jerk_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supvsncfo 252d
def f45nge_f45_network_growth_engine_supvsncfo_252d_jerk_v121_signal(marketcap, ncfo, ev):
    base = _f45_network_growth_superlinear(marketcap, ncfo, 252) * ev
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supvsncfo 504d
def f45nge_f45_network_growth_engine_supvsncfo_504d_jerk_v122_signal(marketcap, ncfo, ev):
    base = _f45_network_growth_superlinear(marketcap, ncfo, 504) * ev
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxevebit 504d
def f45nge_f45_network_growth_engine_compxevebit_504d_jerk_v123_signal(marketcap, evebit):
    base = _f45_network_growth_compound(marketcap, 504) * evebit * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxevebitda 504d
def f45nge_f45_network_growth_engine_compxevebitda_504d_jerk_v124_signal(marketcap, evebitda):
    base = _f45_network_growth_compound(marketcap, 504) * evebitda * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxpb 504d
def f45nge_f45_network_growth_engine_compxpb_504d_jerk_v125_signal(marketcap, pb):
    base = _f45_network_growth_compound(marketcap, 504) * pb * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxps 504d
def f45nge_f45_network_growth_engine_compxps_504d_jerk_v126_signal(marketcap, ps):
    base = _f45_network_growth_compound(marketcap, 504) * ps * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxrevxmc 252d
def f45nge_f45_network_growth_engine_compxrevxmc_252d_jerk_v127_signal(marketcap, revenue):
    base = _f45_network_growth_compound(marketcap, 252) * revenue * marketcap / 1e9
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxebxmc 504d
def f45nge_f45_network_growth_engine_compxebxmc_504d_jerk_v128_signal(marketcap, ebitda):
    base = _f45_network_growth_compound(marketcap, 504) * ebitda * marketcap / 1e9
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxmcxev 252d
def f45nge_f45_network_growth_engine_supxmcxev_252d_jerk_v129_signal(marketcap, revenue, ev):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * marketcap * ev / 1e9
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supxmcxev 504d
def f45nge_f45_network_growth_engine_supxmcxev_504d_jerk_v130_signal(marketcap, revenue, ev):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap * ev / 1e9
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of complogevxmc 252d
def f45nge_f45_network_growth_engine_complogevxmc_252d_jerk_v131_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * np.log(ev.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of complogevxmc 504d
def f45nge_f45_network_growth_engine_complogevxmc_504d_jerk_v132_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 504) * np.log(ev.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxsqrt 252d
def f45nge_f45_network_growth_engine_compxsqrt_252d_jerk_v133_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * np.sqrt(marketcap.abs() * ev.abs())
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supxsqrt 504d
def f45nge_f45_network_growth_engine_supxsqrt_504d_jerk_v134_signal(marketcap, revenue, ev):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * np.sqrt(marketcap.abs() * ev.abs())
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compz 252d
def f45nge_f45_network_growth_engine_compz_252d_jerk_v135_signal(marketcap):
    base = _z(_f45_network_growth_compound(marketcap, 252), 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compz 504d
def f45nge_f45_network_growth_engine_compz_504d_jerk_v136_signal(marketcap):
    base = _z(_f45_network_growth_compound(marketcap, 504), 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supz 252d
def f45nge_f45_network_growth_engine_supz_252d_jerk_v137_signal(marketcap, revenue):
    base = _z(_f45_network_growth_superlinear(marketcap, revenue, 252), 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accz 252d
def f45nge_f45_network_growth_engine_accz_504d_jerk_v138_signal(marketcap):
    base = _z(_f45_network_growth_acceleration(marketcap, 252), 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxsf3aval 252d
def f45nge_f45_network_growth_engine_compxsf3aval_252d_jerk_v139_signal(marketcap, sf3a_value):
    base = _f45_network_growth_compound(marketcap, 252) * sf3a_value
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxevz 252d
def f45nge_f45_network_growth_engine_compxevz_252d_jerk_v140_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * _z(ev, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxevz 504d
def f45nge_f45_network_growth_engine_compxevz_504d_jerk_v141_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 504) * _z(ev, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxmcz 252d
def f45nge_f45_network_growth_engine_compxmcz_252d_jerk_v142_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 252) * _z(marketcap, 252) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxmcz 504d
def f45nge_f45_network_growth_engine_compxmcz_504d_jerk_v143_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 504) * _z(marketcap, 504) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of accxlogmc 252d
def f45nge_f45_network_growth_engine_accxlogmc_252d_jerk_v144_signal(marketcap):
    base = _f45_network_growth_acceleration(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of accxlogev 504d
def f45nge_f45_network_growth_engine_accxlogev_504d_jerk_v145_signal(marketcap, ev):
    base = _f45_network_growth_acceleration(marketcap, 504) * np.log(ev.replace(0, np.nan)) * marketcap
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of compxevstd 252d
def f45nge_f45_network_growth_engine_compxevstd_252d_jerk_v146_signal(marketcap, ev):
    base = _f45_network_growth_compound(marketcap, 252) * _std(ev, 252) * marketcap / ev.replace(0, np.nan).abs()
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of compxmcstd 504d
def f45nge_f45_network_growth_engine_compxmcstd_504d_jerk_v147_signal(marketcap):
    base = _f45_network_growth_compound(marketcap, 504) * _std(marketcap, 504)
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of supxmcsq 252d
def f45nge_f45_network_growth_engine_supxmcsq_252d_jerk_v148_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 252) * marketcap * marketcap.abs() / 1e9
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d jerk of supxmcsq 504d
def f45nge_f45_network_growth_engine_supxmcsq_504d_jerk_v149_signal(marketcap, revenue):
    base = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap * marketcap.abs() / 1e9
    result = _jerk_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of composite engine 252d
def f45nge_f45_network_growth_engine_compositeengine_252d_jerk_v150_signal(marketcap, revenue, ev):
    c = _f45_network_growth_compound(marketcap, 252)
    s = _f45_network_growth_superlinear(marketcap, revenue, 252)
    base = c * s * marketcap * ev / 1e9
    result = _jerk_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45nge_f45_network_growth_engine_compound_21d_jerk_v001_signal,
    f45nge_f45_network_growth_engine_compound_21d_jerk_v002_signal,
    f45nge_f45_network_growth_engine_compound_63d_jerk_v003_signal,
    f45nge_f45_network_growth_engine_compound_63d_jerk_v004_signal,
    f45nge_f45_network_growth_engine_compound_126d_jerk_v005_signal,
    f45nge_f45_network_growth_engine_compound_126d_jerk_v006_signal,
    f45nge_f45_network_growth_engine_compound_252d_jerk_v007_signal,
    f45nge_f45_network_growth_engine_compound_252d_jerk_v008_signal,
    f45nge_f45_network_growth_engine_compound_504d_jerk_v009_signal,
    f45nge_f45_network_growth_engine_compound_504d_jerk_v010_signal,
    f45nge_f45_network_growth_engine_superlin_21d_jerk_v011_signal,
    f45nge_f45_network_growth_engine_superlin_63d_jerk_v012_signal,
    f45nge_f45_network_growth_engine_superlin_252d_jerk_v013_signal,
    f45nge_f45_network_growth_engine_superlin_504d_jerk_v014_signal,
    f45nge_f45_network_growth_engine_accel_21d_jerk_v015_signal,
    f45nge_f45_network_growth_engine_accel_63d_jerk_v016_signal,
    f45nge_f45_network_growth_engine_accel_252d_jerk_v017_signal,
    f45nge_f45_network_growth_engine_accel_504d_jerk_v018_signal,
    f45nge_f45_network_growth_engine_evcomp_21d_jerk_v019_signal,
    f45nge_f45_network_growth_engine_evcomp_63d_jerk_v020_signal,
    f45nge_f45_network_growth_engine_evcomp_252d_jerk_v021_signal,
    f45nge_f45_network_growth_engine_evcomp_504d_jerk_v022_signal,
    f45nge_f45_network_growth_engine_sf3acomp_21d_jerk_v023_signal,
    f45nge_f45_network_growth_engine_sf3acomp_252d_jerk_v024_signal,
    f45nge_f45_network_growth_engine_sf3bcomp_252d_jerk_v025_signal,
    f45nge_f45_network_growth_engine_sf3bcomp_504d_jerk_v026_signal,
    f45nge_f45_network_growth_engine_evsuperlin_21d_jerk_v027_signal,
    f45nge_f45_network_growth_engine_evsuperlin_252d_jerk_v028_signal,
    f45nge_f45_network_growth_engine_evsuperlin_504d_jerk_v029_signal,
    f45nge_f45_network_growth_engine_mcvseb_21d_jerk_v030_signal,
    f45nge_f45_network_growth_engine_mcvseb_252d_jerk_v031_signal,
    f45nge_f45_network_growth_engine_mcvseb_504d_jerk_v032_signal,
    f45nge_f45_network_growth_engine_mcvsni_21d_jerk_v033_signal,
    f45nge_f45_network_growth_engine_mcvsni_252d_jerk_v034_signal,
    f45nge_f45_network_growth_engine_mcvsni_504d_jerk_v035_signal,
    f45nge_f45_network_growth_engine_mcvsfcf_21d_jerk_v036_signal,
    f45nge_f45_network_growth_engine_mcvsfcf_252d_jerk_v037_signal,
    f45nge_f45_network_growth_engine_mcvsfcf_504d_jerk_v038_signal,
    f45nge_f45_network_growth_engine_sf3ashcomp_21d_jerk_v039_signal,
    f45nge_f45_network_growth_engine_sf3ashcomp_252d_jerk_v040_signal,
    f45nge_f45_network_growth_engine_sf3bshcomp_252d_jerk_v041_signal,
    f45nge_f45_network_growth_engine_sf3bshcomp_504d_jerk_v042_signal,
    f45nge_f45_network_growth_engine_compxev_21d_jerk_v043_signal,
    f45nge_f45_network_growth_engine_compxev_63d_jerk_v044_signal,
    f45nge_f45_network_growth_engine_compxev_252d_jerk_v045_signal,
    f45nge_f45_network_growth_engine_compxev_504d_jerk_v046_signal,
    f45nge_f45_network_growth_engine_supsq_21d_jerk_v047_signal,
    f45nge_f45_network_growth_engine_supsq_63d_jerk_v048_signal,
    f45nge_f45_network_growth_engine_supsq_252d_jerk_v049_signal,
    f45nge_f45_network_growth_engine_supsq_504d_jerk_v050_signal,
    f45nge_f45_network_growth_engine_compxlogmc_21d_jerk_v051_signal,
    f45nge_f45_network_growth_engine_compxlogmc_252d_jerk_v052_signal,
    f45nge_f45_network_growth_engine_compxlogmc_504d_jerk_v053_signal,
    f45nge_f45_network_growth_engine_supxpe_21d_jerk_v054_signal,
    f45nge_f45_network_growth_engine_supxpe_252d_jerk_v055_signal,
    f45nge_f45_network_growth_engine_supxpe_504d_jerk_v056_signal,
    f45nge_f45_network_growth_engine_supxevebit_21d_jerk_v057_signal,
    f45nge_f45_network_growth_engine_supxevebit_252d_jerk_v058_signal,
    f45nge_f45_network_growth_engine_supxevebitda_252d_jerk_v059_signal,
    f45nge_f45_network_growth_engine_supxpb_252d_jerk_v060_signal,
    f45nge_f45_network_growth_engine_supxps_252d_jerk_v061_signal,
    f45nge_f45_network_growth_engine_compxrev_21d_jerk_v062_signal,
    f45nge_f45_network_growth_engine_compxrev_252d_jerk_v063_signal,
    f45nge_f45_network_growth_engine_compxrev_504d_jerk_v064_signal,
    f45nge_f45_network_growth_engine_compxeb_252d_jerk_v065_signal,
    f45nge_f45_network_growth_engine_compxeb_504d_jerk_v066_signal,
    f45nge_f45_network_growth_engine_compxni_252d_jerk_v067_signal,
    f45nge_f45_network_growth_engine_compxfcf_504d_jerk_v068_signal,
    f45nge_f45_network_growth_engine_compewm_63d_jerk_v069_signal,
    f45nge_f45_network_growth_engine_compewm_252d_jerk_v070_signal,
    f45nge_f45_network_growth_engine_compewm_504d_jerk_v071_signal,
    f45nge_f45_network_growth_engine_supewm_252d_jerk_v072_signal,
    f45nge_f45_network_growth_engine_supewm_504d_jerk_v073_signal,
    f45nge_f45_network_growth_engine_compxsf3a_252d_jerk_v074_signal,
    f45nge_f45_network_growth_engine_compxsf3b_504d_jerk_v075_signal,
    f45nge_f45_network_growth_engine_compxpe_21d_jerk_v076_signal,
    f45nge_f45_network_growth_engine_compxpe_252d_jerk_v077_signal,
    f45nge_f45_network_growth_engine_compxevebit_252d_jerk_v078_signal,
    f45nge_f45_network_growth_engine_compxevebitda_252d_jerk_v079_signal,
    f45nge_f45_network_growth_engine_compxpb_252d_jerk_v080_signal,
    f45nge_f45_network_growth_engine_compxps_252d_jerk_v081_signal,
    f45nge_f45_network_growth_engine_accxmc_21d_jerk_v082_signal,
    f45nge_f45_network_growth_engine_accxmc_252d_jerk_v083_signal,
    f45nge_f45_network_growth_engine_accxmc_504d_jerk_v084_signal,
    f45nge_f45_network_growth_engine_evaccxmc_21d_jerk_v085_signal,
    f45nge_f45_network_growth_engine_evaccxmc_252d_jerk_v086_signal,
    f45nge_f45_network_growth_engine_evaccxmc_504d_jerk_v087_signal,
    f45nge_f45_network_growth_engine_sf3aaccxmc_252d_jerk_v088_signal,
    f45nge_f45_network_growth_engine_sf3baccxmc_504d_jerk_v089_signal,
    f45nge_f45_network_growth_engine_compxdebt_21d_jerk_v090_signal,
    f45nge_f45_network_growth_engine_compxdebt_252d_jerk_v091_signal,
    f45nge_f45_network_growth_engine_compxdebt_504d_jerk_v092_signal,
    f45nge_f45_network_growth_engine_compxeq_21d_jerk_v093_signal,
    f45nge_f45_network_growth_engine_compxeq_252d_jerk_v094_signal,
    f45nge_f45_network_growth_engine_compxeq_504d_jerk_v095_signal,
    f45nge_f45_network_growth_engine_compxat_252d_jerk_v096_signal,
    f45nge_f45_network_growth_engine_compxat_504d_jerk_v097_signal,
    f45nge_f45_network_growth_engine_supxdebt_252d_jerk_v098_signal,
    f45nge_f45_network_growth_engine_supxeq_252d_jerk_v099_signal,
    f45nge_f45_network_growth_engine_supxat_252d_jerk_v100_signal,
    f45nge_f45_network_growth_engine_compxncfo_21d_jerk_v101_signal,
    f45nge_f45_network_growth_engine_compxncfo_252d_jerk_v102_signal,
    f45nge_f45_network_growth_engine_compxncfo_504d_jerk_v103_signal,
    f45nge_f45_network_growth_engine_evcompxev_21d_jerk_v104_signal,
    f45nge_f45_network_growth_engine_evcompxev_252d_jerk_v105_signal,
    f45nge_f45_network_growth_engine_evcompxev_504d_jerk_v106_signal,
    f45nge_f45_network_growth_engine_compxmcxrev_252d_jerk_v107_signal,
    f45nge_f45_network_growth_engine_supxmcxrev_504d_jerk_v108_signal,
    f45nge_f45_network_growth_engine_accxev_252d_jerk_v109_signal,
    f45nge_f45_network_growth_engine_accxev_504d_jerk_v110_signal,
    f45nge_f45_network_growth_engine_compxsf3ash_252d_jerk_v111_signal,
    f45nge_f45_network_growth_engine_compxsf3bsh_504d_jerk_v112_signal,
    f45nge_f45_network_growth_engine_compxevxrev_252d_jerk_v113_signal,
    f45nge_f45_network_growth_engine_supxevxrev_504d_jerk_v114_signal,
    f45nge_f45_network_growth_engine_triplecomp_21d_jerk_v115_signal,
    f45nge_f45_network_growth_engine_triplecomp_252d_jerk_v116_signal,
    f45nge_f45_network_growth_engine_triplecomp_504d_jerk_v117_signal,
    f45nge_f45_network_growth_engine_complogev_252d_jerk_v118_signal,
    f45nge_f45_network_growth_engine_complogev_504d_jerk_v119_signal,
    f45nge_f45_network_growth_engine_supvsncfo_21d_jerk_v120_signal,
    f45nge_f45_network_growth_engine_supvsncfo_252d_jerk_v121_signal,
    f45nge_f45_network_growth_engine_supvsncfo_504d_jerk_v122_signal,
    f45nge_f45_network_growth_engine_compxevebit_504d_jerk_v123_signal,
    f45nge_f45_network_growth_engine_compxevebitda_504d_jerk_v124_signal,
    f45nge_f45_network_growth_engine_compxpb_504d_jerk_v125_signal,
    f45nge_f45_network_growth_engine_compxps_504d_jerk_v126_signal,
    f45nge_f45_network_growth_engine_compxrevxmc_252d_jerk_v127_signal,
    f45nge_f45_network_growth_engine_compxebxmc_504d_jerk_v128_signal,
    f45nge_f45_network_growth_engine_supxmcxev_252d_jerk_v129_signal,
    f45nge_f45_network_growth_engine_supxmcxev_504d_jerk_v130_signal,
    f45nge_f45_network_growth_engine_complogevxmc_252d_jerk_v131_signal,
    f45nge_f45_network_growth_engine_complogevxmc_504d_jerk_v132_signal,
    f45nge_f45_network_growth_engine_compxsqrt_252d_jerk_v133_signal,
    f45nge_f45_network_growth_engine_supxsqrt_504d_jerk_v134_signal,
    f45nge_f45_network_growth_engine_compz_252d_jerk_v135_signal,
    f45nge_f45_network_growth_engine_compz_504d_jerk_v136_signal,
    f45nge_f45_network_growth_engine_supz_252d_jerk_v137_signal,
    f45nge_f45_network_growth_engine_accz_504d_jerk_v138_signal,
    f45nge_f45_network_growth_engine_compxsf3aval_252d_jerk_v139_signal,
    f45nge_f45_network_growth_engine_compxevz_252d_jerk_v140_signal,
    f45nge_f45_network_growth_engine_compxevz_504d_jerk_v141_signal,
    f45nge_f45_network_growth_engine_compxmcz_252d_jerk_v142_signal,
    f45nge_f45_network_growth_engine_compxmcz_504d_jerk_v143_signal,
    f45nge_f45_network_growth_engine_accxlogmc_252d_jerk_v144_signal,
    f45nge_f45_network_growth_engine_accxlogev_504d_jerk_v145_signal,
    f45nge_f45_network_growth_engine_compxevstd_252d_jerk_v146_signal,
    f45nge_f45_network_growth_engine_compxmcstd_504d_jerk_v147_signal,
    f45nge_f45_network_growth_engine_supxmcsq_252d_jerk_v148_signal,
    f45nge_f45_network_growth_engine_supxmcsq_504d_jerk_v149_signal,
    f45nge_f45_network_growth_engine_compositeengine_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_NETWORK_GROWTH_ENGINE_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")
    sf3a_shares = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="sf3a_shares")
    sf3a_value = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0005, 0.012, n))), name="sf3a_value")
    sf3b_shares = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.006, n))), name="sf3b_shares")
    sf3b_value = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0004, 0.013, n))), name="sf3b_value")

    cols = {
        "closeadj": closeadj, "marketcap": marketcap, "revenue": revenue,
        "netinc": netinc, "fcf": fcf, "ncfo": ncfo, "equity": equity,
        "debt": debt, "assets": assets, "ebitda": ebitda, "opinc": opinc,
        "sharesbas": sharesbas, "ev": ev, "evebit": evebit, "evebitda": evebitda,
        "pe": pe, "pb": pb, "ps": ps,
        "sf3a_shares": sf3a_shares, "sf3a_value": sf3a_value,
        "sf3b_shares": sf3b_shares, "sf3b_value": sf3b_value,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f45_network_growth_compound", "_f45_network_growth_superlinear",
                         "_f45_network_growth_acceleration")
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
    print(f"OK f45_network_growth_engine_3rd_derivatives_001_150_claude: {n_features} features pass")
