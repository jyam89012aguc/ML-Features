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
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives: close-to-close realized volatility term structure =====
def _f10_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f10_rvol(closeadj, w):
    # close-to-close realized volatility (std of log returns) over window w
    r = _f10_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f10_rvol_ann(closeadj, w):
    # annualized realized volatility
    return _f10_rvol(closeadj, w) * np.sqrt(252.0)


def _f10_dnsemi(closeadj, w):
    # downside semi-deviation (negative returns only)
    r = _f10_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f10_upsemi(closeadj, w):
    # upside semi-deviation (positive returns only)
    r = _f10_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f10_cone_pos(closeadj, w, hist):
    # vol-cone position: percentile rank of current realized vol vs its own history
    v = _f10_rvol(closeadj, w)
    return v.rolling(hist, min_periods=max(2, hist // 4)).rank(pct=True) - 0.5


def _f10_vadj_ret(closeadj, w):
    # vol-adjusted return: log return over window divided by realized vol
    lr = np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))
    return lr / _f10_rvol(closeadj, w).replace(0, np.nan)


# ============================================================
# --- realized vol levels (annualized) at canonical windows ---
def f10rv_f10_realized_volatility_term_rvol_5d_base_v001_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_21d_base_v002_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_63d_base_v003_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_126d_base_v004_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_252d_base_v005_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol of MULTI-DAY (overlapping) returns: term structure of the return horizon ---
def f10rv_f10_realized_volatility_term_rvol5dret_63d_base_v006_signal(closeadj):
    # vol of 5-day log returns measured over 63d, per-day scaled (sqrt time)
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    b = r5.rolling(63, min_periods=21).std() / np.sqrt(5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol21dret_126d_base_v007_signal(closeadj):
    # vol of 21-day log returns measured over 126d, per-day scaled
    r21 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    b = r21.rolling(126, min_periods=42).std() / np.sqrt(21.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- variance ratio (Lo-MacKinlay): var(k-day ret)/(k*var(1-day)); >1 trending, <1 mean-reverting ---
def f10rv_f10_realized_volatility_term_varratio_5d_base_v008_signal(closeadj):
    r1 = _f10_logret(closeadj)
    rk = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    v1 = (r1 ** 2).rolling(126, min_periods=42).mean()
    vk = (rk ** 2).rolling(126, min_periods=42).mean()
    b = vk / (5.0 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure ratios: short vol / long vol ---
def f10rv_f10_realized_volatility_term_tsratio_5v21_base_v009_signal(closeadj):
    b = _f10_rvol(closeadj, 5) / _f10_rvol(closeadj, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsaccel_5v63_base_v010_signal(closeadj):
    # vol-shock timing: month-over-month change in the short/mid term-structure ratio
    ratio = _f10_rvol(closeadj, 5) / _f10_rvol(closeadj, 63).replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsratio_21v63_base_v011_signal(closeadj):
    b = _f10_rvol(closeadj, 21) / _f10_rvol(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsratio_21v126_base_v012_signal(closeadj):
    b = _f10_rvol(closeadj, 21) / _f10_rvol(closeadj, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsratio_63v252_base_v013_signal(closeadj):
    b = _f10_rvol(closeadj, 63) / _f10_rvol(closeadj, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsratio_126v252_base_v014_signal(closeadj):
    b = _f10_rvol(closeadj, 126) / _f10_rvol(closeadj, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- change in term-structure ratio over a month (term-structure momentum) ---
def f10rv_f10_realized_volatility_term_tsmom_21v126_base_v015_signal(closeadj):
    ratio = _f10_rvol(closeadj, 21) / _f10_rvol(closeadj, 126).replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure ratio z-scored vs its own 252d history (de-trended) ---
def f10rv_f10_realized_volatility_term_tsz_63v252_base_v016_signal(closeadj):
    ratio = _f10_rvol(closeadj, 63) / _f10_rvol(closeadj, 252).replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure ratio percentile-ranked vs its 504d history (cone of slope) ---
def f10rv_f10_realized_volatility_term_tsrank_5v63_base_v017_signal(closeadj):
    ratio = _f10_rvol(closeadj, 5) / _f10_rvol(closeadj, 63).replace(0, np.nan)
    b = ratio.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- second-order term structure: short/mid ratio minus mid/long ratio (slope-of-slope) ---
def f10rv_f10_realized_volatility_term_tstwist_base_v018_signal(closeadj):
    # curve twist: near-end tilt (21/63) vs far-end tilt (63/252); decoupled from 5d noise
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    near = v21 / v63.replace(0, np.nan)
    far = v126 / v252.replace(0, np.nan)
    b = near - far
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure ratio dispersion across multiple pairs (curve instability) ---
def f10rv_f10_realized_volatility_term_tspairdisp_base_v019_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    p1 = v5 / v21.replace(0, np.nan)
    p2 = v21 / v63.replace(0, np.nan)
    p3 = v63 / v126.replace(0, np.nan)
    p4 = v126 / v252.replace(0, np.nan)
    b = pd.concat([p1, p2, p3, p4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol slope sign-streak: fraction of last quarter in vol-backwardation (short>long) ---
def f10rv_f10_realized_volatility_term_slopestreak_21v252_base_v020_signal(closeadj):
    spread = _f10_rvol(closeadj, 21) - _f10_rvol(closeadj, 252)
    inv = (spread > 0).astype(float)
    b = inv.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol curvature: convexity across 3 term points (short, mid, long) ---
def f10rv_f10_realized_volatility_term_curv_21_63_252_base_v021_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v252 = _f10_rvol(closeadj, 252)
    b = (v21 + v252) / 2.0 - v63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_curv_5_21_63_base_v022_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    b = (v5 + v63) / 2.0 - v21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_curv_21_126_252_base_v023_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    b = (v21 + v252) / 2.0 - v126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- curvature momentum: change in the term-structure butterfly over a month ---
def f10rv_f10_realized_volatility_term_curvmom_21_63_252_base_v024_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v252 = _f10_rvol(closeadj, 252)
    bf = ((v21 + v252) / 2.0 - v63) / v63.replace(0, np.nan)
    b = bf - bf.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside / upside semi-deviation levels ---
def f10rv_f10_realized_volatility_term_dnsemi_21d_base_v025_signal(closeadj):
    b = _f10_dnsemi(closeadj, 21) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_dnsemi_63d_base_v026_signal(closeadj):
    b = _f10_dnsemi(closeadj, 63) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_upsemi_21d_base_v027_signal(closeadj):
    b = _f10_upsemi(closeadj, 21) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_upsemi_63d_base_v028_signal(closeadj):
    b = _f10_upsemi(closeadj, 63) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-deviation asymmetry: downside minus upside (vol skew) ---
def f10rv_f10_realized_volatility_term_semispr_21d_base_v029_signal(closeadj):
    b = (_f10_dnsemi(closeadj, 21) - _f10_upsemi(closeadj, 21)) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_semispr_63d_base_v030_signal(closeadj):
    b = (_f10_dnsemi(closeadj, 63) - _f10_upsemi(closeadj, 63)) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_semispr_126d_base_v031_signal(closeadj):
    b = (_f10_dnsemi(closeadj, 126) - _f10_upsemi(closeadj, 126)) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-deviation ratio: downside / upside (downside vol dominance) ---
def f10rv_f10_realized_volatility_term_semiratio_21d_base_v032_signal(closeadj):
    b = _f10_dnsemi(closeadj, 21) / _f10_upsemi(closeadj, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-semi term structure: short downside vol / long downside vol ---
def f10rv_f10_realized_volatility_term_dnsemits_21v126_base_v033_signal(closeadj):
    b = _f10_dnsemi(closeadj, 21) / _f10_dnsemi(closeadj, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- upside-semi term structure: short upside vol / long upside vol ---
def f10rv_f10_realized_volatility_term_upsemits_21v126_base_v034_signal(closeadj):
    b = _f10_upsemi(closeadj, 21) / _f10_upsemi(closeadj, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-balance momentum: change in downside/upside skew over a quarter ---
def f10rv_f10_realized_volatility_term_semibalmom_63d_base_v035_signal(closeadj):
    dn = _f10_dnsemi(closeadj, 63)
    up = _f10_upsemi(closeadj, 63)
    bal = (dn - up) / (dn + up).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-balance percentile vs its own 504d history (skew regime cone) ---
def f10rv_f10_realized_volatility_term_semibalrank_252d_base_v036_signal(closeadj):
    dn = _f10_dnsemi(closeadj, 252)
    up = _f10_upsemi(closeadj, 252)
    bal = (dn - up) / (dn + up).replace(0, np.nan)
    b = bal.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position: where current short vol sits in its long history ---
def f10rv_f10_realized_volatility_term_cone_21in252_base_v037_signal(closeadj):
    b = _f10_cone_pos(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_cone_252in1260_base_v038_signal(closeadj):
    b = _f10_cone_pos(closeadj, 252, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_cone_63in504_base_v039_signal(closeadj):
    b = _f10_cone_pos(closeadj, 63, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_conechg_21in252_base_v040_signal(closeadj):
    # change in vol-cone position over a month (regime transition speed)
    cp = _f10_cone_pos(closeadj, 21, 252)
    b = cp - cp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_conegap_5v63_base_v041_signal(closeadj):
    # disagreement between short-vol cone and mid-vol cone positions
    c5 = _f10_cone_pos(closeadj, 5, 252)
    c63 = _f10_cone_pos(closeadj, 63, 504)
    b = c5 - c63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol z-score within cone (standardized cone position) ---
def f10rv_f10_realized_volatility_term_conez_21in252_base_v042_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol z-score CHANGE: vol-regime acceleration (is the vol z rising?) ---
def f10rv_f10_realized_volatility_term_conezmom_63in504_base_v043_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    zz = _z(v, 504)
    b = zz - zz.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return (return per unit of realized vol, Sharpe-like) ---
def f10rv_f10_realized_volatility_term_vadjret_21d_base_v044_signal(closeadj):
    b = _f10_vadj_ret(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_vadjret_63d_base_v045_signal(closeadj):
    b = _f10_vadj_ret(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_vadjret_126d_base_v046_signal(closeadj):
    b = _f10_vadj_ret(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_vadjret_252d_base_v047_signal(closeadj):
    b = _f10_vadj_ret(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-of-vol: std of the rolling realized-vol series (cyclical instability) ---
def f10rv_f10_realized_volatility_term_volofvol_21in63_base_v048_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_volofvol_5in63_base_v049_signal(closeadj):
    v = _f10_rvol(closeadj, 5)
    b = v.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_volofvol_63in252_base_v050_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    b = v.rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coefficient of variation of vol (vol-of-vol scaled by mean vol) ---
def f10rv_f10_realized_volatility_term_volcv_21in252_base_v051_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v.rolling(252, min_periods=63).std() / v.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol mean-reversion gap: current short vol vs its EWMA, normalized (regime distance) ---
def f10rv_f10_realized_volatility_term_volrevert_63d_base_v052_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    ew = v.ewm(span=252, min_periods=63).mean()
    sd = v.rolling(504, min_periods=126).std()
    b = (v - ew) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol trend: log-slope of the 63d vol series over a quarter (vol drifting up/down) ---
def f10rv_f10_realized_volatility_term_voltrend_63d_base_v053_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    b = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone width: spread between 90th and 10th percentile of vol history ---
def f10rv_f10_realized_volatility_term_conewidth_21in252_base_v054_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    hi = v.rolling(252, min_periods=63).quantile(0.9)
    lo = v.rolling(252, min_periods=63).quantile(0.1)
    b = (hi - lo) / v.rolling(252, min_periods=63).median().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distance of current vol from cone floor (compression headroom) ---
def f10rv_f10_realized_volatility_term_conefloor_21in252_base_v055_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    lo = v.rolling(252, min_periods=63).min()
    b = (v - lo) / lo.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- distance of current vol below cone ceiling (expansion headroom) ---
def f10rv_f10_realized_volatility_term_coneceil_21in252_base_v056_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    hi = v.rolling(252, min_periods=63).max()
    b = (hi - v) / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope across the full 5/21/63/126/252 curve (OLS slope) ---
def f10rv_f10_realized_volatility_term_tsfit_curv_base_v057_signal(closeadj):
    # quadratic curvature of the vol term structure: 2nd-order finite-difference
    # in log-vol across 21/63/126/252 (convex=vol concentrated at extremes)
    v21 = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    v63 = np.log(_f10_rvol(closeadj, 63).replace(0, np.nan))
    v126 = np.log(_f10_rvol(closeadj, 126).replace(0, np.nan))
    v252 = np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    d1 = v126 - 2.0 * v63 + v21
    d2 = v252 - 2.0 * v126 + v63
    b = d2 - d1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure dispersion: std across the 5 term vols (curve roughness) ---
def f10rv_f10_realized_volatility_term_tsdisp_base_v058_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    stk = pd.concat([v5, v21, v63, v126, v252], axis=1)
    b = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure monotonicity: is the vol curve consistently upward sloping? ---
def f10rv_f10_realized_volatility_term_tsmono_base_v059_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    up = ((v21 > v5).astype(float) + (v63 > v21).astype(float)
          + (v126 > v63).astype(float) + (v252 > v126).astype(float))
    mag = (v252 - v5) / v63.replace(0, np.nan)
    b = (up / 4.0 - 0.5) + 0.25 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean absolute return (L1 vol) vs std (L2 vol) ratio: tail-fatness proxy ---
def f10rv_f10_realized_volatility_term_l1l2_21d_base_v060_signal(closeadj):
    r = _f10_logret(closeadj)
    mad = r.abs().rolling(21, min_periods=10).mean()
    sd = r.rolling(21, min_periods=10).std()
    b = mad / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_l1l2_63d_base_v061_signal(closeadj):
    r = _f10_logret(closeadj)
    mad = r.abs().rolling(63, min_periods=21).mean()
    sd = r.rolling(63, min_periods=21).std()
    b = mad / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized quarticity proxy: kurtosis of returns (vol-of-vol within window) ---
def f10rv_f10_realized_volatility_term_kurt_63d_base_v062_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_kurt_126d_base_v063_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- return skewness within window (directional vol asymmetry) ---
def f10rv_f10_realized_volatility_term_skew_63d_base_v064_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_skew_126d_base_v065_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA realized vol (RiskMetrics-style) vs simple vol (smoothing premium) ---
def f10rv_f10_realized_volatility_term_ewmavol_21d_base_v066_signal(closeadj):
    r = _f10_logret(closeadj)
    b = np.sqrt((r ** 2).ewm(span=21, min_periods=10).mean()) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_ewmavol_63d_base_v067_signal(closeadj):
    r = _f10_logret(closeadj)
    b = np.sqrt((r ** 2).ewm(span=63, min_periods=21).mean()) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA vs simple vol gap (fast-vol leading slow-vol; expansion signal) ---
def f10rv_f10_realized_volatility_term_ewmagap_21d_base_v068_signal(closeadj):
    r = _f10_logret(closeadj)
    ew = np.sqrt((r ** 2).ewm(span=21, min_periods=10).mean())
    sv = _f10_rvol(closeadj, 63)
    b = ew / sv.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- max single-day |return| relative to window vol (jump dominance) ---
def f10rv_f10_realized_volatility_term_jumpdom_63d_base_v069_signal(closeadj):
    r = _f10_logret(closeadj)
    mx = r.abs().rolling(63, min_periods=21).max()
    sd = r.rolling(63, min_periods=21).std()
    b = mx / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- bipower-variation-style: sum |r_t||r_{t-1}| vs realized variance (jump-robust) ---
def f10rv_f10_realized_volatility_term_bipower_63d_base_v070_signal(closeadj):
    r = _f10_logret(closeadj)
    bp = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).mean() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).mean()
    b = 1.0 - bp / rv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol persistence: autocorrelation of squared returns (clustering strength) ---
def f10rv_f10_realized_volatility_term_volpersist_63d_base_v071_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    b = r2.rolling(63, min_periods=21).corr(r2.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_volpersist_126d_base_v072_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    b = r2.rolling(126, min_periods=42).corr(r2.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-vol cone position (semi-dev percentile in its history) ---
def f10rv_f10_realized_volatility_term_dnsemicone_63in504_base_v073_signal(closeadj):
    dn = _f10_dnsemi(closeadj, 63)
    b = dn.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-peak staleness: fraction of the 126d window since the 21d-vol last peaked ---
def f10rv_f10_realized_volatility_term_volpeakage_21in126_base_v074_signal(closeadj):
    v = _f10_rvol(closeadj, 21)

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = v.rolling(126, min_periods=42).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure inversion flag weighted by depth (short>long backwardation) ---
def f10rv_f10_realized_volatility_term_tsinvert_21v126_base_v075_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v126 = _f10_rvol(closeadj, 126)
    spread = (v21 - v126) / v126.replace(0, np.nan)
    inv = (spread > 0).astype(float)
    streak = inv.rolling(63, min_periods=21).mean()
    b = streak + spread.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_realized_volatility_term_rvol_5d_base_v001_signal,
    f10rv_f10_realized_volatility_term_rvol_21d_base_v002_signal,
    f10rv_f10_realized_volatility_term_rvol_63d_base_v003_signal,
    f10rv_f10_realized_volatility_term_rvol_126d_base_v004_signal,
    f10rv_f10_realized_volatility_term_rvol_252d_base_v005_signal,
    f10rv_f10_realized_volatility_term_rvol5dret_63d_base_v006_signal,
    f10rv_f10_realized_volatility_term_rvol21dret_126d_base_v007_signal,
    f10rv_f10_realized_volatility_term_varratio_5d_base_v008_signal,
    f10rv_f10_realized_volatility_term_tsratio_5v21_base_v009_signal,
    f10rv_f10_realized_volatility_term_tsaccel_5v63_base_v010_signal,
    f10rv_f10_realized_volatility_term_tsratio_21v63_base_v011_signal,
    f10rv_f10_realized_volatility_term_tsratio_21v126_base_v012_signal,
    f10rv_f10_realized_volatility_term_tsratio_63v252_base_v013_signal,
    f10rv_f10_realized_volatility_term_tsratio_126v252_base_v014_signal,
    f10rv_f10_realized_volatility_term_tsmom_21v126_base_v015_signal,
    f10rv_f10_realized_volatility_term_tsz_63v252_base_v016_signal,
    f10rv_f10_realized_volatility_term_tsrank_5v63_base_v017_signal,
    f10rv_f10_realized_volatility_term_tstwist_base_v018_signal,
    f10rv_f10_realized_volatility_term_tspairdisp_base_v019_signal,
    f10rv_f10_realized_volatility_term_slopestreak_21v252_base_v020_signal,
    f10rv_f10_realized_volatility_term_curv_21_63_252_base_v021_signal,
    f10rv_f10_realized_volatility_term_curv_5_21_63_base_v022_signal,
    f10rv_f10_realized_volatility_term_curv_21_126_252_base_v023_signal,
    f10rv_f10_realized_volatility_term_curvmom_21_63_252_base_v024_signal,
    f10rv_f10_realized_volatility_term_dnsemi_21d_base_v025_signal,
    f10rv_f10_realized_volatility_term_dnsemi_63d_base_v026_signal,
    f10rv_f10_realized_volatility_term_upsemi_21d_base_v027_signal,
    f10rv_f10_realized_volatility_term_upsemi_63d_base_v028_signal,
    f10rv_f10_realized_volatility_term_semispr_21d_base_v029_signal,
    f10rv_f10_realized_volatility_term_semispr_63d_base_v030_signal,
    f10rv_f10_realized_volatility_term_semispr_126d_base_v031_signal,
    f10rv_f10_realized_volatility_term_semiratio_21d_base_v032_signal,
    f10rv_f10_realized_volatility_term_dnsemits_21v126_base_v033_signal,
    f10rv_f10_realized_volatility_term_upsemits_21v126_base_v034_signal,
    f10rv_f10_realized_volatility_term_semibalmom_63d_base_v035_signal,
    f10rv_f10_realized_volatility_term_semibalrank_252d_base_v036_signal,
    f10rv_f10_realized_volatility_term_cone_21in252_base_v037_signal,
    f10rv_f10_realized_volatility_term_cone_252in1260_base_v038_signal,
    f10rv_f10_realized_volatility_term_cone_63in504_base_v039_signal,
    f10rv_f10_realized_volatility_term_conechg_21in252_base_v040_signal,
    f10rv_f10_realized_volatility_term_conegap_5v63_base_v041_signal,
    f10rv_f10_realized_volatility_term_conez_21in252_base_v042_signal,
    f10rv_f10_realized_volatility_term_conezmom_63in504_base_v043_signal,
    f10rv_f10_realized_volatility_term_vadjret_21d_base_v044_signal,
    f10rv_f10_realized_volatility_term_vadjret_63d_base_v045_signal,
    f10rv_f10_realized_volatility_term_vadjret_126d_base_v046_signal,
    f10rv_f10_realized_volatility_term_vadjret_252d_base_v047_signal,
    f10rv_f10_realized_volatility_term_volofvol_21in63_base_v048_signal,
    f10rv_f10_realized_volatility_term_volofvol_5in63_base_v049_signal,
    f10rv_f10_realized_volatility_term_volofvol_63in252_base_v050_signal,
    f10rv_f10_realized_volatility_term_volcv_21in252_base_v051_signal,
    f10rv_f10_realized_volatility_term_volrevert_63d_base_v052_signal,
    f10rv_f10_realized_volatility_term_voltrend_63d_base_v053_signal,
    f10rv_f10_realized_volatility_term_conewidth_21in252_base_v054_signal,
    f10rv_f10_realized_volatility_term_conefloor_21in252_base_v055_signal,
    f10rv_f10_realized_volatility_term_coneceil_21in252_base_v056_signal,
    f10rv_f10_realized_volatility_term_tsfit_curv_base_v057_signal,
    f10rv_f10_realized_volatility_term_tsdisp_base_v058_signal,
    f10rv_f10_realized_volatility_term_tsmono_base_v059_signal,
    f10rv_f10_realized_volatility_term_l1l2_21d_base_v060_signal,
    f10rv_f10_realized_volatility_term_l1l2_63d_base_v061_signal,
    f10rv_f10_realized_volatility_term_kurt_63d_base_v062_signal,
    f10rv_f10_realized_volatility_term_kurt_126d_base_v063_signal,
    f10rv_f10_realized_volatility_term_skew_63d_base_v064_signal,
    f10rv_f10_realized_volatility_term_skew_126d_base_v065_signal,
    f10rv_f10_realized_volatility_term_ewmavol_21d_base_v066_signal,
    f10rv_f10_realized_volatility_term_ewmavol_63d_base_v067_signal,
    f10rv_f10_realized_volatility_term_ewmagap_21d_base_v068_signal,
    f10rv_f10_realized_volatility_term_jumpdom_63d_base_v069_signal,
    f10rv_f10_realized_volatility_term_bipower_63d_base_v070_signal,
    f10rv_f10_realized_volatility_term_volpersist_63d_base_v071_signal,
    f10rv_f10_realized_volatility_term_volpersist_126d_base_v072_signal,
    f10rv_f10_realized_volatility_term_dnsemicone_63in504_base_v073_signal,
    f10rv_f10_realized_volatility_term_volpeakage_21in126_base_v074_signal,
    f10rv_f10_realized_volatility_term_tsinvert_21v126_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_REALIZED_VOLATILITY_TERM_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    cols = {"closeadj": closeadj}

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

    print("OK f10_realized_volatility_term_base_001_075_claude: %d features pass" % n_features)
