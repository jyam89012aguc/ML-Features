"""
13_drawdown_acceleration — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base drawdown-acceleration features — velocity of underwater-curve
steepening: how fast the gap to trailing highs is widening, how quickly drawdown slope worsens.
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
    """Rolling maximum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling standard deviation over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponentially-weighted mean with given span."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped to _EPS to avoid log(0)."""
    return np.log(s.clip(lower=_EPS))


def _drawdown(close: pd.Series, w: int) -> pd.Series:
    """Drawdown from rolling w-period high: (close - roll_high) / roll_high."""
    roll_high = _rolling_max(close, w)
    return _safe_div(close - roll_high, roll_high)


def _log_drawdown(close: pd.Series, w: int) -> pd.Series:
    """Log drawdown: log(close) - log(rolling w-period high)."""
    return _log_safe(close) - _log_safe(_rolling_max(close, w))


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

def dacc_drv2_001_drawdown_252d_velocity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day drawdown velocity (acceleration of underwater widening)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_002_drawdown_252d_velocity_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the 5-day drawdown velocity (monthly change in velocity)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_drv2_003_drawdown_63d_velocity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 63-day drawdown."""
    vel = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_004_drawdown_21d_velocity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 21-day drawdown."""
    vel = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_005_drawdown_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of 252-day drawdown (slope acceleration)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv2_006_drawdown_slope_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day OLS slope of 252-day drawdown."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return slp.diff(_TD_MON)


def dacc_drv2_007_log_drawdown_velocity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of log-252-day drawdown."""
    vel = _log_drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_008_hwm_gap_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day OLS slope of 52-week high gap."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    slp = _linslope(gap, _TD_WEEK)
    return slp.diff(_TD_WEEK)


def dacc_drv2_009_drawdown_area_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day drawdown area (area acceleration)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    return area.diff(_TD_WEEK)


def dacc_drv2_010_drawdown_area_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day drawdown area."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_QTR)
    return area.diff(_TD_MON)


def dacc_drv2_011_drawdown_composite_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of multi-horizon drawdown composite score."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    return composite.diff(_TD_WEEK)


def dacc_drv2_012_drawdown_composite_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of multi-horizon composite (2nd diff of composite)."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_013_drawdown_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day drawdown z-score (z-score accelerating)."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    return z.diff(_TD_WEEK)


def dacc_drv2_014_drawdown_zscore_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252-day drawdown z-score."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    return z.diff(_TD_MON)


def dacc_drv2_015_vwap_gap_velocity_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 21-day VWAP gap."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    gap = _safe_div(close - vwap, vwap)
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_016_drawdown_depth_increment_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day sum of drawdown increments (deepening pace accelerating)."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deepening = dd_chg.where(dd_chg < 0, 0.0)
    incr_sum = _rolling_sum(deepening, _TD_MON)
    return incr_sum.diff(_TD_WEEK)


def dacc_drv2_017_hwm_gap_widening_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day high-water-mark gap change (second diff of gap)."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_018_drawdown_ewm_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-21 of drawdown depth (EWM velocity)."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    return dd_ewm.diff(_TD_WEEK)


def dacc_drv2_019_drawdown_slope_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day drawdown over 63-day window."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_QTR)
    return slp.diff(_TD_WEEK)


def dacc_drv2_020_successive_decline_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of successive-decline steepening measure (5d return minus prior 5d)."""
    ret5 = close.pct_change(_TD_WEEK)
    delta = ret5 - ret5.shift(_TD_WEEK)
    return delta.diff(_TD_WEEK)


def dacc_drv2_021_drawdown_duration_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day fraction of underwater days (duration velocity)."""
    roll_high = _rolling_max(close, _TD_YEAR)
    underwater = (close < roll_high).astype(float)
    frac = _rolling_mean(underwater, _TD_QTR)
    return frac.diff(_TD_WEEK)


def dacc_drv2_022_drawdown_area_velocity_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5-day change in drawdown area (slope of area growth)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dacc_drv2_023_intraday_drawdown_velocity_5d(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of intraday 252-day drawdown."""
    hwm = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - hwm, hwm)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_024_drawdown_new_depth_rate_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day new-depth count (acceleration of new lows)."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    new_depth = (dd < prior_min).astype(float)
    count63 = _rolling_sum(new_depth, _TD_QTR)
    return count63.diff(_TD_WEEK)


