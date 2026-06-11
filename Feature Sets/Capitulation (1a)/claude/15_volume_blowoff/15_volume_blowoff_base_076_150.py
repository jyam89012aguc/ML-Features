"""
15_volume_blowoff — Base Features 076-200
Domain: volume spikes measured against a trailing baseline — blowoff volume.
Spike clustering, inter-spike spacing, price-conditioned spike signals, spike
magnitude relative to history, spike decay, and composite blowoff indices.
Strictly spike-vs-baseline; no sustained-elevation, single-day-climax-framing,
or volume-collapse concepts.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _vol_ratio_vs_median(volume: pd.Series, w: int) -> pd.Series:
    """Volume / trailing w-day median."""
    return _safe_div(volume, _rolling_median(volume, w))


def _vol_ratio_vs_mean(volume: pd.Series, w: int) -> pd.Series:
    """Volume / trailing w-day mean."""
    return _safe_div(volume, _rolling_mean(volume, w))


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    """Z-score of volume vs trailing w-day mean/std."""
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s)


def _spike_flag_median(volume: pd.Series, w: int, thresh: float) -> pd.Series:
    """1 if volume/trailing-median > thresh."""
    return (_vol_ratio_vs_median(volume, w) > thresh).astype(float)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Spike clustering and consecutive spike streaks ---

def vb_076_consec_spike_days_2x_median(volume: pd.Series) -> pd.Series:
    """Current consecutive days with volume > 2x 21d median (spike streak)."""
    cond = _vol_ratio_vs_median(volume, _TD_MON) > 2.0
    return _consec_streak(cond)


def vb_077_consec_spike_days_3x_median(volume: pd.Series) -> pd.Series:
    """Current consecutive days with volume > 3x 21d median (extreme spike streak)."""
    cond = _vol_ratio_vs_median(volume, _TD_MON) > 3.0
    return _consec_streak(cond)


def vb_078_consec_spike_days_zscore_gt2(volume: pd.Series) -> pd.Series:
    """Current consecutive days with 21d z-score > 2 (z-based spike streak)."""
    cond = _vol_zscore(volume, _TD_MON) > 2.0
    return _consec_streak(cond)


def vb_079_max_consec_spike_2x_median_21d(volume: pd.Series) -> pd.Series:
    """Max consecutive 2x-median spike streak within trailing 21 days."""
    cond = _vol_ratio_vs_median(volume, _TD_MON) > 2.0
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def vb_080_max_consec_spike_2x_median_63d(volume: pd.Series) -> pd.Series:
    """Max consecutive 2x-median spike streak within trailing 63 days."""
    cond = _vol_ratio_vs_median(volume, _TD_MON) > 2.0
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def vb_081_max_consec_spike_2x_median_252d(volume: pd.Series) -> pd.Series:
    """Max consecutive 2x-median spike streak within trailing 252 days."""
    cond = _vol_ratio_vs_median(volume, _TD_MON) > 2.0
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def vb_082_spike_cluster_density_21d(volume: pd.Series) -> pd.Series:
    """Spike-day count / window length ratio: 21-day clustering density (2x median)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_MON) / _TD_MON


