"""
111_jump_discontinuity — Extended Features 001-075
Domain: price jump discontinuities — deeper variants of bipower/jump statistics,
        multi-threshold jump detection, HLOC jump proxies, volume-weighted variants,
        cross-lookback comparisons, tail-risk indicators, conditional jump features
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
    """Rolling bipower variation over w days."""
    mu1 = np.sqrt(2.0 / np.pi)
    abs_r = r.abs()
    bp = abs_r * abs_r.shift(1)
    return (1.0 / (mu1 ** 2)) * _rolling_sum(bp, w)


def _jump_variation(r: pd.Series, w: int) -> pd.Series:
    """Jump variation = max(RV - BPV, 0)."""
    rv = _realized_variance(r, w)
    bpv = _bipower_variation(r, w)
    return (rv - bpv).clip(lower=0.0)


def _jump_flag(r: pd.Series, threshold_sigma: float = 3.0, window: int = _TD_MON) -> pd.Series:
    """Binary flag: |return| > threshold_sigma * rolling std over window."""
    sigma = _rolling_std(r, window)
    return (r.abs() > threshold_sigma * sigma.fillna(_EPS)).astype(float)


def _hl_log_range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log(high/low) as intraday range proxy."""
    return np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Multi-threshold Jump Detection Variants ---

def jmp_ext_001_jump_count_1p5sigma_21d(close: pd.Series) -> pd.Series:
    """Count of 1.5-sigma jumps in 21 days (lower threshold, more sensitive)."""
    r = _log_returns(close)
    return _rolling_sum(_jump_flag(r, 1.5), _TD_MON)


def jmp_ext_002_jump_count_2p5sigma_21d(close: pd.Series) -> pd.Series:
    """Count of 2.5-sigma jumps in 21 days."""
    r = _log_returns(close)
    return _rolling_sum(_jump_flag(r, 2.5), _TD_MON)


def jmp_ext_003_jump_count_5sigma_21d(close: pd.Series) -> pd.Series:
    """Count of 5-sigma extreme jumps in 21 days (catastrophic events)."""
    r = _log_returns(close)
    return _rolling_sum(_jump_flag(r, 5.0), _TD_MON)


def jmp_ext_004_jump_count_3sigma_5d(close: pd.Series) -> pd.Series:
    """Count of 3-sigma jumps in 5 days (very recent jump clustering)."""
    r = _log_returns(close)
    return _rolling_sum(_jump_flag(r, 3.0), _TD_WEEK)


def jmp_ext_005_neg_jump_count_2sigma_21d(close: pd.Series) -> pd.Series:
    """Count of negative 2-sigma jumps in 21 days (broadened crash detection)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -2.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_ext_006_neg_jump_count_4sigma_63d(close: pd.Series) -> pd.Series:
    """Count of negative 4-sigma jumps in 63 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -4.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def jmp_ext_007_neg_jump_count_5sigma_252d(close: pd.Series) -> pd.Series:
    """Count of negative 5-sigma jumps in 252 days (rare crash events in history)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -5.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def jmp_ext_008_jump_count_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day jump count to 252-day jump count (recent vs historical pace)."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    cnt63 = _rolling_sum(flag, _TD_QTR)
    cnt252 = _rolling_sum(flag, _TD_YEAR)
    return _safe_div(cnt63 * (_TD_YEAR / _TD_QTR), cnt252.clip(lower=_EPS))


def jmp_ext_009_jump_flag_3sigma_63d_std(close: pd.Series) -> pd.Series:
    """Std dev of 21-day jump counts measured over 63 days (consistency of jump activity)."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    cnt21 = _rolling_sum(flag, _TD_MON)
    return _rolling_std(cnt21, _TD_QTR)


def jmp_ext_010_neg_jump_intensity_sum_252d(close: pd.Series) -> pd.Series:
    """Sum of |negative jump returns| over 252 days (cumulative crash severity)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    neg_flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(r.abs() * neg_flag, _TD_YEAR)


# --- Group B (011-020): Bipower Variation — Deeper Variants ---

def jmp_ext_011_bpv_5d_annualized(close: pd.Series) -> pd.Series:
    """Annualized BPV over 5 days * (252/5)."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)


def jmp_ext_012_bpv_vs_rv_5d_ratio(close: pd.Series) -> pd.Series:
    """BPV / RV over 5 days (fraction of short-term variance that is continuous)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_WEEK)
    rv = _realized_variance(r, _TD_WEEK)
    return _safe_div(bpv, rv.clip(lower=_EPS))


def jmp_ext_013_bpv_expanding_min(close: pd.Series) -> pd.Series:
    """All-time expanding minimum of 21-day BPV."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    return bpv.expanding(min_periods=_TD_MON).min()


