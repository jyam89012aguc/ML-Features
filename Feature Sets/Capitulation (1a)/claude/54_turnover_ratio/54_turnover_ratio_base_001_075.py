"""
54_turnover_ratio — Base Features 001-075
Domain: long-horizon turnover-rate extremes via price/volume proxy
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — multi-year turnover extremes, float-proxy baseline,
  illiquidity signals, turnover-rate percentile vs years-long history.
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
_TD_2YR = 504
_TD_3YR = 756
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


def _dollar_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxy for traded value: close * volume."""
    return close * volume


def _turnover_proxy(volume: pd.Series, window: int) -> pd.Series:
    """Volume normalized by long-window rolling mean — the core turnover proxy."""
    baseline = _rolling_mean(volume, window)
    return _safe_div(volume, baseline)


def _cum_vol_float_proxy(volume: pd.Series, window: int) -> pd.Series:
    """Trailing cumulative volume as float proxy (sum over long window)."""
    return _rolling_sum(volume, window)


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-010): Volume vs 252d baseline — core annual turnover proxy ---

def tnv_001_vol_vs_252d_mean(volume: pd.Series) -> pd.Series:
    """Volume divided by trailing 252-day mean (annual float-proxy turnover rate)."""
    return _turnover_proxy(volume, _TD_YEAR)


def tnv_002_vol_vs_504d_mean(volume: pd.Series) -> pd.Series:
    """Volume divided by trailing 504-day mean (2-year float-proxy turnover rate)."""
    return _turnover_proxy(volume, _TD_2YR)


def tnv_003_vol_vs_756d_mean(volume: pd.Series) -> pd.Series:
    """Volume divided by trailing 756-day mean (3-year float-proxy turnover rate)."""
    return _turnover_proxy(volume, _TD_3YR)


def tnv_004_vol_vs_252d_median(volume: pd.Series) -> pd.Series:
    """Volume divided by 252-day median (robust annual turnover proxy)."""
    med = _rolling_median(volume, _TD_YEAR)
    return _safe_div(volume, med)


def tnv_005_vol_vs_504d_median(volume: pd.Series) -> pd.Series:
    """Volume divided by 504-day median (robust 2-year turnover proxy)."""
    med = _rolling_median(volume, _TD_2YR)
    return _safe_div(volume, med)


def tnv_006_log_vol_vs_252d_mean(volume: pd.Series) -> pd.Series:
    """Log of volume-to-252d-mean ratio (compresses spike tail)."""
    return np.log1p(_turnover_proxy(volume, _TD_YEAR))


def tnv_007_log_vol_vs_504d_mean(volume: pd.Series) -> pd.Series:
    """Log of volume-to-504d-mean ratio."""
    return np.log1p(_turnover_proxy(volume, _TD_2YR))


def tnv_008_vol_vs_252d_mean_zscore(volume: pd.Series) -> pd.Series:
    """Z-score of volume against 252-day mean/std (standardised turnover)."""
    m = _rolling_mean(volume, _TD_YEAR)
    s = _rolling_std(volume, _TD_YEAR)
    return _safe_div(volume - m, s)


def tnv_009_vol_vs_504d_mean_zscore(volume: pd.Series) -> pd.Series:
    """Z-score of volume against 504-day mean/std."""
    m = _rolling_mean(volume, _TD_2YR)
    s = _rolling_std(volume, _TD_2YR)
    return _safe_div(volume - m, s)


def tnv_010_vol_vs_756d_mean_zscore(volume: pd.Series) -> pd.Series:
    """Z-score of volume against 756-day mean/std."""
    m = _rolling_mean(volume, _TD_3YR)
    s = _rolling_std(volume, _TD_3YR)
    return _safe_div(volume - m, s)


# --- Group B (011-020): Turnover percentile rank vs multi-year history ---

