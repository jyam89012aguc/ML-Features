import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 63d (continued)
def cg_f092_insider_transaction_flow_core75_ewm_63d_v076_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_z(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core76_ewm_63d_v077_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_rank(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core77_ewm_63d_v078_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_event_count(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core78_ewm_63d_v079_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_event_rate(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core79_ewm_63d_v080_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_ewm(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 63))

# core80-89: skew 126d
def cg_f092_insider_transaction_flow_core80_skew_126d_v081_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_to_num(transactionvalue), 126))
def cg_f092_insider_transaction_flow_core81_skew_126d_v082_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_to_num(transactionshares), 126))
def cg_f092_insider_transaction_flow_core82_skew_126d_v083_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_to_num(transactionpricepershare), 126))
def cg_f092_insider_transaction_flow_core83_skew_126d_v084_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_event_flag(transactioncode), 126))
def cg_f092_insider_transaction_flow_core84_skew_126d_v085_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_pct_change(_to_num(transactionvalue), 1), 126))
def cg_f092_insider_transaction_flow_core85_skew_126d_v086_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_z(_to_num(transactionvalue), 252), 126))
def cg_f092_insider_transaction_flow_core86_skew_126d_v087_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_rank(_to_num(transactionvalue), 252), 126))
def cg_f092_insider_transaction_flow_core87_skew_126d_v088_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 126))
def cg_f092_insider_transaction_flow_core88_skew_126d_v089_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_event_count(transactioncode, 21), 126))
def cg_f092_insider_transaction_flow_core89_skew_126d_v090_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_skew(_event_rate(transactioncode, 21), 126))

# core90-99: kurt 126d
def cg_f092_insider_transaction_flow_core90_kurt_126d_v091_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_to_num(transactionvalue), 126))
def cg_f092_insider_transaction_flow_core91_kurt_126d_v092_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_to_num(transactionshares), 126))
def cg_f092_insider_transaction_flow_core92_kurt_126d_v093_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_to_num(transactionpricepershare), 126))
def cg_f092_insider_transaction_flow_core93_kurt_126d_v094_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_event_flag(transactioncode), 126))
def cg_f092_insider_transaction_flow_core94_kurt_126d_v095_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_pct_change(_to_num(transactionvalue), 1), 126))
def cg_f092_insider_transaction_flow_core95_kurt_126d_v096_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_z(_to_num(transactionvalue), 252), 126))
def cg_f092_insider_transaction_flow_core96_kurt_126d_v097_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_rank(_to_num(transactionvalue), 252), 126))
def cg_f092_insider_transaction_flow_core97_kurt_126d_v098_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 126))
def cg_f092_insider_transaction_flow_core98_kurt_126d_v099_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_event_count(transactioncode, 21), 126))
def cg_f092_insider_transaction_flow_core99_kurt_126d_v100_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_kurt(_event_rate(transactioncode, 21), 126))

# core100-109: autocorr 63d
def cg_f092_insider_transaction_flow_core100_autocorr_63d_v101_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_to_num(transactionvalue), 63))
def cg_f092_insider_transaction_flow_core101_autocorr_63d_v102_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core102_autocorr_63d_v103_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_event_flag(transactioncode), 63))
def cg_f092_insider_transaction_flow_core103_autocorr_63d_v104_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_event_count(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core104_autocorr_63d_v105_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_z(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core105_autocorr_63d_v106_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_rank(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core106_autocorr_63d_v107_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_pct_change(_to_num(transactionvalue), 1), 63))
def cg_f092_insider_transaction_flow_core107_autocorr_63d_v108_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 63))
def cg_f092_insider_transaction_flow_core108_autocorr_63d_v109_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_event_rate(transactioncode, 21), 63))
def cg_f092_insider_transaction_flow_core109_autocorr_63d_v110_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_autocorr(_to_num(transactionpricepershare), 63))

