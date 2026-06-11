"""
111_jump_discontinuity — Base Features 076-150
Domain: price jump discontinuities — bipower variation vs realized variance,
        jump test statistics, higher-order jump moments, volume-jump interaction,
        HLOC-based jump proxies, intra-period jump detection variants
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


def _log_returns(close: pd.Series) -> pd.Series:
    """Log returns: ln(close_t / close_{t-1})."""
    return np.log(close / close.shift(1))


def _realized_variance(r: pd.Series, w: int) -> pd.Series:
    """Rolling realized variance (sum of squared log returns) over w days."""
    return _rolling_sum(r ** 2, w)


def _bipower_variation(r: pd.Series, w: int) -> pd.Series:
    """Rolling bipower variation: (1/mu1^2) * sum(|r_t| * |r_{t-1}|)."""
    mu1 = np.sqrt(2.0 / np.pi)
    abs_r = r.abs()
    bp = abs_r * abs_r.shift(1)
    return (1.0 / (mu1 ** 2)) * _rolling_sum(bp, w)


def _jump_variation(r: pd.Series, w: int) -> pd.Series:
    """Jump variation = max(RV - BPV, 0)."""
    rv = _realized_variance(r, w)
    bpv = _bipower_variation(r, w)
    return (rv - bpv).clip(lower=0.0)


def _jump_flag(r: pd.Series, threshold_sigma: float = 3.0) -> pd.Series:
    """Binary flag: |return| > threshold_sigma * rolling 21d std."""
    sigma = _rolling_std(r, _TD_MON)
    return (r.abs() > threshold_sigma * sigma.fillna(_EPS)).astype(float)


def _tripower_quarticity(r: pd.Series, w: int) -> pd.Series:
    """Tripower quarticity estimator (used in Barndorff-Nielsen jump test).
    TQ = n/3 * mu_4/3^{-3} * sum(|r_{t-2}|^{4/3}|r_{t-1}|^{4/3}|r_t|^{4/3})
    where mu_{4/3} = 2^{2/3} * Gamma(7/6)/Gamma(1/2).
    """
    import math
    mu43 = (2.0 ** (2.0 / 3.0)) * (math.gamma(7.0 / 6.0) / math.gamma(0.5))
    abs_r = r.abs()
    tp = (abs_r ** (4.0 / 3.0)) * (abs_r.shift(1) ** (4.0 / 3.0)) * (abs_r.shift(2) ** (4.0 / 3.0))
    n = w
    return (n / 3.0) * (mu43 ** (-3.0)) * _rolling_sum(tp, w)


def _hl_jump_proxy(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday range as jump proxy: ln(high/low) for the day."""
    return np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Higher-order jump statistics and test statistics ---

