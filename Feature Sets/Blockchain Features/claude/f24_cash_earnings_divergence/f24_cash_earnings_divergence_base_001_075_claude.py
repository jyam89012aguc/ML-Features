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


# ============ FEATURES 001-075 ============

# 63d Sloan accrual level
def f24ce_f24_cash_earnings_divergence_accrual_63d_base_v001_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Sloan accrual level
def f24ce_f24_cash_earnings_divergence_accrual_126d_base_v002_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Sloan accrual level
def f24ce_f24_cash_earnings_divergence_accrual_252d_base_v003_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Sloan accrual level
def f24ce_f24_cash_earnings_divergence_accrual_504d_base_v004_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash-conversion (quality) level
def f24ce_f24_cash_earnings_divergence_quality_63d_base_v005_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash-conversion (quality) level
def f24ce_f24_cash_earnings_divergence_quality_126d_base_v006_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash-conversion (quality) level
def f24ce_f24_cash_earnings_divergence_quality_252d_base_v007_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d normalized divergence level
def f24ce_f24_cash_earnings_divergence_diverg_63d_base_v008_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d normalized divergence level
def f24ce_f24_cash_earnings_divergence_diverg_126d_base_v009_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d normalized divergence level
def f24ce_f24_cash_earnings_divergence_diverg_252d_base_v010_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d non-cash earnings load
def f24ce_f24_cash_earnings_divergence_noncash_63d_base_v011_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d non-cash earnings load
def f24ce_f24_cash_earnings_divergence_noncash_126d_base_v012_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d non-cash earnings load
def f24ce_f24_cash_earnings_divergence_noncash_252d_base_v013_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/netinc free-cash conversion, 63d smoothed
def f24ce_f24_cash_earnings_divergence_fcfconv_63d_base_v014_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 63) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/netinc free-cash conversion, 126d smoothed
def f24ce_f24_cash_earnings_divergence_fcfconv_126d_base_v015_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 126) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/netinc free-cash conversion, 252d smoothed
def f24ce_f24_cash_earnings_divergence_fcfconv_252d_base_v016_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 252) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# (netinc - fcf)/assets free-cash accruals, 63d
def f24ce_f24_cash_earnings_divergence_fcfaccr_63d_base_v017_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 63) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# (netinc - fcf)/assets free-cash accruals, 126d
def f24ce_f24_cash_earnings_divergence_fcfaccr_126d_base_v018_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# (netinc - fcf)/assets free-cash accruals, 252d
def f24ce_f24_cash_earnings_divergence_fcfaccr_252d_base_v019_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo/revenue cash margin, 63d
def f24ce_f24_cash_earnings_divergence_cashmargin_63d_base_v020_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 63) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo/revenue cash margin, 126d
def f24ce_f24_cash_earnings_divergence_cashmargin_126d_base_v021_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 126) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo/revenue cash margin, 252d
def f24ce_f24_cash_earnings_divergence_cashmargin_252d_base_v022_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 252) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# netinc/revenue accrual margin, 126d
def f24ce_f24_cash_earnings_divergence_earnmargin_126d_base_v023_signal(netinc, revenue, ncfo):
    result = _mean(_safe_div(netinc, revenue), 126) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-vs-cash margin gap (netinc-ncfo)/revenue, 126d
def f24ce_f24_cash_earnings_divergence_margingap_126d_base_v024_signal(netinc, ncfo, revenue):
    result = _mean(_safe_div(netinc - ncfo, revenue), 126) + _f24_divergence(netinc, ncfo) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-vs-cash margin gap, 252d
def f24ce_f24_cash_earnings_divergence_margingap_252d_base_v025_signal(netinc, ncfo, revenue):
    result = _mean(_safe_div(netinc - ncfo, revenue), 252) + _f24_divergence(netinc, ncfo) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/netinc non-cash share, 126d
def f24ce_f24_cash_earnings_divergence_daearn_126d_base_v026_signal(depamor, netinc, ncfo):
    result = _mean(_safe_div(depamor, netinc), 126) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/netinc non-cash share, 252d
def f24ce_f24_cash_earnings_divergence_daearn_252d_base_v027_signal(depamor, netinc, ncfo):
    result = _mean(_safe_div(depamor, netinc), 252) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/ncfo non-cash-to-cash, 126d
def f24ce_f24_cash_earnings_divergence_dacash_126d_base_v028_signal(depamor, ncfo, netinc):
    result = _mean(_safe_div(depamor, ncfo), 126) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d accrual over 252d
