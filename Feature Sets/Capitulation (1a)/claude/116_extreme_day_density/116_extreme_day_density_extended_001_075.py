"""
116_extreme_day_density — Extended Features 001-075
Domain: deeper variants of extreme-day-density — adaptive sigma thresholds, high/low-based
        extreme days, intraday range extremes, inter-arrival distribution shape, tail
        concentration indices, regime-conditioned density, multi-asset-inspired metrics.
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
    """Days elapsed since the most recent 1 in flag."""
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill()
    elapsed = idx - last
    elapsed = elapsed.where(~flag.isna(), np.nan)
    return elapsed


def _rolling_spacing_mean(flag: pd.Series, w: int) -> pd.Series:
    """Mean gap in days between consecutive extreme days in trailing w-day window."""
    def _mean_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return gaps.mean()
    return flag.rolling(w, min_periods=max(2, w // 2)).apply(_mean_gap, raw=True)


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


# ── Extended Feature functions 001-075 ────────────────────────────────────────

# --- Group A (001-015): Adaptive-sigma thresholds using longer baselines ---

def edd_ext_001_count_2sigma_252d_std_21d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (252d std) in trailing 21 days."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_YEAR)
    flag = (ret <= -2.0 * std).astype(float)
    return _rolling_sum(flag, _TD_MON)


def edd_ext_002_count_2sigma_252d_std_63d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (252d std) in trailing 63 days."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_YEAR)
    flag = (ret <= -2.0 * std).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_003_count_3sigma_252d_std_252d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -3 sigma (252d std) in trailing 252 days."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_YEAR)
    flag = (ret <= -3.0 * std).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def edd_ext_004_days_since_last_2sigma_252d_std(close: pd.Series) -> pd.Series:
    """Days since last 2-sigma down day (252d std baseline)."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_YEAR)
    flag = (ret <= -2.0 * std).astype(float)
    return _time_since_last_extreme(flag)


def edd_ext_005_frac_2sigma_252d_std_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days with return <= -2 sigma (252d std)."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_YEAR)
    flag = (ret <= -2.0 * std).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


def edd_ext_006_count_2sigma_half_std_63d(close: pd.Series) -> pd.Series:
    """Count of days with return <= -2 sigma (126d std) in trailing 63 days."""
    ret = _daily_return(close)
    std = _rolling_std(ret, _TD_HALF)
    flag = (ret <= -2.0 * std).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_007_sigma_adaptive_count_21d(close: pd.Series) -> pd.Series:
    """Count of days where return z-score (21d std) <= -1.5 in trailing 21 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_MON, 1.5), _TD_MON)


def edd_ext_008_sigma_adaptive_count_63d(close: pd.Series) -> pd.Series:
    """Count of days where return z-score (21d std) <= -1.5 in trailing 63 days."""
    return _rolling_sum(_sigma_extreme_flag(close, _TD_MON, 1.5), _TD_QTR)


def edd_ext_009_tail_pctile5_extreme_count_63d(close: pd.Series) -> pd.Series:
    """Count of days in the bottom 5th percentile of trailing 252d returns in last 63 days."""
    ret = _daily_return(close)
    pct5 = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    flag = (ret <= pct5).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_010_tail_pctile1_extreme_count_252d(close: pd.Series) -> pd.Series:
    """Count of days in the bottom 1st percentile of trailing 252d returns in last 252 days."""
    ret = _daily_return(close)
    pct1 = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.01)
    flag = (ret <= pct1).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def edd_ext_011_tail_pctile10_extreme_count_63d(close: pd.Series) -> pd.Series:
    """Count of days in the bottom 10th percentile of trailing 252d returns in last 63 days."""
    ret = _daily_return(close)
    pct10 = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    flag = (ret <= pct10).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_012_frac_tail_pctile5_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days in bottom 5th percentile of 252d return distribution."""
    ret = _daily_return(close)
    pct5 = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    flag = (ret <= pct5).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


def edd_ext_013_days_since_last_pctile5(close: pd.Series) -> pd.Series:
    """Days since last day in bottom 5th percentile of 252d return distribution."""
    ret = _daily_return(close)
    pct5 = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    flag = (ret <= pct5).astype(float)
    return _time_since_last_extreme(flag)


def edd_ext_014_count_2sigma_adaptive_21d_21d(close: pd.Series) -> pd.Series:
    """Count of 2-sigma (21d expanding std) extreme days in trailing 21 days."""
    ret = _daily_return(close)
    std = ret.expanding(min_periods=5).std()
    flag = (ret <= -2.0 * std).astype(float)
    return _rolling_sum(flag, _TD_MON)


def edd_ext_015_tail_concentration_index_252d(close: pd.Series) -> pd.Series:
    """Tail concentration: sum of squared extreme returns / sum of squared all-neg returns in 252d.
    High = damage concentrated in extreme days."""
    ret = _daily_return(close)
    neg_ret = ret.clip(upper=0.0)
    flag5 = _extreme_flag(close, -0.05)
    extreme_ss = _rolling_sum((ret * flag5) ** 2, _TD_YEAR)
    total_ss = _rolling_sum(neg_ret ** 2, _TD_YEAR)
    return _safe_div(extreme_ss, total_ss.clip(lower=_EPS))


