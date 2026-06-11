import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: pct 4q (continued)
def cg_f011_financing_cash_flow_core75_pct_4q_v076_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncff, ncfo.abs() + 1.0), 4))
def cg_f011_financing_cash_flow_core76_pct_4q_v077_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncff, assets), 4))
def cg_f011_financing_cash_flow_core77_pct_4q_v078_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncfinv, assets), 4))
def cg_f011_financing_cash_flow_core78_pct_4q_v079_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncfbus, assets), 4))
def cg_f011_financing_cash_flow_core79_pct_4q_v080_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_pct_change(_safe_div(ncff, marketcap), 4))

# core80-89: std 8q
def cg_f011_financing_cash_flow_core80_std_8q_v081_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(ncff, 8))
def cg_f011_financing_cash_flow_core81_std_8q_v082_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(ncfinv, 8))
def cg_f011_financing_cash_flow_core82_std_8q_v083_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(ncfbus, 8))
def cg_f011_financing_cash_flow_core83_std_8q_v084_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(debt, 8))
def cg_f011_financing_cash_flow_core84_std_8q_v085_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(dps, 8))
def cg_f011_financing_cash_flow_core85_std_8q_v086_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f011_financing_cash_flow_core86_std_8q_v087_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(_safe_div(ncff, assets), 8))
def cg_f011_financing_cash_flow_core87_std_8q_v088_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(_safe_div(ncfinv, assets), 8))
def cg_f011_financing_cash_flow_core88_std_8q_v089_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(_safe_div(ncfbus, assets), 8))
def cg_f011_financing_cash_flow_core89_std_8q_v090_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_std(_safe_div(ncff, marketcap), 8))

# core90-99: log
def cg_f011_financing_cash_flow_core90_log_v091_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(ncff.clip(lower=1.0)))
def cg_f011_financing_cash_flow_core91_log_v092_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(ncfinv.clip(lower=1.0)))
def cg_f011_financing_cash_flow_core92_log_v093_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(ncfbus.clip(lower=1.0)))
def cg_f011_financing_cash_flow_core93_log_v094_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(debt.clip(lower=1.0)))
def cg_f011_financing_cash_flow_core94_log_v095_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(dps.clip(lower=1.0)))
def cg_f011_financing_cash_flow_core95_log_v096_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(_safe_div(ncff, assets).clip(lower=0.001)))
def cg_f011_financing_cash_flow_core96_log_v097_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(_safe_div(ncfinv, assets).clip(lower=0.001)))
def cg_f011_financing_cash_flow_core97_log_v098_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(_safe_div(ncfbus, assets).clip(lower=0.001)))
def cg_f011_financing_cash_flow_core98_log_v099_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(_safe_div(ncff, marketcap).clip(lower=0.001)))
def cg_f011_financing_cash_flow_core99_log_v100_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_log(_safe_div(ncff, ncfo.abs() + 1.0).clip(lower=0.001)))

# core100-109: diff 1q
def cg_f011_financing_cash_flow_core100_diff_1q_v101_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(ncff, 1))
def cg_f011_financing_cash_flow_core101_diff_1q_v102_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(ncfinv, 1))
def cg_f011_financing_cash_flow_core102_diff_1q_v103_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(ncfbus, 1))
def cg_f011_financing_cash_flow_core103_diff_1q_v104_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(debt, 1))
def cg_f011_financing_cash_flow_core104_diff_1q_v105_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(dps, 1))
def cg_f011_financing_cash_flow_core105_diff_1q_v106_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(_safe_div(ncff, ncfo.abs() + 1.0), 1))
def cg_f011_financing_cash_flow_core106_diff_1q_v107_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(_safe_div(ncff, assets), 1))
def cg_f011_financing_cash_flow_core107_diff_1q_v108_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(_safe_div(ncfinv, assets), 1))
def cg_f011_financing_cash_flow_core108_diff_1q_v109_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(_safe_div(ncfbus, assets), 1))
def cg_f011_financing_cash_flow_core109_diff_1q_v110_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_diff(_safe_div(ncff, marketcap), 1))

