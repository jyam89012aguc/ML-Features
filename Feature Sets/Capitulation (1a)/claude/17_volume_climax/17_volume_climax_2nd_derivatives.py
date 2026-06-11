"""
17_volume_climax — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base volume-climax features — velocity of peak volume,
days-since-climax velocity, climax-magnitude change, recency score change.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _days_since_max(s: pd.Series, w: int) -> pd.Series:
    """Number of bars since the rolling-window maximum occurred."""
    def _dsm(arr):
        idx = int(np.argmax(arr))
        return float(len(arr) - 1 - idx)
    return s.rolling(w, min_periods=max(1, w // 2)).apply(_dsm, raw=True)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vcx_drv2_001_max_vol_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day peak volume (velocity of climax level change)."""
    return _rolling_max(volume, _TD_MON).diff(_TD_WEEK)


def vcx_drv2_002_max_vol_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day peak volume."""
    return _rolling_max(volume, _TD_QTR).diff(_TD_WEEK)


def vcx_drv2_003_max_vol_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day peak volume (monthly change in annual climax)."""
    return _rolling_max(volume, _TD_YEAR).diff(_TD_MON)


def vcx_drv2_004_max_vol_21d_vs_mean_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (21d-peak / 21d-mean) ratio (climax multiple velocity)."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vcx_drv2_005_max_vol_63d_vs_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (63d-peak / 63d-mean) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vcx_drv2_006_days_since_max_vol_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of days-since-63d-climax (aging velocity of the climax event)."""
    return _days_since_max(volume, _TD_QTR).diff(_TD_WEEK)


def vcx_drv2_007_days_since_max_vol_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of days-since-252d-climax."""
    return _days_since_max(volume, _TD_YEAR).diff(_TD_MON)


def vcx_drv2_008_climax_recency_score_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day recency score (rate of climax freshness decay)."""
    dsm = _days_since_max(volume, _TD_QTR)
    recency = (1.0 - dsm / _TD_QTR).clip(lower=0.0)
    return recency.diff(_TD_WEEK)


def vcx_drv2_009_climax_recency_score_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day recency score."""
    dsm = _days_since_max(volume, _TD_YEAR)
    recency = (1.0 - dsm / _TD_YEAR).clip(lower=0.0)
    return recency.diff(_TD_MON)


def vcx_drv2_010_singularity_index_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day singularity index (top1 vs rest gap velocity)."""
    top1 = _rolling_max(volume, _TD_QTR)
    total = _rolling_sum(volume, _TD_QTR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_QTR - 1, index=volume.index, dtype=float))
    singularity = _safe_div(top1 - mean_rest, mean_rest)
    return singularity.diff(_TD_WEEK)


def vcx_drv2_011_singularity_index_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day singularity index."""
    top1 = _rolling_max(volume, _TD_YEAR)
    total = _rolling_sum(volume, _TD_YEAR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_YEAR - 1, index=volume.index, dtype=float))
    singularity = _safe_div(top1 - mean_rest, mean_rest)
    return singularity.diff(_TD_MON)


def vcx_drv2_012_today_vol_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of today's volume z-score vs 252-day distribution."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_WEEK)


def vcx_drv2_013_max_vol_21d_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day-peak z-score within 252-day distribution."""
    mx21 = _rolling_max(volume, _TD_MON)
    m = _rolling_mean(mx21, _TD_YEAR)
    s = _rolling_std(mx21, _TD_YEAR)
    z = _safe_div(mx21 - m, s)
    return z.diff(_TD_WEEK)


def vcx_drv2_014_climax_vol_share_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (peak-day / total-21d) volume share."""
    share = _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return share.diff(_TD_WEEK)


def vcx_drv2_015_climax_vol_share_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (peak-day / total-63d) volume share."""
    share = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return share.diff(_TD_MON)


def vcx_drv2_016_max_vol_21d_vs_252d_ratio_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (21d-peak / 252d-peak) ratio (recency of climax horizon)."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON), _rolling_max(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vcx_drv2_017_max_vol_63d_vs_252d_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (63d-peak / 252d-peak) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_max(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vcx_drv2_018_vol_herfindahl_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day Herfindahl concentration index."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_herf, raw=True)
    return herf.diff(_TD_WEEK)


