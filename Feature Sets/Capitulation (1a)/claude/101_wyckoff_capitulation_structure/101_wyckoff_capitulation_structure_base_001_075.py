"""
101_wyckoff_capitulation_structure — Base Features 001-075
Domain: Wyckoff selling-climax -> automatic-rally -> secondary-test -> spring
        sequence measurement. Captures the structural fingerprint of a tested
        capitulation low (climax on extreme volume, rebound, low-volume retest).
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _days_since(flag: pd.Series) -> pd.Series:
    """Trading days since the last True/1 in a 0/1 flag Series."""
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag > 0).ffill()
    return idx - last


def _days_since_rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Trading days since the minimum within a trailing window of length w."""
    return s.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(len(x) - 1 - np.argmin(x)), raw=True)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return ((xi - xi_m) * (x - x.mean())).sum() / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


def _sc_flag(close, high, low, volume, w=_TD_YEAR):
    """Selling-climax flag: extreme down day on extreme volume within window w."""
    ret = _daily_ret(close)
    ret_q = ret.rolling(w, min_periods=max(5, w // 4)).quantile(0.05)
    vol_q = volume.rolling(w, min_periods=max(5, w // 4)).quantile(0.95)
    return ((ret <= ret_q) & (volume >= vol_q)).astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Selling-climax detection & magnitude ---

def wcs_001_sc_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Selling-climax flag: 5th-pctile down day on 95th-pctile volume (252d)."""
    return _sc_flag(close, high, low, volume, _TD_YEAR)


def wcs_002_days_since_sc_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Trading days since the most recent 252d selling climax."""
    return _days_since(_sc_flag(close, high, low, volume, _TD_YEAR))


def wcs_003_sc_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling-climax days within the trailing 252 days."""
    return _rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_YEAR)


def wcs_004_sc_count_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling-climax days within the trailing 63 days."""
    return _rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_QTR)


def wcs_005_largest_down_day_63d(close: pd.Series) -> pd.Series:
    """Most negative single-day return within trailing 63 days (climax magnitude)."""
    return _rolling_min(_daily_ret(close), _TD_QTR)


def wcs_006_largest_down_day_252d(close: pd.Series) -> pd.Series:
    """Most negative single-day return within trailing 252 days."""
    return _rolling_min(_daily_ret(close), _TD_YEAR)


def wcs_007_sc_volume_spike_63d(volume: pd.Series) -> pd.Series:
    """Peak 63-day volume relative to 63-day median volume (climax volume spike)."""
    return _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def wcs_008_sc_range_expansion(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Peak 21-day true range vs 63-day average true range (climax range blow-out)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_max(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))


def wcs_009_climax_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax intensity: magnitude of worst down-day return scaled by volume z-score."""
    ret = _daily_ret(close)
    volz = _zscore_rolling(volume, _TD_QTR)
    return _rolling_min(ret * volz.clip(lower=0), _TD_QTR)


def wcs_010_panic_selloff_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of down days on above-median volume within trailing 63 days."""
    ret = _daily_ret(close)
    hi_vol = volume > _rolling_median(volume, _TD_QTR)
    return _rolling_sum(((ret < 0) & hi_vol).astype(float), _TD_QTR)


def wcs_011_sc_recency_weight_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Exponentially-decayed recency weight of selling-climax events (252d)."""
    flag = _sc_flag(close, high, low, volume, _TD_YEAR)
    return flag.ewm(span=_TD_QTR, min_periods=_TD_MON).mean()


def wcs_012_climax_volume_pctile_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of the peak 5-day volume within the trailing 252 days."""
    return _rolling_rank_pct(_rolling_max(volume, _TD_WEEK), _TD_YEAR)


# --- Group B (013-026): Automatic-rally measures ---

def wcs_013_bounce_off_63d_low(close: pd.Series) -> pd.Series:
    """Percent the close sits above the trailing 63-day closing low."""
    return _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))


def wcs_014_bounce_off_252d_low(close: pd.Series) -> pd.Series:
    """Percent the close sits above the trailing 252-day closing low."""
    return _safe_div(close - _rolling_min(close, _TD_YEAR), _rolling_min(close, _TD_YEAR))


def wcs_015_ar_strength_21d(close: pd.Series) -> pd.Series:
    """Automatic-rally strength: 21d high vs 63d low (rebound off the climax low)."""
    return _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_QTR),
                     _rolling_min(close, _TD_QTR))