def jmp_076_rv_bpv_ratio_252d(close: pd.Series) -> pd.Series:
    """RV / BPV over 252 days."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_YEAR)
    bpv = _bipower_variation(r, _TD_YEAR)
    return _safe_div(rv, bpv.clip(lower=_EPS))


def jmp_077_jump_test_stat_21d(close: pd.Series) -> pd.Series:
    """Barndorff-Nielsen/Shephard z-statistic for jump detection over 21 days.
    z = sqrt(n) * (RV - BPV) / (RV * sqrt(theta * max(1, TQ/BPV^2)))
    where theta = (pi/2)^2 + pi - 5 ≈ 0.6090.  Simplified version without TQ.
    Here we use: z = (RV - BPV) / (RV * sqrt(theta / n)), a rough scalar version."""
    r = _log_returns(close)
    n = _TD_MON
    theta = (np.pi / 2.0) ** 2 + np.pi - 5.0
    rv = _realized_variance(r, n)
    bpv = _bipower_variation(r, n)
    diff = (rv - bpv).clip(lower=0.0)
    denom = rv.clip(lower=_EPS) * np.sqrt(max(theta / n, _EPS))
    return _safe_div(diff, denom)


def jmp_078_jump_test_stat_63d(close: pd.Series) -> pd.Series:
    """BNS jump z-statistic over 63 days."""
    r = _log_returns(close)
    n = _TD_QTR
    theta = (np.pi / 2.0) ** 2 + np.pi - 5.0
    rv = _realized_variance(r, n)
    bpv = _bipower_variation(r, n)
    diff = (rv - bpv).clip(lower=0.0)
    denom = rv.clip(lower=_EPS) * np.sqrt(max(theta / n, _EPS))
    return _safe_div(diff, denom)


def jmp_079_rv4_21d(close: pd.Series) -> pd.Series:
    """Realized quarticity: sum of r^4 over 21 days (4th moment of returns)."""
    r = _log_returns(close)
    return _rolling_sum(r ** 4, _TD_MON)


def jmp_080_rv4_63d(close: pd.Series) -> pd.Series:
    """Realized quarticity over 63 days."""
    r = _log_returns(close)
    return _rolling_sum(r ** 4, _TD_QTR)


def jmp_081_rv_skewness_21d(close: pd.Series) -> pd.Series:
    """Signed skewness of squared returns over 21 days (jump asymmetry measure)."""
    r = _log_returns(close)
    r2 = r ** 2
    m3 = _rolling_mean((r2 - _rolling_mean(r2, _TD_MON)) ** 3, _TD_MON)
    s3 = _rolling_std(r2, _TD_MON) ** 3
    return _safe_div(m3, s3.clip(lower=_EPS))


def jmp_082_rv3_signed_21d(close: pd.Series) -> pd.Series:
    """Signed realized third moment: sum(r^3) over 21 days (captures directional jumps)."""
    r = _log_returns(close)
    return _rolling_sum(r ** 3, _TD_MON)


def jmp_083_rv3_signed_63d(close: pd.Series) -> pd.Series:
    """Signed realized third moment over 63 days."""
    r = _log_returns(close)
    return _rolling_sum(r ** 3, _TD_QTR)


def jmp_084_max_squared_return_21d(close: pd.Series) -> pd.Series:
    """Max squared daily return over 21 days (proxy for dominant jump contribution)."""
    r = _log_returns(close)
    return (r ** 2).rolling(_TD_MON, min_periods=1).max()


def jmp_085_max_squared_return_63d(close: pd.Series) -> pd.Series:
    """Max squared daily return over 63 days."""
    r = _log_returns(close)
    return (r ** 2).rolling(_TD_QTR, min_periods=1).max()


# --- Group I (086-095): Volume-Jump Interaction ---

def jmp_086_volume_on_jump_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on 3-sigma jump days over trailing 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    vol_on_jump = volume * flag
    count = _rolling_sum(flag, _TD_MON).clip(lower=_EPS)
    return _safe_div(_rolling_sum(vol_on_jump, _TD_MON), count)


def jmp_087_volume_on_neg_jump_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on negative 3-sigma jump days over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    vol_on_jump = volume * flag
    count = _rolling_sum(flag, _TD_MON).clip(lower=_EPS)
    return _safe_div(_rolling_sum(vol_on_jump, _TD_MON), count)


def jmp_088_volume_jump_day_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on jump days vs avg volume over 21 days (jump panic indicator)."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_on_jump = (volume * flag).where(flag > 0.5)
    avg_jump_vol = _rolling_mean(vol_on_jump.fillna(0.0), _TD_MON) + _EPS
    return _safe_div(avg_jump_vol, avg_vol.clip(lower=_EPS))


def jmp_089_dollar_volume_on_jump_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume (close * volume) on 3-sigma jump days over 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    dv = close * volume * flag
    return _rolling_sum(dv, _TD_MON)


def jmp_090_jump_volume_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total volume occurring on 3-sigma jump days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    jump_vol = _rolling_sum(volume * flag, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(jump_vol, total_vol.clip(lower=_EPS))


def jmp_091_neg_jump_volume_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day volume on negative 3-sigma jump days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    jump_vol = _rolling_sum(volume * flag, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(jump_vol, total_vol.clip(lower=_EPS))


def jmp_092_volume_zscore_on_jump_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume z-score on 3-sigma jump days over 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    vol_m = _rolling_mean(volume, _TD_YEAR)
    vol_s = _rolling_std(volume, _TD_YEAR)
    vol_z = _safe_div(volume - vol_m, vol_s.clip(lower=_EPS))
    return _rolling_mean(vol_z * flag, _TD_MON)


def jmp_093_neg_jump_volume_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume on negative 3-sigma jump days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    jump_vol = _rolling_sum(volume * flag, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(jump_vol, total_vol.clip(lower=_EPS))


def jmp_094_volume_jump_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume on any 3-sigma jump days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    jump_vol = _rolling_sum(volume * flag, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(jump_vol, total_vol.clip(lower=_EPS))


def jmp_095_high_vol_neg_jump_conc_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: negative jump AND above-median volume on same day, count in 21d."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    neg_flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    vol_median = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > vol_median).astype(float)
    return _rolling_sum(neg_flag * high_vol, _TD_MON)


# --- Group J (096-105): HLOC-based Jump Proxies ---

def jmp_096_intraday_range_5d_sum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of log(high/low) over 5 days (intraday range proxy for jump activity)."""
    hl = _hl_jump_proxy(high, low, close)
    return _rolling_sum(hl, _TD_WEEK)


