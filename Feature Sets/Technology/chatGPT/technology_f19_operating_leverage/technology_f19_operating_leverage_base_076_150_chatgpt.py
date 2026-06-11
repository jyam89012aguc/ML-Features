import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core05 slope 63d
def cg_f19_technology_f19_operating_leverage_core05_slope_63d_base_v076_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _slope(series,63)
    return _clean(result)

# core06 slope 126d
def cg_f19_technology_f19_operating_leverage_core06_slope_126d_base_v077_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _slope(series,126)
    return _clean(result)

# core07 slope 252d
def cg_f19_technology_f19_operating_leverage_core07_slope_252d_base_v078_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _slope(series,252)
    return _clean(result)

# core08 slope 5d
def cg_f19_technology_f19_operating_leverage_core08_slope_5d_base_v079_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _slope(series,5)
    return _clean(result)

# core09 slope 21d
def cg_f19_technology_f19_operating_leverage_core09_slope_21d_base_v080_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _slope(series,21)
    return _clean(result)

# core00 abs_mean 126d
def cg_f19_technology_f19_operating_leverage_core00_abs_mean_126d_base_v081_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _mean(series.abs(),126)
    return _clean(result)

# core01 abs_mean 252d
def cg_f19_technology_f19_operating_leverage_core01_abs_mean_252d_base_v082_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _mean(series.abs(),252)
    return _clean(result)

# core02 abs_mean 5d
def cg_f19_technology_f19_operating_leverage_core02_abs_mean_5d_base_v083_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _mean(series.abs(),5)
    return _clean(result)

# core03 abs_mean 21d
def cg_f19_technology_f19_operating_leverage_core03_abs_mean_21d_base_v084_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _mean(series.abs(),21)
    return _clean(result)

# core04 abs_mean 63d
def cg_f19_technology_f19_operating_leverage_core04_abs_mean_63d_base_v085_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _mean(series.abs(),63)
    return _clean(result)

# core05 abs_mean 126d
def cg_f19_technology_f19_operating_leverage_core05_abs_mean_126d_base_v086_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _mean(series.abs(),126)
    return _clean(result)

# core06 abs_mean 252d
def cg_f19_technology_f19_operating_leverage_core06_abs_mean_252d_base_v087_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _mean(series.abs(),252)
    return _clean(result)

# core07 abs_mean 5d
def cg_f19_technology_f19_operating_leverage_core07_abs_mean_5d_base_v088_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _mean(series.abs(),5)
    return _clean(result)

# core08 abs_mean 21d
def cg_f19_technology_f19_operating_leverage_core08_abs_mean_21d_base_v089_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _mean(series.abs(),21)
    return _clean(result)

# core09 abs_mean 63d
def cg_f19_technology_f19_operating_leverage_core09_abs_mean_63d_base_v090_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _mean(series.abs(),63)
    return _clean(result)

# core00 pos_mag 252d
def cg_f19_technology_f19_operating_leverage_core00_pos_mag_252d_base_v091_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _mean(series.where(series>0,0),252)
    return _clean(result)

# core01 pos_mag 5d
def cg_f19_technology_f19_operating_leverage_core01_pos_mag_5d_base_v092_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _mean(series.where(series>0,0),5)
    return _clean(result)

# core02 pos_mag 21d
def cg_f19_technology_f19_operating_leverage_core02_pos_mag_21d_base_v093_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _mean(series.where(series>0,0),21)
    return _clean(result)

# core03 pos_mag 63d
def cg_f19_technology_f19_operating_leverage_core03_pos_mag_63d_base_v094_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _mean(series.where(series>0,0),63)
    return _clean(result)

# core04 pos_mag 126d
def cg_f19_technology_f19_operating_leverage_core04_pos_mag_126d_base_v095_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _mean(series.where(series>0,0),126)
    return _clean(result)

# core05 pos_mag 252d
def cg_f19_technology_f19_operating_leverage_core05_pos_mag_252d_base_v096_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _mean(series.where(series>0,0),252)
    return _clean(result)

# core06 pos_mag 5d
def cg_f19_technology_f19_operating_leverage_core06_pos_mag_5d_base_v097_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _mean(series.where(series>0,0),5)
    return _clean(result)

