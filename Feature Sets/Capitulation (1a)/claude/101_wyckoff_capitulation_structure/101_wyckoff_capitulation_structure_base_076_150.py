"""
101_wyckoff_capitulation_structure — Base Features 076-150
Domain: Wyckoff selling-climax -> automatic-rally -> secondary-test -> spring
        sequence measurement (extended windows, composites, normalizations).
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


def _sc_flag(close, volume, w=_TD_YEAR):
    """Selling-climax flag: extreme down day on extreme volume within window w."""
    ret = _daily_ret(close)
    ret_q = ret.rolling(w, min_periods=max(5, w // 4)).quantile(0.05)
    vol_q = volume.rolling(w, min_periods=max(5, w // 4)).quantile(0.95)
    return ((ret <= ret_q) & (volume >= vol_q)).astype(float)


def _streak(flag: pd.Series) -> pd.Series:
    """Consecutive-day streak length of a 0/1 flag."""
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group A (076-090): Selling-climax variants ---

def wcs_076_sc_flag_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Selling-climax flag using a 504-day extremity reference."""
    return _sc_flag(close, volume, 504)


def wcs_077_days_since_sc_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trading days since the most recent 504d-referenced selling climax."""
    return _days_since(_sc_flag(close, volume, 504))


def wcs_078_sc_count_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of selling-climax days within the trailing 504 days."""
    return _rolling_sum(_sc_flag(close, volume, 504), 504)


def wcs_079_climax_volume_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of the peak 5-day volume within the trailing 252 days."""
    return _zscore_rolling(_rolling_max(volume, _TD_WEEK), _TD_YEAR)


def wcs_080_worst_3day_return_252d(close: pd.Series) -> pd.Series:
    """Most negative trailing 3-day return within the last 252 days."""
    return _rolling_min(close.pct_change(3), _TD_YEAR)


def wcs_081_worst_5day_return_252d(close: pd.Series) -> pd.Series:
    """Most negative trailing 5-day return within the last 252 days."""
    return _rolling_min(close.pct_change(5), _TD_YEAR)


def wcs_082_climax_gap_down_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Most negative overnight gap (open vs prior close) within 63 days."""
    gap = _safe_div(open - close.shift(1), close.shift(1))
    return _rolling_min(gap, _TD_QTR)


