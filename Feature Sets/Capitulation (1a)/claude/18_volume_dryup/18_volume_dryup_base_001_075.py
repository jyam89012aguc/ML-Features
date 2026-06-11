"""
18_volume_dryup — Base Features 001-100
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Volume vs. trailing mean — raw ratios ---

def vdry_001_vol_ratio_21d_mean(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 21-day trailing mean."""
    return _safe_div(volume, _rolling_mean(volume, _TD_MON))


def vdry_002_vol_ratio_63d_mean(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 63-day trailing mean."""
    return _safe_div(volume, _rolling_mean(volume, _TD_QTR))


def vdry_003_vol_ratio_126d_mean(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 126-day trailing mean."""
    return _safe_div(volume, _rolling_mean(volume, _TD_HALF))


def vdry_004_vol_ratio_252d_mean(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 252-day trailing mean."""
    return _safe_div(volume, _rolling_mean(volume, _TD_YEAR))


def vdry_005_vol_ratio_21d_median(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 21-day trailing median."""
    return _safe_div(volume, _rolling_median(volume, _TD_MON))


def vdry_006_vol_ratio_63d_median(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 63-day trailing median."""
    return _safe_div(volume, _rolling_median(volume, _TD_QTR))


def vdry_007_vol_ratio_252d_median(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 252-day trailing median."""
    return _safe_div(volume, _rolling_median(volume, _TD_YEAR))


def vdry_008_vol_ratio_21d_ema(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 21-day EMA (exponentially smoothed baseline)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_MON))


def vdry_009_vol_ratio_63d_ema(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 63-day EMA."""
    return _safe_div(volume, _ewm_mean(volume, _TD_QTR))


def vdry_010_vol_ratio_252d_ema(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 252-day EMA."""
    return _safe_div(volume, _ewm_mean(volume, _TD_YEAR))


# --- Group B (011-020): Volume z-scores below baseline ---

def vdry_011_vol_zscore_21d(volume: pd.Series) -> pd.Series:
    """Z-score of volume relative to 21-day mean and std (negative = drying up)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(volume - m, s)


def vdry_012_vol_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of volume relative to 63-day mean and std."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    return _safe_div(volume - m, s)


def vdry_013_vol_zscore_126d(volume: pd.Series) -> pd.Series:
    """Z-score of volume relative to 126-day mean and std."""
    m = _rolling_mean(volume, _TD_HALF)
    s = _rolling_std(volume, _TD_HALF)
    return _safe_div(volume - m, s)


def vdry_014_vol_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of volume relative to 252-day mean and std."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    return _safe_div(volume - m, s)


def vdry_015_vol_below_mean_21d_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: today's volume is below its 21-day mean."""
    return (volume < _rolling_mean(volume, _TD_MON)).astype(float)


def vdry_016_vol_below_median_63d_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: today's volume is below its 63-day median."""
    return (volume < _rolling_median(volume, _TD_QTR)).astype(float)


def vdry_017_vol_below_mean_252d_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: today's volume is below its 252-day mean."""
    return (volume < _rolling_mean(volume, _TD_YEAR)).astype(float)


def vdry_018_vol_pct_rank_63d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 63-day distribution."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vdry_019_vol_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 252-day distribution."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_020_vol_log_ratio_63d_mean(volume: pd.Series) -> pd.Series:
    """Log of (volume / 63-day mean); negative values indicate dry-up."""
    return _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_QTR))


# --- Group C (021-030): Consecutive low-volume streaks ---

def vdry_021_consec_below_mean_21d(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume < 21-day mean."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _consec_streak(cond)


def vdry_022_consec_below_mean_63d(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume < 63-day mean."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    return _consec_streak(cond)


def vdry_023_consec_below_mean_252d(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume < 252-day mean."""
    cond = volume < _rolling_mean(volume, _TD_YEAR)
    return _consec_streak(cond)


def vdry_024_consec_below_median_63d(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume < 63-day median."""
    cond = volume < _rolling_median(volume, _TD_QTR)
    return _consec_streak(cond)


def vdry_025_consec_vol_declining(volume: pd.Series) -> pd.Series:
    """Current consecutive days where volume < prior-day volume (shrinking)."""
    cond = volume < volume.shift(1)
    return _consec_streak(cond)


def vdry_026_consec_vol_below_half_mean_21d(volume: pd.Series) -> pd.Series:
    """Streak of days where volume < 50% of 21-day mean (extreme dryup)."""
    cond = volume < 0.5 * _rolling_mean(volume, _TD_MON)
    return _consec_streak(cond)


def vdry_027_consec_vol_below_75pct_mean_63d(volume: pd.Series) -> pd.Series:
    """Streak of days where volume < 75% of 63-day mean."""
    cond = volume < 0.75 * _rolling_mean(volume, _TD_QTR)
    return _consec_streak(cond)


def vdry_028_max_consec_below_mean_21d_63d(volume: pd.Series) -> pd.Series:
    """Maximum below-21d-mean consecutive streak within trailing 63 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_max_streak(cond, _TD_QTR)


def vdry_029_max_consec_below_mean_21d_252d(volume: pd.Series) -> pd.Series:
    """Maximum below-21d-mean consecutive streak within trailing 252 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_max_streak(cond, _TD_YEAR)


def vdry_030_max_consec_declining_vol_63d(volume: pd.Series) -> pd.Series:
    """Maximum consecutive declining-volume days within trailing 63 days."""
    cond = volume < volume.shift(1)
    return _rolling_max_streak(cond, _TD_QTR)


# --- Group D (031-040): Count of low-volume days in windows ---

def vdry_031_count_below_mean_21d_in_21d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 21-day mean over trailing 21 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_MON)


def vdry_032_count_below_mean_21d_in_63d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 21-day mean over trailing 63 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_QTR)


def vdry_033_count_below_mean_63d_in_63d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 63-day mean over trailing 63 days."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    return _rolling_count_true(cond, _TD_QTR)


def vdry_034_count_below_mean_252d_in_252d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 252-day mean over trailing 252 days."""
    cond = volume < _rolling_mean(volume, _TD_YEAR)
    return _rolling_count_true(cond, _TD_YEAR)


def vdry_035_frac_below_mean_21d_in_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where volume < 21-day mean."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def vdry_036_frac_below_mean_63d_in_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume < 63-day mean."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vdry_037_frac_below_median_63d_in_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume < 63-day rolling median."""
    cond = volume < _rolling_median(volume, _TD_QTR)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vdry_038_count_extreme_low_vol_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21 days where volume < 25th-pctile of 252-day vol."""
    p25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    cond = volume < p25
    return _rolling_count_true(cond, _TD_MON)


def vdry_039_count_extreme_low_vol_63d(volume: pd.Series) -> pd.Series:
    """Count of days in last 63 days where volume < 25th-pctile of 252-day vol."""
    p25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    cond = volume < p25
    return _rolling_count_true(cond, _TD_QTR)


def vdry_040_count_declining_vol_in_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21 days where volume declined day-over-day."""
    cond = volume < volume.shift(1)
    return _rolling_count_true(cond, _TD_MON)


# --- Group E (041-050): Trailing minimum volume and days-since-low ---

def vdry_041_trailing_min_vol_21d(volume: pd.Series) -> pd.Series:
    """Trailing 21-day minimum volume."""
    return _rolling_min(volume, _TD_MON)


def vdry_042_trailing_min_vol_63d(volume: pd.Series) -> pd.Series:
    """Trailing 63-day minimum volume."""
    return _rolling_min(volume, _TD_QTR)


def vdry_043_trailing_min_vol_252d(volume: pd.Series) -> pd.Series:
    """Trailing 252-day minimum volume."""
    return _rolling_min(volume, _TD_YEAR)


def vdry_044_vol_vs_21d_min_ratio(volume: pd.Series) -> pd.Series:
    """Today's volume divided by trailing 21-day minimum volume."""
    return _safe_div(volume, _rolling_min(volume.shift(1), _TD_MON))


def vdry_045_vol_vs_63d_min_ratio(volume: pd.Series) -> pd.Series:
    """Today's volume divided by trailing 63-day minimum volume."""
    return _safe_div(volume, _rolling_min(volume.shift(1), _TD_QTR))


def vdry_046_vol_vs_252d_min_ratio(volume: pd.Series) -> pd.Series:
    """Today's volume divided by trailing 252-day minimum volume."""
    return _safe_div(volume, _rolling_min(volume.shift(1), _TD_YEAR))


def vdry_047_days_since_vol_252d_min(volume: pd.Series) -> pd.Series:
    """Number of days since volume last touched its 252-day rolling minimum."""
    min252 = _rolling_min(volume, _TD_YEAR)
    at_min = (volume <= min252).astype(float)
    def _days_since(arr):
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 1.0:
                return float(len(arr) - 1 - i)
        return float(len(arr))
    return at_min.rolling(_TD_YEAR, min_periods=1).apply(_days_since, raw=True)


def vdry_048_new_252d_vol_low_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is a new 252-day low."""
    prev_min = volume.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).min()
    return (volume < prev_min).astype(float)


def vdry_049_new_63d_vol_low_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is a new 63-day low."""
    prev_min = volume.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (volume < prev_min).astype(float)


def vdry_050_consec_new_63d_vol_low(volume: pd.Series) -> pd.Series:
    """Current consecutive days making a new 63-day volume low."""
    prev_min = volume.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    cond = volume < prev_min
    return _consec_streak(cond)


# --- Group F (051-060): Volume contraction after a prior spike ---

def vdry_051_vol_decay_from_21d_max(volume: pd.Series) -> pd.Series:
    """Volume divided by its 21-day trailing maximum (how far below the recent peak)."""
    return _safe_div(volume, _rolling_max(volume.shift(1), _TD_MON))


def vdry_052_vol_decay_from_63d_max(volume: pd.Series) -> pd.Series:
    """Volume divided by its 63-day trailing maximum."""
    return _safe_div(volume, _rolling_max(volume.shift(1), _TD_QTR))


def vdry_053_vol_decay_from_252d_max(volume: pd.Series) -> pd.Series:
    """Volume divided by its 252-day trailing maximum."""
    return _safe_div(volume, _rolling_max(volume.shift(1), _TD_YEAR))


def vdry_054_log_vol_decay_from_63d_max(volume: pd.Series) -> pd.Series:
    """Log of (volume / 63-day max); deeply negative = extreme dryup after a spike."""
    return _log_safe(volume) - _log_safe(_rolling_max(volume.shift(1), _TD_QTR))


def vdry_055_vol_max_to_min_ratio_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day volume max to 63-day volume min (range of extremes)."""
    mx = _rolling_max(volume, _TD_QTR)
    mn = _rolling_min(volume, _TD_QTR)
    return _safe_div(mx, mn)


def vdry_056_vol_contraction_5d_vs_63d_max(volume: pd.Series) -> pd.Series:
    """5-day mean volume divided by 63-day max volume (recent shrinkage)."""
    recent = _rolling_mean(volume, _TD_WEEK)
    mx63 = _rolling_max(volume.shift(1), _TD_QTR)
    return _safe_div(recent, mx63)


def vdry_057_vol_contraction_21d_vs_252d_max(volume: pd.Series) -> pd.Series:
    """21-day mean volume divided by 252-day max volume."""
    recent = _rolling_mean(volume, _TD_MON)
    mx252 = _rolling_max(volume.shift(1), _TD_YEAR)
    return _safe_div(recent, mx252)


def vdry_058_vol_std_contraction_21d_vs_63d(volume: pd.Series) -> pd.Series:
    """21-day vol-std divided by 63-day vol-std (narrowing of volume variability)."""
    s21 = _rolling_std(volume, _TD_MON)
    s63 = _rolling_std(volume, _TD_QTR)
    return _safe_div(s21, s63)


def vdry_059_vol_21d_mean_pct_change_63d(volume: pd.Series) -> pd.Series:
    """Percent change in 21-day mean volume over 63 days (trend in baseline)."""
    m21 = _rolling_mean(volume, _TD_MON)
    return _safe_div(m21 - m21.shift(_TD_QTR), m21.shift(_TD_QTR).abs().replace(0, np.nan))


def vdry_060_vol_spike_then_dryup_ratio(volume: pd.Series) -> pd.Series:
    """5-day mean vol divided by the peak 5-day mean vol over prior 63 days."""
    m5 = _rolling_mean(volume, _TD_WEEK)
    peak_m5 = _rolling_max(m5.shift(1), _TD_QTR)
    return _safe_div(m5, peak_m5)


# --- Group G (061-075): Multi-day volume decay and on-price-decline context ---

def vdry_061_vol_decay_5d_slope(volume: pd.Series) -> pd.Series:
    """OLS slope of volume over last 5 days (negative = shrinking quickly)."""
    def _slope(arr):
        if len(arr) < 2:
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi_m = xi.mean()
        x_m = arr.mean()
        num = ((xi - xi_m) * (arr - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return volume.rolling(_TD_WEEK, min_periods=2).apply(_slope, raw=True)


def vdry_062_vol_decay_21d_slope(volume: pd.Series) -> pd.Series:
    """OLS slope of volume over last 21 days."""
    def _slope(arr):
        if len(arr) < 2:
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi_m = xi.mean()
        x_m = arr.mean()
        num = ((xi - xi_m) * (arr - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return volume.rolling(_TD_MON, min_periods=2).apply(_slope, raw=True)


def vdry_063_low_vol_on_down_close_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in last 21 days where close fell AND volume < 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (close < close.shift(1)) & (volume < mean63)
    return _rolling_count_true(cond, _TD_MON)


def vdry_064_low_vol_on_down_close_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in last 63 days where close fell AND volume < 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    cond = (close < close.shift(1)) & (volume < mean63)
    return _rolling_count_true(cond, _TD_QTR)


def vdry_065_consec_low_vol_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current streak of days where close < prior close AND volume < 21d mean."""
    mean21 = _rolling_mean(volume, _TD_MON)
    cond = (close < close.shift(1)) & (volume < mean21)
    return _consec_streak(cond)


def vdry_066_vol_ratio_on_down_vs_up_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume on down days / avg volume on up days over 21 days."""
    ret = close.pct_change(1)
    dn = volume.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up = volume.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(dn, up)


def vdry_067_dryup_on_down_day_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today close < prior close AND volume < 50% of 21d mean (exhausted sellers)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    cond = (close < close.shift(1)) & (volume < 0.5 * mean21)
    return cond.astype(float)


def vdry_068_vol_21d_mean_vs_63d_mean_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day mean volume to 63-day mean volume (recent vs. medium baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))


def vdry_069_vol_5d_mean_vs_21d_mean_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day mean volume to 21-day mean volume (very short vs. short baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))


def vdry_070_vol_5d_mean_vs_252d_mean_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day mean volume to 252-day mean volume (acute collapse measure)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_YEAR))


def vdry_071_vol_zscore_21d_below_zero_flag(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume z-score is negative (below the recent mean)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    return (z < 0).astype(float)


def vdry_072_vol_dryup_days_below_m1sd_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21 days with volume below mean - 1 std (true dryup)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    threshold = m - s
    cond = volume < threshold
    return _rolling_count_true(cond, _TD_MON)


def vdry_073_vol_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of today's volume."""
    return volume.expanding(min_periods=1).rank(pct=True)


def vdry_074_vol_dryup_intensity_21d(volume: pd.Series) -> pd.Series:
    """Sum of (1 - vol/mean21) for days below the mean over 21 days (depth of dryup)."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_MON)


def vdry_075_vol_dryup_intensity_63d(volume: pd.Series) -> pd.Series:
    """Sum of (1 - vol/mean63) for days below the 63-day mean over 63 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_QTR)


# --- Group P (151-160): Volume dry-up relative to EMA baselines ---

def vdry_151_vol_ratio_5d_ema(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 5-day EMA (ultra-short baseline dryup)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_WEEK))


