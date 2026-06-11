"""
35_capitulation_thrust — 2nd Derivatives (Features drv2_001-025)
Domain: rate-of-change of base capitulation-thrust concepts — velocity of thrust measures
        Diffs and OLS slopes applied to base thrust features to capture how thrust is evolving.
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
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def cth_drv2_001_min_return_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the worst-5d-return within trailing 21d (velocity of thrust depth)."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    worst = _rolling_min(cum5, _TD_MON)
    return worst.diff(_TD_WEEK)


def cth_drv2_002_min_return_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the worst-21d-return in trailing 63d window."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    worst = _rolling_min(cum21, _TD_QTR)
    return worst.diff(_TD_MON)


def cth_drv2_003_single_day_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of current 1-day return z-score (velocity of daily sigma move)."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    return z.diff(_TD_WEEK)


def cth_drv2_004_drawdown_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day drawdown from peak (rate of drawdown deepening)."""
    pk  = _rolling_max(close, _TD_MON)
    dd  = _log_safe(close) - _log_safe(pk)
    return dd.diff(_TD_WEEK)


def cth_drv2_005_drawdown_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day drawdown from peak."""
    pk  = _rolling_max(close, _TD_QTR)
    dd  = _log_safe(close) - _log_safe(pk)
    return dd.diff(_TD_MON)


def cth_drv2_006_thrust_intensity_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day thrust intensity (avg daily log-loss per day in leg)."""
    cum5      = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    intensity = cum5.clip(upper=0) / _TD_WEEK
    return intensity.diff(_TD_WEEK)


def cth_drv2_007_thrust_intensity_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day thrust intensity."""
    cum21     = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    intensity = cum21.clip(upper=0) / _TD_MON
    return intensity.diff(_TD_MON)


def cth_drv2_008_waterfall_freq_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 63-day waterfall frequency (acceleration of cascade events)."""
    l1 = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))) < 0
    l2 = (_log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(2 * _TD_WEEK))) < 0
    l3 = (_log_safe(close.shift(2 * _TD_WEEK)) - _log_safe(close.shift(3 * _TD_WEEK))) < 0
    freq = (l1 & l2 & l3).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return freq.diff(_TD_MON)


def cth_drv2_009_log_slope_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day OLS log-slope (velocity of descent steepness)."""
    slp = _linslope(_log_safe(close), _TD_WEEK)
    return slp.diff(_TD_WEEK)


def cth_drv2_010_log_slope_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day OLS log-slope."""
    slp = _linslope(_log_safe(close), _TD_MON)
    return slp.diff(_TD_MON)


def cth_drv2_011_sigma_burst_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day sigma-burst count (how rapidly shocks are clustering)."""
    lr   = _log_ret(close)
    mn   = _rolling_mean(lr, _TD_YEAR)
    sd   = _rolling_std(lr, _TD_YEAR)
    z    = _safe_div(lr - mn, sd)
    cnt  = (z < -1.5).astype(float).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).sum()
    return cnt.diff(_TD_WEEK)


def cth_drv2_012_sigma_burst_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day 2-sigma burst count."""
    lr  = _log_ret(close)
    mn  = _rolling_mean(lr, _TD_YEAR)
    sd  = _rolling_std(lr, _TD_YEAR)
    z   = _safe_div(lr - mn, sd)
    cnt = (z < -2.0).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return cnt.diff(_TD_MON)


def cth_drv2_013_panic_composite_5d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the dual-horizon panic composite (5d+21d z-score average)."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    z5    = _safe_div(cum5  - _rolling_mean(cum5,  _TD_YEAR), _rolling_std(cum5,  _TD_YEAR))
    z21   = _safe_div(cum21 - _rolling_mean(cum21, _TD_YEAR), _rolling_std(cum21, _TD_YEAR))
    comp  = (z5 + z21) / 2.0
    return comp.diff(_TD_MON)


def cth_drv2_014_vol_thrust_score_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day volume-weighted thrust score."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    score   = (lr * vol_n).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).sum()
    return score.diff(_TD_WEEK)


def cth_drv2_015_vol_down_up_ratio_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day down/up volume ratio."""
    lr     = _log_ret(close)
    down_v = volume.where(lr < 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    up_v   = volume.where(lr > 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    ratio  = _safe_div(down_v, up_v)
    return ratio.diff(_TD_WEEK)


def cth_drv2_016_thrust_persist_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day thrust persistence score (fraction of down days)."""
    lr    = _log_ret(close)
    pers  = (lr < 0).astype(float).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean()
    return pers.diff(_TD_WEEK)


def cth_drv2_017_return_skew_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day return skewness (velocity of left-tail development)."""
    lr   = _log_ret(close)
    skew = lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).skew()
    return skew.diff(_TD_WEEK)


def cth_drv2_018_close_near_low_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day count of close-near-low sessions."""
    pos  = _safe_div(close - low, high - low + _EPS)
    cnt  = (pos < 0.20).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return cnt.diff(_TD_WEEK)


def cth_drv2_019_drawdown_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day drawdown series (trend in drawdown speed)."""
    pk  = _rolling_max(close, _TD_MON)
    dd  = _log_safe(close) - _log_safe(pk)
    return _linslope(dd, _TD_MON)


def cth_drv2_020_atr_norm_5d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day normalized ATR (velocity of range expansion in thrust)."""
    tr   = pd.concat([high - low,
                      (high - close.shift(1)).abs(),
                      (low  - close.shift(1)).abs()], axis=1).max(axis=1)
    atr5 = tr.rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean() / close.clip(lower=_EPS)
    return atr5.diff(_TD_WEEK)


