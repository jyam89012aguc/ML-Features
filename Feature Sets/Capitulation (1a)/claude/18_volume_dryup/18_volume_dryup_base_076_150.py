"""
18_volume_dryup — Base Features 076-200
Domain: volume collapse / exhaustion of selling — volume dry-up below trailing baseline
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Volume dry-up vs. price context ---

def vdry_076_vol_dryup_intensity_252d(volume: pd.Series) -> pd.Series:
    """Sum of (1 - vol/mean252) for days below 252-day mean, over 252 days."""
    m252 = _rolling_mean(volume, _TD_YEAR)
    shortfall = (1.0 - _safe_div(volume, m252)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_YEAR)


def vdry_077_low_vol_on_new_low_close_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 21d-low closes accompanied by below-21d-mean volume, trailing 21 days."""
    prev_min = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    new_low = close < prev_min
    low_vol = volume < _rolling_mean(volume, _TD_MON)
    cond = new_low & low_vol
    return _rolling_count_true(cond, _TD_MON)


def vdry_078_low_vol_on_new_low_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63d-low closes accompanied by below-63d-mean volume, trailing 63 days."""
    prev_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < prev_min
    low_vol = volume < _rolling_mean(volume, _TD_QTR)
    cond = new_low & low_vol
    return _rolling_count_true(cond, _TD_QTR)


def vdry_079_vol_ratio_at_price_low_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on days close <= 5th-pctile of 63d close, divided by overall avg vol."""
    p05 = close.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    at_low = close <= p05
    low_vol = volume.where(at_low, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    avg_vol = _rolling_mean(volume, _TD_QTR)
    return _safe_div(low_vol, avg_vol)


def vdry_080_vol_breadth_dryup_score_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days both below 63d-mean AND below prior-day volume."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (volume < mean63) & (volume < volume.shift(1))
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vdry_081_vol_breadth_dryup_score_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days both below 252d-mean AND below prior-day volume."""
    mean252 = _rolling_mean(volume, _TD_YEAR)
    cond = (volume < mean252) & (volume < volume.shift(1))
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vdry_082_vol_21d_mean_vs_252d_mean_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day mean volume to 252-day mean volume (collapse measure)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def vdry_083_vol_63d_mean_vs_252d_mean_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day mean volume to 252-day mean volume."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))


def vdry_084_vol_5d_mean_vs_63d_mean_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day mean volume to 63-day mean volume."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))


def vdry_085_vol_dryup_composite_score(volume: pd.Series) -> pd.Series:
    """Average of three vol-ratio features: 5d/21d, 21d/63d, 63d/252d means."""
    r1 = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))
    r2 = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))
    r3 = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))
    return (r1 + r2 + r3) / 3.0


# --- Group I (086-095): Volume z-score extremes and rank measures ---

def vdry_086_vol_zscore_252d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of the 252-day volume z-score (all-history extremity)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    z = _safe_div(volume - m, s)
    return z.expanding(min_periods=5).rank(pct=True)


def vdry_087_vol_pct_rank_21d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 21-day distribution."""
    return volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def vdry_088_vol_pct_rank_126d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 126-day distribution."""
    return volume.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def vdry_089_vol_below_p10_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is below the 10th percentile of the past 252 days."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return (volume < p10).astype(float)


def vdry_090_vol_below_p25_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is below the 25th percentile of the past 252 days."""
    p25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return (volume < p25).astype(float)


def vdry_091_count_below_p25_252d_in_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21 days where volume < 25th percentile of 252-day dist."""
    p25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    cond = volume < p25
    return _rolling_count_true(cond, _TD_MON)


def vdry_092_count_below_p25_252d_in_63d(volume: pd.Series) -> pd.Series:
    """Count of days in last 63 days where volume < 25th percentile of 252-day dist."""
    p25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    cond = volume < p25
    return _rolling_count_true(cond, _TD_QTR)


def vdry_093_vol_zscore_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day volume z-score within trailing 252-day distribution."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_094_vol_21d_std_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day volume std within trailing 252-day distribution."""
    s21 = _rolling_std(volume, _TD_MON)
    return s21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_095_vol_log_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of log-volume relative to 63-day log-volume mean and std."""
    lv = _log_safe(volume)
    m = _rolling_mean(lv, _TD_QTR)
    s = _rolling_std(lv, _TD_QTR)
    return _safe_div(lv - m, s)


# --- Group J (096-105): Volume relative to price-range (dollar volume dryup) ---

def vdry_096_dollar_vol_ratio_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's dollar volume (close*vol) / 21-day mean dollar volume."""
    dv = close * volume
    return _safe_div(dv, _rolling_mean(dv, _TD_MON))


def vdry_097_dollar_vol_ratio_63d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's dollar volume / 63-day mean dollar volume."""
    dv = close * volume
    return _safe_div(dv, _rolling_mean(dv, _TD_QTR))


def vdry_098_dollar_vol_ratio_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's dollar volume / 252-day mean dollar volume."""
    dv = close * volume
    return _safe_div(dv, _rolling_mean(dv, _TD_YEAR))


def vdry_099_dollar_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume relative to 63-day mean and std."""
    dv = close * volume
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    return _safe_div(dv - m, s)


def vdry_100_dollar_vol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of dollar volume within trailing 252-day distribution."""
    dv = close * volume
    return dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_101_range_vol_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's (high-low)*volume / 21-day mean of same (intraday activity dryup)."""
    rv = (high - low) * volume
    return _safe_div(rv, _rolling_mean(rv, _TD_MON))


def vdry_102_range_vol_ratio_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's (high-low)*volume / 63-day mean."""
    rv = (high - low) * volume
    return _safe_div(rv, _rolling_mean(rv, _TD_QTR))


def vdry_103_range_vol_zscore_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (high-low)*volume relative to 63-day mean and std."""
    rv = (high - low) * volume
    m = _rolling_mean(rv, _TD_QTR)
    s = _rolling_std(rv, _TD_QTR)
    return _safe_div(rv - m, s)


def vdry_104_dollar_vol_below_p10_252d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: dollar volume < 10th percentile of 252-day dollar volume distribution."""
    dv = close * volume
    p10 = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return (dv < p10).astype(float)


def vdry_105_vol_per_price_range_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume / (high - low) relative to 21-day mean (thin range = exhaustion)."""
    rng = (high - low).replace(0, np.nan)
    vprange = _safe_div(volume, rng)
    return _safe_div(vprange, _rolling_mean(vprange, _TD_MON))


# --- Group K (106-115): Volume vs. prior spike, post-spike dryup windows ---

def vdry_106_days_since_vol_21d_max(volume: pd.Series) -> pd.Series:
    """Days elapsed since volume last equaled its 21-day rolling maximum."""
    max21 = _rolling_max(volume, _TD_MON)
    at_max = (volume >= max21).astype(float)
    def _days_since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 1.0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return at_max.rolling(_TD_MON, min_periods=1).apply(_days_since, raw=True)


def vdry_107_days_since_vol_63d_max(volume: pd.Series) -> pd.Series:
    """Days elapsed since volume last equaled its 63-day rolling maximum."""
    max63 = _rolling_max(volume, _TD_QTR)
    at_max = (volume >= max63).astype(float)
    def _days_since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 1.0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return at_max.rolling(_TD_QTR, min_periods=1).apply(_days_since, raw=True)


def vdry_108_vol_after_spike_decay_5d(volume: pd.Series) -> pd.Series:
    """5-day mean volume / the local spike (1-day lag maximum of prior 5 days)."""
    spike = _rolling_max(volume.shift(1), _TD_WEEK)
    m5 = _rolling_mean(volume, _TD_WEEK)
    return _safe_div(m5, spike)


def vdry_109_vol_after_spike_decay_21d(volume: pd.Series) -> pd.Series:
    """21-day mean volume / local spike (max of prior 21 days)."""
    spike = _rolling_max(volume.shift(1), _TD_MON)
    m21 = _rolling_mean(volume, _TD_MON)
    return _safe_div(m21, spike)


def vdry_110_vol_21d_pct_change(volume: pd.Series) -> pd.Series:
    """Percent change in volume over 21 trading days."""
    return _safe_div(volume - volume.shift(_TD_MON), volume.shift(_TD_MON).abs().replace(0, np.nan))


def vdry_111_vol_63d_pct_change(volume: pd.Series) -> pd.Series:
    """Percent change in volume over 63 trading days."""
    return _safe_div(volume - volume.shift(_TD_QTR), volume.shift(_TD_QTR).abs().replace(0, np.nan))


def vdry_112_vol_126d_pct_change(volume: pd.Series) -> pd.Series:
    """Percent change in volume over 126 trading days."""
    return _safe_div(volume - volume.shift(_TD_HALF), volume.shift(_TD_HALF).abs().replace(0, np.nan))


def vdry_113_vol_252d_pct_change(volume: pd.Series) -> pd.Series:
    """Percent change in volume over 252 trading days."""
    return _safe_div(volume - volume.shift(_TD_YEAR), volume.shift(_TD_YEAR).abs().replace(0, np.nan))


def vdry_114_vol_21d_mean_pct_change_21d(volume: pd.Series) -> pd.Series:
    """Percent change in the 21-day mean volume over 21 days."""
    m21 = _rolling_mean(volume, _TD_MON)
    return _safe_div(m21 - m21.shift(_TD_MON), m21.shift(_TD_MON).abs().replace(0, np.nan))


def vdry_115_vol_63d_mean_pct_change_63d(volume: pd.Series) -> pd.Series:
    """Percent change in 63-day mean volume over 63 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    return _safe_div(m63 - m63.shift(_TD_QTR), m63.shift(_TD_QTR).abs().replace(0, np.nan))


# --- Group L (116-125): Volume dryup with low-price context ---

def vdry_116_low_vol_low_close_combined_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of (1 - vol/mean21) and (1 - close/max21close), trailing 21d sum."""
    m_vol = _rolling_mean(volume, _TD_MON)
    m_close = _rolling_max(close, _TD_MON)
    v_ratio = (1.0 - _safe_div(volume, m_vol)).clip(lower=0.0)
    c_ratio = (1.0 - _safe_div(close, m_close)).clip(lower=0.0)
    return _rolling_sum(v_ratio * c_ratio, _TD_MON)


def vdry_117_low_vol_near_52wk_low_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume < 21d mean AND close within 5% of 252-day low (capitulation zone)."""
    min252 = _rolling_min(close, _TD_YEAR)
    near_low = close <= 1.05 * min252
    low_vol = volume < _rolling_mean(volume, _TD_MON)
    return (near_low & low_vol).astype(float)


def vdry_118_vol_below_mean_on_price_decline_frac(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days over last 63d that also had below-63d-mean volume."""
    ret = close.pct_change(1)
    mean63 = _rolling_mean(volume, _TD_QTR)
    down_days = (ret < 0).astype(float)
    low_vol_down = ((ret < 0) & (volume < mean63)).astype(float)
    dn_count = _rolling_sum(down_days, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(low_vol_down, _TD_QTR), dn_count)


def vdry_119_vol_below_mean_on_price_decline_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-price days over last 21d with below-21d-mean volume."""
    ret = close.pct_change(1)
    mean21 = _rolling_mean(volume, _TD_MON)
    down_days = (ret < 0).astype(float)
    low_vol_down = ((ret < 0) & (volume < mean21)).astype(float)
    dn_count = _rolling_sum(down_days, _TD_MON).replace(0, np.nan)
    return _safe_div(_rolling_sum(low_vol_down, _TD_MON), dn_count)


def vdry_120_vol_dryup_streak_norm_21d(volume: pd.Series) -> pd.Series:
    """Current below-21d-mean streak normalized by 252-day avg below-mean streak."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def vdry_121_vol_dryup_streak_norm_63d(volume: pd.Series) -> pd.Series:
    """Current below-63d-mean streak normalized by 252-day avg below-mean streak."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    streak = _consec_streak(cond)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def vdry_122_consec_below_mean_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of current below-21d-mean streak within 252-day streak dist."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_123_vol_dryup_expanding_max_streak(volume: pd.Series) -> pd.Series:
    """Expanding all-time maximum of the below-21d-mean consecutive streak."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    return streak.expanding(min_periods=1).max()


def vdry_124_vol_dryup_freq_252d(volume: pd.Series) -> pd.Series:
    """Count of streak starts (transitions into below-21d-mean) over trailing 252 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    cond_int = cond.astype(int)
    prev_int = cond_int.shift(1).fillna(0).astype(int)
    is_start = ((cond_int == 1) & (prev_int == 0)).astype(float)
    return _rolling_sum(is_start, _TD_YEAR)


def vdry_125_avg_dryup_streak_len_252d(volume: pd.Series) -> pd.Series:
    """Average length of below-21d-mean streaks over trailing 252 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    cond_int = cond.astype(int)
    prev_int = cond_int.shift(1).fillna(0).astype(int)
    is_start = ((cond_int == 1) & (prev_int == 0)).astype(float)
    total_down = _rolling_sum(cond_int.astype(float), _TD_YEAR)
    num_starts = _rolling_sum(is_start, _TD_YEAR)
    return _safe_div(total_down, num_starts.clip(lower=1))


# --- Group M (126-135): Normalized volume ranges and breadth ---

def vdry_126_vol_iqr_contraction_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day vol IQR to 252-day vol IQR (narrowing distribution)."""
    q75_21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25_21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    q75_252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25_252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    iqr21 = q75_21 - q25_21
    iqr252 = q75_252 - q25_252
    return _safe_div(iqr21, iqr252)


def vdry_127_vol_cv_21d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of volume over 21 days."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))


def vdry_128_vol_cv_63d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 63 days."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def vdry_129_vol_cv_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day CV to 252-day CV of volume (collapsed variability)."""
    cv21 = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    cv252 = _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    return _safe_div(cv21, cv252)


def vdry_130_vol_log_ratio_21d_mean(volume: pd.Series) -> pd.Series:
    """Log(volume / 21d mean); deeply negative = severe dryup."""
    return _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_MON))


