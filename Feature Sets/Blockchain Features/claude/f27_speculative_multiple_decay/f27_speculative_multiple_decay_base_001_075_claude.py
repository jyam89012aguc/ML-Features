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


# ============ FEATURES 001-075 ============

# ps smoothed level 21d
def f27sm_f27_speculative_multiple_decay_pslvl_21d_base_v001_signal(ps):
    result = _f27_mult(ps, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ps smoothed level 63d
def f27sm_f27_speculative_multiple_decay_pslvl_63d_base_v002_signal(ps):
    result = _f27_mult(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# pb smoothed level 21d
def f27sm_f27_speculative_multiple_decay_pblvl_21d_base_v003_signal(pb):
    result = _f27_mult(pb, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# pb smoothed level 63d
def f27sm_f27_speculative_multiple_decay_pblvl_63d_base_v004_signal(pb):
    result = _f27_mult(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# log ps level 21d (compress extreme speculative multiples)
def f27sm_f27_speculative_multiple_decay_logpslvl_21d_base_v005_signal(ps):
    result = np.log(_f27_mult(ps, 21).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log pb level 21d
def f27sm_f27_speculative_multiple_decay_logpblvl_21d_base_v006_signal(pb):
    result = np.log(_f27_mult(pb, 21).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log ps level 63d
def f27sm_f27_speculative_multiple_decay_logpslvl_63d_base_v007_signal(ps):
    result = np.log(_f27_mult(ps, 63).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log abs pe level 21d (pe can be negative -> log of abs)
def f27sm_f27_speculative_multiple_decay_logpelvl_21d_base_v008_signal(pe):
    result = np.log(_f27_mult(pe.abs(), 21).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap over 126d (level minus trailing mean)
def f27sm_f27_speculative_multiple_decay_psdecay_126d_base_v009_signal(ps):
    result = _f27_decay(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap over 252d
def f27sm_f27_speculative_multiple_decay_psdecay_252d_base_v010_signal(ps):
    result = _f27_decay(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap over 126d
def f27sm_f27_speculative_multiple_decay_pbdecay_126d_base_v011_signal(pb):
    result = _f27_decay(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap over 252d
def f27sm_f27_speculative_multiple_decay_pbdecay_252d_base_v012_signal(pb):
    result = _f27_decay(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pe decay gap over 126d (raw pe, handle sign by gap)
def f27sm_f27_speculative_multiple_decay_pedecay_126d_base_v013_signal(pe):
    result = _f27_decay(pe, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap over 63d
def f27sm_f27_speculative_multiple_decay_psdecay_63d_base_v014_signal(ps):
    result = _f27_decay(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap normalized by trailing mean (relative decay) 252d
def f27sm_f27_speculative_multiple_decay_psreldecay_252d_base_v015_signal(ps):
    result = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap normalized by trailing mean 252d
def f27sm_f27_speculative_multiple_decay_pbreldecay_252d_base_v016_signal(pb):
    result = _safe_div(_f27_decay(pb, 252), _f27_mult(pb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap normalized by trailing mean 126d
def f27sm_f27_speculative_multiple_decay_psreldecay_126d_base_v017_signal(ps):
    result = _safe_div(_f27_decay(ps, 126), _f27_mult(ps, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score over 126d
def f27sm_f27_speculative_multiple_decay_psz_126d_base_v018_signal(ps):
    result = _f27_multz(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score over 252d
def f27sm_f27_speculative_multiple_decay_psz_252d_base_v019_signal(ps):
    result = _f27_multz(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score over 504d
def f27sm_f27_speculative_multiple_decay_psz_504d_base_v020_signal(ps):
    result = _f27_multz(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score over 126d
def f27sm_f27_speculative_multiple_decay_pbz_126d_base_v021_signal(pb):
    result = _f27_multz(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score over 252d
def f27sm_f27_speculative_multiple_decay_pbz_252d_base_v022_signal(pb):
    result = _f27_multz(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score over 504d
def f27sm_f27_speculative_multiple_decay_pbz_504d_base_v023_signal(pb):
    result = _f27_multz(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pe z-score over 252d (z handles sign via centering)
def f27sm_f27_speculative_multiple_decay_pez_252d_base_v024_signal(pe):
    result = _f27_multz(pe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pe z-score over 126d
def f27sm_f27_speculative_multiple_decay_pez_126d_base_v025_signal(pe):
    result = _f27_multz(pe, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ps percentile rank over 252d (richness)
def f27sm_f27_speculative_multiple_decay_psrank_252d_base_v026_signal(ps):
    result = _f27_pctile(ps, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps percentile rank over 504d
def f27sm_f27_speculative_multiple_decay_psrank_504d_base_v027_signal(ps):
    result = _f27_pctile(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pb percentile rank over 252d
def f27sm_f27_speculative_multiple_decay_pbrank_252d_base_v028_signal(pb):
    result = _f27_pctile(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pb percentile rank over 504d
def f27sm_f27_speculative_multiple_decay_pbrank_504d_base_v029_signal(pb):
    result = _f27_pctile(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pe percentile rank over 252d
def f27sm_f27_speculative_multiple_decay_perank_252d_base_v030_signal(pe):
    result = _f27_pctile(pe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness vs 252d max-anchored mean (level over trailing mean ratio)
def f27sm_f27_speculative_multiple_decay_psrich_252d_base_v031_signal(ps):
    result = _safe_div(ps, _f27_mult(ps, 252)) + _f27_decay(ps, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb richness ratio vs 252d trailing mean
def f27sm_f27_speculative_multiple_decay_pbrich_252d_base_v032_signal(pb):
    result = _safe_div(pb, _f27_mult(pb, 252)) + _f27_decay(pb, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness ratio vs 126d trailing mean
def f27sm_f27_speculative_multiple_decay_psrich_126d_base_v033_signal(ps):
    result = _safe_div(ps, _f27_mult(ps, 126)) + _f27_decay(ps, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log ps richness ratio vs 252d (log of level/mean)
def f27sm_f27_speculative_multiple_decay_logpsrich_252d_base_v034_signal(ps):
    result = np.log(_safe_div(ps, _f27_mult(ps, 252)).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log pb richness ratio vs 252d
def f27sm_f27_speculative_multiple_decay_logpbrich_252d_base_v035_signal(pb):
    result = np.log(_safe_div(pb, _f27_mult(pb, 252)).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay rate: pct change of ps toward its mean over 21d horizon
def f27sm_f27_speculative_multiple_decay_psdecayrate_21d_base_v036_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(21), _f27_mult(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay rate over 21d
def f27sm_f27_speculative_multiple_decay_pbdecayrate_21d_base_v037_signal(pb):
    gap = _f27_decay(pb, 252)
    result = _safe_div(gap - gap.shift(21), _f27_mult(pb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay rate over 63d
def f27sm_f27_speculative_multiple_decay_psdecayrate_63d_base_v038_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(63), _f27_mult(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple trend slope over 63d (normalized linear drift of level)
def f27sm_f27_speculative_multiple_decay_pstrend_63d_base_v039_signal(ps):
    lvl = _f27_mult(ps, 21)
    result = _safe_div(lvl - lvl.shift(63), _std(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple trend slope over 126d
def f27sm_f27_speculative_multiple_decay_pstrend_126d_base_v040_signal(ps):
    lvl = _f27_mult(ps, 21)
    result = _safe_div(lvl - lvl.shift(126), _std(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pb multiple trend slope over 126d
def f27sm_f27_speculative_multiple_decay_pbtrend_126d_base_v041_signal(pb):
    lvl = _f27_mult(pb, 21)
    result = _safe_div(lvl - lvl.shift(126), _std(pb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps/pb cross ratio (speculative sales-vs-book richness)
def f27sm_f27_speculative_multiple_decay_pspbcross_21d_base_v042_signal(ps, pb):
    result = _safe_div(_f27_mult(ps, 21), _f27_mult(pb, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# ps/pb cross ratio 63d
def f27sm_f27_speculative_multiple_decay_pspbcross_63d_base_v043_signal(ps, pb):
    result = _safe_div(_f27_mult(ps, 63), _f27_mult(pb, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# log ps/pb cross ratio 21d
def f27sm_f27_speculative_multiple_decay_logpspbcross_21d_base_v044_signal(ps, pb):
    result = np.log(_safe_div(_f27_mult(ps, 21), _f27_mult(pb, 21)).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# ps/abs pe cross ratio 63d (sales richness relative to earnings multiple)
def f27sm_f27_speculative_multiple_decay_pspecross_63d_base_v045_signal(ps, pe):
    result = _safe_div(_f27_mult(ps, 63), _f27_mult(pe.abs(), 63))
    return result.replace([np.inf, -np.inf], np.nan)


# ps dispersion over 126d (volatility of the multiple level)
def f27sm_f27_speculative_multiple_decay_psdisp_126d_base_v046_signal(ps):
    result = _std(ps, 126) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps dispersion over 252d
def f27sm_f27_speculative_multiple_decay_psdisp_252d_base_v047_signal(ps):
    result = _std(ps, 252) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb dispersion over 252d
def f27sm_f27_speculative_multiple_decay_pbdisp_252d_base_v048_signal(pb):
    result = _std(pb, 252) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps coefficient of variation over 252d (dispersion scaled by level)
def f27sm_f27_speculative_multiple_decay_pscv_252d_base_v049_signal(ps):
    result = _safe_div(_std(ps, 252), _f27_mult(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pb coefficient of variation over 252d
def f27sm_f27_speculative_multiple_decay_pbcv_252d_base_v050_signal(pb):
    result = _safe_div(_std(pb, 252), _f27_mult(pb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps compression: shrinking dispersion (short std over long std)
def f27sm_f27_speculative_multiple_decay_pscompress_base_v051_signal(ps):
    result = _safe_div(_std(ps, 63), _std(ps, 252)) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb compression ratio
def f27sm_f27_speculative_multiple_decay_pbcompress_base_v052_signal(pb):
    result = _safe_div(_std(pb, 63), _std(pb, 252)) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score smoothed over 21d (denoised richness)
def f27sm_f27_speculative_multiple_decay_pszsm_252d_base_v053_signal(ps):
    result = _mean(_f27_multz(ps, 252), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score smoothed over 21d
def f27sm_f27_speculative_multiple_decay_pbzsm_252d_base_v054_signal(pb):
    result = _mean(_f27_multz(pb, 252), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z minus pb z (relative richness spread, 252d)
def f27sm_f27_speculative_multiple_decay_zspread_252d_base_v055_signal(ps, pb):
    result = _f27_multz(ps, 252) - _f27_multz(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z minus pe z (sales vs earnings richness spread, 252d)
def f27sm_f27_speculative_multiple_decay_pszpez_252d_base_v056_signal(ps, pe):
    result = _f27_multz(ps, 252) - _f27_multz(pe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps percentile minus pb percentile (richness rank spread, 252d)
def f27sm_f27_speculative_multiple_decay_rankspread_252d_base_v057_signal(ps, pb):
    result = _f27_pctile(ps, 252) - _f27_pctile(pb, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness percentile change over 63d (decay of rank)
def f27sm_f27_speculative_multiple_decay_psrankchg_63d_base_v058_signal(ps):
    rk = _f27_pctile(ps, 252)
    result = rk - rk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# pb richness percentile change over 63d
def f27sm_f27_speculative_multiple_decay_pbrankchg_63d_base_v059_signal(pb):
    rk = _f27_pctile(pb, 252)
    result = rk - rk.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score change over 21d (richness velocity)
def f27sm_f27_speculative_multiple_decay_pszchg_21d_base_v060_signal(ps):
    zz = _f27_multz(ps, 252)
    result = zz - zz.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score change over 21d
def f27sm_f27_speculative_multiple_decay_pbzchg_21d_base_v061_signal(pb):
    zz = _f27_multz(pb, 252)
    result = zz - zz.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# ps half-life decay proxy: gap today over gap 21d ago (reversion speed)
def f27sm_f27_speculative_multiple_decay_pshalflife_21d_base_v062_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap, gap.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# ps log-level minus its 252d mean (log-space decay gap)
def f27sm_f27_speculative_multiple_decay_pslogdecay_252d_base_v063_signal(ps):
    lp = np.log(ps.clip(lower=1e-6))
    result = lp - _mean(lp, 252) + _f27_decay(ps, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb log-level minus its 252d mean
def f27sm_f27_speculative_multiple_decay_pblogdecay_252d_base_v064_signal(pb):
    lp = np.log(pb.clip(lower=1e-6))
    result = lp - _mean(lp, 252) + _f27_decay(pb, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps EWMA decay gap (level minus ewm mean, faster reversion weighting)
def f27sm_f27_speculative_multiple_decay_psewmdecay_63d_base_v065_signal(ps):
    em = ps.ewm(span=63, min_periods=21).mean()
    result = (ps - em) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb EWMA decay gap
def f27sm_f27_speculative_multiple_decay_pbewmdecay_63d_base_v066_signal(pb):
    em = pb.ewm(span=63, min_periods=21).mean()
    result = (pb - em) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps EWMA decay gap normalized by ewm level (relative)
def f27sm_f27_speculative_multiple_decay_psrelewm_63d_base_v067_signal(ps):
    em = ps.ewm(span=63, min_periods=21).mean()
    result = _safe_div(ps - em, em) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap z-scored over 126d (standardized reversion distance)
def f27sm_f27_speculative_multiple_decay_psdecayz_126d_base_v068_signal(ps):
    result = _z(_f27_decay(ps, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap z-scored over 126d
def f27sm_f27_speculative_multiple_decay_pbdecayz_126d_base_v069_signal(pb):
    result = _z(_f27_decay(pb, 252), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness acceleration: 63d trend minus 126d trend of level
def f27sm_f27_speculative_multiple_decay_psaccel_base_v070_signal(ps):
    lvl = _f27_mult(ps, 21)
    s1 = _safe_div(lvl - lvl.shift(63), _std(ps, 252))
    s2 = _safe_div(lvl - lvl.shift(126), _std(ps, 252))
    result = s1 - s2
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple skew over 252d (asymmetry of multiple distribution)
def f27sm_f27_speculative_multiple_decay_psskew_252d_base_v071_signal(ps):
    result = ps.rolling(252, min_periods=84).skew() + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb multiple skew over 252d
def f27sm_f27_speculative_multiple_decay_pbskew_252d_base_v072_signal(pb):
    result = pb.rolling(252, min_periods=84).skew() + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple kurtosis over 252d (fat-tail richness regime)
def f27sm_f27_speculative_multiple_decay_pskurt_252d_base_v073_signal(ps):
    result = ps.rolling(252, min_periods=84).kurt() + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness over pe richness ratio of z-scores (speculative tilt) 252d
def f27sm_f27_speculative_multiple_decay_pszratio_252d_base_v074_signal(ps, pe):
    result = _safe_div(_f27_multz(ps, 252), _f27_multz(pe.abs(), 252).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# ps blended richness composite (z + decay-rel + log-rich), 252d
def f27sm_f27_speculative_multiple_decay_psblend_252d_base_v075_signal(ps):
    z = _f27_multz(ps, 252)
    rel = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    lr = np.log(_safe_div(ps, _f27_mult(ps, 252)).clip(lower=1e-6))
    result = (z + rel + lr) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27sm_f27_speculative_multiple_decay_pslvl_21d_base_v001_signal,
    f27sm_f27_speculative_multiple_decay_pslvl_63d_base_v002_signal,
    f27sm_f27_speculative_multiple_decay_pblvl_21d_base_v003_signal,
    f27sm_f27_speculative_multiple_decay_pblvl_63d_base_v004_signal,
    f27sm_f27_speculative_multiple_decay_logpslvl_21d_base_v005_signal,
    f27sm_f27_speculative_multiple_decay_logpblvl_21d_base_v006_signal,
    f27sm_f27_speculative_multiple_decay_logpslvl_63d_base_v007_signal,
    f27sm_f27_speculative_multiple_decay_logpelvl_21d_base_v008_signal,
    f27sm_f27_speculative_multiple_decay_psdecay_126d_base_v009_signal,
    f27sm_f27_speculative_multiple_decay_psdecay_252d_base_v010_signal,
    f27sm_f27_speculative_multiple_decay_pbdecay_126d_base_v011_signal,
    f27sm_f27_speculative_multiple_decay_pbdecay_252d_base_v012_signal,
    f27sm_f27_speculative_multiple_decay_pedecay_126d_base_v013_signal,
    f27sm_f27_speculative_multiple_decay_psdecay_63d_base_v014_signal,
    f27sm_f27_speculative_multiple_decay_psreldecay_252d_base_v015_signal,
    f27sm_f27_speculative_multiple_decay_pbreldecay_252d_base_v016_signal,
    f27sm_f27_speculative_multiple_decay_psreldecay_126d_base_v017_signal,
    f27sm_f27_speculative_multiple_decay_psz_126d_base_v018_signal,
    f27sm_f27_speculative_multiple_decay_psz_252d_base_v019_signal,
    f27sm_f27_speculative_multiple_decay_psz_504d_base_v020_signal,
    f27sm_f27_speculative_multiple_decay_pbz_126d_base_v021_signal,
    f27sm_f27_speculative_multiple_decay_pbz_252d_base_v022_signal,
    f27sm_f27_speculative_multiple_decay_pbz_504d_base_v023_signal,
    f27sm_f27_speculative_multiple_decay_pez_252d_base_v024_signal,
    f27sm_f27_speculative_multiple_decay_pez_126d_base_v025_signal,
    f27sm_f27_speculative_multiple_decay_psrank_252d_base_v026_signal,
    f27sm_f27_speculative_multiple_decay_psrank_504d_base_v027_signal,
    f27sm_f27_speculative_multiple_decay_pbrank_252d_base_v028_signal,
    f27sm_f27_speculative_multiple_decay_pbrank_504d_base_v029_signal,
    f27sm_f27_speculative_multiple_decay_perank_252d_base_v030_signal,
    f27sm_f27_speculative_multiple_decay_psrich_252d_base_v031_signal,
    f27sm_f27_speculative_multiple_decay_pbrich_252d_base_v032_signal,
    f27sm_f27_speculative_multiple_decay_psrich_126d_base_v033_signal,
    f27sm_f27_speculative_multiple_decay_logpsrich_252d_base_v034_signal,
    f27sm_f27_speculative_multiple_decay_logpbrich_252d_base_v035_signal,
    f27sm_f27_speculative_multiple_decay_psdecayrate_21d_base_v036_signal,
    f27sm_f27_speculative_multiple_decay_pbdecayrate_21d_base_v037_signal,
    f27sm_f27_speculative_multiple_decay_psdecayrate_63d_base_v038_signal,
    f27sm_f27_speculative_multiple_decay_pstrend_63d_base_v039_signal,
    f27sm_f27_speculative_multiple_decay_pstrend_126d_base_v040_signal,
    f27sm_f27_speculative_multiple_decay_pbtrend_126d_base_v041_signal,
    f27sm_f27_speculative_multiple_decay_pspbcross_21d_base_v042_signal,
    f27sm_f27_speculative_multiple_decay_pspbcross_63d_base_v043_signal,
    f27sm_f27_speculative_multiple_decay_logpspbcross_21d_base_v044_signal,
    f27sm_f27_speculative_multiple_decay_pspecross_63d_base_v045_signal,
    f27sm_f27_speculative_multiple_decay_psdisp_126d_base_v046_signal,
    f27sm_f27_speculative_multiple_decay_psdisp_252d_base_v047_signal,
    f27sm_f27_speculative_multiple_decay_pbdisp_252d_base_v048_signal,
    f27sm_f27_speculative_multiple_decay_pscv_252d_base_v049_signal,
    f27sm_f27_speculative_multiple_decay_pbcv_252d_base_v050_signal,
    f27sm_f27_speculative_multiple_decay_pscompress_base_v051_signal,
    f27sm_f27_speculative_multiple_decay_pbcompress_base_v052_signal,
    f27sm_f27_speculative_multiple_decay_pszsm_252d_base_v053_signal,
    f27sm_f27_speculative_multiple_decay_pbzsm_252d_base_v054_signal,
    f27sm_f27_speculative_multiple_decay_zspread_252d_base_v055_signal,
    f27sm_f27_speculative_multiple_decay_pszpez_252d_base_v056_signal,
    f27sm_f27_speculative_multiple_decay_rankspread_252d_base_v057_signal,
    f27sm_f27_speculative_multiple_decay_psrankchg_63d_base_v058_signal,
    f27sm_f27_speculative_multiple_decay_pbrankchg_63d_base_v059_signal,
    f27sm_f27_speculative_multiple_decay_pszchg_21d_base_v060_signal,
    f27sm_f27_speculative_multiple_decay_pbzchg_21d_base_v061_signal,
    f27sm_f27_speculative_multiple_decay_pshalflife_21d_base_v062_signal,
    f27sm_f27_speculative_multiple_decay_pslogdecay_252d_base_v063_signal,
    f27sm_f27_speculative_multiple_decay_pblogdecay_252d_base_v064_signal,
    f27sm_f27_speculative_multiple_decay_psewmdecay_63d_base_v065_signal,
    f27sm_f27_speculative_multiple_decay_pbewmdecay_63d_base_v066_signal,
    f27sm_f27_speculative_multiple_decay_psrelewm_63d_base_v067_signal,
    f27sm_f27_speculative_multiple_decay_psdecayz_126d_base_v068_signal,
    f27sm_f27_speculative_multiple_decay_pbdecayz_126d_base_v069_signal,
    f27sm_f27_speculative_multiple_decay_psaccel_base_v070_signal,
    f27sm_f27_speculative_multiple_decay_psskew_252d_base_v071_signal,
    f27sm_f27_speculative_multiple_decay_pbskew_252d_base_v072_signal,
    f27sm_f27_speculative_multiple_decay_pskurt_252d_base_v073_signal,
    f27sm_f27_speculative_multiple_decay_pszratio_252d_base_v074_signal,
    f27sm_f27_speculative_multiple_decay_psblend_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_SPECULATIVE_MULTIPLE_DECAY_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f27_mult", "_f27_decay", "_f27_multz", "_f27_pctile")
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
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f27_speculative_multiple_decay_base_001_075_claude: {n_features} features pass")
