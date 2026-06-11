"""
26_rsi_extremes — Base Features 001-075
Domain: RSI oversold readings — depth and duration of RSI extremes
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder smoothed RSI for a given lookback period."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_sma(close: pd.Series, period: int) -> pd.Series:
    """Simple-average RSI (Cutler variant) for a given lookback."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = _rolling_mean(gain, period)
    avg_loss = _rolling_mean(loss, period)
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw RSI at multiple lookbacks ---

def rsi_001_rsi14(close: pd.Series) -> pd.Series:
    """Wilder RSI with 14-day lookback (standard RSI)."""
    return _rsi(close, 14)


def rsi_002_rsi7(close: pd.Series) -> pd.Series:
    """Wilder RSI with 7-day lookback (fast / sensitive)."""
    return _rsi(close, 7)


def rsi_003_rsi21(close: pd.Series) -> pd.Series:
    """Wilder RSI with 21-day lookback (monthly)."""
    return _rsi(close, _TD_MON)


def rsi_004_rsi63(close: pd.Series) -> pd.Series:
    """Wilder RSI with 63-day lookback (quarterly)."""
    return _rsi(close, _TD_QTR)


def rsi_005_rsi2(close: pd.Series) -> pd.Series:
    """Wilder RSI with 2-day lookback (Connors ultra-short RSI base)."""
    return _rsi(close, 2)


def rsi_006_rsi3(close: pd.Series) -> pd.Series:
    """Wilder RSI with 3-day lookback."""
    return _rsi(close, 3)


def rsi_007_rsi5(close: pd.Series) -> pd.Series:
    """Wilder RSI with 5-day lookback (weekly)."""
    return _rsi(close, _TD_WEEK)


def rsi_008_rsi9(close: pd.Series) -> pd.Series:
    """Wilder RSI with 9-day lookback."""
    return _rsi(close, 9)


def rsi_009_rsi28(close: pd.Series) -> pd.Series:
    """Wilder RSI with 28-day lookback."""
    return _rsi(close, 28)


def rsi_010_rsi126(close: pd.Series) -> pd.Series:
    """Wilder RSI with 126-day lookback (half-year)."""
    return _rsi(close, _TD_HALF)


# --- Group B (011-020): Oversold depth — distance below thresholds ---

def rsi_011_rsi14_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of RSI14 below the 30 oversold threshold (0 when above)."""
    r = _rsi(close, 14)
    return (30.0 - r).clip(lower=0.0)


def rsi_012_rsi14_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of RSI14 below the 20 extreme oversold threshold."""
    r = _rsi(close, 14)
    return (20.0 - r).clip(lower=0.0)


def rsi_013_rsi14_depth_below10(close: pd.Series) -> pd.Series:
    """Depth of RSI14 below the 10 capitulation threshold."""
    r = _rsi(close, 14)
    return (10.0 - r).clip(lower=0.0)


def rsi_014_rsi7_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of RSI7 below 30 (fast oversold reading)."""
    r = _rsi(close, 7)
    return (30.0 - r).clip(lower=0.0)


def rsi_015_rsi7_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of RSI7 below 20."""
    r = _rsi(close, 7)
    return (20.0 - r).clip(lower=0.0)


def rsi_016_rsi21_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of RSI21 below 30."""
    r = _rsi(close, _TD_MON)
    return (30.0 - r).clip(lower=0.0)


def rsi_017_rsi21_depth_below40(close: pd.Series) -> pd.Series:
    """Depth of RSI21 below 40 (mild oversold on slow RSI)."""
    r = _rsi(close, _TD_MON)
    return (40.0 - r).clip(lower=0.0)


def rsi_018_rsi63_depth_below40(close: pd.Series) -> pd.Series:
    """Depth of RSI63 below 40 (quarterly RSI oversold zone)."""
    r = _rsi(close, _TD_QTR)
    return (40.0 - r).clip(lower=0.0)


def rsi_019_rsi63_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of RSI63 below 30."""
    r = _rsi(close, _TD_QTR)
    return (30.0 - r).clip(lower=0.0)


def rsi_020_rsi14_distance_from_midpoint(close: pd.Series) -> pd.Series:
    """RSI14 distance from the 50-midpoint (negative = oversold side)."""
    return _rsi(close, 14) - 50.0


# --- Group C (021-030): Consecutive days RSI below thresholds ---

