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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives: debt / leverage trajectory =====
def _f34_netdebt(debt, cashneq):
    return debt - cashneq


def _f34_chg(s, w):
    return s - s.shift(w)


def _f34_logchg(s, w):
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(w).replace(0, np.nan))


def _f34_debt_ebitda(debt, ebitda):
    return debt / ebitda.replace(0, np.nan)


def _f34_shortmix(debtc, debt):
    return debtc / debt.replace(0, np.nan)


def _f34_longmix(debtnc, debt):
    return debtnc / debt.replace(0, np.nan)


def _f34_paydown_flow(ncfdebt, debt):
    return ncfdebt / debt.replace(0, np.nan)


# ============================================================
# debt level relative to its 252d mean (build extension)
def f34dt_f34_debt_leverage_trajectory_debtext_252d_base_v076_signal(debt):
    mn = _mean(debt, 252)
    b = debt / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt level relative to its 252d mean (front-end build extension)
def f34dt_f34_debt_leverage_trajectory_shortext_252d_base_v077_signal(debtc):
    mn = _mean(debtc, 252)
    b = debtc / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt level relative to its 252d mean (back-end build extension)
def f34dt_f34_debt_leverage_trajectory_longext_252d_base_v078_signal(debtnc):
    mn = _mean(debtnc, 252)
    b = debtnc / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt / ebitda z-scored vs own 252d history (net leverage stretch)
