"""
106_support_violation — Extended Features 001-075
Domain: violation of historical support — deeper variants including multi-year lows,
        Fibonacci retracement support, Keltner-channel-based support, price-at-volume
        support proxies, EMA/SMA support levels, pivot-point support, and
        cross-confirmation composites.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


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


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    return (support - price).clip(lower=0.0)


def _pct_depth_below(price: pd.Series, support: pd.Series) -> pd.Series:
    depth = (support - price).clip(lower=0.0)
    return _safe_div(depth, support.clip(lower=_EPS))


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(tr, w)


def _ema_support(close: pd.Series, span: int) -> pd.Series:
    """EMA of close with given span, shifted 1 day as a support level."""
    return _ewm_mean(close, span).shift(1)


def _sma_support(close: pd.Series, w: int) -> pd.Series:
    """SMA of close over w days, shifted 1 day as a support level."""
    return _rolling_mean(close, w).shift(1)


def _keltner_lower(close: pd.Series, high: pd.Series, low: pd.Series,
                   ema_span: int, atr_w: int, mult: float) -> pd.Series:
    """Keltner Channel lower band: EMA - mult * ATR (shifted 1 day)."""
    ema = _ewm_mean(close, ema_span)
    atr_val = _atr(high, low, close, atr_w)
    return (ema - mult * atr_val).shift(1)


def _vwap_approx(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Approximate rolling VWAP over w days (shifted 1 day)."""
    dollar_vol = close * volume
    return _safe_div(
        dollar_vol.rolling(w, min_periods=max(1, w // 2)).sum(),
        volume.rolling(w, min_periods=max(1, w // 2)).sum()
    ).shift(1)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Multi-year and very long-term support ---

def sv_ext_001_close_depth_below_3yr_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 3-year (756-day) trailing low."""
    support = low.shift(1).rolling(756, min_periods=126).min()
    return _depth_below(close, support)


def sv_ext_002_close_pct_depth_below_3yr_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the prior 3-year trailing low."""
    support = low.shift(1).rolling(756, min_periods=126).min()
    return _pct_depth_below(close, support)


def sv_ext_003_close_below_3yr_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below the prior 3-year trailing low."""
    support = low.shift(1).rolling(756, min_periods=126).min()
    return (close < support).astype(float)


def sv_ext_004_close_depth_below_5yr_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 5-year (1260-day) trailing low."""
    support = low.shift(1).rolling(1260, min_periods=252).min()
    return _depth_below(close, support)


def sv_ext_005_close_below_5yr_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below the prior 5-year trailing low."""
    support = low.shift(1).rolling(1260, min_periods=252).min()
    return (close < support).astype(float)


def sv_ext_006_expanding_low_pct_depth(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the all-time expanding minimum of lows."""
    support = low.shift(1).expanding(min_periods=1).min()
    return _pct_depth_below(close, support)


def sv_ext_007_expanding_low_break_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close is below the all-time expanding minimum low."""
    support = low.shift(1).expanding(min_periods=1).min()
    return (close < support).astype(float)


def sv_ext_008_consec_below_3yr_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days close has been below the prior 3-year trailing low."""
    support = low.shift(1).rolling(756, min_periods=126).min()
    return _consec_streak(close < support)


def sv_ext_009_3yr_low_pct_depth_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of pct-depth below 3-year low within its 252-day distribution."""
    support = low.shift(1).rolling(756, min_periods=126).min()
    depth = _pct_depth_below(close, support)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_ext_010_multi_year_break_composite(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of binary breaks across 1yr, 2yr, 3yr trailing lows."""
    s252 = _prior_low(low, _TD_YEAR)
    s504 = low.shift(1).rolling(504, min_periods=126).min()
    s756 = low.shift(1).rolling(756, min_periods=126).min()
    return ((close < s252).astype(float) + (close < s504).astype(float) +
            (close < s756).astype(float))


# --- Group B (011-020): EMA and SMA dynamic support levels ---

def sv_ext_011_close_depth_below_ema50(close: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior day's 50-day EMA."""
    support = _ema_support(close, 50)
    return _depth_below(close, support)


def sv_ext_012_close_depth_below_ema200(close: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior day's 200-day EMA."""
    support = _ema_support(close, 200)
    return _depth_below(close, support)


def sv_ext_013_close_pct_depth_below_ema50(close: pd.Series) -> pd.Series:
    """Percentage depth of close below the 50-day EMA support."""
    support = _ema_support(close, 50)
    return _pct_depth_below(close, support)


def sv_ext_014_close_pct_depth_below_ema200(close: pd.Series) -> pd.Series:
    """Percentage depth of close below the 200-day EMA support."""
    support = _ema_support(close, 200)
    return _pct_depth_below(close, support)


def sv_ext_015_close_below_ema200_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below the 200-day EMA."""
    support = _ema_support(close, 200)
    return (close < support).astype(float)


def sv_ext_016_close_below_sma200_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below the 200-day SMA."""
    support = _sma_support(close, 200)
    return (close < support).astype(float)


def sv_ext_017_close_pct_depth_below_sma200(close: pd.Series) -> pd.Series:
    """Percentage depth of close below the 200-day SMA support."""
    support = _sma_support(close, 200)
    return _pct_depth_below(close, support)


def sv_ext_018_close_depth_below_sma50(close: pd.Series) -> pd.Series:
    """Absolute depth of close below the 50-day SMA support."""
    support = _sma_support(close, 50)
    return _depth_below(close, support)


def sv_ext_019_consec_below_ema200(close: pd.Series) -> pd.Series:
    """Consecutive days close has been below the 200-day EMA."""
    support = _ema_support(close, 200)
    return _consec_streak(close < support)


def sv_ext_020_ema50_below_ema200_flag(close: pd.Series) -> pd.Series:
    """Binary flag: 50-day EMA is below the 200-day EMA (death-cross condition)."""
    ema50 = _ewm_mean(close, 50).shift(1)
    ema200 = _ewm_mean(close, 200).shift(1)
    return (ema50 < ema200).astype(float)


# --- Group C (021-030): Keltner Channel support ---

def sv_ext_021_close_depth_below_keltner_lower_20(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth of close below Keltner lower band (EMA20, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    return _depth_below(close, support)


def sv_ext_022_close_pct_depth_below_keltner_lower_20(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below Keltner lower band (EMA20, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    return _pct_depth_below(close, support)


def sv_ext_023_close_below_keltner_lower_20_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close below Keltner lower band (EMA20, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    return (close < support).astype(float)


def sv_ext_024_close_depth_below_keltner_lower_50(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth below Keltner lower band (EMA50, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 50, 14, 2.0)
    return _depth_below(close, support)


def sv_ext_025_consec_below_keltner_lower_20(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days close has been below the Keltner lower band (EMA20, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    return _consec_streak(close < support)


def sv_ext_026_close_below_keltner_lower_3x(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close below Keltner lower band (EMA20, 3x ATR14) — extreme channel breach."""
    support = _keltner_lower(close, high, low, 20, 14, 3.0)
    return (close < support).astype(float)


def sv_ext_027_keltner_lower_20_pct_depth_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of pct-depth below Keltner lower band (EMA20, 2x ATR14) vs 252d distribution."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    depth = _pct_depth_below(close, support)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_ext_028_keltner_break_intensity_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day sum of pct-depths below Keltner lower band (EMA20, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    depth = _pct_depth_below(close, support)
    return _rolling_sum(depth, _TD_MON)


def sv_ext_029_days_since_keltner_lower_break(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since last Keltner lower band breach (EMA20, 2x ATR14)."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    flag = (close < support).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~close.isna(), np.nan)


def sv_ext_030_keltner_lower_break_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Keltner lower band (EMA20, 2x ATR14) breaks in trailing 63 days."""
    support = _keltner_lower(close, high, low, 20, 14, 2.0)
    flag = (close < support).astype(float)
    return _rolling_sum(flag, _TD_QTR)


# --- Group D (031-040): Rolling VWAP support ---

def sv_ext_031_close_depth_below_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 21-day rolling VWAP."""
    support = _vwap_approx(close, volume, _TD_MON)
    return _depth_below(close, support)


def sv_ext_032_close_pct_depth_below_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentage depth of close below the prior 21-day rolling VWAP."""
    support = _vwap_approx(close, volume, _TD_MON)
    return _pct_depth_below(close, support)


def sv_ext_033_close_below_vwap_21d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is below the 21-day rolling VWAP."""
    support = _vwap_approx(close, volume, _TD_MON)
    return (close < support).astype(float)


def sv_ext_034_close_depth_below_vwap_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute depth of close below the prior 63-day rolling VWAP."""
    support = _vwap_approx(close, volume, _TD_QTR)
    return _depth_below(close, support)


def sv_ext_035_consec_below_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days close has been below the 21-day rolling VWAP."""
    support = _vwap_approx(close, volume, _TD_MON)
    return _consec_streak(close < support)


def sv_ext_036_vwap_21d_depth_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of pct-depth below 21d VWAP relative to its 252-day distribution."""
    support = _vwap_approx(close, volume, _TD_MON)
    depth = _pct_depth_below(close, support)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_ext_037_vwap_63d_depth_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of pct-depth below 63d VWAP within 252-day distribution."""
    support = _vwap_approx(close, volume, _TD_QTR)
    depth = _pct_depth_below(close, support)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_ext_038_vwap_21d_break_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where close broke below 21d rolling VWAP."""
    support = _vwap_approx(close, volume, _TD_MON)
    flag = (close < support).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def sv_ext_039_vwap_break_multi_tf_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close below both 21d and 63d rolling VWAPs simultaneously."""
    s21 = _vwap_approx(close, volume, _TD_MON)
    s63 = _vwap_approx(close, volume, _TD_QTR)
    return ((close < s21) & (close < s63)).astype(float)


def sv_ext_040_vwap_21d_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling sum of pct-depths below the 21d VWAP."""
    support = _vwap_approx(close, volume, _TD_MON)
    depth = _pct_depth_below(close, support)
    return _rolling_sum(depth, _TD_MON)


# --- Group E (041-050): Fibonacci-retracement-derived support ---

def sv_ext_041_close_below_fib382_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close below 38.2% Fibonacci retracement of the 252-day range from high."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib382 = h252 - 0.382 * (h252 - l252)
    return (close < fib382).astype(float)


def sv_ext_042_close_below_fib618_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close below 61.8% Fibonacci retracement of the 252-day range."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib618 = h252 - 0.618 * (h252 - l252)
    return (close < fib618).astype(float)


def sv_ext_043_close_pct_depth_below_fib618_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of close below the 61.8% Fibonacci level of 252-day range."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib618 = h252 - 0.618 * (h252 - l252)
    return _pct_depth_below(close, fib618)


def sv_ext_044_fib_levels_violated_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Fibonacci levels (23.6%, 38.2%, 50%, 61.8%) violated from 252d high."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    rng = h252 - l252
    fib236 = h252 - 0.236 * rng
    fib382 = h252 - 0.382 * rng
    fib500 = h252 - 0.500 * rng
    fib618 = h252 - 0.618 * rng
    return ((close < fib236).astype(float) + (close < fib382).astype(float) +
            (close < fib500).astype(float) + (close < fib618).astype(float))


def sv_ext_045_close_depth_below_fib786_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute depth below the 78.6% Fibonacci retracement of 252-day range."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib786 = h252 - 0.786 * (h252 - l252)
    return _depth_below(close, fib786)


def sv_ext_046_close_below_fib786_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close below 78.6% Fibonacci retracement (deep retracement)."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib786 = h252 - 0.786 * (h252 - l252)
    return (close < fib786).astype(float)


def sv_ext_047_fib618_depth_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of pct-depth below Fib 61.8% level vs 252-day distribution."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib618 = h252 - 0.618 * (h252 - l252)
    depth = _pct_depth_below(close, fib618)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_ext_048_consec_below_fib618_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days close has been below the 61.8% Fibonacci retracement."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib618 = h252 - 0.618 * (h252 - l252)
    return _consec_streak(close < fib618)


def sv_ext_049_fib382_depth_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of depth below 38.2% Fibonacci level within 252-day distribution."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib382 = h252 - 0.382 * (h252 - l252)
    depth = _pct_depth_below(close, fib382)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_ext_050_fib_break_intensity_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling sum of pct-depth below 61.8% Fibonacci level (intensity)."""
    h252 = _rolling_max(high, _TD_YEAR)
    l252 = _prior_low(low, _TD_YEAR)
    fib618 = h252 - 0.618 * (h252 - l252)
    depth = _pct_depth_below(close, fib618)
    return _rolling_sum(depth, _TD_QTR)


# --- Group F (051-060): Price-at-volume and quantile-based support ---

def sv_ext_051_close_below_vol_weighted_21d_quantile25(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close below the 25th percentile of the vol-weighted 21d price distribution."""
    q25 = close.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25).shift(1)
    return (close < q25).astype(float)


def sv_ext_052_close_depth_below_21d_q10(close: pd.Series) -> pd.Series:
    """Absolute depth of close below the 10th-percentile price over trailing 21 days."""
    q10 = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.10)
    return _depth_below(close, q10)


def sv_ext_053_close_depth_below_252d_q10(close: pd.Series) -> pd.Series:
    """Absolute depth of close below the 10th-percentile price over trailing 252 days."""
    q10 = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return _depth_below(close, q10)


def sv_ext_054_close_depth_below_252d_q5(close: pd.Series) -> pd.Series:
    """Absolute depth of close below the 5th-percentile price over trailing 252 days."""
    q5 = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    return _depth_below(close, q5)


def sv_ext_055_close_below_252d_q5_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is in the bottom 5% of its trailing 252-day price distribution."""
    q5 = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    return (close < q5).astype(float)


def sv_ext_056_close_below_252d_q10_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is in the bottom 10% of its trailing 252-day price distribution."""
    q10 = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return (close < q10).astype(float)


def sv_ext_057_consec_below_252d_q10(close: pd.Series) -> pd.Series:
    """Consecutive days close has been in the bottom 10% of the 252-day price distribution."""
    q10 = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return _consec_streak(close < q10)


def sv_ext_058_vol_weighted_support_break_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close below both the 21d rolling VWAP and the 21d lower price quartile."""
    vwap21 = _vwap_approx(close, volume, _TD_MON)
    q25 = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.25)
    return ((close < vwap21) & (close < q25)).astype(float)


def sv_ext_059_price_below_mode_21d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below the median of trailing 21-day closes (proxy for mode support)."""
    med = close.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()
    return (close < med).astype(float)


def sv_ext_060_pct_rank_in_252d_distribution(close: pd.Series) -> pd.Series:
    """Percentile rank of today's close within its trailing 252-day distribution (0=lowest)."""
    return close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group G (061-075): Cross-confirmation composites and advanced support ---

def sv_ext_061_all_support_violated_flag(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Binary flag: trailing low, EMA200, and SMA200 are all violated simultaneously."""
    s252 = _prior_low(low, _TD_YEAR)
    ema200 = _ema_support(close, 200)
    sma200 = _sma_support(close, 200)
    return ((close < s252) & (close < ema200) & (close < sma200)).astype(float)


def sv_ext_062_support_violation_score_6way(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Sum of 6 support-violation binary flags: 21d/63d/252d trailing lows + EMA50/EMA200/SMA200."""
    b21 = (close < _prior_low(low, _TD_MON)).astype(float)
    b63 = (close < _prior_low(low, _TD_QTR)).astype(float)
    b252 = (close < _prior_low(low, _TD_YEAR)).astype(float)
    bema50 = (close < _ema_support(close, 50)).astype(float)
    bema200 = (close < _ema_support(close, 200)).astype(float)
    bsma200 = (close < _sma_support(close, 200)).astype(float)
    return b21 + b63 + b252 + bema50 + bema200 + bsma200


def sv_ext_063_support_violation_pct_depth_ema200(close: pd.Series) -> pd.Series:
    """Percentage depth of close below the 200-day EMA."""
    support = _ema_support(close, 200)
    return _pct_depth_below(close, support)


def sv_ext_064_ema200_depth_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of pct-depth below EMA200 relative to its 252-day distribution."""
    support = _ema_support(close, 200)
    depth = _pct_depth_below(close, support)
    m = _rolling_mean(depth, _TD_YEAR)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(depth - m, s)


def sv_ext_065_ema200_depth_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of pct-depth below EMA200 in trailing 252-day distribution."""
    support = _ema_support(close, 200)
    depth = _pct_depth_below(close, support)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def sv_ext_066_support_depth_below_ema50_intensity_21d(close: pd.Series) -> pd.Series:
    """21-day rolling sum of pct-depth below EMA50 (sustained breach intensity)."""
    support = _ema_support(close, 50)
    depth = _pct_depth_below(close, support)
    return _rolling_sum(depth, _TD_MON)


def sv_ext_067_break_above_support_then_fail_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close today is below 63d low AND yesterday was above it (fresh break)."""
    support = _prior_low(low, _TD_QTR)
    today_below = close < support
    yest_above = close.shift(1) >= support.shift(1)
    return (today_below & yest_above).astype(float)


def sv_ext_068_retest_failure_flag_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: close retests the 252d low support but fails (today < 252d support,
    prior 5 days had at least 1 day above it)."""
    support = _prior_low(low, _TD_YEAR)
    today_below = close < support
    prev5_max = close.shift(1).rolling(_TD_WEEK, min_periods=1).max()
    prev_ever_above = prev5_max >= support
    return (today_below & prev_ever_above).astype(float)


def sv_ext_069_new_low_vol_confirmation_score(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Score = pct-depth below 252d low multiplied by normalized volume; 0 on non-break days."""
    support = _prior_low(low, _TD_YEAR)
    depth = _pct_depth_below(close, support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.clip(lower=_EPS)).clip(upper=5.0)
    return depth * vol_norm


def sv_ext_070_close_below_all_ema_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below all three EMAs: EMA20, EMA50, EMA200."""
    e20 = _ema_support(close, 20)
    e50 = _ema_support(close, 50)
    e200 = _ema_support(close, 200)
    return ((close < e20) & (close < e50) & (close < e200)).astype(float)


def sv_ext_071_low_vs_ema20_depth_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentage depth of today's low below the prior EMA20."""
    support = _ema_support(close, 20)
    return _pct_depth_below(low, support)


def sv_ext_072_support_break_comprehensive_score(close: pd.Series, low: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Comprehensive capitulation score: 252d trailing depth + EMA200 depth + alignment + vol."""
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    dema200 = _pct_depth_below(close, _ema_support(close, 200))
    align = (
        (close < _prior_low(low, _TD_MON)).astype(float) +
        (close < _prior_low(low, _TD_QTR)).astype(float) +
        (close < _prior_low(low, _TD_YEAR)).astype(float)
    ) / 3.0
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol.clip(lower=_EPS)).clip(upper=5.0) / 5.0
    return d252 + dema200 + align + vol_ratio


def sv_ext_073_low_break_252d_with_keltner_confirm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: 252d low broken AND Keltner lower band also broken (dual confirmation)."""
    s252 = _prior_low(low, _TD_YEAR)
    klt = _keltner_lower(close, high, low, 20, 14, 2.0)
    return ((close < s252) & (close < klt)).astype(float)


def sv_ext_074_support_violation_pct_rank_expanding(close: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of pct-depth below 252d trailing low."""
    depth = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    return depth.expanding(min_periods=1).rank(pct=True)


def sv_ext_075_support_violation_capitulation_composite_ext(close: pd.Series, low: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Extended capitulation composite: z-scored depth below 252d + Keltner + EMA200 + vol.
    Combines multiple support frameworks into a single dimensionless distress score."""
    # 252d trailing low pct depth (z-scored)
    d252 = _pct_depth_below(close, _prior_low(low, _TD_YEAR))
    d252_z = _safe_div(d252 - _rolling_mean(d252, _TD_YEAR), _rolling_std(d252, _TD_YEAR))
    # EMA200 pct depth (z-scored)
    dema = _pct_depth_below(close, _ema_support(close, 200))
    dema_z = _safe_div(dema - _rolling_mean(dema, _TD_YEAR), _rolling_std(dema, _TD_YEAR))
    # Keltner lower band pct depth (z-scored)
    dklt = _pct_depth_below(close, _keltner_lower(close, high, low, 20, 14, 2.0))
    dklt_z = _safe_div(dklt - _rolling_mean(dklt, _TD_YEAR), _rolling_std(dklt, _TD_YEAR))
    # Volume surge
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_z = _safe_div(volume - avg_vol, _rolling_std(volume, _TD_MON)).clip(lower=0.0, upper=3.0)
    return (d252_z.fillna(0) + dema_z.fillna(0) + dklt_z.fillna(0) + vol_z.fillna(0)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

SUPPORT_VIOLATION_EXTENDED_REGISTRY_001_075 = {
    "sv_ext_001_close_depth_below_3yr_low": {"inputs": ["close", "low"], "func": sv_ext_001_close_depth_below_3yr_low},
    "sv_ext_002_close_pct_depth_below_3yr_low": {"inputs": ["close", "low"], "func": sv_ext_002_close_pct_depth_below_3yr_low},
    "sv_ext_003_close_below_3yr_low_flag": {"inputs": ["close", "low"], "func": sv_ext_003_close_below_3yr_low_flag},
    "sv_ext_004_close_depth_below_5yr_low": {"inputs": ["close", "low"], "func": sv_ext_004_close_depth_below_5yr_low},
    "sv_ext_005_close_below_5yr_low_flag": {"inputs": ["close", "low"], "func": sv_ext_005_close_below_5yr_low_flag},
    "sv_ext_006_expanding_low_pct_depth": {"inputs": ["close", "low"], "func": sv_ext_006_expanding_low_pct_depth},
    "sv_ext_007_expanding_low_break_flag": {"inputs": ["close", "low"], "func": sv_ext_007_expanding_low_break_flag},
    "sv_ext_008_consec_below_3yr_low": {"inputs": ["close", "low"], "func": sv_ext_008_consec_below_3yr_low},
    "sv_ext_009_3yr_low_pct_depth_pct_rank_252d": {"inputs": ["close", "low"], "func": sv_ext_009_3yr_low_pct_depth_pct_rank_252d},
    "sv_ext_010_multi_year_break_composite": {"inputs": ["close", "low"], "func": sv_ext_010_multi_year_break_composite},
    "sv_ext_011_close_depth_below_ema50": {"inputs": ["close"], "func": sv_ext_011_close_depth_below_ema50},
    "sv_ext_012_close_depth_below_ema200": {"inputs": ["close"], "func": sv_ext_012_close_depth_below_ema200},
    "sv_ext_013_close_pct_depth_below_ema50": {"inputs": ["close"], "func": sv_ext_013_close_pct_depth_below_ema50},
    "sv_ext_014_close_pct_depth_below_ema200": {"inputs": ["close"], "func": sv_ext_014_close_pct_depth_below_ema200},
    "sv_ext_015_close_below_ema200_flag": {"inputs": ["close"], "func": sv_ext_015_close_below_ema200_flag},
    "sv_ext_016_close_below_sma200_flag": {"inputs": ["close"], "func": sv_ext_016_close_below_sma200_flag},
    "sv_ext_017_close_pct_depth_below_sma200": {"inputs": ["close"], "func": sv_ext_017_close_pct_depth_below_sma200},
    "sv_ext_018_close_depth_below_sma50": {"inputs": ["close"], "func": sv_ext_018_close_depth_below_sma50},
    "sv_ext_019_consec_below_ema200": {"inputs": ["close"], "func": sv_ext_019_consec_below_ema200},
    "sv_ext_020_ema50_below_ema200_flag": {"inputs": ["close"], "func": sv_ext_020_ema50_below_ema200_flag},
    "sv_ext_021_close_depth_below_keltner_lower_20": {"inputs": ["close", "high", "low"], "func": sv_ext_021_close_depth_below_keltner_lower_20},
    "sv_ext_022_close_pct_depth_below_keltner_lower_20": {"inputs": ["close", "high", "low"], "func": sv_ext_022_close_pct_depth_below_keltner_lower_20},
    "sv_ext_023_close_below_keltner_lower_20_flag": {"inputs": ["close", "high", "low"], "func": sv_ext_023_close_below_keltner_lower_20_flag},
    "sv_ext_024_close_depth_below_keltner_lower_50": {"inputs": ["close", "high", "low"], "func": sv_ext_024_close_depth_below_keltner_lower_50},
    "sv_ext_025_consec_below_keltner_lower_20": {"inputs": ["close", "high", "low"], "func": sv_ext_025_consec_below_keltner_lower_20},
    "sv_ext_026_close_below_keltner_lower_3x": {"inputs": ["close", "high", "low"], "func": sv_ext_026_close_below_keltner_lower_3x},
    "sv_ext_027_keltner_lower_20_pct_depth_zscore_252d": {"inputs": ["close", "high", "low"], "func": sv_ext_027_keltner_lower_20_pct_depth_zscore_252d},
    "sv_ext_028_keltner_break_intensity_21d": {"inputs": ["close", "high", "low"], "func": sv_ext_028_keltner_break_intensity_21d},
    "sv_ext_029_days_since_keltner_lower_break": {"inputs": ["close", "high", "low"], "func": sv_ext_029_days_since_keltner_lower_break},
    "sv_ext_030_keltner_lower_break_count_63d": {"inputs": ["close", "high", "low"], "func": sv_ext_030_keltner_lower_break_count_63d},
    "sv_ext_031_close_depth_below_vwap_21d": {"inputs": ["close", "volume"], "func": sv_ext_031_close_depth_below_vwap_21d},
    "sv_ext_032_close_pct_depth_below_vwap_21d": {"inputs": ["close", "volume"], "func": sv_ext_032_close_pct_depth_below_vwap_21d},
    "sv_ext_033_close_below_vwap_21d_flag": {"inputs": ["close", "volume"], "func": sv_ext_033_close_below_vwap_21d_flag},
    "sv_ext_034_close_depth_below_vwap_63d": {"inputs": ["close", "volume"], "func": sv_ext_034_close_depth_below_vwap_63d},
    "sv_ext_035_consec_below_vwap_21d": {"inputs": ["close", "volume"], "func": sv_ext_035_consec_below_vwap_21d},
    "sv_ext_036_vwap_21d_depth_zscore_252d": {"inputs": ["close", "volume"], "func": sv_ext_036_vwap_21d_depth_zscore_252d},
    "sv_ext_037_vwap_63d_depth_pct_rank_252d": {"inputs": ["close", "volume"], "func": sv_ext_037_vwap_63d_depth_pct_rank_252d},
    "sv_ext_038_vwap_21d_break_count_63d": {"inputs": ["close", "volume"], "func": sv_ext_038_vwap_21d_break_count_63d},
    "sv_ext_039_vwap_break_multi_tf_flag": {"inputs": ["close", "volume"], "func": sv_ext_039_vwap_break_multi_tf_flag},
    "sv_ext_040_vwap_21d_intensity_21d": {"inputs": ["close", "volume"], "func": sv_ext_040_vwap_21d_intensity_21d},
    "sv_ext_041_close_below_fib382_252d_flag": {"inputs": ["close", "high", "low"], "func": sv_ext_041_close_below_fib382_252d_flag},
    "sv_ext_042_close_below_fib618_252d_flag": {"inputs": ["close", "high", "low"], "func": sv_ext_042_close_below_fib618_252d_flag},
    "sv_ext_043_close_pct_depth_below_fib618_252d": {"inputs": ["close", "high", "low"], "func": sv_ext_043_close_pct_depth_below_fib618_252d},
    "sv_ext_044_fib_levels_violated_count": {"inputs": ["close", "high", "low"], "func": sv_ext_044_fib_levels_violated_count},
    "sv_ext_045_close_depth_below_fib786_252d": {"inputs": ["close", "high", "low"], "func": sv_ext_045_close_depth_below_fib786_252d},
    "sv_ext_046_close_below_fib786_252d_flag": {"inputs": ["close", "high", "low"], "func": sv_ext_046_close_below_fib786_252d_flag},
    "sv_ext_047_fib618_depth_zscore_252d": {"inputs": ["close", "high", "low"], "func": sv_ext_047_fib618_depth_zscore_252d},
    "sv_ext_048_consec_below_fib618_252d": {"inputs": ["close", "high", "low"], "func": sv_ext_048_consec_below_fib618_252d},
    "sv_ext_049_fib382_depth_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": sv_ext_049_fib382_depth_pct_rank_252d},
    "sv_ext_050_fib_break_intensity_63d": {"inputs": ["close", "high", "low"], "func": sv_ext_050_fib_break_intensity_63d},
    "sv_ext_051_close_below_vol_weighted_21d_quantile25": {"inputs": ["close", "volume"], "func": sv_ext_051_close_below_vol_weighted_21d_quantile25},
    "sv_ext_052_close_depth_below_21d_q10": {"inputs": ["close"], "func": sv_ext_052_close_depth_below_21d_q10},
    "sv_ext_053_close_depth_below_252d_q10": {"inputs": ["close"], "func": sv_ext_053_close_depth_below_252d_q10},
    "sv_ext_054_close_depth_below_252d_q5": {"inputs": ["close"], "func": sv_ext_054_close_depth_below_252d_q5},
    "sv_ext_055_close_below_252d_q5_flag": {"inputs": ["close"], "func": sv_ext_055_close_below_252d_q5_flag},
    "sv_ext_056_close_below_252d_q10_flag": {"inputs": ["close"], "func": sv_ext_056_close_below_252d_q10_flag},
    "sv_ext_057_consec_below_252d_q10": {"inputs": ["close"], "func": sv_ext_057_consec_below_252d_q10},
    "sv_ext_058_vol_weighted_support_break_flag": {"inputs": ["close", "volume"], "func": sv_ext_058_vol_weighted_support_break_flag},
    "sv_ext_059_price_below_mode_21d_flag": {"inputs": ["close"], "func": sv_ext_059_price_below_mode_21d_flag},
    "sv_ext_060_pct_rank_in_252d_distribution": {"inputs": ["close"], "func": sv_ext_060_pct_rank_in_252d_distribution},
    "sv_ext_061_all_support_violated_flag": {"inputs": ["close", "low", "high"], "func": sv_ext_061_all_support_violated_flag},
    "sv_ext_062_support_violation_score_6way": {"inputs": ["close", "low", "high"], "func": sv_ext_062_support_violation_score_6way},
    "sv_ext_063_support_violation_pct_depth_ema200": {"inputs": ["close"], "func": sv_ext_063_support_violation_pct_depth_ema200},
    "sv_ext_064_ema200_depth_zscore_252d": {"inputs": ["close"], "func": sv_ext_064_ema200_depth_zscore_252d},
    "sv_ext_065_ema200_depth_pct_rank_252d": {"inputs": ["close"], "func": sv_ext_065_ema200_depth_pct_rank_252d},
    "sv_ext_066_support_depth_below_ema50_intensity_21d": {"inputs": ["close"], "func": sv_ext_066_support_depth_below_ema50_intensity_21d},
    "sv_ext_067_break_above_support_then_fail_flag": {"inputs": ["close", "low"], "func": sv_ext_067_break_above_support_then_fail_flag},
    "sv_ext_068_retest_failure_flag_252d": {"inputs": ["close", "low"], "func": sv_ext_068_retest_failure_flag_252d},
    "sv_ext_069_new_low_vol_confirmation_score": {"inputs": ["close", "low", "volume"], "func": sv_ext_069_new_low_vol_confirmation_score},
    "sv_ext_070_close_below_all_ema_flag": {"inputs": ["close"], "func": sv_ext_070_close_below_all_ema_flag},
    "sv_ext_071_low_vs_ema20_depth_pct": {"inputs": ["close", "low"], "func": sv_ext_071_low_vs_ema20_depth_pct},
    "sv_ext_072_support_break_comprehensive_score": {"inputs": ["close", "low", "high", "volume"], "func": sv_ext_072_support_break_comprehensive_score},
    "sv_ext_073_low_break_252d_with_keltner_confirm": {"inputs": ["close", "high", "low"], "func": sv_ext_073_low_break_252d_with_keltner_confirm},
    "sv_ext_074_support_violation_pct_rank_expanding": {"inputs": ["close", "low"], "func": sv_ext_074_support_violation_pct_rank_expanding},
    "sv_ext_075_support_violation_capitulation_composite_ext": {"inputs": ["close", "low", "high", "volume"], "func": sv_ext_075_support_violation_capitulation_composite_ext},
}