def tnv_011_vol_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 252-day distribution."""
    return volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tnv_012_vol_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 504-day distribution."""
    return volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_013_vol_pct_rank_756d(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume within trailing 756-day distribution."""
    return volume.rolling(_TD_3YR, min_periods=_TD_2YR).rank(pct=True)


def tnv_014_vol_pct_rank_expanding(volume: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of today's volume."""
    return volume.expanding(min_periods=_TD_QTR).rank(pct=True)


def tnv_015_turnover_proxy_252d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Pct rank of 252d-normalised turnover within trailing 504-day window."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return tnv.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_016_turnover_proxy_252d_pct_rank_756d(volume: pd.Series) -> pd.Series:
    """Pct rank of 252d-normalised turnover within trailing 756-day window."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return tnv.rolling(_TD_3YR, min_periods=_TD_2YR).rank(pct=True)


def tnv_017_vol_top_decile_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is in top decile of trailing 252-day volume."""
    return (volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True) >= 0.9).astype(float)


def tnv_018_vol_top_decile_504d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is in top decile of trailing 504-day volume."""
    return (volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True) >= 0.9).astype(float)


def tnv_019_vol_bottom_decile_252d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is in bottom decile of trailing 252-day volume (illiquidity)."""
    return (volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True) <= 0.1).astype(float)


def tnv_020_vol_bottom_decile_504d_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume is in bottom decile of trailing 504-day volume."""
    return (volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True) <= 0.1).astype(float)


# --- Group C (021-030): Float proxy (cumulative volume) and today vs float ---

def tnv_021_vol_vs_cum_vol_252d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of cumulative 252-day volume (daily float turnover)."""
    cum = _cum_vol_float_proxy(volume, _TD_YEAR)
    return _safe_div(volume, cum)


def tnv_022_vol_vs_cum_vol_504d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of cumulative 504-day volume."""
    cum = _cum_vol_float_proxy(volume, _TD_2YR)
    return _safe_div(volume, cum)


def tnv_023_vol_vs_cum_vol_756d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of cumulative 756-day volume."""
    cum = _cum_vol_float_proxy(volume, _TD_3YR)
    return _safe_div(volume, cum)


def tnv_024_vol_vs_rolling_max_vol_252d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of trailing 252-day peak volume."""
    pk = _rolling_max(volume, _TD_YEAR)
    return _safe_div(volume, pk)


def tnv_025_vol_vs_rolling_max_vol_504d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of trailing 504-day peak volume."""
    pk = _rolling_max(volume, _TD_2YR)
    return _safe_div(volume, pk)


def tnv_026_vol_vs_rolling_max_vol_756d(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of trailing 756-day peak volume."""
    pk = _rolling_max(volume, _TD_3YR)
    return _safe_div(volume, pk)


def tnv_027_expanding_cum_vol_today_fraction(volume: pd.Series) -> pd.Series:
    """Today's volume as fraction of all-time cumulative volume (expanding)."""
    cum = volume.expanding(min_periods=1).sum()
    return _safe_div(volume, cum)


def tnv_028_vol_vs_expanding_max(volume: pd.Series) -> pd.Series:
    """Today's volume vs all-time expanding maximum volume."""
    pk = volume.expanding(min_periods=1).max()
    return _safe_div(volume, pk)


def tnv_029_cum_vol_252d_vs_504d(volume: pd.Series) -> pd.Series:
    """Ratio of 252-day cumulative volume to 504-day cumulative volume (recent float share)."""
    c252 = _cum_vol_float_proxy(volume, _TD_YEAR)
    c504 = _cum_vol_float_proxy(volume, _TD_2YR)
    return _safe_div(c252, c504)


def tnv_030_vol_vs_expanding_mean(volume: pd.Series) -> pd.Series:
    """Today's volume vs expanding all-time mean volume."""
    m = volume.expanding(min_periods=_TD_QTR).mean()
    return _safe_div(volume, m)


# --- Group D (031-040): Dollar-volume turnover proxies ---

def tnv_031_dvol_vs_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume vs 252-day mean dollar-volume (value-weighted turnover proxy)."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_YEAR))


def tnv_032_dvol_vs_504d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume vs 504-day mean dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_2YR))


def tnv_033_dvol_vs_756d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume vs 756-day mean dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_3YR))


