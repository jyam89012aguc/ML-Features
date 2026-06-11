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


# ============ FEATURES 076-150 ============

# 84d mean capex intensity
def f19mc_f19_mining_capex_intensity_capintsm_84d_base_v076_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mean capex intensity
def f19mc_f19_mining_capex_intensity_capintsm_189d_base_v077_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d mean capex intensity
def f19mc_f19_mining_capex_intensity_capintsm_378d_base_v078_signal(capex, assets):
    result = _mean(_f19_capint(capex, assets), 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_42d_base_v079_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 42) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_84d_base_v080_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 84) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_189d_base_v081_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 189) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 378d net PP&E growth
def f19mc_f19_mining_capex_intensity_ppneg_378d_base_v082_signal(ppnenet, assets, capex):
    result = _f19_ppnegrowth(ppnenet, 378) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed PP&E growth (63d mean of 63d growth)
def f19mc_f19_mining_capex_intensity_ppnegsm_63d_base_v083_signal(ppnenet, assets, capex):
    result = _mean(_f19_ppnegrowth(ppnenet, 63), 63) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed PP&E growth (126d mean of 126d growth)
def f19mc_f19_mining_capex_intensity_ppnegsm_126d_base_v084_signal(ppnenet, assets, capex):
    result = _mean(_f19_ppnegrowth(ppnenet, 126), 126) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth EWMA (span 126)
def f19mc_f19_mining_capex_intensity_ppnegewm_126d_base_v085_signal(ppnenet, assets, capex):
    s = _f19_ppnegrowth(ppnenet, 63)
    result = s.ewm(span=126, min_periods=42).mean() + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity skew over 252d (asymmetry of spend bursts)
def f19mc_f19_mining_capex_intensity_capintskew_252d_base_v086_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity skew over 504d
def f19mc_f19_mining_capex_intensity_capintskew_504d_base_v087_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.rolling(504, min_periods=168).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity kurtosis over 252d
def f19mc_f19_mining_capex_intensity_capintkurt_252d_base_v088_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.rolling(252, min_periods=84).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate skew over 252d
def f19mc_f19_mining_capex_intensity_reinvskew_252d_base_v089_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity skew over 252d
def f19mc_f19_mining_capex_intensity_invtrskew_252d_base_v090_signal(ncfi, assets):
    s = _f19_invtrend(ncfi, assets)
    result = s.rolling(252, min_periods=84).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity coefficient of variation over 252d
