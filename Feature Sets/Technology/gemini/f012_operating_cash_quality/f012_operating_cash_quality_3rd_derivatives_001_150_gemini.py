import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f012_operating_cash_quality_core00_3rd_v001_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(ncfo, 4), 4))
def cg_f012_operating_cash_quality_core01_3rd_v002_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f012_operating_cash_quality_core02_3rd_v003_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(depamor, 4), 4))
def cg_f012_operating_cash_quality_core03_3rd_v004_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(sbcomp, 4), 4))
def cg_f012_operating_cash_quality_core04_3rd_v005_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_safe_div(ncfo, netinc), 4), 4))
def cg_f012_operating_cash_quality_core05_3rd_v006_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(ncfo - netinc, 4), 4))
def cg_f012_operating_cash_quality_core06_3rd_v007_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4))
def cg_f012_operating_cash_quality_core07_3rd_v008_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4))
def cg_f012_operating_cash_quality_core08_3rd_v009_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4))
def cg_f012_operating_cash_quality_core09_3rd_v010_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(netinc + depamor + sbcomp, 4), 4))
def cg_f012_operating_cash_quality_core10_3rd_v011_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(ncfo, 4), 8))
def cg_f012_operating_cash_quality_core11_3rd_v012_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f012_operating_cash_quality_core12_3rd_v013_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(depamor, 4), 8))
def cg_f012_operating_cash_quality_core13_3rd_v014_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(sbcomp, 4), 8))
def cg_f012_operating_cash_quality_core14_3rd_v015_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_safe_div(ncfo, netinc), 4), 8))
def cg_f012_operating_cash_quality_core15_3rd_v016_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(ncfo - netinc, 4), 8))
def cg_f012_operating_cash_quality_core16_3rd_v017_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_safe_div(ncfo, netinc + depamor), 4), 8))
def cg_f012_operating_cash_quality_core17_3rd_v018_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 8))
def cg_f012_operating_cash_quality_core18_3rd_v019_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 8))
def cg_f012_operating_cash_quality_core19_3rd_v020_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(netinc + depamor + sbcomp, 4), 8))
def cg_f012_operating_cash_quality_core20_3rd_v021_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(ncfo, 4), 4))
def cg_f012_operating_cash_quality_core21_3rd_v022_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(netinc, 4), 4))
def cg_f012_operating_cash_quality_core22_3rd_v023_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(depamor, 4), 4))
def cg_f012_operating_cash_quality_core23_3rd_v024_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(sbcomp, 4), 4))
def cg_f012_operating_cash_quality_core24_3rd_v025_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(_safe_div(ncfo, netinc), 4), 4))
def cg_f012_operating_cash_quality_core25_3rd_v026_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(ncfo - netinc, 4), 4))
def cg_f012_operating_cash_quality_core26_3rd_v027_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(_safe_div(ncfo, netinc + depamor), 4), 4))
def cg_f012_operating_cash_quality_core27_3rd_v028_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4))
def cg_f012_operating_cash_quality_core28_3rd_v029_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4))
def cg_f012_operating_cash_quality_core29_3rd_v030_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_slope(netinc + depamor + sbcomp, 4), 4))
def cg_f012_operating_cash_quality_core30_3rd_v031_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(ncfo, 4), 4), 8))
def cg_f012_operating_cash_quality_core31_3rd_v032_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f012_operating_cash_quality_core32_3rd_v033_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(depamor, 4), 4), 8))
def cg_f012_operating_cash_quality_core33_3rd_v034_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(sbcomp, 4), 4), 8))
def cg_f012_operating_cash_quality_core34_3rd_v035_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, netinc), 4), 4), 8))
def cg_f012_operating_cash_quality_core35_3rd_v036_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(ncfo - netinc, 4), 4), 8))
def cg_f012_operating_cash_quality_core36_3rd_v037_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4), 8))
def cg_f012_operating_cash_quality_core37_3rd_v038_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f012_operating_cash_quality_core38_3rd_v039_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f012_operating_cash_quality_core39_3rd_v040_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_diff(netinc + depamor + sbcomp, 4), 4), 8))
def cg_f012_operating_cash_quality_core40_3rd_v041_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(ncfo, 4), 8), 12))
def cg_f012_operating_cash_quality_core41_3rd_v042_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f012_operating_cash_quality_core42_3rd_v043_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(depamor, 4), 8), 12))
def cg_f012_operating_cash_quality_core43_3rd_v044_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f012_operating_cash_quality_core44_3rd_v045_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, netinc), 4), 8), 12))
def cg_f012_operating_cash_quality_core45_3rd_v046_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(ncfo - netinc, 4), 8), 12))
def cg_f012_operating_cash_quality_core46_3rd_v047_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, netinc + depamor), 4), 8), 12))
def cg_f012_operating_cash_quality_core47_3rd_v048_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f012_operating_cash_quality_core48_3rd_v049_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f012_operating_cash_quality_core49_3rd_v050_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(netinc + depamor + sbcomp, 4), 8), 12))
def cg_f012_operating_cash_quality_core50_3rd_v051_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(ncfo, 4), 4), 8))
def cg_f012_operating_cash_quality_core51_3rd_v052_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(netinc, 4), 4), 8))
def cg_f012_operating_cash_quality_core52_3rd_v053_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(depamor, 4), 4), 8))
def cg_f012_operating_cash_quality_core53_3rd_v054_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(sbcomp, 4), 4), 8))
def cg_f012_operating_cash_quality_core54_3rd_v055_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, netinc), 4), 4), 8))
def cg_f012_operating_cash_quality_core55_3rd_v056_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(ncfo - netinc, 4), 4), 8))
def cg_f012_operating_cash_quality_core56_3rd_v057_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, netinc + depamor), 4), 4), 8))
def cg_f012_operating_cash_quality_core57_3rd_v058_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f012_operating_cash_quality_core58_3rd_v059_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f012_operating_cash_quality_core59_3rd_v060_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_diff(_slope(netinc + depamor + sbcomp, 4), 4), 8))
def cg_f012_operating_cash_quality_core60_3rd_v061_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(ncfo, 4), 4), 12))
def cg_f012_operating_cash_quality_core61_3rd_v062_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f012_operating_cash_quality_core62_3rd_v063_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(depamor, 4), 4), 12))
def cg_f012_operating_cash_quality_core63_3rd_v064_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(sbcomp, 4), 4), 12))
def cg_f012_operating_cash_quality_core64_3rd_v065_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, netinc), 4), 4), 12))
def cg_f012_operating_cash_quality_core65_3rd_v066_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(ncfo - netinc, 4), 4), 12))
def cg_f012_operating_cash_quality_core66_3rd_v067_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4), 12))
def cg_f012_operating_cash_quality_core67_3rd_v068_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f012_operating_cash_quality_core68_3rd_v069_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f012_operating_cash_quality_core69_3rd_v070_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_diff(netinc + depamor + sbcomp, 4), 4), 12))
def cg_f012_operating_cash_quality_core70_3rd_v071_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(ncfo, 4), 8), 12))
def cg_f012_operating_cash_quality_core71_3rd_v072_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(netinc, 4), 8), 12))
def cg_f012_operating_cash_quality_core72_3rd_v073_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(depamor, 4), 8), 12))
def cg_f012_operating_cash_quality_core73_3rd_v074_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f012_operating_cash_quality_core74_3rd_v075_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, netinc), 4), 8), 12))
def cg_f012_operating_cash_quality_core75_3rd_v076_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(ncfo - netinc, 4), 8), 12))
def cg_f012_operating_cash_quality_core76_3rd_v077_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, netinc + depamor), 4), 8), 12))
def cg_f012_operating_cash_quality_core77_3rd_v078_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f012_operating_cash_quality_core78_3rd_v079_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 8), 12))
def cg_f012_operating_cash_quality_core79_3rd_v080_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_slope(_diff(netinc + depamor + sbcomp, 4), 8), 12))
def cg_f012_operating_cash_quality_core80_3rd_v081_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(ncfo, 4), 4), 12))
def cg_f012_operating_cash_quality_core81_3rd_v082_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(netinc, 4), 4), 12))
def cg_f012_operating_cash_quality_core82_3rd_v083_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(depamor, 4), 4), 12))
def cg_f012_operating_cash_quality_core83_3rd_v084_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(sbcomp, 4), 4), 12))
def cg_f012_operating_cash_quality_core84_3rd_v085_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, netinc), 4), 4), 12))
def cg_f012_operating_cash_quality_core85_3rd_v086_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(ncfo - netinc, 4), 4), 12))
def cg_f012_operating_cash_quality_core86_3rd_v087_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, netinc + depamor), 4), 4), 12))
def cg_f012_operating_cash_quality_core87_3rd_v088_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f012_operating_cash_quality_core88_3rd_v089_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f012_operating_cash_quality_core89_3rd_v090_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_rank(_diff(_slope(netinc + depamor + sbcomp, 4), 4), 12))
def cg_f012_operating_cash_quality_core90_3rd_v091_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(ncfo, 4), 4), 4))
def cg_f012_operating_cash_quality_core91_3rd_v092_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core92_3rd_v093_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(depamor, 4), 4), 4))
def cg_f012_operating_cash_quality_core93_3rd_v094_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core94_3rd_v095_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, netinc), 4), 4), 4))
def cg_f012_operating_cash_quality_core95_3rd_v096_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(ncfo - netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core96_3rd_v097_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4), 4))
def cg_f012_operating_cash_quality_core97_3rd_v098_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core98_3rd_v099_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core99_3rd_v100_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_diff(netinc + depamor + sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core100_3rd_v101_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(ncfo, 4), 8), 4))
def cg_f012_operating_cash_quality_core101_3rd_v102_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(netinc, 4), 8), 4))
def cg_f012_operating_cash_quality_core102_3rd_v103_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(depamor, 4), 8), 4))
def cg_f012_operating_cash_quality_core103_3rd_v104_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(sbcomp, 4), 8), 4))
def cg_f012_operating_cash_quality_core104_3rd_v105_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, netinc), 4), 8), 4))
def cg_f012_operating_cash_quality_core105_3rd_v106_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(ncfo - netinc, 4), 8), 4))
def cg_f012_operating_cash_quality_core106_3rd_v107_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, netinc + depamor), 4), 8), 4))
def cg_f012_operating_cash_quality_core107_3rd_v108_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f012_operating_cash_quality_core108_3rd_v109_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 8), 4))
def cg_f012_operating_cash_quality_core109_3rd_v110_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_slope(_diff(netinc + depamor + sbcomp, 4), 8), 4))
def cg_f012_operating_cash_quality_core110_3rd_v111_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(ncfo, 4), 4), 4))
def cg_f012_operating_cash_quality_core111_3rd_v112_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core112_3rd_v113_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(depamor, 4), 4), 4))
def cg_f012_operating_cash_quality_core113_3rd_v114_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core114_3rd_v115_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, netinc), 4), 4), 4))
def cg_f012_operating_cash_quality_core115_3rd_v116_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(ncfo - netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core116_3rd_v117_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, netinc + depamor), 4), 4), 4))
def cg_f012_operating_cash_quality_core117_3rd_v118_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core118_3rd_v119_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core119_3rd_v120_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_mean(_diff(_slope(netinc + depamor + sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core120_3rd_v121_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(ncfo, 4), 4), 4))
def cg_f012_operating_cash_quality_core121_3rd_v122_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core122_3rd_v123_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(depamor, 4), 4), 4))
def cg_f012_operating_cash_quality_core123_3rd_v124_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core124_3rd_v125_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, netinc), 4), 4), 4))
def cg_f012_operating_cash_quality_core125_3rd_v126_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(ncfo - netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core126_3rd_v127_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4), 4))
def cg_f012_operating_cash_quality_core127_3rd_v128_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core128_3rd_v129_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core129_3rd_v130_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_slope(_diff(_diff(netinc + depamor + sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core130_3rd_v131_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(ncfo, 4), 4), 4))
def cg_f012_operating_cash_quality_core131_3rd_v132_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core132_3rd_v133_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(depamor, 4), 4), 4))
def cg_f012_operating_cash_quality_core133_3rd_v134_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core134_3rd_v135_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, netinc), 4), 4), 4))
def cg_f012_operating_cash_quality_core135_3rd_v136_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(ncfo - netinc, 4), 4), 4))
def cg_f012_operating_cash_quality_core136_3rd_v137_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4), 4))
def cg_f012_operating_cash_quality_core137_3rd_v138_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core138_3rd_v139_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 4))
def cg_f012_operating_cash_quality_core139_3rd_v140_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_diff(_diff(_diff(netinc + depamor + sbcomp, 4), 4), 4))
def cg_f012_operating_cash_quality_core140_3rd_v141_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(ncfo, 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core141_3rd_v142_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core142_3rd_v143_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(depamor, 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core143_3rd_v144_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(sbcomp, 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core144_3rd_v145_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, netinc), 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core145_3rd_v146_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(ncfo - netinc, 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core146_3rd_v147_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, netinc + depamor), 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core147_3rd_v148_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core148_3rd_v149_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(_safe_div(depamor, ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f012_operating_cash_quality_core149_3rd_v150_signal(ncfo, netinc, depamor, sbcomp):
    return _clean(_z(_slope(_diff(_diff(netinc + depamor + sbcomp, 4), 4), 4), 8))