def wcs_016_rally_from_low_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rebound from 63-day low expressed in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_MON)
    return _safe_div(close - _rolling_min(close, _TD_QTR), atr)


def wcs_017_days_since_63d_low(close: pd.Series) -> pd.Series:
    """Trading days since the trailing 63-day closing low was set."""
    return _days_since_rolling_min(close, _TD_QTR)


def wcs_018_days_since_252d_low(close: pd.Series) -> pd.Series:
    """Trading days since the trailing 252-day closing low was set."""
    return _days_since_rolling_min(close, _TD_YEAR)


def wcs_019_low_to_close_recovery_frac(close: pd.Series) -> pd.Series:
    """Recovery fraction of close between the 63d low and 63d high."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _safe_div(close - lo, hi - lo)


def wcs_020_ar_volume_ratio(volume: pd.Series) -> pd.Series:
    """Recent 10-day volume vs 63-day median (rally participation)."""
    return _safe_div(_rolling_mean(volume, 10), _rolling_median(volume, _TD_QTR))


def wcs_021_post_low_max_gain_63d(close: pd.Series) -> pd.Series:
    """Largest single-day gain within trailing 63 days (rally thrust)."""
    return _rolling_max(_daily_ret(close), _TD_QTR)


def wcs_022_rally_up_days_21d(close: pd.Series) -> pd.Series:
    """Count of up days within the trailing 21 days."""
    return _rolling_sum((_daily_ret(close) > 0).astype(float), _TD_MON)


def wcs_023_rebound_velocity_10d(close: pd.Series) -> pd.Series:
    """OLS slope of close over the last 10 days (rebound velocity)."""
    return _safe_div(_linslope(close, 10), _rolling_mean(close, _TD_MON))


def wcs_024_automatic_rally_height_21d(close: pd.Series) -> pd.Series:
    """21-day high-low range as a fraction of the 21-day low."""
    return _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                     _rolling_min(close, _TD_MON))


def wcs_025_undercut_then_close_higher(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's low pierced the prior 21d low but close held above it."""
    prior_low = _rolling_min(low, _TD_MON).shift(1)
    return ((low < prior_low) & (close > prior_low)).astype(float)


def wcs_026_bounce_consistency_10d(close: pd.Series) -> pd.Series:
    """Fraction of the last 10 days that closed up (rally consistency)."""
    return _rolling_mean((_daily_ret(close) > 0).astype(float), 10)


# --- Group C (027-042): Secondary-test / retest measures ---

def wcs_027_retest_proximity_63d(close: pd.Series) -> pd.Series:
    """Closeness of the close to the trailing 63-day low (1 = at the low)."""
    lo = _rolling_min(close, _TD_QTR)
    return _safe_div(lo, close)


def wcs_028_retest_volume_contraction(volume: pd.Series) -> pd.Series:
    """Recent 5-day volume vs the peak 63-day volume (low = clean low-vol test)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume, _TD_QTR))


def wcs_029_retest_range_contraction(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Recent 5-day true range vs peak 63-day true range (range contraction)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_max(tr, _TD_QTR))


def wcs_030_test_on_lower_volume_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: close in bottom quartile of 63d range AND volume below 63d median."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return ((pos < 0.25) & lo_vol).astype(float)


def wcs_031_volume_at_low_vs_median(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on days the close is in the bottom decile vs 63d median volume."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    near_low_vol = volume.where(pos < 0.10)
    return _safe_div(_rolling_mean(near_low_vol, _TD_QTR), _rolling_median(volume, _TD_QTR))


def wcs_032_secondary_test_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of low-volume retests of the 252d low region within 252 days."""
    pos = _safe_div(close - _rolling_min(close, _TD_YEAR),
                    _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR))
    lo_vol = volume < _rolling_median(volume, _TD_YEAR)
    return _rolling_sum(((pos < 0.15) & lo_vol).astype(float), _TD_YEAR)


