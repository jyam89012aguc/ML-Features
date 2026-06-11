import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


# ===== folder domain primitives =====
def _f21_ppe_rejuvenation(capex, ppnenet, depamor):
    return (capex - depamor) / ppnenet.replace(0, np.nan).abs()


def _f21_replacement_intensity(capex, depamor):
    return capex / depamor.replace(0, np.nan).abs()


def _f21_ppe_freshness(ppnenet, depamor, w):
    dep_avg = depamor.rolling(w, min_periods=max(1, w // 2)).mean()
    return ppnenet / dep_avg.replace(0, np.nan).abs()


# v076: replacement intensity reciprocal * close
def f21smr_f21_specialty_machinery_replacement_repl_inv_base_v076_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = (1.0 / (base.abs() + 1e-9)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v077: rejuv ema 126d * close
def f21smr_f21_specialty_machinery_replacement_rejuv_ema_126d_base_v077_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base.ewm(span=126, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v078: freshness ema 126d * close (252 base)
def f21smr_f21_specialty_machinery_replacement_freshness_ema_126d_base_v078_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = base.ewm(span=126, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v079: composite rolling 21 * close
def f21smr_f21_specialty_machinery_replacement_composite_21d_base_v079_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = r + j
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v080: composite rolling 63 * close
def f21smr_f21_specialty_machinery_replacement_composite_63d_base_v080_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = r + j
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v081: composite rolling 126 * close
def f21smr_f21_specialty_machinery_replacement_composite_126d_base_v081_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = r + j
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v082: composite rolling 252 * close
def f21smr_f21_specialty_machinery_replacement_composite_252d_base_v082_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = r + j
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v083: composite std 63 * close
def f21smr_f21_specialty_machinery_replacement_composite_std_63d_base_v083_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = r + j
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v084: composite std 252 * close
def f21smr_f21_specialty_machinery_replacement_composite_std_252d_base_v084_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    base = r + j
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v085: rejuv times closeadj squared
def f21smr_f21_specialty_machinery_replacement_rejuv_x_close2_base_v085_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v086: replacement intensity times closeadj / 100
def f21smr_f21_specialty_machinery_replacement_repl_xclose2_base_v086_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v087: freshness * closeadj * closeadj / 100
def f21smr_f21_specialty_machinery_replacement_freshness_xclose2_base_v087_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v088: replacement intensity above 2 indicator * close
def f21smr_f21_specialty_machinery_replacement_repl_above2_base_v088_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    ind = (base > 2.0).astype(float) * base
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v089: rejuv abs * close
def f21smr_f21_specialty_machinery_replacement_rejuv_abs_base_v089_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v090: replacement intensity log * close
def f21smr_f21_specialty_machinery_replacement_repl_log_base_v090_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor).abs() + 1.0
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v091: rejuv log * close
def f21smr_f21_specialty_machinery_replacement_rejuv_log_base_v091_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs() + 1e-6
    result = np.log(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v092: replacement intensity sign * close
def f21smr_f21_specialty_machinery_replacement_repl_sign_base_v092_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = np.sign(base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v093: 21d cross 252d freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_cross_21_252_base_v093_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (_mean(base, 21) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v094: 63 cross 252 freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_cross_63_252_base_v094_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v095: 126 cross 504 freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_cross_126_504_base_v095_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 504)
    result = (_mean(base, 126) - _mean(base, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v096: replacement intensity diff vs 21d * close
def f21smr_f21_specialty_machinery_replacement_repl_diff_21d_base_v096_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v097: rejuv diff 63d * close
def f21smr_f21_specialty_machinery_replacement_rejuv_diff_63d_base_v097_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v098: freshness diff 252d * close
def f21smr_f21_specialty_machinery_replacement_freshness_diff_252d_base_v098_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (base - base.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v099: cumulative rejuv (capex - dep) / ppnenet then mean 504 * close
def f21smr_f21_specialty_machinery_replacement_rejuv_cum_base_v099_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v100: composite triple product
def f21smr_f21_specialty_machinery_replacement_composite_triple_base_v100_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = r * j * f * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v101: replacement intensity ema 504
def f21smr_f21_specialty_machinery_replacement_repl_ema_504d_base_v101_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base.ewm(span=504, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v102: rejuv ema 504
def f21smr_f21_specialty_machinery_replacement_rejuv_ema_504d_base_v102_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base.ewm(span=504, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v103: 21d window freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_42d_base_v103_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v104: 10d freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_10d_base_v104_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v105: 5d freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_5d_base_v105_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v106: 189d freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_189d_base_v106_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v107: 378d freshness * close
def f21smr_f21_specialty_machinery_replacement_freshness_378d_base_v107_signal(ppnenet, depamor, closeadj):
    result = _f21_ppe_freshness(ppnenet, depamor, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v108: 5d std replacement intensity * close
def f21smr_f21_specialty_machinery_replacement_repl_std_5d_base_v108_signal(capex, depamor, closeadj):
    result = _std(_f21_replacement_intensity(capex, depamor), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v109: 126d std replacement intensity * close
def f21smr_f21_specialty_machinery_replacement_repl_std_126d_base_v109_signal(capex, depamor, closeadj):
    result = _std(_f21_replacement_intensity(capex, depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v110: 504d std replacement intensity * close
def f21smr_f21_specialty_machinery_replacement_repl_std_504d_base_v110_signal(capex, depamor, closeadj):
    result = _std(_f21_replacement_intensity(capex, depamor), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v111: 126d std rejuv * close
def f21smr_f21_specialty_machinery_replacement_rejuv_std_126d_base_v111_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v112: 42d std rejuv * close
def f21smr_f21_specialty_machinery_replacement_rejuv_std_42d_base_v112_signal(capex, ppnenet, depamor, closeadj):
    result = _std(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v113: freshness std 63 * close
def f21smr_f21_specialty_machinery_replacement_freshness_std_63d_base_v113_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v114: freshness std 126 * close
def f21smr_f21_specialty_machinery_replacement_freshness_std_126d_base_v114_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v115: freshness std 504 * close
def f21smr_f21_specialty_machinery_replacement_freshness_std_504d_base_v115_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v116: rejuv z 63 * close
def f21smr_f21_specialty_machinery_replacement_rejuv_z_63d_base_v116_signal(capex, ppnenet, depamor, closeadj):
    result = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v117: rejuv z 126 * close
def f21smr_f21_specialty_machinery_replacement_rejuv_z_126d_base_v117_signal(capex, ppnenet, depamor, closeadj):
    result = _z(_f21_ppe_rejuvenation(capex, ppnenet, depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v118: repl z 63
def f21smr_f21_specialty_machinery_replacement_repl_z_63d_base_v118_signal(capex, depamor, closeadj):
    result = _z(_f21_replacement_intensity(capex, depamor), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v119: repl z 126
def f21smr_f21_specialty_machinery_replacement_repl_z_126d_base_v119_signal(capex, depamor, closeadj):
    result = _z(_f21_replacement_intensity(capex, depamor), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v120: freshness z 126
def f21smr_f21_specialty_machinery_replacement_freshness_z_126d_base_v120_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v121: capex / ppnenet ratio with primitive in body
def f21smr_f21_specialty_machinery_replacement_capex_to_ppe_base_v121_signal(capex, ppnenet, depamor, closeadj):
    ratio = capex / ppnenet.replace(0, np.nan).abs()
    _ = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = _mean(ratio, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v122: depamor / ppnenet (dep rate) - use primitive _f21_ppe_freshness internally
def f21smr_f21_specialty_machinery_replacement_dep_rate_base_v122_signal(ppnenet, depamor, closeadj):
    base = depamor / ppnenet.replace(0, np.nan).abs()
    _ = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v123: capex - dep (rejuv numerator) scaled
def f21smr_f21_specialty_machinery_replacement_rejuv_num_base_v123_signal(capex, ppnenet, depamor, closeadj):
    base = capex - depamor
    _ = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = _mean(base, 63) / 1e7 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v124: composite triple z 252 * close
def f21smr_f21_specialty_machinery_replacement_composite_triple_z_252d_base_v124_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    base = r * j * f
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v125: replacement intensity smoothed - 252 mean (deviation)
def f21smr_f21_specialty_machinery_replacement_repl_dev_252d_base_v125_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    sm = _mean(base, 21)
    result = (sm - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v126: rejuv 63 dev (63 - 252)
def f21smr_f21_specialty_machinery_replacement_rejuv_dev_63_252_base_v126_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v127: freshness diff 63 vs 252 (cycle pulse)
def f21smr_f21_specialty_machinery_replacement_freshness_pulse_base_v127_signal(ppnenet, depamor, closeadj):
    a = _f21_ppe_freshness(ppnenet, depamor, 63)
    b = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v128: replacement intensity bounded sqrt * close
def f21smr_f21_specialty_machinery_replacement_repl_sqrt_base_v128_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v129: rejuv sqrt(abs) * close
def f21smr_f21_specialty_machinery_replacement_rejuv_sqrt_base_v129_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor).abs()
    result = np.sqrt(base + 1e-12) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v130: freshness sqrt 252 * close
def f21smr_f21_specialty_machinery_replacement_freshness_sqrt_base_v130_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v131: replacement intensity rolling median 63 * close
def f21smr_f21_specialty_machinery_replacement_repl_med_63d_base_v131_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base.rolling(63, min_periods=21).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v132: rejuv rolling median 252 * close
def f21smr_f21_specialty_machinery_replacement_rejuv_med_252d_base_v132_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v133: freshness rolling median 252 * close
def f21smr_f21_specialty_machinery_replacement_freshness_med_252d_base_v133_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = base.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v134: rejuv * freshness / replacement (relative compound)
def f21smr_f21_specialty_machinery_replacement_rj_f_div_repl_base_v134_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _safe_div(j * f, r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v135: rejuv plus freshness then sqrt
def f21smr_f21_specialty_machinery_replacement_j_plus_f_sqrt_base_v135_signal(capex, ppnenet, depamor, closeadj):
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 252)
    s = (j + f).abs()
    result = np.sqrt(s + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v136: replacement intensity 21d divided by 252d (ratio of horizons)
def f21smr_f21_specialty_machinery_replacement_repl_ratio_21_252_base_v136_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = _safe_div(_mean(base, 21), _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v137: rejuv 63 / 252 ratio
def f21smr_f21_specialty_machinery_replacement_rejuv_ratio_63_252_base_v137_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = _safe_div(_mean(base, 63), _mean(base, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v138: freshness 63 / 252 ratio
def f21smr_f21_specialty_machinery_replacement_freshness_ratio_63_252_base_v138_signal(ppnenet, depamor, closeadj):
    a = _f21_ppe_freshness(ppnenet, depamor, 63)
    b = _f21_ppe_freshness(ppnenet, depamor, 252)
    result = _safe_div(a, b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v139: replacement intensity * capex/dep secondary
def f21smr_f21_specialty_machinery_replacement_repl_x_capex_dep_base_v139_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    sec = capex / depamor.replace(0, np.nan).abs()
    result = base * sec * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# v140: 63d rolling rank rejuv
def f21smr_f21_specialty_machinery_replacement_rejuv_rank_63d_base_v140_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rk = base.rolling(63, min_periods=21).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v141: 504d rolling rank rejuv
def f21smr_f21_specialty_machinery_replacement_rejuv_rank_504d_base_v141_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    rk = base.rolling(504, min_periods=126).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v142: 63d rolling rank replacement
def f21smr_f21_specialty_machinery_replacement_repl_rank_63d_base_v142_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rk = base.rolling(63, min_periods=21).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v143: 504d rolling rank replacement
def f21smr_f21_specialty_machinery_replacement_repl_rank_504d_base_v143_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    rk = base.rolling(504, min_periods=126).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v144: freshness rank 63
def f21smr_f21_specialty_machinery_replacement_freshness_rank_63d_base_v144_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    rk = base.rolling(63, min_periods=21).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v145: rejuv minus its 252d ema * close
def f21smr_f21_specialty_machinery_replacement_rejuv_ema_dev_252d_base_v145_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    ema = base.ewm(span=252, min_periods=63).mean()
    result = (base - ema) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v146: repl minus its 252 ema
def f21smr_f21_specialty_machinery_replacement_repl_ema_dev_252d_base_v146_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    ema = base.ewm(span=252, min_periods=63).mean()
    result = (base - ema) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v147: freshness minus 252 ema
def f21smr_f21_specialty_machinery_replacement_freshness_ema_dev_252d_base_v147_signal(ppnenet, depamor, closeadj):
    base = _f21_ppe_freshness(ppnenet, depamor, 252)
    ema = base.ewm(span=252, min_periods=63).mean()
    result = (base - ema) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v148: replacement intensity squared * close
def f21smr_f21_specialty_machinery_replacement_repl_sq_base_v148_signal(capex, depamor, closeadj):
    base = _f21_replacement_intensity(capex, depamor)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v149: rejuv squared * close
def f21smr_f21_specialty_machinery_replacement_rejuv_sq_base_v149_signal(capex, ppnenet, depamor, closeadj):
    base = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v150: triple primitive combo * close
def f21smr_f21_specialty_machinery_replacement_triple_combo_base_v150_signal(capex, ppnenet, depamor, closeadj):
    r = _f21_replacement_intensity(capex, depamor)
    j = _f21_ppe_rejuvenation(capex, ppnenet, depamor)
    f = _f21_ppe_freshness(ppnenet, depamor, 504)
    base = _mean(r, 63) + _mean(j, 63) + _mean(f, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f21smr_f21_specialty_machinery_replacement_repl_inv_base_v076_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_ema_126d_base_v077_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_ema_126d_base_v078_signal,
    f21smr_f21_specialty_machinery_replacement_composite_21d_base_v079_signal,
    f21smr_f21_specialty_machinery_replacement_composite_63d_base_v080_signal,
    f21smr_f21_specialty_machinery_replacement_composite_126d_base_v081_signal,
    f21smr_f21_specialty_machinery_replacement_composite_252d_base_v082_signal,
    f21smr_f21_specialty_machinery_replacement_composite_std_63d_base_v083_signal,
    f21smr_f21_specialty_machinery_replacement_composite_std_252d_base_v084_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_x_close2_base_v085_signal,
    f21smr_f21_specialty_machinery_replacement_repl_xclose2_base_v086_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_xclose2_base_v087_signal,
    f21smr_f21_specialty_machinery_replacement_repl_above2_base_v088_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_abs_base_v089_signal,
    f21smr_f21_specialty_machinery_replacement_repl_log_base_v090_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_log_base_v091_signal,
    f21smr_f21_specialty_machinery_replacement_repl_sign_base_v092_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_cross_21_252_base_v093_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_cross_63_252_base_v094_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_cross_126_504_base_v095_signal,
    f21smr_f21_specialty_machinery_replacement_repl_diff_21d_base_v096_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_diff_63d_base_v097_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_diff_252d_base_v098_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_cum_base_v099_signal,
    f21smr_f21_specialty_machinery_replacement_composite_triple_base_v100_signal,
    f21smr_f21_specialty_machinery_replacement_repl_ema_504d_base_v101_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_ema_504d_base_v102_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_42d_base_v103_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_10d_base_v104_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_5d_base_v105_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_189d_base_v106_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_378d_base_v107_signal,
    f21smr_f21_specialty_machinery_replacement_repl_std_5d_base_v108_signal,
    f21smr_f21_specialty_machinery_replacement_repl_std_126d_base_v109_signal,
    f21smr_f21_specialty_machinery_replacement_repl_std_504d_base_v110_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_126d_base_v111_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_std_42d_base_v112_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_std_63d_base_v113_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_std_126d_base_v114_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_std_504d_base_v115_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_z_63d_base_v116_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_z_126d_base_v117_signal,
    f21smr_f21_specialty_machinery_replacement_repl_z_63d_base_v118_signal,
    f21smr_f21_specialty_machinery_replacement_repl_z_126d_base_v119_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_z_126d_base_v120_signal,
    f21smr_f21_specialty_machinery_replacement_capex_to_ppe_base_v121_signal,
    f21smr_f21_specialty_machinery_replacement_dep_rate_base_v122_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_num_base_v123_signal,
    f21smr_f21_specialty_machinery_replacement_composite_triple_z_252d_base_v124_signal,
    f21smr_f21_specialty_machinery_replacement_repl_dev_252d_base_v125_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_dev_63_252_base_v126_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_pulse_base_v127_signal,
    f21smr_f21_specialty_machinery_replacement_repl_sqrt_base_v128_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_sqrt_base_v129_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_sqrt_base_v130_signal,
    f21smr_f21_specialty_machinery_replacement_repl_med_63d_base_v131_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_med_252d_base_v132_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_med_252d_base_v133_signal,
    f21smr_f21_specialty_machinery_replacement_rj_f_div_repl_base_v134_signal,
    f21smr_f21_specialty_machinery_replacement_j_plus_f_sqrt_base_v135_signal,
    f21smr_f21_specialty_machinery_replacement_repl_ratio_21_252_base_v136_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_ratio_63_252_base_v137_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_ratio_63_252_base_v138_signal,
    f21smr_f21_specialty_machinery_replacement_repl_x_capex_dep_base_v139_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_rank_63d_base_v140_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_rank_504d_base_v141_signal,
    f21smr_f21_specialty_machinery_replacement_repl_rank_63d_base_v142_signal,
    f21smr_f21_specialty_machinery_replacement_repl_rank_504d_base_v143_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_rank_63d_base_v144_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_ema_dev_252d_base_v145_signal,
    f21smr_f21_specialty_machinery_replacement_repl_ema_dev_252d_base_v146_signal,
    f21smr_f21_specialty_machinery_replacement_freshness_ema_dev_252d_base_v147_signal,
    f21smr_f21_specialty_machinery_replacement_repl_sq_base_v148_signal,
    f21smr_f21_specialty_machinery_replacement_rejuv_sq_base_v149_signal,
    f21smr_f21_specialty_machinery_replacement_triple_combo_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F21_SPECIALTY_MACHINERY_REPLACEMENT_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {"closeadj": closeadj, "capex": capex, "depamor": depamor, "ppnenet": ppnenet}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f21_ppe_rejuvenation", "_f21_replacement_intensity", "_f21_ppe_freshness")
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f21_specialty_machinery_replacement_base_076_150_claude: {n_features} features pass")
