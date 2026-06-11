"""dollar_volume_intensity base features 526-600 — Pipeline 1b-technical (extension #4 cont.).

Oscillators on log-$-vol (RSI/CCI/Stoch/TRIX/ROC/Williams), $-vol momentum thrust,
$-vol-vs-price binaries, regime transitions, final practicals.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
"""
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


def _dollar_vol(close, volume):
    return (close * volume).astype(float)


def _rsi(s, n):
    d = s.diff()
    g = d.clip(lower=0.0)
    l = (-d).clip(lower=0.0)
    ag = g.ewm(alpha=1.0/n, min_periods=n, adjust=False).mean()
    al = l.ewm(alpha=1.0/n, min_periods=n, adjust=False).mean()
    return 100.0 * _safe_div(ag, ag + al)


# Bucket BG — Oscillators on log-$-vol (526-540)

def f21_dvit_526_log_dv_rsi_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(14) on log-$-vol."""
    return _rsi(_safe_log(_dollar_vol(close, volume)), 14)


def f21_dvit_527_log_dv_rsi_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(21) on log-$-vol."""
    return _rsi(_safe_log(_dollar_vol(close, volume)), MDAYS)


def f21_dvit_528_log_dv_rsi_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(63) on log-$-vol."""
    return _rsi(_safe_log(_dollar_vol(close, volume)), QDAYS)


def f21_dvit_529_log_dv_cci_20d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI(20) on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    sma = ldv.rolling(20, min_periods=10).mean()
    mad = (ldv - sma).abs().rolling(20, min_periods=10).mean()
    return _safe_div(ldv - sma, 0.015 * mad)


def f21_dvit_530_log_dv_cci_40d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI(40) on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    sma = ldv.rolling(40, min_periods=15).mean()
    mad = (ldv - sma).abs().rolling(40, min_periods=15).mean()
    return _safe_div(ldv - sma, 0.015 * mad)


def f21_dvit_531_log_dv_stoch_k_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stochastic %K(14) on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    rmax = ldv.rolling(14, min_periods=5).max()
    rmin = ldv.rolling(14, min_periods=5).min()
    return 100.0 * _safe_div(ldv - rmin, rmax - rmin)


def f21_dvit_532_log_dv_stoch_k_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stochastic %K(63) on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    rmax = ldv.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = ldv.rolling(QDAYS, min_periods=MDAYS).min()
    return 100.0 * _safe_div(ldv - rmin, rmax - rmin)


def f21_dvit_533_log_dv_williams_r_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams %R(14) on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    rmax = ldv.rolling(14, min_periods=5).max()
    rmin = ldv.rolling(14, min_periods=5).min()
    return -100.0 * _safe_div(rmax - ldv, rmax - rmin)


def f21_dvit_534_log_dv_trix_15d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TRIX(15) on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    e1 = ldv.ewm(span=15, min_periods=5, adjust=False).mean()
    e2 = e1.ewm(span=15, min_periods=5, adjust=False).mean()
    e3 = e2.ewm(span=15, min_periods=5, adjust=False).mean()
    return e3.pct_change()


def f21_dvit_535_log_dv_roc_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d rate of change of log-$-vol."""
    return _safe_log(_dollar_vol(close, volume)).diff(WDAYS)


def f21_dvit_536_log_dv_roc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d ROC of log-$-vol."""
    return _safe_log(_dollar_vol(close, volume)).diff(MDAYS)


def f21_dvit_537_log_dv_roc_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d ROC of log-$-vol."""
    return _safe_log(_dollar_vol(close, volume)).diff(QDAYS)


def f21_dvit_538_log_dv_ma_cross_21_63_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when EMA21(log_dv) > EMA63(log_dv)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return (ldv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() > ldv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()).astype(float)