def vdry_152_vol_ratio_126d_ema(volume: pd.Series) -> pd.Series:
    """Today's volume divided by its 126-day EMA (semi-annual baseline dryup)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_HALF))


def vdry_153_vol_5d_ema_vs_63d_ema_ratio(volume: pd.Series) -> pd.Series:
    """5-day EMA volume divided by 63-day EMA (short vs medium EMA collapse)."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))


def vdry_154_vol_21d_ema_vs_252d_ema_ratio(volume: pd.Series) -> pd.Series:
    """21-day EMA volume divided by 252-day EMA (monthly vs annual EMA collapse)."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_YEAR))


def vdry_155_vol_zscore_21d_ema_baseline(volume: pd.Series) -> pd.Series:
    """Z-score of (volume - 21d EMA) / 21d rolling std."""
    ema = _ewm_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    return _safe_div(volume - ema, s)


def vdry_156_log_vol_ratio_21d_ema(volume: pd.Series) -> pd.Series:
    """Log(volume / 21d EMA); negative = below exponential baseline."""
    return _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_MON))


def vdry_157_log_vol_ratio_126d_ema(volume: pd.Series) -> pd.Series:
    """Log(volume / 126d EMA); semi-annual EMA dryup measure."""
    return _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_HALF))


def vdry_158_vol_below_5d_ema_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: today's volume is below its 5-day EMA."""
    return (volume < _ewm_mean(volume, _TD_WEEK)).astype(float)