# core110-119: corr with shares 63d
def cg_f092_insider_transaction_flow_core110_corr_shares_63d_v111_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_to_num(transactionvalue), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core111_corr_shares_63d_v112_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_event_flag(transactioncode), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core112_corr_shares_63d_v113_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_event_count(transactioncode, 21), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core113_corr_shares_63d_v114_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_z(_to_num(transactionvalue), 252), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core114_corr_shares_63d_v115_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_rank(_to_num(transactionvalue), 252), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core115_corr_shares_63d_v116_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_pct_change(_to_num(transactionvalue), 1), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core116_corr_shares_63d_v117_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_to_num(transactionpricepershare), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core117_corr_shares_63d_v118_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_event_rate(transactioncode, 21), _to_num(transactionshares), 63))
def cg_f092_insider_transaction_flow_core118_corr_shares_63d_v119_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_to_num(transactionvalue), _mean(_to_num(transactionvalue), 252), 63))
def cg_f092_insider_transaction_flow_core119_corr_shares_63d_v120_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_corr(_to_num(transactionshares), _mean(_to_num(transactionshares), 252), 63))

# core120-129: stability 63d
def cg_f092_insider_transaction_flow_core120_stability_63d_v121_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _to_num(transactionvalue)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core121_stability_63d_v122_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _to_num(transactionshares)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core122_stability_63d_v123_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _event_flag(transactioncode)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core123_stability_63d_v124_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _event_count(transactioncode, 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core124_stability_63d_v125_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _z(_to_num(transactionvalue), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core125_stability_63d_v126_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _rank(_to_num(transactionvalue), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core126_stability_63d_v127_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _pct_change(_to_num(transactionvalue), 1)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core127_stability_63d_v128_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _safe_div(_to_num(transactionvalue), _to_num(transactionshares))
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core128_stability_63d_v129_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _event_rate(transactioncode, 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f092_insider_transaction_flow_core129_stability_63d_v130_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    base = _to_num(transactionpricepershare)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))

# core130-139: diff 21d
def cg_f092_insider_transaction_flow_core130_diff_21d_v131_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_to_num(transactionvalue), 21))
def cg_f092_insider_transaction_flow_core131_diff_21d_v132_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_to_num(transactionshares), 21))
def cg_f092_insider_transaction_flow_core132_diff_21d_v133_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_event_count(transactioncode, 21), 21))
def cg_f092_insider_transaction_flow_core133_diff_21d_v134_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_z(_to_num(transactionvalue), 252), 21))
def cg_f092_insider_transaction_flow_core134_diff_21d_v135_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_rank(_to_num(transactionvalue), 252), 21))
def cg_f092_insider_transaction_flow_core135_diff_21d_v136_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_pct_change(_to_num(transactionvalue), 1), 21))
def cg_f092_insider_transaction_flow_core136_diff_21d_v137_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_safe_div(_to_num(transactionvalue), _to_num(transactionshares)), 21))
def cg_f092_insider_transaction_flow_core137_diff_21d_v138_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_event_rate(transactioncode, 21), 21))
def cg_f092_insider_transaction_flow_core138_diff_21d_v139_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_to_num(transactionpricepershare), 21))
def cg_f092_insider_transaction_flow_core139_diff_21d_v140_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(_to_num(transactionvalue), 63), 21))

# core140-149: levels
def cg_f092_insider_transaction_flow_core140_level_v141_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_to_num(transactionvalue))
def cg_f092_insider_transaction_flow_core141_shares_v142_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_to_num(transactionshares))
def cg_f092_insider_transaction_flow_core142_price_v143_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_to_num(transactionpricepershare))
def cg_f092_insider_transaction_flow_core143_event_flag_v144_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _event_flag(transactioncode)
def cg_f092_insider_transaction_flow_core144_buy_flag_v145_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return (transactioncode == 'P').astype(float)
def cg_f092_insider_transaction_flow_core145_sell_flag_v146_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return (transactioncode == 'S').astype(float)
def cg_f092_insider_transaction_flow_core146_value_z_v147_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _z(_to_num(transactionvalue), 252)
def cg_f092_insider_transaction_flow_core147_shares_z_v148_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _z(_to_num(transactionshares), 252)
def cg_f092_insider_transaction_flow_core148_value_rank_v149_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _rank(_to_num(transactionvalue), 252)
def cg_f092_insider_transaction_flow_core149_shares_rank_v150_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _rank(_to_num(transactionshares), 252)
