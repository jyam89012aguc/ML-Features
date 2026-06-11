import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f044_inventory_dynamics_core00_2nd_v001_signal(inventory, revenue, cor, assets):
    return _clean(_slope(inventory, 4))
def cg_f044_inventory_dynamics_core01_2nd_v002_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_safe_div(inventory, revenue), 4))
def cg_f044_inventory_dynamics_core02_2nd_v003_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_safe_div(inventory, cor), 4))
def cg_f044_inventory_dynamics_core03_2nd_v004_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_safe_div(inventory, assets), 4))
def cg_f044_inventory_dynamics_core04_2nd_v005_signal(inventory, revenue, cor, assets):
    return _clean(_slope(revenue - cor, 4))
def cg_f044_inventory_dynamics_core05_2nd_v006_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_diff(inventory, 4), 4))
def cg_f044_inventory_dynamics_core06_2nd_v007_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_pct_change(inventory, 4), 4))
def cg_f044_inventory_dynamics_core07_2nd_v008_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_slope(inventory, 8), 4))
def cg_f044_inventory_dynamics_core08_2nd_v009_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_z(inventory, 12), 4))
def cg_f044_inventory_dynamics_core09_2nd_v010_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(inventory, 4), 4))
def cg_f044_inventory_dynamics_core10_2nd_v011_signal(inventory, revenue, cor, assets):
    return _clean(_slope(inventory, 8))
def cg_f044_inventory_dynamics_core11_2nd_v012_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_safe_div(inventory, revenue), 8))
def cg_f044_inventory_dynamics_core12_2nd_v013_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_safe_div(inventory, cor), 8))
def cg_f044_inventory_dynamics_core13_2nd_v014_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_safe_div(inventory, assets), 8))
def cg_f044_inventory_dynamics_core14_2nd_v015_signal(inventory, revenue, cor, assets):
    return _clean(_slope(revenue - cor, 8))
def cg_f044_inventory_dynamics_core15_2nd_v016_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_diff(inventory, 4), 8))
def cg_f044_inventory_dynamics_core16_2nd_v017_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_pct_change(inventory, 4), 8))
def cg_f044_inventory_dynamics_core17_2nd_v018_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_slope(inventory, 8), 8))
def cg_f044_inventory_dynamics_core18_2nd_v019_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_z(inventory, 12), 8))
def cg_f044_inventory_dynamics_core19_2nd_v020_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(inventory, 4), 8))
def cg_f044_inventory_dynamics_core20_2nd_v021_signal(inventory, revenue, cor, assets):
    return _clean(_diff(inventory, 4))
def cg_f044_inventory_dynamics_core21_2nd_v022_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_safe_div(inventory, revenue), 4))
def cg_f044_inventory_dynamics_core22_2nd_v023_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_safe_div(inventory, cor), 4))
def cg_f044_inventory_dynamics_core23_2nd_v024_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_safe_div(inventory, assets), 4))
def cg_f044_inventory_dynamics_core24_2nd_v025_signal(inventory, revenue, cor, assets):
    return _clean(_diff(revenue - cor, 4))
