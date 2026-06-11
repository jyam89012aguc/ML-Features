import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f036_sbc_dilution_pressure_core75_pct_4q_v076_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_pct_change(_safe_div(sbc, sharesbas), 4))
def cg_f036_sbc_dilution_pressure_core76_pct_4q_v077_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_pct_change(_safe_div(sbc, assets), 4))
def cg_f036_sbc_dilution_pressure_core77_pct_4q_v078_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_pct_change(_pct_change(sbc, 4), 4))
def cg_f036_sbc_dilution_pressure_core78_pct_4q_v079_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_pct_change(_diff(sbc, 1), 4))
def cg_f036_sbc_dilution_pressure_core79_pct_4q_v080_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_pct_change(_log(sbc.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f036_sbc_dilution_pressure_core80_std_8q_v081_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, marketcap), 8))
def cg_f036_sbc_dilution_pressure_core81_std_8q_v082_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, ncfo.abs() + 1.0), 8))
def cg_f036_sbc_dilution_pressure_core82_std_8q_v083_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f036_sbc_dilution_pressure_core83_std_8q_v084_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, revenue), 8))
def cg_f036_sbc_dilution_pressure_core84_std_8q_v085_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f036_sbc_dilution_pressure_core85_std_8q_v086_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, sharesbas), 8))
def cg_f036_sbc_dilution_pressure_core86_std_8q_v087_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_safe_div(sbc, assets), 8))
def cg_f036_sbc_dilution_pressure_core87_std_8q_v088_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_pct_change(sbc, 4), 8))
def cg_f036_sbc_dilution_pressure_core88_std_8q_v089_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_diff(sbc, 1), 8))
def cg_f036_sbc_dilution_pressure_core89_std_8q_v090_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_std(_log(sbc.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f036_sbc_dilution_pressure_core90_log_v091_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(sbc.clip(lower=1.0)))
def cg_f036_sbc_dilution_pressure_core91_log_v092_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, marketcap).clip(lower=0.0001)))
def cg_f036_sbc_dilution_pressure_core92_log_v093_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f036_sbc_dilution_pressure_core93_log_v094_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, netinc.abs() + 1.0).clip(lower=0.001)))
def cg_f036_sbc_dilution_pressure_core94_log_v095_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, revenue).clip(lower=0.0001)))
def cg_f036_sbc_dilution_pressure_core95_log_v096_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, sharesbas).clip(lower=0.001)))
def cg_f036_sbc_dilution_pressure_core96_log_v097_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, assets).clip(lower=0.0001)))
def cg_f036_sbc_dilution_pressure_core97_log_v098_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_safe_div(sbc, opex.abs() + 1.0).clip(lower=0.001)))
def cg_f036_sbc_dilution_pressure_core98_log_v099_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(_pct_change(sbc, 4).clip(lower=-0.9) + 1.1))
def cg_f036_sbc_dilution_pressure_core99_log_v100_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(marketcap.clip(lower=1.0)))

