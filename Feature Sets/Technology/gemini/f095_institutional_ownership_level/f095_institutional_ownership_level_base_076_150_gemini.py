import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 63d (continued)
def cg_f095_institutional_ownership_level_core75_ewm_63d_v076_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_z(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core76_ewm_63d_v077_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_rank(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core77_ewm_63d_v078_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_event_count(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core78_ewm_63d_v079_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_event_rate(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core79_ewm_63d_v080_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_ewm(_safe_div(_to_num(value), _to_num(units)), 63))

# core80-89: skew 126d
def cg_f095_institutional_ownership_level_core80_skew_126d_v081_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_to_num(value), 126))
def cg_f095_institutional_ownership_level_core81_skew_126d_v082_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_to_num(units), 126))
def cg_f095_institutional_ownership_level_core82_skew_126d_v083_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_to_num(price), 126))
def cg_f095_institutional_ownership_level_core83_skew_126d_v084_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_event_flag(investorname), 126))
def cg_f095_institutional_ownership_level_core84_skew_126d_v085_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_pct_change(_to_num(value), 1), 126))
def cg_f095_institutional_ownership_level_core85_skew_126d_v086_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_z(_to_num(value), 252), 126))
def cg_f095_institutional_ownership_level_core86_skew_126d_v087_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_rank(_to_num(value), 252), 126))
def cg_f095_institutional_ownership_level_core87_skew_126d_v088_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_safe_div(_to_num(value), _to_num(units)), 126))
def cg_f095_institutional_ownership_level_core88_skew_126d_v089_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_event_count(investorname, 21), 126))
def cg_f095_institutional_ownership_level_core89_skew_126d_v090_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_skew(_event_rate(investorname, 21), 126))

# core90-99: kurt 126d
def cg_f095_institutional_ownership_level_core90_kurt_126d_v091_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_to_num(value), 126))
def cg_f095_institutional_ownership_level_core91_kurt_126d_v092_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_to_num(units), 126))
def cg_f095_institutional_ownership_level_core92_kurt_126d_v093_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_to_num(price), 126))
def cg_f095_institutional_ownership_level_core93_kurt_126d_v094_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_event_flag(investorname), 126))
def cg_f095_institutional_ownership_level_core94_kurt_126d_v095_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_pct_change(_to_num(value), 1), 126))
def cg_f095_institutional_ownership_level_core95_kurt_126d_v096_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_z(_to_num(value), 252), 126))
def cg_f095_institutional_ownership_level_core96_kurt_126d_v097_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_rank(_to_num(value), 252), 126))
def cg_f095_institutional_ownership_level_core97_kurt_126d_v098_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_safe_div(_to_num(value), _to_num(units)), 126))
def cg_f095_institutional_ownership_level_core98_kurt_126d_v099_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_event_count(investorname, 21), 126))
def cg_f095_institutional_ownership_level_core99_kurt_126d_v100_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_kurt(_event_rate(investorname, 21), 126))

# core100-109: autocorr 63d
def cg_f095_institutional_ownership_level_core100_autocorr_63d_v101_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_to_num(value), 63))
def cg_f095_institutional_ownership_level_core101_autocorr_63d_v102_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_to_num(units), 63))
def cg_f095_institutional_ownership_level_core102_autocorr_63d_v103_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_event_flag(investorname), 63))
def cg_f095_institutional_ownership_level_core103_autocorr_63d_v104_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_event_count(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core104_autocorr_63d_v105_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_z(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core105_autocorr_63d_v106_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_rank(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core106_autocorr_63d_v107_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_pct_change(_to_num(value), 1), 63))
def cg_f095_institutional_ownership_level_core107_autocorr_63d_v108_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_safe_div(_to_num(value), _to_num(units)), 63))
def cg_f095_institutional_ownership_level_core108_autocorr_63d_v109_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_event_rate(investorname, 21), 63))
def cg_f095_institutional_ownership_level_core109_autocorr_63d_v110_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_autocorr(_to_num(price), 63))

# core110-119: corr with units 63d
def cg_f095_institutional_ownership_level_core110_corr_units_63d_v111_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_to_num(value), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core111_corr_units_63d_v112_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_event_flag(investorname), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core112_corr_units_63d_v113_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_event_count(investorname, 21), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core113_corr_units_63d_v114_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_z(_to_num(value), 252), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core114_corr_units_63d_v115_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_rank(_to_num(value), 252), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core115_corr_units_63d_v116_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_pct_change(_to_num(value), 1), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core116_corr_units_63d_v117_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_to_num(price), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core117_corr_units_63d_v118_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_event_rate(investorname, 21), _to_num(units), 63))
def cg_f095_institutional_ownership_level_core118_corr_units_63d_v119_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_to_num(value), _mean(_to_num(value), 252), 63))
def cg_f095_institutional_ownership_level_core119_corr_units_63d_v120_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_corr(_to_num(units), _mean(_to_num(units), 252), 63))

