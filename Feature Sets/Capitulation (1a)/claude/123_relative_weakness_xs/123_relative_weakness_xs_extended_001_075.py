"""
123_relative_weakness_xs — Extended Features 001-075
Domain: ticker price weakness relative to sector/industry/universe peer medians
        (cross-sectional comparison) — additional cross-sectional variants:
        high/low composite cross-sectional weakness, volume-relative distress,
        multi-metric ranked distress, peer-adjusted momentum, dispersion metrics,
        EWM variants, higher-order rolling stats of relative return
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily price/volume Series AND a
    precomputed sector/industry peer-median Series of the same daily index.
    Peer-median series are named  peer_median_<field>  where <field> matches
    the own-ticker field name.

    Own price/volume inputs:        close, high, low, open, volume
    Peer-median series available:   peer_median_close, peer_median_high,
                                    peer_median_low, peer_median_volume

    Extended features extend beyond the 150 base features with additional
    variants, combinations, and perspectives on cross-sectional weakness.
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


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Alternate window relative returns ---

def rwx_ext_001_rel_return_3d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """3-day log return of ticker minus 3-day log return of peer median."""
    return _log_return(close, 3) - _log_return(peer_median_close, 3)


def rwx_ext_002_rel_return_10d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """10-day log return of ticker minus 10-day log return of peer median."""
    return _log_return(close, 10) - _log_return(peer_median_close, 10)


def rwx_ext_003_rel_return_42d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """42-day log return of ticker minus peer (2-month)."""
    return _log_return(close, 42) - _log_return(peer_median_close, 42)


def rwx_ext_004_rel_return_189d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """189-day log return of ticker minus peer (9-month)."""
    return _log_return(close, 189) - _log_return(peer_median_close, 189)


def rwx_ext_005_rel_return_1d_rolling_mean_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day rolling mean of daily relative return (weekly smoothed underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_mean(rel, _TD_WEEK)


def rwx_ext_006_rel_return_1d_rolling_mean_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252-day rolling mean of daily relative return (annual average underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_mean(rel, _TD_YEAR)


def rwx_ext_007_rel_return_5d_rolling_mean_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """63-day rolling mean of 5d relative return."""
    rel = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    return _rolling_mean(rel, _TD_QTR)


def rwx_ext_008_rel_return_21d_rolling_mean_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252-day rolling mean of 21d relative return."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return _rolling_mean(rel, _TD_YEAR)


def rwx_ext_009_rel_return_1d_pctrank_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d rolling percentile rank of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def rwx_ext_010_rel_return_1d_pctrank_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """126d rolling percentile rank of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): Alternate z-score windows ---

def rwx_ext_011_rel_return_1d_zscore_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of daily relative return within trailing 21d distribution."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _zscore_rolling(rel, _TD_MON)


def rwx_ext_012_rel_return_1d_zscore_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of daily relative return within trailing 126d distribution."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _zscore_rolling(rel, _TD_HALF)


def rwx_ext_013_rel_return_5d_zscore_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 5d relative return within trailing 21d distribution."""
    rel = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    return _zscore_rolling(rel, _TD_MON)


def rwx_ext_014_rel_return_126d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 126d relative return within trailing 252d distribution."""
    rel = _log_return(close, _TD_HALF) - _log_return(peer_median_close, _TD_HALF)
    return _zscore_rolling(rel, _TD_YEAR)


def rwx_ext_015_log_price_ratio_zscore_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of log(ticker/peer) within trailing 63d distribution."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _zscore_rolling(lr, _TD_QTR)


