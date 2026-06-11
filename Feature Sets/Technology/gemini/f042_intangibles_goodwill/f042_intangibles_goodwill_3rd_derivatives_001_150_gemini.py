import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f042_intangibles_goodwill_core00_3rd_v001_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(intangibles, 4), 4))
def cg_f042_intangibles_goodwill_core01_3rd_v002_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_safe_div(intangibles, assets), 4), 4))
def cg_f042_intangibles_goodwill_core02_3rd_v003_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_safe_div(depamor, assets), 4), 4))
def cg_f042_intangibles_goodwill_core03_3rd_v004_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4))
def cg_f042_intangibles_goodwill_core04_3rd_v005_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(assets - intangibles, 4), 4))
def cg_f042_intangibles_goodwill_core05_3rd_v006_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core06_3rd_v007_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_pct_change(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core07_3rd_v008_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_slope(intangibles, 8), 4), 4))
def cg_f042_intangibles_goodwill_core08_3rd_v009_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_z(intangibles, 12), 4), 4))
def cg_f042_intangibles_goodwill_core09_3rd_v010_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_mean(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core10_3rd_v011_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(intangibles, 4), 8))
def cg_f042_intangibles_goodwill_core11_3rd_v012_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_safe_div(intangibles, assets), 4), 8))
def cg_f042_intangibles_goodwill_core12_3rd_v013_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_safe_div(depamor, assets), 4), 8))
def cg_f042_intangibles_goodwill_core13_3rd_v014_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 8))
def cg_f042_intangibles_goodwill_core14_3rd_v015_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(assets - intangibles, 4), 8))
def cg_f042_intangibles_goodwill_core15_3rd_v016_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core16_3rd_v017_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_pct_change(intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core17_3rd_v018_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_slope(intangibles, 8), 4), 8))
def cg_f042_intangibles_goodwill_core18_3rd_v019_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_z(intangibles, 12), 4), 8))
def cg_f042_intangibles_goodwill_core19_3rd_v020_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_mean(intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core20_3rd_v021_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(intangibles, 4), 4))
def cg_f042_intangibles_goodwill_core21_3rd_v022_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_safe_div(intangibles, assets), 4), 4))
def cg_f042_intangibles_goodwill_core22_3rd_v023_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_safe_div(depamor, assets), 4), 4))
def cg_f042_intangibles_goodwill_core23_3rd_v024_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4))
def cg_f042_intangibles_goodwill_core24_3rd_v025_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(assets - intangibles, 4), 4))
def cg_f042_intangibles_goodwill_core25_3rd_v026_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_diff(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core26_3rd_v027_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_pct_change(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core27_3rd_v028_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_slope(intangibles, 8), 4), 4))
def cg_f042_intangibles_goodwill_core28_3rd_v029_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_z(intangibles, 12), 4), 4))
def cg_f042_intangibles_goodwill_core29_3rd_v030_signal(intangibles, assets, depamor):
    return _clean(_diff(_slope(_mean(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core30_3rd_v031_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core31_3rd_v032_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 8))
def cg_f042_intangibles_goodwill_core32_3rd_v033_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_safe_div(depamor, assets), 4), 4), 8))
def cg_f042_intangibles_goodwill_core33_3rd_v034_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 8))
def cg_f042_intangibles_goodwill_core34_3rd_v035_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(assets - intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core35_3rd_v036_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_diff(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core36_3rd_v037_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_pct_change(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core37_3rd_v038_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_slope(intangibles, 8), 4), 4), 8))
def cg_f042_intangibles_goodwill_core38_3rd_v039_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_z(intangibles, 12), 4), 4), 8))
def cg_f042_intangibles_goodwill_core39_3rd_v040_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_diff(_mean(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core40_3rd_v041_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(intangibles, 4), 8), 12))
def cg_f042_intangibles_goodwill_core41_3rd_v042_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_safe_div(intangibles, assets), 4), 8), 12))
def cg_f042_intangibles_goodwill_core42_3rd_v043_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_safe_div(depamor, assets), 4), 8), 12))
def cg_f042_intangibles_goodwill_core43_3rd_v044_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 8), 12))
def cg_f042_intangibles_goodwill_core44_3rd_v045_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(assets - intangibles, 4), 8), 12))
def cg_f042_intangibles_goodwill_core45_3rd_v046_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(intangibles, 4), 4), 8), 12))
def cg_f042_intangibles_goodwill_core46_3rd_v047_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_pct_change(intangibles, 4), 4), 8), 12))
def cg_f042_intangibles_goodwill_core47_3rd_v048_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_slope(intangibles, 8), 4), 8), 12))
def cg_f042_intangibles_goodwill_core48_3rd_v049_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_z(intangibles, 12), 4), 8), 12))
def cg_f042_intangibles_goodwill_core49_3rd_v050_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_mean(intangibles, 4), 4), 8), 12))
def cg_f042_intangibles_goodwill_core50_3rd_v051_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core51_3rd_v052_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_safe_div(intangibles, assets), 4), 4), 8))
def cg_f042_intangibles_goodwill_core52_3rd_v053_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_safe_div(depamor, assets), 4), 4), 8))
def cg_f042_intangibles_goodwill_core53_3rd_v054_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 8))
def cg_f042_intangibles_goodwill_core54_3rd_v055_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(assets - intangibles, 4), 4), 8))
def cg_f042_intangibles_goodwill_core55_3rd_v056_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_diff(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core56_3rd_v057_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_pct_change(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core57_3rd_v058_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_slope(intangibles, 8), 4), 4), 8))
def cg_f042_intangibles_goodwill_core58_3rd_v059_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_z(intangibles, 12), 4), 4), 8))
def cg_f042_intangibles_goodwill_core59_3rd_v060_signal(intangibles, assets, depamor):
    return _clean(_z(_diff(_slope(_mean(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core60_3rd_v061_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(intangibles, 4), 4), 12))
def cg_f042_intangibles_goodwill_core61_3rd_v062_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 12))
def cg_f042_intangibles_goodwill_core62_3rd_v063_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_safe_div(depamor, assets), 4), 4), 12))
def cg_f042_intangibles_goodwill_core63_3rd_v064_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 12))
def cg_f042_intangibles_goodwill_core64_3rd_v065_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(assets - intangibles, 4), 4), 12))
def cg_f042_intangibles_goodwill_core65_3rd_v066_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_diff(intangibles, 4), 4), 4), 12))
def cg_f042_intangibles_goodwill_core66_3rd_v067_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_pct_change(intangibles, 4), 4), 4), 12))
def cg_f042_intangibles_goodwill_core67_3rd_v068_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_slope(intangibles, 8), 4), 4), 12))
def cg_f042_intangibles_goodwill_core68_3rd_v069_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_z(intangibles, 12), 4), 4), 12))
def cg_f042_intangibles_goodwill_core69_3rd_v070_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_diff(_mean(intangibles, 4), 4), 4), 12))
def cg_f042_intangibles_goodwill_core70_3rd_v071_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(intangibles, 4), 8), 12))
def cg_f042_intangibles_goodwill_core71_3rd_v072_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_safe_div(intangibles, assets), 4), 8), 12))
def cg_f042_intangibles_goodwill_core72_3rd_v073_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_safe_div(depamor, assets), 4), 8), 12))
def cg_f042_intangibles_goodwill_core73_3rd_v074_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 8), 12))
def cg_f042_intangibles_goodwill_core74_3rd_v075_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(assets - intangibles, 4), 8), 12))
def cg_f042_intangibles_goodwill_core75_3rd_v076_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_diff(intangibles, 4), 4), 8), 12))
def cg_f042_intangibles_goodwill_core76_3rd_v077_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_pct_change(intangibles, 4), 4), 8), 12))
def cg_f042_intangibles_goodwill_core77_3rd_v078_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_slope(intangibles, 8), 4), 8), 12))
def cg_f042_intangibles_goodwill_core78_3rd_v079_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_z(intangibles, 12), 4), 8), 12))
def cg_f042_intangibles_goodwill_core79_3rd_v080_signal(intangibles, assets, depamor):
    return _clean(_rank(_slope(_diff(_mean(intangibles, 4), 4), 8), 12))
