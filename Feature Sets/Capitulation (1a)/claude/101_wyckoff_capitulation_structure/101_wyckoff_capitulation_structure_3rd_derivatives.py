"""
101_wyckoff_capitulation_structure — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of the 2nd-derivative Wyckoff features — captures the
        exhaustion / inflection of climax, rally and test-volume acceleration.
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


def _accel(s: pd.Series, n: int = 5) -> pd.Series:
    """Second difference: rate of change of the n-day rate of change."""
    return s.diff(n).diff(n)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def wcs_drv3_001_climax_volume_spike_accel(volume: pd.Series) -> pd.Series:
    """Acceleration of the 63d climax volume spike ratio."""
    spike = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    return _accel(spike)


def wcs_drv3_002_worst_down_day_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the worst 63d single-day return."""
    return _accel(_rolling_min(_daily_ret(close), _TD_QTR))


def wcs_drv3_003_panic_count_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the high-volume down-day count."""
    hi_vol = volume > _rolling_median(volume, _TD_QTR)
    cnt = _rolling_sum(((_daily_ret(close) < 0) & hi_vol).astype(float), _TD_QTR)
    return _accel(cnt)


def wcs_drv3_004_bounce_off_low_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the percent above the 63d low (rally inflection)."""
    bounce = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return _accel(bounce)


def wcs_drv3_005_recovery_frac_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 63d range recovery fraction."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _accel(_safe_div(close - lo, hi - lo))


def wcs_drv3_006_ar_strength_accel(close: pd.Series) -> pd.Series:
    """Acceleration of automatic-rally strength."""
    ar = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_QTR),
                   _rolling_min(close, _TD_QTR))
    return _accel(ar)


def wcs_drv3_007_retest_volume_contraction_accel(volume: pd.Series) -> pd.Series:
    """Acceleration of the retest volume contraction ratio."""
    rc = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_max(volume, _TD_QTR))
    return _accel(rc)


def wcs_drv3_008_retest_range_contraction_accel(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Acceleration of the retest range contraction ratio."""
    tr = _tr(close, high, low)
    rc = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_max(tr, _TD_QTR))
    return _accel(rc)


def wcs_drv3_009_range_position_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the close position within the 63d range."""
    lo = _rolling_min(close, _TD_QTR)
    hi = _rolling_max(close, _TD_QTR)
    return _accel(_safe_div(close - lo, hi - lo))


def wcs_drv3_010_volume_dryup_accel(volume: pd.Series) -> pd.Series:
    """Acceleration of the 5d/21d volume dry-up ratio."""
    dry = _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))
    return _accel(dry)


def wcs_drv3_011_range_width_21d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 21d range width."""
    rw = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                   _rolling_min(close, _TD_MON))
    return _accel(rw)


def wcs_drv3_012_volatility_compression_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 21d/63d return-std compression ratio."""
    ret = _daily_ret(close)
    vc = _safe_div(_rolling_std(ret, _TD_MON), _rolling_std(ret, _TD_QTR))
    return _accel(vc)


def wcs_drv3_013_higher_low_count_accel(low: pd.Series) -> pd.Series:
    """Acceleration of the 252d higher-low count."""
    cur = _rolling_min(low, _TD_MON)
    prior = _rolling_min(low, _TD_MON).shift(_TD_MON)
    cnt = _rolling_sum((cur > prior).astype(float), _TD_YEAR)
    return _accel(cnt)


def wcs_drv3_014_climax_volume_zscore_accel(volume: pd.Series) -> pd.Series:
    """Acceleration of the 63d volume z-score."""
    return _accel(_zscore_rolling(volume, _TD_QTR))


def wcs_drv3_015_effort_vs_result_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the effort-vs-result spread."""
    volz = _zscore_rolling(volume, _TD_QTR)
    retz = _zscore_rolling(_daily_ret(close).abs(), _TD_QTR)
    return _accel(volz - retz)


def wcs_drv3_016_no_supply_count_accel(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the 21d no-supply bar count."""
    tr = _tr(close, high, low)
    down = _daily_ret(close) < 0
    narrow = tr < _rolling_median(tr, _TD_QTR)
    lo_vol = volume < _rolling_median(volume, _TD_QTR)
    cnt = _rolling_sum((down & narrow & lo_vol).astype(float), _TD_MON)
    return _accel(cnt)


def wcs_drv3_017_low_zone_dwell_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 252d bottom-quartile dwell fraction."""
    pos = _safe_div(close - _rolling_min(close, _TD_YEAR),
                    _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR))
    dwell = _rolling_mean((pos < 0.25).astype(float), _TD_YEAR)
    return _accel(dwell)


def wcs_drv3_018_bounce_off_low_21d_accel(close: pd.Series) -> pd.Series:
    """Longer-horizon (21d) acceleration of the bounce off the 63d low."""
    bounce = _safe_div(close - _rolling_min(close, _TD_QTR), _rolling_min(close, _TD_QTR))
    return _accel(bounce, _TD_MON)


def wcs_drv3_019_test_quality_accel(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the composite test-quality score."""
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    tr = _tr(close, high, low)
    score = ((pos < 0.20).astype(float) +
             (volume < _rolling_median(volume, _TD_QTR)).astype(float) +
             (tr < _rolling_median(tr, _TD_QTR)).astype(float))
    return _accel(score)


def wcs_drv3_020_down_volume_share_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the 21d down-day volume share."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    share = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(volume, _TD_MON))
    return _accel(share)


