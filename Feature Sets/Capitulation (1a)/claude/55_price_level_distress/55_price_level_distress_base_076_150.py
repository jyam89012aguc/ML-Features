"""
55_price_level_distress — Base Features 076-150
Domain: absolute price level distress — sub-$1/$5 penny-stock flags, nominal dollar price
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

_LVL_1  = 1.0
_LVL_2  = 2.0
_LVL_3  = 3.0
_LVL_5  = 5.0
_LVL_10 = 10.0

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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """
    Count consecutive True values up to each row (backward-looking).
    Returns 0 on False rows and the current streak length on True rows.
    """
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Intraday low and high absolute level signals ---

def pld_076_low_level(low: pd.Series) -> pd.Series:
    """Raw intraday low price (absolute nominal dollar level)."""
    return low.astype(float)


def pld_077_high_level(high: pd.Series) -> pd.Series:
    """Raw intraday high price (absolute nominal dollar level)."""
    return high.astype(float)


def pld_078_log_low_level(low: pd.Series) -> pd.Series:
    """Natural log of the intraday low price."""
    return _log_safe(low)


def pld_079_low_below_5_flag(low: pd.Series) -> pd.Series:
    """Flag: intraday low touched below $5 (even if close recovered)."""
    return (low < _LVL_5).astype(float)


def pld_080_low_below_2_flag(low: pd.Series) -> pd.Series:
    """Flag: intraday low touched below $2."""
    return (low < _LVL_2).astype(float)


def pld_081_high_below_5_flag(high: pd.Series) -> pd.Series:
    """Flag: even the intraday high was below $5 (fully in penny territory)."""
    return (high < _LVL_5).astype(float)


def pld_082_high_below_1_flag(high: pd.Series) -> pd.Series:
    """Flag: even the intraday high was below $1 (sub-$1 entire session)."""
    return (high < _LVL_1).astype(float)


def pld_083_trailing_min_low_63d(low: pd.Series) -> pd.Series:
    """Trailing 63-day minimum of intraday lows (lowest intraday touch)."""
    return _rolling_min(low, _TD_QTR)


def pld_084_trailing_min_low_252d(low: pd.Series) -> pd.Series:
    """Trailing 252-day minimum of intraday lows."""
    return _rolling_min(low, _TD_YEAR)


def pld_085_low_depth_below_5(low: pd.Series) -> pd.Series:
    """Dollar depth of intraday low below $5 (0 if low >= $5)."""
    return (_LVL_5 - low).clip(lower=0.0)


# --- Group I (086-095): EMA and SMA of the absolute price level ---

def pld_086_close_ema5(close: pd.Series) -> pd.Series:
    """5-day EMA of nominal close price."""
    return _ewm_mean(close, _TD_WEEK)


def pld_087_close_ema21(close: pd.Series) -> pd.Series:
    """21-day EMA of nominal close price."""
    return _ewm_mean(close, _TD_MON)


def pld_088_close_ema63(close: pd.Series) -> pd.Series:
    """63-day EMA of nominal close price."""
    return _ewm_mean(close, _TD_QTR)


def pld_089_close_sma21(close: pd.Series) -> pd.Series:
    """21-day SMA of nominal close price."""
    return _rolling_mean(close, _TD_MON)


def pld_090_close_sma63(close: pd.Series) -> pd.Series:
    """63-day SMA of nominal close price."""
    return _rolling_mean(close, _TD_QTR)


def pld_091_close_sma252(close: pd.Series) -> pd.Series:
    """252-day SMA of nominal close price."""
    return _rolling_mean(close, _TD_YEAR)


def pld_092_ema5_below_1_flag(close: pd.Series) -> pd.Series:
    """Flag: 5-day EMA of close is below $1."""
    return (_ewm_mean(close, _TD_WEEK) < _LVL_1).astype(float)


def pld_093_ema21_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day EMA of close is below $5 (trend-based penny classification)."""
    return (_ewm_mean(close, _TD_MON) < _LVL_5).astype(float)


