"""volume_distribution_dryup base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: volume CONTRACTION / quiet topping / supply exhaustion AFTER the peak —
fade-in-volume, low-participation new highs, post-climax decay, time-since-burst,
absence-of-demand signatures. Distinct hypothesis space from vbpk (blowoff)
and dsig (distribution mechanics): vddu targets the DRY-UP itself. 150 distinct
hypotheses (continued in __base__076_150.py). PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f06_vddu_001_volume_sma5_to_sma252(volume: pd.Series) -> pd.Series:
    """SMA(5d vol) / SMA(252d vol) — short-window contraction ratio (low = dryup)."""
    a = volume.rolling(WDAYS, min_periods=2).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b)


def f06_vddu_002_volume_sma21_to_sma252(volume: pd.Series) -> pd.Series:
    """SMA(21d vol) / SMA(252d vol) — monthly contraction ratio."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b)


def f06_vddu_003_volume_sma21_to_sma63(volume: pd.Series) -> pd.Series:
    """SMA(21d vol) / SMA(63d vol) — monthly vs quarterly contraction."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a, b)


def f06_vddu_004_volume_median_5d_to_252d(volume: pd.Series) -> pd.Series:
    """Median(5d vol) / Median(252d vol) — robust short contraction."""
    a = volume.rolling(WDAYS, min_periods=2).median()
    b = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(a, b)


def f06_vddu_005_log_volume_diff_21_vs_252_means(volume: pd.Series) -> pd.Series:
    """Log( mean 21d vol / mean 252d vol ) — log-space monthly contraction."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(a) - _safe_log(b)


def f06_vddu_006_dollar_volume_sma21_to_sma252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol SMA(21d)/SMA(252d) — capital contraction."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b)


def f06_vddu_007_volume_zscore_252d(volume: pd.Series) -> pd.Series:
    """Volume z over 252d (negative when dry)."""
    return _rolling_zscore(volume, YDAYS)


def f06_vddu_008_volume_zscore_63d(volume: pd.Series) -> pd.Series:
    """Volume z over 63d."""
    return _rolling_zscore(volume, QDAYS)


def f06_vddu_009_pct_rank_mean_21d_vol_in_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of mean-21d volume within the 252d distribution of mean-21d-vol values."""
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return m21.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f06_vddu_010_pct_rank_mean_5d_vol_in_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of mean-5d volume within the 63d distribution of mean-5d-vol values."""
    m5 = volume.rolling(WDAYS, min_periods=2).mean()
    return m5.rolling(QDAYS, min_periods=MDAYS).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f06_vddu_011_log_volume_contraction_21d(volume: pd.Series) -> pd.Series:
    """Negative log-change of volume vs 21d ago — magnitude of contraction."""
    return -_safe_log(volume).diff(MDAYS)


def f06_vddu_012_log_volume_contraction_63d(volume: pd.Series) -> pd.Series:
    """Negative log-change of volume vs 63d ago."""
    return -_safe_log(volume).diff(QDAYS)


def f06_vddu_013_volume_drop_pct_vs_252d_max(volume: pd.Series) -> pd.Series:
    """1 - volume / 252d-max-volume — depth of contraction vs annual peak."""
    mx = volume.rolling(YDAYS, min_periods=QDAYS).max()
    return 1.0 - _safe_div(volume, mx)


def f06_vddu_014_volume_drop_pct_vs_63d_max(volume: pd.Series) -> pd.Series:
    """1 - volume / 63d-max-volume — depth of contraction vs quarterly peak."""
    mx = volume.rolling(QDAYS, min_periods=MDAYS).max()
    return 1.0 - _safe_div(volume, mx)


def f06_vddu_015_volume_vs_252d_75pct(volume: pd.Series) -> pd.Series:
    """Current volume / 252d 75th-pct volume — low when dry."""
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return _safe_div(volume, p)


def f06_vddu_016_volume_vs_63d_75pct(volume: pd.Series) -> pd.Series:
    """Current volume / 63d 75th-pct volume."""
    p = volume.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    return _safe_div(volume, p)


