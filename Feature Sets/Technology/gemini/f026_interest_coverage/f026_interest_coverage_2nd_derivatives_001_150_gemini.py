import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f026_interest_coverage_core00_2nd_v001_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebit, 4))
def cg_f026_interest_coverage_core01_2nd_v002_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebitda, 4))
def cg_f026_interest_coverage_core02_2nd_v003_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ncfo, 4))
def cg_f026_interest_coverage_core03_2nd_v004_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core04_2nd_v005_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core05_2nd_v006_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core06_2nd_v007_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4))
def cg_f026_interest_coverage_core07_2nd_v008_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4))
def cg_f026_interest_coverage_core08_2nd_v009_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebit - intexp, 4))
def cg_f026_interest_coverage_core09_2nd_v010_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebitda - intexp, 4))
def cg_f026_interest_coverage_core10_2nd_v011_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebit, 8))
def cg_f026_interest_coverage_core11_2nd_v012_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebitda, 8))
def cg_f026_interest_coverage_core12_2nd_v013_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ncfo, 8))
def cg_f026_interest_coverage_core13_2nd_v014_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ebit, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core14_2nd_v015_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core15_2nd_v016_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 8))
def cg_f026_interest_coverage_core16_2nd_v017_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 8))
def cg_f026_interest_coverage_core17_2nd_v018_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 8))
def cg_f026_interest_coverage_core18_2nd_v019_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebit - intexp, 8))
def cg_f026_interest_coverage_core19_2nd_v020_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(ebitda - intexp, 8))
def cg_f026_interest_coverage_core20_2nd_v021_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(ebit, 4))
def cg_f026_interest_coverage_core21_2nd_v022_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(ebitda, 4))
def cg_f026_interest_coverage_core22_2nd_v023_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(ncfo, 4))
def cg_f026_interest_coverage_core23_2nd_v024_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core24_2nd_v025_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core25_2nd_v026_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4))
def cg_f026_interest_coverage_core26_2nd_v027_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4))
def cg_f026_interest_coverage_core27_2nd_v028_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4))
def cg_f026_interest_coverage_core28_2nd_v029_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(ebit - intexp, 4))
def cg_f026_interest_coverage_core29_2nd_v030_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(ebitda - intexp, 4))
def cg_f026_interest_coverage_core30_2nd_v031_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebit, 4), 8))
def cg_f026_interest_coverage_core31_2nd_v032_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebitda, 4), 8))
def cg_f026_interest_coverage_core32_2nd_v033_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f026_interest_coverage_core33_2nd_v034_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core34_2nd_v035_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core35_2nd_v036_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core36_2nd_v037_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core37_2nd_v038_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core38_2nd_v039_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebit - intexp, 4), 8))
def cg_f026_interest_coverage_core39_2nd_v040_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebitda - intexp, 4), 8))
def cg_f026_interest_coverage_core40_2nd_v041_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebit, 8), 12))
def cg_f026_interest_coverage_core41_2nd_v042_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebitda, 8), 12))
def cg_f026_interest_coverage_core42_2nd_v043_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f026_interest_coverage_core43_2nd_v044_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ebit, intexp.abs() + 1.0), 8), 12))
def cg_f026_interest_coverage_core44_2nd_v045_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 8), 12))
def cg_f026_interest_coverage_core45_2nd_v046_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 8), 12))
def cg_f026_interest_coverage_core46_2nd_v047_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 8), 12))
def cg_f026_interest_coverage_core47_2nd_v048_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 8), 12))
def cg_f026_interest_coverage_core48_2nd_v049_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebit - intexp, 8), 12))
def cg_f026_interest_coverage_core49_2nd_v050_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_slope(ebitda - intexp, 8), 12))
def cg_f026_interest_coverage_core50_2nd_v051_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(ebit, 4), 8))
def cg_f026_interest_coverage_core51_2nd_v052_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(ebitda, 4), 8))
def cg_f026_interest_coverage_core52_2nd_v053_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f026_interest_coverage_core53_2nd_v054_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core54_2nd_v055_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core55_2nd_v056_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core56_2nd_v057_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core57_2nd_v058_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 8))
def cg_f026_interest_coverage_core58_2nd_v059_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(ebit - intexp, 4), 8))
def cg_f026_interest_coverage_core59_2nd_v060_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(ebitda - intexp, 4), 8))
def cg_f026_interest_coverage_core60_2nd_v061_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(ebit, 4), 12))
def cg_f026_interest_coverage_core61_2nd_v062_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(ebitda, 4), 12))
def cg_f026_interest_coverage_core62_2nd_v063_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f026_interest_coverage_core63_2nd_v064_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core64_2nd_v065_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core65_2nd_v066_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core66_2nd_v067_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core67_2nd_v068_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core68_2nd_v069_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(ebit - intexp, 4), 12))
def cg_f026_interest_coverage_core69_2nd_v070_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(ebitda - intexp, 4), 12))
def cg_f026_interest_coverage_core70_2nd_v071_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(ebit, 4), 12))
def cg_f026_interest_coverage_core71_2nd_v072_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(ebitda, 4), 12))
def cg_f026_interest_coverage_core72_2nd_v073_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f026_interest_coverage_core73_2nd_v074_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core74_2nd_v075_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core75_2nd_v076_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core76_2nd_v077_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core77_2nd_v078_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 12))
def cg_f026_interest_coverage_core78_2nd_v079_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(ebit - intexp, 4), 12))
def cg_f026_interest_coverage_core79_2nd_v080_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_diff(ebitda - intexp, 4), 12))
def cg_f026_interest_coverage_core80_2nd_v081_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(ebit, 4), 4))
def cg_f026_interest_coverage_core81_2nd_v082_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(ebitda, 4), 4))
def cg_f026_interest_coverage_core82_2nd_v083_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f026_interest_coverage_core83_2nd_v084_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_safe_div(ebit, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core84_2nd_v085_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core85_2nd_v086_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core86_2nd_v087_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core87_2nd_v088_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core88_2nd_v089_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(ebit - intexp, 4), 4))
def cg_f026_interest_coverage_core89_2nd_v090_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_slope(ebitda - intexp, 4), 4))
def cg_f026_interest_coverage_core90_2nd_v091_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(ebit, 4), 4))
def cg_f026_interest_coverage_core91_2nd_v092_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(ebitda, 4), 4))
def cg_f026_interest_coverage_core92_2nd_v093_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f026_interest_coverage_core93_2nd_v094_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_safe_div(ebit, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core94_2nd_v095_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core95_2nd_v096_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core96_2nd_v097_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core97_2nd_v098_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core98_2nd_v099_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(ebit - intexp, 4), 4))
def cg_f026_interest_coverage_core99_2nd_v100_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_mean(_diff(ebitda - intexp, 4), 4))
def cg_f026_interest_coverage_core100_2nd_v101_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebit, 4), 4))
def cg_f026_interest_coverage_core101_2nd_v102_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebitda, 4), 4))
def cg_f026_interest_coverage_core102_2nd_v103_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f026_interest_coverage_core103_2nd_v104_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ebit, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core104_2nd_v105_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core105_2nd_v106_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core106_2nd_v107_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core107_2nd_v108_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core108_2nd_v109_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebit - intexp, 4), 4))
def cg_f026_interest_coverage_core109_2nd_v110_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebitda - intexp, 4), 4))
def cg_f026_interest_coverage_core110_2nd_v111_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebit, 8), 8))
def cg_f026_interest_coverage_core111_2nd_v112_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebitda, 8), 8))
def cg_f026_interest_coverage_core112_2nd_v113_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f026_interest_coverage_core113_2nd_v114_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ebit, intexp.abs() + 1.0), 8), 8))
def cg_f026_interest_coverage_core114_2nd_v115_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 8), 8))
def cg_f026_interest_coverage_core115_2nd_v116_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 8), 8))
def cg_f026_interest_coverage_core116_2nd_v117_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ebit, ebitda.abs() + 1.0), 8), 8))
def cg_f026_interest_coverage_core117_2nd_v118_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(_safe_div(ncfo, ebitda.abs() + 1.0), 8), 8))
def cg_f026_interest_coverage_core118_2nd_v119_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebit - intexp, 8), 8))
def cg_f026_interest_coverage_core119_2nd_v120_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_slope(_mean(ebitda - intexp, 8), 8))
def cg_f026_interest_coverage_core120_2nd_v121_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(ebit, 4), 4))
def cg_f026_interest_coverage_core121_2nd_v122_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(ebitda, 4), 4))
def cg_f026_interest_coverage_core122_2nd_v123_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f026_interest_coverage_core123_2nd_v124_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(_safe_div(ebit, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core124_2nd_v125_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core125_2nd_v126_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core126_2nd_v127_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core127_2nd_v128_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4))
def cg_f026_interest_coverage_core128_2nd_v129_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(ebit - intexp, 4), 4))
def cg_f026_interest_coverage_core129_2nd_v130_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_diff(_mean(ebitda - intexp, 4), 4))
def cg_f026_interest_coverage_core130_2nd_v131_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(ebit, 4), 4), 8))
def cg_f026_interest_coverage_core131_2nd_v132_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(ebitda, 4), 4), 8))
def cg_f026_interest_coverage_core132_2nd_v133_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f026_interest_coverage_core133_2nd_v134_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core134_2nd_v135_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core135_2nd_v136_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core136_2nd_v137_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core137_2nd_v138_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 8))
def cg_f026_interest_coverage_core138_2nd_v139_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(ebit - intexp, 4), 4), 8))
def cg_f026_interest_coverage_core139_2nd_v140_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_z(_diff(_mean(ebitda - intexp, 4), 4), 8))
def cg_f026_interest_coverage_core140_2nd_v141_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(ebit, 4), 4), 12))
def cg_f026_interest_coverage_core141_2nd_v142_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(ebitda, 4), 4), 12))
def cg_f026_interest_coverage_core142_2nd_v143_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f026_interest_coverage_core143_2nd_v144_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(_safe_div(ebit, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core144_2nd_v145_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(_safe_div(ebitda, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core145_2nd_v146_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, intexp.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core146_2nd_v147_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(_safe_div(ebit, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core147_2nd_v148_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, ebitda.abs() + 1.0), 4), 4), 12))
def cg_f026_interest_coverage_core148_2nd_v149_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(ebit - intexp, 4), 4), 12))
def cg_f026_interest_coverage_core149_2nd_v150_signal(intexp, ebit, ebitda, ncfo):
    return _clean(_rank(_slope(_mean(ebitda - intexp, 4), 4), 12))