"""
41_range_compression — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base range-compression concepts — velocity / acceleration
        of squeeze tightening, ATR contraction speed, BB-width velocity, NR-streak growth.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rcp_drv2_001_tr_ratio_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR/21d_mean_TR ratio (velocity of compression into baseline)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    return ratio.diff(_TD_WEEK)


def rcp_drv2_002_tr_ratio_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of TR/21d_mean_TR ratio (monthly velocity of TR compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    return ratio.diff(_TD_MON)


def rcp_drv2_003_atr21_vs_atr63_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR21/ATR63 ratio (rapid short-vs-medium compression change)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def rcp_drv2_004_atr21_vs_atr252_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of ATR21/ATR252 ratio (monthly change in annual compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return ratio.diff(_TD_MON)


def rcp_drv2_005_bb_width_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day Bollinger Band width (squeeze tightening velocity)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return bw.diff(_TD_WEEK)


def rcp_drv2_006_bb_width_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day Bollinger Band width (monthly squeeze velocity)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return bw.diff(_TD_MON)


def rcp_drv2_007_bb_squeeze_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of BB-vs-KC squeeze score (rate of squeeze deepening)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    score = _safe_div(2.0 * s, m) - _safe_div(2.0 * atr21, m)
    return score.diff(_TD_WEEK)


def rcp_drv2_008_consec_narrowing_tr_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive narrowing-TR streak (streak growth velocity)."""
    tr = _tr(close, high, low)
    streak = _consec_streak(tr < tr.shift(1))
    return streak.diff(_TD_WEEK)


def rcp_drv2_009_nr4_count_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day NR4 count (how fast narrow days are accumulating)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = (rng < prev_max).astype(float)
    count21 = nr4.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return count21.diff(_TD_WEEK)


def rcp_drv2_010_tr_pct_rank_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR 252-day percentile rank (compression rank velocity)."""
    tr = _tr(close, high, low)
    rank = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(_TD_WEEK)


def rcp_drv2_011_atr21_zscore_252d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR21 z-score within 252-day distribution."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mu = _rolling_mean(atr21, _TD_YEAR)
    sigma = _rolling_std(atr21, _TD_YEAR)
    z = _safe_div(atr21 - mu, sigma)
    return z.diff(_TD_WEEK)


def rcp_drv2_012_bb_width_pct_rank_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of BB-width 252-day percentile rank."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    rank = bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return rank.diff(_TD_MON)


def rcp_drv2_013_keltner_width_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of Keltner Channel width (ATR-based channel compression velocity)."""
    tr = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    mid = _rolling_mean(close, _TD_MON)
    kw = _safe_div(2.0 * atr, mid)
    return kw.diff(_TD_WEEK)


def rcp_drv2_014_atr_compression_composite_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite ATR compression ratio (ATR5/21, ATR21/63, ATR63/252 avg)."""
    tr = _tr(close, high, low)
    r1 = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    r2 = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    r3 = _safe_div(_rolling_mean(tr, _TD_QTR), _rolling_mean(tr, _TD_YEAR))
    composite = (r1 + r2 + r3) / 3.0
    return composite.diff(_TD_WEEK)


def rcp_drv2_015_bb_width_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day BB width over trailing 21 days (trend in squeeze)."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return _linslope(bw, _TD_MON)


def rcp_drv2_016_atr21_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of ATR21 over trailing 63 days (trend in medium-term compression)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    return _linslope(atr21, _TD_QTR)


def rcp_drv2_017_tr_collapse_ratio_5d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of TR/21d_peak ratio (monthly change in collapse-from-peak depth)."""
    tr = _tr(close, high, low)
    peak21 = tr.shift(1).rolling(_TD_MON, min_periods=1).max()
    ratio = _safe_div(tr, peak21)
    return ratio.diff(_TD_MON)


def rcp_drv2_018_hl_channel_5d_vs_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5d/21d HL channel width ratio (short-term contraction velocity)."""
    h5 = _rolling_max(high, _TD_WEEK)
    l5 = _rolling_min(low, _TD_WEEK)
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    ratio = _safe_div(h5 - l5, h21 - l21)
    return ratio.diff(_TD_WEEK)


def rcp_drv2_019_coil_tightness_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR coefficient-of-variation over 21 days (tightness velocity)."""
    tr = _tr(close, high, low)
    cv = _safe_div(_rolling_std(tr, _TD_MON), _rolling_mean(tr, _TD_MON))
    return cv.diff(_TD_WEEK)