def vcx_drv2_019_vol_herfindahl_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day Herfindahl concentration index."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_herf, raw=True)
    return herf.diff(_TD_MON)


def vcx_drv2_020_max_vol_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day peak volume over trailing 63 days."""
    return _linslope(_rolling_max(volume, _TD_MON), _TD_QTR)


def vcx_drv2_021_max_vol_63d_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day peak volume over trailing 126 days."""
    return _linslope(_rolling_max(volume, _TD_QTR), _TD_HALF)


def vcx_drv2_022_climax_recency_x_magnitude_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (recency * magnitude) composite for 63-day window."""
    recency = (1.0 - _days_since_max(volume, _TD_QTR) / _TD_QTR).clip(lower=0.0)
    magnitude = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    composite = recency * magnitude
    return composite.diff(_TD_WEEK)


def vcx_drv2_023_climax_recency_x_magnitude_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (recency * magnitude) composite for 252-day window."""
    recency = (1.0 - _days_since_max(volume, _TD_YEAR) / _TD_YEAR).clip(lower=0.0)
    magnitude = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    composite = recency * magnitude
    return composite.diff(_TD_MON)


def vcx_drv2_024_today_vol_pct_rank_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of today's volume percentile rank in 252-day distribution."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vcx_drv2_025_max_vol_63d_pct_rank_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day peak-volume pct rank in 252-day distribution."""
    mx63 = _rolling_max(volume, _TD_QTR)
    rank = mx63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


# --- 2nd-Derivative Extensions (drv2_026-075) ---

def vcx_drv2_026_vol_coeff_variation_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day coefficient of variation of volume."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_WEEK)


def vcx_drv2_027_vol_coeff_variation_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day coefficient of variation of volume."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return cv.diff(_TD_MON)


def vcx_drv2_028_vol_skew_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume skewness."""
    skew = volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()
    return skew.diff(_TD_WEEK)


def vcx_drv2_029_vol_skew_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume skewness."""
    skew = volume.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    return skew.diff(_TD_MON)


def vcx_drv2_030_vol_iqr_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume interquartile range."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    iqr = q75 - q25
    return iqr.diff(_TD_WEEK)


def vcx_drv2_031_vol_iqr_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume interquartile range."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    return iqr.diff(_TD_MON)


def vcx_drv2_032_max_vol_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day peak volume."""
    return _rolling_max(volume, _TD_HALF).diff(_TD_WEEK)


def vcx_drv2_033_max_vol_126d_vs_mean_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (126d-peak / 126d-mean) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))
    return ratio.diff(_TD_MON)


def vcx_drv2_034_climax_vol_share_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (252d-peak / 252d-total) volume share."""
    share = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return share.diff(_TD_MON)


def vcx_drv2_035_vol_p90_vs_mean_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (90th pct / mean) for 21-day volume distribution."""
    p90 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.9)
    ratio = _safe_div(p90, _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vcx_drv2_036_vol_p90_vs_mean_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (90th pct / mean) for 63-day volume distribution."""
    p90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.9)
    ratio = _safe_div(p90, _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vcx_drv2_037_today_vol_vs_ewm21_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (today volume / 21d EMA of volume)."""
    ratio = _safe_div(volume, volume.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    return ratio.diff(_TD_WEEK)


def vcx_drv2_038_today_vol_vs_ewm63_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (today volume / 63d EMA of volume)."""
    ratio = _safe_div(volume, volume.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return ratio.diff(_TD_MON)


def vcx_drv2_039_max_vol_21d_vs_ewm63_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (21d-peak / 63d-EMA) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON),
                      volume.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    return ratio.diff(_TD_WEEK)


def vcx_drv2_040_max_vol_63d_vs_ewm126_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (63d-peak / 126d-EMA) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR),
                      volume.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())
    return ratio.diff(_TD_MON)


def vcx_drv2_041_vol_max_drawdown_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day max-volume drawdown (min / max ratio decline)."""
    mx21 = _rolling_max(volume, _TD_MON)
    mn21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    dd = _safe_div(mn21 - mx21, mx21)
    return dd.diff(_TD_WEEK)


def vcx_drv2_042_vol_max_drawdown_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day max-volume drawdown."""
    mx63 = _rolling_max(volume, _TD_QTR)
    mn63 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    dd = _safe_div(mn63 - mx63, mx63)
    return dd.diff(_TD_MON)