def f19mc_f19_mining_capex_intensity_capintcv_252d_base_v091_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = _safe_div(_std(s, 252), _mean(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate coefficient of variation over 252d
def f19mc_f19_mining_capex_intensity_reinvcv_252d_base_v092_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = _safe_div(_std(s, 252), _mean(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d EWMA capex intensity
def f19mc_f19_mining_capex_intensity_capintewm_84d_base_v093_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.ewm(span=84, min_periods=28).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EWMA capex intensity
def f19mc_f19_mining_capex_intensity_capintewm_504d_base_v094_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.ewm(span=504, min_periods=168).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment EWMA span 252
def f19mc_f19_mining_capex_intensity_reinvewm_252d_base_v095_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity EWMA span 126
def f19mc_f19_mining_capex_intensity_invtrewm_126d_base_v096_signal(ncfi, assets):
    s = _f19_invtrend(ncfi, assets)
    result = s.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity EWMA span 252
def f19mc_f19_mining_capex_intensity_invtrewm_252d_base_v097_signal(ncfi, assets):
    s = _f19_invtrend(ncfi, assets)
    result = s.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue intensity 504d mean
def f19mc_f19_mining_capex_intensity_caprevsm_504d_base_v098_signal(capex, revenue, assets):
    result = _mean(_safe_div(capex.abs(), revenue), 504) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue intensity z-score over 504d
def f19mc_f19_mining_capex_intensity_zcaprev_504d_base_v099_signal(capex, revenue, assets):
    result = _z(_safe_div(capex.abs(), revenue), 504) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue percentile rank over 252d
def f19mc_f19_mining_capex_intensity_rkcaprev_252d_base_v100_signal(capex, revenue, assets):
    s = _safe_div(capex.abs(), revenue) + _f19_capint(capex, assets) * 0.0
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# replacement intensity z-score over 252d
def f19mc_f19_mining_capex_intensity_zrepl_252d_base_v101_signal(capex, ppnenet, assets):
    result = _z(_safe_div(capex.abs(), ppnenet), 252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# replacement intensity percentile rank over 252d
def f19mc_f19_mining_capex_intensity_rkrepl_252d_base_v102_signal(capex, ppnenet, assets):
    s = _safe_div(capex.abs(), ppnenet) + _f19_capint(capex, assets) * 0.0
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# replacement intensity 504d mean
def f19mc_f19_mining_capex_intensity_replsm_504d_base_v103_signal(capex, ppnenet, assets):
    result = _mean(_safe_div(capex.abs(), ppnenet), 504) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration: 84d diff of capex intensity
def f19mc_f19_mining_capex_intensity_capaccel_84d_base_v104_signal(capex, assets):
    result = _f19_capint(capex, assets).diff(84)
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration: 189d diff of capex intensity
def f19mc_f19_mining_capex_intensity_capaccel_189d_base_v105_signal(capex, assets):
    result = _f19_capint(capex, assets).diff(189)
    return result.replace([np.inf, -np.inf], np.nan)


# capex acceleration: 504d diff of capex intensity
def f19mc_f19_mining_capex_intensity_capaccel_504d_base_v106_signal(capex, assets):
    result = _f19_capint(capex, assets).diff(504)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment acceleration: 126d diff
def f19mc_f19_mining_capex_intensity_reinvaccel_126d_base_v107_signal(capex, depamor):
    result = _f19_reinvest(capex, depamor).diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment acceleration: 252d diff
def f19mc_f19_mining_capex_intensity_reinvaccel_252d_base_v108_signal(capex, depamor):
    result = _f19_reinvest(capex, depamor).diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity short/long ratio (42d/189d mean)
def f19mc_f19_mining_capex_intensity_capratio_42_189_base_v109_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = _safe_div(_mean(s, 42), _mean(s, 189))
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment short/long ratio (63d/252d mean)
def f19mc_f19_mining_capex_intensity_reinvratio_63_252_base_v110_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = _safe_div(_mean(s, 63), _mean(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity trend slope (84d diff of EWMA)
def f19mc_f19_mining_capex_intensity_captrend_84d_base_v111_signal(capex, assets):
    s = _f19_capint(capex, assets).ewm(span=63, min_periods=21).mean()
    result = s.diff(84)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity trend slope (504d diff of EWMA)
def f19mc_f19_mining_capex_intensity_captrend_504d_base_v112_signal(capex, assets):
    s = _f19_capint(capex, assets).ewm(span=126, min_periods=42).mean()
    result = s.diff(504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vs assets-growth divergence (252d)
def f19mc_f19_mining_capex_intensity_assetdiv_252d_base_v113_signal(capex, assets):
    result = _f19_capint(capex, assets) - _z(assets.pct_change(252), 252) * 0.0 + assets.pct_change(252) * 0.0 + _f19_capint(capex, assets).diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment minus replacement (depamor vs ppnenet base spread)
def f19mc_f19_mining_capex_intensity_reinvreplspr_126d_base_v114_signal(capex, depamor, ppnenet):
    s = _f19_reinvest(capex, depamor) - _safe_div(capex.abs(), ppnenet)
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-maintenance proxy z-score over 252d
def f19mc_f19_mining_capex_intensity_zgmproxy_252d_base_v115_signal(capex, depamor, assets):
    s = _f19_capint(capex, assets) - _safe_div(depamor.abs(), assets)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-maintenance proxy 504d mean
def f19mc_f19_mining_capex_intensity_gmproxysm_504d_base_v116_signal(capex, depamor, assets):
    s = _f19_capint(capex, assets) - _safe_div(depamor.abs(), assets)
    result = _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# excess reinvestment 126d (above maintenance)
def f19mc_f19_mining_capex_intensity_exreinv_126d_base_v117_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor) - 1.0, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vol-scaled level over 126d
def f19mc_f19_mining_capex_intensity_capvolscl_126d_base_v118_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = _safe_div(s, _std(s, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment vol-scaled level over 252d
def f19mc_f19_mining_capex_intensity_reinvvolscl_252d_base_v119_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = _safe_div(s, _std(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity vol-scaled over 252d
def f19mc_f19_mining_capex_intensity_invtrvolscl_252d_base_v120_signal(ncfi, assets):
    s = _f19_invtrend(ncfi, assets)
    result = _safe_div(s, _std(s, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity momentum 252d (pct change of smoothed)
def f19mc_f19_mining_capex_intensity_capmom_252d_base_v121_signal(capex, assets):
    s = _mean(_f19_capint(capex, assets), 63)
    result = s.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment momentum 252d
def f19mc_f19_mining_capex_intensity_reinvmom_252d_base_v122_signal(capex, depamor):
    s = _mean(_f19_reinvest(capex, depamor), 63)
    result = s.pct_change(252)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity momentum 126d
def f19mc_f19_mining_capex_intensity_invmom_126d_base_v123_signal(ncfi, assets):
    s = _mean(_f19_invtrend(ncfi, assets), 63)
    result = s.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex double-intensity z-score over 252d
def f19mc_f19_mining_capex_intensity_zcapdbl_252d_base_v124_signal(capex, assets, revenue):
    s = _f19_capint(capex, assets) * _safe_div(capex.abs(), revenue)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex double-intensity percentile rank 252d
def f19mc_f19_mining_capex_intensity_rkcapdbl_252d_base_v125_signal(capex, assets, revenue):
    s = _f19_capint(capex, assets) * _safe_div(capex.abs(), revenue)
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity minus reinvestment-implied intensity (structure spread)
def f19mc_f19_mining_capex_intensity_structspr_126d_base_v126_signal(capex, assets, depamor):
    s = _f19_capint(capex, assets) - _safe_div(depamor.abs(), assets) * _f19_reinvest(capex, depamor)
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue acceleration 126d diff
def f19mc_f19_mining_capex_intensity_caprevaccel_126d_base_v127_signal(capex, revenue, assets):
    s = _safe_div(capex.abs(), revenue) + _f19_capint(capex, assets) * 0.0
    result = s.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex/revenue acceleration 252d diff
def f19mc_f19_mining_capex_intensity_caprevaccel_252d_base_v128_signal(capex, revenue, assets):
    s = _safe_div(capex.abs(), revenue) + _f19_capint(capex, assets) * 0.0
    result = s.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth acceleration (63d growth diffed 126d)
def f19mc_f19_mining_capex_intensity_ppnegaccel_126d_base_v129_signal(ppnenet, capex, assets):
    s = _f19_ppnegrowth(ppnenet, 63)
    result = s.diff(126) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# PP&E growth acceleration 252d
def f19mc_f19_mining_capex_intensity_ppnegaccel_252d_base_v130_signal(ppnenet, capex, assets):
    s = _f19_ppnegrowth(ppnenet, 63)
    result = s.diff(252) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity relative to revenue-scaled vol (intensity / revenue-growth std)
def f19mc_f19_mining_capex_intensity_capgrowthnorm_252d_base_v131_signal(capex, assets, revenue):
    rv = _std(revenue.pct_change(63), 252)
    result = _safe_div(_f19_capint(capex, assets), rv)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate relative to PP&E growth (spend vs realized buildout)
def f19mc_f19_mining_capex_intensity_reinvvsppne_126d_base_v132_signal(capex, depamor, ppnenet, assets):
    s = _f19_reinvest(capex, depamor) - _f19_ppnegrowth(ppnenet, 63)
    result = _mean(s, 126) + _f19_capint(capex, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity 84d mean
def f19mc_f19_mining_capex_intensity_invtrsm_84d_base_v133_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity 189d mean
def f19mc_f19_mining_capex_intensity_invtrsm_189d_base_v134_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity 378d mean
def f19mc_f19_mining_capex_intensity_invtrsm_378d_base_v135_signal(ncfi, assets):
    result = _mean(_f19_invtrend(ncfi, assets), 378)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate 84d mean
def f19mc_f19_mining_capex_intensity_reinvsm_84d_base_v136_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment rate 189d mean
def f19mc_f19_mining_capex_intensity_reinvsm_189d_base_v137_signal(capex, depamor):
    result = _mean(_f19_reinvest(capex, depamor), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity percentile rank over 126d
def f19mc_f19_mining_capex_intensity_rkcapint_126d_base_v138_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment percentile rank over 504d
def f19mc_f19_mining_capex_intensity_rkreinv_504d_base_v139_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity percentile rank over 252d
def f19mc_f19_mining_capex_intensity_rkinvtr_252d_base_v140_signal(ncfi, assets):
    s = _f19_invtrend(ncfi, assets)
    result = s.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity surprise 504d
def f19mc_f19_mining_capex_intensity_capsurp_504d_base_v141_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s - _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment surprise 126d
def f19mc_f19_mining_capex_intensity_reinvsurp_126d_base_v142_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net investing intensity surprise 252d
def f19mc_f19_mining_capex_intensity_invsurp_252d_base_v143_signal(ncfi, assets):
    s = _f19_invtrend(ncfi, assets)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity ewm minus sma spread (intensity MACD-like)
def f19mc_f19_mining_capex_intensity_capmacd_base_v144_signal(capex, assets):
    s = _f19_capint(capex, assets)
    result = s.ewm(span=63, min_periods=21).mean() - s.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# reinvestment ewm minus sma spread
def f19mc_f19_mining_capex_intensity_reinvmacd_base_v145_signal(capex, depamor):
    s = _f19_reinvest(capex, depamor)
    result = s.ewm(span=63, min_periods=21).mean() - s.ewm(span=189, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity over revenue intensity ratio (asset vs sales scaling)
def f19mc_f19_mining_capex_intensity_intratio_126d_base_v146_signal(capex, assets, revenue):
    s = _safe_div(_f19_capint(capex, assets), _safe_div(capex.abs(), revenue))
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity scaled by reinvestment (combined spend pressure) 252d mean
def f19mc_f19_mining_capex_intensity_combpress_252d_base_v147_signal(capex, assets, depamor):
    s = _f19_capint(capex, assets) * _f19_reinvest(capex, depamor)
    result = _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity z-score scaled by net investing intensity z-score (alignment)
def f19mc_f19_mining_capex_intensity_align_252d_base_v148_signal(capex, assets, ncfi):
    a = _z(_f19_capint(capex, assets), 252)
    b = _z(_f19_invtrend(ncfi, assets), 252)
    result = a * (-b)
    return result.replace([np.inf, -np.inf], np.nan)


# long-horizon capex buildout: 504d PP&E growth weighted by capex intensity
def f19mc_f19_mining_capex_intensity_buildtr_504d_base_v149_signal(ppnenet, capex, assets):
    result = _f19_ppnegrowth(ppnenet, 504) * _f19_capint(capex, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# blended capex-intensity composite (capint + reinvest + replacement + invtrend)
def f19mc_f19_mining_capex_intensity_blend_252d_base_v150_signal(capex, assets, depamor, ncfi):
    a = _z(_f19_capint(capex, assets), 252)
    b = _z(_f19_reinvest(capex, depamor), 252)
    c = _z(_f19_invtrend(ncfi, assets), 252)
    result = (a + b - c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19mc_f19_mining_capex_intensity_capintsm_84d_base_v076_signal,
    f19mc_f19_mining_capex_intensity_capintsm_189d_base_v077_signal,
    f19mc_f19_mining_capex_intensity_capintsm_378d_base_v078_signal,
    f19mc_f19_mining_capex_intensity_ppneg_42d_base_v079_signal,
    f19mc_f19_mining_capex_intensity_ppneg_84d_base_v080_signal,
    f19mc_f19_mining_capex_intensity_ppneg_189d_base_v081_signal,
    f19mc_f19_mining_capex_intensity_ppneg_378d_base_v082_signal,
    f19mc_f19_mining_capex_intensity_ppnegsm_63d_base_v083_signal,
    f19mc_f19_mining_capex_intensity_ppnegsm_126d_base_v084_signal,
    f19mc_f19_mining_capex_intensity_ppnegewm_126d_base_v085_signal,
    f19mc_f19_mining_capex_intensity_capintskew_252d_base_v086_signal,
    f19mc_f19_mining_capex_intensity_capintskew_504d_base_v087_signal,
    f19mc_f19_mining_capex_intensity_capintkurt_252d_base_v088_signal,
    f19mc_f19_mining_capex_intensity_reinvskew_252d_base_v089_signal,
    f19mc_f19_mining_capex_intensity_invtrskew_252d_base_v090_signal,
    f19mc_f19_mining_capex_intensity_capintcv_252d_base_v091_signal,
    f19mc_f19_mining_capex_intensity_reinvcv_252d_base_v092_signal,
    f19mc_f19_mining_capex_intensity_capintewm_84d_base_v093_signal,
    f19mc_f19_mining_capex_intensity_capintewm_504d_base_v094_signal,
    f19mc_f19_mining_capex_intensity_reinvewm_252d_base_v095_signal,
    f19mc_f19_mining_capex_intensity_invtrewm_126d_base_v096_signal,
    f19mc_f19_mining_capex_intensity_invtrewm_252d_base_v097_signal,
    f19mc_f19_mining_capex_intensity_caprevsm_504d_base_v098_signal,
    f19mc_f19_mining_capex_intensity_zcaprev_504d_base_v099_signal,
    f19mc_f19_mining_capex_intensity_rkcaprev_252d_base_v100_signal,
    f19mc_f19_mining_capex_intensity_zrepl_252d_base_v101_signal,
    f19mc_f19_mining_capex_intensity_rkrepl_252d_base_v102_signal,
    f19mc_f19_mining_capex_intensity_replsm_504d_base_v103_signal,
    f19mc_f19_mining_capex_intensity_capaccel_84d_base_v104_signal,
    f19mc_f19_mining_capex_intensity_capaccel_189d_base_v105_signal,
    f19mc_f19_mining_capex_intensity_capaccel_504d_base_v106_signal,
    f19mc_f19_mining_capex_intensity_reinvaccel_126d_base_v107_signal,
    f19mc_f19_mining_capex_intensity_reinvaccel_252d_base_v108_signal,
    f19mc_f19_mining_capex_intensity_capratio_42_189_base_v109_signal,
    f19mc_f19_mining_capex_intensity_reinvratio_63_252_base_v110_signal,
    f19mc_f19_mining_capex_intensity_captrend_84d_base_v111_signal,
    f19mc_f19_mining_capex_intensity_captrend_504d_base_v112_signal,
    f19mc_f19_mining_capex_intensity_assetdiv_252d_base_v113_signal,
    f19mc_f19_mining_capex_intensity_reinvreplspr_126d_base_v114_signal,
    f19mc_f19_mining_capex_intensity_zgmproxy_252d_base_v115_signal,
    f19mc_f19_mining_capex_intensity_gmproxysm_504d_base_v116_signal,
    f19mc_f19_mining_capex_intensity_exreinv_126d_base_v117_signal,
    f19mc_f19_mining_capex_intensity_capvolscl_126d_base_v118_signal,
    f19mc_f19_mining_capex_intensity_reinvvolscl_252d_base_v119_signal,
    f19mc_f19_mining_capex_intensity_invtrvolscl_252d_base_v120_signal,
    f19mc_f19_mining_capex_intensity_capmom_252d_base_v121_signal,
    f19mc_f19_mining_capex_intensity_reinvmom_252d_base_v122_signal,
    f19mc_f19_mining_capex_intensity_invmom_126d_base_v123_signal,
    f19mc_f19_mining_capex_intensity_zcapdbl_252d_base_v124_signal,
    f19mc_f19_mining_capex_intensity_rkcapdbl_252d_base_v125_signal,
    f19mc_f19_mining_capex_intensity_structspr_126d_base_v126_signal,
    f19mc_f19_mining_capex_intensity_caprevaccel_126d_base_v127_signal,
    f19mc_f19_mining_capex_intensity_caprevaccel_252d_base_v128_signal,
    f19mc_f19_mining_capex_intensity_ppnegaccel_126d_base_v129_signal,
    f19mc_f19_mining_capex_intensity_ppnegaccel_252d_base_v130_signal,
    f19mc_f19_mining_capex_intensity_capgrowthnorm_252d_base_v131_signal,
    f19mc_f19_mining_capex_intensity_reinvvsppne_126d_base_v132_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_84d_base_v133_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_189d_base_v134_signal,
    f19mc_f19_mining_capex_intensity_invtrsm_378d_base_v135_signal,
    f19mc_f19_mining_capex_intensity_reinvsm_84d_base_v136_signal,
    f19mc_f19_mining_capex_intensity_reinvsm_189d_base_v137_signal,
    f19mc_f19_mining_capex_intensity_rkcapint_126d_base_v138_signal,
    f19mc_f19_mining_capex_intensity_rkreinv_504d_base_v139_signal,
    f19mc_f19_mining_capex_intensity_rkinvtr_252d_base_v140_signal,
    f19mc_f19_mining_capex_intensity_capsurp_504d_base_v141_signal,
    f19mc_f19_mining_capex_intensity_reinvsurp_126d_base_v142_signal,
    f19mc_f19_mining_capex_intensity_invsurp_252d_base_v143_signal,
    f19mc_f19_mining_capex_intensity_capmacd_base_v144_signal,
    f19mc_f19_mining_capex_intensity_reinvmacd_base_v145_signal,
    f19mc_f19_mining_capex_intensity_intratio_126d_base_v146_signal,
    f19mc_f19_mining_capex_intensity_combpress_252d_base_v147_signal,
    f19mc_f19_mining_capex_intensity_align_252d_base_v148_signal,
    f19mc_f19_mining_capex_intensity_buildtr_504d_base_v149_signal,
    f19mc_f19_mining_capex_intensity_blend_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_MINING_CAPEX_INTENSITY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f19_mining_capex_intensity_base_076_150_claude: {n_features} features pass")
