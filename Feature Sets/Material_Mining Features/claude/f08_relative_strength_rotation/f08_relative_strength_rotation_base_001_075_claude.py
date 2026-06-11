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
    # Kaufman efficiency ratio: net directional move / sum of absolute moves
    net = (close - close.shift(w)).abs()
    path = close.diff().abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return net / path.replace(0, np.nan)


def _f08_rs_exponent(logret, w):
    # Hurst-like rescaled-range (R/S) exponent proxy over a window of log returns
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


def _f08_run_signed(logret, w):
    # net signed run-length proxy: (up days - down days) / window
    up = (logret > 0).astype(float)
    dn = (logret < 0).astype(float)
    return (up.rolling(w, min_periods=max(2, w // 2)).sum()
            - dn.rolling(w, min_periods=max(2, w // 2)).sum()) / float(w)


def _f08_curstreak(logret):
    # current signed consecutive run length (positive=up streak, negative=down streak)
    s = np.sign(logret).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    run = s.groupby(grp).cumcount() + 1.0
    return run * s


def _f08_mom(close, w):
    return close / close.shift(w) - 1.0


def _f08_riskadj_mom(close, w, volw):
    r = close / close.shift(w) - 1.0
    vol = close.pct_change().rolling(volw, min_periods=max(2, volw // 2)).std()
    return r / vol.replace(0, np.nan)


def _f08_selfrel_mom(close, w, histw):
    # momentum z-scored vs its own long history -> self-relative rotation proxy
    m = _f08_mom(close, w)
    return _z(m, histw)


# ============================================================
# --- Efficiency ratio family (trend persistence) ---

# Kaufman efficiency ratio over 21d (short-term trend cleanliness)
def f08rs_f08_relative_strength_rotation_effr_21d_base_v001_signal(closeadj):
    b = _f08_efficiency_ratio(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio over 63d
def f08rs_f08_relative_strength_rotation_effr_63d_base_v002_signal(closeadj):
    b = _f08_efficiency_ratio(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio over 126d
def f08rs_f08_relative_strength_rotation_effr_126d_base_v003_signal(closeadj):
    b = _f08_efficiency_ratio(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio over 252d, signed by net direction (clean trend with sign)
def f08rs_f08_relative_strength_rotation_effrsgn_252d_base_v004_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 252)
    direction = np.sign(closeadj - closeadj.shift(252))
    b = er * direction
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 63d z-scored vs its own 252d history (de-trended cleanliness)
def f08rs_f08_relative_strength_rotation_effrz_63d_base_v005_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 63)
    b = _z(er, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio term structure: short 21d minus long 126d (regime of cleanliness)
def f08rs_f08_relative_strength_rotation_effrspr_21v126_base_v006_signal(closeadj):
    s = _f08_efficiency_ratio(closeadj, 21)
    l = _f08_efficiency_ratio(closeadj, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency-ratio momentum: 63d ER change over a month (improving/decaying trend)
def f08rs_f08_relative_strength_rotation_effrmom_63d_base_v007_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 63)
    b = er - er.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 504d (multi-year persistence)
def f08rs_f08_relative_strength_rotation_effr_504d_base_v008_signal(closeadj):
    b = _f08_efficiency_ratio(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio 126d percentile-ranked vs its own 504d history
def f08rs_f08_relative_strength_rotation_effrrank_126d_base_v009_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 126)
    b = _rank(er, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Hurst-like R/S family (long-memory / persistence) ---

# Hurst-like R/S exponent over 63d log returns
def f08rs_f08_relative_strength_rotation_hurst_63d_base_v010_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_rs_exponent(lr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-like R/S exponent over 126d log returns
def f08rs_f08_relative_strength_rotation_hurst_126d_base_v011_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_rs_exponent(lr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst-like R/S exponent over 252d log returns
def f08rs_f08_relative_strength_rotation_hurst_252d_base_v012_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_rs_exponent(lr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-scale variance-ratio Hurst slope over 126d (aggregation-scaling persistence)
def f08rs_f08_relative_strength_rotation_hurstdist_126d_base_v013_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    v21 = lr.rolling(21).sum().rolling(126, min_periods=63).var()
    # Hurst from log(var(q)) ~ (2H) log(q) using q=5 and q=21 points
    y5 = np.log((v5 + 1e-12) / (v1 + 1e-12))
    y21 = np.log((v21 + 1e-12) / (v1 + 1e-12))
    slope = (y21 - y5) / (np.log(21.0) - np.log(5.0))
    b = slope / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst term structure: 63d minus 252d (memory regime shift)
def f08rs_f08_relative_strength_rotation_hurstspr_63v252_base_v014_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = _f08_rs_exponent(lr, 63)
    l = _f08_rs_exponent(lr, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst 126d z-scored vs its own 252d history (de-trended memory)
def f08rs_f08_relative_strength_rotation_hurstz_126d_base_v015_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    h = _f08_rs_exponent(lr, 126)
    b = _z(h, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst momentum: 126d Hurst change over a quarter (regime drift toward trending)
def f08rs_f08_relative_strength_rotation_hurstmom_126d_base_v016_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    h = _f08_rs_exponent(lr, 126)
    b = h - h.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence signed by direction: (Hurst-0.5) x net-trend sign, 252d
def f08rs_f08_relative_strength_rotation_hurstsgn_252d_base_v017_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    h = _f08_rs_exponent(lr, 252)
    direction = np.sign(closeadj - closeadj.shift(252))
    b = (h - 0.5) * direction
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Autocorrelation of returns family ---

# lag-1 autocorrelation of daily log returns over 63d (momentum vs reversal)
def f08rs_f08_relative_strength_rotation_acf1_63d_base_v018_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_autocorr(lr, 63, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-1 autocorrelation over 126d
def f08rs_f08_relative_strength_rotation_acf1_126d_base_v019_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_autocorr(lr, 126, 1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-5 (weekly) autocorrelation over 126d
def f08rs_f08_relative_strength_rotation_acf5_126d_base_v020_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_autocorr(lr, 126, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lag-21 (monthly) autocorrelation of returns over 252d
def f08rs_f08_relative_strength_rotation_acf21_252d_base_v021_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = _f08_autocorr(lr, 252, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorrelation of 5d-aggregated returns, lag-1 over 252d (weekly momentum memory)
def f08rs_f08_relative_strength_rotation_acfwk_252d_base_v022_signal(closeadj):
    wkret = np.log(closeadj.replace(0, np.nan)).diff(5)
    b = _f08_autocorr(wkret, 252, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr lag-1 z-scored vs its own 252d history (de-trended persistence)
def f08rs_f08_relative_strength_rotation_acf1z_63d_base_v023_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    ac = _f08_autocorr(lr, 63, 1)
    b = _z(ac, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# autocorr term structure: lag-1 over 63d minus over 252d
def f08rs_f08_relative_strength_rotation_acfspr_63v252_base_v024_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = _f08_autocorr(lr, 63, 1)
    l = _f08_autocorr(lr, 252, 1)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio (Lo-MacKinlay) proxy: var(5d ret)/(5*var(1d ret)) over 126d
def f08rs_f08_relative_strength_rotation_varratio_126d_base_v025_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(126, min_periods=63).var()
    v5 = lr.rolling(5).sum().rolling(126, min_periods=63).var()
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio proxy over 252d, 21d aggregation
def f08rs_f08_relative_strength_rotation_varratio_252d_base_v026_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    v1 = lr.rolling(252, min_periods=126).var()
    v21 = lr.rolling(21).sum().rolling(252, min_periods=126).var()
    b = v21 / (21.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Run-length / streak family ---

# magnitude-weighted signed run balance over 21d (up-strength minus down-strength)
def f08rs_f08_relative_strength_rotation_runbal_21d_base_v027_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)
    weighted = (sgn * lr.abs().pow(0.5)).rolling(21, min_periods=11).sum()
    scale = lr.abs().pow(0.5).rolling(21, min_periods=11).sum()
    b = weighted / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# streak-weighted directional balance over 63d: sum of signed streak lengths / window
def f08rs_f08_relative_strength_rotation_runbal_63d_base_v028_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    st = _f08_curstreak(lr)
    b = st.rolling(63, min_periods=32).mean() / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current streak length x cumulative move during the streak (magnitude-weighted run)
def f08rs_f08_relative_strength_rotation_curstreak_base_v029_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    runlen = s.groupby(grp).cumcount() + 1.0
    cummove = lr.groupby(grp).cumsum()
    b = runlen * cummove
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current streak length z-scored vs its own 252d history (extreme streak)
def f08rs_f08_relative_strength_rotation_streakz_252d_base_v030_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    st = _f08_curstreak(lr)
    b = _z(st, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest cumulative up-streak gain within 63d (max persistent advance magnitude)
def f08rs_f08_relative_strength_rotation_maxuprun_63d_base_v031_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    cummove = lr.groupby(grp).cumsum()
    upmove = cummove.where(s > 0, 0.0)
    b = upmove.rolling(63, min_periods=32).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest cumulative down-streak loss within 63d (max persistent decline magnitude)
def f08rs_f08_relative_strength_rotation_maxdnrun_63d_base_v032_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    s = np.sign(lr).fillna(0.0)
    grp = (s != s.shift(1)).cumsum()
    cummove = lr.groupby(grp).cumsum()
    dnmove = cummove.where(s < 0, 0.0)
    b = dnmove.rolling(63, min_periods=32).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-persistence: mean of sign(r_t)*sign(r_{t-1}) over 63d (return clustering)
def f08rs_f08_relative_strength_rotation_signpersist_63d_base_v033_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    prod = np.sign(lr) * np.sign(lr.shift(1)) * (lr.abs() * lr.shift(1).abs()).pow(0.25)
    b = prod.rolling(63, min_periods=32).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional-day imbalance momentum: 21d run balance change over a month
def f08rs_f08_relative_strength_rotation_runbalmom_63d_base_v034_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = (lr > 0).astype(float).rolling(21, min_periods=11).mean()
    rb = up - 0.5
    b = rb - rb.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Self-relative momentum (rotation proxy) family ---

# 252d momentum z-scored vs its own 504d history (self-relative RS)
def f08rs_f08_relative_strength_rotation_selfmom_252d_base_v035_signal(closeadj):
    b = _f08_selfrel_mom(closeadj, 252, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d momentum z-scored vs its own 504d history
def f08rs_f08_relative_strength_rotation_selfmom_126d_base_v036_signal(closeadj):
    b = _f08_selfrel_mom(closeadj, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d momentum z-scored vs its own 252d history
def f08rs_f08_relative_strength_rotation_selfmom_63d_base_v037_signal(closeadj):
    b = _f08_selfrel_mom(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 12-1 momentum (252d skip last 21d) z-scored vs own 504d history
def f08rs_f08_relative_strength_rotation_mom121z_base_v038_signal(closeadj):
    m = closeadj.shift(21) / closeadj.shift(252) - 1.0
    b = _z(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-relative momentum percentile rank: 126d momentum vs own 504d distribution
def f08rs_f08_relative_strength_rotation_selfmomrank_126d_base_v039_signal(closeadj):
    m = _f08_mom(closeadj, 126)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-horizon momentum tilt: annualized 63d ROC minus annualized 252d ROC
def f08rs_f08_relative_strength_rotation_momvsavg_63d_base_v040_signal(closeadj):
    short = (closeadj / closeadj.shift(63) - 1.0) * (252.0 / 63.0)
    long = closeadj / closeadj.shift(252) - 1.0
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-relative momentum spread: 63d selfmom minus 252d selfmom (rotation tilt)
def f08rs_f08_relative_strength_rotation_selfmomspr_base_v041_signal(closeadj):
    s = _f08_selfrel_mom(closeadj, 63, 252)
    l = _f08_selfrel_mom(closeadj, 252, 504)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Risk-adjusted relative strength family ---

# risk-adjusted momentum: 63d ROC / 63d daily vol (Sharpe-like RS)
def f08rs_f08_relative_strength_rotation_radjmom_63d_base_v042_signal(closeadj):
    b = _f08_riskadj_mom(closeadj, 63, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted RS with horizon mismatch: 21d ROC scaled by 126d vol (fast RS thrust)
def f08rs_f08_relative_strength_rotation_radjmom_126d_base_v043_signal(closeadj):
    r = closeadj / closeadj.shift(21) - 1.0
    vol = closeadj.pct_change().rolling(126, min_periods=63).std() * np.sqrt(21.0)
    b = r / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum: 252d ROC / 252d vol
def f08rs_f08_relative_strength_rotation_radjmom_252d_base_v044_signal(closeadj):
    b = _f08_riskadj_mom(closeadj, 252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted RS z-scored vs own 252d history (de-trended Sharpe RS)
def f08rs_f08_relative_strength_rotation_radjmomz_126d_base_v045_signal(closeadj):
    r = _f08_riskadj_mom(closeadj, 126, 126)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ulcer-adjusted RS over 126d: net return divided by RMS drawdown (pain-adjusted)
def f08rs_f08_relative_strength_rotation_sharpe_126d_base_v046_signal(closeadj):
    ret = closeadj / closeadj.shift(126) - 1.0
    peak = closeadj.rolling(126, min_periods=63).max()
    dd = closeadj / peak.replace(0, np.nan) - 1.0
    ulcer = (dd ** 2).rolling(126, min_periods=63).mean().pow(0.5)
    b = ret / ulcer.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sortino-RS thrust: change over a quarter in 126d (mean-return / downside-deviation)
def f08rs_f08_relative_strength_rotation_sortino_126d_base_v047_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    mu = lr.rolling(126, min_periods=63).mean()
    downside = lr.clip(upper=0.0)
    dd = downside.rolling(126, min_periods=63).std()
    sortino = mu / dd.replace(0, np.nan)
    b = sortino - sortino.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted momentum term structure: 63d radj minus 252d radj
def f08rs_f08_relative_strength_rotation_radjspr_63v252_base_v048_signal(closeadj):
    s = _f08_riskadj_mom(closeadj, 63, 63)
    l = _f08_riskadj_mom(closeadj, 252, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Additional persistence / trend-quality features ---

# trend slope (log-price OLS slope) over 63d, vol-normalized (clean trend strength)
def f08rs_f08_relative_strength_rotation_trslope_63d_base_v049_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _slp(a):
        if np.isnan(a).any():
            return np.nan
        xc = np.arange(len(a), dtype=float)
        xc = xc - xc.mean()
        denom = (xc ** 2).sum()
        if denom <= 0:
            return np.nan
        return float(np.dot(xc, a - a.mean()) / denom)
    slope = lp.rolling(63, min_periods=32).apply(_slp, raw=True)
    vol = lp.diff().rolling(63, min_periods=32).std()
    b = slope / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend slope over 126d, vol-normalized
def f08rs_f08_relative_strength_rotation_trslope_126d_base_v050_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _slp(a):
        if np.isnan(a).any():
            return np.nan
        xc = np.arange(len(a), dtype=float)
        xc = xc - xc.mean()
        denom = (xc ** 2).sum()
        if denom <= 0:
            return np.nan
        return float(np.dot(xc, a - a.mean()) / denom)
    slope = lp.rolling(126, min_periods=63).apply(_slp, raw=True)
    vol = lp.diff().rolling(126, min_periods=63).std()
    b = slope / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of log-price linear trend over 63d (trend reliability)
def f08rs_f08_relative_strength_rotation_trendr2_63d_base_v051_signal(closeadj):
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
    b = lp.rolling(63, min_periods=32).apply(_r2, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# R-squared of log-price linear trend over 252d (long trend reliability)
def f08rs_f08_relative_strength_rotation_trendr2_252d_base_v052_signal(closeadj):
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
    b = lp.rolling(252, min_periods=126).apply(_r2, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend R2 signed by slope direction over 126d (directional trend quality)
def f08rs_f08_relative_strength_rotation_trendr2sgn_126d_base_v053_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))

    def _r2s(a):
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
        return float(np.sign(beta) * (fit ** 2).sum() / ss)
    b = lp.rolling(126, min_periods=63).apply(_r2s, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# MA-distance persistence: fraction of 126d price stayed above its 63d MA
def f08rs_f08_relative_strength_rotation_aboveMA_126d_base_v054_signal(closeadj):
    ma = _mean(closeadj, 63)
    above = (closeadj > ma).astype(float)
    b = above.rolling(126, min_periods=63).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 126d MA in vol units (relative strength vs own trend baseline)
def f08rs_f08_relative_strength_rotation_madistvol_126d_base_v055_signal(closeadj):
    ma = _mean(closeadj, 126)
    dist = closeadj / ma.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = dist / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net log return over 126d divided by max excursion (path efficiency)
def f08rs_f08_relative_strength_rotation_patheff_126d_base_v056_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = lp - lp.shift(126)
    hi = lp.rolling(126, min_periods=63).max()
    lo = lp.rolling(126, min_periods=63).min()
    b = net / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of up-weeks over 252d (weekly relative strength breadth)
def f08rs_f08_relative_strength_rotation_upweeks_252d_base_v057_signal(closeadj):
    wk = np.log(closeadj.replace(0, np.nan)).diff(5)
    up = (wk > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of up-months (21d) over 252d
def f08rs_f08_relative_strength_rotation_upmonths_252d_base_v058_signal(closeadj):
    mo = np.log(closeadj.replace(0, np.nan)).diff(21)
    up = (mo > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jump dominance over 63d: largest squared daily return as a share of total variance
def f08rs_f08_relative_strength_rotation_consist_63d_base_v059_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sq = lr ** 2
    biggest = sq.rolling(63, min_periods=21).max()
    total = sq.rolling(63, min_periods=21).sum()
    b = biggest / total.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Mann-Kendall-like trend monotonicity: rank-correlation of price with time over 252d
def f08rs_f08_relative_strength_rotation_consist_252d_base_v060_signal(closeadj):
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
    b = lp.rolling(252, min_periods=126).apply(_tau, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside/downside semivariance asymmetry over 252d (volatility-of-direction tilt)
def f08rs_f08_relative_strength_rotation_updnasym_252d_base_v061_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    upvar = (lr.clip(lower=0.0) ** 2).rolling(252, min_periods=126).mean()
    dnvar = (lr.clip(upper=0.0) ** 2).rolling(252, min_periods=126).mean()
    b = np.log((upvar + 1e-12) / (dnvar + 1e-12))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gain/pain ratio: 126d sum of gains over sum of losses minus 1
def f08rs_f08_relative_strength_rotation_gainpain_126d_base_v062_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    up = lr.clip(lower=0.0).rolling(126, min_periods=63).sum()
    dn = (-lr.clip(upper=0.0)).rolling(126, min_periods=63).sum()
    b = up / dn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum acceleration: 63d ROC now minus 63d ROC a quarter ago (RS thrust)
def f08rs_f08_relative_strength_rotation_momaccel_63d_base_v063_signal(closeadj):
    m = _f08_mom(closeadj, 63)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon momentum blend rank: avg of 63/126/252 ROC ranked vs 504d history
def f08rs_f08_relative_strength_rotation_blendmom_base_v064_signal(closeadj):
    m1 = _rank(_f08_mom(closeadj, 63), 504)
    m2 = _rank(_f08_mom(closeadj, 126), 504)
    m3 = _rank(_f08_mom(closeadj, 252), 504)
    b = (m1 + m2 + m3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum agreement across horizons: tanh-squashed blend of 21/63/126/252 ROC
def f08rs_f08_relative_strength_rotation_momagree_base_v065_signal(closeadj):
    s1 = np.tanh(5.0 * _f08_mom(closeadj, 21))
    s2 = np.tanh(5.0 * _f08_mom(closeadj, 63))
    s3 = np.tanh(5.0 * _f08_mom(closeadj, 126))
    s4 = np.tanh(5.0 * _f08_mom(closeadj, 252))
    b = (s1 + s2 + s3 + s4) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend smoothness: 1 - (vol of detrended residual / total vol) over 126d
def f08rs_f08_relative_strength_rotation_smooth_126d_base_v066_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    ma = lp.rolling(21, min_periods=10).mean()
    resid_vol = (lp - ma).rolling(126, min_periods=63).std()
    tot_vol = lp.rolling(126, min_periods=63).std()
    b = 1.0 - resid_vol / tot_vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling skewness of daily returns over 126d (return distribution asymmetry)
def f08rs_f08_relative_strength_rotation_retskew_126d_base_v067_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    b = lr.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of total 252d move captured in best 21d window (concentration of RS)
def f08rs_f08_relative_strength_rotation_momconc_252d_base_v068_signal(closeadj):
    lp = np.log(closeadj.replace(0, np.nan))
    net = (lp - lp.shift(252)).abs()
    best = lp.diff(21).abs().rolling(252, min_periods=126).max()
    b = best / net.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# efficiency ratio scaled by trend direction strength: ER x |momentum|, 126d
def f08rs_f08_relative_strength_rotation_ermomint_126d_base_v069_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 126)
    m = _f08_mom(closeadj, 126)
    b = er * m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Hurst x efficiency ratio interaction over 126d (combined persistence quality)
def f08rs_f08_relative_strength_rotation_hurster_126d_base_v070_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    h = _f08_rs_exponent(lr, 126)
    er = _f08_efficiency_ratio(closeadj, 126)
    b = (h - 0.5) * er
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling Calmar-like RS: 252d return over 252d max drawdown magnitude
def f08rs_f08_relative_strength_rotation_calmar_252d_base_v071_signal(closeadj):
    ret = closeadj / closeadj.shift(252) - 1.0
    peak = closeadj.rolling(252, min_periods=126).max()
    dd = (closeadj / peak.replace(0, np.nan) - 1.0).rolling(252, min_periods=126).min().abs()
    b = ret / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Wald-Wolfowitz runs-test z over 126d: too few runs => trending persistence
def f08rs_f08_relative_strength_rotation_tstat_126d_base_v072_signal(closeadj):
    lr = np.log(closeadj.replace(0, np.nan)).diff()
    sgn = np.sign(lr)

    def _runs_z(a):
        a = a[~np.isnan(a)]
        a = a[a != 0]
        m = len(a)
        if m < 20:
            return np.nan
        n_pos = float((a > 0).sum())
        n_neg = float((a < 0).sum())
        if n_pos == 0 or n_neg == 0:
            return np.nan
        runs = 1 + int((a[1:] != a[:-1]).sum())
        mu = 2.0 * n_pos * n_neg / m + 1.0
        var = (2.0 * n_pos * n_neg * (2.0 * n_pos * n_neg - m)) / (m * m * (m - 1.0))
        if var <= 0:
            return np.nan
        return float((runs - mu) / np.sqrt(var))
    b = sgn.rolling(126, min_periods=63).apply(_runs_z, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# momentum persistence: correlation of 21d ROC with its own 21d-lagged value, 252d
def f08rs_f08_relative_strength_rotation_mompersist_252d_base_v073_signal(closeadj):
    m = _f08_mom(closeadj, 21)
    b = m.rolling(252, min_periods=126).corr(m.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-direction efficiency over 21d signed, smoothed (short clean-trend tilt)
def f08rs_f08_relative_strength_rotation_effsm_21d_base_v074_signal(closeadj):
    er = _f08_efficiency_ratio(closeadj, 21)
    direction = np.sign(closeadj - closeadj.shift(21))
    b = (er * direction).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# relative-strength regime distance: 126d radj-momentum minus its 504d median
def f08rs_f08_relative_strength_rotation_rsregime_126d_base_v075_signal(closeadj):
    r = _f08_riskadj_mom(closeadj, 126, 126)
    med = r.rolling(504, min_periods=126).median()
    b = r - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08rs_f08_relative_strength_rotation_effr_21d_base_v001_signal,
    f08rs_f08_relative_strength_rotation_effr_63d_base_v002_signal,
    f08rs_f08_relative_strength_rotation_effr_126d_base_v003_signal,
    f08rs_f08_relative_strength_rotation_effrsgn_252d_base_v004_signal,
    f08rs_f08_relative_strength_rotation_effrz_63d_base_v005_signal,
    f08rs_f08_relative_strength_rotation_effrspr_21v126_base_v006_signal,
    f08rs_f08_relative_strength_rotation_effrmom_63d_base_v007_signal,
    f08rs_f08_relative_strength_rotation_effr_504d_base_v008_signal,
    f08rs_f08_relative_strength_rotation_effrrank_126d_base_v009_signal,
    f08rs_f08_relative_strength_rotation_hurst_63d_base_v010_signal,
    f08rs_f08_relative_strength_rotation_hurst_126d_base_v011_signal,
    f08rs_f08_relative_strength_rotation_hurst_252d_base_v012_signal,
    f08rs_f08_relative_strength_rotation_hurstdist_126d_base_v013_signal,
    f08rs_f08_relative_strength_rotation_hurstspr_63v252_base_v014_signal,
    f08rs_f08_relative_strength_rotation_hurstz_126d_base_v015_signal,
    f08rs_f08_relative_strength_rotation_hurstmom_126d_base_v016_signal,
    f08rs_f08_relative_strength_rotation_hurstsgn_252d_base_v017_signal,
    f08rs_f08_relative_strength_rotation_acf1_63d_base_v018_signal,
    f08rs_f08_relative_strength_rotation_acf1_126d_base_v019_signal,
    f08rs_f08_relative_strength_rotation_acf5_126d_base_v020_signal,
    f08rs_f08_relative_strength_rotation_acf21_252d_base_v021_signal,
    f08rs_f08_relative_strength_rotation_acfwk_252d_base_v022_signal,
    f08rs_f08_relative_strength_rotation_acf1z_63d_base_v023_signal,
    f08rs_f08_relative_strength_rotation_acfspr_63v252_base_v024_signal,
    f08rs_f08_relative_strength_rotation_varratio_126d_base_v025_signal,
    f08rs_f08_relative_strength_rotation_varratio_252d_base_v026_signal,
    f08rs_f08_relative_strength_rotation_runbal_21d_base_v027_signal,
    f08rs_f08_relative_strength_rotation_runbal_63d_base_v028_signal,
    f08rs_f08_relative_strength_rotation_curstreak_base_v029_signal,
    f08rs_f08_relative_strength_rotation_streakz_252d_base_v030_signal,
    f08rs_f08_relative_strength_rotation_maxuprun_63d_base_v031_signal,
    f08rs_f08_relative_strength_rotation_maxdnrun_63d_base_v032_signal,
    f08rs_f08_relative_strength_rotation_signpersist_63d_base_v033_signal,
    f08rs_f08_relative_strength_rotation_runbalmom_63d_base_v034_signal,
    f08rs_f08_relative_strength_rotation_selfmom_252d_base_v035_signal,
    f08rs_f08_relative_strength_rotation_selfmom_126d_base_v036_signal,
    f08rs_f08_relative_strength_rotation_selfmom_63d_base_v037_signal,
    f08rs_f08_relative_strength_rotation_mom121z_base_v038_signal,
    f08rs_f08_relative_strength_rotation_selfmomrank_126d_base_v039_signal,
    f08rs_f08_relative_strength_rotation_momvsavg_63d_base_v040_signal,
    f08rs_f08_relative_strength_rotation_selfmomspr_base_v041_signal,
    f08rs_f08_relative_strength_rotation_radjmom_63d_base_v042_signal,
    f08rs_f08_relative_strength_rotation_radjmom_126d_base_v043_signal,
    f08rs_f08_relative_strength_rotation_radjmom_252d_base_v044_signal,
    f08rs_f08_relative_strength_rotation_radjmomz_126d_base_v045_signal,
    f08rs_f08_relative_strength_rotation_sharpe_126d_base_v046_signal,
    f08rs_f08_relative_strength_rotation_sortino_126d_base_v047_signal,
    f08rs_f08_relative_strength_rotation_radjspr_63v252_base_v048_signal,
    f08rs_f08_relative_strength_rotation_trslope_63d_base_v049_signal,
    f08rs_f08_relative_strength_rotation_trslope_126d_base_v050_signal,
    f08rs_f08_relative_strength_rotation_trendr2_63d_base_v051_signal,
    f08rs_f08_relative_strength_rotation_trendr2_252d_base_v052_signal,
    f08rs_f08_relative_strength_rotation_trendr2sgn_126d_base_v053_signal,
    f08rs_f08_relative_strength_rotation_aboveMA_126d_base_v054_signal,
    f08rs_f08_relative_strength_rotation_madistvol_126d_base_v055_signal,
    f08rs_f08_relative_strength_rotation_patheff_126d_base_v056_signal,
    f08rs_f08_relative_strength_rotation_upweeks_252d_base_v057_signal,
    f08rs_f08_relative_strength_rotation_upmonths_252d_base_v058_signal,
    f08rs_f08_relative_strength_rotation_consist_63d_base_v059_signal,
    f08rs_f08_relative_strength_rotation_consist_252d_base_v060_signal,
    f08rs_f08_relative_strength_rotation_updnasym_252d_base_v061_signal,
    f08rs_f08_relative_strength_rotation_gainpain_126d_base_v062_signal,
    f08rs_f08_relative_strength_rotation_momaccel_63d_base_v063_signal,
    f08rs_f08_relative_strength_rotation_blendmom_base_v064_signal,
    f08rs_f08_relative_strength_rotation_momagree_base_v065_signal,
    f08rs_f08_relative_strength_rotation_smooth_126d_base_v066_signal,
    f08rs_f08_relative_strength_rotation_retskew_126d_base_v067_signal,
    f08rs_f08_relative_strength_rotation_momconc_252d_base_v068_signal,
    f08rs_f08_relative_strength_rotation_ermomint_126d_base_v069_signal,
    f08rs_f08_relative_strength_rotation_hurster_126d_base_v070_signal,
    f08rs_f08_relative_strength_rotation_calmar_252d_base_v071_signal,
    f08rs_f08_relative_strength_rotation_tstat_126d_base_v072_signal,
    f08rs_f08_relative_strength_rotation_mompersist_252d_base_v073_signal,
    f08rs_f08_relative_strength_rotation_effsm_21d_base_v074_signal,
    f08rs_f08_relative_strength_rotation_rsregime_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_RELATIVE_STRENGTH_ROTATION_REGISTRY_001_075 = REGISTRY


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

    print("OK f08_relative_strength_rotation_base_001_075_claude: %d features pass" % n_features)
