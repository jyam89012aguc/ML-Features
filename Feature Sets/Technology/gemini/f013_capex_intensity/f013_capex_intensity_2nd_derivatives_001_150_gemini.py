import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f013_capex_intensity_core00_2nd_v001_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(capex, 4))
def cg_f013_capex_intensity_core01_2nd_v002_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(ppnenet, 4))
def cg_f013_capex_intensity_core02_2nd_v003_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, ppnenet), 4))
def cg_f013_capex_intensity_core03_2nd_v004_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, assets), 4))
def cg_f013_capex_intensity_core04_2nd_v005_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, revenue), 4))
def cg_f013_capex_intensity_core05_2nd_v006_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(ppnenet, assets), 4))
def cg_f013_capex_intensity_core06_2nd_v007_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4))
def cg_f013_capex_intensity_core07_2nd_v008_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(ppnenet, revenue), 4))
def cg_f013_capex_intensity_core08_2nd_v009_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(capex.abs(), 4))
def cg_f013_capex_intensity_core09_2nd_v010_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_log(capex.abs() + 1.0), 4))
def cg_f013_capex_intensity_core10_2nd_v011_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(capex, 8))
def cg_f013_capex_intensity_core11_2nd_v012_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(ppnenet, 8))
def cg_f013_capex_intensity_core12_2nd_v013_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, ppnenet), 8))
def cg_f013_capex_intensity_core13_2nd_v014_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, assets), 8))
def cg_f013_capex_intensity_core14_2nd_v015_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, revenue), 8))
def cg_f013_capex_intensity_core15_2nd_v016_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(ppnenet, assets), 8))
def cg_f013_capex_intensity_core16_2nd_v017_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 8))
def cg_f013_capex_intensity_core17_2nd_v018_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_safe_div(ppnenet, revenue), 8))
def cg_f013_capex_intensity_core18_2nd_v019_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(capex.abs(), 8))
def cg_f013_capex_intensity_core19_2nd_v020_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_log(capex.abs() + 1.0), 8))
def cg_f013_capex_intensity_core20_2nd_v021_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(capex, 4))
def cg_f013_capex_intensity_core21_2nd_v022_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(ppnenet, 4))
def cg_f013_capex_intensity_core22_2nd_v023_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_safe_div(capex, ppnenet), 4))
def cg_f013_capex_intensity_core23_2nd_v024_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_safe_div(capex, assets), 4))
def cg_f013_capex_intensity_core24_2nd_v025_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_safe_div(capex, revenue), 4))
def cg_f013_capex_intensity_core25_2nd_v026_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_safe_div(ppnenet, assets), 4))
def cg_f013_capex_intensity_core26_2nd_v027_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4))
def cg_f013_capex_intensity_core27_2nd_v028_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_safe_div(ppnenet, revenue), 4))
def cg_f013_capex_intensity_core28_2nd_v029_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(capex.abs(), 4))
def cg_f013_capex_intensity_core29_2nd_v030_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_log(capex.abs() + 1.0), 4))
def cg_f013_capex_intensity_core30_2nd_v031_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(capex, 4), 8))
def cg_f013_capex_intensity_core31_2nd_v032_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(ppnenet, 4), 8))
def cg_f013_capex_intensity_core32_2nd_v033_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, ppnenet), 4), 8))
def cg_f013_capex_intensity_core33_2nd_v034_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, assets), 4), 8))
def cg_f013_capex_intensity_core34_2nd_v035_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, revenue), 4), 8))
def cg_f013_capex_intensity_core35_2nd_v036_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(ppnenet, assets), 4), 8))
def cg_f013_capex_intensity_core36_2nd_v037_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8))
def cg_f013_capex_intensity_core37_2nd_v038_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(ppnenet, revenue), 4), 8))
def cg_f013_capex_intensity_core38_2nd_v039_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(capex.abs(), 4), 8))
def cg_f013_capex_intensity_core39_2nd_v040_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_log(capex.abs() + 1.0), 4), 8))
def cg_f013_capex_intensity_core40_2nd_v041_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(capex, 8), 12))
def cg_f013_capex_intensity_core41_2nd_v042_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(ppnenet, 8), 12))
def cg_f013_capex_intensity_core42_2nd_v043_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, ppnenet), 8), 12))
def cg_f013_capex_intensity_core43_2nd_v044_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, assets), 8), 12))
def cg_f013_capex_intensity_core44_2nd_v045_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, revenue), 8), 12))
def cg_f013_capex_intensity_core45_2nd_v046_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(ppnenet, assets), 8), 12))
def cg_f013_capex_intensity_core46_2nd_v047_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 8), 12))
def cg_f013_capex_intensity_core47_2nd_v048_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_safe_div(ppnenet, revenue), 8), 12))
def cg_f013_capex_intensity_core48_2nd_v049_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(capex.abs(), 8), 12))
def cg_f013_capex_intensity_core49_2nd_v050_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_slope(_log(capex.abs() + 1.0), 8), 12))
def cg_f013_capex_intensity_core50_2nd_v051_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(capex, 4), 8))
def cg_f013_capex_intensity_core51_2nd_v052_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(ppnenet, 4), 8))
def cg_f013_capex_intensity_core52_2nd_v053_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_safe_div(capex, ppnenet), 4), 8))
def cg_f013_capex_intensity_core53_2nd_v054_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_safe_div(capex, assets), 4), 8))
def cg_f013_capex_intensity_core54_2nd_v055_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_safe_div(capex, revenue), 4), 8))
def cg_f013_capex_intensity_core55_2nd_v056_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_safe_div(ppnenet, assets), 4), 8))
def cg_f013_capex_intensity_core56_2nd_v057_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8))
def cg_f013_capex_intensity_core57_2nd_v058_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_safe_div(ppnenet, revenue), 4), 8))
def cg_f013_capex_intensity_core58_2nd_v059_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(capex.abs(), 4), 8))
def cg_f013_capex_intensity_core59_2nd_v060_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_log(capex.abs() + 1.0), 4), 8))
def cg_f013_capex_intensity_core60_2nd_v061_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(capex, 4), 12))
def cg_f013_capex_intensity_core61_2nd_v062_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(ppnenet, 4), 12))
def cg_f013_capex_intensity_core62_2nd_v063_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_safe_div(capex, ppnenet), 4), 12))
def cg_f013_capex_intensity_core63_2nd_v064_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_safe_div(capex, assets), 4), 12))
def cg_f013_capex_intensity_core64_2nd_v065_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_safe_div(capex, revenue), 4), 12))
def cg_f013_capex_intensity_core65_2nd_v066_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_safe_div(ppnenet, assets), 4), 12))
def cg_f013_capex_intensity_core66_2nd_v067_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 12))
def cg_f013_capex_intensity_core67_2nd_v068_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_safe_div(ppnenet, revenue), 4), 12))
def cg_f013_capex_intensity_core68_2nd_v069_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(capex.abs(), 4), 12))
def cg_f013_capex_intensity_core69_2nd_v070_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_log(capex.abs() + 1.0), 4), 12))
def cg_f013_capex_intensity_core70_2nd_v071_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(capex, 4), 12))
def cg_f013_capex_intensity_core71_2nd_v072_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(ppnenet, 4), 12))
def cg_f013_capex_intensity_core72_2nd_v073_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_safe_div(capex, ppnenet), 4), 12))
def cg_f013_capex_intensity_core73_2nd_v074_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_safe_div(capex, assets), 4), 12))
def cg_f013_capex_intensity_core74_2nd_v075_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_safe_div(capex, revenue), 4), 12))
def cg_f013_capex_intensity_core75_2nd_v076_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_safe_div(ppnenet, assets), 4), 12))
def cg_f013_capex_intensity_core76_2nd_v077_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 12))
def cg_f013_capex_intensity_core77_2nd_v078_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_safe_div(ppnenet, revenue), 4), 12))
def cg_f013_capex_intensity_core78_2nd_v079_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(capex.abs(), 4), 12))
def cg_f013_capex_intensity_core79_2nd_v080_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_diff(_log(capex.abs() + 1.0), 4), 12))
def cg_f013_capex_intensity_core80_2nd_v081_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(capex, 4), 4))
def cg_f013_capex_intensity_core81_2nd_v082_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(ppnenet, 4), 4))
def cg_f013_capex_intensity_core82_2nd_v083_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_safe_div(capex, ppnenet), 4), 4))
def cg_f013_capex_intensity_core83_2nd_v084_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_safe_div(capex, assets), 4), 4))
def cg_f013_capex_intensity_core84_2nd_v085_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_safe_div(capex, revenue), 4), 4))
def cg_f013_capex_intensity_core85_2nd_v086_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_safe_div(ppnenet, assets), 4), 4))
def cg_f013_capex_intensity_core86_2nd_v087_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core87_2nd_v088_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_safe_div(ppnenet, revenue), 4), 4))
def cg_f013_capex_intensity_core88_2nd_v089_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(capex.abs(), 4), 4))
def cg_f013_capex_intensity_core89_2nd_v090_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_slope(_log(capex.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core90_2nd_v091_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(capex, 4), 4))
def cg_f013_capex_intensity_core91_2nd_v092_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(ppnenet, 4), 4))
def cg_f013_capex_intensity_core92_2nd_v093_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_safe_div(capex, ppnenet), 4), 4))
def cg_f013_capex_intensity_core93_2nd_v094_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_safe_div(capex, assets), 4), 4))
def cg_f013_capex_intensity_core94_2nd_v095_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_safe_div(capex, revenue), 4), 4))
def cg_f013_capex_intensity_core95_2nd_v096_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_safe_div(ppnenet, assets), 4), 4))
def cg_f013_capex_intensity_core96_2nd_v097_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core97_2nd_v098_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_safe_div(ppnenet, revenue), 4), 4))
def cg_f013_capex_intensity_core98_2nd_v099_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(capex.abs(), 4), 4))
def cg_f013_capex_intensity_core99_2nd_v100_signal(capex, ppnenet, assets, revenue):
    return _clean(_mean(_diff(_log(capex.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core100_2nd_v101_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(capex, 4), 4))
def cg_f013_capex_intensity_core101_2nd_v102_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(ppnenet, 4), 4))
def cg_f013_capex_intensity_core102_2nd_v103_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, ppnenet), 4), 4))
def cg_f013_capex_intensity_core103_2nd_v104_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, assets), 4), 4))
def cg_f013_capex_intensity_core104_2nd_v105_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, revenue), 4), 4))
def cg_f013_capex_intensity_core105_2nd_v106_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(ppnenet, assets), 4), 4))
def cg_f013_capex_intensity_core106_2nd_v107_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core107_2nd_v108_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(ppnenet, revenue), 4), 4))
def cg_f013_capex_intensity_core108_2nd_v109_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(capex.abs(), 4), 4))
def cg_f013_capex_intensity_core109_2nd_v110_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_log(capex.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core110_2nd_v111_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(capex, 8), 8))
def cg_f013_capex_intensity_core111_2nd_v112_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(ppnenet, 8), 8))
def cg_f013_capex_intensity_core112_2nd_v113_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, ppnenet), 8), 8))
def cg_f013_capex_intensity_core113_2nd_v114_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, assets), 8), 8))
def cg_f013_capex_intensity_core114_2nd_v115_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, revenue), 8), 8))
def cg_f013_capex_intensity_core115_2nd_v116_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(ppnenet, assets), 8), 8))
def cg_f013_capex_intensity_core116_2nd_v117_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 8), 8))
def cg_f013_capex_intensity_core117_2nd_v118_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_safe_div(ppnenet, revenue), 8), 8))
def cg_f013_capex_intensity_core118_2nd_v119_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(capex.abs(), 8), 8))
def cg_f013_capex_intensity_core119_2nd_v120_signal(capex, ppnenet, assets, revenue):
    return _clean(_slope(_mean(_log(capex.abs() + 1.0), 8), 8))