# core110-119: slope 4q
def cg_f011_financing_cash_flow_core110_slope_4q_v111_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(ncff, 4))
def cg_f011_financing_cash_flow_core111_slope_4q_v112_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(ncfinv, 4))
def cg_f011_financing_cash_flow_core112_slope_4q_v113_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(ncfbus, 4))
def cg_f011_financing_cash_flow_core113_slope_4q_v114_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(debt, 4))
def cg_f011_financing_cash_flow_core114_slope_4q_v115_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(dps, 4))
def cg_f011_financing_cash_flow_core115_slope_4q_v116_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(_safe_div(ncff, ncfo.abs() + 1.0), 4))
def cg_f011_financing_cash_flow_core116_slope_4q_v117_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(_safe_div(ncff, assets), 4))
def cg_f011_financing_cash_flow_core117_slope_4q_v118_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(_safe_div(ncfinv, assets), 4))
def cg_f011_financing_cash_flow_core118_slope_4q_v119_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(_safe_div(ncfbus, assets), 4))
def cg_f011_financing_cash_flow_core119_slope_4q_v120_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_slope(_safe_div(ncff, marketcap), 4))

# core120-129: ewm 8q
def cg_f011_financing_cash_flow_core120_ewm_8q_v121_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(ncff, 8))
def cg_f011_financing_cash_flow_core121_ewm_8q_v122_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(ncfinv, 8))
def cg_f011_financing_cash_flow_core122_ewm_8q_v123_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(ncfbus, 8))
def cg_f011_financing_cash_flow_core123_ewm_8q_v124_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(debt, 8))
def cg_f011_financing_cash_flow_core124_ewm_8q_v125_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(dps, 8))
def cg_f011_financing_cash_flow_core125_ewm_8q_v126_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(_safe_div(ncff, ncfo.abs() + 1.0), 8))
def cg_f011_financing_cash_flow_core126_ewm_8q_v127_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(_safe_div(ncff, assets), 8))
def cg_f011_financing_cash_flow_core127_ewm_8q_v128_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(_safe_div(ncfinv, assets), 8))
def cg_f011_financing_cash_flow_core128_ewm_8q_v129_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(_safe_div(ncfbus, assets), 8))
def cg_f011_financing_cash_flow_core129_ewm_8q_v130_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_ewm(_safe_div(ncff, marketcap), 8))

# core130-139: stability 12q
def cg_f011_financing_cash_flow_core130_stability_12q_v131_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_safe_div(_std(ncff, 12), _mean(ncff, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core131_stability_12q_v132_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(ncff, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core132_stability_12q_v133_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(ncfinv, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core133_stability_12q_v134_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(ncfbus, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core134_stability_12q_v135_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(debt, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core135_stability_12q_v136_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(dps, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core136_stability_12q_v137_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(ncff, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core137_stability_12q_v138_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = _safe_div(ncff, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core138_stability_12q_v139_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = debt
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f011_financing_cash_flow_core139_stability_12q_v140_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    base = dps
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# core140-149: raw levels (optimized)
def cg_f011_financing_cash_flow_core140_ncff_v141_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(ncff)
def cg_f011_financing_cash_flow_core141_ncfinv_v142_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(ncfinv)
def cg_f011_financing_cash_flow_core142_ncfbus_v143_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(ncfbus)
def cg_f011_financing_cash_flow_core143_debt_v144_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(debt)
def cg_f011_financing_cash_flow_core144_dps_v145_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(dps)
def cg_f011_financing_cash_flow_core145_ncff_assets_v146_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_safe_div(ncff, assets))
def cg_f011_financing_cash_flow_core146_ncff_mcap_v147_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_safe_div(ncff, marketcap))
def cg_f011_financing_cash_flow_core147_ncff_ncfo_v148_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_safe_div(ncff, ncfo.abs() + 1.0))
def cg_f011_financing_cash_flow_core148_ncfinv_assets_v149_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_safe_div(ncfinv, assets))
def cg_f011_financing_cash_flow_core149_ncfbus_assets_v150_signal(ncff, ncfinv, ncfbus, debt, dps, ncfo, assets, marketcap):
    return _clean(_safe_div(ncfbus, assets))