def tnv_034_dvol_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of dollar-volume within trailing 252-day distribution."""
    dv = _dollar_volume(close, volume)
    return dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tnv_035_dvol_pct_rank_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of dollar-volume within trailing 504-day distribution."""
    dv = _dollar_volume(close, volume)
    return dv.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_036_dvol_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar-volume vs 252-day distribution."""
    dv = _dollar_volume(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    return _safe_div(dv - m, s)


def tnv_037_dvol_zscore_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar-volume vs 504-day distribution."""
    dv = _dollar_volume(close, volume)
    m = _rolling_mean(dv, _TD_2YR)
    s = _rolling_std(dv, _TD_2YR)
    return _safe_div(dv - m, s)


def tnv_038_dvol_vs_cum_dvol_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily dollar-volume as fraction of 252-day cumulative dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_sum(dv, _TD_YEAR))


def tnv_039_dvol_vs_cum_dvol_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Daily dollar-volume as fraction of 504-day cumulative dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_sum(dv, _TD_2YR))


def tnv_040_log_dvol_vs_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log ratio of dollar-volume to 252-day mean dollar-volume."""
    dv = _dollar_volume(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_YEAR))


# --- Group E (041-050): High-turnover and low-turnover extremes ---

def tnv_041_vol_gt_2x_252d_mean_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume > 2x the 252-day mean (high turnover extreme)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    return (volume > 2.0 * baseline).astype(float)


def tnv_042_vol_gt_3x_252d_mean_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume > 3x the 252-day mean (very high turnover extreme)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    return (volume > 3.0 * baseline).astype(float)


def tnv_043_vol_gt_2x_504d_mean_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume > 2x the 504-day mean."""
    baseline = _rolling_mean(volume, _TD_2YR)
    return (volume > 2.0 * baseline).astype(float)


def tnv_044_vol_lt_half_252d_mean_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume < 0.5x the 252-day mean (illiquidity extreme)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    return (volume < 0.5 * baseline).astype(float)


def tnv_045_vol_lt_quarter_252d_mean_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume < 0.25x the 252-day mean (severe illiquidity)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    return (volume < 0.25 * baseline).astype(float)


def tnv_046_vol_lt_half_504d_mean_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume < 0.5x the 504-day mean."""
    baseline = _rolling_mean(volume, _TD_2YR)
    return (volume < 0.5 * baseline).astype(float)


def tnv_047_high_turnover_days_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days with volume > 2x 252d mean within trailing 252 days."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    flag = (volume > 2.0 * baseline).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


def tnv_048_high_turnover_days_count_504d(volume: pd.Series) -> pd.Series:
    """Count of days with volume > 2x 504d mean within trailing 504 days."""
    baseline = _rolling_mean(volume, _TD_2YR)
    flag = (volume > 2.0 * baseline).astype(float)
    return flag.rolling(_TD_2YR, min_periods=_TD_YEAR).sum()


def tnv_049_low_turnover_days_count_252d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 0.5x 252d mean within trailing 252 days."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    flag = (volume < 0.5 * baseline).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).sum()


def tnv_050_low_turnover_days_count_504d(volume: pd.Series) -> pd.Series:
    """Count of days with volume < 0.5x 504d mean within trailing 504 days."""
    baseline = _rolling_mean(volume, _TD_2YR)
    flag = (volume < 0.5 * baseline).astype(float)
    return flag.rolling(_TD_2YR, min_periods=_TD_YEAR).sum()


# --- Group F (051-060): Turnover regime — multi-year mean levels ---

def tnv_051_mean_252d_vs_504d_turnover_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 252d mean volume to 504d mean volume (recent vs 2yr baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(volume, _TD_2YR))


def tnv_052_mean_252d_vs_756d_turnover_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 252d mean volume to 756d mean volume (recent vs 3yr baseline)."""
    return _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(volume, _TD_3YR))