def f06_vddu_017_dollar_volume_drop_pct_vs_252d_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 - $-vol / 252d max($-vol) — capital contraction depth."""
    dv = close * volume
    mx = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return 1.0 - _safe_div(dv, mx)


def f06_vddu_018_dollar_volume_drop_pct_vs_63d_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 - $-vol / 63d max($-vol)."""
    dv = close * volume
    mx = dv.rolling(QDAYS, min_periods=MDAYS).max()
    return 1.0 - _safe_div(dv, mx)


def f06_vddu_019_log_max_vol_252d_over_mean_5d(volume: pd.Series) -> pd.Series:
    """Log( 252d max vol / mean 5d vol ) — distance from current to annual climax."""
    mx = volume.rolling(YDAYS, min_periods=QDAYS).max()
    a5 = volume.rolling(WDAYS, min_periods=2).mean()
    return _safe_log(mx) - _safe_log(a5)


def f06_vddu_020_dollar_volume_current_vs_peak_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / max($-vol over 252d) — current vs annual peak share."""
    dv = close * volume
    return _safe_div(dv, dv.rolling(YDAYS, min_periods=QDAYS).max())


def f06_vddu_021_avg_dollar_volume_contraction_21_vs_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean(21d $-vol) / Mean(63d $-vol) — capital contraction quarterly."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a, b)


def f06_vddu_022_volume_sma5_to_ema63(volume: pd.Series) -> pd.Series:
    """SMA(5d) / EMA(63d) of volume — short vs exponential baseline."""
    s5 = volume.rolling(WDAYS, min_periods=2).mean()
    e63 = volume.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return _safe_div(s5, e63)


def f06_vddu_023_ema21_to_ema252_volume(volume: pd.Series) -> pd.Series:
    """EMA(21d) / EMA(252d) of volume."""
    e21 = volume.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    e252 = volume.ewm(span=YDAYS, adjust=False, min_periods=QDAYS).mean()
    return _safe_div(e21, e252)


def f06_vddu_024_volume_proximity_to_252d_min(volume: pd.Series) -> pd.Series:
    """Volume / 252d min volume — close to 1 when fully dried up."""
    mn = volume.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(volume, mn)


def f06_vddu_025_dollar_volume_proximity_to_252d_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / 252d min $-vol."""
    dv = close * volume
    mn = dv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(dv, mn)


def f06_vddu_026_volume_slope_21d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of volume over 21d (negative when fading)."""
    return _rolling_slope(volume, MDAYS)


def f06_vddu_027_volume_slope_63d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of volume over 63d."""
    return _rolling_slope(volume, QDAYS)


def f06_vddu_028_log_volume_slope_21d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log volume over 21d — multiplicative decay."""
    return _rolling_slope(_safe_log(volume), MDAYS)


def f06_vddu_029_log_volume_slope_63d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log volume over 63d."""
    return _rolling_slope(_safe_log(volume), QDAYS)


def f06_vddu_030_dollar_volume_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of $-vol over 21d."""
    return _rolling_slope(close * volume, MDAYS)


def f06_vddu_031_dollar_volume_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of $-vol over 63d."""
    return _rolling_slope(close * volume, QDAYS)


def f06_vddu_032_volume_ema_slope_21d(volume: pd.Series) -> pd.Series:
    """Slope of EMA(21) of volume over 21d window."""
    e = volume.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    return _rolling_slope(e, MDAYS)


def f06_vddu_033_volume_slope_normalized_by_mean_21d(volume: pd.Series) -> pd.Series:
    """Volume slope over 21d / mean 21d volume — pct contraction velocity."""
    sl = _rolling_slope(volume, MDAYS)
    m = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(sl, m)


def f06_vddu_034_consecutive_declining_5d_avg_vol_streak(volume: pd.Series) -> pd.Series:
    """Length of current streak where 5d-avg volume is declining."""
    avg5 = volume.rolling(WDAYS, min_periods=2).mean()
    dec = (avg5.diff() < 0).astype(int)
    grp = (dec == 0).cumsum()
    return dec.groupby(grp).cumsum()


