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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== f44 ownership / institutional-accumulation primitives =====
def _f44ia_own_pct(totalvalue, marketcap):
    # institutional ownership fraction = aggregate 13F value / market cap
    return totalvalue / marketcap.replace(0, np.nan)


def _f44ia_value_per_holder(totalvalue, shrholders):
    # average dollar value held per institutional holder (conviction size)
    return totalvalue / shrholders.replace(0, np.nan)


def _f44ia_units_per_holder(shrunits, shrholders):
    # average share units held per institution (position size in shares)
    return shrunits / shrholders.replace(0, np.nan)


def _f44ia_implied_price(totalvalue, shrunits):
    # implied price institutions are marked at = value / units
    return totalvalue / shrunits.replace(0, np.nan)


def _f44ia_breadth_trend(shrholders, w):
    # net change in holder count over window (accumulation breadth)
    return shrholders - shrholders.shift(w)


# ============================================================
# inst holder-count level z-scored vs its own 252d history (breadth extremity)
def f44ia_f44_institutional_accumulation_holdersz_252d_base_v001_signal(shrholders):
    b = _z(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst holder-count quarterly growth (accumulation breadth momentum)
def f44ia_f44_institutional_accumulation_holdersgr_63d_base_v002_signal(shrholders):
    b = _logroc(shrholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst holder-count year-over-year growth (long-horizon breadth ramp)
def f44ia_f44_institutional_accumulation_holdersgr_252d_base_v003_signal(shrholders):
    b = _logroc(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count percentile-rank vs own 504d history (where breadth sits in cycle)
def f44ia_f44_institutional_accumulation_holdersrank_504d_base_v004_signal(shrholders):
    b = _rank(shrholders, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aggregate inst value level, log-detrended vs its 252d mean (value extremity)
def f44ia_f44_institutional_accumulation_valz_252d_base_v005_signal(totalvalue):
    lv = np.log(totalvalue.replace(0, np.nan))
    b = _z(lv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aggregate inst value quarterly growth (smart-money dollar inflow momentum)
def f44ia_f44_institutional_accumulation_valgr_63d_base_v006_signal(totalvalue):
    b = _logroc(totalvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aggregate inst value yearly growth (multi-quarter ownership-value ramp)
def f44ia_f44_institutional_accumulation_valgr_252d_base_v007_signal(totalvalue):
    b = _logroc(totalvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership pct = totalvalue / marketcap (level)
def f44ia_f44_institutional_accumulation_ownpct_base_v008_signal(totalvalue, marketcap):
    b = _f44ia_own_pct(totalvalue, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# institutional ownership pct z-scored vs its 252d history (ownership extremity)
def f44ia_f44_institutional_accumulation_ownpctz_252d_base_v009_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = _z(op, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in inst ownership pct over a quarter (accumulation vs marketcap)
def f44ia_f44_institutional_accumulation_ownpctchg_63d_base_v010_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = op - op.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst share-units held quarterly growth (true accumulation in shares)
def f44ia_f44_institutional_accumulation_unitsgr_63d_base_v011_signal(shrunits):
    b = _logroc(shrunits, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst share-units held yearly growth (long-horizon share accumulation)
def f44ia_f44_institutional_accumulation_unitsgr_252d_base_v012_signal(shrunits):
    b = _logroc(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst units level z-scored vs 252d (position-size extremity)
def f44ia_f44_institutional_accumulation_unitsz_252d_base_v013_signal(shrunits):
    lu = np.log(shrunits.replace(0, np.nan))
    b = _z(lu, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average value per holder (conviction-size level), log
def f44ia_f44_institutional_accumulation_valperhold_base_v014_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    b = np.log(vph.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder quarterly growth (rising conviction per institution)
def f44ia_f44_institutional_accumulation_valperholdgr_63d_base_v015_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    b = _logroc(vph, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder level (avg share position per institution), log
def f44ia_f44_institutional_accumulation_unitsperhold_base_v016_signal(shrunits, shrholders):
    uph = _f44ia_units_per_holder(shrunits, shrholders)
    b = np.log(uph.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder quarterly growth (position-size accumulation per holder)
def f44ia_f44_institutional_accumulation_unitsperholdgr_63d_base_v017_signal(shrunits, shrholders):
    uph = _f44ia_units_per_holder(shrunits, shrholders)
    b = _logroc(uph, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-investor shrvalue level relative to its 252d mean (single-filing value bias)
def f44ia_f44_institutional_accumulation_shrvalz_252d_base_v018_signal(shrvalue):
    lv = np.log(shrvalue.replace(0, np.nan))
    b = _z(lv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue quarterly growth (representative-holder value inflow)
def f44ia_f44_institutional_accumulation_shrvalgr_63d_base_v019_signal(shrvalue):
    b = _logroc(shrvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue share of aggregate value = shrvalue/totalvalue (top-holder concentration)
def f44ia_f44_institutional_accumulation_shrvalshare_base_v020_signal(shrvalue, totalvalue):
    b = shrvalue / totalvalue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in shrvalue-share over a quarter (concentration trend among institutions)
def f44ia_f44_institutional_accumulation_shrvalsharechg_63d_base_v021_signal(shrvalue, totalvalue):
    share = shrvalue / totalvalue.replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum regime: monthly value-minus-marketcap growth, z-scored vs 252d
def f44ia_f44_institutional_accumulation_valexmktgr_63d_base_v022_signal(totalvalue, marketcap):
    spread = _logroc(totalvalue, 21) - _logroc(marketcap, 21)
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied price institutions hold at (value/units), yearly growth (mark-up rate)
def f44ia_f44_institutional_accumulation_implpxgr_252d_base_v023_signal(totalvalue, shrunits):
    ip = _f44ia_implied_price(totalvalue, shrunits)
    b = _logroc(ip, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units growth minus value growth = pure share-count accumulation ex-mark (real inflow)
def f44ia_f44_institutional_accumulation_unitexvalgr_63d_base_v024_signal(shrunits, totalvalue):
    b = _logroc(shrunits, 63) - _logroc(totalvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-vs-size regime: z-score of holders-to-units ratio (broad vs concentrated base)
def f44ia_f44_institutional_accumulation_breadthsizediv_63d_base_v025_signal(shrholders, shrunits):
    ratio = np.log((shrholders / shrunits.replace(0, np.nan)).replace(0, np.nan))
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count short vs long trend spread (accelerating breadth)
def f44ia_f44_institutional_accumulation_holdtrendspr_base_v026_signal(shrholders):
    short = _logroc(shrholders, 21)
    long = _logroc(shrholders, 126)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value short vs long trend spread (accelerating dollar inflow)
def f44ia_f44_institutional_accumulation_valtrendspr_base_v027_signal(totalvalue):
    short = _logroc(totalvalue, 21)
    long = _logroc(totalvalue, 126)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership pct percentile-rank vs 504d history (cheap/crowded ownership)
def f44ia_f44_institutional_accumulation_ownpctrank_504d_base_v028_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = _rank(op, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow: 21d EMA of inst-value short growth (smoothed momentum)
def f44ia_f44_institutional_accumulation_valinflow_ema_base_v029_signal(totalvalue):
    g = _logroc(totalvalue, 5)
    b = g.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak: fraction of last quarter with rising holder count
def f44ia_f44_institutional_accumulation_holdupfrac_63d_base_v030_signal(shrholders):
    up = (shrholders.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak: fraction of last quarter with rising inst units
def f44ia_f44_institutional_accumulation_unitupfrac_63d_base_v031_signal(shrunits):
    up = (shrunits.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder z vs 252d (conviction extremity, de-trended)
def f44ia_f44_institutional_accumulation_valperholdz_252d_base_v032_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    lv = np.log(vph.replace(0, np.nan))
    b = _z(lv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year ownership pct change scaled by its volatility (risk-adj accumulation)
def f44ia_f44_institutional_accumulation_ownpctriskadj_126d_base_v033_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    chg = op - op.shift(126)
    vol = op.diff().rolling(126, min_periods=63).std()
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst units percentile-rank vs 504d (share-base accumulation position)
def f44ia_f44_institutional_accumulation_unitsrank_504d_base_v034_signal(shrunits):
    b = _rank(shrunits, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value growth risk-adjusted: 63d value growth / its 126d vol (clean inflow signal)
def f44ia_f44_institutional_accumulation_valgrriskadj_base_v035_signal(totalvalue):
    g = _logroc(totalvalue, 63)
    vol = _logroc(totalvalue, 5).rolling(126, min_periods=63).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count acceleration over a month (breadth velocity change)
def f44ia_f44_institutional_accumulation_holdaccel_21d_base_v036_signal(shrholders):
    g = _logroc(shrholders, 21)
    b = g - g.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed units acceleration (bounded change in monthly accumulation pace)
def f44ia_f44_institutional_accumulation_unitstanh_63d_base_v037_signal(shrunits):
    g = _logroc(shrunits, 21)
    acc = g - g.shift(21)
    b = np.tanh(15.0 * acc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of inst ownership pct from its 252d max (room left to crowd in)
def f44ia_f44_institutional_accumulation_ownpctheadroom_252d_base_v038_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    mx = _rmax(op, 252)
    b = op / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery of inst ownership pct off its 252d trough (re-accumulation off lows)
def f44ia_f44_institutional_accumulation_ownpctrecov_252d_base_v039_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    mn = _rmin(op, 252)
    b = op / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied-price (value/units) momentum scaled by units-per-holder level (mark vs size)
def f44ia_f44_institutional_accumulation_convmixspr_63d_base_v040_signal(totalvalue, shrunits, shrholders):
    ip = _f44ia_implied_price(totalvalue, shrunits)
    uph = _f44ia_units_per_holder(shrunits, shrholders)
    b = _logroc(ip, 126) * _rank(uph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue per-investor risk-adjusted quarterly growth
def f44ia_f44_institutional_accumulation_shrvalgrriskadj_base_v041_signal(shrvalue):
    g = _logroc(shrvalue, 63)
    vol = _logroc(shrvalue, 5).rolling(126, min_periods=63).std()
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count position in its 252d range (breadth cycle phase)
def f44ia_f44_institutional_accumulation_holdrngpos_252d_base_v042_signal(shrholders):
    hi = _rmax(shrholders, 252)
    lo = _rmin(shrholders, 252)
    b = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value position in its 504d range (dollar-ownership cycle phase)
def f44ia_f44_institutional_accumulation_valrngpos_504d_base_v043_signal(totalvalue):
    hi = _rmax(totalvalue, 504)
    lo = _rmin(totalvalue, 504)
    b = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth efficiency: holders added per unit of new dollar value (broadening vs concentrating)
def f44ia_f44_institutional_accumulation_netnewhold_252d_base_v044_signal(shrholders, totalvalue):
    dh = shrholders - shrholders.shift(126)
    dv = totalvalue - totalvalue.shift(126)
    b = np.sign(dv) * dh / (dv.abs().replace(0, np.nan) ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow composite: units growth weighted by ownership pct level
def f44ia_f44_institutional_accumulation_inflowweighted_base_v045_signal(shrunits, totalvalue, marketcap):
    g = _logroc(shrunits, 63)
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = g * op
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder percentile rank vs 504d (conviction-size cycle position)
def f44ia_f44_institutional_accumulation_valperholdrank_504d_base_v046_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    b = _rank(vph, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5y ownership-pct trend (very long accumulation drift via log-slope)
def f44ia_f44_institutional_accumulation_ownpctgr_1260d_base_v047_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = np.log(op.replace(0, np.nan) / op.shift(1260).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count smoothed displacement (count minus its slow EMA)
def f44ia_f44_institutional_accumulation_holddisp_base_v048_signal(shrholders):
    lc = np.log(shrholders.replace(0, np.nan))
    b = lc - lc.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value smoothed displacement (value minus slow EMA, log)
def f44ia_f44_institutional_accumulation_valdisp_base_v049_signal(totalvalue):
    lv = np.log(totalvalue.replace(0, np.nan))
    b = lv - lv.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth-quality: net-new-holders sign times units growth magnitude
def f44ia_f44_institutional_accumulation_breadthqual_base_v050_signal(shrholders, shrunits):
    nh = np.sign(_f44ia_breadth_trend(shrholders, 63))
    ug = _logroc(shrunits, 63).abs()
    b = nh * ug
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct vs its 252d mean ratio minus 1 (crowding above normal)
def f44ia_f44_institutional_accumulation_ownpctstretch_252d_base_v051_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    mn = _mean(op, 252)
    b = op / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units 12-1 momentum (yearly units growth ex last month, classic momentum)
def f44ia_f44_institutional_accumulation_units121mom_base_v052_signal(shrunits):
    b = np.log(shrunits.shift(21).replace(0, np.nan) / shrunits.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value inflow consistency: fraction of last year with positive 21d value growth minus 0.5
def f44ia_f44_institutional_accumulation_val121mom_base_v053_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count dispersion (std of holder log-changes, breadth churn)
def f44ia_f44_institutional_accumulation_holdchurn_126d_base_v054_signal(shrholders):
    chg = np.log(shrholders.replace(0, np.nan)).diff()
    b = chg.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-value outflow duration: fraction of last half-year value sat >5% below 504d peak
def f44ia_f44_institutional_accumulation_valdrawdown_504d_base_v055_signal(totalvalue):
    peak = _rmax(totalvalue, 504)
    underwater = totalvalue / peak.replace(0, np.nan) - 1.0
    deep = (underwater <= -0.05).astype(float)
    b = deep.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with inst units above 126d average (accumulation regime time)
def f44ia_f44_institutional_accumulation_unitabovetime_252d_base_v056_signal(shrunits):
    avg = _mean(shrunits, 126)
    above = (shrunits > avg).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-pct mean-reversion gap: pct minus its 63d EMA, scaled by 252d dispersion
def f44ia_f44_institutional_accumulation_ownpctconv_252d_base_v057_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    gap = op - op.ewm(span=63, min_periods=21).mean()
    disp = op.rolling(252, min_periods=126).std()
    b = gap / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-weighted value: holder growth times value growth (broad-and-rich accumulation)
def f44ia_f44_institutional_accumulation_broadrichaccum_base_v058_signal(shrholders, totalvalue):
    hg = _logroc(shrholders, 63)
    vg = _logroc(totalvalue, 63)
    b = hg * vg * np.sign(hg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# representative shrvalue percentile-rank vs 504d
def f44ia_f44_institutional_accumulation_shrvalrank_504d_base_v059_signal(shrvalue):
    b = _rank(shrvalue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied-price z-score vs 252d (institutional mark extremity)
def f44ia_f44_institutional_accumulation_implpxz_252d_base_v060_signal(totalvalue, shrunits):
    ip = _f44ia_implied_price(totalvalue, shrunits)
    lp = np.log(ip.replace(0, np.nan))
    b = _z(lp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units yearly growth scaled by holder-count change volatility (clean share accumulation)
def f44ia_f44_institutional_accumulation_unitgrvsbreadth_base_v061_signal(shrunits, shrholders):
    g = _logroc(shrunits, 252)
    hv = np.log(shrholders.replace(0, np.nan)).diff().rolling(126, min_periods=63).std()
    b = g / hv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year holder breadth growth percentile-ranked (relative accumulation strength)
def f44ia_f44_institutional_accumulation_holdgrrank_126d_base_v062_signal(shrholders):
    g = _logroc(shrholders, 126)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value/marketcap vs units-flow divergence (price effect vs flow effect)
def f44ia_f44_institutional_accumulation_flowpricediv_base_v063_signal(totalvalue, marketcap, shrunits):
    op = _f44ia_own_pct(totalvalue, marketcap)
    ug = _logroc(shrunits, 63)
    opg = op - op.shift(63)
    b = opg - 0.1 * ug
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-investor value share momentum (shrvalue/totalvalue change over half-year)
def f44ia_f44_institutional_accumulation_concmom_126d_base_v064_signal(shrvalue, totalvalue):
    share = shrvalue / totalvalue.replace(0, np.nan)
    b = share - share.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value inflow acceleration: 63d value growth now vs 126d ago (multi-quarter accel)
def f44ia_f44_institutional_accumulation_valemax_base_v065_signal(totalvalue):
    g = _logroc(totalvalue, 63)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count breadth oscillator: 21d holder growth z-scored vs its own 252d history
def f44ia_f44_institutional_accumulation_holdemax_base_v066_signal(shrholders):
    g = _logroc(shrholders, 21)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net accumulation index: ownership pct z plus units growth z (composite)
def f44ia_f44_institutional_accumulation_accumindex_base_v067_signal(totalvalue, marketcap, shrunits):
    op = _f44ia_own_pct(totalvalue, marketcap)
    ug = _logroc(shrunits, 63)
    b = 0.5 * _z(op, 252) + 0.5 * _z(ug, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units position in 1260d range (multi-year share-base cycle position)
def f44ia_f44_institutional_accumulation_unitrngpos_1260d_base_v068_signal(shrunits):
    hi = _rmax(shrunits, 1260)
    lo = _rmin(shrunits, 1260)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-pct year-over-year change (annual accumulation delta)
def f44ia_f44_institutional_accumulation_ownpctyoy_base_v069_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = op - op.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder drawdown from 252d peak (conviction erosion)
def f44ia_f44_institutional_accumulation_valperholddd_252d_base_v070_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    peak = _rmax(vph, 252)
    b = vph / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last half-year inst value made new 126d highs (sustained inflow regime)
def f44ia_f44_institutional_accumulation_valnewhifrac_base_v071_signal(totalvalue):
    rmx = _rmax(totalvalue, 126)
    ishi = (totalvalue >= rmx * 0.99999).astype(float)
    b = ishi.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money tanh inflow: bounded ownership-pct change over quarter
def f44ia_f44_institutional_accumulation_ownpcttanh_63d_base_v072_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    chg = op - op.shift(63)
    sd = op.diff().rolling(126, min_periods=63).std()
    b = np.tanh(chg / sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units acceleration: quarterly growth now vs a quarter ago (flow acceleration)
def f44ia_f44_institutional_accumulation_unitaccel_63d_base_v073_signal(shrunits):
    g = _logroc(shrunits, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-to-value ratio trend: holders / sqrt(value), change over half-year
def f44ia_f44_institutional_accumulation_breadthvalratio_base_v074_signal(shrholders, totalvalue):
    ratio = shrholders / (totalvalue.replace(0, np.nan) ** 0.5)
    b = np.log(ratio.replace(0, np.nan) / ratio.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite accumulation momentum: blended holder/units/value yearly growth rank
def f44ia_f44_institutional_accumulation_accummomrank_base_v075_signal(shrholders, shrunits, totalvalue):
    blend = (_logroc(shrholders, 252) + _logroc(shrunits, 252) + _logroc(totalvalue, 252)) / 3.0
    b = _rank(blend, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44ia_f44_institutional_accumulation_holdersz_252d_base_v001_signal,
    f44ia_f44_institutional_accumulation_holdersgr_63d_base_v002_signal,
    f44ia_f44_institutional_accumulation_holdersgr_252d_base_v003_signal,
    f44ia_f44_institutional_accumulation_holdersrank_504d_base_v004_signal,
    f44ia_f44_institutional_accumulation_valz_252d_base_v005_signal,
    f44ia_f44_institutional_accumulation_valgr_63d_base_v006_signal,
    f44ia_f44_institutional_accumulation_valgr_252d_base_v007_signal,
    f44ia_f44_institutional_accumulation_ownpct_base_v008_signal,
    f44ia_f44_institutional_accumulation_ownpctz_252d_base_v009_signal,
    f44ia_f44_institutional_accumulation_ownpctchg_63d_base_v010_signal,
    f44ia_f44_institutional_accumulation_unitsgr_63d_base_v011_signal,
    f44ia_f44_institutional_accumulation_unitsgr_252d_base_v012_signal,
    f44ia_f44_institutional_accumulation_unitsz_252d_base_v013_signal,
    f44ia_f44_institutional_accumulation_valperhold_base_v014_signal,
    f44ia_f44_institutional_accumulation_valperholdgr_63d_base_v015_signal,
    f44ia_f44_institutional_accumulation_unitsperhold_base_v016_signal,
    f44ia_f44_institutional_accumulation_unitsperholdgr_63d_base_v017_signal,
    f44ia_f44_institutional_accumulation_shrvalz_252d_base_v018_signal,
    f44ia_f44_institutional_accumulation_shrvalgr_63d_base_v019_signal,
    f44ia_f44_institutional_accumulation_shrvalshare_base_v020_signal,
    f44ia_f44_institutional_accumulation_shrvalsharechg_63d_base_v021_signal,
    f44ia_f44_institutional_accumulation_valexmktgr_63d_base_v022_signal,
    f44ia_f44_institutional_accumulation_implpxgr_252d_base_v023_signal,
    f44ia_f44_institutional_accumulation_unitexvalgr_63d_base_v024_signal,
    f44ia_f44_institutional_accumulation_breadthsizediv_63d_base_v025_signal,
    f44ia_f44_institutional_accumulation_holdtrendspr_base_v026_signal,
    f44ia_f44_institutional_accumulation_valtrendspr_base_v027_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_504d_base_v028_signal,
    f44ia_f44_institutional_accumulation_valinflow_ema_base_v029_signal,
    f44ia_f44_institutional_accumulation_holdupfrac_63d_base_v030_signal,
    f44ia_f44_institutional_accumulation_unitupfrac_63d_base_v031_signal,
    f44ia_f44_institutional_accumulation_valperholdz_252d_base_v032_signal,
    f44ia_f44_institutional_accumulation_ownpctriskadj_126d_base_v033_signal,
    f44ia_f44_institutional_accumulation_unitsrank_504d_base_v034_signal,
    f44ia_f44_institutional_accumulation_valgrriskadj_base_v035_signal,
    f44ia_f44_institutional_accumulation_holdaccel_21d_base_v036_signal,
    f44ia_f44_institutional_accumulation_unitstanh_63d_base_v037_signal,
    f44ia_f44_institutional_accumulation_ownpctheadroom_252d_base_v038_signal,
    f44ia_f44_institutional_accumulation_ownpctrecov_252d_base_v039_signal,
    f44ia_f44_institutional_accumulation_convmixspr_63d_base_v040_signal,
    f44ia_f44_institutional_accumulation_shrvalgrriskadj_base_v041_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_252d_base_v042_signal,
    f44ia_f44_institutional_accumulation_valrngpos_504d_base_v043_signal,
    f44ia_f44_institutional_accumulation_netnewhold_252d_base_v044_signal,
    f44ia_f44_institutional_accumulation_inflowweighted_base_v045_signal,
    f44ia_f44_institutional_accumulation_valperholdrank_504d_base_v046_signal,
    f44ia_f44_institutional_accumulation_ownpctgr_1260d_base_v047_signal,
    f44ia_f44_institutional_accumulation_holddisp_base_v048_signal,
    f44ia_f44_institutional_accumulation_valdisp_base_v049_signal,
    f44ia_f44_institutional_accumulation_breadthqual_base_v050_signal,
    f44ia_f44_institutional_accumulation_ownpctstretch_252d_base_v051_signal,
    f44ia_f44_institutional_accumulation_units121mom_base_v052_signal,
    f44ia_f44_institutional_accumulation_val121mom_base_v053_signal,
    f44ia_f44_institutional_accumulation_holdchurn_126d_base_v054_signal,
    f44ia_f44_institutional_accumulation_valdrawdown_504d_base_v055_signal,
    f44ia_f44_institutional_accumulation_unitabovetime_252d_base_v056_signal,
    f44ia_f44_institutional_accumulation_ownpctconv_252d_base_v057_signal,
    f44ia_f44_institutional_accumulation_broadrichaccum_base_v058_signal,
    f44ia_f44_institutional_accumulation_shrvalrank_504d_base_v059_signal,
    f44ia_f44_institutional_accumulation_implpxz_252d_base_v060_signal,
    f44ia_f44_institutional_accumulation_unitgrvsbreadth_base_v061_signal,
    f44ia_f44_institutional_accumulation_holdgrrank_126d_base_v062_signal,
    f44ia_f44_institutional_accumulation_flowpricediv_base_v063_signal,
    f44ia_f44_institutional_accumulation_concmom_126d_base_v064_signal,
    f44ia_f44_institutional_accumulation_valemax_base_v065_signal,
    f44ia_f44_institutional_accumulation_holdemax_base_v066_signal,
    f44ia_f44_institutional_accumulation_accumindex_base_v067_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_1260d_base_v068_signal,
    f44ia_f44_institutional_accumulation_ownpctyoy_base_v069_signal,
    f44ia_f44_institutional_accumulation_valperholddd_252d_base_v070_signal,
    f44ia_f44_institutional_accumulation_valnewhifrac_base_v071_signal,
    f44ia_f44_institutional_accumulation_ownpcttanh_63d_base_v072_signal,
    f44ia_f44_institutional_accumulation_unitaccel_63d_base_v073_signal,
    f44ia_f44_institutional_accumulation_breadthvalratio_base_v074_signal,
    f44ia_f44_institutional_accumulation_accummomrank_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_INSTITUTIONAL_ACCUMULATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    # ownership columns: all positive, with trend so accumulation features vary
    shrholders = _fund(101, base=120.0, drift=0.03, vol=0.06).rename("shrholders")
    shrunits = _fund(102, base=5.0e6, drift=0.04, vol=0.09).rename("shrunits")
    totalvalue = _fund(103, base=8.0e7, drift=0.05, vol=0.10).rename("totalvalue")
    shrvalue = _fund(104, base=9.0e6, drift=0.04, vol=0.11).rename("shrvalue")
    marketcap = _fund(105, base=3.0e8, drift=0.02, vol=0.08).rename("marketcap")

    cols = {
        "shrholders": shrholders,
        "shrunits": shrunits,
        "totalvalue": totalvalue,
        "shrvalue": shrvalue,
        "marketcap": marketcap,
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

    print("OK f44_institutional_accumulation_base_001_075_claude: %d features pass" % n_features)
