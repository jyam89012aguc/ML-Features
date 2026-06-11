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
    r = _f10_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f10_rvol_ann(closeadj, w):
    return _f10_rvol(closeadj, w) * np.sqrt(252.0)


def _f10_dnsemi(closeadj, w):
    r = _f10_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f10_upsemi(closeadj, w):
    r = _f10_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f10_rvar(closeadj, w):
    r = _f10_logret(closeadj)
    return (r ** 2).rolling(w, min_periods=max(2, w // 2)).sum()


def _f10_ewmavol(closeadj, span):
    r = _f10_logret(closeadj)
    return np.sqrt((r ** 2).ewm(span=span, min_periods=max(2, span // 2)).mean())


# ============================================================
# --- additional canonical vol levels (annualized) at finer/longer windows ---
def f10rv_f10_realized_volatility_term_rvol_10d_base_v076_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_42d_base_v077_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_189d_base_v078_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvol_504d_base_v079_signal(closeadj):
    b = _f10_rvol_ann(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure ratios on the finer grid (distinct window pairs) ---
def f10rv_f10_realized_volatility_term_tsratio_10v42_base_v080_signal(closeadj):
    b = _f10_rvol(closeadj, 10) / _f10_rvol(closeadj, 42).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsratio_42v189_base_v081_signal(closeadj):
    b = _f10_rvol(closeadj, 42) / _f10_rvol(closeadj, 189).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_tsratio_189v504_base_v082_signal(closeadj):
    b = _f10_rvol(closeadj, 189) / _f10_rvol(closeadj, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- full-span term-structure ratio z-scored vs its own 252d history (de-trended span) ---
def f10rv_f10_realized_volatility_term_tsratioz_10v252_base_v083_signal(closeadj):
    ratio = _f10_rvol(closeadj, 10) / _f10_rvol(closeadj, 252).replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- variance ratios at longer horizons (vol mean-reversion across scales) ---
def f10rv_f10_realized_volatility_term_varratio_21d_base_v084_signal(closeadj):
    r1 = _f10_logret(closeadj)
    rk = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    v1 = (r1 ** 2).rolling(252, min_periods=84).mean()
    vk = (rk ** 2).rolling(252, min_periods=84).mean()
    b = vk / (21.0 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_varratio_10d_base_v085_signal(closeadj):
    r1 = _f10_logret(closeadj)
    rk = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    v1 = (r1 ** 2).rolling(189, min_periods=63).mean()
    vk = (rk ** 2).rolling(189, min_periods=63).mean()
    b = vk / (10.0 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- variance-ratio curvature: convexity of VR across 5/10/21 horizons (scaling shape) ---
def f10rv_f10_realized_volatility_term_vrcurv_base_v086_signal(closeadj):
    r1 = _f10_logret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(5).replace(0, np.nan))
    r10 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(10).replace(0, np.nan))
    r21 = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    v1 = (r1 ** 2).rolling(252, min_periods=84).mean()
    vr5 = (r5 ** 2).rolling(252, min_periods=84).mean() / (5.0 * v1).replace(0, np.nan)
    vr10 = (r10 ** 2).rolling(252, min_periods=84).mean() / (10.0 * v1).replace(0, np.nan)
    vr21 = (r21 ** 2).rolling(252, min_periods=84).mean() / (21.0 * v1).replace(0, np.nan)
    b = (vr5 + vr21) / 2.0 - vr10
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized variance share of the most extreme day (concentration / jumpiness) ---
def f10rv_f10_realized_volatility_term_rvconc_21d_base_v087_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    mx = r2.rolling(21, min_periods=10).max()
    tot = r2.rolling(21, min_periods=10).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_rvconc_63d_base_v088_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    mx = r2.rolling(63, min_periods=21).max()
    tot = r2.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Herfindahl concentration of daily variance contributions (top-heavy vol) ---
def f10rv_f10_realized_volatility_term_rvherf_63d_base_v089_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    tot = r2.rolling(63, min_periods=21).sum()
    share2 = (r2 ** 2).rolling(63, min_periods=21).sum()
    b = share2 / (tot ** 2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position at finer/longer windows (percentile of vol in its history) ---
def f10rv_f10_realized_volatility_term_cone_10in252_base_v090_signal(closeadj):
    v = _f10_rvol(closeadj, 10)
    b = v.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_cone_42in504_base_v091_signal(closeadj):
    v = _f10_rvol(closeadj, 42)
    b = v.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_conemom_189in1260_base_v092_signal(closeadj):
    # change in the long-window vol-cone position over a quarter (slow regime drift)
    v = _f10_rvol(closeadj, 189)
    cp = v.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    b = cp - cp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone band position: (v - median)/(p90 - p10) standardized within cone ---
def f10rv_f10_realized_volatility_term_conestd_21in252_base_v093_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    med = v.rolling(252, min_periods=63).median()
    hi = v.rolling(252, min_periods=63).quantile(0.9)
    lo = v.rolling(252, min_periods=63).quantile(0.1)
    b = (v - med) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-semi cone position (percentile of downside vol in its history) ---
def f10rv_f10_realized_volatility_term_dnsemicone_21in252_base_v094_signal(closeadj):
    dn = _f10_dnsemi(closeadj, 21)
    b = dn.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- upside-semi cone position ---
def f10rv_f10_realized_volatility_term_upsemicone_21in252_base_v095_signal(closeadj):
    up = _f10_upsemi(closeadj, 21)
    b = up.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-deviation term structure slopes (downside) ---
def f10rv_f10_realized_volatility_term_dnsemislope_21_126_base_v096_signal(closeadj):
    b = (_f10_dnsemi(closeadj, 126) - _f10_dnsemi(closeadj, 21)) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-deviation term structure slopes (upside) ---
def f10rv_f10_realized_volatility_term_upsemislope_21_126_base_v097_signal(closeadj):
    b = (_f10_upsemi(closeadj, 126) - _f10_upsemi(closeadj, 21)) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-vs-upside term-structure divergence (skew steepening across horizons) ---
def f10rv_f10_realized_volatility_term_semitsdiv_base_v098_signal(closeadj):
    dn_s = _f10_dnsemi(closeadj, 21) / _f10_dnsemi(closeadj, 126).replace(0, np.nan)
    up_s = _f10_upsemi(closeadj, 21) / _f10_upsemi(closeadj, 126).replace(0, np.nan)
    b = dn_s - up_s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-of-vol at finer windows ---
def f10rv_f10_realized_volatility_term_volofvol_10in126_base_v099_signal(closeadj):
    v = _f10_rvol(closeadj, 10)
    b = v.rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_volofvol_126in504_base_v100_signal(closeadj):
    v = _f10_rvol(closeadj, 126)
    b = v.rolling(504, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-of-vol coefficient of variation at finer windows (relative vol instability) ---
def f10rv_f10_realized_volatility_term_volcv_63in504_base_v101_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    sd = v.rolling(504, min_periods=126).std()
    mu = v.rolling(504, min_periods=126).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- log-vol of log-vol: standard deviation of the log realized-vol series ---
def f10rv_f10_realized_volatility_term_logvolofvol_21in252_base_v102_signal(closeadj):
    lv = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    b = lv.rolling(252, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol persistence: AR(1) of the log realized-vol series (vol memory) ---
def f10rv_f10_realized_volatility_term_volar1_63d_base_v103_signal(closeadj):
    lv = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    b = lv.rolling(63, min_periods=21).corr(lv.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_volar1_126d_base_v104_signal(closeadj):
    lv = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    b = lv.rolling(126, min_periods=42).corr(lv.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol half-life proxy: 1 - autocorr of squared returns at lag 5 (decay speed) ---
def f10rv_f10_realized_volatility_term_voldecay_63d_base_v105_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    ac = r2.rolling(63, min_periods=21).corr(r2.shift(5))
    b = 1.0 - ac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA vol term structure: fast-span EWMA vol vs slow-span EWMA vol ---
def f10rv_f10_realized_volatility_term_ewts_10v63_base_v106_signal(closeadj):
    b = _f10_ewmavol(closeadj, 10) / _f10_ewmavol(closeadj, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_ewts_21v126_base_v107_signal(closeadj):
    b = _f10_ewmavol(closeadj, 21) / _f10_ewmavol(closeadj, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EWMA vs simple vol convexity gap at a longer horizon ---
def f10rv_f10_realized_volatility_term_ewmagap_63d_base_v108_signal(closeadj):
    ew = _f10_ewmavol(closeadj, 63)
    sv = _f10_rvol(closeadj, 126)
    b = ew / sv.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol momentum: change in 21d vol over a week (vol acceleration) ---
def f10rv_f10_realized_volatility_term_volmom_21d_base_v109_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = np.log(v.replace(0, np.nan) / v.shift(5).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol momentum at the quarterly horizon ---
def f10rv_f10_realized_volatility_term_volmom_126d_base_v110_signal(closeadj):
    v = _f10_rvol(closeadj, 126)
    b = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol expansion streak: fraction of last quarter with 21d vol above its 63d mean ---
def f10rv_f10_realized_volatility_term_volexpstreak_base_v111_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    above = (v > v.rolling(63, min_periods=21).mean()).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- high-vol day intensity: mean exceedance magnitude beyond 2x window vol ---
def f10rv_f10_realized_volatility_term_extremeintensity_63d_base_v112_signal(closeadj):
    r = _f10_logret(closeadj)
    sd = r.rolling(63, min_periods=21).std()
    exc = (r.abs() / (2.0 * sd).replace(0, np.nan) - 1.0).clip(lower=0)
    b = exc.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- tail-asymmetry intensity: magnitude-weighted down-tail minus up-tail exceedance ---
def f10rv_f10_realized_volatility_term_tailasym_63d_base_v113_signal(closeadj):
    r = _f10_logret(closeadj)
    sd = r.rolling(63, min_periods=21).std()
    thr = 1.5 * sd
    dn = (-r - thr).clip(lower=0).rolling(63, min_periods=21).mean()
    up = (r - thr).clip(lower=0).rolling(63, min_periods=21).mean()
    b = (dn - up) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol regime: days since vol last in its bottom quartile (compression staleness) ---
def f10rv_f10_realized_volatility_term_compressage_base_v114_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    q25 = v.rolling(252, min_periods=63).quantile(0.25)
    low = (v <= q25).astype(float)

    def _age(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))

    b = low.rolling(126, min_periods=42).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol skew: third moment of the realized-vol series itself (regime tilt) ---
def f10rv_f10_realized_volatility_term_volseries_skew_base_v115_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v.rolling(252, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol range width over the long history normalized (cone amplitude) ---
def f10rv_f10_realized_volatility_term_coneamp_63in1260_base_v116_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    hi = v.rolling(1260, min_periods=252).max()
    lo = v.rolling(1260, min_periods=252).min()
    b = (hi - lo) / v.rolling(1260, min_periods=252).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol relative to a blended multi-window baseline (curve-center distance) ---
def f10rv_f10_realized_volatility_term_curvecenter_base_v117_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    center = (v21 + v63 + v126 + v252) / 4.0
    b = v21 / center.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure roll-down: vol at 63d minus where it was projected from 126/252 ---
def f10rv_f10_realized_volatility_term_rolldown_base_v118_signal(closeadj):
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    proj = 2.0 * v126 - v252
    b = (v63 - proj) / v126.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return at finer windows (momentum per unit risk) ---
def f10rv_f10_realized_volatility_term_vadjret_42d_base_v119_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan) / closeadj.shift(42).replace(0, np.nan))
    b = lr / _f10_rvol(closeadj, 42).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f10rv_f10_realized_volatility_term_vadjret_189d_base_v120_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan) / closeadj.shift(189).replace(0, np.nan))
    b = lr / _f10_rvol(closeadj, 189).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return term structure: short risk-adj return minus long ---
def f10rv_f10_realized_volatility_term_vadjret_slope_base_v121_signal(closeadj):
    lr_s = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    lr_l = np.log(closeadj.replace(0, np.nan) / closeadj.shift(126).replace(0, np.nan))
    s = lr_s / _f10_rvol(closeadj, 21).replace(0, np.nan)
    l = lr_l / _f10_rvol(closeadj, 126).replace(0, np.nan)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-risk-adjusted return (Sortino) at the monthly horizon ---
def f10rv_f10_realized_volatility_term_sortino_21d_base_v122_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    dn = _f10_dnsemi(closeadj, 21)
    b = lr / (dn * np.sqrt(21.0)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- mean absolute deviation realized vol (robust L1 vol) at the monthly window ---
def f10rv_f10_realized_volatility_term_madvol_21d_base_v123_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.abs().rolling(21, min_periods=10).mean() * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- MAD-vol term-structure ratio (robust short/long vol) ---
def f10rv_f10_realized_volatility_term_madts_21v126_base_v124_signal(closeadj):
    r = _f10_logret(closeadj)
    s = r.abs().rolling(21, min_periods=10).mean()
    l = r.abs().rolling(126, min_periods=42).mean()
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- median absolute return (very robust vol) vs std (outlier sensitivity) ---
def f10rv_f10_realized_volatility_term_medmad_63d_base_v125_signal(closeadj):
    r = _f10_logret(closeadj)
    med = r.abs().rolling(63, min_periods=21).median()
    sd = r.rolling(63, min_periods=21).std()
    b = med / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- interquartile range of returns normalized by std (distribution shape) ---
def f10rv_f10_realized_volatility_term_iqrstd_126d_base_v126_signal(closeadj):
    r = _f10_logret(closeadj)
    q75 = r.rolling(126, min_periods=42).quantile(0.75)
    q25 = r.rolling(126, min_periods=42).quantile(0.25)
    sd = r.rolling(126, min_periods=42).std()
    b = (q75 - q25) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized semivariance gap (Barndorff-Nielsen): (dn^2-up^2) over total var ---
def f10rv_f10_realized_volatility_term_semivargap_63d_base_v127_signal(closeadj):
    dn = _f10_dnsemi(closeadj, 63) ** 2
    up = _f10_upsemi(closeadj, 63) ** 2
    b = (dn - up) / (dn + up).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized semivariance gap momentum (signed jump risk trend) ---
def f10rv_f10_realized_volatility_term_semivargapmom_base_v128_signal(closeadj):
    dn = _f10_dnsemi(closeadj, 63) ** 2
    up = _f10_upsemi(closeadj, 63) ** 2
    gap = (dn - up) / (dn + up).replace(0, np.nan)
    b = gap - gap.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- annualized-vol gap between two estimators: close-to-close vs EWMA (model risk) ---
def f10rv_f10_realized_volatility_term_estgap_21d_base_v129_signal(closeadj):
    cc = _f10_rvol(closeadj, 21)
    ew = _f10_ewmavol(closeadj, 21)
    b = (cc - ew) / ((cc + ew) / 2.0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position momentum (regime climb at 63d window) ---
def f10rv_f10_realized_volatility_term_conemom_63in504_base_v130_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    cp = v.rolling(504, min_periods=126).rank(pct=True) - 0.5
    b = cp - cp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope of the cone position (short cone vs long cone) ---
def f10rv_f10_realized_volatility_term_coneslope_base_v131_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v126 = _f10_rvol(closeadj, 126)
    c21 = v21.rolling(252, min_periods=63).rank(pct=True)
    c126 = v126.rolling(252, min_periods=63).rank(pct=True)
    b = c21 - c126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol z-score gap between short and long windows (term-structure z) ---
def f10rv_f10_realized_volatility_term_volzgap_base_v132_signal(closeadj):
    z21 = _z(_f10_rvol(closeadj, 21), 252)
    z126 = _z(_f10_rvol(closeadj, 126), 252)
    b = z21 - z126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized variance of overnight-equivalent: variance of 2-day returns scaled ---
def f10rv_f10_realized_volatility_term_var2dret_63d_base_v133_signal(closeadj):
    r2d = np.log(closeadj.replace(0, np.nan) / closeadj.shift(2).replace(0, np.nan))
    b = r2d.rolling(63, min_periods=21).std() / np.sqrt(2.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- autocorrelation of returns (sign of vol-clustering vs mean-reversion in price) ---
def f10rv_f10_realized_volatility_term_retac1_63d_base_v134_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(63, min_periods=21).corr(r.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol of the rolling 5d vol expressed as a fraction of mean (micro vol-of-vol) ---
def f10rv_f10_realized_volatility_term_microvov_5in21_base_v135_signal(closeadj):
    v = _f10_rvol(closeadj, 5)
    sd = v.rolling(21, min_periods=10).std()
    mu = v.rolling(21, min_periods=10).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol acceleration: second difference of the 21d vol over weekly steps ---
def f10rv_f10_realized_volatility_term_volaccel_21d_base_v136_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v - 2.0 * v.shift(5) + v.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone breach magnitude: how far above the 90th-pct vol the current vol is ---
def f10rv_f10_realized_volatility_term_conebreach_21in252_base_v137_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    p90 = v.rolling(252, min_periods=63).quantile(0.9)
    b = (v / p90.replace(0, np.nan) - 1.0).clip(lower=-0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol floor distance: how far above the 10th-pct vol the current vol is (squeeze) ---
def f10rv_f10_realized_volatility_term_conefloordist_21in252_base_v138_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    p10 = v.rolling(252, min_periods=63).quantile(0.1)
    b = v / p10.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol elasticity: %change in vol per %change in price over a month ---
def f10rv_f10_realized_volatility_term_volelast_base_v139_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    dvol = np.log(v.replace(0, np.nan) / v.shift(21).replace(0, np.nan))
    dpx = np.log(closeadj.replace(0, np.nan) / closeadj.shift(21).replace(0, np.nan))
    b = dvol * np.sign(dpx)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- leverage effect: correlation between returns and next-day squared returns ---
def f10rv_f10_realized_volatility_term_leverage_126d_base_v140_signal(closeadj):
    r = _f10_logret(closeadj)
    r2next = (r.shift(-1)) ** 2
    b = r.rolling(126, min_periods=42).corr(r2next)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol asymmetry: avg vol after down days minus avg vol after up days ---
def f10rv_f10_realized_volatility_term_volafterdown_base_v141_signal(closeadj):
    r = _f10_logret(closeadj)
    r2 = r ** 2
    down = r.shift(1) < 0
    up = r.shift(1) > 0
    vd = r2.where(down).rolling(126, min_periods=30).mean()
    vu = r2.where(up).rolling(126, min_periods=30).mean()
    b = np.sqrt(vd) - np.sqrt(vu)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol trend strength: |log-slope| of vol over a quarter (directional vol) ---
def f10rv_f10_realized_volatility_term_voltrendstr_base_v142_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    slope = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    b = slope.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol range over a quarter normalized (vol swing amplitude) ---
def f10rv_f10_realized_volatility_term_volswing_63d_base_v143_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    hi = v.rolling(63, min_periods=21).max()
    lo = v.rolling(63, min_periods=21).min()
    b = (hi - lo) / v.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol vs its 252-day-ago value (year-over-year vol regime change) ---
def f10rv_f10_realized_volatility_term_volyoy_63d_base_v144_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    b = np.log(v.replace(0, np.nan) / v.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure ratio year-over-year change (curve-shape regime shift) ---
def f10rv_f10_realized_volatility_term_tsratioyoy_base_v145_signal(closeadj):
    ratio = _f10_rvol(closeadj, 21) / _f10_rvol(closeadj, 126).replace(0, np.nan)
    b = ratio - ratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- effective horizon of vol: window-weighted center of mass of the vol curve ---
def f10rv_f10_realized_volatility_term_volcom_base_v146_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    w = np.array([5.0, 21.0, 63.0, 126.0, 252.0])
    stk = pd.concat([v5, v21, v63, v126, v252], axis=1)
    num = (stk * w).sum(axis=1)
    den = stk.sum(axis=1).replace(0, np.nan)
    b = np.log((num / den).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized-vol entropy: dispersion of daily variance shares within a quarter ---
def f10rv_f10_realized_volatility_term_rventropy_63d_base_v147_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2

    def _ent(a):
        s = a.sum()
        if s <= 0:
            return np.nan
        p = a / s
        p = p[p > 0]
        return -(p * np.log(p)).sum() / np.log(len(a))

    b = r2.rolling(63, min_periods=21).apply(_ent, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol of vol-adjusted returns (stability of risk-adjusted performance) ---
def f10rv_f10_realized_volatility_term_riskadjvol_base_v148_signal(closeadj):
    r = _f10_logret(closeadj)
    sd = r.rolling(21, min_periods=10).std()
    ra = r / sd.replace(0, np.nan)
    b = ra.rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure curvature percentile vs its own history (cone of the butterfly) ---
def f10rv_f10_realized_volatility_term_curvrank_base_v149_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v252 = _f10_rvol(closeadj, 252)
    bf = ((v21 + v252) / 2.0 - v63) / v63.replace(0, np.nan)
    b = bf.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite term-structure stress: short-vol cone x backwardation depth ---
def f10rv_f10_realized_volatility_term_tsstress_base_v150_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v252 = _f10_rvol(closeadj, 252)
    cone = v21.rolling(252, min_periods=63).rank(pct=True) - 0.5
    backw = (v21 / v252.replace(0, np.nan) - 1.0).clip(lower=0)
    b = cone * (1.0 + backw)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_realized_volatility_term_rvol_10d_base_v076_signal,
    f10rv_f10_realized_volatility_term_rvol_42d_base_v077_signal,
    f10rv_f10_realized_volatility_term_rvol_189d_base_v078_signal,
    f10rv_f10_realized_volatility_term_rvol_504d_base_v079_signal,
    f10rv_f10_realized_volatility_term_tsratio_10v42_base_v080_signal,
    f10rv_f10_realized_volatility_term_tsratio_42v189_base_v081_signal,
    f10rv_f10_realized_volatility_term_tsratio_189v504_base_v082_signal,
    f10rv_f10_realized_volatility_term_tsratioz_10v252_base_v083_signal,
    f10rv_f10_realized_volatility_term_varratio_21d_base_v084_signal,
    f10rv_f10_realized_volatility_term_varratio_10d_base_v085_signal,
    f10rv_f10_realized_volatility_term_vrcurv_base_v086_signal,
    f10rv_f10_realized_volatility_term_rvconc_21d_base_v087_signal,
    f10rv_f10_realized_volatility_term_rvconc_63d_base_v088_signal,
    f10rv_f10_realized_volatility_term_rvherf_63d_base_v089_signal,
    f10rv_f10_realized_volatility_term_cone_10in252_base_v090_signal,
    f10rv_f10_realized_volatility_term_cone_42in504_base_v091_signal,
    f10rv_f10_realized_volatility_term_conemom_189in1260_base_v092_signal,
    f10rv_f10_realized_volatility_term_conestd_21in252_base_v093_signal,
    f10rv_f10_realized_volatility_term_dnsemicone_21in252_base_v094_signal,
    f10rv_f10_realized_volatility_term_upsemicone_21in252_base_v095_signal,
    f10rv_f10_realized_volatility_term_dnsemislope_21_126_base_v096_signal,
    f10rv_f10_realized_volatility_term_upsemislope_21_126_base_v097_signal,
    f10rv_f10_realized_volatility_term_semitsdiv_base_v098_signal,
    f10rv_f10_realized_volatility_term_volofvol_10in126_base_v099_signal,
    f10rv_f10_realized_volatility_term_volofvol_126in504_base_v100_signal,
    f10rv_f10_realized_volatility_term_volcv_63in504_base_v101_signal,
    f10rv_f10_realized_volatility_term_logvolofvol_21in252_base_v102_signal,
    f10rv_f10_realized_volatility_term_volar1_63d_base_v103_signal,
    f10rv_f10_realized_volatility_term_volar1_126d_base_v104_signal,
    f10rv_f10_realized_volatility_term_voldecay_63d_base_v105_signal,
    f10rv_f10_realized_volatility_term_ewts_10v63_base_v106_signal,
    f10rv_f10_realized_volatility_term_ewts_21v126_base_v107_signal,
    f10rv_f10_realized_volatility_term_ewmagap_63d_base_v108_signal,
    f10rv_f10_realized_volatility_term_volmom_21d_base_v109_signal,
    f10rv_f10_realized_volatility_term_volmom_126d_base_v110_signal,
    f10rv_f10_realized_volatility_term_volexpstreak_base_v111_signal,
    f10rv_f10_realized_volatility_term_extremeintensity_63d_base_v112_signal,
    f10rv_f10_realized_volatility_term_tailasym_63d_base_v113_signal,
    f10rv_f10_realized_volatility_term_compressage_base_v114_signal,
    f10rv_f10_realized_volatility_term_volseries_skew_base_v115_signal,
    f10rv_f10_realized_volatility_term_coneamp_63in1260_base_v116_signal,
    f10rv_f10_realized_volatility_term_curvecenter_base_v117_signal,
    f10rv_f10_realized_volatility_term_rolldown_base_v118_signal,
    f10rv_f10_realized_volatility_term_vadjret_42d_base_v119_signal,
    f10rv_f10_realized_volatility_term_vadjret_189d_base_v120_signal,
    f10rv_f10_realized_volatility_term_vadjret_slope_base_v121_signal,
    f10rv_f10_realized_volatility_term_sortino_21d_base_v122_signal,
    f10rv_f10_realized_volatility_term_madvol_21d_base_v123_signal,
    f10rv_f10_realized_volatility_term_madts_21v126_base_v124_signal,
    f10rv_f10_realized_volatility_term_medmad_63d_base_v125_signal,
    f10rv_f10_realized_volatility_term_iqrstd_126d_base_v126_signal,
    f10rv_f10_realized_volatility_term_semivargap_63d_base_v127_signal,
    f10rv_f10_realized_volatility_term_semivargapmom_base_v128_signal,
    f10rv_f10_realized_volatility_term_estgap_21d_base_v129_signal,
    f10rv_f10_realized_volatility_term_conemom_63in504_base_v130_signal,
    f10rv_f10_realized_volatility_term_coneslope_base_v131_signal,
    f10rv_f10_realized_volatility_term_volzgap_base_v132_signal,
    f10rv_f10_realized_volatility_term_var2dret_63d_base_v133_signal,
    f10rv_f10_realized_volatility_term_retac1_63d_base_v134_signal,
    f10rv_f10_realized_volatility_term_microvov_5in21_base_v135_signal,
    f10rv_f10_realized_volatility_term_volaccel_21d_base_v136_signal,
    f10rv_f10_realized_volatility_term_conebreach_21in252_base_v137_signal,
    f10rv_f10_realized_volatility_term_conefloordist_21in252_base_v138_signal,
    f10rv_f10_realized_volatility_term_volelast_base_v139_signal,
    f10rv_f10_realized_volatility_term_leverage_126d_base_v140_signal,
    f10rv_f10_realized_volatility_term_volafterdown_base_v141_signal,
    f10rv_f10_realized_volatility_term_voltrendstr_base_v142_signal,
    f10rv_f10_realized_volatility_term_volswing_63d_base_v143_signal,
    f10rv_f10_realized_volatility_term_volyoy_63d_base_v144_signal,
    f10rv_f10_realized_volatility_term_tsratioyoy_base_v145_signal,
    f10rv_f10_realized_volatility_term_volcom_base_v146_signal,
    f10rv_f10_realized_volatility_term_rventropy_63d_base_v147_signal,
    f10rv_f10_realized_volatility_term_riskadjvol_base_v148_signal,
    f10rv_f10_realized_volatility_term_curvrank_base_v149_signal,
    f10rv_f10_realized_volatility_term_tsstress_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_REALIZED_VOLATILITY_TERM_REGISTRY_076_150 = REGISTRY


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

    print("OK f10_realized_volatility_term_base_076_150_claude: %d features pass" % n_features)
