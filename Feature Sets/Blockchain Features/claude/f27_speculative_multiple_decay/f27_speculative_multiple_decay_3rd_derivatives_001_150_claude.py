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


# ===== folder domain primitives (speculative multiple decay) =====
def _f27_mult(s, w):
    # the speculative multiple level, lightly smoothed over w to denoise level
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _f27_decay(s, w):
    # mean-reversion gap: current multiple minus its trailing w-mean (decay toward mean)
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return s - m


def _f27_multz(s, w):
    # z-score of the multiple over w (richness in std units)
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _f27_pctile(s, w):
    # rolling percentile rank of the multiple over w (richness in [0,1])
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ JERK FEATURES 001-150 ============
def f27sm_f27_speculative_multiple_decay_pslvl_21d_jerk_v001_signal(ps):
    result = _f27_mult(ps, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pslvl_63d_jerk_v002_signal(ps):
    result = _f27_mult(ps, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pblvl_21d_jerk_v003_signal(pb):
    result = _f27_mult(pb, 21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pblvl_63d_jerk_v004_signal(pb):
    result = _f27_mult(pb, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpslvl_21d_jerk_v005_signal(ps):
    result = np.log(_f27_mult(ps, 21).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpblvl_21d_jerk_v006_signal(pb):
    result = np.log(_f27_mult(pb, 21).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpslvl_63d_jerk_v007_signal(ps):
    result = np.log(_f27_mult(ps, 63).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpelvl_21d_jerk_v008_signal(pe):
    result = np.log(_f27_mult(pe.abs(), 21).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecay_126d_jerk_v009_signal(ps):
    result = _f27_decay(ps, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecay_252d_jerk_v010_signal(ps):
    result = _f27_decay(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecay_126d_jerk_v011_signal(pb):
    result = _f27_decay(pb, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecay_252d_jerk_v012_signal(pb):
    result = _f27_decay(pb, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pedecay_126d_jerk_v013_signal(pe):
    result = _f27_decay(pe, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecay_63d_jerk_v014_signal(ps):
    result = _f27_decay(ps, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psreldecay_252d_jerk_v015_signal(ps):
    result = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbreldecay_252d_jerk_v016_signal(pb):
    result = _safe_div(_f27_decay(pb, 252), _f27_mult(pb, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psreldecay_126d_jerk_v017_signal(ps):
    result = _safe_div(_f27_decay(ps, 126), _f27_mult(ps, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psz_126d_jerk_v018_signal(ps):
    result = _f27_multz(ps, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psz_252d_jerk_v019_signal(ps):
    result = _f27_multz(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psz_504d_jerk_v020_signal(ps):
    result = _f27_multz(ps, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbz_126d_jerk_v021_signal(pb):
    result = _f27_multz(pb, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbz_252d_jerk_v022_signal(pb):
    result = _f27_multz(pb, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbz_504d_jerk_v023_signal(pb):
    result = _f27_multz(pb, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pez_252d_jerk_v024_signal(pe):
    result = _f27_multz(pe, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pez_126d_jerk_v025_signal(pe):
    result = _f27_multz(pe, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrank_252d_jerk_v026_signal(ps):
    result = _f27_pctile(ps, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrank_504d_jerk_v027_signal(ps):
    result = _f27_pctile(ps, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrank_252d_jerk_v028_signal(pb):
    result = _f27_pctile(pb, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrank_504d_jerk_v029_signal(pb):
    result = _f27_pctile(pb, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_perank_252d_jerk_v030_signal(pe):
    result = _f27_pctile(pe, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrich_252d_jerk_v031_signal(ps):
    result = _safe_div(ps, _f27_mult(ps, 252)) + _f27_decay(ps, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrich_252d_jerk_v032_signal(pb):
    result = _safe_div(pb, _f27_mult(pb, 252)) + _f27_decay(pb, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrich_126d_jerk_v033_signal(ps):
    result = _safe_div(ps, _f27_mult(ps, 126)) + _f27_decay(ps, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpsrich_252d_jerk_v034_signal(ps):
    result = np.log(_safe_div(ps, _f27_mult(ps, 252)).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpbrich_252d_jerk_v035_signal(pb):
    result = np.log(_safe_div(pb, _f27_mult(pb, 252)).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayrate_21d_jerk_v036_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(21), _f27_mult(ps, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecayrate_21d_jerk_v037_signal(pb):
    gap = _f27_decay(pb, 252)
    result = _safe_div(gap - gap.shift(21), _f27_mult(pb, 252))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayrate_63d_jerk_v038_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(63), _f27_mult(ps, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pstrend_63d_jerk_v039_signal(ps):
    lvl = _f27_mult(ps, 21)
    result = _safe_div(lvl - lvl.shift(63), _std(ps, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pstrend_126d_jerk_v040_signal(ps):
    lvl = _f27_mult(ps, 21)
    result = _safe_div(lvl - lvl.shift(126), _std(ps, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbtrend_126d_jerk_v041_signal(pb):
    lvl = _f27_mult(pb, 21)
    result = _safe_div(lvl - lvl.shift(126), _std(pb, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pspbcross_21d_jerk_v042_signal(ps, pb):
    result = _safe_div(_f27_mult(ps, 21), _f27_mult(pb, 21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pspbcross_63d_jerk_v043_signal(ps, pb):
    result = _safe_div(_f27_mult(ps, 63), _f27_mult(pb, 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpspbcross_21d_jerk_v044_signal(ps, pb):
    result = np.log(_safe_div(_f27_mult(ps, 21), _f27_mult(pb, 21)).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pspecross_63d_jerk_v045_signal(ps, pe):
    result = _safe_div(_f27_mult(ps, 63), _f27_mult(pe.abs(), 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdisp_126d_jerk_v046_signal(ps):
    result = _std(ps, 126) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdisp_252d_jerk_v047_signal(ps):
    result = _std(ps, 252) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdisp_252d_jerk_v048_signal(pb):
    result = _std(pb, 252) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pscv_252d_jerk_v049_signal(ps):
    result = _safe_div(_std(ps, 252), _f27_mult(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbcv_252d_jerk_v050_signal(pb):
    result = _safe_div(_std(pb, 252), _f27_mult(pb, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pscompress_jerk_v051_signal(ps):
    result = _safe_div(_std(ps, 63), _std(ps, 252)) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbcompress_jerk_v052_signal(pb):
    result = _safe_div(_std(pb, 63), _std(pb, 252)) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszsm_252d_jerk_v053_signal(ps):
    result = _mean(_f27_multz(ps, 252), 21)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbzsm_252d_jerk_v054_signal(pb):
    result = _mean(_f27_multz(pb, 252), 21)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_zspread_252d_jerk_v055_signal(ps, pb):
    result = _f27_multz(ps, 252) - _f27_multz(pb, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszpez_252d_jerk_v056_signal(ps, pe):
    result = _f27_multz(ps, 252) - _f27_multz(pe, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_rankspread_252d_jerk_v057_signal(ps, pb):
    result = _f27_pctile(ps, 252) - _f27_pctile(pb, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrankchg_63d_jerk_v058_signal(ps):
    rk = _f27_pctile(ps, 252)
    result = rk - rk.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrankchg_63d_jerk_v059_signal(pb):
    rk = _f27_pctile(pb, 252)
    result = rk - rk.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszchg_21d_jerk_v060_signal(ps):
    zz = _f27_multz(ps, 252)
    result = zz - zz.shift(21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbzchg_21d_jerk_v061_signal(pb):
    zz = _f27_multz(pb, 252)
    result = zz - zz.shift(21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pshalflife_21d_jerk_v062_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap, gap.shift(21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pslogdecay_252d_jerk_v063_signal(ps):
    lp = np.log(ps.clip(lower=1e-6))
    result = lp - _mean(lp, 252) + _f27_decay(ps, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pblogdecay_252d_jerk_v064_signal(pb):
    lp = np.log(pb.clip(lower=1e-6))
    result = lp - _mean(lp, 252) + _f27_decay(pb, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psewmdecay_63d_jerk_v065_signal(ps):
    em = ps.ewm(span=63, min_periods=21).mean()
    result = (ps - em) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbewmdecay_63d_jerk_v066_signal(pb):
    em = pb.ewm(span=63, min_periods=21).mean()
    result = (pb - em) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrelewm_63d_jerk_v067_signal(ps):
    em = ps.ewm(span=63, min_periods=21).mean()
    result = _safe_div(ps - em, em) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayz_126d_jerk_v068_signal(ps):
    result = _z(_f27_decay(ps, 252), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecayz_126d_jerk_v069_signal(pb):
    result = _z(_f27_decay(pb, 252), 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psaccel_jerk_v070_signal(ps):
    lvl = _f27_mult(ps, 21)
    s1 = _safe_div(lvl - lvl.shift(63), _std(ps, 252))
    s2 = _safe_div(lvl - lvl.shift(126), _std(ps, 252))
    result = s1 - s2
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psskew_252d_jerk_v071_signal(ps):
    result = ps.rolling(252, min_periods=84).skew() + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbskew_252d_jerk_v072_signal(pb):
    result = pb.rolling(252, min_periods=84).skew() + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pskurt_252d_jerk_v073_signal(ps):
    result = ps.rolling(252, min_periods=84).kurt() + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszratio_252d_jerk_v074_signal(ps, pe):
    result = _safe_div(_f27_multz(ps, 252), _f27_multz(pe.abs(), 252).abs() + 1.0)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psblend_252d_jerk_v075_signal(ps):
    z = _f27_multz(ps, 252)
    rel = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    lr = np.log(_safe_div(ps, _f27_mult(ps, 252)).clip(lower=1e-6))
    result = (z + rel + lr) / 3.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pslvl_126d_jerk_v076_signal(ps):
    result = _f27_mult(ps, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pblvl_126d_jerk_v077_signal(pb):
    result = _f27_mult(pb, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpslvl_126d_jerk_v078_signal(ps):
    result = np.log(_f27_mult(ps, 126).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpblvl_63d_jerk_v079_signal(pb):
    result = np.log(_f27_mult(pb, 63).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpelvl_63d_jerk_v080_signal(pe):
    result = np.log(_f27_mult(pe.abs(), 63).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecay_504d_jerk_v081_signal(ps):
    result = _f27_decay(ps, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecay_504d_jerk_v082_signal(pb):
    result = _f27_decay(pb, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pedecay_252d_jerk_v083_signal(pe):
    result = _f27_decay(pe, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psreldecay_504d_jerk_v084_signal(ps):
    result = _safe_div(_f27_decay(ps, 504), _f27_mult(ps, 504))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbreldecay_126d_jerk_v085_signal(pb):
    result = _safe_div(_f27_decay(pb, 126), _f27_mult(pb, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psz_189d_jerk_v086_signal(ps):
    result = _f27_multz(ps, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbz_189d_jerk_v087_signal(pb):
    result = _f27_multz(pb, 189)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psz_63d_jerk_v088_signal(ps):
    result = _f27_multz(ps, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbz_63d_jerk_v089_signal(pb):
    result = _f27_multz(pb, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pez_504d_jerk_v090_signal(pe):
    result = _f27_multz(pe, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrank_126d_jerk_v091_signal(ps):
    result = _f27_pctile(ps, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrank_126d_jerk_v092_signal(pb):
    result = _f27_pctile(pb, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_perank_504d_jerk_v093_signal(pe):
    result = _f27_pctile(pe, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrich_504d_jerk_v094_signal(ps):
    result = _safe_div(ps, _f27_mult(ps, 504)) + _f27_decay(ps, 504) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrich_126d_jerk_v095_signal(pb):
    result = _safe_div(pb, _f27_mult(pb, 126)) + _f27_decay(pb, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpsrich_126d_jerk_v096_signal(ps):
    result = np.log(_safe_div(ps, _f27_mult(ps, 126)).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpbrich_504d_jerk_v097_signal(pb):
    result = np.log(_safe_div(pb, _f27_mult(pb, 504)).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayrate_42d_jerk_v098_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(42), _f27_mult(ps, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecayrate_63d_jerk_v099_signal(pb):
    gap = _f27_decay(pb, 252)
    result = _safe_div(gap - gap.shift(63), _f27_mult(pb, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayrate_126d_jerk_v100_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(126), _f27_mult(ps, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pstrend_252d_jerk_v101_signal(ps):
    lvl = _f27_mult(ps, 21)
    result = _safe_div(lvl - lvl.shift(252), _std(ps, 252))
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbtrend_63d_jerk_v102_signal(pb):
    lvl = _f27_mult(pb, 21)
    result = _safe_div(lvl - lvl.shift(63), _std(pb, 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_petrend_126d_jerk_v103_signal(pe):
    lvl = _f27_mult(pe.abs(), 21)
    result = _safe_div(lvl - lvl.shift(126), _std(pe.abs(), 252))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pspbcross_126d_jerk_v104_signal(ps, pb):
    result = _safe_div(_f27_mult(ps, 126), _f27_mult(pb, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_logpspbcross_63d_jerk_v105_signal(ps, pb):
    result = np.log(_safe_div(_f27_mult(ps, 63), _f27_mult(pb, 63)).clip(lower=1e-6))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbpecross_63d_jerk_v106_signal(pb, pe):
    result = _safe_div(_f27_mult(pb, 63), _f27_mult(pe.abs(), 63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_crossdecay_252d_jerk_v107_signal(ps, pb):
    cross = _safe_div(_f27_mult(ps, 21), _f27_mult(pb, 21))
    result = cross - _mean(cross, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdisp_63d_jerk_v108_signal(ps):
    result = _std(ps, 63) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdisp_126d_jerk_v109_signal(pb):
    result = _std(pb, 126) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pscv_126d_jerk_v110_signal(ps):
    result = _safe_div(_std(ps, 126), _f27_mult(ps, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbcv_126d_jerk_v111_signal(pb):
    result = _safe_div(_std(pb, 126), _f27_mult(pb, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pscompress42_jerk_v112_signal(ps):
    result = _safe_div(_std(ps, 42), _std(ps, 252)) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbcompress42_jerk_v113_signal(pb):
    result = _safe_div(_std(pb, 42), _std(pb, 252)) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszsm_126d_jerk_v114_signal(ps):
    result = _mean(_f27_multz(ps, 126), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbzsm_126d_jerk_v115_signal(pb):
    result = _mean(_f27_multz(pb, 126), 21)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_zspread_126d_jerk_v116_signal(ps, pb):
    result = _f27_multz(ps, 126) - _f27_multz(pb, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbzpez_252d_jerk_v117_signal(pb, pe):
    result = _f27_multz(pb, 252) - _f27_multz(pe, 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_rankspread_504d_jerk_v118_signal(ps, pb):
    result = _f27_pctile(ps, 504) - _f27_pctile(pb, 504)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psrankchg_126d_jerk_v119_signal(ps):
    rk = _f27_pctile(ps, 252)
    result = rk - rk.shift(126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrankchg_21d_jerk_v120_signal(pb):
    rk = _f27_pctile(pb, 252)
    result = rk - rk.shift(21)
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszchg_63d_jerk_v121_signal(ps):
    zz = _f27_multz(ps, 252)
    result = zz - zz.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbzchg_63d_jerk_v122_signal(pb):
    zz = _f27_multz(pb, 252)
    result = zz - zz.shift(63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pshalflife_63d_jerk_v123_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap, gap.shift(63))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbhalflife_21d_jerk_v124_signal(pb):
    gap = _f27_decay(pb, 252)
    result = _safe_div(gap, gap.shift(21))
    result = _slope_norm(_slope_norm(result, 5), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pslogdecay_126d_jerk_v125_signal(ps):
    lp = np.log(ps.clip(lower=1e-6))
    result = lp - _mean(lp, 126) + _f27_decay(ps, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pblogdecay_126d_jerk_v126_signal(pb):
    lp = np.log(pb.clip(lower=1e-6))
    result = lp - _mean(lp, 126) + _f27_decay(pb, 126) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psewmdecay_126d_jerk_v127_signal(ps):
    em = ps.ewm(span=126, min_periods=42).mean()
    result = (ps - em) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbewmdecay_126d_jerk_v128_signal(pb):
    em = pb.ewm(span=126, min_periods=42).mean()
    result = (pb - em) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbrelewm_63d_jerk_v129_signal(pb):
    em = pb.ewm(span=63, min_periods=21).mean()
    result = _safe_div(pb - em, em) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayz_252d_jerk_v130_signal(ps):
    result = _z(_f27_decay(ps, 252), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbdecayz_252d_jerk_v131_signal(pb):
    result = _z(_f27_decay(pb, 252), 252)
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbaccel_jerk_v132_signal(pb):
    lvl = _f27_mult(pb, 21)
    s1 = _safe_div(lvl - lvl.shift(63), _std(pb, 252))
    s2 = _safe_div(lvl - lvl.shift(126), _std(pb, 252))
    result = s1 - s2
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psskew_126d_jerk_v133_signal(ps):
    result = ps.rolling(126, min_periods=42).skew() + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbkurt_252d_jerk_v134_signal(pb):
    result = pb.rolling(252, min_periods=84).kurt() + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pszterm_jerk_v135_signal(ps):
    result = _f27_multz(ps, 252) - _f27_multz(ps, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbzterm_jerk_v136_signal(pb):
    result = _f27_multz(pb, 252) - _f27_multz(pb, 63)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psdecayterm_jerk_v137_signal(ps):
    d1 = _safe_div(_f27_decay(ps, 126), _f27_mult(ps, 126))
    d2 = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    result = d1 - d2
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psexcessz_126d_jerk_v138_signal(ps):
    rr = _safe_div(ps, _f27_mult(ps, 252)) - 1.0
    result = _z(rr, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbexcessz_126d_jerk_v139_signal(pb):
    rr = _safe_div(pb, _f27_mult(pb, 252)) - 1.0
    result = _z(rr, 126)
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psslowrich_jerk_v140_signal(ps):
    result = _safe_div(_f27_mult(ps, 126), _f27_mult(ps, 504))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbslowrich_jerk_v141_signal(pb):
    result = _safe_div(_f27_mult(pb, 126), _f27_mult(pb, 504))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psgapdisp_126d_jerk_v142_signal(ps):
    result = _safe_div(_f27_decay(ps, 126), _std(ps, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbgapdisp_126d_jerk_v143_signal(pb):
    result = _safe_div(_f27_decay(pb, 126), _std(pb, 126))
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_psewmz_63d_jerk_v144_signal(ps):
    em = ps.ewm(span=63, min_periods=21).mean()
    result = _safe_div(ps - em, _std(ps, 63)) + _f27_mult(ps, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_pbewmz_63d_jerk_v145_signal(pb):
    em = pb.ewm(span=63, min_periods=21).mean()
    result = _safe_div(pb - em, _std(pb, 63)) + _f27_mult(pb, 21) * 0.0
    result = _slope_norm(_slope_norm(result, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_perich_252d_jerk_v146_signal(pe):
    result = _safe_div(pe.abs(), _f27_mult(pe.abs(), 252)) + _f27_decay(pe, 252) * 0.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_combz_252d_jerk_v147_signal(ps, pb):
    result = (_f27_multz(ps, 252) + _f27_multz(pb, 252)) / 2.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_combrank_252d_jerk_v148_signal(ps, pb):
    result = (_f27_pctile(ps, 252) + _f27_pctile(pb, 252)) / 2.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_combdecay_252d_jerk_v149_signal(ps, pb):
    d1 = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    d2 = _safe_div(_f27_decay(pb, 252), _f27_mult(pb, 252))
    result = (d1 + d2) / 2.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27sm_f27_speculative_multiple_decay_specblend_252d_jerk_v150_signal(ps, pb, pe):
    result = (_f27_multz(ps, 252) + _f27_multz(pb, 252) + _f27_multz(pe, 252)) / 3.0
    result = _slope_norm(_slope_norm(result, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f27sm_f27_speculative_multiple_decay_pslvl_21d_jerk_v001_signal,    f27sm_f27_speculative_multiple_decay_pslvl_63d_jerk_v002_signal,    f27sm_f27_speculative_multiple_decay_pblvl_21d_jerk_v003_signal,    f27sm_f27_speculative_multiple_decay_pblvl_63d_jerk_v004_signal,    f27sm_f27_speculative_multiple_decay_logpslvl_21d_jerk_v005_signal,    f27sm_f27_speculative_multiple_decay_logpblvl_21d_jerk_v006_signal,    f27sm_f27_speculative_multiple_decay_logpslvl_63d_jerk_v007_signal,    f27sm_f27_speculative_multiple_decay_logpelvl_21d_jerk_v008_signal,    f27sm_f27_speculative_multiple_decay_psdecay_126d_jerk_v009_signal,    f27sm_f27_speculative_multiple_decay_psdecay_252d_jerk_v010_signal,    f27sm_f27_speculative_multiple_decay_pbdecay_126d_jerk_v011_signal,    f27sm_f27_speculative_multiple_decay_pbdecay_252d_jerk_v012_signal,    f27sm_f27_speculative_multiple_decay_pedecay_126d_jerk_v013_signal,    f27sm_f27_speculative_multiple_decay_psdecay_63d_jerk_v014_signal,    f27sm_f27_speculative_multiple_decay_psreldecay_252d_jerk_v015_signal,    f27sm_f27_speculative_multiple_decay_pbreldecay_252d_jerk_v016_signal,    f27sm_f27_speculative_multiple_decay_psreldecay_126d_jerk_v017_signal,    f27sm_f27_speculative_multiple_decay_psz_126d_jerk_v018_signal,    f27sm_f27_speculative_multiple_decay_psz_252d_jerk_v019_signal,    f27sm_f27_speculative_multiple_decay_psz_504d_jerk_v020_signal,    f27sm_f27_speculative_multiple_decay_pbz_126d_jerk_v021_signal,    f27sm_f27_speculative_multiple_decay_pbz_252d_jerk_v022_signal,    f27sm_f27_speculative_multiple_decay_pbz_504d_jerk_v023_signal,    f27sm_f27_speculative_multiple_decay_pez_252d_jerk_v024_signal,    f27sm_f27_speculative_multiple_decay_pez_126d_jerk_v025_signal,    f27sm_f27_speculative_multiple_decay_psrank_252d_jerk_v026_signal,    f27sm_f27_speculative_multiple_decay_psrank_504d_jerk_v027_signal,    f27sm_f27_speculative_multiple_decay_pbrank_252d_jerk_v028_signal,    f27sm_f27_speculative_multiple_decay_pbrank_504d_jerk_v029_signal,    f27sm_f27_speculative_multiple_decay_perank_252d_jerk_v030_signal,    f27sm_f27_speculative_multiple_decay_psrich_252d_jerk_v031_signal,    f27sm_f27_speculative_multiple_decay_pbrich_252d_jerk_v032_signal,    f27sm_f27_speculative_multiple_decay_psrich_126d_jerk_v033_signal,    f27sm_f27_speculative_multiple_decay_logpsrich_252d_jerk_v034_signal,    f27sm_f27_speculative_multiple_decay_logpbrich_252d_jerk_v035_signal,    f27sm_f27_speculative_multiple_decay_psdecayrate_21d_jerk_v036_signal,    f27sm_f27_speculative_multiple_decay_pbdecayrate_21d_jerk_v037_signal,    f27sm_f27_speculative_multiple_decay_psdecayrate_63d_jerk_v038_signal,    f27sm_f27_speculative_multiple_decay_pstrend_63d_jerk_v039_signal,    f27sm_f27_speculative_multiple_decay_pstrend_126d_jerk_v040_signal,    f27sm_f27_speculative_multiple_decay_pbtrend_126d_jerk_v041_signal,    f27sm_f27_speculative_multiple_decay_pspbcross_21d_jerk_v042_signal,    f27sm_f27_speculative_multiple_decay_pspbcross_63d_jerk_v043_signal,    f27sm_f27_speculative_multiple_decay_logpspbcross_21d_jerk_v044_signal,    f27sm_f27_speculative_multiple_decay_pspecross_63d_jerk_v045_signal,    f27sm_f27_speculative_multiple_decay_psdisp_126d_jerk_v046_signal,    f27sm_f27_speculative_multiple_decay_psdisp_252d_jerk_v047_signal,    f27sm_f27_speculative_multiple_decay_pbdisp_252d_jerk_v048_signal,    f27sm_f27_speculative_multiple_decay_pscv_252d_jerk_v049_signal,    f27sm_f27_speculative_multiple_decay_pbcv_252d_jerk_v050_signal,    f27sm_f27_speculative_multiple_decay_pscompress_jerk_v051_signal,    f27sm_f27_speculative_multiple_decay_pbcompress_jerk_v052_signal,    f27sm_f27_speculative_multiple_decay_pszsm_252d_jerk_v053_signal,    f27sm_f27_speculative_multiple_decay_pbzsm_252d_jerk_v054_signal,    f27sm_f27_speculative_multiple_decay_zspread_252d_jerk_v055_signal,    f27sm_f27_speculative_multiple_decay_pszpez_252d_jerk_v056_signal,    f27sm_f27_speculative_multiple_decay_rankspread_252d_jerk_v057_signal,    f27sm_f27_speculative_multiple_decay_psrankchg_63d_jerk_v058_signal,    f27sm_f27_speculative_multiple_decay_pbrankchg_63d_jerk_v059_signal,    f27sm_f27_speculative_multiple_decay_pszchg_21d_jerk_v060_signal,    f27sm_f27_speculative_multiple_decay_pbzchg_21d_jerk_v061_signal,    f27sm_f27_speculative_multiple_decay_pshalflife_21d_jerk_v062_signal,    f27sm_f27_speculative_multiple_decay_pslogdecay_252d_jerk_v063_signal,    f27sm_f27_speculative_multiple_decay_pblogdecay_252d_jerk_v064_signal,    f27sm_f27_speculative_multiple_decay_psewmdecay_63d_jerk_v065_signal,    f27sm_f27_speculative_multiple_decay_pbewmdecay_63d_jerk_v066_signal,    f27sm_f27_speculative_multiple_decay_psrelewm_63d_jerk_v067_signal,    f27sm_f27_speculative_multiple_decay_psdecayz_126d_jerk_v068_signal,    f27sm_f27_speculative_multiple_decay_pbdecayz_126d_jerk_v069_signal,    f27sm_f27_speculative_multiple_decay_psaccel_jerk_v070_signal,    f27sm_f27_speculative_multiple_decay_psskew_252d_jerk_v071_signal,    f27sm_f27_speculative_multiple_decay_pbskew_252d_jerk_v072_signal,    f27sm_f27_speculative_multiple_decay_pskurt_252d_jerk_v073_signal,    f27sm_f27_speculative_multiple_decay_pszratio_252d_jerk_v074_signal,    f27sm_f27_speculative_multiple_decay_psblend_252d_jerk_v075_signal,    f27sm_f27_speculative_multiple_decay_pslvl_126d_jerk_v076_signal,    f27sm_f27_speculative_multiple_decay_pblvl_126d_jerk_v077_signal,    f27sm_f27_speculative_multiple_decay_logpslvl_126d_jerk_v078_signal,    f27sm_f27_speculative_multiple_decay_logpblvl_63d_jerk_v079_signal,    f27sm_f27_speculative_multiple_decay_logpelvl_63d_jerk_v080_signal,    f27sm_f27_speculative_multiple_decay_psdecay_504d_jerk_v081_signal,    f27sm_f27_speculative_multiple_decay_pbdecay_504d_jerk_v082_signal,    f27sm_f27_speculative_multiple_decay_pedecay_252d_jerk_v083_signal,    f27sm_f27_speculative_multiple_decay_psreldecay_504d_jerk_v084_signal,    f27sm_f27_speculative_multiple_decay_pbreldecay_126d_jerk_v085_signal,    f27sm_f27_speculative_multiple_decay_psz_189d_jerk_v086_signal,    f27sm_f27_speculative_multiple_decay_pbz_189d_jerk_v087_signal,    f27sm_f27_speculative_multiple_decay_psz_63d_jerk_v088_signal,    f27sm_f27_speculative_multiple_decay_pbz_63d_jerk_v089_signal,    f27sm_f27_speculative_multiple_decay_pez_504d_jerk_v090_signal,    f27sm_f27_speculative_multiple_decay_psrank_126d_jerk_v091_signal,    f27sm_f27_speculative_multiple_decay_pbrank_126d_jerk_v092_signal,    f27sm_f27_speculative_multiple_decay_perank_504d_jerk_v093_signal,    f27sm_f27_speculative_multiple_decay_psrich_504d_jerk_v094_signal,    f27sm_f27_speculative_multiple_decay_pbrich_126d_jerk_v095_signal,    f27sm_f27_speculative_multiple_decay_logpsrich_126d_jerk_v096_signal,    f27sm_f27_speculative_multiple_decay_logpbrich_504d_jerk_v097_signal,    f27sm_f27_speculative_multiple_decay_psdecayrate_42d_jerk_v098_signal,    f27sm_f27_speculative_multiple_decay_pbdecayrate_63d_jerk_v099_signal,    f27sm_f27_speculative_multiple_decay_psdecayrate_126d_jerk_v100_signal,    f27sm_f27_speculative_multiple_decay_pstrend_252d_jerk_v101_signal,    f27sm_f27_speculative_multiple_decay_pbtrend_63d_jerk_v102_signal,    f27sm_f27_speculative_multiple_decay_petrend_126d_jerk_v103_signal,    f27sm_f27_speculative_multiple_decay_pspbcross_126d_jerk_v104_signal,    f27sm_f27_speculative_multiple_decay_logpspbcross_63d_jerk_v105_signal,    f27sm_f27_speculative_multiple_decay_pbpecross_63d_jerk_v106_signal,    f27sm_f27_speculative_multiple_decay_crossdecay_252d_jerk_v107_signal,    f27sm_f27_speculative_multiple_decay_psdisp_63d_jerk_v108_signal,    f27sm_f27_speculative_multiple_decay_pbdisp_126d_jerk_v109_signal,    f27sm_f27_speculative_multiple_decay_pscv_126d_jerk_v110_signal,    f27sm_f27_speculative_multiple_decay_pbcv_126d_jerk_v111_signal,    f27sm_f27_speculative_multiple_decay_pscompress42_jerk_v112_signal,    f27sm_f27_speculative_multiple_decay_pbcompress42_jerk_v113_signal,    f27sm_f27_speculative_multiple_decay_pszsm_126d_jerk_v114_signal,    f27sm_f27_speculative_multiple_decay_pbzsm_126d_jerk_v115_signal,    f27sm_f27_speculative_multiple_decay_zspread_126d_jerk_v116_signal,    f27sm_f27_speculative_multiple_decay_pbzpez_252d_jerk_v117_signal,    f27sm_f27_speculative_multiple_decay_rankspread_504d_jerk_v118_signal,    f27sm_f27_speculative_multiple_decay_psrankchg_126d_jerk_v119_signal,    f27sm_f27_speculative_multiple_decay_pbrankchg_21d_jerk_v120_signal,    f27sm_f27_speculative_multiple_decay_pszchg_63d_jerk_v121_signal,    f27sm_f27_speculative_multiple_decay_pbzchg_63d_jerk_v122_signal,    f27sm_f27_speculative_multiple_decay_pshalflife_63d_jerk_v123_signal,    f27sm_f27_speculative_multiple_decay_pbhalflife_21d_jerk_v124_signal,    f27sm_f27_speculative_multiple_decay_pslogdecay_126d_jerk_v125_signal,    f27sm_f27_speculative_multiple_decay_pblogdecay_126d_jerk_v126_signal,    f27sm_f27_speculative_multiple_decay_psewmdecay_126d_jerk_v127_signal,    f27sm_f27_speculative_multiple_decay_pbewmdecay_126d_jerk_v128_signal,    f27sm_f27_speculative_multiple_decay_pbrelewm_63d_jerk_v129_signal,    f27sm_f27_speculative_multiple_decay_psdecayz_252d_jerk_v130_signal,    f27sm_f27_speculative_multiple_decay_pbdecayz_252d_jerk_v131_signal,    f27sm_f27_speculative_multiple_decay_pbaccel_jerk_v132_signal,    f27sm_f27_speculative_multiple_decay_psskew_126d_jerk_v133_signal,    f27sm_f27_speculative_multiple_decay_pbkurt_252d_jerk_v134_signal,    f27sm_f27_speculative_multiple_decay_pszterm_jerk_v135_signal,    f27sm_f27_speculative_multiple_decay_pbzterm_jerk_v136_signal,    f27sm_f27_speculative_multiple_decay_psdecayterm_jerk_v137_signal,    f27sm_f27_speculative_multiple_decay_psexcessz_126d_jerk_v138_signal,    f27sm_f27_speculative_multiple_decay_pbexcessz_126d_jerk_v139_signal,    f27sm_f27_speculative_multiple_decay_psslowrich_jerk_v140_signal,    f27sm_f27_speculative_multiple_decay_pbslowrich_jerk_v141_signal,    f27sm_f27_speculative_multiple_decay_psgapdisp_126d_jerk_v142_signal,    f27sm_f27_speculative_multiple_decay_pbgapdisp_126d_jerk_v143_signal,    f27sm_f27_speculative_multiple_decay_psewmz_63d_jerk_v144_signal,    f27sm_f27_speculative_multiple_decay_pbewmz_63d_jerk_v145_signal,    f27sm_f27_speculative_multiple_decay_perich_252d_jerk_v146_signal,    f27sm_f27_speculative_multiple_decay_combz_252d_jerk_v147_signal,    f27sm_f27_speculative_multiple_decay_combrank_252d_jerk_v148_signal,    f27sm_f27_speculative_multiple_decay_combdecay_252d_jerk_v149_signal,    f27sm_f27_speculative_multiple_decay_specblend_252d_jerk_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_SPECULATIVE_MULTIPLE_DECAY_REGISTRY_JERK = REGISTRY

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
    domain_primitives = ('_f27_mult', '_f27_decay', '_f27_multz', '_f27_pctile')
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
    print("OK f27_speculative_multiple_decay_" + "3rd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
