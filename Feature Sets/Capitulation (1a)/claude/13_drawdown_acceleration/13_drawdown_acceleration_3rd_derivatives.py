"""
13_drawdown_acceleration — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative drawdown-acceleration features — inflection /
exhaustion of underwater-curve steepening; jerk in the drawdown acceleration path.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def dacc_drv3_001_drawdown_252d_velocity_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Third diff: 5d-diff of (5d-diff of 5d-drawdown-velocity) — jerk of widening."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_002_drawdown_252d_velocity_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 5-day drawdown velocity."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    vel21 = vel.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_003_drawdown_63d_velocity_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day velocity of 63-day drawdown."""
    vel = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_004_drawdown_21d_velocity_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day velocity of 21-day drawdown."""
    vel = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_005_drawdown_slope_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day OLS slope of 252-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_006_drawdown_slope_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in OLS slope of 252-day drawdown."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    vel21 = slp.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_007_log_drawdown_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day diff of 5-day log-drawdown velocity (jerk in log space)."""
    vel = _log_drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_008_drawdown_area_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day drawdown area) — area jerk."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_009_drawdown_area_63d_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 63-day drawdown area)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_QTR)
    vel21 = area.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_010_hwm_gap_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day HWM gap velocity) — gap jerk."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    vel = gap.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_011_drawdown_composite_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite drawdown acceleration (3rd diff of composite)."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    accel = composite.diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_012_drawdown_zscore_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of drawdown z-score) — z-score jerk."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_013_drawdown_zscore_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in drawdown z-score."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_014_drawdown_ewm_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EWM-21 drawdown) — EWM jerk."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    vel = dd_ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_015_drawdown_slope_63d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day OLS slope of 252-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_QTR)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_016_successive_decline_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of successive decline steepening measure)."""
    ret5 = close.pct_change(_TD_WEEK)
    delta = ret5 - ret5.shift(_TD_WEEK)
    accel = delta.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_017_drawdown_slope_accel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (5-day diff of 21-day drawdown slope)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dacc_drv3_018_drawdown_depth_increment_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day deepening sum) — deepening jerk."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deepening = dd_chg.where(dd_chg < 0, 0.0)
    incr_sum = _rolling_sum(deepening, _TD_MON)
    vel = incr_sum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_019_vwap_gap_accel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day VWAP gap velocity) — VWAP gap jerk."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    gap = _safe_div(close - vwap, vwap)
    vel = gap.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_020_intraday_drawdown_accel_5d_diff(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of intraday 252-day drawdown velocity)."""
    hwm = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - hwm, hwm)
    accel = dd.diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_021_drawdown_new_depth_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day new-depth count)."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    new_depth = (dd < prior_min).astype(float)
    count63 = _rolling_sum(new_depth, _TD_QTR)
    vel = count63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_022_drawdown_duration_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day underwater fraction)."""
    roll_high = _rolling_max(close, _TD_YEAR)
    underwater = (close < roll_high).astype(float)
    frac = _rolling_mean(underwater, _TD_QTR)
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_023_drawdown_area_velocity_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope (21d) of 5-day drawdown area velocity."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    slp = _linslope(vel, _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv3_024_drawdown_ewm_accel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (5-day diff of EWM-21 drawdown velocity)."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    vel = dd_ewm.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def dacc_drv3_025_drawdown_composite_vel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5-day velocity of composite drawdown score."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    vel = composite.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── 3rd-Derivative Feature Functions (026-075) ────────────────────────────────

