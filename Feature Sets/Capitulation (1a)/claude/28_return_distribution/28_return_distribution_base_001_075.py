"""
28_return_distribution — Base Features 001-075
Domain: shape of the trailing return distribution — skewness, kurtosis, tail ratios,
        downside/upside dispersion shape, worst-return percentiles, fraction in extreme
        left tail, VaR/ES-style quantiles, Jarque-Bera non-normality, mean-vs-median gap,
        return autocorrelation (lags/decay/clustering/Ljung-Box aggregate).
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).quantile(q)


def _log_ret(s: pd.Series) -> pd.Series:
    """Daily log-return series."""
    return np.log(s.clip(lower=_EPS)).diff(1)


def _pct_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Autocorrelation scalar helpers (used with rolling.apply, raw=True) ────────

def _autocorr_lag_scalar(arr: np.ndarray, lag: int) -> float:
    """Pearson autocorrelation at a given lag for a raw numpy array."""
    n = len(arr)
    if n <= lag + 2:
        return np.nan
    x = arr[:-lag]
    y = arr[lag:]
    mx, my = x.mean(), y.mean()
    num = ((x - mx) * (y - my)).sum()
    denom = np.sqrt(((x - mx) ** 2).sum() * ((y - my) ** 2).sum())
    if denom < _EPS:
        return np.nan
    return num / denom


def _make_autocorr_helper(lag: int):
    def _helper(arr: np.ndarray) -> float:
        return _autocorr_lag_scalar(arr, lag)
    return _helper


_ac_lag1 = _make_autocorr_helper(1)
_ac_lag2 = _make_autocorr_helper(2)
_ac_lag3 = _make_autocorr_helper(3)
_ac_lag5 = _make_autocorr_helper(5)
_ac_lag10 = _make_autocorr_helper(10)


def _autocorr_decay_scalar(arr: np.ndarray) -> float:
    """Autocorrelation decay rate: (ac1 - ac5) / 4, measuring mean per-lag decay."""
    ac1 = _autocorr_lag_scalar(arr, 1)
    ac5 = _autocorr_lag_scalar(arr, 5)
    if np.isnan(ac1) or np.isnan(ac5):
        return np.nan
    return (ac1 - ac5) / 4.0


def _abs_autocorr_lag1_scalar(arr: np.ndarray) -> float:
    """Autocorrelation at lag-1 of absolute values (volatility clustering proxy)."""
    abs_arr = np.abs(arr)
    return _autocorr_lag_scalar(abs_arr, 1)


def _ljung_box_scalar(arr: np.ndarray, nlags: int = 5) -> float:
    """Ljung-Box-style aggregate: n*(n+2) * sum(ac_k^2 / (n-k)) for k=1..nlags."""
    n = len(arr)
    if n <= nlags + 2:
        return np.nan
    lb = 0.0
    for k in range(1, nlags + 1):
        ac = _autocorr_lag_scalar(arr, k)
        if np.isnan(ac):
            return np.nan
        denom = n - k
        if denom <= 0:
            return np.nan
        lb += ac * ac / denom
    return n * (n + 2) * lb


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Rolling skewness of daily log-returns ---

def rds_001_skew_logret_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of daily log-returns."""
    return _rolling_skew(_log_ret(close), _TD_MON)


def rds_002_skew_logret_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of daily log-returns."""
    return _rolling_skew(_log_ret(close), _TD_QTR)


def rds_003_skew_logret_126d(close: pd.Series) -> pd.Series:
    """Rolling 126-day skewness of daily log-returns."""
    return _rolling_skew(_log_ret(close), _TD_HALF)


def rds_004_skew_logret_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of daily log-returns."""
    return _rolling_skew(_log_ret(close), _TD_YEAR)


def rds_005_skew_pctret_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day skewness of daily pct-returns."""
    return _rolling_skew(_pct_ret(close), _TD_MON)


def rds_006_skew_pctret_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day skewness of daily pct-returns."""
    return _rolling_skew(_pct_ret(close), _TD_QTR)


