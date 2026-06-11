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
    return totalvalue / marketcap.replace(0, np.nan)


def _f42_val_per_holder(totalvalue, shrholders):
    return totalvalue / shrholders.replace(0, np.nan)


def _f42_units_per_holder(shrunits, shrholders):
    return shrunits / shrholders.replace(0, np.nan)


def _f42_impl_price(totalvalue, shrunits):
    return totalvalue / shrunits.replace(0, np.nan)


def _f42_flow(s, w):
    base = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return (s - s.shift(w)) / base.replace(0, np.nan)


def _f42_accum(s, w):
    up = (s.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(2, w // 3)).mean() - 0.5


# ============================================================
# inst ownership % short trend (21d change of ownership fraction)
def f42io_f42_institutional_ownership_flow_ownpctchg_21d_base_v076_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = p - p.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count growth over a half year (breadth expansion)
def f42io_f42_institutional_ownership_flow_holdgr_126d_base_v077_signal(shrholders):
    b = _logroc(shrholders, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total inst value growth over a half year
def f42io_f42_institutional_ownership_flow_valgr_126d_base_v078_signal(totalvalue):
    b = _logroc(totalvalue, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units growth over a year
def f42io_f42_institutional_ownership_flow_unitgr_252d_base_v079_signal(shrunits):
    b = _logroc(shrunits, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % EWMA level minus 504d mean (persistent ownership tilt)
def f42io_f42_institutional_ownership_flow_ownpctewm_base_v080_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = p.ewm(span=63, min_periods=21).mean() - _mean(p, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder rank vs 252d history (avg position size extremity)
def f42io_f42_institutional_ownership_flow_uphrank_252d_base_v081_signal(shrunits, shrholders):
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _rank(uph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation: up-step fraction of ownership % over a half year
def f42io_f42_institutional_ownership_flow_ownpctaccum_126d_base_v082_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = _f42_accum(p, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-flow momentum: 21d holder flow minus 126d holder flow (breadth acceleration)
def f42io_f42_institutional_ownership_flow_holdflowacc_base_v083_signal(shrholders):
    f_s = _f42_flow(shrholders, 21)
    f_l = _f42_flow(shrholders, 126)
    b = f_s - f_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price (inst cost) OLS slope over a half year
def f42io_f42_institutional_ownership_flow_implpxslope_126d_base_v084_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    b = _slope(np.log(px.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue flow over a quarter, normalized
def f42io_f42_institutional_ownership_flow_shrvalflow_63d_base_v085_signal(shrvalue):
    b = _f42_flow(shrvalue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder dispersion (instability of average conviction)
def f42io_f42_institutional_ownership_flow_vphstd_126d_base_v086_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    b = _std(vph, 126) / _mean(vph, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % vs its 252d max (proximity to record inst ownership)
def f42io_f42_institutional_ownership_flow_ownpctprox_252d_base_v087_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    hi = _rmax(p, 252)
    b = p / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units accumulation streak minus distribution over a quarter (net unit bias)
def f42io_f42_institutional_ownership_flow_unitadbal_63d_base_v088_signal(shrunits):
    d = shrunits.diff()
    up = d.clip(lower=0).rolling(63, min_periods=21).sum()
    dn = (-d.clip(upper=0)).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count z-score (breadth extremity vs own year)
def f42io_f42_institutional_ownership_flow_holdz_252d_base_v089_signal(shrholders):
    b = _z(shrholders, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value growth consistency: std of monthly value growth over a year (lower=steadier)
def f42io_f42_institutional_ownership_flow_valgrstab_252d_base_v090_signal(totalvalue):
    g = _logroc(totalvalue, 21)
    b = -_std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % momentum smoothed (EWMA of quarterly ownpct change)
def f42io_f42_institutional_ownership_flow_ownpctmomsm_base_v091_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    chg = p - p.shift(63)
    b = chg.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow vs holder flow ratio (unit demand per new holder)
def f42io_f42_institutional_ownership_flow_unitperhold_63d_base_v092_signal(shrunits, shrholders):
    uf = shrunits.diff(63)
    hf = shrholders.diff(63)
    b = np.tanh(uf / (uf.abs() + hf.abs()).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price percentile within 252d range (inst cost-basis position)
def f42io_f42_institutional_ownership_flow_implpxrank_252d_base_v093_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    b = _rank(px, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue share of totalvalue level (per-class value weight)
def f42io_f42_institutional_ownership_flow_svtlevel_base_v094_signal(shrvalue, totalvalue):
    sh = shrvalue / totalvalue.replace(0, np.nan)
    b = _z(sh, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder breadth recovery off 504d low (re-broadening base)
def f42io_f42_institutional_ownership_flow_holdrecov_504d_base_v095_signal(shrholders):
    lo = _rmin(shrholders, 504)
    b = shrholders / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow YoY: quarterly value flow minus its level one year ago
def f42io_f42_institutional_ownership_flow_valflowyoy_base_v096_signal(totalvalue):
    f = _f42_flow(totalvalue, 63)
    b = f - f.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % dispersion across horizons (21/63/126 ownpct means disagreement)
def f42io_f42_institutional_ownership_flow_ownpctdisp_base_v097_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    m1 = _mean(p, 21)
    m2 = _mean(p, 63)
    m3 = _mean(p, 126)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1) / m2.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-holder unit build acceleration: 63d units-per-holder flow vs prior 63d
def f42io_f42_institutional_ownership_flow_unitperhold_yoy_base_v098_signal(shrunits, shrholders):
    uph = _f42_units_per_holder(shrunits, shrholders)
    f = _f42_flow(uph, 63)
    b = f - f.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder vs implied-unit-price rank gap (conviction vs revaluation extremity)
def f42io_f42_institutional_ownership_flow_vphvspx_126d_base_v099_signal(totalvalue, shrholders, shrunits):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    px = _f42_impl_price(totalvalue, shrunits)
    b = _rank(vph, 252) - _rank(px, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder-count OLS slope over a year (steady long-run breadth trend)
def f42io_f42_institutional_ownership_flow_holdslope_252d_base_v100_signal(shrholders):
    b = _slope(np.log(shrholders.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % regime: fraction of year above 252d median ownership
def f42io_f42_institutional_ownership_flow_ownpctregime_base_v101_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    med = p.rolling(252, min_periods=126).median()
    above = (p > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow z-scored vs own 252d history (unit-demand extremity)
def f42io_f42_institutional_ownership_flow_unitflowz_63d_base_v102_signal(shrunits):
    f = _f42_flow(shrunits, 63)
    b = _z(f, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total value vs shrvalue growth gap (aggregate vs per-class flow split)
def f42io_f42_institutional_ownership_flow_tvshvgap_126d_base_v103_signal(totalvalue, shrvalue):
    tv = _logroc(totalvalue, 126)
    sv = _logroc(shrvalue, 126)
    b = tv - sv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % acceleration (second difference of ownpct over 63d steps)
def f42io_f42_institutional_ownership_flow_ownpctaccel_base_v104_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distribution flag: holder count below 252d 25th percentile depth
def f42io_f42_institutional_ownership_flow_holddistr_base_v105_signal(shrholders):
    q25 = shrholders.rolling(252, min_periods=126).quantile(0.25)
    below = (q25 - shrholders).clip(lower=0) / shrholders.replace(0, np.nan)
    b = below.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow concentration: |quarterly flow| relative to year-total absolute flows
def f42io_f42_institutional_ownership_flow_flowconc_base_v106_signal(totalvalue):
    qflow = (totalvalue - totalvalue.shift(63)).abs()
    yflow = totalvalue.diff().abs().rolling(252, min_periods=126).sum()
    b = qflow / yflow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % vs units growth (price-driven vs share-driven ownership change)
def f42io_f42_institutional_ownership_flow_ownvsunit_126d_base_v107_signal(totalvalue, marketcap, shrunits):
    op = _logroc(_f42_own_pct(totalvalue, marketcap), 126)
    u = _logroc(shrunits, 126)
    b = op - u
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price growth (inst position revaluation) over a year
def f42io_f42_institutional_ownership_flow_implpxgr_252d_base_v108_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    b = _logroc(px, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-weighted ownership: ownership % times holder-count rank (broad ownership)
def f42io_f42_institutional_ownership_flow_breadthown_base_v109_signal(totalvalue, marketcap, shrholders):
    p = _f42_own_pct(totalvalue, marketcap)
    hr = _rank(shrholders, 252)
    b = _z(p, 252) + 2.0 * hr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow sign persistence (run-length proxy of accumulation)
def f42io_f42_institutional_ownership_flow_unitpersist_base_v110_signal(shrunits):
    sgn = np.sign(shrunits.diff(21))
    same = (sgn == sgn.shift(21)).astype(float)
    b = same.rolling(252, min_periods=126).mean() * sgn - 0.5 * sgn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder OLS slope over a quarter (per-institution conviction trend)
def f42io_f42_institutional_ownership_flow_vphslope_63d_base_v111_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    b = _slope(np.log(vph.replace(0, np.nan)), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % drawdown from 504d peak (inst de-ownership stress)
def f42io_f42_institutional_ownership_flow_ownpctdd_504d_base_v112_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    hi = _rmax(p, 504)
    b = p / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder growth times value growth (joint breadth+value accumulation, signed)
def f42io_f42_institutional_ownership_flow_jointaccum_252d_base_v113_signal(shrholders, totalvalue):
    hg = _logroc(shrholders, 252)
    vg = _logroc(totalvalue, 252)
    b = np.sign(hg + vg) * (hg.abs() * vg.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue percentile vs 504d history (per-class value extremity, long)
def f42io_f42_institutional_ownership_flow_shrvalrank_504d_base_v114_signal(shrvalue):
    b = _rank(shrvalue, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow vs units flow correlation-free spread (revaluation flow component)
def f42io_f42_institutional_ownership_flow_revalflow_63d_base_v115_signal(totalvalue, shrunits):
    vf = _f42_flow(totalvalue, 63)
    uf = _f42_flow(shrunits, 63)
    b = vf - uf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % momentum rank (relative strength of ownership build vs history)
def f42io_f42_institutional_ownership_flow_ownpctmomrank_base_v116_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    mom = p - p.shift(63)
    b = _rank(mom, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units-per-holder change over a year (avg position size growth)
def f42io_f42_institutional_ownership_flow_uphgr_252d_base_v117_signal(shrunits, shrholders):
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _logroc(uph, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst dollar value flow vs market cap, smoothed (sustained ownership pressure)
def f42io_f42_institutional_ownership_flow_pressure_base_v118_signal(totalvalue, marketcap):
    flow = (totalvalue.diff(21)) / marketcap.replace(0, np.nan)
    b = flow.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count half-year change minus year change (breadth momentum curvature)
def f42io_f42_institutional_ownership_flow_holdcurv_base_v119_signal(shrholders):
    g126 = _logroc(shrholders, 126)
    g252 = _logroc(shrholders, 252)
    b = 2.0 * g126 - g252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % short vs long EWMA crossover (ownership MACD)
def f42io_f42_institutional_ownership_flow_ownpctmacd_base_v120_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    fast = p.ewm(span=42, min_periods=21).mean()
    slow = p.ewm(span=126, min_periods=42).mean()
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow asymmetry: up-flow vs down-flow magnitude over a year
def f42io_f42_institutional_ownership_flow_unitasym_base_v121_signal(shrunits):
    mf = _f42_flow(shrunits, 21)
    up = mf.clip(lower=0).rolling(126, min_periods=63).mean()
    dn = (-mf.clip(upper=0)).rolling(126, min_periods=63).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder vs ownership % spread (concentration vs market-relative ownership)
def f42io_f42_institutional_ownership_flow_vphvsown_base_v122_signal(totalvalue, shrholders, marketcap):
    vph = _z(_f42_val_per_holder(totalvalue, shrholders), 252)
    op = _z(_f42_own_pct(totalvalue, marketcap), 252)
    b = vph - op
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-record holder count frequency over a half year (breadth leadership)
def f42io_f42_institutional_ownership_flow_holdnewhi_base_v123_signal(shrholders):
    hi = _rmax(shrholders, 252)
    is_hi = (shrholders >= hi * 0.99999).astype(float)
    b = is_hi.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total value EWMA-detrended impulse (fast ownership value shock)
def f42io_f42_institutional_ownership_flow_valimpulse_base_v124_signal(totalvalue):
    lv = np.log(totalvalue.replace(0, np.nan))
    b = lv - lv.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % per-holder build: ownpct change weighted by holder growth sign
def f42io_f42_institutional_ownership_flow_ownholdbuild_base_v125_signal(totalvalue, marketcap, shrholders):
    op = _f42_own_pct(totalvalue, marketcap).diff(63)
    hsign = np.sign(shrholders.diff(63))
    b = op.abs() * hsign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price drawdown from 252d peak (inst position underwater)
def f42io_f42_institutional_ownership_flow_implpxdd_252d_base_v126_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    hi = _rmax(px, 252)
    b = px / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth-vs-value flow divergence (holders rising while value falling, or vice versa)
def f42io_f42_institutional_ownership_flow_breadthvaldiv_base_v127_signal(shrholders, totalvalue):
    hf = _z(_f42_flow(shrholders, 63), 252)
    vf = _z(_f42_flow(totalvalue, 63), 252)
    b = hf - vf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units accumulation over a half year scaled by holder count (per-holder build)
def f42io_f42_institutional_ownership_flow_unitbuildph_base_v128_signal(shrunits, shrholders):
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _f42_flow(uph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % stability-adjusted momentum (momentum / dispersion)
def f42io_f42_institutional_ownership_flow_ownpctsharpe_base_v129_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    mom = p.diff(63)
    disp = _std(p.diff(), 63)
    b = mom / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shrvalue OLS slope over a half year (per-class value trajectory)
def f42io_f42_institutional_ownership_flow_shrvalslope_126d_base_v130_signal(shrvalue):
    b = _slope(np.log(shrvalue.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value flow hit-rate over a half year minus over a year (flow consistency shift)
def f42io_f42_institutional_ownership_flow_flowhitshift_base_v131_signal(totalvalue):
    mf = _f42_flow(totalvalue, 21)
    hit = (mf > 0).astype(float)
    b = hit.rolling(126, min_periods=63).mean() - hit.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units level vs 504d range position (long-run unit accumulation stage)
def f42io_f42_institutional_ownership_flow_unitpos_504d_base_v132_signal(shrunits):
    hi = _rmax(shrunits, 504)
    lo = _rmin(shrunits, 504)
    b = (shrunits - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % momentum vs holder momentum (value-led vs breadth-led ownership)
def f42io_f42_institutional_ownership_flow_ownvbreadthmom_base_v133_signal(totalvalue, marketcap, shrholders):
    op = _z(_f42_own_pct(totalvalue, marketcap).diff(63), 252)
    hm = _z(shrholders.diff(63), 252)
    b = op - hm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder year-over-year change (deepening conviction YoY)
def f42io_f42_institutional_ownership_flow_vphyoy_base_v134_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    g = _logroc(vph, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inst ownership breakout: ownpct vs prior 252d high, z-scored headroom
def f42io_f42_institutional_ownership_flow_ownpctbrk_252d_base_v135_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    prior_hi = p.shift(1).rolling(252, min_periods=126).max()
    raw = p / prior_hi.replace(0, np.nan) - 1.0
    b = _z(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder flow times value flow agreement (confirmed accumulation strength)
def f42io_f42_institutional_ownership_flow_confirmaccum_base_v136_signal(shrholders, totalvalue):
    hf = _f42_flow(shrholders, 63)
    vf = _f42_flow(totalvalue, 63)
    b = np.sign(hf) * np.sign(vf) * (hf.abs() + vf.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow EWMA-detrended (fast unit demand impulse)
def f42io_f42_institutional_ownership_flow_unitimpulse_base_v137_signal(shrunits):
    lu = np.log(shrunits.replace(0, np.nan))
    b = lu - lu.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % half-year vs full-year mean spread (recent ownership tilt)
def f42io_f42_institutional_ownership_flow_ownpcttilt_base_v138_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    b = (_mean(p, 126) - _mean(p, 252)) / _mean(p, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder accumulation streak (rising conviction frequency)
def f42io_f42_institutional_ownership_flow_vphaccum_126d_base_v139_signal(totalvalue, shrholders):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    b = _f42_accum(vph, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# holder count coefficient of variation (breadth stability, inverse)
def f42io_f42_institutional_ownership_flow_holdcv_base_v140_signal(shrholders):
    cv = _std(shrholders, 126) / _mean(shrholders, 126).replace(0, np.nan)
    b = -_z(cv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# units flow rank vs 504d history (long-run unit-demand percentile)
def f42io_f42_institutional_ownership_flow_unitflowrank_504d_base_v141_signal(shrunits):
    f = _f42_flow(shrunits, 63)
    b = _rank(f, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % vs implied-price level interaction (cheap-yet-owned proxy)
def f42io_f42_institutional_ownership_flow_owncheap_base_v142_signal(totalvalue, marketcap, shrunits):
    op = _z(_f42_own_pct(totalvalue, marketcap), 252)
    pxz = _z(_f42_impl_price(totalvalue, shrunits), 252)
    b = op - 0.5 * pxz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total value vs marketcap range position (inst value vs price cycle stage)
def f42io_f42_institutional_ownership_flow_valmcappos_base_v143_signal(totalvalue, marketcap):
    r = totalvalue / marketcap.replace(0, np.nan)
    hi = _rmax(r, 252)
    lo = _rmin(r, 252)
    b = (r - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breadth acceleration: holder count second difference over quarterly steps
def f42io_f42_institutional_ownership_flow_holdaccel_base_v144_signal(shrholders):
    g = _logroc(shrholders, 63)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership flow momentum scaled by ownership level (weighted inflow intensity)
def f42io_f42_institutional_ownership_flow_weightedflow_base_v145_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    flow = _f42_flow(totalvalue, 63)
    b = flow * _rank(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied unit price stability (inverse vol of unit price over a half year)
def f42io_f42_institutional_ownership_flow_implpxstab_base_v146_signal(totalvalue, shrunits):
    px = _f42_impl_price(totalvalue, shrunits)
    g = _logroc(px, 21)
    b = -_std(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-holder vs units-per-holder rank spread (value- vs size-conviction tilt)
def f42io_f42_institutional_ownership_flow_convtilt_base_v147_signal(totalvalue, shrholders, shrunits):
    vph = _f42_val_per_holder(totalvalue, shrholders)
    uph = _f42_units_per_holder(shrunits, shrholders)
    b = _rank(vph, 504) - _rank(uph, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net ownership accumulation composite: value-flow + breadth-flow + unit-flow signs
def f42io_f42_institutional_ownership_flow_netaccum_base_v148_signal(totalvalue, shrholders, shrunits):
    vs = np.sign(_f42_flow(totalvalue, 63))
    hs = np.sign(_f42_flow(shrholders, 63))
    us = np.sign(_f42_flow(shrunits, 63))
    mag = _f42_flow(shrunits, 63).abs()
    b = (vs + hs + us) / 3.0 * (1.0 + mag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ownership % long-run trend strength: 252d slope per unit of ownpct dispersion
def f42io_f42_institutional_ownership_flow_ownpcttrendstr_base_v149_signal(totalvalue, marketcap):
    p = _f42_own_pct(totalvalue, marketcap)
    sl = _slope(p, 252)
    disp = _std(p, 252)
    b = sl * 252.0 / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total value flow over a year normalized by units flow (revaluation-per-unit-flow)
def f42io_f42_institutional_ownership_flow_revalperunit_base_v150_signal(totalvalue, shrunits):
    vf = totalvalue.diff(252)
    uf = shrunits.diff(252).abs()
    base = _mean(totalvalue, 252)
    b = vf / (uf / _mean(shrunits, 252).replace(0, np.nan) + 0.01).replace(0, np.nan) / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f42io_f42_institutional_ownership_flow_ownpctchg_21d_base_v076_signal,
    f42io_f42_institutional_ownership_flow_holdgr_126d_base_v077_signal,
    f42io_f42_institutional_ownership_flow_valgr_126d_base_v078_signal,
    f42io_f42_institutional_ownership_flow_unitgr_252d_base_v079_signal,
    f42io_f42_institutional_ownership_flow_ownpctewm_base_v080_signal,
    f42io_f42_institutional_ownership_flow_uphrank_252d_base_v081_signal,
    f42io_f42_institutional_ownership_flow_ownpctaccum_126d_base_v082_signal,
    f42io_f42_institutional_ownership_flow_holdflowacc_base_v083_signal,
    f42io_f42_institutional_ownership_flow_implpxslope_126d_base_v084_signal,
    f42io_f42_institutional_ownership_flow_shrvalflow_63d_base_v085_signal,
    f42io_f42_institutional_ownership_flow_vphstd_126d_base_v086_signal,
    f42io_f42_institutional_ownership_flow_ownpctprox_252d_base_v087_signal,
    f42io_f42_institutional_ownership_flow_unitadbal_63d_base_v088_signal,
    f42io_f42_institutional_ownership_flow_holdz_252d_base_v089_signal,
    f42io_f42_institutional_ownership_flow_valgrstab_252d_base_v090_signal,
    f42io_f42_institutional_ownership_flow_ownpctmomsm_base_v091_signal,
    f42io_f42_institutional_ownership_flow_unitperhold_63d_base_v092_signal,
    f42io_f42_institutional_ownership_flow_implpxrank_252d_base_v093_signal,
    f42io_f42_institutional_ownership_flow_svtlevel_base_v094_signal,
    f42io_f42_institutional_ownership_flow_holdrecov_504d_base_v095_signal,
    f42io_f42_institutional_ownership_flow_valflowyoy_base_v096_signal,
    f42io_f42_institutional_ownership_flow_ownpctdisp_base_v097_signal,
    f42io_f42_institutional_ownership_flow_unitperhold_yoy_base_v098_signal,
    f42io_f42_institutional_ownership_flow_vphvspx_126d_base_v099_signal,
    f42io_f42_institutional_ownership_flow_holdslope_252d_base_v100_signal,
    f42io_f42_institutional_ownership_flow_ownpctregime_base_v101_signal,
    f42io_f42_institutional_ownership_flow_unitflowz_63d_base_v102_signal,
    f42io_f42_institutional_ownership_flow_tvshvgap_126d_base_v103_signal,
    f42io_f42_institutional_ownership_flow_ownpctaccel_base_v104_signal,
    f42io_f42_institutional_ownership_flow_holddistr_base_v105_signal,
    f42io_f42_institutional_ownership_flow_flowconc_base_v106_signal,
    f42io_f42_institutional_ownership_flow_ownvsunit_126d_base_v107_signal,
    f42io_f42_institutional_ownership_flow_implpxgr_252d_base_v108_signal,
    f42io_f42_institutional_ownership_flow_breadthown_base_v109_signal,
    f42io_f42_institutional_ownership_flow_unitpersist_base_v110_signal,
    f42io_f42_institutional_ownership_flow_vphslope_63d_base_v111_signal,
    f42io_f42_institutional_ownership_flow_ownpctdd_504d_base_v112_signal,
    f42io_f42_institutional_ownership_flow_jointaccum_252d_base_v113_signal,
    f42io_f42_institutional_ownership_flow_shrvalrank_504d_base_v114_signal,
    f42io_f42_institutional_ownership_flow_revalflow_63d_base_v115_signal,
    f42io_f42_institutional_ownership_flow_ownpctmomrank_base_v116_signal,
    f42io_f42_institutional_ownership_flow_uphgr_252d_base_v117_signal,
    f42io_f42_institutional_ownership_flow_pressure_base_v118_signal,
    f42io_f42_institutional_ownership_flow_holdcurv_base_v119_signal,
    f42io_f42_institutional_ownership_flow_ownpctmacd_base_v120_signal,
    f42io_f42_institutional_ownership_flow_unitasym_base_v121_signal,
    f42io_f42_institutional_ownership_flow_vphvsown_base_v122_signal,
    f42io_f42_institutional_ownership_flow_holdnewhi_base_v123_signal,
    f42io_f42_institutional_ownership_flow_valimpulse_base_v124_signal,
    f42io_f42_institutional_ownership_flow_ownholdbuild_base_v125_signal,
    f42io_f42_institutional_ownership_flow_implpxdd_252d_base_v126_signal,
    f42io_f42_institutional_ownership_flow_breadthvaldiv_base_v127_signal,
    f42io_f42_institutional_ownership_flow_unitbuildph_base_v128_signal,
    f42io_f42_institutional_ownership_flow_ownpctsharpe_base_v129_signal,
    f42io_f42_institutional_ownership_flow_shrvalslope_126d_base_v130_signal,
    f42io_f42_institutional_ownership_flow_flowhitshift_base_v131_signal,
    f42io_f42_institutional_ownership_flow_unitpos_504d_base_v132_signal,
    f42io_f42_institutional_ownership_flow_ownvbreadthmom_base_v133_signal,
    f42io_f42_institutional_ownership_flow_vphyoy_base_v134_signal,
    f42io_f42_institutional_ownership_flow_ownpctbrk_252d_base_v135_signal,
    f42io_f42_institutional_ownership_flow_confirmaccum_base_v136_signal,
    f42io_f42_institutional_ownership_flow_unitimpulse_base_v137_signal,
    f42io_f42_institutional_ownership_flow_ownpcttilt_base_v138_signal,
    f42io_f42_institutional_ownership_flow_vphaccum_126d_base_v139_signal,
    f42io_f42_institutional_ownership_flow_holdcv_base_v140_signal,
    f42io_f42_institutional_ownership_flow_unitflowrank_504d_base_v141_signal,
    f42io_f42_institutional_ownership_flow_owncheap_base_v142_signal,
    f42io_f42_institutional_ownership_flow_valmcappos_base_v143_signal,
    f42io_f42_institutional_ownership_flow_holdaccel_base_v144_signal,
    f42io_f42_institutional_ownership_flow_weightedflow_base_v145_signal,
    f42io_f42_institutional_ownership_flow_implpxstab_base_v146_signal,
    f42io_f42_institutional_ownership_flow_convtilt_base_v147_signal,
    f42io_f42_institutional_ownership_flow_netaccum_base_v148_signal,
    f42io_f42_institutional_ownership_flow_ownpcttrendstr_base_v149_signal,
    f42io_f42_institutional_ownership_flow_revalperunit_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F42_INSTITUTIONAL_OWNERSHIP_FLOW_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    n = 1500
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


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

    print("OK f42_institutional_ownership_flow_base_076_150_claude: %d features pass" % n_features)
