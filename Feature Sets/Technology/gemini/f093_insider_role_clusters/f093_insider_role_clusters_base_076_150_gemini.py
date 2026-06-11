import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 63d (continued)
def cg_f093_insider_role_clusters_core75_ewm_63d_v076_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_count(ownername, 63), 63))
def cg_f093_insider_role_clusters_core76_ewm_63d_v077_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_count(officertitle, 63), 63))
def cg_f093_insider_role_clusters_core77_ewm_63d_v078_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_flag(ownername), 63))
def cg_f093_insider_role_clusters_core78_ewm_63d_v079_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_event_flag(officertitle), 63))
def cg_f093_insider_role_clusters_core79_ewm_63d_v080_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_ewm(_z(_event_count(ownername, 252), 252), 63))

# core80-89: skew 126d
def cg_f093_insider_role_clusters_core80_skew_126d_v081_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_flag(isdirector), 126))
def cg_f093_insider_role_clusters_core81_skew_126d_v082_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_flag(isofficer), 126))
def cg_f093_insider_role_clusters_core82_skew_126d_v083_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_flag(istenpercentowner), 126))
def cg_f093_insider_role_clusters_core83_skew_126d_v084_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_rate(ownername, 21), 126))
def cg_f093_insider_role_clusters_core84_skew_126d_v085_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_rate(officertitle, 21), 126))
def cg_f093_insider_role_clusters_core85_skew_126d_v086_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_count(ownername, 63), 126))
def cg_f093_insider_role_clusters_core86_skew_126d_v087_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_count(officertitle, 63), 126))
def cg_f093_insider_role_clusters_core87_skew_126d_v088_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_flag(ownername), 126))
def cg_f093_insider_role_clusters_core88_skew_126d_v089_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_event_flag(officertitle), 126))
def cg_f093_insider_role_clusters_core89_skew_126d_v090_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_skew(_z(_event_count(ownername, 252), 252), 126))

# core90-99: kurt 126d
def cg_f093_insider_role_clusters_core90_kurt_126d_v091_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_flag(isdirector), 126))
def cg_f093_insider_role_clusters_core91_kurt_126d_v092_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_flag(isofficer), 126))
def cg_f093_insider_role_clusters_core92_kurt_126d_v093_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_flag(istenpercentowner), 126))
def cg_f093_insider_role_clusters_core93_kurt_126d_v094_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_rate(ownername, 21), 126))
def cg_f093_insider_role_clusters_core94_kurt_126d_v095_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_rate(officertitle, 21), 126))
def cg_f093_insider_role_clusters_core95_kurt_126d_v096_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_count(ownername, 63), 126))
def cg_f093_insider_role_clusters_core96_kurt_126d_v097_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_count(officertitle, 63), 126))
def cg_f093_insider_role_clusters_core97_kurt_126d_v098_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_flag(ownername), 126))
def cg_f093_insider_role_clusters_core98_kurt_126d_v099_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_event_flag(officertitle), 126))
def cg_f093_insider_role_clusters_core99_kurt_126d_v100_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_kurt(_z(_event_count(ownername, 252), 252), 126))

# core100-109: autocorr 63d
def cg_f093_insider_role_clusters_core100_autocorr_63d_v101_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core101_autocorr_63d_v102_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_flag(isofficer), 63))
def cg_f093_insider_role_clusters_core102_autocorr_63d_v103_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_rate(ownername, 21), 63))
def cg_f093_insider_role_clusters_core103_autocorr_63d_v104_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_rate(officertitle, 21), 63))
def cg_f093_insider_role_clusters_core104_autocorr_63d_v105_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_count(ownername, 63), 63))
def cg_f093_insider_role_clusters_core105_autocorr_63d_v106_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_count(officertitle, 63), 63))
def cg_f093_insider_role_clusters_core106_autocorr_63d_v107_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_flag(ownername), 63))
def cg_f093_insider_role_clusters_core107_autocorr_63d_v108_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_flag(officertitle), 63))
def cg_f093_insider_role_clusters_core108_autocorr_63d_v109_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_z(_event_count(ownername, 252), 252), 63))
def cg_f093_insider_role_clusters_core109_autocorr_63d_v110_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_autocorr(_event_flag(istenpercentowner), 63))

