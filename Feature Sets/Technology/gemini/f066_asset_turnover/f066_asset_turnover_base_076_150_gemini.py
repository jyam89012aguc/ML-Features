import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f066_asset_turnover_core75_pct_4q_v076_signal(revenue, assetsavg):
    return _clean(_pct_change(assetsavg - _mean(assetsavg, 4), 4))
def cg_f066_asset_turnover_core76_pct_4q_v077_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 4))
def cg_f066_asset_turnover_core77_pct_4q_v078_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 4))
def cg_f066_asset_turnover_core78_pct_4q_v079_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg).abs(), 4))
def cg_f066_asset_turnover_core79_pct_4q_v080_signal(revenue, assetsavg):
    return _clean(_pct_change(_safe_div(revenue, assetsavg * 0.5 + 1.0), 4))

# core80-89: std 8q
def cg_f066_asset_turnover_core80_std_8q_v081_signal(revenue, assetsavg):
    return _clean(_std(revenue, 8))
def cg_f066_asset_turnover_core81_std_8q_v082_signal(revenue, assetsavg):
    return _clean(_std(_safe_div(revenue, assetsavg), 8))
def cg_f066_asset_turnover_core82_std_8q_v083_signal(revenue, assetsavg):
    return _clean(_std(assetsavg, 8))
def cg_f066_asset_turnover_core83_std_8q_v084_signal(revenue, assetsavg):
    return _clean(_std(_safe_div(revenue, assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core84_std_8q_v085_signal(revenue, assetsavg):
    return _clean(_std(revenue - _mean(revenue, 8), 8))
def cg_f066_asset_turnover_core85_std_8q_v086_signal(revenue, assetsavg):
    return _clean(_std(assetsavg - _mean(assetsavg, 8), 8))
def cg_f066_asset_turnover_core86_std_8q_v087_signal(revenue, assetsavg):
    return _clean(_std(_safe_div(revenue - _mean(revenue, 8), assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core87_std_8q_v088_signal(revenue, assetsavg):
    return _clean(_std(_safe_div(revenue, (assetsavg - _mean(assetsavg, 8)).abs() + 1.0), 8))
def cg_f066_asset_turnover_core88_std_8q_v089_signal(revenue, assetsavg):
    return _clean(_std(_safe_div(revenue, assetsavg).abs(), 8))
def cg_f066_asset_turnover_core89_std_8q_v090_signal(revenue, assetsavg):
    return _clean(_std(_safe_div(revenue, assetsavg * 0.5 + 1.0), 8))

# core90-99: log
def cg_f066_asset_turnover_core90_log_v091_signal(revenue, assetsavg):
    return _clean(_log(revenue.abs() + 1.0))
def cg_f066_asset_turnover_core91_log_v092_signal(revenue, assetsavg):
    return _clean(_log(_safe_div(revenue, assetsavg).abs() + 1.0))
def cg_f066_asset_turnover_core92_log_v093_signal(revenue, assetsavg):
    return _clean(_log(assetsavg.abs() + 1.0))
def cg_f066_asset_turnover_core93_log_v094_signal(revenue, assetsavg):
    return _clean(_log(_safe_div(revenue, assetsavg.abs() + 1.0).abs() + 1.0))
def cg_f066_asset_turnover_core94_log_v095_signal(revenue, assetsavg):
    return _clean(_log((revenue - _mean(revenue, 4)).abs() + 1.0))
def cg_f066_asset_turnover_core95_log_v096_signal(revenue, assetsavg):
    return _clean(_log((assetsavg - _mean(assetsavg, 4)).abs() + 1.0))
def cg_f066_asset_turnover_core96_log_v097_signal(revenue, assetsavg):
    return _clean(_log(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0).abs() + 1.0))
def cg_f066_asset_turnover_core97_log_v098_signal(revenue, assetsavg):
    return _clean(_log(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0).abs() + 1.0))
def cg_f066_asset_turnover_core98_log_v099_signal(revenue, assetsavg):
    return _clean(_log(_safe_div(revenue, assetsavg).abs() + 1.0))
def cg_f066_asset_turnover_core99_log_v100_signal(revenue, assetsavg):
    return _clean(_log(_safe_div(revenue, assetsavg * 0.5 + 1.0).abs() + 1.0))

# core100-109: diff 1q
def cg_f066_asset_turnover_core100_diff_1q_v101_signal(revenue, assetsavg):
    return _clean(_diff(revenue, 1))
def cg_f066_asset_turnover_core101_diff_1q_v102_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, assetsavg), 1))
def cg_f066_asset_turnover_core102_diff_1q_v103_signal(revenue, assetsavg):
    return _clean(_diff(assetsavg, 1))
def cg_f066_asset_turnover_core103_diff_1q_v104_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, assetsavg.abs() + 1.0), 1))
def cg_f066_asset_turnover_core104_diff_1q_v105_signal(revenue, assetsavg):
    return _clean(_diff(revenue - _mean(revenue, 4), 1))