def wcs_083_climax_true_range_pctile(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of the peak 63-day true range within 252 days."""
    return _rolling_rank_pct(_rolling_max(_tr(close, high, low), _TD_QTR), _TD_YEAR)


def wcs_084_selloff_acceleration(close: pd.Series) -> pd.Series:
    """Recent worst 5-day return vs the prior-window worst 5-day return."""
    w5 = close.pct_change(5)
    recent = _rolling_min(w5, _TD_MON)
    prior = _rolling_min(w5, _TD_MON).shift(_TD_MON)
    return _safe_div(recent, prior)


def wcs_085_high_volume_down_day_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were down days on above-median volume."""
    down = _daily_ret(close) < 0
    hi_vol = volume > _rolling_median(volume, _TD_QTR)
    return _rolling_mean((down & hi_vol).astype(float), _TD_QTR)


def wcs_086_climax_close_off_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-off-low fraction on the widest-range bar of the last 21 days."""
    tr = _tr(close, high, low)
    off_low = _safe_div(close - low, (high - low).replace(0, np.nan))
    return off_low.where(tr >= _rolling_max(tr, _TD_MON)).ffill()


def wcs_087_volume_climax_isolation(volume: pd.Series) -> pd.Series:
    """Peak 5-day volume vs the 63-day median (climax volume isolation)."""
    return _safe_div(_rolling_max(volume, _TD_WEEK), _rolling_median(volume, _TD_QTR))


def wcs_088_capitulation_volume_zscore_63d(volume: pd.Series) -> pd.Series:
    """Current volume z-score over a trailing 63-day window."""
    return _zscore_rolling(volume, _TD_QTR)


def wcs_089_extreme_down_day_streak(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of below-(-2%) daily returns."""
    return _streak((_daily_ret(close) < -0.02).astype(float))


def wcs_090_climax_magnitude_atr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Worst single-day close-to-close move within 63 days, in ATR units."""
    atr = _rolling_mean(_tr(close, high, low), _TD_MON)
    return _safe_div(_rolling_min(close.diff(1), _TD_QTR), atr)


# --- Group B (091-105): Automatic-rally variants ---

def wcs_091_bounce_off_504d_low(close: pd.Series) -> pd.Series:
    """Percent the close sits above the trailing 504-day closing low."""
    return _safe_div(close - _rolling_min(close, 504), _rolling_min(close, 504))


def wcs_092_bounce_off_1260d_low(close: pd.Series) -> pd.Series:
    """Percent the close sits above the trailing 1260-day closing low."""
    return _safe_div(close - _rolling_min(close, 1260), _rolling_min(close, 1260))


def wcs_093_ar_strength_63d(close: pd.Series) -> pd.Series:
    """Automatic-rally strength: 63d high vs 252d low."""
    return _safe_div(_rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_YEAR),
                     _rolling_min(close, _TD_YEAR))


def wcs_094_days_since_252d_low_norm(close: pd.Series) -> pd.Series:
    """Trading days since the 252d low, normalized by 252 (0 = at the low)."""
    return _days_since_rolling_min(close, _TD_YEAR) / _TD_YEAR


def wcs_095_recovery_fraction_252d(close: pd.Series) -> pd.Series:
    """Recovery fraction of close between the 252d low and 252d high."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - lo, hi - lo)


def wcs_096_rally_up_days_63d(close: pd.Series) -> pd.Series:
    """Count of up days within the trailing 63 days."""
    return _rolling_sum((_daily_ret(close) > 0).astype(float), _TD_QTR)


def wcs_097_max_5day_gain_63d(close: pd.Series) -> pd.Series:
    """Largest trailing 5-day gain within the last 63 days (rally thrust)."""
    return _rolling_max(close.pct_change(5), _TD_QTR)


def wcs_098_rebound_velocity_21d(close: pd.Series) -> pd.Series:
    """OLS slope of close over the last 21 days, normalized by 21d std."""
    return _safe_div(_linslope(close, _TD_MON), _rolling_std(close, _TD_MON))


def wcs_099_rally_breadth_21d(close: pd.Series) -> pd.Series:
    """Up-day fraction times mean up-day return over 21 days (rally breadth)."""
    ret = _daily_ret(close)
    up_frac = _rolling_mean((ret > 0).astype(float), _TD_MON)
    up_ret = _rolling_mean(ret.clip(lower=0), _TD_MON)
    return up_frac * up_ret


def wcs_100_close_above_21d_high_flag(close: pd.Series) -> pd.Series:
    """Flag: close exceeds the prior 21-day closing high (range breakout up)."""
    return (close > _rolling_max(close, _TD_MON).shift(1)).astype(float)


def wcs_101_reclaim_of_sma50_flag(close: pd.Series) -> pd.Series:
    """Flag: close reclaimed its 50-day SMA after being below it."""
    sma = _rolling_mean(close, 50)
    return ((close > sma) & (close.shift(5) < sma.shift(5))).astype(float)


def wcs_102_up_day_volume_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of up-day volume over 21 days (rally participation building)."""
    uv = volume.where(_daily_ret(close) > 0)
    return _safe_div(_linslope(uv.ffill(), _TD_MON), _rolling_median(volume, _TD_QTR))


def wcs_103_thrust_off_63d_low(close: pd.Series) -> pd.Series:
    """Gain of close above the 63d low scaled by days since that low."""
    gain = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    age = _days_since_rolling_min(close, _TD_QTR) + 1.0
    return _safe_div(gain, age)


def wcs_104_consecutive_up_days(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of positive daily returns."""
    return _streak((_daily_ret(close) > 0).astype(float))


def wcs_105_net_advance_21d(close: pd.Series) -> pd.Series:
    """Net up days minus down days over the trailing 21 days."""
    ret = _daily_ret(close)
    up = _rolling_sum((ret > 0).astype(float), _TD_MON)
    dn = _rolling_sum((ret < 0).astype(float), _TD_MON)
    return up - dn


# --- Group C (106-122): Secondary-test / retest variants ---

def wcs_106_retest_proximity_252d(close: pd.Series) -> pd.Series:
    """Closeness of the close to the trailing 252-day low (1 = at the low)."""
    return _safe_div(_rolling_min(close, _TD_YEAR), close)


def wcs_107_retest_volume_contraction_252d(volume: pd.Series) -> pd.Series:
    """Recent 10-day volume vs the peak 252-day volume (low-volume retest)."""
    return _safe_div(_rolling_mean(volume, 10), _rolling_max(volume, _TD_YEAR))


def wcs_108_secondary_test_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of low-volume retests of the 63d low region within 63 days."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return _rolling_sum(((pos < 0.15) & lo_vol).astype(float), _TD_QTR)


def wcs_109_test_depth_vs_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """How far the recent 21d low sits relative to the prior 252d low."""
    prior = _rolling_min(low, _TD_YEAR).shift(_TD_MON)
    return _safe_div(_rolling_min(low, _TD_MON) - prior, prior)


def wcs_110_low_volume_test_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of low-zone days (bottom range third) with below-median volume."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    in_low = (pos < 0.33)
    return _safe_div(_rolling_sum((in_low & lo_vol).astype(float), _TD_QTR),
                     _rolling_sum(in_low.astype(float), _TD_QTR))


def wcs_111_retest_range_pctile(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of recent 5-day true range within 252 days (low = test)."""
    tr = _tr(close, high, low)
    return _rolling_rank_pct(_rolling_mean(tr, _TD_WEEK), _TD_YEAR)


def wcs_112_volume_dryup_ratio_5_21(volume: pd.Series) -> pd.Series:
    """5-day vs 21-day average volume ratio (short-horizon volume dry-up)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))


