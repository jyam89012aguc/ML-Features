import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: turnover (volume/sharesbas)
def cg_f089_volume_liquidity_context_core00_turnover_v001_signal(volume, close, closeadj, sharesbas):
    return _clean(_safe_div(volume, sharesbas))
def cg_f089_volume_liquidity_context_core01_turnover_mean_21d_v002_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_safe_div(volume, sharesbas), 21))
def cg_f089_volume_liquidity_context_core02_turnover_z_63d_v003_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume, sharesbas), 63))
def cg_f089_volume_liquidity_context_core03_dollar_vol_v004_signal(volume, close, closeadj, sharesbas):
    return _clean(volume * close)
def cg_f089_volume_liquidity_context_core04_dollar_vol_mean_21d_v005_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(volume * close, 21))
def cg_f089_volume_liquidity_context_core05_dollar_vol_z_63d_v006_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(volume * close, 63))
def cg_f089_volume_liquidity_context_core06_vol_vs_mean_21d_v007_signal(volume, close, closeadj, sharesbas):
    return _clean(_safe_div(volume, _mean(volume, 21)))
def cg_f089_volume_liquidity_context_core07_vol_vs_mean_252d_v008_signal(volume, close, closeadj, sharesbas):
    return _clean(_safe_div(volume, _mean(volume, 252)))
def cg_f089_volume_liquidity_context_core08_turnover_rank_252d_v009_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume, sharesbas), 252))
def cg_f089_volume_liquidity_context_core09_dollar_vol_rank_252d_v010_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(volume * close, 252))

# core10-19: mean 21d
def cg_f089_volume_liquidity_context_core10_mean_21d_v011_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(volume, 21))
def cg_f089_volume_liquidity_context_core11_mean_21d_v012_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_safe_div(volume, sharesbas), 21))
def cg_f089_volume_liquidity_context_core12_mean_21d_v013_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(volume * close, 21))
def cg_f089_volume_liquidity_context_core13_mean_21d_v014_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_safe_div(volume, _mean(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core14_mean_21d_v015_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_pct_change(volume, 1), 21))
def cg_f089_volume_liquidity_context_core15_mean_21d_v016_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_z(volume, 252), 21))
def cg_f089_volume_liquidity_context_core16_mean_21d_v017_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_rank(volume, 252), 21))
def cg_f089_volume_liquidity_context_core17_mean_21d_v018_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_safe_div(volume, _max(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core18_mean_21d_v019_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_safe_div(volume, _min(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core19_mean_21d_v020_signal(volume, close, closeadj, sharesbas):
    return _clean(_mean(_safe_div(volume * close, _mean(volume * close, 252)), 21))

# core20-29: z 63d
def cg_f089_volume_liquidity_context_core20_z_63d_v021_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(volume, 63))
def cg_f089_volume_liquidity_context_core21_z_63d_v022_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume, sharesbas), 63))
def cg_f089_volume_liquidity_context_core22_z_63d_v023_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(volume * close, 63))
def cg_f089_volume_liquidity_context_core23_z_63d_v024_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume, _mean(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core24_z_63d_v025_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_pct_change(volume, 1), 63))
def cg_f089_volume_liquidity_context_core25_z_63d_v026_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_z(volume, 252), 63))
def cg_f089_volume_liquidity_context_core26_z_63d_v027_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_rank(volume, 252), 63))
def cg_f089_volume_liquidity_context_core27_z_63d_v028_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume, _max(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core28_z_63d_v029_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume, _min(volume, 252)), 63))
def cg_f089_volume_liquidity_context_core29_z_63d_v030_signal(volume, close, closeadj, sharesbas):
    return _clean(_z(_safe_div(volume * close, _mean(volume * close, 252)), 63))

# core30-39: rank 126d
def cg_f089_volume_liquidity_context_core30_rank_126d_v031_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(volume, 126))
def cg_f089_volume_liquidity_context_core31_rank_126d_v032_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume, sharesbas), 126))
def cg_f089_volume_liquidity_context_core32_rank_126d_v033_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(volume * close, 126))
def cg_f089_volume_liquidity_context_core33_rank_126d_v034_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume, _mean(volume, 252)), 126))
def cg_f089_volume_liquidity_context_core34_rank_126d_v035_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_pct_change(volume, 1), 126))
def cg_f089_volume_liquidity_context_core35_rank_126d_v036_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_z(volume, 252), 126))
def cg_f089_volume_liquidity_context_core36_rank_126d_v037_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_rank(volume, 252), 126))
def cg_f089_volume_liquidity_context_core37_rank_126d_v038_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume, _max(volume, 252)), 126))
def cg_f089_volume_liquidity_context_core38_rank_126d_v039_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume, _min(volume, 252)), 126))
def cg_f089_volume_liquidity_context_core39_rank_126d_v040_signal(volume, close, closeadj, sharesbas):
    return _clean(_rank(_safe_div(volume * close, _mean(volume * close, 252)), 126))

