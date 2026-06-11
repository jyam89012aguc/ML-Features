import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f065_return_on_invested_capital_core00_3rd_v001_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(roic, 4), 4))
def cg_f065_return_on_invested_capital_core01_3rd_v002_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(invcap, 4), 4))
def cg_f065_return_on_invested_capital_core02_3rd_v003_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(invcapavg, 4), 4))
def cg_f065_return_on_invested_capital_core03_3rd_v004_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4))
def cg_f065_return_on_invested_capital_core04_3rd_v005_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core05_3rd_v006_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_pct_change(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core06_3rd_v007_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(invcapavg, 4), 4), 4))
def cg_f065_return_on_invested_capital_core07_3rd_v008_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_z(roic, 8), 4), 4))
def cg_f065_return_on_invested_capital_core08_3rd_v009_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_mean(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core09_3rd_v010_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4))
def cg_f065_return_on_invested_capital_core10_3rd_v011_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(roic, 4), 8))
def cg_f065_return_on_invested_capital_core11_3rd_v012_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(invcap, 4), 8))
def cg_f065_return_on_invested_capital_core12_3rd_v013_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(invcapavg, 4), 8))
def cg_f065_return_on_invested_capital_core13_3rd_v014_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 8))
def cg_f065_return_on_invested_capital_core14_3rd_v015_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(roic, 4), 4), 8))
def cg_f065_return_on_invested_capital_core15_3rd_v016_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_pct_change(roic, 4), 4), 8))
def cg_f065_return_on_invested_capital_core16_3rd_v017_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(invcapavg, 4), 4), 8))
def cg_f065_return_on_invested_capital_core17_3rd_v018_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_z(roic, 8), 4), 8))
def cg_f065_return_on_invested_capital_core18_3rd_v019_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_mean(roic, 4), 4), 8))
def cg_f065_return_on_invested_capital_core19_3rd_v020_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 8))
def cg_f065_return_on_invested_capital_core20_3rd_v021_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(roic, 4), 4))
def cg_f065_return_on_invested_capital_core21_3rd_v022_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(invcap, 4), 4))
def cg_f065_return_on_invested_capital_core22_3rd_v023_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(invcapavg, 4), 4))
def cg_f065_return_on_invested_capital_core23_3rd_v024_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4))
def cg_f065_return_on_invested_capital_core24_3rd_v025_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_diff(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core25_3rd_v026_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_pct_change(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core26_3rd_v027_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_diff(invcapavg, 4), 4), 4))
def cg_f065_return_on_invested_capital_core27_3rd_v028_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_z(roic, 8), 4), 4))
def cg_f065_return_on_invested_capital_core28_3rd_v029_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_mean(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core29_3rd_v030_signal(roic, invcap, invcapavg):
    return _clean(_diff(_slope(_safe_div(roic, invcap.abs() + 1.0), 4), 4))
def cg_f065_return_on_invested_capital_core30_3rd_v031_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(roic, 4), 4), 8))
def cg_f065_return_on_invested_capital_core31_3rd_v032_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(invcap, 4), 4), 8))
def cg_f065_return_on_invested_capital_core32_3rd_v033_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(invcapavg, 4), 4), 8))
def cg_f065_return_on_invested_capital_core33_3rd_v034_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 8))
def cg_f065_return_on_invested_capital_core34_3rd_v035_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_diff(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core35_3rd_v036_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_pct_change(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core36_3rd_v037_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_diff(invcapavg, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core37_3rd_v038_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_z(roic, 8), 4), 4), 8))
def cg_f065_return_on_invested_capital_core38_3rd_v039_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_mean(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core39_3rd_v040_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 8))
def cg_f065_return_on_invested_capital_core40_3rd_v041_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(roic, 4), 8), 12))
def cg_f065_return_on_invested_capital_core41_3rd_v042_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(invcap, 4), 8), 12))
def cg_f065_return_on_invested_capital_core42_3rd_v043_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(invcapavg, 4), 8), 12))
def cg_f065_return_on_invested_capital_core43_3rd_v044_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 8), 12))
def cg_f065_return_on_invested_capital_core44_3rd_v045_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(roic, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core45_3rd_v046_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_pct_change(roic, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core46_3rd_v047_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(invcapavg, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core47_3rd_v048_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_z(roic, 8), 4), 8), 12))
def cg_f065_return_on_invested_capital_core48_3rd_v049_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_mean(roic, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core49_3rd_v050_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 8), 12))
def cg_f065_return_on_invested_capital_core50_3rd_v051_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(roic, 4), 4), 8))
def cg_f065_return_on_invested_capital_core51_3rd_v052_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(invcap, 4), 4), 8))
def cg_f065_return_on_invested_capital_core52_3rd_v053_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(invcapavg, 4), 4), 8))
def cg_f065_return_on_invested_capital_core53_3rd_v054_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 8))
def cg_f065_return_on_invested_capital_core54_3rd_v055_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_diff(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core55_3rd_v056_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_pct_change(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core56_3rd_v057_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_diff(invcapavg, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core57_3rd_v058_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_z(roic, 8), 4), 4), 8))
def cg_f065_return_on_invested_capital_core58_3rd_v059_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_mean(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core59_3rd_v060_signal(roic, invcap, invcapavg):
    return _clean(_z(_diff(_slope(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 8))
def cg_f065_return_on_invested_capital_core60_3rd_v061_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(roic, 4), 4), 12))
def cg_f065_return_on_invested_capital_core61_3rd_v062_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(invcap, 4), 4), 12))
def cg_f065_return_on_invested_capital_core62_3rd_v063_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(invcapavg, 4), 4), 12))
def cg_f065_return_on_invested_capital_core63_3rd_v064_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 12))
def cg_f065_return_on_invested_capital_core64_3rd_v065_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_diff(roic, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core65_3rd_v066_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_pct_change(roic, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core66_3rd_v067_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_diff(invcapavg, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core67_3rd_v068_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_z(roic, 8), 4), 4), 12))
def cg_f065_return_on_invested_capital_core68_3rd_v069_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_mean(roic, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core69_3rd_v070_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 12))
def cg_f065_return_on_invested_capital_core70_3rd_v071_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(roic, 4), 8), 12))
def cg_f065_return_on_invested_capital_core71_3rd_v072_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(invcap, 4), 8), 12))
def cg_f065_return_on_invested_capital_core72_3rd_v073_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(invcapavg, 4), 8), 12))
def cg_f065_return_on_invested_capital_core73_3rd_v074_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 8), 12))
def cg_f065_return_on_invested_capital_core74_3rd_v075_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_diff(roic, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core75_3rd_v076_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_pct_change(roic, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core76_3rd_v077_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_diff(invcapavg, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core77_3rd_v078_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_z(roic, 8), 4), 8), 12))
def cg_f065_return_on_invested_capital_core78_3rd_v079_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_mean(roic, 4), 4), 8), 12))
def cg_f065_return_on_invested_capital_core79_3rd_v080_signal(roic, invcap, invcapavg):
    return _clean(_rank(_slope(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 8), 12))