def wcs_033_low_zone_volume_trend(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of volume over 21 days while the close sits in the lower range third."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    v = volume.where(pos < 0.33)
    return _safe_div(_linslope(v.ffill(), _TD_MON), _rolling_median(volume, _TD_QTR))


def wcs_034_double_bottom_proximity(close: pd.Series) -> pd.Series:
    """Similarity of the recent 21d low to the prior 63d low (double-bottom test)."""
    recent_low = _rolling_min(close, _TD_MON)
    prior_low = _rolling_min(close, _TD_QTR).shift(_TD_MON)
    return _safe_div((recent_low - prior_low).abs(), prior_low)


def wcs_035_retest_depth_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """How far the recent low pierced the prior 63d low (negative = undercut)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(_TD_MON)
    recent_low = _rolling_min(low, _TD_MON)
    return _safe_div(recent_low - prior_low, prior_low)


def wcs_036_range_narrowing_near_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR ratio (5d/21d) measured while the close is near the 63d low."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))


def wcs_037_test_quality_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite test quality: near the low + low volume + narrow range (0-3)."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    tr = _tr(close, high, low)
    near = (pos < 0.20).astype(float)
    lo_vol = (volume < _rolling_median(volume, _TD_QTR)).astype(float)
    narrow = (tr < _rolling_median(tr, _TD_QTR)).astype(float)
    return near + lo_vol + narrow


def wcs_038_volume_dryup_at_low(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day vs 63-day volume ratio measured when close is in the bottom decile."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    ratio = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))
    return ratio.where(pos < 0.10).ffill()


def wcs_039_higher_low_flag(low: pd.Series) -> pd.Series:
    """Flag: current 21d low is above the prior 21d low (higher-low forming)."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    return (cur > prior).astype(float)


def wcs_040_higher_low_streak(low: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 21d low being above the prior 21d low."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    f = (cur > prior).astype(float)
    grp = (f == 0).cumsum()
    return f.groupby(grp).cumsum()


def wcs_041_retest_close_above_low(close: pd.Series) -> pd.Series:
    """Margin by which the close holds above the trailing 63d low (small = at test)."""
    return _safe_div(close - _rolling_min(close, _TD_QTR), close)


def wcs_042_lower_wick_at_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower-wick fraction of the daily bar (supply rejected from the lows)."""
    body_low = pd.concat([close, close.shift(0)], axis=1).min(axis=1)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(close - low, rng)


# --- Group D (043-056): Trading-range / consolidation structure ---

def wcs_043_range_width_63d(close: pd.Series) -> pd.Series:
    """63-day high-low range as a fraction of the 63-day low."""
    return _safe_div(_rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR),
                     _rolling_min(close, _TD_QTR))


def wcs_044_range_width_21d(close: pd.Series) -> pd.Series:
    """21-day high-low range as a fraction of the 21-day low."""
    return _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                     _rolling_min(close, _TD_MON))


def wcs_045_price_in_range_position_63d(close: pd.Series) -> pd.Series:
    """Close position within the 63-day range (0 = low, 1 = high)."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _safe_div(close - lo, hi - lo)


def wcs_046_time_in_low_third_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days the close sat in the lower third of its range."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    pos = _safe_div(close - lo, hi - lo)
    return _rolling_mean((pos < 0.33).astype(float), _TD_QTR)


def wcs_047_consolidation_flag(close: pd.Series) -> pd.Series:
    """Flag: 21d range width below its 252d median (tight consolidation)."""
    rw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    return (rw < _rolling_median(rw, _TD_YEAR)).astype(float)


def wcs_048_consolidation_duration(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of tight (sub-median) 21d range width."""
    rw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    f = (rw < _rolling_median(rw, _TD_YEAR)).astype(float)
    grp = (f == 0).cumsum()
    return f.groupby(grp).cumsum()


def wcs_049_range_contraction_ratio(close: pd.Series) -> pd.Series:
    """21-day range divided by 63-day range (range contraction)."""
    r21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    r63 = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    return _safe_div(r21, r63)


def wcs_050_sideways_score_21d(close: pd.Series) -> pd.Series:
    """Flatness score: 1 - |normalized 21d slope| (1 = perfectly sideways)."""
    slope = _safe_div(_linslope(close, _TD_MON), _rolling_std(close, _TD_MON))
    return 1.0 - slope.abs()


def wcs_051_volatility_compression(close: pd.Series) -> pd.Series:
    """21-day return std divided by 63-day return std (volatility compression)."""
    ret = _daily_ret(close)
    return _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_QTR))


def wcs_052_close_clustering_21d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of close over 21 days (price clustering near low)."""
    return _safe_div(_rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))


def wcs_053_bar_overlap_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 bars overlapping the prior bar's high-low range."""
    overlap = (low <= high.shift(1)) & (high >= low.shift(1))
    return _rolling_mean(overlap.astype(float), _TD_MON)


def wcs_054_base_building_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite base score: tight range + near low + low volume (0-3)."""
    rw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    tight = (rw < _rolling_median(rw, _TD_YEAR)).astype(float)
    near = (pos < 0.33).astype(float)
    lo_vol = (volume < _rolling_median(volume, _TD_QTR)).astype(float)
    return tight + near + lo_vol


def wcs_055_range_low_touches_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days the daily low touched within 2% of the 63d low."""
    lo = _rolling_min(low, _TD_QTR)
    touch = low <= lo * 1.02
    return _rolling_sum(touch.astype(float), _TD_QTR)


def wcs_056_range_high_touches_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of days the daily high touched within 2% of the 63d high."""
    hi = _rolling_max(high, _TD_QTR)
    touch = high >= hi * 0.98
    return _rolling_sum(touch.astype(float), _TD_QTR)


# --- Group E (057-066): Spring / shakeout in sequence ---

def wcs_057_spring_flag_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Spring flag: low undercut the prior 63d low intraday, close reclaimed it."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    return ((low < prior_low) & (close > prior_low)).astype(float)


def wcs_058_spring_count_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of spring events within the trailing 252 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _rolling_sum(spring, _TD_YEAR)


def wcs_059_days_since_spring(close: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent spring event."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _days_since(spring)


def wcs_060_shakeout_depth_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Depth the daily low pierced below the prior 63d low (shakeout magnitude)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    pierce = (low - prior_low).clip(upper=0)
    return _safe_div(pierce, prior_low)


def wcs_061_spring_recovery_same_day(close: pd.Series, low: pd.Series) -> pd.Series:
    """Same-day recovery: close vs daily low when the low undercut prior 63d low."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    rec = _safe_div(close - low, low)
    return rec.where(low < prior_low).fillna(0.0)


def wcs_062_false_breakdown_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 252d low undercut then reclaimed by the close within 5 days."""
    prior_low = _rolling_min(low, _TD_YEAR).shift(1)
    undercut = (low < prior_low)
    reclaimed = (close > prior_low)
    return (_rolling_sum(undercut.astype(float), _TD_WEEK) > 0).astype(float) * reclaimed.astype(float)


def wcs_063_undercut_volume_ratio(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on undercut days vs 63d median volume (low = high-quality spring)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    uv = volume.where(low < prior_low)
    return _safe_div(uv.ffill(), _rolling_median(volume, _TD_QTR))


def wcs_064_spring_quality_score(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Spring quality: undercut + same-day reclaim + below-median volume (0-3)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    undercut = (low < prior_low).astype(float)
    reclaim = (close > prior_low).astype(float)
    lo_vol = (volume < _rolling_median(volume, _TD_QTR)).astype(float)
    return undercut + reclaim + lo_vol


def wcs_065_terminal_shakeout_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Deep undercut on high volume followed by a reclaiming close (0-3)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    deep = (low < prior_low * 0.97).astype(float)
    hi_vol = (volume > _rolling_median(volume, _TD_QTR) * 1.5).astype(float)
    reclaim = (close > prior_low).astype(float)
    return deep + hi_vol + reclaim


def wcs_066_low_pierce_recovery_speed(close: pd.Series, low: pd.Series) -> pd.Series:
    """Days since the last 63d-low undercut (recovery speed proxy)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    return _days_since((low < prior_low).astype(float))


# --- Group F (067-075): Effort-vs-result, no-supply, exhaustion ---

def wcs_067_effort_vs_result_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score minus absolute-return z-score (high effort, low result)."""
    volz = _zscore_rolling(volume, _TD_QTR)
    retz = _zscore_rolling(_daily_ret(close).abs(), _TD_QTR)
    return volz - retz


def wcs_068_no_supply_bar(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """No-supply bar flag: down day, narrow range, below-median volume."""
    tr = _tr(close, high, low)
    down = _daily_ret(close) < 0
    narrow = tr < _rolling_median(tr, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return (down & narrow & lo_vol).astype(float)


def wcs_069_no_supply_count_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of no-supply bars within the trailing 21 days."""
    tr = _tr(close, high, low)
    down = _daily_ret(close) < 0
    narrow = tr < _rolling_median(tr, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return _rolling_sum((down & narrow & lo_vol).astype(float), _TD_MON)


def wcs_070_down_day_volume_fade_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of down-day volume over 21 days (negative = selling exhaustion)."""
    dv = volume.where(_daily_ret(close) < 0)
    return _safe_div(_linslope(dv.ffill(), _TD_MON), _rolling_median(volume, _TD_QTR))


def wcs_071_down_volume_share_trend(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Change in down-day volume share: recent 21d vs prior 21d."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    share = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(volume, _TD_MON))
    return share - share.shift(_TD_MON)


def wcs_072_absorption_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """High volume absorbed with small price decline (selling absorbed near low)."""
    volz = _zscore_rolling(volume, _TD_QTR).clip(lower=0)
    move = _daily_ret(close).abs()
    return _safe_div(volz, move + _EPS)


def wcs_073_climax_to_test_volume_ratio(volume: pd.Series) -> pd.Series:
    """Recent 5-day volume vs the peak 21-day volume (climax-to-test contraction)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume, _TD_MON))


def wcs_074_wyckoff_phase_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite presence of climax + rally + low-volume test phases (0-3)."""
    sc = (_rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_QTR) > 0).astype(float)
    ar = (_rolling_max(_daily_ret(close), _TD_QTR) > 0.05).astype(float)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    st = ((pos < 0.25) & (volume < _rolling_median(volume, _TD_QTR))).astype(float)
    return sc + ar + st


def wcs_075_capitulation_sequence_completeness(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ordered-sequence completeness: climax, then rally, then a low-volume retest."""
    sc = _rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_HALF)
    rally = _rolling_max(_daily_ret(close), _TD_QTR)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    seq = (sc > 0).astype(float) + (rally > 0.04).astype(float) + (pos < 0.30).astype(float)
    return seq / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