def jmp_097_intraday_range_21d_sum(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of log(high/low) over 21 days."""
    hl = _hl_jump_proxy(high, low, close)
    return _rolling_sum(hl, _TD_MON)


def jmp_098_hl_vs_rv_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of intraday range sum to log-return RV over 21 days (intra vs inter-period)."""
    hl = _hl_jump_proxy(high, low, close)
    hl_sum = _rolling_sum(hl ** 2, _TD_MON)
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(hl_sum, rv.clip(lower=_EPS))


def jmp_099_open_close_gap_variance_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of open-to-close log returns over 21 days."""
    oc = np.log((close / open.replace(0, np.nan)).clip(lower=_EPS))
    return _realized_variance(oc, _TD_MON)


def jmp_100_open_close_gap_jump_count_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with |open-to-close log return| > 3*std(21d) over 21 days."""
    oc = np.log((close / open.replace(0, np.nan)).clip(lower=_EPS))
    sigma = _rolling_std(oc, _TD_MON)
    flag = (oc.abs() > 3.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_101_high_vs_prev_close_jump_21d(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days where high > prev_close * 1.05 (upside gap + spike) in 21 days."""
    flag = (high > close.shift(1) * 1.05).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_102_low_vs_prev_close_jump_21d(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days where low < prev_close * 0.95 (downside spike) in 21 days."""
    flag = (low < close.shift(1) * 0.95).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_103_tail_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 95th to 5th percentile of |log returns| over 21 days (tail heaviness)."""
    r = _log_returns(close).abs()
    p95 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.95)
    p5 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    return _safe_div(p95, p5.clip(lower=_EPS))


def jmp_104_tail_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of 95th to 5th percentile of |log returns| over 63 days."""
    r = _log_returns(close).abs()
    p95 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.95)
    p5 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)
    return _safe_div(p95, p5.clip(lower=_EPS))


def jmp_105_hl_range_max_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum single-day log(high/low) over 21 days (peak intraday jump)."""
    hl = _hl_jump_proxy(high, low, close)
    return hl.rolling(_TD_MON, min_periods=1).max()


# --- Group K (106-115): Normalized Jump Indicators and Ratios ---

def jmp_106_jv_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day jump variation vs 252-day distribution."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    m = _rolling_mean(jv, _TD_YEAR)
    s = _rolling_std(jv, _TD_YEAR)
    return _safe_div(jv - m, s.clip(lower=_EPS))


def jmp_107_rv_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day RV vs 252-day distribution."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    return _safe_div(rv - m, s.clip(lower=_EPS))


def jmp_108_bpv_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day BPV vs 252-day distribution."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    m = _rolling_mean(bpv, _TD_YEAR)
    s = _rolling_std(bpv, _TD_YEAR)
    return _safe_div(bpv - m, s.clip(lower=_EPS))


def jmp_109_jump_count_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day jump count vs 252-day distribution."""
    r = _log_returns(close)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s.clip(lower=_EPS))


def jmp_110_jv_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day jump variation in trailing 252-day distribution."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    return jv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def jmp_111_rv_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day RV in trailing 252-day distribution."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return rv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def jmp_112_rv_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """All-time expanding percentile rank of 21-day RV."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return rv.expanding(min_periods=_TD_MON).rank(pct=True)


def jmp_113_jv_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """All-time expanding percentile rank of 21-day jump variation."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    return jv.expanding(min_periods=_TD_MON).rank(pct=True)


def jmp_114_rv_current_vs_min_252d(close: pd.Series) -> pd.Series:
    """Ratio of current 21-day RV to its 252-day minimum (1 = at historical low)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    mn = _rolling_min(rv, _TD_YEAR)
    return _safe_div(rv, mn.clip(lower=_EPS))


def jmp_115_rv_current_vs_max_252d(close: pd.Series) -> pd.Series:
    """Ratio of current 21-day RV to its 252-day maximum (1 = at historical spike)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    mx = _rolling_max(rv, _TD_YEAR)
    return _safe_div(rv, mx.clip(lower=_EPS))


# --- Group L (116-125): Jump Regime Indicators ---

