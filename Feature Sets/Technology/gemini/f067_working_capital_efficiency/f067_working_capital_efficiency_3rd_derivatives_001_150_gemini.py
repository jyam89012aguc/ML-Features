import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f067_working_capital_efficiency_core00_3rd_v001_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core01_3rd_v002_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f067_working_capital_efficiency_core02_3rd_v003_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(assets, 4), 4))
def cg_f067_working_capital_efficiency_core03_3rd_v004_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core04_3rd_v005_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_safe_div(workingcapital, assets), 4), 4))
def cg_f067_working_capital_efficiency_core05_3rd_v006_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core06_3rd_v007_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_pct_change(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core07_3rd_v008_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4))
def cg_f067_working_capital_efficiency_core08_3rd_v009_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core09_3rd_v010_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4))
def cg_f067_working_capital_efficiency_core10_3rd_v011_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(workingcapital, 4), 8))
def cg_f067_working_capital_efficiency_core11_3rd_v012_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f067_working_capital_efficiency_core12_3rd_v013_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(assets, 4), 8))
def cg_f067_working_capital_efficiency_core13_3rd_v014_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_safe_div(workingcapital, revenue), 4), 8))
def cg_f067_working_capital_efficiency_core14_3rd_v015_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_safe_div(workingcapital, assets), 4), 8))
def cg_f067_working_capital_efficiency_core15_3rd_v016_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core16_3rd_v017_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_pct_change(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core17_3rd_v018_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 8))
def cg_f067_working_capital_efficiency_core18_3rd_v019_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core19_3rd_v020_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 8))
def cg_f067_working_capital_efficiency_core20_3rd_v021_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core21_3rd_v022_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(revenue, 4), 4))
def cg_f067_working_capital_efficiency_core22_3rd_v023_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(assets, 4), 4))
def cg_f067_working_capital_efficiency_core23_3rd_v024_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core24_3rd_v025_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_safe_div(workingcapital, assets), 4), 4))
def cg_f067_working_capital_efficiency_core25_3rd_v026_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core26_3rd_v027_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_pct_change(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core27_3rd_v028_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 4))
def cg_f067_working_capital_efficiency_core28_3rd_v029_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core29_3rd_v030_signal(workingcapital, revenue, assets):
    return _clean(_diff(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 4))
