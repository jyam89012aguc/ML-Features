"""dollar_volume_intensity base features 376-450 — Pipeline 1b-technical (extension #3 cont.).

ML-focused: concentration cuts, time-spent metrics, cluster-decay shape, mean
reversion, liquidity-event patterns, multi-frame agreement, final composites.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
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


def _consecutive_true_streak(b):
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _dollar_vol(close, volume):
    return (close * volume).astype(float)


# Bucket BG — Concentration cuts (376-390)

def f21_dvit_376_dv_share_top_3_days_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of top-3 dv days / total dv in trailing 252d."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30 or v.sum() <= 0:
            return np.nan
        return float(np.sort(v)[-3:].sum() / v.sum())
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_377_dv_share_top_2_days_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of top-2 dv days / total dv, trailing 252d."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30 or v.sum() <= 0:
            return np.nan
        return float(np.sort(v)[-2:].sum() / v.sum())
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_378_dv_share_top_1_day_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Single largest dv day / total dv, trailing 252d — extreme concentration share."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30 or v.sum() <= 0:
            return np.nan
        return float(v.max() / v.sum())
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_379_dv_share_top_3_days_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of top-3 dv days / total dv, trailing 63d."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20 or v.sum() <= 0:
            return np.nan
        return float(np.sort(v)[-3:].sum() / v.sum())
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_f, raw=True)


def f21_dvit_380_dv_smallest_top_3_in_252d_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Min of trailing-252d top-3 dv days — lowest of the big-3 days (capacity floor)."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        return float(np.sort(v)[-3:].min())
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_381_dv_top_decile_concentration_252_vs_5y(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(top decile dv share 252d) − (top decile dv share 5y) — concentration shift vs longer baseline."""
    dv = _dollar_vol(close, volume)
    def _share(w):
        v = w[~np.isnan(w)]
        if v.size < 30 or v.sum() <= 0:
            return np.nan
        thr = np.quantile(v, 0.90)
        return float(v[v >= thr].sum() / v.sum())
    s252 = dv.rolling(YDAYS, min_periods=QDAYS).apply(_share, raw=True)
    s5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_share, raw=True)
    return s252 - s5y


def f21_dvit_382_dv_iqr_to_median_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(q75 − q25) / q50 of trailing 252d dv — dispersion relative to typical."""
    dv = _dollar_vol(close, volume)
    iqr = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(iqr, med)


def f21_dvit_383_dv_max_to_median_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max(dv,252d) / median(dv,252d) — single-event-vs-typical ratio."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(YDAYS, min_periods=QDAYS).max(), dv.rolling(YDAYS, min_periods=QDAYS).median())


def f21_dvit_384_dv_max_to_q90_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max(dv,252d) / q90(dv,252d) — extreme outlier indicator vs typical-high."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(YDAYS, min_periods=QDAYS).max(), dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.90))


def f21_dvit_385_dv_q95_to_q75_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """q95(dv,252d) / q75(dv,252d) — upper-tail steepness."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.95), dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75))


def f21_dvit_386_dv_q05_to_q25_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """q05(dv,252d) / q25(dv,252d) — lower-tail compression."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.05), dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25))


def f21_dvit_387_dv_iqr_to_iqr_5y_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(IQR dv 252d) / (IQR dv 5y) — recent dispersion vs long baseline."""
    dv = _dollar_vol(close, volume)
    iqr252 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    iqr5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75) - dv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    return _safe_div(iqr252, iqr5y)


