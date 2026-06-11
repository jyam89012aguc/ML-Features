"""
107_change_point_detection — Base Features 001-075
Domain: structural-break / regime-shift detection in return and price series —
        CUSUM statistics, rolling mean-shift and variance-shift detection,
        time since last detected change point, magnitude of the most recent break,
        count of breaks in trailing windows, before/after contrast around detected breaks.
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
    """Log returns of close price."""
    return np.log(close / close.shift(1))


def _cusum_pos(s: pd.Series, w: int) -> pd.Series:
    """
    Upper CUSUM statistic over a rolling window w.
    S_t = max(0, S_{t-1} + (r_t - mu_est)) where mu_est is rolling mean.
    NaN-safe: computed via rolling apply.
    """
    def _cusum_up(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu = clean.mean()
        s_val = 0.0
        for x in clean:
            s_val = max(0.0, s_val + (x - mu))
        return s_val
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_cusum_up, raw=True)


def _cusum_neg(s: pd.Series, w: int) -> pd.Series:
    """
    Lower CUSUM statistic (negative side) over rolling window w.
    S_t = min(0, S_{t-1} + (r_t - mu_est)).
    """
    def _cusum_dn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu = clean.mean()
        s_val = 0.0
        for x in clean:
            s_val = min(0.0, s_val + (x - mu))
        return s_val
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_cusum_dn, raw=True)


def _mean_shift_stat(s: pd.Series, half: int) -> pd.Series:
    """
    Rolling mean-shift test statistic: |mu_after - mu_before| / pooled_std.
    'after' = trailing half periods; 'before' = prior half periods.
    Window = 2*half.
    """
    w = 2 * half
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, half):
            return np.nan
        n = len(clean)
        mid = n // 2
        before = clean[:mid]
        after  = clean[mid:]
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return abs(after.mean() - before.mean()) / (std_all + _EPS)
    return s.rolling(w, min_periods=max(4, half)).apply(_stat, raw=True)


def _var_shift_stat(s: pd.Series, half: int) -> pd.Series:
    """
    Rolling variance-shift test statistic: log(var_after / var_before).
    """
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


def _break_flag(s: pd.Series, half: int, threshold: float) -> pd.Series:
    """Binary: mean-shift stat exceeds threshold (a break is detected)."""
    return (_mean_shift_stat(s, half) > threshold).astype(float)


def _time_since_break(flag: pd.Series) -> pd.Series:
    """Days since last detected break (flag==1). 0 on the break day."""
    idx = pd.Series(range(len(flag)), index=flag.index, dtype=float)
    last = idx.where(flag == 1.0).ffill()
    elapsed = idx - last
    return elapsed.where(last.notna(), np.nan)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): CUSUM on log-returns, multiple windows ---

def cpd_001_cusum_pos_21d(close: pd.Series) -> pd.Series:
    """Upper CUSUM statistic on log-returns over trailing 21-day window."""
    return _cusum_pos(_log_returns(close), _TD_MON)


def cpd_002_cusum_neg_21d(close: pd.Series) -> pd.Series:
    """Lower CUSUM statistic (negative side) on log-returns, 21-day window."""
    return _cusum_neg(_log_returns(close), _TD_MON)


def cpd_003_cusum_pos_63d(close: pd.Series) -> pd.Series:
    """Upper CUSUM statistic on log-returns over trailing 63-day window."""
    return _cusum_pos(_log_returns(close), _TD_QTR)


def cpd_004_cusum_neg_63d(close: pd.Series) -> pd.Series:
    """Lower CUSUM statistic on log-returns, 63-day window."""
    return _cusum_neg(_log_returns(close), _TD_QTR)


def cpd_005_cusum_pos_126d(close: pd.Series) -> pd.Series:
    """Upper CUSUM statistic on log-returns over 126-day window."""
    return _cusum_pos(_log_returns(close), _TD_HALF)


def cpd_006_cusum_neg_126d(close: pd.Series) -> pd.Series:
    """Lower CUSUM statistic on log-returns, 126-day window."""
    return _cusum_neg(_log_returns(close), _TD_HALF)


def cpd_007_cusum_abs_max_21d(close: pd.Series) -> pd.Series:
    """Max(|upper CUSUM|, |lower CUSUM|) on 21-day log-returns — two-sided magnitude."""
    pos = _cusum_pos(_log_returns(close), _TD_MON).abs()
    neg = _cusum_neg(_log_returns(close), _TD_MON).abs()
    return pos.combine(neg, max)


def cpd_008_cusum_abs_max_63d(close: pd.Series) -> pd.Series:
    """Max(|upper CUSUM|, |lower CUSUM|) on 63-day log-returns."""
    pos = _cusum_pos(_log_returns(close), _TD_QTR).abs()
    neg = _cusum_neg(_log_returns(close), _TD_QTR).abs()
    return pos.combine(neg, max)


def cpd_009_cusum_pos_5d(close: pd.Series) -> pd.Series:
    """Upper CUSUM statistic on log-returns over 5-day window (fast detection)."""
    return _cusum_pos(_log_returns(close), _TD_WEEK)


def cpd_010_cusum_neg_5d(close: pd.Series) -> pd.Series:
    """Lower CUSUM statistic on log-returns, 5-day window."""
    return _cusum_neg(_log_returns(close), _TD_WEEK)


# --- Group B (011-020): Mean-shift detection statistics ---

def cpd_011_mean_shift_stat_10d(close: pd.Series) -> pd.Series:
    """Mean-shift test statistic with half=10 (split 20-day window at midpoint)."""
    return _mean_shift_stat(_log_returns(close), 10)


def cpd_012_mean_shift_stat_21d(close: pd.Series) -> pd.Series:
    """Mean-shift test statistic with half=21 (42-day split window)."""
    return _mean_shift_stat(_log_returns(close), _TD_MON)


def cpd_013_mean_shift_stat_63d(close: pd.Series) -> pd.Series:
    """Mean-shift test statistic with half=63 (126-day split window)."""
    return _mean_shift_stat(_log_returns(close), _TD_QTR)


def cpd_014_mean_shift_stat_5d(close: pd.Series) -> pd.Series:
    """Mean-shift test statistic with half=5 (10-day split window, fast)."""
    return _mean_shift_stat(_log_returns(close), _TD_WEEK)


def cpd_015_mean_shift_stat_price_21d(close: pd.Series) -> pd.Series:
    """Mean-shift stat on raw log-price (not returns) with half=21."""
    return _mean_shift_stat(np.log(close.clip(lower=_EPS)), _TD_MON)


def cpd_016_mean_shift_stat_price_63d(close: pd.Series) -> pd.Series:
    """Mean-shift stat on raw log-price with half=63."""
    return _mean_shift_stat(np.log(close.clip(lower=_EPS)), _TD_QTR)


def cpd_017_mean_shift_signed_21d(close: pd.Series) -> pd.Series:
    """Signed mean-shift: (mu_after - mu_before) / std, half=21. Negative = downshift."""
    w = 2 * _TD_MON
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_MON):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return (clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return _log_returns(close).rolling(w, min_periods=max(4, _TD_MON)).apply(_stat, raw=True)


def cpd_018_mean_shift_signed_63d(close: pd.Series) -> pd.Series:
    """Signed mean-shift stat with half=63 — longer horizon down-shift detection."""
    w = 2 * _TD_QTR
    def _stat(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < max(4, _TD_QTR):
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        return (clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
    return _log_returns(close).rolling(w, min_periods=max(4, _TD_QTR)).apply(_stat, raw=True)


def cpd_019_mean_shift_stat_absret_21d(close: pd.Series) -> pd.Series:
    """Mean-shift stat on absolute log-returns (volatility-regime shift) half=21."""
    return _mean_shift_stat(_log_returns(close).abs(), _TD_MON)


def cpd_020_mean_shift_stat_absret_63d(close: pd.Series) -> pd.Series:
    """Mean-shift stat on absolute log-returns half=63."""
    return _mean_shift_stat(_log_returns(close).abs(), _TD_QTR)


# --- Group C (021-030): Variance-shift detection ---

def cpd_021_var_shift_stat_10d(close: pd.Series) -> pd.Series:
    """Log-variance-ratio shift statistic, half=10 (20-day split)."""
    return _var_shift_stat(_log_returns(close), 10)


def cpd_022_var_shift_stat_21d(close: pd.Series) -> pd.Series:
    """Log-variance-ratio shift statistic, half=21."""
    return _var_shift_stat(_log_returns(close), _TD_MON)


def cpd_023_var_shift_stat_63d(close: pd.Series) -> pd.Series:
    """Log-variance-ratio shift statistic, half=63."""
    return _var_shift_stat(_log_returns(close), _TD_QTR)


def cpd_024_var_shift_pos_21d(close: pd.Series) -> pd.Series:
    """Positive variance shift (variance increased in 2nd half), half=21."""
    return _var_shift_stat(_log_returns(close), _TD_MON).clip(lower=0.0)


def cpd_025_var_shift_neg_21d(close: pd.Series) -> pd.Series:
    """Negative variance shift (variance fell in 2nd half, volatility collapse), half=21."""
    return (-_var_shift_stat(_log_returns(close), _TD_MON)).clip(lower=0.0)


def cpd_026_var_shift_stat_5d(close: pd.Series) -> pd.Series:
    """Log-variance-ratio shift statistic, half=5 (10-day split, fast)."""
    return _var_shift_stat(_log_returns(close), _TD_WEEK)


def cpd_027_var_shift_stat_price_21d(close: pd.Series) -> pd.Series:
    """Variance-shift stat on log-price series, half=21."""
    return _var_shift_stat(np.log(close.clip(lower=_EPS)), _TD_MON)


def cpd_028_var_shift_abs_21d(close: pd.Series) -> pd.Series:
    """Absolute variance-shift magnitude, half=21."""
    return _var_shift_stat(_log_returns(close), _TD_MON).abs()


def cpd_029_var_shift_abs_63d(close: pd.Series) -> pd.Series:
    """Absolute variance-shift magnitude, half=63."""
    return _var_shift_stat(_log_returns(close), _TD_QTR).abs()


def cpd_030_combined_shift_stat_21d(close: pd.Series) -> pd.Series:
    """Sum of mean-shift and variance-shift magnitudes, half=21 (composite break score)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    return ms + vs


