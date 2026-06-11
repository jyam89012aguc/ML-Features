"""
32_momentum_divergence — Base Features 076-150
Domain: hidden bullish divergence, OBV divergence, divergence strength grading
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — continuation signals and volume-confirmed divergence
All features are backward-looking only; no forward information.

NEW COVERAGE vs prior version:
  076-100  Hidden bullish divergence: price higher low, oscillator lower low (RSI/MACD/Stoch)
  101-120  OBV divergence: price new low while OBV does NOT (regular + hidden)
  121-150  Divergence strength grading: gap magnitude, multi-oscillator agreement, recency
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


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder RSI, returns 0-100 series."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - _safe_div(pd.Series(100.0, index=close.index), 1.0 + rs)


def _macd_line(close: pd.Series, fast: int = 12, slow: int = 26) -> pd.Series:
    return _ewm_mean(close, fast) - _ewm_mean(close, slow)


def _stoch_k(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14) -> pd.Series:
    lo = _rolling_min(low, period)
    hi = _rolling_max(high, period)
    return _safe_div(close - lo, hi - lo) * 100.0


def _roc(close: pd.Series, period: int) -> pd.Series:
    return _safe_div(close - close.shift(period), close.shift(period))


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


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


def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """On-Balance Volume built from close and volume (backward-looking)."""
    direction = np.sign(close.diff(1)).fillna(0.0)
    return (direction * volume).cumsum()


def _price_higher_low(close: pd.Series, w: int) -> pd.Series:
    """Boolean: close is ABOVE its w-period trailing min shifted 1 bar (higher low than recent floor)."""
    prior_min = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close > prior_min).astype(float)


def _price_new_low(close: pd.Series, w: int) -> pd.Series:
    prior_min = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close < prior_min).astype(float)


def _osc_lower_low(osc: pd.Series, w: int) -> pd.Series:
    """Boolean: oscillator IS at a new w-period low (lower low than recent floor)."""
    prior_min = osc.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (osc < prior_min).astype(float)


def _osc_higher_low(osc: pd.Series, w: int) -> pd.Series:
    """Boolean: oscillator is NOT at a new w-period low (higher low)."""
    return 1.0 - _osc_lower_low(osc, w)


def _days_since_flag(flag: pd.Series) -> pd.Series:
    """Bars since the most recent 1 in a binary series; NaN before first occurrence."""
    idx = np.arange(len(flag), dtype=float)
    last = pd.Series(np.nan, index=flag.index)
    running = np.nan
    arr = flag.values
    out = np.full(len(flag), np.nan)
    for i in range(len(arr)):
        if arr[i] == 1.0:
            running = idx[i]
        if not np.isnan(running):
            out[i] = idx[i] - running
    return pd.Series(out, index=flag.index)


# ── Feature functions 076-100: Hidden Bullish Divergence ────────────────────
# Definition: price makes a HIGHER LOW while the oscillator makes a LOWER LOW.
# This is a CONTINUATION signal (trend likely to resume upward after pullback).
# Detected trailing-only using rolling mins.

def mdv_076_rsi14_hidden_bull_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + RSI(14) lower low over 21-day window."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_MON)
    osc_ll = _osc_lower_low(rsi, _TD_MON)
    return price_hl * osc_ll


def mdv_077_rsi14_hidden_bull_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + RSI(14) lower low over 63-day window."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    return price_hl * osc_ll


def mdv_078_rsi14_hidden_bull_divg_flag_126d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + RSI(14) lower low over 126-day window."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_HALF)
    osc_ll = _osc_lower_low(rsi, _TD_HALF)
    return price_hl * osc_ll


def mdv_079_rsi14_hidden_bull_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + RSI(14) lower low over 252-day window."""
    rsi = _rsi(close, 14)
    price_hl = _price_higher_low(close, _TD_YEAR)
    osc_ll = _osc_lower_low(rsi, _TD_YEAR)
    return price_hl * osc_ll


def mdv_080_rsi14_hidden_bull_divg_magnitude_63d(close: pd.Series) -> pd.Series:
    """Hidden divergence magnitude: price gain from 63d min minus RSI drop below 63d min."""
    rsi = _rsi(close, 14)
    price_floor = _rolling_min(close, _TD_QTR)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    price_lift = _safe_div(close - price_floor, price_floor.clip(lower=_EPS))
    rsi_drop = _safe_div(rsi_floor - rsi, rsi_floor.clip(lower=_EPS))
    flag = mdv_077_rsi14_hidden_bull_divg_flag_63d(close)
    return (price_lift + rsi_drop) * flag


def mdv_081_rsi7_hidden_bull_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + RSI(7) lower low over 21-day window."""
    rsi = _rsi(close, 7)
    price_hl = _price_higher_low(close, _TD_MON)
    osc_ll = _osc_lower_low(rsi, _TD_MON)
    return price_hl * osc_ll


def mdv_082_rsi21_hidden_bull_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + RSI(21) lower low over 63-day window."""
    rsi = _rsi(close, _TD_MON)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(rsi, _TD_QTR)
    return price_hl * osc_ll