def vcx_drv2_043_climax_vol_share_top3_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of top-3 volume days share of 63-day total."""
    def _top3_sum(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].sum())
    top3 = volume.rolling(_TD_QTR, min_periods=3).apply(_top3_sum, raw=True)
    share = _safe_div(top3, _rolling_sum(volume, _TD_QTR))
    return share.diff(_TD_WEEK)


def vcx_drv2_044_climax_vol_share_top3_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of top-3 volume days share of 252-day total."""
    def _top3_sum(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].sum())
    top3 = volume.rolling(_TD_YEAR, min_periods=3).apply(_top3_sum, raw=True)
    share = _safe_div(top3, _rolling_sum(volume, _TD_YEAR))
    return share.diff(_TD_MON)


def vcx_drv2_045_max_vol_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day peak volume over trailing 21 days (shorter window)."""
    return _linslope(_rolling_max(volume, _TD_MON), _TD_MON)


def vcx_drv2_046_max_vol_252d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 252-day peak volume over trailing 252 days."""
    return _linslope(_rolling_max(volume, _TD_YEAR), _TD_YEAR)


def vcx_drv2_047_days_since_max_vol_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of days-since-21d-climax."""
    return _days_since_max(volume, _TD_MON).diff(_TD_WEEK)


def vcx_drv2_048_days_since_max_vol_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of days-since-126d-climax."""
    return _days_since_max(volume, _TD_HALF).diff(_TD_MON)


def vcx_drv2_049_vol_kurtosis_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume kurtosis."""
    kurt = volume.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    return kurt.diff(_TD_WEEK)


def vcx_drv2_050_vol_kurtosis_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day volume kurtosis."""
    kurt = volume.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()
    return kurt.diff(_TD_MON)


def vcx_drv2_051_vol_above_2x_count_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of count of 2x-mean days in trailing 63d."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cnt = (volume >= 2.0 * mean63).astype(float).rolling(_TD_QTR, min_periods=1).sum()
    return cnt.diff(_TD_WEEK)


def vcx_drv2_052_vol_above_3x_count_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of count of 3x-mean days in trailing 63d."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cnt = (volume >= 3.0 * mean63).astype(float).rolling(_TD_QTR, min_periods=1).sum()
    return cnt.diff(_TD_MON)


def vcx_drv2_053_vol_std_norm_by_max_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (21d std / 21d max) volume normalization."""
    ratio = _safe_div(_rolling_std(volume, _TD_MON), _rolling_max(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vcx_drv2_054_vol_std_norm_by_max_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (63d std / 63d max) volume normalization."""
    ratio = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_max(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vcx_drv2_055_max_vol_21d_zscore_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day peak volume z-score within 63-day distribution."""
    mx21 = _rolling_max(volume, _TD_MON)
    m = _rolling_mean(mx21, _TD_QTR)
    s = _rolling_std(mx21, _TD_QTR)
    z = _safe_div(mx21 - m, s)
    return z.diff(_TD_WEEK)


def vcx_drv2_056_today_vol_zscore_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of today's volume z-score within 63-day distribution."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    return z.diff(_TD_WEEK)


def vcx_drv2_057_vol_herfindahl_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day Herfindahl index over trailing 21 days."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_herf, raw=True)
    return _linslope(herf, _TD_MON)


def vcx_drv2_058_vol_herfindahl_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day Herfindahl index over trailing 63 days."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_herf, raw=True)
    return _linslope(herf, _TD_QTR)


def vcx_drv2_059_max_vol_5d_vs_252d_ratio_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (5d-peak / 252d-peak) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_WEEK), _rolling_max(volume, _TD_YEAR))
    return ratio.diff(_TD_WEEK)


def vcx_drv2_060_max_vol_126d_vs_252d_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (126d-peak / 252d-peak) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_HALF), _rolling_max(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vcx_drv2_061_expanding_max_vol_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of expanding all-time max volume over trailing 21 days."""
    exp_max = volume.expanding(min_periods=1).max()
    return _linslope(exp_max, _TD_MON)


def vcx_drv2_062_expanding_vol_rank_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of expanding percentile rank of today's volume."""
    rank = volume.expanding(min_periods=5).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vcx_drv2_063_vol_max_to_second_log_gap_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log (max/second-max) volume in 21-day window."""
    def _log_gap(arr):
        if len(arr) < 2:
            return np.nan
        top2 = np.partition(arr, -2)[-2:]
        if top2[0] <= 0:
            return np.nan
        return float(np.log(top2[1] / top2[0]))
    gap = volume.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_log_gap, raw=True)
    return gap.diff(_TD_WEEK)


def vcx_drv2_064_vol_max_to_second_log_gap_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of log (max/second-max) volume in 63-day window."""
    def _log_gap(arr):
        if len(arr) < 2:
            return np.nan
        top2 = np.partition(arr, -2)[-2:]
        if top2[0] <= 0:
            return np.nan
        return float(np.log(top2[1] / top2[0]))
    gap = volume.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_log_gap, raw=True)
    return gap.diff(_TD_MON)


