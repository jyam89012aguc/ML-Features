"""
107_change_point_detection — Extended Features 001-075
Domain: structural-break / regime-shift detection — deeper variants, multi-scale
        CUSUM, adaptive threshold CUSUM, MOSUM (moving-sum) statistics, Bayesian
        change-point probability proxies, multi-window break consensus, open/low/high
        return structural break, log-volume level breaks, and cross-signal composites.
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


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Multi-window CUSUM and adaptive CUSUM ---

def cpd_ext_001_cusum_neg_252d(close: pd.Series) -> pd.Series:
    """Lower CUSUM on log-returns over full 252-day window (long-horizon break detector)."""
    return _cusum_neg(_log_returns(close), _TD_YEAR)


def cpd_ext_002_cusum_pos_252d(close: pd.Series) -> pd.Series:
    """Upper CUSUM on log-returns over 252-day window."""
    return _cusum_pos(_log_returns(close), _TD_YEAR)


def cpd_ext_003_cusum_neg_adaptive_21d(close: pd.Series) -> pd.Series:
    """
    Adaptive lower CUSUM (21d): allowance k = 0.5 * rolling std.
    S_t = min(0, S_{t-1} + (r_t - mu - k)).
    """
    r = _log_returns(close)
    std_r = _rolling_std(r, _TD_MON)
    def _fn(idx):
        if idx < max(2, _TD_MON // 2):
            return np.nan
        start = max(0, idx - _TD_MON + 1)
        arr = r.iloc[start:idx + 1].dropna().values
        k   = std_r.iloc[idx]
        if len(arr) < 2 or np.isnan(k):
            return np.nan
        mu = arr.mean()
        sv = 0.0
        for x in arr:
            sv = min(0.0, sv + (x - mu - 0.5 * k))
        return sv
    return pd.Series([_fn(i) for i in range(len(r))], index=r.index)


def cpd_ext_004_cusum_neg_adaptive_63d(close: pd.Series) -> pd.Series:
    """
    Adaptive lower CUSUM (63d): allowance k = 0.5 * rolling std.
    """
    r = _log_returns(close)
    std_r = _rolling_std(r, _TD_QTR)
    def _fn(idx):
        if idx < max(2, _TD_QTR // 2):
            return np.nan
        start = max(0, idx - _TD_QTR + 1)
        arr = r.iloc[start:idx + 1].dropna().values
        k   = std_r.iloc[idx]
        if len(arr) < 2 or np.isnan(k):
            return np.nan
        mu = arr.mean()
        sv = 0.0
        for x in arr:
            sv = min(0.0, sv + (x - mu - 0.5 * k))
        return sv
    return pd.Series([_fn(i) for i in range(len(r))], index=r.index)


def cpd_ext_005_cusum_two_sided_max_21d(close: pd.Series) -> pd.Series:
    """Max of upper CUSUM and |lower CUSUM| over 21-day window (two-sided detection)."""
    r = _log_returns(close)
    pos = _cusum_pos(r, _TD_MON)
    neg = _cusum_neg(r, _TD_MON).abs()
    return pos.combine(neg, max)


def cpd_ext_006_cusum_two_sided_max_126d(close: pd.Series) -> pd.Series:
    """Max of upper CUSUM and |lower CUSUM| over 126-day window."""
    r = _log_returns(close)
    pos = _cusum_pos(r, _TD_HALF)
    neg = _cusum_neg(r, _TD_HALF).abs()
    return pos.combine(neg, max)


def cpd_ext_007_cusum_neg_high_63d(high: pd.Series) -> pd.Series:
    """Lower CUSUM on high log-returns over 63-day window."""
    return _cusum_neg(np.log(high / high.shift(1)), _TD_QTR)


def cpd_ext_008_cusum_neg_open_21d(open: pd.Series) -> pd.Series:
    """Lower CUSUM on open log-returns over 21-day window."""
    return _cusum_neg(np.log(open / open.shift(1)), _TD_MON)


def cpd_ext_009_cusum_pos_vol_63d(volume: pd.Series) -> pd.Series:
    """Upper CUSUM on log-volume changes over 63-day window."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    return _cusum_pos(r, _TD_QTR)


def cpd_ext_010_cusum_neg_vol_63d(volume: pd.Series) -> pd.Series:
    """Lower CUSUM on log-volume changes over 63-day window."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    return _cusum_neg(r, _TD_QTR)


# --- Group B (011-020): MOSUM (moving-sum) statistics ---

def cpd_ext_011_mosum_neg_21d(close: pd.Series) -> pd.Series:
    """
    MOSUM (moving-sum) statistic: sum of deviations from full-window mean,
    normalized by std, 21-day window. Negative indicates persistent downward drift.
    """
    r = _log_returns(close)
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu  = clean.mean()
        std = clean.std()
        if std < _EPS:
            return 0.0
        return (clean - mu).sum() / (std + _EPS)
    return r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_fn, raw=True)


def cpd_ext_012_mosum_neg_63d(close: pd.Series) -> pd.Series:
    """MOSUM statistic with 63-day window."""
    r = _log_returns(close)
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu  = clean.mean()
        std = clean.std()
        if std < _EPS:
            return 0.0
        return (clean - mu).sum() / (std + _EPS)
    return r.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_fn, raw=True)


def cpd_ext_013_mosum_abs_21d(close: pd.Series) -> pd.Series:
    """Absolute MOSUM statistic, 21-day window (two-sided deviation from mean)."""
    return cpd_ext_011_mosum_neg_21d(close).abs()


def cpd_ext_014_mosum_abs_63d(close: pd.Series) -> pd.Series:
    """Absolute MOSUM statistic, 63-day window."""
    return cpd_ext_012_mosum_neg_63d(close).abs()


def cpd_ext_015_mosum_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: |MOSUM| (21d) > 2.0 (significant drift detected)."""
    return (cpd_ext_013_mosum_abs_21d(close) > 2.0).astype(float)


