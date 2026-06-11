"""
37_range_expansion — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base range-expansion concepts — velocity / acceleration
        of TR ratios, ATR levels, expansion counts, streak lengths, NR7/WR7
        narrow-range counts, and inside/outside bar counts
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rex_drv2_001_tr_ratio_atr21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR/ATR21 ratio (velocity of daily range expansion)."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    return ratio.diff(_TD_WEEK)


def rex_drv2_002_tr_ratio_atr21_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of TR/ATR21 ratio (monthly change in range expansion level)."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    return ratio.diff(_TD_MON)


def rex_drv2_003_atr21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day absolute diff of 21-day ATR (short-term velocity of ATR change)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return atr.diff(_TD_WEEK)


def rex_drv2_004_atr21_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day ATR (monthly velocity of volatility regime change)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return atr.diff(_TD_MON)


def rex_drv2_005_atr63_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day ATR (medium-term baseline volatility velocity)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return atr.diff(_TD_MON)


def rex_drv2_006_tr_zscore_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day TR z-score (velocity of standardized range extremity)."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_MON)
    s  = _rolling_std(tr, _TD_MON)
    z  = _safe_div(tr - m, s)
    return z.diff(_TD_WEEK)


def rex_drv2_007_tr_zscore_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day TR z-score."""
    tr = _tr(close, high, low)
    m  = _rolling_mean(tr, _TD_QTR)
    s  = _rolling_std(tr, _TD_QTR)
    z  = _safe_div(tr - m, s)
    return z.diff(_TD_MON)


def rex_drv2_008_expansion_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day expansion-day count."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    cnt  = _rolling_count_true(tr > atr, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rex_drv2_009_nr7_count_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day NR7 count (velocity of range-contraction clustering)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    cnt  = _rolling_sum((hl <= min7).astype(float), _TD_MON)
    return cnt.diff(_TD_WEEK)


def rex_drv2_010_wr7_count_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day WR7 count (velocity of wide-range bar clustering)."""
    hl   = high - low
    max7 = hl.rolling(7, min_periods=4).max()
    cnt  = _rolling_sum((hl >= max7).astype(float), _TD_MON)
    return cnt.diff(_TD_WEEK)


def rex_drv2_011_inside_bar_count_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day inside bar count (velocity of consolidation episodes)."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    cnt  = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rex_drv2_012_inside_bar_count_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day inside bar count (monthly change in consolidation rate)."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    cnt  = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def rex_drv2_013_outside_bar_count_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day outside bar count (velocity of expansion breakouts)."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    cnt  = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rex_drv2_014_consec_inside_streak_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of consecutive inside bar streak (streak velocity)."""
    flag = (high <= high.shift(1)) & (low >= low.shift(1))
    s    = _consec_streak(flag)
    return s.diff(_TD_WEEK)


def rex_drv2_015_atr21_vs_atr63_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR21/ATR63 ratio (short/medium-term vol spread velocity)."""
    tr    = _tr(close, high, low)
    ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    return ratio.diff(_TD_WEEK)


def rex_drv2_016_atr21_slope_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of ATR21 (acceleration of ATR trend)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    slp  = _linslope(atr, _TD_MON)
    return slp.diff(_TD_WEEK)


def rex_drv2_017_nr7_count_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day NR7 count (monthly change in contraction frequency)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    cnt  = _rolling_sum((hl <= min7).astype(float), _TD_QTR)
    return cnt.diff(_TD_MON)


def rex_drv2_018_tr_pct_rank_252d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of TR percentile rank in 252-day window."""
    tr  = _tr(close, high, low)
    rk  = tr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rk.diff(_TD_MON)


def rex_drv2_019_composite_expansion_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite expansion index (TR/ATR21, TR/ATR63, HL/avgHL21)."""
    tr    = _tr(close, high, low)
    hl    = high - low
    r1    = _safe_div(tr, _rolling_mean(tr, _TD_MON))
    r2    = _safe_div(tr, _rolling_mean(tr, _TD_QTR))
    r3    = _safe_div(hl, _rolling_mean(hl, _TD_MON))
    idx   = (r1 + r2 + r3) / 3.0
    return idx.diff(_TD_WEEK)


def rex_drv2_020_nr7_wr7_ratio_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of NR7-count / WR7-count ratio (contraction-vs-expansion balance velocity)."""
    hl    = high - low
    min7  = hl.rolling(7, min_periods=4).min()
    max7  = hl.rolling(7, min_periods=4).max()
    nr7   = _rolling_sum((hl <= min7).astype(float), _TD_MON)
    wr7   = _rolling_sum((hl >= max7).astype(float), _TD_MON)
    ratio = _safe_div(nr7, wr7 + 1.0)
    return ratio.diff(_TD_WEEK)


