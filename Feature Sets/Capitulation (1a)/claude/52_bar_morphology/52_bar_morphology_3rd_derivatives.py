"""
52_bar_morphology — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative bar-morphology features — acceleration of
        velocity of body-size, body-to-range ratio, bull/bear body measures,
        and body distribution statistics
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _body_abs(close: pd.Series, open_: pd.Series) -> pd.Series:
    return (close - open_).abs()


def _body(close: pd.Series, open_: pd.Series) -> pd.Series:
    return close - open_


def _range(high: pd.Series, low: pd.Series) -> pd.Series:
    return (high - low).clip(lower=0.0)


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
# Each 3rd-derivative = diff/slope/pct-change applied to a 2nd-derivative concept

def bmf_drv3_001_body_abs_sma21_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day body SMA (acceleration of body-size velocity)."""
    sma21 = _rolling_mean(_body_abs(close, open), _TD_MON)
    vel = sma21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_002_body_abs_sma21_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21-day body SMA."""
    sma21 = _rolling_mean(_body_abs(close, open), _TD_MON)
    vel21 = sma21.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def bmf_drv3_003_body_to_range_sma21_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                      high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day body-to-range SMA (acceleration of bar-fill trend)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    sma21 = _rolling_mean(btr, _TD_MON)
    vel = sma21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_004_bull_body_fraction_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day bull-body fraction."""
    frac = _safe_div(
        _rolling_sum((close > open).astype(float), _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_005_bear_bull_ratio_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day bear/bull body ratio."""
    bear = _rolling_sum((close < open).astype(float), _TD_MON)
    bull = _rolling_sum((close > open).astype(float), _TD_MON)
    ratio = _safe_div(bear, bull)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_006_body_zscore_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day body z-score (jerk in body extremity)."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_MON)
    s = _rolling_std(babs, _TD_MON)
    z = _safe_div(babs - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_007_body_cv_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day body coefficient of variation."""
    babs = _body_abs(close, open)
    cv = _safe_div(_rolling_std(babs, _TD_MON), _rolling_mean(babs, _TD_MON))
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_008_bear_body_dominance_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day bear body dominance fraction."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    dom = _safe_div(_rolling_sum(bear, _TD_MON), _rolling_sum(babs, _TD_MON))
    vel = dom.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_009_net_body_sum_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day net signed body sum."""
    net = _rolling_sum(_body(close, open), _TD_MON)
    vel = net.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_010_body_to_range_ratio_slope_5d_diff(close: pd.Series, open: pd.Series,
                                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of body-to-range ratio over 21 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    slp = _linslope(btr, _TD_MON)
    return slp.diff(_TD_WEEK)


def bmf_drv3_011_body_sma5_slope_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day body SMA (rate of slope change)."""
    sma5 = _rolling_mean(_body_abs(close, open), _TD_WEEK)
    slp = _linslope(sma5, _TD_MON)
    return slp.diff(_TD_WEEK)


def bmf_drv3_012_body_to_avg_range_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                        high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of body-to-21d-avg-range ratio."""
    babs = _body_abs(close, open)
    avg_r = _rolling_mean(_range(high, low), _TD_MON)
    ratio = _safe_div(babs, avg_r)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_013_doji_fraction_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day doji fraction."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    doji = (btr < 0.10).astype(float)
    frac = _safe_div(
        _rolling_sum(doji, _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_014_marubozu_fraction_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                        high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day marubozu fraction."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    maru = (btr >= 0.90).astype(float)
    frac = _safe_div(
        _rolling_sum(maru, _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )
    vel = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_015_body_sma5_vs_sma21_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of the 5d/21d body SMA ratio."""
    babs = _body_abs(close, open)
    ratio = _safe_div(_rolling_mean(babs, _TD_WEEK), _rolling_mean(babs, _TD_MON))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_016_body_sma21_vs_sma63_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21d/63d body SMA ratio."""
    babs = _body_abs(close, open)
    ratio = _safe_div(_rolling_mean(babs, _TD_MON), _rolling_mean(babs, _TD_QTR))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def bmf_drv3_017_body_skew_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day body skewness."""
    skew63 = _body_abs(close, open).rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()
    vel21 = skew63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def bmf_drv3_018_body_q90_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day 90th-percentile body."""
    q90 = _body_abs(close, open).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.90)
    vel21 = q90.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def bmf_drv3_019_bear_body_dominance_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day bear body dominance."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    dom = _safe_div(_rolling_sum(bear, _TD_QTR), _rolling_sum(babs, _TD_QTR))
    vel21 = dom.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def bmf_drv3_020_body_energy_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day body energy."""
    energy = _rolling_sum(_body_abs(close, open) ** 2, _TD_MON)
    vel = energy.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_021_bear_body_sum_21d_5d_diff_slope(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of bear body sum."""
    babs = _body_abs(close, open)
    bear_sum = _rolling_sum(babs.where(close < open, 0.0), _TD_MON)
    vel = bear_sum.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def bmf_drv3_022_bear_to_bull_body_size_21d_5d_diff_slope(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of bear/bull body size ratio."""
    babs = _body_abs(close, open)
    bull = babs.where(close > open, np.nan).rolling(_TD_MON, min_periods=1).mean()
    bear = babs.where(close < open, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(bear, bull)
    vel = ratio.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def bmf_drv3_023_body_composite_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                 high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of composite body score."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_MON)
    s = _rolling_std(babs, _TD_MON)
    body_z = _safe_div(babs - m, s)
    btr = _safe_div(babs, _range(high, low))
    btr_z = _safe_div(btr - _rolling_mean(btr, _TD_MON), _rolling_std(btr, _TD_MON))
    composite = (body_z.fillna(0.0) + btr_z.fillna(0.0)) / 2.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def bmf_drv3_024_net_body_sum_21d_5d_diff_slope(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day net body sum."""
    net = _rolling_sum(_body(close, open), _TD_MON)
    vel = net.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def bmf_drv3_025_body_to_range_sma21_5d_diff_slope(close: pd.Series, open: pd.Series,
                                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day body-to-range SMA."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    sma21 = _rolling_mean(btr, _TD_MON)
    vel = sma21.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

BAR_MORPHOLOGY_REGISTRY_3RD_DERIVATIVES = {
    "bmf_drv3_001_body_abs_sma21_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_001_body_abs_sma21_5d_diff_5d_diff},
    "bmf_drv3_002_body_abs_sma21_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_002_body_abs_sma21_21d_diff_5d_diff},
    "bmf_drv3_003_body_to_range_sma21_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_003_body_to_range_sma21_5d_diff_5d_diff},
    "bmf_drv3_004_bull_body_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_004_bull_body_fraction_21d_5d_diff_5d_diff},
    "bmf_drv3_005_bear_bull_ratio_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_005_bear_bull_ratio_21d_5d_diff_5d_diff},
    "bmf_drv3_006_body_zscore_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_006_body_zscore_21d_5d_diff_5d_diff},
    "bmf_drv3_007_body_cv_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_007_body_cv_21d_5d_diff_5d_diff},
    "bmf_drv3_008_bear_body_dominance_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_008_bear_body_dominance_21d_5d_diff_5d_diff},
    "bmf_drv3_009_net_body_sum_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_009_net_body_sum_21d_5d_diff_5d_diff},
    "bmf_drv3_010_body_to_range_ratio_slope_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_010_body_to_range_ratio_slope_5d_diff},
    "bmf_drv3_011_body_sma5_slope_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_011_body_sma5_slope_5d_diff},
    "bmf_drv3_012_body_to_avg_range_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_012_body_to_avg_range_21d_5d_diff_5d_diff},
    "bmf_drv3_013_doji_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_013_doji_fraction_21d_5d_diff_5d_diff},
    "bmf_drv3_014_marubozu_fraction_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_014_marubozu_fraction_21d_5d_diff_5d_diff},
    "bmf_drv3_015_body_sma5_vs_sma21_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_015_body_sma5_vs_sma21_5d_diff_5d_diff},
    "bmf_drv3_016_body_sma21_vs_sma63_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_016_body_sma21_vs_sma63_21d_diff_5d_diff},
    "bmf_drv3_017_body_skew_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_017_body_skew_63d_21d_diff_5d_diff},
    "bmf_drv3_018_body_q90_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_018_body_q90_63d_21d_diff_5d_diff},
    "bmf_drv3_019_bear_body_dominance_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_019_bear_body_dominance_63d_21d_diff_5d_diff},
    "bmf_drv3_020_body_energy_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv3_020_body_energy_21d_5d_diff_5d_diff},
    "bmf_drv3_021_bear_body_sum_21d_5d_diff_slope": {"inputs": ["close", "open"], "func": bmf_drv3_021_bear_body_sum_21d_5d_diff_slope},
    "bmf_drv3_022_bear_to_bull_body_size_21d_5d_diff_slope": {"inputs": ["close", "open"], "func": bmf_drv3_022_bear_to_bull_body_size_21d_5d_diff_slope},
    "bmf_drv3_023_body_composite_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_023_body_composite_5d_diff_5d_diff},
    "bmf_drv3_024_net_body_sum_21d_5d_diff_slope": {"inputs": ["close", "open"], "func": bmf_drv3_024_net_body_sum_21d_5d_diff_slope},
    "bmf_drv3_025_body_to_range_sma21_5d_diff_slope": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv3_025_body_to_range_sma21_5d_diff_slope},
}
