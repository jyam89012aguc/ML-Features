import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f026_interest_coverage_core00_3rd_v001_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(ebit, 4), 4))
def cg_f026_interest_coverage_core01_3rd_v002_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(ebitda, 4), 4))
def cg_f026_interest_coverage_core02_3rd_v003_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(ncfo, 4), 4))
def cg_f026_interest_coverage_core03_3rd_v004_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core04_3rd_v005_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core05_3rd_v006_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core06_3rd_v007_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core07_3rd_v008_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core08_3rd_v009_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(ebit - intexp, 4), 4))
def cg_f026_interest_coverage_core09_3rd_v010_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(ebitda - intexp, 4), 4))
def cg_f026_interest_coverage_core10_3rd_v011_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(ebit, 4), 8))
def cg_f026_interest_coverage_core11_3rd_v012_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(ebitda, 4), 8))
def cg_f026_interest_coverage_core12_3rd_v013_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(ncfo, 4), 8))
def cg_f026_interest_coverage_core13_3rd_v014_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core14_3rd_v015_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core15_3rd_v016_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core16_3rd_v017_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core17_3rd_v018_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core18_3rd_v019_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(ebit - intexp, 4), 8))
def cg_f026_interest_coverage_core19_3rd_v020_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(ebitda - intexp, 4), 8))
def cg_f026_interest_coverage_core20_3rd_v021_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(ebit, 4), 4))
def cg_f026_interest_coverage_core21_3rd_v022_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(ebitda, 4), 4))
def cg_f026_interest_coverage_core22_3rd_v023_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(ncfo, 4), 4))
def cg_f026_interest_coverage_core23_3rd_v024_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core24_3rd_v025_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core25_3rd_v026_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core26_3rd_v027_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core27_3rd_v028_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core28_3rd_v029_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(ebit - intexp, 4), 4))
def cg_f026_interest_coverage_core29_3rd_v030_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_slope(ebitda - intexp, 4), 4))
def cg_f026_interest_coverage_core30_3rd_v031_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(ebit, 4), 4), 8))
def cg_f026_interest_coverage_core31_3rd_v032_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(ebitda, 4), 4), 8))
def cg_f026_interest_coverage_core32_3rd_v033_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(ncfo, 4), 4), 8))
def cg_f026_interest_coverage_core33_3rd_v034_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core34_3rd_v035_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core35_3rd_v036_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core36_3rd_v037_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core37_3rd_v038_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core38_3rd_v039_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(ebit - intexp, 4), 4), 8))
def cg_f026_interest_coverage_core39_3rd_v040_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_diff(ebitda - intexp, 4), 4), 8))
def cg_f026_interest_coverage_core40_3rd_v041_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(ebit, 4), 8), 12))
def cg_f026_interest_coverage_core41_3rd_v042_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(ebitda, 4), 8), 12))
def cg_f026_interest_coverage_core42_3rd_v043_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(ncfo, 4), 8), 12))
def cg_f026_interest_coverage_core43_3rd_v044_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core44_3rd_v045_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core45_3rd_v046_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core46_3rd_v047_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core47_3rd_v048_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core48_3rd_v049_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(ebit - intexp, 4), 8), 12))
def cg_f026_interest_coverage_core49_3rd_v050_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(ebitda - intexp, 4), 8), 12))
def cg_f026_interest_coverage_core50_3rd_v051_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(ebit, 4), 4), 8))
def cg_f026_interest_coverage_core51_3rd_v052_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(ebitda, 4), 4), 8))
def cg_f026_interest_coverage_core52_3rd_v053_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(ncfo, 4), 4), 8))
def cg_f026_interest_coverage_core53_3rd_v054_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core54_3rd_v055_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core55_3rd_v056_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core56_3rd_v057_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core57_3rd_v058_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core58_3rd_v059_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(ebit - intexp, 4), 4), 8))
def cg_f026_interest_coverage_core59_3rd_v060_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_slope(ebitda - intexp, 4), 4), 8))
def cg_f026_interest_coverage_core60_3rd_v061_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(ebit, 4), 4), 12))
def cg_f026_interest_coverage_core61_3rd_v062_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(ebitda, 4), 4), 12))
def cg_f026_interest_coverage_core62_3rd_v063_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(ncfo, 4), 4), 12))
def cg_f026_interest_coverage_core63_3rd_v064_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core64_3rd_v065_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core65_3rd_v066_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core66_3rd_v067_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core67_3rd_v068_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core68_3rd_v069_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(ebit - intexp, 4), 4), 12))
def cg_f026_interest_coverage_core69_3rd_v070_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_diff(ebitda - intexp, 4), 4), 12))
def cg_f026_interest_coverage_core70_3rd_v071_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(ebit, 4), 8), 12))
def cg_f026_interest_coverage_core71_3rd_v072_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(ebitda, 4), 8), 12))
def cg_f026_interest_coverage_core72_3rd_v073_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(ncfo, 4), 8), 12))
def cg_f026_interest_coverage_core73_3rd_v074_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core74_3rd_v075_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core75_3rd_v076_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core76_3rd_v077_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core77_3rd_v078_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 8), 12))
def cg_f026_interest_coverage_core78_3rd_v079_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(ebit - intexp, 4), 8), 12))
def cg_f026_interest_coverage_core79_3rd_v080_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_diff(ebitda - intexp, 4), 8), 12))
def cg_f026_interest_coverage_core80_3rd_v081_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(ebit, 4), 4), 12))
def cg_f026_interest_coverage_core81_3rd_v082_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(ebitda, 4), 4), 12))
def cg_f026_interest_coverage_core82_3rd_v083_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(ncfo, 4), 4), 12))
def cg_f026_interest_coverage_core83_3rd_v084_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core84_3rd_v085_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core85_3rd_v086_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core86_3rd_v087_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core87_3rd_v088_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core88_3rd_v089_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(ebit - intexp, 4), 4), 12))
def cg_f026_interest_coverage_core89_3rd_v090_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_slope(ebitda - intexp, 4), 4), 12))
def cg_f026_interest_coverage_core90_3rd_v091_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(ebit, 4), 4), 4))
def cg_f026_interest_coverage_core91_3rd_v092_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(ebitda, 4), 4), 4))
def cg_f026_interest_coverage_core92_3rd_v093_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(ncfo, 4), 4), 4))
def cg_f026_interest_coverage_core93_3rd_v094_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core94_3rd_v095_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core95_3rd_v096_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core96_3rd_v097_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core97_3rd_v098_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core98_3rd_v099_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(ebit - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core99_3rd_v100_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_diff(ebitda - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core100_3rd_v101_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(ebit, 4), 8), 4))
def cg_f026_interest_coverage_core101_3rd_v102_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(ebitda, 4), 8), 4))
def cg_f026_interest_coverage_core102_3rd_v103_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(ncfo, 4), 8), 4))
def cg_f026_interest_coverage_core103_3rd_v104_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 8), 4))
def cg_f026_interest_coverage_core104_3rd_v105_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 8), 4))
def cg_f026_interest_coverage_core105_3rd_v106_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 8), 4))
def cg_f026_interest_coverage_core106_3rd_v107_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 8), 4))
def cg_f026_interest_coverage_core107_3rd_v108_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 8), 4))
def cg_f026_interest_coverage_core108_3rd_v109_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(ebit - intexp, 4), 8), 4))
def cg_f026_interest_coverage_core109_3rd_v110_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_diff(ebitda - intexp, 4), 8), 4))
def cg_f026_interest_coverage_core110_3rd_v111_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(ebit, 4), 4), 4))
def cg_f026_interest_coverage_core111_3rd_v112_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(ebitda, 4), 4), 4))
def cg_f026_interest_coverage_core112_3rd_v113_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(ncfo, 4), 4), 4))
def cg_f026_interest_coverage_core113_3rd_v114_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core114_3rd_v115_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core115_3rd_v116_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core116_3rd_v117_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core117_3rd_v118_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core118_3rd_v119_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(ebit - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core119_3rd_v120_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_slope(ebitda - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core120_3rd_v121_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(ebit, 4), 4), 4))
def cg_f026_interest_coverage_core121_3rd_v122_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(ebitda, 4), 4), 4))
def cg_f026_interest_coverage_core122_3rd_v123_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(ncfo, 4), 4), 4))
def cg_f026_interest_coverage_core123_3rd_v124_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core124_3rd_v125_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core125_3rd_v126_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core126_3rd_v127_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core127_3rd_v128_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core128_3rd_v129_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(ebit - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core129_3rd_v130_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_diff(_diff(ebitda - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core130_3rd_v131_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(ebit, 4), 4), 4))
def cg_f026_interest_coverage_core131_3rd_v132_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(ebitda, 4), 4), 4))
def cg_f026_interest_coverage_core132_3rd_v133_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(ncfo, 4), 4), 4))
def cg_f026_interest_coverage_core133_3rd_v134_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core134_3rd_v135_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core135_3rd_v136_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core136_3rd_v137_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core137_3rd_v138_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 4))
def cg_f026_interest_coverage_core138_3rd_v139_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(ebit - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core139_3rd_v140_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_diff(_diff(ebitda - intexp, 4), 4), 4))
def cg_f026_interest_coverage_core140_3rd_v141_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(ebit, 4), 4), 4), 8))
def cg_f026_interest_coverage_core141_3rd_v142_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(ebitda, 4), 4), 4), 8))
def cg_f026_interest_coverage_core142_3rd_v143_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(ncfo, 4), 4), 4), 8))
def cg_f026_interest_coverage_core143_3rd_v144_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 4), 8))
def cg_f026_interest_coverage_core144_3rd_v145_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 4), 8))
def cg_f026_interest_coverage_core145_3rd_v146_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 4), 8))
def cg_f026_interest_coverage_core146_3rd_v147_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 4), 8))
def cg_f026_interest_coverage_core147_3rd_v148_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 4), 8))
def cg_f026_interest_coverage_core148_3rd_v149_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(ebit - intexp, 4), 4), 4), 8))
def cg_f026_interest_coverage_core149_3rd_v150_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_diff(_diff(ebitda - intexp, 4), 4), 4), 8))