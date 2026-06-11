"""
23_dollar_volume_shock — Base Features 001-075
Domain: dollar-volume spikes and turnover extremes — dollar volume shock
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
Dollar volume = close * volume (price-weighted traded value).
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
    """Rolling maximum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling minimum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling standard deviation over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    """Rolling median over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponentially weighted mean with given span."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Natural log with floor at EPS to avoid -inf."""
    return np.log(s.clip(lower=_EPS))


def _dv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume: close * volume."""
    return close * volume


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Dollar-volume ratio vs trailing baseline ---

def dvs_001_dv_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 21-day trailing mean (immediate spike)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_MON))


def dvs_002_dv_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 63-day trailing mean (quarterly baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_QTR))


def dvs_003_dv_ratio_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 126-day trailing mean (half-year baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_HALF))


def dvs_004_dv_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 252-day trailing mean (annual baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_YEAR))


def dvs_005_dv_log_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of dollar volume divided by 21-day mean (log-scale spike)."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_MON))


def dvs_006_dv_log_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of dollar volume divided by 63-day mean (log-scale quarterly)."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_QTR))


def dvs_007_dv_log_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of dollar volume divided by 252-day mean (log-scale annual)."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_YEAR))


def dvs_008_dv_ratio_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 21-day EWM mean (exponential baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _ewm_mean(dv, _TD_MON))


def dvs_009_dv_ratio_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 63-day EWM mean (exponential quarterly)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _ewm_mean(dv, _TD_QTR))


def dvs_010_dv_ratio_median_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 63-day rolling median (robust baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_median(dv, _TD_QTR))


# --- Group B (011-020): Dollar-volume z-scores ---

def dvs_011_dv_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume vs 21-day rolling distribution."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    return _safe_div(dv - m, s)


def dvs_012_dv_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume vs 63-day rolling distribution."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    return _safe_div(dv - m, s)


def dvs_013_dv_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume vs 126-day rolling distribution."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_HALF)
    s = _rolling_std(dv, _TD_HALF)
    return _safe_div(dv - m, s)


def dvs_014_dv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume vs 252-day rolling distribution."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    return _safe_div(dv - m, s)


def dvs_015_dv_log_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log-dollar-volume vs 63-day rolling log distribution."""
    dv = _log_safe(_dv(close, volume))
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    return _safe_div(dv - m, s)


def dvs_016_dv_log_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log-dollar-volume vs 252-day rolling log distribution."""
    dv = _log_safe(_dv(close, volume))
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    return _safe_div(dv - m, s)


def dvs_017_dv_zscore_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding-window z-score of dollar volume (all-history extremity)."""
    dv = _dv(close, volume)
    m = dv.expanding(min_periods=5).mean()
    s = dv.expanding(min_periods=5).std()
    return _safe_div(dv - m, s)


def dvs_018_dv_zscore_21d_on_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day z-score of dollar volume, zeroed on up-price days (down-day shock)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    return z.where(ret < 0, 0.0)


def dvs_019_dv_mad_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Robust z-score: (dv - median) / rolling MAD over 63 days."""
    dv = _dv(close, volume)
    med = _rolling_median(dv, _TD_QTR)
    mad = (dv - med).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    return _safe_div(dv - med, mad)


def dvs_020_dv_mad_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Robust z-score: (dv - median) / rolling MAD over 252 days."""
    dv = _dv(close, volume)
    med = _rolling_median(dv, _TD_YEAR)
    mad = (dv - med).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).median()
    return _safe_div(dv - med, mad)


# --- Group C (021-030): Dollar-volume spike counts ---

def dvs_021_dv_spike_count_2x_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where dollar volume > 2x its 63d mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_MON)


def dvs_022_dv_spike_count_2x_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where dollar volume > 2x its 63d mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def dvs_023_dv_spike_count_3x_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where dollar volume > 3x its 63d mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 3.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def dvs_024_dv_spike_count_2x_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-spike days in trailing 252d."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_YEAR)


def dvs_025_dv_spike_count_zscore2_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days where 63d dollar-volume z-score > 2.0 in trailing 21d."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    spike = (z > 2.0).astype(float)
    return _rolling_sum(spike, _TD_MON)


