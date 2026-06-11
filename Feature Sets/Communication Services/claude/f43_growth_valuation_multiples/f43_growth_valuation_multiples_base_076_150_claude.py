import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _pctl_of_last(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda a: (a <= a[-1]).mean(), raw=True)


# ===== folder domain primitives (growth valuation multiples) =====
def _f43gv_evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _f43gv_ps(ps):
    return ps.clip(lower=0)


def _f43gv_mcap_sales(marketcap, revenue):
    return marketcap / revenue.replace(0, np.nan)


def _f43gv_log_evsales(ev, revenue):
    return np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))


def _f43gv_log_ps(ps):
    return np.log(_f43gv_ps(ps).clip(lower=1e-6))


def _f43gv_log_evebitda(evebitda):
    return np.log(evebitda.clip(lower=1e-6))


def _f43gv_log_pe(pe):
    return np.log(pe.clip(lower=1e-6))


def _f43gv_cheap_z(level, w):
    return -_z(level, w)


def _f43gv_cheap_rank(level, w):
    return -(_rank(level, w))


# ============================================================
# EV/Sales cheapness z (126d short memory) -- fast value signal
def f43gv_f43_growth_valuation_multiples_evsales_cheapz_126d_base_v076_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _f43gv_cheap_z(es, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness rank (504d long memory)
def f43gv_f43_growth_valuation_multiples_evsales_cheaprank_504d_base_v077_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _f43gv_cheap_rank(es, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales level vs market-cap/sales blend (enterprise vs equity sales multiple avg)
def f43gv_f43_growth_valuation_multiples_evs_mcaps_blendlvl_base_v078_signal(ev, marketcap, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    ms = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    b = (es + ms) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales 252d trend (slow re-rating)
def f43gv_f43_growth_valuation_multiples_evsales_trend_252d_base_v079_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    b = _slope(es, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales 21d displacement from 252d mean (stretch from long anchor)
def f43gv_f43_growth_valuation_multiples_evsales_stretch_base_v080_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    b = es - _mean(es, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness composite: average of 126d and 504d cheap z (multi-horizon value)
def f43gv_f43_growth_valuation_multiples_evsales_multihz_z_base_v081_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = (_f43gv_cheap_z(es, 126) + _f43gv_cheap_z(es, 504)) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness z (504d long memory)
def f43gv_f43_growth_valuation_multiples_ps_cheapz_504d_base_v082_signal(ps):
    b = _f43gv_cheap_z(_f43gv_ps(ps), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness rank (252d)
def f43gv_f43_growth_valuation_multiples_ps_cheaprank_252d_base_v083_signal(ps):
    b = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S 126d trend (medium re-rating)
def f43gv_f43_growth_valuation_multiples_ps_trend_126d_base_v084_signal(ps):
    lps = _f43gv_log_ps(ps)
    b = _slope(lps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S displacement from slow EMA (short de-trended richness)
def f43gv_f43_growth_valuation_multiples_ps_disp_base_v085_signal(ps):
    lps = _f43gv_log_ps(ps)
    b = lps - lps.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S dispersion (volatility of the multiple) over 252d
def f43gv_f43_growth_valuation_multiples_ps_dispersion_base_v086_signal(ps):
    lps = _f43gv_log_ps(ps)
    b = _std(lps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness z (126d)
def f43gv_f43_growth_valuation_multiples_evebitda_cheapz_126d_base_v087_signal(evebitda):
    b = _f43gv_cheap_z(evebitda, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness rank (504d)
def f43gv_f43_growth_valuation_multiples_evebitda_cheaprank_504d_base_v088_signal(evebitda):
    b = _f43gv_cheap_rank(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 252d trend
def f43gv_f43_growth_valuation_multiples_evebitda_trend_252d_base_v089_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    b = _slope(le, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA stretch from 252d mean
def f43gv_f43_growth_valuation_multiples_evebitda_stretch_base_v090_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    b = le - _mean(le, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness z (504d)
def f43gv_f43_growth_valuation_multiples_pe_cheapz_504d_base_v091_signal(pe):
    b = _f43gv_cheap_z(pe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness rank (252d)
def f43gv_f43_growth_valuation_multiples_pe_cheaprank_252d_base_v092_signal(pe):
    b = _f43gv_cheap_rank(pe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E 63d trend
def f43gv_f43_growth_valuation_multiples_pe_trend_63d_base_v093_signal(pe):
    lpe = _f43gv_log_pe(pe)
    b = _slope(lpe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E stretch from 252d mean
def f43gv_f43_growth_valuation_multiples_pe_stretch_base_v094_signal(pe):
    lpe = _f43gv_log_pe(pe)
    b = lpe - _mean(lpe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness z: P/S + EV/EBITDA (equity-sales + enterprise-profit cheapness)
def f43gv_f43_growth_valuation_multiples_blend_ps_evebitda_z_base_v095_signal(ps, evebitda):
    z1 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z2 = _f43gv_cheap_z(evebitda, 252)
    b = (z1 + z2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness z: EV/Sales + P/E (growth-sales + earnings cheapness)
def f43gv_f43_growth_valuation_multiples_blend_evs_pe_z_base_v096_signal(ev, revenue, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(pe, 252)
    b = (z1 + z2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness rank: P/S + P/E + EV/EBITDA (triple composite)
def f43gv_f43_growth_valuation_multiples_blend_triple_rank_base_v097_signal(ps, pe, evebitda):
    r1 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    r2 = _f43gv_cheap_rank(pe, 252)
    r3 = _f43gv_cheap_rank(evebitda, 252)
    b = (r1 + r2 + r3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales over P/E ratio (enterprise-sales vs equity-earnings richness, log)
def f43gv_f43_growth_valuation_multiples_evs_pe_ratio_base_v098_signal(ev, revenue, pe):
    es = _f43gv_log_evsales(ev, revenue)
    lpe = _f43gv_log_pe(pe)
    b = es - lpe
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales over EV/EBITDA spread (equity-sales vs enterprise-profit)
def f43gv_f43_growth_valuation_multiples_mcaps_evebitda_spread_base_v099_signal(marketcap, revenue, evebitda):
    ms = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    le = _f43gv_log_evebitda(evebitda)
    b = ms - le
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales re-rating direction relative to P/S re-rating (multiple divergence trend)
def f43gv_f43_growth_valuation_multiples_evs_ps_trenddiv_base_v100_signal(ev, revenue, ps):
    t1 = _slope(_f43gv_log_evsales(ev, revenue), 63)
    t2 = _slope(_f43gv_log_ps(ps), 63)
    b = t1 - t2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA re-rating vs P/E re-rating divergence
def f43gv_f43_growth_valuation_multiples_evebitda_pe_trenddiv_base_v101_signal(evebitda, pe):
    t1 = _slope(_f43gv_log_evebitda(evebitda), 63)
    t2 = _slope(_f43gv_log_pe(pe), 63)
    b = t1 - t2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness acceleration (cheapz 504d change over half year)
def f43gv_f43_growth_valuation_multiples_evsales_cheapaccel_base_v102_signal(ev, revenue):
    cz = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 504)
    b = cz - cz.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness acceleration
def f43gv_f43_growth_valuation_multiples_evebitda_cheapaccel_base_v103_signal(evebitda):
    cz = _f43gv_cheap_z(evebitda, 504)
    b = cz - cz.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness acceleration
def f43gv_f43_growth_valuation_multiples_pe_cheapaccel_base_v104_signal(pe):
    cz = _f43gv_cheap_z(pe, 504)
    b = cz - cz.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales tanh-squashed cheapness rank (bounded cheap signal)
def f43gv_f43_growth_valuation_multiples_evsales_cheaptanh_base_v105_signal(ev, revenue):
    cr = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    b = np.tanh(3.0 * cr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness interacted with re-rating momentum (cheap & re-rating up)
def f43gv_f43_growth_valuation_multiples_evsales_cheapxmom_base_v106_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    cheap = -_z(es, 252)
    mom = es - es.shift(126)
    b = cheap * np.tanh(4.0 * mom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness interacted with multiple stability (cheap & stable = quality value)
def f43gv_f43_growth_valuation_multiples_ps_cheapxstable_base_v107_signal(ps):
    lps = _f43gv_log_ps(ps)
    cheap = -_z(lps, 252)
    instab = _std(lps, 126)
    b = cheap / (1.0 + 4.0 * instab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cheapness z dispersion across EV/Sales, P/S, P/E (valuation disagreement)
def f43gv_f43_growth_valuation_multiples_blend_zdisp3_base_v108_signal(ev, revenue, ps, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(pe, 252)
    b = pd.concat([z1, z2, z3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheapness composite minmax spread (most-cheap minus least-cheap multiple z)
def f43gv_f43_growth_valuation_multiples_blend_zspread_base_v109_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(evebitda, 252)
    z4 = _f43gv_cheap_z(pe, 252)
    stacked = pd.concat([z1, z2, z3, z4], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales fraction-of-year in cheap regime (depth-weighted below mean)
def f43gv_f43_growth_valuation_multiples_evsales_cheapdepth_base_v110_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    depth = (_mean(es, 252) - es).clip(lower=0)
    b = depth.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E fraction-of-year in rich regime (depth-weighted above mean)
def f43gv_f43_growth_valuation_multiples_pe_richdepth_base_v111_signal(pe):
    lpe = _f43gv_log_pe(pe)
    depth = (lpe - _mean(lpe, 252)).clip(lower=0)
    b = depth.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales re-rating efficiency: net drift over absolute path traveled (252d)
def f43gv_f43_growth_valuation_multiples_evsales_rerate_eff_base_v112_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    net = (es - es.shift(252)).abs()
    path = es.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA re-rating efficiency
def f43gv_f43_growth_valuation_multiples_evebitda_rerate_eff_base_v113_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    net = (le - le.shift(252)).abs()
    path = le.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales multiple vol-of-vol (instability of multiple instability)
def f43gv_f43_growth_valuation_multiples_evsales_volofvol_base_v114_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    vol = _std(es.diff(), 63)
    b = _std(vol, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z minus P/S cheapness z (capital-structure cheapness tilt)
def f43gv_f43_growth_valuation_multiples_evs_ps_cheapzgap_base_v115_signal(ev, revenue, ps):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    b = z1 - z2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness z minus EV/EBITDA cheapness z (equity vs enterprise profit cheapness)
def f43gv_f43_growth_valuation_multiples_pe_evebitda_cheapzgap_base_v116_signal(pe, evebitda):
    z1 = _f43gv_cheap_z(pe, 252)
    z2 = _f43gv_cheap_z(evebitda, 252)
    b = z1 - z2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales smoothed cheapness rank (persistent value tilt)
def f43gv_f43_growth_valuation_multiples_evsales_cheaprank_sm_base_v117_signal(ev, revenue):
    cr = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    b = cr.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA smoothed cheapness z (persistent value tilt)
def f43gv_f43_growth_valuation_multiples_evebitda_cheapz_sm_base_v118_signal(evebitda):
    cz = _f43gv_cheap_z(evebitda, 252)
    b = cz.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales year-over-year cheapness rank change (value regime shift)
def f43gv_f43_growth_valuation_multiples_evsales_rankyoy_base_v119_signal(ev, revenue):
    cr = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    b = cr - cr.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales implied net-debt premium: EV/Sales minus mcap/Sales scaled by mcap/Sales
def f43gv_f43_growth_valuation_multiples_evsales_netdebt_prem_base_v120_signal(ev, marketcap, revenue):
    es = _f43gv_evsales(ev, revenue)
    ms = _f43gv_mcap_sales(marketcap, revenue)
    b = (es - ms) / ms.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt premium trend over a quarter (leverage re-pricing)
def f43gv_f43_growth_valuation_multiples_netdebt_prem_trend_base_v121_signal(ev, marketcap, revenue):
    es = _f43gv_evsales(ev, revenue)
    ms = _f43gv_mcap_sales(marketcap, revenue)
    prem = (es - ms) / ms.replace(0, np.nan)
    b = _slope(prem, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cheapness z (all four) smoothed -- durable value score
def f43gv_f43_growth_valuation_multiples_blend_quad_z_sm_base_v122_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(evebitda, 252)
    z4 = _f43gv_cheap_z(pe, 252)
    comp = (z1 + z2 + z3 + z4) / 4.0
    b = comp.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cheapness rank (all four) slope over half year
def f43gv_f43_growth_valuation_multiples_blend_quad_rank_slope_base_v123_signal(ev, revenue, ps, evebitda, pe):
    r1 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    r2 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    r3 = _f43gv_cheap_rank(evebitda, 252)
    r4 = _f43gv_cheap_rank(pe, 252)
    comp = (r1 + r2 + r3 + r4) / 4.0
    b = _slope(comp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales drawup: distance above its trailing 252d minimum (re-rating extension)
def f43gv_f43_growth_valuation_multiples_evsales_drawup_base_v124_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    lo = es.rolling(252, min_periods=126).min()
    b = es - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales drawdown: distance below its trailing 252d maximum (de-rating depth)
def f43gv_f43_growth_valuation_multiples_evsales_drawdn_base_v125_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    b = es - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales position within its own 252d high-low band (multiple range position)
def f43gv_f43_growth_valuation_multiples_evsales_bandpos_base_v126_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    b = (es - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA position within its own 252d band
def f43gv_f43_growth_valuation_multiples_evebitda_bandpos_base_v127_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    hi = le.rolling(252, min_periods=126).max()
    lo = le.rolling(252, min_periods=126).min()
    b = (le - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S band-position momentum: change in 252d band position over a quarter
def f43gv_f43_growth_valuation_multiples_ps_bandpos_base_v128_signal(ps):
    lps = _f43gv_log_ps(ps)
    hi = lps.rolling(252, min_periods=126).max()
    lo = lps.rolling(252, min_periods=126).min()
    pos = (lps - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales band-amplitude (multiple range width / scale) over 252d
def f43gv_f43_growth_valuation_multiples_evsales_bandamp_base_v129_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales mean-reversion half-life proxy: autocorr-ish lag-1 of multiple changes
def f43gv_f43_growth_valuation_multiples_evsales_revspeed_base_v130_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    d = es.diff()
    cov = (d * d.shift(1)).rolling(126, min_periods=63).mean()
    var = (d * d).rolling(126, min_periods=63).mean().replace(0, np.nan)
    b = -(cov / var)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended EV/Sales+EV/EBITDA enterprise cheapness z (enterprise-only value)
def f43gv_f43_growth_valuation_multiples_enterprise_cheapz_base_v131_signal(ev, revenue, evebitda):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(evebitda, 252)
    b = (z1 + z2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended P/S+P/E equity cheapness z (equity-only value)
def f43gv_f43_growth_valuation_multiples_equity_cheapz_base_v132_signal(ps, pe):
    z1 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z2 = _f43gv_cheap_z(pe, 252)
    b = (z1 + z2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise-minus-equity cheapness (capital-structure value tilt composite)
def f43gv_f43_growth_valuation_multiples_ent_eq_cheapgap_base_v133_signal(ev, revenue, evebitda, ps, pe):
    ent = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
           + _f43gv_cheap_z(evebitda, 252)) / 2.0
    eq = (_f43gv_cheap_z(_f43gv_ps(ps), 252)
          + _f43gv_cheap_z(pe, 252)) / 2.0
    b = ent - eq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z relative to its own 126d trailing average (cheapness surprise)
def f43gv_f43_growth_valuation_multiples_evsales_cheapsurprise_base_v134_signal(ev, revenue):
    cz = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    b = cz - cz.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness surprise
def f43gv_f43_growth_valuation_multiples_evebitda_cheapsurprise_base_v135_signal(evebitda):
    cz = _f43gv_cheap_z(evebitda, 252)
    b = cz - cz.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales multiple skewness over 252d (asymmetry of re-rating regime)
def f43gv_f43_growth_valuation_multiples_evsales_skew_base_v136_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    b = es.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E multiple skewness over 252d
def f43gv_f43_growth_valuation_multiples_pe_skew_base_v137_signal(pe):
    lpe = _f43gv_log_pe(pe)
    b = lpe.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness x band-position interaction (deep value at band bottom)
def f43gv_f43_growth_valuation_multiples_evsales_cheapxband_base_v138_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    pos = (es - lo) / (hi - lo).replace(0, np.nan)
    cheap = -_z(es, 252)
    b = cheap * (1.0 - pos)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales cheapness z (504d)
def f43gv_f43_growth_valuation_multiples_mcapsales_cheapz_504d_base_v139_signal(marketcap, revenue):
    ms = _f43gv_mcap_sales(marketcap, revenue)
    b = _f43gv_cheap_z(ms, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales 126d trend
def f43gv_f43_growth_valuation_multiples_mcapsales_trend_126d_base_v140_signal(marketcap, revenue):
    ms = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    b = _slope(ms, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z gated by low re-rating volatility (stable cheap)
def f43gv_f43_growth_valuation_multiples_evsales_stablecheap_base_v141_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    cheap = -_z(es, 252)
    vol = _std(es.diff(), 126)
    gate = 1.0 / (1.0 + (vol / vol.rolling(252, min_periods=126).median().replace(0, np.nan)))
    b = cheap * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness rank x trend (cheap & re-rating up)
def f43gv_f43_growth_valuation_multiples_evebitda_cheapxtrend_base_v142_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    cr = -_rank(le, 252)
    tr = _slope(le, 63)
    b = cr * np.tanh(4.0 * tr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness rank x trend
def f43gv_f43_growth_valuation_multiples_pe_cheapxtrend_base_v143_signal(pe):
    lpe = _f43gv_log_pe(pe)
    cr = -_rank(lpe, 252)
    tr = _slope(lpe, 63)
    b = cr * np.tanh(4.0 * tr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales 5d weekly re-rate momentum (fast multiple shock)
def f43gv_f43_growth_valuation_multiples_evsales_wkmom_base_v144_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    b = es - es.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 5d weekly re-rate momentum
def f43gv_f43_growth_valuation_multiples_evebitda_wkmom_base_v145_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    b = le - le.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cheapness z (enterprise) vs its own 252d band position (where value sits)
def f43gv_f43_growth_valuation_multiples_entz_bandpos_base_v146_signal(ev, revenue, evebitda):
    comp = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
            + _f43gv_cheap_z(evebitda, 252)) / 2.0
    hi = comp.rolling(252, min_periods=126).max()
    lo = comp.rolling(252, min_periods=126).min()
    b = (comp - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness percentile convexity: 252d-pctl deviation from neutral, squared-signed
def f43gv_f43_growth_valuation_multiples_evsales_cheappctldepth_base_v147_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    pct = _pctl_of_last(es, 252)
    dev = 0.5 - pct
    b = np.sign(dev) * (dev ** 2) * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness x P/S cheapness agreement (both-cheap product)
def f43gv_f43_growth_valuation_multiples_evs_ps_cheapagree_base_v148_signal(ev, revenue, ps):
    c1 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    c2 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    b = np.sign(c1) * np.sign(c2) * (c1.abs() + c2.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness x P/E cheapness agreement (both-cheap profit value)
def f43gv_f43_growth_valuation_multiples_evebitda_pe_cheapagree_base_v149_signal(evebitda, pe):
    c1 = _f43gv_cheap_rank(evebitda, 252)
    c2 = _f43gv_cheap_rank(pe, 252)
    b = np.sign(c1) * np.sign(c2) * (c1.abs() + c2.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full composite cheapness z interacted with re-rating direction of EV/Sales (value + catalyst)
def f43gv_f43_growth_valuation_multiples_blend_value_catalyst_base_v150_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(evebitda, 252)
    z4 = _f43gv_cheap_z(pe, 252)
    value = (z1 + z2 + z3 + z4) / 4.0
    es = _f43gv_log_evsales(ev, revenue)
    catalyst = np.tanh(4.0 * (es - es.shift(63)))
    b = value + 0.5 * value * catalyst
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43gv_f43_growth_valuation_multiples_evsales_cheapz_126d_base_v076_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheaprank_504d_base_v077_signal,
    f43gv_f43_growth_valuation_multiples_evs_mcaps_blendlvl_base_v078_signal,
    f43gv_f43_growth_valuation_multiples_evsales_trend_252d_base_v079_signal,
    f43gv_f43_growth_valuation_multiples_evsales_stretch_base_v080_signal,
    f43gv_f43_growth_valuation_multiples_evsales_multihz_z_base_v081_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheapz_504d_base_v082_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheaprank_252d_base_v083_signal,
    f43gv_f43_growth_valuation_multiples_ps_trend_126d_base_v084_signal,
    f43gv_f43_growth_valuation_multiples_ps_disp_base_v085_signal,
    f43gv_f43_growth_valuation_multiples_ps_dispersion_base_v086_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapz_126d_base_v087_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheaprank_504d_base_v088_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_trend_252d_base_v089_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_stretch_base_v090_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheapz_504d_base_v091_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheaprank_252d_base_v092_signal,
    f43gv_f43_growth_valuation_multiples_pe_trend_63d_base_v093_signal,
    f43gv_f43_growth_valuation_multiples_pe_stretch_base_v094_signal,
    f43gv_f43_growth_valuation_multiples_blend_ps_evebitda_z_base_v095_signal,
    f43gv_f43_growth_valuation_multiples_blend_evs_pe_z_base_v096_signal,
    f43gv_f43_growth_valuation_multiples_blend_triple_rank_base_v097_signal,
    f43gv_f43_growth_valuation_multiples_evs_pe_ratio_base_v098_signal,
    f43gv_f43_growth_valuation_multiples_mcaps_evebitda_spread_base_v099_signal,
    f43gv_f43_growth_valuation_multiples_evs_ps_trenddiv_base_v100_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_pe_trenddiv_base_v101_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapaccel_base_v102_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapaccel_base_v103_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheapaccel_base_v104_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheaptanh_base_v105_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapxmom_base_v106_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheapxstable_base_v107_signal,
    f43gv_f43_growth_valuation_multiples_blend_zdisp3_base_v108_signal,
    f43gv_f43_growth_valuation_multiples_blend_zspread_base_v109_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapdepth_base_v110_signal,
    f43gv_f43_growth_valuation_multiples_pe_richdepth_base_v111_signal,
    f43gv_f43_growth_valuation_multiples_evsales_rerate_eff_base_v112_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_rerate_eff_base_v113_signal,
    f43gv_f43_growth_valuation_multiples_evsales_volofvol_base_v114_signal,
    f43gv_f43_growth_valuation_multiples_evs_ps_cheapzgap_base_v115_signal,
    f43gv_f43_growth_valuation_multiples_pe_evebitda_cheapzgap_base_v116_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheaprank_sm_base_v117_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapz_sm_base_v118_signal,
    f43gv_f43_growth_valuation_multiples_evsales_rankyoy_base_v119_signal,
    f43gv_f43_growth_valuation_multiples_evsales_netdebt_prem_base_v120_signal,
    f43gv_f43_growth_valuation_multiples_netdebt_prem_trend_base_v121_signal,
    f43gv_f43_growth_valuation_multiples_blend_quad_z_sm_base_v122_signal,
    f43gv_f43_growth_valuation_multiples_blend_quad_rank_slope_base_v123_signal,
    f43gv_f43_growth_valuation_multiples_evsales_drawup_base_v124_signal,
    f43gv_f43_growth_valuation_multiples_evsales_drawdn_base_v125_signal,
    f43gv_f43_growth_valuation_multiples_evsales_bandpos_base_v126_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_bandpos_base_v127_signal,
    f43gv_f43_growth_valuation_multiples_ps_bandpos_base_v128_signal,
    f43gv_f43_growth_valuation_multiples_evsales_bandamp_base_v129_signal,
    f43gv_f43_growth_valuation_multiples_evsales_revspeed_base_v130_signal,
    f43gv_f43_growth_valuation_multiples_enterprise_cheapz_base_v131_signal,
    f43gv_f43_growth_valuation_multiples_equity_cheapz_base_v132_signal,
    f43gv_f43_growth_valuation_multiples_ent_eq_cheapgap_base_v133_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapsurprise_base_v134_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapsurprise_base_v135_signal,
    f43gv_f43_growth_valuation_multiples_evsales_skew_base_v136_signal,
    f43gv_f43_growth_valuation_multiples_pe_skew_base_v137_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapxband_base_v138_signal,
    f43gv_f43_growth_valuation_multiples_mcapsales_cheapz_504d_base_v139_signal,
    f43gv_f43_growth_valuation_multiples_mcapsales_trend_126d_base_v140_signal,
    f43gv_f43_growth_valuation_multiples_evsales_stablecheap_base_v141_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapxtrend_base_v142_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheapxtrend_base_v143_signal,
    f43gv_f43_growth_valuation_multiples_evsales_wkmom_base_v144_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_wkmom_base_v145_signal,
    f43gv_f43_growth_valuation_multiples_entz_bandpos_base_v146_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheappctldepth_base_v147_signal,
    f43gv_f43_growth_valuation_multiples_evs_ps_cheapagree_base_v148_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_pe_cheapagree_base_v149_signal,
    f43gv_f43_growth_valuation_multiples_blend_value_catalyst_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_GROWTH_VALUATION_MULTIPLES_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    ps = _fund(1, base=8.0, drift=0.0, vol=0.16).clip(lower=0.5).rename("ps")
    evebitda = _fund(2, base=18.0, drift=0.0, vol=0.18).clip(lower=1.0).rename("evebitda")
    pe = _fund(3, base=28.0, drift=0.0, vol=0.20).clip(lower=1.0).rename("pe")
    ev = _fund(4, base=1.2e9, drift=0.02, vol=0.10).rename("ev")
    marketcap = _fund(5, base=1.0e9, drift=0.02, vol=0.10).rename("marketcap")
    revenue = _fund(6, base=2.0e8, drift=0.02, vol=0.07).clip(lower=1e6).rename("revenue")
    ebitda = _fund(7, base=3.0e7, drift=0.01, vol=0.14, allow_neg=True).rename("ebitda")

    cols = {"ps": ps, "evebitda": evebitda, "pe": pe, "ev": ev,
            "marketcap": marketcap, "revenue": revenue, "ebitda": ebitda}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f43_growth_valuation_multiples_base_076_150_claude: %d features pass" % n_features)
