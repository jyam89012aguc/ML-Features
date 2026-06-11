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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (margin TRAJECTORY) =====
def _f24_slope(s, w):
    def _f(a):
        m = len(a)
        x = np.arange(m, dtype=float)
        x = x - x.mean()
        denom = (x ** 2).sum()
        if denom == 0.0:
            return np.nan
        return float(np.dot(x, a) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


def _f24_emaslope(s, span):
    # difference between a fast and slow EMA (smooth directional trajectory)
    fast = s.ewm(span=span, min_periods=max(2, span // 2)).mean()
    slow = s.ewm(span=span * 3, min_periods=max(2, span)).mean()
    return fast - slow


def _f24_chg(s, w):
    return s - s.shift(w)


def _f24_stab(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return m.abs() / sd.replace(0, np.nan)


def _f24_streak(s):
    d = np.sign(s.diff())
    out = np.zeros(len(s), dtype=float)
    run = 0.0
    prev = 0.0
    vals = d.values
    for i in range(len(vals)):
        v = vals[i]
        if np.isnan(v):
            out[i] = np.nan
            run = 0.0
            prev = 0.0
            continue
        if v == prev and v != 0.0:
            run += v
        else:
            run = v
        prev = v
        out[i] = run
    return pd.Series(out, index=s.index)


def _f24_curv(s, w):
    # discrete curvature: forward minus backward half-window change
    return (s - s.shift(w)) - (s.shift(w) - s.shift(2 * w))


# ============================================================
# gross-margin EMA-slope (smooth directional trajectory, quarterly span)
def f24mt_f24_margin_trajectory_gmemaslope_63d_base_v076_signal(grossmargin):
    b = _f24_emaslope(grossmargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin EMA-slope (monthly span)
def f24mt_f24_margin_trajectory_nmemaslope_21d_base_v077_signal(netmargin):
    b = _f24_emaslope(netmargin, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin EMA-slope (half-year span)
def f24mt_f24_margin_trajectory_ememaslope_126d_base_v078_signal(ebitdamargin):
    b = _f24_emaslope(ebitdamargin, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin EMA-slope normalized by level
def f24mt_f24_margin_trajectory_omemaslope_63d_base_v079_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    es = _f24_emaslope(om, 21)
    b = es / _mean(om, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin curvature over a quarter (convex vs concave trajectory)
def f24mt_f24_margin_trajectory_gmcurv_63d_base_v080_signal(grossmargin):
    b = _f24_curv(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin curvature over a half-year
def f24mt_f24_margin_trajectory_nmcurv2_126d_base_v081_signal(netmargin):
    b = _f24_curv(netmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin curvature over a quarter, normalized by dispersion
def f24mt_f24_margin_trajectory_emcurv_63d_base_v082_signal(ebitdamargin):
    cv = _f24_curv(ebitdamargin, 63)
    b = cv / _std(ebitdamargin, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin curvature over a half-year
def f24mt_f24_margin_trajectory_omcurv_126d_base_v083_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    b = _f24_curv(om, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend strength: |slope| ranked cross-time (conviction percentile)
def f24mt_f24_margin_trajectory_gmtrendstr_126d_base_v084_signal(grossmargin):
    sl = _f24_slope(grossmargin, 126).abs()
    b = _rank(sl, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin signed trend magnitude (sign x sqrt of |slope|, compressed)
def f24mt_f24_margin_trajectory_nmsignmag_126d_base_v085_signal(netmargin):
    sl = _f24_slope(netmargin, 126)
    b = np.sign(sl) * sl.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trend interacted with revenue trend (joint expansion composite)
def f24mt_f24_margin_trajectory_emrevtrend_126d_base_v086_signal(ebitdamargin, revenue):
    em_sl = _f24_slope(ebitdamargin, 126)
    rev_sl = _f24_slope(np.log(revenue.replace(0, np.nan)), 126)
    b = em_sl * np.sign(rev_sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-net spread EMA-slope (cost-leverage smooth trajectory)
def f24mt_f24_margin_trajectory_gnspremaslope_base_v087_signal(grossmargin, netmargin):
    spr = grossmargin - netmargin
    b = _f24_emaslope(spr, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-ebitda spread curvature (SG&A absorption bend)
def f24mt_f24_margin_trajectory_gecurv_126d_base_v088_signal(grossmargin, ebitdamargin):
    spr = grossmargin - ebitdamargin
    b = _f24_curv(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-minus-net spread stability (tax/interest predictability)
def f24mt_f24_margin_trajectory_enstab_252d_base_v089_signal(ebitdamargin, netmargin):
    spr = ebitdamargin - netmargin
    b = _f24_stab(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-net margin pass-through ratio trend (how much GM reaches the bottom line)
def f24mt_f24_margin_trajectory_passthru_252d_base_v090_signal(grossmargin, netmargin):
    ratio = netmargin / grossmargin.replace(0, np.nan)
    b = _f24_slope(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-to-ebitda margin pass-through level z-scored (below-the-line efficiency)
def f24mt_f24_margin_trajectory_nepass_252d_base_v091_signal(netmargin, ebitdamargin):
    ratio = netmargin / ebitdamargin.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-trajectory agreement: count of margins above their own 252d baseline (smoothed)
def f24mt_f24_margin_trajectory_baseagree_252d_base_v092_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    a = (grossmargin > _mean(grossmargin, 252)).astype(float)
    b2 = (netmargin > _mean(netmargin, 252)).astype(float)
    c = (ebitdamargin > _mean(ebitdamargin, 252)).astype(float)
    d = (om > _mean(om, 252)).astype(float)
    frac = (a + b2 + c + d) / 4.0
    b = frac.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# margin-trend cross-sectional max minus min (best vs worst trajectory dispersion)
def f24mt_f24_margin_trajectory_trendrange_126d_base_v093_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    g = _f24_slope(grossmargin, 126)
    nn = _f24_slope(netmargin, 126)
    e = _f24_slope(ebitdamargin, 126)
    o = _f24_slope(om, 126)
    stk = pd.concat([g, nn, e, o], axis=1)
    b = stk.max(axis=1) - stk.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin expansion streak ranked cross-time (relative persistence)
def f24mt_f24_margin_trajectory_gmstreakrank_base_v094_signal(grossmargin):
    st = _f24_streak(grossmargin)
    b = _rank(st, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin downside-run severity: cumulative negative streak weighted by magnitude
def f24mt_f24_margin_trajectory_nmdownrun_base_v095_signal(netmargin):
    st = _f24_streak(netmargin)
    down = st.where(st < 0, 0.0)
    b = down * netmargin.diff().abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin acceleration: EMA-slope now minus EMA-slope a quarter ago
def f24mt_f24_margin_trajectory_emaccel_63d_base_v096_signal(ebitdamargin):
    es = _f24_emaslope(ebitdamargin, 21)
    b = es - es.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin acceleration via slope difference of two windows
def f24mt_f24_margin_trajectory_omaccel_base_v097_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    s = _f24_slope(om, 63)
    l = _f24_slope(om, 189)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory vs its 1-year-ago trajectory (slope YoY)
def f24mt_f24_margin_trajectory_gmslopeyoy_base_v098_signal(grossmargin):
    sl = _f24_slope(grossmargin, 126)
    b = sl - sl.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin recent pace vs long pace ratio (acceleration regime, bounded)
def f24mt_f24_margin_trajectory_nmpacespr_base_v099_signal(netmargin):
    short = _f24_chg(netmargin, 63) / 63.0
    long = _f24_chg(netmargin, 252) / 252.0
    b = np.tanh(short / long.replace(0, np.nan)) * np.sign(long)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin level x trend sign (profitable-and-improving composite)
def f24mt_f24_margin_trajectory_emlevdir_126d_base_v100_signal(ebitdamargin):
    lev = _mean(ebitdamargin, 63)
    sl = _f24_slope(ebitdamargin, 126)
    b = lev * np.tanh(40.0 * sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin range position within its own 252d band (cyclical position)
def f24mt_f24_margin_trajectory_omrngpos_252d_base_v101_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    hi = om.rolling(252, min_periods=63).max()
    lo = om.rolling(252, min_periods=63).min()
    b = (om - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin distance below trailing peak ranked (compression severity percentile)
def f24mt_f24_margin_trajectory_gmcomprank_252d_base_v102_signal(grossmargin):
    pk = grossmargin.rolling(252, min_periods=63).max()
    comp = grossmargin / pk.replace(0, np.nan) - 1.0
    b = _rank(comp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin recovery off trough scaled by time-in-recovery
def f24mt_f24_margin_trajectory_nmrecovrate_252d_base_v103_signal(netmargin):
    tr = netmargin.rolling(252, min_periods=63).min()
    rec = netmargin - tr
    # days since trough within the window, approximated by argmin position
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    dsl = netmargin.rolling(252, min_periods=63).apply(_dsl, raw=True).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory z relative to its 504d mean (long de-trended level)
def f24mt_f24_margin_trajectory_emz_504d_base_v104_signal(ebitdamargin):
    b = _z(ebitdamargin, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin EMA-displacement ranked cross-time (relative expansion percentile)
def f24mt_f24_margin_trajectory_gmdisprank_base_v105_signal(grossmargin):
    disp = grossmargin - grossmargin.ewm(span=126, min_periods=63).mean()
    b = _rank(disp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory volatility-of-volatility (regime instability of margins)
def f24mt_f24_margin_trajectory_nmvov_252d_base_v106_signal(netmargin):
    v = _std(netmargin.diff(), 63)
    b = _std(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trend per unit of its trajectory volatility (information ratio)
def f24mt_f24_margin_trajectory_emir_252d_base_v107_signal(ebitdamargin):
    sl = _f24_slope(ebitdamargin, 252)
    vol = _std(ebitdamargin.diff(), 252)
    b = sl / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin direction persistence: lag-1 autocorrelation of margin changes (trend memory)
def f24mt_f24_margin_trajectory_omsignpersist_63d_base_v108_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    d = om.diff()
    b = d.rolling(126, min_periods=42).corr(d.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-net spread range position (cost-structure cyclical position)
def f24mt_f24_margin_trajectory_gnsprrngpos_504d_base_v109_signal(grossmargin, netmargin):
    spr = grossmargin - netmargin
    hi = spr.rolling(504, min_periods=126).max()
    lo = spr.rolling(504, min_periods=126).min()
    b = (spr - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory above its own trailing median: durable above-trend fraction
def f24mt_f24_margin_trajectory_nmprofitfrac_252d_base_v110_signal(netmargin):
    med = netmargin.rolling(252, min_periods=63).median()
    above = (netmargin > med).astype(float)
    raw = above.rolling(126, min_periods=42).mean() - 0.5
    b = raw + 0.25 * (netmargin - med) / _std(netmargin, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin expansion concentration: max single-quarter change over the year
def f24mt_f24_margin_trajectory_emmaxchg_252d_base_v111_signal(ebitdamargin):
    c = _f24_chg(ebitdamargin, 63)
    b = c.rolling(252, min_periods=63).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin worst-quarter contraction over the year (downside trajectory extreme)
def f24mt_f24_margin_trajectory_gmminchg_252d_base_v112_signal(grossmargin):
    c = _f24_chg(grossmargin, 63)
    b = c.rolling(252, min_periods=63).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trajectory skewness of changes (asymmetry of expansions)
def f24mt_f24_margin_trajectory_omchgskew_252d_base_v113_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    d = om.diff()
    b = d.rolling(252, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory kurtosis of changes (fat-tailed margin shocks)
def f24mt_f24_margin_trajectory_nmchgkurt_252d_base_v114_signal(netmargin):
    d = netmargin.diff()
    b = d.rolling(252, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin slope sign-weighted by stability (trusted trajectory)
def f24mt_f24_margin_trajectory_gmtrusttrend_126d_base_v115_signal(grossmargin):
    sl = _f24_slope(grossmargin, 126)
    stab = _f24_stab(grossmargin, 126)
    b = np.sign(sl) * np.log1p(stab.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-vs-gross conversion (operating efficiency) trend
def f24mt_f24_margin_trajectory_egconv_126d_base_v116_signal(ebitdamargin, grossmargin):
    conv = ebitdamargin / grossmargin.replace(0, np.nan)
    b = _f24_slope(conv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin from opinc/revenue minus ebitda-margin spread trend (D&A drift)
def f24mt_f24_margin_trajectory_omemspr_126d_base_v117_signal(opinc, revenue, ebitdamargin):
    om = opinc / revenue.replace(0, np.nan)
    spr = om - ebitdamargin
    b = _f24_slope(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory mean-reversion gap: level minus slow baseline, sign-flipped
def f24mt_f24_margin_trajectory_gmrevgap_252d_base_v118_signal(grossmargin):
    base = _mean(grossmargin, 504)
    gap = grossmargin - base
    b = -gap * _f24_slope(grossmargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory momentum vs reversal blend (slope minus deviation)
def f24mt_f24_margin_trajectory_nmmomrev_126d_base_v119_signal(netmargin):
    sl = _z(_f24_slope(netmargin, 126), 252)
    dev = _z(netmargin, 252)
    b = sl - 0.5 * dev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory hit-rate over a quarter minus over a year (improving consistency)
def f24mt_f24_margin_trajectory_emhitspr_base_v120_signal(ebitdamargin):
    up = (ebitdamargin.diff() > 0).astype(float)
    short = up.rolling(63, min_periods=21).mean()
    long = up.rolling(252, min_periods=63).mean()
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin step detector: latest quarter mean vs prior quarter mean (level shift)
def f24mt_f24_margin_trajectory_gmstep_base_v121_signal(grossmargin):
    cur = _mean(grossmargin, 63)
    prev = _mean(grossmargin, 63).shift(63)
    b = cur - prev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin step detector standardized by recent dispersion (significance of shift)
def f24mt_f24_margin_trajectory_nmstepz_base_v122_signal(netmargin):
    cur = _mean(netmargin, 63)
    prev = _mean(netmargin, 63).shift(63)
    sd = _std(netmargin, 126)
    b = (cur - prev) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory entropy proxy: dispersion of sign of changes
def f24mt_f24_margin_trajectory_emdirentropy_126d_base_v123_signal(ebitdamargin):
    s = np.sign(ebitdamargin.diff())
    b = s.rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trajectory vs gross-margin trajectory correlation (co-movement)
def f24mt_f24_margin_trajectory_omgmcorr_252d_base_v124_signal(opinc, revenue, grossmargin):
    om = (opinc / revenue.replace(0, np.nan)).diff()
    gm = grossmargin.diff()
    b = om.rolling(252, min_periods=63).corr(gm)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin vs ebitda-margin trajectory correlation (below-the-line decoupling)
def f24mt_f24_margin_trajectory_nmemcorr_252d_base_v125_signal(netmargin, ebitdamargin):
    nm = netmargin.diff()
    em = ebitdamargin.diff()
    b = nm.rolling(252, min_periods=63).corr(em)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trend strength relative to revenue trend strength (margin vs scale leadership)
def f24mt_f24_margin_trajectory_gmrevlead_126d_base_v126_signal(grossmargin, revenue):
    gm_sl = _f24_slope(grossmargin, 126).abs()
    rev_sl = _f24_slope(np.log(revenue.replace(0, np.nan)), 126).abs()
    b = gm_sl / (gm_sl + rev_sl).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin cumulative drift: sum of monthly changes over a year (path length signed)
def f24mt_f24_margin_trajectory_emdrift_252d_base_v127_signal(ebitdamargin):
    mchg = ebitdamargin.diff(21)
    b = mchg.rolling(252, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin path roughness: sum of |changes| vs net change (trajectory efficiency)
def f24mt_f24_margin_trajectory_nmeffratio_252d_base_v128_signal(netmargin):
    net = (netmargin - netmargin.shift(252)).abs()
    gross_path = netmargin.diff().abs().rolling(252, min_periods=63).sum()
    b = net / gross_path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory efficiency ratio (directedness of GM moves)
def f24mt_f24_margin_trajectory_gmeffratio_126d_base_v129_signal(grossmargin):
    net = (grossmargin - grossmargin.shift(126)).abs()
    gross_path = grossmargin.diff().abs().rolling(126, min_periods=42).sum()
    b = net / gross_path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trajectory peak-to-current drawdown (margin underwater)
def f24mt_f24_margin_trajectory_omdrawdown_252d_base_v130_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    pk = om.rolling(252, min_periods=63).max()
    b = om - pk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin spread vs net trajectory: slope of (em-nm) normalized by level
def f24mt_f24_margin_trajectory_enslopen_126d_base_v131_signal(ebitdamargin, netmargin):
    spr = ebitdamargin - netmargin
    sl = _f24_slope(spr, 126)
    b = sl / _mean(spr, 126).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory: slope-sign-weighted expansion depth vs contraction depth (bounded balance)
def f24mt_f24_margin_trajectory_gmtanhslope_126d_base_v132_signal(grossmargin):
    d = grossmargin.diff()
    up = d.where(d > 0).rolling(126, min_periods=42).sum()
    dn = (-d.where(d < 0)).rolling(126, min_periods=42).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory: count of quarter-over-quarter improvements in the last year
def f24mt_f24_margin_trajectory_nmqoqwins_252d_base_v133_signal(netmargin):
    qchg = _f24_chg(netmargin, 63)
    win = (qchg > 0).astype(float)
    b = win.rolling(252, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin acceleration ranked cross-time (relative inflection percentile)
def f24mt_f24_margin_trajectory_emaccelrank_base_v134_signal(ebitdamargin):
    sl = _f24_slope(ebitdamargin, 63)
    acc = sl - sl.shift(63)
    b = _rank(acc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-vs-ebitda spread expansion streak (overhead-leverage persistence)
def f24mt_f24_margin_trajectory_gestreak_base_v135_signal(grossmargin, ebitdamargin):
    spr = grossmargin - ebitdamargin
    b = _f24_streak(spr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trend interacted with revenue level (scale-weighted directional)
def f24mt_f24_margin_trajectory_omscaleweight_126d_base_v136_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    sl = _f24_slope(om, 126)
    sc = _z(np.log(revenue.replace(0, np.nan)), 252)
    b = sl * sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin half-year trend minus gross-margin half-year trend, ranked (relative trajectory)
def f24mt_f24_margin_trajectory_nmgmrelrank_base_v137_signal(netmargin, grossmargin):
    nm = _f24_slope(netmargin, 126)
    gm = _f24_slope(grossmargin, 126)
    spr = nm - gm
    b = _rank(spr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory smoothness: 1 / curvature dispersion (steadiness)
def f24mt_f24_margin_trajectory_emsmooth_252d_base_v138_signal(ebitdamargin):
    cv = _f24_curv(ebitdamargin, 21)
    b = 1.0 / _std(cv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory: deviation from its EMA, standardized (anomaly of expansion)
def f24mt_f24_margin_trajectory_gmemaz_base_v139_signal(grossmargin):
    ema = grossmargin.ewm(span=126, min_periods=63).mean()
    dev = grossmargin - ema
    b = dev / _std(grossmargin, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin year change minus net-margin year change (cost vs tax/interest split)
def f24mt_f24_margin_trajectory_omnmchgspr_252d_base_v140_signal(opinc, revenue, netmargin):
    om = opinc / revenue.replace(0, np.nan)
    b = _f24_chg(om, 252) - _f24_chg(netmargin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory: net expansion magnitude per expanding sub-period (depth of up-phases)
def f24mt_f24_margin_trajectory_nmexpandtime_252d_base_v141_signal(netmargin):
    d = netmargin.diff()
    up = d.where(d > 0)
    b = up.rolling(252, min_periods=63).sum() / d.abs().rolling(252, min_periods=63).sum().replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory: largest expansion streak length over the year
def f24mt_f24_margin_trajectory_gmmaxstreak_252d_base_v142_signal(grossmargin):
    st = _f24_streak(grossmargin)
    b = st.rolling(252, min_periods=63).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory: ratio of recent slope to long-run slope, bounded
def f24mt_f24_margin_trajectory_emsloperatio_base_v143_signal(ebitdamargin):
    s = _f24_slope(ebitdamargin, 63)
    l = _f24_slope(ebitdamargin, 252)
    b = np.tanh(s / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trajectory: deviation from baseline weighted by trend (confirmed move)
def f24mt_f24_margin_trajectory_omconfirm_126d_base_v144_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    dev = om - _mean(om, 252)
    sl = _f24_slope(om, 63)
    b = dev * np.sign(sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-minus-net spread acceleration (cost-leverage inflection)
def f24mt_f24_margin_trajectory_gnsprcaccel_base_v145_signal(grossmargin, netmargin):
    spr = grossmargin - netmargin
    sl = _f24_slope(spr, 63)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-margin trajectory: realized expansion vs its own 1-year expectation (surprise)
def f24mt_f24_margin_trajectory_nmsurprise_base_v146_signal(netmargin):
    realized = _f24_chg(netmargin, 63)
    expected = _f24_chg(netmargin, 252) / 4.0
    b = realized - expected
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebitda-margin trajectory: slope x level x stability triple composite
def f24mt_f24_margin_trajectory_emtriple_126d_base_v147_signal(ebitdamargin):
    sl = _f24_slope(ebitdamargin, 126)
    lev = _mean(ebitdamargin, 126)
    stab = np.log1p(_f24_stab(ebitdamargin, 126).clip(lower=0))
    b = np.sign(sl) * sl.abs() ** 0.5 * lev * stab
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-margin trajectory: rolling regression R-squared proxy (trend linearity)
def f24mt_f24_margin_trajectory_gmlinearity_126d_base_v148_signal(grossmargin):
    sl = _f24_slope(grossmargin, 126)
    spread = sl * 126.0
    total = _std(grossmargin, 126) * np.sqrt(126.0)
    b = spread.abs() / total.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating-margin trajectory: net-of-revenue-trend margin alpha (margin beyond scale)
def f24mt_f24_margin_trajectory_omalpha_252d_base_v149_signal(opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    om_g = _f24_chg(om, 252)
    rev_g = np.log(revenue.replace(0, np.nan)).diff(252)
    b = om_g - 0.05 * rev_g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# all-margin composite trajectory: average z-scored trend across the four margins
def f24mt_f24_margin_trajectory_compzscore_252d_base_v150_signal(grossmargin, netmargin, ebitdamargin, opinc, revenue):
    om = opinc / revenue.replace(0, np.nan)
    g = _z(_f24_slope(grossmargin, 252), 504)
    nn = _z(_f24_slope(netmargin, 252), 504)
    e = _z(_f24_slope(ebitdamargin, 252), 504)
    o = _z(_f24_slope(om, 252), 504)
    b = pd.concat([g, nn, e, o], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24mt_f24_margin_trajectory_gmemaslope_63d_base_v076_signal,
    f24mt_f24_margin_trajectory_nmemaslope_21d_base_v077_signal,
    f24mt_f24_margin_trajectory_ememaslope_126d_base_v078_signal,
    f24mt_f24_margin_trajectory_omemaslope_63d_base_v079_signal,
    f24mt_f24_margin_trajectory_gmcurv_63d_base_v080_signal,
    f24mt_f24_margin_trajectory_nmcurv2_126d_base_v081_signal,
    f24mt_f24_margin_trajectory_emcurv_63d_base_v082_signal,
    f24mt_f24_margin_trajectory_omcurv_126d_base_v083_signal,
    f24mt_f24_margin_trajectory_gmtrendstr_126d_base_v084_signal,
    f24mt_f24_margin_trajectory_nmsignmag_126d_base_v085_signal,
    f24mt_f24_margin_trajectory_emrevtrend_126d_base_v086_signal,
    f24mt_f24_margin_trajectory_gnspremaslope_base_v087_signal,
    f24mt_f24_margin_trajectory_gecurv_126d_base_v088_signal,
    f24mt_f24_margin_trajectory_enstab_252d_base_v089_signal,
    f24mt_f24_margin_trajectory_passthru_252d_base_v090_signal,
    f24mt_f24_margin_trajectory_nepass_252d_base_v091_signal,
    f24mt_f24_margin_trajectory_baseagree_252d_base_v092_signal,
    f24mt_f24_margin_trajectory_trendrange_126d_base_v093_signal,
    f24mt_f24_margin_trajectory_gmstreakrank_base_v094_signal,
    f24mt_f24_margin_trajectory_nmdownrun_base_v095_signal,
    f24mt_f24_margin_trajectory_emaccel_63d_base_v096_signal,
    f24mt_f24_margin_trajectory_omaccel_base_v097_signal,
    f24mt_f24_margin_trajectory_gmslopeyoy_base_v098_signal,
    f24mt_f24_margin_trajectory_nmpacespr_base_v099_signal,
    f24mt_f24_margin_trajectory_emlevdir_126d_base_v100_signal,
    f24mt_f24_margin_trajectory_omrngpos_252d_base_v101_signal,
    f24mt_f24_margin_trajectory_gmcomprank_252d_base_v102_signal,
    f24mt_f24_margin_trajectory_nmrecovrate_252d_base_v103_signal,
    f24mt_f24_margin_trajectory_emz_504d_base_v104_signal,
    f24mt_f24_margin_trajectory_gmdisprank_base_v105_signal,
    f24mt_f24_margin_trajectory_nmvov_252d_base_v106_signal,
    f24mt_f24_margin_trajectory_emir_252d_base_v107_signal,
    f24mt_f24_margin_trajectory_omsignpersist_63d_base_v108_signal,
    f24mt_f24_margin_trajectory_gnsprrngpos_504d_base_v109_signal,
    f24mt_f24_margin_trajectory_nmprofitfrac_252d_base_v110_signal,
    f24mt_f24_margin_trajectory_emmaxchg_252d_base_v111_signal,
    f24mt_f24_margin_trajectory_gmminchg_252d_base_v112_signal,
    f24mt_f24_margin_trajectory_omchgskew_252d_base_v113_signal,
    f24mt_f24_margin_trajectory_nmchgkurt_252d_base_v114_signal,
    f24mt_f24_margin_trajectory_gmtrusttrend_126d_base_v115_signal,
    f24mt_f24_margin_trajectory_egconv_126d_base_v116_signal,
    f24mt_f24_margin_trajectory_omemspr_126d_base_v117_signal,
    f24mt_f24_margin_trajectory_gmrevgap_252d_base_v118_signal,
    f24mt_f24_margin_trajectory_nmmomrev_126d_base_v119_signal,
    f24mt_f24_margin_trajectory_emhitspr_base_v120_signal,
    f24mt_f24_margin_trajectory_gmstep_base_v121_signal,
    f24mt_f24_margin_trajectory_nmstepz_base_v122_signal,
    f24mt_f24_margin_trajectory_emdirentropy_126d_base_v123_signal,
    f24mt_f24_margin_trajectory_omgmcorr_252d_base_v124_signal,
    f24mt_f24_margin_trajectory_nmemcorr_252d_base_v125_signal,
    f24mt_f24_margin_trajectory_gmrevlead_126d_base_v126_signal,
    f24mt_f24_margin_trajectory_emdrift_252d_base_v127_signal,
    f24mt_f24_margin_trajectory_nmeffratio_252d_base_v128_signal,
    f24mt_f24_margin_trajectory_gmeffratio_126d_base_v129_signal,
    f24mt_f24_margin_trajectory_omdrawdown_252d_base_v130_signal,
    f24mt_f24_margin_trajectory_enslopen_126d_base_v131_signal,
    f24mt_f24_margin_trajectory_gmtanhslope_126d_base_v132_signal,
    f24mt_f24_margin_trajectory_nmqoqwins_252d_base_v133_signal,
    f24mt_f24_margin_trajectory_emaccelrank_base_v134_signal,
    f24mt_f24_margin_trajectory_gestreak_base_v135_signal,
    f24mt_f24_margin_trajectory_omscaleweight_126d_base_v136_signal,
    f24mt_f24_margin_trajectory_nmgmrelrank_base_v137_signal,
    f24mt_f24_margin_trajectory_emsmooth_252d_base_v138_signal,
    f24mt_f24_margin_trajectory_gmemaz_base_v139_signal,
    f24mt_f24_margin_trajectory_omnmchgspr_252d_base_v140_signal,
    f24mt_f24_margin_trajectory_nmexpandtime_252d_base_v141_signal,
    f24mt_f24_margin_trajectory_gmmaxstreak_252d_base_v142_signal,
    f24mt_f24_margin_trajectory_emsloperatio_base_v143_signal,
    f24mt_f24_margin_trajectory_omconfirm_126d_base_v144_signal,
    f24mt_f24_margin_trajectory_gnsprcaccel_base_v145_signal,
    f24mt_f24_margin_trajectory_nmsurprise_base_v146_signal,
    f24mt_f24_margin_trajectory_emtriple_126d_base_v147_signal,
    f24mt_f24_margin_trajectory_gmlinearity_126d_base_v148_signal,
    f24mt_f24_margin_trajectory_omalpha_252d_base_v149_signal,
    f24mt_f24_margin_trajectory_compzscore_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_MARGIN_TRAJECTORY_REGISTRY_076_150 = REGISTRY


def _fund(seed, n, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    revenue = _fund(101, n, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    grossmargin = _fund(102, n, base=0.35, drift=0.005, vol=0.03).clip(0.02, 0.9).rename("grossmargin")
    netmargin = _fund(103, n, base=0.12, drift=0.004, vol=0.04).clip(-0.2, 0.6).rename("netmargin")
    ebitdamargin = _fund(104, n, base=0.20, drift=0.004, vol=0.035).clip(-0.1, 0.7).rename("ebitdamargin")
    opinc = _fund(105, n, base=1.5e8, drift=0.02, vol=0.05, allow_neg=True).rename("opinc")
    gp = (revenue * _fund(106, n, base=0.33, drift=0.005, vol=0.03).clip(0.02, 0.9)).rename("gp")

    cols = {
        "grossmargin": grossmargin, "netmargin": netmargin,
        "ebitdamargin": ebitdamargin, "opinc": opinc,
        "revenue": revenue, "gp": gp,
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

    print("OK f24_margin_trajectory_base_076_150_claude: %d features pass" % n_features)
