"""20_volume_dryup_at_high d2 features 526-600 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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
    idx = num.index if hasattr(num, 'index') else None
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

def _rsi(s, n):
    d = s.diff()
    g = d.clip(lower=0.0)
    l = (-d).clip(lower=0.0)
    ag = g.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    al = l.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    return 100.0 * _safe_div(ag, ag + al)

def f20_vdah_526_log_vol_rsi_14d_d2(volume: pd.Series) -> pd.Series:
    """RSI(14) on log-vol."""
    return _rsi(_safe_log(volume), 14).diff().diff()

def f20_vdah_527_log_vol_rsi_21d_d2(volume: pd.Series) -> pd.Series:
    """RSI(21) on log-vol."""
    return _rsi(_safe_log(volume), MDAYS).diff().diff()

def f20_vdah_528_log_vol_rsi_63d_d2(volume: pd.Series) -> pd.Series:
    """RSI(63) on log-vol — quarterly RSI."""
    return _rsi(_safe_log(volume), QDAYS).diff().diff()

def f20_vdah_529_log_vol_cci_20d_d2(volume: pd.Series) -> pd.Series:
    """CCI(20) on log-vol: (lv - SMA20) / (0.015 * mean abs dev)."""
    lv = _safe_log(volume)
    sma = lv.rolling(20, min_periods=10).mean()
    mad = (lv - sma).abs().rolling(20, min_periods=10).mean()
    return _safe_div(lv - sma, 0.015 * mad).diff().diff()

def f20_vdah_530_log_vol_cci_40d_d2(volume: pd.Series) -> pd.Series:
    """CCI(40) on log-vol."""
    lv = _safe_log(volume)
    sma = lv.rolling(40, min_periods=15).mean()
    mad = (lv - sma).abs().rolling(40, min_periods=15).mean()
    return _safe_div(lv - sma, 0.015 * mad).diff().diff()

def f20_vdah_531_log_vol_stoch_k_14d_d2(volume: pd.Series) -> pd.Series:
    """Stochastic %K(14) on log-vol: (lv - 14d-min) / (14d-max - 14d-min) × 100."""
    lv = _safe_log(volume)
    rmax = lv.rolling(14, min_periods=5).max()
    rmin = lv.rolling(14, min_periods=5).min()
    return (100.0 * _safe_div(lv - rmin, rmax - rmin)).diff().diff()

def f20_vdah_532_log_vol_stoch_k_63d_d2(volume: pd.Series) -> pd.Series:
    """Stochastic %K(63) on log-vol."""
    lv = _safe_log(volume)
    rmax = lv.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = lv.rolling(QDAYS, min_periods=MDAYS).min()
    return (100.0 * _safe_div(lv - rmin, rmax - rmin)).diff().diff()

def f20_vdah_533_log_vol_williams_r_14d_d2(volume: pd.Series) -> pd.Series:
    """Williams %R(14) on log-vol: -100 * (max - lv) / (max - min)."""
    lv = _safe_log(volume)
    rmax = lv.rolling(14, min_periods=5).max()
    rmin = lv.rolling(14, min_periods=5).min()
    return (-100.0 * _safe_div(rmax - lv, rmax - rmin)).diff().diff()

def f20_vdah_534_log_vol_trix_15d_d2(volume: pd.Series) -> pd.Series:
    """TRIX(15) on log-vol: rate of change of triple-EMA."""
    lv = _safe_log(volume)
    e1 = lv.ewm(span=15, min_periods=5, adjust=False).mean()
    e2 = e1.ewm(span=15, min_periods=5, adjust=False).mean()
    e3 = e2.ewm(span=15, min_periods=5, adjust=False).mean()
    return e3.pct_change().diff().diff()

def f20_vdah_535_log_vol_roc_5d_d2(volume: pd.Series) -> pd.Series:
    """5d rate of change of log-vol."""
    return _safe_log(volume).diff(WDAYS).diff().diff()

def f20_vdah_536_log_vol_roc_21d_d2(volume: pd.Series) -> pd.Series:
    """21d rate of change of log-vol."""
    return _safe_log(volume).diff(MDAYS).diff().diff()

def f20_vdah_537_log_vol_roc_63d_d2(volume: pd.Series) -> pd.Series:
    """63d rate of change of log-vol."""
    return _safe_log(volume).diff(QDAYS).diff().diff()

def f20_vdah_538_log_vol_ma_cross_21_63_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when EMA21(log_vol) > EMA63(log_vol) — short above medium."""
    lv = _safe_log(volume)
    return (lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() > lv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()).astype(float).diff().diff()

