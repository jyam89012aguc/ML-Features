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


# ===== folder domain primitives (asset backing / NAV) =====
def _f42_tangible_book(equity, intangibles):
    # tangible book value = equity minus intangibles (NAV core)
    return equity - intangibles


def _f42_pb_proxy(marketcap, equity):
    # price-to-book proxy from marketcap and book equity
    return marketcap / equity.replace(0, np.nan)


def _f42_ptb(marketcap, equity, intangibles):
    # price-to-tangible-book
    tb = (equity - intangibles).replace(0, np.nan)
    return marketcap / tb


def _f42_discount_to_nav(marketcap, equity, intangibles):
    # discount to tangible NAV: (TB - mcap)/TB ; positive => trades below NAV
    tb = (equity - intangibles).replace(0, np.nan)
    return (tb - marketcap) / tb


def _f42_book_yield(equity, marketcap):
    # book-yield: book equity per dollar of market cap
    return equity / marketcap.replace(0, np.nan)


def _f42_tangible_share(tangibles, assets):
    # tangible-asset share of the balance sheet
    return tangibles / assets.replace(0, np.nan)


# ============================================================
# raw price-to-book multiple
def f42nb_f42_asset_backing_nav_pb_001d_base_v001_signal(pb):
    b = pb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B-proxy (marketcap/equity) z-scored vs its own 126d history (independent NAV-multiple extreme)
