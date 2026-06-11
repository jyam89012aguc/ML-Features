import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f028_retained_earnings_trajectory_core00_2nd_v001_signal(retearn, equity, assets):
    return _clean(_slope(retearn, 4))
def cg_f028_retained_earnings_trajectory_core01_2nd_v002_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(retearn, equity.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core02_2nd_v003_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(retearn, assets.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core03_2nd_v004_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(equity, assets.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core04_2nd_v005_signal(retearn, equity, assets):
    return _clean(_slope(retearn - equity, 4))
def cg_f028_retained_earnings_trajectory_core05_2nd_v006_signal(retearn, equity, assets):
    return _clean(_slope(retearn - assets, 4))
def cg_f028_retained_earnings_trajectory_core06_2nd_v007_signal(retearn, equity, assets):
    return _clean(_slope(_log(retearn.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core07_2nd_v008_signal(retearn, equity, assets):
    return _clean(_slope(_z(retearn, 8), 4))
def cg_f028_retained_earnings_trajectory_core08_2nd_v009_signal(retearn, equity, assets):
    return _clean(_slope(retearn + equity, 4))
def cg_f028_retained_earnings_trajectory_core09_2nd_v010_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(retearn, equity + assets + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core10_2nd_v011_signal(retearn, equity, assets):
    return _clean(_slope(retearn, 8))
def cg_f028_retained_earnings_trajectory_core11_2nd_v012_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(retearn, equity.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core12_2nd_v013_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(retearn, assets.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core13_2nd_v014_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(equity, assets.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core14_2nd_v015_signal(retearn, equity, assets):
    return _clean(_slope(retearn - equity, 8))
def cg_f028_retained_earnings_trajectory_core15_2nd_v016_signal(retearn, equity, assets):
    return _clean(_slope(retearn - assets, 8))
def cg_f028_retained_earnings_trajectory_core16_2nd_v017_signal(retearn, equity, assets):
    return _clean(_slope(_log(retearn.abs() + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core17_2nd_v018_signal(retearn, equity, assets):
    return _clean(_slope(_z(retearn, 8), 8))
def cg_f028_retained_earnings_trajectory_core18_2nd_v019_signal(retearn, equity, assets):
    return _clean(_slope(retearn + equity, 8))
def cg_f028_retained_earnings_trajectory_core19_2nd_v020_signal(retearn, equity, assets):
    return _clean(_slope(_safe_div(retearn, equity + assets + 1.0), 8))
def cg_f028_retained_earnings_trajectory_core20_2nd_v021_signal(retearn, equity, assets):
    return _clean(_diff(retearn, 4))
def cg_f028_retained_earnings_trajectory_core21_2nd_v022_signal(retearn, equity, assets):
    return _clean(_diff(_safe_div(retearn, equity.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core22_2nd_v023_signal(retearn, equity, assets):
    return _clean(_diff(_safe_div(retearn, assets.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core23_2nd_v024_signal(retearn, equity, assets):
    return _clean(_diff(_safe_div(equity, assets.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core24_2nd_v025_signal(retearn, equity, assets):
    return _clean(_diff(retearn - equity, 4))
def cg_f028_retained_earnings_trajectory_core25_2nd_v026_signal(retearn, equity, assets):
    return _clean(_diff(retearn - assets, 4))
def cg_f028_retained_earnings_trajectory_core26_2nd_v027_signal(retearn, equity, assets):
    return _clean(_diff(_log(retearn.abs() + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core27_2nd_v028_signal(retearn, equity, assets):
    return _clean(_diff(_z(retearn, 8), 4))
def cg_f028_retained_earnings_trajectory_core28_2nd_v029_signal(retearn, equity, assets):
    return _clean(_diff(retearn + equity, 4))
def cg_f028_retained_earnings_trajectory_core29_2nd_v030_signal(retearn, equity, assets):
    return _clean(_diff(_safe_div(retearn, equity + assets + 1.0), 4))
def cg_f028_retained_earnings_trajectory_core30_2nd_v031_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn, 4), 8))
def cg_f028_retained_earnings_trajectory_core31_2nd_v032_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core32_2nd_v033_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core33_2nd_v034_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core34_2nd_v035_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn - equity, 4), 8))
def cg_f028_retained_earnings_trajectory_core35_2nd_v036_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn - assets, 4), 8))
def cg_f028_retained_earnings_trajectory_core36_2nd_v037_signal(retearn, equity, assets):
    return _clean(_z(_slope(_log(retearn.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core37_2nd_v038_signal(retearn, equity, assets):
    return _clean(_z(_slope(_z(retearn, 8), 4), 8))
def cg_f028_retained_earnings_trajectory_core38_2nd_v039_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn + equity, 4), 8))
def cg_f028_retained_earnings_trajectory_core39_2nd_v040_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core40_2nd_v041_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn, 8), 12))
def cg_f028_retained_earnings_trajectory_core41_2nd_v042_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(retearn, equity.abs() + 1.0), 8), 12))
def cg_f028_retained_earnings_trajectory_core42_2nd_v043_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(retearn, assets.abs() + 1.0), 8), 12))
def cg_f028_retained_earnings_trajectory_core43_2nd_v044_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(equity, assets.abs() + 1.0), 8), 12))
def cg_f028_retained_earnings_trajectory_core44_2nd_v045_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn - equity, 8), 12))
def cg_f028_retained_earnings_trajectory_core45_2nd_v046_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn - assets, 8), 12))
def cg_f028_retained_earnings_trajectory_core46_2nd_v047_signal(retearn, equity, assets):
    return _clean(_z(_slope(_log(retearn.abs() + 1.0), 8), 12))
