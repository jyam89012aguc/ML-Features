"""volume_blowoff_climax d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d2__076_150.py. Each
feature encodes a different concept in the volume-blowoff-climax theme:
peak detection / post-climax decay / pyramid build-up / burst events / entropy /
vol×return interaction / profile shape / regime shift / multi-horizon ranks /
price-action composites.

Inputs: SEP OHLCV. Volume is the star. PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(N). Self-contained helpers.
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


def _rolling_robust_z(s, window, min_periods=None):
    """MAD-based robust z-score on a rolling window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    med = s.rolling(window, min_periods=min_periods).median()
    mad = (s - med).abs().rolling(window, min_periods=min_periods).median()
    return _safe_div(s - med, 1.4826 * mad)


def _rolling_pct_rank(s, window, min_periods=None):
    """Empirical percentile rank of current value within rolling window."""
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_skew_manual(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 5:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 3))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_kurt_manual(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 5:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((v - m) / sd) ** 4) - 3.0)
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def f19_vblc_001_vol_ratio_to_21d_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(21, min_periods=7).max()
    out = _safe_div(volume, rmax)
    return out.diff().diff()


def f19_vblc_002_vol_ratio_to_63d_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(63, min_periods=21).max()
    out = _safe_div(volume, rmax)
    return out.diff().diff()


def f19_vblc_003_vol_ratio_to_252d_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(252, min_periods=84).max()
    out = _safe_div(volume, rmax)
    return out.diff().diff()


def f19_vblc_004_vol_ratio_to_504d_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(504, min_periods=168).max()
    out = _safe_div(volume, rmax)
    return out.diff().diff()


def f19_vblc_005_log_vol_dist_above_252d_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(252, min_periods=84).max()
    out = _safe_log(volume) - _safe_log(rmax)
    return out.diff().diff()


def f19_vblc_006_log_vol_zscore_63d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_zscore(_safe_log(volume), 63, min_periods=21)
    return out.diff().diff()


