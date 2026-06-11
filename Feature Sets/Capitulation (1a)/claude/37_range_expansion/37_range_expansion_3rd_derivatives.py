"""
37_range_expansion — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative range-expansion concepts — acceleration
        of velocity in TR ratios, ATR trends, expansion counts, streak dynamics,
        NR7/WR7 clustering rates, and inside/outside bar breakout sequences
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range: max of H-L, |H-prevC|, |L-prevC|."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c     = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def rex_drv3_001_tr_ratio_atr21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR/ATR21 (acceleration of range-expansion velocity)."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    vel   = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_002_tr_ratio_atr21_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of TR/ATR21 (jerk in monthly expansion)."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_drv3_003_atr21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR21 (acceleration of volatility-level change)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    vel = atr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_004_atr21_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in ATR21."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    vel21 = atr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_drv3_005_tr_zscore_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day TR z-score (jerk in standardized range)."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_MON)
    s  = _rolling_std(tr, _TD_MON)
    z  = _safe_div(tr - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_006_nr7_count_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day NR7 count (jerk in contraction clustering)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    cnt  = _rolling_sum((hl <= min7).astype(float), _TD_MON)
    vel  = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_007_wr7_count_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day WR7 count (jerk in wide-range bar clustering)."""
    hl   = high - low
    max7 = hl.rolling(7, min_periods=4).max()
    cnt  = _rolling_sum((hl >= max7).astype(float), _TD_MON)
    vel  = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_008_inside_bar_count_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day inside bar count (acceleration of consolidation rate)."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    cnt  = _rolling_sum(flag, _TD_MON)
    vel  = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_009_outside_bar_count_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day outside bar count (acceleration of breakout frequency)."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    cnt  = _rolling_sum(flag, _TD_MON)
    vel  = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_010_atr21_vs_atr63_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR21/ATR63 ratio."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    vel   = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_011_composite_expansion_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite expansion index."""
    tr   = _tr(close, high, low)
    hl   = high - low
    r1   = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    r2   = _safe_div(tr, _rolling_mean(tr, _TD_QTR))
    r3   = _safe_div(hl, _rolling_mean(hl, _TD_MON))
    idx  = (r1 + r2 + r3) / 3.0
    vel  = idx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_012_nr7_count_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day NR7 count (jerk in contraction frequency)."""
    hl    = high - low
    min7  = hl.rolling(7, min_periods=4).min()
    cnt   = _rolling_sum((hl <= min7).astype(float), _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_drv3_013_atr21_slope_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR21 OLS-slope (jerk in ATR trend)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    slp  = _linslope(atr, _TD_MON)
    vel  = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_014_consec_inside_streak_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive inside bar streak (jerk in consolidation depth)."""
    flag = (high <= high.shift(1)) & (low >= low.shift(1))
    s    = _consec_streak(flag)
    vel  = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_015_tr_ratio_atr21_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of TR/ATR21 over 21 days."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    slp   = _linslope(ratio, _TD_MON)
    return slp.diff(_TD_WEEK)


