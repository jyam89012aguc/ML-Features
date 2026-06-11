"""
31_oscillator_extremes — Base Features 001-075
Domain: stochastic / Williams %R style oscillator extreme readings at oversold levels
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
    """Stochastic RSI: stochastic of RSI values."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Fast Stochastic %K oversold levels ---

def osc_001_stoch_k_14_below20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast Stochastic %K (14-day) raw value; low = extreme oversold."""
    return _stoch_k(high, low, close, 14)


def osc_002_stoch_k_14_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 14-day Stochastic %K < 20 (oversold zone)."""
    return (_stoch_k(high, low, close, 14) < 20.0).astype(float)


def osc_003_stoch_k_14_extreme_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 14-day Stochastic %K < 10 (extreme oversold)."""
    return (_stoch_k(high, low, close, 14) < 10.0).astype(float)


def osc_004_stoch_k_14_depth_below20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of 14-day %K below 20 (max(0, 20 - %K)); 0 when not oversold."""
    return (20.0 - _stoch_k(high, low, close, 14)).clip(lower=0.0)


def osc_005_stoch_k_5_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast Stochastic %K (5-day) raw value — shortest lookback extremity."""
    return _stoch_k(high, low, close, _TD_WEEK)


def osc_006_stoch_k_5_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 5-day Stochastic %K < 20."""
    return (_stoch_k(high, low, close, _TD_WEEK) < 20.0).astype(float)


def osc_007_stoch_k_21_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast Stochastic %K (21-day) raw value — monthly lookback."""
    return _stoch_k(high, low, close, _TD_MON)


def osc_008_stoch_k_21_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 21-day Stochastic %K < 20."""
    return (_stoch_k(high, low, close, _TD_MON) < 20.0).astype(float)


def osc_009_stoch_k_63_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast Stochastic %K (63-day) raw value — quarterly lookback."""
    return _stoch_k(high, low, close, _TD_QTR)


def osc_010_stoch_k_63_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 63-day Stochastic %K < 20."""
    return (_stoch_k(high, low, close, _TD_QTR) < 20.0).astype(float)


# --- Group B (011-020): Slow Stochastic %D (smoothed %K) oversold levels ---

def osc_011_stoch_d_14_3_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow Stochastic %D: 3-day SMA of 14-day %K."""
    return _rolling_mean(_stoch_k(high, low, close, 14), 3)


def osc_012_stoch_d_14_3_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Slow %D (14,3) < 20."""
    return (_rolling_mean(_stoch_k(high, low, close, 14), 3) < 20.0).astype(float)


def osc_013_stoch_d_14_3_extreme_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Slow %D (14,3) < 10 (extreme oversold)."""
    return (_rolling_mean(_stoch_k(high, low, close, 14), 3) < 10.0).astype(float)


def osc_014_stoch_d_14_3_depth_below20(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of Slow %D (14,3) below 20."""
    return (20.0 - _rolling_mean(_stoch_k(high, low, close, 14), 3)).clip(lower=0.0)


def osc_015_stoch_k_minus_d_14_3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fast %K minus Slow %D (14,3) — momentum divergence within oscillator."""
    k = _stoch_k(high, low, close, 14)
    d = _rolling_mean(k, 3)
    return k - d


def osc_016_stoch_d_21_3_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow Stochastic %D: 3-day SMA of 21-day %K."""
    return _rolling_mean(_stoch_k(high, low, close, _TD_MON), 3)


def osc_017_stoch_d_21_3_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 21-day Slow %D < 20."""
    return (_rolling_mean(_stoch_k(high, low, close, _TD_MON), 3) < 20.0).astype(float)


def osc_018_stoch_d_63_3_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slow Stochastic %D: 3-day SMA of 63-day %K."""
    return _rolling_mean(_stoch_k(high, low, close, _TD_QTR), 3)