WYCKOFF_CAPITULATION_STRUCTURE_REGISTRY_001_075 = {
    "wcs_001_sc_flag_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_001_sc_flag_252d},
    "wcs_002_days_since_sc_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_002_days_since_sc_252d},
    "wcs_003_sc_count_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_003_sc_count_252d},
    "wcs_004_sc_count_63d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_004_sc_count_63d},
    "wcs_005_largest_down_day_63d": {"inputs": ["close"], "func": wcs_005_largest_down_day_63d},
    "wcs_006_largest_down_day_252d": {"inputs": ["close"], "func": wcs_006_largest_down_day_252d},
    "wcs_007_sc_volume_spike_63d": {"inputs": ["volume"], "func": wcs_007_sc_volume_spike_63d},
    "wcs_008_sc_range_expansion": {"inputs": ["close", "high", "low"], "func": wcs_008_sc_range_expansion},
    "wcs_009_climax_intensity_63d": {"inputs": ["close", "volume"], "func": wcs_009_climax_intensity_63d},
    "wcs_010_panic_selloff_score_63d": {"inputs": ["close", "volume"], "func": wcs_010_panic_selloff_score_63d},
    "wcs_011_sc_recency_weight_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_011_sc_recency_weight_252d},
    "wcs_012_climax_volume_pctile_252d": {"inputs": ["volume"], "func": wcs_012_climax_volume_pctile_252d},
    "wcs_013_bounce_off_63d_low": {"inputs": ["close"], "func": wcs_013_bounce_off_63d_low},
    "wcs_014_bounce_off_252d_low": {"inputs": ["close"], "func": wcs_014_bounce_off_252d_low},
    "wcs_015_ar_strength_21d": {"inputs": ["close"], "func": wcs_015_ar_strength_21d},
    "wcs_016_rally_from_low_atr": {"inputs": ["close", "high", "low"], "func": wcs_016_rally_from_low_atr},
    "wcs_017_days_since_63d_low": {"inputs": ["close"], "func": wcs_017_days_since_63d_low},
    "wcs_018_days_since_252d_low": {"inputs": ["close"], "func": wcs_018_days_since_252d_low},
    "wcs_019_low_to_close_recovery_frac": {"inputs": ["close"], "func": wcs_019_low_to_close_recovery_frac},
    "wcs_020_ar_volume_ratio": {"inputs": ["volume"], "func": wcs_020_ar_volume_ratio},
    "wcs_021_post_low_max_gain_63d": {"inputs": ["close"], "func": wcs_021_post_low_max_gain_63d},
    "wcs_022_rally_up_days_21d": {"inputs": ["close"], "func": wcs_022_rally_up_days_21d},
    "wcs_023_rebound_velocity_10d": {"inputs": ["close"], "func": wcs_023_rebound_velocity_10d},
    "wcs_024_automatic_rally_height_21d": {"inputs": ["close"], "func": wcs_024_automatic_rally_height_21d},
    "wcs_025_undercut_then_close_higher": {"inputs": ["close", "low"], "func": wcs_025_undercut_then_close_higher},
    "wcs_026_bounce_consistency_10d": {"inputs": ["close"], "func": wcs_026_bounce_consistency_10d},
    "wcs_027_retest_proximity_63d": {"inputs": ["close"], "func": wcs_027_retest_proximity_63d},
    "wcs_028_retest_volume_contraction": {"inputs": ["volume"], "func": wcs_028_retest_volume_contraction},
    "wcs_029_retest_range_contraction": {"inputs": ["close", "high", "low"], "func": wcs_029_retest_range_contraction},
    "wcs_030_test_on_lower_volume_flag": {"inputs": ["close", "volume"], "func": wcs_030_test_on_lower_volume_flag},
    "wcs_031_volume_at_low_vs_median": {"inputs": ["close", "volume"], "func": wcs_031_volume_at_low_vs_median},
    "wcs_032_secondary_test_count_252d": {"inputs": ["close", "volume"], "func": wcs_032_secondary_test_count_252d},
    "wcs_033_low_zone_volume_trend": {"inputs": ["close", "volume"], "func": wcs_033_low_zone_volume_trend},
    "wcs_034_double_bottom_proximity": {"inputs": ["close"], "func": wcs_034_double_bottom_proximity},
    "wcs_035_retest_depth_ratio": {"inputs": ["close", "low"], "func": wcs_035_retest_depth_ratio},
    "wcs_036_range_narrowing_near_low": {"inputs": ["close", "high", "low"], "func": wcs_036_range_narrowing_near_low},
    "wcs_037_test_quality_score": {"inputs": ["close", "high", "low", "volume"], "func": wcs_037_test_quality_score},
    "wcs_038_volume_dryup_at_low": {"inputs": ["close", "volume"], "func": wcs_038_volume_dryup_at_low},
    "wcs_039_higher_low_flag": {"inputs": ["low"], "func": wcs_039_higher_low_flag},
    "wcs_040_higher_low_streak": {"inputs": ["low"], "func": wcs_040_higher_low_streak},
    "wcs_041_retest_close_above_low": {"inputs": ["close"], "func": wcs_041_retest_close_above_low},
    "wcs_042_lower_wick_at_low": {"inputs": ["close", "high", "low"], "func": wcs_042_lower_wick_at_low},
    "wcs_043_range_width_63d": {"inputs": ["close"], "func": wcs_043_range_width_63d},
    "wcs_044_range_width_21d": {"inputs": ["close"], "func": wcs_044_range_width_21d},
    "wcs_045_price_in_range_position_63d": {"inputs": ["close"], "func": wcs_045_price_in_range_position_63d},
    "wcs_046_time_in_low_third_63d": {"inputs": ["close"], "func": wcs_046_time_in_low_third_63d},
    "wcs_047_consolidation_flag": {"inputs": ["close"], "func": wcs_047_consolidation_flag},
    "wcs_048_consolidation_duration": {"inputs": ["close"], "func": wcs_048_consolidation_duration},
    "wcs_049_range_contraction_ratio": {"inputs": ["close"], "func": wcs_049_range_contraction_ratio},
    "wcs_050_sideways_score_21d": {"inputs": ["close"], "func": wcs_050_sideways_score_21d},
    "wcs_051_volatility_compression": {"inputs": ["close"], "func": wcs_051_volatility_compression},
    "wcs_052_close_clustering_21d": {"inputs": ["close"], "func": wcs_052_close_clustering_21d},
    "wcs_053_bar_overlap_21d": {"inputs": ["high", "low"], "func": wcs_053_bar_overlap_21d},
    "wcs_054_base_building_score": {"inputs": ["close", "volume"], "func": wcs_054_base_building_score},
    "wcs_055_range_low_touches_63d": {"inputs": ["close", "low"], "func": wcs_055_range_low_touches_63d},
    "wcs_056_range_high_touches_63d": {"inputs": ["close", "high"], "func": wcs_056_range_high_touches_63d},
    "wcs_057_spring_flag_63d": {"inputs": ["close", "low"], "func": wcs_057_spring_flag_63d},
    "wcs_058_spring_count_252d": {"inputs": ["close", "low"], "func": wcs_058_spring_count_252d},
    "wcs_059_days_since_spring": {"inputs": ["close", "low"], "func": wcs_059_days_since_spring},
    "wcs_060_shakeout_depth_63d": {"inputs": ["close", "low"], "func": wcs_060_shakeout_depth_63d},
    "wcs_061_spring_recovery_same_day": {"inputs": ["close", "low"], "func": wcs_061_spring_recovery_same_day},
    "wcs_062_false_breakdown_252d": {"inputs": ["close", "low"], "func": wcs_062_false_breakdown_252d},
    "wcs_063_undercut_volume_ratio": {"inputs": ["close", "low", "volume"], "func": wcs_063_undercut_volume_ratio},
    "wcs_064_spring_quality_score": {"inputs": ["close", "low", "volume"], "func": wcs_064_spring_quality_score},
    "wcs_065_terminal_shakeout_score": {"inputs": ["close", "high", "low", "volume"], "func": wcs_065_terminal_shakeout_score},
    "wcs_066_low_pierce_recovery_speed": {"inputs": ["close", "low"], "func": wcs_066_low_pierce_recovery_speed},
    "wcs_067_effort_vs_result_63d": {"inputs": ["close", "volume"], "func": wcs_067_effort_vs_result_63d},
    "wcs_068_no_supply_bar": {"inputs": ["close", "high", "low", "volume"], "func": wcs_068_no_supply_bar},
    "wcs_069_no_supply_count_21d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_069_no_supply_count_21d},
    "wcs_070_down_day_volume_fade_21d": {"inputs": ["close", "volume"], "func": wcs_070_down_day_volume_fade_21d},
    "wcs_071_down_volume_share_trend": {"inputs": ["close", "volume"], "func": wcs_071_down_volume_share_trend},
    "wcs_072_absorption_score": {"inputs": ["close", "volume"], "func": wcs_072_absorption_score},
    "wcs_073_climax_to_test_volume_ratio": {"inputs": ["volume"], "func": wcs_073_climax_to_test_volume_ratio},
    "wcs_074_wyckoff_phase_score": {"inputs": ["close", "high", "low", "volume"], "func": wcs_074_wyckoff_phase_score},
    "wcs_075_capitulation_sequence_completeness": {"inputs": ["close", "high", "low", "volume"], "func": wcs_075_capitulation_sequence_completeness},
}