def dvs_026_dv_spike_count_zscore2_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days where 63d dollar-volume z-score > 2.0 in trailing 63d."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    spike = (z > 2.0).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def dvs_027_dv_spike_count_zscore3_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days where 252d dollar-volume z-score > 3.0 in trailing 252d."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    spike = (z > 3.0).astype(float)
    return _rolling_sum(spike, _TD_YEAR)


def dvs_028_dv_spike_on_down_day_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 21d with 2x-dv spike AND price decline."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((dv > 2.0 * baseline) & (ret < 0)).astype(float)
    return _rolling_sum(spike_dn, _TD_MON)


def dvs_029_dv_spike_on_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 63d with 2x-dv spike AND price decline (capitulation events)."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((dv > 2.0 * baseline) & (ret < 0)).astype(float)
    return _rolling_sum(spike_dn, _TD_QTR)


def dvs_030_dv_spike_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were 2x dollar-volume spikes."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_MON) / _TD_MON


# --- Group D (031-040): Largest dollar-volume day statistics ---

def dvs_031_dv_max_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum dollar volume observed in trailing 21 days."""
    dv = _dv(close, volume)
    return _rolling_max(dv, _TD_MON)


def dvs_032_dv_max_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum dollar volume observed in trailing 63 days."""
    dv = _dv(close, volume)
    return _rolling_max(dv, _TD_QTR)


def dvs_033_dv_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum dollar volume observed in trailing 252 days."""
    dv = _dv(close, volume)
    return _rolling_max(dv, _TD_YEAR)


def dvs_034_dv_current_vs_max_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar volume as fraction of 63-day maximum."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_max(dv, _TD_QTR))


def dvs_035_dv_current_vs_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar volume as fraction of 252-day maximum."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_max(dv, _TD_YEAR))


def dvs_036_dv_max_21d_vs_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day max dollar volume divided by 252-day mean (recent peak vs long avg)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_max(dv, _TD_MON), _rolling_mean(dv, _TD_YEAR))


def dvs_037_dv_max_63d_vs_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day max dollar volume divided by 252-day mean."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_max(dv, _TD_QTR), _rolling_mean(dv, _TD_YEAR))


def dvs_038_dv_max_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """All-time expanding maximum dollar volume (is today a record day?)."""
    dv = _dv(close, volume)
    return dv.expanding(min_periods=1).max()


def dvs_039_dv_current_vs_expanding_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current dollar volume as fraction of all-time expanding maximum."""
    dv = _dv(close, volume)
    return _safe_div(dv, dv.expanding(min_periods=1).max())