def vdry_159_vol_below_126d_ema_flag(volume: pd.Series) -> pd.Series:
    """Binary flag: today's volume is below its 126-day EMA."""
    return (volume < _ewm_mean(volume, _TD_HALF)).astype(float)


def vdry_160_consec_below_63d_ema(volume: pd.Series) -> pd.Series:
    """Consecutive days where volume < 63-day EMA."""
    cond = volume < _ewm_mean(volume, _TD_QTR)
    return _consec_streak(cond)


# --- Group Q (161-170): Quantile-based dryup thresholds ---

def vdry_161_vol_below_p10_63d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is below the 10th percentile of trailing 63 days."""
    p10 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    return (volume < p10).astype(float)


def vdry_162_vol_below_p25_63d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is below the 25th percentile of trailing 63 days."""
    p25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return (volume < p25).astype(float)


def vdry_163_vol_below_p10_126d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is below the 10th percentile of trailing 126 days."""
    p10 = volume.rolling(_TD_HALF, min_periods=_TD_QTR).quantile(0.10)
    return (volume < p10).astype(float)


def vdry_164_count_below_p10_63d_in_21d(volume: pd.Series) -> pd.Series:
    """Count of days in last 21d where volume < 10th percentile of 63-day dist."""
    p10 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    cond = volume < p10
    return _rolling_count_true(cond, _TD_MON)


def vdry_165_count_below_p10_252d_in_63d(volume: pd.Series) -> pd.Series:
    """Count of days in last 63d where volume < 10th percentile of 252-day dist."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    cond = volume < p10
    return _rolling_count_true(cond, _TD_QTR)