def wcs_113_volume_dryup_ratio_10_63(volume: pd.Series) -> pd.Series:
    """10-day vs 63-day average volume ratio (medium-horizon volume dry-up)."""
    return _safe_div(_rolling_mean(volume, 10), _rolling_mean(volume, _TD_QTR))


def wcs_114_higher_low_count_252d(low: pd.Series) -> pd.Series:
    """Count of days the 21d low exceeded the prior 21d low within 252 days."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    return _rolling_sum((cur > prior).astype(float), _TD_YEAR)


def wcs_115_higher_low_magnitude(low: pd.Series) -> pd.Series:
    """Percent rise of the current 21d low over the prior 21d low."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    return _safe_div(cur - prior, prior)


def wcs_116_test_count_declining_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Low-zone days where volume is also below its own 21d average."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    fading = volume < _rolling_mean(volume, _TD_MON)
    return _rolling_sum(((pos < 0.20) & fading).astype(float), _TD_QTR)


def wcs_117_double_bottom_volume_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recent low-zone volume vs prior low-zone volume (declining = good test)."""
    pos = _safe_div(close - _rolling_min(close, _TD_HALF),
                    _rolling_max(close, _TD_HALF) - _rolling_min(close, _TD_HALF))
    lz = volume.where(pos < 0.20)
    recent = _rolling_mean(lz, _TD_MON)
    prior = _rolling_mean(lz, _TD_MON).shift(_TD_QTR)
    return _safe_div(recent, prior)


def wcs_118_low_zone_dwell_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days the close sat in the bottom range quartile."""
    pos = _safe_div(close - _rolling_min(close, _TD_YEAR),
                    _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR))
    return _rolling_mean((pos < 0.25).astype(float), _TD_YEAR)


