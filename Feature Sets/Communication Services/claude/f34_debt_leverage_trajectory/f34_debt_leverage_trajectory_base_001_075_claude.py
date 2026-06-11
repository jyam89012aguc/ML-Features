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
    # net debt = gross debt minus cash (comm-services often net-cash)
    return debt - cashneq


def _f34_chg(s, w):
    # absolute change over w days
    return s - s.shift(w)


def _f34_logchg(s, w):
    # log-growth of a positive series over w days
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(w).replace(0, np.nan))


def _f34_debt_ebitda(debt, ebitda):
    # leverage coverage; ebitda can be negative -> guarded
    return debt / ebitda.replace(0, np.nan)


def _f34_shortmix(debtc, debt):
    # short-term debt as fraction of total debt
    return debtc / debt.replace(0, np.nan)


def _f34_longmix(debtnc, debt):
    return debtnc / debt.replace(0, np.nan)


def _f34_paydown_flow(ncfdebt, debt):
    # financing debt flow scaled by debt stock (issuance + / paydown -)
    return ncfdebt / debt.replace(0, np.nan)


def _f34_slope(s, w):
    # normalized rate-of-change slope per day
    return (s - s.shift(w)) / (float(w) * s.shift(w).abs().replace(0, np.nan))


# ============================================================
# gross-debt year-over-year log growth (debt build pace)
def f34dt_f34_debt_leverage_trajectory_debtgrow_252d_base_v001_signal(debt):
    b = _f34_logchg(debt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-debt half-year log growth
def f34dt_f34_debt_leverage_trajectory_debtgrow_126d_base_v002_signal(debt):
    b = _f34_logchg(debt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-debt quarterly log growth
def f34dt_f34_debt_leverage_trajectory_debtgrow_63d_base_v003_signal(debt):
    b = _f34_logchg(debt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt (debt - cash) year-over-year change scaled by debt stock
def f34dt_f34_debt_leverage_trajectory_netdebtchg_252d_base_v004_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq)
    b = _f34_chg(nd, 252) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt half-year change scaled by debt stock
def f34dt_f34_debt_leverage_trajectory_netdebtchg_126d_base_v005_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq)
    b = _f34_chg(nd, 126) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt / ebitda leverage level (coverage of net obligations)
def f34dt_f34_debt_leverage_trajectory_netdebtebitda_base_v006_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    b = nd / ebitda.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross debt/ebitda leverage level
def f34dt_f34_debt_leverage_trajectory_debtebitda_base_v007_signal(debt, ebitda):
    b = _f34_debt_ebitda(debt, ebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in debt/ebitda over a year (deleveraging / re-leveraging trajectory)
def f34dt_f34_debt_leverage_trajectory_levtraj_252d_base_v008_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _f34_chg(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in debt/ebitda over a half-year
def f34dt_f34_debt_leverage_trajectory_levtraj_126d_base_v009_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _f34_chg(lev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt mix (debtc / debt) level
def f34dt_f34_debt_leverage_trajectory_shortmix_base_v010_signal(debtc, debt):
    b = _f34_shortmix(debtc, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shift in short-term debt mix over a year (refinancing / maturity wall)
def f34dt_f34_debt_leverage_trajectory_shortmixchg_252d_base_v011_signal(debtc, debt):
    m = _f34_shortmix(debtc, debt)
    b = _f34_chg(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-vs-short debt skew: (debtnc - debtc) / debt (term-structure tilt)
def f34dt_f34_debt_leverage_trajectory_termskew_base_v012_signal(debtnc, debtc, debt):
    b = (debtnc - debtc) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt financing flow scaled by debt stock (issuance vs paydown)
def f34dt_f34_debt_leverage_trajectory_paydownflow_base_v013_signal(ncfdebt, debt):
    b = _f34_paydown_flow(ncfdebt, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing-year cumulative ncfdebt flow scaled by current debt (net financing intensity)
def f34dt_f34_debt_leverage_trajectory_flowintensity_252d_base_v014_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    b = cum / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt log-growth z-scored vs its own 252d history (de-trended build pace)
def f34dt_f34_debt_leverage_trajectory_debtgrowz_126d_base_v015_signal(debt):
    g = _f34_logchg(debt, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging slope: normalized rate-of-change of debt/ebitda
def f34dt_f34_debt_leverage_trajectory_delevslope_126d_base_v016_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _f34_slope(lev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt log-growth (using abs net debt magnitude) over a quarter
def f34dt_f34_debt_leverage_trajectory_netdebtmom_63d_base_v017_signal(debt, cashneq):
    nd = (debt - cashneq).abs()
    b = _f34_logchg(nd, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt buffer (cashneq / debt) level — net-cash cushion
def f34dt_f34_debt_leverage_trajectory_cashcover_base_v018_signal(cashneq, debt):
    b = cashneq / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt buffer momentum z-scored vs its own history (de-trended cushion drift)
def f34dt_f34_debt_leverage_trajectory_cashcoverchg_252d_base_v019_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    chg = _f34_chg(cov, 126)
    b = _z(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda percentile rank vs its own 504d history (leverage regime)
def f34dt_f34_debt_leverage_trajectory_levrank_504d_base_v020_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _rank(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-vs-debt race, percentile-ranked: short-horizon ebitda-led-debt regime
def f34dt_f34_debt_leverage_trajectory_ebitdaleddebt_252d_base_v021_signal(debt, ebitda):
    eg = _f34_logchg(ebitda.abs(), 63)
    dg = _f34_logchg(debt, 63)
    spread = eg - dg
    b = _rank(spread, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt flow proxy: change in debtc scaled by total debt
def f34dt_f34_debt_leverage_trajectory_shortdebtflow_126d_base_v022_signal(debtc, debt):
    b = _f34_chg(debtc, 126) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt flow proxy: change in debtnc scaled by total debt
def f34dt_f34_debt_leverage_trajectory_longdebtflow_126d_base_v023_signal(debtnc, debt):
    b = _f34_chg(debtnc, 126) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence of short vs long debt growth (refinancing rotation)
def f34dt_f34_debt_leverage_trajectory_termrotation_252d_base_v024_signal(debtc, debtnc):
    sg = _f34_logchg(debtc, 252)
    lg = _f34_logchg(debtnc, 252)
    b = sg - lg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow z-scored vs its own 252d history (financing surprise)
def f34dt_f34_debt_leverage_trajectory_flowz_252d_base_v025_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    b = _z(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# acceleration of debt build: quarterly growth minus prior quarterly growth
def f34dt_f34_debt_leverage_trajectory_debtaccel_63d_base_v026_signal(debt):
    g = _f34_logchg(debt, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt / ebitda change over a year (true coverage trajectory)
def f34dt_f34_debt_leverage_trajectory_netlevtraj_252d_base_v027_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = nd / ebitda.replace(0, np.nan)
    b = _f34_chg(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude of net-debt ACCELERATION (compressed direction of leverage inflection)
def f34dt_f34_debt_leverage_trajectory_netdebtsign_126d_base_v028_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    accel = nd - 2.0 * nd.shift(63) + nd.shift(126)
    b = np.sign(accel) * (accel.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build streak: fraction of last year debt growth exceeded its 252d median pace
def f34dt_f34_debt_leverage_trajectory_buildstreak_252d_base_v029_signal(debt):
    g = _f34_logchg(debt, 63)
    med = g.rolling(252, min_periods=126).median()
    up = (g > med).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# paydown streak: fraction of last year ncfdebt ran below its 252d median (net repayment lean)
def f34dt_f34_debt_leverage_trajectory_paydownstreak_252d_base_v030_signal(ncfdebt):
    med = ncfdebt.rolling(252, min_periods=126).median()
    down = (ncfdebt < med).astype(float)
    b = down.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-mix dispersion: rolling std of debtc/debt (maturity-structure instability)
def f34dt_f34_debt_leverage_trajectory_shortmixdisp_252d_base_v031_signal(debtc, debt):
    m = _f34_shortmix(debtc, debt)
    b = _std(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage volatility: rolling std of debt/ebitda (coverage instability)
def f34dt_f34_debt_leverage_trajectory_levvol_252d_base_v032_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _std(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pass-through ratio: reported yearly debt build relative to cumulative financing flow
def f34dt_f34_debt_leverage_trajectory_flowvsbuild_252d_base_v033_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    build = _f34_chg(debt, 252)
    b = np.tanh(build / cum.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth relative to its own slow EMA (build displacement)
def f34dt_f34_debt_leverage_trajectory_debtdisp_126d_base_v034_signal(debt):
    g = _f34_logchg(debt, 126)
    b = g - g.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: leverage level x debt build pace (levered-and-building risk)
def f34dt_f34_debt_leverage_trajectory_levbuild_base_v035_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    g = _f34_logchg(debt, 126)
    b = np.tanh(lev / 5.0) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change per unit of ebitda (incremental leverage demand)
def f34dt_f34_debt_leverage_trajectory_incrlev_126d_base_v036_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    b = _f34_chg(nd, 126) / ebitda.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash regime lean: fraction of last year net-debt/debt below its 252d median
def f34dt_f34_debt_leverage_trajectory_netcashtime_252d_base_v037_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    med = nd.rolling(252, min_periods=126).median()
    netcash = (nd < med).astype(float)
    b = netcash.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/ebitda smoothed (persistent leverage anchor)
def f34dt_f34_debt_leverage_trajectory_levema_base_v038_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = lev.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt coverage by cash (debtc / cashneq — refinancing risk)
def f34dt_f34_debt_leverage_trajectory_shorttocash_base_v039_signal(debtc, cashneq):
    b = debtc / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in short-term-debt-to-cash over a half-year (liquidity squeeze)
def f34dt_f34_debt_leverage_trajectory_shorttocashchg_126d_base_v040_signal(debtc, cashneq):
    r = debtc / cashneq.replace(0, np.nan)
    b = _f34_chg(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# does debt outrun cash? percentile-rank of the debt-vs-cash log-growth spread (regime)
def f34dt_f34_debt_leverage_trajectory_debtvscash_252d_base_v041_signal(debt, cashneq):
    dg = _f34_logchg(debt, 63)
    cg = _f34_logchg(cashneq, 63)
    spread = dg - cg
    b = _rank(spread, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow direction smoothed over a half-year (financing posture)
def f34dt_f34_debt_leverage_trajectory_flowposture_126d_base_v042_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    b = f.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage richness: percentile rank of debt/ebitda vs its own 252d history (regime)
def f34dt_f34_debt_leverage_trajectory_levgap_252d_base_v043_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _rank(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt mix change (debtnc/debt) over a year (terming-out)
def f34dt_f34_debt_leverage_trajectory_longmixchg_252d_base_v044_signal(debtnc, debt):
    m = _f34_longmix(debtnc, debt)
    b = _f34_chg(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth acceleration over half-year horizons
def f34dt_f34_debt_leverage_trajectory_debtaccel_126d_base_v045_signal(debt):
    g = _f34_logchg(debt, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt rank vs own 504d history (leverage extremity)
def f34dt_f34_debt_leverage_trajectory_netdebtrank_504d_base_v046_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq)
    scaled = nd / debt.replace(0, np.nan)
    b = _rank(scaled, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda coverage of short-term debt (ebitda / debtc — near-term serviceability)
def f34dt_f34_debt_leverage_trajectory_shortcover_base_v047_signal(ebitda, debtc):
    b = ebitda / debtc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trajectory of short-term coverage over a year
def f34dt_f34_debt_leverage_trajectory_shortcovertraj_252d_base_v048_signal(ebitda, debtc):
    cov = ebitda / debtc.replace(0, np.nan)
    b = _f34_chg(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow reversal: this-quarter flow minus prior-quarter flow
def f34dt_f34_debt_leverage_trajectory_flowreversal_63d_base_v049_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    fq = f.rolling(63, min_periods=21).mean()
    b = fq - fq.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# convex leverage stress: squared excess of debt/ebitda above its 252d median
def f34dt_f34_debt_leverage_trajectory_levstress_base_v050_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    med = lev.rolling(252, min_periods=126).median()
    excess = (lev - med).clip(lower=0)
    b = np.sign(lev) * (excess ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt deleveraging slope INFLECTION: recent 63d slope vs prior 63d slope (per-day)
def f34dt_f34_debt_leverage_trajectory_netdelevslope_126d_base_v051_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    slope_now = (nd - nd.shift(63)) / 63.0
    slope_prev = (nd.shift(63) - nd.shift(126)) / 63.0
    b = slope_now - slope_prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build pace minus cash build pace, gated by thin-cushion regime (burn-and-borrow)
def f34dt_f34_debt_leverage_trajectory_buildvscushion_126d_base_v052_signal(debt, cashneq):
    dg = _f34_logchg(debt, 126)
    cg = _f34_logchg(cashneq, 126)
    cov = cashneq / debt.replace(0, np.nan)
    thin = (1.0 - np.tanh(cov)).clip(lower=0)
    b = (dg - cg) * thin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-mix tanh-squashed momentum (bounded refinancing tilt change)
def f34dt_f34_debt_leverage_trajectory_shortmixtanh_126d_base_v053_signal(debtc, debt):
    m = _f34_shortmix(debtc, debt)
    chg = m - m.shift(126)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage z-score vs own long history (de-trended coverage regime)
def f34dt_f34_debt_leverage_trajectory_levz_504d_base_v054_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _z(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in financing-flow intensity
def f34dt_f34_debt_leverage_trajectory_flowintchg_252d_base_v055_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(126, min_periods=63).sum() / debt.replace(0, np.nan)
    b = _f34_chg(cum, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# structural debt extension: current debt vs its 1260d trailing mean (above/below trend stock)
def f34dt_f34_debt_leverage_trajectory_debtextend_1260d_base_v056_signal(debt):
    mn = _mean(debt, 1260)
    b = debt / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build dispersion: rolling std of quarterly debt growth
def f34dt_f34_debt_leverage_trajectory_buildvol_252d_base_v057_signal(debt):
    g = _f34_logchg(debt, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-financed deleveraging capacity: how many years cash could absorb current debt-flow run-rate
def f34dt_f34_debt_leverage_trajectory_cashpaydown_base_v058_signal(ncfdebt, cashneq):
    run = ncfdebt.rolling(63, min_periods=21).mean() * 4.0
    b = np.tanh(run / cashneq.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage acceleration: change in debt/ebitda slope over two quarters
def f34dt_f34_debt_leverage_trajectory_levaccel_126d_base_v059_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    s = lev - lev.shift(63)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-ebitda rank vs own 504d history (net leverage regime)
def f34dt_f34_debt_leverage_trajectory_netlevrank_504d_base_v060_signal(debt, cashneq, ebitda):
    nd = _f34_netdebt(debt, cashneq)
    lev = nd / ebitda.replace(0, np.nan)
    b = _rank(lev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# front-loaded build: debt build interacted with the SHIFT toward short-term debt mix
def f34dt_f34_debt_leverage_trajectory_frontbuild_126d_base_v061_signal(debtc, debt):
    m = _f34_shortmix(debtc, debt)
    m_shift = m - m.rolling(252, min_periods=126).mean()
    g = _f34_logchg(debt, 126)
    b = np.sign(m_shift) * g.abs() * m_shift.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-vs-stock reconciliation gap, z-scored (cum debt flow not matching debt build)
def f34dt_f34_debt_leverage_trajectory_reconcile_252d_base_v062_signal(ncfdebt, debt, cashneq):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    build = _f34_chg(debt, 252)
    gap = (cum - build) / cashneq.replace(0, np.nan)
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage breach intensity: mean positive excess above 504d median, z-scored (de-trended stress)
def f34dt_f34_debt_leverage_trajectory_breachcount_252d_base_v063_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    med = lev.rolling(504, min_periods=126).median()
    excess = (lev - med).clip(lower=0)
    intensity = excess.rolling(126, min_periods=63).mean()
    b = _z(intensity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# refinancing readiness regime: cash-to-short-debt coverage percentile-ranked vs history
def f34dt_f34_debt_leverage_trajectory_refireadiness_126d_base_v064_signal(cashneq, debtc):
    r = cashneq / debtc.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# re-leveraging rate: debt build pace divided by ebitda growth pace (build outrunning earnings)
def f34dt_f34_debt_leverage_trajectory_relevrate_126d_base_v065_signal(debt, ebitda):
    dg = _f34_logchg(debt, 126)
    eg = _f34_logchg(ebitda.abs(), 126)
    b = np.tanh(dg / eg.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt log-growth vs ebitda log-growth (leverage vs earnings race)
def f34dt_f34_debt_leverage_trajectory_netvsearn_252d_base_v066_signal(debt, cashneq, ebitda):
    nd = (debt - cashneq).abs()
    ndg = _f34_logchg(nd, 252)
    eg = _f34_logchg(ebitda.abs(), 252)
    b = ndg - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt growth z-scored vs own history (front-end issuance surprise)
def f34dt_f34_debt_leverage_trajectory_shortgrowz_252d_base_v067_signal(debtc):
    g = _f34_logchg(debtc, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt growth z-scored vs own history (back-end issuance surprise)
def f34dt_f34_debt_leverage_trajectory_longgrowz_252d_base_v068_signal(debtnc):
    g = _f34_logchg(debtnc, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage convergence: 63d leverage mean minus 252d leverage mean
def f34dt_f34_debt_leverage_trajectory_levconverge_base_v069_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = _mean(lev, 63) - _mean(lev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-flow dispersion (volatility of ncfdebt/debt — lumpy financing)
def f34dt_f34_debt_leverage_trajectory_flowdisp_252d_base_v070_signal(ncfdebt, debt):
    f = _f34_paydown_flow(ncfdebt, debt)
    b = _std(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change smoothed then differenced (clean deleveraging signal)
def f34dt_f34_debt_leverage_trajectory_netdelevsm_126d_base_v071_signal(debt, cashneq):
    nd = _f34_netdebt(debt, cashneq) / debt.replace(0, np.nan)
    sm = nd.ewm(span=63, min_periods=21).mean()
    b = sm - sm.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity-burden index: term-weighted debt relative to total, z-scored (front-loading regime)
def f34dt_f34_debt_leverage_trajectory_covcushion_base_v072_signal(debtc, debtnc, debt):
    weighted = 2.0 * debtc + debtnc
    burden = weighted / debt.replace(0, np.nan)
    b = _z(burden, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage curvature: second-difference of debt/ebitda over yearly spans
def f34dt_f34_debt_leverage_trajectory_levcurv_252d_base_v073_signal(debt, ebitda):
    lev = _f34_debt_ebitda(debt, ebitda)
    b = lev - 2.0 * lev.shift(126) + lev.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing intensity vs leverage (issuing into high leverage = stress)
def f34dt_f34_debt_leverage_trajectory_issueintolev_base_v074_signal(ncfdebt, debt, ebitda):
    f = _f34_paydown_flow(ncfdebt, debt)
    lev = _f34_debt_ebitda(debt, ebitda)
    b = f * np.tanh(lev / 4.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite deleveraging quality: paydown streak weighted by coverage improvement
def f34dt_f34_debt_leverage_trajectory_delevquality_252d_base_v075_signal(ncfdebt, debt, ebitda):
    med = ncfdebt.rolling(252, min_periods=126).median()
    paydown = (ncfdebt < med).astype(float).rolling(126, min_periods=63).mean()
    lev = _f34_debt_ebitda(debt, ebitda)
    improve = -(lev - lev.shift(252))
    b = paydown * np.tanh(improve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f34dt_f34_debt_leverage_trajectory_debtgrow_252d_base_v001_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_126d_base_v002_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrow_63d_base_v003_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtchg_252d_base_v004_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtchg_126d_base_v005_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtebitda_base_v006_signal,
    f34dt_f34_debt_leverage_trajectory_debtebitda_base_v007_signal,
    f34dt_f34_debt_leverage_trajectory_levtraj_252d_base_v008_signal,
    f34dt_f34_debt_leverage_trajectory_levtraj_126d_base_v009_signal,
    f34dt_f34_debt_leverage_trajectory_shortmix_base_v010_signal,
    f34dt_f34_debt_leverage_trajectory_shortmixchg_252d_base_v011_signal,
    f34dt_f34_debt_leverage_trajectory_termskew_base_v012_signal,
    f34dt_f34_debt_leverage_trajectory_paydownflow_base_v013_signal,
    f34dt_f34_debt_leverage_trajectory_flowintensity_252d_base_v014_signal,
    f34dt_f34_debt_leverage_trajectory_debtgrowz_126d_base_v015_signal,
    f34dt_f34_debt_leverage_trajectory_delevslope_126d_base_v016_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtmom_63d_base_v017_signal,
    f34dt_f34_debt_leverage_trajectory_cashcover_base_v018_signal,
    f34dt_f34_debt_leverage_trajectory_cashcoverchg_252d_base_v019_signal,
    f34dt_f34_debt_leverage_trajectory_levrank_504d_base_v020_signal,
    f34dt_f34_debt_leverage_trajectory_ebitdaleddebt_252d_base_v021_signal,
    f34dt_f34_debt_leverage_trajectory_shortdebtflow_126d_base_v022_signal,
    f34dt_f34_debt_leverage_trajectory_longdebtflow_126d_base_v023_signal,
    f34dt_f34_debt_leverage_trajectory_termrotation_252d_base_v024_signal,
    f34dt_f34_debt_leverage_trajectory_flowz_252d_base_v025_signal,
    f34dt_f34_debt_leverage_trajectory_debtaccel_63d_base_v026_signal,
    f34dt_f34_debt_leverage_trajectory_netlevtraj_252d_base_v027_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtsign_126d_base_v028_signal,
    f34dt_f34_debt_leverage_trajectory_buildstreak_252d_base_v029_signal,
    f34dt_f34_debt_leverage_trajectory_paydownstreak_252d_base_v030_signal,
    f34dt_f34_debt_leverage_trajectory_shortmixdisp_252d_base_v031_signal,
    f34dt_f34_debt_leverage_trajectory_levvol_252d_base_v032_signal,
    f34dt_f34_debt_leverage_trajectory_flowvsbuild_252d_base_v033_signal,
    f34dt_f34_debt_leverage_trajectory_debtdisp_126d_base_v034_signal,
    f34dt_f34_debt_leverage_trajectory_levbuild_base_v035_signal,
    f34dt_f34_debt_leverage_trajectory_incrlev_126d_base_v036_signal,
    f34dt_f34_debt_leverage_trajectory_netcashtime_252d_base_v037_signal,
    f34dt_f34_debt_leverage_trajectory_levema_base_v038_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocash_base_v039_signal,
    f34dt_f34_debt_leverage_trajectory_shorttocashchg_126d_base_v040_signal,
    f34dt_f34_debt_leverage_trajectory_debtvscash_252d_base_v041_signal,
    f34dt_f34_debt_leverage_trajectory_flowposture_126d_base_v042_signal,
    f34dt_f34_debt_leverage_trajectory_levgap_252d_base_v043_signal,
    f34dt_f34_debt_leverage_trajectory_longmixchg_252d_base_v044_signal,
    f34dt_f34_debt_leverage_trajectory_debtaccel_126d_base_v045_signal,
    f34dt_f34_debt_leverage_trajectory_netdebtrank_504d_base_v046_signal,
    f34dt_f34_debt_leverage_trajectory_shortcover_base_v047_signal,
    f34dt_f34_debt_leverage_trajectory_shortcovertraj_252d_base_v048_signal,
    f34dt_f34_debt_leverage_trajectory_flowreversal_63d_base_v049_signal,
    f34dt_f34_debt_leverage_trajectory_levstress_base_v050_signal,
    f34dt_f34_debt_leverage_trajectory_netdelevslope_126d_base_v051_signal,
    f34dt_f34_debt_leverage_trajectory_buildvscushion_126d_base_v052_signal,
    f34dt_f34_debt_leverage_trajectory_shortmixtanh_126d_base_v053_signal,
    f34dt_f34_debt_leverage_trajectory_levz_504d_base_v054_signal,
    f34dt_f34_debt_leverage_trajectory_flowintchg_252d_base_v055_signal,
    f34dt_f34_debt_leverage_trajectory_debtextend_1260d_base_v056_signal,
    f34dt_f34_debt_leverage_trajectory_buildvol_252d_base_v057_signal,
    f34dt_f34_debt_leverage_trajectory_cashpaydown_base_v058_signal,
    f34dt_f34_debt_leverage_trajectory_levaccel_126d_base_v059_signal,
    f34dt_f34_debt_leverage_trajectory_netlevrank_504d_base_v060_signal,
    f34dt_f34_debt_leverage_trajectory_frontbuild_126d_base_v061_signal,
    f34dt_f34_debt_leverage_trajectory_reconcile_252d_base_v062_signal,
    f34dt_f34_debt_leverage_trajectory_breachcount_252d_base_v063_signal,
    f34dt_f34_debt_leverage_trajectory_refireadiness_126d_base_v064_signal,
    f34dt_f34_debt_leverage_trajectory_relevrate_126d_base_v065_signal,
    f34dt_f34_debt_leverage_trajectory_netvsearn_252d_base_v066_signal,
    f34dt_f34_debt_leverage_trajectory_shortgrowz_252d_base_v067_signal,
    f34dt_f34_debt_leverage_trajectory_longgrowz_252d_base_v068_signal,
    f34dt_f34_debt_leverage_trajectory_levconverge_base_v069_signal,
    f34dt_f34_debt_leverage_trajectory_flowdisp_252d_base_v070_signal,
    f34dt_f34_debt_leverage_trajectory_netdelevsm_126d_base_v071_signal,
    f34dt_f34_debt_leverage_trajectory_covcushion_base_v072_signal,
    f34dt_f34_debt_leverage_trajectory_levcurv_252d_base_v073_signal,
    f34dt_f34_debt_leverage_trajectory_issueintolev_base_v074_signal,
    f34dt_f34_debt_leverage_trajectory_delevquality_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F34_DEBT_LEVERAGE_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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

    print("OK f34_debt_leverage_trajectory_base_001_075_claude: %d features pass" % n_features)
