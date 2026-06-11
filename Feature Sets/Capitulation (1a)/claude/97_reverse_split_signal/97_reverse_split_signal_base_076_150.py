"""
97_reverse_split_signal — Base Features 076-200
Domain: reverse splits as late-stage distress flags; nominal-price exhaustion signals
Asset class: US equities
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Input contract
--------------
All inputs are daily-frequency pandas Series aligned to one shared daily
trading-day index.  Functions look strictly backward using .shift(positive),
.rolling(), or .expanding().  Trading-day constants: 1 year = 252 td,
1 quarter = 63 td, 1 month = 21 td, 1 week = 5 td.

  split_factor  : per-day split factor; 1.0 on normal days.
                  < 1.0 on reverse-split effective dates (e.g. 1-for-10 -> 0.1).
                  > 1.0 on forward-split effective dates (e.g. 2-for-1 -> 2.0).
  closeunadj    : raw unadjusted daily close price (USD); nominally raised by
                  reverse splits; driven toward sub-$1 by distress.
  close         : split/dividend-adjusted daily close price (USD).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _is_reverse_split(split_factor: pd.Series) -> pd.Series:
    """Binary indicator: 1 on days where split_factor < 1 (reverse split)."""
    return (split_factor < 1.0).astype(float)


def _is_forward_split(split_factor: pd.Series) -> pd.Series:
    """Binary indicator: 1 on days where split_factor > 1 (forward split)."""
    return (split_factor > 1.0).astype(float)


def _reverse_split_magnitude(split_factor: pd.Series) -> pd.Series:
    """Reverse-split magnitude 1/split_factor on RS days; NaN otherwise."""
    rs = split_factor.copy().astype(float)
    rs[rs >= 1.0] = np.nan
    return 1.0 / rs.replace(0, np.nan)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Adjusted close price level and RS interaction ---

def rss_076_close_below_1_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close < $1.00."""
    return (close < 1.0).astype(float)


def rss_077_close_below_2_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close < $2.00."""
    return (close < 2.0).astype(float)


def rss_078_close_below_5_flag(close: pd.Series) -> pd.Series:
    """Binary: 1 if adjusted close < $5.00."""
    return (close < 5.0).astype(float)


def rss_079_close_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of adjusted close within trailing 252 trading days."""
    return _zscore_rolling(close, _TD_YEAR)


def rss_080_close_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of adjusted close within trailing 252 trading days."""
    return _rolling_rank_pct(close, _TD_YEAR)


def rss_081_close_drawdown_from_252d_peak(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 252-day rolling peak."""
    return close - _rolling_max(close, _TD_YEAR)


def rss_082_close_pct_drawdown_252d(close: pd.Series) -> pd.Series:
    """Percent drawdown of adjusted close from its 252-day rolling peak."""
    peak = _rolling_max(close, _TD_YEAR)
    return _safe_div_abs(close - peak, peak)


def rss_083_close_drawdown_from_504d_peak(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its 504-day rolling peak."""
    return close - _rolling_max(close, _TD_2Y)


def rss_084_close_pct_drawdown_504d(close: pd.Series) -> pd.Series:
    """Percent drawdown of adjusted close from its 504-day rolling peak."""
    peak = _rolling_max(close, _TD_2Y)
    return _safe_div_abs(close - peak, peak)


def rss_085_close_drawdown_from_expanding_peak(close: pd.Series) -> pd.Series:
    """Adjusted close drawdown from its all-history expanding peak."""
    return close - close.expanding(min_periods=1).max()


def rss_086_close_pct_drawdown_expanding(close: pd.Series) -> pd.Series:
    """Percent drawdown of adjusted close from all-history peak."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div_abs(close - peak, peak)


def rss_087_close_log_price(close: pd.Series) -> pd.Series:
    """Log of adjusted close price."""
    return np.log(close.clip(lower=_EPS))


def rss_088_close_ewm_deviation_63d(close: pd.Series) -> pd.Series:
    """Adjusted close minus its EWM (span=63); short-term EWM deviation."""
    return close - _ewm_mean(close, _TD_QTR)


def rss_089_close_ewm_deviation_252d(close: pd.Series) -> pd.Series:
    """Adjusted close minus its EWM (span=252); long-term EWM deviation."""
    return close - _ewm_mean(close, _TD_YEAR)


def rss_090_close_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding (all-history) minimum of adjusted close price."""
    return close.expanding(min_periods=1).min()


# --- Group G (091-105): Price momentum and returns on closeunadj ---

def rss_091_closeunadj_return_1d(closeunadj: pd.Series) -> pd.Series:
    """1-day log return of unadjusted close."""
    return np.log(closeunadj.clip(lower=_EPS)) - np.log(closeunadj.shift(1).clip(lower=_EPS))


def rss_092_closeunadj_return_5d(closeunadj: pd.Series) -> pd.Series:
    """5-day log return of unadjusted close."""
    return np.log(closeunadj.clip(lower=_EPS)) - np.log(closeunadj.shift(_TD_WK).clip(lower=_EPS))


def rss_093_closeunadj_return_21d(closeunadj: pd.Series) -> pd.Series:
    """21-day log return of unadjusted close."""
    return np.log(closeunadj.clip(lower=_EPS)) - np.log(closeunadj.shift(_TD_MO).clip(lower=_EPS))


def rss_094_closeunadj_return_63d(closeunadj: pd.Series) -> pd.Series:
    """63-day log return of unadjusted close."""
    return np.log(closeunadj.clip(lower=_EPS)) - np.log(closeunadj.shift(_TD_QTR).clip(lower=_EPS))


def rss_095_closeunadj_return_252d(closeunadj: pd.Series) -> pd.Series:
    """252-day log return of unadjusted close."""
    return np.log(closeunadj.clip(lower=_EPS)) - np.log(closeunadj.shift(_TD_YEAR).clip(lower=_EPS))


def rss_096_closeunadj_volatility_21d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 21-day std of daily log returns of unadjusted close."""
    lr = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_MO)