def wcs_119_spring_to_test_ratio(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Undercut days vs low-volume test days within 252 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    undercut = _rolling_sum((low < prior_low).astype(float), _TD_YEAR)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    test = _rolling_sum(((pos < 0.2) & (volume < _rolling_median(volume, _TD_QTR))).astype(float), _TD_YEAR)
    return _safe_div(undercut, test)


def wcs_120_retest_close_strength(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-within-bar position averaged over low-zone days (close strength)."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    clv = _safe_div(close - low, (high - low).replace(0, np.nan))
    return clv.where(pos < 0.25).rolling(_TD_QTR, min_periods=5).mean()


def wcs_121_lower_low_with_lower_volume(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: new 63d low set on volume below the 63d median (bullish dry-up)."""
    new_low = low <= _rolling_min(low, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return (new_low & lo_vol).astype(float)


def wcs_122_effort_result_at_low(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-to-move ratio averaged over the bottom-quartile range days."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    eff = _safe_div(_zscore_rolling(volume, _TD_QTR), _daily_ret(close).abs() + _EPS)
    return eff.where(pos < 0.25).rolling(_TD_QTR, min_periods=5).mean()


# --- Group D (123-137): Trading-range / consolidation variants ---

def wcs_123_range_width_126d(close: pd.Series) -> pd.Series:
    """126-day high-low range as a fraction of the 126-day low."""
    return _safe_div(_rolling_max(close, _TD_HALF) - _rolling_min(close, _TD_HALF),
                     _rolling_min(close, _TD_HALF))


def wcs_124_range_width_252d(close: pd.Series) -> pd.Series:
    """252-day high-low range as a fraction of the 252-day low."""
    return _safe_div(_rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR),
                     _rolling_min(close, _TD_YEAR))


def wcs_125_range_position_252d(close: pd.Series) -> pd.Series:
    """Close position within the 252-day range (0 = low, 1 = high)."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - lo, hi - lo)


def wcs_126_time_in_low_quartile_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days the close sat in the lower quartile of range."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    pos = _safe_div(close - lo, hi - lo)
    return _rolling_mean((pos < 0.25).astype(float), _TD_YEAR)


def wcs_127_consolidation_duration_63d(close: pd.Series) -> pd.Series:
    """Consecutive-day streak of tight (sub-median) 63d range width."""
    rw = _safe_div(_rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR),
                   _rolling_min(close, _TD_QTR))
    return _streak((rw < _rolling_median(rw, _TD_YEAR)).astype(float))


def wcs_128_range_contraction_21_126(close: pd.Series) -> pd.Series:
    """21-day range divided by 126-day range (broad range contraction)."""
    r21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    r126 = _rolling_max(close, _TD_HALF) - _rolling_min(close, _TD_HALF)
    return _safe_div(r21, r126)


def wcs_129_volatility_compression_63_252(close: pd.Series) -> pd.Series:
    """63-day return std divided by 252-day return std."""
    ret = _daily_ret(close)
    return _safe_div(_rolling_std(ret, _TD_QTR), _rolling_std(ret, _TD_YEAR))


def wcs_130_nr7_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Narrow-range-7 flag: today's true range is the smallest of the last 7."""
    tr = _tr(close, high, low)
    return (tr <= _rolling_min(tr, 7)).astype(float)


def wcs_131_nr_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of narrow-range-7 bars within the trailing 21 days."""
    tr = _tr(close, high, low)
    nr7 = (tr <= _rolling_min(tr, 7)).astype(float)
    return _rolling_sum(nr7, _TD_MON)


def wcs_132_inside_bar_fraction_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 bars contained within the prior bar's range."""
    inside = (high <= high.shift(1)) & (low >= low.shift(1))
    return _rolling_mean(inside.astype(float), _TD_MON)


def wcs_133_base_depth_vs_height(close: pd.Series) -> pd.Series:
    """63d drawdown depth divided by 63d range width (base proportions)."""
    dd = _safe_div(close - _rolling_max(close, _TD_QTR), _rolling_max(close, _TD_QTR))
    rw = _safe_div(_rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR),
                   _rolling_min(close, _TD_QTR))
    return _safe_div(dd.abs(), rw)


def wcs_134_price_coil_score(close: pd.Series) -> pd.Series:
    """Coil score: inverse of 21d range relative to 252d range (1 = coiled)."""
    r21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    r252 = _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR)
    return 1.0 - _safe_div(r21, r252)


