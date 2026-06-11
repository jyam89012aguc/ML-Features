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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (debt-cycle trajectory) =====
def _f31_net_debt(debt, cashneq):
    return debt - cashneq


def _f31_short_share(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    return debtc / tot


def _f31_lev_trend(debt, w):
    return np.log(debt.replace(0, np.nan)) - np.log(debt.shift(w).replace(0, np.nan))


def _f31_cycle_pos(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


# ============================================================
# debt level smoothed by EMA vs slower EMA (debt-trend displacement)
def f31dt_f31_debt_cycle_trajectory_debtemadisp_base_v076_signal(debt):
    fast = debt.ewm(span=42, min_periods=21).mean()
    slow = debt.ewm(span=189, min_periods=63).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt EMA displacement (medium vs long deleveraging trend)
def f31dt_f31_debt_cycle_trajectory_netdebtemadisp_base_v077_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    fast = nd.ewm(span=42, min_periods=21).mean()
    slow = nd.ewm(span=189, min_periods=63).mean()
    b = (fast - slow) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-cash ratio level (gross leverage vs liquidity)
def f31dt_f31_debt_cycle_trajectory_debtcash_base_v078_signal(debt, cashneq):
    b = debt / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log debt-to-cash, z-scored (leverage-stress regime de-trended)
def f31dt_f31_debt_cycle_trajectory_logdebtcashz_252d_base_v079_signal(debt, cashneq):
    lr = np.log(debt.replace(0, np.nan)) - np.log(cashneq.replace(0, np.nan))
    b = _z(lr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt to cash, percentile-ranked (rollover-liquidity cycle phase)
def f31dt_f31_debt_cycle_trajectory_shortcashrank_504d_base_v080_signal(debtc, cashneq):
    ratio = debtc / cashneq.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow EMA displacement (issuance momentum vs baseline)
def f31dt_f31_debt_cycle_trajectory_flowemadisp_base_v081_signal(ncfdebt, debt):
    fast = ncfdebt.ewm(span=21, min_periods=10).mean()
    slow = ncfdebt.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net financing over 504d vs gross debt (multi-year funding reliance)
def f31dt_f31_debt_cycle_trajectory_cumflow_504d_base_v082_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(504, min_periods=252).sum()
    b = cum / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt slope vs cash slope divergence (debt growing while cash shrinks)
def f31dt_f31_debt_cycle_trajectory_debtcashdiv_126d_base_v083_signal(debt, cashneq):
    ds = _f31_lev_trend(debt, 126)
    cs = np.log(cashneq.replace(0, np.nan)) - np.log(cashneq.shift(126).replace(0, np.nan))
    b = ds - cs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt second difference proxy over quarters (re-leveraging curvature)
def f31dt_f31_debt_cycle_trajectory_netdebtcurv_base_v084_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    d1 = nd - nd.shift(63)
    b = (d1 - d1.shift(63)) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-debt cycle position within 504d range (rollover-wall phase)
def f31dt_f31_debt_cycle_trajectory_shortcyc_504d_base_v085_signal(debtc):
    b = _f31_cycle_pos(debtc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-debt cycle position within 1260d range (term-funding phase)
def f31dt_f31_debt_cycle_trajectory_longcyc_1260d_base_v086_signal(debtnc):
    b = _f31_cycle_pos(debtnc, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd-to-cash ratio z (USD leverage-stress regime)
def f31dt_f31_debt_cycle_trajectory_usdcashz_252d_base_v087_signal(debtusd, cashneq):
    ratio = debtusd / cashneq.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-build inflection: 63d slope crossing zero from negative (paydown→buildup)
def f31dt_f31_debt_cycle_trajectory_buildinflect_base_v088_signal(debt):
    sl = _f31_lev_trend(debt, 63)
    b = np.tanh(8.0 * sl) - np.tanh(8.0 * sl.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow consistency: rolling correlation of flow with its own lag (persistence)
def f31dt_f31_debt_cycle_trajectory_flowautocorr_base_v089_signal(ncfdebt):
    f = ncfdebt
    fl = f.shift(21)
    b = f.rolling(252, min_periods=126).corr(fl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt over total term-debt, smoothed (cash-cushion vs structural debt)
def f31dt_f31_debt_cycle_trajectory_ndtermdebt_base_v090_signal(debt, cashneq, debtc, debtnc):
    nd = _f31_net_debt(debt, cashneq)
    tot = (debtc + debtnc).replace(0, np.nan)
    raw = nd / tot
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt amplitude over 504d normalized by mean (medium-cycle debt swing)
def f31dt_f31_debt_cycle_trajectory_debtamp_504d_base_v091_signal(debt):
    hi = _rmax(debt, 504)
    lo = _rmin(debt, 504)
    mn = _mean(debt, 504)
    b = (hi - lo) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash volatility relative to debt (liquidity instability funding leverage)
def f31dt_f31_debt_cycle_trajectory_cashvoldebt_base_v092_signal(cashneq, debt):
    cv = cashneq.pct_change().rolling(126, min_periods=63).std()
    b = cv * (debt / cashneq.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-debt growth vs long-debt growth ratio (mix-shift intensity)
def f31dt_f31_debt_cycle_trajectory_growthratio_252d_base_v093_signal(debtc, debtnc):
    sg = debtc / debtc.shift(252).replace(0, np.nan)
    lg = debtnc / debtnc.shift(252).replace(0, np.nan)
    b = sg / lg.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow scaled by short-term debt (rollover-funding intensity)
def f31dt_f31_debt_cycle_trajectory_flowvsshort_base_v094_signal(ncfdebt, debtc):
    b = ncfdebt.rolling(63, min_periods=21).sum() / debtc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash as a fraction of USD debt, percentile-ranked (USD-liquidity cushion phase)
def f31dt_f31_debt_cycle_trajectory_ndvsusd_base_v095_signal(cashneq, debtusd):
    ratio = cashneq / debtusd.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-peak proximity weighted by short-share (risky leverage at cycle top)
def f31dt_f31_debt_cycle_trajectory_peakshort_base_v096_signal(debt, debtc, debtnc):
    hi = _rmax(debt, 1260)
    peak = debt / hi.replace(0, np.nan)
    sh = _f31_short_share(debtc, debtnc)
    b = peak * sh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of quarters short-share rose over the last year (rollover-risk build)
def f31dt_f31_debt_cycle_trajectory_shortrisecnt_252d_base_v097_signal(debtc, debtnc):
    sh = _f31_short_share(debtc, debtnc)
    up = (sh.diff(63) > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt slope dispersion across short/long/gross (term-structure trajectory spread)
def f31dt_f31_debt_cycle_trajectory_termslopedisp_base_v098_signal(debt, debtc, debtnc):
    s1 = _f31_lev_trend(debt, 126)
    s2 = _f31_lev_trend(debtc, 126)
    s3 = _f31_lev_trend(debtnc, 126)
    b = pd.concat([s1, s2, s3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt z over a long 504d window (deep-cycle leverage extremity)
def f31dt_f31_debt_cycle_trajectory_netdebtz_504d_base_v099_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = _z(nd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow cumulative sign-persistence weighted by magnitude (funding regime)
def f31dt_f31_debt_cycle_trajectory_flowregime_base_v100_signal(ncfdebt, debt):
    sm = _mean(ncfdebt, 63)
    persist = (np.sign(sm) == np.sign(sm.shift(63))).astype(float)
    pweight = persist.rolling(252, min_periods=126).mean()
    b = pweight * (sm / debt.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-cash momentum over a year (leverage-stress trajectory)
def f31dt_f31_debt_cycle_trajectory_debtcashmom_252d_base_v101_signal(debt, cashneq):
    ratio = debt / cashneq.replace(0, np.nan)
    b = ratio / ratio.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-debt-to-gross-debt level (immediate-maturity concentration)
def f31dt_f31_debt_cycle_trajectory_shortgross_base_v102_signal(debtc, debt):
    b = debtc / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-debt-to-gross-debt momentum (terming-out trajectory)
def f31dt_f31_debt_cycle_trajectory_longgrossmom_252d_base_v103_signal(debtnc, debt):
    ratio = debtnc / debt.replace(0, np.nan)
    b = ratio - ratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt build relative to debt volatility (clean re-leveraging signal)
def f31dt_f31_debt_cycle_trajectory_netbuildvol_base_v104_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    chg = nd - nd.shift(126)
    vol = nd.diff().rolling(252, min_periods=126).std()
    b = chg / (vol.replace(0, np.nan) * np.sqrt(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd cycle position within 504d range (USD leverage phase)
def f31dt_f31_debt_cycle_trajectory_usdcyc_504d_base_v105_signal(debtusd):
    b = _f31_cycle_pos(debtusd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow turning point: change in 63d flow-mean sign-weighted (inflection)
def f31dt_f31_debt_cycle_trajectory_flowturn_base_v106_signal(ncfdebt, debt):
    fl = _mean(ncfdebt, 63) / debt.replace(0, np.nan)
    b = fl - fl.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-cash ratio percentile-rank (deleverage stress phase)
def f31dt_f31_debt_cycle_trajectory_ndcashrank_504d_base_v107_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    ratio = nd / cashneq.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how much gross debt sits above its 252d mean, in std units, smoothed
def f31dt_f31_debt_cycle_trajectory_debtzsm_252d_base_v108_signal(debt):
    z = _z(debt, 252)
    b = z.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown persistence: fraction of last year debt fell qtr-over-qtr
def f31dt_f31_debt_cycle_trajectory_paydownpersist_252d_base_v109_signal(debt):
    down = (debt.diff(63) < 0).astype(float)
    b = down.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-short-debt coverage (immediate maturity runway)
def f31dt_f31_debt_cycle_trajectory_cashshortcov_base_v110_signal(cashneq, debtc):
    b = cashneq / debtc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-short coverage momentum (worsening near-term liquidity)
def f31dt_f31_debt_cycle_trajectory_cashshortmom_126d_base_v111_signal(cashneq, debtc):
    cov = cashneq / debtc.replace(0, np.nan)
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow over total term-debt cumulative (term-funding reliance)
def f31dt_f31_debt_cycle_trajectory_flowtermdebt_252d_base_v112_signal(ncfdebt, debtc, debtnc):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    tot = (debtc + debtnc).replace(0, np.nan)
    b = cum / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt convexity of the multi-year cycle position (top/bottom curvature)
def f31dt_f31_debt_cycle_trajectory_debtcyconvex_1260d_base_v113_signal(debt):
    cp = _f31_cycle_pos(debt, 1260)
    b = np.sign(cp - 0.5) * (cp - 0.5) ** 2 * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd-vs-debt wedge momentum (FX-driven leverage drift)
def f31dt_f31_debt_cycle_trajectory_usdwedgemom_126d_base_v114_signal(debt, debtusd):
    wedge = debtusd / debt.replace(0, np.nan) - 1.0
    b = wedge - wedge.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt to gross-debt spread between short and long horizons (cushion-trend gap)
def f31dt_f31_debt_cycle_trajectory_cushiongap_base_v115_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    r = nd / debt.replace(0, np.nan)
    b = r.rolling(63, min_periods=21).mean() - r.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt build velocity over a month / gross debt
def f31dt_f31_debt_cycle_trajectory_shortvel_21d_base_v116_signal(debtc, debt):
    b = (debtc - debtc.shift(21)) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt amplitude per unit slope (cyclicality vs trend; choppy vs trending leverage)
def f31dt_f31_debt_cycle_trajectory_ampvsslope_base_v117_signal(debt):
    hi = _rmax(debt, 504)
    lo = _rmin(debt, 504)
    amp = (hi - lo) / _mean(debt, 504).replace(0, np.nan)
    slope = _f31_lev_trend(debt, 252).abs()
    b = amp / (slope + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow z minus debt-slope z (flow-vs-stock leverage signal disagreement)
def f31dt_f31_debt_cycle_trajectory_flowstockdiv_base_v118_signal(ncfdebt, debt):
    fz = _z(ncfdebt.rolling(63, min_periods=21).sum(), 252)
    sz = _z(_f31_lev_trend(debt, 63), 252)
    b = fz - sz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash cushion erosion streak: consecutive declines in cash/debt coverage
def f31dt_f31_debt_cycle_trajectory_coverstreak_base_v119_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    dec = (cov.diff(21) < 0).astype(float)
    same = (dec == dec.shift(21)).astype(float)
    streak = same.groupby((same == 0).cumsum()).cumsum()
    b = streak * (2 * dec - 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt to cash, log-scaled and ranked over multi-year (deep deleverage phase)
def f31dt_f31_debt_cycle_trajectory_logndcashrank_1260d_base_v120_signal(debt, cashneq):
    nd = (debt - cashneq)
    lr = np.sign(nd) * np.log1p(nd.abs())
    b = _rank(lr, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt slope skew: asymmetry between build periods and paydown periods
def f31dt_f31_debt_cycle_trajectory_slopeskew_252d_base_v121_signal(debt):
    sl = np.log(debt.replace(0, np.nan)).diff()
    b = sl.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-share dispersion across 63/252/504 lookbacks (mix-stability)
def f31dt_f31_debt_cycle_trajectory_shortsharedisp_base_v122_signal(debtc, debtnc):
    sh = _f31_short_share(debtc, debtnc)
    s1 = sh.rolling(63, min_periods=21).mean()
    s2 = sh.rolling(252, min_periods=126).mean()
    s3 = sh.rolling(504, min_periods=252).mean()
    b = pd.concat([s1, s2, s3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow minimum over a year / debt (deepest paydown event)
def f31dt_f31_debt_cycle_trajectory_maxpaydown_252d_base_v123_signal(ncfdebt, debt):
    b = ncfdebt.rolling(252, min_periods=126).min() / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow maximum over a year / debt (largest issuance event)
def f31dt_f31_debt_cycle_trajectory_maxissue_252d_base_v124_signal(ncfdebt, debt):
    b = ncfdebt.rolling(252, min_periods=126).max() / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt trajectory direction over 126d, tanh-bounded (re-leverage/deleverage)
def f31dt_f31_debt_cycle_trajectory_netdirtanh_126d_base_v125_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    chg = (nd - nd.shift(126)) / debt.replace(0, np.nan)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-cash 1260d cycle position (multi-year leverage-stress phase)
def f31dt_f31_debt_cycle_trajectory_dcashcyc_1260d_base_v126_signal(debt, cashneq):
    ratio = debt / cashneq.replace(0, np.nan)
    b = _f31_cycle_pos(ratio, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt z over 504d (structural-funding extremity)
def f31dt_f31_debt_cycle_trajectory_longz_504d_base_v127_signal(debtnc):
    b = _z(debtnc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt 63d log-slope z-scored (rollover-wall build acceleration)
def f31dt_f31_debt_cycle_trajectory_shortz_504d_base_v128_signal(debtc):
    sl = _f31_lev_trend(debtc, 63)
    b = _z(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow cumulative over 126d relative to its own 504d std (funding shock)
def f31dt_f31_debt_cycle_trajectory_flowshock_base_v129_signal(ncfdebt):
    cum = ncfdebt.rolling(126, min_periods=63).sum()
    sd = cum.rolling(504, min_periods=252).std()
    b = cum / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build-up acceleration: 126d slope minus 252d slope of debtusd
def f31dt_f31_debt_cycle_trajectory_usdslopeaccel_base_v130_signal(debtusd):
    s_fast = _f31_lev_trend(debtusd, 126)
    s_slow = _f31_lev_trend(debtusd, 252)
    b = s_fast - s_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt above its 252d trough scaled by gross debt (re-leverage extent vs base)
def f31dt_f31_debt_cycle_trajectory_netoffrough_252d_base_v131_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    lo = _rmin(nd, 252)
    b = (nd - lo) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt rising while cash falling regime flag, magnitude-weighted (twin stress)
def f31dt_f31_debt_cycle_trajectory_twinstress_base_v132_signal(debt, cashneq):
    dchg = debt.diff(63) / debt.replace(0, np.nan)
    cchg = cashneq.diff(63) / cashneq.replace(0, np.nan)
    flag = ((dchg > 0) & (cchg < 0)).astype(float)
    b = flag * (dchg - cchg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-funding coherence: fraction of last year flow direction matched long-debt change
def f31dt_f31_debt_cycle_trajectory_rolloverrate_base_v133_signal(ncfdebt, debtnc):
    fl = _mean(ncfdebt, 21)
    lchg = debtnc.diff(21)
    match = (np.sign(fl) == np.sign(lchg)).astype(float)
    b = match.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross debt vs its 1260d median (long-cycle level position, robust)
def f31dt_f31_debt_cycle_trajectory_debtmedpos_1260d_base_v134_signal(debt):
    med = debt.rolling(1260, min_periods=504).median()
    b = debt / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt slope minus its own 252d-lagged slope (deleveraging acceleration yoy)
def f31dt_f31_debt_cycle_trajectory_netslopeyoy_base_v135_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    sl = (nd - nd.shift(63)) / debt.replace(0, np.nan)
    b = sl - sl.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-share level interacted with debt-to-cash (risky-mix leverage stress)
def f31dt_f31_debt_cycle_trajectory_riskmixlev_base_v136_signal(debtc, debtnc, debt, cashneq):
    sh = _f31_short_share(debtc, debtnc)
    lev = debt / cashneq.replace(0, np.nan)
    b = sh * np.tanh(lev / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow volatility over a year / debt (funding instability)
def f31dt_f31_debt_cycle_trajectory_flowvol_252d_base_v137_signal(ncfdebt, debt):
    b = _std(ncfdebt, 252) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt trajectory smoothness: 1 - |slope dispersion| (steady vs erratic deleveraging)
def f31dt_f31_debt_cycle_trajectory_smoothness_base_v138_signal(debt):
    sl = np.log(debt.replace(0, np.nan)).diff()
    sd = sl.rolling(252, min_periods=126).std()
    mn = sl.rolling(252, min_periods=126).mean().abs()
    b = mn / (sd.replace(0, np.nan) + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt cycle position 252d (recent leverage phase)
def f31dt_f31_debt_cycle_trajectory_netcyc_252d_base_v139_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = _f31_cycle_pos(nd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd net-of-cash to debtusd (USD cash cushion ratio)
def f31dt_f31_debt_cycle_trajectory_usdcushion_base_v140_signal(debtusd, cashneq):
    nd = debtusd - cashneq
    b = nd / debtusd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow direction vs short-share direction agreement (funding-mix coherence)
def f31dt_f31_debt_cycle_trajectory_flowmixcoher_base_v141_signal(ncfdebt, debtc, debtnc):
    fl = _mean(ncfdebt, 63)
    sh = _f31_short_share(debtc, debtnc)
    shchg = sh.diff(63)
    b = np.sign(fl) * np.sign(shchg) * sh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross debt 63d momentum minus 252d momentum (short-vs-long build divergence)
def f31dt_f31_debt_cycle_trajectory_buildiverge_base_v142_signal(debt):
    m1 = debt / debt.shift(63).replace(0, np.nan) - 1.0
    m2 = debt / debt.shift(252).replace(0, np.nan) - 1.0
    b = m1 - m2 / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage recovery off its 504d minimum (liquidity rebuilt from worst point)
def f31dt_f31_debt_cycle_trajectory_covercyc_504d_base_v143_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    lo = _rmin(cov, 504)
    b = cov / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow per unit net-debt-change (financing efficiency reconciliation)
def f31dt_f31_debt_cycle_trajectory_floweffic_base_v144_signal(ncfdebt, debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    ndchg = nd.diff(126)
    fl = ncfdebt.rolling(126, min_periods=63).sum()
    resid = fl - ndchg
    sd = resid.rolling(252, min_periods=126).std()
    b = resid / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# concentrated rollover risk: rising short-share interacted with thin cash, momentum
def f31dt_f31_debt_cycle_trajectory_concentrisk_base_v145_signal(debtc, debtnc, cashneq):
    sh = _f31_short_share(debtc, debtnc)
    shmom = sh.diff(63)
    thin = 1.0 / (1.0 + cashneq / (debtc + debtnc).replace(0, np.nan))
    b = shmom * thin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt z minus cash z (leverage-vs-liquidity standardized gap)
def f31dt_f31_debt_cycle_trajectory_debtcashzgap_252d_base_v146_signal(debt, cashneq):
    b = _z(debt, 252) - _z(cashneq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-debt slope per unit long-debt volatility (clean term-funding trend)
def f31dt_f31_debt_cycle_trajectory_longtrendvol_base_v147_signal(debtnc):
    slope = _f31_lev_trend(debtnc, 126)
    vol = np.log(debtnc.replace(0, np.nan)).diff().rolling(252, min_periods=126).std()
    b = slope / (vol.replace(0, np.nan) * np.sqrt(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt percentile-rank momentum (cycle-phase advance speed)
def f31dt_f31_debt_cycle_trajectory_netrankmom_base_v148_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    rk = _rank(nd, 504)
    b = rk - rk.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow share of cumulative gross-debt build over 252d (flow-funded growth)
def f31dt_f31_debt_cycle_trajectory_flowfunded_base_v149_signal(ncfdebt, debt):
    fl = ncfdebt.rolling(252, min_periods=126).sum()
    build = (debt - debt.shift(252)).abs()
    b = fl / (build + debt.abs() * 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined cycle-trajectory distress: debt-z x short-share x inverse cash-coverage
def f31dt_f31_debt_cycle_trajectory_trajdistress_base_v150_signal(debt, debtc, debtnc, cashneq):
    dz = _z(debt, 252)
    sh = _f31_short_share(debtc, debtnc)
    invcov = 1.0 / (1.0 + cashneq / debt.replace(0, np.nan))
    b = np.tanh(dz) * sh * invcov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31dt_f31_debt_cycle_trajectory_debtemadisp_base_v076_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtemadisp_base_v077_signal,
    f31dt_f31_debt_cycle_trajectory_debtcash_base_v078_signal,
    f31dt_f31_debt_cycle_trajectory_logdebtcashz_252d_base_v079_signal,
    f31dt_f31_debt_cycle_trajectory_shortcashrank_504d_base_v080_signal,
    f31dt_f31_debt_cycle_trajectory_flowemadisp_base_v081_signal,
    f31dt_f31_debt_cycle_trajectory_cumflow_504d_base_v082_signal,
    f31dt_f31_debt_cycle_trajectory_debtcashdiv_126d_base_v083_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtcurv_base_v084_signal,
    f31dt_f31_debt_cycle_trajectory_shortcyc_504d_base_v085_signal,
    f31dt_f31_debt_cycle_trajectory_longcyc_1260d_base_v086_signal,
    f31dt_f31_debt_cycle_trajectory_usdcashz_252d_base_v087_signal,
    f31dt_f31_debt_cycle_trajectory_buildinflect_base_v088_signal,
    f31dt_f31_debt_cycle_trajectory_flowautocorr_base_v089_signal,
    f31dt_f31_debt_cycle_trajectory_ndtermdebt_base_v090_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_504d_base_v091_signal,
    f31dt_f31_debt_cycle_trajectory_cashvoldebt_base_v092_signal,
    f31dt_f31_debt_cycle_trajectory_growthratio_252d_base_v093_signal,
    f31dt_f31_debt_cycle_trajectory_flowvsshort_base_v094_signal,
    f31dt_f31_debt_cycle_trajectory_ndvsusd_base_v095_signal,
    f31dt_f31_debt_cycle_trajectory_peakshort_base_v096_signal,
    f31dt_f31_debt_cycle_trajectory_shortrisecnt_252d_base_v097_signal,
    f31dt_f31_debt_cycle_trajectory_termslopedisp_base_v098_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtz_504d_base_v099_signal,
    f31dt_f31_debt_cycle_trajectory_flowregime_base_v100_signal,
    f31dt_f31_debt_cycle_trajectory_debtcashmom_252d_base_v101_signal,
    f31dt_f31_debt_cycle_trajectory_shortgross_base_v102_signal,
    f31dt_f31_debt_cycle_trajectory_longgrossmom_252d_base_v103_signal,
    f31dt_f31_debt_cycle_trajectory_netbuildvol_base_v104_signal,
    f31dt_f31_debt_cycle_trajectory_usdcyc_504d_base_v105_signal,
    f31dt_f31_debt_cycle_trajectory_flowturn_base_v106_signal,
    f31dt_f31_debt_cycle_trajectory_ndcashrank_504d_base_v107_signal,
    f31dt_f31_debt_cycle_trajectory_debtzsm_252d_base_v108_signal,
    f31dt_f31_debt_cycle_trajectory_paydownpersist_252d_base_v109_signal,
    f31dt_f31_debt_cycle_trajectory_cashshortcov_base_v110_signal,
    f31dt_f31_debt_cycle_trajectory_cashshortmom_126d_base_v111_signal,
    f31dt_f31_debt_cycle_trajectory_flowtermdebt_252d_base_v112_signal,
    f31dt_f31_debt_cycle_trajectory_debtcyconvex_1260d_base_v113_signal,
    f31dt_f31_debt_cycle_trajectory_usdwedgemom_126d_base_v114_signal,
    f31dt_f31_debt_cycle_trajectory_cushiongap_base_v115_signal,
    f31dt_f31_debt_cycle_trajectory_shortvel_21d_base_v116_signal,
    f31dt_f31_debt_cycle_trajectory_ampvsslope_base_v117_signal,
    f31dt_f31_debt_cycle_trajectory_flowstockdiv_base_v118_signal,
    f31dt_f31_debt_cycle_trajectory_coverstreak_base_v119_signal,
    f31dt_f31_debt_cycle_trajectory_logndcashrank_1260d_base_v120_signal,
    f31dt_f31_debt_cycle_trajectory_slopeskew_252d_base_v121_signal,
    f31dt_f31_debt_cycle_trajectory_shortsharedisp_base_v122_signal,
    f31dt_f31_debt_cycle_trajectory_maxpaydown_252d_base_v123_signal,
    f31dt_f31_debt_cycle_trajectory_maxissue_252d_base_v124_signal,
    f31dt_f31_debt_cycle_trajectory_netdirtanh_126d_base_v125_signal,
    f31dt_f31_debt_cycle_trajectory_dcashcyc_1260d_base_v126_signal,
    f31dt_f31_debt_cycle_trajectory_longz_504d_base_v127_signal,
    f31dt_f31_debt_cycle_trajectory_shortz_504d_base_v128_signal,
    f31dt_f31_debt_cycle_trajectory_flowshock_base_v129_signal,
    f31dt_f31_debt_cycle_trajectory_usdslopeaccel_base_v130_signal,
    f31dt_f31_debt_cycle_trajectory_netoffrough_252d_base_v131_signal,
    f31dt_f31_debt_cycle_trajectory_twinstress_base_v132_signal,
    f31dt_f31_debt_cycle_trajectory_rolloverrate_base_v133_signal,
    f31dt_f31_debt_cycle_trajectory_debtmedpos_1260d_base_v134_signal,
    f31dt_f31_debt_cycle_trajectory_netslopeyoy_base_v135_signal,
    f31dt_f31_debt_cycle_trajectory_riskmixlev_base_v136_signal,
    f31dt_f31_debt_cycle_trajectory_flowvol_252d_base_v137_signal,
    f31dt_f31_debt_cycle_trajectory_smoothness_base_v138_signal,
    f31dt_f31_debt_cycle_trajectory_netcyc_252d_base_v139_signal,
    f31dt_f31_debt_cycle_trajectory_usdcushion_base_v140_signal,
    f31dt_f31_debt_cycle_trajectory_flowmixcoher_base_v141_signal,
    f31dt_f31_debt_cycle_trajectory_buildiverge_base_v142_signal,
    f31dt_f31_debt_cycle_trajectory_covercyc_504d_base_v143_signal,
    f31dt_f31_debt_cycle_trajectory_floweffic_base_v144_signal,
    f31dt_f31_debt_cycle_trajectory_concentrisk_base_v145_signal,
    f31dt_f31_debt_cycle_trajectory_debtcashzgap_252d_base_v146_signal,
    f31dt_f31_debt_cycle_trajectory_longtrendvol_base_v147_signal,
    f31dt_f31_debt_cycle_trajectory_netrankmom_base_v148_signal,
    f31dt_f31_debt_cycle_trajectory_flowfunded_base_v149_signal,
    f31dt_f31_debt_cycle_trajectory_trajdistress_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_DEBT_CYCLE_TRAJECTORY_REGISTRY_076_150 = REGISTRY


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

    debt = _fund(201, base=5e8, drift=0.01, vol=0.10).rename("debt")
    debtusd = (_fund(202, base=5e8, drift=0.01, vol=0.10) * 1.02).rename("debtusd")
    debtc = _fund(203, base=1.5e8, drift=0.005, vol=0.12).rename("debtc")
    debtnc = _fund(204, base=3.5e8, drift=0.008, vol=0.09).rename("debtnc")
    cashneq = _fund(205, base=2e8, drift=0.0, vol=0.15).rename("cashneq")
    ncfdebt = _fund(206, base=8e7, drift=0.0, vol=0.30, allow_neg=True).rename("ncfdebt")

    cols = {"debt": debt, "debtusd": debtusd, "debtc": debtc, "debtnc": debtnc,
            "cashneq": cashneq, "ncfdebt": ncfdebt}

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

    print("OK f31_debt_cycle_trajectory_base_076_150_claude: %d features pass" % n_features)
