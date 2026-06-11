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
    return s.rolling(w, min_periods=max(2, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (close-to-close realized volatility term structure) =====
def _f09_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f09_rvol(closeadj, w):
    r = _f09_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252.0)


def _f09_rvol_raw(closeadj, w):
    r = _f09_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_ewvol(closeadj, span):
    # exponentially-weighted realized vol (annualized)
    r = _f09_logret(closeadj)
    return r.ewm(span=span, min_periods=max(2, span // 2)).std() * np.sqrt(252.0)


def _f09_downvol(closeadj, w):
    r = _f09_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    ss = (neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(ss) * np.sqrt(252.0)


def _f09_upvol(closeadj, w):
    r = _f09_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    ss = (pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(ss) * np.sqrt(252.0)


def _f09_volratio(closeadj, ws, wl):
    return _f09_rvol(closeadj, ws) / _f09_rvol(closeadj, wl).replace(0, np.nan)


def _f09_volslope(closeadj, ws, wl):
    vs = _f09_rvol(closeadj, ws)
    vl = _f09_rvol(closeadj, wl)
    span = np.log(float(wl)) - np.log(float(ws))
    return (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span


def _f09_volcone(closeadj, w, hist):
    v = _f09_rvol(closeadj, w)
    return v.rolling(hist, min_periods=max(5, hist // 4)).rank(pct=True) - 0.5


def _f09_mad_vol(closeadj, w):
    # mean-absolute-deviation volatility (robust dispersion of returns)
    r = _f09_logret(closeadj)
    mu = r.rolling(w, min_periods=max(2, w // 2)).mean()
    return (r - mu).abs().rolling(w, min_periods=max(2, w // 2)).mean() * np.sqrt(252.0)


def _f09_voladjret(closeadj, w):
    r = _f09_logret(closeadj)
    cum = r.rolling(w, min_periods=max(2, w // 2)).sum()
    return cum / _f09_rvol_raw(closeadj, w).replace(0, np.nan)


# ============================================================
# --- EWMA vol levels across spans (smoothed term structure) ---
def f09vt_f09_volatility_term_structure_ewvol_10_base_v076_signal(closeadj):
    b = _f09_ewvol(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewvol_42_base_v077_signal(closeadj):
    b = _f09_ewvol(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA vol vs simple vol gap (recency-weighting premium) ---
def f09vt_f09_volatility_term_structure_ewgap_21_base_v078_signal(closeadj):
    b = _f09_ewvol(closeadj, 21) - _f09_rvol(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA fast/slow vol ratio (smoothed term-structure slope) ---
def f09vt_f09_volatility_term_structure_ewratio_base_v079_signal(closeadj):
    fast = _f09_ewvol(closeadj, 10)
    slow = _f09_ewvol(closeadj, 63)
    b = (fast - slow) / (fast + slow).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MAD-based robust vol level (5/63d) ---
def f09vt_f09_volatility_term_structure_madvol_21_base_v080_signal(closeadj):
    b = _f09_mad_vol(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MAD vol vs std vol ratio (tail-heaviness of the return distribution) ---
def f09vt_f09_volatility_term_structure_madstd_63_base_v081_signal(closeadj):
    mad = _f09_mad_vol(closeadj, 63)
    sd = _f09_rvol(closeadj, 63)
    # for a normal, mad/std ~ 0.8; deviations flag fat tails
    b = mad / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MAD-vol term structure slope (robust short/long) ---
def f09vt_f09_volatility_term_structure_madslope_base_v082_signal(closeadj):
    vs = _f09_mad_vol(closeadj, 21)
    vl = _f09_mad_vol(closeadj, 126)
    b = (vs - vl) / (vs + vl).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol persistence: autocorrelation of the squared returns (vol clustering) ---
def f09vt_f09_volatility_term_structure_volcluster_63_base_v083_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2

    def _ac(a):
        a0 = a[1:]
        a1 = a[:-1]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return np.corrcoef(a0, a1)[0, 1]

    b = r2.rolling(63, min_periods=42).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcluster_126_base_v084_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2

    def _ac(a):
        a0 = a[1:]
        a1 = a[:-1]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return np.corrcoef(a0, a1)[0, 1]

    b = r2.rolling(126, min_periods=63).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- variance ratio of vol horizons: var(63d agg) vs scaled var(21d) ---
def f09vt_f09_volatility_term_structure_varratio_base_v085_signal(closeadj):
    r = _f09_logret(closeadj)
    v21 = r.rolling(21, min_periods=10).var()
    v63 = r.rolling(63, min_periods=21).var()
    # if returns were iid, var scales linearly; ratio of per-day variances reveals mean-reversion/trending
    b = v63 / v21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone at extra horizons (252d cone, 5-year history) ---
def f09vt_f09_volatility_term_structure_cone_252d_base_v086_signal(closeadj):
    b = _f09_volcone(closeadj, 252, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_cone_42d_base_v087_signal(closeadj):
    b = _f09_volcone(closeadj, 42, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone slope across horizons (are short cones more extreme than long cones) ---
def f09vt_f09_volatility_term_structure_coneslope_base_v088_signal(closeadj):
    c_short = _f09_volcone(closeadj, 5, 126)
    c_long = _f09_volcone(closeadj, 126, 504)
    b = c_short - c_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol regression slope across 5 log-horizons (smooth term slope) ---
def f09vt_f09_volatility_term_structure_regslope5_base_v089_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
    logw = np.log(np.array(ws, dtype=float))
    logw = logw - logw.mean()
    denom = float((logw ** 2).sum())
    vols = [np.log(_f09_rvol(closeadj, w).replace(0, np.nan)) for w in ws]
    mat = pd.concat(vols, axis=1)
    mat.columns = range(len(ws))
    centered = mat.sub(mat.mean(axis=1), axis=0)
    num = (centered * logw).sum(axis=1)
    b = num / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- regression R-squared of the term structure (how monotone is the vol curve) ---
def f09vt_f09_volatility_term_structure_regfit_base_v090_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
    logw = np.log(np.array(ws, dtype=float))
    logw = logw - logw.mean()
    denom = float((logw ** 2).sum())
    vols = [np.log(_f09_rvol(closeadj, w).replace(0, np.nan)) for w in ws]
    mat = pd.concat(vols, axis=1)
    mat.columns = range(len(ws))
    centered = mat.sub(mat.mean(axis=1), axis=0)
    slope = (centered * logw).sum(axis=1) / denom
    fitted = pd.DataFrame({k: slope * logw[k] for k in range(len(ws))})
    ss_res = ((centered - fitted) ** 2).sum(axis=1)
    ss_tot = (centered ** 2).sum(axis=1).replace(0, np.nan)
    b = 1.0 - ss_res / ss_tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return at extra horizons (5d Sharpe-like) ---
def f09vt_f09_volatility_term_structure_voladjret_5d_base_v091_signal(closeadj):
    b = _f09_voladjret(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_42d_base_v092_signal(closeadj):
    b = _f09_voladjret(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted-return momentum (change in Sharpe over time) ---
def f09vt_f09_volatility_term_structure_sharpemom_63d_base_v093_signal(closeadj):
    sh = _f09_voladjret(closeadj, 63)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol level ranked at 5d (front-end percentile regime) ---
def f09vt_f09_volatility_term_structure_volrank_5d_base_v094_signal(closeadj):
    v = _f09_rvol(closeadj, 5)
    b = _rank(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol level ranked at 126d (mid percentile regime) ---
def f09vt_f09_volatility_term_structure_volrank_126d_base_v095_signal(closeadj):
    v = _f09_rvol(closeadj, 126)
    b = _rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-deviation cone for upside vol at 126d ---
def f09vt_f09_volatility_term_structure_upcone_126d_base_v096_signal(closeadj):
    uv = _f09_upvol(closeadj, 126)
    b = uv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-vol momentum (is downside risk rising) ---
def f09vt_f09_volatility_term_structure_downmom_21d_base_v097_signal(closeadj):
    dv = _f09_downvol(closeadj, 21)
    b = np.log(dv.replace(0, np.nan) / dv.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- upside-vol momentum at 63d ---
def f09vt_f09_volatility_term_structure_upmom_63d_base_v098_signal(closeadj):
    uv = _f09_upvol(closeadj, 63)
    b = np.log(uv.replace(0, np.nan) / uv.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semivol asymmetry at 252d (long-run skew in vol) ---
def f09vt_f09_volatility_term_structure_volskew_252d_base_v099_signal(closeadj):
    b = _f09_downvol(closeadj, 252) - _f09_upvol(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-of-vol at the 63d horizon, ranked (regime of vol turbulence) ---
def f09vt_f09_volatility_term_structure_vovrank_base_v100_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    vov = v.pct_change().rolling(63, min_periods=21).std()
    b = _rank(vov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-of-vol momentum (turbulence trend) ---
def f09vt_f09_volatility_term_structure_vovmom_base_v101_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    vov = v.pct_change().rolling(63, min_periods=21).std()
    b = vov - vov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol skewness of returns (3rd-moment within window) ---
def f09vt_f09_volatility_term_structure_retskew_63d_base_v102_signal(closeadj):
    r = _f09_logret(closeadj)
    b = r.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized kurtosis of returns (tail fatness; vol-of-vol cousin) ---
def f09vt_f09_volatility_term_structure_retkurt_126d_base_v103_signal(closeadj):
    r = _f09_logret(closeadj)
    b = r.rolling(126, min_periods=42).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure curvature using EWMA vols (smooth hump detector) ---
def f09vt_f09_volatility_term_structure_ewcurv_base_v104_signal(closeadj):
    vs = np.log(_f09_ewvol(closeadj, 10).replace(0, np.nan))
    vm = np.log(_f09_ewvol(closeadj, 42).replace(0, np.nan))
    vl = np.log(_f09_ewvol(closeadj, 126).replace(0, np.nan))
    b = vs - 2.0 * vm + vl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- max single-day return contribution to window vol (jump dominance) ---
def f09vt_f09_volatility_term_structure_jumpshare_21d_base_v105_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    mx = r2.rolling(21, min_periods=10).max()
    tot = r2.rolling(21, min_periods=10).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_jumpshare_63d_base_v106_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    mx = r2.rolling(63, min_periods=21).max()
    tot = r2.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- continuous (median-based) vol vs total vol (jump-robust vol share) ---
def f09vt_f09_volatility_term_structure_contvol_share_base_v107_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    med = r2.rolling(63, min_periods=21).median()
    mean = r2.rolling(63, min_periods=21).mean()
    b = med / mean.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- bipower-ish variation vs realized variance (jump detector) ---
def f09vt_f09_volatility_term_structure_bipower_base_v108_signal(closeadj):
    ar = _f09_logret(closeadj).abs()
    bipow = (ar * ar.shift(1)).rolling(63, min_periods=21).mean() * (np.pi / 2.0)
    rv = (_f09_logret(closeadj) ** 2).rolling(63, min_periods=21).mean()
    b = 1.0 - bipow / rv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol term-structure level percentile spread (short cone minus long cone, 21 vs 252) ---
def f09vt_f09_volatility_term_structure_conespr_21v252_base_v109_signal(closeadj):
    c1 = _f09_volcone(closeadj, 21, 252)
    c2 = _f09_volcone(closeadj, 252, 1260)
    b = c1 - c2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol normalized return interacted with term-slope sign (regime-conditioned Sharpe) ---
def f09vt_f09_volatility_term_structure_condsharpe_base_v110_signal(closeadj):
    sh = _f09_voladjret(closeadj, 63)
    slope_sign = np.sign(_f09_volslope(closeadj, 21, 252))
    b = sh * slope_sign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log-vol dispersion across the whole curve (term-structure roughness, log space) ---
def f09vt_f09_volatility_term_structure_logdisp_base_v111_signal(closeadj):
    v1 = np.log(_f09_rvol(closeadj, 5).replace(0, np.nan))
    v2 = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    v3 = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    v4 = np.log(_f09_rvol(closeadj, 126).replace(0, np.nan))
    v5 = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    b = pd.concat([v1, v2, v3, v4, v5], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range of the vol term structure (max horizon vol minus min horizon vol, normalized) ---
def f09vt_f09_volatility_term_structure_termrange_base_v112_signal(closeadj):
    v1 = _f09_rvol(closeadj, 5)
    v2 = _f09_rvol(closeadj, 21)
    v3 = _f09_rvol(closeadj, 63)
    v4 = _f09_rvol(closeadj, 252)
    stacked = pd.concat([v1, v2, v3, v4], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure concavity: geometric-mean vol vs arithmetic-mean vol across horizons ---
def f09vt_f09_volatility_term_structure_geoarith_base_v113_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
    vols = [_f09_rvol(closeadj, w) for w in ws]
    mat = pd.concat(vols, axis=1)
    mat.columns = range(len(ws))
    geo = np.exp(np.log(mat.replace(0, np.nan)).mean(axis=1))
    arith = mat.mean(axis=1).replace(0, np.nan)
    b = geo / arith - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol mean-reversion speed: corr of vol level with subsequent vol change ---
def f09vt_f09_volatility_term_structure_volmeanrev_base_v114_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    dev = v - v.rolling(252, min_periods=63).mean()
    fwd_chg = v.shift(-21) - v
    # rolling correlation of deviation with forward change (negative => mean-reverting)
    b = dev.rolling(252, min_periods=63).corr(fwd_chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA vol-cone position (smoothed regime percentile) ---
def f09vt_f09_volatility_term_structure_ewcone_base_v115_signal(closeadj):
    ev = _f09_ewvol(closeadj, 21)
    b = ev.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside semivol cone at 126d (downside regime percentile, long history) ---
def f09vt_f09_volatility_term_structure_downcone_126d_base_v116_signal(closeadj):
    dv = _f09_downvol(closeadj, 126)
    b = dv.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semivol slope twist: downside slope minus upside slope across short horizons ---
def f09vt_f09_volatility_term_structure_semitwist_base_v117_signal(closeadj):
    span = np.log(63.0) - np.log(5.0)
    dn = (np.log(_f09_downvol(closeadj, 63).replace(0, np.nan))
          - np.log(_f09_downvol(closeadj, 5).replace(0, np.nan))) / span
    up = (np.log(_f09_upvol(closeadj, 63).replace(0, np.nan))
          - np.log(_f09_upvol(closeadj, 5).replace(0, np.nan))) / span
    b = dn - up
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol curvature momentum (change in the humpedness over a quarter) ---
def f09vt_f09_volatility_term_structure_curvmom_base_v118_signal(closeadj):
    vs = np.log(_f09_rvol(closeadj, 5).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, 42).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    curv = vs - 2.0 * vm + vl
    b = curv - curv.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Lo-MacKinlay variance ratio: var of 5d returns vs 5x var of 1d returns (vol scaling) ---
def f09vt_f09_volatility_term_structure_varratio5_base_v119_signal(closeadj):
    r1 = _f09_logret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    var1 = r1.rolling(126, min_periods=42).var()
    var5 = r5.rolling(126, min_periods=42).var()
    b = var5 / (5.0 * var1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure level z-scored at 63d using a long lookback (regime extremity) ---
def f09vt_f09_volatility_term_structure_volzlong_63d_base_v120_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = _z(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- front-spike velocity: change in the 5d/252d vol ratio over a week (impulse onset) ---
def f09vt_f09_volatility_term_structure_frontspike_base_v121_signal(closeadj):
    ratio = _f09_rvol(closeadj, 5) / _f09_rvol(closeadj, 252).replace(0, np.nan)
    b = ratio - ratio.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mid-vol vs blended short+long (butterfly of the vol curve) ---
def f09vt_f09_volatility_term_structure_butterfly_base_v122_signal(closeadj):
    vs = _f09_rvol(closeadj, 21)
    vm = _f09_rvol(closeadj, 63)
    vl = _f09_rvol(closeadj, 252)
    b = vm - 0.5 * (vs + vl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ratio of EWMA-vol-cone short vs long (smoothed cone slope) ---
def f09vt_f09_volatility_term_structure_ewconeslope_base_v123_signal(closeadj):
    ev_s = _f09_ewvol(closeadj, 10)
    ev_l = _f09_ewvol(closeadj, 63)
    c_s = ev_s.rolling(252, min_periods=63).rank(pct=True)
    c_l = ev_l.rolling(252, min_periods=63).rank(pct=True)
    b = c_s - c_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- long-horizon vol-of-vol: dispersion of the 63d vol over a year (slow turbulence) ---
def f09vt_f09_volatility_term_structure_slowvov_base_v124_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = v.pct_change(21).rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- front inversion: how often AND how strongly 5d vol exceeded 63d vol over a quarter ---
def f09vt_f09_volatility_term_structure_invfreq_base_v125_signal(closeadj):
    v5 = _f09_rvol(closeadj, 5)
    v63 = _f09_rvol(closeadj, 63)
    inv = (v5 > v63).astype(float)
    freq = inv.rolling(63, min_periods=21).mean() - 0.5
    mag = ((v5 - v63) / v63.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = freq + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return using downside denominator at 21d (short Sortino) ---
def f09vt_f09_volatility_term_structure_shortsortino_base_v126_signal(closeadj):
    r = _f09_logret(closeadj)
    cum = r.rolling(21, min_periods=10).sum()
    dv = _f09_downvol(closeadj, 21) / np.sqrt(252.0)
    b = cum / dv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term structure of the vol-adjusted return (short Sharpe minus mid Sharpe) ---
def f09vt_f09_volatility_term_structure_sharpeterm_base_v127_signal(closeadj):
    b = _f09_voladjret(closeadj, 5) - _f09_voladjret(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol curvature sign persistence (is the curve consistently humped or bowed) ---
def f09vt_f09_volatility_term_structure_curvsign_base_v128_signal(closeadj):
    vs = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    curv = vs - 2.0 * vm + vl
    b = np.sign(curv).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol of overlapping 5d returns over 63d (multi-day vol vs 1-day vol) ---
def f09vt_f09_volatility_term_structure_multidayvol_base_v129_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v5 = r5.rolling(63, min_periods=21).std()
    v1 = _f09_rvol_raw(closeadj, 63) * np.sqrt(5.0)
    b = v5 / v1.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone of the multi-day (5d) vol (regime of weekly volatility) ---
def f09vt_f09_volatility_term_structure_weeklyvolcone_base_v130_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v5 = r5.rolling(63, min_periods=21).std()
    b = v5.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-vol vs upside-vol cone spread (asymmetry regime percentile) ---
def f09vt_f09_volatility_term_structure_asymcone_base_v131_signal(closeadj):
    dc = _f09_downvol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    uc = _f09_upvol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    b = dc - uc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol term-slope interacted with vol-of-vol (steepening under turbulence) ---
def f09vt_f09_volatility_term_structure_slopexvov_base_v132_signal(closeadj):
    slope = _f09_volslope(closeadj, 21, 126)
    v = _f09_rvol(closeadj, 21)
    vov = v.pct_change().rolling(63, min_periods=21).std()
    b = slope * vov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- rolling regression slope of vol on time (vol trend over 126d, not horizon) ---
def f09vt_f09_volatility_term_structure_voltimetrend_base_v133_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    w = 126

    def _sl(a):
        m = len(a)
        t = np.arange(m, dtype=float)
        t = t - t.mean()
        denom = float((t ** 2).sum())
        if denom == 0:
            return np.nan
        a = a - a.mean()
        return float((a * t).sum()) / denom

    b = v.rolling(w, min_periods=63).apply(_sl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coefficient of variation of vol (vol dispersion normalized by level) ---
def f09vt_f09_volatility_term_structure_volcv_base_v134_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    sd = v.rolling(126, min_periods=42).std()
    mu = v.rolling(126, min_periods=42).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ratio of recent vol to trailing-year max vol (proximity to vol peak) ---
def f09vt_f09_volatility_term_structure_volpeakprox_base_v135_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    mx = v.rolling(252, min_periods=63).max()
    b = v / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ratio of recent vol to trailing-year min vol (compression off the floor) ---
def f09vt_f09_volatility_term_structure_voltroughprox_base_v136_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    mn = v.rolling(252, min_periods=63).min()
    b = np.log(v.replace(0, np.nan) / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term structure level position within its own 252d hi-lo vol range ---
def f09vt_f09_volatility_term_structure_volrangepos_base_v137_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    mx = v.rolling(252, min_periods=63).max()
    mn = v.rolling(252, min_periods=63).min()
    b = (v - mn) / (mx - mn).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- slope of the semivol asymmetry over time (is skew-in-vol trending) ---
def f09vt_f09_volatility_term_structure_skewtrend_base_v138_signal(closeadj):
    sk = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    b = sk - sk.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol entropy-ish: dispersion of squared returns within window ---
def f09vt_f09_volatility_term_structure_r2disp_base_v139_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    sd = r2.rolling(63, min_periods=21).std()
    mu = r2.rolling(63, min_periods=21).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gap between EWMA-fast vol and 252d realized vol (recency stress) ---
def f09vt_f09_volatility_term_structure_recencystress_base_v140_signal(closeadj):
    fast = _f09_ewvol(closeadj, 5)
    slow = _f09_rvol(closeadj, 252)
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope instability: rolling dispersion of the vol term slope ---
def f09vt_f09_volatility_term_structure_slopevol_base_v141_signal(closeadj):
    sl = _f09_volslope(closeadj, 21, 252)
    b = sl.rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside semivol-adjusted long return (long-horizon Sortino) ---
def f09vt_f09_volatility_term_structure_longsortino_base_v142_signal(closeadj):
    r = _f09_logret(closeadj)
    cum = r.rolling(252, min_periods=63).sum()
    dv = _f09_downvol(closeadj, 252) / np.sqrt(252.0)
    b = cum / dv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-curve convexity ranked vs history (humped regime percentile) ---
def f09vt_f09_volatility_term_structure_convrank_base_v143_signal(closeadj):
    vs = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    curv = vs - 2.0 * vm + vl
    b = curv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol acceleration at 63d (second difference of mid-horizon vol) ---
def f09vt_f09_volatility_term_structure_volaccel_63d_base_v144_signal(closeadj):
    lv = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    b = lv - 2.0 * lv.shift(63) + lv.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- spread between MAD-vol cone and std-vol cone (tail-regime divergence) ---
def f09vt_f09_volatility_term_structure_madconespr_base_v145_signal(closeadj):
    mc = _f09_mad_vol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    sc = _f09_rvol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    b = mc - sc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol times downside-share (downside-weighted vol intensity) ---
def f09vt_f09_volatility_term_structure_downweightvol_base_v146_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    share = _f09_downvol(closeadj, 63) / v.replace(0, np.nan)
    b = v * (share - 0.7071)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-slope of the vol-of-vol (is turbulence front- or back-loaded) ---
def f09vt_f09_volatility_term_structure_vovslope_base_v147_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    chg = v.pct_change()
    vov_s = chg.rolling(42, min_periods=21).std()
    vov_l = chg.rolling(126, min_periods=42).std()
    b = (vov_s - vov_l) / (vov_s + vov_l).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol minus its long EWMA (vol displacement, slow baseline) ---
def f09vt_f09_volatility_term_structure_voldispslow_base_v148_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = v - v.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- skewness of the vol term structure (asymmetry across horizons themselves) ---
def f09vt_f09_volatility_term_structure_termskew_base_v149_signal(closeadj):
    v1 = _f09_rvol(closeadj, 5)
    v2 = _f09_rvol(closeadj, 21)
    v3 = _f09_rvol(closeadj, 63)
    v4 = _f09_rvol(closeadj, 126)
    v5 = _f09_rvol(closeadj, 252)
    mat = pd.concat([v1, v2, v3, v4, v5], axis=1)
    mu = mat.mean(axis=1)
    sd = mat.std(axis=1).replace(0, np.nan)
    m3 = ((mat.sub(mu, axis=0)) ** 3).mean(axis=1)
    b = m3 / (sd ** 3)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite term-structure stress: steep + high + downside-skewed ---
def f09vt_f09_volatility_term_structure_stresscomposite_base_v150_signal(closeadj):
    slope = _f09_volslope(closeadj, 5, 63)
    cone = _f09_volcone(closeadj, 21, 252)
    skew = _f09_downvol(closeadj, 21) - _f09_upvol(closeadj, 21)
    b = slope + cone + np.tanh(50.0 * skew)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vt_f09_volatility_term_structure_ewvol_10_base_v076_signal,
    f09vt_f09_volatility_term_structure_ewvol_42_base_v077_signal,
    f09vt_f09_volatility_term_structure_ewgap_21_base_v078_signal,
    f09vt_f09_volatility_term_structure_ewratio_base_v079_signal,
    f09vt_f09_volatility_term_structure_madvol_21_base_v080_signal,
    f09vt_f09_volatility_term_structure_madstd_63_base_v081_signal,
    f09vt_f09_volatility_term_structure_madslope_base_v082_signal,
    f09vt_f09_volatility_term_structure_volcluster_63_base_v083_signal,
    f09vt_f09_volatility_term_structure_volcluster_126_base_v084_signal,
    f09vt_f09_volatility_term_structure_varratio_base_v085_signal,
    f09vt_f09_volatility_term_structure_cone_252d_base_v086_signal,
    f09vt_f09_volatility_term_structure_cone_42d_base_v087_signal,
    f09vt_f09_volatility_term_structure_coneslope_base_v088_signal,
    f09vt_f09_volatility_term_structure_regslope5_base_v089_signal,
    f09vt_f09_volatility_term_structure_regfit_base_v090_signal,
    f09vt_f09_volatility_term_structure_voladjret_5d_base_v091_signal,
    f09vt_f09_volatility_term_structure_voladjret_42d_base_v092_signal,
    f09vt_f09_volatility_term_structure_sharpemom_63d_base_v093_signal,
    f09vt_f09_volatility_term_structure_volrank_5d_base_v094_signal,
    f09vt_f09_volatility_term_structure_volrank_126d_base_v095_signal,
    f09vt_f09_volatility_term_structure_upcone_126d_base_v096_signal,
    f09vt_f09_volatility_term_structure_downmom_21d_base_v097_signal,
    f09vt_f09_volatility_term_structure_upmom_63d_base_v098_signal,
    f09vt_f09_volatility_term_structure_volskew_252d_base_v099_signal,
    f09vt_f09_volatility_term_structure_vovrank_base_v100_signal,
    f09vt_f09_volatility_term_structure_vovmom_base_v101_signal,
    f09vt_f09_volatility_term_structure_retskew_63d_base_v102_signal,
    f09vt_f09_volatility_term_structure_retkurt_126d_base_v103_signal,
    f09vt_f09_volatility_term_structure_ewcurv_base_v104_signal,
    f09vt_f09_volatility_term_structure_jumpshare_21d_base_v105_signal,
    f09vt_f09_volatility_term_structure_jumpshare_63d_base_v106_signal,
    f09vt_f09_volatility_term_structure_contvol_share_base_v107_signal,
    f09vt_f09_volatility_term_structure_bipower_base_v108_signal,
    f09vt_f09_volatility_term_structure_conespr_21v252_base_v109_signal,
    f09vt_f09_volatility_term_structure_condsharpe_base_v110_signal,
    f09vt_f09_volatility_term_structure_logdisp_base_v111_signal,
    f09vt_f09_volatility_term_structure_termrange_base_v112_signal,
    f09vt_f09_volatility_term_structure_geoarith_base_v113_signal,
    f09vt_f09_volatility_term_structure_volmeanrev_base_v114_signal,
    f09vt_f09_volatility_term_structure_ewcone_base_v115_signal,
    f09vt_f09_volatility_term_structure_downcone_126d_base_v116_signal,
    f09vt_f09_volatility_term_structure_semitwist_base_v117_signal,
    f09vt_f09_volatility_term_structure_curvmom_base_v118_signal,
    f09vt_f09_volatility_term_structure_varratio5_base_v119_signal,
    f09vt_f09_volatility_term_structure_volzlong_63d_base_v120_signal,
    f09vt_f09_volatility_term_structure_frontspike_base_v121_signal,
    f09vt_f09_volatility_term_structure_butterfly_base_v122_signal,
    f09vt_f09_volatility_term_structure_ewconeslope_base_v123_signal,
    f09vt_f09_volatility_term_structure_slowvov_base_v124_signal,
    f09vt_f09_volatility_term_structure_invfreq_base_v125_signal,
    f09vt_f09_volatility_term_structure_shortsortino_base_v126_signal,
    f09vt_f09_volatility_term_structure_sharpeterm_base_v127_signal,
    f09vt_f09_volatility_term_structure_curvsign_base_v128_signal,
    f09vt_f09_volatility_term_structure_multidayvol_base_v129_signal,
    f09vt_f09_volatility_term_structure_weeklyvolcone_base_v130_signal,
    f09vt_f09_volatility_term_structure_asymcone_base_v131_signal,
    f09vt_f09_volatility_term_structure_slopexvov_base_v132_signal,
    f09vt_f09_volatility_term_structure_voltimetrend_base_v133_signal,
    f09vt_f09_volatility_term_structure_volcv_base_v134_signal,
    f09vt_f09_volatility_term_structure_volpeakprox_base_v135_signal,
    f09vt_f09_volatility_term_structure_voltroughprox_base_v136_signal,
    f09vt_f09_volatility_term_structure_volrangepos_base_v137_signal,
    f09vt_f09_volatility_term_structure_skewtrend_base_v138_signal,
    f09vt_f09_volatility_term_structure_r2disp_base_v139_signal,
    f09vt_f09_volatility_term_structure_recencystress_base_v140_signal,
    f09vt_f09_volatility_term_structure_slopevol_base_v141_signal,
    f09vt_f09_volatility_term_structure_longsortino_base_v142_signal,
    f09vt_f09_volatility_term_structure_convrank_base_v143_signal,
    f09vt_f09_volatility_term_structure_volaccel_63d_base_v144_signal,
    f09vt_f09_volatility_term_structure_madconespr_base_v145_signal,
    f09vt_f09_volatility_term_structure_downweightvol_base_v146_signal,
    f09vt_f09_volatility_term_structure_vovslope_base_v147_signal,
    f09vt_f09_volatility_term_structure_voldispslow_base_v148_signal,
    f09vt_f09_volatility_term_structure_termskew_base_v149_signal,
    f09vt_f09_volatility_term_structure_stresscomposite_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_TERM_STRUCTURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f09_volatility_term_structure_base_076_150_claude: %d features pass" % n_features)
