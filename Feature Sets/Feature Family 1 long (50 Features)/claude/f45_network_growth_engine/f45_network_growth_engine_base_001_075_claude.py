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


# 21d compounding marketcap growth × marketcap
def f45nge_f45_network_growth_engine_compound_21d_base_v001_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d compounding marketcap growth × marketcap
def f45nge_f45_network_growth_engine_compound_63d_base_v002_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d compounding marketcap growth × marketcap
def f45nge_f45_network_growth_engine_compound_126d_base_v003_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compounding marketcap growth × marketcap
def f45nge_f45_network_growth_engine_compound_252d_base_v004_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compounding marketcap growth × marketcap
def f45nge_f45_network_growth_engine_compound_504d_base_v005_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d super-linear marketcap vs revenue × marketcap
def f45nge_f45_network_growth_engine_superlin_21d_base_v006_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d super-linear marketcap vs revenue × marketcap
def f45nge_f45_network_growth_engine_superlin_63d_base_v007_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d super-linear marketcap vs revenue × marketcap
def f45nge_f45_network_growth_engine_superlin_126d_base_v008_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear marketcap vs revenue × marketcap
def f45nge_f45_network_growth_engine_superlin_252d_base_v009_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d super-linear marketcap vs revenue × marketcap
def f45nge_f45_network_growth_engine_superlin_504d_base_v010_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap acceleration × ev
def f45nge_f45_network_growth_engine_accel_21d_base_v011_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap acceleration × ev
def f45nge_f45_network_growth_engine_accel_63d_base_v012_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 126d marketcap acceleration × ev
def f45nge_f45_network_growth_engine_accel_126d_base_v013_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 126) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap acceleration × ev
def f45nge_f45_network_growth_engine_accel_252d_base_v014_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap acceleration × ev
def f45nge_f45_network_growth_engine_accel_504d_base_v015_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev compound growth × marketcap
def f45nge_f45_network_growth_engine_evcomp_21d_base_v016_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev compound growth × marketcap
def f45nge_f45_network_growth_engine_evcomp_63d_base_v017_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev compound growth × marketcap
def f45nge_f45_network_growth_engine_evcomp_252d_base_v018_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev compound growth × marketcap
def f45nge_f45_network_growth_engine_evcomp_504d_base_v019_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a value compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3acomp_21d_base_v020_signal(sf3a_value, marketcap):
    result = _f45_network_growth_compound(sf3a_value, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3acomp_252d_base_v021_signal(sf3a_value, marketcap):
    result = _f45_network_growth_compound(sf3a_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b value compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3bcomp_252d_base_v022_signal(sf3b_value, marketcap):
    result = _f45_network_growth_compound(sf3b_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3bcomp_504d_base_v023_signal(sf3b_value, marketcap):
    result = _f45_network_growth_compound(sf3b_value, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev super-linear vs revenue × marketcap
def f45nge_f45_network_growth_engine_evsuperlin_21d_base_v024_signal(ev, revenue, marketcap):
    result = _f45_network_growth_superlinear(ev, revenue, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev super-linear vs revenue × marketcap
def f45nge_f45_network_growth_engine_evsuperlin_252d_base_v025_signal(ev, revenue, marketcap):
    result = _f45_network_growth_superlinear(ev, revenue, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev super-linear vs revenue × marketcap
def f45nge_f45_network_growth_engine_evsuperlin_504d_base_v026_signal(ev, revenue, marketcap):
    result = _f45_network_growth_superlinear(ev, revenue, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap super-linear vs ebitda × marketcap
def f45nge_f45_network_growth_engine_mcvseb_21d_base_v027_signal(marketcap, ebitda):
    result = _f45_network_growth_superlinear(marketcap, ebitda, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap super-linear vs ebitda × marketcap
def f45nge_f45_network_growth_engine_mcvseb_252d_base_v028_signal(marketcap, ebitda):
    result = _f45_network_growth_superlinear(marketcap, ebitda, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap super-linear vs ebitda × marketcap
def f45nge_f45_network_growth_engine_mcvseb_504d_base_v029_signal(marketcap, ebitda):
    result = _f45_network_growth_superlinear(marketcap, ebitda, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap super-linear vs netinc × ev
def f45nge_f45_network_growth_engine_mcvsni_21d_base_v030_signal(marketcap, netinc, ev):
    result = _f45_network_growth_superlinear(marketcap, netinc, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap super-linear vs netinc × ev
def f45nge_f45_network_growth_engine_mcvsni_252d_base_v031_signal(marketcap, netinc, ev):
    result = _f45_network_growth_superlinear(marketcap, netinc, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap super-linear vs netinc × ev
def f45nge_f45_network_growth_engine_mcvsni_504d_base_v032_signal(marketcap, netinc, ev):
    result = _f45_network_growth_superlinear(marketcap, netinc, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap super-linear vs fcf × ev
def f45nge_f45_network_growth_engine_mcvsfcf_21d_base_v033_signal(marketcap, fcf, ev):
    result = _f45_network_growth_superlinear(marketcap, fcf, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap super-linear vs fcf × ev
def f45nge_f45_network_growth_engine_mcvsfcf_252d_base_v034_signal(marketcap, fcf, ev):
    result = _f45_network_growth_superlinear(marketcap, fcf, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap super-linear vs fcf × ev
def f45nge_f45_network_growth_engine_mcvsfcf_504d_base_v035_signal(marketcap, fcf, ev):
    result = _f45_network_growth_superlinear(marketcap, fcf, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a shares compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3ashcomp_21d_base_v036_signal(sf3a_shares, marketcap):
    result = _f45_network_growth_compound(sf3a_shares, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a shares compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3ashcomp_252d_base_v037_signal(sf3a_shares, marketcap):
    result = _f45_network_growth_compound(sf3a_shares, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b shares compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3bshcomp_252d_base_v038_signal(sf3b_shares, marketcap):
    result = _f45_network_growth_compound(sf3b_shares, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b shares compound growth × marketcap
def f45nge_f45_network_growth_engine_sf3bshcomp_504d_base_v039_signal(sf3b_shares, marketcap):
    result = _f45_network_growth_compound(sf3b_shares, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × ev (network engine compound capital)
def f45nge_f45_network_growth_engine_compxev_21d_base_v040_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d compound × ev
def f45nge_f45_network_growth_engine_compxev_63d_base_v041_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ev
def f45nge_f45_network_growth_engine_compxev_252d_base_v042_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × ev
def f45nge_f45_network_growth_engine_compxev_504d_base_v043_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d super-linear squared × marketcap (super-network)
def f45nge_f45_network_growth_engine_superlinsq_21d_base_v044_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 21)
    result = s * s.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d super-linear squared × marketcap
def f45nge_f45_network_growth_engine_superlinsq_63d_base_v045_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 63)
    result = s * s.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear squared × marketcap
def f45nge_f45_network_growth_engine_superlinsq_252d_base_v046_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 252)
    result = s * s.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d super-linear squared × marketcap
def f45nge_f45_network_growth_engine_superlinsq_504d_base_v047_signal(marketcap, revenue):
    s = _f45_network_growth_superlinear(marketcap, revenue, 504)
    result = s * s.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × log marketcap
def f45nge_f45_network_growth_engine_compxlogmc_21d_base_v048_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 21) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × log marketcap
def f45nge_f45_network_growth_engine_compxlogmc_252d_base_v049_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × log marketcap
def f45nge_f45_network_growth_engine_compxlogmc_504d_base_v050_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 504) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d super-linear × pe (network valuation richness)
def f45nge_f45_network_growth_engine_supxpe_21d_base_v051_signal(marketcap, revenue, pe):
    result = _f45_network_growth_superlinear(marketcap, revenue, 21) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear × pe
def f45nge_f45_network_growth_engine_supxpe_252d_base_v052_signal(marketcap, revenue, pe):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d super-linear × pe
def f45nge_f45_network_growth_engine_supxpe_504d_base_v053_signal(marketcap, revenue, pe):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d super-linear × evebit
def f45nge_f45_network_growth_engine_supxevebit_21d_base_v054_signal(marketcap, revenue, evebit):
    result = _f45_network_growth_superlinear(marketcap, revenue, 21) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear × evebit
def f45nge_f45_network_growth_engine_supxevebit_252d_base_v055_signal(marketcap, revenue, evebit):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear × evebitda
def f45nge_f45_network_growth_engine_supxevebitda_252d_base_v056_signal(marketcap, revenue, evebitda):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear × pb
def f45nge_f45_network_growth_engine_supxpb_252d_base_v057_signal(marketcap, revenue, pb):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear × ps
def f45nge_f45_network_growth_engine_supxps_252d_base_v058_signal(marketcap, revenue, ps):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × revenue (network engine fueled by sales)
def f45nge_f45_network_growth_engine_compxrev_21d_base_v059_signal(marketcap, revenue):
    result = _f45_network_growth_compound(marketcap, 21) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × revenue
def f45nge_f45_network_growth_engine_compxrev_252d_base_v060_signal(marketcap, revenue):
    result = _f45_network_growth_compound(marketcap, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × revenue
def f45nge_f45_network_growth_engine_compxrev_504d_base_v061_signal(marketcap, revenue):
    result = _f45_network_growth_compound(marketcap, 504) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ebitda
def f45nge_f45_network_growth_engine_compxeb_252d_base_v062_signal(marketcap, ebitda):
    result = _f45_network_growth_compound(marketcap, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × ebitda
def f45nge_f45_network_growth_engine_compxeb_504d_base_v063_signal(marketcap, ebitda):
    result = _f45_network_growth_compound(marketcap, 504) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × netinc
def f45nge_f45_network_growth_engine_compxni_252d_base_v064_signal(marketcap, netinc):
    result = _f45_network_growth_compound(marketcap, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × fcf
def f45nge_f45_network_growth_engine_compxfcf_504d_base_v065_signal(marketcap, fcf):
    result = _f45_network_growth_compound(marketcap, 504) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound EWM × marketcap
def f45nge_f45_network_growth_engine_compewm_63d_base_v066_signal(marketcap):
    base_ = _f45_network_growth_compound(marketcap, 63)
    result = base_.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound EWM × marketcap
def f45nge_f45_network_growth_engine_compewm_252d_base_v067_signal(marketcap):
    base_ = _f45_network_growth_compound(marketcap, 252)
    result = base_.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound EWM × marketcap
def f45nge_f45_network_growth_engine_compewm_504d_base_v068_signal(marketcap):
    base_ = _f45_network_growth_compound(marketcap, 504)
    result = base_.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear EWM × marketcap
def f45nge_f45_network_growth_engine_supewm_252d_base_v069_signal(marketcap, revenue):
    base_ = _f45_network_growth_superlinear(marketcap, revenue, 252)
    result = base_.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d super-linear EWM × marketcap
def f45nge_f45_network_growth_engine_supewm_504d_base_v070_signal(marketcap, revenue):
    base_ = _f45_network_growth_superlinear(marketcap, revenue, 504)
    result = base_.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × sf3a value (institutional confirmed network growth)
def f45nge_f45_network_growth_engine_compxsf3a_252d_base_v071_signal(marketcap, sf3a_value):
    result = _f45_network_growth_compound(marketcap, 252) * _mean(sf3a_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × sf3b value
def f45nge_f45_network_growth_engine_compxsf3b_504d_base_v072_signal(marketcap, sf3b_value):
    result = _f45_network_growth_compound(marketcap, 504) * _mean(sf3b_value, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear × sf3a value
def f45nge_f45_network_growth_engine_supxsf3a_252d_base_v073_signal(marketcap, revenue, sf3a_value):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * _mean(sf3a_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration × sf3b value
def f45nge_f45_network_growth_engine_accxsf3b_252d_base_v074_signal(marketcap, sf3b_value):
    result = _f45_network_growth_acceleration(marketcap, 252) * _mean(sf3b_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × marketcap squared (super engine)
def f45nge_f45_network_growth_engine_compxmcsq_252d_base_v075_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 252) * marketcap * marketcap.abs() / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45nge_f45_network_growth_engine_compound_21d_base_v001_signal,
    f45nge_f45_network_growth_engine_compound_63d_base_v002_signal,
    f45nge_f45_network_growth_engine_compound_126d_base_v003_signal,
    f45nge_f45_network_growth_engine_compound_252d_base_v004_signal,
    f45nge_f45_network_growth_engine_compound_504d_base_v005_signal,
    f45nge_f45_network_growth_engine_superlin_21d_base_v006_signal,
    f45nge_f45_network_growth_engine_superlin_63d_base_v007_signal,
    f45nge_f45_network_growth_engine_superlin_126d_base_v008_signal,
    f45nge_f45_network_growth_engine_superlin_252d_base_v009_signal,
    f45nge_f45_network_growth_engine_superlin_504d_base_v010_signal,
    f45nge_f45_network_growth_engine_accel_21d_base_v011_signal,
    f45nge_f45_network_growth_engine_accel_63d_base_v012_signal,
    f45nge_f45_network_growth_engine_accel_126d_base_v013_signal,
    f45nge_f45_network_growth_engine_accel_252d_base_v014_signal,
    f45nge_f45_network_growth_engine_accel_504d_base_v015_signal,
    f45nge_f45_network_growth_engine_evcomp_21d_base_v016_signal,
    f45nge_f45_network_growth_engine_evcomp_63d_base_v017_signal,
    f45nge_f45_network_growth_engine_evcomp_252d_base_v018_signal,
    f45nge_f45_network_growth_engine_evcomp_504d_base_v019_signal,
    f45nge_f45_network_growth_engine_sf3acomp_21d_base_v020_signal,
    f45nge_f45_network_growth_engine_sf3acomp_252d_base_v021_signal,
    f45nge_f45_network_growth_engine_sf3bcomp_252d_base_v022_signal,
    f45nge_f45_network_growth_engine_sf3bcomp_504d_base_v023_signal,
    f45nge_f45_network_growth_engine_evsuperlin_21d_base_v024_signal,
    f45nge_f45_network_growth_engine_evsuperlin_252d_base_v025_signal,
    f45nge_f45_network_growth_engine_evsuperlin_504d_base_v026_signal,
    f45nge_f45_network_growth_engine_mcvseb_21d_base_v027_signal,
    f45nge_f45_network_growth_engine_mcvseb_252d_base_v028_signal,
    f45nge_f45_network_growth_engine_mcvseb_504d_base_v029_signal,
    f45nge_f45_network_growth_engine_mcvsni_21d_base_v030_signal,
    f45nge_f45_network_growth_engine_mcvsni_252d_base_v031_signal,
    f45nge_f45_network_growth_engine_mcvsni_504d_base_v032_signal,
    f45nge_f45_network_growth_engine_mcvsfcf_21d_base_v033_signal,
    f45nge_f45_network_growth_engine_mcvsfcf_252d_base_v034_signal,
    f45nge_f45_network_growth_engine_mcvsfcf_504d_base_v035_signal,
    f45nge_f45_network_growth_engine_sf3ashcomp_21d_base_v036_signal,
    f45nge_f45_network_growth_engine_sf3ashcomp_252d_base_v037_signal,
    f45nge_f45_network_growth_engine_sf3bshcomp_252d_base_v038_signal,
    f45nge_f45_network_growth_engine_sf3bshcomp_504d_base_v039_signal,
    f45nge_f45_network_growth_engine_compxev_21d_base_v040_signal,
    f45nge_f45_network_growth_engine_compxev_63d_base_v041_signal,
    f45nge_f45_network_growth_engine_compxev_252d_base_v042_signal,
    f45nge_f45_network_growth_engine_compxev_504d_base_v043_signal,
    f45nge_f45_network_growth_engine_superlinsq_21d_base_v044_signal,
    f45nge_f45_network_growth_engine_superlinsq_63d_base_v045_signal,
    f45nge_f45_network_growth_engine_superlinsq_252d_base_v046_signal,
    f45nge_f45_network_growth_engine_superlinsq_504d_base_v047_signal,
    f45nge_f45_network_growth_engine_compxlogmc_21d_base_v048_signal,
    f45nge_f45_network_growth_engine_compxlogmc_252d_base_v049_signal,
    f45nge_f45_network_growth_engine_compxlogmc_504d_base_v050_signal,
    f45nge_f45_network_growth_engine_supxpe_21d_base_v051_signal,
    f45nge_f45_network_growth_engine_supxpe_252d_base_v052_signal,
    f45nge_f45_network_growth_engine_supxpe_504d_base_v053_signal,
    f45nge_f45_network_growth_engine_supxevebit_21d_base_v054_signal,
    f45nge_f45_network_growth_engine_supxevebit_252d_base_v055_signal,
    f45nge_f45_network_growth_engine_supxevebitda_252d_base_v056_signal,
    f45nge_f45_network_growth_engine_supxpb_252d_base_v057_signal,
    f45nge_f45_network_growth_engine_supxps_252d_base_v058_signal,
    f45nge_f45_network_growth_engine_compxrev_21d_base_v059_signal,
    f45nge_f45_network_growth_engine_compxrev_252d_base_v060_signal,
    f45nge_f45_network_growth_engine_compxrev_504d_base_v061_signal,
    f45nge_f45_network_growth_engine_compxeb_252d_base_v062_signal,
    f45nge_f45_network_growth_engine_compxeb_504d_base_v063_signal,
    f45nge_f45_network_growth_engine_compxni_252d_base_v064_signal,
    f45nge_f45_network_growth_engine_compxfcf_504d_base_v065_signal,
    f45nge_f45_network_growth_engine_compewm_63d_base_v066_signal,
    f45nge_f45_network_growth_engine_compewm_252d_base_v067_signal,
    f45nge_f45_network_growth_engine_compewm_504d_base_v068_signal,
    f45nge_f45_network_growth_engine_supewm_252d_base_v069_signal,
    f45nge_f45_network_growth_engine_supewm_504d_base_v070_signal,
    f45nge_f45_network_growth_engine_compxsf3a_252d_base_v071_signal,
    f45nge_f45_network_growth_engine_compxsf3b_504d_base_v072_signal,
    f45nge_f45_network_growth_engine_supxsf3a_252d_base_v073_signal,
    f45nge_f45_network_growth_engine_accxsf3b_252d_base_v074_signal,
    f45nge_f45_network_growth_engine_compxmcsq_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_NETWORK_GROWTH_ENGINE_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f45_network_growth_engine_base_001_075_claude: {n_features} features pass")
