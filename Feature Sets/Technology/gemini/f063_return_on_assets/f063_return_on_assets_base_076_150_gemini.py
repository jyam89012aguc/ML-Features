import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f063_return_on_assets_core75_pct_4q_v076_signal(netinc, assetsavg):
    return _clean(_pct_change(assetsavg - _mean(assetsavg, 4), 4))
def cg_f063_return_on_assets_core76_pct_4q_v077_signal(netinc, assetsavg):
    return _clean(_pct_change(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0), 4))
def cg_f063_return_on_assets_core77_pct_4q_v078_signal(netinc, assetsavg):
    return _clean(_pct_change(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 4))
def cg_f063_return_on_assets_core78_pct_4q_v079_signal(netinc, assetsavg):
    return _clean(_pct_change(_safe_div(netinc, assetsavg).abs(), 4))
def cg_f063_return_on_assets_core79_pct_4q_v080_signal(netinc, assetsavg):
    return _clean(_pct_change(_safe_div(netinc, assetsavg * 0.5 + 1.0), 4))

# core80-89: std 8q
def cg_f063_return_on_assets_core80_std_8q_v081_signal(netinc, assetsavg):
    return _clean(_std(netinc, 8))
def cg_f063_return_on_assets_core81_std_8q_v082_signal(netinc, assetsavg):
    return _clean(_std(_safe_div(netinc, assetsavg), 8))
def cg_f063_return_on_assets_core82_std_8q_v083_signal(netinc, assetsavg):
    return _clean(_std(assetsavg, 8))
def cg_f063_return_on_assets_core83_std_8q_v084_signal(netinc, assetsavg):
    return _clean(_std(_safe_div(netinc, assetsavg.abs() + 1.0), 8))
def cg_f063_return_on_assets_core84_std_8q_v085_signal(netinc, assetsavg):
    return _clean(_std(netinc - _mean(netinc, 8), 8))
def cg_f063_return_on_assets_core85_std_8q_v086_signal(netinc, assetsavg):
    return _clean(_std(assetsavg - _mean(assetsavg, 8), 8))
def cg_f063_return_on_assets_core86_std_8q_v087_signal(netinc, assetsavg):
    return _clean(_std(_safe_div(netinc - _mean(netinc, 8), assetsavg.abs() + 1.0), 8))
def cg_f063_return_on_assets_core87_std_8q_v088_signal(netinc, assetsavg):
    return _clean(_std(_safe_div(netinc, (assetsavg - _mean(assetsavg, 8)).abs() + 1.0), 8))
def cg_f063_return_on_assets_core88_std_8q_v089_signal(netinc, assetsavg):
    return _clean(_std(_safe_div(netinc, assetsavg).abs(), 8))
def cg_f063_return_on_assets_core89_std_8q_v090_signal(netinc, assetsavg):
    return _clean(_std(_safe_div(netinc, assetsavg * 0.5 + 1.0), 8))

# core90-99: log
def cg_f063_return_on_assets_core90_log_v091_signal(netinc, assetsavg):
    return _clean(_log(netinc.abs() + 1.0))
def cg_f063_return_on_assets_core91_log_v092_signal(netinc, assetsavg):
    return _clean(_log(_safe_div(netinc, assetsavg).abs() + 1.0))
def cg_f063_return_on_assets_core92_log_v093_signal(netinc, assetsavg):
    return _clean(_log(assetsavg.abs() + 1.0))
def cg_f063_return_on_assets_core93_log_v094_signal(netinc, assetsavg):
    return _clean(_log(_safe_div(netinc, assetsavg.abs() + 1.0).abs() + 1.0))
def cg_f063_return_on_assets_core94_log_v095_signal(netinc, assetsavg):
    return _clean(_log((netinc - _mean(netinc, 4)).abs() + 1.0))
def cg_f063_return_on_assets_core95_log_v096_signal(netinc, assetsavg):
    return _clean(_log((assetsavg - _mean(assetsavg, 4)).abs() + 1.0))
def cg_f063_return_on_assets_core96_log_v097_signal(netinc, assetsavg):
    return _clean(_log(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0).abs() + 1.0))
def cg_f063_return_on_assets_core97_log_v098_signal(netinc, assetsavg):
    return _clean(_log(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0).abs() + 1.0))
def cg_f063_return_on_assets_core98_log_v099_signal(netinc, assetsavg):
    return _clean(_log(_safe_div(netinc, assetsavg).abs() + 1.0))
