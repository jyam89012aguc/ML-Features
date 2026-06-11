"""
123_relative_weakness_xs — 2nd Derivatives (Features rwx_drv2_001-025)
Domain: rate of change of base relative-weakness cross-sectional features —
        velocity of relative underperformance behavior
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

    2nd-derivative features are rate-of-change (diff/slope) applied to a
    base feature from the _base_001_075 and _base_076_150 files.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def rwx_drv2_001_rel_return_1d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of daily relative return (velocity of daily relative return)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.diff(_TD_WEEK)


def rwx_drv2_002_rel_return_1d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of daily relative return (monthly velocity)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return rel.diff(_TD_MON)


def rwx_drv2_003_rel_return_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of 21d relative return (how fast monthly underperformance is changing)."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    return rel.diff(_TD_WEEK)


def rwx_drv2_004_rel_return_63d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 63d relative return (monthly change in quarterly underperformance)."""
    rel = _log_return(close, _TD_QTR) - _log_return(peer_median_close, _TD_QTR)
    return rel.diff(_TD_MON)


def rwx_drv2_005_frac_underperf_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of 21d underperformance fraction (how fast regime is shifting)."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac21 = _rolling_mean(flag, _TD_MON)
    return frac21.diff(_TD_WEEK)


def rwx_drv2_006_frac_underperf_63d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 63d underperformance fraction."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1)).astype(float)
    frac63 = _rolling_mean(flag, _TD_QTR)
    return frac63.diff(_TD_MON)


def rwx_drv2_007_consec_underperf_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-underperformance streak (velocity of streak change)."""
    flag   = (_log_return(close, 1) < _log_return(peer_median_close, 1))
    streak = _consec_streak(flag)
    return streak.diff(_TD_WEEK)


def rwx_drv2_008_rel_drawdown_63d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 63d relative drawdown (how fast relative drawdown deepens)."""
    rel_dd = _drawdown_from_peak(close, _TD_QTR) - _drawdown_from_peak(peer_median_close, _TD_QTR)
    return rel_dd.diff(_TD_MON)


def rwx_drv2_009_rel_drawdown_252d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 252d relative drawdown."""
    rel_dd = _drawdown_from_peak(close, _TD_YEAR) - _drawdown_from_peak(peer_median_close, _TD_YEAR)
    return rel_dd.diff(_TD_MON)


def rwx_drv2_010_log_price_ratio_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of log(ticker/peer) (velocity of relative price level change)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr.diff(_TD_WEEK)


def rwx_drv2_011_log_price_ratio_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of log(ticker/peer) (monthly velocity of relative price)."""
    lr = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    return lr.diff(_TD_MON)


def rwx_drv2_012_rel_return_1d_zscore_252d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of daily relative return (velocity of extremity)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    z   = _zscore_rolling(rel, _TD_YEAR)
    return z.diff(_TD_WEEK)


def rwx_drv2_013_rel_return_rolling_mean_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of 21d rolling mean of daily relative return."""
    rel    = _log_return(close, 1) - _log_return(peer_median_close, 1)
    mean21 = _rolling_mean(rel, _TD_MON)
    return mean21.diff(_TD_WEEK)


def rwx_drv2_014_rel_return_rolling_mean_63d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 63d rolling mean of daily relative return."""
    rel    = _log_return(close, 1) - _log_return(peer_median_close, 1)
    mean63 = _rolling_mean(rel, _TD_QTR)
    return mean63.diff(_TD_MON)


def rwx_drv2_015_underperf_depth_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of 21d cumulative underperformance depth."""
    rel    = _log_return(close, 1) - _log_return(peer_median_close, 1)
    depth  = _rolling_sum(rel.clip(upper=0.0), _TD_MON)
    return depth.diff(_TD_WEEK)


def rwx_drv2_016_underperf_depth_63d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 63d cumulative underperformance depth."""
    rel   = _log_return(close, 1) - _log_return(peer_median_close, 1)
    depth = _rolling_sum(rel.clip(upper=0.0), _TD_QTR)
    return depth.diff(_TD_MON)


def rwx_drv2_017_composite_rel_return_score_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of composite relative return score (mean of 5d/21d/63d rel returns)."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    comp = (r5 + r21 + r63) / 3.0
    return comp.diff(_TD_WEEK)


def rwx_drv2_018_rel_return_ewm21_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) daily relative return (velocity of smoothed trend)."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_MON).diff(_TD_WEEK)


def rwx_drv2_019_rel_return_ewm63_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of EWM(63) daily relative return."""
    rel = _log_return(close, 1) - _log_return(peer_median_close, 1)
    return _ewm_mean(rel, _TD_QTR).diff(_TD_MON)


def rwx_drv2_020_rel_return_1d_slope_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d OLS slope of daily relative return (acceleration of trend slope)."""
    rel    = _log_return(close, 1) - _log_return(peer_median_close, 1)
    slope  = _linslope(rel, _TD_MON)
    return slope.diff(_TD_WEEK)


