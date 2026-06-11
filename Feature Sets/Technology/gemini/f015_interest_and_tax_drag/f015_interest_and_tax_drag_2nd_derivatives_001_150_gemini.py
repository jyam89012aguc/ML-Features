import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f015_interest_and_tax_drag_core00_2nd_v001_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(intexp, 4))
def cg_f015_interest_and_tax_drag_core01_2nd_v002_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(taxexp, 4))
def cg_f015_interest_and_tax_drag_core02_2nd_v003_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(intexp, debt), 4))
def cg_f015_interest_and_tax_drag_core03_2nd_v004_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core04_2nd_v005_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core05_2nd_v006_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(intexp + taxexp, 4))
def cg_f015_interest_and_tax_drag_core06_2nd_v007_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core07_2nd_v008_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core08_2nd_v009_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_log(intexp.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core09_2nd_v010_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_log(taxexp.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core10_2nd_v011_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(intexp, 8))
def cg_f015_interest_and_tax_drag_core11_2nd_v012_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(taxexp, 8))
def cg_f015_interest_and_tax_drag_core12_2nd_v013_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(intexp, debt), 8))
def cg_f015_interest_and_tax_drag_core13_2nd_v014_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 8))
def cg_f015_interest_and_tax_drag_core14_2nd_v015_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 8))
def cg_f015_interest_and_tax_drag_core15_2nd_v016_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(intexp + taxexp, 8))
def cg_f015_interest_and_tax_drag_core16_2nd_v017_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 8))
def cg_f015_interest_and_tax_drag_core17_2nd_v018_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_safe_div(debt, ncfo.abs() + 1.0), 8))
def cg_f015_interest_and_tax_drag_core18_2nd_v019_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_log(intexp.abs() + 1.0), 8))
def cg_f015_interest_and_tax_drag_core19_2nd_v020_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_log(taxexp.abs() + 1.0), 8))
def cg_f015_interest_and_tax_drag_core20_2nd_v021_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(intexp, 4))
def cg_f015_interest_and_tax_drag_core21_2nd_v022_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(taxexp, 4))
def cg_f015_interest_and_tax_drag_core22_2nd_v023_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_safe_div(intexp, debt), 4))
def cg_f015_interest_and_tax_drag_core23_2nd_v024_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core24_2nd_v025_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core25_2nd_v026_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(intexp + taxexp, 4))
def cg_f015_interest_and_tax_drag_core26_2nd_v027_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core27_2nd_v028_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core28_2nd_v029_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_log(intexp.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core29_2nd_v030_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_log(taxexp.abs() + 1.0), 4))
def cg_f015_interest_and_tax_drag_core30_2nd_v031_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(intexp, 4), 8))
def cg_f015_interest_and_tax_drag_core31_2nd_v032_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(taxexp, 4), 8))
def cg_f015_interest_and_tax_drag_core32_2nd_v033_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(intexp, debt), 4), 8))
def cg_f015_interest_and_tax_drag_core33_2nd_v034_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core34_2nd_v035_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core35_2nd_v036_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(intexp + taxexp, 4), 8))
def cg_f015_interest_and_tax_drag_core36_2nd_v037_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core37_2nd_v038_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core38_2nd_v039_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_log(intexp.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core39_2nd_v040_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_log(taxexp.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core40_2nd_v041_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(intexp, 8), 12))
def cg_f015_interest_and_tax_drag_core41_2nd_v042_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(taxexp, 8), 12))
def cg_f015_interest_and_tax_drag_core42_2nd_v043_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(intexp, debt), 8), 12))
def cg_f015_interest_and_tax_drag_core43_2nd_v044_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 8), 12))
def cg_f015_interest_and_tax_drag_core44_2nd_v045_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 8), 12))
def cg_f015_interest_and_tax_drag_core45_2nd_v046_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(intexp + taxexp, 8), 12))
def cg_f015_interest_and_tax_drag_core46_2nd_v047_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 8), 12))
def cg_f015_interest_and_tax_drag_core47_2nd_v048_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_safe_div(debt, ncfo.abs() + 1.0), 8), 12))
def cg_f015_interest_and_tax_drag_core48_2nd_v049_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_log(intexp.abs() + 1.0), 8), 12))
def cg_f015_interest_and_tax_drag_core49_2nd_v050_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_slope(_log(taxexp.abs() + 1.0), 8), 12))
def cg_f015_interest_and_tax_drag_core50_2nd_v051_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(intexp, 4), 8))
def cg_f015_interest_and_tax_drag_core51_2nd_v052_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(taxexp, 4), 8))
def cg_f015_interest_and_tax_drag_core52_2nd_v053_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_safe_div(intexp, debt), 4), 8))
def cg_f015_interest_and_tax_drag_core53_2nd_v054_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core54_2nd_v055_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core55_2nd_v056_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(intexp + taxexp, 4), 8))
def cg_f015_interest_and_tax_drag_core56_2nd_v057_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core57_2nd_v058_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core58_2nd_v059_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_log(intexp.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core59_2nd_v060_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_log(taxexp.abs() + 1.0), 4), 8))
def cg_f015_interest_and_tax_drag_core60_2nd_v061_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(intexp, 4), 12))
def cg_f015_interest_and_tax_drag_core61_2nd_v062_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(taxexp, 4), 12))
def cg_f015_interest_and_tax_drag_core62_2nd_v063_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_safe_div(intexp, debt), 4), 12))
def cg_f015_interest_and_tax_drag_core63_2nd_v064_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core64_2nd_v065_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core65_2nd_v066_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(intexp + taxexp, 4), 12))
def cg_f015_interest_and_tax_drag_core66_2nd_v067_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core67_2nd_v068_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core68_2nd_v069_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_log(intexp.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core69_2nd_v070_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_log(taxexp.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core70_2nd_v071_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(intexp, 4), 12))
def cg_f015_interest_and_tax_drag_core71_2nd_v072_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(taxexp, 4), 12))
def cg_f015_interest_and_tax_drag_core72_2nd_v073_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_safe_div(intexp, debt), 4), 12))
def cg_f015_interest_and_tax_drag_core73_2nd_v074_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core74_2nd_v075_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core75_2nd_v076_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(intexp + taxexp, 4), 12))
def cg_f015_interest_and_tax_drag_core76_2nd_v077_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core77_2nd_v078_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core78_2nd_v079_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_log(intexp.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core79_2nd_v080_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_diff(_log(taxexp.abs() + 1.0), 4), 12))
def cg_f015_interest_and_tax_drag_core80_2nd_v081_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(intexp, 4), 4))
def cg_f015_interest_and_tax_drag_core81_2nd_v082_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core82_2nd_v083_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_safe_div(intexp, debt), 4), 4))
def cg_f015_interest_and_tax_drag_core83_2nd_v084_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core84_2nd_v085_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core85_2nd_v086_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(intexp + taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core86_2nd_v087_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core87_2nd_v088_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_safe_div(debt, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core88_2nd_v089_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_log(intexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core89_2nd_v090_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_slope(_log(taxexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core90_2nd_v091_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(intexp, 4), 4))
def cg_f015_interest_and_tax_drag_core91_2nd_v092_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core92_2nd_v093_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_safe_div(intexp, debt), 4), 4))
def cg_f015_interest_and_tax_drag_core93_2nd_v094_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core94_2nd_v095_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core95_2nd_v096_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(intexp + taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core96_2nd_v097_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core97_2nd_v098_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_safe_div(debt, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core98_2nd_v099_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_log(intexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core99_2nd_v100_signal(intexp, taxexp, ncfo, debt):
    return _clean(_mean(_diff(_log(taxexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core100_2nd_v101_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(intexp, 4), 4))
def cg_f015_interest_and_tax_drag_core101_2nd_v102_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core102_2nd_v103_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(intexp, debt), 4), 4))
def cg_f015_interest_and_tax_drag_core103_2nd_v104_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core104_2nd_v105_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core105_2nd_v106_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(intexp + taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core106_2nd_v107_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core107_2nd_v108_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(debt, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core108_2nd_v109_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_log(intexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core109_2nd_v110_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_log(taxexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core110_2nd_v111_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(intexp, 8), 8))
def cg_f015_interest_and_tax_drag_core111_2nd_v112_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(taxexp, 8), 8))
def cg_f015_interest_and_tax_drag_core112_2nd_v113_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(intexp, debt), 8), 8))
def cg_f015_interest_and_tax_drag_core113_2nd_v114_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(intexp, ncfo.abs() + 1.0), 8), 8))
def cg_f015_interest_and_tax_drag_core114_2nd_v115_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(taxexp, ncfo.abs() + 1.0), 8), 8))
def cg_f015_interest_and_tax_drag_core115_2nd_v116_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(intexp + taxexp, 8), 8))
def cg_f015_interest_and_tax_drag_core116_2nd_v117_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 8), 8))
def cg_f015_interest_and_tax_drag_core117_2nd_v118_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_safe_div(debt, ncfo.abs() + 1.0), 8), 8))
def cg_f015_interest_and_tax_drag_core118_2nd_v119_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_log(intexp.abs() + 1.0), 8), 8))
def cg_f015_interest_and_tax_drag_core119_2nd_v120_signal(intexp, taxexp, ncfo, debt):
    return _clean(_slope(_mean(_log(taxexp.abs() + 1.0), 8), 8))
