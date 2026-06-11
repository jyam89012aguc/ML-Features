"""
31_oscillator_extremes — Base Features 076-150
Domain: stochastic / Williams %R style oscillator extreme readings at oversold levels
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Adds 10 canonical missing oscillators: CMO, TRIX, Fisher, PPO, KST, Coppock,
SMI, Schaff Trend Cycle, Klinger Volume Oscillator, RVI.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _stoch_k(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Raw Fast Stochastic %K over window w."""
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((close - ll) * 100.0, hh - ll)


def _williams_r(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Williams %R over window w (range -100..0; -100 = most oversold)."""
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((hh - close) * -100.0, hh - ll)


def _cci(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Commodity Channel Index over window w."""
    tp = (high + low + close) / 3.0
    tp_mean = _rolling_mean(tp, w)
    mad = tp.rolling(w, min_periods=max(1, w // 2)).apply(
        lambda x: np.mean(np.abs(x - x.mean())), raw=True
    )
    return _safe_div(tp - tp_mean, 0.015 * mad)


def _mfi(high: pd.Series, low: pd.Series, close: pd.Series,
          volume: pd.Series, w: int) -> pd.Series:
    """Money Flow Index over window w."""
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos_mf = mf.where(tp > tp.shift(1), 0.0)
    neg_mf = mf.where(tp < tp.shift(1), 0.0)
    pos_sum = _rolling_sum(pos_mf, w)
    neg_sum = _rolling_sum(neg_mf, w)
    mfr = _safe_div(pos_sum, neg_sum)
    return 100.0 - _safe_div(100.0, 1.0 + mfr)


def _stoch_rsi(close: pd.Series, rsi_w: int, stoch_w: int) -> pd.Series:
    """Stochastic RSI: stochastic applied to RSI values."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(span=rsi_w, min_periods=max(1, rsi_w // 2)).mean()
    avg_loss = loss.ewm(span=rsi_w, min_periods=max(1, rsi_w // 2)).mean()
    rs = _safe_div(avg_gain, avg_loss)
    rsi = 100.0 - _safe_div(100.0, 1.0 + rs)
    rsi_min = _rolling_min(rsi, stoch_w)
    rsi_max = _rolling_max(rsi, stoch_w)
    return _safe_div((rsi - rsi_min) * 100.0, rsi_max - rsi_min)


def _ultimate_osc(high: pd.Series, low: pd.Series, close: pd.Series,
                  w1: int = 7, w2: int = 14, w3: int = 28) -> pd.Series:
    """Ultimate Oscillator with three periods."""
    prev_close = close.shift(1)
    tr = pd.concat([high - low,
                    (high - prev_close).abs(),
                    (low - prev_close).abs()], axis=1).max(axis=1)
    bp = close - pd.concat([low, prev_close], axis=1).min(axis=1)
    avg1 = _safe_div(_rolling_sum(bp, w1), _rolling_sum(tr, w1))
    avg2 = _safe_div(_rolling_sum(bp, w2), _rolling_sum(tr, w2))
    avg3 = _safe_div(_rolling_sum(bp, w3), _rolling_sum(tr, w3))
    return (4.0 * avg1 + 2.0 * avg2 + avg3) / 7.0 * 100.0


def _awesome_osc(high: pd.Series, low: pd.Series, w_fast: int = 5, w_slow: int = 34) -> pd.Series:
    """Awesome Oscillator: midpoint SMA fast minus midpoint SMA slow."""
    midpoint = (high + low) / 2.0
    return _rolling_mean(midpoint, w_fast) - _rolling_mean(midpoint, w_slow)


def _aroon_down(low: pd.Series, w: int) -> pd.Series:
    """Aroon Down: how long since w-period low."""
    def _periods_since_min(x):
        return float(w - np.argmin(x))
    return low.rolling(w + 1, min_periods=max(2, w // 2)).apply(
        _periods_since_min, raw=True
    ) / w * 100.0


# ── New canonical oscillator helpers ─────────────────────────────────────────

def _cmo(close: pd.Series, n: int) -> pd.Series:
    """Chande Momentum Oscillator: 100*(sumUp - sumDown)/(sumUp + sumDown) over n."""
    delta = close.diff(1)
    up = delta.clip(lower=0.0)
    dn = (-delta).clip(lower=0.0)
    sum_up = _rolling_sum(up, n)
    sum_dn = _rolling_sum(dn, n)
    return _safe_div(100.0 * (sum_up - sum_dn), sum_up + sum_dn)


def _trix(close: pd.Series, n: int) -> pd.Series:
    """TRIX: 1-period % ROC of triple-EMA of log(close)."""
    log_c = np.log(close.replace(0, np.nan))
    ema1 = _ewm_mean(log_c, n)
    ema2 = _ewm_mean(ema1, n)
    ema3 = _ewm_mean(ema2, n)
    return _safe_div(ema3 - ema3.shift(1), ema3.shift(1)) * 100.0


def _fisher_transform(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    """Fisher Transform: normalize price to [-1,1] then apply log transform."""
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    rng = (hh - ll).replace(0, np.nan)
    val = 2.0 * ((close - ll) / rng) - 1.0
    # clip to avoid log singularity
    val = val.clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + val) / (1.0 - val))


def _ppo(close: pd.Series, fast: int = 12, slow: int = 26, sig: int = 9) -> pd.Series:
    """Percentage Price Oscillator: (EMA_fast - EMA_slow)/EMA_slow * 100."""
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    return _safe_div((ema_f - ema_s), ema_s) * 100.0


def _ppo_signal(close: pd.Series, fast: int = 12, slow: int = 26, sig: int = 9) -> pd.Series:
    """PPO signal line: EMA(sig) of PPO."""
    return _ewm_mean(_ppo(close, fast, slow, sig), sig)


def _roc(close: pd.Series, n: int) -> pd.Series:
    """Rate of change: (close/close[n] - 1) * 100."""
    return _safe_div(close - close.shift(n), close.shift(n)) * 100.0


def _kst(close: pd.Series) -> pd.Series:
    """KST: weighted sum of 4 SMA-smoothed ROCs."""
    r1 = _rolling_mean(_roc(close, 10), 10)
    r2 = _rolling_mean(_roc(close, 15), 10)
    r3 = _rolling_mean(_roc(close, 20), 10)
    r4 = _rolling_mean(_roc(close, 30), 15)
    return r1 * 1.0 + r2 * 2.0 + r3 * 3.0 + r4 * 4.0


def _coppock(close: pd.Series) -> pd.Series:
    """Coppock Curve: WMA(10) of (ROC(14) + ROC(11))."""
    combined = _roc(close, 14) + _roc(close, 11)
    # Weighted moving average: weights 1..10
    w = 10
    weights = np.arange(1, w + 1, dtype=float)
    total_w = weights.sum()
    def _wma(x):
        if len(x) < w // 2:
            return np.nan
        wts = weights[-len(x):]
        return float(np.dot(x, wts) / wts.sum())
    return combined.rolling(w, min_periods=max(1, w // 2)).apply(_wma, raw=True)


def _smi(high: pd.Series, low: pd.Series, close: pd.Series, n: int,
         smooth1: int = 3, smooth2: int = 3) -> pd.Series:
    """Stochastic Momentum Index: double-EMA-smoothed deviation / half-range * 100."""
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    midpoint = (hh + ll) / 2.0
    diff = close - midpoint
    half_range = (hh - ll) / 2.0
    diff_sm = _ewm_mean(_ewm_mean(diff, smooth1), smooth2)
    range_sm = _ewm_mean(_ewm_mean(half_range, smooth1), smooth2)
    return _safe_div(diff_sm, range_sm) * 100.0


def _schaff_trend_cycle(close: pd.Series, fast: int = 23, slow: int = 50,
                        cycle: int = 10) -> pd.Series:
    """Schaff Trend Cycle: stochastic of MACD applied twice."""
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    macd = ema_f - ema_s
    # First stochastic on MACD
    m_min = _rolling_min(macd, cycle)
    m_max = _rolling_max(macd, cycle)
    stoch1 = _safe_div((macd - m_min) * 100.0, m_max - m_min)
    f1 = _ewm_mean(stoch1, 2)
    # Second stochastic
    f1_min = _rolling_min(f1, cycle)
    f1_max = _rolling_max(f1, cycle)
    stoch2 = _safe_div((f1 - f1_min) * 100.0, f1_max - f1_min)
    return _ewm_mean(stoch2, 2)


def _klinger_vf(high: pd.Series, low: pd.Series, close: pd.Series,
                volume: pd.Series) -> pd.Series:
    """Klinger volume force series."""
    tp = high + low + close
    tp_prev = tp.shift(1)
    dm = high - low
    dm_prev = _rolling_mean(dm, 2).shift(0)  # avoid zero-div
    cm_series = pd.Series(np.nan, index=close.index)
    # trending: +1 if tp > tp_prev else -1
    trend = pd.Series(np.where(tp > tp_prev, 1.0, -1.0), index=close.index)
    sv = volume * trend * 2.0 * _safe_div(dm, (high - low).replace(0, np.nan))
    return sv


def _klinger(high: pd.Series, low: pd.Series, close: pd.Series,
             volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator: EMA(34) - EMA(55) of volume force."""
    vf = _klinger_vf(high, low, close, volume)
    return _ewm_mean(vf, 34) - _ewm_mean(vf, 55)


def _rvi(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series,
         n: int = 10) -> pd.Series:
    """Relative Vigor Index: smoothed (close-open)/(high-low)."""
    num = close - open_
    den = high - low
    # Symmetric 4-bar weighted sum
    def _sym4(s: pd.Series) -> pd.Series:
        return (s + 2.0 * s.shift(1) + 2.0 * s.shift(2) + s.shift(3)) / 6.0
    num_sm = _sym4(num)
    den_sm = _sym4(den)
    ratio = _safe_div(num_sm, den_sm.replace(0, np.nan))
    return _rolling_mean(ratio, n)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Time spent in oversold zones (count over window) ---

def osc_076_stoch_k_14_oversold_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with 14-day Stochastic %K < 20 in trailing 21 days."""
    return _rolling_count_true(_stoch_k(high, low, close, 14) < 20.0, _TD_MON)


def osc_077_stoch_k_14_oversold_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with 14-day Stochastic %K < 20 in trailing 63 days."""
    return _rolling_count_true(_stoch_k(high, low, close, 14) < 20.0, _TD_QTR)


def osc_078_stoch_k_14_oversold_frac_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days with 14-day %K < 20."""
    return _rolling_count_true(_stoch_k(high, low, close, 14) < 20.0, _TD_QTR) / _TD_QTR


def osc_079_williams_r_14_oversold_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with Williams %R (14-day) < -80 in trailing 21 days."""
    return _rolling_count_true(_williams_r(high, low, close, 14) < -80.0, _TD_MON)


def osc_080_williams_r_14_oversold_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with Williams %R (14-day) < -80 in trailing 63 days."""
    return _rolling_count_true(_williams_r(high, low, close, 14) < -80.0, _TD_QTR)


def osc_081_cci_14_oversold_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with CCI (14-day) < -100 in trailing 21 days."""
    return _rolling_count_true(_cci(high, low, close, 14) < -100.0, _TD_MON)


def osc_082_cci_14_oversold_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with CCI (14-day) < -100 in trailing 63 days."""
    return _rolling_count_true(_cci(high, low, close, 14) < -100.0, _TD_QTR)


def osc_083_mfi_14_oversold_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with MFI (14-day) < 20 in trailing 21 days."""
    return _rolling_count_true(_mfi(high, low, close, volume, 14) < 20.0, _TD_MON)


def osc_084_mfi_14_oversold_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with MFI (14-day) < 20 in trailing 63 days."""
    return _rolling_count_true(_mfi(high, low, close, volume, 14) < 20.0, _TD_QTR)


def osc_085_stoch_rsi_14_14_oversold_count_21d(close: pd.Series) -> pd.Series:
    """Count of days with StochRSI (14,14) < 20 in trailing 21 days."""
    return _rolling_count_true(_stoch_rsi(close, 14, 14) < 20.0, _TD_MON)


def osc_086_stoch_rsi_14_14_oversold_count_63d(close: pd.Series) -> pd.Series:
    """Count of days with StochRSI (14,14) < 20 in trailing 63 days."""
    return _rolling_count_true(_stoch_rsi(close, 14, 14) < 20.0, _TD_QTR)


def osc_087_ultimate_osc_oversold_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with Ultimate Oscillator < 30 in trailing 21 days."""
    return _rolling_count_true(_ultimate_osc(high, low, close) < 30.0, _TD_MON)


def osc_088_ultimate_osc_oversold_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with Ultimate Oscillator < 30 in trailing 63 days."""
    return _rolling_count_true(_ultimate_osc(high, low, close) < 30.0, _TD_QTR)


def osc_089_multi_osc_all_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: all four oscillators simultaneously oversold (%K<20, WR<-80, CCI<-100, MFI<20)."""
    k_os = _stoch_k(high, low, close, 14) < 20.0
    wr_os = _williams_r(high, low, close, 14) < -80.0
    cci_os = _cci(high, low, close, 14) < -100.0
    mfi_os = _mfi(high, low, close, volume, 14) < 20.0
    return (k_os & wr_os & cci_os & mfi_os).astype(float)


def osc_090_multi_osc_any3_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: at least 3 of 4 oscillators simultaneously oversold."""
    k_os = (_stoch_k(high, low, close, 14) < 20.0).astype(int)
    wr_os = (_williams_r(high, low, close, 14) < -80.0).astype(int)
    cci_os = (_cci(high, low, close, 14) < -100.0).astype(int)
    mfi_os = (_mfi(high, low, close, volume, 14) < 20.0).astype(int)
    return ((k_os + wr_os + cci_os + mfi_os) >= 3).astype(float)


# --- Group I (091-100): Awesome Oscillator and Aroon features (trimmed) ---

def osc_091_awesome_osc_raw(high: pd.Series, low: pd.Series) -> pd.Series:
    """Awesome Oscillator (5/34) raw value; negative = bearish momentum."""
    return _awesome_osc(high, low)


def osc_092_awesome_osc_negative_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: Awesome Oscillator < 0 (bearish momentum)."""
    return (_awesome_osc(high, low) < 0.0).astype(float)


def osc_093_awesome_osc_min_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of Awesome Oscillator."""
    return _rolling_min(_awesome_osc(high, low), _TD_MON)


def osc_094_awesome_osc_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Awesome Oscillator over trailing 252 days."""
    ao = _awesome_osc(high, low)
    return _safe_div(ao - _rolling_mean(ao, _TD_YEAR), _rolling_std(ao, _TD_YEAR))


def osc_095_awesome_osc_consec_negative_days(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days with Awesome Oscillator < 0."""
    return _consec_streak(_awesome_osc(high, low) < 0.0)


def osc_096_aroon_down_14_raw(low: pd.Series) -> pd.Series:
    """Aroon Down (14-period) raw value; high = sustained downtrend."""
    return _aroon_down(low, 14)


def osc_097_aroon_down_14_extreme_flag(low: pd.Series) -> pd.Series:
    """Flag: Aroon Down (14-period) >= 86 (new 14d low recently)."""
    return (_aroon_down(low, 14) >= 86.0).astype(float)


def osc_098_aroon_down_25_raw(low: pd.Series) -> pd.Series:
    """Aroon Down (25-period) raw value."""
    return _aroon_down(low, 25)


def osc_099_aroon_down_25_extreme_flag(low: pd.Series) -> pd.Series:
    """Flag: Aroon Down (25-period) >= 92."""
    return (_aroon_down(low, 25) >= 92.0).astype(float)


def osc_100_aroon_down_14_consec_high_days(low: pd.Series) -> pd.Series:
    """Consecutive days with Aroon Down (14) >= 86."""
    return _consec_streak(_aroon_down(low, 14) >= 86.0)


# --- Group J (101-110): CMO — Chande Momentum Oscillator ---

def osc_101_cmo_14_raw(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (14-day) raw value; below -50 = oversold."""
    return _cmo(close, 14)


def osc_102_cmo_14_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: CMO (14-day) < -50 (oversold)."""
    return (_cmo(close, 14) < -50.0).astype(float)


def osc_103_cmo_14_depth_below50(close: pd.Series) -> pd.Series:
    """Depth of CMO (14-day) below -50 threshold."""
    return (_cmo(close, 14) + 50.0).clip(upper=0.0).abs()


def osc_104_cmo_21_raw(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (21-day) raw value."""
    return _cmo(close, _TD_MON)


def osc_105_cmo_21_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: CMO (21-day) < -50."""
    return (_cmo(close, _TD_MON) < -50.0).astype(float)


def osc_106_cmo_63_raw(close: pd.Series) -> pd.Series:
    """Chande Momentum Oscillator (63-day) raw value — quarterly lookback."""
    return _cmo(close, _TD_QTR)


def osc_107_cmo_14_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of CMO (14-day)."""
    return _rolling_min(_cmo(close, 14), _TD_MON)


def osc_108_cmo_14_consec_oversold_days(close: pd.Series) -> pd.Series:
    """Consecutive days with CMO (14-day) < -50."""
    return _consec_streak(_cmo(close, 14) < -50.0)


def osc_109_cmo_14_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of CMO (14-day) within trailing 252 days."""
    return _cmo(close, 14).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_110_cmo_14_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of CMO (14-day) over trailing 252 days."""
    c = _cmo(close, 14)
    return _safe_div(c - _rolling_mean(c, _TD_YEAR), _rolling_std(c, _TD_YEAR))


# --- Group K (111-117): TRIX ---

def osc_111_trix_14_raw(close: pd.Series) -> pd.Series:
    """TRIX (14-period triple EMA ROC) raw value; negative = bearish."""
    return _trix(close, 14)


def osc_112_trix_14_negative_flag(close: pd.Series) -> pd.Series:
    """Binary flag: TRIX (14) < 0 (bearish momentum)."""
    return (_trix(close, 14) < 0.0).astype(float)


def osc_113_trix_14_signal_line(close: pd.Series) -> pd.Series:
    """TRIX (14) signal line: 9-period EMA of TRIX."""
    return _ewm_mean(_trix(close, 14), 9)


def osc_114_trix_14_histogram(close: pd.Series) -> pd.Series:
    """TRIX (14) histogram: TRIX minus its signal line."""
    t = _trix(close, 14)
    return t - _ewm_mean(t, 9)


def osc_115_trix_21_raw(close: pd.Series) -> pd.Series:
    """TRIX (21-period) raw value — monthly lookback."""
    return _trix(close, _TD_MON)


def osc_116_trix_14_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of TRIX (14)."""
    return _rolling_min(_trix(close, 14), _TD_MON)


def osc_117_trix_14_consec_negative_days(close: pd.Series) -> pd.Series:
    """Consecutive days with TRIX (14) < 0."""
    return _consec_streak(_trix(close, 14) < 0.0)


# --- Group L (118-124): Fisher Transform ---

def osc_118_fisher_10_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fisher Transform (10-day) raw value; below -2 = extreme oversold."""
    return _fisher_transform(high, low, close, 10)


def osc_119_fisher_10_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Fisher Transform (10-day) < -2."""
    return (_fisher_transform(high, low, close, 10) < -2.0).astype(float)


def osc_120_fisher_10_depth_below_neg2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of Fisher Transform (10-day) below -2."""
    return (_fisher_transform(high, low, close, 10) + 2.0).clip(upper=0.0).abs()


def osc_121_fisher_21_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fisher Transform (21-day) raw value."""
    return _fisher_transform(high, low, close, _TD_MON)


def osc_122_fisher_21_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Fisher Transform (21-day) < -2."""
    return (_fisher_transform(high, low, close, _TD_MON) < -2.0).astype(float)


def osc_123_fisher_10_min_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of Fisher Transform (10-day)."""
    return _rolling_min(_fisher_transform(high, low, close, 10), _TD_MON)


def osc_124_fisher_10_consec_oversold_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days with Fisher Transform (10-day) < -2."""
    return _consec_streak(_fisher_transform(high, low, close, 10) < -2.0)


# --- Group M (125-131): PPO (Percentage Price Oscillator) ---

def osc_125_ppo_raw(close: pd.Series) -> pd.Series:
    """PPO (12/26) raw value; negative = bearish momentum."""
    return _ppo(close)


def osc_126_ppo_negative_flag(close: pd.Series) -> pd.Series:
    """Binary flag: PPO (12/26) < 0."""
    return (_ppo(close) < 0.0).astype(float)


def osc_127_ppo_signal_line(close: pd.Series) -> pd.Series:
    """PPO signal line: EMA(9) of PPO (12/26)."""
    return _ppo_signal(close)


def osc_128_ppo_histogram(close: pd.Series) -> pd.Series:
    """PPO histogram: PPO minus signal line."""
    return _ppo(close) - _ppo_signal(close)


def osc_129_ppo_histogram_negative_flag(close: pd.Series) -> pd.Series:
    """Binary flag: PPO histogram < 0 (bearish histogram)."""
    return (_ppo(close) - _ppo_signal(close) < 0.0).astype(float)


def osc_130_ppo_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of PPO (12/26)."""
    return _rolling_min(_ppo(close), _TD_MON)


def osc_131_ppo_consec_negative_days(close: pd.Series) -> pd.Series:
    """Consecutive days with PPO (12/26) < 0."""
    return _consec_streak(_ppo(close) < 0.0)


# --- Group N (132-136): KST (Know Sure Thing) ---

def osc_132_kst_raw(close: pd.Series) -> pd.Series:
    """KST oscillator raw value; negative = bearish."""
    return _kst(close)


def osc_133_kst_signal_line(close: pd.Series) -> pd.Series:
    """KST signal line: 9-period SMA of KST."""
    return _rolling_mean(_kst(close), 9)


def osc_134_kst_negative_flag(close: pd.Series) -> pd.Series:
    """Binary flag: KST < 0."""
    return (_kst(close) < 0.0).astype(float)


def osc_135_kst_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of KST."""
    return _rolling_min(_kst(close), _TD_MON)


def osc_136_kst_consec_negative_days(close: pd.Series) -> pd.Series:
    """Consecutive days with KST < 0."""
    return _consec_streak(_kst(close) < 0.0)


# --- Group O (137-140): Coppock Curve ---

def osc_137_coppock_raw(close: pd.Series) -> pd.Series:
    """Coppock Curve raw value; negative = bearish (buy signal when crosses above 0)."""
    return _coppock(close)


def osc_138_coppock_negative_flag(close: pd.Series) -> pd.Series:
    """Binary flag: Coppock Curve < 0."""
    return (_coppock(close) < 0.0).astype(float)


def osc_139_coppock_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of Coppock Curve."""
    return _rolling_min(_coppock(close), _TD_MON)


def osc_140_coppock_consec_negative_days(close: pd.Series) -> pd.Series:
    """Consecutive days with Coppock Curve < 0."""
    return _consec_streak(_coppock(close) < 0.0)


# --- Group P (141-145): Stochastic Momentum Index (SMI) ---

def osc_141_smi_14_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stochastic Momentum Index (14-day) raw value; below -40 = oversold."""
    return _smi(high, low, close, 14)


def osc_142_smi_14_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: SMI (14-day) < -40."""
    return (_smi(high, low, close, 14) < -40.0).astype(float)


def osc_143_smi_14_depth_below40(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of SMI (14-day) below -40."""
    return (_smi(high, low, close, 14) + 40.0).clip(upper=0.0).abs()


def osc_144_smi_21_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stochastic Momentum Index (21-day) raw value."""
    return _smi(high, low, close, _TD_MON)


def osc_145_smi_14_consec_oversold_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days with SMI (14-day) < -40."""
    return _consec_streak(_smi(high, low, close, 14) < -40.0)


# --- Group Q (146-148): Schaff Trend Cycle ---

def osc_146_schaff_raw(close: pd.Series) -> pd.Series:
    """Schaff Trend Cycle raw value (0-100); below 25 = oversold."""
    return _schaff_trend_cycle(close)


def osc_147_schaff_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: Schaff Trend Cycle < 25 (oversold)."""
    return (_schaff_trend_cycle(close) < 25.0).astype(float)


def osc_148_schaff_depth_below25(close: pd.Series) -> pd.Series:
    """Depth of Schaff Trend Cycle below 25."""
    return (25.0 - _schaff_trend_cycle(close)).clip(lower=0.0)


# --- Group R (149-150): Klinger Volume Oscillator + RVI ---

def osc_149_klinger_raw(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator (EMA34 - EMA55 of volume force); negative = bearish."""
    return _klinger(high, low, close, volume)


def osc_150_rvi_raw(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relative Vigor Index (10-period); positive = bullish vigor."""
    return _rvi(open_, high, low, close, 10)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_REGISTRY_076_150 = {
    "osc_076_stoch_k_14_oversold_count_21d": {"inputs": ["high", "low", "close"], "func": osc_076_stoch_k_14_oversold_count_21d},
    "osc_077_stoch_k_14_oversold_count_63d": {"inputs": ["high", "low", "close"], "func": osc_077_stoch_k_14_oversold_count_63d},
    "osc_078_stoch_k_14_oversold_frac_63d": {"inputs": ["high", "low", "close"], "func": osc_078_stoch_k_14_oversold_frac_63d},
    "osc_079_williams_r_14_oversold_count_21d": {"inputs": ["high", "low", "close"], "func": osc_079_williams_r_14_oversold_count_21d},
    "osc_080_williams_r_14_oversold_count_63d": {"inputs": ["high", "low", "close"], "func": osc_080_williams_r_14_oversold_count_63d},
    "osc_081_cci_14_oversold_count_21d": {"inputs": ["high", "low", "close"], "func": osc_081_cci_14_oversold_count_21d},
    "osc_082_cci_14_oversold_count_63d": {"inputs": ["high", "low", "close"], "func": osc_082_cci_14_oversold_count_63d},
    "osc_083_mfi_14_oversold_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": osc_083_mfi_14_oversold_count_21d},
    "osc_084_mfi_14_oversold_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": osc_084_mfi_14_oversold_count_63d},
    "osc_085_stoch_rsi_14_14_oversold_count_21d": {"inputs": ["close"], "func": osc_085_stoch_rsi_14_14_oversold_count_21d},
    "osc_086_stoch_rsi_14_14_oversold_count_63d": {"inputs": ["close"], "func": osc_086_stoch_rsi_14_14_oversold_count_63d},
    "osc_087_ultimate_osc_oversold_count_21d": {"inputs": ["high", "low", "close"], "func": osc_087_ultimate_osc_oversold_count_21d},
    "osc_088_ultimate_osc_oversold_count_63d": {"inputs": ["high", "low", "close"], "func": osc_088_ultimate_osc_oversold_count_63d},
    "osc_089_multi_osc_all_oversold_flag": {"inputs": ["high", "low", "close", "volume"], "func": osc_089_multi_osc_all_oversold_flag},
    "osc_090_multi_osc_any3_oversold_flag": {"inputs": ["high", "low", "close", "volume"], "func": osc_090_multi_osc_any3_oversold_flag},
    "osc_091_awesome_osc_raw": {"inputs": ["high", "low"], "func": osc_091_awesome_osc_raw},
    "osc_092_awesome_osc_negative_flag": {"inputs": ["high", "low"], "func": osc_092_awesome_osc_negative_flag},
    "osc_093_awesome_osc_min_21d": {"inputs": ["high", "low"], "func": osc_093_awesome_osc_min_21d},
    "osc_094_awesome_osc_zscore_252d": {"inputs": ["high", "low"], "func": osc_094_awesome_osc_zscore_252d},
    "osc_095_awesome_osc_consec_negative_days": {"inputs": ["high", "low"], "func": osc_095_awesome_osc_consec_negative_days},
    "osc_096_aroon_down_14_raw": {"inputs": ["low"], "func": osc_096_aroon_down_14_raw},
    "osc_097_aroon_down_14_extreme_flag": {"inputs": ["low"], "func": osc_097_aroon_down_14_extreme_flag},
    "osc_098_aroon_down_25_raw": {"inputs": ["low"], "func": osc_098_aroon_down_25_raw},
    "osc_099_aroon_down_25_extreme_flag": {"inputs": ["low"], "func": osc_099_aroon_down_25_extreme_flag},
    "osc_100_aroon_down_14_consec_high_days": {"inputs": ["low"], "func": osc_100_aroon_down_14_consec_high_days},
    "osc_101_cmo_14_raw": {"inputs": ["close"], "func": osc_101_cmo_14_raw},
    "osc_102_cmo_14_oversold_flag": {"inputs": ["close"], "func": osc_102_cmo_14_oversold_flag},
    "osc_103_cmo_14_depth_below50": {"inputs": ["close"], "func": osc_103_cmo_14_depth_below50},
    "osc_104_cmo_21_raw": {"inputs": ["close"], "func": osc_104_cmo_21_raw},
    "osc_105_cmo_21_oversold_flag": {"inputs": ["close"], "func": osc_105_cmo_21_oversold_flag},
    "osc_106_cmo_63_raw": {"inputs": ["close"], "func": osc_106_cmo_63_raw},
    "osc_107_cmo_14_min_21d": {"inputs": ["close"], "func": osc_107_cmo_14_min_21d},
    "osc_108_cmo_14_consec_oversold_days": {"inputs": ["close"], "func": osc_108_cmo_14_consec_oversold_days},
    "osc_109_cmo_14_pct_rank_252d": {"inputs": ["close"], "func": osc_109_cmo_14_pct_rank_252d},
    "osc_110_cmo_14_zscore_252d": {"inputs": ["close"], "func": osc_110_cmo_14_zscore_252d},
    "osc_111_trix_14_raw": {"inputs": ["close"], "func": osc_111_trix_14_raw},
    "osc_112_trix_14_negative_flag": {"inputs": ["close"], "func": osc_112_trix_14_negative_flag},
    "osc_113_trix_14_signal_line": {"inputs": ["close"], "func": osc_113_trix_14_signal_line},
    "osc_114_trix_14_histogram": {"inputs": ["close"], "func": osc_114_trix_14_histogram},
    "osc_115_trix_21_raw": {"inputs": ["close"], "func": osc_115_trix_21_raw},
    "osc_116_trix_14_min_21d": {"inputs": ["close"], "func": osc_116_trix_14_min_21d},
    "osc_117_trix_14_consec_negative_days": {"inputs": ["close"], "func": osc_117_trix_14_consec_negative_days},
    "osc_118_fisher_10_raw": {"inputs": ["high", "low", "close"], "func": osc_118_fisher_10_raw},
    "osc_119_fisher_10_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_119_fisher_10_oversold_flag},
    "osc_120_fisher_10_depth_below_neg2": {"inputs": ["high", "low", "close"], "func": osc_120_fisher_10_depth_below_neg2},
    "osc_121_fisher_21_raw": {"inputs": ["high", "low", "close"], "func": osc_121_fisher_21_raw},
    "osc_122_fisher_21_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_122_fisher_21_oversold_flag},
    "osc_123_fisher_10_min_21d": {"inputs": ["high", "low", "close"], "func": osc_123_fisher_10_min_21d},
    "osc_124_fisher_10_consec_oversold_days": {"inputs": ["high", "low", "close"], "func": osc_124_fisher_10_consec_oversold_days},
    "osc_125_ppo_raw": {"inputs": ["close"], "func": osc_125_ppo_raw},
    "osc_126_ppo_negative_flag": {"inputs": ["close"], "func": osc_126_ppo_negative_flag},
    "osc_127_ppo_signal_line": {"inputs": ["close"], "func": osc_127_ppo_signal_line},
    "osc_128_ppo_histogram": {"inputs": ["close"], "func": osc_128_ppo_histogram},
    "osc_129_ppo_histogram_negative_flag": {"inputs": ["close"], "func": osc_129_ppo_histogram_negative_flag},
    "osc_130_ppo_min_21d": {"inputs": ["close"], "func": osc_130_ppo_min_21d},
    "osc_131_ppo_consec_negative_days": {"inputs": ["close"], "func": osc_131_ppo_consec_negative_days},
    "osc_132_kst_raw": {"inputs": ["close"], "func": osc_132_kst_raw},
    "osc_133_kst_signal_line": {"inputs": ["close"], "func": osc_133_kst_signal_line},
    "osc_134_kst_negative_flag": {"inputs": ["close"], "func": osc_134_kst_negative_flag},
    "osc_135_kst_min_21d": {"inputs": ["close"], "func": osc_135_kst_min_21d},
    "osc_136_kst_consec_negative_days": {"inputs": ["close"], "func": osc_136_kst_consec_negative_days},
    "osc_137_coppock_raw": {"inputs": ["close"], "func": osc_137_coppock_raw},
    "osc_138_coppock_negative_flag": {"inputs": ["close"], "func": osc_138_coppock_negative_flag},
    "osc_139_coppock_min_21d": {"inputs": ["close"], "func": osc_139_coppock_min_21d},
    "osc_140_coppock_consec_negative_days": {"inputs": ["close"], "func": osc_140_coppock_consec_negative_days},
    "osc_141_smi_14_raw": {"inputs": ["high", "low", "close"], "func": osc_141_smi_14_raw},
    "osc_142_smi_14_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_142_smi_14_oversold_flag},
    "osc_143_smi_14_depth_below40": {"inputs": ["high", "low", "close"], "func": osc_143_smi_14_depth_below40},
    "osc_144_smi_21_raw": {"inputs": ["high", "low", "close"], "func": osc_144_smi_21_raw},
    "osc_145_smi_14_consec_oversold_days": {"inputs": ["high", "low", "close"], "func": osc_145_smi_14_consec_oversold_days},
    "osc_146_schaff_raw": {"inputs": ["close"], "func": osc_146_schaff_raw},
    "osc_147_schaff_oversold_flag": {"inputs": ["close"], "func": osc_147_schaff_oversold_flag},
    "osc_148_schaff_depth_below25": {"inputs": ["close"], "func": osc_148_schaff_depth_below25},
    "osc_149_klinger_raw": {"inputs": ["high", "low", "close", "volume"], "func": osc_149_klinger_raw},
    "osc_150_rvi_raw": {"inputs": ["open", "high", "low", "close"], "func": osc_150_rvi_raw},
}
