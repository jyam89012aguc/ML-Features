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


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _own_pct(totalvalue, marketcap):
    return totalvalue / marketcap.replace(0, np.nan)


def _val_per_holder(totalvalue, shrholders):
    return totalvalue / shrholders.replace(0, np.nan)


def _units_per_holder(shrunits, shrholders):
    return shrunits / shrholders.replace(0, np.nan)


def _impl_price(totalvalue, shrunits):
    return totalvalue / shrunits.replace(0, np.nan)


def _flow(s, w):
    base = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return (s - s.shift(w)) / base.replace(0, np.nan)


def _accum(s, w):
    up = (s.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 3)).mean() - 0.5


def _droc(s, w):
    # discrete derivative: normalized rate of change over window w
    return (s - s.shift(w)) / (s.shift(w).abs() + 1e-9).replace(0, np.nan)


def _ddiff(s, w):
    # simple first difference over window w (for already-bounded/ratio bases)
    return s - s.shift(w)


def f42io_f42_institutional_ownership_flow_ownpct_21d_slope_v001_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = _mean(p, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdgr_21d_slope_v002_signal(shrholders):
    b = _logroc(shrholders, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valgr_63d_slope_v003_signal(totalvalue):
    b = _logroc(totalvalue, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_uniteff_21d_slope_v004_signal(shrunits):
    d = shrunits.diff()
    net = shrunits - shrunits.shift(63)
    gross = d.abs().rolling(63, min_periods=21).sum()
    b = net / gross.replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valgrz_63d_slope_v005_signal(totalvalue):
    g = _logroc(totalvalue, 126)
    b = _z(g, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctmom_21d_slope_v006_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = p - p.shift(63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vph_21d_slope_v007_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    b = _z(vph, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdaccum_21d_slope_v008_signal(shrholders):
    b = _accum(shrholders, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitvbreadth_21d_slope_v009_signal(shrunits, shrholders):
    b = _logroc(shrunits, 63) - _logroc(shrholders, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpx_21d_slope_v010_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    b = _logroc(px, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valflow_21d_slope_v011_signal(totalvalue):
    b = _flow(totalvalue, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalgr_63d_slope_v012_signal(shrvalue):
    b = _logroc(shrvalue, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdrank_21d_slope_v013_signal(shrholders):
    b = _rank(shrholders, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctspr_21d_slope_v014_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = _mean(p, 21) - _mean(p, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_uph_63d_slope_v015_signal(shrunits, shrholders):
    uph = _units_per_holder(shrunits, shrholders)
    b = _logroc(uph, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valflowdisp_21d_slope_v016_signal(totalvalue):
    vol = _flow(totalvalue, 21).rolling(126, min_periods=63).std()
    b = _z(vol, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctdev_63d_slope_v017_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = p - _mean(p, 504)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valaccum_21d_slope_v018_signal(totalvalue):
    b = _accum(totalvalue, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdflowz_21d_slope_v019_signal(shrholders):
    f = _flow(shrholders, 21)
    b = _z(f, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctyoy_63d_slope_v020_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = p / p.shift(252).replace(0, np.nan) - 1.0
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valvbreadth_63d_slope_v021_signal(totalvalue, shrholders):
    b = _logroc(totalvalue, 252) - _logroc(shrholders, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_svtshare_21d_slope_v022_signal(shrvalue, totalvalue):
    sh = shrvalue / totalvalue.replace(0, np.nan)
    b = sh - sh.shift(63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxgap_21d_slope_v023_signal(totalvalue, shrunits, marketcap):
    px = _impl_price(totalvalue, shrunits)
    b = _z(px / marketcap.replace(0, np.nan), 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowaccel_21d_slope_v024_signal(totalvalue):
    b = _flow(totalvalue, 21) - _flow(totalvalue, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdslope_63d_slope_v025_signal(shrholders):
    b = _slope(np.log(shrholders.replace(0, np.nan)), 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitflow_21d_slope_v026_signal(shrunits):
    b = _flow(shrunits, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphacc_21d_slope_v027_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    g = _logroc(vph, 63)
    b = g - g.shift(63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctstd_21d_slope_v028_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = _std(p, 126) / _mean(p, 126).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitaccum_21d_slope_v029_signal(shrunits):
    b = _accum(shrunits, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_dollarflow_21d_slope_v030_signal(totalvalue, marketcap):
    flow = (totalvalue - totalvalue.shift(63)) / marketcap.replace(0, np.nan)
    b = _z(flow, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdgrrank_21d_slope_v031_signal(shrholders):
    g = _logroc(shrholders, 63)
    b = _rank(g, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitz_21d_slope_v032_signal(shrunits):
    b = _z(shrunits, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vwholdflow_21d_slope_v033_signal(shrholders, totalvalue, marketcap):
    hf = _flow(shrholders, 63)
    vf = _flow(totalvalue, 63)
    p = _own_pct(totalvalue, marketcap)
    b = (hf - vf) * np.sign(p - _mean(p, 252))
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxstr_21d_slope_v034_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    b = px / _mean(px, 252).replace(0, np.nan) - 1.0
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctslope_63d_slope_v035_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = _slope(p, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valunitdiv_63d_slope_v036_signal(totalvalue, shrunits):
    b = _logroc(totalvalue, 126) - _logroc(shrunits, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_breadthsize_21d_slope_v037_signal(shrholders, shrunits):
    r = shrholders / shrunits.replace(0, np.nan)
    b = _z(r, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowhit_21d_slope_v038_signal(totalvalue):
    mf = _flow(totalvalue, 21)
    hit = (mf > 0).astype(float)
    b = hit.rolling(252, min_periods=126).mean() - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalslope_21d_slope_v039_signal(shrvalue):
    b = _slope(np.log(shrvalue.replace(0, np.nan)), 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctrank_63d_slope_v040_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = _rank(p, 504)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitflowturb_21d_slope_v041_signal(shrunits):
    vol = _flow(shrunits, 21).rolling(126, min_periods=63).std()
    b = _z(vol, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphvuph_21d_slope_v042_signal(totalvalue, shrunits, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    uph = _units_per_holder(shrunits, shrholders)
    b = _rank(uph, 252) - _rank(vph, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpcthi_21d_slope_v043_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    hi = _rmax(p, 252)
    b = p / hi.replace(0, np.nan) - 1.0
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holddd_21d_slope_v044_signal(shrholders):
    hi = _rmax(shrholders, 252)
    b = shrholders / hi.replace(0, np.nan) - 1.0
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowflip_21d_slope_v045_signal(totalvalue):
    mf = _flow(totalvalue, 21)
    flips = (np.sign(mf) != np.sign(mf.shift(21))).astype(float)
    b = flips.rolling(252, min_periods=126).mean() - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctslacc_21d_slope_v046_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    sl = _slope(p, 63)
    b = sl - sl.shift(63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdmacd_21d_slope_v047_signal(shrholders):
    fast = shrholders.ewm(span=42, min_periods=21).mean()
    slow = shrholders.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitrecov_63d_slope_v048_signal(shrunits):
    lo = _rmin(shrunits, 504)
    b = shrunits / lo.replace(0, np.nan) - 1.0
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valvmcap_21d_slope_v049_signal(totalvalue, marketcap):
    v = _logroc(totalvalue, 21)
    m = _logroc(marketcap, 21)
    outpace = (v > m).astype(float)
    b = outpace.rolling(126, min_periods=63).mean() - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_signedflow_21d_slope_v050_signal(totalvalue, shrholders):
    vf = _flow(totalvalue, 63)
    hsign = np.sign(shrholders.diff(63))
    b = vf * hsign
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphrank_21d_slope_v051_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    b = _rank(vph, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctvov_21d_slope_v052_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    v = _std(p.diff(), 63)
    b = _std(v, 252) / _mean(v, 252).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalaccum_21d_slope_v053_signal(shrvalue):
    b = _accum(shrvalue, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitgryoy_63d_slope_v054_signal(shrunits):
    g = _logroc(shrunits, 252)
    b = g - g.shift(252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_pxvsown_63d_slope_v055_signal(totalvalue, shrunits, marketcap):
    px = _logroc(_impl_price(totalvalue, shrunits), 126)
    own = _logroc(_own_pct(totalvalue, marketcap), 126)
    b = px - own
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdsurge_21d_slope_v056_signal(shrholders):
    hi = _rmax(shrholders, 252)
    raw = shrholders / hi.replace(0, np.nan)
    b = raw.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctbrk504_63d_slope_v057_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    prior_hi = p.shift(1).rolling(504, min_periods=252).max()
    raw = p / prior_hi.replace(0, np.nan) - 1.0
    b = _z(raw, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_uphz_21d_slope_v058_signal(shrunits, shrholders):
    uph = _units_per_holder(shrunits, shrholders)
    b = _z(uph, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valflowema_21d_slope_v059_signal(totalvalue):
    f = _flow(totalvalue, 63)
    b = _rank(f, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_adbal_21d_slope_v060_signal(totalvalue):
    d = totalvalue.diff()
    up = d.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-d.clip(upper=0)).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowagree_21d_slope_v061_signal(shrholders, totalvalue):
    hf = np.sign(shrholders.diff(63))
    vf = np.sign(totalvalue.diff(63))
    b = (hf * vf).rolling(126, min_periods=63).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctcv_21d_slope_v062_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    cv = _std(p, 126) / _mean(p, 126).replace(0, np.nan)
    b = -_z(cv, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitslope126_63d_slope_v063_signal(shrunits):
    b = _slope(np.log(shrunits.replace(0, np.nan)), 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphmr_63d_slope_v064_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    hi = _rmax(vph, 504)
    lo = _rmin(vph, 504)
    b = (vph - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdslvel_21d_slope_v065_signal(shrholders):
    sl = _slope(np.log(shrholders.replace(0, np.nan)), 63)
    b = sl - sl.shift(21)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_broadaccum_21d_slope_v066_signal(totalvalue, shrholders, marketcap):
    vf = _flow(totalvalue, 63)
    hg = _flow(shrholders, 63)
    p = _own_pct(totalvalue, marketcap)
    b = np.sign(vf) * (vf.abs() * hg.abs()) ** 0.5 + 0.1 * p
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctimp_21d_slope_v067_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = p - p.ewm(span=42, min_periods=21).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitvalratio_21d_slope_v068_signal(shrunits, totalvalue):
    b = _flow(shrunits, 63) - 0.5 * _flow(totalvalue, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalrank_21d_slope_v069_signal(shrvalue):
    b = _rank(shrvalue, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctrel_63d_slope_v070_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = (p - p.shift(126)) / _mean(p, 126).replace(0, np.nan)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdexp_21d_slope_v071_signal(shrholders):
    avg = _mean(shrholders, 252)
    above = (shrholders > avg).astype(float)
    entries = ((above == 1) & (above.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + (shrholders / avg.replace(0, np.nan) - 1.0)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowasym_21d_slope_v072_signal(totalvalue):
    mf = _flow(totalvalue, 21)
    up = mf.clip(lower=0).rolling(126, min_periods=63).mean()
    dn = (-mf.clip(upper=0)).rolling(126, min_periods=63).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxpos_63d_slope_v073_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    hi = _rmax(px, 504)
    lo = _rmin(px, 504)
    b = (px - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_multiflow_21d_slope_v074_signal(totalvalue):
    f1 = np.sign(_flow(totalvalue, 21))
    f2 = np.sign(_flow(totalvalue, 63))
    f3 = np.sign(_flow(totalvalue, 126))
    mag = _flow(totalvalue, 63).abs()
    b = (f1 + f2 + f3) / 3.0 * (1.0 + mag)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_qualgrowth_63d_slope_v075_signal(totalvalue, shrholders):
    vg = _logroc(totalvalue, 252)
    hrank = _rank(shrholders, 252) + 0.5
    b = vg * hrank
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctchg21_21d_slope_v076_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = p - p.shift(21)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdgr126_63d_slope_v077_signal(shrholders):
    b = _logroc(shrholders, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valgr126_63d_slope_v078_signal(totalvalue):
    b = _logroc(totalvalue, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitgr252_63d_slope_v079_signal(shrunits):
    b = _logroc(shrunits, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctewm_63d_slope_v080_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = p.ewm(span=63, min_periods=21).mean() - _mean(p, 504)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_uphrank_21d_slope_v081_signal(shrunits, shrholders):
    uph = _units_per_holder(shrunits, shrholders)
    b = _rank(uph, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctaccum_21d_slope_v082_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = _accum(p, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdflowacc_21d_slope_v083_signal(shrholders):
    b = _flow(shrholders, 21) - _flow(shrholders, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxslope_63d_slope_v084_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    b = _slope(np.log(px.replace(0, np.nan)), 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalflow_21d_slope_v085_signal(shrvalue):
    b = _flow(shrvalue, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphstd_21d_slope_v086_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    b = _std(vph, 126) / _mean(vph, 126).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctprox_21d_slope_v087_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    lo = _rmin(p, 252)
    b = p / lo.replace(0, np.nan) - 1.0
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitadbal_21d_slope_v088_signal(shrunits):
    mf = _flow(shrunits, 21)
    flips = (np.sign(mf) != np.sign(mf.shift(21))).astype(float)
    b = flips.rolling(252, min_periods=126).mean() - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdz_21d_slope_v089_signal(shrholders):
    b = _z(shrholders, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valgrstab_21d_slope_v090_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    b = -_std(g, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctmomsm_21d_slope_v091_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    chg = p - p.shift(63)
    b = chg.ewm(span=42, min_periods=21).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitperhold_21d_slope_v092_signal(shrunits, shrholders):
    uf = shrunits.diff(63)
    hf = shrholders.diff(63)
    b = np.tanh(uf / (uf.abs() + hf.abs()).replace(0, np.nan))
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxrank_21d_slope_v093_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    b = _rank(px, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_svtlevel_21d_slope_v094_signal(shrvalue, totalvalue):
    sh = shrvalue / totalvalue.replace(0, np.nan)
    b = _z(sh, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdrecov_63d_slope_v095_signal(shrholders):
    lo = _rmin(shrholders, 504)
    b = shrholders / lo.replace(0, np.nan) - 1.0
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valflowyoy_63d_slope_v096_signal(totalvalue):
    f = _flow(totalvalue, 63)
    b = f - f.shift(252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctdisp_21d_slope_v097_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    m2 = _mean(p, 63)
    b = pd.concat([_mean(p,21), m2, _mean(p,126)], axis=1).std(axis=1) / m2.replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_uphacc_21d_slope_v098_signal(shrunits, shrholders):
    uph = _units_per_holder(shrunits, shrholders)
    f = _flow(uph, 63)
    b = f - f.shift(63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphvspx_21d_slope_v099_signal(totalvalue, shrholders, shrunits):
    vph = _val_per_holder(totalvalue, shrholders)
    px = _impl_price(totalvalue, shrunits)
    b = _rank(vph, 252) - _rank(px, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdslope252_63d_slope_v100_signal(shrholders):
    b = _slope(np.log(shrholders.replace(0, np.nan)), 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctregime_21d_slope_v101_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    med = p.rolling(252, min_periods=126).median()
    above = (p > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitflowz_21d_slope_v102_signal(shrunits):
    f = _flow(shrunits, 63)
    b = _z(f, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_tvshvgap_63d_slope_v103_signal(totalvalue, shrvalue):
    b = _logroc(totalvalue, 126) - _logroc(shrvalue, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctaccel_21d_slope_v104_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holddistr_21d_slope_v105_signal(shrholders):
    q25 = shrholders.rolling(252, min_periods=126).quantile(0.25)
    below = (q25 - shrholders).clip(lower=0) / shrholders.replace(0, np.nan)
    b = below.rolling(63, min_periods=21).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowconc_21d_slope_v106_signal(totalvalue):
    qflow = (totalvalue - totalvalue.shift(63)).abs()
    yflow = totalvalue.diff().abs().rolling(252, min_periods=126).sum()
    b = qflow / yflow.replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownvsunit_63d_slope_v107_signal(totalvalue, marketcap, shrunits):
    op = _logroc(_own_pct(totalvalue, marketcap), 126)
    u = _logroc(shrunits, 126)
    b = op - u
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxgr_63d_slope_v108_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    b = _logroc(px, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_breadthown_21d_slope_v109_signal(totalvalue, marketcap, shrholders):
    p = _own_pct(totalvalue, marketcap)
    hr = _rank(shrholders, 252)
    b = _z(p, 252) + 2.0 * hr
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitpersist_21d_slope_v110_signal(shrunits):
    sgn = np.sign(shrunits.diff(21))
    same = (sgn == sgn.shift(21)).astype(float)
    b = same.rolling(252, min_periods=126).mean() * sgn - 0.5 * sgn
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphslope_21d_slope_v111_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    b = _slope(np.log(vph.replace(0, np.nan)), 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctdd_63d_slope_v112_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    hi = _rmax(p, 504)
    b = p / hi.replace(0, np.nan) - 1.0
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_jointaccum_63d_slope_v113_signal(shrholders, totalvalue):
    hg = _logroc(shrholders, 252)
    vg = _logroc(totalvalue, 252)
    b = np.sign(hg + vg) * (hg.abs() * vg.abs()) ** 0.5
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalrank504_63d_slope_v114_signal(shrvalue):
    b = _rank(shrvalue, 504)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_revalflow_21d_slope_v115_signal(totalvalue, shrunits):
    vf = _z(_flow(totalvalue, 63), 252)
    uf = _z(_flow(shrunits, 63), 252)
    b = vf - uf
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctmomrank_21d_slope_v116_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    mom = p - p.shift(63)
    b = _rank(mom, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_uphgr_63d_slope_v117_signal(shrunits, shrholders):
    uph = _units_per_holder(shrunits, shrholders)
    b = _logroc(uph, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_pressure_21d_slope_v118_signal(totalvalue, marketcap):
    flow = totalvalue.diff(21) / marketcap.replace(0, np.nan)
    b = flow.ewm(span=63, min_periods=21).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdcurv_63d_slope_v119_signal(shrholders):
    b = 2.0 * _logroc(shrholders, 126) - _logroc(shrholders, 252)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctmacd_21d_slope_v120_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    fast = p.ewm(span=42, min_periods=21).mean()
    slow = p.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitasym_21d_slope_v121_signal(shrunits):
    mf = _flow(shrunits, 21)
    up = mf.clip(lower=0).rolling(126, min_periods=63).mean()
    dn = (-mf.clip(upper=0)).rolling(126, min_periods=63).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphvsown_21d_slope_v122_signal(totalvalue, shrholders, marketcap):
    vph = _z(_val_per_holder(totalvalue, shrholders), 252)
    op = _z(_own_pct(totalvalue, marketcap), 252)
    b = vph - op
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdnewhi_21d_slope_v123_signal(shrholders):
    hi = _rmax(shrholders, 252)
    is_hi = (shrholders >= hi * 0.99999).astype(float)
    b = is_hi.rolling(126, min_periods=63).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valimpulse_21d_slope_v124_signal(totalvalue):
    lv = np.log(totalvalue.replace(0, np.nan))
    b = lv - lv.ewm(span=63, min_periods=21).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownholdbuild_21d_slope_v125_signal(totalvalue, marketcap, shrholders):
    op = _own_pct(totalvalue, marketcap).diff(63)
    hsign = np.sign(shrholders.diff(63))
    b = op.abs() * hsign
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxdd_21d_slope_v126_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    hi = _rmax(px, 252)
    b = px / hi.replace(0, np.nan) - 1.0
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_breadthvaldiv_21d_slope_v127_signal(shrholders, totalvalue):
    hf = _z(_flow(shrholders, 63), 252)
    vf = _z(_flow(totalvalue, 63), 252)
    b = hf - vf
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitbuildph_63d_slope_v128_signal(shrunits, shrholders):
    uph = _units_per_holder(shrunits, shrholders)
    b = _accum(uph, 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctsharpe_21d_slope_v129_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    mom = p.diff(63)
    disp = _std(p.diff(), 63)
    b = mom / disp.replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_shrvalslope126_63d_slope_v130_signal(shrvalue):
    b = _slope(np.log(shrvalue.replace(0, np.nan)), 126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_flowhitshift_21d_slope_v131_signal(totalvalue):
    mf = _flow(totalvalue, 21)
    hit = (mf > 0).astype(float)
    b = hit.rolling(126, min_periods=63).mean() - hit.rolling(252, min_periods=126).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitpos_63d_slope_v132_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownvbreadthmom_21d_slope_v133_signal(totalvalue, marketcap, shrholders):
    op = _z(_own_pct(totalvalue, marketcap).diff(63), 252)
    hm = _z(shrholders.diff(63), 252)
    b = op - hm
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphyoy_63d_slope_v134_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    g = _logroc(vph, 126)
    b = g - g.shift(126)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpctbrk252_21d_slope_v135_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    prior_hi = p.shift(1).rolling(252, min_periods=126).max()
    raw = p / prior_hi.replace(0, np.nan) - 1.0
    b = _z(raw, 63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_confirmaccum_21d_slope_v136_signal(shrholders, totalvalue):
    hf = _flow(shrholders, 63)
    vf = _flow(totalvalue, 63)
    b = np.sign(hf) * np.sign(vf) * (hf.abs() + vf.abs())
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitimpulse_21d_slope_v137_signal(shrunits):
    lu = np.log(shrunits.replace(0, np.nan))
    b = lu - lu.ewm(span=42, min_periods=21).mean()
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpcttilt_21d_slope_v138_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    b = (_mean(p, 126) - _mean(p, 252)) / _mean(p, 252).replace(0, np.nan)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_vphaccum_21d_slope_v139_signal(totalvalue, shrholders):
    vph = _val_per_holder(totalvalue, shrholders)
    b = _accum(vph, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdcv_21d_slope_v140_signal(shrholders):
    cv = _std(shrholders, 126) / _mean(shrholders, 126).replace(0, np.nan)
    b = -_z(cv, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_unitflowrank_63d_slope_v141_signal(shrunits):
    f = _flow(shrunits, 63)
    b = _rank(f, 504)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_owncheap_21d_slope_v142_signal(totalvalue, marketcap, shrunits):
    op = _z(_own_pct(totalvalue, marketcap), 252)
    pxz = _z(_impl_price(totalvalue, shrunits), 252)
    b = op - 0.5 * pxz
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_valmcappos_21d_slope_v143_signal(totalvalue, marketcap):
    r = totalvalue / marketcap.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (r - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_holdaccel_21d_slope_v144_signal(shrholders):
    g = _logroc(shrholders, 63)
    b = g - g.shift(63)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_weightedflow_21d_slope_v145_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    flow = _flow(totalvalue, 63)
    b = flow * _rank(p, 252)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_implpxstab_21d_slope_v146_signal(totalvalue, shrunits):
    px = _impl_price(totalvalue, shrunits)
    g = _logroc(px, 21)
    b = -_std(g, 126)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_convtilt_63d_slope_v147_signal(totalvalue, shrholders, shrunits):
    vph = _val_per_holder(totalvalue, shrholders)
    uph = _units_per_holder(shrunits, shrholders)
    b = _rank(vph, 504) - _rank(uph, 504)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_netaccum_21d_slope_v148_signal(totalvalue, shrholders, shrunits):
    vs = np.sign(_flow(totalvalue, 63))
    hs = np.sign(_flow(shrholders, 63))
    us = np.sign(_flow(shrunits, 63))
    mag = _flow(shrunits, 63).abs()
    b = (vs + hs + us) / 3.0 * (1.0 + mag)
    result = (b - b.shift(21)) / float(21)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_ownpcttrendstr_63d_slope_v149_signal(totalvalue, marketcap):
    p = _own_pct(totalvalue, marketcap)
    sl = _slope(p, 252)
    disp = _std(p, 252)
    b = sl * 252.0 / disp.replace(0, np.nan)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


def f42io_f42_institutional_ownership_flow_revalperunit_63d_slope_v150_signal(totalvalue, shrunits):
    vf = totalvalue.diff(252)
    uf = shrunits.diff(252).abs()
    base = _mean(totalvalue, 252)
    b = vf / (uf / _mean(shrunits, 252).replace(0, np.nan) + 0.01).replace(0, np.nan) / base.replace(0, np.nan)
    result = (b - b.shift(63)) / float(63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42io_f42_institutional_ownership_flow_ownpct_21d_slope_v001_signal,
    f42io_f42_institutional_ownership_flow_holdgr_21d_slope_v002_signal,
    f42io_f42_institutional_ownership_flow_valgr_63d_slope_v003_signal,
    f42io_f42_institutional_ownership_flow_uniteff_21d_slope_v004_signal,
    f42io_f42_institutional_ownership_flow_valgrz_63d_slope_v005_signal,
    f42io_f42_institutional_ownership_flow_ownpctmom_21d_slope_v006_signal,
    f42io_f42_institutional_ownership_flow_vph_21d_slope_v007_signal,
    f42io_f42_institutional_ownership_flow_holdaccum_21d_slope_v008_signal,
    f42io_f42_institutional_ownership_flow_unitvbreadth_21d_slope_v009_signal,
    f42io_f42_institutional_ownership_flow_implpx_21d_slope_v010_signal,
    f42io_f42_institutional_ownership_flow_valflow_21d_slope_v011_signal,
    f42io_f42_institutional_ownership_flow_shrvalgr_63d_slope_v012_signal,
    f42io_f42_institutional_ownership_flow_holdrank_21d_slope_v013_signal,
    f42io_f42_institutional_ownership_flow_ownpctspr_21d_slope_v014_signal,
    f42io_f42_institutional_ownership_flow_uph_63d_slope_v015_signal,
    f42io_f42_institutional_ownership_flow_valflowdisp_21d_slope_v016_signal,
    f42io_f42_institutional_ownership_flow_ownpctdev_63d_slope_v017_signal,
    f42io_f42_institutional_ownership_flow_valaccum_21d_slope_v018_signal,
    f42io_f42_institutional_ownership_flow_holdflowz_21d_slope_v019_signal,
    f42io_f42_institutional_ownership_flow_ownpctyoy_63d_slope_v020_signal,
    f42io_f42_institutional_ownership_flow_valvbreadth_63d_slope_v021_signal,
    f42io_f42_institutional_ownership_flow_svtshare_21d_slope_v022_signal,
    f42io_f42_institutional_ownership_flow_implpxgap_21d_slope_v023_signal,
    f42io_f42_institutional_ownership_flow_flowaccel_21d_slope_v024_signal,
    f42io_f42_institutional_ownership_flow_holdslope_63d_slope_v025_signal,
    f42io_f42_institutional_ownership_flow_unitflow_21d_slope_v026_signal,
    f42io_f42_institutional_ownership_flow_vphacc_21d_slope_v027_signal,
    f42io_f42_institutional_ownership_flow_ownpctstd_21d_slope_v028_signal,
    f42io_f42_institutional_ownership_flow_unitaccum_21d_slope_v029_signal,
    f42io_f42_institutional_ownership_flow_dollarflow_21d_slope_v030_signal,
    f42io_f42_institutional_ownership_flow_holdgrrank_21d_slope_v031_signal,
    f42io_f42_institutional_ownership_flow_unitz_21d_slope_v032_signal,
    f42io_f42_institutional_ownership_flow_vwholdflow_21d_slope_v033_signal,
    f42io_f42_institutional_ownership_flow_implpxstr_21d_slope_v034_signal,
    f42io_f42_institutional_ownership_flow_ownpctslope_63d_slope_v035_signal,
    f42io_f42_institutional_ownership_flow_valunitdiv_63d_slope_v036_signal,
    f42io_f42_institutional_ownership_flow_breadthsize_21d_slope_v037_signal,
    f42io_f42_institutional_ownership_flow_flowhit_21d_slope_v038_signal,
    f42io_f42_institutional_ownership_flow_shrvalslope_21d_slope_v039_signal,
    f42io_f42_institutional_ownership_flow_ownpctrank_63d_slope_v040_signal,
    f42io_f42_institutional_ownership_flow_unitflowturb_21d_slope_v041_signal,
    f42io_f42_institutional_ownership_flow_vphvuph_21d_slope_v042_signal,
    f42io_f42_institutional_ownership_flow_ownpcthi_21d_slope_v043_signal,
    f42io_f42_institutional_ownership_flow_holddd_21d_slope_v044_signal,
    f42io_f42_institutional_ownership_flow_flowflip_21d_slope_v045_signal,
    f42io_f42_institutional_ownership_flow_ownpctslacc_21d_slope_v046_signal,
    f42io_f42_institutional_ownership_flow_holdmacd_21d_slope_v047_signal,
    f42io_f42_institutional_ownership_flow_unitrecov_63d_slope_v048_signal,
    f42io_f42_institutional_ownership_flow_valvmcap_21d_slope_v049_signal,
    f42io_f42_institutional_ownership_flow_signedflow_21d_slope_v050_signal,
    f42io_f42_institutional_ownership_flow_vphrank_21d_slope_v051_signal,
    f42io_f42_institutional_ownership_flow_ownpctvov_21d_slope_v052_signal,
    f42io_f42_institutional_ownership_flow_shrvalaccum_21d_slope_v053_signal,
    f42io_f42_institutional_ownership_flow_unitgryoy_63d_slope_v054_signal,
    f42io_f42_institutional_ownership_flow_pxvsown_63d_slope_v055_signal,
    f42io_f42_institutional_ownership_flow_holdsurge_21d_slope_v056_signal,
    f42io_f42_institutional_ownership_flow_ownpctbrk504_63d_slope_v057_signal,
    f42io_f42_institutional_ownership_flow_uphz_21d_slope_v058_signal,
    f42io_f42_institutional_ownership_flow_valflowema_21d_slope_v059_signal,
    f42io_f42_institutional_ownership_flow_adbal_21d_slope_v060_signal,
    f42io_f42_institutional_ownership_flow_flowagree_21d_slope_v061_signal,
    f42io_f42_institutional_ownership_flow_ownpctcv_21d_slope_v062_signal,
    f42io_f42_institutional_ownership_flow_unitslope126_63d_slope_v063_signal,
    f42io_f42_institutional_ownership_flow_vphmr_63d_slope_v064_signal,
    f42io_f42_institutional_ownership_flow_holdslvel_21d_slope_v065_signal,
    f42io_f42_institutional_ownership_flow_broadaccum_21d_slope_v066_signal,
    f42io_f42_institutional_ownership_flow_ownpctimp_21d_slope_v067_signal,
    f42io_f42_institutional_ownership_flow_unitvalratio_21d_slope_v068_signal,
    f42io_f42_institutional_ownership_flow_shrvalrank_21d_slope_v069_signal,
    f42io_f42_institutional_ownership_flow_ownpctrel_63d_slope_v070_signal,
    f42io_f42_institutional_ownership_flow_holdexp_21d_slope_v071_signal,
    f42io_f42_institutional_ownership_flow_flowasym_21d_slope_v072_signal,
    f42io_f42_institutional_ownership_flow_implpxpos_63d_slope_v073_signal,
    f42io_f42_institutional_ownership_flow_multiflow_21d_slope_v074_signal,
    f42io_f42_institutional_ownership_flow_qualgrowth_63d_slope_v075_signal,
    f42io_f42_institutional_ownership_flow_ownpctchg21_21d_slope_v076_signal,
    f42io_f42_institutional_ownership_flow_holdgr126_63d_slope_v077_signal,
    f42io_f42_institutional_ownership_flow_valgr126_63d_slope_v078_signal,
    f42io_f42_institutional_ownership_flow_unitgr252_63d_slope_v079_signal,
    f42io_f42_institutional_ownership_flow_ownpctewm_63d_slope_v080_signal,
    f42io_f42_institutional_ownership_flow_uphrank_21d_slope_v081_signal,
    f42io_f42_institutional_ownership_flow_ownpctaccum_21d_slope_v082_signal,
    f42io_f42_institutional_ownership_flow_holdflowacc_21d_slope_v083_signal,
    f42io_f42_institutional_ownership_flow_implpxslope_63d_slope_v084_signal,
    f42io_f42_institutional_ownership_flow_shrvalflow_21d_slope_v085_signal,
    f42io_f42_institutional_ownership_flow_vphstd_21d_slope_v086_signal,
    f42io_f42_institutional_ownership_flow_ownpctprox_21d_slope_v087_signal,
    f42io_f42_institutional_ownership_flow_unitadbal_21d_slope_v088_signal,
    f42io_f42_institutional_ownership_flow_holdz_21d_slope_v089_signal,
    f42io_f42_institutional_ownership_flow_valgrstab_21d_slope_v090_signal,
    f42io_f42_institutional_ownership_flow_ownpctmomsm_21d_slope_v091_signal,
    f42io_f42_institutional_ownership_flow_unitperhold_21d_slope_v092_signal,
    f42io_f42_institutional_ownership_flow_implpxrank_21d_slope_v093_signal,
    f42io_f42_institutional_ownership_flow_svtlevel_21d_slope_v094_signal,
    f42io_f42_institutional_ownership_flow_holdrecov_63d_slope_v095_signal,
    f42io_f42_institutional_ownership_flow_valflowyoy_63d_slope_v096_signal,
    f42io_f42_institutional_ownership_flow_ownpctdisp_21d_slope_v097_signal,
    f42io_f42_institutional_ownership_flow_uphacc_21d_slope_v098_signal,
    f42io_f42_institutional_ownership_flow_vphvspx_21d_slope_v099_signal,
    f42io_f42_institutional_ownership_flow_holdslope252_63d_slope_v100_signal,
    f42io_f42_institutional_ownership_flow_ownpctregime_21d_slope_v101_signal,
    f42io_f42_institutional_ownership_flow_unitflowz_21d_slope_v102_signal,
    f42io_f42_institutional_ownership_flow_tvshvgap_63d_slope_v103_signal,
    f42io_f42_institutional_ownership_flow_ownpctaccel_21d_slope_v104_signal,
    f42io_f42_institutional_ownership_flow_holddistr_21d_slope_v105_signal,
    f42io_f42_institutional_ownership_flow_flowconc_21d_slope_v106_signal,
    f42io_f42_institutional_ownership_flow_ownvsunit_63d_slope_v107_signal,
    f42io_f42_institutional_ownership_flow_implpxgr_63d_slope_v108_signal,
    f42io_f42_institutional_ownership_flow_breadthown_21d_slope_v109_signal,
    f42io_f42_institutional_ownership_flow_unitpersist_21d_slope_v110_signal,
    f42io_f42_institutional_ownership_flow_vphslope_21d_slope_v111_signal,
    f42io_f42_institutional_ownership_flow_ownpctdd_63d_slope_v112_signal,
    f42io_f42_institutional_ownership_flow_jointaccum_63d_slope_v113_signal,
    f42io_f42_institutional_ownership_flow_shrvalrank504_63d_slope_v114_signal,
    f42io_f42_institutional_ownership_flow_revalflow_21d_slope_v115_signal,
    f42io_f42_institutional_ownership_flow_ownpctmomrank_21d_slope_v116_signal,
    f42io_f42_institutional_ownership_flow_uphgr_63d_slope_v117_signal,
    f42io_f42_institutional_ownership_flow_pressure_21d_slope_v118_signal,
    f42io_f42_institutional_ownership_flow_holdcurv_63d_slope_v119_signal,
    f42io_f42_institutional_ownership_flow_ownpctmacd_21d_slope_v120_signal,
    f42io_f42_institutional_ownership_flow_unitasym_21d_slope_v121_signal,
    f42io_f42_institutional_ownership_flow_vphvsown_21d_slope_v122_signal,
    f42io_f42_institutional_ownership_flow_holdnewhi_21d_slope_v123_signal,
    f42io_f42_institutional_ownership_flow_valimpulse_21d_slope_v124_signal,
    f42io_f42_institutional_ownership_flow_ownholdbuild_21d_slope_v125_signal,
    f42io_f42_institutional_ownership_flow_implpxdd_21d_slope_v126_signal,
    f42io_f42_institutional_ownership_flow_breadthvaldiv_21d_slope_v127_signal,
    f42io_f42_institutional_ownership_flow_unitbuildph_63d_slope_v128_signal,
    f42io_f42_institutional_ownership_flow_ownpctsharpe_21d_slope_v129_signal,
    f42io_f42_institutional_ownership_flow_shrvalslope126_63d_slope_v130_signal,
    f42io_f42_institutional_ownership_flow_flowhitshift_21d_slope_v131_signal,
    f42io_f42_institutional_ownership_flow_unitpos_63d_slope_v132_signal,
    f42io_f42_institutional_ownership_flow_ownvbreadthmom_21d_slope_v133_signal,
    f42io_f42_institutional_ownership_flow_vphyoy_63d_slope_v134_signal,
    f42io_f42_institutional_ownership_flow_ownpctbrk252_21d_slope_v135_signal,
    f42io_f42_institutional_ownership_flow_confirmaccum_21d_slope_v136_signal,
    f42io_f42_institutional_ownership_flow_unitimpulse_21d_slope_v137_signal,
    f42io_f42_institutional_ownership_flow_ownpcttilt_21d_slope_v138_signal,
    f42io_f42_institutional_ownership_flow_vphaccum_21d_slope_v139_signal,
    f42io_f42_institutional_ownership_flow_holdcv_21d_slope_v140_signal,
    f42io_f42_institutional_ownership_flow_unitflowrank_63d_slope_v141_signal,
    f42io_f42_institutional_ownership_flow_owncheap_21d_slope_v142_signal,
    f42io_f42_institutional_ownership_flow_valmcappos_21d_slope_v143_signal,
    f42io_f42_institutional_ownership_flow_holdaccel_21d_slope_v144_signal,
    f42io_f42_institutional_ownership_flow_weightedflow_21d_slope_v145_signal,
    f42io_f42_institutional_ownership_flow_implpxstab_21d_slope_v146_signal,
    f42io_f42_institutional_ownership_flow_convtilt_63d_slope_v147_signal,
    f42io_f42_institutional_ownership_flow_netaccum_21d_slope_v148_signal,
    f42io_f42_institutional_ownership_flow_ownpcttrendstr_63d_slope_v149_signal,
    f42io_f42_institutional_ownership_flow_revalperunit_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_INSTITUTIONAL_OWNERSHIP_FLOW_REGISTRY_001_150 = REGISTRY


def _fund2(seed, base=1e8, drift=0.02, vol=0.05):
    g = np.random.default_rng(seed)
    n = 1500
    qsteps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    trend = np.cumsum(qsteps / 63)
    msteps = np.repeat(g.normal(0.0, vol * 1.6, n // 21 + 1), 21)[:n]
    wobble = np.cumsum(msteps / 21) * 0.55
    s = base * np.exp(trend + wobble)
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    shrholders = _fund2(101, base=350.0, drift=0.015, vol=0.05).rename("shrholders")
    shrunits = _fund2(102, base=5.0e7, drift=0.02, vol=0.07).rename("shrunits")
    totalvalue = _fund2(103, base=8.0e8, drift=0.025, vol=0.08).rename("totalvalue")
    shrvalue = _fund2(104, base=2.0e8, drift=0.02, vol=0.07).rename("shrvalue")
    marketcap = _fund2(105, base=2.0e9, drift=0.02, vol=0.10).rename("marketcap")
    cols = {"shrholders": shrholders, "shrunits": shrunits, "totalvalue": totalvalue, "shrvalue": shrvalue, "marketcap": marketcap}

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

    print("OK f42_institutional_ownership_flow_2nd_derivatives_001_150_claude: %d features pass" % n_features)
