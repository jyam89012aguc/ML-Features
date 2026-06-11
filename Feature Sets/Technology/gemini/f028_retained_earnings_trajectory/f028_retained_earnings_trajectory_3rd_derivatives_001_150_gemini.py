import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f028_retained_earnings_trajectory_core00_3rd_v001_signal(retearn, equity, assets):
    return _clean(_diff(_diff(retearn, 4), 4))
def cg_f028_retained_earnings_trajectory_core01_3rd_v002_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core02_3rd_v003_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core03_3rd_v004_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core04_3rd_v005_signal(retearn, equity, assets):
    return _clean(_diff(_diff(retearn - equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core05_3rd_v006_signal(retearn, equity, assets):
    return _clean(_diff(_diff(retearn - assets, 4), 4))
def cg_f028_retained_earnings_trajectory_core06_3rd_v007_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core07_3rd_v008_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_z(retearn, 8), 4), 4))
def cg_f028_retained_earnings_trajectory_core08_3rd_v009_signal(retearn, equity, assets):
    return _clean(_diff(_diff(retearn + equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core09_3rd_v010_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core10_3rd_v011_signal(retearn, equity, assets):
    return _clean(_slope(_diff(retearn, 4), 8))
def cg_f028_retained_earnings_trajectory_core11_3rd_v012_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core12_3rd_v013_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core13_3rd_v014_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core14_3rd_v015_signal(retearn, equity, assets):
    return _clean(_slope(_diff(retearn - equity, 4), 8))
def cg_f028_retained_earnings_trajectory_core15_3rd_v016_signal(retearn, equity, assets):
    return _clean(_slope(_diff(retearn - assets, 4), 8))
def cg_f028_retained_earnings_trajectory_core16_3rd_v017_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_log(retearn.abs() + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core17_3rd_v018_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_z(retearn, 8), 4), 8))
def cg_f028_retained_earnings_trajectory_core18_3rd_v019_signal(retearn, equity, assets):
    return _clean(_slope(_diff(retearn + equity, 4), 8))
def cg_f028_retained_earnings_trajectory_core19_3rd_v020_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 8))
def cg_f028_retained_earnings_trajectory_core20_3rd_v021_signal(retearn, equity, assets):
    return _clean(_diff(_slope(retearn, 4), 4))