def dvs_040_dv_max_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day max dollar volume within trailing 252-day distribution."""
    dv = _dv(close, volume)
    mx21 = _rolling_max(dv, _TD_MON)
    return mx21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): Dollar-volume vs price interaction ---

def dvs_041_dv_price_collapse_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 2x dollar-volume spike on a day with >5% price decline (panic sell)."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    return ((dv > 2.0 * baseline) & (ret < -0.05)).astype(float)


def dvs_042_dv_on_down_days_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on down-price days over trailing 21 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, 0.0)
    return _rolling_sum(dv_dn, _TD_MON)


def dvs_043_dv_on_down_days_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on down-price days over trailing 63 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, 0.0)
    return _rolling_sum(dv_dn, _TD_QTR)


def dvs_044_dv_down_vs_up_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average dollar volume on down days to up days over 21 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(dv_dn, dv_up)


def dvs_045_dv_down_vs_up_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average dollar volume on down days to up days over 63 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(dv_dn, dv_up)


def dvs_046_dv_down_vs_up_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of average dollar volume on down days to up days over 252 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    dv_up = dv.where(ret > 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(dv_dn, dv_up)


def dvs_047_dv_price_ret_product_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (dollar_volume * daily_return) over 21 days (signed dollar pressure)."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    signed = dv * ret
    return _rolling_sum(signed, _TD_MON)


def dvs_048_dv_price_ret_product_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (dollar_volume * daily_return) over 63 days (signed dollar pressure)."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    signed = dv * ret
    return _rolling_sum(signed, _TD_QTR)


def dvs_049_dv_weighted_negative_return_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted average of negative daily returns over 21 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    neg_ret = ret.where(ret < 0, 0.0)
    weighted = dv * neg_ret
    return _safe_div(_rolling_sum(weighted, _TD_MON), _rolling_sum(dv, _TD_MON))


def dvs_050_dv_weighted_negative_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted average of negative daily returns over 63 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    neg_ret = ret.where(ret < 0, 0.0)
    weighted = dv * neg_ret
    return _safe_div(_rolling_sum(weighted, _TD_QTR), _rolling_sum(dv, _TD_QTR))


# --- Group F (051-060): Turnover-value extremes and percentile ranks ---

def dvs_051_dv_pct_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current dollar volume within trailing 21-day window."""
    dv = _dv(close, volume)
    return dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def dvs_052_dv_pct_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current dollar volume within trailing 63-day window."""
    dv = _dv(close, volume)
    return dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def dvs_053_dv_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current dollar volume within trailing 252-day window."""
    dv = _dv(close, volume)
    return dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dvs_054_dv_pct_rank_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of current dollar volume (all-history rank)."""
    dv = _dv(close, volume)
    return dv.expanding(min_periods=5).rank(pct=True)


def dvs_055_dv_top_decile_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current dollar volume is in the top 10% of the trailing 252-day range."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (rank >= 0.90).astype(float)


def dvs_056_dv_top_quintile_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current dollar volume is in the top 20% of the trailing 63-day range."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank >= 0.80).astype(float)


def dvs_057_dv_sum_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day total dollar volume within trailing 252-day distribution."""
    dv = _dv(close, volume)
    sum21 = _rolling_sum(dv, _TD_MON)
    return sum21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dvs_058_dv_sum_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day total dollar volume within trailing 252-day distribution."""
    dv = _dv(close, volume)
    sum63 = _rolling_sum(dv, _TD_QTR)
    return sum63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dvs_059_dv_high_rank_on_down_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 21d where dv rank > 80th pctile AND price declined."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    ret = close.pct_change(1)
    cond = ((rank >= 0.80) & (ret < 0)).astype(float)
    return _rolling_sum(cond, _TD_MON)


def dvs_060_dv_high_rank_on_down_day_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 63d where dv rank > 80th pctile AND price declined."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    ret = close.pct_change(1)
    cond = ((rank >= 0.80) & (ret < 0)).astype(float)
    return _rolling_sum(cond, _TD_QTR)


# --- Group G (061-075): Dollar-volume vs price-level interactions ---

def dvs_061_dv_at_52wk_low_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 2x dollar-volume spike on same day as a new 252-day low close."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = close < roll_min
    return ((dv > 2.0 * baseline) & new_low).astype(float)


def dvs_062_dv_cumsum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day cumulative dollar volume (total traded value)."""
    dv = _dv(close, volume)
    return _rolling_sum(dv, _TD_MON)


def dvs_063_dv_cumsum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day cumulative dollar volume."""
    dv = _dv(close, volume)
    return _rolling_sum(dv, _TD_QTR)


def dvs_064_dv_cumsum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252-day cumulative dollar volume."""
    dv = _dv(close, volume)
    return _rolling_sum(dv, _TD_YEAR)


def dvs_065_dv_sum_21d_vs_sum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day cumulative DV to 252-day cumulative DV (recency concentration)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(dv, _TD_YEAR))


def dvs_066_dv_sum_63d_vs_sum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day cumulative DV to 252-day cumulative DV."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_sum(dv, _TD_QTR), _rolling_sum(dv, _TD_YEAR))


def dvs_067_dv_daily_change_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percent change in dollar volume from prior day (day-over-day shock)."""
    dv = _dv(close, volume)
    return dv.pct_change(1)


def dvs_068_dv_daily_log_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log change in dollar volume from prior day."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(dv.shift(1))


def dvs_069_dv_5d_change_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day percent change in dollar volume (weekly surge)."""
    dv = _dv(close, volume)
    return dv.pct_change(_TD_WEEK)