# --- Group D (031-040): Binary break flags ---

def cpd_031_break_flag_10d_thr1(close: pd.Series) -> pd.Series:
    """Binary: mean-shift stat (half=10) exceeds threshold 1.0."""
    return _break_flag(_log_returns(close), 10, 1.0)


def cpd_032_break_flag_21d_thr1(close: pd.Series) -> pd.Series:
    """Binary: mean-shift stat (half=21) exceeds threshold 1.0."""
    return _break_flag(_log_returns(close), _TD_MON, 1.0)


def cpd_033_break_flag_21d_thr2(close: pd.Series) -> pd.Series:
    """Binary: mean-shift stat (half=21) exceeds threshold 2.0 (strong break)."""
    return _break_flag(_log_returns(close), _TD_MON, 2.0)


def cpd_034_break_flag_63d_thr1(close: pd.Series) -> pd.Series:
    """Binary: mean-shift stat (half=63) exceeds threshold 1.0."""
    return _break_flag(_log_returns(close), _TD_QTR, 1.0)


def cpd_035_cusum_break_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: |lower CUSUM| on 21-day returns exceeds 2x rolling std of returns."""
    r = _log_returns(close)
    cusum_dn = _cusum_neg(r, _TD_MON).abs()
    threshold = _rolling_std(r, _TD_MON) * 2.0
    return (cusum_dn > threshold.clip(lower=_EPS)).astype(float)


def cpd_036_cusum_break_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: |lower CUSUM| on 63-day returns exceeds 2x rolling std."""
    r = _log_returns(close)
    cusum_dn = _cusum_neg(r, _TD_QTR).abs()
    threshold = _rolling_std(r, _TD_QTR) * 2.0
    return (cusum_dn > threshold.clip(lower=_EPS)).astype(float)


