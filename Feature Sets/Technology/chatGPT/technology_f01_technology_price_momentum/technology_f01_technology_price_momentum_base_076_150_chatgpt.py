import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core05 ewm 63d
def cg_f01_technology_f01_technology_price_momentum_core05_ewm_63d_base_v076_signal(closeadj, volume):
    result = _ewm((_pct_change(closeadj,252)), 63)
    return _clean(result)

# core06 ewm 126d
def cg_f01_technology_f01_technology_price_momentum_core06_ewm_126d_base_v077_signal(closeadj, volume):
    result = _ewm((_pct_change(closeadj,1260)), 126)
    return _clean(result)

# core07 ewm 252d
def cg_f01_technology_f01_technology_price_momentum_core07_ewm_252d_base_v078_signal(closeadj, volume):
    result = _ewm((_safe_div(closeadj, _max(closeadj, 252))-1.0), 252)
    return _clean(result)

# core08 ewm 5d
def cg_f01_technology_f01_technology_price_momentum_core08_ewm_5d_base_v079_signal(closeadj, volume):
    result = _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    return _clean(result)

# core09 ewm 21d
def cg_f01_technology_f01_technology_price_momentum_core09_ewm_21d_base_v080_signal(closeadj, volume):
    result = _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 21)
    return _clean(result)

# core00 skew 126d
def cg_f01_technology_f01_technology_price_momentum_core00_skew_126d_base_v081_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj, 1)), 126)
    return _clean(result)

# core01 skew 252d
def cg_f01_technology_f01_technology_price_momentum_core01_skew_252d_base_v082_signal(closeadj, volume):
    result = _skew((_diff(_log(closeadj),1)), 252)
    return _clean(result)

# core02 skew 5d
def cg_f01_technology_f01_technology_price_momentum_core02_skew_5d_base_v083_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj, 5)), 5)
    return _clean(result)

# core03 skew 21d
def cg_f01_technology_f01_technology_price_momentum_core03_skew_21d_base_v084_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj, 21)), 21)
    return _clean(result)

# core04 skew 63d
def cg_f01_technology_f01_technology_price_momentum_core04_skew_63d_base_v085_signal(closeadj, volume):
    result = _skew((volume), 63)
    return _clean(result)

# core05 skew 126d
def cg_f01_technology_f01_technology_price_momentum_core05_skew_126d_base_v086_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj,252)), 126)
    return _clean(result)

# core06 skew 252d
def cg_f01_technology_f01_technology_price_momentum_core06_skew_252d_base_v087_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj,1260)), 252)
    return _clean(result)

# core07 skew 5d
def cg_f01_technology_f01_technology_price_momentum_core07_skew_5d_base_v088_signal(closeadj, volume):
    result = _skew((_safe_div(closeadj, _max(closeadj, 252))-1.0), 5)
    return _clean(result)

# core08 skew 21d
def cg_f01_technology_f01_technology_price_momentum_core08_skew_21d_base_v089_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 21)
    return _clean(result)

# core09 skew 63d
def cg_f01_technology_f01_technology_price_momentum_core09_skew_63d_base_v090_signal(closeadj, volume):
    result = _skew((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 63)
    return _clean(result)

# core00 kurt 252d
def cg_f01_technology_f01_technology_price_momentum_core00_kurt_252d_base_v091_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj, 1)), 252)
    return _clean(result)

# core01 kurt 5d
def cg_f01_technology_f01_technology_price_momentum_core01_kurt_5d_base_v092_signal(closeadj, volume):
    result = _kurt((_diff(_log(closeadj),1)), 5)
    return _clean(result)

# core02 kurt 21d
def cg_f01_technology_f01_technology_price_momentum_core02_kurt_21d_base_v093_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj, 5)), 21)
    return _clean(result)

# core03 kurt 63d
def cg_f01_technology_f01_technology_price_momentum_core03_kurt_63d_base_v094_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj, 21)), 63)
    return _clean(result)

# core04 kurt 126d
def cg_f01_technology_f01_technology_price_momentum_core04_kurt_126d_base_v095_signal(closeadj, volume):
    result = _kurt((volume), 126)
    return _clean(result)

# core05 kurt 252d
def cg_f01_technology_f01_technology_price_momentum_core05_kurt_252d_base_v096_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj,252)), 252)
    return _clean(result)

# core06 kurt 5d
def cg_f01_technology_f01_technology_price_momentum_core06_kurt_5d_base_v097_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj,1260)), 5)
    return _clean(result)