def f20_vdah_539_log_vol_ma_cross_21_63_event_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when EMA21(log_vol) crosses BELOW EMA63(log_vol) today."""
    lv = _safe_log(volume)
    e21 = lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    e63 = lv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    above = e21 > e63
    return (~above & above.shift(1).fillna(False)).astype(float).diff().diff()

def f20_vdah_540_log_vol_ma_distance_21_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (log_vol - EMA21(log_vol)) — distance from short MA."""
    lv = _safe_log(volume)
    return _rolling_zscore(lv - lv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean(), YDAYS).diff().diff()

def f20_vdah_541_log_vol_macd_line_12_26_d2(volume: pd.Series) -> pd.Series:
    """MACD line on log-vol: EMA(12, lv) - EMA(26, lv)."""
    lv = _safe_log(volume)
    return (lv.ewm(span=12, min_periods=6, adjust=False).mean() - lv.ewm(span=26, min_periods=12, adjust=False).mean()).diff().diff()

def f20_vdah_542_log_vol_macd_signal_12_26_9_d2(volume: pd.Series) -> pd.Series:
    """MACD signal line: 9-EMA of MACD line."""
    lv = _safe_log(volume)
    macd = lv.ewm(span=12, min_periods=6, adjust=False).mean() - lv.ewm(span=26, min_periods=12, adjust=False).mean()
    return macd.ewm(span=9, min_periods=4, adjust=False).mean().diff().diff()

def f20_vdah_543_log_vol_macd_histogram_d2(volume: pd.Series) -> pd.Series:
    """MACD histogram on log-vol: MACD - signal."""
    lv = _safe_log(volume)
    macd = lv.ewm(span=12, min_periods=6, adjust=False).mean() - lv.ewm(span=26, min_periods=12, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=4, adjust=False).mean()
    return (macd - signal).diff().diff()

def f20_vdah_544_log_vol_macd_hist_zerocross_count_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of MACD histogram zero crossings."""
    lv = _safe_log(volume)
    macd = lv.ewm(span=12, min_periods=6, adjust=False).mean() - lv.ewm(span=26, min_periods=12, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=4, adjust=False).mean()
    hist = macd - signal
    return (np.sign(hist).diff().abs() > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f20_vdah_545_log_vol_momentum_3d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when log-vol increased for 3 consecutive bars."""
    lv = _safe_log(volume)
    d = lv.diff()
    return ((d > 0) & (d.shift(1) > 0) & (d.shift(2) > 0)).astype(float).diff().diff()

def f20_vdah_546_log_vol_momentum_5d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when log-vol increased for 5 consecutive bars."""
    lv = _safe_log(volume)
    d = lv.diff()
    return ((d > 0) & (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0)).astype(float).diff().diff()

def f20_vdah_547_log_vol_neg_momentum_3d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when log-vol decreased for 3 consecutive bars."""
    lv = _safe_log(volume)
    d = lv.diff()
    return ((d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0)).astype(float).diff().diff()

def f20_vdah_548_log_vol_neg_momentum_5d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when log-vol decreased for 5 consecutive bars."""
    lv = _safe_log(volume)
    d = lv.diff()
    return ((d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0) & (d.shift(3) < 0) & (d.shift(4) < 0)).astype(float).diff().diff()

def f20_vdah_549_log_vol_thrust_4_of_5_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when 4+ of last 5 bars had log-vol > prior log-vol."""
    lv = _safe_log(volume)
    up_count = (lv.diff() > 0).astype(float).rolling(WDAYS, min_periods=1).sum()
    return (up_count >= 4).astype(float).diff().diff()