def rsi_021_consec_days_rsi14_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 has been below 30."""
    return _consec_streak(_rsi(close, 14) < 30.0)


def rsi_022_consec_days_rsi14_below20(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 has been below 20."""
    return _consec_streak(_rsi(close, 14) < 20.0)


def rsi_023_consec_days_rsi14_below10(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 has been below 10."""
    return _consec_streak(_rsi(close, 14) < 10.0)


def rsi_024_consec_days_rsi7_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI7 has been below 30."""
    return _consec_streak(_rsi(close, 7) < 30.0)


def rsi_025_consec_days_rsi7_below20(close: pd.Series) -> pd.Series:
    """Consecutive days RSI7 has been below 20."""
    return _consec_streak(_rsi(close, 7) < 20.0)


def rsi_026_consec_days_rsi21_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI21 has been below 30."""
    return _consec_streak(_rsi(close, _TD_MON) < 30.0)


def rsi_027_consec_days_rsi21_below40(close: pd.Series) -> pd.Series:
    """Consecutive days RSI21 has been below 40."""
    return _consec_streak(_rsi(close, _TD_MON) < 40.0)


def rsi_028_consec_days_rsi63_below40(close: pd.Series) -> pd.Series:
    """Consecutive days RSI63 has been below 40."""
    return _consec_streak(_rsi(close, _TD_QTR) < 40.0)


def rsi_029_consec_days_rsi63_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI63 has been below 30."""
    return _consec_streak(_rsi(close, _TD_QTR) < 30.0)


def rsi_030_consec_days_rsi14_below50(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 has been below 50 (general weakness streak)."""
    return _consec_streak(_rsi(close, 14) < 50.0)


# --- Group D (031-040): Rolling minimum RSI over windows ---

def rsi_031_rsi14_min_21d(close: pd.Series) -> pd.Series:
    """Minimum RSI14 over trailing 21 days."""
    return _rolling_min(_rsi(close, 14), _TD_MON)


def rsi_032_rsi14_min_63d(close: pd.Series) -> pd.Series:
    """Minimum RSI14 over trailing 63 days."""
    return _rolling_min(_rsi(close, 14), _TD_QTR)


def rsi_033_rsi14_min_252d(close: pd.Series) -> pd.Series:
    """Minimum RSI14 over trailing 252 days."""
    return _rolling_min(_rsi(close, 14), _TD_YEAR)


def rsi_034_rsi7_min_21d(close: pd.Series) -> pd.Series:
    """Minimum RSI7 over trailing 21 days."""
    return _rolling_min(_rsi(close, 7), _TD_MON)


def rsi_035_rsi7_min_63d(close: pd.Series) -> pd.Series:
    """Minimum RSI7 over trailing 63 days."""
    return _rolling_min(_rsi(close, 7), _TD_QTR)


def rsi_036_rsi21_min_63d(close: pd.Series) -> pd.Series:
    """Minimum RSI21 over trailing 63 days."""
    return _rolling_min(_rsi(close, _TD_MON), _TD_QTR)


def rsi_037_rsi21_min_252d(close: pd.Series) -> pd.Series:
    """Minimum RSI21 over trailing 252 days."""
    return _rolling_min(_rsi(close, _TD_MON), _TD_YEAR)


def rsi_038_rsi63_min_252d(close: pd.Series) -> pd.Series:
    """Minimum RSI63 over trailing 252 days."""
    return _rolling_min(_rsi(close, _TD_QTR), _TD_YEAR)


def rsi_039_rsi14_expanding_min(close: pd.Series) -> pd.Series:
    """All-time expanding minimum of RSI14 (how extreme has RSI ever gotten)."""
    return _rsi(close, 14).expanding(min_periods=14).min()


def rsi_040_rsi14_current_vs_min_252d(close: pd.Series) -> pd.Series:
    """RSI14 as fraction of its 252-day minimum (1.0 = at the lowest)."""
    r = _rsi(close, 14)
    mn = _rolling_min(r, _TD_YEAR)
    return _safe_div(r, mn.clip(lower=_EPS))


# --- Group E (041-050): RSI percentile rank ---

def rsi_041_rsi14_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI14 within trailing 63-day distribution."""
    r = _rsi(close, 14)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rsi_042_rsi14_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI14 within trailing 252-day distribution."""
    r = _rsi(close, 14)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_043_rsi7_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI7 within trailing 63-day distribution."""
    r = _rsi(close, 7)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rsi_044_rsi7_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI7 within trailing 252-day distribution."""
    r = _rsi(close, 7)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_045_rsi21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI21 within trailing 252-day distribution."""
    r = _rsi(close, _TD_MON)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_046_rsi63_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI63 within trailing 252-day distribution."""
    r = _rsi(close, _TD_QTR)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_047_rsi14_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of RSI14."""
    r = _rsi(close, 14)
    return r.expanding(min_periods=14).rank(pct=True)


def rsi_048_rsi14_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of RSI14 relative to its 252-day distribution."""
    r = _rsi(close, 14)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rsi_049_rsi7_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of RSI7 relative to its 252-day distribution."""
    r = _rsi(close, 7)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rsi_050_rsi14_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of RSI14 relative to its 63-day distribution."""
    r = _rsi(close, 14)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(r - m, s)


# --- Group F (051-060): Binary oversold flags ---

def rsi_051_rsi14_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI14 < 30 (oversold)."""
    return (_rsi(close, 14) < 30.0).astype(float)


def rsi_052_rsi14_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI14 < 20 (deeply oversold)."""
    return (_rsi(close, 14) < 20.0).astype(float)


def rsi_053_rsi14_below10_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI14 < 10 (extreme capitulation level)."""
    return (_rsi(close, 14) < 10.0).astype(float)


def rsi_054_rsi7_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI7 < 30."""
    return (_rsi(close, 7) < 30.0).astype(float)


def rsi_055_rsi7_below20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI7 < 20."""
    return (_rsi(close, 7) < 20.0).astype(float)


def rsi_056_rsi21_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI21 < 30."""
    return (_rsi(close, _TD_MON) < 30.0).astype(float)


def rsi_057_rsi63_below40_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI63 < 40 (slow RSI in bear territory)."""
    return (_rsi(close, _TD_QTR) < 40.0).astype(float)


def rsi_058_all_rsi_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI7, RSI14, and RSI21 all below 30 simultaneously."""
    r7 = _rsi(close, 7)
    r14 = _rsi(close, 14)
    r21 = _rsi(close, _TD_MON)
    return ((r7 < 30.0) & (r14 < 30.0) & (r21 < 30.0)).astype(float)


def rsi_059_rsi14_new_low_21d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's RSI14 is the lowest in the trailing 21 days."""
    r = _rsi(close, 14)
    prev_min = r.shift(1).rolling(_TD_MON, min_periods=1).min()
    return (r < prev_min).astype(float)


def rsi_060_rsi14_new_low_63d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's RSI14 is the lowest in the trailing 63 days."""
    r = _rsi(close, 14)
    prev_min = r.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (r < prev_min).astype(float)


# --- Group G (061-075): Oversold count in windows, time-since-extreme ---

def rsi_061_days_rsi14_below30_in_21d(close: pd.Series) -> pd.Series:
    """Count of days RSI14 < 30 in trailing 21 days."""
    return _rolling_sum((_rsi(close, 14) < 30.0).astype(float), _TD_MON)


def rsi_062_days_rsi14_below30_in_63d(close: pd.Series) -> pd.Series:
    """Count of days RSI14 < 30 in trailing 63 days."""
    return _rolling_sum((_rsi(close, 14) < 30.0).astype(float), _TD_QTR)


def rsi_063_days_rsi14_below30_in_252d(close: pd.Series) -> pd.Series:
    """Count of days RSI14 < 30 in trailing 252 days."""
    return _rolling_sum((_rsi(close, 14) < 30.0).astype(float), _TD_YEAR)


def rsi_064_days_rsi14_below20_in_63d(close: pd.Series) -> pd.Series:
    """Count of days RSI14 < 20 in trailing 63 days."""
    return _rolling_sum((_rsi(close, 14) < 20.0).astype(float), _TD_QTR)


def rsi_065_days_rsi7_below30_in_21d(close: pd.Series) -> pd.Series:
    """Count of days RSI7 < 30 in trailing 21 days."""
    return _rolling_sum((_rsi(close, 7) < 30.0).astype(float), _TD_MON)


def rsi_066_days_rsi7_below20_in_63d(close: pd.Series) -> pd.Series:
    """Count of days RSI7 < 20 in trailing 63 days."""
    return _rolling_sum((_rsi(close, 7) < 20.0).astype(float), _TD_QTR)


def rsi_067_days_rsi21_below30_in_252d(close: pd.Series) -> pd.Series:
    """Count of days RSI21 < 30 in trailing 252 days."""
    return _rolling_sum((_rsi(close, _TD_MON) < 30.0).astype(float), _TD_YEAR)


def rsi_068_fraction_rsi14_below30_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where RSI14 < 30."""
    cnt = _rolling_sum((_rsi(close, 14) < 30.0).astype(float), _TD_QTR)
    return cnt / _TD_QTR


def rsi_069_fraction_rsi14_below30_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where RSI14 < 30."""
    cnt = _rolling_sum((_rsi(close, 14) < 30.0).astype(float), _TD_YEAR)
    return cnt / _TD_YEAR


def rsi_070_time_since_rsi14_last_below30(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI14 was last below 30 (0 = currently below)."""
    r = _rsi(close, 14)
    below = (r < 30.0).astype(float)
    idx = below * pd.Series(range(len(below)), index=below.index)
    last_idx = idx.where(below == 1.0).ffill().fillna(0)
    elapsed = pd.Series(range(len(below)), index=below.index) - last_idx
    return elapsed.where(~below.isna(), np.nan)


def rsi_071_time_since_rsi14_last_below20(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI14 was last below 20."""
    r = _rsi(close, 14)
    below = (r < 20.0).astype(float)
    idx = pd.Series(range(len(below)), index=below.index, dtype=float)
    last_idx = idx.where(below == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~r.isna(), np.nan)


def rsi_072_time_since_rsi7_last_below20(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI7 was last below 20."""
    r = _rsi(close, 7)
    below = (r < 20.0).astype(float)
    idx = pd.Series(range(len(below)), index=below.index, dtype=float)
    last_idx = idx.where(below == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~r.isna(), np.nan)


def rsi_073_rsi14_below30_frac_norm_252d(close: pd.Series) -> pd.Series:
    """21-day oversold fraction normalized by 252-day average oversold fraction."""
    r = _rsi(close, 14)
    flag = (r < 30.0).astype(float)
    frac21 = _rolling_sum(flag, _TD_MON) / _TD_MON
    avg252 = _rolling_mean(frac21, _TD_YEAR)
    return _safe_div(frac21, avg252.clip(lower=_EPS))


def rsi_074_rsi14_oversold_intensity_21d(close: pd.Series) -> pd.Series:
    """Sum of oversold depth (30 - RSI14, clipped to 0) over trailing 21 days."""
    depth = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    return _rolling_sum(depth, _TD_MON)


def rsi_075_rsi14_oversold_intensity_63d(close: pd.Series) -> pd.Series:
    """Sum of oversold depth (30 - RSI14, clipped to 0) over trailing 63 days."""
    depth = (30.0 - _rsi(close, 14)).clip(lower=0.0)
    return _rolling_sum(depth, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

RSI_EXTREMES_REGISTRY_001_075 = {
    "rsi_001_rsi14": {"inputs": ["close"], "func": rsi_001_rsi14},
    "rsi_002_rsi7": {"inputs": ["close"], "func": rsi_002_rsi7},
    "rsi_003_rsi21": {"inputs": ["close"], "func": rsi_003_rsi21},
    "rsi_004_rsi63": {"inputs": ["close"], "func": rsi_004_rsi63},
    "rsi_005_rsi2": {"inputs": ["close"], "func": rsi_005_rsi2},
    "rsi_006_rsi3": {"inputs": ["close"], "func": rsi_006_rsi3},
    "rsi_007_rsi5": {"inputs": ["close"], "func": rsi_007_rsi5},
    "rsi_008_rsi9": {"inputs": ["close"], "func": rsi_008_rsi9},
    "rsi_009_rsi28": {"inputs": ["close"], "func": rsi_009_rsi28},
    "rsi_010_rsi126": {"inputs": ["close"], "func": rsi_010_rsi126},
    "rsi_011_rsi14_depth_below30": {"inputs": ["close"], "func": rsi_011_rsi14_depth_below30},
    "rsi_012_rsi14_depth_below20": {"inputs": ["close"], "func": rsi_012_rsi14_depth_below20},
    "rsi_013_rsi14_depth_below10": {"inputs": ["close"], "func": rsi_013_rsi14_depth_below10},
    "rsi_014_rsi7_depth_below30": {"inputs": ["close"], "func": rsi_014_rsi7_depth_below30},
    "rsi_015_rsi7_depth_below20": {"inputs": ["close"], "func": rsi_015_rsi7_depth_below20},
    "rsi_016_rsi21_depth_below30": {"inputs": ["close"], "func": rsi_016_rsi21_depth_below30},
    "rsi_017_rsi21_depth_below40": {"inputs": ["close"], "func": rsi_017_rsi21_depth_below40},
    "rsi_018_rsi63_depth_below40": {"inputs": ["close"], "func": rsi_018_rsi63_depth_below40},
    "rsi_019_rsi63_depth_below30": {"inputs": ["close"], "func": rsi_019_rsi63_depth_below30},
    "rsi_020_rsi14_distance_from_midpoint": {"inputs": ["close"], "func": rsi_020_rsi14_distance_from_midpoint},
    "rsi_021_consec_days_rsi14_below30": {"inputs": ["close"], "func": rsi_021_consec_days_rsi14_below30},
    "rsi_022_consec_days_rsi14_below20": {"inputs": ["close"], "func": rsi_022_consec_days_rsi14_below20},
    "rsi_023_consec_days_rsi14_below10": {"inputs": ["close"], "func": rsi_023_consec_days_rsi14_below10},
    "rsi_024_consec_days_rsi7_below30": {"inputs": ["close"], "func": rsi_024_consec_days_rsi7_below30},
    "rsi_025_consec_days_rsi7_below20": {"inputs": ["close"], "func": rsi_025_consec_days_rsi7_below20},
    "rsi_026_consec_days_rsi21_below30": {"inputs": ["close"], "func": rsi_026_consec_days_rsi21_below30},
    "rsi_027_consec_days_rsi21_below40": {"inputs": ["close"], "func": rsi_027_consec_days_rsi21_below40},
    "rsi_028_consec_days_rsi63_below40": {"inputs": ["close"], "func": rsi_028_consec_days_rsi63_below40},
    "rsi_029_consec_days_rsi63_below30": {"inputs": ["close"], "func": rsi_029_consec_days_rsi63_below30},
    "rsi_030_consec_days_rsi14_below50": {"inputs": ["close"], "func": rsi_030_consec_days_rsi14_below50},
    "rsi_031_rsi14_min_21d": {"inputs": ["close"], "func": rsi_031_rsi14_min_21d},
    "rsi_032_rsi14_min_63d": {"inputs": ["close"], "func": rsi_032_rsi14_min_63d},
    "rsi_033_rsi14_min_252d": {"inputs": ["close"], "func": rsi_033_rsi14_min_252d},
    "rsi_034_rsi7_min_21d": {"inputs": ["close"], "func": rsi_034_rsi7_min_21d},
    "rsi_035_rsi7_min_63d": {"inputs": ["close"], "func": rsi_035_rsi7_min_63d},
    "rsi_036_rsi21_min_63d": {"inputs": ["close"], "func": rsi_036_rsi21_min_63d},
    "rsi_037_rsi21_min_252d": {"inputs": ["close"], "func": rsi_037_rsi21_min_252d},
    "rsi_038_rsi63_min_252d": {"inputs": ["close"], "func": rsi_038_rsi63_min_252d},
    "rsi_039_rsi14_expanding_min": {"inputs": ["close"], "func": rsi_039_rsi14_expanding_min},
    "rsi_040_rsi14_current_vs_min_252d": {"inputs": ["close"], "func": rsi_040_rsi14_current_vs_min_252d},
    "rsi_041_rsi14_pct_rank_63d": {"inputs": ["close"], "func": rsi_041_rsi14_pct_rank_63d},
    "rsi_042_rsi14_pct_rank_252d": {"inputs": ["close"], "func": rsi_042_rsi14_pct_rank_252d},
    "rsi_043_rsi7_pct_rank_63d": {"inputs": ["close"], "func": rsi_043_rsi7_pct_rank_63d},
    "rsi_044_rsi7_pct_rank_252d": {"inputs": ["close"], "func": rsi_044_rsi7_pct_rank_252d},
    "rsi_045_rsi21_pct_rank_252d": {"inputs": ["close"], "func": rsi_045_rsi21_pct_rank_252d},
    "rsi_046_rsi63_pct_rank_252d": {"inputs": ["close"], "func": rsi_046_rsi63_pct_rank_252d},
    "rsi_047_rsi14_expanding_pct_rank": {"inputs": ["close"], "func": rsi_047_rsi14_expanding_pct_rank},
    "rsi_048_rsi14_zscore_252d": {"inputs": ["close"], "func": rsi_048_rsi14_zscore_252d},
    "rsi_049_rsi7_zscore_252d": {"inputs": ["close"], "func": rsi_049_rsi7_zscore_252d},
    "rsi_050_rsi14_zscore_63d": {"inputs": ["close"], "func": rsi_050_rsi14_zscore_63d},
    "rsi_051_rsi14_below30_flag": {"inputs": ["close"], "func": rsi_051_rsi14_below30_flag},
    "rsi_052_rsi14_below20_flag": {"inputs": ["close"], "func": rsi_052_rsi14_below20_flag},
    "rsi_053_rsi14_below10_flag": {"inputs": ["close"], "func": rsi_053_rsi14_below10_flag},
    "rsi_054_rsi7_below30_flag": {"inputs": ["close"], "func": rsi_054_rsi7_below30_flag},
    "rsi_055_rsi7_below20_flag": {"inputs": ["close"], "func": rsi_055_rsi7_below20_flag},
    "rsi_056_rsi21_below30_flag": {"inputs": ["close"], "func": rsi_056_rsi21_below30_flag},
    "rsi_057_rsi63_below40_flag": {"inputs": ["close"], "func": rsi_057_rsi63_below40_flag},
    "rsi_058_all_rsi_below30_flag": {"inputs": ["close"], "func": rsi_058_all_rsi_below30_flag},
    "rsi_059_rsi14_new_low_21d_flag": {"inputs": ["close"], "func": rsi_059_rsi14_new_low_21d_flag},
    "rsi_060_rsi14_new_low_63d_flag": {"inputs": ["close"], "func": rsi_060_rsi14_new_low_63d_flag},
    "rsi_061_days_rsi14_below30_in_21d": {"inputs": ["close"], "func": rsi_061_days_rsi14_below30_in_21d},
    "rsi_062_days_rsi14_below30_in_63d": {"inputs": ["close"], "func": rsi_062_days_rsi14_below30_in_63d},
    "rsi_063_days_rsi14_below30_in_252d": {"inputs": ["close"], "func": rsi_063_days_rsi14_below30_in_252d},
    "rsi_064_days_rsi14_below20_in_63d": {"inputs": ["close"], "func": rsi_064_days_rsi14_below20_in_63d},
    "rsi_065_days_rsi7_below30_in_21d": {"inputs": ["close"], "func": rsi_065_days_rsi7_below30_in_21d},
    "rsi_066_days_rsi7_below20_in_63d": {"inputs": ["close"], "func": rsi_066_days_rsi7_below20_in_63d},
    "rsi_067_days_rsi21_below30_in_252d": {"inputs": ["close"], "func": rsi_067_days_rsi21_below30_in_252d},
    "rsi_068_fraction_rsi14_below30_63d": {"inputs": ["close"], "func": rsi_068_fraction_rsi14_below30_63d},
    "rsi_069_fraction_rsi14_below30_252d": {"inputs": ["close"], "func": rsi_069_fraction_rsi14_below30_252d},
    "rsi_070_time_since_rsi14_last_below30": {"inputs": ["close"], "func": rsi_070_time_since_rsi14_last_below30},
    "rsi_071_time_since_rsi14_last_below20": {"inputs": ["close"], "func": rsi_071_time_since_rsi14_last_below20},
    "rsi_072_time_since_rsi7_last_below20": {"inputs": ["close"], "func": rsi_072_time_since_rsi7_last_below20},
    "rsi_073_rsi14_below30_frac_norm_252d": {"inputs": ["close"], "func": rsi_073_rsi14_below30_frac_norm_252d},
    "rsi_074_rsi14_oversold_intensity_21d": {"inputs": ["close"], "func": rsi_074_rsi14_oversold_intensity_21d},
    "rsi_075_rsi14_oversold_intensity_63d": {"inputs": ["close"], "func": rsi_075_rsi14_oversold_intensity_63d},
}
