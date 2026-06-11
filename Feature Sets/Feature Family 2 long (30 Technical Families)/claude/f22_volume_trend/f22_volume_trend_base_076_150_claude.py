"""f22_volume_trend base features 076-150.

Second base file: structurally distinct features that do NOT share an
expression up to a window change with 001-075 file. Domain: smoothed /
trended volume. Each function spells its formula inline. NaN policy:
never fillna(<v>); only replace([inf,-inf], nan) at final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (smoothing primitives only)
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wma(s: pd.Series, n: int) -> pd.Series:
    w = np.arange(1, n + 1, dtype=float); w /= w.sum()
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w)), raw=True)


def _wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


def _hma(s: pd.Series, n: int) -> pd.Series:
    half = max(2, n // 2); sqn = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _streak_lastflip(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def _consec(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5: c += 1
        else: break
    return float(c)


def _reg_slope_norm(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx)); vr = np.sum((t - mt) ** 2)
    if vr == 0.0 or not np.isfinite(mx) or mx == 0.0:
        return np.nan
    return float((cov / vr) / mx)


def _reg_rsq(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = np.sum((t - mt) * (x - mx))
    vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
    if vt == 0.0 or vx == 0.0:
        return np.nan
    r = cov / np.sqrt(vt * vx)
    return float(r * r)


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
# Features 076-150
# ---------------------------------------------------------------------------


# === Volume MA distance, kernel diversity, single short feature ============


def f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_base_v076_signal(volume):
    """Normalized 21d-slope of WMA(vol,55) MINUS normalized 21d-slope of
    SMA(vol,55). Same-window kernel-disagreement on volume MA slope —
    distinct from MA-ratio features in file 1."""
    a = _wma(volume, 55); b = _sma(volume, 55)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).replace([np.inf, -np.inf], np.nan)


# === Volume MA convergence ratio with sign reversal ========================


def f22vt_f22_volume_trend_volma_squeeze_30d_base_v077_signal(volume):
    """Std of {SMA(vol,n), EMA(vol,n), WMA(vol,n)} for n=30 divided by their
    mean. 'Squeeze' of volume-MA kernels at same window — distinct from
    differences taken pairwise."""
    n = 30
    mat = pd.concat([_sma(volume, n), _ema(volume, n), _wma(volume, n)], axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume Hurst on smoothed volume series ================================


def f22vt_f22_volume_trend_smoothvol_hurst_120d_base_v078_signal(volume):
    """Hurst exponent of SMA(vol,10) returns over 120 bars. Persistence
    of smoothed-volume changes — long-memory metric."""
    sv = _sma(volume, 10)
    return sv.diff().rolling(120, min_periods=120).apply(_hurst_rs, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA slope sign change frequency (frequency-domain) =============


def f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_base_v079_signal(volume):
    """Fraction of last 45 bars where sign of (EMA(vol,15).diff(5) -
    EMA(vol,60).diff(5)) flipped vs prior bar. Higher = more whipsaw."""
    s = np.sign(_ema(volume, 15).diff(5) - _ema(volume, 60).diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


# === Long DV trend: regression slope on log(DV) ============================


def f22vt_f22_volume_trend_logdv_olsslope_60d_base_v080_signal(closeadj, volume):
    """OLS slope of log(closeadj*volume) over 60 bars, normalized by mean.
    Continuous DV trend slope — regression-based, structurally distinct
    from MA-diff based slope features."""
    return np.log(closeadj * volume).rolling(60, min_periods=60).apply(
        _reg_slope_norm, raw=True
    ).replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_logdv_olsslope_180d_base_v081_signal(closeadj, volume):
    """OLS slope of log(closeadj*volume) over 180 bars, normalized."""
    return np.log(closeadj * volume).rolling(180, min_periods=180).apply(
        _reg_slope_norm, raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === DV trend R^2 over long window =========================================


def f22vt_f22_volume_trend_logdv_rsq_90d_base_v082_signal(closeadj, volume):
    """R^2 of OLS fit on log(DV) over 90 bars. Trend-coherence metric
    for dollar-volume."""
    return np.log(closeadj * volume).rolling(90, min_periods=90).apply(
        _reg_rsq, raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Volume MA arc-distance =================================================


def f22vt_f22_volume_trend_arctan_volsma_dist_15d_base_v083_signal(volume):
    """arctan((volume - SMA(vol,15)) / std(vol,15)). Bounded volume z-score
    via arctan — saturates at +/- pi/2, robust to spikes."""
    m = _sma(volume, 15)
    sd = volume.rolling(15, min_periods=15).std()
    return np.arctan((volume - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA inertia: autocorrelation of smoothed-vol diff ==============


def f22vt_f22_volume_trend_volsma40_ac5_120d_base_v084_signal(volume):
    """Autocorrelation lag-5 of SMA(vol,40).diff() over 120 bars.
    Persistence of volume-MA changes at lag 5 — distinct from lag-1 in file 1."""
    m = _sma(volume, 40).diff()
    return m.rolling(120, min_periods=120).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan,
        raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Smoothed volume range / std ratio =====================================


def f22vt_f22_volume_trend_volsma_range_to_std_60d_base_v085_signal(volume):
    """range of SMA(vol,25) over 60 bars divided by std of SMA(vol,25)
    over same window. Distribution-shape metric of trended volume."""
    m = _sma(volume, 25)
    rng = m.rolling(60, min_periods=60).max() - m.rolling(60, min_periods=60).min()
    sd = m.rolling(60, min_periods=60).std()
    return (rng / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Trend slope sign agreement across kernels =============================


def f22vt_f22_volume_trend_kernel_slope_agree_45d_base_v086_signal(volume):
    """Count of kernels in {SMA,EMA,WMA,Wilder,HMA} at n=45 whose 10d-diff is
    positive, MINUS count whose 10d-diff is negative — integer in [-5,5].
    Kernel-consensus trend metric."""
    n = 45; k = 10
    sl = [_sma(volume, n), _ema(volume, n), _wma(volume, n), _wilder(volume, n), _hma(volume, n)]
    pos = pd.Series(0.0, index=volume.index)
    neg = pd.Series(0.0, index=volume.index)
    mask = ~sl[0].isna()
    for s in sl:
        d = s.diff(k)
        pos = pos + (d > 0.0).astype(float)
        neg = neg + (d < 0.0).astype(float)
        mask = mask & ~d.isna()
    return (pos - neg).where(mask).replace([np.inf, -np.inf], np.nan)


# === Volume / dollar-volume cross-correlation in MA space ==================


def f22vt_f22_volume_trend_volma_dvma_corr_60d_base_v087_signal(closeadj, volume):
    """60d rolling correlation of SMA(vol,20) and SMA(closeadj*vol,20).
    Captures whether the volume-MA and DV-MA move together (price stable)
    or diverge (price trends without volume confirmation)."""
    a = _sma(volume, 20); b = _sma(closeadj * volume, 20)
    return a.rolling(60, min_periods=60).corr(b).replace([np.inf, -np.inf], np.nan)


# === Volume MA stationarity (R^2 of MA over its own window) ===============


def f22vt_f22_volume_trend_volsma_trend_rsq_120d_base_v088_signal(volume):
    """R^2 of OLS fit of SMA(vol,30) against time over 120 bars.
    How linearly-trending the smoothed-volume is."""
    return _sma(volume, 30).rolling(120, min_periods=120).apply(
        _reg_rsq, raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Volume oscillator sign-streak count ===================================


def f22vt_f22_volume_trend_streak_vol_osc_pos_60d_base_v089_signal(volume):
    """Current consecutive-bar streak of (SMA(vol,10) > SMA(vol,50)) over 60d.
    Discrete count of bars of bullish volume oscillator."""
    above = (_sma(volume, 10) > _sma(volume, 50)).astype(float).where(
        ~_sma(volume, 50).isna()
    )
    return above.rolling(60, min_periods=60).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume trend reversal frequency (days since flip) =====================


def f22vt_f22_volume_trend_daysince_voldn_emaup_90d_base_v090_signal(volume):
    """Days since last sign-flip of (EMA(vol,40).diff(10)). When does the
    smoothed-volume slope last change direction?"""
    m = _ema(volume, 40)
    s = np.sign(m.diff(10))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(90, min_periods=90).apply(_streak_lastflip, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume-MA elasticity (slope-to-distance ratio) ========================


def f22vt_f22_volume_trend_volma_elasticity_50d_base_v091_signal(volume):
    """SMA(vol,50) 10d-slope normalized by 10d-mean of |vol - SMA(vol,50)|.
    Slope of trended volume in units of typical volume-deviation —
    distinct elasticity-style ratio."""
    m = _sma(volume, 50)
    dev = (volume - m).abs().rolling(10, min_periods=10).mean()
    return (m.diff(10) / dev.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Net volume on trend (up-bar volume minus down-bar volume MA) =========


def f22vt_f22_volume_trend_netvol_ema_slope_45d_base_v092_signal(close, volume):
    """10d-diff of (EMA(sign(close.diff()) * volume, 45) / EMA(volume, 45)).
    SLOPE of normalized signed-volume EMA — distinct from the level itself."""
    sv = np.sign(close.diff()) * volume
    ratio = (sv.ewm(span=45, adjust=False, min_periods=45).mean() /
             volume.ewm(span=45, adjust=False, min_periods=45).mean().replace(0.0, np.nan))
    return ratio.diff(10).replace([np.inf, -np.inf], np.nan)


# === OBV-like trend in MA space ============================================


def f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_base_v093_signal(close, volume):
    """Z-score of EMA(sign(close.diff())*volume, 25) computed over 75d
    trailing window. Smoothed-signed-volume regime metric — structurally
    distinct from up/down-vol ratios and OBV cumulative measures."""
    sv = np.sign(close.diff()) * volume
    e = sv.ewm(span=10, adjust=False, min_periods=10).mean()
    return ((e - e.rolling(75, min_periods=75).mean()) /
            e.rolling(75, min_periods=75).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Accumulation/distribution-line trend ==================================


def f22vt_f22_volume_trend_ad_line_slope_120d_base_v094_signal(high, low, closeadj, volume):
    """Rolling 120-bar sum of money-flow-volume / 120d mean volume.
    Direction-signal equivalent to A/D-line slope; window-sum form avoids
    fillna pattern that cumulative A/D otherwise needs."""
    rng = (high - low).replace(0.0, np.nan)
    mfm = ((closeadj - low) - (high - closeadj)) / rng
    mfv = mfm * volume
    norm = volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    return (mfv.rolling(120, min_periods=120).sum() / norm).replace([np.inf, -np.inf], np.nan)


# === Long horizon volume regime rank =======================================


def f22vt_f22_volume_trend_logvolma_rank_200_500d_base_v095_signal(volume):
    """Percentile rank of SMA(log(vol), 200) over trailing 500d window.
    Long-horizon trended-log-volume regime."""
    m = _sma(np.log(volume), 200)
    return m.rolling(500, min_periods=500).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA % above sigma band =========================================


def f22vt_f22_volume_trend_volsma_above_band_freq_45d_base_v096_signal(volume):
    """Fraction of last 45 bars that volume exceeded SMA(vol,20)+std(vol,20).
    Frequency of bullish-volume bursts above smoothed-volume +1-sigma."""
    m = _sma(volume, 20); sd = volume.rolling(20, min_periods=20).std()
    upper = m + sd
    above = (volume > upper).astype(float).where(~upper.isna())
    return above.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


# === Volume MA below sigma band ===========================================


def f22vt_f22_volume_trend_volsma_below_band_freq_120d_base_v097_signal(volume):
    """Fraction of last 120 bars where volume < SMA(vol,30) - std(vol,30).
    Frequency of low-volume periods, complement of v096."""
    m = _sma(volume, 30); sd = volume.rolling(30, min_periods=30).std()
    lower = m - sd
    below = (volume < lower).astype(float).where(~lower.isna())
    return below.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Cross-window dollar-volume slope spread ==============================


def f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_base_v098_signal(closeadj, volume):
    """Normalized 21d-slope of SMA(DV,30) MINUS normalized 21d-slope of
    SMA(DV,120). DV slope-spread (cancels common DV drift)."""
    dv = closeadj * volume
    a = _sma(dv, 30); b = _sma(dv, 120)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).replace([np.inf, -np.inf], np.nan)


# === Volume above its WMA (kernel-distinct streak) =========================


def f22vt_f22_volume_trend_streak_above_volwma25_60d_base_v099_signal(volume):
    """Consecutive-bar streak of (volume > WMA(vol,25)) over 60d.
    WMA kernel distinct from SMA in file 1's streak features."""
    above = (volume > _wma(volume, 25)).astype(float).where(~_wma(volume, 25).isna())
    return above.rolling(60, min_periods=60).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA range (recent max - recent min, normalized) ================