def vb_083_spike_cluster_density_63d(volume: pd.Series) -> pd.Series:
    """Spike-day count / window: 63-day clustering density (2x median)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_QTR) / _TD_QTR


def vb_084_spike_cluster_score_21d(volume: pd.Series) -> pd.Series:
    """Sum of spike ratios (only on spike days) over 21 days (cluster intensity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vals = ratio.where(ratio > 2.0, 0.0)
    return _rolling_sum(spike_vals, _TD_MON)


def vb_085_spike_cluster_score_63d(volume: pd.Series) -> pd.Series:
    """Sum of spike ratios (only on spike days) over 63 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vals = ratio.where(ratio > 2.0, 0.0)
    return _rolling_sum(spike_vals, _TD_QTR)


def vb_086_spike_cluster_score_252d(volume: pd.Series) -> pd.Series:
    """Sum of spike ratios (only on spike days) over 252 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vals = ratio.where(ratio > 2.0, 0.0)
    return _rolling_sum(spike_vals, _TD_YEAR)


def vb_087_spike_count_21d_norm_252d(volume: pd.Series) -> pd.Series:
    """21-day spike count normalized by 252-day average 21d spike count."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt21 = _rolling_count_true(flag > 0, _TD_MON)
    avg = _rolling_mean(cnt21, _TD_YEAR)
    return _safe_div(cnt21, avg)


def vb_088_spike_count_63d_norm_252d(volume: pd.Series) -> pd.Series:
    """63-day spike count normalized by 252-day average 63d spike count."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt63 = _rolling_count_true(flag > 0, _TD_QTR)
    avg = _rolling_mean(cnt63, _TD_YEAR)
    return _safe_div(cnt63, avg)


def vb_089_days_since_last_spike_2x(volume: pd.Series) -> pd.Series:
    """Days since last 2x-median spike (inter-spike distance, lower = more clustered)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    not_spike = (flag == 0).astype(int)
    group = flag.cumsum()
    days_since = not_spike.groupby(group).cumsum()
    return days_since.astype(float)


def vb_090_spike_recency_score_21d(volume: pd.Series) -> pd.Series:
    """Exponentially decayed spike indicator: sum of exp(-k*lag)*spike_flag over 21d."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    decay = 0.3
    weights = np.array([np.exp(-decay * k) for k in range(_TD_MON)])
    def _weighted_sum(arr):
        n = len(arr)
        w = weights[:n][::-1]
        return float(np.dot(arr, w))
    return flag.rolling(_TD_MON, min_periods=1).apply(_weighted_sum, raw=True)


# --- Group G (091-105): Price-conditioned spike signals ---

def vb_091_spike_ratio_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean spike ratio on down-close days over 21 days (panic selling signal)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_dn = ratio.where(ret < 0, np.nan)
    return ratio_dn.rolling(_TD_MON, min_periods=1).mean()


def vb_092_spike_ratio_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean spike ratio on down-close days over 63 days."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_dn = ratio.where(ret < 0, np.nan)
    return ratio_dn.rolling(_TD_QTR, min_periods=1).mean()


def vb_093_spike_ratio_on_up_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean spike ratio on up-close days over 21 days (buying surge signal)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_up = ratio.where(ret > 0, np.nan)
    return ratio_up.rolling(_TD_MON, min_periods=1).mean()


def vb_094_spike_count_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on down-close days in trailing 63 days."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & (ret < 0)).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


def vb_095_spike_count_on_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on down-close days in trailing 252 days."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & (ret < 0)).astype(float)
    return _rolling_count_true(both > 0, _TD_YEAR)


def vb_096_spike_down_up_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spikes on down days / spikes on up days in trailing 63 days."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    dn = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_QTR)
    up = _rolling_count_true(((flag > 0) & (ret > 0)), _TD_QTR)
    return _safe_div(dn, up)


def vb_097_spike_down_up_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spikes on down days / spikes on up days in trailing 252 days."""
    ret = close.pct_change(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    dn = _rolling_count_true(((flag > 0) & (ret < 0)), _TD_YEAR)
    up = _rolling_count_true(((flag > 0) & (ret > 0)), _TD_YEAR)
    return _safe_div(dn, up)


def vb_098_max_spike_ratio_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max spike ratio seen on down-close days in trailing 63 days."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_dn = ratio.where(ret < 0, np.nan)
    return ratio_dn.rolling(_TD_QTR, min_periods=1).max()


def vb_099_max_spike_ratio_on_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max spike ratio seen on down-close days in trailing 252 days."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_dn = ratio.where(ret < 0, np.nan)
    return ratio_dn.rolling(_TD_YEAR, min_periods=1).max()


def vb_100_spike_vol_zscore_on_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean 21d volume z-score on down-close days in trailing 63 days."""
    ret = close.pct_change(1)
    z = _vol_zscore(volume, _TD_MON)
    z_dn = z.where(ret < 0, np.nan)
    return z_dn.rolling(_TD_QTR, min_periods=1).mean()


def vb_101_spike_on_gap_down_days_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on gap-down open days in trailing 63 days."""
    gap_down = open < close.shift(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & gap_down).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


def vb_102_spike_on_new_52wk_low_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on 252-day new-low closes in trailing 252 days."""
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = close < roll_min
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & new_low).astype(float)
    return _rolling_count_true(both > 0, _TD_YEAR)


def vb_103_vol_ratio_on_large_down_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol/21d-median on days with |return| > 2% in trailing 21 days."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_big = ratio.where(ret < -0.02, np.nan)
    return ratio_big.rolling(_TD_MON, min_periods=1).mean()


def vb_104_spike_on_high_range_day_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of spikes coinciding with top-quartile intraday range in trailing 63 days."""
    rng = high - low
    rng_75 = rng.rolling(_TD_QTR, min_periods=_TD_MON).quantile(0.75)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & (rng > rng_75)).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


def vb_105_spike_on_low_close_rank_day_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of spikes on days where close is in bottom 25% of 63d range, trailing 63d."""
    roll_min = _rolling_min(close, _TD_QTR)
    roll_max = _rolling_max(close, _TD_QTR)
    close_rank = _safe_div(close - roll_min, roll_max - roll_min)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & (close_rank < 0.25)).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


# --- Group H (106-120): Spike magnitude relative to history ---

def vb_106_spike_ratio_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of vol/21d-median ratio vs its own 252-day distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    m = _rolling_mean(ratio, _TD_YEAR)
    s = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio - m, s)


def vb_107_spike_ratio_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of vol/21d-median ratio in trailing 504-day distribution."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