def pld_094_sma21_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day SMA of close is below $5."""
    return (_rolling_mean(close, _TD_MON) < _LVL_5).astype(float)


def pld_095_sma63_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day SMA below $5 (medium-term penny-stock trend signal)."""
    return (_rolling_mean(close, _TD_QTR) < _LVL_5).astype(float)


# --- Group J (096-105): Volume-weighted price level signals ---

def pld_096_vwap_21d_level(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted average price (VWAP) nominal level."""
    return _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def pld_097_vwap_63d_level(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day VWAP nominal level."""
    return _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def pld_098_close_vs_vwap21_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close divided by 21-day VWAP (measures sub-VWAP distress)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _safe_div(close, vwap)


def pld_099_close_vs_vwap63_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close divided by 63-day VWAP."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))
    return _safe_div(close, vwap)


def pld_100_vwap21_below_5_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21-day VWAP is below $5 (volume-weighted penny-stock regime)."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return (vwap < _LVL_5).astype(float)


def pld_101_vwap21_below_1_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 21-day VWAP is below $1."""
    vwap = _safe_div(_rolling_sum(close * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return (vwap < _LVL_1).astype(float)


def pld_102_dollar_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average daily dollar volume (close * volume); low = liquidity distress."""
    return _rolling_mean(close * volume, _TD_MON)


def pld_103_dollar_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day average daily dollar volume."""
    return _rolling_mean(close * volume, _TD_QTR)


def pld_104_log_dollar_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of 21-day average dollar volume."""
    return _log_safe(_rolling_mean(close * volume, _TD_MON))


def pld_105_below_5_flag_x_vol_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Below-$5 flag multiplied by normalized volume (distress × activity)."""
    flag = (close < _LVL_5).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return flag * vol_norm


# --- Group K (106-115): Open price level signals ---

def pld_106_open_below_1_flag(open: pd.Series) -> pd.Series:
    """Flag: today's open is below $1."""
    return (open < _LVL_1).astype(float)


def pld_107_open_below_5_flag(open: pd.Series) -> pd.Series:
    """Flag: today's open is below $5."""
    return (open < _LVL_5).astype(float)


def pld_108_open_depth_below_5(open: pd.Series) -> pd.Series:
    """Dollar depth of open below $5 (0 when open >= $5)."""
    return (_LVL_5 - open).clip(lower=0.0)


def pld_109_open_level_norm_252d_mean(open: pd.Series) -> pd.Series:
    """Open normalized by its 252-day mean."""
    return _safe_div(open, _rolling_mean(open, _TD_YEAR))


def pld_110_gap_open_vs_5_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's open gapped below $5 from a close that was at or above $5."""
    return ((close.shift(1) >= _LVL_5) & (open < _LVL_5)).astype(float)


def pld_111_gap_open_vs_1_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's open gapped below $1 from a close at or above $1."""
    return ((close.shift(1) >= _LVL_1) & (open < _LVL_1)).astype(float)


def pld_112_consec_opens_below_5(open: pd.Series) -> pd.Series:
    """Current consecutive days where the open is below $5."""
    return _consec_streak(open < _LVL_5)


def pld_113_consec_opens_below_1(open: pd.Series) -> pd.Series:
    """Current consecutive days where the open is below $1."""
    return _consec_streak(open < _LVL_1)


def pld_114_open_and_close_below_5_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: both open AND close are below $5 (fully committed penny session)."""
    return ((open < _LVL_5) & (close < _LVL_5)).astype(float)


def pld_115_open_and_close_below_1_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: both open AND close are below $1 (fully sub-$1 session)."""
    return ((open < _LVL_1) & (close < _LVL_1)).astype(float)


# --- Group L (116-125): Price level vs rolling median ---

def pld_116_close_vs_median_21d(close: pd.Series) -> pd.Series:
    """Close divided by its 21-day rolling median."""
    return _safe_div(close, _rolling_median(close, _TD_MON))


def pld_117_close_vs_median_63d(close: pd.Series) -> pd.Series:
    """Close divided by its 63-day rolling median."""
    return _safe_div(close, _rolling_median(close, _TD_QTR))


def pld_118_close_vs_median_252d(close: pd.Series) -> pd.Series:
    """Close divided by its 252-day rolling median."""
    return _safe_div(close, _rolling_median(close, _TD_YEAR))


def pld_119_median_21d_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day rolling median of close is below $5."""
    return (_rolling_median(close, _TD_MON) < _LVL_5).astype(float)


def pld_120_median_63d_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: 63-day rolling median of close is below $5."""
    return (_rolling_median(close, _TD_QTR) < _LVL_5).astype(float)


def pld_121_median_252d_below_5_flag(close: pd.Series) -> pd.Series:
    """Flag: 252-day rolling median of close is below $5."""
    return (_rolling_median(close, _TD_YEAR) < _LVL_5).astype(float)


def pld_122_median_21d_below_1_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day rolling median of close is below $1."""
    return (_rolling_median(close, _TD_MON) < _LVL_1).astype(float)


def pld_123_close_below_median_21d_flag(close: pd.Series) -> pd.Series:
    """Flag: close is below its 21-day rolling median."""
    return (close < _rolling_median(close, _TD_MON)).astype(float)


def pld_124_depth_below_median_21d(close: pd.Series) -> pd.Series:
    """Dollar depth of close below its 21-day median (0 when above)."""
    med = _rolling_median(close, _TD_MON)
    return (med - close).clip(lower=0.0)


def pld_125_depth_below_median_63d(close: pd.Series) -> pd.Series:
    """Dollar depth of close below its 63-day median (0 when above)."""
    med = _rolling_median(close, _TD_QTR)
    return (med - close).clip(lower=0.0)


# --- Group M (126-135): Composite / multi-threshold distress scores ---

def pld_126_sub1_sub5_composite_score(close: pd.Series) -> pd.Series:
    """Composite score: 2*below_$1 + 1*below_$5 (higher = deeper penny distress)."""
    b1 = (close < _LVL_1).astype(float)
    b5 = (close < _LVL_5).astype(float)
    return 2.0 * b1 + b5


def pld_127_multi_threshold_distress_score(close: pd.Series) -> pd.Series:
    """Sum of flags for <$1, <$2, <$3, <$5, <$10 (0-5 scale, 5 = extreme)."""
    return (
        (close < _LVL_1).astype(float)
        + (close < _LVL_2).astype(float)
        + (close < _LVL_3).astype(float)
        + (close < _LVL_5).astype(float)
        + (close < _LVL_10).astype(float)
    )


def pld_128_consec_below_5_norm_252d_avg(close: pd.Series) -> pd.Series:
    """Consecutive-below-$5 streak divided by its 252-day average."""
    streak = _consec_streak(close < _LVL_5)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def pld_129_consec_below_1_norm_252d_avg(close: pd.Series) -> pd.Series:
    """Consecutive-below-$1 streak divided by its 252-day average."""
    streak = _consec_streak(close < _LVL_1)
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def pld_130_price_level_distress_index(close: pd.Series) -> pd.Series:
    """Price-level distress index: (1 - close/5).clip(0,1) when below $5."""
    return ((1.0 - close / _LVL_5).clip(lower=0.0, upper=1.0))


def pld_131_cross_below_5_count_504d(close: pd.Series) -> pd.Series:
    """Count of times close crossed below $5 in the trailing 504 days."""
    was_above = close.shift(1) >= _LVL_5
    is_below = close < _LVL_5
    events = (was_above & is_below).astype(float)
    return _rolling_sum(events, 504)


def pld_132_cross_above_5_count_252d(close: pd.Series) -> pd.Series:
    """Count of times close crossed above $5 in the trailing 252 days (recoveries)."""
    was_below = close.shift(1) < _LVL_5
    is_above = close >= _LVL_5
    events = (was_below & is_above).astype(float)
    return _rolling_sum(events, _TD_YEAR)


def pld_133_frac_days_below_1_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below $1 (annual sub-$1 ratio)."""
    return _rolling_count_true(close < _LVL_1, _TD_YEAR) / _TD_YEAR


def pld_134_frac_days_below_2_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below $2."""
    return _rolling_count_true(close < _LVL_2, _TD_YEAR) / _TD_YEAR


def pld_135_frac_days_below_10_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below $10."""
    return _rolling_count_true(close < _LVL_10, _TD_YEAR) / _TD_YEAR


# --- Group N (136-145): Price level regime change and mean-reversion signals ---

def pld_136_close_vs_expanding_mean(close: pd.Series) -> pd.Series:
    """Close divided by its expanding mean (how today compares to full history avg)."""
    return _safe_div(close, close.expanding(min_periods=1).mean())


def pld_137_close_expanding_min_ratio(close: pd.Series) -> pd.Series:
    """Close divided by expanding all-time minimum (proximity to record low)."""
    return _safe_div(close, close.expanding(min_periods=1).min())


def pld_138_price_level_21d_std(close: pd.Series) -> pd.Series:
    """21-day rolling std of the nominal price level (price-level volatility)."""
    return _rolling_std(close, _TD_MON)


def pld_139_price_level_63d_std(close: pd.Series) -> pd.Series:
    """63-day rolling std of the nominal price level."""
    return _rolling_std(close, _TD_QTR)


def pld_140_price_level_cv_21d(close: pd.Series) -> pd.Series:
    """21-day coefficient of variation of nominal price (std/mean)."""
    return _safe_div(_rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))


