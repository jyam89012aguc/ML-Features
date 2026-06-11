"""
25_momentum_decay — Base Features 076-150
Domain: trailing-return decay across horizons — momentum decay / cross-horizon return term structure
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


def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    """Log return over n periods."""
    return np.log(s.clip(lower=_EPS)) - np.log(s.shift(n).clip(lower=_EPS))


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Rolling slope of trailing returns (momentum slope) ---

def mdc_076_slope_ret_5d_over_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5d log-return series over trailing 21 days (short momentum trend)."""
    return _linslope(_log_ret(close, _TD_WEEK), _TD_MON)


def mdc_077_slope_ret_5d_over_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 5d log-return over trailing 63 days."""
    return _linslope(_log_ret(close, _TD_WEEK), _TD_QTR)


def mdc_078_slope_ret_21d_over_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d log-return over trailing 63 days."""
    return _linslope(_log_ret(close, _TD_MON), _TD_QTR)


def mdc_079_slope_ret_21d_over_126d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d log-return over trailing 126 days."""
    return _linslope(_log_ret(close, _TD_MON), _TD_HALF)


def mdc_080_slope_ret_63d_over_252d(close: pd.Series) -> pd.Series:
    """OLS slope of 63d log-return over trailing 252 days."""
    return _linslope(_log_ret(close, _TD_QTR), _TD_YEAR)


def mdc_081_slope_ret_126d_over_252d(close: pd.Series) -> pd.Series:
    """OLS slope of 126d log-return over trailing 252 days."""
    return _linslope(_log_ret(close, _TD_HALF), _TD_YEAR)


def mdc_082_slope_ret_5d_21d_slope_diff(close: pd.Series) -> pd.Series:
    """Difference of 5d-slope over 21d minus 21d-slope over 63d (slope divergence)."""
    s5_21 = _linslope(_log_ret(close, _TD_WEEK), _TD_MON)
    s21_63 = _linslope(_log_ret(close, _TD_MON), _TD_QTR)
    return s5_21 - s21_63


def mdc_083_ewm_ret_5d_span21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of 5d returns: exponentially weighted short-term momentum."""
    return _ewm_mean(_log_ret(close, _TD_WEEK), _TD_MON)


def mdc_084_ewm_ret_21d_span63(close: pd.Series) -> pd.Series:
    """EWM (span=63) of 21d returns."""
    return _ewm_mean(_log_ret(close, _TD_MON), _TD_QTR)


def mdc_085_ewm_ret_63d_span252(close: pd.Series) -> pd.Series:
    """EWM (span=252) of 63d returns (very smooth quarterly momentum signal)."""
    return _ewm_mean(_log_ret(close, _TD_QTR), _TD_YEAR)


# --- Group I (086-095): Rolling count of negative-return horizons ---