def cg_f067_working_capital_efficiency_core30_3rd_v031_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core31_3rd_v032_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f067_working_capital_efficiency_core32_3rd_v033_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(assets, 4), 4), 8))
def cg_f067_working_capital_efficiency_core33_3rd_v034_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core34_3rd_v035_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_safe_div(workingcapital, assets), 4), 4), 8))
def cg_f067_working_capital_efficiency_core35_3rd_v036_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_diff(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core36_3rd_v037_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_pct_change(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core37_3rd_v038_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 8))
def cg_f067_working_capital_efficiency_core38_3rd_v039_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core39_3rd_v040_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core40_3rd_v041_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(workingcapital, 4), 8), 12))
def cg_f067_working_capital_efficiency_core41_3rd_v042_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f067_working_capital_efficiency_core42_3rd_v043_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(assets, 4), 8), 12))
def cg_f067_working_capital_efficiency_core43_3rd_v044_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_safe_div(workingcapital, revenue), 4), 8), 12))
def cg_f067_working_capital_efficiency_core44_3rd_v045_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_safe_div(workingcapital, assets), 4), 8), 12))
def cg_f067_working_capital_efficiency_core45_3rd_v046_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(workingcapital, 4), 4), 8), 12))
def cg_f067_working_capital_efficiency_core46_3rd_v047_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_pct_change(workingcapital, 4), 4), 8), 12))
def cg_f067_working_capital_efficiency_core47_3rd_v048_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 8), 12))
def cg_f067_working_capital_efficiency_core48_3rd_v049_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 8), 12))
def cg_f067_working_capital_efficiency_core49_3rd_v050_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 8), 12))
def cg_f067_working_capital_efficiency_core50_3rd_v051_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core51_3rd_v052_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(revenue, 4), 4), 8))
def cg_f067_working_capital_efficiency_core52_3rd_v053_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(assets, 4), 4), 8))
def cg_f067_working_capital_efficiency_core53_3rd_v054_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_safe_div(workingcapital, revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core54_3rd_v055_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_safe_div(workingcapital, assets), 4), 4), 8))
def cg_f067_working_capital_efficiency_core55_3rd_v056_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_diff(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core56_3rd_v057_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_pct_change(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core57_3rd_v058_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 8))
def cg_f067_working_capital_efficiency_core58_3rd_v059_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core59_3rd_v060_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core60_3rd_v061_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core61_3rd_v062_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f067_working_capital_efficiency_core62_3rd_v063_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(assets, 4), 4), 12))
def cg_f067_working_capital_efficiency_core63_3rd_v064_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core64_3rd_v065_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_safe_div(workingcapital, assets), 4), 4), 12))
def cg_f067_working_capital_efficiency_core65_3rd_v066_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_diff(workingcapital, 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core66_3rd_v067_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_pct_change(workingcapital, 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core67_3rd_v068_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 12))
def cg_f067_working_capital_efficiency_core68_3rd_v069_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core69_3rd_v070_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core70_3rd_v071_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(workingcapital, 4), 8), 12))
def cg_f067_working_capital_efficiency_core71_3rd_v072_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(revenue, 4), 8), 12))
def cg_f067_working_capital_efficiency_core72_3rd_v073_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(assets, 4), 8), 12))
def cg_f067_working_capital_efficiency_core73_3rd_v074_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_safe_div(workingcapital, revenue), 4), 8), 12))
def cg_f067_working_capital_efficiency_core74_3rd_v075_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_safe_div(workingcapital, assets), 4), 8), 12))
def cg_f067_working_capital_efficiency_core75_3rd_v076_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_diff(workingcapital, 4), 4), 8), 12))
def cg_f067_working_capital_efficiency_core76_3rd_v077_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_pct_change(workingcapital, 4), 4), 8), 12))
def cg_f067_working_capital_efficiency_core77_3rd_v078_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 8), 12))
def cg_f067_working_capital_efficiency_core78_3rd_v079_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 8), 12))
def cg_f067_working_capital_efficiency_core79_3rd_v080_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 8), 12))
def cg_f067_working_capital_efficiency_core80_3rd_v081_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core81_3rd_v082_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(revenue, 4), 4), 12))
def cg_f067_working_capital_efficiency_core82_3rd_v083_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(assets, 4), 4), 12))
def cg_f067_working_capital_efficiency_core83_3rd_v084_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_safe_div(workingcapital, revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core84_3rd_v085_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_safe_div(workingcapital, assets), 4), 4), 12))
def cg_f067_working_capital_efficiency_core85_3rd_v086_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_diff(workingcapital, 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core86_3rd_v087_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_pct_change(workingcapital, 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core87_3rd_v088_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 12))
def cg_f067_working_capital_efficiency_core88_3rd_v089_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core89_3rd_v090_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core90_3rd_v091_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core91_3rd_v092_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f067_working_capital_efficiency_core92_3rd_v093_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(assets, 4), 4), 4))
def cg_f067_working_capital_efficiency_core93_3rd_v094_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core94_3rd_v095_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_safe_div(workingcapital, assets), 4), 4), 4))
def cg_f067_working_capital_efficiency_core95_3rd_v096_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_diff(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core96_3rd_v097_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_pct_change(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core97_3rd_v098_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 4))
def cg_f067_working_capital_efficiency_core98_3rd_v099_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core99_3rd_v100_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core100_3rd_v101_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(workingcapital, 4), 8), 4))
def cg_f067_working_capital_efficiency_core101_3rd_v102_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(revenue, 4), 8), 4))
def cg_f067_working_capital_efficiency_core102_3rd_v103_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(assets, 4), 8), 4))
def cg_f067_working_capital_efficiency_core103_3rd_v104_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_safe_div(workingcapital, revenue), 4), 8), 4))
def cg_f067_working_capital_efficiency_core104_3rd_v105_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_safe_div(workingcapital, assets), 4), 8), 4))
def cg_f067_working_capital_efficiency_core105_3rd_v106_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_diff(workingcapital, 4), 4), 8), 4))
def cg_f067_working_capital_efficiency_core106_3rd_v107_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_pct_change(workingcapital, 4), 4), 8), 4))
def cg_f067_working_capital_efficiency_core107_3rd_v108_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 8), 4))
def cg_f067_working_capital_efficiency_core108_3rd_v109_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 8), 4))
def cg_f067_working_capital_efficiency_core109_3rd_v110_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 8), 4))
def cg_f067_working_capital_efficiency_core110_3rd_v111_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core111_3rd_v112_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(revenue, 4), 4), 4))
def cg_f067_working_capital_efficiency_core112_3rd_v113_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(assets, 4), 4), 4))
def cg_f067_working_capital_efficiency_core113_3rd_v114_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core114_3rd_v115_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_safe_div(workingcapital, assets), 4), 4), 4))
def cg_f067_working_capital_efficiency_core115_3rd_v116_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_diff(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core116_3rd_v117_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_pct_change(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core117_3rd_v118_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 4))
def cg_f067_working_capital_efficiency_core118_3rd_v119_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core119_3rd_v120_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core120_3rd_v121_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core121_3rd_v122_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(revenue, 4), 4), 4))
def cg_f067_working_capital_efficiency_core122_3rd_v123_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(assets, 4), 4), 4))
def cg_f067_working_capital_efficiency_core123_3rd_v124_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core124_3rd_v125_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_safe_div(workingcapital, assets), 4), 4), 4))
def cg_f067_working_capital_efficiency_core125_3rd_v126_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_diff(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core126_3rd_v127_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_pct_change(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core127_3rd_v128_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 4))
def cg_f067_working_capital_efficiency_core128_3rd_v129_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core129_3rd_v130_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core130_3rd_v131_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core131_3rd_v132_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(revenue, 4), 4), 4))
def cg_f067_working_capital_efficiency_core132_3rd_v133_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(assets, 4), 4), 4))
def cg_f067_working_capital_efficiency_core133_3rd_v134_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core134_3rd_v135_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_safe_div(workingcapital, assets), 4), 4), 4))
def cg_f067_working_capital_efficiency_core135_3rd_v136_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_diff(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core136_3rd_v137_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_pct_change(workingcapital, 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core137_3rd_v138_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 4))
def cg_f067_working_capital_efficiency_core138_3rd_v139_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 4))
def cg_f067_working_capital_efficiency_core139_3rd_v140_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core140_3rd_v141_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core141_3rd_v142_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(revenue, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core142_3rd_v143_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(assets, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core143_3rd_v144_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(workingcapital, revenue), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core144_3rd_v145_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(workingcapital, assets), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core145_3rd_v146_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_diff(workingcapital, 4), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core146_3rd_v147_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_pct_change(workingcapital, 4), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core147_3rd_v148_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core148_3rd_v149_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core149_3rd_v150_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 4), 8))