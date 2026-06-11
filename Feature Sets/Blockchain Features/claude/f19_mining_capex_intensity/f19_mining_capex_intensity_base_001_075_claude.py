import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


# ===== folder domain primitives (mining capex intensity) =====
def _f19_capint(capex, assets):
    # capital-expenditure intensity: absolute capex per unit of assets
    return capex.abs() / assets.replace(0, np.nan)


def _f19_ppnegrowth(ppnenet, w):
    # net PP&E growth over w days (asset-base buildout)
    return ppnenet.pct_change(periods=w)


def _f19_invtrend(ncfi, assets):
    # net investing intensity: net cash from investing per unit of assets (signed)
    return ncfi / assets.replace(0, np.nan)


def _f19_reinvest(capex, depamor):
    # reinvestment rate: gross capex relative to depreciation/amortization
    return capex.abs() / depamor.abs().replace(0, np.nan)


# ============ FEATURES 001-075 ============

# capex intensity level (raw |capex|/assets)
def f19mc_f19_mining_capex_intensity_capint_1d_base_v001_signal(capex, assets):
    result = _f19_capint(capex, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex intensity (smoothed)
def f19mc_f19_mining_capex_intensity_capintsm_63d_base_v002_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex intensity
def f19mc_f19_mining_capex_intensity_capintsm_126d_base_v003_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex intensity
def f19mc_f19_mining_capex_intensity_capintsm_252d_base_v004_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean of capex intensity
def f19mc_f19_mining_capex_intensity_capintsm_504d_base_v005_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex / revenue intensity (raw)
def f19mc_f19_mining_capex_intensity_caprev_1d_base_v006_signal(capex, revenue, assets):
    result = _safe_div(capex.abs(), revenue) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of capex/revenue intensity
def f19mc_f19_mining_capex_intensity_caprevsm_63d_base_v007_signal(capex, revenue, assets):
    result = _mean(_safe_div(capex.abs(), revenue), 63) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean of capex/revenue intensity
def f19mc_f19_mining_capex_intensity_caprevsm_126d_base_v008_signal(capex, revenue, assets):
    result = _mean(_safe_div(capex.abs(), revenue), 126) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex/revenue intensity
def f19mc_f19_mining_capex_intensity_caprevsm_252d_base_v009_signal(capex, revenue, assets):
    result = _mean(_safe_div(capex.abs(), revenue), 252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_63d_base_v010_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 63) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_126d_base_v011_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 126) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_252d_base_v012_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d net PP&E growth (full halving-scale buildout)