def mdc_086_neg_ret_5d_count_63d(close: pd.Series) -> pd.Series:
    """Count of trailing 63 days where 5d return was negative."""
    r5 = _log_ret(close, _TD_WEEK)
    return (r5 < 0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def mdc_087_neg_ret_21d_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing 252 days where 21d return was negative."""
    r21 = _log_ret(close, _TD_MON)
    return (r21 < 0).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def mdc_088_neg_ret_63d_count_252d(close: pd.Series) -> pd.Series:
    """Count of trailing 252 days where 63d return was negative."""
    r63 = _log_ret(close, _TD_QTR)
    return (r63 < 0).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def mdc_089_frac_neg_ret_5d_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days with negative 5d return."""
    r5 = _log_ret(close, _TD_WEEK)
    return (r5 < 0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def mdc_090_frac_neg_ret_21d_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days with negative 21d return."""
    r21 = _log_ret(close, _TD_MON)
    return (r21 < 0).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def mdc_091_frac_neg_ret_63d_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days with negative 63d return."""
    r63 = _log_ret(close, _TD_QTR)
    return (r63 < 0).astype(float).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def mdc_092_ret_5d_below_mean_63d_flag(close: pd.Series) -> pd.Series:
    """Flag: current 5d return is below its 63-day rolling mean."""
    r5 = _log_ret(close, _TD_WEEK)
    return (r5 < _rolling_mean(r5, _TD_QTR)).astype(float)


def mdc_093_ret_21d_below_mean_252d_flag(close: pd.Series) -> pd.Series:
    """Flag: current 21d return is below its 252-day rolling mean."""
    r21 = _log_ret(close, _TD_MON)
    return (r21 < _rolling_mean(r21, _TD_YEAR)).astype(float)


def mdc_094_ret_63d_below_mean_252d_flag(close: pd.Series) -> pd.Series:
    """Flag: current 63d return is below its 252-day rolling mean."""
    r63 = _log_ret(close, _TD_QTR)
    return (r63 < _rolling_mean(r63, _TD_YEAR)).astype(float)


def mdc_095_all_horizons_below_mean_flag(close: pd.Series) -> pd.Series:
    """Flag: 5d, 21d, and 63d returns all below their respective 252d means."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    return ((r5 < _rolling_mean(r5, _TD_YEAR)) &
            (r21 < _rolling_mean(r21, _TD_YEAR)) &
            (r63 < _rolling_mean(r63, _TD_YEAR))).astype(float)


# --- Group J (096-105): Volume-weighted momentum decay ---

def mdc_096_vol_weighted_ret_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d return scaled by relative volume (high-vol moves weighted more)."""
    r5 = _log_ret(close, _TD_WEEK)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return r5 * vol_norm


def mdc_097_vol_weighted_ret_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d return scaled by relative volume."""
    r21 = _log_ret(close, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    return r21 * vol_norm


def mdc_098_vol_weighted_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d return scaled by relative volume."""
    r63 = _log_ret(close, _TD_QTR)
    avg_vol = _rolling_mean(volume, _TD_HALF)
    vol_norm = _safe_div(volume, avg_vol)
    return r63 * vol_norm


def mdc_099_vol_weighted_decay_5_minus_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 5d return minus volume-weighted 21d return."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    return (_log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)) * vol_norm


def mdc_100_vol_weighted_decay_21_minus_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 21d minus 63d return spread."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    vol_norm = _safe_div(volume, avg_vol)
    return (_log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR)) * vol_norm


def mdc_101_up_day_avg_ret_5d(close: pd.Series) -> pd.Series:
    """Average 1d return on up-days over last 5 days."""
    r1 = _log_ret(close, 1)
    up = r1.where(r1 > 0, np.nan)
    return up.rolling(_TD_WEEK, min_periods=1).mean()


def mdc_102_down_day_avg_ret_5d(close: pd.Series) -> pd.Series:
    """Average 1d return on down-days over last 5 days."""
    r1 = _log_ret(close, 1)
    dn = r1.where(r1 < 0, np.nan)
    return dn.rolling(_TD_WEEK, min_periods=1).mean()


def mdc_103_up_day_avg_ret_21d(close: pd.Series) -> pd.Series:
    """Average 1d return on up-days over last 21 days."""
    r1 = _log_ret(close, 1)
    up = r1.where(r1 > 0, np.nan)
    return up.rolling(_TD_MON, min_periods=1).mean()


def mdc_104_down_day_avg_ret_21d(close: pd.Series) -> pd.Series:
    """Average 1d return on down-days over last 21 days."""
    r1 = _log_ret(close, 1)
    dn = r1.where(r1 < 0, np.nan)
    return dn.rolling(_TD_MON, min_periods=1).mean()


def mdc_105_up_down_ret_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of avg up-day return to abs avg down-day return over 21d (gain/loss ratio)."""
    r1 = _log_ret(close, 1)
    up = r1.where(r1 > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    dn = r1.where(r1 < 0, np.nan).rolling(_TD_MON, min_periods=1).mean().abs()
    return _safe_div(up, dn)


# --- Group K (106-115): Cross-period return comparisons and sign changes ---

def mdc_106_ret_most_recent_month_vs_prior_year(close: pd.Series) -> pd.Series:
    """21d return vs prior 252d (excluding most recent month) return ratio."""
    r21 = _log_ret(close, _TD_MON)
    r_prior = _log_ret(close.shift(_TD_MON), _TD_YEAR)
    return _safe_div(r21, r_prior.abs() + _EPS)


def mdc_107_ret_rolling_max_252d(close: pd.Series) -> pd.Series:
    """Rolling maximum 5d return seen in trailing 252 days (best recent short momentum)."""
    return _rolling_max(_log_ret(close, _TD_WEEK), _TD_YEAR)


def mdc_108_ret_rolling_min_252d_5d(close: pd.Series) -> pd.Series:
    """Rolling minimum 5d return in trailing 252 days (worst short momentum in year)."""
    return _rolling_min(_log_ret(close, _TD_WEEK), _TD_YEAR)


def mdc_109_ret_current_5d_vs_max_252d(close: pd.Series) -> pd.Series:
    """Current 5d return divided by 252-day max 5d return (proximity to worst)."""
    r5 = _log_ret(close, _TD_WEEK)
    mx = _rolling_max(r5, _TD_YEAR)
    return _safe_div(r5, mx.abs() + _EPS)


def mdc_110_ret_current_5d_vs_min_252d(close: pd.Series) -> pd.Series:
    """Current 5d return divided by 252-day min 5d return (fraction of worst week)."""
    r5 = _log_ret(close, _TD_WEEK)
    mn = _rolling_min(r5, _TD_YEAR)
    return _safe_div(r5, mn.abs() + _EPS)


def mdc_111_ret_3m_vs_prior_3m(close: pd.Series) -> pd.Series:
    """Most-recent 63d return minus prior 63d return (63-126d ago)."""
    recent = _log_ret(close, _TD_QTR)
    prior = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    return recent - prior


def mdc_112_ret_1m_vs_prior_1m(close: pd.Series) -> pd.Series:
    """Most-recent 21d return minus prior 21d return (21-42d ago)."""
    recent = _log_ret(close, _TD_MON)
    prior = _log_ret(close.shift(_TD_MON), _TD_MON)
    return recent - prior


def mdc_113_ret_1w_vs_prior_1w(close: pd.Series) -> pd.Series:
    """Most-recent 5d return minus prior 5d return (5-10d ago)."""
    recent = _log_ret(close, _TD_WEEK)
    prior = _log_ret(close.shift(_TD_WEEK), _TD_WEEK)
    return recent - prior


def mdc_114_ret_sign_change_5_to_21(close: pd.Series) -> pd.Series:
    """Sign change: 5d negative while prior 5d positive (fresh momentum reversal)."""
    r5 = _log_ret(close, _TD_WEEK)
    r5_lag = r5.shift(_TD_WEEK)
    return ((r5 < 0) & (r5_lag > 0)).astype(float)


def mdc_115_ret_sign_change_21_to_63(close: pd.Series) -> pd.Series:
    """Sign change: 21d negative while prior 21d positive (monthly reversal)."""
    r21 = _log_ret(close, _TD_MON)
    r21_lag = r21.shift(_TD_MON)
    return ((r21 < 0) & (r21_lag > 0)).astype(float)


# --- Group L (116-125): Normalized spreads and relative performance ---

def mdc_116_spread_5_21_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d-minus-21d spread within trailing 252 days."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_117_spread_21_63_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d-minus-63d spread within trailing 252 days."""
    spread = _log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_118_spread_63_252_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d-minus-252d spread within trailing 252 days."""
    spread = _log_ret(close, _TD_QTR) - _log_ret(close, _TD_YEAR)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_119_ret_5d_over_rolling_std_21d(close: pd.Series) -> pd.Series:
    """5d return divided by 21-day rolling std of 1d returns (Sharpe-like decay)."""
    r5 = _log_ret(close, _TD_WEEK)
    r1_std = _rolling_std(_log_ret(close, 1), _TD_MON)
    return _safe_div(r5, r1_std)


def mdc_120_ret_21d_over_rolling_std_63d(close: pd.Series) -> pd.Series:
    """21d return divided by 63-day rolling std of 1d returns."""
    r21 = _log_ret(close, _TD_MON)
    r1_std = _rolling_std(_log_ret(close, 1), _TD_QTR)
    return _safe_div(r21, r1_std)


def mdc_121_ret_63d_over_rolling_std_252d(close: pd.Series) -> pd.Series:
    """63d return divided by 252-day rolling std of 1d returns."""
    r63 = _log_ret(close, _TD_QTR)
    r1_std = _rolling_std(_log_ret(close, 1), _TD_YEAR)
    return _safe_div(r63, r1_std)


def mdc_122_ret_252d_over_rolling_std_252d(close: pd.Series) -> pd.Series:
    """252d return divided by 252-day rolling std (annual Sharpe ratio proxy)."""
    r252 = _log_ret(close, _TD_YEAR)
    r1_std = _rolling_std(_log_ret(close, 1), _TD_YEAR) * np.sqrt(_TD_YEAR)
    return _safe_div(r252, r1_std)


def mdc_123_decay_ratio_short_sr_vs_long_sr(close: pd.Series) -> pd.Series:
    """Short Sharpe (5d/std21) minus long Sharpe (252d/std252*sqrt252) — decay in quality."""
    r5 = _log_ret(close, _TD_WEEK)
    r252 = _log_ret(close, _TD_YEAR)
    std21 = _rolling_std(_log_ret(close, 1), _TD_MON)
    std252_ann = _rolling_std(_log_ret(close, 1), _TD_YEAR) * np.sqrt(_TD_YEAR)
    sr_short = _safe_div(r5 * (_TD_YEAR / _TD_WEEK), std21 * np.sqrt(_TD_YEAR))
    sr_long = _safe_div(r252, std252_ann)
    return sr_short - sr_long


def mdc_124_ret_5d_norm_by_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5d return normalized by 21-day average true range (range-adjusted decay)."""
    r5 = _log_ret(close, _TD_WEEK)
    tr = pd.concat([high - low,
                    (high - close.shift(1)).abs(),
                    (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr21_pct = _safe_div(atr21, close)
    return _safe_div(r5, atr21_pct)


def mdc_125_ret_21d_norm_by_atr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d return normalized by 63-day ATR (range-adjusted monthly decay)."""
    r21 = _log_ret(close, _TD_MON)
    tr = pd.concat([high - low,
                    (high - close.shift(1)).abs(),
                    (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr63 = _rolling_mean(tr, _TD_QTR)
    atr63_pct = _safe_div(atr63, close)
    return _safe_div(r21, atr63_pct)


# --- Group M (126-135): EWM-based momentum measures and decay comparisons ---

def mdc_126_ewm_ret_5d_span5_minus_span21(close: pd.Series) -> pd.Series:
    """Diff of fast EWM (span=5) minus slow EWM (span=21) of 5d returns."""
    r5 = _log_ret(close, _TD_WEEK)
    return _ewm_mean(r5, _TD_WEEK) - _ewm_mean(r5, _TD_MON)


def mdc_127_ewm_ret_21d_span21_minus_span63(close: pd.Series) -> pd.Series:
    """Diff of fast EWM (span=21) minus slow EWM (span=63) of 21d returns."""
    r21 = _log_ret(close, _TD_MON)
    return _ewm_mean(r21, _TD_MON) - _ewm_mean(r21, _TD_QTR)


def mdc_128_ewm_ret_63d_span63_minus_span252(close: pd.Series) -> pd.Series:
    """Diff of fast EWM (span=63) minus slow EWM (span=252) of 63d returns."""
    r63 = _log_ret(close, _TD_QTR)
    return _ewm_mean(r63, _TD_QTR) - _ewm_mean(r63, _TD_YEAR)


def mdc_129_ewm_decay_5d_crossunder_21d_flag(close: pd.Series) -> pd.Series:
    """Flag: EWM(span=5) of 5d returns < EWM(span=21) of 5d returns (bearish cross)."""
    r5 = _log_ret(close, _TD_WEEK)
    return (_ewm_mean(r5, _TD_WEEK) < _ewm_mean(r5, _TD_MON)).astype(float)


def mdc_130_ewm_decay_21d_crossunder_63d_flag(close: pd.Series) -> pd.Series:
    """Flag: EWM(span=21) of 21d returns < EWM(span=63) of 21d returns."""
    r21 = _log_ret(close, _TD_MON)
    return (_ewm_mean(r21, _TD_MON) < _ewm_mean(r21, _TD_QTR)).astype(float)


def mdc_131_ret_5d_minus_ewm_5d_21d(close: pd.Series) -> pd.Series:
    """Current 5d return minus its 21-day EWM (deviation from trend)."""
    r5 = _log_ret(close, _TD_WEEK)
    return r5 - _ewm_mean(r5, _TD_MON)


def mdc_132_ret_21d_minus_ewm_21d_63d(close: pd.Series) -> pd.Series:
    """Current 21d return minus its 63-day EWM."""
    r21 = _log_ret(close, _TD_MON)
    return r21 - _ewm_mean(r21, _TD_QTR)


def mdc_133_ret_63d_minus_ewm_63d_252d(close: pd.Series) -> pd.Series:
    """Current 63d return minus its 252-day EWM."""
    r63 = _log_ret(close, _TD_QTR)
    return r63 - _ewm_mean(r63, _TD_YEAR)


def mdc_134_ewm_decay_composite_3level(close: pd.Series) -> pd.Series:
    """Average of three EWM-vs-slow cross signals (5d, 21d, 63d decay composite)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    d5 = (_ewm_mean(r5, _TD_WEEK) < _ewm_mean(r5, _TD_MON)).astype(float)
    d21 = (_ewm_mean(r21, _TD_MON) < _ewm_mean(r21, _TD_QTR)).astype(float)
    d63 = (_ewm_mean(r63, _TD_QTR) < _ewm_mean(r63, _TD_YEAR)).astype(float)
    return (d5 + d21 + d63) / 3.0


def mdc_135_ret_sum_5_21_63_weighted(close: pd.Series) -> pd.Series:
    """Weighted sum of 5d/21d/63d returns (3/2/1 weights) — recency-weighted momentum."""
    return (3 * _log_ret(close, _TD_WEEK) +
            2 * _log_ret(close, _TD_MON) +
            1 * _log_ret(close, _TD_QTR)) / 6.0


# --- Group N (136-145): Multi-period compounding and geometric decay ---

def mdc_136_cumulative_monthly_rets_sum_6m(close: pd.Series) -> pd.Series:
    """Sum of 6 non-overlapping monthly (21d) returns over trailing 126d."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    return r21_0 + r21_1 + r21_2 + r21_3 + r21_4 + r21_5


def mdc_137_best_monthly_ret_in_6m(close: pd.Series) -> pd.Series:
    """Best (maximum) of 6 sequential monthly returns over trailing 126d."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    return pd.concat([r21_0, r21_1, r21_2, r21_3, r21_4, r21_5], axis=1).max(axis=1)


def mdc_138_worst_monthly_ret_in_6m(close: pd.Series) -> pd.Series:
    """Worst (minimum) of 6 sequential monthly returns over trailing 126d."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    return pd.concat([r21_0, r21_1, r21_2, r21_3, r21_4, r21_5], axis=1).min(axis=1)


def mdc_139_neg_monthly_count_in_6m(close: pd.Series) -> pd.Series:
    """Count of negative months in trailing 6 sequential monthly periods (0-6)."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    return ((r21_0 < 0).astype(float) + (r21_1 < 0).astype(float) +
            (r21_2 < 0).astype(float) + (r21_3 < 0).astype(float) +
            (r21_4 < 0).astype(float) + (r21_5 < 0).astype(float))


def mdc_140_recent_month_vs_avg_6m_months(close: pd.Series) -> pd.Series:
    """Most-recent month's return vs avg of prior 5 months (momentum decay)."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    prior_avg = (r21_1 + r21_2 + r21_3 + r21_4 + r21_5) / 5.0
    return r21_0 - prior_avg


def mdc_141_quarterly_rets_sum_4q(close: pd.Series) -> pd.Series:
    """Sum of 4 non-overlapping quarterly returns over trailing year."""
    r63_0 = _log_ret(close, _TD_QTR)
    r63_1 = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    r63_2 = _log_ret(close.shift(2 * _TD_QTR), _TD_QTR)
    r63_3 = _log_ret(close.shift(3 * _TD_QTR), _TD_QTR)
    return r63_0 + r63_1 + r63_2 + r63_3


def mdc_142_worst_quarterly_in_4q(close: pd.Series) -> pd.Series:
    """Minimum of 4 non-overlapping quarterly returns over trailing year."""
    r63_0 = _log_ret(close, _TD_QTR)
    r63_1 = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    r63_2 = _log_ret(close.shift(2 * _TD_QTR), _TD_QTR)
    r63_3 = _log_ret(close.shift(3 * _TD_QTR), _TD_QTR)
    return pd.concat([r63_0, r63_1, r63_2, r63_3], axis=1).min(axis=1)


def mdc_143_recent_quarter_vs_avg_prior_3q(close: pd.Series) -> pd.Series:
    """Most-recent quarter return vs avg of prior 3 quarterly returns."""
    r63_0 = _log_ret(close, _TD_QTR)
    r63_1 = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    r63_2 = _log_ret(close.shift(2 * _TD_QTR), _TD_QTR)
    r63_3 = _log_ret(close.shift(3 * _TD_QTR), _TD_QTR)
    prior_avg = (r63_1 + r63_2 + r63_3) / 3.0
    return r63_0 - prior_avg


def mdc_144_neg_quarterly_count_in_4q(close: pd.Series) -> pd.Series:
    """Count of negative quarters in trailing 4 sequential quarterly periods (0-4)."""
    r63_0 = _log_ret(close, _TD_QTR)
    r63_1 = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    r63_2 = _log_ret(close.shift(2 * _TD_QTR), _TD_QTR)
    r63_3 = _log_ret(close.shift(3 * _TD_QTR), _TD_QTR)
    return ((r63_0 < 0).astype(float) + (r63_1 < 0).astype(float) +
            (r63_2 < 0).astype(float) + (r63_3 < 0).astype(float))


def mdc_145_ret_4q_worst_minus_best_spread(close: pd.Series) -> pd.Series:
    """Worst minus best quarterly return over 4 periods (width of quarterly range)."""
    r63_0 = _log_ret(close, _TD_QTR)
    r63_1 = _log_ret(close.shift(_TD_QTR), _TD_QTR)
    r63_2 = _log_ret(close.shift(2 * _TD_QTR), _TD_QTR)
    r63_3 = _log_ret(close.shift(3 * _TD_QTR), _TD_QTR)
    df4q = pd.concat([r63_0, r63_1, r63_2, r63_3], axis=1)
    return df4q.min(axis=1) - df4q.max(axis=1)


# --- Group O (146-150): Composite cross-horizon decay indices ---

def mdc_146_decay_index_5_21_63_126_252(close: pd.Series) -> pd.Series:
    """Weighted decay index: sum of horizon-signed returns (shorter = more weight)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    return (5 * r5 + 4 * r21 + 3 * r63 + 2 * r126 + 1 * r252) / 15.0


def mdc_147_all_negative_flags_score(close: pd.Series) -> pd.Series:
    """Score: fraction of 5 horizons (5/21/63/126/252d) that are negative (0 to 1)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    return ((r5 < 0).astype(float) + (r21 < 0).astype(float) +
            (r63 < 0).astype(float) + (r126 < 0).astype(float) +
            (r252 < 0).astype(float)) / 5.0


def mdc_148_decay_acceleration_composite(close: pd.Series) -> pd.Series:
    """Composite: avg of (5d-21d), (21d-63d), (63d-252d) spread signs."""
    s1 = np.sign(_log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON))
    s2 = np.sign(_log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR))
    s3 = np.sign(_log_ret(close, _TD_QTR) - _log_ret(close, _TD_YEAR))
    return (s1 + s2 + s3) / 3.0


def mdc_149_multi_horizon_ret_dispersion(close: pd.Series) -> pd.Series:
    """Std dev of 5 horizon log-returns (dispersion across term structure)."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    return pd.concat([r5, r21, r63, r126, r252], axis=1).std(axis=1)


def mdc_150_decay_regime_score(close: pd.Series) -> pd.Series:
    """Regime score: z-score sum of all horizons normalized by 252d std each."""
    def _z(r):
        m = _rolling_mean(r, _TD_YEAR)
        s = _rolling_std(r, _TD_YEAR)
        return _safe_div(r - m, s)
    z5 = _z(_log_ret(close, _TD_WEEK))
    z21 = _z(_log_ret(close, _TD_MON))
    z63 = _z(_log_ret(close, _TD_QTR))
    z126 = _z(_log_ret(close, _TD_HALF))
    z252 = _z(_log_ret(close, _TD_YEAR))
    return (z5 + z21 + z63 + z126 + z252) / 5.0


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DECAY_REGISTRY_076_150 = {
    "mdc_076_slope_ret_5d_over_21d": {"inputs": ["close"], "func": mdc_076_slope_ret_5d_over_21d},
    "mdc_077_slope_ret_5d_over_63d": {"inputs": ["close"], "func": mdc_077_slope_ret_5d_over_63d},
    "mdc_078_slope_ret_21d_over_63d": {"inputs": ["close"], "func": mdc_078_slope_ret_21d_over_63d},
    "mdc_079_slope_ret_21d_over_126d": {"inputs": ["close"], "func": mdc_079_slope_ret_21d_over_126d},
    "mdc_080_slope_ret_63d_over_252d": {"inputs": ["close"], "func": mdc_080_slope_ret_63d_over_252d},
    "mdc_081_slope_ret_126d_over_252d": {"inputs": ["close"], "func": mdc_081_slope_ret_126d_over_252d},
    "mdc_082_slope_ret_5d_21d_slope_diff": {"inputs": ["close"], "func": mdc_082_slope_ret_5d_21d_slope_diff},
    "mdc_083_ewm_ret_5d_span21": {"inputs": ["close"], "func": mdc_083_ewm_ret_5d_span21},
    "mdc_084_ewm_ret_21d_span63": {"inputs": ["close"], "func": mdc_084_ewm_ret_21d_span63},
    "mdc_085_ewm_ret_63d_span252": {"inputs": ["close"], "func": mdc_085_ewm_ret_63d_span252},
    "mdc_086_neg_ret_5d_count_63d": {"inputs": ["close"], "func": mdc_086_neg_ret_5d_count_63d},
    "mdc_087_neg_ret_21d_count_252d": {"inputs": ["close"], "func": mdc_087_neg_ret_21d_count_252d},
    "mdc_088_neg_ret_63d_count_252d": {"inputs": ["close"], "func": mdc_088_neg_ret_63d_count_252d},
    "mdc_089_frac_neg_ret_5d_63d": {"inputs": ["close"], "func": mdc_089_frac_neg_ret_5d_63d},
    "mdc_090_frac_neg_ret_21d_252d": {"inputs": ["close"], "func": mdc_090_frac_neg_ret_21d_252d},
    "mdc_091_frac_neg_ret_63d_252d": {"inputs": ["close"], "func": mdc_091_frac_neg_ret_63d_252d},
    "mdc_092_ret_5d_below_mean_63d_flag": {"inputs": ["close"], "func": mdc_092_ret_5d_below_mean_63d_flag},
    "mdc_093_ret_21d_below_mean_252d_flag": {"inputs": ["close"], "func": mdc_093_ret_21d_below_mean_252d_flag},
    "mdc_094_ret_63d_below_mean_252d_flag": {"inputs": ["close"], "func": mdc_094_ret_63d_below_mean_252d_flag},
    "mdc_095_all_horizons_below_mean_flag": {"inputs": ["close"], "func": mdc_095_all_horizons_below_mean_flag},
    "mdc_096_vol_weighted_ret_5d": {"inputs": ["close", "volume"], "func": mdc_096_vol_weighted_ret_5d},
    "mdc_097_vol_weighted_ret_21d": {"inputs": ["close", "volume"], "func": mdc_097_vol_weighted_ret_21d},
    "mdc_098_vol_weighted_ret_63d": {"inputs": ["close", "volume"], "func": mdc_098_vol_weighted_ret_63d},
    "mdc_099_vol_weighted_decay_5_minus_21": {"inputs": ["close", "volume"], "func": mdc_099_vol_weighted_decay_5_minus_21},
    "mdc_100_vol_weighted_decay_21_minus_63": {"inputs": ["close", "volume"], "func": mdc_100_vol_weighted_decay_21_minus_63},
    "mdc_101_up_day_avg_ret_5d": {"inputs": ["close"], "func": mdc_101_up_day_avg_ret_5d},
    "mdc_102_down_day_avg_ret_5d": {"inputs": ["close"], "func": mdc_102_down_day_avg_ret_5d},
    "mdc_103_up_day_avg_ret_21d": {"inputs": ["close"], "func": mdc_103_up_day_avg_ret_21d},
    "mdc_104_down_day_avg_ret_21d": {"inputs": ["close"], "func": mdc_104_down_day_avg_ret_21d},
    "mdc_105_up_down_ret_ratio_21d": {"inputs": ["close"], "func": mdc_105_up_down_ret_ratio_21d},
    "mdc_106_ret_most_recent_month_vs_prior_year": {"inputs": ["close"], "func": mdc_106_ret_most_recent_month_vs_prior_year},
    "mdc_107_ret_rolling_max_252d": {"inputs": ["close"], "func": mdc_107_ret_rolling_max_252d},
    "mdc_108_ret_rolling_min_252d_5d": {"inputs": ["close"], "func": mdc_108_ret_rolling_min_252d_5d},
    "mdc_109_ret_current_5d_vs_max_252d": {"inputs": ["close"], "func": mdc_109_ret_current_5d_vs_max_252d},
    "mdc_110_ret_current_5d_vs_min_252d": {"inputs": ["close"], "func": mdc_110_ret_current_5d_vs_min_252d},
    "mdc_111_ret_3m_vs_prior_3m": {"inputs": ["close"], "func": mdc_111_ret_3m_vs_prior_3m},
    "mdc_112_ret_1m_vs_prior_1m": {"inputs": ["close"], "func": mdc_112_ret_1m_vs_prior_1m},
    "mdc_113_ret_1w_vs_prior_1w": {"inputs": ["close"], "func": mdc_113_ret_1w_vs_prior_1w},
    "mdc_114_ret_sign_change_5_to_21": {"inputs": ["close"], "func": mdc_114_ret_sign_change_5_to_21},
    "mdc_115_ret_sign_change_21_to_63": {"inputs": ["close"], "func": mdc_115_ret_sign_change_21_to_63},
    "mdc_116_spread_5_21_pctrank_252d": {"inputs": ["close"], "func": mdc_116_spread_5_21_pctrank_252d},
    "mdc_117_spread_21_63_pctrank_252d": {"inputs": ["close"], "func": mdc_117_spread_21_63_pctrank_252d},
    "mdc_118_spread_63_252_pctrank_252d": {"inputs": ["close"], "func": mdc_118_spread_63_252_pctrank_252d},
    "mdc_119_ret_5d_over_rolling_std_21d": {"inputs": ["close"], "func": mdc_119_ret_5d_over_rolling_std_21d},
    "mdc_120_ret_21d_over_rolling_std_63d": {"inputs": ["close"], "func": mdc_120_ret_21d_over_rolling_std_63d},
    "mdc_121_ret_63d_over_rolling_std_252d": {"inputs": ["close"], "func": mdc_121_ret_63d_over_rolling_std_252d},
    "mdc_122_ret_252d_over_rolling_std_252d": {"inputs": ["close"], "func": mdc_122_ret_252d_over_rolling_std_252d},
    "mdc_123_decay_ratio_short_sr_vs_long_sr": {"inputs": ["close"], "func": mdc_123_decay_ratio_short_sr_vs_long_sr},
    "mdc_124_ret_5d_norm_by_atr_21d": {"inputs": ["close", "high", "low"], "func": mdc_124_ret_5d_norm_by_atr_21d},
    "mdc_125_ret_21d_norm_by_atr_63d": {"inputs": ["close", "high", "low"], "func": mdc_125_ret_21d_norm_by_atr_63d},
    "mdc_126_ewm_ret_5d_span5_minus_span21": {"inputs": ["close"], "func": mdc_126_ewm_ret_5d_span5_minus_span21},
    "mdc_127_ewm_ret_21d_span21_minus_span63": {"inputs": ["close"], "func": mdc_127_ewm_ret_21d_span21_minus_span63},
    "mdc_128_ewm_ret_63d_span63_minus_span252": {"inputs": ["close"], "func": mdc_128_ewm_ret_63d_span63_minus_span252},
    "mdc_129_ewm_decay_5d_crossunder_21d_flag": {"inputs": ["close"], "func": mdc_129_ewm_decay_5d_crossunder_21d_flag},
    "mdc_130_ewm_decay_21d_crossunder_63d_flag": {"inputs": ["close"], "func": mdc_130_ewm_decay_21d_crossunder_63d_flag},
    "mdc_131_ret_5d_minus_ewm_5d_21d": {"inputs": ["close"], "func": mdc_131_ret_5d_minus_ewm_5d_21d},
    "mdc_132_ret_21d_minus_ewm_21d_63d": {"inputs": ["close"], "func": mdc_132_ret_21d_minus_ewm_21d_63d},
    "mdc_133_ret_63d_minus_ewm_63d_252d": {"inputs": ["close"], "func": mdc_133_ret_63d_minus_ewm_63d_252d},
    "mdc_134_ewm_decay_composite_3level": {"inputs": ["close"], "func": mdc_134_ewm_decay_composite_3level},
    "mdc_135_ret_sum_5_21_63_weighted": {"inputs": ["close"], "func": mdc_135_ret_sum_5_21_63_weighted},
    "mdc_136_cumulative_monthly_rets_sum_6m": {"inputs": ["close"], "func": mdc_136_cumulative_monthly_rets_sum_6m},
    "mdc_137_best_monthly_ret_in_6m": {"inputs": ["close"], "func": mdc_137_best_monthly_ret_in_6m},
    "mdc_138_worst_monthly_ret_in_6m": {"inputs": ["close"], "func": mdc_138_worst_monthly_ret_in_6m},
    "mdc_139_neg_monthly_count_in_6m": {"inputs": ["close"], "func": mdc_139_neg_monthly_count_in_6m},
    "mdc_140_recent_month_vs_avg_6m_months": {"inputs": ["close"], "func": mdc_140_recent_month_vs_avg_6m_months},
    "mdc_141_quarterly_rets_sum_4q": {"inputs": ["close"], "func": mdc_141_quarterly_rets_sum_4q},
    "mdc_142_worst_quarterly_in_4q": {"inputs": ["close"], "func": mdc_142_worst_quarterly_in_4q},
    "mdc_143_recent_quarter_vs_avg_prior_3q": {"inputs": ["close"], "func": mdc_143_recent_quarter_vs_avg_prior_3q},
    "mdc_144_neg_quarterly_count_in_4q": {"inputs": ["close"], "func": mdc_144_neg_quarterly_count_in_4q},
    "mdc_145_ret_4q_worst_minus_best_spread": {"inputs": ["close"], "func": mdc_145_ret_4q_worst_minus_best_spread},
    "mdc_146_decay_index_5_21_63_126_252": {"inputs": ["close"], "func": mdc_146_decay_index_5_21_63_126_252},
    "mdc_147_all_negative_flags_score": {"inputs": ["close"], "func": mdc_147_all_negative_flags_score},
    "mdc_148_decay_acceleration_composite": {"inputs": ["close"], "func": mdc_148_decay_acceleration_composite},
    "mdc_149_multi_horizon_ret_dispersion": {"inputs": ["close"], "func": mdc_149_multi_horizon_ret_dispersion},
    "mdc_150_decay_regime_score": {"inputs": ["close"], "func": mdc_150_decay_regime_score},
}