def f21_dvit_388_dv_max_to_max_5y_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """max(dv, 252d) / max(dv, 5y) — recent peak vs all-time peak."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(YDAYS, min_periods=QDAYS).max(), dv.rolling(DDAYS_5Y, min_periods=YDAYS).max())


def f21_dvit_389_dv_count_above_5y_max_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where dv > 5y trailing max (capacity exceeds all history)."""
    dv = _dollar_vol(close, volume)
    rmax5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (dv >= rmax5y).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_390_dv_count_below_5y_min_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where dv ≤ 5y trailing min."""
    dv = _dollar_vol(close, volume)
    rmin5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    return (dv <= rmin5y).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# Bucket BH — Time-spent metrics (391-400)

def f21_dvit_391_dv_time_in_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv >= q90."""
    dv = _dollar_vol(close, volume)
    q90 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (dv >= q90).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_392_dv_time_in_top_quartile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv >= q75."""
    dv = _dollar_vol(close, volume)
    q75 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (dv >= q75).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_393_dv_time_in_bottom_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv <= q10."""
    dv = _dollar_vol(close, volume)
    q10 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return (dv <= q10).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_394_dv_time_in_bottom_quartile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv <= q25."""
    dv = _dollar_vol(close, volume)
    q25 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (dv <= q25).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_395_dv_time_above_5y_mean_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with dv > 5y mean."""
    dv = _dollar_vol(close, volume)
    m5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return (dv > m5y).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_396_dv_time_above_252d_mean_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with dv > 252d mean."""
    dv = _dollar_vol(close, volume)
    m252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return (dv > m252).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_397_dv_time_below_252d_mean_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with dv < 252d mean."""
    dv = _dollar_vol(close, volume)
    m252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return (dv < m252).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_398_dv_time_above_5y_mean_in_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars with dv > 5y mean."""
    dv = _dollar_vol(close, volume)
    m5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    return (dv > m5y).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_399_dv_time_above_q95_in_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of bars with dv > 252d q95."""
    dv = _dollar_vol(close, volume)
    q95 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return (dv > q95).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f21_dvit_400_dv_time_below_q05_in_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of bars with dv < 252d q05."""
    dv = _dollar_vol(close, volume)
    q05 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    return (dv < q05).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


# Bucket BI — Cluster decay shape (401-410)

def f21_dvit_401_dv_decay_steepness_after_252d_peak_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """If the 252d-trailing dv-peak was within last 5d, (current dv) / (peak dv) - 1."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        if (len(w) - 1 - peak_idx) > 5:
            return np.nan
        peak = w[peak_idx]; cur = w[-1]
        if not np.isfinite(peak) or peak <= 0 or not np.isfinite(cur):
            return np.nan
        return float(cur / peak - 1.0)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_402_dv_decay_steepness_after_252d_peak_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """If 252d-trailing dv-peak was within last 21d, (current dv) / (peak dv) - 1."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        if (len(w) - 1 - peak_idx) > MDAYS:
            return np.nan
        peak = w[peak_idx]; cur = w[-1]
        if not np.isfinite(peak) or peak <= 0 or not np.isfinite(cur):
            return np.nan
        return float(cur / peak - 1.0)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_403_dv_decay_steepness_after_252d_peak_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """If 252d-trailing dv-peak was within last 63d, (current dv) / (peak dv) - 1."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        if (len(w) - 1 - peak_idx) > QDAYS:
            return np.nan
        peak = w[peak_idx]; cur = w[-1]
        if not np.isfinite(peak) or peak <= 0 or not np.isfinite(cur):
            return np.nan
        return float(cur / peak - 1.0)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_404_dv_recovery_velocity_after_252d_trough_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """If 252d-trailing dv-trough was within last 5d, (current dv) / (trough dv) - 1."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        trough_idx = int(np.argmin(w))
        if (len(w) - 1 - trough_idx) > 5:
            return np.nan
        trough = w[trough_idx]; cur = w[-1]
        if not np.isfinite(trough) or trough <= 0 or not np.isfinite(cur):
            return np.nan
        return float(cur / trough - 1.0)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_405_dv_recovery_velocity_after_252d_trough_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """If 252d-trailing dv-trough was within last 21d, (current dv) / (trough dv) - 1."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        trough_idx = int(np.argmin(w))
        if (len(w) - 1 - trough_idx) > MDAYS:
            return np.nan
        trough = w[trough_idx]; cur = w[-1]
        if not np.isfinite(trough) or trough <= 0 or not np.isfinite(cur):
            return np.nan
        return float(cur / trough - 1.0)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_406_dv_after_peak_drop_to_50pct_age(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from peak to first bar with dv ≤ 0.5 × peak, within trailing 252d window."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        thresh = peak * 0.5
        for j in range(peak_idx + 1, len(w)):
            if not np.isnan(w[j]) and w[j] <= thresh:
                return float(j - peak_idx)
        return float(len(w) - peak_idx)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_407_dv_after_peak_drop_to_25pct_age(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from peak to first bar with dv ≤ 0.25 × peak, within trailing 252d window."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        thresh = peak * 0.25
        for j in range(peak_idx + 1, len(w)):
            if not np.isnan(w[j]) and w[j] <= thresh:
                return float(j - peak_idx)
        return float(len(w) - peak_idx)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_408_dv_after_peak_drop_to_10pct_age(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars from peak to first bar with dv ≤ 0.10 × peak, within trailing 252d."""
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        peak = w[peak_idx]
        if not np.isfinite(peak) or peak <= 0:
            return np.nan
        thresh = peak * 0.10
        for j in range(peak_idx + 1, len(w)):
            if not np.isnan(w[j]) and w[j] <= thresh:
                return float(j - peak_idx)
        return float(len(w) - peak_idx)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_409_dv_volatility_change_around_peak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(std log_dv 21d before peak) − (std log_dv 21d after peak), assuming peak in window."""
    ldv = _safe_log(_dollar_vol(close, volume))
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        peak_idx = int(np.argmax(w))
        before = w[max(0, peak_idx - MDAYS): peak_idx]
        after = w[peak_idx + 1: peak_idx + 1 + MDAYS]
        b = before[~np.isnan(before)]
        a = after[~np.isnan(after)]
        if b.size < 5 or a.size < 5:
            return np.nan
        return float(b.std() - a.std())
    return ldv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_410_dv_decay_linear_vs_exp_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if post-peak decay is more linear (R² of linear fit on log_dv since peak < R² of exponential)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 50:
            return np.nan
        peak_idx = int(np.argmax(w))
        seg = w[peak_idx + 1:]
        seg = seg[~np.isnan(seg)]
        if seg.size < 10:
            return np.nan
        x = np.arange(seg.size, dtype=float)
        # linear fit on seg
        xm = x.mean(); ym = seg.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx <= 0:
            return np.nan
        b = ((x - xm) * (seg - ym)).sum() / sxx
        a = ym - b * xm
        pred_lin = a + b * x
        ss_res_lin = ((seg - pred_lin) ** 2).sum()
        ss_tot = ((seg - ym) ** 2).sum()
        if ss_tot <= 0:
            return np.nan
        r2_lin = 1.0 - ss_res_lin / ss_tot
        # exponential fit: fit log(seg) which is already log_dv... so it's effectively the same. Use seg as-is.
        # As proxy: just compare slope magnitude regimes
        return 1.0 if r2_lin > 0.7 else 0.0
    return ldv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


# Bucket BJ — Mean reversion / extreme reversal (411-420)

def f21_dvit_411_dv_extreme_5sigma_then_reversion_within_3d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 5-sigma dv burst occurred 1-3 bars ago AND today's dv z(252d) < 0."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst_recent = (z.shift(1).rolling(3, min_periods=1).max() > 5.0)
    return (burst_recent & (z < 0)).astype(float)


def f21_dvit_412_dv_extreme_5sigma_then_reversion_within_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 5-sigma dv burst 1-5 bars ago AND today's dv z(252d) < 0."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst_recent = (z.shift(1).rolling(WDAYS, min_periods=1).max() > 5.0)
    return (burst_recent & (z < 0)).astype(float)


def f21_dvit_413_dv_extreme_5sigma_then_continuation_within_3d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 5-sigma dv burst occurred 1-3 bars ago AND today's dv z(252d) > 3 (continuation)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst_recent = (z.shift(1).rolling(3, min_periods=1).max() > 5.0)
    return (burst_recent & (z > 3.0)).astype(float)


def f21_dvit_414_dv_extreme_high_followed_close_lower_5d_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (5d-ago dv z>3) AND (today close < 5d-ago close)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst_5d_ago = z.shift(5) > 3.0
    close_lower = close < close.shift(5)
    return (burst_5d_ago & close_lower).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_415_dv_extreme_high_followed_close_higher_5d_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (5d-ago dv z>3) AND (today close > 5d-ago close)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst_5d_ago = z.shift(5) > 3.0
    close_higher = close > close.shift(5)
    return (burst_5d_ago & close_higher).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_416_dv_capacity_breakdown_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's dv > the trailing 504d rolling max of all prior dv (capacity break)."""
    dv = _dollar_vol(close, volume)
    rmax504 = dv.rolling(DDAYS_2Y, min_periods=YDAYS).max().shift(1)
    return (dv > rmax504).astype(float)


def f21_dvit_417_dv_capacity_at_alltime_high_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's dv ≥ expanding(min_periods=252) max."""
    dv = _dollar_vol(close, volume)
    rmax = dv.expanding(min_periods=YDAYS).max()
    return (dv >= rmax).astype(float)


def f21_dvit_418_dv_capacity_step_change_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when trailing 21d mean dv > 2 × prior 21d mean dv (capacity step up)."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return (m21 > 2.0 * m21.shift(MDAYS)).astype(float)


def f21_dvit_419_dv_capacity_decay_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when trailing 21d mean dv < 0.5 × prior 21d mean dv (capacity step down)."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return (m21 < 0.5 * m21.shift(MDAYS)).astype(float)


def f21_dvit_420_dv_regime_volatility_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of capacity-step-change events (up or down)."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    step_up = (m21 > 2.0 * m21.shift(MDAYS))
    step_dn = (m21 < 0.5 * m21.shift(MDAYS))
    return (step_up | step_dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# Bucket BK — Liquidity-event patterns (421-430)

def f21_dvit_421_dv_freezing_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's dv = trailing 252d minimum dv."""
    dv = _dollar_vol(close, volume)
    return (dv <= dv.rolling(YDAYS, min_periods=QDAYS).min()).astype(float)


def f21_dvit_422_dv_freezing_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of dv-freezing events."""
    dv = _dollar_vol(close, volume)
    return (dv <= dv.rolling(YDAYS, min_periods=QDAYS).min()).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_423_dv_skewed_burst_positive_return_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 3-sigma dv burst AND close return today > 2%."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((z > 3.0) & (close.pct_change() > 0.02)).astype(float)


def f21_dvit_424_dv_skewed_burst_negative_return_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 3-sigma dv burst AND close return today < -2%."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((z > 3.0) & (close.pct_change() < -0.02)).astype(float)


def f21_dvit_425_dv_balanced_burst_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 3-sigma dv burst AND |close return today| < 1%."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((z > 3.0) & (close.pct_change().abs() < 0.01)).astype(float)


def f21_dvit_426_dv_negative_burst_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of (3-sigma dv burst AND close return < -2%)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((z > 3.0) & (close.pct_change() < -0.02)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_427_dv_positive_burst_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of (3-sigma dv burst AND close return > 2%)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((z > 3.0) & (close.pct_change() > 0.02)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_428_dv_silent_burst_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of (3-sigma dv burst AND |return| < 0.5%) — silent burst (likely block-trade)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((z > 3.0) & (close.pct_change().abs() < 0.005)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_429_dv_indecision_burst_signature(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 3-sigma dv burst AND |close - open|/open < 0.1% (indecision burst)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    indecision = (close - open).abs() / open < 0.001
    return ((z > 3.0) & indecision).astype(float)


def f21_dvit_430_dv_block_trade_signature(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's dv > 5 × trailing 5d max dv (unusual single-day extreme — block-trade-like)."""
    dv = _dollar_vol(close, volume)
    rmax5d = dv.rolling(WDAYS, min_periods=2).max().shift(1)
    return (dv > 5.0 * rmax5d).astype(float)


# Bucket BL — Multi-frame agreement (431-440)

def f21_dvit_431_dv_extreme_alignment_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol z>2 at horizons 21d AND 63d AND 252d simultaneously."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ((_rolling_zscore(ldv, MDAYS) > 2.0) & (_rolling_zscore(ldv, QDAYS) > 2.0) & (_rolling_zscore(ldv, YDAYS) > 2.0)).astype(float)


def f21_dvit_432_dv_extreme_disagreement_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol z(21d) > 2 BUT z(252d) < 0 (short-term spike but long-term low)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ((_rolling_zscore(ldv, MDAYS) > 2.0) & (_rolling_zscore(ldv, YDAYS) < 0.0)).astype(float)


def f21_dvit_433_dv_top_decile_multi_horizon_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when dv is in top decile at horizons 21d, 63d, 252d simultaneously."""
    dv = _dollar_vol(close, volume)
    q21 = dv.rolling(MDAYS, min_periods=WDAYS).quantile(0.90)
    q63 = dv.rolling(QDAYS, min_periods=MDAYS).quantile(0.90)
    q252 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((dv >= q21) & (dv >= q63) & (dv >= q252)).astype(float)


def f21_dvit_434_dv_bottom_decile_multi_horizon_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when dv in bottom decile at 21d, 63d, 252d simultaneously."""
    dv = _dollar_vol(close, volume)
    q21 = dv.rolling(MDAYS, min_periods=WDAYS).quantile(0.10)
    q63 = dv.rolling(QDAYS, min_periods=MDAYS).quantile(0.10)
    q252 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return ((dv <= q21) & (dv <= q63) & (dv <= q252)).astype(float)


def f21_dvit_435_dv_pct_rank_diff_5d_vs_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (pct rank dv 5d − pct rank dv 63d)."""
    dv = _dollar_vol(close, volume)
    pr5 = dv.rolling(WDAYS, min_periods=2).rank(pct=True)
    pr63 = dv.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)
    return _rolling_zscore(pr5 - pr63, YDAYS)


def f21_dvit_436_dv_pct_rank_diff_21d_vs_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (pct rank dv 21d − pct rank dv 63d)."""
    dv = _dollar_vol(close, volume)
    pr21 = dv.rolling(MDAYS, min_periods=WDAYS).rank(pct=True)
    pr63 = dv.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)
    return _rolling_zscore(pr21 - pr63, YDAYS)


def f21_dvit_437_dv_horizon_disagreement_dispersion_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std across (pct_rank dv at 21, 63, 252 horizons) per bar."""
    dv = _dollar_vol(close, volume)
    pr21 = dv.rolling(MDAYS, min_periods=WDAYS).rank(pct=True)
    pr63 = dv.rolling(QDAYS, min_periods=MDAYS).rank(pct=True)
    pr252 = dv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return pd.concat([pr21, pr63, pr252], axis=1).std(axis=1)


def f21_dvit_438_dv_consensus_extreme_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of multi-horizon-aligned extreme z>2 events."""
    ldv = _safe_log(_dollar_vol(close, volume))
    aligned = (_rolling_zscore(ldv, MDAYS) > 2.0) & (_rolling_zscore(ldv, QDAYS) > 2.0) & (_rolling_zscore(ldv, YDAYS) > 2.0)
    return aligned.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_439_dv_z_extreme_runlength_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak with log-$-vol z(252d) > 2 in trailing 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    streak = _consecutive_true_streak(z > 2.0).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_440_dv_z_below_neg1_runlength_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak with log-$-vol z(252d) < -1 in trailing 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    streak = _consecutive_true_streak(z < -1.0).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


# Bucket BM — Final practical signals (441-450)

def f21_dvit_441_dv_dwell_at_alltime_high_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dv on bars where close ≥ expanding 5y max, divided by total trailing 252d dv."""
    rmax = close.expanding(min_periods=YDAYS).max()
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(close >= rmax, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), dv.rolling(YDAYS, min_periods=QDAYS).sum())


def f21_dvit_442_dv_silent_dwell_at_5y_high_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where close at 5y max AND dv pct rank(252d) < 0.30."""
    rmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    dv = _dollar_vol(close, volume)
    pr = dv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return ((close >= rmax5y) & (pr < 0.30)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_443_dv_outflow_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when trailing 5d sum of (sign(close.diff) × dv) < -3 × trailing 21d std of same."""
    dv = _dollar_vol(close, volume)
    sgn = np.sign(close.diff()).fillna(0.0)
    flow = sgn * dv
    sum5 = flow.rolling(WDAYS, min_periods=2).sum()
    std21 = flow.rolling(MDAYS, min_periods=WDAYS).std()
    return (sum5 < -3.0 * std21).astype(float)


def f21_dvit_444_dv_outflow_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of dv-outflow events."""
    dv = _dollar_vol(close, volume)
    sgn = np.sign(close.diff()).fillna(0.0)
    flow = sgn * dv
    sum5 = flow.rolling(WDAYS, min_periods=2).sum()
    std21 = flow.rolling(MDAYS, min_periods=WDAYS).std()
    return (sum5 < -3.0 * std21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_445_dv_outflow_streak_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-bar streak of (signed dv < 0), in trailing 252d."""
    dv = _dollar_vol(close, volume)
    sgn = np.sign(close.diff()).fillna(0.0)
    flow = sgn * dv
    streak = _consecutive_true_streak(flow < 0).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_446_dv_inflow_to_outflow_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of positive signed-dv / |sum of negative signed-dv| over trailing 63d."""
    dv = _dollar_vol(close, volume)
    sgn = np.sign(close.diff()).fillna(0.0)
    flow = sgn * dv
    pos = flow.where(flow > 0, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    neg = (-flow.where(flow < 0, 0.0)).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(pos, neg + 1.0)


def f21_dvit_447_dv_signed_burst_imbalance_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(positive-signed 3-sigma dv bursts count) − (negative-signed 3-sigma dv bursts count) in 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst = z > 3.0
    sgn = np.sign(close.pct_change()).fillna(0.0)
    pos_burst = (burst & (sgn > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg_burst = (burst & (sgn < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return pos_burst - neg_burst


def f21_dvit_448_dv_first_red_day_after_5_green_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today close < close.shift(1) AND prior 5 bars all up AND today's log-$-vol z(252d) > 1."""
    up = close > close.shift(1)
    five_up_prior = up.shift(1) & up.shift(2) & up.shift(3) & up.shift(4) & up.shift(5)
    today_red = close < close.shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (five_up_prior & today_red & (z > 1.0)).astype(float)


def f21_dvit_449_dv_first_red_day_after_5_green_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of first-red-after-5-green events with dv z>1."""
    up = close > close.shift(1)
    five_up_prior = up.shift(1) & up.shift(2) & up.shift(3) & up.shift(4) & up.shift(5)
    today_red = close < close.shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    flag = (five_up_prior & today_red & (z > 1.0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_450_dv_capacity_failure_to_recover_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where 21d-ago there was a 3-sigma burst AND current dv still < pre-burst 252d mean."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    dv = _dollar_vol(close, volume)
    burst_21_ago = z.shift(MDAYS) > 3.0
    base_pre = dv.rolling(YDAYS, min_periods=QDAYS).mean().shift(MDAYS + 1)
    return (burst_21_ago & (dv < base_pre)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                         REGISTRY 376-450
# ============================================================

DOLLAR_VOLUME_INTENSITY_BASE_REGISTRY_376_450 = {
    "f21_dvit_376_dv_share_top_3_days_in_252d": {"inputs": ["close", "volume"], "func": f21_dvit_376_dv_share_top_3_days_in_252d},
    "f21_dvit_377_dv_share_top_2_days_in_252d": {"inputs": ["close", "volume"], "func": f21_dvit_377_dv_share_top_2_days_in_252d},
    "f21_dvit_378_dv_share_top_1_day_in_252d": {"inputs": ["close", "volume"], "func": f21_dvit_378_dv_share_top_1_day_in_252d},
    "f21_dvit_379_dv_share_top_3_days_in_63d": {"inputs": ["close", "volume"], "func": f21_dvit_379_dv_share_top_3_days_in_63d},
    "f21_dvit_380_dv_smallest_top_3_in_252d_min": {"inputs": ["close", "volume"], "func": f21_dvit_380_dv_smallest_top_3_in_252d_min},
    "f21_dvit_381_dv_top_decile_concentration_252_vs_5y": {"inputs": ["close", "volume"], "func": f21_dvit_381_dv_top_decile_concentration_252_vs_5y},
    "f21_dvit_382_dv_iqr_to_median_ratio_252d": {"inputs": ["close", "volume"], "func": f21_dvit_382_dv_iqr_to_median_ratio_252d},
    "f21_dvit_383_dv_max_to_median_ratio_252d": {"inputs": ["close", "volume"], "func": f21_dvit_383_dv_max_to_median_ratio_252d},
    "f21_dvit_384_dv_max_to_q90_ratio_252d": {"inputs": ["close", "volume"], "func": f21_dvit_384_dv_max_to_q90_ratio_252d},
    "f21_dvit_385_dv_q95_to_q75_ratio_252d": {"inputs": ["close", "volume"], "func": f21_dvit_385_dv_q95_to_q75_ratio_252d},
    "f21_dvit_386_dv_q05_to_q25_ratio_252d": {"inputs": ["close", "volume"], "func": f21_dvit_386_dv_q05_to_q25_ratio_252d},
    "f21_dvit_387_dv_iqr_to_iqr_5y_ratio": {"inputs": ["close", "volume"], "func": f21_dvit_387_dv_iqr_to_iqr_5y_ratio},
    "f21_dvit_388_dv_max_to_max_5y_ratio": {"inputs": ["close", "volume"], "func": f21_dvit_388_dv_max_to_max_5y_ratio},
    "f21_dvit_389_dv_count_above_5y_max_in_252d": {"inputs": ["close", "volume"], "func": f21_dvit_389_dv_count_above_5y_max_in_252d},
    "f21_dvit_390_dv_count_below_5y_min_in_252d": {"inputs": ["close", "volume"], "func": f21_dvit_390_dv_count_below_5y_min_in_252d},
    "f21_dvit_391_dv_time_in_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_391_dv_time_in_top_decile_252d},
    "f21_dvit_392_dv_time_in_top_quartile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_392_dv_time_in_top_quartile_252d},
    "f21_dvit_393_dv_time_in_bottom_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_393_dv_time_in_bottom_decile_252d},
    "f21_dvit_394_dv_time_in_bottom_quartile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_394_dv_time_in_bottom_quartile_252d},
    "f21_dvit_395_dv_time_above_5y_mean_in_252d": {"inputs": ["close", "volume"], "func": f21_dvit_395_dv_time_above_5y_mean_in_252d},
    "f21_dvit_396_dv_time_above_252d_mean_in_63d": {"inputs": ["close", "volume"], "func": f21_dvit_396_dv_time_above_252d_mean_in_63d},
    "f21_dvit_397_dv_time_below_252d_mean_in_63d": {"inputs": ["close", "volume"], "func": f21_dvit_397_dv_time_below_252d_mean_in_63d},
    "f21_dvit_398_dv_time_above_5y_mean_in_63d": {"inputs": ["close", "volume"], "func": f21_dvit_398_dv_time_above_5y_mean_in_63d},
    "f21_dvit_399_dv_time_above_q95_in_21d": {"inputs": ["close", "volume"], "func": f21_dvit_399_dv_time_above_q95_in_21d},
    "f21_dvit_400_dv_time_below_q05_in_21d": {"inputs": ["close", "volume"], "func": f21_dvit_400_dv_time_below_q05_in_21d},
    "f21_dvit_401_dv_decay_steepness_after_252d_peak_5d": {"inputs": ["close", "volume"], "func": f21_dvit_401_dv_decay_steepness_after_252d_peak_5d},
    "f21_dvit_402_dv_decay_steepness_after_252d_peak_21d": {"inputs": ["close", "volume"], "func": f21_dvit_402_dv_decay_steepness_after_252d_peak_21d},
    "f21_dvit_403_dv_decay_steepness_after_252d_peak_63d": {"inputs": ["close", "volume"], "func": f21_dvit_403_dv_decay_steepness_after_252d_peak_63d},
    "f21_dvit_404_dv_recovery_velocity_after_252d_trough_5d": {"inputs": ["close", "volume"], "func": f21_dvit_404_dv_recovery_velocity_after_252d_trough_5d},
    "f21_dvit_405_dv_recovery_velocity_after_252d_trough_21d": {"inputs": ["close", "volume"], "func": f21_dvit_405_dv_recovery_velocity_after_252d_trough_21d},
    "f21_dvit_406_dv_after_peak_drop_to_50pct_age": {"inputs": ["close", "volume"], "func": f21_dvit_406_dv_after_peak_drop_to_50pct_age},
    "f21_dvit_407_dv_after_peak_drop_to_25pct_age": {"inputs": ["close", "volume"], "func": f21_dvit_407_dv_after_peak_drop_to_25pct_age},
    "f21_dvit_408_dv_after_peak_drop_to_10pct_age": {"inputs": ["close", "volume"], "func": f21_dvit_408_dv_after_peak_drop_to_10pct_age},
    "f21_dvit_409_dv_volatility_change_around_peak_252d": {"inputs": ["close", "volume"], "func": f21_dvit_409_dv_volatility_change_around_peak_252d},
    "f21_dvit_410_dv_decay_linear_vs_exp_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_410_dv_decay_linear_vs_exp_indicator},
    "f21_dvit_411_dv_extreme_5sigma_then_reversion_within_3d": {"inputs": ["close", "volume"], "func": f21_dvit_411_dv_extreme_5sigma_then_reversion_within_3d},
    "f21_dvit_412_dv_extreme_5sigma_then_reversion_within_5d": {"inputs": ["close", "volume"], "func": f21_dvit_412_dv_extreme_5sigma_then_reversion_within_5d},
    "f21_dvit_413_dv_extreme_5sigma_then_continuation_within_3d": {"inputs": ["close", "volume"], "func": f21_dvit_413_dv_extreme_5sigma_then_continuation_within_3d},
    "f21_dvit_414_dv_extreme_high_followed_close_lower_5d_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_414_dv_extreme_high_followed_close_lower_5d_count_252d},
    "f21_dvit_415_dv_extreme_high_followed_close_higher_5d_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_415_dv_extreme_high_followed_close_higher_5d_count_252d},
    "f21_dvit_416_dv_capacity_breakdown_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_416_dv_capacity_breakdown_indicator},
    "f21_dvit_417_dv_capacity_at_alltime_high_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_417_dv_capacity_at_alltime_high_indicator},
    "f21_dvit_418_dv_capacity_step_change_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_418_dv_capacity_step_change_indicator},
    "f21_dvit_419_dv_capacity_decay_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_419_dv_capacity_decay_indicator},
    "f21_dvit_420_dv_regime_volatility_252d": {"inputs": ["close", "volume"], "func": f21_dvit_420_dv_regime_volatility_252d},
    "f21_dvit_421_dv_freezing_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_421_dv_freezing_indicator},
    "f21_dvit_422_dv_freezing_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_422_dv_freezing_count_252d},
    "f21_dvit_423_dv_skewed_burst_positive_return_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_423_dv_skewed_burst_positive_return_indicator},
    "f21_dvit_424_dv_skewed_burst_negative_return_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_424_dv_skewed_burst_negative_return_indicator},
    "f21_dvit_425_dv_balanced_burst_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_425_dv_balanced_burst_indicator},
    "f21_dvit_426_dv_negative_burst_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_426_dv_negative_burst_count_252d},
    "f21_dvit_427_dv_positive_burst_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_427_dv_positive_burst_count_252d},
    "f21_dvit_428_dv_silent_burst_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_428_dv_silent_burst_count_252d},
    "f21_dvit_429_dv_indecision_burst_signature": {"inputs": ["open", "close", "volume"], "func": f21_dvit_429_dv_indecision_burst_signature},
    "f21_dvit_430_dv_block_trade_signature": {"inputs": ["close", "volume"], "func": f21_dvit_430_dv_block_trade_signature},
    "f21_dvit_431_dv_extreme_alignment_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_431_dv_extreme_alignment_indicator},
    "f21_dvit_432_dv_extreme_disagreement_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_432_dv_extreme_disagreement_indicator},
    "f21_dvit_433_dv_top_decile_multi_horizon_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_433_dv_top_decile_multi_horizon_indicator},
    "f21_dvit_434_dv_bottom_decile_multi_horizon_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_434_dv_bottom_decile_multi_horizon_indicator},
    "f21_dvit_435_dv_pct_rank_diff_5d_vs_63d_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_435_dv_pct_rank_diff_5d_vs_63d_zscore_252d},
    "f21_dvit_436_dv_pct_rank_diff_21d_vs_63d_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_436_dv_pct_rank_diff_21d_vs_63d_zscore_252d},
    "f21_dvit_437_dv_horizon_disagreement_dispersion_252d": {"inputs": ["close", "volume"], "func": f21_dvit_437_dv_horizon_disagreement_dispersion_252d},
    "f21_dvit_438_dv_consensus_extreme_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_438_dv_consensus_extreme_count_252d},
    "f21_dvit_439_dv_z_extreme_runlength_252d": {"inputs": ["close", "volume"], "func": f21_dvit_439_dv_z_extreme_runlength_252d},
    "f21_dvit_440_dv_z_below_neg1_runlength_252d": {"inputs": ["close", "volume"], "func": f21_dvit_440_dv_z_below_neg1_runlength_252d},
    "f21_dvit_441_dv_dwell_at_alltime_high_252d": {"inputs": ["close", "volume"], "func": f21_dvit_441_dv_dwell_at_alltime_high_252d},
    "f21_dvit_442_dv_silent_dwell_at_5y_high_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_442_dv_silent_dwell_at_5y_high_count_252d},
    "f21_dvit_443_dv_outflow_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_443_dv_outflow_indicator},
    "f21_dvit_444_dv_outflow_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_444_dv_outflow_count_252d},
    "f21_dvit_445_dv_outflow_streak_max_252d": {"inputs": ["close", "volume"], "func": f21_dvit_445_dv_outflow_streak_max_252d},
    "f21_dvit_446_dv_inflow_to_outflow_ratio_63d": {"inputs": ["close", "volume"], "func": f21_dvit_446_dv_inflow_to_outflow_ratio_63d},
    "f21_dvit_447_dv_signed_burst_imbalance_252d": {"inputs": ["close", "volume"], "func": f21_dvit_447_dv_signed_burst_imbalance_252d},
    "f21_dvit_448_dv_first_red_day_after_5_green_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_448_dv_first_red_day_after_5_green_indicator},
    "f21_dvit_449_dv_first_red_day_after_5_green_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_449_dv_first_red_day_after_5_green_count_252d},
    "f21_dvit_450_dv_capacity_failure_to_recover_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_450_dv_capacity_failure_to_recover_count_252d},
}
