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


# P/B level (book valuation breadth)
def f49vb_f49_valuation_breadth_book_pblvl_252d_base_v001_signal(pb):
    b = _f49_pb(pb)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B cheapness z vs own 252d (high=>cheap book)
def f49vb_f49_valuation_breadth_book_pbcheapz_252d_base_v002_signal(pb):
    b = -_z(_f49_pb(pb), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B cheapness z vs own 504d
def f49vb_f49_valuation_breadth_book_pbcheapz_504d_base_v003_signal(pb):
    b = -_z(_f49_pb(pb), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B cheapness percentile rank vs 252d
def f49vb_f49_valuation_breadth_book_pbcheaprank_252d_base_v004_signal(pb):
    b = -_rank(_f49_pb(pb), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 63d log trend (re-rating)
def f49vb_f49_valuation_breadth_book_pbtrend_63d_base_v005_signal(pb):
    p = _f49_pb(pb)
    b = _f49_log_growth(p, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 126d log trend
def f49vb_f49_valuation_breadth_book_pbtrend_126d_base_v006_signal(pb):
    p = _f49_pb(pb)
    b = _f49_log_growth(p, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 63d dispersion (book multiple instability)
def f49vb_f49_valuation_breadth_book_pbdisp_63d_base_v007_signal(pb):
    p = _f49_pb(pb)
    b = _std(p, 63) / _mean(p, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 504d percentile gated by book-growth direction
def f49vb_f49_valuation_breadth_book_pbpctl_504d_base_v008_signal(pb, bvps):
    p = _f49_pb(pb)
    pr = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    bg = _f49_bvps_growth(bvps, 63)
    b = pr * (1.0 + np.sign(bg))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 21d change (book re-rating momentum)
def f49vb_f49_valuation_breadth_book_pbmom_21d_base_v009_signal(pb):
    p = _f49_pb(pb)
    b = p - p.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B fast-vs-slow EMA crossover (normalized)
def f49vb_f49_valuation_breadth_book_pbema_disp_252d_base_v010_signal(pb):
    p = _f49_pb(pb)
    fast = p.ewm(span=21, min_periods=10).mean()
    slow = p.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B sign x sqrt deviation
def f49vb_f49_valuation_breadth_book_pbsignmag_252d_base_v011_signal(pb):
    p = _f49_pb(pb)
    m = _mean(p, 252)
    d = p - m
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B tanh-z minus book-growth tanh-z (richness net of growth)
def f49vb_f49_valuation_breadth_book_pbtanh_252d_base_v012_signal(pb, bvps):
    p = _f49_pb(pb)
    z = _z(p, 252)
    bg = _z(_f49_bvps_growth(bvps, 252), 252)
    b = np.tanh(z) - np.tanh(bg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B richness minus book-growth (price ahead of book)
def f49vb_f49_valuation_breadth_book_pbgapbook_252d_base_v013_signal(pb, bvps):
    p = _f49_pb(pb)
    bg = _f49_bvps_growth(bvps, 252)
    b = _z(p, 252) - _z(bg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-to-price yield z combined with equity-growth sign
def f49vb_f49_valuation_breadth_book_pbinvyieldz_252d_base_v014_signal(pb, equity):
    p = _f49_pb(pb)
    by = 1.0 / p
    eg = _f49_log_growth(equity, 126)
    b = _z(by, 252) + np.sign(eg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book level (price floor)
def f49vb_f49_valuation_breadth_book_ptblvl_252d_base_v015_signal(pb, tbvps, bvps):
    b = _f49_ptb(pb, tbvps, bvps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book cheapness z (deep value floor)
def f49vb_f49_valuation_breadth_book_ptbcheapz_252d_base_v016_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = -_z(pt, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book cheapness rank plus low-intangible quality rank
def f49vb_f49_valuation_breadth_book_ptbcheaprank_252d_base_v017_signal(pb, tbvps, bvps, intangibles, equity):
    pt = _f49_ptb(pb, tbvps, bvps)
    rk = -_rank(pt, 252)
    iq = -_rank(_f49_intang_share(intangibles, equity), 252)
    b = rk + iq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book 504d percentile
def f49vb_f49_valuation_breadth_book_ptbpctl_504d_base_v018_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = pt.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book 63d re-rating
def f49vb_f49_valuation_breadth_book_ptbtrend_63d_base_v019_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = _f49_log_growth(pt, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book 21d momentum
def f49vb_f49_valuation_breadth_book_ptbmom_21d_base_v020_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = pt - pt.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/book richness z combined with intangible-cushion z (intangible price premium composite)
def f49vb_f49_valuation_breadth_book_ptbspread_252d_base_v021_signal(pb, tbvps, bvps):
    pp = _f49_pb(pb)
    cush = _f49_cushion(tbvps, bvps)
    b = _z(pp, 126) + 2.0 * _z(cush, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book EMA displacement
def f49vb_f49_valuation_breadth_book_ptbema_disp_252d_base_v022_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = pt - pt.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/tangible-book level tanh-z vs 504d (bounded rich/cheap floor)
def f49vb_f49_valuation_breadth_book_ptbtanh_252d_base_v023_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = np.tanh(_z(pt, 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book fraction of book (floor quality)
def f49vb_f49_valuation_breadth_book_tbvfloor_252d_base_v024_signal(tbvps, bvps):
    b = _f49_tbv_floor(tbvps, bvps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book floor z
def f49vb_f49_valuation_breadth_book_tbvfloorz_252d_base_v025_signal(tbvps, bvps):
    f = _f49_tbv_floor(tbvps, bvps)
    b = _z(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible cushion displacement vs its slow EMA (cushion drift)
def f49vb_f49_valuation_breadth_book_tbvcushion_252d_base_v026_signal(tbvps, bvps):
    c = _f49_cushion(tbvps, bvps)
    b = c - c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible cushion rank
def f49vb_f49_valuation_breadth_book_tbvcushionrank_252d_base_v027_signal(tbvps, bvps):
    c = _f49_cushion(tbvps, bvps)
    b = _rank(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book floor 126d trend (asset quality drift)
def f49vb_f49_valuation_breadth_book_tbvfloortrend_126d_base_v028_signal(tbvps, bvps):
    f = _f49_tbv_floor(tbvps, bvps)
    b = f - f.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book per share YoY growth
def f49vb_f49_valuation_breadth_book_tbvgrowth_252d_base_v029_signal(tbvps):
    b = _f49_bvps_growth(tbvps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book per share 63d growth
def f49vb_f49_valuation_breadth_book_tbvgrowth_63d_base_v030_signal(tbvps):
    b = _f49_bvps_growth(tbvps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book per share 126d log growth
def f49vb_f49_valuation_breadth_book_tbvloggrowth_126d_base_v031_signal(tbvps):
    b = _f49_log_growth(tbvps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-book growth z
def f49vb_f49_valuation_breadth_book_tbvgrowthz_252d_base_v032_signal(tbvps):
    g = _f49_bvps_growth(tbvps, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# negative tangible-book frequency (intangible-funded balance sheet)
def f49vb_f49_valuation_breadth_book_negtbvflag_252d_base_v033_signal(tbvps):
    neg = (tbvps < 0).astype(float)
    b = neg.rolling(252, min_periods=126).mean()
    b = b + 0.001 * _z(tbvps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-minus-tangible per-share gap z (intangible build-up momentum)
def f49vb_f49_valuation_breadth_book_tbvbookgap_z_252d_base_v034_signal(tbvps, bvps):
    gap = (bvps - tbvps)
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share YoY growth
def f49vb_f49_valuation_breadth_book_bvpsgrowth_252d_base_v035_signal(bvps):
    b = _f49_bvps_growth(bvps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share 63d growth
def f49vb_f49_valuation_breadth_book_bvpsgrowth_63d_base_v036_signal(bvps):
    b = _f49_bvps_growth(bvps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book value per share 126d log growth
def f49vb_f49_valuation_breadth_book_bvpsloggrowth_126d_base_v037_signal(bvps):
    b = _f49_log_growth(bvps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value growth z
def f49vb_f49_valuation_breadth_book_bvpsgrowthz_252d_base_v038_signal(bvps):
    g = _f49_bvps_growth(bvps, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value growth rank
def f49vb_f49_valuation_breadth_book_bvpsgrowthrank_504d_base_v039_signal(bvps):
    g = _f49_bvps_growth(bvps, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value growth acceleration
def f49vb_f49_valuation_breadth_book_bvpsaccel_252d_base_v040_signal(bvps):
    g = _f49_bvps_growth(bvps, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value growth trajectory per unit of its own variability (consistency)
def f49vb_f49_valuation_breadth_book_bvpstrendslope_126d_base_v041_signal(bvps):
    lg = _f49_log_growth(bvps, 21)
    b = _mean(lg, 126) / _std(lg, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# book-value growth dispersion (trajectory instability)
def f49vb_f49_valuation_breadth_book_bvpsdispersion_252d_base_v042_signal(bvps):
    g = _f49_bvps_growth(bvps, 63)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT level
def f49vb_f49_valuation_breadth_book_evebitlvl_252d_base_v043_signal(evebit):
    b = _f49_evebit(evebit)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT cheapness z
def f49vb_f49_valuation_breadth_book_evebitcheapz_252d_base_v044_signal(evebit):
    b = -_z(_f49_evebit(evebit), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT cheapness z 504d
def f49vb_f49_valuation_breadth_book_evebitcheapz_504d_base_v045_signal(evebit):
    b = -_z(_f49_evebit(evebit), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT cheapness rank
def f49vb_f49_valuation_breadth_book_evebitcheaprank_252d_base_v046_signal(evebit):
    b = -_rank(_f49_evebit(evebit), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT short-vs-long average ratio (recent re-rating vs multi-year norm)
def f49vb_f49_valuation_breadth_book_evebitshortlong_504d_base_v047_signal(evebit):
    e = _f49_evebit(evebit)
    b = _mean(e, 63) / _mean(e, 504).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 252d range position plus EBIT-level rank (cheap-and-profitable)
def f49vb_f49_valuation_breadth_book_evebitrangepos_252d_base_v048_signal(evebit, ebit):
    e = _f49_evebit(evebit)
    mx = _rmax(e, 252)
    mn = _rmin(e, 252)
    rp = (e - mn) / (mx - mn).replace(0, np.nan)
    b = rp + 0.5 * _rank(ebit, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 63d re-rating trend
def f49vb_f49_valuation_breadth_book_evebittrend_63d_base_v049_signal(evebit):
    e = _f49_evebit(evebit)
    b = _f49_log_growth(e, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 126d re-rating trend
def f49vb_f49_valuation_breadth_book_evebittrend_126d_base_v050_signal(evebit):
    e = _f49_evebit(evebit)
    b = _f49_log_growth(e, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 21d momentum
def f49vb_f49_valuation_breadth_book_evebitmom_21d_base_v051_signal(evebit):
    e = _f49_evebit(evebit)
    b = e - e.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT 63d coefficient of variation
def f49vb_f49_valuation_breadth_book_evebitdisp_63d_base_v052_signal(evebit):
    e = _f49_evebit(evebit)
    b = _std(e, 63) / _mean(e, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT EMA displacement
def f49vb_f49_valuation_breadth_book_evebitema_disp_252d_base_v053_signal(evebit):
    e = _f49_evebit(evebit)
    b = e - e.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT-vs-EV/EBITDA relative richness tanh (bounded cross-multiple gap)
def f49vb_f49_valuation_breadth_book_evebittanh_252d_base_v054_signal(evebit, evebitda):
    ze = _z(_f49_evebit(evebit), 252)
    zd = _z(_f49_evebit(evebitda), 252)
    b = np.tanh(ze - zd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT sign x sqrt deviation
def f49vb_f49_valuation_breadth_book_evebitsignmag_252d_base_v055_signal(evebit):
    e = _f49_evebit(evebit)
    m = _mean(e, 252)
    d = e - m
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-to-EV vs EBITDA-to-EV yield z gap (D&A drag on operating yield)
def f49vb_f49_valuation_breadth_book_evebityield_gap_252d_base_v056_signal(evebit, evebitda):
    y1 = 1.0 / _f49_evebit(evebit)
    y2 = 1.0 / _f49_evebit(evebitda)
    b = _z(y1, 252) - _z(y2, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT-to-EV yield fast-vs-slow EMA crossover (yield momentum regime)
def f49vb_f49_valuation_breadth_book_evebityieldcross_252d_base_v057_signal(evebit):
    e = _f49_evebit(evebit)
    y = 1.0 / e
    fast = y.ewm(span=21, min_periods=10).mean()
    slow = y.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA level
def f49vb_f49_valuation_breadth_book_evebitdalvl_252d_base_v058_signal(evebitda):
    b = _f49_evebit(evebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness z
def f49vb_f49_valuation_breadth_book_evebitdacheapz_252d_base_v059_signal(evebitda):
    b = -_z(_f49_evebit(evebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness rank
def f49vb_f49_valuation_breadth_book_evebitdacheaprank_252d_base_v060_signal(evebitda):
    b = -_rank(_f49_evebit(evebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 504d percentile
def f49vb_f49_valuation_breadth_book_evebitdapctl_504d_base_v061_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = e.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 63d trend
def f49vb_f49_valuation_breadth_book_evebitdatrend_63d_base_v062_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = _f49_log_growth(e, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 21d momentum
def f49vb_f49_valuation_breadth_book_evebitdamom_21d_base_v063_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = e - e.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-to-EV yield z net of EV-growth direction
def f49vb_f49_valuation_breadth_book_evebitdayield_z_252d_base_v064_signal(evebitda, ev):
    e = _f49_evebit(evebitda)
    y = 1.0 / e
    evg = _f49_log_growth(ev, 63)
    b = _z(y, 252) - np.sign(evg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT minus EV/EBITDA (D&A burden in valuation)
def f49vb_f49_valuation_breadth_book_evebitdaspread_252d_base_v065_signal(evebit, evebitda):
    e1 = _f49_evebit(evebit)
    e2 = _f49_evebit(evebitda)
    b = e1 - e2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBIT-EBITDA spread z
def f49vb_f49_valuation_breadth_book_evebitdaspreadz_252d_base_v066_signal(evebit, evebitda):
    e1 = _f49_evebit(evebit)
    e2 = _f49_evebit(evebitda)
    sp = e1 - e2
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA EMA displacement
def f49vb_f49_valuation_breadth_book_evebitdaema_disp_252d_base_v067_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = e - e.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raw EBIT/EV operating yield (neg allowed)
def f49vb_f49_valuation_breadth_book_ebityield_252d_base_v068_signal(ebit, ev):
    b = _f49_ebit_yield(ebit, ev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield z
def f49vb_f49_valuation_breadth_book_ebityieldz_252d_base_v069_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = _z(y, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield rank
def f49vb_f49_valuation_breadth_book_ebityieldrank_504d_base_v070_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = _rank(y, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV yield 126d trend
def f49vb_f49_valuation_breadth_book_ebityieldtrend_126d_base_v071_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = y - y.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-profit positivity frequency (profitability breadth)
def f49vb_f49_valuation_breadth_book_ebitposflag_252d_base_v072_signal(ebit):
    pos = (ebit > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    b = b + 0.001 * _z(ebit, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBIT/EV vs implied 1/(EV/EBIT) consistency gap
def f49vb_f49_valuation_breadth_book_ebitmargin_ev_252d_base_v073_signal(ebit, ev, evebit):
    y = _f49_ebit_yield(ebit, ev)
    ie = 1.0 / _f49_evebit(evebit)
    b = y - ie
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share of equity (book asset-quality)
def f49vb_f49_valuation_breadth_book_intangshare_252d_base_v074_signal(intangibles, equity):
    b = _f49_intang_share(intangibles, equity)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intangible share of equity z
def f49vb_f49_valuation_breadth_book_intangsharez_252d_base_v075_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f49vb_f49_valuation_breadth_book_pblvl_252d_base_v001_signal,
    f49vb_f49_valuation_breadth_book_pbcheapz_252d_base_v002_signal,
    f49vb_f49_valuation_breadth_book_pbcheapz_504d_base_v003_signal,
    f49vb_f49_valuation_breadth_book_pbcheaprank_252d_base_v004_signal,
    f49vb_f49_valuation_breadth_book_pbtrend_63d_base_v005_signal,
    f49vb_f49_valuation_breadth_book_pbtrend_126d_base_v006_signal,
    f49vb_f49_valuation_breadth_book_pbdisp_63d_base_v007_signal,
    f49vb_f49_valuation_breadth_book_pbpctl_504d_base_v008_signal,
    f49vb_f49_valuation_breadth_book_pbmom_21d_base_v009_signal,
    f49vb_f49_valuation_breadth_book_pbema_disp_252d_base_v010_signal,
    f49vb_f49_valuation_breadth_book_pbsignmag_252d_base_v011_signal,
    f49vb_f49_valuation_breadth_book_pbtanh_252d_base_v012_signal,
    f49vb_f49_valuation_breadth_book_pbgapbook_252d_base_v013_signal,
    f49vb_f49_valuation_breadth_book_pbinvyieldz_252d_base_v014_signal,
    f49vb_f49_valuation_breadth_book_ptblvl_252d_base_v015_signal,
    f49vb_f49_valuation_breadth_book_ptbcheapz_252d_base_v016_signal,
    f49vb_f49_valuation_breadth_book_ptbcheaprank_252d_base_v017_signal,
    f49vb_f49_valuation_breadth_book_ptbpctl_504d_base_v018_signal,
    f49vb_f49_valuation_breadth_book_ptbtrend_63d_base_v019_signal,
    f49vb_f49_valuation_breadth_book_ptbmom_21d_base_v020_signal,
    f49vb_f49_valuation_breadth_book_ptbspread_252d_base_v021_signal,
    f49vb_f49_valuation_breadth_book_ptbema_disp_252d_base_v022_signal,
    f49vb_f49_valuation_breadth_book_ptbtanh_252d_base_v023_signal,
    f49vb_f49_valuation_breadth_book_tbvfloor_252d_base_v024_signal,
    f49vb_f49_valuation_breadth_book_tbvfloorz_252d_base_v025_signal,
    f49vb_f49_valuation_breadth_book_tbvcushion_252d_base_v026_signal,
    f49vb_f49_valuation_breadth_book_tbvcushionrank_252d_base_v027_signal,
    f49vb_f49_valuation_breadth_book_tbvfloortrend_126d_base_v028_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowth_252d_base_v029_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowth_63d_base_v030_signal,
    f49vb_f49_valuation_breadth_book_tbvloggrowth_126d_base_v031_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowthz_252d_base_v032_signal,
    f49vb_f49_valuation_breadth_book_negtbvflag_252d_base_v033_signal,
    f49vb_f49_valuation_breadth_book_tbvbookgap_z_252d_base_v034_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowth_252d_base_v035_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowth_63d_base_v036_signal,
    f49vb_f49_valuation_breadth_book_bvpsloggrowth_126d_base_v037_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowthz_252d_base_v038_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowthrank_504d_base_v039_signal,
    f49vb_f49_valuation_breadth_book_bvpsaccel_252d_base_v040_signal,
    f49vb_f49_valuation_breadth_book_bvpstrendslope_126d_base_v041_signal,
    f49vb_f49_valuation_breadth_book_bvpsdispersion_252d_base_v042_signal,
    f49vb_f49_valuation_breadth_book_evebitlvl_252d_base_v043_signal,
    f49vb_f49_valuation_breadth_book_evebitcheapz_252d_base_v044_signal,
    f49vb_f49_valuation_breadth_book_evebitcheapz_504d_base_v045_signal,
    f49vb_f49_valuation_breadth_book_evebitcheaprank_252d_base_v046_signal,
    f49vb_f49_valuation_breadth_book_evebitshortlong_504d_base_v047_signal,
    f49vb_f49_valuation_breadth_book_evebitrangepos_252d_base_v048_signal,
    f49vb_f49_valuation_breadth_book_evebittrend_63d_base_v049_signal,
    f49vb_f49_valuation_breadth_book_evebittrend_126d_base_v050_signal,
    f49vb_f49_valuation_breadth_book_evebitmom_21d_base_v051_signal,
    f49vb_f49_valuation_breadth_book_evebitdisp_63d_base_v052_signal,
    f49vb_f49_valuation_breadth_book_evebitema_disp_252d_base_v053_signal,
    f49vb_f49_valuation_breadth_book_evebittanh_252d_base_v054_signal,
    f49vb_f49_valuation_breadth_book_evebitsignmag_252d_base_v055_signal,
    f49vb_f49_valuation_breadth_book_evebityield_gap_252d_base_v056_signal,
    f49vb_f49_valuation_breadth_book_evebityieldcross_252d_base_v057_signal,
    f49vb_f49_valuation_breadth_book_evebitdalvl_252d_base_v058_signal,
    f49vb_f49_valuation_breadth_book_evebitdacheapz_252d_base_v059_signal,
    f49vb_f49_valuation_breadth_book_evebitdacheaprank_252d_base_v060_signal,
    f49vb_f49_valuation_breadth_book_evebitdapctl_504d_base_v061_signal,
    f49vb_f49_valuation_breadth_book_evebitdatrend_63d_base_v062_signal,
    f49vb_f49_valuation_breadth_book_evebitdamom_21d_base_v063_signal,
    f49vb_f49_valuation_breadth_book_evebitdayield_z_252d_base_v064_signal,
    f49vb_f49_valuation_breadth_book_evebitdaspread_252d_base_v065_signal,
    f49vb_f49_valuation_breadth_book_evebitdaspreadz_252d_base_v066_signal,
    f49vb_f49_valuation_breadth_book_evebitdaema_disp_252d_base_v067_signal,
    f49vb_f49_valuation_breadth_book_ebityield_252d_base_v068_signal,
    f49vb_f49_valuation_breadth_book_ebityieldz_252d_base_v069_signal,
    f49vb_f49_valuation_breadth_book_ebityieldrank_504d_base_v070_signal,
    f49vb_f49_valuation_breadth_book_ebityieldtrend_126d_base_v071_signal,
    f49vb_f49_valuation_breadth_book_ebitposflag_252d_base_v072_signal,
    f49vb_f49_valuation_breadth_book_ebitmargin_ev_252d_base_v073_signal,
    f49vb_f49_valuation_breadth_book_intangshare_252d_base_v074_signal,
    f49vb_f49_valuation_breadth_book_intangsharez_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_VALUATION_BREADTH_BOOK_REGISTRY_001_075 = REGISTRY

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
    pb = _fund(201, base=2.5, drift=0.005, vol=0.06).rename("pb")
    tbvps = _fund(203, base=7.0, drift=0.02, vol=0.07, allow_neg=True).rename("tbvps")

    cols = {
        "bvps": bvps,
        "ebit": ebit,
        "equity": equity,
        "ev": ev,
        "evebit": evebit,
        "evebitda": evebitda,
        "intangibles": intangibles,
        "pb": pb,
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

    print("OK f49_valuation_breadth_book_base_001_075_claude.py: %d features pass" % n_features)