def cg_f042_intangibles_goodwill_core80_3rd_v081_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(intangibles, 4), 4), 12))
def cg_f042_intangibles_goodwill_core81_3rd_v082_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_safe_div(intangibles, assets), 4), 4), 12))
def cg_f042_intangibles_goodwill_core82_3rd_v083_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_safe_div(depamor, assets), 4), 4), 12))
def cg_f042_intangibles_goodwill_core83_3rd_v084_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 12))
def cg_f042_intangibles_goodwill_core84_3rd_v085_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(assets - intangibles, 4), 4), 12))
def cg_f042_intangibles_goodwill_core85_3rd_v086_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_diff(intangibles, 4), 4), 4), 12))
def cg_f042_intangibles_goodwill_core86_3rd_v087_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_pct_change(intangibles, 4), 4), 4), 12))
def cg_f042_intangibles_goodwill_core87_3rd_v088_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_slope(intangibles, 8), 4), 4), 12))
def cg_f042_intangibles_goodwill_core88_3rd_v089_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_z(intangibles, 12), 4), 4), 12))
def cg_f042_intangibles_goodwill_core89_3rd_v090_signal(intangibles, assets, depamor):
    return _clean(_rank(_diff(_slope(_mean(intangibles, 4), 4), 4), 12))
def cg_f042_intangibles_goodwill_core90_3rd_v091_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core91_3rd_v092_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core92_3rd_v093_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_safe_div(depamor, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core93_3rd_v094_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 4))
def cg_f042_intangibles_goodwill_core94_3rd_v095_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(assets - intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core95_3rd_v096_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_diff(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core96_3rd_v097_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_pct_change(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core97_3rd_v098_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_slope(intangibles, 8), 4), 4), 4))
def cg_f042_intangibles_goodwill_core98_3rd_v099_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_z(intangibles, 12), 4), 4), 4))
def cg_f042_intangibles_goodwill_core99_3rd_v100_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_diff(_mean(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core100_3rd_v101_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(intangibles, 4), 8), 4))
def cg_f042_intangibles_goodwill_core101_3rd_v102_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_safe_div(intangibles, assets), 4), 8), 4))
def cg_f042_intangibles_goodwill_core102_3rd_v103_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_safe_div(depamor, assets), 4), 8), 4))
def cg_f042_intangibles_goodwill_core103_3rd_v104_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 8), 4))
def cg_f042_intangibles_goodwill_core104_3rd_v105_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(assets - intangibles, 4), 8), 4))
def cg_f042_intangibles_goodwill_core105_3rd_v106_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_diff(intangibles, 4), 4), 8), 4))
def cg_f042_intangibles_goodwill_core106_3rd_v107_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_pct_change(intangibles, 4), 4), 8), 4))
def cg_f042_intangibles_goodwill_core107_3rd_v108_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_slope(intangibles, 8), 4), 8), 4))
def cg_f042_intangibles_goodwill_core108_3rd_v109_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_z(intangibles, 12), 4), 8), 4))
def cg_f042_intangibles_goodwill_core109_3rd_v110_signal(intangibles, assets, depamor):
    return _clean(_mean(_slope(_diff(_mean(intangibles, 4), 4), 8), 4))