def rcp_drv2_020_tr_zscore_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR z-score relative to 21-day distribution."""
    tr = _tr(close, high, low)
    m = _rolling_mean(tr, _TD_MON)
    s = _rolling_std(tr, _TD_MON)
    z = _safe_div(tr - m, s)
    return z.diff(_TD_WEEK)


def rcp_drv2_021_consec_bb_squeeze_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive BB-squeeze streak length."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    cond = 2.0 * s < 2.0 * atr21
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


def rcp_drv2_022_atr5_vs_atr21_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of ATR5/ATR21 ratio (monthly change in ultra-short compression)."""
    tr = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    return ratio.diff(_TD_MON)


def rcp_drv2_023_tr_min_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of trailing 21-day minimum TR (how fast floor is dropping)."""
    tr = _tr(close, high, low)
    mn = _rolling_min(tr, _TD_MON)
    return mn.diff(_TD_WEEK)


def rcp_drv2_024_nr4_fraction_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day NR4 fraction (rate of narrow-day frequency change)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = (rng < prev_max).astype(float)
    frac21 = nr4.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return frac21.diff(_TD_WEEK)


def rcp_drv2_025_squeeze_distress_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of BB-width/252d_rank composite — squeeze rank velocity."""
    tr = _tr(close, high, low)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    bw_rank = bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    tr_rank = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    composite = (tr_rank + bw_rank + atr_ratio) / 3.0
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_REGISTRY_2ND_DERIVATIVES = {
    "rcp_drv2_001_tr_ratio_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_001_tr_ratio_21d_5d_diff},
    "rcp_drv2_002_tr_ratio_21d_21d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_002_tr_ratio_21d_21d_diff},
    "rcp_drv2_003_atr21_vs_atr63_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_003_atr21_vs_atr63_5d_diff},
    "rcp_drv2_004_atr21_vs_atr252_21d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_004_atr21_vs_atr252_21d_diff},
    "rcp_drv2_005_bb_width_21d_5d_diff": {"inputs": ["close"], "func": rcp_drv2_005_bb_width_21d_5d_diff},
    "rcp_drv2_006_bb_width_21d_21d_diff": {"inputs": ["close"], "func": rcp_drv2_006_bb_width_21d_21d_diff},
    "rcp_drv2_007_bb_squeeze_score_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_007_bb_squeeze_score_5d_diff},
    "rcp_drv2_008_consec_narrowing_tr_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_008_consec_narrowing_tr_5d_diff},
    "rcp_drv2_009_nr4_count_21d_5d_diff": {"inputs": ["high", "low"], "func": rcp_drv2_009_nr4_count_21d_5d_diff},
    "rcp_drv2_010_tr_pct_rank_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_010_tr_pct_rank_252d_5d_diff},
    "rcp_drv2_011_atr21_zscore_252d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_011_atr21_zscore_252d_5d_diff},
    "rcp_drv2_012_bb_width_pct_rank_21d_diff": {"inputs": ["close"], "func": rcp_drv2_012_bb_width_pct_rank_21d_diff},
    "rcp_drv2_013_keltner_width_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_013_keltner_width_21d_5d_diff},
    "rcp_drv2_014_atr_compression_composite_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_014_atr_compression_composite_5d_diff},
    "rcp_drv2_015_bb_width_slope_21d": {"inputs": ["close"], "func": rcp_drv2_015_bb_width_slope_21d},
    "rcp_drv2_016_atr21_slope_63d": {"inputs": ["close", "high", "low"], "func": rcp_drv2_016_atr21_slope_63d},
    "rcp_drv2_017_tr_collapse_ratio_5d_21d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_017_tr_collapse_ratio_5d_21d_diff},
    "rcp_drv2_018_hl_channel_5d_vs_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_018_hl_channel_5d_vs_21d_5d_diff},
    "rcp_drv2_019_coil_tightness_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_019_coil_tightness_21d_5d_diff},
    "rcp_drv2_020_tr_zscore_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_020_tr_zscore_21d_5d_diff},
    "rcp_drv2_021_consec_bb_squeeze_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_021_consec_bb_squeeze_5d_diff},
    "rcp_drv2_022_atr5_vs_atr21_21d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_022_atr5_vs_atr21_21d_diff},
    "rcp_drv2_023_tr_min_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rcp_drv2_023_tr_min_21d_5d_diff},
    "rcp_drv2_024_nr4_fraction_21d_5d_diff": {"inputs": ["high", "low"], "func": rcp_drv2_024_nr4_fraction_21d_5d_diff},
    "rcp_drv2_025_squeeze_distress_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rcp_drv2_025_squeeze_distress_5d_diff},
}
