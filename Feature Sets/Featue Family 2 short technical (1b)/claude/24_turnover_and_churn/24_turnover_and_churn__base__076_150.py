"""turnover_and_churn base features 076-150 — Pipeline 1b-technical.

Continuation of the 150-hypothesis family.
Bucket I: True-range / ATR ratio dynamics.
Bucket J: Volume entropy / dispersion / shape.
Bucket K: Price-volume correlation & churn proxies.
Bucket L: Turnover-day distribution / spikes.
Bucket M: Range / volume joint extremes (climax, silent rally, exhaustion).
Bucket N: Close-location vs range (body/range, doji, small-body coincidences).
Bucket O: Range trend & contraction dynamics (slope, streak, squeeze).
Bucket P: Composite churn / saturation indicators.

Inputs: SEP OHLCV only. Self-contained helpers, PIT-clean.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _bars_since_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# Bucket I — TR / ATR ratios (076-085)
# ============================================================

def f24_tnch_076_tr_over_mean_tr_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / mean(TR, 21) — TR relative to its monthly mean."""
    tr = _true_range(high, low, close)
    return _safe_div(tr, tr.rolling(MDAYS, min_periods=WDAYS).mean())


def f24_tnch_077_tr_over_mean_tr_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / mean(TR, 63) — TR relative to its quarterly mean."""
    tr = _true_range(high, low, close)
    return _safe_div(tr, tr.rolling(QDAYS, min_periods=MDAYS).mean())


def f24_tnch_078_tr_over_std_tr_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """TR / std(TR, 63) — TR in units of TR-volatility (alternate normalization)."""
    tr = _true_range(high, low, close)
    return _safe_div(tr, tr.rolling(QDAYS, min_periods=MDAYS).std())


def f24_tnch_079_atr21_over_atr63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 / ATR63 — short-vs-long ATR ratio."""
    return _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, QDAYS))


def f24_tnch_080_atr21_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 / ATR252 — short vs annual ATR ratio."""
    return _safe_div(_atr(high, low, close, MDAYS), _atr(high, low, close, YDAYS))


def f24_tnch_081_atr63_over_atr252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR63 / ATR252 — medium vs annual ATR ratio."""
    return _safe_div(_atr(high, low, close, QDAYS), _atr(high, low, close, YDAYS))


def f24_tnch_082_atr21_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ATR21 vs trailing 252d distribution."""
    return _rolling_zscore(_atr(high, low, close, MDAYS), YDAYS, min_periods=QDAYS)


def f24_tnch_083_atr_pct_rank_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR21 percentile rank vs trailing 252d."""
    return _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f24_tnch_084_atr_above_252d_median_frac_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars ATR21 above its trailing 252d median — sustained high-vol regime."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    return (a > med).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(med.notna(), np.nan)


def f24_tnch_085_atr_expansion_event_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21 crossed above 1.5x ATR63 this bar — ATR-expansion regime trigger."""
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    ratio = _safe_div(a21, a63)
    return ((ratio.shift(1) <= 1.5) & (ratio > 1.5)).astype(float).where(ratio.notna(), np.nan)


# ============================================================
# Bucket J — Volume entropy / dispersion / shape (086-094)
# ============================================================

def f24_tnch_086_vol_cv_21(volume: pd.Series) -> pd.Series:
    """Volume coefficient of variation (std/mean) over 21 bars."""
    return _safe_div(volume.rolling(MDAYS, min_periods=WDAYS).std(),
                     volume.rolling(MDAYS, min_periods=WDAYS).mean())


def f24_tnch_087_vol_cv_63(volume: pd.Series) -> pd.Series:
    """Volume CV over 63 bars."""
    return _safe_div(volume.rolling(QDAYS, min_periods=MDAYS).std(),
                     volume.rolling(QDAYS, min_periods=MDAYS).mean())


def f24_tnch_088_vol_cv_252(volume: pd.Series) -> pd.Series:
    """Volume CV over 252 bars."""
    return _safe_div(volume.rolling(YDAYS, min_periods=QDAYS).std(),
                     volume.rolling(YDAYS, min_periods=QDAYS).mean())


def f24_tnch_089_vol_top5_share_63(volume: pd.Series) -> pd.Series:
    """Top-5 days' volume / total volume past 63 — concentration index (Gini-ish)."""
    def _top5(w):
        arr = w[~np.isnan(w)]
        if arr.size < 10: return np.nan
        s = np.sort(arr)[-5:].sum()
        tot = arr.sum()
        return s / tot if tot != 0 else np.nan
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_top5, raw=True)


