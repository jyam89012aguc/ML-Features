"""
39_intraday_range — Extended Features 001-075
Domain: daily high-low spread — new windows, normalized range variants, range percentile
        ranks on additional windows, range distribution shape on additional windows,
        range vs volume relationships (new angles), range z-scores on new windows,
        Garman-Klass / Parkinson volatility proxies, intraday position measures, and
        range-weighted composite signals oriented toward capitulation detection.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _hl_range_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily high-low range normalized by close price."""
    return _safe_div(high - low, close)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Alternative window averages (10d, 42d, 126d, 189d) ---

def idr_ext_001_avg_range_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day average of close-normalized high-low range (bi-weekly window)."""
    return _rolling_mean(_hl_range_over_close(high, low, close), 10)


def idr_ext_002_avg_range_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """42-day (2-month) average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), 42)


def idr_ext_003_avg_range_189d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """189-day (3-quarter) average of close-normalized high-low range."""
    return _rolling_mean(_hl_range_over_close(high, low, close), 189)


def idr_ext_004_avg_range_ewm_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=5) of close-normalized range (fast exponential average)."""
    return _ewm_mean(_hl_range_over_close(high, low, close), _TD_WEEK)


def idr_ext_005_avg_range_ewm_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=126) of close-normalized range (half-year exponential average)."""
    return _ewm_mean(_hl_range_over_close(high, low, close), _TD_HALF)


def idr_ext_006_avg_range_ewm_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM (span=252) of close-normalized range (full-year exponential average)."""
    return _ewm_mean(_hl_range_over_close(high, low, close), _TD_YEAR)


def idr_ext_007_range_vs_avg_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 10-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, 10))


def idr_ext_008_range_vs_avg_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 42-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, 42))


def idr_ext_009_range_vs_avg_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by 126-day average range."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _rolling_mean(r, _TD_HALF))


def idr_ext_010_range_vs_ewm_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's normalized range divided by EWM(21) range (vs exponential baseline)."""
    r = _hl_range_over_close(high, low, close)
    return _safe_div(r, _ewm_mean(r, _TD_MON))


# --- Group B (011-020): Percentile ranks on new windows ---

def idr_ext_011_range_pct_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 5 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_WEEK, min_periods=1).rank(pct=True)


def idr_ext_012_range_pct_rank_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 10 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(10, min_periods=max(1, 5)).rank(pct=True)


def idr_ext_013_range_pct_rank_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 42 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(42, min_periods=max(1, 21)).rank(pct=True)


def idr_ext_014_range_pct_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of today's normalized range within trailing 126 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def idr_ext_015_range_pct_rank_expanding(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of today's normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.expanding(min_periods=1).rank(pct=True)


def idr_ext_016_range_pct_rank_10d_vs_252d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-day percentile rank minus 252-day percentile rank (short vs long context)."""
    r = _hl_range_over_close(high, low, close)
    p10 = r.rolling(10, min_periods=5).rank(pct=True)
    p252 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return p10 - p252


def idr_ext_017_range_pct_rank_21d_vs_252d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day percentile rank minus 252-day percentile rank (near vs long context)."""
    r = _hl_range_over_close(high, low, close)
    p21 = r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    p252 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    return p21 - p252


def idr_ext_018_range_pct_rank_above_75_flag_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: today's range above 75th percentile of 126-day window."""
    r = _hl_range_over_close(high, low, close)
    p75 = r.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).quantile(0.75)
    return (r > p75).astype(float)


def idr_ext_019_range_pct_rank_above_90_flag_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: today's range above 90th percentile of 252-day window (extreme range)."""
    r = _hl_range_over_close(high, low, close)
    p90 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    return (r > p90).astype(float)