# core07 pos_mag 21d
def cg_f19_technology_f19_operating_leverage_core07_pos_mag_21d_base_v098_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _mean(series.where(series>0,0),21)
    return _clean(result)

# core08 pos_mag 63d
def cg_f19_technology_f19_operating_leverage_core08_pos_mag_63d_base_v099_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _mean(series.where(series>0,0),63)
    return _clean(result)

# core09 pos_mag 126d
def cg_f19_technology_f19_operating_leverage_core09_pos_mag_126d_base_v100_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _mean(series.where(series>0,0),126)
    return _clean(result)

# core00 neg_mag 5d
def cg_f19_technology_f19_operating_leverage_core00_neg_mag_5d_base_v101_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _mean((series.where(series<0,0).abs() ** 2),5)
    return _clean(result)

# core01 neg_mag 21d
def cg_f19_technology_f19_operating_leverage_core01_neg_mag_21d_base_v102_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _mean((series.where(series<0,0).abs() ** 2),21)
    return _clean(result)

# core02 neg_mag 63d
def cg_f19_technology_f19_operating_leverage_core02_neg_mag_63d_base_v103_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _mean((series.where(series<0,0).abs() ** 2),63)
    return _clean(result)

# core03 neg_mag 126d
def cg_f19_technology_f19_operating_leverage_core03_neg_mag_126d_base_v104_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _mean((series.where(series<0,0).abs() ** 2),126)
    return _clean(result)

# core04 neg_mag 252d
def cg_f19_technology_f19_operating_leverage_core04_neg_mag_252d_base_v105_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _mean((series.where(series<0,0).abs() ** 2),252)
    return _clean(result)

# core05 neg_mag 5d
def cg_f19_technology_f19_operating_leverage_core05_neg_mag_5d_base_v106_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _mean((series.where(series<0,0).abs() ** 2),5)
    return _clean(result)

# core06 neg_mag 21d
def cg_f19_technology_f19_operating_leverage_core06_neg_mag_21d_base_v107_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _mean((series.where(series<0,0).abs() ** 2),21)
    return _clean(result)

# core07 neg_mag 63d
def cg_f19_technology_f19_operating_leverage_core07_neg_mag_63d_base_v108_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _mean((series.where(series<0,0).abs() ** 2),63)
    return _clean(result)

# core08 neg_mag 126d
def cg_f19_technology_f19_operating_leverage_core08_neg_mag_126d_base_v109_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _mean((series.where(series<0,0).abs() ** 2),126)
    return _clean(result)

# core09 neg_mag 252d
def cg_f19_technology_f19_operating_leverage_core09_neg_mag_252d_base_v110_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _mean((series.where(series<0,0).abs() ** 2),252)
    return _clean(result)

# core00 vol_ratio 21d
def cg_f19_technology_f19_operating_leverage_core00_vol_ratio_21d_base_v111_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _safe_div(_std(series,21), _mean(series.abs(),21) + 1e-9)
    return _clean(result)

# core01 vol_ratio 63d
def cg_f19_technology_f19_operating_leverage_core01_vol_ratio_63d_base_v112_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _safe_div(_std(series,63), _mean(series.abs(),63) + 1e-9)
    return _clean(result)

# core02 vol_ratio 126d
def cg_f19_technology_f19_operating_leverage_core02_vol_ratio_126d_base_v113_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _safe_div(_std(series,126), _mean(series.abs(),126) + 1e-9)
    return _clean(result)

# core03 vol_ratio 252d
def cg_f19_technology_f19_operating_leverage_core03_vol_ratio_252d_base_v114_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _safe_div(_std(series,252), _mean(series.abs(),252) + 1e-9)
    return _clean(result)

# core04 vol_ratio 5d
def cg_f19_technology_f19_operating_leverage_core04_vol_ratio_5d_base_v115_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _safe_div(_std(series,5), _mean(series.abs(),5) + 1e-9)
    return _clean(result)

# core05 vol_ratio 21d
def cg_f19_technology_f19_operating_leverage_core05_vol_ratio_21d_base_v116_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _safe_div(_std(series,21), _mean(series.abs(),21) + 1e-9)
    return _clean(result)