# core07 kurt 21d
def cg_f01_technology_f01_technology_price_momentum_core07_kurt_21d_base_v098_signal(closeadj, volume):
    result = _kurt((_safe_div(closeadj, _max(closeadj, 252))-1.0), 21)
    return _clean(result)

# core08 kurt 63d
def cg_f01_technology_f01_technology_price_momentum_core08_kurt_63d_base_v099_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63)
    return _clean(result)

# core09 kurt 126d
def cg_f01_technology_f01_technology_price_momentum_core09_kurt_126d_base_v100_signal(closeadj, volume):
    result = _kurt((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 126)
    return _clean(result)

# core00 autocorr 5d
def cg_f01_technology_f01_technology_price_momentum_core00_autocorr_5d_base_v101_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj, 1)), 5)
    return _clean(result)

# core01 autocorr 21d
def cg_f01_technology_f01_technology_price_momentum_core01_autocorr_21d_base_v102_signal(closeadj, volume):
    result = _autocorr((_diff(_log(closeadj),1)), 21)
    return _clean(result)

# core02 autocorr 63d
def cg_f01_technology_f01_technology_price_momentum_core02_autocorr_63d_base_v103_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj, 5)), 63)
    return _clean(result)

# core03 autocorr 126d
def cg_f01_technology_f01_technology_price_momentum_core03_autocorr_126d_base_v104_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj, 21)), 126)
    return _clean(result)

# core04 autocorr 252d
def cg_f01_technology_f01_technology_price_momentum_core04_autocorr_252d_base_v105_signal(closeadj, volume):
    result = _autocorr((volume), 252)
    return _clean(result)

# core05 autocorr 5d
def cg_f01_technology_f01_technology_price_momentum_core05_autocorr_5d_base_v106_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj,252)), 5)
    return _clean(result)

# core06 autocorr 21d
def cg_f01_technology_f01_technology_price_momentum_core06_autocorr_21d_base_v107_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj,1260)), 21)
    return _clean(result)

# core07 autocorr 63d
def cg_f01_technology_f01_technology_price_momentum_core07_autocorr_63d_base_v108_signal(closeadj, volume):
    result = _autocorr((_safe_div(closeadj, _max(closeadj, 252))-1.0), 63)
    return _clean(result)

# core08 autocorr 126d
def cg_f01_technology_f01_technology_price_momentum_core08_autocorr_126d_base_v109_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 126)
    return _clean(result)

# core09 autocorr 252d
def cg_f01_technology_f01_technology_price_momentum_core09_autocorr_252d_base_v110_signal(closeadj, volume):
    result = _autocorr((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 252)
    return _clean(result)

# core00 snr 21d
def cg_f01_technology_f01_technology_price_momentum_core00_snr_21d_base_v111_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj, 1)), max(1, 21//3)).abs(), _std(_diff((_pct_change(closeadj, 1)),1), 21)+1e-9)
    return _clean(result)

# core01 snr 63d
def cg_f01_technology_f01_technology_price_momentum_core01_snr_63d_base_v112_signal(closeadj, volume):
    result = _safe_div(_diff((_diff(_log(closeadj),1)), max(1, 63//3)).abs(), _std(_diff((_diff(_log(closeadj),1)),1), 63)+1e-9)
    return _clean(result)

# core02 snr 126d
def cg_f01_technology_f01_technology_price_momentum_core02_snr_126d_base_v113_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj, 5)), max(1, 126//3)).abs(), _std(_diff((_pct_change(closeadj, 5)),1), 126)+1e-9)
    return _clean(result)

# core03 snr 252d
def cg_f01_technology_f01_technology_price_momentum_core03_snr_252d_base_v114_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj, 21)), max(1, 252//3)).abs(), _std(_diff((_pct_change(closeadj, 21)),1), 252)+1e-9)
    return _clean(result)

# core04 snr 5d
def cg_f01_technology_f01_technology_price_momentum_core04_snr_5d_base_v115_signal(closeadj, volume):
    result = _safe_div(_diff((volume), max(1, 5//3)).abs(), _std(_diff((volume),1), 5)+1e-9)
    return _clean(result)

# core05 snr 21d
def cg_f01_technology_f01_technology_price_momentum_core05_snr_21d_base_v116_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj,252)), max(1, 21//3)).abs(), _std(_diff((_pct_change(closeadj,252)),1), 21)+1e-9)
    return _clean(result)

# core06 snr 63d
def cg_f01_technology_f01_technology_price_momentum_core06_snr_63d_base_v117_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj,1260)), max(1, 63//3)).abs(), _std(_diff((_pct_change(closeadj,1260)),1), 63)+1e-9)
    return _clean(result)

# core07 snr 126d
def cg_f01_technology_f01_technology_price_momentum_core07_snr_126d_base_v118_signal(closeadj, volume):
    result = _safe_div(_diff((_safe_div(closeadj, _max(closeadj, 252))-1.0), max(1, 126//3)).abs(), _std(_diff((_safe_div(closeadj, _max(closeadj, 252))-1.0),1), 126)+1e-9)
    return _clean(result)

# core08 snr 252d
def cg_f01_technology_f01_technology_price_momentum_core08_snr_252d_base_v119_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), max(1, 252//3)).abs(), _std(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)),1), 252)+1e-9)
    return _clean(result)

# core09 snr 5d
def cg_f01_technology_f01_technology_price_momentum_core09_snr_5d_base_v120_signal(closeadj, volume):
    result = _safe_div(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), max(1, 5//3)).abs(), _std(_diff((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()),1), 5)+1e-9)
    return _clean(result)

# core00 ema_gap 63d
def cg_f01_technology_f01_technology_price_momentum_core00_ema_gap_63d_base_v121_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 1)), 63) - _ewm((_pct_change(closeadj, 1)), 63)
    return _clean(result)

# core01 ema_gap 126d
def cg_f01_technology_f01_technology_price_momentum_core01_ema_gap_126d_base_v122_signal(closeadj, volume):
    result = _mean((_diff(_log(closeadj),1)), 126) - _ewm((_diff(_log(closeadj),1)), 126)
    return _clean(result)

# core02 ema_gap 252d
def cg_f01_technology_f01_technology_price_momentum_core02_ema_gap_252d_base_v123_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 5)), 252) - _ewm((_pct_change(closeadj, 5)), 252)
    return _clean(result)

# core03 ema_gap 5d
def cg_f01_technology_f01_technology_price_momentum_core03_ema_gap_5d_base_v124_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 21)), 5) - _ewm((_pct_change(closeadj, 21)), 5)
    return _clean(result)

