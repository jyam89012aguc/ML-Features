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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _consecutive_true_streak(b):
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _dollar_vol(close, volume):
    return (close * volume).astype(float)


def _safe_dow(idx, target):
    if isinstance(idx, pd.DatetimeIndex):
        return pd.Series((idx.dayofweek == target).astype(float), index=idx)
    return pd.Series(np.nan, index=idx)


def f21_dvit_301_dv_zscore_on_doji_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(body < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_302_dv_zscore_on_engulfing_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    engulf = (high > high.shift(1)) & (low < low.shift(1)) & (close < close.shift(1))
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(engulf, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_303_dv_zscore_on_pin_bar_at_high_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    lower_wick = (pd.concat([close, close.shift(1)], axis=1).min(axis=1) - low) / rng
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pin = (body < 0.3) & (lower_wick > 0.5) & (high >= rmax)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(pin, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_304_dv_on_inside_day_below_med_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    inside = (high < high.shift(1)) & (low > low.shift(1))
    dv = _dollar_vol(close, volume)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    return (inside & (dv < med)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_305_dv_on_outside_day_above_med_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    outside = (high > high.shift(1)) & (low < low.shift(1))
    dv = _dollar_vol(close, volume)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    return (outside & (dv > med)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_306_dv_on_marubozu_up_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    up = close > close.shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((body > 0.8) & up & (z > 1.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_307_dv_on_marubozu_down_count_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    dn = close < close.shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((body > 0.8) & dn & (z > 1.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_308_dv_on_hammer_bars_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    body = (close - close.shift(1)).abs()
    lower_wick = pd.concat([close, close.shift(1)], axis=1).min(axis=1) - low
    hammer = (pos >= 0.67) & (lower_wick > 2.0 * body)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(hammer, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_309_dv_on_shooting_star_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = _safe_div(close - low, high - low)
    body = (close - close.shift(1)).abs()
    upper_wick = high - pd.concat([close, close.shift(1)], axis=1).max(axis=1)
    star = (pos <= 0.33) & (upper_wick > 2.0 * body)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(star, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_310_dv_concentration_on_outside_days_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    outside = (high > high.shift(1)) & (low < low.shift(1))
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(outside, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), dv.rolling(YDAYS, min_periods=QDAYS).sum())


def f21_dvit_311_dv_on_3_consec_up_bars_avg_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    three_up = up & up.shift(1) & up.shift(2)
    dv = _dollar_vol(close, volume)
    return dv.where(three_up, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_312_dv_on_3_consec_down_bars_avg_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dn = close < close.shift(1)
    three_dn = dn & dn.shift(1) & dn.shift(2)
    dv = _dollar_vol(close, volume)
    return dv.where(three_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_313_dv_on_gap_up_bars_mean_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_up = open > 1.005 * close.shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(gap_up, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_314_dv_on_gap_down_bars_mean_252d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    gap_dn = open < 0.995 * close.shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(gap_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_315_dv_on_widest_range_5_bars_252d_share(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rng = high - low
    def _sh(idx):
        r = rng.iloc[idx]; v = _dollar_vol(close.iloc[idx], volume.iloc[idx])
        if v.notna().sum() < 30 or v.sum() <= 0:
            return np.nan
        top5_idx = r.nlargest(5).index
        return float(v.loc[top5_idx].sum() / v.sum())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _sh(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_316_dv_mean_monday_to_overall_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_d = _safe_dow(close.index, 0)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_317_dv_mean_tuesday_to_overall_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_d = _safe_dow(close.index, 1)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_318_dv_mean_wednesday_to_overall_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_d = _safe_dow(close.index, 2)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_319_dv_mean_thursday_to_overall_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_d = _safe_dow(close.index, 3)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_320_dv_mean_friday_to_overall_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_d = _safe_dow(close.index, 4)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_d == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_321_dv_mean_first_5_days_of_month_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    if isinstance(close.index, pd.DatetimeIndex):
        is_first = pd.Series(close.index.day <= 5, index=close.index).astype(float)
    else:
        is_first = pd.Series(np.nan, index=close.index)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_first == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_322_dv_mean_last_5_days_of_month_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    if isinstance(close.index, pd.DatetimeIndex):
        is_last = pd.Series(close.index.day >= 25, index=close.index).astype(float)
    else:
        is_last = pd.Series(np.nan, index=close.index)
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.where(is_last == 1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean(), dv.rolling(YDAYS, min_periods=QDAYS).mean())


def f21_dvit_323_dv_quarter_end_5_days_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    if isinstance(close.index, pd.DatetimeIndex):
        is_qe = pd.Series((close.index.month.isin([3, 6, 9, 12])) & (close.index.day >= 25), index=close.index).astype(float)
    else:
        is_qe = pd.Series(np.nan, index=close.index)
    dv = _dollar_vol(close, volume)
    qe_dv = dv.where(is_qe == 1.0, np.nan)
    z = (dv - qe_dv.rolling(YDAYS, min_periods=QDAYS).mean()) / qe_dv.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    return z.where(is_qe == 1.0, np.nan)


def f21_dvit_324_dv_year_end_indicator_5_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    if isinstance(close.index, pd.DatetimeIndex):
        is_ye = pd.Series((close.index.month == 12) & (close.index.day >= 24), index=close.index).astype(float)
    else:
        is_ye = pd.Series(np.nan, index=close.index)
    dv = _dollar_vol(close, volume)
    ye_dv = dv.where(is_ye == 1.0, np.nan)
    z = (dv - ye_dv.rolling(YDAYS, min_periods=QDAYS).mean()) / ye_dv.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    return z.where(is_ye == 1.0, np.nan)


def f21_dvit_325_dv_spike_count_friday_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_fri = _safe_dow(close.index, 4)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((is_fri == 1.0) & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_326_dv_on_new_252d_high_minus_dv_on_close_below_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmean = close.rolling(YDAYS, min_periods=QDAYS).mean()
    dv = _dollar_vol(close, volume)
    a = dv.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    b = dv.where(close < rmean, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return a - b


def f21_dvit_327_dv_spike_at_round_number_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    near = pd.Series((close / 5.0 - (close / 5.0).round()).abs() <= 0.20, index=close.index)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (near & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_328_dv_spike_at_round_10_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    near = pd.Series((close / 10.0 - (close / 10.0).round()).abs() <= 0.10, index=close.index)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (near & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_329_dv_at_top_of_range_in_top_5pct_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    q95c = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return z.where(close >= q95c, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_330_dv_concentration_on_top_5_close_bars_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(idx):
        c = close.iloc[idx]; v = dv.iloc[idx]
        if c.notna().sum() < 30 or v.sum() <= 0:
            return np.nan
        top5_idx = c.nlargest(5).index
        return float(v.loc[top5_idx].sum() / v.sum())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_331_dv_concentration_on_bottom_5_close_bars_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(idx):
        c = close.iloc[idx]; v = dv.iloc[idx]
        if c.notna().sum() < 30 or v.sum() <= 0:
            return np.nan
        bot5_idx = c.nsmallest(5).index
        return float(v.loc[bot5_idx].sum() / v.sum())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_332_dv_ratio_top5_to_bot5_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(idx):
        c = close.iloc[idx]; v = dv.iloc[idx]
        if c.notna().sum() < 30:
            return np.nan
        top5 = c.nlargest(5).index
        bot5 = c.nsmallest(5).index
        bot_sum = float(v.loc[bot5].sum())
        if bot_sum <= 0:
            return np.nan
        return float(v.loc[top5].sum() / bot_sum)
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(range(i - YDAYS + 1, i + 1))
    return out


def f21_dvit_333_dv_at_3_white_soldiers_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    three_up = up & up.shift(1) & up.shift(2)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (three_up & (z > 1.0)).astype(float)


def f21_dvit_334_dv_at_3_black_crows_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dn = close < close.shift(1)
    three_dn = dn & dn.shift(1) & dn.shift(2)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (three_dn & (z > 1.0)).astype(float)


def f21_dvit_335_dv_at_breakout_above_252d_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cmax = close.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close > cmax) & (z > 2.0)).astype(float)


def f21_dvit_336_dv_at_breakout_above_252d_high_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    cmax = close.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close > cmax) & (z > 2.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_337_dv_at_breakdown_below_21d_low_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    lmin = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close < lmin) & (z > 1.0)).astype(float)


def f21_dvit_338_dv_on_first_close_below_21ema_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema21 = close.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    above = close > ema21
    streak_above_yest = _consecutive_true_streak(above.shift(1).fillna(False)).astype(float)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    first_below = (~above) & (streak_above_yest >= MDAYS)
    return (first_below & (z > 0)).astype(float)


def f21_dvit_339_dv_on_first_close_below_63ema_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema63 = close.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    above = close > ema63
    streak_above_yest = _consecutive_true_streak(above.shift(1).fillna(False)).astype(float)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    first_below = (~above) & (streak_above_yest >= MDAYS)
    return (first_below & (z > 0)).astype(float)


def f21_dvit_340_dv_on_first_close_below_252ema_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema252 = close.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()
    above = close > ema252
    streak_above_yest = _consecutive_true_streak(above.shift(1).fillna(False)).astype(float)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    first_below = (~above) & (streak_above_yest >= QDAYS)
    return (first_below & (z > 0)).astype(float)


def f21_dvit_341_dv_above_5_sigma_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 5.0).astype(float)


def f21_dvit_342_dv_above_4_sigma_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 4.0).astype(float)


def f21_dvit_343_dv_above_5_sigma_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 5.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_344_dv_below_neg2_sigma_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z < -2.0).astype(float)


def f21_dvit_345_dv_below_neg3_sigma_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z < -3.0).astype(float)


def f21_dvit_346_dv_below_neg2_sigma_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z < -2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_347_dv_extreme_high_then_extreme_low_within_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    recent_burst = (z.shift(1).rolling(WDAYS, min_periods=1).max() > 3.0)
    return ((z < -2.0) & recent_burst).astype(float)


def f21_dvit_348_dv_extreme_high_followed_by_3_silent_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst = (z > 3.0)
    silent = z < -0.5
    silent3 = silent & silent.shift(1) & silent.shift(2)
    return (burst.shift(3) & silent3).astype(float)


def f21_dvit_349_dv_max_252d_age_recent_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _age(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmax(w)))
    age = dv.rolling(YDAYS, min_periods=QDAYS).apply(_age, raw=True)
    return (age <= 5).astype(float)


def f21_dvit_350_dv_max_252d_age_recent_21d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _age(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float(len(w) - 1 - int(np.argmax(w)))
    age = dv.rolling(YDAYS, min_periods=QDAYS).apply(_age, raw=True)
    return (age <= MDAYS).astype(float)


def f21_dvit_351_dv_top_5_days_in_last_21d_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(idx):
        v = dv.iloc[idx].dropna()
        if v.size < 30:
            return np.nan
        top5 = v.nlargest(5).index
        recent_idx = dv.index[idx[-MDAYS:]]
        return float(sum(1 for ti in top5 if ti in recent_idx))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(list(range(i - YDAYS + 1, i + 1)))
    return out


def f21_dvit_352_dv_top_10_days_in_last_21d_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(idx):
        v = dv.iloc[idx].dropna()
        if v.size < 30:
            return np.nan
        top10 = v.nlargest(10).index
        recent_idx = dv.index[idx[-MDAYS:]]
        return float(sum(1 for ti in top10 if ti in recent_idx))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(list(range(i - YDAYS + 1, i + 1)))
    return out


def f21_dvit_353_dv_top_5_days_in_last_5d_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(idx):
        v = dv.iloc[idx].dropna()
        if v.size < 30:
            return np.nan
        top5 = v.nlargest(5).index
        recent_idx = dv.index[idx[-WDAYS:]]
        return float(sum(1 for ti in top5 if ti in recent_idx))
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _f(list(range(i - YDAYS + 1, i + 1)))
    return out


def f21_dvit_354_dv_top_concentration_in_last_5d_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(WDAYS, min_periods=2).sum(), dv.rolling(YDAYS, min_periods=QDAYS).sum())


def f21_dvit_355_dv_top_concentration_in_last_21d_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(MDAYS, min_periods=WDAYS).sum(), dv.rolling(YDAYS, min_periods=QDAYS).sum())


def f21_dvit_356_dv_increasing_5_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return ((dv > dv.shift(1)) & (dv.shift(1) > dv.shift(2)) & (dv.shift(2) > dv.shift(3)) & (dv.shift(3) > dv.shift(4))).astype(float)


def f21_dvit_357_dv_decreasing_5_days_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return ((dv < dv.shift(1)) & (dv.shift(1) < dv.shift(2)) & (dv.shift(2) < dv.shift(3)) & (dv.shift(3) < dv.shift(4))).astype(float)


def f21_dvit_358_dv_double_burst_within_21d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    cnt = (z > 3.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return (cnt >= 2).astype(float)


def f21_dvit_359_dv_triple_burst_within_63d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    cnt = (z > 3.0).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt >= 3).astype(float)


def f21_dvit_360_dv_burst_followed_by_lower_burst_within_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    today_burst = z > 3.0
    higher_recent = (z.shift(1).rolling(WDAYS - 1, min_periods=1).max() > z)
    return (today_burst & higher_recent).astype(float)


def f21_dvit_361_dv_first_burst_above_median_in_252d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    today_burst = z > 2.0
    no_recent = (z.shift(1).rolling(MDAYS, min_periods=WDAYS).max() <= 2.0)
    return (today_burst & no_recent).astype(float)


def f21_dvit_362_dv_burst_after_long_silence_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    today_burst = z > 3.0
    no_recent = (z.shift(1).rolling(MDAYS, min_periods=WDAYS).max() <= 1.0)
    return (today_burst & no_recent).astype(float)


def f21_dvit_363_dv_climax_burst_signature(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    dvmax = dv.rolling(YDAYS, min_periods=QDAYS).max()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((dv >= dvmax) & (high >= rmax)).astype(float)


def f21_dvit_364_dv_post_climax_5d_drop_pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    def _f(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        peak_idx = int(np.argmax(w))
        if (len(w) - 1 - peak_idx) != 5:
            return np.nan
        peak = w[peak_idx]
        cur = w[-1]
        if not np.isfinite(peak) or peak <= 0 or not np.isfinite(cur):
            return np.nan
        return float(cur / peak - 1.0)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_f, raw=True)


def f21_dvit_365_dv_consecutive_decline_after_burst_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    burst_recent = (z.shift(1).rolling(MDAYS, min_periods=1).max() > 3.0)
    dv = _dollar_vol(close, volume)
    dv_dec = dv < dv.shift(1)
    cond = burst_recent & dv_dec
    return _consecutive_true_streak(cond).astype(float)


def f21_dvit_366_dv_5d_chg_pos_close_5d_chg_neg_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return ((dv.diff(WDAYS) > 0) & (close.diff(WDAYS) < 0)).astype(float)


def f21_dvit_367_dv_5d_chg_neg_close_5d_chg_pos_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return ((dv.diff(WDAYS) < 0) & (close.diff(WDAYS) > 0)).astype(float)


def f21_dvit_368_dv_21d_chg_pos_close_21d_chg_neg_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return ((dv.diff(MDAYS) > 0) & (close.diff(MDAYS) < 0)).astype(float)


def f21_dvit_369_dv_21d_chg_neg_close_21d_chg_pos_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    return ((dv.diff(MDAYS) < 0) & (close.diff(MDAYS) > 0)).astype(float)


def f21_dvit_370_dv_lower_high_with_higher_price_high_252d_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    p_hh = high.rolling(MDAYS, min_periods=WDAYS).max() > high.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    d_lh = dv.rolling(MDAYS, min_periods=WDAYS).max() < dv.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    return (p_hh & d_lh).astype(float)


def f21_dvit_371_dv_lower_low_with_higher_price_low_252d_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    p_hl = low.rolling(MDAYS, min_periods=WDAYS).min() > low.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS)
    d_ll = dv.rolling(MDAYS, min_periods=WDAYS).min() < dv.rolling(MDAYS, min_periods=WDAYS).min().shift(MDAYS)
    return (p_hl & d_ll).astype(float)


def f21_dvit_372_dv_divergence_at_252d_high_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    p_hh = high.rolling(MDAYS, min_periods=WDAYS).max() > high.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    d_lh = dv.rolling(MDAYS, min_periods=WDAYS).max() < dv.rolling(MDAYS, min_periods=WDAYS).max().shift(MDAYS)
    return (p_hh & d_lh).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_373_dv_divergence_severity_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = _dollar_vol(close, volume)
    pr_p = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    pr_d = dv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    diff = pr_p - pr_d
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return diff.where(high >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_374_dv_failure_to_confirm_breakout_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cmax = close.rolling(YDAYS, min_periods=QDAYS).max().shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close > cmax) & (z < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_375_dv_confirms_breakdown_count_252d(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    lmin = low.rolling(MDAYS, min_periods=WDAYS).min().shift(1)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close < lmin) & (z > 1.0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_301_dv_zscore_on_doji_bars_252d_d2(high, low, close, volume):
    return f21_dvit_301_dv_zscore_on_doji_bars_252d(high, low, close, volume).diff().diff()


def f21_dvit_302_dv_zscore_on_engulfing_bars_252d_d2(high, low, close, volume):
    return f21_dvit_302_dv_zscore_on_engulfing_bars_252d(high, low, close, volume).diff().diff()


def f21_dvit_303_dv_zscore_on_pin_bar_at_high_252d_d2(high, low, close, volume):
    return f21_dvit_303_dv_zscore_on_pin_bar_at_high_252d(high, low, close, volume).diff().diff()


def f21_dvit_304_dv_on_inside_day_below_med_count_63d_d2(high, low, close, volume):
    return f21_dvit_304_dv_on_inside_day_below_med_count_63d(high, low, close, volume).diff().diff()


def f21_dvit_305_dv_on_outside_day_above_med_count_63d_d2(high, low, close, volume):
    return f21_dvit_305_dv_on_outside_day_above_med_count_63d(high, low, close, volume).diff().diff()


def f21_dvit_306_dv_on_marubozu_up_count_252d_d2(high, low, close, volume):
    return f21_dvit_306_dv_on_marubozu_up_count_252d(high, low, close, volume).diff().diff()


def f21_dvit_307_dv_on_marubozu_down_count_252d_d2(high, low, close, volume):
    return f21_dvit_307_dv_on_marubozu_down_count_252d(high, low, close, volume).diff().diff()


def f21_dvit_308_dv_on_hammer_bars_252d_d2(high, low, close, volume):
    return f21_dvit_308_dv_on_hammer_bars_252d(high, low, close, volume).diff().diff()


def f21_dvit_309_dv_on_shooting_star_252d_d2(high, low, close, volume):
    return f21_dvit_309_dv_on_shooting_star_252d(high, low, close, volume).diff().diff()


def f21_dvit_310_dv_concentration_on_outside_days_252d_d2(high, low, close, volume):
    return f21_dvit_310_dv_concentration_on_outside_days_252d(high, low, close, volume).diff().diff()


def f21_dvit_311_dv_on_3_consec_up_bars_avg_252d_d2(close, volume):
    return f21_dvit_311_dv_on_3_consec_up_bars_avg_252d(close, volume).diff().diff()


def f21_dvit_312_dv_on_3_consec_down_bars_avg_252d_d2(close, volume):
    return f21_dvit_312_dv_on_3_consec_down_bars_avg_252d(close, volume).diff().diff()


def f21_dvit_313_dv_on_gap_up_bars_mean_252d_d2(open, close, volume):
    return f21_dvit_313_dv_on_gap_up_bars_mean_252d(open, close, volume).diff().diff()


def f21_dvit_314_dv_on_gap_down_bars_mean_252d_d2(open, close, volume):
    return f21_dvit_314_dv_on_gap_down_bars_mean_252d(open, close, volume).diff().diff()


def f21_dvit_315_dv_on_widest_range_5_bars_252d_share_d2(high, low, close, volume):
    return f21_dvit_315_dv_on_widest_range_5_bars_252d_share(high, low, close, volume).diff().diff()


def f21_dvit_316_dv_mean_monday_to_overall_252d_d2(close, volume):
    return f21_dvit_316_dv_mean_monday_to_overall_252d(close, volume).diff().diff()


def f21_dvit_317_dv_mean_tuesday_to_overall_252d_d2(close, volume):
    return f21_dvit_317_dv_mean_tuesday_to_overall_252d(close, volume).diff().diff()


def f21_dvit_318_dv_mean_wednesday_to_overall_252d_d2(close, volume):
    return f21_dvit_318_dv_mean_wednesday_to_overall_252d(close, volume).diff().diff()


def f21_dvit_319_dv_mean_thursday_to_overall_252d_d2(close, volume):
    return f21_dvit_319_dv_mean_thursday_to_overall_252d(close, volume).diff().diff()


def f21_dvit_320_dv_mean_friday_to_overall_252d_d2(close, volume):
    return f21_dvit_320_dv_mean_friday_to_overall_252d(close, volume).diff().diff()


def f21_dvit_321_dv_mean_first_5_days_of_month_252d_d2(close, volume):
    return f21_dvit_321_dv_mean_first_5_days_of_month_252d(close, volume).diff().diff()


def f21_dvit_322_dv_mean_last_5_days_of_month_252d_d2(close, volume):
    return f21_dvit_322_dv_mean_last_5_days_of_month_252d(close, volume).diff().diff()


def f21_dvit_323_dv_quarter_end_5_days_zscore_252d_d2(close, volume):
    return f21_dvit_323_dv_quarter_end_5_days_zscore_252d(close, volume).diff().diff()


def f21_dvit_324_dv_year_end_indicator_5_days_d2(close, volume):
    return f21_dvit_324_dv_year_end_indicator_5_days(close, volume).diff().diff()


def f21_dvit_325_dv_spike_count_friday_252d_d2(close, volume):
    return f21_dvit_325_dv_spike_count_friday_252d(close, volume).diff().diff()


def f21_dvit_326_dv_on_new_252d_high_minus_dv_on_close_below_252d_d2(high, close, volume):
    return f21_dvit_326_dv_on_new_252d_high_minus_dv_on_close_below_252d(high, close, volume).diff().diff()


def f21_dvit_327_dv_spike_at_round_number_count_252d_d2(close, volume):
    return f21_dvit_327_dv_spike_at_round_number_count_252d(close, volume).diff().diff()


def f21_dvit_328_dv_spike_at_round_10_count_252d_d2(close, volume):
    return f21_dvit_328_dv_spike_at_round_10_count_252d(close, volume).diff().diff()


def f21_dvit_329_dv_at_top_of_range_in_top_5pct_close_252d_d2(close, volume):
    return f21_dvit_329_dv_at_top_of_range_in_top_5pct_close_252d(close, volume).diff().diff()


def f21_dvit_330_dv_concentration_on_top_5_close_bars_252d_d2(close, volume):
    return f21_dvit_330_dv_concentration_on_top_5_close_bars_252d(close, volume).diff().diff()


def f21_dvit_331_dv_concentration_on_bottom_5_close_bars_252d_d2(close, volume):
    return f21_dvit_331_dv_concentration_on_bottom_5_close_bars_252d(close, volume).diff().diff()


def f21_dvit_332_dv_ratio_top5_to_bot5_close_252d_d2(close, volume):
    return f21_dvit_332_dv_ratio_top5_to_bot5_close_252d(close, volume).diff().diff()


def f21_dvit_333_dv_at_3_white_soldiers_indicator_d2(close, volume):
    return f21_dvit_333_dv_at_3_white_soldiers_indicator(close, volume).diff().diff()


def f21_dvit_334_dv_at_3_black_crows_indicator_d2(close, volume):
    return f21_dvit_334_dv_at_3_black_crows_indicator(close, volume).diff().diff()


def f21_dvit_335_dv_at_breakout_above_252d_high_indicator_d2(high, close, volume):
    return f21_dvit_335_dv_at_breakout_above_252d_high_indicator(high, close, volume).diff().diff()


def f21_dvit_336_dv_at_breakout_above_252d_high_count_252d_d2(close, volume):
    return f21_dvit_336_dv_at_breakout_above_252d_high_count_252d(close, volume).diff().diff()


def f21_dvit_337_dv_at_breakdown_below_21d_low_indicator_d2(low, close, volume):
    return f21_dvit_337_dv_at_breakdown_below_21d_low_indicator(low, close, volume).diff().diff()


def f21_dvit_338_dv_on_first_close_below_21ema_indicator_d2(close, volume):
    return f21_dvit_338_dv_on_first_close_below_21ema_indicator(close, volume).diff().diff()


def f21_dvit_339_dv_on_first_close_below_63ema_indicator_d2(close, volume):
    return f21_dvit_339_dv_on_first_close_below_63ema_indicator(close, volume).diff().diff()


def f21_dvit_340_dv_on_first_close_below_252ema_indicator_d2(close, volume):
    return f21_dvit_340_dv_on_first_close_below_252ema_indicator(close, volume).diff().diff()


def f21_dvit_341_dv_above_5_sigma_indicator_d2(close, volume):
    return f21_dvit_341_dv_above_5_sigma_indicator(close, volume).diff().diff()


def f21_dvit_342_dv_above_4_sigma_indicator_d2(close, volume):
    return f21_dvit_342_dv_above_4_sigma_indicator(close, volume).diff().diff()


def f21_dvit_343_dv_above_5_sigma_count_252d_d2(close, volume):
    return f21_dvit_343_dv_above_5_sigma_count_252d(close, volume).diff().diff()


def f21_dvit_344_dv_below_neg2_sigma_indicator_d2(close, volume):
    return f21_dvit_344_dv_below_neg2_sigma_indicator(close, volume).diff().diff()


def f21_dvit_345_dv_below_neg3_sigma_indicator_d2(close, volume):
    return f21_dvit_345_dv_below_neg3_sigma_indicator(close, volume).diff().diff()


def f21_dvit_346_dv_below_neg2_sigma_count_252d_d2(close, volume):
    return f21_dvit_346_dv_below_neg2_sigma_count_252d(close, volume).diff().diff()


def f21_dvit_347_dv_extreme_high_then_extreme_low_within_5d_indicator_d2(close, volume):
    return f21_dvit_347_dv_extreme_high_then_extreme_low_within_5d_indicator(close, volume).diff().diff()


def f21_dvit_348_dv_extreme_high_followed_by_3_silent_days_indicator_d2(close, volume):
    return f21_dvit_348_dv_extreme_high_followed_by_3_silent_days_indicator(close, volume).diff().diff()


def f21_dvit_349_dv_max_252d_age_recent_5d_indicator_d2(close, volume):
    return f21_dvit_349_dv_max_252d_age_recent_5d_indicator(close, volume).diff().diff()


def f21_dvit_350_dv_max_252d_age_recent_21d_indicator_d2(close, volume):
    return f21_dvit_350_dv_max_252d_age_recent_21d_indicator(close, volume).diff().diff()


def f21_dvit_351_dv_top_5_days_in_last_21d_count_d2(close, volume):
    return f21_dvit_351_dv_top_5_days_in_last_21d_count(close, volume).diff().diff()


def f21_dvit_352_dv_top_10_days_in_last_21d_count_d2(close, volume):
    return f21_dvit_352_dv_top_10_days_in_last_21d_count(close, volume).diff().diff()


def f21_dvit_353_dv_top_5_days_in_last_5d_count_d2(close, volume):
    return f21_dvit_353_dv_top_5_days_in_last_5d_count(close, volume).diff().diff()


def f21_dvit_354_dv_top_concentration_in_last_5d_share_252d_d2(close, volume):
    return f21_dvit_354_dv_top_concentration_in_last_5d_share_252d(close, volume).diff().diff()


def f21_dvit_355_dv_top_concentration_in_last_21d_share_252d_d2(close, volume):
    return f21_dvit_355_dv_top_concentration_in_last_21d_share_252d(close, volume).diff().diff()


def f21_dvit_356_dv_increasing_5_days_indicator_d2(close, volume):
    return f21_dvit_356_dv_increasing_5_days_indicator(close, volume).diff().diff()


def f21_dvit_357_dv_decreasing_5_days_indicator_d2(close, volume):
    return f21_dvit_357_dv_decreasing_5_days_indicator(close, volume).diff().diff()


def f21_dvit_358_dv_double_burst_within_21d_indicator_d2(close, volume):
    return f21_dvit_358_dv_double_burst_within_21d_indicator(close, volume).diff().diff()


def f21_dvit_359_dv_triple_burst_within_63d_indicator_d2(close, volume):
    return f21_dvit_359_dv_triple_burst_within_63d_indicator(close, volume).diff().diff()


def f21_dvit_360_dv_burst_followed_by_lower_burst_within_5d_d2(close, volume):
    return f21_dvit_360_dv_burst_followed_by_lower_burst_within_5d(close, volume).diff().diff()


def f21_dvit_361_dv_first_burst_above_median_in_252d_indicator_d2(close, volume):
    return f21_dvit_361_dv_first_burst_above_median_in_252d_indicator(close, volume).diff().diff()


def f21_dvit_362_dv_burst_after_long_silence_indicator_d2(close, volume):
    return f21_dvit_362_dv_burst_after_long_silence_indicator(close, volume).diff().diff()


def f21_dvit_363_dv_climax_burst_signature_d2(high, close, volume):
    return f21_dvit_363_dv_climax_burst_signature(high, close, volume).diff().diff()


def f21_dvit_364_dv_post_climax_5d_drop_pct_252d_d2(close, volume):
    return f21_dvit_364_dv_post_climax_5d_drop_pct_252d(close, volume).diff().diff()


def f21_dvit_365_dv_consecutive_decline_after_burst_streak_d2(close, volume):
    return f21_dvit_365_dv_consecutive_decline_after_burst_streak(close, volume).diff().diff()


def f21_dvit_366_dv_5d_chg_pos_close_5d_chg_neg_indicator_d2(close, volume):
    return f21_dvit_366_dv_5d_chg_pos_close_5d_chg_neg_indicator(close, volume).diff().diff()


def f21_dvit_367_dv_5d_chg_neg_close_5d_chg_pos_indicator_d2(close, volume):
    return f21_dvit_367_dv_5d_chg_neg_close_5d_chg_pos_indicator(close, volume).diff().diff()


def f21_dvit_368_dv_21d_chg_pos_close_21d_chg_neg_indicator_d2(close, volume):
    return f21_dvit_368_dv_21d_chg_pos_close_21d_chg_neg_indicator(close, volume).diff().diff()


def f21_dvit_369_dv_21d_chg_neg_close_21d_chg_pos_indicator_d2(close, volume):
    return f21_dvit_369_dv_21d_chg_neg_close_21d_chg_pos_indicator(close, volume).diff().diff()


def f21_dvit_370_dv_lower_high_with_higher_price_high_252d_indicator_d2(high, close, volume):
    return f21_dvit_370_dv_lower_high_with_higher_price_high_252d_indicator(high, close, volume).diff().diff()


def f21_dvit_371_dv_lower_low_with_higher_price_low_252d_indicator_d2(low, close, volume):
    return f21_dvit_371_dv_lower_low_with_higher_price_low_252d_indicator(low, close, volume).diff().diff()


def f21_dvit_372_dv_divergence_at_252d_high_count_252d_d2(high, close, volume):
    return f21_dvit_372_dv_divergence_at_252d_high_count_252d(high, close, volume).diff().diff()


def f21_dvit_373_dv_divergence_severity_252d_d2(high, close, volume):
    return f21_dvit_373_dv_divergence_severity_252d(high, close, volume).diff().diff()


def f21_dvit_374_dv_failure_to_confirm_breakout_count_252d_d2(high, close, volume):
    return f21_dvit_374_dv_failure_to_confirm_breakout_count_252d(high, close, volume).diff().diff()


def f21_dvit_375_dv_confirms_breakdown_count_252d_d2(low, close, volume):
    return f21_dvit_375_dv_confirms_breakdown_count_252d(low, close, volume).diff().diff()


DOLLAR_VOLUME_INTENSITY_D2_REGISTRY_301_375 = {
    "f21_dvit_301_dv_zscore_on_doji_bars_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_301_dv_zscore_on_doji_bars_252d_d2},
    "f21_dvit_302_dv_zscore_on_engulfing_bars_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_302_dv_zscore_on_engulfing_bars_252d_d2},
    "f21_dvit_303_dv_zscore_on_pin_bar_at_high_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_303_dv_zscore_on_pin_bar_at_high_252d_d2},
    "f21_dvit_304_dv_on_inside_day_below_med_count_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_304_dv_on_inside_day_below_med_count_63d_d2},
    "f21_dvit_305_dv_on_outside_day_above_med_count_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_305_dv_on_outside_day_above_med_count_63d_d2},
    "f21_dvit_306_dv_on_marubozu_up_count_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_306_dv_on_marubozu_up_count_252d_d2},
    "f21_dvit_307_dv_on_marubozu_down_count_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_307_dv_on_marubozu_down_count_252d_d2},
    "f21_dvit_308_dv_on_hammer_bars_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_308_dv_on_hammer_bars_252d_d2},
    "f21_dvit_309_dv_on_shooting_star_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_309_dv_on_shooting_star_252d_d2},
    "f21_dvit_310_dv_concentration_on_outside_days_252d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_310_dv_concentration_on_outside_days_252d_d2},
    "f21_dvit_311_dv_on_3_consec_up_bars_avg_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_311_dv_on_3_consec_up_bars_avg_252d_d2},
    "f21_dvit_312_dv_on_3_consec_down_bars_avg_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_312_dv_on_3_consec_down_bars_avg_252d_d2},
    "f21_dvit_313_dv_on_gap_up_bars_mean_252d_d2": {"inputs": ["open", "close", "volume"], "func": f21_dvit_313_dv_on_gap_up_bars_mean_252d_d2},
    "f21_dvit_314_dv_on_gap_down_bars_mean_252d_d2": {"inputs": ["open", "close", "volume"], "func": f21_dvit_314_dv_on_gap_down_bars_mean_252d_d2},
    "f21_dvit_315_dv_on_widest_range_5_bars_252d_share_d2": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_315_dv_on_widest_range_5_bars_252d_share_d2},
    "f21_dvit_316_dv_mean_monday_to_overall_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_316_dv_mean_monday_to_overall_252d_d2},
    "f21_dvit_317_dv_mean_tuesday_to_overall_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_317_dv_mean_tuesday_to_overall_252d_d2},
    "f21_dvit_318_dv_mean_wednesday_to_overall_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_318_dv_mean_wednesday_to_overall_252d_d2},
    "f21_dvit_319_dv_mean_thursday_to_overall_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_319_dv_mean_thursday_to_overall_252d_d2},
    "f21_dvit_320_dv_mean_friday_to_overall_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_320_dv_mean_friday_to_overall_252d_d2},
    "f21_dvit_321_dv_mean_first_5_days_of_month_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_321_dv_mean_first_5_days_of_month_252d_d2},
    "f21_dvit_322_dv_mean_last_5_days_of_month_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_322_dv_mean_last_5_days_of_month_252d_d2},
    "f21_dvit_323_dv_quarter_end_5_days_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_323_dv_quarter_end_5_days_zscore_252d_d2},
    "f21_dvit_324_dv_year_end_indicator_5_days_d2": {"inputs": ["close", "volume"], "func": f21_dvit_324_dv_year_end_indicator_5_days_d2},
    "f21_dvit_325_dv_spike_count_friday_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_325_dv_spike_count_friday_252d_d2},
    "f21_dvit_326_dv_on_new_252d_high_minus_dv_on_close_below_252d_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_326_dv_on_new_252d_high_minus_dv_on_close_below_252d_d2},
    "f21_dvit_327_dv_spike_at_round_number_count_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_327_dv_spike_at_round_number_count_252d_d2},
    "f21_dvit_328_dv_spike_at_round_10_count_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_328_dv_spike_at_round_10_count_252d_d2},
    "f21_dvit_329_dv_at_top_of_range_in_top_5pct_close_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_329_dv_at_top_of_range_in_top_5pct_close_252d_d2},
    "f21_dvit_330_dv_concentration_on_top_5_close_bars_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_330_dv_concentration_on_top_5_close_bars_252d_d2},
    "f21_dvit_331_dv_concentration_on_bottom_5_close_bars_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_331_dv_concentration_on_bottom_5_close_bars_252d_d2},
    "f21_dvit_332_dv_ratio_top5_to_bot5_close_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_332_dv_ratio_top5_to_bot5_close_252d_d2},
    "f21_dvit_333_dv_at_3_white_soldiers_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_333_dv_at_3_white_soldiers_indicator_d2},
    "f21_dvit_334_dv_at_3_black_crows_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_334_dv_at_3_black_crows_indicator_d2},
    "f21_dvit_335_dv_at_breakout_above_252d_high_indicator_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_335_dv_at_breakout_above_252d_high_indicator_d2},
    "f21_dvit_336_dv_at_breakout_above_252d_high_count_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_336_dv_at_breakout_above_252d_high_count_252d_d2},
    "f21_dvit_337_dv_at_breakdown_below_21d_low_indicator_d2": {"inputs": ["low", "close", "volume"], "func": f21_dvit_337_dv_at_breakdown_below_21d_low_indicator_d2},
    "f21_dvit_338_dv_on_first_close_below_21ema_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_338_dv_on_first_close_below_21ema_indicator_d2},
    "f21_dvit_339_dv_on_first_close_below_63ema_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_339_dv_on_first_close_below_63ema_indicator_d2},
    "f21_dvit_340_dv_on_first_close_below_252ema_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_340_dv_on_first_close_below_252ema_indicator_d2},
    "f21_dvit_341_dv_above_5_sigma_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_341_dv_above_5_sigma_indicator_d2},
    "f21_dvit_342_dv_above_4_sigma_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_342_dv_above_4_sigma_indicator_d2},
    "f21_dvit_343_dv_above_5_sigma_count_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_343_dv_above_5_sigma_count_252d_d2},
    "f21_dvit_344_dv_below_neg2_sigma_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_344_dv_below_neg2_sigma_indicator_d2},
    "f21_dvit_345_dv_below_neg3_sigma_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_345_dv_below_neg3_sigma_indicator_d2},
    "f21_dvit_346_dv_below_neg2_sigma_count_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_346_dv_below_neg2_sigma_count_252d_d2},
    "f21_dvit_347_dv_extreme_high_then_extreme_low_within_5d_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_347_dv_extreme_high_then_extreme_low_within_5d_indicator_d2},
    "f21_dvit_348_dv_extreme_high_followed_by_3_silent_days_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_348_dv_extreme_high_followed_by_3_silent_days_indicator_d2},
    "f21_dvit_349_dv_max_252d_age_recent_5d_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_349_dv_max_252d_age_recent_5d_indicator_d2},
    "f21_dvit_350_dv_max_252d_age_recent_21d_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_350_dv_max_252d_age_recent_21d_indicator_d2},
    "f21_dvit_351_dv_top_5_days_in_last_21d_count_d2": {"inputs": ["close", "volume"], "func": f21_dvit_351_dv_top_5_days_in_last_21d_count_d2},
    "f21_dvit_352_dv_top_10_days_in_last_21d_count_d2": {"inputs": ["close", "volume"], "func": f21_dvit_352_dv_top_10_days_in_last_21d_count_d2},
    "f21_dvit_353_dv_top_5_days_in_last_5d_count_d2": {"inputs": ["close", "volume"], "func": f21_dvit_353_dv_top_5_days_in_last_5d_count_d2},
    "f21_dvit_354_dv_top_concentration_in_last_5d_share_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_354_dv_top_concentration_in_last_5d_share_252d_d2},
    "f21_dvit_355_dv_top_concentration_in_last_21d_share_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_355_dv_top_concentration_in_last_21d_share_252d_d2},
    "f21_dvit_356_dv_increasing_5_days_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_356_dv_increasing_5_days_indicator_d2},
    "f21_dvit_357_dv_decreasing_5_days_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_357_dv_decreasing_5_days_indicator_d2},
    "f21_dvit_358_dv_double_burst_within_21d_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_358_dv_double_burst_within_21d_indicator_d2},
    "f21_dvit_359_dv_triple_burst_within_63d_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_359_dv_triple_burst_within_63d_indicator_d2},
    "f21_dvit_360_dv_burst_followed_by_lower_burst_within_5d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_360_dv_burst_followed_by_lower_burst_within_5d_d2},
    "f21_dvit_361_dv_first_burst_above_median_in_252d_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_361_dv_first_burst_above_median_in_252d_indicator_d2},
    "f21_dvit_362_dv_burst_after_long_silence_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_362_dv_burst_after_long_silence_indicator_d2},
    "f21_dvit_363_dv_climax_burst_signature_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_363_dv_climax_burst_signature_d2},
    "f21_dvit_364_dv_post_climax_5d_drop_pct_252d_d2": {"inputs": ["close", "volume"], "func": f21_dvit_364_dv_post_climax_5d_drop_pct_252d_d2},
    "f21_dvit_365_dv_consecutive_decline_after_burst_streak_d2": {"inputs": ["close", "volume"], "func": f21_dvit_365_dv_consecutive_decline_after_burst_streak_d2},
    "f21_dvit_366_dv_5d_chg_pos_close_5d_chg_neg_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_366_dv_5d_chg_pos_close_5d_chg_neg_indicator_d2},
    "f21_dvit_367_dv_5d_chg_neg_close_5d_chg_pos_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_367_dv_5d_chg_neg_close_5d_chg_pos_indicator_d2},
    "f21_dvit_368_dv_21d_chg_pos_close_21d_chg_neg_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_368_dv_21d_chg_pos_close_21d_chg_neg_indicator_d2},
    "f21_dvit_369_dv_21d_chg_neg_close_21d_chg_pos_indicator_d2": {"inputs": ["close", "volume"], "func": f21_dvit_369_dv_21d_chg_neg_close_21d_chg_pos_indicator_d2},
    "f21_dvit_370_dv_lower_high_with_higher_price_high_252d_indicator_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_370_dv_lower_high_with_higher_price_high_252d_indicator_d2},
    "f21_dvit_371_dv_lower_low_with_higher_price_low_252d_indicator_d2": {"inputs": ["low", "close", "volume"], "func": f21_dvit_371_dv_lower_low_with_higher_price_low_252d_indicator_d2},
    "f21_dvit_372_dv_divergence_at_252d_high_count_252d_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_372_dv_divergence_at_252d_high_count_252d_d2},
    "f21_dvit_373_dv_divergence_severity_252d_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_373_dv_divergence_severity_252d_d2},
    "f21_dvit_374_dv_failure_to_confirm_breakout_count_252d_d2": {"inputs": ["high", "close", "volume"], "func": f21_dvit_374_dv_failure_to_confirm_breakout_count_252d_d2},
    "f21_dvit_375_dv_confirms_breakdown_count_252d_d2": {"inputs": ["low", "close", "volume"], "func": f21_dvit_375_dv_confirms_breakdown_count_252d_d2},
}
