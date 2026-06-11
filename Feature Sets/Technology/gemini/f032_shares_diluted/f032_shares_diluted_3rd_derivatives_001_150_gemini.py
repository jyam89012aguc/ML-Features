import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f032_shares_diluted_core00_3rd_v001_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(shareswa, 4), 4))
def cg_f032_shares_diluted_core01_3rd_v002_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(shareswadil, 4), 4))
def cg_f032_shares_diluted_core02_3rd_v003_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core03_3rd_v004_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core04_3rd_v005_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(sharesbas, 4), 4))
def cg_f032_shares_diluted_core05_3rd_v006_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core06_3rd_v007_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core07_3rd_v008_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core08_3rd_v009_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core09_3rd_v010_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_z(shareswadil, 8), 4), 4))
def cg_f032_shares_diluted_core10_3rd_v011_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(shareswa, 4), 8))
def cg_f032_shares_diluted_core11_3rd_v012_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(shareswadil, 4), 8))
def cg_f032_shares_diluted_core12_3rd_v013_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(shareswadil - shareswa, 4), 8))
def cg_f032_shares_diluted_core13_3rd_v014_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core14_3rd_v015_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(sharesbas, 4), 8))
def cg_f032_shares_diluted_core15_3rd_v016_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core16_3rd_v017_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 8))
def cg_f032_shares_diluted_core17_3rd_v018_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(shareswadil - shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core18_3rd_v019_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_slope(shareswadil, 4), 4), 8))
def cg_f032_shares_diluted_core19_3rd_v020_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_z(shareswadil, 8), 4), 8))
def cg_f032_shares_diluted_core20_3rd_v021_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(shareswa, 4), 4))
def cg_f032_shares_diluted_core21_3rd_v022_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(shareswadil, 4), 4))
def cg_f032_shares_diluted_core22_3rd_v023_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(shareswadil - shareswa, 4), 4))
def cg_f032_shares_diluted_core23_3rd_v024_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core24_3rd_v025_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(sharesbas, 4), 4))
def cg_f032_shares_diluted_core25_3rd_v026_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core26_3rd_v027_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4))
def cg_f032_shares_diluted_core27_3rd_v028_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core28_3rd_v029_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core29_3rd_v030_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_slope(_z(shareswadil, 8), 4), 4))
def cg_f032_shares_diluted_core30_3rd_v031_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core31_3rd_v032_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(shareswadil, 4), 4), 8))
def cg_f032_shares_diluted_core32_3rd_v033_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(shareswadil - shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core33_3rd_v034_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core34_3rd_v035_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(sharesbas, 4), 4), 8))
def cg_f032_shares_diluted_core35_3rd_v036_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core36_3rd_v037_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core37_3rd_v038_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 8))
def cg_f032_shares_diluted_core38_3rd_v039_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(_slope(shareswadil, 4), 4), 4), 8))
def cg_f032_shares_diluted_core39_3rd_v040_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_diff(_z(shareswadil, 8), 4), 4), 8))
def cg_f032_shares_diluted_core40_3rd_v041_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(shareswa, 4), 8), 12))
def cg_f032_shares_diluted_core41_3rd_v042_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(shareswadil, 4), 8), 12))
def cg_f032_shares_diluted_core42_3rd_v043_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(shareswadil - shareswa, 4), 8), 12))
def cg_f032_shares_diluted_core43_3rd_v044_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 8), 12))
def cg_f032_shares_diluted_core44_3rd_v045_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(sharesbas, 4), 8), 12))
def cg_f032_shares_diluted_core45_3rd_v046_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f032_shares_diluted_core46_3rd_v047_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f032_shares_diluted_core47_3rd_v048_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(shareswadil - shareswa, 4), 4), 8), 12))
def cg_f032_shares_diluted_core48_3rd_v049_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_slope(shareswadil, 4), 4), 8), 12))
def cg_f032_shares_diluted_core49_3rd_v050_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_z(shareswadil, 8), 4), 8), 12))
def cg_f032_shares_diluted_core50_3rd_v051_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core51_3rd_v052_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(shareswadil, 4), 4), 8))
def cg_f032_shares_diluted_core52_3rd_v053_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(shareswadil - shareswa, 4), 4), 8))
def cg_f032_shares_diluted_core53_3rd_v054_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core54_3rd_v055_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(sharesbas, 4), 4), 8))
def cg_f032_shares_diluted_core55_3rd_v056_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core56_3rd_v057_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f032_shares_diluted_core57_3rd_v058_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(_diff(shareswadil - shareswa, 4), 4), 4), 8))
def cg_f032_shares_diluted_core58_3rd_v059_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(_slope(shareswadil, 4), 4), 4), 8))
def cg_f032_shares_diluted_core59_3rd_v060_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_diff(_slope(_z(shareswadil, 8), 4), 4), 8))
def cg_f032_shares_diluted_core60_3rd_v061_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core61_3rd_v062_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(shareswadil, 4), 4), 12))
def cg_f032_shares_diluted_core62_3rd_v063_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(shareswadil - shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core63_3rd_v064_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core64_3rd_v065_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(sharesbas, 4), 4), 12))
def cg_f032_shares_diluted_core65_3rd_v066_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core66_3rd_v067_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core67_3rd_v068_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 12))
def cg_f032_shares_diluted_core68_3rd_v069_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(_slope(shareswadil, 4), 4), 4), 12))
def cg_f032_shares_diluted_core69_3rd_v070_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_diff(_z(shareswadil, 8), 4), 4), 12))
def cg_f032_shares_diluted_core70_3rd_v071_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(shareswa, 4), 8), 12))
def cg_f032_shares_diluted_core71_3rd_v072_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(shareswadil, 4), 8), 12))
def cg_f032_shares_diluted_core72_3rd_v073_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(shareswadil - shareswa, 4), 8), 12))
def cg_f032_shares_diluted_core73_3rd_v074_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 8), 12))
def cg_f032_shares_diluted_core74_3rd_v075_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(sharesbas, 4), 8), 12))
def cg_f032_shares_diluted_core75_3rd_v076_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f032_shares_diluted_core76_3rd_v077_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f032_shares_diluted_core77_3rd_v078_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(_diff(shareswadil - shareswa, 4), 4), 8), 12))
def cg_f032_shares_diluted_core78_3rd_v079_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(_slope(shareswadil, 4), 4), 8), 12))
def cg_f032_shares_diluted_core79_3rd_v080_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_slope(_diff(_z(shareswadil, 8), 4), 8), 12))
def cg_f032_shares_diluted_core80_3rd_v081_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core81_3rd_v082_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(shareswadil, 4), 4), 12))
def cg_f032_shares_diluted_core82_3rd_v083_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(shareswadil - shareswa, 4), 4), 12))
def cg_f032_shares_diluted_core83_3rd_v084_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core84_3rd_v085_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(sharesbas, 4), 4), 12))
def cg_f032_shares_diluted_core85_3rd_v086_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core86_3rd_v087_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f032_shares_diluted_core87_3rd_v088_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(_diff(shareswadil - shareswa, 4), 4), 4), 12))
def cg_f032_shares_diluted_core88_3rd_v089_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(_slope(shareswadil, 4), 4), 4), 12))
def cg_f032_shares_diluted_core89_3rd_v090_signal(shareswa, shareswadil, sharesbas):
    return _clean(_rank(_diff(_slope(_z(shareswadil, 8), 4), 4), 12))
