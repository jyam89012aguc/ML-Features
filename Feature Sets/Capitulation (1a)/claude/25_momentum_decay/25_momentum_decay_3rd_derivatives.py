"""
25_momentum_decay — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative momentum-decay features — acceleration of decay velocity
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def mdc_drv3_001_ret_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d return (acceleration of short-momentum velocity)."""
    vel = _log_ret(close, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_002_ret_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d return (jerk in monthly momentum)."""
    vel = _log_ret(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_003_ret_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21d return (jerk at monthly scale)."""
    vel = _log_ret(close, _TD_MON).diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_004_ret_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63d return (jerk in quarterly momentum)."""
    vel = _log_ret(close, _TD_QTR).diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_005_spread_5_21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d-minus-21d spread (acceleration of short-end decay)."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_006_spread_21_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d-minus-63d spread."""
    spread = _log_ret(close, _TD_MON) - _log_ret(close, _TD_QTR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_007_spread_63_252_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of 63d-minus-252d spread."""
    spread = _log_ret(close, _TD_QTR) - _log_ret(close, _TD_YEAR)
    vel = spread.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_008_halflife_proxy_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126d/252d half-life proxy (jerk in momentum half-life)."""
    hl = _safe_div(_log_ret(close, _TD_HALF), _log_ret(close, _TD_YEAR).replace(0, np.nan))
    vel = hl.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_009_decay_composite_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of composite decay z-score (acceleration of decay regime)."""
    def _z(r):
        m = _rolling_mean(r, _TD_YEAR)
        s = _rolling_std(r, _TD_YEAR)
        return _safe_div(r - m, s)
    composite = (_z(_log_ret(close, _TD_WEEK)) +
                 _z(_log_ret(close, _TD_MON)) +
                 _z(_log_ret(close, _TD_QTR))) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_010_ret_5d_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d z-score (jerk in short-return extremity)."""
    r = _log_ret(close, _TD_WEEK)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_011_slope_ret_5d_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of OLS slope of 5d returns over 21d (accel of slope trend)."""
    slp = _linslope(_log_ret(close, _TD_WEEK), _TD_MON)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_012_slope_ret_21d_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 21d-over-63d slope."""
    slp = _linslope(_log_ret(close, _TD_MON), _TD_QTR)
    vel = slp.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_013_annualized_ret_5d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of annualized 5d return (jerk in run-rate)."""
    ann5 = _log_ret(close, _TD_WEEK) * (_TD_YEAR / _TD_WEEK)
    vel = ann5.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_014_spread_5_252_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d-minus-252d extreme spread (jerk in full-term decay)."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_YEAR)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_015_neg_count_5horizons_5d_diff_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5d-diff of negative-horizon count."""
    r5 = _log_ret(close, _TD_WEEK)
    r21 = _log_ret(close, _TD_MON)
    r63 = _log_ret(close, _TD_QTR)
    r126 = _log_ret(close, _TD_HALF)
    r252 = _log_ret(close, _TD_YEAR)
    cnt = ((r5 < 0).astype(float) + (r21 < 0).astype(float) +
           (r63 < 0).astype(float) + (r126 < 0).astype(float) +
           (r252 < 0).astype(float))
    vel = cnt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mdc_drv3_016_decay_regime_score_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-horizon z-score regime decay index (jerk in regime)."""
    def _z(r):
        m = _rolling_mean(r, _TD_YEAR)
        s = _rolling_std(r, _TD_YEAR)
        return _safe_div(r - m, s)
    score = (_z(_log_ret(close, _TD_WEEK)) + _z(_log_ret(close, _TD_MON)) +
             _z(_log_ret(close, _TD_QTR)) + _z(_log_ret(close, _TD_HALF)) +
             _z(_log_ret(close, _TD_YEAR))) / 5.0
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_017_frac_neg_5d_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of fraction-neg-5d-in-63d."""
    r5 = _log_ret(close, _TD_WEEK)
    frac = (r5 < 0).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    vel = frac.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_018_vol_weighted_ret_5d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of volume-weighted 5d return."""
    r5 = _log_ret(close, _TD_WEEK)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vw_r5 = r5 * _safe_div(volume, avg_vol)
    vel = vw_r5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def mdc_drv3_019_recent_month_vs_prior_6m_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-velocity of recent-month vs prior-6m spread."""
    r21_0 = _log_ret(close, _TD_MON)
    r21_1 = _log_ret(close.shift(_TD_MON), _TD_MON)
    r21_2 = _log_ret(close.shift(2 * _TD_MON), _TD_MON)
    r21_3 = _log_ret(close.shift(3 * _TD_MON), _TD_MON)
    r21_4 = _log_ret(close.shift(4 * _TD_MON), _TD_MON)
    r21_5 = _log_ret(close.shift(5 * _TD_MON), _TD_MON)
    prior_avg = (r21_1 + r21_2 + r21_3 + r21_4 + r21_5) / 5.0
    spread = r21_0 - prior_avg
    vel = spread.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def mdc_drv3_020_ret_21d_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d returns over 21d window."""
    slp = _linslope(_log_ret(close, _TD_MON), _TD_MON)
    return slp.diff(_TD_WEEK)


def mdc_drv3_021_ewm_ret_5d_span21_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of EWM-smoothed 5d returns over 21d."""
    ewm_r5 = _ewm_mean(_log_ret(close, _TD_WEEK), _TD_MON)
    slp = _linslope(ewm_r5, _TD_MON)
    return slp.diff(_TD_WEEK)


def mdc_drv3_022_ret_5d_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5d-velocity of 5d return (trend in acceleration)."""
    vel = _log_ret(close, _TD_WEEK).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mdc_drv3_023_spread_5_21_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5d-velocity of 5d-minus-21d spread."""
    spread = _log_ret(close, _TD_WEEK) - _log_ret(close, _TD_MON)
    vel = spread.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mdc_drv3_024_decay_composite_5d_diff_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of 5d-velocity of composite decay z-score."""
    def _z(r):
        m = _rolling_mean(r, _TD_YEAR)
        s = _rolling_std(r, _TD_YEAR)
        return _safe_div(r - m, s)
    composite = (_z(_log_ret(close, _TD_WEEK)) +
                 _z(_log_ret(close, _TD_MON)) +
                 _z(_log_ret(close, _TD_QTR))) / 3.0
    vel = composite.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def mdc_drv3_025_ret_63d_21d_diff_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d-velocity of 63d return (3rd-order quarterly jerk)."""
    vel21 = _log_ret(close, _TD_QTR).diff(_TD_MON)
    vel5 = vel21.diff(_TD_WEEK)
    return vel5.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DECAY_REGISTRY_3RD_DERIVATIVES = {
    "mdc_drv3_001_ret_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_001_ret_5d_5d_diff_5d_diff},
    "mdc_drv3_002_ret_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_002_ret_21d_5d_diff_5d_diff},
    "mdc_drv3_003_ret_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_003_ret_21d_21d_diff_5d_diff},
    "mdc_drv3_004_ret_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_004_ret_63d_21d_diff_5d_diff},
    "mdc_drv3_005_spread_5_21_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_005_spread_5_21_5d_diff_5d_diff},
    "mdc_drv3_006_spread_21_63_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_006_spread_21_63_5d_diff_5d_diff},
    "mdc_drv3_007_spread_63_252_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_007_spread_63_252_21d_diff_5d_diff},
    "mdc_drv3_008_halflife_proxy_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_008_halflife_proxy_5d_diff_5d_diff},
    "mdc_drv3_009_decay_composite_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_009_decay_composite_5d_diff_5d_diff},
    "mdc_drv3_010_ret_5d_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_010_ret_5d_zscore_5d_diff_5d_diff},
    "mdc_drv3_011_slope_ret_5d_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_011_slope_ret_5d_21d_5d_diff_5d_diff},
    "mdc_drv3_012_slope_ret_21d_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_012_slope_ret_21d_63d_21d_diff_5d_diff},
    "mdc_drv3_013_annualized_ret_5d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_013_annualized_ret_5d_21d_diff_5d_diff},
    "mdc_drv3_014_spread_5_252_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_014_spread_5_252_5d_diff_5d_diff},
    "mdc_drv3_015_neg_count_5horizons_5d_diff_slope": {"inputs": ["close"], "func": mdc_drv3_015_neg_count_5horizons_5d_diff_slope},
    "mdc_drv3_016_decay_regime_score_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_016_decay_regime_score_5d_diff_5d_diff},
    "mdc_drv3_017_frac_neg_5d_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_017_frac_neg_5d_63d_21d_diff_5d_diff},
    "mdc_drv3_018_vol_weighted_ret_5d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": mdc_drv3_018_vol_weighted_ret_5d_5d_diff_5d_diff},
    "mdc_drv3_019_recent_month_vs_prior_6m_21d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_019_recent_month_vs_prior_6m_21d_diff_5d_diff},
    "mdc_drv3_020_ret_21d_slope_21d_5d_diff": {"inputs": ["close"], "func": mdc_drv3_020_ret_21d_slope_21d_5d_diff},
    "mdc_drv3_021_ewm_ret_5d_span21_slope_5d_diff": {"inputs": ["close"], "func": mdc_drv3_021_ewm_ret_5d_span21_slope_5d_diff},
    "mdc_drv3_022_ret_5d_5d_diff_slope_21d": {"inputs": ["close"], "func": mdc_drv3_022_ret_5d_5d_diff_slope_21d},
    "mdc_drv3_023_spread_5_21_5d_diff_slope_21d": {"inputs": ["close"], "func": mdc_drv3_023_spread_5_21_5d_diff_slope_21d},
    "mdc_drv3_024_decay_composite_5d_diff_slope_21d": {"inputs": ["close"], "func": mdc_drv3_024_decay_composite_5d_diff_slope_21d},
    "mdc_drv3_025_ret_63d_21d_diff_5d_diff_5d_diff": {"inputs": ["close"], "func": mdc_drv3_025_ret_63d_21d_diff_5d_diff_5d_diff},
}
