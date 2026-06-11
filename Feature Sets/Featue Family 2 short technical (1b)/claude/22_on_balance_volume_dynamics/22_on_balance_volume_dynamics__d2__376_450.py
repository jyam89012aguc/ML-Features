import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _consecutive_true_streak(b):
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _obv(close, volume):
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def f22_obvd_376_obv_negative_momentum_streak_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    neg_streak = _consecutive_true_streak(obv.diff() < 0).astype(float)
    return neg_streak.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_377_obv_momentum_thrust_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return ((obv.diff() > 0).astype(float).rolling(WDAYS, min_periods=1).sum() >= 4).astype(float)


def f22_obvd_378_obv_5d_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore(obv - obv.shift(WDAYS), YDAYS)


def f22_obvd_379_obv_21d_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore(obv - obv.shift(MDAYS), YDAYS)


def f22_obvd_380_obv_63d_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore(obv - obv.shift(QDAYS), YDAYS)


def f22_obvd_381_obv_momentum_diff_5d_vs_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore((obv - obv.shift(WDAYS)) - (obv - obv.shift(MDAYS)), YDAYS)


def f22_obvd_382_obv_first_positive_change_after_negative_streak_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    d = obv.diff()
    five_neg = (d.shift(1) < 0) & (d.shift(2) < 0) & (d.shift(3) < 0) & (d.shift(4) < 0) & (d.shift(5) < 0)
    return ((d > 0) & five_neg).astype(float)


def f22_obvd_383_obv_first_negative_change_after_positive_streak_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    d = obv.diff()
    five_pos = (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0) & (d.shift(5) > 0)
    return ((d < 0) & five_pos).astype(float)


