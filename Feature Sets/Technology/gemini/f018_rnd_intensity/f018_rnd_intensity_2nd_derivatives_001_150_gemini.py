import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f018_rnd_intensity_core00_2nd_v001_signal(rnd, revenue, opex, assets):
    return _clean(_slope(rnd, 4))
def cg_f018_rnd_intensity_core01_2nd_v002_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, revenue), 4))
def cg_f018_rnd_intensity_core02_2nd_v003_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, opex), 4))
def cg_f018_rnd_intensity_core03_2nd_v004_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, assets), 4))
def cg_f018_rnd_intensity_core04_2nd_v005_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(opex, revenue), 4))
def cg_f018_rnd_intensity_core05_2nd_v006_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, revenue + opex), 4))
def cg_f018_rnd_intensity_core06_2nd_v007_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_log(rnd.abs() + 1.0), 4))
def cg_f018_rnd_intensity_core07_2nd_v008_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(revenue, assets), 4))
def cg_f018_rnd_intensity_core08_2nd_v009_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(opex, assets), 4))
def cg_f018_rnd_intensity_core09_2nd_v010_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, _mean(rnd, 8)), 4))
def cg_f018_rnd_intensity_core10_2nd_v011_signal(rnd, revenue, opex, assets):
    return _clean(_slope(rnd, 8))
def cg_f018_rnd_intensity_core11_2nd_v012_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, revenue), 8))
def cg_f018_rnd_intensity_core12_2nd_v013_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, opex), 8))
def cg_f018_rnd_intensity_core13_2nd_v014_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, assets), 8))
def cg_f018_rnd_intensity_core14_2nd_v015_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(opex, revenue), 8))
def cg_f018_rnd_intensity_core15_2nd_v016_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, revenue + opex), 8))
def cg_f018_rnd_intensity_core16_2nd_v017_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_log(rnd.abs() + 1.0), 8))
def cg_f018_rnd_intensity_core17_2nd_v018_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(revenue, assets), 8))
def cg_f018_rnd_intensity_core18_2nd_v019_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(opex, assets), 8))
def cg_f018_rnd_intensity_core19_2nd_v020_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_safe_div(rnd, _mean(rnd, 8)), 8))
def cg_f018_rnd_intensity_core20_2nd_v021_signal(rnd, revenue, opex, assets):
    return _clean(_diff(rnd, 4))
