import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: multi-year highs (252d)
def cg_f088_ohlcv_multi_year_highs_core00_high_252d_v001_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeadj, _max(closeadj, 252)))
def cg_f088_ohlcv_multi_year_highs_core01_high_504d_v002_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeadj, _max(closeadj, 504)))
def cg_f088_ohlcv_multi_year_highs_core02_high_756d_v003_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeadj, _max(closeadj, 756)))
def cg_f088_ohlcv_multi_year_highs_core03_high_1260d_v004_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeadj, _max(closeadj, 1260)))
def cg_f088_ohlcv_multi_year_highs_core04_unadj_high_252d_v005_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeunadj, _max(closeunadj, 252)))
def cg_f088_ohlcv_multi_year_highs_core05_unadj_high_504d_v006_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeunadj, _max(closeunadj, 504)))
def cg_f088_ohlcv_multi_year_highs_core06_high_vs_low_252d_v007_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeadj - _min(closeadj, 252), _max(closeadj, 252) - _min(closeadj, 252)))
def cg_f088_ohlcv_multi_year_highs_core07_high_vs_low_504d_v008_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_safe_div(closeadj - _min(closeadj, 504), _max(closeadj, 504) - _min(closeadj, 504)))
def cg_f088_ohlcv_multi_year_highs_core08_volume_z_252d_v009_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 252))
def cg_f088_ohlcv_multi_year_highs_core09_volume_z_504d_v010_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 504))

# core10-19: mean 21d
def cg_f088_ohlcv_multi_year_highs_core10_mean_21d_v011_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(closeadj, 21))
def cg_f088_ohlcv_multi_year_highs_core11_mean_21d_v012_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_safe_div(closeadj, open), 21))
def cg_f088_ohlcv_multi_year_highs_core12_mean_21d_v013_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_safe_div(high, low), 21))
def cg_f088_ohlcv_multi_year_highs_core13_mean_21d_v014_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_safe_div(volume, _mean(volume, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core14_mean_21d_v015_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_pct_change(closeadj, 1), 21))
def cg_f088_ohlcv_multi_year_highs_core15_mean_21d_v016_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_z(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core16_mean_21d_v017_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_rank(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core17_mean_21d_v018_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_safe_div(closeadj, _max(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core18_mean_21d_v019_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_safe_div(closeadj, _min(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core19_mean_21d_v020_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_mean(_safe_div(volume, _max(volume, 252)), 21))

# core20-29: z 63d
def cg_f088_ohlcv_multi_year_highs_core20_z_63d_v021_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(closeadj, 63))
def cg_f088_ohlcv_multi_year_highs_core21_z_63d_v022_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_safe_div(closeadj, open), 63))
def cg_f088_ohlcv_multi_year_highs_core22_z_63d_v023_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_safe_div(high, low), 63))
def cg_f088_ohlcv_multi_year_highs_core23_z_63d_v024_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(volume, 63))
def cg_f088_ohlcv_multi_year_highs_core24_z_63d_v025_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_pct_change(closeadj, 1), 63))
def cg_f088_ohlcv_multi_year_highs_core25_z_63d_v026_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_z(closeadj, 252), 63))
def cg_f088_ohlcv_multi_year_highs_core26_z_63d_v027_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_rank(closeadj, 252), 63))
def cg_f088_ohlcv_multi_year_highs_core27_z_63d_v028_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_safe_div(closeadj, _max(closeadj, 252)), 63))
def cg_f088_ohlcv_multi_year_highs_core28_z_63d_v029_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_safe_div(closeadj, _min(closeadj, 252)), 63))
def cg_f088_ohlcv_multi_year_highs_core29_z_63d_v030_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_z(_safe_div(volume, _max(volume, 252)), 63))

# core30-39: rank 126d
def cg_f088_ohlcv_multi_year_highs_core30_rank_126d_v031_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(closeadj, 126))
def cg_f088_ohlcv_multi_year_highs_core31_rank_126d_v032_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_safe_div(closeadj, open), 126))
def cg_f088_ohlcv_multi_year_highs_core32_rank_126d_v033_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_safe_div(high, low), 126))
def cg_f088_ohlcv_multi_year_highs_core33_rank_126d_v034_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(volume, 126))
def cg_f088_ohlcv_multi_year_highs_core34_rank_126d_v035_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_pct_change(closeadj, 1), 126))
def cg_f088_ohlcv_multi_year_highs_core35_rank_126d_v036_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_z(closeadj, 252), 126))
def cg_f088_ohlcv_multi_year_highs_core36_rank_126d_v037_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_rank(closeadj, 252), 126))
def cg_f088_ohlcv_multi_year_highs_core37_rank_126d_v038_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_safe_div(closeadj, _max(closeadj, 252)), 126))
def cg_f088_ohlcv_multi_year_highs_core38_rank_126d_v039_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_safe_div(closeadj, _min(closeadj, 252)), 126))
def cg_f088_ohlcv_multi_year_highs_core39_rank_126d_v040_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_rank(_safe_div(volume, _max(volume, 252)), 126))

