"""
58_trading_intensity — Base Features 001-075
Domain: trade-frequency / activity-intensity proxies — how busy the tape is
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — active vs lull regimes, price-discovery intensity
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


def _active_day(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True when the day moved: close != prior close OR high != low."""
    moved_close = close != close.shift(1)
    has_range   = (high - low) > 0
    return (moved_close | has_range).astype(float)


def _range_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday range as fraction of prior close."""
    return _safe_div(high - low, close.shift(1).replace(0, np.nan))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
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
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Active-day fraction (non-stale sessions) ---

def tin_001_active_day_frac_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 5 days that were active (price moved or had range)."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_WEEK) / _TD_WEEK


def tin_002_active_day_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were active."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_MON) / _TD_MON


def tin_003_active_day_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were active."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_QTR) / _TD_QTR


def tin_004_active_day_frac_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 126 days that were active."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_HALF) / _TD_HALF


def tin_005_active_day_frac_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days that were active."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_YEAR) / _TD_YEAR


def tin_006_active_day_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of active sessions in trailing 21 days."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_MON)


def tin_007_active_day_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of active sessions in trailing 63 days."""
    act = _active_day(close, high, low)
    return _rolling_sum(act, _TD_QTR)


def tin_008_active_frac_5d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day active-day fraction to 63-day active-day fraction."""
    f5  = tin_001_active_day_frac_5d(close, high, low)
    f63 = tin_003_active_day_frac_63d(close, high, low)
    return _safe_div(f5, f63)


def tin_009_active_frac_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day active fraction to 252-day active fraction."""
    f21  = tin_002_active_day_frac_21d(close, high, low)
    f252 = tin_005_active_day_frac_252d(close, high, low)
    return _safe_div(f21, f252)


def tin_010_active_day_frac_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day active-day fraction relative to 252-day distribution."""
    f21 = tin_002_active_day_frac_21d(close, high, low)
    m   = _rolling_mean(f21, _TD_YEAR)
    s   = _rolling_std(f21, _TD_YEAR)
    return _safe_div(f21 - m, s)


# --- Group B (011-020): Volume-per-unit-range (trade-intensity proxy) ---

def tin_011_vol_per_range_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean daily volume divided by intraday range over 21 days (vol/range intensity)."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    return _rolling_mean(vpr, _TD_MON)


def tin_012_vol_per_range_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean daily volume divided by intraday range over 63 days."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    return _rolling_mean(vpr, _TD_QTR)


def tin_013_vol_per_range_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean daily volume divided by intraday range over 252 days."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    return _rolling_mean(vpr, _TD_YEAR)


def tin_014_vol_per_range_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day vol/range to 252-day vol/range (recent intensity vs history)."""
    return _safe_div(
        tin_011_vol_per_range_21d(close, high, low, volume),
        tin_013_vol_per_range_252d(close, high, low, volume),
    )


def tin_015_vol_per_range_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily vol/range relative to 252-day distribution."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    m   = _rolling_mean(vpr, _TD_YEAR)
    s   = _rolling_std(vpr, _TD_YEAR)
    return _safe_div(vpr - m, s)


def tin_016_vol_per_pct_range_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume per unit of percentage range (range normalized by price) over 21d."""
    rng_pct = _range_pct(close, high, low).replace(0, np.nan)
    vpr_pct = _safe_div(volume, rng_pct)
    return _rolling_mean(vpr_pct, _TD_MON)


def tin_017_vol_per_pct_range_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume per unit of percentage range over 63 days."""
    rng_pct = _range_pct(close, high, low).replace(0, np.nan)
    vpr_pct = _safe_div(volume, rng_pct)
    return _rolling_mean(vpr_pct, _TD_QTR)


def tin_018_range_per_volume_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (range / volume) over 21 days — lower = more activity per price move."""
    rng = (high - low)
    rpv = _safe_div(rng, volume.replace(0, np.nan))
    return _rolling_mean(rpv, _TD_MON)


def tin_019_range_per_volume_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (range / volume) over 63 days."""
    rng = (high - low)
    rpv = _safe_div(rng, volume.replace(0, np.nan))
    return _rolling_mean(rpv, _TD_QTR)


