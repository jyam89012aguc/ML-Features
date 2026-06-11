import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-79: ewm 63d (continued)
def cg_f094_insider_ownership_after_trade_core75_ewm_63d_v076_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_z(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core76_ewm_63d_v077_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_rank(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core77_ewm_63d_v078_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 63))
def cg_f094_insider_ownership_after_trade_core78_ewm_63d_v079_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_diff(_to_num(sharesownedfollowingtransaction), 21), 63))
def cg_f094_insider_ownership_after_trade_core79_ewm_63d_v080_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_ewm(_z(_to_num(transactionshares), 252), 63))

# core80-89: skew 126d
def cg_f094_insider_ownership_after_trade_core80_skew_126d_v081_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_to_num(sharesownedfollowingtransaction), 126))
def cg_f094_insider_ownership_after_trade_core81_skew_126d_v082_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_to_num(transactionshares), 126))
def cg_f094_insider_ownership_after_trade_core82_skew_126d_v083_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_to_num(sharesownedbeforetransaction), 126))
def cg_f094_insider_ownership_after_trade_core83_skew_126d_v084_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 126))
def cg_f094_insider_ownership_after_trade_core84_skew_126d_v085_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 126))
def cg_f094_insider_ownership_after_trade_core85_skew_126d_v086_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_z(_to_num(sharesownedfollowingtransaction), 252), 126))
def cg_f094_insider_ownership_after_trade_core86_skew_126d_v087_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_rank(_to_num(sharesownedfollowingtransaction), 252), 126))
def cg_f094_insider_ownership_after_trade_core87_skew_126d_v088_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 126))
def cg_f094_insider_ownership_after_trade_core88_skew_126d_v089_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_diff(_to_num(sharesownedfollowingtransaction), 21), 126))
def cg_f094_insider_ownership_after_trade_core89_skew_126d_v090_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_skew(_z(_to_num(transactionshares), 252), 126))

# core90-99: kurt 126d
def cg_f094_insider_ownership_after_trade_core90_kurt_126d_v091_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_to_num(sharesownedfollowingtransaction), 126))
def cg_f094_insider_ownership_after_trade_core91_kurt_126d_v092_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_to_num(transactionshares), 126))
def cg_f094_insider_ownership_after_trade_core92_kurt_126d_v093_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_to_num(sharesownedbeforetransaction), 126))
def cg_f094_insider_ownership_after_trade_core93_kurt_126d_v094_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 126))
def cg_f094_insider_ownership_after_trade_core94_kurt_126d_v095_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 126))
def cg_f094_insider_ownership_after_trade_core95_kurt_126d_v096_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_z(_to_num(sharesownedfollowingtransaction), 252), 126))
def cg_f094_insider_ownership_after_trade_core96_kurt_126d_v097_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_rank(_to_num(sharesownedfollowingtransaction), 252), 126))
def cg_f094_insider_ownership_after_trade_core97_kurt_126d_v098_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 126))
def cg_f094_insider_ownership_after_trade_core98_kurt_126d_v099_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_diff(_to_num(sharesownedfollowingtransaction), 21), 126))
def cg_f094_insider_ownership_after_trade_core99_kurt_126d_v100_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_kurt(_z(_to_num(transactionshares), 252), 126))

# core100-109: autocorr 63d
def cg_f094_insider_ownership_after_trade_core100_autocorr_63d_v101_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_to_num(sharesownedfollowingtransaction), 63))
def cg_f094_insider_ownership_after_trade_core101_autocorr_63d_v102_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core102_autocorr_63d_v103_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 63))
def cg_f094_insider_ownership_after_trade_core103_autocorr_63d_v104_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 63))
def cg_f094_insider_ownership_after_trade_core104_autocorr_63d_v105_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_z(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core105_autocorr_63d_v106_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_rank(_to_num(sharesownedfollowingtransaction), 252), 63))
def cg_f094_insider_ownership_after_trade_core106_autocorr_63d_v107_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_diff(_to_num(sharesownedfollowingtransaction), 21), 63))
def cg_f094_insider_ownership_after_trade_core107_autocorr_63d_v108_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 63))
def cg_f094_insider_ownership_after_trade_core108_autocorr_63d_v109_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_z(_to_num(transactionshares), 252), 63))
def cg_f094_insider_ownership_after_trade_core109_autocorr_63d_v110_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_autocorr(_to_num(sharesownedbeforetransaction), 63))

