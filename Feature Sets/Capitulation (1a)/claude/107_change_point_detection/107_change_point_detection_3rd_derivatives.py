"""
107_change_point_detection — 3rd Derivatives (Features cpd_drv3_001-025)
Domain: rate of change of 2nd-derivative change-point features — acceleration of
        structural-break velocities. Captures how quickly the velocity of CUSUM,
        mean-shift, variance-shift, and break-count features are themselves changing.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _log_returns(close: pd.Series) -> pd.Series:
    return np.log(close / close.shift(1))


def _cusum_neg(s: pd.Series, w: int) -> pd.Series:
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu = clean.mean()
        sv = 0.0
        for x in clean:
            sv = min(0.0, sv + (x - mu))
        return sv
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_fn, raw=True)


def _cusum_pos(s: pd.Series, w: int) -> pd.Series:
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu = clean.mean()
        sv = 0.0
        for x in clean:
            sv = max(0.0, sv + (x - mu))
        return sv
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_fn, raw=True)


def _mean_shift_stat(s: pd.Series, half: int) -> pd.Series:
    w = 2 * half
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return abs(clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return s.rolling(w, min_periods=max(4, half)).apply(_stat, raw=True)


def _var_shift_stat(s: pd.Series, half: int) -> pd.Series:
    w = 2 * half
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        var_b = clean[:mid].var()
        var_a = clean[mid:].var()
        if var_b < _EPS:
            return 0.0
        return np.log((var_a + _EPS) / (var_b + _EPS))
    return s.rolling(w, min_periods=max(4, half)).apply(_stat, raw=True)


def _mean_shift_signed(s: pd.Series, half: int) -> pd.Series:
    w = 2 * half
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return (clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return s.rolling(w, min_periods=max(4, half)).apply(_stat, raw=True)


def _break_flag(s: pd.Series, half: int, threshold: float) -> pd.Series:
    return (_mean_shift_stat(s, half) > threshold).astype(float)


def _time_since_break(flag: pd.Series) -> pd.Series:
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last = idx.where(flag == 1.0).ffill()
    elapsed = idx - last
    return elapsed.where(last.notna(), np.nan)


def _linslope(s: pd.Series, w: int) -> pd.Series:
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

def cpd_drv3_001_cusum_neg_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of |lower CUSUM| (21d) — acceleration of CUSUM deterioration."""
    vel = _cusum_neg(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_002_cusum_neg_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of |lower CUSUM| (21d) — jerk in monthly CUSUM trend."""
    vel21 = _cusum_neg(_log_returns(close), _TD_MON).abs().diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cpd_drv3_003_mean_shift_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of mean-shift stat (half=21) — acceleration of break signal."""
    vel = _mean_shift_stat(_log_returns(close), _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_004_mean_shift_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of mean-shift stat — jerk in monthly break change."""
    vel21 = _mean_shift_stat(_log_returns(close), _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cpd_drv3_005_var_shift_abs_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of |var-shift stat| (half=21) — acceleration of variance break."""
    vel = _var_shift_stat(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_006_signed_shift_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of signed mean-shift (half=21) — acceleration of downward break."""
    vel = _mean_shift_signed(_log_returns(close), _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_007_combined_shift_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite break score (mean+var, half=21)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    vel = (ms + vs).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_008_cusum_neg_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of |lower CUSUM| (63d) — acceleration of quarterly CUSUM."""
    vel = _cusum_neg(_log_returns(close), _TD_QTR).abs().diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_009_mean_shift_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of mean-shift stat (half=63) — acceleration of quarterly break."""
    vel = _mean_shift_stat(_log_returns(close), _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_010_cusum_normalized_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of normalized lower CUSUM (21d)."""
    r   = _log_returns(close)
    cs  = _cusum_neg(r, _TD_MON).abs()
    s   = _rolling_std(r, _TD_MON)
    ncs = cs / s.clip(lower=_EPS)
    vel = ncs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_011_break_count_63d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of break count in 63d — acceleration of break frequency change."""
    flag  = _break_flag(_log_returns(close), _TD_MON, 1.0)
    count = _rolling_sum(flag, _TD_QTR)
    vel   = count.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_012_break_score_composite_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite break score (mean+var+normalized CUSUM, half=21)."""
    r   = _log_returns(close)
    ms  = _mean_shift_stat(r, _TD_MON)
    vs  = _var_shift_stat(r, _TD_MON).abs()
    cs  = _cusum_neg(r, _TD_MON).abs()
    std = _rolling_std(r, _TD_MON)
    score = ms + vs + (cs / std.clip(lower=_EPS)).fillna(0.0)
    vel   = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_013_ols_slope_change_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope change (21d)."""
    lp = np.log(close.clip(lower=_EPS))
    sc = _linslope(lp, _TD_MON) - _linslope(lp, _TD_MON).shift(_TD_MON)
    vel = sc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_014_before_after_return_diff_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of before/after return difference (half=21)."""
    r      = _log_returns(close)
    after  = _rolling_mean(r, _TD_MON)
    before = _rolling_mean(r, _TD_MON).shift(_TD_MON)
    diff   = after - before
    vel    = diff.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_015_before_after_vol_diff_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of before/after volatility difference (half=21)."""
    r     = _log_returns(close)
    std_a = _rolling_std(r, _TD_MON)
    std_b = _rolling_std(r, _TD_MON).shift(_TD_MON)
    vel   = (std_a - std_b).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cpd_drv3_016_cusum_neg_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of |lower CUSUM| (21d)."""
    vel = _cusum_neg(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def cpd_drv3_017_mean_shift_21d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of mean-shift stat (half=21)."""
    vel = _mean_shift_stat(_log_returns(close), _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def cpd_drv3_018_var_shift_abs_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of |var-shift stat| (half=21)."""
    vel = _var_shift_stat(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def cpd_drv3_019_combined_shift_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of composite break score (mean+var, half=21)."""
    ms    = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs    = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    vel21 = (ms + vs).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cpd_drv3_020_signed_shift_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in signed mean-shift — jerk in downward break trend."""
    vel21 = _mean_shift_signed(_log_returns(close), _TD_MON).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cpd_drv3_021_cusum_neg_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope over 21d of |lower CUSUM| (21d)."""
    slope = _linslope(_cusum_neg(_log_returns(close), _TD_MON).abs(), _TD_MON)
    return slope.diff(_TD_WEEK)


def cpd_drv3_022_mean_shift_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope over 21d of mean-shift stat (half=21)."""
    slope = _linslope(_mean_shift_stat(_log_returns(close), _TD_MON), _TD_MON)
    return slope.diff(_TD_WEEK)


def cpd_drv3_023_break_score_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of composite break score (mean+var+norm-CUSUM)."""
    r   = _log_returns(close)
    ms  = _mean_shift_stat(r, _TD_MON)
    vs  = _var_shift_stat(r, _TD_MON).abs()
    cs  = _cusum_neg(r, _TD_MON).abs()
    std = _rolling_std(r, _TD_MON)
    score = ms + vs + (cs / std.clip(lower=_EPS)).fillna(0.0)
    vel21 = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cpd_drv3_024_cusum_normalized_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in normalized lower CUSUM (21d)."""
    r   = _log_returns(close)
    cs  = _cusum_neg(r, _TD_MON).abs()
    s   = _rolling_std(r, _TD_MON)
    ncs = cs / s.clip(lower=_EPS)
    vel21 = ncs.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cpd_drv3_025_mean_shift_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of mean-shift stat (half=63)."""
    vel21 = _mean_shift_stat(_log_returns(close), _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CHANGE_POINT_DETECTION_REGISTRY_3RD_DERIVATIVES = {
    "cpd_drv3_001_cusum_neg_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_001_cusum_neg_21d_5d_diff_5d_diff},
    "cpd_drv3_002_cusum_neg_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_002_cusum_neg_21d_21d_diff_5d_diff},
    "cpd_drv3_003_mean_shift_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_003_mean_shift_21d_5d_diff_5d_diff},
    "cpd_drv3_004_mean_shift_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_004_mean_shift_21d_21d_diff_5d_diff},
    "cpd_drv3_005_var_shift_abs_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_005_var_shift_abs_21d_5d_diff_5d_diff},
    "cpd_drv3_006_signed_shift_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_006_signed_shift_21d_5d_diff_5d_diff},
    "cpd_drv3_007_combined_shift_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_007_combined_shift_21d_5d_diff_5d_diff},
    "cpd_drv3_008_cusum_neg_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_008_cusum_neg_63d_5d_diff_5d_diff},
    "cpd_drv3_009_mean_shift_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_009_mean_shift_63d_5d_diff_5d_diff},
    "cpd_drv3_010_cusum_normalized_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_010_cusum_normalized_21d_5d_diff_5d_diff},
    "cpd_drv3_011_break_count_63d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_011_break_count_63d_5d_diff_5d_diff},
    "cpd_drv3_012_break_score_composite_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_012_break_score_composite_21d_5d_diff_5d_diff},
    "cpd_drv3_013_ols_slope_change_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_013_ols_slope_change_21d_5d_diff_5d_diff},
    "cpd_drv3_014_before_after_return_diff_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_014_before_after_return_diff_21d_5d_diff_5d_diff},
    "cpd_drv3_015_before_after_vol_diff_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_015_before_after_vol_diff_21d_5d_diff_5d_diff},
    "cpd_drv3_016_cusum_neg_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": cpd_drv3_016_cusum_neg_21d_5d_diff_slope_21d},
    "cpd_drv3_017_mean_shift_21d_5d_diff_slope_21d": {"inputs": ["close"], "func": cpd_drv3_017_mean_shift_21d_5d_diff_slope_21d},
    "cpd_drv3_018_var_shift_abs_5d_diff_slope_21d": {"inputs": ["close"], "func": cpd_drv3_018_var_shift_abs_5d_diff_slope_21d},
    "cpd_drv3_019_combined_shift_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_019_combined_shift_21d_21d_diff_5d_diff},
    "cpd_drv3_020_signed_shift_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_020_signed_shift_21d_21d_diff_5d_diff},
    "cpd_drv3_021_cusum_neg_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv3_021_cusum_neg_21d_slope_21d_5d_diff},
    "cpd_drv3_022_mean_shift_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv3_022_mean_shift_21d_slope_21d_5d_diff},
    "cpd_drv3_023_break_score_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_023_break_score_21d_21d_diff_5d_diff},
    "cpd_drv3_024_cusum_normalized_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_024_cusum_normalized_21d_21d_diff_5d_diff},
    "cpd_drv3_025_mean_shift_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": cpd_drv3_025_mean_shift_63d_21d_diff_5d_diff},
}