def tnv_053_mean_126d_vs_504d_turnover_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 126d mean volume to 504d mean volume (half-year vs 2-year)."""
    return _safe_div(_rolling_mean(volume, _TD_HALF), _rolling_mean(volume, _TD_2YR))


def tnv_054_mean_63d_vs_252d_turnover_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63d mean volume to 252d mean volume (quarter vs annual)."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))


def tnv_055_mean_21d_vs_252d_turnover_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d mean volume to 252d mean volume (monthly vs annual)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def tnv_056_mean_21d_vs_504d_turnover_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21d mean volume to 504d mean volume (recent month vs 2yr)."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_2YR))


def tnv_057_std_vol_252d_vs_mean_vol_252d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 252 days (turnover volatility)."""
    return _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))


def tnv_058_std_vol_504d_vs_mean_vol_504d(volume: pd.Series) -> pd.Series:
    """Coefficient of variation of volume over 504 days."""
    return _safe_div(_rolling_std(volume, _TD_2YR), _rolling_mean(volume, _TD_2YR))


def tnv_059_log_mean_vol_252d(volume: pd.Series) -> pd.Series:
    """Log of 252-day mean volume (level of long-run turnover activity)."""
    return _log_safe(_rolling_mean(volume, _TD_YEAR))


def tnv_060_log_mean_vol_504d(volume: pd.Series) -> pd.Series:
    """Log of 504-day mean volume."""
    return _log_safe(_rolling_mean(volume, _TD_2YR))


# --- Group G (061-075): Turnover acceleration, rarity, and composite signals ---

def tnv_061_turnover_proxy_252d_zscore_504d(volume: pd.Series) -> pd.Series:
    """Z-score of 252d-normalised turnover proxy within its trailing 504-day distribution."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    m = _rolling_mean(tnv, _TD_2YR)
    s = _rolling_std(tnv, _TD_2YR)
    return _safe_div(tnv - m, s)


def tnv_062_turnover_proxy_252d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 252d-normalised turnover proxy within its own 252-day distribution."""
    tnv = _turnover_proxy(volume, _TD_YEAR)
    return tnv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tnv_063_turnover_proxy_504d_pct_rank_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 504d-normalised turnover proxy within its own 504-day distribution."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    return tnv.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)


def tnv_064_vol_pct_rank_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day change in 252d percentile rank of volume."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_MON)


