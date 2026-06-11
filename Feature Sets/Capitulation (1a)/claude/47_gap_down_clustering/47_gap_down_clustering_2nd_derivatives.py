"""
47_gap_down_clustering — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base gap-down clustering concepts — velocity and acceleration
of consecutive gap streaks, count density, cumulative magnitude, inter-gap timing,
cluster score evolution, and island-reversal count/recency dynamics.
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
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


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


def _down_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    return open < close.shift(1)


def _down_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    raw = (close.shift(1) - open).clip(lower=0.0)
    return _safe_div(raw, close.shift(1).replace(0, np.nan))


def _up_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    return open > close.shift(1)


def _island_bottom_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Island-bottom: gap-down 1-5 bars ago + gap-up today. Backward-looking."""
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        result = result + (ug & entry_gap).astype(float)
    return result.clip(upper=1.0)


def _days_since_island_bottom(close: pd.Series, open: pd.Series) -> pd.Series:
    """Bars elapsed since the last confirmed island-bottom signal."""
    flag = _island_bottom_flag(close, open)
    not_island = 1.0 - flag
    group = flag.cumsum()
    return not_island.groupby(group).cumsum()


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def gdc_drv2_001_consec_gap_streak_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of current consecutive gap-down streak (streak velocity)."""
    streak = _consec_streak(_down_gap(close, open))
    return streak.diff(_TD_WEEK)


def gdc_drv2_002_consec_gap_streak_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of current consecutive gap-down streak (monthly streak velocity)."""
    streak = _consec_streak(_down_gap(close, open))
    return streak.diff(_TD_MON)


def gdc_drv2_003_gap_count_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day gap-down count (surge in cluster density)."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    return cnt21.diff(_TD_WEEK)


def gdc_drv2_004_gap_count_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day gap-down count."""
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    return cnt63.diff(_TD_MON)


def gdc_drv2_005_sum_gap_pct_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day cumulative down-gap pct sum."""
    s21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    return s21.diff(_TD_WEEK)


def gdc_drv2_006_sum_gap_pct_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day cumulative down-gap pct sum."""
    s63 = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    return s63.diff(_TD_MON)


def gdc_drv2_007_max_gap_streak_63d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 63-day maximum consecutive gap-down streak."""
    mx = _rolling_max_streak(_down_gap(close, open), _TD_QTR)
    return mx.diff(_TD_WEEK)


def gdc_drv2_008_max_gap_streak_252d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of the 252-day maximum consecutive gap-down streak."""
    mx = _rolling_max_streak(_down_gap(close, open), _TD_YEAR)
    return mx.diff(_TD_MON)


def gdc_drv2_009_gap_down_fraction_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day gap-down fraction (rate of cluster density change)."""
    frac = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    return frac.diff(_TD_WEEK)


def gdc_drv2_010_gap_down_fraction_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day gap-down fraction."""
    frac = _rolling_count_true(_down_gap(close, open), _TD_QTR) / _TD_QTR
    return frac.diff(_TD_MON)


def gdc_drv2_011_gap_streak_zscore_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of gap-streak z-score vs 252-day distribution."""
    streak = _consec_streak(_down_gap(close, open))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    return z.diff(_TD_WEEK)


def gdc_drv2_012_gap_cluster_score_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of composite gap-cluster score (5d+21d+63d fractions)."""
    cond = _down_gap(close, open).astype(float)
    score = (
        _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
        + _rolling_sum(cond, _TD_MON) / _TD_MON
        + _rolling_sum(cond, _TD_QTR) / _TD_QTR
    ) / 3.0
    return score.diff(_TD_WEEK)


def gdc_drv2_013_gap_cluster_score_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of composite gap-cluster score."""
    cond = _down_gap(close, open).astype(float)
    score = (
        _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
        + _rolling_sum(cond, _TD_MON) / _TD_MON
        + _rolling_sum(cond, _TD_QTR) / _TD_QTR
    ) / 3.0
    return score.diff(_TD_MON)


def gdc_drv2_014_ewm_gap_count_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of EWM(span=21) down-gap indicator (smoothed density velocity)."""
    ewm = _ewm_mean(_down_gap(close, open).astype(float), _TD_MON)
    return ewm.diff(_TD_WEEK)


def gdc_drv2_015_gap_pct_ewm21_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) down-gap pct (velocity of severity accumulation)."""
    ewm = _ewm_mean(_down_gap_pct(close, open), _TD_MON)
    return ewm.diff(_TD_WEEK)


def gdc_drv2_016_days_since_gap_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of days-since-last-gap (change in inter-gap spacing)."""
    cond = _down_gap(close, open).astype(float)
    not_gap = 1.0 - cond
    group = cond.cumsum()
    ds = not_gap.groupby(group).cumsum()
    return ds.diff(_TD_WEEK)


def gdc_drv2_017_gap_count_5d_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 5-day gap count over trailing 63 days."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    return _linslope(cnt5, _TD_QTR)


def gdc_drv2_018_gap_count_21d_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 21-day gap count over trailing 63 days."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    return _linslope(cnt21, _TD_QTR)


def gdc_drv2_019_sum_gap_pct_21d_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 21-day cumulative gap pct over trailing 63 days."""
    s21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    return _linslope(s21, _TD_QTR)


