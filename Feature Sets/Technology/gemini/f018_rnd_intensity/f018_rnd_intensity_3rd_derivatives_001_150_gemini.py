import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f018_rnd_intensity_core00_3rd_v001_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(rnd, 4), 4))
def cg_f018_rnd_intensity_core01_3rd_v002_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(rnd, revenue), 4), 4))
def cg_f018_rnd_intensity_core02_3rd_v003_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(rnd, opex), 4), 4))
def cg_f018_rnd_intensity_core03_3rd_v004_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(rnd, assets), 4), 4))
def cg_f018_rnd_intensity_core04_3rd_v005_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(opex, revenue), 4), 4))
def cg_f018_rnd_intensity_core05_3rd_v006_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4))
def cg_f018_rnd_intensity_core06_3rd_v007_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4))
def cg_f018_rnd_intensity_core07_3rd_v008_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(revenue, assets), 4), 4))
def cg_f018_rnd_intensity_core08_3rd_v009_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(opex, assets), 4), 4))
def cg_f018_rnd_intensity_core09_3rd_v010_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4))
def cg_f018_rnd_intensity_core10_3rd_v011_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(rnd, 4), 8))
def cg_f018_rnd_intensity_core11_3rd_v012_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(rnd, revenue), 4), 8))
def cg_f018_rnd_intensity_core12_3rd_v013_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(rnd, opex), 4), 8))
def cg_f018_rnd_intensity_core13_3rd_v014_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(rnd, assets), 4), 8))
def cg_f018_rnd_intensity_core14_3rd_v015_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(opex, revenue), 4), 8))
def cg_f018_rnd_intensity_core15_3rd_v016_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(rnd, revenue + opex), 4), 8))
def cg_f018_rnd_intensity_core16_3rd_v017_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8))
def cg_f018_rnd_intensity_core17_3rd_v018_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(revenue, assets), 4), 8))
def cg_f018_rnd_intensity_core18_3rd_v019_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(opex, assets), 4), 8))
def cg_f018_rnd_intensity_core19_3rd_v020_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 8))
def cg_f018_rnd_intensity_core20_3rd_v021_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(rnd, 4), 4))
def cg_f018_rnd_intensity_core21_3rd_v022_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(rnd, revenue), 4), 4))
def cg_f018_rnd_intensity_core22_3rd_v023_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(rnd, opex), 4), 4))
def cg_f018_rnd_intensity_core23_3rd_v024_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(rnd, assets), 4), 4))
def cg_f018_rnd_intensity_core24_3rd_v025_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(opex, revenue), 4), 4))
def cg_f018_rnd_intensity_core25_3rd_v026_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(rnd, revenue + opex), 4), 4))
def cg_f018_rnd_intensity_core26_3rd_v027_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4))
def cg_f018_rnd_intensity_core27_3rd_v028_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(revenue, assets), 4), 4))
def cg_f018_rnd_intensity_core28_3rd_v029_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(opex, assets), 4), 4))
def cg_f018_rnd_intensity_core29_3rd_v030_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 4))
def cg_f018_rnd_intensity_core30_3rd_v031_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(rnd, 4), 4), 8))
def cg_f018_rnd_intensity_core31_3rd_v032_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 8))
def cg_f018_rnd_intensity_core32_3rd_v033_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(rnd, opex), 4), 4), 8))
def cg_f018_rnd_intensity_core33_3rd_v034_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(rnd, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core34_3rd_v035_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(opex, revenue), 4), 4), 8))
def cg_f018_rnd_intensity_core35_3rd_v036_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4), 8))
def cg_f018_rnd_intensity_core36_3rd_v037_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f018_rnd_intensity_core37_3rd_v038_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(revenue, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core38_3rd_v039_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(opex, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core39_3rd_v040_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 8))
def cg_f018_rnd_intensity_core40_3rd_v041_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(rnd, 4), 8), 12))
def cg_f018_rnd_intensity_core41_3rd_v042_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(rnd, revenue), 4), 8), 12))
def cg_f018_rnd_intensity_core42_3rd_v043_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(rnd, opex), 4), 8), 12))
def cg_f018_rnd_intensity_core43_3rd_v044_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(rnd, assets), 4), 8), 12))
def cg_f018_rnd_intensity_core44_3rd_v045_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(opex, revenue), 4), 8), 12))
def cg_f018_rnd_intensity_core45_3rd_v046_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(rnd, revenue + opex), 4), 8), 12))
def cg_f018_rnd_intensity_core46_3rd_v047_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 12))
def cg_f018_rnd_intensity_core47_3rd_v048_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(revenue, assets), 4), 8), 12))
def cg_f018_rnd_intensity_core48_3rd_v049_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(opex, assets), 4), 8), 12))
def cg_f018_rnd_intensity_core49_3rd_v050_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 8), 12))
def cg_f018_rnd_intensity_core50_3rd_v051_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(rnd, 4), 4), 8))
def cg_f018_rnd_intensity_core51_3rd_v052_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(rnd, revenue), 4), 4), 8))
def cg_f018_rnd_intensity_core52_3rd_v053_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(rnd, opex), 4), 4), 8))
def cg_f018_rnd_intensity_core53_3rd_v054_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(rnd, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core54_3rd_v055_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(opex, revenue), 4), 4), 8))
def cg_f018_rnd_intensity_core55_3rd_v056_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(rnd, revenue + opex), 4), 4), 8))
def cg_f018_rnd_intensity_core56_3rd_v057_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f018_rnd_intensity_core57_3rd_v058_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(revenue, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core58_3rd_v059_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(opex, assets), 4), 4), 8))
def cg_f018_rnd_intensity_core59_3rd_v060_signal(rnd, revenue, opex, assets):
    return _clean(_z(_diff(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 8))
def cg_f018_rnd_intensity_core60_3rd_v061_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(rnd, 4), 4), 12))
def cg_f018_rnd_intensity_core61_3rd_v062_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 12))
def cg_f018_rnd_intensity_core62_3rd_v063_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, opex), 4), 4), 12))
def cg_f018_rnd_intensity_core63_3rd_v064_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core64_3rd_v065_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(opex, revenue), 4), 4), 12))
def cg_f018_rnd_intensity_core65_3rd_v066_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4), 12))
def cg_f018_rnd_intensity_core66_3rd_v067_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f018_rnd_intensity_core67_3rd_v068_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(revenue, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core68_3rd_v069_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(opex, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core69_3rd_v070_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 12))
def cg_f018_rnd_intensity_core70_3rd_v071_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(rnd, 4), 8), 12))
def cg_f018_rnd_intensity_core71_3rd_v072_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, revenue), 4), 8), 12))
def cg_f018_rnd_intensity_core72_3rd_v073_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, opex), 4), 8), 12))
def cg_f018_rnd_intensity_core73_3rd_v074_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, assets), 4), 8), 12))
def cg_f018_rnd_intensity_core74_3rd_v075_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(opex, revenue), 4), 8), 12))
def cg_f018_rnd_intensity_core75_3rd_v076_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, revenue + opex), 4), 8), 12))
def cg_f018_rnd_intensity_core76_3rd_v077_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 12))
def cg_f018_rnd_intensity_core77_3rd_v078_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(revenue, assets), 4), 8), 12))
def cg_f018_rnd_intensity_core78_3rd_v079_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(opex, assets), 4), 8), 12))
def cg_f018_rnd_intensity_core79_3rd_v080_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 8), 12))
def cg_f018_rnd_intensity_core80_3rd_v081_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(rnd, 4), 4), 12))
def cg_f018_rnd_intensity_core81_3rd_v082_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, revenue), 4), 4), 12))
def cg_f018_rnd_intensity_core82_3rd_v083_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, opex), 4), 4), 12))
def cg_f018_rnd_intensity_core83_3rd_v084_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core84_3rd_v085_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(opex, revenue), 4), 4), 12))
def cg_f018_rnd_intensity_core85_3rd_v086_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, revenue + opex), 4), 4), 12))
def cg_f018_rnd_intensity_core86_3rd_v087_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f018_rnd_intensity_core87_3rd_v088_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(revenue, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core88_3rd_v089_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(opex, assets), 4), 4), 12))
def cg_f018_rnd_intensity_core89_3rd_v090_signal(rnd, revenue, opex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 12))
def cg_f018_rnd_intensity_core90_3rd_v091_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(rnd, 4), 4), 4))
def cg_f018_rnd_intensity_core91_3rd_v092_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core92_3rd_v093_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4))
def cg_f018_rnd_intensity_core93_3rd_v094_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core94_3rd_v095_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(opex, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core95_3rd_v096_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4), 4))
def cg_f018_rnd_intensity_core96_3rd_v097_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f018_rnd_intensity_core97_3rd_v098_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(revenue, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core98_3rd_v099_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(opex, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core99_3rd_v100_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 4))
def cg_f018_rnd_intensity_core100_3rd_v101_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(rnd, 4), 8), 4))
def cg_f018_rnd_intensity_core101_3rd_v102_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, revenue), 4), 8), 4))
def cg_f018_rnd_intensity_core102_3rd_v103_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, opex), 4), 8), 4))
def cg_f018_rnd_intensity_core103_3rd_v104_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, assets), 4), 8), 4))
def cg_f018_rnd_intensity_core104_3rd_v105_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(opex, revenue), 4), 8), 4))
def cg_f018_rnd_intensity_core105_3rd_v106_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, revenue + opex), 4), 8), 4))
def cg_f018_rnd_intensity_core106_3rd_v107_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 4))
def cg_f018_rnd_intensity_core107_3rd_v108_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(revenue, assets), 4), 8), 4))
def cg_f018_rnd_intensity_core108_3rd_v109_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(opex, assets), 4), 8), 4))
def cg_f018_rnd_intensity_core109_3rd_v110_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 8), 4))
def cg_f018_rnd_intensity_core110_3rd_v111_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(rnd, 4), 4), 4))
def cg_f018_rnd_intensity_core111_3rd_v112_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core112_3rd_v113_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, opex), 4), 4), 4))
def cg_f018_rnd_intensity_core113_3rd_v114_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core114_3rd_v115_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(opex, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core115_3rd_v116_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, revenue + opex), 4), 4), 4))
def cg_f018_rnd_intensity_core116_3rd_v117_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f018_rnd_intensity_core117_3rd_v118_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(revenue, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core118_3rd_v119_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(opex, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core119_3rd_v120_signal(rnd, revenue, opex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 4))
def cg_f018_rnd_intensity_core120_3rd_v121_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(rnd, 4), 4), 4))
def cg_f018_rnd_intensity_core121_3rd_v122_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core122_3rd_v123_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4))
def cg_f018_rnd_intensity_core123_3rd_v124_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core124_3rd_v125_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(opex, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core125_3rd_v126_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4), 4))
def cg_f018_rnd_intensity_core126_3rd_v127_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f018_rnd_intensity_core127_3rd_v128_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(revenue, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core128_3rd_v129_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(opex, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core129_3rd_v130_signal(rnd, revenue, opex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 4))
def cg_f018_rnd_intensity_core130_3rd_v131_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(rnd, 4), 4), 4))
def cg_f018_rnd_intensity_core131_3rd_v132_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core132_3rd_v133_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4))
def cg_f018_rnd_intensity_core133_3rd_v134_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core134_3rd_v135_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(opex, revenue), 4), 4), 4))
def cg_f018_rnd_intensity_core135_3rd_v136_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4), 4))
def cg_f018_rnd_intensity_core136_3rd_v137_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f018_rnd_intensity_core137_3rd_v138_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(revenue, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core138_3rd_v139_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(opex, assets), 4), 4), 4))
def cg_f018_rnd_intensity_core139_3rd_v140_signal(rnd, revenue, opex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 4))
def cg_f018_rnd_intensity_core140_3rd_v141_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(rnd, 4), 4), 4), 8))
def cg_f018_rnd_intensity_core141_3rd_v142_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, revenue), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core142_3rd_v143_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, opex), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core143_3rd_v144_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core144_3rd_v145_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(opex, revenue), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core145_3rd_v146_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, revenue + opex), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core146_3rd_v147_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core147_3rd_v148_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(revenue, assets), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core148_3rd_v149_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(opex, assets), 4), 4), 4), 8))
def cg_f018_rnd_intensity_core149_3rd_v150_signal(rnd, revenue, opex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, _mean(rnd, 8)), 4), 4), 4), 8))