import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core05 ewm 63d
def cg_f10_technology_f10_technology_price_compression_core05_ewm_63d_base_v076_signal(high, low, closeadj, volume):
    result = _ewm((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 63)
    return _clean(result)

# core06 ewm 126d
def cg_f10_technology_f10_technology_price_compression_core06_ewm_126d_base_v077_signal(high, low, closeadj, volume):
    result = _ewm((_std(_pct_change(closeadj,1),21)), 126)
    return _clean(result)

# core07 ewm 252d
def cg_f10_technology_f10_technology_price_compression_core07_ewm_252d_base_v078_signal(high, low, closeadj, volume):
    result = _ewm((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 252)
    return _clean(result)

# core08 ewm 5d
def cg_f10_technology_f10_technology_price_compression_core08_ewm_5d_base_v079_signal(high, low, closeadj, volume):
    result = _ewm(((_rank(high-low,63)<0.25).astype(float)), 5)
    return _clean(result)

# core09 ewm 21d
def cg_f10_technology_f10_technology_price_compression_core09_ewm_21d_base_v080_signal(high, low, closeadj, volume):
    result = _ewm((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 21)
    return _clean(result)

# core00 skew 126d
def cg_f10_technology_f10_technology_price_compression_core00_skew_126d_base_v081_signal(high, low, closeadj, volume):
    result = _skew((_safe_div(high-low,closeadj.abs()+1e-9)), 126)
    return _clean(result)

# core01 skew 252d
def cg_f10_technology_f10_technology_price_compression_core01_skew_252d_base_v082_signal(high, low, closeadj, volume):
    result = _skew((high-low), 252)
    return _clean(result)

# core02 skew 5d
def cg_f10_technology_f10_technology_price_compression_core02_skew_5d_base_v083_signal(high, low, closeadj, volume):
    result = _skew((_std(closeadj,21)), 5)
    return _clean(result)

# core03 skew 21d
def cg_f10_technology_f10_technology_price_compression_core03_skew_21d_base_v084_signal(high, low, closeadj, volume):
    result = _skew((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 21)
    return _clean(result)

# core04 skew 63d
def cg_f10_technology_f10_technology_price_compression_core04_skew_63d_base_v085_signal(high, low, closeadj, volume):
    result = _skew(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 63)
    return _clean(result)

# core05 skew 126d
def cg_f10_technology_f10_technology_price_compression_core05_skew_126d_base_v086_signal(high, low, closeadj, volume):
    result = _skew((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 126)
    return _clean(result)

# core06 skew 252d
def cg_f10_technology_f10_technology_price_compression_core06_skew_252d_base_v087_signal(high, low, closeadj, volume):
    result = _skew((_std(_pct_change(closeadj,1),21)), 252)
    return _clean(result)

# core07 skew 5d
def cg_f10_technology_f10_technology_price_compression_core07_skew_5d_base_v088_signal(high, low, closeadj, volume):
    result = _skew((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 5)
    return _clean(result)

# core08 skew 21d
def cg_f10_technology_f10_technology_price_compression_core08_skew_21d_base_v089_signal(high, low, closeadj, volume):
    result = _skew(((_rank(high-low,63)<0.25).astype(float)), 21)
    return _clean(result)

# core09 skew 63d
def cg_f10_technology_f10_technology_price_compression_core09_skew_63d_base_v090_signal(high, low, closeadj, volume):
    result = _skew((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 63)
    return _clean(result)

# core00 kurt 252d
def cg_f10_technology_f10_technology_price_compression_core00_kurt_252d_base_v091_signal(high, low, closeadj, volume):
    result = _kurt((_safe_div(high-low,closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core01 kurt 5d
def cg_f10_technology_f10_technology_price_compression_core01_kurt_5d_base_v092_signal(high, low, closeadj, volume):
    result = _kurt((high-low), 5)
    return _clean(result)

# core02 kurt 21d
def cg_f10_technology_f10_technology_price_compression_core02_kurt_21d_base_v093_signal(high, low, closeadj, volume):
    result = _kurt((_std(closeadj,21)), 21)
    return _clean(result)

# core03 kurt 63d
def cg_f10_technology_f10_technology_price_compression_core03_kurt_63d_base_v094_signal(high, low, closeadj, volume):
    result = _kurt((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 63)
    return _clean(result)

# core04 kurt 126d
def cg_f10_technology_f10_technology_price_compression_core04_kurt_126d_base_v095_signal(high, low, closeadj, volume):
    result = _kurt(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 126)
    return _clean(result)

# core05 kurt 252d
def cg_f10_technology_f10_technology_price_compression_core05_kurt_252d_base_v096_signal(high, low, closeadj, volume):
    result = _kurt((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 252)
    return _clean(result)

# core06 kurt 5d
def cg_f10_technology_f10_technology_price_compression_core06_kurt_5d_base_v097_signal(high, low, closeadj, volume):
    result = _kurt((_std(_pct_change(closeadj,1),21)), 5)
    return _clean(result)

# core07 kurt 21d
def cg_f10_technology_f10_technology_price_compression_core07_kurt_21d_base_v098_signal(high, low, closeadj, volume):
    result = _kurt((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 21)
    return _clean(result)

# core08 kurt 63d
def cg_f10_technology_f10_technology_price_compression_core08_kurt_63d_base_v099_signal(high, low, closeadj, volume):
    result = _kurt(((_rank(high-low,63)<0.25).astype(float)), 63)
    return _clean(result)

# core09 kurt 126d
def cg_f10_technology_f10_technology_price_compression_core09_kurt_126d_base_v100_signal(high, low, closeadj, volume):
    result = _kurt((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 126)
    return _clean(result)

# core00 autocorr 5d
def cg_f10_technology_f10_technology_price_compression_core00_autocorr_5d_base_v101_signal(high, low, closeadj, volume):
    result = _autocorr((_safe_div(high-low,closeadj.abs()+1e-9)), 5)
    return _clean(result)

# core01 autocorr 21d
def cg_f10_technology_f10_technology_price_compression_core01_autocorr_21d_base_v102_signal(high, low, closeadj, volume):
    result = _autocorr((high-low), 21)
    return _clean(result)

# core02 autocorr 63d
def cg_f10_technology_f10_technology_price_compression_core02_autocorr_63d_base_v103_signal(high, low, closeadj, volume):
    result = _autocorr((_std(closeadj,21)), 63)
    return _clean(result)

# core03 autocorr 126d
def cg_f10_technology_f10_technology_price_compression_core03_autocorr_126d_base_v104_signal(high, low, closeadj, volume):
    result = _autocorr((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 126)
    return _clean(result)

# core04 autocorr 252d
def cg_f10_technology_f10_technology_price_compression_core04_autocorr_252d_base_v105_signal(high, low, closeadj, volume):
    result = _autocorr(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 252)
    return _clean(result)

# core05 autocorr 5d
def cg_f10_technology_f10_technology_price_compression_core05_autocorr_5d_base_v106_signal(high, low, closeadj, volume):
    result = _autocorr((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 5)
    return _clean(result)

# core06 autocorr 21d
def cg_f10_technology_f10_technology_price_compression_core06_autocorr_21d_base_v107_signal(high, low, closeadj, volume):
    result = _autocorr((_std(_pct_change(closeadj,1),21)), 21)
    return _clean(result)

# core07 autocorr 63d
def cg_f10_technology_f10_technology_price_compression_core07_autocorr_63d_base_v108_signal(high, low, closeadj, volume):
    result = _autocorr((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 63)
    return _clean(result)

# core08 autocorr 126d
def cg_f10_technology_f10_technology_price_compression_core08_autocorr_126d_base_v109_signal(high, low, closeadj, volume):
    result = _autocorr(((_rank(high-low,63)<0.25).astype(float)), 126)
    return _clean(result)

# core09 autocorr 252d
def cg_f10_technology_f10_technology_price_compression_core09_autocorr_252d_base_v110_signal(high, low, closeadj, volume):
    result = _autocorr((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 252)
    return _clean(result)

# core00 snr 21d
def cg_f10_technology_f10_technology_price_compression_core00_snr_21d_base_v111_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((_safe_div(high-low,closeadj.abs()+1e-9)), max(1,21//3)).abs(), _std(_diff((_safe_div(high-low,closeadj.abs()+1e-9)),1), 21)+1e-9)
    return _clean(result)

# core01 snr 63d
def cg_f10_technology_f10_technology_price_compression_core01_snr_63d_base_v112_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((high-low), max(1,63//3)).abs(), _std(_diff((high-low),1), 63)+1e-9)
    return _clean(result)

# core02 snr 126d
def cg_f10_technology_f10_technology_price_compression_core02_snr_126d_base_v113_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((_std(closeadj,21)), max(1,126//3)).abs(), _std(_diff((_std(closeadj,21)),1), 126)+1e-9)
    return _clean(result)

# core03 snr 252d
def cg_f10_technology_f10_technology_price_compression_core03_snr_252d_base_v114_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), max(1,252//3)).abs(), _std(_diff((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)),1), 252)+1e-9)
    return _clean(result)

# core04 snr 5d
def cg_f10_technology_f10_technology_price_compression_core04_snr_5d_base_v115_signal(high, low, closeadj, volume):
    result = _safe_div(_diff(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), max(1,5//3)).abs(), _std(_diff(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))),1), 5)+1e-9)
    return _clean(result)

# core05 snr 21d
def cg_f10_technology_f10_technology_price_compression_core05_snr_21d_base_v116_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), max(1,21//3)).abs(), _std(_diff((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)),1), 21)+1e-9)
    return _clean(result)

# core06 snr 63d
def cg_f10_technology_f10_technology_price_compression_core06_snr_63d_base_v117_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((_std(_pct_change(closeadj,1),21)), max(1,63//3)).abs(), _std(_diff((_std(_pct_change(closeadj,1),21)),1), 63)+1e-9)
    return _clean(result)

# core07 snr 126d
def cg_f10_technology_f10_technology_price_compression_core07_snr_126d_base_v118_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), max(1,126//3)).abs(), _std(_diff((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)),1), 126)+1e-9)
    return _clean(result)

# core08 snr 252d
def cg_f10_technology_f10_technology_price_compression_core08_snr_252d_base_v119_signal(high, low, closeadj, volume):
    result = _safe_div(_diff(((_rank(high-low,63)<0.25).astype(float)), max(1,252//3)).abs(), _std(_diff(((_rank(high-low,63)<0.25).astype(float)),1), 252)+1e-9)
    return _clean(result)

# core09 snr 5d
def cg_f10_technology_f10_technology_price_compression_core09_snr_5d_base_v120_signal(high, low, closeadj, volume):
    result = _safe_div(_diff((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), max(1,5//3)).abs(), _std(_diff((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)),1), 5)+1e-9)
    return _clean(result)

# core00 ema_gap 63d
def cg_f10_technology_f10_technology_price_compression_core00_ema_gap_63d_base_v121_signal(high, low, closeadj, volume):
    result = _mean((_safe_div(high-low,closeadj.abs()+1e-9)), 63) - _ewm((_safe_div(high-low,closeadj.abs()+1e-9)), 63)
    return _clean(result)

# core01 ema_gap 126d
def cg_f10_technology_f10_technology_price_compression_core01_ema_gap_126d_base_v122_signal(high, low, closeadj, volume):
    result = _mean((high-low), 126) - _ewm((high-low), 126)
    return _clean(result)

# core02 ema_gap 252d
def cg_f10_technology_f10_technology_price_compression_core02_ema_gap_252d_base_v123_signal(high, low, closeadj, volume):
    result = _mean((_std(closeadj,21)), 252) - _ewm((_std(closeadj,21)), 252)
    return _clean(result)

# core03 ema_gap 5d
def cg_f10_technology_f10_technology_price_compression_core03_ema_gap_5d_base_v124_signal(high, low, closeadj, volume):
    result = _mean((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 5) - _ewm((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 5)
    return _clean(result)

# core04 ema_gap 21d
def cg_f10_technology_f10_technology_price_compression_core04_ema_gap_21d_base_v125_signal(high, low, closeadj, volume):
    result = _mean(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 21) - _ewm(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 21)
    return _clean(result)

# core05 ema_gap 63d
def cg_f10_technology_f10_technology_price_compression_core05_ema_gap_63d_base_v126_signal(high, low, closeadj, volume):
    result = _mean((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 63) - _ewm((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 63)
    return _clean(result)

# core06 ema_gap 126d
def cg_f10_technology_f10_technology_price_compression_core06_ema_gap_126d_base_v127_signal(high, low, closeadj, volume):
    result = _mean((_std(_pct_change(closeadj,1),21)), 126) - _ewm((_std(_pct_change(closeadj,1),21)), 126)
    return _clean(result)

# core07 ema_gap 252d
def cg_f10_technology_f10_technology_price_compression_core07_ema_gap_252d_base_v128_signal(high, low, closeadj, volume):
    result = _mean((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 252) - _ewm((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 252)
    return _clean(result)

# core08 ema_gap 5d
def cg_f10_technology_f10_technology_price_compression_core08_ema_gap_5d_base_v129_signal(high, low, closeadj, volume):
    result = _mean(((_rank(high-low,63)<0.25).astype(float)), 5) - _ewm(((_rank(high-low,63)<0.25).astype(float)), 5)
    return _clean(result)

# core09 ema_gap 21d
def cg_f10_technology_f10_technology_price_compression_core09_ema_gap_21d_base_v130_signal(high, low, closeadj, volume):
    result = _mean((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 21) - _ewm((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 21)
    return _clean(result)

# core00 vol_ratio 126d
def cg_f10_technology_f10_technology_price_compression_core00_vol_ratio_126d_base_v131_signal(high, low, closeadj, volume):
    result = _safe_div(_std((_safe_div(high-low,closeadj.abs()+1e-9)), max(2,126//3)), _std((_safe_div(high-low,closeadj.abs()+1e-9)), 126).abs()+1e-9)
    return _clean(result)

# core01 vol_ratio 252d
def cg_f10_technology_f10_technology_price_compression_core01_vol_ratio_252d_base_v132_signal(high, low, closeadj, volume):
    result = _safe_div(_std((high-low), max(2,252//3)), _std((high-low), 252).abs()+1e-9)
    return _clean(result)

# core02 vol_ratio 5d
def cg_f10_technology_f10_technology_price_compression_core02_vol_ratio_5d_base_v133_signal(high, low, closeadj, volume):
    result = _safe_div(_std((_std(closeadj,21)), max(2,5//3)), _std((_std(closeadj,21)), 5).abs()+1e-9)
    return _clean(result)

# core03 vol_ratio 21d
def cg_f10_technology_f10_technology_price_compression_core03_vol_ratio_21d_base_v134_signal(high, low, closeadj, volume):
    result = _safe_div(_std((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), max(2,21//3)), _std((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 21).abs()+1e-9)
    return _clean(result)

# core04 vol_ratio 63d
def cg_f10_technology_f10_technology_price_compression_core04_vol_ratio_63d_base_v135_signal(high, low, closeadj, volume):
    result = _safe_div(_std(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), max(2,63//3)), _std(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 63).abs()+1e-9)
    return _clean(result)

# core05 vol_ratio 126d
def cg_f10_technology_f10_technology_price_compression_core05_vol_ratio_126d_base_v136_signal(high, low, closeadj, volume):
    result = _safe_div(_std((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), max(2,126//3)), _std((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 126).abs()+1e-9)
    return _clean(result)

# core06 vol_ratio 252d
def cg_f10_technology_f10_technology_price_compression_core06_vol_ratio_252d_base_v137_signal(high, low, closeadj, volume):
    result = _safe_div(_std((_std(_pct_change(closeadj,1),21)), max(2,252//3)), _std((_std(_pct_change(closeadj,1),21)), 252).abs()+1e-9)
    return _clean(result)

# core07 vol_ratio 5d
def cg_f10_technology_f10_technology_price_compression_core07_vol_ratio_5d_base_v138_signal(high, low, closeadj, volume):
    result = _safe_div(_std((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), max(2,5//3)), _std((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 5).abs()+1e-9)
    return _clean(result)

# core08 vol_ratio 21d
def cg_f10_technology_f10_technology_price_compression_core08_vol_ratio_21d_base_v139_signal(high, low, closeadj, volume):
    result = _safe_div(_std(((_rank(high-low,63)<0.25).astype(float)), max(2,21//3)), _std(((_rank(high-low,63)<0.25).astype(float)), 21).abs()+1e-9)
    return _clean(result)

# core09 vol_ratio 63d
def cg_f10_technology_f10_technology_price_compression_core09_vol_ratio_63d_base_v140_signal(high, low, closeadj, volume):
    result = _safe_div(_std((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), max(2,63//3)), _std((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 63).abs()+1e-9)
    return _clean(result)

# core00 recent_vs_long 252d
def cg_f10_technology_f10_technology_price_compression_core00_recent_vs_long_252d_base_v141_signal(high, low, closeadj, volume):
    result = _mean((_safe_div(high-low,closeadj.abs()+1e-9)), max(2,252//3)) - _mean((_safe_div(high-low,closeadj.abs()+1e-9)), 252)
    return _clean(result)

# core01 recent_vs_long 5d
def cg_f10_technology_f10_technology_price_compression_core01_recent_vs_long_5d_base_v142_signal(high, low, closeadj, volume):
    result = _mean((high-low), max(2,5//3)) - _mean((high-low), 5)
    return _clean(result)

# core02 recent_vs_long 21d
def cg_f10_technology_f10_technology_price_compression_core02_recent_vs_long_21d_base_v143_signal(high, low, closeadj, volume):
    result = _mean((_std(closeadj,21)), max(2,21//3)) - _mean((_std(closeadj,21)), 21)
    return _clean(result)

# core03 recent_vs_long 63d
def cg_f10_technology_f10_technology_price_compression_core03_recent_vs_long_63d_base_v144_signal(high, low, closeadj, volume):
    result = _mean((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), max(2,63//3)) - _mean((_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9)), 63)
    return _clean(result)

# core04 recent_vs_long 126d
def cg_f10_technology_f10_technology_price_compression_core04_recent_vs_long_126d_base_v145_signal(high, low, closeadj, volume):
    result = _mean(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), max(2,126//3)) - _mean(((1.0-_rank(high-low,63))*(1.0-_rank(volume,63))), 126)
    return _clean(result)

# core05 recent_vs_long 252d
def cg_f10_technology_f10_technology_price_compression_core05_recent_vs_long_252d_base_v146_signal(high, low, closeadj, volume):
    result = _mean((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), max(2,252//3)) - _mean((_diff(_safe_div(_std(closeadj,21),_mean(closeadj.abs(),21)+1e-9),5)), 252)
    return _clean(result)

# core06 recent_vs_long 5d
def cg_f10_technology_f10_technology_price_compression_core06_recent_vs_long_5d_base_v147_signal(high, low, closeadj, volume):
    result = _mean((_std(_pct_change(closeadj,1),21)), max(2,5//3)) - _mean((_std(_pct_change(closeadj,1),21)), 5)
    return _clean(result)

# core07 recent_vs_long 21d
def cg_f10_technology_f10_technology_price_compression_core07_recent_vs_long_21d_base_v148_signal(high, low, closeadj, volume):
    result = _mean((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), max(2,21//3)) - _mean((_slope(_safe_div(high-low,closeadj.abs()+1e-9),21)), 21)
    return _clean(result)

# core08 recent_vs_long 63d
def cg_f10_technology_f10_technology_price_compression_core08_recent_vs_long_63d_base_v149_signal(high, low, closeadj, volume):
    result = _mean(((_rank(high-low,63)<0.25).astype(float)), max(2,63//3)) - _mean(((_rank(high-low,63)<0.25).astype(float)), 63)
    return _clean(result)

# core09 recent_vs_long 126d
def cg_f10_technology_f10_technology_price_compression_core09_recent_vs_long_126d_base_v150_signal(high, low, closeadj, volume):
    result = _mean((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), max(2,126//3)) - _mean((-_z(high-low,63)-_z(volume,63)+_z(_pct_change(closeadj,63),63)), 126)
    return _clean(result)