def dacc_drv3_026_drawdown_126d_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day 126-day drawdown velocity) — 126d jerk."""
    vel = _drawdown(close, _TD_HALF).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_027_drawdown_504d_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day 504-day drawdown velocity) — 504d jerk."""
    vel = _drawdown(close, 504).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_028_drawdown_slope_126d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day OLS slope of 126-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_HALF), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_029_drawdown_cross_4window_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 4-window composite velocity) — composite jerk."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    accel = comp.diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_030_drawdown_slope_composite_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of slope composite across 21d/63d/252d drawdowns)."""
    s21 = _linslope(_drawdown(close, _TD_MON), _TD_MON)
    s63 = _linslope(_drawdown(close, _TD_QTR), _TD_MON)
    s252 = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    comp_slp = (s21 + s63 + s252) / 3.0
    vel = comp_slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_031_drawdown_ewm5_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EWM-5 drawdown depth velocity) — fast EWM jerk."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_WEEK)
    vel = dd_ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_032_drawdown_ewm63_accel_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EWM-63 drawdown depth velocity) — slow EWM jerk."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_QTR)
    vel = dd_ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_033_drawdown_63d_slope_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day OLS slope of 63-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_QTR), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_034_drawdown_21d_slope_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day OLS slope of 21-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_MON), _TD_WEEK)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_035_drawdown_area_63d_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day drawdown area velocity) — area 63d jerk."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_QTR)
    vel = area.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_036_drawdown_zscore_jerk_21d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of drawdown z-score velocity) — z-score jerk at 21d."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_037_drawdown_velocity_accel_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of (5-day diff of 5-day drawdown velocity)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _linslope(accel, _TD_MON)


def dacc_drv3_038_drawdown_composite_jerk_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5-day diff of composite drawdown acceleration."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    accel = composite.diff(_TD_WEEK).diff(_TD_WEEK)
    jerk = accel.diff(_TD_WEEK)
    return _linslope(jerk, _TD_MON)


def dacc_drv3_039_drawdown_area_accel_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of 21-day drawdown area velocity) — fast smooth area jerk."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def dacc_drv3_040_drawdown_hwm_gap_jerk_21d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 5-day HWM gap velocity) — cross-period gap jerk."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    vel = gap.diff(_TD_WEEK)
    vel21 = vel.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_041_drawdown_new_depth_jerk_21d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 63-day new-depth count rate)."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    count63 = _rolling_sum((dd < prior_min).astype(float), _TD_QTR)
    vel21 = count63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_042_drawdown_duration_jerk_21d(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of 63-day underwater fraction) — duration jerk."""
    roll_high = _rolling_max(close, _TD_YEAR)
    frac = _rolling_mean((close < roll_high).astype(float), _TD_QTR)
    vel21 = frac.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def dacc_drv3_043_drawdown_ewm_accel_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of EWM-21 drawdown velocity) — fast smooth EWM jerk."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    vel = dd_ewm.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def dacc_drv3_044_drawdown_slope_accel_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of 5-day diff of 21-day drawdown slope) — slope jerk smooth."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def dacc_drv3_045_drawdown_vwap_jerk_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day VWAP gap change) — VWAP gap 4th order signal."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    gap = _safe_div(close - vwap, vwap)
    vel = gap.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_046_drawdown_intraday_jerk_5d(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of intraday 252-day drawdown acceleration)."""
    hwm = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - hwm, hwm)
    accel = dd.diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_047_drawdown_area_velocity_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope over 21 days of 5-day drawdown area velocity."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    slp = _linslope(vel, _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_drv3_048_drawdown_composite_vel_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 4-window composite drawdown velocity)."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    vel = comp.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_049_drawdown_slope_63d_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day OLS slope of 252-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_QTR)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_050_successive_decline_jerk_21d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of successive decline acceleration)."""
    ret5 = close.pct_change(_TD_WEEK)
    delta = ret5 - ret5.shift(_TD_WEEK)
    accel = delta.diff(_TD_WEEK)
    return accel.diff(_TD_MON)


def dacc_drv3_051_drawdown_slope_accel_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day diff of 21-day drawdown slope within 252-day distribution."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    slp_vel = slp.diff(_TD_WEEK)
    return slp_vel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_drv3_052_drawdown_velocity_jerk_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day drawdown velocity diff (jerk) within 252-day distribution."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    jerk = vel.diff(_TD_WEEK)
    return jerk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_drv3_053_drawdown_composite_jerk_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of composite drawdown acceleration) — smooth composite jerk."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    accel = composite.diff(_TD_WEEK).diff(_TD_WEEK)
    jerk = accel.diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_WEEK)


def dacc_drv3_054_drawdown_depth_jerk_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (5-day diff of 5-day diff of 5-day drawdown velocity) within 252-day dist."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    jerk = vel.diff(_TD_WEEK).diff(_TD_WEEK)
    m = _rolling_mean(jerk, _TD_YEAR)
    s = _rolling_std(jerk, _TD_YEAR)
    return _safe_div(jerk - m, s)


def dacc_drv3_055_drawdown_area_jerk_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of 5-day diff of (5-day diff of 21-day drawdown area velocity)."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_MON)


def dacc_drv3_056_drawdown_slope_jerk_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (5-day diff of 5-day diff of 21-day drawdown slope) within 252-day dist."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    jerk = slp.diff(_TD_WEEK).diff(_TD_WEEK)
    m = _rolling_mean(jerk, _TD_YEAR)
    s = _rolling_std(jerk, _TD_YEAR)
    return _safe_div(jerk - m, s)


def dacc_drv3_057_drawdown_zscore_jerk_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of 5-day diff of drawdown z-score) — smooth z-score jerk."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    z = _safe_div(dd - m, s)
    jerk = z.diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_WEEK)


def dacc_drv3_058_drawdown_log_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of log-drawdown velocity) — log drawdown jerk v2."""
    vel = _log_drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_059_drawdown_63d_velocity_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day 63-day drawdown velocity) — 63d jerk."""
    vel = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_060_drawdown_21d_velocity_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 5-day 21-day drawdown velocity) — 21d jerk."""
    vel = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return accel.diff(_TD_WEEK)


