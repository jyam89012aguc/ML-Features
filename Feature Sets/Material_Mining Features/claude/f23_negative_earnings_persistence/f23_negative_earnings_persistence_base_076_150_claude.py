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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (negative earnings persistence) =====
def _f23_isloss(s):
    return (s < 0.0).astype(float)


def _f23_losscount(s, w):
    return _f23_isloss(s).rolling(w, min_periods=max(1, w // 2)).mean()


def _f23_losssum(s, w):
    return _f23_isloss(s).rolling(w, min_periods=max(1, w // 2)).sum()


def _f23_lossdepth(s, scale):
    return (-s).clip(lower=0.0) / float(scale)


def _f23_profitdepth(s, scale):
    return s.clip(lower=0.0) / float(scale)


def _f23_streak_loss(s):
    loss = _f23_isloss(s)
    grp = (loss == 0).cumsum()
    return loss.groupby(grp).cumsum()


def _f23_streak_profit(s):
    prof = (s > 0.0).astype(float)
    grp = (prof == 0).cumsum()
    return prof.groupby(grp).cumsum()


def _f23_time_since_profit(s):
    prof = (s > 0.0)
    idx = np.arange(len(s), dtype=float)
    last = pd.Series(np.where(prof.values, idx, np.nan), index=s.index).ffill()
    return pd.Series(idx, index=s.index) - last


def _f23_deficit_growth(retearn, w):
    return (retearn.shift(w) - retearn) / float(w)


def _f23_signmag(s, scale):
    return np.sign(s) * np.sqrt(s.abs() / float(scale))


# ============================================================
# --- LOSS-PERSISTENCE SMOOTHED / EWM FORMS ---
# EWM-smoothed net-loss persistence (sticky chronic-loss regime)
def f23ne_f23_negative_earnings_persistence_lossfracema_base_v076_signal(netinc):
    lf = _f23_losscount(netinc, 126)
    b = lf.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-loss persistence minus its slow EWM (loss-regime displacement)
def f23ne_f23_negative_earnings_persistence_lossfracdisp_base_v077_signal(netinc):
    lf = _f23_losscount(netinc, 126)
    b = lf - lf.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWM-smoothed cash-burn persistence (sticky burn regime)
def f23ne_f23_negative_earnings_persistence_burnfracema_base_v078_signal(ncfo):
    bf = _f23_losscount(ncfo, 126)
    b = bf.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CROSS-METRIC DISPERSION OF LOSS PERSISTENCE ---
# dispersion of loss persistence across netinc/ncfo/ebit (signal disagreement)
def f23ne_f23_negative_earnings_persistence_lossdisp_base_v079_signal(netinc, ncfo, ebit):
    a = _f23_losscount(netinc, 252)
    c = _f23_losscount(ncfo, 252)
    d = _f23_losscount(ebit, 252)
    b = pd.concat([a, c, d], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# which flow leads the loss: net-loss persistence rank within the three-flow set
def f23ne_f23_negative_earnings_persistence_lossrange_base_v080_signal(netinc, ncfo, ebit):
    a = _f23_losscount(netinc, 252)
    c = _f23_losscount(ncfo, 252)
    d = _f23_losscount(ebit, 252)
    # how dominant is net-income loss persistence vs the average of the other two
    b = a - (c + d) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ACCRUAL vs CASH LOSS DIVERGENCE ---
# net-loss persistence minus cash-burn persistence (accrual-vs-cash loss gap)
def f23ne_f23_negative_earnings_persistence_accrcashgap_base_v081_signal(netinc, ncfo):
    a = _f23_losscount(netinc, 252)
    c = _f23_losscount(ncfo, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-loss persistence minus net-loss persistence (below-the-line drag)
def f23ne_f23_negative_earnings_persistence_belowline_base_v082_signal(ebit, netinc):
    a = _f23_losscount(ebit, 252)
    c = _f23_losscount(netinc, 252)
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEFICIT-GROWTH FAMILY ---
# accumulated-deficit growth rate over a half-year, signed-log compressed
def f23ne_f23_negative_earnings_persistence_deficitgr_126d_base_v083_signal(retearn):
    dg = _f23_deficit_growth(retearn, 126)
    b = np.sign(dg) * np.log1p(dg.abs() / 1e5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deficit-growth acceleration proxy: half-year growth vs prior half-year
def f23ne_f23_negative_earnings_persistence_deficitgrchg_base_v084_signal(retearn):
    dg = _f23_deficit_growth(retearn, 126)
    b = np.tanh((dg - dg.shift(126)) / 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year retained earnings actively declined (deficit-building days)
def f23ne_f23_negative_earnings_persistence_deficitbuild_base_v085_signal(retearn):
    decl = (retearn < retearn.shift(1)).astype(float)
    b = decl.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-DEPTH RELATIVE LEVELS ---
# current net-loss depth relative to its trailing-year typical loss depth (acute)
def f23ne_f23_negative_earnings_persistence_lossdepthrel_base_v086_signal(netinc):
    d = _f23_lossdepth(netinc, 1.0)
    typ = d.rolling(252, min_periods=126).mean()
    b = d / (typ + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-loss depth percentile-ranked vs its own two-year history (loss-depth position)
def f23ne_f23_negative_earnings_persistence_lossdepthz_base_v087_signal(netinc):
    d = _f23_lossdepth(netinc, 1e7).rolling(21, min_periods=10).mean()
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT loss-depth relative to its own typical depth (operating-loss acuteness)
def f23ne_f23_negative_earnings_persistence_ebitdepthrel_base_v088_signal(ebit):
    d = _f23_lossdepth(ebit, 1.0)
    typ = d.rolling(504, min_periods=252).mean()
    b = d / (typ + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TIME-SINCE-PROFITABLE TRANSFORMS ---
# time-since-profit (netinc) ranked vs its own history (relative dry-spell length)
def f23ne_f23_negative_earnings_persistence_tsnirank_base_v089_signal(netinc):
    t = _f23_time_since_profit(netinc)
    b = _rank(t, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of time-since-EBIT-profit to time-since-net-profit (operating vs bottom-line)
def f23ne_f23_negative_earnings_persistence_tsratio_base_v090_signal(ebit, netinc):
    te = _f23_time_since_profit(ebit)
    tn = _f23_time_since_profit(netinc)
    b = (te + 5.0) / (tn + 5.0) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest dry spell within two years, depth-weighted by mean loss size (severe drought)
def f23ne_f23_negative_earnings_persistence_maxdry_base_v091_signal(netinc):
    t = _f23_time_since_profit(netinc)
    longest = np.log1p(t.rolling(504, min_periods=252).max())
    depth = _f23_lossdepth(netinc, 1e7).rolling(126, min_periods=63).mean()
    b = longest * (1.0 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- PROFIT-RECOVERY FAMILY ---
# fraction of the year that was profitable (recovery breadth, netinc)
def f23ne_f23_negative_earnings_persistence_proffrac_base_v092_signal(netinc):
    b = (netinc > 0).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest profitable streak within two years, profit-depth-weighted (durable recovery)
def f23ne_f23_negative_earnings_persistence_maxprofstreak_base_v093_signal(netinc):
    streak = _f23_streak_profit(netinc)
    longest = streak.rolling(504, min_periods=252).max()
    pdepth = _f23_profitdepth(netinc, 1e7).rolling(126, min_periods=63).mean()
    b = longest + 15.0 * pdepth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# profit-streak vs loss-streak balance (current momentum side, netinc)
def f23ne_f23_negative_earnings_persistence_streakbal_base_v094_signal(netinc):
    ps = _f23_streak_profit(netinc)
    ls = _f23_streak_loss(netinc)
    b = (ps - ls) / (ps + ls + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CUMULATIVE / INTEGRAL FORMS ---
# cumulative EBIT operating loss over the year, log-compressed (total operating drain)
def f23ne_f23_negative_earnings_persistence_cumebitloss_base_v095_signal(ebit):
    loss = (-ebit).clip(lower=0.0)
    b = np.log1p(loss.rolling(252, min_periods=126).sum() / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net loss minus cumulative profit over two years (net cash destroyed)
def f23ne_f23_negative_earnings_persistence_netdestroyed_base_v096_signal(netinc):
    loss = (-netinc).clip(lower=0.0).rolling(504, min_periods=252).sum()
    prof = netinc.clip(lower=0.0).rolling(504, min_periods=252).sum()
    b = np.sign(loss - prof) * np.log1p((loss - prof).abs() / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-WIDENING / NARROWING SLOPE FORMS ---
# slope of net-loss depth over a quarter (acute loss widening velocity)
def f23ne_f23_negative_earnings_persistence_depthvel_63d_base_v097_signal(netinc):
    d = _f23_lossdepth(netinc, 1e7).rolling(21, min_periods=10).mean()
    b = _slope(d, 63) * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-loss-depth slope over a half-year, normalized by typical depth
def f23ne_f23_negative_earnings_persistence_ebitdepthvel_base_v098_signal(ebit):
    d = _f23_lossdepth(ebit, 1.0)
    sl = _slope(d, 126) * 126.0
    typ = d.rolling(252, min_periods=126).mean()
    b = sl / (typ + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn-depth slope over a quarter (cash-burn widening velocity)
def f23ne_f23_negative_earnings_persistence_burndepthvel_base_v099_signal(ncfo):
    d = _f23_lossdepth(ncfo, 1e7).rolling(21, min_periods=10).mean()
    b = _slope(d, 63) * 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EPS FAMILY EXTENSIONS ---
# EPS percentile-rank vs its own two-year history (per-share earnings position)
def f23ne_f23_negative_earnings_persistence_epsrank_base_v100_signal(eps):
    b = _rank(eps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS loss persistence EWM-smoothed (sticky per-share loss regime)
def f23ne_f23_negative_earnings_persistence_epslossema_base_v101_signal(eps):
    lf = _f23_losscount(eps, 126)
    b = lf.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS loss-depth cumulative over the year (per-share total loss load)
def f23ne_f23_negative_earnings_persistence_epscumloss_base_v102_signal(eps):
    loss = (-eps).clip(lower=0.0)
    b = loss.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EPS signed-magnitude z-score (per-share loss/profit intensity extremity)
def f23ne_f23_negative_earnings_persistence_epssignmagz_base_v103_signal(eps):
    sm = _f23_signmag(eps, 1.0)
    b = _z(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RETAINED-EARNINGS / DEFICIT EXTENSIONS ---
# retained-earnings recovery off its two-year trough (deficit healing)
def f23ne_f23_negative_earnings_persistence_retrecov_base_v104_signal(retearn):
    trough = _rmin(retearn, 504)
    b = (retearn - trough) / (trough.abs() + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# retained-earnings drawup from trough scaled by elapsed time (healing rate)
def f23ne_f23_negative_earnings_persistence_rethealrate_base_v105_signal(retearn):
    trough = _rmin(retearn, 504)
    rec = (retearn - trough) / (trough.abs() + 1e6)
    idx = pd.Series(np.arange(len(retearn), dtype=float), index=retearn.index)
    argmin = retearn.rolling(504, min_periods=252).apply(
        lambda a: float(len(a) - 1 - int(np.argmin(a))), raw=True)
    b = rec / (argmin + 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deficit depth relative to net-loss run-rate, ranked (years-of-deficit position)
def f23ne_f23_negative_earnings_persistence_deficitvsrunrank_base_v106_signal(retearn, netinc):
    deficit = (-retearn).clip(lower=0.0)
    run = _f23_lossdepth(netinc, 1.0).rolling(252, min_periods=126).mean() * 252.0
    ratio = deficit / (run + 1e6)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- REGIME COMPOSITES / GATES ---
# both net AND operating loss persistent simultaneously (deep-loss regime fraction)
def f23ne_f23_negative_earnings_persistence_deeplossreg_base_v107_signal(netinc, ebit):
    both = ((netinc < 0) & (ebit < 0)).astype(float)
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# loss persistent AND deficit growing (compounding-distress regime fraction)
def f23ne_f23_negative_earnings_persistence_compdistress_base_v108_signal(netinc, retearn):
    cond = ((netinc < 0) & (retearn < retearn.shift(63))).astype(float)
    b = cond.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# any-flow-negative persistence (broad weakness regime fraction)
def f23ne_f23_negative_earnings_persistence_anyloss_base_v109_signal(netinc, ncfo, ebit):
    anyneg = ((netinc < 0) | (ncfo < 0) | (ebit < 0)).astype(float)
    b = anyneg.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN / LOSS RATIOS ACROSS WINDOWS ---
# burn persistence ratio: half-year vs two-year (acute-vs-chronic burn, multiplicative)
def f23ne_f23_negative_earnings_persistence_burnratio_base_v110_signal(ncfo):
    s = _f23_losscount(ncfo, 126)
    l = _f23_losscount(ncfo, 504)
    b = (s + 0.05) / (l + 0.05) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT loss persistence ratio: quarter vs year (operating acute-vs-chronic)
def f23ne_f23_negative_earnings_persistence_ebitratio_base_v111_signal(ebit):
    s = _f23_losscount(ebit, 63)
    l = _f23_losscount(ebit, 252)
    b = (s + 0.05) / (l + 0.05) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COVERAGE-STYLE (cash vs accrual sign agreement) ---
# fraction of days net income and cash flow share the same sign (quality of loss)
def f23ne_f23_negative_earnings_persistence_signagree_base_v112_signal(netinc, ncfo):
    agree = (np.sign(netinc) == np.sign(ncfo)).astype(float)
    b = agree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of days EBIT and EPS share the same sign (operating vs per-share agreement)
def f23ne_f23_negative_earnings_persistence_signagree2_base_v113_signal(ebit, eps):
    agree = (np.sign(ebit) == np.sign(eps)).astype(float)
    b = agree.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SIGN-MAGNITUDE COMPOSITES ---
# net-income signed-magnitude smoothed over a quarter (persistent loss intensity)
def f23ne_f23_negative_earnings_persistence_nisignmagsm_base_v114_signal(netinc):
    sm = _f23_signmag(netinc, 1e6)
    b = sm.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT signed-magnitude minus its own slow EMA (operating-sign displacement)
def f23ne_f23_negative_earnings_persistence_ebitsignmagdisp_base_v115_signal(ebit):
    sm = _f23_signmag(ebit, 1e6)
    b = sm - sm.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow loss/profit tendency: average sign of operating cash flow (burn-sign tilt)
def f23ne_f23_negative_earnings_persistence_meansign_base_v116_signal(ncfo):
    b = np.sign(ncfo).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- INSTABILITY / VOLATILITY OF LOSS REGIME ---
# volatility of net-loss persistence itself (regime instability)
def f23ne_f23_negative_earnings_persistence_lossfracvol_base_v117_signal(netinc):
    lf = _f23_losscount(netinc, 63)
    b = lf.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of EBIT around zero scaled by typical magnitude (operating swing)
def f23ne_f23_negative_earnings_persistence_ebitvol_base_v118_signal(ebit):
    sd = ebit.rolling(252, min_periods=126).std()
    lvl = ebit.abs().rolling(252, min_periods=126).mean()
    b = sd / (lvl + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation of net income (loss-side dispersion only)
def f23ne_f23_negative_earnings_persistence_nisemidev_base_v119_signal(netinc):
    neg = netinc.where(netinc < 0, 0.0)
    b = neg.rolling(252, min_periods=126).std() / 1e6
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- WORST-CASE / TAIL FORMS ---
# worst single cash-burn day within the year, ranked vs history (tail burn)
def f23ne_f23_negative_earnings_persistence_worstburn_base_v120_signal(ncfo):
    worst = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).max()
    b = _rank(worst, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst net loss relative to cumulative year loss (single-event concentration)
def f23ne_f23_negative_earnings_persistence_lossconc_base_v121_signal(netinc):
    loss = (-netinc).clip(lower=0.0)
    worst = loss.rolling(252, min_periods=126).max()
    total = loss.rolling(252, min_periods=126).sum()
    b = worst / (total + 1e6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEFICIT vs EARNINGS INTERACTIONS ---
# deficit depth gated by current loss persistence (deepening-and-persistent deficit)
def f23ne_f23_negative_earnings_persistence_deficitgated_base_v122_signal(retearn, netinc):
    deficit = np.log1p((-retearn).clip(lower=0.0) / 1e6)
    lf = _f23_losscount(netinc, 252)
    b = deficit * lf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deficit-growth gated by burn persistence (cash-funded deficit growth)
def f23ne_f23_negative_earnings_persistence_deficitburngate_base_v123_signal(retearn, ncfo):
    dg = np.tanh(_f23_deficit_growth(retearn, 126) / 1e6)
    bf = _f23_losscount(ncfo, 126)
    b = dg * bf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MULTI-METRIC LOSS COUNT ---
# average count of negative flows among {netinc,ncfo,ebit,eps} over the year
def f23ne_f23_negative_earnings_persistence_avgnegcount_base_v124_signal(netinc, ncfo, ebit, eps):
    cnt = (_f23_isloss(netinc) + _f23_isloss(ncfo)
           + _f23_isloss(ebit) + _f23_isloss(eps))
    b = cnt.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the year all four flows are simultaneously negative (total distress)
def f23ne_f23_negative_earnings_persistence_quadloss_base_v125_signal(netinc, ncfo, ebit, eps):
    quad = ((netinc < 0) & (ncfo < 0) & (ebit < 0) & (eps < 0)).astype(float)
    b = quad.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TREND OF TIME-SINCE-PROFITABLE ---
# change in time-since-net-profit over a quarter (lengthening vs resetting dry spell)
def f23ne_f23_negative_earnings_persistence_drytrend_base_v126_signal(netinc):
    t = _f23_time_since_profit(netinc)
    b = np.tanh((t - t.shift(63)) / 63.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-DEPTH DISPERSION ACROSS METRICS ---
# spread between net-loss depth and EBIT-loss depth (where the loss originates)
def f23ne_f23_negative_earnings_persistence_depthspread_base_v127_signal(netinc, ebit):
    dn = _f23_lossdepth(netinc, 1e7).rolling(63, min_periods=21).mean()
    de = _f23_lossdepth(ebit, 1e7).rolling(63, min_periods=21).mean()
    b = dn - de
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- NORMALIZED PERSISTENCE (vs own extremes) ---
# net-loss persistence normalized within its own two-year range (regime position)
def f23ne_f23_negative_earnings_persistence_lossfracpos_base_v128_signal(netinc):
    lf = _f23_losscount(netinc, 126)
    hi = _rmax(lf, 504)
    lo = _rmin(lf, 504)
    b = (lf - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn persistence position within its own two-year range
def f23ne_f23_negative_earnings_persistence_burnfracpos_base_v129_signal(ncfo):
    bf = _f23_losscount(ncfo, 126)
    hi = _rmax(bf, 504)
    lo = _rmin(bf, 504)
    b = (bf - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EARNINGS-SIGN ENTROPY / CHURN ---
# net-income crossing-magnitude churn: avg jump size on days the sign flips (instability)
def f23ne_f23_negative_earnings_persistence_signchurn_base_v130_signal(netinc):
    flip = (np.sign(netinc) != np.sign(netinc.shift(1)))
    jump = (netinc - netinc.shift(1)).abs().where(flip, 0.0) / 1e6
    b = jump.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-flow flip-flop intensity: count of sign flips times mean burn depth over two years
def f23ne_f23_negative_earnings_persistence_burnchurn_base_v131_signal(ncfo):
    flip = (np.sign(ncfo) != np.sign(ncfo.shift(1))).astype(float)
    cnt = flip.rolling(504, min_periods=252).mean()
    depth = _f23_lossdepth(ncfo, 1e7).rolling(126, min_periods=63).mean()
    b = cnt * (0.5 + depth)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-LOAD RELATIVE TO DEFICIT ---
# annual net loss as a share of accumulated deficit, ranked (replenishment burden)
def f23ne_f23_negative_earnings_persistence_replenrank_base_v132_signal(netinc, retearn):
    loss = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    ratio = loss / ((-retearn).clip(lower=0.0) + 1e6)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EBIT-TO-EPS LOSS LINKAGE ---
# EPS loss persistence rank relative to its own history (per-share loss-regime extremity)
def f23ne_f23_negative_earnings_persistence_ebitepsgap_base_v133_signal(eps):
    lf = _f23_losscount(eps, 126)
    b = _rank(lf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SMOOTHED SIGNED EPS ---
# EPS direction persistence: average sign of EPS over two years (chronic per-share loss)
def f23ne_f23_negative_earnings_persistence_epsmeansign_base_v134_signal(eps):
    b = np.sign(eps).rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DEFICIT TRAJECTORY Z ---
# half-year deficit-growth z-scored vs two-year history (growth-rate extremity)
def f23ne_f23_negative_earnings_persistence_deficitgr126z_base_v135_signal(retearn):
    dg = _f23_deficit_growth(retearn, 126)
    b = _z(dg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS PERSISTENCE x DEFICIT DRAWDOWN ---
# net-loss persistence times retained-earnings drawdown (persistent-and-eroding)
def f23ne_f23_negative_earnings_persistence_persistxdraw_base_v136_signal(netinc, retearn):
    lf = _f23_losscount(netinc, 252)
    peak = _rmax(retearn, 504)
    dd = (retearn - peak) / (peak.abs() + 1e6)
    b = lf * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- BURN COVERAGE BY EARNINGS ---
# how often net income covers (exceeds) cash burn shortfall (self-funding days)
def f23ne_f23_negative_earnings_persistence_selffund_base_v137_signal(netinc, ncfo):
    cover = ((netinc > 0) & (ncfo < 0)).astype(float)
    b = cover.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS DEPTH EWM ---
# EWM-smoothed net-loss depth (persistent loss-size signal)
def f23ne_f23_negative_earnings_persistence_lossdepthema_base_v138_signal(netinc):
    d = _f23_lossdepth(netinc, 1e7)
    b = d.ewm(span=84, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWM net-loss depth minus slow EWM (loss-depth surge)
def f23ne_f23_negative_earnings_persistence_lossdepthsurge_base_v139_signal(netinc):
    d = _f23_lossdepth(netinc, 1e7)
    b = d.ewm(span=21, min_periods=10).mean() - d.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- CROSS-WINDOW LOSS COUNT DIFFERENCES ---
# net-loss count: month vs quarter (very-acute vs acute, count-friendly)
def f23ne_f23_negative_earnings_persistence_losscntdiff_base_v140_signal(netinc):
    s = _f23_losssum(netinc, 21) / 21.0
    l = _f23_losssum(netinc, 63) / 63.0
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- TIME-IN-DEFICIT FRACTION (retearn) ---
# fraction of two years retained earnings sat below its own two-year median (deficit time)
def f23ne_f23_negative_earnings_persistence_belowmed_base_v141_signal(retearn):
    med = retearn.rolling(504, min_periods=252).median()
    below = (retearn < med).astype(float)
    b = below.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMPOSITE DISTRESS SCORES ---
# weighted distress: loss persistence + burn persistence + dry-spell + deficit growth
def f23ne_f23_negative_earnings_persistence_distresscomp_base_v142_signal(netinc, ncfo, retearn):
    a = _f23_losscount(netinc, 252)
    c = _f23_losscount(ncfo, 252)
    dry = (_f23_time_since_profit(netinc) / 252.0).clip(upper=2.0) / 2.0
    dg = (retearn < retearn.shift(126)).astype(float).rolling(126, min_periods=63).mean()
    b = 0.3 * a + 0.3 * c + 0.2 * dry + 0.2 * dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-distress composite: EBIT loss persistence + EBIT loss depth (operating drag)
def f23ne_f23_negative_earnings_persistence_opdistress_base_v143_signal(ebit):
    lf = _f23_losscount(ebit, 252)
    depth = np.tanh(_f23_lossdepth(ebit, 1e7).rolling(63, min_periods=21).mean())
    b = 0.6 * lf + 0.4 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MOMENTUM OF DISTRESS BREADTH ---
# change in cross-flow loss breadth over a quarter (broadening vs narrowing distress)
def f23ne_f23_negative_earnings_persistence_breadthmom_base_v144_signal(netinc, ncfo, ebit):
    breadth = (_f23_isloss(netinc) + _f23_isloss(ncfo)
               + _f23_isloss(ebit)).rolling(63, min_periods=21).mean()
    b = breadth - breadth.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LOSS-PERSISTENCE YOY ---
# net-loss persistence now vs one year ago (year-over-year regime change)
def f23ne_f23_negative_earnings_persistence_lossfracyoy_base_v145_signal(netinc):
    lf = _f23_losscount(netinc, 252)
    b = lf - lf.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# burn persistence now vs one year ago (cash-burn regime year-over-year change)
def f23ne_f23_negative_earnings_persistence_burnfracyoy_base_v146_signal(ncfo):
    bf = _f23_losscount(ncfo, 252)
    b = bf - bf.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EPS DRY-SPELL DEPTH ---
# EPS dry-spell weighted by per-share loss depth (chronic deep per-share loss)
def f23ne_f23_negative_earnings_persistence_epschronic_base_v147_signal(eps):
    t = _f23_time_since_profit(eps) / 252.0
    d = (-eps).clip(lower=0.0)
    b = t * d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- COMBINED CASH+ACCRUAL DESTROYED ---
# combined cumulative net loss and cash burn over the year (total value destroyed)
def f23ne_f23_negative_earnings_persistence_totaldestroyed_base_v148_signal(netinc, ncfo):
    nl = (-netinc).clip(lower=0.0).rolling(252, min_periods=126).sum()
    cb = (-ncfo).clip(lower=0.0).rolling(252, min_periods=126).sum()
    b = np.log1p((nl + cb) / 1e7)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RETAINED-EARNINGS ACCELERATION (slope of slope at base) ---
# retained-earnings velocity acceleration, z-scored vs history (deficit-growth regime)
def f23ne_f23_negative_earnings_persistence_retaccel_base_v149_signal(retearn):
    vel = _slope(retearn, 63)
    accel = vel - vel.shift(63)
    b = _z(accel, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GRAND DISTRESS COMPOSITE (loss + burn + deficit + dry, ranked) ---
# overall negative-earnings-persistence score, ranked vs its own history
def f23ne_f23_negative_earnings_persistence_grandscore_base_v150_signal(netinc, ncfo, ebit, retearn):
    a = _f23_losscount(netinc, 252)
    c = _f23_losscount(ncfo, 252)
    e = _f23_losscount(ebit, 252)
    dg = (retearn < retearn.shift(126)).astype(float).rolling(126, min_periods=63).mean()
    raw = 0.3 * a + 0.25 * c + 0.25 * e + 0.2 * dg
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23ne_f23_negative_earnings_persistence_lossfracema_base_v076_signal,
    f23ne_f23_negative_earnings_persistence_lossfracdisp_base_v077_signal,
    f23ne_f23_negative_earnings_persistence_burnfracema_base_v078_signal,
    f23ne_f23_negative_earnings_persistence_lossdisp_base_v079_signal,
    f23ne_f23_negative_earnings_persistence_lossrange_base_v080_signal,
    f23ne_f23_negative_earnings_persistence_accrcashgap_base_v081_signal,
    f23ne_f23_negative_earnings_persistence_belowline_base_v082_signal,
    f23ne_f23_negative_earnings_persistence_deficitgr_126d_base_v083_signal,
    f23ne_f23_negative_earnings_persistence_deficitgrchg_base_v084_signal,
    f23ne_f23_negative_earnings_persistence_deficitbuild_base_v085_signal,
    f23ne_f23_negative_earnings_persistence_lossdepthrel_base_v086_signal,
    f23ne_f23_negative_earnings_persistence_lossdepthz_base_v087_signal,
    f23ne_f23_negative_earnings_persistence_ebitdepthrel_base_v088_signal,
    f23ne_f23_negative_earnings_persistence_tsnirank_base_v089_signal,
    f23ne_f23_negative_earnings_persistence_tsratio_base_v090_signal,
    f23ne_f23_negative_earnings_persistence_maxdry_base_v091_signal,
    f23ne_f23_negative_earnings_persistence_proffrac_base_v092_signal,
    f23ne_f23_negative_earnings_persistence_maxprofstreak_base_v093_signal,
    f23ne_f23_negative_earnings_persistence_streakbal_base_v094_signal,
    f23ne_f23_negative_earnings_persistence_cumebitloss_base_v095_signal,
    f23ne_f23_negative_earnings_persistence_netdestroyed_base_v096_signal,
    f23ne_f23_negative_earnings_persistence_depthvel_63d_base_v097_signal,
    f23ne_f23_negative_earnings_persistence_ebitdepthvel_base_v098_signal,
    f23ne_f23_negative_earnings_persistence_burndepthvel_base_v099_signal,
    f23ne_f23_negative_earnings_persistence_epsrank_base_v100_signal,
    f23ne_f23_negative_earnings_persistence_epslossema_base_v101_signal,
    f23ne_f23_negative_earnings_persistence_epscumloss_base_v102_signal,
    f23ne_f23_negative_earnings_persistence_epssignmagz_base_v103_signal,
    f23ne_f23_negative_earnings_persistence_retrecov_base_v104_signal,
    f23ne_f23_negative_earnings_persistence_rethealrate_base_v105_signal,
    f23ne_f23_negative_earnings_persistence_deficitvsrunrank_base_v106_signal,
    f23ne_f23_negative_earnings_persistence_deeplossreg_base_v107_signal,
    f23ne_f23_negative_earnings_persistence_compdistress_base_v108_signal,
    f23ne_f23_negative_earnings_persistence_anyloss_base_v109_signal,
    f23ne_f23_negative_earnings_persistence_burnratio_base_v110_signal,
    f23ne_f23_negative_earnings_persistence_ebitratio_base_v111_signal,
    f23ne_f23_negative_earnings_persistence_signagree_base_v112_signal,
    f23ne_f23_negative_earnings_persistence_signagree2_base_v113_signal,
    f23ne_f23_negative_earnings_persistence_nisignmagsm_base_v114_signal,
    f23ne_f23_negative_earnings_persistence_ebitsignmagdisp_base_v115_signal,
    f23ne_f23_negative_earnings_persistence_meansign_base_v116_signal,
    f23ne_f23_negative_earnings_persistence_lossfracvol_base_v117_signal,
    f23ne_f23_negative_earnings_persistence_ebitvol_base_v118_signal,
    f23ne_f23_negative_earnings_persistence_nisemidev_base_v119_signal,
    f23ne_f23_negative_earnings_persistence_worstburn_base_v120_signal,
    f23ne_f23_negative_earnings_persistence_lossconc_base_v121_signal,
    f23ne_f23_negative_earnings_persistence_deficitgated_base_v122_signal,
    f23ne_f23_negative_earnings_persistence_deficitburngate_base_v123_signal,
    f23ne_f23_negative_earnings_persistence_avgnegcount_base_v124_signal,
    f23ne_f23_negative_earnings_persistence_quadloss_base_v125_signal,
    f23ne_f23_negative_earnings_persistence_drytrend_base_v126_signal,
    f23ne_f23_negative_earnings_persistence_depthspread_base_v127_signal,
    f23ne_f23_negative_earnings_persistence_lossfracpos_base_v128_signal,
    f23ne_f23_negative_earnings_persistence_burnfracpos_base_v129_signal,
    f23ne_f23_negative_earnings_persistence_signchurn_base_v130_signal,
    f23ne_f23_negative_earnings_persistence_burnchurn_base_v131_signal,
    f23ne_f23_negative_earnings_persistence_replenrank_base_v132_signal,
    f23ne_f23_negative_earnings_persistence_ebitepsgap_base_v133_signal,
    f23ne_f23_negative_earnings_persistence_epsmeansign_base_v134_signal,
    f23ne_f23_negative_earnings_persistence_deficitgr126z_base_v135_signal,
    f23ne_f23_negative_earnings_persistence_persistxdraw_base_v136_signal,
    f23ne_f23_negative_earnings_persistence_selffund_base_v137_signal,
    f23ne_f23_negative_earnings_persistence_lossdepthema_base_v138_signal,
    f23ne_f23_negative_earnings_persistence_lossdepthsurge_base_v139_signal,
    f23ne_f23_negative_earnings_persistence_losscntdiff_base_v140_signal,
    f23ne_f23_negative_earnings_persistence_belowmed_base_v141_signal,
    f23ne_f23_negative_earnings_persistence_distresscomp_base_v142_signal,
    f23ne_f23_negative_earnings_persistence_opdistress_base_v143_signal,
    f23ne_f23_negative_earnings_persistence_breadthmom_base_v144_signal,
    f23ne_f23_negative_earnings_persistence_lossfracyoy_base_v145_signal,
    f23ne_f23_negative_earnings_persistence_burnfracyoy_base_v146_signal,
    f23ne_f23_negative_earnings_persistence_epschronic_base_v147_signal,
    f23ne_f23_negative_earnings_persistence_totaldestroyed_base_v148_signal,
    f23ne_f23_negative_earnings_persistence_retaccel_base_v149_signal,
    f23ne_f23_negative_earnings_persistence_grandscore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_NEGATIVE_EARNINGS_PERSISTENCE_REGISTRY_076_150 = REGISTRY


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

    def _swing(seed, seed2, base, vol, amp, period):
        raw = _fund(seed, base=base, vol=vol, allow_neg=True)
        center = raw - raw.rolling(252, min_periods=1).mean()
        t = np.arange(n)
        wob = amp * base * np.sin(2.0 * np.pi * t / period)
        nz = _fund(seed2, base=base, vol=vol, allow_neg=True)
        nz = (nz - nz.rolling(252, min_periods=1).mean()) * 0.5
        return center + wob + nz

    netinc = _swing(2301, 2311, 4.0e7, 0.30, 0.50, 80).rename("netinc")
    ncfo = _swing(2302, 2312, 3.5e7, 0.28, 0.50, 95).rename("ncfo")
    eps = _swing(2303, 2313, 2.0, 0.32, 0.50, 70).rename("eps")
    ebit = _swing(2304, 2314, 4.5e7, 0.27, 0.50, 110).rename("ebit")
    retearn = _swing(2305, 2315, 8.0e7, 0.18, 0.35, 160).rename("retearn")

    cols = {"netinc": netinc, "ncfo": ncfo, "eps": eps,
            "ebit": ebit, "retearn": retearn}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("netinc", "ncfo", "eps", "ebit", "retearn")
                   for c in meta["inputs"]), name
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

    print("OK f23_negative_earnings_persistence_base_076_150_claude: %d features pass" % n_features)