def cpd_037_var_break_flag_21d_thr05(close: pd.Series) -> pd.Series:
    """Binary: absolute var-shift stat (half=21) > 0.5 (moderate variance break)."""
    return (_var_shift_stat(_log_returns(close), _TD_MON).abs() > 0.5).astype(float)


def cpd_038_var_break_flag_21d_thr1(close: pd.Series) -> pd.Series:
    """Binary: absolute var-shift stat (half=21) > 1.0 (strong variance break)."""
    return (_var_shift_stat(_log_returns(close), _TD_MON).abs() > 1.0).astype(float)


def cpd_039_combined_break_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: combined shift stat (half=21) > 2.0 (composite break)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    return ((ms + vs) > 2.0).astype(float)


def cpd_040_downward_break_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: signed mean-shift (half=21) < -1.0 (downward regime shift)."""
    return (cpd_017_mean_shift_signed_21d(close) < -1.0).astype(float)


# --- Group E (041-050): Time since last break ---

def cpd_041_time_since_break_10d_thr1(close: pd.Series) -> pd.Series:
    """Days since last mean-shift break (half=10, threshold=1.0)."""
    flag = _break_flag(_log_returns(close), 10, 1.0)
    return _time_since_break(flag)


def cpd_042_time_since_break_21d_thr1(close: pd.Series) -> pd.Series:
    """Days since last mean-shift break (half=21, threshold=1.0)."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    return _time_since_break(flag)


