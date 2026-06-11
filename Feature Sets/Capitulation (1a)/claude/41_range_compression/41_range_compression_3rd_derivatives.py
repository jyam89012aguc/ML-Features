"""
41_range_compression — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative range-compression features — acceleration
        of squeeze velocity, jerk in ATR contraction, curvature of BB-width trend.
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


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


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

def rcp_drv3_001_tr_ratio_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR/21d_mean ratio (acceleration of compression velocity)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_002_atr21_vs_atr63_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR21/ATR63 ratio (jerk in short-vs-medium compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_003_bb_width_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Bollinger Band width (BB squeeze acceleration)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    vel = bw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_004_bb_squeeze_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of BB-vs-KC squeeze score (jerk in squeeze deepening)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    score = _safe_div(2.0 * s, m) - _safe_div(2.0 * atr21, m)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_005_narrowing_tr_streak_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive narrowing-TR streak (acceleration of coil building)."""
    tr = _tr(close, high, low)
    streak = _consec_streak(tr < tr.shift(1))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_006_atr21_zscore_252d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR21 z-score (acceleration of compression extremity)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mu = _rolling_mean(atr21, _TD_YEAR)
    sigma = _rolling_std(atr21, _TD_YEAR)
    z = _safe_div(atr21 - mu, sigma)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_007_atr21_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of ATR21 over 63 days (rate of slope change)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    slp = _linslope(atr21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rcp_drv3_008_bb_width_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of BB width over 21 days (curvature of BB squeeze)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    slp = _linslope(bw, _TD_MON)
    return slp.diff(_TD_WEEK)


def rcp_drv3_009_atr_composite_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-window ATR compression composite."""
    tr = _tr(close, high, low)
    r1 = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    r2 = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    r3 = _safe_div(_rolling_mean(tr, _TD_QTR), _rolling_mean(tr, _TD_YEAR))
    composite = (r1 + r2 + r3) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_010_tr_pct_rank_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR 252-day percentile rank (rank compression acceleration)."""
    tr = _tr(close, high, low)
    rank = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_011_keltner_width_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of Keltner Channel width (ATR-channel compression jerk)."""
    tr = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    mid = _rolling_mean(close, _TD_MON)
    kw = _safe_div(2.0 * atr, mid)
    vel = kw.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_012_coil_tightness_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR coefficient-of-variation over 21d (tightness acceleration)."""
    tr = _tr(close, high, low)
    cv = _safe_div(_rolling_std(tr, _TD_MON), _rolling_mean(tr, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_013_bb_width_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in BB width (jerk in monthly squeeze velocity)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    vel21 = bw.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rcp_drv3_014_atr21_vs_atr252_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in ATR21/ATR252 ratio."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rcp_drv3_015_nr4_count_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day NR4 count (acceleration of narrow-day clustering)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = (rng < prev_max).astype(float)
    count21 = nr4.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vel = count21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_016_tr_zscore_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR z-score vs 21-day distribution (extremity acceleration)."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_MON)
    s = _rolling_std(tr, _TD_MON)
    z = _safe_div(tr - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_017_consec_bb_squeeze_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of BB-squeeze streak length (squeeze streak acceleration)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    cond = 2.0 * s < 2.0 * atr21
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_018_hl_channel_contraction_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d/21d HL channel ratio (channel contraction jerk)."""
    h5 = _rolling_max(high, _TD_WEEK)
    l5 = _rolling_min(low, _TD_WEEK)
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    ratio = _safe_div(h5 - l5, h21 - l21)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_019_atr5_vs_atr21_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in ATR5/ATR21 ratio."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rcp_drv3_020_tr_collapse_ratio_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in TR/21d_peak ratio (collapse jerk)."""
    tr = _tr(close, high, low)
    peak21 = tr.shift(1).rolling(_TD_MON, min_periods=1).max()
    ratio = _safe_div(tr, peak21)
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rcp_drv3_021_bb_width_pct_rank_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of BB-width 252-day percentile rank (rank acceleration)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    rank = bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_022_tr_min_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of trailing 21-day minimum TR (floor acceleration)."""
    tr = _tr(close, high, low)
    mn = _rolling_min(tr, _TD_MON)
    vel = mn.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rcp_drv3_023_atr21_slope_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 63-day OLS slope of ATR21 (slope of slope)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    slp63 = _linslope(atr21, _TD_QTR)
    return _linslope(slp63, _TD_MON)


def rcp_drv3_024_bb_width_slope_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day OLS slope of BB width (curvature)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    slp21 = _linslope(bw, _TD_MON)
    return _linslope(slp21, _TD_MON)


def rcp_drv3_025_squeeze_distress_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of composite squeeze distress score (distress jerk)."""
    tr = _tr(close, high, low)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    bw_rank = bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    tr_rank = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    composite = (tr_rank + bw_rank + atr_ratio) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_REGISTRY_3RD_DERIVATIVES = {
    "rcp_drv3_001_tr_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_001_tr_ratio_21d_5d_diff_5d_diff},
    "rcp_drv3_002_atr21_vs_atr63_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_002_atr21_vs_atr63_5d_diff_5d_diff},
    "rcp_drv3_003_bb_width_5d_diff_5d_diff": {"inputs": ["close"], "func": rcp_drv3_003_bb_width_5d_diff_5d_diff},
    "rcp_drv3_004_bb_squeeze_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_004_bb_squeeze_score_5d_diff_5d_diff},
    "rcp_drv3_005_narrowing_tr_streak_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_005_narrowing_tr_streak_5d_diff_5d_diff},
    "rcp_drv3_006_atr21_zscore_252d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_006_atr21_zscore_252d_5d_diff_5d_diff},
    "rcp_drv3_007_atr21_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_007_atr21_slope_5d_diff},
    "rcp_drv3_008_bb_width_slope_5d_diff": {"inputs": ["close"], "func": rcp_drv3_008_bb_width_slope_5d_diff},
    "rcp_drv3_009_atr_composite_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_009_atr_composite_5d_diff_5d_diff},
    "rcp_drv3_010_tr_pct_rank_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_010_tr_pct_rank_5d_diff_5d_diff},
    "rcp_drv3_011_keltner_width_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_011_keltner_width_5d_diff_5d_diff},
    "rcp_drv3_012_coil_tightness_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_012_coil_tightness_5d_diff_5d_diff},
    "rcp_drv3_013_bb_width_21d_diff_5d_diff": {"inputs": ["close"], "func": rcp_drv3_013_bb_width_21d_diff_5d_diff},
    "rcp_drv3_014_atr21_vs_atr252_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_014_atr21_vs_atr252_21d_diff_5d_diff},
    "rcp_drv3_015_nr4_count_21d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rcp_drv3_015_nr4_count_21d_5d_diff_5d_diff},
    "rcp_drv3_016_tr_zscore_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_016_tr_zscore_21d_5d_diff_5d_diff},
    "rcp_drv3_017_consec_bb_squeeze_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_017_consec_bb_squeeze_5d_diff_5d_diff},
    "rcp_drv3_018_hl_channel_contraction_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_018_hl_channel_contraction_5d_diff_5d_diff},
    "rcp_drv3_019_atr5_vs_atr21_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_019_atr5_vs_atr21_21d_diff_5d_diff},
    "rcp_drv3_020_tr_collapse_ratio_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_020_tr_collapse_ratio_21d_diff_5d_diff},
    "rcp_drv3_021_bb_width_pct_rank_5d_diff_5d_diff": {"inputs": ["close"], "func": rcp_drv3_021_bb_width_pct_rank_5d_diff_5d_diff},
    "rcp_drv3_022_tr_min_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv3_022_tr_min_21d_5d_diff_5d_diff},
    "rcp_drv3_023_atr21_slope_slope_21d": {"inputs": ["close", "high", "low"], "func": rcp_drv3_023_atr21_slope_slope_21d},
    "rcp_drv3_024_bb_width_slope_slope_21d": {"inputs": ["close"], "func": rcp_drv3_024_bb_width_slope_slope_21d},
    "rcp_drv3_025_squeeze_distress_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rcp_drv3_025_squeeze_distress_5d_diff_5d_diff},
}