def rds_007_skew_logret_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day log-return skewness within trailing 252-day distribution."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    return sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_008_skew_logret_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day log-return skewness within trailing 252-day distribution."""
    sk = _rolling_skew(_log_ret(close), _TD_QTR)
    return sk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_009_skew_logret_expanding(close: pd.Series) -> pd.Series:
    """Expanding-window skewness of daily log-returns (all-history shape)."""
    r = _log_ret(close)
    return r.expanding(min_periods=10).skew()


def rds_010_skew_logret_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day log-return skewness relative to its 252-day distribution."""
    sk = _rolling_skew(_log_ret(close), _TD_MON)
    m = _rolling_mean(sk, _TD_YEAR)
    s = _rolling_std(sk, _TD_YEAR)
    return _safe_div(sk - m, s)


# --- Group B (011-020): Rolling excess kurtosis of daily log-returns ---

def rds_011_kurt_logret_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day excess kurtosis of daily log-returns."""
    return _rolling_kurt(_log_ret(close), _TD_MON)


def rds_012_kurt_logret_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day excess kurtosis of daily log-returns."""
    return _rolling_kurt(_log_ret(close), _TD_QTR)


def rds_013_kurt_logret_126d(close: pd.Series) -> pd.Series:
    """Rolling 126-day excess kurtosis of daily log-returns."""
    return _rolling_kurt(_log_ret(close), _TD_HALF)


def rds_014_kurt_logret_252d(close: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of daily log-returns."""
    return _rolling_kurt(_log_ret(close), _TD_YEAR)


def rds_015_kurt_pctret_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day excess kurtosis of daily pct-returns."""
    return _rolling_kurt(_pct_ret(close), _TD_QTR)


def rds_016_kurt_logret_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day kurtosis within trailing 252-day distribution."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    return kt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_017_kurt_logret_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day kurtosis within trailing 252-day distribution."""
    kt = _rolling_kurt(_log_ret(close), _TD_QTR)
    return kt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_018_kurt_logret_expanding(close: pd.Series) -> pd.Series:
    """Expanding-window excess kurtosis of daily log-returns."""
    r = _log_ret(close)
    return r.expanding(min_periods=10).kurt()


def rds_019_kurt_logret_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day log-return kurtosis relative to its 252-day distribution."""
    kt = _rolling_kurt(_log_ret(close), _TD_MON)
    m = _rolling_mean(kt, _TD_YEAR)
    s = _rolling_std(kt, _TD_YEAR)
    return _safe_div(kt - m, s)


def rds_020_skew_kurt_product_63d(close: pd.Series) -> pd.Series:
    """Product of 63-day skewness and kurtosis (joint shape extremity)."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    return sk * kt


# --- Group C (021-030): Tail ratios and left-tail fraction ---

def rds_021_tail_ratio_5pct_95pct_63d(close: pd.Series) -> pd.Series:
    """63-day ratio of 5th-pct return to 95th-pct return (left/right tail balance)."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    q95 = _rolling_quantile(r, _TD_QTR, 0.95)
    return _safe_div(q05.abs(), q95.abs())


def rds_022_tail_ratio_5pct_95pct_252d(close: pd.Series) -> pd.Series:
    """252-day ratio of 5th-pct return to 95th-pct return."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_YEAR, 0.05)
    q95 = _rolling_quantile(r, _TD_YEAR, 0.95)
    return _safe_div(q05.abs(), q95.abs())


def rds_023_tail_ratio_1pct_99pct_252d(close: pd.Series) -> pd.Series:
    """252-day ratio of 1st-pct return to 99th-pct return (extreme tail balance)."""
    r = _log_ret(close)
    q01 = _rolling_quantile(r, _TD_YEAR, 0.01)
    q99 = _rolling_quantile(r, _TD_YEAR, 0.99)
    return _safe_div(q01.abs(), q99.abs())