# core120-129: stability 63d
def cg_f095_institutional_ownership_level_core120_stability_63d_v121_signal(calendardate, investorname, securitytype, value, units, price):
    base = _to_num(value)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core121_stability_63d_v122_signal(calendardate, investorname, securitytype, value, units, price):
    base = _to_num(units)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core122_stability_63d_v123_signal(calendardate, investorname, securitytype, value, units, price):
    base = _event_flag(investorname)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core123_stability_63d_v124_signal(calendardate, investorname, securitytype, value, units, price):
    base = _event_count(investorname, 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core124_stability_63d_v125_signal(calendardate, investorname, securitytype, value, units, price):
    base = _z(_to_num(value), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core125_stability_63d_v126_signal(calendardate, investorname, securitytype, value, units, price):
    base = _rank(_to_num(value), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core126_stability_63d_v127_signal(calendardate, investorname, securitytype, value, units, price):
    base = _pct_change(_to_num(value), 1)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core127_stability_63d_v128_signal(calendardate, investorname, securitytype, value, units, price):
    base = _safe_div(_to_num(value), _to_num(units))
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core128_stability_63d_v129_signal(calendardate, investorname, securitytype, value, units, price):
    base = _event_rate(investorname, 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f095_institutional_ownership_level_core129_stability_63d_v130_signal(calendardate, investorname, securitytype, value, units, price):
    base = _to_num(price)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))

# core130-139: diff 21d
def cg_f095_institutional_ownership_level_core130_diff_21d_v131_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_to_num(value), 21))
def cg_f095_institutional_ownership_level_core131_diff_21d_v132_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_to_num(units), 21))
def cg_f095_institutional_ownership_level_core132_diff_21d_v133_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_event_count(investorname, 21), 21))
def cg_f095_institutional_ownership_level_core133_diff_21d_v134_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_z(_to_num(value), 252), 21))
def cg_f095_institutional_ownership_level_core134_diff_21d_v135_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_rank(_to_num(value), 252), 21))
def cg_f095_institutional_ownership_level_core135_diff_21d_v136_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_pct_change(_to_num(value), 1), 21))
def cg_f095_institutional_ownership_level_core136_diff_21d_v137_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_safe_div(_to_num(value), _to_num(units)), 21))
def cg_f095_institutional_ownership_level_core137_diff_21d_v138_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_event_rate(investorname, 21), 21))
def cg_f095_institutional_ownership_level_core138_diff_21d_v139_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_to_num(price), 21))
def cg_f095_institutional_ownership_level_core139_diff_21d_v140_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_diff(_mean(_to_num(value), 63), 21))

# core140-149: levels
def cg_f095_institutional_ownership_level_core140_level_v141_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_to_num(value))
def cg_f095_institutional_ownership_level_core141_units_v142_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_to_num(units))
def cg_f095_institutional_ownership_level_core142_price_v143_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_to_num(price))
def cg_f095_institutional_ownership_level_core143_investor_flag_v144_signal(calendardate, investorname, securitytype, value, units, price):
    return _event_flag(investorname)
def cg_f095_institutional_ownership_level_core144_security_flag_v145_signal(calendardate, investorname, securitytype, value, units, price):
    return _event_flag(securitytype)
def cg_f095_institutional_ownership_level_core145_value_z_v146_signal(calendardate, investorname, securitytype, value, units, price):
    return _z(_to_num(value), 252)
def cg_f095_institutional_ownership_level_core146_units_z_v147_signal(calendardate, investorname, securitytype, value, units, price):
    return _z(_to_num(units), 252)
def cg_f095_institutional_ownership_level_core147_value_rank_v148_signal(calendardate, investorname, securitytype, value, units, price):
    return _rank(_to_num(value), 252)
def cg_f095_institutional_ownership_level_core148_units_rank_v149_signal(calendardate, investorname, securitytype, value, units, price):
    return _rank(_to_num(units), 252)
def cg_f095_institutional_ownership_level_core149_avg_price_v150_signal(calendardate, investorname, securitytype, value, units, price):
    return _clean(_safe_div(_to_num(value), _to_num(units)))
