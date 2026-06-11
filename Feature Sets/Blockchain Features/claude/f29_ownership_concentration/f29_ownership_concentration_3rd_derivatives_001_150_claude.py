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
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f29oc_f29_ownership_concentration_conc_21d_jerk_v001_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_63d_jerk_v002_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_126d_jerk_v003_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_252d_jerk_v004_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_5d_jerk_v005_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 5)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concraw_10d_jerk_v006_signal(percentoftotal):
    result = percentoftotal + _f29_conc(percentoftotal, 10) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_21d_jerk_v007_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_63d_jerk_v008_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_126d_jerk_v009_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_252d_jerk_v010_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_504d_jerk_v011_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_21d_jerk_v012_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    result = _safe_div(c - c.shift(21), c.abs())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_63d_jerk_v013_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 63)
    result = _safe_div(c - c.shift(63), c.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_126d_jerk_v014_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 126)
    result = _safe_div(c - c.shift(126), c.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_252d_jerk_v015_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 252)
    result = _safe_div(c - c.shift(252), c.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_5d_jerk_v016_signal(shrvalue, totalvalue):
    result = _f29_mix(shrvalue, totalvalue) + _f29_conc(shrvalue, 5) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_21d_jerk_v017_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_63d_jerk_v018_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_126d_jerk_v019_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_252d_jerk_v020_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixchg_21d_jerk_v021_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(21), m.abs())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixchg_63d_jerk_v022_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(63), m.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixchg_126d_jerk_v023_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(126), m.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixchg_252d_jerk_v024_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(252), m.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_21d_jerk_v025_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_63d_jerk_v026_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_126d_jerk_v027_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_252d_jerk_v028_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_21d_jerk_v029_signal(percentoftotal):
    result = _std(percentoftotal, 21) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_63d_jerk_v030_signal(percentoftotal):
    result = _std(percentoftotal, 63) + _f29_conc(percentoftotal, 63) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_126d_jerk_v031_signal(percentoftotal):
    result = _std(percentoftotal, 126) + _f29_conc(percentoftotal, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_252d_jerk_v032_signal(percentoftotal):
    result = _std(percentoftotal, 252) + _f29_conc(percentoftotal, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_cv_63d_jerk_v033_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 63), _f29_conc(percentoftotal, 63).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_cv_126d_jerk_v034_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 126), _f29_conc(percentoftotal, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_cv_252d_jerk_v035_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 252), _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_rank_126d_jerk_v036_signal(percentoftotal):
    result = percentoftotal.rolling(126, min_periods=42).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_rank_252d_jerk_v037_signal(percentoftotal):
    result = percentoftotal.rolling(252, min_periods=84).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_rank_63d_jerk_v038_signal(percentoftotal):
    result = percentoftotal.rolling(63, min_periods=21).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_rank_504d_jerk_v039_signal(percentoftotal):
    result = percentoftotal.rolling(504, min_periods=126).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_revert_63d_jerk_v040_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_revert_126d_jerk_v041_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_revert_252d_jerk_v042_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_gap_63_252_jerk_v043_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_gap_21_126_jerk_v044_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21) - _f29_conc(percentoftotal, 126),
                       _f29_conc(percentoftotal, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_gap_21_252_jerk_v045_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpu_21d_jerk_v046_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpu_63d_jerk_v047_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpu_126d_jerk_v048_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuz_63d_jerk_v049_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuz_126d_jerk_v050_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuz_252d_jerk_v051_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuchg_63d_jerk_v052_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(63), v.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuchg_126d_jerk_v053_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(126), v.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vsann_21d_jerk_v054_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21), _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vsann_63d_jerk_v055_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63), _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vs504_126d_jerk_v056_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 126), _f29_conc(percentoftotal, 504).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_skew_126d_jerk_v057_signal(percentoftotal):
    result = percentoftotal.rolling(126, min_periods=42).skew() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_skew_252d_jerk_v058_signal(percentoftotal):
    result = percentoftotal.rolling(252, min_periods=84).skew() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_kurt_126d_jerk_v059_signal(percentoftotal):
    result = percentoftotal.rolling(126, min_periods=42).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_kurt_252d_jerk_v060_signal(percentoftotal):
    result = percentoftotal.rolling(252, min_periods=84).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewm_21d_jerk_v061_signal(percentoftotal):
    result = percentoftotal.ewm(span=21, min_periods=10).mean() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewm_63d_jerk_v062_signal(percentoftotal):
    result = percentoftotal.ewm(span=63, min_periods=21).mean() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewm_126d_jerk_v063_signal(percentoftotal):
    result = percentoftotal.ewm(span=126, min_periods=42).mean() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewmgap_21_63_jerk_v064_signal(percentoftotal):
    fast = percentoftotal.ewm(span=21, min_periods=10).mean()
    slow = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewmgap_63_126_jerk_v065_signal(percentoftotal):
    fast = percentoftotal.ewm(span=63, min_periods=21).mean()
    slow = percentoftotal.ewm(span=126, min_periods=42).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concmix_63d_jerk_v066_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_conc(percentoftotal, 63) * _f29_mix(shrvalue, totalvalue)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concmixz_126d_jerk_v067_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_concz(percentoftotal, 126) * _z(_f29_mix(shrvalue, totalvalue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixdisp_63d_jerk_v068_signal(shrvalue, totalvalue):
    result = _std(_f29_mix(shrvalue, totalvalue), 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixdisp_126d_jerk_v069_signal(shrvalue, totalvalue):
    result = _std(_f29_mix(shrvalue, totalvalue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixrank_252d_jerk_v070_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = m.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_loglvl_63d_jerk_v071_signal(percentoftotal):
    result = np.log(_f29_conc(percentoftotal, 63).abs() + 1.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_logchg_63d_jerk_v072_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    result = np.log(c.abs() + 1.0) - np.log(c.shift(63).abs() + 1.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_accel_21_63_jerk_v073_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    t1 = _safe_div(c - c.shift(21), c.abs())
    t2 = _safe_div(c - c.shift(63), c.abs())
    result = t1 - t2
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_dispratio_63_252_jerk_v074_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 63), _std(percentoftotal, 252)) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpumix_63d_jerk_v075_signal(shrvalue, shrunits, totalvalue):
    result = _z(_f29_vpu(shrvalue, shrunits), 63) * _f29_mix(shrvalue, totalvalue)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_42d_jerk_v076_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_84d_jerk_v077_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_189d_jerk_v078_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_315d_jerk_v079_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_conc_504d_jerk_v080_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_42d_jerk_v081_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_84d_jerk_v082_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 84)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_189d_jerk_v083_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concz_315d_jerk_v084_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 315)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_42d_jerk_v085_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 42)
    result = _safe_div(c - c.shift(42), c.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_84d_jerk_v086_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 84)
    result = _safe_div(c - c.shift(84), c.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_189d_jerk_v087_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 189)
    result = _safe_div(c - c.shift(189), c.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_trend_504d_jerk_v088_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 252)
    result = _safe_div(c - c.shift(504), c.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_42d_jerk_v089_signal(percentoftotal):
    result = _std(percentoftotal, 42) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_84d_jerk_v090_signal(percentoftotal):
    result = _std(percentoftotal, 84) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_disp_504d_jerk_v091_signal(percentoftotal):
    result = _std(percentoftotal, 504) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_cv_42d_jerk_v092_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 42), _f29_conc(percentoftotal, 42).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_cv_189d_jerk_v093_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 189), _f29_conc(percentoftotal, 189).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_42d_jerk_v094_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mix_189d_jerk_v095_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixchg_42d_jerk_v096_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(42), m.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixchg_189d_jerk_v097_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(189), m.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_42d_jerk_v098_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_189d_jerk_v099_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixz_504d_jerk_v100_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_rank_42d_jerk_v101_signal(percentoftotal):
    result = percentoftotal.rolling(42, min_periods=21).rank(pct=True) + _f29_concz(percentoftotal, 42) * 0.01
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_rank_189d_jerk_v102_signal(percentoftotal):
    result = percentoftotal.rolling(189, min_periods=63).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_revert_42d_jerk_v103_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_revert_504d_jerk_v104_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_gap_42_252_jerk_v105_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 42) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_gap_84_252_jerk_v106_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 84) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_gap_126_504_jerk_v107_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 126) - _f29_conc(percentoftotal, 504),
                       _f29_conc(percentoftotal, 504).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpu_252d_jerk_v108_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpu_42d_jerk_v109_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuz_42d_jerk_v110_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 42)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuz_504d_jerk_v111_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuchg_252d_jerk_v112_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(252), v.abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpurank_252d_jerk_v113_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpudisp_126d_jerk_v114_signal(shrvalue, shrunits):
    result = _std(_f29_vpu(shrvalue, shrunits), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpucv_126d_jerk_v115_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(_std(v, 126), _mean(v, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vsann_84d_jerk_v116_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 84), _f29_conc(percentoftotal, 252).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vs504_63d_jerk_v117_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63), _f29_conc(percentoftotal, 504).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_skew_63d_jerk_v118_signal(percentoftotal):
    result = percentoftotal.rolling(63, min_periods=21).skew() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_skew_189d_jerk_v119_signal(percentoftotal):
    result = percentoftotal.rolling(189, min_periods=63).skew() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_kurt_63d_jerk_v120_signal(percentoftotal):
    result = percentoftotal.rolling(63, min_periods=21).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_kurt_189d_jerk_v121_signal(percentoftotal):
    result = percentoftotal.rolling(189, min_periods=63).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewm_42d_jerk_v122_signal(percentoftotal):
    result = percentoftotal.ewm(span=42, min_periods=21).mean() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewm_252d_jerk_v123_signal(percentoftotal):
    result = percentoftotal.ewm(span=252, min_periods=84).mean() + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewmgap_42_126_jerk_v124_signal(percentoftotal):
    fast = percentoftotal.ewm(span=42, min_periods=21).mean()
    slow = percentoftotal.ewm(span=126, min_periods=42).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewmgap_126_252_jerk_v125_signal(percentoftotal):
    fast = percentoftotal.ewm(span=126, min_periods=42).mean()
    slow = percentoftotal.ewm(span=252, min_periods=84).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concmix_84d_jerk_v126_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_conc(percentoftotal, 84) * _f29_mix(shrvalue, totalvalue)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_concmixz_252d_jerk_v127_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_concz(percentoftotal, 252) * _z(_f29_mix(shrvalue, totalvalue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixdisp_252d_jerk_v128_signal(shrvalue, totalvalue):
    result = _std(_f29_mix(shrvalue, totalvalue), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixcv_126d_jerk_v129_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(_std(m, 126), _mean(m, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixrank_126d_jerk_v130_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = m.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_loglvl_126d_jerk_v131_signal(percentoftotal):
    result = np.log(_f29_conc(percentoftotal, 126).abs() + 1.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_logchg_126d_jerk_v132_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    result = np.log(c.abs() + 1.0) - np.log(c.shift(126).abs() + 1.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_accel_63_126_jerk_v133_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 63)
    t1 = _safe_div(c - c.shift(63), c.abs())
    t2 = _safe_div(c - c.shift(126), c.abs())
    result = t1 - t2
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_dispratio_42_126_jerk_v134_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 42), _std(percentoftotal, 126)) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuconc_63d_jerk_v135_signal(shrvalue, shrunits, percentoftotal):
    result = _z(_f29_vpu(shrvalue, shrunits), 63) * _f29_conc(percentoftotal, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixconcdiv_126d_jerk_v136_signal(percentoftotal, shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 126) - _f29_concz(percentoftotal, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_spread_21_63_jerk_v137_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21) - _f29_conc(percentoftotal, 63),
                       _f29_conc(percentoftotal, 63).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_spread_63_126_jerk_v138_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63) - _f29_conc(percentoftotal, 126),
                       _f29_conc(percentoftotal, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_zdiff_63_252_jerk_v139_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 63) - _f29_concz(percentoftotal, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_zdiff_126_504_jerk_v140_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 126) - _f29_concz(percentoftotal, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixtrend_63d_jerk_v141_signal(shrvalue, totalvalue):
    m = _mean(_f29_mix(shrvalue, totalvalue), 63)
    result = _safe_div(m - m.shift(63), m.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixtrend_126d_jerk_v142_signal(shrvalue, totalvalue):
    m = _mean(_f29_mix(shrvalue, totalvalue), 126)
    result = _safe_div(m - m.shift(126), m.abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpulog_63d_jerk_v143_signal(shrvalue, shrunits):
    result = np.log(_mean(_f29_vpu(shrvalue, shrunits), 63).abs() + 1.0)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpumixw_126d_jerk_v144_signal(shrvalue, shrunits, totalvalue):
    result = _z(_f29_vpu(shrvalue, shrunits), 126) * _z(_f29_mix(shrvalue, totalvalue), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_ewmz_126d_jerk_v145_signal(percentoftotal):
    e = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = _z(e, 126) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_revtrend_252d_jerk_v146_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 63)
    trend = _safe_div(c - c.shift(252), c.abs())
    result = trend - _f29_concz(percentoftotal, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_mixcv_252d_jerk_v147_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(_std(m, 252), _mean(m, 252).abs())
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_dispz_252d_jerk_v148_signal(percentoftotal):
    d = _std(percentoftotal, 63)
    result = _z(d, 252) + _f29_conc(percentoftotal, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_vpuratio_126d_jerk_v149_signal(shrvalue, shrunits, percentoftotal):
    result = _safe_div(_mean(_f29_vpu(shrvalue, shrunits), 126), _f29_conc(percentoftotal, 126).abs())
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f29oc_f29_ownership_concentration_blend_multi_jerk_v150_signal(percentoftotal):
    result = (_f29_concz(percentoftotal, 21) + _f29_concz(percentoftotal, 63)
              + _f29_concz(percentoftotal, 126) + _f29_concz(percentoftotal, 252)) / 4.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f29oc_f29_ownership_concentration_conc_21d_jerk_v001_signal,    f29oc_f29_ownership_concentration_conc_63d_jerk_v002_signal,    f29oc_f29_ownership_concentration_conc_126d_jerk_v003_signal,    f29oc_f29_ownership_concentration_conc_252d_jerk_v004_signal,    f29oc_f29_ownership_concentration_conc_5d_jerk_v005_signal,    f29oc_f29_ownership_concentration_concraw_10d_jerk_v006_signal,    f29oc_f29_ownership_concentration_concz_21d_jerk_v007_signal,    f29oc_f29_ownership_concentration_concz_63d_jerk_v008_signal,    f29oc_f29_ownership_concentration_concz_126d_jerk_v009_signal,    f29oc_f29_ownership_concentration_concz_252d_jerk_v010_signal,    f29oc_f29_ownership_concentration_concz_504d_jerk_v011_signal,    f29oc_f29_ownership_concentration_trend_21d_jerk_v012_signal,    f29oc_f29_ownership_concentration_trend_63d_jerk_v013_signal,    f29oc_f29_ownership_concentration_trend_126d_jerk_v014_signal,    f29oc_f29_ownership_concentration_trend_252d_jerk_v015_signal,    f29oc_f29_ownership_concentration_mix_5d_jerk_v016_signal,    f29oc_f29_ownership_concentration_mix_21d_jerk_v017_signal,    f29oc_f29_ownership_concentration_mix_63d_jerk_v018_signal,    f29oc_f29_ownership_concentration_mix_126d_jerk_v019_signal,    f29oc_f29_ownership_concentration_mix_252d_jerk_v020_signal,    f29oc_f29_ownership_concentration_mixchg_21d_jerk_v021_signal,    f29oc_f29_ownership_concentration_mixchg_63d_jerk_v022_signal,    f29oc_f29_ownership_concentration_mixchg_126d_jerk_v023_signal,    f29oc_f29_ownership_concentration_mixchg_252d_jerk_v024_signal,    f29oc_f29_ownership_concentration_mixz_21d_jerk_v025_signal,    f29oc_f29_ownership_concentration_mixz_63d_jerk_v026_signal,    f29oc_f29_ownership_concentration_mixz_126d_jerk_v027_signal,    f29oc_f29_ownership_concentration_mixz_252d_jerk_v028_signal,    f29oc_f29_ownership_concentration_disp_21d_jerk_v029_signal,    f29oc_f29_ownership_concentration_disp_63d_jerk_v030_signal,    f29oc_f29_ownership_concentration_disp_126d_jerk_v031_signal,    f29oc_f29_ownership_concentration_disp_252d_jerk_v032_signal,    f29oc_f29_ownership_concentration_cv_63d_jerk_v033_signal,    f29oc_f29_ownership_concentration_cv_126d_jerk_v034_signal,    f29oc_f29_ownership_concentration_cv_252d_jerk_v035_signal,    f29oc_f29_ownership_concentration_rank_126d_jerk_v036_signal,    f29oc_f29_ownership_concentration_rank_252d_jerk_v037_signal,    f29oc_f29_ownership_concentration_rank_63d_jerk_v038_signal,    f29oc_f29_ownership_concentration_rank_504d_jerk_v039_signal,    f29oc_f29_ownership_concentration_revert_63d_jerk_v040_signal,    f29oc_f29_ownership_concentration_revert_126d_jerk_v041_signal,    f29oc_f29_ownership_concentration_revert_252d_jerk_v042_signal,    f29oc_f29_ownership_concentration_gap_63_252_jerk_v043_signal,    f29oc_f29_ownership_concentration_gap_21_126_jerk_v044_signal,    f29oc_f29_ownership_concentration_gap_21_252_jerk_v045_signal,    f29oc_f29_ownership_concentration_vpu_21d_jerk_v046_signal,    f29oc_f29_ownership_concentration_vpu_63d_jerk_v047_signal,    f29oc_f29_ownership_concentration_vpu_126d_jerk_v048_signal,    f29oc_f29_ownership_concentration_vpuz_63d_jerk_v049_signal,    f29oc_f29_ownership_concentration_vpuz_126d_jerk_v050_signal,    f29oc_f29_ownership_concentration_vpuz_252d_jerk_v051_signal,    f29oc_f29_ownership_concentration_vpuchg_63d_jerk_v052_signal,    f29oc_f29_ownership_concentration_vpuchg_126d_jerk_v053_signal,    f29oc_f29_ownership_concentration_vsann_21d_jerk_v054_signal,    f29oc_f29_ownership_concentration_vsann_63d_jerk_v055_signal,    f29oc_f29_ownership_concentration_vs504_126d_jerk_v056_signal,    f29oc_f29_ownership_concentration_skew_126d_jerk_v057_signal,    f29oc_f29_ownership_concentration_skew_252d_jerk_v058_signal,    f29oc_f29_ownership_concentration_kurt_126d_jerk_v059_signal,    f29oc_f29_ownership_concentration_kurt_252d_jerk_v060_signal,    f29oc_f29_ownership_concentration_ewm_21d_jerk_v061_signal,    f29oc_f29_ownership_concentration_ewm_63d_jerk_v062_signal,    f29oc_f29_ownership_concentration_ewm_126d_jerk_v063_signal,    f29oc_f29_ownership_concentration_ewmgap_21_63_jerk_v064_signal,    f29oc_f29_ownership_concentration_ewmgap_63_126_jerk_v065_signal,    f29oc_f29_ownership_concentration_concmix_63d_jerk_v066_signal,    f29oc_f29_ownership_concentration_concmixz_126d_jerk_v067_signal,    f29oc_f29_ownership_concentration_mixdisp_63d_jerk_v068_signal,    f29oc_f29_ownership_concentration_mixdisp_126d_jerk_v069_signal,    f29oc_f29_ownership_concentration_mixrank_252d_jerk_v070_signal,    f29oc_f29_ownership_concentration_loglvl_63d_jerk_v071_signal,    f29oc_f29_ownership_concentration_logchg_63d_jerk_v072_signal,    f29oc_f29_ownership_concentration_accel_21_63_jerk_v073_signal,    f29oc_f29_ownership_concentration_dispratio_63_252_jerk_v074_signal,    f29oc_f29_ownership_concentration_vpumix_63d_jerk_v075_signal,    f29oc_f29_ownership_concentration_conc_42d_jerk_v076_signal,    f29oc_f29_ownership_concentration_conc_84d_jerk_v077_signal,    f29oc_f29_ownership_concentration_conc_189d_jerk_v078_signal,    f29oc_f29_ownership_concentration_conc_315d_jerk_v079_signal,    f29oc_f29_ownership_concentration_conc_504d_jerk_v080_signal,    f29oc_f29_ownership_concentration_concz_42d_jerk_v081_signal,    f29oc_f29_ownership_concentration_concz_84d_jerk_v082_signal,    f29oc_f29_ownership_concentration_concz_189d_jerk_v083_signal,    f29oc_f29_ownership_concentration_concz_315d_jerk_v084_signal,    f29oc_f29_ownership_concentration_trend_42d_jerk_v085_signal,    f29oc_f29_ownership_concentration_trend_84d_jerk_v086_signal,    f29oc_f29_ownership_concentration_trend_189d_jerk_v087_signal,    f29oc_f29_ownership_concentration_trend_504d_jerk_v088_signal,    f29oc_f29_ownership_concentration_disp_42d_jerk_v089_signal,    f29oc_f29_ownership_concentration_disp_84d_jerk_v090_signal,    f29oc_f29_ownership_concentration_disp_504d_jerk_v091_signal,    f29oc_f29_ownership_concentration_cv_42d_jerk_v092_signal,    f29oc_f29_ownership_concentration_cv_189d_jerk_v093_signal,    f29oc_f29_ownership_concentration_mix_42d_jerk_v094_signal,    f29oc_f29_ownership_concentration_mix_189d_jerk_v095_signal,    f29oc_f29_ownership_concentration_mixchg_42d_jerk_v096_signal,    f29oc_f29_ownership_concentration_mixchg_189d_jerk_v097_signal,    f29oc_f29_ownership_concentration_mixz_42d_jerk_v098_signal,    f29oc_f29_ownership_concentration_mixz_189d_jerk_v099_signal,    f29oc_f29_ownership_concentration_mixz_504d_jerk_v100_signal,    f29oc_f29_ownership_concentration_rank_42d_jerk_v101_signal,    f29oc_f29_ownership_concentration_rank_189d_jerk_v102_signal,    f29oc_f29_ownership_concentration_revert_42d_jerk_v103_signal,    f29oc_f29_ownership_concentration_revert_504d_jerk_v104_signal,    f29oc_f29_ownership_concentration_gap_42_252_jerk_v105_signal,    f29oc_f29_ownership_concentration_gap_84_252_jerk_v106_signal,    f29oc_f29_ownership_concentration_gap_126_504_jerk_v107_signal,    f29oc_f29_ownership_concentration_vpu_252d_jerk_v108_signal,    f29oc_f29_ownership_concentration_vpu_42d_jerk_v109_signal,    f29oc_f29_ownership_concentration_vpuz_42d_jerk_v110_signal,    f29oc_f29_ownership_concentration_vpuz_504d_jerk_v111_signal,    f29oc_f29_ownership_concentration_vpuchg_252d_jerk_v112_signal,    f29oc_f29_ownership_concentration_vpurank_252d_jerk_v113_signal,    f29oc_f29_ownership_concentration_vpudisp_126d_jerk_v114_signal,    f29oc_f29_ownership_concentration_vpucv_126d_jerk_v115_signal,    f29oc_f29_ownership_concentration_vsann_84d_jerk_v116_signal,    f29oc_f29_ownership_concentration_vs504_63d_jerk_v117_signal,    f29oc_f29_ownership_concentration_skew_63d_jerk_v118_signal,    f29oc_f29_ownership_concentration_skew_189d_jerk_v119_signal,    f29oc_f29_ownership_concentration_kurt_63d_jerk_v120_signal,    f29oc_f29_ownership_concentration_kurt_189d_jerk_v121_signal,    f29oc_f29_ownership_concentration_ewm_42d_jerk_v122_signal,    f29oc_f29_ownership_concentration_ewm_252d_jerk_v123_signal,    f29oc_f29_ownership_concentration_ewmgap_42_126_jerk_v124_signal,    f29oc_f29_ownership_concentration_ewmgap_126_252_jerk_v125_signal,    f29oc_f29_ownership_concentration_concmix_84d_jerk_v126_signal,    f29oc_f29_ownership_concentration_concmixz_252d_jerk_v127_signal,    f29oc_f29_ownership_concentration_mixdisp_252d_jerk_v128_signal,    f29oc_f29_ownership_concentration_mixcv_126d_jerk_v129_signal,    f29oc_f29_ownership_concentration_mixrank_126d_jerk_v130_signal,    f29oc_f29_ownership_concentration_loglvl_126d_jerk_v131_signal,    f29oc_f29_ownership_concentration_logchg_126d_jerk_v132_signal,    f29oc_f29_ownership_concentration_accel_63_126_jerk_v133_signal,    f29oc_f29_ownership_concentration_dispratio_42_126_jerk_v134_signal,    f29oc_f29_ownership_concentration_vpuconc_63d_jerk_v135_signal,    f29oc_f29_ownership_concentration_mixconcdiv_126d_jerk_v136_signal,    f29oc_f29_ownership_concentration_spread_21_63_jerk_v137_signal,    f29oc_f29_ownership_concentration_spread_63_126_jerk_v138_signal,    f29oc_f29_ownership_concentration_zdiff_63_252_jerk_v139_signal,    f29oc_f29_ownership_concentration_zdiff_126_504_jerk_v140_signal,    f29oc_f29_ownership_concentration_mixtrend_63d_jerk_v141_signal,    f29oc_f29_ownership_concentration_mixtrend_126d_jerk_v142_signal,    f29oc_f29_ownership_concentration_vpulog_63d_jerk_v143_signal,    f29oc_f29_ownership_concentration_vpumixw_126d_jerk_v144_signal,    f29oc_f29_ownership_concentration_ewmz_126d_jerk_v145_signal,    f29oc_f29_ownership_concentration_revtrend_252d_jerk_v146_signal,    f29oc_f29_ownership_concentration_mixcv_252d_jerk_v147_signal,    f29oc_f29_ownership_concentration_dispz_252d_jerk_v148_signal,    f29oc_f29_ownership_concentration_vpuratio_126d_jerk_v149_signal,    f29oc_f29_ownership_concentration_blend_multi_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_OWNERSHIP_CONCENTRATION_REGISTRY_JERK = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f29_conc', '_f29_concz', '_f29_mix', '_f29_vpu')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f29_ownership_concentration_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
