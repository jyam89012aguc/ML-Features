"""
111_jump_discontinuity — 2nd Derivatives (Features jmp_drv2_001-025)
Domain: rate of change of base jump discontinuity features — velocity of jump activity
Includes derivatives of RV, BPV, jump variation ratios, jump counts, jump magnitudes
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


def _log_returns(close: pd.Series) -> pd.Series:
    """Log returns: ln(close_t / close_{t-1})."""
    return np.log(close / close.shift(1))


def _realized_variance(r: pd.Series, w: int) -> pd.Series:
    """Rolling realized variance over w days."""
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


def _jump_flag(r: pd.Series, threshold_sigma: float = 3.0) -> pd.Series:
    """Binary flag: |return| > threshold_sigma * rolling 21d std."""
    sigma = _rolling_std(r, _TD_MON)
    return (r.abs() > threshold_sigma * sigma.fillna(_EPS)).astype(float)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def jmp_drv2_001_rv21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day realized variance (velocity of RV)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return rv.diff(_TD_WEEK)


def jmp_drv2_002_rv21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day realized variance (monthly velocity of RV)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return rv.diff(_TD_MON)


def jmp_drv2_003_bpv21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day bipower variation (velocity of continuous component)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    return bpv.diff(_TD_WEEK)


def jmp_drv2_004_jv21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day jump variation (velocity of jump component deepening)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    return jv.diff(_TD_WEEK)


def jmp_drv2_005_jv_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day JV/RV ratio (velocity of jump fraction change)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def jmp_drv2_006_jump_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day 3-sigma jump count (velocity of jump frequency)."""
    r = _log_returns(close)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_MON)
    return cnt.diff(_TD_WEEK)


def jmp_drv2_007_neg_jump_count_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day negative jump count (crash frequency velocity)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def jmp_drv2_008_max_abs_return_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day max absolute return (velocity of extreme return growth)."""
    r = _log_returns(close)
    mx = r.abs().rolling(_TD_MON, min_periods=1).max()
    return mx.diff(_TD_WEEK)


def jmp_drv2_009_neg_jv_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day negative jump variation ratio."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(neg_jv, rv.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def jmp_drv2_010_rv_bpv_ratio_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of RV/BPV ratio over 21 days (velocity of jump detection ratio)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    ratio = _safe_div(rv, bpv.clip(lower=_EPS))
    return ratio.diff(_TD_WEEK)


def jmp_drv2_011_signed_jv_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of signed jump variation over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    sjv = neg_jv - pos_jv
    return sjv.diff(_TD_WEEK)


def jmp_drv2_012_jv_ratio_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day JV/RV ratio (monthly velocity of jump fraction)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return ratio.diff(_TD_MON)


def jmp_drv2_013_rv_vol_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of annualized 21-day realized volatility (sqrt RV * ann factor)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    rvol = rv.clip(lower=0.0) ** 0.5
    return rvol.diff(_TD_WEEK)


def jmp_drv2_014_bpv_vol_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of annualized 21-day continuous volatility (BPV-based)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    bvol = bpv.clip(lower=0.0) ** 0.5
    return bvol.diff(_TD_WEEK)


def jmp_drv2_015_jv_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 63-day jump variation."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_QTR)
    return jv.diff(_TD_WEEK)


def jmp_drv2_016_jump_count_3sigma_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day 3-sigma jump count."""
    r = _log_returns(close)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_QTR)
    return cnt.diff(_TD_MON)


def jmp_drv2_017_jv_ratio_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day JV/RV ratio."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_QTR)
    rv = _realized_variance(r, _TD_QTR)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    return ratio.diff(_TD_MON)