def cg_f032_shares_diluted_core90_3rd_v091_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core91_3rd_v092_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core92_3rd_v093_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core93_3rd_v094_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core94_3rd_v095_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f032_shares_diluted_core95_3rd_v096_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core96_3rd_v097_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core97_3rd_v098_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 4))
def cg_f032_shares_diluted_core98_3rd_v099_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(_slope(shareswadil, 4), 4), 4), 4))
def cg_f032_shares_diluted_core99_3rd_v100_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_diff(_z(shareswadil, 8), 4), 4), 4))
def cg_f032_shares_diluted_core100_3rd_v101_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(shareswa, 4), 8), 4))
def cg_f032_shares_diluted_core101_3rd_v102_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(shareswadil, 4), 8), 4))
def cg_f032_shares_diluted_core102_3rd_v103_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(shareswadil - shareswa, 4), 8), 4))
def cg_f032_shares_diluted_core103_3rd_v104_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 8), 4))
def cg_f032_shares_diluted_core104_3rd_v105_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(sharesbas, 4), 8), 4))
def cg_f032_shares_diluted_core105_3rd_v106_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 8), 4))
def cg_f032_shares_diluted_core106_3rd_v107_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 8), 4))
def cg_f032_shares_diluted_core107_3rd_v108_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(_diff(shareswadil - shareswa, 4), 4), 8), 4))
def cg_f032_shares_diluted_core108_3rd_v109_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(_slope(shareswadil, 4), 4), 8), 4))
def cg_f032_shares_diluted_core109_3rd_v110_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_slope(_diff(_z(shareswadil, 8), 4), 8), 4))
def cg_f032_shares_diluted_core110_3rd_v111_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core111_3rd_v112_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core112_3rd_v113_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core113_3rd_v114_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core114_3rd_v115_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(sharesbas, 4), 4), 4))
def cg_f032_shares_diluted_core115_3rd_v116_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core116_3rd_v117_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core117_3rd_v118_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(_diff(shareswadil - shareswa, 4), 4), 4), 4))
def cg_f032_shares_diluted_core118_3rd_v119_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(_slope(shareswadil, 4), 4), 4), 4))
def cg_f032_shares_diluted_core119_3rd_v120_signal(shareswa, shareswadil, sharesbas):
    return _clean(_mean(_diff(_slope(_z(shareswadil, 8), 4), 4), 4))