def idr_ext_020_extreme_range_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in trailing 252 days where range exceeds 90th percentile of that window."""
    r = _hl_range_over_close(high, low, close)
    p90 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    return _rolling_sum((r > p90).astype(float), _TD_YEAR)


# --- Group C (021-030): Z-scores on new windows ---

def idr_ext_021_range_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 5-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_WEEK)
    s = _rolling_std(r, _TD_WEEK)
    return _safe_div(r - m, s)


def idr_ext_022_range_zscore_10d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 10-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, 10)
    s = _rolling_std(r, 10)
    return _safe_div(r - m, s)


def idr_ext_023_range_zscore_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 42-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, 42)
    s = _rolling_std(r, 42)
    return _safe_div(r - m, s)


def idr_ext_024_range_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of today's normalized range vs trailing 126-day distribution."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_HALF)
    s = _rolling_std(r, _TD_HALF)
    return _safe_div(r - m, s)


def idr_ext_025_range_zscore_expanding(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of today's normalized range."""
    r = _hl_range_over_close(high, low, close)
    m = r.expanding(min_periods=5).mean()
    s = r.expanding(min_periods=5).std()
    return _safe_div(r - m, s)


def idr_ext_026_range_zscore_abs_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 21-day range z-score (extremity, direction-agnostic)."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_MON)
    s = _rolling_std(r, _TD_MON)
    return _safe_div(r - m, s).abs()


def idr_ext_027_range_zscore_abs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of 252-day range z-score."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s).abs()