def rss_097_closeunadj_volatility_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day std of daily log returns of unadjusted close."""
    lr = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_QTR)


def rss_098_closeunadj_volatility_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day std of daily log returns of unadjusted close."""
    lr = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_YEAR)


def rss_099_closeunadj_mean_21d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 21-day mean of unadjusted close."""
    return _rolling_mean(closeunadj, _TD_MO)


def rss_100_closeunadj_mean_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day mean of unadjusted close."""
    return _rolling_mean(closeunadj, _TD_QTR)


def rss_101_closeunadj_mean_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day mean of unadjusted close."""
    return _rolling_mean(closeunadj, _TD_YEAR)


def rss_102_closeunadj_pct_rank_504d(closeunadj: pd.Series) -> pd.Series:
    """Percentile rank of unadjusted close within trailing 504 days."""
    return _rolling_rank_pct(closeunadj, _TD_2Y)


def rss_103_closeunadj_pct_rank_expanding(closeunadj: pd.Series) -> pd.Series:
    """Expanding percentile rank of unadjusted close (all-history rank)."""
    return closeunadj.expanding(min_periods=2).rank(pct=True)


def rss_104_closeunadj_zscore_504d(closeunadj: pd.Series) -> pd.Series:
    """Z-score of unadjusted close within trailing 504 days."""
    return _zscore_rolling(closeunadj, _TD_2Y)


def rss_105_closeunadj_below_21d_mean_flag(closeunadj: pd.Series) -> pd.Series:
    """1 if unadjusted close is below its 21-day rolling mean."""
    return (closeunadj < _rolling_mean(closeunadj, _TD_MO)).astype(float)


# --- Group H (106-120): RS interacted with price drawdown ---

def rss_106_rs_within_252d_and_drawdown_lt_neg50_flag(split_factor: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RS in past 252 days AND adjusted close is down > 50% from 252d peak."""
    rs_flag = (_rolling_sum(_is_reverse_split(split_factor), _TD_YEAR) > 0).astype(float)
    peak    = _rolling_max(close, _TD_YEAR)
    dd_flag = (_safe_div_abs(close - peak, peak) < -0.50).astype(float)
    return rs_flag * dd_flag


def rss_107_rs_within_504d_and_below5_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if RS in past 504 days AND unadjusted close < $5."""
    rs_flag = (_rolling_sum(_is_reverse_split(split_factor), _TD_2Y) > 0).astype(float)
    return rs_flag * (closeunadj < 5.0).astype(float)


def rss_108_rs_count_252d_x_log_mag(split_factor: pd.Series) -> pd.Series:
    """RS count in 252 days times log of expanding max RS magnitude (severity x frequency)."""
    count   = _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)
    mag     = _reverse_split_magnitude(split_factor).fillna(1.0)
    exp_mag = mag.expanding(min_periods=1).max()
    return count * np.log(exp_mag.clip(lower=1.0))


def rss_109_close_pct_drawdown_252d_x_rs_ever_flag(split_factor: pd.Series, close: pd.Series) -> pd.Series:
    """Adjusted-close 252d pct drawdown multiplied by ever-had-RS indicator."""
    ever_rs = (_is_reverse_split(split_factor).expanding(min_periods=1).sum() > 0).astype(float)
    peak    = _rolling_max(close, _TD_YEAR)
    dd      = _safe_div_abs(close - peak, peak)
    return dd * ever_rs


def rss_110_closeunadj_pct_drawdown_252d_x_rs_21d(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Unadjusted-close 252d pct drawdown x RS-within-21d flag."""
    rs21  = (_rolling_sum(_is_reverse_split(split_factor), _TD_MO) > 0).astype(float)
    peak  = _rolling_max(closeunadj, _TD_YEAR)
    dd    = _safe_div_abs(closeunadj - peak, peak)
    return dd * rs21


def rss_111_rs_magnitude_x_below5_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Expanding max RS magnitude times current sub-$5 flag."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0).expanding(min_periods=1).max()
    return mag * (closeunadj < 5.0).astype(float)


def rss_112_cumulative_rs_factor_252d_log(split_factor: pd.Series) -> pd.Series:
    """Log of cumulative RS factor over 252 days (negative = net dilutive RS)."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return _rolling_sum(log_sf, _TD_YEAR)


def rss_113_cumulative_rs_factor_expanding_log(split_factor: pd.Series) -> pd.Series:
    """Log of cumulative RS factor over entire history."""
    log_sf = np.log(split_factor.clip(lower=_EPS))
    return log_sf.expanding(min_periods=1).sum()


def rss_114_rs_count_252d_x_closeunadj_below2(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """RS count in 252d multiplied by sub-$2 unadjusted close flag."""
    count  = _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)
    return count * (closeunadj < 2.0).astype(float)


def rss_115_days_since_rs_x_below1_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """Days-since-last-RS divided by 252 (normalized recency) times below-$1 flag."""
    days_s = pd.Series(np.full(len(split_factor), np.nan), index=split_factor.index)
    arr    = _is_reverse_split(split_factor).values
    last   = -1
    for i in range(len(arr)):
        if arr[i] == 1.0:
            last = i
        if last >= 0:
            days_s.iloc[i] = float(i - last)
    norm = days_s / _TD_YEAR
    return norm * (closeunadj < 1.0).astype(float)


def rss_116_closeunadj_max_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day maximum of unadjusted close."""
    return _rolling_max(closeunadj, _TD_YEAR)