def vdry_166_vol_pct_rank_5d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 5-day distribution."""
    return volume.rolling(_TD_WEEK, min_periods=1).rank(pct=True)


def vdry_167_vol_zscore_5d(volume: pd.Series) -> pd.Series:
    """Z-score of volume relative to 5-day mean and std."""
    m = _rolling_mean(volume, _TD_WEEK)
    s = _rolling_std(volume, _TD_WEEK)
    return _safe_div(volume - m, s)


def vdry_168_vol_quantile_spread_252d(volume: pd.Series) -> pd.Series:
    """Spread between 75th and 25th percentile of 252-day vol (distribution width)."""
    q75 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


def vdry_169_vol_quantile_spread_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day IQR to 252-day IQR (distribution compression measure)."""
    q75_21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    q25_21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    q75_252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25_252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    iqr21 = q75_21 - q25_21
    iqr252 = (q75_252 - q25_252).replace(0, np.nan)
    return _safe_div(iqr21, iqr252)


def vdry_170_frac_below_p10_252d_in_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where volume < 10th percentile of 252-day dist."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    cond = volume < p10
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


# --- Group R (171-175): Multi-signal composite and price-adjusted exhaustion ---

def vdry_171_vol_5d_mean_pct_change_21d(volume: pd.Series) -> pd.Series:
    """Percent change in 5-day mean volume over 21 days (recent vs. 3-week-ago pace)."""
    m5 = _rolling_mean(volume, _TD_WEEK)
    return _safe_div(m5 - m5.shift(_TD_MON), m5.shift(_TD_MON).abs().replace(0, np.nan))


