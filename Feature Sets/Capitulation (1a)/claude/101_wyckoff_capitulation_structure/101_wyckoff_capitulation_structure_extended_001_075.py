"""
101_wyckoff_capitulation_structure — Extended Features 001-075
Domain: Wyckoff selling-climax -> automatic-rally -> secondary-test -> spring
        sequence — additional structural variants: alternate climax thresholds,
        rally-thrust angles, retest-volume coupling, range-coil geometry,
        spring-quality variants, and effort-vs-result composites not covered
        by the base or derivative files.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y = 504
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


def _streak(flag: pd.Series) -> pd.Series:
    """Consecutive-day run length of flag == 1 (resets to 0 on any 0)."""
    f = (flag > 0).astype(float)
    grp = (f == 0).cumsum()
    return f.groupby(grp).cumsum()


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


def _sc_flag(close, high, low, volume, w=_TD_YEAR, ret_q=0.05, vol_q=0.95):
    """Selling-climax flag: extreme down day on extreme volume within window w."""
    ret = _daily_ret(close)
    rq = ret.rolling(w, min_periods=max(5, w // 4)).quantile(ret_q)
    vq = volume.rolling(w, min_periods=max(5, w // 4)).quantile(vol_q)
    return ((ret <= rq) & (volume >= vq)).astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Alternate selling-climax thresholds & magnitude ---

def wcs_ext_001_sc_flag_strict_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict selling-climax flag: 2nd-pctile down day on 98th-pctile volume (252d)."""
    return _sc_flag(close, high, low, volume, _TD_YEAR, 0.02, 0.98)


def wcs_ext_002_sc_flag_loose_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Loose selling-climax flag: 10th-pctile down day on 90th-pctile volume (252d)."""
    return _sc_flag(close, high, low, volume, _TD_YEAR, 0.10, 0.90)


def wcs_ext_003_sc_flag_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Selling-climax flag computed over a 126-day reference window."""
    return _sc_flag(close, high, low, volume, _TD_HALF)


def wcs_ext_004_sc_strict_count_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of strict selling-climax days within the trailing 252 days."""
    return _rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR, 0.02, 0.98), _TD_YEAR)


def wcs_ext_005_days_since_sc_strict(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Trading days since the most recent strict selling climax."""
    return _days_since(_sc_flag(close, high, low, volume, _TD_YEAR, 0.02, 0.98))


def wcs_ext_006_worst_2day_return_252d(close: pd.Series) -> pd.Series:
    """Most negative 2-day return within the trailing 252 days (climax burst)."""
    r2 = close.pct_change(2)
    return _rolling_min(r2, _TD_YEAR)


def wcs_ext_007_worst_10day_return_252d(close: pd.Series) -> pd.Series:
    """Most negative 10-day return within the trailing 252 days."""
    r10 = close.pct_change(10)
    return _rolling_min(r10, _TD_YEAR)


def wcs_ext_008_largest_down_day_126d(close: pd.Series) -> pd.Series:
    """Most negative single-day return within the trailing 126 days."""
    return _rolling_min(_daily_ret(close), _TD_HALF)


def wcs_ext_009_climax_volume_spike_252d(volume: pd.Series) -> pd.Series:
    """Peak 252-day volume relative to 252-day median volume (climax volume blow-out)."""
    return _safe_div(_rolling_max(volume, _TD_YEAR), _rolling_median(volume, _TD_YEAR))


def wcs_ext_010_climax_range_spike_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Peak 5-day true range vs 252-day median true range (climax range blow-out)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_max(tr, _TD_WEEK), _rolling_median(tr, _TD_YEAR))


def wcs_ext_011_panic_volume_down_sum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on down days over the trailing 21 days (panic distribution mass)."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    return _rolling_sum(dv, _TD_MON)