def cg_f042_intangibles_goodwill_core110_3rd_v111_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core111_3rd_v112_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core112_3rd_v113_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_safe_div(depamor, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core113_3rd_v114_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 4))
def cg_f042_intangibles_goodwill_core114_3rd_v115_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(assets - intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core115_3rd_v116_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_diff(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core116_3rd_v117_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_pct_change(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core117_3rd_v118_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_slope(intangibles, 8), 4), 4), 4))
def cg_f042_intangibles_goodwill_core118_3rd_v119_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_z(intangibles, 12), 4), 4), 4))
def cg_f042_intangibles_goodwill_core119_3rd_v120_signal(intangibles, assets, depamor):
    return _clean(_mean(_diff(_slope(_mean(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core120_3rd_v121_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core121_3rd_v122_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core122_3rd_v123_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_safe_div(depamor, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core123_3rd_v124_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 4))
def cg_f042_intangibles_goodwill_core124_3rd_v125_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(assets - intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core125_3rd_v126_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_diff(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core126_3rd_v127_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_pct_change(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core127_3rd_v128_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_slope(intangibles, 8), 4), 4), 4))
def cg_f042_intangibles_goodwill_core128_3rd_v129_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_z(intangibles, 12), 4), 4), 4))
def cg_f042_intangibles_goodwill_core129_3rd_v130_signal(intangibles, assets, depamor):
    return _clean(_slope(_diff(_diff(_mean(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core130_3rd_v131_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core131_3rd_v132_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core132_3rd_v133_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_safe_div(depamor, assets), 4), 4), 4))
def cg_f042_intangibles_goodwill_core133_3rd_v134_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 4))
def cg_f042_intangibles_goodwill_core134_3rd_v135_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(assets - intangibles, 4), 4), 4))
def cg_f042_intangibles_goodwill_core135_3rd_v136_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_diff(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core136_3rd_v137_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_pct_change(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core137_3rd_v138_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_slope(intangibles, 8), 4), 4), 4))
def cg_f042_intangibles_goodwill_core138_3rd_v139_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_z(intangibles, 12), 4), 4), 4))
def cg_f042_intangibles_goodwill_core139_3rd_v140_signal(intangibles, assets, depamor):
    return _clean(_diff(_diff(_diff(_mean(intangibles, 4), 4), 4), 4))
def cg_f042_intangibles_goodwill_core140_3rd_v141_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core141_3rd_v142_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core142_3rd_v143_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_safe_div(depamor, assets), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core143_3rd_v144_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_safe_div(depamor, intangibles.abs() + 1.0), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core144_3rd_v145_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(assets - intangibles, 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core145_3rd_v146_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_diff(intangibles, 4), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core146_3rd_v147_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_pct_change(intangibles, 4), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core147_3rd_v148_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_slope(intangibles, 8), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core148_3rd_v149_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_z(intangibles, 12), 4), 4), 4), 8))
def cg_f042_intangibles_goodwill_core149_3rd_v150_signal(intangibles, assets, depamor):
    return _clean(_z(_slope(_diff(_diff(_mean(intangibles, 4), 4), 4), 4), 8))