def jmp_ext_014_bpv_current_vs_expanding_mean(close: pd.Series) -> pd.Series:
    """21-day BPV as fraction of its all-time expanding mean."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    exp_mean = bpv.expanding(min_periods=_TD_MON).mean()
    return _safe_div(bpv, exp_mean.clip(lower=_EPS))


def jmp_ext_015_rv_minus_bpv_ewm21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily (RV - BPV) one-period proxy."""
    mu1 = np.sqrt(2.0 / np.pi)
    r = _log_returns(close)
    abs_r = r.abs()
    # Daily approximation: r^2 vs |r|*|r_{t-1}|/mu1^2
    bp_proxy = (abs_r * abs_r.shift(1)) / (mu1 ** 2)
    return _ewm_mean(r ** 2 - bp_proxy, _TD_MON)


def jmp_ext_016_bpv_ratio_short_long_5_63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day BPV (ann) to 63-day BPV (ann)."""
    r = _log_returns(close)
    bpv5 = _bipower_variation(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)
    bpv63 = _bipower_variation(r, _TD_QTR) * (_TD_YEAR / _TD_QTR)
    return _safe_div(bpv5, bpv63.clip(lower=_EPS))


def jmp_ext_017_jv_ratio_5d(close: pd.Series) -> pd.Series:
    """Jump variation / RV over 5 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_WEEK)
    rv = _realized_variance(r, _TD_WEEK)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_ext_018_jv_ratio_126d(close: pd.Series) -> pd.Series:
    """Jump variation / RV over 126 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_HALF)
    rv = _realized_variance(r, _TD_HALF)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_ext_019_bpv_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day BPV in trailing 252-day distribution."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    return bpv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def jmp_ext_020_rv_bpv_diff_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of (RV - BPV) in 252-day distribution."""
    r = _log_returns(close)
    diff = _realized_variance(r, _TD_MON) - _bipower_variation(r, _TD_MON)
    return diff.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (021-030): HLOC-based Extended Variants ---

def jmp_ext_021_hl_range_variance_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of log(high/low) over 21 days (intraday range dispersion)."""
    hl = _hl_log_range(high, low)
    return _rolling_std(hl, _TD_MON) ** 2


def jmp_ext_022_hl_range_max_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum log(high/low) over 63 days (peak intraday jump in quarter)."""
    hl = _hl_log_range(high, low)
    return hl.rolling(_TD_QTR, min_periods=1).max()


def jmp_ext_023_hl_range_ratio_5d_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean log(h/l) over 5d vs 63d (short vs long intraday range ratio)."""
    hl = _hl_log_range(high, low)
    mean5 = _rolling_mean(hl, _TD_WEEK)
    mean63 = _rolling_mean(hl, _TD_QTR)
    return _safe_div(mean5, mean63.clip(lower=_EPS))


def jmp_ext_024_hl_range_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of log(h/l) in 252-day distribution."""
    hl = _hl_log_range(high, low)
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def jmp_ext_025_hl_extreme_days_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with log(h/l) > 2*std(63d) in 21 days."""
    hl = _hl_log_range(high, low)
    thresh = 2.0 * _rolling_std(hl, _TD_QTR)
    flag = (hl > thresh.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_ext_026_gap_down_return_sum_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of negative gap-open returns (prev_close to open) over 21 days."""
    gap = np.log((open / close.shift(1).replace(0, np.nan)).clip(lower=_EPS))
    neg_gap = gap.clip(upper=0.0)
    return _rolling_sum(neg_gap, _TD_MON)


def jmp_ext_027_gap_down_variance_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Variance of negative open gaps over 21 days."""
    gap = np.log((open / close.shift(1).replace(0, np.nan)).clip(lower=_EPS))
    neg_gap = gap.where(gap < 0.0, 0.0)
    return _rolling_sum(neg_gap ** 2, _TD_MON)


def jmp_ext_028_gap_down_count_3pct_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with open-gap < -3% in 21 days."""
    gap_pct = (open / close.shift(1).replace(0, np.nan)).fillna(1.0) - 1.0
    flag = (gap_pct < -0.03).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_ext_029_intraday_recovery_ratio_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of intraday range recovered by close over 21 days: (close-low)/(high-low)."""
    hl = (high - low).replace(0, np.nan)
    recovery = _safe_div(close - low, hl)
    return _rolling_mean(recovery, _TD_MON)


def jmp_ext_030_open_gap_jump_count_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days with |open gap| > 2% in 21 days."""
    gap_pct = ((open / close.shift(1).replace(0, np.nan)).fillna(1.0) - 1.0).abs()
    flag = (gap_pct > 0.02).astype(float)
    return _rolling_sum(flag, _TD_MON)