def wcs_135_range_low_stability_63d(low: pd.Series) -> pd.Series:
    """Coefficient of variation of the rolling 21d low over 63 days (stable base)."""
    rl = _rolling_min(low, _TD_MON)
    return _safe_div(_rolling_std(rl, _TD_QTR), _rolling_mean(rl, _TD_QTR))


def wcs_136_close_dispersion_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of the close over the trailing 63 days."""
    return _safe_div(_rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))


def wcs_137_flat_base_score(close: pd.Series) -> pd.Series:
    """Flat-base score: low |slope| and tight range over 63 days combined."""
    slope = _safe_div(_linslope(close, _TD_QTR), _rolling_std(close, _TD_QTR)).abs()
    rw = _safe_div(_rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR),
                   _rolling_min(close, _TD_QTR))
    rw_rank = _rolling_rank_pct(rw, _TD_YEAR)
    return (1.0 - slope.clip(upper=1.0)) * (1.0 - rw_rank)


# --- Group E (138-150): Spring / exhaustion / composite variants ---

def wcs_138_spring_flag_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Spring flag against the prior 252-day low (major-low undercut & reclaim)."""
    prior_low = _rolling_min(low, _TD_YEAR).shift(1)
    return ((low < prior_low) & (close > prior_low)).astype(float)


def wcs_139_spring_count_504d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 63d-low spring events within the trailing 504 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _rolling_sum(spring, 504)


def wcs_140_deep_undercut_count_252d(low: pd.Series) -> pd.Series:
    """Count of days the low pierced >3% below the prior 63d low within 252 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    return _rolling_sum((low < prior_low * 0.97).astype(float), _TD_YEAR)


def wcs_141_false_breakdown_count_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 63d-low undercuts reclaimed by the close, within 252 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    fb = ((low < prior_low) & (close > prior_low)).astype(float)
    return _rolling_sum(fb, _TD_YEAR)


def wcs_142_shakeout_recovery_strength(close: pd.Series, low: pd.Series) -> pd.Series:
    """Average same-day close-vs-low recovery on undercut days over 63 days."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    rec = _safe_div(close - low, low).where(low < prior_low)
    return rec.rolling(_TD_QTR, min_periods=3).mean()


def wcs_143_no_supply_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days that were no-supply bars (down, narrow, low-vol)."""
    tr = _tr(close, high, low)
    down = _daily_ret(close) < 0
    narrow = tr < _rolling_median(tr, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    return _rolling_mean((down & narrow & lo_vol).astype(float), _TD_QTR)


def wcs_144_selling_exhaustion_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-day volume slope plus shrinking down-day magnitude (exhaustion)."""
    dv = volume.where(_daily_ret(close) < 0)
    vol_slope = _safe_div(_linslope(dv.ffill(), _TD_QTR), _rolling_median(volume, _TD_QTR))
    mag = _rolling_mean(_daily_ret(close).clip(upper=0).abs(), _TD_MON)
    mag_slope = mag - mag.shift(_TD_MON)
    return -(vol_slope + mag_slope)


def wcs_145_absorption_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-volume small-decline days within trailing 21 days."""
    hi_vol = volume > _rolling_median(volume, _TD_QTR) * 1.5
    small = _daily_ret(close).abs() < _rolling_median(_daily_ret(close).abs(), _TD_QTR)
    return _rolling_sum((hi_vol & small).astype(float), _TD_MON)


def wcs_146_down_volume_decay_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Recent vs prior down-day volume sum ratio over 63 days (decay <1)."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    recent = _rolling_sum(dv, _TD_QTR)
    prior = _rolling_sum(dv, _TD_QTR).shift(_TD_QTR)
    return _safe_div(recent, prior)


def wcs_147_climax_rally_test_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: climax volume spike, rally thrust, and test-volume dry-up."""
    climax = _rolling_rank_pct(_rolling_max(volume, _TD_WEEK), _TD_YEAR)
    rally = _rolling_max(close.pct_change(5), _TD_QTR).clip(lower=0)
    dryup = 1.0 - _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR)).clip(upper=2) / 2
    return climax + rally + dryup