def rds_024_left_tail_fraction_2sigma_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21-day returns below 2-sigma on the downside (fat left tail probe)."""
    r = _log_ret(close)
    m = _rolling_mean(r, _TD_MON)
    s = _rolling_std(r, _TD_MON)
    threshold = m - 2.0 * s
    in_tail = (r < threshold).astype(float)
    return _rolling_mean(in_tail, _TD_MON)


def rds_025_left_tail_fraction_2sigma_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day returns below 2-sigma on the downside."""
    r = _log_ret(close)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    threshold = m - 2.0 * s
    in_tail = (r < threshold).astype(float)
    return _rolling_mean(in_tail, _TD_QTR)


def rds_026_left_tail_fraction_2sigma_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252-day returns below 2-sigma on the downside."""
    r = _log_ret(close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    threshold = m - 2.0 * s
    in_tail = (r < threshold).astype(float)
    return _rolling_mean(in_tail, _TD_YEAR)


def rds_027_left_tail_fraction_3sigma_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252-day returns below 3-sigma on the downside (extreme fat tail)."""
    r = _log_ret(close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    threshold = m - 3.0 * s
    in_tail = (r < threshold).astype(float)
    return _rolling_mean(in_tail, _TD_YEAR)


def rds_028_tail_ratio_10pct_90pct_21d(close: pd.Series) -> pd.Series:
    """21-day ratio of 10th-pct to 90th-pct return magnitude."""
    r = _log_ret(close)
    q10 = _rolling_quantile(r, _TD_MON, 0.10)
    q90 = _rolling_quantile(r, _TD_MON, 0.90)
    return _safe_div(q10.abs(), q90.abs())


def rds_029_right_tail_fraction_2sigma_63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day returns above 2-sigma on the upside (right tail)."""
    r = _log_ret(close)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    threshold = m + 2.0 * s
    in_tail = (r > threshold).astype(float)
    return _rolling_mean(in_tail, _TD_QTR)


def rds_030_left_minus_right_tail_frac_63d(close: pd.Series) -> pd.Series:
    """63-day left-tail fraction minus right-tail fraction (asymmetric tail dominance)."""
    return rds_025_left_tail_fraction_2sigma_63d(close) - rds_029_right_tail_fraction_2sigma_63d(close)


# --- Group D (031-040): Worst-return percentiles (VaR-style quantiles) ---

def rds_031_var_1pct_21d(close: pd.Series) -> pd.Series:
    """1% Value-at-Risk of daily log-returns over trailing 21 days."""
    return _rolling_quantile(_log_ret(close), _TD_MON, 0.01)


def rds_032_var_5pct_21d(close: pd.Series) -> pd.Series:
    """5% Value-at-Risk of daily log-returns over trailing 21 days."""
    return _rolling_quantile(_log_ret(close), _TD_MON, 0.05)


def rds_033_var_5pct_63d(close: pd.Series) -> pd.Series:
    """5% Value-at-Risk of daily log-returns over trailing 63 days."""
    return _rolling_quantile(_log_ret(close), _TD_QTR, 0.05)


def rds_034_var_5pct_252d(close: pd.Series) -> pd.Series:
    """5% Value-at-Risk of daily log-returns over trailing 252 days."""
    return _rolling_quantile(_log_ret(close), _TD_YEAR, 0.05)


def rds_035_var_1pct_252d(close: pd.Series) -> pd.Series:
    """1% Value-at-Risk of daily log-returns over trailing 252 days."""
    return _rolling_quantile(_log_ret(close), _TD_YEAR, 0.01)


def rds_036_var_10pct_63d(close: pd.Series) -> pd.Series:
    """10% Value-at-Risk of daily log-returns over trailing 63 days."""
    return _rolling_quantile(_log_ret(close), _TD_QTR, 0.10)


def rds_037_var_1pct_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day 1%-VaR within its 252-day distribution."""
    v = rds_031_var_1pct_21d(close)
    return v.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_038_var_5pct_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day 5%-VaR relative to its 252-day distribution."""
    v = rds_032_var_5pct_21d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def rds_039_var_ratio_1pct_to_5pct_63d(close: pd.Series) -> pd.Series:
    """Ratio of 1%-VaR to 5%-VaR over 63 days (tail steepness index)."""
    r = _log_ret(close)
    q01 = _rolling_quantile(r, _TD_QTR, 0.01)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    return _safe_div(q01, q05)


def rds_040_var_5pct_vs_mean_63d(close: pd.Series) -> pd.Series:
    """63-day 5%-VaR minus mean return (VaR in mean-excess terms)."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    m = _rolling_mean(r, _TD_QTR)
    return q05 - m


# --- Group E (041-050): Expected Shortfall / CVaR-style tail mean ---

def rds_041_cvar_5pct_21d(close: pd.Series) -> pd.Series:
    """21-day expected shortfall: mean return of days below 5th percentile."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_MON, 0.05)
    tail = r.where(r < q05, np.nan)
    return tail.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).mean()


def rds_042_cvar_5pct_63d(close: pd.Series) -> pd.Series:
    """63-day expected shortfall: mean of returns below 5th percentile."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_QTR, 0.05)
    tail = r.where(r < q05, np.nan)
    return tail.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()


def rds_043_cvar_5pct_252d(close: pd.Series) -> pd.Series:
    """252-day expected shortfall: mean of returns below 5th percentile."""
    r = _log_ret(close)
    q05 = _rolling_quantile(r, _TD_YEAR, 0.05)
    tail = r.where(r < q05, np.nan)
    return tail.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean()


def rds_044_cvar_1pct_252d(close: pd.Series) -> pd.Series:
    """252-day expected shortfall at 1% threshold."""
    r = _log_ret(close)
    q01 = _rolling_quantile(r, _TD_YEAR, 0.01)
    tail = r.where(r < q01, np.nan)
    return tail.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).mean()