# --- Group D (031-040): Volume-Weighted Jump Features ---

def jmp_ext_031_vw_neg_jv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted negative jump variation over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jumps = r.where(r < -thresh, 0.0)
    vol_weight = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return _rolling_sum((neg_jumps ** 2) * vol_weight, _TD_MON)


def jmp_ext_032_vw_jump_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted count of jump days in 21d (high-volume jumps count more)."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    vol_weight = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return _rolling_sum(flag * vol_weight, _TD_MON)


def jmp_ext_033_vw_pos_jv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted positive jump variation over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jumps = r.where(r > thresh, 0.0)
    vol_weight = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    return _rolling_sum((pos_jumps ** 2) * vol_weight, _TD_MON)


def jmp_ext_034_vw_signed_jv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted signed jump variation (neg - pos) over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jumps = r.where(r > thresh, 0.0)
    neg_jumps = r.where(r < -thresh, 0.0)
    vol_weight = _safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    pos_jv = _rolling_sum((pos_jumps ** 2) * vol_weight, _TD_MON)
    neg_jv = _rolling_sum((neg_jumps ** 2) * vol_weight, _TD_MON)
    return neg_jv - pos_jv


def jmp_ext_035_dv_on_neg_jump_vs_normal_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume on negative 3-sigma days / dollar volume on non-jump days, 21d."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    neg_flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    non_jump = (1.0 - neg_flag)
    dv = close * volume
    dv_jump = _rolling_sum(dv * neg_flag, _TD_MON)
    dv_normal = _rolling_sum(dv * non_jump, _TD_MON)
    return _safe_div(dv_jump, dv_normal.clip(lower=_EPS))


def jmp_ext_036_volume_spike_on_any_jump_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume spike ratio (vol/avg_vol) on 3-sigma jump days in 21d."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    spike = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return _rolling_mean(spike * flag, _TD_MON)


def jmp_ext_037_high_vol_jump_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with jump AND volume > 2x average in 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > 2.0 * avg_vol.fillna(_EPS)).astype(float)
    return _rolling_sum(flag * high_vol, _TD_MON)


def jmp_ext_038_neg_jump_volume_vs_rv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative jump day volume / RV(21d) — panic-volume per unit variance."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    neg_flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    neg_vol = _rolling_sum(volume * neg_flag, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(neg_vol, rv.clip(lower=_EPS))


def jmp_ext_039_volume_intensity_jump_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on 3-sigma jump days over 63 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    return _rolling_sum(volume * flag, _TD_QTR)


def jmp_ext_040_neg_vol_jump_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day neg-jump volume fraction in 252-day distribution."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    neg_flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    jump_vol = _rolling_sum(volume * neg_flag, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    ratio = _safe_div(jump_vol, total_vol.clip(lower=_EPS)).fillna(0.0)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): Tail Risk and Extreme Return Statistics ---

def jmp_ext_041_var95_21d(close: pd.Series) -> pd.Series:
    """Value-at-Risk (5th pct of log returns) over 21 days (left tail)."""
    r = _log_returns(close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)


def jmp_ext_042_var99_21d(close: pd.Series) -> pd.Series:
    """1% VaR (1st pct of log returns) over 21 days."""
    r = _log_returns(close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.01)


def jmp_ext_043_var95_63d(close: pd.Series) -> pd.Series:
    """5% VaR over 63 days."""
    r = _log_returns(close)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.05)


def jmp_ext_044_expected_shortfall_95_21d(close: pd.Series) -> pd.Series:
    """Expected shortfall (mean of returns below 5th pct) over 21 days."""
    r = _log_returns(close)
    q05 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.05)
    tail = r.where(r <= q05, np.nan)
    return _rolling_mean(tail, _TD_MON)


def jmp_ext_045_expected_shortfall_99_21d(close: pd.Series) -> pd.Series:
    """Expected shortfall (mean of returns below 1st pct) over 21 days."""
    r = _log_returns(close)
    q01 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.01)
    tail = r.where(r <= q01, np.nan)
    return _rolling_mean(tail, _TD_MON)


def jmp_ext_046_kurtosis_21d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of log returns over 21 days (fat tail indicator)."""
    r = _log_returns(close)
    m2 = _rolling_mean((r - _rolling_mean(r, _TD_MON)) ** 2, _TD_MON)
    m4 = _rolling_mean((r - _rolling_mean(r, _TD_MON)) ** 4, _TD_MON)
    kurt = _safe_div(m4, m2.clip(lower=_EPS) ** 2) - 3.0
    return kurt


def jmp_ext_047_kurtosis_63d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of log returns over 63 days."""
    r = _log_returns(close)
    m2 = _rolling_mean((r - _rolling_mean(r, _TD_QTR)) ** 2, _TD_QTR)
    m4 = _rolling_mean((r - _rolling_mean(r, _TD_QTR)) ** 4, _TD_QTR)
    kurt = _safe_div(m4, m2.clip(lower=_EPS) ** 2) - 3.0
    return kurt