def vdry_172_vol_dryup_intensity_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day dryup intensity within trailing 252-day distribution."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    intensity = _rolling_sum(shortfall, _TD_MON)
    return intensity.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_173_vol_std_ratio_5d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day vol-std to 252-day vol-std (extreme short-term quietude)."""
    return _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_std(volume, _TD_YEAR))


def vdry_174_vol_below_mean_and_new_low_63d_combined(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of days where volume < 63d mean AND close < prior 63d low."""
    prev_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    cond = (volume < _rolling_mean(volume, _TD_QTR)) & (close < prev_min)
    return _consec_streak(cond)


def vdry_175_vol_dryup_breadth_score_multi(volume: pd.Series) -> pd.Series:
    """Count of three dryup flags: below 21d mean, below 63d mean, below 252d mean."""
    f1 = (volume < _rolling_mean(volume, _TD_MON)).astype(float)
    f2 = (volume < _rolling_mean(volume, _TD_QTR)).astype(float)
    f3 = (volume < _rolling_mean(volume, _TD_YEAR)).astype(float)
    return f1 + f2 + f3


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DRYUP_REGISTRY_001_075 = {
    "vdry_001_vol_ratio_21d_mean": {"inputs": ["volume"], "func": vdry_001_vol_ratio_21d_mean},
    "vdry_002_vol_ratio_63d_mean": {"inputs": ["volume"], "func": vdry_002_vol_ratio_63d_mean},
    "vdry_003_vol_ratio_126d_mean": {"inputs": ["volume"], "func": vdry_003_vol_ratio_126d_mean},
    "vdry_004_vol_ratio_252d_mean": {"inputs": ["volume"], "func": vdry_004_vol_ratio_252d_mean},
    "vdry_005_vol_ratio_21d_median": {"inputs": ["volume"], "func": vdry_005_vol_ratio_21d_median},
    "vdry_006_vol_ratio_63d_median": {"inputs": ["volume"], "func": vdry_006_vol_ratio_63d_median},
    "vdry_007_vol_ratio_252d_median": {"inputs": ["volume"], "func": vdry_007_vol_ratio_252d_median},
    "vdry_008_vol_ratio_21d_ema": {"inputs": ["volume"], "func": vdry_008_vol_ratio_21d_ema},
    "vdry_009_vol_ratio_63d_ema": {"inputs": ["volume"], "func": vdry_009_vol_ratio_63d_ema},
    "vdry_010_vol_ratio_252d_ema": {"inputs": ["volume"], "func": vdry_010_vol_ratio_252d_ema},
    "vdry_011_vol_zscore_21d": {"inputs": ["volume"], "func": vdry_011_vol_zscore_21d},
    "vdry_012_vol_zscore_63d": {"inputs": ["volume"], "func": vdry_012_vol_zscore_63d},
    "vdry_013_vol_zscore_126d": {"inputs": ["volume"], "func": vdry_013_vol_zscore_126d},
    "vdry_014_vol_zscore_252d": {"inputs": ["volume"], "func": vdry_014_vol_zscore_252d},
    "vdry_015_vol_below_mean_21d_flag": {"inputs": ["volume"], "func": vdry_015_vol_below_mean_21d_flag},
    "vdry_016_vol_below_median_63d_flag": {"inputs": ["volume"], "func": vdry_016_vol_below_median_63d_flag},
    "vdry_017_vol_below_mean_252d_flag": {"inputs": ["volume"], "func": vdry_017_vol_below_mean_252d_flag},
    "vdry_018_vol_pct_rank_63d": {"inputs": ["volume"], "func": vdry_018_vol_pct_rank_63d},
    "vdry_019_vol_pct_rank_252d": {"inputs": ["volume"], "func": vdry_019_vol_pct_rank_252d},
    "vdry_020_vol_log_ratio_63d_mean": {"inputs": ["volume"], "func": vdry_020_vol_log_ratio_63d_mean},
    "vdry_021_consec_below_mean_21d": {"inputs": ["volume"], "func": vdry_021_consec_below_mean_21d},
    "vdry_022_consec_below_mean_63d": {"inputs": ["volume"], "func": vdry_022_consec_below_mean_63d},
    "vdry_023_consec_below_mean_252d": {"inputs": ["volume"], "func": vdry_023_consec_below_mean_252d},
    "vdry_024_consec_below_median_63d": {"inputs": ["volume"], "func": vdry_024_consec_below_median_63d},
    "vdry_025_consec_vol_declining": {"inputs": ["volume"], "func": vdry_025_consec_vol_declining},
    "vdry_026_consec_vol_below_half_mean_21d": {"inputs": ["volume"], "func": vdry_026_consec_vol_below_half_mean_21d},
    "vdry_027_consec_vol_below_75pct_mean_63d": {"inputs": ["volume"], "func": vdry_027_consec_vol_below_75pct_mean_63d},
    "vdry_028_max_consec_below_mean_21d_63d": {"inputs": ["volume"], "func": vdry_028_max_consec_below_mean_21d_63d},
    "vdry_029_max_consec_below_mean_21d_252d": {"inputs": ["volume"], "func": vdry_029_max_consec_below_mean_21d_252d},
    "vdry_030_max_consec_declining_vol_63d": {"inputs": ["volume"], "func": vdry_030_max_consec_declining_vol_63d},
    "vdry_031_count_below_mean_21d_in_21d": {"inputs": ["volume"], "func": vdry_031_count_below_mean_21d_in_21d},
    "vdry_032_count_below_mean_21d_in_63d": {"inputs": ["volume"], "func": vdry_032_count_below_mean_21d_in_63d},
    "vdry_033_count_below_mean_63d_in_63d": {"inputs": ["volume"], "func": vdry_033_count_below_mean_63d_in_63d},
    "vdry_034_count_below_mean_252d_in_252d": {"inputs": ["volume"], "func": vdry_034_count_below_mean_252d_in_252d},
    "vdry_035_frac_below_mean_21d_in_21d": {"inputs": ["volume"], "func": vdry_035_frac_below_mean_21d_in_21d},
    "vdry_036_frac_below_mean_63d_in_63d": {"inputs": ["volume"], "func": vdry_036_frac_below_mean_63d_in_63d},
    "vdry_037_frac_below_median_63d_in_63d": {"inputs": ["volume"], "func": vdry_037_frac_below_median_63d_in_63d},
    "vdry_038_count_extreme_low_vol_21d": {"inputs": ["volume"], "func": vdry_038_count_extreme_low_vol_21d},
    "vdry_039_count_extreme_low_vol_63d": {"inputs": ["volume"], "func": vdry_039_count_extreme_low_vol_63d},
    "vdry_040_count_declining_vol_in_21d": {"inputs": ["volume"], "func": vdry_040_count_declining_vol_in_21d},
    "vdry_041_trailing_min_vol_21d": {"inputs": ["volume"], "func": vdry_041_trailing_min_vol_21d},
    "vdry_042_trailing_min_vol_63d": {"inputs": ["volume"], "func": vdry_042_trailing_min_vol_63d},
    "vdry_043_trailing_min_vol_252d": {"inputs": ["volume"], "func": vdry_043_trailing_min_vol_252d},
    "vdry_044_vol_vs_21d_min_ratio": {"inputs": ["volume"], "func": vdry_044_vol_vs_21d_min_ratio},
    "vdry_045_vol_vs_63d_min_ratio": {"inputs": ["volume"], "func": vdry_045_vol_vs_63d_min_ratio},
    "vdry_046_vol_vs_252d_min_ratio": {"inputs": ["volume"], "func": vdry_046_vol_vs_252d_min_ratio},
    "vdry_047_days_since_vol_252d_min": {"inputs": ["volume"], "func": vdry_047_days_since_vol_252d_min},
    "vdry_048_new_252d_vol_low_flag": {"inputs": ["volume"], "func": vdry_048_new_252d_vol_low_flag},
    "vdry_049_new_63d_vol_low_flag": {"inputs": ["volume"], "func": vdry_049_new_63d_vol_low_flag},
    "vdry_050_consec_new_63d_vol_low": {"inputs": ["volume"], "func": vdry_050_consec_new_63d_vol_low},
    "vdry_051_vol_decay_from_21d_max": {"inputs": ["volume"], "func": vdry_051_vol_decay_from_21d_max},
    "vdry_052_vol_decay_from_63d_max": {"inputs": ["volume"], "func": vdry_052_vol_decay_from_63d_max},
    "vdry_053_vol_decay_from_252d_max": {"inputs": ["volume"], "func": vdry_053_vol_decay_from_252d_max},
    "vdry_054_log_vol_decay_from_63d_max": {"inputs": ["volume"], "func": vdry_054_log_vol_decay_from_63d_max},
    "vdry_055_vol_max_to_min_ratio_63d": {"inputs": ["volume"], "func": vdry_055_vol_max_to_min_ratio_63d},
    "vdry_056_vol_contraction_5d_vs_63d_max": {"inputs": ["volume"], "func": vdry_056_vol_contraction_5d_vs_63d_max},
    "vdry_057_vol_contraction_21d_vs_252d_max": {"inputs": ["volume"], "func": vdry_057_vol_contraction_21d_vs_252d_max},
    "vdry_058_vol_std_contraction_21d_vs_63d": {"inputs": ["volume"], "func": vdry_058_vol_std_contraction_21d_vs_63d},
    "vdry_059_vol_21d_mean_pct_change_63d": {"inputs": ["volume"], "func": vdry_059_vol_21d_mean_pct_change_63d},
    "vdry_060_vol_spike_then_dryup_ratio": {"inputs": ["volume"], "func": vdry_060_vol_spike_then_dryup_ratio},
    "vdry_061_vol_decay_5d_slope": {"inputs": ["volume"], "func": vdry_061_vol_decay_5d_slope},
    "vdry_062_vol_decay_21d_slope": {"inputs": ["volume"], "func": vdry_062_vol_decay_21d_slope},
    "vdry_063_low_vol_on_down_close_21d": {"inputs": ["close", "volume"], "func": vdry_063_low_vol_on_down_close_21d},
    "vdry_064_low_vol_on_down_close_63d": {"inputs": ["close", "volume"], "func": vdry_064_low_vol_on_down_close_63d},
    "vdry_065_consec_low_vol_down_days": {"inputs": ["close", "volume"], "func": vdry_065_consec_low_vol_down_days},
    "vdry_066_vol_ratio_on_down_vs_up_21d": {"inputs": ["close", "volume"], "func": vdry_066_vol_ratio_on_down_vs_up_21d},
    "vdry_067_dryup_on_down_day_flag": {"inputs": ["close", "volume"], "func": vdry_067_dryup_on_down_day_flag},
    "vdry_068_vol_21d_mean_vs_63d_mean_ratio": {"inputs": ["volume"], "func": vdry_068_vol_21d_mean_vs_63d_mean_ratio},
    "vdry_069_vol_5d_mean_vs_21d_mean_ratio": {"inputs": ["volume"], "func": vdry_069_vol_5d_mean_vs_21d_mean_ratio},
    "vdry_070_vol_5d_mean_vs_252d_mean_ratio": {"inputs": ["volume"], "func": vdry_070_vol_5d_mean_vs_252d_mean_ratio},
    "vdry_071_vol_zscore_21d_below_zero_flag": {"inputs": ["volume"], "func": vdry_071_vol_zscore_21d_below_zero_flag},
    "vdry_072_vol_dryup_days_below_m1sd_21d": {"inputs": ["volume"], "func": vdry_072_vol_dryup_days_below_m1sd_21d},
    "vdry_073_vol_expanding_rank": {"inputs": ["volume"], "func": vdry_073_vol_expanding_rank},
    "vdry_074_vol_dryup_intensity_21d": {"inputs": ["volume"], "func": vdry_074_vol_dryup_intensity_21d},
    "vdry_075_vol_dryup_intensity_63d": {"inputs": ["volume"], "func": vdry_075_vol_dryup_intensity_63d},
    "vdry_151_vol_ratio_5d_ema": {"inputs": ["volume"], "func": vdry_151_vol_ratio_5d_ema},
    "vdry_152_vol_ratio_126d_ema": {"inputs": ["volume"], "func": vdry_152_vol_ratio_126d_ema},
    "vdry_153_vol_5d_ema_vs_63d_ema_ratio": {"inputs": ["volume"], "func": vdry_153_vol_5d_ema_vs_63d_ema_ratio},
    "vdry_154_vol_21d_ema_vs_252d_ema_ratio": {"inputs": ["volume"], "func": vdry_154_vol_21d_ema_vs_252d_ema_ratio},
    "vdry_155_vol_zscore_21d_ema_baseline": {"inputs": ["volume"], "func": vdry_155_vol_zscore_21d_ema_baseline},
    "vdry_156_log_vol_ratio_21d_ema": {"inputs": ["volume"], "func": vdry_156_log_vol_ratio_21d_ema},
    "vdry_157_log_vol_ratio_126d_ema": {"inputs": ["volume"], "func": vdry_157_log_vol_ratio_126d_ema},
    "vdry_158_vol_below_5d_ema_flag": {"inputs": ["volume"], "func": vdry_158_vol_below_5d_ema_flag},
    "vdry_159_vol_below_126d_ema_flag": {"inputs": ["volume"], "func": vdry_159_vol_below_126d_ema_flag},
    "vdry_160_consec_below_63d_ema": {"inputs": ["volume"], "func": vdry_160_consec_below_63d_ema},
    "vdry_161_vol_below_p10_63d_flag": {"inputs": ["volume"], "func": vdry_161_vol_below_p10_63d_flag},
    "vdry_162_vol_below_p25_63d_flag": {"inputs": ["volume"], "func": vdry_162_vol_below_p25_63d_flag},
    "vdry_163_vol_below_p10_126d_flag": {"inputs": ["volume"], "func": vdry_163_vol_below_p10_126d_flag},
    "vdry_164_count_below_p10_63d_in_21d": {"inputs": ["volume"], "func": vdry_164_count_below_p10_63d_in_21d},
    "vdry_165_count_below_p10_252d_in_63d": {"inputs": ["volume"], "func": vdry_165_count_below_p10_252d_in_63d},
    "vdry_166_vol_pct_rank_5d": {"inputs": ["volume"], "func": vdry_166_vol_pct_rank_5d},
    "vdry_167_vol_zscore_5d": {"inputs": ["volume"], "func": vdry_167_vol_zscore_5d},
    "vdry_168_vol_quantile_spread_252d": {"inputs": ["volume"], "func": vdry_168_vol_quantile_spread_252d},
    "vdry_169_vol_quantile_spread_21d_vs_252d": {"inputs": ["volume"], "func": vdry_169_vol_quantile_spread_21d_vs_252d},
    "vdry_170_frac_below_p10_252d_in_63d": {"inputs": ["volume"], "func": vdry_170_frac_below_p10_252d_in_63d},
    "vdry_171_vol_5d_mean_pct_change_21d": {"inputs": ["volume"], "func": vdry_171_vol_5d_mean_pct_change_21d},
    "vdry_172_vol_dryup_intensity_21d_pct_rank_252d": {"inputs": ["volume"], "func": vdry_172_vol_dryup_intensity_21d_pct_rank_252d},
    "vdry_173_vol_std_ratio_5d_vs_252d": {"inputs": ["volume"], "func": vdry_173_vol_std_ratio_5d_vs_252d},
    "vdry_174_vol_below_mean_and_new_low_63d_combined": {"inputs": ["close", "volume"], "func": vdry_174_vol_below_mean_and_new_low_63d_combined},
    "vdry_175_vol_dryup_breadth_score_multi": {"inputs": ["volume"], "func": vdry_175_vol_dryup_breadth_score_multi},
}