def pld_141_price_level_cv_63d(close: pd.Series) -> pd.Series:
    """63-day coefficient of variation of nominal price level."""
    return _safe_div(_rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))


def pld_142_price_level_pct_change_21d(close: pd.Series) -> pd.Series:
    """21-day percentage change in nominal price level."""
    return close.pct_change(_TD_MON)


def pld_143_price_level_pct_change_63d(close: pd.Series) -> pd.Series:
    """63-day percentage change in nominal price level."""
    return close.pct_change(_TD_QTR)


def pld_144_price_level_pct_change_252d(close: pd.Series) -> pd.Series:
    """252-day percentage change in nominal price level."""
    return close.pct_change(_TD_YEAR)


def pld_145_price_level_ewma5_vs_ewma21(close: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA to 21-day EMA of nominal price (short-term trend direction)."""
    return _safe_div(_ewm_mean(close, _TD_WEEK), _ewm_mean(close, _TD_MON))


# --- Group O (146-150): High/low absolute level breadth and range signals ---

def pld_146_intraday_range_level(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Nominal dollar intraday range (high - low), a price-level volatility signal."""
    return high - low


def pld_147_range_vs_close_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday range (high - low) as fraction of close price."""
    return _safe_div(high - low, close)


def pld_148_trailing_max_high_252d(high: pd.Series) -> pd.Series:
    """Trailing 252-day maximum of intraday highs (absolute price ceiling)."""
    return _rolling_max(high, _TD_YEAR)


def pld_149_close_vs_max_high_252d_ratio(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close divided by 252-day max intraday high (price level vs recent ceiling)."""
    return _safe_div(close, _rolling_max(high, _TD_YEAR))


def pld_150_low_and_close_both_below_5_consec(close: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where BOTH intraday low AND close are below $5."""
    return _consec_streak((low < _LVL_5) & (close < _LVL_5))


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_LEVEL_DISTRESS_REGISTRY_076_150 = {
    "pld_076_low_level": {"inputs": ["low"], "func": pld_076_low_level},
    "pld_077_high_level": {"inputs": ["high"], "func": pld_077_high_level},
    "pld_078_log_low_level": {"inputs": ["low"], "func": pld_078_log_low_level},
    "pld_079_low_below_5_flag": {"inputs": ["low"], "func": pld_079_low_below_5_flag},
    "pld_080_low_below_2_flag": {"inputs": ["low"], "func": pld_080_low_below_2_flag},
    "pld_081_high_below_5_flag": {"inputs": ["high"], "func": pld_081_high_below_5_flag},
    "pld_082_high_below_1_flag": {"inputs": ["high"], "func": pld_082_high_below_1_flag},
    "pld_083_trailing_min_low_63d": {"inputs": ["low"], "func": pld_083_trailing_min_low_63d},
    "pld_084_trailing_min_low_252d": {"inputs": ["low"], "func": pld_084_trailing_min_low_252d},
    "pld_085_low_depth_below_5": {"inputs": ["low"], "func": pld_085_low_depth_below_5},
    "pld_086_close_ema5": {"inputs": ["close"], "func": pld_086_close_ema5},
    "pld_087_close_ema21": {"inputs": ["close"], "func": pld_087_close_ema21},
    "pld_088_close_ema63": {"inputs": ["close"], "func": pld_088_close_ema63},
    "pld_089_close_sma21": {"inputs": ["close"], "func": pld_089_close_sma21},
    "pld_090_close_sma63": {"inputs": ["close"], "func": pld_090_close_sma63},
    "pld_091_close_sma252": {"inputs": ["close"], "func": pld_091_close_sma252},
    "pld_092_ema5_below_1_flag": {"inputs": ["close"], "func": pld_092_ema5_below_1_flag},
    "pld_093_ema21_below_5_flag": {"inputs": ["close"], "func": pld_093_ema21_below_5_flag},
    "pld_094_sma21_below_5_flag": {"inputs": ["close"], "func": pld_094_sma21_below_5_flag},
    "pld_095_sma63_below_5_flag": {"inputs": ["close"], "func": pld_095_sma63_below_5_flag},
    "pld_096_vwap_21d_level": {"inputs": ["close", "volume"], "func": pld_096_vwap_21d_level},
    "pld_097_vwap_63d_level": {"inputs": ["close", "volume"], "func": pld_097_vwap_63d_level},
    "pld_098_close_vs_vwap21_ratio": {"inputs": ["close", "volume"], "func": pld_098_close_vs_vwap21_ratio},
    "pld_099_close_vs_vwap63_ratio": {"inputs": ["close", "volume"], "func": pld_099_close_vs_vwap63_ratio},
    "pld_100_vwap21_below_5_flag": {"inputs": ["close", "volume"], "func": pld_100_vwap21_below_5_flag},
    "pld_101_vwap21_below_1_flag": {"inputs": ["close", "volume"], "func": pld_101_vwap21_below_1_flag},
    "pld_102_dollar_volume_21d": {"inputs": ["close", "volume"], "func": pld_102_dollar_volume_21d},
    "pld_103_dollar_volume_63d": {"inputs": ["close", "volume"], "func": pld_103_dollar_volume_63d},
    "pld_104_log_dollar_volume_21d": {"inputs": ["close", "volume"], "func": pld_104_log_dollar_volume_21d},
    "pld_105_below_5_flag_x_vol_norm": {"inputs": ["close", "volume"], "func": pld_105_below_5_flag_x_vol_norm},
    "pld_106_open_below_1_flag": {"inputs": ["open"], "func": pld_106_open_below_1_flag},
    "pld_107_open_below_5_flag": {"inputs": ["open"], "func": pld_107_open_below_5_flag},
    "pld_108_open_depth_below_5": {"inputs": ["open"], "func": pld_108_open_depth_below_5},
    "pld_109_open_level_norm_252d_mean": {"inputs": ["open"], "func": pld_109_open_level_norm_252d_mean},
    "pld_110_gap_open_vs_5_flag": {"inputs": ["close", "open"], "func": pld_110_gap_open_vs_5_flag},
    "pld_111_gap_open_vs_1_flag": {"inputs": ["close", "open"], "func": pld_111_gap_open_vs_1_flag},
    "pld_112_consec_opens_below_5": {"inputs": ["open"], "func": pld_112_consec_opens_below_5},
    "pld_113_consec_opens_below_1": {"inputs": ["open"], "func": pld_113_consec_opens_below_1},
    "pld_114_open_and_close_below_5_flag": {"inputs": ["close", "open"], "func": pld_114_open_and_close_below_5_flag},
    "pld_115_open_and_close_below_1_flag": {"inputs": ["close", "open"], "func": pld_115_open_and_close_below_1_flag},
    "pld_116_close_vs_median_21d": {"inputs": ["close"], "func": pld_116_close_vs_median_21d},
    "pld_117_close_vs_median_63d": {"inputs": ["close"], "func": pld_117_close_vs_median_63d},
    "pld_118_close_vs_median_252d": {"inputs": ["close"], "func": pld_118_close_vs_median_252d},
    "pld_119_median_21d_below_5_flag": {"inputs": ["close"], "func": pld_119_median_21d_below_5_flag},
    "pld_120_median_63d_below_5_flag": {"inputs": ["close"], "func": pld_120_median_63d_below_5_flag},
    "pld_121_median_252d_below_5_flag": {"inputs": ["close"], "func": pld_121_median_252d_below_5_flag},
    "pld_122_median_21d_below_1_flag": {"inputs": ["close"], "func": pld_122_median_21d_below_1_flag},
    "pld_123_close_below_median_21d_flag": {"inputs": ["close"], "func": pld_123_close_below_median_21d_flag},
    "pld_124_depth_below_median_21d": {"inputs": ["close"], "func": pld_124_depth_below_median_21d},
    "pld_125_depth_below_median_63d": {"inputs": ["close"], "func": pld_125_depth_below_median_63d},
    "pld_126_sub1_sub5_composite_score": {"inputs": ["close"], "func": pld_126_sub1_sub5_composite_score},
    "pld_127_multi_threshold_distress_score": {"inputs": ["close"], "func": pld_127_multi_threshold_distress_score},
    "pld_128_consec_below_5_norm_252d_avg": {"inputs": ["close"], "func": pld_128_consec_below_5_norm_252d_avg},
    "pld_129_consec_below_1_norm_252d_avg": {"inputs": ["close"], "func": pld_129_consec_below_1_norm_252d_avg},
    "pld_130_price_level_distress_index": {"inputs": ["close"], "func": pld_130_price_level_distress_index},
    "pld_131_cross_below_5_count_504d": {"inputs": ["close"], "func": pld_131_cross_below_5_count_504d},
    "pld_132_cross_above_5_count_252d": {"inputs": ["close"], "func": pld_132_cross_above_5_count_252d},
    "pld_133_frac_days_below_1_252d": {"inputs": ["close"], "func": pld_133_frac_days_below_1_252d},
    "pld_134_frac_days_below_2_252d": {"inputs": ["close"], "func": pld_134_frac_days_below_2_252d},
    "pld_135_frac_days_below_10_252d": {"inputs": ["close"], "func": pld_135_frac_days_below_10_252d},
    "pld_136_close_vs_expanding_mean": {"inputs": ["close"], "func": pld_136_close_vs_expanding_mean},
    "pld_137_close_expanding_min_ratio": {"inputs": ["close"], "func": pld_137_close_expanding_min_ratio},
    "pld_138_price_level_21d_std": {"inputs": ["close"], "func": pld_138_price_level_21d_std},
    "pld_139_price_level_63d_std": {"inputs": ["close"], "func": pld_139_price_level_63d_std},
    "pld_140_price_level_cv_21d": {"inputs": ["close"], "func": pld_140_price_level_cv_21d},
    "pld_141_price_level_cv_63d": {"inputs": ["close"], "func": pld_141_price_level_cv_63d},
    "pld_142_price_level_pct_change_21d": {"inputs": ["close"], "func": pld_142_price_level_pct_change_21d},
    "pld_143_price_level_pct_change_63d": {"inputs": ["close"], "func": pld_143_price_level_pct_change_63d},
    "pld_144_price_level_pct_change_252d": {"inputs": ["close"], "func": pld_144_price_level_pct_change_252d},
    "pld_145_price_level_ewma5_vs_ewma21": {"inputs": ["close"], "func": pld_145_price_level_ewma5_vs_ewma21},
    "pld_146_intraday_range_level": {"inputs": ["close", "high", "low"], "func": pld_146_intraday_range_level},
    "pld_147_range_vs_close_pct": {"inputs": ["close", "high", "low"], "func": pld_147_range_vs_close_pct},
    "pld_148_trailing_max_high_252d": {"inputs": ["high"], "func": pld_148_trailing_max_high_252d},
    "pld_149_close_vs_max_high_252d_ratio": {"inputs": ["close", "high"], "func": pld_149_close_vs_max_high_252d_ratio},
    "pld_150_low_and_close_both_below_5_consec": {"inputs": ["close", "low"], "func": pld_150_low_and_close_both_below_5_consec},
}
