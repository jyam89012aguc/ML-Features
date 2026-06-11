"""
52_bar_morphology — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base bar-morphology body/range concepts — velocity /
        acceleration of body-size, body-to-range ratio, bull/bear body counts,
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def bmf_drv2_001_body_abs_sma21_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day body SMA (velocity of recent average body size)."""
    sma21 = _rolling_mean(_body_abs(close, open), _TD_MON)
    return sma21.diff(_TD_WEEK)


def bmf_drv2_002_body_abs_sma21_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 21-day body SMA (monthly change in average body size)."""
    sma21 = _rolling_mean(_body_abs(close, open), _TD_MON)
    return sma21.diff(_TD_MON)


def bmf_drv2_003_body_to_range_sma21_5d_diff(close: pd.Series, open: pd.Series,
                                              high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day body-to-range SMA (velocity of bar-fill trend)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    sma21 = _rolling_mean(btr, _TD_MON)
    return sma21.diff(_TD_WEEK)


def bmf_drv2_004_body_to_range_sma63_21d_diff(close: pd.Series, open: pd.Series,
                                               high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day body-to-range SMA."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    sma63 = _rolling_mean(btr, _TD_QTR)
    return sma63.diff(_TD_MON)


def bmf_drv2_005_bull_body_fraction_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day bull-body fraction (velocity of bull/bear shift)."""
    frac = _safe_div(
        _rolling_sum((close > open).astype(float), _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )
    return frac.diff(_TD_WEEK)


def bmf_drv2_006_bear_bull_ratio_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day bear/bull body count ratio."""
    bear = _rolling_sum((close < open).astype(float), _TD_MON)
    bull = _rolling_sum((close > open).astype(float), _TD_MON)
    ratio = _safe_div(bear, bull)
    return ratio.diff(_TD_WEEK)


def bmf_drv2_007_body_zscore_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day body z-score (velocity of extremity)."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_MON)
    s = _rolling_std(babs, _TD_MON)
    z = _safe_div(babs - m, s)
    return z.diff(_TD_WEEK)


def bmf_drv2_008_body_cv_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day body coefficient of variation."""
    babs = _body_abs(close, open)
    cv = _safe_div(_rolling_std(babs, _TD_MON), _rolling_mean(babs, _TD_MON))
    return cv.diff(_TD_WEEK)


def bmf_drv2_009_bear_to_bull_body_size_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day bear-to-bull body size ratio."""
    babs = _body_abs(close, open)
    bull = babs.where(close > open, np.nan).rolling(_TD_MON, min_periods=1).mean()
    bear = babs.where(close < open, np.nan).rolling(_TD_MON, min_periods=1).mean()
    ratio = _safe_div(bear, bull)
    return ratio.diff(_TD_WEEK)


def bmf_drv2_010_body_sma5_vs_sma21_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of the 5d/21d body SMA ratio."""
    babs = _body_abs(close, open)
    ratio = _safe_div(_rolling_mean(babs, _TD_WEEK), _rolling_mean(babs, _TD_MON))
    return ratio.diff(_TD_WEEK)


def bmf_drv2_011_body_sma21_vs_sma63_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of the 21d/63d body SMA ratio."""
    babs = _body_abs(close, open)
    ratio = _safe_div(_rolling_mean(babs, _TD_MON), _rolling_mean(babs, _TD_QTR))
    return ratio.diff(_TD_MON)


def bmf_drv2_012_bear_body_dominance_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day bear body dominance fraction."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    dom = _safe_div(_rolling_sum(bear, _TD_MON), _rolling_sum(babs, _TD_MON))
    return dom.diff(_TD_WEEK)


def bmf_drv2_013_net_body_sum_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day net signed body sum."""
    net = _rolling_sum(_body(close, open), _TD_MON)
    return net.diff(_TD_WEEK)


def bmf_drv2_014_body_to_range_ratio_slope_21d(close: pd.Series, open: pd.Series,
                                                high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of body-to-range ratio over trailing 21 days."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    return _linslope(btr, _TD_MON)


def bmf_drv2_015_body_abs_sma5_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 5-day body SMA over trailing 21 days."""
    sma5 = _rolling_mean(_body_abs(close, open), _TD_WEEK)
    return _linslope(sma5, _TD_MON)


def bmf_drv2_016_body_to_avg_range_21d_5d_diff(close: pd.Series, open: pd.Series,
                                                high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of body-to-21d-avg-range ratio."""
    babs = _body_abs(close, open)
    avg_r = _rolling_mean(_range(high, low), _TD_MON)
    ratio = _safe_div(babs, avg_r)
    return ratio.diff(_TD_WEEK)


def bmf_drv2_017_doji_fraction_21d_5d_diff(close: pd.Series, open: pd.Series,
                                            high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day doji fraction (velocity of doji occurrence)."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    doji = (btr < 0.10).astype(float)
    frac = _safe_div(
        _rolling_sum(doji, _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )
    return frac.diff(_TD_WEEK)


def bmf_drv2_018_marubozu_fraction_21d_5d_diff(close: pd.Series, open: pd.Series,
                                                high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day marubozu fraction."""
    btr = _safe_div(_body_abs(close, open), _range(high, low))
    maru = (btr >= 0.90).astype(float)
    frac = _safe_div(
        _rolling_sum(maru, _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )
    return frac.diff(_TD_WEEK)


def bmf_drv2_019_body_skew_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day body skewness."""
    skew63 = _body_abs(close, open).rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()
    return skew63.diff(_TD_MON)


def bmf_drv2_020_body_q90_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day 90th-percentile body (change in outsized bar threshold)."""
    q90 = _body_abs(close, open).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.90)
    return q90.diff(_TD_MON)


def bmf_drv2_021_bear_body_dominance_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day diff of 63-day bear body dominance fraction."""
    babs = _body_abs(close, open)
    bear = babs.where(close < open, 0.0)
    dom = _safe_div(_rolling_sum(bear, _TD_QTR), _rolling_sum(babs, _TD_QTR))
    return dom.diff(_TD_MON)


def bmf_drv2_022_body_energy_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day body energy (sum of squared bodies)."""
    energy = _rolling_sum(_body_abs(close, open) ** 2, _TD_MON)
    return energy.diff(_TD_WEEK)


def bmf_drv2_023_body_range_corr_63d_21d_diff(close: pd.Series, open: pd.Series,
                                               high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day body-range correlation."""
    babs = _body_abs(close, open)
    rng = _range(high, low)
    corr = babs.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).corr(rng)
    return corr.diff(_TD_MON)


def bmf_drv2_024_body_composite_score_5d_diff(close: pd.Series, open: pd.Series,
                                              high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of composite body score (body z + body-to-range z, 21d window)."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_MON)
    s = _rolling_std(babs, _TD_MON)
    body_z = _safe_div(babs - m, s)
    btr = _safe_div(babs, _range(high, low))
    btr_z = _safe_div(btr - _rolling_mean(btr, _TD_MON), _rolling_std(btr, _TD_MON))
    composite = (body_z.fillna(0.0) + btr_z.fillna(0.0)) / 2.0
    return composite.diff(_TD_WEEK)


def bmf_drv2_025_bear_body_sum_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day bear body sum (velocity of bear pressure accumulation)."""
    babs = _body_abs(close, open)
    bear_sum = _rolling_sum(babs.where(close < open, 0.0), _TD_MON)
    return bear_sum.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

BAR_MORPHOLOGY_REGISTRY_2ND_DERIVATIVES = {
    "bmf_drv2_001_body_abs_sma21_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_001_body_abs_sma21_5d_diff},
    "bmf_drv2_002_body_abs_sma21_21d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_002_body_abs_sma21_21d_diff},
    "bmf_drv2_003_body_to_range_sma21_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_003_body_to_range_sma21_5d_diff},
    "bmf_drv2_004_body_to_range_sma63_21d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_004_body_to_range_sma63_21d_diff},
    "bmf_drv2_005_bull_body_fraction_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_005_bull_body_fraction_21d_5d_diff},
    "bmf_drv2_006_bear_bull_ratio_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_006_bear_bull_ratio_21d_5d_diff},
    "bmf_drv2_007_body_zscore_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_007_body_zscore_21d_5d_diff},
    "bmf_drv2_008_body_cv_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_008_body_cv_21d_5d_diff},
    "bmf_drv2_009_bear_to_bull_body_size_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_009_bear_to_bull_body_size_21d_5d_diff},
    "bmf_drv2_010_body_sma5_vs_sma21_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_010_body_sma5_vs_sma21_5d_diff},
    "bmf_drv2_011_body_sma21_vs_sma63_21d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_011_body_sma21_vs_sma63_21d_diff},
    "bmf_drv2_012_bear_body_dominance_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_012_bear_body_dominance_21d_5d_diff},
    "bmf_drv2_013_net_body_sum_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_013_net_body_sum_21d_5d_diff},
    "bmf_drv2_014_body_to_range_ratio_slope_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_014_body_to_range_ratio_slope_21d},
    "bmf_drv2_015_body_abs_sma5_slope_21d": {"inputs": ["close", "open"], "func": bmf_drv2_015_body_abs_sma5_slope_21d},
    "bmf_drv2_016_body_to_avg_range_21d_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_016_body_to_avg_range_21d_5d_diff},
    "bmf_drv2_017_doji_fraction_21d_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_017_doji_fraction_21d_5d_diff},
    "bmf_drv2_018_marubozu_fraction_21d_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_018_marubozu_fraction_21d_5d_diff},
    "bmf_drv2_019_body_skew_63d_21d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_019_body_skew_63d_21d_diff},
    "bmf_drv2_020_body_q90_63d_21d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_020_body_q90_63d_21d_diff},
    "bmf_drv2_021_bear_body_dominance_63d_21d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_021_bear_body_dominance_63d_21d_diff},
    "bmf_drv2_022_body_energy_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_022_body_energy_21d_5d_diff},
    "bmf_drv2_023_body_range_corr_63d_21d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_023_body_range_corr_63d_21d_diff},
    "bmf_drv2_024_body_composite_score_5d_diff": {"inputs": ["close", "open", "high", "low"], "func": bmf_drv2_024_body_composite_score_5d_diff},
    "bmf_drv2_025_bear_body_sum_21d_5d_diff": {"inputs": ["close", "open"], "func": bmf_drv2_025_bear_body_sum_21d_5d_diff},
}
