"""
111_jump_discontinuity — Base Features 001-075
Domain: price jump discontinuities — bipower variation vs realized variance,
        jump frequency/magnitude, signed jump variation, largest-jump statistics,
        jump-vs-diffusion ratios, jump clustering (statistical jump detection)
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
    """Rolling bipower variation: (pi/2) * sum(|r_t| * |r_{t-1}|) over w days.
    BPV is robust to jumps — it estimates the continuous component of QV."""
    mu1 = np.sqrt(2.0 / np.pi)  # E[|Z|] for Z~N(0,1)
    abs_r = r.abs()
    bp = abs_r * abs_r.shift(1)
    return (1.0 / (mu1 ** 2)) * _rolling_sum(bp, w)


def _jump_variation(r: pd.Series, w: int) -> pd.Series:
    """Jump variation = max(RV - BPV, 0): the discontinuous (jump) component."""
    rv = _realized_variance(r, w)
    bpv = _bipower_variation(r, w)
    return (rv - bpv).clip(lower=0.0)


def _jump_flag(r: pd.Series, threshold_sigma: float = 3.0) -> pd.Series:
    """Binary flag: return magnitude exceeds threshold_sigma * rolling std (21d).
    Identifies individual daily jumps using a simple threshold rule."""
    sigma = _rolling_std(r, _TD_MON)
    return (r.abs() > threshold_sigma * sigma.fillna(_EPS)).astype(float)


def _signed_jump_flag(r: pd.Series, threshold_sigma: float = 3.0) -> pd.Series:
    """Signed jump indicator: +1 for large positive, -1 for large negative, 0 otherwise."""
    sigma = _rolling_std(r, _TD_MON)
    thresh = threshold_sigma * sigma.fillna(_EPS)
    pos = (r > thresh).astype(float)
    neg = (r < -thresh).astype(float)
    return pos - neg


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Realized Variance (RV) at multiple lookbacks ---

def jmp_001_rv_5d(close: pd.Series) -> pd.Series:
    """Realized variance (sum of squared log-returns) over trailing 5 days."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_WEEK)


def jmp_002_rv_21d(close: pd.Series) -> pd.Series:
    """Realized variance over trailing 21 days."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_MON)


def jmp_003_rv_63d(close: pd.Series) -> pd.Series:
    """Realized variance over trailing 63 days."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_QTR)


def jmp_004_rv_126d(close: pd.Series) -> pd.Series:
    """Realized variance over trailing 126 days."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_HALF)


def jmp_005_rv_252d(close: pd.Series) -> pd.Series:
    """Realized variance over trailing 252 days."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_YEAR)


def jmp_006_rv_5d_annualized(close: pd.Series) -> pd.Series:
    """Annualized realized variance (5-day RV * 252/5)."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)


def jmp_007_rv_21d_annualized(close: pd.Series) -> pd.Series:
    """Annualized realized variance (21-day RV * 252/21)."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_MON) * (_TD_YEAR / _TD_MON)


def jmp_008_rv_63d_annualized(close: pd.Series) -> pd.Series:
    """Annualized realized variance (63-day RV * 252/63)."""
    r = _log_returns(close)
    return _realized_variance(r, _TD_QTR) * (_TD_YEAR / _TD_QTR)


def jmp_009_rv_vol_5d(close: pd.Series) -> pd.Series:
    """Realized volatility (sqrt of 5-day RV, annualized)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)
    return rv.clip(lower=0.0) ** 0.5


def jmp_010_rv_vol_21d(close: pd.Series) -> pd.Series:
    """Realized volatility (sqrt of 21-day RV, annualized)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    return rv.clip(lower=0.0) ** 0.5


# --- Group B (011-020): Bipower Variation (BPV) at multiple lookbacks ---

def jmp_011_bpv_5d(close: pd.Series) -> pd.Series:
    """Bipower variation (continuous component) over trailing 5 days."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_WEEK)


def jmp_012_bpv_21d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 21 days."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_MON)


def jmp_013_bpv_63d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 63 days."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_QTR)


def jmp_014_bpv_126d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 126 days."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_HALF)


def jmp_015_bpv_252d(close: pd.Series) -> pd.Series:
    """Bipower variation over trailing 252 days."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_YEAR)


