"""
101_wyckoff_capitulation_structure — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base Wyckoff-structure features — captures the
        acceleration of climax intensity, rally thrust and test-volume dry-up.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return ((xi - xi_m) * (x - x.mean())).sum() / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=True)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def wcs_drv2_001_climax_volume_spike_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 63d climax volume spike ratio."""
    spike = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    return spike.diff(5)


def wcs_drv2_002_worst_down_day_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the worst single-day return over 63 days."""
    return _rolling_min(_daily_ret(close), _TD_QTR).diff(5)


def wcs_drv2_003_panic_count_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the count of high-volume down days (63d)."""
    hi_vol = volume > _rolling_median(volume, _TD_QTR)
    cnt = _rolling_sum(((_daily_ret(close) < 0) & hi_vol).astype(float), _TD_QTR)
    return cnt.diff(5)


def wcs_drv2_004_bounce_off_63d_low_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the percent above the 63d low (rally velocity)."""
    bounce = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return bounce.diff(5)


def wcs_drv2_005_recovery_frac_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 63d range recovery fraction."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _safe_div(close - lo, hi - lo).diff(5)


def wcs_drv2_006_ar_strength_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of automatic-rally strength (21d high vs 63d low)."""
    ar = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_QTR),
                   _rolling_min(close, _TD_QTR))
    return ar.diff(5)


def wcs_drv2_007_retest_volume_contraction_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the retest volume contraction ratio (5d vs 63d max)."""
    rc = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume, _TD_QTR))
    return rc.diff(5)


def wcs_drv2_008_retest_range_contraction_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the retest range contraction ratio."""
    tr = _tr(close, high, low)
    rc = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_max(tr, _TD_QTR))
    return rc.diff(5)


def wcs_drv2_009_range_position_63d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of close position within the 63d range."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _safe_div(close - lo, hi - lo).diff(5)


def wcs_drv2_010_volume_dryup_5_21_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 5d/21d volume dry-up ratio."""
    dry = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))
    return dry.diff(5)


def wcs_drv2_011_range_width_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d range width (range expansion/contraction speed)."""
    rw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    return rw.diff(5)


def wcs_drv2_012_volatility_compression_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d/63d return-std compression ratio."""
    ret = _daily_ret(close)
    vc = _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_QTR))
    return vc.diff(5)


def wcs_drv2_013_higher_low_count_5d_diff(low: pd.Series) -> pd.Series:
    """5-day diff of the 252d higher-low count."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    cnt = _rolling_sum((cur > prior).astype(float), _TD_YEAR)
    return cnt.diff(5)


def wcs_drv2_014_climax_volume_zscore_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 63d volume z-score."""
    return _zscore_rolling(volume, _TD_QTR).diff(5)


def wcs_drv2_015_effort_vs_result_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the effort-vs-result spread (volume z minus return z)."""
    volz = _zscore_rolling(volume, _TD_QTR)
    retz = _zscore_rolling(_daily_ret(close).abs(), _TD_QTR)
    return (volz - retz).diff(5)


def wcs_drv2_016_no_supply_count_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21d no-supply bar count."""
    tr = _tr(close, high, low)
    down = _daily_ret(close) < 0
    narrow = tr < _rolling_median(tr, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    cnt = _rolling_sum((down & narrow & lo_vol).astype(float), _TD_MON)
    return cnt.diff(5)


def wcs_drv2_017_low_zone_dwell_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 252d bottom-quartile dwell fraction."""
    pos = _safe_div(close - _rolling_min(close, _TD_YEAR),
                    _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR))
    dwell = _rolling_mean((pos < 0.25).astype(float), _TD_YEAR)
    return dwell.diff(5)


