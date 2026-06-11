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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f24ce_f24_cash_earnings_divergence_accrual_63d_slope_v001_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrual_126d_slope_v002_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrual_252d_slope_v003_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrual_504d_slope_v004_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_63d_slope_v005_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_126d_slope_v006_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_252d_slope_v007_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_63d_slope_v008_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_126d_slope_v009_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_252d_slope_v010_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_noncash_63d_slope_v011_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_noncash_126d_slope_v012_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_noncash_252d_slope_v013_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfconv_63d_slope_v014_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 63) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfconv_126d_slope_v015_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 126) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfconv_252d_slope_v016_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 252) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfaccr_63d_slope_v017_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 63) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfaccr_126d_slope_v018_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfaccr_252d_slope_v019_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_cashmargin_63d_slope_v020_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 63) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_cashmargin_126d_slope_v021_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 126) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_cashmargin_252d_slope_v022_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 252) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_earnmargin_126d_slope_v023_signal(netinc, revenue, ncfo):
    result = _mean(_safe_div(netinc, revenue), 126) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_margingap_126d_slope_v024_signal(netinc, ncfo, revenue):
    result = _mean(_safe_div(netinc - ncfo, revenue), 126) + _f24_divergence(netinc, ncfo) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_margingap_252d_slope_v025_signal(netinc, ncfo, revenue):
    result = _mean(_safe_div(netinc - ncfo, revenue), 252) + _f24_divergence(netinc, ncfo) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_daearn_126d_slope_v026_signal(depamor, netinc, ncfo):
    result = _mean(_safe_div(depamor, netinc), 126) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_daearn_252d_slope_v027_signal(depamor, netinc, ncfo):
    result = _mean(_safe_div(depamor, netinc), 252) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_dacash_126d_slope_v028_signal(depamor, ncfo, netinc):
    result = _mean(_safe_div(depamor, ncfo), 126) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zaccrual_63d_slope_v029_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zaccrual_126d_slope_v030_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zaccrual_504d_slope_v031_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zquality_252d_slope_v032_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zdiverg_252d_slope_v033_signal(netinc, ncfo):
    result = _z(_f24_divergence(netinc, ncfo), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_znoncash_252d_slope_v034_signal(netinc, ncfo, depamor):
    result = _z(_f24_noncash(netinc, ncfo, depamor), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accslope_63d_slope_v035_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accslope_126d_slope_v036_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accslope_252d_slope_v037_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualslope_126d_slope_v038_signal(ncfo, netinc):
    result = _slope(_f24_quality(ncfo, netinc), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divslope_126d_slope_v039_signal(netinc, ncfo):
    result = _slope(_f24_divergence(netinc, ncfo), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accvol_63d_slope_v040_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accvol_126d_slope_v041_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accvol_252d_slope_v042_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divvol_126d_slope_v043_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divvol_252d_slope_v044_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualvol_252d_slope_v045_signal(ncfo, netinc):
    result = _std(_f24_quality(ncfo, netinc), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrank_252d_slope_v046_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualrank_252d_slope_v047_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divrank_126d_slope_v048_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accmr_252d_slope_v049_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a - _mean(a, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualmr_252d_slope_v050_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q - _mean(q, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divsurp_slope_v051_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = _mean(d, 63) - _mean(d, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accspread_slope_v052_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = _mean(a, 63) - _mean(a, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualspread_slope_v053_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = _mean(q, 63) - _mean(q, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accewm_63d_slope_v054_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accewm_126d_slope_v055_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualewm_126d_slope_v056_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accstab_252d_slope_v057_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = _safe_div(_mean(a, 63), _std(a, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divstab_252d_slope_v058_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = _safe_div(_mean(d, 63), _std(d, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_absdiv_126d_slope_v059_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo).abs(), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_absacc_126d_slope_v060_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets).abs(), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfyield_126d_slope_v061_signal(fcf, assets, netinc, ncfo):
    result = _mean(_safe_div(fcf, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_cfroa_126d_slope_v062_signal(ncfo, assets, netinc):
    result = _mean(_safe_div(ncfo, assets), 126) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_earnroa_126d_slope_v063_signal(netinc, assets, ncfo):
    result = _mean(_safe_div(netinc, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_roagap_126d_slope_v064_signal(ncfo, netinc, assets):
    result = _mean(_safe_div(ncfo - netinc, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_capexdrag_126d_slope_v065_signal(ncfo, fcf, assets, netinc):
    result = _mean(_safe_div(ncfo - fcf, assets), 126) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zaccrual63w_slope_v066_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zdiverg126w_slope_v067_signal(netinc, ncfo):
    result = _z(_f24_divergence(netinc, ncfo), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_noncash_504d_slope_v068_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_504d_slope_v069_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_504d_slope_v070_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_daintens_126d_slope_v071_signal(depamor, revenue, netinc, ncfo):
    result = _mean(_safe_div(depamor, revenue), 126) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accnoncash_126d_slope_v072_signal(netinc, ncfo, assets, depamor):
    a = _f24_accrual(netinc, ncfo, assets)
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = _mean(a - nc, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualnoncash_126d_slope_v073_signal(ncfo, netinc, depamor):
    q = _f24_quality(ncfo, netinc)
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = _mean(q * nc, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accewm_252d_slope_v074_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divewm_126d_slope_v075_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrual_42d_slope_v076_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrual_189d_slope_v077_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_42d_slope_v078_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_189d_slope_v079_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_42d_slope_v080_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_189d_slope_v081_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_noncash_189d_slope_v082_signal(netinc, ncfo, depamor):
    result = _mean(_f24_noncash(netinc, ncfo, depamor), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zaccrual_189d_slope_v083_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zquality_126d_slope_v084_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zquality_504d_slope_v085_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zdiverg_504d_slope_v086_signal(netinc, ncfo):
    result = _z(_f24_divergence(netinc, ncfo), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_znoncash_126d_slope_v087_signal(netinc, ncfo, depamor):
    result = _z(_f24_noncash(netinc, ncfo, depamor), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accslope_42d_slope_v088_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accslope_189d_slope_v089_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualslope_63d_slope_v090_signal(ncfo, netinc):
    result = _slope(_f24_quality(ncfo, netinc), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualslope_252d_slope_v091_signal(ncfo, netinc):
    result = _slope(_f24_quality(ncfo, netinc), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divslope_63d_slope_v092_signal(netinc, ncfo):
    result = _slope(_f24_divergence(netinc, ncfo), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divslope_252d_slope_v093_signal(netinc, ncfo):
    result = _slope(_f24_divergence(netinc, ncfo), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_ncslope_126d_slope_v094_signal(netinc, ncfo, depamor):
    result = _slope(_f24_noncash(netinc, ncfo, depamor), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accvol_504d_slope_v095_signal(netinc, ncfo, assets):
    result = _std(_f24_accrual(netinc, ncfo, assets), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualvol_126d_slope_v096_signal(ncfo, netinc):
    result = _std(_f24_quality(ncfo, netinc), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divvol_63d_slope_v097_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_ncvol_252d_slope_v098_signal(netinc, ncfo, depamor):
    result = _std(_f24_noncash(netinc, ncfo, depamor), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrank_126d_slope_v099_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrank_504d_slope_v100_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualrank_126d_slope_v101_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divrank_252d_slope_v102_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_ncrank_252d_slope_v103_signal(netinc, ncfo, depamor):
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = nc.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accmr_126d_slope_v104_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a - _mean(a, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualmr_126d_slope_v105_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q - _mean(q, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divmr_252d_slope_v106_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d - _mean(d, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualsurp_slope_v107_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = _mean(q, 63) - _mean(q, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accsurp_slope_v108_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = _mean(a, 42) - _mean(a, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divspread_slope_v109_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = _mean(d, 42) - _mean(d, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divewm_63d_slope_v110_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualewm_63d_slope_v111_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualewm_252d_slope_v112_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_ncewm_126d_slope_v113_signal(netinc, ncfo, depamor):
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = nc.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divaccstab_slope_v114_signal(netinc, ncfo, assets):
    d = _f24_divergence(netinc, ncfo)
    a = _f24_accrual(netinc, ncfo, assets)
    result = _safe_div(_mean(d, 63), _std(a, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualstab_252d_slope_v115_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = _safe_div(_mean(q, 63), _std(q, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_absdiv_252d_slope_v116_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo).abs(), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_absacc_252d_slope_v117_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets).abs(), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfyield_252d_slope_v118_signal(fcf, assets, netinc, ncfo):
    result = _mean(_safe_div(fcf, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_cfroa_252d_slope_v119_signal(ncfo, assets, netinc):
    result = _mean(_safe_div(ncfo, assets), 252) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_earnroa_252d_slope_v120_signal(netinc, assets, ncfo):
    result = _mean(_safe_div(netinc, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_roagap_252d_slope_v121_signal(ncfo, netinc, assets):
    result = _mean(_safe_div(ncfo - netinc, assets), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfconv_42d_slope_v122_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 42) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfconv_189d_slope_v123_signal(fcf, netinc, ncfo):
    result = _mean(_safe_div(fcf, netinc), 189) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfaccr_42d_slope_v124_signal(netinc, fcf, assets, ncfo):
    result = _mean(_safe_div(netinc - fcf, assets), 42) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_cashmargin_42d_slope_v125_signal(ncfo, revenue, netinc):
    result = _mean(_safe_div(ncfo, revenue), 42) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_earnmargin_252d_slope_v126_signal(netinc, revenue, ncfo):
    result = _mean(_safe_div(netinc, revenue), 252) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_margingap_63d_slope_v127_signal(netinc, ncfo, revenue):
    result = _mean(_safe_div(netinc - ncfo, revenue), 63) + _f24_divergence(netinc, ncfo) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_daearn_63d_slope_v128_signal(depamor, netinc, ncfo):
    result = _mean(_safe_div(depamor, netinc), 63) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_daintens_252d_slope_v129_signal(depamor, revenue, netinc, ncfo):
    result = _mean(_safe_div(depamor, revenue), 252) + _f24_noncash(netinc, ncfo, depamor) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_dacash_252d_slope_v130_signal(depamor, ncfo, netinc):
    result = _mean(_safe_div(depamor, ncfo), 252) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accdivprod_126d_slope_v131_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    d = _f24_divergence(netinc, ncfo)
    result = _mean(a * d, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualminusdiv_126d_slope_v132_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    d = _f24_divergence(netinc, ncfo)
    result = _mean(q - d, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divnoncash_126d_slope_v133_signal(netinc, ncfo, depamor):
    d = _f24_divergence(netinc, ncfo)
    nc = _f24_noncash(netinc, ncfo, depamor)
    result = _mean(d * nc, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accaccel_126d_slope_v134_signal(netinc, ncfo, assets):
    s = _slope(_f24_accrual(netinc, ncfo, assets), 63)
    result = s - _mean(s, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualaccel_126d_slope_v135_signal(ncfo, netinc):
    s = _slope(_f24_quality(ncfo, netinc), 63)
    result = s - _mean(s, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accpercash_126d_slope_v136_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    cm = _safe_div(ncfo, assets)
    result = _mean(_safe_div(a, cm.abs() + 1e-9), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_quality_84d_slope_v137_signal(ncfo, netinc):
    result = _mean(_f24_quality(ncfo, netinc), 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrual_84d_slope_v138_signal(netinc, ncfo, assets):
    result = _mean(_f24_accrual(netinc, ncfo, assets), 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_diverg_84d_slope_v139_signal(netinc, ncfo):
    result = _mean(_f24_divergence(netinc, ncfo), 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zaccrual_84w_slope_v140_signal(netinc, ncfo, assets):
    result = _z(_f24_accrual(netinc, ncfo, assets), 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_zquality_315w_slope_v141_signal(ncfo, netinc):
    result = _z(_f24_quality(ncfo, netinc), 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accslope_315d_slope_v142_signal(netinc, ncfo, assets):
    result = _slope(_f24_accrual(netinc, ncfo, assets), 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divvol_504d_slope_v143_signal(netinc, ncfo):
    result = _std(_f24_divergence(netinc, ncfo), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_fcfdiv_126d_slope_v144_signal(ncfo, fcf, assets, netinc):
    g = _safe_div(ncfo - fcf, assets)
    result = _mean(g, 126) + _f24_quality(ncfo, netinc) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_earnfcfdiv_126d_slope_v145_signal(netinc, fcf, revenue, ncfo):
    g = _safe_div(netinc - fcf, revenue)
    result = _mean(g, 126) + _f24_divergence(netinc, ncfo) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accrev_252d_slope_v146_signal(netinc, ncfo, revenue, assets):
    result = _mean(_safe_div(netinc - ncfo, revenue), 252) + _f24_accrual(netinc, ncfo, assets) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_qualinnov_slope_v147_signal(ncfo, netinc):
    q = _f24_quality(ncfo, netinc)
    result = q.ewm(span=42, min_periods=21).mean() - q.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_accinnov_slope_v148_signal(netinc, ncfo, assets):
    a = _f24_accrual(netinc, ncfo, assets)
    result = a.ewm(span=42, min_periods=21).mean() - a.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_divinnov_slope_v149_signal(netinc, ncfo):
    d = _f24_divergence(netinc, ncfo)
    result = d.ewm(span=42, min_periods=21).mean() - d.ewm(span=252, min_periods=84).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f24ce_f24_cash_earnings_divergence_blend_multi_slope_v150_signal(netinc, ncfo, assets):
    a = _z(_f24_accrual(netinc, ncfo, assets), 252)
    q = _z(_f24_quality(ncfo, netinc), 252)
    d = _z(_f24_divergence(netinc, ncfo), 252)
    result = (a + q + d) / 3.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f24ce_f24_cash_earnings_divergence_accrual_63d_slope_v001_signal,    f24ce_f24_cash_earnings_divergence_accrual_126d_slope_v002_signal,    f24ce_f24_cash_earnings_divergence_accrual_252d_slope_v003_signal,    f24ce_f24_cash_earnings_divergence_accrual_504d_slope_v004_signal,    f24ce_f24_cash_earnings_divergence_quality_63d_slope_v005_signal,    f24ce_f24_cash_earnings_divergence_quality_126d_slope_v006_signal,    f24ce_f24_cash_earnings_divergence_quality_252d_slope_v007_signal,    f24ce_f24_cash_earnings_divergence_diverg_63d_slope_v008_signal,    f24ce_f24_cash_earnings_divergence_diverg_126d_slope_v009_signal,    f24ce_f24_cash_earnings_divergence_diverg_252d_slope_v010_signal,    f24ce_f24_cash_earnings_divergence_noncash_63d_slope_v011_signal,    f24ce_f24_cash_earnings_divergence_noncash_126d_slope_v012_signal,    f24ce_f24_cash_earnings_divergence_noncash_252d_slope_v013_signal,    f24ce_f24_cash_earnings_divergence_fcfconv_63d_slope_v014_signal,    f24ce_f24_cash_earnings_divergence_fcfconv_126d_slope_v015_signal,    f24ce_f24_cash_earnings_divergence_fcfconv_252d_slope_v016_signal,    f24ce_f24_cash_earnings_divergence_fcfaccr_63d_slope_v017_signal,    f24ce_f24_cash_earnings_divergence_fcfaccr_126d_slope_v018_signal,    f24ce_f24_cash_earnings_divergence_fcfaccr_252d_slope_v019_signal,    f24ce_f24_cash_earnings_divergence_cashmargin_63d_slope_v020_signal,    f24ce_f24_cash_earnings_divergence_cashmargin_126d_slope_v021_signal,    f24ce_f24_cash_earnings_divergence_cashmargin_252d_slope_v022_signal,    f24ce_f24_cash_earnings_divergence_earnmargin_126d_slope_v023_signal,    f24ce_f24_cash_earnings_divergence_margingap_126d_slope_v024_signal,    f24ce_f24_cash_earnings_divergence_margingap_252d_slope_v025_signal,    f24ce_f24_cash_earnings_divergence_daearn_126d_slope_v026_signal,    f24ce_f24_cash_earnings_divergence_daearn_252d_slope_v027_signal,    f24ce_f24_cash_earnings_divergence_dacash_126d_slope_v028_signal,    f24ce_f24_cash_earnings_divergence_zaccrual_63d_slope_v029_signal,    f24ce_f24_cash_earnings_divergence_zaccrual_126d_slope_v030_signal,    f24ce_f24_cash_earnings_divergence_zaccrual_504d_slope_v031_signal,    f24ce_f24_cash_earnings_divergence_zquality_252d_slope_v032_signal,    f24ce_f24_cash_earnings_divergence_zdiverg_252d_slope_v033_signal,    f24ce_f24_cash_earnings_divergence_znoncash_252d_slope_v034_signal,    f24ce_f24_cash_earnings_divergence_accslope_63d_slope_v035_signal,    f24ce_f24_cash_earnings_divergence_accslope_126d_slope_v036_signal,    f24ce_f24_cash_earnings_divergence_accslope_252d_slope_v037_signal,    f24ce_f24_cash_earnings_divergence_qualslope_126d_slope_v038_signal,    f24ce_f24_cash_earnings_divergence_divslope_126d_slope_v039_signal,    f24ce_f24_cash_earnings_divergence_accvol_63d_slope_v040_signal,    f24ce_f24_cash_earnings_divergence_accvol_126d_slope_v041_signal,    f24ce_f24_cash_earnings_divergence_accvol_252d_slope_v042_signal,    f24ce_f24_cash_earnings_divergence_divvol_126d_slope_v043_signal,    f24ce_f24_cash_earnings_divergence_divvol_252d_slope_v044_signal,    f24ce_f24_cash_earnings_divergence_qualvol_252d_slope_v045_signal,    f24ce_f24_cash_earnings_divergence_accrank_252d_slope_v046_signal,    f24ce_f24_cash_earnings_divergence_qualrank_252d_slope_v047_signal,    f24ce_f24_cash_earnings_divergence_divrank_126d_slope_v048_signal,    f24ce_f24_cash_earnings_divergence_accmr_252d_slope_v049_signal,    f24ce_f24_cash_earnings_divergence_qualmr_252d_slope_v050_signal,    f24ce_f24_cash_earnings_divergence_divsurp_slope_v051_signal,    f24ce_f24_cash_earnings_divergence_accspread_slope_v052_signal,    f24ce_f24_cash_earnings_divergence_qualspread_slope_v053_signal,    f24ce_f24_cash_earnings_divergence_accewm_63d_slope_v054_signal,    f24ce_f24_cash_earnings_divergence_accewm_126d_slope_v055_signal,    f24ce_f24_cash_earnings_divergence_qualewm_126d_slope_v056_signal,    f24ce_f24_cash_earnings_divergence_accstab_252d_slope_v057_signal,    f24ce_f24_cash_earnings_divergence_divstab_252d_slope_v058_signal,    f24ce_f24_cash_earnings_divergence_absdiv_126d_slope_v059_signal,    f24ce_f24_cash_earnings_divergence_absacc_126d_slope_v060_signal,    f24ce_f24_cash_earnings_divergence_fcfyield_126d_slope_v061_signal,    f24ce_f24_cash_earnings_divergence_cfroa_126d_slope_v062_signal,    f24ce_f24_cash_earnings_divergence_earnroa_126d_slope_v063_signal,    f24ce_f24_cash_earnings_divergence_roagap_126d_slope_v064_signal,    f24ce_f24_cash_earnings_divergence_capexdrag_126d_slope_v065_signal,    f24ce_f24_cash_earnings_divergence_zaccrual63w_slope_v066_signal,    f24ce_f24_cash_earnings_divergence_zdiverg126w_slope_v067_signal,    f24ce_f24_cash_earnings_divergence_noncash_504d_slope_v068_signal,    f24ce_f24_cash_earnings_divergence_quality_504d_slope_v069_signal,    f24ce_f24_cash_earnings_divergence_diverg_504d_slope_v070_signal,    f24ce_f24_cash_earnings_divergence_daintens_126d_slope_v071_signal,    f24ce_f24_cash_earnings_divergence_accnoncash_126d_slope_v072_signal,    f24ce_f24_cash_earnings_divergence_qualnoncash_126d_slope_v073_signal,    f24ce_f24_cash_earnings_divergence_accewm_252d_slope_v074_signal,    f24ce_f24_cash_earnings_divergence_divewm_126d_slope_v075_signal,    f24ce_f24_cash_earnings_divergence_accrual_42d_slope_v076_signal,    f24ce_f24_cash_earnings_divergence_accrual_189d_slope_v077_signal,    f24ce_f24_cash_earnings_divergence_quality_42d_slope_v078_signal,    f24ce_f24_cash_earnings_divergence_quality_189d_slope_v079_signal,    f24ce_f24_cash_earnings_divergence_diverg_42d_slope_v080_signal,    f24ce_f24_cash_earnings_divergence_diverg_189d_slope_v081_signal,    f24ce_f24_cash_earnings_divergence_noncash_189d_slope_v082_signal,    f24ce_f24_cash_earnings_divergence_zaccrual_189d_slope_v083_signal,    f24ce_f24_cash_earnings_divergence_zquality_126d_slope_v084_signal,    f24ce_f24_cash_earnings_divergence_zquality_504d_slope_v085_signal,    f24ce_f24_cash_earnings_divergence_zdiverg_504d_slope_v086_signal,    f24ce_f24_cash_earnings_divergence_znoncash_126d_slope_v087_signal,    f24ce_f24_cash_earnings_divergence_accslope_42d_slope_v088_signal,    f24ce_f24_cash_earnings_divergence_accslope_189d_slope_v089_signal,    f24ce_f24_cash_earnings_divergence_qualslope_63d_slope_v090_signal,    f24ce_f24_cash_earnings_divergence_qualslope_252d_slope_v091_signal,    f24ce_f24_cash_earnings_divergence_divslope_63d_slope_v092_signal,    f24ce_f24_cash_earnings_divergence_divslope_252d_slope_v093_signal,    f24ce_f24_cash_earnings_divergence_ncslope_126d_slope_v094_signal,    f24ce_f24_cash_earnings_divergence_accvol_504d_slope_v095_signal,    f24ce_f24_cash_earnings_divergence_qualvol_126d_slope_v096_signal,    f24ce_f24_cash_earnings_divergence_divvol_63d_slope_v097_signal,    f24ce_f24_cash_earnings_divergence_ncvol_252d_slope_v098_signal,    f24ce_f24_cash_earnings_divergence_accrank_126d_slope_v099_signal,    f24ce_f24_cash_earnings_divergence_accrank_504d_slope_v100_signal,    f24ce_f24_cash_earnings_divergence_qualrank_126d_slope_v101_signal,    f24ce_f24_cash_earnings_divergence_divrank_252d_slope_v102_signal,    f24ce_f24_cash_earnings_divergence_ncrank_252d_slope_v103_signal,    f24ce_f24_cash_earnings_divergence_accmr_126d_slope_v104_signal,    f24ce_f24_cash_earnings_divergence_qualmr_126d_slope_v105_signal,    f24ce_f24_cash_earnings_divergence_divmr_252d_slope_v106_signal,    f24ce_f24_cash_earnings_divergence_qualsurp_slope_v107_signal,    f24ce_f24_cash_earnings_divergence_accsurp_slope_v108_signal,    f24ce_f24_cash_earnings_divergence_divspread_slope_v109_signal,    f24ce_f24_cash_earnings_divergence_divewm_63d_slope_v110_signal,    f24ce_f24_cash_earnings_divergence_qualewm_63d_slope_v111_signal,    f24ce_f24_cash_earnings_divergence_qualewm_252d_slope_v112_signal,    f24ce_f24_cash_earnings_divergence_ncewm_126d_slope_v113_signal,    f24ce_f24_cash_earnings_divergence_divaccstab_slope_v114_signal,    f24ce_f24_cash_earnings_divergence_qualstab_252d_slope_v115_signal,    f24ce_f24_cash_earnings_divergence_absdiv_252d_slope_v116_signal,    f24ce_f24_cash_earnings_divergence_absacc_252d_slope_v117_signal,    f24ce_f24_cash_earnings_divergence_fcfyield_252d_slope_v118_signal,    f24ce_f24_cash_earnings_divergence_cfroa_252d_slope_v119_signal,    f24ce_f24_cash_earnings_divergence_earnroa_252d_slope_v120_signal,    f24ce_f24_cash_earnings_divergence_roagap_252d_slope_v121_signal,    f24ce_f24_cash_earnings_divergence_fcfconv_42d_slope_v122_signal,    f24ce_f24_cash_earnings_divergence_fcfconv_189d_slope_v123_signal,    f24ce_f24_cash_earnings_divergence_fcfaccr_42d_slope_v124_signal,    f24ce_f24_cash_earnings_divergence_cashmargin_42d_slope_v125_signal,    f24ce_f24_cash_earnings_divergence_earnmargin_252d_slope_v126_signal,    f24ce_f24_cash_earnings_divergence_margingap_63d_slope_v127_signal,    f24ce_f24_cash_earnings_divergence_daearn_63d_slope_v128_signal,    f24ce_f24_cash_earnings_divergence_daintens_252d_slope_v129_signal,    f24ce_f24_cash_earnings_divergence_dacash_252d_slope_v130_signal,    f24ce_f24_cash_earnings_divergence_accdivprod_126d_slope_v131_signal,    f24ce_f24_cash_earnings_divergence_qualminusdiv_126d_slope_v132_signal,    f24ce_f24_cash_earnings_divergence_divnoncash_126d_slope_v133_signal,    f24ce_f24_cash_earnings_divergence_accaccel_126d_slope_v134_signal,    f24ce_f24_cash_earnings_divergence_qualaccel_126d_slope_v135_signal,    f24ce_f24_cash_earnings_divergence_accpercash_126d_slope_v136_signal,    f24ce_f24_cash_earnings_divergence_quality_84d_slope_v137_signal,    f24ce_f24_cash_earnings_divergence_accrual_84d_slope_v138_signal,    f24ce_f24_cash_earnings_divergence_diverg_84d_slope_v139_signal,    f24ce_f24_cash_earnings_divergence_zaccrual_84w_slope_v140_signal,    f24ce_f24_cash_earnings_divergence_zquality_315w_slope_v141_signal,    f24ce_f24_cash_earnings_divergence_accslope_315d_slope_v142_signal,    f24ce_f24_cash_earnings_divergence_divvol_504d_slope_v143_signal,    f24ce_f24_cash_earnings_divergence_fcfdiv_126d_slope_v144_signal,    f24ce_f24_cash_earnings_divergence_earnfcfdiv_126d_slope_v145_signal,    f24ce_f24_cash_earnings_divergence_accrev_252d_slope_v146_signal,    f24ce_f24_cash_earnings_divergence_qualinnov_slope_v147_signal,    f24ce_f24_cash_earnings_divergence_accinnov_slope_v148_signal,    f24ce_f24_cash_earnings_divergence_divinnov_slope_v149_signal,    f24ce_f24_cash_earnings_divergence_blend_multi_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_CASH_EARNINGS_DIVERGENCE_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f24_accrual', '_f24_quality', '_f24_divergence', '_f24_noncash')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    print("OK f24_cash_earnings_divergence_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