def tnv_065_vol_pct_rank_504d_expanding(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 504d-normalised turnover proxy (all-history extremity)."""
    tnv = _turnover_proxy(volume, _TD_2YR)
    return tnv.expanding(min_periods=_TD_QTR).rank(pct=True)


def tnv_066_turnover_extremity_score_252d(volume: pd.Series) -> pd.Series:
    """Distance of 252d-pct-rank from 0.5 (measures extremity in either direction)."""
    rank = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (rank - 0.5).abs()


def tnv_067_turnover_extremity_score_504d(volume: pd.Series) -> pd.Series:
    """Distance of 504d-pct-rank from 0.5."""
    rank = volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    return (rank - 0.5).abs()


def tnv_068_vol_pct_rank_756d_expanding(volume: pd.Series) -> pd.Series:
    """Percentile rank of today's volume in the expanding all-history distribution."""
    return volume.expanding(min_periods=_TD_QTR).rank(pct=True)


def tnv_069_consecutive_above_252d_mean(volume: pd.Series) -> pd.Series:
    """Consecutive days volume > 252-day mean (sustained high-turnover run)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    cond = volume > baseline
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def tnv_070_consecutive_below_252d_mean(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 252-day mean (sustained low-turnover run)."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    cond = volume < baseline
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def tnv_071_consecutive_below_504d_mean(volume: pd.Series) -> pd.Series:
    """Consecutive days volume < 504-day mean (illiquidity regime streak)."""
    baseline = _rolling_mean(volume, _TD_2YR)
    cond = volume < baseline
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def tnv_072_high_turnover_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume > 252d rolling mean."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    flag = (volume > baseline).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def tnv_073_low_turnover_fraction_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume < 0.5x 252d rolling mean."""
    baseline = _rolling_mean(volume, _TD_YEAR)
    flag = (volume < 0.5 * baseline).astype(float)
    return flag.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def tnv_074_high_turnover_fraction_504d(volume: pd.Series) -> pd.Series:
    """Fraction of last 504 days where volume > 504d rolling mean."""
    baseline = _rolling_mean(volume, _TD_2YR)
    flag = (volume > baseline).astype(float)
    return flag.rolling(_TD_2YR, min_periods=_TD_YEAR).mean()


def tnv_075_turnover_composite_extremity_score(volume: pd.Series) -> pd.Series:
    """Average of 252d and 504d pct-rank extremity scores (composite rareness)."""
    r252 = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r504 = volume.rolling(_TD_2YR, min_periods=_TD_YEAR).rank(pct=True)
    e252 = (r252 - 0.5).abs()
    e504 = (r504 - 0.5).abs()
    return (e252 + e504) / 2.0


# ── Registry ──────────────────────────────────────────────────────────────────

TURNOVER_RATIO_REGISTRY_001_075 = {
    "tnv_001_vol_vs_252d_mean": {"inputs": ["volume"], "func": tnv_001_vol_vs_252d_mean},
    "tnv_002_vol_vs_504d_mean": {"inputs": ["volume"], "func": tnv_002_vol_vs_504d_mean},
    "tnv_003_vol_vs_756d_mean": {"inputs": ["volume"], "func": tnv_003_vol_vs_756d_mean},
    "tnv_004_vol_vs_252d_median": {"inputs": ["volume"], "func": tnv_004_vol_vs_252d_median},
    "tnv_005_vol_vs_504d_median": {"inputs": ["volume"], "func": tnv_005_vol_vs_504d_median},
    "tnv_006_log_vol_vs_252d_mean": {"inputs": ["volume"], "func": tnv_006_log_vol_vs_252d_mean},
    "tnv_007_log_vol_vs_504d_mean": {"inputs": ["volume"], "func": tnv_007_log_vol_vs_504d_mean},
    "tnv_008_vol_vs_252d_mean_zscore": {"inputs": ["volume"], "func": tnv_008_vol_vs_252d_mean_zscore},
    "tnv_009_vol_vs_504d_mean_zscore": {"inputs": ["volume"], "func": tnv_009_vol_vs_504d_mean_zscore},
    "tnv_010_vol_vs_756d_mean_zscore": {"inputs": ["volume"], "func": tnv_010_vol_vs_756d_mean_zscore},
    "tnv_011_vol_pct_rank_252d": {"inputs": ["volume"], "func": tnv_011_vol_pct_rank_252d},
    "tnv_012_vol_pct_rank_504d": {"inputs": ["volume"], "func": tnv_012_vol_pct_rank_504d},
    "tnv_013_vol_pct_rank_756d": {"inputs": ["volume"], "func": tnv_013_vol_pct_rank_756d},
    "tnv_014_vol_pct_rank_expanding": {"inputs": ["volume"], "func": tnv_014_vol_pct_rank_expanding},
    "tnv_015_turnover_proxy_252d_pct_rank_504d": {"inputs": ["volume"], "func": tnv_015_turnover_proxy_252d_pct_rank_504d},
    "tnv_016_turnover_proxy_252d_pct_rank_756d": {"inputs": ["volume"], "func": tnv_016_turnover_proxy_252d_pct_rank_756d},
    "tnv_017_vol_top_decile_252d_flag": {"inputs": ["volume"], "func": tnv_017_vol_top_decile_252d_flag},
    "tnv_018_vol_top_decile_504d_flag": {"inputs": ["volume"], "func": tnv_018_vol_top_decile_504d_flag},
    "tnv_019_vol_bottom_decile_252d_flag": {"inputs": ["volume"], "func": tnv_019_vol_bottom_decile_252d_flag},
    "tnv_020_vol_bottom_decile_504d_flag": {"inputs": ["volume"], "func": tnv_020_vol_bottom_decile_504d_flag},
    "tnv_021_vol_vs_cum_vol_252d": {"inputs": ["volume"], "func": tnv_021_vol_vs_cum_vol_252d},
    "tnv_022_vol_vs_cum_vol_504d": {"inputs": ["volume"], "func": tnv_022_vol_vs_cum_vol_504d},
    "tnv_023_vol_vs_cum_vol_756d": {"inputs": ["volume"], "func": tnv_023_vol_vs_cum_vol_756d},
    "tnv_024_vol_vs_rolling_max_vol_252d": {"inputs": ["volume"], "func": tnv_024_vol_vs_rolling_max_vol_252d},
    "tnv_025_vol_vs_rolling_max_vol_504d": {"inputs": ["volume"], "func": tnv_025_vol_vs_rolling_max_vol_504d},
    "tnv_026_vol_vs_rolling_max_vol_756d": {"inputs": ["volume"], "func": tnv_026_vol_vs_rolling_max_vol_756d},
    "tnv_027_expanding_cum_vol_today_fraction": {"inputs": ["volume"], "func": tnv_027_expanding_cum_vol_today_fraction},
    "tnv_028_vol_vs_expanding_max": {"inputs": ["volume"], "func": tnv_028_vol_vs_expanding_max},
    "tnv_029_cum_vol_252d_vs_504d": {"inputs": ["volume"], "func": tnv_029_cum_vol_252d_vs_504d},
    "tnv_030_vol_vs_expanding_mean": {"inputs": ["volume"], "func": tnv_030_vol_vs_expanding_mean},
    "tnv_031_dvol_vs_252d_mean": {"inputs": ["close", "volume"], "func": tnv_031_dvol_vs_252d_mean},
    "tnv_032_dvol_vs_504d_mean": {"inputs": ["close", "volume"], "func": tnv_032_dvol_vs_504d_mean},
    "tnv_033_dvol_vs_756d_mean": {"inputs": ["close", "volume"], "func": tnv_033_dvol_vs_756d_mean},
    "tnv_034_dvol_pct_rank_252d": {"inputs": ["close", "volume"], "func": tnv_034_dvol_pct_rank_252d},
    "tnv_035_dvol_pct_rank_504d": {"inputs": ["close", "volume"], "func": tnv_035_dvol_pct_rank_504d},
    "tnv_036_dvol_zscore_252d": {"inputs": ["close", "volume"], "func": tnv_036_dvol_zscore_252d},
    "tnv_037_dvol_zscore_504d": {"inputs": ["close", "volume"], "func": tnv_037_dvol_zscore_504d},
    "tnv_038_dvol_vs_cum_dvol_252d": {"inputs": ["close", "volume"], "func": tnv_038_dvol_vs_cum_dvol_252d},
    "tnv_039_dvol_vs_cum_dvol_504d": {"inputs": ["close", "volume"], "func": tnv_039_dvol_vs_cum_dvol_504d},
    "tnv_040_log_dvol_vs_252d_mean": {"inputs": ["close", "volume"], "func": tnv_040_log_dvol_vs_252d_mean},
    "tnv_041_vol_gt_2x_252d_mean_flag": {"inputs": ["volume"], "func": tnv_041_vol_gt_2x_252d_mean_flag},
    "tnv_042_vol_gt_3x_252d_mean_flag": {"inputs": ["volume"], "func": tnv_042_vol_gt_3x_252d_mean_flag},
    "tnv_043_vol_gt_2x_504d_mean_flag": {"inputs": ["volume"], "func": tnv_043_vol_gt_2x_504d_mean_flag},
    "tnv_044_vol_lt_half_252d_mean_flag": {"inputs": ["volume"], "func": tnv_044_vol_lt_half_252d_mean_flag},
    "tnv_045_vol_lt_quarter_252d_mean_flag": {"inputs": ["volume"], "func": tnv_045_vol_lt_quarter_252d_mean_flag},
    "tnv_046_vol_lt_half_504d_mean_flag": {"inputs": ["volume"], "func": tnv_046_vol_lt_half_504d_mean_flag},
    "tnv_047_high_turnover_days_count_252d": {"inputs": ["volume"], "func": tnv_047_high_turnover_days_count_252d},
    "tnv_048_high_turnover_days_count_504d": {"inputs": ["volume"], "func": tnv_048_high_turnover_days_count_504d},
    "tnv_049_low_turnover_days_count_252d": {"inputs": ["volume"], "func": tnv_049_low_turnover_days_count_252d},
    "tnv_050_low_turnover_days_count_504d": {"inputs": ["volume"], "func": tnv_050_low_turnover_days_count_504d},
    "tnv_051_mean_252d_vs_504d_turnover_ratio": {"inputs": ["volume"], "func": tnv_051_mean_252d_vs_504d_turnover_ratio},
    "tnv_052_mean_252d_vs_756d_turnover_ratio": {"inputs": ["volume"], "func": tnv_052_mean_252d_vs_756d_turnover_ratio},
    "tnv_053_mean_126d_vs_504d_turnover_ratio": {"inputs": ["volume"], "func": tnv_053_mean_126d_vs_504d_turnover_ratio},
    "tnv_054_mean_63d_vs_252d_turnover_ratio": {"inputs": ["volume"], "func": tnv_054_mean_63d_vs_252d_turnover_ratio},
    "tnv_055_mean_21d_vs_252d_turnover_ratio": {"inputs": ["volume"], "func": tnv_055_mean_21d_vs_252d_turnover_ratio},
    "tnv_056_mean_21d_vs_504d_turnover_ratio": {"inputs": ["volume"], "func": tnv_056_mean_21d_vs_504d_turnover_ratio},
    "tnv_057_std_vol_252d_vs_mean_vol_252d": {"inputs": ["volume"], "func": tnv_057_std_vol_252d_vs_mean_vol_252d},
    "tnv_058_std_vol_504d_vs_mean_vol_504d": {"inputs": ["volume"], "func": tnv_058_std_vol_504d_vs_mean_vol_504d},
    "tnv_059_log_mean_vol_252d": {"inputs": ["volume"], "func": tnv_059_log_mean_vol_252d},
    "tnv_060_log_mean_vol_504d": {"inputs": ["volume"], "func": tnv_060_log_mean_vol_504d},
    "tnv_061_turnover_proxy_252d_zscore_504d": {"inputs": ["volume"], "func": tnv_061_turnover_proxy_252d_zscore_504d},
    "tnv_062_turnover_proxy_252d_pct_rank_252d": {"inputs": ["volume"], "func": tnv_062_turnover_proxy_252d_pct_rank_252d},
    "tnv_063_turnover_proxy_504d_pct_rank_504d": {"inputs": ["volume"], "func": tnv_063_turnover_proxy_504d_pct_rank_504d},
    "tnv_064_vol_pct_rank_252d_21d_diff": {"inputs": ["volume"], "func": tnv_064_vol_pct_rank_252d_21d_diff},
    "tnv_065_vol_pct_rank_504d_expanding": {"inputs": ["volume"], "func": tnv_065_vol_pct_rank_504d_expanding},
    "tnv_066_turnover_extremity_score_252d": {"inputs": ["volume"], "func": tnv_066_turnover_extremity_score_252d},
    "tnv_067_turnover_extremity_score_504d": {"inputs": ["volume"], "func": tnv_067_turnover_extremity_score_504d},
    "tnv_068_vol_pct_rank_756d_expanding": {"inputs": ["volume"], "func": tnv_068_vol_pct_rank_756d_expanding},
    "tnv_069_consecutive_above_252d_mean": {"inputs": ["volume"], "func": tnv_069_consecutive_above_252d_mean},
    "tnv_070_consecutive_below_252d_mean": {"inputs": ["volume"], "func": tnv_070_consecutive_below_252d_mean},
    "tnv_071_consecutive_below_504d_mean": {"inputs": ["volume"], "func": tnv_071_consecutive_below_504d_mean},
    "tnv_072_high_turnover_fraction_252d": {"inputs": ["volume"], "func": tnv_072_high_turnover_fraction_252d},
    "tnv_073_low_turnover_fraction_252d": {"inputs": ["volume"], "func": tnv_073_low_turnover_fraction_252d},
    "tnv_074_high_turnover_fraction_504d": {"inputs": ["volume"], "func": tnv_074_high_turnover_fraction_504d},
    "tnv_075_turnover_composite_extremity_score": {"inputs": ["volume"], "func": tnv_075_turnover_composite_extremity_score},
}
