import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f035_buyback_share_reduction_core00_3rd_v001_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core01_3rd_v002_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core02_3rd_v003_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(ncfcommon, 4), 4))
def cg_f035_buyback_share_reduction_core03_3rd_v004_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core04_3rd_v005_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core05_3rd_v006_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_pct_change(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core06_3rd_v007_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_slope(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core07_3rd_v008_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_z(ncfcommon, 8), 4), 4))
def cg_f035_buyback_share_reduction_core08_3rd_v009_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(sharesbas - shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core09_3rd_v010_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core10_3rd_v011_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core11_3rd_v012_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(shareswa, 4), 4), 8))
def cg_f035_buyback_share_reduction_core12_3rd_v013_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(ncfcommon, 4), 8))
def cg_f035_buyback_share_reduction_core13_3rd_v014_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core14_3rd_v015_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core15_3rd_v016_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_pct_change(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core16_3rd_v017_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_slope(sharesbas, 4), 4), 8))
def cg_f035_buyback_share_reduction_core17_3rd_v018_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_z(ncfcommon, 8), 4), 8))
def cg_f035_buyback_share_reduction_core18_3rd_v019_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(sharesbas - shareswa, 4), 8))
def cg_f035_buyback_share_reduction_core19_3rd_v020_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 8))
def cg_f035_buyback_share_reduction_core20_3rd_v021_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_diff(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core21_3rd_v022_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_diff(shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core22_3rd_v023_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(ncfcommon, 4), 4))
def cg_f035_buyback_share_reduction_core23_3rd_v024_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core24_3rd_v025_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core25_3rd_v026_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_pct_change(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core26_3rd_v027_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_slope(sharesbas, 4), 4), 4))
def cg_f035_buyback_share_reduction_core27_3rd_v028_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_z(ncfcommon, 8), 4), 4))
def cg_f035_buyback_share_reduction_core28_3rd_v029_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(sharesbas - shareswa, 4), 4))
def cg_f035_buyback_share_reduction_core29_3rd_v030_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4))
def cg_f035_buyback_share_reduction_core30_3rd_v031_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_diff(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core31_3rd_v032_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_diff(shareswa, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core32_3rd_v033_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(ncfcommon, 4), 4), 8))
def cg_f035_buyback_share_reduction_core33_3rd_v034_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core34_3rd_v035_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core35_3rd_v036_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_pct_change(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core36_3rd_v037_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_slope(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core37_3rd_v038_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_z(ncfcommon, 8), 4), 4), 8))
def cg_f035_buyback_share_reduction_core38_3rd_v039_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(sharesbas - shareswa, 4), 4), 8))
def cg_f035_buyback_share_reduction_core39_3rd_v040_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core40_3rd_v041_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(sharesbas, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core41_3rd_v042_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(shareswa, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core42_3rd_v043_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(ncfcommon, 4), 8), 12))
def cg_f035_buyback_share_reduction_core43_3rd_v044_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f035_buyback_share_reduction_core44_3rd_v045_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f035_buyback_share_reduction_core45_3rd_v046_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_pct_change(sharesbas, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core46_3rd_v047_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_slope(sharesbas, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core47_3rd_v048_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_z(ncfcommon, 8), 4), 8), 12))
def cg_f035_buyback_share_reduction_core48_3rd_v049_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(sharesbas - shareswa, 4), 8), 12))
def cg_f035_buyback_share_reduction_core49_3rd_v050_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 8), 12))
def cg_f035_buyback_share_reduction_core50_3rd_v051_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_diff(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core51_3rd_v052_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_diff(shareswa, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core52_3rd_v053_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(ncfcommon, 4), 4), 8))
def cg_f035_buyback_share_reduction_core53_3rd_v054_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core54_3rd_v055_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core55_3rd_v056_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_pct_change(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core56_3rd_v057_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_slope(sharesbas, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core57_3rd_v058_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_z(ncfcommon, 8), 4), 4), 8))
def cg_f035_buyback_share_reduction_core58_3rd_v059_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(sharesbas - shareswa, 4), 4), 8))
def cg_f035_buyback_share_reduction_core59_3rd_v060_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 8))
def cg_f035_buyback_share_reduction_core60_3rd_v061_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_diff(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core61_3rd_v062_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_diff(shareswa, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core62_3rd_v063_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(ncfcommon, 4), 4), 12))
def cg_f035_buyback_share_reduction_core63_3rd_v064_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core64_3rd_v065_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core65_3rd_v066_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_pct_change(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core66_3rd_v067_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_slope(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core67_3rd_v068_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_z(ncfcommon, 8), 4), 4), 12))
def cg_f035_buyback_share_reduction_core68_3rd_v069_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(sharesbas - shareswa, 4), 4), 12))
def cg_f035_buyback_share_reduction_core69_3rd_v070_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core70_3rd_v071_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_diff(sharesbas, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core71_3rd_v072_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_diff(shareswa, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core72_3rd_v073_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(ncfcommon, 4), 8), 12))
def cg_f035_buyback_share_reduction_core73_3rd_v074_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f035_buyback_share_reduction_core74_3rd_v075_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f035_buyback_share_reduction_core75_3rd_v076_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_pct_change(sharesbas, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core76_3rd_v077_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_slope(sharesbas, 4), 4), 8), 12))
def cg_f035_buyback_share_reduction_core77_3rd_v078_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_z(ncfcommon, 8), 4), 8), 12))
def cg_f035_buyback_share_reduction_core78_3rd_v079_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(sharesbas - shareswa, 4), 8), 12))
def cg_f035_buyback_share_reduction_core79_3rd_v080_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 8), 12))
def cg_f035_buyback_share_reduction_core80_3rd_v081_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_diff(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core81_3rd_v082_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_diff(shareswa, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core82_3rd_v083_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(ncfcommon, 4), 4), 12))
def cg_f035_buyback_share_reduction_core83_3rd_v084_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core84_3rd_v085_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core85_3rd_v086_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_pct_change(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core86_3rd_v087_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_slope(sharesbas, 4), 4), 4), 12))
def cg_f035_buyback_share_reduction_core87_3rd_v088_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_z(ncfcommon, 8), 4), 4), 12))
def cg_f035_buyback_share_reduction_core88_3rd_v089_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(sharesbas - shareswa, 4), 4), 12))
def cg_f035_buyback_share_reduction_core89_3rd_v090_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 12))
def cg_f035_buyback_share_reduction_core90_3rd_v091_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_diff(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core91_3rd_v092_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_diff(shareswa, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core92_3rd_v093_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(ncfcommon, 4), 4), 4))
def cg_f035_buyback_share_reduction_core93_3rd_v094_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core94_3rd_v095_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core95_3rd_v096_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_pct_change(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core96_3rd_v097_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_slope(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core97_3rd_v098_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_z(ncfcommon, 8), 4), 4), 4))
def cg_f035_buyback_share_reduction_core98_3rd_v099_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(sharesbas - shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core99_3rd_v100_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core100_3rd_v101_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_diff(sharesbas, 4), 4), 8), 4))
def cg_f035_buyback_share_reduction_core101_3rd_v102_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_diff(shareswa, 4), 4), 8), 4))
def cg_f035_buyback_share_reduction_core102_3rd_v103_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(ncfcommon, 4), 8), 4))
def cg_f035_buyback_share_reduction_core103_3rd_v104_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 8), 4))
def cg_f035_buyback_share_reduction_core104_3rd_v105_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8), 4))
def cg_f035_buyback_share_reduction_core105_3rd_v106_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_pct_change(sharesbas, 4), 4), 8), 4))
def cg_f035_buyback_share_reduction_core106_3rd_v107_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_slope(sharesbas, 4), 4), 8), 4))
def cg_f035_buyback_share_reduction_core107_3rd_v108_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_z(ncfcommon, 8), 4), 8), 4))
def cg_f035_buyback_share_reduction_core108_3rd_v109_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(sharesbas - shareswa, 4), 8), 4))
def cg_f035_buyback_share_reduction_core109_3rd_v110_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 8), 4))
def cg_f035_buyback_share_reduction_core110_3rd_v111_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_diff(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core111_3rd_v112_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_diff(shareswa, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core112_3rd_v113_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(ncfcommon, 4), 4), 4))
def cg_f035_buyback_share_reduction_core113_3rd_v114_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core114_3rd_v115_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core115_3rd_v116_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_pct_change(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core116_3rd_v117_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_slope(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core117_3rd_v118_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_z(ncfcommon, 8), 4), 4), 4))
def cg_f035_buyback_share_reduction_core118_3rd_v119_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(sharesbas - shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core119_3rd_v120_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core120_3rd_v121_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_diff(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core121_3rd_v122_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_diff(shareswa, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core122_3rd_v123_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(ncfcommon, 4), 4), 4))
def cg_f035_buyback_share_reduction_core123_3rd_v124_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core124_3rd_v125_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core125_3rd_v126_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_pct_change(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core126_3rd_v127_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_slope(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core127_3rd_v128_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_z(ncfcommon, 8), 4), 4), 4))
def cg_f035_buyback_share_reduction_core128_3rd_v129_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(sharesbas - shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core129_3rd_v130_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core130_3rd_v131_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_diff(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core131_3rd_v132_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_diff(shareswa, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core132_3rd_v133_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(ncfcommon, 4), 4), 4))
def cg_f035_buyback_share_reduction_core133_3rd_v134_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core134_3rd_v135_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core135_3rd_v136_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_pct_change(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core136_3rd_v137_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_slope(sharesbas, 4), 4), 4), 4))
def cg_f035_buyback_share_reduction_core137_3rd_v138_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_z(ncfcommon, 8), 4), 4), 4))
def cg_f035_buyback_share_reduction_core138_3rd_v139_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(sharesbas - shareswa, 4), 4), 4))
def cg_f035_buyback_share_reduction_core139_3rd_v140_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 4))
def cg_f035_buyback_share_reduction_core140_3rd_v141_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_diff(sharesbas, 4), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core141_3rd_v142_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_diff(shareswa, 4), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core142_3rd_v143_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(ncfcommon, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core143_3rd_v144_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfcommon, marketcap.abs() + 1.0), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core144_3rd_v145_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core145_3rd_v146_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_pct_change(sharesbas, 4), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core146_3rd_v147_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_slope(sharesbas, 4), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core147_3rd_v148_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_z(ncfcommon, 8), 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core148_3rd_v149_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(sharesbas - shareswa, 4), 4), 4), 8))
def cg_f035_buyback_share_reduction_core149_3rd_v150_signal(sharesbas, shareswa, ncfcommon, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sharesbas, shareswa.abs() + 1.0), 4), 4), 4), 8))