def rwx_ext_016_rel_return_1d_expanding_pctrank_zscore(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding z-score of daily relative-return expanding pctrank (extremity of rank itself)."""
    rel  = _log_return(close, 1) - _log_return(peer_median_close, 1)
    pr   = rel.expanding(min_periods=21).rank(pct=True)
    return _zscore_rolling(pr, _TD_YEAR)


def rwx_ext_017_rel_return_21d_expanding_zscore(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding z-score of 21d relative return."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    m   = rel.expanding(min_periods=21).mean()
    s   = rel.expanding(min_periods=21).std()
    return _safe_div(rel - m, s)


def rwx_ext_018_rel_return_63d_zscore_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 63d relative return within its own trailing 63d distribution."""
    rel = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    return _zscore_rolling(rel, _TD_QTR)


def rwx_ext_019_rel_return_5d_expanding_zscore(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Expanding z-score of 5d relative return (all-time extremity)."""
    rel = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    m   = rel.expanding(min_periods=10).mean()
    s   = rel.expanding(min_periods=10).std()
    return _safe_div(rel - m, s)


def rwx_ext_020_rel_drawdown_21d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 21d relative drawdown within trailing 252d distribution."""
    rel_dd = _drawdown_from_peak(close, _TD_MON) - _drawdown_from_peak(peer_median_close, _TD_MON)
    return _zscore_rolling(rel_dd, _TD_YEAR)


# --- Group C (021-030): Alternate underperformance fraction windows ---

def rwx_ext_021_days_underperf_in_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 5d where ticker daily return < peer median (weekly count)."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def rwx_ext_022_frac_underperf_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Fraction of trailing 5d days where ticker underperforms peer median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_mean(flag, _TD_WEEK)


def rwx_ext_023_frac_underperf_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Fraction of trailing 126d days where ticker underperforms peer median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_mean(flag, _TD_HALF)


def rwx_ext_024_consec_days_underperf_normalized_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Consecutive underperformance streak normalized by 252d average streak length."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag)
    avg252 = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg252.clip(lower=_EPS))


def rwx_ext_025_frac_underperf_21d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 21d underperformance fraction within trailing 252d distribution."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21 = _rolling_mean(flag, _TD_MON)
    return _zscore_rolling(frac21, _TD_YEAR)


def rwx_ext_026_frac_underperf_63d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 63d underperformance fraction within trailing 252d distribution."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac63 = _rolling_mean(flag, _TD_QTR)
    return _zscore_rolling(frac63, _TD_YEAR)


def rwx_ext_027_days_underperf_in_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of days in trailing 126d where ticker daily return < peer median."""
    flag = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    return _rolling_sum(flag, _TD_HALF)


def rwx_ext_028_underperf_streak_max_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Maximum consecutive underperformance streak length within trailing 21d."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag)
    return _rolling_max(streak, _TD_MON)


def rwx_ext_029_underperf_streak_max_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Maximum consecutive underperformance streak length within trailing 63d."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag)
    return _rolling_max(streak, _TD_QTR)


def rwx_ext_030_underperf_depth_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Sum of negative daily relative returns over trailing 126d."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_sum(rel.clip(upper=0.0), _TD_HALF)


# --- Group D (031-040): Additional high/low cross-sectional metrics ---

def rwx_ext_031_rel_high_return_5d(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """5d return of ticker high minus 5d return of peer-median high."""
    return _log_return(high, _TD_WEEK) - _log_return(peer_median_high, _TD_WEEK)


def rwx_ext_032_rel_low_return_5d(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """5d return of ticker low minus 5d return of peer-median low."""
    return _log_return(low, _TD_WEEK) - _log_return(peer_median_low, _TD_WEEK)


def rwx_ext_033_rel_low_return_252d(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """252d return of ticker low minus 252d return of peer-median low."""
    return _log_return(low, _TD_YEAR) - _log_return(peer_median_low, _TD_YEAR)


def rwx_ext_034_rel_high_return_252d(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """252d return of ticker high minus 252d return of peer-median high."""
    return _log_return(high, _TD_YEAR) - _log_return(peer_median_high, _TD_YEAR)


def rwx_ext_035_rel_low_to_peer_low_ratio(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """Log of (ticker low / peer low) — how much lower ticker's low is vs peers."""
    ratio = _safe_div(low, peer_median_low)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def rwx_ext_036_rel_range_vs_peer_range(high: pd.Series, low: pd.Series,
                                         peer_median_high: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """Ticker daily range (high-low) divided by peer daily range (relative intraday range)."""
    own_range  = (high - low).clip(lower=0.0)
    peer_range = (peer_median_high - peer_median_low).clip(lower=0.0)
    return _safe_div(own_range, peer_range.clip(lower=_EPS))


def rwx_ext_037_rel_range_vs_peer_range_21d(high: pd.Series, low: pd.Series,
                                              peer_median_high: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """21d rolling mean of ticker daily range / peer daily range."""
    own_range  = (high - low).clip(lower=0.0)
    peer_range = (peer_median_high - peer_median_low).clip(lower=0.0)
    ratio      = _safe_div(own_range, peer_range.clip(lower=_EPS))
    return _rolling_mean(ratio, _TD_MON)


def rwx_ext_038_low_vs_peer_close_ratio(low: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Log of (ticker low / peer close) — how deep ticker's intraday lows go vs peer close."""
    ratio = _safe_div(low, peer_median_close)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def rwx_ext_039_rel_high_pctrank_252d(high: pd.Series, peer_median_high: pd.Series) -> pd.Series:
    """252d pctrank of log(ticker high / peer high)."""
    lr = np.log(_safe_div(high, peer_median_high).abs().clip(lower=_EPS))
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_ext_040_rel_low_pctrank_252d(low: pd.Series, peer_median_low: pd.Series) -> pd.Series:
    """252d pctrank of log(ticker low / peer low) (0=worst relative low in year)."""
    lr = np.log(_safe_div(low, peer_median_low).abs().clip(lower=_EPS))
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): Volume-relative extended metrics ---

def rwx_ext_041_rel_volume_ratio_5d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Ticker 5d avg volume divided by peer-median 5d avg volume."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(peer_median_volume, _TD_WEEK))


def rwx_ext_042_rel_volume_ratio_252d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Ticker 252d avg volume divided by peer-median 252d avg volume."""
    return _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_mean(peer_median_volume, _TD_YEAR))


def rwx_ext_043_log_volume_ratio_zscore_252d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Z-score of log(ticker volume / peer volume) within trailing 252d distribution."""
    lr = np.log(_safe_div(volume.astype(float), peer_median_volume.astype(float)).abs().clip(lower=_EPS))
    return _zscore_rolling(lr, _TD_YEAR)


def rwx_ext_044_volume_underperf_intensity_21d(close: pd.Series, peer_median_close: pd.Series,
                                                volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """21d sum of (|negative relative return| * volume) / avg_volume (weighted underperf intensity)."""
    rel     = _log_return(close, 1) - _log_return(peer_median_close, 1)
    neg_rel = rel.clip(upper=0.0).abs()
    wt      = neg_rel * volume
    avg_vol = _rolling_mean(volume, _TD_MON)
    return _safe_div(_rolling_sum(wt, _TD_MON), avg_vol.clip(lower=_EPS))


def rwx_ext_045_high_vol_underperf_days_63d(close: pd.Series, peer_median_close: pd.Series,
                                             volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Count of days in 63d with high-volume underperformance (ticker vol > peer AND return < peer)."""
    rel      = _log_return(close, 1) - _log_return(peer_median_close, 1)
    dist_day = ((rel < 0) & (volume > peer_median_volume)).astype(float)
    return _rolling_sum(dist_day, _TD_QTR)


def rwx_ext_046_rel_volume_ratio_pctrank_252d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """252d pctrank of daily volume ratio (ticker/peer)."""
    ratio = _safe_div(volume.astype(float), peer_median_volume.astype(float))
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_ext_047_low_vol_underperf_frac_21d(close: pd.Series, peer_median_close: pd.Series,
                                            volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Fraction of 21d with low-volume underperformance (potential distribution)."""
    rel       = _log_return(close, 1) - _log_return(peer_median_close, 1)
    quiet_day = ((rel < 0) & (volume < peer_median_volume)).astype(float)
    return _rolling_mean(quiet_day, _TD_MON)


def rwx_ext_048_volume_zscore_vs_peer_21d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """Z-score of daily volume ratio within trailing 21d distribution."""
    ratio = _safe_div(volume.astype(float), peer_median_volume.astype(float))
    return _zscore_rolling(ratio, _TD_MON)


def rwx_ext_049_vol_ratio_ewm21(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """EWM(21) of daily volume ratio (ticker/peer) — smooth monthly volume relative."""
    ratio = _safe_div(volume.astype(float), peer_median_volume.astype(float))
    return _ewm_mean(ratio, _TD_MON)


def rwx_ext_050_vol_ratio_slope_21d(volume: pd.Series, peer_median_volume: pd.Series) -> pd.Series:
    """OLS slope over 21d of daily volume ratio — trend in relative volume."""
    ratio = _safe_div(volume.astype(float), peer_median_volume.astype(float))
    return _linslope(ratio, _TD_MON)


# --- Group F (051-060): Multi-input composite weakness scores ---

def rwx_ext_051_composite_close_high_low_underperf_score(
    close: pd.Series, peer_median_close: pd.Series,
    high: pd.Series, peer_median_high: pd.Series,
    low: pd.Series, peer_median_low: pd.Series
) -> pd.Series:
    """Mean of 21d relative returns for close, high, and low (multi-input weakness)."""
    r_close = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r_high  = _log_return(high, _TD_MON)   - _log_return(peer_median_high, _TD_MON)
    r_low   = _log_return(low, _TD_MON)    - _log_return(peer_median_low, _TD_MON)
    return (r_close + r_high + r_low) / 3.0


def rwx_ext_052_all_inputs_underperf_flag_21d(
    close: pd.Series, peer_median_close: pd.Series,
    high: pd.Series, peer_median_high: pd.Series,
    low: pd.Series, peer_median_low: pd.Series
) -> pd.Series:
    """Binary: 1 if 21d return of close, high, AND low all below their peer counterparts."""
    f_c = (_log_return(close, _TD_MON) < _log_return(peer_median_close, _TD_MON))
    f_h = (_log_return(high, _TD_MON)  < _log_return(peer_median_high, _TD_MON))
    f_l = (_log_return(low, _TD_MON)   < _log_return(peer_median_low, _TD_MON))
    return (f_c & f_h & f_l).astype(float)


def rwx_ext_053_composite_rel_return_4window_zscore(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 252d z-scores for 5d/21d/63d/126d relative returns."""
    r5   = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21  = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63  = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    r126 = _log_return(close, _TD_HALF) - _log_return(peer_median_close, _TD_HALF)
    z    = (_zscore_rolling(r5, _TD_YEAR) + _zscore_rolling(r21, _TD_YEAR) +
            _zscore_rolling(r63, _TD_YEAR) + _zscore_rolling(r126, _TD_YEAR)) / 4.0
    return z


def rwx_ext_054_composite_underperf_flag_5window(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Count of windows (1d/5d/21d/63d/126d) where ticker underperforms peers (0-5 score)."""
    f1   = (_log_return(close, 1)        < _log_return(peer_median_close, 1)).astype(float)
    f5   = (_log_return(close, _TD_WEEK) < _log_return(peer_median_close, _TD_WEEK)).astype(float)
    f21  = (_log_return(close, _TD_MON)  < _log_return(peer_median_close, _TD_MON)).astype(float)
    f63  = (_log_return(close, _TD_QTR)  < _log_return(peer_median_close, _TD_QTR)).astype(float)
    f126 = (_log_return(close, _TD_HALF) < _log_return(peer_median_close, _TD_HALF)).astype(float)
    return f1 + f5 + f21 + f63 + f126


def rwx_ext_055_rel_return_5d_21d_63d_weighted_score(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Weighted composite: 0.5*21d + 0.3*63d + 0.2*5d relative returns (momentum-style blend)."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    return 0.2 * r5 + 0.5 * r21 + 0.3 * r63


def rwx_ext_056_drawdown_underperf_composite(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 63d relative return z-score and 252d relative drawdown z-score."""
    r63    = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    rel_dd = _drawdown_from_peak(close, _TD_YEAR) - _drawdown_from_peak(peer_median_close, _TD_YEAR)
    z_r    = _zscore_rolling(r63, _TD_YEAR)
    z_dd   = _zscore_rolling(rel_dd, _TD_YEAR)
    return (z_r + z_dd) / 2.0


def rwx_ext_057_frac_underperf_21d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d pctrank of 21d underperformance fraction."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21 = _rolling_mean(flag, _TD_MON)
    return frac21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_ext_058_frac_underperf_63d_pctrank_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d pctrank of 63d underperformance fraction."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac63 = _rolling_mean(flag, _TD_QTR)
    return frac63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rwx_ext_059_composite_pctrank_frac_and_return(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Mean of 252d pctrank of 21d-frac-underperf and 252d pctrank of 21d rel-return."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21 = _rolling_mean(flag, _TD_MON)
    r21    = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    pr_frac = frac21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    pr_ret  = r21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (pr_frac + pr_ret) / 2.0


def rwx_ext_060_rel_return_1d_iqr_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Interquartile range of daily relative return within trailing 63d (dispersion proxy)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    q75 = rel.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = rel.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


# --- Group G (061-075): EWM and slope extended variants ---

def rwx_ext_061_rel_return_ewm5_minus_ewm63(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(5) minus EWM(63) of daily relative return (short vs long relative trend spread)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_WEEK) - _ewm_mean(rel, _TD_QTR)


def rwx_ext_062_rel_return_ewm21_minus_ewm126(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(126) of daily relative return (medium vs long trend crossover)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_MON) - _ewm_mean(rel, _TD_HALF)


def rwx_ext_063_log_price_ratio_ewm5(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(5) of log(ticker/peer) — very-short smoothed relative price level."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _ewm_mean(lr, _TD_WEEK)


def rwx_ext_064_log_price_ratio_ewm252(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """EWM(252) of log(ticker/peer) — annual smoothed relative price level."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _ewm_mean(lr, _TD_YEAR)


def rwx_ext_065_rel_return_ewm5_slope_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 5d of EWM(5) relative return (fast-moving slope of relative trend)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    ewm = _ewm_mean(rel, _TD_WEEK)
    return _linslope(ewm, _TD_WEEK)


def rwx_ext_066_rel_return_1d_slope_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 5d of daily relative return (ultra-short slope)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _linslope(rel, _TD_WEEK)


def rwx_ext_067_rel_return_1d_slope_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 252d of daily relative return (annual trend in underperformance)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _linslope(rel, _TD_YEAR)


def rwx_ext_068_log_price_ratio_slope_5d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 5d of log(ticker/peer) (fast relative price trend)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _linslope(lr, _TD_WEEK)


def rwx_ext_069_rel_drawdown_126d_zscore_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Z-score of 126d relative drawdown within trailing 252d distribution."""
    rel_dd = _drawdown_from_peak(close, _TD_HALF) - _drawdown_from_peak(peer_median_close, _TD_HALF)
    return _zscore_rolling(rel_dd, _TD_YEAR)


def rwx_ext_070_rel_close_rolling_min_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """126d rolling minimum of log(ticker/peer)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return _rolling_min(lr, _TD_HALF)


def rwx_ext_071_rel_return_1d_rolling_std_252d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """252d rolling std of daily relative return (long-run tracking error)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_std(rel, _TD_YEAR)


def rwx_ext_072_rel_return_1d_rolling_median_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21d rolling median of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _rolling_median(rel, _TD_MON)


def rwx_ext_073_rel_return_1d_vs_rolling_median_63d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Daily relative return minus its 63d rolling median (deviation from quarterly center)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel - _rolling_median(rel, _TD_QTR)


def rwx_ext_074_rel_close_distance_from_126d_floor(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Current log(ticker/peer) minus its 126d rolling minimum (distance above half-year floor)."""
    lr    = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    floor = _rolling_min(lr, _TD_HALF)
    return lr - floor


def rwx_ext_075_time_since_rel_price_new_low_126d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Days elapsed since log(ticker/peer) last hit a 126d relative low."""
    lr       = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    prev_min = lr.shift(1).rolling(_TD_HALF, min_periods=1).min()
    new_low  = (lr < prev_min).astype(float)
    idx      = pd.Series(range(len(lr)), index=lr.index, dtype=float)
    last_idx = idx.where(new_low == 1.0).ffill().fillna(0)
    return (idx - last_idx).where(~lr.isna(), np.nan)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_WEAKNESS_XS_EXTENDED_REGISTRY_001_075 = {
    "rwx_ext_001_rel_return_3d":                          {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_001_rel_return_3d},
    "rwx_ext_002_rel_return_10d":                         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_002_rel_return_10d},
    "rwx_ext_003_rel_return_42d":                         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_003_rel_return_42d},
    "rwx_ext_004_rel_return_189d":                        {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_004_rel_return_189d},
    "rwx_ext_005_rel_return_1d_rolling_mean_5d":          {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_005_rel_return_1d_rolling_mean_5d},
    "rwx_ext_006_rel_return_1d_rolling_mean_252d":        {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_006_rel_return_1d_rolling_mean_252d},
    "rwx_ext_007_rel_return_5d_rolling_mean_63d":         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_007_rel_return_5d_rolling_mean_63d},
    "rwx_ext_008_rel_return_21d_rolling_mean_252d":       {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_008_rel_return_21d_rolling_mean_252d},
    "rwx_ext_009_rel_return_1d_pctrank_21d":              {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_009_rel_return_1d_pctrank_21d},
    "rwx_ext_010_rel_return_1d_pctrank_126d":             {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_010_rel_return_1d_pctrank_126d},
    "rwx_ext_011_rel_return_1d_zscore_21d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_011_rel_return_1d_zscore_21d},
    "rwx_ext_012_rel_return_1d_zscore_126d":              {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_012_rel_return_1d_zscore_126d},
    "rwx_ext_013_rel_return_5d_zscore_21d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_013_rel_return_5d_zscore_21d},
    "rwx_ext_014_rel_return_126d_zscore_252d":            {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_014_rel_return_126d_zscore_252d},
    "rwx_ext_015_log_price_ratio_zscore_63d":             {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_015_log_price_ratio_zscore_63d},
    "rwx_ext_016_rel_return_1d_expanding_pctrank_zscore": {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_016_rel_return_1d_expanding_pctrank_zscore},
    "rwx_ext_017_rel_return_21d_expanding_zscore":        {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_017_rel_return_21d_expanding_zscore},
    "rwx_ext_018_rel_return_63d_zscore_63d":              {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_018_rel_return_63d_zscore_63d},
    "rwx_ext_019_rel_return_5d_expanding_zscore":         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_019_rel_return_5d_expanding_zscore},
    "rwx_ext_020_rel_drawdown_21d_zscore_252d":           {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_020_rel_drawdown_21d_zscore_252d},
    "rwx_ext_021_days_underperf_in_5d":                   {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_021_days_underperf_in_5d},
    "rwx_ext_022_frac_underperf_5d":                      {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_022_frac_underperf_5d},
    "rwx_ext_023_frac_underperf_126d":                    {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_023_frac_underperf_126d},
    "rwx_ext_024_consec_days_underperf_normalized_252d":  {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_024_consec_days_underperf_normalized_252d},
    "rwx_ext_025_frac_underperf_21d_zscore_252d":         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_025_frac_underperf_21d_zscore_252d},
    "rwx_ext_026_frac_underperf_63d_zscore_252d":         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_026_frac_underperf_63d_zscore_252d},
    "rwx_ext_027_days_underperf_in_126d":                 {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_027_days_underperf_in_126d},
    "rwx_ext_028_underperf_streak_max_21d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_028_underperf_streak_max_21d},
    "rwx_ext_029_underperf_streak_max_63d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_029_underperf_streak_max_63d},
    "rwx_ext_030_underperf_depth_126d":                   {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_030_underperf_depth_126d},
    "rwx_ext_031_rel_high_return_5d":                     {"inputs": ["high", "peer_median_high"],                                                                           "func": rwx_ext_031_rel_high_return_5d},
    "rwx_ext_032_rel_low_return_5d":                      {"inputs": ["low", "peer_median_low"],                                                                             "func": rwx_ext_032_rel_low_return_5d},
    "rwx_ext_033_rel_low_return_252d":                    {"inputs": ["low", "peer_median_low"],                                                                             "func": rwx_ext_033_rel_low_return_252d},
    "rwx_ext_034_rel_high_return_252d":                   {"inputs": ["high", "peer_median_high"],                                                                           "func": rwx_ext_034_rel_high_return_252d},
    "rwx_ext_035_rel_low_to_peer_low_ratio":              {"inputs": ["low", "peer_median_low"],                                                                             "func": rwx_ext_035_rel_low_to_peer_low_ratio},
    "rwx_ext_036_rel_range_vs_peer_range":                {"inputs": ["high", "low", "peer_median_high", "peer_median_low"],                                                 "func": rwx_ext_036_rel_range_vs_peer_range},
    "rwx_ext_037_rel_range_vs_peer_range_21d":            {"inputs": ["high", "low", "peer_median_high", "peer_median_low"],                                                 "func": rwx_ext_037_rel_range_vs_peer_range_21d},
    "rwx_ext_038_low_vs_peer_close_ratio":                {"inputs": ["low", "peer_median_close"],                                                                           "func": rwx_ext_038_low_vs_peer_close_ratio},
    "rwx_ext_039_rel_high_pctrank_252d":                  {"inputs": ["high", "peer_median_high"],                                                                           "func": rwx_ext_039_rel_high_pctrank_252d},
    "rwx_ext_040_rel_low_pctrank_252d":                   {"inputs": ["low", "peer_median_low"],                                                                             "func": rwx_ext_040_rel_low_pctrank_252d},
    "rwx_ext_041_rel_volume_ratio_5d":                    {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_041_rel_volume_ratio_5d},
    "rwx_ext_042_rel_volume_ratio_252d":                  {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_042_rel_volume_ratio_252d},
    "rwx_ext_043_log_volume_ratio_zscore_252d":           {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_043_log_volume_ratio_zscore_252d},
    "rwx_ext_044_volume_underperf_intensity_21d":         {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                                         "func": rwx_ext_044_volume_underperf_intensity_21d},
    "rwx_ext_045_high_vol_underperf_days_63d":            {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                                         "func": rwx_ext_045_high_vol_underperf_days_63d},
    "rwx_ext_046_rel_volume_ratio_pctrank_252d":          {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_046_rel_volume_ratio_pctrank_252d},
    "rwx_ext_047_low_vol_underperf_frac_21d":             {"inputs": ["close", "peer_median_close", "volume", "peer_median_volume"],                                         "func": rwx_ext_047_low_vol_underperf_frac_21d},
    "rwx_ext_048_volume_zscore_vs_peer_21d":              {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_048_volume_zscore_vs_peer_21d},
    "rwx_ext_049_vol_ratio_ewm21":                        {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_049_vol_ratio_ewm21},
    "rwx_ext_050_vol_ratio_slope_21d":                    {"inputs": ["volume", "peer_median_volume"],                                                                       "func": rwx_ext_050_vol_ratio_slope_21d},
    "rwx_ext_051_composite_close_high_low_underperf_score": {"inputs": ["close", "peer_median_close", "high", "peer_median_high", "low", "peer_median_low"],                 "func": rwx_ext_051_composite_close_high_low_underperf_score},
    "rwx_ext_052_all_inputs_underperf_flag_21d":          {"inputs": ["close", "peer_median_close", "high", "peer_median_high", "low", "peer_median_low"],                   "func": rwx_ext_052_all_inputs_underperf_flag_21d},
    "rwx_ext_053_composite_rel_return_4window_zscore":    {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_053_composite_rel_return_4window_zscore},
    "rwx_ext_054_composite_underperf_flag_5window":       {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_054_composite_underperf_flag_5window},
    "rwx_ext_055_rel_return_5d_21d_63d_weighted_score":   {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_055_rel_return_5d_21d_63d_weighted_score},
    "rwx_ext_056_drawdown_underperf_composite":           {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_056_drawdown_underperf_composite},
    "rwx_ext_057_frac_underperf_21d_pctrank_252d":        {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_057_frac_underperf_21d_pctrank_252d},
    "rwx_ext_058_frac_underperf_63d_pctrank_252d":        {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_058_frac_underperf_63d_pctrank_252d},
    "rwx_ext_059_composite_pctrank_frac_and_return":      {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_059_composite_pctrank_frac_and_return},
    "rwx_ext_060_rel_return_1d_iqr_63d":                  {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_060_rel_return_1d_iqr_63d},
    "rwx_ext_061_rel_return_ewm5_minus_ewm63":            {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_061_rel_return_ewm5_minus_ewm63},
    "rwx_ext_062_rel_return_ewm21_minus_ewm126":          {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_062_rel_return_ewm21_minus_ewm126},
    "rwx_ext_063_log_price_ratio_ewm5":                   {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_063_log_price_ratio_ewm5},
    "rwx_ext_064_log_price_ratio_ewm252":                 {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_064_log_price_ratio_ewm252},
    "rwx_ext_065_rel_return_ewm5_slope_5d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_065_rel_return_ewm5_slope_5d},
    "rwx_ext_066_rel_return_1d_slope_5d":                 {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_066_rel_return_1d_slope_5d},
    "rwx_ext_067_rel_return_1d_slope_252d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_067_rel_return_1d_slope_252d},
    "rwx_ext_068_log_price_ratio_slope_5d":               {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_068_log_price_ratio_slope_5d},
    "rwx_ext_069_rel_drawdown_126d_zscore_252d":          {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_069_rel_drawdown_126d_zscore_252d},
    "rwx_ext_070_rel_close_rolling_min_126d":             {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_070_rel_close_rolling_min_126d},
    "rwx_ext_071_rel_return_1d_rolling_std_252d":         {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_071_rel_return_1d_rolling_std_252d},
    "rwx_ext_072_rel_return_1d_rolling_median_21d":       {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_072_rel_return_1d_rolling_median_21d},
    "rwx_ext_073_rel_return_1d_vs_rolling_median_63d":    {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_073_rel_return_1d_vs_rolling_median_63d},
    "rwx_ext_074_rel_close_distance_from_126d_floor":     {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_074_rel_close_distance_from_126d_floor},
    "rwx_ext_075_time_since_rel_price_new_low_126d":      {"inputs": ["close", "peer_median_close"],                                                                         "func": rwx_ext_075_time_since_rel_price_new_low_126d},
}