def cg_f018_rnd_intensity_core21_2nd_v022_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(rnd, revenue), 4))
def cg_f018_rnd_intensity_core22_2nd_v023_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(rnd, opex), 4))
def cg_f018_rnd_intensity_core23_2nd_v024_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(rnd, assets), 4))
def cg_f018_rnd_intensity_core24_2nd_v025_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(opex, revenue), 4))
def cg_f018_rnd_intensity_core25_2nd_v026_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(rnd, revenue + opex), 4))
def cg_f018_rnd_intensity_core26_2nd_v027_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_log(rnd.abs() + 1.0), 4))
def cg_f018_rnd_intensity_core27_2nd_v028_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(revenue, assets), 4))
def cg_f018_rnd_intensity_core28_2nd_v029_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(opex, assets), 4))
def cg_f018_rnd_intensity_core29_2nd_v030_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_safe_div(rnd, _mean(rnd, 8)), 4))
def cg_f018_rnd_intensity_core30_2nd_v031_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f018_rnd_intensity_core31_2nd_v032_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, revenue), 4), 8))
def cg_f018_rnd_intensity_core32_2nd_v033_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, opex), 4), 8))
def cg_f018_rnd_intensity_core33_2nd_v034_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, assets), 4), 8))
def cg_f018_rnd_intensity_core34_2nd_v035_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(opex, revenue), 4), 8))
def cg_f018_rnd_intensity_core35_2nd_v036_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, revenue + opex), 4), 8))
def cg_f018_rnd_intensity_core36_2nd_v037_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_log(rnd.abs() + 1.0), 4), 8))
def cg_f018_rnd_intensity_core37_2nd_v038_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(revenue, assets), 4), 8))
def cg_f018_rnd_intensity_core38_2nd_v039_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(opex, assets), 4), 8))
def cg_f018_rnd_intensity_core39_2nd_v040_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 8))
def cg_f018_rnd_intensity_core40_2nd_v041_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f018_rnd_intensity_core41_2nd_v042_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, revenue), 8), 12))
def cg_f018_rnd_intensity_core42_2nd_v043_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, opex), 8), 12))
def cg_f018_rnd_intensity_core43_2nd_v044_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, assets), 8), 12))
def cg_f018_rnd_intensity_core44_2nd_v045_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(opex, revenue), 8), 12))
def cg_f018_rnd_intensity_core45_2nd_v046_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, revenue + opex), 8), 12))
def cg_f018_rnd_intensity_core46_2nd_v047_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_log(rnd.abs() + 1.0), 8), 12))
def cg_f018_rnd_intensity_core47_2nd_v048_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(revenue, assets), 8), 12))
def cg_f018_rnd_intensity_core48_2nd_v049_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(opex, assets), 8), 12))
def cg_f018_rnd_intensity_core49_2nd_v050_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_safe_div(rnd, _mean(rnd, 8)), 8), 12))
def cg_f018_rnd_intensity_core50_2nd_v051_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f018_rnd_intensity_core51_2nd_v052_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(rnd, revenue), 4), 8))
def cg_f018_rnd_intensity_core52_2nd_v053_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(rnd, opex), 4), 8))
def cg_f018_rnd_intensity_core53_2nd_v054_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(rnd, assets), 4), 8))
def cg_f018_rnd_intensity_core54_2nd_v055_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(opex, revenue), 4), 8))
def cg_f018_rnd_intensity_core55_2nd_v056_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(rnd, revenue + opex), 4), 8))
def cg_f018_rnd_intensity_core56_2nd_v057_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_log(rnd.abs() + 1.0), 4), 8))
def cg_f018_rnd_intensity_core57_2nd_v058_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(revenue, assets), 4), 8))
def cg_f018_rnd_intensity_core58_2nd_v059_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(opex, assets), 4), 8))
def cg_f018_rnd_intensity_core59_2nd_v060_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 8))
def cg_f018_rnd_intensity_core60_2nd_v061_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f018_rnd_intensity_core61_2nd_v062_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(rnd, revenue), 4), 12))
def cg_f018_rnd_intensity_core62_2nd_v063_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(rnd, opex), 4), 12))
def cg_f018_rnd_intensity_core63_2nd_v064_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(rnd, assets), 4), 12))
def cg_f018_rnd_intensity_core64_2nd_v065_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(opex, revenue), 4), 12))
def cg_f018_rnd_intensity_core65_2nd_v066_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(rnd, revenue + opex), 4), 12))
def cg_f018_rnd_intensity_core66_2nd_v067_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_log(rnd.abs() + 1.0), 4), 12))
def cg_f018_rnd_intensity_core67_2nd_v068_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(revenue, assets), 4), 12))
def cg_f018_rnd_intensity_core68_2nd_v069_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(opex, assets), 4), 12))
def cg_f018_rnd_intensity_core69_2nd_v070_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 12))
def cg_f018_rnd_intensity_core70_2nd_v071_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f018_rnd_intensity_core71_2nd_v072_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(rnd, revenue), 4), 12))
def cg_f018_rnd_intensity_core72_2nd_v073_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(rnd, opex), 4), 12))
def cg_f018_rnd_intensity_core73_2nd_v074_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(rnd, assets), 4), 12))
def cg_f018_rnd_intensity_core74_2nd_v075_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(opex, revenue), 4), 12))
def cg_f018_rnd_intensity_core75_2nd_v076_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(rnd, revenue + opex), 4), 12))
def cg_f018_rnd_intensity_core76_2nd_v077_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_log(rnd.abs() + 1.0), 4), 12))
def cg_f018_rnd_intensity_core77_2nd_v078_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(revenue, assets), 4), 12))
def cg_f018_rnd_intensity_core78_2nd_v079_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(opex, assets), 4), 12))
def cg_f018_rnd_intensity_core79_2nd_v080_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 12))
def cg_f018_rnd_intensity_core80_2nd_v081_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f018_rnd_intensity_core81_2nd_v082_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(rnd, revenue), 4), 4))
def cg_f018_rnd_intensity_core82_2nd_v083_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(rnd, opex), 4), 4))
def cg_f018_rnd_intensity_core83_2nd_v084_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(rnd, assets), 4), 4))
def cg_f018_rnd_intensity_core84_2nd_v085_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(opex, revenue), 4), 4))
def cg_f018_rnd_intensity_core85_2nd_v086_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(rnd, revenue + opex), 4), 4))
def cg_f018_rnd_intensity_core86_2nd_v087_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_log(rnd.abs() + 1.0), 4), 4))
def cg_f018_rnd_intensity_core87_2nd_v088_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(revenue, assets), 4), 4))
def cg_f018_rnd_intensity_core88_2nd_v089_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(opex, assets), 4), 4))
def cg_f018_rnd_intensity_core89_2nd_v090_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 4))
def cg_f018_rnd_intensity_core90_2nd_v091_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f018_rnd_intensity_core91_2nd_v092_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(rnd, revenue), 4), 4))
def cg_f018_rnd_intensity_core92_2nd_v093_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(rnd, opex), 4), 4))
def cg_f018_rnd_intensity_core93_2nd_v094_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(rnd, assets), 4), 4))
def cg_f018_rnd_intensity_core94_2nd_v095_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(opex, revenue), 4), 4))
def cg_f018_rnd_intensity_core95_2nd_v096_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(rnd, revenue + opex), 4), 4))
def cg_f018_rnd_intensity_core96_2nd_v097_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_log(rnd.abs() + 1.0), 4), 4))
def cg_f018_rnd_intensity_core97_2nd_v098_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(revenue, assets), 4), 4))
def cg_f018_rnd_intensity_core98_2nd_v099_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(opex, assets), 4), 4))
def cg_f018_rnd_intensity_core99_2nd_v100_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4))
def cg_f018_rnd_intensity_core100_2nd_v101_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f018_rnd_intensity_core101_2nd_v102_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, revenue), 4), 4))
def cg_f018_rnd_intensity_core102_2nd_v103_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, opex), 4), 4))
def cg_f018_rnd_intensity_core103_2nd_v104_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, assets), 4), 4))
def cg_f018_rnd_intensity_core104_2nd_v105_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(opex, revenue), 4), 4))
def cg_f018_rnd_intensity_core105_2nd_v106_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, revenue + opex), 4), 4))
def cg_f018_rnd_intensity_core106_2nd_v107_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_log(rnd.abs() + 1.0), 4), 4))
def cg_f018_rnd_intensity_core107_2nd_v108_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(revenue, assets), 4), 4))
def cg_f018_rnd_intensity_core108_2nd_v109_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(opex, assets), 4), 4))
def cg_f018_rnd_intensity_core109_2nd_v110_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, _mean(rnd, 8)), 4), 4))
def cg_f018_rnd_intensity_core110_2nd_v111_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f018_rnd_intensity_core111_2nd_v112_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, revenue), 8), 8))
def cg_f018_rnd_intensity_core112_2nd_v113_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, opex), 8), 8))
def cg_f018_rnd_intensity_core113_2nd_v114_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, assets), 8), 8))
def cg_f018_rnd_intensity_core114_2nd_v115_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(opex, revenue), 8), 8))
def cg_f018_rnd_intensity_core115_2nd_v116_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, revenue + opex), 8), 8))
def cg_f018_rnd_intensity_core116_2nd_v117_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_log(rnd.abs() + 1.0), 8), 8))
def cg_f018_rnd_intensity_core117_2nd_v118_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(revenue, assets), 8), 8))
def cg_f018_rnd_intensity_core118_2nd_v119_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(opex, assets), 8), 8))
def cg_f018_rnd_intensity_core119_2nd_v120_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_mean(_safe_div(rnd, _mean(rnd, 8)), 8), 8))
def cg_f018_rnd_intensity_core120_2nd_v121_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f018_rnd_intensity_core121_2nd_v122_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(rnd, revenue), 4), 4))
def cg_f018_rnd_intensity_core122_2nd_v123_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(rnd, opex), 4), 4))
def cg_f018_rnd_intensity_core123_2nd_v124_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(rnd, assets), 4), 4))
def cg_f018_rnd_intensity_core124_2nd_v125_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(opex, revenue), 4), 4))
def cg_f018_rnd_intensity_core125_2nd_v126_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(rnd, revenue + opex), 4), 4))
def cg_f018_rnd_intensity_core126_2nd_v127_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_log(rnd.abs() + 1.0), 4), 4))
def cg_f018_rnd_intensity_core127_2nd_v128_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(revenue, assets), 4), 4))
def cg_f018_rnd_intensity_core128_2nd_v129_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(opex, assets), 4), 4))
def cg_f018_rnd_intensity_core129_2nd_v130_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_mean(_safe_div(rnd, _mean(rnd, 8)), 4), 4))
def cg_f018_rnd_intensity_core130_2nd_v131_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f018_rnd_intensity_core131_2nd_v132_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(rnd, revenue), 4), 4), 8))
def cg_f018_rnd_intensity_core132_2nd_v133_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(rnd, opex), 4), 4), 8))
def cg_f018_rnd_intensity_core133_2nd_v134_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(rnd, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core134_2nd_v135_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(opex, revenue), 4), 4), 8))
def cg_f018_rnd_intensity_core135_2nd_v136_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(rnd, revenue + opex), 4), 4), 8))
def cg_f018_rnd_intensity_core136_2nd_v137_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f018_rnd_intensity_core137_2nd_v138_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(revenue, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core138_2nd_v139_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(opex, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core139_2nd_v140_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_mean(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 8))
def cg_f018_rnd_intensity_core140_2nd_v141_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f018_rnd_intensity_core141_2nd_v142_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, revenue), 4), 4), 12))
def cg_f018_rnd_intensity_core142_2nd_v143_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, opex), 4), 4), 12))
def cg_f018_rnd_intensity_core143_2nd_v144_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core144_2nd_v145_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(opex, revenue), 4), 4), 12))
def cg_f018_rnd_intensity_core145_2nd_v146_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, revenue + opex), 4), 4), 12))
def cg_f018_rnd_intensity_core146_2nd_v147_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f018_rnd_intensity_core147_2nd_v148_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core148_2nd_v149_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(opex, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core149_2nd_v150_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 12))