# core40-49: pct 5d
def cg_f089_volume_liquidity_context_core40_pct_5d_v041_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(volume, 5))
def cg_f089_volume_liquidity_context_core41_pct_5d_v042_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_safe_div(volume, sharesbas), 5))
def cg_f089_volume_liquidity_context_core42_pct_5d_v043_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(volume * close, 5))
def cg_f089_volume_liquidity_context_core43_pct_5d_v044_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_safe_div(volume, _mean(volume, 252)), 5))
def cg_f089_volume_liquidity_context_core44_pct_5d_v045_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_pct_change(volume, 1), 5))
def cg_f089_volume_liquidity_context_core45_pct_5d_v046_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_z(volume, 252), 5))
def cg_f089_volume_liquidity_context_core46_pct_5d_v047_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_rank(volume, 252), 5))
def cg_f089_volume_liquidity_context_core47_pct_5d_v048_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_safe_div(volume, _max(volume, 252)), 5))
def cg_f089_volume_liquidity_context_core48_pct_5d_v049_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_safe_div(volume, _min(volume, 252)), 5))
def cg_f089_volume_liquidity_context_core49_pct_5d_v050_signal(volume, close, closeadj, sharesbas):
    return _clean(_pct_change(_safe_div(volume * close, _mean(volume * close, 252)), 5))

# core50-59: std 21d
def cg_f089_volume_liquidity_context_core50_std_21d_v051_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(volume, 21))
def cg_f089_volume_liquidity_context_core51_std_21d_v052_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_safe_div(volume, sharesbas), 21))
def cg_f089_volume_liquidity_context_core52_std_21d_v053_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(volume * close, 21))
def cg_f089_volume_liquidity_context_core53_std_21d_v054_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_safe_div(volume, _mean(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core54_std_21d_v055_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_pct_change(volume, 1), 21))
def cg_f089_volume_liquidity_context_core55_std_21d_v056_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_z(volume, 252), 21))
def cg_f089_volume_liquidity_context_core56_std_21d_v057_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_rank(volume, 252), 21))
def cg_f089_volume_liquidity_context_core57_std_21d_v058_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_safe_div(volume, _max(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core58_std_21d_v059_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_safe_div(volume, _min(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core59_std_21d_v060_signal(volume, close, closeadj, sharesbas):
    return _clean(_std(_safe_div(volume * close, _mean(volume * close, 252)), 21))

# core60-69: slope 21d
def cg_f089_volume_liquidity_context_core60_slope_21d_v061_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(volume, 21))
def cg_f089_volume_liquidity_context_core61_slope_21d_v062_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_safe_div(volume, sharesbas), 21))
def cg_f089_volume_liquidity_context_core62_slope_21d_v063_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(volume * close, 21))
def cg_f089_volume_liquidity_context_core63_slope_21d_v064_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_safe_div(volume, _mean(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core64_slope_21d_v065_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_pct_change(volume, 1), 21))
def cg_f089_volume_liquidity_context_core65_slope_21d_v066_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_z(volume, 252), 21))
def cg_f089_volume_liquidity_context_core66_slope_21d_v067_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_rank(volume, 252), 21))
def cg_f089_volume_liquidity_context_core67_slope_21d_v068_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_safe_div(volume, _max(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core68_slope_21d_v069_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_safe_div(volume, _min(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core69_slope_21d_v070_signal(volume, close, closeadj, sharesbas):
    return _clean(_slope(_safe_div(volume * close, _mean(volume * close, 252)), 21))

# core70-74: ewm 21d
def cg_f089_volume_liquidity_context_core70_ewm_21d_v071_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(volume, 21))
def cg_f089_volume_liquidity_context_core71_ewm_21d_v072_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_safe_div(volume, sharesbas), 21))
def cg_f089_volume_liquidity_context_core72_ewm_21d_v073_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(volume * close, 21))
def cg_f089_volume_liquidity_context_core73_ewm_21d_v074_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_safe_div(volume, _mean(volume, 252)), 21))
def cg_f089_volume_liquidity_context_core74_ewm_21d_v075_signal(volume, close, closeadj, sharesbas):
    return _clean(_ewm(_pct_change(volume, 1), 21))