def cg_f044_inventory_dynamics_core25_2nd_v026_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_diff(inventory, 4), 4))
def cg_f044_inventory_dynamics_core26_2nd_v027_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_pct_change(inventory, 4), 4))
def cg_f044_inventory_dynamics_core27_2nd_v028_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_slope(inventory, 8), 4))
def cg_f044_inventory_dynamics_core28_2nd_v029_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_z(inventory, 12), 4))
def cg_f044_inventory_dynamics_core29_2nd_v030_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(inventory, 4), 4))
def cg_f044_inventory_dynamics_core30_2nd_v031_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(inventory, 4), 8))
def cg_f044_inventory_dynamics_core31_2nd_v032_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_safe_div(inventory, revenue), 4), 8))
def cg_f044_inventory_dynamics_core32_2nd_v033_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_safe_div(inventory, cor), 4), 8))
def cg_f044_inventory_dynamics_core33_2nd_v034_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_safe_div(inventory, assets), 4), 8))
def cg_f044_inventory_dynamics_core34_2nd_v035_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(revenue - cor, 4), 8))
def cg_f044_inventory_dynamics_core35_2nd_v036_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_diff(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core36_2nd_v037_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_pct_change(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core37_2nd_v038_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_slope(inventory, 8), 4), 8))
def cg_f044_inventory_dynamics_core38_2nd_v039_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_z(inventory, 12), 4), 8))
def cg_f044_inventory_dynamics_core39_2nd_v040_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_mean(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core40_2nd_v041_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(inventory, 8), 12))
def cg_f044_inventory_dynamics_core41_2nd_v042_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_safe_div(inventory, revenue), 8), 12))
def cg_f044_inventory_dynamics_core42_2nd_v043_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_safe_div(inventory, cor), 8), 12))
def cg_f044_inventory_dynamics_core43_2nd_v044_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_safe_div(inventory, assets), 8), 12))
def cg_f044_inventory_dynamics_core44_2nd_v045_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(revenue - cor, 8), 12))
def cg_f044_inventory_dynamics_core45_2nd_v046_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_diff(inventory, 4), 8), 12))
def cg_f044_inventory_dynamics_core46_2nd_v047_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_pct_change(inventory, 4), 8), 12))
def cg_f044_inventory_dynamics_core47_2nd_v048_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_slope(inventory, 8), 8), 12))
def cg_f044_inventory_dynamics_core48_2nd_v049_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_z(inventory, 12), 8), 12))
def cg_f044_inventory_dynamics_core49_2nd_v050_signal(inventory, revenue, cor, assets):
    return _clean(_z(_slope(_mean(inventory, 4), 8), 12))