def mdv_083_rsi14_hidden_bull_divg_count_63d(close: pd.Series) -> pd.Series:
    """Count of RSI(14) hidden bullish divergence flags in trailing 63 days."""
    flag = mdv_077_rsi14_hidden_bull_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_QTR)


def mdv_084_rsi14_hidden_bull_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of RSI(14) hidden bullish divergence flags in trailing 252 days."""
    flag = mdv_077_rsi14_hidden_bull_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_085_rsi14_hidden_bull_recency_63d(close: pd.Series) -> pd.Series:
    """Days since last RSI(14) hidden bullish divergence flag (63-day window)."""
    flag = mdv_077_rsi14_hidden_bull_divg_flag_63d(close)
    return _days_since_flag(flag)


def mdv_086_macd_hidden_bull_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + MACD lower low over 21-day window."""
    macd = _macd_line(close)
    price_hl = _price_higher_low(close, _TD_MON)
    osc_ll = _osc_lower_low(macd, _TD_MON)
    return price_hl * osc_ll


def mdv_087_macd_hidden_bull_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + MACD lower low over 63-day window."""
    macd = _macd_line(close)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(macd, _TD_QTR)
    return price_hl * osc_ll


def mdv_088_macd_hidden_bull_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + MACD lower low over 252-day window."""
    macd = _macd_line(close)
    price_hl = _price_higher_low(close, _TD_YEAR)
    osc_ll = _osc_lower_low(macd, _TD_YEAR)
    return price_hl * osc_ll


def mdv_089_macd_hidden_bull_divg_magnitude_63d(close: pd.Series) -> pd.Series:
    """MACD hidden divergence magnitude: price above 63d min while MACD below 63d min."""
    macd = _macd_line(close)
    price_floor = _rolling_min(close, _TD_QTR)
    macd_floor = _rolling_min(macd, _TD_QTR)
    price_lift = _safe_div(close - price_floor, price_floor.clip(lower=_EPS))
    macd_drop = macd_floor - macd
    flag = mdv_087_macd_hidden_bull_divg_flag_63d(close)
    return (price_lift + macd_drop.clip(lower=0.0)) * flag


def mdv_090_macd_hidden_bull_divg_count_63d(close: pd.Series) -> pd.Series:
    """Count of MACD hidden bullish divergence flags in trailing 63 days."""
    flag = mdv_087_macd_hidden_bull_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_QTR)


def mdv_091_macd_hidden_bull_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of MACD hidden bullish divergence flags in trailing 252 days."""
    flag = mdv_087_macd_hidden_bull_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_092_macd_hidden_bull_recency_63d(close: pd.Series) -> pd.Series:
    """Days since last MACD hidden bullish divergence (63-day detection window)."""
    flag = mdv_087_macd_hidden_bull_divg_flag_63d(close)
    return _days_since_flag(flag)


def mdv_093_stoch_hidden_bull_divg_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + Stoch %K lower low over 21-day window."""
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_MON)
    osc_ll = _osc_lower_low(sk, _TD_MON)
    return price_hl * osc_ll


def mdv_094_stoch_hidden_bull_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + Stoch %K lower low over 63-day window."""
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_QTR)
    osc_ll = _osc_lower_low(sk, _TD_QTR)
    return price_hl * osc_ll


def mdv_095_stoch_hidden_bull_divg_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Hidden bullish divergence: price higher low + Stoch %K lower low over 252-day window."""
    sk = _stoch_k(close, high, low, 14)
    price_hl = _price_higher_low(close, _TD_YEAR)
    osc_ll = _osc_lower_low(sk, _TD_YEAR)
    return price_hl * osc_ll


def mdv_096_stoch_hidden_bull_divg_magnitude_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stoch hidden divergence magnitude: price lift from 63d min while Stoch drops below 63d min."""
    sk = _stoch_k(close, high, low, 14)
    price_floor = _rolling_min(close, _TD_QTR)
    sk_floor = _rolling_min(sk, _TD_QTR)
    price_lift = _safe_div(close - price_floor, price_floor.clip(lower=_EPS))
    sk_drop = (sk_floor - sk).clip(lower=0.0)
    flag = mdv_094_stoch_hidden_bull_divg_flag_63d(close, high, low)
    return (price_lift + _safe_div(sk_drop, pd.Series(100.0, index=sk.index))) * flag


def mdv_097_stoch_hidden_bull_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Stoch hidden bullish divergence flags in trailing 252 days."""
    flag = mdv_094_stoch_hidden_bull_divg_flag_63d(close, high, low)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_098_composite_hidden_bull_score_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of RSI, MACD, Stoch hidden bullish divergence flags at 21-day bar; 0-3."""
    a = mdv_076_rsi14_hidden_bull_divg_flag_21d(close)
    b = mdv_086_macd_hidden_bull_divg_flag_21d(close)
    c = mdv_093_stoch_hidden_bull_divg_flag_21d(close, high, low)
    return a + b + c


def mdv_099_composite_hidden_bull_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of RSI, MACD, Stoch hidden bullish divergence flags at 63-day bar; 0-3."""
    a = mdv_077_rsi14_hidden_bull_divg_flag_63d(close)
    b = mdv_087_macd_hidden_bull_divg_flag_63d(close)
    c = mdv_094_stoch_hidden_bull_divg_flag_63d(close, high, low)
    return a + b + c


