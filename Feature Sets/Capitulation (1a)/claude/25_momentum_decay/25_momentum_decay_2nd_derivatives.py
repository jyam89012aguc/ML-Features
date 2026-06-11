"""
25_momentum_decay — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base momentum-decay features — velocity of decay across horizons
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    """Log return over n periods."""
    return np.log(s.clip(lower=_EPS)) - np.log(s.shift(n).clip(lower=_EPS))


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def mdc_drv2_001_ret_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d log return (velocity of short momentum)."""
    return _log_ret(close, _TD_WEEK).diff(_TD_WEEK)


def mdc_drv2_002_ret_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d log return (weekly change in monthly momentum)."""
    return _log_ret(close, _TD_MON).diff(_TD_WEEK)


def mdc_drv2_003_ret_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d log return (monthly change in monthly momentum)."""
    return _log_ret(close, _TD_MON).diff(_TD_MON)


def mdc_drv2_004_ret_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d log return (monthly velocity of quarterly momentum)."""
    return _log_ret(close, _TD_QTR).diff(_TD_MON)


def mdc_drv2_005_ret_126d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 126d log return (monthly velocity of half-year momentum)."""
    return _log_ret(close, _TD_HALF).diff(_TD_MON)


def mdc_drv2_006_ret_252d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 252d log return (monthly velocity of annual momentum)."""
    return _log_ret(close, _TD_YEAR).diff(_TD_MON)


def mdc_drv2_007_spread_5_21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d-minus-21d return spread (acceleration of short-end decay)."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)
    return spread.diff(_TD_WEEK)


def mdc_drv2_008_spread_21_63_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-minus-63d spread (weekly change in monthly decay signal)."""
    spread = _log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR)
    return spread.diff(_TD_WEEK)


def mdc_drv2_009_spread_63_252_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63d-minus-252d spread (monthly velocity of long decay)."""
    spread = _log_ret(close, _TD_QTR) - _log_ret(close, _TD_YEAR)
    return spread.diff(_TD_MON)


def mdc_drv2_010_halflife_proxy_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 126d/252d return ratio (velocity of momentum half-life decay)."""
    hl = _safe_div(_log_ret(close, _TD_HALF), _log_ret(close, _TD_YEAR).replace(0, np.nan))
    return hl.diff(_TD_WEEK)


def mdc_drv2_011_annualized_ret_5d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of annualized 5d return (monthly change in short run-rate)."""
    ann5 = _log_ret(close, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)
    return ann5.diff(_TD_MON)


def mdc_drv2_012_annualized_ret_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of annualized 21d return."""
    ann21 = _log_ret(close, _TD_MON) * (_TD_YEAR / _TD_MON)
    return ann21.diff(_TD_MON)


def mdc_drv2_013_decay_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of composite decay z-score (avg of 5d/21d/63d z-scores)."""
    def _z(r):
        m = _rolling_mean(r, _TD_YEAR)
        s = _rolling_std(r, _TD_YEAR)
        return _safe_div(r - m, s)
    composite = (_z(_log_ret(close, _TD_WEEK)) +
                 _z(_log_ret(close, _TD_MON)) +
                 _z(_log_ret(close, _TD_QTR))) / 3.0
    return composite.diff(_TD_WEEK)


def mdc_drv2_014_ret_5d_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d-return z-score (velocity of short-term return extremity)."""
    r = _log_ret(close, _TD_WEEK)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s)
    return z.diff(_TD_WEEK)


def mdc_drv2_015_ret_21d_zscore_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21d-return z-score."""
    r = _log_ret(close, _TD_MON)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s)
    return z.diff(_TD_MON)


def mdc_drv2_016_slope_ret_5d_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5d returns over 21d (velocity of slope)."""
    slp = _linslope(_log_ret(close, _TD_WEEK), _TD_MON)
    return slp.diff(_TD_WEEK)


def mdc_drv2_017_slope_ret_21d_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of OLS slope of 21d returns over 63d."""
    slp = _linslope(_log_ret(close, _TD_MON), _TD_QTR)
    return slp.diff(_TD_MON)


def mdc_drv2_018_vol_weighted_ret_5d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of volume-weighted 5d return."""
    r5 = _log_ret(close, _TD_WEEK)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vw_r5 = r5 * _safe_div(volume, avg_vol)
    return vw_r5.diff(_TD_WEEK)


def mdc_drv2_019_frac_neg_ret_5d_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of fraction of 5d-negative observations in 63d window."""
    r5 = _log_ret(close, _TD_WEEK)
    frac = (r5 < 0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return frac.diff(_TD_MON)


def mdc_drv2_020_ret_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21d log-return series over trailing 21 days (acceleration)."""
    return _linslope(_log_ret(close, _TD_MON), _TD_MON)


def mdc_drv2_021_spread_5_252_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5d-minus-252d extreme spread (velocity of full-term decay)."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_YEAR)
    return spread.diff(_TD_WEEK)


def mdc_drv2_022_neg_count_5horizons_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of count of negative horizons across 5 standard horizons."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    cnt = ((r5 < 0).astype(float) + (r21 < 0).astype(float) +
           (r63 < 0).astype(float) + (r126 < 0).astype(float) +
           (r252 < 0).astype(float))
    return cnt.diff(_TD_WEEK)