def f22vt_f22_volume_trend_volema_swing_180d_base_v100_signal(volume):
    """(max(EMA(vol,40),180d) - min(EMA(vol,40),180d)) / mean(EMA(vol,40),180d).
    Long-horizon trended-volume swing amplitude."""
    m = _ema(volume, 40)
    rng = m.rolling(180, min_periods=180).max() - m.rolling(180, min_periods=180).min()
    mn = m.rolling(180, min_periods=180).mean().replace(0.0, np.nan)
    return (rng / mn).replace([np.inf, -np.inf], np.nan)


# === Volume MA jerk-style normalized ======================================


def f22vt_f22_volume_trend_volsma_jerk_75d_base_v101_signal(volume):
    """SMA(vol,75) 3rd-difference (b - 3*b.shift(k) + 3*b.shift(2k) -
    b.shift(3k)) at k=21 normalized by |SMA|. Trended-volume jerk."""
    m = _sma(volume, 75)
    k = 21
    third = m - 3.0 * m.shift(k) + 3.0 * m.shift(2 * k) - m.shift(3 * k)
    return (third / m.abs()).replace([np.inf, -np.inf], np.nan)


# === Force-index inspired (close-diff * volume) MA ratio ==================


def f22vt_f22_volume_trend_force_index_ema13_to_ema50_base_v102_signal(close, volume):
    """EMA of (close.diff() * volume) at span 13, divided by EMA at span 50.
    Classic force-index short/long ratio — flow-driven trend."""
    fi = close.diff() * volume
    a = fi.ewm(span=13, adjust=False, min_periods=13).mean()
    b = fi.ewm(span=50, adjust=False, min_periods=50).mean()
    return (a / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MFI-like trend: positive money flow EMA / negative money flow EMA ====


def f22vt_f22_volume_trend_mfi_trend_ema_30d_base_v103_signal(high, low, closeadj, volume):
    """log(EMA(positive-MF,30) / EMA(negative-MF,30)). Trended money-flow
    ratio — explicitly using typical-price * volume."""
    tp = (high + low + closeadj) / 3.0
    mf = tp * volume
    pos = mf.where(tp > tp.shift(1), 0.0)
    neg = mf.where(tp < tp.shift(1), 0.0)
    a = pos.ewm(span=30, adjust=False, min_periods=30).mean()
    b = neg.ewm(span=30, adjust=False, min_periods=30).mean()
    return np.log(a.replace(0.0, np.nan) / b.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Trended volume entropy / dispersion ==================================


def f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_base_v104_signal(volume):
    """IQR / median of SMA(vol,30) over 60 bars. Robust spread-to-center
    metric on trended volume."""
    m = _sma(volume, 30)
    def _f(x):
        if len(x) < 4: return np.nan
        q1 = np.quantile(x, 0.25); q3 = np.quantile(x, 0.75); med = np.median(x)
        if med == 0.0 or not np.isfinite(med): return np.nan
        return float((q3 - q1) / med)
    return m.rolling(60, min_periods=60).apply(_f, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume MA gap (volume - MA) MA itself - smoothed deviation ===========


def f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_base_v105_signal(volume):
    """Fraction of last 60 bars where EMA((volume - SMA(vol,20))/SMA(vol,20), 25)
    is POSITIVE. Discrete frequency of persistent above-trend regime —
    bounded [0,1], structurally different from continuous log-ratio."""
    m = _sma(volume, 20)
    pct = (volume - m) / m.replace(0.0, np.nan)
    sm = pct.ewm(span=25, adjust=False, min_periods=25).mean()
    above = (sm > 0.0).astype(float).where(~sm.isna())
    return above.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Volume MA log-ratio long ==============================================


def f22vt_f22_volume_trend_volema_long_ratio_to_3sma_base_v106_signal(volume):
    """log(EMA(vol,180)) - mean over 100d of log(SMA(vol,60)). Long EMA
    relative to mid-window trailing mean of mid SMA — captures very-long
    horizon volume regime drift relative to recent trend baseline."""
    a = np.log(_ema(volume, 180))
    b = np.log(_sma(volume, 60)).rolling(100, min_periods=100).mean()
    return (a - b).replace([np.inf, -np.inf], np.nan)


# === Smoothed volume mean reversion rate ==================================


def f22vt_f22_volume_trend_volma_reversion_freq_100d_base_v107_signal(volume):
    """Fraction of last 100 bars where (volume - SMA(vol,20)) flipped sign
    relative to prior bar. Volume mean-reversion-around-MA rate."""
    d = volume - _sma(volume, 20)
    s = np.sign(d)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(100, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


# === Volume MA double-cross sign ==========================================


def f22vt_f22_volume_trend_sign_double_cross_volsma_base_v108_signal(volume):
    """sign((vol - SMA(vol,10))) * sign((SMA(vol,10) - SMA(vol,40))).
    Two-level volume-MA confirmation — bull (+1) when vol > short MA AND
    short MA > long MA. Discrete in {-1,0,1}."""
    a = np.sign(volume - _sma(volume, 10))
    b = np.sign(_sma(volume, 10) - _sma(volume, 40))
    return (a * b).replace([np.inf, -np.inf], np.nan)


# === Trended dollar volume relative to historical max =====================


def f22vt_f22_volume_trend_dv_drawdown_from_max_252d_base_v109_signal(closeadj, volume):
    """log(EMA(DV,30) / cummax(EMA(DV,30), 252d)). Drawdown of trended
    dollar-volume from its 252d-trailing-max. Always <= 0."""
    dv = closeadj * volume
    m = _ema(dv, 30)
    mx = m.rolling(252, min_periods=252).max().replace(0.0, np.nan)
    return np.log(m / mx).replace([np.inf, -np.inf], np.nan)


# === Trended volume gain from min =========================================


def f22vt_f22_volume_trend_volma_gain_from_min_120d_base_v110_signal(volume):
    """log(SMA(vol,30) / cummin(SMA(vol,30), 120d)). Trended-volume gain
    from 120d-trailing-min. Always >= 0."""
    m = _sma(volume, 30)
    mn = m.rolling(120, min_periods=120).min().replace(0.0, np.nan)
    return np.log(m / mn).replace([np.inf, -np.inf], np.nan)


# === Log-volume difference / std (vol-trend over vol-volatility) ==========


def f22vt_f22_volume_trend_logvol_diff_over_std_30d_base_v111_signal(volume):
    """(log(vol) - log(vol).shift(30)) / std(log(vol),30). Vol log-trend
    in units of log-vol standard deviation."""
    lv = np.log(volume)
    sd = lv.rolling(30, min_periods=30).std()
    return ((lv - lv.shift(30)) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA cross-window slope sign agreement ==========================


def f22vt_f22_volume_trend_volma_slope_sign_count_60d_base_v112_signal(volume):
    """Count of SMA(vol,n) for n in {10,30,60,90,150} whose 10d-diff sign
    is positive. Integer 0..5. Cross-window slope-consensus count."""
    cnt = pd.Series(0.0, index=volume.index)
    mask = ~_sma(volume, 150).isna()
    for n in (10, 30, 60, 90, 150):
        d = _sma(volume, n).diff(10)
        cnt = cnt + (d > 0.0).astype(float)
        mask = mask & ~d.isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


# === Trended volume centered z-score against trailing kernel mean =========


def f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_base_v113_signal(volume):
    """((SMA(vol,30) - SMA(vol,180)) / std(SMA(vol,30) over 180d)).
    Z-score of short-window volume MA against long-window trailing mean
    and std."""
    sw = _sma(volume, 30); lw = _sma(volume, 180)
    sd = sw.rolling(180, min_periods=180).std()
    return ((sw - lw) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Trended volume %change in MA space (acceleration of slope) ===========


def f22vt_f22_volume_trend_volema_slope_pctchg_45d_base_v114_signal(volume):
    """((EMA(vol,30).diff(5) - EMA(vol,30).diff(5).shift(45)) /
    |EMA(vol,30).diff(5).shift(45)|. Slope-of-slope acceleration."""
    sl = _ema(volume, 30).diff(5)
    base_sl = sl.shift(45)
    return ((sl - base_sl) / base_sl.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DV trend strength via Hurst ==========================================


def f22vt_f22_volume_trend_logdv_hurst_120d_base_v115_signal(closeadj, volume):
    """Hurst R/S on log(DV) returns over 120 bars. Persistence of dollar-
    volume changes."""
    dv = closeadj * volume
    return np.log(dv).diff().rolling(120, min_periods=120).apply(
        _hurst_rs, raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Sign of up/down volume MA crossover ==================================


def f22vt_f22_volume_trend_sign_upvol_downvol_ema30_base_v116_signal(close, volume):
    """sign(EMA(up-vol,30) - EMA(down-vol,30)). Discrete signed direction
    of mid-window up/down volume trend (distinct from log-ratio in file 1)."""
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.ewm(span=30, adjust=False, min_periods=30).mean()
    b = dn.ewm(span=30, adjust=False, min_periods=30).mean()
    return np.sign(a - b).replace([np.inf, -np.inf], np.nan)


# === Volume MA percentile across multi-window panel ========================


def f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_base_v117_signal(volume):
    """(SMA(vol,10) - SMA(vol,60)) divided by std(volume,60). Short/long
    MA diff in units of raw volume std — distinct from log-ratio."""
    a = _sma(volume, 10); b = _sma(volume, 60)
    sd = volume.rolling(60, min_periods=60).std()
    return ((a - b) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA bandwidth (Bollinger-style on smoothed volume) =============


def f22vt_f22_volume_trend_volma_bandwidth_40d_base_v118_signal(volume):
    """std(SMA(vol,15) over 40d) / mean(SMA(vol,15) over 40d). Trended-
    volume Bollinger-bandwidth."""
    m = _sma(volume, 15)
    sd = m.rolling(40, min_periods=40).std()
    mn = m.rolling(40, min_periods=40).mean().replace(0.0, np.nan)
    return (sd / mn).replace([np.inf, -np.inf], np.nan)


# === Volume MA inverse % rank =============================================


def f22vt_f22_volume_trend_volsma_rev_rank_300d_base_v119_signal(volume):
    """1 - percentile rank of SMA(vol,45) over 300d window. Inverse rank
    is structurally different (anti-correlated) from straight rank in file 1."""
    m = _sma(volume, 45)
    return (1.0 - m.rolling(300, min_periods=300).rank(pct=True)).replace([np.inf, -np.inf], np.nan)


# === Volume MA centered range fraction ====================================


def f22vt_f22_volume_trend_volsma_center_pos_90d_base_v120_signal(volume):
    """(SMA(vol,20) - mean(SMA(vol,20),90d)) / range(SMA(vol,20),90d).
    Center-of-range position metric, bounded ~[-0.5, 0.5]."""
    m = _sma(volume, 20)
    mu = m.rolling(90, min_periods=90).mean()
    rng = m.rolling(90, min_periods=90).max() - m.rolling(90, min_periods=90).min()
    return ((m - mu) / rng.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Smoothed volume MAD-to-std ratio ======================================


def f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_base_v121_signal(volume):
    """MAD / std of SMA(vol,15) over 60d. Distribution-shape metric on
    trended volume (Gaussian = ~0.8, fatter tails differ)."""
    m = _sma(volume, 15)
    sd = m.rolling(60, min_periods=60).std()
    mad = m.rolling(60, min_periods=60).apply(
        lambda x: float(np.mean(np.abs(x - np.mean(x)))), raw=True
    )
    return (mad / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA skewness ==================================================


def f22vt_f22_volume_trend_smoothvol_skew_90d_base_v122_signal(volume):
    """Skewness of SMA(vol,30) over 90d. Distribution-shape metric on
    trended volume — independent of magnitude."""
    return _sma(volume, 30).rolling(90, min_periods=90).skew().replace([np.inf, -np.inf], np.nan)


# === Volume MA kurtosis ==================================================


def f22vt_f22_volume_trend_smoothvol_kurt_180d_base_v123_signal(volume):
    """Excess kurtosis of SMA(vol,40) over 180d. Tail-shape metric on
    trended volume."""
    return _sma(volume, 40).rolling(180, min_periods=180).kurt().replace([np.inf, -np.inf], np.nan)


# === Volume sign-of-slope autocorrelation ================================


def f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_base_v124_signal(volume):
    """Lag-1 autocorrelation of sign(SMA(vol,30).diff(5)) over 90d.
    Persistence of volume-trend direction (sign-only)."""
    s = np.sign(_sma(volume, 30).diff(5))
    return s.rolling(90, min_periods=90).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan,
        raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Cumulative excess volume above MA over window =======================


def f22vt_f22_volume_trend_cum_excess_volma_120d_base_v125_signal(volume):
    """Sum of max(0, volume - SMA(vol,30)) over 120d divided by sum of
    volume over 120d. Fraction of volume that exceeded its trend."""
    m = _sma(volume, 30)
    excess = (volume - m).clip(lower=0.0)
    a = excess.rolling(120, min_periods=120).sum()
    b = volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return (a / b).replace([np.inf, -np.inf], np.nan)


# === Volume MA convex/concave count (3-point sign of curvature) ===========


def f22vt_f22_volume_trend_volema30_convex_frac_60d_base_v126_signal(volume):
    """Fraction of last 60 bars where 2nd-diff (EMA(vol,30) - 2*shift(5) +
    shift(10)) > 0 (convex). Long-horizon trended-volume curvature freq."""
    m = _ema(volume, 30)
    curv = m - 2.0 * m.shift(5) + m.shift(10)
    pos = (curv > 0.0).astype(float).where(~curv.isna())
    return pos.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Dollar volume rank percentile ========================================


def f22vt_f22_volume_trend_dv_rank_180d_base_v127_signal(closeadj, volume):
    """Percentile rank of EMA(DV,40) over trailing 180d. Long-trended
    dollar-volume regime rank."""
    return _ema(closeadj * volume, 40).rolling(180, min_periods=180).rank(
        pct=True
    ).replace([np.inf, -np.inf], np.nan)


# === Volume MA flip lag (lag at which sign of slope last changed) =========


def f22vt_f22_volume_trend_daysince_volsma_signflip_252d_base_v128_signal(volume):
    """Days since last sign-flip of (vol - SMA(vol,40)) over 252d. Long-
    horizon flip-distance."""
    s = np.sign(volume - _sma(volume, 40))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(252, min_periods=252).apply(_streak_lastflip, raw=True).replace([np.inf, -np.inf], np.nan)


# === Up/down volume MA z-score difference =================================


def f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_base_v129_signal(close, volume):
    """((SMA(up-vol,30)-mean60d)/std60d) MINUS ((SMA(dn-vol,30)-mean60d)/std60d).
    Z-score spread of up-vol MA vs down-vol MA over 60d."""
    up = volume.where(close.diff() > 0.0, 0.0)
    dn = volume.where(close.diff() < 0.0, 0.0)
    a = up.rolling(30, min_periods=30).mean()
    b = dn.rolling(30, min_periods=30).mean()
    za = (a - a.rolling(60, min_periods=60).mean()) / a.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    zb = (b - b.rolling(60, min_periods=60).mean()) / b.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return (za - zb).replace([np.inf, -np.inf], np.nan)


# === Smoothed volume momentum (rate-of-change of MA) ======================


def f22vt_f22_volume_trend_volsma_pctroc_45d_base_v130_signal(volume):
    """(SMA(vol,25) / SMA(vol,25).shift(45)) - 1. Pct rate-of-change of
    trended volume over 45 bars — distinct from log-roc on raw volume."""
    m = _sma(volume, 25)
    return (m / m.shift(45) - 1.0).replace([np.inf, -np.inf], np.nan)


# === Trended dollar volume normalized by price ============================


def f22vt_f22_volume_trend_dv_per_price_ma_60d_base_v131_signal(closeadj, volume):
    """log( EMA(DV,60) / (closeadj * EMA(vol,60)) ). Ratio of trended DV to
    spot-price * trended-volume — captures price-trend within DV-trend
    over equal smoothing windows."""
    dv = closeadj * volume
    return np.log(_ema(dv, 60) / (closeadj * _ema(volume, 60))).replace([np.inf, -np.inf], np.nan)


# === Volume MA cross-window R^2 of slope ==================================


def f22vt_f22_volume_trend_volma_slope_consistency_120d_base_v132_signal(volume):
    """R^2 of OLS fit of (EMA(vol,30) - EMA(vol,90)) over 120 bars.
    Trend-coherence of the MA-spread itself."""
    spread = _ema(volume, 30) - _ema(volume, 90)
    return spread.rolling(120, min_periods=120).apply(_reg_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === Volume oscillator divergence over time ===============================


def f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_base_v133_signal(volume):
    """(SMA(vol,5)-SMA(vol,30))/SMA(vol,30) MINUS shift(45) of same.
    Change in volume oscillator over 45 bars — trend in volume oscillator."""
    o = (_sma(volume, 5) - _sma(volume, 30)) / _sma(volume, 30).replace(0.0, np.nan)
    return (o - o.shift(45)).replace([np.inf, -np.inf], np.nan)


# === Long-horizon trended volume reversal index ============================


def f22vt_f22_volume_trend_volma_max_min_diff_log_252d_base_v134_signal(volume):
    """log(max(EMA(vol,50),252d) / min(EMA(vol,50),252d)). Log range of
    trended volume over a year. Always >= 0."""
    m = _ema(volume, 50)
    mx = m.rolling(252, min_periods=252).max(); mn = m.rolling(252, min_periods=252).min()
    return np.log(mx / mn.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Trended volume sign of long-short MA spread, percentile =============


def f22vt_f22_volume_trend_volma_spread_rank_252d_base_v135_signal(volume):
    """Percentile rank of (SMA(vol,15) - SMA(vol,60)) over 252d. Where in
    the year is the current short/long MA spread?"""
    spread = _sma(volume, 15) - _sma(volume, 60)
    return spread.rolling(252, min_periods=252).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === Smoothed signed volume EMA ratio ====================================


def f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_base_v136_signal(close, volume):
    """log( EMA(sign(close.diff())*vol, 20) / EMA(sign(close.diff())*vol, 80) ).
    Ratio of short to long signed-volume EMAs — flow-trend ratio."""
    sv = np.sign(close.diff()) * volume
    a = sv.ewm(span=20, adjust=False, min_periods=20).mean()
    b = sv.ewm(span=80, adjust=False, min_periods=80).mean()
    return np.log(a.abs().replace(0.0, np.nan) / b.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA trend-following frac ========================================


def f22vt_f22_volume_trend_volma_signconsistency_90d_base_v137_signal(volume):
    """Fraction of last 90 bars where sign(SMA(vol,10) - SMA(vol,30)) ==
    sign(SMA(vol,30) - SMA(vol,90)). Trend-following alignment frequency."""
    s1 = np.sign(_sma(volume, 10) - _sma(volume, 30))
    s2 = np.sign(_sma(volume, 30) - _sma(volume, 90))
    agree = (s1 == s2).astype(float).where(~s1.isna() & ~s2.isna())
    return agree.rolling(90, min_periods=90).mean().replace([np.inf, -np.inf], np.nan)


# === Trended dollar volume MA percentile ==================================


def f22vt_f22_volume_trend_dv_ma_log_rank_252d_base_v138_signal(closeadj, volume):
    """Percentile rank of log(SMA(DV,40)) over 252d. Long DV-MA log-rank."""
    return np.log(_sma(closeadj * volume, 40)).rolling(252, min_periods=252).rank(
        pct=True
    ).replace([np.inf, -np.inf], np.nan)


# === Trended volume slope curvature ratio =================================


def f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_base_v139_signal(volume):
    """(SMA(vol,50).diff(10)) / (SMA(vol,50) - 2*SMA(vol,50).shift(10) +
    SMA(vol,50).shift(20)). Ratio of slope to curvature — when |large|
    indicates pure trend, when small indicates flat or turning."""
    m = _sma(volume, 50)
    sl = m.diff(10)
    cu = m - 2.0 * m.shift(10) + m.shift(20)
    return (sl / cu.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Bounded transform of MA ratio for stability ==========================


def f22vt_f22_volume_trend_sigmoid_volma_spread_70d_base_v140_signal(volume):
    """1 / (1 + exp(-(log(SMA(vol,20)/SMA(vol,70))))). Sigmoid of mid-vs-long
    volume MA log-ratio — bounded in (0,1)."""
    x = np.log(_sma(volume, 20) / _sma(volume, 70))
    return (1.0 / (1.0 + np.exp(-x))).replace([np.inf, -np.inf], np.nan)


# === Long horizon trend strength: linear regression slope of MA ============


def f22vt_f22_volume_trend_volsma_regslope_normalized_180d_base_v141_signal(volume):
    """Normalized OLS slope of SMA(vol,40) over 180 bars."""
    return _sma(volume, 40).rolling(180, min_periods=180).apply(
        _reg_slope_norm, raw=True
    ).replace([np.inf, -np.inf], np.nan)


# === Trended volume relative to mid-point of range ========================


def f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_base_v142_signal(volume):
    """Fraction of last 120 bars where SMA(vol,20) > (max+min)/2 over 60d.
    How often trended volume is in upper half of recent range."""
    m = _sma(volume, 20)
    mid = (m.rolling(60, min_periods=60).max() + m.rolling(60, min_periods=60).min()) / 2.0
    above = (m > mid).astype(float).where(~mid.isna())
    return above.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Dollar-volume slope smoothing =========================================


def f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_base_v143_signal(closeadj, volume):
    """EMA of (log(DV) - log(DV).shift(30)) at span 45. Smoothed long-DV ROC."""
    lr = np.log(closeadj * volume).diff(30)
    return lr.ewm(span=45, adjust=False, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


# === Volume MA proximity to median over long window =======================


def f22vt_f22_volume_trend_volma_minus_med_120d_base_v144_signal(volume):
    """(SMA(vol,25) - median(SMA(vol,25), 120d)) / median. Trended-volume
    distance from long-horizon median, normalized."""
    m = _sma(volume, 25)
    med = m.rolling(120, min_periods=120).median()
    return ((m - med) / med.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Volume MA momentum decay ==============================================


def f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_base_v145_signal(volume):
    """SMA(vol,30).diff(10) / SMA(vol,30).diff(10).shift(30). Slope-to-lagged-
    slope ratio — captures whether trend is accelerating or decaying."""
    sl = _sma(volume, 30).diff(10)
    return (sl / sl.shift(30).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Trended-volume distribution z-score on log space =====================


def f22vt_f22_volume_trend_log_volma_long_z_504d_base_v146_signal(volume):
    """(SMA(log(vol),60) - mean over 504d) / std over 504d. Very-long
    horizon trended-log-volume z-score."""
    m = _sma(np.log(volume), 60)
    return ((m - m.rolling(504, min_periods=504).mean()) /
            m.rolling(504, min_periods=504).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Dollar volume MA crossover sign =====================================


def f22vt_f22_volume_trend_sign_dv_ma_15_60_base_v147_signal(closeadj, volume):
    """sign(EMA(DV,15) - EMA(DV,60)). Discrete dollar-volume MA crossover."""
    dv = closeadj * volume
    return np.sign(_ema(dv, 15) - _ema(dv, 60)).replace([np.inf, -np.inf], np.nan)


# === Volume MA divergence from price MA: cross-signal ====================


def f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_base_v148_signal(closeadj, volume):
    """Normalized 21d-slope of SMA(vol,60) MINUS normalized 21d-slope of
    SMA(closeadj,60). Volume-trend slope distinctness from price slope."""
    a = _sma(volume, 60); b = _sma(closeadj, 60)
    return (a.diff(21) / a.abs() - b.diff(21) / b.abs()).replace([np.inf, -np.inf], np.nan)


# === Smoothed dollar volume range over its mean (long horizon) ============


def f22vt_f22_volume_trend_dv_ema_range_norm_252d_base_v149_signal(closeadj, volume):
    """range of EMA(DV,30) over 252d divided by mean of EMA(DV,30) over 252d.
    Long-horizon trended dollar-volume swing amplitude."""
    m = _ema(closeadj * volume, 30)
    rng = m.rolling(252, min_periods=252).max() - m.rolling(252, min_periods=252).min()
    mn = m.rolling(252, min_periods=252).mean().replace(0.0, np.nan)
    return (rng / mn).replace([np.inf, -np.inf], np.nan)


# === Composite volume-trend signal (sign + slope + percentile) ============


def f22vt_f22_volume_trend_composite_volma_score_base_v150_signal(volume):
    """sign(SMA(vol,20) - SMA(vol,80)) + sign(SMA(vol,80).diff(21)) +
    (rank(SMA(vol,20), 252d) - 0.5). Composite of three orthogonal trended-
    volume signals — bounded around [-2.5, +2.5]."""
    a = np.sign(_sma(volume, 20) - _sma(volume, 80))
    b = np.sign(_sma(volume, 80).diff(21))
    c = _sma(volume, 20).rolling(252, min_periods=252).rank(pct=True) - 0.5
    return (a + b + c).replace([np.inf, -np.inf], np.nan)


f22_volume_trend_base_076_150_REGISTRY = {
    "f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_base_v076_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volwma_minus_volsma_slope_55d_base_v076_signal},
    "f22vt_f22_volume_trend_volma_squeeze_30d_base_v077_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_squeeze_30d_base_v077_signal},
    "f22vt_f22_volume_trend_smoothvol_hurst_120d_base_v078_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_hurst_120d_base_v078_signal},
    "f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_base_v079_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_vol_ema_slope_xover_freq_45d_base_v079_signal},
    "f22vt_f22_volume_trend_logdv_olsslope_60d_base_v080_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_olsslope_60d_base_v080_signal},
    "f22vt_f22_volume_trend_logdv_olsslope_180d_base_v081_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_olsslope_180d_base_v081_signal},
    "f22vt_f22_volume_trend_logdv_rsq_90d_base_v082_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_rsq_90d_base_v082_signal},
    "f22vt_f22_volume_trend_arctan_volsma_dist_15d_base_v083_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_arctan_volsma_dist_15d_base_v083_signal},
    "f22vt_f22_volume_trend_volsma40_ac5_120d_base_v084_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma40_ac5_120d_base_v084_signal},
    "f22vt_f22_volume_trend_volsma_range_to_std_60d_base_v085_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_range_to_std_60d_base_v085_signal},
    "f22vt_f22_volume_trend_kernel_slope_agree_45d_base_v086_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_kernel_slope_agree_45d_base_v086_signal},
    "f22vt_f22_volume_trend_volma_dvma_corr_60d_base_v087_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_volma_dvma_corr_60d_base_v087_signal},
    "f22vt_f22_volume_trend_volsma_trend_rsq_120d_base_v088_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_trend_rsq_120d_base_v088_signal},
    "f22vt_f22_volume_trend_streak_vol_osc_pos_60d_base_v089_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_vol_osc_pos_60d_base_v089_signal},
    "f22vt_f22_volume_trend_daysince_voldn_emaup_90d_base_v090_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_voldn_emaup_90d_base_v090_signal},
    "f22vt_f22_volume_trend_volma_elasticity_50d_base_v091_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_elasticity_50d_base_v091_signal},
    "f22vt_f22_volume_trend_netvol_ema_slope_45d_base_v092_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_netvol_ema_slope_45d_base_v092_signal},
    "f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_base_v093_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_signed_vol_ema_zscore_75d_base_v093_signal},
    "f22vt_f22_volume_trend_ad_line_slope_120d_base_v094_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f22vt_f22_volume_trend_ad_line_slope_120d_base_v094_signal},
    "f22vt_f22_volume_trend_logvolma_rank_200_500d_base_v095_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvolma_rank_200_500d_base_v095_signal},
    "f22vt_f22_volume_trend_volsma_above_band_freq_45d_base_v096_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_above_band_freq_45d_base_v096_signal},
    "f22vt_f22_volume_trend_volsma_below_band_freq_120d_base_v097_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_below_band_freq_120d_base_v097_signal},
    "f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_base_v098_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_sma_slope_spread_30_120_base_v098_signal},
    "f22vt_f22_volume_trend_streak_above_volwma25_60d_base_v099_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_streak_above_volwma25_60d_base_v099_signal},
    "f22vt_f22_volume_trend_volema_swing_180d_base_v100_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_swing_180d_base_v100_signal},
    "f22vt_f22_volume_trend_volsma_jerk_75d_base_v101_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_jerk_75d_base_v101_signal},
    "f22vt_f22_volume_trend_force_index_ema13_to_ema50_base_v102_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_force_index_ema13_to_ema50_base_v102_signal},
    "f22vt_f22_volume_trend_mfi_trend_ema_30d_base_v103_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f22vt_f22_volume_trend_mfi_trend_ema_30d_base_v103_signal},
    "f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_base_v104_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_iqr_to_median_60d_base_v104_signal},
    "f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_base_v105_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothed_volgap_sign_freq_60d_base_v105_signal},
    "f22vt_f22_volume_trend_volema_long_ratio_to_3sma_base_v106_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_long_ratio_to_3sma_base_v106_signal},
    "f22vt_f22_volume_trend_volma_reversion_freq_100d_base_v107_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_reversion_freq_100d_base_v107_signal},
    "f22vt_f22_volume_trend_sign_double_cross_volsma_base_v108_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sign_double_cross_volsma_base_v108_signal},
    "f22vt_f22_volume_trend_dv_drawdown_from_max_252d_base_v109_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_drawdown_from_max_252d_base_v109_signal},
    "f22vt_f22_volume_trend_volma_gain_from_min_120d_base_v110_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_gain_from_min_120d_base_v110_signal},
    "f22vt_f22_volume_trend_logvol_diff_over_std_30d_base_v111_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_logvol_diff_over_std_30d_base_v111_signal},
    "f22vt_f22_volume_trend_volma_slope_sign_count_60d_base_v112_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_sign_count_60d_base_v112_signal},
    "f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_base_v113_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_z_against_trailing_180d_base_v113_signal},
    "f22vt_f22_volume_trend_volema_slope_pctchg_45d_base_v114_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema_slope_pctchg_45d_base_v114_signal},
    "f22vt_f22_volume_trend_logdv_hurst_120d_base_v115_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_logdv_hurst_120d_base_v115_signal},
    "f22vt_f22_volume_trend_sign_upvol_downvol_ema30_base_v116_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_sign_upvol_downvol_ema30_base_v116_signal},
    "f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_base_v117_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_short_long_normaldiff_60d_base_v117_signal},
    "f22vt_f22_volume_trend_volma_bandwidth_40d_base_v118_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_bandwidth_40d_base_v118_signal},
    "f22vt_f22_volume_trend_volsma_rev_rank_300d_base_v119_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_rev_rank_300d_base_v119_signal},
    "f22vt_f22_volume_trend_volsma_center_pos_90d_base_v120_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_center_pos_90d_base_v120_signal},
    "f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_base_v121_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_mad_std_ratio_60d_base_v121_signal},
    "f22vt_f22_volume_trend_smoothvol_skew_90d_base_v122_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_skew_90d_base_v122_signal},
    "f22vt_f22_volume_trend_smoothvol_kurt_180d_base_v123_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_smoothvol_kurt_180d_base_v123_signal},
    "f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_base_v124_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_signed_slope_ac1_90d_base_v124_signal},
    "f22vt_f22_volume_trend_cum_excess_volma_120d_base_v125_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_cum_excess_volma_120d_base_v125_signal},
    "f22vt_f22_volume_trend_volema30_convex_frac_60d_base_v126_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volema30_convex_frac_60d_base_v126_signal},
    "f22vt_f22_volume_trend_dv_rank_180d_base_v127_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_rank_180d_base_v127_signal},
    "f22vt_f22_volume_trend_daysince_volsma_signflip_252d_base_v128_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_daysince_volsma_signflip_252d_base_v128_signal},
    "f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_base_v129_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_upvol_z_minus_dnvol_z_60d_base_v129_signal},
    "f22vt_f22_volume_trend_volsma_pctroc_45d_base_v130_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_pctroc_45d_base_v130_signal},
    "f22vt_f22_volume_trend_dv_per_price_ma_60d_base_v131_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_per_price_ma_60d_base_v131_signal},
    "f22vt_f22_volume_trend_volma_slope_consistency_120d_base_v132_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_slope_consistency_120d_base_v132_signal},
    "f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_base_v133_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volosc_minus_lag_volosc_45d_base_v133_signal},
    "f22vt_f22_volume_trend_volma_max_min_diff_log_252d_base_v134_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_max_min_diff_log_252d_base_v134_signal},
    "f22vt_f22_volume_trend_volma_spread_rank_252d_base_v135_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_spread_rank_252d_base_v135_signal},
    "f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_base_v136_signal": {"inputs": ["close", "volume"], "func": f22vt_f22_volume_trend_signedvol_ema_short_long_ratio_base_v136_signal},
    "f22vt_f22_volume_trend_volma_signconsistency_90d_base_v137_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_signconsistency_90d_base_v137_signal},
    "f22vt_f22_volume_trend_dv_ma_log_rank_252d_base_v138_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ma_log_rank_252d_base_v138_signal},
    "f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_base_v139_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_slope_curv_ratio_50d_base_v139_signal},
    "f22vt_f22_volume_trend_sigmoid_volma_spread_70d_base_v140_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_sigmoid_volma_spread_70d_base_v140_signal},
    "f22vt_f22_volume_trend_volsma_regslope_normalized_180d_base_v141_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volsma_regslope_normalized_180d_base_v141_signal},
    "f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_base_v142_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_above_midpoint_freq_120d_base_v142_signal},
    "f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_base_v143_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_ema_logdv_diff_lag30_smoothed_base_v143_signal},
    "f22vt_f22_volume_trend_volma_minus_med_120d_base_v144_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_minus_med_120d_base_v144_signal},
    "f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_base_v145_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_volma_recent_to_older_slope_ratio_base_v145_signal},
    "f22vt_f22_volume_trend_log_volma_long_z_504d_base_v146_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_log_volma_long_z_504d_base_v146_signal},
    "f22vt_f22_volume_trend_sign_dv_ma_15_60_base_v147_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_sign_dv_ma_15_60_base_v147_signal},
    "f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_base_v148_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_volma_slope_minus_pricema_slope_60d_base_v148_signal},
    "f22vt_f22_volume_trend_dv_ema_range_norm_252d_base_v149_signal": {"inputs": ["closeadj", "volume"], "func": f22vt_f22_volume_trend_dv_ema_range_norm_252d_base_v149_signal},
    "f22vt_f22_volume_trend_composite_volma_score_base_v150_signal": {"inputs": ["volume"], "func": f22vt_f22_volume_trend_composite_volma_score_base_v150_signal},
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
    for name, entry in f22_volume_trend_base_076_150_REGISTRY.items():
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