def f21_dvit_539_log_dv_ma_cross_21_63_event_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when EMA21(log_dv) crosses below EMA63(log_dv) today."""
    ldv = _safe_log(_dollar_vol(close, volume))
    e21 = ldv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    e63 = ldv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    above = e21 > e63
    return ((~above) & above.shift(1).fillna(False)).astype(float)


def f21_dvit_540_log_dv_ma_distance_21_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (log_dv - EMA21(log_dv))."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _rolling_zscore(ldv - ldv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean(), YDAYS)


# Bucket BH — $-vol momentum / thrust (541-555)

def f21_dvit_541_log_dv_macd_line_12_26(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD line on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ldv.ewm(span=12, min_periods=6, adjust=False).mean() - ldv.ewm(span=26, min_periods=12, adjust=False).mean()


def f21_dvit_542_log_dv_macd_signal_12_26_9(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD signal line on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    macd = ldv.ewm(span=12, min_periods=6, adjust=False).mean() - ldv.ewm(span=26, min_periods=12, adjust=False).mean()
    return macd.ewm(span=9, min_periods=4, adjust=False).mean()


def f21_dvit_543_log_dv_macd_histogram(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MACD histogram on log-$-vol."""
    ldv = _safe_log(_dollar_vol(close, volume))
    macd = ldv.ewm(span=12, min_periods=6, adjust=False).mean() - ldv.ewm(span=26, min_periods=12, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=4, adjust=False).mean()
    return macd - signal


def f21_dvit_544_log_dv_macd_hist_zerocross_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of log-$-vol MACD histogram zero crossings."""
    ldv = _safe_log(_dollar_vol(close, volume))
    macd = ldv.ewm(span=12, min_periods=6, adjust=False).mean() - ldv.ewm(span=26, min_periods=12, adjust=False).mean()
    signal = macd.ewm(span=9, min_periods=4, adjust=False).mean()
    hist = macd - signal
    return (np.sign(hist).diff().abs() > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_545_log_dv_momentum_3d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol increased for 3 consecutive bars."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d = ldv.diff()
    return ((d > 0) & (d.shift(1) > 0) & (d.shift(2) > 0)).astype(float)


def f21_dvit_546_log_dv_momentum_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol increased for 5 consecutive bars."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d = ldv.diff()
    return ((d > 0) & (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0)).astype(float)


def f21_dvit_547_log_dv_neg_momentum_3d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol decreased for 3 consecutive bars."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d = ldv.diff()
    return ((d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0)).astype(float)


def f21_dvit_548_log_dv_neg_momentum_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol decreased for 5 consecutive bars."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d = ldv.diff()
    return ((d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0) & (d.shift(3) < 0) & (d.shift(4) < 0)).astype(float)


def f21_dvit_549_log_dv_thrust_4_of_5_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 4+ of last 5 bars had log-$-vol > prior."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ((ldv.diff() > 0).astype(float).rolling(WDAYS, min_periods=1).sum() >= 4).astype(float)


def f21_dvit_550_log_dv_thrust_5_of_5_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when all 5 of last 5 bars had log-$-vol > prior."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return ((ldv.diff() > 0).astype(float).rolling(WDAYS, min_periods=1).sum() >= 5).astype(float)


def f21_dvit_551_log_dv_first_pos_after_neg_streak_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today log-$-vol > prior AND prior 5 bars all decreasing."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d = ldv.diff()
    five_neg = (d.shift(1) < 0) & (d.shift(2) < 0) & (d.shift(3) < 0) & (d.shift(4) < 0) & (d.shift(5) < 0)
    return ((d > 0) & five_neg).astype(float)


def f21_dvit_552_log_dv_first_neg_after_pos_streak_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today log-$-vol < prior AND prior 5 bars all increasing."""
    ldv = _safe_log(_dollar_vol(close, volume))
    d = ldv.diff()
    five_pos = (d.shift(1) > 0) & (d.shift(2) > 0) & (d.shift(3) > 0) & (d.shift(4) > 0) & (d.shift(5) > 0)
    return ((d < 0) & five_pos).astype(float)


def f21_dvit_553_log_dv_5d_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of 5d log-$-vol change."""
    return _rolling_zscore(_safe_log(_dollar_vol(close, volume)).diff(WDAYS), YDAYS)


def f21_dvit_554_log_dv_21d_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of 21d log-$-vol change."""
    return _rolling_zscore(_safe_log(_dollar_vol(close, volume)).diff(MDAYS), YDAYS)


def f21_dvit_555_log_dv_63d_change_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of 63d log-$-vol change."""
    return _rolling_zscore(_safe_log(_dollar_vol(close, volume)).diff(QDAYS), YDAYS)


# Bucket BI — $-vol vs price binaries (556-570)

def f21_dvit_556_dv_up_price_down_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when $-vol > prior $-vol AND close < prior close."""
    dv = _dollar_vol(close, volume)
    return ((dv > dv.shift(1)) & (close < close.shift(1))).astype(float)


