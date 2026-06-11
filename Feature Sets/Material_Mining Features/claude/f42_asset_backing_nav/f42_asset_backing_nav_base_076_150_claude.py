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


def _median(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ===== folder domain primitives (asset backing / NAV) =====
def _f42_tangible_book(equity, intangibles):
    return equity - intangibles


def _f42_pb_proxy(marketcap, equity):
    return marketcap / equity.replace(0, np.nan)


def _f42_ptb(marketcap, equity, intangibles):
    tb = (equity - intangibles).replace(0, np.nan)
    return marketcap / tb


def _f42_discount_to_nav(marketcap, equity, intangibles):
    tb = (equity - intangibles).replace(0, np.nan)
    return (tb - marketcap) / tb


def _f42_book_yield(equity, marketcap):
    return equity / marketcap.replace(0, np.nan)


def _f42_tangible_share(tangibles, assets):
    return tangibles / assets.replace(0, np.nan)


def _f42_price_to_assets(marketcap, assets):
    return marketcap / assets.replace(0, np.nan)


# ============================================================
# price-to-gross-assets level (capacity-backing multiple)
def f42nb_f42_asset_backing_nav_pa_001d_base_v076_signal(marketcap, assets):
    b = _f42_price_to_assets(marketcap, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-gross-assets z-scored vs 252d history (asset-backing cheapness extreme)
def f42nb_f42_asset_backing_nav_paz_252d_base_v077_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = _z(pa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-gross-assets momentum over a quarter (asset-backing re-rating velocity)
def f42nb_f42_asset_backing_nav_parank_504d_base_v078_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = pa - pa.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-assets level (marketcap per dollar of hard assets)
def f42nb_f42_asset_backing_nav_pta_001d_base_v079_signal(marketcap, tangibles):
    b = marketcap / tangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset backing per market dollar, percentile rank vs 1260d history (deep-backing rank)
def f42nb_f42_asset_backing_nav_tangcover_001d_base_v080_signal(tangibles, marketcap):
    tc = tangibles / marketcap.replace(0, np.nan)
    b = _rank(tc, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-asset backing per market dollar, year-over-year change (asset-coverage cyclical shift)
def f42nb_f42_asset_backing_nav_assetcoverz_504d_base_v081_signal(assets, marketcap):
    cov = assets / marketcap.replace(0, np.nan)
    b = cov - cov.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# soft-asset overhang per market dollar, momentum over a half-year (soft-asset repricing rate)
def f42nb_f42_asset_backing_nav_softoverhang_001d_base_v082_signal(assets, tangibles, marketcap):
    soft = (assets - tangibles) / marketcap.replace(0, np.nan)
    b = soft - soft.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net tangible NAV per market dollar, momentum over a half-year (hard-NAV repricing rate)
def f42nb_f42_asset_backing_nav_nettangnav_001d_base_v083_signal(tangibles, intangibles, marketcap):
    nt = (tangibles - intangibles) / marketcap.replace(0, np.nan)
    b = nt - nt.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities share of assets, z-scored vs 504d history (leverage extremity eroding NAV)
def f42nb_f42_asset_backing_nav_liabshare_001d_base_v084_signal(assets, equity):
    ls = (assets - equity) / assets.replace(0, np.nan)
    b = _z(ls, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities-to-equity (book gearing) year-over-year change (deleveraging/releveraging)
def f42nb_f42_asset_backing_nav_liabeq_001d_base_v085_signal(assets, equity):
    le = (assets - equity) / equity.replace(0, np.nan)
    b = le - le.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible NAV after liabilities per market dollar, momentum over a quarter (true hard-NAV repricing)
def f42nb_f42_asset_backing_nav_hardnavmc_001d_base_v086_signal(tangibles, assets, equity, marketcap):
    hard = (tangibles - (assets - equity)) / marketcap.replace(0, np.nan)
    b = hard - hard.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible NAV after liabilities, z-scored vs 252d history
def f42nb_f42_asset_backing_nav_hardnavz_252d_base_v087_signal(tangibles, assets, equity, marketcap):
    hard = (tangibles - (assets - equity)) / marketcap.replace(0, np.nan)
    b = _z(hard, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B vs price-to-assets spread (book-NAV vs gross-asset-NAV disagreement)
def f42nb_f42_asset_backing_nav_pbpaspread_001d_base_v088_signal(pb, marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = pb - pa
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B vs P/B-proxy ratio (reported-vs-derived book multiple agreement)
def f42nb_f42_asset_backing_nav_pbproxyratio_001d_base_v089_signal(pb, marketcap, equity):
    proxy = _f42_pb_proxy(marketcap, equity)
    b = pb / proxy.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log book-to-price momentum over a quarter (cheapness improving/worsening, log)
def f42nb_f42_asset_backing_nav_logbtp_001d_base_v090_signal(pb):
    lbtp = -np.log(pb.replace(0, np.nan).clip(lower=1e-6))
    b = lbtp - lbtp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 1260d dispersion vs 252d dispersion (multiple-instability term structure)
def f42nb_f42_asset_backing_nav_pbvsmed_1260d_base_v091_signal(pb):
    long = _std(pb, 1260)
    short = _std(pb, 252)
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-tangible-book vs its 504d median (tangible-multiple cheapness, log form)
def f42nb_f42_asset_backing_nav_ptbvsmed_504d_base_v092_signal(marketcap, equity, intangibles):
    ptb = _f42_ptb(marketcap, equity, intangibles)
    med = _median(ptb, 504)
    b = np.log(ptb.replace(0, np.nan).clip(lower=1e-6) / med.clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield curvature: second difference over a quarter grid (NAV-yield bend)
def f42nb_f42_asset_backing_nav_byvsmed_504d_base_v093_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    b = by - 2.0 * by.shift(63) + by.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 252d range width relative to price (multiple amplitude through the year)
def f42nb_f42_asset_backing_nav_pblogtrough_1260d_base_v094_signal(pb):
    hi = _rmax(pb, 252)
    lo = _rmin(pb, 252)
    b = (hi - lo) / pb.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets peak distance over 504d (room to de-rate on asset backing)
def f42nb_f42_asset_backing_nav_papeak_504d_base_v095_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    hi = _rmax(pa, 504)
    b = (hi - pa) / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share level (hard-asset composition of the balance sheet)
def f42nb_f42_asset_backing_nav_tangshare_001d_base_v096_signal(tangibles, assets):
    b = _f42_tangible_share(tangibles, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-to-tangibles (soft vs hard asset mix)
def f42nb_f42_asset_backing_nav_softhardmix_001d_base_v097_signal(intangibles, tangibles):
    b = intangibles / tangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share acceleration over a quarter grid (hard-asset-mix bend)
def f42nb_f42_asset_backing_nav_tangsharemom_126d_base_v098_signal(tangibles, assets):
    ts = _f42_tangible_share(tangibles, assets)
    b = ts - 2.0 * ts.shift(63) + ts.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset share z-scored vs 504d history (hard-asset-backing extreme)
def f42nb_f42_asset_backing_nav_tangsharez_504d_base_v099_signal(tangibles, assets):
    ts = _f42_tangible_share(tangibles, assets)
    b = _z(ts, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets level (book cushion underpinning NAV)
def f42nb_f42_asset_backing_nav_eqassets_001d_base_v100_signal(equity, assets):
    b = equity / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets percentile rank vs 1260d history (book-cushion rank)
def f42nb_f42_asset_backing_nav_eqassetsrank_1260d_base_v101_signal(equity, assets):
    ea = equity / assets.replace(0, np.nan)
    b = _rank(ea, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles-to-assets share, year-over-year change (soft-asset build on the balance sheet)
def f42nb_f42_asset_backing_nav_tbassets_001d_base_v102_signal(intangibles, assets):
    ia = intangibles / assets.replace(0, np.nan)
    b = ia - ia.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book-to-assets momentum over a year (hard cushion build/erosion)
def f42nb_f42_asset_backing_nav_tbassetsmom_252d_base_v103_signal(equity, intangibles, assets):
    tb = _f42_tangible_book(equity, intangibles)
    cush = tb / assets.replace(0, np.nan)
    b = cush - cush.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book-to-market log deviation from its 252d mean (hard-NAV mean-reversion gap)
def f42nb_f42_asset_backing_nav_navgapmed_504d_base_v104_signal(marketcap, equity, intangibles):
    tb = _f42_tangible_book(equity, intangibles).clip(lower=1e-6)
    tbm = tb / marketcap.replace(0, np.nan).clip(lower=1e-6)
    ltbm = np.log(tbm.clip(lower=1e-6))
    b = ltbm - _mean(ltbm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NAV-gap rank vs 252d history (where the tangible discount sits in its recent distribution)
def f42nb_f42_asset_backing_nav_navgaprank_252d_base_v105_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B momentum over a half-year (re-rating velocity)
def f42nb_f42_asset_backing_nav_pbmom_126d_base_v106_signal(pb):
    b = pb - pb.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets momentum over a half-year (asset-backing re-rating velocity)
def f42nb_f42_asset_backing_nav_pamom_126d_base_v107_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = pa - pa.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-cover momentum over a year (hard backing per market dollar trend)
def f42nb_f42_asset_backing_nav_tangcovmom_252d_base_v108_signal(tangibles, marketcap):
    tc = tangibles / marketcap.replace(0, np.nan)
    b = tc - tc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield short vs long mean ratio (recent NAV-yield cheapening vs cyclical norm)
def f42nb_f42_asset_backing_nav_byshortlong_001d_base_v109_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    b = _mean(by, 63) / _mean(by, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets short vs long mean ratio (asset-backing trend phase)
def f42nb_f42_asset_backing_nav_pashortlong_001d_base_v110_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = _mean(pa, 63) / _mean(pa, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B fast-vs-slow EMA oscillator (re-rating oscillator)
def f42nb_f42_asset_backing_nav_pbosc_001d_base_v111_signal(pb):
    fast = pb.ewm(span=21, min_periods=10).mean()
    slow = pb.ewm(span=189, min_periods=63).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-cover fast-vs-slow EMA oscillator (hard-backing re-rating oscillator)
def f42nb_f42_asset_backing_nav_ptbosc_001d_base_v112_signal(tangibles, marketcap):
    tc = tangibles / marketcap.replace(0, np.nan)
    fast = tc.ewm(span=21, min_periods=10).mean()
    slow = tc.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B coefficient of variation over 504d (multiple instability across the cycle)
def f42nb_f42_asset_backing_nav_pbcov_504d_base_v113_signal(pb):
    b = _std(pb, 504) / _mean(pb, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets coefficient of variation over 252d (asset-multiple instability)
def f42nb_f42_asset_backing_nav_pacov_252d_base_v114_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = _std(pa, 252) / _mean(pa, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book-to-assets dispersion over a year (cushion stability)
def f42nb_f42_asset_backing_nav_cushstd_252d_base_v115_signal(equity, intangibles, assets):
    tb = _f42_tangible_book(equity, intangibles)
    cush = tb / assets.replace(0, np.nan)
    b = _std(cush, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity (NAV) growth over a year (book accretion vs dilution, log)
def f42nb_f42_asset_backing_nav_eqgrowth_252d_base_v116_signal(equity):
    b = np.log(equity.replace(0, np.nan).clip(lower=1e-6) / equity.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book growth over a half-year (hard-NAV accretion rate, log)
def f42nb_f42_asset_backing_nav_tbgrowth_126d_base_v117_signal(equity, intangibles):
    tb = _f42_tangible_book(equity, intangibles).clip(lower=1e-6)
    b = np.log(tb / tb.shift(126).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# assets growth over a half-year (capacity/reserve backing expansion, log)
def f42nb_f42_asset_backing_nav_assetgrowth_126d_base_v118_signal(assets):
    b = np.log(assets.replace(0, np.nan).clip(lower=1e-6) / assets.shift(126).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles growth over a year (hard-asset base expansion, log)
def f42nb_f42_asset_backing_nav_tanggrowth_252d_base_v119_signal(tangibles):
    b = np.log(tangibles.replace(0, np.nan).clip(lower=1e-6) / tangibles.shift(252).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NAV accretion vs market re-rating: equity growth minus marketcap growth (book outpacing price)
def f42nb_f42_asset_backing_nav_navvsprice_252d_base_v120_signal(equity, marketcap):
    ge = np.log(equity.replace(0, np.nan).clip(lower=1e-6) / equity.shift(252).clip(lower=1e-6))
    gm = np.log(marketcap.replace(0, np.nan).clip(lower=1e-6) / marketcap.shift(252).clip(lower=1e-6))
    b = ge - gm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book growth minus assets growth (hard-NAV outpacing the asset base)
def f42nb_f42_asset_backing_nav_tbvsasset_252d_base_v121_signal(equity, intangibles, assets):
    tb = _f42_tangible_book(equity, intangibles).clip(lower=1e-6)
    gtb = np.log(tb / tb.shift(252).clip(lower=1e-6))
    ga = np.log(assets.replace(0, np.nan).clip(lower=1e-6) / assets.shift(252).clip(lower=1e-6))
    b = gtb - ga
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pb-multiple growth minus equity growth (price re-rating not backed by NAV accretion)
def f42nb_f42_asset_backing_nav_multvsnav_252d_base_v122_signal(pb, equity):
    gp = np.log(pb.replace(0, np.nan).clip(lower=1e-6) / pb.shift(252).clip(lower=1e-6))
    ge = np.log(equity.replace(0, np.nan).clip(lower=1e-6) / equity.shift(252).clip(lower=1e-6))
    b = gp - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B z-scored vs its own 1260d multi-cycle history (deep cyclical cheapness)
def f42nb_f42_asset_backing_nav_pbz_1260d_base_v123_signal(pb):
    b = _z(pb, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-to-price (inverse pb) z-scored vs 504d history (cheapness extreme)
def f42nb_f42_asset_backing_nav_btpz_504d_base_v124_signal(pb):
    btp = (1.0 / pb.replace(0, np.nan)).clip(upper=20)
    b = _z(btp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed tangible-share z (bounded hard-asset-backing extremity)
def f42nb_f42_asset_backing_nav_bytanh_252d_base_v125_signal(tangibles, assets):
    ts = _f42_tangible_share(tangibles, assets)
    b = np.tanh(_z(ts, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed price-to-assets momentum over a quarter (bounded asset-backing impulse)
def f42nb_f42_asset_backing_nav_pasignmag_252d_base_v126_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = np.tanh(3.0 * (pa - pa.shift(63)) / _std(pa, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-asset-backing regime: time-in-regime priced below the 252d median price-to-assets (count + depth)
def f42nb_f42_asset_backing_nav_cheappa_252d_base_v127_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    med = _median(pa, 252)
    below = (pa < med).astype(float)
    frac = below.rolling(252, min_periods=126).mean()
    depth = (med - pa).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rich-multiple regime: time-in-regime priced above the 252d median P/B (count + depth)
def f42nb_f42_asset_backing_nav_richpb_252d_base_v128_signal(pb):
    med = _median(pb, 252)
    above = (pb > med).astype(float)
    frac = above.rolling(252, min_periods=126).mean()
    depth = (pb - med).clip(lower=0).rolling(63, min_periods=21).mean()
    b = frac + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-cover streak: average run-length above the 252d median tangible-cover (regime persistence)
def f42nb_f42_asset_backing_nav_tangcovstreak_001d_base_v129_signal(tangibles, marketcap):
    tc = tangibles / marketcap.replace(0, np.nan)
    med = _median(tc, 252)
    high = (tc > med).astype(float)
    grp = (high != high.shift(1)).cumsum()
    streak = high.groupby(grp).cumsum()
    b = streak.rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# NAV-cushion crossings: how often tangible-book/assets crosses its 252d median over a year (count)
def f42nb_f42_asset_backing_nav_cushcross_252d_base_v130_signal(equity, intangibles, assets):
    tb = _f42_tangible_book(equity, intangibles)
    cush = tb / assets.replace(0, np.nan)
    med = _median(cush, 252)
    side = (cush > med).astype(float)
    cross = (side != side.shift(1)).astype(float)
    raw = cross.rolling(252, min_periods=126).sum()
    b = raw + 5.0 * (cush - med)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B acceleration: second difference over a quarter grid (re-rating bend)
def f42nb_f42_asset_backing_nav_pbaccel_63d_base_v131_signal(pb):
    b = pb - 2.0 * pb.shift(63) + pb.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets acceleration over a monthly grid (asset-backing re-pricing bend)
def f42nb_f42_asset_backing_nav_paaccel_21d_base_v132_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = pa - 2.0 * pa.shift(21) + pa.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-share acceleration over a quarter grid (soft-asset-mix bend)
def f42nb_f42_asset_backing_nav_tbyaccel_63d_base_v133_signal(intangibles, assets):
    isf = intangibles / assets.replace(0, np.nan)
    b = isf - 2.0 * isf.shift(63) + isf.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-NAV per unit of its own dispersion (risk-adjusted NAV-gap, robust)
def f42nb_f42_asset_backing_nav_navgapsharpe_252d_base_v134_signal(marketcap, equity, intangibles):
    d = _f42_discount_to_nav(marketcap, equity, intangibles)
    dd = d - _median(d, 252)
    sd = _std(d, 252)
    b = (dd / sd.replace(0, np.nan)).clip(lower=-10, upper=10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield per unit of P/B dispersion (cheapness scaled by multiple instability)
def f42nb_f42_asset_backing_nav_byperrisk_252d_base_v135_signal(equity, marketcap, pb):
    by = _f42_book_yield(equity, marketcap)
    risk = _std(pb, 252)
    b = (by / risk.replace(0, np.nan)).clip(upper=200)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets per unit of its dispersion (stable book-cushion extreme)
def f42nb_f42_asset_backing_nav_tangstableshare_252d_base_v136_signal(equity, assets):
    ea = equity / assets.replace(0, np.nan)
    dd = ea - _mean(ea, 252)
    sd = _std(ea, 252)
    b = (dd / sd.replace(0, np.nan)).clip(lower=-10, upper=10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep-value gate: book-to-price x tangible-asset share (cheap AND hard-asset-backed)
def f42nb_f42_asset_backing_nav_deepgate_001d_base_v137_signal(pb, tangibles, assets):
    btp = (1.0 / pb.replace(0, np.nan)).clip(upper=20)
    ts = _f42_tangible_share(tangibles, assets)
    b = btp * ts
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency-gated cheapness: book-yield x equity-to-assets (cheap AND solvent)
def f42nb_f42_asset_backing_nav_solvgate_001d_base_v138_signal(equity, marketcap, assets):
    by = _f42_book_yield(equity, marketcap)
    ea = equity / assets.replace(0, np.nan)
    b = (by * ea).clip(upper=20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-cover x hard-cushion interaction, z-scored vs 252d (hard-backing reinforcement extreme)
def f42nb_f42_asset_backing_nav_hardreinf_001d_base_v139_signal(tangibles, marketcap, equity, intangibles, assets):
    tc = tangibles / marketcap.replace(0, np.nan)
    cush = _f42_tangible_book(equity, intangibles) / assets.replace(0, np.nan)
    b = _z((tc * cush).clip(upper=20), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-overhang penalty: price-to-assets x intangibles-share, z-scored vs 252d (overpay extreme)
def f42nb_f42_asset_backing_nav_softpenalty_001d_base_v140_signal(marketcap, assets, intangibles):
    pa = _f42_price_to_assets(marketcap, assets)
    isoft = intangibles / assets.replace(0, np.nan)
    b = _z(pa * isoft, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets range position within 504d (asset-backing cycle phase)
def f42nb_f42_asset_backing_nav_parangepos_504d_base_v141_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    hi = _rmax(pa, 504)
    lo = _rmin(pa, 504)
    b = (pa - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-cover trough distance over a half-year (recent hard-backing cheapness, normalized)
def f42nb_f42_asset_backing_nav_tangcovpos_1260d_base_v142_signal(tangibles, marketcap):
    tc = tangibles / marketcap.replace(0, np.nan)
    lo = _rmin(tc, 126)
    b = (tc - lo) / lo.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-assets range position within 504d (book-cushion cycle phase)
def f42nb_f42_asset_backing_nav_eqassetspos_504d_base_v143_signal(equity, assets):
    ea = equity / assets.replace(0, np.nan)
    hi = _rmax(ea, 504)
    lo = _rmin(ea, 504)
    b = (ea - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-yield range position within 1260d (multi-cycle NAV-yield phase)
def f42nb_f42_asset_backing_nav_byyoy_252d_base_v144_signal(equity, marketcap):
    by = _f42_book_yield(equity, marketcap)
    hi = _rmax(by, 1260)
    lo = _rmin(by, 1260)
    b = (by - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-to-assets displacement from its slow EMA (asset-backing surprise vs trend)
def f42nb_f42_asset_backing_nav_payoy_252d_base_v145_signal(marketcap, assets):
    pa = _f42_price_to_assets(marketcap, assets)
    b = pa - pa.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangibles share of equity, smoothed (persistent book-quality erosion)
def f42nb_f42_asset_backing_nav_intangshareema_001d_base_v146_signal(intangibles, equity):
    ie = intangibles / equity.replace(0, np.nan)
    b = ie.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities-share displacement from its slow EMA (leverage surprise on NAV)
def f42nb_f42_asset_backing_nav_liabdisp_001d_base_v147_signal(assets, equity):
    ls = (assets - equity) / assets.replace(0, np.nan)
    b = ls - ls.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-tangible-NAV per market dollar z-scored vs 504d (deep hard-value extreme)
def f42nb_f42_asset_backing_nav_nettangz_504d_base_v148_signal(tangibles, intangibles, marketcap):
    nt = (tangibles - intangibles) / marketcap.replace(0, np.nan)
    b = _z(nt, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-share to equity-to-assets ratio (hard-asset backing vs book cushion), z-scored
def f42nb_f42_asset_backing_nav_sharecushspread_001d_base_v149_signal(tangibles, assets, equity):
    ts = _f42_tangible_share(tangibles, assets)
    ea = equity / assets.replace(0, np.nan)
    b = _z(ts / ea.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite NAV-backing balance: smoothed up-vs-down daily move balance of tangible-cover over a quarter
def f42nb_f42_asset_backing_nav_navbackbalance_63d_base_v150_signal(tangibles, marketcap):
    tc = (tangibles / marketcap.replace(0, np.nan)).clip(lower=1e-6)
    ltc = np.log(tc)
    chg = ltc.diff()
    up = chg.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-chg.clip(upper=0)).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42nb_f42_asset_backing_nav_pa_001d_base_v076_signal,
    f42nb_f42_asset_backing_nav_paz_252d_base_v077_signal,
    f42nb_f42_asset_backing_nav_parank_504d_base_v078_signal,
    f42nb_f42_asset_backing_nav_pta_001d_base_v079_signal,
    f42nb_f42_asset_backing_nav_tangcover_001d_base_v080_signal,
    f42nb_f42_asset_backing_nav_assetcoverz_504d_base_v081_signal,
    f42nb_f42_asset_backing_nav_softoverhang_001d_base_v082_signal,
    f42nb_f42_asset_backing_nav_nettangnav_001d_base_v083_signal,
    f42nb_f42_asset_backing_nav_liabshare_001d_base_v084_signal,
    f42nb_f42_asset_backing_nav_liabeq_001d_base_v085_signal,
    f42nb_f42_asset_backing_nav_hardnavmc_001d_base_v086_signal,
    f42nb_f42_asset_backing_nav_hardnavz_252d_base_v087_signal,
    f42nb_f42_asset_backing_nav_pbpaspread_001d_base_v088_signal,
    f42nb_f42_asset_backing_nav_pbproxyratio_001d_base_v089_signal,
    f42nb_f42_asset_backing_nav_logbtp_001d_base_v090_signal,
    f42nb_f42_asset_backing_nav_pbvsmed_1260d_base_v091_signal,
    f42nb_f42_asset_backing_nav_ptbvsmed_504d_base_v092_signal,
    f42nb_f42_asset_backing_nav_byvsmed_504d_base_v093_signal,
    f42nb_f42_asset_backing_nav_pblogtrough_1260d_base_v094_signal,
    f42nb_f42_asset_backing_nav_papeak_504d_base_v095_signal,
    f42nb_f42_asset_backing_nav_tangshare_001d_base_v096_signal,
    f42nb_f42_asset_backing_nav_softhardmix_001d_base_v097_signal,
    f42nb_f42_asset_backing_nav_tangsharemom_126d_base_v098_signal,
    f42nb_f42_asset_backing_nav_tangsharez_504d_base_v099_signal,
    f42nb_f42_asset_backing_nav_eqassets_001d_base_v100_signal,
    f42nb_f42_asset_backing_nav_eqassetsrank_1260d_base_v101_signal,
    f42nb_f42_asset_backing_nav_tbassets_001d_base_v102_signal,
    f42nb_f42_asset_backing_nav_tbassetsmom_252d_base_v103_signal,
    f42nb_f42_asset_backing_nav_navgapmed_504d_base_v104_signal,
    f42nb_f42_asset_backing_nav_navgaprank_252d_base_v105_signal,
    f42nb_f42_asset_backing_nav_pbmom_126d_base_v106_signal,
    f42nb_f42_asset_backing_nav_pamom_126d_base_v107_signal,
    f42nb_f42_asset_backing_nav_tangcovmom_252d_base_v108_signal,
    f42nb_f42_asset_backing_nav_byshortlong_001d_base_v109_signal,
    f42nb_f42_asset_backing_nav_pashortlong_001d_base_v110_signal,
    f42nb_f42_asset_backing_nav_pbosc_001d_base_v111_signal,
    f42nb_f42_asset_backing_nav_ptbosc_001d_base_v112_signal,
    f42nb_f42_asset_backing_nav_pbcov_504d_base_v113_signal,
    f42nb_f42_asset_backing_nav_pacov_252d_base_v114_signal,
    f42nb_f42_asset_backing_nav_cushstd_252d_base_v115_signal,
    f42nb_f42_asset_backing_nav_eqgrowth_252d_base_v116_signal,
    f42nb_f42_asset_backing_nav_tbgrowth_126d_base_v117_signal,
    f42nb_f42_asset_backing_nav_assetgrowth_126d_base_v118_signal,
    f42nb_f42_asset_backing_nav_tanggrowth_252d_base_v119_signal,
    f42nb_f42_asset_backing_nav_navvsprice_252d_base_v120_signal,
    f42nb_f42_asset_backing_nav_tbvsasset_252d_base_v121_signal,
    f42nb_f42_asset_backing_nav_multvsnav_252d_base_v122_signal,
    f42nb_f42_asset_backing_nav_pbz_1260d_base_v123_signal,
    f42nb_f42_asset_backing_nav_btpz_504d_base_v124_signal,
    f42nb_f42_asset_backing_nav_bytanh_252d_base_v125_signal,
    f42nb_f42_asset_backing_nav_pasignmag_252d_base_v126_signal,
    f42nb_f42_asset_backing_nav_cheappa_252d_base_v127_signal,
    f42nb_f42_asset_backing_nav_richpb_252d_base_v128_signal,
    f42nb_f42_asset_backing_nav_tangcovstreak_001d_base_v129_signal,
    f42nb_f42_asset_backing_nav_cushcross_252d_base_v130_signal,
    f42nb_f42_asset_backing_nav_pbaccel_63d_base_v131_signal,
    f42nb_f42_asset_backing_nav_paaccel_21d_base_v132_signal,
    f42nb_f42_asset_backing_nav_tbyaccel_63d_base_v133_signal,
    f42nb_f42_asset_backing_nav_navgapsharpe_252d_base_v134_signal,
    f42nb_f42_asset_backing_nav_byperrisk_252d_base_v135_signal,
    f42nb_f42_asset_backing_nav_tangstableshare_252d_base_v136_signal,
    f42nb_f42_asset_backing_nav_deepgate_001d_base_v137_signal,
    f42nb_f42_asset_backing_nav_solvgate_001d_base_v138_signal,
    f42nb_f42_asset_backing_nav_hardreinf_001d_base_v139_signal,
    f42nb_f42_asset_backing_nav_softpenalty_001d_base_v140_signal,
    f42nb_f42_asset_backing_nav_parangepos_504d_base_v141_signal,
    f42nb_f42_asset_backing_nav_tangcovpos_1260d_base_v142_signal,
    f42nb_f42_asset_backing_nav_eqassetspos_504d_base_v143_signal,
    f42nb_f42_asset_backing_nav_byyoy_252d_base_v144_signal,
    f42nb_f42_asset_backing_nav_payoy_252d_base_v145_signal,
    f42nb_f42_asset_backing_nav_intangshareema_001d_base_v146_signal,
    f42nb_f42_asset_backing_nav_liabdisp_001d_base_v147_signal,
    f42nb_f42_asset_backing_nav_nettangz_504d_base_v148_signal,
    f42nb_f42_asset_backing_nav_sharecushspread_001d_base_v149_signal,
    f42nb_f42_asset_backing_nav_navbackbalance_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_ASSET_BACKING_NAV_REGISTRY_076_150 = REGISTRY


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

    print("OK f42_asset_backing_nav_base_076_150_claude: %d features pass" % n_features)
