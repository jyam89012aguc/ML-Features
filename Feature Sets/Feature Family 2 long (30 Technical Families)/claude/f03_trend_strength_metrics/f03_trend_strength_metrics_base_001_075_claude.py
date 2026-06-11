"""f03_trend_strength_metrics base features 001-075.

Domain: trend STRENGTH / persistence — how strong and persistent is the
current trend (regardless of direction). Classic indicators: ADX, DMI+,
DMI-, Aroon, Vortex, Choppiness, TSI, KST, Kaufman efficiency ratio,
Hurst exponent, R^2 of OLS, Mann-Kendall S, polynomial fit, monotonic
streaks, variance ratio, sign-agreement counts.

Each feature is a fully-expanded def block with its formula inline.
Window > 21d uses closeadj. Windows <= 21d use close. NaN policy: never
fillna(0); only replace([inf,-inf], nan) at return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (each feature wraps a helper inside its own unique expression)
# ---------------------------------------------------------------------------


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev_close = close.shift(1)
    a = (high - low).abs()
    b = (high - prev_close).abs()
    c = (low - prev_close).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _plus_dm(high: pd.Series, low: pd.Series) -> pd.Series:
    up = high.diff()
    dn = -low.diff()
    pdm = np.where((up > dn) & (up > 0.0), up, 0.0)
    return pd.Series(pdm, index=high.index, dtype=float)


def _minus_dm(high: pd.Series, low: pd.Series) -> pd.Series:
    up = high.diff()
    dn = -low.diff()
    mdm = np.where((dn > up) & (dn > 0.0), dn, 0.0)
    return pd.Series(mdm, index=high.index, dtype=float)


def _aroon_up(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmax(x)))) / n, raw=True
    )


def _aroon_dn(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmin(x)))) / n, raw=True
    )


def _hurst_rs(s: pd.Series, n: int) -> pd.Series:
    def _calc(x: np.ndarray) -> float:
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        r = np.diff(np.log(x))
        if r.size < 8:
            return np.nan
        m = r.mean()
        y = r - m
        z = np.cumsum(y)
        R = z.max() - z.min()
        S = r.std(ddof=1)
        if S <= 0 or R <= 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(r)))
    return s.rolling(n, min_periods=n).apply(_calc, raw=True)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# --- ADX / DMI core family (varied n) --------------------------------------


def f03ts_f03_trend_strength_metrics_adx_14d_base_v001_signal(high, low, close):
    """Wilder ADX(14). Classic trend-strength magnitude oscillator."""
    n = 14
    tr = _tr(high, low, close)
    atr = _wilder(tr, n)
    pdm = _wilder(_plus_dm(high, low), n)
    mdm = _wilder(_minus_dm(high, low), n)
    pdi = 100.0 * pdm / atr.replace(0.0, np.nan)
    mdi = 100.0 * mdm / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    return adx.replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_adx_50d_base_v002_signal(high, low, closeadj):
    """Wilder ADX(50). Long-horizon trend-strength magnitude."""
    n = 50
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdm = _wilder(_plus_dm(high, low), n)
    mdm = _wilder(_minus_dm(high, low), n)
    pdi = 100.0 * pdm / atr.replace(0.0, np.nan)
    mdi = 100.0 * mdm / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    return adx.replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dmidiff_21d_base_v003_signal(high, low, close):
    """(+DI - -DI) Wilder N=21. Directional movement net imbalance."""
    n = 21
    tr = _tr(high, low, close)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    return (pdi - mdi).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dmiratio_30d_base_v004_signal(high, low, closeadj):
    """Streak count: bars-since-last-sign-change of (+DI - -DI) Wilder N=30,
    capped at 100. Long streak = persistent directional dominance."""
    n = 30
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    s = np.sign(pdi - mdi)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _streak(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 100.0
        return float(len(x) - 1 - idx[-1])
    return flip.rolling(100, min_periods=100).apply(_streak, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_adxstrong_60d_base_v005_signal(high, low, closeadj):
    """Fraction of last 60 bars where ADX(14) > 25 — count of strong-trend bars."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    flag = (adx > 25.0).astype(float).where(~adx.isna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_pdi_14d_base_v006_signal(high, low, close):
    """+DI Wilder 14 standalone (bull directional strength)."""
    n = 14
    tr = _tr(high, low, close)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    return pdi.replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_mdi_40d_base_v007_signal(high, low, closeadj):
    """-DI Wilder 40 standalone (bear directional strength)."""
    n = 40
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    return mdi.replace([np.inf, -np.inf], np.nan)


# --- Aroon family ----------------------------------------------------------


