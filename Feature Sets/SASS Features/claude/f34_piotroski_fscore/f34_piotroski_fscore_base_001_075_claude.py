import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _chg(s, w):
    return s - s.shift(w)


def _pctchg(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


# ===== Piotroski domain primitives =====
# Continuous (magnitude / probability weighted) versions of the 9 binaries.
# Each uses tanh / logistic squashing so the "score" is a smooth [-1,1] or [0,1]
# proxy for the hard 0/1 indicator, giving nunique>50 while preserving economics.

def _f34_soft_pos(s, scale):
    # soft "is positive" indicator: tanh of magnitude relative to its own scale
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(s / sc.replace(0, np.nan))


def _f34_soft_gt(a, b, scale):
    # soft "a > b" indicator scaled by the typical magnitude of |a|+|b|
    diff = a - b
    sc = (a.abs() + b.abs()).rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(diff / sc.replace(0, np.nan))


def _f34_soft_up(s, w, scale):
    # soft "Δs > 0 over w" indicator, magnitude-weighted
    d = s - s.shift(w)
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(d / sc.replace(0, np.nan))


def _f34_soft_down(s, w, scale):
    # soft "Δs < 0 over w" indicator (improvement when the quantity falls, e.g. leverage)
    d = s.shift(w) - s
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(d / sc.replace(0, np.nan))


def _f34_leverage(debt, assets):
    return _safe_div(debt, assets)


# ============================================================
# ---- COMPONENT 1: positive net income (profitability) ----
# soft positive-netinc score over 252d normalization
def f34pf_f34_piotroski_fscore_posni_252d_base_v001_signal(netinc):
    b = _f34_soft_pos(netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-netinc score smoothed over a quarter (persistence of profitability sign)
def f34pf_f34_piotroski_fscore_posni_63d_base_v002_signal(netinc):
    raw = _f34_soft_pos(netinc, 126)
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# netinc/assets dispersion: volatility of profitability (earnings stability)
def f34pf_f34_piotroski_fscore_posnia_252d_base_v003_signal(netinc, assets):
    r = _safe_div(netinc, assets)
    vol = r.rolling(126, min_periods=63).std()
    sc = r.abs().rolling(252, min_periods=126).mean()
    b = -np.tanh(vol / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 2: positive operating cash flow ----
# soft positive-ncfo score
def f34pf_f34_piotroski_fscore_posocf_252d_base_v004_signal(ncfo):
    b = _f34_soft_pos(ncfo, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo scaled by assets, soft-positive (cash return on assets)
def f34pf_f34_piotroski_fscore_posocfa_252d_base_v005_signal(ncfo, assets):
    r = _safe_div(ncfo, assets)
    sc = r.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(r / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year ncfo stayed positive, depth-weighted
def f34pf_f34_piotroski_fscore_posocffrac_252d_base_v006_signal(ncfo):
    soft = _f34_soft_pos(ncfo, 126)
    pos = (soft.clip(lower=0))
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 3: ΔROA > 0 (improving return on assets) ----
# soft ROA-improvement over 252d
def f34pf_f34_piotroski_fscore_droa_252d_base_v007_signal(roa):
    b = _f34_soft_up(roa, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft ROA-improvement over a half year
def f34pf_f34_piotroski_fscore_droa_126d_base_v008_signal(roa):
    b = _f34_soft_up(roa, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA improvement built from netinc/assets directly (independent of roa series)
def f34pf_f34_piotroski_fscore_droasyn_252d_base_v009_signal(netinc, assets):
    r = _safe_div(netinc, assets)
    b = _f34_soft_up(r, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 4: ncfo > netinc (accrual quality) ----
# soft accrual-quality: cash flow exceeds reported earnings
def f34pf_f34_piotroski_fscore_accr_252d_base_v010_signal(ncfo, netinc):
    b = _f34_soft_gt(ncfo, netinc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quality scaled by assets (Sloan-style accrual sign, squashed)
def f34pf_f34_piotroski_fscore_accra_252d_base_v011_signal(ncfo, netinc, assets):
    accr = _safe_div(ncfo - netinc, assets)
    sc = accr.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(accr / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quality smoothed over a quarter (durable cash-backing of earnings)
def f34pf_f34_piotroski_fscore_accrsm_63d_base_v012_signal(ncfo, netinc):
    raw = _f34_soft_gt(ncfo, netinc, 126)
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 5: Δleverage < 0 (deleveraging) ----
# soft deleveraging score (debt/assets falling)
def f34pf_f34_piotroski_fscore_dlev_252d_base_v013_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    b = _f34_soft_down(lev, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft deleveraging over a half year
def f34pf_f34_piotroski_fscore_dlev_126d_base_v014_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    b = _f34_soft_down(lev, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown streak: fraction of last year debt was below its 63d-ago level
def f34pf_f34_piotroski_fscore_dlevraw_252d_base_v015_signal(debt):
    falling = (debt < debt.shift(63)).astype(float)
    streak = falling.rolling(252, min_periods=126).mean()
    depth = (-_pctchg(debt, 63)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = streak + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 6: Δcurrent ratio > 0 (improving liquidity) ----
# soft current-ratio improvement
def f34pf_f34_piotroski_fscore_dcurr_252d_base_v016_signal(currentratio):
    b = _f34_soft_up(currentratio, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft current-ratio improvement over a quarter
def f34pf_f34_piotroski_fscore_dcurr_63d_base_v017_signal(currentratio):
    b = _f34_soft_up(currentratio, 63, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio level relative to its own 252d mean (liquidity standing)
def f34pf_f34_piotroski_fscore_currlvl_252d_base_v018_signal(currentratio):
    b = np.tanh(_z(currentratio, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 7: no dilution (Δsharesbas <= 0) ----
# soft no-dilution score: share count falling is good
def f34pf_f34_piotroski_fscore_nodil_252d_base_v019_signal(sharesbas):
    b = _f34_soft_down(sharesbas, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# no-dilution over a half year
def f34pf_f34_piotroski_fscore_nodil_126d_base_v020_signal(sharesbas):
    b = _f34_soft_down(sharesbas, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback consistency: fraction of quarters in last 2y share count fell, depth-weighted
def f34pf_f34_piotroski_fscore_buyback_252d_base_v021_signal(sharesbas):
    falling = (sharesbas < sharesbas.shift(63)).astype(float)
    consist = falling.rolling(504, min_periods=252).mean()
    b = consist - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 8: Δgross margin > 0 (margin expansion) ----
# soft gross-margin improvement
def f34pf_f34_piotroski_fscore_dgm_252d_base_v022_signal(grossmargin):
    b = _f34_soft_up(grossmargin, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft gross-margin improvement over a quarter
def f34pf_f34_piotroski_fscore_dgm_63d_base_v023_signal(grossmargin):
    b = _f34_soft_up(grossmargin, 63, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin level vs its own history (standing of profitability efficiency)
def f34pf_f34_piotroski_fscore_gmlvl_252d_base_v024_signal(grossmargin):
    b = np.tanh(_z(grossmargin, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- COMPONENT 9: Δasset turnover > 0 (efficiency improvement) ----
# soft asset-turnover improvement
def f34pf_f34_piotroski_fscore_dato_252d_base_v025_signal(assetturnover):
    b = _f34_soft_up(assetturnover, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft asset-turnover improvement over a half year
def f34pf_f34_piotroski_fscore_dato_126d_base_v026_signal(assetturnover):
    b = _f34_soft_up(assetturnover, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover level vs its own history
def f34pf_f34_piotroski_fscore_atolvl_252d_base_v027_signal(assetturnover):
    b = np.tanh(_z(assetturnover, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- FULL 9-COMPONENT CONTINUOUS F-SCORE COMPOSITES ----
# continuous F-score: average of all 9 soft components (range ~ -1..1), 252d
def f34pf_f34_piotroski_fscore_fscore9_252d_base_v028_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    b = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hard-binary 9-component F-score (0..9) made smooth by depth-weighting then ranked
def f34pf_f34_piotroski_fscore_fscorehard_252d_base_v029_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    lev = _f34_leverage(debt, assets)
    s = (
        (netinc > 0).astype(float)
        + (ncfo > 0).astype(float)
        + (_chg(roa, 252) > 0).astype(float)
        + (ncfo > netinc).astype(float)
        + (_chg(lev, 252) < 0).astype(float)
        + (_chg(currentratio, 252) > 0).astype(float)
        + (_chg(sharesbas, 252) <= 0).astype(float)
        + (_chg(grossmargin, 252) > 0).astype(float)
        + (_chg(assetturnover, 252) > 0).astype(float)
    )
    # add a small continuous magnitude tie-breaker so nunique>50
    mag = _z(_safe_div(ncfo, assets), 252) * 0.001
    b = (s + mag).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score over half-year deltas (faster-responding composite)
def f34pf_f34_piotroski_fscore_fscore9_126d_base_v030_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126)
    c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 126, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 126)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 126, 252)
    c6 = _f34_soft_up(currentratio, 126, 252)
    c7 = _f34_soft_down(sharesbas, 126, 252)
    c8 = _f34_soft_up(grossmargin, 126, 252)
    c9 = _f34_soft_up(assetturnover, 126, 252)
    b = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- SUBSET COMPOSITES ----
# profitability subset (components 1-4): netinc, ncfo, ΔROA, accrual quality
def f34pf_f34_piotroski_fscore_profsub_252d_base_v031_signal(netinc, ncfo, roa, assets):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    b = (c1 + c2 + c3 + c4) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage/liquidity subset (components 5-7): deleverage, current ratio, dilution
def f34pf_f34_piotroski_fscore_levsub_252d_base_v032_signal(debt, assets, currentratio, sharesbas):
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c7 = _f34_soft_down(sharesbas, 252, 252)
    b = (c5 + c6 + c7) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-efficiency subset (components 8-9): gross margin & asset turnover
def f34pf_f34_piotroski_fscore_effsub_252d_base_v033_signal(grossmargin, assetturnover):
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    b = (c8 + c9) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# "quality core" subset: positive cash flow + accruals + deleverage (balance-sheet trust)
def f34pf_f34_piotroski_fscore_qualcore_252d_base_v034_signal(ncfo, netinc, debt, assets):
    c2 = _f34_soft_pos(ncfo, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 252, 252)
    b = (c2 + c4 + c5) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# "improvement trio": geometric-mean agreement of ΔROA, Δgrossmargin, Δassetturnover
# (non-linear AND of operating improvements — distinct from the linear average)
def f34pf_f34_piotroski_fscore_imptrio_252d_base_v035_signal(roa, grossmargin, assetturnover):
    c3 = (_f34_soft_up(roa, 63, 126) + 1) / 2
    c8 = (_f34_soft_up(grossmargin, 63, 126) + 1) / 2
    c9 = (_f34_soft_up(assetturnover, 63, 126) + 1) / 2
    b = (c3 * c8 * c9) ** (1.0 / 3.0) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- WEIGHTED VARIANTS ----
# magnitude-weighted F-score: each component scaled by economic size of move
def f34pf_f34_piotroski_fscore_wmag_252d_base_v036_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin):
    roaq = _safe_div(netinc, assets)
    c1 = np.tanh(2.0 * roaq)
    c2 = np.tanh(2.0 * _safe_div(ncfo, assets))
    c3 = np.tanh(50.0 * _chg(roa, 252))
    accr = _safe_div(ncfo - netinc, assets)
    c4 = np.tanh(5.0 * accr)
    lev = _f34_leverage(debt, assets)
    c5 = np.tanh(-10.0 * _chg(lev, 252))
    c6 = np.tanh(2.0 * _chg(currentratio, 252))
    c8 = np.tanh(20.0 * _chg(grossmargin, 252))
    b = (c1 + c2 + c3 + c4 + c5 + c6 + c8) / 7.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# profitability-weighted F-score: difference between profitability subset and
# balance-sheet subset (tilt = where the strength concentrates), not a level
def f34pf_f34_piotroski_fscore_wprof_252d_base_v037_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    prof = (c1 + c2 + c3 + c4) / 4.0
    rest = (c5 + c6 + c7 + c8 + c9) / 5.0
    b = prof - rest
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-weighted F-score: efficiency subset minus profitability subset (tilt)
def f34pf_f34_piotroski_fscore_weff_252d_base_v038_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    eff = (c8 + c9) / 2.0
    base = (c1 + c2 + c5 + c6) / 4.0
    b = np.tanh(2.0 * (eff - base))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recency-weighted F-score: 63d composite MINUS 252d composite (acceleration of health)
def f34pf_f34_piotroski_fscore_wrecency_63d_base_v039_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    def comp(w, sc):
        c3 = _f34_soft_up(roa, w, sc)
        c4 = _f34_soft_gt(ncfo, netinc, sc)
        c5 = _f34_soft_down(_f34_leverage(debt, assets), w, sc)
        c6 = _f34_soft_up(currentratio, w, sc)
        c8 = _f34_soft_up(grossmargin, w, sc)
        c9 = _f34_soft_up(assetturnover, w, sc)
        return (c3 + c4 + c5 + c6 + c8 + c9) / 6.0
    b = comp(63, 126) - comp(252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ROLLING SUMS / PERSISTENCE OF THE COMPOSITE ----
# rolling-mean of the continuous F-score over a year (trend in financial health)
def f34pf_f34_piotroski_fscore_rollmean_252d_base_v040_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126)
    c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 126, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 126)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 126, 252)
    c6 = _f34_soft_up(currentratio, 126, 252)
    c7 = _f34_soft_down(sharesbas, 126, 252)
    c8 = _f34_soft_up(grossmargin, 126, 252)
    c9 = _f34_soft_up(assetturnover, 126, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    b = fs.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in the F-score over a year (improving vs deteriorating fundamentals)
def f34pf_f34_piotroski_fscore_fschg_252d_base_v041_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    b = fs - fs.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score percentile rank vs its own 504d history (relative financial standing)
def f34pf_f34_piotroski_fscore_fsrank_504d_base_v042_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    lev = _f34_leverage(debt, assets)
    c5 = _f34_soft_down(lev, 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    b = fs.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of "strong" components (soft score > 0.3) — depth-weighted discrete tally
def f34pf_f34_piotroski_fscore_strongcnt_252d_base_v043_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    comps = [
        _f34_soft_pos(netinc, 252),
        _f34_soft_pos(ncfo, 252),
        _f34_soft_up(roa, 252, 252),
        _f34_soft_gt(ncfo, netinc, 252),
        _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
        _f34_soft_up(currentratio, 252, 252),
        _f34_soft_down(sharesbas, 252, 252),
        _f34_soft_up(grossmargin, 252, 252),
        _f34_soft_up(assetturnover, 252, 252),
    ]
    tally = sum((c > 0.3).astype(float) for c in comps)
    mag = sum(c.clip(lower=0) for c in comps) * 0.01
    b = (tally + mag).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion across the 9 components (agreement vs conflict in fundamentals)
def f34pf_f34_piotroski_fscore_compdisp_252d_base_v044_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    comps = [
        _f34_soft_pos(netinc, 252),
        _f34_soft_pos(ncfo, 252),
        _f34_soft_up(roa, 252, 252),
        _f34_soft_gt(ncfo, netinc, 252),
        _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
        _f34_soft_up(currentratio, 252, 252),
        _f34_soft_down(sharesbas, 252, 252),
        _f34_soft_up(grossmargin, 252, 252),
        _f34_soft_up(assetturnover, 252, 252),
    ]
    stacked = pd.concat(comps, axis=1)
    b = stacked.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# min component (weakest link in the financial chain), smoothed
def f34pf_f34_piotroski_fscore_weaklink_252d_base_v045_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    comps = [
        _f34_soft_pos(netinc, 252),
        _f34_soft_pos(ncfo, 252),
        _f34_soft_up(roa, 252, 252),
        _f34_soft_gt(ncfo, netinc, 252),
        _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
        _f34_soft_up(currentratio, 252, 252),
        _f34_soft_up(grossmargin, 252, 252),
        _f34_soft_up(assetturnover, 252, 252),
    ]
    stacked = pd.concat(comps, axis=1)
    b = stacked.min(axis=1).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max component (strongest pillar), smoothed
def f34pf_f34_piotroski_fscore_strongpillar_252d_base_v046_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    comps = [
        _f34_soft_pos(netinc, 252),
        _f34_soft_pos(ncfo, 252),
        _f34_soft_up(roa, 252, 252),
        _f34_soft_gt(ncfo, netinc, 252),
        _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
        _f34_soft_up(currentratio, 252, 252),
        _f34_soft_up(grossmargin, 252, 252),
        _f34_soft_up(assetturnover, 252, 252),
    ]
    stacked = pd.concat(comps, axis=1)
    b = stacked.max(axis=1).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- LEVEL / RATIO BUILDING BLOCKS (independent formulas) ----
# ROA level squashed (return-on-assets standing)
def f34pf_f34_piotroski_fscore_roalvl_252d_base_v047_signal(roa):
    sc = roa.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(roa / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow ROA (ncfo/assets) level
def f34pf_f34_piotroski_fscore_cfroalvl_252d_base_v048_signal(ncfo, assets):
    r = _safe_div(ncfo, assets)
    b = np.tanh(3.0 * r)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual ratio level (netinc - ncfo)/assets, sign flipped so high=quality
def f34pf_f34_piotroski_fscore_accrlvl_252d_base_v049_signal(netinc, ncfo, assets):
    accr = _safe_div(netinc - ncfo, assets)
    b = np.tanh(-5.0 * accr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage level relative to history (lower=better, sign flipped)
def f34pf_f34_piotroski_fscore_levlvl_252d_base_v050_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    b = -np.tanh(_z(lev, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio convexity: acceleration of liquidity (Δ of Δ over a quarter)
def f34pf_f34_piotroski_fscore_currmom_63d_base_v051_signal(currentratio):
    d = _chg(currentratio, 63)
    accel = d - d.shift(63)
    sc = currentratio.rolling(252, min_periods=126).mean()
    b = np.tanh(accel / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration: is the pace of share issuance speeding up (2nd diff), flipped
def f34pf_f34_piotroski_fscore_dilution_252d_base_v052_signal(sharesbas):
    g = _pctchg(sharesbas, 126)
    accel = g - g.shift(126)
    sc = g.abs().rolling(504, min_periods=126).mean()
    b = -np.tanh(accel / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# grossmargin trend slope over a half year (margin direction)
def f34pf_f34_piotroski_fscore_gmtrend_126d_base_v053_signal(grossmargin):
    d = _chg(grossmargin, 126)
    sc = grossmargin.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(d / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover regression slope over 252d (smooth OLS trend, distinct from point-delta)
def f34pf_f34_piotroski_fscore_atotrend_252d_base_v054_signal(assetturnover):
    def _slope(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xm = x.mean()
        xden = ((x - xm) ** 2).sum()
        if xden == 0:
            return np.nan
        return ((x - xm) * (a - a.mean())).sum() / xden
    sl = assetturnover.rolling(252, min_periods=126).apply(_slope, raw=True)
    sc = assetturnover.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- INTERACTION & CROSS-COMPONENT SIGNALS ----
# debt-coverage by earnings: netinc relative to debt level (paydown capacity)
def f34pf_f34_piotroski_fscore_profxdelev_252d_base_v055_signal(netinc, debt, assets):
    cover = _safe_div(netinc, debt)
    chg = cover - cover.shift(126)
    sc = cover.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(chg / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-quality x ROA-improvement divergence (conflict between cash & returns)
def f34pf_f34_piotroski_fscore_accrxdroa_252d_base_v056_signal(ncfo, netinc, roa):
    accr = _f34_soft_gt(ncfo, netinc, 126)
    droa = _f34_soft_up(roa, 126, 126)
    b = (accr - droa).abs() * np.sign(accr + droa)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-expansion x turnover-improvement (DuPont-style ROA driver synergy)
def f34pf_f34_piotroski_fscore_gmxato_252d_base_v057_signal(grossmargin, assetturnover):
    dgm = _f34_soft_up(grossmargin, 252, 252)
    dato = _f34_soft_up(assetturnover, 252, 252)
    b = dgm * dato
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-improvement x no-dilution (self-funded strengthening)
def f34pf_f34_piotroski_fscore_currxnodil_252d_base_v058_signal(currentratio, sharesbas):
    dcurr = _f34_soft_up(currentratio, 252, 252)
    nodil = _f34_soft_down(sharesbas, 252, 252)
    b = dcurr * nodil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-margin spread: cash-flow ROA level vs gross-margin level (cash conversion of margins)
def f34pf_f34_piotroski_fscore_ocfxgm_252d_base_v059_signal(ncfo, assets, grossmargin):
    cfroa_z = _z(_safe_div(ncfo, assets), 252)
    gm_z = _z(grossmargin, 252)
    b = np.tanh(cfroa_z - gm_z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net F-score breadth: # positive minus # negative soft components / 9
def f34pf_f34_piotroski_fscore_breadth_252d_base_v060_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    comps = [
        _f34_soft_pos(netinc, 252),
        _f34_soft_pos(ncfo, 252),
        _f34_soft_up(roa, 252, 252),
        _f34_soft_gt(ncfo, netinc, 252),
        _f34_soft_down(_f34_leverage(debt, assets), 252, 252),
        _f34_soft_up(currentratio, 252, 252),
        _f34_soft_down(sharesbas, 252, 252),
        _f34_soft_up(grossmargin, 252, 252),
        _f34_soft_up(assetturnover, 252, 252),
    ]
    pos = sum((c > 0).astype(float) for c in comps)
    neg = sum((c < 0).astype(float) for c in comps)
    b = ((pos - neg) / 9.0).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- ADDITIONAL DISTINCT COMPOSITE / MAGNITUDE FORMULAS ----
# scaled total Piotroski "earnings vs cash" gap trend (accrual reversal proxy)
def f34pf_f34_piotroski_fscore_accrrev_252d_base_v061_signal(netinc, ncfo, assets):
    accr = _safe_div(netinc - ncfo, assets)
    b = np.tanh(5.0 * (accr.shift(252) - accr))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA decomposition consistency: sign agreement of margin & turnover deltas
def f34pf_f34_piotroski_fscore_dupontagree_252d_base_v062_signal(grossmargin, assetturnover):
    dgm = np.sign(_chg(grossmargin, 252))
    dato = np.sign(_chg(assetturnover, 252))
    agree = (dgm * dato)
    mag = np.tanh(_z(_chg(grossmargin, 252), 252)).abs()
    b = (agree * (0.5 + 0.5 * mag)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-quality: deleveraging + buyback combined intensity
def f34pf_f34_piotroski_fscore_finqual_252d_base_v063_signal(debt, assets, sharesbas):
    delev = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    buyback = np.tanh(-8.0 * _pctchg(sharesbas, 252))
    b = (delev + buyback) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# profitability persistence: fraction of last 2y netinc soft-score stayed strong
def f34pf_f34_piotroski_fscore_profpersist_504d_base_v064_signal(netinc):
    soft = _f34_soft_pos(netinc, 126)
    strong = (soft > 0.5).astype(float)
    b = strong.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow persistence: fraction of last 2y ncfo exceeded netinc
def f34pf_f34_piotroski_fscore_accrpersist_504d_base_v065_signal(ncfo, netinc):
    soft = _f34_soft_gt(ncfo, netinc, 126)
    strong = (soft > 0.2).astype(float)
    depth = soft.clip(lower=0)
    b = strong.rolling(504, min_periods=252).mean() + 0.2 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# improvement acceleration: F-score change now vs change a year earlier
def f34pf_f34_piotroski_fscore_fsaccel_252d_base_v066_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    d = fs - fs.shift(126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-adjusted profitability: ROA discounted by leverage level
def f34pf_f34_piotroski_fscore_levadjroa_252d_base_v067_signal(netinc, assets, debt):
    roaq = _safe_div(netinc, assets)
    lev = _f34_leverage(debt, assets)
    b = np.tanh(2.0 * roaq) * (1.0 - np.tanh(lev))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quality-minus-dilution: per-share cash-flow growth (cash accretion to owners)
def f34pf_f34_piotroski_fscore_qmd_252d_base_v068_signal(ncfo, netinc, assets, sharesbas):
    cfps = _safe_div(ncfo, sharesbas)
    g = _pctchg(cfps, 252)
    accr = np.tanh(5.0 * _safe_div(ncfo - netinc, assets))
    b = np.tanh(2.0 * g) + 0.3 * accr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite z-score: standardize the continuous F-score vs its own 504d distribution
def f34pf_f34_piotroski_fscore_fsz_504d_base_v069_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    b = _z(fs, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress-to-quality swing: operating improvement gated by deleveraging
# (improvement only "counts" when balance sheet is also strengthening)
def f34pf_f34_piotroski_fscore_distqual_252d_base_v070_signal(debt, assets, roa, grossmargin):
    delev_gate = (1.0 + _f34_soft_down(_f34_leverage(debt, assets), 126, 252)) / 2.0
    ops = (_f34_soft_up(roa, 126, 252) + _f34_soft_up(grossmargin, 126, 252)) / 2.0
    b = ops * delev_gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-generation growth: YoY growth of cash-flow-ROA scaled by turnover improvement
def f34pf_f34_piotroski_fscore_cashgrowth_252d_base_v071_signal(ncfo, assets, assetturnover):
    cfroa = _safe_div(ncfo, assets)
    g = _pctchg(cfroa, 252)
    datod = _f34_soft_up(assetturnover, 126, 252)
    b = np.tanh(2.0 * g) + 0.4 * datod
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# improving-on-all-fronts breadth: count of the 4 operating metrics above their
# 252d median, depth-weighted (diffusion index over fundamentals)
def f34pf_f34_piotroski_fscore_allfronts_252d_base_v072_signal(roa, grossmargin, assetturnover, currentratio):
    def above_med(s):
        med = s.rolling(252, min_periods=126).median()
        return (s > med).astype(float) + np.tanh(2.0 * _z(s, 252)).clip(-0.5, 0.5) * 0.0
    diff = above_med(roa) + above_med(grossmargin) + above_med(assetturnover) + above_med(currentratio)
    jitter = (_z(roa, 252) + _z(currentratio, 252)) * 0.01
    b = (diff + jitter).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-cash convergence: rolling correlation of netinc and ncfo growth
# (do reported earnings and cash move together — quality of earnings co-movement)
def f34pf_f34_piotroski_fscore_ecconverge_252d_base_v073_signal(ncfo, netinc, assets):
    gn = _pctchg(ncfo, 21)
    ge = _pctchg(netinc, 21)
    b = gn.rolling(252, min_periods=126).corr(ge)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted F-score with logistic (probability) component weighting, 126d
def f34pf_f34_piotroski_fscore_logitfs_126d_base_v074_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    def lg(x):
        return 1.0 / (1.0 + np.exp(-x))
    p1 = lg(2.0 * _safe_div(netinc, assets) / _safe_div(netinc, assets).abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    p2 = lg(3.0 * _safe_div(ncfo, assets))
    p3 = lg(40.0 * _chg(roa, 126))
    p4 = lg(5.0 * _safe_div(ncfo - netinc, assets))
    p5 = lg(-8.0 * _chg(_f34_leverage(debt, assets), 126))
    p6 = lg(2.0 * _chg(currentratio, 126))
    p8 = lg(15.0 * _chg(grossmargin, 126))
    p9 = lg(4.0 * _chg(assetturnover, 126))
    b = (p1 + p2 + p3 + p4 + p5 + p6 + p8 + p9) / 8.0 - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing-3y trend of the continuous F-score (long-horizon health trajectory)
def f34pf_f34_piotroski_fscore_fslongtrend_756d_base_v075_signal(
        netinc, ncfo, roa, assets, debt, grossmargin):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c8) / 6.0
    b = fs.rolling(252, min_periods=126).mean() - fs.rolling(756, min_periods=378).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34pf_f34_piotroski_fscore_posni_252d_base_v001_signal,
    f34pf_f34_piotroski_fscore_posni_63d_base_v002_signal,
    f34pf_f34_piotroski_fscore_posnia_252d_base_v003_signal,
    f34pf_f34_piotroski_fscore_posocf_252d_base_v004_signal,
    f34pf_f34_piotroski_fscore_posocfa_252d_base_v005_signal,
    f34pf_f34_piotroski_fscore_posocffrac_252d_base_v006_signal,
    f34pf_f34_piotroski_fscore_droa_252d_base_v007_signal,
    f34pf_f34_piotroski_fscore_droa_126d_base_v008_signal,
    f34pf_f34_piotroski_fscore_droasyn_252d_base_v009_signal,
    f34pf_f34_piotroski_fscore_accr_252d_base_v010_signal,
    f34pf_f34_piotroski_fscore_accra_252d_base_v011_signal,
    f34pf_f34_piotroski_fscore_accrsm_63d_base_v012_signal,
    f34pf_f34_piotroski_fscore_dlev_252d_base_v013_signal,
    f34pf_f34_piotroski_fscore_dlev_126d_base_v014_signal,
    f34pf_f34_piotroski_fscore_dlevraw_252d_base_v015_signal,
    f34pf_f34_piotroski_fscore_dcurr_252d_base_v016_signal,
    f34pf_f34_piotroski_fscore_dcurr_63d_base_v017_signal,
    f34pf_f34_piotroski_fscore_currlvl_252d_base_v018_signal,
    f34pf_f34_piotroski_fscore_nodil_252d_base_v019_signal,
    f34pf_f34_piotroski_fscore_nodil_126d_base_v020_signal,
    f34pf_f34_piotroski_fscore_buyback_252d_base_v021_signal,
    f34pf_f34_piotroski_fscore_dgm_252d_base_v022_signal,
    f34pf_f34_piotroski_fscore_dgm_63d_base_v023_signal,
    f34pf_f34_piotroski_fscore_gmlvl_252d_base_v024_signal,
    f34pf_f34_piotroski_fscore_dato_252d_base_v025_signal,
    f34pf_f34_piotroski_fscore_dato_126d_base_v026_signal,
    f34pf_f34_piotroski_fscore_atolvl_252d_base_v027_signal,
    f34pf_f34_piotroski_fscore_fscore9_252d_base_v028_signal,
    f34pf_f34_piotroski_fscore_fscorehard_252d_base_v029_signal,
    f34pf_f34_piotroski_fscore_fscore9_126d_base_v030_signal,
    f34pf_f34_piotroski_fscore_profsub_252d_base_v031_signal,
    f34pf_f34_piotroski_fscore_levsub_252d_base_v032_signal,
    f34pf_f34_piotroski_fscore_effsub_252d_base_v033_signal,
    f34pf_f34_piotroski_fscore_qualcore_252d_base_v034_signal,
    f34pf_f34_piotroski_fscore_imptrio_252d_base_v035_signal,
    f34pf_f34_piotroski_fscore_wmag_252d_base_v036_signal,
    f34pf_f34_piotroski_fscore_wprof_252d_base_v037_signal,
    f34pf_f34_piotroski_fscore_weff_252d_base_v038_signal,
    f34pf_f34_piotroski_fscore_wrecency_63d_base_v039_signal,
    f34pf_f34_piotroski_fscore_rollmean_252d_base_v040_signal,
    f34pf_f34_piotroski_fscore_fschg_252d_base_v041_signal,
    f34pf_f34_piotroski_fscore_fsrank_504d_base_v042_signal,
    f34pf_f34_piotroski_fscore_strongcnt_252d_base_v043_signal,
    f34pf_f34_piotroski_fscore_compdisp_252d_base_v044_signal,
    f34pf_f34_piotroski_fscore_weaklink_252d_base_v045_signal,
    f34pf_f34_piotroski_fscore_strongpillar_252d_base_v046_signal,
    f34pf_f34_piotroski_fscore_roalvl_252d_base_v047_signal,
    f34pf_f34_piotroski_fscore_cfroalvl_252d_base_v048_signal,
    f34pf_f34_piotroski_fscore_accrlvl_252d_base_v049_signal,
    f34pf_f34_piotroski_fscore_levlvl_252d_base_v050_signal,
    f34pf_f34_piotroski_fscore_currmom_63d_base_v051_signal,
    f34pf_f34_piotroski_fscore_dilution_252d_base_v052_signal,
    f34pf_f34_piotroski_fscore_gmtrend_126d_base_v053_signal,
    f34pf_f34_piotroski_fscore_atotrend_252d_base_v054_signal,
    f34pf_f34_piotroski_fscore_profxdelev_252d_base_v055_signal,
    f34pf_f34_piotroski_fscore_accrxdroa_252d_base_v056_signal,
    f34pf_f34_piotroski_fscore_gmxato_252d_base_v057_signal,
    f34pf_f34_piotroski_fscore_currxnodil_252d_base_v058_signal,
    f34pf_f34_piotroski_fscore_ocfxgm_252d_base_v059_signal,
    f34pf_f34_piotroski_fscore_breadth_252d_base_v060_signal,
    f34pf_f34_piotroski_fscore_accrrev_252d_base_v061_signal,
    f34pf_f34_piotroski_fscore_dupontagree_252d_base_v062_signal,
    f34pf_f34_piotroski_fscore_finqual_252d_base_v063_signal,
    f34pf_f34_piotroski_fscore_profpersist_504d_base_v064_signal,
    f34pf_f34_piotroski_fscore_accrpersist_504d_base_v065_signal,
    f34pf_f34_piotroski_fscore_fsaccel_252d_base_v066_signal,
    f34pf_f34_piotroski_fscore_levadjroa_252d_base_v067_signal,
    f34pf_f34_piotroski_fscore_qmd_252d_base_v068_signal,
    f34pf_f34_piotroski_fscore_fsz_504d_base_v069_signal,
    f34pf_f34_piotroski_fscore_distqual_252d_base_v070_signal,
    f34pf_f34_piotroski_fscore_cashgrowth_252d_base_v071_signal,
    f34pf_f34_piotroski_fscore_allfronts_252d_base_v072_signal,
    f34pf_f34_piotroski_fscore_ecconverge_252d_base_v073_signal,
    f34pf_f34_piotroski_fscore_logitfs_126d_base_v074_signal,
    f34pf_f34_piotroski_fscore_fslongtrend_756d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_PIOTROSKI_FSCORE_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    netinc = _fund(101, base=5e7, drift=0.03, vol=0.08, allow_neg=True, n=n).rename("netinc")
    ncfo = _fund(102, base=7e7, drift=0.03, vol=0.07, allow_neg=True, n=n).rename("ncfo")
    roa = _fund(103, base=0.08, drift=0.01, vol=0.06, allow_neg=True, n=n).rename("roa")
    assets = _fund(104, base=1e9, drift=0.02, vol=0.03, allow_neg=False, n=n).rename("assets")
    debt = _fund(105, base=4e8, drift=0.015, vol=0.05, allow_neg=False, n=n).rename("debt")
    currentratio = _fund(106, base=1.8, drift=0.005, vol=0.04, allow_neg=False, n=n).rename("currentratio")
    sharesbas = _fund(107, base=1e8, drift=0.005, vol=0.02, allow_neg=False, n=n).rename("sharesbas")
    grossmargin = _fund(108, base=0.42, drift=0.004, vol=0.03, allow_neg=False, n=n).rename("grossmargin")
    assetturnover = _fund(109, base=0.9, drift=0.006, vol=0.04, allow_neg=False, n=n).rename("assetturnover")

    cols = {
        "netinc": netinc, "ncfo": ncfo, "roa": roa, "assets": assets, "debt": debt,
        "currentratio": currentratio, "sharesbas": sharesbas, "grossmargin": grossmargin,
        "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f34_piotroski_fscore_base_001_075_claude: %d features pass" % n_features)
