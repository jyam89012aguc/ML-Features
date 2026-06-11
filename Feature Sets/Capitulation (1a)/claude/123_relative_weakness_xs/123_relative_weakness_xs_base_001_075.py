"""
123_relative_weakness_xs — Base Features 001-075
Domain: ticker price weakness relative to sector/industry/universe peer medians
        (cross-sectional comparison) — relative return, relative drawdown,
        beta-adjusted residual weakness, peer-relative new-low frequency,
        dispersion-normalized underperformance, ranking-style distress,
        persistence of underperformance
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily price/volume Series AND a
    precomputed sector/industry peer-median Series of the same daily index.
    Peer-median series are named  peer_median_<field>  where <field> matches
    the own-ticker field name.  The pipeline computes sector/industry medians
    cross-sectionally and passes them in.

    Own price/volume inputs:        close, high, low, open, volume
    Peer-median series available:   peer_median_close, peer_median_high,
                                    peer_median_low, peer_median_volume
    (peer_median_open is not used — open is too noisy cross-sectionally.)

    All functions look strictly backward.  No forward leakage.
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
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _log_return(close: pd.Series, n: int = 1) -> pd.Series:
    """n-day log return of a price series."""
    return np.log(close / close.shift(n).replace(0, np.nan))


def _drawdown_from_peak(close: pd.Series, w: int) -> pd.Series:
    """Rolling drawdown from w-day peak: (close - peak) / peak."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw relative return vs peer median ---

def rwx_001_rel_return_1d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """1-day log return of ticker minus 1-day log return of peer median."""
    r_own  = _log_return(close, 1)
    r_peer = _log_return(peer_median_close, 1)
    return r_own - r_peer


def rwx_002_rel_return_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day log return of ticker minus 5-day log return of peer median."""
    r_own  = _log_return(close, _TD_WEEK)
    r_peer = _log_return(peer_median_close, _TD_WEEK)
    return r_own - r_peer


def rwx_003_rel_return_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day log return of ticker minus 21-day log return of peer median."""
    r_own  = _log_return(close, _TD_MON)
    r_peer = _log_return(peer_median_close, _TD_MON)
    return r_own - r_peer


def rwx_004_rel_return_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63-day log return of ticker minus 63-day log return of peer median."""
    r_own  = _log_return(close, _TD_QTR)
    r_peer = _log_return(peer_median_close, _TD_QTR)
    return r_own - r_peer


def rwx_005_rel_return_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """126-day log return of ticker minus 126-day log return of peer median."""
    r_own  = _log_return(close, _TD_HALF)
    r_peer = _log_return(peer_median_close, _TD_HALF)
    return r_own - r_peer


def rwx_006_rel_return_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252-day log return of ticker minus 252-day log return of peer median."""
    r_own  = _log_return(close, _TD_YEAR)
    r_peer = _log_return(peer_median_close, _TD_YEAR)
    return r_own - r_peer


