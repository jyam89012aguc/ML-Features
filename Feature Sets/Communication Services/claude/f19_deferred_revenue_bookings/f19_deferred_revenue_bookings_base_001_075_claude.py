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


def _slope(s, w):
    # ordinary-least-squares slope of s over a rolling window (handles partial windows)
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        x = x - x.mean()
        denom = (x * x).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(x, a) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (deferred revenue / bookings) =====
def _f19_coverage(deferredrev, revenue):
    # deferred-revenue / revenue = bookings / subscription coverage ratio
    return deferredrev / revenue.replace(0, np.nan)


def _f19_drev_growth(deferredrev, w):
    # deferred-revenue log growth over window = forward-demand book-build
    return np.log(deferredrev.replace(0, np.nan) / deferredrev.shift(w).replace(0, np.nan))


def _f19_billings(deferredrev, revenue, w):
    # billings proxy = revenue + change in deferred revenue (recognized + booked)
    return revenue + (deferredrev - deferredrev.shift(w))


def _f19_drev_to_cash(deferredrev, ncfo):
    # deferred revenue relative to operating cash collected
    return deferredrev / ncfo.replace(0, np.nan)


def _f19_drev_to_recv(deferredrev, receivables):
    # booked-but-unearned vs billed-but-uncollected (cash-timing of the book)
    return deferredrev / receivables.replace(0, np.nan)


def _f19_recurring_visibility(deferredrev, revenue):
    # months of forward revenue covered by the current deferred book
    return (deferredrev / revenue.replace(0, np.nan)) * 12.0


