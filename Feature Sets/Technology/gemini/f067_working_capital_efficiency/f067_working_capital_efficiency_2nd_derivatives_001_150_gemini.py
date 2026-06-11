import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f067_working_capital_efficiency_core00_2nd_v001_signal(workingcapital, revenue, assets):
    return _clean(_slope(workingcapital, 4))
def cg_f067_working_capital_efficiency_core01_2nd_v002_signal(workingcapital, revenue, assets):
    return _clean(_slope(revenue, 4))
def cg_f067_working_capital_efficiency_core02_2nd_v003_signal(workingcapital, revenue, assets):
    return _clean(_slope(assets, 4))
def cg_f067_working_capital_efficiency_core03_2nd_v004_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, revenue), 4))
def cg_f067_working_capital_efficiency_core04_2nd_v005_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, assets), 4))
def cg_f067_working_capital_efficiency_core05_2nd_v006_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core06_2nd_v007_signal(workingcapital, revenue, assets):
    return _clean(_slope(_pct_change(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core07_2nd_v008_signal(workingcapital, revenue, assets):
    return _clean(_slope(_z(_safe_div(workingcapital, revenue), 8), 4))
def cg_f067_working_capital_efficiency_core08_2nd_v009_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core09_2nd_v010_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4))
def cg_f067_working_capital_efficiency_core10_2nd_v011_signal(workingcapital, revenue, assets):
    return _clean(_slope(workingcapital, 8))
def cg_f067_working_capital_efficiency_core11_2nd_v012_signal(workingcapital, revenue, assets):
    return _clean(_slope(revenue, 8))
def cg_f067_working_capital_efficiency_core12_2nd_v013_signal(workingcapital, revenue, assets):
    return _clean(_slope(assets, 8))
def cg_f067_working_capital_efficiency_core13_2nd_v014_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, revenue), 8))
def cg_f067_working_capital_efficiency_core14_2nd_v015_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(workingcapital, assets), 8))
def cg_f067_working_capital_efficiency_core15_2nd_v016_signal(workingcapital, revenue, assets):
    return _clean(_slope(_diff(workingcapital, 4), 8))
def cg_f067_working_capital_efficiency_core16_2nd_v017_signal(workingcapital, revenue, assets):
    return _clean(_slope(_pct_change(workingcapital, 4), 8))
def cg_f067_working_capital_efficiency_core17_2nd_v018_signal(workingcapital, revenue, assets):
    return _clean(_slope(_z(_safe_div(workingcapital, revenue), 8), 8))
def cg_f067_working_capital_efficiency_core18_2nd_v019_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(workingcapital, revenue), 4), 8))
def cg_f067_working_capital_efficiency_core19_2nd_v020_signal(workingcapital, revenue, assets):
    return _clean(_slope(_safe_div(_diff(workingcapital, 4), revenue), 8))
def cg_f067_working_capital_efficiency_core20_2nd_v021_signal(workingcapital, revenue, assets):
    return _clean(_diff(workingcapital, 4))
def cg_f067_working_capital_efficiency_core21_2nd_v022_signal(workingcapital, revenue, assets):
    return _clean(_diff(revenue, 4))
def cg_f067_working_capital_efficiency_core22_2nd_v023_signal(workingcapital, revenue, assets):
    return _clean(_diff(assets, 4))
def cg_f067_working_capital_efficiency_core23_2nd_v024_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(workingcapital, revenue), 4))
def cg_f067_working_capital_efficiency_core24_2nd_v025_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(workingcapital, assets), 4))
def cg_f067_working_capital_efficiency_core25_2nd_v026_signal(workingcapital, revenue, assets):
    return _clean(_diff(_diff(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core26_2nd_v027_signal(workingcapital, revenue, assets):
    return _clean(_diff(_pct_change(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core27_2nd_v028_signal(workingcapital, revenue, assets):
    return _clean(_diff(_z(_safe_div(workingcapital, revenue), 8), 4))
def cg_f067_working_capital_efficiency_core28_2nd_v029_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core29_2nd_v030_signal(workingcapital, revenue, assets):
    return _clean(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4))
def cg_f067_working_capital_efficiency_core30_2nd_v031_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(workingcapital, 4), 8))
def cg_f067_working_capital_efficiency_core31_2nd_v032_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f067_working_capital_efficiency_core32_2nd_v033_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(assets, 4), 8))
def cg_f067_working_capital_efficiency_core33_2nd_v034_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_safe_div(workingcapital, revenue), 4), 8))
def cg_f067_working_capital_efficiency_core34_2nd_v035_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_safe_div(workingcapital, assets), 4), 8))
def cg_f067_working_capital_efficiency_core35_2nd_v036_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core36_2nd_v037_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_pct_change(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core37_2nd_v038_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 8))
def cg_f067_working_capital_efficiency_core38_2nd_v039_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core39_2nd_v040_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 8))
def cg_f067_working_capital_efficiency_core40_2nd_v041_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(workingcapital, 8), 12))
def cg_f067_working_capital_efficiency_core41_2nd_v042_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f067_working_capital_efficiency_core42_2nd_v043_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(assets, 8), 12))
def cg_f067_working_capital_efficiency_core43_2nd_v044_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_safe_div(workingcapital, revenue), 8), 12))
def cg_f067_working_capital_efficiency_core44_2nd_v045_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_safe_div(workingcapital, assets), 8), 12))
def cg_f067_working_capital_efficiency_core45_2nd_v046_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_diff(workingcapital, 4), 8), 12))
def cg_f067_working_capital_efficiency_core46_2nd_v047_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_pct_change(workingcapital, 4), 8), 12))
def cg_f067_working_capital_efficiency_core47_2nd_v048_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_z(_safe_div(workingcapital, revenue), 8), 8), 12))
def cg_f067_working_capital_efficiency_core48_2nd_v049_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_mean(_safe_div(workingcapital, revenue), 4), 8), 12))
def cg_f067_working_capital_efficiency_core49_2nd_v050_signal(workingcapital, revenue, assets):
    return _clean(_z(_slope(_safe_div(_diff(workingcapital, 4), revenue), 8), 12))