def rwx_007_price_ratio_to_peer(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker close divided by peer-median close (raw cross-sectional price ratio)."""
    return _safe_div(close, peer_median_close)


def rwx_008_log_price_ratio_to_peer(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Log of ticker-close / peer-median-close (signed log price relative)."""
    ratio = _safe_div(close, peer_median_close)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def rwx_009_rel_return_1d_rolling_mean_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day rolling mean of daily relative return (sustained underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_mean(rel, _TD_MON)


def rwx_010_rel_return_1d_rolling_mean_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63-day rolling mean of daily relative return (quarterly underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_mean(rel, _TD_QTR)


# --- Group B (011-020): Relative drawdown vs peer median ---

def rwx_011_rel_drawdown_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker 21d drawdown from peak minus peer-median 21d drawdown from peak."""
    dd_own  = _drawdown_from_peak(close, _TD_MON)
    dd_peer = _drawdown_from_peak(peer_median_close, _TD_MON)
    return dd_own - dd_peer


def rwx_012_rel_drawdown_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker 63d drawdown from peak minus peer-median 63d drawdown from peak."""
    dd_own  = _drawdown_from_peak(close, _TD_QTR)
    dd_peer = _drawdown_from_peak(peer_median_close, _TD_QTR)
    return dd_own - dd_peer


def rwx_013_rel_drawdown_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker 252d drawdown from peak minus peer-median 252d drawdown from peak."""
    dd_own  = _drawdown_from_peak(close, _TD_YEAR)
    dd_peer = _drawdown_from_peak(peer_median_close, _TD_YEAR)
    return dd_own - dd_peer


def rwx_014_ticker_drawdown_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker's own 252-day drawdown from peak (peer series carried for contract; not used in calc)."""
    _ = peer_median_close  # contract compliance
    return _drawdown_from_peak(close, _TD_YEAR)


def rwx_015_peer_drawdown_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Peer-median 252-day drawdown from peak (how bad are peers in comparison)."""
    _ = close  # contract compliance
    return _drawdown_from_peak(peer_median_close, _TD_YEAR)


def rwx_016_rel_drawdown_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker 126d drawdown minus peer-median 126d drawdown."""
    dd_own  = _drawdown_from_peak(close, _TD_HALF)
    dd_peer = _drawdown_from_peak(peer_median_close, _TD_HALF)
    return dd_own - dd_peer


def rwx_017_drawdown_ratio_ticker_vs_peer_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ratio of ticker 252d drawdown to peer 252d drawdown (1 = same; <1 = worse)."""
    dd_own  = _drawdown_from_peak(close, _TD_YEAR).clip(upper=-_EPS)
    dd_peer = _drawdown_from_peak(peer_median_close, _TD_YEAR).clip(upper=-_EPS)
    return _safe_div(dd_own, dd_peer)


def rwx_018_rel_close_to_52w_low(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """(ticker / 252d-low) minus (peer / peer-252d-low) — distance from annual low, relative."""
    low_own  = _rolling_min(close, _TD_YEAR)
    low_peer = _rolling_min(peer_median_close, _TD_YEAR)
    dist_own  = _safe_div(close - low_own, low_own)
    dist_peer = _safe_div(peer_median_close - low_peer, low_peer)
    return dist_own - dist_peer


def rwx_019_rel_high_to_close_ratio(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Ticker (252d-high / close) minus peer (252d-high / close) — how far below its high vs peers."""
    high_own  = _rolling_max(close, _TD_YEAR)
    high_peer = _rolling_max(peer_median_close, _TD_YEAR)
    own_ratio  = _safe_div(high_own,  close)
    peer_ratio = _safe_div(high_peer, peer_median_close)
    return own_ratio - peer_ratio


def rwx_020_close_vs_peer_median_gap(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Additive gap: ticker close minus peer-median close (raw price-level difference)."""
    return close - peer_median_close


# --- Group C (021-030): Underperformance flags and counts ---

def rwx_021_underperf_1d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if ticker 1d return < peer-median 1d return."""
    return (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)


def rwx_022_underperf_5d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if ticker 5d return < peer-median 5d return."""
    return (_log_return(close, _TD_WEEK) < _log_return(peer_median_close, _TD_WEEK)).astype(float)


def rwx_023_underperf_21d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if ticker 21d return < peer-median 21d return."""
    return (_log_return(close, _TD_MON) < _log_return(peer_median_close, _TD_MON)).astype(float)


def rwx_024_underperf_63d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: 1 if ticker 63d return < peer-median 63d return."""
    return (_log_return(close, _TD_QTR) < _log_return(peer_median_close, _TD_QTR)).astype(float)


def rwx_025_consec_days_underperf_1d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Consecutive days where ticker daily return < peer-median daily return."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    return _consec_streak(flag)


def rwx_026_days_underperf_in_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where ticker daily return < peer-median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rwx_027_days_underperf_in_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where ticker daily return < peer-median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rwx_028_days_underperf_in_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where ticker daily return < peer-median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def rwx_029_frac_underperf_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Fraction of trailing 21d days where ticker underperforms peer median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_mean(flag, _TD_MON)


def rwx_030_frac_underperf_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Fraction of trailing 63d days where ticker underperforms peer median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_mean(flag, _TD_QTR)


# --- Group D (031-040): Z-score of relative return (how extreme is underperformance) ---

def rwx_031_rel_return_1d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of daily relative return over trailing 252d distribution."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _zscore_rolling(rel, _TD_YEAR)


def rwx_032_rel_return_1d_zscore_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of daily relative return over trailing 63d distribution."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _zscore_rolling(rel, _TD_QTR)


def rwx_033_rel_return_21d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 21d relative return over trailing 252d distribution."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return _zscore_rolling(rel, _TD_YEAR)


def rwx_034_rel_return_63d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 63d relative return over trailing 252d distribution."""
    rel = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    return _zscore_rolling(rel, _TD_YEAR)


def rwx_035_rel_return_1d_expanding_zscore(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding z-score of daily relative return (all-time extremity of underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    m = rel.expanding(min_periods=21).mean()
    s = rel.expanding(min_periods=21).std()
    return _safe_div(rel - m, s)


def rwx_036_rel_return_21d_zscore_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 21d relative return within trailing 63d distribution."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return _zscore_rolling(rel, _TD_QTR)


def rwx_037_rel_return_5d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 5d relative return over trailing 252d distribution."""
    rel = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    return _zscore_rolling(rel, _TD_YEAR)


def rwx_038_rel_return_5d_zscore_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 5d relative return over trailing 63d distribution."""
    rel = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    return _zscore_rolling(rel, _TD_QTR)


def rwx_039_rel_drawdown_63d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 63d relative drawdown over trailing 252d distribution."""
    rel_dd = _drawdown_from_peak(close, _TD_QTR) - _drawdown_from_peak(peer_median_close, _TD_QTR)
    return _zscore_rolling(rel_dd, _TD_YEAR)


def rwx_040_log_price_ratio_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of log(ticker/peer) over trailing 252d distribution."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _zscore_rolling(lr, _TD_YEAR)


# --- Group E (041-050): Percentile rank of relative return within rolling window ---

def rwx_041_rel_return_1d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling percentile rank of daily relative return (0=worst relative day ever in year)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_042_rel_return_1d_pctrank_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling percentile rank of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rwx_043_rel_return_21d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling percentile rank of 21d relative return."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return rel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_044_rel_return_63d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling percentile rank of 63d relative return."""
    rel = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    return rel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_045_rel_return_1d_expanding_pctrank(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.expanding(min_periods=21).rank(pct=True)


def rwx_046_frac_underperf_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d days where ticker underperforms peer median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def rwx_047_rel_return_5d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling percentile rank of 5d relative return."""
    rel = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    return rel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_048_rel_return_126d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling percentile rank of 126d relative return."""
    rel = _log_return(close, _TD_HALF) - _log_return(peer_median_close, _TD_HALF)
    return rel.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_049_log_price_ratio_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling percentile rank of log(ticker/peer) (relative price level ranking)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_050_log_price_ratio_expanding_pctrank(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of log(ticker/peer)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr.expanding(min_periods=21).rank(pct=True)


# --- Group F (051-060): Peer-relative new-low frequency and distress depth ---

def rwx_051_rel_price_new_low_21d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: ticker hits a new 21d relative-price-ratio low today."""
    ratio = _safe_div(close, peer_median_close)
    prev_min = ratio.shift(1).rolling(_TD_MON, min_periods=1).min()
    return (ratio < prev_min).astype(float)


def rwx_052_rel_price_new_low_63d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: ticker hits a new 63d relative-price-ratio low today."""
    ratio = _safe_div(close, peer_median_close)
    prev_min = ratio.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (ratio < prev_min).astype(float)


def rwx_053_rel_price_new_low_252d_flag(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Binary: ticker hits a new 252d relative-price-ratio low today."""
    ratio = _safe_div(close, peer_median_close)
    prev_min = ratio.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (ratio < prev_min).astype(float)


def rwx_054_rel_new_low_count_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where ticker set a new relative-price low."""
    ratio = _safe_div(close, peer_median_close)
    prev_min = ratio.shift(1).rolling(_TD_MON, min_periods=1).min()
    flag = (ratio < prev_min).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rwx_055_rel_new_low_count_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where ticker set a new relative-price low."""
    ratio = _safe_div(close, peer_median_close)
    prev_min = ratio.shift(1).rolling(_TD_QTR, min_periods=1).min()
    flag = (ratio < prev_min).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rwx_056_underperf_depth_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Sum of negative daily relative returns over trailing 21d (cumulative underperformance depth)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_sum(rel.clip(upper=0.0), _TD_MON)


def rwx_057_underperf_depth_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Sum of negative daily relative returns over trailing 63d."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_sum(rel.clip(upper=0.0), _TD_QTR)


def rwx_058_underperf_depth_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Sum of negative daily relative returns over trailing 252d."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_sum(rel.clip(upper=0.0), _TD_YEAR)


def rwx_059_rel_return_ewm21(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(21) of daily relative return (smooth monthly relative momentum)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_MON)


def rwx_060_rel_return_ewm63(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(63) of daily relative return (smooth quarterly relative momentum)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_QTR)


# --- Group G (061-075): Dispersion-normalized underperformance, rolling min/max, distress ---

def rwx_061_rel_return_21d_rolling_min_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling minimum of 21d relative return (worst recent monthly relative performance)."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return _rolling_min(rel, _TD_YEAR)


def rwx_062_rel_return_63d_rolling_min_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling minimum of 63d relative return."""
    rel = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    return _rolling_min(rel, _TD_YEAR)


def rwx_063_rel_return_1d_rolling_min_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling minimum of daily relative return (worst relative day in quarter)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_min(rel, _TD_QTR)


def rwx_064_rel_return_1d_rolling_min_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling minimum of daily relative return (worst relative day in year)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_min(rel, _TD_YEAR)


def rwx_065_log_price_ratio_rolling_min_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling minimum of log(ticker/peer) — how cheap has it gotten vs peers."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _rolling_min(lr, _TD_YEAR)


def rwx_066_log_price_ratio_expanding_min(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding all-time minimum of log(ticker/peer) (absolute worst relative pricing ever)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr.expanding(min_periods=1).min()


def rwx_067_rel_return_1d_std_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d rolling std of daily relative return (relative dispersion / tracking error)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_std(rel, _TD_MON)


def rwx_068_rel_return_1d_std_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling std of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_std(rel, _TD_QTR)


def rwx_069_dispersion_normalized_underperf_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d mean relative return divided by 63d std of relative return (Sharpe-like of underperf)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    mean21 = _rolling_mean(rel, _TD_MON)
    std63  = _rolling_std(rel, _TD_QTR)
    return _safe_div(mean21, std63)


def rwx_070_dispersion_normalized_underperf_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d mean relative return divided by 252d std of relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    mean63  = _rolling_mean(rel, _TD_QTR)
    std252  = _rolling_std(rel, _TD_YEAR)
    return _safe_div(mean63, std252)


def rwx_071_frac_underperf_21d_normalized_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d underperformance fraction normalized by 252d average fraction (regime-relative)."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21  = _rolling_mean(flag, _TD_MON)
    avg252  = _rolling_mean(frac21, _TD_YEAR)
    return _safe_div(frac21, avg252.clip(lower=_EPS))


def rwx_072_consec_days_underperf_1d_normalized(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Consecutive underperformance streak normalized by 63d avg streak length."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag)
    avg63  = _rolling_mean(streak, _TD_QTR)
    return _safe_div(streak, avg63.clip(lower=_EPS))


def rwx_073_rel_return_21d_distance_from_rolling_min(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Distance of current 21d relative return above its 252d rolling minimum."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    floor = _rolling_min(rel, _TD_YEAR)
    return rel - floor


def rwx_074_underperf_streak_depth_score(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Consecutive underperformance streak times magnitude of daily relative return (distress score)."""
    rel    = _log_return(close, 1) - _log_return(peer_median_close, 1)
    flag   = (rel < 0)
    streak = _consec_streak(flag)
    neg_rel = rel.clip(upper=0.0)
    return streak * neg_rel.abs()


def rwx_075_rel_return_1d_rolling_median_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63d rolling median of daily relative return (robust central tendency of underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_median(rel, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_WEAKNESS_XS_REGISTRY_001_075 = {
    "rwx_001_rel_return_1d":                          {"inputs": ["close", "peer_median_close"], "func": rwx_001_rel_return_1d},
    "rwx_002_rel_return_5d":                          {"inputs": ["close", "peer_median_close"], "func": rwx_002_rel_return_5d},
    "rwx_003_rel_return_21d":                         {"inputs": ["close", "peer_median_close"], "func": rwx_003_rel_return_21d},
    "rwx_004_rel_return_63d":                         {"inputs": ["close", "peer_median_close"], "func": rwx_004_rel_return_63d},
    "rwx_005_rel_return_126d":                        {"inputs": ["close", "peer_median_close"], "func": rwx_005_rel_return_126d},
    "rwx_006_rel_return_252d":                        {"inputs": ["close", "peer_median_close"], "func": rwx_006_rel_return_252d},
    "rwx_007_price_ratio_to_peer":                    {"inputs": ["close", "peer_median_close"], "func": rwx_007_price_ratio_to_peer},
    "rwx_008_log_price_ratio_to_peer":                {"inputs": ["close", "peer_median_close"], "func": rwx_008_log_price_ratio_to_peer},
    "rwx_009_rel_return_1d_rolling_mean_21d":         {"inputs": ["close", "peer_median_close"], "func": rwx_009_rel_return_1d_rolling_mean_21d},
    "rwx_010_rel_return_1d_rolling_mean_63d":         {"inputs": ["close", "peer_median_close"], "func": rwx_010_rel_return_1d_rolling_mean_63d},
    "rwx_011_rel_drawdown_21d":                       {"inputs": ["close", "peer_median_close"], "func": rwx_011_rel_drawdown_21d},
    "rwx_012_rel_drawdown_63d":                       {"inputs": ["close", "peer_median_close"], "func": rwx_012_rel_drawdown_63d},
    "rwx_013_rel_drawdown_252d":                      {"inputs": ["close", "peer_median_close"], "func": rwx_013_rel_drawdown_252d},
    "rwx_014_ticker_drawdown_252d":                   {"inputs": ["close", "peer_median_close"], "func": rwx_014_ticker_drawdown_252d},
    "rwx_015_peer_drawdown_252d":                     {"inputs": ["close", "peer_median_close"], "func": rwx_015_peer_drawdown_252d},
    "rwx_016_rel_drawdown_126d":                      {"inputs": ["close", "peer_median_close"], "func": rwx_016_rel_drawdown_126d},
    "rwx_017_drawdown_ratio_ticker_vs_peer_252d":     {"inputs": ["close", "peer_median_close"], "func": rwx_017_drawdown_ratio_ticker_vs_peer_252d},
    "rwx_018_rel_close_to_52w_low":                   {"inputs": ["close", "peer_median_close"], "func": rwx_018_rel_close_to_52w_low},
    "rwx_019_rel_high_to_close_ratio":                {"inputs": ["close", "peer_median_close"], "func": rwx_019_rel_high_to_close_ratio},
    "rwx_020_close_vs_peer_median_gap":               {"inputs": ["close", "peer_median_close"], "func": rwx_020_close_vs_peer_median_gap},
    "rwx_021_underperf_1d_flag":                      {"inputs": ["close", "peer_median_close"], "func": rwx_021_underperf_1d_flag},
    "rwx_022_underperf_5d_flag":                      {"inputs": ["close", "peer_median_close"], "func": rwx_022_underperf_5d_flag},
    "rwx_023_underperf_21d_flag":                     {"inputs": ["close", "peer_median_close"], "func": rwx_023_underperf_21d_flag},
    "rwx_024_underperf_63d_flag":                     {"inputs": ["close", "peer_median_close"], "func": rwx_024_underperf_63d_flag},
    "rwx_025_consec_days_underperf_1d":               {"inputs": ["close", "peer_median_close"], "func": rwx_025_consec_days_underperf_1d},
    "rwx_026_days_underperf_in_21d":                  {"inputs": ["close", "peer_median_close"], "func": rwx_026_days_underperf_in_21d},
    "rwx_027_days_underperf_in_63d":                  {"inputs": ["close", "peer_median_close"], "func": rwx_027_days_underperf_in_63d},
    "rwx_028_days_underperf_in_252d":                 {"inputs": ["close", "peer_median_close"], "func": rwx_028_days_underperf_in_252d},
    "rwx_029_frac_underperf_21d":                     {"inputs": ["close", "peer_median_close"], "func": rwx_029_frac_underperf_21d},
    "rwx_030_frac_underperf_63d":                     {"inputs": ["close", "peer_median_close"], "func": rwx_030_frac_underperf_63d},
    "rwx_031_rel_return_1d_zscore_252d":              {"inputs": ["close", "peer_median_close"], "func": rwx_031_rel_return_1d_zscore_252d},
    "rwx_032_rel_return_1d_zscore_63d":               {"inputs": ["close", "peer_median_close"], "func": rwx_032_rel_return_1d_zscore_63d},
    "rwx_033_rel_return_21d_zscore_252d":             {"inputs": ["close", "peer_median_close"], "func": rwx_033_rel_return_21d_zscore_252d},
    "rwx_034_rel_return_63d_zscore_252d":             {"inputs": ["close", "peer_median_close"], "func": rwx_034_rel_return_63d_zscore_252d},
    "rwx_035_rel_return_1d_expanding_zscore":         {"inputs": ["close", "peer_median_close"], "func": rwx_035_rel_return_1d_expanding_zscore},
    "rwx_036_rel_return_21d_zscore_63d":              {"inputs": ["close", "peer_median_close"], "func": rwx_036_rel_return_21d_zscore_63d},
    "rwx_037_rel_return_5d_zscore_252d":              {"inputs": ["close", "peer_median_close"], "func": rwx_037_rel_return_5d_zscore_252d},
    "rwx_038_rel_return_5d_zscore_63d":               {"inputs": ["close", "peer_median_close"], "func": rwx_038_rel_return_5d_zscore_63d},
    "rwx_039_rel_drawdown_63d_zscore_252d":           {"inputs": ["close", "peer_median_close"], "func": rwx_039_rel_drawdown_63d_zscore_252d},
    "rwx_040_log_price_ratio_zscore_252d":            {"inputs": ["close", "peer_median_close"], "func": rwx_040_log_price_ratio_zscore_252d},
    "rwx_041_rel_return_1d_pctrank_252d":             {"inputs": ["close", "peer_median_close"], "func": rwx_041_rel_return_1d_pctrank_252d},
    "rwx_042_rel_return_1d_pctrank_63d":              {"inputs": ["close", "peer_median_close"], "func": rwx_042_rel_return_1d_pctrank_63d},
    "rwx_043_rel_return_21d_pctrank_252d":            {"inputs": ["close", "peer_median_close"], "func": rwx_043_rel_return_21d_pctrank_252d},
    "rwx_044_rel_return_63d_pctrank_252d":            {"inputs": ["close", "peer_median_close"], "func": rwx_044_rel_return_63d_pctrank_252d},
    "rwx_045_rel_return_1d_expanding_pctrank":        {"inputs": ["close", "peer_median_close"], "func": rwx_045_rel_return_1d_expanding_pctrank},
    "rwx_046_frac_underperf_252d":                    {"inputs": ["close", "peer_median_close"], "func": rwx_046_frac_underperf_252d},
    "rwx_047_rel_return_5d_pctrank_252d":             {"inputs": ["close", "peer_median_close"], "func": rwx_047_rel_return_5d_pctrank_252d},
    "rwx_048_rel_return_126d_pctrank_252d":           {"inputs": ["close", "peer_median_close"], "func": rwx_048_rel_return_126d_pctrank_252d},
    "rwx_049_log_price_ratio_pctrank_252d":           {"inputs": ["close", "peer_median_close"], "func": rwx_049_log_price_ratio_pctrank_252d},
    "rwx_050_log_price_ratio_expanding_pctrank":      {"inputs": ["close", "peer_median_close"], "func": rwx_050_log_price_ratio_expanding_pctrank},
    "rwx_051_rel_price_new_low_21d_flag":             {"inputs": ["close", "peer_median_close"], "func": rwx_051_rel_price_new_low_21d_flag},
    "rwx_052_rel_price_new_low_63d_flag":             {"inputs": ["close", "peer_median_close"], "func": rwx_052_rel_price_new_low_63d_flag},
    "rwx_053_rel_price_new_low_252d_flag":            {"inputs": ["close", "peer_median_close"], "func": rwx_053_rel_price_new_low_252d_flag},
    "rwx_054_rel_new_low_count_21d":                  {"inputs": ["close", "peer_median_close"], "func": rwx_054_rel_new_low_count_21d},
    "rwx_055_rel_new_low_count_63d":                  {"inputs": ["close", "peer_median_close"], "func": rwx_055_rel_new_low_count_63d},
    "rwx_056_underperf_depth_21d":                    {"inputs": ["close", "peer_median_close"], "func": rwx_056_underperf_depth_21d},
    "rwx_057_underperf_depth_63d":                    {"inputs": ["close", "peer_median_close"], "func": rwx_057_underperf_depth_63d},
    "rwx_058_underperf_depth_252d":                   {"inputs": ["close", "peer_median_close"], "func": rwx_058_underperf_depth_252d},
    "rwx_059_rel_return_ewm21":                       {"inputs": ["close", "peer_median_close"], "func": rwx_059_rel_return_ewm21},
    "rwx_060_rel_return_ewm63":                       {"inputs": ["close", "peer_median_close"], "func": rwx_060_rel_return_ewm63},
    "rwx_061_rel_return_21d_rolling_min_252d":        {"inputs": ["close", "peer_median_close"], "func": rwx_061_rel_return_21d_rolling_min_252d},
    "rwx_062_rel_return_63d_rolling_min_252d":        {"inputs": ["close", "peer_median_close"], "func": rwx_062_rel_return_63d_rolling_min_252d},
    "rwx_063_rel_return_1d_rolling_min_63d":          {"inputs": ["close", "peer_median_close"], "func": rwx_063_rel_return_1d_rolling_min_63d},
    "rwx_064_rel_return_1d_rolling_min_252d":         {"inputs": ["close", "peer_median_close"], "func": rwx_064_rel_return_1d_rolling_min_252d},
    "rwx_065_log_price_ratio_rolling_min_252d":       {"inputs": ["close", "peer_median_close"], "func": rwx_065_log_price_ratio_rolling_min_252d},
    "rwx_066_log_price_ratio_expanding_min":          {"inputs": ["close", "peer_median_close"], "func": rwx_066_log_price_ratio_expanding_min},
    "rwx_067_rel_return_1d_std_21d":                  {"inputs": ["close", "peer_median_close"], "func": rwx_067_rel_return_1d_std_21d},
    "rwx_068_rel_return_1d_std_63d":                  {"inputs": ["close", "peer_median_close"], "func": rwx_068_rel_return_1d_std_63d},
    "rwx_069_dispersion_normalized_underperf_21d":    {"inputs": ["close", "peer_median_close"], "func": rwx_069_dispersion_normalized_underperf_21d},
    "rwx_070_dispersion_normalized_underperf_63d":    {"inputs": ["close", "peer_median_close"], "func": rwx_070_dispersion_normalized_underperf_63d},
    "rwx_071_frac_underperf_21d_normalized_252d":     {"inputs": ["close", "peer_median_close"], "func": rwx_071_frac_underperf_21d_normalized_252d},
    "rwx_072_consec_days_underperf_1d_normalized":    {"inputs": ["close", "peer_median_close"], "func": rwx_072_consec_days_underperf_1d_normalized},
    "rwx_073_rel_return_21d_distance_from_rolling_min": {"inputs": ["close", "peer_median_close"], "func": rwx_073_rel_return_21d_distance_from_rolling_min},
    "rwx_074_underperf_streak_depth_score":           {"inputs": ["close", "peer_median_close"], "func": rwx_074_underperf_streak_depth_score},
    "rwx_075_rel_return_1d_rolling_median_63d":       {"inputs": ["close", "peer_median_close"], "func": rwx_075_rel_return_1d_rolling_median_63d},
}
