"""
107_change_point_detection — 2nd Derivatives (Features cpd_drv2_001-025)
Domain: rate of change of base change-point-detection features — velocity of
        structural-break statistics. Captures how rapidly CUSUM, mean-shift,
        variance-shift, and time-since-break features are changing.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def cpd_drv2_001_cusum_neg_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of |lower CUSUM| (21d) — velocity of CUSUM deterioration."""
    return _cusum_neg(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)


def cpd_drv2_002_cusum_neg_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of |lower CUSUM| (21d) — monthly velocity of CUSUM."""
    return _cusum_neg(_log_returns(close), _TD_MON).abs().diff(_TD_MON)


def cpd_drv2_003_mean_shift_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of mean-shift stat (half=21) — how rapidly break signal is changing."""
    return _mean_shift_stat(_log_returns(close), _TD_MON).diff(_TD_WEEK)


def cpd_drv2_004_mean_shift_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of mean-shift stat (half=21) — monthly velocity of break signal."""
    return _mean_shift_stat(_log_returns(close), _TD_MON).diff(_TD_MON)


def cpd_drv2_005_var_shift_abs_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of |var-shift stat| (half=21) — velocity of variance regime shift."""
    return _var_shift_stat(_log_returns(close), _TD_MON).abs().diff(_TD_WEEK)


def cpd_drv2_006_var_shift_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of signed var-shift stat (half=21) — direction of variance change."""
    return _var_shift_stat(_log_returns(close), _TD_MON).diff(_TD_WEEK)


def cpd_drv2_007_signed_shift_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of signed mean-shift (half=21) — acceleration of downward break."""
    return _mean_shift_signed(_log_returns(close), _TD_MON).diff(_TD_WEEK)


def cpd_drv2_008_cusum_neg_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of |lower CUSUM| (63d) — velocity of longer-window CUSUM."""
    return _cusum_neg(_log_returns(close), _TD_QTR).abs().diff(_TD_WEEK)


def cpd_drv2_009_mean_shift_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of mean-shift stat (half=63) — velocity of quarterly break signal."""
    return _mean_shift_stat(_log_returns(close), _TD_QTR).diff(_TD_WEEK)


def cpd_drv2_010_combined_shift_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite break score (mean+var, half=21)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    return (ms + vs).diff(_TD_WEEK)


def cpd_drv2_011_break_flag_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of break flag (half=21, thr=1.0) — entering/leaving break regime."""
    return _break_flag(_log_returns(close), _TD_MON, 1.0).diff(_TD_WEEK)


def cpd_drv2_012_time_since_break_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of time-since-break (half=21, thr=1.0) — how fast break recedes."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    tsb  = _time_since_break(flag)
    return tsb.diff(_TD_WEEK)


def cpd_drv2_013_break_count_in_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of break count in trailing 63d (half=21, thr=1)."""
    flag  = _break_flag(_log_returns(close), _TD_MON, 1.0)
    count = _rolling_sum(flag, _TD_QTR)
    return count.diff(_TD_WEEK)


def cpd_drv2_014_cusum_normalized_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of scale-normalized lower CUSUM (21d)."""
    r   = _log_returns(close)
    cs  = _cusum_neg(r, _TD_MON).abs()
    s   = _rolling_std(r, _TD_MON)
    ncs = cs / s.clip(lower=_EPS)
    return ncs.diff(_TD_WEEK)


def cpd_drv2_015_mean_shift_pct_rank_252d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of percentile rank of mean-shift stat (half=21, 252d window)."""
    ms   = _mean_shift_stat(_log_returns(close), _TD_MON)
    rank = ms.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


def cpd_drv2_016_cusum_pos_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of upper CUSUM (21d) — velocity of upward CUSUM movement."""
    return _cusum_pos(_log_returns(close), _TD_MON).diff(_TD_WEEK)


def cpd_drv2_017_break_score_composite_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite break score (mean+var+normalized CUSUM, half=21)."""
    r   = _log_returns(close)
    ms  = _mean_shift_stat(r, _TD_MON)
    vs  = _var_shift_stat(r, _TD_MON).abs()
    cs  = _cusum_neg(r, _TD_MON).abs()
    std = _rolling_std(r, _TD_MON)
    score = ms + vs + (cs / std.clip(lower=_EPS)).fillna(0.0)
    return score.diff(_TD_WEEK)


def cpd_drv2_018_ols_slope_change_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope change (21d) — rate of slope-break signal change."""
    lp  = np.log(close.clip(lower=_EPS))
    sc  = _linslope(lp, _TD_MON) - _linslope(lp, _TD_MON).shift(_TD_MON)
    return sc.diff(_TD_WEEK)


def cpd_drv2_019_before_after_return_diff_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of before/after return difference (half=21)."""
    r      = _log_returns(close)
    after  = _rolling_mean(r, _TD_MON)
    before = _rolling_mean(r, _TD_MON).shift(_TD_MON)
    diff   = after - before
    return diff.diff(_TD_WEEK)