def dacc_drv2_025_drawdown_accel_ewm_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-5 of 5-day drawdown acceleration (smoothed jerk)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    accel_ewm = _ewm_mean(accel, _TD_WEEK)
    return accel_ewm.diff(_TD_WEEK)


# ── 2nd-Derivative Feature Functions (026-075) ────────────────────────────────

def dacc_drv2_026_drawdown_126d_velocity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 126-day drawdown."""
    vel = _drawdown(close, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_027_drawdown_504d_velocity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 504-day drawdown."""
    vel = _drawdown(close, 504).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_028_drawdown_126d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of 126-day drawdown."""
    slp = _linslope(_drawdown(close, _TD_HALF), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv2_029_drawdown_504d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of 504-day drawdown."""
    slp = _linslope(_drawdown(close, 504), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv2_030_drawdown_252d_velocity_63d_diff(close: pd.Series) -> pd.Series:
    """63-day diff of 5-day drawdown velocity (quarterly change in velocity)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_QTR)


def dacc_drv2_031_drawdown_63d_velocity_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of 63-day drawdown."""
    vel = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_drv2_032_drawdown_21d_velocity_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of 21-day drawdown."""
    vel = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_drv2_033_log_drawdown_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of log 252-day drawdown."""
    slp = _linslope(_log_drawdown(close, _TD_YEAR), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv2_034_drawdown_area_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling drawdown area (long-horizon area velocity)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_YEAR)
    return area.diff(_TD_WEEK)


def dacc_drv2_035_drawdown_composite_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of multi-horizon drawdown composite score."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    return composite.diff(_TD_MON)


def dacc_drv2_036_hwm_gap_slope_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day OLS slope of 52-week high gap."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    slp = _linslope(gap, _TD_MON)
    return slp.diff(_TD_MON)


def dacc_drv2_037_drawdown_zscore_63d_diff(close: pd.Series) -> pd.Series:
    """63-day diff of 252-day drawdown z-score (quarterly shift in extremity)."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    return z.diff(_TD_QTR)


def dacc_drv2_038_drawdown_ewm5_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-5 smoothed 252-day drawdown (fast EWM acceleration)."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_WEEK)
    return dd_ewm.diff(_TD_WEEK)


def dacc_drv2_039_drawdown_ewm63_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-63 smoothed 252-day drawdown (slow EWM acceleration)."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_QTR)
    return dd_ewm.diff(_TD_WEEK)


def dacc_drv2_040_drawdown_cross_4window_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 4-window composite drawdown (21d+63d+126d+252d average)."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    return comp.diff(_TD_WEEK)


def dacc_drv2_041_drawdown_cross_4window_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 4-window composite drawdown."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    vel = comp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv2_042_drawdown_slope_5d_diff_21w(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day OLS slope of 252-day drawdown (monthly slope change)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_WEEK)
    return slp.diff(_TD_MON)


def dacc_drv2_043_drawdown_area_velocity_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of 5-day change in 21-day drawdown area (smoothed area velocity)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_WEEK)


def dacc_drv2_044_drawdown_velocity_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day drawdown velocity within 252-day distribution."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_drv2_045_drawdown_accel_pct_rank_252d_v2(close: pd.Series) -> pd.Series:
    """Percentile rank of 1-day diff of 5-day drawdown velocity within 252-day distribution."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(1)
    return accel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_drv2_046_intraday_drawdown_velocity_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of intraday 252-day drawdown."""
    hwm = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - hwm, hwm)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_drv2_047_vwap_gap_63d_velocity_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day VWAP gap (long VWAP gap acceleration)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    gap = _safe_div(close - vwap, vwap)
    return gap.diff(_TD_WEEK)


def dacc_drv2_048_drawdown_deepening_streak_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-deepening-day streak (streak growing faster)."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    is_deep = (dd_chg < 0).astype(int)
    group = (is_deep == 0).cumsum()
    streak = is_deep.groupby(group).cumsum().astype(float)
    return streak.diff(_TD_WEEK)


def dacc_drv2_049_drawdown_area_63d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day drawdown area (quarter-horizon area acceleration)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_QTR)
    return area.diff(_TD_WEEK)


def dacc_drv2_050_drawdown_252d_velocity_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of 5-day drawdown velocity (fast-smooth velocity signal)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_WEEK)


def dacc_drv2_051_drawdown_63d_slope_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day OLS slope of 63-day drawdown."""
    slp = _linslope(_drawdown(close, _TD_QTR), _TD_MON)
    return slp.diff(_TD_MON)


def dacc_drv2_052_drawdown_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day OLS slope of 21-day drawdown."""
    slp = _linslope(_drawdown(close, _TD_MON), _TD_WEEK)
    return slp.diff(_TD_WEEK)


def dacc_drv2_053_drawdown_composite_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite 21-day OLS slope across 21d/63d/252d drawdowns."""
    s21 = _linslope(_drawdown(close, _TD_MON), _TD_MON)
    s63 = _linslope(_drawdown(close, _TD_QTR), _TD_MON)
    s252 = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    composite_slp = (s21 + s63 + s252) / 3.0
    return composite_slp.diff(_TD_WEEK)


def dacc_drv2_054_drawdown_zscore_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day drawdown z-score over 21 days."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    slp = _linslope(z, _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv2_055_drawdown_momentum_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-5 drawdown depth (EWM momentum acceleration)."""
    dd_ewm5 = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_WEEK)
    return dd_ewm5.diff(_TD_WEEK)