def cpd_043_time_since_break_21d_thr2(close: pd.Series) -> pd.Series:
    """Days since last strong mean-shift break (half=21, threshold=2.0)."""
    flag = _break_flag(_log_returns(close), _TD_MON, 2.0)
    return _time_since_break(flag)


def cpd_044_time_since_cusum_break_21d(close: pd.Series) -> pd.Series:
    """Days since last CUSUM-detected break on 21-day window."""
    flag = cpd_035_cusum_break_flag_21d(close)
    return _time_since_break(flag)


def cpd_045_time_since_cusum_break_63d(close: pd.Series) -> pd.Series:
    """Days since last CUSUM-detected break on 63-day window."""
    flag = cpd_036_cusum_break_flag_63d(close)
    return _time_since_break(flag)


def cpd_046_time_since_var_break_21d(close: pd.Series) -> pd.Series:
    """Days since last variance-shift break (half=21, threshold=0.5)."""
    flag = cpd_037_var_break_flag_21d_thr05(close)
    return _time_since_break(flag)


def cpd_047_time_since_downward_break_21d(close: pd.Series) -> pd.Series:
    """Days since last downward regime break (signed shift < -1.0, half=21)."""
    flag = cpd_040_downward_break_flag_21d(close)
    return _time_since_break(flag)


def cpd_048_time_since_break_63d_thr1(close: pd.Series) -> pd.Series:
    """Days since last mean-shift break (half=63, threshold=1.0)."""
    flag = _break_flag(_log_returns(close), _TD_QTR, 1.0)
    return _time_since_break(flag)


def cpd_049_time_since_combined_break_21d(close: pd.Series) -> pd.Series:
    """Days since last combined (mean+variance) break (half=21) > 2.0."""
    flag = cpd_039_combined_break_flag_21d(close)
    return _time_since_break(flag)


def cpd_050_time_since_var_break_21d_thr1(close: pd.Series) -> pd.Series:
    """Days since last strong variance-shift break (half=21, threshold=1.0)."""
    flag = cpd_038_var_break_flag_21d_thr1(close)
    return _time_since_break(flag)


# --- Group F (051-060): Break magnitude (how large was the most recent break) ---

def cpd_051_break_magnitude_mean_21d(close: pd.Series) -> pd.Series:
    """Magnitude of mean-shift stat at most recent break (half=21, thr=1.0)."""
    stat = _mean_shift_stat(_log_returns(close), _TD_MON)
    flag = (stat > 1.0).astype(float)
    return stat.where(flag == 1.0).ffill().fillna(0.0)


def cpd_052_break_magnitude_var_21d(close: pd.Series) -> pd.Series:
    """Magnitude of var-shift stat at most recent break (half=21, thr=0.5)."""
    stat = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    flag = (stat > 0.5).astype(float)
    return stat.where(flag == 1.0).ffill().fillna(0.0)


def cpd_053_break_magnitude_cusum_21d(close: pd.Series) -> pd.Series:
    """Magnitude of |CUSUM lower| at most recent CUSUM break (21-day window)."""
    r = _log_returns(close)
    cusum_mag = _cusum_neg(r, _TD_MON).abs()
    threshold = _rolling_std(r, _TD_MON) * 2.0
    flag = (cusum_mag > threshold.clip(lower=_EPS)).astype(float)
    return cusum_mag.where(flag == 1.0).ffill().fillna(0.0)