def tin_020_range_per_volume_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily range/volume relative to 252-day distribution."""
    rng = (high - low)
    rpv = _safe_div(rng, volume.replace(0, np.nan))
    m   = _rolling_mean(rpv, _TD_YEAR)
    s   = _rolling_std(rpv, _TD_YEAR)
    return _safe_div(rpv - m, s)


# --- Group C (021-030): Meaningful-volume day fraction ---

def tin_021_meaningful_vol_day_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with volume above 50% of 63-day median volume."""
    med63 = _rolling_median(volume, _TD_QTR)
    cond  = volume > 0.5 * med63
    return _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON


def tin_022_meaningful_vol_day_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with volume above 50% of 63-day median volume."""
    med63 = _rolling_median(volume, _TD_QTR)
    cond  = volume > 0.5 * med63
    return _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR


def tin_023_meaningful_vol_day_frac_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days with volume above 50% of 252-day median volume."""
    med252 = _rolling_median(volume, _TD_YEAR)
    cond   = volume > 0.5 * med252
    return _rolling_sum(cond.astype(float), _TD_YEAR) / _TD_YEAR


def tin_024_high_vol_day_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with volume above 252-day mean (high-activity sessions)."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = volume > avg252
    return _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON


def tin_025_high_vol_day_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with volume above 252-day mean."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = volume > avg252
    return _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR


def tin_026_high_vol_day_frac_5d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day high-vol-day fraction to 63-day high-vol-day fraction."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = (volume > avg252).astype(float)
    f5  = _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
    f63 = _rolling_sum(cond, _TD_QTR)  / _TD_QTR
    return _safe_div(f5, f63)


def tin_027_low_vol_lull_day_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with volume below 25% of 63-day median (lull sessions)."""
    med63 = _rolling_median(volume, _TD_QTR)
    cond  = volume < 0.25 * med63
    return _rolling_sum(cond.astype(float), _TD_MON) / _TD_MON


def tin_028_low_vol_lull_day_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with volume below 25% of 63-day median."""
    med63 = _rolling_median(volume, _TD_QTR)
    cond  = volume < 0.25 * med63
    return _rolling_sum(cond.astype(float), _TD_QTR) / _TD_QTR


def tin_029_active_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of high-vol-day fraction to low-vol-day fraction over 21 days."""
    med63 = _rolling_median(volume, _TD_QTR)
    high  = _rolling_sum((volume > med63).astype(float), _TD_MON)
    low   = _rolling_sum((volume < 0.5 * med63).astype(float), _TD_MON)
    return _safe_div(high, low.replace(0, np.nan))


def tin_030_active_to_total_session_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Active sessions (moved AND had meaningful volume) / total sessions over 63d."""
    med63 = _rolling_median(volume, _TD_QTR)
    act   = ((_active_day(close, high, low) > 0) & (volume > 0.5 * med63)).astype(float)
    return _rolling_sum(act, _TD_QTR) / _TD_QTR


# --- Group D (031-040): Price-discovery session count ---

def tin_031_distinct_close_count_21d(close: pd.Series) -> pd.Series:
    """Count of days with a close different from prior day's close in 21 days."""
    moved = (close != close.shift(1)).astype(float)
    return _rolling_sum(moved, _TD_MON)


def tin_032_distinct_close_count_63d(close: pd.Series) -> pd.Series:
    """Count of days with a close different from prior day's close in 63 days."""
    moved = (close != close.shift(1)).astype(float)
    return _rolling_sum(moved, _TD_QTR)


def tin_033_distinct_close_frac_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days where the close changed from prior close."""
    moved = (close != close.shift(1)).astype(float)
    return _rolling_sum(moved, _TD_MON) / _TD_MON


def tin_034_price_discovery_events_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where both close moved AND range > prior-21d median range."""
    rng     = high - low
    med_rng = _rolling_median(rng, _TD_MON)
    events  = ((close != close.shift(1)) & (rng > med_rng)).astype(float)
    return _rolling_sum(events, _TD_MON)


