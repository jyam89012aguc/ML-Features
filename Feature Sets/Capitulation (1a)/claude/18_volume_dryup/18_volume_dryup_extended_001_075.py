"""
18_volume_dryup — Extended Features 001-075
Domain: volume collapse / exhaustion of selling — volume dry-up below trailing baseline
         Deeper variants: EWM dryup, quantile thresholds, half-life decay, cross-window
         spreads, regime persistence, dollar-vol extended, open/high/low price-vol context,
         log-ratio smoothed, volatility-adjusted dryup, and capitulation composites.
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


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


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


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(arr):
        if len(arr) < 2:
            return np.nan
        xi = np.arange(len(arr), dtype=float)
        xi_m = xi.mean()
        x_m = arr.mean()
        num = ((xi - xi_m) * (arr - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): EWM-baseline dryup — smoothed reference variants ---

def vdry_ext_001_vol_ratio_5d_ema(volume: pd.Series) -> pd.Series:
    """Volume / 5-day EMA (ultra-short EWM baseline — intra-week dryup)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_WEEK))


def vdry_ext_002_vol_ratio_10d_ema(volume: pd.Series) -> pd.Series:
    """Volume / 10-day EMA (bi-weekly EWM baseline)."""
    return _safe_div(volume, _ewm_mean(volume, 10))


def vdry_ext_003_vol_ratio_126d_ema(volume: pd.Series) -> pd.Series:
    """Volume / 126-day EMA (half-year EWM baseline — new window vs. base)."""
    return _safe_div(volume, _ewm_mean(volume, _TD_HALF))


def vdry_ext_004_vol_ewm_zscore_21d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs. 21-day EWM mean and std."""
    m = _ewm_mean(volume, _TD_MON)
    s = _ewm_std(volume, _TD_MON)
    return _safe_div(volume - m, s)


def vdry_ext_005_vol_ewm_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs. 63-day EWM mean and std."""
    m = _ewm_mean(volume, _TD_QTR)
    s = _ewm_std(volume, _TD_QTR)
    return _safe_div(volume - m, s)


def vdry_ext_006_vol_ewm_zscore_126d(volume: pd.Series) -> pd.Series:
    """Z-score of volume vs. 126-day EWM mean and std."""
    m = _ewm_mean(volume, _TD_HALF)
    s = _ewm_std(volume, _TD_HALF)
    return _safe_div(volume - m, s)


def vdry_ext_007_vol_below_5d_ema_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 5-day EMA (very short-term dryup signal)."""
    return (volume < _ewm_mean(volume, _TD_WEEK)).astype(float)


def vdry_ext_008_vol_below_10d_ema_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 10-day EMA."""
    return (volume < _ewm_mean(volume, 10)).astype(float)


def vdry_ext_009_consec_below_5d_ema(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 5-day EMA."""
    return _consec_streak(volume < _ewm_mean(volume, _TD_WEEK))


def vdry_ext_010_consec_below_126d_ema(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 126-day EMA (long-horizon persistence)."""
    return _consec_streak(volume < _ewm_mean(volume, _TD_HALF))


# --- Group B (011-020): Quantile-threshold dryup — 10th, 5th, 1st percentile ---

def vdry_ext_011_vol_below_p05_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 5th percentile of 252-day distribution (extreme dryup)."""
    p05 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    return (volume < p05).astype(float)


def vdry_ext_012_vol_below_p10_63d_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 10th percentile of 63-day distribution."""
    p10 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    return (volume < p10).astype(float)


def vdry_ext_013_vol_below_p25_63d_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 25th percentile of 63-day distribution."""
    p25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return (volume < p25).astype(float)


def vdry_ext_014_vol_below_p05_126d_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 5th percentile of 126-day distribution."""
    p05 = volume.rolling(_TD_HALF, min_periods=_TD_QTR).quantile(0.05)
    return (volume < p05).astype(float)


def vdry_ext_015_count_below_p10_63d_in_21d(volume: pd.Series) -> pd.Series:
    """Count of last 21 days where volume < 10th percentile of 63-day dist."""
    p10 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.10)
    return _rolling_count_true(volume < p10, _TD_MON)


def vdry_ext_016_count_below_p05_252d_in_63d(volume: pd.Series) -> pd.Series:
    """Count of last 63 days where volume < 5th percentile of 252-day dist."""
    p05 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    return _rolling_count_true(volume < p05, _TD_QTR)


