"""
116_extreme_day_density — Base Features 076-150
Domain: density, spacing and clustering of isolated extreme down-days — rolling window
        variants, sigma-adaptive thresholds, clustering scores, inter-arrival statistics,
        volume-confirmed extreme days, run-length and burstiness measures.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _daily_return(close: pd.Series) -> pd.Series:
    """Simple daily log return."""
    return np.log(close / close.shift(1))


def _extreme_flag(close: pd.Series, threshold: float) -> pd.Series:
    """Binary flag: 1 where daily log return <= threshold, else 0."""
    ret = _daily_return(close)
    return (ret <= threshold).astype(float)


def _sigma_extreme_flag(close: pd.Series, window: int, sigma_mult: float) -> pd.Series:
    """Binary flag: 1 where return <= -sigma_mult * rolling_std over window."""
    ret = _daily_return(close)
    std = _rolling_std(ret, window)
    threshold = -sigma_mult * std
    return (ret <= threshold).astype(float)


def _time_since_last_extreme(flag: pd.Series) -> pd.Series:
    """Days elapsed since the most recent 1 in flag (0 = current day is extreme)."""
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill()
    elapsed = idx - last
    elapsed = elapsed.where(~flag.isna(), np.nan)
    return elapsed


def _rolling_spacing_std(flag: pd.Series, w: int) -> pd.Series:
    """Std of gaps between consecutive extreme days in trailing w-day window."""
    def _std_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 3:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 2:
            return np.nan
        return gaps.std()
    return flag.rolling(w, min_periods=max(2, w // 2)).apply(_std_gap, raw=True)


def _rolling_max_gap(flag: pd.Series, w: int) -> pd.Series:
    """Maximum gap between consecutive extreme days in trailing w-day window."""
    def _max_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return gaps.max()
    return flag.rolling(w, min_periods=max(2, w // 2)).apply(_max_gap, raw=True)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Expanding-window counts and fractions ---

def edd_076_count_neg5pct_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-time count of days with log return <= -5%."""
    return _extreme_flag(close, -0.05).expanding(min_periods=1).sum()


def edd_077_count_neg10pct_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-time count of days with log return <= -10%."""
    return _extreme_flag(close, -0.10).expanding(min_periods=1).sum()


def edd_078_frac_neg5pct_expanding(close: pd.Series) -> pd.Series:
    """Expanding all-time fraction of days with log return <= -5%."""
    flag = _extreme_flag(close, -0.05)
    cnt = flag.expanding(min_periods=1).sum()
    n = pd.Series(np.arange(1, len(flag) + 1, dtype=float), index=flag.index)
    return _safe_div(cnt, n)


def edd_079_count_2sigma_expanding(close: pd.Series) -> pd.Series:
    """Expanding count of 2-sigma down days (63d std)."""
    return _sigma_extreme_flag(close, _TD_QTR, 2.0).expanding(min_periods=1).sum()


def edd_080_frac_neg5pct_5d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 5 days with log return <= -5% (weekly extreme density)."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_WEEK) / _TD_WEEK


def edd_081_count_neg5pct_5d(close: pd.Series) -> pd.Series:
    """Count of trailing 5 days with log return <= -5%."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_WEEK)


def edd_082_count_neg3pct_5d(close: pd.Series) -> pd.Series:
    """Count of trailing 5 days with log return <= -3%."""
    return _rolling_sum(_extreme_flag(close, -0.03), _TD_WEEK)


def edd_083_count_neg5pct_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day -5% count relative to its 252-day distribution."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def edd_084_count_2sigma_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day 2-sigma count relative to its 252-day distribution."""
    cnt = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s)


def edd_085_count_neg5pct_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day -5% count within its trailing 252-day distribution."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def edd_086_count_2sigma_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day 2-sigma count within trailing 252-day distribution."""
    cnt = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def edd_087_count_neg5pct_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day -5% density to 252-day -5% density (recent vs historical rate)."""
    d21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    d252 = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    return _safe_div(d21, d252.clip(lower=_EPS))


def edd_088_count_neg5pct_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day to 252-day -5% density."""
    d63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    d252 = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    return _safe_div(d63, d252.clip(lower=_EPS))