def gdc_drv2_020_gap_vol_interaction_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (gap_down_flag * volume) EWM(21) interaction."""
    signal = _down_gap(close, open).astype(float) * volume
    ewm = _ewm_mean(signal, _TD_MON)
    return ewm.diff(_TD_WEEK)


def gdc_drv2_021_island_bottom_count_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of 21-day island-bottom count (velocity of island-reversal frequency).
    Positive values = accelerating island-bottom pattern formation.
    """
    cnt21 = _rolling_sum(_island_bottom_flag(close, open), _TD_MON)
    return cnt21.diff(_TD_WEEK)


def gdc_drv2_022_island_bottom_ewm_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of EWM(21) island-bottom flag (smoothed velocity of island density).
    Captures whether island-reversal activity is speeding up recently.
    """
    ewm = _ewm_mean(_island_bottom_flag(close, open), _TD_MON)
    return ewm.diff(_TD_WEEK)


def gdc_drv2_023_days_since_island_bottom_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of days-since-last-island-bottom (change in inter-island spacing).
    Falling values (negative diff) mean island bottoms are becoming more frequent.
    """
    return _days_since_island_bottom(close, open).diff(_TD_WEEK)


def gdc_drv2_024_island_bottom_count_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of 63-day island-bottom count (medium-term velocity of island reversals).
    Rising values indicate a cluster of island-bottom patterns over the past quarter.
    """
    cnt63 = _rolling_sum(_island_bottom_flag(close, open), _TD_QTR)
    return cnt63.diff(_TD_MON)


def gdc_drv2_025_gap_cluster_accel_ratio_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21d-vs-63d cluster rate acceleration ratio."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    r21 = cnt21 / _TD_MON
    r63 = cnt63 / _TD_QTR
    ratio = _safe_div(r21, r63)
    return ratio.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_REGISTRY_2ND_DERIVATIVES = {
    "gdc_drv2_001_consec_gap_streak_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_001_consec_gap_streak_5d_diff},
    "gdc_drv2_002_consec_gap_streak_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_002_consec_gap_streak_21d_diff},
    "gdc_drv2_003_gap_count_21d_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_003_gap_count_21d_5d_diff},
    "gdc_drv2_004_gap_count_63d_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_004_gap_count_63d_21d_diff},
    "gdc_drv2_005_sum_gap_pct_21d_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_005_sum_gap_pct_21d_5d_diff},
    "gdc_drv2_006_sum_gap_pct_63d_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_006_sum_gap_pct_63d_21d_diff},
    "gdc_drv2_007_max_gap_streak_63d_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_007_max_gap_streak_63d_5d_diff},
    "gdc_drv2_008_max_gap_streak_252d_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_008_max_gap_streak_252d_21d_diff},
    "gdc_drv2_009_gap_down_fraction_21d_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_009_gap_down_fraction_21d_5d_diff},
    "gdc_drv2_010_gap_down_fraction_63d_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_010_gap_down_fraction_63d_21d_diff},
    "gdc_drv2_011_gap_streak_zscore_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_011_gap_streak_zscore_5d_diff},
    "gdc_drv2_012_gap_cluster_score_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_012_gap_cluster_score_5d_diff},
    "gdc_drv2_013_gap_cluster_score_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_013_gap_cluster_score_21d_diff},
    "gdc_drv2_014_ewm_gap_count_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_014_ewm_gap_count_5d_diff},
    "gdc_drv2_015_gap_pct_ewm21_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_015_gap_pct_ewm21_5d_diff},
    "gdc_drv2_016_days_since_gap_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_016_days_since_gap_5d_diff},
    "gdc_drv2_017_gap_count_5d_slope_63d": {"inputs": ["close", "open"], "func": gdc_drv2_017_gap_count_5d_slope_63d},
    "gdc_drv2_018_gap_count_21d_slope_63d": {"inputs": ["close", "open"], "func": gdc_drv2_018_gap_count_21d_slope_63d},
    "gdc_drv2_019_sum_gap_pct_21d_slope_63d": {"inputs": ["close", "open"], "func": gdc_drv2_019_sum_gap_pct_21d_slope_63d},
    "gdc_drv2_020_gap_vol_interaction_5d_diff": {"inputs": ["close", "open", "volume"], "func": gdc_drv2_020_gap_vol_interaction_5d_diff},
    "gdc_drv2_021_island_bottom_count_21d_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_021_island_bottom_count_21d_5d_diff},
    "gdc_drv2_022_island_bottom_ewm_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_022_island_bottom_ewm_5d_diff},
    "gdc_drv2_023_days_since_island_bottom_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_023_days_since_island_bottom_5d_diff},
    "gdc_drv2_024_island_bottom_count_63d_21d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_024_island_bottom_count_63d_21d_diff},
    "gdc_drv2_025_gap_cluster_accel_ratio_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv2_025_gap_cluster_accel_ratio_5d_diff},
}
