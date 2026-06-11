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


def _slope(s, w):
    # ordinary least-squares slope of s over a trailing window (per-step)
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
    # how far current margin sits above its trailing-low base (off-the-floor lift)
    lo = _rmin(grossmargin, w)
    return (grossmargin - lo) / (grossmargin.abs() + lo.abs()).replace(0, np.nan)


def _f38_loss_narrow(netinc, w):
    # loss narrowing toward zero: rising netinc when starting from a depressed base
    base = _rmin(netinc, w)
    return (netinc - base) / (netinc.abs() + base.abs() + 1.0)


def _f38_fcf_cross(fcf, w):
    # return-to-positive-FCF: signed recovery from the trailing FCF trough
    lo = _rmin(fcf, w)
    return (fcf - lo) / (fcf.abs() + lo.abs()).replace(0, np.nan)


def _f38_delever(debt, w):
    # deleveraging: debt falling off its trailing peak
    hi = _rmax(debt, w)
    return (hi - debt) / hi.replace(0, np.nan)


def _f38_rev_stab(revenue, w):
    # revenue stabilization: inverse coefficient of variation of growth
    g = revenue.pct_change()
    return _mean(g, w) / (_std(g, w).replace(0, np.nan))


def _f38_recover_off_low(s, w):
    # generic recovery ratio off a trailing low for any series
    lo = _rmin(s, w)
    return s / lo.replace(0, np.nan) - 1.0


# ============================================================
# margin inflection: gross margin lift off its 252d floor
def f38ts_f38_turnaround_signature_mfloorgap_252d_base_v001_signal(grossmargin, revenue):
    lift = _f38_margin_floor_gap(grossmargin, 252)
    scale = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = lift * scale
    return result.replace([np.inf, -np.inf], np.nan)


# margin inflection 504d floor, scaled by deleveraging
def f38ts_f38_turnaround_signature_mfloorgap_504d_base_v002_signal(grossmargin, debt):
    lift = _f38_margin_floor_gap(grossmargin, 504)
    dl = _f38_delever(debt, 504)
    result = lift + 0.5 * dl
    return result.replace([np.inf, -np.inf], np.nan)


# gross margin minus its trailing-min margin, in revenue-weighted form
def f38ts_f38_turnaround_signature_mlift_126d_base_v003_signal(grossmargin, revenue):
    lo = _rmin(grossmargin, 126)
    lift = grossmargin - lo
    w = revenue / _rmax(revenue, 126).replace(0, np.nan)
    result = lift * w
    return result.replace([np.inf, -np.inf], np.nan)