def jmp_ext_048_skewness_21d(close: pd.Series) -> pd.Series:
    """Skewness of log returns over 21 days (negative = left-skewed crash potential)."""
    r = _log_returns(close)
    m = _rolling_mean(r, _TD_MON)
    m3 = _rolling_mean((r - m) ** 3, _TD_MON)
    m2 = _rolling_mean((r - m) ** 2, _TD_MON)
    return _safe_div(m3, m2.clip(lower=_EPS) ** 1.5)


def jmp_ext_049_skewness_63d(close: pd.Series) -> pd.Series:
    """Skewness of log returns over 63 days."""
    r = _log_returns(close)
    m = _rolling_mean(r, _TD_QTR)
    m3 = _rolling_mean((r - m) ** 3, _TD_QTR)
    m2 = _rolling_mean((r - m) ** 2, _TD_QTR)
    return _safe_div(m3, m2.clip(lower=_EPS) ** 1.5)


def jmp_ext_050_downside_semivariance_21d(close: pd.Series) -> pd.Series:
    """Semivariance of negative returns over 21 days (pure downside risk)."""
    r = _log_returns(close)
    neg_r = r.clip(upper=0.0)
    return _rolling_sum(neg_r ** 2, _TD_MON)


# --- Group F (051-060): Jump Ratio Cross-Lookback Comparisons ---

def jmp_ext_051_jv_ratio_5d_vs_252d(close: pd.Series) -> pd.Series:
    """5-day JV/RV ratio minus 252-day JV/RV ratio (recent vs historical jump regime)."""
    r = _log_returns(close)
    jv5 = _jump_variation(r, _TD_WEEK)
    rv5 = _realized_variance(r, _TD_WEEK)
    jv252 = _jump_variation(r, _TD_YEAR)
    rv252 = _realized_variance(r, _TD_YEAR)
    ratio5 = _safe_div(jv5, rv5.clip(lower=_EPS)).fillna(0.0)
    ratio252 = _safe_div(jv252, rv252.clip(lower=_EPS)).fillna(0.0)
    return ratio5 - ratio252


def jmp_ext_052_jv_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """21-day JV/RV ratio minus 252-day JV/RV ratio."""
    r = _log_returns(close)
    jv21 = _jump_variation(r, _TD_MON)
    rv21 = _realized_variance(r, _TD_MON)
    jv252 = _jump_variation(r, _TD_YEAR)
    rv252 = _realized_variance(r, _TD_YEAR)
    ratio21 = _safe_div(jv21, rv21.clip(lower=_EPS)).fillna(0.0)
    ratio252 = _safe_div(jv252, rv252.clip(lower=_EPS)).fillna(0.0)
    return ratio21 - ratio252


def jmp_ext_053_rv_vol_5d_vs_252d_spread(close: pd.Series) -> pd.Series:
    """Annualized 5-day RV vol minus annualized 252-day RV vol (short-term vol premium)."""
    r = _log_returns(close)
    rvol5 = (_realized_variance(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)).clip(lower=0.0) ** 0.5
    rvol252 = (_realized_variance(r, _TD_YEAR)).clip(lower=0.0) ** 0.5 * (_TD_YEAR / _TD_YEAR) ** 0.5
    return rvol5 - rvol252


def jmp_ext_054_jv_ratio_21d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day JV/RV ratio vs expanding history."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    exp_mean = ratio.expanding(min_periods=_TD_MON).mean()
    exp_std = ratio.expanding(min_periods=_TD_MON).std()
    return _safe_div(ratio - exp_mean, exp_std.clip(lower=_EPS))


def jmp_ext_055_rv_21d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day RV vs expanding history."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    exp_mean = rv.expanding(min_periods=_TD_MON).mean()
    exp_std = rv.expanding(min_periods=_TD_MON).std()
    return _safe_div(rv - exp_mean, exp_std.clip(lower=_EPS))


def jmp_ext_056_bpv_21d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 21-day BPV vs expanding history."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    exp_mean = bpv.expanding(min_periods=_TD_MON).mean()
    exp_std = bpv.expanding(min_periods=_TD_MON).std()
    return _safe_div(bpv - exp_mean, exp_std.clip(lower=_EPS))