def tin_035_price_discovery_events_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where both close moved AND range > prior-63d median range."""
    rng     = high - low
    med_rng = _rolling_median(rng, _TD_QTR)
    events  = ((close != close.shift(1)) & (rng > med_rng)).astype(float)
    return _rolling_sum(events, _TD_QTR)


def tin_036_new_high_or_low_day_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days that set a new intraday high or low vs prior day."""
    new_h = (high > high.shift(1)).astype(float)
    new_l = (low  < low.shift(1)).astype(float)
    events = ((new_h + new_l) > 0).astype(float)
    return _rolling_sum(events, _TD_MON) / _TD_MON


def tin_037_new_high_or_low_day_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days that set a new intraday high or low vs prior day."""
    new_h  = (high > high.shift(1)).astype(float)
    new_l  = (low  < low.shift(1)).astype(float)
    events = ((new_h + new_l) > 0).astype(float)
    return _rolling_sum(events, _TD_QTR) / _TD_QTR


def tin_038_both_new_high_and_low_frac_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days with both new intraday high AND new low (2-sided discovery)."""
    cond = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_039_close_change_count_5d(close: pd.Series) -> pd.Series:
    """Count of days in last 5 where close changed from prior close."""
    moved = (close != close.shift(1)).astype(float)
    return _rolling_sum(moved, _TD_WEEK)


def tin_040_discovery_intensity_ratio_5d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day price-discovery event fraction divided by 252-day average fraction."""
    rng     = high - low
    med_rng = _rolling_median(rng, _TD_QTR)
    events  = ((close != close.shift(1)) & (rng > med_rng)).astype(float)
    f5   = _rolling_sum(events, _TD_WEEK) / _TD_WEEK
    f252 = _rolling_mean(f5, _TD_YEAR)
    return _safe_div(f5, f252)


# --- Group E (041-050): Activity burst vs lull streaks ---

def tin_041_active_day_consec_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive streak of active (non-stale) days."""
    cond = _active_day(close, high, low) > 0
    return _consec_streak(cond)


def tin_042_lull_day_consec_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive streak of lull (stale / no-range) days."""
    cond = _active_day(close, high, low) == 0
    return _consec_streak(cond)


def tin_043_high_vol_consec_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive streak of above-21d-mean volume days."""
    avg = _rolling_mean(volume, _TD_MON)
    cond = volume > avg
    return _consec_streak(cond)


def tin_044_low_vol_consec_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive streak of below-21d-mean volume days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = volume < avg
    return _consec_streak(cond)


def tin_045_burst_lull_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of high-vol-day count to low-vol-day count over 21 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    high = _rolling_sum((volume > avg).astype(float), _TD_MON)
    low  = _rolling_sum((volume < avg).astype(float), _TD_MON)
    return _safe_div(high, low.replace(0, np.nan))


def tin_046_burst_lull_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of high-vol-day count to low-vol-day count over 63 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    high = _rolling_sum((volume > avg).astype(float), _TD_QTR)
    low  = _rolling_sum((volume < avg).astype(float), _TD_QTR)
    return _safe_div(high, low.replace(0, np.nan))


def tin_047_burst_persistence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive high-vol streak within trailing 21 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > avg)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx:
                mx = cur
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def tin_048_lull_persistence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive low-vol streak within trailing 21 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume < avg)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx:
                mx = cur
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def tin_049_burst_persistence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive high-vol streak within trailing 63 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > avg)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx:
                mx = cur
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def tin_050_lull_persistence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive low-vol streak within trailing 63 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume < avg)
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            cur = cur + 1 if v else 0
            if cur > mx:
                mx = cur
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


# --- Group F (051-060): Activity regime persistence ---

def tin_051_activity_regime_up_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days classified as 'active regime' (active day AND above-avg vol) in 21d."""
    avg  = _rolling_mean(volume, _TD_MON)
    act  = (_active_day(close, high, low) > 0) & (volume > avg)
    return _rolling_sum(act.astype(float), _TD_MON)


def tin_052_activity_regime_up_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days classified as active regime."""
    avg  = _rolling_mean(volume, _TD_MON)
    act  = (_active_day(close, high, low) > 0) & (volume > avg)
    return _rolling_sum(act.astype(float), _TD_QTR) / _TD_QTR


