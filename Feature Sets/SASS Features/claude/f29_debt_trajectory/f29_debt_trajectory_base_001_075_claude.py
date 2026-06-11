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


# ===== folder domain primitives (debt trajectory) =====
def _f29_growth(d, w):
    # log growth of a debt level over window w
    return np.log(d.replace(0, np.nan) / d.shift(w).replace(0, np.nan))


def _f29_pctchg(d, w):
    return d / d.shift(w).replace(0, np.nan) - 1.0


def _f29_netdebt(debt, cashneq):
    return debt - cashneq


def _f29_delever_slope(d, w):
    # OLS slope of log-debt vs time over window w (deleveraging = negative)
    ld = np.log(d.replace(0, np.nan))
    n = w
    idx = np.arange(n)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.any(~np.isfinite(a)):
            return np.nan
        ym = a.mean()
        return float(((idx - xm) * (a - ym)).sum() / xden)

    return ld.rolling(n, min_periods=n).apply(_f, raw=True)


def _f29_paydown_streak(d):
    # consecutive-quarter (63d) debt-decline streak length, normalized
    dec = (d < d.shift(63)).astype(float)
    grp = (dec != dec.shift(1)).cumsum()
    streak = dec.groupby(grp).cumcount() + 1
    return (streak * dec) / 63.0


def _f29_build_streak(d):
    inc = (d > d.shift(63)).astype(float)
    grp = (inc != inc.shift(1)).cumsum()
    streak = inc.groupby(grp).cumcount() + 1
    return (streak * inc) / 63.0


def _f29_st_share(debtc, debt):
    return debtc / debt.replace(0, np.nan)


def _f29_lt_share(debtnc, debt):
    return debtnc / debt.replace(0, np.nan)


