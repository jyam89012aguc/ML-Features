import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives (valuation breadth: book / tangible-book / EV-EBIT) =====
def _f49_pb(pb):
    # price-to-book multiple (already a column); guard positivity
    return pb.where(pb > 0, np.nan)


def _f49_evebit(evebit):
    return evebit.where(evebit > 0, np.nan)


def _f49_tbv_floor(tbvps, bvps):
    # tangible-book as fraction of book per share (price-floor quality)
    return tbvps / bvps.replace(0, np.nan)


def _f49_intang_share(intangibles, equity):
    # intangible share of equity (book asset-quality; high => goodwill-funded)
    return intangibles / equity.replace(0, np.nan)


def _f49_tang_share(tangibles, equity):
    return tangibles / equity.replace(0, np.nan)


def _f49_ptb(pb, tbvps, bvps):
    # price-to-tangible-book = P/B * (book / tangible-book) per share
    return pb * (bvps / tbvps.replace(0, np.nan))


def _f49_ebit_yield(ebit, ev):
    # EBIT yield = ebit / ev (inverse of EV/EBIT, allows negative ebit)
    return ebit / ev.replace(0, np.nan)


def _f49_bvps_growth(bvps, w):
    return bvps / bvps.shift(w).replace(0, np.nan) - 1.0


def _f49_log_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f49_cushion(tbvps, bvps):
    # tangible-book cushion: (book - tangiblebook)/book = intangible per-share share
    return (bvps - tbvps) / bvps.replace(0, np.nan)