# margin acceleration off base: current vs floor, multiplied by ncfo recovery
def f38ts_f38_turnaround_signature_mliftcash_252d_base_v004_signal(grossmargin, ncfo):
    lift = _f38_margin_floor_gap(grossmargin, 252)
    cash = _f38_recover_off_low(ncfo, 252)
    result = lift * np.sign(cash) * (cash.abs() ** 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# margin z-score combined with positive-equity stabilization
def f38ts_f38_turnaround_signature_mz_252d_base_v005_signal(grossmargin, equity):
    mz = _z(grossmargin, 252)
    eq = equity / _mean(equity, 252).replace(0, np.nan)
    result = mz * eq.clip(lower=0)
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing: netinc rising toward zero off its 252d trough, revenue-scaled
def f38ts_f38_turnaround_signature_lossnarrow_252d_base_v006_signal(netinc, revenue):
    ln = _f38_loss_narrow(netinc, 252)
    margin = netinc / revenue.replace(0, np.nan)
    result = ln * (1.0 - np.tanh(5.0 * margin))
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing 504d, interacted with FCF recovery
def f38ts_f38_turnaround_signature_lossnarrow_504d_base_v007_signal(netinc, fcf):
    ln = _f38_loss_narrow(netinc, 504)
    fc = _f38_fcf_cross(fcf, 504)
    result = ln * (1.0 + fc)
    return result.replace([np.inf, -np.inf], np.nan)


# loss narrowing slope: regression slope of netinc when below zero
def f38ts_f38_turnaround_signature_lossslope_126d_base_v008_signal(netinc, equity):
    sl = _slope(netinc, 126)
    norm = _mean(equity, 126).replace(0, np.nan)
    distress = (netinc < 0).astype(float)
    result = (sl / norm) * (0.5 + distress)
    return result.replace([np.inf, -np.inf], np.nan)


# netinc trough recovery ratio combined with revenue stabilization
def f38ts_f38_turnaround_signature_nirecov_252d_base_v009_signal(netinc, revenue):
    lo = _rmin(netinc, 252)
    recov = (netinc - lo) / (lo.abs() + 1.0)
    stab = _f38_rev_stab(revenue, 252)
    result = recov * np.tanh(stab)
    return result.replace([np.inf, -np.inf], np.nan)


# return-to-positive-FCF crossing strength, equity-normalized
def f38ts_f38_turnaround_signature_fcfcross_252d_base_v010_signal(fcf, equity):
    cr = _f38_fcf_cross(fcf, 252)
    lvl = fcf / _mean(equity, 252).replace(0, np.nan)
    result = cr + np.tanh(lvl)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF crossing 504d, weighted by revenue trend
def f38ts_f38_turnaround_signature_fcfcross_504d_base_v011_signal(fcf, revenue):
    cr = _f38_fcf_cross(fcf, 504)
    rt = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = cr * rt
    return result.replace([np.inf, -np.inf], np.nan)


# positive-FCF streak fraction change (cash-positivity broadening) x margin slope
def f38ts_f38_turnaround_signature_fcfstreak_252d_base_v012_signal(fcf, grossmargin):
    pos = (fcf > 0).astype(float)
    streak = pos.rolling(252, min_periods=126).mean()
    broaden = streak - streak.shift(63)
    msl = _slope(grossmargin, 126)
    result = broaden + np.tanh(50.0 * msl)
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin recovery: fcf/revenue minus its trailing min
def f38ts_f38_turnaround_signature_fcfmargrec_252d_base_v013_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    lo = _rmin(fm, 252)
    result = fm - lo
    return result.replace([np.inf, -np.inf], np.nan)


# ncfo return-to-positive crossing, scaled by deleveraging
def f38ts_f38_turnaround_signature_ncforec_252d_base_v014_signal(ncfo, debt):
    cr = _f38_fcf_cross(ncfo, 252)
    dl = _f38_delever(debt, 252)
    result = cr * (0.5 + dl)
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging with stabilizing revenue: debt off peak x revenue inverse-CV
def f38ts_f38_turnaround_signature_delevstab_252d_base_v015_signal(debt, revenue):
    dl = _f38_delever(debt, 252)
    stab = _f38_rev_stab(revenue, 252)
    result = dl * np.tanh(stab)
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging 504d combined with equity rebuild
def f38ts_f38_turnaround_signature_delevstab_504d_base_v016_signal(debt, equity):
    dl = _f38_delever(debt, 504)
    eqrec = _f38_recover_off_low(equity, 504)
    result = dl + 0.5 * np.tanh(eqrec)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt to equity falling: leverage improvement off its trailing peak
def f38ts_f38_turnaround_signature_levimprove_252d_base_v017_signal(debt, equity):
    lev = debt / equity.replace(0, np.nan)
    hi = _rmax(lev, 252)
    result = (hi - lev) / (hi.abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown streak fraction times revenue stability
def f38ts_f38_turnaround_signature_paydownstreak_252d_base_v018_signal(debt, revenue):
    down = (debt.diff() < 0).astype(float)
    streak = down.rolling(252, min_periods=126).mean()
    rt = revenue / _mean(revenue, 126).replace(0, np.nan)
    result = streak * rt
    return result.replace([np.inf, -np.inf], np.nan)


# revenue stabilization (rising inverse-CV rank) gating netinc slope sign
def f38ts_f38_turnaround_signature_twinrev_252d_base_v019_signal(revenue, netinc):
    stab = _f38_rev_stab(revenue, 252)
    stab_rank = stab.rolling(252, min_periods=126).rank(pct=True) - 0.5
    nsl = _slope(netinc, 126) / _mean(netinc.abs(), 252).replace(0, np.nan)
    result = stab_rank * np.sign(nsl) + 0.3 * np.tanh(nsl)
    return result.replace([np.inf, -np.inf], np.nan)


# recovery composite: margin lift + FCF cross + loss narrowing (equal blend)
def f38ts_f38_turnaround_signature_recovcomp_252d_base_v020_signal(grossmargin, fcf, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(fcf, 252)
    c = _f38_loss_narrow(netinc, 252)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# recovery composite weighted by deleveraging
def f38ts_f38_turnaround_signature_recovcomp_504d_base_v021_signal(grossmargin, ncfo, debt):
    a = _f38_margin_floor_gap(grossmargin, 504)
    b = _f38_fcf_cross(ncfo, 504)
    dl = _f38_delever(debt, 504)
    result = (a + b) * (0.5 + dl)
    return result.replace([np.inf, -np.inf], np.nan)


# improving quality from distress: ncfo/netinc conversion rising off low
def f38ts_f38_turnaround_signature_qualconv_252d_base_v022_signal(ncfo, netinc):
    conv = ncfo / (netinc.abs() + 1.0)
    lo = _rmin(conv, 252)
    result = conv - lo
    return result.replace([np.inf, -np.inf], np.nan)


# distress-quality: positive ncfo while netinc still negative (early turn)
def f38ts_f38_turnaround_signature_earlyturn_252d_base_v023_signal(ncfo, netinc):
    early = ((ncfo > 0) & (netinc < 0)).astype(float)
    frac = early.rolling(252, min_periods=126).mean()
    intensity = (ncfo / (ncfo.abs() + netinc.abs() + 1.0))
    result = frac + 0.5 * intensity
    return result.replace([np.inf, -np.inf], np.nan)


# ROE recovery off its trailing trough (return on equity inflection)
def f38ts_f38_turnaround_signature_roerec_252d_base_v024_signal(netinc, equity):
    roe = netinc / equity.replace(0, np.nan)
    lo = _rmin(roe, 252)
    result = (roe - lo) / (roe.abs() + lo.abs() + 0.01)
    return result.replace([np.inf, -np.inf], np.nan)


# ROE recovery 504d interacted with margin lift
def f38ts_f38_turnaround_signature_roerec_504d_base_v025_signal(netinc, equity, grossmargin):
    roe = netinc / equity.replace(0, np.nan)
    lo = _rmin(roe, 504)
    rec = roe - lo
    ml = _f38_margin_floor_gap(grossmargin, 252)
    result = rec * (0.5 + ml)
    return result.replace([np.inf, -np.inf], np.nan)


# margin trend slope while gross margin is depressed (off-base direction)
def f38ts_f38_turnaround_signature_mslope_252d_base_v026_signal(grossmargin, revenue):
    sl = _slope(grossmargin, 252)
    depressed = (grossmargin < _mean(grossmargin, 504)).astype(float)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = sl * (0.5 + depressed) * w
    return result.replace([np.inf, -np.inf], np.nan)


# FCF slope from a negative base (cash inflection direction)
def f38ts_f38_turnaround_signature_fcfslope_252d_base_v027_signal(fcf, revenue):
    sl = _slope(fcf, 252)
    norm = _mean(revenue, 252).replace(0, np.nan)
    neg = (fcf < 0).astype(float)
    result = (sl / norm) * (0.5 + neg)
    return result.replace([np.inf, -np.inf], np.nan)


# debt slope (negative = deleveraging) scaled by revenue stability
def f38ts_f38_turnaround_signature_debtslope_252d_base_v028_signal(debt, revenue):
    sl = _slope(debt, 252)
    norm = _mean(debt, 252).replace(0, np.nan)
    stab = _f38_rev_stab(revenue, 252)
    result = (-sl / norm) * np.tanh(stab)
    return result.replace([np.inf, -np.inf], np.nan)


# equity rebuild slope from a low base
def f38ts_f38_turnaround_signature_eqslope_252d_base_v029_signal(equity, revenue):
    sl = _slope(equity, 252)
    norm = _mean(revenue, 252).replace(0, np.nan)
    low = (equity < _mean(equity, 504)).astype(float)
    result = (sl / norm) * (0.5 + low)
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin crossing momentum: change in distance-above-floor over a month
def f38ts_f38_turnaround_signature_nmcross_252d_base_v030_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    lift = nm - _rmin(nm, 252)
    result = lift - lift.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# composite distress-exit score: weighted positives across five engines
def f38ts_f38_turnaround_signature_distexit_252d_base_v031_signal(netinc, fcf, debt, grossmargin):
    s1 = (netinc.diff(63) > 0).astype(float)
    s2 = (fcf > 0).astype(float)
    s3 = (debt.diff(63) < 0).astype(float)
    s4 = (grossmargin.diff(63) > 0).astype(float)
    raw = (s1 + s2 + s3 + s4).rolling(252, min_periods=126).mean()
    result = raw - 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround breadth: fraction of engines improving over the quarter
def f38ts_f38_turnaround_signature_breadth_252d_base_v032_signal(grossmargin, ncfo, equity):
    s1 = (grossmargin.diff(63) > 0).astype(float)
    s2 = (ncfo.diff(63) > 0).astype(float)
    s3 = (equity.diff(63) > 0).astype(float)
    result = (s1 + s2 + s3).rolling(126, min_periods=63).mean() - 1.5
    return result.replace([np.inf, -np.inf], np.nan)


# margin-inflection convexity: second-difference of gross margin off low
def f38ts_f38_turnaround_signature_mconvex_252d_base_v033_signal(grossmargin, revenue):
    accel = grossmargin.diff(63) - grossmargin.diff(63).shift(63)
    below = (grossmargin < _mean(grossmargin, 252)).astype(float)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = accel * (0.5 + below) * w
    return result.replace([np.inf, -np.inf], np.nan)


# FCF inflection convexity from a trough
def f38ts_f38_turnaround_signature_fcfconvex_252d_base_v034_signal(fcf, equity):
    accel = fcf.diff(63) - fcf.diff(63).shift(63)
    norm = _mean(equity, 252).replace(0, np.nan)
    neg = (fcf < 0).astype(float)
    result = (accel / norm) * (0.5 + neg)
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging combined with FCF turning positive (debt-paydown fuel)
def f38ts_f38_turnaround_signature_delevfcf_252d_base_v035_signal(debt, fcf):
    dl = _f38_delever(debt, 252)
    fc = _f38_fcf_cross(fcf, 252)
    result = dl * (fc > 0).astype(float) + 0.5 * dl
    return result.replace([np.inf, -np.inf], np.nan)


# revenue base stabilization with margin off-floor (top-line + profitability turn)
def f38ts_f38_turnaround_signature_revmargturn_252d_base_v036_signal(revenue, grossmargin):
    rg = revenue / _rmin(revenue, 252).replace(0, np.nan) - 1.0
    ml = _f38_margin_floor_gap(grossmargin, 252)
    result = np.tanh(rg) * ml
    return result.replace([np.inf, -np.inf], np.nan)


# capital structure heal: equity rising while debt falls (twin balance-sheet turn)
def f38ts_f38_turnaround_signature_bsheal_504d_base_v037_signal(equity, debt):
    eqrec = _f38_recover_off_low(equity, 504)
    dl = _f38_delever(debt, 504)
    result = np.tanh(eqrec) + dl
    return result.replace([np.inf, -np.inf], np.nan)


# cash-vs-earnings reconvergence: ncfo recovering faster than netinc deteriorated
def f38ts_f38_turnaround_signature_cashlead_252d_base_v038_signal(ncfo, netinc):
    cr = _f38_recover_off_low(ncfo, 252)
    nr = _f38_recover_off_low(netinc, 252)
    result = np.tanh(cr) - np.tanh(nr)
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing hit-rate: fraction of quarters with rising netinc off a low base
def f38ts_f38_turnaround_signature_nihitrate_252d_base_v039_signal(netinc, revenue):
    up = (netinc.diff(21) > 0).astype(float)
    hr = up.rolling(252, min_periods=126).mean()
    depressed = (netinc < 0).astype(float).rolling(252, min_periods=126).mean()
    result = hr * (0.5 + depressed)
    return result.replace([np.inf, -np.inf], np.nan)


# margin lift dispersion: how broadly margin has lifted across the window
def f38ts_f38_turnaround_signature_mliftdisp_252d_base_v040_signal(grossmargin, revenue):
    lift = grossmargin - _rmin(grossmargin, 252)
    disp = lift.rolling(126, min_periods=63).std()
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = _mean(lift, 63) / disp.replace(0, np.nan) * w
    return result.replace([np.inf, -np.inf], np.nan)


# FCF yield on equity recovery, percentile-ranked vs own history
def f38ts_f38_turnaround_signature_fcfyldrec_252d_base_v041_signal(fcf, equity):
    yld = fcf / equity.replace(0, np.nan)
    rec = yld - _rmin(yld, 252)
    result = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround momentum: change in the recovery composite over a quarter
def f38ts_f38_turnaround_signature_recovmom_252d_base_v042_signal(grossmargin, fcf, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(fcf, 252)
    c = _f38_loss_narrow(netinc, 252)
    comp = (a + b + c) / 3.0
    result = comp - comp.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/revenue (leverage intensity) rolling off its peak
def f38ts_f38_turnaround_signature_debtrevheal_252d_base_v043_signal(debt, revenue):
    ratio = debt / revenue.replace(0, np.nan)
    hi = _rmax(ratio, 252)
    result = (hi - ratio) / (hi.abs() + 0.01)
    return result.replace([np.inf, -np.inf], np.nan)


# distress depth fade: how far netinc has climbed from its worst, equity-scaled
def f38ts_f38_turnaround_signature_distfade_504d_base_v044_signal(netinc, equity):
    worst = _rmin(netinc, 504)
    climb = (netinc - worst) / _mean(equity, 252).replace(0, np.nan)
    result = np.tanh(climb)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue re-acceleration off trough together with FCF turning
def f38ts_f38_turnaround_signature_revaccelfcf_252d_base_v045_signal(revenue, fcf):
    rg = revenue.pct_change(63)
    rg_lift = rg - _rmin(rg, 252)
    fc = _f38_fcf_cross(fcf, 252)
    result = rg_lift * (0.5 + fc.clip(lower=0))
    return result.replace([np.inf, -np.inf], np.nan)


# gross-profit-dollars recovery off low (margin x revenue), equity-normalized
def f38ts_f38_turnaround_signature_gpdollrec_252d_base_v046_signal(grossmargin, revenue, equity):
    gp = grossmargin * revenue
    lo = _rmin(gp, 252)
    result = (gp - lo) / _mean(equity, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround persistence: dispersion-scaled co-movement of netinc & fcf recovery
def f38ts_f38_turnaround_signature_persist_252d_base_v047_signal(netinc, fcf):
    nr = (netinc - _rmin(netinc, 252)) / _std(netinc, 252).replace(0, np.nan)
    fr = (fcf - _rmin(fcf, 252)) / _std(fcf, 252).replace(0, np.nan)
    combo = (nr + fr) / 2.0
    result = combo - combo.rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# self-funding turnaround: ncfo covering debt reduction
def f38ts_f38_turnaround_signature_selffund_252d_base_v048_signal(ncfo, debt):
    paydown = (-debt.diff(63)).clip(lower=0)
    cover = ncfo / (paydown + _mean(debt, 252) * 0.01).replace(0, np.nan)
    lo = _rmin(cover, 252)
    result = np.tanh(cover - lo)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-quality turn: gross margin slope confirmed by ncfo slope (twin direction)
def f38ts_f38_turnaround_signature_mqturn_252d_base_v049_signal(grossmargin, ncfo):
    msl = _slope(grossmargin, 252)
    csl = _slope(ncfo, 252) / _mean(ncfo.abs(), 252).replace(0, np.nan)
    result = np.tanh(80.0 * msl) * np.sign(csl) + np.tanh(csl)
    return result.replace([np.inf, -np.inf], np.nan)


# breakeven approach: net margin distance below its own ceiling shrinking
def f38ts_f38_turnaround_signature_breakeven_252d_base_v050_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    ceil = _rmax(nm, 252)
    gap = (ceil - nm)
    result = -(gap - _mean(gap, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# equity-funded recovery: rising equity with positive FCF emerging
def f38ts_f38_turnaround_signature_eqfundrec_252d_base_v051_signal(equity, fcf):
    eqg = equity.pct_change(63)
    fc = (fcf > 0).astype(float).rolling(252, min_periods=126).mean()
    result = np.tanh(eqg) * (0.5 + fc)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage-and-loss twin fade: debt/equity falling while netinc rises
def f38ts_f38_turnaround_signature_twinfade_252d_base_v052_signal(debt, equity, netinc):
    lev = debt / equity.replace(0, np.nan)
    lev_fade = -(lev - lev.shift(63))
    ln = _f38_loss_narrow(netinc, 252)
    result = np.tanh(lev_fade) + ln
    return result.replace([np.inf, -np.inf], np.nan)


# margin floor depth: how depressed margin was, fading (deeper base, bigger turn)
def f38ts_f38_turnaround_signature_floordepth_504d_base_v053_signal(grossmargin, revenue):
    lo = _rmin(grossmargin, 504)
    depth = (_mean(grossmargin, 504) - lo).clip(lower=0)
    now_lift = (grossmargin - lo)
    w = revenue / _mean(revenue, 252).replace(0, np.nan)
    result = now_lift * np.tanh(depth) * w
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion turn: (ncfo - netinc) accrual gap shrinking from distress
def f38ts_f38_turnaround_signature_accrualturn_252d_base_v054_signal(ncfo, netinc, revenue):
    gap = (ncfo - netinc) / revenue.replace(0, np.nan)
    lo = _rmin(gap, 252)
    result = gap - lo
    return result.replace([np.inf, -np.inf], np.nan)


# revenue stability rising while margin lifts (durable turn)
def f38ts_f38_turnaround_signature_durturn_252d_base_v055_signal(revenue, grossmargin):
    stab_now = _f38_rev_stab(revenue, 126)
    stab_lo = _rmin(_f38_rev_stab(revenue, 126), 252)
    ml = _f38_margin_floor_gap(grossmargin, 252)
    result = np.tanh(stab_now - stab_lo) * ml
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-to-debt coverage improving: z-scored slope of coverage ratio
def f38ts_f38_turnaround_signature_fcfdebtcov_252d_base_v056_signal(fcf, debt):
    cov = fcf / debt.replace(0, np.nan)
    sl = _slope(cov, 126)
    result = _z(sl, 252) + np.tanh(5.0 * (cov - _mean(cov, 252)))
    return result.replace([np.inf, -np.inf], np.nan)


# netinc/equity inflection slope (ROE turning), distress-weighted
def f38ts_f38_turnaround_signature_roeslope_252d_base_v057_signal(netinc, equity):
    roe = netinc / equity.replace(0, np.nan)
    sl = _slope(roe, 252)
    neg = (roe < 0).astype(float)
    result = sl * (0.5 + neg)
    return result.replace([np.inf, -np.inf], np.nan)


# composite Z of three recovery engines (margin, fcf, netinc) off-low
def f38ts_f38_turnaround_signature_compz_252d_base_v058_signal(grossmargin, fcf, netinc):
    a = _z(_f38_margin_floor_gap(grossmargin, 252), 126)
    b = _z(_f38_fcf_cross(fcf, 252), 126)
    c = _z(_f38_loss_narrow(netinc, 252), 126)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown acceleration with revenue holding
def f38ts_f38_turnaround_signature_paydownaccel_252d_base_v059_signal(debt, revenue):
    accel = -(debt.diff(63) - debt.diff(63).shift(63))
    norm = _mean(debt, 252).replace(0, np.nan)
    rhold = (revenue >= _mean(revenue, 252)).astype(float)
    result = (accel / norm) * (0.5 + rhold)
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin recovery rank vs own history (cross-time turnaround percentile)
def f38ts_f38_turnaround_signature_nmrank_252d_base_v060_signal(netinc, revenue):
    nm = netinc / revenue.replace(0, np.nan)
    rec = nm - _rmin(nm, 252)
    result = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# FCF emergence vs debt-paydown timing: z-scored fcf slope minus debt slope
def f38ts_f38_turnaround_signature_fcfemergedelev_252d_base_v061_signal(fcf, debt):
    fsl = _z(_slope(fcf, 126), 252)
    dsl = _z(-_slope(debt, 126), 252)
    result = fsl - dsl
    return result.replace([np.inf, -np.inf], np.nan)


# margin off-floor momentum gated by improving solvency (rank of solvency lift)
def f38ts_f38_turnaround_signature_mfloorsolv_252d_base_v062_signal(grossmargin, equity, debt):
    ml = _f38_margin_floor_gap(grossmargin, 252)
    solv = equity / (equity.abs() + debt.abs()).replace(0, np.nan)
    solv_rank = solv.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = (ml - ml.shift(63)) * (0.5 + solv_rank)
    return result.replace([np.inf, -np.inf], np.nan)


# revenue trough recovery with positive cash flow
def f38ts_f38_turnaround_signature_revtroughcash_252d_base_v063_signal(revenue, ncfo):
    rr = _f38_recover_off_low(revenue, 252)
    pos = (ncfo > 0).astype(float)
    result = np.tanh(rr) * (0.5 + pos)
    return result.replace([np.inf, -np.inf], np.nan)


# loss-narrowing slope normalized by revenue, smoothed (clean turn signal)
def f38ts_f38_turnaround_signature_lossslopesm_252d_base_v064_signal(netinc, revenue):
    sl = _slope(netinc, 126)
    norm = _mean(revenue, 252).replace(0, np.nan)
    result = (sl / norm).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# combined balance-sheet & cash turn: deleveraging x ncfo recovery
def f38ts_f38_turnaround_signature_bscashturn_504d_base_v065_signal(debt, ncfo):
    dl = _f38_delever(debt, 504)
    cr = _f38_fcf_cross(ncfo, 504)
    result = dl * (1.0 + cr)
    return result.replace([np.inf, -np.inf], np.nan)


# margin-revenue interaction lift: gross profit growth off trough vs equity
def f38ts_f38_turnaround_signature_gpgrowthturn_252d_base_v066_signal(grossmargin, revenue):
    gp = grossmargin * revenue
    g = gp.pct_change(63)
    glift = g - _rmin(g, 252)
    result = np.tanh(glift)
    return result.replace([np.inf, -np.inf], np.nan)


# distress-quality index: positive ncfo, narrowing loss, deleveraging together
def f38ts_f38_turnaround_signature_distqual_252d_base_v067_signal(ncfo, netinc, debt):
    s1 = (ncfo > 0).astype(float)
    s2 = (netinc.diff(63) > 0).astype(float)
    s3 = (debt.diff(63) < 0).astype(float)
    raw = (s1 + s2 + s3).rolling(126, min_periods=63).mean()
    result = raw - 1.5
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-debt ratio inflection: z-scored slope of the solvency ratio
def f38ts_f38_turnaround_signature_eqdebtturn_252d_base_v068_signal(equity, debt):
    r = equity / debt.replace(0, np.nan)
    sl = _slope(r, 126)
    result = _z(sl, 252) + np.tanh(r - _rmax(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# FCF margin slope off a negative base, revenue-confirmed
def f38ts_f38_turnaround_signature_fcfmargslope_252d_base_v069_signal(fcf, revenue):
    fm = fcf / revenue.replace(0, np.nan)
    sl = _slope(fm, 252)
    neg = (fm < 0).astype(float)
    rhold = (revenue >= _mean(revenue, 252)).astype(float)
    result = sl * (0.5 + neg) * (0.5 + 0.5 * rhold)
    return result.replace([np.inf, -np.inf], np.nan)


# turnaround maturity: time since the netinc trough minus time since equity trough
def f38ts_f38_turnaround_signature_turnmature_252d_base_v070_signal(netinc, equity):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsl_ni = netinc.rolling(252, min_periods=126).apply(_dsl, raw=True)
    dsl_eq = equity.rolling(252, min_periods=126).apply(_dsl, raw=True)
    recov = np.tanh((netinc - _rmin(netinc, 252)) / _mean(equity.abs(), 252).replace(0, np.nan))
    result = (dsl_ni - dsl_eq) + 0.5 * recov
    return result.replace([np.inf, -np.inf], np.nan)


# all-engine composite: margin, fcf, debt, revenue, netinc improvement blend
def f38ts_f38_turnaround_signature_allengine_252d_base_v071_signal(grossmargin, fcf, debt, revenue, netinc):
    a = _f38_margin_floor_gap(grossmargin, 252)
    b = _f38_fcf_cross(fcf, 252)
    c = _f38_delever(debt, 252)
    d = np.tanh(_f38_rev_stab(revenue, 252))
    e = _f38_loss_narrow(netinc, 252)
    result = (a + b + c + d + e) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash-quality emergence: ncfo/revenue lifting off its floor
def f38ts_f38_turnaround_signature_ncfomargturn_252d_base_v072_signal(ncfo, revenue):
    cm = ncfo / revenue.replace(0, np.nan)
    lo = _rmin(cm, 252)
    result = (cm - lo) / (cm.abs() + lo.abs() + 0.01)
    return result.replace([np.inf, -np.inf], np.nan)


# deleveraging-with-margin-lift: slope of debt-paydown minus margin-floor rank
def f38ts_f38_turnaround_signature_delevmarg_504d_base_v073_signal(debt, grossmargin):
    dsl = -_slope(debt, 252) / _mean(debt, 504).replace(0, np.nan)
    mlr = _f38_margin_floor_gap(grossmargin, 504).rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = np.tanh(200.0 * dsl) * (0.5 + mlr)
    return result.replace([np.inf, -np.inf], np.nan)


# loss-to-profit transition: netinc climbing off its 504d trough, fcf-confirmed
def f38ts_f38_turnaround_signature_l2ptrans_504d_base_v074_signal(netinc, fcf):
    worst = _rmin(netinc, 504)
    span = (_rmax(netinc, 504) - worst).replace(0, np.nan)
    climb = (netinc - worst) / span
    fc = _f38_fcf_cross(fcf, 504)
    result = climb * (0.5 + fc.clip(lower=-0.5))
    return result.replace([np.inf, -np.inf], np.nan)


# recovery composite dispersion across engines (broad vs narrow turn), ranked
def f38ts_f38_turnaround_signature_recovradj_252d_base_v075_signal(grossmargin, fcf, netinc, revenue):
    a = _z(_f38_margin_floor_gap(grossmargin, 252), 126)
    b = _z(_f38_fcf_cross(fcf, 252), 126)
    c = _z(_f38_loss_narrow(netinc, 252), 126)
    d = _z(np.tanh(_f38_rev_stab(revenue, 126)), 126)
    stacked = pd.concat([a, b, c, d], axis=1)
    disp = stacked.std(axis=1)
    result = stacked.mean(axis=1) - disp
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38ts_f38_turnaround_signature_mfloorgap_252d_base_v001_signal,
    f38ts_f38_turnaround_signature_mfloorgap_504d_base_v002_signal,
    f38ts_f38_turnaround_signature_mlift_126d_base_v003_signal,
    f38ts_f38_turnaround_signature_mliftcash_252d_base_v004_signal,
    f38ts_f38_turnaround_signature_mz_252d_base_v005_signal,
    f38ts_f38_turnaround_signature_lossnarrow_252d_base_v006_signal,
    f38ts_f38_turnaround_signature_lossnarrow_504d_base_v007_signal,
    f38ts_f38_turnaround_signature_lossslope_126d_base_v008_signal,
    f38ts_f38_turnaround_signature_nirecov_252d_base_v009_signal,
    f38ts_f38_turnaround_signature_fcfcross_252d_base_v010_signal,
    f38ts_f38_turnaround_signature_fcfcross_504d_base_v011_signal,
    f38ts_f38_turnaround_signature_fcfstreak_252d_base_v012_signal,
    f38ts_f38_turnaround_signature_fcfmargrec_252d_base_v013_signal,
    f38ts_f38_turnaround_signature_ncforec_252d_base_v014_signal,
    f38ts_f38_turnaround_signature_delevstab_252d_base_v015_signal,
    f38ts_f38_turnaround_signature_delevstab_504d_base_v016_signal,
    f38ts_f38_turnaround_signature_levimprove_252d_base_v017_signal,
    f38ts_f38_turnaround_signature_paydownstreak_252d_base_v018_signal,
    f38ts_f38_turnaround_signature_twinrev_252d_base_v019_signal,
    f38ts_f38_turnaround_signature_recovcomp_252d_base_v020_signal,
    f38ts_f38_turnaround_signature_recovcomp_504d_base_v021_signal,
    f38ts_f38_turnaround_signature_qualconv_252d_base_v022_signal,
    f38ts_f38_turnaround_signature_earlyturn_252d_base_v023_signal,
    f38ts_f38_turnaround_signature_roerec_252d_base_v024_signal,
    f38ts_f38_turnaround_signature_roerec_504d_base_v025_signal,
    f38ts_f38_turnaround_signature_mslope_252d_base_v026_signal,
    f38ts_f38_turnaround_signature_fcfslope_252d_base_v027_signal,
    f38ts_f38_turnaround_signature_debtslope_252d_base_v028_signal,
    f38ts_f38_turnaround_signature_eqslope_252d_base_v029_signal,
    f38ts_f38_turnaround_signature_nmcross_252d_base_v030_signal,
    f38ts_f38_turnaround_signature_distexit_252d_base_v031_signal,
    f38ts_f38_turnaround_signature_breadth_252d_base_v032_signal,
    f38ts_f38_turnaround_signature_mconvex_252d_base_v033_signal,
    f38ts_f38_turnaround_signature_fcfconvex_252d_base_v034_signal,
    f38ts_f38_turnaround_signature_delevfcf_252d_base_v035_signal,
    f38ts_f38_turnaround_signature_revmargturn_252d_base_v036_signal,
    f38ts_f38_turnaround_signature_bsheal_504d_base_v037_signal,
    f38ts_f38_turnaround_signature_cashlead_252d_base_v038_signal,
    f38ts_f38_turnaround_signature_nihitrate_252d_base_v039_signal,
    f38ts_f38_turnaround_signature_mliftdisp_252d_base_v040_signal,
    f38ts_f38_turnaround_signature_fcfyldrec_252d_base_v041_signal,
    f38ts_f38_turnaround_signature_recovmom_252d_base_v042_signal,
    f38ts_f38_turnaround_signature_debtrevheal_252d_base_v043_signal,
    f38ts_f38_turnaround_signature_distfade_504d_base_v044_signal,
    f38ts_f38_turnaround_signature_revaccelfcf_252d_base_v045_signal,
    f38ts_f38_turnaround_signature_gpdollrec_252d_base_v046_signal,
    f38ts_f38_turnaround_signature_persist_252d_base_v047_signal,
    f38ts_f38_turnaround_signature_selffund_252d_base_v048_signal,
    f38ts_f38_turnaround_signature_mqturn_252d_base_v049_signal,
    f38ts_f38_turnaround_signature_breakeven_252d_base_v050_signal,
    f38ts_f38_turnaround_signature_eqfundrec_252d_base_v051_signal,
    f38ts_f38_turnaround_signature_twinfade_252d_base_v052_signal,
    f38ts_f38_turnaround_signature_floordepth_504d_base_v053_signal,
    f38ts_f38_turnaround_signature_accrualturn_252d_base_v054_signal,
    f38ts_f38_turnaround_signature_durturn_252d_base_v055_signal,
    f38ts_f38_turnaround_signature_fcfdebtcov_252d_base_v056_signal,
    f38ts_f38_turnaround_signature_roeslope_252d_base_v057_signal,
    f38ts_f38_turnaround_signature_compz_252d_base_v058_signal,
    f38ts_f38_turnaround_signature_paydownaccel_252d_base_v059_signal,
    f38ts_f38_turnaround_signature_nmrank_252d_base_v060_signal,
    f38ts_f38_turnaround_signature_fcfemergedelev_252d_base_v061_signal,
    f38ts_f38_turnaround_signature_mfloorsolv_252d_base_v062_signal,
    f38ts_f38_turnaround_signature_revtroughcash_252d_base_v063_signal,
    f38ts_f38_turnaround_signature_lossslopesm_252d_base_v064_signal,
    f38ts_f38_turnaround_signature_bscashturn_504d_base_v065_signal,
    f38ts_f38_turnaround_signature_gpgrowthturn_252d_base_v066_signal,
    f38ts_f38_turnaround_signature_distqual_252d_base_v067_signal,
    f38ts_f38_turnaround_signature_eqdebtturn_252d_base_v068_signal,
    f38ts_f38_turnaround_signature_fcfmargslope_252d_base_v069_signal,
    f38ts_f38_turnaround_signature_turnmature_252d_base_v070_signal,
    f38ts_f38_turnaround_signature_allengine_252d_base_v071_signal,
    f38ts_f38_turnaround_signature_ncfomargturn_252d_base_v072_signal,
    f38ts_f38_turnaround_signature_delevmarg_504d_base_v073_signal,
    f38ts_f38_turnaround_signature_l2ptrans_504d_base_v074_signal,
    f38ts_f38_turnaround_signature_recovradj_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_TURNAROUND_SIGNATURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f38_turnaround_signature_base_001_075_claude: %d features pass" % n_features)