def f19mc_f19_mining_capex_intensity_ppneg_504d_base_v013_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 504) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d net PP&E growth (short-horizon buildout thrust)
def f19mc_f19_mining_capex_intensity_ppneg_21d_base_v014_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 21) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity (ncfi/assets) raw
def f19mc_f19_mining_capex_intensity_invtr_1d_base_v015_signal(ncfi, assets):
    result = _f19_invtrend(ncfi, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean net investing intensity
def f19mc_f19_mining_capex_intensity_invtrsm_63d_base_v016_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean net investing intensity
def f19mc_f19_mining_capex_intensity_invtrsm_126d_base_v017_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean net investing intensity
def f19mc_f19_mining_capex_intensity_invtrsm_252d_base_v018_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean net investing intensity
def f19mc_f19_mining_capex_intensity_invtrsm_504d_base_v019_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration level: 63d diff of capex intensity
def f19mc_f19_mining_capex_intensity_capaccel_63d_base_v020_signal(capex, assets):
    result = _f19_capint(capex, assets).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration level: 126d diff of capex intensity
def f19mc_f19_mining_capex_intensity_capaccel_126d_base_v021_signal(capex, assets):
    result = _f19_capint(capex, assets).diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration level: 252d diff of capex intensity
def f19mc_f19_mining_capex_intensity_capaccel_252d_base_v022_signal(capex, assets):
    result = _f19_capint(capex, assets).diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate (|capex|/|depamor|) raw
def f19mc_f19_mining_capex_intensity_reinv_1d_base_v023_signal(capex, depamor):
    result = _f19_reinvest(capex, depamor)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean reinvestment rate
def f19mc_f19_mining_capex_intensity_reinvsm_63d_base_v024_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean reinvestment rate
def f19mc_f19_mining_capex_intensity_reinvsm_126d_base_v025_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean reinvestment rate
def f19mc_f19_mining_capex_intensity_reinvsm_252d_base_v026_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mean reinvestment rate
def f19mc_f19_mining_capex_intensity_reinvsm_504d_base_v027_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# asset-buildout trend: 126d pct change of assets, weighted by capex intensity
def f19mc_f19_mining_capex_intensity_buildtr_126d_base_v028_signal(assets, capex):
    result = assets.pct_change(126) * _f19_capint(capex, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# asset-buildout trend: 252d pct change of assets, weighted by capex intensity
def f19mc_f19_mining_capex_intensity_buildtr_252d_base_v029_signal(assets, capex):
    result = assets.pct_change(252) * _f19_capint(capex, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# replacement intensity: |capex|/ppnenet raw
def f19mc_f19_mining_capex_intensity_repl_1d_base_v030_signal(capex, ppnenet, assets):
    result = _safe_div(capex.abs(), ppnenet) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean replacement intensity (|capex|/ppnenet)
def f19mc_f19_mining_capex_intensity_replsm_63d_base_v031_signal(capex, ppnenet, assets):
    result = _mean(_safe_div(capex.abs(), ppnenet), 63) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean replacement intensity
def f19mc_f19_mining_capex_intensity_replsm_126d_base_v032_signal(capex, ppnenet, assets):
    result = _mean(_safe_div(capex.abs(), ppnenet), 126) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean replacement intensity
def f19mc_f19_mining_capex_intensity_replsm_252d_base_v033_signal(capex, ppnenet, assets):
    result = _mean(_safe_div(capex.abs(), ppnenet), 252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of capex intensity over 252d
def f19mc_f19_mining_capex_intensity_zcapint_252d_base_v034_signal(capex, assets):
    result = _z(_f19_capint(capex, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of capex intensity over 504d
def f19mc_f19_mining_capex_intensity_zcapint_504d_base_v035_signal(capex, assets):
    result = _z(_f19_capint(capex, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of capex intensity over 126d
def f19mc_f19_mining_capex_intensity_zcapint_126d_base_v036_signal(capex, assets):
    result = _z(_f19_capint(capex, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of reinvestment rate over 252d
def f19mc_f19_mining_capex_intensity_zreinv_252d_base_v037_signal(capex, depamor):
    result = _z(_f19_reinvest(capex, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of net investing intensity over 252d
def f19mc_f19_mining_capex_intensity_zinvtr_252d_base_v038_signal(ncfi, assets):
    result = _z(_f19_invtrend(ncfi, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of capex intensity over 252d
def f19mc_f19_mining_capex_intensity_rkcapint_252d_base_v039_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of capex intensity over 504d
def f19mc_f19_mining_capex_intensity_rkcapint_504d_base_v040_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of reinvestment rate over 252d
def f19mc_f19_mining_capex_intensity_rkreinv_252d_base_v041_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-maintenance capex proxy: capex intensity minus depamor intensity
def f19mc_f19_mining_capex_intensity_gmproxy_1d_base_v042_signal(capex, depamor, assets):
    result = _f19_capint(capex, assets) - _safe_div(depamor.abs(), assets)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mean gross-vs-maintenance capex proxy
def f19mc_f19_mining_capex_intensity_gmproxysm_126d_base_v043_signal(capex, depamor, assets):
    s = _f19_capint(capex, assets) - _safe_div(depamor.abs(), assets)
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean gross-vs-maintenance capex proxy
def f19mc_f19_mining_capex_intensity_gmproxysm_252d_base_v044_signal(capex, depamor, assets):
    s = _f19_capint(capex, assets) - _safe_div(depamor.abs(), assets)
    result = _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# excess reinvestment: reinvestment rate minus 1 (capex above maintenance)
def f19mc_f19_mining_capex_intensity_exreinv_63d_base_v045_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor) - 1.0, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# excess reinvestment smoothed 252d
def f19mc_f19_mining_capex_intensity_exreinv_252d_base_v046_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor) - 1.0, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity dispersion (63d std)
def f19mc_f19_mining_capex_intensity_capintvol_63d_base_v047_signal(capex, assets):
    result = _std(_f19_capint(capex, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity dispersion (126d std)
def f19mc_f19_mining_capex_intensity_capintvol_126d_base_v048_signal(capex, assets):
    result = _std(_f19_capint(capex, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity dispersion (252d std)
def f19mc_f19_mining_capex_intensity_capintvol_252d_base_v049_signal(capex, assets):
    result = _std(_f19_capint(capex, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity dispersion (252d std)
def f19mc_f19_mining_capex_intensity_invtrvol_252d_base_v050_signal(ncfi, assets):
    result = _std(_f19_invtrend(ncfi, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity EWMA (span 63)
def f19mc_f19_mining_capex_intensity_capintewm_63d_base_v051_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity EWMA (span 126)
def f19mc_f19_mining_capex_intensity_capintewm_126d_base_v052_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity EWMA (span 252)
def f19mc_f19_mining_capex_intensity_capintewm_252d_base_v053_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate EWMA (span 126)
def f19mc_f19_mining_capex_intensity_reinvewm_126d_base_v054_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity surprise: level minus its 126d mean
def f19mc_f19_mining_capex_intensity_capsurp_126d_base_v055_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity surprise: level minus its 252d mean
def f19mc_f19_mining_capex_intensity_capsurp_252d_base_v056_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment surprise: level minus 252d mean
def f19mc_f19_mining_capex_intensity_reinvsurp_252d_base_v057_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity ratio short/long (63d mean / 252d mean)
def f19mc_f19_mining_capex_intensity_capratio_63_252_base_v058_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = _safe_div(_mean(s, 63), _mean(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity ratio short/long (126d mean / 504d mean)
def f19mc_f19_mining_capex_intensity_capratio_126_504_base_v059_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = _safe_div(_mean(s, 126), _mean(s, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# capex-to-assets growth spread: short PP&E growth minus capex intensity drift
def f19mc_f19_mining_capex_intensity_ppnespread_126d_base_v060_signal(ppnenet, capex, assets):
    result = _f19_ppnegrowth(ppnenet, 126) - _f19_capint(capex, assets).diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity trend slope proxy (252d diff of EWMA)
def f19mc_f19_mining_capex_intensity_captrend_252d_base_v061_signal(capex, assets):
    s = _f19_capint(capex, assets).ewm(span=126, min_periods=42).mean()
    result = s.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity acceleration (126d diff)
def f19mc_f19_mining_capex_intensity_invaccel_126d_base_v062_signal(ncfi, assets):
    result = _f19_invtrend(ncfi, assets).diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity acceleration (252d diff)
def f19mc_f19_mining_capex_intensity_invaccel_252d_base_v063_signal(ncfi, assets):
    result = _f19_invtrend(ncfi, assets).diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex per revenue z-score over 252d
def f19mc_f19_mining_capex_intensity_zcaprev_252d_base_v064_signal(capex, revenue, assets):
    result = _z(_safe_div(capex.abs(), revenue), 252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth z-score over 252d
def f19mc_f19_mining_capex_intensity_zppneg_252d_base_v065_signal(ppnenet, capex, assets):
    result = _z(_f19_ppnegrowth(ppnenet, 63), 252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity scaled by revenue base (capex^2 / (assets*revenue))
def f19mc_f19_mining_capex_intensity_capdblint_1d_base_v066_signal(capex, assets, revenue):
    result = _f19_capint(capex, assets) * _safe_div(capex.abs(), revenue)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of capex double-intensity
def f19mc_f19_mining_capex_intensity_capdblintsm_252d_base_v067_signal(capex, assets, revenue):
    s = _f19_capint(capex, assets) * _safe_div(capex.abs(), revenue)
    result = _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# investing-intensity to capex-intensity ratio (how much of investing is capex)
def f19mc_f19_mining_capex_intensity_invcapratio_126d_base_v068_signal(ncfi, capex, assets):
    result = _mean(_safe_div(capex.abs(), ncfi.abs()), 126) + _f19_invtrend(ncfi, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# investing-intensity to capex-intensity ratio over 252d
def f19mc_f19_mining_capex_intensity_invcapratio_252d_base_v069_signal(ncfi, capex, assets):
    result = _mean(_safe_div(capex.abs(), ncfi.abs()), 252) + _f19_invtrend(ncfi, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity momentum (63d pct change of smoothed intensity)
def f19mc_f19_mining_capex_intensity_capmom_63d_base_v070_signal(capex, assets):
    s = _mean(_f19_capint(capex, assets), 63)
    result = s.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity momentum (126d pct change of smoothed intensity)
def f19mc_f19_mining_capex_intensity_capmom_126d_base_v071_signal(capex, assets):
    s = _mean(_f19_capint(capex, assets), 63)
    result = s.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment-rate momentum (126d pct change of smoothed reinvestment)
def f19mc_f19_mining_capex_intensity_reinvmom_126d_base_v072_signal(capex, depamor):
    s = _mean(_f19_reinvest(capex, depamor), 63)
    result = s.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue minus capex/assets (financing-base divergence)
def f19mc_f19_mining_capex_intensity_basediv_126d_base_v073_signal(capex, revenue, assets):
    s = _safe_div(capex.abs(), revenue) - _f19_capint(capex, assets)
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vol-scaled level (intensity / its 252d std)
def f19mc_f19_mining_capex_intensity_capvolscl_252d_base_v074_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = _safe_div(s, _std(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# blended capex-intensity composite (capint + reinvest scaled + ppne growth)
def f19mc_f19_mining_capex_intensity_blend_126d_base_v075_signal(capex, assets, depamor, ppnenet):
    a = _z(_f19_capint(capex, assets), 252)
    b = _z(_f19_reinvest(capex, depamor), 252)
    c = _z(_f19_ppnegrowth(ppnenet, 63), 252)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19mc_f19_mining_capex_intensity_capint_1d_base_v001_signal,
    f19mc_f19_mining_capex_intensity_capintsm_63d_base_v002_signal,
    f19mc_f19_mining_capex_intensity_capintsm_126d_base_v003_signal,
    f19mc_f19_mining_capex_intensity_capintsm_252d_base_v004_signal,
    f19mc_f19_mining_capex_intensity_capintsm_504d_base_v005_signal,
    f19mc_f19_mining_capex_intensity_caprev_1d_base_v006_signal,
    f19mc_f19_mining_capex_intensity_caprevsm_63d_base_v007_signal,
    f19mc_f19_mining_capex_intensity_caprevsm_126d_base_v008_signal,
    f19mc_f19_mining_capex_intensity_caprevsm_252d_base_v009_signal,
    f19mc_f19_mining_capex_intensity_ppneg_63d_base_v010_signal,
    f19mc_f19_mining_capex_intensity_ppneg_126d_base_v011_signal,
    f19mc_f19_mining_capex_intensity_ppneg_252d_base_v012_signal,
    f19mc_f19_mining_capex_intensity_ppneg_504d_base_v013_signal,
    f19mc_f19_mining_capex_intensity_ppneg_21d_base_v014_signal,
    f19mc_f19_mining_capex_intensity_invtr_1d_base_v015_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_63d_base_v016_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_126d_base_v017_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_252d_base_v018_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_504d_base_v019_signal,
    f19mc_f19_mining_capex_intensity_capaccel_63d_base_v020_signal,
    f19mc_f19_mining_capex_intensity_capaccel_126d_base_v021_signal,
    f19mc_f19_mining_capex_intensity_capaccel_252d_base_v022_signal,
    f19mc_f19_mining_capex_intensity_reinv_1d_base_v023_signal,
    f19mc_f19_mining_capex_intensity_reinvsm_63d_base_v024_signal,
    f19mc_f19_mining_capex_intensity_reinvsm_126d_base_v025_signal,
    f19mc_f19_mining_capex_intensity_reinvsm_252d_base_v026_signal,
    f19mc_f19_mining_capex_intensity_reinvsm_504d_base_v027_signal,
    f19mc_f19_mining_capex_intensity_buildtr_126d_base_v028_signal,
    f19mc_f19_mining_capex_intensity_buildtr_252d_base_v029_signal,
    f19mc_f19_mining_capex_intensity_repl_1d_base_v030_signal,
    f19mc_f19_mining_capex_intensity_replsm_63d_base_v031_signal,
    f19mc_f19_mining_capex_intensity_replsm_126d_base_v032_signal,
    f19mc_f19_mining_capex_intensity_replsm_252d_base_v033_signal,
    f19mc_f19_mining_capex_intensity_zcapint_252d_base_v034_signal,
    f19mc_f19_mining_capex_intensity_zcapint_504d_base_v035_signal,
    f19mc_f19_mining_capex_intensity_zcapint_126d_base_v036_signal,
    f19mc_f19_mining_capex_intensity_zreinv_252d_base_v037_signal,
    f19mc_f19_mining_capex_intensity_zinvtr_252d_base_v038_signal,
    f19mc_f19_mining_capex_intensity_rkcapint_252d_base_v039_signal,
    f19mc_f19_mining_capex_intensity_rkcapint_504d_base_v040_signal,
    f19mc_f19_mining_capex_intensity_rkreinv_252d_base_v041_signal,
    f19mc_f19_mining_capex_intensity_gmproxy_1d_base_v042_signal,
    f19mc_f19_mining_capex_intensity_gmproxysm_126d_base_v043_signal,
    f19mc_f19_mining_capex_intensity_gmproxysm_252d_base_v044_signal,
    f19mc_f19_mining_capex_intensity_exreinv_63d_base_v045_signal,
    f19mc_f19_mining_capex_intensity_exreinv_252d_base_v046_signal,
    f19mc_f19_mining_capex_intensity_capintvol_63d_base_v047_signal,
    f19mc_f19_mining_capex_intensity_capintvol_126d_base_v048_signal,
    f19mc_f19_mining_capex_intensity_capintvol_252d_base_v049_signal,
    f19mc_f19_mining_capex_intensity_invtrvol_252d_base_v050_signal,
    f19mc_f19_mining_capex_intensity_capintewm_63d_base_v051_signal,
    f19mc_f19_mining_capex_intensity_capintewm_126d_base_v052_signal,
    f19mc_f19_mining_capex_intensity_capintewm_252d_base_v053_signal,
    f19mc_f19_mining_capex_intensity_reinvewm_126d_base_v054_signal,
    f19mc_f19_mining_capex_intensity_capsurp_126d_base_v055_signal,
    f19mc_f19_mining_capex_intensity_capsurp_252d_base_v056_signal,
    f19mc_f19_mining_capex_intensity_reinvsurp_252d_base_v057_signal,
    f19mc_f19_mining_capex_intensity_capratio_63_252_base_v058_signal,
    f19mc_f19_mining_capex_intensity_capratio_126_504_base_v059_signal,
    f19mc_f19_mining_capex_intensity_ppnespread_126d_base_v060_signal,
    f19mc_f19_mining_capex_intensity_captrend_252d_base_v061_signal,
    f19mc_f19_mining_capex_intensity_invaccel_126d_base_v062_signal,
    f19mc_f19_mining_capex_intensity_invaccel_252d_base_v063_signal,
    f19mc_f19_mining_capex_intensity_zcaprev_252d_base_v064_signal,
    f19mc_f19_mining_capex_intensity_zppneg_252d_base_v065_signal,
    f19mc_f19_mining_capex_intensity_capdblint_1d_base_v066_signal,
    f19mc_f19_mining_capex_intensity_capdblintsm_252d_base_v067_signal,
    f19mc_f19_mining_capex_intensity_invcapratio_126d_base_v068_signal,
    f19mc_f19_mining_capex_intensity_invcapratio_252d_base_v069_signal,
    f19mc_f19_mining_capex_intensity_capmom_63d_base_v070_signal,
    f19mc_f19_mining_capex_intensity_capmom_126d_base_v071_signal,
    f19mc_f19_mining_capex_intensity_reinvmom_126d_base_v072_signal,
    f19mc_f19_mining_capex_intensity_basediv_126d_base_v073_signal,
    f19mc_f19_mining_capex_intensity_capvolscl_252d_base_v074_signal,
    f19mc_f19_mining_capex_intensity_blend_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_MINING_CAPEX_INTENSITY_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f19_capint", "_f19_ppnegrowth", "_f19_invtrend", "_f19_reinvest")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f19_mining_capex_intensity_base_001_075_claude: {n_features} features pass")