# core04 ema_gap 21d
def cg_f01_technology_f01_technology_price_momentum_core04_ema_gap_21d_base_v125_signal(closeadj, volume):
    result = _mean((volume), 21) - _ewm((volume), 21)
    return _clean(result)

# core05 ema_gap 63d
def cg_f01_technology_f01_technology_price_momentum_core05_ema_gap_63d_base_v126_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj,252)), 63) - _ewm((_pct_change(closeadj,252)), 63)
    return _clean(result)

# core06 ema_gap 126d
def cg_f01_technology_f01_technology_price_momentum_core06_ema_gap_126d_base_v127_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj,1260)), 126) - _ewm((_pct_change(closeadj,1260)), 126)
    return _clean(result)

# core07 ema_gap 252d
def cg_f01_technology_f01_technology_price_momentum_core07_ema_gap_252d_base_v128_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj, _max(closeadj, 252))-1.0), 252) - _ewm((_safe_div(closeadj, _max(closeadj, 252))-1.0), 252)
    return _clean(result)

# core08 ema_gap 5d
def cg_f01_technology_f01_technology_price_momentum_core08_ema_gap_5d_base_v129_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5) - _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 5)
    return _clean(result)

# core09 ema_gap 21d
def cg_f01_technology_f01_technology_price_momentum_core09_ema_gap_21d_base_v130_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 21) - _ewm((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 21)
    return _clean(result)

# core00 vol_ratio 126d
def cg_f01_technology_f01_technology_price_momentum_core00_vol_ratio_126d_base_v131_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj, 1)), max(2, 126//3)), _std((_pct_change(closeadj, 1)), 126).abs()+1e-9)
    return _clean(result)

# core01 vol_ratio 252d
def cg_f01_technology_f01_technology_price_momentum_core01_vol_ratio_252d_base_v132_signal(closeadj, volume):
    result = _safe_div(_std((_diff(_log(closeadj),1)), max(2, 252//3)), _std((_diff(_log(closeadj),1)), 252).abs()+1e-9)
    return _clean(result)

# core02 vol_ratio 5d
def cg_f01_technology_f01_technology_price_momentum_core02_vol_ratio_5d_base_v133_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj, 5)), max(2, 5//3)), _std((_pct_change(closeadj, 5)), 5).abs()+1e-9)
    return _clean(result)

# core03 vol_ratio 21d
def cg_f01_technology_f01_technology_price_momentum_core03_vol_ratio_21d_base_v134_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj, 21)), max(2, 21//3)), _std((_pct_change(closeadj, 21)), 21).abs()+1e-9)
    return _clean(result)

# core04 vol_ratio 63d
def cg_f01_technology_f01_technology_price_momentum_core04_vol_ratio_63d_base_v135_signal(closeadj, volume):
    result = _safe_div(_std((volume), max(2, 63//3)), _std((volume), 63).abs()+1e-9)
    return _clean(result)

# core05 vol_ratio 126d
def cg_f01_technology_f01_technology_price_momentum_core05_vol_ratio_126d_base_v136_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj,252)), max(2, 126//3)), _std((_pct_change(closeadj,252)), 126).abs()+1e-9)
    return _clean(result)

# core06 vol_ratio 252d
def cg_f01_technology_f01_technology_price_momentum_core06_vol_ratio_252d_base_v137_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj,1260)), max(2, 252//3)), _std((_pct_change(closeadj,1260)), 252).abs()+1e-9)
    return _clean(result)

# core07 vol_ratio 5d
def cg_f01_technology_f01_technology_price_momentum_core07_vol_ratio_5d_base_v138_signal(closeadj, volume):
    result = _safe_div(_std((_safe_div(closeadj, _max(closeadj, 252))-1.0), max(2, 5//3)), _std((_safe_div(closeadj, _max(closeadj, 252))-1.0), 5).abs()+1e-9)
    return _clean(result)

# core08 vol_ratio 21d
def cg_f01_technology_f01_technology_price_momentum_core08_vol_ratio_21d_base_v139_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), max(2, 21//3)), _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 21).abs()+1e-9)
    return _clean(result)

# core09 vol_ratio 63d
def cg_f01_technology_f01_technology_price_momentum_core09_vol_ratio_63d_base_v140_signal(closeadj, volume):
    result = _safe_div(_std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), max(2, 63//3)), _std((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 63).abs()+1e-9)
    return _clean(result)

# core00 recent_vs_long 252d
def cg_f01_technology_f01_technology_price_momentum_core00_recent_vs_long_252d_base_v141_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 1)), max(2, 252//3)) - _mean((_pct_change(closeadj, 1)), 252)
    return _clean(result)

# core01 recent_vs_long 5d
def cg_f01_technology_f01_technology_price_momentum_core01_recent_vs_long_5d_base_v142_signal(closeadj, volume):
    result = _mean((_diff(_log(closeadj),1)), max(2, 5//3)) - _mean((_diff(_log(closeadj),1)), 5)
    return _clean(result)

# core02 recent_vs_long 21d
def cg_f01_technology_f01_technology_price_momentum_core02_recent_vs_long_21d_base_v143_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 5)), max(2, 21//3)) - _mean((_pct_change(closeadj, 5)), 21)
    return _clean(result)

# core03 recent_vs_long 63d
def cg_f01_technology_f01_technology_price_momentum_core03_recent_vs_long_63d_base_v144_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 21)), max(2, 63//3)) - _mean((_pct_change(closeadj, 21)), 63)
    return _clean(result)

# core04 recent_vs_long 126d
def cg_f01_technology_f01_technology_price_momentum_core04_recent_vs_long_126d_base_v145_signal(closeadj, volume):
    result = _mean((volume), max(2, 126//3)) - _mean((volume), 126)
    return _clean(result)

# core05 recent_vs_long 252d
def cg_f01_technology_f01_technology_price_momentum_core05_recent_vs_long_252d_base_v146_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj,252)), max(2, 252//3)) - _mean((_pct_change(closeadj,252)), 252)
    return _clean(result)

# core06 recent_vs_long 5d
def cg_f01_technology_f01_technology_price_momentum_core06_recent_vs_long_5d_base_v147_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj,1260)), max(2, 5//3)) - _mean((_pct_change(closeadj,1260)), 5)
    return _clean(result)

# core07 recent_vs_long 21d
def cg_f01_technology_f01_technology_price_momentum_core07_recent_vs_long_21d_base_v148_signal(closeadj, volume):
    result = _mean((_safe_div(closeadj, _max(closeadj, 252))-1.0), max(2, 21//3)) - _mean((_safe_div(closeadj, _max(closeadj, 252))-1.0), 21)
    return _clean(result)

# core08 recent_vs_long 63d
def cg_f01_technology_f01_technology_price_momentum_core08_recent_vs_long_63d_base_v149_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), max(2, 63//3)) - _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)>0,0)), 63)
    return _clean(result)

# core09 recent_vs_long 126d
def cg_f01_technology_f01_technology_price_momentum_core09_recent_vs_long_126d_base_v150_signal(closeadj, volume):
    result = _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), max(2, 126//3)) - _mean((_pct_change(closeadj, 1).where(_pct_change(closeadj, 1)<0,0).abs()), 126)
    return _clean(result)