# core06 vol_ratio 63d
def cg_f19_technology_f19_operating_leverage_core06_vol_ratio_63d_base_v117_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _safe_div(_std(series,63), _mean(series.abs(),63) + 1e-9)
    return _clean(result)

# core07 vol_ratio 126d
def cg_f19_technology_f19_operating_leverage_core07_vol_ratio_126d_base_v118_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _safe_div(_std(series,126), _mean(series.abs(),126) + 1e-9)
    return _clean(result)

# core08 vol_ratio 252d
def cg_f19_technology_f19_operating_leverage_core08_vol_ratio_252d_base_v119_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _safe_div(_std(series,252), _mean(series.abs(),252) + 1e-9)
    return _clean(result)

# core09 vol_ratio 5d
def cg_f19_technology_f19_operating_leverage_core09_vol_ratio_5d_base_v120_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _safe_div(_std(series,5), _mean(series.abs(),5) + 1e-9)
    return _clean(result)

# core00 recent_vs_long 63d
def cg_f19_technology_f19_operating_leverage_core00_recent_vs_long_63d_base_v121_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _safe_div(_mean(series,63), _mean(series,126) + 1e-9) - 1.0
    return _clean(result)

# core01 recent_vs_long 126d
def cg_f19_technology_f19_operating_leverage_core01_recent_vs_long_126d_base_v122_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _safe_div(_mean(series,126), _mean(series,252) + 1e-9) - 1.0
    return _clean(result)

# core02 recent_vs_long 252d
def cg_f19_technology_f19_operating_leverage_core02_recent_vs_long_252d_base_v123_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _safe_div(_mean(series,252), _mean(series,504) + 1e-9) - 1.0
    return _clean(result)

# core03 recent_vs_long 5d
def cg_f19_technology_f19_operating_leverage_core03_recent_vs_long_5d_base_v124_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _safe_div(_mean(series,5), _mean(series,10) + 1e-9) - 1.0
    return _clean(result)

# core04 recent_vs_long 21d
def cg_f19_technology_f19_operating_leverage_core04_recent_vs_long_21d_base_v125_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _safe_div(_mean(series,21), _mean(series,42) + 1e-9) - 1.0
    return _clean(result)

# core05 recent_vs_long 63d
def cg_f19_technology_f19_operating_leverage_core05_recent_vs_long_63d_base_v126_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _safe_div(_mean(series,63), _mean(series,126) + 1e-9) - 1.0
    return _clean(result)

# core06 recent_vs_long 126d
def cg_f19_technology_f19_operating_leverage_core06_recent_vs_long_126d_base_v127_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _safe_div(_mean(series,126), _mean(series,252) + 1e-9) - 1.0
    return _clean(result)

# core07 recent_vs_long 252d
def cg_f19_technology_f19_operating_leverage_core07_recent_vs_long_252d_base_v128_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _safe_div(_mean(series,252), _mean(series,504) + 1e-9) - 1.0
    return _clean(result)

# core08 recent_vs_long 5d
def cg_f19_technology_f19_operating_leverage_core08_recent_vs_long_5d_base_v129_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _safe_div(_mean(series,5), _mean(series,10) + 1e-9) - 1.0
    return _clean(result)

# core09 recent_vs_long 21d
def cg_f19_technology_f19_operating_leverage_core09_recent_vs_long_21d_base_v130_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _safe_div(_mean(series,21), _mean(series,42) + 1e-9) - 1.0
    return _clean(result)

# core00 accel 126d
def cg_f19_technology_f19_operating_leverage_core00_accel_126d_base_v131_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _diff(_diff(series,42),42)
    return _clean(result)

# core01 accel 252d
def cg_f19_technology_f19_operating_leverage_core01_accel_252d_base_v132_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _diff(_diff(series,84),84)
    return _clean(result)

# core02 accel 5d
def cg_f19_technology_f19_operating_leverage_core02_accel_5d_base_v133_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _diff(_diff(series,1),1)
    return _clean(result)

# core03 accel 21d
def cg_f19_technology_f19_operating_leverage_core03_accel_21d_base_v134_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _diff(_diff(series,7),7)
    return _clean(result)

