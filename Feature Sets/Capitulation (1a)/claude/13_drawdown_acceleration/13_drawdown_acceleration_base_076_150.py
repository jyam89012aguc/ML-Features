"""
13_drawdown_acceleration — Base Features 076-200
Domain: drawdown acceleration — whether a price decline is speeding up; 2nd-order behavior
of the drawdown path: gap to trailing highs widening at increasing rate, successive declines
steeper, slope of the underwater curve steepening.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling minimum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling standard deviation over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    """Rolling median over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


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


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Drawdown z-scores and distributional measures ---

def dacc_076_drawdown_252d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252-day drawdown relative to its 252-day rolling distribution."""
    dd = _drawdown(close, _TD_YEAR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    return _safe_div(dd - m, s)


def dacc_077_drawdown_252d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day drawdown (all-history extremity)."""
    dd = _drawdown(close, _TD_YEAR)
    m = dd.expanding(min_periods=5).mean()
    s = dd.expanding(min_periods=5).std()
    return _safe_div(dd - m, s)


def dacc_078_drawdown_21d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day drawdown within trailing 504-day distribution."""
    dd = _drawdown(close, _TD_MON)
    m = _rolling_mean(dd, 504)
    s = _rolling_std(dd, 504)
    return _safe_div(dd - m, s)


def dacc_079_drawdown_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day drawdown within 252-day distribution."""
    dd = _drawdown(close, _TD_QTR)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    return _safe_div(dd - m, s)


def dacc_080_drawdown_velocity_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day drawdown velocity within 252-day distribution."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    m = _rolling_mean(vel, _TD_YEAR)
    s = _rolling_std(vel, _TD_YEAR)
    return _safe_div(vel - m, s)


def dacc_081_drawdown_accel_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day drawdown acceleration within 252-day distribution."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    m = _rolling_mean(accel, _TD_YEAR)
    s = _rolling_std(accel, _TD_YEAR)
    return _safe_div(accel - m, s)


def dacc_082_drawdown_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day drawdown in trailing 504-day distribution."""
    dd = _drawdown(close, _TD_YEAR)
    return dd.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dacc_083_drawdown_slope_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 21-day drawdown slope (all-history slope extremity)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    m = slp.expanding(min_periods=5).mean()
    s = slp.expanding(min_periods=5).std()
    return _safe_div(slp - m, s)


def dacc_084_drawdown_depth_accel_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day drawdown acceleration within trailing 252-day window."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return accel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_085_drawdown_ewm_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWM-21 smoothed drawdown depth within 252-day distribution."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_MON)
    m = _rolling_mean(dd_ewm, _TD_YEAR)
    s = _rolling_std(dd_ewm, _TD_YEAR)
    return _safe_div(dd_ewm - m, s)


# --- Group I (086-095): Drawdown duration and time-underwater measures ---

def dacc_086_days_since_last_high_21d(close: pd.Series) -> pd.Series:
    """Days since close was last at or above its 21-day rolling high."""
    roll_high = _rolling_max(close, _TD_MON)
    at_high = (close >= roll_high).astype(int)
    group = at_high.cumsum()
    days_since = (~at_high.astype(bool)).astype(int)
    return days_since.groupby(group).cumsum().astype(float)


def dacc_087_days_since_last_high_252d(close: pd.Series) -> pd.Series:
    """Days since close was last at or above its 252-day rolling high."""
    roll_high = _rolling_max(close, _TD_YEAR)
    at_high = (close >= roll_high).astype(int)
    group = at_high.cumsum()
    days_since = (~at_high.astype(bool)).astype(int)
    return days_since.groupby(group).cumsum().astype(float)


def dacc_088_days_underwater_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days that close was below its 252-day high."""
    roll_high = _rolling_max(close, _TD_YEAR)
    underwater = (close < roll_high).astype(float)
    return _rolling_mean(underwater, _TD_QTR)


def dacc_089_days_underwater_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days that close was below its 252-day high."""
    roll_high = _rolling_max(close, _TD_YEAR)
    underwater = (close < roll_high).astype(float)
    return _rolling_mean(underwater, _TD_YEAR)


def dacc_090_time_underwater_21d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 63-day fraction of days underwater (duration accelerating)."""
    roll_high = _rolling_max(close, _TD_YEAR)
    underwater = (close < roll_high).astype(float)
    frac = _rolling_mean(underwater, _TD_QTR)
    return frac.diff(_TD_WEEK)


def dacc_091_drawdown_duration_accel_zscore(close: pd.Series) -> pd.Series:
    """Z-score of days-since-252d-high within trailing 252-day distribution."""
    roll_high = _rolling_max(close, _TD_YEAR)
    at_high = (close >= roll_high).astype(int)
    group = at_high.cumsum()
    days_under = (~at_high.astype(bool)).astype(int)
    dur = days_under.groupby(group).cumsum().astype(float)
    m = _rolling_mean(dur, _TD_YEAR)
    s = _rolling_std(dur, _TD_YEAR)
    return _safe_div(dur - m, s)


def dacc_092_drawdown_depth_times_duration(close: pd.Series) -> pd.Series:
    """Product of 252-day drawdown depth and days-since-high (pain area proxy)."""
    dd = _drawdown(close, _TD_YEAR).abs()
    roll_high = _rolling_max(close, _TD_YEAR)
    at_high = (close >= roll_high).astype(int)
    group = at_high.cumsum()
    days_under = (~at_high.astype(bool)).astype(int)
    dur = days_under.groupby(group).cumsum().astype(float)
    return dd * dur