def wcs_ext_012_climax_gap_down_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Largest downside gap (prior low minus today's high) over the trailing 252 days."""
    gap = (low.shift(1) - high).clip(lower=0)
    return _safe_div(_rolling_max(gap, _TD_YEAR), close)


# --- Group B (013-024): Automatic-rally thrust & breadth variants ---

def wcs_ext_013_bounce_off_126d_low(close: pd.Series) -> pd.Series:
    """Percent the close sits above the trailing 126-day closing low."""
    lo = _rolling_min(close, _TD_HALF)
    return _safe_div(close - lo, lo)


def wcs_ext_014_bounce_off_504d_low(close: pd.Series) -> pd.Series:
    """Percent the close sits above the trailing 504-day closing low."""
    lo = _rolling_min(close, _TD_2Y)
    return _safe_div(close - lo, lo)


def wcs_ext_015_ar_strength_10d(close: pd.Series) -> pd.Series:
    """Automatic-rally strength: 10-day high vs 63-day low (fast rebound off climax)."""
    return _safe_div(_rolling_max(close, 10) - _rolling_min(close, _TD_QTR),
                     _rolling_min(close, _TD_QTR))


def wcs_ext_016_ar_strength_42d(close: pd.Series) -> pd.Series:
    """Automatic-rally strength: 42-day high vs 126-day low (broad rebound)."""
    return _safe_div(_rolling_max(close, 42) - _rolling_min(close, _TD_HALF),
                     _rolling_min(close, _TD_HALF))


def wcs_ext_017_rally_from_126d_low_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rebound from the 126-day low expressed in 21-day ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_MON)
    return _safe_div(close - _rolling_min(close, _TD_HALF), atr)


def wcs_ext_018_max_3day_gain_63d(close: pd.Series) -> pd.Series:
    """Largest 3-day gain within the trailing 63 days (rally-thrust burst)."""
    r3 = close.pct_change(3)
    return _rolling_max(r3, _TD_QTR)


def wcs_ext_019_max_10day_gain_126d(close: pd.Series) -> pd.Series:
    """Largest 10-day gain within the trailing 126 days."""
    r10 = close.pct_change(10)
    return _rolling_max(r10, _TD_HALF)


def wcs_ext_020_rally_up_days_42d(close: pd.Series) -> pd.Series:
    """Count of up days within the trailing 42 days (rally breadth)."""
    return _rolling_sum((_daily_ret(close) > 0).astype(float), 42)


def wcs_ext_021_up_volume_share_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of trailing-21-day volume occurring on up days (demand participation)."""
    uv = volume.where(_daily_ret(close) > 0, 0.0)
    return _safe_div(_rolling_sum(uv, _TD_MON), _rolling_sum(volume, _TD_MON))


def wcs_ext_022_rebound_velocity_21d(close: pd.Series) -> pd.Series:
    """Normalized OLS slope of close over the last 21 days (rebound velocity)."""
    return _safe_div(_linslope(close, _TD_MON), _rolling_mean(close, _TD_MON))


def wcs_ext_023_rally_thrust_off_63d_low(close: pd.Series) -> pd.Series:
    """Close vs 63-day low scaled by 63-day return std (thrust in volatility units)."""
    lo = _rolling_min(close, _TD_QTR)
    sd = _rolling_std(_daily_ret(close), _TD_QTR)
    return _safe_div(_safe_div(close - lo, lo), sd)


def wcs_ext_024_close_above_42d_high_flag(close: pd.Series) -> pd.Series:
    """Flag: close is at or above its trailing 42-day high (rally reclaiming highs)."""
    return (close >= _rolling_max(close, 42) - _EPS).astype(float)


# --- Group C (025-038): Secondary-test / retest coupling variants ---

def wcs_ext_025_retest_proximity_126d(close: pd.Series) -> pd.Series:
    """Closeness of the close to the trailing 126-day low (1 = at the low)."""
    lo = _rolling_min(close, _TD_HALF)
    return _safe_div(lo, close)


def wcs_ext_026_retest_volume_contraction_126d(volume: pd.Series) -> pd.Series:
    """Recent 10-day volume vs the peak 126-day volume (low = clean retest)."""
    return _safe_div(_rolling_mean(volume, 10), _rolling_max(volume, _TD_HALF))


def wcs_ext_027_low_volume_test_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of low-volume retests of the 63-day low region within 63 days."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return _rolling_sum(((pos < 0.20) & lo_vol).astype(float), _TD_QTR)


def wcs_ext_028_test_volume_vs_climax_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recent 5-day volume vs peak 252-day volume (test-to-climax volume contraction)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume, _TD_YEAR))


def wcs_ext_029_retest_depth_vs_126d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """How far the recent 21-day low pierced the prior 126-day low (negative = undercut)."""
    prior_low = _rolling_min(low, _TD_HALF).shift(_TD_MON)
    recent_low = _rolling_min(low, _TD_MON)
    return _safe_div(recent_low - prior_low, prior_low)


def wcs_ext_030_double_bottom_proximity_252d(close: pd.Series) -> pd.Series:
    """Similarity of the recent 42-day low to the prior 126-day low (double-bottom test)."""
    recent_low = _rolling_min(close, 42)
    prior_low = _rolling_min(close, _TD_HALF).shift(42)
    return _safe_div((recent_low - prior_low).abs(), prior_low)


def wcs_ext_031_low_zone_volume_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score (63d) measured while the close sits in the lower range third."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    volz = _zscore_rolling(volume, _TD_QTR)
    return volz.where(pos < 0.33).ffill()


def wcs_ext_032_higher_low_count_63d(low: pd.Series) -> pd.Series:
    """Count of days within trailing 63d where the 21d low exceeded the prior 21d low."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    return _rolling_sum((cur > prior).astype(float), _TD_QTR)