def cg_f044_inventory_dynamics_core50_2nd_v051_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(inventory, 4), 8))
def cg_f044_inventory_dynamics_core51_2nd_v052_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_safe_div(inventory, revenue), 4), 8))
def cg_f044_inventory_dynamics_core52_2nd_v053_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_safe_div(inventory, cor), 4), 8))
def cg_f044_inventory_dynamics_core53_2nd_v054_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_safe_div(inventory, assets), 4), 8))
def cg_f044_inventory_dynamics_core54_2nd_v055_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(revenue - cor, 4), 8))
def cg_f044_inventory_dynamics_core55_2nd_v056_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_diff(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core56_2nd_v057_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_pct_change(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core57_2nd_v058_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_slope(inventory, 8), 4), 8))
def cg_f044_inventory_dynamics_core58_2nd_v059_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_z(inventory, 12), 4), 8))
def cg_f044_inventory_dynamics_core59_2nd_v060_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core60_2nd_v061_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(inventory, 4), 12))
def cg_f044_inventory_dynamics_core61_2nd_v062_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_safe_div(inventory, revenue), 4), 12))
def cg_f044_inventory_dynamics_core62_2nd_v063_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_safe_div(inventory, cor), 4), 12))
def cg_f044_inventory_dynamics_core63_2nd_v064_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_safe_div(inventory, assets), 4), 12))
def cg_f044_inventory_dynamics_core64_2nd_v065_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(revenue - cor, 4), 12))
def cg_f044_inventory_dynamics_core65_2nd_v066_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_diff(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core66_2nd_v067_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_pct_change(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core67_2nd_v068_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_slope(inventory, 8), 4), 12))
def cg_f044_inventory_dynamics_core68_2nd_v069_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_z(inventory, 12), 4), 12))
def cg_f044_inventory_dynamics_core69_2nd_v070_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core70_2nd_v071_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(inventory, 4), 12))
def cg_f044_inventory_dynamics_core71_2nd_v072_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_safe_div(inventory, revenue), 4), 12))
def cg_f044_inventory_dynamics_core72_2nd_v073_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_safe_div(inventory, cor), 4), 12))
def cg_f044_inventory_dynamics_core73_2nd_v074_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_safe_div(inventory, assets), 4), 12))
def cg_f044_inventory_dynamics_core74_2nd_v075_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(revenue - cor, 4), 12))
def cg_f044_inventory_dynamics_core75_2nd_v076_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_diff(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core76_2nd_v077_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_pct_change(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core77_2nd_v078_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_slope(inventory, 8), 4), 12))
def cg_f044_inventory_dynamics_core78_2nd_v079_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_z(inventory, 12), 4), 12))
def cg_f044_inventory_dynamics_core79_2nd_v080_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_diff(_mean(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core80_2nd_v081_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(inventory, 4), 4))
def cg_f044_inventory_dynamics_core81_2nd_v082_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_safe_div(inventory, revenue), 4), 4))
def cg_f044_inventory_dynamics_core82_2nd_v083_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_safe_div(inventory, cor), 4), 4))
def cg_f044_inventory_dynamics_core83_2nd_v084_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_safe_div(inventory, assets), 4), 4))
def cg_f044_inventory_dynamics_core84_2nd_v085_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(revenue - cor, 4), 4))
def cg_f044_inventory_dynamics_core85_2nd_v086_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_diff(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core86_2nd_v087_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_pct_change(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core87_2nd_v088_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_slope(inventory, 8), 4), 4))
def cg_f044_inventory_dynamics_core88_2nd_v089_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_z(inventory, 12), 4), 4))
def cg_f044_inventory_dynamics_core89_2nd_v090_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_slope(_mean(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core90_2nd_v091_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(inventory, 4), 4))
def cg_f044_inventory_dynamics_core91_2nd_v092_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_safe_div(inventory, revenue), 4), 4))
def cg_f044_inventory_dynamics_core92_2nd_v093_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_safe_div(inventory, cor), 4), 4))
def cg_f044_inventory_dynamics_core93_2nd_v094_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_safe_div(inventory, assets), 4), 4))
def cg_f044_inventory_dynamics_core94_2nd_v095_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(revenue - cor, 4), 4))
def cg_f044_inventory_dynamics_core95_2nd_v096_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_diff(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core96_2nd_v097_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_pct_change(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core97_2nd_v098_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_slope(inventory, 8), 4), 4))
def cg_f044_inventory_dynamics_core98_2nd_v099_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_z(inventory, 12), 4), 4))
def cg_f044_inventory_dynamics_core99_2nd_v100_signal(inventory, revenue, cor, assets):
    return _clean(_mean(_diff(_mean(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core100_2nd_v101_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(inventory, 4), 4))
def cg_f044_inventory_dynamics_core101_2nd_v102_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_safe_div(inventory, revenue), 4), 4))
def cg_f044_inventory_dynamics_core102_2nd_v103_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_safe_div(inventory, cor), 4), 4))
def cg_f044_inventory_dynamics_core103_2nd_v104_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_safe_div(inventory, assets), 4), 4))
def cg_f044_inventory_dynamics_core104_2nd_v105_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(revenue - cor, 4), 4))
def cg_f044_inventory_dynamics_core105_2nd_v106_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_diff(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core106_2nd_v107_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_pct_change(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core107_2nd_v108_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_slope(inventory, 8), 4), 4))
def cg_f044_inventory_dynamics_core108_2nd_v109_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_z(inventory, 12), 4), 4))
def cg_f044_inventory_dynamics_core109_2nd_v110_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_mean(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core110_2nd_v111_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(inventory, 8), 8))
def cg_f044_inventory_dynamics_core111_2nd_v112_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_safe_div(inventory, revenue), 8), 8))
def cg_f044_inventory_dynamics_core112_2nd_v113_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_safe_div(inventory, cor), 8), 8))
def cg_f044_inventory_dynamics_core113_2nd_v114_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_safe_div(inventory, assets), 8), 8))
def cg_f044_inventory_dynamics_core114_2nd_v115_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(revenue - cor, 8), 8))
def cg_f044_inventory_dynamics_core115_2nd_v116_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_diff(inventory, 4), 8), 8))
def cg_f044_inventory_dynamics_core116_2nd_v117_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_pct_change(inventory, 4), 8), 8))
def cg_f044_inventory_dynamics_core117_2nd_v118_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_slope(inventory, 8), 8), 8))
def cg_f044_inventory_dynamics_core118_2nd_v119_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_z(inventory, 12), 8), 8))
def cg_f044_inventory_dynamics_core119_2nd_v120_signal(inventory, revenue, cor, assets):
    return _clean(_slope(_mean(_mean(inventory, 4), 8), 8))
