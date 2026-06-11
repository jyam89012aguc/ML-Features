"""
108_drawdown_history_rank — Base Features 076-150
Domain: current drawdown ranked against the ticker's own history —
        multi-window low-proximity flags, underwater curve statistics,
        high-water mark distance ranks, count-based historical comparisons,
        historical severity tiers.
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


def _expanding_max(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).max()


def _drawdown_depth_pct(close: pd.Series) -> pd.Series:
    """Absolute drawdown depth from expanding peak (fraction >= 0)."""
    peak = _expanding_max(close)
    return _safe_div(peak - close, peak.clip(lower=_EPS))


def _rolling_drawdown_from_peak(close: pd.Series, w: int) -> pd.Series:
    """Drawdown from rolling w-day high (fraction >= 0)."""
    roll_peak = _rolling_max(close, w)
    return _safe_div(roll_peak - close, roll_peak.clip(lower=_EPS))


def _current_dd_duration(close: pd.Series) -> pd.Series:
    """Days elapsed since the current drawdown began (since last all-time high)."""
    depth = _drawdown_depth_pct(close)
    at_high = (depth < _EPS).astype(int)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_high_idx = idx.where(at_high == 1).ffill().fillna(0)
    duration = idx - last_high_idx
    return duration.where(depth >= _EPS, 0.0)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Price vs historical low proximity ---

def dhr_076_pct_above_expanding_low(close: pd.Series) -> pd.Series:
    """Percentage of current price above the all-time expanding low.
    (close / expanding_min - 1), capped at 0 below = impossible here.
    """
    exp_min = close.expanding(min_periods=1).min().clip(lower=_EPS)
    return _safe_div(close - exp_min, exp_min)


def dhr_077_pct_above_rolling_low_252d(close: pd.Series) -> pd.Series:
    """Current price as percentage above 252-day rolling low."""
    low_252 = _rolling_min(close, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(close - low_252, low_252)


def dhr_078_pct_above_rolling_low_504d(close: pd.Series) -> pd.Series:
    """Current price as percentage above 504-day rolling low."""
    low_504 = _rolling_min(close, 504).clip(lower=_EPS)
    return _safe_div(close - low_504, low_504)


def dhr_079_pct_above_rolling_low_756d(close: pd.Series) -> pd.Series:
    """Current price as percentage above 756-day rolling low."""
    low_756 = _rolling_min(close, 756).clip(lower=_EPS)
    return _safe_div(close - low_756, low_756)


def dhr_080_pct_above_rolling_low_1260d(close: pd.Series) -> pd.Series:
    """Current price as percentage above 1260-day rolling low (5-year low proximity)."""
    low_1260 = _rolling_min(close, 1260).clip(lower=_EPS)
    return _safe_div(close - low_1260, low_1260)


def dhr_081_expanding_pctrank_price_vs_low(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of current price in the full price history (low=0, high=1)."""
    return close.expanding(min_periods=2).rank(pct=True)