def vdry_ext_017_consec_below_p25_63d(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 25th percentile of 63-day dist."""
    p25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return _consec_streak(volume < p25)


def vdry_ext_018_consec_below_p10_252d(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 10th percentile of 252-day dist."""
    p10 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return _consec_streak(volume < p10)


def vdry_ext_019_vol_p10_pct_rank_21d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day rolling 10th-pctile vol within 252-day dist."""
    p10_21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.10)
    return p10_21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_ext_020_vol_depth_below_p25_252d(volume: pd.Series) -> pd.Series:
    """Depth of volume below 25th percentile of 252-day dist (0 when above)."""
    p25 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return (p25 - volume).clip(lower=0.0)


# --- Group C (021-030): Cross-window spread and regime duration ---

def vdry_ext_021_vol_5d_vs_63d_mean_spread(volume: pd.Series) -> pd.Series:
    """5-day mean minus 63-day mean volume (negative = short-term dryup below medium)."""
    return _rolling_mean(volume, _TD_WEEK) - _rolling_mean(volume, _TD_QTR)


def vdry_ext_022_vol_21d_vs_126d_mean_spread(volume: pd.Series) -> pd.Series:
    """21-day mean minus 126-day mean volume."""
    return _rolling_mean(volume, _TD_MON) - _rolling_mean(volume, _TD_HALF)


def vdry_ext_023_vol_63d_vs_252d_mean_spread(volume: pd.Series) -> pd.Series:
    """63-day mean minus 252-day mean volume."""
    return _rolling_mean(volume, _TD_QTR) - _rolling_mean(volume, _TD_YEAR)


def vdry_ext_024_vol_21d_vs_252d_log_ratio(volume: pd.Series) -> pd.Series:
    """Log(21d mean / 252d mean) — log-scale collapse indicator."""
    return _log_safe(_rolling_mean(volume, _TD_MON)) - _log_safe(_rolling_mean(volume, _TD_YEAR))


def vdry_ext_025_vol_5d_vs_252d_log_ratio(volume: pd.Series) -> pd.Series:
    """Log(5d mean / 252d mean) — acute vs. long baseline log-ratio."""
    return _log_safe(_rolling_mean(volume, _TD_WEEK)) - _log_safe(_rolling_mean(volume, _TD_YEAR))


def vdry_ext_026_vol_regime_below_mean_63d_frac_126d(volume: pd.Series) -> pd.Series:
    """Fraction of last 126 days where vol was below its concurrent 63d mean."""
    cond = volume < _rolling_mean(volume, _TD_QTR)
    return _rolling_count_true(cond, _TD_HALF) / _TD_HALF


def vdry_ext_027_vol_regime_below_mean_21d_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where vol was below its concurrent 21d mean."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vdry_ext_028_vol_regime_below_mean_252d_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where vol was below its concurrent 252d mean."""
    cond = volume < _rolling_mean(volume, _TD_YEAR)
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def vdry_ext_029_vol_max_consec_below_mean_21d_126d(volume: pd.Series) -> pd.Series:
    """Max consecutive-below-21d-mean streak within trailing 126 days."""
    cond = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_max_streak(cond, _TD_HALF)


def vdry_ext_030_vol_max_consec_below_ema_63d_252d(volume: pd.Series) -> pd.Series:
    """Max consecutive-below-63d-EMA streak within trailing 252 days."""
    cond = volume < _ewm_mean(volume, _TD_QTR)
    return _rolling_max_streak(cond, _TD_YEAR)


# --- Group D (031-040): Volatility-adjusted dryup measures ---

def vdry_ext_031_vol_ratio_21d_mean_adj_by_cv(volume: pd.Series) -> pd.Series:
    """(Vol / 21d mean) / (1 + CV_21d) — ratio penalized by intra-window variability."""
    m21 = _rolling_mean(volume, _TD_MON)
    s21 = _rolling_std(volume, _TD_MON)
    cv = _safe_div(s21, m21).fillna(0.0)
    ratio = _safe_div(volume, m21)
    return _safe_div(ratio, 1.0 + cv)


def vdry_ext_032_vol_zscore_21d_normalized_by_252d_std(volume: pd.Series) -> pd.Series:
    """21-day z-score re-scaled by the 252-day std of z-scores (regime-adjusted)."""
    m21 = _rolling_mean(volume, _TD_MON)
    s21 = _rolling_std(volume, _TD_MON)
    z21 = _safe_div(volume - m21, s21)
    s_z = _rolling_std(z21, _TD_YEAR)
    return _safe_div(z21, s_z)


def vdry_ext_033_vol_dryup_volatility_ratio_21d(volume: pd.Series) -> pd.Series:
    """Std of volume / mean of volume over 21 days — low value = dryup with stability."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))


def vdry_ext_034_vol_dryup_volatility_ratio_63d(volume: pd.Series) -> pd.Series:
    """Std of volume / mean of volume over 63 days."""
    return _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))


def vdry_ext_035_vol_zscore_below_neg2_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day z-score < -2 (severe dryup relative to recent baseline)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    return (z < -2.0).astype(float)


def vdry_ext_036_vol_zscore_below_neg2_flag_63d(volume: pd.Series) -> pd.Series:
    """Flag: 63-day z-score < -2."""
    m = _rolling_mean(volume, _TD_QTR)
    s = _rolling_std(volume, _TD_QTR)
    z = _safe_div(volume - m, s)
    return (z < -2.0).astype(float)


def vdry_ext_037_count_zscore_below_neg1_21d_in_63d(volume: pd.Series) -> pd.Series:
    """Count of days in last 63d where 21d z-score < -1 (moderate dryup breadth)."""
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    return _rolling_count_true(z < -1.0, _TD_QTR)


def vdry_ext_038_vol_ewm_zscore_21d_below_neg1_flag(volume: pd.Series) -> pd.Series:
    """Flag: EWM-21d z-score < -1 (soft dryup via exponential smoothing)."""
    m = _ewm_mean(volume, _TD_MON)
    s = _ewm_std(volume, _TD_MON)
    z = _safe_div(volume - m, s)
    return (z < -1.0).astype(float)


def vdry_ext_039_vol_21d_range_contraction_ratio(volume: pd.Series) -> pd.Series:
    """(21d max - 21d min) / 21d max — how compressed the volume range is."""
    mx = _rolling_max(volume, _TD_MON)
    mn = _rolling_min(volume, _TD_MON)
    return _safe_div(mx - mn, mx)


def vdry_ext_040_vol_63d_range_contraction_ratio(volume: pd.Series) -> pd.Series:
    """(63d max - 63d min) / 63d max — range compression over quarter."""
    mx = _rolling_max(volume, _TD_QTR)
    mn = _rolling_min(volume, _TD_QTR)
    return _safe_div(mx - mn, mx)


# --- Group E (041-050): Price-volume interaction — open/high context ---

def vdry_ext_041_low_vol_on_gap_down_21d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 21 days: gap-down open (open < prior close) AND low volume."""
    mean21 = _rolling_mean(volume, _TD_MON)
    gap_down = open < close.shift(1)
    low_vol = volume < mean21
    return _rolling_count_true(gap_down & low_vol, _TD_MON)


def vdry_ext_042_low_vol_on_gap_down_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 63 days: gap-down open AND volume < 63d mean."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    gap_down = open < close.shift(1)
    low_vol = volume < mean63
    return _rolling_count_true(gap_down & low_vol, _TD_QTR)


def vdry_ext_043_low_vol_near_52wk_low_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of days: close within 3% of 252d low AND volume < 21d mean."""
    min252 = _rolling_min(close, _TD_YEAR)
    near_low = close <= 1.03 * min252
    low_vol = volume < _rolling_mean(volume, _TD_MON)
    return _consec_streak(near_low & low_vol)


def vdry_ext_044_low_vol_near_52wk_low_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 63 days: close within 5% of 252d low AND vol < 21d mean."""
    min252 = _rolling_min(close, _TD_YEAR)
    near_low = close <= 1.05 * min252
    low_vol = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_count_true(near_low & low_vol, _TD_QTR)


def vdry_ext_045_vol_at_high_close_pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on days close >= 75th-pctile of 21d close / overall 21d avg vol."""
    p75 = close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.75)
    at_high = close >= p75
    high_vol = volume.where(at_high, np.nan).rolling(_TD_MON, min_periods=1).mean()
    avg_vol = _rolling_mean(volume, _TD_MON)
    return _safe_div(high_vol, avg_vol)


def vdry_ext_046_vol_on_inside_day_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of inside days (high < prev high, low > prev low) with low vol in 21d."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    low_vol = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_count_true(inside & low_vol, _TD_MON)


def vdry_ext_047_vol_on_outside_day_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of outside days (high > prev high, low < prev low) in 21d regardless of vol."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return _rolling_count_true(outside, _TD_MON).astype(float)


def vdry_ext_048_low_vol_high_close_divergence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 21d: close above 21d mean BUT volume below 21d mean (price/vol divergence)."""
    mean_c = _rolling_mean(close, _TD_MON)
    mean_v = _rolling_mean(volume, _TD_MON)
    cond = (close > mean_c) & (volume < mean_v)
    return _rolling_count_true(cond, _TD_MON)


def vdry_ext_049_high_price_low_vol_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days: close in upper 50th pctile AND vol in lower 50th pctile."""
    med_c = _rolling_median(close, _TD_QTR)
    med_v = _rolling_median(volume, _TD_QTR)
    cond = (close >= med_c) & (volume < med_v)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def vdry_ext_050_open_vol_ratio_21d(open: pd.Series, volume: pd.Series) -> pd.Series:
    """Open-price * volume / 21d mean of open*volume (dollar-at-open dryup)."""
    ov = open * volume
    return _safe_div(ov, _rolling_mean(ov, _TD_MON))


# --- Group F (051-060): Log-smoothed dryup — new window/smoothing combos ---

def vdry_ext_051_log_vol_5d_ema_vs_63d_mean(volume: pd.Series) -> pd.Series:
    """Log(5d EMA of vol) - log(63d mean of vol)."""
    return _log_safe(_ewm_mean(volume, _TD_WEEK)) - _log_safe(_rolling_mean(volume, _TD_QTR))


def vdry_ext_052_log_vol_21d_mean_vs_126d_mean(volume: pd.Series) -> pd.Series:
    """Log(21d mean / 126d mean) — log-scale medium vs. long baseline."""
    return _log_safe(_rolling_mean(volume, _TD_MON)) - _log_safe(_rolling_mean(volume, _TD_HALF))


def vdry_ext_053_log_vol_ema5_vs_ema63(volume: pd.Series) -> pd.Series:
    """Log(5d EMA) - log(63d EMA) — pure EWM log spread."""
    return _log_safe(_ewm_mean(volume, _TD_WEEK)) - _log_safe(_ewm_mean(volume, _TD_QTR))


def vdry_ext_054_log_vol_ema21_vs_ema252(volume: pd.Series) -> pd.Series:
    """Log(21d EMA) - log(252d EMA) — monthly vs. annual EWM log spread."""
    return _log_safe(_ewm_mean(volume, _TD_MON)) - _log_safe(_ewm_mean(volume, _TD_YEAR))


def vdry_ext_055_vol_log_ratio_5d_max(volume: pd.Series) -> pd.Series:
    """Log(volume / 5d trailing max) — how far below the weekly peak."""
    return _log_safe(volume) - _log_safe(_rolling_max(volume.shift(1), _TD_WEEK))


def vdry_ext_056_vol_log_ratio_126d_mean(volume: pd.Series) -> pd.Series:
    """Log(volume / 126d mean) — half-year log baseline (new vs. base)."""
    return _log_safe(volume) - _log_safe(_rolling_mean(volume, _TD_HALF))


def vdry_ext_057_vol_log_zscore_21d(volume: pd.Series) -> pd.Series:
    """Z-score of log-volume relative to 21d log-volume mean and std."""
    lv = _log_safe(volume)
    m = _rolling_mean(lv, _TD_MON)
    s = _rolling_std(lv, _TD_MON)
    return _safe_div(lv - m, s)


def vdry_ext_058_vol_log_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of log-volume relative to 252d log-volume mean and std."""
    lv = _log_safe(volume)
    m = _rolling_mean(lv, _TD_YEAR)
    s = _rolling_std(lv, _TD_YEAR)
    return _safe_div(lv - m, s)


def vdry_ext_059_vol_log_ratio_5d_ema(volume: pd.Series) -> pd.Series:
    """Log(volume / 5d EMA) — deviation from ultra-short EWM baseline."""
    return _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_WEEK))


