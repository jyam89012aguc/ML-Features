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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (relative strength / trend persistence) =====
def _f08_efficiency_ratio(close, w):
    net = (close - close.shift(w)).abs()
    path = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f08_rs_exponent(logret, w):
    def _rs(a):
        a = a[~np.isnan(a)]
        m = len(a)
        if m < 8:
            return np.nan
        mean = a.mean()
        dev = np.cumsum(a - mean)
        R = dev.max() - dev.min()
        S = a.std()
        if S <= 0 or R <= 0:
            return np.nan
        return np.log(R / S) / np.log(m)
    return logret.rolling(w, min_periods=max(8, w // 2)).apply(_rs, raw=True)


def _f08_autocorr(logret, w, lag):
    def _ac(a):
        a = a[~np.isnan(a)]
        if len(a) < lag + 5:
            return np.nan
        x = a[:-lag]
        y = a[lag:]
        if x.std() <= 0 or y.std() <= 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    return logret.rolling(w, min_periods=max(lag + 5, w // 2)).apply(_ac, raw=True)


def _f08_mom(close, w):
    return close / close.shift(w) - 1.0


def _f08_riskadj_mom(close, w, volw):
    r = close / close.shift(w) - 1.0
    vol = close.pct_change().rolling(volw, min_periods=max(2, volw // 2)).std()
    return r / vol.replace(0, np.nan)


def _f08_curstreak(logret):
    s = np.sign(logret).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    run = s.groupby(grp).cumcount() + 1.0
    return run * s


def _f08_trend_slope(logprice, w):
    def _slp(a):
        if np.isnan(a).any():
            return np.nan
        xc = np.arange(len(a), dtype=float)
        xc = xc - xc.mean()
        denom = (xc ** 2).sum()
        if denom <= 0:
            return np.nan
        return float(np.dot(xc, a - a.mean()) / denom)
    return logprice.rolling(w, min_periods=max(8, w // 2)).apply(_slp, raw=True)


# ============================================================
# --- Efficiency-ratio variants ---

# efficiency ratio over 42d (six-week clean-trend)
def f08rs_f08_relative_strength_rotation_effr_42d_base_v076_signal(closeadj):
    b = _f08_efficiency_ratio(closeadj, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 252d percentile-ranked vs 1260d history (cycle-relative cleanliness)
def f08rs_f08_relative_strength_rotation_effrrank_252d_base_v077_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 252)
    b = _rank(er, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio smoothed slope: change in 63d ER's EMA over a quarter
def f08rs_f08_relative_strength_rotation_effrtrend_63d_base_v078_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 63).ewm(span=21, min_periods=10).mean()
    b = er - er.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio gap: 252d ER minus 504d ER (long persistence narrowing)
def f08rs_f08_relative_strength_rotation_effrspr_252v504_base_v079_signal(closeadj):
    s = _f08_efficiency_ratio(closeadj, 252)
    l = _f08_efficiency_ratio(closeadj, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional efficiency over 126d signed and smoothed (clean-trend tilt, medium)
def f08rs_f08_relative_strength_rotation_effsm_126d_base_v080_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 126)
    direction = np.sign(closeadj - closeadj.shift(126))
    b = (er * direction).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fractal-dimension proxy (2 - ER) over 63d: roughness of the path (anti-persistence)
def f08rs_f08_relative_strength_rotation_fracdim_63d_base_v081_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 63)
    b = 2.0 - er
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Hurst / variance-ratio variants ---

# Hurst-like R/S exponent over 504d (multi-year long memory)
def f08rs_f08_relative_strength_rotation_hurst_504d_base_v082_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_rs_exponent(lr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst R/S on weekly (5d) returns over 252d (lower-frequency memory)
def f08rs_f08_relative_strength_rotation_hurstwk_252d_base_v083_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    b = _f08_rs_exponent(wk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio at lag 10 over 252d (multi-day persistence vs reversion)
def f08rs_f08_relative_strength_rotation_varratio10_252d_base_v084_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(252, min_periods=126).var()
    v10 = lr.rolling(10).sum().rolling(252, min_periods=126).var()
    b = v10 / (10.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio multi-scale slope over 252d (Hurst from aggregation scaling)
def f08rs_f08_relative_strength_rotation_vrslope_252d_base_v085_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(252, min_periods=126).var()
    v5 = lr.rolling(5).sum().rolling(252, min_periods=126).var()
    v21 = lr.rolling(21).sum().rolling(252, min_periods=126).var()
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    b = (y21 - y5) / (np.log(21.0) - np.log(5.0)) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst long-vs-short memory spread: 504d Hurst minus 126d Hurst
def f08rs_f08_relative_strength_rotation_hurstspr_504v126_base_v086_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    l = _f08_rs_exponent(lr, 504)
    s = _f08_rs_exponent(lr, 126)
    b = l - s
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Autocorrelation variants ---

# lag-2 autocorrelation of daily returns over 126d
def f08rs_f08_relative_strength_rotation_acf2_126d_base_v087_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_autocorr(lr, 126, 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-10 autocorrelation over 252d (two-week memory)
def f08rs_f08_relative_strength_rotation_acf10_252d_base_v088_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_autocorr(lr, 252, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sum of lag-1..5 autocorrelations over 252d (short-memory mass)
def f08rs_f08_relative_strength_rotation_acfsum_252d_base_v089_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    tot = None
    for lag in (1, 2, 3, 4, 5):
        ac = _f08_autocorr(lr, 252, lag)
        tot = ac if tot is None else tot + ac
    b = tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr of absolute returns lag-1 over 126d (volatility clustering, vol persistence)
def f08rs_f08_relative_strength_rotation_acfabs_126d_base_v090_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff().abs()
    b = _f08_autocorr(lr, 126, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag-1 momentum: change over a quarter in 126d acf (memory drift)
def f08rs_f08_relative_strength_rotation_acfmom_126d_base_v091_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    ac = _f08_autocorr(lr, 126, 1)
    b = ac - ac.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio z-scored vs own 252d history (de-trended persistence regime)
def f08rs_f08_relative_strength_rotation_vrz_126d_base_v092_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    vr = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    b = _z(vr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Streak / run variants ---

# magnitude-weighted run balance over 126d (medium-horizon directional pressure)
def f08rs_f08_relative_strength_rotation_runbal_126d_base_v093_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    weighted = (sgn * lr.abs().pow(0.5)).rolling(126, min_periods=63).sum()
    scale = lr.abs().pow(0.5).rolling(126, min_periods=63).sum()
    b = weighted / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current magnitude-weighted streak relative to its 252d typical magnitude
def f08rs_f08_relative_strength_rotation_streakrel_252d_base_v094_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    runlen = s.groupby(grp).cumcount() + 1.0
    signed = runlen * s
    b = signed / signed.abs().rolling(252, min_periods=126).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted choppiness over 63d: low when flips coincide with big moves
def f08rs_f08_relative_strength_rotation_flips_63d_base_v095_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr)
    flip = (s != s.shift(1)).astype(float)
    w = lr.abs() + lr.shift(1).abs()
    chop = (flip * w).rolling(63, min_periods=32).sum() / w.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = 0.5 - chop
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest current monotone advance fraction over 252d (max up-streak recency proxy)
def f08rs_f08_relative_strength_rotation_streakmax_252d_base_v096_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    cummove = lr.groupby(grp).cumsum()
    signed = cummove * (s != 0).astype(float)
    hi = signed.rolling(252, min_periods=126).max()
    lo = signed.rolling(252, min_periods=126).min()
    b = (hi + lo)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-streak vs down-streak average length over 252d (persistence-duration asymmetry)
def f08rs_f08_relative_strength_rotation_wkrunasym_252d_base_v097_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    runlen = s.groupby(grp).cumcount() + 1.0
    # at each day, length so far of current run, signed
    up_len = (runlen * (s > 0)).rolling(252, min_periods=126).mean()
    dn_len = (runlen * (s < 0)).rolling(252, min_periods=126).mean()
    b = (up_len - dn_len) / (up_len + dn_len).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Self-relative momentum / rotation variants ---

# 504d momentum z-scored vs own 1260d history (multi-year self-relative RS)
def f08rs_f08_relative_strength_rotation_selfmom_504d_base_v098_signal(closeadj):
    m = _f08_mom(closeadj, 504)
    b = _z(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d momentum z-scored vs own 252d history (short self-relative thrust)
def f08rs_f08_relative_strength_rotation_selfmom_21d_base_v099_signal(closeadj):
    m = _f08_mom(closeadj, 21)
    b = _z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 6-1 momentum (126d skip last 21d) ranked vs own 504d history
def f08rs_f08_relative_strength_rotation_mom61rank_base_v100_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(126) - 1.0
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-relative momentum dispersion across 63/126/252 z-scores (rotation disagreement)
def f08rs_f08_relative_strength_rotation_selfmomdisp_base_v101_signal(closeadj):
    z1 = _z(_f08_mom(closeadj, 63), 252)
    z2 = _z(_f08_mom(closeadj, 126), 504)
    z3 = _z(_f08_mom(closeadj, 252), 504)
    b = pd.concat([z1, z2, z3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum (252d skip 21d) z-scored vs its own 1260d cycle history (deep self-RS)
def f08rs_f08_relative_strength_rotation_momcyclerank_252d_base_v102_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(252) - 1.0
    b = _z(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum-of-momentum: 21d change of (63d ROC z vs 252d) (rotation acceleration)
def f08rs_f08_relative_strength_rotation_selfmomaccel_base_v103_signal(closeadj):
    zm = _z(_f08_mom(closeadj, 63), 252)
    b = zm - zm.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Risk-adjusted RS variants ---

# risk-adjusted momentum: 504d ROC / 252d vol (multi-year Sharpe-like RS)
def f08rs_f08_relative_strength_rotation_radjmom_504d_base_v104_signal(closeadj):
    r = closeadj / closeadj.shift(504) - 1.0
    vol = closeadj.pct_change().rolling(252, min_periods=126).std() * np.sqrt(252.0)
    b = r / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# information-ratio-like: 126d trend slope / residual vol around the trend
def f08rs_f08_relative_strength_rotation_infratio_126d_base_v105_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _f08_trend_slope(lp, 126)
    ma = lp.rolling(21, min_periods=10).mean()
    resid = (lp - ma).rolling(126, min_periods=63).std()
    b = slope / resid.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe term structure: 63d Sharpe minus 252d Sharpe (RS regime acceleration)
def f08rs_f08_relative_strength_rotation_sharpespr_base_v106_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s_mu = lr.rolling(63, min_periods=32).mean()
    s_sd = lr.rolling(63, min_periods=32).std()
    l_mu = lr.rolling(252, min_periods=126).mean()
    l_sd = lr.rolling(252, min_periods=126).std()
    b = s_mu / s_sd.replace(0, np.nan) - l_mu / l_sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sterling-like RS: 252d return / average drawdown depth (sustained-RS quality)
def f08rs_f08_relative_strength_rotation_sterling_252d_base_v107_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    peak = closeadj.rolling(252, min_periods=126).max()
    dd = (peak.replace(0, np.nan) - closeadj) / peak.replace(0, np.nan)
    avgdd = dd.rolling(252, min_periods=126).mean()
    b = ret / avgdd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Omega-like RS over 126d about a positive hurdle (median return) threshold
def f08rs_f08_relative_strength_rotation_omega_126d_base_v108_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    hurdle = lr.rolling(126, min_periods=63).median()
    excess = lr - hurdle
    gains = excess.clip(lower=0.0).rolling(126, min_periods=63).mean()
    losses = (-excess.clip(upper=0.0)).rolling(126, min_periods=63).mean()
    b = np.log((gains + 1e-9) / (losses + 1e-9))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted RS rank: 126d (ROC/vol) percentile vs own 504d history
def f08rs_f08_relative_strength_rotation_radjrank_126d_base_v109_signal(closeadj):
    r = _f08_riskadj_mom(closeadj, 126, 63)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Trend slope / monotonicity variants ---

# vol-normalized trend slope over 252d (long clean trend strength)
def f08rs_f08_relative_strength_rotation_trslope_252d_base_v110_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _f08_trend_slope(lp, 252)
    vol = lp.diff().rolling(252, min_periods=126).std()
    b = slope / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-slope acceleration: 126d slope now minus 126d slope a quarter ago
def f08rs_f08_relative_strength_rotation_slopeaccel_126d_base_v111_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _f08_trend_slope(lp, 126)
    b = slope - slope.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-slope curvature: difference of 63d slope and 252d slope (concavity of trend)
def f08rs_f08_relative_strength_rotation_slopecurv_base_v112_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    s = _f08_trend_slope(lp, 63)
    l = _f08_trend_slope(lp, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Mann-Kendall rank-trend over 126d (monotonicity of price)
def f08rs_f08_relative_strength_rotation_mktrend_126d_base_v113_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _tau(a):
        if np.isnan(a).any():
            return np.nan
        m = len(a)
        rk = np.argsort(np.argsort(a)).astype(float)
        t = np.arange(m, dtype=float)
        rkc = rk - rk.mean()
        tc = t - t.mean()
        denom = np.sqrt((rkc ** 2).sum() * (tc ** 2).sum())
        if denom <= 0:
            return np.nan
        return float(np.dot(rkc, tc) / denom)
    b = lp.rolling(126, min_periods=63).apply(_tau, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 252d that price stayed above its 200d MA (long trend regime persistence)
def f08rs_f08_relative_strength_rotation_aboveMA_252d_base_v114_signal(closeadj):
    ma = _mean(closeadj, 200)
    above = (closeadj > ma).astype(float)
    raw = above.rolling(252, min_periods=126).mean() - 0.5
    dist = (closeadj / ma.replace(0, np.nan) - 1.0)
    b = raw + 0.1 * np.tanh(dist)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-stacking persistence: fraction of 126d the 21d MA stayed above the 63d MA
def f08rs_f08_relative_strength_rotation_mastack_126d_base_v115_signal(closeadj):
    fast = _mean(closeadj, 21)
    slow = _mean(closeadj, 63)
    stacked = (fast > slow).astype(float)
    raw = stacked.rolling(126, min_periods=63).mean() - 0.5
    sep = (fast / slow.replace(0, np.nan) - 1.0)
    b = raw + 0.1 * np.tanh(5.0 * sep)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Path / efficiency / concentration variants ---

# path efficiency over 252d: net log move / total absolute path
def f08rs_f08_relative_strength_rotation_patheff_252d_base_v116_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(252)
    path = lp.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net move per max excursion over 504d (multi-year path efficiency)
def f08rs_f08_relative_strength_rotation_patheff_504d_base_v117_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(504)
    hi = lp.rolling(504, min_periods=252).max()
    lo = lp.rolling(504, min_periods=252).min()
    b = net / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum concentration: share of 252d move in worst 21d window (downside concentration)
def f08rs_f08_relative_strength_rotation_dnconc_252d_base_v118_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    chg21 = lp.diff(21)
    worst = chg21.rolling(252, min_periods=126).min()
    net = (lp - lp.shift(252)).abs()
    b = worst / net.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Herfindahl of monthly-return magnitudes over 252d (return concentration / lumpiness)
def f08rs_f08_relative_strength_rotation_retherf_252d_base_v119_signal(closeadj):
    mo = np.log(closeadj.replace(0, np.nan)).diff(21)
    sq = mo ** 2
    tot = sq.rolling(252, min_periods=126).sum()
    sqsq = (sq ** 2).rolling(252, min_periods=126).sum()
    b = sqsq / (tot ** 2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Breadth / asymmetry variants ---

# rolling excess kurtosis of daily returns over 126d (fat-tail / shock-prone regime)
def f08rs_f08_relative_strength_rotation_updays_126d_base_v120_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = lr.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# best-minus-worst day asymmetry over 126d (tail-direction balance)
def f08rs_f08_relative_strength_rotation_tailasym_126d_base_v121_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    best = lr.rolling(126, min_periods=63).max()
    worst = lr.rolling(126, min_periods=63).min()
    b = (best + worst) / (best - worst).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling return skewness over 252d (long-horizon distribution asymmetry)
def f08rs_f08_relative_strength_rotation_retskew_252d_base_v122_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = lr.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-skewness of returns with lagged returns over 126d (asymmetric persistence)
def f08rs_f08_relative_strength_rotation_coskew_126d_base_v123_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    x = lr
    y = lr.shift(1)
    xc = x - x.rolling(126, min_periods=63).mean()
    yc = y - y.rolling(126, min_periods=63).mean()
    num = (xc * yc * yc).rolling(126, min_periods=63).mean()
    den = (xc.rolling(126, min_periods=63).std()
           * yc.rolling(126, min_periods=63).var())
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Interaction / composite RS variants ---

# trend quality x persistence: vol-normalized slope x Hurst over 252d
def f08rs_f08_relative_strength_rotation_slopehurst_252d_base_v124_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _f08_trend_slope(lp, 252)
    vol = lp.diff().rolling(252, min_periods=126).std()
    sn = slope / vol.replace(0, np.nan)
    lr = lp.diff()
    h = _f08_rs_exponent(lr, 252)
    b = sn * (h - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio x risk-adjusted-momentum over 126d (clean strong RS composite)
def f08rs_f08_relative_strength_rotation_ereradj_126d_base_v125_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 126)
    radj = _f08_riskadj_mom(closeadj, 126, 63)
    b = er * radj
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-relative-momentum x efficiency: leadership only when trend is clean, 126d
def f08rs_f08_relative_strength_rotation_leadclean_126d_base_v126_signal(closeadj):
    zm = _z(_f08_mom(closeadj, 126), 504)
    er = _f08_efficiency_ratio(closeadj, 126)
    b = zm * er
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence-weighted return: 63d ROC x sign-clustering over 63d
def f08rs_f08_relative_strength_rotation_perswtret_63d_base_v127_signal(closeadj):
    m = _f08_mom(closeadj, 63)
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    prod = (np.sign(lr) * np.sign(lr.shift(1))).rolling(63, min_periods=32).mean()
    b = m * prod
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend R2 x momentum sign over 252d (reliable directional RS)
def f08rs_f08_relative_strength_rotation_r2dir_252d_base_v128_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _r2(a):
        if np.isnan(a).any():
            return np.nan
        xc = np.arange(len(a), dtype=float)
        xc = xc - xc.mean()
        sxx = (xc ** 2).sum()
        ac = a - a.mean()
        ss = (ac ** 2).sum()
        if ss <= 0 or sxx <= 0:
            return np.nan
        beta = np.dot(xc, ac) / sxx
        fit = beta * xc
        return float((fit ** 2).sum() / ss)
    r2 = lp.rolling(252, min_periods=126).apply(_r2, raw=True)
    direction = np.sign(closeadj - closeadj.shift(252))
    b = r2 * direction
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Regime distance / extra persistence variants ---

# persistence regime distance: 126d Hurst minus its 504d median
def f08rs_f08_relative_strength_rotation_hurstreg_126d_base_v129_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    h = _f08_rs_exponent(lr, 126)
    med = h.rolling(504, min_periods=126).median()
    b = h - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio regime distance: 63d ER minus its 252d median
def f08rs_f08_relative_strength_rotation_erreg_63d_base_v130_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 63)
    med = er.rolling(252, min_periods=126).median()
    b = er - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum regime distance: 252d ROC minus its 504d rolling median
def f08rs_f08_relative_strength_rotation_momreg_252d_base_v131_signal(closeadj):
    m = _f08_mom(closeadj, 252)
    med = m.rolling(504, min_periods=126).median()
    b = m - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe regime distance: 126d Sharpe minus its own 504d median
def f08rs_f08_relative_strength_rotation_sharpereg_126d_base_v132_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    mu = lr.rolling(126, min_periods=63).mean()
    sd = lr.rolling(126, min_periods=63).std()
    sh = mu / sd.replace(0, np.nan)
    med = sh.rolling(504, min_periods=126).median()
    b = sh - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- More distinct trend-persistence forms ---

# drawdown-free streak: fraction of 126d spent at a trailing 126d high (new-high persistence)
def f08rs_f08_relative_strength_rotation_athstreak_126d_base_v133_signal(closeadj):
    peak = closeadj.rolling(126, min_periods=63).max()
    nearhi = (closeadj >= peak * 0.999).astype(float)
    raw = nearhi.rolling(126, min_periods=63).mean()
    prox = closeadj / peak.replace(0, np.nan)
    b = raw + 0.2 * prox
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend reversal pressure: lag-1 acf of weekly returns over 252d, negated (reversion)
def f08rs_f08_relative_strength_rotation_revpressure_252d_base_v134_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    ac = _f08_autocorr(wk, 252, 5)
    b = -ac
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum smoothness ratio: |63d ROC| over std of daily returns x sqrt(63)
def f08rs_f08_relative_strength_rotation_momsmooth_63d_base_v135_signal(closeadj):
    m = (closeadj / closeadj.shift(63) - 1.0)
    vol = closeadj.pct_change().rolling(63, min_periods=32).std() * np.sqrt(63.0)
    b = m / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling cumulative-return drawdown-recovery ratio over 252d (RS resilience)
def f08rs_f08_relative_strength_rotation_resilience_252d_base_v136_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    trough = closeadj.rolling(252, min_periods=126).min()
    recov = closeadj / trough.replace(0, np.nan) - 1.0
    b = ret * (1.0 + recov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 252d trading above the 63d-ago price (trailing-relative strength breadth)
def f08rs_f08_relative_strength_rotation_relbreadth_252d_base_v137_signal(closeadj):
    above = (closeadj > closeadj.shift(63)).astype(float)
    raw = above.rolling(252, min_periods=126).mean() - 0.5
    tilt = np.tanh(2.0 * (closeadj / closeadj.shift(63) - 1.0))
    b = raw + 0.2 * tilt.rolling(63, min_periods=32).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-persistence z: vol-normalized slope of 126d z-scored vs 504d history
def f08rs_f08_relative_strength_rotation_slopez_126d_base_v138_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope = _f08_trend_slope(lp, 126)
    vol = lp.diff().rolling(126, min_periods=63).std()
    sn = slope / vol.replace(0, np.nan)
    b = _z(sn, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation-implied half-life proxy over 126d (mean-reversion speed)
def f08rs_f08_relative_strength_rotation_halflife_126d_base_v139_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    ac = _f08_autocorr(lr, 126, 1)
    # half-life ~ -ln2 / ln(|rho|); map persistence to a bounded score
    rho = ac.clip(-0.99, 0.99)
    b = -np.log(2.0) / np.log(rho.abs().replace(0, np.nan))
    b = np.tanh(b / 50.0) * np.sign(rho)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon risk-adjusted momentum blend rank (63/126/252 radj, ranked vs 504d)
def f08rs_f08_relative_strength_rotation_radjblend_base_v140_signal(closeadj):
    r1 = _rank(_f08_riskadj_mom(closeadj, 63, 63), 504)
    r2 = _rank(_f08_riskadj_mom(closeadj, 126, 63), 504)
    r3 = _rank(_f08_riskadj_mom(closeadj, 252, 126), 504)
    b = (r1 + r2 + r3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-slope stability over 252d: |mean 21d-slope| / std of 21d-slope (steady trend)
def f08rs_f08_relative_strength_rotation_slopeconsist_252d_base_v141_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    slope21 = _f08_trend_slope(lp, 21)
    mu = slope21.rolling(252, min_periods=126).mean()
    sd = slope21.rolling(252, min_periods=126).std()
    b = mu.abs() / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return autocorrelation spectrum tilt: acf1 minus acf21 over 252d (memory shape)
def f08rs_f08_relative_strength_rotation_acftilt_252d_base_v142_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    a1 = _f08_autocorr(lr, 252, 1)
    a21 = _f08_autocorr(lr, 252, 21)
    b = a1 - a21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwater fraction over 126d: share of days below the trailing 126d peak (RS drag)
def f08rs_f08_relative_strength_rotation_kelly_126d_base_v143_signal(closeadj):
    peak = closeadj.rolling(126, min_periods=63).max()
    underwater = (closeadj < peak * 0.999).astype(float)
    raw = underwater.rolling(126, min_periods=63).mean()
    depth = (peak.replace(0, np.nan) - closeadj) / peak.replace(0, np.nan)
    b = raw * depth.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside/upside semideviation ratio over 252d (asymmetric-risk RS, not a return ratio)
def f08rs_f08_relative_strength_rotation_dsrs_252d_base_v144_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    downdev = lr.clip(upper=0.0).rolling(252, min_periods=126).std()
    updev = lr.clip(lower=0.0).rolling(252, min_periods=126).std()
    b = np.log((updev + 1e-9) / (downdev + 1e-9))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of variance from trend vs noise over 252d (signal share / R2-like)
def f08rs_f08_relative_strength_rotation_trendshare_252d_base_v145_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    trend_var = lp.rolling(21, min_periods=10).mean().rolling(252, min_periods=126).var()
    tot_var = lp.rolling(252, min_periods=126).var()
    b = trend_var / tot_var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum persistence test: corr of consecutive 21d ROC over 252d (self-prediction)
def f08rs_f08_relative_strength_rotation_mompred_252d_base_v146_signal(closeadj):
    m = _f08_mom(closeadj, 21)
    b = m.rolling(252, min_periods=126).corr(m.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional efficiency over 504d, signed (multi-year clean-trend direction)
def f08rs_f08_relative_strength_rotation_effsgn_504d_base_v147_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 504)
    direction = np.sign(closeadj - closeadj.shift(504))
    b = er * direction
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail gain-to-pain over 252d: mean of top-decile gains / mean of bottom-decile losses
def f08rs_f08_relative_strength_rotation_gainpain_252d_base_v148_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    q90 = lr.rolling(252, min_periods=126).quantile(0.90)
    q10 = lr.rolling(252, min_periods=126).quantile(0.10)
    b = q90 / q10.abs().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence acceleration: change over a quarter in 126d efficiency ratio rank
def f08rs_f08_relative_strength_rotation_erankmom_126d_base_v149_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 126)
    rk = _rank(er, 504)
    b = rk - rk.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite RS score: blended z of selfmom, radj-mom, and efficiency over 126d
def f08rs_f08_relative_strength_rotation_rsscore_126d_base_v150_signal(closeadj):
    z1 = _z(_f08_mom(closeadj, 126), 504)
    z2 = _z(_f08_riskadj_mom(closeadj, 126, 63), 504)
    z3 = _z(_f08_efficiency_ratio(closeadj, 126), 504)
    b = (z1 + z2 + z3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08rs_f08_relative_strength_rotation_effr_42d_base_v076_signal,
    f08rs_f08_relative_strength_rotation_effrrank_252d_base_v077_signal,
    f08rs_f08_relative_strength_rotation_effrtrend_63d_base_v078_signal,
    f08rs_f08_relative_strength_rotation_effrspr_252v504_base_v079_signal,
    f08rs_f08_relative_strength_rotation_effsm_126d_base_v080_signal,
    f08rs_f08_relative_strength_rotation_fracdim_63d_base_v081_signal,
    f08rs_f08_relative_strength_rotation_hurst_504d_base_v082_signal,
    f08rs_f08_relative_strength_rotation_hurstwk_252d_base_v083_signal,
    f08rs_f08_relative_strength_rotation_varratio10_252d_base_v084_signal,
    f08rs_f08_relative_strength_rotation_vrslope_252d_base_v085_signal,
    f08rs_f08_relative_strength_rotation_hurstspr_504v126_base_v086_signal,
    f08rs_f08_relative_strength_rotation_acf2_126d_base_v087_signal,
    f08rs_f08_relative_strength_rotation_acf10_252d_base_v088_signal,
    f08rs_f08_relative_strength_rotation_acfsum_252d_base_v089_signal,
    f08rs_f08_relative_strength_rotation_acfabs_126d_base_v090_signal,
    f08rs_f08_relative_strength_rotation_acfmom_126d_base_v091_signal,
    f08rs_f08_relative_strength_rotation_vrz_126d_base_v092_signal,
    f08rs_f08_relative_strength_rotation_runbal_126d_base_v093_signal,
    f08rs_f08_relative_strength_rotation_streakrel_252d_base_v094_signal,
    f08rs_f08_relative_strength_rotation_flips_63d_base_v095_signal,
    f08rs_f08_relative_strength_rotation_streakmax_252d_base_v096_signal,
    f08rs_f08_relative_strength_rotation_wkrunasym_252d_base_v097_signal,
    f08rs_f08_relative_strength_rotation_selfmom_504d_base_v098_signal,
    f08rs_f08_relative_strength_rotation_selfmom_21d_base_v099_signal,
    f08rs_f08_relative_strength_rotation_mom61rank_base_v100_signal,
    f08rs_f08_relative_strength_rotation_selfmomdisp_base_v101_signal,
    f08rs_f08_relative_strength_rotation_momcyclerank_252d_base_v102_signal,
    f08rs_f08_relative_strength_rotation_selfmomaccel_base_v103_signal,
    f08rs_f08_relative_strength_rotation_radjmom_504d_base_v104_signal,
    f08rs_f08_relative_strength_rotation_infratio_126d_base_v105_signal,
    f08rs_f08_relative_strength_rotation_sharpespr_base_v106_signal,
    f08rs_f08_relative_strength_rotation_sterling_252d_base_v107_signal,
    f08rs_f08_relative_strength_rotation_omega_126d_base_v108_signal,
    f08rs_f08_relative_strength_rotation_radjrank_126d_base_v109_signal,
    f08rs_f08_relative_strength_rotation_trslope_252d_base_v110_signal,
    f08rs_f08_relative_strength_rotation_slopeaccel_126d_base_v111_signal,
    f08rs_f08_relative_strength_rotation_slopecurv_base_v112_signal,
    f08rs_f08_relative_strength_rotation_mktrend_126d_base_v113_signal,
    f08rs_f08_relative_strength_rotation_aboveMA_252d_base_v114_signal,
    f08rs_f08_relative_strength_rotation_mastack_126d_base_v115_signal,
    f08rs_f08_relative_strength_rotation_patheff_252d_base_v116_signal,
    f08rs_f08_relative_strength_rotation_patheff_504d_base_v117_signal,
    f08rs_f08_relative_strength_rotation_dnconc_252d_base_v118_signal,
    f08rs_f08_relative_strength_rotation_retherf_252d_base_v119_signal,
    f08rs_f08_relative_strength_rotation_updays_126d_base_v120_signal,
    f08rs_f08_relative_strength_rotation_tailasym_126d_base_v121_signal,
    f08rs_f08_relative_strength_rotation_retskew_252d_base_v122_signal,
    f08rs_f08_relative_strength_rotation_coskew_126d_base_v123_signal,
    f08rs_f08_relative_strength_rotation_slopehurst_252d_base_v124_signal,
    f08rs_f08_relative_strength_rotation_ereradj_126d_base_v125_signal,
    f08rs_f08_relative_strength_rotation_leadclean_126d_base_v126_signal,
    f08rs_f08_relative_strength_rotation_perswtret_63d_base_v127_signal,
    f08rs_f08_relative_strength_rotation_r2dir_252d_base_v128_signal,
    f08rs_f08_relative_strength_rotation_hurstreg_126d_base_v129_signal,
    f08rs_f08_relative_strength_rotation_erreg_63d_base_v130_signal,
    f08rs_f08_relative_strength_rotation_momreg_252d_base_v131_signal,
    f08rs_f08_relative_strength_rotation_sharpereg_126d_base_v132_signal,
    f08rs_f08_relative_strength_rotation_athstreak_126d_base_v133_signal,
    f08rs_f08_relative_strength_rotation_revpressure_252d_base_v134_signal,
    f08rs_f08_relative_strength_rotation_momsmooth_63d_base_v135_signal,
    f08rs_f08_relative_strength_rotation_resilience_252d_base_v136_signal,
    f08rs_f08_relative_strength_rotation_relbreadth_252d_base_v137_signal,
    f08rs_f08_relative_strength_rotation_slopez_126d_base_v138_signal,
    f08rs_f08_relative_strength_rotation_halflife_126d_base_v139_signal,
    f08rs_f08_relative_strength_rotation_radjblend_base_v140_signal,
    f08rs_f08_relative_strength_rotation_slopeconsist_252d_base_v141_signal,
    f08rs_f08_relative_strength_rotation_acftilt_252d_base_v142_signal,
    f08rs_f08_relative_strength_rotation_kelly_126d_base_v143_signal,
    f08rs_f08_relative_strength_rotation_dsrs_252d_base_v144_signal,
    f08rs_f08_relative_strength_rotation_trendshare_252d_base_v145_signal,
    f08rs_f08_relative_strength_rotation_mompred_252d_base_v146_signal,
    f08rs_f08_relative_strength_rotation_effsgn_504d_base_v147_signal,
    f08rs_f08_relative_strength_rotation_gainpain_252d_base_v148_signal,
    f08rs_f08_relative_strength_rotation_erankmom_126d_base_v149_signal,
    f08rs_f08_relative_strength_rotation_rsscore_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RELATIVE_STRENGTH_ROTATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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

    print("OK f08_relative_strength_rotation_base_076_150_claude: %d features pass" % n_features)