def idr_ext_028_range_zscore_composite_abs(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average absolute z-score across 21d, 63d, 126d, 252d windows."""
    r = _hl_range_over_close(high, low, close)
    z21 = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON)).abs()
    z63 = _safe_div(r - _rolling_mean(r, _TD_QTR), _rolling_std(r, _TD_QTR)).abs()
    z126 = _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF)).abs()
    z252 = _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR)).abs()
    return (z21 + z63 + z126 + z252) / 4.0


def idr_ext_029_range_ewm_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of EWM(21) range relative to 63-day rolling mean/std of EWM(21)."""
    r_ewm = _ewm_mean(_hl_range_over_close(high, low, close), _TD_MON)
    m = _rolling_mean(r_ewm, _TD_QTR)
    s = _rolling_std(r_ewm, _TD_QTR)
    return _safe_div(r_ewm - m, s)


def idr_ext_030_range_median_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Modified z-score using median and MAD over 63 days (robust outlier detection)."""
    r = _hl_range_over_close(high, low, close)
    med = _rolling_median(r, _TD_QTR)
    mad = (r - med).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    return _safe_div(r - med, mad * 1.4826 + _EPS)


# --- Group D (031-040): Parkinson / Garman-Klass volatility proxies ---

def idr_ext_031_parkinson_vol_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day Parkinson volatility estimator: sqrt(mean(log(H/L)^2) / (4*ln2))."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    sq = log_hl ** 2
    pv = np.sqrt(_rolling_mean(sq, _TD_MON) / (4.0 * np.log(2.0) + _EPS))
    return pv


def idr_ext_032_parkinson_vol_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day Parkinson volatility estimator."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    sq = log_hl ** 2
    return np.sqrt(_rolling_mean(sq, _TD_QTR) / (4.0 * np.log(2.0) + _EPS))


def idr_ext_033_parkinson_vol_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day Parkinson volatility estimator."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    sq = log_hl ** 2
    return np.sqrt(_rolling_mean(sq, _TD_YEAR) / (4.0 * np.log(2.0) + _EPS))


def idr_ext_034_gk_vol_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day Garman-Klass volatility: 0.5*(log(H/L))^2 - (2ln2-1)*(log(C/O))^2."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    log_co = np.log((close / open.replace(0, np.nan)).clip(lower=_EPS))
    gk_daily = 0.5 * log_hl ** 2 - (2.0 * np.log(2.0) - 1.0) * log_co ** 2
    return np.sqrt(_rolling_mean(gk_daily.clip(lower=0), _TD_MON))


def idr_ext_035_gk_vol_63d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day Garman-Klass volatility estimator."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    log_co = np.log((close / open.replace(0, np.nan)).clip(lower=_EPS))
    gk_daily = 0.5 * log_hl ** 2 - (2.0 * np.log(2.0) - 1.0) * log_co ** 2
    return np.sqrt(_rolling_mean(gk_daily.clip(lower=0), _TD_QTR))


def idr_ext_036_parkinson_vol_21d_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day z-score of 21-day Parkinson volatility."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    pv21 = np.sqrt(_rolling_mean(log_hl ** 2, _TD_MON) / (4.0 * np.log(2.0) + _EPS))
    m = _rolling_mean(pv21, _TD_YEAR)
    s = _rolling_std(pv21, _TD_YEAR)
    return _safe_div(pv21 - m, s)


def idr_ext_037_parkinson_vs_realized_vol_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson(21d) divided by close-return realized vol(21d) — range vol premium."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    pv = np.sqrt(_rolling_mean(log_hl ** 2, _TD_MON) / (4.0 * np.log(2.0) + _EPS))
    log_ret = np.log((close / close.shift(1).replace(0, np.nan)).clip(lower=_EPS))
    rv = _rolling_std(log_ret, _TD_MON)
    return _safe_div(pv, rv)


def idr_ext_038_log_range_21d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of log(H-L normalized by close) — log-scale range level."""
    r = _hl_range_over_close(high, low, close).clip(lower=_EPS)
    return _rolling_mean(np.log(r), _TD_MON)


def idr_ext_039_log_range_63d_mean(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean of log(H-L normalized by close)."""
    r = _hl_range_over_close(high, low, close).clip(lower=_EPS)
    return _rolling_mean(np.log(r), _TD_QTR)


def idr_ext_040_log_range_std_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day std of log(normalized range) — log-scale range dispersion."""
    r = _hl_range_over_close(high, low, close).clip(lower=_EPS)
    return _rolling_std(np.log(r), _TD_QTR)


# --- Group E (041-050): Intraday position measures ---

def idr_ext_041_close_position_in_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within day's range: (close - low) / (high - low), 0=low end."""
    rng = (high - low).replace(0, np.nan)
    return _safe_div(close - low, rng)


def idr_ext_042_avg_close_position_in_range_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day average of close's position within day's range."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _rolling_mean(pos, _TD_MON)


def idr_ext_043_avg_close_position_in_range_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day average of close's position within day's range."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _rolling_mean(pos, _TD_QTR)


def idr_ext_044_close_pos_in_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of close position in range vs 63-day distribution."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    m = _rolling_mean(pos, _TD_QTR)
    s = _rolling_std(pos, _TD_QTR)
    return _safe_div(pos - m, s)


def idr_ext_045_close_pos_in_range_pct_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day percentile rank of close's position within range."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return pos.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def idr_ext_046_open_position_in_range(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Open position within day's range: (open - low) / (high - low)."""
    rng = (high - low).replace(0, np.nan)
    return _safe_div(open - low, rng).clip(0, 1)


def idr_ext_047_avg_open_position_in_range_21d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average of open's position within day's range."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(open - low, rng).clip(0, 1)
    return _rolling_mean(pos, _TD_MON)


def idr_ext_048_close_vs_open_in_range_diff_21d(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day avg of (close position - open position) in range: intraday directional drift."""
    rng = (high - low).replace(0, np.nan)
    close_pos = _safe_div(close - low, rng)
    open_pos = _safe_div(open - low, rng).clip(0, 1)
    return _rolling_mean(close_pos - open_pos, _TD_MON)


def idr_ext_049_close_near_low_flag_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in 21d where close is in bottom 25% of day's range (bearish closes)."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _rolling_sum((pos < 0.25).astype(float), _TD_MON)


def idr_ext_050_close_near_low_fraction_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of days in 63d where close is in bottom 25% of day's range."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    return _safe_div(_rolling_sum((pos < 0.25).astype(float), _TD_QTR), pd.Series(_TD_QTR, index=close.index))


# --- Group F (051-060): Range vs volume — new angles ---

def idr_ext_051_range_vol_elasticity_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day ratio of range pct-change to volume pct-change (range-vol elasticity)."""
    r = _hl_range_over_close(high, low, close)
    r_pct = r.pct_change(1)
    v_pct = volume.pct_change(1)
    return _rolling_mean(_safe_div(r_pct, v_pct.replace(0, np.nan)), _TD_MON)


def idr_ext_052_range_vol_zscore_diff_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day z-score of range minus 21-day z-score of volume (range-vol divergence)."""
    r = _hl_range_over_close(high, low, close)
    zr = _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))
    zv = _safe_div(volume - _rolling_mean(volume, _TD_MON), _rolling_std(volume, _TD_MON))
    return zr - zv


