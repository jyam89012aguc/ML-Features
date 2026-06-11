import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f033_equity_issuance_cash_core75_pct_4q_v076_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, equity.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core76_pct_4q_v077_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, sharesbas), 4))
def cg_f033_equity_issuance_cash_core77_pct_4q_v078_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core78_pct_4q_v079_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_pct_change(ncfbus, 4), 4))
def cg_f033_equity_issuance_cash_core79_pct_4q_v080_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(_log(ncfbus.clip(lower=1.0)), 4))

# Block 80-89: std 8q
def cg_f033_equity_issuance_cash_core80_std_8q_v081_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(ncfbus, 8))
def cg_f033_equity_issuance_cash_core81_std_8q_v082_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, assets), 8))
def cg_f033_equity_issuance_cash_core82_std_8q_v083_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, revenue), 8))
def cg_f033_equity_issuance_cash_core83_std_8q_v084_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, marketcap), 8))
def cg_f033_equity_issuance_cash_core84_std_8q_v085_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core85_std_8q_v086_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, equity.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core86_std_8q_v087_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, sharesbas), 8))
def cg_f033_equity_issuance_cash_core87_std_8q_v088_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core88_std_8q_v089_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_pct_change(ncfbus, 4), 8))
def cg_f033_equity_issuance_cash_core89_std_8q_v090_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_std(_log(ncfbus.clip(lower=1.0)), 8))

# Block 90-99: log
def cg_f033_equity_issuance_cash_core90_log_v091_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(ncfbus.clip(lower=1.0)))
def cg_f033_equity_issuance_cash_core91_log_v092_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, assets).clip(lower=0.0001)))
def cg_f033_equity_issuance_cash_core92_log_v093_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, revenue).clip(lower=0.0001)))
def cg_f033_equity_issuance_cash_core93_log_v094_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, marketcap).clip(lower=0.0001)))
def cg_f033_equity_issuance_cash_core94_log_v095_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f033_equity_issuance_cash_core95_log_v096_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, equity.abs() + 1.0).clip(lower=0.001)))
def cg_f033_equity_issuance_cash_core96_log_v097_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, sharesbas).clip(lower=0.001)))
def cg_f033_equity_issuance_cash_core97_log_v098_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0).clip(lower=0.001)))
def cg_f033_equity_issuance_cash_core98_log_v099_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_pct_change(ncfbus, 4).clip(lower=-0.9) + 1.1))
def cg_f033_equity_issuance_cash_core99_log_v100_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(_safe_div(ncfbus, assets).clip(lower=0.0001)))

# Block 100-109: diff 1q
def cg_f033_equity_issuance_cash_core100_diff_1q_v101_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(ncfbus, 1))
def cg_f033_equity_issuance_cash_core101_diff_1q_v102_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, assets), 1))
def cg_f033_equity_issuance_cash_core102_diff_1q_v103_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, revenue), 1))
def cg_f033_equity_issuance_cash_core103_diff_1q_v104_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, marketcap), 1))
def cg_f033_equity_issuance_cash_core104_diff_1q_v105_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, ncfo.abs() + 1.0), 1))
def cg_f033_equity_issuance_cash_core105_diff_1q_v106_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, equity.abs() + 1.0), 1))
def cg_f033_equity_issuance_cash_core106_diff_1q_v107_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, sharesbas), 1))
def cg_f033_equity_issuance_cash_core107_diff_1q_v108_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 1))
def cg_f033_equity_issuance_cash_core108_diff_1q_v109_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_pct_change(ncfbus, 4), 1))
def cg_f033_equity_issuance_cash_core109_diff_1q_v110_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_diff(_log(ncfbus.clip(lower=1.0)), 1))

# Block 110-119: slope 4q
def cg_f033_equity_issuance_cash_core110_slope_4q_v111_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(ncfbus, 4))
def cg_f033_equity_issuance_cash_core111_slope_4q_v112_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, assets), 4))
def cg_f033_equity_issuance_cash_core112_slope_4q_v113_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, revenue), 4))
def cg_f033_equity_issuance_cash_core113_slope_4q_v114_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, marketcap), 4))
def cg_f033_equity_issuance_cash_core114_slope_4q_v115_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, ncfo.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core115_slope_4q_v116_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, equity.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core116_slope_4q_v117_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, sharesbas), 4))
def cg_f033_equity_issuance_cash_core117_slope_4q_v118_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core118_slope_4q_v119_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_pct_change(ncfbus, 4), 4))
def cg_f033_equity_issuance_cash_core119_slope_4q_v120_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_slope(_log(ncfbus.clip(lower=1.0)), 4))

# Block 120-129: ewm 8q
def cg_f033_equity_issuance_cash_core120_ewm_8q_v121_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(ncfbus, 8))
def cg_f033_equity_issuance_cash_core121_ewm_8q_v122_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, assets), 8))
def cg_f033_equity_issuance_cash_core122_ewm_8q_v123_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, revenue), 8))
def cg_f033_equity_issuance_cash_core123_ewm_8q_v124_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, marketcap), 8))
def cg_f033_equity_issuance_cash_core124_ewm_8q_v125_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core125_ewm_8q_v126_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, equity.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core126_ewm_8q_v127_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, sharesbas), 8))
def cg_f033_equity_issuance_cash_core127_ewm_8q_v128_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core128_ewm_8q_v129_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_pct_change(ncfbus, 4), 8))
def cg_f033_equity_issuance_cash_core129_ewm_8q_v130_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_ewm(_log(ncfbus.clip(lower=1.0)), 8))

# Block 130-139: stability 12q
def cg_f033_equity_issuance_cash_core130_stability_12q_v131_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(_std(ncfbus, 12), _mean(ncfbus, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core131_stability_12q_v132_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, assets)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core132_stability_12q_v133_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, revenue)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core133_stability_12q_v134_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, marketcap)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core134_stability_12q_v135_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core135_stability_12q_v136_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, equity.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core136_stability_12q_v137_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, sharesbas)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core137_stability_12q_v138_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core138_stability_12q_v139_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _pct_change(ncfbus, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f033_equity_issuance_cash_core139_stability_12q_v140_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    base = _log(ncfbus.clip(lower=1.0))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f033_equity_issuance_cash_core140_level_v141_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(ncfbus)
def cg_f033_equity_issuance_cash_core141_ratio_assets_v142_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, assets))
def cg_f033_equity_issuance_cash_core142_ratio_rev_v143_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, revenue))
def cg_f033_equity_issuance_cash_core143_ratio_mcap_v144_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, marketcap))
def cg_f033_equity_issuance_cash_core144_ratio_ncfo_v145_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, ncfo.abs() + 1.0))
def cg_f033_equity_issuance_cash_core145_ratio_equity_v146_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, equity.abs() + 1.0))
def cg_f033_equity_issuance_cash_core146_ratio_shares_v147_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, sharesbas))
def cg_f033_equity_issuance_cash_core147_ratio_mix_v148_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_safe_div(ncfbus, ncfbus.abs() + ncfo.abs() + 1.0))
def cg_f033_equity_issuance_cash_core148_growth_yoy_v149_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_pct_change(ncfbus, 4))
def cg_f033_equity_issuance_cash_core149_log_level_v150_signal(ncfbus, sharesbas, assets, revenue, marketcap, ncfo, equity, opex):
    return _clean(_log(ncfbus.clip(lower=1.0)))