def wcs_ext_033_higher_low_streak_long(low: pd.Series) -> pd.Series:
    """Consecutive-day streak of the 42d low being above the prior 42d low."""
    cur = _rolling_min(low, 42)
    prior = _rolling_min(low, 42).shift(42)
    return _streak((cur > prior).astype(float))


def wcs_ext_034_retest_range_pctile_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of recent 5-day mean true range within trailing 63 days."""
    tr = _tr(close, high, low)
    return _rolling_rank_pct(_rolling_mean(tr, _TD_WEEK), _TD_QTR)


def wcs_ext_035_test_quality_score_strict(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict test quality: very near low + very low volume + very narrow range (0-3)."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    tr = _tr(close, high, low)
    near = (pos < 0.10).astype(float)
    lo_vol = (volume < _rolling_median(volume, _TD_QTR) * 0.6).astype(float)
    narrow = (tr < _rolling_median(tr, _TD_QTR) * 0.6).astype(float)
    return near + lo_vol + narrow


def wcs_ext_036_volume_at_low_vs_climax(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on bottom-decile-range days vs peak 252d volume (test dryup vs climax)."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    near_vol = volume.where(pos < 0.10)
    return _safe_div(_rolling_mean(near_vol, _TD_QTR), _rolling_max(volume, _TD_YEAR))


def wcs_ext_037_time_in_low_decile_126d(close: pd.Series) -> pd.Series:
    """Fraction of last 126 days the close sat in the bottom decile of its range."""
    lo = _rolling_min(close, _TD_HALF)
    hi = _rolling_max(close, _TD_HALF)
    pos = _safe_div(close - lo, hi - lo)
    return _rolling_mean((pos < 0.10).astype(float), _TD_HALF)


def wcs_ext_038_retest_close_strength_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within the daily bar, averaged over days near the 63d low."""
    pos_range = _safe_div(close - _rolling_min(close, _TD_QTR),
                          _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    bar_pos = _safe_div(close - low, (high - low))
    return bar_pos.where(pos_range < 0.25).ffill()


# --- Group D (039-050): Trading-range / coil geometry variants ---

def wcs_ext_039_range_width_126d(close: pd.Series) -> pd.Series:
    """126-day high-low range as a fraction of the 126-day low."""
    return _safe_div(_rolling_max(close, _TD_HALF) - _rolling_min(close, _TD_HALF),
                     _rolling_min(close, _TD_HALF))


def wcs_ext_040_range_width_10d(close: pd.Series) -> pd.Series:
    """10-day high-low range as a fraction of the 10-day low (micro-coil width)."""
    return _safe_div(_rolling_max(close, 10) - _rolling_min(close, 10),
                     _rolling_min(close, 10))


def wcs_ext_041_range_position_126d(close: pd.Series) -> pd.Series:
    """Close position within the 126-day range (0 = low, 1 = high)."""
    lo = _rolling_min(close, _TD_HALF)
    hi = _rolling_max(close, _TD_HALF)
    return _safe_div(close - lo, hi - lo)


def wcs_ext_042_range_contraction_10_63(close: pd.Series) -> pd.Series:
    """10-day range divided by 63-day range (fast range contraction)."""
    r10 = _rolling_max(close, 10) - _rolling_min(close, 10)
    r63 = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    return _safe_div(r10, r63)


def wcs_ext_043_range_contraction_63_252(close: pd.Series) -> pd.Series:
    """63-day range divided by 252-day range (broad range contraction)."""
    r63 = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    r252 = _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR)
    return _safe_div(r63, r252)


