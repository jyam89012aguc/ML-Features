import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f015_interest_and_tax_drag_core00_3rd_v001_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(intexp, 4), 4))
def cg_f015_interest_and_tax_drag_core01_3rd_v002_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core02_3rd_v003_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_safe_div(intexp, debt), 4), 4))
def cg_f015_interest_and_tax_drag_core03_3rd_v004_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core04_3rd_v005_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core05_3rd_v006_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(intexp + taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core06_3rd_v007_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core07_3rd_v008_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core08_3rd_v009_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core09_3rd_v010_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core10_3rd_v011_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(intexp, 4), 8))
def cg_f015_interest_and_tax_drag_core11_3rd_v012_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(taxexp, 4), 8))
def cg_f015_interest_and_tax_drag_core12_3rd_v013_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_safe_div(intexp, debt), 4), 8))
def cg_f015_interest_and_tax_drag_core13_3rd_v014_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core14_3rd_v015_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core15_3rd_v016_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(intexp + taxexp, 4), 8))
def cg_f015_interest_and_tax_drag_core16_3rd_v017_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core17_3rd_v018_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core18_3rd_v019_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_log(intexp.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core19_3rd_v020_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_log(taxexp.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core20_3rd_v021_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(intexp, 4), 4))
def cg_f015_interest_and_tax_drag_core21_3rd_v022_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core22_3rd_v023_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_safe_div(intexp, debt), 4), 4))
def cg_f015_interest_and_tax_drag_core23_3rd_v024_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core24_3rd_v025_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core25_3rd_v026_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(intexp + taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core26_3rd_v027_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core27_3rd_v028_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core28_3rd_v029_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_log(intexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core29_3rd_v030_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_slope(_log(taxexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core30_3rd_v031_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(intexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core31_3rd_v032_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(taxexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core32_3rd_v033_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_safe_div(intexp, debt), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core33_3rd_v034_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core34_3rd_v035_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core35_3rd_v036_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(intexp + taxexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core36_3rd_v037_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core37_3rd_v038_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core38_3rd_v039_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core39_3rd_v040_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core40_3rd_v041_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(intexp, 4), 8), 12))
def cg_f015_interest_and_tax_drag_core41_3rd_v042_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(taxexp, 4), 8), 12))
def cg_f015_interest_and_tax_drag_core42_3rd_v043_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_safe_div(intexp, debt), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core43_3rd_v044_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core44_3rd_v045_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core45_3rd_v046_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(intexp + taxexp, 4), 8), 12))
def cg_f015_interest_and_tax_drag_core46_3rd_v047_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core47_3rd_v048_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core48_3rd_v049_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_log(intexp.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core49_3rd_v050_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_log(taxexp.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core50_3rd_v051_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(intexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core51_3rd_v052_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(taxexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core52_3rd_v053_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_safe_div(intexp, debt), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core53_3rd_v054_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core54_3rd_v055_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core55_3rd_v056_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(intexp + taxexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core56_3rd_v057_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core57_3rd_v058_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core58_3rd_v059_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_log(intexp.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core59_3rd_v060_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_slope(_log(taxexp.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core60_3rd_v061_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(intexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core61_3rd_v062_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(taxexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core62_3rd_v063_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_safe_div(intexp, debt), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core63_3rd_v064_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core64_3rd_v065_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core65_3rd_v066_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(intexp + taxexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core66_3rd_v067_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core67_3rd_v068_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core68_3rd_v069_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core69_3rd_v070_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core70_3rd_v071_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(intexp, 4), 8), 12))
def cg_f015_interest_and_tax_drag_core71_3rd_v072_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(taxexp, 4), 8), 12))
def cg_f015_interest_and_tax_drag_core72_3rd_v073_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_safe_div(intexp, debt), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core73_3rd_v074_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core74_3rd_v075_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core75_3rd_v076_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(intexp + taxexp, 4), 8), 12))
def cg_f015_interest_and_tax_drag_core76_3rd_v077_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core77_3rd_v078_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core78_3rd_v079_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_log(intexp.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core79_3rd_v080_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_diff(_log(taxexp.abs() + 1.0), 4), 8), 12))
def cg_f015_interest_and_tax_drag_core80_3rd_v081_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(intexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core81_3rd_v082_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(taxexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core82_3rd_v083_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_safe_div(intexp, debt), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core83_3rd_v084_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core84_3rd_v085_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core85_3rd_v086_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(intexp + taxexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core86_3rd_v087_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core87_3rd_v088_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core88_3rd_v089_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_log(intexp.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core89_3rd_v090_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_slope(_log(taxexp.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core90_3rd_v091_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(intexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core91_3rd_v092_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core92_3rd_v093_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_safe_div(intexp, debt), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core93_3rd_v094_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core94_3rd_v095_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core95_3rd_v096_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(intexp + taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core96_3rd_v097_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core97_3rd_v098_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core98_3rd_v099_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core99_3rd_v100_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core100_3rd_v101_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(intexp, 4), 8), 4))
def cg_f015_interest_and_tax_drag_core101_3rd_v102_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(taxexp, 4), 8), 4))
def cg_f015_interest_and_tax_drag_core102_3rd_v103_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_safe_div(intexp, debt), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core103_3rd_v104_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core104_3rd_v105_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core105_3rd_v106_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(intexp + taxexp, 4), 8), 4))
def cg_f015_interest_and_tax_drag_core106_3rd_v107_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core107_3rd_v108_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core108_3rd_v109_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_log(intexp.abs() + 1.0), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core109_3rd_v110_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_diff(_log(taxexp.abs() + 1.0), 4), 8), 4))
def cg_f015_interest_and_tax_drag_core110_3rd_v111_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(intexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core111_3rd_v112_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core112_3rd_v113_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_safe_div(intexp, debt), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core113_3rd_v114_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core114_3rd_v115_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core115_3rd_v116_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(intexp + taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core116_3rd_v117_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core117_3rd_v118_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core118_3rd_v119_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_log(intexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core119_3rd_v120_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_slope(_log(taxexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core120_3rd_v121_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(intexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core121_3rd_v122_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core122_3rd_v123_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_safe_div(intexp, debt), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core123_3rd_v124_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core124_3rd_v125_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core125_3rd_v126_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(intexp + taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core126_3rd_v127_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core127_3rd_v128_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core128_3rd_v129_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core129_3rd_v130_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core130_3rd_v131_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(intexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core131_3rd_v132_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core132_3rd_v133_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_safe_div(intexp, debt), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core133_3rd_v134_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core134_3rd_v135_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core135_3rd_v136_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(intexp + taxexp, 4), 4), 4))
def cg_f015_interest_and_tax_drag_core136_3rd_v137_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core137_3rd_v138_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core138_3rd_v139_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core139_3rd_v140_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4), 4))
def cg_f015_interest_and_tax_drag_core140_3rd_v141_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(intexp, 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core141_3rd_v142_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(taxexp, 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core142_3rd_v143_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(intexp, debt), 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core143_3rd_v144_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core144_3rd_v145_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core145_3rd_v146_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(intexp + taxexp, 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core146_3rd_v147_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core147_3rd_v148_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core148_3rd_v149_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_log(intexp.abs() + 1.0), 4), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core149_3rd_v150_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_diff(_diff(_log(taxexp.abs() + 1.0), 4), 4), 4), 8))