# core110-119: corr with transactionshares 63d
def cg_f094_insider_ownership_after_trade_core110_corr_shares_63d_v111_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_to_num(sharesownedfollowingtransaction), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core111_corr_shares_63d_v112_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_to_num(sharesownedbeforetransaction), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core112_corr_shares_63d_v113_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core113_corr_shares_63d_v114_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_z(_to_num(sharesownedfollowingtransaction), 252), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core114_corr_shares_63d_v115_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_rank(_to_num(sharesownedfollowingtransaction), 252), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core115_corr_shares_63d_v116_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_pct_change(_to_num(sharesownedfollowingtransaction), 1), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core116_corr_shares_63d_v117_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_diff(_to_num(sharesownedfollowingtransaction), 21), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core117_corr_shares_63d_v118_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core118_corr_shares_63d_v119_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_z(_to_num(transactionshares), 252), _to_num(transactionshares), 63))
def cg_f094_insider_ownership_after_trade_core119_corr_shares_63d_v120_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_corr(_to_num(sharesownedfollowingtransaction), _mean(_to_num(sharesownedfollowingtransaction), 252), 63))

# core120-129: stability 63d
def cg_f094_insider_ownership_after_trade_core120_stability_63d_v121_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _to_num(sharesownedfollowingtransaction)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core121_stability_63d_v122_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _to_num(transactionshares)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core122_stability_63d_v123_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction))
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core123_stability_63d_v124_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _pct_change(_to_num(sharesownedfollowingtransaction), 1)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core124_stability_63d_v125_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _z(_to_num(sharesownedfollowingtransaction), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core125_stability_63d_v126_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _rank(_to_num(sharesownedfollowingtransaction), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core126_stability_63d_v127_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _diff(_to_num(sharesownedfollowingtransaction), 21)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core127_stability_63d_v128_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction))
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core128_stability_63d_v129_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _z(_to_num(transactionshares), 252)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))
def cg_f094_insider_ownership_after_trade_core129_stability_63d_v130_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    base = _to_num(sharesownedbeforetransaction)
    return _clean(_safe_div(_std(base, 63), _mean(base, 63)))

# core130-139: diff 21d
def cg_f094_insider_ownership_after_trade_core130_diff_21d_v131_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_to_num(sharesownedfollowingtransaction), 21))
def cg_f094_insider_ownership_after_trade_core131_diff_21d_v132_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_to_num(transactionshares), 21))
def cg_f094_insider_ownership_after_trade_core132_diff_21d_v133_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)), 21))
def cg_f094_insider_ownership_after_trade_core133_diff_21d_v134_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_z(_to_num(sharesownedfollowingtransaction), 252), 21))
def cg_f094_insider_ownership_after_trade_core134_diff_21d_v135_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_rank(_to_num(sharesownedfollowingtransaction), 252), 21))
def cg_f094_insider_ownership_after_trade_core135_diff_21d_v136_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_pct_change(_to_num(sharesownedfollowingtransaction), 1), 21))
def cg_f094_insider_ownership_after_trade_core136_diff_21d_v137_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_diff(_to_num(sharesownedfollowingtransaction), 21), 21))
def cg_f094_insider_ownership_after_trade_core137_diff_21d_v138_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_safe_div(_to_num(transactionshares), _to_num(sharesownedfollowingtransaction)), 21))
def cg_f094_insider_ownership_after_trade_core138_diff_21d_v139_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_z(_to_num(transactionshares), 252), 21))
def cg_f094_insider_ownership_after_trade_core139_diff_21d_v140_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_diff(_to_num(sharesownedbeforetransaction), 21))

# core140-149: levels
def cg_f094_insider_ownership_after_trade_core140_following_v141_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_to_num(sharesownedfollowingtransaction))
def cg_f094_insider_ownership_after_trade_core141_transaction_v142_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_to_num(transactionshares))
def cg_f094_insider_ownership_after_trade_core142_before_v143_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_to_num(sharesownedbeforetransaction))
def cg_f094_insider_ownership_after_trade_core143_ratio_v144_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_safe_div(_to_num(transactionshares), _to_num(sharesownedbeforetransaction)))
def cg_f094_insider_ownership_after_trade_core144_following_z_v145_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _z(_to_num(sharesownedfollowingtransaction), 252)
def cg_f094_insider_ownership_after_trade_core145_transaction_z_v146_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _z(_to_num(transactionshares), 252)
def cg_f094_insider_ownership_after_trade_core146_following_rank_v147_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _rank(_to_num(sharesownedfollowingtransaction), 252)
def cg_f094_insider_ownership_after_trade_core147_transaction_rank_v148_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _rank(_to_num(transactionshares), 252)
def cg_f094_insider_ownership_after_trade_core148_ownership_diff_v149_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_to_num(sharesownedfollowingtransaction) - _to_num(sharesownedbeforetransaction))
def cg_f094_insider_ownership_after_trade_core149_pct_owned_v150_signal(sharesownedfollowingtransaction, transactionshares, sharesownedbeforetransaction):
    return _clean(_safe_div(_to_num(sharesownedfollowingtransaction), _to_num(sharesownedbeforetransaction)))