def cg_f032_shares_diluted_core120_3rd_v121_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core121_3rd_v122_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core122_3rd_v123_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core123_3rd_v124_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core124_3rd_v125_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f032_shares_diluted_core125_3rd_v126_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core126_3rd_v127_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core127_3rd_v128_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 4))
def cg_f032_shares_diluted_core128_3rd_v129_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(_slope(shareswadil, 4), 4), 4), 4))
def cg_f032_shares_diluted_core129_3rd_v130_signal(shareswa, shareswadil, sharesbas):
    return _clean(_slope(_diff(_diff(_z(shareswadil, 8), 4), 4), 4))
def cg_f032_shares_diluted_core130_3rd_v131_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core131_3rd_v132_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(shareswadil, 4), 4), 4))
def cg_f032_shares_diluted_core132_3rd_v133_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4))
def cg_f032_shares_diluted_core133_3rd_v134_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core134_3rd_v135_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f032_shares_diluted_core135_3rd_v136_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core136_3rd_v137_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f032_shares_diluted_core137_3rd_v138_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 4))
def cg_f032_shares_diluted_core138_3rd_v139_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(_slope(shareswadil, 4), 4), 4), 4))
def cg_f032_shares_diluted_core139_3rd_v140_signal(shareswa, shareswadil, sharesbas):
    return _clean(_diff(_diff(_diff(_z(shareswadil, 8), 4), 4), 4))
def cg_f032_shares_diluted_core140_3rd_v141_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(shareswa, 4), 4), 4), 8))
def cg_f032_shares_diluted_core141_3rd_v142_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(shareswadil, 4), 4), 4), 8))
def cg_f032_shares_diluted_core142_3rd_v143_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 8))
def cg_f032_shares_diluted_core143_3rd_v144_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(shareswadil, shareswa.abs() + 1.0), 4), 4), 4), 8))
def cg_f032_shares_diluted_core144_3rd_v145_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(sharesbas, 4), 4), 4), 8))
def cg_f032_shares_diluted_core145_3rd_v146_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(shareswa, sharesbas.abs() + 1.0), 4), 4), 4), 8))
def cg_f032_shares_diluted_core146_3rd_v147_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(shareswadil, sharesbas.abs() + 1.0), 4), 4), 4), 8))
def cg_f032_shares_diluted_core147_3rd_v148_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_diff(shareswadil - shareswa, 4), 4), 4), 4), 8))
def cg_f032_shares_diluted_core148_3rd_v149_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_slope(shareswadil, 4), 4), 4), 4), 8))
def cg_f032_shares_diluted_core149_3rd_v150_signal(shareswa, shareswadil, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_z(shareswadil, 8), 4), 4), 4), 8))