def idr_ext_053_range_vol_product_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day z-score of (normalized range × volume) product."""
    rv = _hl_range_over_close(high, low, close) * volume
    m = _rolling_mean(rv, _TD_QTR)
    s = _rolling_std(rv, _TD_QTR)
    return _safe_div(rv - m, s)


def idr_ext_054_range_vol_product_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day percentile rank of normalized range × volume product."""
    rv = _hl_range_over_close(high, low, close) * volume
    return rv.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def idr_ext_055_low_vol_high_range_flag_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days with above-avg range but below-avg volume (thin-market expansion)."""
    r = _hl_range_over_close(high, low, close)
    avg_r = _rolling_mean(r, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    flag = ((r > avg_r) & (volume < avg_v)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def idr_ext_056_vol_weighted_range_sum_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted sum of normalized range (VWAP-style range accumulation)."""
    r = _hl_range_over_close(high, low, close)
    vol_sum = _rolling_sum(volume, _TD_MON).replace(0, np.nan)
    return _safe_div(_rolling_sum(r * volume, _TD_MON), vol_sum)


def idr_ext_057_vol_weighted_range_sum_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day volume-weighted average normalized range."""
    r = _hl_range_over_close(high, low, close)
    vol_sum = _rolling_sum(volume, _TD_QTR).replace(0, np.nan)
    return _safe_div(_rolling_sum(r * volume, _TD_QTR), vol_sum)


def idr_ext_058_range_per_log_volume_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg of normalized range divided by log(volume) — scaled illiquidity."""
    r = _hl_range_over_close(high, low, close)
    log_vol = np.log(volume.clip(lower=1.0))
    return _rolling_mean(_safe_div(r, log_vol), _TD_MON)


def idr_ext_059_range_vol_corr_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day rolling Pearson correlation between normalized range and volume."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_HALF, min_periods=max(3, _TD_HALF // 2)).corr(volume)


def idr_ext_060_range_times_vol_pct_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day percentile rank of range × volume (distress pressure ranking)."""
    rv = _hl_range_over_close(high, low, close) * volume
    return rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


# --- Group G (061-075): Distribution shape, range-return relationship, composites ---

def idr_ext_061_range_skew_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling skewness of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()


def idr_ext_062_range_skew_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """126-day rolling skewness of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_HALF, min_periods=max(3, _TD_HALF // 2)).skew()


def idr_ext_063_range_kurt_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day rolling excess kurtosis of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).kurt()


def idr_ext_064_range_kurt_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """126-day rolling excess kurtosis of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_HALF, min_periods=max(4, _TD_HALF // 2)).kurt()


def idr_ext_065_range_kurt_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling excess kurtosis of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 2)).kurt()


def idr_ext_066_range_quantile_90_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """90th-percentile normalized range over trailing 21 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.90)


def idr_ext_067_range_quantile_10_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10th-percentile normalized range over trailing 21 days."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).quantile(0.10)


def idr_ext_068_range_iqr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day interquartile range (Q75-Q25) of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    q75 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def idr_ext_069_range_iqr_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day interquartile range of normalized range distribution."""
    r = _hl_range_over_close(high, low, close)
    q75 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def idr_ext_070_range_to_close_return_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day avg normalized range divided by abs(21-day price return): noise-to-signal."""
    r = _hl_range_over_close(high, low, close)
    ret21 = close.pct_change(_TD_MON).abs()
    return _rolling_mean(_safe_div(r, ret21.replace(0, np.nan)), _TD_MON)