def cg_f065_return_on_invested_capital_core80_3rd_v081_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(roic, 4), 4), 12))
def cg_f065_return_on_invested_capital_core81_3rd_v082_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(invcap, 4), 4), 12))
def cg_f065_return_on_invested_capital_core82_3rd_v083_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(invcapavg, 4), 4), 12))
def cg_f065_return_on_invested_capital_core83_3rd_v084_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 12))
def cg_f065_return_on_invested_capital_core84_3rd_v085_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_diff(roic, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core85_3rd_v086_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_pct_change(roic, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core86_3rd_v087_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_diff(invcapavg, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core87_3rd_v088_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_z(roic, 8), 4), 4), 12))
def cg_f065_return_on_invested_capital_core88_3rd_v089_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_mean(roic, 4), 4), 4), 12))
def cg_f065_return_on_invested_capital_core89_3rd_v090_signal(roic, invcap, invcapavg):
    return _clean(_rank(_diff(_slope(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 12))
def cg_f065_return_on_invested_capital_core90_3rd_v091_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core91_3rd_v092_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(invcap, 4), 4), 4))
def cg_f065_return_on_invested_capital_core92_3rd_v093_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(invcapavg, 4), 4), 4))
def cg_f065_return_on_invested_capital_core93_3rd_v094_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core94_3rd_v095_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_diff(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core95_3rd_v096_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_pct_change(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core96_3rd_v097_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_diff(invcapavg, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core97_3rd_v098_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_z(roic, 8), 4), 4), 4))
def cg_f065_return_on_invested_capital_core98_3rd_v099_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_mean(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core99_3rd_v100_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core100_3rd_v101_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(roic, 4), 8), 4))
def cg_f065_return_on_invested_capital_core101_3rd_v102_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(invcap, 4), 8), 4))
def cg_f065_return_on_invested_capital_core102_3rd_v103_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(invcapavg, 4), 8), 4))
def cg_f065_return_on_invested_capital_core103_3rd_v104_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 8), 4))
def cg_f065_return_on_invested_capital_core104_3rd_v105_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_diff(roic, 4), 4), 8), 4))
def cg_f065_return_on_invested_capital_core105_3rd_v106_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_pct_change(roic, 4), 4), 8), 4))
def cg_f065_return_on_invested_capital_core106_3rd_v107_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_diff(invcapavg, 4), 4), 8), 4))
def cg_f065_return_on_invested_capital_core107_3rd_v108_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_z(roic, 8), 4), 8), 4))
def cg_f065_return_on_invested_capital_core108_3rd_v109_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_mean(roic, 4), 4), 8), 4))
def cg_f065_return_on_invested_capital_core109_3rd_v110_signal(roic, invcap, invcapavg):
    return _clean(_mean(_slope(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 8), 4))