def tin_053_activity_regime_persistence_consec(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive active-regime days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (_active_day(close, high, low) > 0) & (volume > avg)
    return _consec_streak(cond)


def tin_054_lull_regime_persistence_consec(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive lull-regime days (inactive or below-avg vol)."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (_active_day(close, high, low) == 0) | (volume < 0.5 * avg)
    return _consec_streak(cond)


def tin_055_regime_transition_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of active-to-lull or lull-to-active transitions in 21 days."""
    avg    = _rolling_mean(volume, _TD_MON)
    regime = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(int)
    trans  = (regime != regime.shift(1)).astype(float)
    return _rolling_sum(trans, _TD_MON)


def tin_056_regime_transition_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of active/lull regime transitions in trailing 63 days."""
    avg    = _rolling_mean(volume, _TD_MON)
    regime = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(int)
    trans  = (regime != regime.shift(1)).astype(float)
    return _rolling_sum(trans, _TD_QTR)


def tin_057_activity_regime_frac_5d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day active-regime fraction to 252-day average fraction."""
    avg  = _rolling_mean(volume, _TD_MON)
    act  = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(float)
    f5   = _rolling_sum(act, _TD_WEEK) / _TD_WEEK
    f252 = _rolling_mean(f5, _TD_YEAR)
    return _safe_div(f5, f252)


def tin_058_active_regime_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day active-regime fraction within 252-day distribution."""
    avg  = _rolling_mean(volume, _TD_MON)
    act  = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(float)
    f21  = _rolling_sum(act, _TD_MON) / _TD_MON
    m    = _rolling_mean(f21, _TD_YEAR)
    s    = _rolling_std(f21, _TD_YEAR)
    return _safe_div(f21 - m, s)


def tin_059_lull_regime_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days classified as lull regime."""
    avg  = _rolling_mean(volume, _TD_MON)
    lull = ((_active_day(close, high, low) == 0) | (volume < 0.5 * avg)).astype(float)
    return _rolling_sum(lull, _TD_MON) / _TD_MON


def tin_060_lull_regime_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days classified as lull regime."""
    avg  = _rolling_mean(volume, _TD_MON)
    lull = ((_active_day(close, high, low) == 0) | (volume < 0.5 * avg)).astype(float)
    return _rolling_sum(lull, _TD_QTR) / _TD_QTR


# --- Group G (061-075): Trend in activity intensity ---

def tin_061_active_frac_5d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day active-day fraction within its trailing 252-day distribution."""
    f5 = tin_001_active_day_frac_5d(close, high, low)
    return f5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_062_active_frac_21d_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day active-day fraction over trailing 63 days."""
    f21 = tin_002_active_day_frac_21d(close, high, low)
    return _linslope(f21, _TD_QTR)


def tin_063_vol_per_range_21d_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day vol/range over trailing 63 days."""
    vpr21 = tin_011_vol_per_range_21d(close, high, low, volume)
    return _linslope(vpr21, _TD_QTR)


def tin_064_high_vol_frac_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day high-vol-day fraction within its 252-day distribution."""
    avg  = _rolling_mean(volume, _TD_YEAR)
    cond = (volume > avg).astype(float)
    f21  = _rolling_sum(cond, _TD_MON) / _TD_MON
    return f21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_065_lull_frac_21d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day lull-regime fraction within its 252-day distribution."""
    f21 = tin_059_lull_regime_frac_21d(close, high, low, volume)
    return f21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_066_discovery_frac_21d_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day price-discovery event fraction over 63 days."""
    rng     = high - low
    med_rng = _rolling_median(rng, _TD_QTR)
    events  = ((close != close.shift(1)) & (rng > med_rng)).astype(float)
    f21     = _rolling_sum(events, _TD_MON) / _TD_MON
    return _linslope(f21, _TD_QTR)


def tin_067_burst_lull_ratio_21d_diff_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day burst/lull ratio."""
    ratio = tin_045_burst_lull_ratio_21d(close, volume)
    return ratio.diff(_TD_WEEK)


def tin_068_active_frac_ewm21_vs_ewm63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """EMA21 of active-day fraction minus EMA63 (momentum of activity)."""
    act  = _active_day(close, high, low)
    e21  = _ewm_mean(act, _TD_MON)
    e63  = _ewm_mean(act, _TD_QTR)
    return e21 - e63


def tin_069_vol_per_range_ewm21_vs_ewm63(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA21 minus EMA63 of vol/range series (momentum of trade-intensity proxy)."""
    rng  = (high - low).replace(0, np.nan)
    vpr  = _safe_div(volume, rng)
    e21  = _ewm_mean(vpr, _TD_MON)
    e63  = _ewm_mean(vpr, _TD_QTR)
    return e21 - e63


def tin_070_activity_trend_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of composite activity signal (active-day * vol_norm) over 21 days."""
    act     = _active_day(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_n   = _safe_div(volume, avg_vol.replace(0, np.nan))
    signal  = act * vol_n
    return _linslope(signal, _TD_MON)


def tin_071_activity_trend_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of composite activity signal over 63 days."""
    act     = _active_day(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_n   = _safe_div(volume, avg_vol.replace(0, np.nan))
    signal  = act * vol_n
    return _linslope(signal, _TD_QTR)


def tin_072_active_regime_transitions_per_week_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean weekly transition count between active/lull regimes over 63 days."""
    avg    = _rolling_mean(volume, _TD_MON)
    regime = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(int)
    trans  = (regime != regime.shift(1)).astype(float)
    weekly = _rolling_sum(trans, _TD_WEEK)
    return _rolling_mean(weekly, _TD_QTR)


def tin_073_active_day_frac_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day active-day fraction within 252-day distribution."""
    f21 = tin_002_active_day_frac_21d(close, high, low)
    return f21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_074_vol_per_range_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day vol/range within 252-day distribution."""
    vpr21 = tin_011_vol_per_range_21d(close, high, low, volume)
    return vpr21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_075_activity_composite_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite activity score: avg of z-scored active-frac, vol/range, and high-vol-frac."""
    act   = _active_day(close, high, low)
    f21   = _rolling_mean(act, _TD_MON)
    f21_z = _safe_div(f21 - _rolling_mean(f21, _TD_YEAR), _rolling_std(f21, _TD_YEAR))

    rng   = (high - low).replace(0, np.nan)
    vpr   = _safe_div(volume, rng)
    vpr21 = _rolling_mean(vpr, _TD_MON)
    vpr_z = _safe_div(vpr21 - _rolling_mean(vpr21, _TD_YEAR), _rolling_std(vpr21, _TD_YEAR))

    avg252 = _rolling_mean(volume, _TD_YEAR)
    hvf21  = _rolling_sum((volume > avg252).astype(float), _TD_MON) / _TD_MON
    hvf_z  = _safe_div(hvf21 - _rolling_mean(hvf21, _TD_YEAR), _rolling_std(hvf21, _TD_YEAR))

    return (f21_z + vpr_z + hvf_z) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

TRADING_INTENSITY_REGISTRY_001_075 = {
    "tin_001_active_day_frac_5d": {"inputs": ["close", "high", "low"], "func": tin_001_active_day_frac_5d},
    "tin_002_active_day_frac_21d": {"inputs": ["close", "high", "low"], "func": tin_002_active_day_frac_21d},
    "tin_003_active_day_frac_63d": {"inputs": ["close", "high", "low"], "func": tin_003_active_day_frac_63d},
    "tin_004_active_day_frac_126d": {"inputs": ["close", "high", "low"], "func": tin_004_active_day_frac_126d},
    "tin_005_active_day_frac_252d": {"inputs": ["close", "high", "low"], "func": tin_005_active_day_frac_252d},
    "tin_006_active_day_count_21d": {"inputs": ["close", "high", "low"], "func": tin_006_active_day_count_21d},
    "tin_007_active_day_count_63d": {"inputs": ["close", "high", "low"], "func": tin_007_active_day_count_63d},
    "tin_008_active_frac_5d_vs_63d": {"inputs": ["close", "high", "low"], "func": tin_008_active_frac_5d_vs_63d},
    "tin_009_active_frac_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": tin_009_active_frac_21d_vs_252d},
    "tin_010_active_day_frac_zscore_252d": {"inputs": ["close", "high", "low"], "func": tin_010_active_day_frac_zscore_252d},
    "tin_011_vol_per_range_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_011_vol_per_range_21d},
    "tin_012_vol_per_range_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_012_vol_per_range_63d},
    "tin_013_vol_per_range_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_013_vol_per_range_252d},
    "tin_014_vol_per_range_21d_vs_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_014_vol_per_range_21d_vs_252d},
    "tin_015_vol_per_range_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_015_vol_per_range_zscore_252d},
    "tin_016_vol_per_pct_range_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_016_vol_per_pct_range_21d},
    "tin_017_vol_per_pct_range_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_017_vol_per_pct_range_63d},
    "tin_018_range_per_volume_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_018_range_per_volume_21d},
    "tin_019_range_per_volume_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_019_range_per_volume_63d},
    "tin_020_range_per_volume_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_020_range_per_volume_zscore_252d},
    "tin_021_meaningful_vol_day_frac_21d": {"inputs": ["close", "volume"], "func": tin_021_meaningful_vol_day_frac_21d},
    "tin_022_meaningful_vol_day_frac_63d": {"inputs": ["close", "volume"], "func": tin_022_meaningful_vol_day_frac_63d},
    "tin_023_meaningful_vol_day_frac_252d": {"inputs": ["close", "volume"], "func": tin_023_meaningful_vol_day_frac_252d},
    "tin_024_high_vol_day_frac_21d": {"inputs": ["close", "volume"], "func": tin_024_high_vol_day_frac_21d},
    "tin_025_high_vol_day_frac_63d": {"inputs": ["close", "volume"], "func": tin_025_high_vol_day_frac_63d},
    "tin_026_high_vol_day_frac_5d_vs_63d": {"inputs": ["close", "volume"], "func": tin_026_high_vol_day_frac_5d_vs_63d},
    "tin_027_low_vol_lull_day_frac_21d": {"inputs": ["close", "volume"], "func": tin_027_low_vol_lull_day_frac_21d},
    "tin_028_low_vol_lull_day_frac_63d": {"inputs": ["close", "volume"], "func": tin_028_low_vol_lull_day_frac_63d},
    "tin_029_active_vol_ratio_21d": {"inputs": ["close", "volume"], "func": tin_029_active_vol_ratio_21d},
    "tin_030_active_to_total_session_ratio_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_030_active_to_total_session_ratio_63d},
    "tin_031_distinct_close_count_21d": {"inputs": ["close"], "func": tin_031_distinct_close_count_21d},
    "tin_032_distinct_close_count_63d": {"inputs": ["close"], "func": tin_032_distinct_close_count_63d},
    "tin_033_distinct_close_frac_21d": {"inputs": ["close"], "func": tin_033_distinct_close_frac_21d},
    "tin_034_price_discovery_events_21d": {"inputs": ["close", "high", "low"], "func": tin_034_price_discovery_events_21d},
    "tin_035_price_discovery_events_63d": {"inputs": ["close", "high", "low"], "func": tin_035_price_discovery_events_63d},
    "tin_036_new_high_or_low_day_frac_21d": {"inputs": ["close", "high", "low"], "func": tin_036_new_high_or_low_day_frac_21d},
    "tin_037_new_high_or_low_day_frac_63d": {"inputs": ["close", "high", "low"], "func": tin_037_new_high_or_low_day_frac_63d},
    "tin_038_both_new_high_and_low_frac_21d": {"inputs": ["high", "low"], "func": tin_038_both_new_high_and_low_frac_21d},
    "tin_039_close_change_count_5d": {"inputs": ["close"], "func": tin_039_close_change_count_5d},
    "tin_040_discovery_intensity_ratio_5d_vs_252d": {"inputs": ["close", "high", "low"], "func": tin_040_discovery_intensity_ratio_5d_vs_252d},
    "tin_041_active_day_consec_streak": {"inputs": ["close", "high", "low"], "func": tin_041_active_day_consec_streak},
    "tin_042_lull_day_consec_streak": {"inputs": ["close", "high", "low"], "func": tin_042_lull_day_consec_streak},
    "tin_043_high_vol_consec_streak": {"inputs": ["close", "volume"], "func": tin_043_high_vol_consec_streak},
    "tin_044_low_vol_consec_streak": {"inputs": ["close", "volume"], "func": tin_044_low_vol_consec_streak},
    "tin_045_burst_lull_ratio_21d": {"inputs": ["close", "volume"], "func": tin_045_burst_lull_ratio_21d},
    "tin_046_burst_lull_ratio_63d": {"inputs": ["close", "volume"], "func": tin_046_burst_lull_ratio_63d},
    "tin_047_burst_persistence_21d": {"inputs": ["close", "volume"], "func": tin_047_burst_persistence_21d},
    "tin_048_lull_persistence_21d": {"inputs": ["close", "volume"], "func": tin_048_lull_persistence_21d},
    "tin_049_burst_persistence_63d": {"inputs": ["close", "volume"], "func": tin_049_burst_persistence_63d},
    "tin_050_lull_persistence_63d": {"inputs": ["close", "volume"], "func": tin_050_lull_persistence_63d},
    "tin_051_activity_regime_up_count_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_051_activity_regime_up_count_21d},
    "tin_052_activity_regime_up_frac_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_052_activity_regime_up_frac_63d},
    "tin_053_activity_regime_persistence_consec": {"inputs": ["close", "high", "low", "volume"], "func": tin_053_activity_regime_persistence_consec},
    "tin_054_lull_regime_persistence_consec": {"inputs": ["close", "high", "low", "volume"], "func": tin_054_lull_regime_persistence_consec},
    "tin_055_regime_transition_count_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_055_regime_transition_count_21d},
    "tin_056_regime_transition_count_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_056_regime_transition_count_63d},
    "tin_057_activity_regime_frac_5d_vs_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_057_activity_regime_frac_5d_vs_252d},
    "tin_058_active_regime_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_058_active_regime_zscore_252d},
    "tin_059_lull_regime_frac_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_059_lull_regime_frac_21d},
    "tin_060_lull_regime_frac_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_060_lull_regime_frac_63d},
    "tin_061_active_frac_5d_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": tin_061_active_frac_5d_pct_rank_252d},
    "tin_062_active_frac_21d_slope_63d": {"inputs": ["close", "high", "low"], "func": tin_062_active_frac_21d_slope_63d},
    "tin_063_vol_per_range_21d_slope_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_063_vol_per_range_21d_slope_63d},
    "tin_064_high_vol_frac_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": tin_064_high_vol_frac_21d_pct_rank_252d},
    "tin_065_lull_frac_21d_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_065_lull_frac_21d_pct_rank_252d},
    "tin_066_discovery_frac_21d_slope_63d": {"inputs": ["close", "high", "low"], "func": tin_066_discovery_frac_21d_slope_63d},
    "tin_067_burst_lull_ratio_21d_diff_5d": {"inputs": ["close", "volume"], "func": tin_067_burst_lull_ratio_21d_diff_5d},
    "tin_068_active_frac_ewm21_vs_ewm63": {"inputs": ["close", "high", "low"], "func": tin_068_active_frac_ewm21_vs_ewm63},
    "tin_069_vol_per_range_ewm21_vs_ewm63": {"inputs": ["close", "high", "low", "volume"], "func": tin_069_vol_per_range_ewm21_vs_ewm63},
    "tin_070_activity_trend_slope_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_070_activity_trend_slope_21d},
    "tin_071_activity_trend_slope_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_071_activity_trend_slope_63d},
    "tin_072_active_regime_transitions_per_week_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_072_active_regime_transitions_per_week_63d},
    "tin_073_active_day_frac_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": tin_073_active_day_frac_pct_rank_252d},
    "tin_074_vol_per_range_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_074_vol_per_range_pct_rank_252d},
    "tin_075_activity_composite_score": {"inputs": ["close", "high", "low", "volume"], "func": tin_075_activity_composite_score},
}