def f24_tnch_090_vol_top5_share_252(volume: pd.Series) -> pd.Series:
    """Top-5 days' volume / total volume past 252 — annual concentration."""
    def _top5(w):
        arr = w[~np.isnan(w)]
        if arr.size < 30: return np.nan
        s = np.sort(arr)[-5:].sum()
        tot = arr.sum()
        return s / tot if tot != 0 else np.nan
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_top5, raw=True)


def f24_tnch_091_vol_entropy_63(volume: pd.Series) -> pd.Series:
    """Normalized Shannon entropy of volume distribution past 63 (proxy via 10-bin histogram)."""
    def _ent(w):
        arr = w[~np.isnan(w)]
        if arr.size < 10: return np.nan
        # Histogram on log-volume for robustness
        x = np.log(arr.clip(1.0))
        rng = x.max() - x.min()
        if rng == 0: return 0.0
        hist, _ = np.histogram(x, bins=10)
        p = hist / hist.sum() if hist.sum() != 0 else hist
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(10))
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_ent, raw=True)


def f24_tnch_092_vol_skew_63(volume: pd.Series) -> pd.Series:
    """Skewness of volume distribution past 63."""
    return volume.rolling(QDAYS, min_periods=MDAYS).skew()


def f24_tnch_093_vol_skew_252(volume: pd.Series) -> pd.Series:
    """Skewness of volume distribution past 252."""
    return volume.rolling(YDAYS, min_periods=QDAYS).skew()


def f24_tnch_094_vol_kurt_252(volume: pd.Series) -> pd.Series:
    """Kurtosis of volume distribution past 252."""
    return volume.rolling(YDAYS, min_periods=QDAYS).kurt()


# ============================================================
# Bucket K — Price-volume correlation & churn proxies (095-103)
# ============================================================

def f24_tnch_095_abs_ret_volume_corr_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d corr(|return|, volume) — short-horizon flow-impact corr."""
    return close.pct_change().abs().rolling(MDAYS, min_periods=WDAYS).corr(volume)


def f24_tnch_096_abs_ret_volume_corr_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr(|return|, volume)."""
    return close.pct_change().abs().rolling(QDAYS, min_periods=MDAYS).corr(volume)


def f24_tnch_097_abs_ret_volume_corr_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(|return|, volume)."""
    return close.pct_change().abs().rolling(YDAYS, min_periods=QDAYS).corr(volume)


def f24_tnch_098_ret_volume_corr_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d corr(return, volume) — sign-sensitive flow-direction corr."""
    return close.pct_change().rolling(MDAYS, min_periods=WDAYS).corr(volume)


def f24_tnch_099_ret_volume_corr_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr(return, volume)."""
    return close.pct_change().rolling(QDAYS, min_periods=MDAYS).corr(volume)


def f24_tnch_100_retstd_over_meanvol_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d std(return) / 21d mean(volume) — volatility per unit traded shares."""
    return _safe_div(close.pct_change().rolling(MDAYS, min_periods=WDAYS).std(),
                     volume.rolling(MDAYS, min_periods=WDAYS).mean())