def mdv_100_composite_hidden_bull_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of RSI, MACD, Stoch hidden bullish divergence flags at 252-day bar; 0-3."""
    a = mdv_079_rsi14_hidden_bull_divg_flag_252d(close)
    b = mdv_088_macd_hidden_bull_divg_flag_252d(close)
    c = mdv_095_stoch_hidden_bull_divg_flag_252d(close, high, low)
    return a + b + c


# ── Feature functions 101-120: OBV Divergence ────────────────────────────────
# OBV built from close+volume. Regular OBV divergence: price new low, OBV NOT new low.
# Hidden OBV divergence: price higher low, OBV lower low (OBV volume continuation signal).

def mdv_101_obv_regular_divg_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Regular OBV divergence: price 21-day new low but OBV does NOT (volume not confirming)."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_MON)
    obv_nl = _osc_lower_low(obv, _TD_MON)
    return price_nl * (1.0 - obv_nl)


def mdv_102_obv_regular_divg_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Regular OBV divergence: price 63-day new low but OBV does NOT."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_nl = _osc_lower_low(obv, _TD_QTR)
    return price_nl * (1.0 - obv_nl)


def mdv_103_obv_regular_divg_flag_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Regular OBV divergence: price 126-day new low but OBV does NOT."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_HALF)
    obv_nl = _osc_lower_low(obv, _TD_HALF)
    return price_nl * (1.0 - obv_nl)


def mdv_104_obv_regular_divg_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Regular OBV divergence: price 252-day new low but OBV does NOT."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_YEAR)
    obv_nl = _osc_lower_low(obv, _TD_YEAR)
    return price_nl * (1.0 - obv_nl)


def mdv_105_obv_gap_at_price_low_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV above its 63-day min when price makes 63-day new low (divergence gap magnitude)."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_QTR)
    obv_floor = _rolling_min(obv, _TD_QTR)
    gap = (obv - obv_floor).clip(lower=0.0)
    return gap * price_nl


def mdv_106_obv_gap_at_price_low_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV above its 252-day min when price makes 252-day new low."""
    obv = _obv(close, volume)
    price_nl = _price_new_low(close, _TD_YEAR)
    obv_floor = _rolling_min(obv, _TD_YEAR)
    gap = (obv - obv_floor).clip(lower=0.0)
    return gap * price_nl