def f19_vblc_007_log_vol_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_zscore(_safe_log(volume), 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_008_vol_ratio_to_21d_median_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(21, min_periods=7).median()
    out = _safe_div(volume, med)
    return out.diff().diff()


def f19_vblc_009_vol_ratio_to_252d_median_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(252, min_periods=84).median()
    out = _safe_div(volume, med)
    return out.diff().diff()


def f19_vblc_010_extreme_vol_3x_63d_median_indicator_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    out = (volume > 3.0 * med).astype(float).where(med.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_011_extreme_vol_5x_252d_median_indicator_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(252, min_periods=84).median()
    out = (volume > 5.0 * med).astype(float).where(med.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_012_cum5d_vol_vs_63d_5d_median_d2(volume: pd.Series) -> pd.Series:
    c5 = volume.rolling(5, min_periods=2).sum()
    med = c5.rolling(63, min_periods=21).median()
    out = _safe_div(c5, med)
    return out.diff().diff()


def f19_vblc_013_log_vol_robust_z_63d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_robust_z(_safe_log(volume), 63, min_periods=21)
    return out.diff().diff()


def f19_vblc_014_log_vol_robust_z_252d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_robust_z(_safe_log(volume), 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_015_vol_ratio_to_alltime_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.expanding(min_periods=63).max()
    out = _safe_div(volume, rmax)
    return out.diff().diff()


def f19_vblc_016_bars_since_21d_vol_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    out = volume.rolling(21, min_periods=7).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_017_bars_since_63d_vol_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_018_bars_since_252d_vol_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    out = volume.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_019_post_peak_decay_slope_10d_after_21d_max_d2(volume: pd.Series) -> pd.Series:
    def _f_idx(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    bars_since = volume.rolling(21, min_periods=7).apply(_f_idx, raw=True)
    lv = _safe_log(volume)
    out = _rolling_slope(lv, 10, min_periods=4).where(bars_since == 10, np.nan)
    return out.diff().diff()


def f19_vblc_020_post_peak_half_life_63d_max_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(63, min_periods=21).max()
    def _hl(w):
        if w.size < 5 or np.isnan(w).all():
            return np.nan
        peak_idx = int(np.nanargmax(w))
        peak_v = w[peak_idx]
        if peak_v <= 0:
            return np.nan
        for j in range(peak_idx + 1, w.size):
            if not np.isnan(w[j]) and w[j] <= 0.5 * peak_v:
                return float(j - peak_idx)
        return float(w.size - peak_idx)
    out = volume.rolling(63, min_periods=21).apply(_hl, raw=True)
    return out.diff().diff()


def f19_vblc_021_climax_then_fade_indicator_21d_d2(volume: pd.Series) -> pd.Series:
    def _f_idx(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    bars_since = volume.rolling(21, min_periods=7).apply(_f_idx, raw=True)
    med = volume.rolling(63, min_periods=21).median()
    below = (volume < med).astype(float)
    fade = below.rolling(10, min_periods=5).mean()
    out = ((bars_since == 10) & (fade > 0.7)).astype(float).where(bars_since.notna() & fade.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_022_post_climax_vol_ratio_post_over_pre_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 21 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        pre = w[max(0, pk - 21):pk]
        post = w[pk + 1:min(w.size, pk + 22)]
        if pre.size < 5 or post.size < 5:
            return np.nan
        pre_m = np.nanmean(pre); post_m = np.nanmean(post)
        if pre_m <= 0:
            return np.nan
        return float(post_m / pre_m)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_023_frac_low_vol_post_climax_21d_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 21 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        post = w[pk + 1:min(w.size, pk + 22)]
        if post.size < 5:
            return np.nan
        med = np.nanmedian(w)
        return float(np.nansum(post < med)) / float(post.size)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_024_post_climax_decline_pct_10d_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 12 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        peak_v = w[pk]
        if peak_v <= 0:
            return np.nan
        j = pk + 10
        if j >= w.size or np.isnan(w[j]):
            return np.nan
        return float(1.0 - w[j] / peak_v)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_025_echo_peak_count_21d_after_63d_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 22 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk >= w.size - 1:
            return 0.0
        post = w[pk + 1:min(w.size, pk + 22)]
        if post.size < 3:
            return 0.0
        thresh = w[pk] * 0.5
        return float(np.nansum(post > thresh))
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_026_in_mid_decay_window_5_to_15_bars_63d_d2(volume: pd.Series) -> pd.Series:
    def _f_idx(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    bs = volume.rolling(63, min_periods=21).apply(_f_idx, raw=True)
    out = ((bs >= 5) & (bs <= 15)).astype(float).where(bs.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_027_consec_low_vol_bars_post_peak_21d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(21, min_periods=7).median()
    below = (volume < med).astype(int).where(med.notna(), 0)
    block = (below != below.shift(1)).fillna(False).cumsum()
    streak = below.groupby(block).cumcount().astype(float)
    out = (streak * (below > 0)).where(med.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_028_post_climax_21d_mean_over_252d_median_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 84 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        post = w[pk + 1:min(w.size, pk + 22)]
        if post.size < 5:
            return np.nan
        med = np.nanmedian(w)
        if med <= 0:
            return np.nan
        return float(np.nanmean(post) / med)
    out = volume.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_029_climax_hazard_inv_age_252d_d2(volume: pd.Series) -> pd.Series:
    def _f_idx(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    bs = volume.rolling(252, min_periods=84).apply(_f_idx, raw=True)
    out = 1.0 / (bs + 1.0).where(bs.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_030_log_vol_10d_slope_post_peak_63d_d2(volume: pd.Series) -> pd.Series:
    def _f_idx(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = int(np.nanargmax(w))
        return float(w.size - 1 - idx)
    bs = volume.rolling(63, min_periods=21).apply(_f_idx, raw=True)
    sl = _rolling_slope(_safe_log(volume), 10, min_periods=4)
    out = sl.where(bs == 10, np.nan)
    return out.diff().diff()


def f19_vblc_031_monotonic_vol_rise_count_21d_d2(volume: pd.Series) -> pd.Series:
    rise = (volume > volume.shift(1)).astype(float).where(volume.notna() & volume.shift(1).notna(), np.nan)
    out = rise.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_032_current_monotonic_vol_rise_streak_d2(volume: pd.Series) -> pd.Series:
    rise = (volume > volume.shift(1)).astype(int).where(volume.notna() & volume.shift(1).notna(), 0)
    block = (rise != rise.shift(1)).fillna(False).cumsum()
    streak = rise.groupby(block).cumcount().astype(float)
    out = (streak * (rise > 0)).where(volume.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_033_cum_vol_5bars_pre_21d_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 6 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk < 5:
            return np.nan
        pre = w[pk - 5:pk]
        return float(np.nansum(pre))
    out = volume.rolling(21, min_periods=7).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_034_cum_vol_21bars_pre_63d_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 22 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk < 21:
            return np.nan
        pre = w[pk - 21:pk]
        return float(np.nansum(pre))
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_035_log_vol_slope_5bars_pre_21d_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 6 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk < 5:
            return np.nan
        pre = w[pk - 5:pk]
        valid = ~np.isnan(pre) & (pre > 0)
        if valid.sum() < 3:
            return np.nan
        x = np.arange(pre.size, dtype=float)[valid]
        y = np.log(pre[valid])
        xm = x.mean(); ym = y.mean()
        den = ((x - xm) ** 2).sum()
        if den <= 0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den)
    out = volume.rolling(21, min_periods=7).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_036_pre5d_over_post5d_cum_vol_at_21d_max_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 11 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk < 5 or pk > w.size - 6:
            return np.nan
        pre = w[pk - 5:pk]; post = w[pk + 1:pk + 6]
        ps = np.nansum(post)
        if ps <= 0:
            return np.nan
        return float(np.nansum(pre) / ps)
    out = volume.rolling(21, min_periods=7).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_037_new_21d_vol_high_count_63d_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(21, min_periods=7).max()
    new_h = (volume >= rmax).astype(float).where(volume.notna(), np.nan)
    out = new_h.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f19_vblc_038_new_63d_vol_high_count_252d_d2(volume: pd.Series) -> pd.Series:
    rmax = volume.rolling(63, min_periods=21).max()
    new_h = (volume >= rmax).astype(float).where(volume.notna(), np.nan)
    out = new_h.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f19_vblc_039_buildup_density_21d_vs_prior_21d_median_d2(volume: pd.Series) -> pd.Series:
    prior_med = volume.shift(21).rolling(21, min_periods=7).median()
    big = (volume > 1.5 * prior_med).astype(float).where(prior_med.notna(), np.nan)
    out = big.rolling(21, min_periods=7).sum()
    return out.diff().diff()


def f19_vblc_040_consec_vol_and_close_rise_streak_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = ((volume > volume.shift(1)) & (close > close.shift(1))).astype(int).where(close.notna() & volume.notna() & close.shift(1).notna() & volume.shift(1).notna(), 0)
    block = (up != up.shift(1)).fillna(False).cumsum()
    st = up.groupby(block).cumcount().astype(float)
    out = (st * (up > 0)).where(close.notna() & volume.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_041_cum21d_vol_zscore_in_252d_d2(volume: pd.Series) -> pd.Series:
    c21 = volume.rolling(21, min_periods=7).sum()
    out = _rolling_zscore(c21, 252, min_periods=84)
    return out.diff().diff()


def f19_vblc_042_max_log_vol_jump_21d_d2(volume: pd.Series) -> pd.Series:
    j = _safe_log(volume).diff().abs()
    out = j.rolling(21, min_periods=7).max()
    return out.diff().diff()


def f19_vblc_043_log_vol_slope_21d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(volume), 21, min_periods=7)
    return out.diff().diff()


def f19_vblc_044_log_vol_slope_63d_d2(volume: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(volume), 63, min_periods=21)
    return out.diff().diff()


def f19_vblc_045_peak_over_prior_21d_mean_21d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        if w.size < 11 or np.isnan(w).all():
            return np.nan
        pk = int(np.nanargmax(w))
        if pk < 5:
            return np.nan
        pre_m = np.nanmean(w[:pk])
        if pre_m <= 0:
            return np.nan
        return float(w[pk] / pre_m)
    out = volume.rolling(21, min_periods=7).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_046_burst_3x_63d_median_count_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float).where(med.notna(), np.nan)
    out = burst.rolling(63, min_periods=21).sum()
    return out.diff().diff()


def f19_vblc_047_burst_3x_63d_median_count_252d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float).where(med.notna(), np.nan)
    out = burst.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f19_vblc_048_mean_inter_burst_gap_252d_3x_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float).where(med.notna(), np.nan)
    cnt = burst.rolling(252, min_periods=84).sum()
    out = 252.0 / cnt.replace(0, np.nan)
    return out.diff().diff()


def f19_vblc_049_burst_clustering_252d_3x_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float).where(med.notna(), np.nan)
    def _clust(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        idx = np.where(w > 0.5)[0]
        if idx.size < 3:
            return np.nan
        gaps = np.diff(idx)
        if gaps.size < 2 or np.mean(gaps) == 0:
            return np.nan
        return float(np.var(gaps) / (np.mean(gaps) ** 2))
    out = burst.rolling(252, min_periods=84).apply(_clust, raw=True)
    return out.diff().diff()


def f19_vblc_050_max_burst_magnitude_252d_vs_63d_median_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    ratio = _safe_div(volume, med)
    out = ratio.rolling(252, min_periods=84).max()
    return out.diff().diff()


def f19_vblc_051_bars_since_last_burst_3x_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).fillna(False)
    arr = burst.astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=volume.index)
    return out.diff().diff()


def f19_vblc_052_mean_burst_magnitude_252d_3x_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    ratio = _safe_div(volume, med)
    big = ratio.where(volume > 3.0 * med, np.nan)
    out = big.rolling(252, min_periods=84).mean()
    return out.diff().diff()


def f19_vblc_053_burst_then_5d_neg_return_3x_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    ret5 = _safe_log(close).diff(5)
    out = (burst.shift(5) * (ret5 < 0).astype(float)).where(med.notna() & ret5.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_054_three_plus_bursts_in_21d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    cnt = burst.rolling(21, min_periods=7).sum()
    out = (cnt >= 3).astype(float).where(cnt.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_055_first_burst_after_63d_quiet_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    prior_quiet = (burst.shift(1).rolling(63, min_periods=21).sum() == 0).astype(float)
    out = (burst * prior_quiet).where(med.notna() & prior_quiet.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_056_extreme_vs_moderate_burst_ratio_252d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    mod = (volume > 3.0 * med).astype(float).rolling(252, min_periods=84).sum()
    ext = (volume > 5.0 * med).astype(float).rolling(252, min_periods=84).sum()
    out = _safe_div(ext, mod.replace(0, np.nan))
    return out.diff().diff()


def f19_vblc_057_burst_with_price_spike_3x_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    ret = _safe_log(close).diff()
    rv21 = ret.rolling(21, min_periods=7).std()
    spike = (ret.abs() > 2.0 * rv21).astype(float)
    out = (burst * spike).where(med.notna() & rv21.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_058_climactic_burst_near_252d_max_indicator_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    rmax = volume.rolling(252, min_periods=84).max()
    near_max = (volume >= 0.9 * rmax).astype(float)
    out = (burst * near_max).where(med.notna() & rmax.notna(), np.nan)
    return out.diff().diff()


def f19_vblc_059_burst_freq_change_21d_vs_prior_21d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float)
    recent = burst.rolling(21, min_periods=7).sum()
    prior = burst.shift(21).rolling(21, min_periods=7).sum()
    out = recent - prior
    return out.diff().diff()


def f19_vblc_060_longest_burst_free_interval_252d_3x_63d_d2(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63, min_periods=21).median()
    burst = (volume > 3.0 * med).astype(float).where(med.notna(), np.nan)
    def _gap(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        arr = np.nan_to_num(w, nan=0.0)
        best = 0; cur = 0
        for v in arr:
            if v < 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = burst.rolling(252, min_periods=84).apply(_gap, raw=True)
    return out.diff().diff()


def f19_vblc_061_log_vol_shannon_entropy_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ent(w):
        valid = w[~np.isnan(w)]
        if valid.size < 10:
            return np.nan
        bins, _ = np.histogram(valid, bins=10)
        if bins.sum() == 0:
            return np.nan
        p = bins / bins.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = lv.rolling(63, min_periods=21).apply(_ent, raw=True)
    return out.diff().diff()


def f19_vblc_062_log_vol_shannon_entropy_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ent(w):
        valid = w[~np.isnan(w)]
        if valid.size < 10:
            return np.nan
        bins, _ = np.histogram(valid, bins=10)
        if bins.sum() == 0:
            return np.nan
        p = bins / bins.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = lv.rolling(252, min_periods=84).apply(_ent, raw=True)
    return out.diff().diff()


def f19_vblc_063_volume_gini_63d_d2(volume: pd.Series) -> pd.Series:
    def _gini(w):
        v = w[~np.isnan(w)]
        v = v[v >= 0]
        if v.size < 5:
            return np.nan
        s = np.sort(v)
        n = s.size
        cs = np.cumsum(s)
        if cs[-1] == 0:
            return np.nan
        return float((2.0 * np.sum((np.arange(1, n + 1) * s)) - (n + 1) * cs[-1]) / (n * cs[-1]))
    out = volume.rolling(63, min_periods=21).apply(_gini, raw=True)
    return out.diff().diff()


def f19_vblc_064_volume_gini_252d_d2(volume: pd.Series) -> pd.Series:
    def _gini(w):
        v = w[~np.isnan(w)]
        v = v[v >= 0]
        if v.size < 5:
            return np.nan
        s = np.sort(v)
        n = s.size
        cs = np.cumsum(s)
        if cs[-1] == 0:
            return np.nan
        return float((2.0 * np.sum((np.arange(1, n + 1) * s)) - (n + 1) * cs[-1]) / (n * cs[-1]))
    out = volume.rolling(252, min_periods=84).apply(_gini, raw=True)
    return out.diff().diff()


def f19_vblc_065_top3_share_of_21d_total_vol_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 5 or v.sum() == 0:
            return np.nan
        s = np.sort(v)[-3:]
        return float(s.sum() / v.sum())
    out = volume.rolling(21, min_periods=7).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_066_top5_share_of_63d_total_vol_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 10 or v.sum() == 0:
            return np.nan
        s = np.sort(v)[-5:]
        return float(s.sum() / v.sum())
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_067_top_decile_share_of_252d_total_vol_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 50 or v.sum() == 0:
            return np.nan
        k = max(1, v.size // 10)
        s = np.sort(v)[-k:]
        return float(s.sum() / v.sum())
    out = volume.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_068_vol_p95_tail_share_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 10 or v.sum() == 0:
            return np.nan
        th = np.percentile(v, 95)
        return float(v[v >= th].sum() / v.sum())
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_069_vol_p95_over_p50_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        p50 = np.percentile(v, 50)
        if p50 <= 0:
            return np.nan
        return float(np.percentile(v, 95) / p50)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_070_vol_cv_63d_d2(volume: pd.Series) -> pd.Series:
    m = volume.rolling(63, min_periods=21).mean()
    sd = volume.rolling(63, min_periods=21).std()
    out = _safe_div(sd, m)
    return out.diff().diff()


def f19_vblc_071_vol_cv_252d_d2(volume: pd.Series) -> pd.Series:
    m = volume.rolling(252, min_periods=84).mean()
    sd = volume.rolling(252, min_periods=84).std()
    out = _safe_div(sd, m)
    return out.diff().diff()


def f19_vblc_072_log_vol_entropy_21d_change_63d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ent(w):
        valid = w[~np.isnan(w)]
        if valid.size < 10:
            return np.nan
        bins, _ = np.histogram(valid, bins=10)
        if bins.sum() == 0:
            return np.nan
        p = bins / bins.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    e = lv.rolling(63, min_periods=21).apply(_ent, raw=True)
    out = e - e.shift(21)
    return out.diff().diff()


def f19_vblc_073_vol_iqr_over_median_63d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        med = np.median(v)
        if med <= 0:
            return np.nan
        return float((np.percentile(v, 75) - np.percentile(v, 25)) / med)
    out = volume.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_074_vol_iqr_over_median_252d_d2(volume: pd.Series) -> pd.Series:
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 20:
            return np.nan
        med = np.median(v)
        if med <= 0:
            return np.nan
        return float((np.percentile(v, 75) - np.percentile(v, 25)) / med)
    out = volume.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f19_vblc_075_log_vol_entropy_zscore_63d_in_252d_d2(volume: pd.Series) -> pd.Series:
    lv = _safe_log(volume)
    def _ent(w):
        valid = w[~np.isnan(w)]
        if valid.size < 10:
            return np.nan
        bins, _ = np.histogram(valid, bins=10)
        if bins.sum() == 0:
            return np.nan
        p = bins / bins.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    e = lv.rolling(63, min_periods=21).apply(_ent, raw=True)
    out = _rolling_zscore(e, 252, min_periods=84)
    return out.diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d2)
# ============================================================

VOLUME_BLOWOFF_CLIMAX_D2_REGISTRY_001_075 = {
    "f19_vblc_001_vol_ratio_to_21d_max_d2": {"inputs": ["volume"], "func": f19_vblc_001_vol_ratio_to_21d_max_d2},
    "f19_vblc_002_vol_ratio_to_63d_max_d2": {"inputs": ["volume"], "func": f19_vblc_002_vol_ratio_to_63d_max_d2},
    "f19_vblc_003_vol_ratio_to_252d_max_d2": {"inputs": ["volume"], "func": f19_vblc_003_vol_ratio_to_252d_max_d2},
    "f19_vblc_004_vol_ratio_to_504d_max_d2": {"inputs": ["volume"], "func": f19_vblc_004_vol_ratio_to_504d_max_d2},
    "f19_vblc_005_log_vol_dist_above_252d_max_d2": {"inputs": ["volume"], "func": f19_vblc_005_log_vol_dist_above_252d_max_d2},
    "f19_vblc_006_log_vol_zscore_63d_d2": {"inputs": ["volume"], "func": f19_vblc_006_log_vol_zscore_63d_d2},
    "f19_vblc_007_log_vol_zscore_252d_d2": {"inputs": ["volume"], "func": f19_vblc_007_log_vol_zscore_252d_d2},
    "f19_vblc_008_vol_ratio_to_21d_median_d2": {"inputs": ["volume"], "func": f19_vblc_008_vol_ratio_to_21d_median_d2},
    "f19_vblc_009_vol_ratio_to_252d_median_d2": {"inputs": ["volume"], "func": f19_vblc_009_vol_ratio_to_252d_median_d2},
    "f19_vblc_010_extreme_vol_3x_63d_median_indicator_d2": {"inputs": ["volume"], "func": f19_vblc_010_extreme_vol_3x_63d_median_indicator_d2},
    "f19_vblc_011_extreme_vol_5x_252d_median_indicator_d2": {"inputs": ["volume"], "func": f19_vblc_011_extreme_vol_5x_252d_median_indicator_d2},
    "f19_vblc_012_cum5d_vol_vs_63d_5d_median_d2": {"inputs": ["volume"], "func": f19_vblc_012_cum5d_vol_vs_63d_5d_median_d2},
    "f19_vblc_013_log_vol_robust_z_63d_d2": {"inputs": ["volume"], "func": f19_vblc_013_log_vol_robust_z_63d_d2},
    "f19_vblc_014_log_vol_robust_z_252d_d2": {"inputs": ["volume"], "func": f19_vblc_014_log_vol_robust_z_252d_d2},
    "f19_vblc_015_vol_ratio_to_alltime_max_d2": {"inputs": ["volume"], "func": f19_vblc_015_vol_ratio_to_alltime_max_d2},
    "f19_vblc_016_bars_since_21d_vol_max_d2": {"inputs": ["volume"], "func": f19_vblc_016_bars_since_21d_vol_max_d2},
    "f19_vblc_017_bars_since_63d_vol_max_d2": {"inputs": ["volume"], "func": f19_vblc_017_bars_since_63d_vol_max_d2},
    "f19_vblc_018_bars_since_252d_vol_max_d2": {"inputs": ["volume"], "func": f19_vblc_018_bars_since_252d_vol_max_d2},
    "f19_vblc_019_post_peak_decay_slope_10d_after_21d_max_d2": {"inputs": ["volume"], "func": f19_vblc_019_post_peak_decay_slope_10d_after_21d_max_d2},
    "f19_vblc_020_post_peak_half_life_63d_max_d2": {"inputs": ["volume"], "func": f19_vblc_020_post_peak_half_life_63d_max_d2},
    "f19_vblc_021_climax_then_fade_indicator_21d_d2": {"inputs": ["volume"], "func": f19_vblc_021_climax_then_fade_indicator_21d_d2},
    "f19_vblc_022_post_climax_vol_ratio_post_over_pre_63d_d2": {"inputs": ["volume"], "func": f19_vblc_022_post_climax_vol_ratio_post_over_pre_63d_d2},
    "f19_vblc_023_frac_low_vol_post_climax_21d_63d_d2": {"inputs": ["volume"], "func": f19_vblc_023_frac_low_vol_post_climax_21d_63d_d2},
    "f19_vblc_024_post_climax_decline_pct_10d_63d_d2": {"inputs": ["volume"], "func": f19_vblc_024_post_climax_decline_pct_10d_63d_d2},
    "f19_vblc_025_echo_peak_count_21d_after_63d_max_d2": {"inputs": ["volume"], "func": f19_vblc_025_echo_peak_count_21d_after_63d_max_d2},
    "f19_vblc_026_in_mid_decay_window_5_to_15_bars_63d_d2": {"inputs": ["volume"], "func": f19_vblc_026_in_mid_decay_window_5_to_15_bars_63d_d2},
    "f19_vblc_027_consec_low_vol_bars_post_peak_21d_d2": {"inputs": ["volume"], "func": f19_vblc_027_consec_low_vol_bars_post_peak_21d_d2},
    "f19_vblc_028_post_climax_21d_mean_over_252d_median_d2": {"inputs": ["volume"], "func": f19_vblc_028_post_climax_21d_mean_over_252d_median_d2},
    "f19_vblc_029_climax_hazard_inv_age_252d_d2": {"inputs": ["volume"], "func": f19_vblc_029_climax_hazard_inv_age_252d_d2},
    "f19_vblc_030_log_vol_10d_slope_post_peak_63d_d2": {"inputs": ["volume"], "func": f19_vblc_030_log_vol_10d_slope_post_peak_63d_d2},
    "f19_vblc_031_monotonic_vol_rise_count_21d_d2": {"inputs": ["volume"], "func": f19_vblc_031_monotonic_vol_rise_count_21d_d2},
    "f19_vblc_032_current_monotonic_vol_rise_streak_d2": {"inputs": ["volume"], "func": f19_vblc_032_current_monotonic_vol_rise_streak_d2},
    "f19_vblc_033_cum_vol_5bars_pre_21d_max_d2": {"inputs": ["volume"], "func": f19_vblc_033_cum_vol_5bars_pre_21d_max_d2},
    "f19_vblc_034_cum_vol_21bars_pre_63d_max_d2": {"inputs": ["volume"], "func": f19_vblc_034_cum_vol_21bars_pre_63d_max_d2},
    "f19_vblc_035_log_vol_slope_5bars_pre_21d_max_d2": {"inputs": ["volume"], "func": f19_vblc_035_log_vol_slope_5bars_pre_21d_max_d2},
    "f19_vblc_036_pre5d_over_post5d_cum_vol_at_21d_max_d2": {"inputs": ["volume"], "func": f19_vblc_036_pre5d_over_post5d_cum_vol_at_21d_max_d2},
    "f19_vblc_037_new_21d_vol_high_count_63d_d2": {"inputs": ["volume"], "func": f19_vblc_037_new_21d_vol_high_count_63d_d2},
    "f19_vblc_038_new_63d_vol_high_count_252d_d2": {"inputs": ["volume"], "func": f19_vblc_038_new_63d_vol_high_count_252d_d2},
    "f19_vblc_039_buildup_density_21d_vs_prior_21d_median_d2": {"inputs": ["volume"], "func": f19_vblc_039_buildup_density_21d_vs_prior_21d_median_d2},
    "f19_vblc_040_consec_vol_and_close_rise_streak_d2": {"inputs": ["close", "volume"], "func": f19_vblc_040_consec_vol_and_close_rise_streak_d2},
    "f19_vblc_041_cum21d_vol_zscore_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_041_cum21d_vol_zscore_in_252d_d2},
    "f19_vblc_042_max_log_vol_jump_21d_d2": {"inputs": ["volume"], "func": f19_vblc_042_max_log_vol_jump_21d_d2},
    "f19_vblc_043_log_vol_slope_21d_d2": {"inputs": ["volume"], "func": f19_vblc_043_log_vol_slope_21d_d2},
    "f19_vblc_044_log_vol_slope_63d_d2": {"inputs": ["volume"], "func": f19_vblc_044_log_vol_slope_63d_d2},
    "f19_vblc_045_peak_over_prior_21d_mean_21d_d2": {"inputs": ["volume"], "func": f19_vblc_045_peak_over_prior_21d_mean_21d_d2},
    "f19_vblc_046_burst_3x_63d_median_count_63d_d2": {"inputs": ["volume"], "func": f19_vblc_046_burst_3x_63d_median_count_63d_d2},
    "f19_vblc_047_burst_3x_63d_median_count_252d_d2": {"inputs": ["volume"], "func": f19_vblc_047_burst_3x_63d_median_count_252d_d2},
    "f19_vblc_048_mean_inter_burst_gap_252d_3x_63d_d2": {"inputs": ["volume"], "func": f19_vblc_048_mean_inter_burst_gap_252d_3x_63d_d2},
    "f19_vblc_049_burst_clustering_252d_3x_d2": {"inputs": ["volume"], "func": f19_vblc_049_burst_clustering_252d_3x_d2},
    "f19_vblc_050_max_burst_magnitude_252d_vs_63d_median_d2": {"inputs": ["volume"], "func": f19_vblc_050_max_burst_magnitude_252d_vs_63d_median_d2},
    "f19_vblc_051_bars_since_last_burst_3x_63d_d2": {"inputs": ["volume"], "func": f19_vblc_051_bars_since_last_burst_3x_63d_d2},
    "f19_vblc_052_mean_burst_magnitude_252d_3x_63d_d2": {"inputs": ["volume"], "func": f19_vblc_052_mean_burst_magnitude_252d_3x_63d_d2},
    "f19_vblc_053_burst_then_5d_neg_return_3x_63d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_053_burst_then_5d_neg_return_3x_63d_d2},
    "f19_vblc_054_three_plus_bursts_in_21d_d2": {"inputs": ["volume"], "func": f19_vblc_054_three_plus_bursts_in_21d_d2},
    "f19_vblc_055_first_burst_after_63d_quiet_d2": {"inputs": ["volume"], "func": f19_vblc_055_first_burst_after_63d_quiet_d2},
    "f19_vblc_056_extreme_vs_moderate_burst_ratio_252d_d2": {"inputs": ["volume"], "func": f19_vblc_056_extreme_vs_moderate_burst_ratio_252d_d2},
    "f19_vblc_057_burst_with_price_spike_3x_63d_d2": {"inputs": ["close", "volume"], "func": f19_vblc_057_burst_with_price_spike_3x_63d_d2},
    "f19_vblc_058_climactic_burst_near_252d_max_indicator_d2": {"inputs": ["volume"], "func": f19_vblc_058_climactic_burst_near_252d_max_indicator_d2},
    "f19_vblc_059_burst_freq_change_21d_vs_prior_21d_d2": {"inputs": ["volume"], "func": f19_vblc_059_burst_freq_change_21d_vs_prior_21d_d2},
    "f19_vblc_060_longest_burst_free_interval_252d_3x_63d_d2": {"inputs": ["volume"], "func": f19_vblc_060_longest_burst_free_interval_252d_3x_63d_d2},
    "f19_vblc_061_log_vol_shannon_entropy_63d_d2": {"inputs": ["volume"], "func": f19_vblc_061_log_vol_shannon_entropy_63d_d2},
    "f19_vblc_062_log_vol_shannon_entropy_252d_d2": {"inputs": ["volume"], "func": f19_vblc_062_log_vol_shannon_entropy_252d_d2},
    "f19_vblc_063_volume_gini_63d_d2": {"inputs": ["volume"], "func": f19_vblc_063_volume_gini_63d_d2},
    "f19_vblc_064_volume_gini_252d_d2": {"inputs": ["volume"], "func": f19_vblc_064_volume_gini_252d_d2},
    "f19_vblc_065_top3_share_of_21d_total_vol_d2": {"inputs": ["volume"], "func": f19_vblc_065_top3_share_of_21d_total_vol_d2},
    "f19_vblc_066_top5_share_of_63d_total_vol_d2": {"inputs": ["volume"], "func": f19_vblc_066_top5_share_of_63d_total_vol_d2},
    "f19_vblc_067_top_decile_share_of_252d_total_vol_d2": {"inputs": ["volume"], "func": f19_vblc_067_top_decile_share_of_252d_total_vol_d2},
    "f19_vblc_068_vol_p95_tail_share_63d_d2": {"inputs": ["volume"], "func": f19_vblc_068_vol_p95_tail_share_63d_d2},
    "f19_vblc_069_vol_p95_over_p50_63d_d2": {"inputs": ["volume"], "func": f19_vblc_069_vol_p95_over_p50_63d_d2},
    "f19_vblc_070_vol_cv_63d_d2": {"inputs": ["volume"], "func": f19_vblc_070_vol_cv_63d_d2},
    "f19_vblc_071_vol_cv_252d_d2": {"inputs": ["volume"], "func": f19_vblc_071_vol_cv_252d_d2},
    "f19_vblc_072_log_vol_entropy_21d_change_63d_d2": {"inputs": ["volume"], "func": f19_vblc_072_log_vol_entropy_21d_change_63d_d2},
    "f19_vblc_073_vol_iqr_over_median_63d_d2": {"inputs": ["volume"], "func": f19_vblc_073_vol_iqr_over_median_63d_d2},
    "f19_vblc_074_vol_iqr_over_median_252d_d2": {"inputs": ["volume"], "func": f19_vblc_074_vol_iqr_over_median_252d_d2},
    "f19_vblc_075_log_vol_entropy_zscore_63d_in_252d_d2": {"inputs": ["volume"], "func": f19_vblc_075_log_vol_entropy_zscore_63d_in_252d_d2},
}
