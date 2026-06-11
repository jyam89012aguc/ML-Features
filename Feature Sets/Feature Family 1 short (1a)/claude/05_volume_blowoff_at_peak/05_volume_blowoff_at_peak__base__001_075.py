"""volume_blowoff_at_peak base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: extreme volume EVENTS at/near peak prices — climax bars, blowoff spikes,
single-day extremes, peak-day participation, VWAP overshoots, dollar-volume
concentration, pattern-level climaxes. 150 distinct hypotheses (continued in
__base__076_150.py for 150 total). Inputs: SEP OHLCV only. PIT-clean:
right-anchored rolling, explicit min_periods, no centered windows, no .shift(-N).
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


def _rolling_vwap(price, volume, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    num = (price * volume).rolling(n, min_periods=min_periods).sum()
    den = volume.rolling(n, min_periods=min_periods).sum().replace(0, np.nan)
    return num / den


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f05_vbpk_001_volume_zscore_252d(volume: pd.Series) -> pd.Series:
    """Volume z-score over 252d — extreme participation vs annual baseline."""
    return _rolling_zscore(volume, YDAYS)


def f05_vbpk_002_volume_zscore_63d(volume: pd.Series) -> pd.Series:
    """Volume z-score over 63d — quarterly extremity."""
    return _rolling_zscore(volume, QDAYS)


def f05_vbpk_003_volume_ratio_to_252d_median(volume: pd.Series) -> pd.Series:
    """Volume / 252d median — robust extremity ratio."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(volume, med)


def f05_vbpk_004_volume_ratio_to_63d_median(volume: pd.Series) -> pd.Series:
    """Volume / 63d median — quarterly robust ratio."""
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(volume, med)


def f05_vbpk_005_dollar_volume_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume z-score over 252d — capital intensity extremity."""
    dv = close * volume
    return _rolling_zscore(dv, YDAYS)


def f05_vbpk_006_dollar_volume_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume z-score over 63d."""
    dv = close * volume
    return _rolling_zscore(dv, QDAYS)


def f05_vbpk_007_log_volume_max_21d(volume: pd.Series) -> pd.Series:
    """Max of log volume over last 21d — recent peak intensity level."""
    return _safe_log(volume).rolling(MDAYS, min_periods=WDAYS).max()


def f05_vbpk_008_single_day_peak_volume_zscore_21d(volume: pd.Series) -> pd.Series:
    """Max of 21d-window volume / 252d mean — single-bar peak amplification."""
    peak = volume.rolling(MDAYS, min_periods=WDAYS).max()
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(peak, m)


def f05_vbpk_009_max_volume_5d_vs_252d_median(volume: pd.Series) -> pd.Series:
    """Max-5d volume / 252d median — short-window blowoff intensity."""
    peak = volume.rolling(WDAYS, min_periods=2).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(peak, med)


