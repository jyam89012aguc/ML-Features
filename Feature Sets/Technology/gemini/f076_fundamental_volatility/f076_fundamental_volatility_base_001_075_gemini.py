import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core00-09: mean 4q
def cg_f076_fundamental_volatility_core00_mean_4q_v001_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(revenue, 4))
def cg_f076_fundamental_volatility_core01_mean_4q_v002_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(ncfo, 4))
def cg_f076_fundamental_volatility_core02_mean_4q_v003_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(rnd, 4))
def cg_f076_fundamental_volatility_core03_mean_4q_v004_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(netinc, 4))
def cg_f076_fundamental_volatility_core04_mean_4q_v005_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(opinc, 4))
def cg_f076_fundamental_volatility_core05_mean_4q_v006_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(ncfo, revenue.abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core06_mean_4q_v007_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(rnd, revenue.abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core07_mean_4q_v008_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(netinc, revenue.abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core08_mean_4q_v009_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(opinc, revenue.abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core09_mean_4q_v010_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(ncfo, opinc.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f076_fundamental_volatility_core10_mean_8q_v011_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(revenue, 8))
def cg_f076_fundamental_volatility_core11_mean_8q_v012_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(ncfo, 8))
def cg_f076_fundamental_volatility_core12_mean_8q_v013_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(rnd, 8))
def cg_f076_fundamental_volatility_core13_mean_8q_v014_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(netinc, 8))
def cg_f076_fundamental_volatility_core14_mean_8q_v015_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(opinc, 8))
def cg_f076_fundamental_volatility_core15_mean_8q_v016_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(ncfo, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core16_mean_8q_v017_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(rnd, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core17_mean_8q_v018_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(netinc, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core18_mean_8q_v019_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(opinc, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core19_mean_8q_v020_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_safe_div(ncfo, opinc.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f076_fundamental_volatility_core20_z_8q_v021_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(revenue, 8))
def cg_f076_fundamental_volatility_core21_z_8q_v022_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(ncfo, 8))
def cg_f076_fundamental_volatility_core22_z_8q_v023_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(rnd, 8))
def cg_f076_fundamental_volatility_core23_z_8q_v024_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(netinc, 8))
def cg_f076_fundamental_volatility_core24_z_8q_v025_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(opinc, 8))
def cg_f076_fundamental_volatility_core25_z_8q_v026_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(ncfo, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core26_z_8q_v027_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(rnd, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core27_z_8q_v028_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(netinc, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core28_z_8q_v029_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(opinc, revenue.abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core29_z_8q_v030_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(ncfo, opinc.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f076_fundamental_volatility_core30_z_20q_v031_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(revenue, 20))
def cg_f076_fundamental_volatility_core31_z_20q_v032_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(ncfo, 20))
def cg_f076_fundamental_volatility_core32_z_20q_v033_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(rnd, 20))
def cg_f076_fundamental_volatility_core33_z_20q_v034_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(netinc, 20))
def cg_f076_fundamental_volatility_core34_z_20q_v035_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(opinc, 20))
def cg_f076_fundamental_volatility_core35_z_20q_v036_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(ncfo, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core36_z_20q_v037_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(rnd, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core37_z_20q_v038_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(netinc, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core38_z_20q_v039_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(opinc, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core39_z_20q_v040_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_safe_div(ncfo, opinc.abs() + 1.0), 20))

# core40-49: rank 12q
def cg_f076_fundamental_volatility_core40_rank_12q_v041_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(revenue, 12))
def cg_f076_fundamental_volatility_core41_rank_12q_v042_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(ncfo, 12))
def cg_f076_fundamental_volatility_core42_rank_12q_v043_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(rnd, 12))
def cg_f076_fundamental_volatility_core43_rank_12q_v044_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(netinc, 12))
def cg_f076_fundamental_volatility_core44_rank_12q_v045_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(opinc, 12))
def cg_f076_fundamental_volatility_core45_rank_12q_v046_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(ncfo, revenue.abs() + 1.0), 12))
def cg_f076_fundamental_volatility_core46_rank_12q_v047_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(rnd, revenue.abs() + 1.0), 12))
def cg_f076_fundamental_volatility_core47_rank_12q_v048_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(netinc, revenue.abs() + 1.0), 12))
def cg_f076_fundamental_volatility_core48_rank_12q_v049_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(opinc, revenue.abs() + 1.0), 12))
def cg_f076_fundamental_volatility_core49_rank_12q_v050_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(ncfo, opinc.abs() + 1.0), 12))

# core50-59: rank 20q
def cg_f076_fundamental_volatility_core50_rank_20q_v051_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(revenue, 20))
def cg_f076_fundamental_volatility_core51_rank_20q_v052_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(ncfo, 20))
def cg_f076_fundamental_volatility_core52_rank_20q_v053_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(rnd, 20))
def cg_f076_fundamental_volatility_core53_rank_20q_v054_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(netinc, 20))
def cg_f076_fundamental_volatility_core54_rank_20q_v055_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(opinc, 20))
def cg_f076_fundamental_volatility_core55_rank_20q_v056_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(ncfo, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core56_rank_20q_v057_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(rnd, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core57_rank_20q_v058_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(netinc, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core58_rank_20q_v059_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(opinc, revenue.abs() + 1.0), 20))
def cg_f076_fundamental_volatility_core59_rank_20q_v060_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_safe_div(ncfo, opinc.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f076_fundamental_volatility_core60_pct_1q_v061_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(revenue, 1))
def cg_f076_fundamental_volatility_core61_pct_1q_v062_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(ncfo, 1))
def cg_f076_fundamental_volatility_core62_pct_1q_v063_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(rnd, 1))
def cg_f076_fundamental_volatility_core63_pct_1q_v064_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(netinc, 1))
def cg_f076_fundamental_volatility_core64_pct_1q_v065_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(opinc, 1))
def cg_f076_fundamental_volatility_core65_pct_1q_v066_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(_safe_div(ncfo, revenue.abs() + 1.0), 1))
def cg_f076_fundamental_volatility_core66_pct_1q_v067_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(_safe_div(rnd, revenue.abs() + 1.0), 1))
def cg_f076_fundamental_volatility_core67_pct_1q_v068_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(_safe_div(netinc, revenue.abs() + 1.0), 1))
def cg_f076_fundamental_volatility_core68_pct_1q_v069_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(_safe_div(opinc, revenue.abs() + 1.0), 1))
def cg_f076_fundamental_volatility_core69_pct_1q_v070_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(_safe_div(ncfo, opinc.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f076_fundamental_volatility_core70_pct_4q_v071_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(revenue, 4))
def cg_f076_fundamental_volatility_core71_pct_4q_v072_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(ncfo, 4))
def cg_f076_fundamental_volatility_core72_pct_4q_v073_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(rnd, 4))
def cg_f076_fundamental_volatility_core73_pct_4q_v074_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(netinc, 4))
def cg_f076_fundamental_volatility_core74_pct_4q_v075_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_pct_change(opinc, 4))
