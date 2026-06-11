"""
17_volume_climax — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative volume-climax features — acceleration of
peak-volume velocity, inflection in recency decay, jerk in singularity index.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vcx_drv3_001_max_vol_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day peak volume (acceleration of climax level)."""
    vel = _rolling_max(volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_002_max_vol_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day peak volume."""
    vel = _rolling_max(volume, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_003_max_vol_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day peak volume (jerk in annual climax)."""
    vel21 = _rolling_max(volume, _TD_YEAR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_004_max_vol_21d_vs_mean_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d-peak / 21d-mean) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_005_max_vol_63d_vs_mean_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (63d-peak / 63d-mean) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_006_days_since_max_vol_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-63d-climax (acceleration of aging)."""
    vel = _days_since_max(volume, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_007_climax_recency_score_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day recency score (jerk in freshness decay)."""
    dsm = _days_since_max(volume, _TD_QTR)
    recency = (1.0 - dsm / _TD_QTR).clip(lower=0.0)
    vel = recency.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_008_climax_recency_score_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day recency score."""
    dsm = _days_since_max(volume, _TD_YEAR)
    recency = (1.0 - dsm / _TD_YEAR).clip(lower=0.0)
    vel21 = recency.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_009_singularity_index_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day singularity index."""
    top1 = _rolling_max(volume, _TD_QTR)
    total = _rolling_sum(volume, _TD_QTR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_QTR - 1, index=volume.index, dtype=float))
    singularity = _safe_div(top1 - mean_rest, mean_rest)
    vel = singularity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_010_singularity_index_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day singularity index."""
    top1 = _rolling_max(volume, _TD_YEAR)
    total = _rolling_sum(volume, _TD_YEAR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_YEAR - 1, index=volume.index, dtype=float))
    singularity = _safe_div(top1 - mean_rest, mean_rest)
    vel21 = singularity.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_011_today_vol_zscore_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of today's volume z-score (acceleration of extremity)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_012_climax_vol_share_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day peak-day volume share."""
    share = _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel = share.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_013_climax_vol_share_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day peak-day volume share."""
    share = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    vel21 = share.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_014_max_vol_21d_vs_252d_ratio_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d-peak / 252d-peak) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON), _rolling_max(volume, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_015_vol_herfindahl_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Herfindahl index (acceleration of concentration)."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_herf, raw=True)
    vel = herf.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_016_vol_herfindahl_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day Herfindahl index."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_herf, raw=True)
    vel21 = herf.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_017_max_vol_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day peak volume over 63-day window."""
    slp = _linslope(_rolling_max(volume, _TD_MON), _TD_QTR)
    return slp.diff(_TD_WEEK)