def osc_019_stoch_d_63_3_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 63-day Slow %D < 20."""
    return (_rolling_mean(_stoch_k(high, low, close, _TD_QTR), 3) < 20.0).astype(float)


def osc_020_stoch_both_k_d_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: both 14-day %K and Slow %D < 20 simultaneously."""
    k = _stoch_k(high, low, close, 14)
    d = _rolling_mean(k, 3)
    return ((k < 20.0) & (d < 20.0)).astype(float)


# --- Group C (021-030): Williams %R oversold levels ---

def osc_021_williams_r_14_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R (14-day) raw value; -80 to -100 = oversold."""
    return _williams_r(high, low, close, 14)


def osc_022_williams_r_14_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Williams %R (14-day) < -80."""
    return (_williams_r(high, low, close, 14) < -80.0).astype(float)


def osc_023_williams_r_14_extreme_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Williams %R (14-day) < -90 (extreme oversold)."""
    return (_williams_r(high, low, close, 14) < -90.0).astype(float)


def osc_024_williams_r_14_depth_below80(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of Williams %R below -80 threshold (abs distance into oversold)."""
    return (_williams_r(high, low, close, 14) + 80.0).clip(upper=0.0).abs()


def osc_025_williams_r_5_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R (5-day) raw value — short-term sensitivity."""
    return _williams_r(high, low, close, _TD_WEEK)


def osc_026_williams_r_21_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R (21-day) raw value — monthly lookback."""
    return _williams_r(high, low, close, _TD_MON)


def osc_027_williams_r_21_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Williams %R (21-day) < -80."""
    return (_williams_r(high, low, close, _TD_MON) < -80.0).astype(float)


def osc_028_williams_r_63_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams %R (63-day) raw value — quarterly lookback."""
    return _williams_r(high, low, close, _TD_QTR)


def osc_029_williams_r_63_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Williams %R (63-day) < -80."""
    return (_williams_r(high, low, close, _TD_QTR) < -80.0).astype(float)


def osc_030_williams_r_14_min_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of Williams %R (14-day) — most oversold recently."""
    wr = _williams_r(high, low, close, 14)
    return _rolling_min(wr, _TD_MON)


# --- Group D (031-040): CCI extreme readings ---

def osc_031_cci_14_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI (14-day) raw value; below -100 = oversold."""
    return _cci(high, low, close, 14)


def osc_032_cci_14_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: CCI (14-day) < -100."""
    return (_cci(high, low, close, 14) < -100.0).astype(float)


def osc_033_cci_14_extreme_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: CCI (14-day) < -200 (extreme oversold)."""
    return (_cci(high, low, close, 14) < -200.0).astype(float)


def osc_034_cci_14_depth_below100(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of CCI below -100 (abs excess below -100)."""
    return (_cci(high, low, close, 14) + 100.0).clip(upper=0.0).abs()


def osc_035_cci_21_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI (21-day) raw value."""
    return _cci(high, low, close, _TD_MON)


def osc_036_cci_21_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: CCI (21-day) < -100."""
    return (_cci(high, low, close, _TD_MON) < -100.0).astype(float)


def osc_037_cci_63_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI (63-day) raw value — quarterly lookback."""
    return _cci(high, low, close, _TD_QTR)


def osc_038_cci_63_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: CCI (63-day) < -100."""
    return (_cci(high, low, close, _TD_QTR) < -100.0).astype(float)


def osc_039_cci_14_min_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of 14-day CCI — worst reading in past month."""
    return _rolling_min(_cci(high, low, close, 14), _TD_MON)


def osc_040_cci_14_min_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of 14-day CCI — worst reading in past quarter."""
    return _rolling_min(_cci(high, low, close, 14), _TD_QTR)


# --- Group E (041-050): Money Flow Index (MFI) oversold levels ---