# core40-49: pct 5d
def cg_f088_ohlcv_multi_year_highs_core40_pct_5d_v041_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(closeadj, 5))
def cg_f088_ohlcv_multi_year_highs_core41_pct_5d_v042_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_safe_div(closeadj, open), 5))
def cg_f088_ohlcv_multi_year_highs_core42_pct_5d_v043_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_safe_div(high, low), 5))
def cg_f088_ohlcv_multi_year_highs_core43_pct_5d_v044_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(volume, 5))
def cg_f088_ohlcv_multi_year_highs_core44_pct_5d_v045_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_pct_change(closeadj, 1), 5))
def cg_f088_ohlcv_multi_year_highs_core45_pct_5d_v046_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_z(closeadj, 252), 5))
def cg_f088_ohlcv_multi_year_highs_core46_pct_5d_v047_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_rank(closeadj, 252), 5))
def cg_f088_ohlcv_multi_year_highs_core47_pct_5d_v048_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_safe_div(closeadj, _max(closeadj, 252)), 5))
def cg_f088_ohlcv_multi_year_highs_core48_pct_5d_v049_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_safe_div(closeadj, _min(closeadj, 252)), 5))
def cg_f088_ohlcv_multi_year_highs_core49_pct_5d_v050_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_pct_change(_safe_div(volume, _max(volume, 252)), 5))

# core50-59: std 21d
def cg_f088_ohlcv_multi_year_highs_core50_std_21d_v051_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(closeadj, 21))
def cg_f088_ohlcv_multi_year_highs_core51_std_21d_v052_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_safe_div(closeadj, open), 21))
def cg_f088_ohlcv_multi_year_highs_core52_std_21d_v053_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_safe_div(high, low), 21))
def cg_f088_ohlcv_multi_year_highs_core53_std_21d_v054_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(volume, 21))
def cg_f088_ohlcv_multi_year_highs_core54_std_21d_v055_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_pct_change(closeadj, 1), 21))
def cg_f088_ohlcv_multi_year_highs_core55_std_21d_v056_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_z(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core56_std_21d_v057_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_rank(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core57_std_21d_v058_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_safe_div(closeadj, _max(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core58_std_21d_v059_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_safe_div(closeadj, _min(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core59_std_21d_v060_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_std(_safe_div(volume, _max(volume, 252)), 21))

# core60-69: slope 21d
def cg_f088_ohlcv_multi_year_highs_core60_slope_21d_v061_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(closeadj, 21))
def cg_f088_ohlcv_multi_year_highs_core61_slope_21d_v062_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(closeadj, open), 21))
def cg_f088_ohlcv_multi_year_highs_core62_slope_21d_v063_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(high, low), 21))
def cg_f088_ohlcv_multi_year_highs_core63_slope_21d_v064_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(volume, 21))
def cg_f088_ohlcv_multi_year_highs_core64_slope_21d_v065_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_pct_change(closeadj, 1), 21))
def cg_f088_ohlcv_multi_year_highs_core65_slope_21d_v066_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_z(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core66_slope_21d_v067_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_rank(closeadj, 252), 21))
def cg_f088_ohlcv_multi_year_highs_core67_slope_21d_v068_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(closeadj, _max(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core68_slope_21d_v069_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(closeadj, _min(closeadj, 252)), 21))
def cg_f088_ohlcv_multi_year_highs_core69_slope_21d_v070_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_slope(_safe_div(volume, _max(volume, 252)), 21))

# core70-74: ewm 21d
def cg_f088_ohlcv_multi_year_highs_core70_ewm_21d_v071_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(closeadj, 21))
def cg_f088_ohlcv_multi_year_highs_core71_ewm_21d_v072_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_safe_div(closeadj, open), 21))
def cg_f088_ohlcv_multi_year_highs_core72_ewm_21d_v073_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_safe_div(high, low), 21))
def cg_f088_ohlcv_multi_year_highs_core73_ewm_21d_v074_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(volume, 21))
def cg_f088_ohlcv_multi_year_highs_core74_ewm_21d_v075_signal(date, open, high, low, close, volume, closeadj, closeunadj):
    return _clean(_ewm(_pct_change(closeadj, 1), 21))