def vdry_ext_060_vol_log_ratio_252d_ema(volume: pd.Series) -> pd.Series:
    """Log(volume / 252d EMA) — deviation from annual EWM baseline."""
    return _log_safe(volume) - _log_safe(_ewm_mean(volume, _TD_YEAR))


# --- Group G (061-068): Dryup intensity — new threshold / window combos ---

def vdry_ext_061_vol_dryup_intensity_5d(volume: pd.Series) -> pd.Series:
    """Sum of max(0, 1 - vol/21d mean) over trailing 5 days (weekly shortfall)."""
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_WEEK)


def vdry_ext_062_vol_dryup_intensity_126d(volume: pd.Series) -> pd.Series:
    """Sum of max(0, 1 - vol/63d mean) over trailing 126 days."""
    m63 = _rolling_mean(volume, _TD_QTR)
    shortfall = (1.0 - _safe_div(volume, m63)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_HALF)


def vdry_ext_063_vol_dryup_intensity_vs_252d_ema(volume: pd.Series) -> pd.Series:
    """Sum of max(0, 1 - vol/252d EMA) over trailing 63 days."""
    m_ema = _ewm_mean(volume, _TD_YEAR)
    shortfall = (1.0 - _safe_div(volume, m_ema)).clip(lower=0.0)
    return _rolling_sum(shortfall, _TD_QTR)


