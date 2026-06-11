import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f061_tax_rate_and_geography_core00_2nd_v001_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxexp, 4))
def cg_f061_tax_rate_and_geography_core01_2nd_v002_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(ebt, 4))
def cg_f061_tax_rate_and_geography_core02_2nd_v003_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxassets, 4))
def cg_f061_tax_rate_and_geography_core03_2nd_v004_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core04_2nd_v005_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core05_2nd_v006_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core06_2nd_v007_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxassets - taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core07_2nd_v008_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core08_2nd_v009_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core09_2nd_v010_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_pct_change(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core10_2nd_v011_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxexp, 8))
def cg_f061_tax_rate_and_geography_core11_2nd_v012_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(ebt, 8))
def cg_f061_tax_rate_and_geography_core12_2nd_v013_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxassets, 8))
def cg_f061_tax_rate_and_geography_core13_2nd_v014_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core14_2nd_v015_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core15_2nd_v016_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core16_2nd_v017_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(taxassets - taxliabilities, 8))
def cg_f061_tax_rate_and_geography_core17_2nd_v018_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 8))
def cg_f061_tax_rate_and_geography_core18_2nd_v019_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(taxexp, 4), 8))
def cg_f061_tax_rate_and_geography_core19_2nd_v020_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_pct_change(taxexp, 4), 8))
def cg_f061_tax_rate_and_geography_core20_2nd_v021_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxexp, 4))
def cg_f061_tax_rate_and_geography_core21_2nd_v022_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(ebt, 4))
def cg_f061_tax_rate_and_geography_core22_2nd_v023_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxassets, 4))
def cg_f061_tax_rate_and_geography_core23_2nd_v024_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core24_2nd_v025_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core25_2nd_v026_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core26_2nd_v027_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(taxassets - taxliabilities, 4))
def cg_f061_tax_rate_and_geography_core27_2nd_v028_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4))
def cg_f061_tax_rate_and_geography_core28_2nd_v029_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core29_2nd_v030_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_pct_change(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core30_2nd_v031_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxexp, 4), 8))
def cg_f061_tax_rate_and_geography_core31_2nd_v032_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(ebt, 4), 8))
def cg_f061_tax_rate_and_geography_core32_2nd_v033_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxassets, 4), 8))
def cg_f061_tax_rate_and_geography_core33_2nd_v034_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxliabilities, 4), 8))
def cg_f061_tax_rate_and_geography_core34_2nd_v035_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core35_2nd_v036_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core36_2nd_v037_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxassets - taxliabilities, 4), 8))
def cg_f061_tax_rate_and_geography_core37_2nd_v038_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core38_2nd_v039_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core39_2nd_v040_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_pct_change(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core40_2nd_v041_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxexp, 8), 12))
def cg_f061_tax_rate_and_geography_core41_2nd_v042_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(ebt, 8), 12))
def cg_f061_tax_rate_and_geography_core42_2nd_v043_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxassets, 8), 12))
def cg_f061_tax_rate_and_geography_core43_2nd_v044_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxliabilities, 8), 12))
def cg_f061_tax_rate_and_geography_core44_2nd_v045_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 8), 12))
def cg_f061_tax_rate_and_geography_core45_2nd_v046_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8), 12))
def cg_f061_tax_rate_and_geography_core46_2nd_v047_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(taxassets - taxliabilities, 8), 12))
def cg_f061_tax_rate_and_geography_core47_2nd_v048_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 8), 12))
def cg_f061_tax_rate_and_geography_core48_2nd_v049_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(taxexp, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core49_2nd_v050_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_pct_change(taxexp, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core50_2nd_v051_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(taxexp, 4), 8))
def cg_f061_tax_rate_and_geography_core51_2nd_v052_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(ebt, 4), 8))
def cg_f061_tax_rate_and_geography_core52_2nd_v053_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(taxassets, 4), 8))
def cg_f061_tax_rate_and_geography_core53_2nd_v054_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(taxliabilities, 4), 8))
def cg_f061_tax_rate_and_geography_core54_2nd_v055_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core55_2nd_v056_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core56_2nd_v057_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(taxassets - taxliabilities, 4), 8))
def cg_f061_tax_rate_and_geography_core57_2nd_v058_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core58_2nd_v059_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core59_2nd_v060_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_pct_change(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core60_2nd_v061_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(taxexp, 4), 12))
def cg_f061_tax_rate_and_geography_core61_2nd_v062_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(ebt, 4), 12))
def cg_f061_tax_rate_and_geography_core62_2nd_v063_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(taxassets, 4), 12))
def cg_f061_tax_rate_and_geography_core63_2nd_v064_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(taxliabilities, 4), 12))
def cg_f061_tax_rate_and_geography_core64_2nd_v065_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 12))
def cg_f061_tax_rate_and_geography_core65_2nd_v066_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 12))
def cg_f061_tax_rate_and_geography_core66_2nd_v067_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(taxassets - taxliabilities, 4), 12))
def cg_f061_tax_rate_and_geography_core67_2nd_v068_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 12))
def cg_f061_tax_rate_and_geography_core68_2nd_v069_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core69_2nd_v070_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_pct_change(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core70_2nd_v071_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(taxexp, 4), 12))
def cg_f061_tax_rate_and_geography_core71_2nd_v072_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(ebt, 4), 12))
def cg_f061_tax_rate_and_geography_core72_2nd_v073_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(taxassets, 4), 12))
def cg_f061_tax_rate_and_geography_core73_2nd_v074_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(taxliabilities, 4), 12))
def cg_f061_tax_rate_and_geography_core74_2nd_v075_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 12))
def cg_f061_tax_rate_and_geography_core75_2nd_v076_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 12))
def cg_f061_tax_rate_and_geography_core76_2nd_v077_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(taxassets - taxliabilities, 4), 12))
def cg_f061_tax_rate_and_geography_core77_2nd_v078_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 12))
def cg_f061_tax_rate_and_geography_core78_2nd_v079_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core79_2nd_v080_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_pct_change(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core80_2nd_v081_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core81_2nd_v082_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(ebt, 4), 4))
def cg_f061_tax_rate_and_geography_core82_2nd_v083_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(taxassets, 4), 4))
def cg_f061_tax_rate_and_geography_core83_2nd_v084_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core84_2nd_v085_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core85_2nd_v086_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core86_2nd_v087_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(taxassets - taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core87_2nd_v088_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core88_2nd_v089_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core89_2nd_v090_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_pct_change(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core90_2nd_v091_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core91_2nd_v092_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(ebt, 4), 4))
def cg_f061_tax_rate_and_geography_core92_2nd_v093_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(taxassets, 4), 4))
def cg_f061_tax_rate_and_geography_core93_2nd_v094_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core94_2nd_v095_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core95_2nd_v096_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core96_2nd_v097_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(taxassets - taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core97_2nd_v098_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core98_2nd_v099_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core99_2nd_v100_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_pct_change(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core100_2nd_v101_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core101_2nd_v102_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(ebt, 4), 4))
def cg_f061_tax_rate_and_geography_core102_2nd_v103_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxassets, 4), 4))
def cg_f061_tax_rate_and_geography_core103_2nd_v104_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core104_2nd_v105_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core105_2nd_v106_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core106_2nd_v107_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxassets - taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core107_2nd_v108_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core108_2nd_v109_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core109_2nd_v110_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_pct_change(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core110_2nd_v111_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxexp, 8), 8))
def cg_f061_tax_rate_and_geography_core111_2nd_v112_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(ebt, 8), 8))
def cg_f061_tax_rate_and_geography_core112_2nd_v113_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxassets, 8), 8))
def cg_f061_tax_rate_and_geography_core113_2nd_v114_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxliabilities, 8), 8))
def cg_f061_tax_rate_and_geography_core114_2nd_v115_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_safe_div(taxexp, ebt.abs() + 1.0), 8), 8))
def cg_f061_tax_rate_and_geography_core115_2nd_v116_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 8), 8))
def cg_f061_tax_rate_and_geography_core116_2nd_v117_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(taxassets - taxliabilities, 8), 8))
def cg_f061_tax_rate_and_geography_core117_2nd_v118_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 8), 8))
def cg_f061_tax_rate_and_geography_core118_2nd_v119_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_diff(taxexp, 4), 8), 8))
def cg_f061_tax_rate_and_geography_core119_2nd_v120_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_mean(_pct_change(taxexp, 4), 8), 8))
def cg_f061_tax_rate_and_geography_core120_2nd_v121_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core121_2nd_v122_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(ebt, 4), 4))
def cg_f061_tax_rate_and_geography_core122_2nd_v123_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(taxassets, 4), 4))
def cg_f061_tax_rate_and_geography_core123_2nd_v124_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core124_2nd_v125_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core125_2nd_v126_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core126_2nd_v127_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(taxassets - taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core127_2nd_v128_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core128_2nd_v129_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core129_2nd_v130_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_mean(_pct_change(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core130_2nd_v131_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core131_2nd_v132_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(ebt, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core132_2nd_v133_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(taxassets, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core133_2nd_v134_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(taxliabilities, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core134_2nd_v135_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core135_2nd_v136_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core136_2nd_v137_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(taxassets - taxliabilities, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core137_2nd_v138_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core138_2nd_v139_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(_diff(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core139_2nd_v140_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_mean(_pct_change(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core140_2nd_v141_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core141_2nd_v142_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(ebt, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core142_2nd_v143_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(taxassets, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core143_2nd_v144_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(taxliabilities, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core144_2nd_v145_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core145_2nd_v146_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core146_2nd_v147_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(taxassets - taxliabilities, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core147_2nd_v148_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core148_2nd_v149_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(_diff(taxexp, 4), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core149_2nd_v150_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_mean(_pct_change(taxexp, 4), 4), 4), 12))