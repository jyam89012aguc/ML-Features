import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f078_ttm_vs_annual_consistency_core00_2nd_v001_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(revenue, 4))
def cg_f078_ttm_vs_annual_consistency_core01_2nd_v002_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(ncfo, 4))
def cg_f078_ttm_vs_annual_consistency_core02_2nd_v003_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(netinc, 4))
def cg_f078_ttm_vs_annual_consistency_core03_2nd_v004_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(rnd, 4))
def cg_f078_ttm_vs_annual_consistency_core04_2nd_v005_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_to_num(dimension == 'ARQ'), 4))
def cg_f078_ttm_vs_annual_consistency_core05_2nd_v006_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_to_num(dimension == 'MRT'), 4))
def cg_f078_ttm_vs_annual_consistency_core06_2nd_v007_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4))
def cg_f078_ttm_vs_annual_consistency_core07_2nd_v008_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_safe_div(netinc, revenue), 4))
def cg_f078_ttm_vs_annual_consistency_core08_2nd_v009_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_safe_div(rnd, revenue), 4))
def cg_f078_ttm_vs_annual_consistency_core09_2nd_v010_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_event_flag(dimension), 4))
def cg_f078_ttm_vs_annual_consistency_core10_2nd_v011_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(revenue, 8))
def cg_f078_ttm_vs_annual_consistency_core11_2nd_v012_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(ncfo, 8))
def cg_f078_ttm_vs_annual_consistency_core12_2nd_v013_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(netinc, 8))
def cg_f078_ttm_vs_annual_consistency_core13_2nd_v014_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(rnd, 8))
def cg_f078_ttm_vs_annual_consistency_core14_2nd_v015_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_to_num(dimension == 'ARQ'), 8))
def cg_f078_ttm_vs_annual_consistency_core15_2nd_v016_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_to_num(dimension == 'MRT'), 8))
def cg_f078_ttm_vs_annual_consistency_core16_2nd_v017_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 8))
def cg_f078_ttm_vs_annual_consistency_core17_2nd_v018_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_safe_div(netinc, revenue), 8))
def cg_f078_ttm_vs_annual_consistency_core18_2nd_v019_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_safe_div(rnd, revenue), 8))
def cg_f078_ttm_vs_annual_consistency_core19_2nd_v020_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_event_flag(dimension), 8))
def cg_f078_ttm_vs_annual_consistency_core20_2nd_v021_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(revenue, 4))
def cg_f078_ttm_vs_annual_consistency_core21_2nd_v022_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(ncfo, 4))
def cg_f078_ttm_vs_annual_consistency_core22_2nd_v023_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(netinc, 4))
def cg_f078_ttm_vs_annual_consistency_core23_2nd_v024_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(rnd, 4))
def cg_f078_ttm_vs_annual_consistency_core24_2nd_v025_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_to_num(dimension == 'ARQ'), 4))
def cg_f078_ttm_vs_annual_consistency_core25_2nd_v026_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_to_num(dimension == 'MRT'), 4))
def cg_f078_ttm_vs_annual_consistency_core26_2nd_v027_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4))
def cg_f078_ttm_vs_annual_consistency_core27_2nd_v028_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_safe_div(netinc, revenue), 4))
def cg_f078_ttm_vs_annual_consistency_core28_2nd_v029_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_safe_div(rnd, revenue), 4))
def cg_f078_ttm_vs_annual_consistency_core29_2nd_v030_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_event_flag(dimension), 4))
def cg_f078_ttm_vs_annual_consistency_core30_2nd_v031_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core31_2nd_v032_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core32_2nd_v033_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(netinc, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core33_2nd_v034_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core34_2nd_v035_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_to_num(dimension == 'ARQ'), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core35_2nd_v036_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_to_num(dimension == 'MRT'), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core36_2nd_v037_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core37_2nd_v038_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_safe_div(netinc, revenue), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core38_2nd_v039_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_safe_div(rnd, revenue), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core39_2nd_v040_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_event_flag(dimension), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core40_2nd_v041_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f078_ttm_vs_annual_consistency_core41_2nd_v042_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f078_ttm_vs_annual_consistency_core42_2nd_v043_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(netinc, 8), 12))
def cg_f078_ttm_vs_annual_consistency_core43_2nd_v044_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f078_ttm_vs_annual_consistency_core44_2nd_v045_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_to_num(dimension == 'ARQ'), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core45_2nd_v046_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_to_num(dimension == 'MRT'), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core46_2nd_v047_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core47_2nd_v048_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_safe_div(netinc, revenue), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core48_2nd_v049_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_safe_div(rnd, revenue), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core49_2nd_v050_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_slope(_event_flag(dimension), 8), 12))
def cg_f078_ttm_vs_annual_consistency_core50_2nd_v051_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core51_2nd_v052_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core52_2nd_v053_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(netinc, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core53_2nd_v054_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f078_ttm_vs_annual_consistency_core54_2nd_v055_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_to_num(dimension == 'ARQ'), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core55_2nd_v056_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_to_num(dimension == 'MRT'), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core56_2nd_v057_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core57_2nd_v058_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_safe_div(netinc, revenue), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core58_2nd_v059_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_safe_div(rnd, revenue), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core59_2nd_v060_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_event_flag(dimension), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core60_2nd_v061_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core61_2nd_v062_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core62_2nd_v063_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(netinc, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core63_2nd_v064_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core64_2nd_v065_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_to_num(dimension == 'ARQ'), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core65_2nd_v066_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_to_num(dimension == 'MRT'), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core66_2nd_v067_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core67_2nd_v068_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_safe_div(netinc, revenue), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core68_2nd_v069_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_safe_div(rnd, revenue), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core69_2nd_v070_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_event_flag(dimension), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core70_2nd_v071_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core71_2nd_v072_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core72_2nd_v073_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(netinc, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core73_2nd_v074_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f078_ttm_vs_annual_consistency_core74_2nd_v075_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_to_num(dimension == 'ARQ'), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core75_2nd_v076_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_to_num(dimension == 'MRT'), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core76_2nd_v077_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core77_2nd_v078_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_safe_div(netinc, revenue), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core78_2nd_v079_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_safe_div(rnd, revenue), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core79_2nd_v080_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_diff(_event_flag(dimension), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core80_2nd_v081_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core81_2nd_v082_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core82_2nd_v083_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(netinc, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core83_2nd_v084_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core84_2nd_v085_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_to_num(dimension == 'ARQ'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core85_2nd_v086_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_to_num(dimension == 'MRT'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core86_2nd_v087_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core87_2nd_v088_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_safe_div(netinc, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core88_2nd_v089_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_safe_div(rnd, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core89_2nd_v090_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_slope(_event_flag(dimension), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core90_2nd_v091_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core91_2nd_v092_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core92_2nd_v093_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(netinc, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core93_2nd_v094_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core94_2nd_v095_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_to_num(dimension == 'ARQ'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core95_2nd_v096_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_to_num(dimension == 'MRT'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core96_2nd_v097_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core97_2nd_v098_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_safe_div(netinc, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core98_2nd_v099_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_safe_div(rnd, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core99_2nd_v100_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_mean(_diff(_event_flag(dimension), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core100_2nd_v101_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core101_2nd_v102_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core102_2nd_v103_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(netinc, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core103_2nd_v104_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core104_2nd_v105_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_to_num(dimension == 'ARQ'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core105_2nd_v106_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_to_num(dimension == 'MRT'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core106_2nd_v107_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core107_2nd_v108_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_safe_div(netinc, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core108_2nd_v109_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_safe_div(rnd, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core109_2nd_v110_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_event_flag(dimension), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core110_2nd_v111_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f078_ttm_vs_annual_consistency_core111_2nd_v112_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f078_ttm_vs_annual_consistency_core112_2nd_v113_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(netinc, 8), 8))
def cg_f078_ttm_vs_annual_consistency_core113_2nd_v114_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f078_ttm_vs_annual_consistency_core114_2nd_v115_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_to_num(dimension == 'ARQ'), 8), 8))
def cg_f078_ttm_vs_annual_consistency_core115_2nd_v116_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_to_num(dimension == 'MRT'), 8), 8))
def cg_f078_ttm_vs_annual_consistency_core116_2nd_v117_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_safe_div(revenue, ncfo.abs() + 1.0), 8), 8))
def cg_f078_ttm_vs_annual_consistency_core117_2nd_v118_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_safe_div(netinc, revenue), 8), 8))
def cg_f078_ttm_vs_annual_consistency_core118_2nd_v119_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_safe_div(rnd, revenue), 8), 8))
def cg_f078_ttm_vs_annual_consistency_core119_2nd_v120_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_slope(_mean(_event_flag(dimension), 8), 8))
def cg_f078_ttm_vs_annual_consistency_core120_2nd_v121_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core121_2nd_v122_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core122_2nd_v123_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(netinc, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core123_2nd_v124_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f078_ttm_vs_annual_consistency_core124_2nd_v125_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(_to_num(dimension == 'ARQ'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core125_2nd_v126_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(_to_num(dimension == 'MRT'), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core126_2nd_v127_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core127_2nd_v128_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(_safe_div(netinc, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core128_2nd_v129_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(_safe_div(rnd, revenue), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core129_2nd_v130_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_diff(_mean(_event_flag(dimension), 4), 4))
def cg_f078_ttm_vs_annual_consistency_core130_2nd_v131_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core131_2nd_v132_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core132_2nd_v133_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(netinc, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core133_2nd_v134_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core134_2nd_v135_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(_to_num(dimension == 'ARQ'), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core135_2nd_v136_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(_to_num(dimension == 'MRT'), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core136_2nd_v137_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core137_2nd_v138_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(_safe_div(netinc, revenue), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core138_2nd_v139_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(_safe_div(rnd, revenue), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core139_2nd_v140_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_z(_diff(_mean(_event_flag(dimension), 4), 4), 8))
def cg_f078_ttm_vs_annual_consistency_core140_2nd_v141_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core141_2nd_v142_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core142_2nd_v143_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(netinc, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core143_2nd_v144_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core144_2nd_v145_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(_to_num(dimension == 'ARQ'), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core145_2nd_v146_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(_to_num(dimension == 'MRT'), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core146_2nd_v147_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core147_2nd_v148_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(netinc, revenue), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core148_2nd_v149_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, revenue), 4), 4), 12))
def cg_f078_ttm_vs_annual_consistency_core149_2nd_v150_signal(dimension, revenue, ncfo, netinc, rnd):
    return _clean(_rank(_slope(_mean(_event_flag(dimension), 4), 4), 12))