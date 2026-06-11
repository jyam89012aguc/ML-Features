"""
46_gap_structure — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base gap-structure features — velocity of gap behavior
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Includes velocity of gap-type classification features (exhaustion, breakaway, runaway, common).
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _gap_pct(close: pd.Series, open_: pd.Series) -> pd.Series:
    prior_close = close.shift(1)
    return _safe_div(open_ - prior_close, prior_close.abs().clip(lower=_EPS))


def _gap_down(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(upper=0).abs()


def _gap_up(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(lower=0)


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


# ── Gap-type classification helpers (self-contained) ─────────────────────────

def _trend_direction(close: pd.Series, w: int = _TD_MON) -> pd.Series:
    slope = close.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if len(x) >= 2 else 0.0,
        raw=True
    )
    return np.sign(slope)


def _trailing_range_position(close: pd.Series, high: pd.Series, low: pd.Series,
                              open_: pd.Series, w: int = _TD_MON) -> pd.Series:
    prior_high = high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    prior_low = low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    rng = (prior_high - prior_low).clip(lower=_EPS)
    return _safe_div(open_ - prior_low, rng).clip(0.0, 1.0)


def _vol_ratio(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    avg = volume.shift(1).rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=_EPS)
    return _safe_div(volume, avg)


def _trend_maturity(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    rolling_mean_w = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > rolling_mean_w).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _exhaustion_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                               volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    maturity = _trend_maturity(close, _TD_QTR)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & late_downtrend & (vol_r > 1.5)).astype(float)


def _breakaway_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                              volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & (rng_pos <= 0.1) & (vol_r > 1.2)).astype(float)


def _exhaustion_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                         volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    late_uptrend = (trend_dir > 0) & (maturity > 0.75)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    late_trend = late_uptrend | late_downtrend
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & late_trend & (vol_r > 1.5)).astype(float)


def _breakaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                        volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    outside_range = (rng_pos <= 0.1) | (rng_pos >= 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & outside_range & (vol_r > 1.2)).astype(float)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

# --- drv2_001-010: Velocity of core gap metrics ---

def gap_drv2_001_avg_gap_abs_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day avg abs gap (velocity of gap size)."""
    avg = _rolling_mean(_gap_pct(close, open).abs(), _TD_MON)
    return avg.diff(_TD_WEEK)


def gap_drv2_002_avg_gap_abs_21d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 21-day avg abs gap (monthly change in gap size)."""
    avg = _rolling_mean(_gap_pct(close, open).abs(), _TD_MON)
    return avg.diff(_TD_MON)


def gap_drv2_003_avg_gap_abs_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day avg abs gap."""
    avg = _rolling_mean(_gap_pct(close, open).abs(), _TD_QTR)
    return avg.diff(_TD_MON)


def gap_drv2_004_gap_down_freq_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-gap frequency."""
    freq = _rolling_count_true(_gap_pct(close, open) < 0, _TD_MON) / _TD_MON
    return freq.diff(_TD_WEEK)


def gap_drv2_005_gap_down_freq_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-gap frequency."""
    freq = _rolling_count_true(_gap_pct(close, open) < 0, _TD_QTR) / _TD_QTR
    return freq.diff(_TD_MON)


def gap_drv2_006_gap_std_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day gap standard deviation (volatility acceleration)."""
    s = _rolling_std(_gap_pct(close, open), _TD_MON)
    return s.diff(_TD_WEEK)


def gap_drv2_007_gap_std_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day gap std."""
    s = _rolling_std(_gap_pct(close, open), _TD_QTR)
    return s.diff(_TD_MON)


def gap_drv2_008_gap_down_sum_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative down-gap return."""
    dg_sum = _rolling_sum(_gap_down(close, open), _TD_MON)
    return dg_sum.diff(_TD_WEEK)


def gap_drv2_009_gap_down_sum_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day cumulative down-gap return."""
    dg_sum = _rolling_sum(_gap_down(close, open), _TD_QTR)
    return dg_sum.diff(_TD_MON)


def gap_drv2_010_gap_signed_avg_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day average signed gap (net overnight drift velocity)."""
    avg = _rolling_mean(_gap_pct(close, open), _TD_MON)
    return avg.diff(_TD_WEEK)


# --- drv2_011-015: Velocity of gap fill and regime metrics ---

def gap_drv2_011_gap_fill_freq_63d_21d_diff(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day gap-fill frequency."""
    prior_close = close.shift(1)
    gap = open - prior_close
    filled = ((gap > 0) & (low <= prior_close) | (gap < 0) & (high >= prior_close)).astype(float)
    has_gap = (_gap_pct(close, open).abs() > _EPS).astype(float)
    fill_sum = _rolling_sum(filled, _TD_QTR)
    gap_sum = _rolling_sum(has_gap, _TD_QTR).clip(lower=1)
    fill_rate = _safe_div(fill_sum, gap_sum)
    return fill_rate.diff(_TD_MON)