# --- Group B (016-030): High/low-based extreme day measures ---

def edd_ext_016_count_high_to_close_neg5pct_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of days with high-to-close return <= -5% in trailing 63 days (intraday reversal)."""
    htc_ret = np.log(close / high)
    flag = (htc_ret <= -0.05).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_017_count_open_to_close_neg5pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days with open-to-close return <= -5% in trailing 63 days."""
    otc_ret = np.log(close / open)
    flag = (otc_ret <= -0.05).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_018_count_high_to_low_range_gt10pct_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with high-to-low range > 10% in trailing 63 days (panic bar)."""
    rng = np.log(high / low.clip(lower=_EPS))
    flag = (rng >= 0.10).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_019_count_gap_down_neg5pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days with gap-down (open vs prior close) <= -5% in trailing 63 days."""
    gap_ret = np.log(open / close.shift(1))
    flag = (gap_ret <= -0.05).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_020_count_gap_down_neg3pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days with gap-down <= -3% in trailing 63 days."""
    gap_ret = np.log(open / close.shift(1))
    flag = (gap_ret <= -0.03).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_021_days_since_last_gap_down_neg5pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Days since last gap-down <= -5%."""
    gap_ret = np.log(open / close.shift(1))
    flag = (gap_ret <= -0.05).astype(float)
    return _time_since_last_extreme(flag)


def edd_ext_022_count_close_at_low_extreme_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where close equals or is within 0.5% of the day's low in 63 days."""
    diff = _safe_div(close - low, low.clip(lower=_EPS))
    flag = (diff <= 0.005).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def edd_ext_023_extreme_intraday_range_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of high-to-low range on -3% close days in trailing 63 days."""
    ret = _daily_return(close)
    flag = (ret <= -0.03).astype(float)
    rng = np.log(high / low.clip(lower=_EPS))
    return _rolling_sum(rng * flag, _TD_QTR)


def edd_ext_024_count_open_to_close_neg3pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days with open-to-close return <= -3% in trailing 21 days."""
    otc_ret = np.log(close / open)
    flag = (otc_ret <= -0.03).astype(float)
    return _rolling_sum(flag, _TD_MON)


def edd_ext_025_gap_down_share_of_decline_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Share of total -3% daily decline delivered by gap-down contribution in 63 days."""
    gap_ret = np.log(open / close.shift(1))
    close_ret = np.log(close / close.shift(1))
    gap_flag = (close_ret <= -0.03).astype(float)
    gap_contrib = _rolling_sum(gap_ret.clip(upper=0.0) * gap_flag, _TD_QTR)
    total_neg = _rolling_sum(close_ret.clip(upper=0.0), _TD_QTR)
    return _safe_div(gap_contrib, total_neg.clip(upper=-_EPS))


# --- Group C (031-045): Inter-arrival distribution shape and tail statistics ---

def edd_ext_026_spacing_skew_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Skewness of inter-arrival gaps for -5% days in trailing 252 days.
    Positive = heavy right tail (one very long gap among clusters)."""
    def _skew_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 4:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 3:
            return np.nan
        m = gaps.mean()
        s = gaps.std()
        if s < _EPS:
            return 0.0
        return float(np.mean(((gaps - m) / s) ** 3))
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_skew_gap, raw=True)


def edd_ext_027_spacing_kurtosis_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of inter-arrival gaps for -5% days in trailing 252 days."""
    def _kurt_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 5:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 4:
            return np.nan
        m = gaps.mean()
        s = gaps.std()
        if s < _EPS:
            return 0.0
        return float(np.mean(((gaps - m) / s) ** 4)) - 3.0
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_kurt_gap, raw=True)


def edd_ext_028_spacing_median_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Median inter-arrival gap for -5% days in trailing 252 days."""
    def _med_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return float(np.median(gaps))
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_med_gap, raw=True)


def edd_ext_029_spacing_p75_neg5pct_252d(close: pd.Series) -> pd.Series:
    """75th percentile inter-arrival gap for -5% days in trailing 252 days."""
    def _p75_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return float(np.percentile(gaps, 75))
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_p75_gap, raw=True)


def edd_ext_030_spacing_p25_neg5pct_252d(close: pd.Series) -> pd.Series:
    """25th percentile inter-arrival gap for -5% days in trailing 252 days."""
    def _p25_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 2:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) == 0:
            return np.nan
        return float(np.percentile(gaps, 25))
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_p25_gap, raw=True)


def edd_ext_031_iqr_spacing_neg5pct_252d(close: pd.Series) -> pd.Series:
    """Interquartile range of inter-arrival gaps for -5% days in trailing 252 days."""
    def _iqr_gap(arr):
        hits = np.where(arr == 1.0)[0]
        if len(hits) < 3:
            return np.nan
        gaps = np.diff(hits.astype(float))
        gaps = gaps[~np.isnan(gaps)]
        if len(gaps) < 2:
            return np.nan
        return float(np.percentile(gaps, 75) - np.percentile(gaps, 25))
    return _extreme_flag(close, -0.05).rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_iqr_gap, raw=True)