def f24_tnch_101_retstd_over_meanvol_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d std(return) / 63d mean(volume) — quarterly impact proxy."""
    return _safe_div(close.pct_change().rolling(QDAYS, min_periods=MDAYS).std(),
                     volume.rolling(QDAYS, min_periods=MDAYS).mean())


def f24_tnch_102_abs_ret_per_volume_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """sum(|return|) / sum(volume) past 63 — Amihud-like impact proxy."""
    num = close.pct_change().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den)


def f24_tnch_103_abs_ret_per_volume_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """sum(|return|) / sum(volume) past 252 — annual impact proxy."""
    num = close.pct_change().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    den = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(num, den)


# ============================================================
# Bucket L — Turnover-day distribution / spikes (104-112)
# ============================================================

def f24_tnch_104_max_vol_over_mean_63(volume: pd.Series) -> pd.Series:
    """Max(vol, 63) / mean(vol, 63) — quarterly outlier-day amplitude."""
    return _safe_div(volume.rolling(QDAYS, min_periods=MDAYS).max(),
                     volume.rolling(QDAYS, min_periods=MDAYS).mean())


def f24_tnch_105_max_vol_over_mean_252(volume: pd.Series) -> pd.Series:
    """Max(vol, 252) / mean(vol, 252) — annual outlier amplitude."""
    return _safe_div(volume.rolling(YDAYS, min_periods=QDAYS).max(),
                     volume.rolling(YDAYS, min_periods=QDAYS).mean())


def f24_tnch_106_bars_since_63d_max_vol(volume: pd.Series) -> pd.Series:
    """Bars since volume reached its 63d maximum."""
    at_max = volume == volume.rolling(QDAYS, min_periods=MDAYS).max()
    return _bars_since_true(at_max)


def f24_tnch_107_bars_since_252d_max_vol(volume: pd.Series) -> pd.Series:
    """Bars since volume reached its 252d maximum."""
    at_max = volume == volume.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since_true(at_max)


def f24_tnch_108_bars_since_504d_max_vol(volume: pd.Series) -> pd.Series:
    """Bars since volume reached its 504d (2y) maximum — multi-year peak recency."""
    at_max = volume == volume.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return _bars_since_true(at_max)


def f24_tnch_109_vol_spike_count_63(volume: pd.Series) -> pd.Series:
    """Count of vol-spike bars (vol > 3x rolling 63d median) in past 63."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    spike = (volume > 3.0 * med).astype(float)
    return spike.rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


def f24_tnch_110_vol_spike_count_252(volume: pd.Series) -> pd.Series:
    """Annual count of vol-spike bars."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    spike = (volume > 3.0 * med).astype(float)
    return spike.rolling(YDAYS, min_periods=QDAYS).sum().where(med.notna(), np.nan)


def f24_tnch_111_vol_spike_cluster_flag(volume: pd.Series) -> pd.Series:
    """1 if 3+ vol-spike bars in past 5 bars — cluster warning."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    spike = (volume > 3.0 * med).astype(float)
    cnt = spike.rolling(WDAYS, min_periods=2).sum()
    return (cnt >= 3).astype(float).where(med.notna(), np.nan)


def f24_tnch_112_vol_spike_cluster_count_63(volume: pd.Series) -> pd.Series:
    """Count of bars where vol-spike cluster (3+ in 5) was active, past 63."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    spike = (volume > 3.0 * med).astype(float)
    cluster = (spike.rolling(WDAYS, min_periods=2).sum() >= 3).astype(float)
    return cluster.rolling(QDAYS, min_periods=MDAYS).sum().where(med.notna(), np.nan)


# ============================================================
# Bucket M — Range / volume joint extremes (113-122)
# ============================================================

def f24_tnch_113_climax_pressure_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (TR > 2x ATR21) AND (vol > 2x 21d-avg-vol) — climax-pressure bar."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return ((r > 2.0) & (vr > 2.0)).astype(float).where(r.notna() & vr.notna(), np.nan)


def f24_tnch_114_climax_pressure_count_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax-pressure count past 21 bars."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    f = ((r > 2.0) & (vr > 2.0)).astype(float)
    return f.rolling(MDAYS, min_periods=WDAYS).sum().where(r.notna() & vr.notna(), np.nan)


def f24_tnch_115_climax_pressure_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax-pressure count past 63."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    f = ((r > 2.0) & (vr > 2.0)).astype(float)
    return f.rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna() & vr.notna(), np.nan)


def f24_tnch_116_climax_pressure_count_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax-pressure count past 252."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    f = ((r > 2.0) & (vr > 2.0)).astype(float)
    return f.rolling(YDAYS, min_periods=QDAYS).sum().where(r.notna() & vr.notna(), np.nan)


def f24_tnch_117_bars_since_last_climax(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent climax-pressure bar."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    return _bars_since_true((r > 2.0) & (vr > 2.0))


def f24_tnch_118_silent_rally_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if return > 2x 21d-avg|return| but volume < 0.7x 21d avg — large gain on quiet vol."""
    rt = close.pct_change()
    ar_avg = rt.abs().rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = (rt > 2.0 * ar_avg) & (volume < 0.7 * v_avg)
    return flag.astype(float).where(ar_avg.notna() & v_avg.notna(), np.nan)