def f05_vbpk_010_max_volume_21d_vs_252d_median(volume: pd.Series) -> pd.Series:
    """Max-21d volume / 252d median — monthly climax intensity."""
    peak = volume.rolling(MDAYS, min_periods=WDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(peak, med)


def f05_vbpk_011_max_volume_63d_vs_252d_median(volume: pd.Series) -> pd.Series:
    """Max-63d volume / 252d median — quarterly climax intensity."""
    peak = volume.rolling(QDAYS, min_periods=MDAYS).max()
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(peak, med)


def f05_vbpk_012_volume_top_decile_count_21d(volume: pd.Series) -> pd.Series:
    """Bars in last 21d whose volume is in top decile of 252d distribution."""
    thr = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (volume >= thr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_013_volume_top_percentile_count_63d(volume: pd.Series) -> pd.Series:
    """Bars in last 63d whose volume is in top 5pct of 252d distribution."""
    thr = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (volume >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f05_vbpk_014_dollar_volume_top_decile_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in last 21d whose dollar volume is in top decile of 252d distribution."""
    dv = close * volume
    thr = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (dv >= thr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_015_count_3sigma_vol_days_63d(volume: pd.Series) -> pd.Series:
    """Count of volume>3-sigma bars (vs 252d) inside the last 63d."""
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 3.0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f05_vbpk_016_count_5sigma_vol_days_252d(volume: pd.Series) -> pd.Series:
    """Count of volume>5-sigma bars inside the last 252d."""
    z = _rolling_zscore(volume, YDAYS)
    flag = (z > 5.0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f05_vbpk_017_days_since_max_252d_volume(volume: pd.Series) -> pd.Series:
    """Bars since the volume hit its 252d rolling max — recency of annual climax."""
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


def f05_vbpk_018_days_since_max_63d_volume(volume: pd.Series) -> pd.Series:
    """Bars since the volume hit its 63d rolling max."""
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)


def f05_vbpk_019_max_to_mean_volume_ratio_63d(volume: pd.Series) -> pd.Series:
    """Max(63d volume) / Mean(63d volume) — single-day spike vs baseline."""
    mx = volume.rolling(QDAYS, min_periods=MDAYS).max()
    mn = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(mx, mn)


def f05_vbpk_020_max_to_mean_dollar_volume_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max(63d $ vol) / Mean(63d $ vol)."""
    dv = close * volume
    mx = dv.rolling(QDAYS, min_periods=MDAYS).max()
    mn = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(mx, mn)


def f05_vbpk_021_volume_rank_pct_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within last 252d (0-1)."""
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f05_vbpk_022_volume_rank_pct_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current volume within last 63d (0-1)."""
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f05_vbpk_023_log_volume_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of log volume over 252d — log-space tail handling."""
    return _rolling_zscore(_safe_log(volume), YDAYS)


def f05_vbpk_024_extreme_volume_tail_mass_63d(volume: pd.Series) -> pd.Series:
    """Fraction of 63d volume sum that comes from the top-5 bars."""
    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-5:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True)


def f05_vbpk_025_volume_kurtosis_63d(volume: pd.Series) -> pd.Series:
    """Excess kurtosis of volume over 63d — fat-tailed climax regime."""
    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / (sd ** 4) - 3.0)
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_k, raw=True)


def f05_vbpk_026_volume_sma5_to_sma63(volume: pd.Series) -> pd.Series:
    """SMA(5d vol) / SMA(63d vol) — short-burst vs quarterly baseline."""
    s5 = volume.rolling(WDAYS, min_periods=2).mean()
    s63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s5, s63)


def f05_vbpk_027_volume_sma5_to_sma252(volume: pd.Series) -> pd.Series:
    """SMA(5d vol) / SMA(252d vol) — short-burst vs annual baseline."""
    s5 = volume.rolling(WDAYS, min_periods=2).mean()
    s252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s5, s252)


def f05_vbpk_028_volume_sma21_to_sma252(volume: pd.Series) -> pd.Series:
    """SMA(21d vol) / SMA(252d vol) — monthly amplification."""
    s21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    s252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s21, s252)


def f05_vbpk_029_volume_sma21_to_sma63(volume: pd.Series) -> pd.Series:
    """SMA(21d vol) / SMA(63d vol) — monthly vs quarterly."""
    s21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s21, s63)


def f05_vbpk_030_dollar_volume_sma21_to_sma252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-vol SMA(21d)/SMA(252d) — capital amplification."""
    dv = close * volume
    s21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    s252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s21, s252)


def f05_vbpk_031_log_volume_diff_5d(volume: pd.Series) -> pd.Series:
    """5-day log volume change — week-scale thrust in participation."""
    return _safe_log(volume).diff(WDAYS)


def f05_vbpk_032_log_volume_diff_21d(volume: pd.Series) -> pd.Series:
    """21-day log volume change — monthly thrust."""
    return _safe_log(volume).diff(MDAYS)


def f05_vbpk_033_log_volume_diff_63d(volume: pd.Series) -> pd.Series:
    """63-day log volume change — quarterly thrust."""
    return _safe_log(volume).diff(QDAYS)


def f05_vbpk_034_avg_volume_5d_to_median_252d(volume: pd.Series) -> pd.Series:
    """Avg(5d vol) / Median(252d vol) — recent-burst vs robust baseline."""
    a = volume.rolling(WDAYS, min_periods=2).mean()
    m = volume.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(a, m)


def f05_vbpk_035_ema_volume_ratio_short_vs_long(volume: pd.Series) -> pd.Series:
    """EMA(5) vol / EMA(63) vol — exponential amplification."""
    e5 = volume.ewm(span=5, adjust=False, min_periods=2).mean()
    e63 = volume.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return _safe_div(e5, e63)


def f05_vbpk_036_volume_slope_21d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of volume over 21d."""
    return _rolling_slope(volume, MDAYS)


def f05_vbpk_037_volume_slope_63d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of volume over 63d."""
    return _rolling_slope(volume, QDAYS)


def f05_vbpk_038_volume_accel_vs_63d_baseline_z(volume: pd.Series) -> pd.Series:
    """Z-score of 21d volume slope vs its 63d distribution."""
    slope = _rolling_slope(volume, MDAYS)
    return _rolling_zscore(slope, QDAYS)


def f05_vbpk_039_volume_regime_shift_21_vs_252(volume: pd.Series) -> pd.Series:
    """Log( mean(21d vol) / mean(252d vol) ) — regime-level participation shift."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(a) - _safe_log(b)


def f05_vbpk_040_volume_rising_streak_max_21d(volume: pd.Series) -> pd.Series:
    """Max consecutive-up volume streak length inside last 21d."""
    up = (volume.diff() > 0).astype(int)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max()


def f05_vbpk_041_volume_up_day_count_21d(volume: pd.Series) -> pd.Series:
    """Number of bars in last 21d whose volume rose vs prior bar."""
    up = (volume.diff() > 0).astype(float)
    return up.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_042_volume_expansion_at_new_high_days_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on bars setting a new 63d high, divided by total 63d mean volume."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    new_high = (high > prior_max).astype(float)
    nh_vol = (volume * new_high).rolling(QDAYS, min_periods=MDAYS).sum()
    nh_cnt = new_high.rolling(QDAYS, min_periods=MDAYS).sum()
    nh_mean = _safe_div(nh_vol, nh_cnt)
    all_mean = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(nh_mean, all_mean)


def f05_vbpk_043_volume_expanding_pct_days_21d(volume: pd.Series) -> pd.Series:
    """Fraction of bars in last 21d whose volume rose vs prior bar."""
    up = (volume.diff() > 0).astype(float)
    return up.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_044_log_volume_regression_intercept_21d(volume: pd.Series) -> pd.Series:
    """Intercept of log-volume linear fit over 21d — recent log-vol baseline level."""
    lv = _safe_log(volume)
    def _ic(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float(c0)
    return lv.rolling(MDAYS, min_periods=WDAYS).apply(_ic, raw=True)


def f05_vbpk_045_volume_mean_reverter_score_63d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs 63d mean, capturing pull-back-to-mean tendency."""
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return (volume - m) / sd.replace(0, np.nan)


def f05_vbpk_046_top5_volume_share_of_63d(volume: pd.Series) -> pd.Series:
    """Sum of top-5 volume bars / sum of all 63d volume — concentration."""
    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        tot = w.sum()
        if tot == 0:
            return np.nan
        return float(np.sort(w)[-5:].sum() / tot)
    return volume.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True)


def f05_vbpk_047_top1_volume_share_of_21d(volume: pd.Series) -> pd.Series:
    """Max volume bar / sum of all 21d volume — single-bar dominance."""
    mx = volume.rolling(MDAYS, min_periods=WDAYS).max()
    sm = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(mx, sm)


def f05_vbpk_048_top5_volume_share_of_252d(volume: pd.Series) -> pd.Series:
    """Top-5 bar share of 252d volume sum."""
    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        tot = w.sum()
        if tot == 0:
            return np.nan
        return float(np.sort(w)[-5:].sum() / tot)
    return volume.rolling(YDAYS, min_periods=QDAYS).apply(_sh, raw=True)


def f05_vbpk_049_volume_sum_21d_vs_63d(volume: pd.Series) -> pd.Series:
    """Sum(21d vol) / Sum(63d vol) — recent quarter share."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    b = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(a, b)


def f05_vbpk_050_volume_sum_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Sum(21d vol) / Sum(252d vol) — recent month share of year."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    b = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(a, b)


def f05_vbpk_051_volume_on_new_252d_high_zscore_recent(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on the most recent 252d new-high bar, vs that bar's 252d baseline.

    Forward-fills the volume value sampled on the latest new-high bar so the
    feature is defined between new-high events; uses prior-known data only."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = high > prior_max
    nh_vol = volume.where(is_nh).ffill()
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return (nh_vol - m) / sd.replace(0, np.nan)


def f05_vbpk_052_volume_on_new_63d_high_zscore_recent(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on the most recent 63d new-high bar."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = high > prior_max
    nh_vol = volume.where(is_nh).ffill()
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return (nh_vol - m) / sd.replace(0, np.nan)


def f05_vbpk_053_avg_volume_at_new_ath_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on bars marking a 252d new high, over last 63d."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high > prior_max).astype(float)
    s = (volume * is_nh).rolling(QDAYS, min_periods=MDAYS).sum()
    c = is_nh.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(s, c)


def f05_vbpk_054_newhigh_vs_nonnewhigh_volume_ratio_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on 252d-new-high bars / avg volume on other bars in last 63d."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high > prior_max).astype(float)
    is_nn = 1.0 - is_nh
    nh = _safe_div(
        (volume * is_nh).rolling(QDAYS, min_periods=MDAYS).sum(),
        is_nh.rolling(QDAYS, min_periods=MDAYS).sum(),
    )
    nn = _safe_div(
        (volume * is_nn).rolling(QDAYS, min_periods=MDAYS).sum(),
        is_nn.rolling(QDAYS, min_periods=MDAYS).sum(),
    )
    return _safe_div(nh, nn)


def f05_vbpk_055_up_volume_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of up-bar volume (vol on green days) over last 21d window of all days."""
    up = (close.diff() > 0).astype(float)
    up_vol = volume * up
    return _rolling_zscore(up_vol, MDAYS)


def f05_vbpk_056_up_volume_share_at_peak_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of total 63d up-bar volume that landed on 63d new-high bars."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = (high > prior_max)
    is_up = (close.diff() > 0)
    nh_up = (is_nh & is_up).astype(float) * volume
    up_all = is_up.astype(float) * volume
    return _safe_div(
        nh_up.rolling(QDAYS, min_periods=MDAYS).sum(),
        up_all.rolling(QDAYS, min_periods=MDAYS).sum(),
    )


def f05_vbpk_057_volume_on_top5pct_high_bars_z_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on bars where high is within top 5pct of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = high.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    top_flag = ((high - rmin) / rng) >= 0.95
    masked = volume.where(top_flag)
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return (masked.ffill() - m) / sd.replace(0, np.nan)


def f05_vbpk_058_dollar_volume_at_new_highs_vs_other_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $vol on 63d-new-high bars / avg $vol on other bars in last 63d."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = (high > prior_max).astype(float)
    is_nn = 1.0 - is_nh
    dv = close * volume
    nh = _safe_div(
        (dv * is_nh).rolling(QDAYS, min_periods=MDAYS).sum(),
        is_nh.rolling(QDAYS, min_periods=MDAYS).sum(),
    )
    nn = _safe_div(
        (dv * is_nn).rolling(QDAYS, min_periods=MDAYS).sum(),
        is_nn.rolling(QDAYS, min_periods=MDAYS).sum(),
    )
    return _safe_div(nh, nn)


def f05_vbpk_059_volume_times_return_top_quintile_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-quintile (vol * |return|) contribution to total 63d (vol*|ret|) sum."""
    r = _safe_log(close).diff().abs()
    vr = volume * r
    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        n = len(w)
        k = max(1, n // 5)
        tot = w.sum()
        if tot == 0:
            return np.nan
        return float(np.sort(w)[-k:].sum() / tot)
    return vr.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True)


def f05_vbpk_060_price_volume_product_anomaly_z_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (volume * |daily return|) over 21d — anomalous activity-bar burst."""
    r = _safe_log(close).diff().abs()
    vr = volume * r
    return _rolling_zscore(vr, MDAYS)


def f05_vbpk_061_vol_rallies_vs_pullbacks_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(volume on up bars) / Sum(volume on down bars) in 63d."""
    chg = close.diff()
    up_v = (volume.where(chg > 0)).fillna(0)
    dn_v = (volume.where(chg < 0)).fillna(0)
    return _safe_div(
        up_v.rolling(QDAYS, min_periods=MDAYS).sum(),
        dn_v.rolling(QDAYS, min_periods=MDAYS).sum(),
    )


def f05_vbpk_062_cumulative_up_volume_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of cumulative 63d up-volume sum."""
    chg = close.diff()
    up_v = (volume.where(chg > 0)).fillna(0)
    cum = up_v.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_zscore(cum, YDAYS)


def f05_vbpk_063_peak_bar_volume_z_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on the highest-high bar inside the last 63d."""
    def _peakv(idx_window, vol_window):
        if np.isnan(idx_window).any():
            return np.nan
        return float(vol_window[int(np.argmax(idx_window))])
    # use a paired rolling — implement via combined frame
    def _f(w_high, w_vol):
        if np.isnan(w_high).any() or np.isnan(w_vol).any():
            return np.nan
        i = int(np.argmax(w_high))
        return float(w_vol[i])
    peak_v = pd.Series(
        [
            _f(high.iloc[max(0, i - QDAYS + 1):i + 1].values, volume.iloc[max(0, i - QDAYS + 1):i + 1].values)
            if i >= MDAYS else np.nan
            for i in range(len(high))
        ],
        index=high.index,
    )
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return (peak_v - m) / sd.replace(0, np.nan)


def f05_vbpk_064_volume_on_new_252d_high_mean_z_252d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on 252d-new-high bars, z-scored vs 252d volume distribution."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = (high > prior_max).astype(float)
    nh_mean = _safe_div(
        (volume * is_nh).rolling(YDAYS, min_periods=QDAYS).sum(),
        is_nh.rolling(YDAYS, min_periods=QDAYS).sum(),
    )
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return (nh_mean - m) / sd.replace(0, np.nan)


def f05_vbpk_065_newhigh_with_2x_vol_count_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Count bars in last 21d that set 21d new high with vol > 2x sma(252)."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (nh & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_066_up_volume_blowoff_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (up-bar volume * up-bar return) over 21d, z-scored vs 252d distribution."""
    r = _safe_log(close).diff().clip(lower=0)
    v_r = volume * r
    m21 = v_r.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m21, YDAYS)