def rds_045_cvar_10pct_63d(close: pd.Series) -> pd.Series:
    """63-day expected shortfall at 10% threshold."""
    r = _log_ret(close)
    q10 = _rolling_quantile(r, _TD_QTR, 0.10)
    tail = r.where(r < q10, np.nan)
    return tail.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).mean()


def rds_046_cvar_5pct_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day CVaR-5% within trailing 252-day distribution."""
    cv = rds_041_cvar_5pct_21d(close)
    return cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_047_cvar_vs_var_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of CVaR-5% to VaR-5% over 63 days (tail shape beyond threshold)."""
    return _safe_div(rds_042_cvar_5pct_63d(close), rds_033_var_5pct_63d(close))


def rds_048_cvar_5pct_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day CVaR-5% relative to its 252-day distribution."""
    cv = rds_041_cvar_5pct_21d(close)
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s)


def rds_049_cvar_expanding_5pct(close: pd.Series) -> pd.Series:
    """Expanding CVaR-5%: mean return of days in the worst 5% all-time."""
    r = _log_ret(close)
    q05 = r.expanding(min_periods=10).quantile(0.05)
    tail = r.where(r < q05, np.nan)
    return tail.expanding(min_periods=10).mean()


def rds_050_cvar_10pct_minus_cvar_5pct_63d(close: pd.Series) -> pd.Series:
    """63-day CVaR-10% minus CVaR-5% (shape of inner vs extreme left tail)."""
    return rds_045_cvar_10pct_63d(close) - rds_042_cvar_5pct_63d(close)


# --- Group F (051-060): Downside vs upside dispersion shape ---

def rds_051_downside_std_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day std of returns on down days only."""
    r = _log_ret(close)
    down = r.where(r < 0, np.nan)
    return down.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()


