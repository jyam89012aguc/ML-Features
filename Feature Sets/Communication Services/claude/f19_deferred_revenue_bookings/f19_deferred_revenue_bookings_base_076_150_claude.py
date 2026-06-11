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
    return deferredrev / revenue.replace(0, np.nan)


def _f19_drev_growth(deferredrev, w):
    return np.log(deferredrev.replace(0, np.nan) / deferredrev.shift(w).replace(0, np.nan))


def _f19_billings(deferredrev, revenue, w):
    return revenue + (deferredrev - deferredrev.shift(w))


def _f19_drev_to_cash(deferredrev, ncfo):
    return deferredrev / ncfo.replace(0, np.nan)


def _f19_drev_to_recv(deferredrev, receivables):
    return deferredrev / receivables.replace(0, np.nan)


def _f19_recurring_visibility(deferredrev, revenue):
    return (deferredrev / revenue.replace(0, np.nan)) * 12.0


# ============================================================
# log deferred-revenue level normalized by its 252d mean (book scale extension)
def f19db_f19_deferred_revenue_bookings_logdrev_ext_base_v076_signal(deferredrev):
    ld = np.log(deferredrev.replace(0, np.nan))
    b = ld - _mean(ld, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# size-neutral coverage displacement from its 252d mean in std units (size-adj coverage z)
def f19db_f19_deferred_revenue_bookings_coversz_base_v077_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    sz = c / np.log(revenue.replace(0, np.nan).clip(lower=1.0))
    b = (sz - _mean(sz, 252)) / _std(sz, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy / receivables, z-scored (forward demand vs uncollected billings)
def f19db_f19_deferred_revenue_bookings_billrecv_z_base_v078_signal(deferredrev, revenue, receivables):
    bill = _f19_billings(deferredrev, revenue, 63)
    r = bill / receivables.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage skewness over 252d (asymmetry of subscription-coverage regime)
def f19db_f19_deferred_revenue_bookings_coverskew_base_v079_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = c.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue growth kurtosis (fat-tailed book-build / lumpy bookings)
def f19db_f19_deferred_revenue_bookings_drevkurt_base_v080_signal(deferredrev):
    g = deferredrev.pct_change(21)
    b = g.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year vs two-year book-build spread (medium vs long forward-demand trend)
def f19db_f19_deferred_revenue_bookings_buildspr_base_v081_signal(deferredrev):
    g126 = _f19_drev_growth(deferredrev, 126)
    g504 = _f19_drev_growth(deferredrev, 504)
    b = g126 - 0.25 * g504
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage z-scored over a short 63d window (near-term coverage tension)
def f19db_f19_deferred_revenue_bookings_cover_z63_base_v082_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _z(c, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-bookings intensity over a 126d window (medium-term forward-demand intensity)
def f19db_f19_deferred_revenue_bookings_netbook126_base_v083_signal(deferredrev, revenue):
    delta = deferredrev - deferredrev.shift(126)
    b = delta / revenue.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue relative to cash collected, range-position in 504d window
def f19db_f19_deferred_revenue_bookings_drevcash_pos_base_v084_signal(deferredrev, ncfo):
    r = _f19_drev_to_cash(deferredrev, ncfo)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = (r - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue / deferred revenue (book turnover = how fast the book is recognized)
def f19db_f19_deferred_revenue_bookings_bookturn_base_v085_signal(deferredrev, revenue):
    b = revenue / deferredrev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book turnover momentum over a quarter (recognition-pace acceleration)
def f19db_f19_deferred_revenue_bookings_bookturn_mom_base_v086_signal(deferredrev, revenue):
    turn = revenue / deferredrev.replace(0, np.nan)
    b = turn - turn.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash margin trend, weighted by book coverage (cash-quality of visible book)
def f19db_f19_deferred_revenue_bookings_cashqual_base_v087_signal(deferredrev, revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    c = _f19_coverage(deferredrev, revenue)
    b = _slope(cm, 126) * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year coverage rose AND book grew (twin-expansion regime)
def f19db_f19_deferred_revenue_bookings_twinexp_base_v088_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    cup = (c > c.shift(21)).astype(float)
    dup = (deferredrev > deferredrev.shift(21)).astype(float)
    both = (cup * dup)
    b = both.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy growth vs operating-cash growth (book vs cash collection divergence)
def f19db_f19_deferred_revenue_bookings_billcash_base_v089_signal(deferredrev, revenue, ncfo):
    bill = _f19_billings(deferredrev, revenue, 63)
    bg = np.log(bill.replace(0, np.nan) / bill.shift(63).replace(0, np.nan))
    cg = np.log(ncfo.abs().replace(0, np.nan) / ncfo.shift(63).abs().replace(0, np.nan))
    b = bg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend over two years (long subscription-coverage trajectory)
def f19db_f19_deferred_revenue_bookings_cover_slp504_base_v090_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _slope(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue 21d acceleration: 2nd difference of log deferred revenue
def f19db_f19_deferred_revenue_bookings_drev_accel21_base_v091_signal(deferredrev):
    ld = np.log(deferredrev.replace(0, np.nan))
    b = ld - 2.0 * ld.shift(21) + ld.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue / receivables, displacement from slow EMA (book/billing surprise)
def f19db_f19_deferred_revenue_bookings_drevrecv_disp_base_v092_signal(deferredrev, receivables):
    r = _f19_drev_to_recv(deferredrev, receivables)
    b = r - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage minus DSO spread, ranked vs 504d (forward-visibility net of collection regime)
def f19db_f19_deferred_revenue_bookings_netvisib_base_v093_signal(deferredrev, revenue, receivables):
    cover = _f19_coverage(deferredrev, revenue)
    dso = receivables / revenue.replace(0, np.nan)
    spread = cover - dso
    b = spread.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# forward-booking mix z-scored vs its own 252d history (de-trended booking mix)
def f19db_f19_deferred_revenue_bookings_fwdmix_base_v094_signal(deferredrev, revenue):
    mix = deferredrev / (revenue + deferredrev).replace(0, np.nan)
    b = _z(mix, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# forward-mix momentum over half a year (shift toward forward bookings)
def f19db_f19_deferred_revenue_bookings_fwdmix_mom_base_v095_signal(deferredrev, revenue):
    mix = deferredrev / (revenue + deferredrev).replace(0, np.nan)
    b = mix - mix.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual net-book accretion vs prior year (acceleration of yearly book accretion)
def f19db_f19_deferred_revenue_bookings_annbook_base_v096_signal(deferredrev):
    delta = (deferredrev - deferredrev.shift(21))
    cum = delta.rolling(252, min_periods=126).sum()
    accr = cum / _mean(deferredrev, 252).replace(0, np.nan)
    b = accr - accr.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash relative to billings proxy (cash backing per unit of demand)
def f19db_f19_deferred_revenue_bookings_cashbill_base_v097_signal(deferredrev, revenue, ncfo):
    bill = _f19_billings(deferredrev, revenue, 63)
    b = ncfo / bill.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage volatility relative to coverage level (relative visibility instability)
def f19db_f19_deferred_revenue_bookings_covercv_base_v098_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    b = _std(c, 252) / _mean(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue book-build over a week, smoothed (high-frequency book pulse)
def f19db_f19_deferred_revenue_bookings_pulse_base_v099_signal(deferredrev):
    g = _f19_drev_growth(deferredrev, 5)
    b = g.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth-to-bookbuild ratio (recognition keeping pace with new bookings)
def f19db_f19_deferred_revenue_bookings_recogpace_base_v100_signal(deferredrev, revenue):
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(126).replace(0, np.nan))
    dg = _f19_drev_growth(deferredrev, 126)
    b = rg / dg.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev drawdown depth x duration (book erosion severity)
def f19db_f19_deferred_revenue_bookings_bookdd_base_v101_signal(deferredrev):
    hi = _rmax(deferredrev, 504)
    dd = deferredrev / hi.replace(0, np.nan) - 1.0
    under = (dd < -0.02).astype(float)
    dur = under.rolling(252, min_periods=126).mean()
    b = dd * dur
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage Bollinger position (where coverage sits in its own band)
def f19db_f19_deferred_revenue_bookings_coverboll_base_v102_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    m = _mean(c, 126)
    sd = _std(c, 126)
    b = (c - m) / (2.0 * sd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings intensity vs receivables build (forward demand net of billing inflation, z)
def f19db_f19_deferred_revenue_bookings_cleanintens_base_v103_signal(deferredrev, receivables):
    ddelta = deferredrev - deferredrev.shift(63)
    rdelta = receivables - receivables.shift(63)
    spread = (ddelta - rdelta) / _mean(deferredrev, 252).replace(0, np.nan)
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash conversion vs its own trailing mean (cash-on-book improvement)
def f19db_f19_deferred_revenue_bookings_convimprove_base_v104_signal(deferredrev, ncfo):
    conv = ncfo / deferredrev.replace(0, np.nan)
    b = conv - _mean(conv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy 252d range-position (where forward demand sits in its 2yr range)
def f19db_f19_deferred_revenue_bookings_billpos_base_v105_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    hi = _rmax(bill, 504)
    lo = _rmin(bill, 504)
    b = (bill - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage minus its year-ago value, vol-scaled (de-trended YoY coverage shift)
def f19db_f19_deferred_revenue_bookings_coveryoy_z_base_v106_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    yoy = c - c.shift(252)
    b = yoy / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue growth signed by whether cash is positive (cash-validated book-build)
def f19db_f19_deferred_revenue_bookings_cashvalid_base_v107_signal(deferredrev, ncfo):
    g = _f19_drev_growth(deferredrev, 63)
    cashsign = np.tanh(ncfo / _mean(ncfo.abs(), 252).replace(0, np.nan))
    b = g * cashsign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage range amplitude over 504d normalized by mean coverage (regime breadth)
def f19db_f19_deferred_revenue_bookings_coverampl_base_v108_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    hi = _rmax(c, 504)
    lo = _rmin(c, 504)
    b = (hi - lo) / _mean(c, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings intensity smoothed minus its 252d mean (book-build surprise)
def f19db_f19_deferred_revenue_bookings_netsurprise_base_v109_signal(deferredrev, revenue):
    delta = deferredrev - deferredrev.shift(63)
    intensity = delta / revenue.replace(0, np.nan)
    sm = intensity.ewm(span=42, min_periods=21).mean()
    b = sm - _mean(intensity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue-to-cash spread vs deferred-revenue-to-receivables (cash vs billing book)
def f19db_f19_deferred_revenue_bookings_bookbalance_base_v110_signal(deferredrev, ncfo, receivables):
    rc = _f19_drev_to_cash(deferredrev, ncfo)
    rr = _f19_drev_to_recv(deferredrev, receivables)
    b = np.tanh(rc) - np.tanh(rr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend sign persistence (consistent direction of subscription coverage)
def f19db_f19_deferred_revenue_bookings_coversign_base_v111_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    mom = c - c.shift(21)
    sgn = np.sign(mom)
    b = sgn.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings-to-revenue spread accel: 2nd diff of the billings gap (demand inflection)
def f19db_f19_deferred_revenue_bookings_billaccel_base_v112_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    gap = bill / revenue.replace(0, np.nan) - 1.0
    b = gap - 2.0 * gap.shift(63) + gap.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log(drev)-vs-log(revenue) spread acceleration (2nd diff of log-coverage spread)
def f19db_f19_deferred_revenue_bookings_logspread_base_v113_signal(deferredrev, revenue):
    spread = np.log(deferredrev.replace(0, np.nan)) - np.log(revenue.replace(0, np.nan))
    b = spread - 2.0 * spread.shift(63) + spread.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-to-receivables vs deferred coverage (cash collection vs forward book)
def f19db_f19_deferred_revenue_bookings_collvsbook_base_v114_signal(deferredrev, revenue, ncfo, receivables):
    coll = ncfo / receivables.replace(0, np.nan)
    cover = _f19_coverage(deferredrev, revenue)
    b = np.tanh(coll) - cover
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue momentum risk-adjusted by receivables volatility (clean book signal)
def f19db_f19_deferred_revenue_bookings_drevvol2_base_v115_signal(deferredrev, receivables):
    g = _f19_drev_growth(deferredrev, 63)
    recvol = _std(receivables.pct_change(21), 252)
    b = g / recvol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the last 2yr coverage stayed in upper third of its range (durable visibility)
def f19db_f19_deferred_revenue_bookings_uppervis_base_v116_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    hi = _rmax(c, 504)
    lo = _rmin(c, 504)
    pos = (c - lo) / (hi - lo).replace(0, np.nan)
    upper = (pos >= 0.6667).astype(float)
    b = upper.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net new bookings entries into negative territory (book-erosion event count)
def f19db_f19_deferred_revenue_bookings_erosioncnt_base_v117_signal(deferredrev):
    delta = deferredrev - deferredrev.shift(21)
    neg = (delta < 0).astype(float)
    entries = ((neg == 1) & (neg.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = (-delta / _mean(deferredrev, 252).replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 20.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaled by lagged deferred book (recognition of prior-year bookings)
def f19db_f19_deferred_revenue_bookings_lagrecog_base_v118_signal(deferredrev, revenue):
    b = revenue / deferredrev.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# positive-operating-cash regime fraction modulated by coverage level (cash+visibility count)
def f19db_f19_deferred_revenue_bookings_cashregime_base_v119_signal(deferredrev, revenue, ncfo):
    c = _f19_coverage(deferredrev, revenue)
    hi_cov = (c > c.rolling(252, min_periods=126).median()).astype(float)
    poscash = (ncfo > 0).astype(float)
    both = (hi_cov * poscash).rolling(252, min_periods=126).mean()
    b = both - 0.5 * poscash.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy growth z-scored over a short window (near-term demand impulse)
def f19db_f19_deferred_revenue_bookings_billimpulse_base_v120_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    bg = np.log(bill.replace(0, np.nan) / bill.shift(63).replace(0, np.nan))
    b = _z(bg, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue / receivables drawdown vs 504d max (book draining vs billing)
def f19db_f19_deferred_revenue_bookings_drevrecv_dd_base_v121_signal(deferredrev, receivables):
    r = _f19_drev_to_recv(deferredrev, receivables)
    hi = _rmax(r, 504)
    b = r / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage half-life proxy: coverage / its 252d slope magnitude (regime persistence)
def f19db_f19_deferred_revenue_bookings_coverhalf_base_v122_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    slp = _slope(c, 252).abs()
    b = c / slp.replace(0, np.nan)
    result = b
    return np.log1p(result).replace([np.inf, -np.inf], np.nan)


# net bookings minus revenue change vs cash (organic accretion cash-backed)
def f19db_f19_deferred_revenue_bookings_orgcash_base_v123_signal(deferredrev, revenue, ncfo):
    ddelta = deferredrev - deferredrev.shift(63)
    rdelta = revenue - revenue.shift(63)
    b = (ddelta - rdelta) / ncfo.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue growth vs its long-run trend slope (above/below structural pace)
def f19db_f19_deferred_revenue_bookings_paceres_base_v124_signal(deferredrev):
    g63 = _f19_drev_growth(deferredrev, 63)
    ld = np.log(deferredrev.replace(0, np.nan))
    trend = _slope(ld, 504) * 63.0
    b = g63 - trend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage entropy proxy: rolling range of coverage / IQR-like dispersion
def f19db_f19_deferred_revenue_bookings_coverdisp2_base_v125_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    q80 = c.rolling(252, min_periods=126).quantile(0.8)
    q20 = c.rolling(252, min_periods=126).quantile(0.2)
    b = (q80 - q20) / _mean(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings-to-book ratio momentum (recognition+booking pace vs standing book, change)
def f19db_f19_deferred_revenue_bookings_billvsbook_base_v126_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    ratio = bill / deferredrev.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables growth minus deferred growth ranked (billing-led vs booking-led demand)
def f19db_f19_deferred_revenue_bookings_billled_base_v127_signal(deferredrev, receivables):
    recg = np.log(receivables.replace(0, np.nan) / receivables.shift(63).replace(0, np.nan))
    dg = _f19_drev_growth(deferredrev, 63)
    spread = recg - dg
    b = spread.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash per dollar of revenue, weighted by forward mix (forward-cash quality)
def f19db_f19_deferred_revenue_bookings_fwdcashqual_base_v128_signal(deferredrev, revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    mix = deferredrev / (revenue + deferredrev).replace(0, np.nan)
    b = cm * mix
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue acceleration over a quarter, vol-scaled (forward-demand inflection z)
def f19db_f19_deferred_revenue_bookings_drevacc_z_base_v129_signal(deferredrev):
    g = _f19_drev_growth(deferredrev, 63)
    acc = g - g.shift(63)
    b = acc / _std(g, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage above long-run median, magnitude-weighted (visibility premium)
def f19db_f19_deferred_revenue_bookings_vispremium_base_v130_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    med = c.rolling(504, min_periods=252).median()
    b = (c - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings vs cash, sign-and-magnitude compressed (cash-funded book direction)
def f19db_f19_deferred_revenue_bookings_netcashsm_base_v131_signal(deferredrev, ncfo):
    delta = deferredrev - deferredrev.shift(63)
    ratio = delta / ncfo.abs().replace(0, np.nan)
    b = np.sign(ratio) * np.log1p(ratio.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage trend minus billings trend (book-coverage vs demand-pace divergence)
def f19db_f19_deferred_revenue_bookings_coverbilldiv_base_v132_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    bill = _f19_billings(deferredrev, revenue, 63)
    cslp = _slope(c, 126)
    bslp = _slope(np.log(bill.replace(0, np.nan).clip(lower=1.0)), 126)
    b = np.tanh(50.0 * cslp) - np.tanh(50.0 * bslp)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-rev to revenue, smoothed slope of the log ratio (structural coverage drift)
def f19db_f19_deferred_revenue_bookings_logcoverslp_base_v133_signal(deferredrev, revenue):
    lc = np.log(_f19_coverage(deferredrev, revenue).clip(lower=1e-6))
    b = _slope(lc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings intensity quarter-over-quarter change (forward-demand 2nd derivative level)
def f19db_f19_deferred_revenue_bookings_netqoq_base_v134_signal(deferredrev, revenue):
    delta = deferredrev - deferredrev.shift(63)
    intensity = delta / revenue.replace(0, np.nan)
    b = intensity - intensity.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash drawdown vs deferred book (cash strain relative to standing book)
def f19db_f19_deferred_revenue_bookings_cashstrain_base_v135_signal(deferredrev, ncfo):
    ratio = ncfo / deferredrev.replace(0, np.nan)
    hi = _rmax(ratio, 252)
    b = ratio - hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage percentile in 252d window minus same a year ago (regime migration)
def f19db_f19_deferred_revenue_bookings_covermigr_base_v136_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    rk = c.rolling(252, min_periods=126).rank(pct=True)
    b = rk - rk.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy / receivables momentum (forward demand vs collection drift)
def f19db_f19_deferred_revenue_bookings_billrecvmom_base_v137_signal(deferredrev, revenue, receivables):
    bill = _f19_billings(deferredrev, revenue, 63)
    ratio = bill / receivables.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue compound book-build vs receivables compound (relative two-year build)
def f19db_f19_deferred_revenue_bookings_relbuild504_base_v138_signal(deferredrev, receivables):
    dg = _f19_drev_growth(deferredrev, 504)
    recg = np.log(receivables.replace(0, np.nan) / receivables.shift(504).replace(0, np.nan))
    b = dg - recg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage vs cash-conversion balance composite (visible-and-collecting book score)
def f19db_f19_deferred_revenue_bookings_balcomp_base_v139_signal(deferredrev, revenue, ncfo):
    crank = _f19_coverage(deferredrev, revenue).rolling(504, min_periods=126).rank(pct=True) - 0.5
    conv = ncfo / deferredrev.replace(0, np.nan)
    convrank = conv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    b = 0.6 * crank + 0.4 * convrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred-revenue 5d-vol normalized by 63d-vol (book volatility term structure)
def f19db_f19_deferred_revenue_bookings_volterm_base_v140_signal(deferredrev):
    ch = deferredrev.pct_change()
    short = _std(ch, 21)
    long = _std(ch, 126)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue recognition vs new bookings ratio change (recognition outpacing booking)
def f19db_f19_deferred_revenue_bookings_recogratio_base_v141_signal(deferredrev, revenue):
    newbook = (deferredrev - deferredrev.shift(63)).clip(lower=0)
    recog = revenue
    ratio = recog / (newbook + revenue).replace(0, np.nan)
    b = ratio - _mean(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage tail risk: 5th-percentile coverage distance from current (downside visibility)
def f19db_f19_deferred_revenue_bookings_covertail_base_v142_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    q05 = c.rolling(504, min_periods=252).quantile(0.05)
    b = (c - q05) / c.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net bookings cash-backing trend over a year (improving cash backing of new book)
def f19db_f19_deferred_revenue_bookings_backtrend_base_v143_signal(deferredrev, ncfo):
    delta = deferredrev - deferredrev.shift(63)
    backing = ncfo / delta.replace(0, np.nan)
    b = _slope(np.tanh(backing), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# billings proxy YoY growth minus revenue YoY growth, smoothed (durable demand lead)
def f19db_f19_deferred_revenue_bookings_durablelead_base_v144_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 126)
    bg = np.log(bill.replace(0, np.nan) / bill.shift(252).replace(0, np.nan))
    rg = np.log(revenue.replace(0, np.nan) / revenue.shift(252).replace(0, np.nan))
    b = (bg - rg).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred book / receivables, curvature (book-vs-billing inflection)
def f19db_f19_deferred_revenue_bookings_drevrecvcurv_base_v145_signal(deferredrev, receivables):
    r = _f19_drev_to_recv(deferredrev, receivables)
    b = r - 2.0 * r.shift(63) + r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year billings exceeded revenue (forward-booked-growth regime)
def f19db_f19_deferred_revenue_bookings_billdom_base_v146_signal(deferredrev, revenue):
    bill = _f19_billings(deferredrev, revenue, 63)
    dom = (bill > revenue).astype(float)
    b = dom.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coverage x book-build interaction, ranked (high-coverage-and-growing composite)
def f19db_f19_deferred_revenue_bookings_growcover_base_v147_signal(deferredrev, revenue):
    c = _f19_coverage(deferredrev, revenue)
    g = _f19_drev_growth(deferredrev, 63)
    inter = c * g
    b = inter.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-cash-margin trend net of book-turnover trend (cash efficiency vs recognition trend)
def f19db_f19_deferred_revenue_bookings_cashnetturn_base_v148_signal(deferredrev, revenue, ncfo):
    cm = ncfo / revenue.replace(0, np.nan)
    turn = revenue / deferredrev.replace(0, np.nan)
    b = np.tanh(50.0 * _slope(cm, 126)) - np.tanh(50.0 * _slope(turn, 126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deferred revenue + receivables (total billed pipeline) growth (gross demand pipeline)
def f19db_f19_deferred_revenue_bookings_pipegrowth_base_v149_signal(deferredrev, receivables):
    pipe = deferredrev + receivables
    b = np.log(pipe.replace(0, np.nan) / pipe.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite forward-demand health: book-build rank + coverage trend - cash-strain rank
def f19db_f19_deferred_revenue_bookings_fwdhealth_base_v150_signal(deferredrev, revenue, ncfo):
    g = _f19_drev_growth(deferredrev, 126)
    grank = g.rolling(504, min_periods=126).rank(pct=True) - 0.5
    c = _f19_coverage(deferredrev, revenue)
    cslp = np.tanh(50.0 * _slope(c, 252))
    strain = (ncfo / deferredrev.replace(0, np.nan))
    strainrank = strain.rolling(504, min_periods=126).rank(pct=True) - 0.5
    b = 0.5 * grank + 0.3 * cslp + 0.2 * strainrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19db_f19_deferred_revenue_bookings_logdrev_ext_base_v076_signal,
    f19db_f19_deferred_revenue_bookings_coversz_base_v077_signal,
    f19db_f19_deferred_revenue_bookings_billrecv_z_base_v078_signal,
    f19db_f19_deferred_revenue_bookings_coverskew_base_v079_signal,
    f19db_f19_deferred_revenue_bookings_drevkurt_base_v080_signal,
    f19db_f19_deferred_revenue_bookings_buildspr_base_v081_signal,
    f19db_f19_deferred_revenue_bookings_cover_z63_base_v082_signal,
    f19db_f19_deferred_revenue_bookings_netbook126_base_v083_signal,
    f19db_f19_deferred_revenue_bookings_drevcash_pos_base_v084_signal,
    f19db_f19_deferred_revenue_bookings_bookturn_base_v085_signal,
    f19db_f19_deferred_revenue_bookings_bookturn_mom_base_v086_signal,
    f19db_f19_deferred_revenue_bookings_cashqual_base_v087_signal,
    f19db_f19_deferred_revenue_bookings_twinexp_base_v088_signal,
    f19db_f19_deferred_revenue_bookings_billcash_base_v089_signal,
    f19db_f19_deferred_revenue_bookings_cover_slp504_base_v090_signal,
    f19db_f19_deferred_revenue_bookings_drev_accel21_base_v091_signal,
    f19db_f19_deferred_revenue_bookings_drevrecv_disp_base_v092_signal,
    f19db_f19_deferred_revenue_bookings_netvisib_base_v093_signal,
    f19db_f19_deferred_revenue_bookings_fwdmix_base_v094_signal,
    f19db_f19_deferred_revenue_bookings_fwdmix_mom_base_v095_signal,
    f19db_f19_deferred_revenue_bookings_annbook_base_v096_signal,
    f19db_f19_deferred_revenue_bookings_cashbill_base_v097_signal,
    f19db_f19_deferred_revenue_bookings_covercv_base_v098_signal,
    f19db_f19_deferred_revenue_bookings_pulse_base_v099_signal,
    f19db_f19_deferred_revenue_bookings_recogpace_base_v100_signal,
    f19db_f19_deferred_revenue_bookings_bookdd_base_v101_signal,
    f19db_f19_deferred_revenue_bookings_coverboll_base_v102_signal,
    f19db_f19_deferred_revenue_bookings_cleanintens_base_v103_signal,
    f19db_f19_deferred_revenue_bookings_convimprove_base_v104_signal,
    f19db_f19_deferred_revenue_bookings_billpos_base_v105_signal,
    f19db_f19_deferred_revenue_bookings_coveryoy_z_base_v106_signal,
    f19db_f19_deferred_revenue_bookings_cashvalid_base_v107_signal,
    f19db_f19_deferred_revenue_bookings_coverampl_base_v108_signal,
    f19db_f19_deferred_revenue_bookings_netsurprise_base_v109_signal,
    f19db_f19_deferred_revenue_bookings_bookbalance_base_v110_signal,
    f19db_f19_deferred_revenue_bookings_coversign_base_v111_signal,
    f19db_f19_deferred_revenue_bookings_billaccel_base_v112_signal,
    f19db_f19_deferred_revenue_bookings_logspread_base_v113_signal,
    f19db_f19_deferred_revenue_bookings_collvsbook_base_v114_signal,
    f19db_f19_deferred_revenue_bookings_drevvol2_base_v115_signal,
    f19db_f19_deferred_revenue_bookings_uppervis_base_v116_signal,
    f19db_f19_deferred_revenue_bookings_erosioncnt_base_v117_signal,
    f19db_f19_deferred_revenue_bookings_lagrecog_base_v118_signal,
    f19db_f19_deferred_revenue_bookings_cashregime_base_v119_signal,
    f19db_f19_deferred_revenue_bookings_billimpulse_base_v120_signal,
    f19db_f19_deferred_revenue_bookings_drevrecv_dd_base_v121_signal,
    f19db_f19_deferred_revenue_bookings_coverhalf_base_v122_signal,
    f19db_f19_deferred_revenue_bookings_orgcash_base_v123_signal,
    f19db_f19_deferred_revenue_bookings_paceres_base_v124_signal,
    f19db_f19_deferred_revenue_bookings_coverdisp2_base_v125_signal,
    f19db_f19_deferred_revenue_bookings_billvsbook_base_v126_signal,
    f19db_f19_deferred_revenue_bookings_billled_base_v127_signal,
    f19db_f19_deferred_revenue_bookings_fwdcashqual_base_v128_signal,
    f19db_f19_deferred_revenue_bookings_drevacc_z_base_v129_signal,
    f19db_f19_deferred_revenue_bookings_vispremium_base_v130_signal,
    f19db_f19_deferred_revenue_bookings_netcashsm_base_v131_signal,
    f19db_f19_deferred_revenue_bookings_coverbilldiv_base_v132_signal,
    f19db_f19_deferred_revenue_bookings_logcoverslp_base_v133_signal,
    f19db_f19_deferred_revenue_bookings_netqoq_base_v134_signal,
    f19db_f19_deferred_revenue_bookings_cashstrain_base_v135_signal,
    f19db_f19_deferred_revenue_bookings_covermigr_base_v136_signal,
    f19db_f19_deferred_revenue_bookings_billrecvmom_base_v137_signal,
    f19db_f19_deferred_revenue_bookings_relbuild504_base_v138_signal,
    f19db_f19_deferred_revenue_bookings_balcomp_base_v139_signal,
    f19db_f19_deferred_revenue_bookings_volterm_base_v140_signal,
    f19db_f19_deferred_revenue_bookings_recogratio_base_v141_signal,
    f19db_f19_deferred_revenue_bookings_covertail_base_v142_signal,
    f19db_f19_deferred_revenue_bookings_backtrend_base_v143_signal,
    f19db_f19_deferred_revenue_bookings_durablelead_base_v144_signal,
    f19db_f19_deferred_revenue_bookings_drevrecvcurv_base_v145_signal,
    f19db_f19_deferred_revenue_bookings_billdom_base_v146_signal,
    f19db_f19_deferred_revenue_bookings_growcover_base_v147_signal,
    f19db_f19_deferred_revenue_bookings_cashnetturn_base_v148_signal,
    f19db_f19_deferred_revenue_bookings_pipegrowth_base_v149_signal,
    f19db_f19_deferred_revenue_bookings_fwdhealth_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_DEFERRED_REVENUE_BOOKINGS_REGISTRY_076_150 = REGISTRY


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

    print("OK f19_deferred_revenue_bookings_base_076_150_claude: %d features pass" % n_features)