def vdry_ext_064_vol_dryup_depth_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of vol/21d-mean ratio within trailing 252-day distribution."""
    ratio = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vdry_ext_065_vol_below_half_ema21_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 50% of 21-day EMA (severe EWM dryup)."""
    return (volume < 0.5 * _ewm_mean(volume, _TD_MON)).astype(float)


def vdry_ext_066_vol_below_half_ema63_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume < 50% of 63-day EMA."""
    return (volume < 0.5 * _ewm_mean(volume, _TD_QTR)).astype(float)


def vdry_ext_067_consec_below_half_mean_63d(volume: pd.Series) -> pd.Series:
    """Streak of days volume < 50% of 63-day rolling mean."""
    return _consec_streak(volume < 0.5 * _rolling_mean(volume, _TD_QTR))


def vdry_ext_068_vol_dryup_iqr_score_63d(volume: pd.Series) -> pd.Series:
    """(Q25_63d - volume) / IQR_63d clipped to 0 — robust quantile shortfall."""
    q25 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    q75 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    iqr = (q75 - q25).replace(0, np.nan)
    return _safe_div((q25 - volume).clip(lower=0.0), iqr)


# --- Group H (069-075): Capitulation composite dryup indices ---

def vdry_ext_069_vol_dryup_multi_window_composite(volume: pd.Series) -> pd.Series:
    """Average of vol/mean ratios across 5d, 21d, 63d, 126d, 252d windows."""
    r1 = _safe_div(volume, _rolling_mean(volume, _TD_WEEK))
    r2 = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    r3 = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    r4 = _safe_div(volume, _rolling_mean(volume, _TD_HALF))
    r5 = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return (r1 + r2 + r3 + r4 + r5) / 5.0


def vdry_ext_070_vol_dryup_pct_rank_composite(volume: pd.Series) -> pd.Series:
    """Average of vol percentile ranks at 21d, 63d, 126d, 252d windows."""
    p1 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    p2 = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    p3 = volume.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)
    p4 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (p1 + p2 + p3 + p4) / 4.0


def vdry_ext_071_vol_dryup_zscore_ema_composite(volume: pd.Series) -> pd.Series:
    """Average of EWM z-scores at 21d, 63d, 252d spans."""
    z1 = _safe_div(volume - _ewm_mean(volume, _TD_MON), _ewm_std(volume, _TD_MON))
    z2 = _safe_div(volume - _ewm_mean(volume, _TD_QTR), _ewm_std(volume, _TD_QTR))
    z3 = _safe_div(volume - _ewm_mean(volume, _TD_YEAR), _ewm_std(volume, _TD_YEAR))
    return (z1 + z2 + z3) / 3.0


def vdry_ext_072_vol_dryup_flag_all4_below_mean(volume: pd.Series) -> pd.Series:
    """Flag: volume simultaneously below 5d, 21d, 63d, and 252d means (full-spectrum dryup)."""
    b1 = volume < _rolling_mean(volume, _TD_WEEK)
    b2 = volume < _rolling_mean(volume, _TD_MON)
    b3 = volume < _rolling_mean(volume, _TD_QTR)
    b4 = volume < _rolling_mean(volume, _TD_YEAR)
    return (b1 & b2 & b3 & b4).astype(float)


def vdry_ext_073_vol_dryup_seller_exhaustion_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day seller exhaustion: sum of (low_vol_down * vol shortfall depth)."""
    mean63 = _rolling_mean(volume, _TD_QTR)
    ret = close.pct_change(1)
    low_vol_down = ((ret < 0) & (volume < mean63)).astype(float)
    depth = (1.0 - _safe_div(volume, mean63)).clip(lower=0.0)
    return _rolling_sum(low_vol_down * depth, _TD_QTR)