def dacc_093_drawdown_area_21d(close: pd.Series) -> pd.Series:
    """Sum of daily 252-day drawdown magnitudes over 21 days (area under underwater curve)."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    return _rolling_sum(dd_abs, _TD_MON)


def dacc_094_drawdown_area_63d(close: pd.Series) -> pd.Series:
    """Sum of daily 252-day drawdown magnitudes over 63 days."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    return _rolling_sum(dd_abs, _TD_QTR)


def dacc_095_drawdown_area_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 21-day drawdown area (area expanding = acceleration)."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    area21 = _rolling_sum(dd_abs, _TD_MON)
    return area21.diff(_TD_WEEK)


# --- Group J (096-105): High-water-mark gap and distance measures ---

def dacc_096_dist_from_52wk_high_pct(close: pd.Series) -> pd.Series:
    """Percentage distance of close below 52-week (252-day) closing high."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - hwm, hwm)


def dacc_097_dist_from_52wk_high_log(close: pd.Series) -> pd.Series:
    """Log distance from 52-week closing high."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(hwm)


def dacc_098_hwm_gap_widening_5d(close: pd.Series) -> pd.Series:
    """5-day change in distance from 52-week high (widening = bearish)."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    return gap.diff(_TD_WEEK)


def dacc_099_hwm_gap_widening_21d(close: pd.Series) -> pd.Series:
    """21-day change in distance from 52-week high."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    return gap.diff(_TD_MON)


def dacc_100_hwm_gap_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 52-week high-gap over the last 21 days (steepening of descent)."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    return _linslope(gap, _TD_MON)


def dacc_101_hwm_gap_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of 52-week high-gap over the last 5 days."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    return _linslope(gap, _TD_WEEK)


def dacc_102_hwm_gap_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 52-week high gap (gap accelerating)."""
    hwm = _rolling_max(close, _TD_YEAR)
    gap = _safe_div(close - hwm, hwm)
    slp = _linslope(gap, _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_103_hwm_126d_gap_pct(close: pd.Series) -> pd.Series:
    """Percentage distance from 126-day high."""
    hwm = _rolling_max(close, _TD_HALF)
    return _safe_div(close - hwm, hwm)


def dacc_104_hwm_126d_gap_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in distance from 126-day high."""
    hwm = _rolling_max(close, _TD_HALF)
    gap = _safe_div(close - hwm, hwm)
    return gap.diff(_TD_WEEK)


def dacc_105_hwm_gap_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day high gap to 252-day high gap (short vs long horizon severity)."""
    g21 = _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))
    g252 = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _safe_div(g21, g252.replace(0, np.nan))


# --- Group K (106-115): Drawdown acceleration with volume signals ---

def dacc_106_drawdown_on_high_vol_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average 252-day drawdown on days with above-average volume over 21 days."""
    dd = _drawdown(close, _TD_YEAR)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol_dd = dd.where(volume > avg_vol, np.nan)
    return high_vol_dd.rolling(_TD_MON, min_periods=1).mean()


def dacc_107_drawdown_accel_on_high_vol_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean daily drawdown deepening on high-volume days over 63 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol_chg = dd_chg.where(volume > avg_vol, np.nan)
    return high_vol_chg.rolling(_TD_QTR, min_periods=1).mean()