def mdc_drv2_023_recent_month_vs_prior_6m_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of recent-month-vs-prior-6m-average spread."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    prior_avg = (r21_1 + r21_2 + r21_3 + r21_4 + r21_5) / 5.0
    spread = r21_0 - prior_avg
    return spread.diff(_TD_MON)


def mdc_drv2_024_decay_regime_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-horizon z-score regime decay index."""
    def _z(r):
        m = _rolling_mean(r, _TD_YEAR)
        s = _rolling_std(r, _TD_YEAR)
        return _safe_div(r - m, s)
    score = (_z(_log_ret(close, _TD_WEEK)) + _z(_log_ret(close, _TD_MON)) +
             _z(_log_ret(close, _TD_QTR)) + _z(_log_ret(close, _TD_HALF)) +
             _z(_log_ret(close, _TD_YEAR))) / 5.0
    return score.diff(_TD_WEEK)


def mdc_drv2_025_ewm_ret_5d_span21_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of EWM-smoothed 5d return (trend in smoothed momentum)."""
    ewm_r5 = _ewm_mean(_log_ret(close, _TD_WEEK), _TD_MON)
    return _linslope(ewm_r5, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DECAY_REGISTRY_2ND_DERIVATIVES = {
    "mdc_drv2_001_ret_5d_5d_diff": {"inputs": ["close"], "func": mdc_drv2_001_ret_5d_5d_diff},
    "mdc_drv2_002_ret_21d_5d_diff": {"inputs": ["close"], "func": mdc_drv2_002_ret_21d_5d_diff},
    "mdc_drv2_003_ret_21d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_003_ret_21d_21d_diff},
    "mdc_drv2_004_ret_63d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_004_ret_63d_21d_diff},
    "mdc_drv2_005_ret_126d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_005_ret_126d_21d_diff},
    "mdc_drv2_006_ret_252d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_006_ret_252d_21d_diff},
    "mdc_drv2_007_spread_5_21_5d_diff": {"inputs": ["close"], "func": mdc_drv2_007_spread_5_21_5d_diff},
    "mdc_drv2_008_spread_21_63_5d_diff": {"inputs": ["close"], "func": mdc_drv2_008_spread_21_63_5d_diff},
    "mdc_drv2_009_spread_63_252_21d_diff": {"inputs": ["close"], "func": mdc_drv2_009_spread_63_252_21d_diff},
    "mdc_drv2_010_halflife_proxy_5d_diff": {"inputs": ["close"], "func": mdc_drv2_010_halflife_proxy_5d_diff},
    "mdc_drv2_011_annualized_ret_5d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_011_annualized_ret_5d_21d_diff},
    "mdc_drv2_012_annualized_ret_21d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_012_annualized_ret_21d_21d_diff},
    "mdc_drv2_013_decay_composite_5d_diff": {"inputs": ["close"], "func": mdc_drv2_013_decay_composite_5d_diff},
    "mdc_drv2_014_ret_5d_zscore_5d_diff": {"inputs": ["close"], "func": mdc_drv2_014_ret_5d_zscore_5d_diff},
    "mdc_drv2_015_ret_21d_zscore_21d_diff": {"inputs": ["close"], "func": mdc_drv2_015_ret_21d_zscore_21d_diff},
    "mdc_drv2_016_slope_ret_5d_21d_5d_diff": {"inputs": ["close"], "func": mdc_drv2_016_slope_ret_5d_21d_5d_diff},
    "mdc_drv2_017_slope_ret_21d_63d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_017_slope_ret_21d_63d_21d_diff},
    "mdc_drv2_018_vol_weighted_ret_5d_5d_diff": {"inputs": ["close", "volume"], "func": mdc_drv2_018_vol_weighted_ret_5d_5d_diff},
    "mdc_drv2_019_frac_neg_ret_5d_63d_21d_diff": {"inputs": ["close"], "func": mdc_drv2_019_frac_neg_ret_5d_63d_21d_diff},
    "mdc_drv2_020_ret_21d_slope_21d": {"inputs": ["close"], "func": mdc_drv2_020_ret_21d_slope_21d},
    "mdc_drv2_021_spread_5_252_5d_diff": {"inputs": ["close"], "func": mdc_drv2_021_spread_5_252_5d_diff},
    "mdc_drv2_022_neg_count_5horizons_5d_diff": {"inputs": ["close"], "func": mdc_drv2_022_neg_count_5horizons_5d_diff},
    "mdc_drv2_023_recent_month_vs_prior_6m_21d_diff": {"inputs": ["close"], "func": mdc_drv2_023_recent_month_vs_prior_6m_21d_diff},
    "mdc_drv2_024_decay_regime_score_5d_diff": {"inputs": ["close"], "func": mdc_drv2_024_decay_regime_score_5d_diff},
    "mdc_drv2_025_ewm_ret_5d_span21_slope_21d": {"inputs": ["close"], "func": mdc_drv2_025_ewm_ret_5d_span21_slope_21d},
}
