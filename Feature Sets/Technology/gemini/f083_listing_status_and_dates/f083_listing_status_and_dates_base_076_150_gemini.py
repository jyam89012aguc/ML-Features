import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f083_listing_status_and_dates_core75_event_flag_v076_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(isdelisted))
def cg_f083_listing_status_and_dates_core76_event_flag_v077_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstpricedate))
def cg_f083_listing_status_and_dates_core77_event_flag_v078_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastpricedate))
def cg_f083_listing_status_and_dates_core78_event_flag_v079_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstquarter))
def cg_f083_listing_status_and_dates_core79_event_flag_v080_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastquarter))
def cg_f083_listing_status_and_dates_core80_event_count_4q_v081_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(isdelisted, 4))
def cg_f083_listing_status_and_dates_core81_event_count_4q_v082_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstpricedate, 4))
def cg_f083_listing_status_and_dates_core82_event_count_4q_v083_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastpricedate, 4))
def cg_f083_listing_status_and_dates_core83_event_count_4q_v084_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstquarter, 4))
def cg_f083_listing_status_and_dates_core84_event_count_4q_v085_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastquarter, 4))
def cg_f083_listing_status_and_dates_core85_event_count_8q_v086_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(isdelisted, 8))
def cg_f083_listing_status_and_dates_core86_event_count_8q_v087_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstpricedate, 8))
def cg_f083_listing_status_and_dates_core87_event_count_8q_v088_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastpricedate, 8))
def cg_f083_listing_status_and_dates_core88_event_count_8q_v089_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstquarter, 8))
def cg_f083_listing_status_and_dates_core89_event_count_8q_v090_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastquarter, 8))
def cg_f083_listing_status_and_dates_core90_event_rate_4q_v091_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(isdelisted, 4))
def cg_f083_listing_status_and_dates_core91_event_rate_4q_v092_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstpricedate, 4))
def cg_f083_listing_status_and_dates_core92_event_rate_4q_v093_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastpricedate, 4))
def cg_f083_listing_status_and_dates_core93_event_rate_4q_v094_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstquarter, 4))
def cg_f083_listing_status_and_dates_core94_event_rate_4q_v095_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastquarter, 4))
def cg_f083_listing_status_and_dates_core95_event_rate_8q_v096_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(isdelisted, 8))
def cg_f083_listing_status_and_dates_core96_event_rate_8q_v097_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstpricedate, 8))
def cg_f083_listing_status_and_dates_core97_event_rate_8q_v098_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastpricedate, 8))
def cg_f083_listing_status_and_dates_core98_event_rate_8q_v099_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstquarter, 8))
def cg_f083_listing_status_and_dates_core99_event_rate_8q_v100_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastquarter, 8))
def cg_f083_listing_status_and_dates_core100_autocorr_4q_v101_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(isdelisted, 4))
def cg_f083_listing_status_and_dates_core101_autocorr_4q_v102_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstpricedate, 4))
def cg_f083_listing_status_and_dates_core102_autocorr_4q_v103_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastpricedate, 4))
def cg_f083_listing_status_and_dates_core103_autocorr_4q_v104_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstquarter, 4))
def cg_f083_listing_status_and_dates_core104_autocorr_4q_v105_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastquarter, 4))
def cg_f083_listing_status_and_dates_core105_autocorr_8q_v106_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(isdelisted, 8))
def cg_f083_listing_status_and_dates_core106_autocorr_8q_v107_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstpricedate, 8))
def cg_f083_listing_status_and_dates_core107_autocorr_8q_v108_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastpricedate, 8))
def cg_f083_listing_status_and_dates_core108_autocorr_8q_v109_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstquarter, 8))
def cg_f083_listing_status_and_dates_core109_autocorr_8q_v110_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastquarter, 8))
def cg_f083_listing_status_and_dates_core110_rank_event_count_4q_12q_v111_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(isdelisted, 4), 12))
def cg_f083_listing_status_and_dates_core111_rank_event_count_4q_12q_v112_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core112_rank_event_count_4q_12q_v113_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core113_rank_event_count_4q_12q_v114_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstquarter, 4), 12))
def cg_f083_listing_status_and_dates_core114_rank_event_count_4q_12q_v115_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastquarter, 4), 12))
def cg_f083_listing_status_and_dates_core115_rank_event_rate_4q_12q_v116_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(isdelisted, 4), 12))
def cg_f083_listing_status_and_dates_core116_rank_event_rate_4q_12q_v117_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(firstpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core117_rank_event_rate_4q_12q_v118_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(lastpricedate, 4), 12))
def cg_f083_listing_status_and_dates_core118_rank_event_rate_4q_12q_v119_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(firstquarter, 4), 12))
def cg_f083_listing_status_and_dates_core119_rank_event_rate_4q_12q_v120_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_rate(lastquarter, 4), 12))
def cg_f083_listing_status_and_dates_core120_event_diff_1q_v121_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(isdelisted).diff(1))
def cg_f083_listing_status_and_dates_core121_diff_1q_v122_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(firstpricedate), 1))
def cg_f083_listing_status_and_dates_core122_diff_1q_v123_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_diff(_to_num(lastpricedate), 1))
def cg_f083_listing_status_and_dates_core123_event_diff_1q_v124_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstquarter).diff(1))
def cg_f083_listing_status_and_dates_core124_event_diff_1q_v125_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastquarter).diff(1))
def cg_f083_listing_status_and_dates_core125_event_count_12q_v126_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(isdelisted, 12))
def cg_f083_listing_status_and_dates_core126_event_count_12q_v127_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstpricedate, 12))
def cg_f083_listing_status_and_dates_core127_event_count_12q_v128_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastpricedate, 12))
def cg_f083_listing_status_and_dates_core128_event_count_12q_v129_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(firstquarter, 12))
def cg_f083_listing_status_and_dates_core129_event_count_12q_v130_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_count(lastquarter, 12))
def cg_f083_listing_status_and_dates_core130_event_rate_12q_v131_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(isdelisted, 12))
def cg_f083_listing_status_and_dates_core131_event_rate_12q_v132_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstpricedate, 12))
def cg_f083_listing_status_and_dates_core132_event_rate_12q_v133_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastpricedate, 12))
def cg_f083_listing_status_and_dates_core133_event_rate_12q_v134_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(firstquarter, 12))
def cg_f083_listing_status_and_dates_core134_event_rate_12q_v135_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_rate(lastquarter, 12))
def cg_f083_listing_status_and_dates_core135_autocorr_12q_v136_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(isdelisted, 12))
def cg_f083_listing_status_and_dates_core136_autocorr_12q_v137_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstpricedate, 12))
def cg_f083_listing_status_and_dates_core137_autocorr_12q_v138_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastpricedate, 12))
def cg_f083_listing_status_and_dates_core138_autocorr_12q_v139_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(firstquarter, 12))
def cg_f083_listing_status_and_dates_core139_autocorr_12q_v140_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_autocorr(lastquarter, 12))
def cg_f083_listing_status_and_dates_core140_rank_event_count_8q_20q_v141_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(isdelisted, 8), 20))
def cg_f083_listing_status_and_dates_core141_rank_event_count_8q_20q_v142_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstpricedate, 8), 20))
def cg_f083_listing_status_and_dates_core142_rank_event_count_8q_20q_v143_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastpricedate, 8), 20))
def cg_f083_listing_status_and_dates_core143_rank_event_count_8q_20q_v144_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(firstquarter, 8), 20))
def cg_f083_listing_status_and_dates_core144_rank_event_count_8q_20q_v145_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_rank(_event_count(lastquarter, 8), 20))
def cg_f083_listing_status_and_dates_core145_event_flag_alt_v146_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(isdelisted))
def cg_f083_listing_status_and_dates_core146_event_flag_alt_v147_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstpricedate))
def cg_f083_listing_status_and_dates_core147_event_flag_alt_v148_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastpricedate))
def cg_f083_listing_status_and_dates_core148_event_flag_alt_v149_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(firstquarter))
def cg_f083_listing_status_and_dates_core149_event_flag_alt_v150_signal(isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter):
    return _clean(_event_flag(lastquarter))