def cg_f015_interest_and_tax_drag_core120_2nd_v121_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(intexp, 4), 4))
def cg_f015_interest_and_tax_drag_core121_2nd_v122_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core122_2nd_v123_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_safe_div(intexp, debt), 4), 4))
def cg_f015_interest_and_tax_drag_core123_2nd_v124_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core124_2nd_v125_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core125_2nd_v126_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(intexp + taxexp, 4), 4))
def cg_f015_interest_and_tax_drag_core126_2nd_v127_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core127_2nd_v128_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_safe_div(debt, ncfo.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core128_2nd_v129_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_log(intexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core129_2nd_v130_signal(intexp, taxexp, ncfo, debt):
    return _clean(_diff(_mean(_log(taxexp.abs() + 1.0), 4), 4))
def cg_f015_interest_and_tax_drag_core130_2nd_v131_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(intexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core131_2nd_v132_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(taxexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core132_2nd_v133_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_safe_div(intexp, debt), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core133_2nd_v134_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core134_2nd_v135_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core135_2nd_v136_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(intexp + taxexp, 4), 4), 8))
def cg_f015_interest_and_tax_drag_core136_2nd_v137_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core137_2nd_v138_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core138_2nd_v139_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_log(intexp.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core139_2nd_v140_signal(intexp, taxexp, ncfo, debt):
    return _clean(_z(_diff(_mean(_log(taxexp.abs() + 1.0), 4), 4), 8))
def cg_f015_interest_and_tax_drag_core140_2nd_v141_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(intexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core141_2nd_v142_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(taxexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core142_2nd_v143_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_safe_div(intexp, debt), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core143_2nd_v144_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_safe_div(intexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core144_2nd_v145_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_safe_div(taxexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core145_2nd_v146_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(intexp + taxexp, 4), 4), 12))
def cg_f015_interest_and_tax_drag_core146_2nd_v147_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_safe_div(intexp + taxexp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core147_2nd_v148_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_safe_div(debt, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core148_2nd_v149_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_log(intexp.abs() + 1.0), 4), 4), 12))
def cg_f015_interest_and_tax_drag_core149_2nd_v150_signal(intexp, taxexp, ncfo, debt):
    return _clean(_rank(_slope(_mean(_log(taxexp.abs() + 1.0), 4), 4), 12))