def vdry_131_vol_log_ratio_252d_mean(volume: pd.Series) -> pd.Series:
    """Log(volume / 252d mean)."""
    return _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_YEAR))


def vdry_132_vol_log_ratio_63d_ema(volume: pd.Series) -> pd.Series:
    """Log(volume / 63d EMA)."""
    return _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_QTR))


def vdry_133_vol_21d_min_vs_252d_min_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day minimum volume to 252-day minimum volume."""
    return _safe_div(_rolling_min(volume, _TD_MON), _rolling_min(volume, _TD_YEAR))


def vdry_134_vol_21d_min_vs_252d_mean_ratio(volume: pd.Series) -> pd.Series:
    """21-day minimum volume divided by 252-day mean volume."""
    return _safe_div(_rolling_min(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def vdry_135_vol_5d_min_vs_63d_mean_ratio(volume: pd.Series) -> pd.Series:
    """5-day minimum volume divided by 63-day mean volume (acute low)."""
    return _safe_div(_rolling_min(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))


# --- Group N (136-145): Volume dry-up with intraday range context ---

def vdry_136_vol_times_range_below_mean_21d_flag(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: (high-low)*vol below its 21-day mean (combined range-vol dryup)."""
    rv = (high - low) * volume
    return (rv < _rolling_mean(rv, _TD_MON)).astype(float)