def edd_089_count_2sigma_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day 2-sigma extreme density."""
    d21 = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON) / _TD_MON
    d252 = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR) / _TD_YEAR
    return _safe_div(d21, d252.clip(lower=_EPS))


def edd_090_extreme_density_trend_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of rolling 5-day extreme-5% count over trailing 63 days (rising density)."""
    cnt5d = _rolling_sum(_extreme_flag(close, -0.05), _TD_WEEK)
    def _slope(arr):
        if len(arr) < 5:
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi -= xi.mean()
        arr = arr - arr.mean()
        denom = (xi ** 2).sum()
        if denom < _EPS:
            return np.nan
        return (xi * arr).sum() / denom
    return cnt5d.rolling(_TD_QTR, min_periods=_TD_MON).apply(_slope, raw=True)


# --- Group H (091-105): Clustering and burstiness of extreme days ---

def edd_091_burstiness_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Burstiness: (std_gap - mean_gap) / (std_gap + mean_gap) for -5% days over 252d.
    +1 = maximally bursty (clustered), -1 = maximally regular."""
    def _burst(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 3:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 2:
            return np.nan
        m, s = gaps.mean(), gaps.std()
        denom = s + m
        if abs(denom) < _EPS:
            return np.nan
        return (s - m) / denom
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_burst, raw=True)


def edd_092_burstiness_2sigma_252d(close: pd.Series) -> pd.Series:
    """Burstiness of 2-sigma down days over trailing 252 days."""
    def _burst(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 3:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 2:
            return np.nan
        m, s = gaps.mean(), gaps.std()
        denom = s + m
        if abs(denom) < _EPS:
            return np.nan
        return (s - m) / denom
    return _sigma_extreme_flag(close, _TD_QTR, 2.0).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_burst, raw=True)


def edd_093_cluster_score_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Extreme cluster score: (count_5d_max / total_21d_count), measuring how bunched extreme days are."""
    flag = _extreme_flag(close, -0.05)
    cnt21 = _rolling_sum(flag, _TD_MON)
    cnt5d_max = flag.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda arr: max(
            sum(arr[max(0, i - _TD_WEEK + 1):i + 1]) for i in range(len(arr))
        ) if arr.sum() > 0 else 0.0,
        raw=True
    )
    return _safe_div(cnt5d_max, cnt21.clip(lower=_EPS))


def edd_094_max_extreme_gap_252d(close: pd.Series) -> pd.Series:
    """Maximum gap between consecutive -5% days in trailing 252 days."""
    return _rolling_max_gap(_extreme_flag(close, -0.05), _TD_YEAR)


def edd_095_max_extreme_gap_neg10pct_252d(close: pd.Series) -> pd.Series:
    """Maximum gap between consecutive -10% days in trailing 252 days."""
    return _rolling_max_gap(_extreme_flag(close, -0.10), _TD_YEAR)


def edd_096_std_spacing_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Standard deviation of gaps between -5% days in trailing 252 days."""
    return _rolling_spacing_std(_extreme_flag(close, -0.05), _TD_YEAR)


def edd_097_std_spacing_2sigma_252d(close: pd.Series) -> pd.Series:
    """Standard deviation of gaps between 2-sigma down days in trailing 252 days."""
    return _rolling_spacing_std(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR)


def edd_098_count_neg5pct_clustered_21d(close: pd.Series) -> pd.Series:
    """Count of -5% days occurring within 5 days of another -5% day in trailing 21d."""
    flag = _extreme_flag(close, -0.05)
    nearby = (flag.rolling(_TD_WEEK, min_periods=1).sum() > 1).astype(float)
    return _rolling_sum(flag * nearby, _TD_MON)


def edd_099_count_neg5pct_isolated_21d(close: pd.Series) -> pd.Series:
    """Count of -5% days NOT within 5 days of another -5% day in trailing 21 days."""
    flag = _extreme_flag(close, -0.05)
    nearby_sum = flag.rolling(_TD_WEEK * 2 + 1, min_periods=1, center=False).sum()
    isolated = (flag == 1.0) & (nearby_sum <= 1.0)
    return _rolling_sum(isolated.astype(float), _TD_MON)


def edd_100_ratio_clustered_to_total_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Ratio of clustered (within 5d) to total -5% days in trailing 63 days."""
    flag = _extreme_flag(close, -0.05)
    nearby = (flag.rolling(_TD_WEEK, min_periods=1).sum() > 1).astype(float)
    clustered = _rolling_sum(flag * nearby, _TD_QTR)
    total = _rolling_sum(flag, _TD_QTR)
    return _safe_div(clustered, total.clip(lower=_EPS))