def cg_f044_inventory_dynamics_core120_2nd_v121_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(inventory, 4), 4))
def cg_f044_inventory_dynamics_core121_2nd_v122_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_safe_div(inventory, revenue), 4), 4))
def cg_f044_inventory_dynamics_core122_2nd_v123_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_safe_div(inventory, cor), 4), 4))
def cg_f044_inventory_dynamics_core123_2nd_v124_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_safe_div(inventory, assets), 4), 4))
def cg_f044_inventory_dynamics_core124_2nd_v125_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(revenue - cor, 4), 4))
def cg_f044_inventory_dynamics_core125_2nd_v126_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_diff(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core126_2nd_v127_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_pct_change(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core127_2nd_v128_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_slope(inventory, 8), 4), 4))
def cg_f044_inventory_dynamics_core128_2nd_v129_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_z(inventory, 12), 4), 4))
def cg_f044_inventory_dynamics_core129_2nd_v130_signal(inventory, revenue, cor, assets):
    return _clean(_diff(_mean(_mean(inventory, 4), 4), 4))
def cg_f044_inventory_dynamics_core130_2nd_v131_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(inventory, 4), 4), 8))
def cg_f044_inventory_dynamics_core131_2nd_v132_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_safe_div(inventory, revenue), 4), 4), 8))
def cg_f044_inventory_dynamics_core132_2nd_v133_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_safe_div(inventory, cor), 4), 4), 8))
def cg_f044_inventory_dynamics_core133_2nd_v134_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_safe_div(inventory, assets), 4), 4), 8))
def cg_f044_inventory_dynamics_core134_2nd_v135_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(revenue - cor, 4), 4), 8))
def cg_f044_inventory_dynamics_core135_2nd_v136_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_diff(inventory, 4), 4), 4), 8))
def cg_f044_inventory_dynamics_core136_2nd_v137_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_pct_change(inventory, 4), 4), 4), 8))
def cg_f044_inventory_dynamics_core137_2nd_v138_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_slope(inventory, 8), 4), 4), 8))
def cg_f044_inventory_dynamics_core138_2nd_v139_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_z(inventory, 12), 4), 4), 8))
def cg_f044_inventory_dynamics_core139_2nd_v140_signal(inventory, revenue, cor, assets):
    return _clean(_z(_diff(_mean(_mean(inventory, 4), 4), 4), 8))
def cg_f044_inventory_dynamics_core140_2nd_v141_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(inventory, 4), 4), 12))
def cg_f044_inventory_dynamics_core141_2nd_v142_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_safe_div(inventory, revenue), 4), 4), 12))
def cg_f044_inventory_dynamics_core142_2nd_v143_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_safe_div(inventory, cor), 4), 4), 12))
def cg_f044_inventory_dynamics_core143_2nd_v144_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_safe_div(inventory, assets), 4), 4), 12))
def cg_f044_inventory_dynamics_core144_2nd_v145_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(revenue - cor, 4), 4), 12))
def cg_f044_inventory_dynamics_core145_2nd_v146_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_diff(inventory, 4), 4), 4), 12))
def cg_f044_inventory_dynamics_core146_2nd_v147_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_pct_change(inventory, 4), 4), 4), 12))
def cg_f044_inventory_dynamics_core147_2nd_v148_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_slope(inventory, 8), 4), 4), 12))
def cg_f044_inventory_dynamics_core148_2nd_v149_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_z(inventory, 12), 4), 4), 12))
def cg_f044_inventory_dynamics_core149_2nd_v150_signal(inventory, revenue, cor, assets):
    return _clean(_rank(_slope(_mean(_mean(inventory, 4), 4), 4), 12))