def f20_vdah_550_log_vol_thrust_5_of_5_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when all of last 5 bars had log-vol > prior log-vol (full thrust)."""
    lv = _safe_log(volume)
    up_count = (lv.diff() > 0).astype(float).rolling(WDAYS, min_periods=1).sum()
    return (up_count >= 5).astype(float).diff().diff()

def f20_vdah_551_log_vol_first_pos_after_neg_streak_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when today log-vol > prior log-vol AND prior 5 bars all had decreasing log-vol."""
    lv = _safe_log(volume)
    d = lv.diff()
    five_neg = (d.shift(1) < 0) & (d.shift(2) < 0) & (d.shift(3) < 0) & (d.shift(4) < 0) & (d.shift(5) < 0)
    return ((d > 0) & five_neg).astype(float).diff().diff()

def f20_vdah_552_log_vol_first_neg_after_pos_streak_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when today log-vol < prior log-vol AND prior 5 bars all had increasing log-vol."""
    lv = _safe_log(volume)
    d = lv.diff()
    five_pos = (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0) & (d.shift(5) > 0)
    return ((d < 0) & five_pos).astype(float).diff().diff()

def f20_vdah_553_log_vol_5d_change_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of 5d log-vol change."""
    return _rolling_zscore(_safe_log(volume).diff(WDAYS), YDAYS).diff().diff()

def f20_vdah_554_log_vol_21d_change_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of 21d log-vol change."""
    return _rolling_zscore(_safe_log(volume).diff(MDAYS), YDAYS).diff().diff()

def f20_vdah_555_log_vol_63d_change_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of 63d log-vol change."""
    return _rolling_zscore(_safe_log(volume).diff(QDAYS), YDAYS).diff().diff()