def cpd_drv2_020_before_after_vol_diff_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of before/after volatility difference (half=21)."""
    r     = _log_returns(close)
    std_a = _rolling_std(r, _TD_MON)
    std_b = _rolling_std(r, _TD_MON).shift(_TD_MON)
    diff  = std_a - std_b
    return diff.diff(_TD_WEEK)


def cpd_drv2_021_cusum_neg_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the |lower CUSUM| (21d) — trend in CUSUM degradation."""
    return _linslope(_cusum_neg(_log_returns(close), _TD_MON).abs(), _TD_MON)


def cpd_drv2_022_mean_shift_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of mean-shift stat (half=21)."""
    return _linslope(_mean_shift_stat(_log_returns(close), _TD_MON), _TD_MON)


def cpd_drv2_023_downward_break_flag_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of downward break flag (signed shift < -1.0, half=21)."""
    flag = (_mean_shift_signed(_log_returns(close), _TD_MON) < -1.0).astype(float)
    return flag.diff(_TD_WEEK)


def cpd_drv2_024_break_density_norm_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of break density (21d fraction normalized by 252d avg fraction)."""
    flag   = _break_flag(_log_returns(close), _TD_MON, 1.0)
    frac21 = _rolling_sum(flag, _TD_MON) / _TD_MON
    avg252 = _rolling_mean(frac21, _TD_YEAR)
    dens   = frac21 / avg252.clip(lower=_EPS)
    return dens.diff(_TD_WEEK)


def cpd_drv2_025_combined_shift_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of composite break score (mean+var, half=21)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    return (ms + vs).diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

CHANGE_POINT_DETECTION_REGISTRY_2ND_DERIVATIVES = {
    "cpd_drv2_001_cusum_neg_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_001_cusum_neg_21d_5d_diff},
    "cpd_drv2_002_cusum_neg_21d_21d_diff": {"inputs": ["close"], "func": cpd_drv2_002_cusum_neg_21d_21d_diff},
    "cpd_drv2_003_mean_shift_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_003_mean_shift_21d_5d_diff},
    "cpd_drv2_004_mean_shift_21d_21d_diff": {"inputs": ["close"], "func": cpd_drv2_004_mean_shift_21d_21d_diff},
    "cpd_drv2_005_var_shift_abs_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_005_var_shift_abs_21d_5d_diff},
    "cpd_drv2_006_var_shift_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_006_var_shift_21d_5d_diff},
    "cpd_drv2_007_signed_shift_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_007_signed_shift_21d_5d_diff},
    "cpd_drv2_008_cusum_neg_63d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_008_cusum_neg_63d_5d_diff},
    "cpd_drv2_009_mean_shift_63d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_009_mean_shift_63d_5d_diff},
    "cpd_drv2_010_combined_shift_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_010_combined_shift_21d_5d_diff},
    "cpd_drv2_011_break_flag_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_011_break_flag_21d_5d_diff},
    "cpd_drv2_012_time_since_break_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_012_time_since_break_21d_5d_diff},
    "cpd_drv2_013_break_count_in_63d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_013_break_count_in_63d_5d_diff},
    "cpd_drv2_014_cusum_normalized_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_014_cusum_normalized_21d_5d_diff},
    "cpd_drv2_015_mean_shift_pct_rank_252d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_015_mean_shift_pct_rank_252d_5d_diff},
    "cpd_drv2_016_cusum_pos_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_016_cusum_pos_21d_5d_diff},
    "cpd_drv2_017_break_score_composite_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_017_break_score_composite_21d_5d_diff},
    "cpd_drv2_018_ols_slope_change_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_018_ols_slope_change_21d_5d_diff},
    "cpd_drv2_019_before_after_return_diff_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_019_before_after_return_diff_21d_5d_diff},
    "cpd_drv2_020_before_after_vol_diff_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_020_before_after_vol_diff_21d_5d_diff},
    "cpd_drv2_021_cusum_neg_21d_slope_21d": {"inputs": ["close"], "func": cpd_drv2_021_cusum_neg_21d_slope_21d},
    "cpd_drv2_022_mean_shift_21d_slope_21d": {"inputs": ["close"], "func": cpd_drv2_022_mean_shift_21d_slope_21d},
    "cpd_drv2_023_downward_break_flag_21d_5d_diff": {"inputs": ["close"], "func": cpd_drv2_023_downward_break_flag_21d_5d_diff},
    "cpd_drv2_024_break_density_norm_5d_diff": {"inputs": ["close"], "func": cpd_drv2_024_break_density_norm_5d_diff},
    "cpd_drv2_025_combined_shift_21d_21d_diff": {"inputs": ["close"], "func": cpd_drv2_025_combined_shift_21d_21d_diff},
}