def edd_101_inter_arrival_rate_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Inter-arrival rate of -5% days: count / 252 (Poisson rate estimate)."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR


def edd_102_inter_arrival_rate_2sigma_252d(close: pd.Series) -> pd.Series:
    """Inter-arrival rate of 2-sigma days: count / 252."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_YEAR) / _TD_YEAR


def edd_103_neg5pct_density_accel_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Acceleration: 21d -5% density minus 63d -5% density (positive = accelerating)."""
    d21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    d63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    return d21 - d63


def edd_104_neg5pct_density_accel_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Acceleration: 63d -5% density minus 252d -5% density."""
    d63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    d252 = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    return d63 - d252


def edd_105_neg3pct_density_accel_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Acceleration: 21d -3% density minus 252d -3% density."""
    d21 = _rolling_sum(_extreme_flag(close, -0.03), _TD_MON) / _TD_MON
    d252 = _rolling_sum(_extreme_flag(close, -0.03), _TD_YEAR) / _TD_YEAR
    return d21 - d252


# --- Group I (106-120): Volume-confirmed extreme days ---

def edd_106_vol_confirmed_neg5pct_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of -5% days with volume > 21d avg volume in trailing 21 days."""
    flag = _extreme_flag(close, -0.05)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_MON)


def edd_107_vol_confirmed_neg5pct_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of -5% days with volume > 21d avg volume in trailing 63 days."""
    flag = _extreme_flag(close, -0.05)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_QTR)


def edd_108_vol_confirmed_neg5pct_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of -5% days with elevated volume in trailing 63 days."""
    flag = _extreme_flag(close, -0.05)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > avg_vol).astype(float)
    confirmed = _rolling_sum(flag * high_vol, _TD_QTR)
    total = _rolling_sum(flag, _TD_QTR)
    return _safe_div(confirmed, total.clip(lower=_EPS))


def edd_109_vol_confirmed_neg10pct_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of -10% days with volume > 21d avg volume in trailing 252 days."""
    flag = _extreme_flag(close, -0.10)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_YEAR)


def edd_110_vol_ratio_on_neg5pct_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume-to-21d-avg ratio on -5% days in trailing 63 days."""
    flag = _extreme_flag(close, -0.05)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS))
    cnt = _rolling_sum(flag, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(vol_ratio * flag, _TD_QTR), cnt)


def edd_111_vol_2x_neg5pct_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of -5% days with volume > 2x 21d avg in trailing 63 days."""
    flag = _extreme_flag(close, -0.05)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol2x = (volume > 2.0 * avg_vol).astype(float)
    return _rolling_sum(flag * vol2x, _TD_QTR)


def edd_112_vol_confirmed_2sigma_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2-sigma down days with volume > 21d avg in trailing 63 days."""
    flag = _sigma_extreme_flag(close, _TD_QTR, 2.0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_QTR)


def edd_113_vol_on_extreme_days_vs_normal_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on -5% days to avg volume on non-extreme days in 63d."""
    flag = _extreme_flag(close, -0.05)
    non_flag = 1.0 - flag
    cnt_e = _rolling_sum(flag, _TD_QTR).replace(0, np.nan)
    cnt_n = _rolling_sum(non_flag, _TD_QTR).replace(0, np.nan)
    avg_e = _safe_div(_rolling_sum(volume * flag, _TD_QTR), cnt_e)
    avg_n = _safe_div(_rolling_sum(volume * non_flag, _TD_QTR), cnt_n)
    return _safe_div(avg_e, avg_n.clip(lower=_EPS))


def edd_114_extreme_dollar_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of total dollar volume transacted on -5% days in trailing 63 days."""
    flag = _extreme_flag(close, -0.05)
    dvol = close * volume
    return _safe_div(_rolling_sum(dvol * flag, _TD_QTR), _rolling_sum(dvol, _TD_QTR).clip(lower=_EPS))


def edd_115_vol_confirmed_neg5pct_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of -5% days with volume > 21d avg in trailing 252 days."""
    flag = _extreme_flag(close, -0.05)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > avg_vol).astype(float)
    return _rolling_sum(flag * high_vol, _TD_YEAR)


# --- Group J (116-130): Return-based depth scores on extreme days ---

def edd_116_min_ret_in_21d(close: pd.Series) -> pd.Series:
    """Most negative daily log return in trailing 21 days."""
    return _rolling_min(_daily_return(close), _TD_MON)