def dacc_drv2_056_drawdown_new_depth_rate_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day new-depth count (monthly change in new-lows pace)."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    count63 = _rolling_sum((dd < prior_min).astype(float), _TD_QTR)
    return count63.diff(_TD_MON)


def dacc_drv2_057_drawdown_duration_fraction_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day underwater fraction (quarterly change in duration velocity)."""
    roll_high = _rolling_max(close, _TD_YEAR)
    frac = _rolling_mean((close < roll_high).astype(float), _TD_QTR)
    return frac.diff(_TD_MON)


def dacc_drv2_058_drawdown_area_velocity_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of 5-day change in 21-day drawdown area (smooth area velocity)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_MON)


def dacc_drv2_059_drawdown_vwap_accel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of 21-day VWAP gap (monthly gap acceleration)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    gap = _safe_div(close - vwap, vwap)
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_drv2_060_drawdown_126d_accel_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of 5-day velocity of 126-day drawdown (fast-smooth half-year accel)."""
    vel = _drawdown(close, _TD_HALF).diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_WEEK)


def dacc_drv2_061_drawdown_depth_vol_weighted_velocity_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted 21-day drawdown depth."""
    dd = _drawdown(close, _TD_YEAR)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vw_dd = _rolling_mean(dd * vol_norm, _TD_MON)
    return vw_dd.diff(_TD_WEEK)


def dacc_drv2_062_drawdown_slope_ewm5_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-5 of 21-day drawdown slope (fast-smooth slope velocity)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    slp_ewm = _ewm_mean(slp, _TD_WEEK)
    return slp_ewm.diff(_TD_WEEK)


def dacc_drv2_063_drawdown_slope_ewm21_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-21 of 21-day drawdown slope (smooth slope velocity)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    slp_ewm = _ewm_mean(slp, _TD_MON)
    return slp_ewm.diff(_TD_WEEK)


def dacc_drv2_064_drawdown_median_21d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling median drawdown (robust depth velocity)."""
    med = _drawdown(close, _TD_YEAR).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()
    return med.diff(_TD_WEEK)


def dacc_drv2_065_drawdown_area_ratio_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-to-252d drawdown area ratio (short-vs-long area accel)."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    area21 = _rolling_sum(dd_abs, _TD_MON)
    area252 = _rolling_sum(dd_abs, _TD_YEAR)
    ratio = _safe_div(area21 * (_TD_YEAR / _TD_MON), area252)
    return ratio.diff(_TD_WEEK)


def dacc_drv2_066_drawdown_cross_window_accel_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day drawdown minus 63-day drawdown) cross-window gap velocity."""
    cross = _drawdown(close, _TD_MON) - _drawdown(close, _TD_QTR)
    return cross.diff(_TD_WEEK)


def dacc_drv2_067_drawdown_63d_minus_252d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (63-day drawdown minus 252-day drawdown) gap velocity."""
    cross = _drawdown(close, _TD_QTR) - _drawdown(close, _TD_YEAR)
    return cross.diff(_TD_WEEK)


def dacc_drv2_068_drawdown_atr_norm_velocity_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of ATR-normalized 252-day drawdown depth."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    dd_norm = _safe_div(_drawdown(close, _TD_YEAR) * close, atr21)
    return dd_norm.diff(_TD_WEEK)


