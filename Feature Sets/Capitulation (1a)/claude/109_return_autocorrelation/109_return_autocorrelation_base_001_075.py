"""
109_return_autocorrelation — Base Features 001-075
Domain: autocorrelation and serial-dependence structure of returns — return autocorrelation
        at multiple lags, partial autocorrelation, Ljung-Box-style statistics, variance ratios,
        runs-test statistics, persistence vs anti-persistence/mean-reversion, sign-autocorrelation,
        trending-vs-choppy serial structure
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
    """Log returns of close price."""
    return np.log(close / close.shift(1))


def _rolling_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of series s at given lag over window w.
    NaN-safe: drops NaN before computing each window's correlation."""
    def _ac(x):
        arr = x[~np.isnan(x)]
        if len(arr) < max(lag + 2, w // 2):
            return np.nan
        if len(arr) <= lag:
            return np.nan
        x1 = arr[:-lag]
        x2 = arr[lag:]
        if len(x1) < 2:
            return np.nan
        m1, m2 = x1.mean(), x2.mean()
        num = ((x1 - m1) * (x2 - m2)).mean()
        den = x1.std(ddof=0) * x2.std(ddof=0)
        if den < _EPS:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(lag + 2, w // 2)).apply(_ac, raw=True)


def _rolling_pacf_lag1(s: pd.Series, w: int) -> pd.Series:
    """Rolling partial autocorrelation at lag 1 (equals ACF lag 1 for lag=1)."""
    return _rolling_autocorr(s, w, 1)


def _rolling_pacf_lag2(s: pd.Series, w: int) -> pd.Series:
    """Rolling partial autocorrelation at lag 2 via Yule-Walker recursion."""
    def _pacf2(x):
        arr = x[~np.isnan(x)]
        if len(arr) < max(5, w // 2):
            return np.nan
        x1 = arr[:-1]
        x2 = arr[1:]
        m1, m2 = x1.mean(), x2.mean()
        num = ((x1 - m1) * (x2 - m2)).mean()
        den = x1.std(ddof=0) * x2.std(ddof=0)
        r1 = num / den if den > _EPS else np.nan
        x1b = arr[:-2]
        x2b = arr[2:]
        m1b, m2b = x1b.mean(), x2b.mean()
        num2 = ((x1b - m1b) * (x2b - m2b)).mean()
        den2 = x1b.std(ddof=0) * x2b.std(ddof=0)
        r2 = num2 / den2 if den2 > _EPS else np.nan
        if r1 is None or np.isnan(r1):
            return np.nan
        denom = 1.0 - r1 ** 2
        if abs(denom) < _EPS:
            return np.nan
        return (r2 - r1 ** 2) / denom
    return s.rolling(w, min_periods=max(5, w // 2)).apply(_pacf2, raw=True)


def _ljung_box_stat(s: pd.Series, w: int, max_lag: int) -> pd.Series:
    """Rolling Ljung-Box Q-statistic up to max_lag lags over window w."""
    def _lb(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(max_lag + 2, w // 2):
            return np.nan
        q = 0.0
        for k in range(1, max_lag + 1):
            x1 = arr[:-k]
            x2 = arr[k:]
            m1, m2 = x1.mean(), x2.mean()
            num = ((x1 - m1) * (x2 - m2)).mean()
            den = x1.std(ddof=0) * x2.std(ddof=0)
            rk = num / den if den > _EPS else 0.0
            q += rk ** 2 / (n - k)
        return n * (n + 2) * q
    return s.rolling(w, min_periods=max(max_lag + 2, w // 2)).apply(_lb, raw=True)


def _variance_ratio(s: pd.Series, w: int, k: int) -> pd.Series:
    """Rolling Lo-MacKinlay variance ratio: Var(k-period ret) / (k * Var(1-period ret))."""
    def _vr(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(k + 2, w // 2):
            return np.nan
        var1 = np.var(arr[1:] - arr[:-1], ddof=1) if n > 1 else np.nan
        # k-period returns
        if n < k + 1:
            return np.nan
        kret = arr[k:] - arr[:-k]
        vark = np.var(kret, ddof=1) if len(kret) > 1 else np.nan
        if var1 is None or np.isnan(var1) or var1 < _EPS:
            return np.nan
        return vark / (k * var1)
    return s.rolling(w, min_periods=max(k + 2, w // 2)).apply(_vr, raw=True)


def _sign_autocorr(s: pd.Series, w: int, lag: int) -> pd.Series:
    """Rolling autocorrelation of the sign of returns at given lag."""
    signs = np.sign(s)
    return _rolling_autocorr(signs, w, lag)


def _runs_ratio(s: pd.Series, w: int) -> pd.Series:
    """Rolling ratio of observed runs to expected runs (>1 = trending, <1 = choppy)."""
    def _rr(x):
        arr = x[~np.isnan(x)]
        n = len(arr)
        if n < max(4, w // 2):
            return np.nan
        signs = np.sign(arr)
        # count runs
        runs = 1
        for i in range(1, n):
            if signs[i] != signs[i - 1]:
                runs += 1
        n_pos = np.sum(signs > 0)
        n_neg = np.sum(signs < 0)
        if n_pos == 0 or n_neg == 0:
            return np.nan
        expected = (2.0 * n_pos * n_neg / n) + 1.0
        if expected < _EPS:
            return np.nan
        return runs / expected
    return s.rolling(w, min_periods=max(4, w // 2)).apply(_rr, raw=True)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw autocorrelation at single lags, short windows ---

def rac_001_ac_lag1_21d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 1 over 21-day rolling window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_MON, 1)


def rac_002_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 1 over 63-day rolling window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 1)


def rac_003_ac_lag1_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 1 over 126-day rolling window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_HALF, 1)


def rac_004_ac_lag1_252d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 1 over 252-day rolling window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 1)


def rac_005_ac_lag2_21d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 2 over 21-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_MON, 2)


def rac_006_ac_lag2_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 2 over 63-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 2)


def rac_007_ac_lag3_21d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 3 over 21-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_MON, 3)


def rac_008_ac_lag3_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 3 over 63-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 3)


def rac_009_ac_lag5_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 5 (weekly) over 63-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 5)


def rac_010_ac_lag5_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of log-returns at lag 5 over 126-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_HALF, 5)


# --- Group B (011-020): Partial autocorrelation and multi-lag sum ---

def rac_011_pacf_lag1_21d(close: pd.Series) -> pd.Series:
    """Partial autocorrelation of returns at lag 1 over 21-day window."""
    r = _log_returns(close)
    return _rolling_pacf_lag1(r, _TD_MON)


def rac_012_pacf_lag1_63d(close: pd.Series) -> pd.Series:
    """Partial autocorrelation of returns at lag 1 over 63-day window."""
    r = _log_returns(close)
    return _rolling_pacf_lag1(r, _TD_QTR)


def rac_013_pacf_lag2_63d(close: pd.Series) -> pd.Series:
    """Partial autocorrelation of returns at lag 2 over 63-day window."""
    r = _log_returns(close)
    return _rolling_pacf_lag2(r, _TD_QTR)


def rac_014_pacf_lag2_126d(close: pd.Series) -> pd.Series:
    """Partial autocorrelation of returns at lag 2 over 126-day window."""
    r = _log_returns(close)
    return _rolling_pacf_lag2(r, _TD_HALF)


def rac_015_ac_sum_lags1_5_63d(close: pd.Series) -> pd.Series:
    """Sum of |autocorrelation| at lags 1-5 over 63-day window (total serial structure)."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(r, _TD_QTR, lag).abs().fillna(0.0)
    return total


def rac_016_ac_sum_lags1_5_126d(close: pd.Series) -> pd.Series:
    """Sum of |autocorrelation| at lags 1-5 over 126-day window."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        total = total + _rolling_autocorr(r, _TD_HALF, lag).abs().fillna(0.0)
    return total


def rac_017_ac_lag1_minus_lag2_63d(close: pd.Series) -> pd.Series:
    """Difference: AC(lag1) - AC(lag2) at 63-day window (monotone decay check)."""
    r = _log_returns(close)
    a1 = _rolling_autocorr(r, _TD_QTR, 1)
    a2 = _rolling_autocorr(r, _TD_QTR, 2)
    return a1 - a2


def rac_018_ac_lag1_sign_63d(close: pd.Series) -> pd.Series:
    """Sign of lag-1 autocorrelation at 63-day window (+1=persistence,-1=reversal)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return np.sign(ac)


def rac_019_ac_lag1_abs_63d(close: pd.Series) -> pd.Series:
    """Absolute value of lag-1 autocorrelation at 63-day window (magnitude of serial dep)."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_QTR, 1).abs()


def rac_020_ac_lag1_abs_252d(close: pd.Series) -> pd.Series:
    """Absolute value of lag-1 autocorrelation at 252-day window."""
    r = _log_returns(close)
    return _rolling_autocorr(r, _TD_YEAR, 1).abs()


# --- Group C (021-030): Ljung-Box style Q-statistics ---

def rac_021_lb_q4_63d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (4 lags) over 63-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_QTR, 4)


def rac_022_lb_q4_126d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (4 lags) over 126-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_HALF, 4)


def rac_023_lb_q8_126d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (8 lags) over 126-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_HALF, 8)


def rac_024_lb_q8_252d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (8 lags) over 252-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_YEAR, 8)


def rac_025_lb_q4_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day LB(4) Q-stat relative to its 252-day distribution."""
    r = _log_returns(close)
    q = _ljung_box_stat(r, _TD_QTR, 4)
    m = _rolling_mean(q, _TD_YEAR)
    s = _rolling_std(q, _TD_YEAR)
    return _safe_div(q - m, s)


def rac_026_lb_q4_21d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (4 lags) over 21-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_MON, 4)


def rac_027_lb_q2_21d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (2 lags) over 21-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_MON, 2)


def rac_028_lb_q10_252d(close: pd.Series) -> pd.Series:
    """Ljung-Box Q-statistic (10 lags) over 252-day rolling window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_YEAR, 10)


def rac_029_lb_q4_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day LB(4) Q-stat within its 252-day distribution."""
    r = _log_returns(close)
    q = _ljung_box_stat(r, _TD_QTR, 4)
    return q.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_030_lb_q4_normalized_n(close: pd.Series) -> pd.Series:
    """Normalized LB(4) Q-stat (divided by number of lags) over 63-day window."""
    r = _log_returns(close)
    return _ljung_box_stat(r, _TD_QTR, 4) / 4.0


# --- Group D (031-040): Variance ratios ---

def rac_031_vr_2_63d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=2) over 63-day window on log-price (>1=trending,<1=reverting)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_QTR, 2)


def rac_032_vr_5_63d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=5) over 63-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_QTR, 5)


def rac_033_vr_5_126d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=5) over 126-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 5)


def rac_034_vr_10_126d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=10) over 126-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 10)


def rac_035_vr_10_252d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=10) over 252-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_YEAR, 10)


def rac_036_vr_21_252d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=21, monthly) over 252-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_YEAR, 21)


def rac_037_vr_2_126d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=2) over 126-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 2)


def rac_038_vr_5_252d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=5) over 252-day window on log-price."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_YEAR, 5)


def rac_039_vr_2_minus1_63d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=2) minus 1 over 63-day window (signed deviation from random walk)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_QTR, 2) - 1.0


def rac_040_vr_5_minus1_126d(close: pd.Series) -> pd.Series:
    """Variance ratio (k=5) minus 1 over 126-day window (signed mean-reversion signal)."""
    lp = np.log(close.replace(0, np.nan))
    return _variance_ratio(lp, _TD_HALF, 5) - 1.0


# --- Group E (041-050): Runs tests and sign autocorrelation ---

def rac_041_sign_ac_lag1_21d(close: pd.Series) -> pd.Series:
    """Autocorrelation of return sign at lag 1 over 21-day window."""
    r = _log_returns(close)
    return _sign_autocorr(r, _TD_MON, 1)


def rac_042_sign_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of return sign at lag 1 over 63-day window."""
    r = _log_returns(close)
    return _sign_autocorr(r, _TD_QTR, 1)


def rac_043_sign_ac_lag1_126d(close: pd.Series) -> pd.Series:
    """Autocorrelation of return sign at lag 1 over 126-day window."""
    r = _log_returns(close)
    return _sign_autocorr(r, _TD_HALF, 1)


def rac_044_sign_ac_lag2_63d(close: pd.Series) -> pd.Series:
    """Autocorrelation of return sign at lag 2 over 63-day window."""
    r = _log_returns(close)
    return _sign_autocorr(r, _TD_QTR, 2)


def rac_045_runs_ratio_21d(close: pd.Series) -> pd.Series:
    """Runs ratio (observed/expected) of return signs over 21-day window."""
    r = _log_returns(close)
    return _runs_ratio(r, _TD_MON)


def rac_046_runs_ratio_63d(close: pd.Series) -> pd.Series:
    """Runs ratio (observed/expected) of return signs over 63-day window."""
    r = _log_returns(close)
    return _runs_ratio(r, _TD_QTR)


def rac_047_runs_ratio_126d(close: pd.Series) -> pd.Series:
    """Runs ratio (observed/expected) of return signs over 126-day window."""
    r = _log_returns(close)
    return _runs_ratio(r, _TD_HALF)


def rac_048_pct_same_sign_lag1_21d(close: pd.Series) -> pd.Series:
    """Fraction of days where sign(r_t) == sign(r_{t-1}) over 21-day window."""
    r = _log_returns(close)
    same = (np.sign(r) == np.sign(r.shift(1))).astype(float)
    return _rolling_mean(same, _TD_MON)


def rac_049_pct_same_sign_lag1_63d(close: pd.Series) -> pd.Series:
    """Fraction of days where sign(r_t) == sign(r_{t-1}) over 63-day window."""
    r = _log_returns(close)
    same = (np.sign(r) == np.sign(r.shift(1))).astype(float)
    return _rolling_mean(same, _TD_QTR)


def rac_050_pct_reversal_lag1_63d(close: pd.Series) -> pd.Series:
    """Fraction of days where sign(r_t) != sign(r_{t-1}) over 63-day window (choppiness)."""
    r = _log_returns(close)
    rev = (np.sign(r) != np.sign(r.shift(1))).astype(float)
    return _rolling_mean(rev, _TD_QTR)


# --- Group F (051-060): Persistence and mean-reversion flags ---

def rac_051_ac_lag1_positive_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: lag-1 autocorrelation is positive (trending) over 63-day window."""
    r = _log_returns(close)
    return (_rolling_autocorr(r, _TD_QTR, 1) > 0).astype(float)


def rac_052_ac_lag1_negative_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: lag-1 autocorrelation is negative (mean-reverting) over 63-day window."""
    r = _log_returns(close)
    return (_rolling_autocorr(r, _TD_QTR, 1) < 0).astype(float)


def rac_053_vr5_above1_flag_126d(close: pd.Series) -> pd.Series:
    """Binary flag: variance ratio (k=5) > 1 (trending price structure) over 126-day window."""
    lp = np.log(close.replace(0, np.nan))
    return (_variance_ratio(lp, _TD_HALF, 5) > 1.0).astype(float)


def rac_054_vr5_below1_flag_126d(close: pd.Series) -> pd.Series:
    """Binary flag: variance ratio (k=5) < 1 (mean-reverting structure) over 126-day window."""
    lp = np.log(close.replace(0, np.nan))
    return (_variance_ratio(lp, _TD_HALF, 5) < 1.0).astype(float)


def rac_055_runs_below1_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: runs ratio < 1 (fewer runs than random = trending) over 63-day window."""
    r = _log_returns(close)
    return (_runs_ratio(r, _TD_QTR) < 1.0).astype(float)


def rac_056_runs_above1_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: runs ratio > 1 (more runs than random = choppy) over 63-day window."""
    r = _log_returns(close)
    return (_runs_ratio(r, _TD_QTR) > 1.0).astype(float)


def rac_057_ac_lag1_below_neg01_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: lag-1 AC < -0.1 (strong mean-reversion signal) over 63-day window."""
    r = _log_returns(close)
    return (_rolling_autocorr(r, _TD_QTR, 1) < -0.1).astype(float)


def rac_058_ac_lag1_above_01_flag_63d(close: pd.Series) -> pd.Series:
    """Binary flag: lag-1 AC > 0.1 (strong persistence) over 63-day window."""
    r = _log_returns(close)
    return (_rolling_autocorr(r, _TD_QTR, 1) > 0.1).astype(float)


def rac_059_vr2_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of VR(k=2) 63-day value within its 252-day distribution."""
    lp = np.log(close.replace(0, np.nan))
    vr = _variance_ratio(lp, _TD_QTR, 2)
    return vr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rac_060_ac_lag1_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day lag-1 AC within its 252-day distribution."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return ac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group G (061-075): Signed and time-varying serial structure ---

def rac_061_ac_lag1_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM (span=21) smoothed lag-1 autocorrelation signal."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _ewm_mean(ac, _TD_MON)


def rac_062_ac_lag1_ewm_63d(close: pd.Series) -> pd.Series:
    """EWM (span=63) smoothed lag-1 autocorrelation signal."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return _ewm_mean(ac, _TD_QTR)


def rac_063_ac_lag1_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day lag-1 AC relative to 252-day mean and std."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    m = _rolling_mean(ac, _TD_YEAR)
    s = _rolling_std(ac, _TD_YEAR)
    return _safe_div(ac - m, s)


def rac_064_sign_ac_sum_lags1_3_63d(close: pd.Series) -> pd.Series:
    """Sum of sign-AC at lags 1, 2, 3 over 63-day window."""
    r = _log_returns(close)
    total = pd.Series(0.0, index=close.index)
    for lag in range(1, 4):
        total = total + _sign_autocorr(r, _TD_QTR, lag).fillna(0.0)
    return total


def rac_065_consec_positive_ac_lag1_21d(close: pd.Series) -> pd.Series:
    """Consecutive days where 21-day lag-1 AC has been positive."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _consec_streak(ac > 0)


def rac_066_consec_negative_ac_lag1_63d(close: pd.Series) -> pd.Series:
    """Consecutive days where 63-day lag-1 AC has been negative (mean-reversion regime)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    return _consec_streak(ac < 0)


def rac_067_ac_lag1_min_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of the 21-day lag-1 AC (most negative serial structure)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_min(ac, _TD_QTR)


def rac_068_ac_lag1_max_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day maximum of the 21-day lag-1 AC."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return _rolling_max(ac, _TD_QTR)


def rac_069_vr_ratio_5_to_2_126d(close: pd.Series) -> pd.Series:
    """Ratio VR(k=5)/VR(k=2) over 126-day window (multi-horizon VR comparison)."""
    lp = np.log(close.replace(0, np.nan))
    vr5 = _variance_ratio(lp, _TD_HALF, 5)
    vr2 = _variance_ratio(lp, _TD_HALF, 2)
    return _safe_div(vr5, vr2.clip(lower=_EPS))


def rac_070_ac_lag1_times_vr5_126d(close: pd.Series) -> pd.Series:
    """Product of 63-day lag-1 AC and VR(k=5) 126-day (combined serial structure score)."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac = _rolling_autocorr(r, _TD_QTR, 1)
    vr = _variance_ratio(lp, _TD_HALF, 5)
    return ac * vr


def rac_071_lb_q4_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of the 63-day LB(4) Q-stat."""
    r = _log_returns(close)
    q = _ljung_box_stat(r, _TD_QTR, 4)
    return q.expanding(min_periods=_TD_QTR).rank(pct=True)


def rac_072_runs_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day runs ratio relative to its 252-day distribution."""
    r = _log_returns(close)
    rr = _runs_ratio(r, _TD_QTR)
    m = _rolling_mean(rr, _TD_YEAR)
    s = _rolling_std(rr, _TD_YEAR)
    return _safe_div(rr - m, s)


def rac_073_pct_same_sign_lag1_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day same-sign fraction vs its 252-day distribution."""
    r = _log_returns(close)
    same = _rolling_mean((np.sign(r) == np.sign(r.shift(1))).astype(float), _TD_MON)
    m = _rolling_mean(same, _TD_YEAR)
    s = _rolling_std(same, _TD_YEAR)
    return _safe_div(same - m, s)


def rac_074_ac_lag1_21d_min_252d(close: pd.Series) -> pd.Series:
    """Expanding minimum of 21-day lag-1 AC (all-time most negative serial structure)."""
    r = _log_returns(close)
    ac = _rolling_autocorr(r, _TD_MON, 1)
    return ac.expanding(min_periods=_TD_MON).min()


def rac_075_ac_structure_composite_63d(close: pd.Series) -> pd.Series:
    """Composite serial-structure score: lag-1 AC + (VR(k=5)-1) over 63-day window."""
    r = _log_returns(close)
    lp = np.log(close.replace(0, np.nan))
    ac1 = _rolling_autocorr(r, _TD_QTR, 1).fillna(0.0)
    vr5 = (_variance_ratio(lp, _TD_QTR, 5) - 1.0).fillna(0.0)
    return ac1 + vr5


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_AUTOCORRELATION_REGISTRY_001_075 = {
    "rac_001_ac_lag1_21d": {"inputs": ["close"], "func": rac_001_ac_lag1_21d},
    "rac_002_ac_lag1_63d": {"inputs": ["close"], "func": rac_002_ac_lag1_63d},
    "rac_003_ac_lag1_126d": {"inputs": ["close"], "func": rac_003_ac_lag1_126d},
    "rac_004_ac_lag1_252d": {"inputs": ["close"], "func": rac_004_ac_lag1_252d},
    "rac_005_ac_lag2_21d": {"inputs": ["close"], "func": rac_005_ac_lag2_21d},
    "rac_006_ac_lag2_63d": {"inputs": ["close"], "func": rac_006_ac_lag2_63d},
    "rac_007_ac_lag3_21d": {"inputs": ["close"], "func": rac_007_ac_lag3_21d},
    "rac_008_ac_lag3_63d": {"inputs": ["close"], "func": rac_008_ac_lag3_63d},
    "rac_009_ac_lag5_63d": {"inputs": ["close"], "func": rac_009_ac_lag5_63d},
    "rac_010_ac_lag5_126d": {"inputs": ["close"], "func": rac_010_ac_lag5_126d},
    "rac_011_pacf_lag1_21d": {"inputs": ["close"], "func": rac_011_pacf_lag1_21d},
    "rac_012_pacf_lag1_63d": {"inputs": ["close"], "func": rac_012_pacf_lag1_63d},
    "rac_013_pacf_lag2_63d": {"inputs": ["close"], "func": rac_013_pacf_lag2_63d},
    "rac_014_pacf_lag2_126d": {"inputs": ["close"], "func": rac_014_pacf_lag2_126d},
    "rac_015_ac_sum_lags1_5_63d": {"inputs": ["close"], "func": rac_015_ac_sum_lags1_5_63d},
    "rac_016_ac_sum_lags1_5_126d": {"inputs": ["close"], "func": rac_016_ac_sum_lags1_5_126d},
    "rac_017_ac_lag1_minus_lag2_63d": {"inputs": ["close"], "func": rac_017_ac_lag1_minus_lag2_63d},
    "rac_018_ac_lag1_sign_63d": {"inputs": ["close"], "func": rac_018_ac_lag1_sign_63d},
    "rac_019_ac_lag1_abs_63d": {"inputs": ["close"], "func": rac_019_ac_lag1_abs_63d},
    "rac_020_ac_lag1_abs_252d": {"inputs": ["close"], "func": rac_020_ac_lag1_abs_252d},
    "rac_021_lb_q4_63d": {"inputs": ["close"], "func": rac_021_lb_q4_63d},
    "rac_022_lb_q4_126d": {"inputs": ["close"], "func": rac_022_lb_q4_126d},
    "rac_023_lb_q8_126d": {"inputs": ["close"], "func": rac_023_lb_q8_126d},
    "rac_024_lb_q8_252d": {"inputs": ["close"], "func": rac_024_lb_q8_252d},
    "rac_025_lb_q4_63d_zscore_252d": {"inputs": ["close"], "func": rac_025_lb_q4_63d_zscore_252d},
    "rac_026_lb_q4_21d": {"inputs": ["close"], "func": rac_026_lb_q4_21d},
    "rac_027_lb_q2_21d": {"inputs": ["close"], "func": rac_027_lb_q2_21d},
    "rac_028_lb_q10_252d": {"inputs": ["close"], "func": rac_028_lb_q10_252d},
    "rac_029_lb_q4_pct_rank_252d": {"inputs": ["close"], "func": rac_029_lb_q4_pct_rank_252d},
    "rac_030_lb_q4_normalized_n": {"inputs": ["close"], "func": rac_030_lb_q4_normalized_n},
    "rac_031_vr_2_63d": {"inputs": ["close"], "func": rac_031_vr_2_63d},
    "rac_032_vr_5_63d": {"inputs": ["close"], "func": rac_032_vr_5_63d},
    "rac_033_vr_5_126d": {"inputs": ["close"], "func": rac_033_vr_5_126d},
    "rac_034_vr_10_126d": {"inputs": ["close"], "func": rac_034_vr_10_126d},
    "rac_035_vr_10_252d": {"inputs": ["close"], "func": rac_035_vr_10_252d},
    "rac_036_vr_21_252d": {"inputs": ["close"], "func": rac_036_vr_21_252d},
    "rac_037_vr_2_126d": {"inputs": ["close"], "func": rac_037_vr_2_126d},
    "rac_038_vr_5_252d": {"inputs": ["close"], "func": rac_038_vr_5_252d},
    "rac_039_vr_2_minus1_63d": {"inputs": ["close"], "func": rac_039_vr_2_minus1_63d},
    "rac_040_vr_5_minus1_126d": {"inputs": ["close"], "func": rac_040_vr_5_minus1_126d},
    "rac_041_sign_ac_lag1_21d": {"inputs": ["close"], "func": rac_041_sign_ac_lag1_21d},
    "rac_042_sign_ac_lag1_63d": {"inputs": ["close"], "func": rac_042_sign_ac_lag1_63d},
    "rac_043_sign_ac_lag1_126d": {"inputs": ["close"], "func": rac_043_sign_ac_lag1_126d},
    "rac_044_sign_ac_lag2_63d": {"inputs": ["close"], "func": rac_044_sign_ac_lag2_63d},
    "rac_045_runs_ratio_21d": {"inputs": ["close"], "func": rac_045_runs_ratio_21d},
    "rac_046_runs_ratio_63d": {"inputs": ["close"], "func": rac_046_runs_ratio_63d},
    "rac_047_runs_ratio_126d": {"inputs": ["close"], "func": rac_047_runs_ratio_126d},
    "rac_048_pct_same_sign_lag1_21d": {"inputs": ["close"], "func": rac_048_pct_same_sign_lag1_21d},
    "rac_049_pct_same_sign_lag1_63d": {"inputs": ["close"], "func": rac_049_pct_same_sign_lag1_63d},
    "rac_050_pct_reversal_lag1_63d": {"inputs": ["close"], "func": rac_050_pct_reversal_lag1_63d},
    "rac_051_ac_lag1_positive_flag_63d": {"inputs": ["close"], "func": rac_051_ac_lag1_positive_flag_63d},
    "rac_052_ac_lag1_negative_flag_63d": {"inputs": ["close"], "func": rac_052_ac_lag1_negative_flag_63d},
    "rac_053_vr5_above1_flag_126d": {"inputs": ["close"], "func": rac_053_vr5_above1_flag_126d},
    "rac_054_vr5_below1_flag_126d": {"inputs": ["close"], "func": rac_054_vr5_below1_flag_126d},
    "rac_055_runs_below1_flag_63d": {"inputs": ["close"], "func": rac_055_runs_below1_flag_63d},
    "rac_056_runs_above1_flag_63d": {"inputs": ["close"], "func": rac_056_runs_above1_flag_63d},
    "rac_057_ac_lag1_below_neg01_flag_63d": {"inputs": ["close"], "func": rac_057_ac_lag1_below_neg01_flag_63d},
    "rac_058_ac_lag1_above_01_flag_63d": {"inputs": ["close"], "func": rac_058_ac_lag1_above_01_flag_63d},
    "rac_059_vr2_pct_rank_252d": {"inputs": ["close"], "func": rac_059_vr2_pct_rank_252d},
    "rac_060_ac_lag1_pct_rank_252d": {"inputs": ["close"], "func": rac_060_ac_lag1_pct_rank_252d},
    "rac_061_ac_lag1_ewm_21d": {"inputs": ["close"], "func": rac_061_ac_lag1_ewm_21d},
    "rac_062_ac_lag1_ewm_63d": {"inputs": ["close"], "func": rac_062_ac_lag1_ewm_63d},
    "rac_063_ac_lag1_zscore_252d": {"inputs": ["close"], "func": rac_063_ac_lag1_zscore_252d},
    "rac_064_sign_ac_sum_lags1_3_63d": {"inputs": ["close"], "func": rac_064_sign_ac_sum_lags1_3_63d},
    "rac_065_consec_positive_ac_lag1_21d": {"inputs": ["close"], "func": rac_065_consec_positive_ac_lag1_21d},
    "rac_066_consec_negative_ac_lag1_63d": {"inputs": ["close"], "func": rac_066_consec_negative_ac_lag1_63d},
    "rac_067_ac_lag1_min_63d": {"inputs": ["close"], "func": rac_067_ac_lag1_min_63d},
    "rac_068_ac_lag1_max_63d": {"inputs": ["close"], "func": rac_068_ac_lag1_max_63d},
    "rac_069_vr_ratio_5_to_2_126d": {"inputs": ["close"], "func": rac_069_vr_ratio_5_to_2_126d},
    "rac_070_ac_lag1_times_vr5_126d": {"inputs": ["close"], "func": rac_070_ac_lag1_times_vr5_126d},
    "rac_071_lb_q4_expanding_pct_rank": {"inputs": ["close"], "func": rac_071_lb_q4_expanding_pct_rank},
    "rac_072_runs_ratio_zscore_252d": {"inputs": ["close"], "func": rac_072_runs_ratio_zscore_252d},
    "rac_073_pct_same_sign_lag1_21d_zscore_252d": {"inputs": ["close"], "func": rac_073_pct_same_sign_lag1_21d_zscore_252d},
    "rac_074_ac_lag1_21d_min_252d": {"inputs": ["close"], "func": rac_074_ac_lag1_21d_min_252d},
    "rac_075_ac_structure_composite_63d": {"inputs": ["close"], "func": rac_075_ac_structure_composite_63d},
}