def idr_ext_071_range_autocorr_lag2_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling autocorrelation at lag-2 of normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(
        lambda x: float(np.corrcoef(x[:-2], x[2:])[0, 1]) if len(x) > 3 else np.nan, raw=True
    )


def idr_ext_072_range_autocorr_lag5_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling autocorrelation at lag-5 of normalized range."""
    r = _hl_range_over_close(high, low, close)
    return r.rolling(_TD_QTR, min_periods=max(7, _TD_QTR // 2)).apply(
        lambda x: float(np.corrcoef(x[:-5], x[5:])[0, 1]) if len(x) > 6 else np.nan, raw=True
    )


def idr_ext_073_range_consec_above_2xavg_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where range > 2x 63-day median (panic count)."""
    r = _hl_range_over_close(high, low, close)
    med = _rolling_median(r, _TD_QTR)
    return _rolling_sum((r > 2.0 * med).astype(float), _TD_QTR)


def idr_ext_074_range_capitulation_score_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation score: 252d z-score of range × 252d pct-rank × down-day fraction.
    Combines extremity, historical rarity, and bearish direction."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z252 = _safe_div(r - m, s).clip(lower=0)
    p252 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    is_dn = (close < close.shift(1)).astype(float)
    dn_frac = _rolling_mean(is_dn, _TD_MON)
    return z252 * p252 * dn_frac