# Block 100-109: diff 1q
def cg_f036_sbc_dilution_pressure_core100_diff_1q_v101_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, marketcap), 1))
def cg_f036_sbc_dilution_pressure_core101_diff_1q_v102_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, ncfo.abs() + 1.0), 1))
def cg_f036_sbc_dilution_pressure_core102_diff_1q_v103_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, netinc.abs() + 1.0), 1))
def cg_f036_sbc_dilution_pressure_core103_diff_1q_v104_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, revenue), 1))
def cg_f036_sbc_dilution_pressure_core104_diff_1q_v105_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, opex.abs() + 1.0), 1))
def cg_f036_sbc_dilution_pressure_core105_diff_1q_v106_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, sharesbas), 1))
def cg_f036_sbc_dilution_pressure_core106_diff_1q_v107_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_safe_div(sbc, assets), 1))
def cg_f036_sbc_dilution_pressure_core107_diff_1q_v108_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_pct_change(sbc, 4), 1))
def cg_f036_sbc_dilution_pressure_core108_diff_1q_v109_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(sbc, 1))
def cg_f036_sbc_dilution_pressure_core109_diff_1q_v110_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(_log(sbc.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f036_sbc_dilution_pressure_core110_slope_4q_v111_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, marketcap), 4))
def cg_f036_sbc_dilution_pressure_core111_slope_4q_v112_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, ncfo.abs() + 1.0), 4))
def cg_f036_sbc_dilution_pressure_core112_slope_4q_v113_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, netinc.abs() + 1.0), 4))
def cg_f036_sbc_dilution_pressure_core113_slope_4q_v114_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, revenue), 4))
def cg_f036_sbc_dilution_pressure_core114_slope_4q_v115_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, opex.abs() + 1.0), 4))
def cg_f036_sbc_dilution_pressure_core115_slope_4q_v116_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, sharesbas), 4))
def cg_f036_sbc_dilution_pressure_core116_slope_4q_v117_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_safe_div(sbc, assets), 4))
def cg_f036_sbc_dilution_pressure_core117_slope_4q_v118_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_pct_change(sbc, 4), 4))
def cg_f036_sbc_dilution_pressure_core118_slope_4q_v119_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(sbc, 4))
def cg_f036_sbc_dilution_pressure_core119_slope_4q_v120_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_slope(_log(sbc.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f036_sbc_dilution_pressure_core120_ewm_8q_v121_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, marketcap), 8))
def cg_f036_sbc_dilution_pressure_core121_ewm_8q_v122_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, ncfo.abs() + 1.0), 8))
def cg_f036_sbc_dilution_pressure_core122_ewm_8q_v123_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, netinc.abs() + 1.0), 8))
def cg_f036_sbc_dilution_pressure_core123_ewm_8q_v124_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, revenue), 8))
def cg_f036_sbc_dilution_pressure_core124_ewm_8q_v125_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, opex.abs() + 1.0), 8))
def cg_f036_sbc_dilution_pressure_core125_ewm_8q_v126_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, sharesbas), 8))
def cg_f036_sbc_dilution_pressure_core126_ewm_8q_v127_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_safe_div(sbc, assets), 8))
def cg_f036_sbc_dilution_pressure_core127_ewm_8q_v128_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_pct_change(sbc, 4), 8))
def cg_f036_sbc_dilution_pressure_core128_ewm_8q_v129_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(sbc, 8))
def cg_f036_sbc_dilution_pressure_core129_ewm_8q_v130_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_ewm(_log(sbc.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f036_sbc_dilution_pressure_core130_stability_12q_v131_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core131_stability_12q_v132_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core132_stability_12q_v133_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, netinc.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core133_stability_12q_v134_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core134_stability_12q_v135_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, opex.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core135_stability_12q_v136_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core136_stability_12q_v137_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _safe_div(sbc, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core137_stability_12q_v138_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _pct_change(sbc, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core138_stability_12q_v139_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = sbc
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core139_stability_12q_v140_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    base = _log(sbc.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f036_sbc_dilution_pressure_core140_dil_yield_v141_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, marketcap))
def cg_f036_sbc_dilution_pressure_core141_dil_ncfo_v142_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, ncfo.abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core142_dil_ni_v143_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, netinc.abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core143_dil_rev_v144_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, revenue))
def cg_f036_sbc_dilution_pressure_core144_dil_opex_v145_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, opex.abs() + 1.0))
def cg_f036_sbc_dilution_pressure_core145_dil_shares_v146_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, sharesbas))
def cg_f036_sbc_dilution_pressure_core146_dil_assets_v147_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_safe_div(sbc, assets))
def cg_f036_sbc_dilution_pressure_core147_dil_growth_v148_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_pct_change(sbc, 4))
def cg_f036_sbc_dilution_pressure_core148_sbc_diff_v149_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_diff(sbc, 1))
def cg_f036_sbc_dilution_pressure_core149_sbc_log_v150_signal(sbc, sharesbas, marketcap, netinc, revenue, ncfo, assets, opex):
    return _clean(_log(sbc.clip(lower=1.0)))
