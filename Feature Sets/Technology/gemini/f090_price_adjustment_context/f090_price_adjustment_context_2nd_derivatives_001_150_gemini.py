import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f090_price_adjustment_context_core00_2nd_v001_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(close, 4))
def cg_f090_price_adjustment_context_core01_2nd_v002_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(closeadj, 4))
def cg_f090_price_adjustment_context_core02_2nd_v003_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(closeunadj, 4))
def cg_f090_price_adjustment_context_core03_2nd_v004_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(open, 4))
def cg_f090_price_adjustment_context_core04_2nd_v005_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(high, 4))
def cg_f090_price_adjustment_context_core05_2nd_v006_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(low, 4))
def cg_f090_price_adjustment_context_core06_2nd_v007_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeadj, close), 4))
def cg_f090_price_adjustment_context_core07_2nd_v008_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeunadj, close), 4))
def cg_f090_price_adjustment_context_core08_2nd_v009_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(high, low), 4))
def cg_f090_price_adjustment_context_core09_2nd_v010_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(close, open), 4))
def cg_f090_price_adjustment_context_core10_2nd_v011_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(close, 8))
def cg_f090_price_adjustment_context_core11_2nd_v012_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(closeadj, 8))
def cg_f090_price_adjustment_context_core12_2nd_v013_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(closeunadj, 8))
def cg_f090_price_adjustment_context_core13_2nd_v014_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(open, 8))
def cg_f090_price_adjustment_context_core14_2nd_v015_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(high, 8))
def cg_f090_price_adjustment_context_core15_2nd_v016_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(low, 8))
def cg_f090_price_adjustment_context_core16_2nd_v017_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeadj, close), 8))
def cg_f090_price_adjustment_context_core17_2nd_v018_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(closeunadj, close), 8))
def cg_f090_price_adjustment_context_core18_2nd_v019_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(high, low), 8))
def cg_f090_price_adjustment_context_core19_2nd_v020_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_safe_div(close, open), 8))
def cg_f090_price_adjustment_context_core20_2nd_v021_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(close, 4))
def cg_f090_price_adjustment_context_core21_2nd_v022_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(closeadj, 4))
def cg_f090_price_adjustment_context_core22_2nd_v023_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(closeunadj, 4))
def cg_f090_price_adjustment_context_core23_2nd_v024_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(open, 4))
def cg_f090_price_adjustment_context_core24_2nd_v025_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(high, 4))
def cg_f090_price_adjustment_context_core25_2nd_v026_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(low, 4))
def cg_f090_price_adjustment_context_core26_2nd_v027_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(closeadj, close), 4))
def cg_f090_price_adjustment_context_core27_2nd_v028_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(closeunadj, close), 4))
def cg_f090_price_adjustment_context_core28_2nd_v029_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(high, low), 4))
def cg_f090_price_adjustment_context_core29_2nd_v030_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_safe_div(close, open), 4))
def cg_f090_price_adjustment_context_core30_2nd_v031_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(close, 4), 8))
def cg_f090_price_adjustment_context_core31_2nd_v032_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(closeadj, 4), 8))
def cg_f090_price_adjustment_context_core32_2nd_v033_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(closeunadj, 4), 8))
def cg_f090_price_adjustment_context_core33_2nd_v034_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(open, 4), 8))
def cg_f090_price_adjustment_context_core34_2nd_v035_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(high, 4), 8))
def cg_f090_price_adjustment_context_core35_2nd_v036_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(low, 4), 8))
def cg_f090_price_adjustment_context_core36_2nd_v037_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(closeadj, close), 4), 8))
def cg_f090_price_adjustment_context_core37_2nd_v038_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(closeunadj, close), 4), 8))
def cg_f090_price_adjustment_context_core38_2nd_v039_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(high, low), 4), 8))
def cg_f090_price_adjustment_context_core39_2nd_v040_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(close, open), 4), 8))
def cg_f090_price_adjustment_context_core40_2nd_v041_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(close, 8), 12))
def cg_f090_price_adjustment_context_core41_2nd_v042_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(closeadj, 8), 12))
def cg_f090_price_adjustment_context_core42_2nd_v043_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(closeunadj, 8), 12))
def cg_f090_price_adjustment_context_core43_2nd_v044_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(open, 8), 12))
def cg_f090_price_adjustment_context_core44_2nd_v045_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(high, 8), 12))
def cg_f090_price_adjustment_context_core45_2nd_v046_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(low, 8), 12))
def cg_f090_price_adjustment_context_core46_2nd_v047_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(closeadj, close), 8), 12))
def cg_f090_price_adjustment_context_core47_2nd_v048_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(closeunadj, close), 8), 12))
def cg_f090_price_adjustment_context_core48_2nd_v049_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(high, low), 8), 12))
def cg_f090_price_adjustment_context_core49_2nd_v050_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_safe_div(close, open), 8), 12))
def cg_f090_price_adjustment_context_core50_2nd_v051_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(close, 4), 8))
def cg_f090_price_adjustment_context_core51_2nd_v052_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(closeadj, 4), 8))
def cg_f090_price_adjustment_context_core52_2nd_v053_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(closeunadj, 4), 8))
def cg_f090_price_adjustment_context_core53_2nd_v054_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(open, 4), 8))
def cg_f090_price_adjustment_context_core54_2nd_v055_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(high, 4), 8))
def cg_f090_price_adjustment_context_core55_2nd_v056_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(low, 4), 8))
def cg_f090_price_adjustment_context_core56_2nd_v057_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_safe_div(closeadj, close), 4), 8))
def cg_f090_price_adjustment_context_core57_2nd_v058_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_safe_div(closeunadj, close), 4), 8))
def cg_f090_price_adjustment_context_core58_2nd_v059_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_safe_div(high, low), 4), 8))
def cg_f090_price_adjustment_context_core59_2nd_v060_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_safe_div(close, open), 4), 8))
def cg_f090_price_adjustment_context_core60_2nd_v061_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(close, 4), 12))
def cg_f090_price_adjustment_context_core61_2nd_v062_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(closeadj, 4), 12))
def cg_f090_price_adjustment_context_core62_2nd_v063_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(closeunadj, 4), 12))
def cg_f090_price_adjustment_context_core63_2nd_v064_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(open, 4), 12))
def cg_f090_price_adjustment_context_core64_2nd_v065_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(high, 4), 12))
def cg_f090_price_adjustment_context_core65_2nd_v066_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(low, 4), 12))
def cg_f090_price_adjustment_context_core66_2nd_v067_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_safe_div(closeadj, close), 4), 12))
def cg_f090_price_adjustment_context_core67_2nd_v068_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_safe_div(closeunadj, close), 4), 12))
def cg_f090_price_adjustment_context_core68_2nd_v069_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_safe_div(high, low), 4), 12))
def cg_f090_price_adjustment_context_core69_2nd_v070_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_safe_div(close, open), 4), 12))
def cg_f090_price_adjustment_context_core70_2nd_v071_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(close, 4), 12))
def cg_f090_price_adjustment_context_core71_2nd_v072_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(closeadj, 4), 12))
def cg_f090_price_adjustment_context_core72_2nd_v073_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(closeunadj, 4), 12))
def cg_f090_price_adjustment_context_core73_2nd_v074_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(open, 4), 12))
def cg_f090_price_adjustment_context_core74_2nd_v075_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(high, 4), 12))
def cg_f090_price_adjustment_context_core75_2nd_v076_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(low, 4), 12))
def cg_f090_price_adjustment_context_core76_2nd_v077_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_safe_div(closeadj, close), 4), 12))
def cg_f090_price_adjustment_context_core77_2nd_v078_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_safe_div(closeunadj, close), 4), 12))
def cg_f090_price_adjustment_context_core78_2nd_v079_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_safe_div(high, low), 4), 12))
def cg_f090_price_adjustment_context_core79_2nd_v080_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_safe_div(close, open), 4), 12))
def cg_f090_price_adjustment_context_core80_2nd_v081_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(close, 4), 4))
def cg_f090_price_adjustment_context_core81_2nd_v082_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(closeadj, 4), 4))
def cg_f090_price_adjustment_context_core82_2nd_v083_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(closeunadj, 4), 4))
def cg_f090_price_adjustment_context_core83_2nd_v084_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(open, 4), 4))
def cg_f090_price_adjustment_context_core84_2nd_v085_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(high, 4), 4))
def cg_f090_price_adjustment_context_core85_2nd_v086_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(low, 4), 4))
def cg_f090_price_adjustment_context_core86_2nd_v087_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_safe_div(closeadj, close), 4), 4))
def cg_f090_price_adjustment_context_core87_2nd_v088_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_safe_div(closeunadj, close), 4), 4))
def cg_f090_price_adjustment_context_core88_2nd_v089_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_safe_div(high, low), 4), 4))
def cg_f090_price_adjustment_context_core89_2nd_v090_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_safe_div(close, open), 4), 4))
def cg_f090_price_adjustment_context_core90_2nd_v091_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(close, 4), 4))
def cg_f090_price_adjustment_context_core91_2nd_v092_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(closeadj, 4), 4))
def cg_f090_price_adjustment_context_core92_2nd_v093_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(closeunadj, 4), 4))
def cg_f090_price_adjustment_context_core93_2nd_v094_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(open, 4), 4))
def cg_f090_price_adjustment_context_core94_2nd_v095_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(high, 4), 4))
def cg_f090_price_adjustment_context_core95_2nd_v096_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(low, 4), 4))
def cg_f090_price_adjustment_context_core96_2nd_v097_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_safe_div(closeadj, close), 4), 4))
def cg_f090_price_adjustment_context_core97_2nd_v098_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_safe_div(closeunadj, close), 4), 4))
def cg_f090_price_adjustment_context_core98_2nd_v099_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_safe_div(high, low), 4), 4))
def cg_f090_price_adjustment_context_core99_2nd_v100_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_safe_div(close, open), 4), 4))
def cg_f090_price_adjustment_context_core100_2nd_v101_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(close, 4), 4))
def cg_f090_price_adjustment_context_core101_2nd_v102_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(closeadj, 4), 4))
def cg_f090_price_adjustment_context_core102_2nd_v103_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(closeunadj, 4), 4))
def cg_f090_price_adjustment_context_core103_2nd_v104_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(open, 4), 4))
def cg_f090_price_adjustment_context_core104_2nd_v105_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(high, 4), 4))
def cg_f090_price_adjustment_context_core105_2nd_v106_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(low, 4), 4))
def cg_f090_price_adjustment_context_core106_2nd_v107_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(closeadj, close), 4), 4))
def cg_f090_price_adjustment_context_core107_2nd_v108_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(closeunadj, close), 4), 4))
def cg_f090_price_adjustment_context_core108_2nd_v109_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(high, low), 4), 4))
def cg_f090_price_adjustment_context_core109_2nd_v110_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(close, open), 4), 4))
def cg_f090_price_adjustment_context_core110_2nd_v111_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(close, 8), 8))
def cg_f090_price_adjustment_context_core111_2nd_v112_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(closeadj, 8), 8))
def cg_f090_price_adjustment_context_core112_2nd_v113_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(closeunadj, 8), 8))
def cg_f090_price_adjustment_context_core113_2nd_v114_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(open, 8), 8))
def cg_f090_price_adjustment_context_core114_2nd_v115_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(high, 8), 8))
def cg_f090_price_adjustment_context_core115_2nd_v116_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(low, 8), 8))
def cg_f090_price_adjustment_context_core116_2nd_v117_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(closeadj, close), 8), 8))
def cg_f090_price_adjustment_context_core117_2nd_v118_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(closeunadj, close), 8), 8))
def cg_f090_price_adjustment_context_core118_2nd_v119_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(high, low), 8), 8))
def cg_f090_price_adjustment_context_core119_2nd_v120_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_mean(_safe_div(close, open), 8), 8))
def cg_f090_price_adjustment_context_core120_2nd_v121_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(close, 4), 4))
def cg_f090_price_adjustment_context_core121_2nd_v122_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(closeadj, 4), 4))
def cg_f090_price_adjustment_context_core122_2nd_v123_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(closeunadj, 4), 4))
def cg_f090_price_adjustment_context_core123_2nd_v124_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(open, 4), 4))
def cg_f090_price_adjustment_context_core124_2nd_v125_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(high, 4), 4))
def cg_f090_price_adjustment_context_core125_2nd_v126_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(low, 4), 4))
def cg_f090_price_adjustment_context_core126_2nd_v127_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(_safe_div(closeadj, close), 4), 4))
def cg_f090_price_adjustment_context_core127_2nd_v128_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(_safe_div(closeunadj, close), 4), 4))
def cg_f090_price_adjustment_context_core128_2nd_v129_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(_safe_div(high, low), 4), 4))
def cg_f090_price_adjustment_context_core129_2nd_v130_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_mean(_safe_div(close, open), 4), 4))
def cg_f090_price_adjustment_context_core130_2nd_v131_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(close, 4), 4), 8))
def cg_f090_price_adjustment_context_core131_2nd_v132_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(closeadj, 4), 4), 8))
def cg_f090_price_adjustment_context_core132_2nd_v133_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(closeunadj, 4), 4), 8))
def cg_f090_price_adjustment_context_core133_2nd_v134_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(open, 4), 4), 8))
def cg_f090_price_adjustment_context_core134_2nd_v135_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(high, 4), 4), 8))
def cg_f090_price_adjustment_context_core135_2nd_v136_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(low, 4), 4), 8))
def cg_f090_price_adjustment_context_core136_2nd_v137_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(_safe_div(closeadj, close), 4), 4), 8))
def cg_f090_price_adjustment_context_core137_2nd_v138_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(_safe_div(closeunadj, close), 4), 4), 8))
def cg_f090_price_adjustment_context_core138_2nd_v139_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(_safe_div(high, low), 4), 4), 8))
def cg_f090_price_adjustment_context_core139_2nd_v140_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_mean(_safe_div(close, open), 4), 4), 8))
def cg_f090_price_adjustment_context_core140_2nd_v141_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(close, 4), 4), 12))
def cg_f090_price_adjustment_context_core141_2nd_v142_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(closeadj, 4), 4), 12))
def cg_f090_price_adjustment_context_core142_2nd_v143_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(closeunadj, 4), 4), 12))
def cg_f090_price_adjustment_context_core143_2nd_v144_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(open, 4), 4), 12))
def cg_f090_price_adjustment_context_core144_2nd_v145_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(high, 4), 4), 12))
def cg_f090_price_adjustment_context_core145_2nd_v146_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(low, 4), 4), 12))
def cg_f090_price_adjustment_context_core146_2nd_v147_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(_safe_div(closeadj, close), 4), 4), 12))
def cg_f090_price_adjustment_context_core147_2nd_v148_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(_safe_div(closeunadj, close), 4), 4), 12))
def cg_f090_price_adjustment_context_core148_2nd_v149_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(_safe_div(high, low), 4), 4), 12))
def cg_f090_price_adjustment_context_core149_2nd_v150_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_mean(_safe_div(close, open), 4), 4), 12))