def jmp_drv2_018_max_neg_return_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day most negative return (is the bottom getting worse?)."""
    r = _log_returns(close)
    mx = r.rolling(_TD_MON, min_periods=1).min()
    return mx.diff(_TD_WEEK)


def jmp_drv2_019_jump_asymmetry_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day jump asymmetry ratio (neg_JV / total_JV)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    total = (pos_jv + neg_jv).clip(lower=_EPS)
    asym = _safe_div(neg_jv, total)
    return asym.diff(_TD_WEEK)


def jmp_drv2_020_rv_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day RV over 21 days (trend in realized variance)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return _linslope(rv, _TD_MON)


def jmp_drv2_021_jv_ratio_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of JV/RV ratio over 21 days."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    return _linslope(ratio, _TD_MON)


def jmp_drv2_022_neg_jump_count_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day negative jump count."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    return _linslope(cnt, _TD_MON)


def jmp_drv2_023_rv21d_5d_slope(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day RV over 5 days (very recent RV trend)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    return _linslope(rv, _TD_WEEK)


def jmp_drv2_024_jv_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day jump variation (monthly velocity of jump activity)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    return jv.diff(_TD_MON)


def jmp_drv2_025_rv_bpv_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (RV - BPV) over 21 days (raw jump-component velocity)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    diff = rv - bpv
    return diff.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

JUMP_DISCONTINUITY_REGISTRY_2ND_DERIVATIVES = {
    "jmp_drv2_001_rv21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_001_rv21d_5d_diff},
    "jmp_drv2_002_rv21d_21d_diff": {"inputs": ["close"], "func": jmp_drv2_002_rv21d_21d_diff},
    "jmp_drv2_003_bpv21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_003_bpv21d_5d_diff},
    "jmp_drv2_004_jv21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_004_jv21d_5d_diff},
    "jmp_drv2_005_jv_ratio_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_005_jv_ratio_21d_5d_diff},
    "jmp_drv2_006_jump_count_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_006_jump_count_21d_5d_diff},
    "jmp_drv2_007_neg_jump_count_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_007_neg_jump_count_21d_5d_diff},
    "jmp_drv2_008_max_abs_return_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_008_max_abs_return_21d_5d_diff},
    "jmp_drv2_009_neg_jv_ratio_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_009_neg_jv_ratio_21d_5d_diff},
    "jmp_drv2_010_rv_bpv_ratio_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_010_rv_bpv_ratio_21d_5d_diff},
    "jmp_drv2_011_signed_jv_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_011_signed_jv_21d_5d_diff},
    "jmp_drv2_012_jv_ratio_21d_21d_diff": {"inputs": ["close"], "func": jmp_drv2_012_jv_ratio_21d_21d_diff},
    "jmp_drv2_013_rv_vol_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_013_rv_vol_21d_5d_diff},
    "jmp_drv2_014_bpv_vol_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_014_bpv_vol_21d_5d_diff},
    "jmp_drv2_015_jv_63d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_015_jv_63d_5d_diff},
    "jmp_drv2_016_jump_count_3sigma_63d_21d_diff": {"inputs": ["close"], "func": jmp_drv2_016_jump_count_3sigma_63d_21d_diff},
    "jmp_drv2_017_jv_ratio_63d_21d_diff": {"inputs": ["close"], "func": jmp_drv2_017_jv_ratio_63d_21d_diff},
    "jmp_drv2_018_max_neg_return_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_018_max_neg_return_21d_5d_diff},
    "jmp_drv2_019_jump_asymmetry_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv2_019_jump_asymmetry_21d_5d_diff},
    "jmp_drv2_020_rv_slope_21d": {"inputs": ["close"], "func": jmp_drv2_020_rv_slope_21d},
    "jmp_drv2_021_jv_ratio_slope_21d": {"inputs": ["close"], "func": jmp_drv2_021_jv_ratio_slope_21d},
    "jmp_drv2_022_neg_jump_count_21d_slope_21d": {"inputs": ["close"], "func": jmp_drv2_022_neg_jump_count_21d_slope_21d},
    "jmp_drv2_023_rv21d_5d_slope": {"inputs": ["close"], "func": jmp_drv2_023_rv21d_5d_slope},
    "jmp_drv2_024_jv_21d_21d_diff": {"inputs": ["close"], "func": jmp_drv2_024_jv_21d_21d_diff},
    "jmp_drv2_025_rv_bpv_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv2_025_rv_bpv_diff_5d_diff},
}
