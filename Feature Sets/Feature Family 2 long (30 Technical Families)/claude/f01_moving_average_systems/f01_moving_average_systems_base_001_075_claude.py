"""f01_moving_average_systems base features 001-075.

Domain: moving-average SYSTEMS — kernels (SMA/EMA/WMA/HMA/DEMA/TEMA/ZLEMA
/KAMA/T3/ALMA/McGinley/Wilder/median/quantile/trimmed/winsorized/geometric
/harmonic), MA distances (sign, distance, log-distance, z-score), slopes,
curvatures, ribbon counts/ordering, streaks, days-since-cross, percentile
ranks, stochastics, bounded transforms, %B, kernel comparisons, Hurst R/S,
MAD/std, regression slope/residual/R^2, correlation with time, dispersion.

These features are structurally distinct from base_076_150 (no shared
expression up to a window change). NaN policy: never fillna(<value>);
only replace([inf,-inf], nan) at the final return. Window > 21d uses
closeadj; <= 21d uses close. Each function spells its formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (kernel constructors). Each feature spells its full formula inline.
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _hma(s: pd.Series, n: int) -> pd.Series:
    half = max(2, n // 2); sqn = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _dema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n)
    return 2.0 * e1 - e2


def _tema(s: pd.Series, n: int) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _zlema(s: pd.Series, n: int) -> pd.Series:
    lag = max(1, (n - 1) // 2)
    return _ema(s + (s - s.shift(lag)), n)


def _kama(s: pd.Series, n: int, fast: int = 2, slow: int = 30) -> pd.Series:
    direction = (s - s.shift(n)).abs()
    volatility = s.diff().abs().rolling(n, min_periods=n).sum()
    er = direction / volatility.replace(0.0, np.nan)
    sc = (er * (2.0 / (fast + 1) - 2.0 / (slow + 1)) + 2.0 / (slow + 1)) ** 2
    out = pd.Series(np.nan, index=s.index, dtype=float)
    prev = np.nan; sv = s.values; scv = sc.values
    for i in range(len(s)):
        if i < n or not np.isfinite(scv[i]) or not np.isfinite(sv[i]):
            continue
        if not np.isfinite(prev):
            prev = sv[i]
        else:
            prev = prev + scv[i] * (sv[i] - prev)
        out.iat[i] = prev
    return out


def _alma(s: pd.Series, n: int, offset: float = 0.85, sigma: float = 6.0) -> pd.Series:
    m = offset * (n - 1); sig = n / sigma
    w = np.exp(-((np.arange(n) - m) ** 2) / (2.0 * sig * sig)); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _t3(s: pd.Series, n: int, vfactor: float = 0.7) -> pd.Series:
    e1 = _ema(s, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    e4 = _ema(e3, n); e5 = _ema(e4, n); e6 = _ema(e5, n)
    v = vfactor
    c1 = -v ** 3
    c2 = 3.0 * v ** 2 + 3.0 * v ** 3
    c3 = -6.0 * v ** 2 - 3.0 * v - 3.0 * v ** 3
    c4 = 1.0 + 3.0 * v + v ** 3 + 3.0 * v ** 2
    return c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3


def _mcginley(s: pd.Series, n: int) -> pd.Series:
    out = pd.Series(np.nan, index=s.index, dtype=float)
    prev = np.nan; sv = s.values
    seed_i = None
    for i in range(len(s)):
        if not np.isfinite(sv[i]):
            continue
        if seed_i is None and i >= n - 1:
            prev = float(np.mean(sv[i - n + 1:i + 1]))
            seed_i = i
            out.iat[i] = prev
        elif seed_i is not None and i > seed_i:
            denom = float(n) * (sv[i] / prev) ** 4
            if denom == 0.0 or not np.isfinite(denom):
                continue
            prev = prev + (sv[i] - prev) / denom
            out.iat[i] = prev
    return out


def _vwma(s: pd.Series, v: pd.Series, n: int) -> pd.Series:
    num = (s * v).rolling(n, min_periods=n).sum()
    den = v.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return num / den


def _trimmed_mean(s: pd.Series, n: int, trim: float = 0.1) -> pd.Series:
    def _f(x):
        k = int(np.floor(trim * len(x)))
        if k * 2 >= len(x):
            return np.nan
        y = np.sort(x)
        return float(np.mean(y[k:len(y) - k]))
    return s.rolling(n, min_periods=n).apply(_f, raw=True)


def _winsor_mean(s: pd.Series, n: int, q: float = 0.1) -> pd.Series:
    def _f(x):
        lo = np.quantile(x, q); hi = np.quantile(x, 1.0 - q)
        y = np.clip(x, lo, hi)
        return float(np.mean(y))
    return s.rolling(n, min_periods=n).apply(_f, raw=True)


def _hurst_rs(x):
    n = len(x)
    if n < 16:
        return np.nan
    y = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(y)):
        return np.nan
    mean = y.mean()
    dev = y - mean
    z = np.cumsum(dev)
    R = z.max() - z.min()
    S = y.std(ddof=0)
    if S == 0.0 or not np.isfinite(R / S) or R / S <= 0.0:
        return np.nan
    return float(np.log(R / S) / np.log(n))


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === Distance metrics using DIFFERENT kernels than 076-150 (T3/Wilder/McG) =


def f01ms_f01_moving_average_systems_logclose_t3_30d_base_v001_signal(closeadj):
    """log(close / T3(30)). T3 is a triple-smoothed kernel not used in 076-150."""
    n = 30
    e1 = _ema(closeadj, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    e4 = _ema(e3, n); e5 = _ema(e4, n); e6 = _ema(e5, n)
    v = 0.7
    c1 = -v ** 3
    c2 = 3.0 * v ** 2 + 3.0 * v ** 3
    c3 = -6.0 * v ** 2 - 3.0 * v - 3.0 * v ** 3
    c4 = 1.0 + 3.0 * v + v ** 3 + 3.0 * v ** 2
    t3 = c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3
    return np.log(closeadj / t3).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_close_wilder45_base_v002_signal(closeadj):
    """sign(close - WilderMA(45)). Wilder smoothing kernel-based trend filter.
    Discrete sign decorrelates from continuous log-distance features in 076-150."""
    n = 45
    w = closeadj.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()
    return np.sign(closeadj - w).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_mcginley_sma_60d_base_v003_signal(closeadj):
    """sign(McGinleyDynamic(60) - SMA(60)). Adaptive-kernel sign-vs-equal-weight.
    Discrete output decorrelates from continuous log-distance features."""
    return np.sign(_mcginley(closeadj, 60) - _sma(closeadj, 60)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_close_zlema18_base_v004_signal(close):
    """sign(close - ZLEMA(18)). Zero-lag EMA SIGN trend filter.
    Discrete decorrelates from continuous log-distance features in 076-150."""
    return np.sign(close - _zlema(close, 18)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_logclose_kama_35d_base_v005_signal(closeadj):
    """log(close / KAMA(35)). Adaptive Kaufman MA distance."""
    return np.log(closeadj / _kama(closeadj, 35)).replace([np.inf, -np.inf], np.nan)


# === KERNEL-PAIR differentials (NOT in 076-150) ============================


def f01ms_f01_moving_average_systems_t3_ema_diff_30d_base_v006_signal(closeadj):
    """log(T3(30) / EMA(30)). T3 vs simple EMA at same N."""
    n = 30
    e1 = _ema(closeadj, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    e4 = _ema(e3, n); e5 = _ema(e4, n); e6 = _ema(e5, n)
    v = 0.7
    c1 = -v ** 3; c2 = 3.0 * v ** 2 + 3.0 * v ** 3
    c3 = -6.0 * v ** 2 - 3.0 * v - 3.0 * v ** 3
    c4 = 1.0 + 3.0 * v + v ** 3 + 3.0 * v ** 2
    t3 = c1 * e6 + c2 * e5 + c3 * e4 + c4 * e3
    return np.log(t3 / _ema(closeadj, n)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_tema_dema_25d_base_v007_signal(closeadj):
    """sign(TEMA(25) - DEMA(25)). Triple vs double-smoothing crossover SIGN.
    Discrete output decorrelates from continuous log-ratio features in 076-150."""
    n = 25
    e1 = _ema(closeadj, n); e2 = _ema(e1, n); e3 = _ema(e2, n)
    tema = 3.0 * e1 - 3.0 * e2 + e3
    dema = 2.0 * e1 - e2
    return np.sign(tema - dema).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_kama_sma_diff_50d_base_v008_signal(closeadj):
    """log(KAMA(50) / SMA(50)). Adaptive vs equal-weight kernel differential."""
    return np.log(_kama(closeadj, 50) / _sma(closeadj, 50)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_zlema_ema_22d_base_v009_signal(close):
    """sign(ZLEMA(22) - EMA(22)). Zero-lag vs standard EMA crossover SIGN.
    Discrete decorrelates from continuous log-ratio features."""
    return np.sign(_zlema(close, 22) - _ema(close, 22)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_wilder_ema_diff_30d_base_v010_signal(closeadj):
    """log(WilderMA(30) / EMA(30)). Wilder vs standard EMA differential."""
    w = closeadj.ewm(alpha=1.0 / 30.0, adjust=False, min_periods=30).mean()
    return np.log(w / _ema(closeadj, 30)).replace([np.inf, -np.inf], np.nan)


# === TRIMMED / WINSORIZED means (robust kernels, NOT in 076-150) ==========


def f01ms_f01_moving_average_systems_trimmed_sma_diff_40d_base_v011_signal(closeadj):
    """log(TrimmedMean(40, 10%) / SMA(40)). Robust vs raw mean differential."""
    n = 40
    trim = _trimmed_mean(closeadj, n, 0.1)
    return np.log(trim / _sma(closeadj, n)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_winsor_sma_diff_60d_base_v012_signal(closeadj):
    """log(WinsorMean(60, 10%) / SMA(60)). Winsorized vs raw mean differential."""
    n = 60
    wins = _winsor_mean(closeadj, n, 0.1)
    return np.log(wins / _sma(closeadj, n)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_logclose_trimmed_18d_base_v013_signal(close):
    """log(close / TrimmedMean(close, 18, 10%)). Distance from robust kernel."""
    return np.log(close / _trimmed_mean(close, 18, 0.1)).replace([np.inf, -np.inf], np.nan)


# === STANDARDIZED distance (z-scores at NEW windows) =======================


def f01ms_f01_moving_average_systems_z_close_sma15_45d_base_v014_signal(close):
    """z-score: (close - SMA(15)) divided by 45d rolling std of close.
    Standardized short-MA distance — different normalization than 076-150."""
    n = 15
    m = _sma(close, n)
    sig = close.rolling(45, min_periods=45).std()
    return ((close - m) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_z_close_ema40_100d_base_v015_signal(closeadj):
    """z-score: (close - EMA(40)) divided by 100d rolling std of close."""
    e = _ema(closeadj, 40)
    sig = closeadj.rolling(100, min_periods=100).std()
    return ((closeadj - e) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_z_close_sma120_252d_base_v016_signal(closeadj):
    """z-score: (close - SMA(120)) divided by 252d rolling std of close.
    Long-window standardized distance."""
    m = _sma(closeadj, 120)
    sig = closeadj.rolling(252, min_periods=252).std()
    return ((closeadj - m) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === SIGMOID-BOUNDED distance (NEW transform, not in 076-150) ==============


def f01ms_f01_moving_average_systems_sigmoid_dist_ema20_base_v017_signal(close):
    """1/(1+exp(-x)) where x = (close-EMA(20)) / rolling-15d-mad."""
    e = _ema(close, 20)
    d = close - e
    mad = d.rolling(15, min_periods=15).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    z = d / mad.replace(0.0, np.nan)
    return (1.0 / (1.0 + np.exp(-z.clip(-30.0, 30.0)))).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sigmoid_ma_slope_60d_base_v018_signal(closeadj):
    """1/(1+exp(-x)) where x = SMA(60).diff(21) / 21d-std of SMA(60).diff(21).
    Bounded MA-slope momentum — structurally distinct from price-MA distance."""
    m = _sma(closeadj, 60)
    sl = m.diff(21)
    sig = sl.rolling(60, min_periods=60).std()
    z = sl / sig.replace(0.0, np.nan)
    return (1.0 / (1.0 + np.exp(-z.clip(-30.0, 30.0)))).replace([np.inf, -np.inf], np.nan)


# === %B-style stochastic of MA position (NEW transform) ====================


def f01ms_f01_moving_average_systems_pctB_close_sma20_band_base_v019_signal(close):
    """%B = (close - lower) / (upper - lower) for SMA(20)+/-2*std bands.
    Bollinger %B family — bounded [0,1] mostly. Window 20 -> close."""
    n = 20
    m = _sma(close, n)
    sd = close.rolling(n, min_periods=n).std()
    upper = m + 2.0 * sd
    lower = m - 2.0 * sd
    return ((close - lower) / (upper - lower).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_pctB_width_50d_base_v020_signal(closeadj):
    """Bollinger BAND-WIDTH (not %B): (upper - lower) / EMA(50). Width-only measure,
    decorrelated from position-based features."""
    n = 50
    e = _ema(closeadj, n)
    sd = closeadj.rolling(n, min_periods=n).std()
    return (4.0 * sd / e).replace([np.inf, -np.inf], np.nan)


# === MA-VELOCITY (instantaneous rate of change of MA, normalized) ==========


def f01ms_f01_moving_average_systems_ma_velocity_sma25_base_v021_signal(closeadj):
    """SMA(25).diff(5) / SMA(25). Velocity of mid-MA, normalized."""
    m = _sma(closeadj, 25)
    return (m.diff(5) / m).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ma_velocity_ema60_base_v022_signal(closeadj):
    """EMA(60).diff(10) / EMA(60). Velocity of long-MA."""
    e = _ema(closeadj, 60)
    return (e.diff(10) / e).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ma_velocity_hma20_base_v023_signal(close):
    """HMA(20).diff(3) / HMA(20). Velocity of Hull-MA."""
    h = _hma(close, 20)
    return (h.diff(3) / h).replace([np.inf, -np.inf], np.nan)


# === SLOPE-DIFF (cross-window MA slope spread, using .diff not pct_change) =


def f01ms_f01_moving_average_systems_slope_spread_sma10_40_base_v024_signal(close):
    """SMA(10).diff(5)/SMA(10) - SMA(40).diff(5)/SMA(40). Short-vs-mid slope spread."""
    s10 = _sma(close, 10); s40 = _sma(close, 40)
    return (s10.diff(5) / s10 - s40.diff(5) / s40).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_slope_spread_ema30_100_base_v025_signal(closeadj):
    """EMA(30).diff(10)/EMA(30) - EMA(100).diff(10)/EMA(100). Mid-vs-long EMA slope."""
    e30 = _ema(closeadj, 30); e100 = _ema(closeadj, 100)
    return (e30.diff(10) / e30 - e100.diff(10) / e100).replace([np.inf, -np.inf], np.nan)


# === DAYS-SINCE-CROSS at NEW MA pairs (not in 076-150) =====================


def f01ms_f01_moving_average_systems_daysince_sma_5_15_40d_base_v026_signal(close):
    """Bars since last (SMA(5) vs SMA(15)) sign-change, capped 40."""
    diff = _sma(close, 5) - _sma(close, 15)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _streak(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(40, min_periods=40).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_daysince_wma_15_45_80d_base_v027_signal(closeadj):
    """Bars since last (WMA(15) vs WMA(45)) sign-change, capped 80."""
    diff = _wma(closeadj, 15) - _wma(closeadj, 45)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _streak(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(80, min_periods=80).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === STREAK / consecutive-bars-above-MA (NEW class) ========================


def f01ms_f01_moving_average_systems_streak_above_sma10_50d_base_v028_signal(close):
    """Consecutive bars where close>SMA(10), capped 50."""
    sgn = (close > _sma(close, 10)).astype(float).where(~_sma(close, 10).isna())
    def _consec(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return sgn.rolling(50, min_periods=50).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_streak_below_ema40_120d_base_v029_signal(closeadj):
    """Consecutive bars where close<EMA(40), capped 120."""
    sgn = (closeadj < _ema(closeadj, 40)).astype(float).where(~_ema(closeadj, 40).isna())
    def _consec(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return sgn.rolling(120, min_periods=120).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === HURST R/S exponent (NEW class) ========================================


def f01ms_f01_moving_average_systems_hurst_close_60d_base_v030_signal(closeadj):
    """Hurst R/S exponent over 60d window of log-returns."""
    r = np.log(closeadj / closeadj.shift(1))
    return r.rolling(60, min_periods=60).apply(_hurst_rs, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_hurst_close_120d_base_v031_signal(closeadj):
    """Hurst R/S exponent over 120d window of log-returns."""
    r = np.log(closeadj / closeadj.shift(1))
    return r.rolling(120, min_periods=120).apply(_hurst_rs, raw=True).replace([np.inf, -np.inf], np.nan)


# === MAD / std ratio (NEW class — robust scale comparison) =================


def f01ms_f01_moving_average_systems_mad_std_ratio_30d_base_v032_signal(closeadj):
    """MAD/std of (close - SMA(30)) over 30 bars. Robust vs L2 scale ratio."""
    d = closeadj - _sma(closeadj, 30)
    mad = d.rolling(30, min_periods=30).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    sd = d.rolling(30, min_periods=30).std()
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_mad_std_ratio_ema_80d_base_v033_signal(closeadj):
    """MAD/std of (close - EMA(80)) over 80 bars."""
    d = closeadj - _ema(closeadj, 80)
    mad = d.rolling(80, min_periods=80).apply(lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True)
    sd = d.rolling(80, min_periods=80).std()
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === REGRESSION SLOPE of MA vs time (NEW class) ============================


def f01ms_f01_moving_average_systems_regslope_sma15_30d_base_v034_signal(close):
    """OLS slope of SMA(15) vs time index over 30 bars, normalized by mean."""
    m = _sma(close, 15)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var = np.sum((t - mean_t) ** 2)
        if var == 0.0 or not np.isfinite(mean_x) or mean_x == 0.0:
            return np.nan
        return float((cov / var) / mean_x)
    return m.rolling(30, min_periods=30).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_regslope_ema60_80d_base_v035_signal(closeadj):
    """OLS slope of EMA(60) vs time index over 80 bars, normalized by mean."""
    e = _ema(closeadj, 60)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var = np.sum((t - mean_t) ** 2)
        if var == 0.0 or not np.isfinite(mean_x) or mean_x == 0.0:
            return np.nan
        return float((cov / var) / mean_x)
    return e.rolling(80, min_periods=80).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# === R^2 of MA vs time (NEW class) =========================================


def f01ms_f01_moving_average_systems_rsq_sma30_60d_base_v036_signal(closeadj):
    """R^2 of OLS fit of SMA(30) vs time index over 60 bars."""
    m = _sma(closeadj, 30)
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var_t = np.sum((t - mean_t) ** 2)
        var_x = np.sum((x - mean_x) ** 2)
        if var_t == 0.0 or var_x == 0.0:
            return np.nan
        r = cov / np.sqrt(var_t * var_x)
        return float(r * r)
    return m.rolling(60, min_periods=60).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_rsq_ema100_120d_base_v037_signal(closeadj):
    """R^2 of OLS fit of EMA(100) vs time index over 120 bars. Long trend purity."""
    e = _ema(closeadj, 100)
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var_t = np.sum((t - mean_t) ** 2)
        var_x = np.sum((x - mean_x) ** 2)
        if var_t == 0.0 or var_x == 0.0:
            return np.nan
        r = cov / np.sqrt(var_t * var_x)
        return float(r * r)
    return e.rolling(120, min_periods=120).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === MA REGRESSION RESIDUAL std (NEW class) ================================


def f01ms_f01_moving_average_systems_regresid_sma40_50d_base_v038_signal(closeadj):
    """Std of residuals of OLS fit SMA(40) vs time, normalized by MA mean.
    Measures linearity-of-MA deviation."""
    m = _sma(closeadj, 40)
    def _resid_std(x):
        n = len(x); t = np.arange(n, dtype=float)
        mean_t = t.mean(); mean_x = x.mean()
        cov = np.sum((t - mean_t) * (x - mean_x))
        var_t = np.sum((t - mean_t) ** 2)
        if var_t == 0.0 or not np.isfinite(mean_x) or mean_x == 0.0:
            return np.nan
        b = cov / var_t
        a = mean_x - b * mean_t
        resid = x - (a + b * t)
        return float(np.std(resid) / abs(mean_x))
    return m.rolling(50, min_periods=50).apply(_resid_std, raw=True).replace([np.inf, -np.inf], np.nan)


# === STOCHASTIC %K of MA position ==========================================


def f01ms_f01_moving_average_systems_stoch_close_sma20_30d_base_v039_signal(close):
    """Stochastic %K of close against rolling-30d min/max of SMA(20).
    Position of price relative to MA's recent range."""
    n = 30
    m = _sma(close, 20)
    hi = m.rolling(n, min_periods=n).max()
    lo = m.rolling(n, min_periods=n).min()
    return ((close - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_stoch_ema_50_100d_base_v040_signal(closeadj):
    """Stochastic %K of EMA(50) against its rolling-100d min/max."""
    n = 100
    e = _ema(closeadj, 50)
    hi = e.rolling(n, min_periods=n).max()
    lo = e.rolling(n, min_periods=n).min()
    return ((e - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DEV-FROM-MA AUTOCORRELATION (NEW class) ===============================


def f01ms_f01_moving_average_systems_dev_autocorr_sma20_40d_base_v041_signal(close):
    """40d autocorr-lag-1 of (close - SMA(20)) residual."""
    d = close - _sma(close, 20)
    return d.rolling(40, min_periods=40).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_dev_autocorr_ema40_60d_base_v042_signal(closeadj):
    """60d autocorr-lag-5 of (close - EMA(40)) residual."""
    d = closeadj - _ema(closeadj, 40)
    return d.rolling(60, min_periods=60).apply(lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan, raw=False).replace([np.inf, -np.inf], np.nan)


# === RETURN AUTOCORRELATION (return persistence — MA-systems context) ======


def f01ms_f01_moving_average_systems_return_autocorr_30d_base_v043_signal(close):
    """30d autocorr-lag-1 of close.pct_change(). Return persistence signature."""
    r = close.pct_change()
    return r.rolling(30, min_periods=30).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_return_autocorr_100d_base_v044_signal(closeadj):
    """100d autocorr-lag-5 of close.pct_change()."""
    r = closeadj.pct_change()
    return r.rolling(100, min_periods=100).apply(lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan, raw=False).replace([np.inf, -np.inf], np.nan)


# === RETURN SKEW (NEW class) ===============================================


def f01ms_f01_moving_average_systems_return_skew_50d_base_v045_signal(closeadj):
    """50d rolling skew of log returns."""
    r = np.log(closeadj / closeadj.shift(1))
    return r.rolling(50, min_periods=50).skew().replace([np.inf, -np.inf], np.nan)


# === MA PERCENTILE-RANK at NEW windows =====================================


def f01ms_f01_moving_average_systems_rank_close_sma25_45d_base_v046_signal(close):
    """45d percentile rank of (close - SMA(25)). Short-distance rank."""
    d = close - _sma(close, 25)
    return d.rolling(45, min_periods=45).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_rank_logclose_ema80_180d_base_v047_signal(closeadj):
    """180d percentile rank of log(close/EMA(80))."""
    d = np.log(closeadj / _ema(closeadj, 80))
    return d.rolling(180, min_periods=180).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_rank_hma40_120d_base_v048_signal(closeadj):
    """120d percentile rank of (HMA(40) - SMA(40)). Hull-vs-SMA rank."""
    d = _hma(closeadj, 40) - _sma(closeadj, 40)
    return d.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === RIBBON DISPERSION at NEW window combos ================================


def f01ms_f01_moving_average_systems_ribbon_iqr_wma_70d_base_v049_signal(closeadj):
    """(Q75-Q25) of WMA ribbon {12, 24, 36, 48, 60, 70} / close.
    Interquartile dispersion of WMA fan."""
    w = [_wma(closeadj, k) for k in (12, 24, 36, 48, 60, 70)]
    mat = pd.concat(w, axis=1)
    iqr = mat.quantile(0.75, axis=1) - mat.quantile(0.25, axis=1)
    return (iqr / closeadj).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ribbon_position_50d_base_v050_signal(closeadj):
    """Rank of close within SMA ribbon {10,20,30,40,50}, in [0..5].
    Discrete position of price within MA fan."""
    sn = [_sma(closeadj, k) for k in (10, 20, 30, 40, 50)]
    cnt = pd.Series(0.0, index=closeadj.index)
    mask = ~sn[0].isna()
    for s in sn:
        cnt = cnt + (closeadj > s).astype(float)
        mask = mask & ~s.isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ribbon_skew_60d_base_v051_signal(closeadj):
    """Cross-sectional skew of EMA ribbon {12, 24, 36, 48, 60} per bar."""
    e = [_ema(closeadj, k) for k in (12, 24, 36, 48, 60)]
    mat = pd.concat(e, axis=1)
    return mat.skew(axis=1).replace([np.inf, -np.inf], np.nan)


# === KERNEL COMPARISONS at NEW pairings ====================================


def f01ms_f01_moving_average_systems_ma_acc_signum_30d_base_v052_signal(closeadj):
    """Sign of MA-acceleration: sign(SMA(30).diff(5).diff(5)). Discrete acceleration sign,
    structurally distinct from level-distance and slope features."""
    m = _sma(closeadj, 30)
    return np.sign(m.diff(5).diff(5)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_count_ma_pos_slopes_45d_base_v053_signal(closeadj):
    """Count of MAs with positive 21d slope among {SMA(20), EMA(30), WMA(40), HMA(25), DEMA(20)}.
    Range 0-5. Discrete count decorrelates from level-based features."""
    sigs = [
        (_sma(closeadj, 20).diff(21) > 0).astype(float),
        (_ema(closeadj, 30).diff(21) > 0).astype(float),
        (_wma(closeadj, 40).diff(21) > 0).astype(float),
        (_hma(closeadj, 25).diff(21) > 0).astype(float),
        ((2.0 * _ema(closeadj, 20) - _ema(_ema(closeadj, 20), 20)).diff(21) > 0).astype(float),
    ]
    mat = pd.concat(sigs, axis=1)
    mask = ~_sma(closeadj, 20).diff(21).isna() & ~_hma(closeadj, 25).diff(21).isna()
    return mat.sum(axis=1).where(mask).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ma_velocity_zscore_35d_base_v054_signal(closeadj):
    """z-score of EMA(35).diff(5) using its own rolling-90d mean/std.
    Standardized MA-velocity — distinct normalization."""
    e = _ema(closeadj, 35)
    v = e.diff(5)
    return ((v - v.rolling(90, min_periods=90).mean()) / v.rolling(90, min_periods=90).std()).replace([np.inf, -np.inf], np.nan)


# === BOUNDED arctan/tanh at NEW windows ====================================


def f01ms_f01_moving_average_systems_arctan_dist_sma10_base_v055_signal(close):
    """arctan of (close - SMA(10)) / 10d-std. Short bounded distance."""
    n = 10
    m = _sma(close, n)
    sig = close.rolling(n, min_periods=n).std()
    return np.arctan((close - m) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_tanh_dist_ema120_base_v056_signal(closeadj):
    """tanh of (close - EMA(120)) / 60d-std of price. Long bounded distance."""
    e = _ema(closeadj, 120)
    sig = closeadj.rolling(60, min_periods=60).std()
    return np.tanh((closeadj - e) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === KERNEL CROSS-CORRELATION (NEW class) ==================================


def f01ms_f01_moving_average_systems_corr_sma_ema_50d_base_v057_signal(closeadj):
    """50d Pearson corr between SMA(15) and EMA(15). Kernel agreement quality."""
    return _sma(closeadj, 15).rolling(50, min_periods=50).corr(_ema(closeadj, 15)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_corr_hma_wma_80d_base_v058_signal(closeadj):
    """80d Pearson corr between HMA(20) and WMA(20). Hull-vs-WMA tracking."""
    return _hma(closeadj, 20).rolling(80, min_periods=80).corr(_wma(closeadj, 20)).replace([np.inf, -np.inf], np.nan)


# === SIGN-CROSS PRICE features (NEW pair) ==================================


def f01ms_f01_moving_average_systems_sign_close_wma15_base_v059_signal(close):
    """sign(close - WMA(15)). WMA-based short trend filter."""
    return np.sign(close - _wma(close, 15)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_close_zlema35_base_v060_signal(closeadj):
    """sign(close - ZLEMA(35)). Zero-lag EMA trend filter."""
    return np.sign(closeadj - _zlema(closeadj, 35)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_wma10_wma35_base_v061_signal(close):
    """sign(WMA(10) - WMA(35)). WMA-WMA crossover sign at fast/slow."""
    return np.sign(_wma(close, 10) - _wma(close, 35)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_sign_tema30_tema60_base_v062_signal(closeadj):
    """sign(TEMA(30) - TEMA(60)). TEMA pair crossover sign."""
    return np.sign(_tema(closeadj, 30) - _tema(closeadj, 60)).replace([np.inf, -np.inf], np.nan)


# === MA SLOPE PERSISTENCE / FRACTION POSITIVE ==============================


def f01ms_f01_moving_average_systems_slope_positive_frac_sma25_45d_base_v063_signal(closeadj):
    """Fraction of last 45 bars where SMA(25).diff(5) > 0."""
    m = _sma(closeadj, 25)
    pos = (m.diff(5) > 0).astype(float).where(~m.diff(5).isna())
    return pos.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_slope_positive_frac_ema80_120d_base_v064_signal(closeadj):
    """Fraction of last 120 bars where EMA(80).diff(21) > 0."""
    e = _ema(closeadj, 80)
    pos = (e.diff(21) > 0).astype(float).where(~e.diff(21).isna())
    return pos.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === MA CURVATURE at NEW kernels ===========================================


def f01ms_f01_moving_average_systems_curv_ema25_norm_base_v065_signal(closeadj):
    """(EMA(25) - 2*EMA(25).shift(5) + EMA(25).shift(10)) / 5d-std of EMA(25)."""
    e = _ema(closeadj, 25)
    c = e - 2.0 * e.shift(5) + e.shift(10)
    sig = e.rolling(20, min_periods=20).std()
    return (c / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_curv_wma50_norm_base_v066_signal(closeadj):
    """(WMA(50) - 2*WMA(50).shift(10) + WMA(50).shift(20)) / 40d-std of WMA(50)."""
    w = _wma(closeadj, 50)
    c = w - 2.0 * w.shift(10) + w.shift(20)
    sig = w.rolling(40, min_periods=40).std()
    return (c / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MA DOLLAR-VOLUME EFFICIENCY (uses volume) =============================


def f01ms_f01_moving_average_systems_dv_efficiency_30d_base_v067_signal(closeadj, volume):
    """|SMA(closeadj,30).diff(10)| / SMA(volume*close, 30). Dollar-volume MA-move efficiency."""
    m = _sma(closeadj, 30)
    dv = (closeadj * volume).rolling(30, min_periods=30).mean()
    return ((m.diff(10).abs()) / dv).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_volprice_ma_corr_60d_base_v068_signal(closeadj, volume):
    """60d Pearson corr between SMA(closeadj,15) and SMA(volume,15)."""
    return _sma(closeadj, 15).rolling(60, min_periods=60).corr(_sma(volume, 15)).replace([np.inf, -np.inf], np.nan)


# === MA-LAGGED CORR (NEW pattern, with-time alignment) =====================


def f01ms_f01_moving_average_systems_corr_close_sma_lag20_60d_base_v069_signal(closeadj):
    """60d corr between closeadj and SMA(15).shift(20). Lag-MA tracking."""
    return closeadj.rolling(60, min_periods=60).corr(_sma(closeadj, 15).shift(20)).replace([np.inf, -np.inf], np.nan)


# === MA WIDTH (rolling max-min of MA itself, NEW class) ====================


def f01ms_f01_moving_average_systems_ma_range_sma30_50d_base_v070_signal(closeadj):
    """(rolling-50-max(SMA(30)) - rolling-50-min(SMA(30))) / close. MA-range / price."""
    m = _sma(closeadj, 30)
    rng = m.rolling(50, min_periods=50).max() - m.rolling(50, min_periods=50).min()
    return (rng / closeadj).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ma_range_ema60_120d_base_v071_signal(closeadj):
    """(rolling-120-max(EMA(60)) - rolling-120-min(EMA(60))) / EMA(60)."""
    e = _ema(closeadj, 60)
    rng = e.rolling(120, min_periods=120).max() - e.rolling(120, min_periods=120).min()
    return (rng / e).replace([np.inf, -np.inf], np.nan)


# === MA-CROSSOVER MAGNITUDE-Z (NEW combo) ==================================


def f01ms_f01_moving_average_systems_xover_mag_z_sma_30_90_base_v072_signal(closeadj):
    """z-score (against 60d window) of |SMA(30) - SMA(90)| / closeadj."""
    mag = (_sma(closeadj, 30) - _sma(closeadj, 90)).abs() / closeadj
    return ((mag - mag.rolling(60, min_periods=60).mean()) / mag.rolling(60, min_periods=60).std()).replace([np.inf, -np.inf], np.nan)


# === KAMA EFFICIENCY RATIO (raw KER, NEW class) ============================


def f01ms_f01_moving_average_systems_ker_25d_base_v073_signal(closeadj):
    """Kaufman efficiency ratio at N=25.
    |close - close.shift(25)| / sum(|close.diff()|, 25)."""
    n = 25
    direction = (closeadj - closeadj.shift(n)).abs()
    volatility = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f01ms_f01_moving_average_systems_ker_80d_base_v074_signal(closeadj):
    """Kaufman efficiency ratio at N=80. Long-window trend efficiency."""
    n = 80
    direction = (closeadj - closeadj.shift(n)).abs()
    volatility = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MA REVERSION RATE (NEW class) =========================================


def f01ms_f01_moving_average_systems_reversion_rate_sma20_50d_base_v075_signal(closeadj):
    """50d rolling count of sign-flips of (close - SMA(20)) divided by 50.
    Cross-frequency normalized — a distinct flavor from 076-150 crossfreq raw counts."""
    diff = closeadj - _sma(closeadj, 20)
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return (flip.rolling(50, min_periods=50).sum() / 50.0).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f01_moving_average_systems_base_001_075_REGISTRY = {
    "f01ms_f01_moving_average_systems_logclose_t3_30d_base_v001_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_t3_30d_base_v001_signal},
    "f01ms_f01_moving_average_systems_sign_close_wilder45_base_v002_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_wilder45_base_v002_signal},
    "f01ms_f01_moving_average_systems_sign_mcginley_sma_60d_base_v003_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_mcginley_sma_60d_base_v003_signal},
    "f01ms_f01_moving_average_systems_sign_close_zlema18_base_v004_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_close_zlema18_base_v004_signal},
    "f01ms_f01_moving_average_systems_logclose_kama_35d_base_v005_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_logclose_kama_35d_base_v005_signal},
    "f01ms_f01_moving_average_systems_t3_ema_diff_30d_base_v006_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_t3_ema_diff_30d_base_v006_signal},
    "f01ms_f01_moving_average_systems_sign_tema_dema_25d_base_v007_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_tema_dema_25d_base_v007_signal},
    "f01ms_f01_moving_average_systems_kama_sma_diff_50d_base_v008_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_kama_sma_diff_50d_base_v008_signal},
    "f01ms_f01_moving_average_systems_sign_zlema_ema_22d_base_v009_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_zlema_ema_22d_base_v009_signal},
    "f01ms_f01_moving_average_systems_wilder_ema_diff_30d_base_v010_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_wilder_ema_diff_30d_base_v010_signal},
    "f01ms_f01_moving_average_systems_trimmed_sma_diff_40d_base_v011_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_trimmed_sma_diff_40d_base_v011_signal},
    "f01ms_f01_moving_average_systems_winsor_sma_diff_60d_base_v012_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_winsor_sma_diff_60d_base_v012_signal},
    "f01ms_f01_moving_average_systems_logclose_trimmed_18d_base_v013_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_logclose_trimmed_18d_base_v013_signal},
    "f01ms_f01_moving_average_systems_z_close_sma15_45d_base_v014_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_z_close_sma15_45d_base_v014_signal},
    "f01ms_f01_moving_average_systems_z_close_ema40_100d_base_v015_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_z_close_ema40_100d_base_v015_signal},
    "f01ms_f01_moving_average_systems_z_close_sma120_252d_base_v016_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_z_close_sma120_252d_base_v016_signal},
    "f01ms_f01_moving_average_systems_sigmoid_dist_ema20_base_v017_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sigmoid_dist_ema20_base_v017_signal},
    "f01ms_f01_moving_average_systems_sigmoid_ma_slope_60d_base_v018_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sigmoid_ma_slope_60d_base_v018_signal},
    "f01ms_f01_moving_average_systems_pctB_close_sma20_band_base_v019_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_pctB_close_sma20_band_base_v019_signal},
    "f01ms_f01_moving_average_systems_pctB_width_50d_base_v020_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_pctB_width_50d_base_v020_signal},
    "f01ms_f01_moving_average_systems_ma_velocity_sma25_base_v021_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_velocity_sma25_base_v021_signal},
    "f01ms_f01_moving_average_systems_ma_velocity_ema60_base_v022_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_velocity_ema60_base_v022_signal},
    "f01ms_f01_moving_average_systems_ma_velocity_hma20_base_v023_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_ma_velocity_hma20_base_v023_signal},
    "f01ms_f01_moving_average_systems_slope_spread_sma10_40_base_v024_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_slope_spread_sma10_40_base_v024_signal},
    "f01ms_f01_moving_average_systems_slope_spread_ema30_100_base_v025_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_spread_ema30_100_base_v025_signal},
    "f01ms_f01_moving_average_systems_daysince_sma_5_15_40d_base_v026_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_daysince_sma_5_15_40d_base_v026_signal},
    "f01ms_f01_moving_average_systems_daysince_wma_15_45_80d_base_v027_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_daysince_wma_15_45_80d_base_v027_signal},
    "f01ms_f01_moving_average_systems_streak_above_sma10_50d_base_v028_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_streak_above_sma10_50d_base_v028_signal},
    "f01ms_f01_moving_average_systems_streak_below_ema40_120d_base_v029_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_streak_below_ema40_120d_base_v029_signal},
    "f01ms_f01_moving_average_systems_hurst_close_60d_base_v030_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_hurst_close_60d_base_v030_signal},
    "f01ms_f01_moving_average_systems_hurst_close_120d_base_v031_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_hurst_close_120d_base_v031_signal},
    "f01ms_f01_moving_average_systems_mad_std_ratio_30d_base_v032_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_mad_std_ratio_30d_base_v032_signal},
    "f01ms_f01_moving_average_systems_mad_std_ratio_ema_80d_base_v033_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_mad_std_ratio_ema_80d_base_v033_signal},
    "f01ms_f01_moving_average_systems_regslope_sma15_30d_base_v034_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_regslope_sma15_30d_base_v034_signal},
    "f01ms_f01_moving_average_systems_regslope_ema60_80d_base_v035_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_regslope_ema60_80d_base_v035_signal},
    "f01ms_f01_moving_average_systems_rsq_sma30_60d_base_v036_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rsq_sma30_60d_base_v036_signal},
    "f01ms_f01_moving_average_systems_rsq_ema100_120d_base_v037_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rsq_ema100_120d_base_v037_signal},
    "f01ms_f01_moving_average_systems_regresid_sma40_50d_base_v038_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_regresid_sma40_50d_base_v038_signal},
    "f01ms_f01_moving_average_systems_stoch_close_sma20_30d_base_v039_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_stoch_close_sma20_30d_base_v039_signal},
    "f01ms_f01_moving_average_systems_stoch_ema_50_100d_base_v040_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_stoch_ema_50_100d_base_v040_signal},
    "f01ms_f01_moving_average_systems_dev_autocorr_sma20_40d_base_v041_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_dev_autocorr_sma20_40d_base_v041_signal},
    "f01ms_f01_moving_average_systems_dev_autocorr_ema40_60d_base_v042_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_dev_autocorr_ema40_60d_base_v042_signal},
    "f01ms_f01_moving_average_systems_return_autocorr_30d_base_v043_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_return_autocorr_30d_base_v043_signal},
    "f01ms_f01_moving_average_systems_return_autocorr_100d_base_v044_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_return_autocorr_100d_base_v044_signal},
    "f01ms_f01_moving_average_systems_return_skew_50d_base_v045_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_return_skew_50d_base_v045_signal},
    "f01ms_f01_moving_average_systems_rank_close_sma25_45d_base_v046_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_rank_close_sma25_45d_base_v046_signal},
    "f01ms_f01_moving_average_systems_rank_logclose_ema80_180d_base_v047_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_logclose_ema80_180d_base_v047_signal},
    "f01ms_f01_moving_average_systems_rank_hma40_120d_base_v048_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_rank_hma40_120d_base_v048_signal},
    "f01ms_f01_moving_average_systems_ribbon_iqr_wma_70d_base_v049_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_iqr_wma_70d_base_v049_signal},
    "f01ms_f01_moving_average_systems_ribbon_position_50d_base_v050_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_position_50d_base_v050_signal},
    "f01ms_f01_moving_average_systems_ribbon_skew_60d_base_v051_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ribbon_skew_60d_base_v051_signal},
    "f01ms_f01_moving_average_systems_ma_acc_signum_30d_base_v052_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_acc_signum_30d_base_v052_signal},
    "f01ms_f01_moving_average_systems_count_ma_pos_slopes_45d_base_v053_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_count_ma_pos_slopes_45d_base_v053_signal},
    "f01ms_f01_moving_average_systems_ma_velocity_zscore_35d_base_v054_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_velocity_zscore_35d_base_v054_signal},
    "f01ms_f01_moving_average_systems_arctan_dist_sma10_base_v055_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_arctan_dist_sma10_base_v055_signal},
    "f01ms_f01_moving_average_systems_tanh_dist_ema120_base_v056_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_tanh_dist_ema120_base_v056_signal},
    "f01ms_f01_moving_average_systems_corr_sma_ema_50d_base_v057_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_sma_ema_50d_base_v057_signal},
    "f01ms_f01_moving_average_systems_corr_hma_wma_80d_base_v058_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_hma_wma_80d_base_v058_signal},
    "f01ms_f01_moving_average_systems_sign_close_wma15_base_v059_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_close_wma15_base_v059_signal},
    "f01ms_f01_moving_average_systems_sign_close_zlema35_base_v060_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_close_zlema35_base_v060_signal},
    "f01ms_f01_moving_average_systems_sign_wma10_wma35_base_v061_signal": {"inputs": ["close"], "func": f01ms_f01_moving_average_systems_sign_wma10_wma35_base_v061_signal},
    "f01ms_f01_moving_average_systems_sign_tema30_tema60_base_v062_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_sign_tema30_tema60_base_v062_signal},
    "f01ms_f01_moving_average_systems_slope_positive_frac_sma25_45d_base_v063_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_positive_frac_sma25_45d_base_v063_signal},
    "f01ms_f01_moving_average_systems_slope_positive_frac_ema80_120d_base_v064_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_slope_positive_frac_ema80_120d_base_v064_signal},
    "f01ms_f01_moving_average_systems_curv_ema25_norm_base_v065_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_ema25_norm_base_v065_signal},
    "f01ms_f01_moving_average_systems_curv_wma50_norm_base_v066_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_curv_wma50_norm_base_v066_signal},
    "f01ms_f01_moving_average_systems_dv_efficiency_30d_base_v067_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_dv_efficiency_30d_base_v067_signal},
    "f01ms_f01_moving_average_systems_volprice_ma_corr_60d_base_v068_signal": {"inputs": ["closeadj", "volume"], "func": f01ms_f01_moving_average_systems_volprice_ma_corr_60d_base_v068_signal},
    "f01ms_f01_moving_average_systems_corr_close_sma_lag20_60d_base_v069_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_corr_close_sma_lag20_60d_base_v069_signal},
    "f01ms_f01_moving_average_systems_ma_range_sma30_50d_base_v070_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_range_sma30_50d_base_v070_signal},
    "f01ms_f01_moving_average_systems_ma_range_ema60_120d_base_v071_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ma_range_ema60_120d_base_v071_signal},
    "f01ms_f01_moving_average_systems_xover_mag_z_sma_30_90_base_v072_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_xover_mag_z_sma_30_90_base_v072_signal},
    "f01ms_f01_moving_average_systems_ker_25d_base_v073_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ker_25d_base_v073_signal},
    "f01ms_f01_moving_average_systems_ker_80d_base_v074_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_ker_80d_base_v074_signal},
    "f01ms_f01_moving_average_systems_reversion_rate_sma20_50d_base_v075_signal": {"inputs": ["closeadj"], "func": f01ms_f01_moving_average_systems_reversion_rate_sma20_50d_base_v075_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f01_moving_average_systems_base_001_075_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