def edd_ext_032_mean_spacing_neg5pct_63d_norm_21d(close: pd.Series) -> pd.Series:
    """Mean spacing between -5% days in 63d normalized by 21-day window (relative to monthly)."""
    mean_sp = _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_QTR)
    return mean_sp / _TD_MON


def edd_ext_033_count_extreme_before_new_low_21d(close: pd.Series) -> pd.Series:
    """Count of -5% days in 21d occurring when the prior 252-day low was recently set."""
    flag = _extreme_flag(close, -0.05)
    price_min252 = close.rolling(_TD_YEAR, min_periods=_TD_QTR).min()
    new_low = (close <= price_min252.shift(1)).astype(float)
    new_low_recent = new_low.rolling(_TD_WEEK, min_periods=1).max()
    preceded = (flag * new_low_recent).clip(upper=1.0)
    return _rolling_sum(preceded, _TD_MON)


def edd_ext_034_spacing_ratio_mean_to_window_252d(close: pd.Series) -> pd.Series:
    """Mean spacing / 252 — fraction of year between average extreme days."""
    mean_sp = _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_YEAR)
    return mean_sp / _TD_YEAR


def edd_ext_035_count_neg5pct_within_2d_of_neg3pct_63d(close: pd.Series) -> pd.Series:
    """Count of -5% days occurring within 2 days of a -3% day in trailing 63 days."""
    flag5 = _extreme_flag(close, -0.05)
    flag3 = _extreme_flag(close, -0.03)
    near3 = (flag3.rolling(5, min_periods=1).sum() > 1).astype(float)
    return _rolling_sum(flag5 * near3, _TD_QTR)


# --- Group D (036-050): Regime-conditioned extreme day density ---

def edd_ext_036_extreme_density_in_bear_regime_63d(close: pd.Series) -> pd.Series:
    """Count of -5% days in last 63d during bear regime (close < 200d MA)."""
    flag5 = _extreme_flag(close, -0.05)
    ma200 = _rolling_mean(close, _TD_YEAR)
    bear = (close < ma200).astype(float)
    return _rolling_sum(flag5 * bear, _TD_QTR)


def edd_ext_037_extreme_density_in_bull_regime_63d(close: pd.Series) -> pd.Series:
    """Count of -5% days in last 63d during bull regime (close >= 200d MA)."""
    flag5 = _extreme_flag(close, -0.05)
    ma200 = _rolling_mean(close, _TD_YEAR)
    bull = (close >= ma200).astype(float)
    return _rolling_sum(flag5 * bull, _TD_QTR)


def edd_ext_038_bear_regime_extreme_density_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63d bear-regime -5% density to overall 63d -5% density."""
    flag5 = _extreme_flag(close, -0.05)
    ma200 = _rolling_mean(close, _TD_YEAR)
    bear = (close < ma200).astype(float)
    in_bear = _rolling_sum(flag5 * bear, _TD_QTR)
    total = _rolling_sum(flag5, _TD_QTR)
    return _safe_div(in_bear, total.clip(lower=_EPS))


def edd_ext_039_high_vol_regime_extreme_count_63d(close: pd.Series) -> pd.Series:
    """Count of -5% days in last 63d during high-vol regime (21d vol > 63d avg vol)."""
    ret = _daily_return(close)
    vol21 = _rolling_std(ret, _TD_MON)
    avg_vol = _rolling_mean(vol21, _TD_QTR)
    high_vol = (vol21 > avg_vol).astype(float)
    flag5 = _extreme_flag(close, -0.05)
    return _rolling_sum(flag5 * high_vol, _TD_QTR)


def edd_ext_040_extreme_density_after_gap_down_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of -5% days within 5 days of a gap-down of >= -3% in trailing 21 days."""
    flag5 = _extreme_flag(close, -0.05)
    gap = np.log(open / close.shift(1))
    gap_flag = (gap <= -0.03).astype(float)
    gap_near = gap_flag.rolling(_TD_WEEK, min_periods=1).max()
    return _rolling_sum(flag5 * gap_near, _TD_MON)


def edd_ext_041_count_neg5pct_accelerating_period(close: pd.Series) -> pd.Series:
    """Count of -5% days in 21d when 5d density > 63d density (in acceleration phase)."""
    flag5 = _extreme_flag(close, -0.05)
    d5 = _rolling_sum(flag5, _TD_WEEK) / _TD_WEEK
    d63 = _rolling_sum(flag5, _TD_QTR) / _TD_QTR
    accel = (d5 > d63).astype(float)
    return _rolling_sum(flag5 * accel, _TD_MON)


def edd_ext_042_extreme_density_consecutive_months_63d(close: pd.Series) -> pd.Series:
    """Count of 21-day sub-windows within 63d that contain at least one -5% day."""
    flag5 = _extreme_flag(close, -0.05)
    has_month = (flag5.rolling(_TD_MON, min_periods=1).sum() > 0).astype(float)
    return has_month.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def edd_ext_043_frac_neg5pct_21d_in_bottom_decile_252d(close: pd.Series) -> pd.Series:
    """Binary: current 21-day -5% density is in the top decile of its 252-day distribution."""
    frac21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    p90 = frac21.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (frac21 >= p90).astype(float)


