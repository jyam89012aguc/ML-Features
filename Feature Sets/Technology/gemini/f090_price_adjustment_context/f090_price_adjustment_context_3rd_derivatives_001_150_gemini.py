import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f090_price_adjustment_context_core00_3rd_v001_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(close, 4), 4))
def cg_f090_price_adjustment_context_core01_3rd_v002_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(closeadj, 4), 4))
def cg_f090_price_adjustment_context_core02_3rd_v003_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(closeunadj, 4), 4))
def cg_f090_price_adjustment_context_core03_3rd_v004_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(open, 4), 4))
def cg_f090_price_adjustment_context_core04_3rd_v005_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(high, 4), 4))
def cg_f090_price_adjustment_context_core05_3rd_v006_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(low, 4), 4))
def cg_f090_price_adjustment_context_core06_3rd_v007_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_safe_div(closeadj, close), 4), 4))
def cg_f090_price_adjustment_context_core07_3rd_v008_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_safe_div(closeunadj, close), 4), 4))
def cg_f090_price_adjustment_context_core08_3rd_v009_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_safe_div(high, low), 4), 4))
def cg_f090_price_adjustment_context_core09_3rd_v010_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_safe_div(close, open), 4), 4))
def cg_f090_price_adjustment_context_core10_3rd_v011_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(close, 4), 8))
def cg_f090_price_adjustment_context_core11_3rd_v012_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(closeadj, 4), 8))
def cg_f090_price_adjustment_context_core12_3rd_v013_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(closeunadj, 4), 8))
def cg_f090_price_adjustment_context_core13_3rd_v014_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(open, 4), 8))
def cg_f090_price_adjustment_context_core14_3rd_v015_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(high, 4), 8))
def cg_f090_price_adjustment_context_core15_3rd_v016_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(low, 4), 8))
def cg_f090_price_adjustment_context_core16_3rd_v017_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_safe_div(closeadj, close), 4), 8))
def cg_f090_price_adjustment_context_core17_3rd_v018_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_safe_div(closeunadj, close), 4), 8))
def cg_f090_price_adjustment_context_core18_3rd_v019_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_safe_div(high, low), 4), 8))
def cg_f090_price_adjustment_context_core19_3rd_v020_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_safe_div(close, open), 4), 8))
def cg_f090_price_adjustment_context_core20_3rd_v021_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(close, 4), 4))
def cg_f090_price_adjustment_context_core21_3rd_v022_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(closeadj, 4), 4))
def cg_f090_price_adjustment_context_core22_3rd_v023_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(closeunadj, 4), 4))
def cg_f090_price_adjustment_context_core23_3rd_v024_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(open, 4), 4))
def cg_f090_price_adjustment_context_core24_3rd_v025_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(high, 4), 4))
def cg_f090_price_adjustment_context_core25_3rd_v026_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(low, 4), 4))
def cg_f090_price_adjustment_context_core26_3rd_v027_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(_safe_div(closeadj, close), 4), 4))
def cg_f090_price_adjustment_context_core27_3rd_v028_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(_safe_div(closeunadj, close), 4), 4))
def cg_f090_price_adjustment_context_core28_3rd_v029_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(_safe_div(high, low), 4), 4))
def cg_f090_price_adjustment_context_core29_3rd_v030_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_slope(_safe_div(close, open), 4), 4))
def cg_f090_price_adjustment_context_core30_3rd_v031_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(close, 4), 4), 8))
def cg_f090_price_adjustment_context_core31_3rd_v032_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(closeadj, 4), 4), 8))
def cg_f090_price_adjustment_context_core32_3rd_v033_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(closeunadj, 4), 4), 8))
def cg_f090_price_adjustment_context_core33_3rd_v034_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(open, 4), 4), 8))
def cg_f090_price_adjustment_context_core34_3rd_v035_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(high, 4), 4), 8))
def cg_f090_price_adjustment_context_core35_3rd_v036_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(low, 4), 4), 8))
def cg_f090_price_adjustment_context_core36_3rd_v037_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(_safe_div(closeadj, close), 4), 4), 8))
def cg_f090_price_adjustment_context_core37_3rd_v038_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(_safe_div(closeunadj, close), 4), 4), 8))
def cg_f090_price_adjustment_context_core38_3rd_v039_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(_safe_div(high, low), 4), 4), 8))
def cg_f090_price_adjustment_context_core39_3rd_v040_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_diff(_safe_div(close, open), 4), 4), 8))
def cg_f090_price_adjustment_context_core40_3rd_v041_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(close, 4), 8), 12))
def cg_f090_price_adjustment_context_core41_3rd_v042_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(closeadj, 4), 8), 12))
def cg_f090_price_adjustment_context_core42_3rd_v043_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(closeunadj, 4), 8), 12))
def cg_f090_price_adjustment_context_core43_3rd_v044_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(open, 4), 8), 12))
def cg_f090_price_adjustment_context_core44_3rd_v045_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(high, 4), 8), 12))
def cg_f090_price_adjustment_context_core45_3rd_v046_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(low, 4), 8), 12))
def cg_f090_price_adjustment_context_core46_3rd_v047_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_safe_div(closeadj, close), 4), 8), 12))
def cg_f090_price_adjustment_context_core47_3rd_v048_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_safe_div(closeunadj, close), 4), 8), 12))
def cg_f090_price_adjustment_context_core48_3rd_v049_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_safe_div(high, low), 4), 8), 12))
def cg_f090_price_adjustment_context_core49_3rd_v050_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_safe_div(close, open), 4), 8), 12))
def cg_f090_price_adjustment_context_core50_3rd_v051_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(close, 4), 4), 8))
def cg_f090_price_adjustment_context_core51_3rd_v052_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(closeadj, 4), 4), 8))
def cg_f090_price_adjustment_context_core52_3rd_v053_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(closeunadj, 4), 4), 8))
def cg_f090_price_adjustment_context_core53_3rd_v054_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(open, 4), 4), 8))
def cg_f090_price_adjustment_context_core54_3rd_v055_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(high, 4), 4), 8))
def cg_f090_price_adjustment_context_core55_3rd_v056_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(low, 4), 4), 8))
def cg_f090_price_adjustment_context_core56_3rd_v057_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(_safe_div(closeadj, close), 4), 4), 8))
def cg_f090_price_adjustment_context_core57_3rd_v058_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(_safe_div(closeunadj, close), 4), 4), 8))
def cg_f090_price_adjustment_context_core58_3rd_v059_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(_safe_div(high, low), 4), 4), 8))
def cg_f090_price_adjustment_context_core59_3rd_v060_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_diff(_slope(_safe_div(close, open), 4), 4), 8))
def cg_f090_price_adjustment_context_core60_3rd_v061_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(close, 4), 4), 12))
def cg_f090_price_adjustment_context_core61_3rd_v062_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(closeadj, 4), 4), 12))
def cg_f090_price_adjustment_context_core62_3rd_v063_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(closeunadj, 4), 4), 12))
def cg_f090_price_adjustment_context_core63_3rd_v064_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(open, 4), 4), 12))
def cg_f090_price_adjustment_context_core64_3rd_v065_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(high, 4), 4), 12))
def cg_f090_price_adjustment_context_core65_3rd_v066_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(low, 4), 4), 12))
def cg_f090_price_adjustment_context_core66_3rd_v067_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(_safe_div(closeadj, close), 4), 4), 12))
def cg_f090_price_adjustment_context_core67_3rd_v068_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(_safe_div(closeunadj, close), 4), 4), 12))
def cg_f090_price_adjustment_context_core68_3rd_v069_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(_safe_div(high, low), 4), 4), 12))
def cg_f090_price_adjustment_context_core69_3rd_v070_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_diff(_safe_div(close, open), 4), 4), 12))
def cg_f090_price_adjustment_context_core70_3rd_v071_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(close, 4), 8), 12))
def cg_f090_price_adjustment_context_core71_3rd_v072_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(closeadj, 4), 8), 12))
def cg_f090_price_adjustment_context_core72_3rd_v073_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(closeunadj, 4), 8), 12))
def cg_f090_price_adjustment_context_core73_3rd_v074_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(open, 4), 8), 12))
def cg_f090_price_adjustment_context_core74_3rd_v075_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(high, 4), 8), 12))
def cg_f090_price_adjustment_context_core75_3rd_v076_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(low, 4), 8), 12))
def cg_f090_price_adjustment_context_core76_3rd_v077_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(_safe_div(closeadj, close), 4), 8), 12))
def cg_f090_price_adjustment_context_core77_3rd_v078_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(_safe_div(closeunadj, close), 4), 8), 12))
def cg_f090_price_adjustment_context_core78_3rd_v079_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(_safe_div(high, low), 4), 8), 12))
def cg_f090_price_adjustment_context_core79_3rd_v080_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_slope(_diff(_safe_div(close, open), 4), 8), 12))
def cg_f090_price_adjustment_context_core80_3rd_v081_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(close, 4), 4), 12))
def cg_f090_price_adjustment_context_core81_3rd_v082_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(closeadj, 4), 4), 12))
def cg_f090_price_adjustment_context_core82_3rd_v083_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(closeunadj, 4), 4), 12))
def cg_f090_price_adjustment_context_core83_3rd_v084_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(open, 4), 4), 12))
def cg_f090_price_adjustment_context_core84_3rd_v085_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(high, 4), 4), 12))
def cg_f090_price_adjustment_context_core85_3rd_v086_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(low, 4), 4), 12))
def cg_f090_price_adjustment_context_core86_3rd_v087_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(_safe_div(closeadj, close), 4), 4), 12))
def cg_f090_price_adjustment_context_core87_3rd_v088_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(_safe_div(closeunadj, close), 4), 4), 12))
def cg_f090_price_adjustment_context_core88_3rd_v089_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(_safe_div(high, low), 4), 4), 12))
def cg_f090_price_adjustment_context_core89_3rd_v090_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_rank(_diff(_slope(_safe_div(close, open), 4), 4), 12))
def cg_f090_price_adjustment_context_core90_3rd_v091_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(close, 4), 4), 4))
def cg_f090_price_adjustment_context_core91_3rd_v092_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(closeadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core92_3rd_v093_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(closeunadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core93_3rd_v094_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(open, 4), 4), 4))
def cg_f090_price_adjustment_context_core94_3rd_v095_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(high, 4), 4), 4))
def cg_f090_price_adjustment_context_core95_3rd_v096_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(low, 4), 4), 4))
def cg_f090_price_adjustment_context_core96_3rd_v097_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(_safe_div(closeadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core97_3rd_v098_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(_safe_div(closeunadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core98_3rd_v099_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(_safe_div(high, low), 4), 4), 4))
def cg_f090_price_adjustment_context_core99_3rd_v100_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_diff(_safe_div(close, open), 4), 4), 4))
def cg_f090_price_adjustment_context_core100_3rd_v101_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(close, 4), 8), 4))
def cg_f090_price_adjustment_context_core101_3rd_v102_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(closeadj, 4), 8), 4))
def cg_f090_price_adjustment_context_core102_3rd_v103_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(closeunadj, 4), 8), 4))
def cg_f090_price_adjustment_context_core103_3rd_v104_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(open, 4), 8), 4))
def cg_f090_price_adjustment_context_core104_3rd_v105_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(high, 4), 8), 4))
def cg_f090_price_adjustment_context_core105_3rd_v106_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(low, 4), 8), 4))
def cg_f090_price_adjustment_context_core106_3rd_v107_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(_safe_div(closeadj, close), 4), 8), 4))
def cg_f090_price_adjustment_context_core107_3rd_v108_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(_safe_div(closeunadj, close), 4), 8), 4))
def cg_f090_price_adjustment_context_core108_3rd_v109_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(_safe_div(high, low), 4), 8), 4))
def cg_f090_price_adjustment_context_core109_3rd_v110_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_slope(_diff(_safe_div(close, open), 4), 8), 4))
def cg_f090_price_adjustment_context_core110_3rd_v111_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(close, 4), 4), 4))
def cg_f090_price_adjustment_context_core111_3rd_v112_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(closeadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core112_3rd_v113_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(closeunadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core113_3rd_v114_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(open, 4), 4), 4))
def cg_f090_price_adjustment_context_core114_3rd_v115_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(high, 4), 4), 4))
def cg_f090_price_adjustment_context_core115_3rd_v116_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(low, 4), 4), 4))
def cg_f090_price_adjustment_context_core116_3rd_v117_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(_safe_div(closeadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core117_3rd_v118_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(_safe_div(closeunadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core118_3rd_v119_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(_safe_div(high, low), 4), 4), 4))
def cg_f090_price_adjustment_context_core119_3rd_v120_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_mean(_diff(_slope(_safe_div(close, open), 4), 4), 4))
def cg_f090_price_adjustment_context_core120_3rd_v121_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(close, 4), 4), 4))
def cg_f090_price_adjustment_context_core121_3rd_v122_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(closeadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core122_3rd_v123_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(closeunadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core123_3rd_v124_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(open, 4), 4), 4))
def cg_f090_price_adjustment_context_core124_3rd_v125_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(high, 4), 4), 4))
def cg_f090_price_adjustment_context_core125_3rd_v126_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(low, 4), 4), 4))
def cg_f090_price_adjustment_context_core126_3rd_v127_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(_safe_div(closeadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core127_3rd_v128_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(_safe_div(closeunadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core128_3rd_v129_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(_safe_div(high, low), 4), 4), 4))
def cg_f090_price_adjustment_context_core129_3rd_v130_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_slope(_diff(_diff(_safe_div(close, open), 4), 4), 4))
def cg_f090_price_adjustment_context_core130_3rd_v131_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(close, 4), 4), 4))
def cg_f090_price_adjustment_context_core131_3rd_v132_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(closeadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core132_3rd_v133_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(closeunadj, 4), 4), 4))
def cg_f090_price_adjustment_context_core133_3rd_v134_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(open, 4), 4), 4))
def cg_f090_price_adjustment_context_core134_3rd_v135_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(high, 4), 4), 4))
def cg_f090_price_adjustment_context_core135_3rd_v136_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(low, 4), 4), 4))
def cg_f090_price_adjustment_context_core136_3rd_v137_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(_safe_div(closeadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core137_3rd_v138_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(_safe_div(closeunadj, close), 4), 4), 4))
def cg_f090_price_adjustment_context_core138_3rd_v139_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(_safe_div(high, low), 4), 4), 4))
def cg_f090_price_adjustment_context_core139_3rd_v140_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_diff(_diff(_diff(_safe_div(close, open), 4), 4), 4))
def cg_f090_price_adjustment_context_core140_3rd_v141_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(close, 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core141_3rd_v142_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(closeadj, 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core142_3rd_v143_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(closeunadj, 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core143_3rd_v144_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(open, 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core144_3rd_v145_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(high, 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core145_3rd_v146_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(low, 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core146_3rd_v147_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(_safe_div(closeadj, close), 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core147_3rd_v148_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(_safe_div(closeunadj, close), 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core148_3rd_v149_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(_safe_div(high, low), 4), 4), 4), 8))
def cg_f090_price_adjustment_context_core149_3rd_v150_signal(close, closeadj, closeunadj, open, high, low):
    return _clean(_z(_slope(_diff(_diff(_safe_div(close, open), 4), 4), 4), 8))