# core110-119: corr with director 63d
def cg_f093_insider_role_clusters_core110_corr_director_63d_v111_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_flag(isofficer), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core111_corr_director_63d_v112_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_flag(istenpercentowner), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core112_corr_director_63d_v113_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_rate(ownername, 21), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core113_corr_director_63d_v114_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_rate(officertitle, 21), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core114_corr_director_63d_v115_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_count(ownername, 63), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core115_corr_director_63d_v116_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_count(officertitle, 63), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core116_corr_director_63d_v117_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_flag(ownername), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core117_corr_director_63d_v118_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_flag(officertitle), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core118_corr_director_63d_v119_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_z(_event_count(ownername, 252), 252), _event_flag(isdirector), 63))
def cg_f093_insider_role_clusters_core119_corr_director_63d_v120_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_corr(_event_rate(ownername, 63), _event_flag(isdirector), 63))

# core120-129: stability 63d
def cg_f093_insider_role_clusters_core120_stability_63d_v121_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_flag(isdirector)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core121_stability_63d_v122_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_flag(isofficer)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core122_stability_63d_v123_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_rate(ownername, 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core123_stability_63d_v124_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_rate(officertitle, 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core124_stability_63d_v125_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_count(ownername, 63)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core125_stability_63d_v126_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_count(officertitle, 63)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core126_stability_63d_v127_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_flag(ownername)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core127_stability_63d_v128_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_flag(officertitle)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core128_stability_63d_v129_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _z(_event_count(ownername, 252), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f093_insider_role_clusters_core129_stability_63d_v130_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    base = _event_rate(ownername, 63)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))

# core130-139: diff 21d
def cg_f093_insider_role_clusters_core130_diff_21d_v131_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_event_rate(ownername, 252), 21))
def cg_f093_insider_role_clusters_core131_diff_21d_v132_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_event_rate(officertitle, 252), 21))
def cg_f093_insider_role_clusters_core132_diff_21d_v133_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(_event_flag(isdirector), 63), 21))
def cg_f093_insider_role_clusters_core133_diff_21d_v134_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(_event_flag(isofficer), 63), 21))
def cg_f093_insider_role_clusters_core134_diff_21d_v135_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_event_count(ownername, 63), 21))
def cg_f093_insider_role_clusters_core135_diff_21d_v136_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_event_count(officertitle, 63), 21))
def cg_f093_insider_role_clusters_core136_diff_21d_v137_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_z(_event_count(ownername, 252), 252), 21))
def cg_f093_insider_role_clusters_core137_diff_21d_v138_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_rank(_event_count(ownername, 252), 252), 21))
def cg_f093_insider_role_clusters_core138_diff_21d_v139_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_event_rate(ownername, 63), 21))
def cg_f093_insider_role_clusters_core139_diff_21d_v140_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(_event_flag(istenpercentowner), 63), 21))

# core140-149: levels
def cg_f093_insider_role_clusters_core140_director_level_v141_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(isdirector)
def cg_f093_insider_role_clusters_core141_officer_level_v142_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(isofficer)
def cg_f093_insider_role_clusters_core142_ten_pct_level_v143_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(istenpercentowner)
def cg_f093_insider_role_clusters_core143_owner_count_v144_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_count(ownername, 252)
def cg_f093_insider_role_clusters_core144_title_count_v145_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_count(officertitle, 252)
def cg_f093_insider_role_clusters_core145_director_rate_v146_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_rate(isdirector, 252)
def cg_f093_insider_role_clusters_core146_officer_rate_v147_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_rate(isofficer, 252)
def cg_f093_insider_role_clusters_core147_ten_pct_rate_v148_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_rate(istenpercentowner, 252)
def cg_f093_insider_role_clusters_core148_multi_role_v149_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return (_event_flag(isdirector) + _event_flag(isofficer) + _event_flag(istenpercentowner)).astype(float)
def cg_f093_insider_role_clusters_core149_owner_unique_v150_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _event_flag(ownername)
