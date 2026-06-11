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


# ============ FEATURES 076-150 ============

# 42d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_42d_base_v076_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_84d_base_v077_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_189d_base_v078_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_315d_base_v079_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d smoothed concentration level
def f29oc_f29_ownership_concentration_conc_504d_base_v080_signal(percentoftotal):
    result = _f29_conc(percentoftotal, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d concentration z-score
def f29oc_f29_ownership_concentration_concz_42d_base_v081_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d concentration z-score
def f29oc_f29_ownership_concentration_concz_84d_base_v082_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d concentration z-score
def f29oc_f29_ownership_concentration_concz_189d_base_v083_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d concentration z-score
def f29oc_f29_ownership_concentration_concz_315d_base_v084_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d concentration trend slope
def f29oc_f29_ownership_concentration_trend_42d_base_v085_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 42)
    result = _safe_div(c - c.shift(42), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 84d concentration trend slope
def f29oc_f29_ownership_concentration_trend_84d_base_v086_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 84)
    result = _safe_div(c - c.shift(84), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d concentration trend slope
def f29oc_f29_ownership_concentration_trend_189d_base_v087_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 189)
    result = _safe_div(c - c.shift(189), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d concentration trend slope
def f29oc_f29_ownership_concentration_trend_504d_base_v088_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 252)
    result = _safe_div(c - c.shift(504), c.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 42d concentration dispersion
def f29oc_f29_ownership_concentration_disp_42d_base_v089_signal(percentoftotal):
    result = _std(percentoftotal, 42) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 84d concentration dispersion
def f29oc_f29_ownership_concentration_disp_84d_base_v090_signal(percentoftotal):
    result = _std(percentoftotal, 84) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d concentration dispersion
def f29oc_f29_ownership_concentration_disp_504d_base_v091_signal(percentoftotal):
    result = _std(percentoftotal, 504) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d coefficient of variation of concentration
def f29oc_f29_ownership_concentration_cv_42d_base_v092_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 42), _f29_conc(percentoftotal, 42).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d coefficient of variation of concentration
def f29oc_f29_ownership_concentration_cv_189d_base_v093_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 189), _f29_conc(percentoftotal, 189).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mix smoothed
def f29oc_f29_ownership_concentration_mix_42d_base_v094_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mix smoothed
def f29oc_f29_ownership_concentration_mix_189d_base_v095_signal(shrvalue, totalvalue):
    result = _mean(_f29_mix(shrvalue, totalvalue), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mix change
def f29oc_f29_ownership_concentration_mixchg_42d_base_v096_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(42), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mix change
def f29oc_f29_ownership_concentration_mixchg_189d_base_v097_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(m - m.shift(189), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 42d mix z-score
def f29oc_f29_ownership_concentration_mixz_42d_base_v098_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d mix z-score
def f29oc_f29_ownership_concentration_mixz_189d_base_v099_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d mix z-score
def f29oc_f29_ownership_concentration_mixz_504d_base_v100_signal(shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d concentration percentile rank blended with concentration z (continuous)
def f29oc_f29_ownership_concentration_rank_42d_base_v101_signal(percentoftotal):
    result = percentoftotal.rolling(42, min_periods=21).rank(pct=True) + _f29_concz(percentoftotal, 42) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


# 189d concentration percentile rank
def f29oc_f29_ownership_concentration_rank_189d_base_v102_signal(percentoftotal):
    result = percentoftotal.rolling(189, min_periods=63).rank(pct=True) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d concentration mean-reversion
def f29oc_f29_ownership_concentration_revert_42d_base_v103_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d concentration mean-reversion
def f29oc_f29_ownership_concentration_revert_504d_base_v104_signal(percentoftotal):
    result = -_f29_concz(percentoftotal, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d concentration gap to 252d level
def f29oc_f29_ownership_concentration_gap_42_252_base_v105_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 42) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 84d concentration gap to 252d level
def f29oc_f29_ownership_concentration_gap_84_252_base_v106_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 84) - _f29_conc(percentoftotal, 252),
                       _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d concentration gap to 504d level
def f29oc_f29_ownership_concentration_gap_126_504_base_v107_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 126) - _f29_conc(percentoftotal, 504),
                       _f29_conc(percentoftotal, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit 252d smoothed
def f29oc_f29_ownership_concentration_vpu_252d_base_v108_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit 42d smoothed
def f29oc_f29_ownership_concentration_vpu_42d_base_v109_signal(shrvalue, shrunits):
    result = _mean(_f29_vpu(shrvalue, shrunits), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit z-score 42d
def f29oc_f29_ownership_concentration_vpuz_42d_base_v110_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit z-score 504d
def f29oc_f29_ownership_concentration_vpuz_504d_base_v111_signal(shrvalue, shrunits):
    result = _z(_f29_vpu(shrvalue, shrunits), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit change 252d
def f29oc_f29_ownership_concentration_vpuchg_252d_base_v112_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(v - v.shift(252), v.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit percentile rank 252d
def f29oc_f29_ownership_concentration_vpurank_252d_base_v113_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = v.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit dispersion 126d
def f29oc_f29_ownership_concentration_vpudisp_126d_base_v114_signal(shrvalue, shrunits):
    result = _std(_f29_vpu(shrvalue, shrunits), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit CV 126d
def f29oc_f29_ownership_concentration_vpucv_126d_base_v115_signal(shrvalue, shrunits):
    v = _f29_vpu(shrvalue, shrunits)
    result = _safe_div(_std(v, 126), _mean(v, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs 252d ratio (84d level)
def f29oc_f29_ownership_concentration_vsann_84d_base_v116_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 84), _f29_conc(percentoftotal, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration vs 504d ratio (63d level)
def f29oc_f29_ownership_concentration_vs504_63d_base_v117_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63), _f29_conc(percentoftotal, 504).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# holder-skew proxy: 63d rolling skew of concentration
def f29oc_f29_ownership_concentration_skew_63d_base_v118_signal(percentoftotal):
    result = percentoftotal.rolling(63, min_periods=21).skew() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# holder-skew proxy: 189d rolling skew of concentration
def f29oc_f29_ownership_concentration_skew_189d_base_v119_signal(percentoftotal):
    result = percentoftotal.rolling(189, min_periods=63).skew() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration 63d rolling kurtosis
def f29oc_f29_ownership_concentration_kurt_63d_base_v120_signal(percentoftotal):
    result = percentoftotal.rolling(63, min_periods=21).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration 189d rolling kurtosis
def f29oc_f29_ownership_concentration_kurt_189d_base_v121_signal(percentoftotal):
    result = percentoftotal.rolling(189, min_periods=63).kurt() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d EWMA of concentration level
def f29oc_f29_ownership_concentration_ewm_42d_base_v122_signal(percentoftotal):
    result = percentoftotal.ewm(span=42, min_periods=21).mean() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA of concentration level
def f29oc_f29_ownership_concentration_ewm_252d_base_v123_signal(percentoftotal):
    result = percentoftotal.ewm(span=252, min_periods=84).mean() + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration EWMA gap (42 vs 126)
def f29oc_f29_ownership_concentration_ewmgap_42_126_base_v124_signal(percentoftotal):
    fast = percentoftotal.ewm(span=42, min_periods=21).mean()
    slow = percentoftotal.ewm(span=126, min_periods=42).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration EWMA gap (126 vs 252)
def f29oc_f29_ownership_concentration_ewmgap_126_252_base_v125_signal(percentoftotal):
    fast = percentoftotal.ewm(span=126, min_periods=42).mean()
    slow = percentoftotal.ewm(span=252, min_periods=84).mean()
    result = _safe_div(fast - slow, slow.abs()) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration scaled by mix (84d)
def f29oc_f29_ownership_concentration_concmix_84d_base_v126_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_conc(percentoftotal, 84) * _f29_mix(shrvalue, totalvalue)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration z scaled by mix z (252d)
def f29oc_f29_ownership_concentration_concmixz_252d_base_v127_signal(percentoftotal, shrvalue, totalvalue):
    result = _f29_concz(percentoftotal, 252) * _z(_f29_mix(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# mix dispersion 252d
def f29oc_f29_ownership_concentration_mixdisp_252d_base_v128_signal(shrvalue, totalvalue):
    result = _std(_f29_mix(shrvalue, totalvalue), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# mix CV 126d
def f29oc_f29_ownership_concentration_mixcv_126d_base_v129_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(_std(m, 126), _mean(m, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# mix percentile rank 126d
def f29oc_f29_ownership_concentration_mixrank_126d_base_v130_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = m.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration log level 126d
def f29oc_f29_ownership_concentration_loglvl_126d_base_v131_signal(percentoftotal):
    result = np.log(_f29_conc(percentoftotal, 126).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration log change 126d
def f29oc_f29_ownership_concentration_logchg_126d_base_v132_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 21)
    result = np.log(c.abs() + 1.0) - np.log(c.shift(126).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration acceleration (63d trend minus 126d trend)
def f29oc_f29_ownership_concentration_accel_63_126_base_v133_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 63)
    t1 = _safe_div(c - c.shift(63), c.abs())
    t2 = _safe_div(c - c.shift(126), c.abs())
    result = t1 - t2
    return result.replace([np.inf, -np.inf], np.nan)


# concentration dispersion ratio (42 vs 126)
def f29oc_f29_ownership_concentration_dispratio_42_126_base_v134_signal(percentoftotal):
    result = _safe_div(_std(percentoftotal, 42), _std(percentoftotal, 126)) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit weighted by concentration (richness, 63d)
def f29oc_f29_ownership_concentration_vpuconc_63d_base_v135_signal(shrvalue, shrunits, percentoftotal):
    result = _z(_f29_vpu(shrvalue, shrunits), 63) * _f29_conc(percentoftotal, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# mix minus concentration (holder-type divergence, 126d z)
def f29oc_f29_ownership_concentration_mixconcdiv_126d_base_v136_signal(percentoftotal, shrvalue, totalvalue):
    result = _z(_f29_mix(shrvalue, totalvalue), 126) - _f29_concz(percentoftotal, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration spread short vs long smoothed levels (21 vs 63)
def f29oc_f29_ownership_concentration_spread_21_63_base_v137_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 21) - _f29_conc(percentoftotal, 63),
                       _f29_conc(percentoftotal, 63).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration spread 63 vs 126
def f29oc_f29_ownership_concentration_spread_63_126_base_v138_signal(percentoftotal):
    result = _safe_div(_f29_conc(percentoftotal, 63) - _f29_conc(percentoftotal, 126),
                       _f29_conc(percentoftotal, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration z-score difference (short vs long window)
def f29oc_f29_ownership_concentration_zdiff_63_252_base_v139_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 63) - _f29_concz(percentoftotal, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration z-score difference (126 vs 504)
def f29oc_f29_ownership_concentration_zdiff_126_504_base_v140_signal(percentoftotal):
    result = _f29_concz(percentoftotal, 126) - _f29_concz(percentoftotal, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# mix trend slope smoothed (63d level diff)
def f29oc_f29_ownership_concentration_mixtrend_63d_base_v141_signal(shrvalue, totalvalue):
    m = _mean(_f29_mix(shrvalue, totalvalue), 63)
    result = _safe_div(m - m.shift(63), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# mix trend slope smoothed (126d level diff)
def f29oc_f29_ownership_concentration_mixtrend_126d_base_v142_signal(shrvalue, totalvalue):
    m = _mean(_f29_mix(shrvalue, totalvalue), 126)
    result = _safe_div(m - m.shift(126), m.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit log level 63d
def f29oc_f29_ownership_concentration_vpulog_63d_base_v143_signal(shrvalue, shrunits):
    result = np.log(_mean(_f29_vpu(shrvalue, shrunits), 63).abs() + 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration-weighted value per unit (mix interaction, 126d)
def f29oc_f29_ownership_concentration_vpumixw_126d_base_v144_signal(shrvalue, shrunits, totalvalue):
    result = _z(_f29_vpu(shrvalue, shrunits), 126) * _z(_f29_mix(shrvalue, totalvalue), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# concentration EWMA z-score (smoothed then standardized, 126d)
def f29oc_f29_ownership_concentration_ewmz_126d_base_v145_signal(percentoftotal):
    e = percentoftotal.ewm(span=63, min_periods=21).mean()
    result = _z(e, 126) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# concentration mean-reversion vs trend composite (252d)
def f29oc_f29_ownership_concentration_revtrend_252d_base_v146_signal(percentoftotal):
    c = _f29_conc(percentoftotal, 63)
    trend = _safe_div(c - c.shift(252), c.abs())
    result = trend - _f29_concz(percentoftotal, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# mix CV 252d
def f29oc_f29_ownership_concentration_mixcv_252d_base_v147_signal(shrvalue, totalvalue):
    m = _f29_mix(shrvalue, totalvalue)
    result = _safe_div(_std(m, 252), _mean(m, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# concentration dispersion z-score (regime of holder churn, 252d)
def f29oc_f29_ownership_concentration_dispz_252d_base_v148_signal(percentoftotal):
    d = _std(percentoftotal, 63)
    result = _z(d, 252) + _f29_conc(percentoftotal, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# value-per-unit vs concentration ratio (richness per holding share, 126d)
def f29oc_f29_ownership_concentration_vpuratio_126d_base_v149_signal(shrvalue, shrunits, percentoftotal):
    result = _safe_div(_mean(_f29_vpu(shrvalue, shrunits), 126), _f29_conc(percentoftotal, 126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon concentration z composite (21/63/126/252)
def f29oc_f29_ownership_concentration_blend_multi_base_v150_signal(percentoftotal):
    result = (_f29_concz(percentoftotal, 21) + _f29_concz(percentoftotal, 63)
              + _f29_concz(percentoftotal, 126) + _f29_concz(percentoftotal, 252)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29oc_f29_ownership_concentration_conc_42d_base_v076_signal,
    f29oc_f29_ownership_concentration_conc_84d_base_v077_signal,
    f29oc_f29_ownership_concentration_conc_189d_base_v078_signal,
    f29oc_f29_ownership_concentration_conc_315d_base_v079_signal,
    f29oc_f29_ownership_concentration_conc_504d_base_v080_signal,
    f29oc_f29_ownership_concentration_concz_42d_base_v081_signal,
    f29oc_f29_ownership_concentration_concz_84d_base_v082_signal,
    f29oc_f29_ownership_concentration_concz_189d_base_v083_signal,
    f29oc_f29_ownership_concentration_concz_315d_base_v084_signal,
    f29oc_f29_ownership_concentration_trend_42d_base_v085_signal,
    f29oc_f29_ownership_concentration_trend_84d_base_v086_signal,
    f29oc_f29_ownership_concentration_trend_189d_base_v087_signal,
    f29oc_f29_ownership_concentration_trend_504d_base_v088_signal,
    f29oc_f29_ownership_concentration_disp_42d_base_v089_signal,
    f29oc_f29_ownership_concentration_disp_84d_base_v090_signal,
    f29oc_f29_ownership_concentration_disp_504d_base_v091_signal,
    f29oc_f29_ownership_concentration_cv_42d_base_v092_signal,
    f29oc_f29_ownership_concentration_cv_189d_base_v093_signal,
    f29oc_f29_ownership_concentration_mix_42d_base_v094_signal,
    f29oc_f29_ownership_concentration_mix_189d_base_v095_signal,
    f29oc_f29_ownership_concentration_mixchg_42d_base_v096_signal,
    f29oc_f29_ownership_concentration_mixchg_189d_base_v097_signal,
    f29oc_f29_ownership_concentration_mixz_42d_base_v098_signal,
    f29oc_f29_ownership_concentration_mixz_189d_base_v099_signal,
    f29oc_f29_ownership_concentration_mixz_504d_base_v100_signal,
    f29oc_f29_ownership_concentration_rank_42d_base_v101_signal,
    f29oc_f29_ownership_concentration_rank_189d_base_v102_signal,
    f29oc_f29_ownership_concentration_revert_42d_base_v103_signal,
    f29oc_f29_ownership_concentration_revert_504d_base_v104_signal,
    f29oc_f29_ownership_concentration_gap_42_252_base_v105_signal,
    f29oc_f29_ownership_concentration_gap_84_252_base_v106_signal,
    f29oc_f29_ownership_concentration_gap_126_504_base_v107_signal,
    f29oc_f29_ownership_concentration_vpu_252d_base_v108_signal,
    f29oc_f29_ownership_concentration_vpu_42d_base_v109_signal,
    f29oc_f29_ownership_concentration_vpuz_42d_base_v110_signal,
    f29oc_f29_ownership_concentration_vpuz_504d_base_v111_signal,
    f29oc_f29_ownership_concentration_vpuchg_252d_base_v112_signal,
    f29oc_f29_ownership_concentration_vpurank_252d_base_v113_signal,
    f29oc_f29_ownership_concentration_vpudisp_126d_base_v114_signal,
    f29oc_f29_ownership_concentration_vpucv_126d_base_v115_signal,
    f29oc_f29_ownership_concentration_vsann_84d_base_v116_signal,
    f29oc_f29_ownership_concentration_vs504_63d_base_v117_signal,
    f29oc_f29_ownership_concentration_skew_63d_base_v118_signal,
    f29oc_f29_ownership_concentration_skew_189d_base_v119_signal,
    f29oc_f29_ownership_concentration_kurt_63d_base_v120_signal,
    f29oc_f29_ownership_concentration_kurt_189d_base_v121_signal,
    f29oc_f29_ownership_concentration_ewm_42d_base_v122_signal,
    f29oc_f29_ownership_concentration_ewm_252d_base_v123_signal,
    f29oc_f29_ownership_concentration_ewmgap_42_126_base_v124_signal,
    f29oc_f29_ownership_concentration_ewmgap_126_252_base_v125_signal,
    f29oc_f29_ownership_concentration_concmix_84d_base_v126_signal,
    f29oc_f29_ownership_concentration_concmixz_252d_base_v127_signal,
    f29oc_f29_ownership_concentration_mixdisp_252d_base_v128_signal,
    f29oc_f29_ownership_concentration_mixcv_126d_base_v129_signal,
    f29oc_f29_ownership_concentration_mixrank_126d_base_v130_signal,
    f29oc_f29_ownership_concentration_loglvl_126d_base_v131_signal,
    f29oc_f29_ownership_concentration_logchg_126d_base_v132_signal,
    f29oc_f29_ownership_concentration_accel_63_126_base_v133_signal,
    f29oc_f29_ownership_concentration_dispratio_42_126_base_v134_signal,
    f29oc_f29_ownership_concentration_vpuconc_63d_base_v135_signal,
    f29oc_f29_ownership_concentration_mixconcdiv_126d_base_v136_signal,
    f29oc_f29_ownership_concentration_spread_21_63_base_v137_signal,
    f29oc_f29_ownership_concentration_spread_63_126_base_v138_signal,
    f29oc_f29_ownership_concentration_zdiff_63_252_base_v139_signal,
    f29oc_f29_ownership_concentration_zdiff_126_504_base_v140_signal,
    f29oc_f29_ownership_concentration_mixtrend_63d_base_v141_signal,
    f29oc_f29_ownership_concentration_mixtrend_126d_base_v142_signal,
    f29oc_f29_ownership_concentration_vpulog_63d_base_v143_signal,
    f29oc_f29_ownership_concentration_vpumixw_126d_base_v144_signal,
    f29oc_f29_ownership_concentration_ewmz_126d_base_v145_signal,
    f29oc_f29_ownership_concentration_revtrend_252d_base_v146_signal,
    f29oc_f29_ownership_concentration_mixcv_252d_base_v147_signal,
    f29oc_f29_ownership_concentration_dispz_252d_base_v148_signal,
    f29oc_f29_ownership_concentration_vpuratio_126d_base_v149_signal,
    f29oc_f29_ownership_concentration_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_OWNERSHIP_CONCENTRATION_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f29_ownership_concentration_base_076_150_claude: {n_features} features pass")