def cg_f063_return_on_assets_core99_log_v100_signal(netinc, assetsavg):
    return _clean(_log(_safe_div(netinc, assetsavg * 0.5 + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f063_return_on_assets_core100_diff_1q_v101_signal(netinc, assetsavg):
    return _clean(_diff(netinc, 1))
def cg_f063_return_on_assets_core101_diff_1q_v102_signal(netinc, assetsavg):
    return _clean(_diff(_safe_div(netinc, assetsavg), 1))
def cg_f063_return_on_assets_core102_diff_1q_v103_signal(netinc, assetsavg):
    return _clean(_diff(assetsavg, 1))
def cg_f063_return_on_assets_core103_diff_1q_v104_signal(netinc, assetsavg):
    return _clean(_diff(_safe_div(netinc, assetsavg.abs() + 1.0), 1))
def cg_f063_return_on_assets_core104_diff_1q_v105_signal(netinc, assetsavg):
    return _clean(_diff(netinc - _mean(netinc, 4), 1))
def cg_f063_return_on_assets_core105_diff_1q_v106_signal(netinc, assetsavg):
    return _clean(_diff(assetsavg - _mean(assetsavg, 4), 1))
def cg_f063_return_on_assets_core106_diff_1q_v107_signal(netinc, assetsavg):
    return _clean(_diff(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0), 1))
def cg_f063_return_on_assets_core107_diff_1q_v108_signal(netinc, assetsavg):
    return _clean(_diff(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 1))
def cg_f063_return_on_assets_core108_diff_1q_v109_signal(netinc, assetsavg):
    return _clean(_diff(_safe_div(netinc, assetsavg).abs(), 1))
def cg_f063_return_on_assets_core109_diff_1q_v110_signal(netinc, assetsavg):
    return _clean(_diff(_safe_div(netinc, assetsavg * 0.5 + 1.0), 1))

# core110-119: slope 4q
def cg_f063_return_on_assets_core110_slope_4q_v111_signal(netinc, assetsavg):
    return _clean(_slope(netinc, 4))
def cg_f063_return_on_assets_core111_slope_4q_v112_signal(netinc, assetsavg):
    return _clean(_slope(_safe_div(netinc, assetsavg), 4))
def cg_f063_return_on_assets_core112_slope_4q_v113_signal(netinc, assetsavg):
    return _clean(_slope(assetsavg, 4))
def cg_f063_return_on_assets_core113_slope_4q_v114_signal(netinc, assetsavg):
    return _clean(_slope(_safe_div(netinc, assetsavg.abs() + 1.0), 4))
def cg_f063_return_on_assets_core114_slope_4q_v115_signal(netinc, assetsavg):
    return _clean(_slope(netinc - _mean(netinc, 4), 4))
def cg_f063_return_on_assets_core115_slope_4q_v116_signal(netinc, assetsavg):
    return _clean(_slope(assetsavg - _mean(assetsavg, 4), 4))
def cg_f063_return_on_assets_core116_slope_4q_v117_signal(netinc, assetsavg):
    return _clean(_slope(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0), 4))
def cg_f063_return_on_assets_core117_slope_4q_v118_signal(netinc, assetsavg):
    return _clean(_slope(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 4))
def cg_f063_return_on_assets_core118_slope_4q_v119_signal(netinc, assetsavg):
    return _clean(_slope(_safe_div(netinc, assetsavg).abs(), 4))
def cg_f063_return_on_assets_core119_slope_4q_v120_signal(netinc, assetsavg):
    return _clean(_slope(_safe_div(netinc, assetsavg * 0.5 + 1.0), 4))

# core120-129: ewm 8q
def cg_f063_return_on_assets_core120_ewm_8q_v121_signal(netinc, assetsavg):
    return _clean(_ewm(netinc, 8))
def cg_f063_return_on_assets_core121_ewm_8q_v122_signal(netinc, assetsavg):
    return _clean(_ewm(_safe_div(netinc, assetsavg), 8))
def cg_f063_return_on_assets_core122_ewm_8q_v123_signal(netinc, assetsavg):
    return _clean(_ewm(assetsavg, 8))
def cg_f063_return_on_assets_core123_ewm_8q_v124_signal(netinc, assetsavg):
    return _clean(_ewm(_safe_div(netinc, assetsavg.abs() + 1.0), 8))
def cg_f063_return_on_assets_core124_ewm_8q_v125_signal(netinc, assetsavg):
    return _clean(_ewm(netinc - _mean(netinc, 4), 8))
def cg_f063_return_on_assets_core125_ewm_8q_v126_signal(netinc, assetsavg):
    return _clean(_ewm(assetsavg - _mean(assetsavg, 4), 8))
def cg_f063_return_on_assets_core126_ewm_8q_v127_signal(netinc, assetsavg):
    return _clean(_ewm(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0), 8))