def dvs_070_dv_21d_change_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day percent change in dollar volume (monthly surge)."""
    dv = _dv(close, volume)
    return dv.pct_change(_TD_MON)


def dvs_071_dv_spike_after_low_price_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume z-score only on days when close is a 21-day low (distress signature)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    roll_min = _rolling_min(close, _TD_MON)
    at_low = (close <= roll_min)
    return z.where(at_low, 0.0)


def dvs_072_dv_spike_after_low_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume z-score on days when close is a 63-day low."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    roll_min = _rolling_min(close, _TD_QTR)
    at_low = (close <= roll_min)
    return z.where(at_low, 0.0)


def dvs_073_dv_to_price_ratio_21d_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by price-squared, normalized by 21-day mean (turnover intensity)."""
    dv = _dv(close, volume)
    tv = _safe_div(dv, close ** 2)
    return _safe_div(tv, _rolling_mean(tv, _TD_MON))


def dvs_074_dv_concentration_hhi_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HHI-style concentration of daily DV within 21-day window (1 big day = high HHI)."""
    dv = _dv(close, volume)
    sum21 = _rolling_sum(dv, _TD_MON)
    share = _safe_div(dv, sum21)
    share_sq = share ** 2
    return _rolling_sum(share_sq, _TD_MON)


def dvs_075_dv_concentration_hhi_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HHI-style concentration of daily DV within 63-day window."""
    dv = _dv(close, volume)
    sum63 = _rolling_sum(dv, _TD_QTR)
    share = _safe_div(dv, sum63)
    share_sq = share ** 2
    return _rolling_sum(share_sq, _TD_QTR)


# --- Group H (151-175): Additional base features ---

def dvs_151_dv_ratio_ewm126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by its 126-day EWM mean (half-year exponential baseline)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _ewm_mean(dv, _TD_HALF))


def dvs_152_dv_log_ratio_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log ratio of dollar volume to its 63-day EWM mean."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(_ewm_mean(dv, _TD_QTR))


def dvs_153_dv_mad_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Robust z-score: (dv - median) / rolling MAD over 21 days."""
    dv = _dv(close, volume)
    med = _rolling_median(dv, _TD_MON)
    mad = (dv - med).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()
    return _safe_div(dv - med, mad)


def dvs_154_dv_spike_count_3x_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where dollar volume > 3x its 63d mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 3.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_MON)


def dvs_155_dv_spike_count_4x_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where dollar volume > 4x its 63d mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 4.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_QTR)


def dvs_156_dv_spike_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were 2x dollar-volume spikes."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_QTR) / _TD_QTR


def dvs_157_dv_spike_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days that were 2x dollar-volume spikes."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return _rolling_sum(spike, _TD_YEAR) / _TD_YEAR


def dvs_158_dv_pct_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current dollar volume within trailing 5-day window."""
    dv = _dv(close, volume)
    return dv.rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).rank(pct=True)


def dvs_159_dv_top_decile_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current dollar volume is in the top 10% of the trailing 63-day range."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (rank >= 0.90).astype(float)


def dvs_160_dv_bottom_decile_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current dollar volume is in the bottom 10% of the trailing 252-day range."""
    dv = _dv(close, volume)
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (rank <= 0.10).astype(float)


def dvs_161_dv_expanding_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of dollar volume log-transformed."""
    dv = _log_safe(_dv(close, volume))
    return dv.expanding(min_periods=5).rank(pct=True)


def dvs_162_dv_min_63d_vs_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day minimum DV divided by 63-day mean (liquidity drought signal)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_min(dv, _TD_QTR), _rolling_mean(dv, _TD_QTR))


def dvs_163_dv_max_5d_vs_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day max DV divided by 63-day mean DV (short-term peak vs quarterly norm)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_max(dv, _TD_WEEK), _rolling_mean(dv, _TD_QTR))


def dvs_164_dv_log_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log-dollar-volume vs 21-day rolling log distribution."""
    dv = _log_safe(_dv(close, volume))
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    return _safe_div(dv - m, s)


def dvs_165_dv_log_zscore_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding z-score of log-dollar-volume (all-history log-space extremity)."""
    dv = _log_safe(_dv(close, volume))
    m = dv.expanding(min_periods=5).mean()
    s = dv.expanding(min_periods=5).std()
    return _safe_div(dv - m, s)