def f34dt_f34_debt_leverage_trajectory_netlevz_252d_base_v079_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = nd / ebitda.replace(0, np.nan)
    b = _z(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt mix percentile rank vs 504d history (maturity-wall regime)
def f34dt_f34_debt_leverage_trajectory_shortmixrank_504d_base_v080_signal(debtc, debt):
    m = _f34_shortmix(debtc, debt)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt quarterly flow minus its trailing-year average (financing impulse)
def f34dt_f34_debt_leverage_trajectory_flowimpulse_63d_base_v081_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    fq = f.rolling(63, min_periods=21).mean()
    fy = f.rolling(252, min_periods=126).mean()
    b = fq - fy
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda 63d slope minus 252d slope (leverage trend divergence)
def f34dt_f34_debt_leverage_trajectory_levtrenddiv_base_v082_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    s_short = (lev - lev.shift(63)) / 63.0
    s_long = (lev - lev.shift(252)) / 252.0
    b = s_short - s_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt log-growth half-year vs quarter (build acceleration spread)
def f34dt_f34_debt_leverage_trajectory_buildspread_base_v083_signal(debt):
    g63 = _f34_logchg(debt, 63)
    g126 = _f34_logchg(debt, 126)
    b = g63 - 0.5 * g126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash buffer (cashneq/debt) z-scored vs 252d history (cushion stretch)
def f34dt_f34_debt_leverage_trajectory_cushionz_252d_base_v084_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change scaled by ebitda, z-scored (incremental leverage surprise)
def f34dt_f34_debt_leverage_trajectory_incrlevz_126d_base_v085_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    incr = _f34_chg(nd, 126) / ebitda.abs().replace(0, np.nan)
    b = _z(incr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-skew change over a year (maturity-structure rotation)
def f34dt_f34_debt_leverage_trajectory_termskewchg_252d_base_v086_signal(debtnc, debtc, debt):
    skew = (debtnc - debtc) / debt.replace(0, np.nan)
    b = _f34_chg(skew, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda smoothed deviation from slow EMA (leverage displacement)
def f34dt_f34_debt_leverage_trajectory_levdisp_base_v087_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = lev - lev.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt-to-cash rank vs 504d history (refinancing-risk regime)
def f34dt_f34_debt_leverage_trajectory_shorttocashrank_504d_base_v088_signal(debtc, cashneq):
    r = debtc / cashneq.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt cumulative half-year flow scaled by ebitda (earnings-funded financing)
def f34dt_f34_debt_leverage_trajectory_flowtoearn_126d_base_v089_signal(ncfdebt, ebitda):
    cum = ncfdebt.rolling(126, min_periods=63).sum()
    b = cum / ebitda.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build pace minus ebitda build pace, smoothed (sustained over-borrow)
def f34dt_f34_debt_leverage_trajectory_overborrow_sm_base_v090_signal(debt, ebitda):
    dg = _f34_logchg(debt, 63)
    eg = _f34_logchg(ebitda.abs(), 63)
    diff = dg - eg
    b = diff.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year debt/ebitda fell vs prior quarter (deleveraging persistence)
def f34dt_f34_debt_leverage_trajectory_delevpersist_252d_base_v091_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    down = (lev < lev.shift(63)).astype(float)
    b = down.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt momentum over a half-year scaled by ebitda (coverage drift)
def f34dt_f34_debt_leverage_trajectory_netdriftcov_126d_base_v092_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    b = _f34_chg(nd, 126) / ebitda.abs().replace(0, np.nan).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-debt vs long-debt growth ratio (refinancing rotation magnitude)
def f34dt_f34_debt_leverage_trajectory_rotationmag_126d_base_v093_signal(debtc, debtnc):
    sg = _f34_logchg(debtc, 126)
    lg = _f34_logchg(debtnc, 126)
    b = np.tanh(sg - lg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt buffer 63d slope (cushion velocity)
def f34dt_f34_debt_leverage_trajectory_cushionvel_63d_base_v094_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    b = (cov - cov.shift(63)) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda coverage of total debt (ebitda/debt), z-scored (serviceability regime)
def f34dt_f34_debt_leverage_trajectory_servicez_252d_base_v095_signal(ebitda, debt):
    cov = ebitda / debt.replace(0, np.nan)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow sign-magnitude (compressed direction of net issuance)
def f34dt_f34_debt_leverage_trajectory_flowsignmag_base_v096_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    b = np.sign(f) * (f.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/ebitda curvature (second difference over yearly spans)
def f34dt_f34_debt_leverage_trajectory_netlevcurv_base_v097_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = nd / ebitda.replace(0, np.nan)
    b = lev - 2.0 * lev.shift(126) + lev.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt growth minus total debt growth (front-end skew velocity)
def f34dt_f34_debt_leverage_trajectory_frontskewvel_126d_base_v098_signal(debtc, debt):
    sg = _f34_logchg(debtc, 126)
    dg = _f34_logchg(debt, 126)
    b = sg - dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt growth minus total debt growth (back-end skew velocity)
def f34dt_f34_debt_leverage_trajectory_backskewvel_126d_base_v099_signal(debtnc, debt):
    lg = _f34_logchg(debtnc, 126)
    dg = _f34_logchg(debt, 126)
    b = lg - dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage level interacted with deleveraging slope (high-and-falling vs high-and-rising)
def f34dt_f34_debt_leverage_trajectory_levxslope_base_v100_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    slope = (lev - lev.shift(126)) / 126.0
    b = np.tanh(lev / 5.0) * np.sign(slope) * slope.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow dispersion ratio: 63d std vs 252d std (financing lumpiness shift)
def f34dt_f34_debt_leverage_trajectory_flowlumpshift_base_v101_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    s63 = _std(f, 63)
    s252 = _std(f, 252)
    b = s63 / s252.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change scaled by debt, percentile-ranked vs 252d (net-deleveraging regime)
def f34dt_f34_debt_leverage_trajectory_netscaledrank_252d_base_v102_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    chg = _f34_chg(nd, 63)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build acceleration scaled by leverage (levered re-acceleration)
def f34dt_f34_debt_leverage_trajectory_levreaccel_base_v103_signal(debt, ebitda):
    g = _f34_logchg(debt, 63)
    accel = g - g.shift(63)
    lev = _f34_debt_ebitda(debt, ebitda)
    b = accel * np.tanh(lev / 4.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt coverage by cash, change over a quarter (near-term liquidity drift)
def f34dt_f34_debt_leverage_trajectory_liqdrift_63d_base_v104_signal(cashneq, debtc):
    cov = cashneq / debtc.replace(0, np.nan)
    b = _f34_chg(cov, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-led-debt cumulative race over two years (structural earnings vs leverage)
def f34dt_f34_debt_leverage_trajectory_structrace_504d_base_v105_signal(debt, ebitda):
    eg = _f34_logchg(ebitda.abs(), 504)
    dg = _f34_logchg(debt, 504)
    b = eg - dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing posture regime: half-year mean financing flow percentile-ranked vs history
def f34dt_f34_debt_leverage_trajectory_posturerank_base_v106_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    fm = f.rolling(126, min_periods=63).mean()
    b = _rank(fm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage volatility ratio: 126d std vs 504d std (coverage-instability shift)
def f34dt_f34_debt_leverage_trajectory_levvolshift_base_v107_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    v126 = _std(lev, 126)
    v504 = _std(lev, 504)
    b = v126 / v504.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt smoothed level vs its yearly lag (de-noised net-leverage trend)
def f34dt_f34_debt_leverage_trajectory_netsmtrend_base_v108_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    sm = nd.ewm(span=63, min_periods=21).mean()
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-mix interacted with leverage (short-funded leverage risk)
def f34dt_f34_debt_leverage_trajectory_shortlev_base_v109_signal(debtc, debt, ebitda):
    m = _f34_shortmix(debtc, debt)
    lev = _f34_debt_ebitda(debt, ebitda)
    b = m * np.tanh(lev / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative ncfdebt over two years scaled by debt (structural financing trend)
def f34dt_f34_debt_leverage_trajectory_flowstruct_504d_base_v110_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(504, min_periods=252).sum()
    b = cum / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda yearly change z-scored (deleveraging-trajectory surprise)
def f34dt_f34_debt_leverage_trajectory_levtrajz_252d_base_v111_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    chg = _f34_chg(lev, 252)
    b = _z(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash buffer build minus debt build (deleveraging via cash accumulation)
def f34dt_f34_debt_leverage_trajectory_cashdelev_252d_base_v112_signal(cashneq, debt):
    cg = _f34_logchg(cashneq, 252)
    dg = _f34_logchg(debt, 252)
    b = cg - dg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt growth acceleration (front-end re-acceleration)
def f34dt_f34_debt_leverage_trajectory_shortaccel_base_v113_signal(debtc):
    g = _f34_logchg(debtc, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt growth acceleration (back-end re-acceleration)
def f34dt_f34_debt_leverage_trajectory_longaccel_base_v114_signal(debtnc):
    g = _f34_logchg(debtnc, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-ebitda gap vs its long mean (net-leverage richness)
def f34dt_f34_debt_leverage_trajectory_netlevgap_base_v115_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = nd / ebitda.replace(0, np.nan)
    b = lev - _mean(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow trend: 63d mean minus 126d mean (financing momentum)
def f34dt_f34_debt_leverage_trajectory_flowmom_base_v116_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    b = _mean(f, 63) - _mean(f, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage breach intensity scaled by build (high-and-building stress)
def f34dt_f34_debt_leverage_trajectory_stressbuild_base_v117_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    med = lev.rolling(252, min_periods=126).median()
    stress = (lev - med).clip(lower=0)
    g = _f34_logchg(debt, 126)
    b = stress * np.tanh(5.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt extension dispersion: rolling std of debt/252d-mean ratio (build instability)
def f34dt_f34_debt_leverage_trajectory_extdisp_base_v118_signal(debt):
    mn = _mean(debt, 252)
    ext = debt / mn.replace(0, np.nan)
    b = _std(ext, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-funding share: debt build as a fraction of combined debt+cash build (funding mix)
def f34dt_f34_debt_leverage_trajectory_fundmix_252d_base_v119_signal(debt, cashneq):
    dg = _f34_chg(debt, 252).abs()
    cg = _f34_chg(cashneq, 252).abs()
    b = dg / (dg + cg).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt mix EMA-smoothed (persistent maturity profile)
def f34dt_f34_debt_leverage_trajectory_shortmixema_base_v120_signal(debtc, debt):
    m = _f34_shortmix(debtc, debt)
    b = m.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage convergence: 126d mean minus 504d mean (medium-vs-long leverage drift)
def f34dt_f34_debt_leverage_trajectory_levconv2_base_v121_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _mean(lev, 126) - _mean(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net financing intensity quarterly, z-scored (financing-intensity surprise)
def f34dt_f34_debt_leverage_trajectory_flowintz_63d_base_v122_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(63, min_periods=21).sum() / debt.replace(0, np.nan)
    b = _z(cum, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build minus ebitda build, ranked (over-borrow regime percentile)
def f34dt_f34_debt_leverage_trajectory_overborrowrank_base_v123_signal(debt, ebitda):
    dg = _f34_logchg(debt, 126)
    eg = _f34_logchg(ebitda.abs(), 126)
    b = _rank(dg - eg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt move standardized by its own volatility (statistically large leverage shift)
def f34dt_f34_debt_leverage_trajectory_netincrsign_base_v124_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    chg = _f34_chg(nd, 63)
    vol = _std(chg, 252)
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term coverage (ebitda/debtc) percentile-ranked vs 504d (near-term serviceability regime)
def f34dt_f34_debt_leverage_trajectory_shortcovrank_504d_base_v125_signal(ebitda, debtc):
    cov = ebitda / debtc.replace(0, np.nan)
    b = _rank(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage 252d slope per day normalized by leverage level (relative delev rate)
def f34dt_f34_debt_leverage_trajectory_rellevslope_base_v126_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = (lev - lev.shift(252)) / (252.0 * lev.shift(252).abs().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawdown vs debt: cash below its 252d max while debt rising (squeeze)
def f34dt_f34_debt_leverage_trajectory_cashsqueeze_base_v127_signal(cashneq, debt):
    cash_peak = cashneq.rolling(252, min_periods=126).max()
    drawdown = cashneq / cash_peak.replace(0, np.nan) - 1.0
    dg = _f34_logchg(debt, 126)
    b = drawdown * np.tanh(10.0 * dg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# front-funded issuance: cumulative financing flow gated by the shift toward short debt
def f34dt_f34_debt_leverage_trajectory_frontfund_base_v128_signal(ncfdebt, debtc, debt):
    cum = ncfdebt.rolling(126, min_periods=63).sum() / debt.replace(0, np.nan)
    m = _f34_shortmix(debtc, debt)
    m_shift = m - m.rolling(252, min_periods=126).mean()
    b = cum * np.tanh(10.0 * m_shift)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage above 504d 90th-pct excess, smoothed (tail-leverage proximity)
def f34dt_f34_debt_leverage_trajectory_tailev_base_v129_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    thr = lev.rolling(504, min_periods=126).quantile(0.90)
    excess = (lev - thr).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt half-year change minus its prior half-year change (net leverage jerk-proxy)
def f34dt_f34_debt_leverage_trajectory_netchgaccel_base_v130_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    chg = _f34_chg(nd, 126)
    b = chg - chg.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth dispersion ratio: 126d std vs 504d std (build-vol regime shift)
def f34dt_f34_debt_leverage_trajectory_buildvolshift_base_v131_signal(debt):
    g = _f34_logchg(debt, 63)
    v126 = _std(g, 126)
    v504 = _std(g, 504)
    b = v126 / v504.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt buffer EMA-smoothed (persistent net-cash posture)
def f34dt_f34_debt_leverage_trajectory_cushionema_base_v132_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    b = cov.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda coverage of short debt, slope per day (near-term serviceability velocity)
def f34dt_f34_debt_leverage_trajectory_shortcovvel_base_v133_signal(ebitda, debtc):
    cov = ebitda / debtc.replace(0, np.nan)
    b = (cov - cov.shift(126)) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing flow cumulative quarterly minus prior quarter (issuance reversal scaled by ebitda)
def f34dt_f34_debt_leverage_trajectory_issuereversal_base_v134_signal(ncfdebt, ebitda):
    cum = ncfdebt.rolling(63, min_periods=21).sum()
    b = (cum - cum.shift(63)) / ebitda.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure entropy proxy: short and long mix balance distance from 50/50
def f34dt_f34_debt_leverage_trajectory_termbalance_base_v135_signal(debtc, debtnc, debt):
    sm = _f34_shortmix(debtc, debt)
    lm = _f34_longmix(debtnc, debt)
    b = (sm - lm).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-ebitda smoothed minus yearly lag (clean net-leverage trajectory)
def f34dt_f34_debt_leverage_trajectory_netlevsmtraj_base_v136_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = (nd / ebitda.replace(0, np.nan)).ewm(span=63, min_periods=21).mean()
    b = lev - lev.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year financing flow exceeded its 252d 75th-pct (issuance-burst lean)
def f34dt_f34_debt_leverage_trajectory_issueburst_base_v137_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    thr = f.rolling(252, min_periods=126).quantile(0.75)
    burst = (f > thr).astype(float)
    b = burst.rolling(252, min_periods=126).mean() - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage level times short-term-debt-to-cash (compounded refinancing+leverage risk)
def f34dt_f34_debt_leverage_trajectory_compoundrisk_base_v138_signal(debt, ebitda, debtc, cashneq):
    lev = _f34_debt_ebitda(debt, ebitda)
    refi = debtc / cashneq.replace(0, np.nan)
    b = np.tanh(lev / 5.0) * np.tanh(refi)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt extension velocity: change in (debt/252d-mean) over a quarter
def f34dt_f34_debt_leverage_trajectory_extvel_63d_base_v139_signal(debt):
    mn = _mean(debt, 252)
    ext = debt / mn.replace(0, np.nan)
    b = _f34_chg(ext, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of total debt minus its yearly lag (cushion structural trend)
def f34dt_f34_debt_leverage_trajectory_cushiontrend_504d_base_v140_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    b = cov - cov.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt sign-stability: rolling std of flow direction (financing consistency)
def f34dt_f34_debt_leverage_trajectory_flowconsist_base_v141_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    direction = np.sign(f - f.rolling(252, min_periods=126).median())
    b = -_std(direction, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage curvature scaled by level (relative leverage convexity)
def f34dt_f34_debt_leverage_trajectory_relcurv_base_v142_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    curv = lev - 2.0 * lev.shift(63) + lev.shift(126)
    b = curv / lev.abs().rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long debt level ratio (debtc/debtnc), z-scored (maturity-tilt regime)
def f34dt_f34_debt_leverage_trajectory_sltiltz_base_v143_signal(debtc, debtnc):
    ratio = debtc / debtnc.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt extension: net-debt/debt minus its 504d mean (net-leverage stretch)
def f34dt_f34_debt_leverage_trajectory_netext_base_v144_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    b = nd - _mean(nd, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing intensity vs deleveraging: cum flow times sign of leverage change
def f34dt_f34_debt_leverage_trajectory_flowdelevalign_base_v145_signal(ncfdebt, debt, ebitda):
    cum = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    lev = _f34_debt_ebitda(debt, ebitda)
    levchg = lev - lev.shift(252)
    b = cum * np.sign(levchg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build pace minus cash build pace, ranked (relative-funding regime)
def f34dt_f34_debt_leverage_trajectory_fundrank_base_v146_signal(debt, cashneq):
    dg = _f34_logchg(debt, 126)
    cg = _f34_logchg(cashneq, 126)
    b = _rank(dg - cg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage tail-time change: shift in fraction of time above 504d median over a year
def f34dt_f34_debt_leverage_trajectory_levtailtime_base_v147_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    med = lev.rolling(504, min_periods=126).median()
    above = (lev > med).astype(float)
    frac = above.rolling(126, min_periods=63).mean()
    b = frac - frac.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt build cumulative scaled by total debt (front-end issuance trend)
def f34dt_f34_debt_leverage_trajectory_shortbuildcum_base_v148_signal(debtc, debt):
    build = _f34_chg(debtc, 252)
    b = build / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-ebitda 63d mean minus 252d mean (net-leverage convergence)
def f34dt_f34_debt_leverage_trajectory_netlevconv_base_v149_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = nd / ebitda.replace(0, np.nan)
    b = _mean(lev, 63) - _mean(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite deleveraging momentum: cash-build minus debt-build, weighted by coverage gain
def f34dt_f34_debt_leverage_trajectory_delevmom_base_v150_signal(debt, cashneq, ebitda):
    cg = _f34_logchg(cashneq, 126)
    dg = _f34_logchg(debt, 126)
    lev = _f34_debt_ebitda(debt, ebitda)
    gain = -(lev - lev.shift(126))
    b = (cg - dg) * np.tanh(gain)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34dt_f34_debt_leverage_trajectory_debtext_252d_base_v076_signal,
    f34dt_f34_debt_leverage_trajectory_shortext_252d_base_v077_signal,
    f34dt_f34_debt_leverage_trajectory_longext_252d_base_v078_signal,
    f34dt_f34_debt_leverage_trajectory_netlevz_252d_base_v079_signal,
    f34dt_f34_debt_leverage_trajectory_shortmixrank_504d_base_v080_signal,
    f34dt_f34_debt_leverage_trajectory_flowimpulse_63d_base_v081_signal,
    f34dt_f34_debt_leverage_trajectory_levtrenddiv_base_v082_signal,
    f34dt_f34_debt_leverage_trajectory_buildspread_base_v083_signal,
    f34dt_f34_debt_leverage_trajectory_cushionz_252d_base_v084_signal,
    f34dt_f34_debt_leverage_trajectory_incrlevz_126d_base_v085_signal,
    f34dt_f34_debt_leverage_trajectory_termskewchg_252d_base_v086_signal,
    f34dt_f34_debt_leverage_trajectory_levdisp_base_v087_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocashrank_504d_base_v088_signal,
    f34dt_f34_debt_leverage_trajectory_flowtoearn_126d_base_v089_signal,
    f34dt_f34_debt_leverage_trajectory_overborrow_sm_base_v090_signal,
    f34dt_f34_debt_leverage_trajectory_delevpersist_252d_base_v091_signal,
    f34dt_f34_debt_leverage_trajectory_netdriftcov_126d_base_v092_signal,
    f34dt_f34_debt_leverage_trajectory_rotationmag_126d_base_v093_signal,
    f34dt_f34_debt_leverage_trajectory_cushionvel_63d_base_v094_signal,
    f34dt_f34_debt_leverage_trajectory_servicez_252d_base_v095_signal,
    f34dt_f34_debt_leverage_trajectory_flowsignmag_base_v096_signal,
    f34dt_f34_debt_leverage_trajectory_netlevcurv_base_v097_signal,
    f34dt_f34_debt_leverage_trajectory_frontskewvel_126d_base_v098_signal,
    f34dt_f34_debt_leverage_trajectory_backskewvel_126d_base_v099_signal,
    f34dt_f34_debt_leverage_trajectory_levxslope_base_v100_signal,
    f34dt_f34_debt_leverage_trajectory_flowlumpshift_base_v101_signal,
    f34dt_f34_debt_leverage_trajectory_netscaledrank_252d_base_v102_signal,
    f34dt_f34_debt_leverage_trajectory_levreaccel_base_v103_signal,
    f34dt_f34_debt_leverage_trajectory_liqdrift_63d_base_v104_signal,
    f34dt_f34_debt_leverage_trajectory_structrace_504d_base_v105_signal,
    f34dt_f34_debt_leverage_trajectory_posturerank_base_v106_signal,
    f34dt_f34_debt_leverage_trajectory_levvolshift_base_v107_signal,
    f34dt_f34_debt_leverage_trajectory_netsmtrend_base_v108_signal,
    f34dt_f34_debt_leverage_trajectory_shortlev_base_v109_signal,
    f34dt_f34_debt_leverage_trajectory_flowstruct_504d_base_v110_signal,
    f34dt_f34_debt_leverage_trajectory_levtrajz_252d_base_v111_signal,
    f34dt_f34_debt_leverage_trajectory_cashdelev_252d_base_v112_signal,
    f34dt_f34_debt_leverage_trajectory_shortaccel_base_v113_signal,
    f34dt_f34_debt_leverage_trajectory_longaccel_base_v114_signal,
    f34dt_f34_debt_leverage_trajectory_netlevgap_base_v115_signal,
    f34dt_f34_debt_leverage_trajectory_flowmom_base_v116_signal,
    f34dt_f34_debt_leverage_trajectory_stressbuild_base_v117_signal,
    f34dt_f34_debt_leverage_trajectory_extdisp_base_v118_signal,
    f34dt_f34_debt_leverage_trajectory_fundmix_252d_base_v119_signal,
    f34dt_f34_debt_leverage_trajectory_shortmixema_base_v120_signal,
    f34dt_f34_debt_leverage_trajectory_levconv2_base_v121_signal,
    f34dt_f34_debt_leverage_trajectory_flowintz_63d_base_v122_signal,
    f34dt_f34_debt_leverage_trajectory_overborrowrank_base_v123_signal,
    f34dt_f34_debt_leverage_trajectory_netincrsign_base_v124_signal,
    f34dt_f34_debt_leverage_trajectory_shortcovrank_504d_base_v125_signal,
    f34dt_f34_debt_leverage_trajectory_rellevslope_base_v126_signal,
    f34dt_f34_debt_leverage_trajectory_cashsqueeze_base_v127_signal,
    f34dt_f34_debt_leverage_trajectory_frontfund_base_v128_signal,
    f34dt_f34_debt_leverage_trajectory_tailev_base_v129_signal,
    f34dt_f34_debt_leverage_trajectory_netchgaccel_base_v130_signal,
    f34dt_f34_debt_leverage_trajectory_buildvolshift_base_v131_signal,
    f34dt_f34_debt_leverage_trajectory_cushionema_base_v132_signal,
    f34dt_f34_debt_leverage_trajectory_shortcovvel_base_v133_signal,
    f34dt_f34_debt_leverage_trajectory_issuereversal_base_v134_signal,
    f34dt_f34_debt_leverage_trajectory_termbalance_base_v135_signal,
    f34dt_f34_debt_leverage_trajectory_netlevsmtraj_base_v136_signal,
    f34dt_f34_debt_leverage_trajectory_issueburst_base_v137_signal,
    f34dt_f34_debt_leverage_trajectory_compoundrisk_base_v138_signal,
    f34dt_f34_debt_leverage_trajectory_extvel_63d_base_v139_signal,
    f34dt_f34_debt_leverage_trajectory_cushiontrend_504d_base_v140_signal,
    f34dt_f34_debt_leverage_trajectory_flowconsist_base_v141_signal,
    f34dt_f34_debt_leverage_trajectory_relcurv_base_v142_signal,
    f34dt_f34_debt_leverage_trajectory_sltiltz_base_v143_signal,
    f34dt_f34_debt_leverage_trajectory_netext_base_v144_signal,
    f34dt_f34_debt_leverage_trajectory_flowdelevalign_base_v145_signal,
    f34dt_f34_debt_leverage_trajectory_fundrank_base_v146_signal,
    f34dt_f34_debt_leverage_trajectory_levtailtime_base_v147_signal,
    f34dt_f34_debt_leverage_trajectory_shortbuildcum_base_v148_signal,
    f34dt_f34_debt_leverage_trajectory_netlevconv_base_v149_signal,
    f34dt_f34_debt_leverage_trajectory_delevmom_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_DEBT_LEVERAGE_TRAJECTORY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    debt = _fund(101, base=2.0e8, drift=0.02, vol=0.06).rename("debt")
    debtc = _fund(102, base=6.0e7, drift=0.015, vol=0.08).rename("debtc")
    debtnc = _fund(103, base=1.4e8, drift=0.02, vol=0.06).rename("debtnc")
    cashneq = _fund(104, base=1.2e8, drift=0.01, vol=0.09).rename("cashneq")
    ebitda = _fund(105, base=8.0e7, drift=0.02, vol=0.10, allow_neg=True).rename("ebitda")
    ncfdebt = _fund(106, base=3.0e7, drift=0.0, vol=0.20, allow_neg=True).rename("ncfdebt")

    cols = {
        "debt": debt, "debtc": debtc, "debtnc": debtnc,
        "cashneq": cashneq, "ebitda": ebitda, "ncfdebt": ncfdebt,
    }

    ALLOW = {"debt", "debtc", "debtnc", "ncfdebt", "cashneq", "ebitda"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f34_debt_leverage_trajectory_base_076_150_claude: %d features pass" % n_features)