def rss_117_closeunadj_range_252d(closeunadj: pd.Series) -> pd.Series:
    """252-day range (max - min) of unadjusted close."""
    return _rolling_max(closeunadj, _TD_YEAR) - _rolling_min(closeunadj, _TD_YEAR)


def rss_118_closeunadj_normalized_position_252d(closeunadj: pd.Series) -> pd.Series:
    """Position of close within 252d range: (close - min252) / (max252 - min252)."""
    lo  = _rolling_min(closeunadj, _TD_YEAR)
    hi  = _rolling_max(closeunadj, _TD_YEAR)
    rng = (hi - lo).replace(0, np.nan)
    return (closeunadj - lo) / rng


def rss_119_closeunadj_below_63d_min_flag(closeunadj: pd.Series) -> pd.Series:
    """1 if unadjusted close just reached a new 63-day low today."""
    return (closeunadj <= _rolling_min(closeunadj.shift(1), _TD_QTR)).astype(float)


def rss_120_closeunadj_below_252d_min_flag(closeunadj: pd.Series) -> pd.Series:
    """1 if unadjusted close just reached a new 252-day low today."""
    return (closeunadj <= _rolling_min(closeunadj.shift(1), _TD_YEAR)).astype(float)


# --- Group I (121-135): Price momentum, trend-break, and distress composites ---

def rss_121_close_return_1d(close: pd.Series) -> pd.Series:
    """1-day log return of adjusted close."""
    return np.log(close.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))


def rss_122_close_return_21d(close: pd.Series) -> pd.Series:
    """21-day log return of adjusted close."""
    return np.log(close.clip(lower=_EPS)) - np.log(close.shift(_TD_MO).clip(lower=_EPS))


def rss_123_close_return_63d(close: pd.Series) -> pd.Series:
    """63-day log return of adjusted close."""
    return np.log(close.clip(lower=_EPS)) - np.log(close.shift(_TD_QTR).clip(lower=_EPS))


def rss_124_close_return_252d(close: pd.Series) -> pd.Series:
    """252-day log return of adjusted close."""
    return np.log(close.clip(lower=_EPS)) - np.log(close.shift(_TD_YEAR).clip(lower=_EPS))


def rss_125_close_return_504d(close: pd.Series) -> pd.Series:
    """504-day log return of adjusted close."""
    return np.log(close.clip(lower=_EPS)) - np.log(close.shift(_TD_2Y).clip(lower=_EPS))


def rss_126_close_volatility_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day volatility (std of daily log returns) of adjusted close."""
    lr = np.log(close.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_MO)


def rss_127_close_volatility_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day volatility of adjusted close."""
    lr = np.log(close.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_QTR)


def rss_128_close_volatility_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day volatility of adjusted close."""
    lr = np.log(close.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_YEAR)


def rss_129_close_below_63d_mean_flag(close: pd.Series) -> pd.Series:
    """1 if adjusted close is below its 63-day rolling mean."""
    return (close < _rolling_mean(close, _TD_QTR)).astype(float)


def rss_130_close_below_252d_mean_flag(close: pd.Series) -> pd.Series:
    """1 if adjusted close is below its 252-day rolling mean."""
    return (close < _rolling_mean(close, _TD_YEAR)).astype(float)


def rss_131_close_days_below_252d_mean_count(close: pd.Series) -> pd.Series:
    """Count of days adjusted close was below its 252d mean in trailing 252 days."""
    below = (close < _rolling_mean(close, _TD_YEAR)).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def rss_132_closeunadj_days_below_21d_mean_count_63d(closeunadj: pd.Series) -> pd.Series:
    """Count of days unadjusted close below its 21d mean, in trailing 63 days."""
    below = (closeunadj < _rolling_mean(closeunadj, _TD_MO)).astype(float)
    return _rolling_sum(below, _TD_QTR)


def rss_133_close_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of adjusted close (vs all history)."""
    m  = close.expanding(min_periods=2).mean()
    sd = close.expanding(min_periods=2).std()
    return _safe_div(close - m, sd)


def rss_134_closeunadj_expanding_zscore(closeunadj: pd.Series) -> pd.Series:
    """Expanding z-score of unadjusted close (vs all history)."""
    m  = closeunadj.expanding(min_periods=2).mean()
    sd = closeunadj.expanding(min_periods=2).std()
    return _safe_div(closeunadj - m, sd)


def rss_135_closeunadj_below_3_flag(closeunadj: pd.Series) -> pd.Series:
    """Binary: 1 if unadjusted close < $3.00."""
    return (closeunadj < 3.0).astype(float)


# --- Group J (136-150): Additional RS flags, composites, and mixed features ---