def cg_f028_retained_earnings_trajectory_core47_2nd_v048_signal(retearn, equity, assets):
    return _clean(_z(_slope(_z(retearn, 8), 8), 12))
def cg_f028_retained_earnings_trajectory_core48_2nd_v049_signal(retearn, equity, assets):
    return _clean(_z(_slope(retearn + equity, 8), 12))
def cg_f028_retained_earnings_trajectory_core49_2nd_v050_signal(retearn, equity, assets):
    return _clean(_z(_slope(_safe_div(retearn, equity + assets + 1.0), 8), 12))
def cg_f028_retained_earnings_trajectory_core50_2nd_v051_signal(retearn, equity, assets):
    return _clean(_z(_diff(retearn, 4), 8))
def cg_f028_retained_earnings_trajectory_core51_2nd_v052_signal(retearn, equity, assets):
    return _clean(_z(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core52_2nd_v053_signal(retearn, equity, assets):
    return _clean(_z(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core53_2nd_v054_signal(retearn, equity, assets):
    return _clean(_z(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core54_2nd_v055_signal(retearn, equity, assets):
    return _clean(_z(_diff(retearn - equity, 4), 8))
def cg_f028_retained_earnings_trajectory_core55_2nd_v056_signal(retearn, equity, assets):
    return _clean(_z(_diff(retearn - assets, 4), 8))
def cg_f028_retained_earnings_trajectory_core56_2nd_v057_signal(retearn, equity, assets):
    return _clean(_z(_diff(_log(retearn.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core57_2nd_v058_signal(retearn, equity, assets):
    return _clean(_z(_diff(_z(retearn, 8), 4), 8))
def cg_f028_retained_earnings_trajectory_core58_2nd_v059_signal(retearn, equity, assets):
    return _clean(_z(_diff(retearn + equity, 4), 8))
def cg_f028_retained_earnings_trajectory_core59_2nd_v060_signal(retearn, equity, assets):
    return _clean(_z(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core60_2nd_v061_signal(retearn, equity, assets):
    return _clean(_rank(_slope(retearn, 4), 12))
def cg_f028_retained_earnings_trajectory_core61_2nd_v062_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core62_2nd_v063_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core63_2nd_v064_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core64_2nd_v065_signal(retearn, equity, assets):
    return _clean(_rank(_slope(retearn - equity, 4), 12))
def cg_f028_retained_earnings_trajectory_core65_2nd_v066_signal(retearn, equity, assets):
    return _clean(_rank(_slope(retearn - assets, 4), 12))
def cg_f028_retained_earnings_trajectory_core66_2nd_v067_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_log(retearn.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core67_2nd_v068_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_z(retearn, 8), 4), 12))
def cg_f028_retained_earnings_trajectory_core68_2nd_v069_signal(retearn, equity, assets):
    return _clean(_rank(_slope(retearn + equity, 4), 12))
def cg_f028_retained_earnings_trajectory_core69_2nd_v070_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core70_2nd_v071_signal(retearn, equity, assets):
    return _clean(_rank(_diff(retearn, 4), 12))
def cg_f028_retained_earnings_trajectory_core71_2nd_v072_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core72_2nd_v073_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core73_2nd_v074_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core74_2nd_v075_signal(retearn, equity, assets):
    return _clean(_rank(_diff(retearn - equity, 4), 12))
def cg_f028_retained_earnings_trajectory_core75_2nd_v076_signal(retearn, equity, assets):
    return _clean(_rank(_diff(retearn - assets, 4), 12))
def cg_f028_retained_earnings_trajectory_core76_2nd_v077_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_log(retearn.abs() + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core77_2nd_v078_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_z(retearn, 8), 4), 12))
def cg_f028_retained_earnings_trajectory_core78_2nd_v079_signal(retearn, equity, assets):
    return _clean(_rank(_diff(retearn + equity, 4), 12))
def cg_f028_retained_earnings_trajectory_core79_2nd_v080_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 12))
def cg_f028_retained_earnings_trajectory_core80_2nd_v081_signal(retearn, equity, assets):
    return _clean(_mean(_slope(retearn, 4), 4))
def cg_f028_retained_earnings_trajectory_core81_2nd_v082_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core82_2nd_v083_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core83_2nd_v084_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core84_2nd_v085_signal(retearn, equity, assets):
    return _clean(_mean(_slope(retearn - equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core85_2nd_v086_signal(retearn, equity, assets):
    return _clean(_mean(_slope(retearn - assets, 4), 4))
def cg_f028_retained_earnings_trajectory_core86_2nd_v087_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_log(retearn.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core87_2nd_v088_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_z(retearn, 8), 4), 4))
def cg_f028_retained_earnings_trajectory_core88_2nd_v089_signal(retearn, equity, assets):
    return _clean(_mean(_slope(retearn + equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core89_2nd_v090_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core90_2nd_v091_signal(retearn, equity, assets):
    return _clean(_mean(_diff(retearn, 4), 4))
def cg_f028_retained_earnings_trajectory_core91_2nd_v092_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core92_2nd_v093_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core93_2nd_v094_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core94_2nd_v095_signal(retearn, equity, assets):
    return _clean(_mean(_diff(retearn - equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core95_2nd_v096_signal(retearn, equity, assets):
    return _clean(_mean(_diff(retearn - assets, 4), 4))
def cg_f028_retained_earnings_trajectory_core96_2nd_v097_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_log(retearn.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core97_2nd_v098_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_z(retearn, 8), 4), 4))
def cg_f028_retained_earnings_trajectory_core98_2nd_v099_signal(retearn, equity, assets):
    return _clean(_mean(_diff(retearn + equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core99_2nd_v100_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core100_2nd_v101_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn, 4), 4))
def cg_f028_retained_earnings_trajectory_core101_2nd_v102_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(retearn, equity.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core102_2nd_v103_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(retearn, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core103_2nd_v104_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core104_2nd_v105_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn - equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core105_2nd_v106_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn - assets, 4), 4))
def cg_f028_retained_earnings_trajectory_core106_2nd_v107_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_log(retearn.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core107_2nd_v108_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_z(retearn, 8), 4), 4))
def cg_f028_retained_earnings_trajectory_core108_2nd_v109_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn + equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core109_2nd_v110_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(retearn, equity + assets + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core110_2nd_v111_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn, 8), 8))
def cg_f028_retained_earnings_trajectory_core111_2nd_v112_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(retearn, equity.abs() + 1.0), 8), 8))
def cg_f028_retained_earnings_trajectory_core112_2nd_v113_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(retearn, assets.abs() + 1.0), 8), 8))
def cg_f028_retained_earnings_trajectory_core113_2nd_v114_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(equity, assets.abs() + 1.0), 8), 8))
def cg_f028_retained_earnings_trajectory_core114_2nd_v115_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn - equity, 8), 8))
def cg_f028_retained_earnings_trajectory_core115_2nd_v116_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn - assets, 8), 8))
def cg_f028_retained_earnings_trajectory_core116_2nd_v117_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_log(retearn.abs() + 1.0), 8), 8))
def cg_f028_retained_earnings_trajectory_core117_2nd_v118_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_z(retearn, 8), 8), 8))
def cg_f028_retained_earnings_trajectory_core118_2nd_v119_signal(retearn, equity, assets):
    return _clean(_slope(_mean(retearn + equity, 8), 8))