def cg_f028_retained_earnings_trajectory_core21_3rd_v022_signal(retearn, equity, assets):
    return _clean(_diff(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core22_3rd_v023_signal(retearn, equity, assets):
    return _clean(_diff(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core23_3rd_v024_signal(retearn, equity, assets):
    return _clean(_diff(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core24_3rd_v025_signal(retearn, equity, assets):
    return _clean(_diff(_slope(retearn - equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core25_3rd_v026_signal(retearn, equity, assets):
    return _clean(_diff(_slope(retearn - assets, 4), 4))
def cg_f028_retained_earnings_trajectory_core26_3rd_v027_signal(retearn, equity, assets):
    return _clean(_diff(_slope(_log(retearn.abs() + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core27_3rd_v028_signal(retearn, equity, assets):
    return _clean(_diff(_slope(_z(retearn, 8), 4), 4))
def cg_f028_retained_earnings_trajectory_core28_3rd_v029_signal(retearn, equity, assets):
    return _clean(_diff(_slope(retearn + equity, 4), 4))
def cg_f028_retained_earnings_trajectory_core29_3rd_v030_signal(retearn, equity, assets):
    return _clean(_diff(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 4))
def cg_f028_retained_earnings_trajectory_core30_3rd_v031_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(retearn, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core31_3rd_v032_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core32_3rd_v033_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core33_3rd_v034_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core34_3rd_v035_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(retearn - equity, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core35_3rd_v036_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(retearn - assets, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core36_3rd_v037_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core37_3rd_v038_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(_z(retearn, 8), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core38_3rd_v039_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(retearn + equity, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core39_3rd_v040_signal(retearn, equity, assets):
    return _clean(_z(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core40_3rd_v041_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(retearn, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core41_3rd_v042_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core42_3rd_v043_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core43_3rd_v044_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core44_3rd_v045_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(retearn - equity, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core45_3rd_v046_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(retearn - assets, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core46_3rd_v047_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_log(retearn.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core47_3rd_v048_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_z(retearn, 8), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core48_3rd_v049_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(retearn + equity, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core49_3rd_v050_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core50_3rd_v051_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(retearn, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core51_3rd_v052_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core52_3rd_v053_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core53_3rd_v054_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core54_3rd_v055_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(retearn - equity, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core55_3rd_v056_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(retearn - assets, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core56_3rd_v057_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(_log(retearn.abs() + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core57_3rd_v058_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(_z(retearn, 8), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core58_3rd_v059_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(retearn + equity, 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core59_3rd_v060_signal(retearn, equity, assets):
    return _clean(_z(_diff(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core60_3rd_v061_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(retearn, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core61_3rd_v062_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core62_3rd_v063_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core63_3rd_v064_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core64_3rd_v065_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(retearn - equity, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core65_3rd_v066_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(retearn - assets, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core66_3rd_v067_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core67_3rd_v068_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(_z(retearn, 8), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core68_3rd_v069_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(retearn + equity, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core69_3rd_v070_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core70_3rd_v071_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(retearn, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core71_3rd_v072_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core72_3rd_v073_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core73_3rd_v074_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core74_3rd_v075_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(retearn - equity, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core75_3rd_v076_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(retearn - assets, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core76_3rd_v077_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(_log(retearn.abs() + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core77_3rd_v078_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(_z(retearn, 8), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core78_3rd_v079_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(retearn + equity, 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core79_3rd_v080_signal(retearn, equity, assets):
    return _clean(_rank(_slope(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 8), 12))
def cg_f028_retained_earnings_trajectory_core80_3rd_v081_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(retearn, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core81_3rd_v082_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core82_3rd_v083_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core83_3rd_v084_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core84_3rd_v085_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(retearn - equity, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core85_3rd_v086_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(retearn - assets, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core86_3rd_v087_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(_log(retearn.abs() + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core87_3rd_v088_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(_z(retearn, 8), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core88_3rd_v089_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(retearn + equity, 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core89_3rd_v090_signal(retearn, equity, assets):
    return _clean(_rank(_diff(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 4), 12))
def cg_f028_retained_earnings_trajectory_core90_3rd_v091_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(retearn, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core91_3rd_v092_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core92_3rd_v093_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core93_3rd_v094_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core94_3rd_v095_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(retearn - equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core95_3rd_v096_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(retearn - assets, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core96_3rd_v097_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core97_3rd_v098_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(_z(retearn, 8), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core98_3rd_v099_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(retearn + equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core99_3rd_v100_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core100_3rd_v101_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(retearn, 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core101_3rd_v102_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core102_3rd_v103_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core103_3rd_v104_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core104_3rd_v105_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(retearn - equity, 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core105_3rd_v106_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(retearn - assets, 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core106_3rd_v107_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(_log(retearn.abs() + 1.0), 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core107_3rd_v108_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(_z(retearn, 8), 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core108_3rd_v109_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(retearn + equity, 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core109_3rd_v110_signal(retearn, equity, assets):
    return _clean(_mean(_slope(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 8), 4))
def cg_f028_retained_earnings_trajectory_core110_3rd_v111_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(retearn, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core111_3rd_v112_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core112_3rd_v113_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core113_3rd_v114_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core114_3rd_v115_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(retearn - equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core115_3rd_v116_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(retearn - assets, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core116_3rd_v117_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(_log(retearn.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core117_3rd_v118_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(_z(retearn, 8), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core118_3rd_v119_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(retearn + equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core119_3rd_v120_signal(retearn, equity, assets):
    return _clean(_mean(_diff(_slope(_safe_div(retearn, equity + assets + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core120_3rd_v121_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(retearn, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core121_3rd_v122_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core122_3rd_v123_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core123_3rd_v124_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core124_3rd_v125_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(retearn - equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core125_3rd_v126_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(retearn - assets, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core126_3rd_v127_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core127_3rd_v128_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(_z(retearn, 8), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core128_3rd_v129_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(retearn + equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core129_3rd_v130_signal(retearn, equity, assets):
    return _clean(_slope(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core130_3rd_v131_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(retearn, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core131_3rd_v132_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core132_3rd_v133_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core133_3rd_v134_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core134_3rd_v135_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(retearn - equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core135_3rd_v136_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(retearn - assets, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core136_3rd_v137_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core137_3rd_v138_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(_z(retearn, 8), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core138_3rd_v139_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(retearn + equity, 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core139_3rd_v140_signal(retearn, equity, assets):
    return _clean(_diff(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4), 4))
def cg_f028_retained_earnings_trajectory_core140_3rd_v141_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(retearn, 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core141_3rd_v142_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(retearn, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core142_3rd_v143_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(retearn, assets.abs() + 1.0), 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core143_3rd_v144_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core144_3rd_v145_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(retearn - equity, 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core145_3rd_v146_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(retearn - assets, 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core146_3rd_v147_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(_log(retearn.abs() + 1.0), 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core147_3rd_v148_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(_z(retearn, 8), 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core148_3rd_v149_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(retearn + equity, 4), 4), 4), 8))
def cg_f028_retained_earnings_trajectory_core149_3rd_v150_signal(retearn, equity, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(retearn, equity + assets + 1.0), 4), 4), 4), 8))