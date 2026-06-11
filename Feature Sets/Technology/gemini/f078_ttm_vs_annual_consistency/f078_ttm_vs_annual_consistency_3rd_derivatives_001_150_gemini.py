import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f078_ttm_vs_annual_consistency_core00_3rd_v001_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core01_3rd_v002_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(ncfo, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core02_3rd_v003_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core03_3rd_v004_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(rnd, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core04_3rd_v005_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core05_3rd_v006_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core06_3rd_v007_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core07_3rd_v008_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_safe_div(netinc, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core08_3rd_v009_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_safe_div(rnd, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core09_3rd_v010_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_event_flag(dimension), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core10_3rd_v011_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core11_3rd_v012_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(ncfo, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core12_3rd_v013_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core13_3rd_v014_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(rnd, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core14_3rd_v015_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_to_num(dimension == 'ARQ'), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core15_3rd_v016_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_to_num(dimension == 'MRT'), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core16_3rd_v017_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core17_3rd_v018_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_safe_div(netinc, revenue), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core18_3rd_v019_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_safe_div(rnd, revenue), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core19_3rd_v020_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_event_flag(dimension), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core20_3rd_v021_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(revenue, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core21_3rd_v022_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(ncfo, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core22_3rd_v023_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(netinc, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core23_3rd_v024_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(rnd, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core24_3rd_v025_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(_to_num(dimension == 'ARQ'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core25_3rd_v026_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(_to_num(dimension == 'MRT'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core26_3rd_v027_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core27_3rd_v028_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(_safe_div(netinc, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core28_3rd_v029_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(_safe_div(rnd, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core29_3rd_v030_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_slope(_event_flag(dimension), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core30_3rd_v031_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core31_3rd_v032_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(ncfo, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core32_3rd_v033_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core33_3rd_v034_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(rnd, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core34_3rd_v035_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core35_3rd_v036_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core36_3rd_v037_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core37_3rd_v038_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core38_3rd_v039_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core39_3rd_v040_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_diff(_event_flag(dimension), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core40_3rd_v041_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core41_3rd_v042_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(ncfo, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core42_3rd_v043_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core43_3rd_v044_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(rnd, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core44_3rd_v045_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_to_num(dimension == 'ARQ'), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core45_3rd_v046_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_to_num(dimension == 'MRT'), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core46_3rd_v047_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core47_3rd_v048_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_safe_div(netinc, revenue), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core48_3rd_v049_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_safe_div(rnd, revenue), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core49_3rd_v050_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_event_flag(dimension), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core50_3rd_v051_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(revenue, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core51_3rd_v052_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(ncfo, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core52_3rd_v053_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(netinc, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core53_3rd_v054_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(rnd, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core54_3rd_v055_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(_to_num(dimension == 'ARQ'), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core55_3rd_v056_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(_to_num(dimension == 'MRT'), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core56_3rd_v057_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core57_3rd_v058_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(_safe_div(netinc, revenue), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core58_3rd_v059_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(_safe_div(rnd, revenue), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core59_3rd_v060_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_slope(_event_flag(dimension), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core60_3rd_v061_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core61_3rd_v062_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(ncfo, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core62_3rd_v063_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core63_3rd_v064_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(rnd, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core64_3rd_v065_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core65_3rd_v066_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core66_3rd_v067_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core67_3rd_v068_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core68_3rd_v069_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core69_3rd_v070_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_diff(_event_flag(dimension), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core70_3rd_v071_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(revenue, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core71_3rd_v072_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(ncfo, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core72_3rd_v073_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(netinc, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core73_3rd_v074_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(rnd, 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core74_3rd_v075_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(_to_num(dimension == 'ARQ'), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core75_3rd_v076_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(_to_num(dimension == 'MRT'), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core76_3rd_v077_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core77_3rd_v078_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(netinc, revenue), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core78_3rd_v079_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, revenue), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core79_3rd_v080_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_diff(_event_flag(dimension), 4), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core80_3rd_v081_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(revenue, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core81_3rd_v082_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(ncfo, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core82_3rd_v083_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(netinc, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core83_3rd_v084_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(rnd, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core84_3rd_v085_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(_to_num(dimension == 'ARQ'), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core85_3rd_v086_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(_to_num(dimension == 'MRT'), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core86_3rd_v087_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core87_3rd_v088_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(netinc, revenue), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core88_3rd_v089_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, revenue), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core89_3rd_v090_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_slope(_event_flag(dimension), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core90_3rd_v091_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core91_3rd_v092_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(ncfo, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core92_3rd_v093_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core93_3rd_v094_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(rnd, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core94_3rd_v095_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core95_3rd_v096_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core96_3rd_v097_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core97_3rd_v098_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core98_3rd_v099_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core99_3rd_v100_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_diff(_event_flag(dimension), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core100_3rd_v101_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(revenue, 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core101_3rd_v102_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(ncfo, 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core102_3rd_v103_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(netinc, 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core103_3rd_v104_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(rnd, 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core104_3rd_v105_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(_to_num(dimension == 'ARQ'), 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core105_3rd_v106_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(_to_num(dimension == 'MRT'), 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core106_3rd_v107_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core107_3rd_v108_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(netinc, revenue), 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core108_3rd_v109_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, revenue), 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core109_3rd_v110_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_diff(_event_flag(dimension), 4), 8), 4))
def cg_f078_ttm_vs_annual_consistency_core110_3rd_v111_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(revenue, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core111_3rd_v112_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(ncfo, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core112_3rd_v113_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(netinc, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core113_3rd_v114_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(rnd, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core114_3rd_v115_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(_to_num(dimension == 'ARQ'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core115_3rd_v116_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(_to_num(dimension == 'MRT'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core116_3rd_v117_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core117_3rd_v118_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core118_3rd_v119_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core119_3rd_v120_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_slope(_event_flag(dimension), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core120_3rd_v121_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(revenue, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core121_3rd_v122_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(ncfo, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core122_3rd_v123_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core123_3rd_v124_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(rnd, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core124_3rd_v125_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core125_3rd_v126_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core126_3rd_v127_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core127_3rd_v128_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core128_3rd_v129_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core129_3rd_v130_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_diff(_diff(_event_flag(dimension), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core130_3rd_v131_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(revenue, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core131_3rd_v132_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(ncfo, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core132_3rd_v133_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core133_3rd_v134_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(rnd, 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core134_3rd_v135_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core135_3rd_v136_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core136_3rd_v137_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core137_3rd_v138_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core138_3rd_v139_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core139_3rd_v140_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_diff(_diff(_event_flag(dimension), 4), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core140_3rd_v141_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(revenue, 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core141_3rd_v142_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(ncfo, 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core142_3rd_v143_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core143_3rd_v144_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(rnd, 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core144_3rd_v145_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(_to_num(dimension == 'ARQ'), 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core145_3rd_v146_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(_to_num(dimension == 'MRT'), 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core146_3rd_v147_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core147_3rd_v148_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core148_3rd_v149_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core149_3rd_v150_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_diff(_diff(_event_flag(dimension), 4), 4), 4), 8))