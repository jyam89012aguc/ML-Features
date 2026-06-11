import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: adjustment ratios
def cg_f090_price_adjustment_context_core00_adj_factor_v001_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(closeadj, close))
def cg_f090_price_adjustment_context_core01_unadj_ratio_v002_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(closeunadj, close))
def cg_f090_price_adjustment_context_core02_adj_diff_v003_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(closeadj - close)
def cg_f090_price_adjustment_context_core03_adj_factor_mean_252d_v004_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_safe_div(closeadj, close), 252))
def cg_f090_price_adjustment_context_core04_adj_factor_z_252d_v005_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_safe_div(closeadj, close), 252))
def cg_f090_price_adjustment_context_core05_adj_factor_pct_1q_v006_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_safe_div(closeadj, close), 63))
def cg_f090_price_adjustment_context_core06_open_adj_v007_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(open * _safe_div(closeadj, close), closeadj))
def cg_f090_price_adjustment_context_core07_high_adj_v008_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(high * _safe_div(closeadj, close), closeadj))
def cg_f090_price_adjustment_context_core08_low_adj_v009_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(low * _safe_div(closeadj, close), closeadj))
def cg_f090_price_adjustment_context_core09_cum_adj_v010_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_safe_div(closeadj, closeunadj))

# core10-19: mean 21d
def cg_f090_price_adjustment_context_core10_mean_21d_v011_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_safe_div(closeadj, close), 21))
def cg_f090_price_adjustment_context_core11_mean_21d_v012_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_safe_div(closeunadj, close), 21))
def cg_f090_price_adjustment_context_core12_mean_21d_v013_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_safe_div(closeadj, closeunadj), 21))
def cg_f090_price_adjustment_context_core13_mean_21d_v014_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_pct_change(closeadj, 1), 21))
def cg_f090_price_adjustment_context_core14_mean_21d_v015_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_pct_change(close, 1), 21))
def cg_f090_price_adjustment_context_core15_mean_21d_v016_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_pct_change(closeunadj, 1), 21))
def cg_f090_price_adjustment_context_core16_mean_21d_v017_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_z(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core17_mean_21d_v018_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_rank(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core18_mean_21d_v019_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_safe_div(high, low), 21))
def cg_f090_price_adjustment_context_core19_mean_21d_v020_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_safe_div(close, open), 21))

# core20-29: z 63d
def cg_f090_price_adjustment_context_core20_z_63d_v021_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_safe_div(closeadj, close), 63))
def cg_f090_price_adjustment_context_core21_z_63d_v022_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_safe_div(closeunadj, close), 63))
def cg_f090_price_adjustment_context_core22_z_63d_v023_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_safe_div(closeadj, closeunadj), 63))
def cg_f090_price_adjustment_context_core23_z_63d_v024_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_pct_change(closeadj, 1), 63))
def cg_f090_price_adjustment_context_core24_z_63d_v025_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_pct_change(close, 1), 63))
def cg_f090_price_adjustment_context_core25_z_63d_v026_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_pct_change(closeunadj, 1), 63))
def cg_f090_price_adjustment_context_core26_z_63d_v027_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_z(closeadj, 252), 63))
def cg_f090_price_adjustment_context_core27_z_63d_v028_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_rank(closeadj, 252), 63))
def cg_f090_price_adjustment_context_core28_z_63d_v029_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_safe_div(high, low), 63))
def cg_f090_price_adjustment_context_core29_z_63d_v030_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_safe_div(close, open), 63))

# core30-39: rank 126d
def cg_f090_price_adjustment_context_core30_rank_126d_v031_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_safe_div(closeadj, close), 126))
def cg_f090_price_adjustment_context_core31_rank_126d_v032_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_safe_div(closeunadj, close), 126))
def cg_f090_price_adjustment_context_core32_rank_126d_v033_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_safe_div(closeadj, closeunadj), 126))
def cg_f090_price_adjustment_context_core33_rank_126d_v034_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_pct_change(closeadj, 1), 126))
def cg_f090_price_adjustment_context_core34_rank_126d_v035_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_pct_change(close, 1), 126))
def cg_f090_price_adjustment_context_core35_rank_126d_v036_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_pct_change(closeunadj, 1), 126))
def cg_f090_price_adjustment_context_core36_rank_126d_v037_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_z(closeadj, 252), 126))
def cg_f090_price_adjustment_context_core37_rank_126d_v038_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_rank(closeadj, 252), 126))
def cg_f090_price_adjustment_context_core38_rank_126d_v039_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_safe_div(high, low), 126))
def cg_f090_price_adjustment_context_core39_rank_126d_v040_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_safe_div(close, open), 126))