def wcs_drv3_021_spring_count_accel(close: pd.Series, low: pd.Series) -> pd.Series:
    """Acceleration of the 252d spring-event count."""
    prior_low = _rolling_min(low, _TD_QTR).shift(1)
    spring = ((low < prior_low) & (close > prior_low)).astype(float)
    return _accel(_rolling_sum(spring, _TD_YEAR))


def wcs_drv3_022_consolidation_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 21d/63d range contraction ratio."""
    r21 = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    r63 = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    return _accel(_safe_div(r21, r63))


def wcs_drv3_023_phase_score_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the climax-rally-test composite score."""
    climax = _rolling_rank_pct(_rolling_max(volume, _TD_WEEK), _TD_YEAR)
    rally = _rolling_max(close.pct_change(5), _TD_QTR).clip(lower=0)
    dryup = 1.0 - _safe_div(_rolling_mean(volume, _TD_WEEK),
                            _rolling_mean(volume, _TD_QTR)).clip(upper=2) / 2
    return _accel(climax + rally + dryup)


def wcs_drv3_024_recovery_frac_252d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 252d range recovery fraction."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    return _accel(_safe_div(close - lo, hi - lo))


def wcs_drv3_025_structure_index_accel(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the capitulation-structure master index."""
    ret = _daily_ret(close)
    rq = ret.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    vq = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    sc = (_rolling_sum(((ret <= rq) & (volume >= vq)).astype(float), _TD_HALF) > 0).astype(float)
    rally = (_rolling_max(close.pct_change(5), _TD_QTR) > 0.04).astype(float)
    pos = _safe_div(close - _rolling_min(close, _TD_QTR),
                    _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR))
    test = ((pos < 0.30) & (volume < _rolling_median(volume, _TD_QTR))).astype(float)
    idx = (sc + rally + test) / 3.0
    return _accel(idx)


# ── Registry ──────────────────────────────────────────────────────────────────

WYCKOFF_CAPITULATION_STRUCTURE_REGISTRY_3RD_DERIVATIVES = {
    "wcs_drv3_001_climax_volume_spike_accel": {"inputs": ["volume"], "func": wcs_drv3_001_climax_volume_spike_accel},
    "wcs_drv3_002_worst_down_day_accel": {"inputs": ["close"], "func": wcs_drv3_002_worst_down_day_accel},
    "wcs_drv3_003_panic_count_accel": {"inputs": ["close", "volume"], "func": wcs_drv3_003_panic_count_accel},
    "wcs_drv3_004_bounce_off_low_accel": {"inputs": ["close"], "func": wcs_drv3_004_bounce_off_low_accel},
    "wcs_drv3_005_recovery_frac_accel": {"inputs": ["close"], "func": wcs_drv3_005_recovery_frac_accel},
    "wcs_drv3_006_ar_strength_accel": {"inputs": ["close"], "func": wcs_drv3_006_ar_strength_accel},
    "wcs_drv3_007_retest_volume_contraction_accel": {"inputs": ["volume"], "func": wcs_drv3_007_retest_volume_contraction_accel},
    "wcs_drv3_008_retest_range_contraction_accel": {"inputs": ["close", "high", "low"], "func": wcs_drv3_008_retest_range_contraction_accel},
    "wcs_drv3_009_range_position_accel": {"inputs": ["close"], "func": wcs_drv3_009_range_position_accel},
    "wcs_drv3_010_volume_dryup_accel": {"inputs": ["volume"], "func": wcs_drv3_010_volume_dryup_accel},
    "wcs_drv3_011_range_width_21d_accel": {"inputs": ["close"], "func": wcs_drv3_011_range_width_21d_accel},
    "wcs_drv3_012_volatility_compression_accel": {"inputs": ["close"], "func": wcs_drv3_012_volatility_compression_accel},
    "wcs_drv3_013_higher_low_count_accel": {"inputs": ["low"], "func": wcs_drv3_013_higher_low_count_accel},
    "wcs_drv3_014_climax_volume_zscore_accel": {"inputs": ["volume"], "func": wcs_drv3_014_climax_volume_zscore_accel},
    "wcs_drv3_015_effort_vs_result_accel": {"inputs": ["close", "volume"], "func": wcs_drv3_015_effort_vs_result_accel},
    "wcs_drv3_016_no_supply_count_accel": {"inputs": ["close", "high", "low", "volume"], "func": wcs_drv3_016_no_supply_count_accel},
    "wcs_drv3_017_low_zone_dwell_accel": {"inputs": ["close"], "func": wcs_drv3_017_low_zone_dwell_accel},
    "wcs_drv3_018_bounce_off_low_21d_accel": {"inputs": ["close"], "func": wcs_drv3_018_bounce_off_low_21d_accel},
    "wcs_drv3_019_test_quality_accel": {"inputs": ["close", "high", "low", "volume"], "func": wcs_drv3_019_test_quality_accel},
    "wcs_drv3_020_down_volume_share_accel": {"inputs": ["close", "volume"], "func": wcs_drv3_020_down_volume_share_accel},
    "wcs_drv3_021_spring_count_accel": {"inputs": ["close", "low"], "func": wcs_drv3_021_spring_count_accel},
    "wcs_drv3_022_consolidation_score_accel": {"inputs": ["close"], "func": wcs_drv3_022_consolidation_score_accel},
    "wcs_drv3_023_phase_score_accel": {"inputs": ["close", "volume"], "func": wcs_drv3_023_phase_score_accel},
    "wcs_drv3_024_recovery_frac_252d_accel": {"inputs": ["close"], "func": wcs_drv3_024_recovery_frac_252d_accel},
    "wcs_drv3_025_structure_index_accel": {"inputs": ["close", "high", "low", "volume"], "func": wcs_drv3_025_structure_index_accel},
}
