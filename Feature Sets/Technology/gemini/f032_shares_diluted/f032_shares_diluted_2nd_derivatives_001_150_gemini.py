import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f032_shares_diluted_core00_2nd_v001_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(shareswa, 4))
def cg_f032_shares_diluted_core01_2nd_v002_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(shareswadil, 4))
def cg_f032_shares_diluted_core02_2nd_v003_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(shareswadil - shareswa, 4))
def cg_f032_shares_diluted_core03_2nd_v004_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4))
def cg_f032_shares_diluted_core04_2nd_v005_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(sharesbas, 4))
def cg_f032_shares_diluted_core05_2nd_v006_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core06_2nd_v007_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core07_2nd_v008_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core08_2nd_v009_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_slope(shareswadil, 4), 4))
def cg_f032_shares_diluted_core09_2nd_v010_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_z(shareswadil, 8), 4))
def cg_f032_shares_diluted_core10_2nd_v011_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(shareswa, 8))
def cg_f032_shares_diluted_core11_2nd_v012_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(shareswadil, 8))
def cg_f032_shares_diluted_core12_2nd_v013_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(shareswadil - shareswa, 8))
def cg_f032_shares_diluted_core13_2nd_v014_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 8))
def cg_f032_shares_diluted_core14_2nd_v015_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(sharesbas, 8))
def cg_f032_shares_diluted_core15_2nd_v016_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 8))
def cg_f032_shares_diluted_core16_2nd_v017_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 8))
def cg_f032_shares_diluted_core17_2nd_v018_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(shareswadil - shareswa, 4), 8))
def cg_f032_shares_diluted_core18_2nd_v019_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_slope(shareswadil, 4), 8))
def cg_f032_shares_diluted_core19_2nd_v020_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_z(shareswadil, 8), 8))
def cg_f032_shares_diluted_core20_2nd_v021_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(shareswa, 4))
def cg_f032_shares_diluted_core21_2nd_v022_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(shareswadil, 4))
def cg_f032_shares_diluted_core22_2nd_v023_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(shareswadil - shareswa, 4))
def cg_f032_shares_diluted_core23_2nd_v024_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4))
def cg_f032_shares_diluted_core24_2nd_v025_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(sharesbas, 4))
def cg_f032_shares_diluted_core25_2nd_v026_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core26_2nd_v027_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4))
def cg_f032_shares_diluted_core27_2nd_v028_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core28_2nd_v029_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(shareswadil, 4), 4))
def cg_f032_shares_diluted_core29_2nd_v030_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_z(shareswadil, 8), 4))
def cg_f032_shares_diluted_core30_2nd_v031_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(shareswa, 4), 8))
def cg_f032_shares_diluted_core31_2nd_v032_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(shareswadil, 4), 8))
def cg_f032_shares_diluted_core32_2nd_v033_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(shareswadil - shareswa, 4), 8))
def cg_f032_shares_diluted_core33_2nd_v034_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core34_2nd_v035_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(sharesbas, 4), 8))
def cg_f032_shares_diluted_core35_2nd_v036_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core36_2nd_v037_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core37_2nd_v038_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(shareswadil - shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core38_2nd_v039_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_slope(shareswadil, 4), 4), 8))
def cg_f032_shares_diluted_core39_2nd_v040_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_z(shareswadil, 8), 4), 8))
def cg_f032_shares_diluted_core40_2nd_v041_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(shareswa, 8), 12))
def cg_f032_shares_diluted_core41_2nd_v042_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(shareswadil, 8), 12))
def cg_f032_shares_diluted_core42_2nd_v043_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(shareswadil - shareswa, 8), 12))
def cg_f032_shares_diluted_core43_2nd_v044_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 8), 12))
def cg_f032_shares_diluted_core44_2nd_v045_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(sharesbas, 8), 12))
def cg_f032_shares_diluted_core45_2nd_v046_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 8), 12))
def cg_f032_shares_diluted_core46_2nd_v047_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 8), 12))
def cg_f032_shares_diluted_core47_2nd_v048_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(shareswadil - shareswa, 4), 8), 12))
def cg_f032_shares_diluted_core48_2nd_v049_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_slope(shareswadil, 4), 8), 12))
def cg_f032_shares_diluted_core49_2nd_v050_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_z(shareswadil, 8), 8), 12))
def cg_f032_shares_diluted_core50_2nd_v051_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(shareswa, 4), 8))
def cg_f032_shares_diluted_core51_2nd_v052_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(shareswadil, 4), 8))
def cg_f032_shares_diluted_core52_2nd_v053_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(shareswadil - shareswa, 4), 8))
def cg_f032_shares_diluted_core53_2nd_v054_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core54_2nd_v055_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(sharesbas, 4), 8))
def cg_f032_shares_diluted_core55_2nd_v056_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core56_2nd_v057_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core57_2nd_v058_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(shareswadil - shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core58_2nd_v059_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(shareswadil, 4), 4), 8))
def cg_f032_shares_diluted_core59_2nd_v060_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_z(shareswadil, 8), 4), 8))
def cg_f032_shares_diluted_core60_2nd_v061_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(shareswa, 4), 12))
def cg_f032_shares_diluted_core61_2nd_v062_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(shareswadil, 4), 12))
def cg_f032_shares_diluted_core62_2nd_v063_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(shareswadil - shareswa, 4), 12))
def cg_f032_shares_diluted_core63_2nd_v064_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 12))
def cg_f032_shares_diluted_core64_2nd_v065_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(sharesbas, 4), 12))
def cg_f032_shares_diluted_core65_2nd_v066_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 12))
def cg_f032_shares_diluted_core66_2nd_v067_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 12))
def cg_f032_shares_diluted_core67_2nd_v068_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(shareswadil - shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core68_2nd_v069_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_slope(shareswadil, 4), 4), 12))
def cg_f032_shares_diluted_core69_2nd_v070_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_z(shareswadil, 8), 4), 12))
def cg_f032_shares_diluted_core70_2nd_v071_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(shareswa, 4), 12))
def cg_f032_shares_diluted_core71_2nd_v072_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(shareswadil, 4), 12))
def cg_f032_shares_diluted_core72_2nd_v073_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(shareswadil - shareswa, 4), 12))
def cg_f032_shares_diluted_core73_2nd_v074_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 12))
def cg_f032_shares_diluted_core74_2nd_v075_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(sharesbas, 4), 12))
def cg_f032_shares_diluted_core75_2nd_v076_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 12))
def cg_f032_shares_diluted_core76_2nd_v077_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 12))
def cg_f032_shares_diluted_core77_2nd_v078_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(shareswadil - shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core78_2nd_v079_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(shareswadil, 4), 4), 12))
def cg_f032_shares_diluted_core79_2nd_v080_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_z(shareswadil, 8), 4), 12))
def cg_f032_shares_diluted_core80_2nd_v081_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(shareswa, 4), 4))
def cg_f032_shares_diluted_core81_2nd_v082_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(shareswadil, 4), 4))
def cg_f032_shares_diluted_core82_2nd_v083_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core83_2nd_v084_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core84_2nd_v085_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(sharesbas, 4), 4))
def cg_f032_shares_diluted_core85_2nd_v086_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core86_2nd_v087_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core87_2nd_v088_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core88_2nd_v089_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core89_2nd_v090_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_z(shareswadil, 8), 4), 4))
def cg_f032_shares_diluted_core90_2nd_v091_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(shareswa, 4), 4))
def cg_f032_shares_diluted_core91_2nd_v092_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(shareswadil, 4), 4))
def cg_f032_shares_diluted_core92_2nd_v093_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core93_2nd_v094_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core94_2nd_v095_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(sharesbas, 4), 4))
def cg_f032_shares_diluted_core95_2nd_v096_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core96_2nd_v097_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core97_2nd_v098_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core98_2nd_v099_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core99_2nd_v100_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_z(shareswadil, 8), 4), 4))
def cg_f032_shares_diluted_core100_2nd_v101_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(shareswa, 4), 4))
def cg_f032_shares_diluted_core101_2nd_v102_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(shareswadil, 4), 4))
def cg_f032_shares_diluted_core102_2nd_v103_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core103_2nd_v104_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core104_2nd_v105_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(sharesbas, 4), 4))
def cg_f032_shares_diluted_core105_2nd_v106_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core106_2nd_v107_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core107_2nd_v108_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core108_2nd_v109_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core109_2nd_v110_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_z(shareswadil, 8), 4), 4))
def cg_f032_shares_diluted_core110_2nd_v111_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(shareswa, 8), 8))
def cg_f032_shares_diluted_core111_2nd_v112_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(shareswadil, 8), 8))
def cg_f032_shares_diluted_core112_2nd_v113_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(shareswadil - shareswa, 8), 8))
def cg_f032_shares_diluted_core113_2nd_v114_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_safe_div(shareswadil, shareswa.abs() + 1.0), 8), 8))
def cg_f032_shares_diluted_core114_2nd_v115_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(sharesbas, 8), 8))
def cg_f032_shares_diluted_core115_2nd_v116_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_safe_div(shareswa, sharesbas.abs() + 1.0), 8), 8))
def cg_f032_shares_diluted_core116_2nd_v117_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_safe_div(shareswadil, sharesbas.abs() + 1.0), 8), 8))
def cg_f032_shares_diluted_core117_2nd_v118_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_diff(shareswadil - shareswa, 4), 8), 8))
def cg_f032_shares_diluted_core118_2nd_v119_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_slope(shareswadil, 4), 8), 8))
def cg_f032_shares_diluted_core119_2nd_v120_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_mean(_z(shareswadil, 8), 8), 8))
def cg_f032_shares_diluted_core120_2nd_v121_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(shareswa, 4), 4))
def cg_f032_shares_diluted_core121_2nd_v122_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(shareswadil, 4), 4))
def cg_f032_shares_diluted_core122_2nd_v123_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core123_2nd_v124_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core124_2nd_v125_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(sharesbas, 4), 4))
def cg_f032_shares_diluted_core125_2nd_v126_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core126_2nd_v127_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core127_2nd_v128_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core128_2nd_v129_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core129_2nd_v130_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_mean(_z(shareswadil, 8), 4), 4))
def cg_f032_shares_diluted_core130_2nd_v131_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core131_2nd_v132_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(shareswadil, 4), 4), 8))
def cg_f032_shares_diluted_core132_2nd_v133_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(shareswadil - shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core133_2nd_v134_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core134_2nd_v135_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(sharesbas, 4), 4), 8))
def cg_f032_shares_diluted_core135_2nd_v136_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core136_2nd_v137_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core137_2nd_v138_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(_diff(shareswadil - shareswa, 4), 4), 4), 8))
def cg_f032_shares_diluted_core138_2nd_v139_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(_slope(shareswadil, 4), 4), 4), 8))
def cg_f032_shares_diluted_core139_2nd_v140_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_mean(_z(shareswadil, 8), 4), 4), 8))
def cg_f032_shares_diluted_core140_2nd_v141_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core141_2nd_v142_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(shareswadil, 4), 4), 12))
def cg_f032_shares_diluted_core142_2nd_v143_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(shareswadil - shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core143_2nd_v144_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core144_2nd_v145_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(sharesbas, 4), 4), 12))
def cg_f032_shares_diluted_core145_2nd_v146_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core146_2nd_v147_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core147_2nd_v148_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(_diff(shareswadil - shareswa, 4), 4), 4), 12))
def cg_f032_shares_diluted_core148_2nd_v149_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(_slope(shareswadil, 4), 4), 4), 12))
def cg_f032_shares_diluted_core149_2nd_v150_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_mean(_z(shareswadil, 8), 4), 4), 12))