def f06_vddu_035_days_since_vol_1sigma(volume: pd.Series) -> pd.Series:
    """Bars since the last time volume z (252d) > 1."""
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 1.0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f06_vddu_036_days_since_vol_2sigma(volume: pd.Series) -> pd.Series:
    """Bars since the last time volume z (252d) > 2."""
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 2.0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f06_vddu_037_days_since_252d_vol_max(volume: pd.Series) -> pd.Series:
    """Bars since the 252d vol max — recency of annual climax."""
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


def f06_vddu_038_days_since_63d_vol_max(volume: pd.Series) -> pd.Series:
    """Bars since the 63d vol max."""
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)


def f06_vddu_039_declining_vol_days_count_21d(volume: pd.Series) -> pd.Series:
    """Count of bars in last 21d where vol fell from prior bar."""
    dec = (volume.diff() < 0).astype(float)
    return dec.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_040_declining_vol_days_count_63d(volume: pd.Series) -> pd.Series:
    """Count of bars in last 63d where vol fell from prior bar."""
    dec = (volume.diff() < 0).astype(float)
    return dec.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_vddu_041_log_volume_range_63d(volume: pd.Series) -> pd.Series:
    """Log(max(63d vol) / min(63d vol)) — dispersion of recent vol intensity."""
    return _safe_log(volume.rolling(QDAYS, min_periods=MDAYS).max()) - _safe_log(volume.rolling(QDAYS, min_periods=MDAYS).min())


def f06_vddu_042_volume_range_compression_21_vs_63(volume: pd.Series) -> pd.Series:
    """(max-min over 21d) / (max-min over 63d) of volume — range compression."""
    rng21 = volume.rolling(MDAYS, min_periods=WDAYS).max() - volume.rolling(MDAYS, min_periods=WDAYS).min()
    rng63 = volume.rolling(QDAYS, min_periods=MDAYS).max() - volume.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(rng21, rng63)


def f06_vddu_043_volume_cv_drop_21_vs_63(volume: pd.Series) -> pd.Series:
    """CV(21d vol) - CV(63d vol) — recent CV vs longer."""
    cv21 = volume.rolling(MDAYS, min_periods=WDAYS).std() / volume.rolling(MDAYS, min_periods=WDAYS).mean().replace(0, np.nan)
    cv63 = volume.rolling(QDAYS, min_periods=MDAYS).std() / volume.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return cv21 - cv63


def f06_vddu_044_log_volume_std_drop_21_vs_63(volume: pd.Series) -> pd.Series:
    """Std(log vol over 21d) / Std(log vol over 63d) — log-space dispersion compression."""
    lv = _safe_log(volume)
    return _safe_div(lv.rolling(MDAYS, min_periods=WDAYS).std(), lv.rolling(QDAYS, min_periods=MDAYS).std())


def f06_vddu_045_volume_exponential_decay_half_life_63d(volume: pd.Series) -> pd.Series:
    """Approximated decay half-life: -log(2) / log-volume slope over 63d (in days)."""
    sl = _rolling_slope(_safe_log(volume), QDAYS)
    return _safe_div(-np.log(2.0), sl)


def f06_vddu_046_volume_drift_to_vol_of_vol_63d(volume: pd.Series) -> pd.Series:
    """Mean(volume 63d) / Std(volume 63d) — analog to Sharpe for vol."""
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(m, sd)


