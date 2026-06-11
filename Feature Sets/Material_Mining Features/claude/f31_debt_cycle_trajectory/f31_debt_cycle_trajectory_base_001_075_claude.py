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
    # net debt = gross debt minus cash
    return debt - cashneq


def _f31_log_chg(s, w):
    return np.log(s.replace(0, np.nan).abs()) - np.log(s.shift(w).replace(0, np.nan).abs())


def _f31_short_share(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    return debtc / tot


def _f31_lev_trend(debt, w):
    # rolling log-slope of debt level (deleveraging slope proxy)
    return np.log(debt.replace(0, np.nan)) - np.log(debt.shift(w).replace(0, np.nan))


def _f31_cycle_pos(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f31_peak_dist(s, w):
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    return s / hi.replace(0, np.nan)


# ============================================================
# gross debt level vs its own 252d mean (where in the debt cycle)
def f31dt_f31_debt_cycle_trajectory_debtlvl_252d_base_v001_signal(debt):
    b = _z(debt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build/paydown: 252d log-change of gross debt (deleveraging slope)
def f31dt_f31_debt_cycle_trajectory_debtslope_252d_base_v002_signal(debt):
    b = _f31_lev_trend(debt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build/paydown: 126d log-change of gross debt
def f31dt_f31_debt_cycle_trajectory_debtslope_126d_base_v003_signal(debt):
    b = _f31_lev_trend(debt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build/paydown: 63d log-change of gross debt (recent leverage move)
def f31dt_f31_debt_cycle_trajectory_debtslope_63d_base_v004_signal(debt):
    b = _f31_lev_trend(debt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt (debt - cashneq) level, z-scored vs 252d history
def f31dt_f31_debt_cycle_trajectory_netdebtz_252d_base_v005_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = _z(nd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change over a year (cycle deleveraging / re-leveraging)
def f31dt_f31_debt_cycle_trajectory_netdebtchg_252d_base_v006_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = (nd - nd.shift(252)) / nd.shift(252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change over a quarter
def f31dt_f31_debt_cycle_trajectory_netdebtchg_63d_base_v007_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = (nd - nd.shift(63)) / nd.shift(63).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long debt mix: short-term debt share of total
def f31dt_f31_debt_cycle_trajectory_shortshare_base_v008_signal(debtc, debtnc):
    b = _f31_short_share(debtc, debtnc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-debt share momentum over a year (rollover-risk drift)
def f31dt_f31_debt_cycle_trajectory_shortsharemom_252d_base_v009_signal(debtc, debtnc):
    sh = _f31_short_share(debtc, debtnc)
    b = sh - sh.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow: net cash from debt issuance/repayment, z-scored
def f31dt_f31_debt_cycle_trajectory_debtflowz_252d_base_v010_signal(ncfdebt):
    b = _z(ncfdebt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow smoothed over a quarter (sustained financing direction)
def f31dt_f31_debt_cycle_trajectory_debtflowsm_63d_base_v011_signal(ncfdebt):
    b = _mean(ncfdebt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-at-cycle-peak risk: how close gross debt is to its 1260d max
def f31dt_f31_debt_cycle_trajectory_debtpeakdist_1260d_base_v012_signal(debt):
    b = _f31_peak_dist(debt, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-at-cycle-peak risk: gross debt vs 504d max
def f31dt_f31_debt_cycle_trajectory_debtpeakdist_504d_base_v013_signal(debt):
    b = _f31_peak_dist(debt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cycle position of net debt within its 504d range
def f31dt_f31_debt_cycle_trajectory_netdebtpos_504d_base_v014_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = _f31_cycle_pos(nd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd level z-scored (USD-normalized debt cycle)
def f31dt_f31_debt_cycle_trajectory_debtusdz_252d_base_v015_signal(debtusd):
    b = _z(debtusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd 252d log-slope (USD deleveraging trajectory)
def f31dt_f31_debt_cycle_trajectory_debtusdslope_252d_base_v016_signal(debtusd):
    b = _f31_lev_trend(debtusd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of gross debt (cashneq / debt) — liquidity vs leverage
def f31dt_f31_debt_cycle_trajectory_cashcover_base_v017_signal(debt, cashneq):
    b = cashneq / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage momentum over a year (improving/deteriorating buffer)
def f31dt_f31_debt_cycle_trajectory_cashcovermom_252d_base_v018_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    b = cov - cov.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-cash ratio (how levered net of liquidity)
def f31dt_f31_debt_cycle_trajectory_netdebtcash_base_v019_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = nd / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging acceleration: 63d slope minus 252d slope of debt
def f31dt_f31_debt_cycle_trajectory_levaccel_base_v020_signal(debt):
    s_fast = _f31_lev_trend(debt, 63)
    s_slow = _f31_lev_trend(debt, 252)
    b = s_fast - s_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow as a fraction of gross debt (issuance intensity)
def f31dt_f31_debt_cycle_trajectory_flowintensity_base_v021_signal(ncfdebt, debt):
    b = ncfdebt / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative debt financing over a year relative to debt level
def f31dt_f31_debt_cycle_trajectory_cumflow_252d_base_v022_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    b = cum / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt level z-scored (rollover wall build-up)
def f31dt_f31_debt_cycle_trajectory_shortlvlz_252d_base_v023_signal(debtc):
    b = _z(debtc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt level z-scored (term funding cycle)
def f31dt_f31_debt_cycle_trajectory_longlvlz_252d_base_v024_signal(debtnc):
    b = _z(debtnc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt 126d log-slope (short funding ramp)
def f31dt_f31_debt_cycle_trajectory_shortslope_126d_base_v025_signal(debtc):
    b = _f31_lev_trend(debtc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt 252d log-slope (term issuance trajectory)
def f31dt_f31_debt_cycle_trajectory_longslope_252d_base_v026_signal(debtnc):
    b = _f31_lev_trend(debtnc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: short-debt slope minus long-debt slope (mix shift speed)
def f31dt_f31_debt_cycle_trajectory_mixslopediv_base_v027_signal(debtc, debtnc):
    s_short = _f31_lev_trend(debtc, 126)
    s_long = _f31_lev_trend(debtnc, 126)
    b = s_short - s_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt peak risk x cash thinness: near-peak debt with low cash buffer
def f31dt_f31_debt_cycle_trajectory_peakrisk_base_v028_signal(debt, cashneq):
    peak = _f31_peak_dist(debt, 1260)
    thin = 1.0 / (1.0 + cashneq / debt.replace(0, np.nan))
    b = peak * thin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt percentile-rank within 504d history (cycle phase)
def f31dt_f31_debt_cycle_trajectory_netdebtrank_504d_base_v029_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = _rank(nd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt percentile-rank within 1260d history (rollover-wall cycle phase)
def f31dt_f31_debt_cycle_trajectory_debtrank_1260d_base_v030_signal(debtc):
    b = _rank(debtc, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt acceleration regime streak: consecutive periods of above/below-trend flow
def f31dt_f31_debt_cycle_trajectory_flowstreak_base_v031_signal(ncfdebt):
    dev = ncfdebt - _mean(ncfdebt, 63)
    sgn = np.sign(dev)
    same = (sgn == sgn.shift(1)).astype(float)
    streak = same.groupby((same == 0).cumsum()).cumsum()
    b = streak * sgn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with above-trend debt financing (issuance-heavy regime)
def f31dt_f31_debt_cycle_trajectory_issuefrac_252d_base_v032_signal(ncfdebt):
    above = (ncfdebt > _mean(ncfdebt, 252)).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt amplitude: 1260d high-low span of gross debt normalized by mean (cyclicality)
def f31dt_f31_debt_cycle_trajectory_debtamp_1260d_base_v033_signal(debt):
    hi = _rmax(debt, 1260)
    lo = _rmin(debt, 1260)
    mn = _mean(debt, 1260)
    b = (hi - lo) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt amplitude over 504d normalized by gross debt
def f31dt_f31_debt_cycle_trajectory_netdebtamp_504d_base_v034_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    hi = _rmax(nd, 504)
    lo = _rmin(nd, 504)
    b = (hi - lo) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build from trough: debt vs its 504d minimum (re-leveraging extent)
def f31dt_f31_debt_cycle_trajectory_debttrough_504d_base_v035_signal(debt):
    lo = _rmin(debt, 504)
    b = debt / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt paydown depth from its 504d peak (deleveraging completed, net of cash)
def f31dt_f31_debt_cycle_trajectory_paydowndepth_504d_base_v036_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    hi = _rmax(nd, 504)
    b = (nd - hi) / hi.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow risk-adjusted: financing flow over its own volatility
def f31dt_f31_debt_cycle_trajectory_flowsharpe_252d_base_v037_signal(ncfdebt):
    m = _mean(ncfdebt, 126)
    v = _std(ncfdebt, 126)
    b = m / v.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd-vs-debt wedge (FX/reporting wedge in leverage)
def f31dt_f31_debt_cycle_trajectory_usdwedge_base_v038_signal(debt, debtusd):
    b = debtusd / debt.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt distance above its 1260d trough, in 252d-vol units (deep re-leverage extent)
def f31dt_f31_debt_cycle_trajectory_netdebtcyc_1260d_base_v039_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    lo = _rmin(nd, 1260)
    vol = nd.diff().rolling(252, min_periods=126).std()
    b = (nd - lo) / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-share extremity z-scored vs own history (rollover stress regime)
def f31dt_f31_debt_cycle_trajectory_shortsharez_252d_base_v040_signal(debtc, debtnc):
    sh = _f31_short_share(debtc, debtnc)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawn down against debt: change in cash coverage over a quarter
def f31dt_f31_debt_cycle_trajectory_cashburnlev_63d_base_v041_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    b = cov - cov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt slope per unit of debt volatility (clean deleveraging trend)
def f31dt_f31_debt_cycle_trajectory_levtrendvol_252d_base_v042_signal(debt):
    slope = _f31_lev_trend(debt, 63)
    vol = np.log(debt.replace(0, np.nan)).diff().rolling(126, min_periods=63).std()
    b = slope / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed net-debt momentum (bounded re-leveraging signal)
def f31dt_f31_debt_cycle_trajectory_netdebttanh_126d_base_v043_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    chg = (nd - nd.shift(126)) / nd.shift(126).abs().replace(0, np.nan)
    b = np.tanh(3.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow direction relative to net-debt change (consistency check)
def f31dt_f31_debt_cycle_trajectory_flowconsist_63d_base_v044_signal(ncfdebt, debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    ndchg = nd - nd.shift(63)
    fl = _mean(ncfdebt, 63)
    b = np.sign(fl) * np.sign(ndchg) * (fl.abs() / debt.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-cycle peak proximity over multiple horizons (worst-case nearness)
def f31dt_f31_debt_cycle_trajectory_multipeak_base_v045_signal(debt):
    p1 = _f31_peak_dist(debt, 252)
    p2 = _f31_peak_dist(debt, 504)
    p3 = _f31_peak_dist(debt, 1260)
    b = pd.concat([p1, p2, p3], axis=1).max(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt share trend (terming-out of debt, opposite of short share)
def f31dt_f31_debt_cycle_trajectory_longshareslope_126d_base_v046_signal(debtc, debtnc):
    tot = (debtc + debtnc).replace(0, np.nan)
    lsh = debtnc / tot
    b = lsh - lsh.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt slope smoothed by EMA (persistent leverage direction)
def f31dt_f31_debt_cycle_trajectory_netdebtema_base_v047_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    chg = nd.diff()
    b = chg.ewm(span=63, min_periods=21).mean() / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow swing within the quarter (issuance volatility / debt)
def f31dt_f31_debt_cycle_trajectory_issueburst_63d_base_v048_signal(ncfdebt, debt):
    hi = ncfdebt.rolling(63, min_periods=21).max()
    lo = ncfdebt.rolling(63, min_periods=21).min()
    b = (hi - lo) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paydown burst depth below typical: quarter-min flow vs quarter-mean flow / debt
def f31dt_f31_debt_cycle_trajectory_paydownburst_63d_base_v049_signal(ncfdebt, debt):
    lo = ncfdebt.rolling(63, min_periods=21).min()
    mn = ncfdebt.rolling(63, min_periods=21).mean()
    b = (mn - lo) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt level percentile vs 504d, interacted with short-share (risky-mix peak)
def f31dt_f31_debt_cycle_trajectory_riskmixpeak_base_v050_signal(debt, debtc, debtnc):
    rk = _rank(debt, 504) + 0.5
    sh = _f31_short_share(debtc, debtnc)
    b = rk * sh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-debt growth decoupled from cash growth (debt outrunning liquidity)
def f31dt_f31_debt_cycle_trajectory_debtyoy_base_v051_signal(debt, cashneq):
    dg = debt / debt.shift(252).replace(0, np.nan) - 1.0
    cg = cashneq / cashneq.shift(252).replace(0, np.nan) - 1.0
    b = dg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year short-term debt growth (rollover-wall growth)
def f31dt_f31_debt_cycle_trajectory_shortyoy_base_v052_signal(debtc):
    b = debtc / debtc.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow cumulative vs cash (debt funding the cash pile)
def f31dt_f31_debt_cycle_trajectory_flowvscash_252d_base_v053_signal(ncfdebt, cashneq):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    b = cum / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-cash ratio z-scored (deleveraging stress de-trended)
def f31dt_f31_debt_cycle_trajectory_ndcashz_252d_base_v054_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    ratio = nd / cashneq.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt convexity proxy: how the cycle position curves (pos minus mid distance^2)
def f31dt_f31_debt_cycle_trajectory_debtconvex_504d_base_v055_signal(debt):
    cp = _f31_cycle_pos(debt, 504)
    b = np.sign(cp - 0.5) * (cp - 0.5) ** 2 * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long mix acceleration: 63d change of the short/long log-ratio momentum
def f31dt_f31_debt_cycle_trajectory_mixspread_base_v056_signal(debtc, debtnc):
    lr = np.log(debtc.replace(0, np.nan)) - np.log(debtnc.replace(0, np.nan))
    mom = lr - lr.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd net-of-cash level z (USD net leverage cycle)
def f31dt_f31_debt_cycle_trajectory_usdnetz_252d_base_v057_signal(debtusd, cashneq):
    nd = debtusd - cashneq
    b = _z(nd, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how long since debt last at a 504d low (staleness of deleveraging trough)
def f31dt_f31_debt_cycle_trajectory_dsltrough_504d_base_v058_signal(debt):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = debt.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how long since debt last at a 504d peak (time since max leverage)
def f31dt_f31_debt_cycle_trajectory_dshpeak_504d_base_v059_signal(debt):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = debt.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# non-flow debt drift: debt change minus reported financing flow, in debt-vol units
def f31dt_f31_debt_cycle_trajectory_flowvsdebt_126d_base_v060_signal(ncfdebt, debt):
    dchg = debt - debt.shift(126)
    fl = ncfdebt.rolling(126, min_periods=63).sum()
    resid = dchg - fl
    sd = resid.rolling(252, min_periods=126).std()
    b = resid / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt build velocity over a month normalized by debt
def f31dt_f31_debt_cycle_trajectory_netdebtvel_21d_base_v061_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    b = (nd - nd.shift(21)) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of net debt-reduction quarters over the last year (deleveraging persistence)
def f31dt_f31_debt_cycle_trajectory_delevcount_252d_base_v062_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    dq = (nd.diff(63) < 0).astype(float)
    b = dq.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-debt log-slope smoothed (clean cycle deleveraging trend)
def f31dt_f31_debt_cycle_trajectory_debtslopesm_base_v063_signal(debt):
    sl = np.log(debt.replace(0, np.nan)).diff()
    b = sl.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-cash ratio cycle position (leverage stress phase, 504d)
def f31dt_f31_debt_cycle_trajectory_dcashcyc_504d_base_v064_signal(debt, cashneq):
    ratio = debt / cashneq.replace(0, np.nan)
    b = _f31_cycle_pos(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net debt rebuild off trough scaled by time since trough (re-leverage rate)
def f31dt_f31_debt_cycle_trajectory_rebuildrate_504d_base_v065_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    lo = _rmin(nd, 504)
    ext = nd / lo.replace(0, np.nan).abs() - np.sign(lo)

    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsl = nd.rolling(504, min_periods=252).apply(_f, raw=True).replace(0, np.nan)
    b = ext / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-debt level relative to cash (immediate rollover liquidity gap)
def f31dt_f31_debt_cycle_trajectory_shortvscash_base_v066_signal(debtc, cashneq):
    b = debtc / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-cash gap momentum over a year (worsening rollover liquidity)
def f31dt_f31_debt_cycle_trajectory_shortcashmom_252d_base_v067_signal(debtc, cashneq):
    ratio = debtc / cashneq.replace(0, np.nan)
    b = ratio - ratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd peak distance over 1260d (USD debt-at-peak risk)
def f31dt_f31_debt_cycle_trajectory_usdpeakdist_1260d_base_v068_signal(debtusd):
    b = _f31_peak_dist(debtusd, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of debt slope across 63/126/252 horizons (trajectory disagreement)
def f31dt_f31_debt_cycle_trajectory_slopedisp_base_v069_signal(debt):
    s1 = _f31_lev_trend(debt, 63)
    s2 = _f31_lev_trend(debt, 126)
    s3 = _f31_lev_trend(debt, 252)
    b = pd.concat([s1, s2, s3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow percentile-rank within 504d (issuance-cycle phase)
def f31dt_f31_debt_cycle_trajectory_flowrank_504d_base_v070_signal(ncfdebt):
    b = _rank(ncfdebt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short+long term-debt total vs reported gross debt (component reconciliation gap)
def f31dt_f31_debt_cycle_trajectory_netgrossratio_base_v071_signal(debt, debtc, debtnc):
    tot = debtc + debtnc
    b = tot / debt.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net/gross ratio momentum over a half-year (cash-cushion erosion)
def f31dt_f31_debt_cycle_trajectory_netgrossmom_126d_base_v072_signal(debt, cashneq):
    nd = _f31_net_debt(debt, cashneq)
    ratio = nd / debt.replace(0, np.nan)
    b = ratio - ratio.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined cycle-peak distress: near-peak debt x rising short share x thin cash
def f31dt_f31_debt_cycle_trajectory_distresscombo_base_v073_signal(debt, debtc, debtnc, cashneq):
    peak = _f31_peak_dist(debt, 1260)
    sh = _f31_short_share(debtc, debtnc)
    thin = 1.0 / (1.0 + cashneq / debt.replace(0, np.nan))
    b = peak * sh * thin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd log-slope acceleration (USD leverage jerk-ish over base horizons)
def f31dt_f31_debt_cycle_trajectory_usdaccel_base_v074_signal(debtusd):
    s_fast = _f31_lev_trend(debtusd, 63)
    s_slow = _f31_lev_trend(debtusd, 252)
    b = s_fast - s_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mix-weighted financing pressure: short-share interacted with recent flow intensity z
def f31dt_f31_debt_cycle_trajectory_levmixflow_base_v075_signal(debtc, debtnc, ncfdebt):
    sh = _f31_short_share(debtc, debtnc)
    flow = ncfdebt.rolling(63, min_periods=21).sum()
    fz = _z(flow, 252)
    b = sh * fz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31dt_f31_debt_cycle_trajectory_debtlvl_252d_base_v001_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_252d_base_v002_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_126d_base_v003_signal,
    f31dt_f31_debt_cycle_trajectory_debtslope_63d_base_v004_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtz_252d_base_v005_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtchg_252d_base_v006_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtchg_63d_base_v007_signal,
    f31dt_f31_debt_cycle_trajectory_shortshare_base_v008_signal,
    f31dt_f31_debt_cycle_trajectory_shortsharemom_252d_base_v009_signal,
    f31dt_f31_debt_cycle_trajectory_debtflowz_252d_base_v010_signal,
    f31dt_f31_debt_cycle_trajectory_debtflowsm_63d_base_v011_signal,
    f31dt_f31_debt_cycle_trajectory_debtpeakdist_1260d_base_v012_signal,
    f31dt_f31_debt_cycle_trajectory_debtpeakdist_504d_base_v013_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtpos_504d_base_v014_signal,
    f31dt_f31_debt_cycle_trajectory_debtusdz_252d_base_v015_signal,
    f31dt_f31_debt_cycle_trajectory_debtusdslope_252d_base_v016_signal,
    f31dt_f31_debt_cycle_trajectory_cashcover_base_v017_signal,
    f31dt_f31_debt_cycle_trajectory_cashcovermom_252d_base_v018_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtcash_base_v019_signal,
    f31dt_f31_debt_cycle_trajectory_levaccel_base_v020_signal,
    f31dt_f31_debt_cycle_trajectory_flowintensity_base_v021_signal,
    f31dt_f31_debt_cycle_trajectory_cumflow_252d_base_v022_signal,
    f31dt_f31_debt_cycle_trajectory_shortlvlz_252d_base_v023_signal,
    f31dt_f31_debt_cycle_trajectory_longlvlz_252d_base_v024_signal,
    f31dt_f31_debt_cycle_trajectory_shortslope_126d_base_v025_signal,
    f31dt_f31_debt_cycle_trajectory_longslope_252d_base_v026_signal,
    f31dt_f31_debt_cycle_trajectory_mixslopediv_base_v027_signal,
    f31dt_f31_debt_cycle_trajectory_peakrisk_base_v028_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtrank_504d_base_v029_signal,
    f31dt_f31_debt_cycle_trajectory_debtrank_1260d_base_v030_signal,
    f31dt_f31_debt_cycle_trajectory_flowstreak_base_v031_signal,
    f31dt_f31_debt_cycle_trajectory_issuefrac_252d_base_v032_signal,
    f31dt_f31_debt_cycle_trajectory_debtamp_1260d_base_v033_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtamp_504d_base_v034_signal,
    f31dt_f31_debt_cycle_trajectory_debttrough_504d_base_v035_signal,
    f31dt_f31_debt_cycle_trajectory_paydowndepth_504d_base_v036_signal,
    f31dt_f31_debt_cycle_trajectory_flowsharpe_252d_base_v037_signal,
    f31dt_f31_debt_cycle_trajectory_usdwedge_base_v038_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtcyc_1260d_base_v039_signal,
    f31dt_f31_debt_cycle_trajectory_shortsharez_252d_base_v040_signal,
    f31dt_f31_debt_cycle_trajectory_cashburnlev_63d_base_v041_signal,
    f31dt_f31_debt_cycle_trajectory_levtrendvol_252d_base_v042_signal,
    f31dt_f31_debt_cycle_trajectory_netdebttanh_126d_base_v043_signal,
    f31dt_f31_debt_cycle_trajectory_flowconsist_63d_base_v044_signal,
    f31dt_f31_debt_cycle_trajectory_multipeak_base_v045_signal,
    f31dt_f31_debt_cycle_trajectory_longshareslope_126d_base_v046_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtema_base_v047_signal,
    f31dt_f31_debt_cycle_trajectory_issueburst_63d_base_v048_signal,
    f31dt_f31_debt_cycle_trajectory_paydownburst_63d_base_v049_signal,
    f31dt_f31_debt_cycle_trajectory_riskmixpeak_base_v050_signal,
    f31dt_f31_debt_cycle_trajectory_debtyoy_base_v051_signal,
    f31dt_f31_debt_cycle_trajectory_shortyoy_base_v052_signal,
    f31dt_f31_debt_cycle_trajectory_flowvscash_252d_base_v053_signal,
    f31dt_f31_debt_cycle_trajectory_ndcashz_252d_base_v054_signal,
    f31dt_f31_debt_cycle_trajectory_debtconvex_504d_base_v055_signal,
    f31dt_f31_debt_cycle_trajectory_mixspread_base_v056_signal,
    f31dt_f31_debt_cycle_trajectory_usdnetz_252d_base_v057_signal,
    f31dt_f31_debt_cycle_trajectory_dsltrough_504d_base_v058_signal,
    f31dt_f31_debt_cycle_trajectory_dshpeak_504d_base_v059_signal,
    f31dt_f31_debt_cycle_trajectory_flowvsdebt_126d_base_v060_signal,
    f31dt_f31_debt_cycle_trajectory_netdebtvel_21d_base_v061_signal,
    f31dt_f31_debt_cycle_trajectory_delevcount_252d_base_v062_signal,
    f31dt_f31_debt_cycle_trajectory_debtslopesm_base_v063_signal,
    f31dt_f31_debt_cycle_trajectory_dcashcyc_504d_base_v064_signal,
    f31dt_f31_debt_cycle_trajectory_rebuildrate_504d_base_v065_signal,
    f31dt_f31_debt_cycle_trajectory_shortvscash_base_v066_signal,
    f31dt_f31_debt_cycle_trajectory_shortcashmom_252d_base_v067_signal,
    f31dt_f31_debt_cycle_trajectory_usdpeakdist_1260d_base_v068_signal,
    f31dt_f31_debt_cycle_trajectory_slopedisp_base_v069_signal,
    f31dt_f31_debt_cycle_trajectory_flowrank_504d_base_v070_signal,
    f31dt_f31_debt_cycle_trajectory_netgrossratio_base_v071_signal,
    f31dt_f31_debt_cycle_trajectory_netgrossmom_126d_base_v072_signal,
    f31dt_f31_debt_cycle_trajectory_distresscombo_base_v073_signal,
    f31dt_f31_debt_cycle_trajectory_usdaccel_base_v074_signal,
    f31dt_f31_debt_cycle_trajectory_levmixflow_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_DEBT_CYCLE_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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

    debt = _fund(101, base=5e8, drift=0.01, vol=0.10).rename("debt")
    debtusd = (_fund(102, base=5e8, drift=0.01, vol=0.10) * 1.02).rename("debtusd")
    debtc = _fund(103, base=1.5e8, drift=0.005, vol=0.12).rename("debtc")
    debtnc = _fund(104, base=3.5e8, drift=0.008, vol=0.09).rename("debtnc")
    cashneq = _fund(105, base=2e8, drift=0.0, vol=0.15).rename("cashneq")
    ncfdebt = _fund(106, base=8e7, drift=0.0, vol=0.30, allow_neg=True).rename("ncfdebt")

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

    print("OK f31_debt_cycle_trajectory_base_001_075_claude: %d features pass" % n_features)