def cg_f063_return_on_assets_core127_ewm_8q_v128_signal(netinc, assetsavg):
    return _clean(_ewm(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 8))
def cg_f063_return_on_assets_core128_ewm_8q_v129_signal(netinc, assetsavg):
    return _clean(_ewm(_safe_div(netinc, assetsavg).abs(), 8))
def cg_f063_return_on_assets_core129_ewm_8q_v130_signal(netinc, assetsavg):
    return _clean(_ewm(_safe_div(netinc, assetsavg * 0.5 + 1.0), 8))

# core130-139: stability 12q
def cg_f063_return_on_assets_core130_stability_12q_v131_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(netinc, 12), _mean(netinc, 12)))
def cg_f063_return_on_assets_core131_stability_12q_v132_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(_safe_div(netinc, assetsavg), 12), _mean(_safe_div(netinc, assetsavg), 12)))
def cg_f063_return_on_assets_core132_stability_12q_v133_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(assetsavg, 12), _mean(assetsavg, 12)))
def cg_f063_return_on_assets_core133_stability_12q_v134_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(_safe_div(netinc, assetsavg.abs() + 1.0), 12), _mean(_safe_div(netinc, assetsavg.abs() + 1.0), 12)))
def cg_f063_return_on_assets_core134_stability_12q_v135_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(netinc - _mean(netinc, 4), 12), _mean(netinc - _mean(netinc, 4), 12).abs() + 1.0))
def cg_f063_return_on_assets_core135_stability_12q_v136_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(assetsavg - _mean(assetsavg, 4), 12), _mean(assetsavg - _mean(assetsavg, 4), 12).abs() + 1.0))
def cg_f063_return_on_assets_core136_stability_12q_v137_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0), 12), _mean(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0), 12).abs() + 1.0))
def cg_f063_return_on_assets_core137_stability_12q_v138_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 12), _mean(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 12).abs() + 1.0))
def cg_f063_return_on_assets_core138_stability_12q_v139_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(_safe_div(netinc, assetsavg).abs(), 12), _mean(_safe_div(netinc, assetsavg).abs(), 12).abs() + 1.0))
def cg_f063_return_on_assets_core139_stability_12q_v140_signal(netinc, assetsavg):
    return _clean(_safe_div(_std(_safe_div(netinc, assetsavg * 0.5 + 1.0), 12), _mean(_safe_div(netinc, assetsavg * 0.5 + 1.0), 12).abs() + 1.0))

# core140-149: raw variations
def cg_f063_return_on_assets_core140_raw_v141_signal(netinc, assetsavg):
    return _clean(netinc)
def cg_f063_return_on_assets_core141_raw_v142_signal(netinc, assetsavg):
    return _clean(_safe_div(netinc, assetsavg))
def cg_f063_return_on_assets_core142_raw_v143_signal(netinc, assetsavg):
    return _clean(assetsavg)
def cg_f063_return_on_assets_core143_raw_v144_signal(netinc, assetsavg):
    return _clean(_safe_div(netinc, assetsavg.abs() + 1.0))
def cg_f063_return_on_assets_core144_raw_v145_signal(netinc, assetsavg):
    return _clean(netinc - _mean(netinc, 4))
def cg_f063_return_on_assets_core145_raw_v146_signal(netinc, assetsavg):
    return _clean(assetsavg - _mean(assetsavg, 4))
def cg_f063_return_on_assets_core146_raw_v147_signal(netinc, assetsavg):
    return _clean(_safe_div(netinc - _mean(netinc, 4), assetsavg.abs() + 1.0))
def cg_f063_return_on_assets_core147_raw_v148_signal(netinc, assetsavg):
    return _clean(_safe_div(netinc, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0))
def cg_f063_return_on_assets_core148_raw_v149_signal(netinc, assetsavg):
    return _clean(_safe_div(netinc, assetsavg).abs())
def cg_f063_return_on_assets_core149_raw_v150_signal(netinc, assetsavg):
    return _clean(_safe_div(netinc, assetsavg * 0.5 + 1.0))