def cpd_054_break_magnitude_cusum_63d(close: pd.Series) -> pd.Series:
    """Magnitude of |CUSUM lower| at most recent CUSUM break (63-day window)."""
    r = _log_returns(close)
    cusum_mag = _cusum_neg(r, _TD_QTR).abs()
    threshold = _rolling_std(r, _TD_QTR) * 2.0
    flag = (cusum_mag > threshold.clip(lower=_EPS)).astype(float)
    return cusum_mag.where(flag == 1.0).ffill().fillna(0.0)


def cpd_055_break_signed_magnitude_21d(close: pd.Series) -> pd.Series:
    """Signed mean-shift magnitude at most recent break (half=21), negative=downward."""
    stat = cpd_017_mean_shift_signed_21d(close)
    flag = (stat.abs() > 1.0).astype(float)
    return stat.where(flag == 1.0).ffill().fillna(0.0)


def cpd_056_break_magnitude_combined_21d(close: pd.Series) -> pd.Series:
    """Combined magnitude (mean+var) at most recent combined break (half=21)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    combined = ms + vs
    flag = (combined > 2.0).astype(float)
    return combined.where(flag == 1.0).ffill().fillna(0.0)


def cpd_057_cusum_pos_max_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day maximum of the upper CUSUM statistic on log-returns."""
    return _rolling_max(_cusum_pos(_log_returns(close), _TD_MON), _TD_MON)


def cpd_058_cusum_neg_max_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day maximum of |lower CUSUM| (peak negative CUSUM magnitude)."""
    return _rolling_max(_cusum_neg(_log_returns(close), _TD_MON).abs(), _TD_MON)


def cpd_059_break_depth_return_21d(close: pd.Series) -> pd.Series:
    """
    At each mean-shift break (half=21,thr=1), the absolute difference in
    rolling-mean returns before vs after. Held forward until next break.
    """
    r = _log_returns(close)
    ms = _mean_shift_stat(r, _TD_MON)
    flag = (ms > 1.0).astype(float)
    m_before = _rolling_mean(r, _TD_MON).shift(_TD_MON)
    m_after  = _rolling_mean(r, _TD_MON)
    diff = (m_after - m_before).abs()
    return diff.where(flag == 1.0).ffill().fillna(0.0)


def cpd_060_break_depth_vol_21d(close: pd.Series) -> pd.Series:
    """
    At each variance break (half=21, thr=0.5), the difference in rolling std
    after vs before. Held forward until next break.
    """
    r = _log_returns(close)
    vs = _var_shift_stat(r, _TD_MON).abs()
    flag = (vs > 0.5).astype(float)
    std_before = _rolling_std(r, _TD_MON).shift(_TD_MON)
    std_after  = _rolling_std(r, _TD_MON)
    diff = (std_after - std_before).abs()
    return diff.where(flag == 1.0).ffill().fillna(0.0)


# --- Group G (061-075): Break count in trailing windows ---

def cpd_061_break_count_21d_in_63d(close: pd.Series) -> pd.Series:
    """Count of mean-shift breaks (half=21, thr=1) in trailing 63-day window."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    return _rolling_sum(flag, _TD_QTR)


def cpd_062_break_count_21d_in_126d(close: pd.Series) -> pd.Series:
    """Count of mean-shift breaks (half=21, thr=1) in trailing 126-day window."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    return _rolling_sum(flag, _TD_HALF)


def cpd_063_break_count_21d_in_252d(close: pd.Series) -> pd.Series:
    """Count of mean-shift breaks (half=21, thr=1) in trailing 252-day window."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    return _rolling_sum(flag, _TD_YEAR)


def cpd_064_cusum_break_count_21d_in_63d(close: pd.Series) -> pd.Series:
    """Count of CUSUM breaks (21-day) in trailing 63-day window."""
    flag = cpd_035_cusum_break_flag_21d(close)
    return _rolling_sum(flag, _TD_QTR)


def cpd_065_cusum_break_count_21d_in_252d(close: pd.Series) -> pd.Series:
    """Count of CUSUM breaks (21-day) in trailing 252-day window."""
    flag = cpd_035_cusum_break_flag_21d(close)
    return _rolling_sum(flag, _TD_YEAR)


