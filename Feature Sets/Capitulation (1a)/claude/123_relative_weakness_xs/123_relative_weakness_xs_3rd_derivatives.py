"""
123_relative_weakness_xs — 3rd Derivatives (Features rwx_drv3_001-025)
Domain: rate of change of 2nd-derivative relative-weakness features —
        acceleration of relative underperformance velocity
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

    3rd-derivative features are diff/slope applied to a 2nd-derivative
    concept (i.e., second diff or diff-of-slope of a base feature).
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff or slope applied to a 2nd-derivative concept

def rwx_drv3_001_rel_return_1d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of daily relative return (acceleration of daily relative return velocity)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_002_rel_return_1d_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d velocity of daily relative return (jerk in monthly rel-return change)."""
    rel   = _log_return(close, 1) - _log_return(peer_median_close, 1)
    vel21 = rel.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_003_rel_return_21d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d relative return (acceleration of monthly underperformance velocity)."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    vel = rel.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_004_frac_underperf_21d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d underperformance fraction (acceleration of regime shift)."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21 = _rolling_mean(flag, _TD_MON)
    vel    = frac21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_005_consec_underperf_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of consecutive-underperformance streak (acceleration of streak change)."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag)
    vel    = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_006_rel_drawdown_63d_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d change in 63d relative drawdown."""
    rel_dd = _drawdown_from_peak(close, _TD_QTR) - _drawdown_from_peak(peer_median_close, _TD_QTR)
    vel21  = rel_dd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_007_log_price_ratio_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of log(ticker/peer) (acceleration of relative price level change)."""
    lr  = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    vel = lr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_008_log_price_ratio_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d velocity of log(ticker/peer)."""
    lr    = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    vel21 = lr.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_009_rel_return_ewm21_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(21) daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    ewm = _ewm_mean(rel, _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_010_rel_return_ewm63_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d velocity of EWM(63) daily relative return."""
    rel   = _log_return(close, 1) - _log_return(peer_median_close, 1)
    ewm   = _ewm_mean(rel, _TD_QTR)
    vel21 = ewm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_011_composite_rel_return_score_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite relative return score (acceleration of composite weakness)."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    comp = (r5 + r21 + r63) / 3.0
    vel  = comp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_012_rel_return_zscore_252d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d z-score of daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    z   = _zscore_rolling(rel, _TD_YEAR)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_013_underperf_depth_21d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d cumulative underperformance depth."""
    rel   = _log_return(close, 1) - _log_return(peer_median_close, 1)
    depth = _rolling_sum(rel.clip(upper=0.0), _TD_MON)
    vel   = depth.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_014_rel_return_1d_slope_21d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d OLS slope of daily relative return (jerk of slope)."""
    rel   = _log_return(close, 1) - _log_return(peer_median_close, 1)
    slope = _linslope(rel, _TD_MON)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_015_frac_underperf_63d_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of 21d change in 63d underperformance fraction."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac63 = _rolling_mean(flag, _TD_QTR)
    vel21  = frac63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_016_rel_return_21d_5d_diff_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d velocity of 21d relative return."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    vel = rel.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rwx_drv3_017_log_price_ratio_5d_diff_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d velocity of log(ticker/peer)."""
    lr  = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    vel = lr.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rwx_drv3_018_rel_return_ewm21_5d_diff_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d velocity of EWM(21) relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    ewm = _ewm_mean(rel, _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rwx_drv3_019_rel_drawdown_252d_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d change in 252d relative drawdown (jerk in drawdown deepening)."""
    rel_dd = _drawdown_from_peak(close, _TD_YEAR) - _drawdown_from_peak(peer_median_close, _TD_YEAR)
    vel21  = rel_dd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_020_rel_return_rolling_mean_21d_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d rolling mean of daily relative return."""
    rel    = _log_return(close, 1) - _log_return(peer_median_close, 1)
    mean21 = _rolling_mean(rel, _TD_MON)
    vel    = mean21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_021_consec_underperf_5d_diff_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d velocity of consecutive-underperformance streak."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag).astype(float)
    vel    = streak.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rwx_drv3_022_log_price_ratio_slope_21d_5d_diff_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d velocity of 21d slope of log(ticker/peer)."""
    lr     = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    slope  = _linslope(lr, _TD_MON)
    vel    = slope.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def rwx_drv3_023_rel_return_63d_21d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d change in 63d relative return (jerk in quarterly underperformance)."""
    rel   = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    vel21 = rel.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rwx_drv3_024_composite_zscore_3window_5d_diff_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite 252d z-score across 5d/21d/63d relative returns."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    z   = (_zscore_rolling(r5, _TD_YEAR) + _zscore_rolling(r21, _TD_YEAR) + _zscore_rolling(r63, _TD_YEAR)) / 3.0
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rwx_drv3_025_rel_vol_adj_return_21d_5d_diff_slope_21d(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d velocity of risk-adjusted 21d relative return."""
    rel  = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    te63 = _rolling_std(_log_return(close, 1) - _log_return(peer_median_close, 1), _TD_QTR)
    adj  = _safe_div(rel, te63.clip(lower=_EPS))
    vel  = adj.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_WEAKNESS_XS_REGISTRY_3RD_DERIVATIVES = {
    "rwx_drv3_001_rel_return_1d_5d_diff_5d_diff":                   {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_001_rel_return_1d_5d_diff_5d_diff},
    "rwx_drv3_002_rel_return_1d_21d_diff_5d_diff":                  {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_002_rel_return_1d_21d_diff_5d_diff},
    "rwx_drv3_003_rel_return_21d_5d_diff_5d_diff":                  {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_003_rel_return_21d_5d_diff_5d_diff},
    "rwx_drv3_004_frac_underperf_21d_5d_diff_5d_diff":              {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_004_frac_underperf_21d_5d_diff_5d_diff},
    "rwx_drv3_005_consec_underperf_5d_diff_5d_diff":                {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_005_consec_underperf_5d_diff_5d_diff},
    "rwx_drv3_006_rel_drawdown_63d_21d_diff_5d_diff":               {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_006_rel_drawdown_63d_21d_diff_5d_diff},
    "rwx_drv3_007_log_price_ratio_5d_diff_5d_diff":                 {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_007_log_price_ratio_5d_diff_5d_diff},
    "rwx_drv3_008_log_price_ratio_21d_diff_5d_diff":                {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_008_log_price_ratio_21d_diff_5d_diff},
    "rwx_drv3_009_rel_return_ewm21_5d_diff_5d_diff":                {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_009_rel_return_ewm21_5d_diff_5d_diff},
    "rwx_drv3_010_rel_return_ewm63_21d_diff_5d_diff":               {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_010_rel_return_ewm63_21d_diff_5d_diff},
    "rwx_drv3_011_composite_rel_return_score_5d_diff_5d_diff":      {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_011_composite_rel_return_score_5d_diff_5d_diff},
    "rwx_drv3_012_rel_return_zscore_252d_5d_diff_5d_diff":          {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_012_rel_return_zscore_252d_5d_diff_5d_diff},
    "rwx_drv3_013_underperf_depth_21d_5d_diff_5d_diff":             {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_013_underperf_depth_21d_5d_diff_5d_diff},
    "rwx_drv3_014_rel_return_1d_slope_21d_5d_diff_5d_diff":         {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_014_rel_return_1d_slope_21d_5d_diff_5d_diff},
    "rwx_drv3_015_frac_underperf_63d_21d_diff_5d_diff":             {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_015_frac_underperf_63d_21d_diff_5d_diff},
    "rwx_drv3_016_rel_return_21d_5d_diff_slope_21d":                {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_016_rel_return_21d_5d_diff_slope_21d},
    "rwx_drv3_017_log_price_ratio_5d_diff_slope_21d":               {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_017_log_price_ratio_5d_diff_slope_21d},
    "rwx_drv3_018_rel_return_ewm21_5d_diff_slope_21d":              {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_018_rel_return_ewm21_5d_diff_slope_21d},
    "rwx_drv3_019_rel_drawdown_252d_21d_diff_5d_diff":              {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_019_rel_drawdown_252d_21d_diff_5d_diff},
    "rwx_drv3_020_rel_return_rolling_mean_21d_5d_diff_5d_diff":     {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_020_rel_return_rolling_mean_21d_5d_diff_5d_diff},
    "rwx_drv3_021_consec_underperf_5d_diff_slope_21d":              {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_021_consec_underperf_5d_diff_slope_21d},
    "rwx_drv3_022_log_price_ratio_slope_21d_5d_diff_slope_21d":     {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_022_log_price_ratio_slope_21d_5d_diff_slope_21d},
    "rwx_drv3_023_rel_return_63d_21d_diff_5d_diff":                 {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_023_rel_return_63d_21d_diff_5d_diff},
    "rwx_drv3_024_composite_zscore_3window_5d_diff_5d_diff":        {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_024_composite_zscore_3window_5d_diff_5d_diff},
    "rwx_drv3_025_rel_vol_adj_return_21d_5d_diff_slope_21d":        {"inputs": ["close", "peer_median_close"], "func": rwx_drv3_025_rel_vol_adj_return_21d_5d_diff_slope_21d},
}