def cg_f067_working_capital_efficiency_core50_2nd_v051_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(workingcapital, 4), 8))
def cg_f067_working_capital_efficiency_core51_2nd_v052_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f067_working_capital_efficiency_core52_2nd_v053_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(assets, 4), 8))
def cg_f067_working_capital_efficiency_core53_2nd_v054_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_safe_div(workingcapital, revenue), 4), 8))
def cg_f067_working_capital_efficiency_core54_2nd_v055_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_safe_div(workingcapital, assets), 4), 8))
def cg_f067_working_capital_efficiency_core55_2nd_v056_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_diff(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core56_2nd_v057_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_pct_change(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core57_2nd_v058_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 8))
def cg_f067_working_capital_efficiency_core58_2nd_v059_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core59_2nd_v060_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 8))
def cg_f067_working_capital_efficiency_core60_2nd_v061_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(workingcapital, 4), 12))
def cg_f067_working_capital_efficiency_core61_2nd_v062_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f067_working_capital_efficiency_core62_2nd_v063_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(assets, 4), 12))
def cg_f067_working_capital_efficiency_core63_2nd_v064_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_safe_div(workingcapital, revenue), 4), 12))
def cg_f067_working_capital_efficiency_core64_2nd_v065_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_safe_div(workingcapital, assets), 4), 12))
def cg_f067_working_capital_efficiency_core65_2nd_v066_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_diff(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core66_2nd_v067_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_pct_change(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core67_2nd_v068_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 12))
def cg_f067_working_capital_efficiency_core68_2nd_v069_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core69_2nd_v070_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 12))
def cg_f067_working_capital_efficiency_core70_2nd_v071_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(workingcapital, 4), 12))
def cg_f067_working_capital_efficiency_core71_2nd_v072_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f067_working_capital_efficiency_core72_2nd_v073_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(assets, 4), 12))
def cg_f067_working_capital_efficiency_core73_2nd_v074_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_safe_div(workingcapital, revenue), 4), 12))
def cg_f067_working_capital_efficiency_core74_2nd_v075_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_safe_div(workingcapital, assets), 4), 12))
def cg_f067_working_capital_efficiency_core75_2nd_v076_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_diff(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core76_2nd_v077_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_pct_change(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core77_2nd_v078_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 12))
def cg_f067_working_capital_efficiency_core78_2nd_v079_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core79_2nd_v080_signal(workingcapital, revenue, assets):
    return _clean(_rank(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 12))
def cg_f067_working_capital_efficiency_core80_2nd_v081_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core81_2nd_v082_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f067_working_capital_efficiency_core82_2nd_v083_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(assets, 4), 4))
def cg_f067_working_capital_efficiency_core83_2nd_v084_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core84_2nd_v085_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_safe_div(workingcapital, assets), 4), 4))
def cg_f067_working_capital_efficiency_core85_2nd_v086_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core86_2nd_v087_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_pct_change(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core87_2nd_v088_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_z(_safe_div(workingcapital, revenue), 8), 4), 4))
def cg_f067_working_capital_efficiency_core88_2nd_v089_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core89_2nd_v090_signal(workingcapital, revenue, assets):
    return _clean(_mean(_slope(_safe_div(_diff(workingcapital, 4), revenue), 4), 4))
def cg_f067_working_capital_efficiency_core90_2nd_v091_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core91_2nd_v092_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f067_working_capital_efficiency_core92_2nd_v093_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(assets, 4), 4))
def cg_f067_working_capital_efficiency_core93_2nd_v094_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core94_2nd_v095_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_safe_div(workingcapital, assets), 4), 4))
def cg_f067_working_capital_efficiency_core95_2nd_v096_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core96_2nd_v097_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_pct_change(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core97_2nd_v098_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_z(_safe_div(workingcapital, revenue), 8), 4), 4))
def cg_f067_working_capital_efficiency_core98_2nd_v099_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core99_2nd_v100_signal(workingcapital, revenue, assets):
    return _clean(_mean(_diff(_safe_div(_diff(workingcapital, 4), revenue), 4), 4))