def vdry_ext_074_vol_dryup_capitulation_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation score: pct_rank_dryup_252d + (1 - vol/21d_mean).clip(0) * (near_52wk_low).
    Combines quantile rank, vol shortfall, and price proximity to 52-week low."""
    pct_rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.5)
    m21 = _rolling_mean(volume, _TD_MON)
    shortfall = (1.0 - _safe_div(volume, m21)).clip(lower=0.0)
    min252 = _rolling_min(close, _TD_YEAR)
    near_low = (1.0 - _safe_div(close, min252.replace(0, np.nan))).clip(lower=0.0, upper=1.0)
    return (1.0 - pct_rank) + shortfall + near_low


def vdry_ext_075_vol_dryup_expanding_pct_rank(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of today's volume (absolute rarity)."""
    return volume.expanding(min_periods=1).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DRYUP_EXTENDED_REGISTRY_001_075 = {
    "vdry_ext_001_vol_ratio_5d_ema": {"inputs": ["volume"], "func": vdry_ext_001_vol_ratio_5d_ema},
    "vdry_ext_002_vol_ratio_10d_ema": {"inputs": ["volume"], "func": vdry_ext_002_vol_ratio_10d_ema},
    "vdry_ext_003_vol_ratio_126d_ema": {"inputs": ["volume"], "func": vdry_ext_003_vol_ratio_126d_ema},
    "vdry_ext_004_vol_ewm_zscore_21d": {"inputs": ["volume"], "func": vdry_ext_004_vol_ewm_zscore_21d},
    "vdry_ext_005_vol_ewm_zscore_63d": {"inputs": ["volume"], "func": vdry_ext_005_vol_ewm_zscore_63d},
    "vdry_ext_006_vol_ewm_zscore_126d": {"inputs": ["volume"], "func": vdry_ext_006_vol_ewm_zscore_126d},
    "vdry_ext_007_vol_below_5d_ema_flag": {"inputs": ["volume"], "func": vdry_ext_007_vol_below_5d_ema_flag},
    "vdry_ext_008_vol_below_10d_ema_flag": {"inputs": ["volume"], "func": vdry_ext_008_vol_below_10d_ema_flag},
    "vdry_ext_009_consec_below_5d_ema": {"inputs": ["volume"], "func": vdry_ext_009_consec_below_5d_ema},
    "vdry_ext_010_consec_below_126d_ema": {"inputs": ["volume"], "func": vdry_ext_010_consec_below_126d_ema},
    "vdry_ext_011_vol_below_p05_252d_flag": {"inputs": ["volume"], "func": vdry_ext_011_vol_below_p05_252d_flag},
    "vdry_ext_012_vol_below_p10_63d_flag": {"inputs": ["volume"], "func": vdry_ext_012_vol_below_p10_63d_flag},
    "vdry_ext_013_vol_below_p25_63d_flag": {"inputs": ["volume"], "func": vdry_ext_013_vol_below_p25_63d_flag},
    "vdry_ext_014_vol_below_p05_126d_flag": {"inputs": ["volume"], "func": vdry_ext_014_vol_below_p05_126d_flag},
    "vdry_ext_015_count_below_p10_63d_in_21d": {"inputs": ["volume"], "func": vdry_ext_015_count_below_p10_63d_in_21d},
    "vdry_ext_016_count_below_p05_252d_in_63d": {"inputs": ["volume"], "func": vdry_ext_016_count_below_p05_252d_in_63d},
    "vdry_ext_017_consec_below_p25_63d": {"inputs": ["volume"], "func": vdry_ext_017_consec_below_p25_63d},
    "vdry_ext_018_consec_below_p10_252d": {"inputs": ["volume"], "func": vdry_ext_018_consec_below_p10_252d},
    "vdry_ext_019_vol_p10_pct_rank_21d": {"inputs": ["volume"], "func": vdry_ext_019_vol_p10_pct_rank_21d},
    "vdry_ext_020_vol_depth_below_p25_252d": {"inputs": ["volume"], "func": vdry_ext_020_vol_depth_below_p25_252d},
    "vdry_ext_021_vol_5d_vs_63d_mean_spread": {"inputs": ["volume"], "func": vdry_ext_021_vol_5d_vs_63d_mean_spread},
    "vdry_ext_022_vol_21d_vs_126d_mean_spread": {"inputs": ["volume"], "func": vdry_ext_022_vol_21d_vs_126d_mean_spread},
    "vdry_ext_023_vol_63d_vs_252d_mean_spread": {"inputs": ["volume"], "func": vdry_ext_023_vol_63d_vs_252d_mean_spread},
    "vdry_ext_024_vol_21d_vs_252d_log_ratio": {"inputs": ["volume"], "func": vdry_ext_024_vol_21d_vs_252d_log_ratio},
    "vdry_ext_025_vol_5d_vs_252d_log_ratio": {"inputs": ["volume"], "func": vdry_ext_025_vol_5d_vs_252d_log_ratio},
    "vdry_ext_026_vol_regime_below_mean_63d_frac_126d": {"inputs": ["volume"], "func": vdry_ext_026_vol_regime_below_mean_63d_frac_126d},
    "vdry_ext_027_vol_regime_below_mean_21d_frac_252d": {"inputs": ["volume"], "func": vdry_ext_027_vol_regime_below_mean_21d_frac_252d},
    "vdry_ext_028_vol_regime_below_mean_252d_frac_252d": {"inputs": ["volume"], "func": vdry_ext_028_vol_regime_below_mean_252d_frac_252d},
    "vdry_ext_029_vol_max_consec_below_mean_21d_126d": {"inputs": ["volume"], "func": vdry_ext_029_vol_max_consec_below_mean_21d_126d},
    "vdry_ext_030_vol_max_consec_below_ema_63d_252d": {"inputs": ["volume"], "func": vdry_ext_030_vol_max_consec_below_ema_63d_252d},
    "vdry_ext_031_vol_ratio_21d_mean_adj_by_cv": {"inputs": ["volume"], "func": vdry_ext_031_vol_ratio_21d_mean_adj_by_cv},
    "vdry_ext_032_vol_zscore_21d_normalized_by_252d_std": {"inputs": ["volume"], "func": vdry_ext_032_vol_zscore_21d_normalized_by_252d_std},
    "vdry_ext_033_vol_dryup_volatility_ratio_21d": {"inputs": ["volume"], "func": vdry_ext_033_vol_dryup_volatility_ratio_21d},
    "vdry_ext_034_vol_dryup_volatility_ratio_63d": {"inputs": ["volume"], "func": vdry_ext_034_vol_dryup_volatility_ratio_63d},
    "vdry_ext_035_vol_zscore_below_neg2_flag_21d": {"inputs": ["volume"], "func": vdry_ext_035_vol_zscore_below_neg2_flag_21d},
    "vdry_ext_036_vol_zscore_below_neg2_flag_63d": {"inputs": ["volume"], "func": vdry_ext_036_vol_zscore_below_neg2_flag_63d},
    "vdry_ext_037_count_zscore_below_neg1_21d_in_63d": {"inputs": ["volume"], "func": vdry_ext_037_count_zscore_below_neg1_21d_in_63d},
    "vdry_ext_038_vol_ewm_zscore_21d_below_neg1_flag": {"inputs": ["volume"], "func": vdry_ext_038_vol_ewm_zscore_21d_below_neg1_flag},
    "vdry_ext_039_vol_21d_range_contraction_ratio": {"inputs": ["volume"], "func": vdry_ext_039_vol_21d_range_contraction_ratio},
    "vdry_ext_040_vol_63d_range_contraction_ratio": {"inputs": ["volume"], "func": vdry_ext_040_vol_63d_range_contraction_ratio},
    "vdry_ext_041_low_vol_on_gap_down_21d": {"inputs": ["open", "close", "volume"], "func": vdry_ext_041_low_vol_on_gap_down_21d},
    "vdry_ext_042_low_vol_on_gap_down_63d": {"inputs": ["open", "close", "volume"], "func": vdry_ext_042_low_vol_on_gap_down_63d},
    "vdry_ext_043_low_vol_near_52wk_low_streak": {"inputs": ["close", "volume"], "func": vdry_ext_043_low_vol_near_52wk_low_streak},
    "vdry_ext_044_low_vol_near_52wk_low_count_63d": {"inputs": ["close", "volume"], "func": vdry_ext_044_low_vol_near_52wk_low_count_63d},
    "vdry_ext_045_vol_at_high_close_pct_21d": {"inputs": ["close", "volume"], "func": vdry_ext_045_vol_at_high_close_pct_21d},
    "vdry_ext_046_vol_on_inside_day_21d": {"inputs": ["high", "low", "volume"], "func": vdry_ext_046_vol_on_inside_day_21d},
    "vdry_ext_047_vol_on_outside_day_21d": {"inputs": ["high", "low", "volume"], "func": vdry_ext_047_vol_on_outside_day_21d},
    "vdry_ext_048_low_vol_high_close_divergence_21d": {"inputs": ["close", "volume"], "func": vdry_ext_048_low_vol_high_close_divergence_21d},
    "vdry_ext_049_high_price_low_vol_frac_63d": {"inputs": ["close", "volume"], "func": vdry_ext_049_high_price_low_vol_frac_63d},
    "vdry_ext_050_open_vol_ratio_21d": {"inputs": ["open", "volume"], "func": vdry_ext_050_open_vol_ratio_21d},
    "vdry_ext_051_log_vol_5d_ema_vs_63d_mean": {"inputs": ["volume"], "func": vdry_ext_051_log_vol_5d_ema_vs_63d_mean},
    "vdry_ext_052_log_vol_21d_mean_vs_126d_mean": {"inputs": ["volume"], "func": vdry_ext_052_log_vol_21d_mean_vs_126d_mean},
    "vdry_ext_053_log_vol_ema5_vs_ema63": {"inputs": ["volume"], "func": vdry_ext_053_log_vol_ema5_vs_ema63},
    "vdry_ext_054_log_vol_ema21_vs_ema252": {"inputs": ["volume"], "func": vdry_ext_054_log_vol_ema21_vs_ema252},
    "vdry_ext_055_vol_log_ratio_5d_max": {"inputs": ["volume"], "func": vdry_ext_055_vol_log_ratio_5d_max},
    "vdry_ext_056_vol_log_ratio_126d_mean": {"inputs": ["volume"], "func": vdry_ext_056_vol_log_ratio_126d_mean},
    "vdry_ext_057_vol_log_zscore_21d": {"inputs": ["volume"], "func": vdry_ext_057_vol_log_zscore_21d},
    "vdry_ext_058_vol_log_zscore_252d": {"inputs": ["volume"], "func": vdry_ext_058_vol_log_zscore_252d},
    "vdry_ext_059_vol_log_ratio_5d_ema": {"inputs": ["volume"], "func": vdry_ext_059_vol_log_ratio_5d_ema},
    "vdry_ext_060_vol_log_ratio_252d_ema": {"inputs": ["volume"], "func": vdry_ext_060_vol_log_ratio_252d_ema},
    "vdry_ext_061_vol_dryup_intensity_5d": {"inputs": ["volume"], "func": vdry_ext_061_vol_dryup_intensity_5d},
    "vdry_ext_062_vol_dryup_intensity_126d": {"inputs": ["volume"], "func": vdry_ext_062_vol_dryup_intensity_126d},
    "vdry_ext_063_vol_dryup_intensity_vs_252d_ema": {"inputs": ["volume"], "func": vdry_ext_063_vol_dryup_intensity_vs_252d_ema},
    "vdry_ext_064_vol_dryup_depth_pct_rank_252d": {"inputs": ["volume"], "func": vdry_ext_064_vol_dryup_depth_pct_rank_252d},
    "vdry_ext_065_vol_below_half_ema21_flag": {"inputs": ["volume"], "func": vdry_ext_065_vol_below_half_ema21_flag},
    "vdry_ext_066_vol_below_half_ema63_flag": {"inputs": ["volume"], "func": vdry_ext_066_vol_below_half_ema63_flag},
    "vdry_ext_067_consec_below_half_mean_63d": {"inputs": ["volume"], "func": vdry_ext_067_consec_below_half_mean_63d},
    "vdry_ext_068_vol_dryup_iqr_score_63d": {"inputs": ["volume"], "func": vdry_ext_068_vol_dryup_iqr_score_63d},
    "vdry_ext_069_vol_dryup_multi_window_composite": {"inputs": ["volume"], "func": vdry_ext_069_vol_dryup_multi_window_composite},
    "vdry_ext_070_vol_dryup_pct_rank_composite": {"inputs": ["volume"], "func": vdry_ext_070_vol_dryup_pct_rank_composite},
    "vdry_ext_071_vol_dryup_zscore_ema_composite": {"inputs": ["volume"], "func": vdry_ext_071_vol_dryup_zscore_ema_composite},
    "vdry_ext_072_vol_dryup_flag_all4_below_mean": {"inputs": ["volume"], "func": vdry_ext_072_vol_dryup_flag_all4_below_mean},
    "vdry_ext_073_vol_dryup_seller_exhaustion_63d": {"inputs": ["close", "volume"], "func": vdry_ext_073_vol_dryup_seller_exhaustion_63d},
    "vdry_ext_074_vol_dryup_capitulation_score": {"inputs": ["close", "volume"], "func": vdry_ext_074_vol_dryup_capitulation_score},
    "vdry_ext_075_vol_dryup_expanding_pct_rank": {"inputs": ["volume"], "func": vdry_ext_075_vol_dryup_expanding_pct_rank},
}
