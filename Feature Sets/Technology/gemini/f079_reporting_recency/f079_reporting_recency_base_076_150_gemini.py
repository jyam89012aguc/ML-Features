import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f079_reporting_recency_core75_event_rate_4q_v076_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(lastupdated, 4))
def cg_f079_reporting_recency_core76_event_rate_8q_v077_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(calendardate, 8))
def cg_f079_reporting_recency_core77_event_rate_8q_v078_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(reportperiod, 8))
def cg_f079_reporting_recency_core78_event_rate_8q_v079_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(datekey, 8))
def cg_f079_reporting_recency_core79_event_rate_8q_v080_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(lastupdated, 8))
def cg_f079_reporting_recency_core80_autocorr_4q_v081_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(calendardate, 4))
def cg_f079_reporting_recency_core81_autocorr_4q_v082_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(reportperiod, 4))
def cg_f079_reporting_recency_core82_autocorr_4q_v083_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(datekey, 4))
def cg_f079_reporting_recency_core83_autocorr_4q_v084_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(lastupdated, 4))
def cg_f079_reporting_recency_core84_autocorr_8q_v085_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(calendardate, 8))
def cg_f079_reporting_recency_core85_autocorr_8q_v086_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(reportperiod, 8))
def cg_f079_reporting_recency_core86_autocorr_8q_v087_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(datekey, 8))
def cg_f079_reporting_recency_core87_autocorr_8q_v088_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(lastupdated, 8))
def cg_f079_reporting_recency_core88_rank_event_count_4q_12q_v089_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(calendardate, 4), 12))
def cg_f079_reporting_recency_core89_rank_event_count_4q_12q_v090_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(reportperiod, 4), 12))
def cg_f079_reporting_recency_core90_rank_event_count_4q_12q_v091_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(datekey, 4), 12))
def cg_f079_reporting_recency_core91_rank_event_count_4q_12q_v092_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(lastupdated, 4), 12))
def cg_f079_reporting_recency_core92_rank_event_rate_4q_12q_v093_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_rate(calendardate, 4), 12))
def cg_f079_reporting_recency_core93_rank_event_rate_4q_12q_v094_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_rate(reportperiod, 4), 12))
def cg_f079_reporting_recency_core94_rank_event_rate_4q_12q_v095_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_rate(datekey, 4), 12))
def cg_f079_reporting_recency_core95_rank_event_rate_4q_12q_v096_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_rate(lastupdated, 4), 12))
def cg_f079_reporting_recency_core96_event_diff_1q_v097_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(calendardate).diff(1))
def cg_f079_reporting_recency_core97_diff_1q_v098_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(reportperiod), 1))
def cg_f079_reporting_recency_core98_diff_1q_v099_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(datekey), 1))
def cg_f079_reporting_recency_core99_diff_1q_v100_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(lastupdated), 1))
def cg_f079_reporting_recency_core100_event_count_12q_v101_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(calendardate, 12))
def cg_f079_reporting_recency_core101_event_count_12q_v102_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(reportperiod, 12))
def cg_f079_reporting_recency_core102_event_count_12q_v103_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(datekey, 12))
def cg_f079_reporting_recency_core103_event_count_12q_v104_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(lastupdated, 12))
def cg_f079_reporting_recency_core104_event_rate_12q_v105_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(calendardate, 12))
def cg_f079_reporting_recency_core105_event_rate_12q_v106_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(reportperiod, 12))
def cg_f079_reporting_recency_core106_event_rate_12q_v107_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(datekey, 12))
def cg_f079_reporting_recency_core107_event_rate_12q_v108_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(lastupdated, 12))
def cg_f079_reporting_recency_core108_autocorr_12q_v109_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(calendardate, 12))
def cg_f079_reporting_recency_core109_autocorr_12q_v110_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(reportperiod, 12))
def cg_f079_reporting_recency_core110_autocorr_12q_v111_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(datekey, 12))
def cg_f079_reporting_recency_core111_autocorr_12q_v112_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(lastupdated, 12))
def cg_f079_reporting_recency_core112_rank_event_count_8q_20q_v113_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(calendardate, 8), 20))
def cg_f079_reporting_recency_core113_rank_event_count_8q_20q_v114_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(reportperiod, 8), 20))
def cg_f079_reporting_recency_core114_rank_event_count_8q_20q_v115_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(datekey, 8), 20))
def cg_f079_reporting_recency_core115_rank_event_count_8q_20q_v116_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(lastupdated, 8), 20))
def cg_f079_reporting_recency_core116_event_flag_alt_v117_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(calendardate))
def cg_f079_reporting_recency_core117_event_flag_alt_v118_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(reportperiod))
def cg_f079_reporting_recency_core118_event_flag_alt_v119_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(datekey))
def cg_f079_reporting_recency_core119_event_flag_alt_v120_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(lastupdated))
def cg_f079_reporting_recency_core120_event_flag_v121_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(calendardate))
def cg_f079_reporting_recency_core121_event_flag_v122_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(reportperiod))
def cg_f079_reporting_recency_core122_event_flag_v123_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(datekey))
def cg_f079_reporting_recency_core123_event_flag_v124_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_flag(lastupdated))
def cg_f079_reporting_recency_core124_event_count_4q_v125_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(calendardate, 4))
def cg_f079_reporting_recency_core125_event_count_4q_v126_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(reportperiod, 4))
def cg_f079_reporting_recency_core126_event_count_4q_v127_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(datekey, 4))
def cg_f079_reporting_recency_core127_event_count_4q_v128_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(lastupdated, 4))
def cg_f079_reporting_recency_core128_event_count_8q_v129_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(calendardate, 8))
def cg_f079_reporting_recency_core129_event_count_8q_v130_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(reportperiod, 8))
def cg_f079_reporting_recency_core130_event_count_8q_v131_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(datekey, 8))
def cg_f079_reporting_recency_core131_event_count_8q_v132_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_count(lastupdated, 8))
def cg_f079_reporting_recency_core132_event_rate_4q_v133_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(calendardate, 4))
def cg_f079_reporting_recency_core133_event_rate_4q_v134_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(reportperiod, 4))
def cg_f079_reporting_recency_core134_event_rate_4q_v135_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(datekey, 4))
def cg_f079_reporting_recency_core135_event_rate_4q_v136_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(lastupdated, 4))
def cg_f079_reporting_recency_core136_event_rate_8q_v137_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(calendardate, 8))
def cg_f079_reporting_recency_core137_event_rate_8q_v138_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(reportperiod, 8))
def cg_f079_reporting_recency_core138_event_rate_8q_v139_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(datekey, 8))
def cg_f079_reporting_recency_core139_event_rate_8q_v140_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_event_rate(lastupdated, 8))
def cg_f079_reporting_recency_core140_autocorr_4q_v141_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(calendardate, 4))
def cg_f079_reporting_recency_core141_autocorr_4q_v142_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(reportperiod, 4))
def cg_f079_reporting_recency_core142_autocorr_4q_v143_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(datekey, 4))
def cg_f079_reporting_recency_core143_autocorr_4q_v144_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(lastupdated, 4))
def cg_f079_reporting_recency_core144_autocorr_8q_v145_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(calendardate, 8))
def cg_f079_reporting_recency_core145_autocorr_8q_v146_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(reportperiod, 8))
def cg_f079_reporting_recency_core146_autocorr_8q_v147_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(datekey, 8))
def cg_f079_reporting_recency_core147_autocorr_8q_v148_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_autocorr(lastupdated, 8))
def cg_f079_reporting_recency_core148_rank_event_count_4q_12q_v149_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(calendardate, 4), 12))
def cg_f079_reporting_recency_core149_rank_event_count_4q_12q_v150_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_event_count(reportperiod, 4), 12))