def rss_136_rs_within_21d_and_below1_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if RS in past 21 days AND unadjusted close < $1."""
    rs = (_rolling_sum(_is_reverse_split(split_factor), _TD_MO) > 0).astype(float)
    return rs * (closeunadj < 1.0).astype(float)


def rss_137_rs_within_63d_and_below2_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if RS in past 63 days AND unadjusted close < $2."""
    rs = (_rolling_sum(_is_reverse_split(split_factor), _TD_QTR) > 0).astype(float)
    return rs * (closeunadj < 2.0).astype(float)


def rss_138_fs_count_504d(split_factor: pd.Series) -> pd.Series:
    """Count of forward-split days in trailing 504 trading days."""
    return _rolling_sum(_is_forward_split(split_factor), _TD_2Y)


def rss_139_rs_minus_fs_count_504d(split_factor: pd.Series) -> pd.Series:
    """Reverse-split count minus forward-split count in trailing 504 days."""
    return rss_021_rs_count_756d_proxy(split_factor) - rss_138_fs_count_504d(split_factor)


def rss_021_rs_count_756d_proxy(split_factor: pd.Series) -> pd.Series:
    """(Internal proxy) count of RS days in trailing 504 days for rss_139 use."""
    return _rolling_sum(_is_reverse_split(split_factor), _TD_2Y)


def rss_140_closeunadj_median_252d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 252-day median of unadjusted close."""
    return _rolling_median(closeunadj, _TD_YEAR)


def rss_141_closeunadj_below_median_252d_flag(closeunadj: pd.Series) -> pd.Series:
    """1 if unadjusted close is below its 252-day rolling median."""
    return (closeunadj < _rolling_median(closeunadj, _TD_YEAR)).astype(float)


def rss_142_rs_severity_ewm_span63(split_factor: pd.Series) -> pd.Series:
    """EWM (span=63) of reverse-split magnitude (1/sf on RS days, 1 otherwise)."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _ewm_mean(mag, _TD_QTR)


def rss_143_rs_severity_ewm_span252(split_factor: pd.Series) -> pd.Series:
    """EWM (span=252) of reverse-split magnitude (1/sf on RS days, 1 otherwise)."""
    mag = _reverse_split_magnitude(split_factor).fillna(1.0)
    return _ewm_mean(mag, _TD_YEAR)


def rss_144_closeunadj_std_21d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 21-day std of unadjusted close (price-level dispersion)."""
    return _rolling_std(closeunadj, _TD_MO)


def rss_145_closeunadj_std_63d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 63-day std of unadjusted close."""
    return _rolling_std(closeunadj, _TD_QTR)


def rss_146_closeunadj_cv_63d(closeunadj: pd.Series) -> pd.Series:
    """Coefficient of variation of unadjusted close over 63 days (std/mean)."""
    return _safe_div(_rolling_std(closeunadj, _TD_QTR),
                     _rolling_mean(closeunadj, _TD_QTR).replace(0, np.nan))


def rss_147_close_below_all_time_low_approach(close: pd.Series) -> pd.Series:
    """Ratio: adjusted close / expanding min (how close to all-time low; <1 impossible)."""
    emin = close.expanding(min_periods=1).min()
    return _safe_div(close, emin.replace(0, np.nan))


def rss_148_distress_composite_score(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """
    Composite distress score: equally-weighted sum of 5 normalized signals.
    1) RS-within-252d flag, 2) sub-$5 flag, 3) fraction-below-$1 in 252d,
    4) expanding-RS-count (clipped to [0,5]/5), 5) 252d pct-drawdown of closeunadj (clipped).
    Each component scaled to [0,1] range before averaging.
    """
    rs252  = (_rolling_sum(_is_reverse_split(split_factor), _TD_YEAR) > 0).astype(float)
    sub5   = (closeunadj < 5.0).astype(float)
    frac1  = _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)
    cnt_rs = (_is_reverse_split(split_factor).expanding(min_periods=1).sum().clip(upper=5) / 5.0)
    peak   = _rolling_max(closeunadj, _TD_YEAR)
    dd     = _safe_div_abs(closeunadj - peak, peak).abs().clip(upper=1.0)
    return (rs252 + sub5 + frac1 + cnt_rs + dd) / 5.0


def rss_149_rs_count_252d_x_volatility_21d(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """RS count in 252d multiplied by 21-day volatility of unadjusted close returns."""
    count = _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)
    lr    = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    vol   = _rolling_std(lr, _TD_MO)
    return count * vol


def rss_150_reverse_split_signal_composite(split_factor: pd.Series, closeunadj: pd.Series, close: pd.Series) -> pd.Series:
    """
    Overall reverse-split distress composite:
    average of three z-scores — RS recency decay, log unadjusted close, log adjusted close —
    each computed over trailing 252-day windows.  High values = severe distress.
    """
    rs_decay = _ewm_mean(_is_reverse_split(split_factor), _TD_QTR)
    z_rs     = _zscore_rolling(rs_decay, _TD_YEAR)
    z_unadj  = _zscore_rolling(np.log(closeunadj.clip(lower=_EPS)), _TD_YEAR)
    z_adj    = _zscore_rolling(np.log(close.clip(lower=_EPS)), _TD_YEAR)
    return (z_rs - z_unadj - z_adj) / 3.0


# --- Group K (176-200): Additional adjusted-close distress, RS timing, and mixed features ---

