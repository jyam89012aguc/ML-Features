"""f03_trend_strength_metrics base features 076-150.

Companion to f03 base 001-075. Continues the trend-strength domain:
extended ADX/DMI variants, additional Aroon/Vortex/Choppiness slices,
log-regression slope/R^2 at varied windows, Hurst/variance-ratio
variants, more Mann-Kendall and ranked-correlation features, longer
streak / monotonicity counts, OHLC-based efficiency variants, and
multi-window agreement / dispersion features.

Each function fully inlines its formula. No fillna(0). Windows > 21d use
closeadj. NaN policy: replace([inf,-inf], nan) at the final return only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _tr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev_close = close.shift(1)
    a = (high - low).abs()
    b = (high - prev_close).abs()
    c = (low - prev_close).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _plus_dm(high: pd.Series, low: pd.Series) -> pd.Series:
    up = high.diff(); dn = -low.diff()
    return pd.Series(np.where((up > dn) & (up > 0.0), up, 0.0), index=high.index, dtype=float)


def _minus_dm(high: pd.Series, low: pd.Series) -> pd.Series:
    up = high.diff(); dn = -low.diff()
    return pd.Series(np.where((dn > up) & (dn > 0.0), dn, 0.0), index=high.index, dtype=float)


# --- Extended ADX/DMI family ---------------------------------------------


def f03ts_f03_trend_strength_metrics_adx_8d_base_v076_signal(high, low, close):
    """ADX(8) — very short Wilder ADX."""
    n = 8
    tr = _tr(high, low, close)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    return _wilder(dx, n).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_adxrank_120d_base_v077_signal(high, low, closeadj):
    """120d pct-rank of ADX(14). Bounded relative trend-strength."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    return adx.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_pdimrnk_60d_base_v078_signal(high, low, closeadj):
    """sign(+DI - -DI) Wilder N=21. Discrete bull/bear directional state."""
    n = 21
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    return np.sign(pdi - mdi).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dxraw_14d_base_v079_signal(high, low, close):
    """Raw DX(14) before Wilder smoothing — unsmoothed strength oscillator."""
    n = 14
    tr = _tr(high, low, close)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    return (100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_adxz_60d_base_v080_signal(high, low, closeadj):
    """Z-score of ADX(14) over trailing 60d window."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    mu = adx.rolling(60, min_periods=60).mean()
    sd = adx.rolling(60, min_periods=60).std(ddof=1)
    return ((adx - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Aroon extensions ----------------------------------------------------


def f03ts_f03_trend_strength_metrics_aroonup_18d_base_v081_signal(close):
    """Aroon-up at N=18 standalone (close)."""
    n = 18
    return close.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmax(x)))) / n, raw=True
    ).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroondn_40d_base_v082_signal(closeadj):
    """Aroon-down at N=40 standalone (closeadj)."""
    n = 40
    return closeadj.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmin(x)))) / n, raw=True
    ).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonlog_25d_base_v083_signal(closeadj):
    """log((Aroon-up + 1) / (Aroon-down + 1)) at N=25 — bounded log ratio."""
    n = 25
    au = closeadj.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmax(x)))) / n, raw=True
    )
    ad = closeadj.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmin(x)))) / n, raw=True
    )
    return np.log((au + 1.0) / (ad + 1.0)).replace([np.inf, -np.inf], np.nan)


# --- Vortex extensions ---------------------------------------------------


def f03ts_f03_trend_strength_metrics_viplus_21d_base_v084_signal(high, low, close):
    """VI+ standalone at N=21."""
    n = 21
    tr_n = _tr(high, low, close).rolling(n, min_periods=n).sum()
    return ((high - low.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_viminus_40d_base_v085_signal(high, low, closeadj):
    """VI- standalone at N=40."""
    n = 40
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    return ((low - high.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_visum_50d_base_v086_signal(high, low, closeadj):
    """VI+ + VI- at N=50 — total directional movement (range / tr)."""
    n = 50
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    vp = (high - low.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    vm = (low - high.shift(1)).abs().rolling(n, min_periods=n).sum() / tr_n.replace(0.0, np.nan)
    return (vp + vm).replace([np.inf, -np.inf], np.nan)


# --- Choppiness extensions -----------------------------------------------


def f03ts_f03_trend_strength_metrics_chop_28d_base_v087_signal(high, low, closeadj):
    """-Choppiness(28). Mid-horizon trend-vs-chop signal."""
    n = 28
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return (-chop).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_chopdiff_30d_base_v088_signal(high, low, closeadj):
    """Choppiness(14) - Choppiness(56). Short vs long chop differential."""
    def _chop(n):
        tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
        hh = high.rolling(n, min_periods=n).max()
        ll = low.rolling(n, min_periods=n).min()
        return 100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return (_chop(14) - _chop(56)).replace([np.inf, -np.inf], np.nan)


# --- TSI extensions ------------------------------------------------------


def f03ts_f03_trend_strength_metrics_tsi_13_7_base_v089_signal(close):
    """TSI(r=13, s=7) on close — fast variant."""
    diff = close.diff()
    num = diff.ewm(span=13, adjust=False, min_periods=13).mean().ewm(span=7, adjust=False, min_periods=7).mean()
    den = diff.abs().ewm(span=13, adjust=False, min_periods=13).mean().ewm(span=7, adjust=False, min_periods=7).mean()
    return (100.0 * num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tsihigh_25_13_base_v090_signal(high):
    """TSI(25,13) computed on HIGH series — uses OHLC."""
    diff = high.diff()
    num = diff.ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    den = diff.abs().ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    return (100.0 * num / den.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Kaufman efficiency extensions ---------------------------------------


def f03ts_f03_trend_strength_metrics_kefr_5d_base_v091_signal(close):
    """KER N=5 — very short efficiency ratio."""
    n = 5
    d = (close - close.shift(n)).abs()
    v = close.diff().abs().rolling(n, min_periods=n).sum()
    return (d / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)




def f03ts_f03_trend_strength_metrics_kerhi_50d_base_v093_signal(high):
    """KER N=50 on HIGH series — OHLC variant."""
    n = 50
    d = (high - high.shift(n)).abs()
    v = high.diff().abs().rolling(n, min_periods=n).sum()
    return (d / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kerlo_50d_base_v094_signal(high, low):
    """KER on HIGH minus KER on LOW at N=50. Asymmetric OHLC efficiency — captures
    differential trend strength of upside vs downside extremes."""
    n = 50
    dh = (high - high.shift(n)).abs()
    vh = high.diff().abs().rolling(n, min_periods=n).sum()
    erh = dh / vh.replace(0.0, np.nan)
    dl = (low - low.shift(n)).abs()
    vl = low.diff().abs().rolling(n, min_periods=n).sum()
    erl = dl / vl.replace(0.0, np.nan)
    return (erh - erl).replace([np.inf, -np.inf], np.nan)


# --- R^2 / regression extensions -----------------------------------------


def f03ts_f03_trend_strength_metrics_r2lin_40d_base_v095_signal(closeadj):
    """R^2 OLS(close, t) at N=40."""
    n = 40
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


def f03ts_f03_trend_strength_metrics_logregslp_30d_base_v096_signal(closeadj):
    """OLS slope of log(close) ~ t at N=30 (short-horizon rate)."""
    n = 30
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0):
            return np.nan
        y = np.log(x)
        t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    return closeadj.rolling(n, min_periods=n).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_logregslp_180d_base_v097_signal(closeadj):
    """OLS slope of log(close) ~ t at N=180 (annual)."""
    n = 180
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0):
            return np.nan
        y = np.log(x)
        t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    return closeadj.rolling(n, min_periods=n).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_regresid_60d_base_v098_signal(closeadj):
    """Residual std normalized by close (CV of residual). Small = clean trend."""
    n = 60
    def _cvres(x):
        if np.any(~np.isfinite(x)) or x.mean() == 0:
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        resid = x - (a[0] * t + a[1])
        return float(np.std(resid, ddof=1) / abs(x.mean()))
    return closeadj.rolling(n, min_periods=n).apply(_cvres, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_regrsnr_50d_base_v099_signal(closeadj):
    """SNR: slope * N / residual_std at N=50 — Lo-MacKinlay-style trend SNR."""
    n = 50
    def _snr(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float)
        a = np.polyfit(t, x, 1)
        resid = x - (a[0] * t + a[1])
        s = float(np.std(resid, ddof=1))
        if s <= 0:
            return np.nan
        return float(a[0]) * n / s
    return closeadj.rolling(n, min_periods=n).apply(_snr, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_polylin_40d_base_v100_signal(closeadj):
    """Linear coefficient from a degree-2 polyfit — short-term momentum after
    removing quadratic curvature."""
    n = 40
    def _lin(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float) / n
        a = np.polyfit(t, x, 2)
        return float(a[1])
    return closeadj.rolling(n, min_periods=n).apply(_lin, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_polyquad_120d_base_v101_signal(closeadj):
    """Long-horizon quadratic coefficient at N=120 — captures regime curvature."""
    n = 120
    def _quad(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        t = np.arange(n, dtype=float) / n
        a = np.polyfit(t, x, 2)
        return float(a[0])
    return closeadj.rolling(n, min_periods=n).apply(_quad, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Hurst & variance-ratio extensions -----------------------------------


def f03ts_f03_trend_strength_metrics_hurstrs_60d_base_v102_signal(closeadj):
    """Hurst R/S exponent at N=60 (shorter horizon than v037)."""
    n = 60
    def _hurst(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        r = np.diff(np.log(x))
        if r.size < 8:
            return np.nan
        y = r - r.mean()
        z = np.cumsum(y)
        R = z.max() - z.min()
        S = r.std(ddof=1)
        if S <= 0 or R <= 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(r)))
    return closeadj.rolling(n, min_periods=n).apply(_hurst, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_varratio_q20_120d_base_v103_signal(closeadj):
    """Variance ratio q=20, N=120 — long-horizon variance-ratio."""
    n = 120
    q = 20
    r1 = np.log(closeadj).diff()
    rq = np.log(closeadj).diff(q)
    v1 = r1.rolling(n, min_periods=n).var(ddof=1)
    vq = rq.rolling(n, min_periods=n).var(ddof=1)
    return (vq / (q * v1.replace(0.0, np.nan)) - 1.0).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_hurstdiff_120d_base_v104_signal(closeadj):
    """Hurst(60) - Hurst(120) — trend-persistence change with horizon."""
    def _hurst(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        r = np.diff(np.log(x))
        if r.size < 8:
            return np.nan
        y = r - r.mean()
        z = np.cumsum(y)
        R = z.max() - z.min()
        S = r.std(ddof=1)
        if S <= 0 or R <= 0:
            return np.nan
        return float(np.log(R / S) / np.log(len(r)))
    h60 = closeadj.rolling(60, min_periods=60).apply(_hurst, raw=True)
    h120 = closeadj.rolling(120, min_periods=120).apply(_hurst, raw=True)
    return (h60 - h120).replace([np.inf, -np.inf], np.nan)


# --- Mann-Kendall extensions ---------------------------------------------


def f03ts_f03_trend_strength_metrics_mk_15d_base_v105_signal(close):
    """Mann-Kendall S/max at N=15 — short-horizon monotone-trend strength."""
    n = 15
    norm = n * (n - 1) / 2.0
    def _mk(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    return close.rolling(n, min_periods=n).apply(_mk, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_mk_90d_base_v106_signal(closeadj):
    """Mann-Kendall S at N=90 (long monotone trend)."""
    n = 90
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


# --- Persistence / streak extensions -------------------------------------


def f03ts_f03_trend_strength_metrics_anymonotone_30d_base_v107_signal(closeadj):
    """Length of longest strict monotone (any direction) run within 30d window."""
    n = 30
    def _longest(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        d = np.sign(np.diff(x))
        best = 1; cur = 1
        for i in range(1, len(d)):
            if d[i] == d[i - 1] and d[i] != 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 1
        return float(best)
    return closeadj.rolling(n, min_periods=n).apply(_longest, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_uprunlong_120d_base_v108_signal(closeadj):
    """Longest up-streak within 120 bars."""
    n = 120
    def _up(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        d = np.sign(np.diff(x))
        best = 0; cur = 0
        for v in d:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return closeadj.rolling(n, min_periods=n).apply(_up, raw=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_dirsignmean_8d_base_v109_signal(close):
    """Mean of sign(diff) over N=8 — very short directional bias."""
    n = 8
    return (np.sign(close.diff()).rolling(n, min_periods=n).mean()).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_acclbal_45d_base_v110_signal(closeadj):
    """Net up minus down bars at N=45 (sum of sign(diff))."""
    n = 45
    return (np.sign(closeadj.diff()).rolling(n, min_periods=n).sum()).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_sameside_60d_base_v111_signal(closeadj):
    """Max consecutive bars on same side of SMA(20) at N=60."""
    s = closeadj.rolling(20, min_periods=20).mean()
    rel = np.sign(closeadj - s)
    n = 60
    def _longest_same(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        best = 0; cur = 0; prev = 0
        for v in x:
            if v == prev and v != 0:
                cur += 1
            else:
                cur = 1
            if cur > best:
                best = cur
            prev = v
        return float(best)
    return rel.rolling(n, min_periods=n).apply(_longest_same, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Cross-window trend agreement features ------------------------------


def f03ts_f03_trend_strength_metrics_efrmulti_30d_base_v112_signal(closeadj):
    """sum of sign(KER_signed) over multiple windows (10,20,40,80,160)."""
    def _ksg(n):
        return np.sign((closeadj - closeadj.shift(n)) / (closeadj.diff().abs().rolling(n, min_periods=n).sum().replace(0.0, np.nan)))
    return (_ksg(10) + _ksg(20) + _ksg(40) + _ksg(80) + _ksg(160)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_efragree_30d_base_v113_signal(closeadj):
    """Mean of sign agreement: pairwise sign(ROC(20)) == sign(ROC(60))? — count."""
    s20 = np.sign(closeadj - closeadj.shift(20))
    s60 = np.sign(closeadj - closeadj.shift(60))
    s120 = np.sign(closeadj - closeadj.shift(120))
    agreement = ((s20 == s60).astype(float) + (s20 == s120).astype(float) + (s60 == s120).astype(float))
    mask = s20.isna() | s60.isna() | s120.isna()
    return agreement.where(~mask).replace([np.inf, -np.inf], np.nan)


# --- Bounded transforms --------------------------------------------------


def f03ts_f03_trend_strength_metrics_sigmoidker_25d_base_v114_signal(closeadj):
    """sigmoid(5 * signed-KER(25)) — bounded smooth squash."""
    n = 25
    raw = closeadj - closeadj.shift(n)
    v = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    er = raw / v.replace(0.0, np.nan)
    return (1.0 / (1.0 + np.exp(-5.0 * er))).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_arctsi_30d_base_v115_signal(closeadj):
    """Discrete count: bars in last 60 where |TSI(13,7)| > 25 — fraction-of-strong-momentum
    state. Different shape from raw TSI by thresholding+counting."""
    diff = closeadj.diff()
    num = diff.ewm(span=13, adjust=False, min_periods=13).mean().ewm(span=7, adjust=False, min_periods=7).mean()
    den = diff.abs().ewm(span=13, adjust=False, min_periods=13).mean().ewm(span=7, adjust=False, min_periods=7).mean()
    tsi = 100.0 * num / den.replace(0.0, np.nan)
    flag = (tsi.abs() > 25.0).astype(float).where(~tsi.isna())
    return flag.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# --- Trend strength via dispersion ---------------------------------------


def f03ts_f03_trend_strength_metrics_pricedispr_40d_base_v116_signal(closeadj):
    """std(log(close).diff()) / |mean(log(close).diff())|, N=40. Inverse SNR
    (low = strong trend)."""
    n = 40
    r = np.log(closeadj).diff()
    mu = r.rolling(n, min_periods=n).mean()
    sd = r.rolling(n, min_periods=n).std(ddof=1)
    return (sd / mu.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_pricesnr_60d_base_v117_signal(closeadj):
    """SNR: |mean(r)| * sqrt(N) / std(r) at N=60 — t-statistic of drift."""
    n = 60
    r = np.log(closeadj).diff()
    mu = r.rolling(n, min_periods=n).mean()
    sd = r.rolling(n, min_periods=n).std(ddof=1)
    return (mu.abs() * np.sqrt(n) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_rangertr_50d_base_v118_signal(high, low, closeadj):
    """(highest_high - lowest_low) / sum(TR) at N=50 — efficiency on TR."""
    n = 50
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    tr_sum = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    return ((hh - ll) / tr_sum.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- OHLC / candle trend-strength features -------------------------------


def f03ts_f03_trend_strength_metrics_bullbarpct_40d_base_v119_signal(close, open_):
    """Fraction of bull bars (close>open) in last 40 — trend-direction count."""
    flag = (close > open_).astype(float).where(~close.isna() & ~open_.isna())
    return flag.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_directnbody_30d_base_v120_signal(close, open_):
    """sum((close-open)) over 30 days normalized by sum|close-open|."""
    body = close - open_
    s = body.rolling(30, min_periods=30).sum()
    a = body.abs().rolling(30, min_periods=30).sum()
    return (s / a.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_hhseq_30d_base_v121_signal(high):
    """Count of bars in last 30 where high > rolling 5d high.shift(1) — higher-high streak count."""
    cond = (high > high.shift(1).rolling(5, min_periods=5).max()).astype(float).where(~high.isna())
    return cond.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_llseq_60d_base_v122_signal(low):
    """Count of bars in last 60 where low < rolling 10d low.shift(1) — lower-low count."""
    cond = (low < low.shift(1).rolling(10, min_periods=10).min()).astype(float).where(~low.isna())
    return cond.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)




def f03ts_f03_trend_strength_metrics_atrtrendlong_120d_base_v124_signal(high, low, closeadj):
    """Long-horizon ATR-normalized momentum at N=120."""
    n = 120
    move = closeadj - closeadj.shift(n)
    tr_sum = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    return (move / tr_sum.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Time-since-event features -------------------------------------------




def f03ts_f03_trend_strength_metrics_daysadxhi_120d_base_v126_signal(high, low, closeadj):
    """Days since ADX(14) last exceeded 40, capped at 120."""
    n = 14
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, n)
    pdi = 100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0, np.nan)
    mdi = 100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0, np.nan)
    dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0, np.nan)
    adx = _wilder(dx, n)
    cond = (adx > 40.0).astype(float).where(~adx.isna())
    def _dsince(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 120.0
        return float(len(x) - 1 - idx[-1])
    return cond.rolling(120, min_periods=120).apply(_dsince, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Choppiness slope / curvature ----------------------------------------


def f03ts_f03_trend_strength_metrics_chopcurv_40d_base_v127_signal(high, low, closeadj):
    """Discrete curvature of -Choppiness(20): -chop - 2*lag10 + lag20."""
    n = 20
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    nchop = -100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    return (nchop - 2.0 * nchop.shift(10) + nchop.shift(20)).replace([np.inf, -np.inf], np.nan)


# --- Rank / percentile features ------------------------------------------


def f03ts_f03_trend_strength_metrics_kerrank_100d_base_v128_signal(closeadj):
    """100d pct-rank of KER(30) — bounded relative efficiency."""
    n = 30
    d = (closeadj - closeadj.shift(n)).abs()
    v = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    er = d / v.replace(0.0, np.nan)
    return er.rolling(100, min_periods=100).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_tsi_rank_120d_base_v129_signal(closeadj):
    """120d pct-rank of TSI(25,13). Rank-of-momentum strength."""
    diff = closeadj.diff()
    num = diff.ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    den = diff.abs().ewm(span=25, adjust=False, min_periods=25).mean().ewm(span=13, adjust=False, min_periods=13).mean()
    tsi = 100.0 * num / den.replace(0.0, np.nan)
    return tsi.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_aroonrank_120d_base_v130_signal(closeadj):
    """120d pct-rank of Aroon oscillator(25)."""
    n = 25
    au = closeadj.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmax(x)))) / n, raw=True
    )
    ad = closeadj.rolling(n + 1, min_periods=n + 1).apply(
        lambda x: 100.0 * (n - (n - int(np.argmin(x)))) / n, raw=True
    )
    osc = au - ad
    return osc.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# --- Position vs extremes (trend-strength related) ----------------------


def f03ts_f03_trend_strength_metrics_distargmax_30d_base_v131_signal(closeadj):
    """Bars since rolling 30d highest close — small = strong upward trend, large = stale top."""
    n = 30
    return closeadj.rolling(n, min_periods=n).apply(
        lambda x: float(len(x) - 1 - int(np.argmax(x))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_distargmin_60d_base_v132_signal(closeadj):
    """Bars since rolling 60d lowest close — small = strong downward trend."""
    n = 60
    return closeadj.rolling(n, min_periods=n).apply(
        lambda x: float(len(x) - 1 - int(np.argmin(x))), raw=True
    ).replace([np.inf, -np.inf], np.nan)


# --- KST extensions ------------------------------------------------------


def f03ts_f03_trend_strength_metrics_kstsig_30d_base_v133_signal(closeadj):
    """KST minus its 9-bar SMA signal line — trend strength change."""
    r1 = closeadj.pct_change(10).rolling(10, min_periods=10).mean()
    r2 = closeadj.pct_change(15).rolling(10, min_periods=10).mean()
    r3 = closeadj.pct_change(20).rolling(10, min_periods=10).mean()
    r4 = closeadj.pct_change(30).rolling(15, min_periods=15).mean()
    kst = 1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    sig = kst.rolling(9, min_periods=9).mean()
    return (kst - sig).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_kstsign_30d_base_v134_signal(closeadj):
    """sign(KST) discrete bull/bear state."""
    r1 = closeadj.pct_change(10).rolling(10, min_periods=10).mean()
    r2 = closeadj.pct_change(15).rolling(10, min_periods=10).mean()
    r3 = closeadj.pct_change(20).rolling(10, min_periods=10).mean()
    r4 = closeadj.pct_change(30).rolling(15, min_periods=15).mean()
    kst = 1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    return np.sign(kst).replace([np.inf, -np.inf], np.nan)


# --- Stochastic / windowed ---------------------------------------------


def f03ts_f03_trend_strength_metrics_stochmom_30d_base_v135_signal(closeadj):
    """(close - LL30) / (HH30 - LL30) on log(close) at N=30 — channel position
    on closeadj; trend-strength-related as it measures position within range."""
    n = 30
    y = np.log(closeadj)
    hh = y.rolling(n, min_periods=n).max()
    ll = y.rolling(n, min_periods=n).min()
    return ((y - ll) / (hh - ll).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Trend slope of ATR (volatility of trend) ---------------------------


def f03ts_f03_trend_strength_metrics_atrdrift_50d_base_v136_signal(high, low, closeadj):
    """OLS slope of log(ATR(14)) on time at N=50. Trending volatility."""
    tr = _tr(high, low, closeadj)
    atr = _wilder(tr, 14)
    n = 50
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0):
            return np.nan
        y = np.log(x)
        t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    return atr.rolling(n, min_periods=n).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


# --- Higher-order moments of returns relative to direction --------------






# --- Multi-window agreement features ------------------------------------


def f03ts_f03_trend_strength_metrics_mkmulti_60d_base_v139_signal(closeadj):
    """Number of MK(N) statistics that are > 0 at multi-window {20,40,60,80} (range 0..4)."""
    def _mk(n):
        norm = n * (n - 1) / 2.0
        def _f(x):
            if np.any(~np.isfinite(x)):
                return np.nan
            s = 0
            for i in range(n - 1):
                d = x[i + 1:] - x[i]
                s += int(np.sum(d > 0) - np.sum(d < 0))
            return s / norm
        return closeadj.rolling(n, min_periods=n).apply(_f, raw=True)
    m20 = _mk(20); m40 = _mk(40); m60 = _mk(60); m80 = _mk(80)
    pos = (m20 > 0).astype(float) + (m40 > 0).astype(float) + (m60 > 0).astype(float) + (m80 > 0).astype(float)
    mask = m20.isna() | m40.isna() | m60.isna() | m80.isna()
    return pos.where(~mask).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_r2multi_80d_base_v140_signal(closeadj):
    """Mean R^2 over horizons {20,40,80}."""
    def _r2(n):
        def _f(x):
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
        return closeadj.rolling(n, min_periods=n).apply(_f, raw=True)
    return ((_r2(20) + _r2(40) + _r2(80)) / 3.0).replace([np.inf, -np.inf], np.nan)


# --- Persistence of high-strength regime --------------------------------


def f03ts_f03_trend_strength_metrics_kerfracmid_40d_base_v141_signal(closeadj):
    """Fraction of last 40 bars where KER(20) > 0.5 (significant trend efficiency)."""
    n = 20
    d = (closeadj - closeadj.shift(n)).abs()
    v = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    er = d / v.replace(0.0, np.nan)
    flag = (er > 0.5).astype(float).where(~er.isna())
    return flag.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_chopreg_80d_base_v142_signal(high, low, closeadj):
    """Fraction of last 80 bars where Choppiness(14) > 61.8 (Fibonacci threshold)."""
    n = 14
    tr_n = _tr(high, low, closeadj).rolling(n, min_periods=n).sum()
    hh = high.rolling(n, min_periods=n).max()
    ll = low.rolling(n, min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0, np.nan)) / np.log10(n)
    flag = (chop > 61.8).astype(float).where(~chop.isna())
    return flag.rolling(80, min_periods=80).mean().replace([np.inf, -np.inf], np.nan)


# --- More OHLC features -------------------------------------------------


def f03ts_f03_trend_strength_metrics_hlmidslope_30d_base_v143_signal(high, low):
    """5-bar slope of (high+low)/2 normalized by midpoint at N=30."""
    n = 30
    mid = 0.5 * (high + low)
    sma = mid.rolling(n, min_periods=n).mean()
    return (sma.diff(5) / sma.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_typmompow_25d_base_v144_signal(high, low, close):
    """(typical price - typical[-25]) / sum(|diff|, 25), where typical=(h+l+c)/3."""
    n = 25
    typ = (high + low + close) / 3.0
    d = (typ - typ.shift(n)).abs()
    v = typ.diff().abs().rolling(n, min_periods=n).sum()
    return (d / v.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Lo-MacKinlay-style ratio differences ------------------------------


def f03ts_f03_trend_strength_metrics_vrdiff_120d_base_v145_signal(closeadj):
    """VarianceRatio(q=2) - VarianceRatio(q=10), N=120. Cross-scale trend signature."""
    n = 120
    r1 = np.log(closeadj).diff()
    v1 = r1.rolling(n, min_periods=n).var(ddof=1)
    vq2 = np.log(closeadj).diff(2).rolling(n, min_periods=n).var(ddof=1)
    vq10 = np.log(closeadj).diff(10).rolling(n, min_periods=n).var(ddof=1)
    return ((vq2 / (2 * v1.replace(0.0, np.nan))) - (vq10 / (10 * v1.replace(0.0, np.nan)))).replace([np.inf, -np.inf], np.nan)


# --- Robust trend slope (Theil-Sen-like simplified) --------------------


def f03ts_f03_trend_strength_metrics_robslp_25d_base_v146_signal(closeadj):
    """Median pairwise slope estimator at N=25 (Theil-Sen subsample)."""
    n = 25
    def _ts(x):
        if np.any(~np.isfinite(x)):
            return np.nan
        slopes = []
        for i in range(n - 1):
            slopes.append((x[-1] - x[i]) / (n - 1 - i + 1e-9))
        return float(np.median(slopes))
    return closeadj.rolling(n, min_periods=n).apply(_ts, raw=True).replace([np.inf, -np.inf], np.nan)


# --- DM "balance" features ---------------------------------------------


def f03ts_f03_trend_strength_metrics_plusminusratio_30d_base_v147_signal(high, low):
    """(+DM(20) - -DM(20)) / (+DM(20) + -DM(20)) — DM imbalance ratio."""
    pdm = _plus_dm(high, low).rolling(20, min_periods=20).mean()
    mdm = _minus_dm(high, low).rolling(20, min_periods=20).mean()
    return ((pdm - mdm) / (pdm + mdm).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Pure run-fraction features ----------------------------------------


def f03ts_f03_trend_strength_metrics_signz_50d_base_v148_signal(closeadj):
    """Z-score of sign-sum: ((sum sign(diff))/N) divided by its rolling 100d std."""
    n = 50
    s = np.sign(closeadj.diff()).rolling(n, min_periods=n).sum() / n
    sd = s.rolling(100, min_periods=100).std(ddof=1)
    return (s / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# --- Trend-vs-Range power ratio ---------------------------------------


def f03ts_f03_trend_strength_metrics_trrng_30d_base_v149_signal(high, low, closeadj):
    """log( |close - close[-30]| / range_30 ), where range_30 = max(high,30)-min(low,30)."""
    n = 30
    move = (closeadj - closeadj.shift(n)).abs()
    rng = high.rolling(n, min_periods=n).max() - low.rolling(n, min_periods=n).min()
    return np.log((move + 1e-12) / rng.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f03ts_f03_trend_strength_metrics_efqctile_50d_base_v150_signal(closeadj):
    """Difference: KER(50) - 50d median KER. Anomaly of efficiency."""
    n = 50
    d = (closeadj - closeadj.shift(n)).abs()
    v = closeadj.diff().abs().rolling(n, min_periods=n).sum()
    er = d / v.replace(0.0, np.nan)
    med = er.rolling(50, min_periods=50).median()
    return (er - med).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f03_trend_strength_metrics_base_076_150_REGISTRY = dict([
    _e(f03ts_f03_trend_strength_metrics_adx_8d_base_v076_signal, "high", "low", "close"),
    _e(f03ts_f03_trend_strength_metrics_adxrank_120d_base_v077_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_pdimrnk_60d_base_v078_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_dxraw_14d_base_v079_signal, "high", "low", "close"),
    _e(f03ts_f03_trend_strength_metrics_adxz_60d_base_v080_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_aroonup_18d_base_v081_signal, "close"),
    _e(f03ts_f03_trend_strength_metrics_aroondn_40d_base_v082_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_aroonlog_25d_base_v083_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_viplus_21d_base_v084_signal, "high", "low", "close"),
    _e(f03ts_f03_trend_strength_metrics_viminus_40d_base_v085_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_visum_50d_base_v086_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_chop_28d_base_v087_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_chopdiff_30d_base_v088_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_tsi_13_7_base_v089_signal, "close"),
    _e(f03ts_f03_trend_strength_metrics_tsihigh_25_13_base_v090_signal, "high"),
    _e(f03ts_f03_trend_strength_metrics_kefr_5d_base_v091_signal, "close"),
    _e(f03ts_f03_trend_strength_metrics_kerhi_50d_base_v093_signal, "high"),
    _e(f03ts_f03_trend_strength_metrics_kerlo_50d_base_v094_signal, "high", "low"),
    _e(f03ts_f03_trend_strength_metrics_r2lin_40d_base_v095_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_logregslp_30d_base_v096_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_logregslp_180d_base_v097_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_regresid_60d_base_v098_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_regrsnr_50d_base_v099_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_polylin_40d_base_v100_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_polyquad_120d_base_v101_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_hurstrs_60d_base_v102_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_varratio_q20_120d_base_v103_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_hurstdiff_120d_base_v104_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_mk_15d_base_v105_signal, "close"),
    _e(f03ts_f03_trend_strength_metrics_mk_90d_base_v106_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_anymonotone_30d_base_v107_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_uprunlong_120d_base_v108_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_dirsignmean_8d_base_v109_signal, "close"),
    _e(f03ts_f03_trend_strength_metrics_acclbal_45d_base_v110_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_sameside_60d_base_v111_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_efrmulti_30d_base_v112_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_efragree_30d_base_v113_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_sigmoidker_25d_base_v114_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_arctsi_30d_base_v115_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_pricedispr_40d_base_v116_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_pricesnr_60d_base_v117_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_rangertr_50d_base_v118_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_bullbarpct_40d_base_v119_signal, "close", "open"),
    _e(f03ts_f03_trend_strength_metrics_directnbody_30d_base_v120_signal, "close", "open"),
    _e(f03ts_f03_trend_strength_metrics_hhseq_30d_base_v121_signal, "high"),
    _e(f03ts_f03_trend_strength_metrics_llseq_60d_base_v122_signal, "low"),
    _e(f03ts_f03_trend_strength_metrics_atrtrendlong_120d_base_v124_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_daysadxhi_120d_base_v126_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_chopcurv_40d_base_v127_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_kerrank_100d_base_v128_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_tsi_rank_120d_base_v129_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_aroonrank_120d_base_v130_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_distargmax_30d_base_v131_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_distargmin_60d_base_v132_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_kstsig_30d_base_v133_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_kstsign_30d_base_v134_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_stochmom_30d_base_v135_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_atrdrift_50d_base_v136_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_mkmulti_60d_base_v139_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_r2multi_80d_base_v140_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_kerfracmid_40d_base_v141_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_chopreg_80d_base_v142_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_hlmidslope_30d_base_v143_signal, "high", "low"),
    _e(f03ts_f03_trend_strength_metrics_typmompow_25d_base_v144_signal, "high", "low", "close"),
    _e(f03ts_f03_trend_strength_metrics_vrdiff_120d_base_v145_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_robslp_25d_base_v146_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_plusminusratio_30d_base_v147_signal, "high", "low"),
    _e(f03ts_f03_trend_strength_metrics_signz_50d_base_v148_signal, "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_trrng_30d_base_v149_signal, "high", "low", "closeadj"),
    _e(f03ts_f03_trend_strength_metrics_efqctile_50d_base_v150_signal, "closeadj"),
])


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
    for name, entry in f03_trend_strength_metrics_base_076_150_REGISTRY.items():
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
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