def cpd_066_var_break_count_21d_in_63d(close: pd.Series) -> pd.Series:
    """Count of variance-shift breaks (half=21, thr=0.5) in trailing 63-day window."""
    flag = cpd_037_var_break_flag_21d_thr05(close)
    return _rolling_sum(flag, _TD_QTR)


def cpd_067_var_break_count_21d_in_252d(close: pd.Series) -> pd.Series:
    """Count of variance-shift breaks (half=21, thr=0.5) in trailing 252-day window."""
    flag = cpd_037_var_break_flag_21d_thr05(close)
    return _rolling_sum(flag, _TD_YEAR)


def cpd_068_downward_break_count_21d_in_126d(close: pd.Series) -> pd.Series:
    """Count of downward regime breaks (half=21) in trailing 126-day window."""
    flag = cpd_040_downward_break_flag_21d(close)
    return _rolling_sum(flag, _TD_HALF)


def cpd_069_downward_break_count_21d_in_252d(close: pd.Series) -> pd.Series:
    """Count of downward regime breaks (half=21) in trailing 252-day window."""
    flag = cpd_040_downward_break_flag_21d(close)
    return _rolling_sum(flag, _TD_YEAR)


def cpd_070_combined_break_count_21d_in_63d(close: pd.Series) -> pd.Series:
    """Count of combined (mean+var) breaks (half=21) in trailing 63-day window."""
    flag = cpd_039_combined_break_flag_21d(close)
    return _rolling_sum(flag, _TD_QTR)


def cpd_071_break_fraction_21d_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where mean-shift break (half=21, thr=1) occurred."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


def cpd_072_break_fraction_21d_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where mean-shift break (half=21, thr=1) occurred."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def cpd_073_consec_break_days_21d(close: pd.Series) -> pd.Series:
    """Consecutive days of detected mean-shift break (half=21, thr=1.0) streak."""
    return _consec_streak(_break_flag(_log_returns(close), _TD_MON, 1.0) == 1.0)


def cpd_074_cusum_break_consec_21d(close: pd.Series) -> pd.Series:
    """Consecutive days of CUSUM-detected break (21-day window)."""
    return _consec_streak(cpd_035_cusum_break_flag_21d(close) == 1.0)


def cpd_075_break_density_21d_norm252d(close: pd.Series) -> pd.Series:
    """21-day break fraction normalized by 252-day average break fraction."""
    flag = _break_flag(_log_returns(close), _TD_MON, 1.0)
    frac21  = _rolling_sum(flag, _TD_MON) / _TD_MON
    avg252  = _rolling_mean(frac21, _TD_YEAR)
    return _safe_div(frac21, avg252.clip(lower=_EPS))


# ── Registry ──────────────────────────────────────────────────────────────────