def f20_vdah_556_vol_up_price_down_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when vol > prior vol AND close < prior close — selling pressure."""
    return ((volume > volume.shift(1)) & (close < close.shift(1))).astype(float).diff().diff()

def f20_vdah_557_vol_up_price_down_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of vol-up-price-down events."""
    return ((volume > volume.shift(1)) & (close < close.shift(1))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f20_vdah_558_vol_up_price_down_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of vol-up-price-down events."""
    return ((volume > volume.shift(1)) & (close < close.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f20_vdah_559_vol_down_price_up_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when vol < prior vol AND close > prior close — weak rally."""
    return ((volume < volume.shift(1)) & (close > close.shift(1))).astype(float).diff().diff()

def f20_vdah_560_vol_down_price_up_count_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of vol-down-price-up events."""
    return ((volume < volume.shift(1)) & (close > close.shift(1))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f20_vdah_561_vol_down_price_up_count_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of vol-down-price-up events."""
    return ((volume < volume.shift(1)) & (close > close.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f20_vdah_562_vol_up_price_down_to_vol_up_price_up_ratio_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d vol-up-price-down count) / (252d vol-up-price-up count)."""
    a = ((volume > volume.shift(1)) & (close < close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    b = ((volume > volume.shift(1)) & (close > close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(a, b + 1.0).diff().diff()

def f20_vdah_563_vol_down_with_close_at_252d_high_indicator_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when high at 252d max AND vol < prior vol — soft top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (volume < volume.shift(1))).astype(float).diff().diff()

def f20_vdah_564_vol_down_with_close_at_252d_high_count_252d_d2(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of soft-top events (high at 252d max AND vol < prior)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (volume < volume.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f20_vdah_565_vol_at_inside_day_vs_outside_day_ratio_252d_d2(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on inside days / avg vol on outside days over 252d."""
    inside = (high < high.shift(1)) & (low > low.shift(1))
    outside = (high > high.shift(1)) & (low < low.shift(1))
    av_in = volume.where(inside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    av_out = volume.where(outside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(av_in, av_out).diff().diff()

def f20_vdah_566_vol_at_doji_to_overall_vol_ratio_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on doji bars / overall avg vol, 252d."""
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    doji_v = volume.where(body < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    overall_v = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(doji_v, overall_v).diff().diff()

def f20_vdah_567_vol_at_close_above_high_5d_ago_indicator_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close > close.shift(5) AND vol < 21d median (silent recovery)."""
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    return ((close > close.shift(5)) & (volume < med21)).astype(float).diff().diff()

def f20_vdah_568_vol_when_close_pct_gt_2pct_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close pct_change > 2% over trailing 252d."""
    return volume.where(close.pct_change() > 0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f20_vdah_569_vol_when_close_pct_lt_neg2pct_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close pct_change < -2% over trailing 252d."""
    return volume.where(close.pct_change() < -0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f20_vdah_570_vol_extreme_move_asymmetry_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Avg vol on bars w/ close pct_change>2%) - (avg vol on bars w/ close pct_change<-2%), 252d."""
    up_v = volume.where(close.pct_change() > 0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn_v = volume.where(close.pct_change() < -0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (up_v - dn_v).diff().diff()

def f20_vdah_571_log_vol_3state_regime_label_d2(volume: pd.Series) -> pd.Series:
    """3-state regime label from log-vol z(252d): -1 (z<-0.5), 0, +1 (z>+0.5)."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0)).diff().diff()

def f20_vdah_572_log_vol_regime_high_dwell_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in high-vol regime (z>+0.5)."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f20_vdah_573_log_vol_regime_low_dwell_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in low-vol regime (z<-0.5)."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f20_vdah_574_log_vol_regime_transitions_count_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of log-vol regime transitions (label changes)."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f20_vdah_575_log_vol_regime_current_age_d2(volume: pd.Series) -> pd.Series:
    """Bars in current log-vol regime."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    diff = label != label.shift(1)
    grp = diff.cumsum()
    return label.groupby(grp).cumcount().astype(float).diff().diff()

def f20_vdah_576_log_vol_regime_high_to_low_transition_count_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of high→low log-vol regime transitions."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == 1) & (label == -1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f20_vdah_577_log_vol_regime_low_to_high_transition_count_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of low→high log-vol regime transitions."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == -1) & (label == 1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f20_vdah_578_log_vol_regime_persistence_mean_run_252d_d2(volume: pd.Series) -> pd.Series:
    """Mean regime-run length over trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    diff = (label != label.shift(1)).astype(int)
    return (252.0 / diff.rolling(YDAYS, min_periods=QDAYS).sum().replace(0, np.nan)).diff().diff()

def f20_vdah_579_log_vol_at_regime_transition_event_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when today is a regime transition (label changed)."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).diff().diff()

def f20_vdah_580_log_vol_recently_transitioned_5d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when a regime transition occurred within last 5 bars."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(WDAYS, min_periods=1).max().fillna(0.0).diff().diff()

def f20_vdah_581_log_vol_recently_transitioned_21d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when a regime transition occurred within last 21 bars."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).max().fillna(0.0).diff().diff()

def f20_vdah_582_log_vol_regime_volatility_index_252d_d2(volume: pd.Series) -> pd.Series:
    """Std of log-vol regime labels over 252d — higher = more flipping."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return label.rolling(YDAYS, min_periods=QDAYS).std().diff().diff()

def f20_vdah_583_log_vol_regime_max_run_length_252d_d2(volume: pd.Series) -> pd.Series:
    """Max run length of single regime label over trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    same = label == label.shift(1)
    return _consecutive_true_streak(same).astype(float).rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f20_vdah_584_log_vol_regime_low_persistence_252d_d2(volume: pd.Series) -> pd.Series:
    """Max consec-bar run in low-vol regime (z<-0.5), trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return _consecutive_true_streak(z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f20_vdah_585_log_vol_regime_high_persistence_252d_d2(volume: pd.Series) -> pd.Series:
    """Max consec-bar run in high-vol regime (z>+0.5), trailing 252d."""
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return _consecutive_true_streak(z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f20_vdah_586_vol_ema21_minus_ema63_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (EMA21(vol) - EMA63(vol)) — short vs medium vol divergence."""
    ema21 = volume.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    ema63 = volume.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    return _rolling_zscore(ema21 - ema63, YDAYS).diff().diff()

def f20_vdah_587_vol_ema63_minus_ema252_zscore_252d_d2(volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (EMA63(vol) - EMA252(vol))."""
    ema63 = volume.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    ema252 = volume.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()
    return _rolling_zscore(ema63 - ema252, YDAYS).diff().diff()

def f20_vdah_588_vol_pulse_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when vol > 3 × max(vol, prior 3 bars) — sudden lone pulse."""
    rmax3 = volume.shift(1).rolling(3, min_periods=1).max()
    return (volume > 3.0 * rmax3).astype(float).diff().diff()

def f20_vdah_589_vol_pulse_count_63d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 63d count of vol-pulse events."""
    rmax3 = volume.shift(1).rolling(3, min_periods=1).max()
    return (volume > 3.0 * rmax3).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f20_vdah_590_vol_pulse_then_dryup_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when pulse occurred 5 bars ago AND last 5 bars all had vol < 21d median."""
    rmax3 = volume.shift(1).rolling(3, min_periods=1).max()
    pulse_5d_ago = (volume > 3.0 * rmax3).shift(5).fillna(False)
    med21 = volume.rolling(MDAYS, min_periods=WDAYS).median()
    silent5 = (volume < med21) & (volume.shift(1) < med21.shift(1)) & (volume.shift(2) < med21.shift(2)) & (volume.shift(3) < med21.shift(3)) & (volume.shift(4) < med21.shift(4))
    return (pulse_5d_ago & silent5).astype(float).diff().diff()

def f20_vdah_591_vol_at_lowest_5pct_of_5y_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when vol in bottom 5% of trailing 5y distribution."""
    q05 = volume.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.05)
    return (volume <= q05).astype(float).diff().diff()

def f20_vdah_592_vol_at_lowest_1pct_of_5y_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when vol in bottom 1% of trailing 5y distribution — extreme dryup."""
    q01 = volume.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.01)
    return (volume <= q01).astype(float).diff().diff()

def f20_vdah_593_vol_bars_since_top_decile_252d_d2(volume: pd.Series) -> pd.Series:
    """Bars since vol last reached top decile of 252d distribution."""
    q90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (volume >= q90).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS)).diff().diff()

def f20_vdah_594_vol_bars_since_bottom_decile_252d_d2(volume: pd.Series) -> pd.Series:
    """Bars since vol last reached bottom decile of 252d distribution."""
    q10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    flag = (volume <= q10).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS)).diff().diff()

