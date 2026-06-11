"""22_on_balance_volume_dynamics d1 features 526-600 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _obv(close, volume):
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()

def _rsi(s, n):
    d = s.diff()
    g = d.clip(lower=0.0)
    l = (-d).clip(lower=0.0)
    ag = g.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    al = l.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    return 100.0 * _safe_div(ag, ag + al)

def f22_obvd_526_obv_rsi_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(63) on OBV — quarterly OBV momentum oscillator."""
    return _rsi(_obv(close, volume), QDAYS).diff()

def f22_obvd_527_obv_cci_20d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI(20) on OBV."""
    obv = _obv(close, volume)
    sma = obv.rolling(20, min_periods=10).mean()
    mad = (obv - sma).abs().rolling(20, min_periods=10).mean()
    return _safe_div(obv - sma, 0.015 * mad).diff()

def f22_obvd_528_obv_cci_40d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI(40) on OBV."""
    obv = _obv(close, volume)
    sma = obv.rolling(40, min_periods=15).mean()
    mad = (obv - sma).abs().rolling(40, min_periods=15).mean()
    return _safe_div(obv - sma, 0.015 * mad).diff()

def f22_obvd_529_obv_cci_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CCI(63) on OBV."""
    obv = _obv(close, volume)
    sma = obv.rolling(QDAYS, min_periods=MDAYS).mean()
    mad = (obv - sma).abs().rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(obv - sma, 0.015 * mad).diff()

def f22_obvd_530_obv_stoch_d_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stochastic %D(63, 3) on OBV — slow stoch smoothed."""
    obv = _obv(close, volume)
    rmax = obv.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = obv.rolling(QDAYS, min_periods=MDAYS).min()
    k = 100.0 * _safe_div(obv - rmin, rmax - rmin)
    return k.rolling(3, min_periods=2).mean().diff()

def f22_obvd_531_obv_williams_r_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams %R(21) on OBV."""
    obv = _obv(close, volume)
    rmax = obv.rolling(MDAYS, min_periods=WDAYS).max()
    rmin = obv.rolling(MDAYS, min_periods=WDAYS).min()
    return (-100.0 * _safe_div(rmax - obv, rmax - rmin)).diff()

def f22_obvd_532_obv_williams_r_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Williams %R(63) on OBV."""
    obv = _obv(close, volume)
    rmax = obv.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = obv.rolling(QDAYS, min_periods=MDAYS).min()
    return (-100.0 * _safe_div(rmax - obv, rmax - rmin)).diff()

def f22_obvd_533_obv_trix_15d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TRIX(15) on OBV."""
    obv = _obv(close, volume)
    e1 = obv.ewm(span=15, min_periods=5, adjust=False).mean()
    e2 = e1.ewm(span=15, min_periods=5, adjust=False).mean()
    e3 = e2.ewm(span=15, min_periods=5, adjust=False).mean()
    return e3.pct_change().diff()

def f22_obvd_534_obv_trix_30d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """TRIX(30) on OBV."""
    obv = _obv(close, volume)
    e1 = obv.ewm(span=30, min_periods=10, adjust=False).mean()
    e2 = e1.ewm(span=30, min_periods=10, adjust=False).mean()
    e3 = e2.ewm(span=30, min_periods=10, adjust=False).mean()
    return e3.pct_change().diff()

def f22_obvd_535_obv_roc_3d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3d OBV ROC."""
    obv = _obv(close, volume)
    return (obv - obv.shift(3)).diff()

def f22_obvd_536_obv_roc_8d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """8d OBV ROC."""
    obv = _obv(close, volume)
    return (obv - obv.shift(8)).diff()

def f22_obvd_537_obv_roc_13d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """13d OBV ROC."""
    obv = _obv(close, volume)
    return (obv - obv.shift(13)).diff()

def f22_obvd_538_obv_roc_34d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """34d OBV ROC."""
    obv = _obv(close, volume)
    return (obv - obv.shift(34)).diff()

def f22_obvd_539_obv_roc_55d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """55d OBV ROC."""
    obv = _obv(close, volume)
    return (obv - obv.shift(55)).diff()