def dacc_drv3_061_drawdown_slope_21d_jerk_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day slope jerk (5-day diff of slope) within 252-day distribution."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    jerk = slp.diff(_TD_WEEK)
    m = _rolling_mean(jerk, _TD_YEAR)
    s = _rolling_std(jerk, _TD_YEAR)
    return _safe_div(jerk - m, s)


def dacc_drv3_062_drawdown_velocity_jerk_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of (5-day diff of 5-day drawdown velocity) — smooth jerk signal."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    jerk = vel.diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_MON)


def dacc_drv3_063_drawdown_cross_4window_jerk_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of 4-window composite jerk (3rd diff of composite)."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    jerk = comp.diff(_TD_WEEK).diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_WEEK)


def dacc_drv3_064_drawdown_slope_ewm5_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EWM-5 drawdown slope) — fast slope jerk."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    slp_ewm = _ewm_mean(slp, _TD_WEEK)
    vel = slp_ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_065_drawdown_area_velocity_jerk_pct_rank(close: pd.Series) -> pd.Series:
    """Percentile rank of area velocity acceleration within 252-day distribution."""
    area = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    vel = area.diff(_TD_WEEK)
    jerk = vel.diff(_TD_WEEK)
    return jerk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_drv3_066_drawdown_hwm_gap_jerk_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of 3rd diff of 52-week high gap — smooth gap jerk."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    jerk = gap.diff(_TD_WEEK).diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_WEEK)


def dacc_drv3_067_drawdown_duration_jerk_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of underwater fraction acceleration)."""
    roll_high = _rolling_max(close, _TD_YEAR)
    frac = _rolling_mean((close < roll_high).astype(float), _TD_QTR)
    jerk = frac.diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_WEEK)


def dacc_drv3_068_drawdown_126d_slope_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day OLS slope of 126-day drawdown)."""
    slp = _linslope(_drawdown(close, _TD_HALF), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_069_drawdown_atr_norm_jerk_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of ATR-normalized 252-day drawdown velocity)."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    dd_norm = _safe_div(_drawdown(close, _TD_YEAR) * close, atr21)
    vel = dd_norm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_drv3_070_drawdown_depth_jerk_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of (5-day diff of 5-day drawdown velocity acceleration)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    jerk = vel.diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(jerk, _TD_MON)


def dacc_drv3_071_drawdown_composite_accel_pct_rank(close: pd.Series) -> pd.Series:
    """Percentile rank of composite drawdown jerk within 252-day distribution."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    jerk = ((n21 + n63 + n252) / 3.0).diff(_TD_WEEK).diff(_TD_WEEK).diff(_TD_WEEK)
    return jerk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_drv3_072_drawdown_slope_accel_ewm21(close: pd.Series) -> pd.Series:
    """EWM-21 of (5-day diff of 21-day drawdown slope velocity)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    accel = slp.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_MON)