def f05_vbpk_067_volume_of_largest_gain_day_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on the largest-gain day within last 21d, z-scored vs 252d distribution."""
    r = close.pct_change()
    def _vol_on_max(w_ret, w_vol):
        if np.isnan(w_ret).any() or np.isnan(w_vol).any():
            return np.nan
        i = int(np.argmax(w_ret))
        return float(w_vol[i])
    peak_v = pd.Series(
        [
            _vol_on_max(r.iloc[max(0, i - MDAYS + 1):i + 1].values, volume.iloc[max(0, i - MDAYS + 1):i + 1].values)
            if i >= WDAYS else np.nan
            for i in range(len(r))
        ],
        index=r.index,
    )
    m = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = volume.rolling(YDAYS, min_periods=QDAYS).std()
    return (peak_v - m) / sd.replace(0, np.nan)


def f05_vbpk_068_top5_gain_days_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on top-5 daily-gain bars / mean 63d volume."""
    r = close.pct_change()
    def _topv(w_ret, w_vol):
        if np.isnan(w_ret).any() or np.isnan(w_vol).any():
            return np.nan
        idx = np.argsort(w_ret)[-5:]
        return float(np.sum(w_vol[idx]))
    s = pd.Series(
        [
            _topv(r.iloc[max(0, i - QDAYS + 1):i + 1].values, volume.iloc[max(0, i - QDAYS + 1):i + 1].values)
            if i >= MDAYS else np.nan
            for i in range(len(r))
        ],
        index=r.index,
    )
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s, m * 5.0)