def f03ts_f03_trend_strength_metrics_aroonosc_14d_base_v008_signal(close):
    """Aroon oscillator (up - down), N=14, on close."""
    n = 14
    au = _aroon_up(close, n)
    ad = _aroon_dn(close, n)
    return (au - ad).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonosc_50d_base_v009_signal(closeadj):
    """Aroon oscillator N=50 on closeadj — long-horizon."""
    n = 50
    au = _aroon_up(closeadj, n)
    ad = _aroon_dn(closeadj, n)
    return (au - ad).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroondiff_25d_base_v010_signal(high, low):
    """Aroon-up on high MINUS Aroon-down on low, N=25 — uses OHLC, structurally
    differs from close-based aroon."""
    n = 25
    au = _aroon_up(high, n)
    ad = _aroon_dn(low, n)
    return (au - ad).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonsign_30d_base_v011_signal(closeadj):
    """sign(Aroon-up - Aroon-down) at N=30. Discrete bull/bear regime."""
    n = 30
    au = _aroon_up(closeadj, n)
    ad = _aroon_dn(closeadj, n)
    return np.sign(au - ad).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonconv_21d_base_v012_signal(close):
    """Aroon up + down at N=21 — convergence (low) vs divergence (high)."""
    n = 21
    au = _aroon_up(close, n)
    ad = _aroon_dn(close, n)
    return (au + ad).replace([np.inf, -np.inf], np.nan)


# --- Vortex family ---------------------------------------------------------