def rds_052_upside_std_21d(close: pd.Series) -> pd.Series:
    """Rolling 21-day std of returns on up days only."""
    r = _log_ret(close)
    up = r.where(r > 0, np.nan)
    return up.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()


def rds_053_downside_std_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day std of returns on down days only."""
    r = _log_ret(close)
    down = r.where(r < 0, np.nan)
    return down.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()


def rds_054_upside_std_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day std of returns on up days only."""
    r = _log_ret(close)
    up = r.where(r > 0, np.nan)
    return up.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).std()


def rds_055_down_vs_up_std_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of downside std to upside std over 21 days (asymmetric volatility shape)."""
    return _safe_div(rds_051_downside_std_21d(close), rds_052_upside_std_21d(close))


def rds_056_down_vs_up_std_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of downside std to upside std over 63 days."""
    return _safe_div(rds_053_downside_std_63d(close), rds_054_upside_std_63d(close))


def rds_057_down_vs_up_std_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of downside std to upside std over 252 days."""
    r = _log_ret(close)
    dn_std = r.where(r < 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    up_std = r.where(r > 0, np.nan).rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    return _safe_div(dn_std, up_std)


def rds_058_down_std_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day downside std within its 252-day distribution."""
    ds = rds_051_downside_std_21d(close)
    return ds.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_059_down_vs_up_std_ratio_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day downside/upside std ratio in 252-day distribution."""
    ratio = rds_055_down_vs_up_std_ratio_21d(close)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rds_060_down_std_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day downside std relative to its 252-day distribution."""
    ds = rds_051_downside_std_21d(close)
    m = _rolling_mean(ds, _TD_YEAR)
    s = _rolling_std(ds, _TD_YEAR)
    return _safe_div(ds - m, s)


# --- Group G (061-066): Mean-vs-median gap and Jarque-Bera non-normality ---

def rds_061_mean_minus_median_ret_21d(close: pd.Series) -> pd.Series:
    """21-day mean log-return minus median log-return (skew proxy via location gap)."""
    r = _log_ret(close)
    return _rolling_mean(r, _TD_MON) - _rolling_median(r, _TD_MON)