def vb_108_max_spike_ratio_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63-day max spike ratio (all-history extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx63 = _rolling_max(ratio, _TD_QTR)
    return mx63.expanding(min_periods=5).rank(pct=True)


def vb_109_spike_magnitude_norm_21d_avg(volume: pd.Series) -> pd.Series:
    """Current spike ratio / 252-day average spike-day magnitude."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vals = ratio.where(ratio > 2.0, np.nan)
    avg_mag = spike_vals.rolling(_TD_YEAR, min_periods=1).mean()
    return _safe_div(ratio, avg_mag)


def vb_110_excess_ratio_above_2x_median_21d(volume: pd.Series) -> pd.Series:
    """Excess of vol/21d-median above 2.0 (zero if below; measures blowoff excess)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return (ratio - 2.0).clip(lower=0.0)


def vb_111_excess_ratio_above_3x_median_21d(volume: pd.Series) -> pd.Series:
    """Excess of vol/21d-median above 3.0 (zero if below; extreme excess)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return (ratio - 3.0).clip(lower=0.0)


def vb_112_sum_excess_ratio_63d(volume: pd.Series) -> pd.Series:
    """Sum of excess-above-2x-median over trailing 63 days (accumulated blowoff energy)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = (ratio - 2.0).clip(lower=0.0)
    return _rolling_sum(excess, _TD_QTR)


def vb_113_sum_excess_ratio_252d(volume: pd.Series) -> pd.Series:
    """Sum of excess-above-2x-median over trailing 252 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = (ratio - 2.0).clip(lower=0.0)
    return _rolling_sum(excess, _TD_YEAR)


def vb_114_max_excess_ratio_63d(volume: pd.Series) -> pd.Series:
    """Max excess-above-2x-median seen in trailing 63 days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = (ratio - 2.0).clip(lower=0.0)
    return _rolling_max(excess, _TD_QTR)


def vb_115_max_excess_ratio_252d(volume: pd.Series) -> pd.Series:
    """Max excess-above-2x-median seen in trailing 252 days (all-year record blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    excess = (ratio - 2.0).clip(lower=0.0)
    return _rolling_max(excess, _TD_YEAR)


def vb_116_spike_ratio_ewm_21d(volume: pd.Series) -> pd.Series:
    """EWM21 of vol/21d-median ratio (smoothed blowoff indicator)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _ewm_mean(ratio, _TD_MON)


def vb_117_spike_ratio_ewm_63d(volume: pd.Series) -> pd.Series:
    """EWM63 of vol/21d-median ratio (quarterly smoothed blowoff)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _ewm_mean(ratio, _TD_QTR)


def vb_118_max_vol_raw_63d(volume: pd.Series) -> pd.Series:
    """Raw maximum volume value in trailing 63 days (absolute peak)."""
    return _rolling_max(volume, _TD_QTR)


def vb_119_max_vol_raw_252d(volume: pd.Series) -> pd.Series:
    """Raw maximum volume value in trailing 252 days."""
    return _rolling_max(volume, _TD_YEAR)


def vb_120_current_vol_vs_max_63d(volume: pd.Series) -> pd.Series:
    """Current volume / 63-day max volume (proximity to recent peak)."""
    return _safe_div(volume, _rolling_max(volume, _TD_QTR))


# --- Group I (121-135): Spike decay and post-spike behavior ---

def vb_121_vol_decay_since_spike_5d(volume: pd.Series) -> pd.Series:
    """Ratio of current vol / max-vol-last-5d (decay from recent peak)."""
    return _safe_div(volume, _rolling_max(volume, _TD_WEEK))


def vb_122_vol_decay_since_spike_21d(volume: pd.Series) -> pd.Series:
    """Ratio of current vol / max-vol-last-21d (decay from monthly peak)."""
    return _safe_div(volume, _rolling_max(volume, _TD_MON))


def vb_123_vol_decay_since_spike_63d(volume: pd.Series) -> pd.Series:
    """Ratio of current vol / max-vol-last-63d (decay from quarterly peak)."""
    return _safe_div(volume, _rolling_max(volume, _TD_QTR))


def vb_124_vol_stddev_21d_norm_by_mean(volume: pd.Series) -> pd.Series:
    """21-day coefficient of variation (std/mean) of volume (spike dispersion)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(s, m)


def vb_125_vol_stddev_63d_norm_by_mean(volume: pd.Series) -> pd.Series:
    """63-day coefficient of variation (std/mean) of volume."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    return _safe_div(s, m)


def vb_126_vol_stddev_252d_norm_by_mean(volume: pd.Series) -> pd.Series:
    """252-day coefficient of variation of volume (annual spike dispersion)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    return _safe_div(s, m)


def vb_127_vol_iqr_21d_norm_by_median(volume: pd.Series) -> pd.Series:
    """21-day IQR of volume normalized by 21d median (robust dispersion proxy)."""
    q75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    med = _rolling_median(volume, _TD_MON)
    return _safe_div(q75 - q25, med)


def vb_128_vol_iqr_63d_norm_by_median(volume: pd.Series) -> pd.Series:
    """63-day IQR of volume normalized by 63d median."""
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    med = _rolling_median(volume, _TD_QTR)
    return _safe_div(q75 - q25, med)


def vb_129_vol_90th_pct_63d_norm_median(volume: pd.Series) -> pd.Series:
    """90th-percentile volume over 63d normalized by 63d median (tail spike height)."""
    p90 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.90)
    med = _rolling_median(volume, _TD_QTR)
    return _safe_div(p90, med)


def vb_130_vol_95th_pct_252d_norm_median(volume: pd.Series) -> pd.Series:
    """95th-percentile volume over 252d normalized by 252d median."""
    p95 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.95)
    med = _rolling_median(volume, _TD_YEAR)
    return _safe_div(p95, med)


def vb_131_vol_75th_pct_21d_norm_median(volume: pd.Series) -> pd.Series:
    """75th-percentile volume over 21d normalized by 21d median."""
    p75 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    med = _rolling_median(volume, _TD_MON)
    return _safe_div(p75, med)


def vb_132_spike_half_life_21d(volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of vol/21d-median ratio over 21d (spike persistence)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    def _ac1(arr):
        if len(arr) < 3:
            return np.nan
        r0 = arr[:-1]
        r1 = arr[1:]
        if r0.std() < _EPS or r1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(r0, r1)[0, 1])
    return ratio.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(_ac1, raw=True)


def vb_133_spike_half_life_63d(volume: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of vol/21d-median ratio over 63d (persistence)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    def _ac1(arr):
        if len(arr) < 3:
            return np.nan
        r0 = arr[:-1]
        r1 = arr[1:]
        if r0.std() < _EPS or r1.std() < _EPS:
            return np.nan
        return float(np.corrcoef(r0, r1)[0, 1])
    return ratio.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_ac1, raw=True)