def dvs_166_dv_spike_on_down_day_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 252d with 2x-dv spike AND price decline."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    ret = close.pct_change(1)
    spike_dn = ((dv > 2.0 * baseline) & (ret < 0)).astype(float)
    return _rolling_sum(spike_dn, _TD_YEAR)


def dvs_167_dv_big_down_day_dv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d z-score of DV, masked to days with >3% price decline (extreme capitulation)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    return z.where(ret < -0.03, 0.0)


def dvs_168_dv_weighted_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted average daily return over 63 days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    return _safe_div(_rolling_sum(dv * ret, _TD_QTR), _rolling_sum(dv, _TD_QTR))


def dvs_169_dv_10d_change_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """10-day percent change in dollar volume (2-week surge)."""
    dv = _dv(close, volume)
    return dv.pct_change(10)


def dvs_170_dv_63d_change_pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day percent change in dollar volume (quarterly surge)."""
    dv = _dv(close, volume)
    return dv.pct_change(_TD_QTR)


def dvs_171_dv_log_change_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day log change in dollar volume (weekly log-scale surge)."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(dv.shift(_TD_WEEK))


def dvs_172_dv_log_change_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day log change in dollar volume (monthly log-scale surge)."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(dv.shift(_TD_MON))


def dvs_173_dv_concentration_hhi_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HHI-style concentration of daily DV within 252-day window."""
    dv = _dv(close, volume)
    sum252 = _rolling_sum(dv, _TD_YEAR)
    share = _safe_div(dv, sum252)
    return _rolling_sum(share ** 2, _TD_YEAR)