def dacc_drv3_073_drawdown_new_depth_jerk_ewm5(close: pd.Series) -> pd.Series:
    """EWM-5 of (5-day diff of 63-day new-depth count acceleration)."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    count63 = _rolling_sum((dd < prior_min).astype(float), _TD_QTR)
    vel = count63.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def dacc_drv3_074_drawdown_velocity_ewm21_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EWM-21 drawdown velocity) — EWM-vel jerk."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    vel_ewm = _ewm_mean(vel, _TD_MON)
    return vel_ewm.diff(_TD_WEEK).diff(_TD_WEEK)


def dacc_drv3_075_drawdown_composite_vel_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope over 21 days of 5-day composite drawdown velocity."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    vel = composite.diff(_TD_WEEK)
    slp = _linslope(vel, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_ACCELERATION_REGISTRY_3RD_DERIVATIVES = {
    "dacc_drv3_001_drawdown_252d_velocity_5d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_001_drawdown_252d_velocity_5d_diff_5d_diff},
    "dacc_drv3_002_drawdown_252d_velocity_21d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_002_drawdown_252d_velocity_21d_diff_5d_diff},
    "dacc_drv3_003_drawdown_63d_velocity_5d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_003_drawdown_63d_velocity_5d_diff_5d_diff},
    "dacc_drv3_004_drawdown_21d_velocity_5d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_004_drawdown_21d_velocity_5d_diff_5d_diff},
    "dacc_drv3_005_drawdown_slope_5d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_005_drawdown_slope_5d_diff_5d_diff},
    "dacc_drv3_006_drawdown_slope_21d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_006_drawdown_slope_21d_diff_5d_diff},
    "dacc_drv3_007_log_drawdown_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_007_log_drawdown_accel_5d_diff},
    "dacc_drv3_008_drawdown_area_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_008_drawdown_area_accel_5d_diff},
    "dacc_drv3_009_drawdown_area_63d_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_009_drawdown_area_63d_accel_5d_diff},
    "dacc_drv3_010_hwm_gap_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_010_hwm_gap_accel_5d_diff},
    "dacc_drv3_011_drawdown_composite_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_011_drawdown_composite_accel_5d_diff},
    "dacc_drv3_012_drawdown_zscore_accel_5d": {"inputs": ["close"], "func": dacc_drv3_012_drawdown_zscore_accel_5d},
    "dacc_drv3_013_drawdown_zscore_21d_diff_5d_diff": {"inputs": ["close"], "func": dacc_drv3_013_drawdown_zscore_21d_diff_5d_diff},
    "dacc_drv3_014_drawdown_ewm_accel_5d": {"inputs": ["close"], "func": dacc_drv3_014_drawdown_ewm_accel_5d},
    "dacc_drv3_015_drawdown_slope_63d_accel_5d": {"inputs": ["close"], "func": dacc_drv3_015_drawdown_slope_63d_accel_5d},
    "dacc_drv3_016_successive_decline_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_016_successive_decline_accel_5d_diff},
    "dacc_drv3_017_drawdown_slope_accel_slope_21d": {"inputs": ["close"], "func": dacc_drv3_017_drawdown_slope_accel_slope_21d},
    "dacc_drv3_018_drawdown_depth_increment_accel_5d": {"inputs": ["close"], "func": dacc_drv3_018_drawdown_depth_increment_accel_5d},
    "dacc_drv3_019_vwap_gap_accel_5d": {"inputs": ["close", "volume"], "func": dacc_drv3_019_vwap_gap_accel_5d},
    "dacc_drv3_020_intraday_drawdown_accel_5d_diff": {"inputs": ["close", "high"], "func": dacc_drv3_020_intraday_drawdown_accel_5d_diff},
    "dacc_drv3_021_drawdown_new_depth_accel_5d": {"inputs": ["close"], "func": dacc_drv3_021_drawdown_new_depth_accel_5d},
    "dacc_drv3_022_drawdown_duration_accel_5d": {"inputs": ["close"], "func": dacc_drv3_022_drawdown_duration_accel_5d},
    "dacc_drv3_023_drawdown_area_velocity_accel_5d": {"inputs": ["close"], "func": dacc_drv3_023_drawdown_area_velocity_accel_5d},
    "dacc_drv3_024_drawdown_ewm_accel_slope_21d": {"inputs": ["close"], "func": dacc_drv3_024_drawdown_ewm_accel_slope_21d},
    "dacc_drv3_025_drawdown_composite_vel_slope_21d": {"inputs": ["close"], "func": dacc_drv3_025_drawdown_composite_vel_slope_21d},
    "dacc_drv3_026_drawdown_126d_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_026_drawdown_126d_accel_5d_diff},
    "dacc_drv3_027_drawdown_504d_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_027_drawdown_504d_accel_5d_diff},
    "dacc_drv3_028_drawdown_slope_126d_accel_5d": {"inputs": ["close"], "func": dacc_drv3_028_drawdown_slope_126d_accel_5d},
    "dacc_drv3_029_drawdown_cross_4window_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_029_drawdown_cross_4window_jerk_5d},
    "dacc_drv3_030_drawdown_slope_composite_accel_5d": {"inputs": ["close"], "func": dacc_drv3_030_drawdown_slope_composite_accel_5d},
    "dacc_drv3_031_drawdown_ewm5_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_031_drawdown_ewm5_accel_5d_diff},
    "dacc_drv3_032_drawdown_ewm63_accel_5d_diff": {"inputs": ["close"], "func": dacc_drv3_032_drawdown_ewm63_accel_5d_diff},
    "dacc_drv3_033_drawdown_63d_slope_accel_5d": {"inputs": ["close"], "func": dacc_drv3_033_drawdown_63d_slope_accel_5d},
    "dacc_drv3_034_drawdown_21d_slope_accel_5d": {"inputs": ["close"], "func": dacc_drv3_034_drawdown_21d_slope_accel_5d},
    "dacc_drv3_035_drawdown_area_63d_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_035_drawdown_area_63d_jerk_5d},
    "dacc_drv3_036_drawdown_zscore_jerk_21d_diff": {"inputs": ["close"], "func": dacc_drv3_036_drawdown_zscore_jerk_21d_diff},
    "dacc_drv3_037_drawdown_velocity_accel_slope_21d": {"inputs": ["close"], "func": dacc_drv3_037_drawdown_velocity_accel_slope_21d},
    "dacc_drv3_038_drawdown_composite_jerk_slope_21d": {"inputs": ["close"], "func": dacc_drv3_038_drawdown_composite_jerk_slope_21d},
    "dacc_drv3_039_drawdown_area_accel_ewm5": {"inputs": ["close"], "func": dacc_drv3_039_drawdown_area_accel_ewm5},
    "dacc_drv3_040_drawdown_hwm_gap_jerk_21d_diff": {"inputs": ["close"], "func": dacc_drv3_040_drawdown_hwm_gap_jerk_21d_diff},
    "dacc_drv3_041_drawdown_new_depth_jerk_21d_diff": {"inputs": ["close"], "func": dacc_drv3_041_drawdown_new_depth_jerk_21d_diff},
    "dacc_drv3_042_drawdown_duration_jerk_21d": {"inputs": ["close"], "func": dacc_drv3_042_drawdown_duration_jerk_21d},
    "dacc_drv3_043_drawdown_ewm_accel_ewm5": {"inputs": ["close"], "func": dacc_drv3_043_drawdown_ewm_accel_ewm5},
    "dacc_drv3_044_drawdown_slope_accel_ewm5": {"inputs": ["close"], "func": dacc_drv3_044_drawdown_slope_accel_ewm5},
    "dacc_drv3_045_drawdown_vwap_jerk_5d": {"inputs": ["close", "volume"], "func": dacc_drv3_045_drawdown_vwap_jerk_5d},
    "dacc_drv3_046_drawdown_intraday_jerk_5d": {"inputs": ["close", "high"], "func": dacc_drv3_046_drawdown_intraday_jerk_5d},
    "dacc_drv3_047_drawdown_area_velocity_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv3_047_drawdown_area_velocity_slope_5d_diff},
    "dacc_drv3_048_drawdown_composite_vel_accel_5d": {"inputs": ["close"], "func": dacc_drv3_048_drawdown_composite_vel_accel_5d},
    "dacc_drv3_049_drawdown_slope_63d_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_049_drawdown_slope_63d_jerk_5d},
    "dacc_drv3_050_successive_decline_jerk_21d_diff": {"inputs": ["close"], "func": dacc_drv3_050_successive_decline_jerk_21d_diff},
    "dacc_drv3_051_drawdown_slope_accel_pct_rank_252d": {"inputs": ["close"], "func": dacc_drv3_051_drawdown_slope_accel_pct_rank_252d},
    "dacc_drv3_052_drawdown_velocity_jerk_pct_rank_252d": {"inputs": ["close"], "func": dacc_drv3_052_drawdown_velocity_jerk_pct_rank_252d},
    "dacc_drv3_053_drawdown_composite_jerk_ewm5": {"inputs": ["close"], "func": dacc_drv3_053_drawdown_composite_jerk_ewm5},
    "dacc_drv3_054_drawdown_depth_jerk_zscore_252d": {"inputs": ["close"], "func": dacc_drv3_054_drawdown_depth_jerk_zscore_252d},
    "dacc_drv3_055_drawdown_area_jerk_ewm21": {"inputs": ["close"], "func": dacc_drv3_055_drawdown_area_jerk_ewm21},
    "dacc_drv3_056_drawdown_slope_jerk_zscore_252d": {"inputs": ["close"], "func": dacc_drv3_056_drawdown_slope_jerk_zscore_252d},
    "dacc_drv3_057_drawdown_zscore_jerk_ewm5": {"inputs": ["close"], "func": dacc_drv3_057_drawdown_zscore_jerk_ewm5},
    "dacc_drv3_058_drawdown_log_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_058_drawdown_log_jerk_5d},
    "dacc_drv3_059_drawdown_63d_velocity_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_059_drawdown_63d_velocity_jerk_5d},
    "dacc_drv3_060_drawdown_21d_velocity_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_060_drawdown_21d_velocity_jerk_5d},
    "dacc_drv3_061_drawdown_slope_21d_jerk_zscore": {"inputs": ["close"], "func": dacc_drv3_061_drawdown_slope_21d_jerk_zscore},
    "dacc_drv3_062_drawdown_velocity_jerk_ewm21": {"inputs": ["close"], "func": dacc_drv3_062_drawdown_velocity_jerk_ewm21},
    "dacc_drv3_063_drawdown_cross_4window_jerk_ewm5": {"inputs": ["close"], "func": dacc_drv3_063_drawdown_cross_4window_jerk_ewm5},
    "dacc_drv3_064_drawdown_slope_ewm5_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_064_drawdown_slope_ewm5_jerk_5d},
    "dacc_drv3_065_drawdown_area_velocity_jerk_pct_rank": {"inputs": ["close"], "func": dacc_drv3_065_drawdown_area_velocity_jerk_pct_rank},
    "dacc_drv3_066_drawdown_hwm_gap_jerk_ewm5": {"inputs": ["close"], "func": dacc_drv3_066_drawdown_hwm_gap_jerk_ewm5},
    "dacc_drv3_067_drawdown_duration_jerk_ewm5": {"inputs": ["close"], "func": dacc_drv3_067_drawdown_duration_jerk_ewm5},
    "dacc_drv3_068_drawdown_126d_slope_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_068_drawdown_126d_slope_jerk_5d},
    "dacc_drv3_069_drawdown_atr_norm_jerk_5d": {"inputs": ["close", "high", "low"], "func": dacc_drv3_069_drawdown_atr_norm_jerk_5d},
    "dacc_drv3_070_drawdown_depth_jerk_ewm21": {"inputs": ["close"], "func": dacc_drv3_070_drawdown_depth_jerk_ewm21},
    "dacc_drv3_071_drawdown_composite_accel_pct_rank": {"inputs": ["close"], "func": dacc_drv3_071_drawdown_composite_accel_pct_rank},
    "dacc_drv3_072_drawdown_slope_accel_ewm21": {"inputs": ["close"], "func": dacc_drv3_072_drawdown_slope_accel_ewm21},
    "dacc_drv3_073_drawdown_new_depth_jerk_ewm5": {"inputs": ["close"], "func": dacc_drv3_073_drawdown_new_depth_jerk_ewm5},
    "dacc_drv3_074_drawdown_velocity_ewm21_jerk_5d": {"inputs": ["close"], "func": dacc_drv3_074_drawdown_velocity_ewm21_jerk_5d},
    "dacc_drv3_075_drawdown_composite_vel_slope_5d_diff": {"inputs": ["close"], "func": dacc_drv3_075_drawdown_composite_vel_slope_5d_diff},
}
