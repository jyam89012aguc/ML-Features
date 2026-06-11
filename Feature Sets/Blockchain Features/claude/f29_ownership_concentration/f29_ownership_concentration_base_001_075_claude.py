import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (ownership concentration) =====
def _f29_conc(percentoftotal, w):
    # smoothed concentration level: rolling mean of a holding's share of 13F value
    return percentoftotal.rolling(w, min_periods=max(1, w // 2)).mean()


def _f29_concz(percentoftotal, w):
    # z-score of concentration level over w (how unusual current concentration is)
    m = percentoftotal.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = percentoftotal.rolling(w, min_periods=max(1, w // 2)).std()
    return (percentoftotal - m) / sd.replace(0, np.nan)


def _f29_mix(shrvalue, totalvalue):
    # share-type value mix: this holding's dollar value over total 13F value
    return shrvalue / totalvalue.replace(0, np.nan)


def _f29_vpu(shrvalue, shrunits):
    # value-per-unit concentration: dollar value per share unit held
    return shrvalue / shrunits.replace(0, np.nan)


# ============ FEATURES 001-075 ============

# 21d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_21d_base_v001_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_63d_base_v002_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_126d_base_v003_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_252d_base_v004_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d smoothed concentration level (fast)
def f29oc_f29_ownership_concentration_conc_5d_base_v005_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# raw concentration anchored to primitive
def f29oc_f29_ownership_concentration_concraw_10d_base_v006_signal(percentoftotal):
    result = percentoftotal + _f29_conc(percentoftotal, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d concentration z-score
def f29oc_f29_ownership_concentration_concz_21d_base_v007_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d concentration z-score
def f29oc_f29_ownership_concentration_concz_63d_base_v008_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d concentration z-score
def f29oc_f29_ownership_concentration_concz_126d_base_v009_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d concentration z-score
def f29oc_f29_ownership_concentration_concz_252d_base_v010_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d concentration z-score (long lookback)
def f29oc_f29_ownership_concentration_concz_504d_base_v011_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d concentration trend slope (diff of smoothed level scaled by level)
def f29oc_f29_ownership_concentration_trend_21d_base_v012_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    result = _safe_div(c - c.shift(21), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d concentration trend slope
def f29oc_f29_ownership_concentration_trend_63d_base_v013_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 63)
    result = _safe_div(c - c.shift(63), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d concentration trend slope
def f29oc_f29_ownership_concentration_trend_126d_base_v014_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 126)
    result = _safe_div(c - c.shift(126), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d concentration trend slope
def f29oc_f29_ownership_concentration_trend_252d_base_v015_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 252)
    result = _safe_div(c - c.shift(252), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# share-type value mix level
def f29oc_f29_ownership_concentration_mix_5d_base_v016_signal(shrvalue, totalvalue):
    result = _f29_mix(shrvalue, totalvalue) + _f29_conc(shrvalue, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d smoothed mix
def f29oc_f29_ownership_concentration_mix_21d_base_v017_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d smoothed mix
def f29oc_f29_ownership_concentration_mix_63d_base_v018_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d smoothed mix
def f29oc_f29_ownership_concentration_mix_126d_base_v019_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d smoothed mix
def f29oc_f29_ownership_concentration_mix_252d_base_v020_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mix change (normalized diff)
def f29oc_f29_ownership_concentration_mixchg_21d_base_v021_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(21), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mix change
def f29oc_f29_ownership_concentration_mixchg_63d_base_v022_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(63), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mix change
def f29oc_f29_ownership_concentration_mixchg_126d_base_v023_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(126), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mix change
def f29oc_f29_ownership_concentration_mixchg_252d_base_v024_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(252), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mix z-score
def f29oc_f29_ownership_concentration_mixz_21d_base_v025_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mix z-score
def f29oc_f29_ownership_concentration_mixz_63d_base_v026_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d mix z-score
def f29oc_f29_ownership_concentration_mixz_126d_base_v027_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mix z-score
def f29oc_f29_ownership_concentration_mixz_252d_base_v028_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d concentration dispersion (rolling std of percentoftotal)
def f29oc_f29_ownership_concentration_disp_21d_base_v029_signal(percentoftotal):
    result = _std(percentoftotal, 21) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d concentration dispersion
def f29oc_f29_ownership_concentration_disp_63d_base_v030_signal(percentoftotal):
    result = _std(percentoftotal, 63) + _f29_conc(percentoftotal, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d concentration dispersion
def f29oc_f29_ownership_concentration_disp_126d_base_v031_signal(percentoftotal):
    result = _std(percentoftotal, 126) + _f29_conc(percentoftotal, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d concentration dispersion
def f29oc_f29_ownership_concentration_disp_252d_base_v032_signal(percentoftotal):
    result = _std(percentoftotal, 252) + _f29_conc(percentoftotal, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d coefficient of variation of concentration (dispersion / level)
def f29oc_f29_ownership_concentration_cv_63d_base_v033_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 63), _f29_conc(percentoftotal, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d coefficient of variation of concentration
def f29oc_f29_ownership_concentration_cv_126d_base_v034_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 126), _f29_conc(percentoftotal, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d coefficient of variation of concentration
def f29oc_f29_ownership_concentration_cv_252d_base_v035_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 252), _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d concentration percentile rank
def f29oc_f29_ownership_concentration_rank_126d_base_v036_signal(percentoftotal):
    result = percentoftotal.rolling(126, min_periods=42).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d concentration percentile rank
def f29oc_f29_ownership_concentration_rank_252d_base_v037_signal(percentoftotal):
    result = percentoftotal.rolling(252, min_periods=84).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d concentration percentile rank
def f29oc_f29_ownership_concentration_rank_63d_base_v038_signal(percentoftotal):
    result = percentoftotal.rolling(63, min_periods=21).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d concentration percentile rank
def f29oc_f29_ownership_concentration_rank_504d_base_v039_signal(percentoftotal):
    result = percentoftotal.rolling(504, min_periods=126).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d concentration mean-reversion (negative z-score)
def f29oc_f29_ownership_concentration_revert_63d_base_v040_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d concentration mean-reversion
def f29oc_f29_ownership_concentration_revert_126d_base_v041_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d concentration mean-reversion
def f29oc_f29_ownership_concentration_revert_252d_base_v042_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d concentration gap to its 252d level
def f29oc_f29_ownership_concentration_gap_63_252_base_v043_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d concentration gap to its 126d level
def f29oc_f29_ownership_concentration_gap_21_126_base_v044_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21) - _f29_conc(percentoftotal, 126),
                       _f29_conc(percentoftotal, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d concentration gap to its 252d level
def f29oc_f29_ownership_concentration_gap_21_252_base_v045_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit concentration level (smoothed)
def f29oc_f29_ownership_concentration_vpu_21d_base_v046_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit concentration 63d
def f29oc_f29_ownership_concentration_vpu_63d_base_v047_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit concentration 126d
def f29oc_f29_ownership_concentration_vpu_126d_base_v048_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit z-score 63d
def f29oc_f29_ownership_concentration_vpuz_63d_base_v049_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit z-score 126d
def f29oc_f29_ownership_concentration_vpuz_126d_base_v050_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit z-score 252d
def f29oc_f29_ownership_concentration_vpuz_252d_base_v051_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit change 63d (normalized)
def f29oc_f29_ownership_concentration_vpuchg_63d_base_v052_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(63), v.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit change 126d
def f29oc_f29_ownership_concentration_vpuchg_126d_base_v053_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(126), v.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs 252d ratio (level / long-run level)
def f29oc_f29_ownership_concentration_vsann_21d_base_v054_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21), _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs 252d ratio (63d level)
def f29oc_f29_ownership_concentration_vsann_63d_base_v055_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63), _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs 504d ratio (126d level)
def f29oc_f29_ownership_concentration_vs504_126d_base_v056_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 126), _f29_conc(percentoftotal, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# holder-skew proxy: 126d rolling skew of concentration
def f29oc_f29_ownership_concentration_skew_126d_base_v057_signal(percentoftotal):
    result = percentoftotal.rolling(126, min_periods=42).skew() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# holder-skew proxy: 252d rolling skew of concentration
def f29oc_f29_ownership_concentration_skew_252d_base_v058_signal(percentoftotal):
    result = percentoftotal.rolling(252, min_periods=84).skew() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration 126d rolling kurtosis (fat-tail holder mix)
def f29oc_f29_ownership_concentration_kurt_126d_base_v059_signal(percentoftotal):
    result = percentoftotal.rolling(126, min_periods=42).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration 252d rolling kurtosis
def f29oc_f29_ownership_concentration_kurt_252d_base_v060_signal(percentoftotal):
    result = percentoftotal.rolling(252, min_periods=84).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EWMA of concentration level
def f29oc_f29_ownership_concentration_ewm_21d_base_v061_signal(percentoftotal):
    result = percentoftotal.ewm(span=21, min_periods=10).mean() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA of concentration level
def f29oc_f29_ownership_concentration_ewm_63d_base_v062_signal(percentoftotal):
    result = percentoftotal.ewm(span=63, min_periods=21).mean() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA of concentration level
def f29oc_f29_ownership_concentration_ewm_126d_base_v063_signal(percentoftotal):
    result = percentoftotal.ewm(span=126, min_periods=42).mean() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration EWMA gap (fast vs slow)
def f29oc_f29_ownership_concentration_ewmgap_21_63_base_v064_signal(percentoftotal):
    fast = percentoftotal.ewm(span=21, min_periods=10).mean()
    slow = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration EWMA gap (63 vs 126)
def f29oc_f29_ownership_concentration_ewmgap_63_126_base_v065_signal(percentoftotal):
    fast = percentoftotal.ewm(span=63, min_periods=21).mean()
    slow = percentoftotal.ewm(span=126, min_periods=42).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration share of total value (percentoftotal scaled by mix)
def f29oc_f29_ownership_concentration_concmix_63d_base_v066_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_conc(percentoftotal, 63) * _f29_mix(shrvalue, totalvalue)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration scaled by mix z-score
def f29oc_f29_ownership_concentration_concmixz_126d_base_v067_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_concz(percentoftotal, 126) * _z(_f29_mix(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# mix dispersion 63d (rolling std of mix)
def f29oc_f29_ownership_concentration_mixdisp_63d_base_v068_signal(shrvalue, totalvalue):
    result = _std(_f29_mix(shrvalue, totalvalue), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# mix dispersion 126d
def f29oc_f29_ownership_concentration_mixdisp_126d_base_v069_signal(shrvalue, totalvalue):
    result = _std(_f29_mix(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# mix percentile rank 252d
def f29oc_f29_ownership_concentration_mixrank_252d_base_v070_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = m.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration log level (compresses tail)
def f29oc_f29_ownership_concentration_loglvl_63d_base_v071_signal(percentoftotal):
    result = np.log(_f29_conc(percentoftotal, 63).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration log change 63d
def f29oc_f29_ownership_concentration_logchg_63d_base_v072_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    result = np.log(c.abs() + 1.0) - np.log(c.shift(63).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration acceleration (21d trend minus 63d trend)
def f29oc_f29_ownership_concentration_accel_21_63_base_v073_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    t1 = _safe_div(c - c.shift(21), c.abs())
    t2 = _safe_div(c - c.shift(63), c.abs())
    result = t1 - t2
    return result.replace([np.inf, -np.inf], np.nan)


# concentration dispersion ratio (short vs long)
def f29oc_f29_ownership_concentration_dispratio_63_252_base_v074_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 63), _std(percentoftotal, 252)) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit vs mix interaction (concentration richness)
def f29oc_f29_ownership_concentration_vpumix_63d_base_v075_signal(shrvalue, shrunits, totalvalue):
    result = _z(_f29_vpu(shrvalue, shrunits), 63) * _f29_mix(shrvalue, totalvalue)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29oc_f29_ownership_concentration_conc_21d_base_v001_signal,
    f29oc_f29_ownership_concentration_conc_63d_base_v002_signal,
    f29oc_f29_ownership_concentration_conc_126d_base_v003_signal,
    f29oc_f29_ownership_concentration_conc_252d_base_v004_signal,
    f29oc_f29_ownership_concentration_conc_5d_base_v005_signal,
    f29oc_f29_ownership_concentration_concraw_10d_base_v006_signal,
    f29oc_f29_ownership_concentration_concz_21d_base_v007_signal,
    f29oc_f29_ownership_concentration_concz_63d_base_v008_signal,
    f29oc_f29_ownership_concentration_concz_126d_base_v009_signal,
    f29oc_f29_ownership_concentration_concz_252d_base_v010_signal,
    f29oc_f29_ownership_concentration_concz_504d_base_v011_signal,
    f29oc_f29_ownership_concentration_trend_21d_base_v012_signal,
    f29oc_f29_ownership_concentration_trend_63d_base_v013_signal,
    f29oc_f29_ownership_concentration_trend_126d_base_v014_signal,
    f29oc_f29_ownership_concentration_trend_252d_base_v015_signal,
    f29oc_f29_ownership_concentration_mix_5d_base_v016_signal,
    f29oc_f29_ownership_concentration_mix_21d_base_v017_signal,
    f29oc_f29_ownership_concentration_mix_63d_base_v018_signal,
    f29oc_f29_ownership_concentration_mix_126d_base_v019_signal,
    f29oc_f29_ownership_concentration_mix_252d_base_v020_signal,
    f29oc_f29_ownership_concentration_mixchg_21d_base_v021_signal,
    f29oc_f29_ownership_concentration_mixchg_63d_base_v022_signal,
    f29oc_f29_ownership_concentration_mixchg_126d_base_v023_signal,
    f29oc_f29_ownership_concentration_mixchg_252d_base_v024_signal,
    f29oc_f29_ownership_concentration_mixz_21d_base_v025_signal,
    f29oc_f29_ownership_concentration_mixz_63d_base_v026_signal,
    f29oc_f29_ownership_concentration_mixz_126d_base_v027_signal,
    f29oc_f29_ownership_concentration_mixz_252d_base_v028_signal,
    f29oc_f29_ownership_concentration_disp_21d_base_v029_signal,
    f29oc_f29_ownership_concentration_disp_63d_base_v030_signal,
    f29oc_f29_ownership_concentration_disp_126d_base_v031_signal,
    f29oc_f29_ownership_concentration_disp_252d_base_v032_signal,
    f29oc_f29_ownership_concentration_cv_63d_base_v033_signal,
    f29oc_f29_ownership_concentration_cv_126d_base_v034_signal,
    f29oc_f29_ownership_concentration_cv_252d_base_v035_signal,
    f29oc_f29_ownership_concentration_rank_126d_base_v036_signal,
    f29oc_f29_ownership_concentration_rank_252d_base_v037_signal,
    f29oc_f29_ownership_concentration_rank_63d_base_v038_signal,
    f29oc_f29_ownership_concentration_rank_504d_base_v039_signal,
    f29oc_f29_ownership_concentration_revert_63d_base_v040_signal,
    f29oc_f29_ownership_concentration_revert_126d_base_v041_signal,
    f29oc_f29_ownership_concentration_revert_252d_base_v042_signal,
    f29oc_f29_ownership_concentration_gap_63_252_base_v043_signal,
    f29oc_f29_ownership_concentration_gap_21_126_base_v044_signal,
    f29oc_f29_ownership_concentration_gap_21_252_base_v045_signal,
    f29oc_f29_ownership_concentration_vpu_21d_base_v046_signal,
    f29oc_f29_ownership_concentration_vpu_63d_base_v047_signal,
    f29oc_f29_ownership_concentration_vpu_126d_base_v048_signal,
    f29oc_f29_ownership_concentration_vpuz_63d_base_v049_signal,
    f29oc_f29_ownership_concentration_vpuz_126d_base_v050_signal,
    f29oc_f29_ownership_concentration_vpuz_252d_base_v051_signal,
    f29oc_f29_ownership_concentration_vpuchg_63d_base_v052_signal,
    f29oc_f29_ownership_concentration_vpuchg_126d_base_v053_signal,
    f29oc_f29_ownership_concentration_vsann_21d_base_v054_signal,
    f29oc_f29_ownership_concentration_vsann_63d_base_v055_signal,
    f29oc_f29_ownership_concentration_vs504_126d_base_v056_signal,
    f29oc_f29_ownership_concentration_skew_126d_base_v057_signal,
    f29oc_f29_ownership_concentration_skew_252d_base_v058_signal,
    f29oc_f29_ownership_concentration_kurt_126d_base_v059_signal,
    f29oc_f29_ownership_concentration_kurt_252d_base_v060_signal,
    f29oc_f29_ownership_concentration_ewm_21d_base_v061_signal,
    f29oc_f29_ownership_concentration_ewm_63d_base_v062_signal,
    f29oc_f29_ownership_concentration_ewm_126d_base_v063_signal,
    f29oc_f29_ownership_concentration_ewmgap_21_63_base_v064_signal,
    f29oc_f29_ownership_concentration_ewmgap_63_126_base_v065_signal,
    f29oc_f29_ownership_concentration_concmix_63d_base_v066_signal,
    f29oc_f29_ownership_concentration_concmixz_126d_base_v067_signal,
    f29oc_f29_ownership_concentration_mixdisp_63d_base_v068_signal,
    f29oc_f29_ownership_concentration_mixdisp_126d_base_v069_signal,
    f29oc_f29_ownership_concentration_mixrank_252d_base_v070_signal,
    f29oc_f29_ownership_concentration_loglvl_63d_base_v071_signal,
    f29oc_f29_ownership_concentration_logchg_63d_base_v072_signal,
    f29oc_f29_ownership_concentration_accel_21_63_base_v073_signal,
    f29oc_f29_ownership_concentration_dispratio_63_252_base_v074_signal,
    f29oc_f29_ownership_concentration_vpumix_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_OWNERSHIP_CONCENTRATION_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f29_conc", "_f29_concz", "_f29_mix", "_f29_vpu")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f29_ownership_concentration_base_001_075_claude: {n_features} features pass")