def f22_obvd_540_obv_dema_distance_20d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV - DEMA(20, OBV); DEMA = 2*EMA - EMA(EMA)."""
    obv = _obv(close, volume)
    e1 = obv.ewm(span=20, min_periods=10, adjust=False).mean()
    e2 = e1.ewm(span=20, min_periods=10, adjust=False).mean()
    dema = 2.0 * e1 - e2
    return (obv - dema).diff()

def f22_obvd_541_obv_kama_distance_20d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV - KAMA-like adaptive smoothing(20). Simplified: SMA(20) but weighted by efficiency-ratio."""
    obv = _obv(close, volume)
    direct = (obv - obv.shift(20)).abs()
    vol_sum = obv.diff().abs().rolling(20, min_periods=10).sum()
    er = _safe_div(direct, vol_sum)
    sc = (er * (2.0 / (2.0 + 1.0) - 2.0 / (30.0 + 1.0)) + 2.0 / (30.0 + 1.0)) ** 2
    sma = obv.rolling(20, min_periods=10).mean()
    kama_proxy = sma * sc + obv * (1.0 - sc)
    return (obv - kama_proxy).diff()

def f22_obvd_542_obv_hull_ma_distance_20d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV - Hull MA proxy(20)."""
    obv = _obv(close, volume)
    wma10 = obv.rolling(10, min_periods=5).apply(lambda x: np.average(x[~np.isnan(x)], weights=np.arange(1, len(x[~np.isnan(x)]) + 1)) if (~np.isnan(x)).sum() > 0 else np.nan, raw=True)
    wma20 = obv.rolling(20, min_periods=10).apply(lambda x: np.average(x[~np.isnan(x)], weights=np.arange(1, len(x[~np.isnan(x)]) + 1)) if (~np.isnan(x)).sum() > 0 else np.nan, raw=True)
    raw = 2.0 * wma10 - wma20
    sqrt_n = int(np.sqrt(20))
    hma = raw.rolling(sqrt_n, min_periods=2).apply(lambda x: np.average(x[~np.isnan(x)], weights=np.arange(1, len(x[~np.isnan(x)]) + 1)) if (~np.isnan(x)).sum() > 0 else np.nan, raw=True)
    return (obv - hma).diff()

def f22_obvd_543_obv_tsi_25_13_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """True Strength Index(25,13) on OBV: 100 * EMA13(EMA25(diff)) / EMA13(EMA25(|diff|))."""
    obv = _obv(close, volume)
    d = obv.diff()
    num = d.ewm(span=25, min_periods=10, adjust=False).mean().ewm(span=13, min_periods=5, adjust=False).mean()
    den = d.abs().ewm(span=25, min_periods=10, adjust=False).mean().ewm(span=13, min_periods=5, adjust=False).mean()
    return (100.0 * _safe_div(num, den)).diff()

def f22_obvd_544_obv_dpo_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Detrended Price Oscillator on OBV(21): OBV - SMA21(OBV shifted)."""
    obv = _obv(close, volume)
    sma21 = obv.rolling(MDAYS, min_periods=WDAYS).mean().shift(int(MDAYS / 2) + 1)
    return (obv - sma21).diff()

def f22_obvd_545_obv_chaikin_proxy_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin-style oscillator proxy on OBV: EMA3(OBV) - EMA10(OBV)."""
    obv = _obv(close, volume)
    return (obv.ewm(span=3, min_periods=2, adjust=False).mean() - obv.ewm(span=10, min_periods=4, adjust=False).mean()).diff()

def f22_obvd_546_obv_thrust_8_of_10_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 8+ of last 10 bars had OBV-diff > 0."""
    obv = _obv(close, volume)
    return ((obv.diff() > 0).astype(float).rolling(10, min_periods=3).sum() >= 8).astype(float).diff()

def f22_obvd_547_obv_thrust_10_of_10_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when all 10 of last 10 bars had OBV-diff > 0."""
    obv = _obv(close, volume)
    return ((obv.diff() > 0).astype(float).rolling(10, min_periods=3).sum() >= 10).astype(float).diff()

def f22_obvd_548_obv_thrust_8_of_10_neg_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 8+ of last 10 bars had OBV-diff < 0."""
    obv = _obv(close, volume)
    return ((obv.diff() < 0).astype(float).rolling(10, min_periods=3).sum() >= 8).astype(float).diff()

def f22_obvd_549_obv_2sigma_burst_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when |OBV-diff z(252d)| > 2 — single-bar OBV shock."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z.abs() > 2.0).astype(float).diff()

def f22_obvd_550_obv_3sigma_burst_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when |OBV-diff z(252d)| > 3 — extreme single-bar."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z.abs() > 3.0).astype(float).diff()

