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


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== f44 ownership / institutional-accumulation primitives =====
def _f44ia_own_pct(totalvalue, marketcap):
    return totalvalue / marketcap.replace(0, np.nan)


def _f44ia_value_per_holder(totalvalue, shrholders):
    return totalvalue / shrholders.replace(0, np.nan)


def _f44ia_units_per_holder(shrunits, shrholders):
    return shrunits / shrholders.replace(0, np.nan)


def _f44ia_implied_price(totalvalue, shrunits):
    return totalvalue / shrunits.replace(0, np.nan)


def _slope(s, w):
    # OLS slope of s over a rolling window of length w (per-bar drift)
    x = np.arange(w, dtype=float)
    xm = x.mean()
    xd = x - xm
    denom = (xd ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        ym = a.mean()
        return float((xd * (a - ym)).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ============================================================
# inst holder-count 126d growth (half-year breadth ramp)
def f44ia_f44_institutional_accumulation_holdgr_126d_base_v076_signal(shrholders):
    b = _logroc(shrholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count 21d growth z-scored vs 126d (short breadth surge)
def f44ia_f44_institutional_accumulation_holdsurge_21d_base_v077_signal(shrholders):
    g = _logroc(shrholders, 21)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of log holder count over a quarter (smoothed breadth drift)
def f44ia_f44_institutional_accumulation_holdslope_63d_base_v078_signal(shrholders):
    lc = np.log(shrholders.replace(0, np.nan))
    b = _slope(lc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value 126d growth (half-year dollar inflow)
def f44ia_f44_institutional_accumulation_valgr_126d_base_v079_signal(totalvalue):
    b = _logroc(totalvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curvature of log inst value: OLS slope now minus slope a quarter ago (inflow bend)
def f44ia_f44_institutional_accumulation_valslope_126d_base_v080_signal(totalvalue):
    lv = np.log(totalvalue.replace(0, np.nan))
    sl = _slope(lv, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst units 126d growth (half-year share accumulation)
def f44ia_f44_institutional_accumulation_unitgr_126d_base_v081_signal(shrunits):
    b = _logroc(shrunits, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of log inst units over a quarter (smoothed share-accumulation drift)
def f44ia_f44_institutional_accumulation_unitslope_63d_base_v082_signal(shrunits):
    lu = np.log(shrunits.replace(0, np.nan))
    b = _slope(lu, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct half-year change (mid-horizon accumulation vs marketcap)
def f44ia_f44_institutional_accumulation_ownpctchg_126d_base_v083_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = op - op.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct OLS slope over a year (long accumulation drift)
def f44ia_f44_institutional_accumulation_ownpctslope_252d_base_v084_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = _slope(op, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct rank vs 252d history (where ownership sits this year)
def f44ia_f44_institutional_accumulation_ownpctrank_252d_base_v085_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = _rank(op, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder 126d growth (half-year conviction build per institution)
def f44ia_f44_institutional_accumulation_vphgr_126d_base_v086_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    b = _logroc(vph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder 126d growth (half-year position-size build)
def f44ia_f44_institutional_accumulation_uphgr_126d_base_v087_signal(shrunits, shrholders):
    uph = _f44ia_units_per_holder(shrunits, shrholders)
    b = _logroc(uph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder rank vs 504d (position-size cycle position)
def f44ia_f44_institutional_accumulation_uphrank_504d_base_v088_signal(shrunits, shrholders):
    uph = _f44ia_units_per_holder(shrunits, shrholders)
    b = _rank(uph, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# representative shrvalue 126d growth (half-year per-filing value inflow)
def f44ia_f44_institutional_accumulation_shrvalgr_126d_base_v089_signal(shrvalue):
    b = _logroc(shrvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue z-scored vs 504d (per-filing value extremity, long history)
def f44ia_f44_institutional_accumulation_shrvalz_504d_base_v090_signal(shrvalue):
    lv = np.log(shrvalue.replace(0, np.nan))
    b = _z(lv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue-share OLS slope over a year (concentration drift)
def f44ia_f44_institutional_accumulation_shrvalshareslope_252d_base_v091_signal(shrvalue, totalvalue):
    share = shrvalue / totalvalue.replace(0, np.nan)
    b = _slope(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue-share z vs 252d (concentration extremity)
def f44ia_f44_institutional_accumulation_shrvalsharez_252d_base_v092_signal(shrvalue, totalvalue):
    share = shrvalue / totalvalue.replace(0, np.nan)
    b = _z(share, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied price (value/units) 126d growth (half-year mark-up rate)
def f44ia_f44_institutional_accumulation_implpxgr_126d_base_v093_signal(totalvalue, shrunits):
    ip = _f44ia_implied_price(totalvalue, shrunits)
    b = _logroc(ip, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied-price rank vs 504d (mark cycle position)
def f44ia_f44_institutional_accumulation_implpxrank_504d_base_v094_signal(totalvalue, shrunits):
    ip = _f44ia_implied_price(totalvalue, shrunits)
    b = _rank(ip, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth-quality 126d: net-holder sign times value growth magnitude
def f44ia_f44_institutional_accumulation_breadthqual_126d_base_v095_signal(shrholders, totalvalue):
    nh = np.sign(shrholders - shrholders.shift(126))
    vg = _logroc(totalvalue, 126).abs()
    b = nh * vg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count 504d position in range (multi-year breadth phase)
def f44ia_f44_institutional_accumulation_holdrngpos_504d_base_v096_signal(shrholders):
    hi = _rmax(shrholders, 504)
    lo = _rmin(shrholders, 504)
    b = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units 252d position in range (yearly share-base phase)
def f44ia_f44_institutional_accumulation_unitrngpos_252d_base_v097_signal(shrunits):
    hi = _rmax(shrunits, 252)
    lo = _rmin(shrunits, 252)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value 252d position in range (yearly dollar-ownership phase)
def f44ia_f44_institutional_accumulation_valrngpos_252d_base_v098_signal(totalvalue):
    hi = _rmax(totalvalue, 252)
    lo = _rmin(totalvalue, 252)
    b = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct 504d position in range (multi-year ownership phase)
def f44ia_f44_institutional_accumulation_ownpctrngpos_504d_base_v099_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    hi = _rmax(op, 504)
    lo = _rmin(op, 504)
    b = (op - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder attrition duration: fraction of last quarter holders sat >3% below 252d peak
def f44ia_f44_institutional_accumulation_holddd_252d_base_v100_signal(shrholders):
    peak = _rmax(shrholders, 252)
    underwater = shrholders / peak.replace(0, np.nan) - 1.0
    deep = (underwater <= -0.03).astype(float)
    b = deep.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units recovery off 252d trough (share re-accumulation off lows)
def f44ia_f44_institutional_accumulation_unitrecov_252d_base_v101_signal(shrunits):
    trough = _rmin(shrunits, 252)
    b = shrunits / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value recovery off 504d trough (dollar re-accumulation off lows)
def f44ia_f44_institutional_accumulation_valrecov_504d_base_v102_signal(totalvalue):
    trough = _rmin(totalvalue, 504)
    b = totalvalue / trough.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money inflow EMA (smoothed quarterly value growth, slow span)
def f44ia_f44_institutional_accumulation_valinflowema_slow_base_v103_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units inflow oscillator: monthly units growth minus its 63-EMA (impulse vs trend)
def f44ia_f44_institutional_accumulation_unitinflowema_base_v104_signal(shrunits):
    g = _logroc(shrunits, 21)
    b = g - g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation regime time: fraction of last year holders above 252d median
def f44ia_f44_institutional_accumulation_holdabovetime_252d_base_v105_signal(shrholders):
    med = shrholders.rolling(252, min_periods=126).median()
    above = (shrholders > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation regime time: fraction of last year value above 252d median
def f44ia_f44_institutional_accumulation_valabovetime_252d_base_v106_signal(totalvalue):
    med = totalvalue.rolling(252, min_periods=126).median()
    above = (totalvalue > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-holder regime: fraction of last quarter holder count made new 126d highs
def f44ia_f44_institutional_accumulation_holdnewhifrac_base_v107_signal(shrholders):
    rmx = _rmax(shrholders, 126)
    ishi = (shrholders >= rmx * 0.99999).astype(float)
    b = ishi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-units regime: fraction of last quarter units made new 126d highs (share-base highs)
def f44ia_f44_institutional_accumulation_unitnewhifrac_base_v108_signal(shrunits):
    rmx = _rmax(shrunits, 126)
    ishi = (shrunits >= rmx * 0.99999).astype(float)
    b = ishi.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value inflow consistency: fraction of last half-year with positive 21d value growth
def f44ia_f44_institutional_accumulation_valposfrac_126d_base_v109_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    pos = (g > 0).astype(float)
    b = pos.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder breadth consistency: fraction of last half-year with positive 21d holder growth
def f44ia_f44_institutional_accumulation_holdposfrac_126d_base_v110_signal(shrholders):
    g = _logroc(shrholders, 21)
    pos = (g > 0).astype(float)
    b = pos.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth churn: std of 21d holder growth over a year (inflow turbulence)
def f44ia_f44_institutional_accumulation_holdgrvol_252d_base_v111_signal(shrholders):
    g = _logroc(shrholders, 21)
    b = g.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inflow volatility: std of 21d value growth over a year (dollar-inflow turbulence)
def f44ia_f44_institutional_accumulation_valgrvol_252d_base_v112_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    b = g.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct momentum / dispersion (risk-adj accumulation over quarter)
def f44ia_f44_institutional_accumulation_ownpctsharpe_63d_base_v113_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    chg = op - op.shift(63)
    sd = op.diff().rolling(63, min_periods=21).std()
    b = chg / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder conviction curvature: 63d slope now minus 63d slope a quarter ago
def f44ia_f44_institutional_accumulation_vphslope_126d_base_v114_signal(totalvalue, shrholders):
    vph = np.log(_f44ia_value_per_holder(totalvalue, shrholders).replace(0, np.nan))
    sl = _slope(vph, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder OLS slope over a quarter (smoothed position-size drift)
def f44ia_f44_institutional_accumulation_uphslope_63d_base_v115_signal(shrunits, shrholders):
    uph = np.log(_f44ia_units_per_holder(shrunits, shrholders).replace(0, np.nan))
    b = _slope(uph, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inflow vs breadth divergence regime: z(value/holders ratio) over 252d
def f44ia_f44_institutional_accumulation_valholdratioz_252d_base_v116_signal(totalvalue, shrholders):
    ratio = np.log((totalvalue / shrholders.replace(0, np.nan)).replace(0, np.nan))
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smart-money weighted inflow: value growth times ownership-pct rank (rich+crowded)
def f44ia_f44_institutional_accumulation_inflowcrowd_base_v117_signal(totalvalue, marketcap):
    vg = _logroc(totalvalue, 63)
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = vg * _rank(op, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-weighted units inflow: units growth times holder-rank (broad share adds)
def f44ia_f44_institutional_accumulation_inflowbroad_base_v118_signal(shrunits, shrholders):
    ug = _logroc(shrunits, 63)
    b = ug * _rank(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net accumulation composite z: holder-z + value-z (broad dollar accumulation)
def f44ia_f44_institutional_accumulation_accumcompz_base_v119_signal(shrholders, totalvalue):
    hz = _z(np.log(shrholders.replace(0, np.nan)), 252)
    vz = _z(np.log(totalvalue.replace(0, np.nan)), 252)
    b = 0.5 * hz + 0.5 * vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value yearly growth minus units yearly growth = mark-up (price effect on holdings)
def f44ia_f44_institutional_accumulation_markupyr_base_v120_signal(totalvalue, shrunits):
    b = _logroc(totalvalue, 252) - _logroc(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holders yearly growth minus value yearly growth scaled (broadening vs enriching, yr)
def f44ia_f44_institutional_accumulation_broadenyr_base_v121_signal(shrholders, totalvalue):
    spread = _logroc(shrholders, 252) - 0.5 * _logroc(totalvalue, 252)
    b = spread
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation acceleration: holder 63d growth now vs 126d ago (multi-q breadth accel)
def f44ia_f44_institutional_accumulation_holdaccel_126d_base_v122_signal(shrholders):
    g = _logroc(shrholders, 63)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct stretch above 504d mean (multi-year crowding)
def f44ia_f44_institutional_accumulation_ownpctstretch_504d_base_v123_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    mn = _mean(op, 504)
    b = op / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded value inflow (monthly value growth, squashed)
def f44ia_f44_institutional_accumulation_valtanh_21d_base_v124_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    b = np.tanh(20.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded holder breadth surge (monthly holder growth, squashed)
def f44ia_f44_institutional_accumulation_holdtanh_21d_base_v125_signal(shrholders):
    g = _logroc(shrholders, 21)
    b = np.tanh(30.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder drawdown from 504d peak (multi-year conviction erosion)
def f44ia_f44_institutional_accumulation_vphdd_504d_base_v126_signal(totalvalue, shrholders):
    vph = _f44ia_value_per_holder(totalvalue, shrholders)
    peak = _rmax(vph, 504)
    b = vph / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder drawdown from 252d peak (position-size erosion)
def f44ia_f44_institutional_accumulation_uphdd_252d_base_v127_signal(shrunits, shrholders):
    uph = _f44ia_units_per_holder(shrunits, shrholders)
    peak = _rmax(uph, 252)
    b = uph / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied-price drawdown from 252d peak (institutional mark stress)
def f44ia_f44_institutional_accumulation_implpxdd_252d_base_v128_signal(totalvalue, shrunits):
    ip = _f44ia_implied_price(totalvalue, shrunits)
    peak = _rmax(ip, 252)
    b = ip / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation momentum rank: 126d value growth percentile vs 252d history
def f44ia_f44_institutional_accumulation_valgrrank_126d_base_v129_signal(totalvalue):
    g = _logroc(totalvalue, 126)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units growth rank: 126d units growth percentile vs 252d history
def f44ia_f44_institutional_accumulation_unitgrrank_126d_base_v130_signal(shrunits):
    g = _logroc(shrunits, 126)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct yearly growth rank (relative accumulation strength)
def f44ia_f44_institutional_accumulation_ownpctgrrank_base_v131_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    g = op - op.shift(126)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue inflow EMA (smoothed per-filing value growth)
def f44ia_f44_institutional_accumulation_shrvalinflowema_base_v132_signal(shrvalue):
    g = _logroc(shrvalue, 21)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue drawdown from 252d peak (per-filing value erosion)
def f44ia_f44_institutional_accumulation_shrvaldd_252d_base_v133_signal(shrvalue):
    peak = _rmax(shrvalue, 252)
    b = shrvalue / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-to-implied-mark interaction: holder growth times implied-price growth sign
def f44ia_f44_institutional_accumulation_breadthmark_base_v134_signal(shrholders, totalvalue, shrunits):
    hg = _logroc(shrholders, 63)
    ip = _f44ia_implied_price(totalvalue, shrunits)
    ipg = _logroc(ip, 63)
    b = hg * np.sign(ipg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct vs holder-breadth divergence: pct change minus holder growth
def f44ia_f44_institutional_accumulation_pctbreadthdiv_base_v135_signal(totalvalue, marketcap, shrholders):
    op = _f44ia_own_pct(totalvalue, marketcap)
    opg = (op - op.shift(63)) / op.shift(63).replace(0, np.nan)
    hg = _logroc(shrholders, 63)
    b = opg - hg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year ownership pct trend via OLS slope over 504d
def f44ia_f44_institutional_accumulation_ownpctslope_504d_base_v136_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    b = _slope(op, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value 1260d position in range (multi-year dollar-ownership cycle)
def f44ia_f44_institutional_accumulation_valrngpos_1260d_base_v137_signal(totalvalue):
    hi = _rmax(totalvalue, 1260)
    lo = _rmin(totalvalue, 1260)
    b = (totalvalue - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holders 1260d range-position momentum: change in multi-year breadth phase over a quarter
def f44ia_f44_institutional_accumulation_holdrngpos_1260d_base_v138_signal(shrholders):
    hi = _rmax(shrholders, 1260)
    lo = _rmin(shrholders, 1260)
    pos = (shrholders - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth z minus value z (broadening-vs-enriching regime spread)
def f44ia_f44_institutional_accumulation_breadthrichspr_base_v139_signal(shrholders, totalvalue):
    hz = _z(np.log(shrholders.replace(0, np.nan)), 252)
    vz = _z(np.log(totalvalue.replace(0, np.nan)), 252)
    b = hz - vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value inflow per holder: 63d value growth divided by holder-count level (dilution-adj)
def f44ia_f44_institutional_accumulation_inflowperhold_base_v140_signal(totalvalue, shrholders):
    vg = _logroc(totalvalue, 63)
    hr = _rank(shrholders, 252) + 0.5 + 0.1
    b = vg / hr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership pct headroom to 504d max (room to crowd, multi-year)
def f44ia_f44_institutional_accumulation_ownpctheadroom_504d_base_v141_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    mx = _rmax(op, 504)
    b = op / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units headroom to 504d max (share-base room to grow)
def f44ia_f44_institutional_accumulation_unitheadroom_504d_base_v142_signal(shrunits):
    mx = _rmax(shrunits, 504)
    b = shrunits / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation impulse: 5d value growth z-scored vs 63d (very-short inflow shock)
def f44ia_f44_institutional_accumulation_valshock_5d_base_v143_signal(totalvalue):
    g = _logroc(totalvalue, 5)
    b = _z(g, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth impulse: 5d holder growth z-scored vs 63d (very-short breadth shock)
def f44ia_f44_institutional_accumulation_holdshock_5d_base_v144_signal(shrholders):
    g = _logroc(shrholders, 5)
    b = _z(g, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value vs marketcap relative strength: value rank minus marketcap rank over 252d
def f44ia_f44_institutional_accumulation_valmktrs_base_v145_signal(totalvalue, marketcap):
    vr = _rank(np.log(totalvalue.replace(0, np.nan)), 252)
    mr = _rank(np.log(marketcap.replace(0, np.nan)), 252)
    b = vr - mr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value/marketcap (ownership pct) volatility-of-trend: std of 21d pct change over year
def f44ia_f44_institutional_accumulation_ownpctchurn_base_v146_signal(totalvalue, marketcap):
    op = _f44ia_own_pct(totalvalue, marketcap)
    chg = op.pct_change(21)
    b = chg.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak length: consecutive months of rising holders (scaled count)
def f44ia_f44_institutional_accumulation_holdstreak_base_v147_signal(shrholders):
    up = (shrholders.diff(21) > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    streak = up.groupby(grp).cumsum() * up
    b = streak.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak length: consecutive months of rising units (scaled count)
def f44ia_f44_institutional_accumulation_unitstreak_base_v148_signal(shrunits):
    up = (shrunits.diff(21) > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    streak = up.groupby(grp).cumsum() * up
    b = streak.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite smart-money score: units-per-holder z + value-per-holder z (deep conviction)
def f44ia_f44_institutional_accumulation_smartscore_base_v149_signal(shrunits, totalvalue, shrholders):
    uph = np.log(_f44ia_units_per_holder(shrunits, shrholders).replace(0, np.nan))
    vph = np.log(_f44ia_value_per_holder(totalvalue, shrholders).replace(0, np.nan))
    b = 0.5 * _z(uph, 252) + 0.5 * _z(vph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth-and-value yearly growth product (confirmed broad inflow)
def f44ia_f44_institutional_accumulation_confirmaccum_base_v150_signal(shrholders, totalvalue, shrunits):
    hg = _logroc(shrholders, 252)
    ug = _logroc(shrunits, 252)
    b = np.sign(hg) * (hg.abs() * ug.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44ia_f44_institutional_accumulation_holdgr_126d_base_v076_signal,
    f44ia_f44_institutional_accumulation_holdsurge_21d_base_v077_signal,
    f44ia_f44_institutional_accumulation_holdslope_63d_base_v078_signal,
    f44ia_f44_institutional_accumulation_valgr_126d_base_v079_signal,
    f44ia_f44_institutional_accumulation_valslope_126d_base_v080_signal,
    f44ia_f44_institutional_accumulation_unitgr_126d_base_v081_signal,
    f44ia_f44_institutional_accumulation_unitslope_63d_base_v082_signal,
    f44ia_f44_institutional_accumulation_ownpctchg_126d_base_v083_signal,
    f44ia_f44_institutional_accumulation_ownpctslope_252d_base_v084_signal,
    f44ia_f44_institutional_accumulation_ownpctrank_252d_base_v085_signal,
    f44ia_f44_institutional_accumulation_vphgr_126d_base_v086_signal,
    f44ia_f44_institutional_accumulation_uphgr_126d_base_v087_signal,
    f44ia_f44_institutional_accumulation_uphrank_504d_base_v088_signal,
    f44ia_f44_institutional_accumulation_shrvalgr_126d_base_v089_signal,
    f44ia_f44_institutional_accumulation_shrvalz_504d_base_v090_signal,
    f44ia_f44_institutional_accumulation_shrvalshareslope_252d_base_v091_signal,
    f44ia_f44_institutional_accumulation_shrvalsharez_252d_base_v092_signal,
    f44ia_f44_institutional_accumulation_implpxgr_126d_base_v093_signal,
    f44ia_f44_institutional_accumulation_implpxrank_504d_base_v094_signal,
    f44ia_f44_institutional_accumulation_breadthqual_126d_base_v095_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_504d_base_v096_signal,
    f44ia_f44_institutional_accumulation_unitrngpos_252d_base_v097_signal,
    f44ia_f44_institutional_accumulation_valrngpos_252d_base_v098_signal,
    f44ia_f44_institutional_accumulation_ownpctrngpos_504d_base_v099_signal,
    f44ia_f44_institutional_accumulation_holddd_252d_base_v100_signal,
    f44ia_f44_institutional_accumulation_unitrecov_252d_base_v101_signal,
    f44ia_f44_institutional_accumulation_valrecov_504d_base_v102_signal,
    f44ia_f44_institutional_accumulation_valinflowema_slow_base_v103_signal,
    f44ia_f44_institutional_accumulation_unitinflowema_base_v104_signal,
    f44ia_f44_institutional_accumulation_holdabovetime_252d_base_v105_signal,
    f44ia_f44_institutional_accumulation_valabovetime_252d_base_v106_signal,
    f44ia_f44_institutional_accumulation_holdnewhifrac_base_v107_signal,
    f44ia_f44_institutional_accumulation_unitnewhifrac_base_v108_signal,
    f44ia_f44_institutional_accumulation_valposfrac_126d_base_v109_signal,
    f44ia_f44_institutional_accumulation_holdposfrac_126d_base_v110_signal,
    f44ia_f44_institutional_accumulation_holdgrvol_252d_base_v111_signal,
    f44ia_f44_institutional_accumulation_valgrvol_252d_base_v112_signal,
    f44ia_f44_institutional_accumulation_ownpctsharpe_63d_base_v113_signal,
    f44ia_f44_institutional_accumulation_vphslope_126d_base_v114_signal,
    f44ia_f44_institutional_accumulation_uphslope_63d_base_v115_signal,
    f44ia_f44_institutional_accumulation_valholdratioz_252d_base_v116_signal,
    f44ia_f44_institutional_accumulation_inflowcrowd_base_v117_signal,
    f44ia_f44_institutional_accumulation_inflowbroad_base_v118_signal,
    f44ia_f44_institutional_accumulation_accumcompz_base_v119_signal,
    f44ia_f44_institutional_accumulation_markupyr_base_v120_signal,
    f44ia_f44_institutional_accumulation_broadenyr_base_v121_signal,
    f44ia_f44_institutional_accumulation_holdaccel_126d_base_v122_signal,
    f44ia_f44_institutional_accumulation_ownpctstretch_504d_base_v123_signal,
    f44ia_f44_institutional_accumulation_valtanh_21d_base_v124_signal,
    f44ia_f44_institutional_accumulation_holdtanh_21d_base_v125_signal,
    f44ia_f44_institutional_accumulation_vphdd_504d_base_v126_signal,
    f44ia_f44_institutional_accumulation_uphdd_252d_base_v127_signal,
    f44ia_f44_institutional_accumulation_implpxdd_252d_base_v128_signal,
    f44ia_f44_institutional_accumulation_valgrrank_126d_base_v129_signal,
    f44ia_f44_institutional_accumulation_unitgrrank_126d_base_v130_signal,
    f44ia_f44_institutional_accumulation_ownpctgrrank_base_v131_signal,
    f44ia_f44_institutional_accumulation_shrvalinflowema_base_v132_signal,
    f44ia_f44_institutional_accumulation_shrvaldd_252d_base_v133_signal,
    f44ia_f44_institutional_accumulation_breadthmark_base_v134_signal,
    f44ia_f44_institutional_accumulation_pctbreadthdiv_base_v135_signal,
    f44ia_f44_institutional_accumulation_ownpctslope_504d_base_v136_signal,
    f44ia_f44_institutional_accumulation_valrngpos_1260d_base_v137_signal,
    f44ia_f44_institutional_accumulation_holdrngpos_1260d_base_v138_signal,
    f44ia_f44_institutional_accumulation_breadthrichspr_base_v139_signal,
    f44ia_f44_institutional_accumulation_inflowperhold_base_v140_signal,
    f44ia_f44_institutional_accumulation_ownpctheadroom_504d_base_v141_signal,
    f44ia_f44_institutional_accumulation_unitheadroom_504d_base_v142_signal,
    f44ia_f44_institutional_accumulation_valshock_5d_base_v143_signal,
    f44ia_f44_institutional_accumulation_holdshock_5d_base_v144_signal,
    f44ia_f44_institutional_accumulation_valmktrs_base_v145_signal,
    f44ia_f44_institutional_accumulation_ownpctchurn_base_v146_signal,
    f44ia_f44_institutional_accumulation_holdstreak_base_v147_signal,
    f44ia_f44_institutional_accumulation_unitstreak_base_v148_signal,
    f44ia_f44_institutional_accumulation_smartscore_base_v149_signal,
    f44ia_f44_institutional_accumulation_confirmaccum_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_INSTITUTIONAL_ACCUMULATION_REGISTRY_076_150 = REGISTRY


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

    shrholders = _fund(201, base=120.0, drift=0.03, vol=0.06).rename("shrholders")
    shrunits = _fund(202, base=5.0e6, drift=0.04, vol=0.09).rename("shrunits")
    totalvalue = _fund(203, base=8.0e7, drift=0.05, vol=0.10).rename("totalvalue")
    shrvalue = _fund(204, base=9.0e6, drift=0.04, vol=0.11).rename("shrvalue")
    marketcap = _fund(205, base=3.0e8, drift=0.02, vol=0.08).rename("marketcap")

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

    print("OK f44_institutional_accumulation_base_076_150_claude: %d features pass" % n_features)
