import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f053_ebitda_margin_core00_3rd_v001_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(ebitda, 4), 4))
def cg_f053_ebitda_margin_core01_3rd_v002_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core02_3rd_v003_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f053_ebitda_margin_core03_3rd_v004_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_safe_div(ebitda, revenue), 4), 4))
def cg_f053_ebitda_margin_core04_3rd_v005_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core05_3rd_v006_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_pct_change(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core06_3rd_v007_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_slope(ebitdamargin, 8), 4), 4))
def cg_f053_ebitda_margin_core07_3rd_v008_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_z(ebitdamargin, 12), 4), 4))
def cg_f053_ebitda_margin_core08_3rd_v009_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_mean(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core09_3rd_v010_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4))
def cg_f053_ebitda_margin_core10_3rd_v011_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(ebitda, 4), 8))
def cg_f053_ebitda_margin_core11_3rd_v012_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core12_3rd_v013_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f053_ebitda_margin_core13_3rd_v014_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_safe_div(ebitda, revenue), 4), 8))
def cg_f053_ebitda_margin_core14_3rd_v015_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core15_3rd_v016_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_pct_change(ebitda, 4), 4), 8))
def cg_f053_ebitda_margin_core16_3rd_v017_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_slope(ebitdamargin, 8), 4), 8))
def cg_f053_ebitda_margin_core17_3rd_v018_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_z(ebitdamargin, 12), 4), 8))
def cg_f053_ebitda_margin_core18_3rd_v019_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_mean(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core19_3rd_v020_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 8))
def cg_f053_ebitda_margin_core20_3rd_v021_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(ebitda, 4), 4))
def cg_f053_ebitda_margin_core21_3rd_v022_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core22_3rd_v023_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(revenue, 4), 4))
def cg_f053_ebitda_margin_core23_3rd_v024_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_safe_div(ebitda, revenue), 4), 4))
def cg_f053_ebitda_margin_core24_3rd_v025_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core25_3rd_v026_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_pct_change(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core26_3rd_v027_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_slope(ebitdamargin, 8), 4), 4))
def cg_f053_ebitda_margin_core27_3rd_v028_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_z(ebitdamargin, 12), 4), 4))
def cg_f053_ebitda_margin_core28_3rd_v029_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_mean(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core29_3rd_v030_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4))
def cg_f053_ebitda_margin_core30_3rd_v031_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(ebitda, 4), 4), 8))
def cg_f053_ebitda_margin_core31_3rd_v032_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core32_3rd_v033_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f053_ebitda_margin_core33_3rd_v034_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_safe_div(ebitda, revenue), 4), 4), 8))
def cg_f053_ebitda_margin_core34_3rd_v035_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_diff(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core35_3rd_v036_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_pct_change(ebitda, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core36_3rd_v037_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_slope(ebitdamargin, 8), 4), 4), 8))
def cg_f053_ebitda_margin_core37_3rd_v038_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_z(ebitdamargin, 12), 4), 4), 8))
def cg_f053_ebitda_margin_core38_3rd_v039_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_mean(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core39_3rd_v040_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 8))
def cg_f053_ebitda_margin_core40_3rd_v041_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(ebitda, 4), 8), 12))
def cg_f053_ebitda_margin_core41_3rd_v042_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(ebitdamargin, 4), 8), 12))
def cg_f053_ebitda_margin_core42_3rd_v043_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f053_ebitda_margin_core43_3rd_v044_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_safe_div(ebitda, revenue), 4), 8), 12))
def cg_f053_ebitda_margin_core44_3rd_v045_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(ebitdamargin, 4), 4), 8), 12))
def cg_f053_ebitda_margin_core45_3rd_v046_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_pct_change(ebitda, 4), 4), 8), 12))
def cg_f053_ebitda_margin_core46_3rd_v047_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_slope(ebitdamargin, 8), 4), 8), 12))
def cg_f053_ebitda_margin_core47_3rd_v048_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_z(ebitdamargin, 12), 4), 8), 12))
def cg_f053_ebitda_margin_core48_3rd_v049_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_mean(ebitdamargin, 4), 4), 8), 12))
def cg_f053_ebitda_margin_core49_3rd_v050_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 8), 12))
def cg_f053_ebitda_margin_core50_3rd_v051_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(ebitda, 4), 4), 8))
def cg_f053_ebitda_margin_core51_3rd_v052_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core52_3rd_v053_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(revenue, 4), 4), 8))
def cg_f053_ebitda_margin_core53_3rd_v054_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_safe_div(ebitda, revenue), 4), 4), 8))
def cg_f053_ebitda_margin_core54_3rd_v055_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_diff(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core55_3rd_v056_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_pct_change(ebitda, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core56_3rd_v057_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_slope(ebitdamargin, 8), 4), 4), 8))
def cg_f053_ebitda_margin_core57_3rd_v058_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_z(ebitdamargin, 12), 4), 4), 8))
def cg_f053_ebitda_margin_core58_3rd_v059_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_mean(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core59_3rd_v060_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 8))
def cg_f053_ebitda_margin_core60_3rd_v061_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(ebitda, 4), 4), 12))
def cg_f053_ebitda_margin_core61_3rd_v062_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core62_3rd_v063_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f053_ebitda_margin_core63_3rd_v064_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_safe_div(ebitda, revenue), 4), 4), 12))
def cg_f053_ebitda_margin_core64_3rd_v065_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_diff(ebitdamargin, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core65_3rd_v066_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_pct_change(ebitda, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core66_3rd_v067_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_slope(ebitdamargin, 8), 4), 4), 12))
def cg_f053_ebitda_margin_core67_3rd_v068_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_z(ebitdamargin, 12), 4), 4), 12))
def cg_f053_ebitda_margin_core68_3rd_v069_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_mean(ebitdamargin, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core69_3rd_v070_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 12))
def cg_f053_ebitda_margin_core70_3rd_v071_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(ebitda, 4), 8), 12))
def cg_f053_ebitda_margin_core71_3rd_v072_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(ebitdamargin, 4), 8), 12))
def cg_f053_ebitda_margin_core72_3rd_v073_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(revenue, 4), 8), 12))
def cg_f053_ebitda_margin_core73_3rd_v074_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_safe_div(ebitda, revenue), 4), 8), 12))
def cg_f053_ebitda_margin_core74_3rd_v075_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_diff(ebitdamargin, 4), 4), 8), 12))
def cg_f053_ebitda_margin_core75_3rd_v076_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_pct_change(ebitda, 4), 4), 8), 12))
def cg_f053_ebitda_margin_core76_3rd_v077_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_slope(ebitdamargin, 8), 4), 8), 12))
def cg_f053_ebitda_margin_core77_3rd_v078_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_z(ebitdamargin, 12), 4), 8), 12))
def cg_f053_ebitda_margin_core78_3rd_v079_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_mean(ebitdamargin, 4), 4), 8), 12))
def cg_f053_ebitda_margin_core79_3rd_v080_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 8), 12))
def cg_f053_ebitda_margin_core80_3rd_v081_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(ebitda, 4), 4), 12))
def cg_f053_ebitda_margin_core81_3rd_v082_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core82_3rd_v083_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(revenue, 4), 4), 12))
def cg_f053_ebitda_margin_core83_3rd_v084_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_safe_div(ebitda, revenue), 4), 4), 12))
def cg_f053_ebitda_margin_core84_3rd_v085_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_diff(ebitdamargin, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core85_3rd_v086_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_pct_change(ebitda, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core86_3rd_v087_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_slope(ebitdamargin, 8), 4), 4), 12))
def cg_f053_ebitda_margin_core87_3rd_v088_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_z(ebitdamargin, 12), 4), 4), 12))
def cg_f053_ebitda_margin_core88_3rd_v089_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_mean(ebitdamargin, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core89_3rd_v090_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 12))
def cg_f053_ebitda_margin_core90_3rd_v091_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core91_3rd_v092_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core92_3rd_v093_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f053_ebitda_margin_core93_3rd_v094_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_safe_div(ebitda, revenue), 4), 4), 4))
def cg_f053_ebitda_margin_core94_3rd_v095_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_diff(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core95_3rd_v096_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_pct_change(ebitda, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core96_3rd_v097_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_slope(ebitdamargin, 8), 4), 4), 4))
def cg_f053_ebitda_margin_core97_3rd_v098_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_z(ebitdamargin, 12), 4), 4), 4))
def cg_f053_ebitda_margin_core98_3rd_v099_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_mean(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core99_3rd_v100_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 4))
def cg_f053_ebitda_margin_core100_3rd_v101_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(ebitda, 4), 8), 4))
def cg_f053_ebitda_margin_core101_3rd_v102_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(ebitdamargin, 4), 8), 4))
def cg_f053_ebitda_margin_core102_3rd_v103_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(revenue, 4), 8), 4))
def cg_f053_ebitda_margin_core103_3rd_v104_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_safe_div(ebitda, revenue), 4), 8), 4))
def cg_f053_ebitda_margin_core104_3rd_v105_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_diff(ebitdamargin, 4), 4), 8), 4))
def cg_f053_ebitda_margin_core105_3rd_v106_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_pct_change(ebitda, 4), 4), 8), 4))
def cg_f053_ebitda_margin_core106_3rd_v107_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_slope(ebitdamargin, 8), 4), 8), 4))
def cg_f053_ebitda_margin_core107_3rd_v108_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_z(ebitdamargin, 12), 4), 8), 4))
def cg_f053_ebitda_margin_core108_3rd_v109_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_mean(ebitdamargin, 4), 4), 8), 4))
def cg_f053_ebitda_margin_core109_3rd_v110_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 8), 4))
def cg_f053_ebitda_margin_core110_3rd_v111_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core111_3rd_v112_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core112_3rd_v113_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(revenue, 4), 4), 4))
def cg_f053_ebitda_margin_core113_3rd_v114_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_safe_div(ebitda, revenue), 4), 4), 4))
def cg_f053_ebitda_margin_core114_3rd_v115_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_diff(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core115_3rd_v116_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_pct_change(ebitda, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core116_3rd_v117_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_slope(ebitdamargin, 8), 4), 4), 4))
def cg_f053_ebitda_margin_core117_3rd_v118_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_z(ebitdamargin, 12), 4), 4), 4))
def cg_f053_ebitda_margin_core118_3rd_v119_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_mean(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core119_3rd_v120_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 4))
def cg_f053_ebitda_margin_core120_3rd_v121_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core121_3rd_v122_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core122_3rd_v123_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(revenue, 4), 4), 4))
def cg_f053_ebitda_margin_core123_3rd_v124_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_safe_div(ebitda, revenue), 4), 4), 4))
def cg_f053_ebitda_margin_core124_3rd_v125_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_diff(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core125_3rd_v126_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_pct_change(ebitda, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core126_3rd_v127_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_slope(ebitdamargin, 8), 4), 4), 4))
def cg_f053_ebitda_margin_core127_3rd_v128_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_z(ebitdamargin, 12), 4), 4), 4))
def cg_f053_ebitda_margin_core128_3rd_v129_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_mean(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core129_3rd_v130_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 4))
def cg_f053_ebitda_margin_core130_3rd_v131_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core131_3rd_v132_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core132_3rd_v133_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(revenue, 4), 4), 4))
def cg_f053_ebitda_margin_core133_3rd_v134_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_safe_div(ebitda, revenue), 4), 4), 4))
def cg_f053_ebitda_margin_core134_3rd_v135_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_diff(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core135_3rd_v136_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_pct_change(ebitda, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core136_3rd_v137_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_slope(ebitdamargin, 8), 4), 4), 4))
def cg_f053_ebitda_margin_core137_3rd_v138_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_z(ebitdamargin, 12), 4), 4), 4))
def cg_f053_ebitda_margin_core138_3rd_v139_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_mean(ebitdamargin, 4), 4), 4), 4))
def cg_f053_ebitda_margin_core139_3rd_v140_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 4))
def cg_f053_ebitda_margin_core140_3rd_v141_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(ebitda, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core141_3rd_v142_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core142_3rd_v143_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(revenue, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core143_3rd_v144_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebitda, revenue), 4), 4), 4), 8))
def cg_f053_ebitda_margin_core144_3rd_v145_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_diff(ebitdamargin, 4), 4), 4), 4), 8))
def cg_f053_ebitda_margin_core145_3rd_v146_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_pct_change(ebitda, 4), 4), 4), 4), 8))
def cg_f053_ebitda_margin_core146_3rd_v147_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_slope(ebitdamargin, 8), 4), 4), 4), 8))
def cg_f053_ebitda_margin_core147_3rd_v148_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_z(ebitdamargin, 12), 4), 4), 4), 8))
def cg_f053_ebitda_margin_core148_3rd_v149_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_mean(ebitdamargin, 4), 4), 4), 4), 8))
def cg_f053_ebitda_margin_core149_3rd_v150_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 4), 8))