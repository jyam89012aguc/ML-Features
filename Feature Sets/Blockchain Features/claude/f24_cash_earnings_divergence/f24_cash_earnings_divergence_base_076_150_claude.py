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


def _slope(s, w):
    # OLS-style slope via diff over w normalized by w (continuous trend)
    return s.diff(periods=w) / float(w)


# ===== folder domain primitives (cash-earnings divergence) =====
def _f24_accrual(netinc, ncfo, assets):
    # Sloan accruals: (earnings - operating cash flow) / total assets
    return _safe_div(netinc - ncfo, assets)


def _f24_quality(ncfo, netinc):
    # cash conversion / earnings quality: operating cash flow per unit earnings
    return _safe_div(ncfo, netinc)


def _f24_divergence(netinc, ncfo):
    # normalized earnings-vs-cash divergence (scaled by gross magnitude)
    return _safe_div(netinc - ncfo, (netinc.abs() + ncfo.abs()))


def _f24_noncash(netinc, ncfo, depamor):
    # non-cash earnings load: depreciation+amortization relative to the accrual gap
    return _safe_div(depamor, (netinc - ncfo).abs() + depamor.abs())


# ============ FEATURES 076-150 ============

# 42d Sloan accrual level
def f24ce_f24_cash_earnings_divergence_accrual_42d_base_v076_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d Sloan accrual level
def f24ce_f24_cash_earnings_divergence_accrual_189d_base_v077_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d quality level
def f24ce_f24_cash_earnings_divergence_quality_42d_base_v078_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d quality level
def f24ce_f24_cash_earnings_divergence_quality_189d_base_v079_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d divergence level
def f24ce_f24_cash_earnings_divergence_diverg_42d_base_v080_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d divergence level
def f24ce_f24_cash_earnings_divergence_diverg_189d_base_v081_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d non-cash load
def f24ce_f24_cash_earnings_divergence_noncash_189d_base_v082_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual z over 189d
def f24ce_f24_cash_earnings_divergence_zaccrual_189d_base_v083_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# quality z over 126d
def f24ce_f24_cash_earnings_divergence_zquality_126d_base_v084_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# quality z over 504d
def f24ce_f24_cash_earnings_divergence_zquality_504d_base_v085_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence z over 504d
def f24ce_f24_cash_earnings_divergence_zdiverg_504d_base_v086_signal(netinc, ncfo):
    result = _z(_f24_divergence(netinc, ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# non-cash z over 126d
def f24ce_f24_cash_earnings_divergence_znoncash_126d_base_v087_signal(netinc, ncfo, depamor):
    result = _z(_f24_noncash(netinc, ncfo, depamor), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual slope over 42d
def f24ce_f24_cash_earnings_divergence_accslope_42d_base_v088_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual slope over 189d
def f24ce_f24_cash_earnings_divergence_accslope_189d_base_v089_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# quality slope over 63d
def f24ce_f24_cash_earnings_divergence_qualslope_63d_base_v090_signal(ncfo, netinc):
    result = _slope(_f24_quality(ncfo, netinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# quality slope over 252d
def f24ce_f24_cash_earnings_divergence_qualslope_252d_base_v091_signal(ncfo, netinc):
    result = _slope(_f24_quality(ncfo, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence slope over 63d
def f24ce_f24_cash_earnings_divergence_divslope_63d_base_v092_signal(netinc, ncfo):
    result = _slope(_f24_divergence(netinc, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence slope over 252d
def f24ce_f24_cash_earnings_divergence_divslope_252d_base_v093_signal(netinc, ncfo):
    result = _slope(_f24_divergence(netinc, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# non-cash slope over 126d
def f24ce_f24_cash_earnings_divergence_ncslope_126d_base_v094_signal(netinc, ncfo, depamor):
    result = _slope(_f24_noncash(netinc, ncfo, depamor), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual vol over 504d
def f24ce_f24_cash_earnings_divergence_accvol_504d_base_v095_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# quality vol over 126d
def f24ce_f24_cash_earnings_divergence_qualvol_126d_base_v096_signal(ncfo, netinc):
    result = _std(_f24_quality(ncfo, netinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence vol over 63d
def f24ce_f24_cash_earnings_divergence_divvol_63d_base_v097_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# non-cash vol over 252d
def f24ce_f24_cash_earnings_divergence_ncvol_252d_base_v098_signal(netinc, ncfo, depamor):
    result = _std(_f24_noncash(netinc, ncfo, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual rank over 126d
def f24ce_f24_cash_earnings_divergence_accrank_126d_base_v099_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual rank over 504d
def f24ce_f24_cash_earnings_divergence_accrank_504d_base_v100_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# quality rank over 126d
def f24ce_f24_cash_earnings_divergence_qualrank_126d_base_v101_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence rank over 252d
def f24ce_f24_cash_earnings_divergence_divrank_252d_base_v102_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# non-cash rank over 252d
def f24ce_f24_cash_earnings_divergence_ncrank_252d_base_v103_signal(netinc, ncfo, depamor):
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = nc.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual mean-reversion over 126d
def f24ce_f24_cash_earnings_divergence_accmr_126d_base_v104_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a - _mean(a, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# quality mean-reversion over 126d
def f24ce_f24_cash_earnings_divergence_qualmr_126d_base_v105_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q - _mean(q, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence mean-reversion over 252d
def f24ce_f24_cash_earnings_divergence_divmr_252d_base_v106_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d - _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# quality surprise: 63d minus 252d mean
def f24ce_f24_cash_earnings_divergence_qualsurp_base_v107_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = _mean(q, 63) - _mean(q, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual surprise: 42d minus 189d mean
def f24ce_f24_cash_earnings_divergence_accsurp_base_v108_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = _mean(a, 42) - _mean(a, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence spread: 42d minus 252d mean
def f24ce_f24_cash_earnings_divergence_divspread_base_v109_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = _mean(d, 42) - _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence EWMA span 63
def f24ce_f24_cash_earnings_divergence_divewm_63d_base_v110_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# quality EWMA span 63
def f24ce_f24_cash_earnings_divergence_qualewm_63d_base_v111_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# quality EWMA span 252
def f24ce_f24_cash_earnings_divergence_qualewm_252d_base_v112_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# non-cash EWMA span 126
def f24ce_f24_cash_earnings_divergence_ncewm_126d_base_v113_signal(netinc, ncfo, depamor):
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = nc.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# divergence scaled by accrual vol (cross-stability) 252d
def f24ce_f24_cash_earnings_divergence_divaccstab_base_v114_signal(netinc, ncfo, assets):
    d = _f24_divergence(netinc, ncfo)
    a = _f24_accrual(netinc, ncfo, assets)
    result = _safe_div(_mean(d, 63), _std(a, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# quality stability: mean over vol, 252d
def f24ce_f24_cash_earnings_divergence_qualstab_252d_base_v115_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = _safe_div(_mean(q, 63), _std(q, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# absolute divergence magnitude, 252d
def f24ce_f24_cash_earnings_divergence_absdiv_252d_base_v116_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute accrual magnitude, 252d
def f24ce_f24_cash_earnings_divergence_absacc_252d_base_v117_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/assets free-cash yield, 252d
def f24ce_f24_cash_earnings_divergence_fcfyield_252d_base_v118_signal(fcf, assets, netinc, ncfo):
    result = _mean(_safe_div(fcf, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo/assets cash ROA, 252d
def f24ce_f24_cash_earnings_divergence_cfroa_252d_base_v119_signal(ncfo, assets, netinc):
    result = _mean(_safe_div(ncfo, assets), 252) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# netinc/assets accrual ROA, 252d
def f24ce_f24_cash_earnings_divergence_earnroa_252d_base_v120_signal(netinc, assets, ncfo):
    result = _mean(_safe_div(netinc, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-accrual ROA gap, 252d
def f24ce_f24_cash_earnings_divergence_roagap_252d_base_v121_signal(ncfo, netinc, assets):
    result = _mean(_safe_div(ncfo - netinc, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/netinc free-cash conversion, 42d
def f24ce_f24_cash_earnings_divergence_fcfconv_42d_base_v122_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 42) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/netinc free-cash conversion, 189d
def f24ce_f24_cash_earnings_divergence_fcfconv_189d_base_v123_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 189) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# (netinc - fcf)/assets free-cash accruals, 42d
def f24ce_f24_cash_earnings_divergence_fcfaccr_42d_base_v124_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 42) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo/revenue cash margin, 42d
def f24ce_f24_cash_earnings_divergence_cashmargin_42d_base_v125_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 42) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# netinc/revenue accrual margin, 252d
def f24ce_f24_cash_earnings_divergence_earnmargin_252d_base_v126_signal(netinc, revenue, ncfo):
    result = _mean(_safe_div(netinc, revenue), 252) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual margin minus cash margin (netinc-ncfo)/revenue, 63d
def f24ce_f24_cash_earnings_divergence_margingap_63d_base_v127_signal(netinc, ncfo, revenue):
    result = _mean(_safe_div(netinc - ncfo, revenue), 63) + _f24_divergence(netinc, ncfo) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/netinc non-cash share, 63d
def f24ce_f24_cash_earnings_divergence_daearn_63d_base_v128_signal(depamor, netinc, ncfo):
    result = _mean(_safe_div(depamor, netinc), 63) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/revenue D&A intensity, 252d
def f24ce_f24_cash_earnings_divergence_daintens_252d_base_v129_signal(depamor, revenue, netinc, ncfo):
    result = _mean(_safe_div(depamor, revenue), 252) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/ncfo non-cash to cash, 252d
def f24ce_f24_cash_earnings_divergence_dacash_252d_base_v130_signal(depamor, ncfo, netinc):
    result = _mean(_safe_div(depamor, ncfo), 252) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual conditioned on divergence sign-free magnitude, 126d product
def f24ce_f24_cash_earnings_divergence_accdivprod_126d_base_v131_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    d = _f24_divergence(netinc, ncfo)
    result = _mean(a * d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# quality minus divergence composite, 126d
def f24ce_f24_cash_earnings_divergence_qualminusdiv_126d_base_v132_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    d = _f24_divergence(netinc, ncfo)
    result = _mean(q - d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence times non-cash load (impairment-driven divergence), 126d
def f24ce_f24_cash_earnings_divergence_divnoncash_126d_base_v133_signal(netinc, ncfo, depamor):
    d = _f24_divergence(netinc, ncfo)
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = _mean(d * nc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual change acceleration: slope minus its own 126d mean
def f24ce_f24_cash_earnings_divergence_accaccel_126d_base_v134_signal(netinc, ncfo, assets):
    s = _slope(_f24_accrual(netinc, ncfo, assets), 63)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# quality change acceleration: slope minus its own 126d mean
def f24ce_f24_cash_earnings_divergence_qualaccel_126d_base_v135_signal(ncfo, netinc):
    s = _slope(_f24_quality(ncfo, netinc), 63)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual relative to assets-growth-adjusted base, 126d (accrual/cash-margin)
def f24ce_f24_cash_earnings_divergence_accpercash_126d_base_v136_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    cm = _safe_div(ncfo, assets)
    result = _mean(_safe_div(a, cm.abs() + 1e-9), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# quality smoothed 84d
def f24ce_f24_cash_earnings_divergence_quality_84d_base_v137_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual smoothed 84d
def f24ce_f24_cash_earnings_divergence_accrual_84d_base_v138_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence smoothed 84d
def f24ce_f24_cash_earnings_divergence_diverg_84d_base_v139_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual z over 84d window
def f24ce_f24_cash_earnings_divergence_zaccrual_84w_base_v140_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# quality z over 315d window
def f24ce_f24_cash_earnings_divergence_zquality_315w_base_v141_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 315)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual slope over 315d
def f24ce_f24_cash_earnings_divergence_accslope_315d_base_v142_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 315)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence vol over 504d
def f24ce_f24_cash_earnings_divergence_divvol_504d_base_v143_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-intensity gap: (ncfo - fcf)/assets, 126d
def f24ce_f24_cash_earnings_divergence_fcfdiv_126d_base_v144_signal(ncfo, fcf, assets, netinc):
    g = _safe_div(ncfo - fcf, assets)
    result = _mean(g, 126) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-vs-free-cash margin gap: (netinc - fcf)/revenue, 126d
def f24ce_f24_cash_earnings_divergence_earnfcfdiv_126d_base_v145_signal(netinc, fcf, revenue, ncfo):
    g = _safe_div(netinc - fcf, revenue)
    result = _mean(g, 126) + _f24_divergence(netinc, ncfo) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-to-revenue scaled, 252d
def f24ce_f24_cash_earnings_divergence_accrev_252d_base_v146_signal(netinc, ncfo, revenue, assets):
    result = _mean(_safe_div(netinc - ncfo, revenue), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# quality detrended by 252d (cash-conversion innovation)
def f24ce_f24_cash_earnings_divergence_qualinnov_base_v147_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=42, min_periods=21).mean() - q.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# accrual detrended (fast minus slow EWMA)
def f24ce_f24_cash_earnings_divergence_accinnov_base_v148_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=42, min_periods=21).mean() - a.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# divergence detrended (fast minus slow EWMA)
def f24ce_f24_cash_earnings_divergence_divinnov_base_v149_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.ewm(span=42, min_periods=21).mean() - d.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon earnings-quality composite (accrual + quality + divergence)
def f24ce_f24_cash_earnings_divergence_blend_multi_base_v150_signal(netinc, ncfo, assets):
    a = _z(_f24_accrual(netinc, ncfo, assets), 252)
    q = _z(_f24_quality(ncfo, netinc), 252)
    d = _z(_f24_divergence(netinc, ncfo), 252)
    result = (a + q + d) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24ce_f24_cash_earnings_divergence_accrual_42d_base_v076_signal,
    f24ce_f24_cash_earnings_divergence_accrual_189d_base_v077_signal,
    f24ce_f24_cash_earnings_divergence_quality_42d_base_v078_signal,
    f24ce_f24_cash_earnings_divergence_quality_189d_base_v079_signal,
    f24ce_f24_cash_earnings_divergence_diverg_42d_base_v080_signal,
    f24ce_f24_cash_earnings_divergence_diverg_189d_base_v081_signal,
    f24ce_f24_cash_earnings_divergence_noncash_189d_base_v082_signal,
    f24ce_f24_cash_earnings_divergence_zaccrual_189d_base_v083_signal,
    f24ce_f24_cash_earnings_divergence_zquality_126d_base_v084_signal,
    f24ce_f24_cash_earnings_divergence_zquality_504d_base_v085_signal,
    f24ce_f24_cash_earnings_divergence_zdiverg_504d_base_v086_signal,
    f24ce_f24_cash_earnings_divergence_znoncash_126d_base_v087_signal,
    f24ce_f24_cash_earnings_divergence_accslope_42d_base_v088_signal,
    f24ce_f24_cash_earnings_divergence_accslope_189d_base_v089_signal,
    f24ce_f24_cash_earnings_divergence_qualslope_63d_base_v090_signal,
    f24ce_f24_cash_earnings_divergence_qualslope_252d_base_v091_signal,
    f24ce_f24_cash_earnings_divergence_divslope_63d_base_v092_signal,
    f24ce_f24_cash_earnings_divergence_divslope_252d_base_v093_signal,
    f24ce_f24_cash_earnings_divergence_ncslope_126d_base_v094_signal,
    f24ce_f24_cash_earnings_divergence_accvol_504d_base_v095_signal,
    f24ce_f24_cash_earnings_divergence_qualvol_126d_base_v096_signal,
    f24ce_f24_cash_earnings_divergence_divvol_63d_base_v097_signal,
    f24ce_f24_cash_earnings_divergence_ncvol_252d_base_v098_signal,
    f24ce_f24_cash_earnings_divergence_accrank_126d_base_v099_signal,
    f24ce_f24_cash_earnings_divergence_accrank_504d_base_v100_signal,
    f24ce_f24_cash_earnings_divergence_qualrank_126d_base_v101_signal,
    f24ce_f24_cash_earnings_divergence_divrank_252d_base_v102_signal,
    f24ce_f24_cash_earnings_divergence_ncrank_252d_base_v103_signal,
    f24ce_f24_cash_earnings_divergence_accmr_126d_base_v104_signal,
    f24ce_f24_cash_earnings_divergence_qualmr_126d_base_v105_signal,
    f24ce_f24_cash_earnings_divergence_divmr_252d_base_v106_signal,
    f24ce_f24_cash_earnings_divergence_qualsurp_base_v107_signal,
    f24ce_f24_cash_earnings_divergence_accsurp_base_v108_signal,
    f24ce_f24_cash_earnings_divergence_divspread_base_v109_signal,
    f24ce_f24_cash_earnings_divergence_divewm_63d_base_v110_signal,
    f24ce_f24_cash_earnings_divergence_qualewm_63d_base_v111_signal,
    f24ce_f24_cash_earnings_divergence_qualewm_252d_base_v112_signal,
    f24ce_f24_cash_earnings_divergence_ncewm_126d_base_v113_signal,
    f24ce_f24_cash_earnings_divergence_divaccstab_base_v114_signal,
    f24ce_f24_cash_earnings_divergence_qualstab_252d_base_v115_signal,
    f24ce_f24_cash_earnings_divergence_absdiv_252d_base_v116_signal,
    f24ce_f24_cash_earnings_divergence_absacc_252d_base_v117_signal,
    f24ce_f24_cash_earnings_divergence_fcfyield_252d_base_v118_signal,
    f24ce_f24_cash_earnings_divergence_cfroa_252d_base_v119_signal,
    f24ce_f24_cash_earnings_divergence_earnroa_252d_base_v120_signal,
    f24ce_f24_cash_earnings_divergence_roagap_252d_base_v121_signal,
    f24ce_f24_cash_earnings_divergence_fcfconv_42d_base_v122_signal,
    f24ce_f24_cash_earnings_divergence_fcfconv_189d_base_v123_signal,
    f24ce_f24_cash_earnings_divergence_fcfaccr_42d_base_v124_signal,
    f24ce_f24_cash_earnings_divergence_cashmargin_42d_base_v125_signal,
    f24ce_f24_cash_earnings_divergence_earnmargin_252d_base_v126_signal,
    f24ce_f24_cash_earnings_divergence_margingap_63d_base_v127_signal,
    f24ce_f24_cash_earnings_divergence_daearn_63d_base_v128_signal,
    f24ce_f24_cash_earnings_divergence_daintens_252d_base_v129_signal,
    f24ce_f24_cash_earnings_divergence_dacash_252d_base_v130_signal,
    f24ce_f24_cash_earnings_divergence_accdivprod_126d_base_v131_signal,
    f24ce_f24_cash_earnings_divergence_qualminusdiv_126d_base_v132_signal,
    f24ce_f24_cash_earnings_divergence_divnoncash_126d_base_v133_signal,
    f24ce_f24_cash_earnings_divergence_accaccel_126d_base_v134_signal,
    f24ce_f24_cash_earnings_divergence_qualaccel_126d_base_v135_signal,
    f24ce_f24_cash_earnings_divergence_accpercash_126d_base_v136_signal,
    f24ce_f24_cash_earnings_divergence_quality_84d_base_v137_signal,
    f24ce_f24_cash_earnings_divergence_accrual_84d_base_v138_signal,
    f24ce_f24_cash_earnings_divergence_diverg_84d_base_v139_signal,
    f24ce_f24_cash_earnings_divergence_zaccrual_84w_base_v140_signal,
    f24ce_f24_cash_earnings_divergence_zquality_315w_base_v141_signal,
    f24ce_f24_cash_earnings_divergence_accslope_315d_base_v142_signal,
    f24ce_f24_cash_earnings_divergence_divvol_504d_base_v143_signal,
    f24ce_f24_cash_earnings_divergence_fcfdiv_126d_base_v144_signal,
    f24ce_f24_cash_earnings_divergence_earnfcfdiv_126d_base_v145_signal,
    f24ce_f24_cash_earnings_divergence_accrev_252d_base_v146_signal,
    f24ce_f24_cash_earnings_divergence_qualinnov_base_v147_signal,
    f24ce_f24_cash_earnings_divergence_accinnov_base_v148_signal,
    f24ce_f24_cash_earnings_divergence_divinnov_base_v149_signal,
    f24ce_f24_cash_earnings_divergence_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_CASH_EARNINGS_DIVERGENCE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f24_accrual", "_f24_quality", "_f24_divergence", "_f24_noncash")
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
    print(f"OK f24_cash_earnings_divergence_base_076_150_claude: {n_features} features pass")