def gap_drv2_012_gap_abs_zscore_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 252-day abs-gap z-score."""
    ag = _gap_pct(close, open).abs()
    m = _rolling_mean(ag, _TD_YEAR)
    s = _rolling_std(ag, _TD_YEAR)
    z = _safe_div(ag - m, s)
    return z.diff(_TD_WEEK)


def gap_drv2_013_gap_down_vs_up_freq_ratio_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-vs-up gap frequency ratio."""
    g = _gap_pct(close, open)
    up = _rolling_count_true(g > 0, _TD_QTR)
    dn = _rolling_count_true(g < 0, _TD_QTR)
    ratio = _safe_div(dn, up)
    return ratio.diff(_TD_MON)


def gap_drv2_014_gap_vol_ratio_21d_vs_252d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21d/252d gap vol ratio (regime shift speed)."""
    ag = _gap_pct(close, open).abs()
    ratio = _safe_div(_rolling_std(ag, _TD_MON), _rolling_std(ag, _TD_YEAR).clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def gap_drv2_015_gap_net_bias_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day net overnight gap bias."""
    bias = _rolling_sum(_gap_up(close, open), _TD_QTR) - _rolling_sum(_gap_down(close, open), _TD_QTR)
    return bias.diff(_TD_MON)


# --- drv2_016-025: Velocity of gap-type classification features ───────────────