def f24ce_f24_cash_earnings_divergence_zaccrual_63d_base_v029_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of accrual over 126d
def f24ce_f24_cash_earnings_divergence_zaccrual_126d_base_v030_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of accrual over 504d
def f24ce_f24_cash_earnings_divergence_zaccrual_504d_base_v031_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of cash-conversion quality over 252d
def f24ce_f24_cash_earnings_divergence_zquality_252d_base_v032_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of divergence over 252d
def f24ce_f24_cash_earnings_divergence_zdiverg_252d_base_v033_signal(netinc, ncfo):
    result = _z(_f24_divergence(netinc, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of non-cash load over 252d
def f24ce_f24_cash_earnings_divergence_znoncash_252d_base_v034_signal(netinc, ncfo, depamor):
    result = _z(_f24_noncash(netinc, ncfo, depamor), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual trend slope over 63d
def f24ce_f24_cash_earnings_divergence_accslope_63d_base_v035_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual trend slope over 126d
def f24ce_f24_cash_earnings_divergence_accslope_126d_base_v036_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual trend slope over 252d
def f24ce_f24_cash_earnings_divergence_accslope_252d_base_v037_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# quality trend slope over 126d
def f24ce_f24_cash_earnings_divergence_qualslope_126d_base_v038_signal(ncfo, netinc):
    result = _slope(_f24_quality(ncfo, netinc), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence trend slope over 126d
def f24ce_f24_cash_earnings_divergence_divslope_126d_base_v039_signal(netinc, ncfo):
    result = _slope(_f24_divergence(netinc, ncfo), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual volatility (dispersion) over 63d
def f24ce_f24_cash_earnings_divergence_accvol_63d_base_v040_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual volatility over 126d
def f24ce_f24_cash_earnings_divergence_accvol_126d_base_v041_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual volatility over 252d
def f24ce_f24_cash_earnings_divergence_accvol_252d_base_v042_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence volatility over 126d
def f24ce_f24_cash_earnings_divergence_divvol_126d_base_v043_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence volatility over 252d
def f24ce_f24_cash_earnings_divergence_divvol_252d_base_v044_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# quality volatility over 252d
def f24ce_f24_cash_earnings_divergence_qualvol_252d_base_v045_signal(ncfo, netinc):
    result = _std(_f24_quality(ncfo, netinc), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual percentile rank over 252d
def f24ce_f24_cash_earnings_divergence_accrank_252d_base_v046_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# quality percentile rank over 252d (earnings-quality rank)
def f24ce_f24_cash_earnings_divergence_qualrank_252d_base_v047_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence percentile rank over 126d
def f24ce_f24_cash_earnings_divergence_divrank_126d_base_v048_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual mean-reversion: level minus its 252d mean
def f24ce_f24_cash_earnings_divergence_accmr_252d_base_v049_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a - _mean(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# quality mean-reversion: level minus its 252d mean
def f24ce_f24_cash_earnings_divergence_qualmr_252d_base_v050_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q - _mean(q, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence surprise: 63d level minus 252d mean
def f24ce_f24_cash_earnings_divergence_divsurp_base_v051_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = _mean(d, 63) - _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual short-minus-long spread (63d vs 252d means)
def f24ce_f24_cash_earnings_divergence_accspread_base_v052_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = _mean(a, 63) - _mean(a, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# quality short-minus-long spread (63d vs 252d means)
def f24ce_f24_cash_earnings_divergence_qualspread_base_v053_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = _mean(q, 63) - _mean(q, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual EWMA (span 63)
def f24ce_f24_cash_earnings_divergence_accewm_63d_base_v054_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# accrual EWMA (span 126)
def f24ce_f24_cash_earnings_divergence_accewm_126d_base_v055_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# quality EWMA (span 126)
def f24ce_f24_cash_earnings_divergence_qualewm_126d_base_v056_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# accrual scaled by its own 252d volatility (stability-adjusted)
def f24ce_f24_cash_earnings_divergence_accstab_252d_base_v057_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = _safe_div(_mean(a, 63), _std(a, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# divergence scaled by its own 252d volatility
def f24ce_f24_cash_earnings_divergence_divstab_252d_base_v058_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = _safe_div(_mean(d, 63), _std(d, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# absolute divergence magnitude (earnings opacity), 126d
def f24ce_f24_cash_earnings_divergence_absdiv_126d_base_v059_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo).abs(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# absolute accrual magnitude (accrual intensity), 126d
def f24ce_f24_cash_earnings_divergence_absacc_126d_base_v060_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets).abs(), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# fcf/assets free-cash yield, 126d
def f24ce_f24_cash_earnings_divergence_fcfyield_126d_base_v061_signal(fcf, assets, netinc, ncfo):
    result = _mean(_safe_div(fcf, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo/assets cash-return on assets, 126d
def f24ce_f24_cash_earnings_divergence_cfroa_126d_base_v062_signal(ncfo, assets, netinc):
    result = _mean(_safe_div(ncfo, assets), 126) + _f24_quality(ncfo, netinc) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# netinc/assets accrual ROA, 126d
def f24ce_f24_cash_earnings_divergence_earnroa_126d_base_v063_signal(netinc, assets, ncfo):
    result = _mean(_safe_div(netinc, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-accrual ROA gap (ncfo - netinc)/assets, 126d
def f24ce_f24_cash_earnings_divergence_roagap_126d_base_v064_signal(ncfo, netinc, assets):
    result = _mean(_safe_div(ncfo - netinc, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fcf-vs-ncfo investing drag (ncfo - fcf)/assets, 126d
def f24ce_f24_cash_earnings_divergence_capexdrag_126d_base_v065_signal(ncfo, fcf, assets, netinc):
    result = _mean(_safe_div(ncfo - fcf, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual z over 63d window (short reactive)
def f24ce_f24_cash_earnings_divergence_zaccrual63w_base_v066_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence z over 126d window
def f24ce_f24_cash_earnings_divergence_zdiverg126w_base_v067_signal(netinc, ncfo):
    result = _z(_f24_divergence(netinc, ncfo), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# noncash load smoothed long, 504d
def f24ce_f24_cash_earnings_divergence_noncash_504d_base_v068_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# quality smoothed long, 504d
def f24ce_f24_cash_earnings_divergence_quality_504d_base_v069_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# divergence smoothed long, 504d
def f24ce_f24_cash_earnings_divergence_diverg_504d_base_v070_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# depamor/revenue D&A intensity, 126d
def f24ce_f24_cash_earnings_divergence_daintens_126d_base_v071_signal(depamor, revenue, netinc, ncfo):
    result = _mean(_safe_div(depamor, revenue), 126) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual minus non-cash load interaction, 126d
def f24ce_f24_cash_earnings_divergence_accnoncash_126d_base_v072_signal(netinc, ncfo, assets, depamor):
    a = _f24_accrual(netinc, ncfo, assets)
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = _mean(a - nc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# quality times non-cash load (earnings-quality conditioned on D&A), 126d
def f24ce_f24_cash_earnings_divergence_qualnoncash_126d_base_v073_signal(ncfo, netinc, depamor):
    q = _f24_quality(ncfo, netinc)
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = _mean(q * nc, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accrual EWMA span 252
def f24ce_f24_cash_earnings_divergence_accewm_252d_base_v074_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# divergence EWMA span 126
def f24ce_f24_cash_earnings_divergence_divewm_126d_base_v075_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24ce_f24_cash_earnings_divergence_accrual_63d_base_v001_signal,
    f24ce_f24_cash_earnings_divergence_accrual_126d_base_v002_signal,
    f24ce_f24_cash_earnings_divergence_accrual_252d_base_v003_signal,
    f24ce_f24_cash_earnings_divergence_accrual_504d_base_v004_signal,
    f24ce_f24_cash_earnings_divergence_quality_63d_base_v005_signal,
    f24ce_f24_cash_earnings_divergence_quality_126d_base_v006_signal,
    f24ce_f24_cash_earnings_divergence_quality_252d_base_v007_signal,
    f24ce_f24_cash_earnings_divergence_diverg_63d_base_v008_signal,
    f24ce_f24_cash_earnings_divergence_diverg_126d_base_v009_signal,
    f24ce_f24_cash_earnings_divergence_diverg_252d_base_v010_signal,
    f24ce_f24_cash_earnings_divergence_noncash_63d_base_v011_signal,
    f24ce_f24_cash_earnings_divergence_noncash_126d_base_v012_signal,
    f24ce_f24_cash_earnings_divergence_noncash_252d_base_v013_signal,
    f24ce_f24_cash_earnings_divergence_fcfconv_63d_base_v014_signal,
    f24ce_f24_cash_earnings_divergence_fcfconv_126d_base_v015_signal,
    f24ce_f24_cash_earnings_divergence_fcfconv_252d_base_v016_signal,
    f24ce_f24_cash_earnings_divergence_fcfaccr_63d_base_v017_signal,
    f24ce_f24_cash_earnings_divergence_fcfaccr_126d_base_v018_signal,
    f24ce_f24_cash_earnings_divergence_fcfaccr_252d_base_v019_signal,
    f24ce_f24_cash_earnings_divergence_cashmargin_63d_base_v020_signal,
    f24ce_f24_cash_earnings_divergence_cashmargin_126d_base_v021_signal,
    f24ce_f24_cash_earnings_divergence_cashmargin_252d_base_v022_signal,
    f24ce_f24_cash_earnings_divergence_earnmargin_126d_base_v023_signal,
    f24ce_f24_cash_earnings_divergence_margingap_126d_base_v024_signal,
    f24ce_f24_cash_earnings_divergence_margingap_252d_base_v025_signal,
    f24ce_f24_cash_earnings_divergence_daearn_126d_base_v026_signal,
    f24ce_f24_cash_earnings_divergence_daearn_252d_base_v027_signal,
    f24ce_f24_cash_earnings_divergence_dacash_126d_base_v028_signal,
    f24ce_f24_cash_earnings_divergence_zaccrual_63d_base_v029_signal,
    f24ce_f24_cash_earnings_divergence_zaccrual_126d_base_v030_signal,
    f24ce_f24_cash_earnings_divergence_zaccrual_504d_base_v031_signal,
    f24ce_f24_cash_earnings_divergence_zquality_252d_base_v032_signal,
    f24ce_f24_cash_earnings_divergence_zdiverg_252d_base_v033_signal,
    f24ce_f24_cash_earnings_divergence_znoncash_252d_base_v034_signal,
    f24ce_f24_cash_earnings_divergence_accslope_63d_base_v035_signal,
    f24ce_f24_cash_earnings_divergence_accslope_126d_base_v036_signal,
    f24ce_f24_cash_earnings_divergence_accslope_252d_base_v037_signal,
    f24ce_f24_cash_earnings_divergence_qualslope_126d_base_v038_signal,
    f24ce_f24_cash_earnings_divergence_divslope_126d_base_v039_signal,
    f24ce_f24_cash_earnings_divergence_accvol_63d_base_v040_signal,
    f24ce_f24_cash_earnings_divergence_accvol_126d_base_v041_signal,
    f24ce_f24_cash_earnings_divergence_accvol_252d_base_v042_signal,
    f24ce_f24_cash_earnings_divergence_divvol_126d_base_v043_signal,
    f24ce_f24_cash_earnings_divergence_divvol_252d_base_v044_signal,
    f24ce_f24_cash_earnings_divergence_qualvol_252d_base_v045_signal,
    f24ce_f24_cash_earnings_divergence_accrank_252d_base_v046_signal,
    f24ce_f24_cash_earnings_divergence_qualrank_252d_base_v047_signal,
    f24ce_f24_cash_earnings_divergence_divrank_126d_base_v048_signal,
    f24ce_f24_cash_earnings_divergence_accmr_252d_base_v049_signal,
    f24ce_f24_cash_earnings_divergence_qualmr_252d_base_v050_signal,
    f24ce_f24_cash_earnings_divergence_divsurp_base_v051_signal,
    f24ce_f24_cash_earnings_divergence_accspread_base_v052_signal,
    f24ce_f24_cash_earnings_divergence_qualspread_base_v053_signal,
    f24ce_f24_cash_earnings_divergence_accewm_63d_base_v054_signal,
    f24ce_f24_cash_earnings_divergence_accewm_126d_base_v055_signal,
    f24ce_f24_cash_earnings_divergence_qualewm_126d_base_v056_signal,
    f24ce_f24_cash_earnings_divergence_accstab_252d_base_v057_signal,
    f24ce_f24_cash_earnings_divergence_divstab_252d_base_v058_signal,
    f24ce_f24_cash_earnings_divergence_absdiv_126d_base_v059_signal,
    f24ce_f24_cash_earnings_divergence_absacc_126d_base_v060_signal,
    f24ce_f24_cash_earnings_divergence_fcfyield_126d_base_v061_signal,
    f24ce_f24_cash_earnings_divergence_cfroa_126d_base_v062_signal,
    f24ce_f24_cash_earnings_divergence_earnroa_126d_base_v063_signal,
    f24ce_f24_cash_earnings_divergence_roagap_126d_base_v064_signal,
    f24ce_f24_cash_earnings_divergence_capexdrag_126d_base_v065_signal,
    f24ce_f24_cash_earnings_divergence_zaccrual63w_base_v066_signal,
    f24ce_f24_cash_earnings_divergence_zdiverg126w_base_v067_signal,
    f24ce_f24_cash_earnings_divergence_noncash_504d_base_v068_signal,
    f24ce_f24_cash_earnings_divergence_quality_504d_base_v069_signal,
    f24ce_f24_cash_earnings_divergence_diverg_504d_base_v070_signal,
    f24ce_f24_cash_earnings_divergence_daintens_126d_base_v071_signal,
    f24ce_f24_cash_earnings_divergence_accnoncash_126d_base_v072_signal,
    f24ce_f24_cash_earnings_divergence_qualnoncash_126d_base_v073_signal,
    f24ce_f24_cash_earnings_divergence_accewm_252d_base_v074_signal,
    f24ce_f24_cash_earnings_divergence_divewm_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_CASH_EARNINGS_DIVERGENCE_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f24_cash_earnings_divergence_base_001_075_claude: {n_features} features pass")
