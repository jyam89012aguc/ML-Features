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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logroc(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    # ordinary-least-squares slope of s over a trailing window, per-step
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (institutional ownership flow) =====
def _f42_own_pct(totalvalue, marketcap):
    # institutional ownership fraction of market cap
    return totalvalue / marketcap.replace(0, np.nan)


def _f42_val_per_holder(totalvalue, shrholders):
    # average institutional position value per holder
    return totalvalue / shrholders.replace(0, np.nan)


def _f42_units_per_holder(shrunits, shrholders):
    return shrunits / shrholders.replace(0, np.nan)


def _f42_impl_price(totalvalue, shrunits):
    # implied value per unit held by institutions
    return totalvalue / shrunits.replace(0, np.nan)


def _f42_flow(s, w):
    # normalized flow: change over w scaled by trailing level
    base = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return (s - s.shift(w)) / base.replace(0, np.nan)


def _f42_accum(s, w):
    # accumulation streak: fraction of up-steps over window minus 0.5
    up = (s.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 3)).mean() - 0.5


# ============================================================
# institutional ownership % of market cap (level)
def f42io_f42_institutional_ownership_flow_ownpct_63d_base_v001_signal(totalvalue, marketcap):
    b = _f42_own_pct(totalvalue, marketcap)
    result = _mean(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# inst-holder-count growth over a quarter
def f42io_f42_institutional_ownership_flow_holdgr_63d_base_v002_signal(shrholders):
    b = _logroc(shrholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst-value growth over a year
def f42io_f42_institutional_ownership_flow_valgr_252d_base_v003_signal(totalvalue):
    b = _logroc(totalvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst units accumulation efficiency: net change / sum of |daily changes| over a quarter
def f42io_f42_institutional_ownership_flow_unitslope_63d_base_v004_signal(shrunits):
    d = shrunits.diff()
    net = shrunits - shrunits.shift(63)
    gross = d.abs().rolling(63, min_periods=21).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-value growth z-scored vs its own 252d history
def f42io_f42_institutional_ownership_flow_valgrz_126d_base_v005_signal(totalvalue):
    g = _logroc(totalvalue, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership % momentum (change in ownership fraction over a quarter)
def f42io_f42_institutional_ownership_flow_ownpctmom_63d_base_v006_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = p - p.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder level, z-scored (conviction proxy)
def f42io_f42_institutional_ownership_flow_vph_126d_base_v007_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    b = _z(vph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation: fraction of up-days in holder count over a quarter
def f42io_f42_institutional_ownership_flow_holdaccum_63d_base_v008_signal(shrholders):
    b = _f42_accum(shrholders, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units growth minus holder growth (position-size vs breadth divergence)
def f42io_f42_institutional_ownership_flow_unitvbreadth_63d_base_v009_signal(shrunits, shrholders):
    u = _logroc(shrunits, 63)
    h = _logroc(shrholders, 63)
    b = u - h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied price per unit trend (inst valuation of their position)
def f42io_f42_institutional_ownership_flow_implpx_63d_base_v010_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    b = _logroc(px, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-flow momentum: normalized totalvalue flow over a quarter
def f42io_f42_institutional_ownership_flow_valflow_63d_base_v011_signal(totalvalue):
    b = _f42_flow(totalvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue growth over a half year
def f42io_f42_institutional_ownership_flow_shrvalgr_126d_base_v012_signal(shrvalue):
    b = _logroc(shrvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count percentile-rank vs its own 252d history (breadth extremity)
def f42io_f42_institutional_ownership_flow_holdrank_252d_base_v013_signal(shrholders):
    b = _rank(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership %: 21d vs 252d (short vs long ownership tilt)
def f42io_f42_institutional_ownership_flow_ownpctspr_21v252_base_v014_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = _mean(p, 21) - _mean(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder trend (avg position size in units)
def f42io_f42_institutional_ownership_flow_uph_126d_base_v015_signal(shrunits, shrholders):
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _logroc(uph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-flow dispersion regime: vol of monthly value flow, z-scored (flow turbulence)
def f42io_f42_institutional_ownership_flow_valflowadj_63d_base_v016_signal(totalvalue):
    vol = _f42_flow(totalvalue, 21).rolling(126, min_periods=63).std()
    b = _z(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership % deviation from its 504d mean (mean-reversion gap)
def f42io_f42_institutional_ownership_flow_ownpctdev_504d_base_v017_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = p - _mean(p, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation of total inst value (up-streak fraction over a half year)
def f42io_f42_institutional_ownership_flow_valaccum_126d_base_v018_signal(totalvalue):
    b = _f42_accum(totalvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count flow over a month, z-scored vs its own history
def f42io_f42_institutional_ownership_flow_holdflowz_21d_base_v019_signal(shrholders):
    f = _f42_flow(shrholders, 21)
    b = _z(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value/marketcap relative to value/marketcap one year ago (YoY ownership change)
def f42io_f42_institutional_ownership_flow_ownpctyoy_252d_base_v020_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = p / p.shift(252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value growth minus holder growth (value concentration into fewer/more holders)
def f42io_f42_institutional_ownership_flow_valvbreadth_252d_base_v021_signal(totalvalue, shrholders):
    v = _logroc(totalvalue, 252)
    h = _logroc(shrholders, 252)
    b = v - h
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue vs totalvalue ratio (per-share-class value share) trend
def f42io_f42_institutional_ownership_flow_svtshare_63d_base_v022_signal(shrvalue, totalvalue):
    sh = shrvalue / totalvalue.replace(0, np.nan)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price vs marketcap-implied price gap (inst valuation premium proxy)
def f42io_f42_institutional_ownership_flow_implpxgap_126d_base_v023_signal(totalvalue, shrunits, marketcap):
    px = _f42_impl_price(totalvalue, shrunits)
    b = _z(px / marketcap.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership flow momentum: 21d flow minus 126d flow (acceleration of inflow)
def f42io_f42_institutional_ownership_flow_flowaccel_base_v024_signal(totalvalue):
    f_s = _f42_flow(totalvalue, 21)
    f_l = _f42_flow(totalvalue, 126)
    b = f_s - f_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count OLS slope over a half year (steady breadth build)
def f42io_f42_institutional_ownership_flow_holdslope_126d_base_v025_signal(shrholders):
    b = _slope(np.log(shrholders.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow over a quarter, normalized
def f42io_f42_institutional_ownership_flow_unitflow_63d_base_v026_signal(shrunits):
    b = _f42_flow(shrunits, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder acceleration: 63d growth of vph minus its prior-63d growth
def f42io_f42_institutional_ownership_flow_vphgr_252d_base_v027_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    g = _logroc(vph, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % dispersion (vol of ownership fraction over a half year)
def f42io_f42_institutional_ownership_flow_ownpctstd_126d_base_v028_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = _std(p, 126) / _mean(p, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation of units (up-step fraction over a quarter)
def f42io_f42_institutional_ownership_flow_unitaccum_63d_base_v029_signal(shrunits):
    b = _f42_accum(shrunits, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst dollar-flow pressure relative to its own 252d typical magnitude (z of flow)
def f42io_f42_institutional_ownership_flow_dollarflow_63d_base_v030_signal(totalvalue, marketcap):
    flow = (totalvalue - totalvalue.shift(63)) / marketcap.replace(0, np.nan)
    b = _z(flow, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder growth percentile-ranked vs its own history (breadth momentum extremity)
def f42io_f42_institutional_ownership_flow_holdgrrank_126d_base_v031_signal(shrholders):
    g = _logroc(shrholders, 63)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrunits level z-score (units held extremity)
def f42io_f42_institutional_ownership_flow_unitz_252d_base_v032_signal(shrunits):
    b = _z(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-flow per unit of value-flow (breadth efficiency of inflow)
def f42io_f42_institutional_ownership_flow_vwholdflow_63d_base_v033_signal(shrholders, totalvalue, marketcap):
    hf = _f42_flow(shrholders, 63)
    vf = _f42_flow(totalvalue, 63)
    p = _f42_own_pct(totalvalue, marketcap)
    b = (hf - vf) * np.sign(p - _mean(p, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied price per unit vs its 252d mean (inst cost-basis stretch)
def f42io_f42_institutional_ownership_flow_implpxstr_252d_base_v034_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    b = px / _mean(px, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % OLS slope over a year (steady re-ownership)
def f42io_f42_institutional_ownership_flow_ownpctslope_252d_base_v035_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = _slope(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# divergence: value growing while units flat (price-driven vs share-driven value)
def f42io_f42_institutional_ownership_flow_valunitdiv_126d_base_v036_signal(totalvalue, shrunits):
    v = _logroc(totalvalue, 126)
    u = _logroc(shrunits, 126)
    b = v - u
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-to-size ratio level, z-scored (structural concentration extremity)
def f42io_f42_institutional_ownership_flow_breadthsize_126d_base_v037_signal(shrholders, shrunits):
    r = shrholders / shrunits.replace(0, np.nan)
    b = _z(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow consistency: hit-rate of positive monthly flows over a year
def f42io_f42_institutional_ownership_flow_flowhit_252d_base_v038_signal(totalvalue):
    mf = _f42_flow(totalvalue, 21)
    hit = (mf > 0).astype(float)
    b = hit.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue OLS slope over a quarter
def f42io_f42_institutional_ownership_flow_shrvalslope_63d_base_v039_signal(shrvalue):
    b = _slope(np.log(shrvalue.replace(0, np.nan)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % rank vs its own multi-year history
def f42io_f42_institutional_ownership_flow_ownpctrank_504d_base_v040_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = _rank(p, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-flow turbulence regime: dispersion of monthly units flow, z-scored
def f42io_f42_institutional_ownership_flow_unitflowadj_63d_base_v041_signal(shrunits):
    vol = _f42_flow(shrunits, 21).rolling(126, min_periods=63).std()
    b = _z(vol, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder vs value-per-holder rank gap (size-led vs value-led conviction)
def f42io_f42_institutional_ownership_flow_vphvuph_126d_base_v042_signal(totalvalue, shrunits, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _rank(uph, 252) - _rank(vph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high ownership %: distance to 252d max ownership fraction
def f42io_f42_institutional_ownership_flow_ownpcthi_252d_base_v043_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    hi = _rmax(p, 252)
    b = p / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distribution detection: holder-count drawdown from its 252d peak
def f42io_f42_institutional_ownership_flow_holddd_252d_base_v044_signal(shrholders):
    hi = _rmax(shrholders, 252)
    b = shrholders / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership flow turning point: sign-change density of monthly value flow
def f42io_f42_institutional_ownership_flow_flowtanh_63d_base_v045_signal(totalvalue):
    mf = _f42_flow(totalvalue, 21)
    flips = (np.sign(mf) != np.sign(mf.shift(21))).astype(float)
    b = flips.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % acceleration: 63d slope minus prior 63d slope
def f42io_f42_institutional_ownership_flow_ownpctslacc_base_v046_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    sl = _slope(p, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder breadth curvature: short EMA minus long EMA of holder level (breadth MACD)
def f42io_f42_institutional_ownership_flow_holdgrema_126d_base_v047_signal(shrholders):
    fast = shrholders.ewm(span=42, min_periods=21).mean()
    slow = shrholders.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units accumulation deep: units vs 504d min (rebuild off low base)
def f42io_f42_institutional_ownership_flow_unitrecov_504d_base_v048_signal(shrunits):
    lo = _rmin(shrunits, 504)
    b = shrunits / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value vs market cap divergence streak: fraction of quarter inst value outpaces mcap
def f42io_f42_institutional_ownership_flow_valvmcap_252d_base_v049_signal(totalvalue, marketcap):
    v = _logroc(totalvalue, 21)
    m = _logroc(marketcap, 21)
    outpace = (v > m).astype(float)
    b = outpace.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-flow momentum signed by holder direction (conviction-aligned flow)
def f42io_f42_institutional_ownership_flow_signedflow_63d_base_v050_signal(totalvalue, shrholders):
    vf = _f42_flow(totalvalue, 63)
    hsign = np.sign(shrholders.diff(63))
    b = vf * hsign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder rank vs history (relative conviction extremity)
def f42io_f42_institutional_ownership_flow_vphrank_252d_base_v051_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    b = _rank(vph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % vol-of-vol (regime instability of inst ownership)
def f42io_f42_institutional_ownership_flow_ownpctvov_252d_base_v052_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    v = _std(p.diff(), 63)
    b = _std(v, 252) / _mean(v, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue accumulation streak minus distribution (net up-bias over half year)
def f42io_f42_institutional_ownership_flow_shrvalaccum_126d_base_v053_signal(shrvalue):
    b = _f42_accum(shrvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units growth YoY relative to prior year (units re-acceleration)
def f42io_f42_institutional_ownership_flow_unitgryoy_base_v054_signal(shrunits):
    g = _logroc(shrunits, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price change relative to ownership % change (re-pricing vs re-ownership)
def f42io_f42_institutional_ownership_flow_pxvsown_126d_base_v055_signal(totalvalue, shrunits, marketcap):
    px = _logroc(_f42_impl_price(totalvalue, shrunits), 126)
    own = _logroc(_f42_own_pct(totalvalue, marketcap), 126)
    b = px - own
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count breadth surge: new-holder additions vs 252d peak holder count
def f42io_f42_institutional_ownership_flow_holdsurge_base_v056_signal(shrholders):
    hi = _rmax(shrholders, 252)
    raw = shrholders / hi.replace(0, np.nan)
    b = raw.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % stretch above 504d max (breakout into record inst ownership)
def f42io_f42_institutional_ownership_flow_ownpctbrk_504d_base_v057_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    prior_hi = p.shift(1).rolling(504, min_periods=252).max()
    raw = p / prior_hi.replace(0, np.nan) - 1.0
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder z-score (avg position concentration extremity)
def f42io_f42_institutional_ownership_flow_uphz_252d_base_v058_signal(shrunits, shrholders):
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _z(uph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total value flow over a year, smoothed and de-trended vs slow EMA
def f42io_f42_institutional_ownership_flow_valflowdisp_base_v059_signal(totalvalue):
    f = _f42_flow(totalvalue, 63)
    b = f - f.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation/distribution balance: (up - down value steps) / total over quarter
def f42io_f42_institutional_ownership_flow_adbal_63d_base_v060_signal(totalvalue):
    d = totalvalue.diff()
    up = d.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-d.clip(upper=0)).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count vs value flow agreement (breadth confirms value flow)
def f42io_f42_institutional_ownership_flow_flowagree_63d_base_v061_signal(shrholders, totalvalue):
    hf = np.sign(shrholders.diff(63))
    vf = np.sign(totalvalue.diff(63))
    agree = (hf * vf)
    b = agree.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % stability: inverse coefficient-of-variation of ownership over a half year
def f42io_f42_institutional_ownership_flow_ownpctriskadj_base_v062_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    cv = _std(p, 126) / _mean(p, 126).replace(0, np.nan)
    b = -_z(cv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrunits OLS slope half year (steady unit accumulation)
def f42io_f42_institutional_ownership_flow_unitslope_126d_base_v063_signal(shrunits):
    b = _slope(np.log(shrunits.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder mean reversion: percentile rank of vph within its 504d range
def f42io_f42_institutional_ownership_flow_vphmr_504d_base_v064_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    hi = _rmax(vph, 504)
    lo = _rmin(vph, 504)
    b = (vph - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distribution velocity: how fast holder count is falling (negative slope magnitude)
def f42io_f42_institutional_ownership_flow_holdslvel_63d_base_v065_signal(shrholders):
    sl = _slope(np.log(shrholders.replace(0, np.nan)), 63)
    b = sl - sl.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership flow times holder breadth growth (broad-based accumulation composite)
def f42io_f42_institutional_ownership_flow_broadaccum_63d_base_v066_signal(totalvalue, shrholders, marketcap):
    vf = _f42_flow(totalvalue, 63)
    hg = _f42_flow(shrholders, 63)
    p = _f42_own_pct(totalvalue, marketcap)
    b = np.sign(vf) * (vf.abs() * hg.abs()) ** 0.5 + 0.1 * p
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst value share of marketcap minus its 21d-smoothed self (fast ownership impulse)
def f42io_f42_institutional_ownership_flow_ownpctimp_base_v067_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = p - p.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow vs value flow ratio (organic unit demand vs price-led value)
def f42io_f42_institutional_ownership_flow_unitvalratio_63d_base_v068_signal(shrunits, totalvalue):
    uf = _f42_flow(shrunits, 63)
    vf = _f42_flow(totalvalue, 63)
    b = uf - 0.5 * vf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue rank vs history (per-class value extremity)
def f42io_f42_institutional_ownership_flow_shrvalrank_252d_base_v069_signal(shrvalue):
    b = _rank(shrvalue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % half-year change scaled by its own level (relative ownership build)
def f42io_f42_institutional_ownership_flow_ownpctrel_126d_base_v070_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = (p - p.shift(126)) / _mean(p, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count entries above 252d average (breadth expansion events)
def f42io_f42_institutional_ownership_flow_holdexp_252d_base_v071_signal(shrholders):
    avg = _mean(shrholders, 252)
    above = (shrholders > avg).astype(float)
    entries = ((above == 1) & (above.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + (shrholders / avg.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow asymmetry: upside flow magnitude vs downside flow magnitude
def f42io_f42_institutional_ownership_flow_flowasym_126d_base_v072_signal(totalvalue):
    mf = _f42_flow(totalvalue, 21)
    up = mf.clip(lower=0).rolling(126, min_periods=63).mean()
    dn = (-mf.clip(upper=0)).rolling(126, min_periods=63).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price vs 504d range position (inst cost basis within range)
def f42io_f42_institutional_ownership_flow_implpxpos_504d_base_v073_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    hi = _rmax(px, 504)
    lo = _rmin(px, 504)
    b = (px - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon ownership flow agreement (21/63/126 value flows same sign strength)
def f42io_f42_institutional_ownership_flow_multiflow_base_v074_signal(totalvalue):
    f1 = np.sign(_f42_flow(totalvalue, 21))
    f2 = np.sign(_f42_flow(totalvalue, 63))
    f3 = np.sign(_f42_flow(totalvalue, 126))
    b = (f1 + f2 + f3) / 3.0
    mag = _f42_flow(totalvalue, 63).abs()
    b = b * (1.0 + mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership-value growth funded by breadth: value growth weighted by holder rank
def f42io_f42_institutional_ownership_flow_qualgrowth_252d_base_v075_signal(totalvalue, shrholders):
    vg = _logroc(totalvalue, 252)
    hrank = _rank(shrholders, 252) + 0.5
    b = vg * hrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42io_f42_institutional_ownership_flow_ownpct_63d_base_v001_signal,
    f42io_f42_institutional_ownership_flow_holdgr_63d_base_v002_signal,
    f42io_f42_institutional_ownership_flow_valgr_252d_base_v003_signal,
    f42io_f42_institutional_ownership_flow_unitslope_63d_base_v004_signal,
    f42io_f42_institutional_ownership_flow_valgrz_126d_base_v005_signal,
    f42io_f42_institutional_ownership_flow_ownpctmom_63d_base_v006_signal,
    f42io_f42_institutional_ownership_flow_vph_126d_base_v007_signal,
    f42io_f42_institutional_ownership_flow_holdaccum_63d_base_v008_signal,
    f42io_f42_institutional_ownership_flow_unitvbreadth_63d_base_v009_signal,
    f42io_f42_institutional_ownership_flow_implpx_63d_base_v010_signal,
    f42io_f42_institutional_ownership_flow_valflow_63d_base_v011_signal,
    f42io_f42_institutional_ownership_flow_shrvalgr_126d_base_v012_signal,
    f42io_f42_institutional_ownership_flow_holdrank_252d_base_v013_signal,
    f42io_f42_institutional_ownership_flow_ownpctspr_21v252_base_v014_signal,
    f42io_f42_institutional_ownership_flow_uph_126d_base_v015_signal,
    f42io_f42_institutional_ownership_flow_valflowadj_63d_base_v016_signal,
    f42io_f42_institutional_ownership_flow_ownpctdev_504d_base_v017_signal,
    f42io_f42_institutional_ownership_flow_valaccum_126d_base_v018_signal,
    f42io_f42_institutional_ownership_flow_holdflowz_21d_base_v019_signal,
    f42io_f42_institutional_ownership_flow_ownpctyoy_252d_base_v020_signal,
    f42io_f42_institutional_ownership_flow_valvbreadth_252d_base_v021_signal,
    f42io_f42_institutional_ownership_flow_svtshare_63d_base_v022_signal,
    f42io_f42_institutional_ownership_flow_implpxgap_126d_base_v023_signal,
    f42io_f42_institutional_ownership_flow_flowaccel_base_v024_signal,
    f42io_f42_institutional_ownership_flow_holdslope_126d_base_v025_signal,
    f42io_f42_institutional_ownership_flow_unitflow_63d_base_v026_signal,
    f42io_f42_institutional_ownership_flow_vphgr_252d_base_v027_signal,
    f42io_f42_institutional_ownership_flow_ownpctstd_126d_base_v028_signal,
    f42io_f42_institutional_ownership_flow_unitaccum_63d_base_v029_signal,
    f42io_f42_institutional_ownership_flow_dollarflow_63d_base_v030_signal,
    f42io_f42_institutional_ownership_flow_holdgrrank_126d_base_v031_signal,
    f42io_f42_institutional_ownership_flow_unitz_252d_base_v032_signal,
    f42io_f42_institutional_ownership_flow_vwholdflow_63d_base_v033_signal,
    f42io_f42_institutional_ownership_flow_implpxstr_252d_base_v034_signal,
    f42io_f42_institutional_ownership_flow_ownpctslope_252d_base_v035_signal,
    f42io_f42_institutional_ownership_flow_valunitdiv_126d_base_v036_signal,
    f42io_f42_institutional_ownership_flow_breadthsize_126d_base_v037_signal,
    f42io_f42_institutional_ownership_flow_flowhit_252d_base_v038_signal,
    f42io_f42_institutional_ownership_flow_shrvalslope_63d_base_v039_signal,
    f42io_f42_institutional_ownership_flow_ownpctrank_504d_base_v040_signal,
    f42io_f42_institutional_ownership_flow_unitflowadj_63d_base_v041_signal,
    f42io_f42_institutional_ownership_flow_vphvuph_126d_base_v042_signal,
    f42io_f42_institutional_ownership_flow_ownpcthi_252d_base_v043_signal,
    f42io_f42_institutional_ownership_flow_holddd_252d_base_v044_signal,
    f42io_f42_institutional_ownership_flow_flowtanh_63d_base_v045_signal,
    f42io_f42_institutional_ownership_flow_ownpctslacc_base_v046_signal,
    f42io_f42_institutional_ownership_flow_holdgrema_126d_base_v047_signal,
    f42io_f42_institutional_ownership_flow_unitrecov_504d_base_v048_signal,
    f42io_f42_institutional_ownership_flow_valvmcap_252d_base_v049_signal,
    f42io_f42_institutional_ownership_flow_signedflow_63d_base_v050_signal,
    f42io_f42_institutional_ownership_flow_vphrank_252d_base_v051_signal,
    f42io_f42_institutional_ownership_flow_ownpctvov_252d_base_v052_signal,
    f42io_f42_institutional_ownership_flow_shrvalaccum_126d_base_v053_signal,
    f42io_f42_institutional_ownership_flow_unitgryoy_base_v054_signal,
    f42io_f42_institutional_ownership_flow_pxvsown_126d_base_v055_signal,
    f42io_f42_institutional_ownership_flow_holdsurge_base_v056_signal,
    f42io_f42_institutional_ownership_flow_ownpctbrk_504d_base_v057_signal,
    f42io_f42_institutional_ownership_flow_uphz_252d_base_v058_signal,
    f42io_f42_institutional_ownership_flow_valflowdisp_base_v059_signal,
    f42io_f42_institutional_ownership_flow_adbal_63d_base_v060_signal,
    f42io_f42_institutional_ownership_flow_flowagree_63d_base_v061_signal,
    f42io_f42_institutional_ownership_flow_ownpctriskadj_base_v062_signal,
    f42io_f42_institutional_ownership_flow_unitslope_126d_base_v063_signal,
    f42io_f42_institutional_ownership_flow_vphmr_504d_base_v064_signal,
    f42io_f42_institutional_ownership_flow_holdslvel_63d_base_v065_signal,
    f42io_f42_institutional_ownership_flow_broadaccum_63d_base_v066_signal,
    f42io_f42_institutional_ownership_flow_ownpctimp_base_v067_signal,
    f42io_f42_institutional_ownership_flow_unitvalratio_63d_base_v068_signal,
    f42io_f42_institutional_ownership_flow_shrvalrank_252d_base_v069_signal,
    f42io_f42_institutional_ownership_flow_ownpctrel_126d_base_v070_signal,
    f42io_f42_institutional_ownership_flow_holdexp_252d_base_v071_signal,
    f42io_f42_institutional_ownership_flow_flowasym_126d_base_v072_signal,
    f42io_f42_institutional_ownership_flow_implpxpos_504d_base_v073_signal,
    f42io_f42_institutional_ownership_flow_multiflow_base_v074_signal,
    f42io_f42_institutional_ownership_flow_qualgrowth_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_INSTITUTIONAL_OWNERSHIP_FLOW_REGISTRY_001_075 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


def _fund2(seed, base=1e8, drift=0.02, vol=0.05):
    # quarterly-stepped trend plus an independent monthly-stepped wobble,
    # so long-window trend features carry genuinely independent structure
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
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    shrholders = _fund2(101, base=350.0, drift=0.015, vol=0.05).rename("shrholders")
    shrunits = _fund2(102, base=5.0e7, drift=0.02, vol=0.07).rename("shrunits")
    totalvalue = _fund2(103, base=8.0e8, drift=0.025, vol=0.08).rename("totalvalue")
    shrvalue = _fund2(104, base=2.0e8, drift=0.02, vol=0.07).rename("shrvalue")
    marketcap = _fund2(105, base=2.0e9, drift=0.02, vol=0.10).rename("marketcap")

    cols = {
        "closeadj": closeadj,
        "shrholders": shrholders,
        "shrunits": shrunits,
        "totalvalue": totalvalue,
        "shrvalue": shrvalue,
        "marketcap": marketcap,
    }

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

    print("OK f42_institutional_ownership_flow_base_001_075_claude: %d features pass" % n_features)