def jmp_016_bpv_vol_5d(close: pd.Series) -> pd.Series:
    """Continuous volatility via BPV (annualized sqrt, 5-day)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)
    return bpv.clip(lower=0.0) ** 0.5


def jmp_017_bpv_vol_21d(close: pd.Series) -> pd.Series:
    """Continuous volatility via BPV (annualized sqrt, 21-day)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    return bpv.clip(lower=0.0) ** 0.5


def jmp_018_bpv_vol_63d(close: pd.Series) -> pd.Series:
    """Continuous volatility via BPV (annualized sqrt, 63-day)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_QTR) * (_TD_YEAR / _TD_QTR)
    return bpv.clip(lower=0.0) ** 0.5


def jmp_019_bpv_5d_annualized(close: pd.Series) -> pd.Series:
    """Annualized bipower variation (5-day BPV * 252/5)."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)


def jmp_020_bpv_21d_annualized(close: pd.Series) -> pd.Series:
    """Annualized bipower variation (21-day BPV * 252/21)."""
    r = _log_returns(close)
    return _bipower_variation(r, _TD_MON) * (_TD_YEAR / _TD_MON)


# --- Group C (021-030): Jump Variation and Jump-to-RV Ratios ---

def jmp_021_jv_5d(close: pd.Series) -> pd.Series:
    """Jump variation (RV - BPV, floored at 0) over trailing 5 days."""
    r = _log_returns(close)
    return _jump_variation(r, _TD_WEEK)


def jmp_022_jv_21d(close: pd.Series) -> pd.Series:
    """Jump variation over trailing 21 days."""
    r = _log_returns(close)
    return _jump_variation(r, _TD_MON)


def jmp_023_jv_63d(close: pd.Series) -> pd.Series:
    """Jump variation over trailing 63 days."""
    r = _log_returns(close)
    return _jump_variation(r, _TD_QTR)


def jmp_024_jv_252d(close: pd.Series) -> pd.Series:
    """Jump variation over trailing 252 days."""
    r = _log_returns(close)
    return _jump_variation(r, _TD_YEAR)


def jmp_025_jv_ratio_5d(close: pd.Series) -> pd.Series:
    """Ratio of jump variation to realized variance over 5 days (jump fraction)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_WEEK)
    rv = _realized_variance(r, _TD_WEEK)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_026_jv_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of jump variation to realized variance over 21 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_027_jv_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of jump variation to realized variance over 63 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_QTR)
    rv = _realized_variance(r, _TD_QTR)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_028_jv_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of jump variation to realized variance over 252 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_YEAR)
    rv = _realized_variance(r, _TD_YEAR)
    return _safe_div(jv, rv.clip(lower=_EPS))


def jmp_029_continuous_var_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of BPV to RV over 21 days (continuous-diffusion fraction)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(bpv, rv.clip(lower=_EPS))


def jmp_030_rv_minus_bpv_signed_21d(close: pd.Series) -> pd.Series:
    """Raw RV - BPV over 21 days (signed; negative possible if BPV > RV due to noise)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    return rv - bpv


# --- Group D (031-040): Jump Frequency and Count ---

def jmp_031_jump_count_3sigma_21d(close: pd.Series) -> pd.Series:
    """Count of 3-sigma daily jumps (|r| > 3*std) in trailing 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _rolling_sum(flag, _TD_MON)


def jmp_032_jump_count_3sigma_63d(close: pd.Series) -> pd.Series:
    """Count of 3-sigma jumps in trailing 63 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _rolling_sum(flag, _TD_QTR)


def jmp_033_jump_count_3sigma_252d(close: pd.Series) -> pd.Series:
    """Count of 3-sigma jumps in trailing 252 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _rolling_sum(flag, _TD_YEAR)


def jmp_034_jump_count_2sigma_21d(close: pd.Series) -> pd.Series:
    """Count of 2-sigma daily jumps in trailing 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=2.0)
    return _rolling_sum(flag, _TD_MON)


