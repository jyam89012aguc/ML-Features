import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f061_tax_rate_and_geography_core00_3rd_v001_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core01_3rd_v002_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(ebt, 4), 4))
def cg_f061_tax_rate_and_geography_core02_3rd_v003_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(taxassets, 4), 4))
def cg_f061_tax_rate_and_geography_core03_3rd_v004_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core04_3rd_v005_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core05_3rd_v006_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core06_3rd_v007_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(taxassets - taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core07_3rd_v008_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core08_3rd_v009_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core09_3rd_v010_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_pct_change(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core10_3rd_v011_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(taxexp, 4), 8))
def cg_f061_tax_rate_and_geography_core11_3rd_v012_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(ebt, 4), 8))
def cg_f061_tax_rate_and_geography_core12_3rd_v013_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(taxassets, 4), 8))
def cg_f061_tax_rate_and_geography_core13_3rd_v014_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(taxliabilities, 4), 8))
def cg_f061_tax_rate_and_geography_core14_3rd_v015_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core15_3rd_v016_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core16_3rd_v017_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(taxassets - taxliabilities, 4), 8))
def cg_f061_tax_rate_and_geography_core17_3rd_v018_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 8))
def cg_f061_tax_rate_and_geography_core18_3rd_v019_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core19_3rd_v020_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_pct_change(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core20_3rd_v021_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(taxexp, 4), 4))
def cg_f061_tax_rate_and_geography_core21_3rd_v022_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(ebt, 4), 4))
def cg_f061_tax_rate_and_geography_core22_3rd_v023_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(taxassets, 4), 4))
def cg_f061_tax_rate_and_geography_core23_3rd_v024_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core24_3rd_v025_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core25_3rd_v026_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core26_3rd_v027_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(taxassets - taxliabilities, 4), 4))
def cg_f061_tax_rate_and_geography_core27_3rd_v028_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4))
def cg_f061_tax_rate_and_geography_core28_3rd_v029_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core29_3rd_v030_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_slope(_pct_change(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core30_3rd_v031_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core31_3rd_v032_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(ebt, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core32_3rd_v033_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(taxassets, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core33_3rd_v034_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(taxliabilities, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core34_3rd_v035_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core35_3rd_v036_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core36_3rd_v037_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(taxassets - taxliabilities, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core37_3rd_v038_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core38_3rd_v039_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(_diff(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core39_3rd_v040_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_diff(_pct_change(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core40_3rd_v041_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(taxexp, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core41_3rd_v042_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(ebt, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core42_3rd_v043_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(taxassets, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core43_3rd_v044_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(taxliabilities, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core44_3rd_v045_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core45_3rd_v046_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core46_3rd_v047_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(taxassets - taxliabilities, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core47_3rd_v048_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core48_3rd_v049_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(taxexp, 4), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core49_3rd_v050_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_pct_change(taxexp, 4), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core50_3rd_v051_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(taxexp, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core51_3rd_v052_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(ebt, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core52_3rd_v053_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(taxassets, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core53_3rd_v054_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(taxliabilities, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core54_3rd_v055_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core55_3rd_v056_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core56_3rd_v057_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(taxassets - taxliabilities, 4), 4), 8))
def cg_f061_tax_rate_and_geography_core57_3rd_v058_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core58_3rd_v059_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(_diff(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core59_3rd_v060_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_diff(_slope(_pct_change(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core60_3rd_v061_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core61_3rd_v062_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(ebt, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core62_3rd_v063_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(taxassets, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core63_3rd_v064_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(taxliabilities, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core64_3rd_v065_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core65_3rd_v066_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core66_3rd_v067_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(taxassets - taxliabilities, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core67_3rd_v068_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core68_3rd_v069_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(_diff(taxexp, 4), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core69_3rd_v070_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_diff(_pct_change(taxexp, 4), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core70_3rd_v071_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(taxexp, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core71_3rd_v072_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(ebt, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core72_3rd_v073_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(taxassets, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core73_3rd_v074_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(taxliabilities, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core74_3rd_v075_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core75_3rd_v076_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core76_3rd_v077_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(taxassets - taxliabilities, 4), 8), 12))
def cg_f061_tax_rate_and_geography_core77_3rd_v078_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core78_3rd_v079_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(_diff(taxexp, 4), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core79_3rd_v080_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_slope(_diff(_pct_change(taxexp, 4), 4), 8), 12))
def cg_f061_tax_rate_and_geography_core80_3rd_v081_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(taxexp, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core81_3rd_v082_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(ebt, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core82_3rd_v083_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(taxassets, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core83_3rd_v084_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(taxliabilities, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core84_3rd_v085_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core85_3rd_v086_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core86_3rd_v087_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(taxassets - taxliabilities, 4), 4), 12))
def cg_f061_tax_rate_and_geography_core87_3rd_v088_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core88_3rd_v089_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(_diff(taxexp, 4), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core89_3rd_v090_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_rank(_diff(_slope(_pct_change(taxexp, 4), 4), 4), 12))
def cg_f061_tax_rate_and_geography_core90_3rd_v091_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core91_3rd_v092_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(ebt, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core92_3rd_v093_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(taxassets, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core93_3rd_v094_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core94_3rd_v095_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core95_3rd_v096_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core96_3rd_v097_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(taxassets - taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core97_3rd_v098_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core98_3rd_v099_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(_diff(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core99_3rd_v100_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_diff(_pct_change(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core100_3rd_v101_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(taxexp, 4), 8), 4))
def cg_f061_tax_rate_and_geography_core101_3rd_v102_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(ebt, 4), 8), 4))
def cg_f061_tax_rate_and_geography_core102_3rd_v103_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(taxassets, 4), 8), 4))
def cg_f061_tax_rate_and_geography_core103_3rd_v104_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(taxliabilities, 4), 8), 4))
def cg_f061_tax_rate_and_geography_core104_3rd_v105_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 8), 4))
def cg_f061_tax_rate_and_geography_core105_3rd_v106_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 8), 4))
def cg_f061_tax_rate_and_geography_core106_3rd_v107_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(taxassets - taxliabilities, 4), 8), 4))
def cg_f061_tax_rate_and_geography_core107_3rd_v108_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 8), 4))
def cg_f061_tax_rate_and_geography_core108_3rd_v109_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(_diff(taxexp, 4), 4), 8), 4))
def cg_f061_tax_rate_and_geography_core109_3rd_v110_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_slope(_diff(_pct_change(taxexp, 4), 4), 8), 4))
def cg_f061_tax_rate_and_geography_core110_3rd_v111_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core111_3rd_v112_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(ebt, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core112_3rd_v113_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(taxassets, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core113_3rd_v114_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core114_3rd_v115_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core115_3rd_v116_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core116_3rd_v117_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(taxassets - taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core117_3rd_v118_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core118_3rd_v119_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(_diff(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core119_3rd_v120_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_mean(_diff(_slope(_pct_change(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core120_3rd_v121_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core121_3rd_v122_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(ebt, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core122_3rd_v123_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(taxassets, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core123_3rd_v124_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core124_3rd_v125_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core125_3rd_v126_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core126_3rd_v127_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(taxassets - taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core127_3rd_v128_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core128_3rd_v129_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(_diff(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core129_3rd_v130_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_slope(_diff(_diff(_pct_change(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core130_3rd_v131_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(taxexp, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core131_3rd_v132_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(ebt, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core132_3rd_v133_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(taxassets, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core133_3rd_v134_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core134_3rd_v135_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core135_3rd_v136_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core136_3rd_v137_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(taxassets - taxliabilities, 4), 4), 4))
def cg_f061_tax_rate_and_geography_core137_3rd_v138_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core138_3rd_v139_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(_diff(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core139_3rd_v140_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_diff(_diff(_diff(_pct_change(taxexp, 4), 4), 4), 4))
def cg_f061_tax_rate_and_geography_core140_3rd_v141_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(taxexp, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core141_3rd_v142_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(ebt, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core142_3rd_v143_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(taxassets, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core143_3rd_v144_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(taxliabilities, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core144_3rd_v145_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(taxexp, ebt.abs() + 1.0), 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core145_3rd_v146_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(taxassets, taxliabilities.abs() + 1.0), 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core146_3rd_v147_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(taxassets - taxliabilities, 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core147_3rd_v148_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(_safe_div(taxassets - taxliabilities, ebt.abs() + 1.0), 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core148_3rd_v149_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(_diff(taxexp, 4), 4), 4), 4), 8))
def cg_f061_tax_rate_and_geography_core149_3rd_v150_signal(taxexp, ebt, taxassets, taxliabilities):
    return _clean(_z(_slope(_diff(_diff(_pct_change(taxexp, 4), 4), 4), 4), 8))