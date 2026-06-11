"""
15_volume_blowoff — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base volume-blowoff features — velocity / acceleration
of spike ratios, spike counts, z-scores, and composite blowoff indices.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _vol_ratio_vs_median(volume: pd.Series, w: int) -> pd.Series:
    return _safe_div(volume, _rolling_median(volume, w))


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s)


def _spike_flag_median(volume: pd.Series, w: int, thresh: float) -> pd.Series:
    return (_vol_ratio_vs_median(volume, w) > thresh).astype(float)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vb_drv2_001_vol_ratio_median_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/21d-median ratio (velocity of blowoff ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.diff(_TD_WEEK)


def vb_drv2_002_vol_ratio_median_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/21d-median ratio (monthly velocity of blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.diff(_TD_MON)


def vb_drv2_003_vol_zscore_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume z-score (velocity of z-score)."""
    z = _vol_zscore(volume, _TD_MON)
    return z.diff(_TD_WEEK)


def vb_drv2_004_vol_zscore_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume z-score (monthly velocity of quarterly z-score)."""
    z = _vol_zscore(volume, _TD_QTR)
    return z.diff(_TD_MON)


def vb_drv2_005_spike_count_2x_median_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day 2x-spike count (velocity of spike frequency)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_MON)
    return cnt.diff(_TD_WEEK)


def vb_drv2_006_spike_count_2x_median_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day 2x-spike count (monthly velocity of quarterly spike count)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_QTR)
    return cnt.diff(_TD_MON)


def vb_drv2_007_max_spike_ratio_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day max spike ratio (velocity of peak blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx63 = _rolling_max(ratio, _TD_QTR)
    return mx63.diff(_TD_WEEK)


def vb_drv2_008_max_spike_ratio_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day max spike ratio (monthly change in all-year peak)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    return mx252.diff(_TD_MON)


def vb_drv2_009_spike_cluster_score_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day spike cluster score (velocity of accumulated blowoff energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_QTR)
    return cluster.diff(_TD_MON)


def vb_drv2_010_vol_ratio_mean_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/21d-mean ratio (velocity of mean-based blowoff ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vb_drv2_011_vol_ratio_mean_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/63d-mean ratio (monthly velocity of quarterly mean ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vb_drv2_012_log_vol_ratio_median_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log(vol/21d-median) (velocity on log scale)."""
    log_ratio = np.log1p(_vol_ratio_vs_median(volume, _TD_MON))
    return log_ratio.diff(_TD_WEEK)


def vb_drv2_013_spike_count_down_days_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day spike-on-down-days count (velocity of panic selling)."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    return cnt.diff(_TD_MON)