def rds_062_mean_minus_median_norm_std_63d(close: pd.Series) -> pd.Series:
    """63-day (mean - median) / std (Pearson skewness approximation)."""
    r = _log_ret(close)
    m = _rolling_mean(r, _TD_QTR)
    med = _rolling_median(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(m - med, s)


def rds_063_jarque_bera_stat_63d(close: pd.Series) -> pd.Series:
    """63-day Jarque-Bera statistic: n/6*(sk^2 + (ku)^2/4)."""
    r = _log_ret(close)
    n = _TD_QTR
    sk = _rolling_skew(r, n)
    ku = _rolling_kurt(r, n)
    return (n / 6.0) * (sk ** 2 + (ku ** 2) / 4.0)


def rds_064_jarque_bera_stat_252d(close: pd.Series) -> pd.Series:
    """252-day Jarque-Bera statistic approximation."""
    r = _log_ret(close)
    n = _TD_YEAR
    sk = _rolling_skew(r, n)
    ku = _rolling_kurt(r, n)
    return (n / 6.0) * (sk ** 2 + (ku ** 2) / 4.0)


def rds_065_skew_negative_flag_63d(close: pd.Series) -> pd.Series:
    """Flag: 63-day log-return skewness is negative."""
    return (rds_002_skew_logret_63d(close) < 0).astype(float)


def rds_066_skew_kurt_composite_distress_63d(close: pd.Series) -> pd.Series:
    """63-day composite distress: (-skewness) * (kurtosis + 3) as fat-left-tail proxy."""
    r = _log_ret(close)
    sk = _rolling_skew(r, _TD_QTR)
    kt = _rolling_kurt(r, _TD_QTR)
    return (-sk) * (kt + 3.0)


# --- Group H (067-075): Return autocorrelation (lags, decay, clustering, Ljung-Box) ---

def rds_067_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of daily log-returns at lag 1."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_ac_lag1, raw=True)


def rds_068_autocorr_lag1_126d(close: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of daily log-returns at lag 1."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(15, _TD_HALF // 2)).apply(_ac_lag1, raw=True)


def rds_069_autocorr_lag2_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of daily log-returns at lag 2."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_ac_lag2, raw=True)


def rds_070_autocorr_lag3_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of daily log-returns at lag 3."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_ac_lag3, raw=True)


def rds_071_autocorr_lag5_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day autocorrelation of daily log-returns at lag 5 (weekly)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(_ac_lag5, raw=True)


def rds_072_autocorr_lag10_126d(close: pd.Series) -> pd.Series:
    """Rolling 126-day autocorrelation of daily log-returns at lag 10 (biweekly)."""
    r = _log_ret(close)
    return r.rolling(_TD_HALF, min_periods=max(20, _TD_HALF // 2)).apply(_ac_lag10, raw=True)


def rds_073_autocorr_decay_rate_63d(close: pd.Series) -> pd.Series:
    """63-day autocorrelation decay rate: (ac_lag1 - ac_lag5) / 4 per lag."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _autocorr_decay_scalar, raw=True
    )


def rds_074_abs_ret_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day lag-1 autocorrelation of |returns| (volatility clustering proxy)."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _abs_autocorr_lag1_scalar, raw=True
    )


def rds_075_ljung_box_5lag_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day Ljung-Box aggregate of autocorrelations at lags 1-5."""
    r = _log_ret(close)
    return r.rolling(_TD_QTR, min_periods=max(15, _TD_QTR // 2)).apply(
        _ljung_box_scalar, raw=True
    )


# ── Registry ──────────────────────────────────────────────────────────────────

RETURN_DISTRIBUTION_REGISTRY_001_075 = {
    "rds_001_skew_logret_21d": {"inputs": ["close"], "func": rds_001_skew_logret_21d},
    "rds_002_skew_logret_63d": {"inputs": ["close"], "func": rds_002_skew_logret_63d},
    "rds_003_skew_logret_126d": {"inputs": ["close"], "func": rds_003_skew_logret_126d},
    "rds_004_skew_logret_252d": {"inputs": ["close"], "func": rds_004_skew_logret_252d},
    "rds_005_skew_pctret_21d": {"inputs": ["close"], "func": rds_005_skew_pctret_21d},
    "rds_006_skew_pctret_63d": {"inputs": ["close"], "func": rds_006_skew_pctret_63d},
    "rds_007_skew_logret_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_007_skew_logret_21d_pct_rank_252d},
    "rds_008_skew_logret_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_008_skew_logret_63d_pct_rank_252d},
    "rds_009_skew_logret_expanding": {"inputs": ["close"], "func": rds_009_skew_logret_expanding},
    "rds_010_skew_logret_21d_zscore_252d": {"inputs": ["close"], "func": rds_010_skew_logret_21d_zscore_252d},
    "rds_011_kurt_logret_21d": {"inputs": ["close"], "func": rds_011_kurt_logret_21d},
    "rds_012_kurt_logret_63d": {"inputs": ["close"], "func": rds_012_kurt_logret_63d},
    "rds_013_kurt_logret_126d": {"inputs": ["close"], "func": rds_013_kurt_logret_126d},
    "rds_014_kurt_logret_252d": {"inputs": ["close"], "func": rds_014_kurt_logret_252d},
    "rds_015_kurt_pctret_63d": {"inputs": ["close"], "func": rds_015_kurt_pctret_63d},
    "rds_016_kurt_logret_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_016_kurt_logret_21d_pct_rank_252d},
    "rds_017_kurt_logret_63d_pct_rank_252d": {"inputs": ["close"], "func": rds_017_kurt_logret_63d_pct_rank_252d},
    "rds_018_kurt_logret_expanding": {"inputs": ["close"], "func": rds_018_kurt_logret_expanding},
    "rds_019_kurt_logret_21d_zscore_252d": {"inputs": ["close"], "func": rds_019_kurt_logret_21d_zscore_252d},
    "rds_020_skew_kurt_product_63d": {"inputs": ["close"], "func": rds_020_skew_kurt_product_63d},
    "rds_021_tail_ratio_5pct_95pct_63d": {"inputs": ["close"], "func": rds_021_tail_ratio_5pct_95pct_63d},
    "rds_022_tail_ratio_5pct_95pct_252d": {"inputs": ["close"], "func": rds_022_tail_ratio_5pct_95pct_252d},
    "rds_023_tail_ratio_1pct_99pct_252d": {"inputs": ["close"], "func": rds_023_tail_ratio_1pct_99pct_252d},
    "rds_024_left_tail_fraction_2sigma_21d": {"inputs": ["close"], "func": rds_024_left_tail_fraction_2sigma_21d},
    "rds_025_left_tail_fraction_2sigma_63d": {"inputs": ["close"], "func": rds_025_left_tail_fraction_2sigma_63d},
    "rds_026_left_tail_fraction_2sigma_252d": {"inputs": ["close"], "func": rds_026_left_tail_fraction_2sigma_252d},
    "rds_027_left_tail_fraction_3sigma_252d": {"inputs": ["close"], "func": rds_027_left_tail_fraction_3sigma_252d},
    "rds_028_tail_ratio_10pct_90pct_21d": {"inputs": ["close"], "func": rds_028_tail_ratio_10pct_90pct_21d},
    "rds_029_right_tail_fraction_2sigma_63d": {"inputs": ["close"], "func": rds_029_right_tail_fraction_2sigma_63d},
    "rds_030_left_minus_right_tail_frac_63d": {"inputs": ["close"], "func": rds_030_left_minus_right_tail_frac_63d},
    "rds_031_var_1pct_21d": {"inputs": ["close"], "func": rds_031_var_1pct_21d},
    "rds_032_var_5pct_21d": {"inputs": ["close"], "func": rds_032_var_5pct_21d},
    "rds_033_var_5pct_63d": {"inputs": ["close"], "func": rds_033_var_5pct_63d},
    "rds_034_var_5pct_252d": {"inputs": ["close"], "func": rds_034_var_5pct_252d},
    "rds_035_var_1pct_252d": {"inputs": ["close"], "func": rds_035_var_1pct_252d},
    "rds_036_var_10pct_63d": {"inputs": ["close"], "func": rds_036_var_10pct_63d},
    "rds_037_var_1pct_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_037_var_1pct_21d_pct_rank_252d},
    "rds_038_var_5pct_21d_zscore_252d": {"inputs": ["close"], "func": rds_038_var_5pct_21d_zscore_252d},
    "rds_039_var_ratio_1pct_to_5pct_63d": {"inputs": ["close"], "func": rds_039_var_ratio_1pct_to_5pct_63d},
    "rds_040_var_5pct_vs_mean_63d": {"inputs": ["close"], "func": rds_040_var_5pct_vs_mean_63d},
    "rds_041_cvar_5pct_21d": {"inputs": ["close"], "func": rds_041_cvar_5pct_21d},
    "rds_042_cvar_5pct_63d": {"inputs": ["close"], "func": rds_042_cvar_5pct_63d},
    "rds_043_cvar_5pct_252d": {"inputs": ["close"], "func": rds_043_cvar_5pct_252d},
    "rds_044_cvar_1pct_252d": {"inputs": ["close"], "func": rds_044_cvar_1pct_252d},
    "rds_045_cvar_10pct_63d": {"inputs": ["close"], "func": rds_045_cvar_10pct_63d},
    "rds_046_cvar_5pct_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_046_cvar_5pct_21d_pct_rank_252d},
    "rds_047_cvar_vs_var_ratio_63d": {"inputs": ["close"], "func": rds_047_cvar_vs_var_ratio_63d},
    "rds_048_cvar_5pct_21d_zscore_252d": {"inputs": ["close"], "func": rds_048_cvar_5pct_21d_zscore_252d},
    "rds_049_cvar_expanding_5pct": {"inputs": ["close"], "func": rds_049_cvar_expanding_5pct},
    "rds_050_cvar_10pct_minus_cvar_5pct_63d": {"inputs": ["close"], "func": rds_050_cvar_10pct_minus_cvar_5pct_63d},
    "rds_051_downside_std_21d": {"inputs": ["close"], "func": rds_051_downside_std_21d},
    "rds_052_upside_std_21d": {"inputs": ["close"], "func": rds_052_upside_std_21d},
    "rds_053_downside_std_63d": {"inputs": ["close"], "func": rds_053_downside_std_63d},
    "rds_054_upside_std_63d": {"inputs": ["close"], "func": rds_054_upside_std_63d},
    "rds_055_down_vs_up_std_ratio_21d": {"inputs": ["close"], "func": rds_055_down_vs_up_std_ratio_21d},
    "rds_056_down_vs_up_std_ratio_63d": {"inputs": ["close"], "func": rds_056_down_vs_up_std_ratio_63d},
    "rds_057_down_vs_up_std_ratio_252d": {"inputs": ["close"], "func": rds_057_down_vs_up_std_ratio_252d},
    "rds_058_down_std_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_058_down_std_21d_pct_rank_252d},
    "rds_059_down_vs_up_std_ratio_21d_pct_rank_252d": {"inputs": ["close"], "func": rds_059_down_vs_up_std_ratio_21d_pct_rank_252d},
    "rds_060_down_std_zscore_252d": {"inputs": ["close"], "func": rds_060_down_std_zscore_252d},
    "rds_061_mean_minus_median_ret_21d": {"inputs": ["close"], "func": rds_061_mean_minus_median_ret_21d},
    "rds_062_mean_minus_median_norm_std_63d": {"inputs": ["close"], "func": rds_062_mean_minus_median_norm_std_63d},
    "rds_063_jarque_bera_stat_63d": {"inputs": ["close"], "func": rds_063_jarque_bera_stat_63d},
    "rds_064_jarque_bera_stat_252d": {"inputs": ["close"], "func": rds_064_jarque_bera_stat_252d},
    "rds_065_skew_negative_flag_63d": {"inputs": ["close"], "func": rds_065_skew_negative_flag_63d},
    "rds_066_skew_kurt_composite_distress_63d": {"inputs": ["close"], "func": rds_066_skew_kurt_composite_distress_63d},
    "rds_067_autocorr_lag1_63d": {"inputs": ["close"], "func": rds_067_autocorr_lag1_63d},
    "rds_068_autocorr_lag1_126d": {"inputs": ["close"], "func": rds_068_autocorr_lag1_126d},
    "rds_069_autocorr_lag2_63d": {"inputs": ["close"], "func": rds_069_autocorr_lag2_63d},
    "rds_070_autocorr_lag3_63d": {"inputs": ["close"], "func": rds_070_autocorr_lag3_63d},
    "rds_071_autocorr_lag5_63d": {"inputs": ["close"], "func": rds_071_autocorr_lag5_63d},
    "rds_072_autocorr_lag10_126d": {"inputs": ["close"], "func": rds_072_autocorr_lag10_126d},
    "rds_073_autocorr_decay_rate_63d": {"inputs": ["close"], "func": rds_073_autocorr_decay_rate_63d},
    "rds_074_abs_ret_autocorr_lag1_63d": {"inputs": ["close"], "func": rds_074_abs_ret_autocorr_lag1_63d},
    "rds_075_ljung_box_5lag_63d": {"inputs": ["close"], "func": rds_075_ljung_box_5lag_63d},
}
