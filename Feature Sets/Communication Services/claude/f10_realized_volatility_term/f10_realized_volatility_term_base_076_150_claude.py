import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
ANN = np.sqrt(252.0)


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


# ===== folder domain primitives (realized-volatility term structure) =====
def _f10_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f10_rvol(closeadj, w):
    r = _f10_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std() * ANN


def _f10_downside(closeadj, w):
    r = _f10_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * ANN


def _f10_upside(closeadj, w):
    r = _f10_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * ANN


def _f10_term_ratio(closeadj, ws, wl):
    return _f10_rvol(closeadj, ws) / _f10_rvol(closeadj, wl).replace(0, np.nan)


def _f10_voladj_ret(closeadj, w):
    r = _f10_logret(closeadj)
    cum = r.rolling(w, min_periods=max(2, w // 2)).sum()
    v = _f10_rvol(closeadj, w)
    return cum / v.replace(0, np.nan)


def _f10_ewma_vol(closeadj, alpha):
    r2 = _f10_logret(closeadj) ** 2
    return np.sqrt(r2.ewm(alpha=alpha, min_periods=21).mean()) * ANN


# ============================================================
# realized vol 42d (between 21 and 63 tenor; mid-front)
def f10rv_f10_realized_volatility_term_rvol_42d_base_v076_signal(closeadj):
    b = _f10_rvol(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 10d (between 5 and 21 tenor; near-front)
def f10rv_f10_realized_volatility_term_rvol_10d_base_v077_signal(closeadj):
    b = _f10_rvol(closeadj, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 189d (3/4-year tenor; between 126 and 252)
def f10rv_f10_realized_volatility_term_rvol_189d_base_v078_signal(closeadj):
    b = _f10_rvol(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term ratio 10v42 (near-front vs mid-front)
def f10rv_f10_realized_volatility_term_tratio_10v42_base_v079_signal(closeadj):
    b = _f10_term_ratio(closeadj, 10, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term ratio 42v189 (mid vs long-mid)
def f10rv_f10_realized_volatility_term_tratio_42v189_base_v080_signal(closeadj):
    b = _f10_term_ratio(closeadj, 42, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log term slope 10 vs 42 minus its slow EMA (de-leveled near-front slope)
def f10rv_f10_realized_volatility_term_tslope_10v42_base_v081_signal(closeadj):
    sl = np.log(_f10_rvol(closeadj, 10).replace(0, np.nan)) - np.log(_f10_rvol(closeadj, 42).replace(0, np.nan))
    b = sl - sl.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol acceleration: monthly change of 21d-vol-change (vol 2nd diff as level)
def f10rv_f10_realized_volatility_term_rvolaccel_21d_base_v082_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    mom = v - v.shift(21)
    b = mom - mom.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation 5d (very-front drawdown intensity)
def f10rv_f10_realized_volatility_term_dsemi_5d_base_v083_signal(closeadj):
    b = _f10_downside(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-deviation 126d
def f10rv_f10_realized_volatility_term_usemi_126d_base_v084_signal(closeadj):
    b = _f10_upside(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation 252d (long-horizon drawdown vol)
def f10rv_f10_realized_volatility_term_dsemi_252d_base_v085_signal(closeadj):
    b = _f10_downside(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation asymmetry 126d (mid-horizon downside skew)
def f10rv_f10_realized_volatility_term_semiasym_126d_base_v086_signal(closeadj):
    d = _f10_downside(closeadj, 126)
    u = _f10_upside(closeadj, 126)
    b = (d - u) / (d + u).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside/downside vol ratio 63d (asymmetric vol balance)
def f10rv_f10_realized_volatility_term_udratio_63d_base_v087_signal(closeadj):
    u = _f10_upside(closeadj, 63)
    d = _f10_downside(closeadj, 63)
    b = u / d.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-vol term ratio 63 vs 252 (downside steepness across horizons)
def f10rv_f10_realized_volatility_term_dterm_63v252_base_v088_signal(closeadj):
    ds = _f10_downside(closeadj, 63)
    dl = _f10_downside(closeadj, 252)
    b = ds / dl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside-vol term ratio 63 vs 252
def f10rv_f10_realized_volatility_term_uterm_63v252_base_v089_signal(closeadj):
    us = _f10_upside(closeadj, 63)
    ul = _f10_upside(closeadj, 252)
    b = us / ul.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position of 42d vol within 252d history
def f10rv_f10_realized_volatility_term_cone_42in252_base_v090_signal(closeadj):
    v = _f10_rvol(closeadj, 42)
    b = _rank(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position of 10d vol within 252d history (front cone)
def f10rv_f10_realized_volatility_term_cone_10in252_base_v091_signal(closeadj):
    v = _f10_rvol(closeadj, 10)
    b = _rank(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position of 252d vol within 504d (long-vol regime)
def f10rv_f10_realized_volatility_term_cone_252in504_base_v092_signal(closeadj):
    v = _f10_rvol(closeadj, 252)
    b = _rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return 5d (very-short risk-adjusted move)
def f10rv_f10_realized_volatility_term_voladjret_5d_base_v093_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return 42d
def f10rv_f10_realized_volatility_term_voladjret_42d_base_v094_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return 189d (long risk-adjusted trend)
def f10rv_f10_realized_volatility_term_voladjret_189d_base_v095_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol scaled by 252d vol minus 1, smoothed by EMA (persistent inversion regime)
def f10rv_f10_realized_volatility_term_inv_sm_base_v096_signal(closeadj):
    ratio = _f10_term_ratio(closeadj, 21, 252) - 1.0
    b = ratio.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol 63d using 5d vol (front instability)
def f10rv_f10_realized_volatility_term_vov_5in63_base_v097_signal(closeadj):
    v = _f10_rvol(closeadj, 5)
    b = _std(v, 63) / _mean(v, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol 126d using 21d vol (mid instability)
def f10rv_f10_realized_volatility_term_vov_21in126_base_v098_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = _std(v, 126) / _mean(v, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol momentum: change in 21in63 vol-of-vol over a quarter
def f10rv_f10_realized_volatility_term_vovmom_base_v099_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    vov = _std(v, 63) / _mean(v, 63).replace(0, np.nan)
    b = vov - vov.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vol fast (alpha 0.10) annualized level
def f10rv_f10_realized_volatility_term_ewmavol_fast_base_v100_signal(closeadj):
    b = _f10_ewma_vol(closeadj, 0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vol slow (alpha 0.02) minus 252d simple vol (memory vs simple-window gap)
def f10rv_f10_realized_volatility_term_ewmagap_base_v101_signal(closeadj):
    ew = _f10_ewma_vol(closeadj, 0.02)
    sm = _f10_rvol(closeadj, 252)
    b = (ew - sm) / sm.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return kurtosis 126d (long-horizon fat tails)
def f10rv_f10_realized_volatility_term_rvkurt_126d_base_v102_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return skewness 21d (short-horizon asymmetry)
def f10rv_f10_realized_volatility_term_rvskew_21d_base_v103_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(21, min_periods=10).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean absolute return (L1 vol) 63d annualized
def f10rv_f10_realized_volatility_term_madvol_63d_base_v104_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.abs().rolling(63, min_periods=21).mean() * ANN
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# L2/L1 ratio 21d (short-horizon tail-heaviness)
def f10rv_f10_realized_volatility_term_l2l1_21d_base_v105_signal(closeadj):
    r = _f10_logret(closeadj)
    l2 = r.rolling(21, min_periods=10).std()
    l1 = r.abs().rolling(21, min_periods=10).mean()
    b = l2 / l1.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max-drawdown over 63d (close-to-close path) as a tail-risk vol proxy
def f10rv_f10_realized_volatility_term_maxdd_63d_base_v106_signal(closeadj):
    roll_peak = closeadj.rolling(63, min_periods=21).max()
    dd = closeadj / roll_peak.replace(0, np.nan) - 1.0
    b = dd.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwater fraction over 63d: share of days >2% below the running 63d peak (duration)
def f10rv_f10_realized_volatility_term_ddpervol_63d_base_v107_signal(closeadj):
    roll_peak = closeadj.rolling(63, min_periods=21).max()
    underwater = closeadj / roll_peak.replace(0, np.nan) - 1.0
    deep = (underwater <= -0.02).astype(float)
    b = deep.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jump fraction: share of 63d realized variance from the single largest squared return
def f10rv_f10_realized_volatility_term_jumpvar_63d_base_v108_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    mx = r2.rolling(63, min_periods=21).max()
    tot = r2.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# continuous-vs-jump variance: bipower-style (sum |r_t||r_t-1|) vs realized var, 63d
def f10rv_f10_realized_volatility_term_bipower_63d_base_v109_signal(closeadj):
    r = _f10_logret(closeadj)
    bp = (r.abs() * r.abs().shift(1)).rolling(63, min_periods=21).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).sum()
    b = 1.0 - bp / rv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol persistence: corr of 21d-vol with its own 21d-lagged value over 252d
def f10rv_f10_realized_volatility_term_volpersist_base_v110_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    def _ac(a):
        x = a[:-21]
        y = a[21:]
        if len(x) < 30 or np.std(x) == 0 or np.std(y) == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = v.rolling(252, min_periods=126).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol mean-reversion: 21d vol vs 252d vol, signed gap times reversion tendency
def f10rv_f10_realized_volatility_term_volmeanrev_base_v111_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v252 = _f10_rvol(closeadj, 252)
    gap = v21 - v252
    fwd_chg = -(gap - gap.shift(21))
    b = np.sign(gap) * fwd_chg.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure curvature 5/63/252 (wide-spaced butterfly level)
def f10rv_f10_realized_volatility_term_wbfly_5_63_252_base_v112_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v63 = _f10_rvol(closeadj, 63)
    v252 = _f10_rvol(closeadj, 252)
    b = (v5 + v252) / 2.0 - v63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 21d divided by its 252d max (cone headroom, distinct tenor base)
def f10rv_f10_realized_volatility_term_conehead_63d_base_v113_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    vmax = v.rolling(252, min_periods=126).max()
    b = v / vmax.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 63d divided by its 252d min minus 1 (compression gap, 63d base)
def f10rv_f10_realized_volatility_term_conefloor_63d_base_v114_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    vmin = v.rolling(252, min_periods=126).min()
    b = v / vmin.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol regime distance: 21d vol vs its 252d median (signed, normalized by median)
def f10rv_f10_realized_volatility_term_regdist_21d_base_v115_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    med = v.rolling(252, min_periods=126).median()
    b = (v - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 126d the 21d vol exceeded its 252d 75th percentile (high-vol time)
def f10rv_f10_realized_volatility_term_highvoltime_base_v116_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    q75 = v.rolling(252, min_periods=126).quantile(0.75)
    excess = (v - q75).clip(lower=0) / q75.replace(0, np.nan)
    b = excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 126d the 21d vol was below its 252d 25th percentile (low-vol time)
def f10rv_f10_realized_volatility_term_lowvoltime_base_v117_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    q25 = v.rolling(252, min_periods=126).quantile(0.25)
    deficit = (q25 - v).clip(lower=0) / q25.replace(0, np.nan)
    b = deficit.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol expansion magnitude: 21d vol over its 63d-ago value (quarterly vol growth)
def f10rv_f10_realized_volatility_term_volgrowth_base_v118_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation spread momentum: change over a quarter in (down-up) at 126d
def f10rv_f10_realized_volatility_term_semisprmom_base_v119_signal(closeadj):
    d = _f10_downside(closeadj, 126)
    u = _f10_upside(closeadj, 126)
    spr = d - u
    b = spr - spr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-vol cone (rank) of 21d downside semi-dev within 252d history
def f10rv_f10_realized_volatility_term_dcone_21in252_base_v120_signal(closeadj):
    d = _f10_downside(closeadj, 21)
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside-vol cone (rank) of 63d upside semi-dev within 252d history
def f10rv_f10_realized_volatility_term_ucone_63in252_base_v121_signal(closeadj):
    u = _f10_upside(closeadj, 63)
    b = _rank(u, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return spread: 42d minus 189d voladj-ret (momentum-horizon rotation)
def f10rv_f10_realized_volatility_term_voladjrot_base_v122_signal(closeadj):
    s = _f10_voladj_ret(closeadj, 42)
    l = _f10_voladj_ret(closeadj, 189)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-ratio 5v63 ranked within 252d (front-steepness regime percentile)
def f10rv_f10_realized_volatility_term_tratiocone_5v63_base_v123_signal(closeadj):
    tr = _f10_term_ratio(closeadj, 5, 63)
    b = _rank(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-ratio 21v126 ranked within 252d (mid-steepness regime percentile)
def f10rv_f10_realized_volatility_term_tratiocone_21v126_base_v124_signal(closeadj):
    tr = _f10_term_ratio(closeadj, 21, 126)
    b = _rank(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curvature dispersion across the near tenors 5/10/21/42/63 (front-curve roughness)
def f10rv_f10_realized_volatility_term_frontdisp_base_v125_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v10 = _f10_rvol(closeadj, 10)
    v21 = _f10_rvol(closeadj, 21)
    v42 = _f10_rvol(closeadj, 42)
    v63 = _f10_rvol(closeadj, 63)
    stacked = pd.concat([v5, v10, v21, v42, v63], axis=1)
    b = stacked.std(axis=1) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curvature dispersion across the far tenors 63/126/189/252 (back-curve roughness)
def f10rv_f10_realized_volatility_term_backdisp_base_v126_signal(closeadj):
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v189 = _f10_rvol(closeadj, 189)
    v252 = _f10_rvol(closeadj, 252)
    stacked = pd.concat([v63, v126, v189, v252], axis=1)
    b = stacked.std(axis=1) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# back-end least-squares log-vol slope over far tenors 63/126/189/252 (long-end tilt)
def f10rv_f10_realized_volatility_term_lsslope_alt_base_v127_signal(closeadj):
    xs = np.log(np.array([63.0, 126.0, 189.0, 252.0]))
    xm = xs.mean()
    dx = xs - xm
    denom = float((dx ** 2).sum())
    l63 = np.log(_f10_rvol(closeadj, 63).replace(0, np.nan))
    l126 = np.log(_f10_rvol(closeadj, 126).replace(0, np.nan))
    l189 = np.log(_f10_rvol(closeadj, 189).replace(0, np.nan))
    l252 = np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    ys = pd.concat([l63, l126, l189, l252], axis=1)
    ym = ys.mean(axis=1)
    cov = (ys.sub(ym, axis=0)).mul(dx, axis=1).sum(axis=1)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol slope residual: actual 21d vol minus the curve-fit prediction at 21d
def f10rv_f10_realized_volatility_term_slopefit_resid_base_v128_signal(closeadj):
    l5 = np.log(_f10_rvol(closeadj, 5).replace(0, np.nan))
    l252 = np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    # linear interp in log-horizon between 5 and 252, evaluated at 21
    w = (np.log(21.0) - np.log(5.0)) / (np.log(252.0) - np.log(5.0))
    pred = l5 + w * (l252 - l5)
    actual = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    b = actual - pred
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return z-scored vs own 252d history (risk-adjusted-momentum regime)
def f10rv_f10_realized_volatility_term_voladjz_63d_base_v129_signal(closeadj):
    va = _f10_voladj_ret(closeadj, 63)
    b = _z(va, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-downside-vol: 63d dispersion of the 21d downside semi-deviation (drawdown-risk churn)
def f10rv_f10_realized_volatility_term_skewvol_63d_base_v130_signal(closeadj):
    d = _f10_downside(closeadj, 21)
    b = _std(d, 63) / _mean(d, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure inversion persistence: fraction of last 63d with 21d-vol>252d-vol
def f10rv_f10_realized_volatility_term_invpersist_base_v131_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v252 = _f10_rvol(closeadj, 252)
    inv = (v21 > v252).astype(float)
    raw = inv.rolling(63, min_periods=21).mean()
    depth = ((v21 - v252) / v252.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = raw + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression-then-expansion: low 21d-vol cone followed by sharp 21d-vol jump
def f10rv_f10_realized_volatility_term_squeezepop_base_v132_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    cone = v.rolling(126, min_periods=63).rank(pct=True)
    prior_low = (1.0 - cone).shift(21)
    jump = (v / v.shift(21).replace(0, np.nan) - 1.0).clip(lower=0)
    b = prior_low * jump
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-vol-adjusted return (Sortino) at 21d
def f10rv_f10_realized_volatility_term_sortino_21d_base_v133_signal(closeadj):
    r = _f10_logret(closeadj)
    cum = r.rolling(21, min_periods=10).sum()
    d = _f10_downside(closeadj, 21) / ANN
    sharpe = cum / (_f10_rvol(closeadj, 21) / ANN).replace(0, np.nan)
    sortino = cum / d.replace(0, np.nan)
    b = sortino - sharpe
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol of overlapping 5d returns, 63d window (term-aggregated vol)
def f10rv_f10_realized_volatility_term_rvol5agg_63d_base_v134_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    b = r5.rolling(63, min_periods=21).std() * np.sqrt(252.0 / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio 21d-vs-1d over 252 window minus 1 (mean-reversion vs trending)
def f10rv_f10_realized_volatility_term_varratio_21d_base_v135_signal(closeadj):
    r = _f10_logret(closeadj)
    r21 = r.rolling(21, min_periods=21).sum()
    v1 = (r ** 2).rolling(252, min_periods=126).mean()
    v21 = (r21 ** 2).rolling(252, min_periods=126).mean()
    b = v21 / (21.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone width: 252d (q90 - q10) of 21d vol normalized by median (regime spread)
def f10rv_f10_realized_volatility_term_conewidth_base_v136_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    q90 = v.rolling(252, min_periods=126).quantile(0.90)
    q10 = v.rolling(252, min_periods=126).quantile(0.10)
    med = v.rolling(252, min_periods=126).median()
    b = (q90 - q10) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol gap between simple-21d and EWMA-fast vol (estimator divergence)
def f10rv_f10_realized_volatility_term_estgap_base_v137_signal(closeadj):
    simple = _f10_rvol(closeadj, 21)
    ew = _f10_ewma_vol(closeadj, 0.10)
    b = (simple - ew) / ew.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semivol cross-term: 21d downside times 252d-cone position (acute-and-elevated risk)
def f10rv_f10_realized_volatility_term_acutedown_base_v138_signal(closeadj):
    d = _f10_downside(closeadj, 21)
    cone = d.rolling(252, min_periods=126).rank(pct=True) - 0.5
    raw = _f10_downside(closeadj, 252)
    b = (d / raw.replace(0, np.nan)) * cone
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol curvature ranked within 504d (long-cone of front butterfly)
def f10rv_f10_realized_volatility_term_bflyrank_base_v139_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    bfly = (v5 + v63) / 2.0 - v21
    b = _rank(bfly, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average pairwise term-ratio across the curve (overall steepness composite)
def f10rv_f10_realized_volatility_term_avgsteep_base_v140_signal(closeadj):
    t1 = _f10_term_ratio(closeadj, 5, 21)
    t2 = _f10_term_ratio(closeadj, 21, 63)
    t3 = _f10_term_ratio(closeadj, 63, 252)
    b = (t1 + t2 + t3) / 3.0 - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol asymmetry of speed: up-vol momentum minus down-vol momentum, 63d
def f10rv_f10_realized_volatility_term_semivelo_base_v141_signal(closeadj):
    u = _f10_upside(closeadj, 63)
    d = _f10_downside(closeadj, 63)
    umom = u - u.shift(21)
    dmom = d - d.shift(21)
    b = umom - dmom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vol relative to trailing 5d vol (very-front term inversion, raw)
def f10rv_f10_realized_volatility_term_frontinv_base_v142_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    b = (v5 - v21) / v21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol drawup: max run-up over 63d normalized by 63d vol (upside path stretch)
def f10rv_f10_realized_volatility_term_drawup_63d_base_v143_signal(closeadj):
    roll_trough = closeadj.rolling(63, min_periods=21).min()
    ru = (closeadj / roll_trough.replace(0, np.nan) - 1.0).rolling(63, min_periods=21).max()
    v = _f10_rvol(closeadj, 63)
    b = ru / v.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol entropy proxy: dispersion of |returns| within 63d (move-size evenness)
def f10rv_f10_realized_volatility_term_moveeven_base_v144_signal(closeadj):
    a = _f10_logret(closeadj).abs()
    m = a.rolling(63, min_periods=21).mean()
    sd = a.rolling(63, min_periods=21).std()
    b = sd / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure twist: mid-front slope minus back slope of raw vol (level twist)
def f10rv_f10_realized_volatility_term_twist_base_v145_signal(closeadj):
    v10 = _f10_rvol(closeadj, 10)
    v42 = _f10_rvol(closeadj, 42)
    v63 = _f10_rvol(closeadj, 63)
    v252 = _f10_rvol(closeadj, 252)
    front = (v10 - v42) / v42.replace(0, np.nan)
    back = (v63 - v252) / v252.replace(0, np.nan)
    b = front - back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vol normalized by its own 504d EWMA, then quarter-differenced (long-norm momentum)
def f10rv_f10_realized_volatility_term_volnorm_base_v146_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    base = v.ewm(span=504, min_periods=126).mean()
    norm = v / base.replace(0, np.nan) - 1.0
    b = norm - norm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation ratio term-spread: (down/up at 21d) minus (down/up at 126d)
def f10rv_f10_realized_volatility_term_udterm_base_v147_signal(closeadj):
    d21 = _f10_downside(closeadj, 21)
    u21 = _f10_upside(closeadj, 21)
    d126 = _f10_downside(closeadj, 126)
    u126 = _f10_upside(closeadj, 126)
    s = d21 / u21.replace(0, np.nan)
    l = d126 / u126.replace(0, np.nan)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol convexity sign-magnitude: sqrt-compressed back butterfly (21/63/126)
def f10rv_f10_realized_volatility_term_bflysignmag_base_v148_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    bfly = (v21 + v126) / 2.0 - v63
    b = np.sign(bfly) * (bfly.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol regime streak: consecutive days 21d vol above its 252d 75th pct (length)
def f10rv_f10_realized_volatility_term_hivolstreak_base_v149_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    q75 = v.rolling(252, min_periods=126).quantile(0.75)
    hi = (v > q75).astype(float)
    grp = (hi == 0).cumsum()
    streak = hi.groupby(grp).cumsum()
    b = streak / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# whole-curve vol level normalized by its 252d mean (overall vol regime, centered)
def f10rv_f10_realized_volatility_term_curvelevelnorm_base_v150_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    level = pd.concat([v5, v21, v63, v126, v252], axis=1).mean(axis=1)
    base = level.rolling(252, min_periods=126).mean()
    b = level / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_realized_volatility_term_rvol_42d_base_v076_signal,
    f10rv_f10_realized_volatility_term_rvol_10d_base_v077_signal,
    f10rv_f10_realized_volatility_term_rvol_189d_base_v078_signal,
    f10rv_f10_realized_volatility_term_tratio_10v42_base_v079_signal,
    f10rv_f10_realized_volatility_term_tratio_42v189_base_v080_signal,
    f10rv_f10_realized_volatility_term_tslope_10v42_base_v081_signal,
    f10rv_f10_realized_volatility_term_rvolaccel_21d_base_v082_signal,
    f10rv_f10_realized_volatility_term_dsemi_5d_base_v083_signal,
    f10rv_f10_realized_volatility_term_usemi_126d_base_v084_signal,
    f10rv_f10_realized_volatility_term_dsemi_252d_base_v085_signal,
    f10rv_f10_realized_volatility_term_semiasym_126d_base_v086_signal,
    f10rv_f10_realized_volatility_term_udratio_63d_base_v087_signal,
    f10rv_f10_realized_volatility_term_dterm_63v252_base_v088_signal,
    f10rv_f10_realized_volatility_term_uterm_63v252_base_v089_signal,
    f10rv_f10_realized_volatility_term_cone_42in252_base_v090_signal,
    f10rv_f10_realized_volatility_term_cone_10in252_base_v091_signal,
    f10rv_f10_realized_volatility_term_cone_252in504_base_v092_signal,
    f10rv_f10_realized_volatility_term_voladjret_5d_base_v093_signal,
    f10rv_f10_realized_volatility_term_voladjret_42d_base_v094_signal,
    f10rv_f10_realized_volatility_term_voladjret_189d_base_v095_signal,
    f10rv_f10_realized_volatility_term_inv_sm_base_v096_signal,
    f10rv_f10_realized_volatility_term_vov_5in63_base_v097_signal,
    f10rv_f10_realized_volatility_term_vov_21in126_base_v098_signal,
    f10rv_f10_realized_volatility_term_vovmom_base_v099_signal,
    f10rv_f10_realized_volatility_term_ewmavol_fast_base_v100_signal,
    f10rv_f10_realized_volatility_term_ewmagap_base_v101_signal,
    f10rv_f10_realized_volatility_term_rvkurt_126d_base_v102_signal,
    f10rv_f10_realized_volatility_term_rvskew_21d_base_v103_signal,
    f10rv_f10_realized_volatility_term_madvol_63d_base_v104_signal,
    f10rv_f10_realized_volatility_term_l2l1_21d_base_v105_signal,
    f10rv_f10_realized_volatility_term_maxdd_63d_base_v106_signal,
    f10rv_f10_realized_volatility_term_ddpervol_63d_base_v107_signal,
    f10rv_f10_realized_volatility_term_jumpvar_63d_base_v108_signal,
    f10rv_f10_realized_volatility_term_bipower_63d_base_v109_signal,
    f10rv_f10_realized_volatility_term_volpersist_base_v110_signal,
    f10rv_f10_realized_volatility_term_volmeanrev_base_v111_signal,
    f10rv_f10_realized_volatility_term_wbfly_5_63_252_base_v112_signal,
    f10rv_f10_realized_volatility_term_conehead_63d_base_v113_signal,
    f10rv_f10_realized_volatility_term_conefloor_63d_base_v114_signal,
    f10rv_f10_realized_volatility_term_regdist_21d_base_v115_signal,
    f10rv_f10_realized_volatility_term_highvoltime_base_v116_signal,
    f10rv_f10_realized_volatility_term_lowvoltime_base_v117_signal,
    f10rv_f10_realized_volatility_term_volgrowth_base_v118_signal,
    f10rv_f10_realized_volatility_term_semisprmom_base_v119_signal,
    f10rv_f10_realized_volatility_term_dcone_21in252_base_v120_signal,
    f10rv_f10_realized_volatility_term_ucone_63in252_base_v121_signal,
    f10rv_f10_realized_volatility_term_voladjrot_base_v122_signal,
    f10rv_f10_realized_volatility_term_tratiocone_5v63_base_v123_signal,
    f10rv_f10_realized_volatility_term_tratiocone_21v126_base_v124_signal,
    f10rv_f10_realized_volatility_term_frontdisp_base_v125_signal,
    f10rv_f10_realized_volatility_term_backdisp_base_v126_signal,
    f10rv_f10_realized_volatility_term_lsslope_alt_base_v127_signal,
    f10rv_f10_realized_volatility_term_slopefit_resid_base_v128_signal,
    f10rv_f10_realized_volatility_term_voladjz_63d_base_v129_signal,
    f10rv_f10_realized_volatility_term_skewvol_63d_base_v130_signal,
    f10rv_f10_realized_volatility_term_invpersist_base_v131_signal,
    f10rv_f10_realized_volatility_term_squeezepop_base_v132_signal,
    f10rv_f10_realized_volatility_term_sortino_21d_base_v133_signal,
    f10rv_f10_realized_volatility_term_rvol5agg_63d_base_v134_signal,
    f10rv_f10_realized_volatility_term_varratio_21d_base_v135_signal,
    f10rv_f10_realized_volatility_term_conewidth_base_v136_signal,
    f10rv_f10_realized_volatility_term_estgap_base_v137_signal,
    f10rv_f10_realized_volatility_term_acutedown_base_v138_signal,
    f10rv_f10_realized_volatility_term_bflyrank_base_v139_signal,
    f10rv_f10_realized_volatility_term_avgsteep_base_v140_signal,
    f10rv_f10_realized_volatility_term_semivelo_base_v141_signal,
    f10rv_f10_realized_volatility_term_frontinv_base_v142_signal,
    f10rv_f10_realized_volatility_term_drawup_63d_base_v143_signal,
    f10rv_f10_realized_volatility_term_moveeven_base_v144_signal,
    f10rv_f10_realized_volatility_term_twist_base_v145_signal,
    f10rv_f10_realized_volatility_term_volnorm_base_v146_signal,
    f10rv_f10_realized_volatility_term_udterm_base_v147_signal,
    f10rv_f10_realized_volatility_term_bflysignmag_base_v148_signal,
    f10rv_f10_realized_volatility_term_hivolstreak_base_v149_signal,
    f10rv_f10_realized_volatility_term_curvelevelnorm_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_REALIZED_VOLATILITY_TERM_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

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

    print("OK f10_realized_volatility_term_base_076_150_claude: %d features pass" % n_features)