def f03ts_f03_trend_strength_metrics_vortexdiff_14d_base_v013_signal(high, low, close):
    """VI+ - VI- at N=14. Vortex difference — trend direction strength."""
    n = 14
    tr_n = _tr(high, low, close).rolling(n, min_periods=n).sum()
    vp = (high - low.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    vm = (low - high.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    return (vp - vm).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_vortexabs_30d_base_v014_signal(high, low, closeadj):
    """|VI+ - VI-| at N=30 — magnitude of vortex spread (direction-agnostic)."""
    n = 30
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    vp = (high - low.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    vm = (low - high.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    return (vp - vm).abs().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_vortexratio_60d_base_v015_signal(high, low, closeadj):
    """log(VI+ / VI-) at N=60 — symmetric vortex log-ratio."""
    n = 60
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    vp = (high - low.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    vm = (low - high.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    return np.log(vp.replace(0.0, np.nan) / vm.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Choppiness Index ------------------------------------------------------


def f03ts_f03_trend_strength_metrics_chop_14d_base_v016_signal(high, low, close):
    """Choppiness Index N=14 (negated so higher = more trending)."""
    n = 14
    tr_n = _tr(high, low, close).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return (-chop).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_chop_40d_base_v017_signal(high, low, closeadj):
    """Choppiness Index N=40 (negated). Mid-horizon."""
    n = 40
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return (-chop).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_choprank_120d_base_v018_signal(high, low, closeadj):
    """120d percentile rank of Choppiness(40). High rank = very choppy regime."""
    n = 40
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return chop.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- TSI (True Strength Index) family --------------------------------------


def f03ts_f03_trend_strength_metrics_tsi_25_13_base_v019_signal(close):
    """TSI(r=25, s=13). Classic. Double-smoothed momentum / its abs."""
    diff = close.diff()
    num = diff.ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    den = diff.abs().ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    return (100.0 * num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tsi_50_25_base_v020_signal(closeadj):
    """TSI(r=50, s=25) on closeadj. Long-horizon double-smoothed."""
    diff = closeadj.diff()
    num = diff.ewm(span=50, adjust=False, min_periods=50).mean().ewm(span=25, adjust=False, min_periods=25).mean()
    den = diff.abs().ewm(span=50, adjust=False, min_periods=50).mean().ewm(span=25, adjust=False, min_periods=25).mean()
    return (100.0 * num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tsiabs_25_13_base_v021_signal(close):
    """|TSI(25,13)| — direction-agnostic trend strength."""
    diff = close.diff()
    num = diff.ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    den = diff.abs().ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    return (100.0 * num.abs() / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- KST (Know Sure Thing) -------------------------------------------------


def f03ts_f03_trend_strength_metrics_kst_30d_base_v022_signal(closeadj):
    """KST = sum(w_i * SMA(ROC(close, n_i), s_i)) — composite trend strength."""
    r1 = closeadj.pct_change(10).rolling(10, min_periods=10).mean()
    r2 = closeadj.pct_change(15).rolling(10, min_periods=10).mean()
    r3 = closeadj.pct_change(20).rolling(10, min_periods=10).mean()
    r4 = closeadj.pct_change(30).rolling(15, min_periods=15).mean()
    return (1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kstlong_120d_base_v023_signal(closeadj):
    """Long-horizon KST variant (longer ROC windows). Distinct shape from v022."""
    r1 = closeadj.pct_change(40).rolling(20, min_periods=20).mean()
    r2 = closeadj.pct_change(60).rolling(20, min_periods=20).mean()
    r3 = closeadj.pct_change(90).rolling(30, min_periods=30).mean()
    r4 = closeadj.pct_change(120).rolling(40, min_periods=40).mean()
    return (1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4).replace([np.inf, -np.inf], np.nan)


# --- Kaufman efficiency ratio family ---------------------------------------


def f03ts_f03_trend_strength_metrics_kefr_10d_base_v024_signal(close):
    """Kaufman efficiency ratio at N=10 — |close-close[-10]| / sum(|diff|,10)."""
    n = 10
    direction = (close - close.shift(n)).abs()
    volatility = close.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kefr_40d_base_v025_signal(closeadj):
    """Kaufman efficiency ratio at N=40."""
    n = 40
    direction = (closeadj - closeadj.shift(n)).abs()
    volatility = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kefr_120d_base_v026_signal(closeadj):
    """Kaufman efficiency ratio at N=120 — slow."""
    n = 120
    direction = (closeadj - closeadj.shift(n)).abs()
    volatility = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kefrsigned_30d_base_v027_signal(closeadj):
    """Signed efficiency: sign(close-close[-30]) * KER(30)."""
    n = 30
    raw = closeadj - closeadj.shift(n)
    volatility = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    out = raw / volatility.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kefrhl_25d_base_v028_signal(high, low):
    """Efficiency ratio on midpoint (high+low)/2 at N=25 — OHLC variant."""
    n = 25
    mid = 0.5 * (high + low)
    direction = (mid - mid.shift(n)).abs()
    volatility = mid.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- R^2 / regression family ----------------------------------------------


def f03ts_f03_trend_strength_metrics_r2lin_20d_base_v029_signal(close):
    """R^2 of OLS regression of close on time, N=20. Trend linearity."""
    n = 20
    def _r2(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        yhat = a[0] * t + a[1]
        ss_res = float(np.sum((x - yhat) ** 2))
        ss_tot = float(np.sum((x - x.mean()) ** 2))
        if ss_tot <= 0:
            return np.nan
        return 1.0 - ss_res / ss_tot
    return close.rolling(n, min_periods=n).apply(_r2, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_r2lin_63d_base_v030_signal(closeadj):
    """R^2 of OLS regression of closeadj on time, N=63 — quarterly."""
    n = 63
    def _r2(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        yhat = a[0] * t + a[1]
        ss_res = float(np.sum((x - yhat) ** 2))
        ss_tot = float(np.sum((x - x.mean()) ** 2))
        if ss_tot <= 0:
            return np.nan
        return 1.0 - ss_res / ss_tot
    return closeadj.rolling(n, min_periods=n).apply(_r2, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_r2log_120d_base_v031_signal(closeadj):
    """R^2 of OLS regression of log(closeadj) on time, N=120 — exponential trend fit."""
    n = 120
    def _r2(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0):
            return np.nan
        y = np.log(x)
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, y, 1)
        yhat = a[0] * t + a[1]
        ss_res = float(np.sum((y - yhat) ** 2))
        ss_tot = float(np.sum((y - y.mean()) ** 2))
        if ss_tot <= 0:
            return np.nan
        return 1.0 - ss_res / ss_tot
    return closeadj.rolling(n, min_periods=n).apply(_r2, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_logregslp_60d_base_v032_signal(closeadj):
    """Slope of OLS log(closeadj) ~ time at N=60. Exponential trend rate (annualized scale)."""
    n = 60
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0):
            return np.nan
        y = np.log(x)
        t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    return closeadj.rolling(n, min_periods=n).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_regrres_30d_base_v033_signal(closeadj):
    """Residual standard deviation of OLS(close ~ t), N=30 — small = strong linear trend."""
    n = 30
    def _resstd(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        yhat = a[0] * t + a[1]
        return float(np.std(x - yhat, ddof=1))
    return closeadj.rolling(n, min_periods=n).apply(_resstd, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_robtrend_40d_base_v034_signal(closeadj):
    """Robust trend strength: |slope| / MAD(residuals), N=40."""
    n = 40
    def _calc(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        resid = x - (a[0] * t + a[1])
        mad = float(np.median(np.abs(resid - np.median(resid))))
        if mad <= 0:
            return np.nan
        return abs(float(a[0])) / mad
    return closeadj.rolling(n, min_periods=n).apply(_calc, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_poly2coef_50d_base_v035_signal(closeadj):
    """Quadratic coefficient of degree-2 polyfit, N=50. Detects accelerating/decelerating trends."""
    n = 50
    def _quad(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float) / n
        a = np.polyfit(t, x, 2)
        return float(a[0])
    return closeadj.rolling(n, min_periods=n).apply(_quad, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_lastresid_30d_base_v036_signal(closeadj):
    """Last-bar residual of OLS(close~t,N=30) normalized by residual std. Z-score of last point."""
    n = 30
    def _resz(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        resid = x - (a[0] * t + a[1])
        sd = float(np.std(resid, ddof=1))
        if sd <= 0:
            return np.nan
        return float(resid[-1] / sd)
    return closeadj.rolling(n, min_periods=n).apply(_resz, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Hurst / variance-ratio / persistence ---------------------------------


def f03ts_f03_trend_strength_metrics_hurstrs_80d_base_v037_signal(closeadj):
    """Hurst R/S exponent N=80. >0.5 trending, <0.5 mean-reverting."""
    return _hurst_rs(closeadj, 80)


def f03ts_f03_trend_strength_metrics_hurstrs_160d_base_v038_signal(closeadj):
    """Hurst R/S exponent N=160. Long-horizon."""
    return _hurst_rs(closeadj, 160)


def f03ts_f03_trend_strength_metrics_varratio_30d_base_v039_signal(closeadj):
    """Lo-MacKinlay variance ratio: var(r_q)/(q*var(r_1)) - 1, q=5, N=30."""
    n = 30
    q = 5
    r1 = np.log(closeadj).diff()
    rq = np.log(closeadj).diff(q)
    v1 = r1.rolling(n, min_periods=n).var(ddof=1)
    vq = rq.rolling(n, min_periods=n).var(ddof=1)
    return (vq / (q * v1.replace(0.0, np.nan)) - 1.0).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_varratio_100d_base_v040_signal(closeadj):
    """Variance ratio q=10, N=100."""
    n = 100
    q = 10
    r1 = np.log(closeadj).diff()
    rq = np.log(closeadj).diff(q)
    v1 = r1.rolling(n, min_periods=n).var(ddof=1)
    vq = rq.rolling(n, min_periods=n).var(ddof=1)
    return (vq / (q * v1.replace(0.0, np.nan)) - 1.0).replace([np.inf, -np.inf], np.nan)


# --- Mann-Kendall family ---------------------------------------------------


def f03ts_f03_trend_strength_metrics_mks_30d_base_v041_signal(closeadj):
    """Mann-Kendall S statistic (normalized by N*(N-1)/2), N=30."""
    n = 30
    norm = n * (n - 1) / 2.0
    def _mk(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    return closeadj.rolling(n, min_periods=n).apply(_mk, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_mksabs_60d_base_v042_signal(closeadj):
    """120d pct-rank of Mann-Kendall S statistic (N=60). Rank transform of MK
    — structurally distinct from raw R^2/MK linear measures."""
    n = 60
    norm = n * (n - 1) / 2.0
    def _mk(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    raw = closeadj.rolling(n, min_periods=n).apply(_mk, raw=True)
    return raw.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Monotonicity / streak / persistence ----------------------------------


def f03ts_f03_trend_strength_metrics_uprun_20d_base_v043_signal(close):
    """Longest consecutive up-day run length in last 20 bars."""
    n = 20
    diff = close.diff()
    def _longest_up(x):
        if np.any(np.isnan(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return diff.rolling(n, min_periods=n).apply(_longest_up, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dnrun_60d_base_v044_signal(closeadj):
    """Longest consecutive down-day run length in last 60 bars."""
    n = 60
    diff = closeadj.diff()
    def _longest_dn(x):
        if np.any(np.isnan(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v < 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return diff.rolling(n, min_periods=n).apply(_longest_dn, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_signfrac_40d_base_v045_signal(closeadj):
    """Fraction of last 40 bars where sign(close.diff) == sign of cumulative move."""
    n = 40
    diff = closeadj.diff()
    cum = closeadj - closeadj.shift(n)
    sgn_d = np.sign(diff)
    sgn_c = np.sign(cum)
    flag = (sgn_d == sgn_c).astype(float).where(~sgn_d.isna() & ~sgn_c.isna())
    return flag.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_upfrac_15d_base_v046_signal(close):
    """Fraction of up days in last 15 — short-term persistence."""
    n = 15
    flag = (close.diff() > 0).astype(float).where(~close.diff().isna())
    return flag.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dirpersist_50d_base_v047_signal(closeadj):
    """Persistence: |sum(sign(diff))| / N over N=50 (rectified)."""
    n = 50
    sgn = np.sign(closeadj.diff())
    return (sgn.rolling(n, min_periods=n).sum().abs() / n).replace([np.inf, -np.inf], np.nan)


# --- Smoothed-DM family using non-Wilder smoothers ------------------------


def f03ts_f03_trend_strength_metrics_smaplusdm_20d_base_v048_signal(high, low):
    """SMA(+DM, 20) / SMA(TR, 20) approximation — uses simple smoothing instead of Wilder."""
    n = 20
    tr_proxy = (high - low).rolling(n, min_periods=n).mean()
    pdm = _plus_dm(high, low).rolling(n, min_periods=n).mean()
    return (pdm / tr_proxy.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_smaminusdm_60d_base_v049_signal(high, low):
    """SMA(-DM, 60) / SMA(TR, 60) — simple smoothed bear DM."""
    n = 60
    tr_proxy = (high - low).rolling(n, min_periods=n).mean()
    mdm = _minus_dm(high, low).rolling(n, min_periods=n).mean()
    return (mdm / tr_proxy.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dmrank_120d_base_v050_signal(high, low):
    """120d pct-rank of (+DM - -DM) Wilder smoothed at N=14."""
    pdm = _wilder(_plus_dm(high, low), 14)
    mdm = _wilder(_minus_dm(high, low), 14)
    spread = pdm - mdm
    return spread.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Discrete trend states & counts ---------------------------------------


def f03ts_f03_trend_strength_metrics_adxregime_14d_base_v051_signal(high, low, close):
    """sign(ADX(14) - 25) — discrete strong-trend (1) vs weak-trend (-1) state."""
    n = 14
    tr = _tr(high, low, close)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    return np.sign(adx - 25.0).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_adxhigh_50d_base_v052_signal(high, low, closeadj):
    """Count in last 50 days where ADX(14) > 30 — extended strong-trend regime."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    flag = (adx > 30.0).astype(float).where(~adx.isna())
    return flag.rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_bullbearcnt_30d_base_v053_signal(closeadj):
    """sum of sign(close - close.shift(20)) * sign(diff) over last 30 — counts
    bars where local daily-move sign agrees with 20d trend direction.
    Discrete persistence metric, structurally different from raw KER."""
    direction = np.sign(closeadj - closeadj.shift(20))
    daily = np.sign(closeadj.diff())
    agree = (direction * daily)
    return agree.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonstrong_50d_base_v054_signal(closeadj):
    """Count in 50 bars where (Aroon_up > 70) - count where (Aroon_down > 70). N=25 aroon window."""
    n = 25
    au = _aroon_up(closeadj, n)
    ad = _aroon_dn(closeadj, n)
    bullish = (au > 70.0).astype(float)
    bearish = (ad > 70.0).astype(float)
    return (bullish - bearish).rolling(50, min_periods=50).sum().replace([np.inf, -np.inf], np.nan)


# --- Cross-window trend-strength differentials ----------------------------


def f03ts_f03_trend_strength_metrics_adxdiff_30d_base_v055_signal(high, low, closeadj):
    """sign(ADX(14) - ADX(60)). Discrete bull/bear-of-trend-strength regime —
    captures whether short-horizon trend strength is leading or lagging."""
    def _adx(n):
        tr = _tr(high, low, closeadj)
        atr = _wilder(tr, n)
        pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
        mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
        dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
        return _wilder(dx, n)
    return np.sign(_adx(14) - _adx(60)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kerdiff_30d_base_v056_signal(closeadj):
    """KER(20) - KER(60). Trend-efficiency leading vs lagging."""
    def _ker(n):
        d = (closeadj - closeadj.shift(n)).abs()
        v = closeadj.diff().abs().rolling(n, min_periods=n).sum()
        return d / v.replace(0.0, np.nan)
    return (_ker(20) - _ker(60)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tsidiff_30d_base_v057_signal(closeadj):
    """TSI(25,13) - TSI(50,25). Momentum-acceleration via TSI."""
    def _tsi(r, s):
        d = closeadj.diff()
        n = d.ewm(span=r, adjust=False, min_periods=r).mean().ewm(span=s, adjust=False, min_periods=s).mean()
        dn = d.abs().ewm(span=r, adjust=False, min_periods=r).mean().ewm(span=s, adjust=False, min_periods=s).mean()
        return 100.0 * n / dn.replace(0.0, np.nan)
    return (_tsi(25, 13) - _tsi(50, 25)).replace([np.inf, -np.inf], np.nan)


# --- Bounded transforms of trend-strength measures ------------------------


def f03ts_f03_trend_strength_metrics_tanhker_30d_base_v058_signal(closeadj):
    """Number of MAs (out of 4 spans) whose sign(diff) agrees with a 60d signed
    trend direction. Discrete agreement count in [0,4]."""
    dir60 = np.sign(closeadj - closeadj.shift(60))
    s5 = np.sign(closeadj.rolling(5, min_periods=5).mean().diff(5))
    s20 = np.sign(closeadj.rolling(20, min_periods=20).mean().diff(5))
    s50 = np.sign(closeadj.rolling(50, min_periods=50).mean().diff(10))
    s100 = np.sign(closeadj.rolling(100, min_periods=100).mean().diff(21))
    agree = ((s5 == dir60).astype(float) + (s20 == dir60).astype(float)
             + (s50 == dir60).astype(float) + (s100 == dir60).astype(float))
    mask = dir60.isna() | s5.isna() | s20.isna() | s50.isna() | s100.isna()
    return agree.where(~mask).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_arctanmk_40d_base_v059_signal(closeadj):
    """arctan(MK-statistic scaled). Bounded transform of Mann-Kendall."""
    n = 40
    norm = n * (n - 1) / 2.0
    def _mk(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    raw = closeadj.rolling(n, min_periods=n).apply(_mk, raw=True)
    return (np.arctan(3.0 * raw) / (np.pi / 2.0)).replace([np.inf, -np.inf], np.nan)


# --- Slope / DMI curvature ------------------------------------------------


def f03ts_f03_trend_strength_metrics_adxslope_30d_base_v060_signal(high, low, closeadj):
    """ADX(14) 5-bar slope at end of rolling 30d. Momentum of trend strength."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    return adx.diff(5).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_adxcurv_40d_base_v061_signal(high, low, closeadj):
    """ADX(14) discrete curvature: ADX - 2*ADX.shift(10) + ADX.shift(20)."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    return (adx - 2.0 * adx.shift(10) + adx.shift(20)).replace([np.inf, -np.inf], np.nan)


# --- Other trend-strength shape metrics ----------------------------------


def f03ts_f03_trend_strength_metrics_corrtrend_25d_base_v062_signal(close):
    """Spearman-style rank corr between close and time at N=25 — robust trend strength."""
    n = 25
    def _rc(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        rx = pd.Series(x).rank().to_numpy()
        rt = np.arange(1, n + 1, dtype=float)
        return float(np.corrcoef(rx, rt)[0, 1])
    return close.rolling(n, min_periods=n).apply(_rc, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_corrtrend_120d_base_v063_signal(closeadj):
    """|Spearman rank-corr between |close.diff| and time, N=80| — measures
    whether absolute return-magnitude is rising or falling over horizon,
    a volatility-trend strength proxy (distinct from price-direction trend)."""
    n = 80
    absdiff = closeadj.diff().abs()
    def _rc(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        rx = pd.Series(x).rank().to_numpy()
        rt = np.arange(1, n + 1, dtype=float)
        c = np.corrcoef(rx, rt)
        return float(abs(c[0, 1]))
    return absdiff.rolling(n, min_periods=n).apply(_rc, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_signdiff_30d_base_v064_signal(closeadj):
    """Net sign sum: sum(sign(diff)) over N=30 / N. Bounded in [-1, 1]."""
    n = 30
    return (np.sign(closeadj.diff()).rolling(n, min_periods=n).sum() / n).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_signagree_25d_base_v065_signal(close):
    """Mean over 25 bars of sign(diff(close)) * sign(diff(close.shift(1)))
    — autocorrelation-of-sign trend persistence."""
    n = 25
    sgn = np.sign(close.diff())
    prod = sgn * sgn.shift(1)
    return prod.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_acfr1_60d_base_v066_signal(closeadj):
    """Lag-1 autocorrelation of log-returns at N=60.  >0 trending,  <0 mean-reverting."""
    n = 60
    r = np.log(closeadj).diff()
    def _ac(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() <= 0 or b.std() <= 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return r.rolling(n, min_periods=n).apply(_ac, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dmi_xover_30d_base_v067_signal(high, low, closeadj):
    """Count of +DI / -DI crossovers in last 30 — frequent = choppy, rare = strong trend (negated)."""
    n = 30
    pdi = 100.0 * _wilder(_plus_dm(high, low), 14) / _wilder(_tr(high, low, closeadj), 14).replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), 14) / _wilder(_tr(high, low, closeadj), 14).replace(0.0, np.nan)
    s = np.sign(pdi - mdi)
    xover = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return (-xover.rolling(n, min_periods=n).sum()).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tdays_dmihigh_60d_base_v068_signal(high, low, closeadj):
    """Days since the last |+DI - -DI| > 30, capped at 60."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    cond = ((pdi - mdi).abs() > 30.0).astype(float).where(~pdi.isna() & ~mdi.isna())
    def _dsince(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 60.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(60, min_periods=60).apply(_dsince, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tslowstr_30d_base_v069_signal(high, low, closeadj):
    """Trend-strength fraction: bars in last 30 where ADX(14) is in lowest tertile of trailing 120d."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    q33 = adx.rolling(120, min_periods=120).quantile(0.33)
    flag = (adx < q33).astype(float).where(~adx.isna() & ~q33.isna())
    return flag.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_chopslope_30d_base_v070_signal(high, low, closeadj):
    """10-bar diff of negative Choppiness(14). Rate-of-change of trendiness."""
    n = 14
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    chop = -100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return chop.diff(10).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonslope_30d_base_v071_signal(closeadj):
    """5-bar slope of Aroon oscillator at N=25."""
    n = 25
    au = _aroon_up(closeadj, n)
    ad = _aroon_dn(closeadj, n)
    osc = au - ad
    return osc.diff(5).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_vortexslope_30d_base_v072_signal(high, low, closeadj):
    """10-bar slope of |VI+ - VI-| at N=21."""
    n = 21
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    vp = (high - low.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    vm = (low - high.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    return (vp - vm).abs().diff(10).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_persistz_60d_base_v073_signal(closeadj):
    """Z-score of |sum(sign(diff))| over its rolling stddev. Persistence anomaly."""
    n = 60
    sgn = np.sign(closeadj.diff())
    s = sgn.rolling(n, min_periods=n).sum().abs()
    mu = s.rolling(120, min_periods=120).mean()
    sd = s.rolling(120, min_periods=120).std(ddof=1)
    return ((s - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_efrhl_50d_base_v074_signal(high, low):
    """OHLC efficiency on (high+low)/2 at N=50."""
    n = 50
    mid = 0.5 * (high + low)
    direction = mid - mid.shift(n)
    volatility = mid.diff().abs().rolling(n, min_periods=n).sum()
    return (direction / volatility.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_efrkam_15d_base_v075_signal(close):
    """Squared efficiency ratio at N=15 (Kaufman's smoothing-constant input)."""
    n = 15
    direction = (close - close.shift(n)).abs()
    volatility = close.diff().abs().rolling(n, min_periods=n).sum()
    er = direction / volatility.replace(0.0, np.nan)
    return (er ** 2).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f03_trend_strength_metrics_base_001_075_REGISTRY = {
    "f03ts_f03_trend_strength_metrics_adx_14d_base_v001_signal": {"inputs": ["high", "low", "close"], "func": f03ts_f03_trend_strength_metrics_adx_14d_base_v001_signal},
    "f03ts_f03_trend_strength_metrics_adx_50d_base_v002_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_adx_50d_base_v002_signal},
    "f03ts_f03_trend_strength_metrics_dmidiff_21d_base_v003_signal": {"inputs": ["high", "low", "close"], "func": f03ts_f03_trend_strength_metrics_dmidiff_21d_base_v003_signal},
    "f03ts_f03_trend_strength_metrics_dmiratio_30d_base_v004_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_dmiratio_30d_base_v004_signal},
    "f03ts_f03_trend_strength_metrics_adxstrong_60d_base_v005_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_adxstrong_60d_base_v005_signal},
    "f03ts_f03_trend_strength_metrics_pdi_14d_base_v006_signal": {"inputs": ["high", "low", "close"], "func": f03ts_f03_trend_strength_metrics_pdi_14d_base_v006_signal},
    "f03ts_f03_trend_strength_metrics_mdi_40d_base_v007_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_mdi_40d_base_v007_signal},
    "f03ts_f03_trend_strength_metrics_aroonosc_14d_base_v008_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_aroonosc_14d_base_v008_signal},
    "f03ts_f03_trend_strength_metrics_aroonosc_50d_base_v009_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_aroonosc_50d_base_v009_signal},
    "f03ts_f03_trend_strength_metrics_aroondiff_25d_base_v010_signal": {"inputs": ["high", "low"], "func": f03ts_f03_trend_strength_metrics_aroondiff_25d_base_v010_signal},
    "f03ts_f03_trend_strength_metrics_aroonsign_30d_base_v011_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_aroonsign_30d_base_v011_signal},
    "f03ts_f03_trend_strength_metrics_aroonconv_21d_base_v012_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_aroonconv_21d_base_v012_signal},
    "f03ts_f03_trend_strength_metrics_vortexdiff_14d_base_v013_signal": {"inputs": ["high", "low", "close"], "func": f03ts_f03_trend_strength_metrics_vortexdiff_14d_base_v013_signal},
    "f03ts_f03_trend_strength_metrics_vortexabs_30d_base_v014_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_vortexabs_30d_base_v014_signal},
    "f03ts_f03_trend_strength_metrics_vortexratio_60d_base_v015_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_vortexratio_60d_base_v015_signal},
    "f03ts_f03_trend_strength_metrics_chop_14d_base_v016_signal": {"inputs": ["high", "low", "close"], "func": f03ts_f03_trend_strength_metrics_chop_14d_base_v016_signal},
    "f03ts_f03_trend_strength_metrics_chop_40d_base_v017_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_chop_40d_base_v017_signal},
    "f03ts_f03_trend_strength_metrics_choprank_120d_base_v018_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_choprank_120d_base_v018_signal},
    "f03ts_f03_trend_strength_metrics_tsi_25_13_base_v019_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_tsi_25_13_base_v019_signal},
    "f03ts_f03_trend_strength_metrics_tsi_50_25_base_v020_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_tsi_50_25_base_v020_signal},
    "f03ts_f03_trend_strength_metrics_tsiabs_25_13_base_v021_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_tsiabs_25_13_base_v021_signal},
    "f03ts_f03_trend_strength_metrics_kst_30d_base_v022_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_kst_30d_base_v022_signal},
    "f03ts_f03_trend_strength_metrics_kstlong_120d_base_v023_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_kstlong_120d_base_v023_signal},
    "f03ts_f03_trend_strength_metrics_kefr_10d_base_v024_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_kefr_10d_base_v024_signal},
    "f03ts_f03_trend_strength_metrics_kefr_40d_base_v025_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_kefr_40d_base_v025_signal},
    "f03ts_f03_trend_strength_metrics_kefr_120d_base_v026_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_kefr_120d_base_v026_signal},
    "f03ts_f03_trend_strength_metrics_kefrsigned_30d_base_v027_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_kefrsigned_30d_base_v027_signal},
    "f03ts_f03_trend_strength_metrics_kefrhl_25d_base_v028_signal": {"inputs": ["high", "low"], "func": f03ts_f03_trend_strength_metrics_kefrhl_25d_base_v028_signal},
    "f03ts_f03_trend_strength_metrics_r2lin_20d_base_v029_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_r2lin_20d_base_v029_signal},
    "f03ts_f03_trend_strength_metrics_r2lin_63d_base_v030_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_r2lin_63d_base_v030_signal},
    "f03ts_f03_trend_strength_metrics_r2log_120d_base_v031_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_r2log_120d_base_v031_signal},
    "f03ts_f03_trend_strength_metrics_logregslp_60d_base_v032_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_logregslp_60d_base_v032_signal},
    "f03ts_f03_trend_strength_metrics_regrres_30d_base_v033_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_regrres_30d_base_v033_signal},
    "f03ts_f03_trend_strength_metrics_robtrend_40d_base_v034_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_robtrend_40d_base_v034_signal},
    "f03ts_f03_trend_strength_metrics_poly2coef_50d_base_v035_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_poly2coef_50d_base_v035_signal},
    "f03ts_f03_trend_strength_metrics_lastresid_30d_base_v036_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_lastresid_30d_base_v036_signal},
    "f03ts_f03_trend_strength_metrics_hurstrs_80d_base_v037_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_hurstrs_80d_base_v037_signal},
    "f03ts_f03_trend_strength_metrics_hurstrs_160d_base_v038_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_hurstrs_160d_base_v038_signal},
    "f03ts_f03_trend_strength_metrics_varratio_30d_base_v039_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_varratio_30d_base_v039_signal},
    "f03ts_f03_trend_strength_metrics_varratio_100d_base_v040_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_varratio_100d_base_v040_signal},
    "f03ts_f03_trend_strength_metrics_mks_30d_base_v041_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_mks_30d_base_v041_signal},
    "f03ts_f03_trend_strength_metrics_mksabs_60d_base_v042_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_mksabs_60d_base_v042_signal},
    "f03ts_f03_trend_strength_metrics_uprun_20d_base_v043_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_uprun_20d_base_v043_signal},
    "f03ts_f03_trend_strength_metrics_dnrun_60d_base_v044_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_dnrun_60d_base_v044_signal},
    "f03ts_f03_trend_strength_metrics_signfrac_40d_base_v045_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_signfrac_40d_base_v045_signal},
    "f03ts_f03_trend_strength_metrics_upfrac_15d_base_v046_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_upfrac_15d_base_v046_signal},
    "f03ts_f03_trend_strength_metrics_dirpersist_50d_base_v047_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_dirpersist_50d_base_v047_signal},
    "f03ts_f03_trend_strength_metrics_smaplusdm_20d_base_v048_signal": {"inputs": ["high", "low"], "func": f03ts_f03_trend_strength_metrics_smaplusdm_20d_base_v048_signal},
    "f03ts_f03_trend_strength_metrics_smaminusdm_60d_base_v049_signal": {"inputs": ["high", "low"], "func": f03ts_f03_trend_strength_metrics_smaminusdm_60d_base_v049_signal},
    "f03ts_f03_trend_strength_metrics_dmrank_120d_base_v050_signal": {"inputs": ["high", "low"], "func": f03ts_f03_trend_strength_metrics_dmrank_120d_base_v050_signal},
    "f03ts_f03_trend_strength_metrics_adxregime_14d_base_v051_signal": {"inputs": ["high", "low", "close"], "func": f03ts_f03_trend_strength_metrics_adxregime_14d_base_v051_signal},
    "f03ts_f03_trend_strength_metrics_adxhigh_50d_base_v052_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_adxhigh_50d_base_v052_signal},
    "f03ts_f03_trend_strength_metrics_bullbearcnt_30d_base_v053_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_bullbearcnt_30d_base_v053_signal},
    "f03ts_f03_trend_strength_metrics_aroonstrong_50d_base_v054_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_aroonstrong_50d_base_v054_signal},
    "f03ts_f03_trend_strength_metrics_adxdiff_30d_base_v055_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_adxdiff_30d_base_v055_signal},
    "f03ts_f03_trend_strength_metrics_kerdiff_30d_base_v056_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_kerdiff_30d_base_v056_signal},
    "f03ts_f03_trend_strength_metrics_tsidiff_30d_base_v057_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_tsidiff_30d_base_v057_signal},
    "f03ts_f03_trend_strength_metrics_tanhker_30d_base_v058_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_tanhker_30d_base_v058_signal},
    "f03ts_f03_trend_strength_metrics_arctanmk_40d_base_v059_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_arctanmk_40d_base_v059_signal},
    "f03ts_f03_trend_strength_metrics_adxslope_30d_base_v060_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_adxslope_30d_base_v060_signal},
    "f03ts_f03_trend_strength_metrics_adxcurv_40d_base_v061_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_adxcurv_40d_base_v061_signal},
    "f03ts_f03_trend_strength_metrics_corrtrend_25d_base_v062_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_corrtrend_25d_base_v062_signal},
    "f03ts_f03_trend_strength_metrics_corrtrend_120d_base_v063_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_corrtrend_120d_base_v063_signal},
    "f03ts_f03_trend_strength_metrics_signdiff_30d_base_v064_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_signdiff_30d_base_v064_signal},
    "f03ts_f03_trend_strength_metrics_signagree_25d_base_v065_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_signagree_25d_base_v065_signal},
    "f03ts_f03_trend_strength_metrics_acfr1_60d_base_v066_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_acfr1_60d_base_v066_signal},
    "f03ts_f03_trend_strength_metrics_dmi_xover_30d_base_v067_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_dmi_xover_30d_base_v067_signal},
    "f03ts_f03_trend_strength_metrics_tdays_dmihigh_60d_base_v068_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_tdays_dmihigh_60d_base_v068_signal},
    "f03ts_f03_trend_strength_metrics_tslowstr_30d_base_v069_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_tslowstr_30d_base_v069_signal},
    "f03ts_f03_trend_strength_metrics_chopslope_30d_base_v070_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_chopslope_30d_base_v070_signal},
    "f03ts_f03_trend_strength_metrics_aroonslope_30d_base_v071_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_aroonslope_30d_base_v071_signal},
    "f03ts_f03_trend_strength_metrics_vortexslope_30d_base_v072_signal": {"inputs": ["high", "low", "closeadj"], "func": f03ts_f03_trend_strength_metrics_vortexslope_30d_base_v072_signal},
    "f03ts_f03_trend_strength_metrics_persistz_60d_base_v073_signal": {"inputs": ["closeadj"], "func": f03ts_f03_trend_strength_metrics_persistz_60d_base_v073_signal},
    "f03ts_f03_trend_strength_metrics_efrhl_50d_base_v074_signal": {"inputs": ["high", "low"], "func": f03ts_f03_trend_strength_metrics_efrhl_50d_base_v074_signal},
    "f03ts_f03_trend_strength_metrics_efrkam_15d_base_v075_signal": {"inputs": ["close"], "func": f03ts_f03_trend_strength_metrics_efrkam_15d_base_v075_signal},
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
    for name, entry in f03_trend_strength_metrics_base_001_075_REGISTRY.items():
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
