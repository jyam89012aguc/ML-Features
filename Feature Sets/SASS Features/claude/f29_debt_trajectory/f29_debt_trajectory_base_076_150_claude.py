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
    return np.log(d.replace(0, np.nan) / d.shift(w).replace(0, np.nan))


def _f29_pctchg(d, w):
    return d / d.shift(w).replace(0, np.nan) - 1.0


def _f29_netdebt(debt, cashneq):
    return debt - cashneq


def _f29_st_share(debtc, debt):
    return debtc / debt.replace(0, np.nan)


def _f29_lt_share(debtnc, debt):
    return debtnc / debt.replace(0, np.nan)


def _f29_ols_slope(s, w):
    n = w
    idx = np.arange(n)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _f(a):
        if np.any(~np.isfinite(a)):
            return np.nan
        ym = a.mean()
        return float(((idx - xm) * (a - ym)).sum() / xden)

    return s.rolling(n, min_periods=n).apply(_f, raw=True)


# ============================================================
# debt level EMA displacement: debt vs its own slow EMA (above/below financing trend)
def f29dt_f29_debt_trajectory_debtemadisp_252d_base_v076_signal(debt):
    e = debt.ewm(span=252, min_periods=63).mean()
    b = debt / e.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt month-growth EMA (fast persistent financing pace)
def f29dt_f29_debt_trajectory_dgrowema_21d_base_v077_signal(debt):
    g = _f29_growth(debt, 21)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt log-growth over two years (long net-leverage trajectory)