def rss_176_close_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of adjusted close within trailing 504 trading days."""
    return _zscore_rolling(close, _TD_2Y)


def rss_177_close_median_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day median of adjusted close."""
    return _rolling_median(close, _TD_YEAR)


def rss_178_close_below_median_252d_flag(close: pd.Series) -> pd.Series:
    """1 if adjusted close is below its 252-day rolling median."""
    return (close < _rolling_median(close, _TD_YEAR)).astype(float)


def rss_179_close_mean_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day mean of adjusted close."""
    return _rolling_mean(close, _TD_MO)


def rss_180_close_mean_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day mean of adjusted close."""
    return _rolling_mean(close, _TD_QTR)


def rss_181_close_std_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day std of adjusted close (price-level dispersion)."""
    return _rolling_std(close, _TD_MO)


def rss_182_close_std_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day std of adjusted close."""
    return _rolling_std(close, _TD_QTR)


def rss_183_close_cv_63d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of adjusted close over 63 days (std/mean)."""
    return _safe_div(_rolling_std(close, _TD_QTR),
                     _rolling_mean(close, _TD_QTR).replace(0, np.nan))


def rss_184_close_range_252d(close: pd.Series) -> pd.Series:
    """252-day range (max - min) of adjusted close."""
    return _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR)


def rss_185_close_normalized_position_252d(close: pd.Series) -> pd.Series:
    """Position of adjusted close within 252d range: (close - min) / (max - min)."""
    lo  = _rolling_min(close, _TD_YEAR)
    hi  = _rolling_max(close, _TD_YEAR)
    rng = (hi - lo).replace(0, np.nan)
    return (close - lo) / rng


def rss_186_close_below_504d_mean_flag(close: pd.Series) -> pd.Series:
    """1 if adjusted close is below its 504-day rolling mean."""
    return (close < _rolling_mean(close, _TD_2Y)).astype(float)


def rss_187_close_return_126d(close: pd.Series) -> pd.Series:
    """126-day log return of adjusted close."""
    return np.log(close.clip(lower=_EPS)) - np.log(close.shift(_TD_2Q).clip(lower=_EPS))


def rss_188_closeunadj_return_126d(closeunadj: pd.Series) -> pd.Series:
    """126-day log return of unadjusted close."""
    return np.log(closeunadj.clip(lower=_EPS)) - np.log(closeunadj.shift(_TD_2Q).clip(lower=_EPS))


def rss_189_closeunadj_volatility_126d(closeunadj: pd.Series) -> pd.Series:
    """Rolling 126-day std of daily log returns of unadjusted close."""
    lr = np.log(closeunadj.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_2Q)


def rss_190_close_volatility_126d(close: pd.Series) -> pd.Series:
    """Rolling 126-day volatility of adjusted close."""
    lr = np.log(close.clip(lower=_EPS)).diff(1)
    return _rolling_std(lr, _TD_2Q)


def rss_191_rs_within_252d_and_below2_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if RS in past 252 days AND unadjusted close < $2."""
    rs = (_rolling_sum(_is_reverse_split(split_factor), _TD_YEAR) > 0).astype(float)
    return rs * (closeunadj < 2.0).astype(float)