def rex_drv3_016_atr21_pct_close_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of ATR21/close% (acceleration of normalized vol)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    pct = _safe_div(atr, close) * 100.0
    vel = pct.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_017_nr7_wr7_ratio_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of NR7-count / WR7-count ratio (jerk in contraction-vs-expansion balance)."""
    hl    = high - low
    min7  = hl.rolling(7, min_periods=4).min()
    max7  = hl.rolling(7, min_periods=4).max()
    nr7   = _rolling_sum((hl <= min7).astype(float), _TD_MON)
    wr7   = _rolling_sum((hl >= max7).astype(float), _TD_MON)
    ratio = _safe_div(nr7, wr7 + 1.0)
    vel   = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_018_atr5_vs_atr63_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in ATR5/ATR63 ratio."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_drv3_019_inside_bar_fraction_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day inside-bar fraction (acceleration of consolidation density)."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    frac = _rolling_mean(flag, _TD_MON)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_020_tr_pct_rank_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in TR percentile rank (252-day window)."""
    tr    = _tr(close, high, low)
    rk    = tr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel21 = rk.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_drv3_021_atr_regime_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of multi-scale ATR regime score."""
    tr     = _tr(close, high, low)
    atr5   = _rolling_mean(tr, _TD_WEEK)
    atr21  = _rolling_mean(tr, _TD_MON)
    atr63  = _rolling_mean(tr, _TD_QTR)
    atr252 = _rolling_mean(tr, _TD_YEAR)
    score  = (_safe_div(atr5, atr63) + _safe_div(atr21, atr252)) / 2.0
    vel    = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_022_outside_after_inside_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day outside-after-inside count (jerk in breakout rate)."""
    ib_yesterday = (high.shift(1) <= high.shift(2)) & (low.shift(1) >= low.shift(2))
    ob_today     = (high > high.shift(1)) & (low < low.shift(1))
    flag  = (ib_yesterday & ob_today).astype(float)
    cnt   = _rolling_sum(flag, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_drv3_023_atr21_rising_count_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day count of ATR21-rising days."""
    tr     = _tr(close, high, low)
    atr    = _rolling_mean(tr, _TD_MON)
    rising = atr > atr.shift(_TD_WEEK)
    cnt    = _rolling_count_true(rising, _TD_MON)
    vel    = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_024_expansion_count_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day expansion count (acceleration of count change)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    cnt = _rolling_count_true(tr > atr, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_drv3_025_atr63_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day ATR (jerk in medium-term vol baseline)."""
    tr    = _tr(close, high, low)
    atr63 = _rolling_mean(tr, _TD_QTR)
    vel21 = atr63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_REGISTRY_3RD_DERIVATIVES = {
    "rex_drv3_001_tr_ratio_atr21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_001_tr_ratio_atr21_5d_diff_5d_diff},
    "rex_drv3_002_tr_ratio_atr21_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_002_tr_ratio_atr21_21d_diff_5d_diff},
    "rex_drv3_003_atr21_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_003_atr21_5d_diff_5d_diff},
    "rex_drv3_004_atr21_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_004_atr21_21d_diff_5d_diff},
    "rex_drv3_005_tr_zscore_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_005_tr_zscore_21d_5d_diff_5d_diff},
    "rex_drv3_006_nr7_count_21d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_006_nr7_count_21d_5d_diff_5d_diff},
    "rex_drv3_007_wr7_count_21d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_007_wr7_count_21d_5d_diff_5d_diff},
    "rex_drv3_008_inside_bar_count_21d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_008_inside_bar_count_21d_5d_diff_5d_diff},
    "rex_drv3_009_outside_bar_count_21d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_009_outside_bar_count_21d_5d_diff_5d_diff},
    "rex_drv3_010_atr21_vs_atr63_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_010_atr21_vs_atr63_5d_diff_5d_diff},
    "rex_drv3_011_composite_expansion_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_011_composite_expansion_5d_diff_5d_diff},
    "rex_drv3_012_nr7_count_63d_21d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_012_nr7_count_63d_21d_diff_5d_diff},
    "rex_drv3_013_atr21_slope_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_013_atr21_slope_21d_5d_diff_5d_diff},
    "rex_drv3_014_consec_inside_streak_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_014_consec_inside_streak_5d_diff_5d_diff},
    "rex_drv3_015_tr_ratio_atr21_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_015_tr_ratio_atr21_slope_5d_diff},
    "rex_drv3_016_atr21_pct_close_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_016_atr21_pct_close_5d_diff_5d_diff},
    "rex_drv3_017_nr7_wr7_ratio_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_017_nr7_wr7_ratio_5d_diff_5d_diff},
    "rex_drv3_018_atr5_vs_atr63_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_018_atr5_vs_atr63_21d_diff_5d_diff},
    "rex_drv3_019_inside_bar_fraction_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_019_inside_bar_fraction_5d_diff_5d_diff},
    "rex_drv3_020_tr_pct_rank_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_020_tr_pct_rank_21d_diff_5d_diff},
    "rex_drv3_021_atr_regime_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_021_atr_regime_score_5d_diff_5d_diff},
    "rex_drv3_022_outside_after_inside_63d_21d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_drv3_022_outside_after_inside_63d_21d_diff_5d_diff},
    "rex_drv3_023_atr21_rising_count_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_023_atr21_rising_count_5d_diff_5d_diff},
    "rex_drv3_024_expansion_count_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_024_expansion_count_21d_5d_diff_5d_diff},
    "rex_drv3_025_atr63_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv3_025_atr63_21d_diff_5d_diff},
}