def f29dt_f29_debt_trajectory_ndgrow_504d_base_v078_signal(debt, cashneq):
    nd = (debt - cashneq).clip(lower=1.0)
    b = np.log(nd) - np.log(nd.shift(504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-cash ratio level, percentile-ranked vs 504d history (leverage extremity)
def f29dt_f29_debt_trajectory_debtcashrank_504d_base_v079_signal(debt, cashneq):
    r = debt / cashneq.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow tilt: net issuance vs repayment magnitude balance over a year
def f29dt_f29_debt_trajectory_ncftilt_252d_base_v080_signal(ncfdebt):
    pos = ncfdebt.clip(lower=0.0).rolling(252, min_periods=126).sum()
    neg = (-ncfdebt.clip(upper=0.0)).rolling(252, min_periods=126).sum()
    b = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt growth over a quarter (near-term funding ramp)
def f29dt_f29_debt_trajectory_stgrow_63d_base_v081_signal(debtc):
    b = _f29_growth(debtc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt growth over a year, de-trended vs its 504d mean
def f29dt_f29_debt_trajectory_ltgrowdev_252d_base_v082_signal(debtnc):
    g = _f29_growth(debtnc, 252)
    b = g - _mean(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# maturity mix entropy proxy: |0.5 - st-share| inverted (balanced vs lopsided debt)
def f29dt_f29_debt_trajectory_maturitymix_base_v083_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    b = 0.5 - (sh - 0.5).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt level vs cash level cross-growth gap, EMA-smoothed (balance trend)
def f29dt_f29_debt_trajectory_balgap_ema_base_v084_signal(debt, cashneq):
    gd = _f29_growth(debt, 63)
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(63).clip(lower=1.0))
    b = (gd - gc).ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt acceleration over a half-year (half-year growth now vs half-year ago)
def f29dt_f29_debt_trajectory_daccel_126d_base_v085_signal(debt):
    g = _f29_growth(debt, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt deviation from its 252d peak (net deleveraging from worst point)
def f29dt_f29_debt_trajectory_ndfrompeak_252d_base_v086_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    pk = _rmax(nd, 252)
    b = (nd - pk) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt cumulative net flow over two years scaled by debt (long financing balance)
def f29dt_f29_debt_trajectory_ncfcum_504d_base_v087_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(504, min_periods=252).sum()
    b = cum / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-growth vs USD-debt-growth ratio over a half-year (fx-adjusted financing)
def f29dt_f29_debt_trajectory_dusdratio_126d_base_v088_signal(debt, debtusd):
    gd = _f29_pctchg(debt, 126)
    gu = _f29_pctchg(debtusd, 126)
    b = gd - gu
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt level z-score relative to gross debt (rollover-load extremity)
def f29dt_f29_debt_trajectory_stloadz_252d_base_v089_signal(debtc, debt):
    load = debtc / debt.replace(0, np.nan)
    b = _z(load, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging persistence: longest fraction of 2y with net-debt below 252d-ago level
def f29dt_f29_debt_trajectory_delpersist_504d_base_v090_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    below = (nd < nd.shift(252)).astype(float)
    b = below.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-growth skewness over a year (asymmetry of financing shocks)
def f29dt_f29_debt_trajectory_dgrowskew_252d_base_v091_signal(debt):
    g = _f29_growth(debt, 21)
    b = g.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage of short-term debt, change over a year (rollover-buffer trend)
def f29dt_f29_debt_trajectory_stcovchg_252d_base_v092_signal(cashneq, debtc):
    cov = cashneq / debtc.replace(0, np.nan)
    b = cov - cov.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build × cash drawdown interaction (levering up while burning cash)
def f29dt_f29_debt_trajectory_leverburn_252d_base_v093_signal(debt, cashneq):
    gd = _f29_growth(debt, 252)
    cpk = _rmax(cashneq, 252)
    cdd = (cashneq / cpk.replace(0, np.nan) - 1.0)
    b = gd.clip(lower=0.0) * (-cdd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow slope (OLS slope of debt flow over a year, financing acceleration)
def f29dt_f29_debt_trajectory_ncfslope_252d_base_v094_signal(ncfdebt, debt):
    f = ncfdebt / debt.replace(0, np.nan)
    b = _f29_ols_slope(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt position within 252d range, de-meaned (where in net-leverage cycle)
def f29dt_f29_debt_trajectory_ndcyclepos_252d_base_v095_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    hi = _rmax(nd, 252)
    lo = _rmin(nd, 252)
    pos = (nd - lo) / (hi - lo).replace(0, np.nan)
    b = pos - _mean(pos, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-growth downside semi-deviation over a year (volatility of paydown shocks)
def f29dt_f29_debt_trajectory_dgrowsemidev_252d_base_v096_signal(debt):
    g = _f29_growth(debt, 21)
    neg = g.where(g < 0)
    b = neg.rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-vs-short debt level ratio trend (term structure of the debt stack)
def f29dt_f29_debt_trajectory_ltstratio_252d_base_v097_signal(debtnc, debtc):
    r = debtnc / debtc.replace(0, np.nan)
    b = np.log(r.replace(0, np.nan)) - np.log(r.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown amount vs cash level (paydown capacity used)
def f29dt_f29_debt_trajectory_paycapacity_252d_base_v098_signal(debt, cashneq):
    paid = (debt.shift(252) - debt).clip(lower=0.0)
    b = paid / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd level extension above its 252d mean (absolute debt-load stretch)
def f29dt_f29_debt_trajectory_dusdextend_252d_base_v099_signal(debtusd):
    mn = _mean(debtusd, 252)
    b = (debtusd - mn) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net financing flow asymmetry between halves of the past year (front/back loaded)
def f29dt_f29_debt_trajectory_ncfhalfasym_252d_base_v100_signal(ncfdebt, debt):
    f = ncfdebt / debt.replace(0, np.nan)
    recent = f.rolling(126, min_periods=63).sum()
    older = f.shift(126).rolling(126, min_periods=63).sum()
    b = recent - older
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash growth minus net-debt growth (liquidity-led balance improvement)
def f29dt_f29_debt_trajectory_liqled_252d_base_v101_signal(cashneq, debt):
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(252).clip(lower=1.0))
    nd = (debt - cashneq).clip(lower=1.0)
    gnd = np.log(nd) - np.log(nd.shift(252))
    b = gc - gnd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt share momentum vs its long-run average (rollover regime shift)
def f29dt_f29_debt_trajectory_stsharemom_252d_base_v102_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    b = sh.ewm(span=63, min_periods=21).mean() - _mean(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build relative to two-year median debt (structural leverage shift)
def f29dt_f29_debt_trajectory_buildvsmed_504d_base_v103_signal(debt):
    med = debt.rolling(504, min_periods=252).median()
    b = debt / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt repayment consistency: rolling std of flow sign over a year
def f29dt_f29_debt_trajectory_ncfsignstd_252d_base_v104_signal(ncfdebt):
    sg = np.sign(ncfdebt)
    b = _std(sg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth minus its long-term-debt growth (where new debt is concentrated)
def f29dt_f29_debt_trajectory_growconcentr_252d_base_v105_signal(debt, debtnc):
    gd = _f29_growth(debt, 252)
    gnc = _f29_growth(debtnc, 252)
    b = gd - gnc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt to debt-flow coverage: how many years of flow to clear net debt
def f29dt_f29_debt_trajectory_ndflowyears_252d_base_v106_signal(debt, cashneq, ncfdebt):
    nd = (debt - cashneq)
    repay = (-ncfdebt).rolling(252, min_periods=126).sum()
    b = nd / repay.replace(0, np.nan)
    b = np.sign(b) * np.log1p(b.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-growth dispersion across short/long maturities (uneven term financing)
def f29dt_f29_debt_trajectory_termdisp_252d_base_v107_signal(debtc, debtnc, debt):
    gc = _f29_growth(debtc, 252)
    gnc = _f29_growth(debtnc, 252)
    gd = _f29_growth(debt, 252)
    b = pd.concat([gc, gnc, gd], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt ratio slope (OLS) over a year (liquidity-buffer trajectory)
def f29dt_f29_debt_trajectory_cashdebtslope_252d_base_v108_signal(cashneq, debt):
    r = cashneq / debt.replace(0, np.nan)
    b = _f29_ols_slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt drawup duration: fraction of a year debt sat above its 252d-ago level
def f29dt_f29_debt_trajectory_buildtime_252d_base_v109_signal(debt):
    above = (debt > debt.shift(252)).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow z-score interacted with debt-growth sign (confirmed financing)
def f29dt_f29_debt_trajectory_ncfconfirm_252d_base_v110_signal(ncfdebt, debt):
    fz = _z(ncfdebt, 252)
    gs = np.sign(_f29_growth(debt, 63))
    b = fz * gs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt build relative to its 252d trough (near-term debt ramp from low)
def f29dt_f29_debt_trajectory_sttroughbuild_252d_base_v111_signal(debtc):
    tr = _rmin(debtc, 252)
    b = debtc / tr.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt level coefficient of variation over a year (stable vs volatile debt load)
def f29dt_f29_debt_trajectory_debtcv_252d_base_v112_signal(debt):
    b = _std(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt change relative to cash level (paydown funded out of cash)
def f29dt_f29_debt_trajectory_ndchgvscash_252d_base_v113_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    chg = nd - nd.shift(252)
    b = chg / cashneq.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debtusd growth acceleration over a quarter (absolute-load financing turn)
def f29dt_f29_debt_trajectory_dusdaccel_63d_base_v114_signal(debtusd):
    g = _f29_growth(debtusd, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of year with positive net-debt change (net-leverage-up frequency)
def f29dt_f29_debt_trajectory_ndupfreq_252d_base_v115_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    up = (nd > nd.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term-debt share level z-scored (term-out extremity)
def f29dt_f29_debt_trajectory_ltsharez_252d_base_v116_signal(debtnc, debt):
    sh = _f29_lt_share(debtnc, debt)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth half-life proxy: growth divided by its own 252d volatility (signal/noise)
def f29dt_f29_debt_trajectory_growsnr_252d_base_v117_signal(debt):
    g = _f29_growth(debt, 252)
    vol = _std(_f29_growth(debt, 21), 252)
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net repayment flow accelerating: change in smoothed repayment over a quarter
def f29dt_f29_debt_trajectory_repayaccel_63d_base_v118_signal(ncfdebt, debt):
    repay = (-ncfdebt).rolling(63, min_periods=21).mean() / debt.replace(0, np.nan)
    b = repay - repay.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-net-of-short-term-debt trajectory (net liquidity after near-term obligations)
def f29dt_f29_debt_trajectory_netliq_252d_base_v119_signal(cashneq, debtc, debt):
    nl = (cashneq - debtc) / debt.replace(0, np.nan)
    b = nl - nl.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth percentile vs long history, smoothed (durable financing regime)
def f29dt_f29_debt_trajectory_growregime_126d_base_v120_signal(debt):
    g = _f29_growth(debt, 126)
    b = _rank(g, 504).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute net-debt level relative to debtusd (net leverage on USD base), de-trended
def f29dt_f29_debt_trajectory_ndtousd_dev_126d_base_v121_signal(debt, cashneq, debtusd):
    nd = debt - cashneq
    r = nd / debtusd.replace(0, np.nan)
    b = r - _mean(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown momentum confirmed by falling short-term share (clean term-out paydown)
def f29dt_f29_debt_trajectory_cleanpaydown_252d_base_v122_signal(debt, debtc):
    pay = -_f29_growth(debt, 252)
    sh = _f29_st_share(debtc, debt)
    dsh = -(sh - sh.shift(252))
    b = pay * np.tanh(5.0 * dsh)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since fresh 252d debt high, normalized (staleness of peak borrowing)
def f29dt_f29_debt_trajectory_recorddebt_252d_base_v123_signal(debt):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = debt.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt repayment-vs-issuance flow ratio over two years
def f29dt_f29_debt_trajectory_repayissratio_504d_base_v124_signal(ncfdebt):
    iss = ncfdebt.clip(lower=0.0).rolling(504, min_periods=252).sum()
    rep = (-ncfdebt.clip(upper=0.0)).rolling(504, min_periods=252).sum()
    b = (rep - iss) / (rep + iss).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build vs cash build correlation of monthly changes (joint financing behavior)
def f29dt_f29_debt_trajectory_debtcashcorr_252d_base_v125_signal(debt, cashneq):
    gd = _f29_growth(debt, 21)
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(21).clip(lower=1.0))
    b = gd.rolling(252, min_periods=126).corr(gc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term debt acceleration (quarter-growth now vs a quarter ago)
def f29dt_f29_debt_trajectory_staccel_63d_base_v126_signal(debtc):
    g = _f29_growth(debtc, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt deviation from its 504d EMA (long net-leverage displacement)
def f29dt_f29_debt_trajectory_ndemadisp_504d_base_v127_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    e = nd.ewm(span=252, min_periods=63).mean()
    b = (nd - e) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth weighted by inverse cash coverage (riskier when cash is thin)
def f29dt_f29_debt_trajectory_growthincover_252d_base_v128_signal(debt, cashneq):
    g = _f29_growth(debt, 252)
    cov = cashneq / debt.replace(0, np.nan)
    b = g / (1.0 + cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-term debt growth over two years (structural term-debt trajectory)
def f29dt_f29_debt_trajectory_ltgrow_504d_base_v129_signal(debtnc):
    b = _f29_growth(debtnc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow as fraction of cashneq (financing pressure on liquidity)
def f29dt_f29_debt_trajectory_ncfvscash_126d_base_v130_signal(ncfdebt, cashneq):
    f = ncfdebt / cashneq.replace(0, np.nan)
    b = _mean(f, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-trough recovery time proxy: days since 504d min debt, normalized
def f29dt_f29_debt_trajectory_dayssincemin_504d_base_v131_signal(debt):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    b = debt.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 504d peak debt, normalized (staleness of peak leverage)
def f29dt_f29_debt_trajectory_dayssincemax_504d_base_v132_signal(debt):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = debt.rolling(504, min_periods=252).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-gross-debt ratio level, percentile-ranked (cash-cushion extremity)
def f29dt_f29_debt_trajectory_ndratiorank_252d_base_v133_signal(debt, cashneq):
    r = (debt - cashneq) / debt.replace(0, np.nan)
    b = _rank(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-growth EMA crossover: fast vs slow EMA of monthly debt growth
def f29dt_f29_debt_trajectory_growcross_base_v134_signal(debt):
    g = _f29_growth(debt, 21)
    fast = g.ewm(span=42, min_periods=21).mean()
    slow = g.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term-debt-to-cash whipsaw: rolling std of the ratio (rollover instability)
def f29dt_f29_debt_trajectory_strolvol_252d_base_v135_signal(debtc, cashneq):
    r = debtc / cashneq.replace(0, np.nan)
    b = _std(r, 252) / _mean(r, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net financing flow z-scored vs history (abnormal cumulative borrowing)
def f29dt_f29_debt_trajectory_ncfcumz_252d_base_v136_signal(ncfdebt, debt):
    cum = ncfdebt.rolling(252, min_periods=126).sum() / debt.replace(0, np.nan)
    b = _z(cum, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt build acceleration vs cash build acceleration (relative financing impulse)
def f29dt_f29_debt_trajectory_impulsegap_126d_base_v137_signal(debt, cashneq):
    gd = _f29_growth(debt, 63)
    ad = gd - gd.shift(63)
    gc = np.log(cashneq.clip(lower=1.0)) - np.log(cashneq.shift(63).clip(lower=1.0))
    ac = gc - gc.shift(63)
    b = ad - ac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-up streak strength: consecutive months of net-debt increase, normalized
def f29dt_f29_debt_trajectory_ndupstreak_base_v138_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    inc = (nd > nd.shift(21)).astype(float)
    grp = (inc != inc.shift(1)).cumsum()
    streak = inc.groupby(grp).cumcount() + 1
    b = (streak * inc) / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth minus debtusd growth, ranked (reported-vs-USD financing divergence)
def f29dt_f29_debt_trajectory_usddivrank_252d_base_v139_signal(debt, debtusd):
    diff = _f29_growth(debt, 252) - _f29_growth(debtusd, 252)
    b = _rank(diff, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage convexity: 2nd difference of cash/debt (accelerating buffer build)
def f29dt_f29_debt_trajectory_covconvex_126d_base_v140_signal(cashneq, debt):
    cov = cashneq / debt.replace(0, np.nan)
    b = (cov - 2.0 * cov.shift(63) + cov.shift(126)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total debt vs sum of components consistency (st+lt vs gross), de-trended
def f29dt_f29_debt_trajectory_componentgap_126d_base_v141_signal(debtc, debtnc, debt):
    gap = (debtc + debtnc - debt) / debt.replace(0, np.nan)
    b = gap - _mean(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt momentum scaled by debt volatility (risk-adjusted net leverage change)
def f29dt_f29_debt_trajectory_ndmomriskadj_252d_base_v142_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    chg = (nd - nd.shift(252)) / debt.replace(0, np.nan)
    vol = _std(_f29_growth(debt, 21), 252)
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of two years with net repayment flow weighted by flow magnitude
def f29dt_f29_debt_trajectory_repaydom_504d_base_v143_signal(ncfdebt, debt):
    f = ncfdebt / debt.replace(0, np.nan)
    repaymag = (-f.clip(upper=0.0)).rolling(504, min_periods=252).mean()
    rate = (f < 0).astype(float).rolling(504, min_periods=252).mean()
    b = rate - 0.5 + 5.0 * repaymag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt ratio momentum minus its own trend (liquidity-buffer surprise)
def f29dt_f29_debt_trajectory_buffersurprise_252d_base_v144_signal(debt, cashneq):
    r = cashneq / debt.replace(0, np.nan)
    mom = r - r.shift(126)
    b = mom - _mean(mom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short-term share trend slope (OLS) over a year (rollover-mix trajectory)
def f29dt_f29_debt_trajectory_stshareslope_252d_base_v145_signal(debtc, debt):
    sh = _f29_st_share(debtc, debt)
    b = _f29_ols_slope(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-to-cash log ratio momentum over a half-year (gross leverage trend)
def f29dt_f29_debt_trajectory_debtcashmom_126d_base_v146_signal(debt, cashneq):
    lr = np.log(debt.replace(0, np.nan)) - np.log(cashneq.replace(0, np.nan))
    b = lr - lr.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ncfdebt flow turning point: sign of smoothed flow vs sign a half-year ago
def f29dt_f29_debt_trajectory_ncfturn_126d_base_v147_signal(ncfdebt):
    sm = _mean(ncfdebt, 63)
    b = np.sign(sm) - np.sign(sm.shift(126))
    b = b + 0.25 * np.tanh(_z(ncfdebt, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-growth quartile-spread over a year (dispersion of financing intensity)
def f29dt_f29_debt_trajectory_growiqr_252d_base_v148_signal(debt):
    g = _f29_growth(debt, 21)
    q75 = g.rolling(252, min_periods=126).quantile(0.75)
    q25 = g.rolling(252, min_periods=126).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt range width over two years normalized by debt (net-leverage amplitude)
def f29dt_f29_debt_trajectory_ndamplitude_504d_base_v149_signal(debt, cashneq):
    nd = _f29_netdebt(debt, cashneq)
    hi = _rmax(nd, 504)
    lo = _rmin(nd, 504)
    b = (hi - lo) / debt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite financing-health: paydown hit-rate plus cash-coverage volatility penalty
def f29dt_f29_debt_trajectory_finhealth_252d_base_v150_signal(debt, cashneq):
    paydown = (debt < debt.shift(21)).astype(float).rolling(252, min_periods=126).mean()
    cov = cashneq / debt.replace(0, np.nan)
    covvol = _std(cov, 252) / _mean(cov, 252).replace(0, np.nan)
    b = (paydown - 0.5) - np.tanh(covvol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29dt_f29_debt_trajectory_debtemadisp_252d_base_v076_signal,
    f29dt_f29_debt_trajectory_dgrowema_21d_base_v077_signal,
    f29dt_f29_debt_trajectory_ndgrow_504d_base_v078_signal,
    f29dt_f29_debt_trajectory_debtcashrank_504d_base_v079_signal,
    f29dt_f29_debt_trajectory_ncftilt_252d_base_v080_signal,
    f29dt_f29_debt_trajectory_stgrow_63d_base_v081_signal,
    f29dt_f29_debt_trajectory_ltgrowdev_252d_base_v082_signal,
    f29dt_f29_debt_trajectory_maturitymix_base_v083_signal,
    f29dt_f29_debt_trajectory_balgap_ema_base_v084_signal,
    f29dt_f29_debt_trajectory_daccel_126d_base_v085_signal,
    f29dt_f29_debt_trajectory_ndfrompeak_252d_base_v086_signal,
    f29dt_f29_debt_trajectory_ncfcum_504d_base_v087_signal,
    f29dt_f29_debt_trajectory_dusdratio_126d_base_v088_signal,
    f29dt_f29_debt_trajectory_stloadz_252d_base_v089_signal,
    f29dt_f29_debt_trajectory_delpersist_504d_base_v090_signal,
    f29dt_f29_debt_trajectory_dgrowskew_252d_base_v091_signal,
    f29dt_f29_debt_trajectory_stcovchg_252d_base_v092_signal,
    f29dt_f29_debt_trajectory_leverburn_252d_base_v093_signal,
    f29dt_f29_debt_trajectory_ncfslope_252d_base_v094_signal,
    f29dt_f29_debt_trajectory_ndcyclepos_252d_base_v095_signal,
    f29dt_f29_debt_trajectory_dgrowsemidev_252d_base_v096_signal,
    f29dt_f29_debt_trajectory_ltstratio_252d_base_v097_signal,
    f29dt_f29_debt_trajectory_paycapacity_252d_base_v098_signal,
    f29dt_f29_debt_trajectory_dusdextend_252d_base_v099_signal,
    f29dt_f29_debt_trajectory_ncfhalfasym_252d_base_v100_signal,
    f29dt_f29_debt_trajectory_liqled_252d_base_v101_signal,
    f29dt_f29_debt_trajectory_stsharemom_252d_base_v102_signal,
    f29dt_f29_debt_trajectory_buildvsmed_504d_base_v103_signal,
    f29dt_f29_debt_trajectory_ncfsignstd_252d_base_v104_signal,
    f29dt_f29_debt_trajectory_growconcentr_252d_base_v105_signal,
    f29dt_f29_debt_trajectory_ndflowyears_252d_base_v106_signal,
    f29dt_f29_debt_trajectory_termdisp_252d_base_v107_signal,
    f29dt_f29_debt_trajectory_cashdebtslope_252d_base_v108_signal,
    f29dt_f29_debt_trajectory_buildtime_252d_base_v109_signal,
    f29dt_f29_debt_trajectory_ncfconfirm_252d_base_v110_signal,
    f29dt_f29_debt_trajectory_sttroughbuild_252d_base_v111_signal,
    f29dt_f29_debt_trajectory_debtcv_252d_base_v112_signal,
    f29dt_f29_debt_trajectory_ndchgvscash_252d_base_v113_signal,
    f29dt_f29_debt_trajectory_dusdaccel_63d_base_v114_signal,
    f29dt_f29_debt_trajectory_ndupfreq_252d_base_v115_signal,
    f29dt_f29_debt_trajectory_ltsharez_252d_base_v116_signal,
    f29dt_f29_debt_trajectory_growsnr_252d_base_v117_signal,
    f29dt_f29_debt_trajectory_repayaccel_63d_base_v118_signal,
    f29dt_f29_debt_trajectory_netliq_252d_base_v119_signal,
    f29dt_f29_debt_trajectory_growregime_126d_base_v120_signal,
    f29dt_f29_debt_trajectory_ndtousd_dev_126d_base_v121_signal,
    f29dt_f29_debt_trajectory_cleanpaydown_252d_base_v122_signal,
    f29dt_f29_debt_trajectory_recorddebt_252d_base_v123_signal,
    f29dt_f29_debt_trajectory_repayissratio_504d_base_v124_signal,
    f29dt_f29_debt_trajectory_debtcashcorr_252d_base_v125_signal,
    f29dt_f29_debt_trajectory_staccel_63d_base_v126_signal,
    f29dt_f29_debt_trajectory_ndemadisp_504d_base_v127_signal,
    f29dt_f29_debt_trajectory_growthincover_252d_base_v128_signal,
    f29dt_f29_debt_trajectory_ltgrow_504d_base_v129_signal,
    f29dt_f29_debt_trajectory_ncfvscash_126d_base_v130_signal,
    f29dt_f29_debt_trajectory_dayssincemin_504d_base_v131_signal,
    f29dt_f29_debt_trajectory_dayssincemax_504d_base_v132_signal,
    f29dt_f29_debt_trajectory_ndratiorank_252d_base_v133_signal,
    f29dt_f29_debt_trajectory_growcross_base_v134_signal,
    f29dt_f29_debt_trajectory_strolvol_252d_base_v135_signal,
    f29dt_f29_debt_trajectory_ncfcumz_252d_base_v136_signal,
    f29dt_f29_debt_trajectory_impulsegap_126d_base_v137_signal,
    f29dt_f29_debt_trajectory_ndupstreak_base_v138_signal,
    f29dt_f29_debt_trajectory_usddivrank_252d_base_v139_signal,
    f29dt_f29_debt_trajectory_covconvex_126d_base_v140_signal,
    f29dt_f29_debt_trajectory_componentgap_126d_base_v141_signal,
    f29dt_f29_debt_trajectory_ndmomriskadj_252d_base_v142_signal,
    f29dt_f29_debt_trajectory_repaydom_504d_base_v143_signal,
    f29dt_f29_debt_trajectory_buffersurprise_252d_base_v144_signal,
    f29dt_f29_debt_trajectory_stshareslope_252d_base_v145_signal,
    f29dt_f29_debt_trajectory_debtcashmom_126d_base_v146_signal,
    f29dt_f29_debt_trajectory_ncfturn_126d_base_v147_signal,
    f29dt_f29_debt_trajectory_growiqr_252d_base_v148_signal,
    f29dt_f29_debt_trajectory_ndamplitude_504d_base_v149_signal,
    f29dt_f29_debt_trajectory_finhealth_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_DEBT_TRAJECTORY_REGISTRY_076_150 = REGISTRY


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
    _dwalk = _fund(106, base=8.0e8, drift=0.0, vol=0.12, allow_neg=True)
    ncfdebt = _dwalk.diff().fillna(0.0)
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

    print("OK f29_debt_trajectory_base_076_150_claude: %d features pass" % n_features)