def f22_obvd_384_obv_consecutive_negative_bars_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return (obv.diff() < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_385_obv_consecutive_positive_bars_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return (obv.diff() > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_386_down_to_up_vol_ratio_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(WDAYS, min_periods=2).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(WDAYS, min_periods=2).sum()
    return _safe_div(dn_v, up_v + 1.0)


def f22_obvd_387_down_to_up_vol_ratio_3d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(3, min_periods=2).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(3, min_periods=2).sum()
    return _safe_div(dn_v, up_v + 1.0)


def f22_obvd_388_down_vol_dominance_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    dn_v_signal = (sgn < 0) & (volume > volume.shift(1))
    return _consecutive_true_streak(dn_v_signal).astype(float)


def f22_obvd_389_up_to_down_vol_ratio_at_252d_high_5d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(WDAYS, min_periods=2).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(WDAYS, min_periods=2).sum()
    ratio = _safe_div(up_v, dn_v + 1.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ratio.where(high >= rmax, np.nan)


def f22_obvd_390_up_to_down_vol_ratio_at_252d_high_21d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    up_v = volume.where(sgn > 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(sgn < 0, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(up_v, dn_v + 1.0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ratio.where(high >= rmax, np.nan)


def f22_obvd_391_max_consec_down_vol_dominant_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    cond = (sgn < 0) & (volume > volume.shift(1))
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_392_max_consec_up_vol_dominant_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff())
    cond = (sgn > 0) & (volume > volume.shift(1))
    streak = _consecutive_true_streak(cond).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_393_net_volume_5d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    nv5 = (sgn * volume).rolling(WDAYS, min_periods=2).sum()
    return _rolling_zscore(nv5, YDAYS)


def f22_obvd_394_net_volume_3d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    nv3 = (sgn * volume).rolling(3, min_periods=2).sum()
    return _rolling_zscore(nv3, YDAYS)


def f22_obvd_395_net_volume_diff_5d_vs_21d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    nv5 = (sgn * volume).rolling(WDAYS, min_periods=2).sum()
    nv21 = (sgn * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(nv5 - nv21, YDAYS)


def f22_obvd_396_signed_vol_skewness_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).rolling(WDAYS, min_periods=3).skew()


def f22_obvd_397_signed_vol_max_5d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return _rolling_zscore((sgn * volume).rolling(WDAYS, min_periods=2).max(), YDAYS)


def f22_obvd_398_signed_vol_min_5d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return _rolling_zscore((sgn * volume).rolling(WDAYS, min_periods=2).min(), YDAYS)


def f22_obvd_399_cumulative_signed_vol_5d_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return _rolling_zscore((sgn * volume).rolling(WDAYS, min_periods=2).sum(), YDAYS)


def f22_obvd_400_cumulative_signed_vol_21d_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return _rolling_zscore((sgn * volume).rolling(MDAYS, min_periods=WDAYS).sum(), YDAYS)


def f22_obvd_401_obv_change_on_gap_fill_count_252d(open: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_dn_5d_ago = (open.shift(5) < close.shift(6))
    cap_filled = high.rolling(WDAYS, min_periods=1).max() >= close.shift(6)
    return (gap_dn_5d_ago & cap_filled).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_402_obv_change_on_breakaway_gap_count_252d(open: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max().shift(1)
    breakaway = open > rmax21
    return breakaway.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_403_obv_change_on_island_top_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_up_lag2 = open.shift(2) > high.shift(3)
    gap_dn_today = open < low.shift(1)
    return (gap_up_lag2 & gap_dn_today).astype(float)


def f22_obvd_404_obv_change_on_island_bottom_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_dn_lag2 = open.shift(2) < low.shift(3)
    gap_up_today = open > high.shift(1)
    return (gap_dn_lag2 & gap_up_today).astype(float)


def f22_obvd_405_obv_change_after_8day_consecutive_up_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    eight_up = up.shift(1)
    for i in range(2, 9):
        eight_up = eight_up & up.shift(i)
    obv = _obv(close, volume)
    d = obv.diff()
    std252 = d.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(d, std252).where(eight_up, np.nan)


def f22_obvd_406_obv_change_after_8day_consecutive_down_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dn = close < close.shift(1)
    eight_dn = dn.shift(1)
    for i in range(2, 9):
        eight_dn = eight_dn & dn.shift(i)
    obv = _obv(close, volume)
    d = obv.diff()
    std252 = d.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(d, std252).where(eight_dn, np.nan)


def f22_obvd_407_obv_change_on_fib_retrace_38_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib38 = rmin + 0.382 * (rmax - rmin)
    near = ((close - fib38).abs() / fib38) < 0.01
    return near.astype(float)


def f22_obvd_408_obv_change_on_fib_retrace_50_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib50 = rmin + 0.50 * (rmax - rmin)
    near = ((close - fib50).abs() / fib50) < 0.01
    return near.astype(float)


def f22_obvd_409_obv_change_on_fib_retrace_61_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib61 = rmin + 0.618 * (rmax - rmin)
    near = ((close - fib61).abs() / fib61) < 0.01
    return near.astype(float)


def f22_obvd_410_obv_at_first_bar_below_21ema_after_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema21 = close.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    above = close > ema21
    streak_above_yest = _consecutive_true_streak(above.shift(1).fillna(False)).astype(float)
    first_below = (~above) & (streak_above_yest >= MDAYS)
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return z.where(first_below, np.nan)


def f22_obvd_411_obv_at_first_bar_above_21ema_after_low(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema21 = close.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    below = close < ema21
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    first_above = (close > ema21) & (streak_below_yest >= MDAYS)
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return z.where(first_above, np.nan)


def f22_obvd_412_obv_change_on_test_of_recent_low_count_252d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    obv = _obv(close, volume)
    return ((low <= rmin21 * 1.005) & (obv.diff() > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_413_obv_change_on_test_of_recent_high_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    obv = _obv(close, volume)
    return ((high >= rmax21 * 0.995) & (obv.diff() < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_414_obv_change_on_round_number_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    near = pd.Series((close / 5.0 - (close / 5.0).round()).abs() <= 0.20, index=close.index)
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return z.where(near, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_415_obv_change_on_round_number_with_rejection(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    near = pd.Series((close / 5.0 - (close / 5.0).round()).abs() <= 0.20, index=close.index)
    pos = _safe_div(close - low, high - low)
    return (near & (pos <= 0.33)).astype(float)


def f22_obvd_416_obv_breakout_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return (obv > obv.rolling(YDAYS, min_periods=QDAYS).max().shift(1)).astype(float)


def f22_obvd_417_obv_breakdown_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return (obv < obv.rolling(YDAYS, min_periods=QDAYS).min().shift(1)).astype(float)


def f22_obvd_418_obv_first_252d_high_after_drawdown_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    at_max = obv >= rmax
    was_below = (obv < 0.9 * rmax).shift(1).rolling(MDAYS, min_periods=WDAYS).max().fillna(False).astype(bool)
    return (at_max & was_below).astype(float)


def f22_obvd_419_obv_first_252d_low_after_rally_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    at_min = obv <= rmin
    was_above = (obv > 1.1 * rmin.abs()).shift(1).rolling(MDAYS, min_periods=WDAYS).max().fillna(False).astype(bool)
    return (at_min & was_above).astype(float)


def f22_obvd_420_obv_zigzag_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    sgn = np.sign(obv.diff())
    return (sgn != sgn.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_421_obv_above_zero_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (_obv(close, volume) > 0).astype(float)


def f22_obvd_422_obv_above_zero_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    return (_obv(close, volume) > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_423_obv_crossed_zero_recently_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    cross = (np.sign(obv) != np.sign(obv.shift(1)))
    return cross.shift(1).rolling(WDAYS, min_periods=1).max().fillna(False).astype(float)


def f22_obvd_424_obv_zero_cross_age_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    cross = (np.sign(obv) != np.sign(obv.shift(1))).astype(int)
    grp = cross.cumsum()
    bars = (~cross.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f22_obvd_425_obv_velocity_acceleration_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore(obv.diff().diff(), YDAYS)


def f22_obvd_426_obv_jerk_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore(obv.diff().diff().diff(), YDAYS)


def f22_obvd_427_obv_smoothness_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return 1.0 - _safe_div(obv.diff().rolling(YDAYS, min_periods=QDAYS).std(), obv.abs().rolling(YDAYS, min_periods=QDAYS).mean())


def f22_obvd_428_obv_trend_clarity_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    direct = (obv - obv.shift(YDAYS)).abs()
    vol_sum = obv.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(direct, vol_sum)


def f22_obvd_429_obv_choppiness_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = obv.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(obv.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum(), rmax - rmin)


def f22_obvd_430_obv_efficiency_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    direct = (obv - obv.shift(YDAYS)).abs()
    vol_sum = obv.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(direct, vol_sum)


def f22_obvd_431_obv_diff_when_close_new_252d_high_avg_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    obv = _obv(close, volume)
    return obv.diff().where(close >= cmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_432_obv_diff_when_close_new_5y_high_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    cmax5y = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    obv = _obv(close, volume)
    return obv.diff().where(close >= cmax5y, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_433_obv_diff_at_alltime_high_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = close.expanding(min_periods=YDAYS).max()
    obv = _obv(close, volume)
    return obv.diff().where(close >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_434_obv_at_alltime_high_dwell_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = close.expanding(min_periods=YDAYS).max()
    obv = _obv(close, volume)
    return ((close >= rmax) & (obv.diff() > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_435_obv_diff_zscore_at_alltime_high_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = close.expanding(min_periods=YDAYS).max()
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return z.where(close >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_436_obv_negative_during_uptrend_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema63 = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    obv = _obv(close, volume)
    return ((obv.diff() < 0) & (close > ema63)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_437_obv_negative_during_uptrend_streak_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema63 = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    obv = _obv(close, volume)
    streak = _consecutive_true_streak((obv.diff() < 0) & (close > ema63)).astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_438_obv_positive_during_downtrend_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema63 = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    obv = _obv(close, volume)
    return ((obv.diff() > 0) & (close < ema63)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_439_obv_compound_topping_signal_simple(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    obv = _obv(close, volume)
    m21 = obv - obv.shift(MDAYS)
    return ((high >= rmax) & (obv.diff() < 0) & (m21 < m21.shift(WDAYS))).astype(float)


def f22_obvd_440_obv_breakout_failure_within_3d_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    rmax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    cross_up = (obv >= rmax) & (obv.shift(1) < rmax.shift(1))
    fall_back = (obv < rmax)
    fail_recent = cross_up.shift(1).rolling(3, min_periods=1).max().fillna(False).astype(bool) & fall_back
    return fail_recent.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_441_obv_5d_minus_21d_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore((obv - obv.shift(WDAYS)) - (obv - obv.shift(MDAYS)), YDAYS)


def f22_obvd_442_obv_21d_minus_63d_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore((obv - obv.shift(MDAYS)) - (obv - obv.shift(QDAYS)), YDAYS)


def f22_obvd_443_obv_63d_minus_252d_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore((obv - obv.shift(QDAYS)) - (obv - obv.shift(YDAYS)), YDAYS)


def f22_obvd_444_obv_252d_minus_504d_z(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _rolling_zscore((obv - obv.shift(YDAYS)) - (obv - obv.shift(DDAYS_2Y)), DDAYS_2Y)


def f22_obvd_445_obv_long_short_alignment_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    z63 = _rolling_zscore(obv, QDAYS)
    z252 = _rolling_zscore(obv, YDAYS)
    return ((z63 > 1.0) & (z252 > 1.0)).astype(float)


def f22_obvd_446_obv_long_short_disagreement_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    z63 = _rolling_zscore(obv, QDAYS)
    z252 = _rolling_zscore(obv, YDAYS)
    return ((z63 > 1.0) & (z252 < 0)).astype(float)


def f22_obvd_447_obv_pct_change_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _safe_div(obv - obv.shift(WDAYS), obv.shift(WDAYS).abs() + 1.0)


def f22_obvd_448_obv_pct_change_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _safe_div(obv - obv.shift(MDAYS), obv.shift(MDAYS).abs() + 1.0)


def f22_obvd_449_obv_pct_change_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    return _safe_div(obv - obv.shift(QDAYS), obv.shift(QDAYS).abs() + 1.0)


def f22_obvd_450_obv_alpha_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    obv = _obv(close, volume)
    s_o = (obv - obv.shift(YDAYS)) / float(YDAYS)
    s_p = (_safe_log(close) - _safe_log(close).shift(YDAYS)) / float(YDAYS)
    return _safe_div(s_o, s_p)


def f22_obvd_376_obv_negative_momentum_streak_max_252d_d2(close, volume):
    return f22_obvd_376_obv_negative_momentum_streak_max_252d(close, volume).diff().diff()


def f22_obvd_377_obv_momentum_thrust_indicator_d2(close, volume):
    return f22_obvd_377_obv_momentum_thrust_indicator(close, volume).diff().diff()


def f22_obvd_378_obv_5d_change_zscore_252d_d2(close, volume):
    return f22_obvd_378_obv_5d_change_zscore_252d(close, volume).diff().diff()


def f22_obvd_379_obv_21d_change_zscore_252d_d2(close, volume):
    return f22_obvd_379_obv_21d_change_zscore_252d(close, volume).diff().diff()


def f22_obvd_380_obv_63d_change_zscore_252d_d2(close, volume):
    return f22_obvd_380_obv_63d_change_zscore_252d(close, volume).diff().diff()


def f22_obvd_381_obv_momentum_diff_5d_vs_21d_zscore_252d_d2(close, volume):
    return f22_obvd_381_obv_momentum_diff_5d_vs_21d_zscore_252d(close, volume).diff().diff()


def f22_obvd_382_obv_first_positive_change_after_negative_streak_indicator_d2(close, volume):
    return f22_obvd_382_obv_first_positive_change_after_negative_streak_indicator(close, volume).diff().diff()


def f22_obvd_383_obv_first_negative_change_after_positive_streak_indicator_d2(close, volume):
    return f22_obvd_383_obv_first_negative_change_after_positive_streak_indicator(close, volume).diff().diff()


def f22_obvd_384_obv_consecutive_negative_bars_count_252d_d2(close, volume):
    return f22_obvd_384_obv_consecutive_negative_bars_count_252d(close, volume).diff().diff()


def f22_obvd_385_obv_consecutive_positive_bars_count_252d_d2(close, volume):
    return f22_obvd_385_obv_consecutive_positive_bars_count_252d(close, volume).diff().diff()


def f22_obvd_386_down_to_up_vol_ratio_5d_d2(close, volume):
    return f22_obvd_386_down_to_up_vol_ratio_5d(close, volume).diff().diff()


def f22_obvd_387_down_to_up_vol_ratio_3d_d2(close, volume):
    return f22_obvd_387_down_to_up_vol_ratio_3d(close, volume).diff().diff()


def f22_obvd_388_down_vol_dominance_streak_252d_d2(close, volume):
    return f22_obvd_388_down_vol_dominance_streak_252d(close, volume).diff().diff()


def f22_obvd_389_up_to_down_vol_ratio_at_252d_high_5d_d2(high, close, volume):
    return f22_obvd_389_up_to_down_vol_ratio_at_252d_high_5d(high, close, volume).diff().diff()


def f22_obvd_390_up_to_down_vol_ratio_at_252d_high_21d_d2(high, close, volume):
    return f22_obvd_390_up_to_down_vol_ratio_at_252d_high_21d(high, close, volume).diff().diff()


def f22_obvd_391_max_consec_down_vol_dominant_252d_d2(close, volume):
    return f22_obvd_391_max_consec_down_vol_dominant_252d(close, volume).diff().diff()


def f22_obvd_392_max_consec_up_vol_dominant_252d_d2(close, volume):
    return f22_obvd_392_max_consec_up_vol_dominant_252d(close, volume).diff().diff()


def f22_obvd_393_net_volume_5d_zscore_252d_d2(close, volume):
    return f22_obvd_393_net_volume_5d_zscore_252d(close, volume).diff().diff()


def f22_obvd_394_net_volume_3d_zscore_252d_d2(close, volume):
    return f22_obvd_394_net_volume_3d_zscore_252d(close, volume).diff().diff()


def f22_obvd_395_net_volume_diff_5d_vs_21d_252d_d2(close, volume):
    return f22_obvd_395_net_volume_diff_5d_vs_21d_252d(close, volume).diff().diff()


def f22_obvd_396_signed_vol_skewness_5d_d2(close, volume):
    return f22_obvd_396_signed_vol_skewness_5d(close, volume).diff().diff()


def f22_obvd_397_signed_vol_max_5d_zscore_252d_d2(close, volume):
    return f22_obvd_397_signed_vol_max_5d_zscore_252d(close, volume).diff().diff()


def f22_obvd_398_signed_vol_min_5d_zscore_252d_d2(close, volume):
    return f22_obvd_398_signed_vol_min_5d_zscore_252d(close, volume).diff().diff()


def f22_obvd_399_cumulative_signed_vol_5d_z_252d_d2(close, volume):
    return f22_obvd_399_cumulative_signed_vol_5d_z_252d(close, volume).diff().diff()


def f22_obvd_400_cumulative_signed_vol_21d_z_252d_d2(close, volume):
    return f22_obvd_400_cumulative_signed_vol_21d_z_252d(close, volume).diff().diff()


def f22_obvd_401_obv_change_on_gap_fill_count_252d_d2(open, high, close, volume):
    return f22_obvd_401_obv_change_on_gap_fill_count_252d(open, high, close, volume).diff().diff()


def f22_obvd_402_obv_change_on_breakaway_gap_count_252d_d2(open, high, close, volume):
    return f22_obvd_402_obv_change_on_breakaway_gap_count_252d(open, high, close, volume).diff().diff()


def f22_obvd_403_obv_change_on_island_top_indicator_d2(open, high, low, close, volume):
    return f22_obvd_403_obv_change_on_island_top_indicator(open, high, low, close, volume).diff().diff()


def f22_obvd_404_obv_change_on_island_bottom_indicator_d2(open, high, low, close, volume):
    return f22_obvd_404_obv_change_on_island_bottom_indicator(open, high, low, close, volume).diff().diff()


def f22_obvd_405_obv_change_after_8day_consecutive_up_252d_d2(close, volume):
    return f22_obvd_405_obv_change_after_8day_consecutive_up_252d(close, volume).diff().diff()


def f22_obvd_406_obv_change_after_8day_consecutive_down_252d_d2(close, volume):
    return f22_obvd_406_obv_change_after_8day_consecutive_down_252d(close, volume).diff().diff()


def f22_obvd_407_obv_change_on_fib_retrace_38_indicator_d2(high, low, close, volume):
    return f22_obvd_407_obv_change_on_fib_retrace_38_indicator(high, low, close, volume).diff().diff()


def f22_obvd_408_obv_change_on_fib_retrace_50_indicator_d2(high, low, close, volume):
    return f22_obvd_408_obv_change_on_fib_retrace_50_indicator(high, low, close, volume).diff().diff()


def f22_obvd_409_obv_change_on_fib_retrace_61_indicator_d2(high, low, close, volume):
    return f22_obvd_409_obv_change_on_fib_retrace_61_indicator(high, low, close, volume).diff().diff()


def f22_obvd_410_obv_at_first_bar_below_21ema_after_high_d2(close, volume):
    return f22_obvd_410_obv_at_first_bar_below_21ema_after_high(close, volume).diff().diff()


def f22_obvd_411_obv_at_first_bar_above_21ema_after_low_d2(close, volume):
    return f22_obvd_411_obv_at_first_bar_above_21ema_after_low(close, volume).diff().diff()


def f22_obvd_412_obv_change_on_test_of_recent_low_count_252d_d2(low, close, volume):
    return f22_obvd_412_obv_change_on_test_of_recent_low_count_252d(low, close, volume).diff().diff()


def f22_obvd_413_obv_change_on_test_of_recent_high_count_252d_d2(high, close, volume):
    return f22_obvd_413_obv_change_on_test_of_recent_high_count_252d(high, close, volume).diff().diff()


def f22_obvd_414_obv_change_on_round_number_252d_d2(close, volume):
    return f22_obvd_414_obv_change_on_round_number_252d(close, volume).diff().diff()


def f22_obvd_415_obv_change_on_round_number_with_rejection_d2(high, low, close, volume):
    return f22_obvd_415_obv_change_on_round_number_with_rejection(high, low, close, volume).diff().diff()


def f22_obvd_416_obv_breakout_indicator_d2(close, volume):
    return f22_obvd_416_obv_breakout_indicator(close, volume).diff().diff()


def f22_obvd_417_obv_breakdown_indicator_d2(close, volume):
    return f22_obvd_417_obv_breakdown_indicator(close, volume).diff().diff()


def f22_obvd_418_obv_first_252d_high_after_drawdown_indicator_d2(close, volume):
    return f22_obvd_418_obv_first_252d_high_after_drawdown_indicator(close, volume).diff().diff()


def f22_obvd_419_obv_first_252d_low_after_rally_indicator_d2(close, volume):
    return f22_obvd_419_obv_first_252d_low_after_rally_indicator(close, volume).diff().diff()


def f22_obvd_420_obv_zigzag_count_252d_d2(close, volume):
    return f22_obvd_420_obv_zigzag_count_252d(close, volume).diff().diff()


def f22_obvd_421_obv_above_zero_indicator_d2(close, volume):
    return f22_obvd_421_obv_above_zero_indicator(close, volume).diff().diff()


def f22_obvd_422_obv_above_zero_dwell_252d_d2(close, volume):
    return f22_obvd_422_obv_above_zero_dwell_252d(close, volume).diff().diff()


def f22_obvd_423_obv_crossed_zero_recently_indicator_d2(close, volume):
    return f22_obvd_423_obv_crossed_zero_recently_indicator(close, volume).diff().diff()


def f22_obvd_424_obv_zero_cross_age_252d_d2(close, volume):
    return f22_obvd_424_obv_zero_cross_age_252d(close, volume).diff().diff()


def f22_obvd_425_obv_velocity_acceleration_252d_d2(close, volume):
    return f22_obvd_425_obv_velocity_acceleration_252d(close, volume).diff().diff()


def f22_obvd_426_obv_jerk_252d_d2(close, volume):
    return f22_obvd_426_obv_jerk_252d(close, volume).diff().diff()


def f22_obvd_427_obv_smoothness_index_252d_d2(close, volume):
    return f22_obvd_427_obv_smoothness_index_252d(close, volume).diff().diff()


def f22_obvd_428_obv_trend_clarity_index_252d_d2(close, volume):
    return f22_obvd_428_obv_trend_clarity_index_252d(close, volume).diff().diff()


def f22_obvd_429_obv_choppiness_index_252d_d2(close, volume):
    return f22_obvd_429_obv_choppiness_index_252d(close, volume).diff().diff()


def f22_obvd_430_obv_efficiency_ratio_252d_d2(close, volume):
    return f22_obvd_430_obv_efficiency_ratio_252d(close, volume).diff().diff()


def f22_obvd_431_obv_diff_when_close_new_252d_high_avg_252d_d2(high, close, volume):
    return f22_obvd_431_obv_diff_when_close_new_252d_high_avg_252d(high, close, volume).diff().diff()


def f22_obvd_432_obv_diff_when_close_new_5y_high_avg_d2(close, volume):
    return f22_obvd_432_obv_diff_when_close_new_5y_high_avg(close, volume).diff().diff()


def f22_obvd_433_obv_diff_at_alltime_high_avg_d2(close, volume):
    return f22_obvd_433_obv_diff_at_alltime_high_avg(close, volume).diff().diff()


def f22_obvd_434_obv_at_alltime_high_dwell_count_252d_d2(close, volume):
    return f22_obvd_434_obv_at_alltime_high_dwell_count_252d(close, volume).diff().diff()


def f22_obvd_435_obv_diff_zscore_at_alltime_high_mean_d2(close, volume):
    return f22_obvd_435_obv_diff_zscore_at_alltime_high_mean(close, volume).diff().diff()


def f22_obvd_436_obv_negative_during_uptrend_count_252d_d2(close, volume):
    return f22_obvd_436_obv_negative_during_uptrend_count_252d(close, volume).diff().diff()


def f22_obvd_437_obv_negative_during_uptrend_streak_252d_d2(close, volume):
    return f22_obvd_437_obv_negative_during_uptrend_streak_252d(close, volume).diff().diff()


def f22_obvd_438_obv_positive_during_downtrend_count_252d_d2(close, volume):
    return f22_obvd_438_obv_positive_during_downtrend_count_252d(close, volume).diff().diff()


def f22_obvd_439_obv_compound_topping_signal_simple_d2(high, close, volume):
    return f22_obvd_439_obv_compound_topping_signal_simple(high, close, volume).diff().diff()


def f22_obvd_440_obv_breakout_failure_within_3d_count_252d_d2(close, volume):
    return f22_obvd_440_obv_breakout_failure_within_3d_count_252d(close, volume).diff().diff()


def f22_obvd_441_obv_5d_minus_21d_z_252d_d2(close, volume):
    return f22_obvd_441_obv_5d_minus_21d_z_252d(close, volume).diff().diff()


def f22_obvd_442_obv_21d_minus_63d_z_252d_d2(close, volume):
    return f22_obvd_442_obv_21d_minus_63d_z_252d(close, volume).diff().diff()


def f22_obvd_443_obv_63d_minus_252d_z_252d_d2(close, volume):
    return f22_obvd_443_obv_63d_minus_252d_z_252d(close, volume).diff().diff()


def f22_obvd_444_obv_252d_minus_504d_z_d2(close, volume):
    return f22_obvd_444_obv_252d_minus_504d_z(close, volume).diff().diff()


def f22_obvd_445_obv_long_short_alignment_indicator_d2(close, volume):
    return f22_obvd_445_obv_long_short_alignment_indicator(close, volume).diff().diff()


def f22_obvd_446_obv_long_short_disagreement_indicator_d2(close, volume):
    return f22_obvd_446_obv_long_short_disagreement_indicator(close, volume).diff().diff()


def f22_obvd_447_obv_pct_change_5d_d2(close, volume):
    return f22_obvd_447_obv_pct_change_5d(close, volume).diff().diff()


def f22_obvd_448_obv_pct_change_21d_d2(close, volume):
    return f22_obvd_448_obv_pct_change_21d(close, volume).diff().diff()


def f22_obvd_449_obv_pct_change_63d_d2(close, volume):
    return f22_obvd_449_obv_pct_change_63d(close, volume).diff().diff()


def f22_obvd_450_obv_alpha_ratio_252d_d2(close, volume):
    return f22_obvd_450_obv_alpha_ratio_252d(close, volume).diff().diff()


ON_BALANCE_VOLUME_DYNAMICS_D2_REGISTRY_376_450 = {
    "f22_obvd_376_obv_negative_momentum_streak_max_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_376_obv_negative_momentum_streak_max_252d_d2},
    "f22_obvd_377_obv_momentum_thrust_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_377_obv_momentum_thrust_indicator_d2},
    "f22_obvd_378_obv_5d_change_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_378_obv_5d_change_zscore_252d_d2},
    "f22_obvd_379_obv_21d_change_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_379_obv_21d_change_zscore_252d_d2},
    "f22_obvd_380_obv_63d_change_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_380_obv_63d_change_zscore_252d_d2},
    "f22_obvd_381_obv_momentum_diff_5d_vs_21d_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_381_obv_momentum_diff_5d_vs_21d_zscore_252d_d2},
    "f22_obvd_382_obv_first_positive_change_after_negative_streak_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_382_obv_first_positive_change_after_negative_streak_indicator_d2},
    "f22_obvd_383_obv_first_negative_change_after_positive_streak_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_383_obv_first_negative_change_after_positive_streak_indicator_d2},
    "f22_obvd_384_obv_consecutive_negative_bars_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_384_obv_consecutive_negative_bars_count_252d_d2},
    "f22_obvd_385_obv_consecutive_positive_bars_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_385_obv_consecutive_positive_bars_count_252d_d2},
    "f22_obvd_386_down_to_up_vol_ratio_5d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_386_down_to_up_vol_ratio_5d_d2},
    "f22_obvd_387_down_to_up_vol_ratio_3d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_387_down_to_up_vol_ratio_3d_d2},
    "f22_obvd_388_down_vol_dominance_streak_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_388_down_vol_dominance_streak_252d_d2},
    "f22_obvd_389_up_to_down_vol_ratio_at_252d_high_5d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_389_up_to_down_vol_ratio_at_252d_high_5d_d2},
    "f22_obvd_390_up_to_down_vol_ratio_at_252d_high_21d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_390_up_to_down_vol_ratio_at_252d_high_21d_d2},
    "f22_obvd_391_max_consec_down_vol_dominant_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_391_max_consec_down_vol_dominant_252d_d2},
    "f22_obvd_392_max_consec_up_vol_dominant_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_392_max_consec_up_vol_dominant_252d_d2},
    "f22_obvd_393_net_volume_5d_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_393_net_volume_5d_zscore_252d_d2},
    "f22_obvd_394_net_volume_3d_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_394_net_volume_3d_zscore_252d_d2},
    "f22_obvd_395_net_volume_diff_5d_vs_21d_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_395_net_volume_diff_5d_vs_21d_252d_d2},
    "f22_obvd_396_signed_vol_skewness_5d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_396_signed_vol_skewness_5d_d2},
    "f22_obvd_397_signed_vol_max_5d_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_397_signed_vol_max_5d_zscore_252d_d2},
    "f22_obvd_398_signed_vol_min_5d_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_398_signed_vol_min_5d_zscore_252d_d2},
    "f22_obvd_399_cumulative_signed_vol_5d_z_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_399_cumulative_signed_vol_5d_z_252d_d2},
    "f22_obvd_400_cumulative_signed_vol_21d_z_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_400_cumulative_signed_vol_21d_z_252d_d2},
    "f22_obvd_401_obv_change_on_gap_fill_count_252d_d2": {"inputs": ["open", "high", "close", "volume"], "func": f22_obvd_401_obv_change_on_gap_fill_count_252d_d2},
    "f22_obvd_402_obv_change_on_breakaway_gap_count_252d_d2": {"inputs": ["open", "high", "close", "volume"], "func": f22_obvd_402_obv_change_on_breakaway_gap_count_252d_d2},
    "f22_obvd_403_obv_change_on_island_top_indicator_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f22_obvd_403_obv_change_on_island_top_indicator_d2},
    "f22_obvd_404_obv_change_on_island_bottom_indicator_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f22_obvd_404_obv_change_on_island_bottom_indicator_d2},
    "f22_obvd_405_obv_change_after_8day_consecutive_up_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_405_obv_change_after_8day_consecutive_up_252d_d2},
    "f22_obvd_406_obv_change_after_8day_consecutive_down_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_406_obv_change_after_8day_consecutive_down_252d_d2},
    "f22_obvd_407_obv_change_on_fib_retrace_38_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_407_obv_change_on_fib_retrace_38_indicator_d2},
    "f22_obvd_408_obv_change_on_fib_retrace_50_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_408_obv_change_on_fib_retrace_50_indicator_d2},
    "f22_obvd_409_obv_change_on_fib_retrace_61_indicator_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_409_obv_change_on_fib_retrace_61_indicator_d2},
    "f22_obvd_410_obv_at_first_bar_below_21ema_after_high_d2": {"inputs": ["close", "volume"], "func": f22_obvd_410_obv_at_first_bar_below_21ema_after_high_d2},
    "f22_obvd_411_obv_at_first_bar_above_21ema_after_low_d2": {"inputs": ["close", "volume"], "func": f22_obvd_411_obv_at_first_bar_above_21ema_after_low_d2},
    "f22_obvd_412_obv_change_on_test_of_recent_low_count_252d_d2": {"inputs": ["low", "close", "volume"], "func": f22_obvd_412_obv_change_on_test_of_recent_low_count_252d_d2},
    "f22_obvd_413_obv_change_on_test_of_recent_high_count_252d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_413_obv_change_on_test_of_recent_high_count_252d_d2},
    "f22_obvd_414_obv_change_on_round_number_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_414_obv_change_on_round_number_252d_d2},
    "f22_obvd_415_obv_change_on_round_number_with_rejection_d2": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_415_obv_change_on_round_number_with_rejection_d2},
    "f22_obvd_416_obv_breakout_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_416_obv_breakout_indicator_d2},
    "f22_obvd_417_obv_breakdown_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_417_obv_breakdown_indicator_d2},
    "f22_obvd_418_obv_first_252d_high_after_drawdown_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_418_obv_first_252d_high_after_drawdown_indicator_d2},
    "f22_obvd_419_obv_first_252d_low_after_rally_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_419_obv_first_252d_low_after_rally_indicator_d2},
    "f22_obvd_420_obv_zigzag_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_420_obv_zigzag_count_252d_d2},
    "f22_obvd_421_obv_above_zero_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_421_obv_above_zero_indicator_d2},
    "f22_obvd_422_obv_above_zero_dwell_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_422_obv_above_zero_dwell_252d_d2},
    "f22_obvd_423_obv_crossed_zero_recently_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_423_obv_crossed_zero_recently_indicator_d2},
    "f22_obvd_424_obv_zero_cross_age_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_424_obv_zero_cross_age_252d_d2},
    "f22_obvd_425_obv_velocity_acceleration_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_425_obv_velocity_acceleration_252d_d2},
    "f22_obvd_426_obv_jerk_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_426_obv_jerk_252d_d2},
    "f22_obvd_427_obv_smoothness_index_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_427_obv_smoothness_index_252d_d2},
    "f22_obvd_428_obv_trend_clarity_index_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_428_obv_trend_clarity_index_252d_d2},
    "f22_obvd_429_obv_choppiness_index_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_429_obv_choppiness_index_252d_d2},
    "f22_obvd_430_obv_efficiency_ratio_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_430_obv_efficiency_ratio_252d_d2},
    "f22_obvd_431_obv_diff_when_close_new_252d_high_avg_252d_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_431_obv_diff_when_close_new_252d_high_avg_252d_d2},
    "f22_obvd_432_obv_diff_when_close_new_5y_high_avg_d2": {"inputs": ["close", "volume"], "func": f22_obvd_432_obv_diff_when_close_new_5y_high_avg_d2},
    "f22_obvd_433_obv_diff_at_alltime_high_avg_d2": {"inputs": ["close", "volume"], "func": f22_obvd_433_obv_diff_at_alltime_high_avg_d2},
    "f22_obvd_434_obv_at_alltime_high_dwell_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_434_obv_at_alltime_high_dwell_count_252d_d2},
    "f22_obvd_435_obv_diff_zscore_at_alltime_high_mean_d2": {"inputs": ["close", "volume"], "func": f22_obvd_435_obv_diff_zscore_at_alltime_high_mean_d2},
    "f22_obvd_436_obv_negative_during_uptrend_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_436_obv_negative_during_uptrend_count_252d_d2},
    "f22_obvd_437_obv_negative_during_uptrend_streak_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_437_obv_negative_during_uptrend_streak_252d_d2},
    "f22_obvd_438_obv_positive_during_downtrend_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_438_obv_positive_during_downtrend_count_252d_d2},
    "f22_obvd_439_obv_compound_topping_signal_simple_d2": {"inputs": ["high", "close", "volume"], "func": f22_obvd_439_obv_compound_topping_signal_simple_d2},
    "f22_obvd_440_obv_breakout_failure_within_3d_count_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_440_obv_breakout_failure_within_3d_count_252d_d2},
    "f22_obvd_441_obv_5d_minus_21d_z_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_441_obv_5d_minus_21d_z_252d_d2},
    "f22_obvd_442_obv_21d_minus_63d_z_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_442_obv_21d_minus_63d_z_252d_d2},
    "f22_obvd_443_obv_63d_minus_252d_z_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_443_obv_63d_minus_252d_z_252d_d2},
    "f22_obvd_444_obv_252d_minus_504d_z_d2": {"inputs": ["close", "volume"], "func": f22_obvd_444_obv_252d_minus_504d_z_d2},
    "f22_obvd_445_obv_long_short_alignment_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_445_obv_long_short_alignment_indicator_d2},
    "f22_obvd_446_obv_long_short_disagreement_indicator_d2": {"inputs": ["close", "volume"], "func": f22_obvd_446_obv_long_short_disagreement_indicator_d2},
    "f22_obvd_447_obv_pct_change_5d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_447_obv_pct_change_5d_d2},
    "f22_obvd_448_obv_pct_change_21d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_448_obv_pct_change_21d_d2},
    "f22_obvd_449_obv_pct_change_63d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_449_obv_pct_change_63d_d2},
    "f22_obvd_450_obv_alpha_ratio_252d_d2": {"inputs": ["close", "volume"], "func": f22_obvd_450_obv_alpha_ratio_252d_d2},
}