def edd_117_min_ret_in_63d(close: pd.Series) -> pd.Series:
    """Most negative daily log return in trailing 63 days."""
    return _rolling_min(_daily_return(close), _TD_QTR)


def edd_118_min_ret_in_252d(close: pd.Series) -> pd.Series:
    """Most negative daily log return in trailing 252 days (worst single day)."""
    return _rolling_min(_daily_return(close), _TD_YEAR)


def edd_119_avg_extreme_ret_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Average log return on -5% days in trailing 252 days."""
    ret = _daily_return(close)
    flag = _extreme_flag(close, -0.05)
    cnt = _rolling_sum(flag, _TD_YEAR).replace(0, np.nan)
    return _safe_div(_rolling_sum(ret * flag, _TD_YEAR), cnt)


def edd_120_worst_extreme_ret_63d(close: pd.Series) -> pd.Series:
    """Minimum return on -5% days in trailing 63 days (most extreme of the extremes)."""
    ret = _daily_return(close)
    flag = _extreme_flag(close, -0.05)
    extreme_ret = ret.where(flag == 1.0, np.nan)
    return extreme_ret.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()


def edd_121_sum_extreme_ret_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Sum of log returns on -5% days in trailing 252 days."""
    ret = _daily_return(close)
    flag = _extreme_flag(close, -0.05)
    return _rolling_sum(ret * flag, _TD_YEAR)


def edd_122_extreme_ret_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of today's log return vs 252-day return distribution."""
    ret = _daily_return(close)
    m = _rolling_mean(ret, _TD_YEAR)
    s = _rolling_std(ret, _TD_YEAR)
    return _safe_div(ret - m, s)


def edd_123_extreme_depth_score_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Sum of excess depth beyond -5% threshold on extreme days in 21 days."""
    ret = _daily_return(close)
    excess = (ret - (-0.05)).clip(upper=0.0)
    return _rolling_sum(excess, _TD_MON)


def edd_124_extreme_depth_score_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Sum of excess depth beyond -5% on extreme days in trailing 63 days."""
    ret = _daily_return(close)
    excess = (ret - (-0.05)).clip(upper=0.0)
    return _rolling_sum(excess, _TD_QTR)


def edd_125_extreme_depth_score_2sigma_63d(close: pd.Series) -> pd.Series:
    """Sum of excess negative z-score beyond -2 sigma on extreme days in 63 days."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_QTR)
    zscore = _safe_div(ret, std.clip(lower=_EPS))
    excess = (zscore - (-2.0)).clip(upper=0.0)
    return _rolling_sum(excess, _TD_QTR)


# --- Group K (126-140): Persistence and recurrence of extreme day clusters ---

def edd_126_ewm_extreme_density_neg5pct(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily -5% flag — smooth estimate of extreme day intensity."""
    return _ewm_mean(_extreme_flag(close, -0.05), _TD_MON)