def cg_f066_asset_turnover_core105_diff_1q_v106_signal(revenue, assetsavg):
    return _clean(_diff(assetsavg - _mean(assetsavg, 4), 1))
def cg_f066_asset_turnover_core106_diff_1q_v107_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 1))
def cg_f066_asset_turnover_core107_diff_1q_v108_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 1))
def cg_f066_asset_turnover_core108_diff_1q_v109_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, assetsavg).abs(), 1))
def cg_f066_asset_turnover_core109_diff_1q_v110_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, assetsavg * 0.5 + 1.0), 1))

# core110-119: slope 4q
def cg_f066_asset_turnover_core110_slope_4q_v111_signal(revenue, assetsavg):
    return _clean(_slope(revenue, 4))
def cg_f066_asset_turnover_core111_slope_4q_v112_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, assetsavg), 4))
def cg_f066_asset_turnover_core112_slope_4q_v113_signal(revenue, assetsavg):
    return _clean(_slope(assetsavg, 4))
def cg_f066_asset_turnover_core113_slope_4q_v114_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, assetsavg.abs() + 1.0), 4))
def cg_f066_asset_turnover_core114_slope_4q_v115_signal(revenue, assetsavg):
    return _clean(_slope(revenue - _mean(revenue, 4), 4))
def cg_f066_asset_turnover_core115_slope_4q_v116_signal(revenue, assetsavg):
    return _clean(_slope(assetsavg - _mean(assetsavg, 4), 4))
def cg_f066_asset_turnover_core116_slope_4q_v117_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 4))
def cg_f066_asset_turnover_core117_slope_4q_v118_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 4))
def cg_f066_asset_turnover_core118_slope_4q_v119_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, assetsavg).abs(), 4))
def cg_f066_asset_turnover_core119_slope_4q_v120_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, assetsavg * 0.5 + 1.0), 4))

# core120-129: ewm 8q
def cg_f066_asset_turnover_core120_ewm_8q_v121_signal(revenue, assetsavg):
    return _clean(_ewm(revenue, 8))
def cg_f066_asset_turnover_core121_ewm_8q_v122_signal(revenue, assetsavg):
    return _clean(_ewm(_safe_div(revenue, assetsavg), 8))
def cg_f066_asset_turnover_core122_ewm_8q_v123_signal(revenue, assetsavg):
    return _clean(_ewm(assetsavg, 8))