def vcx_drv3_018_max_vol_63d_slope_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 63-day peak volume over 126-day window."""
    slp = _linslope(_rolling_max(volume, _TD_QTR), _TD_HALF)
    return slp.diff(_TD_WEEK)


def vcx_drv3_019_climax_recency_x_magnitude_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (recency * magnitude) composite for 63-day window."""
    recency = (1.0 - _days_since_max(volume, _TD_QTR) / _TD_QTR).clip(lower=0.0)
    magnitude = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    composite = recency * magnitude
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_020_climax_recency_x_magnitude_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (recency * magnitude) 252-day composite."""
    recency = (1.0 - _days_since_max(volume, _TD_YEAR) / _TD_YEAR).clip(lower=0.0)
    magnitude = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    composite = recency * magnitude
    vel21 = composite.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_021_today_vol_pct_rank_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of today's volume percentile rank in 252-day distribution."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_022_max_vol_21d_zscore_252d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day-peak z-score."""
    mx21 = _rolling_max(volume, _TD_MON)
    m = _rolling_mean(mx21, _TD_YEAR)
    s = _rolling_std(mx21, _TD_YEAR)
    z = _safe_div(mx21 - m, s)
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcx_drv3_023_max_vol_63d_vs_252d_ratio_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (63d-peak / 252d-peak) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_max(volume, _TD_YEAR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_024_climax_vol_share_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day peak-day vol share."""
    share = _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel = share.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcx_drv3_025_days_since_max_vol_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in days-since-252d-climax (jerk in aging)."""
    vel21 = _days_since_max(volume, _TD_YEAR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- 3rd-Derivative Extensions (drv3_026-075) ---

def vcx_drv3_026_vol_coeff_variation_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CV of volume (acceleration of dispersion change)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_027_vol_coeff_variation_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day CV of volume."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_028_vol_skew_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume skewness (jerk in asymmetry)."""
    skew = volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()
    vel = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_029_vol_skew_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day volume skewness."""
    skew = volume.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    vel21 = skew.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_030_vol_iqr_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day IQR of volume."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    iqr = q75 - q25
    vel = iqr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_031_vol_iqr_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day IQR of volume."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    vel21 = iqr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_032_max_vol_126d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day peak volume (acceleration of half-year climax)."""
    vel = _rolling_max(volume, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_033_max_vol_126d_vs_mean_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (126d-peak / 126d-mean) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_034_vol_p90_vs_mean_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d p90 / 21d mean) volume ratio."""
    p90 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.9)
    ratio = _safe_div(p90, _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_035_vol_p90_vs_mean_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (63d p90 / 63d mean) volume ratio."""
    p90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.9)
    ratio = _safe_div(p90, _rolling_mean(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_036_today_vol_vs_ewm21_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (volume / 21d EMA) ratio."""
    ratio = _safe_div(volume, volume.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean())
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_037_today_vol_vs_ewm63_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (volume / 63d EMA) ratio."""
    ratio = _safe_div(volume, volume.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_038_vol_max_drawdown_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume max-drawdown."""
    mx21 = _rolling_max(volume, _TD_MON)
    mn21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    dd = _safe_div(mn21 - mx21, mx21)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_039_vol_max_drawdown_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day volume max-drawdown."""
    mx63 = _rolling_max(volume, _TD_QTR)
    mn63 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    dd = _safe_div(mn63 - mx63, mx63)
    vel21 = dd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_040_max_vol_21d_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 21-day peak volume over 63-day window."""
    slp = _linslope(_rolling_max(volume, _TD_MON), _TD_QTR)
    return slp.diff(_TD_MON)


def vcx_drv3_041_max_vol_63d_slope_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 63-day peak volume over 126-day window."""
    slp = _linslope(_rolling_max(volume, _TD_QTR), _TD_HALF)
    return slp.diff(_TD_MON)


def vcx_drv3_042_vol_kurtosis_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day volume kurtosis (jerk in tail extremity)."""
    kurt = volume.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    vel = kurt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_043_vol_kurtosis_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day volume kurtosis."""
    kurt = volume.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()
    vel21 = kurt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_044_vol_herfindahl_21d_5d_diff_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of 21-day Herfindahl index."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_herf, raw=True)
    vel = herf.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def vcx_drv3_045_vol_herfindahl_63d_21d_diff_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of 63-day Herfindahl index."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_herf, raw=True)
    vel21 = herf.diff(_TD_MON)
    return vel21.diff(_TD_MON)


def vcx_drv3_046_days_since_max_vol_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-21d-climax."""
    vel = _days_since_max(volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_047_days_since_max_vol_126d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in days-since-126d-climax."""
    vel21 = _days_since_max(volume, _TD_HALF).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_048_climax_recency_score_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day recency score."""
    dsm = _days_since_max(volume, _TD_MON)
    recency = (1.0 - dsm / _TD_MON).clip(lower=0.0)
    vel = recency.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_049_vol_above_2x_count_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of count of 2x-mean-volume days in trailing 63d."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cnt = (volume >= 2.0 * mean63).astype(float).rolling(_TD_QTR, min_periods=1).sum()
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_050_vol_above_3x_count_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in count of 3x-mean-volume days in trailing 63d."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cnt = (volume >= 3.0 * mean63).astype(float).rolling(_TD_QTR, min_periods=1).sum()
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_051_max_vol_21d_5d_log_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log-21d-peak volume (log-acceleration)."""
    log_mx = _log_safe(_rolling_max(volume, _TD_MON))
    vel = log_mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_052_max_vol_252d_21d_log_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-diff of 252-day peak volume."""
    log_mx = _log_safe(_rolling_max(volume, _TD_YEAR))
    vel21 = log_mx.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_053_vol_std_norm_max_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d std / 21d max) ratio."""
    ratio = _safe_div(_rolling_std(volume, _TD_MON), _rolling_max(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_054_vol_std_norm_max_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (63d std / 63d max) ratio."""
    ratio = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_max(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_055_climax_vol_share_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (252d-peak / 252d-total) share."""
    share = _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    vel21 = share.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_056_climax_count_in_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of count of 21d-climax days in trailing 63d."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    cnt = is_climax.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_057_climax_count_in_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in count of 21d-climax days in trailing 252d."""
    is_climax = (volume >= _rolling_max(volume, _TD_MON)).astype(float)
    cnt = is_climax.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_058_expanding_vol_rank_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of expanding percentile rank of volume."""
    rank = volume.expanding(min_periods=5).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_059_max_vol_21d_vs_ewm63_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (21d-peak / 63d-EMA) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON),
                      volume.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean())
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_060_max_vol_63d_vs_ewm126_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (63d-peak / 126d-EMA) ratio."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR),
                      volume.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean())
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_061_vol_max_to_second_log_gap_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log (max/second-max) in 21-day window."""
    def _log_gap(arr):
        if len(arr) < 2:
            return np.nan
        top2 = np.partition(arr, -2)[-2:]
        if top2[0] <= 0:
            return np.nan
        return float(np.log(top2[1] / top2[0]))
    gap = volume.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_log_gap, raw=True)
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_062_vol_max_to_second_log_gap_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in log (max/second-max) in 63-day window."""
    def _log_gap(arr):
        if len(arr) < 2:
            return np.nan
        top2 = np.partition(arr, -2)[-2:]
        if top2[0] <= 0:
            return np.nan
        return float(np.log(top2[1] / top2[0]))
    gap = volume.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_log_gap, raw=True)
    vel21 = gap.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_063_climax_vol_share_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day peak-day vol share over 63 days."""
    share = _safe_div(_rolling_max(volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    slp = _linslope(share, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vcx_drv3_064_today_vol_pct_rank_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of today's volume percentile rank in 63-day distribution."""
    rank = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_065_vol_above_1pt5x_count_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of count of 1.5x-mean-volume days in trailing 21d."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cnt = (volume >= 1.5 * mean63).astype(float).rolling(_TD_MON, min_periods=1).sum()
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_066_days_since_vol_2x_mean_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-volume-exceeded-2x-mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    above2x = (volume >= 2.0 * mean63).astype(float)
    def _since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > 0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    days = above2x.rolling(_TD_YEAR, min_periods=1).apply(_since, raw=True)
    vel = days.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_067_vol_mean_top3_over_mean_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of (mean-top3 / mean) for 21-day window."""
    def _mean_top3(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].mean())
    top3_mean = volume.rolling(_TD_MON, min_periods=3).apply(_mean_top3, raw=True)
    ratio = _safe_div(top3_mean, _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_068_vol_mean_top3_over_mean_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in (mean-top3 / mean) for 63-day window."""
    def _mean_top3(arr):
        if len(arr) < 3:
            return np.nan
        return float(np.partition(arr, -3)[-3:].mean())
    top3_mean = volume.rolling(_TD_QTR, min_periods=3).apply(_mean_top3, raw=True)
    ratio = _safe_div(top3_mean, _rolling_mean(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_069_singularity_index_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day singularity index."""
    top1 = _rolling_max(volume, _TD_QTR)
    total = _rolling_sum(volume, _TD_QTR)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_QTR - 1, index=volume.index, dtype=float))
    singularity = _safe_div(top1 - mean_rest, mean_rest)
    vel21 = singularity.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vcx_drv3_070_singularity_index_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day singularity index."""
    top1 = _rolling_max(volume, _TD_MON)
    total = _rolling_sum(volume, _TD_MON)
    mean_rest = _safe_div(total - top1, pd.Series(_TD_MON - 1, index=volume.index, dtype=float))
    singularity = _safe_div(top1 - mean_rest, mean_rest)
    vel = singularity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcx_drv3_071_max_vol_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day peak volume over 21-day window."""
    slp = _linslope(_rolling_max(volume, _TD_MON), _TD_MON)
    return slp.diff(_TD_WEEK)


def vcx_drv3_072_max_vol_252d_slope_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 252-day peak volume over 252-day window."""
    slp = _linslope(_rolling_max(volume, _TD_YEAR), _TD_YEAR)
    return slp.diff(_TD_MON)


def vcx_drv3_073_expanding_max_vol_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of expanding all-time max volume over 21 days."""
    exp_max = volume.expanding(min_periods=1).max()
    slp = _linslope(exp_max, _TD_MON)
    return slp.diff(_TD_WEEK)


def vcx_drv3_074_vol_herfindahl_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day Herfindahl over trailing 21 days."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_herf, raw=True)
    slp = _linslope(herf, _TD_MON)
    return slp.diff(_TD_WEEK)


def vcx_drv3_075_vol_herfindahl_63d_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 63-day Herfindahl over trailing 63 days."""
    def _herf(arr):
        t = arr.sum()
        if t == 0:
            return np.nan
        shares = arr / t
        return float((shares ** 2).sum())
    herf = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_herf, raw=True)
    slp = _linslope(herf, _TD_QTR)
    return slp.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CLIMAX_REGISTRY_3RD_DERIVATIVES = {
    "vcx_drv3_001_max_vol_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_001_max_vol_21d_5d_diff_5d_diff},
    "vcx_drv3_002_max_vol_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_002_max_vol_63d_5d_diff_5d_diff},
    "vcx_drv3_003_max_vol_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_003_max_vol_252d_21d_diff_5d_diff},
    "vcx_drv3_004_max_vol_21d_vs_mean_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_004_max_vol_21d_vs_mean_5d_diff_5d_diff},
    "vcx_drv3_005_max_vol_63d_vs_mean_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_005_max_vol_63d_vs_mean_21d_diff_5d_diff},
    "vcx_drv3_006_days_since_max_vol_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_006_days_since_max_vol_63d_5d_diff_5d_diff},
    "vcx_drv3_007_climax_recency_score_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_007_climax_recency_score_63d_5d_diff_5d_diff},
    "vcx_drv3_008_climax_recency_score_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_008_climax_recency_score_252d_21d_diff_5d_diff},
    "vcx_drv3_009_singularity_index_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_009_singularity_index_63d_5d_diff_5d_diff},
    "vcx_drv3_010_singularity_index_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_010_singularity_index_252d_21d_diff_5d_diff},
    "vcx_drv3_011_today_vol_zscore_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_011_today_vol_zscore_252d_5d_diff_5d_diff},
    "vcx_drv3_012_climax_vol_share_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_012_climax_vol_share_21d_5d_diff_5d_diff},
    "vcx_drv3_013_climax_vol_share_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_013_climax_vol_share_63d_21d_diff_5d_diff},
    "vcx_drv3_014_max_vol_21d_vs_252d_ratio_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_014_max_vol_21d_vs_252d_ratio_5d_diff_5d_diff},
    "vcx_drv3_015_vol_herfindahl_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_015_vol_herfindahl_21d_5d_diff_5d_diff},
    "vcx_drv3_016_vol_herfindahl_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_016_vol_herfindahl_63d_21d_diff_5d_diff},
    "vcx_drv3_017_max_vol_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_017_max_vol_21d_slope_63d_5d_diff},
    "vcx_drv3_018_max_vol_63d_slope_126d_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_018_max_vol_63d_slope_126d_5d_diff},
    "vcx_drv3_019_climax_recency_x_magnitude_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_019_climax_recency_x_magnitude_63d_5d_diff_5d_diff},
    "vcx_drv3_020_climax_recency_x_magnitude_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_020_climax_recency_x_magnitude_252d_21d_diff_5d_diff},
    "vcx_drv3_021_today_vol_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_021_today_vol_pct_rank_252d_5d_diff_5d_diff},
    "vcx_drv3_022_max_vol_21d_zscore_252d_slope_21d": {"inputs": ["volume"], "func": vcx_drv3_022_max_vol_21d_zscore_252d_slope_21d},
    "vcx_drv3_023_max_vol_63d_vs_252d_ratio_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_023_max_vol_63d_vs_252d_ratio_21d_diff_5d_diff},
    "vcx_drv3_024_climax_vol_share_21d_slope_21d": {"inputs": ["volume"], "func": vcx_drv3_024_climax_vol_share_21d_slope_21d},
    "vcx_drv3_025_days_since_max_vol_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_025_days_since_max_vol_252d_21d_diff_5d_diff},
    "vcx_drv3_026_vol_coeff_variation_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_026_vol_coeff_variation_21d_5d_diff_5d_diff},
    "vcx_drv3_027_vol_coeff_variation_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_027_vol_coeff_variation_63d_21d_diff_5d_diff},
    "vcx_drv3_028_vol_skew_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_028_vol_skew_21d_5d_diff_5d_diff},
    "vcx_drv3_029_vol_skew_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_029_vol_skew_63d_21d_diff_5d_diff},
    "vcx_drv3_030_vol_iqr_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_030_vol_iqr_21d_5d_diff_5d_diff},
    "vcx_drv3_031_vol_iqr_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_031_vol_iqr_63d_21d_diff_5d_diff},
    "vcx_drv3_032_max_vol_126d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_032_max_vol_126d_5d_diff_5d_diff},
    "vcx_drv3_033_max_vol_126d_vs_mean_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_033_max_vol_126d_vs_mean_21d_diff_5d_diff},
    "vcx_drv3_034_vol_p90_vs_mean_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_034_vol_p90_vs_mean_21d_5d_diff_5d_diff},
    "vcx_drv3_035_vol_p90_vs_mean_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_035_vol_p90_vs_mean_63d_21d_diff_5d_diff},
    "vcx_drv3_036_today_vol_vs_ewm21_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_036_today_vol_vs_ewm21_5d_diff_5d_diff},
    "vcx_drv3_037_today_vol_vs_ewm63_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_037_today_vol_vs_ewm63_21d_diff_5d_diff},
    "vcx_drv3_038_vol_max_drawdown_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_038_vol_max_drawdown_21d_5d_diff_5d_diff},
    "vcx_drv3_039_vol_max_drawdown_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_039_vol_max_drawdown_63d_21d_diff_5d_diff},
    "vcx_drv3_040_max_vol_21d_slope_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv3_040_max_vol_21d_slope_63d_21d_diff},
    "vcx_drv3_041_max_vol_63d_slope_126d_21d_diff": {"inputs": ["volume"], "func": vcx_drv3_041_max_vol_63d_slope_126d_21d_diff},
    "vcx_drv3_042_vol_kurtosis_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_042_vol_kurtosis_63d_5d_diff_5d_diff},
    "vcx_drv3_043_vol_kurtosis_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_043_vol_kurtosis_252d_21d_diff_5d_diff},
    "vcx_drv3_044_vol_herfindahl_21d_5d_diff_21d_diff": {"inputs": ["volume"], "func": vcx_drv3_044_vol_herfindahl_21d_5d_diff_21d_diff},
    "vcx_drv3_045_vol_herfindahl_63d_21d_diff_21d_diff": {"inputs": ["volume"], "func": vcx_drv3_045_vol_herfindahl_63d_21d_diff_21d_diff},
    "vcx_drv3_046_days_since_max_vol_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_046_days_since_max_vol_21d_5d_diff_5d_diff},
    "vcx_drv3_047_days_since_max_vol_126d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_047_days_since_max_vol_126d_21d_diff_5d_diff},
    "vcx_drv3_048_climax_recency_score_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_048_climax_recency_score_21d_5d_diff_5d_diff},
    "vcx_drv3_049_vol_above_2x_count_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_049_vol_above_2x_count_63d_5d_diff_5d_diff},
    "vcx_drv3_050_vol_above_3x_count_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_050_vol_above_3x_count_63d_21d_diff_5d_diff},
    "vcx_drv3_051_max_vol_21d_5d_log_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_051_max_vol_21d_5d_log_diff_5d_diff},
    "vcx_drv3_052_max_vol_252d_21d_log_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_052_max_vol_252d_21d_log_diff_5d_diff},
    "vcx_drv3_053_vol_std_norm_max_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_053_vol_std_norm_max_21d_5d_diff_5d_diff},
    "vcx_drv3_054_vol_std_norm_max_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_054_vol_std_norm_max_63d_21d_diff_5d_diff},
    "vcx_drv3_055_climax_vol_share_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_055_climax_vol_share_252d_21d_diff_5d_diff},
    "vcx_drv3_056_climax_count_in_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_056_climax_count_in_63d_5d_diff_5d_diff},
    "vcx_drv3_057_climax_count_in_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_057_climax_count_in_252d_21d_diff_5d_diff},
    "vcx_drv3_058_expanding_vol_rank_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_058_expanding_vol_rank_5d_diff_5d_diff},
    "vcx_drv3_059_max_vol_21d_vs_ewm63_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_059_max_vol_21d_vs_ewm63_5d_diff_5d_diff},
    "vcx_drv3_060_max_vol_63d_vs_ewm126_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_060_max_vol_63d_vs_ewm126_21d_diff_5d_diff},
    "vcx_drv3_061_vol_max_to_second_log_gap_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_061_vol_max_to_second_log_gap_21d_5d_diff_5d_diff},
    "vcx_drv3_062_vol_max_to_second_log_gap_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_062_vol_max_to_second_log_gap_63d_21d_diff_5d_diff},
    "vcx_drv3_063_climax_vol_share_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_063_climax_vol_share_21d_slope_63d_5d_diff},
    "vcx_drv3_064_today_vol_pct_rank_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_064_today_vol_pct_rank_63d_5d_diff_5d_diff},
    "vcx_drv3_065_vol_above_1pt5x_count_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_065_vol_above_1pt5x_count_21d_5d_diff_5d_diff},
    "vcx_drv3_066_days_since_vol_2x_mean_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_066_days_since_vol_2x_mean_5d_diff_5d_diff},
    "vcx_drv3_067_vol_mean_top3_over_mean_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_067_vol_mean_top3_over_mean_21d_5d_diff_5d_diff},
    "vcx_drv3_068_vol_mean_top3_over_mean_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_068_vol_mean_top3_over_mean_63d_21d_diff_5d_diff},
    "vcx_drv3_069_singularity_index_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_069_singularity_index_63d_21d_diff_5d_diff},
    "vcx_drv3_070_singularity_index_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_070_singularity_index_21d_5d_diff_5d_diff},
    "vcx_drv3_071_max_vol_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_071_max_vol_21d_slope_21d_5d_diff},
    "vcx_drv3_072_max_vol_252d_slope_252d_21d_diff": {"inputs": ["volume"], "func": vcx_drv3_072_max_vol_252d_slope_252d_21d_diff},
    "vcx_drv3_073_expanding_max_vol_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_073_expanding_max_vol_slope_21d_5d_diff},
    "vcx_drv3_074_vol_herfindahl_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcx_drv3_074_vol_herfindahl_21d_slope_21d_5d_diff},
    "vcx_drv3_075_vol_herfindahl_63d_slope_63d_21d_diff": {"inputs": ["volume"], "func": vcx_drv3_075_vol_herfindahl_63d_slope_63d_21d_diff},
}