def vdry_137_vol_times_range_zscore_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (high-low)*volume over 21-day window."""
    rv = (high - low) * volume
    m = _rolling_mean(rv, _TD_MON)
    s = _rolling_std(rv, _TD_MON)
    return _safe_div(rv - m, s)


def vdry_138_vol_times_range_pct_rank_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of (high-low)*volume in trailing 252-day distribution."""
    rv = (high - low) * volume
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_139_low_range_low_vol_consec_streak(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of days where both (high-low) < 21d-mean range AND vol < 21d-mean vol."""
    rng = high - low
    cond = (rng < _rolling_mean(rng, _TD_MON)) & (volume < _rolling_mean(volume, _TD_MON))
    return _consec_streak(cond)


def vdry_140_vol_below_mean_low_close_21d_count(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in last 21d where vol < 21d mean AND close in bottom 25% of daily range."""
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    cond = (volume < _rolling_mean(volume, _TD_MON)) & (pos <= 0.25)
    return _rolling_count_true(cond, _TD_MON)


def vdry_141_narrow_range_vol_dryup_score_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 63d of (1 - rv / mean63_rv) clipped to 0 (shortfall intensity)."""
    rv = (high - low) * volume
    m63 = _rolling_mean(rv, _TD_QTR)
    shortfall = (1.0 - _safe_div(rv, m63)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_QTR)


def vdry_142_open_close_range_vol_zscore_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of abs(close-open)*volume over 21-day window."""
    body_vol = (close - open).abs() * volume
    m = _rolling_mean(body_vol, _TD_MON)
    s = _rolling_std(body_vol, _TD_MON)
    return _safe_div(body_vol - m, s)


def vdry_143_vol_to_intraday_range_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean of volume / (high - low); high ratio suggests thin-range, high-vol."""
    rng = (high - low).replace(0, np.nan)
    vr = _safe_div(volume, rng)
    return _rolling_mean(vr, _TD_MON)


def vdry_144_vol_21d_below_median_and_range_below_median(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where both vol and range are below their 21d medians."""
    cond = (volume < _rolling_median(volume, _TD_MON)) & ((high - low) < _rolling_median(high - low, _TD_MON))
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vdry_145_dollar_vol_dryup_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (1 - dv/mean63_dv) clipped to 0 over 63 days for dollar volume."""
    dv = close * volume
    m63 = _rolling_mean(dv, _TD_QTR)
    shortfall = (1.0 - _safe_div(dv, m63)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_QTR)


# --- Group O (146-150): Composite dryup and exhaustion indices ---

def vdry_146_vol_dryup_composite_zscore(volume: pd.Series) -> pd.Series:
    """Avg of z-scores at 21d, 63d, 252d windows (broad-based dryup)."""
    z21 = _safe_div(volume - _rolling_mean(volume, _TD_MON), _rolling_std(volume, _TD_MON))
    z63 = _safe_div(volume - _rolling_mean(volume, _TD_QTR), _rolling_std(volume, _TD_QTR))
    z252 = _safe_div(volume - _rolling_mean(volume, _TD_YEAR), _rolling_std(volume, _TD_YEAR))
    return (z21 + z63 + z252) / 3.0


def vdry_147_seller_exhaustion_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Low-vol down-days count * avg below-mean vol depth, 21d (exhaustion proxy)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    ret = close.pct_change(1)
    low_vol_down = ((ret < 0) & (volume < mean21)).astype(float)
    depth = (1.0 - _safe_div(volume, mean21)).clip(lower=0.0)
    score = low_vol_down * depth
    return _rolling_sum(score, _TD_MON)


def vdry_148_vol_dryup_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's vol within trailing 504-day distribution."""
    return volume.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def vdry_149_vol_dryup_21d_streak_zscore(volume: pd.Series) -> pd.Series:
    """Z-score of current below-21d-mean streak relative to 252-day streak distribution."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    streak = _consec_streak(cond)
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - m, s)


def vdry_150_vol_dryup_distress_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined: below-mean vol streak * vol shortfall depth * down-price fraction."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = volume < mean63
    streak = _consec_streak(cond)
    depth = (1.0 - _safe_div(volume, mean63)).clip(lower=0.0)
    ret = close.pct_change(1)
    dn_frac = _rolling_count_true(ret < 0, _TD_MON) / _TD_MON
    return streak * depth * dn_frac


# --- Group P2 (176-185): Volume dry-up measured on open-to-close body ---

def vdry_176_body_vol_ratio_21d_mean(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """abs(close-open)*volume / 21d mean of same (body-volume dryup)."""
    bv = (close - open).abs() * volume
    return _safe_div(bv, _rolling_mean(bv, _TD_MON))


def vdry_177_body_vol_ratio_63d_mean(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """abs(close-open)*volume / 63d mean of same."""
    bv = (close - open).abs() * volume
    return _safe_div(bv, _rolling_mean(bv, _TD_QTR))


def vdry_178_body_vol_pct_rank_252d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of abs(close-open)*volume in trailing 252-day distribution."""
    bv = (close - open).abs() * volume
    return bv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_179_body_vol_zscore_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of abs(close-open)*volume relative to 63-day mean and std."""
    bv = (close - open).abs() * volume
    m = _rolling_mean(bv, _TD_QTR)
    s = _rolling_std(bv, _TD_QTR)
    return _safe_div(bv - m, s)


def vdry_180_shadow_vol_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """(wick range)/(total range) weighted by volume vs. 21d mean; wicks = (H-max(O,C))+(min(O,C)-L)."""
    body_hi = pd.concat([close, open], axis=1).max(axis=1)
    body_lo = pd.concat([close, open], axis=1).min(axis=1)
    wick = (high - body_hi) + (body_lo - low)
    rng = (high - low).replace(0, np.nan)
    wick_frac = _safe_div(wick, rng)
    wv = wick_frac * volume
    return _safe_div(wv, _rolling_mean(wv, _TD_MON))


def vdry_181_vol_on_gap_down_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 21 days where open < prior close AND volume < 63d mean."""
    gap_down = open < close.shift(1)
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = gap_down & (volume < mean63)
    return _rolling_count_true(cond, _TD_MON)


def vdry_182_vol_open_close_shortfall_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 21d of (1 - body_vol/mean21_body_vol) clipped to 0 (body dryup depth)."""
    bv = (close - open).abs() * volume
    m21 = _rolling_mean(bv, _TD_MON)
    shortfall = (1.0 - _safe_div(bv, m21)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_MON)


def vdry_183_vol_ratio_at_open_below_prior_close(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on days open < prior close / overall 21d avg vol."""
    gap_down = open < close.shift(1)
    vol_gap = volume.where(gap_down, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(vol_gap, _rolling_mean(volume, _TD_MON))


def vdry_184_consec_low_body_vol_days(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days where abs(close-open)*volume < 21d mean of that product."""
    bv = (close - open).abs() * volume
    cond = bv < _rolling_mean(bv, _TD_MON)
    return _consec_streak(cond)


def vdry_185_down_body_low_vol_frac_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with bearish close-open body AND volume < 21d mean."""
    bear_body = close < open
    low_vol = volume < _rolling_mean(volume, _TD_MON)
    cond = bear_body & low_vol
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


# --- Group Q2 (186-195): Volume decay measured vs. trailing max over varied windows ---

def vdry_186_vol_decay_from_5d_max(volume: pd.Series) -> pd.Series:
    """Volume divided by its 5-day trailing maximum (very short post-spike decay)."""
    return _safe_div(volume, _rolling_max(volume.shift(1), _TD_WEEK))


def vdry_187_vol_decay_from_126d_max(volume: pd.Series) -> pd.Series:
    """Volume divided by its 126-day trailing maximum."""
    return _safe_div(volume, _rolling_max(volume.shift(1), _TD_HALF))


def vdry_188_log_vol_decay_from_21d_max(volume: pd.Series) -> pd.Series:
    """Log(volume / 21d-trailing-max); negative = below recent peak."""
    return _log_safe(volume) - _log_safe(_rolling_max(volume.shift(1), _TD_MON))


def vdry_189_log_vol_decay_from_252d_max(volume: pd.Series) -> pd.Series:
    """Log(volume / 252d-trailing-max); deeply negative = long-term post-spike collapse."""
    return _log_safe(volume) - _log_safe(_rolling_max(volume.shift(1), _TD_YEAR))


def vdry_190_vol_5d_max_to_5d_min_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day maximum to 5-day minimum volume (intra-week spread)."""
    return _safe_div(_rolling_max(volume, _TD_WEEK), _rolling_min(volume, _TD_WEEK))


def vdry_191_vol_21d_max_to_252d_mean_ratio(volume: pd.Series) -> pd.Series:
    """21-day max volume divided by 252-day mean (how large the recent spike vs. long baseline)."""
    return _safe_div(_rolling_max(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def vdry_192_vol_contraction_5d_vs_21d_max(volume: pd.Series) -> pd.Series:
    """5-day mean volume divided by 21-day max volume (short recent shrinkage)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume.shift(1), _TD_MON))


def vdry_193_vol_decay_from_252d_max_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of (vol / 252d-max) within trailing 252-day distribution."""
    ratio = _safe_div(volume, _rolling_max(volume.shift(1), _TD_YEAR))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_194_vol_21d_min_vs_63d_mean_ratio(volume: pd.Series) -> pd.Series:
    """21-day minimum volume divided by 63-day mean volume."""
    return _safe_div(_rolling_min(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))


def vdry_195_vol_5d_min_vs_252d_mean_ratio(volume: pd.Series) -> pd.Series:
    """5-day minimum volume divided by 252-day mean volume (extreme recent low)."""
    return _safe_div(_rolling_min(volume, _TD_WEEK), _rolling_mean(volume, _TD_YEAR))


# --- Group R2 (196-200): Dollar-volume and range exhaustion composites ---

def vdry_196_dollar_vol_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume relative to 21-day mean and std."""
    dv = close * volume
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    return _safe_div(dv - m, s)


def vdry_197_dollar_vol_log_ratio_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log(dollar_vol / 21d-mean-dollar-vol); negative = dryup in trading dollars."""
    dv = close * volume
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_MON))


def vdry_198_range_dollar_vol_composite_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of z-score of dollar-vol and z-score of range-vol over 63 days."""
    dv = close * volume
    rv = (high - low) * volume
    z_dv = _safe_div(dv - _rolling_mean(dv, _TD_QTR), _rolling_std(dv, _TD_QTR))
    z_rv = _safe_div(rv - _rolling_mean(rv, _TD_QTR), _rolling_std(rv, _TD_QTR))
    return (z_dv + z_rv) / 2.0


def vdry_199_vol_dryup_all_windows_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume simultaneously below 5d, 21d, 63d, and 252d means (total dryup)."""
    f1 = volume < _rolling_mean(volume, _TD_WEEK)
    f2 = volume < _rolling_mean(volume, _TD_MON)
    f3 = volume < _rolling_mean(volume, _TD_QTR)
    f4 = volume < _rolling_mean(volume, _TD_YEAR)
    return (f1 & f2 & f3 & f4).astype(float)


def vdry_200_vol_dryup_weighted_shortfall_252d(volume: pd.Series) -> pd.Series:
    """Exponentially weighted sum of daily vol shortfalls below 63d-mean over 252 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    return shortfall.ewm(span=_TD_YEAR, min_periods=_TD_QTR).mean()


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DRYUP_REGISTRY_076_150 = {
    "vdry_076_vol_dryup_intensity_252d": {"inputs": ["volume"], "func": vdry_076_vol_dryup_intensity_252d},
    "vdry_077_low_vol_on_new_low_close_21d": {"inputs": ["close", "volume"], "func": vdry_077_low_vol_on_new_low_close_21d},
    "vdry_078_low_vol_on_new_low_close_63d": {"inputs": ["close", "volume"], "func": vdry_078_low_vol_on_new_low_close_63d},
    "vdry_079_vol_ratio_at_price_low_63d": {"inputs": ["close", "volume"], "func": vdry_079_vol_ratio_at_price_low_63d},
    "vdry_080_vol_breadth_dryup_score_21d": {"inputs": ["volume"], "func": vdry_080_vol_breadth_dryup_score_21d},
    "vdry_081_vol_breadth_dryup_score_63d": {"inputs": ["volume"], "func": vdry_081_vol_breadth_dryup_score_63d},
    "vdry_082_vol_21d_mean_vs_252d_mean_ratio": {"inputs": ["volume"], "func": vdry_082_vol_21d_mean_vs_252d_mean_ratio},
    "vdry_083_vol_63d_mean_vs_252d_mean_ratio": {"inputs": ["volume"], "func": vdry_083_vol_63d_mean_vs_252d_mean_ratio},
    "vdry_084_vol_5d_mean_vs_63d_mean_ratio": {"inputs": ["volume"], "func": vdry_084_vol_5d_mean_vs_63d_mean_ratio},
    "vdry_085_vol_dryup_composite_score": {"inputs": ["volume"], "func": vdry_085_vol_dryup_composite_score},
    "vdry_086_vol_zscore_252d_expanding_rank": {"inputs": ["volume"], "func": vdry_086_vol_zscore_252d_expanding_rank},
    "vdry_087_vol_pct_rank_21d": {"inputs": ["volume"], "func": vdry_087_vol_pct_rank_21d},
    "vdry_088_vol_pct_rank_126d": {"inputs": ["volume"], "func": vdry_088_vol_pct_rank_126d},
    "vdry_089_vol_below_p10_252d_flag": {"inputs": ["volume"], "func": vdry_089_vol_below_p10_252d_flag},
    "vdry_090_vol_below_p25_252d_flag": {"inputs": ["volume"], "func": vdry_090_vol_below_p25_252d_flag},
    "vdry_091_count_below_p25_252d_in_21d": {"inputs": ["volume"], "func": vdry_091_count_below_p25_252d_in_21d},
    "vdry_092_count_below_p25_252d_in_63d": {"inputs": ["volume"], "func": vdry_092_count_below_p25_252d_in_63d},
    "vdry_093_vol_zscore_63d_pct_rank_252d": {"inputs": ["volume"], "func": vdry_093_vol_zscore_63d_pct_rank_252d},
    "vdry_094_vol_21d_std_pct_rank_252d": {"inputs": ["volume"], "func": vdry_094_vol_21d_std_pct_rank_252d},
    "vdry_095_vol_log_zscore_63d": {"inputs": ["volume"], "func": vdry_095_vol_log_zscore_63d},
    "vdry_096_dollar_vol_ratio_21d_mean": {"inputs": ["close", "volume"], "func": vdry_096_dollar_vol_ratio_21d_mean},
    "vdry_097_dollar_vol_ratio_63d_mean": {"inputs": ["close", "volume"], "func": vdry_097_dollar_vol_ratio_63d_mean},
    "vdry_098_dollar_vol_ratio_252d_mean": {"inputs": ["close", "volume"], "func": vdry_098_dollar_vol_ratio_252d_mean},
    "vdry_099_dollar_vol_zscore_63d": {"inputs": ["close", "volume"], "func": vdry_099_dollar_vol_zscore_63d},
    "vdry_100_dollar_vol_pct_rank_252d": {"inputs": ["close", "volume"], "func": vdry_100_dollar_vol_pct_rank_252d},
    "vdry_101_range_vol_ratio_21d": {"inputs": ["high", "low", "volume"], "func": vdry_101_range_vol_ratio_21d},
    "vdry_102_range_vol_ratio_63d": {"inputs": ["high", "low", "volume"], "func": vdry_102_range_vol_ratio_63d},
    "vdry_103_range_vol_zscore_63d": {"inputs": ["high", "low", "volume"], "func": vdry_103_range_vol_zscore_63d},
    "vdry_104_dollar_vol_below_p10_252d_flag": {"inputs": ["close", "volume"], "func": vdry_104_dollar_vol_below_p10_252d_flag},
    "vdry_105_vol_per_price_range_ratio_21d": {"inputs": ["high", "low", "volume"], "func": vdry_105_vol_per_price_range_ratio_21d},
    "vdry_106_days_since_vol_21d_max": {"inputs": ["volume"], "func": vdry_106_days_since_vol_21d_max},
    "vdry_107_days_since_vol_63d_max": {"inputs": ["volume"], "func": vdry_107_days_since_vol_63d_max},
    "vdry_108_vol_after_spike_decay_5d": {"inputs": ["volume"], "func": vdry_108_vol_after_spike_decay_5d},
    "vdry_109_vol_after_spike_decay_21d": {"inputs": ["volume"], "func": vdry_109_vol_after_spike_decay_21d},
    "vdry_110_vol_21d_pct_change": {"inputs": ["volume"], "func": vdry_110_vol_21d_pct_change},
    "vdry_111_vol_63d_pct_change": {"inputs": ["volume"], "func": vdry_111_vol_63d_pct_change},
    "vdry_112_vol_126d_pct_change": {"inputs": ["volume"], "func": vdry_112_vol_126d_pct_change},
    "vdry_113_vol_252d_pct_change": {"inputs": ["volume"], "func": vdry_113_vol_252d_pct_change},
    "vdry_114_vol_21d_mean_pct_change_21d": {"inputs": ["volume"], "func": vdry_114_vol_21d_mean_pct_change_21d},
    "vdry_115_vol_63d_mean_pct_change_63d": {"inputs": ["volume"], "func": vdry_115_vol_63d_mean_pct_change_63d},
    "vdry_116_low_vol_low_close_combined_21d": {"inputs": ["close", "volume"], "func": vdry_116_low_vol_low_close_combined_21d},
    "vdry_117_low_vol_near_52wk_low_flag": {"inputs": ["close", "volume"], "func": vdry_117_low_vol_near_52wk_low_flag},
    "vdry_118_vol_below_mean_on_price_decline_frac": {"inputs": ["close", "volume"], "func": vdry_118_vol_below_mean_on_price_decline_frac},
    "vdry_119_vol_below_mean_on_price_decline_frac_21d": {"inputs": ["close", "volume"], "func": vdry_119_vol_below_mean_on_price_decline_frac_21d},
    "vdry_120_vol_dryup_streak_norm_21d": {"inputs": ["volume"], "func": vdry_120_vol_dryup_streak_norm_21d},
    "vdry_121_vol_dryup_streak_norm_63d": {"inputs": ["volume"], "func": vdry_121_vol_dryup_streak_norm_63d},
    "vdry_122_consec_below_mean_21d_pct_rank_252d": {"inputs": ["volume"], "func": vdry_122_consec_below_mean_21d_pct_rank_252d},
    "vdry_123_vol_dryup_expanding_max_streak": {"inputs": ["volume"], "func": vdry_123_vol_dryup_expanding_max_streak},
    "vdry_124_vol_dryup_freq_252d": {"inputs": ["volume"], "func": vdry_124_vol_dryup_freq_252d},
    "vdry_125_avg_dryup_streak_len_252d": {"inputs": ["volume"], "func": vdry_125_avg_dryup_streak_len_252d},
    "vdry_126_vol_iqr_contraction_21d_vs_252d": {"inputs": ["volume"], "func": vdry_126_vol_iqr_contraction_21d_vs_252d},
    "vdry_127_vol_cv_21d": {"inputs": ["volume"], "func": vdry_127_vol_cv_21d},
    "vdry_128_vol_cv_63d": {"inputs": ["volume"], "func": vdry_128_vol_cv_63d},
    "vdry_129_vol_cv_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vdry_129_vol_cv_ratio_21d_vs_252d},
    "vdry_130_vol_log_ratio_21d_mean": {"inputs": ["volume"], "func": vdry_130_vol_log_ratio_21d_mean},
    "vdry_131_vol_log_ratio_252d_mean": {"inputs": ["volume"], "func": vdry_131_vol_log_ratio_252d_mean},
    "vdry_132_vol_log_ratio_63d_ema": {"inputs": ["volume"], "func": vdry_132_vol_log_ratio_63d_ema},
    "vdry_133_vol_21d_min_vs_252d_min_ratio": {"inputs": ["volume"], "func": vdry_133_vol_21d_min_vs_252d_min_ratio},
    "vdry_134_vol_21d_min_vs_252d_mean_ratio": {"inputs": ["volume"], "func": vdry_134_vol_21d_min_vs_252d_mean_ratio},
    "vdry_135_vol_5d_min_vs_63d_mean_ratio": {"inputs": ["volume"], "func": vdry_135_vol_5d_min_vs_63d_mean_ratio},
    "vdry_136_vol_times_range_below_mean_21d_flag": {"inputs": ["high", "low", "volume"], "func": vdry_136_vol_times_range_below_mean_21d_flag},
    "vdry_137_vol_times_range_zscore_21d": {"inputs": ["high", "low", "volume"], "func": vdry_137_vol_times_range_zscore_21d},
    "vdry_138_vol_times_range_pct_rank_252d": {"inputs": ["high", "low", "volume"], "func": vdry_138_vol_times_range_pct_rank_252d},
    "vdry_139_low_range_low_vol_consec_streak": {"inputs": ["high", "low", "volume"], "func": vdry_139_low_range_low_vol_consec_streak},
    "vdry_140_vol_below_mean_low_close_21d_count": {"inputs": ["close", "high", "low", "volume"], "func": vdry_140_vol_below_mean_low_close_21d_count},
    "vdry_141_narrow_range_vol_dryup_score_63d": {"inputs": ["high", "low", "volume"], "func": vdry_141_narrow_range_vol_dryup_score_63d},
    "vdry_142_open_close_range_vol_zscore_21d": {"inputs": ["close", "open", "volume"], "func": vdry_142_open_close_range_vol_zscore_21d},
    "vdry_143_vol_to_intraday_range_ratio_21d": {"inputs": ["high", "low", "volume"], "func": vdry_143_vol_to_intraday_range_ratio_21d},
    "vdry_144_vol_21d_below_median_and_range_below_median": {"inputs": ["high", "low", "volume"], "func": vdry_144_vol_21d_below_median_and_range_below_median},
    "vdry_145_dollar_vol_dryup_intensity_63d": {"inputs": ["close", "volume"], "func": vdry_145_dollar_vol_dryup_intensity_63d},
    "vdry_146_vol_dryup_composite_zscore": {"inputs": ["volume"], "func": vdry_146_vol_dryup_composite_zscore},
    "vdry_147_seller_exhaustion_score": {"inputs": ["close", "volume"], "func": vdry_147_seller_exhaustion_score},
    "vdry_148_vol_dryup_pct_rank_504d": {"inputs": ["volume"], "func": vdry_148_vol_dryup_pct_rank_504d},
    "vdry_149_vol_dryup_21d_streak_zscore": {"inputs": ["volume"], "func": vdry_149_vol_dryup_21d_streak_zscore},
    "vdry_150_vol_dryup_distress_index": {"inputs": ["close", "volume"], "func": vdry_150_vol_dryup_distress_index},
    "vdry_176_body_vol_ratio_21d_mean": {"inputs": ["close", "open", "volume"], "func": vdry_176_body_vol_ratio_21d_mean},
    "vdry_177_body_vol_ratio_63d_mean": {"inputs": ["close", "open", "volume"], "func": vdry_177_body_vol_ratio_63d_mean},
    "vdry_178_body_vol_pct_rank_252d": {"inputs": ["close", "open", "volume"], "func": vdry_178_body_vol_pct_rank_252d},
    "vdry_179_body_vol_zscore_63d": {"inputs": ["close", "open", "volume"], "func": vdry_179_body_vol_zscore_63d},
    "vdry_180_shadow_vol_ratio_21d": {"inputs": ["high", "low", "close", "open", "volume"], "func": vdry_180_shadow_vol_ratio_21d},
    "vdry_181_vol_on_gap_down_days_21d": {"inputs": ["close", "open", "volume"], "func": vdry_181_vol_on_gap_down_days_21d},
    "vdry_182_vol_open_close_shortfall_21d": {"inputs": ["close", "open", "volume"], "func": vdry_182_vol_open_close_shortfall_21d},
    "vdry_183_vol_ratio_at_open_below_prior_close": {"inputs": ["close", "open", "volume"], "func": vdry_183_vol_ratio_at_open_below_prior_close},
    "vdry_184_consec_low_body_vol_days": {"inputs": ["close", "open", "volume"], "func": vdry_184_consec_low_body_vol_days},
    "vdry_185_down_body_low_vol_frac_63d": {"inputs": ["close", "open", "volume"], "func": vdry_185_down_body_low_vol_frac_63d},
    "vdry_186_vol_decay_from_5d_max": {"inputs": ["volume"], "func": vdry_186_vol_decay_from_5d_max},
    "vdry_187_vol_decay_from_126d_max": {"inputs": ["volume"], "func": vdry_187_vol_decay_from_126d_max},
    "vdry_188_log_vol_decay_from_21d_max": {"inputs": ["volume"], "func": vdry_188_log_vol_decay_from_21d_max},
    "vdry_189_log_vol_decay_from_252d_max": {"inputs": ["volume"], "func": vdry_189_log_vol_decay_from_252d_max},
    "vdry_190_vol_5d_max_to_5d_min_ratio": {"inputs": ["volume"], "func": vdry_190_vol_5d_max_to_5d_min_ratio},
    "vdry_191_vol_21d_max_to_252d_mean_ratio": {"inputs": ["volume"], "func": vdry_191_vol_21d_max_to_252d_mean_ratio},
    "vdry_192_vol_contraction_5d_vs_21d_max": {"inputs": ["volume"], "func": vdry_192_vol_contraction_5d_vs_21d_max},
    "vdry_193_vol_decay_from_252d_max_pct_rank_252d": {"inputs": ["volume"], "func": vdry_193_vol_decay_from_252d_max_pct_rank_252d},
    "vdry_194_vol_21d_min_vs_63d_mean_ratio": {"inputs": ["volume"], "func": vdry_194_vol_21d_min_vs_63d_mean_ratio},
    "vdry_195_vol_5d_min_vs_252d_mean_ratio": {"inputs": ["volume"], "func": vdry_195_vol_5d_min_vs_252d_mean_ratio},
    "vdry_196_dollar_vol_zscore_21d": {"inputs": ["close", "volume"], "func": vdry_196_dollar_vol_zscore_21d},
    "vdry_197_dollar_vol_log_ratio_21d_mean": {"inputs": ["close", "volume"], "func": vdry_197_dollar_vol_log_ratio_21d_mean},
    "vdry_198_range_dollar_vol_composite_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": vdry_198_range_dollar_vol_composite_zscore_63d},
    "vdry_199_vol_dryup_all_windows_flag": {"inputs": ["volume"], "func": vdry_199_vol_dryup_all_windows_flag},
    "vdry_200_vol_dryup_weighted_shortfall_252d": {"inputs": ["volume"], "func": vdry_200_vol_dryup_weighted_shortfall_252d},
}