def jmp_035_jump_count_4sigma_21d(close: pd.Series) -> pd.Series:
    """Count of 4-sigma extreme jumps in trailing 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=4.0)
    return _rolling_sum(flag, _TD_MON)


def jmp_036_jump_count_4sigma_252d(close: pd.Series) -> pd.Series:
    """Count of 4-sigma extreme jumps in trailing 252 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=4.0)
    return _rolling_sum(flag, _TD_YEAR)


def jmp_037_neg_jump_count_3sigma_21d(close: pd.Series) -> pd.Series:
    """Count of negative 3-sigma jumps (crashes) in trailing 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_038_neg_jump_count_3sigma_63d(close: pd.Series) -> pd.Series:
    """Count of negative 3-sigma jumps in trailing 63 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def jmp_039_pos_jump_count_3sigma_21d(close: pd.Series) -> pd.Series:
    """Count of positive 3-sigma jumps (pops) in trailing 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r > 3.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def jmp_040_jump_freq_21d(close: pd.Series) -> pd.Series:
    """Fraction of days with 3-sigma jumps in trailing 21 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _rolling_sum(flag, _TD_MON) / _TD_MON


# --- Group E (041-050): Jump Magnitude Statistics ---

def jmp_041_max_abs_return_5d(close: pd.Series) -> pd.Series:
    """Maximum absolute log-return in trailing 5 days (largest single jump)."""
    r = _log_returns(close)
    return r.abs().rolling(_TD_WEEK, min_periods=1).max()


def jmp_042_max_abs_return_21d(close: pd.Series) -> pd.Series:
    """Maximum absolute log-return in trailing 21 days."""
    r = _log_returns(close)
    return r.abs().rolling(_TD_MON, min_periods=1).max()


def jmp_043_max_abs_return_63d(close: pd.Series) -> pd.Series:
    """Maximum absolute log-return in trailing 63 days."""
    r = _log_returns(close)
    return r.abs().rolling(_TD_QTR, min_periods=1).max()


def jmp_044_max_abs_return_252d(close: pd.Series) -> pd.Series:
    """Maximum absolute log-return in trailing 252 days."""
    r = _log_returns(close)
    return r.abs().rolling(_TD_YEAR, min_periods=1).max()


def jmp_045_max_neg_return_21d(close: pd.Series) -> pd.Series:
    """Most negative log-return (largest down-jump) in trailing 21 days."""
    r = _log_returns(close)
    return r.rolling(_TD_MON, min_periods=1).min()


def jmp_046_max_neg_return_63d(close: pd.Series) -> pd.Series:
    """Most negative log-return in trailing 63 days."""
    r = _log_returns(close)
    return r.rolling(_TD_QTR, min_periods=1).min()


def jmp_047_max_neg_return_252d(close: pd.Series) -> pd.Series:
    """Most negative log-return in trailing 252 days."""
    r = _log_returns(close)
    return r.rolling(_TD_YEAR, min_periods=1).min()


def jmp_048_max_pos_return_21d(close: pd.Series) -> pd.Series:
    """Largest positive log-return in trailing 21 days."""
    r = _log_returns(close)
    return r.rolling(_TD_MON, min_periods=1).max()


def jmp_049_jump_magnitude_ratio_21d(close: pd.Series) -> pd.Series:
    """Max |return| divided by avg |return| over 21 days (jump-vs-diffusion height)."""
    r = _log_returns(close)
    max_abs = r.abs().rolling(_TD_MON, min_periods=1).max()
    avg_abs = _rolling_mean(r.abs(), _TD_MON)
    return _safe_div(max_abs, avg_abs.clip(lower=_EPS))


def jmp_050_jump_magnitude_ratio_63d(close: pd.Series) -> pd.Series:
    """Max |return| divided by avg |return| over 63 days."""
    r = _log_returns(close)
    max_abs = r.abs().rolling(_TD_QTR, min_periods=1).max()
    avg_abs = _rolling_mean(r.abs(), _TD_QTR)
    return _safe_div(max_abs, avg_abs.clip(lower=_EPS))


# --- Group F (051-060): Signed Jump Variation ---