def jmp_116_high_jump_regime_21d(close: pd.Series) -> pd.Series:
    """Binary flag: 21-day jump variation ratio > 0.3 (high jump regime)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return (ratio > 0.3).astype(float)


def jmp_117_extreme_jump_regime_21d(close: pd.Series) -> pd.Series:
    """Binary flag: 21-day jump variation ratio > 0.5 (extreme jump regime)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return (ratio > 0.5).astype(float)


def jmp_118_jump_regime_streak(close: pd.Series) -> pd.Series:
    """Consecutive days in high jump regime (JV/RV > 0.3)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return _consec_streak(ratio > 0.3)


def jmp_119_jump_regime_days_252d(close: pd.Series) -> pd.Series:
    """Count of days in high jump regime (JV/RV > 0.3) in trailing 252 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return _rolling_sum((ratio > 0.3).astype(float), _TD_YEAR)


def jmp_120_jump_ratio_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day JV/RV ratio in trailing 63-day distribution."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    return ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def jmp_121_rv_vol_ratio_5d_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day annualized RV vol to 21-day annualized RV vol (short-term spike)."""
    r = _log_returns(close)
    rv5 = _realized_variance(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)
    rv21 = _realized_variance(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    return _safe_div(rv5.clip(lower=0.0) ** 0.5, rv21.clip(lower=_EPS) ** 0.5)


def jmp_122_rv_vol_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day annualized RV vol (medium-term jump spike)."""
    r = _log_returns(close)
    rv21 = _realized_variance(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    rv63 = _realized_variance(r, _TD_QTR) * (_TD_YEAR / _TD_QTR)
    return _safe_div(rv21.clip(lower=0.0) ** 0.5, rv63.clip(lower=_EPS) ** 0.5)


def jmp_123_neg_jump_count_rolling_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day negative 3-sigma jump count vs 252-day distribution."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    m = _rolling_mean(cnt, _TD_YEAR)
    s = _rolling_std(cnt, _TD_YEAR)
    return _safe_div(cnt - m, s.clip(lower=_EPS))


def jmp_124_jump_ratio_ema_21d(close: pd.Series) -> pd.Series:
    """EMA (span=21) of daily jump flags (smooth jump frequency signal)."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    return _ewm_mean(flag, _TD_MON)


def jmp_125_neg_jump_ratio_ema_21d(close: pd.Series) -> pd.Series:
    """EMA (span=21) of daily negative jump flags."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    return _ewm_mean(flag, _TD_MON)


# --- Group M (126-135): Tripower and Quad-power Variants ---

def jmp_126_tpv_21d(close: pd.Series) -> pd.Series:
    """Tripower variation over 21 days (more robust continuous var estimator).
    TPV = mu_{4/3}^{-3} * n * sum(|r_{t}|^{4/3}|r_{t-1}|^{4/3}|r_{t-2}|^{4/3}) / n."""
    import math
    mu43 = (2.0 ** (2.0 / 3.0)) * (math.gamma(7.0 / 6.0) / math.gamma(0.5))
    r = _log_returns(close)
    abs_r = r.abs()
    tp = (abs_r ** (4.0 / 3.0)) * (abs_r.shift(1) ** (4.0 / 3.0)) * (abs_r.shift(2) ** (4.0 / 3.0))
    return (mu43 ** (-3.0)) * _rolling_sum(tp, _TD_MON)


def jmp_127_tpv_63d(close: pd.Series) -> pd.Series:
    """Tripower variation over 63 days."""
    import math
    mu43 = (2.0 ** (2.0 / 3.0)) * (math.gamma(7.0 / 6.0) / math.gamma(0.5))
    r = _log_returns(close)
    abs_r = r.abs()
    tp = (abs_r ** (4.0 / 3.0)) * (abs_r.shift(1) ** (4.0 / 3.0)) * (abs_r.shift(2) ** (4.0 / 3.0))
    return (mu43 ** (-3.0)) * _rolling_sum(tp, _TD_QTR)


def jmp_128_rv_tpv_jump_ratio_21d(close: pd.Series) -> pd.Series:
    """Jump ratio using tripower: (RV - TPV) / RV over 21 days."""
    import math
    mu43 = (2.0 ** (2.0 / 3.0)) * (math.gamma(7.0 / 6.0) / math.gamma(0.5))
    r = _log_returns(close)
    abs_r = r.abs()
    tp = (abs_r ** (4.0 / 3.0)) * (abs_r.shift(1) ** (4.0 / 3.0)) * (abs_r.shift(2) ** (4.0 / 3.0))
    tpv = (mu43 ** (-3.0)) * _rolling_sum(tp, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    jv_tp = (rv - tpv).clip(lower=0.0)
    return _safe_div(jv_tp, rv.clip(lower=_EPS))


def jmp_129_quad_power_variation_21d(close: pd.Series) -> pd.Series:
    """Quad-power variation (QPV) over 21 days: mu1^{-4} * sum(|r||r-1||r-2||r-3|)."""
    mu1 = np.sqrt(2.0 / np.pi)
    r = _log_returns(close)
    abs_r = r.abs()
    qp = abs_r * abs_r.shift(1) * abs_r.shift(2) * abs_r.shift(3)
    return (mu1 ** (-4.0)) * _rolling_sum(qp, _TD_MON)


def jmp_130_rv_qpv_ratio_21d(close: pd.Series) -> pd.Series:
    """RV / QPV over 21 days (high values indicate jumps)."""
    mu1 = np.sqrt(2.0 / np.pi)
    r = _log_returns(close)
    abs_r = r.abs()
    qp = abs_r * abs_r.shift(1) * abs_r.shift(2) * abs_r.shift(3)
    qpv = (mu1 ** (-4.0)) * _rolling_sum(qp, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(rv, qpv.clip(lower=_EPS))


def jmp_131_median_return_21d(close: pd.Series) -> pd.Series:
    """Median absolute log-return over 21 days (robust volatility, insensitive to jumps)."""
    r = _log_returns(close).abs()
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()


def jmp_132_rv_median_ratio_21d(close: pd.Series) -> pd.Series:
    """RV divided by (median |return|)^2 * n over 21 days (RV inflation by jumps)."""
    r = _log_returns(close)
    abs_r = r.abs()
    med = abs_r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).median()
    rv = _realized_variance(r, _TD_MON)
    robust_var = (med ** 2) * _TD_MON
    return _safe_div(rv, robust_var.clip(lower=_EPS))


def jmp_133_rv_median_ratio_63d(close: pd.Series) -> pd.Series:
    """RV divided by (median |return|)^2 * n over 63 days."""
    r = _log_returns(close)
    abs_r = r.abs()
    med = abs_r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    rv = _realized_variance(r, _TD_QTR)
    robust_var = (med ** 2) * _TD_QTR
    return _safe_div(rv, robust_var.clip(lower=_EPS))


def jmp_134_abs_return_95th_pct_21d(close: pd.Series) -> pd.Series:
    """95th percentile of |log return| over trailing 21 days."""
    r = _log_returns(close).abs()
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.95)


def jmp_135_abs_return_99th_pct_21d(close: pd.Series) -> pd.Series:
    """99th percentile of |log return| over trailing 21 days."""
    r = _log_returns(close).abs()
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.99)


# --- Group N (136-150): Extended Lookback, EWM and Combination Features ---

def jmp_136_rv_bpv_diff_ewm21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily (r^2 - |r|*|r_{t-1}|/mu1^2) — smoothed jump contribution."""
    mu1 = np.sqrt(2.0 / np.pi)
    r = _log_returns(close)
    abs_r = r.abs()
    daily_jump_proxy = r ** 2 - (abs_r * abs_r.shift(1)) / (mu1 ** 2)
    return _ewm_mean(daily_jump_proxy, _TD_MON)


def jmp_137_rv_half_year(close: pd.Series) -> pd.Series:
    """Realized variance over trailing 126 days."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_HALF)


def jmp_138_bpv_half_year(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 126 days."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_HALF)


def jmp_139_jv_half_year(close: pd.Series) -> pd.Series:
    """Jump variation over 126 days."""
    r = _log_returns(close)
    return _jump_variation(r, _TD_HALF)


def jmp_140_jv_ratio_half_year(close: pd.Series) -> pd.Series:
    """Jump variation / RV ratio over 126 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_HALF)
    rv = _realized_variance(r, _TD_HALF)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_141_neg_jump_count_21d_ewm(close: pd.Series) -> pd.Series:
    """EWM (span=63) of 21-day negative jump count (trend in jump frequency)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return _ewm_mean(cnt, _TD_QTR)


def jmp_142_max_neg_return_expanding(close: pd.Series) -> pd.Series:
    """All-time expanding minimum log-return (absolute worst single-day crash seen)."""
    r = _log_returns(close)
    return r.expanding(min_periods=2).min()


def jmp_143_max_abs_return_expanding(close: pd.Series) -> pd.Series:
    """All-time expanding maximum absolute log-return."""
    r = _log_returns(close)
    return r.abs().expanding(min_periods=2).max()


def jmp_144_current_return_vs_max_abs_252d(close: pd.Series) -> pd.Series:
    """Today's |return| / 252-day max |return| (current jump size vs recent worst)."""
    r = _log_returns(close)
    max_abs = r.abs().rolling(_TD_YEAR, min_periods=1).max()
    return _safe_div(r.abs(), max_abs.clip(lower=_EPS))