def wcs_drv2_018_rebound_velocity_21d_slope(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 10-day rebound velocity."""
    vel = _safe_div(_linslope(close, 10), _rolling_mean(close, _TD_MON))
    return _linslope(vel, _TD_MON)


def wcs_drv2_019_test_quality_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the composite test-quality score."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    tr = _tr(close, high, low)
    score = ((pos < 0.20).astype(float) +
             (volume < _rolling_median(volume, _TD_QTR)).astype(float) +
             (tr < _rolling_median(tr, _TD_QTR)).astype(float))
    return score.diff(5)


def wcs_drv2_020_down_volume_share_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21d down-day volume share."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    share = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(volume, _TD_MON))
    return share.diff(5)


def wcs_drv2_021_spring_count_5d_diff(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 252d spring-event count."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _rolling_sum(spring, _TD_YEAR).diff(5)


def wcs_drv2_022_consolidation_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d/63d range contraction ratio."""
    r21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    r63 = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    return _safe_div(r21, r63).diff(5)


def wcs_drv2_023_phase_score_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the climax-rally-test composite score."""
    climax = _rolling_rank_pct(_rolling_max(volume, _TD_WEEK), _TD_YEAR)
    rally = _rolling_max(close.pct_change(5), _TD_QTR).clip(lower=0)
    dryup = 1.0 - _safe_div(_rolling_mean(volume, _TD_WEEK),
                            _rolling_mean(volume, _TD_QTR)).clip(upper=2) / 2
    return (climax + rally + dryup).diff(5)


def wcs_drv2_024_climax_intensity_21d_slope(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of climax intensity (worst vol-weighted return)."""
    volz = _zscore_rolling(volume, _TD_QTR)
    intensity = _rolling_min(_daily_ret(close) * volz.clip(lower=0), _TD_QTR)
    return _linslope(intensity, _TD_MON)


def wcs_drv2_025_structure_index_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the capitulation-structure master index."""
    ret = _daily_ret(close)
    rq = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    vq = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    sc = (_rolling_sum(((ret <= rq) & (volume >= vq)).astype(float), _TD_HALF) > 0).astype(float)
    rally = (_rolling_max(close.pct_change(5), _TD_QTR) > 0.04).astype(float)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    test = ((pos < 0.30) & (volume < _rolling_median(volume, _TD_QTR))).astype(float)
    idx = (sc + rally + test) / 3.0
    return idx.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

WYCKOFF_CAPITULATION_STRUCTURE_REGISTRY_2ND_DERIVATIVES = {
    "wcs_drv2_001_climax_volume_spike_5d_diff": {"inputs": ["volume"], "func": wcs_drv2_001_climax_volume_spike_5d_diff},
    "wcs_drv2_002_worst_down_day_5d_diff": {"inputs": ["close"], "func": wcs_drv2_002_worst_down_day_5d_diff},
    "wcs_drv2_003_panic_count_5d_diff": {"inputs": ["close", "volume"], "func": wcs_drv2_003_panic_count_5d_diff},
    "wcs_drv2_004_bounce_off_63d_low_5d_diff": {"inputs": ["close"], "func": wcs_drv2_004_bounce_off_63d_low_5d_diff},
    "wcs_drv2_005_recovery_frac_63d_5d_diff": {"inputs": ["close"], "func": wcs_drv2_005_recovery_frac_63d_5d_diff},
    "wcs_drv2_006_ar_strength_5d_diff": {"inputs": ["close"], "func": wcs_drv2_006_ar_strength_5d_diff},
    "wcs_drv2_007_retest_volume_contraction_5d_diff": {"inputs": ["volume"], "func": wcs_drv2_007_retest_volume_contraction_5d_diff},
    "wcs_drv2_008_retest_range_contraction_5d_diff": {"inputs": ["close", "high", "low"], "func": wcs_drv2_008_retest_range_contraction_5d_diff},
    "wcs_drv2_009_range_position_63d_5d_diff": {"inputs": ["close"], "func": wcs_drv2_009_range_position_63d_5d_diff},
    "wcs_drv2_010_volume_dryup_5_21_5d_diff": {"inputs": ["volume"], "func": wcs_drv2_010_volume_dryup_5_21_5d_diff},
    "wcs_drv2_011_range_width_21d_5d_diff": {"inputs": ["close"], "func": wcs_drv2_011_range_width_21d_5d_diff},
    "wcs_drv2_012_volatility_compression_5d_diff": {"inputs": ["close"], "func": wcs_drv2_012_volatility_compression_5d_diff},
    "wcs_drv2_013_higher_low_count_5d_diff": {"inputs": ["low"], "func": wcs_drv2_013_higher_low_count_5d_diff},
    "wcs_drv2_014_climax_volume_zscore_5d_diff": {"inputs": ["volume"], "func": wcs_drv2_014_climax_volume_zscore_5d_diff},
    "wcs_drv2_015_effort_vs_result_5d_diff": {"inputs": ["close", "volume"], "func": wcs_drv2_015_effort_vs_result_5d_diff},
    "wcs_drv2_016_no_supply_count_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": wcs_drv2_016_no_supply_count_5d_diff},
    "wcs_drv2_017_low_zone_dwell_5d_diff": {"inputs": ["close"], "func": wcs_drv2_017_low_zone_dwell_5d_diff},
    "wcs_drv2_018_rebound_velocity_21d_slope": {"inputs": ["close"], "func": wcs_drv2_018_rebound_velocity_21d_slope},
    "wcs_drv2_019_test_quality_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": wcs_drv2_019_test_quality_5d_diff},
    "wcs_drv2_020_down_volume_share_5d_diff": {"inputs": ["close", "volume"], "func": wcs_drv2_020_down_volume_share_5d_diff},
    "wcs_drv2_021_spring_count_5d_diff": {"inputs": ["close", "low"], "func": wcs_drv2_021_spring_count_5d_diff},
    "wcs_drv2_022_consolidation_score_5d_diff": {"inputs": ["close"], "func": wcs_drv2_022_consolidation_score_5d_diff},
    "wcs_drv2_023_phase_score_5d_diff": {"inputs": ["close", "volume"], "func": wcs_drv2_023_phase_score_5d_diff},
    "wcs_drv2_024_climax_intensity_21d_slope": {"inputs": ["close", "volume"], "func": wcs_drv2_024_climax_intensity_21d_slope},
    "wcs_drv2_025_structure_index_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": wcs_drv2_025_structure_index_5d_diff},
}