def osc_041_mfi_14_raw(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Money Flow Index (14-day) raw value; below 20 = oversold."""
    return _mfi(high, low, close, volume, 14)


def osc_042_mfi_14_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: MFI (14-day) < 20."""
    return (_mfi(high, low, close, volume, 14) < 20.0).astype(float)


def osc_043_mfi_14_extreme_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: MFI (14-day) < 10 (extreme oversold)."""
    return (_mfi(high, low, close, volume, 14) < 10.0).astype(float)


def osc_044_mfi_14_depth_below20(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Depth of MFI (14-day) below 20."""
    return (20.0 - _mfi(high, low, close, volume, 14)).clip(lower=0.0)


def osc_045_mfi_21_raw(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Money Flow Index (21-day) raw value."""
    return _mfi(high, low, close, volume, _TD_MON)


def osc_046_mfi_21_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: MFI (21-day) < 20."""
    return (_mfi(high, low, close, volume, _TD_MON) < 20.0).astype(float)


def osc_047_mfi_63_raw(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Money Flow Index (63-day) raw value — quarterly window."""
    return _mfi(high, low, close, volume, _TD_QTR)


def osc_048_mfi_63_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: MFI (63-day) < 20."""
    return (_mfi(high, low, close, volume, _TD_QTR) < 20.0).astype(float)


def osc_049_mfi_14_min_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of 14-day MFI."""
    return _rolling_min(_mfi(high, low, close, volume, 14), _TD_MON)


def osc_050_mfi_14_min_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of 14-day MFI."""
    return _rolling_min(_mfi(high, low, close, volume, 14), _TD_QTR)


# --- Group F (051-060): Stochastic RSI oversold levels ---

def osc_051_stoch_rsi_14_14_raw(close: pd.Series) -> pd.Series:
    """Stochastic RSI (RSI=14, Stoch=14) raw value; 0-100."""
    return _stoch_rsi(close, 14, 14)


def osc_052_stoch_rsi_14_14_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI (14,14) < 20."""
    return (_stoch_rsi(close, 14, 14) < 20.0).astype(float)


def osc_053_stoch_rsi_14_14_extreme_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI (14,14) < 5 (extreme oversold)."""
    return (_stoch_rsi(close, 14, 14) < 5.0).astype(float)


def osc_054_stoch_rsi_14_14_depth_below20(close: pd.Series) -> pd.Series:
    """Depth of StochRSI (14,14) below 20."""
    return (20.0 - _stoch_rsi(close, 14, 14)).clip(lower=0.0)


def osc_055_stoch_rsi_14_14_min_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of StochRSI (14,14)."""
    return _rolling_min(_stoch_rsi(close, 14, 14), _TD_MON)


def osc_056_stoch_rsi_21_21_raw(close: pd.Series) -> pd.Series:
    """Stochastic RSI (RSI=21, Stoch=21) raw value."""
    return _stoch_rsi(close, _TD_MON, _TD_MON)


def osc_057_stoch_rsi_21_21_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI (21,21) < 20."""
    return (_stoch_rsi(close, _TD_MON, _TD_MON) < 20.0).astype(float)


def osc_058_stoch_rsi_14_21_raw(close: pd.Series) -> pd.Series:
    """Stochastic RSI (RSI=14, Stoch=21) — broader stochastic window."""
    return _stoch_rsi(close, 14, _TD_MON)


def osc_059_stoch_rsi_14_21_oversold_flag(close: pd.Series) -> pd.Series:
    """Binary flag: StochRSI (14,21) < 20."""
    return (_stoch_rsi(close, 14, _TD_MON) < 20.0).astype(float)


def osc_060_stoch_rsi_14_14_d_line(close: pd.Series) -> pd.Series:
    """Signal line of StochRSI: 3-day SMA of StochRSI(14,14)."""
    return _rolling_mean(_stoch_rsi(close, 14, 14), 3)


# --- Group G (061-075): Ultimate Oscillator, consecutive extreme days, percentile ranks ---

def osc_061_ultimate_osc_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ultimate Oscillator (7/14/28) raw value; below 30 = oversold."""
    return _ultimate_osc(high, low, close)


def osc_062_ultimate_osc_oversold_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Ultimate Oscillator < 30."""
    return (_ultimate_osc(high, low, close) < 30.0).astype(float)


def osc_063_ultimate_osc_extreme_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: Ultimate Oscillator < 20 (extreme oversold)."""
    return (_ultimate_osc(high, low, close) < 20.0).astype(float)


def osc_064_ultimate_osc_depth_below30(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Depth of Ultimate Oscillator below 30."""
    return (30.0 - _ultimate_osc(high, low, close)).clip(lower=0.0)


def osc_065_ultimate_osc_min_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day minimum of Ultimate Oscillator."""
    return _rolling_min(_ultimate_osc(high, low, close), _TD_MON)


def osc_066_stoch_k_14_consec_oversold_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days with 14-day Stochastic %K < 20 (streak in oversold zone)."""
    return _consec_streak(_stoch_k(high, low, close, 14) < 20.0)


def osc_067_williams_r_14_consec_oversold_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days with Williams %R (14-day) < -80."""
    return _consec_streak(_williams_r(high, low, close, 14) < -80.0)


def osc_068_cci_14_consec_oversold_days(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days with CCI (14-day) < -100."""
    return _consec_streak(_cci(high, low, close, 14) < -100.0)


def osc_069_mfi_14_consec_oversold_days(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days with MFI (14-day) < 20."""
    return _consec_streak(_mfi(high, low, close, volume, 14) < 20.0)


def osc_070_stoch_rsi_14_14_consec_oversold_days(close: pd.Series) -> pd.Series:
    """Consecutive days with StochRSI (14,14) < 20."""
    return _consec_streak(_stoch_rsi(close, 14, 14) < 20.0)


def osc_071_stoch_k_14_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 14-day Stochastic %K within trailing 252 days."""
    k = _stoch_k(high, low, close, 14)
    return k.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_072_williams_r_14_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 14-day Williams %R within trailing 252 days (low = extreme)."""
    wr = _williams_r(high, low, close, 14)
    return wr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_073_cci_14_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 14-day CCI within trailing 252 days."""
    return _cci(high, low, close, 14).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_074_mfi_14_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 14-day MFI within trailing 252 days."""
    return _mfi(high, low, close, volume, 14).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def osc_075_stoch_rsi_14_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of StochRSI (14,14) within trailing 252 days."""
    return _stoch_rsi(close, 14, 14).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_REGISTRY_001_075 = {
    "osc_001_stoch_k_14_below20": {"inputs": ["high", "low", "close"], "func": osc_001_stoch_k_14_below20},
    "osc_002_stoch_k_14_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_002_stoch_k_14_oversold_flag},
    "osc_003_stoch_k_14_extreme_flag": {"inputs": ["high", "low", "close"], "func": osc_003_stoch_k_14_extreme_flag},
    "osc_004_stoch_k_14_depth_below20": {"inputs": ["high", "low", "close"], "func": osc_004_stoch_k_14_depth_below20},
    "osc_005_stoch_k_5_raw": {"inputs": ["high", "low", "close"], "func": osc_005_stoch_k_5_raw},
    "osc_006_stoch_k_5_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_006_stoch_k_5_oversold_flag},
    "osc_007_stoch_k_21_raw": {"inputs": ["high", "low", "close"], "func": osc_007_stoch_k_21_raw},
    "osc_008_stoch_k_21_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_008_stoch_k_21_oversold_flag},
    "osc_009_stoch_k_63_raw": {"inputs": ["high", "low", "close"], "func": osc_009_stoch_k_63_raw},
    "osc_010_stoch_k_63_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_010_stoch_k_63_oversold_flag},
    "osc_011_stoch_d_14_3_raw": {"inputs": ["high", "low", "close"], "func": osc_011_stoch_d_14_3_raw},
    "osc_012_stoch_d_14_3_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_012_stoch_d_14_3_oversold_flag},
    "osc_013_stoch_d_14_3_extreme_flag": {"inputs": ["high", "low", "close"], "func": osc_013_stoch_d_14_3_extreme_flag},
    "osc_014_stoch_d_14_3_depth_below20": {"inputs": ["high", "low", "close"], "func": osc_014_stoch_d_14_3_depth_below20},
    "osc_015_stoch_k_minus_d_14_3": {"inputs": ["high", "low", "close"], "func": osc_015_stoch_k_minus_d_14_3},
    "osc_016_stoch_d_21_3_raw": {"inputs": ["high", "low", "close"], "func": osc_016_stoch_d_21_3_raw},
    "osc_017_stoch_d_21_3_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_017_stoch_d_21_3_oversold_flag},
    "osc_018_stoch_d_63_3_raw": {"inputs": ["high", "low", "close"], "func": osc_018_stoch_d_63_3_raw},
    "osc_019_stoch_d_63_3_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_019_stoch_d_63_3_oversold_flag},
    "osc_020_stoch_both_k_d_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_020_stoch_both_k_d_oversold_flag},
    "osc_021_williams_r_14_raw": {"inputs": ["high", "low", "close"], "func": osc_021_williams_r_14_raw},
    "osc_022_williams_r_14_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_022_williams_r_14_oversold_flag},
    "osc_023_williams_r_14_extreme_flag": {"inputs": ["high", "low", "close"], "func": osc_023_williams_r_14_extreme_flag},
    "osc_024_williams_r_14_depth_below80": {"inputs": ["high", "low", "close"], "func": osc_024_williams_r_14_depth_below80},
    "osc_025_williams_r_5_raw": {"inputs": ["high", "low", "close"], "func": osc_025_williams_r_5_raw},
    "osc_026_williams_r_21_raw": {"inputs": ["high", "low", "close"], "func": osc_026_williams_r_21_raw},
    "osc_027_williams_r_21_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_027_williams_r_21_oversold_flag},
    "osc_028_williams_r_63_raw": {"inputs": ["high", "low", "close"], "func": osc_028_williams_r_63_raw},
    "osc_029_williams_r_63_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_029_williams_r_63_oversold_flag},
    "osc_030_williams_r_14_min_21d": {"inputs": ["high", "low", "close"], "func": osc_030_williams_r_14_min_21d},
    "osc_031_cci_14_raw": {"inputs": ["high", "low", "close"], "func": osc_031_cci_14_raw},
    "osc_032_cci_14_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_032_cci_14_oversold_flag},
    "osc_033_cci_14_extreme_flag": {"inputs": ["high", "low", "close"], "func": osc_033_cci_14_extreme_flag},
    "osc_034_cci_14_depth_below100": {"inputs": ["high", "low", "close"], "func": osc_034_cci_14_depth_below100},
    "osc_035_cci_21_raw": {"inputs": ["high", "low", "close"], "func": osc_035_cci_21_raw},
    "osc_036_cci_21_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_036_cci_21_oversold_flag},
    "osc_037_cci_63_raw": {"inputs": ["high", "low", "close"], "func": osc_037_cci_63_raw},
    "osc_038_cci_63_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_038_cci_63_oversold_flag},
    "osc_039_cci_14_min_21d": {"inputs": ["high", "low", "close"], "func": osc_039_cci_14_min_21d},
    "osc_040_cci_14_min_63d": {"inputs": ["high", "low", "close"], "func": osc_040_cci_14_min_63d},
    "osc_041_mfi_14_raw": {"inputs": ["high", "low", "close", "volume"], "func": osc_041_mfi_14_raw},
    "osc_042_mfi_14_oversold_flag": {"inputs": ["high", "low", "close", "volume"], "func": osc_042_mfi_14_oversold_flag},
    "osc_043_mfi_14_extreme_flag": {"inputs": ["high", "low", "close", "volume"], "func": osc_043_mfi_14_extreme_flag},
    "osc_044_mfi_14_depth_below20": {"inputs": ["high", "low", "close", "volume"], "func": osc_044_mfi_14_depth_below20},
    "osc_045_mfi_21_raw": {"inputs": ["high", "low", "close", "volume"], "func": osc_045_mfi_21_raw},
    "osc_046_mfi_21_oversold_flag": {"inputs": ["high", "low", "close", "volume"], "func": osc_046_mfi_21_oversold_flag},
    "osc_047_mfi_63_raw": {"inputs": ["high", "low", "close", "volume"], "func": osc_047_mfi_63_raw},
    "osc_048_mfi_63_oversold_flag": {"inputs": ["high", "low", "close", "volume"], "func": osc_048_mfi_63_oversold_flag},
    "osc_049_mfi_14_min_21d": {"inputs": ["high", "low", "close", "volume"], "func": osc_049_mfi_14_min_21d},
    "osc_050_mfi_14_min_63d": {"inputs": ["high", "low", "close", "volume"], "func": osc_050_mfi_14_min_63d},
    "osc_051_stoch_rsi_14_14_raw": {"inputs": ["close"], "func": osc_051_stoch_rsi_14_14_raw},
    "osc_052_stoch_rsi_14_14_oversold_flag": {"inputs": ["close"], "func": osc_052_stoch_rsi_14_14_oversold_flag},
    "osc_053_stoch_rsi_14_14_extreme_flag": {"inputs": ["close"], "func": osc_053_stoch_rsi_14_14_extreme_flag},
    "osc_054_stoch_rsi_14_14_depth_below20": {"inputs": ["close"], "func": osc_054_stoch_rsi_14_14_depth_below20},
    "osc_055_stoch_rsi_14_14_min_21d": {"inputs": ["close"], "func": osc_055_stoch_rsi_14_14_min_21d},
    "osc_056_stoch_rsi_21_21_raw": {"inputs": ["close"], "func": osc_056_stoch_rsi_21_21_raw},
    "osc_057_stoch_rsi_21_21_oversold_flag": {"inputs": ["close"], "func": osc_057_stoch_rsi_21_21_oversold_flag},
    "osc_058_stoch_rsi_14_21_raw": {"inputs": ["close"], "func": osc_058_stoch_rsi_14_21_raw},
    "osc_059_stoch_rsi_14_21_oversold_flag": {"inputs": ["close"], "func": osc_059_stoch_rsi_14_21_oversold_flag},
    "osc_060_stoch_rsi_14_14_d_line": {"inputs": ["close"], "func": osc_060_stoch_rsi_14_14_d_line},
    "osc_061_ultimate_osc_raw": {"inputs": ["high", "low", "close"], "func": osc_061_ultimate_osc_raw},
    "osc_062_ultimate_osc_oversold_flag": {"inputs": ["high", "low", "close"], "func": osc_062_ultimate_osc_oversold_flag},
    "osc_063_ultimate_osc_extreme_flag": {"inputs": ["high", "low", "close"], "func": osc_063_ultimate_osc_extreme_flag},
    "osc_064_ultimate_osc_depth_below30": {"inputs": ["high", "low", "close"], "func": osc_064_ultimate_osc_depth_below30},
    "osc_065_ultimate_osc_min_21d": {"inputs": ["high", "low", "close"], "func": osc_065_ultimate_osc_min_21d},
    "osc_066_stoch_k_14_consec_oversold_days": {"inputs": ["high", "low", "close"], "func": osc_066_stoch_k_14_consec_oversold_days},
    "osc_067_williams_r_14_consec_oversold_days": {"inputs": ["high", "low", "close"], "func": osc_067_williams_r_14_consec_oversold_days},
    "osc_068_cci_14_consec_oversold_days": {"inputs": ["high", "low", "close"], "func": osc_068_cci_14_consec_oversold_days},
    "osc_069_mfi_14_consec_oversold_days": {"inputs": ["high", "low", "close", "volume"], "func": osc_069_mfi_14_consec_oversold_days},
    "osc_070_stoch_rsi_14_14_consec_oversold_days": {"inputs": ["close"], "func": osc_070_stoch_rsi_14_14_consec_oversold_days},
    "osc_071_stoch_k_14_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": osc_071_stoch_k_14_pct_rank_252d},
    "osc_072_williams_r_14_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": osc_072_williams_r_14_pct_rank_252d},
    "osc_073_cci_14_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": osc_073_cci_14_pct_rank_252d},
    "osc_074_mfi_14_pct_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": osc_074_mfi_14_pct_rank_252d},
    "osc_075_stoch_rsi_14_pct_rank_252d": {"inputs": ["close"], "func": osc_075_stoch_rsi_14_pct_rank_252d},
}