def cg_f066_asset_turnover_core123_ewm_8q_v124_signal(revenue, assetsavg):
    return _clean(_ewm(_safe_div(revenue, assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core124_ewm_8q_v125_signal(revenue, assetsavg):
    return _clean(_ewm(revenue - _mean(revenue, 4), 8))
def cg_f066_asset_turnover_core125_ewm_8q_v126_signal(revenue, assetsavg):
    return _clean(_ewm(assetsavg - _mean(assetsavg, 4), 8))
def cg_f066_asset_turnover_core126_ewm_8q_v127_signal(revenue, assetsavg):
    return _clean(_ewm(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 8))
def cg_f066_asset_turnover_core127_ewm_8q_v128_signal(revenue, assetsavg):
    return _clean(_ewm(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 8))
def cg_f066_asset_turnover_core128_ewm_8q_v129_signal(revenue, assetsavg):
    return _clean(_ewm(_safe_div(revenue, assetsavg).abs(), 8))
def cg_f066_asset_turnover_core129_ewm_8q_v130_signal(revenue, assetsavg):
    return _clean(_ewm(_safe_div(revenue, assetsavg * 0.5 + 1.0), 8))

# core130-139: stability 12q
def cg_f066_asset_turnover_core130_stability_12q_v131_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(revenue, 12), _mean(revenue, 12).abs() + 1.0))
def cg_f066_asset_turnover_core131_stability_12q_v132_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(_safe_div(revenue, assetsavg), 12), _mean(_safe_div(revenue, assetsavg), 12).abs() + 1.0))
def cg_f066_asset_turnover_core132_stability_12q_v133_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(assetsavg, 12), _mean(assetsavg, 12).abs() + 1.0))
def cg_f066_asset_turnover_core133_stability_12q_v134_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(_safe_div(revenue, assetsavg.abs() + 1.0), 12), _mean(_safe_div(revenue, assetsavg.abs() + 1.0), 12).abs() + 1.0))
def cg_f066_asset_turnover_core134_stability_12q_v135_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(revenue - _mean(revenue, 4), 12), _mean(revenue - _mean(revenue, 4), 12).abs() + 1.0))
def cg_f066_asset_turnover_core135_stability_12q_v136_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(assetsavg - _mean(assetsavg, 4), 12), _mean(assetsavg - _mean(assetsavg, 4), 12).abs() + 1.0))
def cg_f066_asset_turnover_core136_stability_12q_v137_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 12), _mean(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0), 12).abs() + 1.0))
def cg_f066_asset_turnover_core137_stability_12q_v138_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 12), _mean(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0), 12).abs() + 1.0))
def cg_f066_asset_turnover_core138_stability_12q_v139_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(_safe_div(revenue, assetsavg).abs(), 12), _mean(_safe_div(revenue, assetsavg).abs(), 12).abs() + 1.0))
def cg_f066_asset_turnover_core139_stability_12q_v140_signal(revenue, assetsavg):
    return _clean(_safe_div(_std(_safe_div(revenue, assetsavg * 0.5 + 1.0), 12), _mean(_safe_div(revenue, assetsavg * 0.5 + 1.0), 12).abs() + 1.0))

# core140-149: raw variations
def cg_f066_asset_turnover_core140_raw_v141_signal(revenue, assetsavg):
    return _clean(revenue)
def cg_f066_asset_turnover_core141_raw_v142_signal(revenue, assetsavg):
    return _clean(_safe_div(revenue, assetsavg))
def cg_f066_asset_turnover_core142_raw_v143_signal(revenue, assetsavg):
    return _clean(assetsavg)
def cg_f066_asset_turnover_core143_raw_v144_signal(revenue, assetsavg):
    return _clean(_safe_div(revenue, assetsavg.abs() + 1.0))
def cg_f066_asset_turnover_core144_raw_v145_signal(revenue, assetsavg):
    return _clean(revenue - _mean(revenue, 4))
def cg_f066_asset_turnover_core145_raw_v146_signal(revenue, assetsavg):
    return _clean(assetsavg - _mean(assetsavg, 4))
def cg_f066_asset_turnover_core146_raw_v147_signal(revenue, assetsavg):
    return _clean(_safe_div(revenue - _mean(revenue, 4), assetsavg.abs() + 1.0))
def cg_f066_asset_turnover_core147_raw_v148_signal(revenue, assetsavg):
    return _clean(_safe_div(revenue, (assetsavg - _mean(assetsavg, 4)).abs() + 1.0))
def cg_f066_asset_turnover_core148_raw_v149_signal(revenue, assetsavg):
    return _clean(_safe_div(revenue, assetsavg).abs())
def cg_f066_asset_turnover_core149_raw_v150_signal(revenue, assetsavg):
    return _clean(_safe_div(revenue, assetsavg * 0.5 + 1.0))
