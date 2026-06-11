"""Auto-generated D2 wrappers from distribution_signature__base__076_150.py.

Each function inlines the base body and appends .diff() chained 2 time(s)."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

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
    idx = num.index if hasattr(num, 'index') else None
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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f07_dsig_076_upthrust_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    pos = (close - low) / (high - low).replace(0, np.nan)
    below_mid = pos < 0.5
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    flag = (nh & below_mid & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_077_upthrust_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    pos = (close - low) / (high - low).replace(0, np.nan)
    below_mid = pos < 0.5
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    flag = (nh & below_mid & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_078_utad_pattern_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = high > prior_max
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 1.0 / 3.0
    atr = _atr(high, low, close, MDAYS)
    range_bound = high.rolling(10, min_periods=5).max() - low.rolling(10, min_periods=5).min() < 1.5 * atr
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    flag = (nh & weak & range_bound.shift(1).fillna(False) & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_079_spring_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_low = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    pierce = low < prior_low
    recover = close > prior_low
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    low_v = volume < avg
    flag = (pierce & recover & low_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_080_selling_climax_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_min = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    new_low = low < prior_min
    z = _rolling_zscore(volume, YDAYS)
    big = z > 3.0
    flag = (new_low & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_081_automatic_rally_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    z = _rolling_zscore(volume, YDAYS)
    climax = (z.shift(WDAYS) > 3.0) & (close.diff(WDAYS) < 0)
    rally = close.diff() > 0
    flag = (climax & rally).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_082_test_bar_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_low = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    near_low = low <= prior_low * 1.02
    med = volume.rolling(QDAYS, min_periods=MDAYS).median()
    low_v = volume < med
    flag = (near_low & low_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_083_preliminary_supply_marker_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = high - low > 1.5 * atr
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 0.5
    up = close > close.shift(1)
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (wide & weak & up & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_084_sign_of_weakness_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    down = chg < -0.01
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    flag = (down & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_085_sign_of_weakness_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    down = chg < -0.01
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    flag = (down & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_086_no_demand_bar_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    avg5 = volume.shift(1).rolling(WDAYS, min_periods=2).mean()
    low_v = volume < avg5
    flag = (up & low_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_087_no_demand_bar_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    up = close > close.shift(1)
    avg5 = volume.shift(1).rolling(WDAYS, min_periods=2).mean()
    low_v = volume < avg5
    flag = (up & low_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_088_weak_rally_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    weak = (chg > 0) & (chg < 0.005)
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_089_weak_rally_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    weak = (chg > 0) & (chg < 0.005)
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (weak & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_090_lps_retest_lower_high_count_21d_d2(high: pd.Series) -> pd.Series:
    prior21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    prior5 = high.shift(1).rolling(WDAYS, min_periods=2).max()
    flag = ((high < prior21) & (high > prior5)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_091_lps_retest_lower_high_count_63d_d2(high: pd.Series) -> pd.Series:
    prior21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    prior5 = high.shift(1).rolling(WDAYS, min_periods=2).max()
    flag = ((high < prior21) & (high > prior5)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_092_top_pattern_rolling_high_count_63d_d2(high: pd.Series) -> pd.Series:
    h21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    h63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    fail = (h21 < h63).astype(float)
    return fail.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_093_distribution_phase_fraction_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    supply = (chg < 0) & (volume > volume.shift(1))
    flag = supply.astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_094_accumulation_vs_distribution_composite_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > avg
    acc = ((chg > 0) & big_v).astype(float)
    dist = ((chg < 0) & big_v).astype(float)
    return (acc - dist).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_095_wyckoff_phase_indicator_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > avg
    acc = ((chg > 0) & big_v).astype(float)
    dist = ((chg < 0) & big_v).astype(float)
    net = (acc - dist).rolling(QDAYS, min_periods=MDAYS).sum()
    hi63 = close.rolling(QDAYS, min_periods=MDAYS).max()
    near = close / hi63.replace(0, np.nan) >= 0.95
    return ((net < 0) & near).astype(float).diff().diff()

def f07_dsig_096_trend_line_break_vol_z_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    above = close > sma
    streak = above.astype(int).groupby((~above).cumsum()).cumsum()
    just_broke = (close < sma) & (streak.shift(1).fillna(0) >= 5)
    v_on_break = volume.where(just_broke)
    return _rolling_zscore(v_on_break.ffill(), YDAYS).diff().diff()

def f07_dsig_097_supply_line_touch_count_63d_d2(high: pd.Series) -> pd.Series:
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    touch = (high >= 0.99 * rmax).astype(float)
    return touch.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_098_demand_line_break_count_63d_d2(low: pd.Series) -> pd.Series:
    prior_min = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    flag = (low < prior_min).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_099_composite_wyckoff_distribution_score_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    pos = (close - low) / (high - low).replace(0, np.nan)
    below_mid = pos < 0.5
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    upthrust = (nh & below_mid & big).astype(float)
    chg = close.pct_change()
    sow = ((chg < -0.01) & big).astype(float)
    dist = ((chg < -0.005) & (volume > volume.shift(1))).astype(float)
    return (upthrust + sow + dist).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_100_composite_wyckoff_exhaustion_score_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    pos = (close - low) / (high - low).replace(0, np.nan)
    below_mid = pos < 0.5
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 1.5 * avg
    upthrust = (nh & below_mid & big).astype(float)
    chg = close.pct_change()
    sow = ((chg < -0.01) & big).astype(float)
    return (upthrust + sow).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_101_pct_up_bars_21d_d2(close: pd.Series) -> pd.Series:
    up = (close.diff() > 0).astype(float)
    return up.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_102_pct_up_bars_63d_d2(close: pd.Series) -> pd.Series:
    up = (close.diff() > 0).astype(float)
    return up.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_103_pct_down_bars_21d_d2(close: pd.Series) -> pd.Series:
    dn = (close.diff() < 0).astype(float)
    return dn.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_104_pct_down_bars_63d_d2(close: pd.Series) -> pd.Series:
    dn = (close.diff() < 0).astype(float)
    return dn.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_105_up_down_bar_imbalance_z_21d_d2(close: pd.Series) -> pd.Series:
    up = (close.diff() > 0).astype(float)
    dn = (close.diff() < 0).astype(float)
    imb = up.rolling(MDAYS, min_periods=WDAYS).sum() - dn.rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(imb, YDAYS).diff().diff()

def f07_dsig_106_up_down_bar_imbalance_z_63d_d2(close: pd.Series) -> pd.Series:
    up = (close.diff() > 0).astype(float)
    dn = (close.diff() < 0).astype(float)
    imb = up.rolling(QDAYS, min_periods=MDAYS).sum() - dn.rolling(QDAYS, min_periods=MDAYS).sum()
    return _rolling_zscore(imb, YDAYS).diff().diff()

def f07_dsig_107_wide_range_down_bar_pct_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = high - low > 1.5 * atr
    down = close < close.shift(1)
    flag = (wide & down).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_108_wide_range_down_bar_pct_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = high - low > 1.5 * atr
    down = close < close.shift(1)
    flag = (wide & down).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_109_wide_range_up_bar_pct_decline_21_vs_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    atr = _atr(high, low, close, MDAYS)
    wide = high - low > 1.5 * atr
    up = close > close.shift(1)
    flag = (wide & up).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).mean() - flag.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f07_dsig_110_avg_up_bar_gain_21d_d2(close: pd.Series) -> pd.Series:
    chg = _safe_log(close).diff()
    return chg.where(chg > 0).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_111_avg_down_bar_loss_21d_d2(close: pd.Series) -> pd.Series:
    chg = _safe_log(close).diff()
    return chg.where(chg < 0).abs().rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_112_up_to_down_avg_return_ratio_21d_d2(close: pd.Series) -> pd.Series:
    chg = _safe_log(close).diff()
    up = chg.where(chg > 0).rolling(MDAYS, min_periods=WDAYS).mean()
    dn = chg.where(chg < 0).abs().rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(up, dn).diff().diff()

def f07_dsig_113_up_to_down_avg_return_ratio_63d_d2(close: pd.Series) -> pd.Series:
    chg = _safe_log(close).diff()
    up = chg.where(chg > 0).rolling(QDAYS, min_periods=MDAYS).mean()
    dn = chg.where(chg < 0).abs().rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(up, dn).diff().diff()

def f07_dsig_114_consecutive_down_bar_max_21d_d2(close: pd.Series) -> pd.Series:
    dn = (close.diff() < 0).astype(int)
    grp = (dn == 0).cumsum()
    streak = dn.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max().diff().diff()

def f07_dsig_115_consecutive_down_bar_max_63d_d2(close: pd.Series) -> pd.Series:
    dn = (close.diff() < 0).astype(int)
    grp = (dn == 0).cumsum()
    streak = dn.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max().diff().diff()

def f07_dsig_116_down_bar_streak_count_63d_d2(close: pd.Series) -> pd.Series:
    dn = (close.diff() < 0).astype(int)
    grp = (dn == 0).cumsum()
    streak = dn.groupby(grp).cumsum()
    ended = ((streak.shift(1) >= 3) & (dn == 0)).astype(float)
    return ended.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_117_trin_style_proxy_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_c = (chg > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_c = (chg < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    up_v = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(_safe_div(dn_c, up_c), _safe_div(dn_v, up_v)).diff().diff()

def f07_dsig_118_mcclellan_style_oscillator_63d_d2(close: pd.Series) -> pd.Series:
    chg = close.diff()
    diff = (chg > 0).astype(float) - (chg < 0).astype(float)
    e19 = diff.ewm(span=19, adjust=False, min_periods=10).mean()
    e39 = diff.ewm(span=39, adjust=False, min_periods=15).mean()
    return (e19 - e39).diff().diff()

def f07_dsig_119_directional_movement_dx_14d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    up = high.diff()
    dn = -low.diff()
    plus_dm = up.where((up > dn) & (up > 0), 0.0)
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    tr = _true_range(high, low, close)
    atr14 = tr.rolling(14, min_periods=5).mean()
    plus_di = 100.0 * plus_dm.rolling(14, min_periods=5).mean() / atr14.replace(0, np.nan)
    minus_di = 100.0 * minus_dm.rolling(14, min_periods=5).mean() / atr14.replace(0, np.nan)
    return (100.0 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)).diff().diff()

def f07_dsig_120_minus_dm_avg_14d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    up = high.diff()
    dn = -low.diff()
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    return minus_dm.rolling(14, min_periods=5).mean().diff().diff()

def f07_dsig_121_minus_dm_avg_28d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    up = high.diff()
    dn = -low.diff()
    minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
    return minus_dm.rolling(28, min_periods=10).mean().diff().diff()

def f07_dsig_122_pct_bars_close_upper_third_decline_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    flag = (pos >= 2.0 / 3.0).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_123_pct_bars_close_lower_third_rising_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    flag = (pos <= 1.0 / 3.0).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_124_avg_close_position_in_bar_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    return pos.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_125_avg_close_position_in_bar_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    return pos.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_126_price_vol_slope_diff_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_sl = _rolling_slope(close, MDAYS) / close.rolling(MDAYS, min_periods=WDAYS).mean().replace(0, np.nan)
    v_sl = _rolling_slope(volume, MDAYS) / volume.rolling(MDAYS, min_periods=WDAYS).mean().replace(0, np.nan)
    return (p_sl - v_sl).diff().diff()

def f07_dsig_127_price_vol_slope_diff_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    v_sl = _rolling_slope(volume, QDAYS) / volume.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return (p_sl - v_sl).diff().diff()

def f07_dsig_128_price_vol_correlation_collapse_21_vs_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    c21 = close.rolling(MDAYS, min_periods=WDAYS).corr(volume)
    c63 = close.rolling(QDAYS, min_periods=MDAYS).corr(volume)
    return (c21 - c63).diff().diff()

def f07_dsig_129_price_below_vwap_21d_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    num = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    vw = num / den
    flag = (close < vw).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_130_price_below_vwap_63d_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    num = (close * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)
    vw = num / den
    flag = (close < vw).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_131_close_below_vwap_transition_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    num = (close * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)
    vw = num / den
    below = (close < vw).astype(int)
    cross_down = ((below == 1) & (below.shift(1) == 0)).astype(float)
    return cross_down.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_132_trin_style_topping_signal_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    up_c = (chg > 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_c = (chg < 0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    up_v = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_v = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    trin = _safe_div(_safe_div(dn_c, up_c), _safe_div(dn_v, up_v))
    return _rolling_slope(trin, QDAYS).diff().diff()

def f07_dsig_133_effort_up_vs_down_ratio_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    up_eff = (volume * chg.where(chg > 0, 0)).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_eff = (volume * chg.where(chg < 0, 0).abs()).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up_eff, dn_eff).diff().diff()

def f07_dsig_134_avg_loss_size_vs_avg_gain_size_21d_d2(close: pd.Series) -> pd.Series:
    chg = close.pct_change()
    g = chg.where(chg > 0).rolling(MDAYS, min_periods=WDAYS).mean()
    l = chg.where(chg < 0).abs().rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(l, g).diff().diff()

def f07_dsig_135_avg_loss_size_vs_avg_gain_size_63d_d2(close: pd.Series) -> pd.Series:
    chg = close.pct_change()
    g = chg.where(chg > 0).rolling(QDAYS, min_periods=MDAYS).mean()
    l = chg.where(chg < 0).abs().rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(l, g).diff().diff()

def f07_dsig_136_ibd_distribution_day_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    flag = ((chg < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_137_ibd_distribution_day_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    flag = ((chg < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_138_distribution_day_fraction_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    flag = ((chg < -0.002) & (volume > volume.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_139_follow_through_failure_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_up_v = (chg.shift(1) > 0.01) & (volume.shift(1) > 1.5 * avg.shift(1))
    rev = chg < -0.005
    flag = (big_up_v & rev).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_140_consecutive_distribution_days_max_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.pct_change()
    flag = ((chg < -0.002) & (volume > volume.shift(1))).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max().diff().diff()

def f07_dsig_141_red_dollar_vol_z_21d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    red_dv = dv.where(close < open_)
    m = red_dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m, YDAYS).diff().diff()

def f07_dsig_142_red_dollar_vol_z_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    red_dv = dv.where(close < open_)
    m = red_dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(m, YDAYS).diff().diff()

def f07_dsig_143_up_top_decile_vs_down_top_decile_vol_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    thr = volume.rolling(QDAYS, min_periods=MDAYS).quantile(0.9)
    big = volume >= thr
    chg = close.diff()
    up_big = (big & (chg > 0)).astype(float)
    dn_big = (big & (chg < 0)).astype(float)
    return (up_big.rolling(QDAYS, min_periods=MDAYS).sum() - dn_big.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()

def f07_dsig_144_cumulative_vol_skew_down_heavy_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    chg = close.diff()
    signed = volume * np.sign(chg).fillna(0)

    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / sd ** 3)
    return signed.rolling(QDAYS, min_periods=MDAYS).apply(_sk, raw=True).diff().diff()

def f07_dsig_145_pct_bars_close_lower_half_high_vol_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 0.5
    z = _rolling_zscore(volume, YDAYS)
    big = z > 1.5
    flag = (weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_146_pct_bars_close_lower_half_high_vol_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 0.5
    z = _rolling_zscore(volume, YDAYS)
    big = z > 1.5
    flag = (weak & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f07_dsig_147_weak_close_high_vol_count_21d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    weak = close < open_
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f07_dsig_148_weak_close_high_vol_count_63d_d2(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    weak = close < open_
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (weak & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f07_dsig_149_final_distribution_composite_score_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, open_: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0, 0)
    dn_v = volume.where(chg < 0, 0)
    sup = _safe_div(dn_v.rolling(WDAYS, min_periods=2).sum(), up_v.rolling(WDAYS, min_periods=2).sum())
    z = _rolling_zscore(volume, YDAYS)
    weak = ((close < open_) & (z > 2.0)).astype(float)
    chg_pct = close.pct_change()
    dist = ((chg_pct < -0.002) & (volume > volume.shift(1))).astype(float)
    return (sup + weak + dist).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f07_dsig_150_final_distribution_composite_score_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, open_: pd.Series) -> pd.Series:
    chg = close.diff()
    up_v = volume.where(chg > 0, 0)
    dn_v = volume.where(chg < 0, 0)
    sup = _safe_div(dn_v.rolling(WDAYS, min_periods=2).sum(), up_v.rolling(WDAYS, min_periods=2).sum())
    z = _rolling_zscore(volume, YDAYS)
    weak = ((close < open_) & (z > 2.0)).astype(float)
    chg_pct = close.pct_change()
    dist = ((chg_pct < -0.002) & (volume > volume.shift(1))).astype(float)
    return (sup + weak + dist).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()
DISTRIBUTION_SIGNATURE_D2_REGISTRY_076_150 = {'f07_dsig_076_upthrust_count_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_076_upthrust_count_21d_d2}, 'f07_dsig_077_upthrust_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_077_upthrust_count_63d_d2}, 'f07_dsig_078_utad_pattern_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_078_utad_pattern_count_63d_d2}, 'f07_dsig_079_spring_count_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_079_spring_count_21d_d2}, 'f07_dsig_080_selling_climax_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_080_selling_climax_count_63d_d2}, 'f07_dsig_081_automatic_rally_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_081_automatic_rally_count_63d_d2}, 'f07_dsig_082_test_bar_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_082_test_bar_count_63d_d2}, 'f07_dsig_083_preliminary_supply_marker_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_083_preliminary_supply_marker_count_63d_d2}, 'f07_dsig_084_sign_of_weakness_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_084_sign_of_weakness_count_21d_d2}, 'f07_dsig_085_sign_of_weakness_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_085_sign_of_weakness_count_63d_d2}, 'f07_dsig_086_no_demand_bar_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_086_no_demand_bar_count_21d_d2}, 'f07_dsig_087_no_demand_bar_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_087_no_demand_bar_count_63d_d2}, 'f07_dsig_088_weak_rally_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_088_weak_rally_count_21d_d2}, 'f07_dsig_089_weak_rally_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_089_weak_rally_count_63d_d2}, 'f07_dsig_090_lps_retest_lower_high_count_21d_d2': {'inputs': ['high'], 'func': f07_dsig_090_lps_retest_lower_high_count_21d_d2}, 'f07_dsig_091_lps_retest_lower_high_count_63d_d2': {'inputs': ['high'], 'func': f07_dsig_091_lps_retest_lower_high_count_63d_d2}, 'f07_dsig_092_top_pattern_rolling_high_count_63d_d2': {'inputs': ['high'], 'func': f07_dsig_092_top_pattern_rolling_high_count_63d_d2}, 'f07_dsig_093_distribution_phase_fraction_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_093_distribution_phase_fraction_63d_d2}, 'f07_dsig_094_accumulation_vs_distribution_composite_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_094_accumulation_vs_distribution_composite_63d_d2}, 'f07_dsig_095_wyckoff_phase_indicator_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_095_wyckoff_phase_indicator_63d_d2}, 'f07_dsig_096_trend_line_break_vol_z_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_096_trend_line_break_vol_z_21d_d2}, 'f07_dsig_097_supply_line_touch_count_63d_d2': {'inputs': ['high'], 'func': f07_dsig_097_supply_line_touch_count_63d_d2}, 'f07_dsig_098_demand_line_break_count_63d_d2': {'inputs': ['low'], 'func': f07_dsig_098_demand_line_break_count_63d_d2}, 'f07_dsig_099_composite_wyckoff_distribution_score_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_099_composite_wyckoff_distribution_score_63d_d2}, 'f07_dsig_100_composite_wyckoff_exhaustion_score_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_100_composite_wyckoff_exhaustion_score_21d_d2}, 'f07_dsig_101_pct_up_bars_21d_d2': {'inputs': ['close'], 'func': f07_dsig_101_pct_up_bars_21d_d2}, 'f07_dsig_102_pct_up_bars_63d_d2': {'inputs': ['close'], 'func': f07_dsig_102_pct_up_bars_63d_d2}, 'f07_dsig_103_pct_down_bars_21d_d2': {'inputs': ['close'], 'func': f07_dsig_103_pct_down_bars_21d_d2}, 'f07_dsig_104_pct_down_bars_63d_d2': {'inputs': ['close'], 'func': f07_dsig_104_pct_down_bars_63d_d2}, 'f07_dsig_105_up_down_bar_imbalance_z_21d_d2': {'inputs': ['close'], 'func': f07_dsig_105_up_down_bar_imbalance_z_21d_d2}, 'f07_dsig_106_up_down_bar_imbalance_z_63d_d2': {'inputs': ['close'], 'func': f07_dsig_106_up_down_bar_imbalance_z_63d_d2}, 'f07_dsig_107_wide_range_down_bar_pct_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_107_wide_range_down_bar_pct_21d_d2}, 'f07_dsig_108_wide_range_down_bar_pct_63d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_108_wide_range_down_bar_pct_63d_d2}, 'f07_dsig_109_wide_range_up_bar_pct_decline_21_vs_63_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_109_wide_range_up_bar_pct_decline_21_vs_63_d2}, 'f07_dsig_110_avg_up_bar_gain_21d_d2': {'inputs': ['close'], 'func': f07_dsig_110_avg_up_bar_gain_21d_d2}, 'f07_dsig_111_avg_down_bar_loss_21d_d2': {'inputs': ['close'], 'func': f07_dsig_111_avg_down_bar_loss_21d_d2}, 'f07_dsig_112_up_to_down_avg_return_ratio_21d_d2': {'inputs': ['close'], 'func': f07_dsig_112_up_to_down_avg_return_ratio_21d_d2}, 'f07_dsig_113_up_to_down_avg_return_ratio_63d_d2': {'inputs': ['close'], 'func': f07_dsig_113_up_to_down_avg_return_ratio_63d_d2}, 'f07_dsig_114_consecutive_down_bar_max_21d_d2': {'inputs': ['close'], 'func': f07_dsig_114_consecutive_down_bar_max_21d_d2}, 'f07_dsig_115_consecutive_down_bar_max_63d_d2': {'inputs': ['close'], 'func': f07_dsig_115_consecutive_down_bar_max_63d_d2}, 'f07_dsig_116_down_bar_streak_count_63d_d2': {'inputs': ['close'], 'func': f07_dsig_116_down_bar_streak_count_63d_d2}, 'f07_dsig_117_trin_style_proxy_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_117_trin_style_proxy_21d_d2}, 'f07_dsig_118_mcclellan_style_oscillator_63d_d2': {'inputs': ['close'], 'func': f07_dsig_118_mcclellan_style_oscillator_63d_d2}, 'f07_dsig_119_directional_movement_dx_14d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_119_directional_movement_dx_14d_d2}, 'f07_dsig_120_minus_dm_avg_14d_d2': {'inputs': ['high', 'low'], 'func': f07_dsig_120_minus_dm_avg_14d_d2}, 'f07_dsig_121_minus_dm_avg_28d_d2': {'inputs': ['high', 'low'], 'func': f07_dsig_121_minus_dm_avg_28d_d2}, 'f07_dsig_122_pct_bars_close_upper_third_decline_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_122_pct_bars_close_upper_third_decline_21d_d2}, 'f07_dsig_123_pct_bars_close_lower_third_rising_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_123_pct_bars_close_lower_third_rising_21d_d2}, 'f07_dsig_124_avg_close_position_in_bar_21d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_124_avg_close_position_in_bar_21d_d2}, 'f07_dsig_125_avg_close_position_in_bar_63d_d2': {'inputs': ['high', 'low', 'close'], 'func': f07_dsig_125_avg_close_position_in_bar_63d_d2}, 'f07_dsig_126_price_vol_slope_diff_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_126_price_vol_slope_diff_21d_d2}, 'f07_dsig_127_price_vol_slope_diff_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_127_price_vol_slope_diff_63d_d2}, 'f07_dsig_128_price_vol_correlation_collapse_21_vs_63_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_128_price_vol_correlation_collapse_21_vs_63_d2}, 'f07_dsig_129_price_below_vwap_21d_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_129_price_below_vwap_21d_count_21d_d2}, 'f07_dsig_130_price_below_vwap_63d_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_130_price_below_vwap_63d_count_63d_d2}, 'f07_dsig_131_close_below_vwap_transition_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_131_close_below_vwap_transition_count_21d_d2}, 'f07_dsig_132_trin_style_topping_signal_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_132_trin_style_topping_signal_63d_d2}, 'f07_dsig_133_effort_up_vs_down_ratio_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_133_effort_up_vs_down_ratio_21d_d2}, 'f07_dsig_134_avg_loss_size_vs_avg_gain_size_21d_d2': {'inputs': ['close'], 'func': f07_dsig_134_avg_loss_size_vs_avg_gain_size_21d_d2}, 'f07_dsig_135_avg_loss_size_vs_avg_gain_size_63d_d2': {'inputs': ['close'], 'func': f07_dsig_135_avg_loss_size_vs_avg_gain_size_63d_d2}, 'f07_dsig_136_ibd_distribution_day_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_136_ibd_distribution_day_count_21d_d2}, 'f07_dsig_137_ibd_distribution_day_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_137_ibd_distribution_day_count_63d_d2}, 'f07_dsig_138_distribution_day_fraction_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_138_distribution_day_fraction_63d_d2}, 'f07_dsig_139_follow_through_failure_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_139_follow_through_failure_count_21d_d2}, 'f07_dsig_140_consecutive_distribution_days_max_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_140_consecutive_distribution_days_max_63d_d2}, 'f07_dsig_141_red_dollar_vol_z_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_141_red_dollar_vol_z_21d_d2}, 'f07_dsig_142_red_dollar_vol_z_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_142_red_dollar_vol_z_63d_d2}, 'f07_dsig_143_up_top_decile_vs_down_top_decile_vol_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_143_up_top_decile_vs_down_top_decile_vol_63d_d2}, 'f07_dsig_144_cumulative_vol_skew_down_heavy_63d_d2': {'inputs': ['close', 'volume'], 'func': f07_dsig_144_cumulative_vol_skew_down_heavy_63d_d2}, 'f07_dsig_145_pct_bars_close_lower_half_high_vol_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_145_pct_bars_close_lower_half_high_vol_21d_d2}, 'f07_dsig_146_pct_bars_close_lower_half_high_vol_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f07_dsig_146_pct_bars_close_lower_half_high_vol_63d_d2}, 'f07_dsig_147_weak_close_high_vol_count_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_147_weak_close_high_vol_count_21d_d2}, 'f07_dsig_148_weak_close_high_vol_count_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f07_dsig_148_weak_close_high_vol_count_63d_d2}, 'f07_dsig_149_final_distribution_composite_score_21d_d2': {'inputs': ['high', 'low', 'close', 'volume', 'open'], 'func': f07_dsig_149_final_distribution_composite_score_21d_d2}, 'f07_dsig_150_final_distribution_composite_score_63d_d2': {'inputs': ['high', 'low', 'close', 'volume', 'open'], 'func': f07_dsig_150_final_distribution_composite_score_63d_d2}}