def dvs_174_dv_down_day_dv_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day total dollar volume traded on down-price days."""
    dv = _dv(close, volume)
    ret = close.pct_change(1)
    dv_dn = dv.where(ret < 0, 0.0)
    return _safe_div(_rolling_sum(dv_dn, _TD_YEAR), _rolling_sum(dv, _TD_YEAR))


def dvs_175_dv_zscore_21d_on_big_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day z-score of dollar volume, masked to days with >2% price decline."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    return z.where(ret < -0.02, 0.0)


# ── Registry ──────────────────────────────────────────────────────────────────

DOLLAR_VOLUME_SHOCK_REGISTRY_001_075 = {
    "dvs_001_dv_ratio_21d": {"inputs": ["close", "volume"], "func": dvs_001_dv_ratio_21d},
    "dvs_002_dv_ratio_63d": {"inputs": ["close", "volume"], "func": dvs_002_dv_ratio_63d},
    "dvs_003_dv_ratio_126d": {"inputs": ["close", "volume"], "func": dvs_003_dv_ratio_126d},
    "dvs_004_dv_ratio_252d": {"inputs": ["close", "volume"], "func": dvs_004_dv_ratio_252d},
    "dvs_005_dv_log_ratio_21d": {"inputs": ["close", "volume"], "func": dvs_005_dv_log_ratio_21d},
    "dvs_006_dv_log_ratio_63d": {"inputs": ["close", "volume"], "func": dvs_006_dv_log_ratio_63d},
    "dvs_007_dv_log_ratio_252d": {"inputs": ["close", "volume"], "func": dvs_007_dv_log_ratio_252d},
    "dvs_008_dv_ratio_ewm21": {"inputs": ["close", "volume"], "func": dvs_008_dv_ratio_ewm21},
    "dvs_009_dv_ratio_ewm63": {"inputs": ["close", "volume"], "func": dvs_009_dv_ratio_ewm63},
    "dvs_010_dv_ratio_median_63d": {"inputs": ["close", "volume"], "func": dvs_010_dv_ratio_median_63d},
    "dvs_011_dv_zscore_21d": {"inputs": ["close", "volume"], "func": dvs_011_dv_zscore_21d},
    "dvs_012_dv_zscore_63d": {"inputs": ["close", "volume"], "func": dvs_012_dv_zscore_63d},
    "dvs_013_dv_zscore_126d": {"inputs": ["close", "volume"], "func": dvs_013_dv_zscore_126d},
    "dvs_014_dv_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_014_dv_zscore_252d},
    "dvs_015_dv_log_zscore_63d": {"inputs": ["close", "volume"], "func": dvs_015_dv_log_zscore_63d},
    "dvs_016_dv_log_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_016_dv_log_zscore_252d},
    "dvs_017_dv_zscore_expanding": {"inputs": ["close", "volume"], "func": dvs_017_dv_zscore_expanding},
    "dvs_018_dv_zscore_21d_on_down_days": {"inputs": ["close", "volume"], "func": dvs_018_dv_zscore_21d_on_down_days},
    "dvs_019_dv_mad_zscore_63d": {"inputs": ["close", "volume"], "func": dvs_019_dv_mad_zscore_63d},
    "dvs_020_dv_mad_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_020_dv_mad_zscore_252d},
    "dvs_021_dv_spike_count_2x_21d": {"inputs": ["close", "volume"], "func": dvs_021_dv_spike_count_2x_21d},
    "dvs_022_dv_spike_count_2x_63d": {"inputs": ["close", "volume"], "func": dvs_022_dv_spike_count_2x_63d},
    "dvs_023_dv_spike_count_3x_63d": {"inputs": ["close", "volume"], "func": dvs_023_dv_spike_count_3x_63d},
    "dvs_024_dv_spike_count_2x_252d": {"inputs": ["close", "volume"], "func": dvs_024_dv_spike_count_2x_252d},
    "dvs_025_dv_spike_count_zscore2_21d": {"inputs": ["close", "volume"], "func": dvs_025_dv_spike_count_zscore2_21d},
    "dvs_026_dv_spike_count_zscore2_63d": {"inputs": ["close", "volume"], "func": dvs_026_dv_spike_count_zscore2_63d},
    "dvs_027_dv_spike_count_zscore3_252d": {"inputs": ["close", "volume"], "func": dvs_027_dv_spike_count_zscore3_252d},
    "dvs_028_dv_spike_on_down_day_count_21d": {"inputs": ["close", "volume"], "func": dvs_028_dv_spike_on_down_day_count_21d},
    "dvs_029_dv_spike_on_down_day_count_63d": {"inputs": ["close", "volume"], "func": dvs_029_dv_spike_on_down_day_count_63d},
    "dvs_030_dv_spike_fraction_21d": {"inputs": ["close", "volume"], "func": dvs_030_dv_spike_fraction_21d},
    "dvs_031_dv_max_21d": {"inputs": ["close", "volume"], "func": dvs_031_dv_max_21d},
    "dvs_032_dv_max_63d": {"inputs": ["close", "volume"], "func": dvs_032_dv_max_63d},
    "dvs_033_dv_max_252d": {"inputs": ["close", "volume"], "func": dvs_033_dv_max_252d},
    "dvs_034_dv_current_vs_max_63d": {"inputs": ["close", "volume"], "func": dvs_034_dv_current_vs_max_63d},
    "dvs_035_dv_current_vs_max_252d": {"inputs": ["close", "volume"], "func": dvs_035_dv_current_vs_max_252d},
    "dvs_036_dv_max_21d_vs_mean_252d": {"inputs": ["close", "volume"], "func": dvs_036_dv_max_21d_vs_mean_252d},
    "dvs_037_dv_max_63d_vs_mean_252d": {"inputs": ["close", "volume"], "func": dvs_037_dv_max_63d_vs_mean_252d},
    "dvs_038_dv_max_expanding": {"inputs": ["close", "volume"], "func": dvs_038_dv_max_expanding},
    "dvs_039_dv_current_vs_expanding_max": {"inputs": ["close", "volume"], "func": dvs_039_dv_current_vs_expanding_max},
    "dvs_040_dv_max_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": dvs_040_dv_max_21d_pct_rank_252d},
    "dvs_041_dv_price_collapse_flag": {"inputs": ["close", "volume"], "func": dvs_041_dv_price_collapse_flag},
    "dvs_042_dv_on_down_days_sum_21d": {"inputs": ["close", "volume"], "func": dvs_042_dv_on_down_days_sum_21d},
    "dvs_043_dv_on_down_days_sum_63d": {"inputs": ["close", "volume"], "func": dvs_043_dv_on_down_days_sum_63d},
    "dvs_044_dv_down_vs_up_ratio_21d": {"inputs": ["close", "volume"], "func": dvs_044_dv_down_vs_up_ratio_21d},
    "dvs_045_dv_down_vs_up_ratio_63d": {"inputs": ["close", "volume"], "func": dvs_045_dv_down_vs_up_ratio_63d},
    "dvs_046_dv_down_vs_up_ratio_252d": {"inputs": ["close", "volume"], "func": dvs_046_dv_down_vs_up_ratio_252d},
    "dvs_047_dv_price_ret_product_21d": {"inputs": ["close", "volume"], "func": dvs_047_dv_price_ret_product_21d},
    "dvs_048_dv_price_ret_product_63d": {"inputs": ["close", "volume"], "func": dvs_048_dv_price_ret_product_63d},
    "dvs_049_dv_weighted_negative_return_21d": {"inputs": ["close", "volume"], "func": dvs_049_dv_weighted_negative_return_21d},
    "dvs_050_dv_weighted_negative_return_63d": {"inputs": ["close", "volume"], "func": dvs_050_dv_weighted_negative_return_63d},
    "dvs_051_dv_pct_rank_21d": {"inputs": ["close", "volume"], "func": dvs_051_dv_pct_rank_21d},
    "dvs_052_dv_pct_rank_63d": {"inputs": ["close", "volume"], "func": dvs_052_dv_pct_rank_63d},
    "dvs_053_dv_pct_rank_252d": {"inputs": ["close", "volume"], "func": dvs_053_dv_pct_rank_252d},
    "dvs_054_dv_pct_rank_expanding": {"inputs": ["close", "volume"], "func": dvs_054_dv_pct_rank_expanding},
    "dvs_055_dv_top_decile_flag_252d": {"inputs": ["close", "volume"], "func": dvs_055_dv_top_decile_flag_252d},
    "dvs_056_dv_top_quintile_flag_63d": {"inputs": ["close", "volume"], "func": dvs_056_dv_top_quintile_flag_63d},
    "dvs_057_dv_sum_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": dvs_057_dv_sum_21d_pct_rank_252d},
    "dvs_058_dv_sum_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": dvs_058_dv_sum_63d_pct_rank_252d},
    "dvs_059_dv_high_rank_on_down_day_21d": {"inputs": ["close", "volume"], "func": dvs_059_dv_high_rank_on_down_day_21d},
    "dvs_060_dv_high_rank_on_down_day_63d": {"inputs": ["close", "volume"], "func": dvs_060_dv_high_rank_on_down_day_63d},
    "dvs_061_dv_at_52wk_low_flag": {"inputs": ["close", "volume"], "func": dvs_061_dv_at_52wk_low_flag},
    "dvs_062_dv_cumsum_21d": {"inputs": ["close", "volume"], "func": dvs_062_dv_cumsum_21d},
    "dvs_063_dv_cumsum_63d": {"inputs": ["close", "volume"], "func": dvs_063_dv_cumsum_63d},
    "dvs_064_dv_cumsum_252d": {"inputs": ["close", "volume"], "func": dvs_064_dv_cumsum_252d},
    "dvs_065_dv_sum_21d_vs_sum_252d": {"inputs": ["close", "volume"], "func": dvs_065_dv_sum_21d_vs_sum_252d},
    "dvs_066_dv_sum_63d_vs_sum_252d": {"inputs": ["close", "volume"], "func": dvs_066_dv_sum_63d_vs_sum_252d},
    "dvs_067_dv_daily_change_pct": {"inputs": ["close", "volume"], "func": dvs_067_dv_daily_change_pct},
    "dvs_068_dv_daily_log_change": {"inputs": ["close", "volume"], "func": dvs_068_dv_daily_log_change},
    "dvs_069_dv_5d_change_pct": {"inputs": ["close", "volume"], "func": dvs_069_dv_5d_change_pct},
    "dvs_070_dv_21d_change_pct": {"inputs": ["close", "volume"], "func": dvs_070_dv_21d_change_pct},
    "dvs_071_dv_spike_after_low_price_21d": {"inputs": ["close", "volume"], "func": dvs_071_dv_spike_after_low_price_21d},
    "dvs_072_dv_spike_after_low_price_63d": {"inputs": ["close", "volume"], "func": dvs_072_dv_spike_after_low_price_63d},
    "dvs_073_dv_to_price_ratio_21d_norm": {"inputs": ["close", "volume"], "func": dvs_073_dv_to_price_ratio_21d_norm},
    "dvs_074_dv_concentration_hhi_21d": {"inputs": ["close", "volume"], "func": dvs_074_dv_concentration_hhi_21d},
    "dvs_075_dv_concentration_hhi_63d": {"inputs": ["close", "volume"], "func": dvs_075_dv_concentration_hhi_63d},
    "dvs_151_dv_ratio_ewm126": {"inputs": ["close", "volume"], "func": dvs_151_dv_ratio_ewm126},
    "dvs_152_dv_log_ratio_ewm63": {"inputs": ["close", "volume"], "func": dvs_152_dv_log_ratio_ewm63},
    "dvs_153_dv_mad_zscore_21d": {"inputs": ["close", "volume"], "func": dvs_153_dv_mad_zscore_21d},
    "dvs_154_dv_spike_count_3x_21d": {"inputs": ["close", "volume"], "func": dvs_154_dv_spike_count_3x_21d},
    "dvs_155_dv_spike_count_4x_63d": {"inputs": ["close", "volume"], "func": dvs_155_dv_spike_count_4x_63d},
    "dvs_156_dv_spike_fraction_63d": {"inputs": ["close", "volume"], "func": dvs_156_dv_spike_fraction_63d},
    "dvs_157_dv_spike_fraction_252d": {"inputs": ["close", "volume"], "func": dvs_157_dv_spike_fraction_252d},
    "dvs_158_dv_pct_rank_5d": {"inputs": ["close", "volume"], "func": dvs_158_dv_pct_rank_5d},
    "dvs_159_dv_top_decile_flag_63d": {"inputs": ["close", "volume"], "func": dvs_159_dv_top_decile_flag_63d},
    "dvs_160_dv_bottom_decile_flag_252d": {"inputs": ["close", "volume"], "func": dvs_160_dv_bottom_decile_flag_252d},
    "dvs_161_dv_expanding_pct_rank": {"inputs": ["close", "volume"], "func": dvs_161_dv_expanding_pct_rank},
    "dvs_162_dv_min_63d_vs_mean_63d": {"inputs": ["close", "volume"], "func": dvs_162_dv_min_63d_vs_mean_63d},
    "dvs_163_dv_max_5d_vs_mean_63d": {"inputs": ["close", "volume"], "func": dvs_163_dv_max_5d_vs_mean_63d},
    "dvs_164_dv_log_zscore_21d": {"inputs": ["close", "volume"], "func": dvs_164_dv_log_zscore_21d},
    "dvs_165_dv_log_zscore_expanding": {"inputs": ["close", "volume"], "func": dvs_165_dv_log_zscore_expanding},
    "dvs_166_dv_spike_on_down_day_count_252d": {"inputs": ["close", "volume"], "func": dvs_166_dv_spike_on_down_day_count_252d},
    "dvs_167_dv_big_down_day_dv_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_167_dv_big_down_day_dv_zscore_252d},
    "dvs_168_dv_weighted_return_63d": {"inputs": ["close", "volume"], "func": dvs_168_dv_weighted_return_63d},
    "dvs_169_dv_10d_change_pct": {"inputs": ["close", "volume"], "func": dvs_169_dv_10d_change_pct},
    "dvs_170_dv_63d_change_pct": {"inputs": ["close", "volume"], "func": dvs_170_dv_63d_change_pct},
    "dvs_171_dv_log_change_5d": {"inputs": ["close", "volume"], "func": dvs_171_dv_log_change_5d},
    "dvs_172_dv_log_change_21d": {"inputs": ["close", "volume"], "func": dvs_172_dv_log_change_21d},
    "dvs_173_dv_concentration_hhi_252d": {"inputs": ["close", "volume"], "func": dvs_173_dv_concentration_hhi_252d},
    "dvs_174_dv_down_day_dv_fraction_252d": {"inputs": ["close", "volume"], "func": dvs_174_dv_down_day_dv_fraction_252d},
    "dvs_175_dv_zscore_21d_on_big_down_days": {"inputs": ["close", "volume"], "func": dvs_175_dv_zscore_21d_on_big_down_days},
}
