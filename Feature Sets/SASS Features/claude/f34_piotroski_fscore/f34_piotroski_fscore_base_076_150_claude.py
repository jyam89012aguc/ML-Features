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
def _f34_soft_pos(s, scale):
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(s / sc.replace(0, np.nan))


def _f34_soft_gt(a, b, scale):
    diff = a - b
    sc = (a.abs() + b.abs()).rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(diff / sc.replace(0, np.nan))


def _f34_soft_up(s, w, scale):
    d = s - s.shift(w)
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(d / sc.replace(0, np.nan))


def _f34_soft_down(s, w, scale):
    d = s.shift(w) - s
    sc = s.abs().rolling(scale, min_periods=max(1, scale // 2)).mean()
    return np.tanh(d / sc.replace(0, np.nan))


def _f34_leverage(debt, assets):
    return _safe_div(debt, assets)


def _rollslope(s, w, mp):
    def _slope(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        xm = x.mean()
        xden = ((x - xm) ** 2).sum()
        if xden == 0:
            return np.nan
        return ((x - xm) * (a - a.mean())).sum() / xden
    return s.rolling(w, min_periods=mp).apply(_slope, raw=True)


# ============================================================
# ---- COMPONENT MAGNITUDE LEVELS (distinct windows / transforms) ----
# net-income margin proxy: netinc per unit assets, ranked vs 504d history
def f34pf_f34_piotroski_fscore_nirank_504d_base_v076_signal(netinc, assets):
    r = _safe_div(netinc, assets)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow ROA percentile-rank vs its own 504d distribution
def f34pf_f34_piotroski_fscore_cfrank_504d_base_v077_signal(ncfo, assets):
    r = _safe_div(ncfo, assets)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA level relative to its 126d vs 504d means (short vs long standing)
def f34pf_f34_piotroski_fscore_roacross_126d_base_v078_signal(roa):
    short = roa.rolling(126, min_periods=63).mean()
    long = roa.rolling(504, min_periods=252).mean()
    sc = roa.abs().rolling(504, min_periods=126).mean()
    b = np.tanh((short - long) / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual ratio (netinc-ncfo)/assets relative to its own range (Sloan z)
def f34pf_f34_piotroski_fscore_accrz_252d_base_v079_signal(netinc, ncfo, assets):
    accr = _safe_div(netinc - ncfo, assets)
    b = -_z(accr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage level ranked vs 504d history (lower rank=better, flipped)
def f34pf_f34_piotroski_fscore_levrank_504d_base_v080_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    b = 0.5 - lev.rolling(504, min_periods=126).rank(pct=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio percentile rank (liquidity standing)
def f34pf_f34_piotroski_fscore_currrank_504d_base_v081_signal(currentratio):
    b = currentratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count level vs its trailing min (issuance overhang above the low)
def f34pf_f34_piotroski_fscore_shareoverhang_504d_base_v082_signal(sharesbas):
    lo = sharesbas.rolling(504, min_periods=252).min()
    b = -np.tanh(5.0 * (_safe_div(sharesbas, lo) - 1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin percentile rank vs 504d history
def f34pf_f34_piotroski_fscore_gmrank_504d_base_v083_signal(grossmargin):
    b = grossmargin.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-turnover percentile rank vs 504d history
def f34pf_f34_piotroski_fscore_atorank_504d_base_v084_signal(assetturnover):
    b = assetturnover.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- REGRESSION-SLOPE TRENDS OF EACH PIOTROSKI INPUT ----
# OLS slope of ROA over 252d (smooth improvement rate)
def f34pf_f34_piotroski_fscore_roaslope_252d_base_v085_signal(roa):
    sl = _rollslope(roa, 252, 126)
    sc = roa.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of gross margin over 126d
def f34pf_f34_piotroski_fscore_gmslope_126d_base_v086_signal(grossmargin):
    sl = _rollslope(grossmargin, 126, 63)
    sc = grossmargin.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(126.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of current ratio over 252d (liquidity drift)
def f34pf_f34_piotroski_fscore_currslope_252d_base_v087_signal(currentratio):
    sl = _rollslope(currentratio, 252, 126)
    sc = currentratio.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of leverage over 252d (deleveraging trend, flipped)
def f34pf_f34_piotroski_fscore_levslope_252d_base_v088_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    sl = _rollslope(lev, 252, 126)
    sc = lev.abs().rolling(252, min_periods=126).mean()
    b = -np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of share count over 252d (dilution drift, flipped)
def f34pf_f34_piotroski_fscore_shareslope_252d_base_v089_signal(sharesbas):
    sl = _rollslope(sharesbas, 252, 126)
    sc = sharesbas.abs().rolling(252, min_periods=126).mean()
    b = -np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# OLS slope of cash-flow ROA over 252d
def f34pf_f34_piotroski_fscore_cfroaslope_252d_base_v090_signal(ncfo, assets):
    r = _safe_div(ncfo, assets)
    sl = _rollslope(r, 252, 126)
    sc = r.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(252.0 * sl / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- HIT-RATE / CONSISTENCY OF IMPROVEMENT ----
# fraction of last year roa rose quarter-over-quarter (improvement consistency)
def f34pf_f34_piotroski_fscore_roahit_252d_base_v091_signal(roa):
    up = (roa > roa.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year gross margin rose q/q
def f34pf_f34_piotroski_fscore_gmhit_252d_base_v092_signal(grossmargin):
    up = (grossmargin > grossmargin.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year asset turnover rose q/q
def f34pf_f34_piotroski_fscore_atohit_252d_base_v093_signal(assetturnover):
    up = (assetturnover > assetturnover.shift(63)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual-quality hit-rate: fraction of last year the cash-earnings gap widened
# in the firm's favor (ncfo growing faster than netinc), depth-weighted
def f34pf_f34_piotroski_fscore_accrhit_252d_base_v094_signal(ncfo, netinc):
    gn = _pctchg(ncfo, 63)
    ge = _pctchg(netinc, 63)
    hit = (gn > ge).astype(float)
    depth = np.tanh(2.0 * (gn - ge))
    b = hit.rolling(252, min_periods=126).mean() - 0.5 + 0.1 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year leverage fell q/q (deleveraging consistency)
def f34pf_f34_piotroski_fscore_levhit_252d_base_v095_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    down = (lev < lev.shift(63)).astype(float)
    b = down.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year netinc positive (profitability consistency)
def f34pf_f34_piotroski_fscore_nihit_252d_base_v096_signal(netinc):
    pos = (netinc > 0).astype(float)
    depth = _f34_soft_pos(netinc, 126).clip(lower=0)
    b = pos.rolling(252, min_periods=126).mean() - 0.5 + 0.05 * depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- VOLATILITY / STABILITY OF FUNDAMENTALS ----
# stability of ROA: inverse coefficient of variation (steady earnings quality)
def f34pf_f34_piotroski_fscore_roastab_252d_base_v097_signal(roa):
    sd = roa.rolling(252, min_periods=126).std()
    mn = roa.rolling(252, min_periods=126).mean().abs()
    b = -np.tanh(sd / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stability of gross margin (margin durability)
def f34pf_f34_piotroski_fscore_gmstab_252d_base_v098_signal(grossmargin):
    sd = grossmargin.rolling(252, min_periods=126).std()
    mn = grossmargin.rolling(252, min_periods=126).mean().abs()
    b = -np.tanh(10.0 * sd / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow downside risk: semivariance of ncfo growth (asymmetric stability), flipped
def f34pf_f34_piotroski_fscore_cfstab_252d_base_v099_signal(ncfo):
    g = _pctchg(ncfo, 21)
    downs = g.where(g < 0, 0.0)
    semi = (downs ** 2).rolling(252, min_periods=126).mean() ** 0.5
    b = -np.tanh(10.0 * semi)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stability of leverage (low volatility = predictable balance sheet)
def f34pf_f34_piotroski_fscore_levstab_252d_base_v100_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    sd = lev.rolling(252, min_periods=126).std()
    mn = lev.rolling(252, min_periods=126).mean().abs()
    b = -np.tanh(5.0 * sd / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- MULTI-COMPONENT COMPOSITES (distinct subset combos) ----
# balance-sheet trust composite: deleverage + liquidity + share discipline (slopes)
def f34pf_f34_piotroski_fscore_bstrust_252d_base_v101_signal(debt, assets, currentratio, sharesbas):
    lev = _f34_leverage(debt, assets)
    c5 = -np.tanh(252.0 * _rollslope(lev, 252, 126) / lev.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c6 = np.tanh(252.0 * _rollslope(currentratio, 252, 126) / currentratio.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c7 = -np.tanh(252.0 * _rollslope(sharesbas, 252, 126) / sharesbas.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = (c5 + c6 + c7) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-quality composite: ROA + margin + turnover slopes (DuPont improvement)
def f34pf_f34_piotroski_fscore_opqual_252d_base_v102_signal(roa, grossmargin, assetturnover):
    c3 = np.tanh(252.0 * _rollslope(roa, 252, 126) / roa.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c8 = np.tanh(252.0 * _rollslope(grossmargin, 252, 126) / grossmargin.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c9 = np.tanh(252.0 * _rollslope(assetturnover, 252, 126) / assetturnover.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = (c3 + c8 + c9) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-earnings quality composite: positive cash + accrual + cash stability
def f34pf_f34_piotroski_fscore_cashqual_252d_base_v103_signal(ncfo, netinc, assets):
    pos = _f34_soft_pos(ncfo, 252)
    accr = _f34_soft_gt(ncfo, netinc, 252)
    sd = ncfo.rolling(252, min_periods=126).std()
    mn = ncfo.rolling(252, min_periods=126).mean().abs()
    stab = -np.tanh(sd / mn.replace(0, np.nan))
    b = (pos + accr + stab) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score hit-rate composite: average of the 6 improvement hit-rates (breadth of momentum)
def f34pf_f34_piotroski_fscore_hitcomp_252d_base_v104_signal(
        roa, grossmargin, assetturnover, currentratio, ncfo, netinc, debt, assets):
    h3 = (roa > roa.shift(63)).astype(float)
    h8 = (grossmargin > grossmargin.shift(63)).astype(float)
    h9 = (assetturnover > assetturnover.shift(63)).astype(float)
    h6 = (currentratio > currentratio.shift(63)).astype(float)
    h4 = (ncfo > netinc).astype(float)
    lev = _f34_leverage(debt, assets)
    h5 = (lev < lev.shift(63)).astype(float)
    raw = (h3 + h8 + h9 + h6 + h4 + h5) / 6.0
    b = raw.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weakest-improvement composite: min of the operating-improvement slopes
def f34pf_f34_piotroski_fscore_minimprove_252d_base_v105_signal(roa, grossmargin, assetturnover):
    c3 = _f34_soft_up(roa, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    b = pd.concat([c3, c8, c9], axis=1).min(axis=1).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- INTERACTIONS WITH MAGNITUDE WEIGHTING ----
# ROA improvement scaled by current profitability level (improving from strength)
def f34pf_f34_piotroski_fscore_roaimpxlvl_252d_base_v106_signal(roa, netinc, assets):
    impr = _f34_soft_up(roa, 252, 252)
    lvl = np.tanh(2.0 * _safe_div(netinc, assets))
    b = impr * (1.0 + lvl) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion weighted by turnover level (efficient margin growth)
def f34pf_f34_piotroski_fscore_gmxatolvl_252d_base_v107_signal(grossmargin, assetturnover):
    dgm = _f34_soft_up(grossmargin, 252, 252)
    atolvl = np.tanh(_z(assetturnover, 252))
    b = dgm + 0.5 * dgm * atolvl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-earnings burden trend: debt/netinc multiple direction (years-to-repay)
def f34pf_f34_piotroski_fscore_delevxprof_252d_base_v108_signal(debt, assets, netinc):
    burden = _safe_div(debt, netinc)
    b = -np.tanh(0.5 * _chg(burden, 252) / burden.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual quality scaled by ROA level (clean earnings at high returns)
def f34pf_f34_piotroski_fscore_accrxroalvl_252d_base_v109_signal(ncfo, netinc, assets):
    accr = _f34_soft_gt(ncfo, netinc, 252)
    roalvl = np.tanh(3.0 * _safe_div(netinc, assets))
    b = accr * (1.0 + roalvl.abs()) / 2.0 * np.sign(accr)
    b = accr + 0.4 * accr * roalvl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity improvement net of dilution (self-funded balance-sheet repair)
def f34pf_f34_piotroski_fscore_currnetdil_252d_base_v110_signal(currentratio, sharesbas):
    dcurr = _f34_soft_up(currentratio, 252, 252)
    dil = _f34_soft_up(sharesbas, 252, 252)
    b = dcurr - 0.6 * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- F-SCORE COMPOSITE TRAJECTORY / DYNAMICS ----
# continuous F-score momentum: 63d change in the 8-component composite
def f34pf_f34_piotroski_fscore_fsmom_63d_base_v111_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126)
    c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 63, 126)
    c4 = _f34_soft_gt(ncfo, netinc, 126)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 63, 126)
    c6 = _f34_soft_up(currentratio, 63, 126)
    c8 = _f34_soft_up(grossmargin, 63, 126)
    c9 = _f34_soft_up(assetturnover, 63, 126)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    b = fs - fs.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score volatility: how unstable the composite is (regime uncertainty)
def f34pf_f34_piotroski_fscore_fsvol_252d_base_v112_signal(
        netinc, ncfo, roa, assets, debt, currentratio, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 126)
    c2 = _f34_soft_pos(ncfo, 126)
    c3 = _f34_soft_up(roa, 126, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 126)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 126, 252)
    c6 = _f34_soft_up(currentratio, 126, 252)
    c8 = _f34_soft_up(grossmargin, 126, 252)
    c9 = _f34_soft_up(assetturnover, 126, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c8 + c9) / 8.0
    b = fs.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score EMA displacement: composite minus its own slow EMA (fresh improvement)
def f34pf_f34_piotroski_fscore_fsdisp_252d_base_v113_signal(
        netinc, ncfo, roa, assets, debt, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c8 + c9) / 7.0
    b = fs - fs.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score regime: sign of composite weighted by its persistence
def f34pf_f34_piotroski_fscore_fsregime_252d_base_v114_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    persist = (np.sign(fs) == np.sign(fs.shift(63))).astype(float).rolling(126, min_periods=63).mean()
    b = np.sign(fs) * persist + 0.001 * fs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# F-score drawdown: composite vs its trailing 252d max (deterioration depth)
def f34pf_f34_piotroski_fscore_fsdd_252d_base_v115_signal(
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
    peak = fs.rolling(252, min_periods=126).max()
    b = fs - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- DUPONT / DRIVER DECOMPOSITION ----
# ROA driver attribution: is improvement margin-led or turnover-led
def f34pf_f34_piotroski_fscore_dupontlead_252d_base_v116_signal(grossmargin, assetturnover):
    dgm = _f34_soft_up(grossmargin, 252, 252)
    dato = _f34_soft_up(assetturnover, 252, 252)
    b = dgm - dato
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied ROA from margin x turnover vs reported ROA (consistency check)
def f34pf_f34_piotroski_fscore_roaimplied_252d_base_v117_signal(grossmargin, assetturnover, roa):
    implied = grossmargin * assetturnover
    gap = _safe_div(roa - implied, implied.abs().rolling(252, min_periods=126).mean())
    b = np.tanh(gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-times-turnover growth (synthetic ROA growth via DuPont)
def f34pf_f34_piotroski_fscore_dupontgrow_252d_base_v118_signal(grossmargin, assetturnover):
    prod = grossmargin * assetturnover
    b = np.tanh(3.0 * _pctchg(prod, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- LONG-HORIZON & ACCELERATION COMPOSITES ----
# 2y improvement: ROA change over 504d (durable return improvement)
def f34pf_f34_piotroski_fscore_roa2y_504d_base_v119_signal(roa):
    b = _f34_soft_up(roa, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2y deleveraging: leverage change over 504d
def f34pf_f34_piotroski_fscore_lev2y_504d_base_v120_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    b = _f34_soft_down(lev, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2y margin expansion
def f34pf_f34_piotroski_fscore_gm2y_504d_base_v121_signal(grossmargin):
    b = _f34_soft_up(grossmargin, 504, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ROA improvement acceleration: 126d change of the 126d ROA change
def f34pf_f34_piotroski_fscore_roaaccel_126d_base_v122_signal(roa):
    d = _chg(roa, 126)
    accel = d - d.shift(126)
    sc = roa.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(accel / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin expansion acceleration
def f34pf_f34_piotroski_fscore_gmaccel_126d_base_v123_signal(grossmargin):
    d = _chg(grossmargin, 126)
    accel = d - d.shift(126)
    sc = grossmargin.abs().rolling(252, min_periods=126).mean()
    b = np.tanh(accel / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trajectory acceleration (paydown speeding up, flipped)
def f34pf_f34_piotroski_fscore_levaccel_126d_base_v124_signal(debt, assets):
    lev = _f34_leverage(debt, assets)
    d = _chg(lev, 126)
    accel = d - d.shift(126)
    sc = lev.abs().rolling(252, min_periods=126).mean()
    b = -np.tanh(accel / sc.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- CROSS-METRIC SPREADS & RATIOS ----
# cash-vs-earnings spread trend (accrual reversal momentum)
def f34pf_f34_piotroski_fscore_cespread_252d_base_v125_signal(ncfo, netinc, assets):
    spread = _safe_div(ncfo - netinc, assets)
    b = np.tanh(5.0 * _chg(spread, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# profitability-to-leverage ratio (returns earned per unit balance-sheet risk)
def f34pf_f34_piotroski_fscore_proflevratio_252d_base_v126_signal(netinc, assets, debt):
    roaq = _safe_div(netinc, assets)
    lev = _f34_leverage(debt, assets)
    ratio = _safe_div(roaq, lev)
    b = np.tanh(ratio / ratio.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-to-turnover ratio change (idle-liquidity vs efficiency tension)
def f34pf_f34_piotroski_fscore_liqturn_252d_base_v127_signal(currentratio, assetturnover):
    ratio = _safe_div(currentratio, assetturnover)
    b = -np.tanh(2.0 * _pctchg(ratio, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-minus-turnover level spread (business-model tilt)
def f34pf_f34_piotroski_fscore_gmatospread_252d_base_v128_signal(grossmargin, assetturnover):
    b = np.tanh(_z(grossmargin, 252) - _z(assetturnover, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow to debt change (debt-service capacity trend)
def f34pf_f34_piotroski_fscore_cfdebt_252d_base_v129_signal(ncfo, debt):
    cover = _safe_div(ncfo, debt)
    b = np.tanh(2.0 * _pctchg(cover, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- DISCRETE F-SCORE TALLIES (smoothed for nunique) ----
# count of profitability binaries met (0-4), depth-jittered & smoothed
def f34pf_f34_piotroski_fscore_proftally_252d_base_v130_signal(netinc, ncfo, roa, assets):
    s = (
        (netinc > 0).astype(float)
        + (ncfo > 0).astype(float)
        + (_chg(roa, 252) > 0).astype(float)
        + (ncfo > netinc).astype(float)
    )
    jitter = (_z(_safe_div(netinc, assets), 252)) * 0.02
    b = (s + jitter).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of leverage/liquidity binaries met (0-3), smoothed
def f34pf_f34_piotroski_fscore_levtally_252d_base_v131_signal(debt, assets, currentratio, sharesbas):
    lev = _f34_leverage(debt, assets)
    s = (
        (_chg(lev, 252) < 0).astype(float)
        + (_chg(currentratio, 252) > 0).astype(float)
        + (_chg(sharesbas, 252) <= 0).astype(float)
    )
    jitter = (_z(currentratio, 252)) * 0.02
    b = (s + jitter).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of efficiency binaries met (0-2), smoothed
def f34pf_f34_piotroski_fscore_efftally_252d_base_v132_signal(grossmargin, assetturnover):
    s = (
        (_chg(grossmargin, 252) > 0).astype(float)
        + (_chg(assetturnover, 252) > 0).astype(float)
    )
    jitter = (_z(grossmargin, 252)) * 0.02
    b = (s + jitter).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full discrete F-score (0-9) smoothed over a quarter with magnitude jitter
def f34pf_f34_piotroski_fscore_fulltally_252d_base_v133_signal(
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
    jitter = (_z(_safe_div(ncfo, assets), 252)) * 0.03
    b = (s + jitter).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- ADDITIONAL DISTINCT MAGNITUDE-COMPOSITES ----
# high-quality-improver score: the WEAKEST of {positive earnings, improving ROA,
# clean accruals} governs (a chain is only as strong as its weakest link)
def f34pf_f34_piotroski_fscore_hqimprover_252d_base_v134_signal(netinc, ncfo, roa, assets):
    a = _f34_soft_pos(netinc, 126)
    b2 = _f34_soft_up(roa, 126, 126)
    c = _f34_soft_gt(ncfo, netinc, 126)
    weak = pd.concat([a, b2, c], axis=1).min(axis=1)
    b = weak.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fragility score: high leverage AND deteriorating margins (distress tilt, flipped)
def f34pf_f34_piotroski_fscore_fragility_252d_base_v135_signal(debt, assets, grossmargin):
    lev = (np.tanh(_z(_f34_leverage(debt, assets), 252)) + 1) / 2
    margdet = (_f34_soft_down(grossmargin, 252, 252) + 1) / 2
    b = -(lev * margdet) + 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround tilt: improving operations from a weak (low-ROA) starting point
def f34pf_f34_piotroski_fscore_turnaround_252d_base_v136_signal(roa, grossmargin, netinc, assets):
    weak = (-np.tanh(3.0 * _safe_div(netinc, assets)) + 1) / 2
    impr = (_f34_soft_up(roa, 252, 252) + _f34_soft_up(grossmargin, 252, 252)) / 2.0
    impr01 = (impr + 1) / 2
    b = weak * impr01 - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding score: cash flow covers growth without dilution or leverage-up
def f34pf_f34_piotroski_fscore_selffund_252d_base_v137_signal(ncfo, assets, sharesbas, debt):
    cf = np.tanh(3.0 * _safe_div(ncfo, assets))
    nodil = _f34_soft_down(sharesbas, 252, 252)
    delev = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    b = (cf + nodil + delev) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-quality gate: accrual-quality trend gated by whether cash flow is rising
# (clean earnings only credited when cash generation itself is improving)
def f34pf_f34_piotroski_fscore_qualitygate_252d_base_v138_signal(roa, ncfo, netinc):
    accrtrend = np.tanh(3.0 * _chg(_f34_soft_gt(ncfo, netinc, 126), 126))
    cfrising = (_f34_soft_up(ncfo, 126, 126) + 1) / 2
    b = accrtrend * cfrising
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance-strength gate: margin expansion only counts with stable balance sheet
def f34pf_f34_piotroski_fscore_strengthgate_252d_base_v139_signal(grossmargin, debt, assets):
    dgm = _f34_soft_up(grossmargin, 252, 252)
    lev = _f34_leverage(debt, assets)
    gate = (1.0 - np.tanh(lev.clip(lower=0)))
    b = dgm * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- F-SCORE vs SECTOR-LIKE NORMALIZATION (self-history percentile composites) ----
# composite percentile rank over a longer 756d window (cycle-aware standing)
def f34pf_f34_piotroski_fscore_fsrank_756d_base_v140_signal(
        netinc, ncfo, roa, assets, debt, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = _f34_soft_down(_f34_leverage(debt, assets), 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c5 + c8 + c9) / 7.0
    b = fs.rolling(756, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# improvement-breadth diffusion: how many of 6 metrics are above their 252d mean
def f34pf_f34_piotroski_fscore_diffusion_252d_base_v141_signal(
        roa, grossmargin, assetturnover, currentratio, ncfo, assets):
    cfroa = _safe_div(ncfo, assets)
    metrics = [roa, grossmargin, assetturnover, currentratio, cfroa, _safe_div(ncfo, assets).diff()]
    diff = None
    for s in [roa, grossmargin, assetturnover, currentratio, cfroa]:
        z = (s > s.rolling(252, min_periods=126).mean()).astype(float)
        diff = z if diff is None else diff + z
    jitter = _z(roa, 252) * 0.02
    b = (diff / 5.0 + jitter).rolling(21, min_periods=10).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite minus its 1y-ago value (year-over-year F-score change)
def f34pf_f34_piotroski_fscore_fsyoy_252d_base_v142_signal(
        netinc, ncfo, roa, assets, currentratio, grossmargin):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = _f34_soft_up(roa, 252, 252)
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    fs = (c1 + c2 + c3 + c4 + c6 + c8) / 6.0
    b = fs - fs.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ============================================================
# ---- FINAL DISTINCT MAGNITUDE FEATURES ----
# return-on-assets level minus cash-ROA level (earnings overstatement proxy, flipped)
def f34pf_f34_piotroski_fscore_roaminuscf_252d_base_v143_signal(netinc, ncfo, assets):
    roaq = _safe_div(netinc, assets)
    cfroa = _safe_div(ncfo, assets)
    b = -np.tanh(5.0 * (roaq - cfroa))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net solvency: leverage level relative to current-ratio cushion (structural risk)
def f34pf_f34_piotroski_fscore_netsolv_252d_base_v144_signal(debt, assets, currentratio):
    lev = _f34_leverage(debt, assets)
    risk = _safe_div(lev, currentratio)
    b = -np.tanh(_z(risk, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow growth net of share growth (per-share cash accretion)
def f34pf_f34_piotroski_fscore_cfaccrete_252d_base_v145_signal(ncfo, sharesbas):
    cfg = _pctchg(ncfo, 252)
    shg = _pctchg(sharesbas, 252)
    b = np.tanh(2.0 * (cfg - shg))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conviction: level-based quality composite (profitability & efficiency LEVELS,
# not improvements) scaled by its dispersion — a standing-quality magnitude
def f34pf_f34_piotroski_fscore_conviction_252d_base_v146_signal(
        netinc, ncfo, roa, assets, debt, grossmargin):
    l1 = np.tanh(2.0 * _safe_div(netinc, assets))
    l2 = np.tanh(2.0 * _safe_div(ncfo, assets))
    l5 = -np.tanh(_z(_f34_leverage(debt, assets), 252))
    l8 = np.tanh(_z(grossmargin, 252))
    levels = (l1 + l2 + l5 + l8) / 4.0
    disp = pd.concat([l1, l2, l5, l8], axis=1).std(axis=1)
    b = levels * (1.0 - disp.clip(upper=1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover-efficiency improvement scaled by margin stability (durable efficiency)
def f34pf_f34_piotroski_fscore_dureffic_252d_base_v147_signal(assetturnover, grossmargin):
    dato = _f34_soft_up(assetturnover, 252, 252)
    sd = grossmargin.rolling(252, min_periods=126).std()
    mn = grossmargin.rolling(252, min_periods=126).mean().abs()
    stab = (1.0 - np.tanh(10.0 * sd / mn.replace(0, np.nan)))
    b = dato * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reliability: rolling correlation of ROA and cash-ROA (do they agree)
def f34pf_f34_piotroski_fscore_accrreliab_252d_base_v148_signal(roa, ncfo, assets):
    cfroa = _safe_div(ncfo, assets)
    b = roa.rolling(252, min_periods=126).corr(cfroa)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# improvement persistence: how long the composite has stayed positive (streak frac)
def f34pf_f34_piotroski_fscore_imppersist_252d_base_v149_signal(
        roa, grossmargin, assetturnover, currentratio):
    c3 = _f34_soft_up(roa, 252, 252)
    c8 = _f34_soft_up(grossmargin, 252, 252)
    c9 = _f34_soft_up(assetturnover, 252, 252)
    c6 = _f34_soft_up(currentratio, 252, 252)
    fs = (c3 + c8 + c9 + c6) / 4.0
    pos = (fs > 0).astype(float)
    streak = pos.rolling(252, min_periods=126).mean()
    b = streak - 0.5 + 0.05 * fs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overall financial-health index: blended slope composite z-scored (final summary)
def f34pf_f34_piotroski_fscore_healthindex_252d_base_v150_signal(
        netinc, ncfo, roa, assets, debt, currentratio, sharesbas, grossmargin, assetturnover):
    c1 = _f34_soft_pos(netinc, 252)
    c2 = _f34_soft_pos(ncfo, 252)
    c3 = np.tanh(252.0 * _rollslope(roa, 252, 126) / roa.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c4 = _f34_soft_gt(ncfo, netinc, 252)
    c5 = -np.tanh(252.0 * _rollslope(_f34_leverage(debt, assets), 252, 126) / _f34_leverage(debt, assets).abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c6 = np.tanh(252.0 * _rollslope(currentratio, 252, 126) / currentratio.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c7 = _f34_soft_down(sharesbas, 252, 252)
    c8 = np.tanh(252.0 * _rollslope(grossmargin, 252, 126) / grossmargin.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    c9 = np.tanh(252.0 * _rollslope(assetturnover, 252, 126) / assetturnover.abs().rolling(252, min_periods=126).mean().replace(0, np.nan))
    fs = (c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9) / 9.0
    b = _z(fs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34pf_f34_piotroski_fscore_nirank_504d_base_v076_signal,
    f34pf_f34_piotroski_fscore_cfrank_504d_base_v077_signal,
    f34pf_f34_piotroski_fscore_roacross_126d_base_v078_signal,
    f34pf_f34_piotroski_fscore_accrz_252d_base_v079_signal,
    f34pf_f34_piotroski_fscore_levrank_504d_base_v080_signal,
    f34pf_f34_piotroski_fscore_currrank_504d_base_v081_signal,
    f34pf_f34_piotroski_fscore_shareoverhang_504d_base_v082_signal,
    f34pf_f34_piotroski_fscore_gmrank_504d_base_v083_signal,
    f34pf_f34_piotroski_fscore_atorank_504d_base_v084_signal,
    f34pf_f34_piotroski_fscore_roaslope_252d_base_v085_signal,
    f34pf_f34_piotroski_fscore_gmslope_126d_base_v086_signal,
    f34pf_f34_piotroski_fscore_currslope_252d_base_v087_signal,
    f34pf_f34_piotroski_fscore_levslope_252d_base_v088_signal,
    f34pf_f34_piotroski_fscore_shareslope_252d_base_v089_signal,
    f34pf_f34_piotroski_fscore_cfroaslope_252d_base_v090_signal,
    f34pf_f34_piotroski_fscore_roahit_252d_base_v091_signal,
    f34pf_f34_piotroski_fscore_gmhit_252d_base_v092_signal,
    f34pf_f34_piotroski_fscore_atohit_252d_base_v093_signal,
    f34pf_f34_piotroski_fscore_accrhit_252d_base_v094_signal,
    f34pf_f34_piotroski_fscore_levhit_252d_base_v095_signal,
    f34pf_f34_piotroski_fscore_nihit_252d_base_v096_signal,
    f34pf_f34_piotroski_fscore_roastab_252d_base_v097_signal,
    f34pf_f34_piotroski_fscore_gmstab_252d_base_v098_signal,
    f34pf_f34_piotroski_fscore_cfstab_252d_base_v099_signal,
    f34pf_f34_piotroski_fscore_levstab_252d_base_v100_signal,
    f34pf_f34_piotroski_fscore_bstrust_252d_base_v101_signal,
    f34pf_f34_piotroski_fscore_opqual_252d_base_v102_signal,
    f34pf_f34_piotroski_fscore_cashqual_252d_base_v103_signal,
    f34pf_f34_piotroski_fscore_hitcomp_252d_base_v104_signal,
    f34pf_f34_piotroski_fscore_minimprove_252d_base_v105_signal,
    f34pf_f34_piotroski_fscore_roaimpxlvl_252d_base_v106_signal,
    f34pf_f34_piotroski_fscore_gmxatolvl_252d_base_v107_signal,
    f34pf_f34_piotroski_fscore_delevxprof_252d_base_v108_signal,
    f34pf_f34_piotroski_fscore_accrxroalvl_252d_base_v109_signal,
    f34pf_f34_piotroski_fscore_currnetdil_252d_base_v110_signal,
    f34pf_f34_piotroski_fscore_fsmom_63d_base_v111_signal,
    f34pf_f34_piotroski_fscore_fsvol_252d_base_v112_signal,
    f34pf_f34_piotroski_fscore_fsdisp_252d_base_v113_signal,
    f34pf_f34_piotroski_fscore_fsregime_252d_base_v114_signal,
    f34pf_f34_piotroski_fscore_fsdd_252d_base_v115_signal,
    f34pf_f34_piotroski_fscore_dupontlead_252d_base_v116_signal,
    f34pf_f34_piotroski_fscore_roaimplied_252d_base_v117_signal,
    f34pf_f34_piotroski_fscore_dupontgrow_252d_base_v118_signal,
    f34pf_f34_piotroski_fscore_roa2y_504d_base_v119_signal,
    f34pf_f34_piotroski_fscore_lev2y_504d_base_v120_signal,
    f34pf_f34_piotroski_fscore_gm2y_504d_base_v121_signal,
    f34pf_f34_piotroski_fscore_roaaccel_126d_base_v122_signal,
    f34pf_f34_piotroski_fscore_gmaccel_126d_base_v123_signal,
    f34pf_f34_piotroski_fscore_levaccel_126d_base_v124_signal,
    f34pf_f34_piotroski_fscore_cespread_252d_base_v125_signal,
    f34pf_f34_piotroski_fscore_proflevratio_252d_base_v126_signal,
    f34pf_f34_piotroski_fscore_liqturn_252d_base_v127_signal,
    f34pf_f34_piotroski_fscore_gmatospread_252d_base_v128_signal,
    f34pf_f34_piotroski_fscore_cfdebt_252d_base_v129_signal,
    f34pf_f34_piotroski_fscore_proftally_252d_base_v130_signal,
    f34pf_f34_piotroski_fscore_levtally_252d_base_v131_signal,
    f34pf_f34_piotroski_fscore_efftally_252d_base_v132_signal,
    f34pf_f34_piotroski_fscore_fulltally_252d_base_v133_signal,
    f34pf_f34_piotroski_fscore_hqimprover_252d_base_v134_signal,
    f34pf_f34_piotroski_fscore_fragility_252d_base_v135_signal,
    f34pf_f34_piotroski_fscore_turnaround_252d_base_v136_signal,
    f34pf_f34_piotroski_fscore_selffund_252d_base_v137_signal,
    f34pf_f34_piotroski_fscore_qualitygate_252d_base_v138_signal,
    f34pf_f34_piotroski_fscore_strengthgate_252d_base_v139_signal,
    f34pf_f34_piotroski_fscore_fsrank_756d_base_v140_signal,
    f34pf_f34_piotroski_fscore_diffusion_252d_base_v141_signal,
    f34pf_f34_piotroski_fscore_fsyoy_252d_base_v142_signal,
    f34pf_f34_piotroski_fscore_roaminuscf_252d_base_v143_signal,
    f34pf_f34_piotroski_fscore_netsolv_252d_base_v144_signal,
    f34pf_f34_piotroski_fscore_cfaccrete_252d_base_v145_signal,
    f34pf_f34_piotroski_fscore_conviction_252d_base_v146_signal,
    f34pf_f34_piotroski_fscore_dureffic_252d_base_v147_signal,
    f34pf_f34_piotroski_fscore_accrreliab_252d_base_v148_signal,
    f34pf_f34_piotroski_fscore_imppersist_252d_base_v149_signal,
    f34pf_f34_piotroski_fscore_healthindex_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_PIOTROSKI_FSCORE_REGISTRY_076_150 = REGISTRY


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

    print("OK f34_piotroski_fscore_base_076_150_claude: %d features pass" % n_features)