def vcx_drv2_065_climax_vol_share_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day peak-day vol share over trailing 63 days."""
    share = _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _linslope(share, _TD_QTR)


def vcx_drv2_066_today_vol_pct_rank_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of today's volume percentile rank in 63-day distribution."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def vcx_drv2_067_vol_above_1pt5x_count_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of count of 1.5x-mean days in trailing 21d."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cnt = (volume >= 1.5 * mean63).astype(float).rolling(_TD_MON, min_periods=1).sum()
    return cnt.diff(_TD_WEEK)


def vcx_drv2_068_climax_recency_score_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day recency score."""
    dsm = _days_since_max(volume, _TD_MON)
    recency = (1.0 - dsm / _TD_MON).clip(lower=0.0)
    return recency.diff(_TD_WEEK)


def vcx_drv2_069_days_since_vol_2x_mean_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of days-since-volume-exceeded-2x-63d-mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above2x = (volume >= 2.0 * mean63).astype(float)
    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    days = above2x.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)
    return days.diff(_TD_WEEK)


def vcx_drv2_070_vol_mean_top3_over_mean_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (mean-top3 / mean) ratio for 21-day window."""
    def _mean_top3(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].mean())
    top3_mean = volume.rolling(_TD_MON, min_periods=3).apply(_mean_top3, raw=True)
    ratio = _safe_div(top3_mean, _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vcx_drv2_071_vol_mean_top3_over_mean_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (mean-top3 / mean) ratio for 63-day window."""
    def _mean_top3(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].mean())
    top3_mean = volume.rolling(_TD_QTR, min_periods=3).apply(_mean_top3, raw=True)
    ratio = _safe_div(top3_mean, _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vcx_drv2_072_climax_count_in_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of count of 21d-max-volume days in trailing 63d."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    cnt = is_climax.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return cnt.diff(_TD_WEEK)


def vcx_drv2_073_climax_count_in_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of count of 21d-max-volume days in trailing 252d."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    cnt = is_climax.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()
    return cnt.diff(_TD_MON)


def vcx_drv2_074_max_vol_21d_5d_log_diff(volume: pd.Series) -> pd.Series:
    """5-day log-diff of 21-day peak volume (log-velocity of climax level)."""
    log_mx = _log_safe(_rolling_max(volume, _TD_MON))
    return log_mx.diff(_TD_WEEK)


def vcx_drv2_075_max_vol_252d_21d_log_diff(volume: pd.Series) -> pd.Series:
    """21-day log-diff of 252-day peak volume."""
    log_mx = _log_safe(_rolling_max(volume, _TD_YEAR))
    return log_mx.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CLIMAX_REGISTRY_2ND_DERIVATIVES = {
    "vcx_drv2_001_max_vol_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_001_max_vol_21d_5d_diff},
    "vcx_drv2_002_max_vol_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_002_max_vol_63d_5d_diff},
    "vcx_drv2_003_max_vol_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_003_max_vol_252d_21d_diff},
    "vcx_drv2_004_max_vol_21d_vs_mean_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_004_max_vol_21d_vs_mean_5d_diff},
    "vcx_drv2_005_max_vol_63d_vs_mean_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_005_max_vol_63d_vs_mean_21d_diff},
    "vcx_drv2_006_days_since_max_vol_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_006_days_since_max_vol_63d_5d_diff},
    "vcx_drv2_007_days_since_max_vol_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_007_days_since_max_vol_252d_21d_diff},
    "vcx_drv2_008_climax_recency_score_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_008_climax_recency_score_63d_5d_diff},
    "vcx_drv2_009_climax_recency_score_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_009_climax_recency_score_252d_21d_diff},
    "vcx_drv2_010_singularity_index_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_010_singularity_index_63d_5d_diff},
    "vcx_drv2_011_singularity_index_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_011_singularity_index_252d_21d_diff},
    "vcx_drv2_012_today_vol_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_012_today_vol_zscore_252d_5d_diff},
    "vcx_drv2_013_max_vol_21d_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_013_max_vol_21d_zscore_252d_5d_diff},
    "vcx_drv2_014_climax_vol_share_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_014_climax_vol_share_21d_5d_diff},
    "vcx_drv2_015_climax_vol_share_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_015_climax_vol_share_63d_21d_diff},
    "vcx_drv2_016_max_vol_21d_vs_252d_ratio_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_016_max_vol_21d_vs_252d_ratio_5d_diff},
    "vcx_drv2_017_max_vol_63d_vs_252d_ratio_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_017_max_vol_63d_vs_252d_ratio_21d_diff},
    "vcx_drv2_018_vol_herfindahl_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_018_vol_herfindahl_21d_5d_diff},
    "vcx_drv2_019_vol_herfindahl_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_019_vol_herfindahl_63d_21d_diff},
    "vcx_drv2_020_max_vol_21d_slope_63d": {"inputs": ["volume"], "func": vcx_drv2_020_max_vol_21d_slope_63d},
    "vcx_drv2_021_max_vol_63d_slope_126d": {"inputs": ["volume"], "func": vcx_drv2_021_max_vol_63d_slope_126d},
    "vcx_drv2_022_climax_recency_x_magnitude_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_022_climax_recency_x_magnitude_63d_5d_diff},
    "vcx_drv2_023_climax_recency_x_magnitude_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_023_climax_recency_x_magnitude_252d_21d_diff},
    "vcx_drv2_024_today_vol_pct_rank_252d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_024_today_vol_pct_rank_252d_5d_diff},
    "vcx_drv2_025_max_vol_63d_pct_rank_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_025_max_vol_63d_pct_rank_252d_21d_diff},
    "vcx_drv2_026_vol_coeff_variation_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_026_vol_coeff_variation_21d_5d_diff},
    "vcx_drv2_027_vol_coeff_variation_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_027_vol_coeff_variation_63d_21d_diff},
    "vcx_drv2_028_vol_skew_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_028_vol_skew_21d_5d_diff},
    "vcx_drv2_029_vol_skew_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_029_vol_skew_63d_21d_diff},
    "vcx_drv2_030_vol_iqr_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_030_vol_iqr_21d_5d_diff},
    "vcx_drv2_031_vol_iqr_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_031_vol_iqr_63d_21d_diff},
    "vcx_drv2_032_max_vol_126d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_032_max_vol_126d_5d_diff},
    "vcx_drv2_033_max_vol_126d_vs_mean_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_033_max_vol_126d_vs_mean_21d_diff},
    "vcx_drv2_034_climax_vol_share_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_034_climax_vol_share_252d_21d_diff},
    "vcx_drv2_035_vol_p90_vs_mean_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_035_vol_p90_vs_mean_21d_5d_diff},
    "vcx_drv2_036_vol_p90_vs_mean_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_036_vol_p90_vs_mean_63d_21d_diff},
    "vcx_drv2_037_today_vol_vs_ewm21_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_037_today_vol_vs_ewm21_5d_diff},
    "vcx_drv2_038_today_vol_vs_ewm63_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_038_today_vol_vs_ewm63_21d_diff},
    "vcx_drv2_039_max_vol_21d_vs_ewm63_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_039_max_vol_21d_vs_ewm63_5d_diff},
    "vcx_drv2_040_max_vol_63d_vs_ewm126_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_040_max_vol_63d_vs_ewm126_21d_diff},
    "vcx_drv2_041_vol_max_drawdown_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_041_vol_max_drawdown_21d_5d_diff},
    "vcx_drv2_042_vol_max_drawdown_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_042_vol_max_drawdown_63d_21d_diff},
    "vcx_drv2_043_climax_vol_share_top3_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_043_climax_vol_share_top3_63d_5d_diff},
    "vcx_drv2_044_climax_vol_share_top3_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_044_climax_vol_share_top3_252d_21d_diff},
    "vcx_drv2_045_max_vol_21d_slope_21d": {"inputs": ["volume"], "func": vcx_drv2_045_max_vol_21d_slope_21d},
    "vcx_drv2_046_max_vol_252d_slope_252d": {"inputs": ["volume"], "func": vcx_drv2_046_max_vol_252d_slope_252d},
    "vcx_drv2_047_days_since_max_vol_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_047_days_since_max_vol_21d_5d_diff},
    "vcx_drv2_048_days_since_max_vol_126d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_048_days_since_max_vol_126d_21d_diff},
    "vcx_drv2_049_vol_kurtosis_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_049_vol_kurtosis_63d_5d_diff},
    "vcx_drv2_050_vol_kurtosis_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_050_vol_kurtosis_252d_21d_diff},
    "vcx_drv2_051_vol_above_2x_count_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_051_vol_above_2x_count_63d_5d_diff},
    "vcx_drv2_052_vol_above_3x_count_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_052_vol_above_3x_count_63d_21d_diff},
    "vcx_drv2_053_vol_std_norm_by_max_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_053_vol_std_norm_by_max_21d_5d_diff},
    "vcx_drv2_054_vol_std_norm_by_max_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_054_vol_std_norm_by_max_63d_21d_diff},
    "vcx_drv2_055_max_vol_21d_zscore_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_055_max_vol_21d_zscore_63d_5d_diff},
    "vcx_drv2_056_today_vol_zscore_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_056_today_vol_zscore_63d_5d_diff},
    "vcx_drv2_057_vol_herfindahl_21d_slope_21d": {"inputs": ["volume"], "func": vcx_drv2_057_vol_herfindahl_21d_slope_21d},
    "vcx_drv2_058_vol_herfindahl_63d_slope_63d": {"inputs": ["volume"], "func": vcx_drv2_058_vol_herfindahl_63d_slope_63d},
    "vcx_drv2_059_max_vol_5d_vs_252d_ratio_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_059_max_vol_5d_vs_252d_ratio_5d_diff},
    "vcx_drv2_060_max_vol_126d_vs_252d_ratio_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_060_max_vol_126d_vs_252d_ratio_21d_diff},
    "vcx_drv2_061_expanding_max_vol_slope_21d": {"inputs": ["volume"], "func": vcx_drv2_061_expanding_max_vol_slope_21d},
    "vcx_drv2_062_expanding_vol_rank_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_062_expanding_vol_rank_5d_diff},
    "vcx_drv2_063_vol_max_to_second_log_gap_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_063_vol_max_to_second_log_gap_21d_5d_diff},
    "vcx_drv2_064_vol_max_to_second_log_gap_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_064_vol_max_to_second_log_gap_63d_21d_diff},
    "vcx_drv2_065_climax_vol_share_21d_slope_63d": {"inputs": ["volume"], "func": vcx_drv2_065_climax_vol_share_21d_slope_63d},
    "vcx_drv2_066_today_vol_pct_rank_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_066_today_vol_pct_rank_63d_5d_diff},
    "vcx_drv2_067_vol_above_1pt5x_count_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_067_vol_above_1pt5x_count_21d_5d_diff},
    "vcx_drv2_068_climax_recency_score_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_068_climax_recency_score_21d_5d_diff},
    "vcx_drv2_069_days_since_vol_2x_mean_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_069_days_since_vol_2x_mean_5d_diff},
    "vcx_drv2_070_vol_mean_top3_over_mean_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_070_vol_mean_top3_over_mean_21d_5d_diff},
    "vcx_drv2_071_vol_mean_top3_over_mean_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_071_vol_mean_top3_over_mean_63d_21d_diff},
    "vcx_drv2_072_climax_count_in_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv2_072_climax_count_in_63d_5d_diff},
    "vcx_drv2_073_climax_count_in_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv2_073_climax_count_in_252d_21d_diff},
    "vcx_drv2_074_max_vol_21d_5d_log_diff": {"inputs": ["volume"], "func": vcx_drv2_074_max_vol_21d_5d_log_diff},
    "vcx_drv2_075_max_vol_252d_21d_log_diff": {"inputs": ["volume"], "func": vcx_drv2_075_max_vol_252d_21d_log_diff},
}