def f42nb_f42_asset_backing_nav_pbproxy_001d_base_v002_signal(marketcap, equity):
    pbx = _f42_pb_proxy(marketcap, equity)
    b = _z(pbx, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-book z-scored vs its own 252d history (tangible-multiple cheapness extreme)
def f42nb_f42_asset_backing_nav_ptb_001d_base_v003_signal(marketcap, equity, intangibles):
    ptb = _f42_ptb(marketcap, equity, intangibles)
    b = _z(ptb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-gross-assets momentum over a quarter (asset-backing re-rating velocity)
def f42nb_f42_asset_backing_nav_discnav_001d_base_v004_signal(marketcap, assets):
    pa = marketcap / assets.replace(0, np.nan)
    b = pa - pa.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield: book equity per dollar of market value (canonical NAV yield level)
def f42nb_f42_asset_backing_nav_bookyield_001d_base_v005_signal(equity, marketcap):
    b = _f42_book_yield(equity, marketcap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share of total assets (hard-asset backing of the balance sheet)
def f42nb_f42_asset_backing_nav_tangshare_001d_base_v006_signal(tangibles, assets):
    b = _f42_tangible_share(tangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-P/B detrended by its own 252d mean (cyclical cheapness of the log multiple)
def f42nb_f42_asset_backing_nav_logpb_001d_base_v007_signal(pb):
    lp = np.log(pb.replace(0, np.nan).clip(lower=1e-6))
    b = lp - _mean(lp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-overhang momentum: change in intangibles/equity over a half-year (book-quality drift)
def f42nb_f42_asset_backing_nav_tbyield_001d_base_v008_signal(intangibles, equity):
    ie = intangibles / equity.replace(0, np.nan)
    b = ie - ie.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible drag: intangibles as a share of equity (book-quality erosion)
def f42nb_f42_asset_backing_nav_intangdrag_001d_base_v009_signal(intangibles, equity):
    b = intangibles / equity.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets (book leverage cushion underpinning NAV)
def f42nb_f42_asset_backing_nav_eqassets_001d_base_v010_signal(equity, assets):
    b = equity / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of P/B vs its own 252d cyclical history (cheap-vs-history)
def f42nb_f42_asset_backing_nav_pbz_252d_base_v011_signal(pb):
    b = _z(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B dispersion over 504d (multiple instability across the cycle, level form)
def f42nb_f42_asset_backing_nav_pbz_504d_base_v012_signal(pb):
    b = _std(pb, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-book momentum over a quarter (tangible-multiple re-rating velocity)
def f42nb_f42_asset_backing_nav_ptbz_252d_base_v013_signal(marketcap, equity, intangibles):
    ptb = _f42_ptb(marketcap, equity, intangibles)
    b = ptb - ptb.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV z-scored vs 504d cyclical history
def f42nb_f42_asset_backing_nav_discnavz_504d_base_v014_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield curvature: second difference of book-yield over a quarter grid (NAV-yield bend)
def f42nb_f42_asset_backing_nav_byieldz_252d_base_v015_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    b = by - 2.0 * by.shift(63) + by.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of P/B vs its 504d history (cheapness rank)
def f42nb_f42_asset_backing_nav_pbrank_504d_base_v016_signal(pb):
    b = _rank(pb, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of discount-to-NAV vs 1260d multi-cycle history
def f42nb_f42_asset_backing_nav_discnavrank_504d_base_v017_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = _rank(d, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of tangible-asset share vs 252d (asset-backing rank)
def f42nb_f42_asset_backing_nav_tangsharerank_252d_base_v018_signal(tangibles, assets):
    ts = _f42_tangible_share(tangibles, assets)
    b = _rank(ts, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B fast vs slow EMA crossover (cheapening/re-rating oscillator)
def f42nb_f42_asset_backing_nav_pbgap_252d_base_v019_signal(pb):
    fast = pb.ewm(span=21, min_periods=10).mean()
    slow = pb.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-book trough distance over 1260d (multi-cycle tangible cheapness)
def f42nb_f42_asset_backing_nav_ptbgap_126d_base_v020_signal(marketcap, equity, intangibles):
    ptb = _f42_ptb(marketcap, equity, intangibles)
    lo = _rmin(ptb, 1260)
    b = (ptb - lo) / lo.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: pb-proxy minus reported pb (book-measurement disagreement)
def f42nb_f42_asset_backing_nav_pbspread_001d_base_v021_signal(marketcap, equity, pb):
    proxy = _f42_pb_proxy(marketcap, equity)
    b = proxy - pb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wedge: price-to-tangible-book minus P/B proxy (intangible premium in the multiple)
def f42nb_f42_asset_backing_nav_pbptbwedge_001d_base_v022_signal(marketcap, equity, intangibles):
    pbx = _f42_pb_proxy(marketcap, equity)
    ptb = _f42_ptb(marketcap, equity, intangibles)
    b = ptb - pbx
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing per dollar of market value (tangibles / marketcap)
def f42nb_f42_asset_backing_nav_tangbackmc_001d_base_v023_signal(tangibles, marketcap):
    b = tangibles / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-asset backing per dollar of market value (assets / marketcap)
def f42nb_f42_asset_backing_nav_assetbackmc_001d_base_v024_signal(assets, marketcap):
    b = assets / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book coverage of market cap, quarter momentum minus its 252d drift (coverage impulse)
def f42nb_f42_asset_backing_nav_tbcover_001d_base_v025_signal(equity, intangibles, marketcap):
    tb = _f42_tangible_book(equity, intangibles)
    cov = (tb / marketcap.replace(0, np.nan)).clip(lower=-5, upper=5)
    mom = cov - cov.shift(63)
    b = mom - _mean(mom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B momentum: change over a quarter (re-rating velocity)
def f42nb_f42_asset_backing_nav_pbmom_63d_base_v026_signal(pb):
    b = pb - pb.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log change in P/B over a year (cyclical re-rating, log form)
def f42nb_f42_asset_backing_nav_pblogchg_252d_base_v027_signal(pb):
    b = np.log(pb.replace(0, np.nan) / pb.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV curvature: second difference over a quarter grid (NAV-gap bend)
def f42nb_f42_asset_backing_nav_discnavchg_63d_base_v028_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = d - 2.0 * d.shift(63) + d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield momentum over a half-year
def f42nb_f42_asset_backing_nav_byieldmom_126d_base_v029_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    b = by - by.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share momentum over a year (hard-asset accumulation)
def f42nb_f42_asset_backing_nav_tangsharemom_252d_base_v030_signal(tangibles, assets):
    ts = _f42_tangible_share(tangibles, assets)
    b = ts - ts.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B distance from its 126d median, normalized by price (short-horizon mean-reversion gap)
def f42nb_f42_asset_backing_nav_pbrev_252d_base_v031_signal(pb):
    med = pb.rolling(126, min_periods=63).median()
    b = (pb - med) / pb.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book yield mean-reversion vs 252d mean
def f42nb_f42_asset_backing_nav_tbyrev_252d_base_v032_signal(equity, intangibles, marketcap):
    tb = _f42_tangible_book(equity, intangibles)
    tby = tb / marketcap.replace(0, np.nan)
    b = tby - _mean(tby, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheapness extreme: how far above 504d min-band P/B sits (deep-value distance)
def f42nb_f42_asset_backing_nav_pbtrough_504d_base_v033_signal(pb):
    lo = _rmin(pb, 504)
    b = (pb - lo) / lo.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# richness extreme: how far below 504d max-band P/B sits (room to re-rate down)
def f42nb_f42_asset_backing_nav_pbpeak_504d_base_v034_signal(pb):
    hi = _rmax(pb, 504)
    b = (hi - pb) / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position of P/B within its 504d range (cycle valuation phase)
def f42nb_f42_asset_backing_nav_pbrangepos_504d_base_v035_signal(pb):
    hi = _rmax(pb, 504)
    lo = _rmin(pb, 504)
    b = (pb - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-book year-over-year log change (tangible-multiple cyclical re-rating)
def f42nb_f42_asset_backing_nav_ptbrangepos_1260d_base_v036_signal(marketcap, equity, intangibles):
    ptb = _f42_ptb(marketcap, equity, intangibles).clip(lower=1e-6)
    b = np.log(ptb / ptb.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV position within its 252d range (shorter NAV-gap cycle phase)
def f42nb_f42_asset_backing_nav_discnavpos_504d_base_v037_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    hi = _rmax(d, 252)
    lo = _rmin(d, 252)
    b = (d - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield range position within 252d (yield-cycle phase)
def f42nb_f42_asset_backing_nav_byieldpos_252d_base_v038_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    hi = _rmax(by, 252)
    lo = _rmin(by, 252)
    b = (by - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible NAV growth proxy: log growth of tangible book over a year
def f42nb_f42_asset_backing_nav_tbgrowth_252d_base_v039_signal(equity, intangibles):
    tb = _f42_tangible_book(equity, intangibles).clip(lower=1e-6)
    b = np.log(tb / tb.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity (NAV) growth over a half-year (book accretion vs dilution)
def f42nb_f42_asset_backing_nav_eqgrowth_126d_base_v040_signal(equity):
    b = np.log(equity.replace(0, np.nan).clip(lower=1e-6) / equity.shift(126).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# assets base growth over a year (capacity/reserve backing expansion)
def f42nb_f42_asset_backing_nav_assetgrowth_252d_base_v041_signal(assets):
    b = np.log(assets.replace(0, np.nan).clip(lower=1e-6) / assets.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible asset wedge growth: log-growth of (assets - tangibles) over a year (soft-asset build)
def f42nb_f42_asset_backing_nav_tangmix_252d_base_v042_signal(tangibles, assets):
    soft = (assets - tangibles).clip(lower=1e-6)
    b = np.log(soft / soft.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NAV accretion vs price re-rating: equity growth minus P/B growth (value vs hype)
def f42nb_f42_asset_backing_nav_navvsmult_252d_base_v043_signal(equity, pb):
    ge = np.log(equity.replace(0, np.nan).clip(lower=1e-6) / equity.shift(252).clip(lower=1e-6))
    gp = np.log(pb.replace(0, np.nan).clip(lower=1e-6) / pb.shift(252).clip(lower=1e-6))
    b = ge - gp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap growth vs NAV growth (price outrunning book)
def f42nb_f42_asset_backing_nav_mcvsnav_252d_base_v044_signal(marketcap, equity):
    gm = np.log(marketcap.replace(0, np.nan).clip(lower=1e-6) / marketcap.shift(252).clip(lower=1e-6))
    ge = np.log(equity.replace(0, np.nan).clip(lower=1e-6) / equity.shift(252).clip(lower=1e-6))
    b = gm - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-to-price (inverse P/B) curvature: second difference over a quarter grid (cheapness bend)
def f42nb_f42_asset_backing_nav_invpb_001d_base_v045_signal(pb):
    btp = (1.0 / pb.replace(0, np.nan)).clip(upper=20)
    b = btp - 2.0 * btp.shift(63) + btp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-discount day count: days in the last year the NAV discount exceeds its 504d median (count-friendly)
def f42nb_f42_asset_backing_nav_discsignmag_001d_base_v046_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    med = d.rolling(504, min_periods=252).median()
    wide = (d > med).astype(float)
    b = wide.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed quarter-over-quarter change in P/B z (bounded re-rating impulse)
def f42nb_f42_asset_backing_nav_pbztanh_252d_base_v047_signal(pb):
    z = _z(pb, 252)
    b = np.tanh(2.0 * (z - z.shift(63)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# hard-NAV over assets, z-scored vs 252d history (tangible-cushion extremity)
def f42nb_f42_asset_backing_nav_hardnavassets_001d_base_v048_signal(equity, intangibles, assets):
    tba = _f42_tangible_book(equity, intangibles) / assets.replace(0, np.nan)
    b = _z(tba, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-quality trend: change in tangible-share-of-equity over a year (quality drift)
def f42nb_f42_asset_backing_nav_bookquality_001d_base_v049_signal(equity, intangibles):
    tb = _f42_tangible_book(equity, intangibles)
    q = tb / equity.replace(0, np.nan)
    b = q - q.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles vs equity coverage (hard-asset backing of book)
def f42nb_f42_asset_backing_nav_tangeqcover_001d_base_v050_signal(tangibles, equity):
    b = tangibles / equity.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of P/B over a year (multiple instability through the cycle)
def f42nb_f42_asset_backing_nav_pbvol_252d_base_v051_signal(pb):
    b = _std(pb, 252) / _mean(pb, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coefficient of variation of book-yield over a half-year (NAV-yield instability)
def f42nb_f42_asset_backing_nav_byieldvol_126d_base_v052_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    b = _std(by, 126) / _mean(by, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B short vs long mean ratio (recent cheapening vs cyclical norm)
def f42nb_f42_asset_backing_nav_pbshortlong_001d_base_v053_signal(pb):
    short = _mean(pb, 63)
    long = _mean(pb, 504)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-book short vs long ratio
def f42nb_f42_asset_backing_nav_ptbshortlong_001d_base_v054_signal(marketcap, equity, intangibles):
    ptb = _f42_ptb(marketcap, equity, intangibles)
    short = _mean(ptb, 63)
    long = _mean(ptb, 504)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV smoothed level (persistent below-NAV regime)
def f42nb_f42_asset_backing_nav_discnavema_001d_base_v055_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = d.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV displacement from its slow EMA (NAV-gap surprise vs trend)
def f42nb_f42_asset_backing_nav_discnavdisp_001d_base_v056_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = d - d.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-NAV streak: consecutive days the discount sits above its 252d median (regime persistence)
def f42nb_f42_asset_backing_nav_belownavfrac_252d_base_v057_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    med = d.rolling(252, min_periods=126).median()
    cheap = (d > med).astype(float)
    grp = (cheap != cheap.shift(1)).cumsum()
    streak = cheap.groupby(grp).cumsum()
    b = streak.rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-P/B time-in-regime weighted by depth below the 252d median (count + magnitude)
def f42nb_f42_asset_backing_nav_subonefrac_252d_base_v058_signal(pb):
    med = pb.rolling(252, min_periods=126).median()
    below = (pb < med).astype(float)
    frac = below.rolling(252, min_periods=126).mean()
    depth = (med - pb).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield reinforced cheapness: book-yield times book-to-price (cheapness reinforcement)
def f42nb_f42_asset_backing_nav_cheapreinf_001d_base_v059_signal(equity, marketcap, pb):
    by = _f42_book_yield(equity, marketcap)
    btp = 1.0 / pb.replace(0, np.nan)
    b = (by * btp).clip(upper=50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible inflation z-scored vs 504d history (intangible-heavy regime extreme)
def f42nb_f42_asset_backing_nav_intanginflate_001d_base_v060_signal(intangibles, assets):
    ia = intangibles / assets.replace(0, np.nan)
    b = _z(ia, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing per market dollar, ranked vs 504d history
def f42nb_f42_asset_backing_nav_tangbackrank_504d_base_v061_signal(tangibles, marketcap):
    tbm = tangibles / marketcap.replace(0, np.nan)
    b = _rank(tbm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-backing coverage trend: assets/marketcap change over a half-year
def f42nb_f42_asset_backing_nav_assetcovtrend_126d_base_v062_signal(assets, marketcap):
    cov = assets / marketcap.replace(0, np.nan)
    b = cov - cov.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book-yield dispersion over 252d (tangible-NAV-yield instability through cycle)
def f42nb_f42_asset_backing_nav_tbyieldz_504d_base_v063_signal(equity, intangibles, marketcap):
    tb = _f42_tangible_book(equity, intangibles)
    tby = tb / marketcap.replace(0, np.nan)
    b = _std(tby, 252) / _mean(tby, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets momentum over a year (book-cushion build/erosion through the cycle)
def f42nb_f42_asset_backing_nav_eqassetsz_252d_base_v064_signal(equity, assets):
    ea = equity / assets.replace(0, np.nan)
    b = ea - ea.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B acceleration proxy: quarter momentum minus prior quarter momentum
def f42nb_f42_asset_backing_nav_pbmomchg_63d_base_v065_signal(pb):
    mom = pb - pb.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV dispersion over a year (instability of the NAV gap through the cycle)
def f42nb_f42_asset_backing_nav_discnavyoy_252d_base_v066_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = _std(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield percentile rank vs 1260d multi-cycle history (deep-value rank)
def f42nb_f42_asset_backing_nav_byieldrank_1260d_base_v067_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    b = _rank(by, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share dispersion (stability of hard-asset backing) over a year
def f42nb_f42_asset_backing_nav_tangsharestd_252d_base_v068_signal(tangibles, assets):
    ts = _f42_tangible_share(tangibles, assets)
    b = _std(ts, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NAV cushion displacement: tangible-book/assets minus its slow EMA (cushion surprise)
def f42nb_f42_asset_backing_nav_navcushion_001d_base_v069_signal(equity, intangibles, assets):
    tb = _f42_tangible_book(equity, intangibles)
    cush = tb / assets.replace(0, np.nan)
    b = cush - cush.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute distance from book parity, smoothed (mispricing magnitude either side of 1.0)
def f42nb_f42_asset_backing_nav_parityconv_001d_base_v070_signal(pb):
    dist = (pb - 1.0).abs().clip(upper=10)
    b = dist.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined deep-value gate: book-yield x tangible share (cheap AND hard-asset-backed)
def f42nb_f42_asset_backing_nav_deepvalgate_001d_base_v071_signal(equity, marketcap, tangibles, assets):
    by = _f42_book_yield(equity, marketcap)
    ts = _f42_tangible_share(tangibles, assets)
    b = (by * ts).clip(upper=20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-erosion velocity: change in intangibles/assets over a year (writedown setup)
def f42nb_f42_asset_backing_nav_intangvel_252d_base_v072_signal(intangibles, assets):
    ia = intangibles / assets.replace(0, np.nan)
    b = ia - ia.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV per unit of P/B volatility (risk-adjusted cheapness)
def f42nb_f42_asset_backing_nav_discperrisk_252d_base_v073_signal(marketcap, equity, intangibles, pb):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    vol = _std(pb, 252)
    b = (d / vol.replace(0, np.nan)).clip(lower=-50, upper=50)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-overhang on market cap, momentum over a quarter (soft-asset re-pricing)
def f42nb_f42_asset_backing_nav_tbtrough_1260d_base_v074_signal(intangibles, marketcap):
    im = intangibles / marketcap.replace(0, np.nan)
    b = im - im.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-cover regime balance: signed share of last year cheap vs rich vs its 252d median (tangibles/marketcap)
def f42nb_f42_asset_backing_nav_navbalance_63d_base_v075_signal(tangibles, marketcap):
    tc = tangibles / marketcap.replace(0, np.nan)
    med = tc.rolling(252, min_periods=126).median()
    cheap = (tc > med).astype(float)
    rich = (tc <= med).astype(float)
    fc = cheap.rolling(252, min_periods=126).mean()
    fr = rich.rolling(252, min_periods=126).mean()
    b = (fc - fr) / (fc + fr).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42nb_f42_asset_backing_nav_pb_001d_base_v001_signal,
    f42nb_f42_asset_backing_nav_pbproxy_001d_base_v002_signal,
    f42nb_f42_asset_backing_nav_ptb_001d_base_v003_signal,
    f42nb_f42_asset_backing_nav_discnav_001d_base_v004_signal,
    f42nb_f42_asset_backing_nav_bookyield_001d_base_v005_signal,
    f42nb_f42_asset_backing_nav_tangshare_001d_base_v006_signal,
    f42nb_f42_asset_backing_nav_logpb_001d_base_v007_signal,
    f42nb_f42_asset_backing_nav_tbyield_001d_base_v008_signal,
    f42nb_f42_asset_backing_nav_intangdrag_001d_base_v009_signal,
    f42nb_f42_asset_backing_nav_eqassets_001d_base_v010_signal,
    f42nb_f42_asset_backing_nav_pbz_252d_base_v011_signal,
    f42nb_f42_asset_backing_nav_pbz_504d_base_v012_signal,
    f42nb_f42_asset_backing_nav_ptbz_252d_base_v013_signal,
    f42nb_f42_asset_backing_nav_discnavz_504d_base_v014_signal,
    f42nb_f42_asset_backing_nav_byieldz_252d_base_v015_signal,
    f42nb_f42_asset_backing_nav_pbrank_504d_base_v016_signal,
    f42nb_f42_asset_backing_nav_discnavrank_504d_base_v017_signal,
    f42nb_f42_asset_backing_nav_tangsharerank_252d_base_v018_signal,
    f42nb_f42_asset_backing_nav_pbgap_252d_base_v019_signal,
    f42nb_f42_asset_backing_nav_ptbgap_126d_base_v020_signal,
    f42nb_f42_asset_backing_nav_pbspread_001d_base_v021_signal,
    f42nb_f42_asset_backing_nav_pbptbwedge_001d_base_v022_signal,
    f42nb_f42_asset_backing_nav_tangbackmc_001d_base_v023_signal,
    f42nb_f42_asset_backing_nav_assetbackmc_001d_base_v024_signal,
    f42nb_f42_asset_backing_nav_tbcover_001d_base_v025_signal,
    f42nb_f42_asset_backing_nav_pbmom_63d_base_v026_signal,
    f42nb_f42_asset_backing_nav_pblogchg_252d_base_v027_signal,
    f42nb_f42_asset_backing_nav_discnavchg_63d_base_v028_signal,
    f42nb_f42_asset_backing_nav_byieldmom_126d_base_v029_signal,
    f42nb_f42_asset_backing_nav_tangsharemom_252d_base_v030_signal,
    f42nb_f42_asset_backing_nav_pbrev_252d_base_v031_signal,
    f42nb_f42_asset_backing_nav_tbyrev_252d_base_v032_signal,
    f42nb_f42_asset_backing_nav_pbtrough_504d_base_v033_signal,
    f42nb_f42_asset_backing_nav_pbpeak_504d_base_v034_signal,
    f42nb_f42_asset_backing_nav_pbrangepos_504d_base_v035_signal,
    f42nb_f42_asset_backing_nav_ptbrangepos_1260d_base_v036_signal,
    f42nb_f42_asset_backing_nav_discnavpos_504d_base_v037_signal,
    f42nb_f42_asset_backing_nav_byieldpos_252d_base_v038_signal,
    f42nb_f42_asset_backing_nav_tbgrowth_252d_base_v039_signal,
    f42nb_f42_asset_backing_nav_eqgrowth_126d_base_v040_signal,
    f42nb_f42_asset_backing_nav_assetgrowth_252d_base_v041_signal,
    f42nb_f42_asset_backing_nav_tangmix_252d_base_v042_signal,
    f42nb_f42_asset_backing_nav_navvsmult_252d_base_v043_signal,
    f42nb_f42_asset_backing_nav_mcvsnav_252d_base_v044_signal,
    f42nb_f42_asset_backing_nav_invpb_001d_base_v045_signal,
    f42nb_f42_asset_backing_nav_discsignmag_001d_base_v046_signal,
    f42nb_f42_asset_backing_nav_pbztanh_252d_base_v047_signal,
    f42nb_f42_asset_backing_nav_hardnavassets_001d_base_v048_signal,
    f42nb_f42_asset_backing_nav_bookquality_001d_base_v049_signal,
    f42nb_f42_asset_backing_nav_tangeqcover_001d_base_v050_signal,
    f42nb_f42_asset_backing_nav_pbvol_252d_base_v051_signal,
    f42nb_f42_asset_backing_nav_byieldvol_126d_base_v052_signal,
    f42nb_f42_asset_backing_nav_pbshortlong_001d_base_v053_signal,
    f42nb_f42_asset_backing_nav_ptbshortlong_001d_base_v054_signal,
    f42nb_f42_asset_backing_nav_discnavema_001d_base_v055_signal,
    f42nb_f42_asset_backing_nav_discnavdisp_001d_base_v056_signal,
    f42nb_f42_asset_backing_nav_belownavfrac_252d_base_v057_signal,
    f42nb_f42_asset_backing_nav_subonefrac_252d_base_v058_signal,
    f42nb_f42_asset_backing_nav_cheapreinf_001d_base_v059_signal,
    f42nb_f42_asset_backing_nav_intanginflate_001d_base_v060_signal,
    f42nb_f42_asset_backing_nav_tangbackrank_504d_base_v061_signal,
    f42nb_f42_asset_backing_nav_assetcovtrend_126d_base_v062_signal,
    f42nb_f42_asset_backing_nav_tbyieldz_504d_base_v063_signal,
    f42nb_f42_asset_backing_nav_eqassetsz_252d_base_v064_signal,
    f42nb_f42_asset_backing_nav_pbmomchg_63d_base_v065_signal,
    f42nb_f42_asset_backing_nav_discnavyoy_252d_base_v066_signal,
    f42nb_f42_asset_backing_nav_byieldrank_1260d_base_v067_signal,
    f42nb_f42_asset_backing_nav_tangsharestd_252d_base_v068_signal,
    f42nb_f42_asset_backing_nav_navcushion_001d_base_v069_signal,
    f42nb_f42_asset_backing_nav_parityconv_001d_base_v070_signal,
    f42nb_f42_asset_backing_nav_deepvalgate_001d_base_v071_signal,
    f42nb_f42_asset_backing_nav_intangvel_252d_base_v072_signal,
    f42nb_f42_asset_backing_nav_discperrisk_252d_base_v073_signal,
    f42nb_f42_asset_backing_nav_tbtrough_1260d_base_v074_signal,
    f42nb_f42_asset_backing_nav_navbalance_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_ASSET_BACKING_NAV_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.5
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    # asset-backing / NAV inputs: pb small positive; balance-sheet items positive; tangibles < assets
    pb = _fund(101, base=1.5, drift=0.0, vol=0.10).clip(lower=0.3, upper=5.0).rename("pb")
    marketcap = _fund(102, base=5e8, drift=0.0, vol=0.09).clip(lower=1e6).rename("marketcap")
    equity = _fund(103, base=4e8, drift=0.0, vol=0.08).clip(lower=1e6).rename("equity")
    assets = _fund(104, base=9e8, drift=0.0, vol=0.07).clip(lower=2e6).rename("assets")
    tangibles = _fund(105, base=6e8, drift=0.0, vol=0.075).clip(lower=1e6).rename("tangibles")
    tangibles = pd.Series(np.minimum(tangibles.values, assets.values * 0.97), name="tangibles")
    intangibles = _fund(106, base=1.2e8, drift=0.0, vol=0.085).clip(lower=1e5).rename("intangibles")
    intangibles = pd.Series(np.minimum(intangibles.values, equity.values * 0.9), name="intangibles")

    cols = {"pb": pb, "marketcap": marketcap, "equity": equity,
            "tangibles": tangibles, "intangibles": intangibles, "assets": assets}

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

    print("OK f42_asset_backing_nav_base_001_075_claude: %d features pass" % n_features)