def idr_ext_075_range_distress_extended_composite(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extended distress composite: avg of 5d/21d/63d z-scores of range × vol, scaled by
    down-close fraction and close-near-low fraction — multi-horizon capitulation signal."""
    r = _hl_range_over_close(high, low, close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol)
    rv = r * vol_norm
    z5 = _safe_div(rv - _rolling_mean(rv, _TD_WEEK), _rolling_std(rv, _TD_WEEK))
    z21 = _safe_div(rv - _rolling_mean(rv, _TD_MON), _rolling_std(rv, _TD_MON))
    z63 = _safe_div(rv - _rolling_mean(rv, _TD_QTR), _rolling_std(rv, _TD_QTR))
    z_avg = (z5 + z21 + z63) / 3.0
    is_dn = (close < close.shift(1)).astype(float)
    dn_frac = _rolling_mean(is_dn, _TD_MON)
    rng = (high - low).replace(0, np.nan)
    cl_near_low = (close - low) / rng
    cl_bias = 1.0 - _rolling_mean(cl_near_low, _TD_MON).fillna(0.5)
    return z_avg * (1.0 + dn_frac) * (1.0 + cl_bias)


# ── Registry ──────────────────────────────────────────────────────────────────

INTRADAY_RANGE_EXTENDED_REGISTRY_001_075 = {
    "idr_ext_001_avg_range_10d": {"inputs": ["high", "low", "close"], "func": idr_ext_001_avg_range_10d},
    "idr_ext_002_avg_range_42d": {"inputs": ["high", "low", "close"], "func": idr_ext_002_avg_range_42d},
    "idr_ext_003_avg_range_189d": {"inputs": ["high", "low", "close"], "func": idr_ext_003_avg_range_189d},
    "idr_ext_004_avg_range_ewm_5d": {"inputs": ["high", "low", "close"], "func": idr_ext_004_avg_range_ewm_5d},
    "idr_ext_005_avg_range_ewm_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_005_avg_range_ewm_126d},
    "idr_ext_006_avg_range_ewm_252d": {"inputs": ["high", "low", "close"], "func": idr_ext_006_avg_range_ewm_252d},
    "idr_ext_007_range_vs_avg_10d": {"inputs": ["high", "low", "close"], "func": idr_ext_007_range_vs_avg_10d},
    "idr_ext_008_range_vs_avg_42d": {"inputs": ["high", "low", "close"], "func": idr_ext_008_range_vs_avg_42d},
    "idr_ext_009_range_vs_avg_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_009_range_vs_avg_126d},
    "idr_ext_010_range_vs_ewm_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_010_range_vs_ewm_21d},
    "idr_ext_011_range_pct_rank_5d": {"inputs": ["high", "low", "close"], "func": idr_ext_011_range_pct_rank_5d},
    "idr_ext_012_range_pct_rank_10d": {"inputs": ["high", "low", "close"], "func": idr_ext_012_range_pct_rank_10d},
    "idr_ext_013_range_pct_rank_42d": {"inputs": ["high", "low", "close"], "func": idr_ext_013_range_pct_rank_42d},
    "idr_ext_014_range_pct_rank_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_014_range_pct_rank_126d},
    "idr_ext_015_range_pct_rank_expanding": {"inputs": ["high", "low", "close"], "func": idr_ext_015_range_pct_rank_expanding},
    "idr_ext_016_range_pct_rank_10d_vs_252d_diff": {"inputs": ["high", "low", "close"], "func": idr_ext_016_range_pct_rank_10d_vs_252d_diff},
    "idr_ext_017_range_pct_rank_21d_vs_252d_diff": {"inputs": ["high", "low", "close"], "func": idr_ext_017_range_pct_rank_21d_vs_252d_diff},
    "idr_ext_018_range_pct_rank_above_75_flag_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_018_range_pct_rank_above_75_flag_126d},
    "idr_ext_019_range_pct_rank_above_90_flag_252d": {"inputs": ["high", "low", "close"], "func": idr_ext_019_range_pct_rank_above_90_flag_252d},
    "idr_ext_020_extreme_range_count_252d": {"inputs": ["high", "low", "close"], "func": idr_ext_020_extreme_range_count_252d},
    "idr_ext_021_range_zscore_5d": {"inputs": ["high", "low", "close"], "func": idr_ext_021_range_zscore_5d},
    "idr_ext_022_range_zscore_10d": {"inputs": ["high", "low", "close"], "func": idr_ext_022_range_zscore_10d},
    "idr_ext_023_range_zscore_42d": {"inputs": ["high", "low", "close"], "func": idr_ext_023_range_zscore_42d},
    "idr_ext_024_range_zscore_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_024_range_zscore_126d},
    "idr_ext_025_range_zscore_expanding": {"inputs": ["high", "low", "close"], "func": idr_ext_025_range_zscore_expanding},
    "idr_ext_026_range_zscore_abs_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_026_range_zscore_abs_21d},
    "idr_ext_027_range_zscore_abs_252d": {"inputs": ["high", "low", "close"], "func": idr_ext_027_range_zscore_abs_252d},
    "idr_ext_028_range_zscore_composite_abs": {"inputs": ["high", "low", "close"], "func": idr_ext_028_range_zscore_composite_abs},
    "idr_ext_029_range_ewm_zscore_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_029_range_ewm_zscore_21d},
    "idr_ext_030_range_median_zscore_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_030_range_median_zscore_63d},
    "idr_ext_031_parkinson_vol_21d": {"inputs": ["high", "low"], "func": idr_ext_031_parkinson_vol_21d},
    "idr_ext_032_parkinson_vol_63d": {"inputs": ["high", "low"], "func": idr_ext_032_parkinson_vol_63d},
    "idr_ext_033_parkinson_vol_252d": {"inputs": ["high", "low"], "func": idr_ext_033_parkinson_vol_252d},
    "idr_ext_034_gk_vol_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_ext_034_gk_vol_21d},
    "idr_ext_035_gk_vol_63d": {"inputs": ["high", "low", "close", "open"], "func": idr_ext_035_gk_vol_63d},
    "idr_ext_036_parkinson_vol_21d_zscore_252d": {"inputs": ["high", "low"], "func": idr_ext_036_parkinson_vol_21d_zscore_252d},
    "idr_ext_037_parkinson_vs_realized_vol_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_037_parkinson_vs_realized_vol_21d},
    "idr_ext_038_log_range_21d_mean": {"inputs": ["high", "low", "close"], "func": idr_ext_038_log_range_21d_mean},
    "idr_ext_039_log_range_63d_mean": {"inputs": ["high", "low", "close"], "func": idr_ext_039_log_range_63d_mean},
    "idr_ext_040_log_range_std_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_040_log_range_std_63d},
    "idr_ext_041_close_position_in_range": {"inputs": ["high", "low", "close"], "func": idr_ext_041_close_position_in_range},
    "idr_ext_042_avg_close_position_in_range_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_042_avg_close_position_in_range_21d},
    "idr_ext_043_avg_close_position_in_range_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_043_avg_close_position_in_range_63d},
    "idr_ext_044_close_pos_in_range_zscore_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_044_close_pos_in_range_zscore_63d},
    "idr_ext_045_close_pos_in_range_pct_rank_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_045_close_pos_in_range_pct_rank_63d},
    "idr_ext_046_open_position_in_range": {"inputs": ["high", "low", "open"], "func": idr_ext_046_open_position_in_range},
    "idr_ext_047_avg_open_position_in_range_21d": {"inputs": ["high", "low", "open"], "func": idr_ext_047_avg_open_position_in_range_21d},
    "idr_ext_048_close_vs_open_in_range_diff_21d": {"inputs": ["high", "low", "close", "open"], "func": idr_ext_048_close_vs_open_in_range_diff_21d},
    "idr_ext_049_close_near_low_flag_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_049_close_near_low_flag_21d},
    "idr_ext_050_close_near_low_fraction_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_050_close_near_low_fraction_63d},
    "idr_ext_051_range_vol_elasticity_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_051_range_vol_elasticity_21d},
    "idr_ext_052_range_vol_zscore_diff_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_052_range_vol_zscore_diff_21d},
    "idr_ext_053_range_vol_product_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_053_range_vol_product_zscore_63d},
    "idr_ext_054_range_vol_product_pct_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_054_range_vol_product_pct_rank_252d},
    "idr_ext_055_low_vol_high_range_flag_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_055_low_vol_high_range_flag_21d},
    "idr_ext_056_vol_weighted_range_sum_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_056_vol_weighted_range_sum_21d},
    "idr_ext_057_vol_weighted_range_sum_63d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_057_vol_weighted_range_sum_63d},
    "idr_ext_058_range_per_log_volume_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_058_range_per_log_volume_21d},
    "idr_ext_059_range_vol_corr_126d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_059_range_vol_corr_126d},
    "idr_ext_060_range_times_vol_pct_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_060_range_times_vol_pct_rank_63d},
    "idr_ext_061_range_skew_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_061_range_skew_21d},
    "idr_ext_062_range_skew_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_062_range_skew_126d},
    "idr_ext_063_range_kurt_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_063_range_kurt_21d},
    "idr_ext_064_range_kurt_126d": {"inputs": ["high", "low", "close"], "func": idr_ext_064_range_kurt_126d},
    "idr_ext_065_range_kurt_252d": {"inputs": ["high", "low", "close"], "func": idr_ext_065_range_kurt_252d},
    "idr_ext_066_range_quantile_90_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_066_range_quantile_90_21d},
    "idr_ext_067_range_quantile_10_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_067_range_quantile_10_21d},
    "idr_ext_068_range_iqr_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_068_range_iqr_63d},
    "idr_ext_069_range_iqr_252d": {"inputs": ["high", "low", "close"], "func": idr_ext_069_range_iqr_252d},
    "idr_ext_070_range_to_close_return_ratio_21d": {"inputs": ["high", "low", "close"], "func": idr_ext_070_range_to_close_return_ratio_21d},
    "idr_ext_071_range_autocorr_lag2_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_071_range_autocorr_lag2_63d},
    "idr_ext_072_range_autocorr_lag5_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_072_range_autocorr_lag5_63d},
    "idr_ext_073_range_consec_above_2xavg_63d": {"inputs": ["high", "low", "close"], "func": idr_ext_073_range_consec_above_2xavg_63d},
    "idr_ext_074_range_capitulation_score_21d": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_074_range_capitulation_score_21d},
    "idr_ext_075_range_distress_extended_composite": {"inputs": ["high", "low", "close", "volume"], "func": idr_ext_075_range_distress_extended_composite},
}