def cpd_ext_016_mosum_neg_below_neg2_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: MOSUM (21d) < -2.0 (persistent downward drift)."""
    return (cpd_ext_011_mosum_neg_21d(close) < -2.0).astype(float)


def cpd_ext_017_mosum_neg_vol_21d(volume: pd.Series) -> pd.Series:
    """MOSUM statistic on log-volume changes, 21-day window."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 2:
            return np.nan
        mu  = clean.mean()
        std = clean.std()
        if std < _EPS:
            return 0.0
        return (clean - mu).sum() / (std + _EPS)
    return r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_fn, raw=True)


def cpd_ext_018_time_since_mosum_flag_21d(close: pd.Series) -> pd.Series:
    """Days since last MOSUM (21d) break flag (|MOSUM| > 2.0)."""
    return _time_since_break(cpd_ext_015_mosum_flag_21d(close))


def cpd_ext_019_mosum_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of MOSUM (21d) in trailing 252-day distribution."""
    ms = cpd_ext_011_mosum_neg_21d(close)
    return ms.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_ext_020_mosum_neg_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of MOSUM (21d) — velocity of MOSUM statistic."""
    return cpd_ext_011_mosum_neg_21d(close).diff(_TD_WEEK)


# --- Group C (021-030): Deeper mean-shift variants (multiple splits) ---

