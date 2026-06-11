"""
47_gap_down_clustering — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative gap-down clustering features — acceleration
of velocity: jerk in gap streak growth, jerk in cluster density change, acceleration
of gap magnitude accumulation, second-order cluster score dynamics, and jerk in
island-bottom reversal frequency (capturing sudden explosions in reversal activity).
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def gdc_drv3_001_consec_gap_streak_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of gap-streak length (jerk in streak velocity)."""
    streak = _consec_streak(_down_gap(close, open))
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_002_consec_gap_streak_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of gap-streak (jerk in monthly streak change)."""
    streak = _consec_streak(_down_gap(close, open))
    vel21 = streak.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_drv3_003_gap_count_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day gap count (acceleration of cluster density velocity)."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    vel = cnt21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_004_gap_count_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day gap count."""
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    vel21 = cnt63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_drv3_005_sum_gap_pct_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative gap pct (jerk in magnitude accumulation)."""
    s21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    vel = s21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_006_sum_gap_pct_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 63-day gap pct sum."""
    s63 = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    vel21 = s63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_drv3_007_gap_down_fraction_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day gap-down fraction (jerk in density rate)."""
    frac = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_008_gap_streak_zscore_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of gap-streak z-score (acceleration of extremity signal)."""
    streak = _consec_streak(_down_gap(close, open))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_009_gap_cluster_score_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of composite gap-cluster score."""
    cond = _down_gap(close, open).astype(float)
    score = (
        _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
        + _rolling_sum(cond, _TD_MON) / _TD_MON
        + _rolling_sum(cond, _TD_QTR) / _TD_QTR
    ) / 3.0
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_010_ewm_gap_count_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(21) gap-down indicator (jerk in smoothed density)."""
    ewm = _ewm_mean(_down_gap(close, open).astype(float), _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_011_gap_pct_ewm21_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(21) gap pct (jerk in severity accumulation)."""
    ewm = _ewm_mean(_down_gap_pct(close, open), _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_012_max_gap_streak_63d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day max gap-streak (acceleration of worst-streak growth)."""
    mx = _rolling_max_streak(_down_gap(close, open), _TD_QTR)
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_013_gap_count_5d_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day gap count over 63-day window."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    slp = _linslope(cnt5, _TD_QTR)
    return slp.diff(_TD_WEEK)


def gdc_drv3_014_gap_count_21d_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day gap count over 63-day window."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    slp = _linslope(cnt21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def gdc_drv3_015_sum_gap_pct_21d_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day cumulative gap pct."""
    s21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    slp = _linslope(s21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def gdc_drv3_016_gap_cluster_score_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of composite gap-cluster score."""
    cond = _down_gap(close, open).astype(float)
    score = (
        _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
        + _rolling_sum(cond, _TD_MON) / _TD_MON
        + _rolling_sum(cond, _TD_QTR) / _TD_QTR
    ) / 3.0
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_drv3_017_max_gap_pct_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day max gap pct (jerk in peak severity)."""
    mx = _rolling_max(_down_gap_pct(close, open), _TD_MON)
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_018_gap_down_fraction_252d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 252-day gap fraction."""
    frac = _rolling_count_true(_down_gap(close, open), _TD_YEAR) / _TD_YEAR
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_drv3_019_gap_vol_interaction_5d_diff_5d_diff(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(21) gap*volume interaction (panic jerk)."""
    signal = _down_gap(close, open).astype(float) * volume
    ewm = _ewm_mean(signal, _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_020_days_since_gap_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of days-since-last-gap (jerk in inter-gap spacing)."""
    cond = _down_gap(close, open).astype(float)
    not_gap = 1.0 - cond
    group = cond.cumsum()
    ds = not_gap.groupby(group).cumsum()
    vel = ds.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_021_island_bottom_count_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Second 5-day diff of 21-day island-bottom count (jerk in reversal frequency).
    Captures sudden explosive acceleration in island-bottom pattern formation —
    a sharp bottom signal in the gap-clustering/island-reversal domain.
    """
    cnt21 = _rolling_sum(_island_bottom_flag(close, open), _TD_MON)
    vel = cnt21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_022_island_bottom_ewm_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Second 5-day diff of EWM(21) island-bottom flag (jerk in smoothed island density).
    Measures whether the rate of island-reversal acceleration is itself accelerating.
    """
    ewm = _ewm_mean(_island_bottom_flag(close, open), _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_drv3_023_gap_fraction_21d_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day gap fraction over 63-day window."""
    frac21 = _rolling_count_true(_down_gap(close, open), _TD_MON) / _TD_MON
    slp = _linslope(frac21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def gdc_drv3_024_gap_streak_zscore_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of gap-streak z-score over 21-day window."""
    streak = _consec_streak(_down_gap(close, open))
    m = _rolling_mean(streak, _TD_YEAR)
    s = _rolling_std(streak, _TD_YEAR)
    z = _safe_div(streak - m, s)
    slp = _linslope(z, _TD_MON)
    return slp.diff(_TD_WEEK)


def gdc_drv3_025_days_since_island_bottom_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Second 5-day diff of days-since-last-island-bottom (jerk in inter-island spacing).
    Sharp negative jerk = sudden clustering of island-bottom reversals,
    a high-conviction capitulation-bottom timing signal.
    """
    ds = _days_since_island_bottom(close, open)
    vel = ds.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_REGISTRY_3RD_DERIVATIVES = {
    "gdc_drv3_001_consec_gap_streak_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_001_consec_gap_streak_5d_diff_5d_diff},
    "gdc_drv3_002_consec_gap_streak_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_002_consec_gap_streak_21d_diff_5d_diff},
    "gdc_drv3_003_gap_count_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_003_gap_count_21d_5d_diff_5d_diff},
    "gdc_drv3_004_gap_count_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_004_gap_count_63d_21d_diff_5d_diff},
    "gdc_drv3_005_sum_gap_pct_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_005_sum_gap_pct_21d_5d_diff_5d_diff},
    "gdc_drv3_006_sum_gap_pct_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_006_sum_gap_pct_63d_21d_diff_5d_diff},
    "gdc_drv3_007_gap_down_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_007_gap_down_fraction_21d_5d_diff_5d_diff},
    "gdc_drv3_008_gap_streak_zscore_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_008_gap_streak_zscore_5d_diff_5d_diff},
    "gdc_drv3_009_gap_cluster_score_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_009_gap_cluster_score_5d_diff_5d_diff},
    "gdc_drv3_010_ewm_gap_count_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_010_ewm_gap_count_5d_diff_5d_diff},
    "gdc_drv3_011_gap_pct_ewm21_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_011_gap_pct_ewm21_5d_diff_5d_diff},
    "gdc_drv3_012_max_gap_streak_63d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_012_max_gap_streak_63d_5d_diff_5d_diff},
    "gdc_drv3_013_gap_count_5d_slope_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_013_gap_count_5d_slope_5d_diff},
    "gdc_drv3_014_gap_count_21d_slope_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_014_gap_count_21d_slope_5d_diff},
    "gdc_drv3_015_sum_gap_pct_21d_slope_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_015_sum_gap_pct_21d_slope_5d_diff},
    "gdc_drv3_016_gap_cluster_score_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_016_gap_cluster_score_21d_diff_5d_diff},
    "gdc_drv3_017_max_gap_pct_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_017_max_gap_pct_21d_5d_diff_5d_diff},
    "gdc_drv3_018_gap_down_fraction_252d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_018_gap_down_fraction_252d_21d_diff_5d_diff},
    "gdc_drv3_019_gap_vol_interaction_5d_diff_5d_diff": {"inputs": ["close", "open", "volume"], "func": gdc_drv3_019_gap_vol_interaction_5d_diff_5d_diff},
    "gdc_drv3_020_days_since_gap_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_020_days_since_gap_5d_diff_5d_diff},
    "gdc_drv3_021_island_bottom_count_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_021_island_bottom_count_21d_5d_diff_5d_diff},
    "gdc_drv3_022_island_bottom_ewm_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_022_island_bottom_ewm_5d_diff_5d_diff},
    "gdc_drv3_023_gap_fraction_21d_slope_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_023_gap_fraction_21d_slope_5d_diff},
    "gdc_drv3_024_gap_streak_zscore_slope_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_024_gap_streak_zscore_slope_5d_diff},
    "gdc_drv3_025_days_since_island_bottom_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gdc_drv3_025_days_since_island_bottom_5d_diff_5d_diff},
}