def wcs_ext_044_volatility_compression_10_63(close: pd.Series) -> pd.Series:
    """10-day return std divided by 63-day return std (fast volatility compression)."""
    ret = _daily_ret(close)
    return _safe_div(_rolling_std(ret, 10), _rolling_std(ret, _TD_QTR))


def wcs_ext_045_atr_compression_10_63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day ATR divided by 63-day ATR (true-range compression near base)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, 10), _rolling_mean(tr, _TD_QTR))


def wcs_ext_046_consolidation_flag_63d(close: pd.Series) -> pd.Series:
    """Flag: 63d range width below its 252d median (broad consolidation)."""
    rw = _safe_div(_rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR),
                   _rolling_min(close, _TD_QTR))
    return (rw < _rolling_median(rw, _TD_YEAR)).astype(float)


def wcs_ext_047_inside_bar_fraction_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 bars fully inside the prior bar's high-low range."""
    inside = (high <= high.shift(1)) & (low >= low.shift(1))
    return _rolling_mean(inside.astype(float), _TD_QTR)


def wcs_ext_048_close_dispersion_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of close over 63 days (price clustering near base)."""
    return _safe_div(_rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))


def wcs_ext_049_range_low_touches_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days the daily low touched within 3% of the 252d low."""
    lo = _rolling_min(low, _TD_YEAR)
    touch = low <= lo * 1.03
    return _rolling_sum(touch.astype(float), _TD_YEAR)


def wcs_ext_050_flat_base_score(close: pd.Series) -> pd.Series:
    """Flat-base score: tight 21d range AND near 126d low AND low 21d slope (0-3)."""
    rw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    pos = _safe_div(close - _rolling_min(close, _TD_HALF),
                    _rolling_max(close, _TD_HALF) - _rolling_min(close, _TD_HALF))
    slope = _safe_div(_linslope(close, _TD_MON), _rolling_std(close, _TD_MON))
    tight = (rw < _rolling_median(rw, _TD_YEAR)).astype(float)
    near = (pos < 0.33).astype(float)
    flat = (slope.abs() < 0.10).astype(float)
    return tight + near + flat


# --- Group E (051-062): Spring / shakeout / exhaustion variants ---