def jmp_145_neg_rv_share_expanding(close: pd.Series) -> pd.Series:
    """Expanding fraction of total RV from negative returns (downside vol share)."""
    r = _log_returns(close)
    neg_r = r.clip(upper=0.0)
    neg_rv = (neg_r ** 2).expanding(min_periods=2).sum()
    rv = (r ** 2).expanding(min_periods=2).sum()
    return _safe_div(neg_rv, rv.clip(lower=_EPS))


def jmp_146_abs_return_ema5_vs_ema63(close: pd.Series) -> pd.Series:
    """EMA5 of |return| vs EMA63 of |return| (short vs long vol ratio)."""
    r = _log_returns(close).abs()
    ema5 = _ewm_mean(r, _TD_WEEK)
    ema63 = _ewm_mean(r, _TD_QTR)
    return _safe_div(ema5, ema63.clip(lower=_EPS))


def jmp_147_rv_short_long_ratio_5_252(close: pd.Series) -> pd.Series:
    """Ratio of 5-day RV to 252-day RV (short-term spike vs long-term baseline)."""
    r = _log_returns(close)
    rv5 = _realized_variance(r, _TD_WEEK)
    rv252 = _realized_variance(r, _TD_YEAR)
    return _safe_div(rv5 * (_TD_YEAR / _TD_WEEK), rv252.clip(lower=_EPS))