def jmp_ext_057_jump_count_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day jump count in 252-day distribution."""
    r = _log_returns(close)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_MON)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def jmp_ext_058_neg_jump_count_63d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Z-score of 63-day negative jump count vs expanding history."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_QTR)
    exp_mean = cnt.expanding(min_periods=_TD_QTR).mean()
    exp_std = cnt.expanding(min_periods=_TD_QTR).std()
    return _safe_div(cnt - exp_mean, exp_std.clip(lower=_EPS))


def jmp_ext_059_max_neg_return_vs_rv21_ratio(close: pd.Series) -> pd.Series:
    """Max |negative return| / sqrt(21d RV) — largest crash in vol units."""
    r = _log_returns(close)
    max_neg = r.rolling(_TD_MON, min_periods=1).min().abs()
    rv_vol = _realized_variance(r, _TD_MON).clip(lower=_EPS) ** 0.5
    return _safe_div(max_neg, rv_vol)


def jmp_ext_060_neg_jv_252d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """252-day neg JV (annualized) divided by 21-day neg JV (annualized)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv21 = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON) * (_TD_YEAR / _TD_MON)
    neg_jv252 = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_YEAR)
    return _safe_div(neg_jv252, neg_jv21.clip(lower=_EPS))


# --- Group G (061-075): Composite and Conditional Jump Features ---

def jmp_ext_061_jump_regime_score_21d(close: pd.Series) -> pd.Series:
    """Composite: JV_ratio_21d * 3 + neg_jump_count_21d/21 + skewness_neg (0 floored)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    jv_ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0).clip(0.0, 1.0)
    sigma = _rolling_std(r, _TD_MON)
    neg_cnt = _rolling_sum((r < -3.0 * sigma.fillna(_EPS)).astype(float), _TD_MON) / _TD_MON
    m = _rolling_mean(r, _TD_MON)
    m3 = _rolling_mean((r - m) ** 3, _TD_MON)
    m2 = _rolling_mean((r - m) ** 2, _TD_MON)
    skew = _safe_div(m3, m2.clip(lower=_EPS) ** 1.5).fillna(0.0)
    neg_skew = (-skew).clip(lower=0.0)
    return jv_ratio * 3.0 + neg_cnt + neg_skew


def jmp_ext_062_consec_neg_jump_days_3sigma(close: pd.Series) -> pd.Series:
    """Consecutive days with a negative 3-sigma jump."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = r < -3.0 * sigma.fillna(_EPS)
    return _consec_streak(flag)


def jmp_ext_063_jump_calm_period_length(close: pd.Series) -> pd.Series:
    """Days since last ANY 3-sigma jump (calm period length since disruption)."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~r.isna(), np.nan)


def jmp_ext_064_rv_jump_regime_ema_cross(close: pd.Series) -> pd.Series:
    """EMA21(JV/RV ratio) minus EMA63(JV/RV ratio) — regime momentum."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    return _ewm_mean(ratio, _TD_MON) - _ewm_mean(ratio, _TD_QTR)


def jmp_ext_065_neg_jv_21d_min_252d(close: pd.Series) -> pd.Series:
    """252-day rolling minimum of 21-day negative jump variation."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    return _rolling_min(neg_jv, _TD_YEAR)


def jmp_ext_066_neg_jv_21d_max_252d(close: pd.Series) -> pd.Series:
    """252-day rolling maximum of 21-day negative jump variation (worst period)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    return _rolling_max(neg_jv, _TD_YEAR)


def jmp_ext_067_jv_ratio_ema_diff_5_21(close: pd.Series) -> pd.Series:
    """EMA5(JV_ratio) - EMA21(JV_ratio): very short vs short term jump regime."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    return _ewm_mean(ratio, _TD_WEEK) - _ewm_mean(ratio, _TD_MON)


def jmp_ext_068_rv_spike_above_2yr_avg(close: pd.Series) -> pd.Series:
    """21-day RV as multiple of its 2-year (504d) rolling average."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    avg504 = rv.rolling(504, min_periods=_TD_YEAR).mean()
    return _safe_div(rv, avg504.clip(lower=_EPS))


