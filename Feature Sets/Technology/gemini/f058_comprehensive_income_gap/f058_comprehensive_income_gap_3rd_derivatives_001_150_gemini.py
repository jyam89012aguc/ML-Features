import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f058_comprehensive_income_gap_core00_3rd_v001_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(consolinc, 4), 4))
def cg_f058_comprehensive_income_gap_core01_3rd_v002_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core02_3rd_v003_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(equity, 4), 4))
def cg_f058_comprehensive_income_gap_core03_3rd_v004_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(consolinc - netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core04_3rd_v005_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core05_3rd_v006_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core06_3rd_v007_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core07_3rd_v008_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core08_3rd_v009_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core09_3rd_v010_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_pct_change(consolinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core10_3rd_v011_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(consolinc, 4), 8))
def cg_f058_comprehensive_income_gap_core11_3rd_v012_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f058_comprehensive_income_gap_core12_3rd_v013_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(equity, 4), 8))
def cg_f058_comprehensive_income_gap_core13_3rd_v014_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(consolinc - netinc, 4), 8))
def cg_f058_comprehensive_income_gap_core14_3rd_v015_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 8))
def cg_f058_comprehensive_income_gap_core15_3rd_v016_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 8))
def cg_f058_comprehensive_income_gap_core16_3rd_v017_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8))
def cg_f058_comprehensive_income_gap_core17_3rd_v018_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 8))
def cg_f058_comprehensive_income_gap_core18_3rd_v019_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(consolinc - netinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core19_3rd_v020_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_pct_change(consolinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core20_3rd_v021_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(consolinc, 4), 4))
def cg_f058_comprehensive_income_gap_core21_3rd_v022_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core22_3rd_v023_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(equity, 4), 4))
def cg_f058_comprehensive_income_gap_core23_3rd_v024_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(consolinc - netinc, 4), 4))
def cg_f058_comprehensive_income_gap_core24_3rd_v025_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core25_3rd_v026_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core26_3rd_v027_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core27_3rd_v028_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(_safe_div(consolinc, equity.abs() + 1.0), 4), 4))
def cg_f058_comprehensive_income_gap_core28_3rd_v029_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(_diff(consolinc - netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core29_3rd_v030_signal(consolinc, netinc, equity):
    return _clean(_diff(_slope(_pct_change(consolinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core30_3rd_v031_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(consolinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core31_3rd_v032_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core32_3rd_v033_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(equity, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core33_3rd_v034_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(consolinc - netinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core34_3rd_v035_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core35_3rd_v036_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core36_3rd_v037_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core37_3rd_v038_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core38_3rd_v039_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core39_3rd_v040_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_diff(_pct_change(consolinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core40_3rd_v041_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(consolinc, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core41_3rd_v042_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core42_3rd_v043_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(equity, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core43_3rd_v044_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(consolinc - netinc, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core44_3rd_v045_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core45_3rd_v046_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core46_3rd_v047_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core47_3rd_v048_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core48_3rd_v049_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(consolinc - netinc, 4), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core49_3rd_v050_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_pct_change(consolinc, 4), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core50_3rd_v051_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(consolinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core51_3rd_v052_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(netinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core52_3rd_v053_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(equity, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core53_3rd_v054_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(consolinc - netinc, 4), 4), 8))
def cg_f058_comprehensive_income_gap_core54_3rd_v055_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core55_3rd_v056_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core56_3rd_v057_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core57_3rd_v058_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core58_3rd_v059_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(_diff(consolinc - netinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core59_3rd_v060_signal(consolinc, netinc, equity):
    return _clean(_z(_diff(_slope(_pct_change(consolinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core60_3rd_v061_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(consolinc, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core61_3rd_v062_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core62_3rd_v063_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(equity, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core63_3rd_v064_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(consolinc - netinc, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core64_3rd_v065_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core65_3rd_v066_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core66_3rd_v067_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core67_3rd_v068_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core68_3rd_v069_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core69_3rd_v070_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_diff(_pct_change(consolinc, 4), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core70_3rd_v071_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(consolinc, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core71_3rd_v072_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(netinc, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core72_3rd_v073_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(equity, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core73_3rd_v074_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(consolinc - netinc, 4), 8), 12))
def cg_f058_comprehensive_income_gap_core74_3rd_v075_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core75_3rd_v076_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core76_3rd_v077_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core77_3rd_v078_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core78_3rd_v079_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(_diff(consolinc - netinc, 4), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core79_3rd_v080_signal(consolinc, netinc, equity):
    return _clean(_rank(_slope(_diff(_pct_change(consolinc, 4), 4), 8), 12))
def cg_f058_comprehensive_income_gap_core80_3rd_v081_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(consolinc, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core81_3rd_v082_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(netinc, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core82_3rd_v083_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(equity, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core83_3rd_v084_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(consolinc - netinc, 4), 4), 12))
def cg_f058_comprehensive_income_gap_core84_3rd_v085_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core85_3rd_v086_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core86_3rd_v087_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core87_3rd_v088_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core88_3rd_v089_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(_diff(consolinc - netinc, 4), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core89_3rd_v090_signal(consolinc, netinc, equity):
    return _clean(_rank(_diff(_slope(_pct_change(consolinc, 4), 4), 4), 12))
def cg_f058_comprehensive_income_gap_core90_3rd_v091_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(consolinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core91_3rd_v092_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core92_3rd_v093_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(equity, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core93_3rd_v094_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(consolinc - netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core94_3rd_v095_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core95_3rd_v096_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core96_3rd_v097_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core97_3rd_v098_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core98_3rd_v099_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core99_3rd_v100_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_diff(_pct_change(consolinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core100_3rd_v101_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(consolinc, 4), 8), 4))
def cg_f058_comprehensive_income_gap_core101_3rd_v102_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(netinc, 4), 8), 4))
def cg_f058_comprehensive_income_gap_core102_3rd_v103_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(equity, 4), 8), 4))
def cg_f058_comprehensive_income_gap_core103_3rd_v104_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(consolinc - netinc, 4), 8), 4))
def cg_f058_comprehensive_income_gap_core104_3rd_v105_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 8), 4))
def cg_f058_comprehensive_income_gap_core105_3rd_v106_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 8), 4))
def cg_f058_comprehensive_income_gap_core106_3rd_v107_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 4))
def cg_f058_comprehensive_income_gap_core107_3rd_v108_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 8), 4))
def cg_f058_comprehensive_income_gap_core108_3rd_v109_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(_diff(consolinc - netinc, 4), 4), 8), 4))
def cg_f058_comprehensive_income_gap_core109_3rd_v110_signal(consolinc, netinc, equity):
    return _clean(_mean(_slope(_diff(_pct_change(consolinc, 4), 4), 8), 4))
def cg_f058_comprehensive_income_gap_core110_3rd_v111_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(consolinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core111_3rd_v112_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core112_3rd_v113_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(equity, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core113_3rd_v114_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(consolinc - netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core114_3rd_v115_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core115_3rd_v116_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core116_3rd_v117_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core117_3rd_v118_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core118_3rd_v119_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(_diff(consolinc - netinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core119_3rd_v120_signal(consolinc, netinc, equity):
    return _clean(_mean(_diff(_slope(_pct_change(consolinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core120_3rd_v121_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(consolinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core121_3rd_v122_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core122_3rd_v123_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(equity, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core123_3rd_v124_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(consolinc - netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core124_3rd_v125_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core125_3rd_v126_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core126_3rd_v127_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core127_3rd_v128_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core128_3rd_v129_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core129_3rd_v130_signal(consolinc, netinc, equity):
    return _clean(_slope(_diff(_diff(_pct_change(consolinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core130_3rd_v131_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(consolinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core131_3rd_v132_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core132_3rd_v133_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(equity, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core133_3rd_v134_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4))
def cg_f058_comprehensive_income_gap_core134_3rd_v135_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core135_3rd_v136_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core136_3rd_v137_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core137_3rd_v138_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core138_3rd_v139_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core139_3rd_v140_signal(consolinc, netinc, equity):
    return _clean(_diff(_diff(_diff(_pct_change(consolinc, 4), 4), 4), 4))
def cg_f058_comprehensive_income_gap_core140_3rd_v141_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(consolinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core141_3rd_v142_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core142_3rd_v143_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(equity, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core143_3rd_v144_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(consolinc - netinc, 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core144_3rd_v145_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(consolinc, netinc.abs() + 1.0), 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core145_3rd_v146_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(consolinc - netinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core146_3rd_v147_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core147_3rd_v148_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(consolinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core148_3rd_v149_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_diff(consolinc - netinc, 4), 4), 4), 4), 8))
def cg_f058_comprehensive_income_gap_core149_3rd_v150_signal(consolinc, netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_pct_change(consolinc, 4), 4), 4), 4), 8))