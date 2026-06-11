import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f080_restatement_revision_proxy_core75_event_rate_4q_v076_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 4))
def cg_f080_restatement_revision_proxy_core76_event_rate_8q_v077_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 8))
def cg_f080_restatement_revision_proxy_core77_event_rate_8q_v078_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core78_event_rate_8q_v079_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core79_event_rate_8q_v080_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 8))
def cg_f080_restatement_revision_proxy_core80_autocorr_4q_v081_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 4))
def cg_f080_restatement_revision_proxy_core81_autocorr_4q_v082_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core82_autocorr_4q_v083_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core83_autocorr_4q_v084_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 4))
def cg_f080_restatement_revision_proxy_core84_autocorr_8q_v085_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 8))
def cg_f080_restatement_revision_proxy_core85_autocorr_8q_v086_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core86_autocorr_8q_v087_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core87_autocorr_8q_v088_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 8))
def cg_f080_restatement_revision_proxy_core88_rank_event_count_4q_12q_v089_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(datekey, 4), 12))
def cg_f080_restatement_revision_proxy_core89_rank_event_count_4q_12q_v090_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(lastupdated, 4), 12))
def cg_f080_restatement_revision_proxy_core90_rank_event_count_4q_12q_v091_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(reportperiod, 4), 12))
def cg_f080_restatement_revision_proxy_core91_rank_event_count_4q_12q_v092_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(dimension, 4), 12))
def cg_f080_restatement_revision_proxy_core92_rank_event_rate_4q_12q_v093_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(datekey, 4), 12))
def cg_f080_restatement_revision_proxy_core93_rank_event_rate_4q_12q_v094_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(lastupdated, 4), 12))
def cg_f080_restatement_revision_proxy_core94_rank_event_rate_4q_12q_v095_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(reportperiod, 4), 12))
def cg_f080_restatement_revision_proxy_core95_rank_event_rate_4q_12q_v096_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_rate(dimension, 4), 12))
def cg_f080_restatement_revision_proxy_core96_diff_1q_v097_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(datekey), 1))
def cg_f080_restatement_revision_proxy_core97_diff_1q_v098_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(lastupdated), 1))
def cg_f080_restatement_revision_proxy_core98_diff_1q_v099_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(reportperiod), 1))
def cg_f080_restatement_revision_proxy_core99_event_diff_1q_v100_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension).diff(1))
def cg_f080_restatement_revision_proxy_core100_event_count_12q_v101_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 12))
def cg_f080_restatement_revision_proxy_core101_event_count_12q_v102_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 12))
def cg_f080_restatement_revision_proxy_core102_event_count_12q_v103_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 12))
def cg_f080_restatement_revision_proxy_core103_event_count_12q_v104_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 12))
def cg_f080_restatement_revision_proxy_core104_event_rate_12q_v105_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 12))
def cg_f080_restatement_revision_proxy_core105_event_rate_12q_v106_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 12))
def cg_f080_restatement_revision_proxy_core106_event_rate_12q_v107_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 12))
def cg_f080_restatement_revision_proxy_core107_event_rate_12q_v108_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 12))
def cg_f080_restatement_revision_proxy_core108_autocorr_12q_v109_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 12))
def cg_f080_restatement_revision_proxy_core109_autocorr_12q_v110_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 12))
def cg_f080_restatement_revision_proxy_core110_autocorr_12q_v111_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 12))
def cg_f080_restatement_revision_proxy_core111_autocorr_12q_v112_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 12))
def cg_f080_restatement_revision_proxy_core112_rank_event_count_8q_20q_v113_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(datekey, 8), 20))
def cg_f080_restatement_revision_proxy_core113_rank_event_count_8q_20q_v114_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(lastupdated, 8), 20))
def cg_f080_restatement_revision_proxy_core114_rank_event_count_8q_20q_v115_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(reportperiod, 8), 20))
def cg_f080_restatement_revision_proxy_core115_rank_event_count_8q_20q_v116_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(dimension, 8), 20))
def cg_f080_restatement_revision_proxy_core116_event_flag_alt_v117_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(datekey))
def cg_f080_restatement_revision_proxy_core117_event_flag_alt_v118_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(lastupdated))
def cg_f080_restatement_revision_proxy_core118_event_flag_alt_v119_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(reportperiod))
def cg_f080_restatement_revision_proxy_core119_event_flag_alt_v120_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension))
def cg_f080_restatement_revision_proxy_core120_event_flag_v121_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(datekey))
def cg_f080_restatement_revision_proxy_core121_event_flag_v122_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(lastupdated))
def cg_f080_restatement_revision_proxy_core122_event_flag_v123_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(reportperiod))
def cg_f080_restatement_revision_proxy_core123_event_flag_v124_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_flag(dimension))
def cg_f080_restatement_revision_proxy_core124_event_count_4q_v125_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 4))
def cg_f080_restatement_revision_proxy_core125_event_count_4q_v126_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core126_event_count_4q_v127_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core127_event_count_4q_v128_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 4))
def cg_f080_restatement_revision_proxy_core128_event_count_8q_v129_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(datekey, 8))
def cg_f080_restatement_revision_proxy_core129_event_count_8q_v130_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core130_event_count_8q_v131_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core131_event_count_8q_v132_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_count(dimension, 8))
def cg_f080_restatement_revision_proxy_core132_event_rate_4q_v133_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 4))
def cg_f080_restatement_revision_proxy_core133_event_rate_4q_v134_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core134_event_rate_4q_v135_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core135_event_rate_4q_v136_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 4))
def cg_f080_restatement_revision_proxy_core136_event_rate_8q_v137_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(datekey, 8))
def cg_f080_restatement_revision_proxy_core137_event_rate_8q_v138_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core138_event_rate_8q_v139_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core139_event_rate_8q_v140_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_event_rate(dimension, 8))
def cg_f080_restatement_revision_proxy_core140_autocorr_4q_v141_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 4))
def cg_f080_restatement_revision_proxy_core141_autocorr_4q_v142_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 4))
def cg_f080_restatement_revision_proxy_core142_autocorr_4q_v143_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 4))
def cg_f080_restatement_revision_proxy_core143_autocorr_4q_v144_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 4))
def cg_f080_restatement_revision_proxy_core144_autocorr_8q_v145_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(datekey, 8))
def cg_f080_restatement_revision_proxy_core145_autocorr_8q_v146_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(lastupdated, 8))
def cg_f080_restatement_revision_proxy_core146_autocorr_8q_v147_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(reportperiod, 8))
def cg_f080_restatement_revision_proxy_core147_autocorr_8q_v148_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_autocorr(dimension, 8))
def cg_f080_restatement_revision_proxy_core148_rank_event_count_4q_12q_v149_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(datekey, 4), 12))
def cg_f080_restatement_revision_proxy_core149_rank_event_count_4q_12q_v150_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_event_count(lastupdated, 4), 12))