def gap_drv2_016_exhaustion_gap_down_count_63d_21d_diff(close: pd.Series, open: pd.Series,
                                                          high: pd.Series, low: pd.Series,
                                                          volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-exhaustion gap count (velocity of exhaustion activity)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def gap_drv2_017_breakaway_gap_down_count_63d_21d_diff(close: pd.Series, open: pd.Series,
                                                         high: pd.Series, low: pd.Series,
                                                         volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-breakaway gap count."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def gap_drv2_018_exhaustion_gap_down_flag_ewm_5d_diff(close: pd.Series, open: pd.Series,
                                                        high: pd.Series, low: pd.Series,
                                                        volume: pd.Series) -> pd.Series:
    """5-day diff of 21-span EWM of down-exhaustion gap flag (smoothed capitulation pulse velocity)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ewm = _ewm_mean(flag, _TD_MON)
    return ewm.diff(_TD_WEEK)


def gap_drv2_019_breakaway_gap_down_flag_ewm_5d_diff(close: pd.Series, open: pd.Series,
                                                       high: pd.Series, low: pd.Series,
                                                       volume: pd.Series) -> pd.Series:
    """5-day diff of 21-span EWM of down-breakaway gap flag (regime-break velocity)."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    ewm = _ewm_mean(flag, _TD_MON)
    return ewm.diff(_TD_WEEK)


def gap_drv2_020_exhaustion_gap_count_all_21d_5d_diff(close: pd.Series, open: pd.Series,
                                                        high: pd.Series, low: pd.Series,
                                                        volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of all exhaustion gaps (any direction)."""
    flag = _exhaustion_gap_flag(close, open, high, low, volume)
    cnt21 = _rolling_sum(flag, _TD_MON)
    return cnt21.diff(_TD_WEEK)


def gap_drv2_021_gap_type_distress_score_21d_5d_diff(close: pd.Series, open: pd.Series,
                                                       high: pd.Series, low: pd.Series,
                                                       volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day gap-type distress score (weighted exhaustion + breakaway down count)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    score = _rolling_sum(2.0 * ex_dn + 1.0 * ba_dn, _TD_MON)
    return score.diff(_TD_WEEK)


def gap_drv2_022_exhaustion_vs_breakaway_ratio_21d_diff(close: pd.Series, open: pd.Series,
                                                          high: pd.Series, low: pd.Series,
                                                          volume: pd.Series) -> pd.Series:
    """21-day diff of ratio of exhaustion-down count to breakaway-down count (63d window)."""
    ex = _rolling_sum(_exhaustion_gap_down_flag(close, open, high, low, volume), _TD_QTR)
    ba = _rolling_sum(_breakaway_gap_down_flag(close, open, high, low, volume), _TD_QTR)
    ratio = _safe_div(ex, ba.clip(lower=1))
    return ratio.diff(_TD_MON)


def gap_drv2_023_breakaway_gap_all_count_63d_21d_diff(close: pd.Series, open: pd.Series,
                                                        high: pd.Series, low: pd.Series,
                                                        volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day all-direction breakaway gap count."""
    flag = _breakaway_gap_flag(close, open, high, low, volume)
    cnt = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def gap_drv2_024_gap_down_share_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-gap share of total gap activity."""
    dn_sum = _rolling_sum(_gap_down(close, open), _TD_QTR)
    tot_sum = _rolling_sum(_gap_pct(close, open).abs(), _TD_QTR).clip(lower=_EPS)
    share = _safe_div(dn_sum, tot_sum)
    return share.diff(_TD_MON)


def gap_drv2_025_exhaustion_gap_down_count_21d_5d_diff(close: pd.Series, open: pd.Series,
                                                         high: pd.Series, low: pd.Series,
                                                         volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-exhaustion gap count (short-horizon capitulation impulse velocity)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    cnt21 = _rolling_sum(flag, _TD_MON)
    return cnt21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_STRUCTURE_REGISTRY_2ND_DERIVATIVES = {
    "gap_drv2_001_avg_gap_abs_21d_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_001_avg_gap_abs_21d_5d_diff},
    "gap_drv2_002_avg_gap_abs_21d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_002_avg_gap_abs_21d_21d_diff},
    "gap_drv2_003_avg_gap_abs_63d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_003_avg_gap_abs_63d_21d_diff},
    "gap_drv2_004_gap_down_freq_21d_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_004_gap_down_freq_21d_5d_diff},
    "gap_drv2_005_gap_down_freq_63d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_005_gap_down_freq_63d_21d_diff},
    "gap_drv2_006_gap_std_21d_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_006_gap_std_21d_5d_diff},
    "gap_drv2_007_gap_std_63d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_007_gap_std_63d_21d_diff},
    "gap_drv2_008_gap_down_sum_21d_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_008_gap_down_sum_21d_5d_diff},
    "gap_drv2_009_gap_down_sum_63d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_009_gap_down_sum_63d_21d_diff},
    "gap_drv2_010_gap_signed_avg_21d_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_010_gap_signed_avg_21d_5d_diff},
    "gap_drv2_011_gap_fill_freq_63d_21d_diff": {"inputs": ["close", "open", "high", "low"], "func": gap_drv2_011_gap_fill_freq_63d_21d_diff},
    "gap_drv2_012_gap_abs_zscore_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_012_gap_abs_zscore_5d_diff},
    "gap_drv2_013_gap_down_vs_up_freq_ratio_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_013_gap_down_vs_up_freq_ratio_21d_diff},
    "gap_drv2_014_gap_vol_ratio_21d_vs_252d_5d_diff": {"inputs": ["close", "open"], "func": gap_drv2_014_gap_vol_ratio_21d_vs_252d_5d_diff},
    "gap_drv2_015_gap_net_bias_63d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_015_gap_net_bias_63d_21d_diff},
    "gap_drv2_016_exhaustion_gap_down_count_63d_21d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_016_exhaustion_gap_down_count_63d_21d_diff},
    "gap_drv2_017_breakaway_gap_down_count_63d_21d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_017_breakaway_gap_down_count_63d_21d_diff},
    "gap_drv2_018_exhaustion_gap_down_flag_ewm_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_018_exhaustion_gap_down_flag_ewm_5d_diff},
    "gap_drv2_019_breakaway_gap_down_flag_ewm_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_019_breakaway_gap_down_flag_ewm_5d_diff},
    "gap_drv2_020_exhaustion_gap_count_all_21d_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_020_exhaustion_gap_count_all_21d_5d_diff},
    "gap_drv2_021_gap_type_distress_score_21d_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_021_gap_type_distress_score_21d_5d_diff},
    "gap_drv2_022_exhaustion_vs_breakaway_ratio_21d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_022_exhaustion_vs_breakaway_ratio_21d_diff},
    "gap_drv2_023_breakaway_gap_all_count_63d_21d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_023_breakaway_gap_all_count_63d_21d_diff},
    "gap_drv2_024_gap_down_share_63d_21d_diff": {"inputs": ["close", "open"], "func": gap_drv2_024_gap_down_share_63d_21d_diff},
    "gap_drv2_025_exhaustion_gap_down_count_21d_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv2_025_exhaustion_gap_down_count_21d_5d_diff},
}