# ============================================================
# deferred-revenue / revenue coverage level (bookings coverage)
def f19db_f19_deferred_revenue_bookings_cover_lvl_base_v001_signal(deferredrev, revenue):
    b = _f19_coverage(deferredrev, revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage z-scored vs its own 252d history (de-trended subscription coverage)
def f19db_f19_deferred_revenue_bookings_cover_z252_base_v002_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage percentile-ranked vs its own 504d history
def f19db_f19_deferred_revenue_bookings_cover_rk504_base_v003_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = c.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recurring-revenue visibility curvature: 2nd difference of forward-months visibility
def f19db_f19_deferred_revenue_bookings_visib_lvl_base_v004_signal(deferredrev, revenue):
    v = _f19_recurring_visibility(deferredrev, revenue)
    b = v - 2.0 * v.shift(63) + v.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage momentum normalized by coverage dispersion (risk-adjusted coverage drift)
def f19db_f19_deferred_revenue_bookings_cover_mom63_base_v005_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    mom = c - c.shift(63)
    disp = _std(c, 126)
    b = mom / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage displacement from its 126d mean, in coverage-std units (de-meaned z, 63d)
def f19db_f19_deferred_revenue_bookings_cover_disp126_base_v006_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = (c - _mean(c, 126)) / _std(c, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue book-build over a quarter (forward demand)
def f19db_f19_deferred_revenue_bookings_drevg_63_base_v007_signal(deferredrev):
    b = _f19_drev_growth(deferredrev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue book-build over half a year
def f19db_f19_deferred_revenue_bookings_drevg_126_base_v008_signal(deferredrev):
    b = _f19_drev_growth(deferredrev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue book-build year-over-year
def f19db_f19_deferred_revenue_bookings_drevg_252_base_v009_signal(deferredrev):
    b = _f19_drev_growth(deferredrev, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue book-build over two years (long forward demand)
def f19db_f19_deferred_revenue_bookings_drevg_504_base_v010_signal(deferredrev):
    b = _f19_drev_growth(deferredrev, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-build acceleration ranked vs its 252d history (forward-demand inflection regime)
def f19db_f19_deferred_revenue_bookings_drevg_accel_base_v011_signal(deferredrev):
    g = _f19_drev_growth(deferredrev, 63)
    acc = g - g.shift(63)
    b = acc.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-build consistency: fraction of last year's quarterly book-build that was positive
def f19db_f19_deferred_revenue_bookings_drevg_z252_base_v012_signal(deferredrev):
    g = _f19_drev_growth(deferredrev, 63)
    pos = (g > 0).astype(float)
    consist = pos.rolling(252, min_periods=126).mean()
    b = consist * g.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy growth vs revenue growth gap, z-scored (de-trended demand lead)
def f19db_f19_deferred_revenue_bookings_billgap_63_base_v013_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    bg = np.log(bill.replace(0, np.nan) / bill.shift(63).replace(0, np.nan))
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(63).replace(0, np.nan))
    b = _z(bg - rg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings-to-revenue ratio percentile-ranked vs 504d (forward-demand premium regime)
def f19db_f19_deferred_revenue_bookings_billratio_63_base_v014_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    ratio = bill / revenue.replace(0, np.nan)
    b = ratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d billings-to-revenue gap, smoothed and de-meaned vs 252d (structural demand premium)
def f19db_f19_deferred_revenue_bookings_billratio_126_base_v015_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 126)
    gap = bill / revenue.replace(0, np.nan) - 1.0
    sm = gap.ewm(span=42, min_periods=21).mean()
    b = sm - _mean(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net new bookings vs receivables build (book accretion net of billing inflation, level)
def f19db_f19_deferred_revenue_bookings_netbook_63_base_v016_signal(deferredrev, receivables):
    ddelta = deferredrev - deferredrev.shift(63)
    rdelta = receivables - receivables.shift(63)
    b = (ddelta - rdelta) / receivables.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-new-bookings intensity vs ncfo cash intake (cash-backed bookings z-score)
def f19db_f19_deferred_revenue_bookings_netbook_z252_base_v017_signal(deferredrev, ncfo):
    delta = deferredrev - deferredrev.shift(63)
    intensity = delta / ncfo.abs().replace(0, np.nan)
    b = _z(intensity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue vs operating cash collected (book vs cash)
def f19db_f19_deferred_revenue_bookings_drevcash_lvl_base_v018_signal(deferredrev, ncfo):
    b = _f19_drev_to_cash(deferredrev, ncfo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev-to-cash displacement from its smoothed trend (book/cash surprise)
def f19db_f19_deferred_revenue_bookings_drevcash_ema_base_v019_signal(deferredrev, ncfo):
    r = _f19_drev_to_cash(deferredrev, ncfo)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue vs receivables (unearned book vs uncollected billings)
def f19db_f19_deferred_revenue_bookings_drevrecv_lvl_base_v020_signal(deferredrev, receivables):
    b = _f19_drev_to_recv(deferredrev, receivables)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev-to-receivables momentum over a quarter
def f19db_f19_deferred_revenue_bookings_drevrecv_mom_base_v021_signal(deferredrev, receivables):
    r = _f19_drev_to_recv(deferredrev, receivables)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue scaled by cash, ranked vs its 504d history
def f19db_f19_deferred_revenue_bookings_drevcash_rk_base_v022_signal(deferredrev, ncfo):
    r = _f19_drev_to_cash(deferredrev, ncfo)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage spread: short-window coverage minus long-window coverage average
def f19db_f19_deferred_revenue_bookings_cover_spr_base_v023_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _mean(c, 63) - _mean(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage stability: inverse coefficient-of-variation of coverage (visibility quality)
def f19db_f19_deferred_revenue_bookings_cover_stab_base_v024_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    m = _mean(c, 252)
    sd = _std(c, 252)
    b = m / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth funded by the deferred book: revenue growth x coverage
def f19db_f19_deferred_revenue_bookings_revfund_base_v025_signal(deferredrev, revenue):
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(63).replace(0, np.nan))
    c = _f19_coverage(deferredrev, revenue)
    b = rg * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-build minus revenue growth (lead/lag of bookings over recognized rev)
def f19db_f19_deferred_revenue_bookings_leadlag_63_base_v026_signal(deferredrev, revenue):
    dg = _f19_drev_growth(deferredrev, 63)
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(63).replace(0, np.nan))
    b = dg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-build minus revenue growth over 126d
def f19db_f19_deferred_revenue_bookings_leadlag_126_base_v027_signal(deferredrev, revenue):
    dg = _f19_drev_growth(deferredrev, 126)
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(126).replace(0, np.nan))
    b = dg - rg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-share regime: drev/(drev+receivables) percentile-ranked vs 504d (mix level regime)
def f19db_f19_deferred_revenue_bookings_bookshare_base_v028_signal(deferredrev, receivables):
    share = deferredrev / (deferredrev + receivables).replace(0, np.nan)
    b = share.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book quality regime: fraction of last year drev outgrew receivables (clean-build time)
def f19db_f19_deferred_revenue_bookings_bookqual_base_v029_signal(deferredrev, receivables):
    dg = _f19_drev_growth(deferredrev, 63)
    recg = np.log(receivables.replace(0, np.nan) / receivables.shift(63).replace(0, np.nan))
    clean = (dg > recg).astype(float)
    b = clean.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion of the book: ncfo relative to deferred revenue (collection on book)
def f19db_f19_deferred_revenue_bookings_cashconv_base_v030_signal(deferredrev, ncfo):
    b = ncfo / deferredrev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash margin of the book: ncfo / revenue, weighted by coverage
def f19db_f19_deferred_revenue_bookings_cashcover_base_v031_signal(deferredrev, revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    c = _f19_coverage(deferredrev, revenue)
    b = cm * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage relative to one year ago (year-over-year coverage change)
def f19db_f19_deferred_revenue_bookings_cover_yoy_base_v032_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue level vs its 252d mean (book expansion vs trend)
def f19db_f19_deferred_revenue_bookings_drev_ext_base_v033_signal(deferredrev):
    m = _mean(deferredrev, 252)
    b = deferredrev / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue distance to its trailing 504d max (book at peak vs drained)
def f19db_f19_deferred_revenue_bookings_drev_peak_base_v034_signal(deferredrev):
    hi = _rmax(deferredrev, 504)
    b = deferredrev / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue position within its 504d range (book fill level, 0=drained 1=peak)
def f19db_f19_deferred_revenue_bookings_drev_recov_base_v035_signal(deferredrev):
    hi = _rmax(deferredrev, 504)
    lo = _rmin(deferredrev, 504)
    b = (deferredrev - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy z-scored vs its own 252d history (de-trended demand)
def f19db_f19_deferred_revenue_bookings_bill_z252_base_v036_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    b = _z(bill, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-new bookings vs operating cash (cash-backing of new book)
def f19db_f19_deferred_revenue_bookings_netcash_base_v037_signal(deferredrev, ncfo):
    delta = deferredrev - deferredrev.shift(63)
    b = delta / ncfo.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage dispersion: rolling std of coverage (visibility instability)
def f19db_f19_deferred_revenue_bookings_cover_disp_base_v038_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _std(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-days vs deferred-coverage-days spread (collection lag vs forward visibility)
def f19db_f19_deferred_revenue_bookings_recvcover_base_v039_signal(deferredrev, revenue, receivables):
    dso = receivables / revenue.replace(0, np.nan)
    cover = _f19_coverage(deferredrev, revenue)
    spread = cover - dso
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of weekly book changes within the quarter (lumpy vs smooth book-build)
def f19db_f19_deferred_revenue_bookings_netsignmag_base_v040_signal(deferredrev):
    wk = deferredrev.pct_change(5)
    b = _std(wk, 63) / _mean(wk.abs(), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-build impulse: short (21d) drev growth minus its long (252d) average (impulse vs trend)
def f19db_f19_deferred_revenue_bookings_drevtanh_base_v041_signal(deferredrev):
    short = _f19_drev_growth(deferredrev, 21)
    b = short - _mean(short, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage convexity: how far coverage sits from its mid-range, squared & signed
def f19db_f19_deferred_revenue_bookings_cover_conv_base_v042_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    hi = _rmax(c, 252)
    lo = _rmin(c, 252)
    pos = (c - lo) / (hi - lo).replace(0, np.nan)
    b = np.sign(pos - 0.5) * (pos - 0.5) ** 2 * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the last year deferred revenue grew sequentially (book-build streak)
def f19db_f19_deferred_revenue_bookings_buildfreq_base_v043_signal(deferredrev):
    up = (deferredrev > deferredrev.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy momentum over a quarter (demand acceleration)
def f19db_f19_deferred_revenue_bookings_bill_mom_base_v044_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    b = np.log(bill.replace(0, np.nan) / bill.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue / receivables, z-scored (book vs billing balance, de-trended)
def f19db_f19_deferred_revenue_bookings_drevrecv_z_base_v045_signal(deferredrev, receivables):
    r = _f19_drev_to_recv(deferredrev, receivables)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year coverage regime distance: coverage minus its 1260d median, vol-scaled
def f19db_f19_deferred_revenue_bookings_cover_rk1260_base_v046_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    med = c.rolling(1260, min_periods=252).median()
    sd = c.rolling(1260, min_periods=252).std()
    b = np.tanh((c - med) / sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue covered per dollar of receivables, scaled by coverage (collection-adjusted book)
def f19db_f19_deferred_revenue_bookings_collbook_base_v047_signal(deferredrev, revenue, receivables):
    coll = revenue / receivables.replace(0, np.nan)
    c = _f19_coverage(deferredrev, revenue)
    b = c / coll.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev growth minus cash growth (book outpacing collected cash)
def f19db_f19_deferred_revenue_bookings_drevvscash_base_v048_signal(deferredrev, ncfo):
    dg = _f19_drev_growth(deferredrev, 63)
    cg = np.log(ncfo.replace(0, np.nan).abs() / ncfo.shift(63).replace(0, np.nan).abs())
    b = dg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend: OLS slope of coverage over 126d
def f19db_f19_deferred_revenue_bookings_cover_slp_base_v049_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _slope(c, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings-proxy trend: OLS slope of log billings over 126d (forward-demand trajectory)
def f19db_f19_deferred_revenue_bookings_drev_slp_base_v050_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    lb = np.log(bill.replace(0, np.nan).clip(lower=1.0))
    b = _slope(lb, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# visibility minus its slow EMA (visibility surprise)
def f19db_f19_deferred_revenue_bookings_visib_disp_base_v051_signal(deferredrev, revenue):
    v = _f19_recurring_visibility(deferredrev, revenue)
    b = v - v.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings / receivables (booked demand vs uncollected billings)
def f19db_f19_deferred_revenue_bookings_billrecv_base_v052_signal(deferredrev, revenue, receivables):
    bill = _f19_billings(deferredrev, revenue, 63)
    b = bill / receivables.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net new bookings smoothed and ranked (sustained book-build regime)
def f19db_f19_deferred_revenue_bookings_netbook_rk_base_v053_signal(deferredrev, revenue):
    delta = deferredrev - deferredrev.shift(63)
    intensity = delta / revenue.replace(0, np.nan)
    sm = intensity.ewm(span=42, min_periods=21).mean()
    b = sm.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage drawdown: coverage vs its trailing 252d max (book coverage erosion)
def f19db_f19_deferred_revenue_bookings_cover_dd_base_v054_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    hi = _rmax(c, 252)
    b = c / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue book-build vs cash-conversion interaction (growth-with-cash quality)
def f19db_f19_deferred_revenue_bookings_buildcash_base_v055_signal(deferredrev, ncfo):
    g = _f19_drev_growth(deferredrev, 63)
    conv = ncfo / deferredrev.replace(0, np.nan)
    b = g * np.tanh(conv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage position in its 504d range (where subscription coverage sits)
def f19db_f19_deferred_revenue_bookings_cover_pos_base_v056_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    hi = _rmax(c, 504)
    lo = _rmin(c, 504)
    b = (c - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recognized revenue relative to the deferred book it draws from (book burn-down rate)
def f19db_f19_deferred_revenue_bookings_drain_base_v057_signal(deferredrev, revenue):
    burn = revenue / deferredrev.shift(63).replace(0, np.nan)
    b = burn - _mean(burn, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue / (revenue trailing-mean) — coverage vs smoothed scale
def f19db_f19_deferred_revenue_bookings_drevscale_base_v058_signal(deferredrev, revenue):
    rm = _mean(revenue, 252)
    b = deferredrev / rm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings intensity dispersion (lumpiness of forward demand)
def f19db_f19_deferred_revenue_bookings_bookvol_base_v059_signal(deferredrev, revenue):
    delta = deferredrev - deferredrev.shift(21)
    intensity = delta / revenue.replace(0, np.nan)
    b = _std(intensity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage curvature regime: sign-agreement of coverage slope over consecutive quarters
def f19db_f19_deferred_revenue_bookings_cover_acc_base_v060_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    s1 = c - c.shift(63)
    s2 = c.shift(63) - c.shift(126)
    b = np.sign(s1) * np.log1p((s1 * s2).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy growth over a year (full-cycle demand expansion)
def f19db_f19_deferred_revenue_bookings_billg_252_base_v061_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 126)
    b = np.log(bill.replace(0, np.nan) / bill.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev-to-receivables trend: OLS slope over 252d (book vs billing trajectory)
def f19db_f19_deferred_revenue_bookings_drevrecv_rk_base_v062_signal(deferredrev, receivables):
    r = _f19_drev_to_recv(deferredrev, receivables)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# visible-and-cash-backed book: coverage rank times sign of operating cash (regime composite)
def f19db_f19_deferred_revenue_bookings_visiblecash_base_v063_signal(deferredrev, revenue, ncfo):
    c = _f19_coverage(deferredrev, revenue)
    crank = c.rolling(252, min_periods=126).rank(pct=True) - 0.5
    cashpos = np.tanh(ncfo / _mean(revenue, 252).replace(0, np.nan))
    b = crank * cashpos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev book-build minus receivables-build (clean book vs billing inflation)
def f19db_f19_deferred_revenue_bookings_cleanbook_base_v064_signal(deferredrev, receivables):
    dg = _f19_drev_growth(deferredrev, 126)
    recg = np.log(receivables.replace(0, np.nan) / receivables.shift(126).replace(0, np.nan))
    b = np.tanh(3.0 * (dg - recg))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage half-vs-full-year mean spread, normalized (recent vs structural coverage)
def f19db_f19_deferred_revenue_bookings_coverspr_norm_base_v065_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    short = _mean(c, 126)
    long = _mean(c, 504)
    b = (short - long) / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash-conversion of the book over a year (collection-trend on the book)
def f19db_f19_deferred_revenue_bookings_cashpervis_base_v066_signal(deferredrev, ncfo):
    conv = ncfo / deferredrev.replace(0, np.nan)
    b = conv - conv.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue growth, downside semi-deviation (book-erosion risk)
def f19db_f19_deferred_revenue_bookings_drev_dsd_base_v067_signal(deferredrev):
    g = deferredrev.pct_change(21)
    neg = g.where(g < 0, 0.0)
    b = np.sqrt((neg ** 2).rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-new-bookings sign streak length (consecutive book-build direction)
def f19db_f19_deferred_revenue_bookings_streak_base_v068_signal(deferredrev):
    delta = deferredrev - deferredrev.shift(21)
    sgn = np.sign(delta)
    grp = (sgn != sgn.shift(1)).cumsum()
    b = sgn * sgn.groupby(grp).cumcount().add(1).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings-gap volatility: dispersion of the billings-to-revenue gap (demand lumpiness)
def f19db_f19_deferred_revenue_bookings_billgap_rk_base_v069_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    gap = bill / revenue.replace(0, np.nan) - 1.0
    b = _std(gap, 126) / _mean(gap.abs(), 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage interaction with revenue scale (large + well-covered book)
def f19db_f19_deferred_revenue_bookings_coverscale_base_v070_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    scale = np.log(revenue.replace(0, np.nan))
    b = c * (scale - scale.rolling(252, min_periods=126).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue vs cash, change relative to a year ago (book/cash regime shift)
def f19db_f19_deferred_revenue_bookings_drevcash_yoy_base_v071_signal(deferredrev, ncfo):
    r = _f19_drev_to_cash(deferredrev, ncfo)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-build per unit of book-build volatility (risk-adjusted forward demand)
def f19db_f19_deferred_revenue_bookings_riskadj_base_v072_signal(deferredrev):
    g = _f19_drev_growth(deferredrev, 63)
    vol = _std(deferredrev.pct_change(21), 252)
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the last year coverage stayed above its long-run median (high-visibility time)
def f19db_f19_deferred_revenue_bookings_highvistime_base_v073_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    med = c.rolling(504, min_periods=252).median()
    above = (c > med).astype(float)
    b = above.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings minus revenue change, scaled by deferred book (organic book accretion)
def f19db_f19_deferred_revenue_bookings_accretion_base_v074_signal(deferredrev, revenue):
    ddelta = deferredrev - deferredrev.shift(63)
    rdelta = revenue - revenue.shift(63)
    b = (ddelta - rdelta) / deferredrev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite book-health: coverage rank + book-build rank - cash-strain (balanced book)
def f19db_f19_deferred_revenue_bookings_bookhealth_base_v075_signal(deferredrev, revenue, ncfo):
    c = _f19_coverage(deferredrev, revenue)
    crank = c.rolling(504, min_periods=126).rank(pct=True) - 0.5
    g = _f19_drev_growth(deferredrev, 63)
    grank = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    strain = np.tanh((deferredrev - deferredrev.shift(63)) / ncfo.replace(0, np.nan))
    b = crank + grank - 0.3 * strain
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19db_f19_deferred_revenue_bookings_cover_lvl_base_v001_signal,
    f19db_f19_deferred_revenue_bookings_cover_z252_base_v002_signal,
    f19db_f19_deferred_revenue_bookings_cover_rk504_base_v003_signal,
    f19db_f19_deferred_revenue_bookings_visib_lvl_base_v004_signal,
    f19db_f19_deferred_revenue_bookings_cover_mom63_base_v005_signal,
    f19db_f19_deferred_revenue_bookings_cover_disp126_base_v006_signal,
    f19db_f19_deferred_revenue_bookings_drevg_63_base_v007_signal,
    f19db_f19_deferred_revenue_bookings_drevg_126_base_v008_signal,
    f19db_f19_deferred_revenue_bookings_drevg_252_base_v009_signal,
    f19db_f19_deferred_revenue_bookings_drevg_504_base_v010_signal,
    f19db_f19_deferred_revenue_bookings_drevg_accel_base_v011_signal,
    f19db_f19_deferred_revenue_bookings_drevg_z252_base_v012_signal,
    f19db_f19_deferred_revenue_bookings_billgap_63_base_v013_signal,
    f19db_f19_deferred_revenue_bookings_billratio_63_base_v014_signal,
    f19db_f19_deferred_revenue_bookings_billratio_126_base_v015_signal,
    f19db_f19_deferred_revenue_bookings_netbook_63_base_v016_signal,
    f19db_f19_deferred_revenue_bookings_netbook_z252_base_v017_signal,
    f19db_f19_deferred_revenue_bookings_drevcash_lvl_base_v018_signal,
    f19db_f19_deferred_revenue_bookings_drevcash_ema_base_v019_signal,
    f19db_f19_deferred_revenue_bookings_drevrecv_lvl_base_v020_signal,
    f19db_f19_deferred_revenue_bookings_drevrecv_mom_base_v021_signal,
    f19db_f19_deferred_revenue_bookings_drevcash_rk_base_v022_signal,
    f19db_f19_deferred_revenue_bookings_cover_spr_base_v023_signal,
    f19db_f19_deferred_revenue_bookings_cover_stab_base_v024_signal,
    f19db_f19_deferred_revenue_bookings_revfund_base_v025_signal,
    f19db_f19_deferred_revenue_bookings_leadlag_63_base_v026_signal,
    f19db_f19_deferred_revenue_bookings_leadlag_126_base_v027_signal,
    f19db_f19_deferred_revenue_bookings_bookshare_base_v028_signal,
    f19db_f19_deferred_revenue_bookings_bookqual_base_v029_signal,
    f19db_f19_deferred_revenue_bookings_cashconv_base_v030_signal,
    f19db_f19_deferred_revenue_bookings_cashcover_base_v031_signal,
    f19db_f19_deferred_revenue_bookings_cover_yoy_base_v032_signal,
    f19db_f19_deferred_revenue_bookings_drev_ext_base_v033_signal,
    f19db_f19_deferred_revenue_bookings_drev_peak_base_v034_signal,
    f19db_f19_deferred_revenue_bookings_drev_recov_base_v035_signal,
    f19db_f19_deferred_revenue_bookings_bill_z252_base_v036_signal,
    f19db_f19_deferred_revenue_bookings_netcash_base_v037_signal,
    f19db_f19_deferred_revenue_bookings_cover_disp_base_v038_signal,
    f19db_f19_deferred_revenue_bookings_recvcover_base_v039_signal,
    f19db_f19_deferred_revenue_bookings_netsignmag_base_v040_signal,
    f19db_f19_deferred_revenue_bookings_drevtanh_base_v041_signal,
    f19db_f19_deferred_revenue_bookings_cover_conv_base_v042_signal,
    f19db_f19_deferred_revenue_bookings_buildfreq_base_v043_signal,
    f19db_f19_deferred_revenue_bookings_bill_mom_base_v044_signal,
    f19db_f19_deferred_revenue_bookings_drevrecv_z_base_v045_signal,
    f19db_f19_deferred_revenue_bookings_cover_rk1260_base_v046_signal,
    f19db_f19_deferred_revenue_bookings_collbook_base_v047_signal,
    f19db_f19_deferred_revenue_bookings_drevvscash_base_v048_signal,
    f19db_f19_deferred_revenue_bookings_cover_slp_base_v049_signal,
    f19db_f19_deferred_revenue_bookings_drev_slp_base_v050_signal,
    f19db_f19_deferred_revenue_bookings_visib_disp_base_v051_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_base_v052_signal,
    f19db_f19_deferred_revenue_bookings_netbook_rk_base_v053_signal,
    f19db_f19_deferred_revenue_bookings_cover_dd_base_v054_signal,
    f19db_f19_deferred_revenue_bookings_buildcash_base_v055_signal,
    f19db_f19_deferred_revenue_bookings_cover_pos_base_v056_signal,
    f19db_f19_deferred_revenue_bookings_drain_base_v057_signal,
    f19db_f19_deferred_revenue_bookings_drevscale_base_v058_signal,
    f19db_f19_deferred_revenue_bookings_bookvol_base_v059_signal,
    f19db_f19_deferred_revenue_bookings_cover_acc_base_v060_signal,
    f19db_f19_deferred_revenue_bookings_billg_252_base_v061_signal,
    f19db_f19_deferred_revenue_bookings_drevrecv_rk_base_v062_signal,
    f19db_f19_deferred_revenue_bookings_visiblecash_base_v063_signal,
    f19db_f19_deferred_revenue_bookings_cleanbook_base_v064_signal,
    f19db_f19_deferred_revenue_bookings_coverspr_norm_base_v065_signal,
    f19db_f19_deferred_revenue_bookings_cashpervis_base_v066_signal,
    f19db_f19_deferred_revenue_bookings_drev_dsd_base_v067_signal,
    f19db_f19_deferred_revenue_bookings_streak_base_v068_signal,
    f19db_f19_deferred_revenue_bookings_billgap_rk_base_v069_signal,
    f19db_f19_deferred_revenue_bookings_coverscale_base_v070_signal,
    f19db_f19_deferred_revenue_bookings_drevcash_yoy_base_v071_signal,
    f19db_f19_deferred_revenue_bookings_riskadj_base_v072_signal,
    f19db_f19_deferred_revenue_bookings_highvistime_base_v073_signal,
    f19db_f19_deferred_revenue_bookings_accretion_base_v074_signal,
    f19db_f19_deferred_revenue_bookings_bookhealth_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_DEFERRED_REVENUE_BOOKINGS_REGISTRY_001_075 = REGISTRY


ALLOW = {
    "open", "high", "low", "close", "closeadj", "volume",
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
    "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
    "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
    "investments", "inventory", "receivables", "payables", "equity", "retearn",
    "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
    "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
    "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
    "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb",
    "ps", "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
    "fndholders", "undholders", "prfholders", "dbtholders", "putholders", "putvalue",
    "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
}
FUNDAMENTAL = {
    "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
    "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
    "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
    "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
    "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
    "investments", "inventory", "receivables", "payables", "equity", "retearn",
    "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
    "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
    "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
    "payoutratio", "prefdivis",
}


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

    deferredrev = _fund(101, base=8e7, drift=0.035, vol=0.08).rename("deferredrev")
    revenue = _fund(102, base=2e8, drift=0.030, vol=0.06).rename("revenue")
    receivables = _fund(103, base=5e7, drift=0.028, vol=0.07).rename("receivables")
    ncfo = _fund(104, base=4e7, drift=0.025, vol=0.10, allow_neg=True).rename("ncfo")

    cols = {
        "deferredrev": deferredrev, "revenue": revenue,
        "receivables": receivables, "ncfo": ncfo,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "ALLOWLIST %s: %s" % (name, meta["inputs"])
        assert any(c in FUNDAMENTAL for c in meta["inputs"]), "NO FUND %s" % name
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

    print("OK f19_deferred_revenue_bookings_base_001_075_claude: %d features pass" % n_features)