CHANGE_POINT_DETECTION_REGISTRY_001_075 = {
    "cpd_001_cusum_pos_21d": {"inputs": ["close"], "func": cpd_001_cusum_pos_21d},
    "cpd_002_cusum_neg_21d": {"inputs": ["close"], "func": cpd_002_cusum_neg_21d},
    "cpd_003_cusum_pos_63d": {"inputs": ["close"], "func": cpd_003_cusum_pos_63d},
    "cpd_004_cusum_neg_63d": {"inputs": ["close"], "func": cpd_004_cusum_neg_63d},
    "cpd_005_cusum_pos_126d": {"inputs": ["close"], "func": cpd_005_cusum_pos_126d},
    "cpd_006_cusum_neg_126d": {"inputs": ["close"], "func": cpd_006_cusum_neg_126d},
    "cpd_007_cusum_abs_max_21d": {"inputs": ["close"], "func": cpd_007_cusum_abs_max_21d},
    "cpd_008_cusum_abs_max_63d": {"inputs": ["close"], "func": cpd_008_cusum_abs_max_63d},
    "cpd_009_cusum_pos_5d": {"inputs": ["close"], "func": cpd_009_cusum_pos_5d},
    "cpd_010_cusum_neg_5d": {"inputs": ["close"], "func": cpd_010_cusum_neg_5d},
    "cpd_011_mean_shift_stat_10d": {"inputs": ["close"], "func": cpd_011_mean_shift_stat_10d},
    "cpd_012_mean_shift_stat_21d": {"inputs": ["close"], "func": cpd_012_mean_shift_stat_21d},
    "cpd_013_mean_shift_stat_63d": {"inputs": ["close"], "func": cpd_013_mean_shift_stat_63d},
    "cpd_014_mean_shift_stat_5d": {"inputs": ["close"], "func": cpd_014_mean_shift_stat_5d},
    "cpd_015_mean_shift_stat_price_21d": {"inputs": ["close"], "func": cpd_015_mean_shift_stat_price_21d},
    "cpd_016_mean_shift_stat_price_63d": {"inputs": ["close"], "func": cpd_016_mean_shift_stat_price_63d},
    "cpd_017_mean_shift_signed_21d": {"inputs": ["close"], "func": cpd_017_mean_shift_signed_21d},
    "cpd_018_mean_shift_signed_63d": {"inputs": ["close"], "func": cpd_018_mean_shift_signed_63d},
    "cpd_019_mean_shift_stat_absret_21d": {"inputs": ["close"], "func": cpd_019_mean_shift_stat_absret_21d},
    "cpd_020_mean_shift_stat_absret_63d": {"inputs": ["close"], "func": cpd_020_mean_shift_stat_absret_63d},
    "cpd_021_var_shift_stat_10d": {"inputs": ["close"], "func": cpd_021_var_shift_stat_10d},
    "cpd_022_var_shift_stat_21d": {"inputs": ["close"], "func": cpd_022_var_shift_stat_21d},
    "cpd_023_var_shift_stat_63d": {"inputs": ["close"], "func": cpd_023_var_shift_stat_63d},
    "cpd_024_var_shift_pos_21d": {"inputs": ["close"], "func": cpd_024_var_shift_pos_21d},
    "cpd_025_var_shift_neg_21d": {"inputs": ["close"], "func": cpd_025_var_shift_neg_21d},
    "cpd_026_var_shift_stat_5d": {"inputs": ["close"], "func": cpd_026_var_shift_stat_5d},
    "cpd_027_var_shift_stat_price_21d": {"inputs": ["close"], "func": cpd_027_var_shift_stat_price_21d},
    "cpd_028_var_shift_abs_21d": {"inputs": ["close"], "func": cpd_028_var_shift_abs_21d},
    "cpd_029_var_shift_abs_63d": {"inputs": ["close"], "func": cpd_029_var_shift_abs_63d},
    "cpd_030_combined_shift_stat_21d": {"inputs": ["close"], "func": cpd_030_combined_shift_stat_21d},
    "cpd_031_break_flag_10d_thr1": {"inputs": ["close"], "func": cpd_031_break_flag_10d_thr1},
    "cpd_032_break_flag_21d_thr1": {"inputs": ["close"], "func": cpd_032_break_flag_21d_thr1},
    "cpd_033_break_flag_21d_thr2": {"inputs": ["close"], "func": cpd_033_break_flag_21d_thr2},
    "cpd_034_break_flag_63d_thr1": {"inputs": ["close"], "func": cpd_034_break_flag_63d_thr1},
    "cpd_035_cusum_break_flag_21d": {"inputs": ["close"], "func": cpd_035_cusum_break_flag_21d},
    "cpd_036_cusum_break_flag_63d": {"inputs": ["close"], "func": cpd_036_cusum_break_flag_63d},
    "cpd_037_var_break_flag_21d_thr05": {"inputs": ["close"], "func": cpd_037_var_break_flag_21d_thr05},
    "cpd_038_var_break_flag_21d_thr1": {"inputs": ["close"], "func": cpd_038_var_break_flag_21d_thr1},
    "cpd_039_combined_break_flag_21d": {"inputs": ["close"], "func": cpd_039_combined_break_flag_21d},
    "cpd_040_downward_break_flag_21d": {"inputs": ["close"], "func": cpd_040_downward_break_flag_21d},
    "cpd_041_time_since_break_10d_thr1": {"inputs": ["close"], "func": cpd_041_time_since_break_10d_thr1},
    "cpd_042_time_since_break_21d_thr1": {"inputs": ["close"], "func": cpd_042_time_since_break_21d_thr1},
    "cpd_043_time_since_break_21d_thr2": {"inputs": ["close"], "func": cpd_043_time_since_break_21d_thr2},
    "cpd_044_time_since_cusum_break_21d": {"inputs": ["close"], "func": cpd_044_time_since_cusum_break_21d},
    "cpd_045_time_since_cusum_break_63d": {"inputs": ["close"], "func": cpd_045_time_since_cusum_break_63d},
    "cpd_046_time_since_var_break_21d": {"inputs": ["close"], "func": cpd_046_time_since_var_break_21d},
    "cpd_047_time_since_downward_break_21d": {"inputs": ["close"], "func": cpd_047_time_since_downward_break_21d},
    "cpd_048_time_since_break_63d_thr1": {"inputs": ["close"], "func": cpd_048_time_since_break_63d_thr1},
    "cpd_049_time_since_combined_break_21d": {"inputs": ["close"], "func": cpd_049_time_since_combined_break_21d},
    "cpd_050_time_since_var_break_21d_thr1": {"inputs": ["close"], "func": cpd_050_time_since_var_break_21d_thr1},
    "cpd_051_break_magnitude_mean_21d": {"inputs": ["close"], "func": cpd_051_break_magnitude_mean_21d},
    "cpd_052_break_magnitude_var_21d": {"inputs": ["close"], "func": cpd_052_break_magnitude_var_21d},
    "cpd_053_break_magnitude_cusum_21d": {"inputs": ["close"], "func": cpd_053_break_magnitude_cusum_21d},
    "cpd_054_break_magnitude_cusum_63d": {"inputs": ["close"], "func": cpd_054_break_magnitude_cusum_63d},
    "cpd_055_break_signed_magnitude_21d": {"inputs": ["close"], "func": cpd_055_break_signed_magnitude_21d},
    "cpd_056_break_magnitude_combined_21d": {"inputs": ["close"], "func": cpd_056_break_magnitude_combined_21d},
    "cpd_057_cusum_pos_max_21d": {"inputs": ["close"], "func": cpd_057_cusum_pos_max_21d},
    "cpd_058_cusum_neg_max_21d": {"inputs": ["close"], "func": cpd_058_cusum_neg_max_21d},
    "cpd_059_break_depth_return_21d": {"inputs": ["close"], "func": cpd_059_break_depth_return_21d},
    "cpd_060_break_depth_vol_21d": {"inputs": ["close"], "func": cpd_060_break_depth_vol_21d},
    "cpd_061_break_count_21d_in_63d": {"inputs": ["close"], "func": cpd_061_break_count_21d_in_63d},
    "cpd_062_break_count_21d_in_126d": {"inputs": ["close"], "func": cpd_062_break_count_21d_in_126d},
    "cpd_063_break_count_21d_in_252d": {"inputs": ["close"], "func": cpd_063_break_count_21d_in_252d},
    "cpd_064_cusum_break_count_21d_in_63d": {"inputs": ["close"], "func": cpd_064_cusum_break_count_21d_in_63d},
    "cpd_065_cusum_break_count_21d_in_252d": {"inputs": ["close"], "func": cpd_065_cusum_break_count_21d_in_252d},
    "cpd_066_var_break_count_21d_in_63d": {"inputs": ["close"], "func": cpd_066_var_break_count_21d_in_63d},
    "cpd_067_var_break_count_21d_in_252d": {"inputs": ["close"], "func": cpd_067_var_break_count_21d_in_252d},
    "cpd_068_downward_break_count_21d_in_126d": {"inputs": ["close"], "func": cpd_068_downward_break_count_21d_in_126d},
    "cpd_069_downward_break_count_21d_in_252d": {"inputs": ["close"], "func": cpd_069_downward_break_count_21d_in_252d},
    "cpd_070_combined_break_count_21d_in_63d": {"inputs": ["close"], "func": cpd_070_combined_break_count_21d_in_63d},
    "cpd_071_break_fraction_21d_in_63d": {"inputs": ["close"], "func": cpd_071_break_fraction_21d_in_63d},
    "cpd_072_break_fraction_21d_in_252d": {"inputs": ["close"], "func": cpd_072_break_fraction_21d_in_252d},
    "cpd_073_consec_break_days_21d": {"inputs": ["close"], "func": cpd_073_consec_break_days_21d},
    "cpd_074_cusum_break_consec_21d": {"inputs": ["close"], "func": cpd_074_cusum_break_consec_21d},
    "cpd_075_break_density_21d_norm252d": {"inputs": ["close"], "func": cpd_075_break_density_21d_norm252d},
}