def dacc_108_vol_ratio_deepening_vs_recovery_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio: deepening days vs non-deepening days over 21 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    is_deep = dd_chg < 0
    deep_vol = volume.where(is_deep, np.nan).rolling(_TD_MON, min_periods=1).mean()
    flat_vol = volume.where(~is_deep, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(deep_vol, flat_vol)


def dacc_109_drawdown_depth_increment_volume_weighted_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of drawdown increments over 21 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deepening = dd_chg.where(dd_chg < 0, 0.0)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _rolling_sum(deepening * vol_norm, _TD_MON)


def dacc_110_drawdown_depth_increment_volume_weighted_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of drawdown increments over 63 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deepening = dd_chg.where(dd_chg < 0, 0.0)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return _rolling_sum(deepening * vol_norm, _TD_QTR)


def dacc_111_drawdown_vwap_gap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 21-day VWAP as fraction of VWAP (underwater from avg cost)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _safe_div(close - vwap, vwap)


def dacc_112_drawdown_vwap_gap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 63-day VWAP as fraction of VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _safe_div(close - vwap, vwap)


def dacc_113_vwap_gap_5d_chg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day change in 21-day VWAP gap (drift below average cost accelerating)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    gap = _safe_div(close - vwap, vwap)
    return gap.diff(_TD_WEEK)


def dacc_114_drawdown_high_vol_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day deepening events that occurred on high-volume days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    deep_hiVol = ((dd_chg < 0) & (volume > avg_vol)).astype(float)
    deep_any = (dd_chg < 0).astype(float)
    return _safe_div(_rolling_sum(deep_hiVol, _TD_MON), _rolling_sum(deep_any, _TD_MON))


def dacc_115_cumulative_volume_during_drawdown_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Total volume traded on drawdown-deepening days over 21 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deep_vol = volume.where(dd_chg < 0, 0.0)
    return _rolling_sum(deep_vol, _TD_MON)


# --- Group L (116-125): Open-to-close and gap contributions to drawdown ---

def dacc_116_open_drawdown_from_252d_high(close: pd.Series, open: pd.Series) -> pd.Series:
    """Drawdown of open from 252-day close high (gap-open contribution to underwater)."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(open - hwm, hwm)


def dacc_117_open_drawdown_5d_chg(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day change in open drawdown from 252-day high."""
    hwm = _rolling_max(close, _TD_YEAR)
    od = _safe_div(open - hwm, hwm)
    return od.diff(_TD_WEEK)


def dacc_118_intraday_drawdown_deepening_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where close-drawdown was worse than open-drawdown (intraday worsening)."""
    hwm = _rolling_max(close, _TD_YEAR)
    cd = _safe_div(close - hwm, hwm)
    od = _safe_div(open - hwm, hwm)
    worse = (cd < od).astype(float)
    return _rolling_mean(worse, _TD_MON)


def dacc_119_gap_contribution_to_drawdown_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average gap-down contribution (open vs prior-close) on drawdown-deepening days, 21d."""
    hwm = _rolling_max(close, _TD_YEAR)
    cd = _safe_div(close - hwm, hwm)
    cd_chg = cd.diff(1)
    gap_ret = _safe_div(open - close.shift(1), close.shift(1))
    gap_on_deep = gap_ret.where(cd_chg < 0, np.nan)
    return gap_on_deep.rolling(_TD_MON, min_periods=1).mean()


def dacc_120_close_drawdown_minus_open_drawdown_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean difference of close-drawdown minus open-drawdown over 21 days."""
    hwm = _rolling_max(close, _TD_YEAR)
    cd = _safe_div(close - hwm, hwm)
    od = _safe_div(open - hwm, hwm)
    return _rolling_mean(cd - od, _TD_MON)


def dacc_121_drawdown_open_to_close_accel_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day change in intraday drawdown deepening (close-open vs prior-close-open)."""
    hwm = _rolling_max(close, _TD_YEAR)
    cd = _safe_div(close - hwm, hwm)
    od = _safe_div(open - hwm, hwm)
    intra = cd - od
    return intra.diff(_TD_WEEK)


def dacc_122_gap_down_drawdown_score_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of gap-down magnitudes on drawdown-deepening days over 21 days."""
    hwm = _rolling_max(close, _TD_YEAR)
    cd_chg = _safe_div(close - hwm, hwm).diff(1)
    gap = _safe_div(open - close.shift(1), close.shift(1))
    gap_deep = gap.where((cd_chg < 0) & (gap < 0), 0.0)
    return _rolling_sum(gap_deep, _TD_MON)


def dacc_123_low_drawdown_accel_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day change in intraday-low drawdown from 252-day high."""
    hwm = _rolling_max(high, _TD_YEAR)
    ld = _safe_div(low - hwm, hwm)
    return ld.diff(_TD_WEEK)


def dacc_124_high_drawdown_accel_5d(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day change in intraday-high drawdown from 252-day high (even highs dipping)."""
    hwm252 = _rolling_max(high, _TD_YEAR)
    hd = _safe_div(high - hwm252, hwm252)
    return hd.diff(_TD_WEEK)


def dacc_125_intraday_range_during_drawdown_accel(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average intraday range (high-low) on drawdown-deepening days over 21 days."""
    hwm = _rolling_max(close, _TD_YEAR)
    cd_chg = _safe_div(close - hwm, hwm).diff(1)
    rng = high - low
    rng_deep = rng.where(cd_chg < 0, np.nan)
    return rng_deep.rolling(_TD_MON, min_periods=1).mean()


# --- Group M (126-135): Multi-horizon drawdown composites and interaction scores ---

def dacc_126_drawdown_composite_score(close: pd.Series) -> pd.Series:
    """Composite of normalized 21d, 63d, 252d drawdowns (multi-horizon distress)."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    return (n21 + n63 + n252) / 3.0


def dacc_127_drawdown_composite_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in multi-horizon drawdown composite score."""
    dd21 = _drawdown(close, _TD_MON)
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    n21 = _safe_div(dd21, _rolling_std(dd21, _TD_YEAR).clip(lower=_EPS))
    n63 = _safe_div(dd63, _rolling_std(dd63, _TD_YEAR).clip(lower=_EPS))
    n252 = _safe_div(dd252, _rolling_std(dd252, _TD_YEAR).clip(lower=_EPS))
    composite = (n21 + n63 + n252) / 3.0
    return composite.diff(_TD_WEEK)


def dacc_128_drawdown_slope_composite(close: pd.Series) -> pd.Series:
    """Composite of 21-day OLS slopes across 21d/63d/252d drawdown series."""
    s21 = _linslope(_drawdown(close, _TD_MON), _TD_MON)
    s63 = _linslope(_drawdown(close, _TD_QTR), _TD_MON)
    s252 = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return (s21 + s63 + s252) / 3.0


def dacc_129_drawdown_depth_area_ratio_21_252(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 252-day drawdown area (short-term area accelerating)."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    area21 = _rolling_sum(dd_abs, _TD_MON)
    area252 = _rolling_sum(dd_abs, _TD_YEAR)
    return _safe_div(area21 * (_TD_YEAR / _TD_MON), area252)


def dacc_130_drawdown_accel_vs_avg_21d(close: pd.Series) -> pd.Series:
    """Current 5-day drawdown acceleration vs 252-day avg acceleration."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    avg_accel = _rolling_mean(accel, _TD_YEAR)
    return accel - avg_accel


def dacc_131_drawdown_252d_slope_vs_avg(close: pd.Series) -> pd.Series:
    """Current 21-day slope of 252-day drawdown minus 252-day avg slope."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    avg_slp = _rolling_mean(slp, _TD_YEAR)
    return slp - avg_slp


def dacc_132_drawdown_velocity_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM-21 of 5-day drawdown velocity (smoothed deterioration trend)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_MON)


def dacc_133_drawdown_accel_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM-21 of 5-day drawdown acceleration (smoothed 2nd-order trend)."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_MON)


def dacc_134_drawdown_velocity_cumsum_21d(close: pd.Series) -> pd.Series:
    """Sum of 5-day drawdown velocities over 21 days (net deepening over month)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return _rolling_sum(vel, _TD_MON)


def dacc_135_drawdown_accel_positive_days_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63 days where drawdown acceleration was negative (worsening)."""
    accel = _drawdown(close, _TD_YEAR).diff(1).diff(1)
    worsening = (accel < 0).astype(float)
    return _rolling_mean(worsening, _TD_QTR)


# --- Group N (136-145): Cross-period drawdown comparisons and regime flags ---

def dacc_136_drawdown_new_depth_flag_21d(close: pd.Series) -> pd.Series:
    """Flag: today's 252-day drawdown is deeper than any in the prior 21 days."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_MON, min_periods=1).min()
    return (dd < prior_min).astype(float)


def dacc_137_drawdown_new_depth_flag_63d(close: pd.Series) -> pd.Series:
    """Flag: today's 252-day drawdown is deeper than any in the prior 63 days."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (dd < prior_min).astype(float)


def dacc_138_drawdown_new_depth_count_63d(close: pd.Series) -> pd.Series:
    """Count of new 252-day drawdown depth records in trailing 63 days."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return _rolling_sum((dd < prior_min).astype(float), _TD_QTR)


def dacc_139_drawdown_new_depth_count_252d(close: pd.Series) -> pd.Series:
    """Count of new drawdown records (new depth) in trailing 252 days."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return _rolling_sum((dd < prior_min).astype(float), _TD_YEAR)


def dacc_140_drawdown_gt10pct_flag(close: pd.Series) -> pd.Series:
    """Flag: 252-day drawdown is greater than 10%."""
    return (_drawdown(close, _TD_YEAR) < -0.10).astype(float)


def dacc_141_drawdown_gt20pct_flag(close: pd.Series) -> pd.Series:
    """Flag: 252-day drawdown is greater than 20% (bear-market territory)."""
    return (_drawdown(close, _TD_YEAR) < -0.20).astype(float)


def dacc_142_drawdown_gt30pct_flag(close: pd.Series) -> pd.Series:
    """Flag: 252-day drawdown is greater than 30% (severe bear)."""
    return (_drawdown(close, _TD_YEAR) < -0.30).astype(float)


def dacc_143_drawdown_exceeds_1yr_avg_flag(close: pd.Series) -> pd.Series:
    """Flag: current drawdown is worse than the 252-day rolling mean drawdown."""
    dd = _drawdown(close, _TD_YEAR)
    avg_dd = _rolling_mean(dd, _TD_YEAR)
    return (dd < avg_dd).astype(float)


def dacc_144_drawdown_acceleration_regime_score(close: pd.Series) -> pd.Series:
    """Score combining: depth flag, velocity flag, acceleration flag (0-3 distress count)."""
    dd = _drawdown(close, _TD_YEAR)
    avg_dd = _rolling_mean(dd, _TD_YEAR)
    vel = dd.diff(_TD_WEEK)
    avg_vel = _rolling_mean(vel, _TD_YEAR)
    accel = vel.diff(_TD_WEEK)
    avg_accel = _rolling_mean(accel, _TD_YEAR)
    f1 = (dd < avg_dd).astype(float)
    f2 = (vel < avg_vel).astype(float)
    f3 = (accel < avg_accel).astype(float)
    return f1 + f2 + f3


def dacc_145_drawdown_acceleration_persistence_21d(close: pd.Series) -> pd.Series:
    """Fraction of past 21 days where drawdown was both deep AND worsening."""
    dd = _drawdown(close, _TD_YEAR)
    avg_dd = _rolling_mean(dd, _TD_YEAR)
    dd_chg = dd.diff(1)
    persistent = ((dd < avg_dd) & (dd_chg < 0)).astype(float)
    return _rolling_mean(persistent, _TD_MON)


# --- Group O (146-150): Composite distress indices ---

def dacc_146_drawdown_distress_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day distress index: depth * vol_norm * acceleration magnitude."""
    dd = _drawdown(close, _TD_YEAR).abs()
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    accel = dd.diff(_TD_WEEK).diff(_TD_WEEK).abs()
    return _rolling_mean(dd * vol_norm * (1.0 + accel), _TD_MON)


def dacc_147_drawdown_momentum_index(close: pd.Series) -> pd.Series:
    """Drawdown momentum: EWM-5 of daily drawdown depth (captures persistent worsening)."""
    return _ewm_mean(_drawdown(close, _TD_YEAR), _TD_WEEK)


def dacc_148_drawdown_acceleration_magnitude_63d(close: pd.Series) -> pd.Series:
    """Mean absolute 5-day drawdown acceleration over trailing 63 days."""
    accel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK).diff(_TD_WEEK)
    return _rolling_mean(accel.abs(), _TD_QTR)


def dacc_149_drawdown_severity_trend_score(close: pd.Series) -> pd.Series:
    """Trend score: slope of 252-day drawdown normalized by std of drawdown."""
    dd = _drawdown(close, _TD_YEAR)
    slp = _linslope(dd, _TD_MON)
    std_dd = _rolling_std(dd, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(slp, std_dd)


def dacc_150_drawdown_combined_accel_distress(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined distress: depth from intraday high * vol_norm * slope steepening."""
    hwm = _rolling_max(high, _TD_YEAR)
    depth = _safe_div(close - hwm, hwm).abs()
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    gap = _safe_div(close - hwm, hwm)
    slope_steep = _linslope(gap, _TD_MON).abs()
    return depth * vol_norm * (1.0 + slope_steep)


# --- Group P2 (176-185): Drawdown regime persistence and streak measures ---

def dacc_176_drawdown_deepening_streak_21d(close: pd.Series) -> pd.Series:
    """Count of consecutive days drawdown deepened (current run length), capped at 21."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    is_deep = (dd_chg < 0).astype(int)
    group = (is_deep == 0).cumsum()
    streak = is_deep.groupby(group).cumsum().astype(float)
    return streak.clip(upper=21.0)


def dacc_177_drawdown_deepening_streak_63d(close: pd.Series) -> pd.Series:
    """Count of consecutive days drawdown deepened, capped at 63."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    is_deep = (dd_chg < 0).astype(int)
    group = (is_deep == 0).cumsum()
    streak = is_deep.groupby(group).cumsum().astype(float)
    return streak.clip(upper=63.0)


def dacc_178_drawdown_recovery_streak_21d(close: pd.Series) -> pd.Series:
    """Count of consecutive days drawdown shallowed (recovery run), capped at 21."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    is_rec = (dd_chg > 0).astype(int)
    group = (is_rec == 0).cumsum()
    streak = is_rec.groupby(group).cumsum().astype(float)
    return streak.clip(upper=21.0)


def dacc_179_drawdown_max_deepening_run_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive deepening-day run length in trailing 63 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    is_deep = (dd_chg < 0).astype(float)
    group = (is_deep == 0).cumsum()
    run = is_deep.groupby(group).cumsum()
    return run.rolling(_TD_QTR, min_periods=1).max()


def dacc_180_drawdown_gt40pct_flag(close: pd.Series) -> pd.Series:
    """Flag: 252-day drawdown is greater than 40% (capitulation-level bear)."""
    return (_drawdown(close, _TD_YEAR) < -0.40).astype(float)


def dacc_181_drawdown_gt50pct_flag(close: pd.Series) -> pd.Series:
    """Flag: 252-day drawdown is greater than 50% (extreme distress)."""
    return (_drawdown(close, _TD_YEAR) < -0.50).astype(float)


def dacc_182_drawdown_median_21d(close: pd.Series) -> pd.Series:
    """21-day rolling median of 252-day drawdown (robust central depth measure)."""
    return _rolling_median(_drawdown(close, _TD_YEAR), _TD_MON)


def dacc_183_drawdown_median_63d(close: pd.Series) -> pd.Series:
    """63-day rolling median of 252-day drawdown."""
    return _rolling_median(_drawdown(close, _TD_YEAR), _TD_QTR)


def dacc_184_drawdown_iqr_63d(close: pd.Series) -> pd.Series:
    """63-day interquartile range of 252-day drawdown (dispersion of underwater curve)."""
    dd = _drawdown(close, _TD_YEAR)
    q75 = dd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = dd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def dacc_185_drawdown_iqr_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 63-day IQR of drawdown (spreading out of underwater distribution)."""
    dd = _drawdown(close, _TD_YEAR)
    q75 = dd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = dd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    return iqr.diff(_TD_WEEK)


# --- Group Q2 (186-195): Drawdown vs volume interaction extensions ---

def dacc_186_drawdown_vwap_gap_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 252-day VWAP as fraction of VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    return _safe_div(close - vwap, vwap)


def dacc_187_drawdown_vwap_252d_gap_5d_chg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day change in 252-day VWAP gap (long-term VWAP distance accelerating)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_YEAR), _rolling_sum(volume, _TD_YEAR))
    gap = _safe_div(close - vwap, vwap)
    return gap.diff(_TD_WEEK)