def cg_f067_working_capital_efficiency_core100_2nd_v101_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core101_2nd_v102_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f067_working_capital_efficiency_core102_2nd_v103_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f067_working_capital_efficiency_core103_2nd_v104_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core104_2nd_v105_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(workingcapital, assets), 4), 4))
def cg_f067_working_capital_efficiency_core105_2nd_v106_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core106_2nd_v107_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_pct_change(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core107_2nd_v108_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_z(_safe_div(workingcapital, revenue), 8), 4), 4))
def cg_f067_working_capital_efficiency_core108_2nd_v109_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_mean(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core109_2nd_v110_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(_diff(workingcapital, 4), revenue), 4), 4))
def cg_f067_working_capital_efficiency_core110_2nd_v111_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(workingcapital, 8), 8))
def cg_f067_working_capital_efficiency_core111_2nd_v112_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f067_working_capital_efficiency_core112_2nd_v113_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(assets, 8), 8))
def cg_f067_working_capital_efficiency_core113_2nd_v114_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(workingcapital, revenue), 8), 8))
def cg_f067_working_capital_efficiency_core114_2nd_v115_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(workingcapital, assets), 8), 8))
def cg_f067_working_capital_efficiency_core115_2nd_v116_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_diff(workingcapital, 4), 8), 8))
def cg_f067_working_capital_efficiency_core116_2nd_v117_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_pct_change(workingcapital, 4), 8), 8))
def cg_f067_working_capital_efficiency_core117_2nd_v118_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_z(_safe_div(workingcapital, revenue), 8), 8), 8))
def cg_f067_working_capital_efficiency_core118_2nd_v119_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_mean(_safe_div(workingcapital, revenue), 4), 8), 8))
def cg_f067_working_capital_efficiency_core119_2nd_v120_signal(workingcapital, revenue, assets):
    return _clean(_slope(_mean(_safe_div(_diff(workingcapital, 4), revenue), 8), 8))
def cg_f067_working_capital_efficiency_core120_2nd_v121_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(workingcapital, 4), 4))
def cg_f067_working_capital_efficiency_core121_2nd_v122_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f067_working_capital_efficiency_core122_2nd_v123_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f067_working_capital_efficiency_core123_2nd_v124_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4))
def cg_f067_working_capital_efficiency_core124_2nd_v125_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_safe_div(workingcapital, assets), 4), 4))
def cg_f067_working_capital_efficiency_core125_2nd_v126_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_diff(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core126_2nd_v127_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_pct_change(workingcapital, 4), 4), 4))
def cg_f067_working_capital_efficiency_core127_2nd_v128_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_z(_safe_div(workingcapital, revenue), 8), 4), 4))
def cg_f067_working_capital_efficiency_core128_2nd_v129_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_mean(_safe_div(workingcapital, revenue), 4), 4), 4))
def cg_f067_working_capital_efficiency_core129_2nd_v130_signal(workingcapital, revenue, assets):
    return _clean(_diff(_mean(_safe_div(_diff(workingcapital, 4), revenue), 4), 4))
def cg_f067_working_capital_efficiency_core130_2nd_v131_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(workingcapital, 4), 4), 8))
def cg_f067_working_capital_efficiency_core131_2nd_v132_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f067_working_capital_efficiency_core132_2nd_v133_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f067_working_capital_efficiency_core133_2nd_v134_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_safe_div(workingcapital, revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core134_2nd_v135_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_safe_div(workingcapital, assets), 4), 4), 8))
def cg_f067_working_capital_efficiency_core135_2nd_v136_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_diff(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core136_2nd_v137_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_pct_change(workingcapital, 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core137_2nd_v138_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 8))
def cg_f067_working_capital_efficiency_core138_2nd_v139_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 8))
def cg_f067_working_capital_efficiency_core139_2nd_v140_signal(workingcapital, revenue, assets):
    return _clean(_z(_diff(_mean(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 8))
def cg_f067_working_capital_efficiency_core140_2nd_v141_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(workingcapital, 4), 4), 12))
def cg_f067_working_capital_efficiency_core141_2nd_v142_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f067_working_capital_efficiency_core142_2nd_v143_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f067_working_capital_efficiency_core143_2nd_v144_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_safe_div(workingcapital, revenue), 4), 4), 12))
def cg_f067_working_capital_efficiency_core144_2nd_v145_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_safe_div(workingcapital, assets), 4), 4), 12))
def cg_f067_working_capital_efficiency_core145_2nd_v146_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_diff(workingcapital, 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core146_2nd_v147_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_pct_change(workingcapital, 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core147_2nd_v148_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_z(_safe_div(workingcapital, revenue), 8), 4), 4), 12))
def cg_f067_working_capital_efficiency_core148_2nd_v149_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_mean(_safe_div(workingcapital, revenue), 4), 4), 4), 12))
def cg_f067_working_capital_efficiency_core149_2nd_v150_signal(workingcapital, revenue, assets):
    return _clean(_rank(_slope(_mean(_safe_div(_diff(workingcapital, 4), revenue), 4), 4), 12))