def vb_drv2_014_spike_ratio_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of spike-ratio z-score vs 252d distribution (velocity of extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    z = _safe_div(ratio - m, s)
    return z.diff(_TD_WEEK)


def vb_drv2_015_spike_ratio_median_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/21d-median ratio over trailing 21 days (trend in ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _linslope(ratio, _TD_MON)


def vb_drv2_016_spike_ratio_median_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/21d-median ratio over trailing 63 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _linslope(ratio, _TD_QTR)


def vb_drv2_017_vol_zscore_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day volume z-score over trailing 21 days."""
    z = _vol_zscore(volume, _TD_MON)
    return _linslope(z, _TD_MON)


def vb_drv2_018_spike_cluster_score_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day spike cluster score (short-term velocity of cluster intensity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_MON)
    return cluster.diff(_TD_WEEK)


def vb_drv2_019_blowoff_composite_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day composite blowoff score (velocity of composite signal)."""
    z_rank = _vol_zscore(volume, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    r_rank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    c_rank = _rolling_count_true(flag > 0, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    composite = (z_rank + r_rank + c_rank) / 3.0
    return composite.diff(_TD_WEEK)


def vb_drv2_020_max_vol_ratio_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day max vol/21d-median ratio (velocity of recent spike peak)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _rolling_max(ratio, _TD_QTR).diff(_TD_WEEK)


def vb_drv2_021_vol_mean_vs_median_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d mean/median ratio (velocity of spike-skew indicator)."""
    skew = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    return skew.diff(_TD_WEEK)


def vb_drv2_022_excess_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of sum of excess-above-2x-median over 63d (velocity of blowoff energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_QTR)
    return excess.diff(_TD_MON)


def vb_drv2_023_spike_down_up_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day spike-on-down/spike-on-up ratio."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    dn = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    up = _rolling_count_true(((flag > 0) & (ret > 0)), _TD_QTR)
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_MON)


def vb_drv2_024_vol_ratio_median_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/63d-median ratio (monthly velocity of quarterly ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_QTR)
    return ratio.diff(_TD_MON)


def vb_drv2_025_spike_count_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day 2x-spike count (monthly velocity of annual spike count)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_YEAR)
    return cnt.diff(_TD_MON)


# --- drv2_026-075: Extended 2nd derivatives ---

def vb_drv2_026_vol_ratio_median_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/126d-median ratio (monthly velocity of half-year ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_HALF)
    return ratio.diff(_TD_MON)


def vb_drv2_027_vol_ratio_median_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/252d-median ratio (monthly velocity of annual ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_YEAR)
    return ratio.diff(_TD_MON)


def vb_drv2_028_vol_zscore_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume z-score (velocity of half-year z-score)."""
    z = _vol_zscore(volume, _TD_HALF)
    return z.diff(_TD_MON)


def vb_drv2_029_vol_zscore_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day volume z-score (monthly velocity of annual z-score)."""
    z = _vol_zscore(volume, _TD_YEAR)
    return z.diff(_TD_MON)


def vb_drv2_030_spike_count_3x_median_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day 3x-spike count (velocity of extreme spike frequency)."""
    flag = _spike_flag_median(volume, _TD_MON, 3.0)
    cnt = _rolling_count_true(flag > 0, _TD_QTR)
    return cnt.diff(_TD_MON)


def vb_drv2_031_spike_count_3x_median_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day 3x-spike count (velocity of annual extreme spike rate)."""
    flag = _spike_flag_median(volume, _TD_MON, 3.0)
    cnt = _rolling_count_true(flag > 0, _TD_YEAR)
    return cnt.diff(_TD_MON)


def vb_drv2_032_max_spike_ratio_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 126-day max spike ratio (velocity of half-year peak blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx126 = _rolling_max(ratio, _TD_HALF)
    return mx126.diff(_TD_WEEK)


def vb_drv2_033_max_spike_ratio_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252-day max spike ratio (ultra-short velocity of annual peak)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    return mx252.diff(_TD_WEEK)


def vb_drv2_034_spike_cluster_score_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day spike cluster score (velocity of annual blowoff energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_YEAR)
    return cluster.diff(_TD_MON)


def vb_drv2_035_vol_mean_vs_median_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63d mean/median ratio (velocity of quarterly spike-skew)."""
    skew = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    return skew.diff(_TD_WEEK)


def vb_drv2_036_vol_mean_vs_median_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252d mean/median ratio (velocity of annual skew indicator)."""
    skew = _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_median(volume, _TD_YEAR))
    return skew.diff(_TD_MON)


def vb_drv2_037_excess_ratio_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of sum of excess-above-2x-median over 21d (velocity of short energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_MON)
    return excess.diff(_TD_WEEK)


def vb_drv2_038_excess_ratio_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day excess blowoff energy (velocity of annual accumulation)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_YEAR)
    return excess.diff(_TD_MON)


def vb_drv2_039_spike_ratio_zscore_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of spike-ratio z-score vs 252d distribution (velocity of extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    z = _safe_div(ratio - m, s)
    return z.diff(_TD_MON)


def vb_drv2_040_log_vol_ratio_median_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of log(vol/21d-median) (monthly velocity on log scale)."""
    log_ratio = np.log1p(_vol_ratio_vs_median(volume, _TD_MON))
    return log_ratio.diff(_TD_MON)


def vb_drv2_041_spike_ratio_median_21d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/21d-median ratio over trailing 252 days (annual trend in ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _linslope(ratio, _TD_YEAR)


def vb_drv2_042_vol_zscore_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day volume z-score over trailing 63 days (quarterly z-score trend)."""
    z = _vol_zscore(volume, _TD_MON)
    return _linslope(z, _TD_QTR)


def vb_drv2_043_vol_zscore_63d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day volume z-score over trailing 21 days (short quarterly trend)."""
    z = _vol_zscore(volume, _TD_QTR)
    return _linslope(z, _TD_MON)


def vb_drv2_044_vol_zscore_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day volume z-score over trailing 63 days."""
    z = _vol_zscore(volume, _TD_QTR)
    return _linslope(z, _TD_QTR)


def vb_drv2_045_spike_cluster_score_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day spike cluster score (monthly velocity of short cluster)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_MON)
    return cluster.diff(_TD_MON)


def vb_drv2_046_blowoff_composite_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day composite blowoff score (monthly velocity of composite)."""
    z_rank = _vol_zscore(volume, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    r_rank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    c_rank = _rolling_count_true(flag > 0, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    composite = (z_rank + r_rank + c_rank) / 3.0
    return composite.diff(_TD_MON)


def vb_drv2_047_spike_vol_turnover_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day spike volume turnover fraction (velocity of turnover share)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    turnover = _safe_div(_rolling_sum(spike_vol, _TD_MON), _rolling_sum(volume, _TD_MON))
    return turnover.diff(_TD_WEEK)


def vb_drv2_048_spike_vol_turnover_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day spike volume turnover fraction."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    turnover = _safe_div(_rolling_sum(spike_vol, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return turnover.diff(_TD_MON)


def vb_drv2_049_vol_iqr_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume IQR/median ratio (velocity of spike dispersion)."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr = _safe_div(q75 - q25, med)
    return iqr.diff(_TD_WEEK)


def vb_drv2_050_vol_iqr_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume IQR/median ratio (velocity of quarterly dispersion)."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    med = _rolling_median(volume, _TD_QTR)
    iqr = _safe_div(q75 - q25, med)
    return iqr.diff(_TD_MON)


def vb_drv2_051_vol_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day coefficient of variation (velocity of spike dispersion CV)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_WEEK)


def vb_drv2_052_vol_cv_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day coefficient of variation (monthly velocity of quarterly CV)."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return cv.diff(_TD_MON)


def vb_drv2_053_spike_ratio_median_63d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/63d-median ratio over trailing 21 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_QTR)
    return _linslope(ratio, _TD_MON)


def vb_drv2_054_spike_ratio_median_63d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/63d-median ratio over trailing 63 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_QTR)
    return _linslope(ratio, _TD_QTR)


def vb_drv2_055_spike_ratio_pct_rank_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of spike ratio in 252d distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    prank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return prank.diff(_TD_WEEK)


def vb_drv2_056_spike_ratio_pct_rank_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of percentile rank of spike ratio in 252d distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    prank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return prank.diff(_TD_MON)


def vb_drv2_057_vol_zscore_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 252-day volume z-score (ultra-short velocity of annual z-score)."""
    z = _vol_zscore(volume, _TD_YEAR)
    return z.diff(_TD_WEEK)


def vb_drv2_058_log_vol_zscore_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log-volume z-score vs 21d baseline (velocity of log-zscore)."""
    lv = np.log(volume.clip(lower=1e-9))
    m = _rolling_mean(lv, _TD_MON)
    s = _rolling_std(lv, _TD_MON)
    z = _safe_div(lv - m, s)
    return z.diff(_TD_WEEK)


def vb_drv2_059_log_vol_zscore_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of log-volume z-score vs 63d baseline."""
    lv = np.log(volume.clip(lower=1e-9))
    m = _rolling_mean(lv, _TD_QTR)
    s = _rolling_std(lv, _TD_QTR)
    z = _safe_div(lv - m, s)
    return z.diff(_TD_MON)


def vb_drv2_060_spike_asymmetry_ratio_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of down/up spike mean ratio over 63d (velocity of panic asymmetry)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    dn_mean = ratio.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_mean = ratio.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    asym = _safe_div(dn_mean, up_mean)
    return asym.diff(_TD_MON)


def vb_drv2_061_spike_down_up_ratio_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day spike-on-down/spike-on-up ratio."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    dn = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_YEAR)
    up = _rolling_count_true(((flag > 0) & (ret > 0)), _TD_YEAR)
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_MON)


def vb_drv2_062_spike_count_down_days_252d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day spike-on-down-days count."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_YEAR)
    return cnt.diff(_TD_MON)


def vb_drv2_063_vol_ratio_mean_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of vol/252d-mean ratio (velocity of annual mean ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return ratio.diff(_TD_MON)


def vb_drv2_064_vol_ratio_mean_126d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of vol/126d-mean ratio (velocity of half-year mean ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_HALF))
    return ratio.diff(_TD_WEEK)


def vb_drv2_065_spike_vol_turnover_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d spike volume turnover (monthly velocity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    turnover = _safe_div(_rolling_sum(spike_vol, _TD_MON), _rolling_sum(volume, _TD_MON))
    return turnover.diff(_TD_MON)


def vb_drv2_066_spike_ratio_ewm21_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EWM21 spike ratio (velocity of smoothed blowoff signal)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ewm = _safe_div(volume, _rolling_mean(volume, _TD_MON)).ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return ewm.diff(_TD_WEEK)


def vb_drv2_067_spike_ratio_ewm63_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EWM63 spike ratio (velocity of quarterly smoothed blowoff)."""
    ewm = _vol_ratio_vs_median(volume, _TD_MON).ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return ewm.diff(_TD_MON)


def vb_drv2_068_spike_cluster_density_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day spike cluster density (velocity of spike day fraction)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    density = _rolling_count_true(flag > 0, _TD_MON) / _TD_MON
    return density.diff(_TD_WEEK)


def vb_drv2_069_spike_cluster_density_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day spike cluster density."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    density = _rolling_count_true(flag > 0, _TD_QTR) / _TD_QTR
    return density.diff(_TD_MON)


def vb_drv2_070_vol_90th_pct_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 90th-percentile/median ratio over 63d (velocity of tail spike height)."""
    p90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.90)
    med = _rolling_median(volume, _TD_QTR)
    tail = _safe_div(p90, med)
    return tail.diff(_TD_WEEK)


def vb_drv2_071_vol_95th_pct_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 95th-percentile/median ratio over 252d."""
    p95 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    med = _rolling_median(volume, _TD_YEAR)
    tail = _safe_div(p95, med)
    return tail.diff(_TD_MON)


def vb_drv2_072_spike_recency_score_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of spike recency score (velocity of decay-weighted spike signal)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    decay = 0.3
    weights = np.array([np.exp(-decay * k) for k in range(_TD_MON)])
    def _weighted_sum(arr):
        n = len(arr)
        w = weights[:n][::-1]
        return float(np.dot(arr, w))
    recency = flag.rolling(_TD_MON, min_periods=1).apply(_weighted_sum, raw=True)
    return recency.diff(_TD_WEEK)


def vb_drv2_073_spike_surprise_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day spike surprise index (velocity of ratio vs norm)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    surprise = ratio - _rolling_mean(ratio, _TD_MON)
    return surprise.diff(_TD_WEEK)


def vb_drv2_074_spike_surprise_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day spike surprise index (velocity of quarterly deviation)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    surprise = ratio - _rolling_mean(ratio, _TD_QTR)
    return surprise.diff(_TD_MON)


def vb_drv2_075_vol_ratio_median_21d_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of vol/21d-median ratio over trailing 126 days (half-year trend)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _linslope(ratio, _TD_HALF)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_BLOWOFF_REGISTRY_2ND_DERIVATIVES = {
    "vb_drv2_001_vol_ratio_median_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_001_vol_ratio_median_21d_5d_diff},
    "vb_drv2_002_vol_ratio_median_21d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_002_vol_ratio_median_21d_21d_diff},
    "vb_drv2_003_vol_zscore_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_003_vol_zscore_21d_5d_diff},
    "vb_drv2_004_vol_zscore_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_004_vol_zscore_63d_21d_diff},
    "vb_drv2_005_spike_count_2x_median_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_005_spike_count_2x_median_21d_5d_diff},
    "vb_drv2_006_spike_count_2x_median_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_006_spike_count_2x_median_63d_21d_diff},
    "vb_drv2_007_max_spike_ratio_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_007_max_spike_ratio_63d_5d_diff},
    "vb_drv2_008_max_spike_ratio_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_008_max_spike_ratio_252d_21d_diff},
    "vb_drv2_009_spike_cluster_score_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_009_spike_cluster_score_63d_21d_diff},
    "vb_drv2_010_vol_ratio_mean_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_010_vol_ratio_mean_21d_5d_diff},
    "vb_drv2_011_vol_ratio_mean_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_011_vol_ratio_mean_63d_21d_diff},
    "vb_drv2_012_log_vol_ratio_median_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_012_log_vol_ratio_median_21d_5d_diff},
    "vb_drv2_013_spike_count_down_days_63d_21d_diff": {"inputs": ["close", "volume"], "func": vb_drv2_013_spike_count_down_days_63d_21d_diff},
    "vb_drv2_014_spike_ratio_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_014_spike_ratio_zscore_252d_5d_diff},
    "vb_drv2_015_spike_ratio_median_21d_slope_21d": {"inputs": ["volume"], "func": vb_drv2_015_spike_ratio_median_21d_slope_21d},
    "vb_drv2_016_spike_ratio_median_21d_slope_63d": {"inputs": ["volume"], "func": vb_drv2_016_spike_ratio_median_21d_slope_63d},
    "vb_drv2_017_vol_zscore_21d_slope_21d": {"inputs": ["volume"], "func": vb_drv2_017_vol_zscore_21d_slope_21d},
    "vb_drv2_018_spike_cluster_score_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_018_spike_cluster_score_21d_5d_diff},
    "vb_drv2_019_blowoff_composite_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_019_blowoff_composite_21d_5d_diff},
    "vb_drv2_020_max_vol_ratio_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_020_max_vol_ratio_63d_5d_diff},
    "vb_drv2_021_vol_mean_vs_median_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_021_vol_mean_vs_median_21d_5d_diff},
    "vb_drv2_022_excess_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_022_excess_ratio_63d_21d_diff},
    "vb_drv2_023_spike_down_up_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": vb_drv2_023_spike_down_up_ratio_63d_21d_diff},
    "vb_drv2_024_vol_ratio_median_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_024_vol_ratio_median_63d_21d_diff},
    "vb_drv2_025_spike_count_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_025_spike_count_252d_21d_diff},
    "vb_drv2_026_vol_ratio_median_126d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_026_vol_ratio_median_126d_21d_diff},
    "vb_drv2_027_vol_ratio_median_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_027_vol_ratio_median_252d_21d_diff},
    "vb_drv2_028_vol_zscore_126d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_028_vol_zscore_126d_21d_diff},
    "vb_drv2_029_vol_zscore_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_029_vol_zscore_252d_21d_diff},
    "vb_drv2_030_spike_count_3x_median_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_030_spike_count_3x_median_63d_21d_diff},
    "vb_drv2_031_spike_count_3x_median_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_031_spike_count_3x_median_252d_21d_diff},
    "vb_drv2_032_max_spike_ratio_126d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_032_max_spike_ratio_126d_5d_diff},
    "vb_drv2_033_max_spike_ratio_252d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_033_max_spike_ratio_252d_5d_diff},
    "vb_drv2_034_spike_cluster_score_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_034_spike_cluster_score_252d_21d_diff},
    "vb_drv2_035_vol_mean_vs_median_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_035_vol_mean_vs_median_63d_5d_diff},
    "vb_drv2_036_vol_mean_vs_median_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_036_vol_mean_vs_median_252d_21d_diff},
    "vb_drv2_037_excess_ratio_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_037_excess_ratio_21d_5d_diff},
    "vb_drv2_038_excess_ratio_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_038_excess_ratio_252d_21d_diff},
    "vb_drv2_039_spike_ratio_zscore_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_039_spike_ratio_zscore_252d_21d_diff},
    "vb_drv2_040_log_vol_ratio_median_21d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_040_log_vol_ratio_median_21d_21d_diff},
    "vb_drv2_041_spike_ratio_median_21d_slope_252d": {"inputs": ["volume"], "func": vb_drv2_041_spike_ratio_median_21d_slope_252d},
    "vb_drv2_042_vol_zscore_21d_slope_63d": {"inputs": ["volume"], "func": vb_drv2_042_vol_zscore_21d_slope_63d},
    "vb_drv2_043_vol_zscore_63d_slope_21d": {"inputs": ["volume"], "func": vb_drv2_043_vol_zscore_63d_slope_21d},
    "vb_drv2_044_vol_zscore_63d_slope_63d": {"inputs": ["volume"], "func": vb_drv2_044_vol_zscore_63d_slope_63d},
    "vb_drv2_045_spike_cluster_score_21d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_045_spike_cluster_score_21d_21d_diff},
    "vb_drv2_046_blowoff_composite_21d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_046_blowoff_composite_21d_21d_diff},
    "vb_drv2_047_spike_vol_turnover_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_047_spike_vol_turnover_21d_5d_diff},
    "vb_drv2_048_spike_vol_turnover_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_048_spike_vol_turnover_63d_21d_diff},
    "vb_drv2_049_vol_iqr_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_049_vol_iqr_21d_5d_diff},
    "vb_drv2_050_vol_iqr_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_050_vol_iqr_63d_21d_diff},
    "vb_drv2_051_vol_cv_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_051_vol_cv_21d_5d_diff},
    "vb_drv2_052_vol_cv_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_052_vol_cv_63d_21d_diff},
    "vb_drv2_053_spike_ratio_median_63d_slope_21d": {"inputs": ["volume"], "func": vb_drv2_053_spike_ratio_median_63d_slope_21d},
    "vb_drv2_054_spike_ratio_median_63d_slope_63d": {"inputs": ["volume"], "func": vb_drv2_054_spike_ratio_median_63d_slope_63d},
    "vb_drv2_055_spike_ratio_pct_rank_252d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_055_spike_ratio_pct_rank_252d_5d_diff},
    "vb_drv2_056_spike_ratio_pct_rank_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_056_spike_ratio_pct_rank_252d_21d_diff},
    "vb_drv2_057_vol_zscore_252d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_057_vol_zscore_252d_5d_diff},
    "vb_drv2_058_log_vol_zscore_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_058_log_vol_zscore_21d_5d_diff},
    "vb_drv2_059_log_vol_zscore_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_059_log_vol_zscore_63d_21d_diff},
    "vb_drv2_060_spike_asymmetry_ratio_63d_21d_diff": {"inputs": ["close", "volume"], "func": vb_drv2_060_spike_asymmetry_ratio_63d_21d_diff},
    "vb_drv2_061_spike_down_up_ratio_252d_21d_diff": {"inputs": ["close", "volume"], "func": vb_drv2_061_spike_down_up_ratio_252d_21d_diff},
    "vb_drv2_062_spike_count_down_days_252d_21d_diff": {"inputs": ["close", "volume"], "func": vb_drv2_062_spike_count_down_days_252d_21d_diff},
    "vb_drv2_063_vol_ratio_mean_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_063_vol_ratio_mean_252d_21d_diff},
    "vb_drv2_064_vol_ratio_mean_126d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_064_vol_ratio_mean_126d_5d_diff},
    "vb_drv2_065_spike_vol_turnover_21d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_065_spike_vol_turnover_21d_21d_diff},
    "vb_drv2_066_spike_ratio_ewm21_5d_diff": {"inputs": ["volume"], "func": vb_drv2_066_spike_ratio_ewm21_5d_diff},
    "vb_drv2_067_spike_ratio_ewm63_21d_diff": {"inputs": ["volume"], "func": vb_drv2_067_spike_ratio_ewm63_21d_diff},
    "vb_drv2_068_spike_cluster_density_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_068_spike_cluster_density_21d_5d_diff},
    "vb_drv2_069_spike_cluster_density_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_069_spike_cluster_density_63d_21d_diff},
    "vb_drv2_070_vol_90th_pct_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_070_vol_90th_pct_63d_5d_diff},
    "vb_drv2_071_vol_95th_pct_252d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_071_vol_95th_pct_252d_21d_diff},
    "vb_drv2_072_spike_recency_score_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_072_spike_recency_score_21d_5d_diff},
    "vb_drv2_073_spike_surprise_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv2_073_spike_surprise_21d_5d_diff},
    "vb_drv2_074_spike_surprise_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv2_074_spike_surprise_63d_21d_diff},
    "vb_drv2_075_vol_ratio_median_21d_slope_126d": {"inputs": ["volume"], "func": vb_drv2_075_vol_ratio_median_21d_slope_126d},
}