def cg_f028_retained_earnings_trajectory_core119_2nd_v120_signal(retearn, equity, assets):
    return _clean(_slope(_mean(_safe_div(retearn, equity + assets + 1.0), 8), 8))
def cg_f028_retained_earnings_trajectory_core120_2nd_v121_signal(retearn, equity, assets):
    return _clean(_diff(_mean(retearn, 4), 4))
def cg_f028_retained_earnings_trajectory_core121_2nd_v122_signal(retearn, equity, assets):
    return _clean(_diff(_mean(_safe_div(retearn, equity.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core122_2nd_v123_signal(retearn, equity, assets):
    return _clean(_diff(_mean(_safe_div(retearn, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core123_2nd_v124_signal(retearn, equity, assets):
    return _clean(_diff(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core124_2nd_v125_signal(retearn, equity, assets):
    return _clean(_diff(_mean(retearn - equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core125_2nd_v126_signal(retearn, equity, assets):
    return _clean(_diff(_mean(retearn - assets, 4), 4))
def cg_f028_retained_earnings_trajectory_core126_2nd_v127_signal(retearn, equity, assets):
    return _clean(_diff(_mean(_log(retearn.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core127_2nd_v128_signal(retearn, equity, assets):
    return _clean(_diff(_mean(_z(retearn, 8), 4), 4))
def cg_f028_retained_earnings_trajectory_core128_2nd_v129_signal(retearn, equity, assets):
    return _clean(_diff(_mean(retearn + equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core129_2nd_v130_signal(retearn, equity, assets):
    return _clean(_diff(_mean(_safe_div(retearn, equity + assets + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core130_2nd_v131_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(retearn, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core131_2nd_v132_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core132_2nd_v133_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core133_2nd_v134_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core134_2nd_v135_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(retearn - equity, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core135_2nd_v136_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(retearn - assets, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core136_2nd_v137_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(_log(retearn.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core137_2nd_v138_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(_z(retearn, 8), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core138_2nd_v139_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(retearn + equity, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core139_2nd_v140_signal(retearn, equity, assets):
    return _clean(_z(_diff(_mean(_safe_div(retearn, equity + assets + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core140_2nd_v141_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(retearn, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core141_2nd_v142_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core142_2nd_v143_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core143_2nd_v144_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core144_2nd_v145_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(retearn - equity, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core145_2nd_v146_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(retearn - assets, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core146_2nd_v147_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(_log(retearn.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core147_2nd_v148_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(_z(retearn, 8), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core148_2nd_v149_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(retearn + equity, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core149_2nd_v150_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_mean(_safe_div(retearn, equity + assets + 1.0), 4), 4), 12))