def cg_f013_capex_intensity_core120_2nd_v121_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(capex, 4), 4))
def cg_f013_capex_intensity_core121_2nd_v122_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(ppnenet, 4), 4))
def cg_f013_capex_intensity_core122_2nd_v123_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_safe_div(capex, ppnenet), 4), 4))
def cg_f013_capex_intensity_core123_2nd_v124_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_safe_div(capex, assets), 4), 4))
def cg_f013_capex_intensity_core124_2nd_v125_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_safe_div(capex, revenue), 4), 4))
def cg_f013_capex_intensity_core125_2nd_v126_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_safe_div(ppnenet, assets), 4), 4))
def cg_f013_capex_intensity_core126_2nd_v127_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core127_2nd_v128_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_safe_div(ppnenet, revenue), 4), 4))
def cg_f013_capex_intensity_core128_2nd_v129_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(capex.abs(), 4), 4))
def cg_f013_capex_intensity_core129_2nd_v130_signal(capex, ppnenet, assets, revenue):
    return _clean(_diff(_mean(_log(capex.abs() + 1.0), 4), 4))
def cg_f013_capex_intensity_core130_2nd_v131_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(capex, 4), 4), 8))
def cg_f013_capex_intensity_core131_2nd_v132_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(ppnenet, 4), 4), 8))
def cg_f013_capex_intensity_core132_2nd_v133_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_safe_div(capex, ppnenet), 4), 4), 8))
def cg_f013_capex_intensity_core133_2nd_v134_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_safe_div(capex, assets), 4), 4), 8))
def cg_f013_capex_intensity_core134_2nd_v135_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_safe_div(capex, revenue), 4), 4), 8))
def cg_f013_capex_intensity_core135_2nd_v136_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_safe_div(ppnenet, assets), 4), 4), 8))
def cg_f013_capex_intensity_core136_2nd_v137_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 8))
def cg_f013_capex_intensity_core137_2nd_v138_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_safe_div(ppnenet, revenue), 4), 4), 8))
def cg_f013_capex_intensity_core138_2nd_v139_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(capex.abs(), 4), 4), 8))
def cg_f013_capex_intensity_core139_2nd_v140_signal(capex, ppnenet, assets, revenue):
    return _clean(_z(_diff(_mean(_log(capex.abs() + 1.0), 4), 4), 8))
def cg_f013_capex_intensity_core140_2nd_v141_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(capex, 4), 4), 12))
def cg_f013_capex_intensity_core141_2nd_v142_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(ppnenet, 4), 4), 12))
def cg_f013_capex_intensity_core142_2nd_v143_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(capex, ppnenet), 4), 4), 12))
def cg_f013_capex_intensity_core143_2nd_v144_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(capex, assets), 4), 4), 12))
def cg_f013_capex_intensity_core144_2nd_v145_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(capex, revenue), 4), 4), 12))
def cg_f013_capex_intensity_core145_2nd_v146_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(ppnenet, assets), 4), 4), 12))
def cg_f013_capex_intensity_core146_2nd_v147_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 12))
def cg_f013_capex_intensity_core147_2nd_v148_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(ppnenet, revenue), 4), 4), 12))
def cg_f013_capex_intensity_core148_2nd_v149_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(capex.abs(), 4), 4), 12))
def cg_f013_capex_intensity_core149_2nd_v150_signal(capex, ppnenet, assets, revenue):
    return _clean(_rank(_slope(_mean(_log(capex.abs() + 1.0), 4), 4), 12))