def jmp_ext_069_neg_jump_frac_21d_ewm_63(close: pd.Series) -> pd.Series:
    """EWM (span=63) of 21-day negative jump fraction (smoothed crash frequency trend)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    frac = _rolling_sum(flag, _TD_MON) / _TD_MON
    return _ewm_mean(frac, _TD_QTR)


def jmp_ext_070_kurtosis_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day return kurtosis in 252-day distribution."""
    r = _log_returns(close)
    m2 = _rolling_mean((r - _rolling_mean(r, _TD_MON)) ** 2, _TD_MON)
    m4 = _rolling_mean((r - _rolling_mean(r, _TD_MON)) ** 4, _TD_MON)
    kurt = _safe_div(m4, m2.clip(lower=_EPS) ** 2).fillna(3.0)
    return kurt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def jmp_ext_071_downside_sv_ratio_21d_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day downside semivariance to 63-day downside semivariance (ann)."""
    r = _log_returns(close)
    neg_r = r.clip(upper=0.0)
    sv21 = _rolling_sum(neg_r ** 2, _TD_MON) * (_TD_YEAR / _TD_MON)
    sv63 = _rolling_sum(neg_r ** 2, _TD_QTR) * (_TD_YEAR / _TD_QTR)
    return _safe_div(sv21, sv63.clip(lower=_EPS))


def jmp_ext_072_jv_ratio_21d_5d_ema_signal(close: pd.Series) -> pd.Series:
    """Binary flag: 5-day EMA of JV/RV ratio > its 21-day EMA (jump regime rising)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    return (_ewm_mean(ratio, _TD_WEEK) > _ewm_mean(ratio, _TD_MON)).astype(float)


def jmp_ext_073_neg_jv_21d_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of 21-day negative jump variation."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    exp_mean = neg_jv.expanding(min_periods=_TD_MON).mean()
    exp_std = neg_jv.expanding(min_periods=_TD_MON).std()
    return _safe_div(neg_jv - exp_mean, exp_std.clip(lower=_EPS))


def jmp_ext_074_jump_count_21d_trend_score(close: pd.Series) -> pd.Series:
    """Jump count trend: 21d count / 63d avg count (recent vs medium-term pace)."""
    r = _log_returns(close)
    flag = _jump_flag(r, 3.0)
    cnt21 = _rolling_sum(flag, _TD_MON)
    avg_cnt63 = _rolling_mean(cnt21, _TD_QTR)
    return _safe_div(cnt21, avg_cnt63.clip(lower=_EPS))


def jmp_ext_075_rv_bpv_ratio_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day RV/BPV ratio in 252-day distribution."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    ratio = _safe_div(rv, bpv.clip(lower=_EPS)).fillna(1.0)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