def edd_127_ewm_extreme_density_neg10pct(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily -10% flag."""
    return _ewm_mean(_extreme_flag(close, -0.10), _TD_MON)


def edd_128_ewm_extreme_density_2sigma(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily 2-sigma down flag."""
    return _ewm_mean(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_MON)


def edd_129_ewm_extreme_density_neg5pct_span63(close: pd.Series) -> pd.Series:
    """EWM (span=63) of daily -5% flag — slow-moving extreme density signal."""
    return _ewm_mean(_extreme_flag(close, -0.05), _TD_QTR)


def edd_130_extreme_density_delta_ewm(close: pd.Series) -> pd.Series:
    """Difference between fast (span=5) and slow (span=63) EWM of -5% flag."""
    fast = _ewm_mean(_extreme_flag(close, -0.05), _TD_WEEK)
    slow = _ewm_mean(_extreme_flag(close, -0.05), _TD_QTR)
    return fast - slow


def edd_131_recurrence_neg5pct_in_5d_after_neg5pct(close: pd.Series) -> pd.Series:
    """Flag: a -5% day occurred within 5 days following a prior -5% day."""
    flag = _extreme_flag(close, -0.05)
    prior5 = flag.shift(1).rolling(_TD_WEEK, min_periods=1).sum()
    return ((flag == 1.0) & (prior5 > 0)).astype(float)


def edd_132_double_extreme_5pct_21d(close: pd.Series) -> pd.Series:
    """Count of pairs of back-to-back -5% days (two consecutive extreme days) in 21d."""
    flag = _extreme_flag(close, -0.05)
    pair = (flag * flag.shift(1)).fillna(0.0)
    return _rolling_sum(pair, _TD_MON)


def edd_133_triple_extreme_3pct_21d(close: pd.Series) -> pd.Series:
    """Count of 3-in-a-row -3% days in trailing 21 days."""
    flag = _extreme_flag(close, -0.03)
    triple = (flag * flag.shift(1) * flag.shift(2)).fillna(0.0)
    return _rolling_sum(triple, _TD_MON)


def edd_134_extreme_run_length_max_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive run of days with at least 1 -3% day per 5d window in 63d."""
    flag = _extreme_flag(close, -0.03)
    has_5d = (flag.rolling(_TD_WEEK, min_periods=1).sum() > 0).astype(float)

    def _max_run(arr):
        max_r, cur = 0, 0
        for v in arr:
            if v == 1.0:
                cur += 1
                max_r = max(max_r, cur)
            else:
                cur = 0
        return float(max_r)

    return has_5d.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def edd_135_recurrence_neg10pct_21d(close: pd.Series) -> pd.Series:
    """Count of -10% days in 21d following a prior -10% day within 21 days."""
    flag = _extreme_flag(close, -0.10)
    prior21 = flag.shift(1).rolling(_TD_MON, min_periods=1).sum()
    return _rolling_sum(((flag == 1.0) & (prior21 > 0)).astype(float), _TD_MON)


# --- Group L (136-150): Binary and composite flags ---

def edd_136_any_neg5pct_in_5d_flag(close: pd.Series) -> pd.Series:
    """Binary: any -5% day in trailing 5 trading days."""
    return (_rolling_sum(_extreme_flag(close, -0.05), _TD_WEEK) > 0).astype(float)


def edd_137_any_neg10pct_in_21d_flag(close: pd.Series) -> pd.Series:
    """Binary: any -10% day in trailing 21 days."""
    return (_rolling_sum(_extreme_flag(close, -0.10), _TD_MON) > 0).astype(float)


def edd_138_any_3sigma_in_21d_flag(close: pd.Series) -> pd.Series:
    """Binary: any 3-sigma down day in trailing 21 days."""
    return (_rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 3.0), _TD_MON) > 0).astype(float)


def edd_139_multi_threshold_density_score_21d(close: pd.Series) -> pd.Series:
    """Composite: count_-3% + 2*count_-5% + 4*count_-10% in 21d (weighted extreme density)."""
    c3 = _rolling_sum(_extreme_flag(close, -0.03), _TD_MON)
    c5 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    c10 = _rolling_sum(_extreme_flag(close, -0.10), _TD_MON)
    return c3 + 2.0 * c5 + 4.0 * c10


def edd_140_multi_threshold_density_score_63d(close: pd.Series) -> pd.Series:
    """Composite: count_-3% + 2*count_-5% + 4*count_-10% in 63d (weighted extreme density)."""
    c3 = _rolling_sum(_extreme_flag(close, -0.03), _TD_QTR)
    c5 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    c10 = _rolling_sum(_extreme_flag(close, -0.10), _TD_QTR)
    return c3 + 2.0 * c5 + 4.0 * c10


def edd_141_new_extreme_count_high_21d(close: pd.Series) -> pd.Series:
    """Count of -5% days in 21d that set a new 252d worst-day record on that date."""
    ret = _daily_return(close)
    flag = _extreme_flag(close, -0.05)
    prior_min = ret.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).min()
    new_low = ((flag == 1.0) & (ret < prior_min)).astype(float)
    return _rolling_sum(new_low, _TD_MON)


def edd_142_extreme_day_return_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's return in trailing 252-day return distribution."""
    ret = _daily_return(close)
    return ret.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def edd_143_extreme_density_neg5pct_21d_ewm5_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-5 extreme density to 21d count (how recently weighted vs raw)."""
    cnt21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    ewm5 = _ewm_mean(_extreme_flag(close, -0.05), _TD_WEEK)
    return _safe_div(ewm5, cnt21.clip(lower=_EPS))


def edd_144_count_neg5pct_21d_minus_63d_norm(close: pd.Series) -> pd.Series:
    """21d -5% count normalized: (count21 - count63/3) — excess above long-run rate."""
    c21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    c63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    return c21 - c63 / 3.0


def edd_145_vol_times_extreme_flag_neg5pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on today's extreme day (0 if not extreme); proxy for panic selling size."""
    flag = _extreme_flag(close, -0.05)
    return volume * flag


def edd_146_extreme_density_neg3pct_ewm21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily -3% flag — smooth moderate extreme density."""
    return _ewm_mean(_extreme_flag(close, -0.03), _TD_MON)


def edd_147_neg5pct_days_count_5wk(close: pd.Series) -> pd.Series:
    """Count of -5% days in trailing 25 days (5 weeks)."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_WEEK * 5)


def edd_148_neg5pct_days_count_10wk(close: pd.Series) -> pd.Series:
    """Count of -5% days in trailing 50 days (10 weeks)."""
    return _rolling_sum(_extreme_flag(close, -0.05), _TD_WEEK * 10)


def edd_149_extreme_density_composite_score_252d(close: pd.Series) -> pd.Series:
    """Composite extreme density z-score: z-score of (c5 + sigma2_count) over 252d."""
    c5 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    cs = _rolling_sum(_sigma_extreme_flag(close, _TD_QTR, 2.0), _TD_QTR)
    combo = c5 + cs
    m = _rolling_mean(combo, _TD_YEAR)
    s = _rolling_std(combo, _TD_YEAR)
    return _safe_div(combo - m, s)


def edd_150_extreme_day_flag_2sigma_current(close: pd.Series) -> pd.Series:
    """Binary flag: today's return <= -2 sigma (63d std) — current 2-sigma extreme day."""
    return _sigma_extreme_flag(close, _TD_QTR, 2.0)


# ── Registry ──────────────────────────────────────────────────────────────────

EXTREME_DAY_DENSITY_REGISTRY_076_150 = {
    "edd_076_count_neg5pct_expanding": {"inputs": ["close"], "func": edd_076_count_neg5pct_expanding},
    "edd_077_count_neg10pct_expanding": {"inputs": ["close"], "func": edd_077_count_neg10pct_expanding},
    "edd_078_frac_neg5pct_expanding": {"inputs": ["close"], "func": edd_078_frac_neg5pct_expanding},
    "edd_079_count_2sigma_expanding": {"inputs": ["close"], "func": edd_079_count_2sigma_expanding},
    "edd_080_frac_neg5pct_5d": {"inputs": ["close"], "func": edd_080_frac_neg5pct_5d},
    "edd_081_count_neg5pct_5d": {"inputs": ["close"], "func": edd_081_count_neg5pct_5d},
    "edd_082_count_neg3pct_5d": {"inputs": ["close"], "func": edd_082_count_neg3pct_5d},
    "edd_083_count_neg5pct_21d_zscore_252d": {"inputs": ["close"], "func": edd_083_count_neg5pct_21d_zscore_252d},
    "edd_084_count_2sigma_21d_zscore_252d": {"inputs": ["close"], "func": edd_084_count_2sigma_21d_zscore_252d},
    "edd_085_count_neg5pct_63d_pct_rank_252d": {"inputs": ["close"], "func": edd_085_count_neg5pct_63d_pct_rank_252d},
    "edd_086_count_2sigma_63d_pct_rank_252d": {"inputs": ["close"], "func": edd_086_count_2sigma_63d_pct_rank_252d},
    "edd_087_count_neg5pct_21d_vs_252d_ratio": {"inputs": ["close"], "func": edd_087_count_neg5pct_21d_vs_252d_ratio},
    "edd_088_count_neg5pct_63d_vs_252d_ratio": {"inputs": ["close"], "func": edd_088_count_neg5pct_63d_vs_252d_ratio},
    "edd_089_count_2sigma_21d_vs_252d_ratio": {"inputs": ["close"], "func": edd_089_count_2sigma_21d_vs_252d_ratio},
    "edd_090_extreme_density_trend_slope_63d": {"inputs": ["close"], "func": edd_090_extreme_density_trend_slope_63d},
    "edd_091_burstiness_neg5pct_252d": {"inputs": ["close"], "func": edd_091_burstiness_neg5pct_252d},
    "edd_092_burstiness_2sigma_252d": {"inputs": ["close"], "func": edd_092_burstiness_2sigma_252d},
    "edd_093_cluster_score_neg5pct_21d": {"inputs": ["close"], "func": edd_093_cluster_score_neg5pct_21d},
    "edd_094_max_extreme_gap_252d": {"inputs": ["close"], "func": edd_094_max_extreme_gap_252d},
    "edd_095_max_extreme_gap_neg10pct_252d": {"inputs": ["close"], "func": edd_095_max_extreme_gap_neg10pct_252d},
    "edd_096_std_spacing_neg5pct_252d": {"inputs": ["close"], "func": edd_096_std_spacing_neg5pct_252d},
    "edd_097_std_spacing_2sigma_252d": {"inputs": ["close"], "func": edd_097_std_spacing_2sigma_252d},
    "edd_098_count_neg5pct_clustered_21d": {"inputs": ["close"], "func": edd_098_count_neg5pct_clustered_21d},
    "edd_099_count_neg5pct_isolated_21d": {"inputs": ["close"], "func": edd_099_count_neg5pct_isolated_21d},
    "edd_100_ratio_clustered_to_total_neg5pct_63d": {"inputs": ["close"], "func": edd_100_ratio_clustered_to_total_neg5pct_63d},
    "edd_101_inter_arrival_rate_neg5pct_252d": {"inputs": ["close"], "func": edd_101_inter_arrival_rate_neg5pct_252d},
    "edd_102_inter_arrival_rate_2sigma_252d": {"inputs": ["close"], "func": edd_102_inter_arrival_rate_2sigma_252d},
    "edd_103_neg5pct_density_accel_21d_vs_63d": {"inputs": ["close"], "func": edd_103_neg5pct_density_accel_21d_vs_63d},
    "edd_104_neg5pct_density_accel_63d_vs_252d": {"inputs": ["close"], "func": edd_104_neg5pct_density_accel_63d_vs_252d},
    "edd_105_neg3pct_density_accel_21d_vs_252d": {"inputs": ["close"], "func": edd_105_neg3pct_density_accel_21d_vs_252d},
    "edd_106_vol_confirmed_neg5pct_count_21d": {"inputs": ["close", "volume"], "func": edd_106_vol_confirmed_neg5pct_count_21d},
    "edd_107_vol_confirmed_neg5pct_count_63d": {"inputs": ["close", "volume"], "func": edd_107_vol_confirmed_neg5pct_count_63d},
    "edd_108_vol_confirmed_neg5pct_frac_63d": {"inputs": ["close", "volume"], "func": edd_108_vol_confirmed_neg5pct_frac_63d},
    "edd_109_vol_confirmed_neg10pct_count_252d": {"inputs": ["close", "volume"], "func": edd_109_vol_confirmed_neg10pct_count_252d},
    "edd_110_vol_ratio_on_neg5pct_days_63d": {"inputs": ["close", "volume"], "func": edd_110_vol_ratio_on_neg5pct_days_63d},
    "edd_111_vol_2x_neg5pct_count_63d": {"inputs": ["close", "volume"], "func": edd_111_vol_2x_neg5pct_count_63d},
    "edd_112_vol_confirmed_2sigma_count_63d": {"inputs": ["close", "volume"], "func": edd_112_vol_confirmed_2sigma_count_63d},
    "edd_113_vol_on_extreme_days_vs_normal_63d": {"inputs": ["close", "volume"], "func": edd_113_vol_on_extreme_days_vs_normal_63d},
    "edd_114_extreme_dollar_vol_share_63d": {"inputs": ["close", "volume"], "func": edd_114_extreme_dollar_vol_share_63d},
    "edd_115_vol_confirmed_neg5pct_count_252d": {"inputs": ["close", "volume"], "func": edd_115_vol_confirmed_neg5pct_count_252d},
    "edd_116_min_ret_in_21d": {"inputs": ["close"], "func": edd_116_min_ret_in_21d},
    "edd_117_min_ret_in_63d": {"inputs": ["close"], "func": edd_117_min_ret_in_63d},
    "edd_118_min_ret_in_252d": {"inputs": ["close"], "func": edd_118_min_ret_in_252d},
    "edd_119_avg_extreme_ret_neg5pct_252d": {"inputs": ["close"], "func": edd_119_avg_extreme_ret_neg5pct_252d},
    "edd_120_worst_extreme_ret_63d": {"inputs": ["close"], "func": edd_120_worst_extreme_ret_63d},
    "edd_121_sum_extreme_ret_neg5pct_252d": {"inputs": ["close"], "func": edd_121_sum_extreme_ret_neg5pct_252d},
    "edd_122_extreme_ret_zscore_252d": {"inputs": ["close"], "func": edd_122_extreme_ret_zscore_252d},
    "edd_123_extreme_depth_score_neg5pct_21d": {"inputs": ["close"], "func": edd_123_extreme_depth_score_neg5pct_21d},
    "edd_124_extreme_depth_score_neg5pct_63d": {"inputs": ["close"], "func": edd_124_extreme_depth_score_neg5pct_63d},
    "edd_125_extreme_depth_score_2sigma_63d": {"inputs": ["close"], "func": edd_125_extreme_depth_score_2sigma_63d},
    "edd_126_ewm_extreme_density_neg5pct": {"inputs": ["close"], "func": edd_126_ewm_extreme_density_neg5pct},
    "edd_127_ewm_extreme_density_neg10pct": {"inputs": ["close"], "func": edd_127_ewm_extreme_density_neg10pct},
    "edd_128_ewm_extreme_density_2sigma": {"inputs": ["close"], "func": edd_128_ewm_extreme_density_2sigma},
    "edd_129_ewm_extreme_density_neg5pct_span63": {"inputs": ["close"], "func": edd_129_ewm_extreme_density_neg5pct_span63},
    "edd_130_extreme_density_delta_ewm": {"inputs": ["close"], "func": edd_130_extreme_density_delta_ewm},
    "edd_131_recurrence_neg5pct_in_5d_after_neg5pct": {"inputs": ["close"], "func": edd_131_recurrence_neg5pct_in_5d_after_neg5pct},
    "edd_132_double_extreme_5pct_21d": {"inputs": ["close"], "func": edd_132_double_extreme_5pct_21d},
    "edd_133_triple_extreme_3pct_21d": {"inputs": ["close"], "func": edd_133_triple_extreme_3pct_21d},
    "edd_134_extreme_run_length_max_63d": {"inputs": ["close"], "func": edd_134_extreme_run_length_max_63d},
    "edd_135_recurrence_neg10pct_21d": {"inputs": ["close"], "func": edd_135_recurrence_neg10pct_21d},
    "edd_136_any_neg5pct_in_5d_flag": {"inputs": ["close"], "func": edd_136_any_neg5pct_in_5d_flag},
    "edd_137_any_neg10pct_in_21d_flag": {"inputs": ["close"], "func": edd_137_any_neg10pct_in_21d_flag},
    "edd_138_any_3sigma_in_21d_flag": {"inputs": ["close"], "func": edd_138_any_3sigma_in_21d_flag},
    "edd_139_multi_threshold_density_score_21d": {"inputs": ["close"], "func": edd_139_multi_threshold_density_score_21d},
    "edd_140_multi_threshold_density_score_63d": {"inputs": ["close"], "func": edd_140_multi_threshold_density_score_63d},
    "edd_141_new_extreme_count_high_21d": {"inputs": ["close"], "func": edd_141_new_extreme_count_high_21d},
    "edd_142_extreme_day_return_pct_rank_252d": {"inputs": ["close"], "func": edd_142_extreme_day_return_pct_rank_252d},
    "edd_143_extreme_density_neg5pct_21d_ewm5_ratio": {"inputs": ["close"], "func": edd_143_extreme_density_neg5pct_21d_ewm5_ratio},
    "edd_144_count_neg5pct_21d_minus_63d_norm": {"inputs": ["close"], "func": edd_144_count_neg5pct_21d_minus_63d_norm},
    "edd_145_vol_times_extreme_flag_neg5pct": {"inputs": ["close", "volume"], "func": edd_145_vol_times_extreme_flag_neg5pct},
    "edd_146_extreme_density_neg3pct_ewm21": {"inputs": ["close"], "func": edd_146_extreme_density_neg3pct_ewm21},
    "edd_147_neg5pct_days_count_5wk": {"inputs": ["close"], "func": edd_147_neg5pct_days_count_5wk},
    "edd_148_neg5pct_days_count_10wk": {"inputs": ["close"], "func": edd_148_neg5pct_days_count_10wk},
    "edd_149_extreme_density_composite_score_252d": {"inputs": ["close"], "func": edd_149_extreme_density_composite_score_252d},
    "edd_150_extreme_day_flag_2sigma_current": {"inputs": ["close"], "func": edd_150_extreme_day_flag_2sigma_current},
}
