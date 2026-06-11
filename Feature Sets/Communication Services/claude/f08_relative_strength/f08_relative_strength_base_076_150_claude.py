import inspect
import numpy as np
import pandas as pd

# f08_relative_strength (f08rs) — Communication Services SASS signal features (076-150).
# TIGHTENED DOMAIN: SELF-RELATIVE *RISK-ADJUSTED* STRENGTH ONLY. This file emphasises
# risk-VIEW DISAGREEMENT and path-shape: cross-measure DIFFERENCES (Sterling vs Calmar,
# Omega vs Sharpe, pain-ratio vs Sterling, CVaR-adj vs Sortino — each cancels the common
# return component and isolates which risk lens a name is strong/weak under), plus genuinely
# orthogonal path-shape measures (time-above-water, tail-ratio, downside-share, recovery off
# own trough, conditional-drawdown-at-risk, standalone downside-deviation / avg-drawdown),
# all vs the stock's OWN 63/126/252/504/1260d history.
#   DO NOT compute Kaufman efficiency ratio / Hurst / autocorrelation (that is f03).
#   DO NOT compute raw ROC / 12-1 momentum LEVELS or rank-of-raw-ROC (that is f02).
#   DO NOT compute price-vs-MA / RS-ratio-vs-MA, or trend-slope-t-stat (that is f01/f03).
# Inputs: closeadj only. Windows >21d use closeadj (per SPEC).

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _iqr_ctr(s, w):
    med = s.rolling(w, min_periods=max(2, w // 2)).median()
    q1 = s.rolling(w, min_periods=max(2, w // 2)).quantile(0.25)
    q3 = s.rolling(w, min_periods=max(2, w // 2)).quantile(0.75)
    return (s - med) / (q3 - q1).replace(0, np.nan)


# ===== folder domain primitives (RISK-ADJUSTED self-relative strength) =====
def _f08rs_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f08rs_cumret(closeadj, w):
    return np.log(closeadj.replace(0, np.nan)) - np.log(closeadj.shift(w).replace(0, np.nan))


def _f08rs_sharpe(closeadj, w):
    lr = _f08rs_logret(closeadj)
    mu = lr.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return mu / sd.replace(0, np.nan) * np.sqrt(252.0)


def _f08rs_sortino(closeadj, w):
    lr = _f08rs_logret(closeadj)
    mu = lr.rolling(w, min_periods=max(2, w // 2)).mean()
    down = lr.where(lr < 0, 0.0)
    dd = np.sqrt((down ** 2).rolling(w, min_periods=max(2, w // 2)).mean())
    return mu / dd.replace(0, np.nan) * np.sqrt(252.0)


def _f08rs_underwater(closeadj, w):
    peak = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return closeadj / peak.replace(0, np.nan) - 1.0


def _f08rs_maxdd(closeadj, w):
    uw = _f08rs_underwater(closeadj, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).max()


def _f08rs_avgdd(closeadj, w):
    # average drawdown depth over w (positive) — Sterling denominator
    uw = _f08rs_underwater(closeadj, w)
    return (-uw).rolling(w, min_periods=max(1, w // 2)).mean()


def _f08rs_ulcer(closeadj, w):
    uw = _f08rs_underwater(closeadj, w)
    return np.sqrt((uw ** 2).rolling(w, min_periods=max(1, w // 2)).mean())


def _f08rs_cdar(closeadj, w):
    # conditional drawdown at risk: mean of underwater depths at/above their own 75th pct,
    # computed densely as sum-of-tail-depths / count-of-tail to avoid NaN sparsity.
    uw = (-_f08rs_underwater(closeadj, w))
    thr = uw.rolling(w, min_periods=max(2, w // 2)).quantile(0.75)
    above = (uw >= thr)
    tail_sum = (uw.where(above, 0.0)).rolling(w, min_periods=max(2, w // 2)).sum()
    tail_cnt = above.astype(float).rolling(w, min_periods=max(2, w // 2)).sum()
    return tail_sum / tail_cnt.replace(0, np.nan)


def _f08rs_calmar(closeadj, w):
    return _f08rs_cumret(closeadj, w) / _f08rs_maxdd(closeadj, w).replace(0, np.nan)


def _f08rs_martin(closeadj, w):
    return _f08rs_cumret(closeadj, w) / _f08rs_ulcer(closeadj, w).replace(0, np.nan)


def _f08rs_sterling(closeadj, w):
    return _f08rs_cumret(closeadj, w) / _f08rs_avgdd(closeadj, w).replace(0, np.nan)


def _f08rs_painratio(closeadj, w):
    # pain ratio: net return per unit of conditional drawdown at risk
    return _f08rs_cumret(closeadj, w) / _f08rs_cdar(closeadj, w).replace(0, np.nan)


def _f08rs_omega(closeadj, w):
    lr = _f08rs_logret(closeadj)
    up = lr.clip(lower=0).rolling(w, min_periods=max(2, w // 2)).sum()
    dn = lr.clip(upper=0).abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return up / dn.replace(0, np.nan)


def _f08rs_downdev(closeadj, w):
    lr = _f08rs_logret(closeadj)
    down = lr.where(lr < 0, 0.0)
    return np.sqrt((down ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * np.sqrt(252.0)


def _f08rs_downdevadj(closeadj, w):
    return _f08rs_cumret(closeadj, w) / _f08rs_downdev(closeadj, w).replace(0, np.nan)


def _f08rs_cvaradj(closeadj, w):
    lr = _f08rs_logret(closeadj)
    cvar = (-lr).rolling(w, min_periods=max(2, w // 2)).quantile(0.95)
    return _f08rs_cumret(closeadj, w) / cvar.replace(0, np.nan)


def _f08rs_tailratio(closeadj, w):
    lr = _f08rs_logret(closeadj)
    hi = lr.rolling(w, min_periods=max(2, w // 2)).quantile(0.95)
    lo = lr.rolling(w, min_periods=max(2, w // 2)).quantile(0.05)
    return hi / (-lo).replace(0, np.nan)


def _f08rs_timeabovewater(closeadj, w):
    # PATH-SHAPE strength (no return numerator): time spent near own running peak, penalised
    # by typical drawdown depth. Orthogonal to all return/risk ratios and to slope-t-stat.
    uw = _f08rs_underwater(closeadj, w)
    near = (uw >= -0.005).astype(float).rolling(w, min_periods=max(2, w // 2)).mean()
    depth = (-uw).rolling(w, min_periods=max(2, w // 2)).mean()
    return near - 5.0 * depth


# ============================================================
# === CROSS-MEASURE RISK-VIEW DIFFERENCES (cancel return, isolate the risk lens) ===
# Sterling minus Calmar rank 252d (avg-drawdown vs single-worst-drawdown view)
def f08rs_f08_relative_strength_sterlingcalmardiff_252d_base_v076_signal(closeadj):
    b = _rank(_f08rs_sterling(closeadj, 252), 504) - _rank(_f08rs_calmar(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling minus Martin rank 504d (avg-drawdown vs ulcer view, deep)
def f08rs_f08_relative_strength_sterlingmartindiff_504d_base_v077_signal(closeadj):
    b = _rank(_f08rs_sterling(closeadj, 504), 1260) - _rank(_f08rs_martin(closeadj, 504), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-ratio minus Sterling rank 252d (conditional-DD-at-risk vs avg-drawdown view)
def f08rs_f08_relative_strength_painsterlingdiff_252d_base_v078_signal(closeadj):
    b = _rank(_f08rs_painratio(closeadj, 252), 504) - _rank(_f08rs_sterling(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega minus Sharpe rank 252d (whole-distribution gain/loss vs vol view)
def f08rs_f08_relative_strength_omegasharpediff_252d_base_v079_signal(closeadj):
    b = _rank(_f08rs_omega(closeadj, 252), 504) - _rank(_f08rs_sharpe(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega minus Sortino rank 126d (gain/loss vs downside-deviation view, fast)
def f08rs_f08_relative_strength_omegasortinodiff_126d_base_v080_signal(closeadj):
    b = _rank(_f08rs_omega(closeadj, 126), 504) - _rank(_f08rs_sortino(closeadj, 126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CVaR-adjusted minus Sortino rank 252d (worst-tail vs semi-deviation view)
def f08rs_f08_relative_strength_cvarsortinodiff_252d_base_v081_signal(closeadj):
    b = _rank(_f08rs_cvaradj(closeadj, 252), 504) - _rank(_f08rs_sortino(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CVaR-adjusted minus Calmar rank 504d (worst-daily-tail vs worst-drawdown view, deep)
def f08rs_f08_relative_strength_cvarcalmardiff_504d_base_v082_signal(closeadj):
    b = _rank(_f08rs_cvaradj(closeadj, 504), 1260) - _rank(_f08rs_calmar(closeadj, 504), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downdev-adjusted minus Omega rank 252d (semi-deviation vs gain/loss view)
def f08rs_f08_relative_strength_downdevomegadiff_252d_base_v083_signal(closeadj):
    b = _rank(_f08rs_downdevadj(closeadj, 252), 504) - _rank(_f08rs_omega(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-ratio (CDaR) minus Omega rank 252d (tail-conditional-drawdown vs gain/loss view)
def f08rs_f08_relative_strength_painmartindiff_252d_base_v084_signal(closeadj):
    b = _rank(_f08rs_painratio(closeadj, 252), 504) - _rank(_f08rs_omega(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-ratio minus Omega rank 252d (extreme-tail asymmetry vs whole-distribution gain/loss)
def f08rs_f08_relative_strength_tailomegadiff_252d_base_v085_signal(closeadj):
    b = _rank(_f08rs_tailratio(closeadj, 252), 504) - _rank(_f08rs_omega(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === STANDALONE PAIN / PATH-SHAPE COMPONENTS (no return numerator -> orthogonal) ===
# conditional drawdown at risk over 252d, ranked & negated (shallow tail-DD = strength)
def f08rs_f08_relative_strength_cdarstrength_252d_base_v086_signal(closeadj):
    b = -_rank(_f08rs_cdar(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average drawdown over 504d, ranked & negated (shallow typical drawdown = strength)
def f08rs_f08_relative_strength_avgddstrength_504d_base_v087_signal(closeadj):
    b = -_rank(_f08rs_avgdd(closeadj, 504), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside deviation over 252d, ranked & negated (low semi-risk = strength)
def f08rs_f08_relative_strength_downdevstrength_252d_base_v088_signal(closeadj):
    b = -_rank(_f08rs_downdev(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-shape ratio 252d: ulcer (RMS) over avg-drawdown (how tail-skewed the pain is)
def f08rs_f08_relative_strength_painshape_252d_base_v089_signal(closeadj):
    b = (_f08rs_ulcer(closeadj, 252) / _f08rs_avgdd(closeadj, 252).replace(0, np.nan)) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === TIME-ABOVE-WATER (path-shape) family ===
# time-above-water minus Sharpe rank 252d (pure path-shape vs vol-adjusted-return view)
def f08rs_f08_relative_strength_taw_252d_base_v090_signal(closeadj):
    b = _rank(_f08rs_timeabovewater(closeadj, 252), 504) - _rank(_f08rs_sharpe(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water over 126d ranked vs own 504d history (fast path-shape leadership)
def f08rs_f08_relative_strength_tawrank_126d_base_v091_signal(closeadj):
    b = _rank(_f08rs_timeabovewater(closeadj, 126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water horizon spread 126d minus 252d (path-shape horizon tilt)
def f08rs_f08_relative_strength_tawspr_base_v092_signal(closeadj):
    b = _f08rs_timeabovewater(closeadj, 126) - _f08rs_timeabovewater(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water over 504d (long-horizon path-shape strength)
def f08rs_f08_relative_strength_taw_504d_base_v093_signal(closeadj):
    b = _f08rs_timeabovewater(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water robust extremity vs own 504d IQR
def f08rs_f08_relative_strength_tawiqr_base_v094_signal(closeadj):
    b = _iqr_ctr(_f08rs_timeabovewater(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water change over a quarter (path-shape velocity)
def f08rs_f08_relative_strength_tawmom_base_v095_signal(closeadj):
    t = _f08rs_timeabovewater(closeadj, 252)
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === TAIL-RATIO family (return-tail asymmetry) ===
# return tail ratio over 252d (upside tail / downside tail of daily returns)
def f08rs_f08_relative_strength_tailratio_252d_base_v096_signal(closeadj):
    b = _f08rs_tailratio(closeadj, 252).clip(0, 5) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail ratio over 126d ranked vs own 504d distribution (fast tail-asymmetry rank)
def f08rs_f08_relative_strength_tailratiorank_base_v097_signal(closeadj):
    b = _rank(_f08rs_tailratio(closeadj, 126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail ratio change over a quarter (shift in upside/downside tail balance)
def f08rs_f08_relative_strength_tailratiomom_base_v098_signal(closeadj):
    t = _f08rs_tailratio(closeadj, 252).clip(0, 5)
    b = t - t.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail ratio robust extremity vs own 504d IQR
def f08rs_f08_relative_strength_tailratioiqr_base_v099_signal(closeadj):
    b = _iqr_ctr(_f08rs_tailratio(closeadj, 252).clip(0, 5), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === RECOVERY-STRENGTH family (climb off own underwater trough) ===
# recovery strength 252d: current underwater minus own 252d deepest underwater
def f08rs_f08_relative_strength_recov_252d_base_v100_signal(closeadj):
    uw = _f08rs_underwater(closeadj, 252)
    b = uw - uw.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery strength 504d ranked vs own 1260d distribution (deep recovery rank)
def f08rs_f08_relative_strength_recovrank_base_v101_signal(closeadj):
    uw = _f08rs_underwater(closeadj, 504)
    rec = uw - uw.rolling(504, min_periods=252).min()
    b = _rank(rec, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery strength change over a quarter (acceleration of climb off own trough)
def f08rs_f08_relative_strength_recovmom_base_v102_signal(closeadj):
    uw = _f08rs_underwater(closeadj, 252)
    rec = uw - uw.rolling(252, min_periods=126).min()
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === DOWNSIDE-SHARE family (risk asymmetry, return-independent) ===
# downside-variance share over 252d ranked vs own 504d, negated (low downside-share = strength)
def f08rs_f08_relative_strength_downshare_504d_base_v103_signal(closeadj):
    lr = _f08rs_logret(closeadj)
    dvar = (lr.where(lr < 0, 0.0) ** 2).rolling(252, min_periods=126).mean()
    tvar = (lr ** 2).rolling(252, min_periods=126).mean()
    sh = dvar / tvar.replace(0, np.nan)
    b = -_rank(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-share change over a quarter (rotation in risk asymmetry)
def f08rs_f08_relative_strength_downsharemom_base_v104_signal(closeadj):
    lr = _f08rs_logret(closeadj)
    dvar = (lr.where(lr < 0, 0.0) ** 2).rolling(252, min_periods=126).mean()
    tvar = (lr ** 2).rolling(252, min_periods=126).mean()
    sh = dvar / tvar.replace(0, np.nan)
    b = sh - sh.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === DEEP RANKS of the difference families ===
# time-above-water deep rank: 252d path-shape strength ranked vs own 1260d
def f08rs_f08_relative_strength_tawdeeprank_base_v105_signal(closeadj):
    b = _rank(_f08rs_timeabovewater(closeadj, 252), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega minus Sharpe deep rank 504d (gain/loss vs vol, deep horizon)
def f08rs_f08_relative_strength_omegasharpedeep_base_v106_signal(closeadj):
    b = _rank(_f08rs_omega(closeadj, 504), 1260) - _rank(_f08rs_sharpe(closeadj, 504), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling minus pain-ratio rank 252d, curvature over quarters (which-pain-dominates bend)
def f08rs_f08_relative_strength_painviewcurv_base_v107_signal(closeadj):
    d = _rank(_f08rs_sterling(closeadj, 252), 504) - _rank(_f08rs_painratio(closeadj, 252), 504)
    b = d - 2.0 * d.shift(42) + d.shift(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water rank velocity over a quarter (path-shape leadership velocity)
def f08rs_f08_relative_strength_tawrankvel_base_v108_signal(closeadj):
    r = _rank(_f08rs_timeabovewater(closeadj, 252), 504)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling minus Martin smoothed-median gap 252d (avg-DD vs ulcer persistent-extremity gap)
def f08rs_f08_relative_strength_sterlingctr_base_v109_signal(closeadj):
    s = _f08rs_sterling(closeadj, 252).clip(-30, 30)
    ssm = s.ewm(span=42, min_periods=21).mean()
    sc = ssm - ssm.rolling(252, min_periods=126).median()
    m = _f08rs_martin(closeadj, 252).clip(-80, 80)
    msm = m.ewm(span=42, min_periods=21).mean()
    mc = msm - msm.rolling(252, min_periods=126).median()
    b = sc - mc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega minus Sharpe regime: gain/loss band position MINUS vol band position over 504d
def f08rs_f08_relative_strength_omegasharperegime_base_v110_signal(closeadj):
    def _band(x):
        q25 = x.rolling(504, min_periods=252).quantile(0.25)
        q75 = x.rolling(504, min_periods=252).quantile(0.75)
        return (x - q25) / (q75 - q25).replace(0, np.nan)
    b = _band(_f08rs_omega(closeadj, 252)) - _band(_f08rs_sharpe(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water minus Calmar regime-time gap (path-shape vs drawdown-adj up-regime contrast)
def f08rs_f08_relative_strength_tawposfrac_base_v111_signal(closeadj):
    t = _f08rs_timeabovewater(closeadj, 126)
    tfrac = (t > t.rolling(252, min_periods=126).median()).astype(float).rolling(252, min_periods=126).mean()
    c = _f08rs_calmar(closeadj, 126).clip(-20, 20)
    cfrac = (c > c.rolling(252, min_periods=126).median()).astype(float).rolling(252, min_periods=126).mean()
    b = tfrac - cfrac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === BOUNDED differences ===
# tanh(Sterling) minus tanh(Calmar) over 252d (bounded avg-DD vs worst-DD view)
def f08rs_f08_relative_strength_sterlingcalmartanh_base_v112_signal(closeadj):
    b = np.tanh(_f08rs_sterling(closeadj, 252) / 5.0) - np.tanh(_f08rs_calmar(closeadj, 252) / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh(Omega-1) minus tanh(Sortino) over 252d (bounded gain/loss vs downside-dev view)
def f08rs_f08_relative_strength_omegasortinotanh_base_v113_signal(closeadj):
    b = np.tanh(_f08rs_omega(closeadj, 252) - 1.0) - np.tanh(_f08rs_sortino(closeadj, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === SMOOTHED-RANK durability of difference families ===
# Sterling-minus-Calmar rank smoothed over 504d (durable which-DD-view leadership)
def f08rs_f08_relative_strength_sterlingcalmarsmrank_base_v114_signal(closeadj):
    d = _f08rs_sterling(closeadj, 252) - _f08rs_calmar(closeadj, 252).clip(-20, 20)
    sm = d.ewm(span=42, min_periods=21).mean()
    b = _rank(sm, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega-minus-Sortino smoothed minus own median (persistent gain/loss-vs-downside extremity)
def f08rs_f08_relative_strength_omegasortinoctr_base_v115_signal(closeadj):
    d = (_f08rs_omega(closeadj, 252).clip(0, 5)) - np.tanh(_f08rs_sortino(closeadj, 252))
    sm = d.ewm(span=42, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === STABILITY ===
# time-above-water rank stability: negative std of 126d TAW rank over 126d (steady path-shape)
def f08rs_f08_relative_strength_tawstab_base_v116_signal(closeadj):
    r = _rank(_f08rs_timeabovewater(closeadj, 126), 252)
    b = -r.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === YEAR-OVER-YEAR of difference families ===
# Sterling-minus-Calmar rank year-over-year change (which-DD-view annual drift)
def f08rs_f08_relative_strength_sterlingcalmaryoy_base_v117_signal(closeadj):
    d = _rank(_f08rs_sterling(closeadj, 252), 504) - _rank(_f08rs_calmar(closeadj, 252), 504)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water year-over-year change (path-shape annual drift)
def f08rs_f08_relative_strength_tawyoy_base_v118_signal(closeadj):
    t = _f08rs_timeabovewater(closeadj, 252)
    b = t - t.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === PEAK-GAP / trough-gap of difference & path families ===
# time-above-water curvature: 2nd-difference of 252d TAW over quarters (path-shape bend)
def f08rs_f08_relative_strength_tawpeakgap_base_v119_signal(closeadj):
    t = _f08rs_timeabovewater(closeadj, 252)
    b = t - 2.0 * t.shift(42) + t.shift(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega-minus-Sharpe recovery-from-trough: current rank-diff above own trailing 504d min
def f08rs_f08_relative_strength_omegasharpetrough_base_v120_signal(closeadj):
    d = _rank(_f08rs_omega(closeadj, 252), 504) - _rank(_f08rs_sharpe(closeadj, 252), 504)
    trough = d.rolling(504, min_periods=252).min()
    b = d - trough
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === BLENDS / dispersion of the risk-view differences ===
# blended risk-view-difference: mean of (Sterling-Calmar, Omega-Sharpe, pain-Sterling) ranks
def f08rs_f08_relative_strength_viewdiffblend_base_v121_signal(closeadj):
    d1 = _rank(_f08rs_sterling(closeadj, 252), 504) - _rank(_f08rs_calmar(closeadj, 252), 504)
    d2 = _rank(_f08rs_omega(closeadj, 252), 504) - _rank(_f08rs_sharpe(closeadj, 252), 504)
    d3 = _rank(_f08rs_painratio(closeadj, 252), 504) - _rank(_f08rs_sterling(closeadj, 252), 504)
    b = (d1 + d2 + d3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of risk-adjusted ranks across MEASURES at 252d (how much the lens matters)
def f08rs_f08_relative_strength_lensdisp_base_v122_signal(closeadj):
    r1 = _rank(_f08rs_sterling(closeadj, 252), 504)
    r2 = _rank(_f08rs_omega(closeadj, 252), 504)
    r3 = _rank(_f08rs_cvaradj(closeadj, 252), 504)
    r4 = _rank(_f08rs_painratio(closeadj, 252), 504)
    b = pd.concat([r1, r2, r3, r4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# horizon dispersion of time-above-water across 63/126/252/504 (path-shape horizon disagreement)
def f08rs_f08_relative_strength_tawhorizdisp_base_v123_signal(closeadj):
    cols = [_f08rs_timeabovewater(closeadj, w) for w in (63, 126, 252, 504)]
    b = pd.concat(cols, axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === MORE distinct difference facets ===
# downdev-adjusted minus CVaR-adjusted rank 252d (semi-deviation vs worst-tail view)
def f08rs_f08_relative_strength_downdevcvardiff_base_v124_signal(closeadj):
    b = _rank(_f08rs_downdevadj(closeadj, 252), 504) - _rank(_f08rs_cvaradj(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling minus Omega rank 126d (avg-drawdown vs gain/loss view, fast)
def f08rs_f08_relative_strength_sterlingomegadiff_126d_base_v125_signal(closeadj):
    b = _rank(_f08rs_sterling(closeadj, 126), 504) - _rank(_f08rs_omega(closeadj, 126), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling x Omega joint conviction (sign agreement x min bounded magnitude)
def f08rs_f08_relative_strength_sterlingomegajoint_base_v126_signal(closeadj):
    s = _f08rs_sterling(closeadj, 252).clip(-30, 30)
    o = _f08rs_omega(closeadj, 252).clip(0, 5) - 1.0
    agree = np.sign(s) * np.sign(o)
    mag = pd.concat([(s / 5.0).abs(), o.abs()], axis=1).min(axis=1)
    b = agree * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega-minus-Sortino regime velocity (gain/loss-vs-downside band rotation over a quarter)
def f08rs_f08_relative_strength_omegasortinoregimevel_base_v127_signal(closeadj):
    def _band(x):
        q25 = x.rolling(504, min_periods=252).quantile(0.25)
        q75 = x.rolling(504, min_periods=252).quantile(0.75)
        return (x - q25) / (q75 - q25).replace(0, np.nan)
    d = _band(_f08rs_omega(closeadj, 252)) - _band(_f08rs_sortino(closeadj, 252))
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pain-ratio minus Sterling rank velocity (tail-DD-vs-avg-DD rotation over a quarter)
def f08rs_f08_relative_strength_painsterlingvel_base_v128_signal(closeadj):
    d = _rank(_f08rs_painratio(closeadj, 252), 504) - _rank(_f08rs_sterling(closeadj, 252), 504)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast time-above-water rank over 63d vs own 252d (very-fast path-shape leadership)
def f08rs_f08_relative_strength_fasttawrank_base_v129_signal(closeadj):
    b = _rank(_f08rs_timeabovewater(closeadj, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery strength fraction-of-year above own median (sustained climb-off-trough time)
def f08rs_f08_relative_strength_recovposfrac_base_v130_signal(closeadj):
    uw = _f08rs_underwater(closeadj, 126)
    rec = uw - uw.rolling(126, min_periods=63).min()
    med = rec.rolling(252, min_periods=126).median()
    above = (rec > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino/Sharpe ratio rank minus downdev-strength rank 252d (asymmetry-multiplier vs raw semi-risk)
def f08rs_f08_relative_strength_downasym_504d_base_v131_signal(closeadj):
    ratio = (_f08rs_sortino(closeadj, 252) / _f08rs_sharpe(closeadj, 252).replace(0, np.nan)).clip(-3, 3)
    b = _rank(ratio, 504) - (-_rank(_f08rs_downdev(closeadj, 252), 504))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CVaR-adjusted minus downdev-adjusted IQR-robust gap (worst-tail vs semi-deviation extremity)
def f08rs_f08_relative_strength_cvardowndeviqr_base_v132_signal(closeadj):
    c = _iqr_ctr(_f08rs_cvaradj(closeadj, 252).clip(-30, 30), 504)
    d = _iqr_ctr(_f08rs_downdevadj(closeadj, 252), 504)
    b = c - d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling minus time-above-water rank 252d (return/avg-DD vs pure path-shape view)
def f08rs_f08_relative_strength_sterlingtawdiff_base_v133_signal(closeadj):
    b = _rank(_f08rs_sterling(closeadj, 252), 504) - _rank(_f08rs_timeabovewater(closeadj, 252), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-ratio minus downside-share rank 252d (extreme-tail asymmetry vs whole-variance asymmetry)
def f08rs_f08_relative_strength_taildownsharediff_base_v134_signal(closeadj):
    lr = _f08rs_logret(closeadj)
    dvar = (lr.where(lr < 0, 0.0) ** 2).rolling(252, min_periods=126).mean()
    tvar = (lr ** 2).rolling(252, min_periods=126).mean()
    dshare = dvar / tvar.replace(0, np.nan)
    b = _rank(_f08rs_tailratio(closeadj, 252), 504) - _rank(-dshare, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling minus Calmar trend-to-noise (which-DD-view trend over its own dispersion)
def f08rs_f08_relative_strength_viewtrendnoise_base_v135_signal(closeadj):
    d = _rank(_f08rs_sterling(closeadj, 252), 504) - _rank(_f08rs_calmar(closeadj, 252), 504)
    slope = d - d.shift(42)
    noise = d.diff().abs().rolling(63, min_periods=21).mean()
    b = slope / noise.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CVaR-adjusted change over a half-year (worst-tail-adjusted medium-horizon drift)
def f08rs_f08_relative_strength_cvarmom_base_v136_signal(closeadj):
    c = _f08rs_cvaradj(closeadj, 252).clip(-30, 30)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega-minus-Sharpe deep rank vs 1260d minus pain-Sterling deep (multi-lens deep contrast)
def f08rs_f08_relative_strength_deeplenscontrast_base_v137_signal(closeadj):
    d1 = _rank(_f08rs_omega(closeadj, 504), 1260) - _rank(_f08rs_sharpe(closeadj, 504), 1260)
    d2 = _rank(_f08rs_painratio(closeadj, 504), 1260) - _rank(_f08rs_sterling(closeadj, 504), 1260)
    b = d1 - d2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water smoothed minus own 252d median (persistent path-shape extremity)
def f08rs_f08_relative_strength_tawdeepvel_base_v138_signal(closeadj):
    t = _f08rs_timeabovewater(closeadj, 252)
    sm = t.ewm(span=42, min_periods=21).mean()
    b = sm - sm.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year in top-quartile time-above-water rank (sustained path-shape lead)
def f08rs_f08_relative_strength_tawtopq_base_v139_signal(closeadj):
    r = _rank(_f08rs_timeabovewater(closeadj, 126), 252) + 0.5
    top = (r >= 0.75).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year Omega-beats-Sharpe (gain/loss lens dominates vol lens regime-time)
def f08rs_f08_relative_strength_omegawinsfrac_base_v140_signal(closeadj):
    win = (_rank(_f08rs_omega(closeadj, 126), 252) > _rank(_f08rs_sharpe(closeadj, 126), 252)).astype(float)
    b = win.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max-drawdown over 504d in own-vol units, change over a quarter (vol-scaled drawdown velocity)
def f08rs_f08_relative_strength_ddvolunitsmom_base_v141_signal(closeadj):
    mdd = _f08rs_maxdd(closeadj, 504)
    vol = _f08rs_logret(closeadj).rolling(126, min_periods=63).std() * np.sqrt(252.0)
    raw = -mdd / vol.replace(0, np.nan)
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# conditional-DD-at-risk velocity over a quarter, negated (tail-drawdown healing)
def f08rs_f08_relative_strength_cdarmom_base_v142_signal(closeadj):
    cd = _f08rs_cdar(closeadj, 126)
    b = -(cd - cd.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# === COMPOSITES ===
# pain-lens contrast composite: conditional-DD strength MINUS gain/loss (Omega) strength rank
def f08rs_f08_relative_strength_paincomposite_base_v143_signal(closeadj):
    pain = -_rank(_f08rs_cdar(closeadj, 252), 504)
    omega = _rank(_f08rs_omega(closeadj, 252), 504)
    b = pain - omega
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep durable path-shape composite: TAW deep rank + recovery + shallow-downdev, contrast-weighted
def f08rs_f08_relative_strength_deepdurable_base_v144_signal(closeadj):
    taw = _rank(_f08rs_timeabovewater(closeadj, 504), 1260)
    uw = _f08rs_underwater(closeadj, 504)
    rec = _rank(uw - uw.rolling(504, min_periods=252).min(), 1260)
    dd = -_rank(_f08rs_downdev(closeadj, 252), 504)
    b = taw + 0.5 * rec + 0.5 * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega minus Sharpe bounded gap over 504d (gain/loss vs vol lens, long bounded; cancels return)
def f08rs_f08_relative_strength_sterlingomegatanh_504d_base_v145_signal(closeadj):
    o = np.tanh(_f08rs_omega(closeadj, 504) - 1.0)
    s = np.tanh(_f08rs_sharpe(closeadj, 504))
    b = o - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# time-above-water fraction-of-2y above own deep median (deep path-shape up-regime time)
def f08rs_f08_relative_strength_tawregime_base_v146_signal(closeadj):
    t = _f08rs_timeabovewater(closeadj, 252)
    med = t.rolling(1260, min_periods=504).median()
    above = (t > med).astype(float)
    b = above.rolling(504, min_periods=252).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-ratio year-over-year change (tail-asymmetry annual drift)
def f08rs_f08_relative_strength_tailratioyoy_base_v147_signal(closeadj):
    t = _f08rs_tailratio(closeadj, 252).clip(0, 5)
    b = t - t.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CVaR-minus-Calmar change over a quarter (worst-daily-tail-vs-worst-drawdown velocity)
def f08rs_f08_relative_strength_painmartinvel_base_v148_signal(closeadj):
    d = _rank(_f08rs_cvaradj(closeadj, 252), 504) - _rank(_f08rs_calmar(closeadj, 252), 504)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery-strength minus drawdown-depth contrast 252d (climbing vs still-deep)
def f08rs_f08_relative_strength_recovcontrast_base_v149_signal(closeadj):
    uw = _f08rs_underwater(closeadj, 252)
    rec = _rank(uw - uw.rolling(252, min_periods=126).min(), 504)
    depth = -_rank(_f08rs_maxdd(closeadj, 252), 504)
    b = rec - depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling deep-rank velocity: change in 252d-over-1260d Sterling rank over a quarter
def f08rs_f08_relative_strength_sterlingdeepvel_base_v150_signal(closeadj):
    r = _rank(_f08rs_sterling(closeadj, 252), 1260)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08rs_f08_relative_strength_sterlingcalmardiff_252d_base_v076_signal,
    f08rs_f08_relative_strength_sterlingmartindiff_504d_base_v077_signal,
    f08rs_f08_relative_strength_painsterlingdiff_252d_base_v078_signal,
    f08rs_f08_relative_strength_omegasharpediff_252d_base_v079_signal,
    f08rs_f08_relative_strength_omegasortinodiff_126d_base_v080_signal,
    f08rs_f08_relative_strength_cvarsortinodiff_252d_base_v081_signal,
    f08rs_f08_relative_strength_cvarcalmardiff_504d_base_v082_signal,
    f08rs_f08_relative_strength_downdevomegadiff_252d_base_v083_signal,
    f08rs_f08_relative_strength_painmartindiff_252d_base_v084_signal,
    f08rs_f08_relative_strength_tailomegadiff_252d_base_v085_signal,
    f08rs_f08_relative_strength_cdarstrength_252d_base_v086_signal,
    f08rs_f08_relative_strength_avgddstrength_504d_base_v087_signal,
    f08rs_f08_relative_strength_downdevstrength_252d_base_v088_signal,
    f08rs_f08_relative_strength_painshape_252d_base_v089_signal,
    f08rs_f08_relative_strength_taw_252d_base_v090_signal,
    f08rs_f08_relative_strength_tawrank_126d_base_v091_signal,
    f08rs_f08_relative_strength_tawspr_base_v092_signal,
    f08rs_f08_relative_strength_taw_504d_base_v093_signal,
    f08rs_f08_relative_strength_tawiqr_base_v094_signal,
    f08rs_f08_relative_strength_tawmom_base_v095_signal,
    f08rs_f08_relative_strength_tailratio_252d_base_v096_signal,
    f08rs_f08_relative_strength_tailratiorank_base_v097_signal,
    f08rs_f08_relative_strength_tailratiomom_base_v098_signal,
    f08rs_f08_relative_strength_tailratioiqr_base_v099_signal,
    f08rs_f08_relative_strength_recov_252d_base_v100_signal,
    f08rs_f08_relative_strength_recovrank_base_v101_signal,
    f08rs_f08_relative_strength_recovmom_base_v102_signal,
    f08rs_f08_relative_strength_downshare_504d_base_v103_signal,
    f08rs_f08_relative_strength_downsharemom_base_v104_signal,
    f08rs_f08_relative_strength_tawdeeprank_base_v105_signal,
    f08rs_f08_relative_strength_omegasharpedeep_base_v106_signal,
    f08rs_f08_relative_strength_painviewcurv_base_v107_signal,
    f08rs_f08_relative_strength_tawrankvel_base_v108_signal,
    f08rs_f08_relative_strength_sterlingctr_base_v109_signal,
    f08rs_f08_relative_strength_omegasharperegime_base_v110_signal,
    f08rs_f08_relative_strength_tawposfrac_base_v111_signal,
    f08rs_f08_relative_strength_sterlingcalmartanh_base_v112_signal,
    f08rs_f08_relative_strength_omegasortinotanh_base_v113_signal,
    f08rs_f08_relative_strength_sterlingcalmarsmrank_base_v114_signal,
    f08rs_f08_relative_strength_omegasortinoctr_base_v115_signal,
    f08rs_f08_relative_strength_tawstab_base_v116_signal,
    f08rs_f08_relative_strength_sterlingcalmaryoy_base_v117_signal,
    f08rs_f08_relative_strength_tawyoy_base_v118_signal,
    f08rs_f08_relative_strength_tawpeakgap_base_v119_signal,
    f08rs_f08_relative_strength_omegasharpetrough_base_v120_signal,
    f08rs_f08_relative_strength_viewdiffblend_base_v121_signal,
    f08rs_f08_relative_strength_lensdisp_base_v122_signal,
    f08rs_f08_relative_strength_tawhorizdisp_base_v123_signal,
    f08rs_f08_relative_strength_downdevcvardiff_base_v124_signal,
    f08rs_f08_relative_strength_sterlingomegadiff_126d_base_v125_signal,
    f08rs_f08_relative_strength_sterlingomegajoint_base_v126_signal,
    f08rs_f08_relative_strength_omegasortinoregimevel_base_v127_signal,
    f08rs_f08_relative_strength_painsterlingvel_base_v128_signal,
    f08rs_f08_relative_strength_fasttawrank_base_v129_signal,
    f08rs_f08_relative_strength_recovposfrac_base_v130_signal,
    f08rs_f08_relative_strength_downasym_504d_base_v131_signal,
    f08rs_f08_relative_strength_cvardowndeviqr_base_v132_signal,
    f08rs_f08_relative_strength_sterlingtawdiff_base_v133_signal,
    f08rs_f08_relative_strength_taildownsharediff_base_v134_signal,
    f08rs_f08_relative_strength_viewtrendnoise_base_v135_signal,
    f08rs_f08_relative_strength_cvarmom_base_v136_signal,
    f08rs_f08_relative_strength_deeplenscontrast_base_v137_signal,
    f08rs_f08_relative_strength_tawdeepvel_base_v138_signal,
    f08rs_f08_relative_strength_tawtopq_base_v139_signal,
    f08rs_f08_relative_strength_omegawinsfrac_base_v140_signal,
    f08rs_f08_relative_strength_ddvolunitsmom_base_v141_signal,
    f08rs_f08_relative_strength_cdarmom_base_v142_signal,
    f08rs_f08_relative_strength_paincomposite_base_v143_signal,
    f08rs_f08_relative_strength_deepdurable_base_v144_signal,
    f08rs_f08_relative_strength_sterlingomegatanh_504d_base_v145_signal,
    f08rs_f08_relative_strength_tawregime_base_v146_signal,
    f08rs_f08_relative_strength_tailratioyoy_base_v147_signal,
    f08rs_f08_relative_strength_painmartinvel_base_v148_signal,
    f08rs_f08_relative_strength_recovcontrast_base_v149_signal,
    f08rs_f08_relative_strength_sterlingdeepvel_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RELATIVE_STRENGTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
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

    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    cols = {"closeadj": closeadj}

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

    print("OK f08_relative_strength_base_076_150_claude: %d features pass" % n_features)