def dacc_188_drawdown_volume_on_new_depth_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on new-depth record days over 21 days, normalized by avg volume."""
    dd = _drawdown(close, _TD_YEAR)
    prior_min = dd.shift(1).rolling(_TD_MON, min_periods=1).min()
    new_depth = dd < prior_min
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    vol_on_new = vol_norm.where(new_depth, np.nan)
    return vol_on_new.rolling(_TD_MON, min_periods=1).mean()


def dacc_189_drawdown_vol_surge_deepening_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with both volume >1.5x avg and drawdown deepening over 21 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    both = ((dd_chg < 0) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(both, _TD_MON)


def dacc_190_drawdown_vol_dry_deepening_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with volume <0.7x avg AND drawdown deepening over 21 days (no-panic sell)."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    avg_vol = _rolling_mean(volume, _TD_MON)
    both = ((dd_chg < 0) & (volume < 0.7 * avg_vol)).astype(float)
    return _rolling_sum(both, _TD_MON)


def dacc_191_drawdown_area_volume_weighted_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of daily drawdown magnitudes over 21 days."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _rolling_sum(dd_abs * vol_norm, _TD_MON)


def dacc_192_drawdown_area_volume_weighted_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of daily drawdown magnitudes over 63 days."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return _rolling_sum(dd_abs * vol_norm, _TD_QTR)


def dacc_193_drawdown_vol_ratio_21d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day volume-weighted drawdown area (recent vs quarter)."""
    dd_abs = _drawdown(close, _TD_YEAR).abs()
    vol_norm21 = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vol_norm63 = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    area21 = _rolling_sum(dd_abs * vol_norm21, _TD_MON)
    area63 = _rolling_sum(dd_abs * vol_norm63, _TD_QTR)
    return _safe_div(area21 * (_TD_QTR / _TD_MON), area63)