def rex_drv2_021_tr_vol_product_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of TR*volume z-score (velocity of panic-range signal)."""
    tr = _tr(close, high, low)
    tv = tr * volume
    m  = _rolling_mean(tv, _TD_MON)
    s  = _rolling_std(tv, _TD_MON)
    z  = _safe_div(tv - m, s)
    return z.diff(_TD_WEEK)


def rex_drv2_022_outside_after_inside_count_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day outside-after-inside event count (breakout velocity)."""
    ib_yesterday = (high.shift(1) <= high.shift(2)) & (low.shift(1) >= low.shift(2))
    ob_today     = (high > high.shift(1)) & (low < low.shift(1))
    flag = (ib_yesterday & ob_today).astype(float)
    cnt  = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def rex_drv2_023_atr21_rising_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of ATR21-rising days."""
    tr     = _tr(close, high, low)
    atr    = _rolling_mean(tr, _TD_MON)
    rising = atr > atr.shift(_TD_WEEK)
    cnt    = _rolling_count_true(rising, _TD_MON)
    return cnt.diff(_TD_WEEK)


def rex_drv2_024_max_tr_21d_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day max-TR over trailing 63 days."""
    tr   = _tr(close, high, low)
    mx21 = _rolling_max(tr, _TD_MON)
    return _linslope(mx21, _TD_QTR)


def rex_drv2_025_inside_bar_fraction_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day inside-bar fraction (velocity of consolidation density)."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    frac = _rolling_mean(flag, _TD_MON)
    return frac.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_REGISTRY_2ND_DERIVATIVES = {
    "rex_drv2_001_tr_ratio_atr21_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_001_tr_ratio_atr21_5d_diff},
    "rex_drv2_002_tr_ratio_atr21_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_002_tr_ratio_atr21_21d_diff},
    "rex_drv2_003_atr21_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_003_atr21_5d_diff},
    "rex_drv2_004_atr21_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_004_atr21_21d_diff},
    "rex_drv2_005_atr63_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_005_atr63_21d_diff},
    "rex_drv2_006_tr_zscore_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_006_tr_zscore_21d_5d_diff},
    "rex_drv2_007_tr_zscore_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_007_tr_zscore_63d_21d_diff},
    "rex_drv2_008_expansion_count_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_008_expansion_count_21d_5d_diff},
    "rex_drv2_009_nr7_count_21d_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_009_nr7_count_21d_5d_diff},
    "rex_drv2_010_wr7_count_21d_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_010_wr7_count_21d_5d_diff},
    "rex_drv2_011_inside_bar_count_21d_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_011_inside_bar_count_21d_5d_diff},
    "rex_drv2_012_inside_bar_count_63d_21d_diff": {"inputs": ["high", "low"], "func": rex_drv2_012_inside_bar_count_63d_21d_diff},
    "rex_drv2_013_outside_bar_count_21d_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_013_outside_bar_count_21d_5d_diff},
    "rex_drv2_014_consec_inside_streak_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_014_consec_inside_streak_5d_diff},
    "rex_drv2_015_atr21_vs_atr63_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_015_atr21_vs_atr63_5d_diff},
    "rex_drv2_016_atr21_slope_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_016_atr21_slope_21d_5d_diff},
    "rex_drv2_017_nr7_count_63d_21d_diff": {"inputs": ["high", "low"], "func": rex_drv2_017_nr7_count_63d_21d_diff},
    "rex_drv2_018_tr_pct_rank_252d_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_018_tr_pct_rank_252d_21d_diff},
    "rex_drv2_019_composite_expansion_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_019_composite_expansion_5d_diff},
    "rex_drv2_020_nr7_wr7_ratio_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_020_nr7_wr7_ratio_5d_diff},
    "rex_drv2_021_tr_vol_product_zscore_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_drv2_021_tr_vol_product_zscore_5d_diff},
    "rex_drv2_022_outside_after_inside_count_63d_21d_diff": {"inputs": ["high", "low"], "func": rex_drv2_022_outside_after_inside_count_63d_21d_diff},
    "rex_drv2_023_atr21_rising_count_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_drv2_023_atr21_rising_count_21d_5d_diff},
    "rex_drv2_024_max_tr_21d_slope_63d": {"inputs": ["close", "high", "low"], "func": rex_drv2_024_max_tr_21d_slope_63d},
    "rex_drv2_025_inside_bar_fraction_5d_diff": {"inputs": ["high", "low"], "func": rex_drv2_025_inside_bar_fraction_5d_diff},
}
