import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f081_company_identity_metadata_core75_autocorr_12q_v076_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(category, 12))
def cg_f081_company_identity_metadata_core76_autocorr_12q_v077_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(siccode, 12))
def cg_f081_company_identity_metadata_core77_autocorr_12q_v078_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(scalemarketcap, 12))
def cg_f081_company_identity_metadata_core78_rank_event_count_8q_20q_v079_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(ticker, 8), 20))
def cg_f081_company_identity_metadata_core79_rank_event_count_8q_20q_v080_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(name, 8), 20))
def cg_f081_company_identity_metadata_core80_rank_event_count_8q_20q_v081_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(exchange, 8), 20))
def cg_f081_company_identity_metadata_core81_rank_event_count_8q_20q_v082_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(category, 8), 20))
def cg_f081_company_identity_metadata_core82_rank_event_count_8q_20q_v083_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(siccode, 8), 20))
def cg_f081_company_identity_metadata_core83_rank_event_count_8q_20q_v084_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(scalemarketcap, 8), 20))
def cg_f081_company_identity_metadata_core84_event_flag_alt_v085_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(ticker))
def cg_f081_company_identity_metadata_core85_event_flag_alt_v086_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(name))
def cg_f081_company_identity_metadata_core86_event_flag_alt_v087_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(exchange))
def cg_f081_company_identity_metadata_core87_event_flag_alt_v088_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(category))
def cg_f081_company_identity_metadata_core88_event_flag_alt_v089_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(siccode))
def cg_f081_company_identity_metadata_core89_event_flag_alt_v090_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(scalemarketcap))
def cg_f081_company_identity_metadata_core90_event_flag_v091_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(ticker))
def cg_f081_company_identity_metadata_core91_event_flag_v092_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(name))
def cg_f081_company_identity_metadata_core92_event_flag_v093_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(exchange))
def cg_f081_company_identity_metadata_core93_event_flag_v094_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(category))
def cg_f081_company_identity_metadata_core94_event_flag_v095_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(siccode))
def cg_f081_company_identity_metadata_core95_event_flag_v096_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(scalemarketcap))
def cg_f081_company_identity_metadata_core96_event_count_4q_v097_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(ticker, 4))
def cg_f081_company_identity_metadata_core97_event_count_4q_v098_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(name, 4))
def cg_f081_company_identity_metadata_core98_event_count_4q_v099_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(exchange, 4))
def cg_f081_company_identity_metadata_core99_event_count_4q_v100_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(category, 4))
def cg_f081_company_identity_metadata_core100_event_count_4q_v101_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(siccode, 4))
def cg_f081_company_identity_metadata_core101_event_count_4q_v102_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(scalemarketcap, 4))
def cg_f081_company_identity_metadata_core102_event_count_8q_v103_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(ticker, 8))
def cg_f081_company_identity_metadata_core103_event_count_8q_v104_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(name, 8))
def cg_f081_company_identity_metadata_core104_event_count_8q_v105_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(exchange, 8))
def cg_f081_company_identity_metadata_core105_event_count_8q_v106_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(category, 8))
def cg_f081_company_identity_metadata_core106_event_count_8q_v107_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(siccode, 8))
def cg_f081_company_identity_metadata_core107_event_count_8q_v108_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_count(scalemarketcap, 8))
def cg_f081_company_identity_metadata_core108_event_rate_4q_v109_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(ticker, 4))
def cg_f081_company_identity_metadata_core109_event_rate_4q_v110_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(name, 4))
def cg_f081_company_identity_metadata_core110_event_rate_4q_v111_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(exchange, 4))
def cg_f081_company_identity_metadata_core111_event_rate_4q_v112_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(category, 4))
def cg_f081_company_identity_metadata_core112_event_rate_4q_v113_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(siccode, 4))
def cg_f081_company_identity_metadata_core113_event_rate_4q_v114_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(scalemarketcap, 4))
def cg_f081_company_identity_metadata_core114_event_rate_8q_v115_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(ticker, 8))
def cg_f081_company_identity_metadata_core115_event_rate_8q_v116_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(name, 8))
def cg_f081_company_identity_metadata_core116_event_rate_8q_v117_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(exchange, 8))
def cg_f081_company_identity_metadata_core117_event_rate_8q_v118_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(category, 8))
def cg_f081_company_identity_metadata_core118_event_rate_8q_v119_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(siccode, 8))
def cg_f081_company_identity_metadata_core119_event_rate_8q_v120_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_rate(scalemarketcap, 8))
def cg_f081_company_identity_metadata_core120_autocorr_4q_v121_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(ticker, 4))
def cg_f081_company_identity_metadata_core121_autocorr_4q_v122_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(name, 4))
def cg_f081_company_identity_metadata_core122_autocorr_4q_v123_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(exchange, 4))
def cg_f081_company_identity_metadata_core123_autocorr_4q_v124_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(category, 4))
def cg_f081_company_identity_metadata_core124_autocorr_4q_v125_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(siccode, 4))
def cg_f081_company_identity_metadata_core125_autocorr_4q_v126_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(scalemarketcap, 4))
def cg_f081_company_identity_metadata_core126_autocorr_8q_v127_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(ticker, 8))
def cg_f081_company_identity_metadata_core127_autocorr_8q_v128_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(name, 8))
def cg_f081_company_identity_metadata_core128_autocorr_8q_v129_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(exchange, 8))
def cg_f081_company_identity_metadata_core129_autocorr_8q_v130_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(category, 8))
def cg_f081_company_identity_metadata_core130_autocorr_8q_v131_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(siccode, 8))
def cg_f081_company_identity_metadata_core131_autocorr_8q_v132_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_autocorr(scalemarketcap, 8))
def cg_f081_company_identity_metadata_core132_rank_event_count_4q_12q_v133_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(ticker, 4), 12))
def cg_f081_company_identity_metadata_core133_rank_event_count_4q_12q_v134_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(name, 4), 12))
def cg_f081_company_identity_metadata_core134_rank_event_count_4q_12q_v135_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(exchange, 4), 12))
def cg_f081_company_identity_metadata_core135_rank_event_count_4q_12q_v136_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(category, 4), 12))
def cg_f081_company_identity_metadata_core136_rank_event_count_4q_12q_v137_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(siccode, 4), 12))
def cg_f081_company_identity_metadata_core137_rank_event_count_4q_12q_v138_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_count(scalemarketcap, 4), 12))
def cg_f081_company_identity_metadata_core138_rank_event_rate_4q_12q_v139_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(ticker, 4), 12))
def cg_f081_company_identity_metadata_core139_rank_event_rate_4q_12q_v140_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(name, 4), 12))
def cg_f081_company_identity_metadata_core140_rank_event_rate_4q_12q_v141_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(exchange, 4), 12))
def cg_f081_company_identity_metadata_core141_rank_event_rate_4q_12q_v142_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(category, 4), 12))
def cg_f081_company_identity_metadata_core142_rank_event_rate_4q_12q_v143_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(siccode, 4), 12))
def cg_f081_company_identity_metadata_core143_rank_event_rate_4q_12q_v144_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_rank(_event_rate(scalemarketcap, 4), 12))
def cg_f081_company_identity_metadata_core144_event_diff_1q_v145_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(ticker).diff(1))
def cg_f081_company_identity_metadata_core145_event_diff_1q_v146_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(name).diff(1))
def cg_f081_company_identity_metadata_core146_event_diff_1q_v147_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(exchange).diff(1))
def cg_f081_company_identity_metadata_core147_event_diff_1q_v148_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(category).diff(1))
def cg_f081_company_identity_metadata_core148_event_diff_1q_v149_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(siccode).diff(1))
def cg_f081_company_identity_metadata_core149_event_diff_1q_v150_signal(ticker, name, exchange, category, siccode, scalemarketcap):
    return _clean(_event_flag(scalemarketcap).diff(1))