# core40-49: pct 5d
def cg_f090_price_adjustment_context_core40_pct_5d_v041_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_safe_div(closeadj, close), 5))
def cg_f090_price_adjustment_context_core41_pct_5d_v042_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_safe_div(closeunadj, close), 5))
def cg_f090_price_adjustment_context_core42_pct_5d_v043_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_safe_div(closeadj, closeunadj), 5))
def cg_f090_price_adjustment_context_core43_pct_5d_v044_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_pct_change(closeadj, 1), 5))
def cg_f090_price_adjustment_context_core44_pct_5d_v045_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_pct_change(close, 1), 5))
def cg_f090_price_adjustment_context_core45_pct_5d_v046_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_z(closeadj, 252), 5))
def cg_f090_price_adjustment_context_core46_pct_5d_v047_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_rank(closeadj, 252), 5))
def cg_f090_price_adjustment_context_core47_pct_5d_v048_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_safe_div(high, low), 5))
def cg_f090_price_adjustment_context_core48_pct_5d_v049_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(_safe_div(close, open), 5))
def cg_f090_price_adjustment_context_core49_pct_5d_v050_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_pct_change(closeadj, 5))

# core50-59: std 21d
def cg_f090_price_adjustment_context_core50_std_21d_v051_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_safe_div(closeadj, close), 21))
def cg_f090_price_adjustment_context_core51_std_21d_v052_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_safe_div(closeunadj, close), 21))
def cg_f090_price_adjustment_context_core52_std_21d_v053_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_safe_div(closeadj, closeunadj), 21))
def cg_f090_price_adjustment_context_core53_std_21d_v054_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_pct_change(closeadj, 1), 21))
def cg_f090_price_adjustment_context_core54_std_21d_v055_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_pct_change(close, 1), 21))
def cg_f090_price_adjustment_context_core55_std_21d_v056_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_z(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core56_std_21d_v057_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_rank(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core57_std_21d_v058_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_safe_div(high, low), 21))
def cg_f090_price_adjustment_context_core58_std_21d_v059_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(_safe_div(close, open), 21))
def cg_f090_price_adjustment_context_core59_std_21d_v060_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_std(closeadj, 21))

# core60-69: slope 21d
def cg_f090_price_adjustment_context_core60_slope_21d_v061_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeadj, close), 21))
def cg_f090_price_adjustment_context_core61_slope_21d_v062_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeunadj, close), 21))
def cg_f090_price_adjustment_context_core62_slope_21d_v063_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeadj, closeunadj), 21))
def cg_f090_price_adjustment_context_core63_slope_21d_v064_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_pct_change(closeadj, 1), 21))
def cg_f090_price_adjustment_context_core64_slope_21d_v065_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_pct_change(close, 1), 21))
def cg_f090_price_adjustment_context_core65_slope_21d_v066_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_z(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core66_slope_21d_v067_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_rank(closeadj, 252), 21))
def cg_f090_price_adjustment_context_core67_slope_21d_v068_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(high, low), 21))
def cg_f090_price_adjustment_context_core68_slope_21d_v069_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(close, open), 21))
def cg_f090_price_adjustment_context_core69_slope_21d_v070_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(closeadj, 21))

# core70-74: ewm 21d
def cg_f090_price_adjustment_context_core70_ewm_21d_v071_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_safe_div(closeadj, close), 21))
def cg_f090_price_adjustment_context_core71_ewm_21d_v072_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_safe_div(closeunadj, close), 21))
def cg_f090_price_adjustment_context_core72_ewm_21d_v073_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_safe_div(closeadj, closeunadj), 21))
def cg_f090_price_adjustment_context_core73_ewm_21d_v074_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_pct_change(closeadj, 1), 21))
def cg_f090_price_adjustment_context_core74_ewm_21d_v075_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_ewm(_pct_change(close, 1), 21))