def f05_vbpk_069_vol_range_product_top_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Max(volume * (high-low)) over 21d / its 63d median — peak-bar effort."""
    rng = (high - low)
    vr = volume * rng
    mx = vr.rolling(MDAYS, min_periods=WDAYS).max()
    med = vr.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(mx, med)


def f05_vbpk_070_avg_top5_vol_range_to_median_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of top-5 (vol*range) bars in 63d / median (vol*range) in 63d."""
    vr = volume * (high - low)
    def _r(w):
        if np.isnan(w).any():
            return np.nan
        med = np.median(w)
        if med == 0:
            return np.nan
        return float(np.sort(w)[-5:].mean() / med)
    return vr.rolling(QDAYS, min_periods=MDAYS).apply(_r, raw=True)


def f05_vbpk_071_peak_bar_dollar_vol_z_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of max(close*volume) over 21d vs 252d distribution."""
    dv = close * volume
    peak = dv.rolling(MDAYS, min_periods=WDAYS).max()
    m = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = dv.rolling(YDAYS, min_periods=QDAYS).std()
    return (peak - m) / sd.replace(0, np.nan)


def f05_vbpk_072_price_vs_volume_z_divergence_at_top_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d price z-score minus 63d volume z-score (divergence sign)."""
    zp = _rolling_zscore(close, QDAYS)
    zv = _rolling_zscore(volume, QDAYS)
    return zp - zv