# core04 accel 63d
def cg_f19_technology_f19_operating_leverage_core04_accel_63d_base_v135_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _diff(_diff(series,21),21)
    return _clean(result)

# core05 accel 126d
def cg_f19_technology_f19_operating_leverage_core05_accel_126d_base_v136_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _diff(_diff(series,42),42)
    return _clean(result)

# core06 accel 252d
def cg_f19_technology_f19_operating_leverage_core06_accel_252d_base_v137_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _diff(_diff(series,84),84)
    return _clean(result)

# core07 accel 5d
def cg_f19_technology_f19_operating_leverage_core07_accel_5d_base_v138_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _diff(_diff(series,1),1)
    return _clean(result)

# core08 accel 21d
def cg_f19_technology_f19_operating_leverage_core08_accel_21d_base_v139_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _diff(_diff(series,7),7)
    return _clean(result)

# core09 accel 63d
def cg_f19_technology_f19_operating_leverage_core09_accel_63d_base_v140_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _diff(_diff(series,21),21)
    return _clean(result)

# core00 range_norm 252d
def cg_f19_technology_f19_operating_leverage_core00_range_norm_252d_base_v141_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(opinc, revenue.abs()+1e-9)
    result = _safe_div(series - _mean(series,252), (_max(series,252) - _min(series,252)).abs() + 1e-9)
    return _clean(result)

# core01 range_norm 5d
def cg_f19_technology_f19_operating_leverage_core01_range_norm_5d_base_v142_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = revenue
    result = _safe_div(series - _mean(series,5), (_max(series,5) - _min(series,5)).abs() + 1e-9)
    return _clean(result)

# core02 range_norm 21d
def cg_f19_technology_f19_operating_leverage_core02_range_norm_21d_base_v143_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(gp, revenue.abs() + 1e-9)
    result = _safe_div(series - _mean(series,21), (_max(series,21) - _min(series,21)).abs() + 1e-9)
    return _clean(result)

# core03 range_norm 63d
def cg_f19_technology_f19_operating_leverage_core03_range_norm_63d_base_v144_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(opinc,63), _diff(revenue,63).abs()+1e-9)
    result = _safe_div(series - _mean(series,63), (_max(series,63) - _min(series,63)).abs() + 1e-9)
    return _clean(result)

# core04 range_norm 126d
def cg_f19_technology_f19_operating_leverage_core04_range_norm_126d_base_v145_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(gp,63)
    result = _safe_div(series - _mean(series,126), (_max(series,126) - _min(series,126)).abs() + 1e-9)
    return _clean(result)

# core05 range_norm 252d
def cg_f19_technology_f19_operating_leverage_core05_range_norm_252d_base_v146_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _pct_change(revenue,63)
    result = _safe_div(series - _mean(series,252), (_max(series,252) - _min(series,252)).abs() + 1e-9)
    return _clean(result)

# core06 range_norm 5d
def cg_f19_technology_f19_operating_leverage_core06_range_norm_5d_base_v147_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,63), _std(gp,252).abs() + 1e-9)
    result = _safe_div(series - _mean(series,5), (_max(series,5) - _min(series,5)).abs() + 1e-9)
    return _clean(result)

# core07 range_norm 21d
def cg_f19_technology_f19_operating_leverage_core07_range_norm_21d_base_v148_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _corr(gp, _pct_change(closeadj,21),252)
    result = _safe_div(series - _mean(series,21), (_max(series,21) - _min(series,21)).abs() + 1e-9)
    return _clean(result)

# core08 range_norm 63d
def cg_f19_technology_f19_operating_leverage_core08_range_norm_63d_base_v149_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_pct_change(closeadj,21), _std(gp,126).abs() + 1e-9)
    result = _safe_div(series - _mean(series,63), (_max(series,63) - _min(series,63)).abs() + 1e-9)
    return _clean(result)

# core09 range_norm 126d
def cg_f19_technology_f19_operating_leverage_core09_range_norm_126d_base_v150_signal(gp, revenue, opinc, closeadj, grossmargin):
    series = _safe_div(_diff(gp,21), _diff(revenue,21).abs() + 1e-9)
    result = _safe_div(series - _mean(series,126), (_max(series,126) - _min(series,126)).abs() + 1e-9)
    return _clean(result)