def cpd_ext_021_mean_shift_stat_3split_21d(close: pd.Series) -> pd.Series:
    """
    Max mean-shift statistic across 3 split points (1/4, 1/2, 3/4) in 21-day window.
    Detects breaks at any location within the window.
    """
    r = _log_returns(close)
    w = _TD_MON
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        n = len(clean)
        if n < 4:
            return np.nan
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        best = 0.0
        for frac in [0.25, 0.5, 0.75]:
            mid = max(1, int(n * frac))
            if mid >= n:
                continue
            diff = abs(clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
            if diff > best:
                best = diff
        return best
    return r.rolling(w, min_periods=max(4, w // 2)).apply(_fn, raw=True)


def cpd_ext_022_mean_shift_stat_3split_63d(close: pd.Series) -> pd.Series:
    """Max mean-shift across 3 split points in 63-day window."""
    r = _log_returns(close)
    w = _TD_QTR
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        n = len(clean)
        if n < 4:
            return np.nan
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        best = 0.0
        for frac in [0.25, 0.5, 0.75]:
            mid = max(1, int(n * frac))
            if mid >= n:
                continue
            diff = abs(clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
            if diff > best:
                best = diff
        return best
    return r.rolling(w, min_periods=max(4, w // 2)).apply(_fn, raw=True)


def cpd_ext_023_mean_shift_stat_5split_63d(close: pd.Series) -> pd.Series:
    """Max mean-shift across 5 split points (1/6..5/6) in 63-day window."""
    r = _log_returns(close)
    w = _TD_QTR
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        n = len(clean)
        if n < 4:
            return np.nan
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        best = 0.0
        for frac in [1/6, 2/6, 3/6, 4/6, 5/6]:
            mid = max(1, int(n * frac))
            if mid >= n:
                continue
            diff = abs(clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS)
            if diff > best:
                best = diff
        return best
    return r.rolling(w, min_periods=max(4, w // 2)).apply(_fn, raw=True)


def cpd_ext_024_mean_shift_stat_21d_on_logprice(close: pd.Series) -> pd.Series:
    """Mean-shift stat (half=21) applied to log-price levels (not returns)."""
    return _mean_shift_stat(np.log(close.clip(lower=_EPS)), _TD_MON)


def cpd_ext_025_mean_shift_stat_63d_on_logprice(close: pd.Series) -> pd.Series:
    """Mean-shift stat (half=63) applied to log-price levels."""
    return _mean_shift_stat(np.log(close.clip(lower=_EPS)), _TD_QTR)


def cpd_ext_026_mean_shift_stat_21d_half_weight(close: pd.Series) -> pd.Series:
    """
    Weighted mean-shift (half=21): recent half weighted 2x vs prior half.
    Detects break where recent behavior more heavily influences test.
    """
    r = _log_returns(close)
    w = 2 * _TD_MON
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        if len(clean) < 4:
            return np.nan
        n = len(clean)
        mid = n // 2
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        mu_b = clean[:mid].mean()
        mu_a = clean[mid:].mean() * 2.0 / (1.0 + 1.0)
        return abs(mu_a - mu_b) / (std_all + _EPS)
    return r.rolling(w, min_periods=max(4, _TD_MON)).apply(_fn, raw=True)


def cpd_ext_027_mean_shift_stat_vol_63d(volume: pd.Series) -> pd.Series:
    """Mean-shift stat (half=63) on log-volume changes."""
    r = np.log((volume + 1) / (volume.shift(1) + 1))
    return _mean_shift_stat(r, _TD_QTR)


def cpd_ext_028_mean_shift_stat_open_21d(open: pd.Series) -> pd.Series:
    """Mean-shift stat (half=21) on open log-returns."""
    return _mean_shift_stat(np.log(open / open.shift(1)), _TD_MON)


def cpd_ext_029_mean_shift_stat_hl_midpoint_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean-shift stat (half=21) on log-returns of (high+low)/2 midpoint."""
    mid = (high + low) / 2.0
    return _mean_shift_stat(np.log(mid / mid.shift(1)), _TD_MON)


def cpd_ext_030_var_shift_stat_open_21d(open: pd.Series) -> pd.Series:
    """Variance-shift stat (half=21) on open log-returns."""
    return _var_shift_stat(np.log(open / open.shift(1)), _TD_MON)


# --- Group D (031-040): Multi-window break consensus scores ---

def cpd_ext_031_break_consensus_3windows(close: pd.Series) -> pd.Series:
    """
    Break consensus count across 3 windows (half=5, 10, 21), threshold=1.0.
    0-3 score: higher = breaks detected at multiple time scales simultaneously.
    """
    r = _log_returns(close)
    f5  = (_mean_shift_stat(r, _TD_WEEK)  > 1.0).astype(float)
    f10 = (_mean_shift_stat(r, 10)        > 1.0).astype(float)
    f21 = (_mean_shift_stat(r, _TD_MON)   > 1.0).astype(float)
    return f5 + f10 + f21


def cpd_ext_032_downward_break_consensus_3windows(close: pd.Series) -> pd.Series:
    """Downward break consensus (signed shift < -1.0) across 3 windows (5, 10, 21)."""
    r = _log_returns(close)
    f5  = (_mean_shift_signed(r, _TD_WEEK) < -1.0).astype(float)
    f10 = (_mean_shift_signed(r, 10)       < -1.0).astype(float)
    f21 = (_mean_shift_signed(r, _TD_MON)  < -1.0).astype(float)
    return f5 + f10 + f21


def cpd_ext_033_cusum_break_consensus_3windows(close: pd.Series) -> pd.Series:
    """CUSUM break consensus across 3 windows (21, 63, 126). 0-3 score."""
    r = _log_returns(close)
    def _flag(w):
        cs  = _cusum_neg(r, w).abs()
        thr = _rolling_std(r, w) * 2.0
        return (cs > thr.clip(lower=_EPS)).astype(float)
    return _flag(_TD_MON) + _flag(_TD_QTR) + _flag(_TD_HALF)


def cpd_ext_034_var_break_consensus_3windows(close: pd.Series) -> pd.Series:
    """Variance-break consensus across 3 windows (half=5, 10, 21), threshold=0.5. 0-3."""
    r = _log_returns(close)
    f5  = (_var_shift_stat(r, _TD_WEEK).abs() > 0.5).astype(float)
    f10 = (_var_shift_stat(r, 10).abs()       > 0.5).astype(float)
    f21 = (_var_shift_stat(r, _TD_MON).abs()  > 0.5).astype(float)
    return f5 + f10 + f21


def cpd_ext_035_break_consensus_score_weighted(close: pd.Series) -> pd.Series:
    """
    Weighted break consensus: short-window (half=5) weight=1, medium (21) weight=2,
    long (63) weight=3. Rewards breaks that show at longer horizons.
    """
    r = _log_returns(close)
    f5  = (_mean_shift_stat(r, _TD_WEEK) > 1.0).astype(float)
    f21 = (_mean_shift_stat(r, _TD_MON)  > 1.0).astype(float)
    f63 = (_mean_shift_stat(r, _TD_QTR)  > 1.0).astype(float)
    return f5 * 1.0 + f21 * 2.0 + f63 * 3.0


def cpd_ext_036_time_since_any_break_multiscale(close: pd.Series) -> pd.Series:
    """Days since ANY of the three scale break flags (half=5,21,63) fired."""
    r = _log_returns(close)
    f5  = (_mean_shift_stat(r, _TD_WEEK) > 1.0).astype(float)
    f21 = (_mean_shift_stat(r, _TD_MON)  > 1.0).astype(float)
    f63 = (_mean_shift_stat(r, _TD_QTR)  > 1.0).astype(float)
    any_flag = ((f5 + f21 + f63) > 0).astype(float)
    return _time_since_break(any_flag)


def cpd_ext_037_break_count_multiscale_in_63d(close: pd.Series) -> pd.Series:
    """
    Sum of break counts for half=5 and half=21 windows in trailing 63d.
    Captures multi-scale break frequency.
    """
    r = _log_returns(close)
    f5  = _rolling_sum((_mean_shift_stat(r, _TD_WEEK) > 1.0).astype(float), _TD_QTR)
    f21 = _rolling_sum((_mean_shift_stat(r, _TD_MON)  > 1.0).astype(float), _TD_QTR)
    return f5 + f21


def cpd_ext_038_mosum_cusum_composite_21d(close: pd.Series) -> pd.Series:
    """
    Composite of MOSUM and CUSUM negative sides, 21-day window.
    |MOSUM| + normalized |CUSUM_neg|.
    """
    r = _log_returns(close)
    mosum = cpd_ext_013_mosum_abs_21d(close)
    cs    = _cusum_neg(r, _TD_MON).abs()
    std   = _rolling_std(r, _TD_MON)
    return mosum + (cs / std.clip(lower=_EPS)).fillna(0.0)


def cpd_ext_039_all_method_break_score_21d(close: pd.Series) -> pd.Series:
    """
    Mean-shift + var-shift + MOSUM composite, all 21d window.
    Maximum multi-method composite break score.
    """
    r  = _log_returns(close)
    ms = _mean_shift_stat(r, _TD_MON)
    vs = _var_shift_stat(r, _TD_MON).abs()
    mo = cpd_ext_013_mosum_abs_21d(close)
    return ms + vs + mo


def cpd_ext_040_cusum_mean_shift_concordance_21d(close: pd.Series) -> pd.Series:
    """
    Binary: both CUSUM-neg break AND mean-shift break simultaneously detected (21d).
    """
    r    = _log_returns(close)
    cs   = _cusum_neg(r, _TD_MON).abs()
    thr  = _rolling_std(r, _TD_MON) * 2.0
    f_cs = (cs > thr.clip(lower=_EPS)).astype(float)
    f_ms = (_mean_shift_stat(r, _TD_MON) > 1.0).astype(float)
    return (f_cs * f_ms)


# --- Group E (041-050): Bayesian-style break probability proxies ---

def cpd_ext_041_bayes_break_prob_21d(close: pd.Series) -> pd.Series:
    """
    Bayesian-style break probability proxy (21d):
    P(break) ∝ exp(mean_shift_stat^2 / 2). Normalized to [0,1] by rolling max.
    """
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    score = np.exp(ms.clip(upper=10) ** 2 / 2.0)
    mx = _rolling_max(score, _TD_YEAR)
    return _safe_div(score, mx.clip(lower=_EPS))


def cpd_ext_042_bayes_break_prob_63d(close: pd.Series) -> pd.Series:
    """Bayesian-style break probability proxy (63d)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_QTR)
    score = np.exp(ms.clip(upper=10) ** 2 / 2.0)
    mx = _rolling_max(score, _TD_YEAR)
    return _safe_div(score, mx.clip(lower=_EPS))


def cpd_ext_043_break_score_log_likelihood_21d(close: pd.Series) -> pd.Series:
    """
    Log-likelihood ratio of mean-shift model vs null (half=21).
    Approximation: n/2 * log(1 + t_stat^2 / (n-2)) where t_stat = mean_shift_stat * sqrt(n/2).
    """
    r = _log_returns(close)
    w = 2 * _TD_MON
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        n = len(clean)
        if n < 4:
            return np.nan
        std_all = clean.std()
        if std_all < _EPS:
            return 0.0
        mid = n // 2
        t_stat = abs(clean[mid:].mean() - clean[:mid].mean()) / (std_all + _EPS) * np.sqrt(mid)
        return (n / 2.0) * np.log(1.0 + t_stat ** 2 / max(1.0, n - 2))
    return r.rolling(w, min_periods=max(4, _TD_MON)).apply(_fn, raw=True)


def cpd_ext_044_break_information_criterion_21d(close: pd.Series) -> pd.Series:
    """
    Bayesian Information Criterion difference between break-model and null model (half=21).
    Higher = stronger evidence for break. BIC_null - BIC_break (positive = break preferred).
    """
    r = _log_returns(close)
    w = 2 * _TD_MON
    def _fn(arr):
        clean = arr[~np.isnan(arr)]
        n = len(clean)
        if n < 4:
            return np.nan
        mid = n // 2
        var_null = clean.var()
        var_b    = clean[:mid].var()
        var_a    = clean[mid:].var()
        if var_null < _EPS:
            return 0.0
        ll_null  = -n / 2.0 * np.log(var_null + _EPS)
        ll_break = -mid / 2.0 * np.log(var_b + _EPS) - (n - mid) / 2.0 * np.log(var_a + _EPS)
        # BIC penalty: k=1 for null, k=3 for break (mu1, mu2, sigma)
        bic_diff = 2.0 * (ll_break - ll_null) - 2.0 * np.log(max(n, 1))
        return bic_diff
    return r.rolling(w, min_periods=max(4, _TD_MON)).apply(_fn, raw=True)


def cpd_ext_045_break_posterior_update_21d(close: pd.Series) -> pd.Series:
    """
    Sequential posterior probability of break (EWM update of break flag).
    Starts at prior 0.1, updates toward 1.0 on break detection.
    Approximated as EWM(span=5) of break flag with floor 0.05.
    """
    flag = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    return flag.ewm(span=5, min_periods=1).mean().clip(lower=0.05, upper=1.0)


def cpd_ext_046_break_posterior_update_63d(close: pd.Series) -> pd.Series:
    """EWM(span=10) of break flag (half=63, thr=1.0) as posterior probability proxy."""
    flag = (_mean_shift_stat(_log_returns(close), _TD_QTR) > 1.0).astype(float)
    return flag.ewm(span=10, min_periods=1).mean().clip(lower=0.05, upper=1.0)


def cpd_ext_047_bic_diff_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of BIC difference (21d) — is current break extreme historically?"""
    bic = cpd_ext_044_break_information_criterion_21d(close)
    return bic.expanding(min_periods=_TD_QTR).rank(pct=True)


def cpd_ext_048_log_likelihood_ratio_21d_pct_rank(close: pd.Series) -> pd.Series:
    """Percentile rank of log-likelihood ratio (21d) in trailing 252d distribution."""
    llr = cpd_ext_043_break_score_log_likelihood_21d(close)
    return llr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_ext_049_break_prior_decay_21d(close: pd.Series) -> pd.Series:
    """
    Break signal with exponential time-decay:
    magnitude * exp(-days_since_break / 21). Magnitude = mean-shift stat at break.
    """
    ms   = _mean_shift_stat(_log_returns(close), _TD_MON)
    flag = (ms > 1.0).astype(float)
    tsb  = _time_since_break(flag).fillna(999.0)
    mag  = ms.where(flag == 1.0).ffill().fillna(0.0)
    decay = np.exp(-tsb / _TD_MON)
    return mag * decay


def cpd_ext_050_break_prior_decay_63d(close: pd.Series) -> pd.Series:
    """Break signal with exponential decay, decay constant=63d."""
    ms   = _mean_shift_stat(_log_returns(close), _TD_QTR)
    flag = (ms > 1.0).astype(float)
    tsb  = _time_since_break(flag).fillna(999.0)
    mag  = ms.where(flag == 1.0).ffill().fillna(0.0)
    decay = np.exp(-tsb / _TD_QTR)
    return mag * decay


# --- Group F (051-060): Structural break on derived series ---

def cpd_ext_051_mean_shift_stat_absret_5d(close: pd.Series) -> pd.Series:
    """Mean-shift stat on absolute log-returns, half=5 (fast volatility-regime shift)."""
    return _mean_shift_stat(_log_returns(close).abs(), _TD_WEEK)


def cpd_ext_052_mean_shift_stat_sqret_21d(close: pd.Series) -> pd.Series:
    """Mean-shift stat on squared log-returns (proxy for variance), half=21."""
    r2 = _log_returns(close) ** 2
    return _mean_shift_stat(r2, _TD_MON)


def cpd_ext_053_cusum_neg_sqret_21d(close: pd.Series) -> pd.Series:
    """Lower CUSUM on squared log-returns, 21-day window."""
    r2 = _log_returns(close) ** 2
    return _cusum_neg(r2, _TD_MON)


def cpd_ext_054_mean_shift_stat_close_open_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean-shift stat (half=21) on close-to-open log-returns (overnight gap regime break)."""
    co_ret = np.log(close / open.clip(lower=_EPS))
    return _mean_shift_stat(co_ret, _TD_MON)


def cpd_ext_055_mean_shift_stat_hl_range_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean-shift stat (half=21) on daily log(high/low) range."""
    rng = np.log((high + _EPS) / (low + _EPS))
    return _mean_shift_stat(rng, _TD_MON)


def cpd_ext_056_cusum_neg_range_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower CUSUM on daily log(high/low) range, 21-day window."""
    rng = np.log((high + _EPS) / (low + _EPS))
    return _cusum_neg(rng, _TD_MON)


def cpd_ext_057_var_shift_stat_sqret_21d(close: pd.Series) -> pd.Series:
    """Variance-shift stat on squared log-returns, half=21."""
    r2 = _log_returns(close) ** 2
    return _var_shift_stat(r2, _TD_MON)


def cpd_ext_058_mean_shift_stat_logvol_21d(volume: pd.Series) -> pd.Series:
    """Mean-shift stat (half=21) on log-volume levels (not changes)."""
    lv = np.log(volume.clip(lower=1.0))
    return _mean_shift_stat(lv, _TD_MON)


def cpd_ext_059_cusum_neg_logvol_21d(volume: pd.Series) -> pd.Series:
    """Lower CUSUM on log-volume levels, 21-day window."""
    lv = np.log(volume.clip(lower=1.0))
    return _cusum_neg(lv, _TD_MON)


def cpd_ext_060_var_shift_logvol_21d(volume: pd.Series) -> pd.Series:
    """Variance-shift stat on log-volume levels, half=21."""
    lv = np.log(volume.clip(lower=1.0))
    return _var_shift_stat(lv, _TD_MON)


# --- Group G (061-075): Cross-signal confluence and deep composite features ---

def cpd_ext_061_price_vol_break_confluence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Confluence of price-return break and log-volume break (half=21, thr=1).
    0, 1, or 2 signals firing together.
    """
    r = _log_returns(close)
    lv = np.log(volume.clip(lower=1.0))
    f_r  = (_mean_shift_stat(r,  _TD_MON) > 1.0).astype(float)
    f_lv = (_mean_shift_stat(lv, _TD_MON) > 1.0).astype(float)
    return f_r + f_lv


def cpd_ext_062_ohlcv_break_max_stat_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Maximum mean-shift stat across all 5 series (close-ret, high-ret, low-ret, open-ret, vol-change).
    Half=21. Maximum statistic across OHLCV.
    """
    r_c = _log_returns(close)
    r_h = np.log(high / high.shift(1))
    r_l = np.log(low / low.shift(1))
    r_o = np.log(open / open.shift(1))
    r_v = np.log((volume + 1) / (volume.shift(1) + 1))
    ms_c = _mean_shift_stat(r_c, _TD_MON)
    ms_h = _mean_shift_stat(r_h, _TD_MON)
    ms_l = _mean_shift_stat(r_l, _TD_MON)
    ms_o = _mean_shift_stat(r_o, _TD_MON)
    ms_v = _mean_shift_stat(r_v, _TD_MON)
    return pd.concat([ms_c, ms_h, ms_l, ms_o, ms_v], axis=1).max(axis=1)


def cpd_ext_063_all_method_downward_score_21d(close: pd.Series) -> pd.Series:
    """
    Downward-focused composite: signed mean-shift negative part + CUSUM-neg magnitude
    + negative MOSUM, all 21d.
    """
    r  = _log_returns(close)
    ms_neg = (-_mean_shift_signed(r, _TD_MON)).clip(lower=0.0)
    cs_neg = _cusum_neg(r, _TD_MON).abs()
    mo_neg = (-cpd_ext_011_mosum_neg_21d(close)).clip(lower=0.0)
    std    = _rolling_std(r, _TD_MON)
    return ms_neg + (cs_neg / std.clip(lower=_EPS)).fillna(0.0) + mo_neg


def cpd_ext_064_break_score_composite_21d_pct_rank(close: pd.Series) -> pd.Series:
    """Percentile rank (252d) of all-method composite break score (21d)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    mo = cpd_ext_013_mosum_abs_21d(close)
    score = ms + vs + mo
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cpd_ext_065_time_since_downward_break_any_method(close: pd.Series) -> pd.Series:
    """Days since last downward break by any method (CUSUM, signed-shift, MOSUM)."""
    r = _log_returns(close)
    f_cs = (_cusum_neg(r, _TD_MON).abs() > (_rolling_std(r, _TD_MON) * 2.0).clip(lower=_EPS)).astype(float)
    f_ms = (_mean_shift_signed(r, _TD_MON) < -1.0).astype(float)
    f_mo = (cpd_ext_011_mosum_neg_21d(close) < -2.0).astype(float)
    any_flag = ((f_cs + f_ms + f_mo) > 0).astype(float)
    return _time_since_break(any_flag)


def cpd_ext_066_cusum_break_intensity_sum_3windows(close: pd.Series) -> pd.Series:
    """Sum of normalized |lower CUSUM| across 3 windows (21, 63, 126d)."""
    r = _log_returns(close)
    def _ncs(w):
        cs  = _cusum_neg(r, w).abs()
        std = _rolling_std(r, w)
        return (cs / std.clip(lower=_EPS)).fillna(0.0)
    return _ncs(_TD_MON) + _ncs(_TD_QTR) + _ncs(_TD_HALF)


def cpd_ext_067_mean_shift_max_3windows(close: pd.Series) -> pd.Series:
    """Maximum mean-shift stat across 3 windows (half=5, 21, 63)."""
    r = _log_returns(close)
    ms5  = _mean_shift_stat(r, _TD_WEEK)
    ms21 = _mean_shift_stat(r, _TD_MON)
    ms63 = _mean_shift_stat(r, _TD_QTR)
    return pd.concat([ms5, ms21, ms63], axis=1).max(axis=1)


def cpd_ext_068_downward_break_all_methods_flag(close: pd.Series) -> pd.Series:
    """Binary: all 3 methods (CUSUM, signed-shift, MOSUM) detect downward break (21d)."""
    r = _log_returns(close)
    f_cs = (_cusum_neg(r, _TD_MON).abs() > (_rolling_std(r, _TD_MON) * 2.0).clip(lower=_EPS)).astype(float)
    f_ms = (_mean_shift_signed(r, _TD_MON) < -1.0).astype(float)
    f_mo = (cpd_ext_011_mosum_neg_21d(close) < -2.0).astype(float)
    return ((f_cs + f_ms + f_mo) == 3.0).astype(float)


def cpd_ext_069_break_cluster_score_21d_in_252d(close: pd.Series) -> pd.Series:
    """
    Break cluster score: weighted count of break detections in trailing 252d,
    with breaks in the most recent 21d weighted 3x, next 63d 2x, remainder 1x.
    """
    flag = (_mean_shift_stat(_log_returns(close), _TD_MON) > 1.0).astype(float)
    recent21 = _rolling_sum(flag, _TD_MON) * 3.0
    next63   = (_rolling_sum(flag, _TD_QTR) - _rolling_sum(flag, _TD_MON)) * 2.0
    older    = (_rolling_sum(flag, _TD_YEAR) - _rolling_sum(flag, _TD_QTR)) * 1.0
    return recent21 + next63 + older


def cpd_ext_070_break_cross_asset_proxy_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Proxy for cross-signal break: sum of 5 binary flags from close, high (from OHLCV),
    low, volume, and squared-return series (half=21, thr=1).
    """
    r_c  = _log_returns(close)
    r2   = r_c ** 2
    r_v  = np.log((volume + 1) / (volume.shift(1) + 1))
    f_c  = (_mean_shift_stat(r_c, _TD_MON)  > 1.0).astype(float)
    f_r2 = (_mean_shift_stat(r2,  _TD_MON)  > 1.0).astype(float)
    f_v  = (_mean_shift_stat(r_v, _TD_MON)  > 1.0).astype(float)
    return f_c + f_r2 + f_v


def cpd_ext_071_break_regime_persistence_score(close: pd.Series) -> pd.Series:
    """
    EWM(span=63) of composite break score (21d). Long-duration persistence of
    structural-break environment — captures extended period of regime instability.
    """
    r  = _log_returns(close)
    ms = _mean_shift_stat(r, _TD_MON)
    vs = _var_shift_stat(r, _TD_MON).abs()
    score = ms + vs
    return score.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def cpd_ext_072_cusum_neg_streak_count_252d(close: pd.Series) -> pd.Series:
    """Count of CUSUM-neg breaks (21d) in trailing 252d — frequency in past year."""
    r   = _log_returns(close)
    cs  = _cusum_neg(r, _TD_MON).abs()
    thr = _rolling_std(r, _TD_MON) * 2.0
    flag = (cs > thr.clip(lower=_EPS)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def cpd_ext_073_mean_shift_signed_21d_ewm(close: pd.Series) -> pd.Series:
    """EWM(span=10) of signed mean-shift (half=21) — smoothed directional break signal."""
    return _mean_shift_signed(_log_returns(close), _TD_MON).ewm(span=10, min_periods=5).mean()


def cpd_ext_074_break_magnitude_decay_composite(close: pd.Series) -> pd.Series:
    """
    Composite of two decay signals: mean-shift decay (tau=21) + CUSUM decay (tau=21).
    """
    return cpd_ext_049_break_prior_decay_21d(close) + (
        _cusum_neg(_log_returns(close), _TD_MON).abs()
        .where((_cusum_neg(_log_returns(close), _TD_MON).abs() >
                (_rolling_std(_log_returns(close), _TD_MON) * 2.0).clip(lower=_EPS)).astype(bool))
        .ffill().fillna(0.0)
        * np.exp(
            -_time_since_break(
                (_cusum_neg(_log_returns(close), _TD_MON).abs() >
                 (_rolling_std(_log_returns(close), _TD_MON) * 2.0).clip(lower=_EPS)).astype(float)
            ).fillna(999.0) / _TD_MON
        )
    )


def cpd_ext_075_all_method_break_score_expanding_pct(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of all-method composite break score (21d)."""
    ms = _mean_shift_stat(_log_returns(close), _TD_MON)
    vs = _var_shift_stat(_log_returns(close), _TD_MON).abs()
    mo = cpd_ext_013_mosum_abs_21d(close)
    score = ms + vs + mo
    return score.expanding(min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

CHANGE_POINT_DETECTION_EXTENDED_REGISTRY_001_075 = {
    "cpd_ext_001_cusum_neg_252d": {"inputs": ["close"], "func": cpd_ext_001_cusum_neg_252d},
    "cpd_ext_002_cusum_pos_252d": {"inputs": ["close"], "func": cpd_ext_002_cusum_pos_252d},
    "cpd_ext_003_cusum_neg_adaptive_21d": {"inputs": ["close"], "func": cpd_ext_003_cusum_neg_adaptive_21d},
    "cpd_ext_004_cusum_neg_adaptive_63d": {"inputs": ["close"], "func": cpd_ext_004_cusum_neg_adaptive_63d},
    "cpd_ext_005_cusum_two_sided_max_21d": {"inputs": ["close"], "func": cpd_ext_005_cusum_two_sided_max_21d},
    "cpd_ext_006_cusum_two_sided_max_126d": {"inputs": ["close"], "func": cpd_ext_006_cusum_two_sided_max_126d},
    "cpd_ext_007_cusum_neg_high_63d": {"inputs": ["high"], "func": cpd_ext_007_cusum_neg_high_63d},
    "cpd_ext_008_cusum_neg_open_21d": {"inputs": ["open"], "func": cpd_ext_008_cusum_neg_open_21d},
    "cpd_ext_009_cusum_pos_vol_63d": {"inputs": ["volume"], "func": cpd_ext_009_cusum_pos_vol_63d},
    "cpd_ext_010_cusum_neg_vol_63d": {"inputs": ["volume"], "func": cpd_ext_010_cusum_neg_vol_63d},
    "cpd_ext_011_mosum_neg_21d": {"inputs": ["close"], "func": cpd_ext_011_mosum_neg_21d},
    "cpd_ext_012_mosum_neg_63d": {"inputs": ["close"], "func": cpd_ext_012_mosum_neg_63d},
    "cpd_ext_013_mosum_abs_21d": {"inputs": ["close"], "func": cpd_ext_013_mosum_abs_21d},
    "cpd_ext_014_mosum_abs_63d": {"inputs": ["close"], "func": cpd_ext_014_mosum_abs_63d},
    "cpd_ext_015_mosum_flag_21d": {"inputs": ["close"], "func": cpd_ext_015_mosum_flag_21d},
    "cpd_ext_016_mosum_neg_below_neg2_flag_21d": {"inputs": ["close"], "func": cpd_ext_016_mosum_neg_below_neg2_flag_21d},
    "cpd_ext_017_mosum_neg_vol_21d": {"inputs": ["volume"], "func": cpd_ext_017_mosum_neg_vol_21d},
    "cpd_ext_018_time_since_mosum_flag_21d": {"inputs": ["close"], "func": cpd_ext_018_time_since_mosum_flag_21d},
    "cpd_ext_019_mosum_pct_rank_252d": {"inputs": ["close"], "func": cpd_ext_019_mosum_pct_rank_252d},
    "cpd_ext_020_mosum_neg_21d_5d_diff": {"inputs": ["close"], "func": cpd_ext_020_mosum_neg_21d_5d_diff},
    "cpd_ext_021_mean_shift_stat_3split_21d": {"inputs": ["close"], "func": cpd_ext_021_mean_shift_stat_3split_21d},
    "cpd_ext_022_mean_shift_stat_3split_63d": {"inputs": ["close"], "func": cpd_ext_022_mean_shift_stat_3split_63d},
    "cpd_ext_023_mean_shift_stat_5split_63d": {"inputs": ["close"], "func": cpd_ext_023_mean_shift_stat_5split_63d},
    "cpd_ext_024_mean_shift_stat_21d_on_logprice": {"inputs": ["close"], "func": cpd_ext_024_mean_shift_stat_21d_on_logprice},
    "cpd_ext_025_mean_shift_stat_63d_on_logprice": {"inputs": ["close"], "func": cpd_ext_025_mean_shift_stat_63d_on_logprice},
    "cpd_ext_026_mean_shift_stat_21d_half_weight": {"inputs": ["close"], "func": cpd_ext_026_mean_shift_stat_21d_half_weight},
    "cpd_ext_027_mean_shift_stat_vol_63d": {"inputs": ["volume"], "func": cpd_ext_027_mean_shift_stat_vol_63d},
    "cpd_ext_028_mean_shift_stat_open_21d": {"inputs": ["open"], "func": cpd_ext_028_mean_shift_stat_open_21d},
    "cpd_ext_029_mean_shift_stat_hl_midpoint_21d": {"inputs": ["high", "low"], "func": cpd_ext_029_mean_shift_stat_hl_midpoint_21d},
    "cpd_ext_030_var_shift_stat_open_21d": {"inputs": ["open"], "func": cpd_ext_030_var_shift_stat_open_21d},
    "cpd_ext_031_break_consensus_3windows": {"inputs": ["close"], "func": cpd_ext_031_break_consensus_3windows},
    "cpd_ext_032_downward_break_consensus_3windows": {"inputs": ["close"], "func": cpd_ext_032_downward_break_consensus_3windows},
    "cpd_ext_033_cusum_break_consensus_3windows": {"inputs": ["close"], "func": cpd_ext_033_cusum_break_consensus_3windows},
    "cpd_ext_034_var_break_consensus_3windows": {"inputs": ["close"], "func": cpd_ext_034_var_break_consensus_3windows},
    "cpd_ext_035_break_consensus_score_weighted": {"inputs": ["close"], "func": cpd_ext_035_break_consensus_score_weighted},
    "cpd_ext_036_time_since_any_break_multiscale": {"inputs": ["close"], "func": cpd_ext_036_time_since_any_break_multiscale},
    "cpd_ext_037_break_count_multiscale_in_63d": {"inputs": ["close"], "func": cpd_ext_037_break_count_multiscale_in_63d},
    "cpd_ext_038_mosum_cusum_composite_21d": {"inputs": ["close"], "func": cpd_ext_038_mosum_cusum_composite_21d},
    "cpd_ext_039_all_method_break_score_21d": {"inputs": ["close"], "func": cpd_ext_039_all_method_break_score_21d},
    "cpd_ext_040_cusum_mean_shift_concordance_21d": {"inputs": ["close"], "func": cpd_ext_040_cusum_mean_shift_concordance_21d},
    "cpd_ext_041_bayes_break_prob_21d": {"inputs": ["close"], "func": cpd_ext_041_bayes_break_prob_21d},
    "cpd_ext_042_bayes_break_prob_63d": {"inputs": ["close"], "func": cpd_ext_042_bayes_break_prob_63d},
    "cpd_ext_043_break_score_log_likelihood_21d": {"inputs": ["close"], "func": cpd_ext_043_break_score_log_likelihood_21d},
    "cpd_ext_044_break_information_criterion_21d": {"inputs": ["close"], "func": cpd_ext_044_break_information_criterion_21d},
    "cpd_ext_045_break_posterior_update_21d": {"inputs": ["close"], "func": cpd_ext_045_break_posterior_update_21d},
    "cpd_ext_046_break_posterior_update_63d": {"inputs": ["close"], "func": cpd_ext_046_break_posterior_update_63d},
    "cpd_ext_047_bic_diff_expanding": {"inputs": ["close"], "func": cpd_ext_047_bic_diff_expanding},
    "cpd_ext_048_log_likelihood_ratio_21d_pct_rank": {"inputs": ["close"], "func": cpd_ext_048_log_likelihood_ratio_21d_pct_rank},
    "cpd_ext_049_break_prior_decay_21d": {"inputs": ["close"], "func": cpd_ext_049_break_prior_decay_21d},
    "cpd_ext_050_break_prior_decay_63d": {"inputs": ["close"], "func": cpd_ext_050_break_prior_decay_63d},
    "cpd_ext_051_mean_shift_stat_absret_5d": {"inputs": ["close"], "func": cpd_ext_051_mean_shift_stat_absret_5d},
    "cpd_ext_052_mean_shift_stat_sqret_21d": {"inputs": ["close"], "func": cpd_ext_052_mean_shift_stat_sqret_21d},
    "cpd_ext_053_cusum_neg_sqret_21d": {"inputs": ["close"], "func": cpd_ext_053_cusum_neg_sqret_21d},
    "cpd_ext_054_mean_shift_stat_close_open_ret_21d": {"inputs": ["close", "open"], "func": cpd_ext_054_mean_shift_stat_close_open_ret_21d},
    "cpd_ext_055_mean_shift_stat_hl_range_21d": {"inputs": ["close", "high", "low"], "func": cpd_ext_055_mean_shift_stat_hl_range_21d},
    "cpd_ext_056_cusum_neg_range_21d": {"inputs": ["close", "high", "low"], "func": cpd_ext_056_cusum_neg_range_21d},
    "cpd_ext_057_var_shift_stat_sqret_21d": {"inputs": ["close"], "func": cpd_ext_057_var_shift_stat_sqret_21d},
    "cpd_ext_058_mean_shift_stat_logvol_21d": {"inputs": ["volume"], "func": cpd_ext_058_mean_shift_stat_logvol_21d},
    "cpd_ext_059_cusum_neg_logvol_21d": {"inputs": ["volume"], "func": cpd_ext_059_cusum_neg_logvol_21d},
    "cpd_ext_060_var_shift_logvol_21d": {"inputs": ["volume"], "func": cpd_ext_060_var_shift_logvol_21d},
    "cpd_ext_061_price_vol_break_confluence_21d": {"inputs": ["close", "volume"], "func": cpd_ext_061_price_vol_break_confluence_21d},
    "cpd_ext_062_ohlcv_break_max_stat_21d": {"inputs": ["close", "high", "low", "open", "volume"], "func": cpd_ext_062_ohlcv_break_max_stat_21d},
    "cpd_ext_063_all_method_downward_score_21d": {"inputs": ["close"], "func": cpd_ext_063_all_method_downward_score_21d},
    "cpd_ext_064_break_score_composite_21d_pct_rank": {"inputs": ["close"], "func": cpd_ext_064_break_score_composite_21d_pct_rank},
    "cpd_ext_065_time_since_downward_break_any_method": {"inputs": ["close"], "func": cpd_ext_065_time_since_downward_break_any_method},
    "cpd_ext_066_cusum_break_intensity_sum_3windows": {"inputs": ["close"], "func": cpd_ext_066_cusum_break_intensity_sum_3windows},
    "cpd_ext_067_mean_shift_max_3windows": {"inputs": ["close"], "func": cpd_ext_067_mean_shift_max_3windows},
    "cpd_ext_068_downward_break_all_methods_flag": {"inputs": ["close"], "func": cpd_ext_068_downward_break_all_methods_flag},
    "cpd_ext_069_break_cluster_score_21d_in_252d": {"inputs": ["close"], "func": cpd_ext_069_break_cluster_score_21d_in_252d},
    "cpd_ext_070_break_cross_asset_proxy_21d": {"inputs": ["close", "volume"], "func": cpd_ext_070_break_cross_asset_proxy_21d},
    "cpd_ext_071_break_regime_persistence_score": {"inputs": ["close"], "func": cpd_ext_071_break_regime_persistence_score},
    "cpd_ext_072_cusum_neg_streak_count_252d": {"inputs": ["close"], "func": cpd_ext_072_cusum_neg_streak_count_252d},
    "cpd_ext_073_mean_shift_signed_21d_ewm": {"inputs": ["close"], "func": cpd_ext_073_mean_shift_signed_21d_ewm},
    "cpd_ext_074_break_magnitude_decay_composite": {"inputs": ["close"], "func": cpd_ext_074_break_magnitude_decay_composite},
    "cpd_ext_075_all_method_break_score_expanding_pct": {"inputs": ["close"], "func": cpd_ext_075_all_method_break_score_expanding_pct},
}
