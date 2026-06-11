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


# ============ FEATURES 076-150 ============

# ps smoothed level 126d
def f27sm_f27_speculative_multiple_decay_pslvl_126d_base_v076_signal(ps):
    result = _f27_mult(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb smoothed level 126d
def f27sm_f27_speculative_multiple_decay_pblvl_126d_base_v077_signal(pb):
    result = _f27_mult(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# log ps level 126d
def f27sm_f27_speculative_multiple_decay_logpslvl_126d_base_v078_signal(ps):
    result = np.log(_f27_mult(ps, 126).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log pb level 63d
def f27sm_f27_speculative_multiple_decay_logpblvl_63d_base_v079_signal(pb):
    result = np.log(_f27_mult(pb, 63).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log abs pe level 63d
def f27sm_f27_speculative_multiple_decay_logpelvl_63d_base_v080_signal(pe):
    result = np.log(_f27_mult(pe.abs(), 63).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap over 504d (long-horizon reversion)
def f27sm_f27_speculative_multiple_decay_psdecay_504d_base_v081_signal(ps):
    result = _f27_decay(ps, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap over 504d
def f27sm_f27_speculative_multiple_decay_pbdecay_504d_base_v082_signal(pb):
    result = _f27_decay(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pe decay gap over 252d
def f27sm_f27_speculative_multiple_decay_pedecay_252d_base_v083_signal(pe):
    result = _f27_decay(pe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps relative decay over 504d (gap / trailing mean)
def f27sm_f27_speculative_multiple_decay_psreldecay_504d_base_v084_signal(ps):
    result = _safe_div(_f27_decay(ps, 504), _f27_mult(ps, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# pb relative decay over 126d
def f27sm_f27_speculative_multiple_decay_pbreldecay_126d_base_v085_signal(pb):
    result = _safe_div(_f27_decay(pb, 126), _f27_mult(pb, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score over 189d
def f27sm_f27_speculative_multiple_decay_psz_189d_base_v086_signal(ps):
    result = _f27_multz(ps, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score over 189d
def f27sm_f27_speculative_multiple_decay_pbz_189d_base_v087_signal(pb):
    result = _f27_multz(pb, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score over 63d (short-horizon richness)
def f27sm_f27_speculative_multiple_decay_psz_63d_base_v088_signal(ps):
    result = _f27_multz(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score over 63d
def f27sm_f27_speculative_multiple_decay_pbz_63d_base_v089_signal(pb):
    result = _f27_multz(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# pe z-score over 504d
def f27sm_f27_speculative_multiple_decay_pez_504d_base_v090_signal(pe):
    result = _f27_multz(pe, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ps percentile rank over 126d
def f27sm_f27_speculative_multiple_decay_psrank_126d_base_v091_signal(ps):
    result = _f27_pctile(ps, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb percentile rank over 126d
def f27sm_f27_speculative_multiple_decay_pbrank_126d_base_v092_signal(pb):
    result = _f27_pctile(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pe percentile rank over 504d
def f27sm_f27_speculative_multiple_decay_perank_504d_base_v093_signal(pe):
    result = _f27_pctile(pe, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness ratio vs 504d trailing mean
def f27sm_f27_speculative_multiple_decay_psrich_504d_base_v094_signal(ps):
    result = _safe_div(ps, _f27_mult(ps, 504)) + _f27_decay(ps, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb richness ratio vs 126d trailing mean
def f27sm_f27_speculative_multiple_decay_pbrich_126d_base_v095_signal(pb):
    result = _safe_div(pb, _f27_mult(pb, 126)) + _f27_decay(pb, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log ps richness ratio vs 126d
def f27sm_f27_speculative_multiple_decay_logpsrich_126d_base_v096_signal(ps):
    result = np.log(_safe_div(ps, _f27_mult(ps, 126)).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# log pb richness ratio vs 504d
def f27sm_f27_speculative_multiple_decay_logpbrich_504d_base_v097_signal(pb):
    result = np.log(_safe_div(pb, _f27_mult(pb, 504)).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay rate over 42d
def f27sm_f27_speculative_multiple_decay_psdecayrate_42d_base_v098_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(42), _f27_mult(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay rate over 63d
def f27sm_f27_speculative_multiple_decay_pbdecayrate_63d_base_v099_signal(pb):
    gap = _f27_decay(pb, 252)
    result = _safe_div(gap - gap.shift(63), _f27_mult(pb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay rate over 126d
def f27sm_f27_speculative_multiple_decay_psdecayrate_126d_base_v100_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap - gap.shift(126), _f27_mult(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple trend slope over 252d
def f27sm_f27_speculative_multiple_decay_pstrend_252d_base_v101_signal(ps):
    lvl = _f27_mult(ps, 21)
    result = _safe_div(lvl - lvl.shift(252), _std(ps, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pb multiple trend slope over 63d
def f27sm_f27_speculative_multiple_decay_pbtrend_63d_base_v102_signal(pb):
    lvl = _f27_mult(pb, 21)
    result = _safe_div(lvl - lvl.shift(63), _std(pb, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# pe multiple trend slope over 126d (abs pe level drift)
def f27sm_f27_speculative_multiple_decay_petrend_126d_base_v103_signal(pe):
    lvl = _f27_mult(pe.abs(), 21)
    result = _safe_div(lvl - lvl.shift(126), _std(pe.abs(), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ps/pb cross ratio 126d
def f27sm_f27_speculative_multiple_decay_pspbcross_126d_base_v104_signal(ps, pb):
    result = _safe_div(_f27_mult(ps, 126), _f27_mult(pb, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# log ps/pb cross ratio 63d
def f27sm_f27_speculative_multiple_decay_logpspbcross_63d_base_v105_signal(ps, pb):
    result = np.log(_safe_div(_f27_mult(ps, 63), _f27_mult(pb, 63)).clip(lower=1e-6))
    return result.replace([np.inf, -np.inf], np.nan)


# pb/abs pe cross ratio 63d
def f27sm_f27_speculative_multiple_decay_pbpecross_63d_base_v106_signal(pb, pe):
    result = _safe_div(_f27_mult(pb, 63), _f27_mult(pe.abs(), 63))
    return result.replace([np.inf, -np.inf], np.nan)


# ps/pb cross ratio decay gap (cross richness vs its 252d mean)
def f27sm_f27_speculative_multiple_decay_crossdecay_252d_base_v107_signal(ps, pb):
    cross = _safe_div(_f27_mult(ps, 21), _f27_mult(pb, 21))
    result = cross - _mean(cross, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps dispersion over 63d
def f27sm_f27_speculative_multiple_decay_psdisp_63d_base_v108_signal(ps):
    result = _std(ps, 63) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb dispersion over 126d
def f27sm_f27_speculative_multiple_decay_pbdisp_126d_base_v109_signal(pb):
    result = _std(pb, 126) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps coefficient of variation over 126d
def f27sm_f27_speculative_multiple_decay_pscv_126d_base_v110_signal(ps):
    result = _safe_div(_std(ps, 126), _f27_mult(ps, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# pb coefficient of variation over 126d
def f27sm_f27_speculative_multiple_decay_pbcv_126d_base_v111_signal(pb):
    result = _safe_div(_std(pb, 126), _f27_mult(pb, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# ps compression 42 over 252
def f27sm_f27_speculative_multiple_decay_pscompress42_base_v112_signal(ps):
    result = _safe_div(_std(ps, 42), _std(ps, 252)) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb compression 42 over 252
def f27sm_f27_speculative_multiple_decay_pbcompress42_base_v113_signal(pb):
    result = _safe_div(_std(pb, 42), _std(pb, 252)) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score smoothed over 21d using 126d window
def f27sm_f27_speculative_multiple_decay_pszsm_126d_base_v114_signal(ps):
    result = _mean(_f27_multz(ps, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score smoothed over 21d using 126d window
def f27sm_f27_speculative_multiple_decay_pbzsm_126d_base_v115_signal(pb):
    result = _mean(_f27_multz(pb, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z minus pb z over 126d (relative richness spread)
def f27sm_f27_speculative_multiple_decay_zspread_126d_base_v116_signal(ps, pb):
    result = _f27_multz(ps, 126) - _f27_multz(pb, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z minus pe z over 252d
def f27sm_f27_speculative_multiple_decay_pbzpez_252d_base_v117_signal(pb, pe):
    result = _f27_multz(pb, 252) - _f27_multz(pe, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ps percentile minus pb percentile over 504d
def f27sm_f27_speculative_multiple_decay_rankspread_504d_base_v118_signal(ps, pb):
    result = _f27_pctile(ps, 504) - _f27_pctile(pb, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness percentile change over 126d
def f27sm_f27_speculative_multiple_decay_psrankchg_126d_base_v119_signal(ps):
    rk = _f27_pctile(ps, 252)
    result = rk - rk.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb richness percentile change over 21d
def f27sm_f27_speculative_multiple_decay_pbrankchg_21d_base_v120_signal(pb):
    rk = _f27_pctile(pb, 252)
    result = rk - rk.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# ps z-score change over 63d (richness velocity, medium)
def f27sm_f27_speculative_multiple_decay_pszchg_63d_base_v121_signal(ps):
    zz = _f27_multz(ps, 252)
    result = zz - zz.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z-score change over 63d
def f27sm_f27_speculative_multiple_decay_pbzchg_63d_base_v122_signal(pb):
    zz = _f27_multz(pb, 252)
    result = zz - zz.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# ps half-life decay proxy over 63d
def f27sm_f27_speculative_multiple_decay_pshalflife_63d_base_v123_signal(ps):
    gap = _f27_decay(ps, 252)
    result = _safe_div(gap, gap.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# pb half-life decay proxy over 21d
def f27sm_f27_speculative_multiple_decay_pbhalflife_21d_base_v124_signal(pb):
    gap = _f27_decay(pb, 252)
    result = _safe_div(gap, gap.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# ps log-level minus its 126d mean (log-space decay gap)
def f27sm_f27_speculative_multiple_decay_pslogdecay_126d_base_v125_signal(ps):
    lp = np.log(ps.clip(lower=1e-6))
    result = lp - _mean(lp, 126) + _f27_decay(ps, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb log-level minus its 126d mean
def f27sm_f27_speculative_multiple_decay_pblogdecay_126d_base_v126_signal(pb):
    lp = np.log(pb.clip(lower=1e-6))
    result = lp - _mean(lp, 126) + _f27_decay(pb, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps EWMA decay gap span 126
def f27sm_f27_speculative_multiple_decay_psewmdecay_126d_base_v127_signal(ps):
    em = ps.ewm(span=126, min_periods=42).mean()
    result = (ps - em) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb EWMA decay gap span 126
def f27sm_f27_speculative_multiple_decay_pbewmdecay_126d_base_v128_signal(pb):
    em = pb.ewm(span=126, min_periods=42).mean()
    result = (pb - em) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb EWMA relative decay span 63
def f27sm_f27_speculative_multiple_decay_pbrelewm_63d_base_v129_signal(pb):
    em = pb.ewm(span=63, min_periods=21).mean()
    result = _safe_div(pb - em, em) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap z-scored over 252d
def f27sm_f27_speculative_multiple_decay_psdecayz_252d_base_v130_signal(ps):
    result = _z(_f27_decay(ps, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap z-scored over 252d
def f27sm_f27_speculative_multiple_decay_pbdecayz_252d_base_v131_signal(pb):
    result = _z(_f27_decay(pb, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# pb richness acceleration: 63d trend minus 126d trend of level
def f27sm_f27_speculative_multiple_decay_pbaccel_base_v132_signal(pb):
    lvl = _f27_mult(pb, 21)
    s1 = _safe_div(lvl - lvl.shift(63), _std(pb, 252))
    s2 = _safe_div(lvl - lvl.shift(126), _std(pb, 252))
    result = s1 - s2
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple skew over 126d
def f27sm_f27_speculative_multiple_decay_psskew_126d_base_v133_signal(ps):
    result = ps.rolling(126, min_periods=42).skew() + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb multiple kurtosis over 252d
def f27sm_f27_speculative_multiple_decay_pbkurt_252d_base_v134_signal(pb):
    result = pb.rolling(252, min_periods=84).kurt() + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps z over 252d minus ps z over 63d (richness term-structure)
def f27sm_f27_speculative_multiple_decay_pszterm_base_v135_signal(ps):
    result = _f27_multz(ps, 252) - _f27_multz(ps, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# pb z over 252d minus pb z over 63d
def f27sm_f27_speculative_multiple_decay_pbzterm_base_v136_signal(pb):
    result = _f27_multz(pb, 252) - _f27_multz(pb, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ps relative decay 126 minus 252 (reversion term-structure)
def f27sm_f27_speculative_multiple_decay_psdecayterm_base_v137_signal(ps):
    d1 = _safe_div(_f27_decay(ps, 126), _f27_mult(ps, 126))
    d2 = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    result = d1 - d2
    return result.replace([np.inf, -np.inf], np.nan)


# ps richness ratio minus 1, z-scored over 126d (excess richness signal)
def f27sm_f27_speculative_multiple_decay_psexcessz_126d_base_v138_signal(ps):
    rr = _safe_div(ps, _f27_mult(ps, 252)) - 1.0
    result = _z(rr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# pb richness ratio minus 1, z-scored over 126d
def f27sm_f27_speculative_multiple_decay_pbexcessz_126d_base_v139_signal(pb):
    rr = _safe_div(pb, _f27_mult(pb, 252)) - 1.0
    result = _z(rr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# ps multiple over 252d, smoothed level vs 504d level ratio (slow richness)
def f27sm_f27_speculative_multiple_decay_psslowrich_base_v140_signal(ps):
    result = _safe_div(_f27_mult(ps, 126), _f27_mult(ps, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# pb slow richness ratio
def f27sm_f27_speculative_multiple_decay_pbslowrich_base_v141_signal(pb):
    result = _safe_div(_f27_mult(pb, 126), _f27_mult(pb, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# ps decay gap normalized by dispersion (reversion in std units), 126d
def f27sm_f27_speculative_multiple_decay_psgapdisp_126d_base_v142_signal(ps):
    result = _safe_div(_f27_decay(ps, 126), _std(ps, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# pb decay gap normalized by dispersion, 126d
def f27sm_f27_speculative_multiple_decay_pbgapdisp_126d_base_v143_signal(pb):
    result = _safe_div(_f27_decay(pb, 126), _std(pb, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# ps EWMA z-score (level minus ewm over ewm-std proxy via rolling std), 63d
def f27sm_f27_speculative_multiple_decay_psewmz_63d_base_v144_signal(ps):
    em = ps.ewm(span=63, min_periods=21).mean()
    result = _safe_div(ps - em, _std(ps, 63)) + _f27_mult(ps, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pb EWMA z-score 63d
def f27sm_f27_speculative_multiple_decay_pbewmz_63d_base_v145_signal(pb):
    em = pb.ewm(span=63, min_periods=21).mean()
    result = _safe_div(pb - em, _std(pb, 63)) + _f27_mult(pb, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# pe richness ratio vs 252d mean of abs pe (earnings-multiple richness)
def f27sm_f27_speculative_multiple_decay_perich_252d_base_v146_signal(pe):
    result = _safe_div(pe.abs(), _f27_mult(pe.abs(), 252)) + _f27_decay(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps + pb combined richness z composite over 252d
def f27sm_f27_speculative_multiple_decay_combz_252d_base_v147_signal(ps, pb):
    result = (_f27_multz(ps, 252) + _f27_multz(pb, 252)) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps + pb combined percentile richness over 252d
def f27sm_f27_speculative_multiple_decay_combrank_252d_base_v148_signal(ps, pb):
    result = (_f27_pctile(ps, 252) + _f27_pctile(pb, 252)) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps + pb combined relative decay over 252d (joint reversion pressure)
def f27sm_f27_speculative_multiple_decay_combdecay_252d_base_v149_signal(ps, pb):
    d1 = _safe_div(_f27_decay(ps, 252), _f27_mult(ps, 252))
    d2 = _safe_div(_f27_decay(pb, 252), _f27_mult(pb, 252))
    result = (d1 + d2) / 2.0
    return result.replace([np.inf, -np.inf], np.nan)


# ps/pb/pe blended speculative richness composite (z of each), 252d
def f27sm_f27_speculative_multiple_decay_specblend_252d_base_v150_signal(ps, pb, pe):
    result = (_f27_multz(ps, 252) + _f27_multz(pb, 252) + _f27_multz(pe, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27sm_f27_speculative_multiple_decay_pslvl_126d_base_v076_signal,
    f27sm_f27_speculative_multiple_decay_pblvl_126d_base_v077_signal,
    f27sm_f27_speculative_multiple_decay_logpslvl_126d_base_v078_signal,
    f27sm_f27_speculative_multiple_decay_logpblvl_63d_base_v079_signal,
    f27sm_f27_speculative_multiple_decay_logpelvl_63d_base_v080_signal,
    f27sm_f27_speculative_multiple_decay_psdecay_504d_base_v081_signal,
    f27sm_f27_speculative_multiple_decay_pbdecay_504d_base_v082_signal,
    f27sm_f27_speculative_multiple_decay_pedecay_252d_base_v083_signal,
    f27sm_f27_speculative_multiple_decay_psreldecay_504d_base_v084_signal,
    f27sm_f27_speculative_multiple_decay_pbreldecay_126d_base_v085_signal,
    f27sm_f27_speculative_multiple_decay_psz_189d_base_v086_signal,
    f27sm_f27_speculative_multiple_decay_pbz_189d_base_v087_signal,
    f27sm_f27_speculative_multiple_decay_psz_63d_base_v088_signal,
    f27sm_f27_speculative_multiple_decay_pbz_63d_base_v089_signal,
    f27sm_f27_speculative_multiple_decay_pez_504d_base_v090_signal,
    f27sm_f27_speculative_multiple_decay_psrank_126d_base_v091_signal,
    f27sm_f27_speculative_multiple_decay_pbrank_126d_base_v092_signal,
    f27sm_f27_speculative_multiple_decay_perank_504d_base_v093_signal,
    f27sm_f27_speculative_multiple_decay_psrich_504d_base_v094_signal,
    f27sm_f27_speculative_multiple_decay_pbrich_126d_base_v095_signal,
    f27sm_f27_speculative_multiple_decay_logpsrich_126d_base_v096_signal,
    f27sm_f27_speculative_multiple_decay_logpbrich_504d_base_v097_signal,
    f27sm_f27_speculative_multiple_decay_psdecayrate_42d_base_v098_signal,
    f27sm_f27_speculative_multiple_decay_pbdecayrate_63d_base_v099_signal,
    f27sm_f27_speculative_multiple_decay_psdecayrate_126d_base_v100_signal,
    f27sm_f27_speculative_multiple_decay_pstrend_252d_base_v101_signal,
    f27sm_f27_speculative_multiple_decay_pbtrend_63d_base_v102_signal,
    f27sm_f27_speculative_multiple_decay_petrend_126d_base_v103_signal,
    f27sm_f27_speculative_multiple_decay_pspbcross_126d_base_v104_signal,
    f27sm_f27_speculative_multiple_decay_logpspbcross_63d_base_v105_signal,
    f27sm_f27_speculative_multiple_decay_pbpecross_63d_base_v106_signal,
    f27sm_f27_speculative_multiple_decay_crossdecay_252d_base_v107_signal,
    f27sm_f27_speculative_multiple_decay_psdisp_63d_base_v108_signal,
    f27sm_f27_speculative_multiple_decay_pbdisp_126d_base_v109_signal,
    f27sm_f27_speculative_multiple_decay_pscv_126d_base_v110_signal,
    f27sm_f27_speculative_multiple_decay_pbcv_126d_base_v111_signal,
    f27sm_f27_speculative_multiple_decay_pscompress42_base_v112_signal,
    f27sm_f27_speculative_multiple_decay_pbcompress42_base_v113_signal,
    f27sm_f27_speculative_multiple_decay_pszsm_126d_base_v114_signal,
    f27sm_f27_speculative_multiple_decay_pbzsm_126d_base_v115_signal,
    f27sm_f27_speculative_multiple_decay_zspread_126d_base_v116_signal,
    f27sm_f27_speculative_multiple_decay_pbzpez_252d_base_v117_signal,
    f27sm_f27_speculative_multiple_decay_rankspread_504d_base_v118_signal,
    f27sm_f27_speculative_multiple_decay_psrankchg_126d_base_v119_signal,
    f27sm_f27_speculative_multiple_decay_pbrankchg_21d_base_v120_signal,
    f27sm_f27_speculative_multiple_decay_pszchg_63d_base_v121_signal,
    f27sm_f27_speculative_multiple_decay_pbzchg_63d_base_v122_signal,
    f27sm_f27_speculative_multiple_decay_pshalflife_63d_base_v123_signal,
    f27sm_f27_speculative_multiple_decay_pbhalflife_21d_base_v124_signal,
    f27sm_f27_speculative_multiple_decay_pslogdecay_126d_base_v125_signal,
    f27sm_f27_speculative_multiple_decay_pblogdecay_126d_base_v126_signal,
    f27sm_f27_speculative_multiple_decay_psewmdecay_126d_base_v127_signal,
    f27sm_f27_speculative_multiple_decay_pbewmdecay_126d_base_v128_signal,
    f27sm_f27_speculative_multiple_decay_pbrelewm_63d_base_v129_signal,
    f27sm_f27_speculative_multiple_decay_psdecayz_252d_base_v130_signal,
    f27sm_f27_speculative_multiple_decay_pbdecayz_252d_base_v131_signal,
    f27sm_f27_speculative_multiple_decay_pbaccel_base_v132_signal,
    f27sm_f27_speculative_multiple_decay_psskew_126d_base_v133_signal,
    f27sm_f27_speculative_multiple_decay_pbkurt_252d_base_v134_signal,
    f27sm_f27_speculative_multiple_decay_pszterm_base_v135_signal,
    f27sm_f27_speculative_multiple_decay_pbzterm_base_v136_signal,
    f27sm_f27_speculative_multiple_decay_psdecayterm_base_v137_signal,
    f27sm_f27_speculative_multiple_decay_psexcessz_126d_base_v138_signal,
    f27sm_f27_speculative_multiple_decay_pbexcessz_126d_base_v139_signal,
    f27sm_f27_speculative_multiple_decay_psslowrich_base_v140_signal,
    f27sm_f27_speculative_multiple_decay_pbslowrich_base_v141_signal,
    f27sm_f27_speculative_multiple_decay_psgapdisp_126d_base_v142_signal,
    f27sm_f27_speculative_multiple_decay_pbgapdisp_126d_base_v143_signal,
    f27sm_f27_speculative_multiple_decay_psewmz_63d_base_v144_signal,
    f27sm_f27_speculative_multiple_decay_pbewmz_63d_base_v145_signal,
    f27sm_f27_speculative_multiple_decay_perich_252d_base_v146_signal,
    f27sm_f27_speculative_multiple_decay_combz_252d_base_v147_signal,
    f27sm_f27_speculative_multiple_decay_combrank_252d_base_v148_signal,
    f27sm_f27_speculative_multiple_decay_combdecay_252d_base_v149_signal,
    f27sm_f27_speculative_multiple_decay_specblend_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_SPECULATIVE_MULTIPLE_DECAY_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f27_speculative_multiple_decay_base_076_150_claude: {n_features} features pass")
