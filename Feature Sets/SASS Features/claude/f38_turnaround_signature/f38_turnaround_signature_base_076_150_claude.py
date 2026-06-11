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


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(~np.isfinite(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (turnaround signature) =====
def _f38_margin_floor_gap(grossmargin, w):
    lo = _rmin(grossmargin, w)
    return (grossmargin - lo) / (grossmargin.abs() + lo.abs()).replace(0, np.nan)


def _f38_loss_narrow(netinc, w):
    base = _rmin(netinc, w)
    return (netinc - base) / (netinc.abs() + base.abs() + 1.0)


def _f38_fcf_cross(fcf, w):
    lo = _rmin(fcf, w)
    return (fcf - lo) / (fcf.abs() + lo.abs()).replace(0, np.nan)


def _f38_delever(debt, w):
    hi = _rmax(debt, w)
    return (hi - debt) / hi.replace(0, np.nan)


def _f38_rev_stab(revenue, w):
    g = revenue.pct_change()
    return _mean(g, w) / (_std(g, w).replace(0, np.nan))


def _f38_recover_off_low(s, w):
    lo = _rmin(s, w)
    return s / lo.replace(0, np.nan) - 1.0


# ============================================================
# margin floor lift, exponentially weighted (persistent inflection)
def f38ts_f38_turnaround_signature_mliftewm_252d_base_v076_signal(grossmargin, revenue):
    lift = _f38_margin_floor_gap(grossmargin, 252)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = (lift * w).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# margin lift relative to its own dispersion (signal-to-noise turn)
def f38ts_f38_turnaround_signature_mliftsnr_252d_base_v077_signal(grossmargin, ncfo):
    lift = grossmargin - _rmin(grossmargin, 252)
    snr = _mean(lift, 63) / _std(lift, 126).replace(0, np.nan)
    cl = np.tanh(_f38_recover_off_low(ncfo, 252))
    result = snr * (0.5 + cl)
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin acceleration sign times revenue stability (durable inflection)
def f38ts_f38_turnaround_signature_maccel_252d_base_v078_signal(grossmargin, revenue):
    acc = grossmargin.diff(21) - grossmargin.diff(21).shift(21)
    stab = np.tanh(_f38_rev_stab(revenue, 126))
    result = np.sign(acc) * (acc.abs() ** 0.5) * (0.5 + stab)
    return result.replace([np.inf, -np.inf], np.nan)


# margin lift cross-time rank weighted by equity solvency
def f38ts_f38_turnaround_signature_mliftrank_252d_base_v079_signal(grossmargin, equity, debt):
    lift = _f38_margin_floor_gap(grossmargin, 252)
    r = _rank(lift, 504)
    solv = equity / (equity.abs() + debt.abs()).replace(0, np.nan)
    result = r * (0.5 + solv.clip(lower=-0.5))
    return result.replace([np.inf, -np.inf], np.nan)


# net income recovery off trough, z-scored (distress-exit intensity)
def f38ts_f38_turnaround_signature_nirecovz_252d_base_v080_signal(netinc, revenue):
    rec = (netinc - _rmin(netinc, 252)) / _mean(revenue, 252).replace(0, np.nan)
    result = _z(rec, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing slope ranked vs history (cleanly improving earnings)
def f38ts_f38_turnaround_signature_lossslopernk_252d_base_v081_signal(netinc, equity):
    sl = _slope(netinc, 252) / _mean(equity.abs(), 252).replace(0, np.nan)
    result = _rank(sl, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# earnings convexity from a depressed base (second difference, distress-weighted)
def f38ts_f38_turnaround_signature_niconvex_252d_base_v082_signal(netinc, revenue):
    acc = netinc.diff(63) - netinc.diff(63).shift(63)
    norm = _mean(revenue, 252).replace(0, np.nan)
    below = (netinc < _mean(netinc, 504)).astype(float)
    result = (acc / norm) * (0.5 + below)
    return result.replace([np.inf, -np.inf], np.nan)


# net-income hit rate of improvement weighted by depth of loss
def f38ts_f38_turnaround_signature_nihitdepth_252d_base_v083_signal(netinc, equity):
    up = (netinc.diff(21) > 0).astype(float).rolling(252, min_periods=126).mean()
    depth = (-(netinc / _mean(equity.abs(), 252).replace(0, np.nan))).clip(lower=0)
    result = up * (0.5 + np.tanh(depth))
    return result.replace([np.inf, -np.inf], np.nan)


# FCF crossing strength smoothed and z-scored (sustained cash turn)
def f38ts_f38_turnaround_signature_fcfcrossz_252d_base_v084_signal(fcf, equity):
    cr = _f38_fcf_cross(fcf, 252)
    lvl = np.tanh(fcf / _mean(equity.abs(), 252).replace(0, np.nan))
    result = _z(cr, 126) + lvl
    return result.replace([np.inf, -np.inf], np.nan)


# FCF crossing-strength lift gated by margin slope sign (cash turn confirmed)
def f38ts_f38_turnaround_signature_fcfshareturn_252d_base_v085_signal(fcf, grossmargin):
    cr = _f38_fcf_cross(fcf, 252)
    lift = cr - cr.shift(63)
    msl = np.tanh(80.0 * _slope(grossmargin, 126))
    result = lift * (0.5 + 0.5 * msl)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin recovery slope normalized by revenue
def f38ts_f38_turnaround_signature_fcfmargslp_252d_base_v086_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    sl = _slope(fm, 126)
    result = np.tanh(20.0 * sl) + (fm - _rmin(fm, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo crossing back positive, ranked vs own history
def f38ts_f38_turnaround_signature_ncfocrossrnk_252d_base_v087_signal(ncfo, debt):
    cr = _f38_fcf_cross(ncfo, 252)
    dl = _f38_delever(debt, 252)
    result = _rank(cr, 504) * (0.5 + dl)
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash recovery relative to its volatility
def f38ts_f38_turnaround_signature_ncforecsnr_252d_base_v088_signal(ncfo, revenue):
    rec = (ncfo - _rmin(ncfo, 252))
    snr = rec / _std(ncfo, 126).replace(0, np.nan)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = snr * w
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging slope, z-scored, with stabilizing revenue gate
def f38ts_f38_turnaround_signature_delevslopez_252d_base_v089_signal(debt, revenue):
    sl = -_slope(debt, 252) / _mean(debt, 252).replace(0, np.nan)
    stab = np.tanh(_f38_rev_stab(revenue, 126))
    result = _z(sl, 252) * (0.5 + stab)
    return result.replace([np.inf, -np.inf], np.nan)


# debt off-peak ratio smoothed, deeper window
def f38ts_f38_turnaround_signature_delevema_504d_base_v090_signal(debt, equity):
    dl = _f38_delever(debt, 504)
    eqr = np.tanh(_f38_recover_off_low(equity, 504))
    result = (dl + 0.5 * eqr).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage (debt/equity) decline rank with revenue holding
def f38ts_f38_turnaround_signature_levdeclrnk_252d_base_v091_signal(debt, equity, revenue):
    lev = debt / equity.replace(0, np.nan)
    decl = _rmax(lev, 252) - lev
    rhold = (revenue >= _mean(revenue, 252)).astype(float)
    result = _rank(decl, 504) * (0.5 + 0.5 * rhold)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt (debt minus cash-like equity buffer) improvement
def f38ts_f38_turnaround_signature_netdebtturn_252d_base_v092_signal(debt, equity):
    nd = debt - equity.clip(lower=0)
    hi = _rmax(nd, 252)
    result = (hi - nd) / (hi.abs() + _mean(debt, 252) * 0.1).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue trough recovery slope (top-line stabilizing then turning)
def f38ts_f38_turnaround_signature_revturnslope_252d_base_v093_signal(revenue, netinc):
    rg = revenue.pct_change(21)
    sl = _slope(rg, 126)
    ln = _f38_loss_narrow(netinc, 252)
    result = np.tanh(50.0 * sl) * (0.5 + ln)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue stability improvement (inverse-CV rising off its low)
def f38ts_f38_turnaround_signature_revstabturn_252d_base_v094_signal(revenue, grossmargin):
    stab = _f38_rev_stab(revenue, 126)
    lift = stab - _rmin(stab, 252)
    ml = _f38_margin_floor_gap(grossmargin, 252)
    result = np.tanh(lift) * (0.5 + ml)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery composite of slopes (margin, fcf, debt-paydown) z-blended
def f38ts_f38_turnaround_signature_slopecomp_252d_base_v095_signal(grossmargin, fcf, debt):
    a = _z(_slope(grossmargin, 252), 252)
    b = _z(_slope(fcf, 252), 252)
    c = _z(-_slope(debt, 252), 252)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# recovery composite of off-low ratios, dispersion-penalized
def f38ts_f38_turnaround_signature_offlowdisp_252d_base_v096_signal(grossmargin, ncfo, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(ncfo, 252)
    c = _f38_loss_narrow(netinc, 252)
    stk = pd.concat([a, b, c], axis=1)
    result = stk.mean(axis=1) - 0.5 * stk.std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# quality conversion (ncfo/|netinc|) recovery slope from distress
def f38ts_f38_turnaround_signature_qualconvslp_252d_base_v097_signal(ncfo, netinc):
    conv = ncfo / (netinc.abs() + 1.0)
    sl = _slope(conv, 126)
    lo = conv - _rmin(conv, 252)
    result = np.tanh(sl) + np.tanh(lo)
    return result.replace([np.inf, -np.inf], np.nan)


# early-turn intensity: ncfo positive while netinc depressed, ranked
def f38ts_f38_turnaround_signature_earlyturnrnk_252d_base_v098_signal(ncfo, netinc):
    inten = ncfo / (ncfo.abs() + netinc.abs() + 1.0)
    distress = (netinc < _mean(netinc, 504)).astype(float)
    result = _rank(inten, 504) * (0.5 + distress)
    return result.replace([np.inf, -np.inf], np.nan)


# ROA-style recovery: netinc/(equity+debt) lifting off trough
def f38ts_f38_turnaround_signature_roacaprec_252d_base_v099_signal(netinc, equity, debt):
    cap = (equity.abs() + debt.abs()).replace(0, np.nan)
    roa = netinc / cap
    rec = roa - _rmin(roa, 252)
    result = np.tanh(10.0 * rec)
    return result.replace([np.inf, -np.inf], np.nan)


# ROE inflection: off-trough recovery of return-on-equity, convexity-weighted
def f38ts_f38_turnaround_signature_roeslprnk_252d_base_v100_signal(netinc, equity):
    roe = netinc / equity.replace(0, np.nan)
    rec = (roe - _rmin(roe, 252)) / (roe.abs() + _rmin(roe, 252).abs() + 0.01)
    acc = roe.diff(63) - roe.diff(63).shift(63)
    result = rec + np.tanh(20.0 * acc)
    return result.replace([np.inf, -np.inf], np.nan)


# margin trend minus revenue trend (profitability leading the top line)
def f38ts_f38_turnaround_signature_marglead_252d_base_v101_signal(grossmargin, revenue):
    msl = _z(_slope(grossmargin, 252), 252)
    rsl = _z(_slope(revenue, 252), 252)
    result = msl - rsl
    return result.replace([np.inf, -np.inf], np.nan)


# FCF slope minus netinc slope (cash leading earnings recovery)
def f38ts_f38_turnaround_signature_cashleadslp_252d_base_v102_signal(fcf, netinc):
    fsl = _z(_slope(fcf, 252), 252)
    nsl = _z(_slope(netinc, 252), 252)
    result = fsl - nsl
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown slope minus margin slope (balance-sheet vs ops timing)
def f38ts_f38_turnaround_signature_bstiming_252d_base_v103_signal(debt, grossmargin):
    dsl = _z(-_slope(debt, 252), 252)
    msl = _z(_slope(grossmargin, 252), 252)
    result = dsl - msl
    return result.replace([np.inf, -np.inf], np.nan)


# breakeven approach: net margin distance below ceiling, slope
def f38ts_f38_turnaround_signature_breakevenslp_252d_base_v104_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    gap = _rmax(nm, 252) - nm
    result = -_slope(gap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# distress-exit composite count, smoothed and z-scored
def f38ts_f38_turnaround_signature_distexitz_252d_base_v105_signal(netinc, fcf, debt, grossmargin):
    s1 = (netinc.diff(63) > 0).astype(float)
    s2 = (fcf > _rmin(fcf, 252)).astype(float)
    s3 = (debt.diff(63) < 0).astype(float)
    s4 = (grossmargin.diff(63) > 0).astype(float)
    raw = (s1 + s2 + s3 + s4).rolling(126, min_periods=63).mean()
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround breadth dispersion across five engines
def f38ts_f38_turnaround_signature_breadthdisp_252d_base_v106_signal(grossmargin, fcf, debt, revenue, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(fcf, 252)
    c = _f38_delever(debt, 252)
    d = np.tanh(_f38_rev_stab(revenue, 126))
    e = _f38_loss_narrow(netinc, 252)
    stk = pd.concat([a, b, c, d, e], axis=1)
    result = -stk.std(axis=1) + stk.min(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-dollars recovery slope vs equity
def f38ts_f38_turnaround_signature_gpdollslp_252d_base_v107_signal(grossmargin, revenue, equity):
    gp = grossmargin * revenue
    sl = _slope(gp, 252) / _mean(equity.abs(), 252).replace(0, np.nan)
    result = np.tanh(sl) + np.tanh((gp - _rmin(gp, 252)) / _mean(equity.abs(), 252).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding turnaround: ncfo covering debt-paydown, ranked
def f38ts_f38_turnaround_signature_selffundrnk_252d_base_v108_signal(ncfo, debt):
    paydown = (-debt.diff(63)).clip(lower=0)
    cover = ncfo / (paydown + _mean(debt, 252) * 0.01).replace(0, np.nan)
    result = _rank(cover - _rmin(cover, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capital-structure heal slope: equity up + debt down combined slope
def f38ts_f38_turnaround_signature_bshealslp_504d_base_v109_signal(equity, debt):
    esl = _z(_slope(equity, 252), 252)
    dsl = _z(-_slope(debt, 252), 252)
    result = (esl + dsl) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# accrual gap (ncfo-netinc)/revenue recovery slope
def f38ts_f38_turnaround_signature_accrualslp_252d_base_v110_signal(ncfo, netinc, revenue):
    gap = (ncfo - netinc) / revenue.replace(0, np.nan)
    result = _slope(gap, 126) + (gap - _rmin(gap, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# durable turn: revenue stability rank x margin lift rank product
def f38ts_f38_turnaround_signature_durturnrnk_252d_base_v111_signal(revenue, grossmargin):
    sr = _rank(_f38_rev_stab(revenue, 126), 504)
    mr = _rank(_f38_margin_floor_gap(grossmargin, 252), 504)
    result = sr * mr * 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-debt coverage recovery, ranked
def f38ts_f38_turnaround_signature_fcfdebtrnk_252d_base_v112_signal(fcf, debt):
    cov = fcf / debt.replace(0, np.nan)
    result = _rank(cov - _rmin(cov, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# composite z of off-low ratios over a deeper 504d base
def f38ts_f38_turnaround_signature_compz504_504d_base_v113_signal(grossmargin, fcf, netinc):
    a = _z(_f38_margin_floor_gap(grossmargin, 504), 252)
    b = _z(_f38_fcf_cross(fcf, 504), 252)
    c = _z(_f38_loss_narrow(netinc, 504), 252)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# paydown acceleration z-scored with revenue holding
def f38ts_f38_turnaround_signature_paydownaccz_252d_base_v114_signal(debt, revenue):
    accel = -(debt.diff(63) - debt.diff(63).shift(63)) / _mean(debt, 252).replace(0, np.nan)
    rhold = (revenue >= _mean(revenue, 252)).astype(float)
    result = _z(accel, 252) * (0.5 + 0.5 * rhold)
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin recovery momentum (change over a quarter), smoothed
def f38ts_f38_turnaround_signature_nmrecmom_252d_base_v115_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    rec = nm - _rmin(nm, 252)
    result = (rec - rec.shift(63)).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# margin off-floor x revenue-trough recovery (top + bottom line turn)
def f38ts_f38_turnaround_signature_dualturn_252d_base_v116_signal(grossmargin, revenue):
    ml = _f38_margin_floor_gap(grossmargin, 252)
    rr = np.tanh(_f38_recover_off_low(revenue, 252))
    result = ml * rr
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-trough cash confirmation, ranked
def f38ts_f38_turnaround_signature_revcashrnk_252d_base_v117_signal(revenue, ncfo):
    rr = _f38_recover_off_low(revenue, 252)
    cm = ncfo / revenue.replace(0, np.nan)
    result = _rank(rr, 504) * (0.5 + np.tanh(cm))
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing slope smoothed by revenue, deeper window
def f38ts_f38_turnaround_signature_lossslp504_504d_base_v118_signal(netinc, revenue):
    sl = _slope(netinc, 252) / _mean(revenue, 504).replace(0, np.nan)
    result = sl.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# bs+cash turn slope: deleveraging slope x ncfo recovery
def f38ts_f38_turnaround_signature_bscashslp_504d_base_v119_signal(debt, ncfo):
    dsl = np.tanh(-_slope(debt, 252) / _mean(debt, 504).replace(0, np.nan) * 100.0)
    cr = _f38_fcf_cross(ncfo, 504)
    result = dsl * (0.5 + cr)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit growth turn off trough, ranked
def f38ts_f38_turnaround_signature_gpgrowthrnk_252d_base_v120_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    g = gp.pct_change(63)
    result = _rank(g - _rmin(g, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# distress-quality composite z (positive ncfo, narrowing loss, deleveraging)
def f38ts_f38_turnaround_signature_distqualz_252d_base_v121_signal(ncfo, netinc, debt):
    s1 = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    s2 = _f38_loss_narrow(netinc, 252)
    s3 = _f38_delever(debt, 252)
    raw = (s1 + s2 + s3) / 3.0
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# equity/debt solvency inflection ranked
def f38ts_f38_turnaround_signature_eqdebtrnk_252d_base_v122_signal(equity, debt):
    r = equity / debt.replace(0, np.nan)
    result = _rank(r - _rmin(r, 252), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin slope from negative base ranked
def f38ts_f38_turnaround_signature_fcfmargrnk_252d_base_v123_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    sl = _slope(fm, 252)
    neg = (fm < 0).astype(float)
    result = _rank(sl, 504) * (0.5 + neg)
    return result.replace([np.inf, -np.inf], np.nan)


# all-engine composite, deeper 504d window, smoothed
def f38ts_f38_turnaround_signature_allengine504_504d_base_v124_signal(grossmargin, fcf, debt, revenue, netinc):
    a = _f38_margin_floor_gap(grossmargin, 504)
    b = _f38_fcf_cross(fcf, 504)
    c = _f38_delever(debt, 504)
    d = np.tanh(_f38_rev_stab(revenue, 252))
    e = _f38_loss_narrow(netinc, 504)
    result = ((a + b + c + d + e) / 5.0).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash margin turn off-floor, z-scored
def f38ts_f38_turnaround_signature_ncfomargz_252d_base_v125_signal(ncfo, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    rec = cm - _rmin(cm, 252)
    result = _z(rec, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround momentum of all-engine composite (change over a quarter)
def f38ts_f38_turnaround_signature_allenginemom_252d_base_v126_signal(grossmargin, fcf, debt, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(fcf, 252)
    c = _f38_delever(debt, 252)
    e = _f38_loss_narrow(netinc, 252)
    comp = (a + b + c + e) / 4.0
    result = comp - comp.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# margin lift x deleveraging interaction, sign-magnitude
def f38ts_f38_turnaround_signature_mlxdelev_504d_base_v127_signal(grossmargin, debt):
    ml = _f38_margin_floor_gap(grossmargin, 504) - 0.5
    dl = _f38_delever(debt, 504) - 0.3
    prod = ml * dl
    result = np.sign(prod) * (prod.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF emergence z minus netinc emergence z (cash-first recovery)
def f38ts_f38_turnaround_signature_cashfirst_252d_base_v128_signal(fcf, netinc):
    fr = _z(_f38_fcf_cross(fcf, 252), 126)
    nr = _z(_f38_loss_narrow(netinc, 252), 126)
    result = fr - nr
    return result.replace([np.inf, -np.inf], np.nan)


# distress depth fade slope (how fast netinc climbs from worst)
def f38ts_f38_turnaround_signature_distfadeslp_504d_base_v129_signal(netinc, equity):
    climb = (netinc - _rmin(netinc, 504)) / _mean(equity.abs(), 252).replace(0, np.nan)
    result = _slope(climb, 126) + np.tanh(climb)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue re-acceleration off trough x positive cash, ranked
def f38ts_f38_turnaround_signature_revaccelrnk_252d_base_v130_signal(revenue, fcf):
    rg = revenue.pct_change(63)
    rl = rg - _rmin(rg, 252)
    fc = (fcf > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _rank(rl, 504) * (0.5 + fc)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-and-loss twin fade slope
def f38ts_f38_turnaround_signature_twinfadeslp_252d_base_v131_signal(debt, equity, netinc):
    lev = debt / equity.replace(0, np.nan)
    levfade = _z(-_slope(lev, 126), 252)
    nirise = _z(_slope(netinc, 126), 252)
    result = (levfade + nirise) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# margin floor depth (how deep the trough was) x current lift, ranked
def f38ts_f38_turnaround_signature_floordepthrnk_504d_base_v132_signal(grossmargin, revenue):
    lo = _rmin(grossmargin, 504)
    depth = (_mean(grossmargin, 504) - lo).clip(lower=0)
    lift = grossmargin - lo
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = _rank(lift * depth * w, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-earnings reconvergence (ncfo recover minus netinc recover), z
def f38ts_f38_turnaround_signature_reconvergz_252d_base_v133_signal(ncfo, netinc):
    cr = _z(np.tanh(_f38_recover_off_low(ncfo, 252)), 126)
    nr = _z(np.tanh(_f38_recover_off_low(netinc, 252)), 126)
    result = cr - nr
    return result.replace([np.inf, -np.inf], np.nan)


# net-income improvement hit-rate minus deterioration (asymmetry)
def f38ts_f38_turnaround_signature_niasym_252d_base_v134_signal(netinc, revenue):
    d = netinc.diff(21)
    up = (d > 0).astype(float).rolling(252, min_periods=126).mean()
    dn = (d < 0).astype(float).rolling(252, min_periods=126).mean()
    distress = (netinc < _mean(netinc, 504)).astype(float)
    result = (up - dn) * (0.5 + distress)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF yield-on-equity recovery slope z
def f38ts_f38_turnaround_signature_fcfyldslpz_252d_base_v135_signal(fcf, equity):
    yld = fcf / equity.replace(0, np.nan)
    result = _z(_slope(yld, 126), 252) + np.tanh(yld - _rmin(yld, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# debt/revenue heal slope (leverage intensity falling)
def f38ts_f38_turnaround_signature_debtrevslp_252d_base_v136_signal(debt, revenue):
    ratio = debt / revenue.replace(0, np.nan)
    result = -_slope(ratio, 252) / _mean(ratio, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-inflection convexity ranked (off-low acceleration)
def f38ts_f38_turnaround_signature_mconvexrnk_252d_base_v137_signal(grossmargin, revenue):
    acc = grossmargin.diff(63) - grossmargin.diff(63).shift(63)
    below = (grossmargin < _mean(grossmargin, 252)).astype(float)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = _rank(acc * (0.5 + below) * w, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF convexity from trough, z-scored
def f38ts_f38_turnaround_signature_fcfconvexz_252d_base_v138_signal(fcf, equity):
    acc = (fcf.diff(63) - fcf.diff(63).shift(63)) / _mean(equity.abs(), 252).replace(0, np.nan)
    neg = (fcf < 0).astype(float)
    result = _z(acc, 126) * (0.5 + neg)
    return result.replace([np.inf, -np.inf], np.nan)


# self-funded deleveraging: ncfo/debt rising off floor, smoothed
def f38ts_f38_turnaround_signature_ncfodebtturn_252d_base_v139_signal(ncfo, debt):
    cov = ncfo / debt.replace(0, np.nan)
    rec = cov - _rmin(cov, 252)
    result = rec.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# equity rebuild slope from low, ranked, with cash gate
def f38ts_f38_turnaround_signature_eqrebuildrnk_252d_base_v140_signal(equity, fcf):
    sl = _slope(equity, 252) / _mean(equity.abs(), 252).replace(0, np.nan)
    fc = (fcf > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _rank(sl, 504) * (0.5 + fc)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-quality twin slope (gross margin & ncfo both rising) product
def f38ts_f38_turnaround_signature_mqtwinslp_252d_base_v141_signal(grossmargin, ncfo):
    msl = np.tanh(80.0 * _slope(grossmargin, 252))
    csl = np.tanh(_slope(ncfo, 252) / _mean(ncfo.abs(), 252).replace(0, np.nan))
    result = (msl + csl) / 2.0 + msl * csl
    return result.replace([np.inf, -np.inf], np.nan)


# recovery composite cross-time rank (overall turnaround percentile)
def f38ts_f38_turnaround_signature_recovrnk_252d_base_v142_signal(grossmargin, fcf, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(fcf, 252)
    c = _f38_loss_narrow(netinc, 252)
    comp = (a + b + c) / 3.0
    result = _rank(comp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt-to-equity decline x revenue stability, deeper window
def f38ts_f38_turnaround_signature_ndestab_504d_base_v143_signal(debt, equity, revenue):
    lev = debt / equity.replace(0, np.nan)
    decl = (_rmax(lev, 504) - lev) / (_rmax(lev, 504).abs() + 1.0)
    stab = np.tanh(_f38_rev_stab(revenue, 252))
    result = decl * (0.5 + stab)
    return result.replace([np.inf, -np.inf], np.nan)


# loss-to-profit climb fraction of span, fcf-confirmed, z
def f38ts_f38_turnaround_signature_l2pclimbz_504d_base_v144_signal(netinc, fcf):
    worst = _rmin(netinc, 504)
    span = (_rmax(netinc, 504) - worst).replace(0, np.nan)
    climb = (netinc - worst) / span
    fc = _f38_fcf_cross(fcf, 504)
    result = _z(climb * (0.5 + fc.clip(lower=-0.5)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin lift minus debt/equity rise (profit improving faster than leverage)
def f38ts_f38_turnaround_signature_mlminuslev_252d_base_v145_signal(grossmargin, debt, equity):
    ml = _z(_f38_margin_floor_gap(grossmargin, 252), 126)
    lev = debt / equity.replace(0, np.nan)
    levz = _z(lev - _rmin(lev, 252), 126)
    result = ml - levz
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash slope from trough, revenue-weighted, smoothed
def f38ts_f38_turnaround_signature_ncfoslpsm_252d_base_v146_signal(ncfo, revenue):
    sl = _slope(ncfo, 252) / _mean(revenue, 252).replace(0, np.nan)
    result = sl.ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# margin floor gap minus its slow EMA (fresh margin displacement)
def f38ts_f38_turnaround_signature_mldisplace_252d_base_v147_signal(grossmargin, revenue):
    ml = _f38_margin_floor_gap(grossmargin, 252)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    base = (ml * w)
    result = base - base.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# composite of three slopes minus their dispersion (broad clean turn)
def f38ts_f38_turnaround_signature_cleanturn_252d_base_v148_signal(grossmargin, fcf, debt):
    a = _z(_slope(grossmargin, 252), 252)
    b = _z(_slope(fcf, 252), 252)
    c = _z(-_slope(debt, 252), 252)
    stk = pd.concat([a, b, c], axis=1)
    result = stk.mean(axis=1) - stk.std(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-power recovery: netinc/revenue z minus its trough z
def f38ts_f38_turnaround_signature_epowerrec_252d_base_v149_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    znow = _z(nm, 126)
    result = znow - _rmin(znow, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# grand turnaround signature: z-blend of margin, cash, leverage, earnings recovery
def f38ts_f38_turnaround_signature_grandsig_252d_base_v150_signal(grossmargin, ncfo, debt, netinc):
    a = _z(_f38_margin_floor_gap(grossmargin, 252), 126)
    b = _z(_f38_fcf_cross(ncfo, 252), 126)
    c = _z(_f38_delever(debt, 252), 126)
    d = _z(_f38_loss_narrow(netinc, 252), 126)
    blend = (a + b + c + d) / 4.0
    result = np.tanh(blend) * (1.0 + 0.25 * _rank(blend, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38ts_f38_turnaround_signature_mliftewm_252d_base_v076_signal,
    f38ts_f38_turnaround_signature_mliftsnr_252d_base_v077_signal,
    f38ts_f38_turnaround_signature_maccel_252d_base_v078_signal,
    f38ts_f38_turnaround_signature_mliftrank_252d_base_v079_signal,
    f38ts_f38_turnaround_signature_nirecovz_252d_base_v080_signal,
    f38ts_f38_turnaround_signature_lossslopernk_252d_base_v081_signal,
    f38ts_f38_turnaround_signature_niconvex_252d_base_v082_signal,
    f38ts_f38_turnaround_signature_nihitdepth_252d_base_v083_signal,
    f38ts_f38_turnaround_signature_fcfcrossz_252d_base_v084_signal,
    f38ts_f38_turnaround_signature_fcfshareturn_252d_base_v085_signal,
    f38ts_f38_turnaround_signature_fcfmargslp_252d_base_v086_signal,
    f38ts_f38_turnaround_signature_ncfocrossrnk_252d_base_v087_signal,
    f38ts_f38_turnaround_signature_ncforecsnr_252d_base_v088_signal,
    f38ts_f38_turnaround_signature_delevslopez_252d_base_v089_signal,
    f38ts_f38_turnaround_signature_delevema_504d_base_v090_signal,
    f38ts_f38_turnaround_signature_levdeclrnk_252d_base_v091_signal,
    f38ts_f38_turnaround_signature_netdebtturn_252d_base_v092_signal,
    f38ts_f38_turnaround_signature_revturnslope_252d_base_v093_signal,
    f38ts_f38_turnaround_signature_revstabturn_252d_base_v094_signal,
    f38ts_f38_turnaround_signature_slopecomp_252d_base_v095_signal,
    f38ts_f38_turnaround_signature_offlowdisp_252d_base_v096_signal,
    f38ts_f38_turnaround_signature_qualconvslp_252d_base_v097_signal,
    f38ts_f38_turnaround_signature_earlyturnrnk_252d_base_v098_signal,
    f38ts_f38_turnaround_signature_roacaprec_252d_base_v099_signal,
    f38ts_f38_turnaround_signature_roeslprnk_252d_base_v100_signal,
    f38ts_f38_turnaround_signature_marglead_252d_base_v101_signal,
    f38ts_f38_turnaround_signature_cashleadslp_252d_base_v102_signal,
    f38ts_f38_turnaround_signature_bstiming_252d_base_v103_signal,
    f38ts_f38_turnaround_signature_breakevenslp_252d_base_v104_signal,
    f38ts_f38_turnaround_signature_distexitz_252d_base_v105_signal,
    f38ts_f38_turnaround_signature_breadthdisp_252d_base_v106_signal,
    f38ts_f38_turnaround_signature_gpdollslp_252d_base_v107_signal,
    f38ts_f38_turnaround_signature_selffundrnk_252d_base_v108_signal,
    f38ts_f38_turnaround_signature_bshealslp_504d_base_v109_signal,
    f38ts_f38_turnaround_signature_accrualslp_252d_base_v110_signal,
    f38ts_f38_turnaround_signature_durturnrnk_252d_base_v111_signal,
    f38ts_f38_turnaround_signature_fcfdebtrnk_252d_base_v112_signal,
    f38ts_f38_turnaround_signature_compz504_504d_base_v113_signal,
    f38ts_f38_turnaround_signature_paydownaccz_252d_base_v114_signal,
    f38ts_f38_turnaround_signature_nmrecmom_252d_base_v115_signal,
    f38ts_f38_turnaround_signature_dualturn_252d_base_v116_signal,
    f38ts_f38_turnaround_signature_revcashrnk_252d_base_v117_signal,
    f38ts_f38_turnaround_signature_lossslp504_504d_base_v118_signal,
    f38ts_f38_turnaround_signature_bscashslp_504d_base_v119_signal,
    f38ts_f38_turnaround_signature_gpgrowthrnk_252d_base_v120_signal,
    f38ts_f38_turnaround_signature_distqualz_252d_base_v121_signal,
    f38ts_f38_turnaround_signature_eqdebtrnk_252d_base_v122_signal,
    f38ts_f38_turnaround_signature_fcfmargrnk_252d_base_v123_signal,
    f38ts_f38_turnaround_signature_allengine504_504d_base_v124_signal,
    f38ts_f38_turnaround_signature_ncfomargz_252d_base_v125_signal,
    f38ts_f38_turnaround_signature_allenginemom_252d_base_v126_signal,
    f38ts_f38_turnaround_signature_mlxdelev_504d_base_v127_signal,
    f38ts_f38_turnaround_signature_cashfirst_252d_base_v128_signal,
    f38ts_f38_turnaround_signature_distfadeslp_504d_base_v129_signal,
    f38ts_f38_turnaround_signature_revaccelrnk_252d_base_v130_signal,
    f38ts_f38_turnaround_signature_twinfadeslp_252d_base_v131_signal,
    f38ts_f38_turnaround_signature_floordepthrnk_504d_base_v132_signal,
    f38ts_f38_turnaround_signature_reconvergz_252d_base_v133_signal,
    f38ts_f38_turnaround_signature_niasym_252d_base_v134_signal,
    f38ts_f38_turnaround_signature_fcfyldslpz_252d_base_v135_signal,
    f38ts_f38_turnaround_signature_debtrevslp_252d_base_v136_signal,
    f38ts_f38_turnaround_signature_mconvexrnk_252d_base_v137_signal,
    f38ts_f38_turnaround_signature_fcfconvexz_252d_base_v138_signal,
    f38ts_f38_turnaround_signature_ncfodebtturn_252d_base_v139_signal,
    f38ts_f38_turnaround_signature_eqrebuildrnk_252d_base_v140_signal,
    f38ts_f38_turnaround_signature_mqtwinslp_252d_base_v141_signal,
    f38ts_f38_turnaround_signature_recovrnk_252d_base_v142_signal,
    f38ts_f38_turnaround_signature_ndestab_504d_base_v143_signal,
    f38ts_f38_turnaround_signature_l2pclimbz_504d_base_v144_signal,
    f38ts_f38_turnaround_signature_mlminuslev_252d_base_v145_signal,
    f38ts_f38_turnaround_signature_ncfoslpsm_252d_base_v146_signal,
    f38ts_f38_turnaround_signature_mldisplace_252d_base_v147_signal,
    f38ts_f38_turnaround_signature_cleanturn_252d_base_v148_signal,
    f38ts_f38_turnaround_signature_epowerrec_252d_base_v149_signal,
    f38ts_f38_turnaround_signature_grandsig_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_TURNAROUND_SIGNATURE_REGISTRY_076_150 = REGISTRY


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

    netinc = _fund(101, base=6e7, drift=0.03, vol=0.16, allow_neg=True, n=n).rename("netinc")
    grossmargin = _fund(102, base=0.35, drift=0.005, vol=0.05, allow_neg=False, n=n).rename("grossmargin")
    revenue = _fund(103, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=n).rename("revenue")
    debt = _fund(104, base=8e7, drift=-0.01, vol=0.06, allow_neg=False, n=n).rename("debt")
    fcf = _fund(105, base=5e7, drift=0.03, vol=0.18, allow_neg=True, n=n).rename("fcf")
    equity = _fund(106, base=1.2e8, drift=0.015, vol=0.05, allow_neg=True, n=n).rename("equity")
    ncfo = _fund(107, base=7e7, drift=0.025, vol=0.13, allow_neg=True, n=n).rename("ncfo")

    cols = {"netinc": netinc, "grossmargin": grossmargin, "revenue": revenue,
            "debt": debt, "fcf": fcf, "equity": equity, "ncfo": ncfo}

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

    print("OK f38_turnaround_signature_base_076_150_claude: %d features pass" % n_features)