def jmp_051_pos_jv_21d(close: pd.Series) -> pd.Series:
    """Positive jump variation: sum of squared positive jump returns over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jumps = r.where(r > thresh, 0.0)
    return _rolling_sum(pos_jumps ** 2, _TD_MON)


def jmp_052_neg_jv_21d(close: pd.Series) -> pd.Series:
    """Negative jump variation: sum of squared negative jump returns over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jumps = r.where(r < -thresh, 0.0)
    return _rolling_sum(neg_jumps ** 2, _TD_MON)


def jmp_053_signed_jv_21d(close: pd.Series) -> pd.Series:
    """Signed jump variation: neg_JV - pos_JV over 21 days (negative = down-jump dominance)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    return neg_jv - pos_jv


def jmp_054_neg_jv_ratio_21d(close: pd.Series) -> pd.Series:
    """Fraction of RV explained by negative jumps over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(neg_jv, rv.clip(lower=_EPS))


def jmp_055_pos_jv_ratio_21d(close: pd.Series) -> pd.Series:
    """Fraction of RV explained by positive jumps over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(pos_jv, rv.clip(lower=_EPS))


def jmp_056_neg_jv_63d(close: pd.Series) -> pd.Series:
    """Negative jump variation over 63 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jumps = r.where(r < -thresh, 0.0)
    return _rolling_sum(neg_jumps ** 2, _TD_QTR)


def jmp_057_signed_jv_63d(close: pd.Series) -> pd.Series:
    """Signed jump variation over 63 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_QTR)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_QTR)
    return neg_jv - pos_jv


def jmp_058_neg_jv_ratio_63d(close: pd.Series) -> pd.Series:
    """Fraction of RV explained by negative jumps over 63 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_QTR)
    rv = _realized_variance(r, _TD_QTR)
    return _safe_div(neg_jv, rv.clip(lower=_EPS))


def jmp_059_jump_asymmetry_21d(close: pd.Series) -> pd.Series:
    """Jump asymmetry: neg_JV / (pos_JV + neg_JV) over 21 days; > 0.5 = down-jump dominated."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    total = (pos_jv + neg_jv).clip(lower=_EPS)
    return _safe_div(neg_jv, total)


def jmp_060_jump_net_direction_21d(close: pd.Series) -> pd.Series:
    """Net jump direction: sum of signed jump returns over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    signed = r.where(r.abs() > thresh, 0.0)
    return _rolling_sum(signed, _TD_MON)


# --- Group G (061-075): Jump Clustering and Timing Statistics ---

def jmp_061_consec_jump_days_3sigma(close: pd.Series) -> pd.Series:
    """Consecutive days with a 3-sigma jump (jump clustering streak)."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _consec_streak(flag > 0.5)


def jmp_062_days_since_last_neg_jump_3sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since last negative 3-sigma jump (0 = today is a jump day)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~r.isna(), np.nan)


def jmp_063_days_since_last_pos_jump_3sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since last positive 3-sigma jump."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r > 3.0 * sigma.fillna(_EPS)).astype(float)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~r.isna(), np.nan)


def jmp_064_days_since_last_jump_any_3sigma(close: pd.Series) -> pd.Series:
    """Days elapsed since last jump of either sign at 3-sigma."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last_idx = idx.where(flag == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~r.isna(), np.nan)


def jmp_065_jump_cluster_intensity_21d(close: pd.Series) -> pd.Series:
    """Sum of |returns| on jump days over trailing 21 days (cluster intensity)."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _rolling_sum(r.abs() * flag, _TD_MON)


def jmp_066_neg_jump_cluster_intensity_21d(close: pd.Series) -> pd.Series:
    """Sum of absolute negative jump returns over trailing 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    return _rolling_sum(r.abs() * flag, _TD_MON)