def dhr_082_rolling_pctrank_price_252d(close: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of current price (0=yearly low, 1=yearly high)."""
    return close.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_083_rolling_pctrank_price_504d(close: pd.Series) -> pd.Series:
    """504-day rolling percentile rank of current price (2-year context)."""
    return close.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dhr_084_rolling_pctrank_price_756d(close: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of current price (3-year context)."""
    return close.rolling(756, min_periods=504).rank(pct=True)


def dhr_085_rolling_pctrank_price_1260d(close: pd.Series) -> pd.Series:
    """1260-day rolling percentile rank of current price (5-year context)."""
    return close.rolling(1260, min_periods=756).rank(pct=True)


def dhr_086_is_at_expanding_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close equals the all-time expanding minimum price."""
    exp_min = close.expanding(min_periods=1).min()
    return (close <= exp_min + _EPS).astype(float)


def dhr_087_is_at_252d_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close equals or is below the 252-day rolling low."""
    low_252 = _rolling_min(close, _TD_YEAR)
    return (close <= low_252 + _EPS).astype(float)


def dhr_088_is_at_504d_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close is at or below the 504-day rolling low."""
    low_504 = _rolling_min(close, 504)
    return (close <= low_504 + _EPS).astype(float)


def dhr_089_is_at_756d_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close is at or below the 756-day rolling low (3-year low)."""
    low_756 = _rolling_min(close, 756)
    return (close <= low_756 + _EPS).astype(float)


def dhr_090_is_at_1260d_low_flag(close: pd.Series) -> pd.Series:
    """Binary flag: today's close is at or below the 1260-day rolling low (5-year low)."""
    low_1260 = _rolling_min(close, 1260)
    return (close <= low_1260 + _EPS).astype(float)


# --- Group I (091-105): Underwater curve statistics vs history ---

def dhr_091_fraction_time_underwater_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days the price was in drawdown (below its own prior peak)."""
    depth = _drawdown_depth_pct(close)
    in_dd = (depth > _EPS).astype(float)
    return _rolling_sum(in_dd, _TD_YEAR) / _TD_YEAR


def dhr_092_fraction_time_underwater_504d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 504 days the price was in drawdown."""
    depth = _drawdown_depth_pct(close)
    in_dd = (depth > _EPS).astype(float)
    return _rolling_sum(in_dd, 504) / 504.0


def dhr_093_fraction_time_underwater_expanding(close: pd.Series) -> pd.Series:
    """All-time fraction of trading days spent in drawdown (expanding)."""
    depth = _drawdown_depth_pct(close)
    in_dd = (depth > _EPS).astype(float)
    n = pd.Series(range(1, len(close) + 1), index=close.index, dtype=float)
    return in_dd.expanding(min_periods=1).sum() / n


def dhr_094_pctrank_underwater_frac_252d_vs_history(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of the trailing 252-day underwater fraction vs all prior values."""
    frac = _rolling_sum((_drawdown_depth_pct(close) > _EPS).astype(float), _TD_YEAR) / _TD_YEAR
    return frac.expanding(min_periods=2).rank(pct=True)


def dhr_095_consec_days_in_drawdown(close: pd.Series) -> pd.Series:
    """Consecutive trading days the price has been continuously below an all-time high."""
    depth = _drawdown_depth_pct(close)
    return _consec_streak(depth > _EPS)


def dhr_096_expanding_pctrank_consec_days_in_dd(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of consecutive drawdown days vs all-history streaks."""
    streak = dhr_095_consec_days_in_drawdown(close)
    return streak.expanding(min_periods=2).rank(pct=True)


def dhr_097_rolling_pctrank_consec_days_in_dd_252d(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of current consecutive drawdown days."""
    streak = dhr_095_consec_days_in_drawdown(close)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_098_avg_dd_depth_in_252d(close: pd.Series) -> pd.Series:
    """Rolling average drawdown depth over trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_mean(depth, _TD_YEAR)


def dhr_099_avg_dd_depth_in_504d(close: pd.Series) -> pd.Series:
    """Rolling average drawdown depth over trailing 504 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_mean(depth, 504)


def dhr_100_avg_dd_depth_expanding(close: pd.Series) -> pd.Series:
    """Expanding mean of daily drawdown depths (average underwater level historically)."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=1).mean()


def dhr_101_dd_depth_above_avg_252d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds the 252-day average drawdown depth."""
    depth = _drawdown_depth_pct(close)
    avg = _rolling_mean(depth, _TD_YEAR)
    return (depth > avg).astype(float)


def dhr_102_dd_depth_above_expanding_avg_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds the expanding-mean drawdown depth."""
    depth = _drawdown_depth_pct(close)
    avg = depth.expanding(min_periods=2).mean()
    return (depth > avg).astype(float)


def dhr_103_dd_depth_std_252d(close: pd.Series) -> pd.Series:
    """Rolling standard deviation of drawdown depths over trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_std(depth, _TD_YEAR)


def dhr_104_dd_depth_std_expanding(close: pd.Series) -> pd.Series:
    """Expanding standard deviation of drawdown depths (all-time volatility of distress)."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=2).std()


def dhr_105_dd_depth_normalised_by_252d_std(close: pd.Series) -> pd.Series:
    """Current drawdown depth divided by its 252-day standard deviation."""
    depth = _drawdown_depth_pct(close)
    s = _rolling_std(depth, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(depth, s)


# --- Group J (106-120): High-water-mark and recovery distance vs history ---

def dhr_106_hwm_recovery_pct_needed(close: pd.Series) -> pd.Series:
    """Percentage gain required to recover to the all-time high from current price.
    = (peak/close - 1).
    """
    peak = _expanding_max(close)
    return _safe_div(peak - close, close.clip(lower=_EPS))


def dhr_107_hwm_recovery_pct_needed_252d(close: pd.Series) -> pd.Series:
    """Percentage gain needed to recover to 252-day high."""
    peak_252 = _rolling_max(close, _TD_YEAR)
    return _safe_div(peak_252 - close, close.clip(lower=_EPS))


def dhr_108_hwm_recovery_pct_needed_504d(close: pd.Series) -> pd.Series:
    """Percentage gain needed to recover to 504-day high."""
    peak_504 = _rolling_max(close, 504)
    return _safe_div(peak_504 - close, close.clip(lower=_EPS))


def dhr_109_expanding_pctrank_recovery_needed(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of percentage recovery needed vs all-history values."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    return rec.expanding(min_periods=2).rank(pct=True)


def dhr_110_rolling_pctrank_recovery_needed_252d(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of percentage recovery needed."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    return rec.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_111_rolling_pctrank_recovery_needed_504d(close: pd.Series) -> pd.Series:
    """504-day rolling pct-rank of percentage recovery needed."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    return rec.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dhr_112_recovery_needed_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """Current recovery-needed vs all-time maximum recovery-needed ratio."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    max_ever = rec.expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(rec, max_ever)


def dhr_113_recovery_needed_vs_expanding_median_ratio(close: pd.Series) -> pd.Series:
    """Recovery-needed vs expanding median recovery-needed ratio."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    med = rec.expanding(min_periods=2).median().clip(lower=_EPS)
    return _safe_div(rec, med)


def dhr_114_is_recovery_needed_worst_ever_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current recovery-needed equals the all-time maximum."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    max_ever = rec.expanding(min_periods=1).max()
    return (rec >= max_ever - _EPS).astype(float)


def dhr_115_recovery_needed_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of percentage recovery needed."""
    rec = dhr_106_hwm_recovery_pct_needed(close)
    m = rec.expanding(min_periods=2).mean()
    s = rec.expanding(min_periods=2).std()
    return _safe_div(rec - m, s)


def dhr_116_days_since_expanding_low(close: pd.Series) -> pd.Series:
    """Trading days since the current all-time expanding price low was set."""
    exp_low_idx = close.expanding(min_periods=1).apply(lambda x: np.argmin(x), raw=True)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    return idx - exp_low_idx


def dhr_117_days_since_252d_low(close: pd.Series) -> pd.Series:
    """Trading days since the 252-day rolling low was set."""
    def _days_since_min(arr):
        if len(arr) == 0:
            return np.nan
        valid = arr[~np.isnan(arr)]
        if len(valid) == 0:
            return np.nan
        pos = np.argmin(arr)
        return float(len(arr) - 1 - pos)
    return close.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_days_since_min, raw=True)


def dhr_118_days_since_504d_low(close: pd.Series) -> pd.Series:
    """Trading days since the 504-day rolling low was set."""
    def _days_since_min(arr):
        if len(arr) == 0:
            return np.nan
        pos = np.argmin(arr)
        return float(len(arr) - 1 - pos)
    return close.rolling(504, min_periods=max(1, 252)).apply(_days_since_min, raw=True)


def dhr_119_pctrank_days_since_252d_low_vs_history(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of days-since-252d-low vs all-history (low rank = recently at low)."""
    d = dhr_117_days_since_252d_low(close)
    return d.expanding(min_periods=2).rank(pct=True)


def dhr_120_rolling_pctrank_days_since_expanding_low_252d(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of days since expanding all-time low (lower = more recent)."""
    d = dhr_116_days_since_expanding_low(close)
    return d.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group K (121-135): Count-based comparisons vs history ---

def dhr_121_days_dd_below_10pct_in_252d(close: pd.Series) -> pd.Series:
    """Count of days with drawdown depth >10% in trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_sum((depth > 0.10).astype(float), _TD_YEAR)


def dhr_122_days_dd_below_20pct_in_252d(close: pd.Series) -> pd.Series:
    """Count of days with drawdown depth >20% in trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_sum((depth > 0.20).astype(float), _TD_YEAR)


def dhr_123_days_dd_below_30pct_in_252d(close: pd.Series) -> pd.Series:
    """Count of days with drawdown depth >30% in trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_sum((depth > 0.30).astype(float), _TD_YEAR)


def dhr_124_days_dd_below_50pct_in_252d(close: pd.Series) -> pd.Series:
    """Count of days with drawdown depth >50% in trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_sum((depth > 0.50).astype(float), _TD_YEAR)


def dhr_125_fraction_days_dd_below_20pct_expanding(close: pd.Series) -> pd.Series:
    """Expanding fraction of all trading days with >20% drawdown depth."""
    depth = _drawdown_depth_pct(close)
    in_severe = (depth > 0.20).astype(float)
    n = pd.Series(range(1, len(close) + 1), index=close.index, dtype=float)
    return in_severe.expanding(min_periods=1).sum() / n


def dhr_126_current_dd_depth_flag_10pct(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds 10%."""
    return (_drawdown_depth_pct(close) > 0.10).astype(float)


def dhr_127_current_dd_depth_flag_20pct(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds 20%."""
    return (_drawdown_depth_pct(close) > 0.20).astype(float)


def dhr_128_current_dd_depth_flag_30pct(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds 30%."""
    return (_drawdown_depth_pct(close) > 0.30).astype(float)


def dhr_129_current_dd_depth_flag_50pct(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds 50%."""
    return (_drawdown_depth_pct(close) > 0.50).astype(float)


def dhr_130_current_dd_depth_flag_70pct(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth exceeds 70%."""
    return (_drawdown_depth_pct(close) > 0.70).astype(float)


def dhr_131_days_dd_above_10pct_fraction_expanding(close: pd.Series) -> pd.Series:
    """Expanding fraction of days with >10% drawdown (how common severe drawdowns are)."""
    depth = _drawdown_depth_pct(close)
    flag = (depth > 0.10).astype(float)
    n = pd.Series(range(1, len(close) + 1), index=close.index, dtype=float)
    return flag.expanding(min_periods=1).sum() / n


def dhr_132_rolling_count_new_lows_252d(close: pd.Series) -> pd.Series:
    """Count of new 252-day closing lows within the trailing 252-day window."""
    low_252 = _rolling_min(close, _TD_YEAR)
    new_low = (close <= low_252.shift(1).fillna(close) + _EPS).astype(float)
    return _rolling_sum(new_low, _TD_YEAR)


def dhr_133_rolling_count_new_expanding_lows_252d(close: pd.Series) -> pd.Series:
    """Count of days in the trailing 252-day window where price was at an all-time low."""
    exp_min = close.expanding(min_periods=1).min()
    at_exp_low = (close <= exp_min + _EPS).astype(float)
    return _rolling_sum(at_exp_low, _TD_YEAR)


def dhr_134_pctrank_count_new_expanding_lows_252d(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of the 252-day count of new all-time lows."""
    cnt = dhr_133_rolling_count_new_expanding_lows_252d(close)
    return cnt.expanding(min_periods=2).rank(pct=True)


def dhr_135_fraction_252d_price_in_lower_half_of_range(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where price was in the lower half of the annual range."""
    low_252 = _rolling_min(close, _TD_YEAR)
    high_252 = _rolling_max(close, _TD_YEAR)
    midpoint = (low_252 + high_252) / 2.0
    in_lower = (close <= midpoint).astype(float)
    return _rolling_sum(in_lower, _TD_YEAR) / _TD_YEAR


# --- Group L (136-150): Severity tiers and composite historical ranks ---

def dhr_136_dd_severity_tier(close: pd.Series) -> pd.Series:
    """Ordinal drawdown severity tier based on expanding percentile rank.
    0=below 50th pct, 1=50-75th, 2=75-90th, 3=90-95th, 4=95-99th, 5=>=99th.
    """
    depth = _drawdown_depth_pct(close)
    pct = depth.expanding(min_periods=2).rank(pct=True)
    tier = pd.Series(0.0, index=close.index)
    tier = tier.where(pct < 0.50, 1.0)
    tier = tier.where(pct < 0.75, 2.0)
    tier = tier.where(pct < 0.90, 3.0)
    tier = tier.where(pct < 0.95, 4.0)
    tier = tier.where(pct < 0.99, 5.0)
    return tier.where(~pct.isna(), np.nan)


def dhr_137_dd_depth_log_ratio_vs_expanding_median(close: pd.Series) -> pd.Series:
    """Log ratio of current drawdown depth to expanding median drawdown depth."""
    depth = _drawdown_depth_pct(close)
    med = depth.expanding(min_periods=2).median().clip(lower=_EPS)
    return np.log(_safe_div(depth.clip(lower=_EPS), med))


def dhr_138_dd_depth_log_ratio_vs_expanding_max(close: pd.Series) -> pd.Series:
    """Log ratio of current drawdown depth to all-time max drawdown depth."""
    depth = _drawdown_depth_pct(close)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    return np.log(_safe_div(depth.clip(lower=_EPS), max_ever))


def dhr_139_rolling_pctrank_dd_depth_vs_5yr_expanding(close: pd.Series) -> pd.Series:
    """Percentile rank of current drawdown in trailing 1260 days, expanding fallback."""
    depth = _drawdown_depth_pct(close)
    pct_5yr = depth.rolling(1260, min_periods=1).rank(pct=True)
    return pct_5yr


def dhr_140_expanding_pctrank_dd_depth_above_30pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current drawdown depth is above expanding 30th-percentile AND >30%."""
    depth = _drawdown_depth_pct(close)
    q30 = depth.expanding(min_periods=2).quantile(0.30)
    return ((depth > q30) & (depth > 0.30)).astype(float)


def dhr_141_dd_distress_z_and_pctrank_product(close: pd.Series) -> pd.Series:
    """Product of expanding z-score and pct-rank of drawdown depth (combined signal strength)."""
    depth = _drawdown_depth_pct(close)
    m = depth.expanding(min_periods=2).mean()
    s = depth.expanding(min_periods=2).std().clip(lower=_EPS)
    z = _safe_div(depth - m, s).clip(lower=0.0)
    pct = depth.expanding(min_periods=2).rank(pct=True)
    return z * pct


def dhr_142_dd_depth_vs_252d_90pct_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown depth vs 252-day 90th-percentile drawdown ratio."""
    depth = _drawdown_depth_pct(close)
    q90 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90).clip(lower=_EPS)
    return _safe_div(depth, q90)


def dhr_143_dd_depth_vs_504d_90pct_ratio(close: pd.Series) -> pd.Series:
    """Current drawdown depth vs 504-day 90th-percentile drawdown ratio."""
    depth = _drawdown_depth_pct(close)
    q90 = depth.rolling(504, min_periods=_TD_YEAR).quantile(0.90).clip(lower=_EPS)
    return _safe_div(depth, q90)


def dhr_144_rolling_pctrank_dd_depth_vs_3yr_252d_window(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of drawdown depth using only the past 252 observations."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def dhr_145_days_price_below_expanding_25pct_quantile(close: pd.Series) -> pd.Series:
    """Count of trailing 252 days where price was below its expanding 25th-percentile."""
    q25 = close.expanding(min_periods=4).quantile(0.25)
    below = (close < q25).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def dhr_146_days_price_below_expanding_10pct_quantile(close: pd.Series) -> pd.Series:
    """Count of trailing 252 days where price was below its expanding 10th-percentile."""
    q10 = close.expanding(min_periods=10).quantile(0.10)
    below = (close < q10).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def dhr_147_price_below_expanding_10pct_quantile_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current price is below its expanding 10th-percentile value."""
    q10 = close.expanding(min_periods=10).quantile(0.10)
    return (close < q10).astype(float)


def dhr_148_price_below_expanding_5pct_quantile_flag(close: pd.Series) -> pd.Series:
    """Binary flag: current price is below its expanding 5th-percentile value."""
    q5 = close.expanding(min_periods=20).quantile(0.05)
    return (close < q5).astype(float)


def dhr_149_dd_expanding_skew(close: pd.Series) -> pd.Series:
    """Expanding skewness of drawdown depth distribution (tail shape over history)."""
    depth = _drawdown_depth_pct(close)
    return depth.expanding(min_periods=4).skew()


def dhr_150_dd_capitulation_rank_composite(close: pd.Series) -> pd.Series:
    """Capitulation rank composite: average of expanding pct-ranks for depth, duration,
    recovery-needed, and underwater-fraction metrics — overall historical distress rank.
    """
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    rec = _safe_div(_expanding_max(close) - close, close.clip(lower=_EPS))
    frac_uw = _rolling_sum((depth > _EPS).astype(float), _TD_YEAR) / _TD_YEAR

    r_depth = depth.expanding(min_periods=2).rank(pct=True)
    r_dur = dur.expanding(min_periods=2).rank(pct=True)
    r_rec = rec.expanding(min_periods=2).rank(pct=True)
    r_frac = frac_uw.expanding(min_periods=2).rank(pct=True)

    return (r_depth + r_dur + r_rec + r_frac) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_HISTORY_RANK_REGISTRY_076_150 = {
    "dhr_076_pct_above_expanding_low": {"inputs": ["close"], "func": dhr_076_pct_above_expanding_low},
    "dhr_077_pct_above_rolling_low_252d": {"inputs": ["close"], "func": dhr_077_pct_above_rolling_low_252d},
    "dhr_078_pct_above_rolling_low_504d": {"inputs": ["close"], "func": dhr_078_pct_above_rolling_low_504d},
    "dhr_079_pct_above_rolling_low_756d": {"inputs": ["close"], "func": dhr_079_pct_above_rolling_low_756d},
    "dhr_080_pct_above_rolling_low_1260d": {"inputs": ["close"], "func": dhr_080_pct_above_rolling_low_1260d},
    "dhr_081_expanding_pctrank_price_vs_low": {"inputs": ["close"], "func": dhr_081_expanding_pctrank_price_vs_low},
    "dhr_082_rolling_pctrank_price_252d": {"inputs": ["close"], "func": dhr_082_rolling_pctrank_price_252d},
    "dhr_083_rolling_pctrank_price_504d": {"inputs": ["close"], "func": dhr_083_rolling_pctrank_price_504d},
    "dhr_084_rolling_pctrank_price_756d": {"inputs": ["close"], "func": dhr_084_rolling_pctrank_price_756d},
    "dhr_085_rolling_pctrank_price_1260d": {"inputs": ["close"], "func": dhr_085_rolling_pctrank_price_1260d},
    "dhr_086_is_at_expanding_low_flag": {"inputs": ["close"], "func": dhr_086_is_at_expanding_low_flag},
    "dhr_087_is_at_252d_low_flag": {"inputs": ["close"], "func": dhr_087_is_at_252d_low_flag},
    "dhr_088_is_at_504d_low_flag": {"inputs": ["close"], "func": dhr_088_is_at_504d_low_flag},
    "dhr_089_is_at_756d_low_flag": {"inputs": ["close"], "func": dhr_089_is_at_756d_low_flag},
    "dhr_090_is_at_1260d_low_flag": {"inputs": ["close"], "func": dhr_090_is_at_1260d_low_flag},
    "dhr_091_fraction_time_underwater_252d": {"inputs": ["close"], "func": dhr_091_fraction_time_underwater_252d},
    "dhr_092_fraction_time_underwater_504d": {"inputs": ["close"], "func": dhr_092_fraction_time_underwater_504d},
    "dhr_093_fraction_time_underwater_expanding": {"inputs": ["close"], "func": dhr_093_fraction_time_underwater_expanding},
    "dhr_094_pctrank_underwater_frac_252d_vs_history": {"inputs": ["close"], "func": dhr_094_pctrank_underwater_frac_252d_vs_history},
    "dhr_095_consec_days_in_drawdown": {"inputs": ["close"], "func": dhr_095_consec_days_in_drawdown},
    "dhr_096_expanding_pctrank_consec_days_in_dd": {"inputs": ["close"], "func": dhr_096_expanding_pctrank_consec_days_in_dd},
    "dhr_097_rolling_pctrank_consec_days_in_dd_252d": {"inputs": ["close"], "func": dhr_097_rolling_pctrank_consec_days_in_dd_252d},
    "dhr_098_avg_dd_depth_in_252d": {"inputs": ["close"], "func": dhr_098_avg_dd_depth_in_252d},
    "dhr_099_avg_dd_depth_in_504d": {"inputs": ["close"], "func": dhr_099_avg_dd_depth_in_504d},
    "dhr_100_avg_dd_depth_expanding": {"inputs": ["close"], "func": dhr_100_avg_dd_depth_expanding},
    "dhr_101_dd_depth_above_avg_252d_flag": {"inputs": ["close"], "func": dhr_101_dd_depth_above_avg_252d_flag},
    "dhr_102_dd_depth_above_expanding_avg_flag": {"inputs": ["close"], "func": dhr_102_dd_depth_above_expanding_avg_flag},
    "dhr_103_dd_depth_std_252d": {"inputs": ["close"], "func": dhr_103_dd_depth_std_252d},
    "dhr_104_dd_depth_std_expanding": {"inputs": ["close"], "func": dhr_104_dd_depth_std_expanding},
    "dhr_105_dd_depth_normalised_by_252d_std": {"inputs": ["close"], "func": dhr_105_dd_depth_normalised_by_252d_std},
    "dhr_106_hwm_recovery_pct_needed": {"inputs": ["close"], "func": dhr_106_hwm_recovery_pct_needed},
    "dhr_107_hwm_recovery_pct_needed_252d": {"inputs": ["close"], "func": dhr_107_hwm_recovery_pct_needed_252d},
    "dhr_108_hwm_recovery_pct_needed_504d": {"inputs": ["close"], "func": dhr_108_hwm_recovery_pct_needed_504d},
    "dhr_109_expanding_pctrank_recovery_needed": {"inputs": ["close"], "func": dhr_109_expanding_pctrank_recovery_needed},
    "dhr_110_rolling_pctrank_recovery_needed_252d": {"inputs": ["close"], "func": dhr_110_rolling_pctrank_recovery_needed_252d},
    "dhr_111_rolling_pctrank_recovery_needed_504d": {"inputs": ["close"], "func": dhr_111_rolling_pctrank_recovery_needed_504d},
    "dhr_112_recovery_needed_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_112_recovery_needed_vs_expanding_max_ratio},
    "dhr_113_recovery_needed_vs_expanding_median_ratio": {"inputs": ["close"], "func": dhr_113_recovery_needed_vs_expanding_median_ratio},
    "dhr_114_is_recovery_needed_worst_ever_flag": {"inputs": ["close"], "func": dhr_114_is_recovery_needed_worst_ever_flag},
    "dhr_115_recovery_needed_expanding_zscore": {"inputs": ["close"], "func": dhr_115_recovery_needed_expanding_zscore},
    "dhr_116_days_since_expanding_low": {"inputs": ["close"], "func": dhr_116_days_since_expanding_low},
    "dhr_117_days_since_252d_low": {"inputs": ["close"], "func": dhr_117_days_since_252d_low},
    "dhr_118_days_since_504d_low": {"inputs": ["close"], "func": dhr_118_days_since_504d_low},
    "dhr_119_pctrank_days_since_252d_low_vs_history": {"inputs": ["close"], "func": dhr_119_pctrank_days_since_252d_low_vs_history},
    "dhr_120_rolling_pctrank_days_since_expanding_low_252d": {"inputs": ["close"], "func": dhr_120_rolling_pctrank_days_since_expanding_low_252d},
    "dhr_121_days_dd_below_10pct_in_252d": {"inputs": ["close"], "func": dhr_121_days_dd_below_10pct_in_252d},
    "dhr_122_days_dd_below_20pct_in_252d": {"inputs": ["close"], "func": dhr_122_days_dd_below_20pct_in_252d},
    "dhr_123_days_dd_below_30pct_in_252d": {"inputs": ["close"], "func": dhr_123_days_dd_below_30pct_in_252d},
    "dhr_124_days_dd_below_50pct_in_252d": {"inputs": ["close"], "func": dhr_124_days_dd_below_50pct_in_252d},
    "dhr_125_fraction_days_dd_below_20pct_expanding": {"inputs": ["close"], "func": dhr_125_fraction_days_dd_below_20pct_expanding},
    "dhr_126_current_dd_depth_flag_10pct": {"inputs": ["close"], "func": dhr_126_current_dd_depth_flag_10pct},
    "dhr_127_current_dd_depth_flag_20pct": {"inputs": ["close"], "func": dhr_127_current_dd_depth_flag_20pct},
    "dhr_128_current_dd_depth_flag_30pct": {"inputs": ["close"], "func": dhr_128_current_dd_depth_flag_30pct},
    "dhr_129_current_dd_depth_flag_50pct": {"inputs": ["close"], "func": dhr_129_current_dd_depth_flag_50pct},
    "dhr_130_current_dd_depth_flag_70pct": {"inputs": ["close"], "func": dhr_130_current_dd_depth_flag_70pct},
    "dhr_131_days_dd_above_10pct_fraction_expanding": {"inputs": ["close"], "func": dhr_131_days_dd_above_10pct_fraction_expanding},
    "dhr_132_rolling_count_new_lows_252d": {"inputs": ["close"], "func": dhr_132_rolling_count_new_lows_252d},
    "dhr_133_rolling_count_new_expanding_lows_252d": {"inputs": ["close"], "func": dhr_133_rolling_count_new_expanding_lows_252d},
    "dhr_134_pctrank_count_new_expanding_lows_252d": {"inputs": ["close"], "func": dhr_134_pctrank_count_new_expanding_lows_252d},
    "dhr_135_fraction_252d_price_in_lower_half_of_range": {"inputs": ["close"], "func": dhr_135_fraction_252d_price_in_lower_half_of_range},
    "dhr_136_dd_severity_tier": {"inputs": ["close"], "func": dhr_136_dd_severity_tier},
    "dhr_137_dd_depth_log_ratio_vs_expanding_median": {"inputs": ["close"], "func": dhr_137_dd_depth_log_ratio_vs_expanding_median},
    "dhr_138_dd_depth_log_ratio_vs_expanding_max": {"inputs": ["close"], "func": dhr_138_dd_depth_log_ratio_vs_expanding_max},
    "dhr_139_rolling_pctrank_dd_depth_vs_5yr_expanding": {"inputs": ["close"], "func": dhr_139_rolling_pctrank_dd_depth_vs_5yr_expanding},
    "dhr_140_expanding_pctrank_dd_depth_above_30pct_flag": {"inputs": ["close"], "func": dhr_140_expanding_pctrank_dd_depth_above_30pct_flag},
    "dhr_141_dd_distress_z_and_pctrank_product": {"inputs": ["close"], "func": dhr_141_dd_distress_z_and_pctrank_product},
    "dhr_142_dd_depth_vs_252d_90pct_ratio": {"inputs": ["close"], "func": dhr_142_dd_depth_vs_252d_90pct_ratio},
    "dhr_143_dd_depth_vs_504d_90pct_ratio": {"inputs": ["close"], "func": dhr_143_dd_depth_vs_504d_90pct_ratio},
    "dhr_144_rolling_pctrank_dd_depth_vs_3yr_252d_window": {"inputs": ["close"], "func": dhr_144_rolling_pctrank_dd_depth_vs_3yr_252d_window},
    "dhr_145_days_price_below_expanding_25pct_quantile": {"inputs": ["close"], "func": dhr_145_days_price_below_expanding_25pct_quantile},
    "dhr_146_days_price_below_expanding_10pct_quantile": {"inputs": ["close"], "func": dhr_146_days_price_below_expanding_10pct_quantile},
    "dhr_147_price_below_expanding_10pct_quantile_flag": {"inputs": ["close"], "func": dhr_147_price_below_expanding_10pct_quantile_flag},
    "dhr_148_price_below_expanding_5pct_quantile_flag": {"inputs": ["close"], "func": dhr_148_price_below_expanding_5pct_quantile_flag},
    "dhr_149_dd_expanding_skew": {"inputs": ["close"], "func": dhr_149_dd_expanding_skew},
    "dhr_150_dd_capitulation_rank_composite": {"inputs": ["close"], "func": dhr_150_dd_capitulation_rank_composite},
}