def f06_vddu_047_pct_days_vol_below_half_sma252_in_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars where volume < 0.5 * SMA_252 vol."""
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume < 0.5 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_048_pct_days_vol_below_quarter_sma252_in_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars where volume < 0.25 * SMA_252 vol."""
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume < 0.25 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_049_pct_days_vol_below_25pct_252d_in_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars where volume < 25th-pct of 252d distribution."""
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (volume < p).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_050_pct_days_vol_below_25pct_252d_in_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63d bars where volume < 25th-pct of 252d distribution."""
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (volume < p).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f06_vddu_051_low_vol_up_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of up-bars in 21d where vol < 252d median — no-demand bumps."""
    up = close.diff() > 0
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (up & (volume < med)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_052_low_vol_up_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of up-bars in 63d where vol < 252d median."""
    up = close.diff() > 0
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (up & (volume < med)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_vddu_053_up_to_down_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on up bars / avg vol on down bars over 21d."""
    chg = close.diff()
    up_v = volume.where(chg > 0)
    dn_v = volume.where(chg < 0)
    return _safe_div(
        up_v.rolling(MDAYS, min_periods=WDAYS).mean(),
        dn_v.rolling(MDAYS, min_periods=WDAYS).mean(),
    )


def f06_vddu_054_up_to_down_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on up bars / avg vol on down bars over 63d."""
    chg = close.diff()
    up_v = volume.where(chg > 0)
    dn_v = volume.where(chg < 0)
    return _safe_div(
        up_v.rolling(QDAYS, min_periods=MDAYS).mean(),
        dn_v.rolling(QDAYS, min_periods=MDAYS).mean(),
    )


def f06_vddu_055_up_to_down_vol_ratio_drop_21_vs_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up/down vol ratio 21d minus same ratio over 63d — recent contraction in demand."""
    chg = close.diff()
    up_v = volume.where(chg > 0)
    dn_v = volume.where(chg < 0)
    r21 = _safe_div(up_v.rolling(MDAYS, min_periods=WDAYS).mean(), dn_v.rolling(MDAYS, min_periods=WDAYS).mean())
    r63 = _safe_div(up_v.rolling(QDAYS, min_periods=MDAYS).mean(), dn_v.rolling(QDAYS, min_periods=MDAYS).mean())
    return r21 - r63


def f06_vddu_056_low_vol_new_high_count_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Count bars in 21d setting 21d new high with vol < 252d median (true dryup at top)."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_v = volume < med
    flag = (nh & low_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_057_low_vol_new_high_count_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Count bars in 63d setting 63d new high with vol < 252d median."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = high > prior_max
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_v = volume < med
    flag = (nh & low_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_vddu_058_low_vol_new_highs_share_of_all_new_highs_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63d new-high bars that were on low-vol days (vol < median 252d)."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = (high > prior_max).astype(float)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_v = (volume < med).astype(float)
    num = (nh * low_v).rolling(QDAYS, min_periods=MDAYS).sum()
    den = nh.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den)


def f06_vddu_059_avg_vol_on_new_21d_high_bars_to_21d_total(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol on 21d-new-high bars / mean vol over all 21d."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = (high > prior_max).astype(float)
    nh_mean = _safe_div(
        (volume * nh).rolling(MDAYS, min_periods=WDAYS).sum(),
        nh.rolling(MDAYS, min_periods=WDAYS).sum(),
    )
    all_mean = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(nh_mean, all_mean)


def f06_vddu_060_avg_vol_on_new_63d_high_bars_to_63d_total(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol on 63d-new-high bars / mean vol over all 63d."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = (high > prior_max).astype(float)
    nh_mean = _safe_div(
        (volume * nh).rolling(QDAYS, min_periods=MDAYS).sum(),
        nh.rolling(QDAYS, min_periods=MDAYS).sum(),
    )
    all_mean = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(nh_mean, all_mean)


def f06_vddu_061_pct_new_high_bars_below_median_vol_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Of 63d new-high bars, fraction with vol below 63d median."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = high > prior_max
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    below = (volume < med)
    nh_total = nh.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    nh_below = (nh & below).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(nh_below, nh_total)


def f06_vddu_062_dryup_at_high_composite_count_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d near 252d max (high/rmax>=0.98) AND vol z < -0.5."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.98
    z = _rolling_zscore(volume, YDAYS)
    low = z < -0.5
    flag = (near & low).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_063_up_volume_waning_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of up-bar volume (vol on close>prev-close bars) over 63d."""
    chg = close.diff()
    up_v = (volume.where(chg > 0)).fillna(0)
    return _rolling_slope(up_v, QDAYS)


def f06_vddu_064_up_minus_down_vol_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of (up vol - down vol) over 21d."""
    chg = close.diff()
    diff_v = (volume.where(chg > 0).fillna(0)) - (volume.where(chg < 0).fillna(0))
    return _rolling_slope(diff_v, MDAYS)


def f06_vddu_065_up_minus_down_vol_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of (up vol - down vol) over 63d."""
    chg = close.diff()
    diff_v = (volume.where(chg > 0).fillna(0)) - (volume.where(chg < 0).fillna(0))
    return _rolling_slope(diff_v, QDAYS)


def f06_vddu_066_avg_up_vol_5d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean up-vol 5d / mean up-vol 63d — recent demand contraction."""
    chg = close.diff()
    up_v = (volume.where(chg > 0)).fillna(0)
    a = up_v.rolling(WDAYS, min_periods=2).mean()
    b = up_v.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a, b)


def f06_vddu_067_cumulative_net_vol_21_vs_63_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(up-vol minus down-vol over 21d) / Sum same over 63d."""
    chg = close.diff()
    net = (volume.where(chg > 0).fillna(0)) - (volume.where(chg < 0).fillna(0))
    a = net.rolling(MDAYS, min_periods=WDAYS).sum()
    b = net.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(a, b)


def f06_vddu_068_accumulated_up_vol_decay_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of cumulative up-vol (cumulative sum) over 63d."""
    chg = close.diff()
    up_v = (volume.where(chg > 0)).fillna(0)
    cum = up_v.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_slope(cum, QDAYS)


def f06_vddu_069_dryup_with_price_stagnation_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z(-vol over 21d) + (-|21d log return|) — both terms positive when quiet AND flat."""
    z = -_rolling_zscore(volume, YDAYS)
    flat = -_safe_log(close).diff(MDAYS).abs()
    return z.rolling(MDAYS, min_periods=WDAYS).mean() + flat


def f06_vddu_070_price_near_high_with_low_vol_count_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d where high/252d_max >= 0.98 AND volume < 252d median."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.98
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (near & (volume < med)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_071_near_252d_high_with_low_quartile_vol_count_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d near 252d high with vol < 252d 25th-pct."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.97
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = (near & (volume < p)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_072_price_vol_divergence_at_top_z_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(price z 63d) - (volume z 63d) — high when price up but vol down."""
    return _rolling_zscore(close, QDAYS) - _rolling_zscore(volume, QDAYS)


def f06_vddu_073_silent_topping_index_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z(-vol) weighted by near-high indicator, averaged over 21d."""
    z = -_rolling_zscore(volume, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.95
    score = z * near.astype(float)
    return score.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_074_low_vol_rally_days_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d up-bars where vol was below 252d median."""
    chg = close.diff()
    up = chg > 0
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low_up = (up & (volume < med)).astype(float)
    return _safe_div(
        low_up.rolling(MDAYS, min_periods=WDAYS).sum(),
        up.astype(float).rolling(MDAYS, min_periods=WDAYS).sum(),
    )


def f06_vddu_075_low_vol_thrust_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 63d where close > prior close by > 1pct but vol below 63d median."""
    chg_pct = close.pct_change()
    thrust = chg_pct > 0.01
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    low_v = volume < med
    flag = (thrust & low_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                        REGISTRY
# ============================================================

VOLUME_DISTRIBUTION_DRYUP_BASE_REGISTRY_001_075 = {
    "f06_vddu_001_volume_sma5_to_sma252": {"inputs": ["volume"], "func": f06_vddu_001_volume_sma5_to_sma252},
    "f06_vddu_002_volume_sma21_to_sma252": {"inputs": ["volume"], "func": f06_vddu_002_volume_sma21_to_sma252},
    "f06_vddu_003_volume_sma21_to_sma63": {"inputs": ["volume"], "func": f06_vddu_003_volume_sma21_to_sma63},
    "f06_vddu_004_volume_median_5d_to_252d": {"inputs": ["volume"], "func": f06_vddu_004_volume_median_5d_to_252d},
    "f06_vddu_005_log_volume_diff_21_vs_252_means": {"inputs": ["volume"], "func": f06_vddu_005_log_volume_diff_21_vs_252_means},
    "f06_vddu_006_dollar_volume_sma21_to_sma252": {"inputs": ["close", "volume"], "func": f06_vddu_006_dollar_volume_sma21_to_sma252},
    "f06_vddu_007_volume_zscore_252d": {"inputs": ["volume"], "func": f06_vddu_007_volume_zscore_252d},
    "f06_vddu_008_volume_zscore_63d": {"inputs": ["volume"], "func": f06_vddu_008_volume_zscore_63d},
    "f06_vddu_009_pct_rank_mean_21d_vol_in_252d": {"inputs": ["volume"], "func": f06_vddu_009_pct_rank_mean_21d_vol_in_252d},
    "f06_vddu_010_pct_rank_mean_5d_vol_in_63d": {"inputs": ["volume"], "func": f06_vddu_010_pct_rank_mean_5d_vol_in_63d},
    "f06_vddu_011_log_volume_contraction_21d": {"inputs": ["volume"], "func": f06_vddu_011_log_volume_contraction_21d},
    "f06_vddu_012_log_volume_contraction_63d": {"inputs": ["volume"], "func": f06_vddu_012_log_volume_contraction_63d},
    "f06_vddu_013_volume_drop_pct_vs_252d_max": {"inputs": ["volume"], "func": f06_vddu_013_volume_drop_pct_vs_252d_max},
    "f06_vddu_014_volume_drop_pct_vs_63d_max": {"inputs": ["volume"], "func": f06_vddu_014_volume_drop_pct_vs_63d_max},
    "f06_vddu_015_volume_vs_252d_75pct": {"inputs": ["volume"], "func": f06_vddu_015_volume_vs_252d_75pct},
    "f06_vddu_016_volume_vs_63d_75pct": {"inputs": ["volume"], "func": f06_vddu_016_volume_vs_63d_75pct},
    "f06_vddu_017_dollar_volume_drop_pct_vs_252d_max": {"inputs": ["close", "volume"], "func": f06_vddu_017_dollar_volume_drop_pct_vs_252d_max},
    "f06_vddu_018_dollar_volume_drop_pct_vs_63d_max": {"inputs": ["close", "volume"], "func": f06_vddu_018_dollar_volume_drop_pct_vs_63d_max},
    "f06_vddu_019_log_max_vol_252d_over_mean_5d": {"inputs": ["volume"], "func": f06_vddu_019_log_max_vol_252d_over_mean_5d},
    "f06_vddu_020_dollar_volume_current_vs_peak_ratio": {"inputs": ["close", "volume"], "func": f06_vddu_020_dollar_volume_current_vs_peak_ratio},
    "f06_vddu_021_avg_dollar_volume_contraction_21_vs_63": {"inputs": ["close", "volume"], "func": f06_vddu_021_avg_dollar_volume_contraction_21_vs_63},
    "f06_vddu_022_volume_sma5_to_ema63": {"inputs": ["volume"], "func": f06_vddu_022_volume_sma5_to_ema63},
    "f06_vddu_023_ema21_to_ema252_volume": {"inputs": ["volume"], "func": f06_vddu_023_ema21_to_ema252_volume},
    "f06_vddu_024_volume_proximity_to_252d_min": {"inputs": ["volume"], "func": f06_vddu_024_volume_proximity_to_252d_min},
    "f06_vddu_025_dollar_volume_proximity_to_252d_min": {"inputs": ["close", "volume"], "func": f06_vddu_025_dollar_volume_proximity_to_252d_min},
    "f06_vddu_026_volume_slope_21d": {"inputs": ["volume"], "func": f06_vddu_026_volume_slope_21d},
    "f06_vddu_027_volume_slope_63d": {"inputs": ["volume"], "func": f06_vddu_027_volume_slope_63d},
    "f06_vddu_028_log_volume_slope_21d": {"inputs": ["volume"], "func": f06_vddu_028_log_volume_slope_21d},
    "f06_vddu_029_log_volume_slope_63d": {"inputs": ["volume"], "func": f06_vddu_029_log_volume_slope_63d},
    "f06_vddu_030_dollar_volume_slope_21d": {"inputs": ["close", "volume"], "func": f06_vddu_030_dollar_volume_slope_21d},
    "f06_vddu_031_dollar_volume_slope_63d": {"inputs": ["close", "volume"], "func": f06_vddu_031_dollar_volume_slope_63d},
    "f06_vddu_032_volume_ema_slope_21d": {"inputs": ["volume"], "func": f06_vddu_032_volume_ema_slope_21d},
    "f06_vddu_033_volume_slope_normalized_by_mean_21d": {"inputs": ["volume"], "func": f06_vddu_033_volume_slope_normalized_by_mean_21d},
    "f06_vddu_034_consecutive_declining_5d_avg_vol_streak": {"inputs": ["volume"], "func": f06_vddu_034_consecutive_declining_5d_avg_vol_streak},
    "f06_vddu_035_days_since_vol_1sigma": {"inputs": ["volume"], "func": f06_vddu_035_days_since_vol_1sigma},
    "f06_vddu_036_days_since_vol_2sigma": {"inputs": ["volume"], "func": f06_vddu_036_days_since_vol_2sigma},
    "f06_vddu_037_days_since_252d_vol_max": {"inputs": ["volume"], "func": f06_vddu_037_days_since_252d_vol_max},
    "f06_vddu_038_days_since_63d_vol_max": {"inputs": ["volume"], "func": f06_vddu_038_days_since_63d_vol_max},
    "f06_vddu_039_declining_vol_days_count_21d": {"inputs": ["volume"], "func": f06_vddu_039_declining_vol_days_count_21d},
    "f06_vddu_040_declining_vol_days_count_63d": {"inputs": ["volume"], "func": f06_vddu_040_declining_vol_days_count_63d},
    "f06_vddu_041_log_volume_range_63d": {"inputs": ["volume"], "func": f06_vddu_041_log_volume_range_63d},
    "f06_vddu_042_volume_range_compression_21_vs_63": {"inputs": ["volume"], "func": f06_vddu_042_volume_range_compression_21_vs_63},
    "f06_vddu_043_volume_cv_drop_21_vs_63": {"inputs": ["volume"], "func": f06_vddu_043_volume_cv_drop_21_vs_63},
    "f06_vddu_044_log_volume_std_drop_21_vs_63": {"inputs": ["volume"], "func": f06_vddu_044_log_volume_std_drop_21_vs_63},
    "f06_vddu_045_volume_exponential_decay_half_life_63d": {"inputs": ["volume"], "func": f06_vddu_045_volume_exponential_decay_half_life_63d},
    "f06_vddu_046_volume_drift_to_vol_of_vol_63d": {"inputs": ["volume"], "func": f06_vddu_046_volume_drift_to_vol_of_vol_63d},
    "f06_vddu_047_pct_days_vol_below_half_sma252_in_21d": {"inputs": ["volume"], "func": f06_vddu_047_pct_days_vol_below_half_sma252_in_21d},
    "f06_vddu_048_pct_days_vol_below_quarter_sma252_in_21d": {"inputs": ["volume"], "func": f06_vddu_048_pct_days_vol_below_quarter_sma252_in_21d},
    "f06_vddu_049_pct_days_vol_below_25pct_252d_in_21d": {"inputs": ["volume"], "func": f06_vddu_049_pct_days_vol_below_25pct_252d_in_21d},
    "f06_vddu_050_pct_days_vol_below_25pct_252d_in_63d": {"inputs": ["volume"], "func": f06_vddu_050_pct_days_vol_below_25pct_252d_in_63d},
    "f06_vddu_051_low_vol_up_day_count_21d": {"inputs": ["close", "volume"], "func": f06_vddu_051_low_vol_up_day_count_21d},
    "f06_vddu_052_low_vol_up_day_count_63d": {"inputs": ["close", "volume"], "func": f06_vddu_052_low_vol_up_day_count_63d},
    "f06_vddu_053_up_to_down_vol_ratio_21d": {"inputs": ["close", "volume"], "func": f06_vddu_053_up_to_down_vol_ratio_21d},
    "f06_vddu_054_up_to_down_vol_ratio_63d": {"inputs": ["close", "volume"], "func": f06_vddu_054_up_to_down_vol_ratio_63d},
    "f06_vddu_055_up_to_down_vol_ratio_drop_21_vs_63": {"inputs": ["close", "volume"], "func": f06_vddu_055_up_to_down_vol_ratio_drop_21_vs_63},
    "f06_vddu_056_low_vol_new_high_count_21d": {"inputs": ["high", "volume"], "func": f06_vddu_056_low_vol_new_high_count_21d},
    "f06_vddu_057_low_vol_new_high_count_63d": {"inputs": ["high", "volume"], "func": f06_vddu_057_low_vol_new_high_count_63d},
    "f06_vddu_058_low_vol_new_highs_share_of_all_new_highs_63d": {"inputs": ["high", "volume"], "func": f06_vddu_058_low_vol_new_highs_share_of_all_new_highs_63d},
    "f06_vddu_059_avg_vol_on_new_21d_high_bars_to_21d_total": {"inputs": ["high", "volume"], "func": f06_vddu_059_avg_vol_on_new_21d_high_bars_to_21d_total},
    "f06_vddu_060_avg_vol_on_new_63d_high_bars_to_63d_total": {"inputs": ["high", "volume"], "func": f06_vddu_060_avg_vol_on_new_63d_high_bars_to_63d_total},
    "f06_vddu_061_pct_new_high_bars_below_median_vol_63d": {"inputs": ["high", "volume"], "func": f06_vddu_061_pct_new_high_bars_below_median_vol_63d},
    "f06_vddu_062_dryup_at_high_composite_count_21d": {"inputs": ["high", "volume"], "func": f06_vddu_062_dryup_at_high_composite_count_21d},
    "f06_vddu_063_up_volume_waning_slope_63d": {"inputs": ["close", "volume"], "func": f06_vddu_063_up_volume_waning_slope_63d},
    "f06_vddu_064_up_minus_down_vol_slope_21d": {"inputs": ["close", "volume"], "func": f06_vddu_064_up_minus_down_vol_slope_21d},
    "f06_vddu_065_up_minus_down_vol_slope_63d": {"inputs": ["close", "volume"], "func": f06_vddu_065_up_minus_down_vol_slope_63d},
    "f06_vddu_066_avg_up_vol_5d_vs_63d": {"inputs": ["close", "volume"], "func": f06_vddu_066_avg_up_vol_5d_vs_63d},
    "f06_vddu_067_cumulative_net_vol_21_vs_63_ratio": {"inputs": ["close", "volume"], "func": f06_vddu_067_cumulative_net_vol_21_vs_63_ratio},
    "f06_vddu_068_accumulated_up_vol_decay_63d": {"inputs": ["close", "volume"], "func": f06_vddu_068_accumulated_up_vol_decay_63d},
    "f06_vddu_069_dryup_with_price_stagnation_score_21d": {"inputs": ["close", "volume"], "func": f06_vddu_069_dryup_with_price_stagnation_score_21d},
    "f06_vddu_070_price_near_high_with_low_vol_count_21d": {"inputs": ["high", "volume"], "func": f06_vddu_070_price_near_high_with_low_vol_count_21d},
    "f06_vddu_071_near_252d_high_with_low_quartile_vol_count_21d": {"inputs": ["high", "volume"], "func": f06_vddu_071_near_252d_high_with_low_quartile_vol_count_21d},
    "f06_vddu_072_price_vol_divergence_at_top_z_63d": {"inputs": ["close", "volume"], "func": f06_vddu_072_price_vol_divergence_at_top_z_63d},
    "f06_vddu_073_silent_topping_index_21d": {"inputs": ["high", "volume"], "func": f06_vddu_073_silent_topping_index_21d},
    "f06_vddu_074_low_vol_rally_days_fraction_21d": {"inputs": ["close", "volume"], "func": f06_vddu_074_low_vol_rally_days_fraction_21d},
    "f06_vddu_075_low_vol_thrust_count_63d": {"inputs": ["close", "volume"], "func": f06_vddu_075_low_vol_thrust_count_63d},
}