JUMP_DISCONTINUITY_EXTENDED_REGISTRY_001_075 = {
    "jmp_ext_001_jump_count_1p5sigma_21d": {"inputs": ["close"], "func": jmp_ext_001_jump_count_1p5sigma_21d},
    "jmp_ext_002_jump_count_2p5sigma_21d": {"inputs": ["close"], "func": jmp_ext_002_jump_count_2p5sigma_21d},
    "jmp_ext_003_jump_count_5sigma_21d": {"inputs": ["close"], "func": jmp_ext_003_jump_count_5sigma_21d},
    "jmp_ext_004_jump_count_3sigma_5d": {"inputs": ["close"], "func": jmp_ext_004_jump_count_3sigma_5d},
    "jmp_ext_005_neg_jump_count_2sigma_21d": {"inputs": ["close"], "func": jmp_ext_005_neg_jump_count_2sigma_21d},
    "jmp_ext_006_neg_jump_count_4sigma_63d": {"inputs": ["close"], "func": jmp_ext_006_neg_jump_count_4sigma_63d},
    "jmp_ext_007_neg_jump_count_5sigma_252d": {"inputs": ["close"], "func": jmp_ext_007_neg_jump_count_5sigma_252d},
    "jmp_ext_008_jump_count_63d_vs_252d_ratio": {"inputs": ["close"], "func": jmp_ext_008_jump_count_63d_vs_252d_ratio},
    "jmp_ext_009_jump_flag_3sigma_63d_std": {"inputs": ["close"], "func": jmp_ext_009_jump_flag_3sigma_63d_std},
    "jmp_ext_010_neg_jump_intensity_sum_252d": {"inputs": ["close"], "func": jmp_ext_010_neg_jump_intensity_sum_252d},
    "jmp_ext_011_bpv_5d_annualized": {"inputs": ["close"], "func": jmp_ext_011_bpv_5d_annualized},
    "jmp_ext_012_bpv_vs_rv_5d_ratio": {"inputs": ["close"], "func": jmp_ext_012_bpv_vs_rv_5d_ratio},
    "jmp_ext_013_bpv_expanding_min": {"inputs": ["close"], "func": jmp_ext_013_bpv_expanding_min},
    "jmp_ext_014_bpv_current_vs_expanding_mean": {"inputs": ["close"], "func": jmp_ext_014_bpv_current_vs_expanding_mean},
    "jmp_ext_015_rv_minus_bpv_ewm21": {"inputs": ["close"], "func": jmp_ext_015_rv_minus_bpv_ewm21},
    "jmp_ext_016_bpv_ratio_short_long_5_63": {"inputs": ["close"], "func": jmp_ext_016_bpv_ratio_short_long_5_63},
    "jmp_ext_017_jv_ratio_5d": {"inputs": ["close"], "func": jmp_ext_017_jv_ratio_5d},
    "jmp_ext_018_jv_ratio_126d": {"inputs": ["close"], "func": jmp_ext_018_jv_ratio_126d},
    "jmp_ext_019_bpv_pct_rank_252d": {"inputs": ["close"], "func": jmp_ext_019_bpv_pct_rank_252d},
    "jmp_ext_020_rv_bpv_diff_pct_rank_252d": {"inputs": ["close"], "func": jmp_ext_020_rv_bpv_diff_pct_rank_252d},
    "jmp_ext_021_hl_range_variance_21d": {"inputs": ["high", "low", "close"], "func": jmp_ext_021_hl_range_variance_21d},
    "jmp_ext_022_hl_range_max_63d": {"inputs": ["high", "low", "close"], "func": jmp_ext_022_hl_range_max_63d},
    "jmp_ext_023_hl_range_ratio_5d_63d": {"inputs": ["high", "low", "close"], "func": jmp_ext_023_hl_range_ratio_5d_63d},
    "jmp_ext_024_hl_range_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": jmp_ext_024_hl_range_pct_rank_252d},
    "jmp_ext_025_hl_extreme_days_21d": {"inputs": ["high", "low", "close"], "func": jmp_ext_025_hl_extreme_days_21d},
    "jmp_ext_026_gap_down_return_sum_21d": {"inputs": ["open", "close"], "func": jmp_ext_026_gap_down_return_sum_21d},
    "jmp_ext_027_gap_down_variance_21d": {"inputs": ["open", "close"], "func": jmp_ext_027_gap_down_variance_21d},
    "jmp_ext_028_gap_down_count_3pct_21d": {"inputs": ["open", "close"], "func": jmp_ext_028_gap_down_count_3pct_21d},
    "jmp_ext_029_intraday_recovery_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": jmp_ext_029_intraday_recovery_ratio_21d},
    "jmp_ext_030_open_gap_jump_count_21d": {"inputs": ["open", "close"], "func": jmp_ext_030_open_gap_jump_count_21d},
    "jmp_ext_031_vw_neg_jv_21d": {"inputs": ["close", "volume"], "func": jmp_ext_031_vw_neg_jv_21d},
    "jmp_ext_032_vw_jump_count_21d": {"inputs": ["close", "volume"], "func": jmp_ext_032_vw_jump_count_21d},
    "jmp_ext_033_vw_pos_jv_21d": {"inputs": ["close", "volume"], "func": jmp_ext_033_vw_pos_jv_21d},
    "jmp_ext_034_vw_signed_jv_21d": {"inputs": ["close", "volume"], "func": jmp_ext_034_vw_signed_jv_21d},
    "jmp_ext_035_dv_on_neg_jump_vs_normal_21d": {"inputs": ["close", "volume"], "func": jmp_ext_035_dv_on_neg_jump_vs_normal_21d},
    "jmp_ext_036_volume_spike_on_any_jump_21d": {"inputs": ["close", "volume"], "func": jmp_ext_036_volume_spike_on_any_jump_21d},
    "jmp_ext_037_high_vol_jump_flag_21d": {"inputs": ["close", "volume"], "func": jmp_ext_037_high_vol_jump_flag_21d},
    "jmp_ext_038_neg_jump_volume_vs_rv_21d": {"inputs": ["close", "volume"], "func": jmp_ext_038_neg_jump_volume_vs_rv_21d},
    "jmp_ext_039_volume_intensity_jump_63d": {"inputs": ["close", "volume"], "func": jmp_ext_039_volume_intensity_jump_63d},
    "jmp_ext_040_neg_vol_jump_pct_rank_252d": {"inputs": ["close", "volume"], "func": jmp_ext_040_neg_vol_jump_pct_rank_252d},
    "jmp_ext_041_var95_21d": {"inputs": ["close"], "func": jmp_ext_041_var95_21d},
    "jmp_ext_042_var99_21d": {"inputs": ["close"], "func": jmp_ext_042_var99_21d},
    "jmp_ext_043_var95_63d": {"inputs": ["close"], "func": jmp_ext_043_var95_63d},
    "jmp_ext_044_expected_shortfall_95_21d": {"inputs": ["close"], "func": jmp_ext_044_expected_shortfall_95_21d},
    "jmp_ext_045_expected_shortfall_99_21d": {"inputs": ["close"], "func": jmp_ext_045_expected_shortfall_99_21d},
    "jmp_ext_046_kurtosis_21d": {"inputs": ["close"], "func": jmp_ext_046_kurtosis_21d},
    "jmp_ext_047_kurtosis_63d": {"inputs": ["close"], "func": jmp_ext_047_kurtosis_63d},
    "jmp_ext_048_skewness_21d": {"inputs": ["close"], "func": jmp_ext_048_skewness_21d},
    "jmp_ext_049_skewness_63d": {"inputs": ["close"], "func": jmp_ext_049_skewness_63d},
    "jmp_ext_050_downside_semivariance_21d": {"inputs": ["close"], "func": jmp_ext_050_downside_semivariance_21d},
    "jmp_ext_051_jv_ratio_5d_vs_252d": {"inputs": ["close"], "func": jmp_ext_051_jv_ratio_5d_vs_252d},
    "jmp_ext_052_jv_ratio_21d_vs_252d": {"inputs": ["close"], "func": jmp_ext_052_jv_ratio_21d_vs_252d},
    "jmp_ext_053_rv_vol_5d_vs_252d_spread": {"inputs": ["close"], "func": jmp_ext_053_rv_vol_5d_vs_252d_spread},
    "jmp_ext_054_jv_ratio_21d_expanding_zscore": {"inputs": ["close"], "func": jmp_ext_054_jv_ratio_21d_expanding_zscore},
    "jmp_ext_055_rv_21d_expanding_zscore": {"inputs": ["close"], "func": jmp_ext_055_rv_21d_expanding_zscore},
    "jmp_ext_056_bpv_21d_expanding_zscore": {"inputs": ["close"], "func": jmp_ext_056_bpv_21d_expanding_zscore},
    "jmp_ext_057_jump_count_21d_pct_rank_252d": {"inputs": ["close"], "func": jmp_ext_057_jump_count_21d_pct_rank_252d},
    "jmp_ext_058_neg_jump_count_63d_expanding_zscore": {"inputs": ["close"], "func": jmp_ext_058_neg_jump_count_63d_expanding_zscore},
    "jmp_ext_059_max_neg_return_vs_rv21_ratio": {"inputs": ["close"], "func": jmp_ext_059_max_neg_return_vs_rv21_ratio},
    "jmp_ext_060_neg_jv_252d_vs_21d_ratio": {"inputs": ["close"], "func": jmp_ext_060_neg_jv_252d_vs_21d_ratio},
    "jmp_ext_061_jump_regime_score_21d": {"inputs": ["close"], "func": jmp_ext_061_jump_regime_score_21d},
    "jmp_ext_062_consec_neg_jump_days_3sigma": {"inputs": ["close"], "func": jmp_ext_062_consec_neg_jump_days_3sigma},
    "jmp_ext_063_jump_calm_period_length": {"inputs": ["close"], "func": jmp_ext_063_jump_calm_period_length},
    "jmp_ext_064_rv_jump_regime_ema_cross": {"inputs": ["close"], "func": jmp_ext_064_rv_jump_regime_ema_cross},
    "jmp_ext_065_neg_jv_21d_min_252d": {"inputs": ["close"], "func": jmp_ext_065_neg_jv_21d_min_252d},
    "jmp_ext_066_neg_jv_21d_max_252d": {"inputs": ["close"], "func": jmp_ext_066_neg_jv_21d_max_252d},
    "jmp_ext_067_jv_ratio_ema_diff_5_21": {"inputs": ["close"], "func": jmp_ext_067_jv_ratio_ema_diff_5_21},
    "jmp_ext_068_rv_spike_above_2yr_avg": {"inputs": ["close"], "func": jmp_ext_068_rv_spike_above_2yr_avg},
    "jmp_ext_069_neg_jump_frac_21d_ewm_63": {"inputs": ["close"], "func": jmp_ext_069_neg_jump_frac_21d_ewm_63},
    "jmp_ext_070_kurtosis_21d_pct_rank_252d": {"inputs": ["close"], "func": jmp_ext_070_kurtosis_21d_pct_rank_252d},
    "jmp_ext_071_downside_sv_ratio_21d_63d": {"inputs": ["close"], "func": jmp_ext_071_downside_sv_ratio_21d_63d},
    "jmp_ext_072_jv_ratio_21d_5d_ema_signal": {"inputs": ["close"], "func": jmp_ext_072_jv_ratio_21d_5d_ema_signal},
    "jmp_ext_073_neg_jv_21d_expanding_zscore": {"inputs": ["close"], "func": jmp_ext_073_neg_jv_21d_expanding_zscore},
    "jmp_ext_074_jump_count_21d_trend_score": {"inputs": ["close"], "func": jmp_ext_074_jump_count_21d_trend_score},
    "jmp_ext_075_rv_bpv_ratio_21d_pct_rank_252d": {"inputs": ["close"], "func": jmp_ext_075_rv_bpv_ratio_21d_pct_rank_252d},
}