def dacc_194_drawdown_vwap_gap_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 21-day VWAP gap (trend in VWAP distance)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    gap = _safe_div(close - vwap, vwap)
    return _linslope(gap, _TD_MON)


def dacc_195_drawdown_depth_vol_norm_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM-21 of volume-normalized daily drawdown depth (smooth vol-adj underwater)."""
    dd = _drawdown(close, _TD_YEAR)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _ewm_mean(dd * vol_norm, _TD_MON)


# --- Group R2 (196-200): Composite and cross-horizon drawdown distress ---

def dacc_196_drawdown_cross_4window_composite(close: pd.Series) -> pd.Series:
    """Composite of 21d, 63d, 126d, 252d drawdowns equally weighted."""
    return (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0


def dacc_197_drawdown_cross_4window_composite_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 4-window drawdown composite."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    return comp.diff(_TD_WEEK)


def dacc_198_drawdown_252d_abs_area_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day drawdown area within its trailing 252-day distribution."""
    area21 = _rolling_sum(_drawdown(close, _TD_YEAR).abs(), _TD_MON)
    return area21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_199_drawdown_intraday_vs_close_gap_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean of (intraday-high drawdown minus intraday-low drawdown) over 21 days."""
    hwm = _rolling_max(high, _TD_YEAR)
    dd_high = _safe_div(high - hwm, hwm)
    dd_low = _safe_div(low - hwm, hwm)
    return _rolling_mean(dd_high - dd_low, _TD_MON)


def dacc_200_drawdown_composite_ewm_trend(close: pd.Series) -> pd.Series:
    """EWM-21 of 4-window composite drawdown (smoothed multi-horizon distress trend)."""
    comp = (_drawdown(close, _TD_MON) + _drawdown(close, _TD_QTR)
            + _drawdown(close, _TD_HALF) + _drawdown(close, _TD_YEAR)) / 4.0
    return _ewm_mean(comp, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_ACCELERATION_REGISTRY_076_150 = {
    "dacc_076_drawdown_252d_zscore_252d": {"inputs": ["close"], "func": dacc_076_drawdown_252d_zscore_252d},
    "dacc_077_drawdown_252d_expanding_zscore": {"inputs": ["close"], "func": dacc_077_drawdown_252d_expanding_zscore},
    "dacc_078_drawdown_21d_zscore_504d": {"inputs": ["close"], "func": dacc_078_drawdown_21d_zscore_504d},
    "dacc_079_drawdown_63d_zscore_252d": {"inputs": ["close"], "func": dacc_079_drawdown_63d_zscore_252d},
    "dacc_080_drawdown_velocity_zscore_252d": {"inputs": ["close"], "func": dacc_080_drawdown_velocity_zscore_252d},
    "dacc_081_drawdown_accel_zscore_252d": {"inputs": ["close"], "func": dacc_081_drawdown_accel_zscore_252d},
    "dacc_082_drawdown_252d_pct_rank_504d": {"inputs": ["close"], "func": dacc_082_drawdown_252d_pct_rank_504d},
    "dacc_083_drawdown_slope_expanding_zscore": {"inputs": ["close"], "func": dacc_083_drawdown_slope_expanding_zscore},
    "dacc_084_drawdown_depth_accel_pct_rank_252d": {"inputs": ["close"], "func": dacc_084_drawdown_depth_accel_pct_rank_252d},
    "dacc_085_drawdown_ewm_21d_zscore_252d": {"inputs": ["close"], "func": dacc_085_drawdown_ewm_21d_zscore_252d},
    "dacc_086_days_since_last_high_21d": {"inputs": ["close"], "func": dacc_086_days_since_last_high_21d},
    "dacc_087_days_since_last_high_252d": {"inputs": ["close"], "func": dacc_087_days_since_last_high_252d},
    "dacc_088_days_underwater_fraction_63d": {"inputs": ["close"], "func": dacc_088_days_underwater_fraction_63d},
    "dacc_089_days_underwater_fraction_252d": {"inputs": ["close"], "func": dacc_089_days_underwater_fraction_252d},
    "dacc_090_time_underwater_21d_5d_chg": {"inputs": ["close"], "func": dacc_090_time_underwater_21d_5d_chg},
    "dacc_091_drawdown_duration_accel_zscore": {"inputs": ["close"], "func": dacc_091_drawdown_duration_accel_zscore},
    "dacc_092_drawdown_depth_times_duration": {"inputs": ["close"], "func": dacc_092_drawdown_depth_times_duration},
    "dacc_093_drawdown_area_21d": {"inputs": ["close"], "func": dacc_093_drawdown_area_21d},
    "dacc_094_drawdown_area_63d": {"inputs": ["close"], "func": dacc_094_drawdown_area_63d},
    "dacc_095_drawdown_area_5d_chg": {"inputs": ["close"], "func": dacc_095_drawdown_area_5d_chg},
    "dacc_096_dist_from_52wk_high_pct": {"inputs": ["close"], "func": dacc_096_dist_from_52wk_high_pct},
    "dacc_097_dist_from_52wk_high_log": {"inputs": ["close"], "func": dacc_097_dist_from_52wk_high_log},
    "dacc_098_hwm_gap_widening_5d": {"inputs": ["close"], "func": dacc_098_hwm_gap_widening_5d},
    "dacc_099_hwm_gap_widening_21d": {"inputs": ["close"], "func": dacc_099_hwm_gap_widening_21d},
    "dacc_100_hwm_gap_slope_21d": {"inputs": ["close"], "func": dacc_100_hwm_gap_slope_21d},
    "dacc_101_hwm_gap_slope_5d": {"inputs": ["close"], "func": dacc_101_hwm_gap_slope_5d},
    "dacc_102_hwm_gap_accel_5d": {"inputs": ["close"], "func": dacc_102_hwm_gap_accel_5d},
    "dacc_103_hwm_126d_gap_pct": {"inputs": ["close"], "func": dacc_103_hwm_126d_gap_pct},
    "dacc_104_hwm_126d_gap_5d_chg": {"inputs": ["close"], "func": dacc_104_hwm_126d_gap_5d_chg},
    "dacc_105_hwm_gap_21d_vs_252d": {"inputs": ["close"], "func": dacc_105_hwm_gap_21d_vs_252d},
    "dacc_106_drawdown_on_high_vol_days_21d": {"inputs": ["close", "volume"], "func": dacc_106_drawdown_on_high_vol_days_21d},
    "dacc_107_drawdown_accel_on_high_vol_days": {"inputs": ["close", "volume"], "func": dacc_107_drawdown_accel_on_high_vol_days},
    "dacc_108_vol_ratio_deepening_vs_recovery_days_21d": {"inputs": ["close", "volume"], "func": dacc_108_vol_ratio_deepening_vs_recovery_days_21d},
    "dacc_109_drawdown_depth_increment_volume_weighted_21d": {"inputs": ["close", "volume"], "func": dacc_109_drawdown_depth_increment_volume_weighted_21d},
    "dacc_110_drawdown_depth_increment_volume_weighted_63d": {"inputs": ["close", "volume"], "func": dacc_110_drawdown_depth_increment_volume_weighted_63d},
    "dacc_111_drawdown_vwap_gap_21d": {"inputs": ["close", "volume"], "func": dacc_111_drawdown_vwap_gap_21d},
    "dacc_112_drawdown_vwap_gap_63d": {"inputs": ["close", "volume"], "func": dacc_112_drawdown_vwap_gap_63d},
    "dacc_113_vwap_gap_5d_chg": {"inputs": ["close", "volume"], "func": dacc_113_vwap_gap_5d_chg},
    "dacc_114_drawdown_high_vol_fraction_21d": {"inputs": ["close", "volume"], "func": dacc_114_drawdown_high_vol_fraction_21d},
    "dacc_115_cumulative_volume_during_drawdown_21d": {"inputs": ["close", "volume"], "func": dacc_115_cumulative_volume_during_drawdown_21d},
    "dacc_116_open_drawdown_from_252d_high": {"inputs": ["close", "open"], "func": dacc_116_open_drawdown_from_252d_high},
    "dacc_117_open_drawdown_5d_chg": {"inputs": ["close", "open"], "func": dacc_117_open_drawdown_5d_chg},
    "dacc_118_intraday_drawdown_deepening_fraction_21d": {"inputs": ["close", "open"], "func": dacc_118_intraday_drawdown_deepening_fraction_21d},
    "dacc_119_gap_contribution_to_drawdown_21d": {"inputs": ["close", "open"], "func": dacc_119_gap_contribution_to_drawdown_21d},
    "dacc_120_close_drawdown_minus_open_drawdown_21d": {"inputs": ["close", "open"], "func": dacc_120_close_drawdown_minus_open_drawdown_21d},
    "dacc_121_drawdown_open_to_close_accel_5d": {"inputs": ["close", "open"], "func": dacc_121_drawdown_open_to_close_accel_5d},
    "dacc_122_gap_down_drawdown_score_21d": {"inputs": ["close", "open"], "func": dacc_122_gap_down_drawdown_score_21d},
    "dacc_123_low_drawdown_accel_5d": {"inputs": ["close", "high", "low"], "func": dacc_123_low_drawdown_accel_5d},
    "dacc_124_high_drawdown_accel_5d": {"inputs": ["close", "high"], "func": dacc_124_high_drawdown_accel_5d},
    "dacc_125_intraday_range_during_drawdown_accel": {"inputs": ["close", "high", "low"], "func": dacc_125_intraday_range_during_drawdown_accel},
    "dacc_126_drawdown_composite_score": {"inputs": ["close"], "func": dacc_126_drawdown_composite_score},
    "dacc_127_drawdown_composite_5d_chg": {"inputs": ["close"], "func": dacc_127_drawdown_composite_5d_chg},
    "dacc_128_drawdown_slope_composite": {"inputs": ["close"], "func": dacc_128_drawdown_slope_composite},
    "dacc_129_drawdown_depth_area_ratio_21_252": {"inputs": ["close"], "func": dacc_129_drawdown_depth_area_ratio_21_252},
    "dacc_130_drawdown_accel_vs_avg_21d": {"inputs": ["close"], "func": dacc_130_drawdown_accel_vs_avg_21d},
    "dacc_131_drawdown_252d_slope_vs_avg": {"inputs": ["close"], "func": dacc_131_drawdown_252d_slope_vs_avg},
    "dacc_132_drawdown_velocity_ewm_21d": {"inputs": ["close"], "func": dacc_132_drawdown_velocity_ewm_21d},
    "dacc_133_drawdown_accel_ewm_21d": {"inputs": ["close"], "func": dacc_133_drawdown_accel_ewm_21d},
    "dacc_134_drawdown_velocity_cumsum_21d": {"inputs": ["close"], "func": dacc_134_drawdown_velocity_cumsum_21d},
    "dacc_135_drawdown_accel_positive_days_fraction_63d": {"inputs": ["close"], "func": dacc_135_drawdown_accel_positive_days_fraction_63d},
    "dacc_136_drawdown_new_depth_flag_21d": {"inputs": ["close"], "func": dacc_136_drawdown_new_depth_flag_21d},
    "dacc_137_drawdown_new_depth_flag_63d": {"inputs": ["close"], "func": dacc_137_drawdown_new_depth_flag_63d},
    "dacc_138_drawdown_new_depth_count_63d": {"inputs": ["close"], "func": dacc_138_drawdown_new_depth_count_63d},
    "dacc_139_drawdown_new_depth_count_252d": {"inputs": ["close"], "func": dacc_139_drawdown_new_depth_count_252d},
    "dacc_140_drawdown_gt10pct_flag": {"inputs": ["close"], "func": dacc_140_drawdown_gt10pct_flag},
    "dacc_141_drawdown_gt20pct_flag": {"inputs": ["close"], "func": dacc_141_drawdown_gt20pct_flag},
    "dacc_142_drawdown_gt30pct_flag": {"inputs": ["close"], "func": dacc_142_drawdown_gt30pct_flag},
    "dacc_143_drawdown_exceeds_1yr_avg_flag": {"inputs": ["close"], "func": dacc_143_drawdown_exceeds_1yr_avg_flag},
    "dacc_144_drawdown_acceleration_regime_score": {"inputs": ["close"], "func": dacc_144_drawdown_acceleration_regime_score},
    "dacc_145_drawdown_acceleration_persistence_21d": {"inputs": ["close"], "func": dacc_145_drawdown_acceleration_persistence_21d},
    "dacc_146_drawdown_distress_index_21d": {"inputs": ["close", "volume"], "func": dacc_146_drawdown_distress_index_21d},
    "dacc_147_drawdown_momentum_index": {"inputs": ["close"], "func": dacc_147_drawdown_momentum_index},
    "dacc_148_drawdown_acceleration_magnitude_63d": {"inputs": ["close"], "func": dacc_148_drawdown_acceleration_magnitude_63d},
    "dacc_149_drawdown_severity_trend_score": {"inputs": ["close"], "func": dacc_149_drawdown_severity_trend_score},
    "dacc_150_drawdown_combined_accel_distress": {"inputs": ["close", "high", "volume"], "func": dacc_150_drawdown_combined_accel_distress},
    "dacc_176_drawdown_deepening_streak_21d": {"inputs": ["close"], "func": dacc_176_drawdown_deepening_streak_21d},
    "dacc_177_drawdown_deepening_streak_63d": {"inputs": ["close"], "func": dacc_177_drawdown_deepening_streak_63d},
    "dacc_178_drawdown_recovery_streak_21d": {"inputs": ["close"], "func": dacc_178_drawdown_recovery_streak_21d},
    "dacc_179_drawdown_max_deepening_run_63d": {"inputs": ["close"], "func": dacc_179_drawdown_max_deepening_run_63d},
    "dacc_180_drawdown_gt40pct_flag": {"inputs": ["close"], "func": dacc_180_drawdown_gt40pct_flag},
    "dacc_181_drawdown_gt50pct_flag": {"inputs": ["close"], "func": dacc_181_drawdown_gt50pct_flag},
    "dacc_182_drawdown_median_21d": {"inputs": ["close"], "func": dacc_182_drawdown_median_21d},
    "dacc_183_drawdown_median_63d": {"inputs": ["close"], "func": dacc_183_drawdown_median_63d},
    "dacc_184_drawdown_iqr_63d": {"inputs": ["close"], "func": dacc_184_drawdown_iqr_63d},
    "dacc_185_drawdown_iqr_5d_chg": {"inputs": ["close"], "func": dacc_185_drawdown_iqr_5d_chg},
    "dacc_186_drawdown_vwap_gap_252d": {"inputs": ["close", "volume"], "func": dacc_186_drawdown_vwap_gap_252d},
    "dacc_187_drawdown_vwap_252d_gap_5d_chg": {"inputs": ["close", "volume"], "func": dacc_187_drawdown_vwap_252d_gap_5d_chg},
    "dacc_188_drawdown_volume_on_new_depth_days_21d": {"inputs": ["close", "volume"], "func": dacc_188_drawdown_volume_on_new_depth_days_21d},
    "dacc_189_drawdown_vol_surge_deepening_21d": {"inputs": ["close", "volume"], "func": dacc_189_drawdown_vol_surge_deepening_21d},
    "dacc_190_drawdown_vol_dry_deepening_21d": {"inputs": ["close", "volume"], "func": dacc_190_drawdown_vol_dry_deepening_21d},
    "dacc_191_drawdown_area_volume_weighted_21d": {"inputs": ["close", "volume"], "func": dacc_191_drawdown_area_volume_weighted_21d},
    "dacc_192_drawdown_area_volume_weighted_63d": {"inputs": ["close", "volume"], "func": dacc_192_drawdown_area_volume_weighted_63d},
    "dacc_193_drawdown_vol_ratio_21d_vs_63d": {"inputs": ["close", "volume"], "func": dacc_193_drawdown_vol_ratio_21d_vs_63d},
    "dacc_194_drawdown_vwap_gap_slope_21d": {"inputs": ["close", "volume"], "func": dacc_194_drawdown_vwap_gap_slope_21d},
    "dacc_195_drawdown_depth_vol_norm_ewm21": {"inputs": ["close", "volume"], "func": dacc_195_drawdown_depth_vol_norm_ewm21},
    "dacc_196_drawdown_cross_4window_composite": {"inputs": ["close"], "func": dacc_196_drawdown_cross_4window_composite},
    "dacc_197_drawdown_cross_4window_composite_5d_chg": {"inputs": ["close"], "func": dacc_197_drawdown_cross_4window_composite_5d_chg},
    "dacc_198_drawdown_252d_abs_area_pct_rank_252d": {"inputs": ["close"], "func": dacc_198_drawdown_252d_abs_area_pct_rank_252d},
    "dacc_199_drawdown_intraday_vs_close_gap_21d": {"inputs": ["close", "high", "low"], "func": dacc_199_drawdown_intraday_vs_close_gap_21d},
    "dacc_200_drawdown_composite_ewm_trend": {"inputs": ["close"], "func": dacc_200_drawdown_composite_ewm_trend},
}