def wcs_ext_051_spring_flag_126d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Spring flag: low undercut the prior 126d low intraday, close reclaimed it."""
    prior_low = _rolling_min(low, _TD_HALF).shift(1)
    return ((low < prior_low) & (close > prior_low)).astype(float)


def wcs_ext_052_spring_count_504d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 63d-low spring events within the trailing 504 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _rolling_sum(spring, _TD_2Y)


def wcs_ext_053_days_since_spring_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Trading days since the most recent 252d-low spring event."""
    prior_low = _rolling_min(low, _TD_YEAR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _days_since(spring)


def wcs_ext_054_deep_undercut_count_63d(low: pd.Series) -> pd.Series:
    """Count of days the daily low pierced more than 3% below the prior 63d low."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    deep = (low < prior_low * 0.97).astype(float)
    return _rolling_sum(deep, _TD_QTR)


def wcs_ext_055_shakeout_recovery_strength_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close margin above the prior 63d low on days the low undercut it (recovery strength)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    rec = _safe_div(close - prior_low, prior_low)
    return rec.where(low < prior_low).fillna(0.0)


def wcs_ext_056_spring_volume_quality_63d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on undercut days vs 252d median volume (low = high-quality dry spring)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    uv = volume.where(low < prior_low)
    return _safe_div(uv.ffill(), _rolling_median(volume, _TD_YEAR))


def wcs_ext_057_spring_quality_score_strict(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict spring quality: deep undercut + reclaim + sub-60%-median volume (0-3)."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    deep = (low < prior_low * 0.98).astype(float)
    reclaim = (close > prior_low).astype(float)
    dry = (volume < _rolling_median(volume, _TD_QTR) * 0.6).astype(float)
    return deep + reclaim + dry


def wcs_ext_058_false_breakdown_count_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of false-breakdown days: 63d low undercut intraday, close reclaimed it."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    fb = ((low < prior_low) & (close > prior_low)).astype(float)
    return _rolling_sum(fb, _TD_YEAR)


def wcs_ext_059_no_supply_fraction_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days that were no-supply bars (down, narrow, low volume)."""
    tr = _tr(close, high, low)
    down = _daily_ret(close) < 0
    narrow = tr < _rolling_median(tr, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return _rolling_mean((down & narrow & lo_vol).astype(float), _TD_MON)


def wcs_ext_060_down_volume_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of trailing-63-day volume occurring on down days (selling pressure mass)."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    return _safe_div(_rolling_sum(dv, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def wcs_ext_061_effort_vs_result_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume z-score minus absolute-return z-score over 21 days (high effort, low result)."""
    volz = _zscore_rolling(volume, _TD_MON)
    retz = _zscore_rolling(_daily_ret(close).abs(), _TD_MON)
    return volz - retz


def wcs_ext_062_selling_climax_to_dryup_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Peak 5-day down-volume vs recent 5-day volume (climax-to-dryup contraction)."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    return _safe_div(_rolling_max(dv, _TD_QTR), _rolling_mean(volume, _TD_WEEK))


# --- Group F (063-075): Sequencing, recency-weight & structure composites ---

def wcs_ext_063_sc_recency_ewm_126(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM (span=126) recency-weighted selling-climax intensity."""
    flag = _sc_flag(close, high, low, volume, _TD_YEAR)
    return _ewm_mean(flag, _TD_HALF)


def wcs_ext_064_sc_count_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling-climax days within the trailing 126 days."""
    return _rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_HALF)


def wcs_ext_065_days_since_252d_low_norm(close: pd.Series) -> pd.Series:
    """Days since the 252-day closing low was set, normalized by 252 (0-1 maturity)."""
    lo = _rolling_min(close, _TD_YEAR)
    at_low = (close <= lo + _EPS).astype(float)
    return _days_since(at_low) / float(_TD_YEAR)


def wcs_ext_066_climax_then_rally_flag(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: a selling climax occurred in prior 63d AND a >5% rally followed within 63d."""
    sc = _rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_QTR)
    rally = _rolling_max(_daily_ret(close), _TD_QTR)
    return ((sc > 0) & (rally > 0.05)).astype(float)


def wcs_ext_067_rally_then_test_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: a >5% rally occurred in prior 63d AND close now back in lower range third."""
    rally = _rolling_max(_daily_ret(close), _TD_QTR)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    return ((rally > 0.05) & (pos < 0.33)).astype(float)


def wcs_ext_068_low_volume_at_higher_low_flag(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21d low above prior 21d low AND volume below 63d median (low-supply higher low)."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return ((cur > prior) & lo_vol).astype(float)


def wcs_ext_069_absorption_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of absorption days (high-volume z-score, small price move) in trailing 63d."""
    volz = _zscore_rolling(volume, _TD_QTR)
    small_move = _daily_ret(close).abs() < _rolling_median(_daily_ret(close).abs(), _TD_QTR)
    return _rolling_sum(((volz > 1.0) & small_move).astype(float), _TD_QTR)


def wcs_ext_070_climax_volume_pctile_504d(volume: pd.Series) -> pd.Series:
    """Percentile rank of peak 5-day volume within the trailing 504 days."""
    return _rolling_rank_pct(_rolling_max(volume, _TD_WEEK), _TD_2Y)


def wcs_ext_071_volume_dryup_trend_63d(volume: pd.Series) -> pd.Series:
    """Normalized OLS slope of volume over 63 days (negative = sustained volume dryup)."""
    return _safe_div(_linslope(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def wcs_ext_072_range_low_stability_126d(low: pd.Series) -> pd.Series:
    """Std of daily lows over 126d relative to mean low (low = stable tested base)."""
    return _safe_div(_rolling_std(low, _TD_HALF), _rolling_mean(low, _TD_HALF))


def wcs_ext_073_climax_rally_test_composite(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite presence of climax + rally + low-volume retest phases, 0-1 normalized."""
    sc = (_rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_HALF) > 0).astype(float)
    rally = (_rolling_max(_daily_ret(close), _TD_QTR) > 0.05).astype(float)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    test = ((pos < 0.25) & (volume < _rolling_median(volume, _TD_QTR))).astype(float)
    return (sc + rally + test) / 3.0


def wcs_ext_074_tested_low_quality_score(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Tested-low quality: higher-low + spring present + below-median volume (0-3)."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    higher_low = (cur > prior).astype(float)
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = (_rolling_sum(((low < prior_low) & (close > prior_low)).astype(float), _TD_QTR) > 0).astype(float)
    lo_vol = (volume < _rolling_median(volume, _TD_QTR)).astype(float)
    return higher_low + spring + lo_vol


def wcs_ext_075_capitulation_structure_index(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Capitulation-structure index, 0-1: averages four normalized sub-scores —
    recent selling climax, completed automatic rally, low-volume secondary test,
    and a higher-low / spring confirmation. Higher = a more complete tested low.
    """
    sc = (_rolling_sum(_sc_flag(close, high, low, volume, _TD_YEAR), _TD_HALF) > 0).astype(float)
    rally = (_rolling_max(_daily_ret(close), _TD_QTR) > 0.04).astype(float)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    test = ((pos < 0.30) & (volume < _rolling_median(volume, _TD_QTR))).astype(float)
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    higher_low = (cur > prior).astype(float)
    return (sc + rally + test + higher_low) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

WYCKOFF_CAPITULATION_STRUCTURE_EXTENDED_REGISTRY_001_075 = {
    "wcs_ext_001_sc_flag_strict_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_001_sc_flag_strict_252d},
    "wcs_ext_002_sc_flag_loose_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_002_sc_flag_loose_252d},
    "wcs_ext_003_sc_flag_126d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_003_sc_flag_126d},
    "wcs_ext_004_sc_strict_count_252d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_004_sc_strict_count_252d},
    "wcs_ext_005_days_since_sc_strict": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_005_days_since_sc_strict},
    "wcs_ext_006_worst_2day_return_252d": {"inputs": ["close"], "func": wcs_ext_006_worst_2day_return_252d},
    "wcs_ext_007_worst_10day_return_252d": {"inputs": ["close"], "func": wcs_ext_007_worst_10day_return_252d},
    "wcs_ext_008_largest_down_day_126d": {"inputs": ["close"], "func": wcs_ext_008_largest_down_day_126d},
    "wcs_ext_009_climax_volume_spike_252d": {"inputs": ["volume"], "func": wcs_ext_009_climax_volume_spike_252d},
    "wcs_ext_010_climax_range_spike_252d": {"inputs": ["close", "high", "low"], "func": wcs_ext_010_climax_range_spike_252d},
    "wcs_ext_011_panic_volume_down_sum_21d": {"inputs": ["close", "volume"], "func": wcs_ext_011_panic_volume_down_sum_21d},
    "wcs_ext_012_climax_gap_down_252d": {"inputs": ["close", "low", "high"], "func": wcs_ext_012_climax_gap_down_252d},
    "wcs_ext_013_bounce_off_126d_low": {"inputs": ["close"], "func": wcs_ext_013_bounce_off_126d_low},
    "wcs_ext_014_bounce_off_504d_low": {"inputs": ["close"], "func": wcs_ext_014_bounce_off_504d_low},
    "wcs_ext_015_ar_strength_10d": {"inputs": ["close"], "func": wcs_ext_015_ar_strength_10d},
    "wcs_ext_016_ar_strength_42d": {"inputs": ["close"], "func": wcs_ext_016_ar_strength_42d},
    "wcs_ext_017_rally_from_126d_low_atr": {"inputs": ["close", "high", "low"], "func": wcs_ext_017_rally_from_126d_low_atr},
    "wcs_ext_018_max_3day_gain_63d": {"inputs": ["close"], "func": wcs_ext_018_max_3day_gain_63d},
    "wcs_ext_019_max_10day_gain_126d": {"inputs": ["close"], "func": wcs_ext_019_max_10day_gain_126d},
    "wcs_ext_020_rally_up_days_42d": {"inputs": ["close"], "func": wcs_ext_020_rally_up_days_42d},
    "wcs_ext_021_up_volume_share_21d": {"inputs": ["close", "volume"], "func": wcs_ext_021_up_volume_share_21d},
    "wcs_ext_022_rebound_velocity_21d": {"inputs": ["close"], "func": wcs_ext_022_rebound_velocity_21d},
    "wcs_ext_023_rally_thrust_off_63d_low": {"inputs": ["close"], "func": wcs_ext_023_rally_thrust_off_63d_low},
    "wcs_ext_024_close_above_42d_high_flag": {"inputs": ["close"], "func": wcs_ext_024_close_above_42d_high_flag},
    "wcs_ext_025_retest_proximity_126d": {"inputs": ["close"], "func": wcs_ext_025_retest_proximity_126d},
    "wcs_ext_026_retest_volume_contraction_126d": {"inputs": ["volume"], "func": wcs_ext_026_retest_volume_contraction_126d},
    "wcs_ext_027_low_volume_test_count_63d": {"inputs": ["close", "volume"], "func": wcs_ext_027_low_volume_test_count_63d},
    "wcs_ext_028_test_volume_vs_climax_volume": {"inputs": ["close", "volume"], "func": wcs_ext_028_test_volume_vs_climax_volume},
    "wcs_ext_029_retest_depth_vs_126d_low": {"inputs": ["close", "low"], "func": wcs_ext_029_retest_depth_vs_126d_low},
    "wcs_ext_030_double_bottom_proximity_252d": {"inputs": ["close"], "func": wcs_ext_030_double_bottom_proximity_252d},
    "wcs_ext_031_low_zone_volume_zscore": {"inputs": ["close", "volume"], "func": wcs_ext_031_low_zone_volume_zscore},
    "wcs_ext_032_higher_low_count_63d": {"inputs": ["low"], "func": wcs_ext_032_higher_low_count_63d},
    "wcs_ext_033_higher_low_streak_long": {"inputs": ["low"], "func": wcs_ext_033_higher_low_streak_long},
    "wcs_ext_034_retest_range_pctile_63d": {"inputs": ["close", "high", "low"], "func": wcs_ext_034_retest_range_pctile_63d},
    "wcs_ext_035_test_quality_score_strict": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_035_test_quality_score_strict},
    "wcs_ext_036_volume_at_low_vs_climax": {"inputs": ["close", "volume"], "func": wcs_ext_036_volume_at_low_vs_climax},
    "wcs_ext_037_time_in_low_decile_126d": {"inputs": ["close"], "func": wcs_ext_037_time_in_low_decile_126d},
    "wcs_ext_038_retest_close_strength_63d": {"inputs": ["close", "high", "low"], "func": wcs_ext_038_retest_close_strength_63d},
    "wcs_ext_039_range_width_126d": {"inputs": ["close"], "func": wcs_ext_039_range_width_126d},
    "wcs_ext_040_range_width_10d": {"inputs": ["close"], "func": wcs_ext_040_range_width_10d},
    "wcs_ext_041_range_position_126d": {"inputs": ["close"], "func": wcs_ext_041_range_position_126d},
    "wcs_ext_042_range_contraction_10_63": {"inputs": ["close"], "func": wcs_ext_042_range_contraction_10_63},
    "wcs_ext_043_range_contraction_63_252": {"inputs": ["close"], "func": wcs_ext_043_range_contraction_63_252},
    "wcs_ext_044_volatility_compression_10_63": {"inputs": ["close"], "func": wcs_ext_044_volatility_compression_10_63},
    "wcs_ext_045_atr_compression_10_63": {"inputs": ["close", "high", "low"], "func": wcs_ext_045_atr_compression_10_63},
    "wcs_ext_046_consolidation_flag_63d": {"inputs": ["close"], "func": wcs_ext_046_consolidation_flag_63d},
    "wcs_ext_047_inside_bar_fraction_63d": {"inputs": ["high", "low"], "func": wcs_ext_047_inside_bar_fraction_63d},
    "wcs_ext_048_close_dispersion_63d": {"inputs": ["close"], "func": wcs_ext_048_close_dispersion_63d},
    "wcs_ext_049_range_low_touches_252d": {"inputs": ["close", "low"], "func": wcs_ext_049_range_low_touches_252d},
    "wcs_ext_050_flat_base_score": {"inputs": ["close"], "func": wcs_ext_050_flat_base_score},
    "wcs_ext_051_spring_flag_126d": {"inputs": ["close", "low"], "func": wcs_ext_051_spring_flag_126d},
    "wcs_ext_052_spring_count_504d": {"inputs": ["close", "low"], "func": wcs_ext_052_spring_count_504d},
    "wcs_ext_053_days_since_spring_252d": {"inputs": ["close", "low"], "func": wcs_ext_053_days_since_spring_252d},
    "wcs_ext_054_deep_undercut_count_63d": {"inputs": ["low"], "func": wcs_ext_054_deep_undercut_count_63d},
    "wcs_ext_055_shakeout_recovery_strength_63d": {"inputs": ["close", "low"], "func": wcs_ext_055_shakeout_recovery_strength_63d},
    "wcs_ext_056_spring_volume_quality_63d": {"inputs": ["close", "low", "volume"], "func": wcs_ext_056_spring_volume_quality_63d},
    "wcs_ext_057_spring_quality_score_strict": {"inputs": ["close", "low", "volume"], "func": wcs_ext_057_spring_quality_score_strict},
    "wcs_ext_058_false_breakdown_count_252d": {"inputs": ["close", "low"], "func": wcs_ext_058_false_breakdown_count_252d},
    "wcs_ext_059_no_supply_fraction_21d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_059_no_supply_fraction_21d},
    "wcs_ext_060_down_volume_share_63d": {"inputs": ["close", "volume"], "func": wcs_ext_060_down_volume_share_63d},
    "wcs_ext_061_effort_vs_result_21d": {"inputs": ["close", "volume"], "func": wcs_ext_061_effort_vs_result_21d},
    "wcs_ext_062_selling_climax_to_dryup_ratio": {"inputs": ["close", "volume"], "func": wcs_ext_062_selling_climax_to_dryup_ratio},
    "wcs_ext_063_sc_recency_ewm_126": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_063_sc_recency_ewm_126},
    "wcs_ext_064_sc_count_126d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_064_sc_count_126d},
    "wcs_ext_065_days_since_252d_low_norm": {"inputs": ["close"], "func": wcs_ext_065_days_since_252d_low_norm},
    "wcs_ext_066_climax_then_rally_flag": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_066_climax_then_rally_flag},
    "wcs_ext_067_rally_then_test_flag": {"inputs": ["close", "volume"], "func": wcs_ext_067_rally_then_test_flag},
    "wcs_ext_068_low_volume_at_higher_low_flag": {"inputs": ["close", "low", "volume"], "func": wcs_ext_068_low_volume_at_higher_low_flag},
    "wcs_ext_069_absorption_count_63d": {"inputs": ["close", "volume"], "func": wcs_ext_069_absorption_count_63d},
    "wcs_ext_070_climax_volume_pctile_504d": {"inputs": ["volume"], "func": wcs_ext_070_climax_volume_pctile_504d},
    "wcs_ext_071_volume_dryup_trend_63d": {"inputs": ["volume"], "func": wcs_ext_071_volume_dryup_trend_63d},
    "wcs_ext_072_range_low_stability_126d": {"inputs": ["low"], "func": wcs_ext_072_range_low_stability_126d},
    "wcs_ext_073_climax_rally_test_composite": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_073_climax_rally_test_composite},
    "wcs_ext_074_tested_low_quality_score": {"inputs": ["close", "low", "volume"], "func": wcs_ext_074_tested_low_quality_score},
    "wcs_ext_075_capitulation_structure_index": {"inputs": ["close", "high", "low", "volume"], "func": wcs_ext_075_capitulation_structure_index},
}