def f21_dvit_557_dv_up_price_down_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of $-vol-up-price-down events."""
    dv = _dollar_vol(close, volume)
    return ((dv > dv.shift(1)) & (close < close.shift(1))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f21_dvit_558_dv_up_price_down_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of $-vol-up-price-down events."""
    dv = _dollar_vol(close, volume)
    return ((dv > dv.shift(1)) & (close < close.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_559_dv_down_price_up_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when $-vol < prior AND close > prior close — weak rally."""
    dv = _dollar_vol(close, volume)
    return ((dv < dv.shift(1)) & (close > close.shift(1))).astype(float)


def f21_dvit_560_dv_down_price_up_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of $-vol-down-price-up events."""
    dv = _dollar_vol(close, volume)
    return ((dv < dv.shift(1)) & (close > close.shift(1))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f21_dvit_561_dv_down_price_up_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of $-vol-down-price-up events."""
    dv = _dollar_vol(close, volume)
    return ((dv < dv.shift(1)) & (close > close.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_562_dv_up_price_down_ratio_to_up_up_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d count $-vol-up-price-down) / (252d count $-vol-up-price-up)."""
    dv = _dollar_vol(close, volume)
    a = ((dv > dv.shift(1)) & (close < close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    b = ((dv > dv.shift(1)) & (close > close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(a, b + 1.0)


def f21_dvit_563_dv_down_with_close_at_252d_high_indicator(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when high at 252d max AND $-vol < prior $-vol."""
    dv = _dollar_vol(close, volume)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (dv < dv.shift(1))).astype(float)


def f21_dvit_564_dv_down_with_close_at_252d_high_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of soft-top $-vol events."""
    dv = _dollar_vol(close, volume)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= rmax) & (dv < dv.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_565_dv_at_inside_day_vs_outside_day_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on inside days / avg $-vol on outside days over 252d."""
    dv = _dollar_vol(close, volume)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    outside = (high > high.shift(1)) & (low < low.shift(1))
    av_in = dv.where(inside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    av_out = dv.where(outside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(av_in, av_out)


def f21_dvit_566_dv_at_doji_to_overall_ratio_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on doji / overall avg $-vol over 252d."""
    rng = (high - low).replace(0, np.nan)
    body = (close - close.shift(1)).abs() / rng
    dv = _dollar_vol(close, volume)
    doji_av = dv.where(body < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    overall_av = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(doji_av, overall_av)


def f21_dvit_567_dv_at_close_above_high_5d_ago_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when close > close.shift(5) AND log-$-vol z(252d) < 0 (silent recovery)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return ((close > close.shift(5)) & (z < 0)).astype(float)


def f21_dvit_568_dv_when_close_pct_gt_2pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close pct_change > 2%, over 252d."""
    dv = _dollar_vol(close, volume)
    return dv.where(close.pct_change() > 0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_569_dv_when_close_pct_lt_neg2pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close pct_change < -2%, over 252d."""
    dv = _dollar_vol(close, volume)
    return dv.where(close.pct_change() < -0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_570_dv_extreme_move_asymmetry_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Avg $-vol on +2% bars) - (avg $-vol on -2% bars), 252d."""
    dv = _dollar_vol(close, volume)
    up_dv = dv.where(close.pct_change() > 0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn_dv = dv.where(close.pct_change() < -0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return up_dv - dn_dv


# Bucket BJ — Regime transition / final practicals (571-600)

def f21_dvit_571_log_dv_3state_regime_label(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3-state regime label from log-$-vol z(252d)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0))


def f21_dvit_572_log_dv_regime_high_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in high-$-vol regime (z>+0.5)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_573_log_dv_regime_low_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in low-$-vol regime (z<-0.5)."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f21_dvit_574_log_dv_regime_transitions_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of log-$-vol regime transitions."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_575_log_dv_regime_current_age(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in current log-$-vol regime."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    diff = (label != label.shift(1))
    grp = diff.cumsum()
    return label.groupby(grp).cumcount().astype(float)


def f21_dvit_576_log_dv_regime_high_to_low_transition_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of high→low log-$-vol regime transitions."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == 1) & (label == -1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_577_log_dv_regime_low_to_high_transition_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of low→high log-$-vol regime transitions."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == -1) & (label == 1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_578_log_dv_at_regime_transition_event_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today is a log-$-vol regime transition."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float)


def f21_dvit_579_log_dv_recently_transitioned_5d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when a log-$-vol regime transition occurred in last 5 bars."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(WDAYS, min_periods=1).max().fillna(0.0)


def f21_dvit_580_log_dv_recently_transitioned_21d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when a log-$-vol regime transition occurred in last 21 bars."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).max().fillna(0.0)


def f21_dvit_581_log_dv_regime_volatility_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of regime labels over 252d — more flipping = higher."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return label.rolling(YDAYS, min_periods=QDAYS).std()


def f21_dvit_582_log_dv_regime_max_run_length_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec-bar run of single regime label over 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    same = (label == label.shift(1))
    return _consecutive_true_streak(same).astype(float).rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_583_log_dv_regime_low_persistence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec-bar run in low-$-vol regime (z<-0.5), 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return _consecutive_true_streak(z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_584_log_dv_regime_high_persistence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec-bar run in high-$-vol regime (z>+0.5), 252d."""
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return _consecutive_true_streak(z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).max()


def f21_dvit_585_dv_ema21_minus_ema63_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of EMA21($-vol) - EMA63($-vol)."""
    dv = _dollar_vol(close, volume)
    ema21 = dv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    ema63 = dv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    return _rolling_zscore(ema21 - ema63, YDAYS)


def f21_dvit_586_dv_ema63_minus_ema252_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of EMA63($-vol) - EMA252($-vol)."""
    dv = _dollar_vol(close, volume)
    ema63 = dv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean()
    ema252 = dv.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()
    return _rolling_zscore(ema63 - ema252, YDAYS)


def f21_dvit_587_dv_pulse_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when $-vol > 3 × max(prior 3 bars $-vol) — sudden lone pulse."""
    dv = _dollar_vol(close, volume)
    rmax3 = dv.shift(1).rolling(3, min_periods=1).max()
    return (dv > 3.0 * rmax3).astype(float)


def f21_dvit_588_dv_pulse_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of $-vol pulse events."""
    dv = _dollar_vol(close, volume)
    rmax3 = dv.shift(1).rolling(3, min_periods=1).max()
    return (dv > 3.0 * rmax3).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f21_dvit_589_dv_pulse_then_dryup_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when $-vol pulse 5 bars ago AND last 5 bars below 21d median."""
    dv = _dollar_vol(close, volume)
    rmax3 = dv.shift(1).rolling(3, min_periods=1).max()
    pulse_5d_ago = (dv > 3.0 * rmax3).shift(5).fillna(False)
    med21 = dv.rolling(MDAYS, min_periods=WDAYS).median()
    silent5 = (dv < med21) & (dv.shift(1) < med21.shift(1)) & (dv.shift(2) < med21.shift(2)) & (dv.shift(3) < med21.shift(3)) & (dv.shift(4) < med21.shift(4))
    return (pulse_5d_ago & silent5).astype(float)


def f21_dvit_590_dv_at_lowest_5pct_of_5y_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when $-vol in bottom 5% of 5y distribution."""
    dv = _dollar_vol(close, volume)
    q05 = dv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.05)
    return (dv <= q05).astype(float)


def f21_dvit_591_dv_at_lowest_1pct_of_5y_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when $-vol in bottom 1% of 5y distribution."""
    dv = _dollar_vol(close, volume)
    q01 = dv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.01)
    return (dv <= q01).astype(float)


def f21_dvit_592_dv_bars_since_top_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since $-vol last reached top decile of 252d."""
    dv = _dollar_vol(close, volume)
    q90 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    flag = (dv >= q90).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f21_dvit_593_dv_bars_since_bottom_decile_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since $-vol last reached bottom decile of 252d."""
    dv = _dollar_vol(close, volume)
    q10 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    flag = (dv <= q10).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(YDAYS))


def f21_dvit_594_dv_total_252d_to_5y_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d sum of $-vol) / (5y sum × 252/1260)."""
    dv = _dollar_vol(close, volume)
    s252 = dv.rolling(YDAYS, min_periods=QDAYS).sum()
    s5y = dv.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return _safe_div(s252, s5y * (YDAYS / float(DDAYS_5Y)))


def f21_dvit_595_dv_decay_score_5d_within_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(5d $-vol mean) / (21d $-vol mean) − 1, gated to when 21d < 252d mean."""
    dv = _dollar_vol(close, volume)
    m5 = dv.rolling(WDAYS, min_periods=2).mean()
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    ratio = _safe_div(m5, m21) - 1.0
    return ratio.where(m21 < m252, np.nan)


def f21_dvit_596_dv_decay_score_21d_within_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(21d $-vol mean) / (252d $-vol mean) − 1."""
    dv = _dollar_vol(close, volume)
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(m21, m252) - 1.0


def f21_dvit_597_dv_dryup_severity_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (1 - dv/(252d-median-dv))+."""
    dv = _dollar_vol(close, volume)
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    deficit = (1.0 - _safe_div(dv, med)).clip(lower=0.0)
    return deficit.rolling(YDAYS, min_periods=QDAYS).sum()


def f21_dvit_598_dv_dryup_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank(252d) of trailing 21d $-vol mean."""
    dv = _dollar_vol(close, volume)
    return dv.rolling(MDAYS, min_periods=WDAYS).mean().rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f21_dvit_599_dv_5d_streak_below_q25_252d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when ALL last 5 bars had $-vol below q25 of trailing 252d."""
    dv = _dollar_vol(close, volume)
    q25 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    cond = dv < q25
    return (cond & cond.shift(1) & cond.shift(2) & cond.shift(3) & cond.shift(4)).astype(float)


def f21_dvit_600_dv_5d_streak_above_q75_252d_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when ALL last 5 bars had $-vol above q75 of trailing 252d."""
    dv = _dollar_vol(close, volume)
    q75 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    cond = dv > q75
    return (cond & cond.shift(1) & cond.shift(2) & cond.shift(3) & cond.shift(4)).astype(float)


# ============================================================
#                         REGISTRY 526-600
# ============================================================

DOLLAR_VOLUME_INTENSITY_BASE_REGISTRY_526_600 = {
    "f21_dvit_526_log_dv_rsi_14d": {"inputs": ["close", "volume"], "func": f21_dvit_526_log_dv_rsi_14d},
    "f21_dvit_527_log_dv_rsi_21d": {"inputs": ["close", "volume"], "func": f21_dvit_527_log_dv_rsi_21d},
    "f21_dvit_528_log_dv_rsi_63d": {"inputs": ["close", "volume"], "func": f21_dvit_528_log_dv_rsi_63d},
    "f21_dvit_529_log_dv_cci_20d": {"inputs": ["close", "volume"], "func": f21_dvit_529_log_dv_cci_20d},
    "f21_dvit_530_log_dv_cci_40d": {"inputs": ["close", "volume"], "func": f21_dvit_530_log_dv_cci_40d},
    "f21_dvit_531_log_dv_stoch_k_14d": {"inputs": ["close", "volume"], "func": f21_dvit_531_log_dv_stoch_k_14d},
    "f21_dvit_532_log_dv_stoch_k_63d": {"inputs": ["close", "volume"], "func": f21_dvit_532_log_dv_stoch_k_63d},
    "f21_dvit_533_log_dv_williams_r_14d": {"inputs": ["close", "volume"], "func": f21_dvit_533_log_dv_williams_r_14d},
    "f21_dvit_534_log_dv_trix_15d": {"inputs": ["close", "volume"], "func": f21_dvit_534_log_dv_trix_15d},
    "f21_dvit_535_log_dv_roc_5d": {"inputs": ["close", "volume"], "func": f21_dvit_535_log_dv_roc_5d},
    "f21_dvit_536_log_dv_roc_21d": {"inputs": ["close", "volume"], "func": f21_dvit_536_log_dv_roc_21d},
    "f21_dvit_537_log_dv_roc_63d": {"inputs": ["close", "volume"], "func": f21_dvit_537_log_dv_roc_63d},
    "f21_dvit_538_log_dv_ma_cross_21_63_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_538_log_dv_ma_cross_21_63_indicator},
    "f21_dvit_539_log_dv_ma_cross_21_63_event_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_539_log_dv_ma_cross_21_63_event_indicator},
    "f21_dvit_540_log_dv_ma_distance_21_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_540_log_dv_ma_distance_21_zscore_252d},
    "f21_dvit_541_log_dv_macd_line_12_26": {"inputs": ["close", "volume"], "func": f21_dvit_541_log_dv_macd_line_12_26},
    "f21_dvit_542_log_dv_macd_signal_12_26_9": {"inputs": ["close", "volume"], "func": f21_dvit_542_log_dv_macd_signal_12_26_9},
    "f21_dvit_543_log_dv_macd_histogram": {"inputs": ["close", "volume"], "func": f21_dvit_543_log_dv_macd_histogram},
    "f21_dvit_544_log_dv_macd_hist_zerocross_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_544_log_dv_macd_hist_zerocross_count_252d},
    "f21_dvit_545_log_dv_momentum_3d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_545_log_dv_momentum_3d_indicator},
    "f21_dvit_546_log_dv_momentum_5d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_546_log_dv_momentum_5d_indicator},
    "f21_dvit_547_log_dv_neg_momentum_3d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_547_log_dv_neg_momentum_3d_indicator},
    "f21_dvit_548_log_dv_neg_momentum_5d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_548_log_dv_neg_momentum_5d_indicator},
    "f21_dvit_549_log_dv_thrust_4_of_5_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_549_log_dv_thrust_4_of_5_indicator},
    "f21_dvit_550_log_dv_thrust_5_of_5_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_550_log_dv_thrust_5_of_5_indicator},
    "f21_dvit_551_log_dv_first_pos_after_neg_streak_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_551_log_dv_first_pos_after_neg_streak_indicator},
    "f21_dvit_552_log_dv_first_neg_after_pos_streak_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_552_log_dv_first_neg_after_pos_streak_indicator},
    "f21_dvit_553_log_dv_5d_change_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_553_log_dv_5d_change_zscore_252d},
    "f21_dvit_554_log_dv_21d_change_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_554_log_dv_21d_change_zscore_252d},
    "f21_dvit_555_log_dv_63d_change_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_555_log_dv_63d_change_zscore_252d},
    "f21_dvit_556_dv_up_price_down_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_556_dv_up_price_down_indicator},
    "f21_dvit_557_dv_up_price_down_count_21d": {"inputs": ["close", "volume"], "func": f21_dvit_557_dv_up_price_down_count_21d},
    "f21_dvit_558_dv_up_price_down_count_63d": {"inputs": ["close", "volume"], "func": f21_dvit_558_dv_up_price_down_count_63d},
    "f21_dvit_559_dv_down_price_up_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_559_dv_down_price_up_indicator},
    "f21_dvit_560_dv_down_price_up_count_21d": {"inputs": ["close", "volume"], "func": f21_dvit_560_dv_down_price_up_count_21d},
    "f21_dvit_561_dv_down_price_up_count_63d": {"inputs": ["close", "volume"], "func": f21_dvit_561_dv_down_price_up_count_63d},
    "f21_dvit_562_dv_up_price_down_ratio_to_up_up_252d": {"inputs": ["close", "volume"], "func": f21_dvit_562_dv_up_price_down_ratio_to_up_up_252d},
    "f21_dvit_563_dv_down_with_close_at_252d_high_indicator": {"inputs": ["high", "close", "volume"], "func": f21_dvit_563_dv_down_with_close_at_252d_high_indicator},
    "f21_dvit_564_dv_down_with_close_at_252d_high_count_252d": {"inputs": ["high", "close", "volume"], "func": f21_dvit_564_dv_down_with_close_at_252d_high_count_252d},
    "f21_dvit_565_dv_at_inside_day_vs_outside_day_ratio_252d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_565_dv_at_inside_day_vs_outside_day_ratio_252d},
    "f21_dvit_566_dv_at_doji_to_overall_ratio_252d": {"inputs": ["high", "low", "close", "volume"], "func": f21_dvit_566_dv_at_doji_to_overall_ratio_252d},
    "f21_dvit_567_dv_at_close_above_high_5d_ago_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_567_dv_at_close_above_high_5d_ago_indicator},
    "f21_dvit_568_dv_when_close_pct_gt_2pct_252d": {"inputs": ["close", "volume"], "func": f21_dvit_568_dv_when_close_pct_gt_2pct_252d},
    "f21_dvit_569_dv_when_close_pct_lt_neg2pct_252d": {"inputs": ["close", "volume"], "func": f21_dvit_569_dv_when_close_pct_lt_neg2pct_252d},
    "f21_dvit_570_dv_extreme_move_asymmetry_252d": {"inputs": ["close", "volume"], "func": f21_dvit_570_dv_extreme_move_asymmetry_252d},
    "f21_dvit_571_log_dv_3state_regime_label": {"inputs": ["close", "volume"], "func": f21_dvit_571_log_dv_3state_regime_label},
    "f21_dvit_572_log_dv_regime_high_dwell_252d": {"inputs": ["close", "volume"], "func": f21_dvit_572_log_dv_regime_high_dwell_252d},
    "f21_dvit_573_log_dv_regime_low_dwell_252d": {"inputs": ["close", "volume"], "func": f21_dvit_573_log_dv_regime_low_dwell_252d},
    "f21_dvit_574_log_dv_regime_transitions_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_574_log_dv_regime_transitions_count_252d},
    "f21_dvit_575_log_dv_regime_current_age": {"inputs": ["close", "volume"], "func": f21_dvit_575_log_dv_regime_current_age},
    "f21_dvit_576_log_dv_regime_high_to_low_transition_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_576_log_dv_regime_high_to_low_transition_count_252d},
    "f21_dvit_577_log_dv_regime_low_to_high_transition_count_252d": {"inputs": ["close", "volume"], "func": f21_dvit_577_log_dv_regime_low_to_high_transition_count_252d},
    "f21_dvit_578_log_dv_at_regime_transition_event_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_578_log_dv_at_regime_transition_event_indicator},
    "f21_dvit_579_log_dv_recently_transitioned_5d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_579_log_dv_recently_transitioned_5d_indicator},
    "f21_dvit_580_log_dv_recently_transitioned_21d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_580_log_dv_recently_transitioned_21d_indicator},
    "f21_dvit_581_log_dv_regime_volatility_index_252d": {"inputs": ["close", "volume"], "func": f21_dvit_581_log_dv_regime_volatility_index_252d},
    "f21_dvit_582_log_dv_regime_max_run_length_252d": {"inputs": ["close", "volume"], "func": f21_dvit_582_log_dv_regime_max_run_length_252d},
    "f21_dvit_583_log_dv_regime_low_persistence_252d": {"inputs": ["close", "volume"], "func": f21_dvit_583_log_dv_regime_low_persistence_252d},
    "f21_dvit_584_log_dv_regime_high_persistence_252d": {"inputs": ["close", "volume"], "func": f21_dvit_584_log_dv_regime_high_persistence_252d},
    "f21_dvit_585_dv_ema21_minus_ema63_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_585_dv_ema21_minus_ema63_zscore_252d},
    "f21_dvit_586_dv_ema63_minus_ema252_zscore_252d": {"inputs": ["close", "volume"], "func": f21_dvit_586_dv_ema63_minus_ema252_zscore_252d},
    "f21_dvit_587_dv_pulse_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_587_dv_pulse_indicator},
    "f21_dvit_588_dv_pulse_count_63d": {"inputs": ["close", "volume"], "func": f21_dvit_588_dv_pulse_count_63d},
    "f21_dvit_589_dv_pulse_then_dryup_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_589_dv_pulse_then_dryup_indicator},
    "f21_dvit_590_dv_at_lowest_5pct_of_5y_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_590_dv_at_lowest_5pct_of_5y_indicator},
    "f21_dvit_591_dv_at_lowest_1pct_of_5y_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_591_dv_at_lowest_1pct_of_5y_indicator},
    "f21_dvit_592_dv_bars_since_top_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_592_dv_bars_since_top_decile_252d},
    "f21_dvit_593_dv_bars_since_bottom_decile_252d": {"inputs": ["close", "volume"], "func": f21_dvit_593_dv_bars_since_bottom_decile_252d},
    "f21_dvit_594_dv_total_252d_to_5y_ratio": {"inputs": ["close", "volume"], "func": f21_dvit_594_dv_total_252d_to_5y_ratio},
    "f21_dvit_595_dv_decay_score_5d_within_21d": {"inputs": ["close", "volume"], "func": f21_dvit_595_dv_decay_score_5d_within_21d},
    "f21_dvit_596_dv_decay_score_21d_within_252d": {"inputs": ["close", "volume"], "func": f21_dvit_596_dv_decay_score_21d_within_252d},
    "f21_dvit_597_dv_dryup_severity_index_252d": {"inputs": ["close", "volume"], "func": f21_dvit_597_dv_dryup_severity_index_252d},
    "f21_dvit_598_dv_dryup_pct_rank_252d": {"inputs": ["close", "volume"], "func": f21_dvit_598_dv_dryup_pct_rank_252d},
    "f21_dvit_599_dv_5d_streak_below_q25_252d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_599_dv_5d_streak_below_q25_252d_indicator},
    "f21_dvit_600_dv_5d_streak_above_q75_252d_indicator": {"inputs": ["close", "volume"], "func": f21_dvit_600_dv_5d_streak_above_q75_252d_indicator},
}