# intangible share rank
def f49vb_f49_valuation_breadth_book_intangsharerank_504d_base_v076_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share 126d trend (goodwill build-up)
def f49vb_f49_valuation_breadth_book_intangsharetrend_126d_base_v077_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = s - s.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share of equity (hard-asset backing)
def f49vb_f49_valuation_breadth_book_tangshare_252d_base_v078_signal(tangibles, equity):
    b = _f49_tang_share(tangibles, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share of equity z
def f49vb_f49_valuation_breadth_book_tangsharez_252d_base_v079_signal(tangibles, equity):
    s = _f49_tang_share(tangibles, equity)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-to-intangible asset ratio
def f49vb_f49_valuation_breadth_book_tangtointang_252d_base_v080_signal(tangibles, intangibles):
    b = tangibles / intangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-asset YoY log growth (content/IP capitalization)
def f49vb_f49_valuation_breadth_book_intanggrowth_252d_base_v081_signal(intangibles):
    b = _f49_log_growth(intangibles, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book equity YoY log growth
def f49vb_f49_valuation_breadth_book_equitygrowth_252d_base_v082_signal(equity):
    b = _f49_log_growth(equity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book equity growth z
def f49vb_f49_valuation_breadth_book_equitygrowthz_252d_base_v083_signal(equity):
    g = _f49_log_growth(equity, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# negative-book-equity frequency (buyback/deficit regime)
def f49vb_f49_valuation_breadth_book_negequityflag_252d_base_v084_signal(equity):
    neg = (equity < 0).astype(float)
    b = neg.rolling(252, min_periods=126).mean()
    b = b + 0.001 * _z(equity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/marketcap (net-debt weight in enterprise value)
def f49vb_f49_valuation_breadth_book_evmcapratio_252d_base_v085_signal(ev, marketcap):
    b = ev / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/marketcap z
def f49vb_f49_valuation_breadth_book_evmcapratioz_252d_base_v086_signal(ev, marketcap):
    r = ev / marketcap.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/marketcap 126d trend (leverage creep into EV)
def f49vb_f49_valuation_breadth_book_evmcaptrend_126d_base_v087_signal(ev, marketcap):
    r = ev / marketcap.replace(0, np.nan)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/book equity (aggregate price-to-book)
def f49vb_f49_valuation_breadth_book_mcapbookratio_252d_base_v088_signal(marketcap, equity):
    b = marketcap / equity.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/book cheapness z
def f49vb_f49_valuation_breadth_book_mcapbookz_252d_base_v089_signal(marketcap, equity):
    r = marketcap / equity.replace(0, np.nan)
    b = -_z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/tangible assets (price vs hard assets)
def f49vb_f49_valuation_breadth_book_mcaptangratio_252d_base_v090_signal(marketcap, tangibles):
    b = marketcap / tangibles.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book+EV/EBIT cheapness composite (valuation breadth)
def f49vb_f49_valuation_breadth_book_bookebit_blend_252d_base_v091_signal(pb, evebit):
    cb = -_z(_f49_pb(pb), 252)
    ce = -_z(_f49_evebit(evebit), 252)
    b = 0.5 * (cb + ce)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book vs EV/EBIT cheapness disagreement
def f49vb_f49_valuation_breadth_book_bookebit_disagree_252d_base_v092_signal(pb, evebit):
    cb = -_z(_f49_pb(pb), 252)
    ce = -_z(_f49_evebit(evebit), 252)
    b = cb - ce
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book + EV/EBIT cheapness composite
def f49vb_f49_valuation_breadth_book_tbvebit_blend_252d_base_v093_signal(pb, tbvps, bvps, evebit):
    pt = _f49_ptb(pb, tbvps, bvps)
    ct = -_z(pt, 126)
    ce = -_z(_f49_evebit(evebit), 504)
    b = 0.7 * ct + 0.3 * ce
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 3-multiple cheapness breadth mean (book + EV/EBIT + EV/EBITDA)
def f49vb_f49_valuation_breadth_book_multibreadth_252d_base_v094_signal(pb, evebit, evebitda):
    a = -_z(_f49_pb(pb), 252)
    c = -_z(_f49_evebit(evebit), 252)
    d = -_z(_f49_evebit(evebitda), 252)
    st = pd.concat([a, c, d], axis=1)
    b = st.mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 3-multiple cheapness dispersion (valuation disagreement)
def f49vb_f49_valuation_breadth_book_multidisp_252d_base_v095_signal(pb, evebit, evebitda):
    a = -_z(_f49_pb(pb), 252)
    c = -_z(_f49_evebit(evebit), 252)
    d = -_z(_f49_evebit(evebitda), 252)
    st = pd.concat([a, c, d], axis=1)
    b = st.std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book cheapness plus tangible-book floor-quality z (additive composite)
def f49vb_f49_valuation_breadth_book_qualcheap_252d_base_v096_signal(pb, tbvps, bvps):
    floorz = _z(_f49_tbv_floor(tbvps, bvps), 252)
    cheap = -_z(_f49_pb(pb), 252)
    b = cheap + floorz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-growth rank minus EV/EBIT rank (growth-vs-multiple spread)
def f49vb_f49_valuation_breadth_book_evebit_to_bvgrowth_252d_base_v097_signal(evebit, bvps):
    e = _f49_evebit(evebit)
    g = _f49_bvps_growth(bvps, 252)
    b = _rank(g, 252) - _rank(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book GARP: low-P/B rank plus high book-growth rank (rank composite)
def f49vb_f49_valuation_breadth_book_pb_to_bvgrowth_252d_base_v098_signal(pb, bvps):
    p = _f49_pb(pb)
    g = _f49_bvps_growth(bvps, 252)
    b = -_rank(p, 252) + _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B cheapness rank 504d
def f49vb_f49_valuation_breadth_book_pbcheaprank_504d_base_v099_signal(pb):
    b = -_rank(_f49_pb(pb), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B year-over-year log change
def f49vb_f49_valuation_breadth_book_pbyoy_252d_base_v100_signal(pb):
    p = _f49_pb(pb)
    b = _f49_log_growth(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B deviation from rolling median (mean-reversion)
def f49vb_f49_valuation_breadth_book_pbmedrev_252d_base_v101_signal(pb):
    p = _f49_pb(pb)
    med = p.rolling(252, min_periods=126).median()
    b = (p - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B short/long volatility ratio (re-rating turbulence)
def f49vb_f49_valuation_breadth_book_pbvolratio_252d_base_v102_signal(pb):
    p = _f49_pb(pb)
    b = _std(p, 63) / _std(p, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 252d distributional skew
def f49vb_f49_valuation_breadth_book_pbskew_252d_base_v103_signal(pb):
    p = _f49_pb(pb)
    b = p.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B rise off its 252d trough (re-rating magnitude)
def f49vb_f49_valuation_breadth_book_pbdrawup_252d_base_v104_signal(pb):
    p = _f49_pb(pb)
    mn = _rmin(p, 252)
    b = p / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT compression below its 504d peak (de-rating cheapness magnitude)
def f49vb_f49_valuation_breadth_book_evebitcheapdd_504d_base_v105_signal(evebit):
    e = _f49_evebit(evebit)
    mx = _rmax(e, 504)
    b = (mx - e) / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT year-over-year log change
def f49vb_f49_valuation_breadth_book_evebityoy_252d_base_v106_signal(evebit):
    e = _f49_evebit(evebit)
    b = _f49_log_growth(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT deviation from rolling median
def f49vb_f49_valuation_breadth_book_evebitmedrev_252d_base_v107_signal(evebit):
    e = _f49_evebit(evebit)
    med = e.rolling(252, min_periods=126).median()
    b = (e - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT short/long vol ratio
def f49vb_f49_valuation_breadth_book_evebitvolratio_252d_base_v108_signal(evebit):
    e = _f49_evebit(evebit)
    b = _std(e, 63) / _std(e, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 252d skew
def f49vb_f49_valuation_breadth_book_evebitskew_252d_base_v109_signal(evebit):
    e = _f49_evebit(evebit)
    b = e.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT compression off its 252d peak (de-rating)
def f49vb_f49_valuation_breadth_book_evebitdrawdn_252d_base_v110_signal(evebit):
    e = _f49_evebit(evebit)
    mx = _rmax(e, 252)
    b = e / mx.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 504d range position minus EV-growth rank (multiple vs enterprise drift)
def f49vb_f49_valuation_breadth_book_evebitcompress_252d_base_v111_signal(evebit, ev):
    e = _f49_evebit(evebit)
    evg = _f49_log_growth(ev, 126)
    rp = (e - _rmin(e, 504)) / (_rmax(e, 504) - _rmin(e, 504)).replace(0, np.nan)
    b = rp - _rank(evg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA YoY log change
def f49vb_f49_valuation_breadth_book_evebitdayoy_252d_base_v112_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = _f49_log_growth(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA deviation from rolling median
def f49vb_f49_valuation_breadth_book_evebitdamedrev_252d_base_v113_signal(evebitda):
    e = _f49_evebit(evebitda)
    med = e.rolling(252, min_periods=126).median()
    b = (e - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA position within 252d range
def f49vb_f49_valuation_breadth_book_evebitdacompress_252d_base_v114_signal(evebitda):
    e = _f49_evebit(evebitda)
    rng = _rmax(e, 252) - _rmin(e, 252)
    b = (e - _rmin(e, 252)) / rng.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT-to-EV/EBITDA ratio percentile (D&A burden percentile)
def f49vb_f49_valuation_breadth_book_evebitdaratio_pctl_504d_base_v115_signal(evebit, evebitda):
    sp = _f49_evebit(evebit) / _f49_evebit(evebitda).replace(0, np.nan)
    b = sp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book floor rank 504d
def f49vb_f49_valuation_breadth_book_tbvfloorrank_504d_base_v116_signal(tbvps, bvps):
    f = _f49_tbv_floor(tbvps, bvps)
    b = _rank(f, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible per-share cushion z combined with marketcap-momentum sign
def f49vb_f49_valuation_breadth_book_tbvcushionz_252d_base_v117_signal(bvps, tbvps, marketcap):
    cush = _f49_cushion(tbvps, bvps)
    mg = _f49_log_growth(marketcap, 63)
    b = _z(cush, 252) + np.sign(mg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-vs-equity growth gap 126d change (asset-quality drift)
def f49vb_f49_valuation_breadth_book_tbvcushiontrend_126d_base_v118_signal(intangibles, equity):
    ig = _f49_log_growth(intangibles, 63)
    eg = _f49_log_growth(equity, 63)
    b = (ig - eg) - (ig - eg).shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book growth rank
def f49vb_f49_valuation_breadth_book_tbvgrowthrank_504d_base_v119_signal(tbvps):
    g = _f49_bvps_growth(tbvps, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book growth acceleration
def f49vb_f49_valuation_breadth_book_tbvaccel_252d_base_v120_signal(tbvps):
    g = _f49_bvps_growth(tbvps, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book-to-price yield (deep value floor yield)
def f49vb_f49_valuation_breadth_book_tbvtomcap_252d_base_v121_signal(tbvps, pb, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = 1.0 / pt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book value rise off 252d trough
def f49vb_f49_valuation_breadth_book_bvpsdrawup_252d_base_v122_signal(bvps):
    mn = _rmin(bvps, 252)
    b = bvps / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book value 504d (2-year) log growth
def f49vb_f49_valuation_breadth_book_bvpsyoy_504d_base_v123_signal(bvps):
    b = _f49_log_growth(bvps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book value EMA-smoothed quarterly growth
def f49vb_f49_valuation_breadth_book_bvpssmoothgrow_252d_base_v124_signal(bvps):
    lg = _f49_log_growth(bvps, 63)
    b = lg.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value growth tanh z
def f49vb_f49_valuation_breadth_book_bvpsgrowthtanh_252d_base_v125_signal(bvps):
    g = _f49_bvps_growth(bvps, 252)
    b = np.tanh(_z(g, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share YoY change
def f49vb_f49_valuation_breadth_book_intangshareyoy_252d_base_v126_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = _f49_log_growth(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible-asset growth z
def f49vb_f49_valuation_breadth_book_intanggrowthz_252d_base_v127_signal(intangibles):
    g = _f49_log_growth(intangibles, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible share rank
def f49vb_f49_valuation_breadth_book_tangsharerank_504d_base_v128_signal(tangibles, equity):
    s = _f49_tang_share(tangibles, equity)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-to-intangible ratio 126d log trend
def f49vb_f49_valuation_breadth_book_tangtointangtrend_126d_base_v129_signal(tangibles, intangibles):
    r = tangibles / intangibles.replace(0, np.nan)
    b = _f49_log_growth(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book equity growth acceleration
def f49vb_f49_valuation_breadth_book_equitygrowthaccel_252d_base_v130_signal(equity):
    g = _f49_log_growth(equity, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible assets relative to marketcap (IP-embedded valuation)
def f49vb_f49_valuation_breadth_book_intangtomcap_252d_base_v131_signal(intangibles, marketcap):
    b = intangibles / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/marketcap rank (leverage embedded in EV)
def f49vb_f49_valuation_breadth_book_evmcaprank_504d_base_v132_signal(ev, marketcap):
    r = ev / marketcap.replace(0, np.nan)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/book cheapness rank
def f49vb_f49_valuation_breadth_book_mcapbookrank_504d_base_v133_signal(marketcap, equity):
    r = marketcap / equity.replace(0, np.nan)
    b = -_rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/book 126d trend
def f49vb_f49_valuation_breadth_book_mcapbooktrend_126d_base_v134_signal(marketcap, equity):
    r = marketcap / equity.replace(0, np.nan)
    b = _f49_log_growth(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/tangible cheapness z
def f49vb_f49_valuation_breadth_book_mcaptangz_252d_base_v135_signal(marketcap, tangibles):
    r = marketcap / tangibles.replace(0, np.nan)
    b = -_z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/tangible assets z (enterprise value vs hard assets, de-trended)
def f49vb_f49_valuation_breadth_book_evtotang_252d_base_v136_signal(ev, tangibles):
    r = ev / tangibles.replace(0, np.nan)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/book equity (enterprise-to-book)
def f49vb_f49_valuation_breadth_book_evtoequity_252d_base_v137_signal(ev, equity):
    b = ev / equity.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield 21d momentum
def f49vb_f49_valuation_breadth_book_ebityieldmom_21d_base_v138_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = y - y.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield tanh z
def f49vb_f49_valuation_breadth_book_ebityieldtanh_252d_base_v139_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = np.tanh(_z(y, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield sign x sqrt-deviation vs 504d mean
def f49vb_f49_valuation_breadth_book_ebityieldsignmag_504d_base_v140_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    m = _mean(y, 504)
    d = y - m
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield dispersion vs its own level (operating-yield instability)
def f49vb_f49_valuation_breadth_book_ebityielddisp_252d_base_v141_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = _std(y, 63) / _mean(y, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# worst-of book/EV-EBIT cheapness (conservative valuation breadth)
def f49vb_f49_valuation_breadth_book_bookebit_minblend_252d_base_v142_signal(pb, evebit):
    cb = -_z(_f49_pb(pb), 252)
    ce = -_z(_f49_evebit(evebit), 252)
    b = pd.concat([cb, ce], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book + EV/EBIT + EV/EBITDA cheapness breadth mean
def f49vb_f49_valuation_breadth_book_fullbreadth_252d_base_v143_signal(pb, tbvps, bvps, evebit, evebitda):
    pt = _f49_ptb(pb, tbvps, bvps)
    a = -_z(pt, 252)
    c = -_z(_f49_evebit(evebit), 252)
    d = -_z(_f49_evebit(evebitda), 252)
    st = pd.concat([a, c, d], axis=1)
    b = st.mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT cheapness plus tangible-book floor-quality z (additive)
def f49vb_f49_valuation_breadth_book_qualcheap_ebit_252d_base_v144_signal(evebit, tbvps, bvps):
    floorz = _z(_f49_tbv_floor(tbvps, bvps), 252)
    cheap = -_z(_f49_evebit(evebit), 252)
    b = cheap + 0.7 * floorz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT scaled up by intangible reliance (quality-penalized multiple)
def f49vb_f49_valuation_breadth_book_evebit_to_intang_252d_base_v145_signal(evebit, intangibles, equity):
    e = _f49_evebit(evebit)
    s = _f49_intang_share(intangibles, equity)
    b = e * (1.0 + s)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book cheapness + low-intangible quality blend
def f49vb_f49_valuation_breadth_book_cheapquality_blend_252d_base_v146_signal(pb, intangibles, equity):
    cheap = -_z(_f49_pb(pb), 252)
    tq = -_z(_f49_intang_share(intangibles, equity), 252)
    b = 0.5 * (cheap + tq)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute book vs EV/EBIT cheapness-rank gap
def f49vb_f49_valuation_breadth_book_bookebit_corrgap_252d_base_v147_signal(pb, evebit):
    cb = -_rank(_f49_pb(pb), 252)
    ce = -_rank(_f49_evebit(evebit), 252)
    b = (cb - ce).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted EV/EBIT rank (book-growth per multiple)
def f49vb_f49_valuation_breadth_book_evebit_growthadj_rank_504d_base_v148_signal(evebit, tbvps):
    e = _f49_evebit(evebit)
    g = _f49_bvps_growth(tbvps, 252)
    b = _rank(g, 504) - _rank(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book growth per unit P/tangible-book
def f49vb_f49_valuation_breadth_book_ptb_growthadj_252d_base_v149_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    g = _f49_bvps_growth(tbvps, 252)
    b = g / pt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/marketcap operating earnings yield (equity-side, neg allowed)
def f49vb_f49_valuation_breadth_book_evebityield_mcap_252d_base_v150_signal(ebit, marketcap):
    b = ebit / marketcap.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f49vb_f49_valuation_breadth_book_intangsharerank_504d_base_v076_signal,
    f49vb_f49_valuation_breadth_book_intangsharetrend_126d_base_v077_signal,
    f49vb_f49_valuation_breadth_book_tangshare_252d_base_v078_signal,
    f49vb_f49_valuation_breadth_book_tangsharez_252d_base_v079_signal,
    f49vb_f49_valuation_breadth_book_tangtointang_252d_base_v080_signal,
    f49vb_f49_valuation_breadth_book_intanggrowth_252d_base_v081_signal,
    f49vb_f49_valuation_breadth_book_equitygrowth_252d_base_v082_signal,
    f49vb_f49_valuation_breadth_book_equitygrowthz_252d_base_v083_signal,
    f49vb_f49_valuation_breadth_book_negequityflag_252d_base_v084_signal,
    f49vb_f49_valuation_breadth_book_evmcapratio_252d_base_v085_signal,
    f49vb_f49_valuation_breadth_book_evmcapratioz_252d_base_v086_signal,
    f49vb_f49_valuation_breadth_book_evmcaptrend_126d_base_v087_signal,
    f49vb_f49_valuation_breadth_book_mcapbookratio_252d_base_v088_signal,
    f49vb_f49_valuation_breadth_book_mcapbookz_252d_base_v089_signal,
    f49vb_f49_valuation_breadth_book_mcaptangratio_252d_base_v090_signal,
    f49vb_f49_valuation_breadth_book_bookebit_blend_252d_base_v091_signal,
    f49vb_f49_valuation_breadth_book_bookebit_disagree_252d_base_v092_signal,
    f49vb_f49_valuation_breadth_book_tbvebit_blend_252d_base_v093_signal,
    f49vb_f49_valuation_breadth_book_multibreadth_252d_base_v094_signal,
    f49vb_f49_valuation_breadth_book_multidisp_252d_base_v095_signal,
    f49vb_f49_valuation_breadth_book_qualcheap_252d_base_v096_signal,
    f49vb_f49_valuation_breadth_book_evebit_to_bvgrowth_252d_base_v097_signal,
    f49vb_f49_valuation_breadth_book_pb_to_bvgrowth_252d_base_v098_signal,
    f49vb_f49_valuation_breadth_book_pbcheaprank_504d_base_v099_signal,
    f49vb_f49_valuation_breadth_book_pbyoy_252d_base_v100_signal,
    f49vb_f49_valuation_breadth_book_pbmedrev_252d_base_v101_signal,
    f49vb_f49_valuation_breadth_book_pbvolratio_252d_base_v102_signal,
    f49vb_f49_valuation_breadth_book_pbskew_252d_base_v103_signal,
    f49vb_f49_valuation_breadth_book_pbdrawup_252d_base_v104_signal,
    f49vb_f49_valuation_breadth_book_evebitcheapdd_504d_base_v105_signal,
    f49vb_f49_valuation_breadth_book_evebityoy_252d_base_v106_signal,
    f49vb_f49_valuation_breadth_book_evebitmedrev_252d_base_v107_signal,
    f49vb_f49_valuation_breadth_book_evebitvolratio_252d_base_v108_signal,
    f49vb_f49_valuation_breadth_book_evebitskew_252d_base_v109_signal,
    f49vb_f49_valuation_breadth_book_evebitdrawdn_252d_base_v110_signal,
    f49vb_f49_valuation_breadth_book_evebitcompress_252d_base_v111_signal,
    f49vb_f49_valuation_breadth_book_evebitdayoy_252d_base_v112_signal,
    f49vb_f49_valuation_breadth_book_evebitdamedrev_252d_base_v113_signal,
    f49vb_f49_valuation_breadth_book_evebitdacompress_252d_base_v114_signal,
    f49vb_f49_valuation_breadth_book_evebitdaratio_pctl_504d_base_v115_signal,
    f49vb_f49_valuation_breadth_book_tbvfloorrank_504d_base_v116_signal,
    f49vb_f49_valuation_breadth_book_tbvcushionz_252d_base_v117_signal,
    f49vb_f49_valuation_breadth_book_tbvcushiontrend_126d_base_v118_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowthrank_504d_base_v119_signal,
    f49vb_f49_valuation_breadth_book_tbvaccel_252d_base_v120_signal,
    f49vb_f49_valuation_breadth_book_tbvtomcap_252d_base_v121_signal,
    f49vb_f49_valuation_breadth_book_bvpsdrawup_252d_base_v122_signal,
    f49vb_f49_valuation_breadth_book_bvpsyoy_504d_base_v123_signal,
    f49vb_f49_valuation_breadth_book_bvpssmoothgrow_252d_base_v124_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowthtanh_252d_base_v125_signal,
    f49vb_f49_valuation_breadth_book_intangshareyoy_252d_base_v126_signal,
    f49vb_f49_valuation_breadth_book_intanggrowthz_252d_base_v127_signal,
    f49vb_f49_valuation_breadth_book_tangsharerank_504d_base_v128_signal,
    f49vb_f49_valuation_breadth_book_tangtointangtrend_126d_base_v129_signal,
    f49vb_f49_valuation_breadth_book_equitygrowthaccel_252d_base_v130_signal,
    f49vb_f49_valuation_breadth_book_intangtomcap_252d_base_v131_signal,
    f49vb_f49_valuation_breadth_book_evmcaprank_504d_base_v132_signal,
    f49vb_f49_valuation_breadth_book_mcapbookrank_504d_base_v133_signal,
    f49vb_f49_valuation_breadth_book_mcapbooktrend_126d_base_v134_signal,
    f49vb_f49_valuation_breadth_book_mcaptangz_252d_base_v135_signal,
    f49vb_f49_valuation_breadth_book_evtotang_252d_base_v136_signal,
    f49vb_f49_valuation_breadth_book_evtoequity_252d_base_v137_signal,
    f49vb_f49_valuation_breadth_book_ebityieldmom_21d_base_v138_signal,
    f49vb_f49_valuation_breadth_book_ebityieldtanh_252d_base_v139_signal,
    f49vb_f49_valuation_breadth_book_ebityieldsignmag_504d_base_v140_signal,
    f49vb_f49_valuation_breadth_book_ebityielddisp_252d_base_v141_signal,
    f49vb_f49_valuation_breadth_book_bookebit_minblend_252d_base_v142_signal,
    f49vb_f49_valuation_breadth_book_fullbreadth_252d_base_v143_signal,
    f49vb_f49_valuation_breadth_book_qualcheap_ebit_252d_base_v144_signal,
    f49vb_f49_valuation_breadth_book_evebit_to_intang_252d_base_v145_signal,
    f49vb_f49_valuation_breadth_book_cheapquality_blend_252d_base_v146_signal,
    f49vb_f49_valuation_breadth_book_bookebit_corrgap_252d_base_v147_signal,
    f49vb_f49_valuation_breadth_book_evebit_growthadj_rank_504d_base_v148_signal,
    f49vb_f49_valuation_breadth_book_ptb_growthadj_252d_base_v149_signal,
    f49vb_f49_valuation_breadth_book_evebityield_mcap_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_VALUATION_BREADTH_BOOK_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)
    bvps = _fund(202, base=12.0, drift=0.02, vol=0.05).rename("bvps")
    ebit = _fund(207, base=1.2e8, drift=0.025, vol=0.10, allow_neg=True).rename("ebit")
    equity = _fund(209, base=9.0e8, drift=0.025, vol=0.06).rename("equity")
    ev = _fund(206, base=2.2e9, drift=0.03, vol=0.07).rename("ev")
    evebit = _fund(204, base=16.0, drift=0.005, vol=0.06).rename("evebit")
    evebitda = _fund(205, base=11.0, drift=0.005, vol=0.05).rename("evebitda")
    intangibles = _fund(211, base=4.0e8, drift=0.03, vol=0.08).rename("intangibles")
    marketcap = _fund(208, base=1.8e9, drift=0.03, vol=0.07).rename("marketcap")
    pb = _fund(201, base=2.5, drift=0.005, vol=0.06).rename("pb")
    tangibles = _fund(210, base=6.0e8, drift=0.02, vol=0.06).rename("tangibles")
    tbvps = _fund(203, base=7.0, drift=0.02, vol=0.07, allow_neg=True).rename("tbvps")

    cols = {
        "bvps": bvps,
        "ebit": ebit,
        "equity": equity,
        "ev": ev,
        "evebit": evebit,
        "evebitda": evebitda,
        "intangibles": intangibles,
        "marketcap": marketcap,
        "pb": pb,
        "tangibles": tangibles,
        "tbvps": tbvps,
    }

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

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

    print("OK f49_valuation_breadth_book_base_076_150_claude.py: %d features pass" % n_features)