def jmp_148_jv_acceleration_21d(close: pd.Series) -> pd.Series:
    """Difference of current 21-day JV ratio and prior 21-day JV ratio (5d lag)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return ratio - ratio.shift(_TD_WEEK)


def jmp_149_neg_jv_sum_rolling_max_frac_21d(close: pd.Series) -> pd.Series:
    """21-day neg JV as fraction of its own 252-day rolling max."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    mx = _rolling_max(neg_jv, _TD_YEAR)
    return _safe_div(neg_jv, mx.clip(lower=_EPS))


def jmp_150_jump_contribution_score_21d(close: pd.Series) -> pd.Series:
    """Composite jump activity score: JV_ratio + jump_count/21 + neg_jump_frac (0-3 range)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    jv_ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0).clip(0.0, 1.0)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_MON) / _TD_MON
    sigma = _rolling_std(r, _TD_MON)
    neg_flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    pos_jv = _rolling_sum(r.where(r > 3.0 * sigma.fillna(_EPS), 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -3.0 * sigma.fillna(_EPS), 0.0) ** 2, _TD_MON)
    total_jv = (pos_jv + neg_jv).clip(lower=_EPS)
    neg_frac = _safe_div(neg_jv, total_jv).fillna(0.5)
    return jv_ratio + cnt + neg_frac


# ── Registry ──────────────────────────────────────────────────────────────────

JUMP_DISCONTINUITY_REGISTRY_076_150 = {
    "jmp_076_rv_bpv_ratio_252d": {"inputs": ["close"], "func": jmp_076_rv_bpv_ratio_252d},
    "jmp_077_jump_test_stat_21d": {"inputs": ["close"], "func": jmp_077_jump_test_stat_21d},
    "jmp_078_jump_test_stat_63d": {"inputs": ["close"], "func": jmp_078_jump_test_stat_63d},
    "jmp_079_rv4_21d": {"inputs": ["close"], "func": jmp_079_rv4_21d},
    "jmp_080_rv4_63d": {"inputs": ["close"], "func": jmp_080_rv4_63d},
    "jmp_081_rv_skewness_21d": {"inputs": ["close"], "func": jmp_081_rv_skewness_21d},
    "jmp_082_rv3_signed_21d": {"inputs": ["close"], "func": jmp_082_rv3_signed_21d},
    "jmp_083_rv3_signed_63d": {"inputs": ["close"], "func": jmp_083_rv3_signed_63d},
    "jmp_084_max_squared_return_21d": {"inputs": ["close"], "func": jmp_084_max_squared_return_21d},
    "jmp_085_max_squared_return_63d": {"inputs": ["close"], "func": jmp_085_max_squared_return_63d},
    "jmp_086_volume_on_jump_days_21d": {"inputs": ["close", "volume"], "func": jmp_086_volume_on_jump_days_21d},
    "jmp_087_volume_on_neg_jump_days_21d": {"inputs": ["close", "volume"], "func": jmp_087_volume_on_neg_jump_days_21d},
    "jmp_088_volume_jump_day_ratio_21d": {"inputs": ["close", "volume"], "func": jmp_088_volume_jump_day_ratio_21d},
    "jmp_089_dollar_volume_on_jump_21d": {"inputs": ["close", "volume"], "func": jmp_089_dollar_volume_on_jump_21d},
    "jmp_090_jump_volume_frac_21d": {"inputs": ["close", "volume"], "func": jmp_090_jump_volume_frac_21d},
    "jmp_091_neg_jump_volume_frac_21d": {"inputs": ["close", "volume"], "func": jmp_091_neg_jump_volume_frac_21d},
    "jmp_092_volume_zscore_on_jump_21d": {"inputs": ["close", "volume"], "func": jmp_092_volume_zscore_on_jump_21d},
    "jmp_093_neg_jump_volume_frac_63d": {"inputs": ["close", "volume"], "func": jmp_093_neg_jump_volume_frac_63d},
    "jmp_094_volume_jump_frac_63d": {"inputs": ["close", "volume"], "func": jmp_094_volume_jump_frac_63d},
    "jmp_095_high_vol_neg_jump_conc_21d": {"inputs": ["close", "volume"], "func": jmp_095_high_vol_neg_jump_conc_21d},
    "jmp_096_intraday_range_5d_sum": {"inputs": ["high", "low", "close"], "func": jmp_096_intraday_range_5d_sum},
    "jmp_097_intraday_range_21d_sum": {"inputs": ["high", "low", "close"], "func": jmp_097_intraday_range_21d_sum},
    "jmp_098_hl_vs_rv_ratio_21d": {"inputs": ["high", "low", "close"], "func": jmp_098_hl_vs_rv_ratio_21d},
    "jmp_099_open_close_gap_variance_21d": {"inputs": ["open", "close"], "func": jmp_099_open_close_gap_variance_21d},
    "jmp_100_open_close_gap_jump_count_21d": {"inputs": ["open", "close"], "func": jmp_100_open_close_gap_jump_count_21d},
    "jmp_101_high_vs_prev_close_jump_21d": {"inputs": ["high", "close"], "func": jmp_101_high_vs_prev_close_jump_21d},
    "jmp_102_low_vs_prev_close_jump_21d": {"inputs": ["low", "close"], "func": jmp_102_low_vs_prev_close_jump_21d},
    "jmp_103_tail_ratio_21d": {"inputs": ["close"], "func": jmp_103_tail_ratio_21d},
    "jmp_104_tail_ratio_63d": {"inputs": ["close"], "func": jmp_104_tail_ratio_63d},
    "jmp_105_hl_range_max_21d": {"inputs": ["high", "low", "close"], "func": jmp_105_hl_range_max_21d},
    "jmp_106_jv_zscore_252d": {"inputs": ["close"], "func": jmp_106_jv_zscore_252d},
    "jmp_107_rv_zscore_252d": {"inputs": ["close"], "func": jmp_107_rv_zscore_252d},
    "jmp_108_bpv_zscore_252d": {"inputs": ["close"], "func": jmp_108_bpv_zscore_252d},
    "jmp_109_jump_count_zscore_252d": {"inputs": ["close"], "func": jmp_109_jump_count_zscore_252d},
    "jmp_110_jv_pct_rank_252d": {"inputs": ["close"], "func": jmp_110_jv_pct_rank_252d},
    "jmp_111_rv_pct_rank_252d": {"inputs": ["close"], "func": jmp_111_rv_pct_rank_252d},
    "jmp_112_rv_expanding_pct_rank": {"inputs": ["close"], "func": jmp_112_rv_expanding_pct_rank},
    "jmp_113_jv_expanding_pct_rank": {"inputs": ["close"], "func": jmp_113_jv_expanding_pct_rank},
    "jmp_114_rv_current_vs_min_252d": {"inputs": ["close"], "func": jmp_114_rv_current_vs_min_252d},
    "jmp_115_rv_current_vs_max_252d": {"inputs": ["close"], "func": jmp_115_rv_current_vs_max_252d},
    "jmp_116_high_jump_regime_21d": {"inputs": ["close"], "func": jmp_116_high_jump_regime_21d},
    "jmp_117_extreme_jump_regime_21d": {"inputs": ["close"], "func": jmp_117_extreme_jump_regime_21d},
    "jmp_118_jump_regime_streak": {"inputs": ["close"], "func": jmp_118_jump_regime_streak},
    "jmp_119_jump_regime_days_252d": {"inputs": ["close"], "func": jmp_119_jump_regime_days_252d},
    "jmp_120_jump_ratio_pct_rank_63d": {"inputs": ["close"], "func": jmp_120_jump_ratio_pct_rank_63d},
    "jmp_121_rv_vol_ratio_5d_21d": {"inputs": ["close"], "func": jmp_121_rv_vol_ratio_5d_21d},
    "jmp_122_rv_vol_ratio_21d_63d": {"inputs": ["close"], "func": jmp_122_rv_vol_ratio_21d_63d},
    "jmp_123_neg_jump_count_rolling_zscore": {"inputs": ["close"], "func": jmp_123_neg_jump_count_rolling_zscore},
    "jmp_124_jump_ratio_ema_21d": {"inputs": ["close"], "func": jmp_124_jump_ratio_ema_21d},
    "jmp_125_neg_jump_ratio_ema_21d": {"inputs": ["close"], "func": jmp_125_neg_jump_ratio_ema_21d},
    "jmp_126_tpv_21d": {"inputs": ["close"], "func": jmp_126_tpv_21d},
    "jmp_127_tpv_63d": {"inputs": ["close"], "func": jmp_127_tpv_63d},
    "jmp_128_rv_tpv_jump_ratio_21d": {"inputs": ["close"], "func": jmp_128_rv_tpv_jump_ratio_21d},
    "jmp_129_quad_power_variation_21d": {"inputs": ["close"], "func": jmp_129_quad_power_variation_21d},
    "jmp_130_rv_qpv_ratio_21d": {"inputs": ["close"], "func": jmp_130_rv_qpv_ratio_21d},
    "jmp_131_median_return_21d": {"inputs": ["close"], "func": jmp_131_median_return_21d},
    "jmp_132_rv_median_ratio_21d": {"inputs": ["close"], "func": jmp_132_rv_median_ratio_21d},
    "jmp_133_rv_median_ratio_63d": {"inputs": ["close"], "func": jmp_133_rv_median_ratio_63d},
    "jmp_134_abs_return_95th_pct_21d": {"inputs": ["close"], "func": jmp_134_abs_return_95th_pct_21d},
    "jmp_135_abs_return_99th_pct_21d": {"inputs": ["close"], "func": jmp_135_abs_return_99th_pct_21d},
    "jmp_136_rv_bpv_diff_ewm21": {"inputs": ["close"], "func": jmp_136_rv_bpv_diff_ewm21},
    "jmp_137_rv_half_year": {"inputs": ["close"], "func": jmp_137_rv_half_year},
    "jmp_138_bpv_half_year": {"inputs": ["close"], "func": jmp_138_bpv_half_year},
    "jmp_139_jv_half_year": {"inputs": ["close"], "func": jmp_139_jv_half_year},
    "jmp_140_jv_ratio_half_year": {"inputs": ["close"], "func": jmp_140_jv_ratio_half_year},
    "jmp_141_neg_jump_count_21d_ewm": {"inputs": ["close"], "func": jmp_141_neg_jump_count_21d_ewm},
    "jmp_142_max_neg_return_expanding": {"inputs": ["close"], "func": jmp_142_max_neg_return_expanding},
    "jmp_143_max_abs_return_expanding": {"inputs": ["close"], "func": jmp_143_max_abs_return_expanding},
    "jmp_144_current_return_vs_max_abs_252d": {"inputs": ["close"], "func": jmp_144_current_return_vs_max_abs_252d},
    "jmp_145_neg_rv_share_expanding": {"inputs": ["close"], "func": jmp_145_neg_rv_share_expanding},
    "jmp_146_abs_return_ema5_vs_ema63": {"inputs": ["close"], "func": jmp_146_abs_return_ema5_vs_ema63},
    "jmp_147_rv_short_long_ratio_5_252": {"inputs": ["close"], "func": jmp_147_rv_short_long_ratio_5_252},
    "jmp_148_jv_acceleration_21d": {"inputs": ["close"], "func": jmp_148_jv_acceleration_21d},
    "jmp_149_neg_jv_sum_rolling_max_frac_21d": {"inputs": ["close"], "func": jmp_149_neg_jv_sum_rolling_max_frac_21d},
    "jmp_150_jump_contribution_score_21d": {"inputs": ["close"], "func": jmp_150_jump_contribution_score_21d},
}