def mdv_107_obv_pctrank_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct-rank minus price pct-rank over 63-day window (normalized OBV divergence)."""
    obv = _obv(close, volume)
    return _pct_rank(obv, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_108_obv_pctrank_spread_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct-rank minus price pct-rank over 252-day window."""
    obv = _obv(close, volume)
    return _pct_rank(obv, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_109_obv_regular_divg_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of regular OBV divergence flags in trailing 63 days."""
    flag = mdv_102_obv_regular_divg_flag_63d(close, volume)
    return _rolling_sum(flag, _TD_QTR)


def mdv_110_obv_regular_divg_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of regular OBV divergence flags in trailing 252 days."""
    flag = mdv_102_obv_regular_divg_flag_63d(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_111_obv_hidden_bull_divg_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden OBV divergence: price higher low + OBV lower low over 21-day window."""
    obv = _obv(close, volume)
    price_hl = _price_higher_low(close, _TD_MON)
    obv_ll = _osc_lower_low(obv, _TD_MON)
    return price_hl * obv_ll


def mdv_112_obv_hidden_bull_divg_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden OBV divergence: price higher low + OBV lower low over 63-day window."""
    obv = _obv(close, volume)
    price_hl = _price_higher_low(close, _TD_QTR)
    obv_ll = _osc_lower_low(obv, _TD_QTR)
    return price_hl * obv_ll


def mdv_113_obv_hidden_bull_divg_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hidden OBV divergence: price higher low + OBV lower low over 252-day window."""
    obv = _obv(close, volume)
    price_hl = _price_higher_low(close, _TD_YEAR)
    obv_ll = _osc_lower_low(obv, _TD_YEAR)
    return price_hl * obv_ll


def mdv_114_obv_hidden_bull_divg_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of hidden OBV divergence flags in trailing 252 days."""
    flag = mdv_112_obv_hidden_bull_divg_flag_63d(close, volume)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_115_obv_divg_recency_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last regular OBV bullish divergence flag (63-day detection)."""
    flag = mdv_102_obv_regular_divg_flag_63d(close, volume)
    return _days_since_flag(flag)


def mdv_116_obv_slope_divg_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 21-day slope positive while price makes 63-day new low (OBV trending up, price down)."""
    obv = _obv(close, volume)
    obv_slope = obv.diff(_TD_MON)
    price_nl = _price_new_low(close, _TD_QTR)
    return price_nl * (obv_slope > 0).astype(float)


def mdv_117_obv_slope_divg_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 63-day slope positive while price makes 252-day new low."""
    obv = _obv(close, volume)
    obv_slope = obv.diff(_TD_QTR)
    price_nl = _price_new_low(close, _TD_YEAR)
    return price_nl * (obv_slope > 0).astype(float)


def mdv_118_obv_pctrank_spread_pctrank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of OBV-price pct-rank spread within trailing 252 days."""
    spread = mdv_107_obv_pctrank_spread_63d(close, volume)
    return _pct_rank(spread, _TD_YEAR)


def mdv_119_obv_gap_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum OBV divergence gap at price new-low over trailing 252 days."""
    gap = mdv_105_obv_gap_at_price_low_63d(close, volume)
    return _rolling_max(gap, _TD_YEAR)


def mdv_120_obv_rsi_joint_divg_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: both OBV and RSI(14) confirm bullish divergence at same 63-day price low."""
    obv_flag = mdv_102_obv_regular_divg_flag_63d(close, volume)
    rsi = _rsi(close, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    rsi_nl = _osc_lower_low(rsi, _TD_QTR)
    rsi_flag = price_nl * (1.0 - rsi_nl)
    return obv_flag * rsi_flag


# ── Feature functions 121-150: Divergence Strength Grading ───────────────────
# Magnitude of price-vs-oscillator gap, count of divergences in window,
# multi-oscillator agreement, strength grading across indicators.

def mdv_121_rsi14_divg_gap_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of RSI(14) gap at price-new-low vs its 63-day mean and std."""
    rsi = _rsi(close, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    gap = (rsi - rsi_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    return _safe_div(gap - m, s)


def mdv_122_macd_divg_gap_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of MACD gap at price-new-low vs 63-day window."""
    macd = _macd_line(close)
    price_nl = _price_new_low(close, _TD_QTR)
    macd_floor = _rolling_min(macd, _TD_QTR)
    gap = (macd - macd_floor) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    return _safe_div(gap - m, s)


def mdv_123_stoch_divg_gap_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of Stoch %K gap at price-new-low vs 63-day window."""
    sk = _stoch_k(close, high, low, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    sk_floor = _rolling_min(sk, _TD_QTR)
    gap = (sk - sk_floor).clip(lower=0.0) * price_nl
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    return _safe_div(gap - m, s)


def mdv_124_obv_divg_gap_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV gap at price-new-low vs 63-day window."""
    gap = mdv_105_obv_gap_at_price_low_63d(close, volume)
    m = _rolling_mean(gap, _TD_QTR)
    s = _rolling_std(gap, _TD_QTR)
    return _safe_div(gap - m, s)


def mdv_125_rsi14_divg_gap_pctrank_252d(close: pd.Series) -> pd.Series:
    """Pct-rank of RSI(14) divergence gap within trailing 252 days (strength grade)."""
    rsi = _rsi(close, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    gap = (rsi - rsi_floor).clip(lower=0.0) * price_nl
    return _pct_rank(gap, _TD_YEAR)


def mdv_126_macd_divg_gap_pctrank_252d(close: pd.Series) -> pd.Series:
    """Pct-rank of MACD divergence gap within trailing 252 days."""
    macd = _macd_line(close)
    price_nl = _price_new_low(close, _TD_QTR)
    macd_floor = _rolling_min(macd, _TD_QTR)
    gap = (macd - macd_floor) * price_nl
    return _pct_rank(gap, _TD_YEAR)


def mdv_127_composite_divg_gap_avg_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average of RSI, MACD, Stoch normalized gap at price-new-low (composite strength, 63d)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    price_nl = _price_new_low(close, _TD_QTR)
    rsi_gap = (rsi - _rolling_min(rsi, _TD_QTR)).clip(lower=0.0) * price_nl
    macd_gap = (macd - _rolling_min(macd, _TD_QTR)) * price_nl
    sk_gap = (sk - _rolling_min(sk, _TD_QTR)).clip(lower=0.0) * price_nl
    rsi_norm = _safe_div(rsi_gap, _rolling_std(rsi, _TD_QTR).clip(lower=_EPS))
    macd_norm = _safe_div(macd_gap, _rolling_std(macd, _TD_QTR).clip(lower=_EPS))
    sk_norm = _safe_div(sk_gap, _rolling_std(sk, _TD_QTR).clip(lower=_EPS))
    return (rsi_norm + macd_norm + sk_norm) / 3.0


def mdv_128_multi_osc_divg_agreement_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of oscillators (RSI/MACD/Stoch/ROC10) diverging at 63-day price low; 0-4."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    roc = _roc(close, 10)
    price_nl = _price_new_low(close, _TD_QTR)
    a = price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
    b = price_nl * (1.0 - _osc_lower_low(macd, _TD_QTR))
    c = price_nl * (1.0 - _osc_lower_low(sk, _TD_QTR))
    d = price_nl * (1.0 - _osc_lower_low(roc, _TD_QTR))
    return a + b + c + d


def mdv_129_multi_osc_divg_agreement_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of oscillators (RSI/MACD/Stoch/ROC10) diverging at 252-day price low; 0-4."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    sk = _stoch_k(close, high, low, 14)
    roc = _roc(close, 10)
    price_nl = _price_new_low(close, _TD_YEAR)
    a = price_nl * (1.0 - _osc_lower_low(rsi, _TD_YEAR))
    b = price_nl * (1.0 - _osc_lower_low(macd, _TD_YEAR))
    c = price_nl * (1.0 - _osc_lower_low(sk, _TD_YEAR))
    d = price_nl * (1.0 - _osc_lower_low(roc, _TD_YEAR))
    return a + b + c + d


def mdv_130_multi_osc_with_obv_agreement_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of oscillators+OBV diverging at 63-day price low; 0-5 (RSI/MACD/Stoch/ROC/OBV)."""
    base = mdv_128_multi_osc_divg_agreement_score_63d(close, high, low)
    obv_flag = mdv_102_obv_regular_divg_flag_63d(close, volume)
    return base + obv_flag


def mdv_131_divg_agreement_score_pctrank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pct-rank of multi-oscillator divergence agreement score within 252-day window."""
    score = mdv_128_multi_osc_divg_agreement_score_63d(close, high, low)
    return _pct_rank(score, _TD_YEAR)


def mdv_132_four_osc_all_agree_divg_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: all 4 oscillators (RSI/MACD/Stoch/ROC10) diverge simultaneously at 63-day low."""
    score = mdv_128_multi_osc_divg_agreement_score_63d(close, high, low)
    return (score >= 4.0).astype(float)


def mdv_133_divg_strength_grade_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Continuous divergence strength grade: agreement * avg normalized gap (63d)."""
    agreement = mdv_128_multi_osc_divg_agreement_score_63d(close, high, low)
    gap_avg = mdv_127_composite_divg_gap_avg_63d(close, high, low)
    return agreement * gap_avg.clip(lower=0.0)


def mdv_134_divg_strength_grade_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pct-rank of 63d strength grade within trailing 252-day window."""
    grade = mdv_133_divg_strength_grade_63d(close, high, low)
    return _pct_rank(grade, _TD_YEAR)


def mdv_135_rsi14_hidden_vs_regular_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio: hidden bullish divergence count vs regular divergence count (63d)."""
    hidden_cnt = mdv_083_rsi14_hidden_bull_divg_count_63d(close)
    reg_cnt = _rolling_sum(
        _price_new_low(close, _TD_QTR) * (1.0 - _osc_lower_low(_rsi(close, 14), _TD_QTR)),
        _TD_QTR,
    )
    return _safe_div(hidden_cnt, reg_cnt.clip(lower=_EPS))


def mdv_136_hidden_bull_divg_score_rolling_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max composite hidden bullish divergence score over trailing 63 days."""
    score = mdv_099_composite_hidden_bull_score_63d(close, high, low)
    return _rolling_max(score, _TD_QTR)


def mdv_137_hidden_bull_divg_score_rolling_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max composite hidden bullish divergence score over trailing 252 days."""
    score = mdv_099_composite_hidden_bull_score_63d(close, high, low)
    return _rolling_max(score, _TD_YEAR)


def mdv_138_obv_divg_strength_grade_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV divergence strength: normalized OBV gap at 63d price-low * divergence flag."""
    gap = mdv_105_obv_gap_at_price_low_63d(close, volume)
    obv = _obv(close, volume)
    obv_std = _rolling_std(obv, _TD_QTR).clip(lower=_EPS)
    return _safe_div(gap, obv_std)


def mdv_139_obv_divg_strength_pctrank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct-rank of OBV divergence strength grade within trailing 252 days."""
    grade = mdv_138_obv_divg_strength_grade_63d(close, volume)
    return _pct_rank(grade, _TD_YEAR)


def mdv_140_rsi14_divg_recency_21d(close: pd.Series) -> pd.Series:
    """Days since last RSI(14) regular bullish divergence flag (21-day detection)."""
    rsi = _rsi(close, 14)
    flag = _price_new_low(close, _TD_MON) * (1.0 - _osc_lower_low(rsi, _TD_MON))
    return _days_since_flag(flag)


def mdv_141_macd_divg_recency_63d(close: pd.Series) -> pd.Series:
    """Days since last MACD regular bullish divergence flag (63-day detection)."""
    macd = _macd_line(close)
    flag = _price_new_low(close, _TD_QTR) * (1.0 - _osc_lower_low(macd, _TD_QTR))
    return _days_since_flag(flag)


def mdv_142_composite_divg_recency_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Recency score: inverse of bars since last multi-osc agreement event (capped at 252)."""
    rsi = _rsi(close, 14)
    macd = _macd_line(close)
    price_nl = _price_new_low(close, _TD_QTR)
    rsi_flag = price_nl * (1.0 - _osc_lower_low(rsi, _TD_QTR))
    macd_flag = price_nl * (1.0 - _osc_lower_low(macd, _TD_QTR))
    joint_flag = (rsi_flag * macd_flag)
    recency = _days_since_flag(joint_flag).clip(upper=_TD_YEAR)
    return _safe_div(pd.Series(1.0, index=close.index), recency.clip(lower=_EPS))


def mdv_143_multi_osc_hidden_agreement_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of oscillators (RSI/MACD/Stoch) showing hidden bullish divergence at 63d; 0-3."""
    return mdv_099_composite_hidden_bull_score_63d(close, high, low)


def mdv_144_multi_osc_hidden_agreement_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of oscillators (RSI/MACD/Stoch) showing hidden bullish divergence at 252d; 0-3."""
    return mdv_100_composite_hidden_bull_score_252d(close, high, low)


def mdv_145_rsi14_regular_plus_hidden_strength(close: pd.Series) -> pd.Series:
    """Combined RSI divergence signal: regular gap * hidden flag (both present = stronger)."""
    gap = mdv_006_rsi14_gap_at_price_low_63d_local(close)
    hidden = mdv_077_rsi14_hidden_bull_divg_flag_63d(close)
    return gap * (1.0 + hidden)


def mdv_006_rsi14_gap_at_price_low_63d_local(close: pd.Series) -> pd.Series:
    """RSI(14) minus its 63-day min at each 63-day price-new-low bar (local)."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_floor = _rolling_min(rsi, _TD_QTR)
    return (rsi - rsi_floor).clip(lower=0.0) * price_nl


def mdv_146_obv_plus_rsi_divg_strength(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Strength when both OBV and RSI signal regular bullish divergence (product of z-scores)."""
    rsi_z = mdv_121_rsi14_divg_gap_zscore_63d(close)
    obv_z = mdv_124_obv_divg_gap_zscore_63d(close, volume)
    joint = mdv_120_obv_rsi_joint_divg_flag_63d(close, volume)
    return (rsi_z + obv_z).clip(lower=0.0) * joint


def mdv_147_divg_agreement_cluster_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars with 3+ oscillator agreement in trailing 252 days (cluster intensity)."""
    score = mdv_128_multi_osc_divg_agreement_score_63d(close, high, low)
    high_agree = (score >= 3.0).astype(float)
    return _rolling_sum(high_agree, _TD_YEAR)


def mdv_148_grand_strength_with_obv(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Grand strength: 5-oscillator agreement * avg gap grade (RSI/MACD/Stoch/ROC/OBV)."""
    agreement = mdv_130_multi_osc_with_obv_agreement_63d(close, high, low, volume)
    gap_avg = mdv_127_composite_divg_gap_avg_63d(close, high, low)
    return agreement * gap_avg.clip(lower=0.0)


def mdv_149_hidden_bull_recency_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Inverse recency of composite hidden bullish divergence event (63d composite)."""
    flag = (mdv_099_composite_hidden_bull_score_63d(close, high, low) >= 2.0).astype(float)
    recency = _days_since_flag(flag).clip(upper=_TD_YEAR)
    return _safe_div(pd.Series(1.0, index=close.index), recency.clip(lower=_EPS))


def mdv_150_ultimate_divg_strength_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ultimate: 5-osc agreement * hidden score * OBV confirmation * gap grade (max signal confluence)."""
    agree = mdv_128_multi_osc_divg_agreement_score_63d(close, high, low)
    hidden = mdv_099_composite_hidden_bull_score_63d(close, high, low)
    obv_flag = mdv_102_obv_regular_divg_flag_63d(close, volume)
    gap = mdv_127_composite_divg_gap_avg_63d(close, high, low).clip(lower=0.0)
    return agree * (1.0 + hidden) * (1.0 + obv_flag) * (1.0 + gap)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DIVERGENCE_REGISTRY_076_150 = {
    "mdv_076_rsi14_hidden_bull_divg_flag_21d": {"inputs": ["close"], "func": mdv_076_rsi14_hidden_bull_divg_flag_21d},
    "mdv_077_rsi14_hidden_bull_divg_flag_63d": {"inputs": ["close"], "func": mdv_077_rsi14_hidden_bull_divg_flag_63d},
    "mdv_078_rsi14_hidden_bull_divg_flag_126d": {"inputs": ["close"], "func": mdv_078_rsi14_hidden_bull_divg_flag_126d},
    "mdv_079_rsi14_hidden_bull_divg_flag_252d": {"inputs": ["close"], "func": mdv_079_rsi14_hidden_bull_divg_flag_252d},
    "mdv_080_rsi14_hidden_bull_divg_magnitude_63d": {"inputs": ["close"], "func": mdv_080_rsi14_hidden_bull_divg_magnitude_63d},
    "mdv_081_rsi7_hidden_bull_divg_flag_21d": {"inputs": ["close"], "func": mdv_081_rsi7_hidden_bull_divg_flag_21d},
    "mdv_082_rsi21_hidden_bull_divg_flag_63d": {"inputs": ["close"], "func": mdv_082_rsi21_hidden_bull_divg_flag_63d},
    "mdv_083_rsi14_hidden_bull_divg_count_63d": {"inputs": ["close"], "func": mdv_083_rsi14_hidden_bull_divg_count_63d},
    "mdv_084_rsi14_hidden_bull_divg_count_252d": {"inputs": ["close"], "func": mdv_084_rsi14_hidden_bull_divg_count_252d},
    "mdv_085_rsi14_hidden_bull_recency_63d": {"inputs": ["close"], "func": mdv_085_rsi14_hidden_bull_recency_63d},
    "mdv_086_macd_hidden_bull_divg_flag_21d": {"inputs": ["close"], "func": mdv_086_macd_hidden_bull_divg_flag_21d},
    "mdv_087_macd_hidden_bull_divg_flag_63d": {"inputs": ["close"], "func": mdv_087_macd_hidden_bull_divg_flag_63d},
    "mdv_088_macd_hidden_bull_divg_flag_252d": {"inputs": ["close"], "func": mdv_088_macd_hidden_bull_divg_flag_252d},
    "mdv_089_macd_hidden_bull_divg_magnitude_63d": {"inputs": ["close"], "func": mdv_089_macd_hidden_bull_divg_magnitude_63d},
    "mdv_090_macd_hidden_bull_divg_count_63d": {"inputs": ["close"], "func": mdv_090_macd_hidden_bull_divg_count_63d},
    "mdv_091_macd_hidden_bull_divg_count_252d": {"inputs": ["close"], "func": mdv_091_macd_hidden_bull_divg_count_252d},
    "mdv_092_macd_hidden_bull_recency_63d": {"inputs": ["close"], "func": mdv_092_macd_hidden_bull_recency_63d},
    "mdv_093_stoch_hidden_bull_divg_flag_21d": {"inputs": ["close", "high", "low"], "func": mdv_093_stoch_hidden_bull_divg_flag_21d},
    "mdv_094_stoch_hidden_bull_divg_flag_63d": {"inputs": ["close", "high", "low"], "func": mdv_094_stoch_hidden_bull_divg_flag_63d},
    "mdv_095_stoch_hidden_bull_divg_flag_252d": {"inputs": ["close", "high", "low"], "func": mdv_095_stoch_hidden_bull_divg_flag_252d},
    "mdv_096_stoch_hidden_bull_divg_magnitude_63d": {"inputs": ["close", "high", "low"], "func": mdv_096_stoch_hidden_bull_divg_magnitude_63d},
    "mdv_097_stoch_hidden_bull_divg_count_252d": {"inputs": ["close", "high", "low"], "func": mdv_097_stoch_hidden_bull_divg_count_252d},
    "mdv_098_composite_hidden_bull_score_21d": {"inputs": ["close", "high", "low"], "func": mdv_098_composite_hidden_bull_score_21d},
    "mdv_099_composite_hidden_bull_score_63d": {"inputs": ["close", "high", "low"], "func": mdv_099_composite_hidden_bull_score_63d},
    "mdv_100_composite_hidden_bull_score_252d": {"inputs": ["close", "high", "low"], "func": mdv_100_composite_hidden_bull_score_252d},
    "mdv_101_obv_regular_divg_flag_21d": {"inputs": ["close", "volume"], "func": mdv_101_obv_regular_divg_flag_21d},
    "mdv_102_obv_regular_divg_flag_63d": {"inputs": ["close", "volume"], "func": mdv_102_obv_regular_divg_flag_63d},
    "mdv_103_obv_regular_divg_flag_126d": {"inputs": ["close", "volume"], "func": mdv_103_obv_regular_divg_flag_126d},
    "mdv_104_obv_regular_divg_flag_252d": {"inputs": ["close", "volume"], "func": mdv_104_obv_regular_divg_flag_252d},
    "mdv_105_obv_gap_at_price_low_63d": {"inputs": ["close", "volume"], "func": mdv_105_obv_gap_at_price_low_63d},
    "mdv_106_obv_gap_at_price_low_252d": {"inputs": ["close", "volume"], "func": mdv_106_obv_gap_at_price_low_252d},
    "mdv_107_obv_pctrank_spread_63d": {"inputs": ["close", "volume"], "func": mdv_107_obv_pctrank_spread_63d},
    "mdv_108_obv_pctrank_spread_252d": {"inputs": ["close", "volume"], "func": mdv_108_obv_pctrank_spread_252d},
    "mdv_109_obv_regular_divg_count_63d": {"inputs": ["close", "volume"], "func": mdv_109_obv_regular_divg_count_63d},
    "mdv_110_obv_regular_divg_count_252d": {"inputs": ["close", "volume"], "func": mdv_110_obv_regular_divg_count_252d},
    "mdv_111_obv_hidden_bull_divg_flag_21d": {"inputs": ["close", "volume"], "func": mdv_111_obv_hidden_bull_divg_flag_21d},
    "mdv_112_obv_hidden_bull_divg_flag_63d": {"inputs": ["close", "volume"], "func": mdv_112_obv_hidden_bull_divg_flag_63d},
    "mdv_113_obv_hidden_bull_divg_flag_252d": {"inputs": ["close", "volume"], "func": mdv_113_obv_hidden_bull_divg_flag_252d},
    "mdv_114_obv_hidden_bull_divg_count_252d": {"inputs": ["close", "volume"], "func": mdv_114_obv_hidden_bull_divg_count_252d},
    "mdv_115_obv_divg_recency_63d": {"inputs": ["close", "volume"], "func": mdv_115_obv_divg_recency_63d},
    "mdv_116_obv_slope_divg_flag_63d": {"inputs": ["close", "volume"], "func": mdv_116_obv_slope_divg_flag_63d},
    "mdv_117_obv_slope_divg_flag_252d": {"inputs": ["close", "volume"], "func": mdv_117_obv_slope_divg_flag_252d},
    "mdv_118_obv_pctrank_spread_pctrank_252d": {"inputs": ["close", "volume"], "func": mdv_118_obv_pctrank_spread_pctrank_252d},
    "mdv_119_obv_gap_max_252d": {"inputs": ["close", "volume"], "func": mdv_119_obv_gap_max_252d},
    "mdv_120_obv_rsi_joint_divg_flag_63d": {"inputs": ["close", "volume"], "func": mdv_120_obv_rsi_joint_divg_flag_63d},
    "mdv_121_rsi14_divg_gap_zscore_63d": {"inputs": ["close"], "func": mdv_121_rsi14_divg_gap_zscore_63d},
    "mdv_122_macd_divg_gap_zscore_63d": {"inputs": ["close"], "func": mdv_122_macd_divg_gap_zscore_63d},
    "mdv_123_stoch_divg_gap_zscore_63d": {"inputs": ["close", "high", "low"], "func": mdv_123_stoch_divg_gap_zscore_63d},
    "mdv_124_obv_divg_gap_zscore_63d": {"inputs": ["close", "volume"], "func": mdv_124_obv_divg_gap_zscore_63d},
    "mdv_125_rsi14_divg_gap_pctrank_252d": {"inputs": ["close"], "func": mdv_125_rsi14_divg_gap_pctrank_252d},
    "mdv_126_macd_divg_gap_pctrank_252d": {"inputs": ["close"], "func": mdv_126_macd_divg_gap_pctrank_252d},
    "mdv_127_composite_divg_gap_avg_63d": {"inputs": ["close", "high", "low"], "func": mdv_127_composite_divg_gap_avg_63d},
    "mdv_128_multi_osc_divg_agreement_score_63d": {"inputs": ["close", "high", "low"], "func": mdv_128_multi_osc_divg_agreement_score_63d},
    "mdv_129_multi_osc_divg_agreement_score_252d": {"inputs": ["close", "high", "low"], "func": mdv_129_multi_osc_divg_agreement_score_252d},
    "mdv_130_multi_osc_with_obv_agreement_63d": {"inputs": ["close", "high", "low", "volume"], "func": mdv_130_multi_osc_with_obv_agreement_63d},
    "mdv_131_divg_agreement_score_pctrank_252d": {"inputs": ["close", "high", "low"], "func": mdv_131_divg_agreement_score_pctrank_252d},
    "mdv_132_four_osc_all_agree_divg_63d": {"inputs": ["close", "high", "low"], "func": mdv_132_four_osc_all_agree_divg_63d},
    "mdv_133_divg_strength_grade_63d": {"inputs": ["close", "high", "low"], "func": mdv_133_divg_strength_grade_63d},
    "mdv_134_divg_strength_grade_252d": {"inputs": ["close", "high", "low"], "func": mdv_134_divg_strength_grade_252d},
    "mdv_135_rsi14_hidden_vs_regular_ratio_63d": {"inputs": ["close"], "func": mdv_135_rsi14_hidden_vs_regular_ratio_63d},
    "mdv_136_hidden_bull_divg_score_rolling_max_63d": {"inputs": ["close", "high", "low"], "func": mdv_136_hidden_bull_divg_score_rolling_max_63d},
    "mdv_137_hidden_bull_divg_score_rolling_max_252d": {"inputs": ["close", "high", "low"], "func": mdv_137_hidden_bull_divg_score_rolling_max_252d},
    "mdv_138_obv_divg_strength_grade_63d": {"inputs": ["close", "volume"], "func": mdv_138_obv_divg_strength_grade_63d},
    "mdv_139_obv_divg_strength_pctrank_252d": {"inputs": ["close", "volume"], "func": mdv_139_obv_divg_strength_pctrank_252d},
    "mdv_140_rsi14_divg_recency_21d": {"inputs": ["close"], "func": mdv_140_rsi14_divg_recency_21d},
    "mdv_141_macd_divg_recency_63d": {"inputs": ["close"], "func": mdv_141_macd_divg_recency_63d},
    "mdv_142_composite_divg_recency_score": {"inputs": ["close", "high", "low"], "func": mdv_142_composite_divg_recency_score},
    "mdv_143_multi_osc_hidden_agreement_63d": {"inputs": ["close", "high", "low"], "func": mdv_143_multi_osc_hidden_agreement_63d},
    "mdv_144_multi_osc_hidden_agreement_252d": {"inputs": ["close", "high", "low"], "func": mdv_144_multi_osc_hidden_agreement_252d},
    "mdv_145_rsi14_regular_plus_hidden_strength": {"inputs": ["close"], "func": mdv_145_rsi14_regular_plus_hidden_strength},
    "mdv_146_obv_plus_rsi_divg_strength": {"inputs": ["close", "volume"], "func": mdv_146_obv_plus_rsi_divg_strength},
    "mdv_147_divg_agreement_cluster_252d": {"inputs": ["close", "high", "low"], "func": mdv_147_divg_agreement_cluster_252d},
    "mdv_148_grand_strength_with_obv": {"inputs": ["close", "high", "low", "volume"], "func": mdv_148_grand_strength_with_obv},
    "mdv_149_hidden_bull_recency_score_63d": {"inputs": ["close", "high", "low"], "func": mdv_149_hidden_bull_recency_score_63d},
    "mdv_150_ultimate_divg_strength_score": {"inputs": ["close", "high", "low", "volume"], "func": mdv_150_ultimate_divg_strength_score},
}