def rwx_drv2_021_rel_return_21d_rolling_min_252d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of 252d rolling min of 21d relative return (how fast floor is moving)."""
    rel = _log_return(close, _TD_MON) - _log_return(peer_median_close, _TD_MON)
    mn  = _rolling_min(rel, _TD_YEAR)
    return mn.diff(_TD_MON)


def rwx_drv2_022_rel_vol_adj_return_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of risk-adjusted 21d relative return (21d rel ret / 63d tracking error)."""
    rel  = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    te63 = _rolling_std(_log_return(close, 1) - _log_return(peer_median_close, 1), _TD_QTR)
    adj  = _safe_div(rel, te63.clip(lower=_EPS))
    return adj.diff(_TD_WEEK)


def rwx_drv2_023_log_price_ratio_slope_21d_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of the 21d slope of log(ticker/peer) (acceleration of relative price trend)."""
    lr    = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    slope = _linslope(lr, _TD_MON)
    return slope.diff(_TD_WEEK)


def rwx_drv2_024_rel_close_drawdown_252d_21d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """21-day diff of drawdown of log(ticker/peer) from its 252d peak."""
    lr   = np.log(_safe_div(close, peer_median_close).abs().clip(lower=_EPS))
    peak = _rolling_max(lr, _TD_YEAR)
    dd   = _safe_div(lr - peak, peak.abs().clip(lower=_EPS))
    return dd.diff(_TD_MON)


def rwx_drv2_025_composite_zscore_3window_5d_diff(close: pd.Series, peer_median_close: pd.Series) -> pd.Series:
    """5-day diff of composite 252d z-score across 5d/21d/63d relative returns."""
    r5  = _log_return(close, _TD_WEEK) - _log_return(peer_median_close, _TD_WEEK)
    r21 = _log_return(close, _TD_MON)  - _log_return(peer_median_close, _TD_MON)
    r63 = _log_return(close, _TD_QTR)  - _log_return(peer_median_close, _TD_QTR)
    z   = (_zscore_rolling(r5, _TD_YEAR) + _zscore_rolling(r21, _TD_YEAR) + _zscore_rolling(r63, _TD_YEAR)) / 3.0
    return z.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_WEAKNESS_XS_REGISTRY_2ND_DERIVATIVES = {
    "rwx_drv2_001_rel_return_1d_5d_diff":                  {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_001_rel_return_1d_5d_diff},
    "rwx_drv2_002_rel_return_1d_21d_diff":                 {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_002_rel_return_1d_21d_diff},
    "rwx_drv2_003_rel_return_21d_5d_diff":                 {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_003_rel_return_21d_5d_diff},
    "rwx_drv2_004_rel_return_63d_21d_diff":                {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_004_rel_return_63d_21d_diff},
    "rwx_drv2_005_frac_underperf_21d_5d_diff":             {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_005_frac_underperf_21d_5d_diff},
    "rwx_drv2_006_frac_underperf_63d_21d_diff":            {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_006_frac_underperf_63d_21d_diff},
    "rwx_drv2_007_consec_underperf_5d_diff":               {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_007_consec_underperf_5d_diff},
    "rwx_drv2_008_rel_drawdown_63d_21d_diff":              {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_008_rel_drawdown_63d_21d_diff},
    "rwx_drv2_009_rel_drawdown_252d_21d_diff":             {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_009_rel_drawdown_252d_21d_diff},
    "rwx_drv2_010_log_price_ratio_5d_diff":                {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_010_log_price_ratio_5d_diff},
    "rwx_drv2_011_log_price_ratio_21d_diff":               {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_011_log_price_ratio_21d_diff},
    "rwx_drv2_012_rel_return_1d_zscore_252d_5d_diff":      {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_012_rel_return_1d_zscore_252d_5d_diff},
    "rwx_drv2_013_rel_return_rolling_mean_21d_5d_diff":    {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_013_rel_return_rolling_mean_21d_5d_diff},
    "rwx_drv2_014_rel_return_rolling_mean_63d_21d_diff":   {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_014_rel_return_rolling_mean_63d_21d_diff},
    "rwx_drv2_015_underperf_depth_21d_5d_diff":            {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_015_underperf_depth_21d_5d_diff},
    "rwx_drv2_016_underperf_depth_63d_21d_diff":           {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_016_underperf_depth_63d_21d_diff},
    "rwx_drv2_017_composite_rel_return_score_5d_diff":     {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_017_composite_rel_return_score_5d_diff},
    "rwx_drv2_018_rel_return_ewm21_5d_diff":               {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_018_rel_return_ewm21_5d_diff},
    "rwx_drv2_019_rel_return_ewm63_21d_diff":              {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_019_rel_return_ewm63_21d_diff},
    "rwx_drv2_020_rel_return_1d_slope_21d_5d_diff":        {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_020_rel_return_1d_slope_21d_5d_diff},
    "rwx_drv2_021_rel_return_21d_rolling_min_252d_21d_diff": {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_021_rel_return_21d_rolling_min_252d_21d_diff},
    "rwx_drv2_022_rel_vol_adj_return_21d_5d_diff":         {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_022_rel_vol_adj_return_21d_5d_diff},
    "rwx_drv2_023_log_price_ratio_slope_21d_5d_diff":      {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_023_log_price_ratio_slope_21d_5d_diff},
    "rwx_drv2_024_rel_close_drawdown_252d_21d_diff":       {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_024_rel_close_drawdown_252d_21d_diff},
    "rwx_drv2_025_composite_zscore_3window_5d_diff":       {"inputs": ["close", "peer_median_close"], "func": rwx_drv2_025_composite_zscore_3window_5d_diff},
}
