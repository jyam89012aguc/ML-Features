import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f053_ebitda_margin_core00_2nd_v001_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(ebitda, 4))
def cg_f053_ebitda_margin_core01_2nd_v002_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(ebitdamargin, 4))
def cg_f053_ebitda_margin_core02_2nd_v003_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(revenue, 4))
def cg_f053_ebitda_margin_core03_2nd_v004_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_safe_div(ebitda, revenue), 4))
def cg_f053_ebitda_margin_core04_2nd_v005_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core05_2nd_v006_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_pct_change(ebitda, 4), 4))
def cg_f053_ebitda_margin_core06_2nd_v007_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_slope(ebitdamargin, 8), 4))
def cg_f053_ebitda_margin_core07_2nd_v008_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_z(ebitdamargin, 12), 4))
def cg_f053_ebitda_margin_core08_2nd_v009_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core09_2nd_v010_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core10_2nd_v011_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(ebitda, 8))
def cg_f053_ebitda_margin_core11_2nd_v012_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(ebitdamargin, 8))
def cg_f053_ebitda_margin_core12_2nd_v013_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(revenue, 8))
def cg_f053_ebitda_margin_core13_2nd_v014_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_safe_div(ebitda, revenue), 8))
def cg_f053_ebitda_margin_core14_2nd_v015_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core15_2nd_v016_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_pct_change(ebitda, 4), 8))
def cg_f053_ebitda_margin_core16_2nd_v017_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_slope(ebitdamargin, 8), 8))
def cg_f053_ebitda_margin_core17_2nd_v018_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_z(ebitdamargin, 12), 8))
def cg_f053_ebitda_margin_core18_2nd_v019_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core19_2nd_v020_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 8))
def cg_f053_ebitda_margin_core20_2nd_v021_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(ebitda, 4))
def cg_f053_ebitda_margin_core21_2nd_v022_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(ebitdamargin, 4))
def cg_f053_ebitda_margin_core22_2nd_v023_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(revenue, 4))
def cg_f053_ebitda_margin_core23_2nd_v024_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_safe_div(ebitda, revenue), 4))
def cg_f053_ebitda_margin_core24_2nd_v025_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core25_2nd_v026_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_pct_change(ebitda, 4), 4))
def cg_f053_ebitda_margin_core26_2nd_v027_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_slope(ebitdamargin, 8), 4))
def cg_f053_ebitda_margin_core27_2nd_v028_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_z(ebitdamargin, 12), 4))
def cg_f053_ebitda_margin_core28_2nd_v029_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core29_2nd_v030_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4))
def cg_f053_ebitda_margin_core30_2nd_v031_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(ebitda, 4), 8))
def cg_f053_ebitda_margin_core31_2nd_v032_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core32_2nd_v033_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f053_ebitda_margin_core33_2nd_v034_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_safe_div(ebitda, revenue), 4), 8))
def cg_f053_ebitda_margin_core34_2nd_v035_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core35_2nd_v036_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_pct_change(ebitda, 4), 4), 8))
def cg_f053_ebitda_margin_core36_2nd_v037_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_slope(ebitdamargin, 8), 4), 8))
def cg_f053_ebitda_margin_core37_2nd_v038_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_z(ebitdamargin, 12), 4), 8))
def cg_f053_ebitda_margin_core38_2nd_v039_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_mean(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core39_2nd_v040_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 8))
def cg_f053_ebitda_margin_core40_2nd_v041_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(ebitda, 8), 12))
def cg_f053_ebitda_margin_core41_2nd_v042_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(ebitdamargin, 8), 12))
def cg_f053_ebitda_margin_core42_2nd_v043_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f053_ebitda_margin_core43_2nd_v044_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_safe_div(ebitda, revenue), 8), 12))
def cg_f053_ebitda_margin_core44_2nd_v045_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_diff(ebitdamargin, 4), 8), 12))
def cg_f053_ebitda_margin_core45_2nd_v046_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_pct_change(ebitda, 4), 8), 12))
def cg_f053_ebitda_margin_core46_2nd_v047_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_slope(ebitdamargin, 8), 8), 12))
def cg_f053_ebitda_margin_core47_2nd_v048_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_z(ebitdamargin, 12), 8), 12))
def cg_f053_ebitda_margin_core48_2nd_v049_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_mean(ebitdamargin, 4), 8), 12))
def cg_f053_ebitda_margin_core49_2nd_v050_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 8), 12))
def cg_f053_ebitda_margin_core50_2nd_v051_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(ebitda, 4), 8))
def cg_f053_ebitda_margin_core51_2nd_v052_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(ebitdamargin, 4), 8))
def cg_f053_ebitda_margin_core52_2nd_v053_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f053_ebitda_margin_core53_2nd_v054_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_safe_div(ebitda, revenue), 4), 8))
def cg_f053_ebitda_margin_core54_2nd_v055_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_diff(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core55_2nd_v056_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_pct_change(ebitda, 4), 4), 8))
def cg_f053_ebitda_margin_core56_2nd_v057_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_slope(ebitdamargin, 8), 4), 8))
def cg_f053_ebitda_margin_core57_2nd_v058_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_z(ebitdamargin, 12), 4), 8))
def cg_f053_ebitda_margin_core58_2nd_v059_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core59_2nd_v060_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 8))
def cg_f053_ebitda_margin_core60_2nd_v061_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(ebitda, 4), 12))
def cg_f053_ebitda_margin_core61_2nd_v062_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(ebitdamargin, 4), 12))
def cg_f053_ebitda_margin_core62_2nd_v063_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f053_ebitda_margin_core63_2nd_v064_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_safe_div(ebitda, revenue), 4), 12))
def cg_f053_ebitda_margin_core64_2nd_v065_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_diff(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core65_2nd_v066_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_pct_change(ebitda, 4), 4), 12))
def cg_f053_ebitda_margin_core66_2nd_v067_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_slope(ebitdamargin, 8), 4), 12))
def cg_f053_ebitda_margin_core67_2nd_v068_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_z(ebitdamargin, 12), 4), 12))
def cg_f053_ebitda_margin_core68_2nd_v069_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core69_2nd_v070_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 12))
def cg_f053_ebitda_margin_core70_2nd_v071_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(ebitda, 4), 12))
def cg_f053_ebitda_margin_core71_2nd_v072_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(ebitdamargin, 4), 12))
def cg_f053_ebitda_margin_core72_2nd_v073_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f053_ebitda_margin_core73_2nd_v074_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_safe_div(ebitda, revenue), 4), 12))
def cg_f053_ebitda_margin_core74_2nd_v075_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_diff(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core75_2nd_v076_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_pct_change(ebitda, 4), 4), 12))
def cg_f053_ebitda_margin_core76_2nd_v077_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_slope(ebitdamargin, 8), 4), 12))
def cg_f053_ebitda_margin_core77_2nd_v078_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_z(ebitdamargin, 12), 4), 12))
def cg_f053_ebitda_margin_core78_2nd_v079_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_mean(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core79_2nd_v080_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 12))
def cg_f053_ebitda_margin_core80_2nd_v081_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(ebitda, 4), 4))
def cg_f053_ebitda_margin_core81_2nd_v082_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core82_2nd_v083_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f053_ebitda_margin_core83_2nd_v084_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_safe_div(ebitda, revenue), 4), 4))
def cg_f053_ebitda_margin_core84_2nd_v085_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core85_2nd_v086_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_pct_change(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core86_2nd_v087_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_slope(ebitdamargin, 8), 4), 4))
def cg_f053_ebitda_margin_core87_2nd_v088_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_z(ebitdamargin, 12), 4), 4))
def cg_f053_ebitda_margin_core88_2nd_v089_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_mean(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core89_2nd_v090_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_slope(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4))
def cg_f053_ebitda_margin_core90_2nd_v091_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(ebitda, 4), 4))
def cg_f053_ebitda_margin_core91_2nd_v092_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core92_2nd_v093_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f053_ebitda_margin_core93_2nd_v094_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_safe_div(ebitda, revenue), 4), 4))
def cg_f053_ebitda_margin_core94_2nd_v095_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core95_2nd_v096_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_pct_change(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core96_2nd_v097_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_slope(ebitdamargin, 8), 4), 4))
def cg_f053_ebitda_margin_core97_2nd_v098_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_z(ebitdamargin, 12), 4), 4))
def cg_f053_ebitda_margin_core98_2nd_v099_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_mean(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core99_2nd_v100_signal(ebitda, ebitdamargin, revenue):
    return _clean(_mean(_diff(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4))
def cg_f053_ebitda_margin_core100_2nd_v101_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(ebitda, 4), 4))
def cg_f053_ebitda_margin_core101_2nd_v102_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core102_2nd_v103_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f053_ebitda_margin_core103_2nd_v104_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_safe_div(ebitda, revenue), 4), 4))
def cg_f053_ebitda_margin_core104_2nd_v105_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core105_2nd_v106_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_pct_change(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core106_2nd_v107_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_slope(ebitdamargin, 8), 4), 4))
def cg_f053_ebitda_margin_core107_2nd_v108_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_z(ebitdamargin, 12), 4), 4))
def cg_f053_ebitda_margin_core108_2nd_v109_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_mean(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core109_2nd_v110_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4))
def cg_f053_ebitda_margin_core110_2nd_v111_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(ebitda, 8), 8))
def cg_f053_ebitda_margin_core111_2nd_v112_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(ebitdamargin, 8), 8))
def cg_f053_ebitda_margin_core112_2nd_v113_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f053_ebitda_margin_core113_2nd_v114_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_safe_div(ebitda, revenue), 8), 8))
def cg_f053_ebitda_margin_core114_2nd_v115_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_diff(ebitdamargin, 4), 8), 8))
def cg_f053_ebitda_margin_core115_2nd_v116_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_pct_change(ebitda, 4), 8), 8))
def cg_f053_ebitda_margin_core116_2nd_v117_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_slope(ebitdamargin, 8), 8), 8))
def cg_f053_ebitda_margin_core117_2nd_v118_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_z(ebitdamargin, 12), 8), 8))
def cg_f053_ebitda_margin_core118_2nd_v119_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_mean(ebitdamargin, 4), 8), 8))
def cg_f053_ebitda_margin_core119_2nd_v120_signal(ebitda, ebitdamargin, revenue):
    return _clean(_slope(_mean(_safe_div(ebitda, revenue.abs() + 1.0), 8), 8))