def cth_drv2_021_thrust_5d_vs_21d_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5d-vs-21d return concentration ratio."""
    c5  = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))).abs()
    c21 = (_log_safe(close) - _log_safe(close.shift(_TD_MON))).abs()
    rat = _safe_div(c5, c21 + _EPS)
    return rat.diff(_TD_WEEK)


def cth_drv2_022_bear_body_fraction_5d_5d_diff(close: pd.Series, open: pd.Series,
                                                high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day bear-body fraction (velocity of candle anatomy deterioration)."""
    body  = (open - close).clip(lower=0)
    rng   = (high - low).clip(lower=_EPS)
    frac  = (body / rng).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean()
    return frac.diff(_TD_WEEK)


def cth_drv2_023_panic_score_sigma_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day sigma-exceedance score (acceleration of tail-shock energy)."""
    lr  = _log_ret(close)
    mn  = _rolling_mean(lr, _TD_YEAR)
    sd  = _rolling_std(lr, _TD_YEAR)
    z   = _safe_div(lr - mn, sd)
    exc = (-z - 2.0).clip(lower=0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return exc.diff(_TD_WEEK)


def cth_drv2_024_thrust_intensity_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day thrust intensity (trend in thrust steepness)."""
    cum5      = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    intensity = cum5.clip(upper=0) / _TD_WEEK
    return _linslope(intensity, _TD_MON)


def cth_drv2_025_horizon_thrust_rank_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 252-day percentile rank of the 5d return (rank velocity)."""
    c5   = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    rank = c5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITULATION_THRUST_REGISTRY_2ND_DERIVATIVES = {
    "cth_drv2_001_min_return_5d_5d_diff": {"inputs": ["close"], "func": cth_drv2_001_min_return_5d_5d_diff},
    "cth_drv2_002_min_return_21d_21d_diff": {"inputs": ["close"], "func": cth_drv2_002_min_return_21d_21d_diff},
    "cth_drv2_003_single_day_zscore_5d_diff": {"inputs": ["close"], "func": cth_drv2_003_single_day_zscore_5d_diff},
    "cth_drv2_004_drawdown_21d_5d_diff": {"inputs": ["close"], "func": cth_drv2_004_drawdown_21d_5d_diff},
    "cth_drv2_005_drawdown_63d_21d_diff": {"inputs": ["close"], "func": cth_drv2_005_drawdown_63d_21d_diff},
    "cth_drv2_006_thrust_intensity_5d_5d_diff": {"inputs": ["close"], "func": cth_drv2_006_thrust_intensity_5d_5d_diff},
    "cth_drv2_007_thrust_intensity_21d_21d_diff": {"inputs": ["close"], "func": cth_drv2_007_thrust_intensity_21d_21d_diff},
    "cth_drv2_008_waterfall_freq_21d_diff": {"inputs": ["close"], "func": cth_drv2_008_waterfall_freq_21d_diff},
    "cth_drv2_009_log_slope_5d_5d_diff": {"inputs": ["close"], "func": cth_drv2_009_log_slope_5d_5d_diff},
    "cth_drv2_010_log_slope_21d_21d_diff": {"inputs": ["close"], "func": cth_drv2_010_log_slope_21d_21d_diff},
    "cth_drv2_011_sigma_burst_5d_5d_diff": {"inputs": ["close"], "func": cth_drv2_011_sigma_burst_5d_5d_diff},
    "cth_drv2_012_sigma_burst_21d_21d_diff": {"inputs": ["close"], "func": cth_drv2_012_sigma_burst_21d_21d_diff},
    "cth_drv2_013_panic_composite_5d_21d_diff": {"inputs": ["close"], "func": cth_drv2_013_panic_composite_5d_21d_diff},
    "cth_drv2_014_vol_thrust_score_5d_diff": {"inputs": ["close", "volume"], "func": cth_drv2_014_vol_thrust_score_5d_diff},
    "cth_drv2_015_vol_down_up_ratio_5d_diff": {"inputs": ["close", "volume"], "func": cth_drv2_015_vol_down_up_ratio_5d_diff},
    "cth_drv2_016_thrust_persist_score_5d_diff": {"inputs": ["close"], "func": cth_drv2_016_thrust_persist_score_5d_diff},
    "cth_drv2_017_return_skew_21d_5d_diff": {"inputs": ["close"], "func": cth_drv2_017_return_skew_21d_5d_diff},
    "cth_drv2_018_close_near_low_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": cth_drv2_018_close_near_low_21d_5d_diff},
    "cth_drv2_019_drawdown_21d_slope_21d": {"inputs": ["close"], "func": cth_drv2_019_drawdown_21d_slope_21d},
    "cth_drv2_020_atr_norm_5d_5d_diff": {"inputs": ["close", "high", "low"], "func": cth_drv2_020_atr_norm_5d_5d_diff},
    "cth_drv2_021_thrust_5d_vs_21d_ratio_5d_diff": {"inputs": ["close"], "func": cth_drv2_021_thrust_5d_vs_21d_ratio_5d_diff},
    "cth_drv2_022_bear_body_fraction_5d_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": cth_drv2_022_bear_body_fraction_5d_5d_diff},
    "cth_drv2_023_panic_score_sigma_21d_5d_diff": {"inputs": ["close"], "func": cth_drv2_023_panic_score_sigma_21d_5d_diff},
    "cth_drv2_024_thrust_intensity_5d_slope_21d": {"inputs": ["close"], "func": cth_drv2_024_thrust_intensity_5d_slope_21d},
    "cth_drv2_025_horizon_thrust_rank_5d_5d_diff": {"inputs": ["close"], "func": cth_drv2_025_horizon_thrust_rank_5d_5d_diff},
}
