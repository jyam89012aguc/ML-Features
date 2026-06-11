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


# slope (1st math derivative) of pblvl over 63d
def f49vb_f49_valuation_breadth_book_pblvl_252d_slope_v001_signal(pb):
    b = _f49_pb(pb)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbcheapz over 63d
def f49vb_f49_valuation_breadth_book_pbcheapz_252d_slope_v002_signal(pb):
    b = -_z(_f49_pb(pb), 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbcheapz over 126d
def f49vb_f49_valuation_breadth_book_pbcheapz_504d_slope_v003_signal(pb):
    b = -_z(_f49_pb(pb), 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbcheaprank over 63d
def f49vb_f49_valuation_breadth_book_pbcheaprank_252d_slope_v004_signal(pb):
    b = -_rank(_f49_pb(pb), 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbtrend over 21d
def f49vb_f49_valuation_breadth_book_pbtrend_63d_slope_v005_signal(pb):
    p = _f49_pb(pb)
    b = _f49_log_growth(p, 63)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbtrend over 42d
def f49vb_f49_valuation_breadth_book_pbtrend_126d_slope_v006_signal(pb):
    p = _f49_pb(pb)
    b = _f49_log_growth(p, 126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbdisp over 21d
def f49vb_f49_valuation_breadth_book_pbdisp_63d_slope_v007_signal(pb):
    p = _f49_pb(pb)
    b = _std(p, 63) / _mean(p, 63).replace(0, np.nan)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbpctl over 126d
def f49vb_f49_valuation_breadth_book_pbpctl_504d_slope_v008_signal(pb, bvps):
    p = _f49_pb(pb)
    pr = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    bg = _f49_bvps_growth(bvps, 63)
    b = pr * (1.0 + np.sign(bg))
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbmom over 10d
def f49vb_f49_valuation_breadth_book_pbmom_21d_slope_v009_signal(pb):
    p = _f49_pb(pb)
    b = p - p.shift(21)
    base = b
    d = base.diff(10) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbema_disp over 63d
def f49vb_f49_valuation_breadth_book_pbema_disp_252d_slope_v010_signal(pb):
    p = _f49_pb(pb)
    fast = p.ewm(span=21, min_periods=10).mean()
    slow = p.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbsignmag over 63d
def f49vb_f49_valuation_breadth_book_pbsignmag_252d_slope_v011_signal(pb):
    p = _f49_pb(pb)
    m = _mean(p, 252)
    d = p - m
    b = np.sign(d) * (d.abs() ** 0.5)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbtanh over 63d
def f49vb_f49_valuation_breadth_book_pbtanh_252d_slope_v012_signal(pb, bvps):
    p = _f49_pb(pb)
    z = _z(p, 252)
    bg = _z(_f49_bvps_growth(bvps, 252), 252)
    b = np.tanh(z) - np.tanh(bg)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbgapbook over 63d
def f49vb_f49_valuation_breadth_book_pbgapbook_252d_slope_v013_signal(pb, bvps):
    p = _f49_pb(pb)
    bg = _f49_bvps_growth(bvps, 252)
    b = _z(p, 252) - _z(bg, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbinvyieldz over 63d
def f49vb_f49_valuation_breadth_book_pbinvyieldz_252d_slope_v014_signal(pb, equity):
    p = _f49_pb(pb)
    by = 1.0 / p
    eg = _f49_log_growth(equity, 126)
    b = _z(by, 252) + np.sign(eg)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptblvl over 63d
def f49vb_f49_valuation_breadth_book_ptblvl_252d_slope_v015_signal(pb, tbvps, bvps):
    b = _f49_ptb(pb, tbvps, bvps)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbcheapz over 63d
def f49vb_f49_valuation_breadth_book_ptbcheapz_252d_slope_v016_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = -_z(pt, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbcheaprank over 63d
def f49vb_f49_valuation_breadth_book_ptbcheaprank_252d_slope_v017_signal(pb, tbvps, bvps, intangibles, equity):
    pt = _f49_ptb(pb, tbvps, bvps)
    rk = -_rank(pt, 252)
    iq = -_rank(_f49_intang_share(intangibles, equity), 252)
    b = rk + iq
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbpctl over 126d
def f49vb_f49_valuation_breadth_book_ptbpctl_504d_slope_v018_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = pt.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbtrend over 21d
def f49vb_f49_valuation_breadth_book_ptbtrend_63d_slope_v019_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = _f49_log_growth(pt, 63)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbmom over 10d
def f49vb_f49_valuation_breadth_book_ptbmom_21d_slope_v020_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = pt - pt.shift(21)
    base = b
    d = base.diff(10) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbspread over 63d
def f49vb_f49_valuation_breadth_book_ptbspread_252d_slope_v021_signal(pb, tbvps, bvps):
    pp = _f49_pb(pb)
    cush = _f49_cushion(tbvps, bvps)
    b = _z(pp, 126) + 2.0 * _z(cush, 126)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbema_disp over 63d
def f49vb_f49_valuation_breadth_book_ptbema_disp_252d_slope_v022_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = pt - pt.ewm(span=63, min_periods=21).mean()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptbtanh over 63d
def f49vb_f49_valuation_breadth_book_ptbtanh_252d_slope_v023_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = np.tanh(_z(pt, 504))
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvfloor over 63d
def f49vb_f49_valuation_breadth_book_tbvfloor_252d_slope_v024_signal(tbvps, bvps):
    b = _f49_tbv_floor(tbvps, bvps)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvfloorz over 63d
def f49vb_f49_valuation_breadth_book_tbvfloorz_252d_slope_v025_signal(tbvps, bvps):
    f = _f49_tbv_floor(tbvps, bvps)
    b = _z(f, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvcushion over 63d
def f49vb_f49_valuation_breadth_book_tbvcushion_252d_slope_v026_signal(tbvps, bvps):
    c = _f49_cushion(tbvps, bvps)
    b = c - c.ewm(span=126, min_periods=42).mean()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvcushionrank over 63d
def f49vb_f49_valuation_breadth_book_tbvcushionrank_252d_slope_v027_signal(tbvps, bvps):
    c = _f49_cushion(tbvps, bvps)
    b = _rank(c, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvfloortrend over 42d
def f49vb_f49_valuation_breadth_book_tbvfloortrend_126d_slope_v028_signal(tbvps, bvps):
    f = _f49_tbv_floor(tbvps, bvps)
    b = f - f.shift(126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvgrowth over 63d
def f49vb_f49_valuation_breadth_book_tbvgrowth_252d_slope_v029_signal(tbvps):
    b = _f49_bvps_growth(tbvps, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvgrowth over 21d
def f49vb_f49_valuation_breadth_book_tbvgrowth_63d_slope_v030_signal(tbvps):
    b = _f49_bvps_growth(tbvps, 63)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvloggrowth over 42d
def f49vb_f49_valuation_breadth_book_tbvloggrowth_126d_slope_v031_signal(tbvps):
    b = _f49_log_growth(tbvps, 126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvgrowthz over 63d
def f49vb_f49_valuation_breadth_book_tbvgrowthz_252d_slope_v032_signal(tbvps):
    g = _f49_bvps_growth(tbvps, 252)
    b = _z(g, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of negtbvflag over 63d
def f49vb_f49_valuation_breadth_book_negtbvflag_252d_slope_v033_signal(tbvps):
    neg = (tbvps < 0).astype(float)
    b = neg.rolling(252, min_periods=126).mean()
    b = b + 0.001 * _z(tbvps, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvbookgap_z over 63d
def f49vb_f49_valuation_breadth_book_tbvbookgap_z_252d_slope_v034_signal(tbvps, bvps):
    gap = (bvps - tbvps)
    b = _z(gap, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsgrowth over 63d
def f49vb_f49_valuation_breadth_book_bvpsgrowth_252d_slope_v035_signal(bvps):
    b = _f49_bvps_growth(bvps, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsgrowth over 21d
def f49vb_f49_valuation_breadth_book_bvpsgrowth_63d_slope_v036_signal(bvps):
    b = _f49_bvps_growth(bvps, 63)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsloggrowth over 42d
def f49vb_f49_valuation_breadth_book_bvpsloggrowth_126d_slope_v037_signal(bvps):
    b = _f49_log_growth(bvps, 126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsgrowthz over 63d
def f49vb_f49_valuation_breadth_book_bvpsgrowthz_252d_slope_v038_signal(bvps):
    g = _f49_bvps_growth(bvps, 252)
    b = _z(g, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsgrowthrank over 126d
def f49vb_f49_valuation_breadth_book_bvpsgrowthrank_504d_slope_v039_signal(bvps):
    g = _f49_bvps_growth(bvps, 252)
    b = _rank(g, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsaccel over 63d
def f49vb_f49_valuation_breadth_book_bvpsaccel_252d_slope_v040_signal(bvps):
    g = _f49_bvps_growth(bvps, 63)
    b = g - g.shift(63)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpstrendslope over 42d
def f49vb_f49_valuation_breadth_book_bvpstrendslope_126d_slope_v041_signal(bvps):
    lg = _f49_log_growth(bvps, 21)
    b = _mean(lg, 126) / _std(lg, 126).replace(0, np.nan)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsdispersion over 63d
def f49vb_f49_valuation_breadth_book_bvpsdispersion_252d_slope_v042_signal(bvps):
    g = _f49_bvps_growth(bvps, 63)
    b = _std(g, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitlvl over 63d
def f49vb_f49_valuation_breadth_book_evebitlvl_252d_slope_v043_signal(evebit):
    b = _f49_evebit(evebit)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitcheapz over 63d
def f49vb_f49_valuation_breadth_book_evebitcheapz_252d_slope_v044_signal(evebit):
    b = -_z(_f49_evebit(evebit), 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitcheapz over 126d
def f49vb_f49_valuation_breadth_book_evebitcheapz_504d_slope_v045_signal(evebit):
    b = -_z(_f49_evebit(evebit), 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitcheaprank over 63d
def f49vb_f49_valuation_breadth_book_evebitcheaprank_252d_slope_v046_signal(evebit):
    b = -_rank(_f49_evebit(evebit), 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitshortlong over 126d
def f49vb_f49_valuation_breadth_book_evebitshortlong_504d_slope_v047_signal(evebit):
    e = _f49_evebit(evebit)
    b = _mean(e, 63) / _mean(e, 504).replace(0, np.nan) - 1.0
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitrangepos over 63d
def f49vb_f49_valuation_breadth_book_evebitrangepos_252d_slope_v048_signal(evebit, ebit):
    e = _f49_evebit(evebit)
    mx = _rmax(e, 252)
    mn = _rmin(e, 252)
    rp = (e - mn) / (mx - mn).replace(0, np.nan)
    b = rp + 0.5 * _rank(ebit, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebittrend over 21d
def f49vb_f49_valuation_breadth_book_evebittrend_63d_slope_v049_signal(evebit):
    e = _f49_evebit(evebit)
    b = _f49_log_growth(e, 63)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebittrend over 42d
def f49vb_f49_valuation_breadth_book_evebittrend_126d_slope_v050_signal(evebit):
    e = _f49_evebit(evebit)
    b = _f49_log_growth(e, 126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitmom over 10d
def f49vb_f49_valuation_breadth_book_evebitmom_21d_slope_v051_signal(evebit):
    e = _f49_evebit(evebit)
    b = e - e.shift(21)
    base = b
    d = base.diff(10) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdisp over 21d
def f49vb_f49_valuation_breadth_book_evebitdisp_63d_slope_v052_signal(evebit):
    e = _f49_evebit(evebit)
    b = _std(e, 63) / _mean(e, 63).replace(0, np.nan)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitema_disp over 63d
def f49vb_f49_valuation_breadth_book_evebitema_disp_252d_slope_v053_signal(evebit):
    e = _f49_evebit(evebit)
    b = e - e.ewm(span=63, min_periods=21).mean()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebittanh over 63d
def f49vb_f49_valuation_breadth_book_evebittanh_252d_slope_v054_signal(evebit, evebitda):
    ze = _z(_f49_evebit(evebit), 252)
    zd = _z(_f49_evebit(evebitda), 252)
    b = np.tanh(ze - zd)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitsignmag over 63d
def f49vb_f49_valuation_breadth_book_evebitsignmag_252d_slope_v055_signal(evebit):
    e = _f49_evebit(evebit)
    m = _mean(e, 252)
    d = e - m
    b = np.sign(d) * (d.abs() ** 0.5)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebityield_gap over 63d
def f49vb_f49_valuation_breadth_book_evebityield_gap_252d_slope_v056_signal(evebit, evebitda):
    y1 = 1.0 / _f49_evebit(evebit)
    y2 = 1.0 / _f49_evebit(evebitda)
    b = _z(y1, 252) - _z(y2, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebityieldcross over 63d
def f49vb_f49_valuation_breadth_book_evebityieldcross_252d_slope_v057_signal(evebit):
    e = _f49_evebit(evebit)
    y = 1.0 / e
    fast = y.ewm(span=21, min_periods=10).mean()
    slow = y.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.abs().replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdalvl over 63d
def f49vb_f49_valuation_breadth_book_evebitdalvl_252d_slope_v058_signal(evebitda):
    b = _f49_evebit(evebitda)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdacheapz over 63d
def f49vb_f49_valuation_breadth_book_evebitdacheapz_252d_slope_v059_signal(evebitda):
    b = -_z(_f49_evebit(evebitda), 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdacheaprank over 63d
def f49vb_f49_valuation_breadth_book_evebitdacheaprank_252d_slope_v060_signal(evebitda):
    b = -_rank(_f49_evebit(evebitda), 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdapctl over 126d
def f49vb_f49_valuation_breadth_book_evebitdapctl_504d_slope_v061_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = e.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdatrend over 21d
def f49vb_f49_valuation_breadth_book_evebitdatrend_63d_slope_v062_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = _f49_log_growth(e, 63)
    base = b
    d = base.diff(21) / float(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdamom over 10d
def f49vb_f49_valuation_breadth_book_evebitdamom_21d_slope_v063_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = e - e.shift(21)
    base = b
    d = base.diff(10) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdayield_z over 63d
def f49vb_f49_valuation_breadth_book_evebitdayield_z_252d_slope_v064_signal(evebitda, ev):
    e = _f49_evebit(evebitda)
    y = 1.0 / e
    evg = _f49_log_growth(ev, 63)
    b = _z(y, 252) - np.sign(evg)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdaspread over 63d
def f49vb_f49_valuation_breadth_book_evebitdaspread_252d_slope_v065_signal(evebit, evebitda):
    e1 = _f49_evebit(evebit)
    e2 = _f49_evebit(evebitda)
    b = e1 - e2
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdaspreadz over 63d
def f49vb_f49_valuation_breadth_book_evebitdaspreadz_252d_slope_v066_signal(evebit, evebitda):
    e1 = _f49_evebit(evebit)
    e2 = _f49_evebit(evebitda)
    sp = e1 - e2
    b = _z(sp, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdaema_disp over 63d
def f49vb_f49_valuation_breadth_book_evebitdaema_disp_252d_slope_v067_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = e - e.ewm(span=63, min_periods=21).mean()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityield over 63d
def f49vb_f49_valuation_breadth_book_ebityield_252d_slope_v068_signal(ebit, ev):
    b = _f49_ebit_yield(ebit, ev)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityieldz over 63d
def f49vb_f49_valuation_breadth_book_ebityieldz_252d_slope_v069_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = _z(y, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityieldrank over 126d
def f49vb_f49_valuation_breadth_book_ebityieldrank_504d_slope_v070_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = _rank(y, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityieldtrend over 42d
def f49vb_f49_valuation_breadth_book_ebityieldtrend_126d_slope_v071_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = y - y.shift(126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebitposflag over 63d
def f49vb_f49_valuation_breadth_book_ebitposflag_252d_slope_v072_signal(ebit):
    pos = (ebit > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    b = b + 0.001 * _z(ebit, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebitmargin_ev over 63d
def f49vb_f49_valuation_breadth_book_ebitmargin_ev_252d_slope_v073_signal(ebit, ev, evebit):
    y = _f49_ebit_yield(ebit, ev)
    ie = 1.0 / _f49_evebit(evebit)
    b = y - ie
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intangshare over 63d
def f49vb_f49_valuation_breadth_book_intangshare_252d_slope_v074_signal(intangibles, equity):
    b = _f49_intang_share(intangibles, equity)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intangsharez over 63d
def f49vb_f49_valuation_breadth_book_intangsharez_252d_slope_v075_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = _z(s, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intangsharerank over 126d
def f49vb_f49_valuation_breadth_book_intangsharerank_504d_slope_v076_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = _rank(s, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intangsharetrend over 42d
def f49vb_f49_valuation_breadth_book_intangsharetrend_126d_slope_v077_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = s - s.shift(126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tangshare over 63d
def f49vb_f49_valuation_breadth_book_tangshare_252d_slope_v078_signal(tangibles, equity):
    b = _f49_tang_share(tangibles, equity)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tangsharez over 63d
def f49vb_f49_valuation_breadth_book_tangsharez_252d_slope_v079_signal(tangibles, equity):
    s = _f49_tang_share(tangibles, equity)
    b = _z(s, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tangtointang over 63d
def f49vb_f49_valuation_breadth_book_tangtointang_252d_slope_v080_signal(tangibles, intangibles):
    b = tangibles / intangibles.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intanggrowth over 63d
def f49vb_f49_valuation_breadth_book_intanggrowth_252d_slope_v081_signal(intangibles):
    b = _f49_log_growth(intangibles, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of equitygrowth over 63d
def f49vb_f49_valuation_breadth_book_equitygrowth_252d_slope_v082_signal(equity):
    b = _f49_log_growth(equity, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of equitygrowthz over 63d
def f49vb_f49_valuation_breadth_book_equitygrowthz_252d_slope_v083_signal(equity):
    g = _f49_log_growth(equity, 252)
    b = _z(g, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of negequityflag over 63d
def f49vb_f49_valuation_breadth_book_negequityflag_252d_slope_v084_signal(equity):
    neg = (equity < 0).astype(float)
    b = neg.rolling(252, min_periods=126).mean()
    b = b + 0.001 * _z(equity, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evmcapratio over 63d
def f49vb_f49_valuation_breadth_book_evmcapratio_252d_slope_v085_signal(ev, marketcap):
    b = ev / marketcap.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evmcapratioz over 63d
def f49vb_f49_valuation_breadth_book_evmcapratioz_252d_slope_v086_signal(ev, marketcap):
    r = ev / marketcap.replace(0, np.nan)
    b = _z(r, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evmcaptrend over 42d
def f49vb_f49_valuation_breadth_book_evmcaptrend_126d_slope_v087_signal(ev, marketcap):
    r = ev / marketcap.replace(0, np.nan)
    b = r - r.shift(126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of mcapbookratio over 63d
def f49vb_f49_valuation_breadth_book_mcapbookratio_252d_slope_v088_signal(marketcap, equity):
    b = marketcap / equity.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of mcapbookz over 63d
def f49vb_f49_valuation_breadth_book_mcapbookz_252d_slope_v089_signal(marketcap, equity):
    r = marketcap / equity.replace(0, np.nan)
    b = -_z(r, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of mcaptangratio over 63d
def f49vb_f49_valuation_breadth_book_mcaptangratio_252d_slope_v090_signal(marketcap, tangibles):
    b = marketcap / tangibles.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bookebit_blend over 63d
def f49vb_f49_valuation_breadth_book_bookebit_blend_252d_slope_v091_signal(pb, evebit):
    cb = -_z(_f49_pb(pb), 252)
    ce = -_z(_f49_evebit(evebit), 252)
    b = 0.5 * (cb + ce)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bookebit_disagree over 63d
def f49vb_f49_valuation_breadth_book_bookebit_disagree_252d_slope_v092_signal(pb, evebit):
    cb = -_z(_f49_pb(pb), 252)
    ce = -_z(_f49_evebit(evebit), 252)
    b = cb - ce
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvebit_blend over 63d
def f49vb_f49_valuation_breadth_book_tbvebit_blend_252d_slope_v093_signal(pb, tbvps, bvps, evebit):
    pt = _f49_ptb(pb, tbvps, bvps)
    ct = -_z(pt, 126)
    ce = -_z(_f49_evebit(evebit), 504)
    b = 0.7 * ct + 0.3 * ce
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of multibreadth over 63d
def f49vb_f49_valuation_breadth_book_multibreadth_252d_slope_v094_signal(pb, evebit, evebitda):
    a = -_z(_f49_pb(pb), 252)
    c = -_z(_f49_evebit(evebit), 252)
    d = -_z(_f49_evebit(evebitda), 252)
    st = pd.concat([a, c, d], axis=1)
    b = st.mean(axis=1)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of multidisp over 63d
def f49vb_f49_valuation_breadth_book_multidisp_252d_slope_v095_signal(pb, evebit, evebitda):
    a = -_z(_f49_pb(pb), 252)
    c = -_z(_f49_evebit(evebit), 252)
    d = -_z(_f49_evebit(evebitda), 252)
    st = pd.concat([a, c, d], axis=1)
    b = st.std(axis=1)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of qualcheap over 63d
def f49vb_f49_valuation_breadth_book_qualcheap_252d_slope_v096_signal(pb, tbvps, bvps):
    floorz = _z(_f49_tbv_floor(tbvps, bvps), 252)
    cheap = -_z(_f49_pb(pb), 252)
    b = cheap + floorz
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebit_to_bvgrowth over 63d
def f49vb_f49_valuation_breadth_book_evebit_to_bvgrowth_252d_slope_v097_signal(evebit, bvps):
    e = _f49_evebit(evebit)
    g = _f49_bvps_growth(bvps, 252)
    b = _rank(g, 252) - _rank(e, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pb_to_bvgrowth over 63d
def f49vb_f49_valuation_breadth_book_pb_to_bvgrowth_252d_slope_v098_signal(pb, bvps):
    p = _f49_pb(pb)
    g = _f49_bvps_growth(bvps, 252)
    b = -_rank(p, 252) + _rank(g, 504)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbcheaprank over 126d
def f49vb_f49_valuation_breadth_book_pbcheaprank_504d_slope_v099_signal(pb):
    b = -_rank(_f49_pb(pb), 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbyoy over 63d
def f49vb_f49_valuation_breadth_book_pbyoy_252d_slope_v100_signal(pb):
    p = _f49_pb(pb)
    b = _f49_log_growth(p, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbmedrev over 63d
def f49vb_f49_valuation_breadth_book_pbmedrev_252d_slope_v101_signal(pb):
    p = _f49_pb(pb)
    med = p.rolling(252, min_periods=126).median()
    b = (p - med) / med.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbvolratio over 63d
def f49vb_f49_valuation_breadth_book_pbvolratio_252d_slope_v102_signal(pb):
    p = _f49_pb(pb)
    b = _std(p, 63) / _std(p, 252).replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbskew over 63d
def f49vb_f49_valuation_breadth_book_pbskew_252d_slope_v103_signal(pb):
    p = _f49_pb(pb)
    b = p.rolling(252, min_periods=126).skew()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of pbdrawup over 63d
def f49vb_f49_valuation_breadth_book_pbdrawup_252d_slope_v104_signal(pb):
    p = _f49_pb(pb)
    mn = _rmin(p, 252)
    b = p / mn.replace(0, np.nan) - 1.0
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitcheapdd over 126d
def f49vb_f49_valuation_breadth_book_evebitcheapdd_504d_slope_v105_signal(evebit):
    e = _f49_evebit(evebit)
    mx = _rmax(e, 504)
    b = (mx - e) / mx.replace(0, np.nan)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebityoy over 63d
def f49vb_f49_valuation_breadth_book_evebityoy_252d_slope_v106_signal(evebit):
    e = _f49_evebit(evebit)
    b = _f49_log_growth(e, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitmedrev over 63d
def f49vb_f49_valuation_breadth_book_evebitmedrev_252d_slope_v107_signal(evebit):
    e = _f49_evebit(evebit)
    med = e.rolling(252, min_periods=126).median()
    b = (e - med) / med.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitvolratio over 63d
def f49vb_f49_valuation_breadth_book_evebitvolratio_252d_slope_v108_signal(evebit):
    e = _f49_evebit(evebit)
    b = _std(e, 63) / _std(e, 252).replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitskew over 63d
def f49vb_f49_valuation_breadth_book_evebitskew_252d_slope_v109_signal(evebit):
    e = _f49_evebit(evebit)
    b = e.rolling(252, min_periods=126).skew()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdrawdn over 63d
def f49vb_f49_valuation_breadth_book_evebitdrawdn_252d_slope_v110_signal(evebit):
    e = _f49_evebit(evebit)
    mx = _rmax(e, 252)
    b = e / mx.replace(0, np.nan) - 1.0
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitcompress over 63d
def f49vb_f49_valuation_breadth_book_evebitcompress_252d_slope_v111_signal(evebit, ev):
    e = _f49_evebit(evebit)
    evg = _f49_log_growth(ev, 126)
    rp = (e - _rmin(e, 504)) / (_rmax(e, 504) - _rmin(e, 504)).replace(0, np.nan)
    b = rp - _rank(evg, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdayoy over 63d
def f49vb_f49_valuation_breadth_book_evebitdayoy_252d_slope_v112_signal(evebitda):
    e = _f49_evebit(evebitda)
    b = _f49_log_growth(e, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdamedrev over 63d
def f49vb_f49_valuation_breadth_book_evebitdamedrev_252d_slope_v113_signal(evebitda):
    e = _f49_evebit(evebitda)
    med = e.rolling(252, min_periods=126).median()
    b = (e - med) / med.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdacompress over 63d
def f49vb_f49_valuation_breadth_book_evebitdacompress_252d_slope_v114_signal(evebitda):
    e = _f49_evebit(evebitda)
    rng = _rmax(e, 252) - _rmin(e, 252)
    b = (e - _rmin(e, 252)) / rng.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebitdaratio_pctl over 126d
def f49vb_f49_valuation_breadth_book_evebitdaratio_pctl_504d_slope_v115_signal(evebit, evebitda):
    sp = _f49_evebit(evebit) / _f49_evebit(evebitda).replace(0, np.nan)
    b = sp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvfloorrank over 126d
def f49vb_f49_valuation_breadth_book_tbvfloorrank_504d_slope_v116_signal(tbvps, bvps):
    f = _f49_tbv_floor(tbvps, bvps)
    b = _rank(f, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvcushionz over 63d
def f49vb_f49_valuation_breadth_book_tbvcushionz_252d_slope_v117_signal(bvps, tbvps, marketcap):
    cush = _f49_cushion(tbvps, bvps)
    mg = _f49_log_growth(marketcap, 63)
    b = _z(cush, 252) + np.sign(mg)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvcushiontrend over 42d
def f49vb_f49_valuation_breadth_book_tbvcushiontrend_126d_slope_v118_signal(intangibles, equity):
    ig = _f49_log_growth(intangibles, 63)
    eg = _f49_log_growth(equity, 63)
    b = (ig - eg) - (ig - eg).shift(126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvgrowthrank over 126d
def f49vb_f49_valuation_breadth_book_tbvgrowthrank_504d_slope_v119_signal(tbvps):
    g = _f49_bvps_growth(tbvps, 252)
    b = _rank(g, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvaccel over 63d
def f49vb_f49_valuation_breadth_book_tbvaccel_252d_slope_v120_signal(tbvps):
    g = _f49_bvps_growth(tbvps, 63)
    b = g - g.shift(63)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tbvtomcap over 63d
def f49vb_f49_valuation_breadth_book_tbvtomcap_252d_slope_v121_signal(tbvps, pb, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    b = 1.0 / pt
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsdrawup over 63d
def f49vb_f49_valuation_breadth_book_bvpsdrawup_252d_slope_v122_signal(bvps):
    mn = _rmin(bvps, 252)
    b = bvps / mn.replace(0, np.nan) - 1.0
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsyoy over 126d
def f49vb_f49_valuation_breadth_book_bvpsyoy_504d_slope_v123_signal(bvps):
    b = _f49_log_growth(bvps, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpssmoothgrow over 63d
def f49vb_f49_valuation_breadth_book_bvpssmoothgrow_252d_slope_v124_signal(bvps):
    lg = _f49_log_growth(bvps, 63)
    b = lg.ewm(span=63, min_periods=21).mean()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bvpsgrowthtanh over 63d
def f49vb_f49_valuation_breadth_book_bvpsgrowthtanh_252d_slope_v125_signal(bvps):
    g = _f49_bvps_growth(bvps, 252)
    b = np.tanh(_z(g, 252))
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intangshareyoy over 63d
def f49vb_f49_valuation_breadth_book_intangshareyoy_252d_slope_v126_signal(intangibles, equity):
    s = _f49_intang_share(intangibles, equity)
    b = _f49_log_growth(s, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intanggrowthz over 63d
def f49vb_f49_valuation_breadth_book_intanggrowthz_252d_slope_v127_signal(intangibles):
    g = _f49_log_growth(intangibles, 252)
    b = _z(g, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tangsharerank over 126d
def f49vb_f49_valuation_breadth_book_tangsharerank_504d_slope_v128_signal(tangibles, equity):
    s = _f49_tang_share(tangibles, equity)
    b = _rank(s, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of tangtointangtrend over 42d
def f49vb_f49_valuation_breadth_book_tangtointangtrend_126d_slope_v129_signal(tangibles, intangibles):
    r = tangibles / intangibles.replace(0, np.nan)
    b = _f49_log_growth(r, 126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of equitygrowthaccel over 63d
def f49vb_f49_valuation_breadth_book_equitygrowthaccel_252d_slope_v130_signal(equity):
    g = _f49_log_growth(equity, 63)
    b = g - g.shift(63)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of intangtomcap over 63d
def f49vb_f49_valuation_breadth_book_intangtomcap_252d_slope_v131_signal(intangibles, marketcap):
    b = intangibles / marketcap.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evmcaprank over 126d
def f49vb_f49_valuation_breadth_book_evmcaprank_504d_slope_v132_signal(ev, marketcap):
    r = ev / marketcap.replace(0, np.nan)
    b = _rank(r, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of mcapbookrank over 126d
def f49vb_f49_valuation_breadth_book_mcapbookrank_504d_slope_v133_signal(marketcap, equity):
    r = marketcap / equity.replace(0, np.nan)
    b = -_rank(r, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of mcapbooktrend over 42d
def f49vb_f49_valuation_breadth_book_mcapbooktrend_126d_slope_v134_signal(marketcap, equity):
    r = marketcap / equity.replace(0, np.nan)
    b = _f49_log_growth(r, 126)
    base = b
    d = base.diff(42) / float(42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of mcaptangz over 63d
def f49vb_f49_valuation_breadth_book_mcaptangz_252d_slope_v135_signal(marketcap, tangibles):
    r = marketcap / tangibles.replace(0, np.nan)
    b = -_z(r, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evtotang over 63d
def f49vb_f49_valuation_breadth_book_evtotang_252d_slope_v136_signal(ev, tangibles):
    r = ev / tangibles.replace(0, np.nan)
    b = _z(r, 252)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evtoequity over 63d
def f49vb_f49_valuation_breadth_book_evtoequity_252d_slope_v137_signal(ev, equity):
    b = ev / equity.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityieldmom over 10d
def f49vb_f49_valuation_breadth_book_ebityieldmom_21d_slope_v138_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = y - y.shift(21)
    base = b
    d = base.diff(10) / float(10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityieldtanh over 63d
def f49vb_f49_valuation_breadth_book_ebityieldtanh_252d_slope_v139_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = np.tanh(_z(y, 252))
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityieldsignmag over 126d
def f49vb_f49_valuation_breadth_book_ebityieldsignmag_504d_slope_v140_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    m = _mean(y, 504)
    d = y - m
    b = np.sign(d) * (d.abs() ** 0.5)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ebityielddisp over 63d
def f49vb_f49_valuation_breadth_book_ebityielddisp_252d_slope_v141_signal(ebit, ev):
    y = _f49_ebit_yield(ebit, ev)
    b = _std(y, 63) / _mean(y, 252).abs().replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bookebit_minblend over 63d
def f49vb_f49_valuation_breadth_book_bookebit_minblend_252d_slope_v142_signal(pb, evebit):
    cb = -_z(_f49_pb(pb), 252)
    ce = -_z(_f49_evebit(evebit), 252)
    b = pd.concat([cb, ce], axis=1).min(axis=1)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of fullbreadth over 63d
def f49vb_f49_valuation_breadth_book_fullbreadth_252d_slope_v143_signal(pb, tbvps, bvps, evebit, evebitda):
    pt = _f49_ptb(pb, tbvps, bvps)
    a = -_z(pt, 252)
    c = -_z(_f49_evebit(evebit), 252)
    d = -_z(_f49_evebit(evebitda), 252)
    st = pd.concat([a, c, d], axis=1)
    b = st.mean(axis=1)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of qualcheap_ebit over 63d
def f49vb_f49_valuation_breadth_book_qualcheap_ebit_252d_slope_v144_signal(evebit, tbvps, bvps):
    floorz = _z(_f49_tbv_floor(tbvps, bvps), 252)
    cheap = -_z(_f49_evebit(evebit), 252)
    b = cheap + 0.7 * floorz
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebit_to_intang over 63d
def f49vb_f49_valuation_breadth_book_evebit_to_intang_252d_slope_v145_signal(evebit, intangibles, equity):
    e = _f49_evebit(evebit)
    s = _f49_intang_share(intangibles, equity)
    b = e * (1.0 + s)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of cheapquality_blend over 63d
def f49vb_f49_valuation_breadth_book_cheapquality_blend_252d_slope_v146_signal(pb, intangibles, equity):
    cheap = -_z(_f49_pb(pb), 252)
    tq = -_z(_f49_intang_share(intangibles, equity), 252)
    b = 0.5 * (cheap + tq)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of bookebit_corrgap over 63d
def f49vb_f49_valuation_breadth_book_bookebit_corrgap_252d_slope_v147_signal(pb, evebit):
    cb = -_rank(_f49_pb(pb), 252)
    ce = -_rank(_f49_evebit(evebit), 252)
    b = (cb - ce).abs()
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebit_growthadj_rank over 126d
def f49vb_f49_valuation_breadth_book_evebit_growthadj_rank_504d_slope_v148_signal(evebit, tbvps):
    e = _f49_evebit(evebit)
    g = _f49_bvps_growth(tbvps, 252)
    b = _rank(g, 504) - _rank(e, 504)
    base = b
    d = base.diff(126) / float(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of ptb_growthadj over 63d
def f49vb_f49_valuation_breadth_book_ptb_growthadj_252d_slope_v149_signal(pb, tbvps, bvps):
    pt = _f49_ptb(pb, tbvps, bvps)
    g = _f49_bvps_growth(tbvps, 252)
    b = g / pt
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st math derivative) of evebityield_mcap over 63d
def f49vb_f49_valuation_breadth_book_evebityield_mcap_252d_slope_v150_signal(ebit, marketcap):
    b = ebit / marketcap.replace(0, np.nan)
    base = b
    d = base.diff(63) / float(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f49vb_f49_valuation_breadth_book_pblvl_252d_slope_v001_signal,
    f49vb_f49_valuation_breadth_book_pbcheapz_252d_slope_v002_signal,
    f49vb_f49_valuation_breadth_book_pbcheapz_504d_slope_v003_signal,
    f49vb_f49_valuation_breadth_book_pbcheaprank_252d_slope_v004_signal,
    f49vb_f49_valuation_breadth_book_pbtrend_63d_slope_v005_signal,
    f49vb_f49_valuation_breadth_book_pbtrend_126d_slope_v006_signal,
    f49vb_f49_valuation_breadth_book_pbdisp_63d_slope_v007_signal,
    f49vb_f49_valuation_breadth_book_pbpctl_504d_slope_v008_signal,
    f49vb_f49_valuation_breadth_book_pbmom_21d_slope_v009_signal,
    f49vb_f49_valuation_breadth_book_pbema_disp_252d_slope_v010_signal,
    f49vb_f49_valuation_breadth_book_pbsignmag_252d_slope_v011_signal,
    f49vb_f49_valuation_breadth_book_pbtanh_252d_slope_v012_signal,
    f49vb_f49_valuation_breadth_book_pbgapbook_252d_slope_v013_signal,
    f49vb_f49_valuation_breadth_book_pbinvyieldz_252d_slope_v014_signal,
    f49vb_f49_valuation_breadth_book_ptblvl_252d_slope_v015_signal,
    f49vb_f49_valuation_breadth_book_ptbcheapz_252d_slope_v016_signal,
    f49vb_f49_valuation_breadth_book_ptbcheaprank_252d_slope_v017_signal,
    f49vb_f49_valuation_breadth_book_ptbpctl_504d_slope_v018_signal,
    f49vb_f49_valuation_breadth_book_ptbtrend_63d_slope_v019_signal,
    f49vb_f49_valuation_breadth_book_ptbmom_21d_slope_v020_signal,
    f49vb_f49_valuation_breadth_book_ptbspread_252d_slope_v021_signal,
    f49vb_f49_valuation_breadth_book_ptbema_disp_252d_slope_v022_signal,
    f49vb_f49_valuation_breadth_book_ptbtanh_252d_slope_v023_signal,
    f49vb_f49_valuation_breadth_book_tbvfloor_252d_slope_v024_signal,
    f49vb_f49_valuation_breadth_book_tbvfloorz_252d_slope_v025_signal,
    f49vb_f49_valuation_breadth_book_tbvcushion_252d_slope_v026_signal,
    f49vb_f49_valuation_breadth_book_tbvcushionrank_252d_slope_v027_signal,
    f49vb_f49_valuation_breadth_book_tbvfloortrend_126d_slope_v028_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowth_252d_slope_v029_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowth_63d_slope_v030_signal,
    f49vb_f49_valuation_breadth_book_tbvloggrowth_126d_slope_v031_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowthz_252d_slope_v032_signal,
    f49vb_f49_valuation_breadth_book_negtbvflag_252d_slope_v033_signal,
    f49vb_f49_valuation_breadth_book_tbvbookgap_z_252d_slope_v034_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowth_252d_slope_v035_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowth_63d_slope_v036_signal,
    f49vb_f49_valuation_breadth_book_bvpsloggrowth_126d_slope_v037_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowthz_252d_slope_v038_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowthrank_504d_slope_v039_signal,
    f49vb_f49_valuation_breadth_book_bvpsaccel_252d_slope_v040_signal,
    f49vb_f49_valuation_breadth_book_bvpstrendslope_126d_slope_v041_signal,
    f49vb_f49_valuation_breadth_book_bvpsdispersion_252d_slope_v042_signal,
    f49vb_f49_valuation_breadth_book_evebitlvl_252d_slope_v043_signal,
    f49vb_f49_valuation_breadth_book_evebitcheapz_252d_slope_v044_signal,
    f49vb_f49_valuation_breadth_book_evebitcheapz_504d_slope_v045_signal,
    f49vb_f49_valuation_breadth_book_evebitcheaprank_252d_slope_v046_signal,
    f49vb_f49_valuation_breadth_book_evebitshortlong_504d_slope_v047_signal,
    f49vb_f49_valuation_breadth_book_evebitrangepos_252d_slope_v048_signal,
    f49vb_f49_valuation_breadth_book_evebittrend_63d_slope_v049_signal,
    f49vb_f49_valuation_breadth_book_evebittrend_126d_slope_v050_signal,
    f49vb_f49_valuation_breadth_book_evebitmom_21d_slope_v051_signal,
    f49vb_f49_valuation_breadth_book_evebitdisp_63d_slope_v052_signal,
    f49vb_f49_valuation_breadth_book_evebitema_disp_252d_slope_v053_signal,
    f49vb_f49_valuation_breadth_book_evebittanh_252d_slope_v054_signal,
    f49vb_f49_valuation_breadth_book_evebitsignmag_252d_slope_v055_signal,
    f49vb_f49_valuation_breadth_book_evebityield_gap_252d_slope_v056_signal,
    f49vb_f49_valuation_breadth_book_evebityieldcross_252d_slope_v057_signal,
    f49vb_f49_valuation_breadth_book_evebitdalvl_252d_slope_v058_signal,
    f49vb_f49_valuation_breadth_book_evebitdacheapz_252d_slope_v059_signal,
    f49vb_f49_valuation_breadth_book_evebitdacheaprank_252d_slope_v060_signal,
    f49vb_f49_valuation_breadth_book_evebitdapctl_504d_slope_v061_signal,
    f49vb_f49_valuation_breadth_book_evebitdatrend_63d_slope_v062_signal,
    f49vb_f49_valuation_breadth_book_evebitdamom_21d_slope_v063_signal,
    f49vb_f49_valuation_breadth_book_evebitdayield_z_252d_slope_v064_signal,
    f49vb_f49_valuation_breadth_book_evebitdaspread_252d_slope_v065_signal,
    f49vb_f49_valuation_breadth_book_evebitdaspreadz_252d_slope_v066_signal,
    f49vb_f49_valuation_breadth_book_evebitdaema_disp_252d_slope_v067_signal,
    f49vb_f49_valuation_breadth_book_ebityield_252d_slope_v068_signal,
    f49vb_f49_valuation_breadth_book_ebityieldz_252d_slope_v069_signal,
    f49vb_f49_valuation_breadth_book_ebityieldrank_504d_slope_v070_signal,
    f49vb_f49_valuation_breadth_book_ebityieldtrend_126d_slope_v071_signal,
    f49vb_f49_valuation_breadth_book_ebitposflag_252d_slope_v072_signal,
    f49vb_f49_valuation_breadth_book_ebitmargin_ev_252d_slope_v073_signal,
    f49vb_f49_valuation_breadth_book_intangshare_252d_slope_v074_signal,
    f49vb_f49_valuation_breadth_book_intangsharez_252d_slope_v075_signal,
    f49vb_f49_valuation_breadth_book_intangsharerank_504d_slope_v076_signal,
    f49vb_f49_valuation_breadth_book_intangsharetrend_126d_slope_v077_signal,
    f49vb_f49_valuation_breadth_book_tangshare_252d_slope_v078_signal,
    f49vb_f49_valuation_breadth_book_tangsharez_252d_slope_v079_signal,
    f49vb_f49_valuation_breadth_book_tangtointang_252d_slope_v080_signal,
    f49vb_f49_valuation_breadth_book_intanggrowth_252d_slope_v081_signal,
    f49vb_f49_valuation_breadth_book_equitygrowth_252d_slope_v082_signal,
    f49vb_f49_valuation_breadth_book_equitygrowthz_252d_slope_v083_signal,
    f49vb_f49_valuation_breadth_book_negequityflag_252d_slope_v084_signal,
    f49vb_f49_valuation_breadth_book_evmcapratio_252d_slope_v085_signal,
    f49vb_f49_valuation_breadth_book_evmcapratioz_252d_slope_v086_signal,
    f49vb_f49_valuation_breadth_book_evmcaptrend_126d_slope_v087_signal,
    f49vb_f49_valuation_breadth_book_mcapbookratio_252d_slope_v088_signal,
    f49vb_f49_valuation_breadth_book_mcapbookz_252d_slope_v089_signal,
    f49vb_f49_valuation_breadth_book_mcaptangratio_252d_slope_v090_signal,
    f49vb_f49_valuation_breadth_book_bookebit_blend_252d_slope_v091_signal,
    f49vb_f49_valuation_breadth_book_bookebit_disagree_252d_slope_v092_signal,
    f49vb_f49_valuation_breadth_book_tbvebit_blend_252d_slope_v093_signal,
    f49vb_f49_valuation_breadth_book_multibreadth_252d_slope_v094_signal,
    f49vb_f49_valuation_breadth_book_multidisp_252d_slope_v095_signal,
    f49vb_f49_valuation_breadth_book_qualcheap_252d_slope_v096_signal,
    f49vb_f49_valuation_breadth_book_evebit_to_bvgrowth_252d_slope_v097_signal,
    f49vb_f49_valuation_breadth_book_pb_to_bvgrowth_252d_slope_v098_signal,
    f49vb_f49_valuation_breadth_book_pbcheaprank_504d_slope_v099_signal,
    f49vb_f49_valuation_breadth_book_pbyoy_252d_slope_v100_signal,
    f49vb_f49_valuation_breadth_book_pbmedrev_252d_slope_v101_signal,
    f49vb_f49_valuation_breadth_book_pbvolratio_252d_slope_v102_signal,
    f49vb_f49_valuation_breadth_book_pbskew_252d_slope_v103_signal,
    f49vb_f49_valuation_breadth_book_pbdrawup_252d_slope_v104_signal,
    f49vb_f49_valuation_breadth_book_evebitcheapdd_504d_slope_v105_signal,
    f49vb_f49_valuation_breadth_book_evebityoy_252d_slope_v106_signal,
    f49vb_f49_valuation_breadth_book_evebitmedrev_252d_slope_v107_signal,
    f49vb_f49_valuation_breadth_book_evebitvolratio_252d_slope_v108_signal,
    f49vb_f49_valuation_breadth_book_evebitskew_252d_slope_v109_signal,
    f49vb_f49_valuation_breadth_book_evebitdrawdn_252d_slope_v110_signal,
    f49vb_f49_valuation_breadth_book_evebitcompress_252d_slope_v111_signal,
    f49vb_f49_valuation_breadth_book_evebitdayoy_252d_slope_v112_signal,
    f49vb_f49_valuation_breadth_book_evebitdamedrev_252d_slope_v113_signal,
    f49vb_f49_valuation_breadth_book_evebitdacompress_252d_slope_v114_signal,
    f49vb_f49_valuation_breadth_book_evebitdaratio_pctl_504d_slope_v115_signal,
    f49vb_f49_valuation_breadth_book_tbvfloorrank_504d_slope_v116_signal,
    f49vb_f49_valuation_breadth_book_tbvcushionz_252d_slope_v117_signal,
    f49vb_f49_valuation_breadth_book_tbvcushiontrend_126d_slope_v118_signal,
    f49vb_f49_valuation_breadth_book_tbvgrowthrank_504d_slope_v119_signal,
    f49vb_f49_valuation_breadth_book_tbvaccel_252d_slope_v120_signal,
    f49vb_f49_valuation_breadth_book_tbvtomcap_252d_slope_v121_signal,
    f49vb_f49_valuation_breadth_book_bvpsdrawup_252d_slope_v122_signal,
    f49vb_f49_valuation_breadth_book_bvpsyoy_504d_slope_v123_signal,
    f49vb_f49_valuation_breadth_book_bvpssmoothgrow_252d_slope_v124_signal,
    f49vb_f49_valuation_breadth_book_bvpsgrowthtanh_252d_slope_v125_signal,
    f49vb_f49_valuation_breadth_book_intangshareyoy_252d_slope_v126_signal,
    f49vb_f49_valuation_breadth_book_intanggrowthz_252d_slope_v127_signal,
    f49vb_f49_valuation_breadth_book_tangsharerank_504d_slope_v128_signal,
    f49vb_f49_valuation_breadth_book_tangtointangtrend_126d_slope_v129_signal,
    f49vb_f49_valuation_breadth_book_equitygrowthaccel_252d_slope_v130_signal,
    f49vb_f49_valuation_breadth_book_intangtomcap_252d_slope_v131_signal,
    f49vb_f49_valuation_breadth_book_evmcaprank_504d_slope_v132_signal,
    f49vb_f49_valuation_breadth_book_mcapbookrank_504d_slope_v133_signal,
    f49vb_f49_valuation_breadth_book_mcapbooktrend_126d_slope_v134_signal,
    f49vb_f49_valuation_breadth_book_mcaptangz_252d_slope_v135_signal,
    f49vb_f49_valuation_breadth_book_evtotang_252d_slope_v136_signal,
    f49vb_f49_valuation_breadth_book_evtoequity_252d_slope_v137_signal,
    f49vb_f49_valuation_breadth_book_ebityieldmom_21d_slope_v138_signal,
    f49vb_f49_valuation_breadth_book_ebityieldtanh_252d_slope_v139_signal,
    f49vb_f49_valuation_breadth_book_ebityieldsignmag_504d_slope_v140_signal,
    f49vb_f49_valuation_breadth_book_ebityielddisp_252d_slope_v141_signal,
    f49vb_f49_valuation_breadth_book_bookebit_minblend_252d_slope_v142_signal,
    f49vb_f49_valuation_breadth_book_fullbreadth_252d_slope_v143_signal,
    f49vb_f49_valuation_breadth_book_qualcheap_ebit_252d_slope_v144_signal,
    f49vb_f49_valuation_breadth_book_evebit_to_intang_252d_slope_v145_signal,
    f49vb_f49_valuation_breadth_book_cheapquality_blend_252d_slope_v146_signal,
    f49vb_f49_valuation_breadth_book_bookebit_corrgap_252d_slope_v147_signal,
    f49vb_f49_valuation_breadth_book_evebit_growthadj_rank_504d_slope_v148_signal,
    f49vb_f49_valuation_breadth_book_ptb_growthadj_252d_slope_v149_signal,
    f49vb_f49_valuation_breadth_book_evebityield_mcap_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_VALUATION_BREADTH_BOOK_SLOPE_REGISTRY_001_150 = REGISTRY

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

    assert n_features == 150, n_features
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

    print("OK f49_valuation_breadth_book_2nd_derivatives_001_150_claude.py: %d features pass" % n_features)