def wcs_148_wyckoff_accumulation_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Accumulation score: near low, range tightening, volume declining (0-3)."""
    pos = _safe_div(close - _rolling_min(close, _TD_YEAR),
                    _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR))
    near = (pos < 0.30).astype(float)
    rw = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    tight = (rw < _rolling_median(rw, _TD_YEAR)).astype(float)
    vfade = (_rolling_mean(volume, _TD_MON) < _rolling_mean(volume, _TD_QTR)).astype(float)
    return near + tight + vfade


def wcs_149_tested_low_confidence(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Confidence the 252d low has been retested on contracting volume."""
    age = _days_since_rolling_min(low, _TD_YEAR)
    retested = (_rolling_sum((_safe_div(low, _rolling_min(low, _TD_YEAR)) < 1.03).astype(float), _TD_QTR) > 1)
    vcontract = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume, _TD_QTR))
    return retested.astype(float) * (1.0 - vcontract.clip(upper=1)) * (age / _TD_YEAR).clip(upper=1)


def wcs_150_capitulation_structure_index(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Master index: climax + rally + low-volume test + spring presence (0-1)."""
    sc = (_rolling_sum(_sc_flag(close, volume, _TD_YEAR), _TD_HALF) > 0).astype(float)
    rally = (_rolling_max(close.pct_change(5), _TD_QTR) > 0.04).astype(float)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    test = ((pos < 0.30) & (volume < _rolling_median(volume, _TD_QTR))).astype(float)
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = (_rolling_sum(((low < prior_low) & (close > prior_low)).astype(float), _TD_QTR) > 0).astype(float)
    return (sc + rally + test + spring) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

WYCKOFF_CAPITULATION_STRUCTURE_REGISTRY_076_150 = {
    "wcs_076_sc_flag_504d": {"inputs": ["close", "volume"], "func": wcs_076_sc_flag_504d},
    "wcs_077_days_since_sc_504d": {"inputs": ["close", "volume"], "func": wcs_077_days_since_sc_504d},
    "wcs_078_sc_count_504d": {"inputs": ["close", "volume"], "func": wcs_078_sc_count_504d},
    "wcs_079_climax_volume_zscore_252d": {"inputs": ["volume"], "func": wcs_079_climax_volume_zscore_252d},
    "wcs_080_worst_3day_return_252d": {"inputs": ["close"], "func": wcs_080_worst_3day_return_252d},
    "wcs_081_worst_5day_return_252d": {"inputs": ["close"], "func": wcs_081_worst_5day_return_252d},
    "wcs_082_climax_gap_down_63d": {"inputs": ["close", "open"], "func": wcs_082_climax_gap_down_63d},
    "wcs_083_climax_true_range_pctile": {"inputs": ["close", "high", "low"], "func": wcs_083_climax_true_range_pctile},
    "wcs_084_selloff_acceleration": {"inputs": ["close"], "func": wcs_084_selloff_acceleration},
    "wcs_085_high_volume_down_day_fraction_63d": {"inputs": ["close", "volume"], "func": wcs_085_high_volume_down_day_fraction_63d},
    "wcs_086_climax_close_off_low": {"inputs": ["close", "high", "low"], "func": wcs_086_climax_close_off_low},
    "wcs_087_volume_climax_isolation": {"inputs": ["volume"], "func": wcs_087_volume_climax_isolation},
    "wcs_088_capitulation_volume_zscore_63d": {"inputs": ["volume"], "func": wcs_088_capitulation_volume_zscore_63d},
    "wcs_089_extreme_down_day_streak": {"inputs": ["close"], "func": wcs_089_extreme_down_day_streak},
    "wcs_090_climax_magnitude_atr_63d": {"inputs": ["close", "high", "low"], "func": wcs_090_climax_magnitude_atr_63d},
    "wcs_091_bounce_off_504d_low": {"inputs": ["close"], "func": wcs_091_bounce_off_504d_low},
    "wcs_092_bounce_off_1260d_low": {"inputs": ["close"], "func": wcs_092_bounce_off_1260d_low},
    "wcs_093_ar_strength_63d": {"inputs": ["close"], "func": wcs_093_ar_strength_63d},
    "wcs_094_days_since_252d_low_norm": {"inputs": ["close"], "func": wcs_094_days_since_252d_low_norm},
    "wcs_095_recovery_fraction_252d": {"inputs": ["close"], "func": wcs_095_recovery_fraction_252d},
    "wcs_096_rally_up_days_63d": {"inputs": ["close"], "func": wcs_096_rally_up_days_63d},
    "wcs_097_max_5day_gain_63d": {"inputs": ["close"], "func": wcs_097_max_5day_gain_63d},
    "wcs_098_rebound_velocity_21d": {"inputs": ["close"], "func": wcs_098_rebound_velocity_21d},
    "wcs_099_rally_breadth_21d": {"inputs": ["close"], "func": wcs_099_rally_breadth_21d},
    "wcs_100_close_above_21d_high_flag": {"inputs": ["close"], "func": wcs_100_close_above_21d_high_flag},
    "wcs_101_reclaim_of_sma50_flag": {"inputs": ["close"], "func": wcs_101_reclaim_of_sma50_flag},
    "wcs_102_up_day_volume_slope_21d": {"inputs": ["close", "volume"], "func": wcs_102_up_day_volume_slope_21d},
    "wcs_103_thrust_off_63d_low": {"inputs": ["close"], "func": wcs_103_thrust_off_63d_low},
    "wcs_104_consecutive_up_days": {"inputs": ["close"], "func": wcs_104_consecutive_up_days},
    "wcs_105_net_advance_21d": {"inputs": ["close"], "func": wcs_105_net_advance_21d},
    "wcs_106_retest_proximity_252d": {"inputs": ["close"], "func": wcs_106_retest_proximity_252d},
    "wcs_107_retest_volume_contraction_252d": {"inputs": ["volume"], "func": wcs_107_retest_volume_contraction_252d},
    "wcs_108_secondary_test_count_63d": {"inputs": ["close", "volume"], "func": wcs_108_secondary_test_count_63d},
    "wcs_109_test_depth_vs_252d_low": {"inputs": ["close", "low"], "func": wcs_109_test_depth_vs_252d_low},
    "wcs_110_low_volume_test_fraction_63d": {"inputs": ["close", "volume"], "func": wcs_110_low_volume_test_fraction_63d},
    "wcs_111_retest_range_pctile": {"inputs": ["close", "high", "low"], "func": wcs_111_retest_range_pctile},
    "wcs_112_volume_dryup_ratio_5_21": {"inputs": ["volume"], "func": wcs_112_volume_dryup_ratio_5_21},
    "wcs_113_volume_dryup_ratio_10_63": {"inputs": ["volume"], "func": wcs_113_volume_dryup_ratio_10_63},
    "wcs_114_higher_low_count_252d": {"inputs": ["low"], "func": wcs_114_higher_low_count_252d},
    "wcs_115_higher_low_magnitude": {"inputs": ["low"], "func": wcs_115_higher_low_magnitude},
    "wcs_116_test_count_declining_volume": {"inputs": ["close", "volume"], "func": wcs_116_test_count_declining_volume},
    "wcs_117_double_bottom_volume_ratio": {"inputs": ["close", "volume"], "func": wcs_117_double_bottom_volume_ratio},
    "wcs_118_low_zone_dwell_252d": {"inputs": ["close"], "func": wcs_118_low_zone_dwell_252d},
    "wcs_119_spring_to_test_ratio": {"inputs": ["close", "low", "volume"], "func": wcs_119_spring_to_test_ratio},
    "wcs_120_retest_close_strength": {"inputs": ["close", "high", "low"], "func": wcs_120_retest_close_strength},
    "wcs_121_lower_low_with_lower_volume": {"inputs": ["close", "low", "volume"], "func": wcs_121_lower_low_with_lower_volume},
    "wcs_122_effort_result_at_low": {"inputs": ["close", "volume"], "func": wcs_122_effort_result_at_low},
    "wcs_123_range_width_126d": {"inputs": ["close"], "func": wcs_123_range_width_126d},
    "wcs_124_range_width_252d": {"inputs": ["close"], "func": wcs_124_range_width_252d},
    "wcs_125_range_position_252d": {"inputs": ["close"], "func": wcs_125_range_position_252d},
    "wcs_126_time_in_low_quartile_252d": {"inputs": ["close"], "func": wcs_126_time_in_low_quartile_252d},
    "wcs_127_consolidation_duration_63d": {"inputs": ["close"], "func": wcs_127_consolidation_duration_63d},
    "wcs_128_range_contraction_21_126": {"inputs": ["close"], "func": wcs_128_range_contraction_21_126},
    "wcs_129_volatility_compression_63_252": {"inputs": ["close"], "func": wcs_129_volatility_compression_63_252},
    "wcs_130_nr7_flag": {"inputs": ["close", "high", "low"], "func": wcs_130_nr7_flag},
    "wcs_131_nr_count_21d": {"inputs": ["close", "high", "low"], "func": wcs_131_nr_count_21d},
    "wcs_132_inside_bar_fraction_21d": {"inputs": ["high", "low"], "func": wcs_132_inside_bar_fraction_21d},
    "wcs_133_base_depth_vs_height": {"inputs": ["close"], "func": wcs_133_base_depth_vs_height},
    "wcs_134_price_coil_score": {"inputs": ["close"], "func": wcs_134_price_coil_score},
    "wcs_135_range_low_stability_63d": {"inputs": ["low"], "func": wcs_135_range_low_stability_63d},
    "wcs_136_close_dispersion_63d": {"inputs": ["close"], "func": wcs_136_close_dispersion_63d},
    "wcs_137_flat_base_score": {"inputs": ["close"], "func": wcs_137_flat_base_score},
    "wcs_138_spring_flag_252d": {"inputs": ["close", "low"], "func": wcs_138_spring_flag_252d},
    "wcs_139_spring_count_504d": {"inputs": ["close", "low"], "func": wcs_139_spring_count_504d},
    "wcs_140_deep_undercut_count_252d": {"inputs": ["low"], "func": wcs_140_deep_undercut_count_252d},
    "wcs_141_false_breakdown_count_252d": {"inputs": ["close", "low"], "func": wcs_141_false_breakdown_count_252d},
    "wcs_142_shakeout_recovery_strength": {"inputs": ["close", "low"], "func": wcs_142_shakeout_recovery_strength},
    "wcs_143_no_supply_fraction_63d": {"inputs": ["close", "high", "low", "volume"], "func": wcs_143_no_supply_fraction_63d},
    "wcs_144_selling_exhaustion_score": {"inputs": ["close", "volume"], "func": wcs_144_selling_exhaustion_score},
    "wcs_145_absorption_count_21d": {"inputs": ["close", "volume"], "func": wcs_145_absorption_count_21d},
    "wcs_146_down_volume_decay_63d": {"inputs": ["close", "volume"], "func": wcs_146_down_volume_decay_63d},
    "wcs_147_climax_rally_test_composite": {"inputs": ["close", "volume"], "func": wcs_147_climax_rally_test_composite},
    "wcs_148_wyckoff_accumulation_score": {"inputs": ["close", "volume"], "func": wcs_148_wyckoff_accumulation_score},
    "wcs_149_tested_low_confidence": {"inputs": ["close", "low", "volume"], "func": wcs_149_tested_low_confidence},
    "wcs_150_capitulation_structure_index": {"inputs": ["close", "high", "low", "volume"], "func": wcs_150_capitulation_structure_index},
}