def dacc_drv2_069_drawdown_intraday_low_velocity_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of intraday-low drawdown from 252-day high."""
    hwm = _rolling_max(high, _TD_YEAR)
    ld = _safe_div(low - hwm, hwm)
    return ld.diff(_TD_MON)


def dacc_drv2_070_drawdown_composite_velocity_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of 5-day velocity of 4-window composite drawdown."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    vel = comp.diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_WEEK)


def dacc_drv2_071_drawdown_zscore_velocity_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of 5-day change in 252-day drawdown z-score (smooth z-score velocity)."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    vel = z.diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_MON)


def dacc_drv2_072_drawdown_slope_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of 252-day drawdown — 126-day lookback variant."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_HALF)
    return slp.diff(_TD_WEEK)


def dacc_drv2_073_drawdown_velocity_zscore_252d_v2(close: pd.Series) -> pd.Series:
    """Z-score of 1-day drawdown velocity within 252-day distribution."""
    vel = _drawdown(close, _TD_YEAR).diff(1)
    m = _rolling_mean(vel, _TD_YEAR)
    s = _rolling_std(vel, _TD_YEAR)
    return _safe_div(vel - m, s)


def dacc_drv2_074_drawdown_area_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day drawdown area (slope of area growth)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    return _linslope(area, _TD_MON)


def dacc_drv2_075_drawdown_cumsum_velocity_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of 21-day cumulative drawdown velocity (smooth net deterioration)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    cum_vel = _rolling_sum(vel, _TD_MON)
    return _ewm_mean(cum_vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_ACCELERATION_REGISTRY_2ND_DERIVATIVES = {
    "dacc_drv2_001_drawdown_252d_velocity_5d_diff": {"inputs": ["close"], "func": dacc_drv2_001_drawdown_252d_velocity_5d_diff},
    "dacc_drv2_002_drawdown_252d_velocity_21d_diff": {"inputs": ["close"], "func": dacc_drv2_002_drawdown_252d_velocity_21d_diff},
    "dacc_drv2_003_drawdown_63d_velocity_5d_diff": {"inputs": ["close"], "func": dacc_drv2_003_drawdown_63d_velocity_5d_diff},
    "dacc_drv2_004_drawdown_21d_velocity_5d_diff": {"inputs": ["close"], "func": dacc_drv2_004_drawdown_21d_velocity_5d_diff},
    "dacc_drv2_005_drawdown_slope_21d_5d_diff": {"inputs": ["close"], "func": dacc_drv2_005_drawdown_slope_21d_5d_diff},
    "dacc_drv2_006_drawdown_slope_21d_21d_diff": {"inputs": ["close"], "func": dacc_drv2_006_drawdown_slope_21d_21d_diff},
    "dacc_drv2_007_log_drawdown_velocity_5d_diff": {"inputs": ["close"], "func": dacc_drv2_007_log_drawdown_velocity_5d_diff},
    "dacc_drv2_008_hwm_gap_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_008_hwm_gap_slope_5d_diff},
    "dacc_drv2_009_drawdown_area_21d_5d_diff": {"inputs": ["close"], "func": dacc_drv2_009_drawdown_area_21d_5d_diff},
    "dacc_drv2_010_drawdown_area_63d_21d_diff": {"inputs": ["close"], "func": dacc_drv2_010_drawdown_area_63d_21d_diff},
    "dacc_drv2_011_drawdown_composite_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_011_drawdown_composite_velocity_5d},
    "dacc_drv2_012_drawdown_composite_accel_5d": {"inputs": ["close"], "func": dacc_drv2_012_drawdown_composite_accel_5d},
    "dacc_drv2_013_drawdown_zscore_5d_diff": {"inputs": ["close"], "func": dacc_drv2_013_drawdown_zscore_5d_diff},
    "dacc_drv2_014_drawdown_zscore_21d_diff": {"inputs": ["close"], "func": dacc_drv2_014_drawdown_zscore_21d_diff},
    "dacc_drv2_015_vwap_gap_velocity_5d": {"inputs": ["close", "volume"], "func": dacc_drv2_015_vwap_gap_velocity_5d},
    "dacc_drv2_016_drawdown_depth_increment_5d_diff": {"inputs": ["close"], "func": dacc_drv2_016_drawdown_depth_increment_5d_diff},
    "dacc_drv2_017_hwm_gap_widening_accel_5d": {"inputs": ["close"], "func": dacc_drv2_017_hwm_gap_widening_accel_5d},
    "dacc_drv2_018_drawdown_ewm_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_018_drawdown_ewm_velocity_5d},
    "dacc_drv2_019_drawdown_slope_63d_5d_diff": {"inputs": ["close"], "func": dacc_drv2_019_drawdown_slope_63d_5d_diff},
    "dacc_drv2_020_successive_decline_accel_5d": {"inputs": ["close"], "func": dacc_drv2_020_successive_decline_accel_5d},
    "dacc_drv2_021_drawdown_duration_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_021_drawdown_duration_velocity_5d},
    "dacc_drv2_022_drawdown_area_velocity_slope_21d": {"inputs": ["close"], "func": dacc_drv2_022_drawdown_area_velocity_slope_21d},
    "dacc_drv2_023_intraday_drawdown_velocity_5d": {"inputs": ["close", "high"], "func": dacc_drv2_023_intraday_drawdown_velocity_5d},
    "dacc_drv2_024_drawdown_new_depth_rate_5d_diff": {"inputs": ["close"], "func": dacc_drv2_024_drawdown_new_depth_rate_5d_diff},
    "dacc_drv2_025_drawdown_accel_ewm_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_025_drawdown_accel_ewm_velocity_5d},
    "dacc_drv2_026_drawdown_126d_velocity_5d_diff": {"inputs": ["close"], "func": dacc_drv2_026_drawdown_126d_velocity_5d_diff},
    "dacc_drv2_027_drawdown_504d_velocity_5d_diff": {"inputs": ["close"], "func": dacc_drv2_027_drawdown_504d_velocity_5d_diff},
    "dacc_drv2_028_drawdown_126d_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_028_drawdown_126d_slope_5d_diff},
    "dacc_drv2_029_drawdown_504d_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_029_drawdown_504d_slope_5d_diff},
    "dacc_drv2_030_drawdown_252d_velocity_63d_diff": {"inputs": ["close"], "func": dacc_drv2_030_drawdown_252d_velocity_63d_diff},
    "dacc_drv2_031_drawdown_63d_velocity_21d_diff": {"inputs": ["close"], "func": dacc_drv2_031_drawdown_63d_velocity_21d_diff},
    "dacc_drv2_032_drawdown_21d_velocity_21d_diff": {"inputs": ["close"], "func": dacc_drv2_032_drawdown_21d_velocity_21d_diff},
    "dacc_drv2_033_log_drawdown_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_033_log_drawdown_slope_5d_diff},
    "dacc_drv2_034_drawdown_area_252d_5d_diff": {"inputs": ["close"], "func": dacc_drv2_034_drawdown_area_252d_5d_diff},
    "dacc_drv2_035_drawdown_composite_21d_diff": {"inputs": ["close"], "func": dacc_drv2_035_drawdown_composite_21d_diff},
    "dacc_drv2_036_hwm_gap_slope_21d_diff": {"inputs": ["close"], "func": dacc_drv2_036_hwm_gap_slope_21d_diff},
    "dacc_drv2_037_drawdown_zscore_63d_diff": {"inputs": ["close"], "func": dacc_drv2_037_drawdown_zscore_63d_diff},
    "dacc_drv2_038_drawdown_ewm5_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_038_drawdown_ewm5_velocity_5d},
    "dacc_drv2_039_drawdown_ewm63_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_039_drawdown_ewm63_velocity_5d},
    "dacc_drv2_040_drawdown_cross_4window_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_040_drawdown_cross_4window_velocity_5d},
    "dacc_drv2_041_drawdown_cross_4window_accel_5d": {"inputs": ["close"], "func": dacc_drv2_041_drawdown_cross_4window_accel_5d},
    "dacc_drv2_042_drawdown_slope_5d_diff_21w": {"inputs": ["close"], "func": dacc_drv2_042_drawdown_slope_5d_diff_21w},
    "dacc_drv2_043_drawdown_area_velocity_ewm5": {"inputs": ["close"], "func": dacc_drv2_043_drawdown_area_velocity_ewm5},
    "dacc_drv2_044_drawdown_velocity_pct_rank_252d": {"inputs": ["close"], "func": dacc_drv2_044_drawdown_velocity_pct_rank_252d},
    "dacc_drv2_045_drawdown_accel_pct_rank_252d_v2": {"inputs": ["close"], "func": dacc_drv2_045_drawdown_accel_pct_rank_252d_v2},
    "dacc_drv2_046_intraday_drawdown_velocity_21d": {"inputs": ["close", "high"], "func": dacc_drv2_046_intraday_drawdown_velocity_21d},
    "dacc_drv2_047_vwap_gap_63d_velocity_5d": {"inputs": ["close", "volume"], "func": dacc_drv2_047_vwap_gap_63d_velocity_5d},
    "dacc_drv2_048_drawdown_deepening_streak_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_048_drawdown_deepening_streak_velocity_5d},
    "dacc_drv2_049_drawdown_area_63d_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_049_drawdown_area_63d_velocity_5d},
    "dacc_drv2_050_drawdown_252d_velocity_ewm5": {"inputs": ["close"], "func": dacc_drv2_050_drawdown_252d_velocity_ewm5},
    "dacc_drv2_051_drawdown_63d_slope_21d_diff": {"inputs": ["close"], "func": dacc_drv2_051_drawdown_63d_slope_21d_diff},
    "dacc_drv2_052_drawdown_21d_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_052_drawdown_21d_slope_5d_diff},
    "dacc_drv2_053_drawdown_composite_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_053_drawdown_composite_slope_5d_diff},
    "dacc_drv2_054_drawdown_zscore_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv2_054_drawdown_zscore_slope_5d_diff},
    "dacc_drv2_055_drawdown_momentum_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_055_drawdown_momentum_velocity_5d},
    "dacc_drv2_056_drawdown_new_depth_rate_21d_diff": {"inputs": ["close"], "func": dacc_drv2_056_drawdown_new_depth_rate_21d_diff},
    "dacc_drv2_057_drawdown_duration_fraction_21d_diff": {"inputs": ["close"], "func": dacc_drv2_057_drawdown_duration_fraction_21d_diff},
    "dacc_drv2_058_drawdown_area_velocity_ewm21": {"inputs": ["close"], "func": dacc_drv2_058_drawdown_area_velocity_ewm21},
    "dacc_drv2_059_drawdown_vwap_accel_21d": {"inputs": ["close", "volume"], "func": dacc_drv2_059_drawdown_vwap_accel_21d},
    "dacc_drv2_060_drawdown_126d_accel_ewm5": {"inputs": ["close"], "func": dacc_drv2_060_drawdown_126d_accel_ewm5},
    "dacc_drv2_061_drawdown_depth_vol_weighted_velocity_5d": {"inputs": ["close", "volume"], "func": dacc_drv2_061_drawdown_depth_vol_weighted_velocity_5d},
    "dacc_drv2_062_drawdown_slope_ewm5_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_062_drawdown_slope_ewm5_velocity_5d},
    "dacc_drv2_063_drawdown_slope_ewm21_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_063_drawdown_slope_ewm21_velocity_5d},
    "dacc_drv2_064_drawdown_median_21d_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_064_drawdown_median_21d_velocity_5d},
    "dacc_drv2_065_drawdown_area_ratio_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_065_drawdown_area_ratio_velocity_5d},
    "dacc_drv2_066_drawdown_cross_window_accel_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_066_drawdown_cross_window_accel_velocity_5d},
    "dacc_drv2_067_drawdown_63d_minus_252d_velocity_5d": {"inputs": ["close"], "func": dacc_drv2_067_drawdown_63d_minus_252d_velocity_5d},
    "dacc_drv2_068_drawdown_atr_norm_velocity_5d": {"inputs": ["close", "high", "low"], "func": dacc_drv2_068_drawdown_atr_norm_velocity_5d},
    "dacc_drv2_069_drawdown_intraday_low_velocity_21d": {"inputs": ["close", "high", "low"], "func": dacc_drv2_069_drawdown_intraday_low_velocity_21d},
    "dacc_drv2_070_drawdown_composite_velocity_ewm5": {"inputs": ["close"], "func": dacc_drv2_070_drawdown_composite_velocity_ewm5},
    "dacc_drv2_071_drawdown_zscore_velocity_ewm21": {"inputs": ["close"], "func": dacc_drv2_071_drawdown_zscore_velocity_ewm21},
    "dacc_drv2_072_drawdown_slope_126d_5d_diff": {"inputs": ["close"], "func": dacc_drv2_072_drawdown_slope_126d_5d_diff},
    "dacc_drv2_073_drawdown_velocity_zscore_252d_v2": {"inputs": ["close"], "func": dacc_drv2_073_drawdown_velocity_zscore_252d_v2},
    "dacc_drv2_074_drawdown_area_21d_slope_21d": {"inputs": ["close"], "func": dacc_drv2_074_drawdown_area_21d_slope_21d},
    "dacc_drv2_075_drawdown_cumsum_velocity_ewm21": {"inputs": ["close"], "func": dacc_drv2_075_drawdown_cumsum_velocity_ewm21},
}