def rss_192_rs_within_504d_and_below1_flag(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """1 if RS in past 504 days AND unadjusted close < $1."""
    rs = (_rolling_sum(_is_reverse_split(split_factor), _TD_2Y) > 0).astype(float)
    return rs * (closeunadj < 1.0).astype(float)


def rss_193_close_days_below_504d_mean_count(close: pd.Series) -> pd.Series:
    """Count of days adjusted close was below its 504d mean in trailing 504 days."""
    below = (close < _rolling_mean(close, _TD_2Y)).astype(float)
    return _rolling_sum(below, _TD_2Y)


def rss_194_closeunadj_days_below_2_count_63d(closeunadj: pd.Series) -> pd.Series:
    """Count of days below $2 in trailing 63 trading days."""
    return _rolling_sum((closeunadj < 2.0).astype(float), _TD_QTR)


def rss_195_rs_count_252d_x_log_price(split_factor: pd.Series, closeunadj: pd.Series) -> pd.Series:
    """RS count in 252d multiplied by log unadjusted close (distress amplified by price level)."""
    count = _rolling_sum(_is_reverse_split(split_factor), _TD_YEAR)
    return count * np.log(closeunadj.clip(lower=_EPS))


def rss_196_closeunadj_ewm_deviation_21d(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its EWM (span=21); short-term EWM deviation."""
    return closeunadj - _ewm_mean(closeunadj, _TD_MO)


def rss_197_closeunadj_ewm_deviation_63d(closeunadj: pd.Series) -> pd.Series:
    """Unadjusted close minus its EWM (span=63); medium-term EWM deviation."""
    return closeunadj - _ewm_mean(closeunadj, _TD_QTR)


def rss_198_rs_recency_decay_wk(split_factor: pd.Series) -> pd.Series:
    """EWM-decayed reverse-split flag with fast decay (span=5, one week)."""
    return _ewm_mean(_is_reverse_split(split_factor), _TD_WK)


def rss_199_close_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of adjusted close pct-drawdown from expanding peak."""
    peak = close.expanding(min_periods=1).max()
    dd   = _safe_div_abs(close - peak, peak)
    m    = dd.expanding(min_periods=2).mean()
    sd   = dd.expanding(min_periods=2).std()
    return _safe_div(dd - m, sd)


def rss_200_distress_composite_v2(split_factor: pd.Series, closeunadj: pd.Series, close: pd.Series) -> pd.Series:
    """
    Composite distress score v2: equally-weighted sum of 6 normalized signals.
    1) RS-within-504d, 2) sub-$2 unadjusted flag, 3) below-$1 fraction 252d,
    4) expanding RS count clipped/5, 5) 252d pct drawdown unadj, 6) 252d pct drawdown adj.
    """
    rs504  = (_rolling_sum(_is_reverse_split(split_factor), _TD_2Y) > 0).astype(float)
    sub2   = (closeunadj < 2.0).astype(float)
    frac1  = _rolling_mean((closeunadj < 1.0).astype(float), _TD_YEAR)
    cnt_rs = (_is_reverse_split(split_factor).expanding(min_periods=1).sum().clip(upper=5) / 5.0)
    peak_u = _rolling_max(closeunadj, _TD_YEAR)
    dd_u   = _safe_div_abs(closeunadj - peak_u, peak_u).abs().clip(upper=1.0)
    peak_a = _rolling_max(close, _TD_YEAR)
    dd_a   = _safe_div_abs(close - peak_a, peak_a).abs().clip(upper=1.0)
    return (rs504 + sub2 + frac1 + cnt_rs + dd_u + dd_a) / 6.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

REVERSE_SPLIT_SIGNAL_REGISTRY_076_150 = {
    "rss_076_close_below_1_flag":                          {"inputs": ["close"],                           "func": rss_076_close_below_1_flag},
    "rss_077_close_below_2_flag":                          {"inputs": ["close"],                           "func": rss_077_close_below_2_flag},
    "rss_078_close_below_5_flag":                          {"inputs": ["close"],                           "func": rss_078_close_below_5_flag},
    "rss_079_close_zscore_252d":                           {"inputs": ["close"],                           "func": rss_079_close_zscore_252d},
    "rss_080_close_pct_rank_252d":                         {"inputs": ["close"],                           "func": rss_080_close_pct_rank_252d},
    "rss_081_close_drawdown_from_252d_peak":               {"inputs": ["close"],                           "func": rss_081_close_drawdown_from_252d_peak},
    "rss_082_close_pct_drawdown_252d":                     {"inputs": ["close"],                           "func": rss_082_close_pct_drawdown_252d},
    "rss_083_close_drawdown_from_504d_peak":               {"inputs": ["close"],                           "func": rss_083_close_drawdown_from_504d_peak},
    "rss_084_close_pct_drawdown_504d":                     {"inputs": ["close"],                           "func": rss_084_close_pct_drawdown_504d},
    "rss_085_close_drawdown_from_expanding_peak":          {"inputs": ["close"],                           "func": rss_085_close_drawdown_from_expanding_peak},
    "rss_086_close_pct_drawdown_expanding":                {"inputs": ["close"],                           "func": rss_086_close_pct_drawdown_expanding},
    "rss_087_close_log_price":                             {"inputs": ["close"],                           "func": rss_087_close_log_price},
    "rss_088_close_ewm_deviation_63d":                     {"inputs": ["close"],                           "func": rss_088_close_ewm_deviation_63d},
    "rss_089_close_ewm_deviation_252d":                    {"inputs": ["close"],                           "func": rss_089_close_ewm_deviation_252d},
    "rss_090_close_expanding_min":                         {"inputs": ["close"],                           "func": rss_090_close_expanding_min},
    "rss_091_closeunadj_return_1d":                        {"inputs": ["closeunadj"],                      "func": rss_091_closeunadj_return_1d},
    "rss_092_closeunadj_return_5d":                        {"inputs": ["closeunadj"],                      "func": rss_092_closeunadj_return_5d},
    "rss_093_closeunadj_return_21d":                       {"inputs": ["closeunadj"],                      "func": rss_093_closeunadj_return_21d},
    "rss_094_closeunadj_return_63d":                       {"inputs": ["closeunadj"],                      "func": rss_094_closeunadj_return_63d},
    "rss_095_closeunadj_return_252d":                      {"inputs": ["closeunadj"],                      "func": rss_095_closeunadj_return_252d},
    "rss_096_closeunadj_volatility_21d":                   {"inputs": ["closeunadj"],                      "func": rss_096_closeunadj_volatility_21d},
    "rss_097_closeunadj_volatility_63d":                   {"inputs": ["closeunadj"],                      "func": rss_097_closeunadj_volatility_63d},
    "rss_098_closeunadj_volatility_252d":                  {"inputs": ["closeunadj"],                      "func": rss_098_closeunadj_volatility_252d},
    "rss_099_closeunadj_mean_21d":                         {"inputs": ["closeunadj"],                      "func": rss_099_closeunadj_mean_21d},
    "rss_100_closeunadj_mean_63d":                         {"inputs": ["closeunadj"],                      "func": rss_100_closeunadj_mean_63d},
    "rss_101_closeunadj_mean_252d":                        {"inputs": ["closeunadj"],                      "func": rss_101_closeunadj_mean_252d},
    "rss_102_closeunadj_pct_rank_504d":                    {"inputs": ["closeunadj"],                      "func": rss_102_closeunadj_pct_rank_504d},
    "rss_103_closeunadj_pct_rank_expanding":               {"inputs": ["closeunadj"],                      "func": rss_103_closeunadj_pct_rank_expanding},
    "rss_104_closeunadj_zscore_504d":                      {"inputs": ["closeunadj"],                      "func": rss_104_closeunadj_zscore_504d},
    "rss_105_closeunadj_below_21d_mean_flag":              {"inputs": ["closeunadj"],                      "func": rss_105_closeunadj_below_21d_mean_flag},
    "rss_106_rs_within_252d_and_drawdown_lt_neg50_flag":   {"inputs": ["split_factor", "close"],           "func": rss_106_rs_within_252d_and_drawdown_lt_neg50_flag},
    "rss_107_rs_within_504d_and_below5_flag":              {"inputs": ["split_factor", "closeunadj"],      "func": rss_107_rs_within_504d_and_below5_flag},
    "rss_108_rs_count_252d_x_log_mag":                     {"inputs": ["split_factor"],                    "func": rss_108_rs_count_252d_x_log_mag},
    "rss_109_close_pct_drawdown_252d_x_rs_ever_flag":      {"inputs": ["split_factor", "close"],           "func": rss_109_close_pct_drawdown_252d_x_rs_ever_flag},
    "rss_110_closeunadj_pct_drawdown_252d_x_rs_21d":       {"inputs": ["split_factor", "closeunadj"],      "func": rss_110_closeunadj_pct_drawdown_252d_x_rs_21d},
    "rss_111_rs_magnitude_x_below5_flag":                  {"inputs": ["split_factor", "closeunadj"],      "func": rss_111_rs_magnitude_x_below5_flag},
    "rss_112_cumulative_rs_factor_252d_log":               {"inputs": ["split_factor"],                    "func": rss_112_cumulative_rs_factor_252d_log},
    "rss_113_cumulative_rs_factor_expanding_log":          {"inputs": ["split_factor"],                    "func": rss_113_cumulative_rs_factor_expanding_log},
    "rss_114_rs_count_252d_x_closeunadj_below2":           {"inputs": ["split_factor", "closeunadj"],      "func": rss_114_rs_count_252d_x_closeunadj_below2},
    "rss_115_days_since_rs_x_below1_flag":                 {"inputs": ["split_factor", "closeunadj"],      "func": rss_115_days_since_rs_x_below1_flag},
    "rss_116_closeunadj_max_252d":                         {"inputs": ["closeunadj"],                      "func": rss_116_closeunadj_max_252d},
    "rss_117_closeunadj_range_252d":                       {"inputs": ["closeunadj"],                      "func": rss_117_closeunadj_range_252d},
    "rss_118_closeunadj_normalized_position_252d":         {"inputs": ["closeunadj"],                      "func": rss_118_closeunadj_normalized_position_252d},
    "rss_119_closeunadj_below_63d_min_flag":               {"inputs": ["closeunadj"],                      "func": rss_119_closeunadj_below_63d_min_flag},
    "rss_120_closeunadj_below_252d_min_flag":              {"inputs": ["closeunadj"],                      "func": rss_120_closeunadj_below_252d_min_flag},
    "rss_121_close_return_1d":                             {"inputs": ["close"],                           "func": rss_121_close_return_1d},
    "rss_122_close_return_21d":                            {"inputs": ["close"],                           "func": rss_122_close_return_21d},
    "rss_123_close_return_63d":                            {"inputs": ["close"],                           "func": rss_123_close_return_63d},
    "rss_124_close_return_252d":                           {"inputs": ["close"],                           "func": rss_124_close_return_252d},
    "rss_125_close_return_504d":                           {"inputs": ["close"],                           "func": rss_125_close_return_504d},
    "rss_126_close_volatility_21d":                        {"inputs": ["close"],                           "func": rss_126_close_volatility_21d},
    "rss_127_close_volatility_63d":                        {"inputs": ["close"],                           "func": rss_127_close_volatility_63d},
    "rss_128_close_volatility_252d":                       {"inputs": ["close"],                           "func": rss_128_close_volatility_252d},
    "rss_129_close_below_63d_mean_flag":                   {"inputs": ["close"],                           "func": rss_129_close_below_63d_mean_flag},
    "rss_130_close_below_252d_mean_flag":                  {"inputs": ["close"],                           "func": rss_130_close_below_252d_mean_flag},
    "rss_131_close_days_below_252d_mean_count":            {"inputs": ["close"],                           "func": rss_131_close_days_below_252d_mean_count},
    "rss_132_closeunadj_days_below_21d_mean_count_63d":    {"inputs": ["closeunadj"],                      "func": rss_132_closeunadj_days_below_21d_mean_count_63d},
    "rss_133_close_expanding_zscore":                      {"inputs": ["close"],                           "func": rss_133_close_expanding_zscore},
    "rss_134_closeunadj_expanding_zscore":                 {"inputs": ["closeunadj"],                      "func": rss_134_closeunadj_expanding_zscore},
    "rss_135_closeunadj_below_3_flag":                     {"inputs": ["closeunadj"],                      "func": rss_135_closeunadj_below_3_flag},
    "rss_136_rs_within_21d_and_below1_flag":               {"inputs": ["split_factor", "closeunadj"],      "func": rss_136_rs_within_21d_and_below1_flag},
    "rss_137_rs_within_63d_and_below2_flag":               {"inputs": ["split_factor", "closeunadj"],      "func": rss_137_rs_within_63d_and_below2_flag},
    "rss_138_fs_count_504d":                               {"inputs": ["split_factor"],                    "func": rss_138_fs_count_504d},
    "rss_139_rs_minus_fs_count_504d":                      {"inputs": ["split_factor"],                    "func": rss_139_rs_minus_fs_count_504d},
    "rss_140_closeunadj_median_252d":                      {"inputs": ["closeunadj"],                      "func": rss_140_closeunadj_median_252d},
    "rss_141_closeunadj_below_median_252d_flag":           {"inputs": ["closeunadj"],                      "func": rss_141_closeunadj_below_median_252d_flag},
    "rss_142_rs_severity_ewm_span63":                      {"inputs": ["split_factor"],                    "func": rss_142_rs_severity_ewm_span63},
    "rss_143_rs_severity_ewm_span252":                     {"inputs": ["split_factor"],                    "func": rss_143_rs_severity_ewm_span252},
    "rss_144_closeunadj_std_21d":                          {"inputs": ["closeunadj"],                      "func": rss_144_closeunadj_std_21d},
    "rss_145_closeunadj_std_63d":                          {"inputs": ["closeunadj"],                      "func": rss_145_closeunadj_std_63d},
    "rss_146_closeunadj_cv_63d":                           {"inputs": ["closeunadj"],                      "func": rss_146_closeunadj_cv_63d},
    "rss_147_close_below_all_time_low_approach":           {"inputs": ["close"],                           "func": rss_147_close_below_all_time_low_approach},
    "rss_148_distress_composite_score":                    {"inputs": ["split_factor", "closeunadj"],      "func": rss_148_distress_composite_score},
    "rss_149_rs_count_252d_x_volatility_21d":              {"inputs": ["split_factor", "closeunadj"],      "func": rss_149_rs_count_252d_x_volatility_21d},
    "rss_150_reverse_split_signal_composite":              {"inputs": ["split_factor", "closeunadj", "close"], "func": rss_150_reverse_split_signal_composite},
    "rss_176_close_zscore_504d":                           {"inputs": ["close"],                           "func": rss_176_close_zscore_504d},
    "rss_177_close_median_252d":                           {"inputs": ["close"],                           "func": rss_177_close_median_252d},
    "rss_178_close_below_median_252d_flag":                {"inputs": ["close"],                           "func": rss_178_close_below_median_252d_flag},
    "rss_179_close_mean_21d":                              {"inputs": ["close"],                           "func": rss_179_close_mean_21d},
    "rss_180_close_mean_63d":                              {"inputs": ["close"],                           "func": rss_180_close_mean_63d},
    "rss_181_close_std_21d":                               {"inputs": ["close"],                           "func": rss_181_close_std_21d},
    "rss_182_close_std_63d":                               {"inputs": ["close"],                           "func": rss_182_close_std_63d},
    "rss_183_close_cv_63d":                                {"inputs": ["close"],                           "func": rss_183_close_cv_63d},
    "rss_184_close_range_252d":                            {"inputs": ["close"],                           "func": rss_184_close_range_252d},
    "rss_185_close_normalized_position_252d":              {"inputs": ["close"],                           "func": rss_185_close_normalized_position_252d},
    "rss_186_close_below_504d_mean_flag":                  {"inputs": ["close"],                           "func": rss_186_close_below_504d_mean_flag},
    "rss_187_close_return_126d":                           {"inputs": ["close"],                           "func": rss_187_close_return_126d},
    "rss_188_closeunadj_return_126d":                      {"inputs": ["closeunadj"],                      "func": rss_188_closeunadj_return_126d},
    "rss_189_closeunadj_volatility_126d":                  {"inputs": ["closeunadj"],                      "func": rss_189_closeunadj_volatility_126d},
    "rss_190_close_volatility_126d":                       {"inputs": ["close"],                           "func": rss_190_close_volatility_126d},
    "rss_191_rs_within_252d_and_below2_flag":              {"inputs": ["split_factor", "closeunadj"],      "func": rss_191_rs_within_252d_and_below2_flag},
    "rss_192_rs_within_504d_and_below1_flag":              {"inputs": ["split_factor", "closeunadj"],      "func": rss_192_rs_within_504d_and_below1_flag},
    "rss_193_close_days_below_504d_mean_count":            {"inputs": ["close"],                           "func": rss_193_close_days_below_504d_mean_count},
    "rss_194_closeunadj_days_below_2_count_63d":           {"inputs": ["closeunadj"],                      "func": rss_194_closeunadj_days_below_2_count_63d},
    "rss_195_rs_count_252d_x_log_price":                   {"inputs": ["split_factor", "closeunadj"],      "func": rss_195_rs_count_252d_x_log_price},
    "rss_196_closeunadj_ewm_deviation_21d":                {"inputs": ["closeunadj"],                      "func": rss_196_closeunadj_ewm_deviation_21d},
    "rss_197_closeunadj_ewm_deviation_63d":                {"inputs": ["closeunadj"],                      "func": rss_197_closeunadj_ewm_deviation_63d},
    "rss_198_rs_recency_decay_wk":                         {"inputs": ["split_factor"],                    "func": rss_198_rs_recency_decay_wk},
    "rss_199_close_expanding_zscore":                      {"inputs": ["close"],                           "func": rss_199_close_expanding_zscore},
    "rss_200_distress_composite_v2":                       {"inputs": ["split_factor", "closeunadj", "close"], "func": rss_200_distress_composite_v2},
}
