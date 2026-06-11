"""
111_jump_discontinuity — 3rd Derivatives (Features jmp_drv3_001-025)
Domain: rate of change of 2nd-derivative jump features — acceleration of jump velocity
Includes acceleration of RV velocity, BPV velocity, jump ratio velocity, jump count velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def jmp_drv3_001_rv21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day RV (acceleration of RV velocity)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    vel = rv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_002_rv21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21-day RV (jerk in monthly RV change)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    vel21 = rv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def jmp_drv3_003_bpv21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day BPV (acceleration of continuous var velocity)."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    vel = bpv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_004_jv21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day jump variation (jerk in JV deepening)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    vel = jv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_005_jv_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day JV/RV ratio (acceleration of jump fraction change)."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_006_jump_count_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day jump count (acceleration of jump frequency)."""
    r = _log_returns(close)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_007_neg_jump_count_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day negative jump count."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_008_rv_bpv_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of RV/BPV ratio (acceleration of jump detection ratio)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    ratio = _safe_div(rv, bpv.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_009_signed_jv_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of signed jump variation (acceleration of down-jump dominance)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    sjv = neg_jv - pos_jv
    vel = sjv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_010_jv_ratio_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of JV/RV ratio."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def jmp_drv3_011_rv_vol_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of annualized 21-day RV vol."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON) * (_TD_YEAR / _TD_MON)
    rvol = rv.clip(lower=0.0) ** 0.5
    vel = rvol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_012_jv_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day jump variation."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_QTR)
    vel = jv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_013_neg_jv_ratio_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of negative JV ratio over 21 days."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(neg_jv, rv.clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_014_jump_asymmetry_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of jump asymmetry (acceleration of down-jump skew)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    total = (pos_jv + neg_jv).clip(lower=_EPS)
    asym = _safe_div(neg_jv, total)
    vel = asym.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_015_max_abs_return_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day max |return| (acceleration of extreme return growth)."""
    r = _log_returns(close)
    mx = r.abs().rolling(_TD_MON, min_periods=1).max()
    vel = mx.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_016_rv_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of RV (rate of slope change)."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    slope21 = _linslope(rv, _TD_MON)
    return slope21.diff(_TD_WEEK)


def jmp_drv3_017_jv_ratio_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of JV/RV ratio."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS)).fillna(0.0)
    slope21 = _linslope(ratio, _TD_MON)
    return slope21.diff(_TD_WEEK)


def jmp_drv3_018_rv21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day RV."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    vel5 = rv.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def jmp_drv3_019_jv_ratio_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of JV/RV ratio."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_MON)
    rv = _realized_variance(r, _TD_MON)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    vel5 = ratio.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def jmp_drv3_020_neg_jump_count_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day negative jump count (jerk in crash freq trend)."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    flag = (r < -3.0 * sigma.fillna(_EPS)).astype(float)
    cnt = _rolling_sum(flag, _TD_MON)
    slope21 = _linslope(cnt, _TD_MON)
    return slope21.diff(_TD_WEEK)


def jmp_drv3_021_bpv21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day BPV."""
    r = _log_returns(close)
    bpv = _bipower_variation(r, _TD_MON)
    vel5 = bpv.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def jmp_drv3_022_signed_jv_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of signed JV."""
    r = _log_returns(close)
    sigma = _rolling_std(r, _TD_MON)
    thresh = 3.0 * sigma.fillna(_EPS)
    pos_jv = _rolling_sum(r.where(r > thresh, 0.0) ** 2, _TD_MON)
    neg_jv = _rolling_sum(r.where(r < -thresh, 0.0) ** 2, _TD_MON)
    sjv = neg_jv - pos_jv
    vel5 = sjv.diff(_TD_WEEK)
    return _linslope(vel5, _TD_MON)


def jmp_drv3_023_rv_bpv_diff_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (RV - BPV) — acceleration of raw jump component velocity."""
    r = _log_returns(close)
    rv = _realized_variance(r, _TD_MON)
    bpv = _bipower_variation(r, _TD_MON)
    diff = rv - bpv
    vel = diff.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def jmp_drv3_024_jv_ratio_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day JV/RV ratio."""
    r = _log_returns(close)
    jv = _jump_variation(r, _TD_QTR)
    rv = _realized_variance(r, _TD_QTR)
    ratio = _safe_div(jv, rv.clip(lower=_EPS))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def jmp_drv3_025_jump_count_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21-day jump count."""
    r = _log_returns(close)
    cnt = _rolling_sum(_jump_flag(r, 3.0), _TD_MON)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

JUMP_DISCONTINUITY_REGISTRY_3RD_DERIVATIVES = {
    "jmp_drv3_001_rv21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_001_rv21d_5d_diff_5d_diff},
    "jmp_drv3_002_rv21d_21d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_002_rv21d_21d_diff_5d_diff},
    "jmp_drv3_003_bpv21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_003_bpv21d_5d_diff_5d_diff},
    "jmp_drv3_004_jv21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_004_jv21d_5d_diff_5d_diff},
    "jmp_drv3_005_jv_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_005_jv_ratio_21d_5d_diff_5d_diff},
    "jmp_drv3_006_jump_count_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_006_jump_count_21d_5d_diff_5d_diff},
    "jmp_drv3_007_neg_jump_count_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_007_neg_jump_count_21d_5d_diff_5d_diff},
    "jmp_drv3_008_rv_bpv_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_008_rv_bpv_ratio_21d_5d_diff_5d_diff},
    "jmp_drv3_009_signed_jv_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_009_signed_jv_21d_5d_diff_5d_diff},
    "jmp_drv3_010_jv_ratio_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_010_jv_ratio_21d_21d_diff_5d_diff},
    "jmp_drv3_011_rv_vol_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_011_rv_vol_21d_5d_diff_5d_diff},
    "jmp_drv3_012_jv_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_012_jv_63d_5d_diff_5d_diff},
    "jmp_drv3_013_neg_jv_ratio_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_013_neg_jv_ratio_21d_5d_diff_5d_diff},
    "jmp_drv3_014_jump_asymmetry_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_014_jump_asymmetry_21d_5d_diff_5d_diff},
    "jmp_drv3_015_max_abs_return_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_015_max_abs_return_21d_5d_diff_5d_diff},
    "jmp_drv3_016_rv_slope_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv3_016_rv_slope_21d_5d_diff},
    "jmp_drv3_017_jv_ratio_slope_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv3_017_jv_ratio_slope_21d_5d_diff},
    "jmp_drv3_018_rv21d_5d_diff_slope_21d": {"inputs": ["close"], "func": jmp_drv3_018_rv21d_5d_diff_slope_21d},
    "jmp_drv3_019_jv_ratio_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": jmp_drv3_019_jv_ratio_21d_5d_diff_slope_21d},
    "jmp_drv3_020_neg_jump_count_slope_21d_5d_diff": {"inputs": ["close"], "func": jmp_drv3_020_neg_jump_count_slope_21d_5d_diff},
    "jmp_drv3_021_bpv21d_5d_diff_slope_21d": {"inputs": ["close"], "func": jmp_drv3_021_bpv21d_5d_diff_slope_21d},
    "jmp_drv3_022_signed_jv_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": jmp_drv3_022_signed_jv_21d_5d_diff_slope_21d},
    "jmp_drv3_023_rv_bpv_diff_5d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_023_rv_bpv_diff_5d_diff_5d_diff},
    "jmp_drv3_024_jv_ratio_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_024_jv_ratio_63d_21d_diff_5d_diff},
    "jmp_drv3_025_jump_count_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": jmp_drv3_025_jump_count_21d_21d_diff_5d_diff},
}