def cg_f053_ebitda_margin_core120_2nd_v121_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(ebitda, 4), 4))
def cg_f053_ebitda_margin_core121_2nd_v122_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(ebitdamargin, 4), 4))
def cg_f053_ebitda_margin_core122_2nd_v123_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f053_ebitda_margin_core123_2nd_v124_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_safe_div(ebitda, revenue), 4), 4))
def cg_f053_ebitda_margin_core124_2nd_v125_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_diff(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core125_2nd_v126_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_pct_change(ebitda, 4), 4), 4))
def cg_f053_ebitda_margin_core126_2nd_v127_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_slope(ebitdamargin, 8), 4), 4))
def cg_f053_ebitda_margin_core127_2nd_v128_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_z(ebitdamargin, 12), 4), 4))
def cg_f053_ebitda_margin_core128_2nd_v129_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_mean(ebitdamargin, 4), 4), 4))
def cg_f053_ebitda_margin_core129_2nd_v130_signal(ebitda, ebitdamargin, revenue):
    return _clean(_diff(_mean(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4))
def cg_f053_ebitda_margin_core130_2nd_v131_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(ebitda, 4), 4), 8))
def cg_f053_ebitda_margin_core131_2nd_v132_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(ebitdamargin, 4), 4), 8))
def cg_f053_ebitda_margin_core132_2nd_v133_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f053_ebitda_margin_core133_2nd_v134_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_safe_div(ebitda, revenue), 4), 4), 8))
def cg_f053_ebitda_margin_core134_2nd_v135_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_diff(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core135_2nd_v136_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_pct_change(ebitda, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core136_2nd_v137_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_slope(ebitdamargin, 8), 4), 4), 8))
def cg_f053_ebitda_margin_core137_2nd_v138_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_z(ebitdamargin, 12), 4), 4), 8))
def cg_f053_ebitda_margin_core138_2nd_v139_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_mean(ebitdamargin, 4), 4), 4), 8))
def cg_f053_ebitda_margin_core139_2nd_v140_signal(ebitda, ebitdamargin, revenue):
    return _clean(_z(_diff(_mean(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 8))
def cg_f053_ebitda_margin_core140_2nd_v141_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(ebitda, 4), 4), 12))
def cg_f053_ebitda_margin_core141_2nd_v142_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(ebitdamargin, 4), 4), 12))
def cg_f053_ebitda_margin_core142_2nd_v143_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f053_ebitda_margin_core143_2nd_v144_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(ebitda, revenue), 4), 4), 12))
def cg_f053_ebitda_margin_core144_2nd_v145_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_diff(ebitdamargin, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core145_2nd_v146_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_pct_change(ebitda, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core146_2nd_v147_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_slope(ebitdamargin, 8), 4), 4), 12))
def cg_f053_ebitda_margin_core147_2nd_v148_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_z(ebitdamargin, 12), 4), 4), 12))
def cg_f053_ebitda_margin_core148_2nd_v149_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_mean(ebitdamargin, 4), 4), 4), 12))
def cg_f053_ebitda_margin_core149_2nd_v150_signal(ebitda, ebitdamargin, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(ebitda, revenue.abs() + 1.0), 4), 4), 12))