import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f035_buyback_share_reduction_core00_2nd_v001_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(sharesbas, 4), 4))
def cg_f035_buyback_share_reduction_core01_2nd_v002_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core02_2nd_v003_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(ncfcommon, 4))
def cg_f035_buyback_share_reduction_core03_2nd_v004_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core04_2nd_v005_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core05_2nd_v006_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_pct_change(sharesbas, 4), 4))
def cg_f035_buyback_share_reduction_core06_2nd_v007_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_slope(sharesbas, 4), 4))
def cg_f035_buyback_share_reduction_core07_2nd_v008_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_z(ncfcommon, 8), 4))
def cg_f035_buyback_share_reduction_core08_2nd_v009_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(sharesbas - shareswa, 4))
def cg_f035_buyback_share_reduction_core09_2nd_v010_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core10_2nd_v011_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(sharesbas, 4), 8))
def cg_f035_buyback_share_reduction_core11_2nd_v012_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(shareswa, 4), 8))
def cg_f035_buyback_share_reduction_core12_2nd_v013_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(ncfcommon, 8))
def cg_f035_buyback_share_reduction_core13_2nd_v014_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core14_2nd_v015_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core15_2nd_v016_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_pct_change(sharesbas, 4), 8))
def cg_f035_buyback_share_reduction_core16_2nd_v017_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_slope(sharesbas, 4), 8))
def cg_f035_buyback_share_reduction_core17_2nd_v018_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_z(ncfcommon, 8), 8))
def cg_f035_buyback_share_reduction_core18_2nd_v019_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(sharesbas - shareswa, 8))
def cg_f035_buyback_share_reduction_core19_2nd_v020_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 8))
def cg_f035_buyback_share_reduction_core20_2nd_v021_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(sharesbas, 4), 4))
def cg_f035_buyback_share_reduction_core21_2nd_v022_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core22_2nd_v023_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(ncfcommon, 4))
def cg_f035_buyback_share_reduction_core23_2nd_v024_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core24_2nd_v025_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core25_2nd_v026_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_pct_change(sharesbas, 4), 4))
def cg_f035_buyback_share_reduction_core26_2nd_v027_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(sharesbas, 4), 4))
def cg_f035_buyback_share_reduction_core27_2nd_v028_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_z(ncfcommon, 8), 4))
def cg_f035_buyback_share_reduction_core28_2nd_v029_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(sharesbas - shareswa, 4))
def cg_f035_buyback_share_reduction_core29_2nd_v030_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4))
def cg_f035_buyback_share_reduction_core30_2nd_v031_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core31_2nd_v032_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(shareswa, 4), 4), 8))
def cg_f035_buyback_share_reduction_core32_2nd_v033_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(ncfcommon, 4), 8))
def cg_f035_buyback_share_reduction_core33_2nd_v034_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core34_2nd_v035_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core35_2nd_v036_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_pct_change(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core36_2nd_v037_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_slope(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core37_2nd_v038_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_z(ncfcommon, 8), 4), 8))
def cg_f035_buyback_share_reduction_core38_2nd_v039_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(sharesbas - shareswa, 4), 8))
def cg_f035_buyback_share_reduction_core39_2nd_v040_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core40_2nd_v041_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(sharesbas, 4), 8), 12))
def cg_f035_buyback_share_reduction_core41_2nd_v042_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(shareswa, 4), 8), 12))
def cg_f035_buyback_share_reduction_core42_2nd_v043_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(ncfcommon, 8), 12))
def cg_f035_buyback_share_reduction_core43_2nd_v044_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 8), 12))
def cg_f035_buyback_share_reduction_core44_2nd_v045_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 8), 12))
def cg_f035_buyback_share_reduction_core45_2nd_v046_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_pct_change(sharesbas, 4), 8), 12))
def cg_f035_buyback_share_reduction_core46_2nd_v047_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_slope(sharesbas, 4), 8), 12))
def cg_f035_buyback_share_reduction_core47_2nd_v048_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_z(ncfcommon, 8), 8), 12))
def cg_f035_buyback_share_reduction_core48_2nd_v049_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(sharesbas - shareswa, 8), 12))
def cg_f035_buyback_share_reduction_core49_2nd_v050_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 8), 12))
def cg_f035_buyback_share_reduction_core50_2nd_v051_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core51_2nd_v052_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(shareswa, 4), 4), 8))
def cg_f035_buyback_share_reduction_core52_2nd_v053_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(ncfcommon, 4), 8))
def cg_f035_buyback_share_reduction_core53_2nd_v054_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core54_2nd_v055_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core55_2nd_v056_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_pct_change(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core56_2nd_v057_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core57_2nd_v058_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_z(ncfcommon, 8), 4), 8))
def cg_f035_buyback_share_reduction_core58_2nd_v059_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(sharesbas - shareswa, 4), 8))
def cg_f035_buyback_share_reduction_core59_2nd_v060_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core60_2nd_v061_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(sharesbas, 4), 4), 12))
def cg_f035_buyback_share_reduction_core61_2nd_v062_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(shareswa, 4), 4), 12))
def cg_f035_buyback_share_reduction_core62_2nd_v063_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(ncfcommon, 4), 12))
def cg_f035_buyback_share_reduction_core63_2nd_v064_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 12))
def cg_f035_buyback_share_reduction_core64_2nd_v065_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 12))
def cg_f035_buyback_share_reduction_core65_2nd_v066_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_pct_change(sharesbas, 4), 4), 12))
def cg_f035_buyback_share_reduction_core66_2nd_v067_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_slope(sharesbas, 4), 4), 12))
def cg_f035_buyback_share_reduction_core67_2nd_v068_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_z(ncfcommon, 8), 4), 12))
def cg_f035_buyback_share_reduction_core68_2nd_v069_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(sharesbas - shareswa, 4), 12))
def cg_f035_buyback_share_reduction_core69_2nd_v070_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 12))
def cg_f035_buyback_share_reduction_core70_2nd_v071_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(sharesbas, 4), 4), 12))
def cg_f035_buyback_share_reduction_core71_2nd_v072_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(shareswa, 4), 4), 12))
def cg_f035_buyback_share_reduction_core72_2nd_v073_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(ncfcommon, 4), 12))
def cg_f035_buyback_share_reduction_core73_2nd_v074_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 12))
def cg_f035_buyback_share_reduction_core74_2nd_v075_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 12))
def cg_f035_buyback_share_reduction_core75_2nd_v076_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_pct_change(sharesbas, 4), 4), 12))
def cg_f035_buyback_share_reduction_core76_2nd_v077_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(sharesbas, 4), 4), 12))
def cg_f035_buyback_share_reduction_core77_2nd_v078_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_z(ncfcommon, 8), 4), 12))
def cg_f035_buyback_share_reduction_core78_2nd_v079_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(sharesbas - shareswa, 4), 12))
def cg_f035_buyback_share_reduction_core79_2nd_v080_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 12))
def cg_f035_buyback_share_reduction_core80_2nd_v081_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core81_2nd_v082_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core82_2nd_v083_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(ncfcommon, 4), 4))
def cg_f035_buyback_share_reduction_core83_2nd_v084_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core84_2nd_v085_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core85_2nd_v086_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_pct_change(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core86_2nd_v087_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_slope(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core87_2nd_v088_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_z(ncfcommon, 8), 4), 4))
def cg_f035_buyback_share_reduction_core88_2nd_v089_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(sharesbas - shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core89_2nd_v090_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core90_2nd_v091_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core91_2nd_v092_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core92_2nd_v093_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(ncfcommon, 4), 4))
def cg_f035_buyback_share_reduction_core93_2nd_v094_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core94_2nd_v095_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core95_2nd_v096_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_pct_change(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core96_2nd_v097_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core97_2nd_v098_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_z(ncfcommon, 8), 4), 4))
def cg_f035_buyback_share_reduction_core98_2nd_v099_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(sharesbas - shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core99_2nd_v100_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core100_2nd_v101_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_diff(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core101_2nd_v102_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_diff(shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core102_2nd_v103_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(ncfcommon, 4), 4))
def cg_f035_buyback_share_reduction_core103_2nd_v104_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core104_2nd_v105_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core105_2nd_v106_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_pct_change(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core106_2nd_v107_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_slope(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core107_2nd_v108_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_z(ncfcommon, 8), 4), 4))
def cg_f035_buyback_share_reduction_core108_2nd_v109_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(sharesbas - shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core109_2nd_v110_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core110_2nd_v111_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_diff(sharesbas, 4), 8), 8))
def cg_f035_buyback_share_reduction_core111_2nd_v112_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_diff(shareswa, 4), 8), 8))
def cg_f035_buyback_share_reduction_core112_2nd_v113_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(ncfcommon, 8), 8))
def cg_f035_buyback_share_reduction_core113_2nd_v114_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_safe_div(ncfcommon, marketcap.abs() + 1.0), 8), 8))
def cg_f035_buyback_share_reduction_core114_2nd_v115_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 8), 8))
def cg_f035_buyback_share_reduction_core115_2nd_v116_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_pct_change(sharesbas, 4), 8), 8))
def cg_f035_buyback_share_reduction_core116_2nd_v117_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_slope(sharesbas, 4), 8), 8))
def cg_f035_buyback_share_reduction_core117_2nd_v118_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_z(ncfcommon, 8), 8), 8))
def cg_f035_buyback_share_reduction_core118_2nd_v119_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(sharesbas - shareswa, 8), 8))
def cg_f035_buyback_share_reduction_core119_2nd_v120_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_mean(_safe_div(sharesbas, shareswa.abs() + 1.0), 8), 8))
def cg_f035_buyback_share_reduction_core120_2nd_v121_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_diff(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core121_2nd_v122_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_diff(shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core122_2nd_v123_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(ncfcommon, 4), 4))
def cg_f035_buyback_share_reduction_core123_2nd_v124_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core124_2nd_v125_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core125_2nd_v126_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_pct_change(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core126_2nd_v127_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_slope(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core127_2nd_v128_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_z(ncfcommon, 8), 4), 4))
def cg_f035_buyback_share_reduction_core128_2nd_v129_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(sharesbas - shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core129_2nd_v130_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_mean(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core130_2nd_v131_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_diff(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core131_2nd_v132_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_diff(shareswa, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core132_2nd_v133_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(ncfcommon, 4), 4), 8))
def cg_f035_buyback_share_reduction_core133_2nd_v134_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core134_2nd_v135_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core135_2nd_v136_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_pct_change(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core136_2nd_v137_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_slope(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core137_2nd_v138_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_z(ncfcommon, 8), 4), 4), 8))
def cg_f035_buyback_share_reduction_core138_2nd_v139_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(sharesbas - shareswa, 4), 4), 8))
def cg_f035_buyback_share_reduction_core139_2nd_v140_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core140_2nd_v141_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_diff(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core141_2nd_v142_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_diff(shareswa, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core142_2nd_v143_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(ncfcommon, 4), 4), 12))
def cg_f035_buyback_share_reduction_core143_2nd_v144_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core144_2nd_v145_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core145_2nd_v146_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_pct_change(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core146_2nd_v147_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_slope(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core147_2nd_v148_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_z(ncfcommon, 8), 4), 4), 12))
def cg_f035_buyback_share_reduction_core148_2nd_v149_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(sharesbas - shareswa, 4), 4), 12))
def cg_f035_buyback_share_reduction_core149_2nd_v150_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 12))