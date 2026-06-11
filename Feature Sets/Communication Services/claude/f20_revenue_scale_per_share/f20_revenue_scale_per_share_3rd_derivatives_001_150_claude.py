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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _f20_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f20_pershare(rev, sh):
    return rev / sh.replace(0, np.nan)


def _f20_scale(s):
    return np.log(s.replace(0, np.nan))


def _f20_accel(s, w):
    g = np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))
    return g - g.shift(w)


def _f20_fxdiverge(reported, usd):
    return reported / usd.replace(0, np.nan) - 1.0


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    sl = (s - s.shift(w)) / float(w)
    return (sl - sl.shift(w)) / float(w)



def f20rs_f20_revenue_scale_per_share_spslevel_252d_jerk_v001_signal(sps):
    b = _f20_scale(sps)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgr63_63d_jerk_v002_signal(sps):
    b = _f20_loggrowth(sps, 63)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgr126_126d_jerk_v003_signal(sps):
    b = _f20_loggrowth(sps, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgr252_252d_jerk_v004_signal(sps):
    b = _f20_loggrowth(sps, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revscale_252d_jerk_v005_signal(revenue):
    b = _f20_scale(revenue)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revgr63_63d_jerk_v006_signal(revenue):
    b = _f20_loggrowth(revenue, 63)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revgr126_126d_jerk_v007_signal(revenue):
    b = _f20_loggrowth(revenue, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revgr252_252d_jerk_v008_signal(revenue):
    b = _f20_loggrowth(revenue, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdscale_252d_jerk_v009_signal(revenueusd):
    b = _f20_scale(revenueusd)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdgr252_252d_jerk_v010_signal(revenueusd):
    b = _f20_loggrowth(revenueusd, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsscale_252d_jerk_v011_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    b = _rank(_f20_scale(rps), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsgr126_126d_jerk_v012_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    b = _z(_f20_loggrowth(rps, 126), 252)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsgr252_252d_jerk_v013_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    b = _rank(_f20_loggrowth(rps, 252), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_shscale_252d_jerk_v014_signal(shareswa):
    b = _f20_scale(shareswa)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_shgr252_252d_jerk_v015_signal(shareswa):
    b = _f20_loggrowth(shareswa, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdpsscale_252d_jerk_v016_signal(revenueusd, shareswa):
    ups = _f20_pershare(revenueusd, shareswa)
    b = _z(_f20_scale(ups), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxdiv_126d_jerk_v017_signal(revenue, revenueusd):
    b = _f20_fxdiverge(revenue, revenueusd)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxgap_126d_jerk_v018_signal(revenue, revenueusd):
    gap = _f20_scale(revenueusd) - _f20_scale(revenue)
    b = _std(gap, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsz252_252d_jerk_v019_signal(sps):
    b = _z(sps, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revz252_252d_jerk_v020_signal(revenue):
    b = _z(revenue, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgrspr_252d_jerk_v021_signal(sps):
    b = _f20_loggrowth(sps, 63) - _f20_loggrowth(sps, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revgrspr_252d_jerk_v022_signal(revenue):
    b = _f20_loggrowth(revenue, 63) - _f20_loggrowth(revenue, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsema_126d_jerk_v023_signal(sps):
    ls = _f20_scale(sps)
    b = ls - ls.ewm(span=63, min_periods=21).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revema_126d_jerk_v024_signal(revenue):
    ls = _f20_scale(revenue)
    b = ls - ls.ewm(span=126, min_periods=42).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsdd252_252d_jerk_v025_signal(sps):
    hi = _rmax(sps, 252)
    b = sps / hi.replace(0, np.nan) - 1.0
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revdd252_252d_jerk_v026_signal(revenue):
    hi = _rmax(revenue, 252)
    b = revenue / hi.replace(0, np.nan) - 1.0
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsrngpos_504d_jerk_v027_signal(sps):
    hi = _rmax(sps, 504)
    lo = _rmin(sps, 504)
    pos = (sps - lo) / (hi - lo).replace(0, np.nan)
    b = _z(pos, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revrngpos_504d_jerk_v028_signal(revenue):
    hi = _rmax(revenue, 504)
    lo = _rmin(revenue, 504)
    pos = (revenue - lo) / (hi - lo).replace(0, np.nan)
    b = _z(pos, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spscagr_504d_jerk_v029_signal(sps):
    b = _f20_loggrowth(sps, 504) * (252.0 / 504.0)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk of dilution-adjusted per-share scaling smoothness (clean-compounding efficiency)
def f20rs_f20_revenue_scale_per_share_cleaneff_504d_jerk_v030_signal(sps, shareswa):
    net = _f20_loggrowth(sps, 504) - _f20_loggrowth(shareswa, 504)
    path = _f20_loggrowth(sps, 63).abs().rolling(504, min_periods=252).sum()
    b = net / path.replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsaccel126_126d_jerk_v031_signal(sps):
    b = _f20_accel(sps, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revaccel126_126d_jerk_v032_signal(revenue):
    b = _f20_accel(revenue, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdaccel126_126d_jerk_v033_signal(revenueusd):
    b = _f20_accel(revenueusd, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_shaccel126_126d_jerk_v034_signal(shareswa):
    b = _f20_accel(shareswa, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_dildrag_252d_jerk_v035_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 252)
    shg = _f20_loggrowth(shareswa, 252)
    b = shg / (rg.abs() + 0.02)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsstab_252d_jerk_v036_signal(sps):
    g = _f20_loggrowth(sps, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revstab_252d_jerk_v037_signal(revenue):
    g = _f20_loggrowth(revenue, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdstab_252d_jerk_v038_signal(revenueusd):
    g = _f20_loggrowth(revenueusd, 63)
    b = _mean(g, 252) / _std(g, 252).replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgrrank_504d_jerk_v039_signal(sps):
    g = _f20_loggrowth(sps, 252)
    b = _rank(g, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revgrrank_504d_jerk_v040_signal(revenue):
    g = _f20_loggrowth(revenue, 252)
    b = _rank(g, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxz_252d_jerk_v041_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = _z(d, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdgrgap_252d_jerk_v042_signal(revenue, revenueusd):
    b = _f20_loggrowth(revenue, 252) - _f20_loggrowth(revenueusd, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsinflect_126d_jerk_v043_signal(sps):
    g = _f20_loggrowth(sps, 126)
    b = _rank(g - _mean(g, 252), 504)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revinflect_126d_jerk_v044_signal(revenue):
    g = _f20_loggrowth(revenue, 126)
    b = _rank(g - _mean(g, 252), 504)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsadv_252d_jerk_v045_signal(sps, revenue):
    b = _f20_loggrowth(sps, 252) - _f20_loggrowth(revenue, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsz_252d_jerk_v046_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    b = _z(rps, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsdisp_126d_jerk_v047_signal(sps):
    ls = _f20_scale(sps)
    b = ls - ls.ewm(span=126, min_periods=63).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revdisp_126d_jerk_v048_signal(revenue):
    ls = _f20_scale(revenue)
    disp = ls - ls.ewm(span=252, min_periods=63).mean()
    b = _z(disp, 252)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsslope63_63d_jerk_v049_signal(sps):
    ls = _f20_scale(sps)
    sl = (ls - ls.shift(63)) / 63.0
    vol = _std(_f20_loggrowth(sps, 21), 252).replace(0, np.nan)
    b = sl / vol
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revslope63_63d_jerk_v050_signal(revenue):
    ls = _f20_scale(revenue)
    sl = (ls - ls.shift(63)) / 63.0
    vol = _std(_f20_loggrowth(revenue, 21), 252).replace(0, np.nan)
    b = sl / vol
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsceil_504d_jerk_v051_signal(sps):
    hi = _rmax(sps, 504)
    raw = np.log(sps.replace(0, np.nan) / hi.replace(0, np.nan))
    b = raw.ewm(span=63, min_periods=21).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revfloor_504d_jerk_v052_signal(revenue):
    lo = _rmin(revenue, 504)
    b = np.log(revenue.replace(0, np.nan) / lo.replace(0, np.nan))
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsmemory_504d_jerk_v053_signal(sps):
    anchor = _rmax(sps, 504).shift(126)
    raw = np.log(sps.replace(0, np.nan) / anchor.replace(0, np.nan))
    b = _rank(raw, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revmemory_504d_jerk_v054_signal(revenue):
    anchor = _rmax(revenue, 504).shift(126)
    b = np.log(revenue.replace(0, np.nan) / anchor.replace(0, np.nan))
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revgrvol_252d_jerk_v055_signal(revenue):
    g = _f20_loggrowth(revenue, 21)
    b = _std(g, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgrvol_252d_jerk_v056_signal(sps):
    g = _f20_loggrowth(sps, 21)
    b = _std(g, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_sizetier_504d_jerk_v057_signal(revenue):
    ls = _f20_scale(revenue)
    b = ls - ls.rolling(504, min_periods=126).median()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spssizetier_504d_jerk_v058_signal(sps):
    ls = _f20_scale(sps)
    b = ls - ls.rolling(504, min_periods=126).median()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdscalez_504d_jerk_v059_signal(revenueusd):
    b = _z(_f20_scale(revenueusd), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgr504_504d_jerk_v060_signal(sps):
    b = _z(_f20_loggrowth(sps, 504), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spstrendreg_189d_jerk_v061_signal(sps):
    ls = _f20_scale(sps)
    b = ls.ewm(span=42, min_periods=21).mean() - ls.ewm(span=189, min_periods=63).mean()
    d = _jerk(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revtrendreg_189d_jerk_v062_signal(revenue):
    ls = _f20_scale(revenue)
    b = ls.ewm(span=42, min_periods=21).mean() - ls.ewm(span=189, min_periods=63).mean()
    d = _jerk(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spshalfbal_252d_jerk_v063_signal(sps):
    b = 2.0 * _f20_loggrowth(sps, 126) - _f20_loggrowth(sps, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revhalfbal_252d_jerk_v064_signal(revenue):
    b = 2.0 * _f20_loggrowth(revenue, 126) - _f20_loggrowth(revenue, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spseff_252d_jerk_v065_signal(sps):
    net = (sps - sps.shift(252)).abs()
    path = sps.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_reveff_252d_jerk_v066_signal(revenue):
    net = (revenue - revenue.shift(252)).abs()
    path = revenue.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsturb_252d_jerk_v067_signal(sps):
    g = _f20_loggrowth(sps, 63)
    b = _std(g, 252) / (_mean(g, 252).abs() + 0.01)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revturb_252d_jerk_v068_signal(revenue):
    g = _f20_loggrowth(revenue, 63)
    b = _std(g, 252) / (_mean(g, 252).abs() + 0.01)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_psleader_504d_jerk_v069_signal(sps, revenue):
    rs = _rank(_f20_loggrowth(sps, 252), 504)
    rr = _rank(_f20_loggrowth(revenue, 252), 504)
    b = rs - rr
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_netscale_252d_jerk_v070_signal(sps, shareswa):
    sg = _f20_loggrowth(sps, 252)
    shg = _f20_loggrowth(shareswa, 252)
    b = np.tanh(3.0 * sg) - np.tanh(8.0 * shg)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_cleanps_126d_jerk_v071_signal(sps, shareswa):
    spsg = _f20_loggrowth(sps, 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = _z((spsg - shg), 252)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsriskadj_252d_jerk_v072_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 63)
    vol = _std(_f20_loggrowth(rps, 21), 252).replace(0, np.nan)
    b = g / vol
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revddsm_504d_jerk_v073_signal(revenue):
    hi = _rmax(revenue, 504)
    dd = revenue / hi.replace(0, np.nan) - 1.0
    b = _mean(dd, 126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsddsm_504d_jerk_v074_signal(sps):
    hi = _rmax(sps, 504)
    dd = sps / hi.replace(0, np.nan) - 1.0
    b = _mean(dd, 126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_relaccel_63d_jerk_v075_signal(revenue):
    g63 = _f20_loggrowth(revenue, 63)
    drift = _mean(_f20_loggrowth(revenue, 63), 504)
    b = g63 / (drift.abs() + 0.01) - 1.0
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsrelaccel_126d_jerk_v076_signal(sps):
    g126 = _f20_loggrowth(sps, 126)
    drift = _mean(_f20_loggrowth(sps, 126), 504)
    b = _rank(g126 / (drift.abs() + 0.01) - 1.0, 504)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_pstension_252d_jerk_v077_signal(revenue, shareswa):
    rpsg = _f20_loggrowth(_f20_pershare(revenue, shareswa), 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = np.tanh(5.0 * rpsg) + np.tanh(10.0 * shg)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxtrend_126d_jerk_v078_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = (d - d.shift(126)) / 126.0
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxrank_504d_jerk_v079_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = _rank(d, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdgrz_252d_jerk_v080_signal(revenueusd):
    b = _z(_f20_loggrowth(revenueusd, 252), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdinflect_126d_jerk_v081_signal(revenueusd):
    g = _f20_loggrowth(revenueusd, 126)
    b = g - _mean(g, 252)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsmom_ema_126d_jerk_v082_signal(sps):
    g = _f20_loggrowth(sps, 126)
    b = g.ewm(span=63, min_periods=21).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revmom_ema_126d_jerk_v083_signal(revenue):
    g = _f20_loggrowth(revenue, 126)
    b = g.ewm(span=63, min_periods=21).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsyoychg_252d_jerk_v084_signal(sps):
    g = _f20_loggrowth(sps, 252)
    b = g - g.shift(126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revyoychg_252d_jerk_v085_signal(revenue):
    g = _f20_loggrowth(revenue, 252)
    b = g - g.shift(126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsslope126_126d_jerk_v086_signal(sps):
    ls = _f20_scale(sps)
    sl = (ls - ls.shift(126)) / 126.0
    b = _rank(sl, 504)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revslope126_126d_jerk_v087_signal(revenue):
    ls = _f20_scale(revenue)
    sl = (ls - ls.shift(126)) / 126.0
    b = _rank(sl, 504)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsheadroom_504d_jerk_v088_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    hi = _rmax(rps, 504)
    b = np.log(rps.replace(0, np.nan) / hi.replace(0, np.nan))
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdpsdisp_126d_jerk_v089_signal(revenueusd, shareswa):
    ups = _f20_scale(_f20_pershare(revenueusd, shareswa))
    b = ups - ups.ewm(span=63, min_periods=21).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxmag_126d_jerk_v090_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd).abs()
    b = _mean(d, 126)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsscalerank_504d_jerk_v091_signal(sps):
    b = _rank(_f20_scale(sps), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revscalerank_504d_jerk_v092_signal(revenue):
    b = _rank(_f20_scale(revenue), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsconvex_252d_jerk_v093_signal(sps):
    g = _f20_loggrowth(sps, 252)
    z = _z(g, 252)
    b = np.sign(z) * (z ** 2)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revconvex_252d_jerk_v094_signal(revenue):
    z = _z(_f20_scale(revenue), 252)
    b = np.sign(z) * (z ** 2)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsspan_252d_jerk_v095_signal(sps):
    hi = _rmax(sps, 252)
    lo = _rmin(sps, 252)
    b = (hi - lo) / sps.replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revspan_252d_jerk_v096_signal(revenue):
    hi = _rmax(revenue, 252)
    lo = _rmin(revenue, 252)
    b = (hi - lo) / revenue.replace(0, np.nan)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spslongrank_504d_jerk_v097_signal(sps, revenue):
    sg = _f20_loggrowth(sps, 504)
    rg = _f20_loggrowth(revenue, 504)
    b = sg - rg
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revlongrz_504d_jerk_v098_signal(revenue):
    b = _z(_f20_loggrowth(revenue, 504), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsnearpos_252d_jerk_v099_signal(sps):
    hi = _rmax(sps, 252)
    lo = _rmin(sps, 252)
    b = (sps - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revnearpos_252d_jerk_v100_signal(revenue):
    hi = _rmax(revenue, 252)
    lo = _rmin(revenue, 252)
    b = (revenue - lo) / (hi - lo).replace(0, np.nan) - 0.5
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxsignmag_126d_jerk_v101_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = np.sign(d) * (d.abs() ** 0.5)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxlevelwedge_252d_jerk_v102_signal(revenue, revenueusd):
    wedge = _f20_scale(revenueusd) - _f20_scale(revenue)
    b = wedge.ewm(span=126, min_periods=42).mean() - wedge.ewm(span=504, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_psratio_504d_jerk_v103_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    ratio = _f20_scale(rps) / _f20_scale(revenue).replace(0, np.nan)
    b = ratio - ratio.shift(126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_rpsweighted_126d_jerk_v104_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 126)
    w = _rank(_f20_scale(rps), 504) + 0.5
    b = g * w
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsquality_126d_jerk_v105_signal(sps):
    g = _f20_loggrowth(sps, 126)
    stab = _mean(_f20_loggrowth(sps, 21), 252) / _std(_f20_loggrowth(sps, 21), 252).replace(0, np.nan)
    b = np.tanh(g) * np.tanh(stab)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revquality_126d_jerk_v106_signal(revenue):
    g = _f20_loggrowth(revenue, 126)
    stab = _mean(_f20_loggrowth(revenue, 21), 252) / _std(_f20_loggrowth(revenue, 21), 252).replace(0, np.nan)
    b = np.tanh(g) * np.tanh(stab)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_sizerankmom_504d_jerk_v107_signal(revenue):
    r = _rank(_f20_scale(revenue), 504)
    b = r - r.shift(63)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spssizerankmom_504d_jerk_v108_signal(sps):
    r = _rank(_f20_scale(sps), 504)
    b = r - r.shift(63)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsstretch_252d_jerk_v109_signal(sps):
    hi = _rmax(sps, 252)
    raw = np.log(sps.replace(0, np.nan) / hi.replace(0, np.nan))
    b = _z(raw, 126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revstretch_252d_jerk_v110_signal(revenue):
    hi = _rmax(revenue, 252)
    raw = np.log(revenue.replace(0, np.nan) / hi.replace(0, np.nan))
    b = _z(raw, 126)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_scalemom_126d_jerk_v111_signal(sps, revenue):
    sg = np.tanh(3.0 * _f20_loggrowth(sps, 126))
    rg = np.tanh(3.0 * _f20_loggrowth(revenue, 126))
    b = (sg + rg) / 2.0
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_diloverhang_504d_jerk_v112_signal(shareswa):
    b = np.tanh(6.0 * _f20_loggrowth(shareswa, 504))
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_dilstreak_252d_jerk_v113_signal(shareswa):
    g = _f20_loggrowth(shareswa, 63)
    b = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdpsgr_252d_jerk_v114_signal(revenueusd, shareswa):
    ups = _f20_pershare(revenueusd, shareswa)
    b = _rank(_f20_loggrowth(ups, 252), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_psefficrank_504d_jerk_v115_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    rpsg = _f20_loggrowth(rps, 252)
    shg = _f20_loggrowth(shareswa, 252).abs() + 0.01
    b = _rank(rpsg / shg, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_accelfx_504d_jerk_v116_signal(revenue, revenueusd):
    ar = _f20_accel(revenue, 126)
    au = _f20_accel(revenueusd, 126)
    b = _rank(ar - au, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxcontrib_504d_jerk_v117_signal(revenue, revenueusd):
    rg = _f20_loggrowth(revenue, 252)
    ug = _f20_loggrowth(revenueusd, 252)
    b = _rank(rg - ug, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spstopband_504d_jerk_v118_signal(sps):
    hi = _rmax(sps, 504)
    lo = _rmin(sps, 504)
    pos = (sps - lo) / (hi - lo).replace(0, np.nan)
    b = (pos >= 0.9).astype(float).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revcontract_252d_jerk_v119_signal(revenue):
    g = _f20_loggrowth(revenue, 63)
    b = (g < 0).astype(float).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revhifreq_252d_jerk_v120_signal(revenue):
    hi = _rmax(revenue, 252)
    b = (revenue >= hi * 0.99999).astype(float).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spshifreq_252d_jerk_v121_signal(sps):
    hi = _rmax(sps, 252)
    b = (sps >= hi * 0.99999).astype(float).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revpersist_252d_jerk_v122_signal(revenue):
    g = _f20_loggrowth(revenue, 21)
    sg = np.sign(g)
    b = (sg * sg.shift(21)).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spspersist_252d_jerk_v123_signal(sps):
    g = _f20_loggrowth(sps, 21)
    sg = np.sign(g)
    b = (sg * sg.shift(21)).rolling(252, min_periods=126).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_inflectagree_126d_jerk_v124_signal(sps, revenue):
    a1 = np.sign(_f20_accel(sps, 126))
    a2 = np.sign(_f20_accel(revenue, 126))
    b = (a1 * a2).rolling(126, min_periods=42).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_sizecurve_252d_jerk_v125_signal(revenue, sps):
    zr = _z(_f20_scale(revenue), 252)
    zs = _z(_f20_scale(sps), 252)
    b = np.sign(zr) * (zr ** 2) - np.sign(zs) * (zs ** 2)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_cleanprod_126d_jerk_v126_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = np.sign(rg) * np.sqrt(rg.abs()) * (1.0 - np.tanh(10.0 * shg.clip(lower=0)))
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgrtanh_126d_jerk_v127_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = np.tanh(4.0 * (rg - shg)) - np.tanh(4.0 * rg)
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsgrextreme_252d_jerk_v128_signal(sps):
    g = _f20_loggrowth(sps, 252)
    z = _z(g, 252)
    b = np.tanh(z) * z.abs()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_fxgrwedge_126d_jerk_v129_signal(revenue, revenueusd):
    rg = _f20_loggrowth(revenue, 126)
    ug = _f20_loggrowth(revenueusd, 126)
    b = (rg - ug).ewm(span=63, min_periods=21).mean()
    d = _jerk(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_psvssh_504d_jerk_v130_signal(sps, shareswa):
    spsg = _f20_loggrowth(sps, 252)
    shg = _f20_loggrowth(shareswa, 252).abs() + 0.005
    b = _rank(spsg / shg, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spspereff_252d_jerk_v131_signal(sps, shareswa):
    spsg = _f20_loggrowth(sps, 252)
    shg = _f20_loggrowth(shareswa, 252).abs() + 0.01
    b = spsg / shg
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revaccelz_252d_jerk_v132_signal(revenue):
    b = _z(_f20_accel(revenue, 126), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdpsaccel_252d_jerk_v133_signal(revenueusd, shareswa):
    ups = _f20_pershare(revenueusd, shareswa)
    b = _z(_f20_accel(ups, 126), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsaccel252_252d_jerk_v134_signal(sps):
    b = _f20_accel(sps, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revaccel252_252d_jerk_v135_signal(revenue):
    b = _f20_accel(revenue, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsseq21_21d_jerk_v136_signal(sps):
    b = _f20_loggrowth(sps, 21)
    d = _jerk(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revseq21_21d_jerk_v137_signal(revenue):
    b = _f20_loggrowth(revenue, 21)
    d = _jerk(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spscurv_252d_jerk_v138_signal(sps):
    g1 = _f20_loggrowth(sps, 63) * (252.0 / 63.0)
    g2 = _f20_loggrowth(sps, 126) * (252.0 / 126.0)
    g3 = _f20_loggrowth(sps, 252)
    b = g1 - 2.0 * g2 + g3
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revcurv_252d_jerk_v139_signal(revenue):
    g1 = _f20_loggrowth(revenue, 63) * (252.0 / 63.0)
    g2 = _f20_loggrowth(revenue, 126) * (252.0 / 126.0)
    g3 = _f20_loggrowth(revenue, 252)
    b = g1 - 2.0 * g2 + g3
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_scalecomp_252d_jerk_v140_signal(sps):
    g63 = _f20_loggrowth(sps, 63)
    g252 = _f20_loggrowth(sps, 252)
    b = np.tanh(4.0 * g63) - np.tanh(2.0 * g252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_grbal_252d_jerk_v141_signal(revenue, sps):
    b = _z(_f20_loggrowth(revenue, 252) - _f20_loggrowth(sps, 252), 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_cleanscale_504d_jerk_v142_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 252)
    shg = _f20_loggrowth(shareswa, 252)
    b = _rank(rg - 3.0 * shg, 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_usdscale_dt_252d_jerk_v143_signal(revenueusd):
    lu = _f20_scale(revenueusd)
    b = lu - lu.ewm(span=252, min_periods=63).mean()
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revpershare_dt_252d_jerk_v144_signal(revenue, shareswa):
    lrps = _f20_scale(_f20_pershare(revenue, shareswa))
    b = _rank(lrps - _mean(lrps, 252), 504)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsdurable_504d_jerk_v145_signal(sps):
    g = _f20_loggrowth(sps, 63)
    pos = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    b = pos * _mean(g, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spscompound_504d_jerk_v146_signal(sps):
    g = _f20_loggrowth(sps, 63)
    posfrac = (g > 0).astype(float).rolling(504, min_periods=126).mean()
    drift = _mean(g, 504) * (252.0 / 63.0)
    b = (posfrac - 0.5) * drift
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revrecovrate_252d_jerk_v147_signal(revenue):
    lo = _rmin(revenue, 252)
    rec = revenue / lo.replace(0, np.nan) - 1.0
    b = rec - rec.shift(63)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsrecovrate_252d_jerk_v148_signal(sps):
    lo = _rmin(sps, 252)
    rec = sps / lo.replace(0, np.nan) - 1.0
    b = rec - rec.shift(63)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_revjerkbase_252d_jerk_v149_signal(revenue):
    g = _f20_loggrowth(revenue, 126)
    b = _z(g, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f20rs_f20_revenue_scale_per_share_spsjerkbase_252d_jerk_v150_signal(sps):
    g = _f20_loggrowth(sps, 126)
    b = _z(g, 252)
    d = _jerk(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rs_f20_revenue_scale_per_share_spslevel_252d_jerk_v001_signal,
    f20rs_f20_revenue_scale_per_share_spsgr63_63d_jerk_v002_signal,
    f20rs_f20_revenue_scale_per_share_spsgr126_126d_jerk_v003_signal,
    f20rs_f20_revenue_scale_per_share_spsgr252_252d_jerk_v004_signal,
    f20rs_f20_revenue_scale_per_share_revscale_252d_jerk_v005_signal,
    f20rs_f20_revenue_scale_per_share_revgr63_63d_jerk_v006_signal,
    f20rs_f20_revenue_scale_per_share_revgr126_126d_jerk_v007_signal,
    f20rs_f20_revenue_scale_per_share_revgr252_252d_jerk_v008_signal,
    f20rs_f20_revenue_scale_per_share_usdscale_252d_jerk_v009_signal,
    f20rs_f20_revenue_scale_per_share_usdgr252_252d_jerk_v010_signal,
    f20rs_f20_revenue_scale_per_share_rpsscale_252d_jerk_v011_signal,
    f20rs_f20_revenue_scale_per_share_rpsgr126_126d_jerk_v012_signal,
    f20rs_f20_revenue_scale_per_share_rpsgr252_252d_jerk_v013_signal,
    f20rs_f20_revenue_scale_per_share_shscale_252d_jerk_v014_signal,
    f20rs_f20_revenue_scale_per_share_shgr252_252d_jerk_v015_signal,
    f20rs_f20_revenue_scale_per_share_usdpsscale_252d_jerk_v016_signal,
    f20rs_f20_revenue_scale_per_share_fxdiv_126d_jerk_v017_signal,
    f20rs_f20_revenue_scale_per_share_fxgap_126d_jerk_v018_signal,
    f20rs_f20_revenue_scale_per_share_spsz252_252d_jerk_v019_signal,
    f20rs_f20_revenue_scale_per_share_revz252_252d_jerk_v020_signal,
    f20rs_f20_revenue_scale_per_share_spsgrspr_252d_jerk_v021_signal,
    f20rs_f20_revenue_scale_per_share_revgrspr_252d_jerk_v022_signal,
    f20rs_f20_revenue_scale_per_share_spsema_126d_jerk_v023_signal,
    f20rs_f20_revenue_scale_per_share_revema_126d_jerk_v024_signal,
    f20rs_f20_revenue_scale_per_share_spsdd252_252d_jerk_v025_signal,
    f20rs_f20_revenue_scale_per_share_revdd252_252d_jerk_v026_signal,
    f20rs_f20_revenue_scale_per_share_spsrngpos_504d_jerk_v027_signal,
    f20rs_f20_revenue_scale_per_share_revrngpos_504d_jerk_v028_signal,
    f20rs_f20_revenue_scale_per_share_spscagr_504d_jerk_v029_signal,
    f20rs_f20_revenue_scale_per_share_cleaneff_504d_jerk_v030_signal,
    f20rs_f20_revenue_scale_per_share_spsaccel126_126d_jerk_v031_signal,
    f20rs_f20_revenue_scale_per_share_revaccel126_126d_jerk_v032_signal,
    f20rs_f20_revenue_scale_per_share_usdaccel126_126d_jerk_v033_signal,
    f20rs_f20_revenue_scale_per_share_shaccel126_126d_jerk_v034_signal,
    f20rs_f20_revenue_scale_per_share_dildrag_252d_jerk_v035_signal,
    f20rs_f20_revenue_scale_per_share_spsstab_252d_jerk_v036_signal,
    f20rs_f20_revenue_scale_per_share_revstab_252d_jerk_v037_signal,
    f20rs_f20_revenue_scale_per_share_usdstab_252d_jerk_v038_signal,
    f20rs_f20_revenue_scale_per_share_spsgrrank_504d_jerk_v039_signal,
    f20rs_f20_revenue_scale_per_share_revgrrank_504d_jerk_v040_signal,
    f20rs_f20_revenue_scale_per_share_fxz_252d_jerk_v041_signal,
    f20rs_f20_revenue_scale_per_share_usdgrgap_252d_jerk_v042_signal,
    f20rs_f20_revenue_scale_per_share_spsinflect_126d_jerk_v043_signal,
    f20rs_f20_revenue_scale_per_share_revinflect_126d_jerk_v044_signal,
    f20rs_f20_revenue_scale_per_share_spsadv_252d_jerk_v045_signal,
    f20rs_f20_revenue_scale_per_share_rpsz_252d_jerk_v046_signal,
    f20rs_f20_revenue_scale_per_share_spsdisp_126d_jerk_v047_signal,
    f20rs_f20_revenue_scale_per_share_revdisp_126d_jerk_v048_signal,
    f20rs_f20_revenue_scale_per_share_spsslope63_63d_jerk_v049_signal,
    f20rs_f20_revenue_scale_per_share_revslope63_63d_jerk_v050_signal,
    f20rs_f20_revenue_scale_per_share_spsceil_504d_jerk_v051_signal,
    f20rs_f20_revenue_scale_per_share_revfloor_504d_jerk_v052_signal,
    f20rs_f20_revenue_scale_per_share_spsmemory_504d_jerk_v053_signal,
    f20rs_f20_revenue_scale_per_share_revmemory_504d_jerk_v054_signal,
    f20rs_f20_revenue_scale_per_share_revgrvol_252d_jerk_v055_signal,
    f20rs_f20_revenue_scale_per_share_spsgrvol_252d_jerk_v056_signal,
    f20rs_f20_revenue_scale_per_share_sizetier_504d_jerk_v057_signal,
    f20rs_f20_revenue_scale_per_share_spssizetier_504d_jerk_v058_signal,
    f20rs_f20_revenue_scale_per_share_usdscalez_504d_jerk_v059_signal,
    f20rs_f20_revenue_scale_per_share_spsgr504_504d_jerk_v060_signal,
    f20rs_f20_revenue_scale_per_share_spstrendreg_189d_jerk_v061_signal,
    f20rs_f20_revenue_scale_per_share_revtrendreg_189d_jerk_v062_signal,
    f20rs_f20_revenue_scale_per_share_spshalfbal_252d_jerk_v063_signal,
    f20rs_f20_revenue_scale_per_share_revhalfbal_252d_jerk_v064_signal,
    f20rs_f20_revenue_scale_per_share_spseff_252d_jerk_v065_signal,
    f20rs_f20_revenue_scale_per_share_reveff_252d_jerk_v066_signal,
    f20rs_f20_revenue_scale_per_share_spsturb_252d_jerk_v067_signal,
    f20rs_f20_revenue_scale_per_share_revturb_252d_jerk_v068_signal,
    f20rs_f20_revenue_scale_per_share_psleader_504d_jerk_v069_signal,
    f20rs_f20_revenue_scale_per_share_netscale_252d_jerk_v070_signal,
    f20rs_f20_revenue_scale_per_share_cleanps_126d_jerk_v071_signal,
    f20rs_f20_revenue_scale_per_share_rpsriskadj_252d_jerk_v072_signal,
    f20rs_f20_revenue_scale_per_share_revddsm_504d_jerk_v073_signal,
    f20rs_f20_revenue_scale_per_share_spsddsm_504d_jerk_v074_signal,
    f20rs_f20_revenue_scale_per_share_relaccel_63d_jerk_v075_signal,
    f20rs_f20_revenue_scale_per_share_spsrelaccel_126d_jerk_v076_signal,
    f20rs_f20_revenue_scale_per_share_pstension_252d_jerk_v077_signal,
    f20rs_f20_revenue_scale_per_share_fxtrend_126d_jerk_v078_signal,
    f20rs_f20_revenue_scale_per_share_fxrank_504d_jerk_v079_signal,
    f20rs_f20_revenue_scale_per_share_usdgrz_252d_jerk_v080_signal,
    f20rs_f20_revenue_scale_per_share_usdinflect_126d_jerk_v081_signal,
    f20rs_f20_revenue_scale_per_share_spsmom_ema_126d_jerk_v082_signal,
    f20rs_f20_revenue_scale_per_share_revmom_ema_126d_jerk_v083_signal,
    f20rs_f20_revenue_scale_per_share_spsyoychg_252d_jerk_v084_signal,
    f20rs_f20_revenue_scale_per_share_revyoychg_252d_jerk_v085_signal,
    f20rs_f20_revenue_scale_per_share_spsslope126_126d_jerk_v086_signal,
    f20rs_f20_revenue_scale_per_share_revslope126_126d_jerk_v087_signal,
    f20rs_f20_revenue_scale_per_share_rpsheadroom_504d_jerk_v088_signal,
    f20rs_f20_revenue_scale_per_share_usdpsdisp_126d_jerk_v089_signal,
    f20rs_f20_revenue_scale_per_share_fxmag_126d_jerk_v090_signal,
    f20rs_f20_revenue_scale_per_share_spsscalerank_504d_jerk_v091_signal,
    f20rs_f20_revenue_scale_per_share_revscalerank_504d_jerk_v092_signal,
    f20rs_f20_revenue_scale_per_share_spsconvex_252d_jerk_v093_signal,
    f20rs_f20_revenue_scale_per_share_revconvex_252d_jerk_v094_signal,
    f20rs_f20_revenue_scale_per_share_spsspan_252d_jerk_v095_signal,
    f20rs_f20_revenue_scale_per_share_revspan_252d_jerk_v096_signal,
    f20rs_f20_revenue_scale_per_share_spslongrank_504d_jerk_v097_signal,
    f20rs_f20_revenue_scale_per_share_revlongrz_504d_jerk_v098_signal,
    f20rs_f20_revenue_scale_per_share_spsnearpos_252d_jerk_v099_signal,
    f20rs_f20_revenue_scale_per_share_revnearpos_252d_jerk_v100_signal,
    f20rs_f20_revenue_scale_per_share_fxsignmag_126d_jerk_v101_signal,
    f20rs_f20_revenue_scale_per_share_fxlevelwedge_252d_jerk_v102_signal,
    f20rs_f20_revenue_scale_per_share_psratio_504d_jerk_v103_signal,
    f20rs_f20_revenue_scale_per_share_rpsweighted_126d_jerk_v104_signal,
    f20rs_f20_revenue_scale_per_share_spsquality_126d_jerk_v105_signal,
    f20rs_f20_revenue_scale_per_share_revquality_126d_jerk_v106_signal,
    f20rs_f20_revenue_scale_per_share_sizerankmom_504d_jerk_v107_signal,
    f20rs_f20_revenue_scale_per_share_spssizerankmom_504d_jerk_v108_signal,
    f20rs_f20_revenue_scale_per_share_spsstretch_252d_jerk_v109_signal,
    f20rs_f20_revenue_scale_per_share_revstretch_252d_jerk_v110_signal,
    f20rs_f20_revenue_scale_per_share_scalemom_126d_jerk_v111_signal,
    f20rs_f20_revenue_scale_per_share_diloverhang_504d_jerk_v112_signal,
    f20rs_f20_revenue_scale_per_share_dilstreak_252d_jerk_v113_signal,
    f20rs_f20_revenue_scale_per_share_usdpsgr_252d_jerk_v114_signal,
    f20rs_f20_revenue_scale_per_share_psefficrank_504d_jerk_v115_signal,
    f20rs_f20_revenue_scale_per_share_accelfx_504d_jerk_v116_signal,
    f20rs_f20_revenue_scale_per_share_fxcontrib_504d_jerk_v117_signal,
    f20rs_f20_revenue_scale_per_share_spstopband_504d_jerk_v118_signal,
    f20rs_f20_revenue_scale_per_share_revcontract_252d_jerk_v119_signal,
    f20rs_f20_revenue_scale_per_share_revhifreq_252d_jerk_v120_signal,
    f20rs_f20_revenue_scale_per_share_spshifreq_252d_jerk_v121_signal,
    f20rs_f20_revenue_scale_per_share_revpersist_252d_jerk_v122_signal,
    f20rs_f20_revenue_scale_per_share_spspersist_252d_jerk_v123_signal,
    f20rs_f20_revenue_scale_per_share_inflectagree_126d_jerk_v124_signal,
    f20rs_f20_revenue_scale_per_share_sizecurve_252d_jerk_v125_signal,
    f20rs_f20_revenue_scale_per_share_cleanprod_126d_jerk_v126_signal,
    f20rs_f20_revenue_scale_per_share_spsgrtanh_126d_jerk_v127_signal,
    f20rs_f20_revenue_scale_per_share_spsgrextreme_252d_jerk_v128_signal,
    f20rs_f20_revenue_scale_per_share_fxgrwedge_126d_jerk_v129_signal,
    f20rs_f20_revenue_scale_per_share_psvssh_504d_jerk_v130_signal,
    f20rs_f20_revenue_scale_per_share_spspereff_252d_jerk_v131_signal,
    f20rs_f20_revenue_scale_per_share_revaccelz_252d_jerk_v132_signal,
    f20rs_f20_revenue_scale_per_share_usdpsaccel_252d_jerk_v133_signal,
    f20rs_f20_revenue_scale_per_share_spsaccel252_252d_jerk_v134_signal,
    f20rs_f20_revenue_scale_per_share_revaccel252_252d_jerk_v135_signal,
    f20rs_f20_revenue_scale_per_share_spsseq21_21d_jerk_v136_signal,
    f20rs_f20_revenue_scale_per_share_revseq21_21d_jerk_v137_signal,
    f20rs_f20_revenue_scale_per_share_spscurv_252d_jerk_v138_signal,
    f20rs_f20_revenue_scale_per_share_revcurv_252d_jerk_v139_signal,
    f20rs_f20_revenue_scale_per_share_scalecomp_252d_jerk_v140_signal,
    f20rs_f20_revenue_scale_per_share_grbal_252d_jerk_v141_signal,
    f20rs_f20_revenue_scale_per_share_cleanscale_504d_jerk_v142_signal,
    f20rs_f20_revenue_scale_per_share_usdscale_dt_252d_jerk_v143_signal,
    f20rs_f20_revenue_scale_per_share_revpershare_dt_252d_jerk_v144_signal,
    f20rs_f20_revenue_scale_per_share_spsdurable_504d_jerk_v145_signal,
    f20rs_f20_revenue_scale_per_share_spscompound_504d_jerk_v146_signal,
    f20rs_f20_revenue_scale_per_share_revrecovrate_252d_jerk_v147_signal,
    f20rs_f20_revenue_scale_per_share_spsrecovrate_252d_jerk_v148_signal,
    f20rs_f20_revenue_scale_per_share_revjerkbase_252d_jerk_v149_signal,
    f20rs_f20_revenue_scale_per_share_spsjerkbase_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_REVENUE_SCALE_PER_SHARE_REGISTRY_JERK_001_150 = REGISTRY


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

    revenue = _fund(2001, base=2.5e8, drift=0.035, vol=0.08).rename("revenue")
    _rng = np.random.default_rng(2002)
    _fx = 1.0 + 0.18 * np.sin(np.linspace(0, 14, n)) + np.cumsum(_rng.normal(0, 0.006, n))
    _fx = np.clip(_fx, 0.7, 1.5)
    revenueusd = (revenue * _fx).rename("revenueusd")
    shareswa = _fund(2003, base=8e7, drift=0.012, vol=0.02).rename("shareswa")
    sps = _fund(2004, base=3.1, drift=0.03, vol=0.06).rename("sps")

    cols = {"revenue": revenue, "revenueusd": revenueusd,
            "shareswa": shareswa, "sps": sps}

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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
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

    print("OK f20_revenue_scale_per_share_3rd_derivatives_001_150_claude: %d features pass" % n_features)