def cg_f065_return_on_invested_capital_core110_3rd_v111_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core111_3rd_v112_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(invcap, 4), 4), 4))
def cg_f065_return_on_invested_capital_core112_3rd_v113_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(invcapavg, 4), 4), 4))
def cg_f065_return_on_invested_capital_core113_3rd_v114_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core114_3rd_v115_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_diff(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core115_3rd_v116_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_pct_change(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core116_3rd_v117_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_diff(invcapavg, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core117_3rd_v118_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_z(roic, 8), 4), 4), 4))
def cg_f065_return_on_invested_capital_core118_3rd_v119_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_mean(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core119_3rd_v120_signal(roic, invcap, invcapavg):
    return _clean(_mean(_diff(_slope(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core120_3rd_v121_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core121_3rd_v122_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(invcap, 4), 4), 4))
def cg_f065_return_on_invested_capital_core122_3rd_v123_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(invcapavg, 4), 4), 4))
def cg_f065_return_on_invested_capital_core123_3rd_v124_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core124_3rd_v125_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_diff(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core125_3rd_v126_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_pct_change(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core126_3rd_v127_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_diff(invcapavg, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core127_3rd_v128_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_z(roic, 8), 4), 4), 4))
def cg_f065_return_on_invested_capital_core128_3rd_v129_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_mean(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core129_3rd_v130_signal(roic, invcap, invcapavg):
    return _clean(_slope(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core130_3rd_v131_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(roic, 4), 4), 4))
def cg_f065_return_on_invested_capital_core131_3rd_v132_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(invcap, 4), 4), 4))
def cg_f065_return_on_invested_capital_core132_3rd_v133_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(invcapavg, 4), 4), 4))
def cg_f065_return_on_invested_capital_core133_3rd_v134_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core134_3rd_v135_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_diff(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core135_3rd_v136_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_pct_change(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core136_3rd_v137_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_diff(invcapavg, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core137_3rd_v138_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_z(roic, 8), 4), 4), 4))
def cg_f065_return_on_invested_capital_core138_3rd_v139_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_mean(roic, 4), 4), 4), 4))
def cg_f065_return_on_invested_capital_core139_3rd_v140_signal(roic, invcap, invcapavg):
    return _clean(_diff(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 4))
def cg_f065_return_on_invested_capital_core140_3rd_v141_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(roic, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core141_3rd_v142_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(invcap, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core142_3rd_v143_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(invcapavg, 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core143_3rd_v144_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_safe_div(roic, invcapavg.abs() + 1.0), 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core144_3rd_v145_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_diff(roic, 4), 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core145_3rd_v146_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_pct_change(roic, 4), 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core146_3rd_v147_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_diff(invcapavg, 4), 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core147_3rd_v148_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_z(roic, 8), 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core148_3rd_v149_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_mean(roic, 4), 4), 4), 4), 8))
def cg_f065_return_on_invested_capital_core149_3rd_v150_signal(roic, invcap, invcapavg):
    return _clean(_z(_slope(_diff(_diff(_safe_div(roic, invcap.abs() + 1.0), 4), 4), 4), 8))