# ============================================================
# debt log-growth over a quarter
def f29dt_f29_debt_trajectory_dgrow_63d_base_v001_signal(debt):
    b = _f29_growth(debt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt log-growth over a half-year
def f29dt_f29_debt_trajectory_dgrow_126d_base_v002_signal(debt):
    b = _f29_growth(debt, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt log-growth over a year
def f29dt_f29_debt_trajectory_dgrow_252d_base_v003_signal(debt):
    b = _f29_growth(debt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt log-growth over two years
def f29dt_f29_debt_trajectory_dgrow_504d_base_v004_signal(debt):
    b = _f29_growth(debt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-debt year growth, z-scored vs its own 252d history (de-trended)
def f29dt_f29_debt_trajectory_dusdgrowz_252d_base_v005_signal(debtusd):
    g = _f29_growth(debtusd, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-debt quarter growth, percentile-ranked vs its own 504d history
def f29dt_f29_debt_trajectory_dusdgrowrank_63d_base_v006_signal(debtusd):
    g = _f29_growth(debtusd, 63)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt (debt - cash) log-level change over a year
def f29dt_f29_debt_trajectory_ndgrow_252d_base_v007_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    b = np.log(nd.clip(lower=1.0)) - np.log(nd.shift(252).clip(lower=1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change over a quarter, scaled by gross debt (net leverage delta)
def f29dt_f29_debt_trajectory_ndchg_63d_base_v008_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    b = (nd - nd.shift(63)) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change over a half-year, scaled by gross debt
def f29dt_f29_debt_trajectory_ndchg_126d_base_v009_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    b = (nd - nd.shift(126)) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt: cash/debt level, z-scored vs own 252d history
def f29dt_f29_debt_trajectory_cashcovz_252d_base_v010_signal(debt, cashneq):
    cov = cashneq / debt.replace(0, np.nan)
    b = _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging slope (OLS slope of log-debt) over a year
def f29dt_f29_debt_trajectory_delslope_252d_base_v011_signal(debt):
    b = _f29_delever_slope(debt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging slope residual: 126d slope minus its own 126d average (slope surprise)
def f29dt_f29_debt_trajectory_delslopedev_126d_base_v012_signal(debt):
    sl = _f29_delever_slope(debt, 126)
    b = sl - _mean(sl, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-path curvature: 2nd difference of log-debt (convex build vs concave paydown)
def f29dt_f29_debt_trajectory_dcurv_63d_base_v013_signal(debt):
    ld = np.log(debt.replace(0, np.nan))
    b = (ld - 2.0 * ld.shift(63) + ld.shift(126)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow (net debt-issuance cash flow), smoothed over a quarter
def f29dt_f29_debt_trajectory_ncfflow_63d_base_v014_signal(ncfdebt):
    b = _mean(ncfdebt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow scaled by debt level (issuance/paydown intensity)
def f29dt_f29_debt_trajectory_ncfintens_126d_base_v015_signal(ncfdebt, debt):
    intens = ncfdebt / debt.replace(0, np.nan)
    b = _mean(intens, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow z-scored vs its own 252d history (abnormal issuance)
def f29dt_f29_debt_trajectory_ncfz_252d_base_v016_signal(ncfdebt):
    b = _z(ncfdebt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative ncfdebt flow over a year, scaled by debt (net new debt funded)
def f29dt_f29_debt_trajectory_ncfcum_252d_base_v017_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(252, min_periods=126).sum()
    b = cum / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share (debtc/debt) level
def f29dt_f29_debt_trajectory_stshare_base_v018_signal(debtc, debt):
    b = _f29_st_share(debtc, debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share change over a year (maturity shift toward short)
def f29dt_f29_debt_trajectory_stsharechg_252d_base_v019_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    b = sh - sh.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long debt spread: (debtc - debtnc)/debt level
def f29dt_f29_debt_trajectory_stltspr_base_v020_signal(debtc, debtnc, debt):
    b = (debtc - debtnc) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long debt spread change over a half-year (refinancing tilt)
def f29dt_f29_debt_trajectory_stltsprchg_126d_base_v021_signal(debtc, debtnc, debt):
    spr = (debtc - debtnc) / debt.replace(0, np.nan)
    b = spr - spr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth differential: short-term debt grows faster than long-term (maturity wall risk)
def f29dt_f29_debt_trajectory_stltgrowdiff_252d_base_v022_signal(debtc, debtnc):
    gc = _f29_growth(debtc, 252)
    gnc = _f29_growth(debtnc, 252)
    b = gc - gnc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown streak length (consecutive quarters of decline)
def f29dt_f29_debt_trajectory_paydown_streak_base_v023_signal(debt):
    b = _f29_paydown_streak(debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-build streak length (consecutive quarters of increase)
def f29dt_f29_debt_trajectory_build_streak_base_v024_signal(debt):
    b = _f29_build_streak(debt)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net paydown-vs-build streak balance (signed persistence)
def f29dt_f29_debt_trajectory_streakbal_base_v025_signal(debt):
    pay = _f29_paydown_streak(debt)
    bld = _f29_build_streak(debt)
    b = pay - bld
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with falling debt (deleveraging hit-rate)
def f29dt_f29_debt_trajectory_payhitrate_252d_base_v026_signal(debt):
    dec = (debt < debt.shift(21)).astype(float)
    b = dec.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt acceleration: quarter growth now minus quarter growth a quarter ago
def f29dt_f29_debt_trajectory_daccel_63d_base_v027_signal(debt):
    g = _f29_growth(debt, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth stability: std of monthly debt growth over a year (erratic financing)
def f29dt_f29_debt_trajectory_dgrowstd_252d_base_v028_signal(debt):
    g = _f29_growth(debt, 21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth vs its own trend: current year-growth minus 2y-avg of year-growth
def f29dt_f29_debt_trajectory_dgrowdev_252d_base_v029_signal(debt):
    g = _f29_growth(debt, 252)
    b = g - _mean(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-cash dependence: how much of net debt is uncovered by cash, ranked
def f29dt_f29_debt_trajectory_ndcoverrank_252d_base_v030_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    ratio = nd / debt.replace(0, np.nan)
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash build vs debt build: cash growth minus debt growth over a year (balance improving)
def f29dt_f29_debt_trajectory_cashvsdebt_252d_base_v031_signal(debt, cashneq):
    gd = _f29_growth(debt, 252)
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(252).clip(lower=1.0))
    b = gc - gd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt level relative to its trailing 504d max (paydown from peak debt)
def f29dt_f29_debt_trajectory_peakpaydown_504d_base_v032_signal(debt):
    pk = _rmax(debt, 504)
    b = debt / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt level relative to its trailing 504d min (build above the trough)
def f29dt_f29_debt_trajectory_troughbuild_504d_base_v033_signal(debt):
    tr = _rmin(debt, 504)
    b = debt / tr.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt position within its 252d range (where in the debt cycle)
def f29dt_f29_debt_trajectory_debtrangepos_252d_base_v034_signal(debt):
    hi = _rmax(debt, 252)
    lo = _rmin(debt, 252)
    b = (debt - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt sign persistence: fraction of last year with net issuance (positive flow)
def f29dt_f29_debt_trajectory_ncfissrate_252d_base_v035_signal(ncfdebt):
    iss = (ncfdebt > 0).astype(float)
    b = iss.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt momentum: change in smoothed flow over a quarter (financing turn)
def f29dt_f29_debt_trajectory_ncfmom_63d_base_v036_signal(ncfdebt):
    sm = _mean(ncfdebt, 63)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt vs debt-change reconciliation (flow-implied vs observed delta)
def f29dt_f29_debt_trajectory_flowrecon_63d_base_v037_signal(ncfdebt, debt):
    flow = ncfdebt.rolling(63, min_periods=21).sum()
    delta = debt - debt.shift(63)
    b = (flow - delta) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-vs-reported debt divergence (currency/translation drift), z-scored
def f29dt_f29_debt_trajectory_usddiverg_252d_base_v038_signal(debt, debtusd):
    g1 = _f29_growth(debt, 252)
    g2 = _f29_growth(debtusd, 252)
    b = _z(g1 - g2, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year debt percent-change, smoothed by EMA (persistent financing trend)
def f29dt_f29_debt_trajectory_dpctema_126d_base_v039_signal(debt):
    p = _f29_pctchg(debt, 126)
    b = p.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt trajectory slope (OLS slope of net debt vs time) over a year
def f29dt_f29_debt_trajectory_ndslope_252d_base_v040_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    nds = nd / nd.rolling(252, min_periods=126).mean().replace(0, np.nan)
    n = 252
    idx = np.arange(n)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.any(~np.isfinite(a)):
            return np.nan
        ym = a.mean()
        return float(((idx - xm) * (a - ym)).sum() / xden)

    b = nds.rolling(n, min_periods=n).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt share trend (term-out toward long maturities)
def f29dt_f29_debt_trajectory_ltsharechg_252d_base_v041_signal(debtnc, debt):
    sh = _f29_lt_share(debtnc, debt)
    b = sh - sh.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-coverage cushion: (cash - short-term debt)/debt level (refinancing buffer)
def f29dt_f29_debt_trajectory_stcushion_base_v042_signal(cashneq, debtc, debt):
    b = (cashneq - debtc) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt growth z-scored (near-term funding pressure)
def f29dt_f29_debt_trajectory_stgrowz_252d_base_v043_signal(debtc):
    g = _f29_growth(debtc, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term-debt growth, percentile-ranked (capital-structure lengthening)
def f29dt_f29_debt_trajectory_ltgrowrank_252d_base_v044_signal(debtnc):
    g = _f29_growth(debtnc, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-build intensity x sign of net flow (issuance-confirmed build)
def f29dt_f29_debt_trajectory_buildconfirm_252d_base_v045_signal(debt, ncfdebt):
    g = _f29_growth(debt, 252)
    flowsign = np.sign(_mean(ncfdebt, 126))
    b = g * flowsign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging quality: net repayment flow weighted by cash-coverage change
def f29dt_f29_debt_trajectory_cleandelev_base_v046_signal(debt, cashneq, ncfdebt):
    repay = (-ncfdebt).rolling(63, min_periods=21).mean() / debt.replace(0, np.nan)
    cov = cashneq / debt.replace(0, np.nan)
    dcov = cov - cov.shift(126)
    b = repay * np.tanh(5.0 * dcov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt range position over two years (net leverage cycle)
def f29dt_f29_debt_trajectory_ndrangepos_504d_base_v047_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    hi = _rmax(nd, 504)
    lo = _rmin(nd, 504)
    b = (nd - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance-shift dispersion: rolling std of (monthly debt-growth minus cash-growth)
def f29dt_f29_debt_trajectory_balsignmag_252d_base_v048_signal(debt, cashneq):
    gd = _f29_growth(debt, 21)
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(21).clip(lower=1.0))
    b = _std(gd - gc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt dispersion: rolling std of debt flow (lumpy vs smooth financing)
def f29dt_f29_debt_trajectory_ncfdisp_252d_base_v049_signal(ncfdebt):
    b = _std(ncfdebt, 252) / _mean(ncfdebt.abs(), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-change acceleration: quarter net-debt change now vs a quarter ago
def f29dt_f29_debt_trajectory_ndaccel_63d_base_v050_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    chg = (nd - nd.shift(63)) / debt.replace(0, np.nan)
    b = chg - chg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth acceleration over a year (year-growth now vs year-growth a year ago)
def f29dt_f29_debt_trajectory_dgrowyoy_252d_base_v051_signal(debt):
    g = _f29_growth(debt, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash drawdown to repay: how far cash has fallen while debt held (liquidity stress)
def f29dt_f29_debt_trajectory_cashdrawdebt_252d_base_v052_signal(cashneq, debt):
    cpk = _rmax(cashneq, 252)
    cdd = cashneq / cpk.replace(0, np.nan) - 1.0
    dchg = _f29_pctchg(debt, 252)
    b = cdd - dchg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd level momentum, smoothed and de-meaned (absolute debt-load trajectory)
def f29dt_f29_debt_trajectory_dusdmom_126d_base_v053_signal(debtusd):
    p = _f29_pctchg(debtusd, 126)
    b = p - _mean(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt-to-cash ratio change (rollover risk delta)
def f29dt_f29_debt_trajectory_stcashratiochg_126d_base_v054_signal(debtc, cashneq):
    r = debtc / cashneq.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown depth: cumulative log reduction during current decline streak
def f29dt_f29_debt_trajectory_paydepth_252d_base_v055_signal(debt):
    g = _f29_growth(debt, 63)
    neg = g.clip(upper=0.0)
    b = neg.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-build depth: cumulative log increase over a year (financing buildup)
def f29dt_f29_debt_trajectory_builddepth_252d_base_v056_signal(debt):
    g = _f29_growth(debt, 63)
    pos = g.clip(lower=0.0)
    b = pos.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing whipsaw: count of debt-direction flips over a year (erratic financing)
def f29dt_f29_debt_trajectory_whipsaw_252d_base_v057_signal(debt):
    g = _f29_growth(debt, 21)
    flip = (np.sign(g) != np.sign(g.shift(21))).astype(float)
    b = flip.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-net-debt ratio momentum (deleveraging via liquidity)
def f29dt_f29_debt_trajectory_cashtondmom_252d_base_v058_signal(cashneq, debt):
    nd = (debt - cashneq).clip(lower=1.0)
    r = cashneq / nd
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt cumulative paydown intensity (net repayments over a year)
def f29dt_f29_debt_trajectory_ncfpaydown_252d_base_v059_signal(ncfdebt, debt):
    repay = (-ncfdebt.clip(upper=0.0)).rolling(252, min_periods=126).sum()
    b = repay / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt cumulative issuance intensity (net new borrowing over a year)
def f29dt_f29_debt_trajectory_ncfissue_252d_base_v060_signal(ncfdebt, debt):
    issue = ncfdebt.clip(lower=0.0).rolling(252, min_periods=126).sum()
    b = issue / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-load extension: how far debt sits above its 252d mean (over-levered vs trend)
def f29dt_f29_debt_trajectory_debtextend_252d_base_v061_signal(debt):
    mn = _mean(debt, 252)
    b = (debt - mn) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share dispersion across 63/252 windows (maturity volatility)
def f29dt_f29_debt_trajectory_stsharevol_252d_base_v062_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    b = _std(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt-to-cash rollover-coverage level, z-scored vs 252d history
def f29dt_f29_debt_trajectory_strollcov_252d_base_v063_signal(debtc, cashneq):
    r = debtc / cashneq.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build confirmed by rising short-term share (build that worsens maturity profile)
def f29dt_f29_debt_trajectory_riskybuild_252d_base_v064_signal(debt, debtc):
    gd = _f29_growth(debt, 252)
    sh = _f29_st_share(debtc, debt)
    dsh = sh - sh.shift(126)
    b = np.sign(gd) * dsh.abs() + dsh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow per unit of debt volatility (risk-adjusted financing)
def f29dt_f29_debt_trajectory_ncfriskadj_252d_base_v065_signal(ncfdebt, debt):
    sm = _mean(ncfdebt, 126)
    vol = _std(_f29_growth(debt, 21), 252)
    b = sm / (debt * vol).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging consistency: fraction of quarters with negative ncfdebt over 2y
def f29dt_f29_debt_trajectory_delconsist_504d_base_v066_signal(ncfdebt):
    repay = (ncfdebt < 0).astype(float)
    b = repay.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-quarter-growth rank within long history (cross-time financing extremity)
def f29dt_f29_debt_trajectory_dgrowrank_63d_base_v067_signal(debt):
    g = _f29_growth(debt, 63)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage improvement slope (OLS slope of cash/debt over a year)
def f29dt_f29_debt_trajectory_covslope_252d_base_v068_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    n = 252
    idx = np.arange(n)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.any(~np.isfinite(a)):
            return np.nan
        ym = a.mean()
        return float(((idx - xm) * (a - ym)).sum() / xden)

    b = cov.rolling(n, min_periods=n).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-vs-long growth spread, EMA-smoothed (persistent maturity migration)
def f29dt_f29_debt_trajectory_stltspread_ema_base_v069_signal(debtc, debtnc):
    gc = _f29_growth(debtc, 126)
    gnc = _f29_growth(debtnc, 126)
    b = (gc - gnc).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-debtusd ratio (leverage net of cash on USD base), de-trended
def f29dt_f29_debt_trajectory_ndusd_dev_252d_base_v070_signal(debt, cashneq, debtusd):
    nd = debt - cashneq
    r = nd / debtusd.replace(0, np.nan)
    b = r - _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown momentum confirmed by cash growth (self-funded deleveraging)
def f29dt_f29_debt_trajectory_selffunddelev_252d_base_v071_signal(debt, cashneq):
    dpay = -_f29_growth(debt, 252)
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(252).clip(lower=1.0))
    b = dpay * np.tanh(2.0 * gc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in short-term debt share growth (acceleration of rollover)
def f29dt_f29_debt_trajectory_stshareaccel_252d_base_v072_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    chg = sh - sh.shift(126)
    b = chg - chg.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fragile build: debt build over a year scaled by rising short-term-debt growth
def f29dt_f29_debt_trajectory_fragilebuild_504d_base_v073_signal(debt, debtc):
    gd = _f29_growth(debt, 252)
    gc = _f29_growth(debtc, 252)
    b = gd.clip(lower=0.0) * np.tanh(2.0 * gc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change rank over a half-year (cross-time net leverage shift)
def f29dt_f29_debt_trajectory_ndchgrank_126d_base_v074_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    chg = (nd - nd.shift(126)) / debt.replace(0, np.nan)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite deleveraging score: paydown hit-rate combined with repayment-flow rank
def f29dt_f29_debt_trajectory_delevscore_252d_base_v075_signal(debt, ncfdebt):
    dec = (debt < debt.shift(21)).astype(float)
    hitrate = dec.rolling(252, min_periods=126).mean() - 0.5
    repayflow = (-ncfdebt).rolling(126, min_periods=63).mean()
    b = hitrate + 0.5 * _rank(repayflow, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29dt_f29_debt_trajectory_dgrow_63d_base_v001_signal,
    f29dt_f29_debt_trajectory_dgrow_126d_base_v002_signal,
    f29dt_f29_debt_trajectory_dgrow_252d_base_v003_signal,
    f29dt_f29_debt_trajectory_dgrow_504d_base_v004_signal,
    f29dt_f29_debt_trajectory_dusdgrowz_252d_base_v005_signal,
    f29dt_f29_debt_trajectory_dusdgrowrank_63d_base_v006_signal,
    f29dt_f29_debt_trajectory_ndgrow_252d_base_v007_signal,
    f29dt_f29_debt_trajectory_ndchg_63d_base_v008_signal,
    f29dt_f29_debt_trajectory_ndchg_126d_base_v009_signal,
    f29dt_f29_debt_trajectory_cashcovz_252d_base_v010_signal,
    f29dt_f29_debt_trajectory_delslope_252d_base_v011_signal,
    f29dt_f29_debt_trajectory_delslopedev_126d_base_v012_signal,
    f29dt_f29_debt_trajectory_dcurv_63d_base_v013_signal,
    f29dt_f29_debt_trajectory_ncfflow_63d_base_v014_signal,
    f29dt_f29_debt_trajectory_ncfintens_126d_base_v015_signal,
    f29dt_f29_debt_trajectory_ncfz_252d_base_v016_signal,
    f29dt_f29_debt_trajectory_ncfcum_252d_base_v017_signal,
    f29dt_f29_debt_trajectory_stshare_base_v018_signal,
    f29dt_f29_debt_trajectory_stsharechg_252d_base_v019_signal,
    f29dt_f29_debt_trajectory_stltspr_base_v020_signal,
    f29dt_f29_debt_trajectory_stltsprchg_126d_base_v021_signal,
    f29dt_f29_debt_trajectory_stltgrowdiff_252d_base_v022_signal,
    f29dt_f29_debt_trajectory_paydown_streak_base_v023_signal,
    f29dt_f29_debt_trajectory_build_streak_base_v024_signal,
    f29dt_f29_debt_trajectory_streakbal_base_v025_signal,
    f29dt_f29_debt_trajectory_payhitrate_252d_base_v026_signal,
    f29dt_f29_debt_trajectory_daccel_63d_base_v027_signal,
    f29dt_f29_debt_trajectory_dgrowstd_252d_base_v028_signal,
    f29dt_f29_debt_trajectory_dgrowdev_252d_base_v029_signal,
    f29dt_f29_debt_trajectory_ndcoverrank_252d_base_v030_signal,
    f29dt_f29_debt_trajectory_cashvsdebt_252d_base_v031_signal,
    f29dt_f29_debt_trajectory_peakpaydown_504d_base_v032_signal,
    f29dt_f29_debt_trajectory_troughbuild_504d_base_v033_signal,
    f29dt_f29_debt_trajectory_debtrangepos_252d_base_v034_signal,
    f29dt_f29_debt_trajectory_ncfissrate_252d_base_v035_signal,
    f29dt_f29_debt_trajectory_ncfmom_63d_base_v036_signal,
    f29dt_f29_debt_trajectory_flowrecon_63d_base_v037_signal,
    f29dt_f29_debt_trajectory_usddiverg_252d_base_v038_signal,
    f29dt_f29_debt_trajectory_dpctema_126d_base_v039_signal,
    f29dt_f29_debt_trajectory_ndslope_252d_base_v040_signal,
    f29dt_f29_debt_trajectory_ltsharechg_252d_base_v041_signal,
    f29dt_f29_debt_trajectory_stcushion_base_v042_signal,
    f29dt_f29_debt_trajectory_stgrowz_252d_base_v043_signal,
    f29dt_f29_debt_trajectory_ltgrowrank_252d_base_v044_signal,
    f29dt_f29_debt_trajectory_buildconfirm_252d_base_v045_signal,
    f29dt_f29_debt_trajectory_cleandelev_base_v046_signal,
    f29dt_f29_debt_trajectory_ndrangepos_504d_base_v047_signal,
    f29dt_f29_debt_trajectory_balsignmag_252d_base_v048_signal,
    f29dt_f29_debt_trajectory_ncfdisp_252d_base_v049_signal,
    f29dt_f29_debt_trajectory_ndaccel_63d_base_v050_signal,
    f29dt_f29_debt_trajectory_dgrowyoy_252d_base_v051_signal,
    f29dt_f29_debt_trajectory_cashdrawdebt_252d_base_v052_signal,
    f29dt_f29_debt_trajectory_dusdmom_126d_base_v053_signal,
    f29dt_f29_debt_trajectory_stcashratiochg_126d_base_v054_signal,
    f29dt_f29_debt_trajectory_paydepth_252d_base_v055_signal,
    f29dt_f29_debt_trajectory_builddepth_252d_base_v056_signal,
    f29dt_f29_debt_trajectory_whipsaw_252d_base_v057_signal,
    f29dt_f29_debt_trajectory_cashtondmom_252d_base_v058_signal,
    f29dt_f29_debt_trajectory_ncfpaydown_252d_base_v059_signal,
    f29dt_f29_debt_trajectory_ncfissue_252d_base_v060_signal,
    f29dt_f29_debt_trajectory_debtextend_252d_base_v061_signal,
    f29dt_f29_debt_trajectory_stsharevol_252d_base_v062_signal,
    f29dt_f29_debt_trajectory_strollcov_252d_base_v063_signal,
    f29dt_f29_debt_trajectory_riskybuild_252d_base_v064_signal,
    f29dt_f29_debt_trajectory_ncfriskadj_252d_base_v065_signal,
    f29dt_f29_debt_trajectory_delconsist_504d_base_v066_signal,
    f29dt_f29_debt_trajectory_dgrowrank_63d_base_v067_signal,
    f29dt_f29_debt_trajectory_covslope_252d_base_v068_signal,
    f29dt_f29_debt_trajectory_stltspread_ema_base_v069_signal,
    f29dt_f29_debt_trajectory_ndusd_dev_252d_base_v070_signal,
    f29dt_f29_debt_trajectory_selffunddelev_252d_base_v071_signal,
    f29dt_f29_debt_trajectory_stshareaccel_252d_base_v072_signal,
    f29dt_f29_debt_trajectory_fragilebuild_504d_base_v073_signal,
    f29dt_f29_debt_trajectory_ndchgrank_126d_base_v074_signal,
    f29dt_f29_debt_trajectory_delevscore_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_DEBT_TRAJECTORY_REGISTRY_001_075 = REGISTRY


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

    debt = _fund(101, base=1.2e9, drift=0.015, vol=0.06).rename("debt")
    debtusd = _fund(102, base=1.2e9, drift=0.015, vol=0.06).rename("debtusd")
    debtc = _fund(103, base=3.0e8, drift=0.01, vol=0.08).rename("debtc")
    debtnc = _fund(104, base=9.0e8, drift=0.018, vol=0.05).rename("debtnc")
    cashneq = _fund(105, base=4.0e8, drift=0.02, vol=0.09).rename("cashneq")
    # ncfdebt is a financing FLOW: derive it as the period change of a debt-like
    # walk so it genuinely oscillates in sign (issuance vs repayment quarters).
    _dwalk = _fund(106, base=8.0e8, drift=0.0, vol=0.12, allow_neg=True)
    ncfdebt = _dwalk.diff().fillna(0.0).rename("ncfdebt")
    ncfdebt = ncfdebt + pd.Series(np.random.normal(0, 5e5, n), index=ncfdebt.index)
    ncfdebt = ncfdebt.rename("ncfdebt")

    cols = {"debt": debt, "debtusd": debtusd, "debtc": debtc,
            "debtnc": debtnc, "cashneq": cashneq, "ncfdebt": ncfdebt}

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

    print("OK f29_debt_trajectory_base_001_075_claude: %d features pass" % n_features)