def f24_tnch_119_silent_rally_count_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of silent-rally bars in past 63."""
    rt = close.pct_change()
    ar_avg = rt.abs().rolling(MDAYS, min_periods=WDAYS).mean()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((rt > 2.0 * ar_avg) & (volume < 0.7 * v_avg)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().where(ar_avg.notna() & v_avg.notna(), np.nan)


def f24_tnch_120_exhaustion_gap_flag(high: pd.Series, low: pd.Series, open_: pd.Series,
                                       close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if gap > 2% AND vol > 3x 21d-avg AND body < 0.3x range — exhaustion gap signature."""
    pc = close.shift(1)
    gap = ((open_ - pc) / pc).abs()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rng = (high - low).replace(0, np.nan)
    body_ratio = (close - open_).abs() / rng
    flag = (gap > 0.02) & (volume > 3.0 * v_avg) & (body_ratio < 0.3)
    return flag.astype(float).where(v_avg.notna() & rng.notna(), np.nan)


def f24_tnch_121_exhaustion_gap_count_252(high: pd.Series, low: pd.Series, open_: pd.Series,
                                            close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of exhaustion-gap bars."""
    pc = close.shift(1)
    gap = ((open_ - pc) / pc).abs()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rng = (high - low).replace(0, np.nan)
    body_ratio = (close - open_).abs() / rng
    flag = ((gap > 0.02) & (volume > 3.0 * v_avg) & (body_ratio < 0.3)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().where(v_avg.notna() & rng.notna(), np.nan)


def f24_tnch_122_bars_since_last_exhaustion_gap(high: pd.Series, low: pd.Series, open_: pd.Series,
                                                  close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent exhaustion-gap bar."""
    pc = close.shift(1)
    gap = ((open_ - pc) / pc).abs()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    rng = (high - low).replace(0, np.nan)
    body_ratio = (close - open_).abs() / rng
    return _bars_since_true((gap > 0.02) & (volume > 3.0 * v_avg) & (body_ratio < 0.3))


# ============================================================
# Bucket N — Close-location vs range (123-131)
# ============================================================

def f24_tnch_123_body_over_range_mean_21(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of |C - O| / (H - L) past 21 — monthly avg body-to-range ratio."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    return br.rolling(MDAYS, min_periods=WDAYS).mean()


def f24_tnch_124_body_over_range_mean_63(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean body/range past 63 — quarterly avg."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    return br.rolling(QDAYS, min_periods=MDAYS).mean()


def f24_tnch_125_body_over_range_mean_252(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Annual mean body/range."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    return br.rolling(YDAYS, min_periods=QDAYS).mean()


def f24_tnch_126_small_body_frac_63(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with body/range < 0.25 — small-body dwell."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    return (br < 0.25).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(br.notna(), np.nan)


def f24_tnch_127_small_body_frac_252(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Annual fraction of small-body bars."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    return (br < 0.25).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(br.notna(), np.nan)


def f24_tnch_128_small_body_high_vol_count_63(high: pd.Series, low: pd.Series, open_: pd.Series,
                                                 close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 63 bars with body/range < 0.25 AND vol > 1.5x 21d avg — churn-bar count."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((br < 0.25) & (volume > 1.5 * v_avg)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().where(br.notna() & v_avg.notna(), np.nan)


def f24_tnch_129_small_body_high_vol_count_252(high: pd.Series, low: pd.Series, open_: pd.Series,
                                                  close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of small-body high-vol churn bars."""
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = ((br < 0.25) & (volume > 1.5 * v_avg)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().where(br.notna() & v_avg.notna(), np.nan)


def f24_tnch_130_doji_count_63(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Count of doji bars (|C - O| < 0.05 * range) in past 63 — indecision-bar dwell."""
    rng = (high - low).replace(0, np.nan)
    is_doji = ((close - open_).abs() < 0.05 * rng).astype(float)
    return is_doji.rolling(QDAYS, min_periods=MDAYS).sum().where(rng.notna(), np.nan)


def f24_tnch_131_doji_count_252(high: pd.Series, low: pd.Series, open_: pd.Series, close: pd.Series) -> pd.Series:
    """Annual doji count."""
    rng = (high - low).replace(0, np.nan)
    is_doji = ((close - open_).abs() < 0.05 * rng).astype(float)
    return is_doji.rolling(YDAYS, min_periods=QDAYS).sum().where(rng.notna(), np.nan)


# ============================================================
# Bucket O — Range trend & contraction (132-140)
# ============================================================

def f24_tnch_132_tr_slope_21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d rolling slope of TR — short-term range trend."""
    return _rolling_slope(_true_range(high, low, close), MDAYS)


def f24_tnch_133_tr_slope_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d rolling slope of TR — quarterly range trend."""
    return _rolling_slope(_true_range(high, low, close), QDAYS)


def f24_tnch_134_tr_slope_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d rolling slope of TR — annual range trend."""
    return _rolling_slope(_true_range(high, low, close), YDAYS)


def f24_tnch_135_bars_since_last_nr4(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent NR4 (today's range smallest of past 4)."""
    r = high - low
    rm = r.rolling(4, min_periods=4).min()
    return _bars_since_true(r == rm)


def f24_tnch_136_range_contraction_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive run of TR < prior TR (range-contraction streak)."""
    r = high - low
    return _streak_true(r < r.shift(1))


def f24_tnch_137_longest_contraction_streak_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """Longest TR-contraction streak in past 63 bars."""
    r = high - low
    streak = _streak_true(r < r.shift(1))
    return streak.rolling(QDAYS, min_periods=MDAYS).max().where(r.notna(), np.nan)


def f24_tnch_138_range_squeeze_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if 21d std(HL range) < 20th-pct of trailing-252d std(HL range) — range squeeze regime."""
    r = high - low
    s21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    q20 = s21.rolling(YDAYS, min_periods=QDAYS).quantile(0.2)
    return (s21 < q20).astype(float).where(q20.notna(), np.nan)


def f24_tnch_139_range_squeeze_count_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of past 63 bars in range-squeeze regime."""
    r = high - low
    s21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    q20 = s21.rolling(YDAYS, min_periods=QDAYS).quantile(0.2)
    return (s21 < q20).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(q20.notna(), np.nan)


def f24_tnch_140_range_squeeze_count_252(high: pd.Series, low: pd.Series) -> pd.Series:
    """Annual count of range-squeeze bars."""
    r = high - low
    s21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    q20 = s21.rolling(YDAYS, min_periods=QDAYS).quantile(0.2)
    return (s21 < q20).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(q20.notna(), np.nan)


# ============================================================
# Bucket P — Composite churn / saturation indicators (141-150)
# ============================================================

def f24_tnch_141_churn_score_mean_21(high: pd.Series, low: pd.Series, open_: pd.Series,
                                       close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (vol-zscore-21) * (1 - body/range) past 21 — monthly churn score."""
    vz = _rolling_zscore(volume, MDAYS, min_periods=WDAYS)
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    s = vz * (1.0 - br)
    return s.rolling(MDAYS, min_periods=WDAYS).mean()


def f24_tnch_142_churn_score_mean_63(high: pd.Series, low: pd.Series, open_: pd.Series,
                                       close: pd.Series, volume: pd.Series) -> pd.Series:
    """Quarterly mean churn score."""
    vz = _rolling_zscore(volume, MDAYS, min_periods=WDAYS)
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    s = vz * (1.0 - br)
    return s.rolling(QDAYS, min_periods=MDAYS).mean()


def f24_tnch_143_churn_score_mean_252(high: pd.Series, low: pd.Series, open_: pd.Series,
                                        close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual mean churn score."""
    vz = _rolling_zscore(volume, MDAYS, min_periods=WDAYS)
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    s = vz * (1.0 - br)
    return s.rolling(YDAYS, min_periods=QDAYS).mean()


def f24_tnch_144_dollar_vol_zscore_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar-volume vs trailing 21d — short-horizon dollar-turnover anomaly."""
    return _rolling_zscore(close * volume, MDAYS, min_periods=WDAYS)


def f24_tnch_145_dollar_vol_zscore_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar-volume vs trailing 63d."""
    return _rolling_zscore(close * volume, QDAYS, min_periods=MDAYS)


def f24_tnch_146_net_vol_slope_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d rolling slope of cumulative (sign(ret) * vol) — net-volume trend direction."""
    sgn = np.sign(close.diff()).fillna(0.0)
    cum = (sgn * volume).cumsum()
    return _rolling_slope(cum, QDAYS)


def f24_tnch_147_turnover_price_divergence_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of (vol-slope-63) - sign of (price-slope-63) — disagreement signal."""
    vs = _rolling_slope(volume, QDAYS)
    ps = _rolling_slope(close, QDAYS)
    return np.sign(vs) - np.sign(ps)


def f24_tnch_148_exhaustion_composite_flag(high: pd.Series, low: pd.Series, open_: pd.Series,
                                              close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if climax + wide-range + small body coincide — multi-condition exhaustion signature."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    flag = (r > 2.0) & (vr > 2.0) & (br < 0.3)
    return flag.astype(float).where(r.notna() & vr.notna() & rng.notna(), np.nan)


def f24_tnch_149_exhaustion_composite_count_63(high: pd.Series, low: pd.Series, open_: pd.Series,
                                                  close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of exhaustion-composite bars in past 63."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    rng = (high - low).replace(0, np.nan)
    br = (close - open_).abs() / rng
    flag = ((r > 2.0) & (vr > 2.0) & (br < 0.3)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().where(r.notna() & vr.notna() & rng.notna(), np.nan)


def f24_tnch_150_saturation_index_63(high: pd.Series, low: pd.Series, open_: pd.Series,
                                       close: pd.Series, volume: pd.Series) -> pd.Series:
    """Saturation = (wide-range frac + churn-bar frac + climax frac) past 63 — composite intensity."""
    r = _safe_div(_true_range(high, low, close), _atr(high, low, close, MDAYS))
    vr = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    ar = close.pct_change().abs()
    ar_avg = ar.rolling(MDAYS, min_periods=WDAYS).mean()
    wide = (r > 2.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    churn = ((ar < 0.5 * ar_avg) & (volume > 1.5 * volume.rolling(MDAYS, min_periods=WDAYS).mean())).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    clim = ((r > 2.0) & (vr > 2.0)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return (wide + churn + clim).where(r.notna() & vr.notna() & ar_avg.notna(), np.nan)


# ============================================================
#                         REGISTRY 076-150
# ============================================================

_HLCV = ["high", "low", "close", "volume"]
_HLC = ["high", "low", "close"]
_HL = ["high", "low"]
_CV = ["close", "volume"]
_OHLC = ["open", "high", "low", "close"]
_OHLCV = ["open", "high", "low", "close", "volume"]

TURNOVER_AND_CHURN_BASE_REGISTRY_076_150 = {
    "f24_tnch_076_tr_over_mean_tr_21": {"inputs": _HLC, "func": f24_tnch_076_tr_over_mean_tr_21},
    "f24_tnch_077_tr_over_mean_tr_63": {"inputs": _HLC, "func": f24_tnch_077_tr_over_mean_tr_63},
    "f24_tnch_078_tr_over_std_tr_63": {"inputs": _HLC, "func": f24_tnch_078_tr_over_std_tr_63},
    "f24_tnch_079_atr21_over_atr63": {"inputs": _HLC, "func": f24_tnch_079_atr21_over_atr63},
    "f24_tnch_080_atr21_over_atr252": {"inputs": _HLC, "func": f24_tnch_080_atr21_over_atr252},
    "f24_tnch_081_atr63_over_atr252": {"inputs": _HLC, "func": f24_tnch_081_atr63_over_atr252},
    "f24_tnch_082_atr21_zscore_252": {"inputs": _HLC, "func": f24_tnch_082_atr21_zscore_252},
    "f24_tnch_083_atr_pct_rank_252": {"inputs": _HLC, "func": f24_tnch_083_atr_pct_rank_252},
    "f24_tnch_084_atr_above_252d_median_frac_63": {"inputs": _HLC, "func": f24_tnch_084_atr_above_252d_median_frac_63},
    "f24_tnch_085_atr_expansion_event_flag": {"inputs": _HLC, "func": f24_tnch_085_atr_expansion_event_flag},
    "f24_tnch_086_vol_cv_21": {"inputs": ["volume"], "func": f24_tnch_086_vol_cv_21},
    "f24_tnch_087_vol_cv_63": {"inputs": ["volume"], "func": f24_tnch_087_vol_cv_63},
    "f24_tnch_088_vol_cv_252": {"inputs": ["volume"], "func": f24_tnch_088_vol_cv_252},
    "f24_tnch_089_vol_top5_share_63": {"inputs": ["volume"], "func": f24_tnch_089_vol_top5_share_63},
    "f24_tnch_090_vol_top5_share_252": {"inputs": ["volume"], "func": f24_tnch_090_vol_top5_share_252},
    "f24_tnch_091_vol_entropy_63": {"inputs": ["volume"], "func": f24_tnch_091_vol_entropy_63},
    "f24_tnch_092_vol_skew_63": {"inputs": ["volume"], "func": f24_tnch_092_vol_skew_63},
    "f24_tnch_093_vol_skew_252": {"inputs": ["volume"], "func": f24_tnch_093_vol_skew_252},
    "f24_tnch_094_vol_kurt_252": {"inputs": ["volume"], "func": f24_tnch_094_vol_kurt_252},
    "f24_tnch_095_abs_ret_volume_corr_21": {"inputs": _CV, "func": f24_tnch_095_abs_ret_volume_corr_21},
    "f24_tnch_096_abs_ret_volume_corr_63": {"inputs": _CV, "func": f24_tnch_096_abs_ret_volume_corr_63},
    "f24_tnch_097_abs_ret_volume_corr_252": {"inputs": _CV, "func": f24_tnch_097_abs_ret_volume_corr_252},
    "f24_tnch_098_ret_volume_corr_21": {"inputs": _CV, "func": f24_tnch_098_ret_volume_corr_21},
    "f24_tnch_099_ret_volume_corr_63": {"inputs": _CV, "func": f24_tnch_099_ret_volume_corr_63},
    "f24_tnch_100_retstd_over_meanvol_21": {"inputs": _CV, "func": f24_tnch_100_retstd_over_meanvol_21},
    "f24_tnch_101_retstd_over_meanvol_63": {"inputs": _CV, "func": f24_tnch_101_retstd_over_meanvol_63},
    "f24_tnch_102_abs_ret_per_volume_63": {"inputs": _CV, "func": f24_tnch_102_abs_ret_per_volume_63},
    "f24_tnch_103_abs_ret_per_volume_252": {"inputs": _CV, "func": f24_tnch_103_abs_ret_per_volume_252},
    "f24_tnch_104_max_vol_over_mean_63": {"inputs": ["volume"], "func": f24_tnch_104_max_vol_over_mean_63},
    "f24_tnch_105_max_vol_over_mean_252": {"inputs": ["volume"], "func": f24_tnch_105_max_vol_over_mean_252},
    "f24_tnch_106_bars_since_63d_max_vol": {"inputs": ["volume"], "func": f24_tnch_106_bars_since_63d_max_vol},
    "f24_tnch_107_bars_since_252d_max_vol": {"inputs": ["volume"], "func": f24_tnch_107_bars_since_252d_max_vol},
    "f24_tnch_108_bars_since_504d_max_vol": {"inputs": ["volume"], "func": f24_tnch_108_bars_since_504d_max_vol},
    "f24_tnch_109_vol_spike_count_63": {"inputs": ["volume"], "func": f24_tnch_109_vol_spike_count_63},
    "f24_tnch_110_vol_spike_count_252": {"inputs": ["volume"], "func": f24_tnch_110_vol_spike_count_252},
    "f24_tnch_111_vol_spike_cluster_flag": {"inputs": ["volume"], "func": f24_tnch_111_vol_spike_cluster_flag},
    "f24_tnch_112_vol_spike_cluster_count_63": {"inputs": ["volume"], "func": f24_tnch_112_vol_spike_cluster_count_63},
    "f24_tnch_113_climax_pressure_flag": {"inputs": _HLCV, "func": f24_tnch_113_climax_pressure_flag},
    "f24_tnch_114_climax_pressure_count_21": {"inputs": _HLCV, "func": f24_tnch_114_climax_pressure_count_21},
    "f24_tnch_115_climax_pressure_count_63": {"inputs": _HLCV, "func": f24_tnch_115_climax_pressure_count_63},
    "f24_tnch_116_climax_pressure_count_252": {"inputs": _HLCV, "func": f24_tnch_116_climax_pressure_count_252},
    "f24_tnch_117_bars_since_last_climax": {"inputs": _HLCV, "func": f24_tnch_117_bars_since_last_climax},
    "f24_tnch_118_silent_rally_flag": {"inputs": _CV, "func": f24_tnch_118_silent_rally_flag},
    "f24_tnch_119_silent_rally_count_63": {"inputs": _CV, "func": f24_tnch_119_silent_rally_count_63},
    "f24_tnch_120_exhaustion_gap_flag": {"inputs": _OHLCV, "func": f24_tnch_120_exhaustion_gap_flag},
    "f24_tnch_121_exhaustion_gap_count_252": {"inputs": _OHLCV, "func": f24_tnch_121_exhaustion_gap_count_252},
    "f24_tnch_122_bars_since_last_exhaustion_gap": {"inputs": _OHLCV, "func": f24_tnch_122_bars_since_last_exhaustion_gap},
    "f24_tnch_123_body_over_range_mean_21": {"inputs": _OHLC, "func": f24_tnch_123_body_over_range_mean_21},
    "f24_tnch_124_body_over_range_mean_63": {"inputs": _OHLC, "func": f24_tnch_124_body_over_range_mean_63},
    "f24_tnch_125_body_over_range_mean_252": {"inputs": _OHLC, "func": f24_tnch_125_body_over_range_mean_252},
    "f24_tnch_126_small_body_frac_63": {"inputs": _OHLC, "func": f24_tnch_126_small_body_frac_63},
    "f24_tnch_127_small_body_frac_252": {"inputs": _OHLC, "func": f24_tnch_127_small_body_frac_252},
    "f24_tnch_128_small_body_high_vol_count_63": {"inputs": _OHLCV, "func": f24_tnch_128_small_body_high_vol_count_63},
    "f24_tnch_129_small_body_high_vol_count_252": {"inputs": _OHLCV, "func": f24_tnch_129_small_body_high_vol_count_252},
    "f24_tnch_130_doji_count_63": {"inputs": _OHLC, "func": f24_tnch_130_doji_count_63},
    "f24_tnch_131_doji_count_252": {"inputs": _OHLC, "func": f24_tnch_131_doji_count_252},
    "f24_tnch_132_tr_slope_21": {"inputs": _HLC, "func": f24_tnch_132_tr_slope_21},
    "f24_tnch_133_tr_slope_63": {"inputs": _HLC, "func": f24_tnch_133_tr_slope_63},
    "f24_tnch_134_tr_slope_252": {"inputs": _HLC, "func": f24_tnch_134_tr_slope_252},
    "f24_tnch_135_bars_since_last_nr4": {"inputs": _HL, "func": f24_tnch_135_bars_since_last_nr4},
    "f24_tnch_136_range_contraction_streak": {"inputs": _HL, "func": f24_tnch_136_range_contraction_streak},
    "f24_tnch_137_longest_contraction_streak_63": {"inputs": _HL, "func": f24_tnch_137_longest_contraction_streak_63},
    "f24_tnch_138_range_squeeze_flag": {"inputs": _HL, "func": f24_tnch_138_range_squeeze_flag},
    "f24_tnch_139_range_squeeze_count_63": {"inputs": _HL, "func": f24_tnch_139_range_squeeze_count_63},
    "f24_tnch_140_range_squeeze_count_252": {"inputs": _HL, "func": f24_tnch_140_range_squeeze_count_252},
    "f24_tnch_141_churn_score_mean_21": {"inputs": _OHLCV, "func": f24_tnch_141_churn_score_mean_21},
    "f24_tnch_142_churn_score_mean_63": {"inputs": _OHLCV, "func": f24_tnch_142_churn_score_mean_63},
    "f24_tnch_143_churn_score_mean_252": {"inputs": _OHLCV, "func": f24_tnch_143_churn_score_mean_252},
    "f24_tnch_144_dollar_vol_zscore_21": {"inputs": _CV, "func": f24_tnch_144_dollar_vol_zscore_21},
    "f24_tnch_145_dollar_vol_zscore_63": {"inputs": _CV, "func": f24_tnch_145_dollar_vol_zscore_63},
    "f24_tnch_146_net_vol_slope_63": {"inputs": _CV, "func": f24_tnch_146_net_vol_slope_63},
    "f24_tnch_147_turnover_price_divergence_63": {"inputs": _CV, "func": f24_tnch_147_turnover_price_divergence_63},
    "f24_tnch_148_exhaustion_composite_flag": {"inputs": _OHLCV, "func": f24_tnch_148_exhaustion_composite_flag},
    "f24_tnch_149_exhaustion_composite_count_63": {"inputs": _OHLCV, "func": f24_tnch_149_exhaustion_composite_count_63},
    "f24_tnch_150_saturation_index_63": {"inputs": _OHLCV, "func": f24_tnch_150_saturation_index_63},
}
