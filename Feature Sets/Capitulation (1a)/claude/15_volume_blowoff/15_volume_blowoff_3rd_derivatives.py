"""
15_volume_blowoff — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative volume-blowoff features — acceleration
of velocity; inflection and exhaustion signals in blowoff-spike dynamics.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vb_drv3_001_vol_ratio_median_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/21d-median ratio (acceleration of blowoff ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_002_vol_ratio_median_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of vol/21d-median ratio (jerk in monthly blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_003_vol_zscore_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d volume z-score (acceleration of z-score spike)."""
    z = _vol_zscore(volume, _TD_MON)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_004_vol_zscore_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d z-score (jerk in quarterly z-score)."""
    z63 = _vol_zscore(volume, _TD_QTR)
    vel21 = z63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_005_spike_count_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day 2x-spike count (acceleration of spike frequency)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_006_spike_count_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63d spike count (jerk in quarterly spike rate)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt63 = _rolling_count_true(flag > 0, _TD_QTR)
    vel21 = cnt63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_007_max_spike_ratio_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d max spike ratio (acceleration of peak blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx63 = _rolling_max(ratio, _TD_QTR)
    vel = mx63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_008_spike_cluster_score_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d spike cluster score (jerk in blowoff energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_QTR)
    vel21 = cluster.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_009_vol_ratio_mean_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol/21d-mean ratio (acceleration of mean-based ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_010_log_ratio_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log(vol/21d-median) (log-scale acceleration)."""
    log_ratio = np.log1p(_vol_ratio_vs_median(volume, _TD_MON))
    vel = log_ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_011_spike_ratio_zscore_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of spike-ratio z-score (acceleration of extremity signal)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    z = _safe_div(ratio - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_012_spike_ratio_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/21d-median over 21d (rate of slope change)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def vb_drv3_013_spike_ratio_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/21d-median over 63d (rate of quarterly trend change)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vb_drv3_014_vol_zscore_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d z-score over 21d (rate of z-score trend change)."""
    z = _vol_zscore(volume, _TD_MON)
    slp = _linslope(z, _TD_MON)
    return slp.diff(_TD_WEEK)


def vb_drv3_015_spike_cluster_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d spike cluster score (acceleration of cluster intensity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_MON)
    vel = cluster.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_016_blowoff_composite_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of composite blowoff score (acceleration of composite signal)."""
    z_rank = _vol_zscore(volume, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    r_rank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    c_rank = _rolling_count_true(flag > 0, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    composite = (z_rank + r_rank + c_rank) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_017_spike_count_down_days_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d spike-on-down-days count (jerk in panic selling)."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt63 = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    vel21 = cnt63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_018_max_spike_ratio_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 252d max spike ratio (jerk in annual peak blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    vel21 = mx252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_019_excess_ratio_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d excess blowoff energy (jerk in energy accumulation)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess63 = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_QTR)
    vel21 = excess63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_020_vol_mean_vs_median_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d mean/median skew ratio (acceleration of spike-skew)."""
    skew = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    vel = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_021_spike_down_up_ratio_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d spike-down/spike-up ratio."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    dn = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    up = _rolling_count_true(((flag > 0) & (ret > 0)), _TD_QTR)
    ratio = _safe_div(dn, up)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_022_vol_ratio_median_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in vol/63d-median ratio (jerk in quarterly ratio)."""
    ratio63 = _vol_ratio_vs_median(volume, _TD_QTR)
    vel21 = ratio63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_023_spike_ratio_slope_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63d of the 21d-slope of vol/21d-median (2nd order slope)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp21 = _linslope(ratio, _TD_MON)
    return _linslope(slp21, _TD_QTR)


def vb_drv3_024_vol_zscore_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of 21d z-score (smoothed acceleration)."""
    z = _vol_zscore(volume, _TD_MON)
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vb_drv3_025_spike_cluster_score_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 252d spike cluster score (jerk in annual blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster252 = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_YEAR)
    vel21 = cluster252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- drv3_026-075: Extended 3rd derivatives ---

def vb_drv3_026_vol_ratio_median_126d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in vol/126d-median ratio (jerk in half-year ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_HALF)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_027_vol_ratio_median_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in vol/252d-median ratio (jerk in annual ratio)."""
    ratio = _vol_ratio_vs_median(volume, _TD_YEAR)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_028_vol_zscore_126d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 126d z-score (jerk in half-year z-score)."""
    z = _vol_zscore(volume, _TD_HALF)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_029_vol_zscore_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 252d z-score (jerk in annual z-score)."""
    z = _vol_zscore(volume, _TD_YEAR)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_030_spike_count_3x_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d 3x-spike count (jerk in extreme spike rate)."""
    flag = _spike_flag_median(volume, _TD_MON, 3.0)
    cnt63 = _rolling_count_true(flag > 0, _TD_QTR)
    vel21 = cnt63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_031_max_spike_ratio_126d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 126d max spike ratio (acceleration of half-year peak)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx126 = _rolling_max(ratio, _TD_HALF)
    vel = mx126.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_032_excess_ratio_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d excess blowoff energy (acceleration of short energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_MON)
    vel = excess.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_033_excess_ratio_63d_21d_diff_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d change in 63d excess energy (monthly acceleration of energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess63 = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_QTR)
    vel21 = excess63.diff(_TD_MON)
    return vel21.diff(_TD_MON)


def vb_drv3_034_vol_mean_vs_median_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d mean/median skew ratio (acceleration of quarterly skew)."""
    skew = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    vel = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_035_vol_zscore_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d volume z-score (acceleration of annual z-score)."""
    z = _vol_zscore(volume, _TD_YEAR)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_036_spike_ratio_pct_rank_252d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of spike-ratio percentile rank in 252d distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    prank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel = prank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_037_spike_cluster_score_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 21d spike cluster score (jerk in short cluster)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_MON)
    vel21 = cluster.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_038_spike_vol_turnover_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d spike volume turnover (acceleration of turnover share)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    turnover = _safe_div(_rolling_sum(spike_vol, _TD_MON), _rolling_sum(volume, _TD_MON))
    vel = turnover.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_039_spike_vol_turnover_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d spike turnover (jerk in quarterly turnover)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    turnover63 = _safe_div(_rolling_sum(spike_vol, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    vel21 = turnover63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_040_vol_cv_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d coefficient of variation (acceleration of dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_041_spike_ratio_slope_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of vol/21d-median over 21d (change in short slope)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_MON)


def vb_drv3_042_spike_ratio_slope_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of vol/21d-median over 63d (change in quarterly slope)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp = _linslope(ratio, _TD_QTR)
    return slp.diff(_TD_MON)


def vb_drv3_043_vol_zscore_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d z-score over 63d (rate of quarterly trend change)."""
    z = _vol_zscore(volume, _TD_MON)
    slp = _linslope(z, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vb_drv3_044_spike_cluster_density_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d spike cluster density (acceleration of spike density)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    density = _rolling_count_true(flag > 0, _TD_MON) / _TD_MON
    vel = density.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_045_spike_cluster_density_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d spike density (jerk in quarterly spike density)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    density = _rolling_count_true(flag > 0, _TD_QTR) / _TD_QTR
    vel21 = density.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_046_blowoff_composite_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in composite blowoff score (jerk in composite signal)."""
    z_rank = _vol_zscore(volume, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    r_rank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    c_rank = _rolling_count_true(flag > 0, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    composite = (z_rank + r_rank + c_rank) / 3.0
    vel21 = composite.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_047_spike_surprise_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d spike surprise (acceleration of ratio vs norm deviation)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    surprise = ratio - _rolling_mean(ratio, _TD_MON)
    vel = surprise.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_048_spike_surprise_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d spike surprise (jerk in quarterly deviation)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    surprise = ratio - _rolling_mean(ratio, _TD_QTR)
    vel21 = surprise.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_049_log_vol_ratio_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of log(vol/21d-median) velocity (log-scale jerk)."""
    log_ratio = np.log1p(_vol_ratio_vs_median(volume, _TD_MON))
    vel = log_ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_050_log_vol_ratio_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d velocity of log(vol/21d-median) (jerk in monthly log change)."""
    log_ratio = np.log1p(_vol_ratio_vs_median(volume, _TD_MON))
    vel21 = log_ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_051_vol_ratio_mean_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in vol/21d-mean ratio (jerk in mean-based ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_052_vol_ratio_mean_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in vol/63d-mean ratio (jerk in quarterly mean ratio)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_053_spike_count_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 21d spike count (jerk in spike frequency)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_MON)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_054_spike_count_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 252d spike count (jerk in annual spike rate)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt252 = _rolling_count_true(flag > 0, _TD_YEAR)
    vel21 = cnt252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_055_max_spike_ratio_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d max spike ratio (jerk in quarterly peak)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx63 = _rolling_max(ratio, _TD_QTR)
    vel21 = mx63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_056_max_spike_ratio_252d_21d_diff_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d change in 252d max spike ratio (monthly acceleration of annual peak)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx252 = _rolling_max(ratio, _TD_YEAR)
    vel21 = mx252.diff(_TD_MON)
    return vel21.diff(_TD_MON)


def vb_drv3_057_spike_down_up_ratio_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d spike-down/spike-up ratio (acceleration of panic asymmetry)."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    dn = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    up = _rolling_count_true(((flag > 0) & (ret > 0)), _TD_QTR)
    ratio = _safe_div(dn, up)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_058_spike_count_down_days_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d spike-on-down-days count (acceleration of panic count)."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt63 = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    vel = cnt63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_059_spike_asymmetry_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d down/up mean ratio (acceleration of asymmetry signal)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    dn_mean = ratio.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_mean = ratio.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    asym = _safe_div(dn_mean, up_mean)
    vel = asym.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_060_spike_ratio_slope_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 21d-slope of vol/21d-median (curvature at short scale)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp21 = _linslope(ratio, _TD_MON)
    return _linslope(slp21, _TD_MON)


def vb_drv3_061_vol_zscore_21d_5d_diff_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope over 63d of the 5d-velocity of 21d z-score (quarterly smoothed accel)."""
    z = _vol_zscore(volume, _TD_MON)
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_QTR)


def vb_drv3_062_spike_ratio_slope_252d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/21d-median over 252d (rate of annual trend change)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp = _linslope(ratio, _TD_YEAR)
    return slp.diff(_TD_WEEK)


def vb_drv3_063_vol_mean_vs_median_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 21d mean/median skew (jerk in spike skew)."""
    skew = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    vel21 = skew.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_064_spike_ratio_zscore_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in spike-ratio z-score (jerk in extremity measure)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    z = _safe_div(ratio - m, s)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_065_vol_iqr_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d volume IQR/median (acceleration of dispersion)."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr = _safe_div(q75 - q25, med)
    vel = iqr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_066_spike_ratio_ewm21_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM21 spike ratio (acceleration of smoothed blowoff)."""
    ewm = _vol_ratio_vs_median(volume, _TD_MON).ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_067_spike_ratio_ewm63_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in EWM63 spike ratio (jerk in quarterly smooth blowoff)."""
    ewm = _vol_ratio_vs_median(volume, _TD_MON).ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel21 = ewm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_068_vol_zscore_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d volume z-score (acceleration of quarterly z-score)."""
    z = _vol_zscore(volume, _TD_QTR)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_069_vol_zscore_126d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 126d volume z-score (acceleration of half-year z-score)."""
    z = _vol_zscore(volume, _TD_HALF)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_070_spike_cluster_score_63d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63d spike cluster score (acceleration of cluster energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    cluster63 = _rolling_sum(ratio.where(ratio > 2.0, 0.0), _TD_QTR)
    vel = cluster63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_071_excess_ratio_252d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 252d excess blowoff energy (jerk in annual energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess252 = _rolling_sum((ratio - 2.0).clip(lower=0.0), _TD_YEAR)
    vel21 = excess252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_072_vol_cv_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d CV (jerk in quarterly dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    vel21 = cv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_073_spike_recency_score_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of spike recency score (acceleration of decay-weighted signal)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    decay = 0.3
    weights = np.array([np.exp(-decay * k) for k in range(_TD_MON)])
    def _weighted_sum(arr):
        n = len(arr)
        w = weights[:n][::-1]
        return float(np.dot(arr, w))
    recency = flag.rolling(_TD_MON, min_periods=1).apply(_weighted_sum, raw=True)
    vel = recency.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vb_drv3_074_spike_count_down_days_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 252d spike-on-down-days count (jerk in annual panic)."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt252 = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_YEAR)
    vel21 = cnt252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vb_drv3_075_vol_ratio_median_21d_slope_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of vol/21d-median over 63d (rate of quarterly slope change)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    slp63 = _linslope(ratio, _TD_QTR)
    return slp63.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_BLOWOFF_REGISTRY_3RD_DERIVATIVES = {
    "vb_drv3_001_vol_ratio_median_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_001_vol_ratio_median_21d_5d_diff_5d_diff},
    "vb_drv3_002_vol_ratio_median_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_002_vol_ratio_median_21d_21d_diff_5d_diff},
    "vb_drv3_003_vol_zscore_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_003_vol_zscore_21d_5d_diff_5d_diff},
    "vb_drv3_004_vol_zscore_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_004_vol_zscore_63d_21d_diff_5d_diff},
    "vb_drv3_005_spike_count_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_005_spike_count_21d_5d_diff_5d_diff},
    "vb_drv3_006_spike_count_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_006_spike_count_63d_21d_diff_5d_diff},
    "vb_drv3_007_max_spike_ratio_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_007_max_spike_ratio_63d_5d_diff_5d_diff},
    "vb_drv3_008_spike_cluster_score_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_008_spike_cluster_score_63d_21d_diff_5d_diff},
    "vb_drv3_009_vol_ratio_mean_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_009_vol_ratio_mean_21d_5d_diff_5d_diff},
    "vb_drv3_010_log_ratio_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_010_log_ratio_21d_5d_diff_5d_diff},
    "vb_drv3_011_spike_ratio_zscore_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_011_spike_ratio_zscore_252d_5d_diff_5d_diff},
    "vb_drv3_012_spike_ratio_slope_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv3_012_spike_ratio_slope_21d_5d_diff},
    "vb_drv3_013_spike_ratio_slope_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv3_013_spike_ratio_slope_63d_5d_diff},
    "vb_drv3_014_vol_zscore_slope_21d_5d_diff": {"inputs": ["volume"], "func": vb_drv3_014_vol_zscore_slope_21d_5d_diff},
    "vb_drv3_015_spike_cluster_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_015_spike_cluster_21d_5d_diff_5d_diff},
    "vb_drv3_016_blowoff_composite_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_016_blowoff_composite_5d_diff_5d_diff},
    "vb_drv3_017_spike_count_down_days_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vb_drv3_017_spike_count_down_days_21d_diff_5d_diff},
    "vb_drv3_018_max_spike_ratio_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_018_max_spike_ratio_252d_21d_diff_5d_diff},
    "vb_drv3_019_excess_ratio_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_019_excess_ratio_63d_21d_diff_5d_diff},
    "vb_drv3_020_vol_mean_vs_median_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_020_vol_mean_vs_median_21d_5d_diff_5d_diff},
    "vb_drv3_021_spike_down_up_ratio_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vb_drv3_021_spike_down_up_ratio_63d_21d_diff_5d_diff},
    "vb_drv3_022_vol_ratio_median_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_022_vol_ratio_median_63d_21d_diff_5d_diff},
    "vb_drv3_023_spike_ratio_slope_21d_slope_63d": {"inputs": ["volume"], "func": vb_drv3_023_spike_ratio_slope_21d_slope_63d},
    "vb_drv3_024_vol_zscore_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vb_drv3_024_vol_zscore_21d_5d_diff_slope_21d},
    "vb_drv3_025_spike_cluster_score_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_025_spike_cluster_score_252d_21d_diff_5d_diff},
    "vb_drv3_026_vol_ratio_median_126d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_026_vol_ratio_median_126d_21d_diff_5d_diff},
    "vb_drv3_027_vol_ratio_median_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_027_vol_ratio_median_252d_21d_diff_5d_diff},
    "vb_drv3_028_vol_zscore_126d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_028_vol_zscore_126d_21d_diff_5d_diff},
    "vb_drv3_029_vol_zscore_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_029_vol_zscore_252d_21d_diff_5d_diff},
    "vb_drv3_030_spike_count_3x_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_030_spike_count_3x_63d_21d_diff_5d_diff},
    "vb_drv3_031_max_spike_ratio_126d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_031_max_spike_ratio_126d_5d_diff_5d_diff},
    "vb_drv3_032_excess_ratio_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_032_excess_ratio_21d_5d_diff_5d_diff},
    "vb_drv3_033_excess_ratio_63d_21d_diff_21d_diff": {"inputs": ["volume"], "func": vb_drv3_033_excess_ratio_63d_21d_diff_21d_diff},
    "vb_drv3_034_vol_mean_vs_median_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_034_vol_mean_vs_median_63d_5d_diff_5d_diff},
    "vb_drv3_035_vol_zscore_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_035_vol_zscore_252d_5d_diff_5d_diff},
    "vb_drv3_036_spike_ratio_pct_rank_252d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_036_spike_ratio_pct_rank_252d_5d_diff_5d_diff},
    "vb_drv3_037_spike_cluster_score_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_037_spike_cluster_score_21d_21d_diff_5d_diff},
    "vb_drv3_038_spike_vol_turnover_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_038_spike_vol_turnover_21d_5d_diff_5d_diff},
    "vb_drv3_039_spike_vol_turnover_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_039_spike_vol_turnover_63d_21d_diff_5d_diff},
    "vb_drv3_040_vol_cv_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_040_vol_cv_21d_5d_diff_5d_diff},
    "vb_drv3_041_spike_ratio_slope_21d_21d_diff": {"inputs": ["volume"], "func": vb_drv3_041_spike_ratio_slope_21d_21d_diff},
    "vb_drv3_042_spike_ratio_slope_63d_21d_diff": {"inputs": ["volume"], "func": vb_drv3_042_spike_ratio_slope_63d_21d_diff},
    "vb_drv3_043_vol_zscore_slope_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv3_043_vol_zscore_slope_63d_5d_diff},
    "vb_drv3_044_spike_cluster_density_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_044_spike_cluster_density_21d_5d_diff_5d_diff},
    "vb_drv3_045_spike_cluster_density_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_045_spike_cluster_density_63d_21d_diff_5d_diff},
    "vb_drv3_046_blowoff_composite_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_046_blowoff_composite_21d_21d_diff_5d_diff},
    "vb_drv3_047_spike_surprise_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_047_spike_surprise_21d_5d_diff_5d_diff},
    "vb_drv3_048_spike_surprise_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_048_spike_surprise_63d_21d_diff_5d_diff},
    "vb_drv3_049_log_vol_ratio_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_049_log_vol_ratio_21d_5d_diff_5d_diff},
    "vb_drv3_050_log_vol_ratio_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_050_log_vol_ratio_21d_21d_diff_5d_diff},
    "vb_drv3_051_vol_ratio_mean_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_051_vol_ratio_mean_21d_21d_diff_5d_diff},
    "vb_drv3_052_vol_ratio_mean_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_052_vol_ratio_mean_63d_21d_diff_5d_diff},
    "vb_drv3_053_spike_count_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_053_spike_count_21d_21d_diff_5d_diff},
    "vb_drv3_054_spike_count_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_054_spike_count_252d_21d_diff_5d_diff},
    "vb_drv3_055_max_spike_ratio_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_055_max_spike_ratio_63d_21d_diff_5d_diff},
    "vb_drv3_056_max_spike_ratio_252d_21d_diff_21d_diff": {"inputs": ["volume"], "func": vb_drv3_056_max_spike_ratio_252d_21d_diff_21d_diff},
    "vb_drv3_057_spike_down_up_ratio_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vb_drv3_057_spike_down_up_ratio_63d_5d_diff_5d_diff},
    "vb_drv3_058_spike_count_down_days_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vb_drv3_058_spike_count_down_days_63d_5d_diff_5d_diff},
    "vb_drv3_059_spike_asymmetry_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vb_drv3_059_spike_asymmetry_63d_5d_diff_5d_diff},
    "vb_drv3_060_spike_ratio_slope_21d_slope_21d": {"inputs": ["volume"], "func": vb_drv3_060_spike_ratio_slope_21d_slope_21d},
    "vb_drv3_061_vol_zscore_21d_5d_diff_slope_63d": {"inputs": ["volume"], "func": vb_drv3_061_vol_zscore_21d_5d_diff_slope_63d},
    "vb_drv3_062_spike_ratio_slope_252d_5d_diff": {"inputs": ["volume"], "func": vb_drv3_062_spike_ratio_slope_252d_5d_diff},
    "vb_drv3_063_vol_mean_vs_median_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_063_vol_mean_vs_median_21d_21d_diff_5d_diff},
    "vb_drv3_064_spike_ratio_zscore_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_064_spike_ratio_zscore_252d_21d_diff_5d_diff},
    "vb_drv3_065_vol_iqr_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_065_vol_iqr_21d_5d_diff_5d_diff},
    "vb_drv3_066_spike_ratio_ewm21_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_066_spike_ratio_ewm21_5d_diff_5d_diff},
    "vb_drv3_067_spike_ratio_ewm63_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_067_spike_ratio_ewm63_21d_diff_5d_diff},
    "vb_drv3_068_vol_zscore_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_068_vol_zscore_63d_5d_diff_5d_diff},
    "vb_drv3_069_vol_zscore_126d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_069_vol_zscore_126d_5d_diff_5d_diff},
    "vb_drv3_070_spike_cluster_score_63d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_070_spike_cluster_score_63d_5d_diff_5d_diff},
    "vb_drv3_071_excess_ratio_252d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_071_excess_ratio_252d_21d_diff_5d_diff},
    "vb_drv3_072_vol_cv_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_072_vol_cv_63d_21d_diff_5d_diff},
    "vb_drv3_073_spike_recency_score_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vb_drv3_073_spike_recency_score_21d_5d_diff_5d_diff},
    "vb_drv3_074_spike_count_down_days_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vb_drv3_074_spike_count_down_days_252d_21d_diff_5d_diff},
    "vb_drv3_075_vol_ratio_median_21d_slope_63d_5d_diff": {"inputs": ["volume"], "func": vb_drv3_075_vol_ratio_median_21d_slope_63d_5d_diff},
}