def jmp_067_jump_cluster_intensity_63d(close: pd.Series) -> pd.Series:
    """Sum of |returns| on jump days over trailing 63 days."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    return _rolling_sum(r.abs() * flag, _TD_QTR)


def jmp_068_jump_pairs_within_5d_21d(close: pd.Series) -> pd.Series:
    """Count of days within 5 days of another jump in trailing 21 days (clustering proxy)."""
    r = _log_returns(close)
    flag = _jump_flag(r, threshold_sigma=3.0)
    flag_float = flag.astype(float)
    # A day is "near a jump" if any of the past 5 days also had a jump
    recent_jump = _rolling_sum(flag_float, _TD_WEEK).shift(1).fillna(0.0)
    near_jump = ((flag_float > 0.5) & (recent_jump > 0)).astype(float)
    return _rolling_sum(near_jump, _TD_MON)


def jmp_069_jump_vol_frac_21d(close: pd.Series) -> pd.Series:
    """Fraction of total realized vol explained by jump vol (sqrt ratio) over 21 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    return _safe_div(jv.clip(lower=0.0) ** 0.5, rv.clip(lower=_EPS) ** 0.5)


def jmp_070_jump_vol_frac_63d(close: pd.Series) -> pd.Series:
    """Fraction of total realized vol explained by jump vol over 63 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_QTR)
    rv = _realized_variance(r, _TD_QTR)
    return _safe_div(jv.clip(lower=0.0) ** 0.5, rv.clip(lower=_EPS) ** 0.5)


def jmp_071_current_jump_flag_3sigma(close: pd.Series) -> pd.Series:
    """Binary flag: today's return is a 3-sigma jump (either direction)."""
    r = _log_returns(close)
    return _jump_flag(r, threshold_sigma=3.0)


def jmp_072_current_neg_jump_flag_3sigma(close: pd.Series) -> pd.Series:
    """Binary flag: today's return is a negative 3-sigma jump (crash day)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    return (r < -3.0 * sigma.fillna(_EPS)).astype(float)


def jmp_073_current_jump_flag_4sigma(close: pd.Series) -> pd.Series:
    """Binary flag: today's return is a 4-sigma extreme jump."""
    r = _log_returns(close)
    return _jump_flag(r, threshold_sigma=4.0)


def jmp_074_rv_bpv_ratio_21d(close: pd.Series) -> pd.Series:
    """RV / BPV over 21 days (>1 indicates jump presence; 1 = pure diffusion)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    return _safe_div(rv, bpv.clip(lower=_EPS))


def jmp_075_rv_bpv_ratio_63d(close: pd.Series) -> pd.Series:
    """RV / BPV over 63 days."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_QTR)
    bpv = _bipower_variation(r, _TD_QTR)
    return _safe_div(rv, bpv.clip(lower=_EPS))


# ── Registry ──────────────────────────────────────────────────────────────────