def edd_ext_044_count_neg5pct_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 21-day -5% count vs trailing 252-day distribution."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def edd_ext_045_extreme_day_gap_halved_flag(close: pd.Series) -> pd.Series:
    """Binary: mean spacing between -5% days in 63d is less than half the 252d mean spacing."""
    sp63 = _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_QTR)
    sp252 = _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_YEAR)
    return (sp63 < 0.5 * sp252).astype(float)


# --- Group E (046-060): Depth-weighted density metrics ---

def edd_ext_046_depth_weighted_count_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Depth-weighted count of -5% days in 21d: each extreme day weighted by |excess return|."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    depth_weight = ((-ret - 0.05).clip(lower=0.0) + 1.0) * flag5
    return _rolling_sum(depth_weight, _TD_MON)


def edd_ext_047_depth_weighted_count_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Depth-weighted count of -5% days in 63d."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    depth_weight = ((-ret - 0.05).clip(lower=0.0) + 1.0) * flag5
    return _rolling_sum(depth_weight, _TD_QTR)


def edd_ext_048_sigma_weighted_extreme_count_63d(close: pd.Series) -> pd.Series:
    """Sigma-weighted count: each -2-sigma day weighted by its sigma-multiple in 63d."""
    ret = _daily_return(close)
    std63 = _rolling_std(ret, _TD_QTR)
    zscore = _safe_div(ret, std63.clip(lower=_EPS))
    flag = (zscore <= -2.0).astype(float)
    weight = (-zscore).clip(lower=0.0) * flag
    return _rolling_sum(weight, _TD_QTR)


def edd_ext_049_extreme_count_vol_adjusted_63d(close: pd.Series) -> pd.Series:
    """Count of -5% days in 63d adjusted by current vol regime (count / vol_ratio)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    ret = _daily_return(close)
    vol63 = _rolling_std(ret, _TD_QTR)
    avg_vol = _rolling_mean(vol63, _TD_YEAR)
    vol_ratio = _safe_div(vol63, avg_vol.clip(lower=_EPS))
    return _safe_div(cnt, vol_ratio.clip(lower=_EPS))


def edd_ext_050_extreme_damage_concentration_21d(close: pd.Series) -> pd.Series:
    """Concentration: fraction of 21d total return delivered by -5% days (absolute basis)."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    extreme_sum = _rolling_sum(ret.abs() * flag5, _TD_MON)
    total_sum = _rolling_sum(ret.abs(), _TD_MON)
    return _safe_div(extreme_sum, total_sum.clip(lower=_EPS))


# --- Group F (051-065): Multi-lag and frequency decomposition ---

def edd_ext_051_count_neg5pct_21d_lag21(close: pd.Series) -> pd.Series:
    """21-day -5% count lagged by 21 days (density one month ago)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return cnt.shift(_TD_MON)


def edd_ext_052_count_neg5pct_21d_lag63(close: pd.Series) -> pd.Series:
    """21-day -5% count lagged by 63 days (density one quarter ago)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return cnt.shift(_TD_QTR)


def edd_ext_053_count_neg5pct_change_21d_vs_lag21(close: pd.Series) -> pd.Series:
    """Change: current 21-day -5% count minus count 21 days ago."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return cnt - cnt.shift(_TD_MON)


def edd_ext_054_count_neg5pct_change_63d_vs_lag63(close: pd.Series) -> pd.Series:
    """Change: current 63-day -5% count minus count 63 days ago."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR)
    return cnt - cnt.shift(_TD_QTR)


def edd_ext_055_frac_neg5pct_21d_rolling_max_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day maximum of the 21-day -5% fraction (peak density in quarter)."""
    frac21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    return _rolling_max(frac21, _TD_QTR)


def edd_ext_056_frac_neg5pct_21d_current_vs_peak_252d(close: pd.Series) -> pd.Series:
    """Current 21-day -5% fraction as fraction of its 252-day peak."""
    frac21 = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON) / _TD_MON
    peak = _rolling_max(frac21, _TD_YEAR)
    return _safe_div(frac21, peak.clip(lower=_EPS))


def edd_ext_057_count_neg5pct_streak_of_active_months_63d(close: pd.Series) -> pd.Series:
    """Count of consecutive 21-day periods ending now that each have >= 1 extreme -5% day."""
    flag5 = _extreme_flag(close, -0.05)
    has21 = (flag5.rolling(_TD_MON, min_periods=1).sum() > 0).astype(int)

    def _consec_end(arr):
        cnt = 0
        for v in reversed(arr):
            if v == 1:
                cnt += 1
            else:
                break
        return float(cnt)

    return has21.rolling(_TD_QTR, min_periods=1).apply(_consec_end, raw=True)


def edd_ext_058_extreme_density_autocorr_lag5_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of daily -5% flag at lag 5 (weekly clustering persistence)."""
    flag5 = _extreme_flag(close, -0.05)
    lag5 = flag5.shift(_TD_WEEK)
    return flag5.rolling(_TD_QTR, min_periods=_TD_MON).corr(lag5)