def f20_vdah_595_vol_total_252d_to_5y_ratio_d2(volume: pd.Series) -> pd.Series:
    """(252d sum of vol) / (5y sum of vol × 252/1260) — relative-trailing-volume ratio."""
    s252 = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    s5y = volume.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return _safe_div(s252, s5y * (YDAYS / float(DDAYS_5Y))).diff().diff()

def f20_vdah_596_vol_decay_score_5d_within_21d_d2(volume: pd.Series) -> pd.Series:
    """(5d vol mean) / (21d vol mean) − 1, gated to bars where 21d mean is itself below 252d mean."""
    m5 = volume.rolling(WDAYS, min_periods=2).mean()
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    ratio = _safe_div(m5, m21) - 1.0
    return ratio.where(m21 < m252, np.nan).diff().diff()

def f20_vdah_597_vol_decay_score_21d_within_252d_d2(volume: pd.Series) -> pd.Series:
    """(21d vol mean) / (252d vol mean) − 1."""
    m21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(m21, m252) - 1.0).diff().diff()

def f20_vdah_598_vol_dryup_severity_index_252d_d2(volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (1 - vol/(252d-median-vol))+ — total dryup magnitude."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    deficit = (1.0 - _safe_div(volume, med)).clip(lower=0.0)
    return deficit.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f20_vdah_599_vol_dryup_pct_rank_252d_d2(volume: pd.Series) -> pd.Series:
    """Pct rank(252d) of trailing 21d vol mean — quick scan of recent vol regime."""
    return volume.rolling(MDAYS, min_periods=WDAYS).mean().rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff().diff()

def f20_vdah_600_vol_5d_streak_below_q25_252d_indicator_d2(volume: pd.Series) -> pd.Series:
    """1 when ALL last 5 bars had vol below q25 of trailing 252d."""
    q25 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    cond = volume < q25
    return (cond & cond.shift(1) & cond.shift(2) & cond.shift(3) & cond.shift(4)).astype(float).diff().diff()
VOLUME_DRYUP_AT_HIGH_D2_REGISTRY_526_600 = {'f20_vdah_526_log_vol_rsi_14d_d2': {'inputs': ['volume'], 'func': f20_vdah_526_log_vol_rsi_14d_d2}, 'f20_vdah_527_log_vol_rsi_21d_d2': {'inputs': ['volume'], 'func': f20_vdah_527_log_vol_rsi_21d_d2}, 'f20_vdah_528_log_vol_rsi_63d_d2': {'inputs': ['volume'], 'func': f20_vdah_528_log_vol_rsi_63d_d2}, 'f20_vdah_529_log_vol_cci_20d_d2': {'inputs': ['volume'], 'func': f20_vdah_529_log_vol_cci_20d_d2}, 'f20_vdah_530_log_vol_cci_40d_d2': {'inputs': ['volume'], 'func': f20_vdah_530_log_vol_cci_40d_d2}, 'f20_vdah_531_log_vol_stoch_k_14d_d2': {'inputs': ['volume'], 'func': f20_vdah_531_log_vol_stoch_k_14d_d2}, 'f20_vdah_532_log_vol_stoch_k_63d_d2': {'inputs': ['volume'], 'func': f20_vdah_532_log_vol_stoch_k_63d_d2}, 'f20_vdah_533_log_vol_williams_r_14d_d2': {'inputs': ['volume'], 'func': f20_vdah_533_log_vol_williams_r_14d_d2}, 'f20_vdah_534_log_vol_trix_15d_d2': {'inputs': ['volume'], 'func': f20_vdah_534_log_vol_trix_15d_d2}, 'f20_vdah_535_log_vol_roc_5d_d2': {'inputs': ['volume'], 'func': f20_vdah_535_log_vol_roc_5d_d2}, 'f20_vdah_536_log_vol_roc_21d_d2': {'inputs': ['volume'], 'func': f20_vdah_536_log_vol_roc_21d_d2}, 'f20_vdah_537_log_vol_roc_63d_d2': {'inputs': ['volume'], 'func': f20_vdah_537_log_vol_roc_63d_d2}, 'f20_vdah_538_log_vol_ma_cross_21_63_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_538_log_vol_ma_cross_21_63_indicator_d2}, 'f20_vdah_539_log_vol_ma_cross_21_63_event_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_539_log_vol_ma_cross_21_63_event_indicator_d2}, 'f20_vdah_540_log_vol_ma_distance_21_zscore_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_540_log_vol_ma_distance_21_zscore_252d_d2}, 'f20_vdah_541_log_vol_macd_line_12_26_d2': {'inputs': ['volume'], 'func': f20_vdah_541_log_vol_macd_line_12_26_d2}, 'f20_vdah_542_log_vol_macd_signal_12_26_9_d2': {'inputs': ['volume'], 'func': f20_vdah_542_log_vol_macd_signal_12_26_9_d2}, 'f20_vdah_543_log_vol_macd_histogram_d2': {'inputs': ['volume'], 'func': f20_vdah_543_log_vol_macd_histogram_d2}, 'f20_vdah_544_log_vol_macd_hist_zerocross_count_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_544_log_vol_macd_hist_zerocross_count_252d_d2}, 'f20_vdah_545_log_vol_momentum_3d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_545_log_vol_momentum_3d_indicator_d2}, 'f20_vdah_546_log_vol_momentum_5d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_546_log_vol_momentum_5d_indicator_d2}, 'f20_vdah_547_log_vol_neg_momentum_3d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_547_log_vol_neg_momentum_3d_indicator_d2}, 'f20_vdah_548_log_vol_neg_momentum_5d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_548_log_vol_neg_momentum_5d_indicator_d2}, 'f20_vdah_549_log_vol_thrust_4_of_5_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_549_log_vol_thrust_4_of_5_indicator_d2}, 'f20_vdah_550_log_vol_thrust_5_of_5_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_550_log_vol_thrust_5_of_5_indicator_d2}, 'f20_vdah_551_log_vol_first_pos_after_neg_streak_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_551_log_vol_first_pos_after_neg_streak_indicator_d2}, 'f20_vdah_552_log_vol_first_neg_after_pos_streak_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_552_log_vol_first_neg_after_pos_streak_indicator_d2}, 'f20_vdah_553_log_vol_5d_change_zscore_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_553_log_vol_5d_change_zscore_252d_d2}, 'f20_vdah_554_log_vol_21d_change_zscore_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_554_log_vol_21d_change_zscore_252d_d2}, 'f20_vdah_555_log_vol_63d_change_zscore_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_555_log_vol_63d_change_zscore_252d_d2}, 'f20_vdah_556_vol_up_price_down_indicator_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_556_vol_up_price_down_indicator_d2}, 'f20_vdah_557_vol_up_price_down_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_557_vol_up_price_down_count_21d_d2}, 'f20_vdah_558_vol_up_price_down_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_558_vol_up_price_down_count_63d_d2}, 'f20_vdah_559_vol_down_price_up_indicator_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_559_vol_down_price_up_indicator_d2}, 'f20_vdah_560_vol_down_price_up_count_21d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_560_vol_down_price_up_count_21d_d2}, 'f20_vdah_561_vol_down_price_up_count_63d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_561_vol_down_price_up_count_63d_d2}, 'f20_vdah_562_vol_up_price_down_to_vol_up_price_up_ratio_252d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_562_vol_up_price_down_to_vol_up_price_up_ratio_252d_d2}, 'f20_vdah_563_vol_down_with_close_at_252d_high_indicator_d2': {'inputs': ['high', 'volume'], 'func': f20_vdah_563_vol_down_with_close_at_252d_high_indicator_d2}, 'f20_vdah_564_vol_down_with_close_at_252d_high_count_252d_d2': {'inputs': ['high', 'volume'], 'func': f20_vdah_564_vol_down_with_close_at_252d_high_count_252d_d2}, 'f20_vdah_565_vol_at_inside_day_vs_outside_day_ratio_252d_d2': {'inputs': ['high', 'low', 'volume'], 'func': f20_vdah_565_vol_at_inside_day_vs_outside_day_ratio_252d_d2}, 'f20_vdah_566_vol_at_doji_to_overall_vol_ratio_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_566_vol_at_doji_to_overall_vol_ratio_252d_d2}, 'f20_vdah_567_vol_at_close_above_high_5d_ago_indicator_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_567_vol_at_close_above_high_5d_ago_indicator_d2}, 'f20_vdah_568_vol_when_close_pct_gt_2pct_252d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_568_vol_when_close_pct_gt_2pct_252d_d2}, 'f20_vdah_569_vol_when_close_pct_lt_neg2pct_252d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_569_vol_when_close_pct_lt_neg2pct_252d_d2}, 'f20_vdah_570_vol_extreme_move_asymmetry_252d_d2': {'inputs': ['close', 'volume'], 'func': f20_vdah_570_vol_extreme_move_asymmetry_252d_d2}, 'f20_vdah_571_log_vol_3state_regime_label_d2': {'inputs': ['volume'], 'func': f20_vdah_571_log_vol_3state_regime_label_d2}, 'f20_vdah_572_log_vol_regime_high_dwell_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_572_log_vol_regime_high_dwell_252d_d2}, 'f20_vdah_573_log_vol_regime_low_dwell_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_573_log_vol_regime_low_dwell_252d_d2}, 'f20_vdah_574_log_vol_regime_transitions_count_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_574_log_vol_regime_transitions_count_252d_d2}, 'f20_vdah_575_log_vol_regime_current_age_d2': {'inputs': ['volume'], 'func': f20_vdah_575_log_vol_regime_current_age_d2}, 'f20_vdah_576_log_vol_regime_high_to_low_transition_count_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_576_log_vol_regime_high_to_low_transition_count_252d_d2}, 'f20_vdah_577_log_vol_regime_low_to_high_transition_count_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_577_log_vol_regime_low_to_high_transition_count_252d_d2}, 'f20_vdah_578_log_vol_regime_persistence_mean_run_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_578_log_vol_regime_persistence_mean_run_252d_d2}, 'f20_vdah_579_log_vol_at_regime_transition_event_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_579_log_vol_at_regime_transition_event_indicator_d2}, 'f20_vdah_580_log_vol_recently_transitioned_5d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_580_log_vol_recently_transitioned_5d_indicator_d2}, 'f20_vdah_581_log_vol_recently_transitioned_21d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_581_log_vol_recently_transitioned_21d_indicator_d2}, 'f20_vdah_582_log_vol_regime_volatility_index_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_582_log_vol_regime_volatility_index_252d_d2}, 'f20_vdah_583_log_vol_regime_max_run_length_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_583_log_vol_regime_max_run_length_252d_d2}, 'f20_vdah_584_log_vol_regime_low_persistence_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_584_log_vol_regime_low_persistence_252d_d2}, 'f20_vdah_585_log_vol_regime_high_persistence_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_585_log_vol_regime_high_persistence_252d_d2}, 'f20_vdah_586_vol_ema21_minus_ema63_zscore_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_586_vol_ema21_minus_ema63_zscore_252d_d2}, 'f20_vdah_587_vol_ema63_minus_ema252_zscore_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_587_vol_ema63_minus_ema252_zscore_252d_d2}, 'f20_vdah_588_vol_pulse_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_588_vol_pulse_indicator_d2}, 'f20_vdah_589_vol_pulse_count_63d_d2': {'inputs': ['volume'], 'func': f20_vdah_589_vol_pulse_count_63d_d2}, 'f20_vdah_590_vol_pulse_then_dryup_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_590_vol_pulse_then_dryup_indicator_d2}, 'f20_vdah_591_vol_at_lowest_5pct_of_5y_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_591_vol_at_lowest_5pct_of_5y_indicator_d2}, 'f20_vdah_592_vol_at_lowest_1pct_of_5y_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_592_vol_at_lowest_1pct_of_5y_indicator_d2}, 'f20_vdah_593_vol_bars_since_top_decile_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_593_vol_bars_since_top_decile_252d_d2}, 'f20_vdah_594_vol_bars_since_bottom_decile_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_594_vol_bars_since_bottom_decile_252d_d2}, 'f20_vdah_595_vol_total_252d_to_5y_ratio_d2': {'inputs': ['volume'], 'func': f20_vdah_595_vol_total_252d_to_5y_ratio_d2}, 'f20_vdah_596_vol_decay_score_5d_within_21d_d2': {'inputs': ['volume'], 'func': f20_vdah_596_vol_decay_score_5d_within_21d_d2}, 'f20_vdah_597_vol_decay_score_21d_within_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_597_vol_decay_score_21d_within_252d_d2}, 'f20_vdah_598_vol_dryup_severity_index_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_598_vol_dryup_severity_index_252d_d2}, 'f20_vdah_599_vol_dryup_pct_rank_252d_d2': {'inputs': ['volume'], 'func': f20_vdah_599_vol_dryup_pct_rank_252d_d2}, 'f20_vdah_600_vol_5d_streak_below_q25_252d_indicator_d2': {'inputs': ['volume'], 'func': f20_vdah_600_vol_5d_streak_below_q25_252d_indicator_d2}}