JUMP_DISCONTINUITY_REGISTRY_001_075 = {
    "jmp_001_rv_5d": {"inputs": ["close"], "func": jmp_001_rv_5d},
    "jmp_002_rv_21d": {"inputs": ["close"], "func": jmp_002_rv_21d},
    "jmp_003_rv_63d": {"inputs": ["close"], "func": jmp_003_rv_63d},
    "jmp_004_rv_126d": {"inputs": ["close"], "func": jmp_004_rv_126d},
    "jmp_005_rv_252d": {"inputs": ["close"], "func": jmp_005_rv_252d},
    "jmp_006_rv_5d_annualized": {"inputs": ["close"], "func": jmp_006_rv_5d_annualized},
    "jmp_007_rv_21d_annualized": {"inputs": ["close"], "func": jmp_007_rv_21d_annualized},
    "jmp_008_rv_63d_annualized": {"inputs": ["close"], "func": jmp_008_rv_63d_annualized},
    "jmp_009_rv_vol_5d": {"inputs": ["close"], "func": jmp_009_rv_vol_5d},
    "jmp_010_rv_vol_21d": {"inputs": ["close"], "func": jmp_010_rv_vol_21d},
    "jmp_011_bpv_5d": {"inputs": ["close"], "func": jmp_011_bpv_5d},
    "jmp_012_bpv_21d": {"inputs": ["close"], "func": jmp_012_bpv_21d},
    "jmp_013_bpv_63d": {"inputs": ["close"], "func": jmp_013_bpv_63d},
    "jmp_014_bpv_126d": {"inputs": ["close"], "func": jmp_014_bpv_126d},
    "jmp_015_bpv_252d": {"inputs": ["close"], "func": jmp_015_bpv_252d},
    "jmp_016_bpv_vol_5d": {"inputs": ["close"], "func": jmp_016_bpv_vol_5d},
    "jmp_017_bpv_vol_21d": {"inputs": ["close"], "func": jmp_017_bpv_vol_21d},
    "jmp_018_bpv_vol_63d": {"inputs": ["close"], "func": jmp_018_bpv_vol_63d},
    "jmp_019_bpv_5d_annualized": {"inputs": ["close"], "func": jmp_019_bpv_5d_annualized},
    "jmp_020_bpv_21d_annualized": {"inputs": ["close"], "func": jmp_020_bpv_21d_annualized},
    "jmp_021_jv_5d": {"inputs": ["close"], "func": jmp_021_jv_5d},
    "jmp_022_jv_21d": {"inputs": ["close"], "func": jmp_022_jv_21d},
    "jmp_023_jv_63d": {"inputs": ["close"], "func": jmp_023_jv_63d},
    "jmp_024_jv_252d": {"inputs": ["close"], "func": jmp_024_jv_252d},
    "jmp_025_jv_ratio_5d": {"inputs": ["close"], "func": jmp_025_jv_ratio_5d},
    "jmp_026_jv_ratio_21d": {"inputs": ["close"], "func": jmp_026_jv_ratio_21d},
    "jmp_027_jv_ratio_63d": {"inputs": ["close"], "func": jmp_027_jv_ratio_63d},
    "jmp_028_jv_ratio_252d": {"inputs": ["close"], "func": jmp_028_jv_ratio_252d},
    "jmp_029_continuous_var_ratio_21d": {"inputs": ["close"], "func": jmp_029_continuous_var_ratio_21d},
    "jmp_030_rv_minus_bpv_signed_21d": {"inputs": ["close"], "func": jmp_030_rv_minus_bpv_signed_21d},
    "jmp_031_jump_count_3sigma_21d": {"inputs": ["close"], "func": jmp_031_jump_count_3sigma_21d},
    "jmp_032_jump_count_3sigma_63d": {"inputs": ["close"], "func": jmp_032_jump_count_3sigma_63d},
    "jmp_033_jump_count_3sigma_252d": {"inputs": ["close"], "func": jmp_033_jump_count_3sigma_252d},
    "jmp_034_jump_count_2sigma_21d": {"inputs": ["close"], "func": jmp_034_jump_count_2sigma_21d},
    "jmp_035_jump_count_4sigma_21d": {"inputs": ["close"], "func": jmp_035_jump_count_4sigma_21d},
    "jmp_036_jump_count_4sigma_252d": {"inputs": ["close"], "func": jmp_036_jump_count_4sigma_252d},
    "jmp_037_neg_jump_count_3sigma_21d": {"inputs": ["close"], "func": jmp_037_neg_jump_count_3sigma_21d},
    "jmp_038_neg_jump_count_3sigma_63d": {"inputs": ["close"], "func": jmp_038_neg_jump_count_3sigma_63d},
    "jmp_039_pos_jump_count_3sigma_21d": {"inputs": ["close"], "func": jmp_039_pos_jump_count_3sigma_21d},
    "jmp_040_jump_freq_21d": {"inputs": ["close"], "func": jmp_040_jump_freq_21d},
    "jmp_041_max_abs_return_5d": {"inputs": ["close"], "func": jmp_041_max_abs_return_5d},
    "jmp_042_max_abs_return_21d": {"inputs": ["close"], "func": jmp_042_max_abs_return_21d},
    "jmp_043_max_abs_return_63d": {"inputs": ["close"], "func": jmp_043_max_abs_return_63d},
    "jmp_044_max_abs_return_252d": {"inputs": ["close"], "func": jmp_044_max_abs_return_252d},
    "jmp_045_max_neg_return_21d": {"inputs": ["close"], "func": jmp_045_max_neg_return_21d},
    "jmp_046_max_neg_return_63d": {"inputs": ["close"], "func": jmp_046_max_neg_return_63d},
    "jmp_047_max_neg_return_252d": {"inputs": ["close"], "func": jmp_047_max_neg_return_252d},
    "jmp_048_max_pos_return_21d": {"inputs": ["close"], "func": jmp_048_max_pos_return_21d},
    "jmp_049_jump_magnitude_ratio_21d": {"inputs": ["close"], "func": jmp_049_jump_magnitude_ratio_21d},
    "jmp_050_jump_magnitude_ratio_63d": {"inputs": ["close"], "func": jmp_050_jump_magnitude_ratio_63d},
    "jmp_051_pos_jv_21d": {"inputs": ["close"], "func": jmp_051_pos_jv_21d},
    "jmp_052_neg_jv_21d": {"inputs": ["close"], "func": jmp_052_neg_jv_21d},
    "jmp_053_signed_jv_21d": {"inputs": ["close"], "func": jmp_053_signed_jv_21d},
    "jmp_054_neg_jv_ratio_21d": {"inputs": ["close"], "func": jmp_054_neg_jv_ratio_21d},
    "jmp_055_pos_jv_ratio_21d": {"inputs": ["close"], "func": jmp_055_pos_jv_ratio_21d},
    "jmp_056_neg_jv_63d": {"inputs": ["close"], "func": jmp_056_neg_jv_63d},
    "jmp_057_signed_jv_63d": {"inputs": ["close"], "func": jmp_057_signed_jv_63d},
    "jmp_058_neg_jv_ratio_63d": {"inputs": ["close"], "func": jmp_058_neg_jv_ratio_63d},
    "jmp_059_jump_asymmetry_21d": {"inputs": ["close"], "func": jmp_059_jump_asymmetry_21d},
    "jmp_060_jump_net_direction_21d": {"inputs": ["close"], "func": jmp_060_jump_net_direction_21d},
    "jmp_061_consec_jump_days_3sigma": {"inputs": ["close"], "func": jmp_061_consec_jump_days_3sigma},
    "jmp_062_days_since_last_neg_jump_3sigma": {"inputs": ["close"], "func": jmp_062_days_since_last_neg_jump_3sigma},
    "jmp_063_days_since_last_pos_jump_3sigma": {"inputs": ["close"], "func": jmp_063_days_since_last_pos_jump_3sigma},
    "jmp_064_days_since_last_jump_any_3sigma": {"inputs": ["close"], "func": jmp_064_days_since_last_jump_any_3sigma},
    "jmp_065_jump_cluster_intensity_21d": {"inputs": ["close"], "func": jmp_065_jump_cluster_intensity_21d},
    "jmp_066_neg_jump_cluster_intensity_21d": {"inputs": ["close"], "func": jmp_066_neg_jump_cluster_intensity_21d},
    "jmp_067_jump_cluster_intensity_63d": {"inputs": ["close"], "func": jmp_067_jump_cluster_intensity_63d},
    "jmp_068_jump_pairs_within_5d_21d": {"inputs": ["close"], "func": jmp_068_jump_pairs_within_5d_21d},
    "jmp_069_jump_vol_frac_21d": {"inputs": ["close"], "func": jmp_069_jump_vol_frac_21d},
    "jmp_070_jump_vol_frac_63d": {"inputs": ["close"], "func": jmp_070_jump_vol_frac_63d},
    "jmp_071_current_jump_flag_3sigma": {"inputs": ["close"], "func": jmp_071_current_jump_flag_3sigma},
    "jmp_072_current_neg_jump_flag_3sigma": {"inputs": ["close"], "func": jmp_072_current_neg_jump_flag_3sigma},
    "jmp_073_current_jump_flag_4sigma": {"inputs": ["close"], "func": jmp_073_current_jump_flag_4sigma},
    "jmp_074_rv_bpv_ratio_21d": {"inputs": ["close"], "func": jmp_074_rv_bpv_ratio_21d},
    "jmp_075_rv_bpv_ratio_63d": {"inputs": ["close"], "func": jmp_075_rv_bpv_ratio_63d},
}