def f22_obvd_551_obv_2sigma_positive_burst_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-diff z > 2 (positive shock)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_552_obv_2sigma_negative_burst_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-diff z < -2 (negative shock)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z < -2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_553_obv_burst_imbalance_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(count OBV-diff z>2) − (count OBV-diff z<-2) over 252d."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    pos = (z > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    neg = (z < -2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (pos - neg).diff()

def f22_obvd_554_obv_5d_thrust_index_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of trailing 5d sum of OBV-diff."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv.diff().rolling(WDAYS, min_periods=2).sum(), YDAYS).diff()

def f22_obvd_555_obv_21d_thrust_index_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of trailing 21d sum of OBV-diff."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv.diff().rolling(MDAYS, min_periods=WDAYS).sum(), YDAYS).diff()

def f22_obvd_556_obv_up_price_down_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV-diff > 0 AND close < prior close (rare — vol on small up close)."""
    obv = _obv(close, volume)
    return ((obv.diff() > 0) & (close < close.shift(1))).astype(float).diff()

def f22_obvd_557_obv_down_price_up_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV-diff < 0 AND close > prior close."""
    obv = _obv(close, volume)
    return ((obv.diff() < 0) & (close > close.shift(1))).astype(float).diff()

def f22_obvd_558_obv_pos_price_pos_count_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of bars where OBV-diff > 0 AND close > prior close (confirmation)."""
    obv = _obv(close, volume)
    return ((obv.diff() > 0) & (close > close.shift(1))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f22_obvd_559_obv_neg_price_neg_count_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 21d count of bars where OBV-diff < 0 AND close < prior close (confirmation)."""
    obv = _obv(close, volume)
    return ((obv.diff() < 0) & (close < close.shift(1))).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f22_obvd_560_obv_pos_price_neg_to_pos_price_pos_ratio_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d count OBV-up & price-down) / (252d count OBV-up & price-up)."""
    obv = _obv(close, volume)
    a = ((obv.diff() > 0) & (close < close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    b = ((obv.diff() > 0) & (close > close.shift(1))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(a, b + 1.0).diff()

def f22_obvd_561_obv_diff_signal_unconfirmed_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count where sign(OBV-diff) != sign(close-diff)."""
    obv = _obv(close, volume)
    return (np.sign(obv.diff()) != np.sign(close.diff())).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_562_obv_confirmed_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count where sign(OBV-diff) == sign(close-diff)."""
    obv = _obv(close, volume)
    return (np.sign(obv.diff()) == np.sign(close.diff())).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_563_obv_confirmation_rate_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where sign(OBV-diff) == sign(close-diff)."""
    obv = _obv(close, volume)
    return (np.sign(obv.diff()) == np.sign(close.diff())).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_564_obv_diff_when_price_up_avg_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars where close > prior close, 252d."""
    obv = _obv(close, volume)
    return obv.diff().where(close > close.shift(1), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_565_obv_diff_when_price_down_avg_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars where close < prior close, 252d."""
    obv = _obv(close, volume)
    return obv.diff().where(close < close.shift(1), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_566_obv_diff_when_close_pct_gt_2pct_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars where close pct_change > 2%."""
    obv = _obv(close, volume)
    return obv.diff().where(close.pct_change() > 0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_567_obv_diff_when_close_pct_lt_neg2pct_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars where close pct_change < -2%."""
    obv = _obv(close, volume)
    return obv.diff().where(close.pct_change() < -0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_568_obv_signal_strength_index_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """|Avg OBV-diff on up-bars| / |Avg OBV-diff on down-bars| over 252d."""
    obv = _obv(close, volume)
    up = obv.diff().where(close > close.shift(1), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().abs()
    dn = obv.diff().where(close < close.shift(1), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().abs()
    return _safe_div(up, dn + 1.0).diff()

def f22_obvd_569_obv_diff_at_inside_day_to_outside_day_ratio_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on inside days / avg OBV-diff on outside days over 252d."""
    obv = _obv(close, volume)
    d = obv.diff()
    inside = (high < high.shift(1)) & (low > low.shift(1))
    outside = (high > high.shift(1)) & (low < low.shift(1))
    a = d.where(inside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    b = d.where(outside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(a, b).diff()

def f22_obvd_570_obv_extreme_move_asymmetry_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Avg OBV-diff on +2% bars) - (avg OBV-diff on -2% bars), 252d."""
    obv = _obv(close, volume)
    d = obv.diff()
    up_d = d.where(close.pct_change() > 0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn_d = d.where(close.pct_change() < -0.02, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (up_d - dn_d).diff()

def f22_obvd_571_obv_diff_3state_regime_label_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3-state regime label from OBV-diff z(252d)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0)).diff()

def f22_obvd_572_obv_diff_regime_pos_dwell_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in positive-flow regime (OBV-diff z>+0.5)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_573_obv_diff_regime_neg_dwell_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in negative-flow regime (OBV-diff z<-0.5)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f22_obvd_574_obv_diff_regime_transitions_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-diff regime transitions."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_575_obv_diff_regime_current_age_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in current OBV-diff regime."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    diff = label != label.shift(1)
    grp = diff.cumsum()
    return label.groupby(grp).cumcount().astype(float).diff()

def f22_obvd_576_obv_diff_regime_pos_to_neg_transition_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-diff positive→negative regime transitions."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == 1) & (label == -1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_577_obv_diff_regime_neg_to_pos_transition_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-diff negative→positive regime transitions."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == -1) & (label == 1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f22_obvd_578_obv_diff_recently_transitioned_5d_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when an OBV-diff regime transition occurred in last 5 bars."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(WDAYS, min_periods=1).max().fillna(0.0).diff()

def f22_obvd_579_obv_diff_recently_transitioned_21d_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when an OBV-diff regime transition occurred in last 21 bars."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).max().fillna(0.0).diff()

def f22_obvd_580_obv_diff_regime_volatility_index_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of OBV-diff regime labels over 252d."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return label.rolling(YDAYS, min_periods=QDAYS).std().diff()

def f22_obvd_581_obv_diff_regime_pos_persistence_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec-bar run in positive-flow regime, 252d."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return _consecutive_true_streak(z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).max().diff()

def f22_obvd_582_obv_diff_regime_neg_persistence_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consec-bar run in negative-flow regime, 252d."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    return _consecutive_true_streak(z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).max().diff()

def f22_obvd_583_obv_diff_pulse_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when |OBV-diff| > 3 × max(|OBV-diff|, prior 3 bars) — sudden lone pulse."""
    obv = _obv(close, volume)
    d_abs = obv.diff().abs()
    rmax3 = d_abs.shift(1).rolling(3, min_periods=1).max()
    return (d_abs > 3.0 * rmax3).astype(float).diff()

def f22_obvd_584_obv_diff_pulse_count_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of OBV-diff pulse events."""
    obv = _obv(close, volume)
    d_abs = obv.diff().abs()
    rmax3 = d_abs.shift(1).rolling(3, min_periods=1).max()
    return (d_abs > 3.0 * rmax3).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f22_obvd_585_obv_diff_pulse_then_quiet_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV-diff pulse 5 bars ago AND last 5 bars all |OBV-diff| below 21d median."""
    obv = _obv(close, volume)
    d_abs = obv.diff().abs()
    rmax3 = d_abs.shift(1).rolling(3, min_periods=1).max()
    pulse_5d_ago = (d_abs > 3.0 * rmax3).shift(5).fillna(False)
    med21 = d_abs.rolling(MDAYS, min_periods=WDAYS).median()
    quiet5 = (d_abs < med21) & (d_abs.shift(1) < med21.shift(1)) & (d_abs.shift(2) < med21.shift(2)) & (d_abs.shift(3) < med21.shift(3)) & (d_abs.shift(4) < med21.shift(4))
    return (pulse_5d_ago & quiet5).astype(float).diff()

def f22_obvd_586_obv_at_lowest_5pct_of_5y_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV in bottom 5% of 5y distribution."""
    obv = _obv(close, volume)
    q05 = obv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.05)
    return (obv <= q05).astype(float).diff()

def f22_obvd_587_obv_at_highest_5pct_of_5y_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV in top 5% of 5y distribution."""
    obv = _obv(close, volume)
    q95 = obv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.95)
    return (obv >= q95).astype(float).diff()

def f22_obvd_588_obv_bars_since_5y_max_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since OBV last reached its trailing 5y max."""
    obv = _obv(close, volume)
    rmax = obv.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    flag = (obv >= rmax).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(DDAYS_5Y)).diff()

def f22_obvd_589_obv_bars_since_5y_min_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since OBV last reached its trailing 5y min."""
    obv = _obv(close, volume)
    rmin = obv.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    flag = (obv <= rmin).astype(int)
    grp = flag.cumsum()
    bars = (~flag.astype(bool)).astype(int).groupby(grp).cumsum().astype(float)
    return bars.clip(upper=float(DDAYS_5Y)).diff()

def f22_obvd_590_obv_distance_to_5y_max_normalized_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 5y-max) / (5y-max - 5y-min) — position relative to 5y range top."""
    obv = _obv(close, volume)
    rmax = obv.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = obv.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    return _safe_div(obv - rmax, rmax - rmin).diff()

def f22_obvd_591_obv_distance_to_5y_min_normalized_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 5y-min) / (5y-max - 5y-min) — position relative to 5y range bottom."""
    obv = _obv(close, volume)
    rmax = obv.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = obv.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    return _safe_div(obv - rmin, rmax - rmin).diff()

def f22_obvd_592_obv_in_top_third_of_5y_range_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV in top third of 5y range."""
    obv = _obv(close, volume)
    rmax = obv.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = obv.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return (pos >= 0.67).astype(float).diff()

def f22_obvd_593_obv_in_bottom_third_of_5y_range_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV in bottom third of 5y range."""
    obv = _obv(close, volume)
    rmax = obv.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = obv.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(obv - rmin, rmax - rmin)
    return (pos <= 0.33).astype(float).diff()

def f22_obvd_594_obv_total_252d_to_5y_ratio_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d OBV-diff sum) / (5y OBV-diff sum × 252/1260) — relative recent flow."""
    obv = _obv(close, volume)
    d = obv.diff().abs()
    s252 = d.rolling(YDAYS, min_periods=QDAYS).sum()
    s5y = d.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return _safe_div(s252, s5y * (YDAYS / float(DDAYS_5Y))).diff()

def f22_obvd_595_obv_decay_score_21d_within_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(21d OBV-diff mean) / (252d OBV-diff mean) − 1."""
    obv = _obv(close, volume)
    d = obv.diff()
    m21 = d.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = d.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(m21, m252) - 1.0).diff()

def f22_obvd_596_obv_5d_streak_pos_252d_pct_rank_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank(252d) of trailing 5d OBV-diff sum."""
    obv = _obv(close, volume)
    return obv.diff().rolling(WDAYS, min_periods=2).sum().rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f22_obvd_597_obv_5d_streak_below_q25_252d_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when ALL last 5 bars had OBV-diff < q25 of trailing 252d."""
    obv = _obv(close, volume)
    d = obv.diff()
    q25 = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    cond = d < q25
    return (cond & cond.shift(1) & cond.shift(2) & cond.shift(3) & cond.shift(4)).astype(float).diff()

def f22_obvd_598_obv_5d_streak_above_q75_252d_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when ALL last 5 bars had OBV-diff > q75 of trailing 252d."""
    obv = _obv(close, volume)
    d = obv.diff()
    q75 = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    cond = d > q75
    return (cond & cond.shift(1) & cond.shift(2) & cond.shift(3) & cond.shift(4)).astype(float).diff()

def f22_obvd_599_obv_dispersion_recent_5_vs_63_ratio_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """std(OBV-diff, 5d) / std(OBV-diff, 63d) — short-vs-long dispersion."""
    obv = _obv(close, volume)
    d = obv.diff()
    return _safe_div(d.rolling(WDAYS, min_periods=2).std(), d.rolling(QDAYS, min_periods=MDAYS).std()).diff()

def f22_obvd_600_obv_dispersion_collapse_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when std(OBV-diff, 5d) / std(OBV-diff, 63d) < 0.5 — recent flow dispersion has collapsed."""
    obv = _obv(close, volume)
    d = obv.diff()
    return (_safe_div(d.rolling(WDAYS, min_periods=2).std(), d.rolling(QDAYS, min_periods=MDAYS).std()) < 0.5).astype(float).diff()
ON_BALANCE_VOLUME_DYNAMICS_D1_REGISTRY_526_600 = {'f22_obvd_526_obv_rsi_63d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_526_obv_rsi_63d_d1}, 'f22_obvd_527_obv_cci_20d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_527_obv_cci_20d_d1}, 'f22_obvd_528_obv_cci_40d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_528_obv_cci_40d_d1}, 'f22_obvd_529_obv_cci_63d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_529_obv_cci_63d_d1}, 'f22_obvd_530_obv_stoch_d_63d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_530_obv_stoch_d_63d_d1}, 'f22_obvd_531_obv_williams_r_21d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_531_obv_williams_r_21d_d1}, 'f22_obvd_532_obv_williams_r_63d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_532_obv_williams_r_63d_d1}, 'f22_obvd_533_obv_trix_15d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_533_obv_trix_15d_d1}, 'f22_obvd_534_obv_trix_30d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_534_obv_trix_30d_d1}, 'f22_obvd_535_obv_roc_3d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_535_obv_roc_3d_d1}, 'f22_obvd_536_obv_roc_8d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_536_obv_roc_8d_d1}, 'f22_obvd_537_obv_roc_13d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_537_obv_roc_13d_d1}, 'f22_obvd_538_obv_roc_34d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_538_obv_roc_34d_d1}, 'f22_obvd_539_obv_roc_55d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_539_obv_roc_55d_d1}, 'f22_obvd_540_obv_dema_distance_20d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_540_obv_dema_distance_20d_d1}, 'f22_obvd_541_obv_kama_distance_20d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_541_obv_kama_distance_20d_d1}, 'f22_obvd_542_obv_hull_ma_distance_20d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_542_obv_hull_ma_distance_20d_d1}, 'f22_obvd_543_obv_tsi_25_13_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_543_obv_tsi_25_13_d1}, 'f22_obvd_544_obv_dpo_21d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_544_obv_dpo_21d_d1}, 'f22_obvd_545_obv_chaikin_proxy_21d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_545_obv_chaikin_proxy_21d_d1}, 'f22_obvd_546_obv_thrust_8_of_10_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_546_obv_thrust_8_of_10_indicator_d1}, 'f22_obvd_547_obv_thrust_10_of_10_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_547_obv_thrust_10_of_10_indicator_d1}, 'f22_obvd_548_obv_thrust_8_of_10_neg_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_548_obv_thrust_8_of_10_neg_indicator_d1}, 'f22_obvd_549_obv_2sigma_burst_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_549_obv_2sigma_burst_indicator_d1}, 'f22_obvd_550_obv_3sigma_burst_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_550_obv_3sigma_burst_indicator_d1}, 'f22_obvd_551_obv_2sigma_positive_burst_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_551_obv_2sigma_positive_burst_count_252d_d1}, 'f22_obvd_552_obv_2sigma_negative_burst_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_552_obv_2sigma_negative_burst_count_252d_d1}, 'f22_obvd_553_obv_burst_imbalance_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_553_obv_burst_imbalance_252d_d1}, 'f22_obvd_554_obv_5d_thrust_index_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_554_obv_5d_thrust_index_252d_d1}, 'f22_obvd_555_obv_21d_thrust_index_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_555_obv_21d_thrust_index_252d_d1}, 'f22_obvd_556_obv_up_price_down_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_556_obv_up_price_down_indicator_d1}, 'f22_obvd_557_obv_down_price_up_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_557_obv_down_price_up_indicator_d1}, 'f22_obvd_558_obv_pos_price_pos_count_21d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_558_obv_pos_price_pos_count_21d_d1}, 'f22_obvd_559_obv_neg_price_neg_count_21d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_559_obv_neg_price_neg_count_21d_d1}, 'f22_obvd_560_obv_pos_price_neg_to_pos_price_pos_ratio_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_560_obv_pos_price_neg_to_pos_price_pos_ratio_252d_d1}, 'f22_obvd_561_obv_diff_signal_unconfirmed_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_561_obv_diff_signal_unconfirmed_count_252d_d1}, 'f22_obvd_562_obv_confirmed_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_562_obv_confirmed_count_252d_d1}, 'f22_obvd_563_obv_confirmation_rate_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_563_obv_confirmation_rate_252d_d1}, 'f22_obvd_564_obv_diff_when_price_up_avg_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_564_obv_diff_when_price_up_avg_252d_d1}, 'f22_obvd_565_obv_diff_when_price_down_avg_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_565_obv_diff_when_price_down_avg_252d_d1}, 'f22_obvd_566_obv_diff_when_close_pct_gt_2pct_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_566_obv_diff_when_close_pct_gt_2pct_252d_d1}, 'f22_obvd_567_obv_diff_when_close_pct_lt_neg2pct_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_567_obv_diff_when_close_pct_lt_neg2pct_252d_d1}, 'f22_obvd_568_obv_signal_strength_index_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_568_obv_signal_strength_index_252d_d1}, 'f22_obvd_569_obv_diff_at_inside_day_to_outside_day_ratio_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_569_obv_diff_at_inside_day_to_outside_day_ratio_252d_d1}, 'f22_obvd_570_obv_extreme_move_asymmetry_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_570_obv_extreme_move_asymmetry_252d_d1}, 'f22_obvd_571_obv_diff_3state_regime_label_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_571_obv_diff_3state_regime_label_d1}, 'f22_obvd_572_obv_diff_regime_pos_dwell_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_572_obv_diff_regime_pos_dwell_252d_d1}, 'f22_obvd_573_obv_diff_regime_neg_dwell_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_573_obv_diff_regime_neg_dwell_252d_d1}, 'f22_obvd_574_obv_diff_regime_transitions_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_574_obv_diff_regime_transitions_count_252d_d1}, 'f22_obvd_575_obv_diff_regime_current_age_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_575_obv_diff_regime_current_age_d1}, 'f22_obvd_576_obv_diff_regime_pos_to_neg_transition_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_576_obv_diff_regime_pos_to_neg_transition_count_252d_d1}, 'f22_obvd_577_obv_diff_regime_neg_to_pos_transition_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_577_obv_diff_regime_neg_to_pos_transition_count_252d_d1}, 'f22_obvd_578_obv_diff_recently_transitioned_5d_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_578_obv_diff_recently_transitioned_5d_indicator_d1}, 'f22_obvd_579_obv_diff_recently_transitioned_21d_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_579_obv_diff_recently_transitioned_21d_indicator_d1}, 'f22_obvd_580_obv_diff_regime_volatility_index_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_580_obv_diff_regime_volatility_index_252d_d1}, 'f22_obvd_581_obv_diff_regime_pos_persistence_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_581_obv_diff_regime_pos_persistence_252d_d1}, 'f22_obvd_582_obv_diff_regime_neg_persistence_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_582_obv_diff_regime_neg_persistence_252d_d1}, 'f22_obvd_583_obv_diff_pulse_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_583_obv_diff_pulse_indicator_d1}, 'f22_obvd_584_obv_diff_pulse_count_63d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_584_obv_diff_pulse_count_63d_d1}, 'f22_obvd_585_obv_diff_pulse_then_quiet_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_585_obv_diff_pulse_then_quiet_indicator_d1}, 'f22_obvd_586_obv_at_lowest_5pct_of_5y_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_586_obv_at_lowest_5pct_of_5y_indicator_d1}, 'f22_obvd_587_obv_at_highest_5pct_of_5y_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_587_obv_at_highest_5pct_of_5y_indicator_d1}, 'f22_obvd_588_obv_bars_since_5y_max_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_588_obv_bars_since_5y_max_d1}, 'f22_obvd_589_obv_bars_since_5y_min_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_589_obv_bars_since_5y_min_d1}, 'f22_obvd_590_obv_distance_to_5y_max_normalized_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_590_obv_distance_to_5y_max_normalized_d1}, 'f22_obvd_591_obv_distance_to_5y_min_normalized_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_591_obv_distance_to_5y_min_normalized_d1}, 'f22_obvd_592_obv_in_top_third_of_5y_range_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_592_obv_in_top_third_of_5y_range_indicator_d1}, 'f22_obvd_593_obv_in_bottom_third_of_5y_range_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_593_obv_in_bottom_third_of_5y_range_indicator_d1}, 'f22_obvd_594_obv_total_252d_to_5y_ratio_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_594_obv_total_252d_to_5y_ratio_d1}, 'f22_obvd_595_obv_decay_score_21d_within_252d_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_595_obv_decay_score_21d_within_252d_d1}, 'f22_obvd_596_obv_5d_streak_pos_252d_pct_rank_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_596_obv_5d_streak_pos_252d_pct_rank_d1}, 'f22_obvd_597_obv_5d_streak_below_q25_252d_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_597_obv_5d_streak_below_q25_252d_indicator_d1}, 'f22_obvd_598_obv_5d_streak_above_q75_252d_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_598_obv_5d_streak_above_q75_252d_indicator_d1}, 'f22_obvd_599_obv_dispersion_recent_5_vs_63_ratio_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_599_obv_dispersion_recent_5_vs_63_ratio_d1}, 'f22_obvd_600_obv_dispersion_collapse_indicator_d1': {'inputs': ['close', 'volume'], 'func': f22_obvd_600_obv_dispersion_collapse_indicator_d1}}