def vb_134_spike_vol_momentum_5d(volume: pd.Series) -> pd.Series:
    """5-day change in vol/21d-median ratio (short-term spike momentum)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.diff(_TD_WEEK)


def vb_135_spike_vol_momentum_21d(volume: pd.Series) -> pd.Series:
    """21-day change in vol/21d-median ratio (monthly spike momentum)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return ratio.diff(_TD_MON)


# --- Group J (136-150): Composite blowoff indices ---

def vb_136_blowoff_composite_score_21d(volume: pd.Series) -> pd.Series:
    """Composite blowoff: avg of 21d z-score rank, 21d median ratio rank, spike-count rank."""
    z_rank = _vol_zscore(volume, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    r_rank = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt = _rolling_count_true(flag > 0, _TD_MON)
    c_rank = cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (z_rank + r_rank + c_rank) / 3.0


def vb_137_blowoff_composite_score_63d(volume: pd.Series) -> pd.Series:
    """Composite blowoff: avg of 63d z-score rank, 63d median ratio rank, 63d spike-count rank."""
    z63 = _vol_zscore(volume, _TD_QTR)
    z_rank = z63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio63 = _vol_ratio_vs_median(volume, _TD_QTR)
    r_rank = ratio63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt63 = _rolling_count_true(flag > 0, _TD_QTR)
    c_rank = cnt63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (z_rank + r_rank + c_rank) / 3.0


def vb_138_spike_down_day_blowoff_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spike count on down days x avg spike ratio on down days over 63d (panic energy)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_dn = ratio.where((ratio > 2.0) & (ret < 0), 0.0)
    return _rolling_sum(spike_dn, _TD_QTR)


def vb_139_blowoff_index_weighted_21d(volume: pd.Series) -> pd.Series:
    """Volume-weighted blowoff index: sum(vol*spike_ratio) / sum(vol) over 21d."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_contrib = volume * ratio.where(ratio > 2.0, 0.0)
    vol_sum = _rolling_sum(volume, _TD_MON)
    return _safe_div(_rolling_sum(spike_contrib, _TD_MON), vol_sum)


def vb_140_blowoff_index_weighted_63d(volume: pd.Series) -> pd.Series:
    """Volume-weighted blowoff index over 63d: sum(vol*spike_ratio) / sum(vol)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_contrib = volume * ratio.where(ratio > 2.0, 0.0)
    vol_sum = _rolling_sum(volume, _TD_QTR)
    return _safe_div(_rolling_sum(spike_contrib, _TD_QTR), vol_sum)


def vb_141_spike_ratio_vs_1yr_max_ratio(volume: pd.Series) -> pd.Series:
    """Current vol/21d-median ratio as fraction of 252-day max spike ratio."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    max252 = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(ratio, max252)


def vb_142_spike_ratio_vs_1yr_avg_spike(volume: pd.Series) -> pd.Series:
    """Current spike ratio divided by 252-day average of ratios on spike days."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    avg_spike = ratio.where(ratio > 2.0, np.nan).rolling(_TD_YEAR, min_periods=1).mean()
    return _safe_div(ratio, avg_spike)


def vb_143_spike_surprise_index_21d(volume: pd.Series) -> pd.Series:
    """Current ratio minus 21-day average ratio (deviation from recent norm)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    avg21 = _rolling_mean(ratio, _TD_MON)
    return ratio - avg21


def vb_144_spike_surprise_index_63d(volume: pd.Series) -> pd.Series:
    """Current ratio minus 63-day average ratio (deviation from quarterly norm)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    avg63 = _rolling_mean(ratio, _TD_QTR)
    return ratio - avg63


def vb_145_spike_surprise_index_252d(volume: pd.Series) -> pd.Series:
    """Current ratio minus 252-day average ratio (deviation from annual norm)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    avg252 = _rolling_mean(ratio, _TD_YEAR)
    return ratio - avg252


def vb_146_spike_ratio_21d_zscore_504d(volume: pd.Series) -> pd.Series:
    """Z-score of vol/21d-median ratio vs 504-day distribution (ultra-long baseline)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    m = ratio.rolling(504, min_periods=_TD_YEAR // 2).mean()
    s = ratio.rolling(504, min_periods=_TD_YEAR // 2).std()
    return _safe_div(ratio - m, s)


def vb_147_spike_count_21d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day spike count in 504-day distribution."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt21 = _rolling_count_true(flag > 0, _TD_MON)
    return cnt21.rolling(504, min_periods=_TD_YEAR // 2).rank(pct=True)


def vb_148_spike_cluster_vs_history_score(volume: pd.Series) -> pd.Series:
    """63-day spike cluster score normalized by 252-day average cluster score."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vals = ratio.where(ratio > 2.0, 0.0)
    cluster63 = _rolling_sum(spike_vals, _TD_QTR)
    avg252 = _rolling_mean(cluster63, _TD_YEAR)
    return _safe_div(cluster63, avg252)


def vb_149_spike_vol_stddev_ratio_21d(volume: pd.Series) -> pd.Series:
    """Std of vol/21d-median ratio over 21d / its 252d avg std (dispersion extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    std21 = _rolling_std(ratio, _TD_MON)
    avg_std = _rolling_mean(std21, _TD_YEAR)
    return _safe_div(std21, avg_std)


def vb_150_blowoff_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined distress: (spike ratio * spike-count-21d) / 252d-avg, on down days."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt21 = _rolling_count_true(flag > 0, _TD_MON)
    intensity = ratio * cnt21
    avg_intensity = _rolling_mean(intensity, _TD_YEAR)
    down_frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    return _safe_div(intensity, avg_intensity.clip(lower=_EPS)) * down_frac


# --- Group K (176-190): Extended spike/price constructions ---

def vb_176_spike_ratio_on_gap_up_days_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean spike ratio on gap-up open days over 63 days (buying surge after gap)."""
    gap_up = open > close.shift(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_gap = ratio.where(gap_up, np.nan)
    return ratio_gap.rolling(_TD_QTR, min_periods=1).mean()


def vb_177_spike_count_on_gap_down_days_252d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on gap-down open days in trailing 252 days."""
    gap_down = open < close.shift(1)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & gap_down).astype(float)
    return _rolling_count_true(both > 0, _TD_YEAR)


def vb_178_vol_ratio_on_gap_down_day_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol/21d-median on gap-down open days in trailing 21 days."""
    gap_down = open < close.shift(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_gap = ratio.where(gap_down, np.nan)
    return ratio_gap.rolling(_TD_MON, min_periods=1).mean()


def vb_179_spike_on_new_21d_low_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on 21-day new-low closes in trailing 63 days."""
    roll_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    new_low = close < roll_min
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & new_low).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


def vb_180_spike_on_new_63d_low_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes on 63-day new-low closes in trailing 252 days."""
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < roll_min
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & new_low).astype(float)
    return _rolling_count_true(both > 0, _TD_YEAR)


def vb_181_vol_ratio_on_large_up_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol/21d-median on days with return > 2% in trailing 21 days (relief spike)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    ratio_up = ratio.where(ret > 0.02, np.nan)
    return ratio_up.rolling(_TD_MON, min_periods=1).mean()


def vb_182_spike_asymmetry_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-day spike ratio mean / up-day spike ratio mean over 63d (panic asymmetry)."""
    ret = close.pct_change(1)
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    dn_mean = ratio.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_mean = ratio.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(dn_mean, up_mean)


def vb_183_spike_on_wk_low_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of spikes on 5-day new-low close days in trailing 63 days."""
    roll_min = close.shift(1).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).min()
    new_low = close < roll_min
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & new_low).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


def vb_184_vol_range_spike_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (H-L)/close-scale spike ratio on spike days over 21 days."""
    rng = high - low
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    rng_on_spike = rng.where(flag > 0, np.nan)
    return rng_on_spike.rolling(_TD_MON, min_periods=1).mean()


def vb_185_spike_vol_on_wide_bar_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of spikes coinciding with top-quartile intraday range in trailing 63d (alternative window)."""
    rng = high - low
    rng_75 = rng.rolling(_TD_YEAR, min_periods=_TD_HALF).quantile(0.75)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    both = ((flag > 0) & (rng > rng_75)).astype(float)
    return _rolling_count_true(both > 0, _TD_QTR)


def vb_186_spike_count_3x_median_21d(volume: pd.Series) -> pd.Series:
    """Count of 3x-median extreme spikes in trailing 21 days."""
    flag = _spike_flag_median(volume, _TD_MON, 3.0)
    return _rolling_count_true(flag > 0, _TD_MON)


def vb_187_spike_count_2x_median_5d(volume: pd.Series) -> pd.Series:
    """Count of 2x-median spikes in trailing 5 days (very short cluster)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_WEEK)


def vb_188_spike_fraction_3x_median_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with volume > 3x 21d median (extreme spike density)."""
    flag = _spike_flag_median(volume, _TD_MON, 3.0)
    return _rolling_count_true(flag > 0, _TD_QTR) / _TD_QTR


def vb_189_spike_fraction_3x_median_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with volume > 3x 21d median (annual extreme density)."""
    flag = _spike_flag_median(volume, _TD_MON, 3.0)
    return _rolling_count_true(flag > 0, _TD_YEAR) / _TD_YEAR


def vb_190_spike_vol_turnover_21d(volume: pd.Series) -> pd.Series:
    """Sum of volume on spike days / total volume over 21 days (spike share of turnover)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    return _safe_div(_rolling_sum(spike_vol, _TD_MON), _rolling_sum(volume, _TD_MON))


# --- Group L (191-200): Composite and normalized blowoff extensions ---

def vb_191_spike_vol_turnover_63d(volume: pd.Series) -> pd.Series:
    """Sum of volume on spike days / total volume over 63 days (quarterly spike turnover)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    return _safe_div(_rolling_sum(spike_vol, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def vb_192_blowoff_composite_score_252d(volume: pd.Series) -> pd.Series:
    """Composite blowoff: avg of 252d z-score rank, 252d ratio rank, 252d spike-count rank."""
    z252 = _vol_zscore(volume, _TD_YEAR)
    z_rank = z252.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    ratio252 = _vol_ratio_vs_median(volume, _TD_YEAR)
    r_rank = ratio252.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt252 = _rolling_count_true(flag > 0, _TD_YEAR)
    c_rank = cnt252.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (z_rank + r_rank + c_rank) / 3.0


def vb_193_spike_ratio_ewm_126d(volume: pd.Series) -> pd.Series:
    """EWM126 of vol/21d-median ratio (half-year smoothed blowoff indicator)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    return _ewm_mean(ratio, _TD_HALF)


def vb_194_spike_count_21d_pct_rank_126d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day 2x-spike count in trailing 126-day distribution."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    cnt21 = _rolling_count_true(flag > 0, _TD_MON)
    return cnt21.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


def vb_195_max_vol_ratio_vs_mean_252d(volume: pd.Series) -> pd.Series:
    """Max volume/21d-mean ratio seen in trailing 252 days (annual mean-based peak)."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _rolling_max(ratio, _TD_YEAR)


def vb_196_spike_ratio_range_63d(volume: pd.Series) -> pd.Series:
    """Max minus min of vol/21d-median ratio over 63 days (intraperiod range)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx = _rolling_max(ratio, _TD_QTR)
    mn = ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return mx - mn


def vb_197_spike_ratio_range_252d(volume: pd.Series) -> pd.Series:
    """Max minus min of vol/21d-median ratio over 252 days (annual intraperiod range)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    mx = _rolling_max(ratio, _TD_YEAR)
    mn = ratio.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return mx - mn


def vb_198_blowoff_index_weighted_252d(volume: pd.Series) -> pd.Series:
    """Volume-weighted blowoff index over 252d: sum(vol*spike_ratio) / sum(vol)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_contrib = volume * ratio.where(ratio > 2.0, 0.0)
    vol_sum = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(_rolling_sum(spike_contrib, _TD_YEAR), vol_sum)


def vb_199_spike_cluster_density_252d(volume: pd.Series) -> pd.Series:
    """Spike-day count / window: 252-day clustering density (2x median)."""
    flag = _spike_flag_median(volume, _TD_MON, 2.0)
    return _rolling_count_true(flag > 0, _TD_YEAR) / _TD_YEAR


def vb_200_spike_vol_turnover_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63-day spike volume turnover (all-history extremity)."""
    ratio = _vol_ratio_vs_median(volume, _TD_MON)
    spike_vol = volume.where(ratio > 2.0, 0.0)
    turnover63 = _safe_div(_rolling_sum(spike_vol, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return turnover63.expanding(min_periods=5).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_BLOWOFF_REGISTRY_076_150 = {
    "vb_076_consec_spike_days_2x_median": {"inputs": ["volume"], "func": vb_076_consec_spike_days_2x_median},
    "vb_077_consec_spike_days_3x_median": {"inputs": ["volume"], "func": vb_077_consec_spike_days_3x_median},
    "vb_078_consec_spike_days_zscore_gt2": {"inputs": ["volume"], "func": vb_078_consec_spike_days_zscore_gt2},
    "vb_079_max_consec_spike_2x_median_21d": {"inputs": ["volume"], "func": vb_079_max_consec_spike_2x_median_21d},
    "vb_080_max_consec_spike_2x_median_63d": {"inputs": ["volume"], "func": vb_080_max_consec_spike_2x_median_63d},
    "vb_081_max_consec_spike_2x_median_252d": {"inputs": ["volume"], "func": vb_081_max_consec_spike_2x_median_252d},
    "vb_082_spike_cluster_density_21d": {"inputs": ["volume"], "func": vb_082_spike_cluster_density_21d},
    "vb_083_spike_cluster_density_63d": {"inputs": ["volume"], "func": vb_083_spike_cluster_density_63d},
    "vb_084_spike_cluster_score_21d": {"inputs": ["volume"], "func": vb_084_spike_cluster_score_21d},
    "vb_085_spike_cluster_score_63d": {"inputs": ["volume"], "func": vb_085_spike_cluster_score_63d},
    "vb_086_spike_cluster_score_252d": {"inputs": ["volume"], "func": vb_086_spike_cluster_score_252d},
    "vb_087_spike_count_21d_norm_252d": {"inputs": ["volume"], "func": vb_087_spike_count_21d_norm_252d},
    "vb_088_spike_count_63d_norm_252d": {"inputs": ["volume"], "func": vb_088_spike_count_63d_norm_252d},
    "vb_089_days_since_last_spike_2x": {"inputs": ["volume"], "func": vb_089_days_since_last_spike_2x},
    "vb_090_spike_recency_score_21d": {"inputs": ["volume"], "func": vb_090_spike_recency_score_21d},
    "vb_091_spike_ratio_on_down_days_21d": {"inputs": ["close", "volume"], "func": vb_091_spike_ratio_on_down_days_21d},
    "vb_092_spike_ratio_on_down_days_63d": {"inputs": ["close", "volume"], "func": vb_092_spike_ratio_on_down_days_63d},
    "vb_093_spike_ratio_on_up_days_21d": {"inputs": ["close", "volume"], "func": vb_093_spike_ratio_on_up_days_21d},
    "vb_094_spike_count_on_down_days_63d": {"inputs": ["close", "volume"], "func": vb_094_spike_count_on_down_days_63d},
    "vb_095_spike_count_on_down_days_252d": {"inputs": ["close", "volume"], "func": vb_095_spike_count_on_down_days_252d},
    "vb_096_spike_down_up_ratio_63d": {"inputs": ["close", "volume"], "func": vb_096_spike_down_up_ratio_63d},
    "vb_097_spike_down_up_ratio_252d": {"inputs": ["close", "volume"], "func": vb_097_spike_down_up_ratio_252d},
    "vb_098_max_spike_ratio_on_down_days_63d": {"inputs": ["close", "volume"], "func": vb_098_max_spike_ratio_on_down_days_63d},
    "vb_099_max_spike_ratio_on_down_days_252d": {"inputs": ["close", "volume"], "func": vb_099_max_spike_ratio_on_down_days_252d},
    "vb_100_spike_vol_zscore_on_down_days_63d": {"inputs": ["close", "volume"], "func": vb_100_spike_vol_zscore_on_down_days_63d},
    "vb_101_spike_on_gap_down_days_63d": {"inputs": ["close", "open", "volume"], "func": vb_101_spike_on_gap_down_days_63d},
    "vb_102_spike_on_new_52wk_low_days_252d": {"inputs": ["close", "volume"], "func": vb_102_spike_on_new_52wk_low_days_252d},
    "vb_103_vol_ratio_on_large_down_day_21d": {"inputs": ["close", "volume"], "func": vb_103_vol_ratio_on_large_down_day_21d},
    "vb_104_spike_on_high_range_day_63d": {"inputs": ["close", "high", "low", "volume"], "func": vb_104_spike_on_high_range_day_63d},
    "vb_105_spike_on_low_close_rank_day_63d": {"inputs": ["close", "volume"], "func": vb_105_spike_on_low_close_rank_day_63d},
    "vb_106_spike_ratio_zscore_252d": {"inputs": ["volume"], "func": vb_106_spike_ratio_zscore_252d},
    "vb_107_spike_ratio_pct_rank_504d": {"inputs": ["volume"], "func": vb_107_spike_ratio_pct_rank_504d},
    "vb_108_max_spike_ratio_expanding_rank": {"inputs": ["volume"], "func": vb_108_max_spike_ratio_expanding_rank},
    "vb_109_spike_magnitude_norm_21d_avg": {"inputs": ["volume"], "func": vb_109_spike_magnitude_norm_21d_avg},
    "vb_110_excess_ratio_above_2x_median_21d": {"inputs": ["volume"], "func": vb_110_excess_ratio_above_2x_median_21d},
    "vb_111_excess_ratio_above_3x_median_21d": {"inputs": ["volume"], "func": vb_111_excess_ratio_above_3x_median_21d},
    "vb_112_sum_excess_ratio_63d": {"inputs": ["volume"], "func": vb_112_sum_excess_ratio_63d},
    "vb_113_sum_excess_ratio_252d": {"inputs": ["volume"], "func": vb_113_sum_excess_ratio_252d},
    "vb_114_max_excess_ratio_63d": {"inputs": ["volume"], "func": vb_114_max_excess_ratio_63d},
    "vb_115_max_excess_ratio_252d": {"inputs": ["volume"], "func": vb_115_max_excess_ratio_252d},
    "vb_116_spike_ratio_ewm_21d": {"inputs": ["volume"], "func": vb_116_spike_ratio_ewm_21d},
    "vb_117_spike_ratio_ewm_63d": {"inputs": ["volume"], "func": vb_117_spike_ratio_ewm_63d},
    "vb_118_max_vol_raw_63d": {"inputs": ["volume"], "func": vb_118_max_vol_raw_63d},
    "vb_119_max_vol_raw_252d": {"inputs": ["volume"], "func": vb_119_max_vol_raw_252d},
    "vb_120_current_vol_vs_max_63d": {"inputs": ["volume"], "func": vb_120_current_vol_vs_max_63d},
    "vb_121_vol_decay_since_spike_5d": {"inputs": ["volume"], "func": vb_121_vol_decay_since_spike_5d},
    "vb_122_vol_decay_since_spike_21d": {"inputs": ["volume"], "func": vb_122_vol_decay_since_spike_21d},
    "vb_123_vol_decay_since_spike_63d": {"inputs": ["volume"], "func": vb_123_vol_decay_since_spike_63d},
    "vb_124_vol_stddev_21d_norm_by_mean": {"inputs": ["volume"], "func": vb_124_vol_stddev_21d_norm_by_mean},
    "vb_125_vol_stddev_63d_norm_by_mean": {"inputs": ["volume"], "func": vb_125_vol_stddev_63d_norm_by_mean},
    "vb_126_vol_stddev_252d_norm_by_mean": {"inputs": ["volume"], "func": vb_126_vol_stddev_252d_norm_by_mean},
    "vb_127_vol_iqr_21d_norm_by_median": {"inputs": ["volume"], "func": vb_127_vol_iqr_21d_norm_by_median},
    "vb_128_vol_iqr_63d_norm_by_median": {"inputs": ["volume"], "func": vb_128_vol_iqr_63d_norm_by_median},
    "vb_129_vol_90th_pct_63d_norm_median": {"inputs": ["volume"], "func": vb_129_vol_90th_pct_63d_norm_median},
    "vb_130_vol_95th_pct_252d_norm_median": {"inputs": ["volume"], "func": vb_130_vol_95th_pct_252d_norm_median},
    "vb_131_vol_75th_pct_21d_norm_median": {"inputs": ["volume"], "func": vb_131_vol_75th_pct_21d_norm_median},
    "vb_132_spike_half_life_21d": {"inputs": ["volume"], "func": vb_132_spike_half_life_21d},
    "vb_133_spike_half_life_63d": {"inputs": ["volume"], "func": vb_133_spike_half_life_63d},
    "vb_134_spike_vol_momentum_5d": {"inputs": ["volume"], "func": vb_134_spike_vol_momentum_5d},
    "vb_135_spike_vol_momentum_21d": {"inputs": ["volume"], "func": vb_135_spike_vol_momentum_21d},
    "vb_136_blowoff_composite_score_21d": {"inputs": ["volume"], "func": vb_136_blowoff_composite_score_21d},
    "vb_137_blowoff_composite_score_63d": {"inputs": ["volume"], "func": vb_137_blowoff_composite_score_63d},
    "vb_138_spike_down_day_blowoff_score_63d": {"inputs": ["close", "volume"], "func": vb_138_spike_down_day_blowoff_score_63d},
    "vb_139_blowoff_index_weighted_21d": {"inputs": ["volume"], "func": vb_139_blowoff_index_weighted_21d},
    "vb_140_blowoff_index_weighted_63d": {"inputs": ["volume"], "func": vb_140_blowoff_index_weighted_63d},
    "vb_141_spike_ratio_vs_1yr_max_ratio": {"inputs": ["volume"], "func": vb_141_spike_ratio_vs_1yr_max_ratio},
    "vb_142_spike_ratio_vs_1yr_avg_spike": {"inputs": ["volume"], "func": vb_142_spike_ratio_vs_1yr_avg_spike},
    "vb_143_spike_surprise_index_21d": {"inputs": ["volume"], "func": vb_143_spike_surprise_index_21d},
    "vb_144_spike_surprise_index_63d": {"inputs": ["volume"], "func": vb_144_spike_surprise_index_63d},
    "vb_145_spike_surprise_index_252d": {"inputs": ["volume"], "func": vb_145_spike_surprise_index_252d},
    "vb_146_spike_ratio_21d_zscore_504d": {"inputs": ["volume"], "func": vb_146_spike_ratio_21d_zscore_504d},
    "vb_147_spike_count_21d_pct_rank_504d": {"inputs": ["volume"], "func": vb_147_spike_count_21d_pct_rank_504d},
    "vb_148_spike_cluster_vs_history_score": {"inputs": ["volume"], "func": vb_148_spike_cluster_vs_history_score},
    "vb_149_spike_vol_stddev_ratio_21d": {"inputs": ["volume"], "func": vb_149_spike_vol_stddev_ratio_21d},
    "vb_150_blowoff_distress_index": {"inputs": ["close", "volume"], "func": vb_150_blowoff_distress_index},
    "vb_176_spike_ratio_on_gap_up_days_63d": {"inputs": ["close", "open", "volume"], "func": vb_176_spike_ratio_on_gap_up_days_63d},
    "vb_177_spike_count_on_gap_down_days_252d": {"inputs": ["close", "open", "volume"], "func": vb_177_spike_count_on_gap_down_days_252d},
    "vb_178_vol_ratio_on_gap_down_day_21d": {"inputs": ["close", "open", "volume"], "func": vb_178_vol_ratio_on_gap_down_day_21d},
    "vb_179_spike_on_new_21d_low_days_63d": {"inputs": ["close", "volume"], "func": vb_179_spike_on_new_21d_low_days_63d},
    "vb_180_spike_on_new_63d_low_days_252d": {"inputs": ["close", "volume"], "func": vb_180_spike_on_new_63d_low_days_252d},
    "vb_181_vol_ratio_on_large_up_day_21d": {"inputs": ["close", "volume"], "func": vb_181_vol_ratio_on_large_up_day_21d},
    "vb_182_spike_asymmetry_ratio_63d": {"inputs": ["close", "volume"], "func": vb_182_spike_asymmetry_ratio_63d},
    "vb_183_spike_on_wk_low_63d": {"inputs": ["close", "volume"], "func": vb_183_spike_on_wk_low_63d},
    "vb_184_vol_range_spike_ratio_21d": {"inputs": ["high", "low", "volume"], "func": vb_184_vol_range_spike_ratio_21d},
    "vb_185_spike_vol_on_wide_bar_63d": {"inputs": ["high", "low", "volume"], "func": vb_185_spike_vol_on_wide_bar_63d},
    "vb_186_spike_count_3x_median_21d": {"inputs": ["volume"], "func": vb_186_spike_count_3x_median_21d},
    "vb_187_spike_count_2x_median_5d": {"inputs": ["volume"], "func": vb_187_spike_count_2x_median_5d},
    "vb_188_spike_fraction_3x_median_63d": {"inputs": ["volume"], "func": vb_188_spike_fraction_3x_median_63d},
    "vb_189_spike_fraction_3x_median_252d": {"inputs": ["volume"], "func": vb_189_spike_fraction_3x_median_252d},
    "vb_190_spike_vol_turnover_21d": {"inputs": ["volume"], "func": vb_190_spike_vol_turnover_21d},
    "vb_191_spike_vol_turnover_63d": {"inputs": ["volume"], "func": vb_191_spike_vol_turnover_63d},
    "vb_192_blowoff_composite_score_252d": {"inputs": ["volume"], "func": vb_192_blowoff_composite_score_252d},
    "vb_193_spike_ratio_ewm_126d": {"inputs": ["volume"], "func": vb_193_spike_ratio_ewm_126d},
    "vb_194_spike_count_21d_pct_rank_126d": {"inputs": ["volume"], "func": vb_194_spike_count_21d_pct_rank_126d},
    "vb_195_max_vol_ratio_vs_mean_252d": {"inputs": ["volume"], "func": vb_195_max_vol_ratio_vs_mean_252d},
    "vb_196_spike_ratio_range_63d": {"inputs": ["volume"], "func": vb_196_spike_ratio_range_63d},
    "vb_197_spike_ratio_range_252d": {"inputs": ["volume"], "func": vb_197_spike_ratio_range_252d},
    "vb_198_blowoff_index_weighted_252d": {"inputs": ["volume"], "func": vb_198_blowoff_index_weighted_252d},
    "vb_199_spike_cluster_density_252d": {"inputs": ["volume"], "func": vb_199_spike_cluster_density_252d},
    "vb_200_spike_vol_turnover_expanding_rank": {"inputs": ["volume"], "func": vb_200_spike_vol_turnover_expanding_rank},
}
