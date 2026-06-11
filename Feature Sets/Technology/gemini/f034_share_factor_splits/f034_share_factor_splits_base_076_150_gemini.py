import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# Primary input is the Sharadar `sharefactor` adjustment field so split / reverse-split events are captured exactly rather than inferred from sharesbas (which would duplicate f031).

# core75-84: pct_4q
def cg_f034_share_factor_splits_core75_pct_4q_v076_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(_event_flag(sharefactor.diff().abs(), 0.01), 4))
def cg_f034_share_factor_splits_core76_pct_4q_v077_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change((sharefactor > 1.0).astype(float), 4))
def cg_f034_share_factor_splits_core77_pct_4q_v078_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change((sharefactor < 1.0).astype(float), 4))
def cg_f034_share_factor_splits_core78_pct_4q_v079_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(_log(sharefactor.abs().clip(lower=0.01)), 4))
def cg_f034_share_factor_splits_core79_pct_4q_v080_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(_pct_change(sharefactor, 1), 4))
# core80-89: std_8q
def cg_f034_share_factor_splits_core80_std_8q_v081_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(sharefactor, 8))
def cg_f034_share_factor_splits_core81_std_8q_v082_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(sharefactor.diff(), 8))
def cg_f034_share_factor_splits_core82_std_8q_v083_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(sharefactor.diff().abs(), 8))
def cg_f034_share_factor_splits_core83_std_8q_v084_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(sharefactor - 1.0, 8))
def cg_f034_share_factor_splits_core84_std_8q_v085_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std((sharefactor - 1.0).abs(), 8))
def cg_f034_share_factor_splits_core85_std_8q_v086_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(_event_flag(sharefactor.diff().abs(), 0.01), 8))
def cg_f034_share_factor_splits_core86_std_8q_v087_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std((sharefactor > 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core87_std_8q_v088_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std((sharefactor < 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core88_std_8q_v089_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(_log(sharefactor.abs().clip(lower=0.01)), 8))
def cg_f034_share_factor_splits_core89_std_8q_v090_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_std(_pct_change(sharefactor, 1), 8))
# core90-99: log
def cg_f034_share_factor_splits_core90_log_v091_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((sharefactor).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core91_log_v092_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((sharefactor.diff()).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core92_log_v093_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((sharefactor.diff().abs()).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core93_log_v094_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((sharefactor - 1.0).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core94_log_v095_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log(((sharefactor - 1.0).abs()).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core95_log_v096_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((_event_flag(sharefactor.diff().abs(), 0.01)).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core96_log_v097_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log(((sharefactor > 1.0).astype(float)).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core97_log_v098_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log(((sharefactor < 1.0).astype(float)).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core98_log_v099_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((_log(sharefactor.abs().clip(lower=0.01))).abs().clip(lower=0.0001)))
def cg_f034_share_factor_splits_core99_log_v100_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log((_pct_change(sharefactor, 1)).abs().clip(lower=0.0001)))
# core100-109: diff_1q
def cg_f034_share_factor_splits_core100_diff_1q_v101_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(sharefactor, 1))
def cg_f034_share_factor_splits_core101_diff_1q_v102_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(sharefactor.diff(), 1))
def cg_f034_share_factor_splits_core102_diff_1q_v103_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(sharefactor.diff().abs(), 1))
def cg_f034_share_factor_splits_core103_diff_1q_v104_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(sharefactor - 1.0, 1))
def cg_f034_share_factor_splits_core104_diff_1q_v105_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff((sharefactor - 1.0).abs(), 1))
def cg_f034_share_factor_splits_core105_diff_1q_v106_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(_event_flag(sharefactor.diff().abs(), 0.01), 1))
def cg_f034_share_factor_splits_core106_diff_1q_v107_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff((sharefactor > 1.0).astype(float), 1))
def cg_f034_share_factor_splits_core107_diff_1q_v108_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff((sharefactor < 1.0).astype(float), 1))
def cg_f034_share_factor_splits_core108_diff_1q_v109_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(_log(sharefactor.abs().clip(lower=0.01)), 1))
def cg_f034_share_factor_splits_core109_diff_1q_v110_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_diff(_pct_change(sharefactor, 1), 1))
# core110-119: slope_4q
def cg_f034_share_factor_splits_core110_slope_4q_v111_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(sharefactor, 4))
def cg_f034_share_factor_splits_core111_slope_4q_v112_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(sharefactor.diff(), 4))
def cg_f034_share_factor_splits_core112_slope_4q_v113_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(sharefactor.diff().abs(), 4))
def cg_f034_share_factor_splits_core113_slope_4q_v114_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(sharefactor - 1.0, 4))
def cg_f034_share_factor_splits_core114_slope_4q_v115_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope((sharefactor - 1.0).abs(), 4))
def cg_f034_share_factor_splits_core115_slope_4q_v116_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(_event_flag(sharefactor.diff().abs(), 0.01), 4))
def cg_f034_share_factor_splits_core116_slope_4q_v117_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope((sharefactor > 1.0).astype(float), 4))
def cg_f034_share_factor_splits_core117_slope_4q_v118_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope((sharefactor < 1.0).astype(float), 4))
def cg_f034_share_factor_splits_core118_slope_4q_v119_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(_log(sharefactor.abs().clip(lower=0.01)), 4))
def cg_f034_share_factor_splits_core119_slope_4q_v120_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_slope(_pct_change(sharefactor, 1), 4))
# core120-129: ewm_8q
def cg_f034_share_factor_splits_core120_ewm_8q_v121_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(sharefactor, 8))
def cg_f034_share_factor_splits_core121_ewm_8q_v122_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(sharefactor.diff(), 8))
def cg_f034_share_factor_splits_core122_ewm_8q_v123_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(sharefactor.diff().abs(), 8))
def cg_f034_share_factor_splits_core123_ewm_8q_v124_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(sharefactor - 1.0, 8))
def cg_f034_share_factor_splits_core124_ewm_8q_v125_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm((sharefactor - 1.0).abs(), 8))
def cg_f034_share_factor_splits_core125_ewm_8q_v126_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(_event_flag(sharefactor.diff().abs(), 0.01), 8))
def cg_f034_share_factor_splits_core126_ewm_8q_v127_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm((sharefactor > 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core127_ewm_8q_v128_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm((sharefactor < 1.0).astype(float), 8))
def cg_f034_share_factor_splits_core128_ewm_8q_v129_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(_log(sharefactor.abs().clip(lower=0.01)), 8))
def cg_f034_share_factor_splits_core129_ewm_8q_v130_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_ewm(_pct_change(sharefactor, 1), 8))
# core130-139: stability_12q
def cg_f034_share_factor_splits_core130_stability_12q_v131_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = sharefactor
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core131_stability_12q_v132_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = sharefactor.diff()
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core132_stability_12q_v133_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = sharefactor.diff().abs()
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core133_stability_12q_v134_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = sharefactor - 1.0
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core134_stability_12q_v135_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = (sharefactor - 1.0).abs()
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core135_stability_12q_v136_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = _event_flag(sharefactor.diff().abs(), 0.01)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core136_stability_12q_v137_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = (sharefactor > 1.0).astype(float)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core137_stability_12q_v138_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = (sharefactor < 1.0).astype(float)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core138_stability_12q_v139_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = _log(sharefactor.abs().clip(lower=0.01))
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f034_share_factor_splits_core139_stability_12q_v140_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    base = _pct_change(sharefactor, 1)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
# core140-149: levels
def cg_f034_share_factor_splits_core140_levels_v141_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(sharefactor)
def cg_f034_share_factor_splits_core141_levels_v142_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(sharefactor.diff())
def cg_f034_share_factor_splits_core142_levels_v143_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(sharefactor.diff().abs())
def cg_f034_share_factor_splits_core143_levels_v144_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(sharefactor - 1.0)
def cg_f034_share_factor_splits_core144_levels_v145_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean((sharefactor - 1.0).abs())
def cg_f034_share_factor_splits_core145_levels_v146_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_event_flag(sharefactor.diff().abs(), 0.01))
def cg_f034_share_factor_splits_core146_levels_v147_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean((sharefactor > 1.0).astype(float))
def cg_f034_share_factor_splits_core147_levels_v148_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean((sharefactor < 1.0).astype(float))
def cg_f034_share_factor_splits_core148_levels_v149_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_log(sharefactor.abs().clip(lower=0.01)))
def cg_f034_share_factor_splits_core149_levels_v150_signal(sharefactor, sharesbas, sharesdil, marketcap, assets, equity, revenue, opex, netinc):
    return _clean(_pct_change(sharefactor, 1))
