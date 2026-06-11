import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f036_sbc_dilution_pressure_core00_3rd_v001_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(sbcomp, 4), 4))
def cg_f036_sbc_dilution_pressure_core01_3rd_v002_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core02_3rd_v003_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core03_3rd_v004_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core04_3rd_v005_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_slope(sbcomp, 8), 4), 4))
def cg_f036_sbc_dilution_pressure_core05_3rd_v006_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_z(sbcomp, 12), 4), 4))
def cg_f036_sbc_dilution_pressure_core06_3rd_v007_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_pct_change(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core07_3rd_v008_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_mean(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core08_3rd_v009_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core09_3rd_v010_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core10_3rd_v011_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(sbcomp, 4), 8))
def cg_f036_sbc_dilution_pressure_core11_3rd_v012_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 8))
def cg_f036_sbc_dilution_pressure_core12_3rd_v013_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 8))
def cg_f036_sbc_dilution_pressure_core13_3rd_v014_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(sbcomp, 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core14_3rd_v015_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_slope(sbcomp, 8), 4), 8))
def cg_f036_sbc_dilution_pressure_core15_3rd_v016_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_z(sbcomp, 12), 4), 8))
def cg_f036_sbc_dilution_pressure_core16_3rd_v017_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_pct_change(sbcomp, 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core17_3rd_v018_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_mean(sbcomp, 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core18_3rd_v019_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8))
def cg_f036_sbc_dilution_pressure_core19_3rd_v020_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 8))
def cg_f036_sbc_dilution_pressure_core20_3rd_v021_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(sbcomp, 4), 4))
def cg_f036_sbc_dilution_pressure_core21_3rd_v022_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core22_3rd_v023_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core23_3rd_v024_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_diff(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core24_3rd_v025_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_slope(sbcomp, 8), 4), 4))
def cg_f036_sbc_dilution_pressure_core25_3rd_v026_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_z(sbcomp, 12), 4), 4))
def cg_f036_sbc_dilution_pressure_core26_3rd_v027_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_pct_change(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core27_3rd_v028_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_mean(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core28_3rd_v029_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core29_3rd_v030_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_slope(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4))
def cg_f036_sbc_dilution_pressure_core30_3rd_v031_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(sbcomp, 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core31_3rd_v032_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core32_3rd_v033_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core33_3rd_v034_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_diff(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core34_3rd_v035_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_slope(sbcomp, 8), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core35_3rd_v036_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_z(sbcomp, 12), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core36_3rd_v037_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_pct_change(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core37_3rd_v038_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_mean(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core38_3rd_v039_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core39_3rd_v040_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core40_3rd_v041_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core41_3rd_v042_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core42_3rd_v043_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core43_3rd_v044_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(sbcomp, 4), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core44_3rd_v045_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_slope(sbcomp, 8), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core45_3rd_v046_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_z(sbcomp, 12), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core46_3rd_v047_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_pct_change(sbcomp, 4), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core47_3rd_v048_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_mean(sbcomp, 4), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core48_3rd_v049_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core49_3rd_v050_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core50_3rd_v051_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(sbcomp, 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core51_3rd_v052_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core52_3rd_v053_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core53_3rd_v054_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_diff(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core54_3rd_v055_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_slope(sbcomp, 8), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core55_3rd_v056_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_z(sbcomp, 12), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core56_3rd_v057_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_pct_change(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core57_3rd_v058_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_mean(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core58_3rd_v059_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core59_3rd_v060_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core60_3rd_v061_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(sbcomp, 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core61_3rd_v062_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core62_3rd_v063_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core63_3rd_v064_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_diff(sbcomp, 4), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core64_3rd_v065_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_slope(sbcomp, 8), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core65_3rd_v066_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_z(sbcomp, 12), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core66_3rd_v067_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_pct_change(sbcomp, 4), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core67_3rd_v068_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_mean(sbcomp, 4), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core68_3rd_v069_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core69_3rd_v070_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core70_3rd_v071_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core71_3rd_v072_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core72_3rd_v073_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core73_3rd_v074_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_diff(sbcomp, 4), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core74_3rd_v075_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_slope(sbcomp, 8), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core75_3rd_v076_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_z(sbcomp, 12), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core76_3rd_v077_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_pct_change(sbcomp, 4), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core77_3rd_v078_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_mean(sbcomp, 4), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core78_3rd_v079_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core79_3rd_v080_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 8), 12))
def cg_f036_sbc_dilution_pressure_core80_3rd_v081_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(sbcomp, 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core81_3rd_v082_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core82_3rd_v083_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core83_3rd_v084_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_diff(sbcomp, 4), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core84_3rd_v085_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_slope(sbcomp, 8), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core85_3rd_v086_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_z(sbcomp, 12), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core86_3rd_v087_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_pct_change(sbcomp, 4), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core87_3rd_v088_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_mean(sbcomp, 4), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core88_3rd_v089_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core89_3rd_v090_signal(sbcomp, sharesbas, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 12))
def cg_f036_sbc_dilution_pressure_core90_3rd_v091_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core91_3rd_v092_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core92_3rd_v093_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core93_3rd_v094_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_diff(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core94_3rd_v095_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_slope(sbcomp, 8), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core95_3rd_v096_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_z(sbcomp, 12), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core96_3rd_v097_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_pct_change(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core97_3rd_v098_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_mean(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core98_3rd_v099_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core99_3rd_v100_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core100_3rd_v101_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(sbcomp, 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core101_3rd_v102_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core102_3rd_v103_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core103_3rd_v104_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_diff(sbcomp, 4), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core104_3rd_v105_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_slope(sbcomp, 8), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core105_3rd_v106_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_z(sbcomp, 12), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core106_3rd_v107_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_pct_change(sbcomp, 4), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core107_3rd_v108_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_mean(sbcomp, 4), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core108_3rd_v109_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core109_3rd_v110_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 8), 4))
def cg_f036_sbc_dilution_pressure_core110_3rd_v111_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core111_3rd_v112_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core112_3rd_v113_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core113_3rd_v114_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_diff(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core114_3rd_v115_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_slope(sbcomp, 8), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core115_3rd_v116_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_z(sbcomp, 12), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core116_3rd_v117_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_pct_change(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core117_3rd_v118_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_mean(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core118_3rd_v119_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core119_3rd_v120_signal(sbcomp, sharesbas, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core120_3rd_v121_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core121_3rd_v122_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core122_3rd_v123_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core123_3rd_v124_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_diff(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core124_3rd_v125_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_slope(sbcomp, 8), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core125_3rd_v126_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_z(sbcomp, 12), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core126_3rd_v127_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_pct_change(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core127_3rd_v128_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_mean(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core128_3rd_v129_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core129_3rd_v130_signal(sbcomp, sharesbas, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core130_3rd_v131_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core131_3rd_v132_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core132_3rd_v133_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core133_3rd_v134_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_diff(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core134_3rd_v135_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_slope(sbcomp, 8), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core135_3rd_v136_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_z(sbcomp, 12), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core136_3rd_v137_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_pct_change(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core137_3rd_v138_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_mean(sbcomp, 4), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core138_3rd_v139_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core139_3rd_v140_signal(sbcomp, sharesbas, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 4))
def cg_f036_sbc_dilution_pressure_core140_3rd_v141_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(sbcomp, 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core141_3rd_v142_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, marketcap.abs() + 1.0), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core142_3rd_v143_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, sharesbas.abs() + 1.0), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core143_3rd_v144_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_diff(sbcomp, 4), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core144_3rd_v145_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_slope(sbcomp, 8), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core145_3rd_v146_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_z(sbcomp, 12), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core146_3rd_v147_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_pct_change(sbcomp, 4), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core147_3rd_v148_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_mean(sbcomp, 4), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core148_3rd_v149_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4), 8))
def cg_f036_sbc_dilution_pressure_core149_3rd_v150_signal(sbcomp, sharesbas, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, marketcap / sharesbas + 1.0), 4), 4), 4), 8))