def edd_ext_059_neg5pct_density_halflife_ewm(close: pd.Series) -> pd.Series:
    """EWM half-life proxy: EWM (halflife=21d) of -5% flag."""
    return _extreme_flag(close, -0.05).ewm(halflife=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def edd_ext_060_extreme_day_density_entropy_63d(close: pd.Series) -> pd.Series:
    """Shannon entropy of weekly extreme day counts in trailing 63 days (regularity measure)."""
    flag5 = _extreme_flag(close, -0.05)

    def _entropy(arr):
        weeks = [arr[i:i + _TD_WEEK].sum() for i in range(0, len(arr), _TD_WEEK) if len(arr[i:i + _TD_WEEK]) == _TD_WEEK]
        weeks = [float(w) for w in weeks]
        total = sum(weeks)
        if total <= 0:
            return 0.0
        probs = [w / total for w in weeks if w > 0]
        return float(-sum(p * np.log(p + _EPS) for p in probs))

    return flag5.rolling(_TD_QTR, min_periods=_TD_MON).apply(_entropy, raw=True)


# --- Group G (061-075): Second-order spacing and density features ---

def edd_ext_061_mean_spacing_neg5pct_21d(close: pd.Series) -> pd.Series:
    """Mean inter-arrival gap between -5% days in trailing 21 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_MON)


def edd_ext_062_mean_spacing_neg3pct_252d(close: pd.Series) -> pd.Series:
    """Mean inter-arrival gap between -3% days in trailing 252 days."""
    return _rolling_spacing_mean(_extreme_flag(close, -0.03), _TD_YEAR)


def edd_ext_063_extreme5pct_share_decline_21d(close: pd.Series) -> pd.Series:
    """Share of total negative return in 21d delivered by -5% days."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    extreme_sum = _rolling_sum(ret * flag5, _TD_MON)
    total_neg = _rolling_sum(ret.clip(upper=0.0), _TD_MON)
    return _safe_div(extreme_sum, total_neg.clip(upper=-_EPS))


def edd_ext_064_extreme_count_normalized_vol_21d(close: pd.Series) -> pd.Series:
    """21-day -5% count * annualized vol (sigma-adjusted count)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    ret = _daily_return(close)
    vol = _rolling_std(ret, _TD_QTR) * np.sqrt(_TD_YEAR)
    return cnt * vol.clip(lower=_EPS)


def edd_ext_065_extreme5pct_share_vs_all_neg_days_63d(close: pd.Series) -> pd.Series:
    """Fraction of all negative-return days in 63d that are -5% extreme days."""
    ret = _daily_return(close)
    neg_flag = (ret < 0).astype(float)
    flag5 = _extreme_flag(close, -0.05)
    return _safe_div(
        _rolling_sum(flag5, _TD_QTR),
        _rolling_sum(neg_flag, _TD_QTR).clip(lower=_EPS)
    )


def edd_ext_066_extreme_density_gini_252d(close: pd.Series) -> pd.Series:
    """Gini coefficient of weekly extreme day counts in 252 days (inequality of distribution)."""
    flag5 = _extreme_flag(close, -0.05)

    def _gini(arr):
        weeks = np.array([arr[i:i + _TD_WEEK].sum() for i in range(0, len(arr) - _TD_WEEK + 1, _TD_WEEK)], dtype=float)
        weeks = weeks[~np.isnan(weeks)]
        if len(weeks) < 2:
            return np.nan
        n = len(weeks)
        weeks_sorted = np.sort(weeks)
        cumsum = np.cumsum(weeks_sorted)
        total = cumsum[-1]
        if total < _EPS:
            return 0.0
        return float((2.0 * np.sum((np.arange(1, n + 1) * weeks_sorted)) / (n * total)) - (n + 1) / n)

    return flag5.rolling(_TD_YEAR, min_periods=_TD_HALF).apply(_gini, raw=True)


def edd_ext_067_mean_ret_on_extreme_days_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Mean log return on -5% days in trailing 63 days (average severity)."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    cnt = _rolling_sum(flag5, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(ret * flag5, _TD_QTR), cnt)


def edd_ext_068_std_ret_on_extreme_days_neg5pct_63d(close: pd.Series) -> pd.Series:
    """Std of returns on -5% days in trailing 63 days (severity dispersion)."""
    ret = _daily_return(close)
    flag5 = _extreme_flag(close, -0.05)
    mean_e = edd_ext_067_mean_ret_on_extreme_days_neg5pct_63d(close)
    dev_sq = ((ret - mean_e) ** 2) * flag5
    cnt = _rolling_sum(flag5, _TD_QTR).replace(0, np.nan)
    return np.sqrt(_safe_div(_rolling_sum(dev_sq, _TD_QTR), cnt))


def edd_ext_069_count_neg5pct_63d_above_ewm(close: pd.Series) -> pd.Series:
    """Count of 63-day -5% days when EWM-21 density is above its 252d mean (crowded extremes)."""
    flag5 = _extreme_flag(close, -0.05)
    ewm21 = _ewm_mean(flag5, _TD_MON)
    avg_ewm = _rolling_mean(ewm21, _TD_YEAR)
    high_density = (ewm21 > avg_ewm).astype(float)
    return _rolling_sum(flag5 * high_density, _TD_QTR)


def edd_ext_070_days_since_last_neg5pct_minus_mean_spacing_252d(close: pd.Series) -> pd.Series:
    """Days-since-last minus mean spacing (negative = recent extreme, positive = quiet period)."""
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05))
    mean_sp = _rolling_spacing_mean(_extreme_flag(close, -0.05), _TD_YEAR)
    return elapsed - mean_sp


def edd_ext_071_count_neg5pct_21d_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope over 5 days of the 21-day -5% count (very short-term density trend)."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_MON)
    return _linslope(cnt, _TD_WEEK)


def edd_ext_072_extreme_density_excess_score_63d(close: pd.Series) -> pd.Series:
    """Excess extreme density: (63d density - 252d density) * days_since_last_neg5pct_inverse."""
    d63 = _rolling_sum(_extreme_flag(close, -0.05), _TD_QTR) / _TD_QTR
    d252 = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR) / _TD_YEAR
    excess = (d63 - d252).clip(lower=0.0)
    elapsed = _time_since_last_extreme(_extreme_flag(close, -0.05)).clip(lower=1.0)
    recency = 1.0 / elapsed
    return excess * recency


def edd_ext_073_count_neg5pct_252d_pct_rank_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day -5% count — how extreme vs all history."""
    cnt = _rolling_sum(_extreme_flag(close, -0.05), _TD_YEAR)
    return cnt.expanding(min_periods=_TD_YEAR).rank(pct=True)


def edd_ext_074_vol_weighted_extreme_density_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted -5% density: sum(vol_on_extreme_days) / total_vol in 63d."""
    flag5 = _extreme_flag(close, -0.05)
    return _safe_div(
        _rolling_sum(volume * flag5, _TD_QTR),
        _rolling_sum(volume, _TD_QTR).clip(lower=_EPS)
    )


def edd_ext_075_extreme_day_density_composite_distress(close: pd.Series) -> pd.Series:
    """Composite distress: z-score(count_21d) + z-score(frac_252d) + z-score(spacing_21d_inverse).
    Higher = more extreme day clustering concurrent with capitulation."""
    flag5 = _extreme_flag(close, -0.05)
    cnt21 = _rolling_sum(flag5, _TD_MON)
    frac252 = _rolling_sum(flag5, _TD_YEAR) / _TD_YEAR
    sp21 = _rolling_spacing_mean(flag5, _TD_MON).fillna(_TD_MON)

    def _zscore(s):
        m = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    z_cnt = _zscore(cnt21)
    z_frac = _zscore(frac252)
    z_sp_inv = _zscore(1.0 / sp21.clip(lower=_EPS))
    return z_cnt.fillna(0.0) + z_frac.fillna(0.0) + z_sp_inv.fillna(0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

EXTREME_DAY_DENSITY_EXTENDED_REGISTRY_001_075 = {
    "edd_ext_001_count_2sigma_252d_std_21d": {"inputs": ["close"], "func": edd_ext_001_count_2sigma_252d_std_21d},
    "edd_ext_002_count_2sigma_252d_std_63d": {"inputs": ["close"], "func": edd_ext_002_count_2sigma_252d_std_63d},
    "edd_ext_003_count_3sigma_252d_std_252d": {"inputs": ["close"], "func": edd_ext_003_count_3sigma_252d_std_252d},
    "edd_ext_004_days_since_last_2sigma_252d_std": {"inputs": ["close"], "func": edd_ext_004_days_since_last_2sigma_252d_std},
    "edd_ext_005_frac_2sigma_252d_std_63d": {"inputs": ["close"], "func": edd_ext_005_frac_2sigma_252d_std_63d},
    "edd_ext_006_count_2sigma_half_std_63d": {"inputs": ["close"], "func": edd_ext_006_count_2sigma_half_std_63d},
    "edd_ext_007_sigma_adaptive_count_21d": {"inputs": ["close"], "func": edd_ext_007_sigma_adaptive_count_21d},
    "edd_ext_008_sigma_adaptive_count_63d": {"inputs": ["close"], "func": edd_ext_008_sigma_adaptive_count_63d},
    "edd_ext_009_tail_pctile5_extreme_count_63d": {"inputs": ["close"], "func": edd_ext_009_tail_pctile5_extreme_count_63d},
    "edd_ext_010_tail_pctile1_extreme_count_252d": {"inputs": ["close"], "func": edd_ext_010_tail_pctile1_extreme_count_252d},
    "edd_ext_011_tail_pctile10_extreme_count_63d": {"inputs": ["close"], "func": edd_ext_011_tail_pctile10_extreme_count_63d},
    "edd_ext_012_frac_tail_pctile5_63d": {"inputs": ["close"], "func": edd_ext_012_frac_tail_pctile5_63d},
    "edd_ext_013_days_since_last_pctile5": {"inputs": ["close"], "func": edd_ext_013_days_since_last_pctile5},
    "edd_ext_014_count_2sigma_adaptive_21d_21d": {"inputs": ["close"], "func": edd_ext_014_count_2sigma_adaptive_21d_21d},
    "edd_ext_015_tail_concentration_index_252d": {"inputs": ["close"], "func": edd_ext_015_tail_concentration_index_252d},
    "edd_ext_016_count_high_to_close_neg5pct_63d": {"inputs": ["close", "high"], "func": edd_ext_016_count_high_to_close_neg5pct_63d},
    "edd_ext_017_count_open_to_close_neg5pct_63d": {"inputs": ["close", "open"], "func": edd_ext_017_count_open_to_close_neg5pct_63d},
    "edd_ext_018_count_high_to_low_range_gt10pct_63d": {"inputs": ["close", "high", "low"], "func": edd_ext_018_count_high_to_low_range_gt10pct_63d},
    "edd_ext_019_count_gap_down_neg5pct_63d": {"inputs": ["close", "open"], "func": edd_ext_019_count_gap_down_neg5pct_63d},
    "edd_ext_020_count_gap_down_neg3pct_63d": {"inputs": ["close", "open"], "func": edd_ext_020_count_gap_down_neg3pct_63d},
    "edd_ext_021_days_since_last_gap_down_neg5pct": {"inputs": ["close", "open"], "func": edd_ext_021_days_since_last_gap_down_neg5pct},
    "edd_ext_022_count_close_at_low_extreme_63d": {"inputs": ["close", "low"], "func": edd_ext_022_count_close_at_low_extreme_63d},
    "edd_ext_023_extreme_intraday_range_sum_63d": {"inputs": ["close", "high", "low"], "func": edd_ext_023_extreme_intraday_range_sum_63d},
    "edd_ext_024_count_open_to_close_neg3pct_21d": {"inputs": ["close", "open"], "func": edd_ext_024_count_open_to_close_neg3pct_21d},
    "edd_ext_025_gap_down_share_of_decline_63d": {"inputs": ["close", "open"], "func": edd_ext_025_gap_down_share_of_decline_63d},
    "edd_ext_026_spacing_skew_neg5pct_252d": {"inputs": ["close"], "func": edd_ext_026_spacing_skew_neg5pct_252d},
    "edd_ext_027_spacing_kurtosis_neg5pct_252d": {"inputs": ["close"], "func": edd_ext_027_spacing_kurtosis_neg5pct_252d},
    "edd_ext_028_spacing_median_neg5pct_252d": {"inputs": ["close"], "func": edd_ext_028_spacing_median_neg5pct_252d},
    "edd_ext_029_spacing_p75_neg5pct_252d": {"inputs": ["close"], "func": edd_ext_029_spacing_p75_neg5pct_252d},
    "edd_ext_030_spacing_p25_neg5pct_252d": {"inputs": ["close"], "func": edd_ext_030_spacing_p25_neg5pct_252d},
    "edd_ext_031_iqr_spacing_neg5pct_252d": {"inputs": ["close"], "func": edd_ext_031_iqr_spacing_neg5pct_252d},
    "edd_ext_032_mean_spacing_neg5pct_63d_norm_21d": {"inputs": ["close"], "func": edd_ext_032_mean_spacing_neg5pct_63d_norm_21d},
    "edd_ext_033_count_extreme_before_new_low_21d": {"inputs": ["close"], "func": edd_ext_033_count_extreme_before_new_low_21d},
    "edd_ext_034_spacing_ratio_mean_to_window_252d": {"inputs": ["close"], "func": edd_ext_034_spacing_ratio_mean_to_window_252d},
    "edd_ext_035_count_neg5pct_within_2d_of_neg3pct_63d": {"inputs": ["close"], "func": edd_ext_035_count_neg5pct_within_2d_of_neg3pct_63d},
    "edd_ext_036_extreme_density_in_bear_regime_63d": {"inputs": ["close"], "func": edd_ext_036_extreme_density_in_bear_regime_63d},
    "edd_ext_037_extreme_density_in_bull_regime_63d": {"inputs": ["close"], "func": edd_ext_037_extreme_density_in_bull_regime_63d},
    "edd_ext_038_bear_regime_extreme_density_ratio": {"inputs": ["close"], "func": edd_ext_038_bear_regime_extreme_density_ratio},
    "edd_ext_039_high_vol_regime_extreme_count_63d": {"inputs": ["close"], "func": edd_ext_039_high_vol_regime_extreme_count_63d},
    "edd_ext_040_extreme_density_after_gap_down_21d": {"inputs": ["close", "open"], "func": edd_ext_040_extreme_density_after_gap_down_21d},
    "edd_ext_041_count_neg5pct_accelerating_period": {"inputs": ["close"], "func": edd_ext_041_count_neg5pct_accelerating_period},
    "edd_ext_042_extreme_density_consecutive_months_63d": {"inputs": ["close"], "func": edd_ext_042_extreme_density_consecutive_months_63d},
    "edd_ext_043_frac_neg5pct_21d_in_bottom_decile_252d": {"inputs": ["close"], "func": edd_ext_043_frac_neg5pct_21d_in_bottom_decile_252d},
    "edd_ext_044_count_neg5pct_21d_pct_rank_252d": {"inputs": ["close"], "func": edd_ext_044_count_neg5pct_21d_pct_rank_252d},
    "edd_ext_045_extreme_day_gap_halved_flag": {"inputs": ["close"], "func": edd_ext_045_extreme_day_gap_halved_flag},
    "edd_ext_046_depth_weighted_count_neg5pct_21d": {"inputs": ["close"], "func": edd_ext_046_depth_weighted_count_neg5pct_21d},
    "edd_ext_047_depth_weighted_count_neg5pct_63d": {"inputs": ["close"], "func": edd_ext_047_depth_weighted_count_neg5pct_63d},
    "edd_ext_048_sigma_weighted_extreme_count_63d": {"inputs": ["close"], "func": edd_ext_048_sigma_weighted_extreme_count_63d},
    "edd_ext_049_extreme_count_vol_adjusted_63d": {"inputs": ["close"], "func": edd_ext_049_extreme_count_vol_adjusted_63d},
    "edd_ext_050_extreme_damage_concentration_21d": {"inputs": ["close"], "func": edd_ext_050_extreme_damage_concentration_21d},
    "edd_ext_051_count_neg5pct_21d_lag21": {"inputs": ["close"], "func": edd_ext_051_count_neg5pct_21d_lag21},
    "edd_ext_052_count_neg5pct_21d_lag63": {"inputs": ["close"], "func": edd_ext_052_count_neg5pct_21d_lag63},
    "edd_ext_053_count_neg5pct_change_21d_vs_lag21": {"inputs": ["close"], "func": edd_ext_053_count_neg5pct_change_21d_vs_lag21},
    "edd_ext_054_count_neg5pct_change_63d_vs_lag63": {"inputs": ["close"], "func": edd_ext_054_count_neg5pct_change_63d_vs_lag63},
    "edd_ext_055_frac_neg5pct_21d_rolling_max_63d": {"inputs": ["close"], "func": edd_ext_055_frac_neg5pct_21d_rolling_max_63d},
    "edd_ext_056_frac_neg5pct_21d_current_vs_peak_252d": {"inputs": ["close"], "func": edd_ext_056_frac_neg5pct_21d_current_vs_peak_252d},
    "edd_ext_057_count_neg5pct_streak_of_active_months_63d": {"inputs": ["close"], "func": edd_ext_057_count_neg5pct_streak_of_active_months_63d},
    "edd_ext_058_extreme_density_autocorr_lag5_63d": {"inputs": ["close"], "func": edd_ext_058_extreme_density_autocorr_lag5_63d},
    "edd_ext_059_neg5pct_density_halflife_ewm": {"inputs": ["close"], "func": edd_ext_059_neg5pct_density_halflife_ewm},
    "edd_ext_060_extreme_day_density_entropy_63d": {"inputs": ["close"], "func": edd_ext_060_extreme_day_density_entropy_63d},
    "edd_ext_061_mean_spacing_neg5pct_21d": {"inputs": ["close"], "func": edd_ext_061_mean_spacing_neg5pct_21d},
    "edd_ext_062_mean_spacing_neg3pct_252d": {"inputs": ["close"], "func": edd_ext_062_mean_spacing_neg3pct_252d},
    "edd_ext_063_extreme5pct_share_decline_21d": {"inputs": ["close"], "func": edd_ext_063_extreme5pct_share_decline_21d},
    "edd_ext_064_extreme_count_normalized_vol_21d": {"inputs": ["close"], "func": edd_ext_064_extreme_count_normalized_vol_21d},
    "edd_ext_065_extreme5pct_share_vs_all_neg_days_63d": {"inputs": ["close"], "func": edd_ext_065_extreme5pct_share_vs_all_neg_days_63d},
    "edd_ext_066_extreme_density_gini_252d": {"inputs": ["close"], "func": edd_ext_066_extreme_density_gini_252d},
    "edd_ext_067_mean_ret_on_extreme_days_neg5pct_63d": {"inputs": ["close"], "func": edd_ext_067_mean_ret_on_extreme_days_neg5pct_63d},
    "edd_ext_068_std_ret_on_extreme_days_neg5pct_63d": {"inputs": ["close"], "func": edd_ext_068_std_ret_on_extreme_days_neg5pct_63d},
    "edd_ext_069_count_neg5pct_63d_above_ewm": {"inputs": ["close"], "func": edd_ext_069_count_neg5pct_63d_above_ewm},
    "edd_ext_070_days_since_last_neg5pct_minus_mean_spacing_252d": {"inputs": ["close"], "func": edd_ext_070_days_since_last_neg5pct_minus_mean_spacing_252d},
    "edd_ext_071_count_neg5pct_21d_slope_5d": {"inputs": ["close"], "func": edd_ext_071_count_neg5pct_21d_slope_5d},
    "edd_ext_072_extreme_density_excess_score_63d": {"inputs": ["close"], "func": edd_ext_072_extreme_density_excess_score_63d},
    "edd_ext_073_count_neg5pct_252d_pct_rank_expanding": {"inputs": ["close"], "func": edd_ext_073_count_neg5pct_252d_pct_rank_expanding},
    "edd_ext_074_vol_weighted_extreme_density_63d": {"inputs": ["close", "volume"], "func": edd_ext_074_vol_weighted_extreme_density_63d},
    "edd_ext_075_extreme_day_density_composite_distress": {"inputs": ["close"], "func": edd_ext_075_extreme_day_density_composite_distress},
}