def f05_vbpk_073_closer_to_high_high_vol_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in last 21d with close in top quartile of bar range AND volume > 2x sma_252."""
    pos = (close - low) / (high - low).replace(0, np.nan)
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = ((pos >= 0.75) & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_074_pct_near_max_high_with_2sigma_vol_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars near 252d high with volume z > 2."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.98
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (near & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_075_composite_blowoff_score_near_max_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean composite (vol_z + near_max_pct) over 21d — fused blowoff indicator."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan))
    z = _rolling_zscore(volume, YDAYS)
    score = z.clip(lower=0) * near
    return score.rolling(MDAYS, min_periods=WDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

VOLUME_BLOWOFF_AT_PEAK_BASE_REGISTRY_001_075 = {
    "f05_vbpk_001_volume_zscore_252d": {"inputs": ["volume"], "func": f05_vbpk_001_volume_zscore_252d},
    "f05_vbpk_002_volume_zscore_63d": {"inputs": ["volume"], "func": f05_vbpk_002_volume_zscore_63d},
    "f05_vbpk_003_volume_ratio_to_252d_median": {"inputs": ["volume"], "func": f05_vbpk_003_volume_ratio_to_252d_median},
    "f05_vbpk_004_volume_ratio_to_63d_median": {"inputs": ["volume"], "func": f05_vbpk_004_volume_ratio_to_63d_median},
    "f05_vbpk_005_dollar_volume_zscore_252d": {"inputs": ["close", "volume"], "func": f05_vbpk_005_dollar_volume_zscore_252d},
    "f05_vbpk_006_dollar_volume_zscore_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_006_dollar_volume_zscore_63d},
    "f05_vbpk_007_log_volume_max_21d": {"inputs": ["volume"], "func": f05_vbpk_007_log_volume_max_21d},
    "f05_vbpk_008_single_day_peak_volume_zscore_21d": {"inputs": ["volume"], "func": f05_vbpk_008_single_day_peak_volume_zscore_21d},
    "f05_vbpk_009_max_volume_5d_vs_252d_median": {"inputs": ["volume"], "func": f05_vbpk_009_max_volume_5d_vs_252d_median},
    "f05_vbpk_010_max_volume_21d_vs_252d_median": {"inputs": ["volume"], "func": f05_vbpk_010_max_volume_21d_vs_252d_median},
    "f05_vbpk_011_max_volume_63d_vs_252d_median": {"inputs": ["volume"], "func": f05_vbpk_011_max_volume_63d_vs_252d_median},
    "f05_vbpk_012_volume_top_decile_count_21d": {"inputs": ["volume"], "func": f05_vbpk_012_volume_top_decile_count_21d},
    "f05_vbpk_013_volume_top_percentile_count_63d": {"inputs": ["volume"], "func": f05_vbpk_013_volume_top_percentile_count_63d},
    "f05_vbpk_014_dollar_volume_top_decile_count_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_014_dollar_volume_top_decile_count_21d},
    "f05_vbpk_015_count_3sigma_vol_days_63d": {"inputs": ["volume"], "func": f05_vbpk_015_count_3sigma_vol_days_63d},
    "f05_vbpk_016_count_5sigma_vol_days_252d": {"inputs": ["volume"], "func": f05_vbpk_016_count_5sigma_vol_days_252d},
    "f05_vbpk_017_days_since_max_252d_volume": {"inputs": ["volume"], "func": f05_vbpk_017_days_since_max_252d_volume},
    "f05_vbpk_018_days_since_max_63d_volume": {"inputs": ["volume"], "func": f05_vbpk_018_days_since_max_63d_volume},
    "f05_vbpk_019_max_to_mean_volume_ratio_63d": {"inputs": ["volume"], "func": f05_vbpk_019_max_to_mean_volume_ratio_63d},
    "f05_vbpk_020_max_to_mean_dollar_volume_ratio_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_020_max_to_mean_dollar_volume_ratio_63d},
    "f05_vbpk_021_volume_rank_pct_252d": {"inputs": ["volume"], "func": f05_vbpk_021_volume_rank_pct_252d},
    "f05_vbpk_022_volume_rank_pct_63d": {"inputs": ["volume"], "func": f05_vbpk_022_volume_rank_pct_63d},
    "f05_vbpk_023_log_volume_zscore_252d": {"inputs": ["volume"], "func": f05_vbpk_023_log_volume_zscore_252d},
    "f05_vbpk_024_extreme_volume_tail_mass_63d": {"inputs": ["volume"], "func": f05_vbpk_024_extreme_volume_tail_mass_63d},
    "f05_vbpk_025_volume_kurtosis_63d": {"inputs": ["volume"], "func": f05_vbpk_025_volume_kurtosis_63d},
    "f05_vbpk_026_volume_sma5_to_sma63": {"inputs": ["volume"], "func": f05_vbpk_026_volume_sma5_to_sma63},
    "f05_vbpk_027_volume_sma5_to_sma252": {"inputs": ["volume"], "func": f05_vbpk_027_volume_sma5_to_sma252},
    "f05_vbpk_028_volume_sma21_to_sma252": {"inputs": ["volume"], "func": f05_vbpk_028_volume_sma21_to_sma252},
    "f05_vbpk_029_volume_sma21_to_sma63": {"inputs": ["volume"], "func": f05_vbpk_029_volume_sma21_to_sma63},
    "f05_vbpk_030_dollar_volume_sma21_to_sma252": {"inputs": ["close", "volume"], "func": f05_vbpk_030_dollar_volume_sma21_to_sma252},
    "f05_vbpk_031_log_volume_diff_5d": {"inputs": ["volume"], "func": f05_vbpk_031_log_volume_diff_5d},
    "f05_vbpk_032_log_volume_diff_21d": {"inputs": ["volume"], "func": f05_vbpk_032_log_volume_diff_21d},
    "f05_vbpk_033_log_volume_diff_63d": {"inputs": ["volume"], "func": f05_vbpk_033_log_volume_diff_63d},
    "f05_vbpk_034_avg_volume_5d_to_median_252d": {"inputs": ["volume"], "func": f05_vbpk_034_avg_volume_5d_to_median_252d},
    "f05_vbpk_035_ema_volume_ratio_short_vs_long": {"inputs": ["volume"], "func": f05_vbpk_035_ema_volume_ratio_short_vs_long},
    "f05_vbpk_036_volume_slope_21d": {"inputs": ["volume"], "func": f05_vbpk_036_volume_slope_21d},
    "f05_vbpk_037_volume_slope_63d": {"inputs": ["volume"], "func": f05_vbpk_037_volume_slope_63d},
    "f05_vbpk_038_volume_accel_vs_63d_baseline_z": {"inputs": ["volume"], "func": f05_vbpk_038_volume_accel_vs_63d_baseline_z},
    "f05_vbpk_039_volume_regime_shift_21_vs_252": {"inputs": ["volume"], "func": f05_vbpk_039_volume_regime_shift_21_vs_252},
    "f05_vbpk_040_volume_rising_streak_max_21d": {"inputs": ["volume"], "func": f05_vbpk_040_volume_rising_streak_max_21d},
    "f05_vbpk_041_volume_up_day_count_21d": {"inputs": ["volume"], "func": f05_vbpk_041_volume_up_day_count_21d},
    "f05_vbpk_042_volume_expansion_at_new_high_days_63d": {"inputs": ["high", "volume"], "func": f05_vbpk_042_volume_expansion_at_new_high_days_63d},
    "f05_vbpk_043_volume_expanding_pct_days_21d": {"inputs": ["volume"], "func": f05_vbpk_043_volume_expanding_pct_days_21d},
    "f05_vbpk_044_log_volume_regression_intercept_21d": {"inputs": ["volume"], "func": f05_vbpk_044_log_volume_regression_intercept_21d},
    "f05_vbpk_045_volume_mean_reverter_score_63d": {"inputs": ["volume"], "func": f05_vbpk_045_volume_mean_reverter_score_63d},
    "f05_vbpk_046_top5_volume_share_of_63d": {"inputs": ["volume"], "func": f05_vbpk_046_top5_volume_share_of_63d},
    "f05_vbpk_047_top1_volume_share_of_21d": {"inputs": ["volume"], "func": f05_vbpk_047_top1_volume_share_of_21d},
    "f05_vbpk_048_top5_volume_share_of_252d": {"inputs": ["volume"], "func": f05_vbpk_048_top5_volume_share_of_252d},
    "f05_vbpk_049_volume_sum_21d_vs_63d": {"inputs": ["volume"], "func": f05_vbpk_049_volume_sum_21d_vs_63d},
    "f05_vbpk_050_volume_sum_21d_vs_252d": {"inputs": ["volume"], "func": f05_vbpk_050_volume_sum_21d_vs_252d},
    "f05_vbpk_051_volume_on_new_252d_high_zscore_recent": {"inputs": ["high", "volume"], "func": f05_vbpk_051_volume_on_new_252d_high_zscore_recent},
    "f05_vbpk_052_volume_on_new_63d_high_zscore_recent": {"inputs": ["high", "volume"], "func": f05_vbpk_052_volume_on_new_63d_high_zscore_recent},
    "f05_vbpk_053_avg_volume_at_new_ath_63d": {"inputs": ["high", "volume"], "func": f05_vbpk_053_avg_volume_at_new_ath_63d},
    "f05_vbpk_054_newhigh_vs_nonnewhigh_volume_ratio_63d": {"inputs": ["high", "volume"], "func": f05_vbpk_054_newhigh_vs_nonnewhigh_volume_ratio_63d},
    "f05_vbpk_055_up_volume_zscore_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_055_up_volume_zscore_21d},
    "f05_vbpk_056_up_volume_share_at_peak_63d": {"inputs": ["high", "close", "volume"], "func": f05_vbpk_056_up_volume_share_at_peak_63d},
    "f05_vbpk_057_volume_on_top5pct_high_bars_z_252d": {"inputs": ["high", "volume"], "func": f05_vbpk_057_volume_on_top5pct_high_bars_z_252d},
    "f05_vbpk_058_dollar_volume_at_new_highs_vs_other_63d": {"inputs": ["high", "close", "volume"], "func": f05_vbpk_058_dollar_volume_at_new_highs_vs_other_63d},
    "f05_vbpk_059_volume_times_return_top_quintile_share_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_059_volume_times_return_top_quintile_share_63d},
    "f05_vbpk_060_price_volume_product_anomaly_z_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_060_price_volume_product_anomaly_z_21d},
    "f05_vbpk_061_vol_rallies_vs_pullbacks_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_061_vol_rallies_vs_pullbacks_63d},
    "f05_vbpk_062_cumulative_up_volume_zscore_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_062_cumulative_up_volume_zscore_63d},
    "f05_vbpk_063_peak_bar_volume_z_63d": {"inputs": ["high", "volume"], "func": f05_vbpk_063_peak_bar_volume_z_63d},
    "f05_vbpk_064_volume_on_new_252d_high_mean_z_252d": {"inputs": ["high", "volume"], "func": f05_vbpk_064_volume_on_new_252d_high_mean_z_252d},
    "f05_vbpk_065_newhigh_with_2x_vol_count_21d": {"inputs": ["high", "volume"], "func": f05_vbpk_065_newhigh_with_2x_vol_count_21d},
    "f05_vbpk_066_up_volume_blowoff_index_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_066_up_volume_blowoff_index_21d},
    "f05_vbpk_067_volume_of_largest_gain_day_z_252d": {"inputs": ["close", "volume"], "func": f05_vbpk_067_volume_of_largest_gain_day_z_252d},
    "f05_vbpk_068_top5_gain_days_vol_share_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_068_top5_gain_days_vol_share_63d},
    "f05_vbpk_069_vol_range_product_top_21d": {"inputs": ["high", "low", "volume"], "func": f05_vbpk_069_vol_range_product_top_21d},
    "f05_vbpk_070_avg_top5_vol_range_to_median_63d": {"inputs": ["high", "low", "volume"], "func": f05_vbpk_070_avg_top5_vol_range_to_median_63d},
    "f05_vbpk_071_peak_bar_dollar_vol_z_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_071_peak_bar_dollar_vol_z_21d},
    "f05_vbpk_072_price_vs_volume_z_divergence_at_top_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_072_price_vs_volume_z_divergence_at_top_63d},
    "f05_vbpk_073_closer_to_high_high_vol_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": f05_vbpk_073_closer_to_high_high_vol_count_21d},
    "f05_vbpk_074_pct_near_max_high_with_2sigma_vol_21d": {"inputs": ["high", "volume"], "func": f05_vbpk_074_pct_near_max_high_with_2sigma_vol_21d},
    "f05_vbpk_075_composite_blowoff_score_near_max_21d": {"inputs": ["high", "volume"], "func": f05_vbpk_075_composite_blowoff_score_near_max_21d},
}
