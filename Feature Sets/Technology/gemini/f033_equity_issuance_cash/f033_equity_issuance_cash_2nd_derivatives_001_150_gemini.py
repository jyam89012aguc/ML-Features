import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f033_equity_issuance_cash_core00_2nd_v001_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(ncfcommon, 4))
def cg_f033_equity_issuance_cash_core01_2nd_v002_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(ncff, 4))
def cg_f033_equity_issuance_cash_core02_2nd_v003_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_safe_div(ncfcommon, ncff.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core03_2nd_v004_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core04_2nd_v005_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_diff(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core05_2nd_v006_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_slope(ncfcommon, 8), 4))
def cg_f033_equity_issuance_cash_core06_2nd_v007_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_z(ncfcommon, 12), 4))
def cg_f033_equity_issuance_cash_core07_2nd_v008_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(ncfcommon + ncff, 4))
def cg_f033_equity_issuance_cash_core08_2nd_v009_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_pct_change(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core09_2nd_v010_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_safe_div(ncff, sharesbas.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core10_2nd_v011_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(ncfcommon, 8))
def cg_f033_equity_issuance_cash_core11_2nd_v012_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(ncff, 8))
def cg_f033_equity_issuance_cash_core12_2nd_v013_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_safe_div(ncfcommon, ncff.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core13_2nd_v014_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core14_2nd_v015_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_diff(ncfcommon, 4), 8))
def cg_f033_equity_issuance_cash_core15_2nd_v016_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_slope(ncfcommon, 8), 8))
def cg_f033_equity_issuance_cash_core16_2nd_v017_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_z(ncfcommon, 12), 8))
def cg_f033_equity_issuance_cash_core17_2nd_v018_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(ncfcommon + ncff, 8))
def cg_f033_equity_issuance_cash_core18_2nd_v019_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_pct_change(ncfcommon, 4), 8))
def cg_f033_equity_issuance_cash_core19_2nd_v020_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_safe_div(ncff, sharesbas.abs() + 1.0), 8))
def cg_f033_equity_issuance_cash_core20_2nd_v021_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(ncfcommon, 4))
def cg_f033_equity_issuance_cash_core21_2nd_v022_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(ncff, 4))
def cg_f033_equity_issuance_cash_core22_2nd_v023_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_safe_div(ncfcommon, ncff.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core23_2nd_v024_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core24_2nd_v025_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_diff(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core25_2nd_v026_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_slope(ncfcommon, 8), 4))
def cg_f033_equity_issuance_cash_core26_2nd_v027_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_z(ncfcommon, 12), 4))
def cg_f033_equity_issuance_cash_core27_2nd_v028_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(ncfcommon + ncff, 4))
def cg_f033_equity_issuance_cash_core28_2nd_v029_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_pct_change(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core29_2nd_v030_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_safe_div(ncff, sharesbas.abs() + 1.0), 4))
def cg_f033_equity_issuance_cash_core30_2nd_v031_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(ncfcommon, 4), 8))
def cg_f033_equity_issuance_cash_core31_2nd_v032_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(ncff, 4), 8))
def cg_f033_equity_issuance_cash_core32_2nd_v033_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 8))
def cg_f033_equity_issuance_cash_core33_2nd_v034_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8))
def cg_f033_equity_issuance_cash_core34_2nd_v035_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_diff(ncfcommon, 4), 4), 8))
def cg_f033_equity_issuance_cash_core35_2nd_v036_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_slope(ncfcommon, 8), 4), 8))
def cg_f033_equity_issuance_cash_core36_2nd_v037_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_z(ncfcommon, 12), 4), 8))
def cg_f033_equity_issuance_cash_core37_2nd_v038_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(ncfcommon + ncff, 4), 8))
def cg_f033_equity_issuance_cash_core38_2nd_v039_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_pct_change(ncfcommon, 4), 4), 8))
def cg_f033_equity_issuance_cash_core39_2nd_v040_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 8))
def cg_f033_equity_issuance_cash_core40_2nd_v041_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(ncfcommon, 8), 12))
def cg_f033_equity_issuance_cash_core41_2nd_v042_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(ncff, 8), 12))
def cg_f033_equity_issuance_cash_core42_2nd_v043_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_safe_div(ncfcommon, ncff.abs() + 1.0), 8), 12))
def cg_f033_equity_issuance_cash_core43_2nd_v044_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 8), 12))
def cg_f033_equity_issuance_cash_core44_2nd_v045_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_diff(ncfcommon, 4), 8), 12))
def cg_f033_equity_issuance_cash_core45_2nd_v046_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_slope(ncfcommon, 8), 8), 12))
def cg_f033_equity_issuance_cash_core46_2nd_v047_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_z(ncfcommon, 12), 8), 12))
def cg_f033_equity_issuance_cash_core47_2nd_v048_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(ncfcommon + ncff, 8), 12))
def cg_f033_equity_issuance_cash_core48_2nd_v049_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_pct_change(ncfcommon, 4), 8), 12))
def cg_f033_equity_issuance_cash_core49_2nd_v050_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_slope(_safe_div(ncff, sharesbas.abs() + 1.0), 8), 12))
def cg_f033_equity_issuance_cash_core50_2nd_v051_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(ncfcommon, 4), 8))
def cg_f033_equity_issuance_cash_core51_2nd_v052_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(ncff, 4), 8))
def cg_f033_equity_issuance_cash_core52_2nd_v053_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 8))
def cg_f033_equity_issuance_cash_core53_2nd_v054_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 8))
def cg_f033_equity_issuance_cash_core54_2nd_v055_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_diff(ncfcommon, 4), 4), 8))
def cg_f033_equity_issuance_cash_core55_2nd_v056_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_slope(ncfcommon, 8), 4), 8))
def cg_f033_equity_issuance_cash_core56_2nd_v057_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_z(ncfcommon, 12), 4), 8))
def cg_f033_equity_issuance_cash_core57_2nd_v058_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(ncfcommon + ncff, 4), 8))
def cg_f033_equity_issuance_cash_core58_2nd_v059_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_pct_change(ncfcommon, 4), 4), 8))
def cg_f033_equity_issuance_cash_core59_2nd_v060_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 8))
def cg_f033_equity_issuance_cash_core60_2nd_v061_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(ncfcommon, 4), 12))
def cg_f033_equity_issuance_cash_core61_2nd_v062_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(ncff, 4), 12))
def cg_f033_equity_issuance_cash_core62_2nd_v063_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 12))
def cg_f033_equity_issuance_cash_core63_2nd_v064_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 12))
def cg_f033_equity_issuance_cash_core64_2nd_v065_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_diff(ncfcommon, 4), 4), 12))
def cg_f033_equity_issuance_cash_core65_2nd_v066_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_slope(ncfcommon, 8), 4), 12))
def cg_f033_equity_issuance_cash_core66_2nd_v067_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_z(ncfcommon, 12), 4), 12))
def cg_f033_equity_issuance_cash_core67_2nd_v068_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(ncfcommon + ncff, 4), 12))
def cg_f033_equity_issuance_cash_core68_2nd_v069_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_pct_change(ncfcommon, 4), 4), 12))
def cg_f033_equity_issuance_cash_core69_2nd_v070_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 12))
def cg_f033_equity_issuance_cash_core70_2nd_v071_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(ncfcommon, 4), 12))
def cg_f033_equity_issuance_cash_core71_2nd_v072_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(ncff, 4), 12))
def cg_f033_equity_issuance_cash_core72_2nd_v073_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 12))
def cg_f033_equity_issuance_cash_core73_2nd_v074_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 12))
def cg_f033_equity_issuance_cash_core74_2nd_v075_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_diff(ncfcommon, 4), 4), 12))
def cg_f033_equity_issuance_cash_core75_2nd_v076_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_slope(ncfcommon, 8), 4), 12))
def cg_f033_equity_issuance_cash_core76_2nd_v077_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_z(ncfcommon, 12), 4), 12))
def cg_f033_equity_issuance_cash_core77_2nd_v078_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(ncfcommon + ncff, 4), 12))
def cg_f033_equity_issuance_cash_core78_2nd_v079_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_pct_change(ncfcommon, 4), 4), 12))
def cg_f033_equity_issuance_cash_core79_2nd_v080_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_diff(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 12))
def cg_f033_equity_issuance_cash_core80_2nd_v081_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core81_2nd_v082_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(ncff, 4), 4))
def cg_f033_equity_issuance_cash_core82_2nd_v083_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core83_2nd_v084_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core84_2nd_v085_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_diff(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core85_2nd_v086_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_slope(ncfcommon, 8), 4), 4))
def cg_f033_equity_issuance_cash_core86_2nd_v087_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_z(ncfcommon, 12), 4), 4))
def cg_f033_equity_issuance_cash_core87_2nd_v088_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(ncfcommon + ncff, 4), 4))
def cg_f033_equity_issuance_cash_core88_2nd_v089_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_pct_change(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core89_2nd_v090_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_slope(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core90_2nd_v091_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core91_2nd_v092_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(ncff, 4), 4))
def cg_f033_equity_issuance_cash_core92_2nd_v093_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core93_2nd_v094_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core94_2nd_v095_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_diff(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core95_2nd_v096_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_slope(ncfcommon, 8), 4), 4))
def cg_f033_equity_issuance_cash_core96_2nd_v097_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_z(ncfcommon, 12), 4), 4))
def cg_f033_equity_issuance_cash_core97_2nd_v098_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(ncfcommon + ncff, 4), 4))
def cg_f033_equity_issuance_cash_core98_2nd_v099_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_pct_change(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core99_2nd_v100_signal(ncfcommon, ncff, sharesbas):
    return _clean(_mean(_diff(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core100_2nd_v101_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core101_2nd_v102_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(ncff, 4), 4))
def cg_f033_equity_issuance_cash_core102_2nd_v103_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core103_2nd_v104_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core104_2nd_v105_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_diff(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core105_2nd_v106_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_slope(ncfcommon, 8), 4), 4))
def cg_f033_equity_issuance_cash_core106_2nd_v107_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_z(ncfcommon, 12), 4), 4))
def cg_f033_equity_issuance_cash_core107_2nd_v108_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(ncfcommon + ncff, 4), 4))
def cg_f033_equity_issuance_cash_core108_2nd_v109_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_pct_change(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core109_2nd_v110_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core110_2nd_v111_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(ncfcommon, 8), 8))
def cg_f033_equity_issuance_cash_core111_2nd_v112_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(ncff, 8), 8))
def cg_f033_equity_issuance_cash_core112_2nd_v113_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_safe_div(ncfcommon, ncff.abs() + 1.0), 8), 8))
def cg_f033_equity_issuance_cash_core113_2nd_v114_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 8), 8))
def cg_f033_equity_issuance_cash_core114_2nd_v115_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_diff(ncfcommon, 4), 8), 8))
def cg_f033_equity_issuance_cash_core115_2nd_v116_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_slope(ncfcommon, 8), 8), 8))
def cg_f033_equity_issuance_cash_core116_2nd_v117_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_z(ncfcommon, 12), 8), 8))
def cg_f033_equity_issuance_cash_core117_2nd_v118_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(ncfcommon + ncff, 8), 8))
def cg_f033_equity_issuance_cash_core118_2nd_v119_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_pct_change(ncfcommon, 4), 8), 8))
def cg_f033_equity_issuance_cash_core119_2nd_v120_signal(ncfcommon, ncff, sharesbas):
    return _clean(_slope(_mean(_safe_div(ncff, sharesbas.abs() + 1.0), 8), 8))
def cg_f033_equity_issuance_cash_core120_2nd_v121_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(ncfcommon, 4), 4))
def cg_f033_equity_issuance_cash_core121_2nd_v122_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(ncff, 4), 4))
def cg_f033_equity_issuance_cash_core122_2nd_v123_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core123_2nd_v124_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core124_2nd_v125_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_diff(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core125_2nd_v126_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_slope(ncfcommon, 8), 4), 4))
def cg_f033_equity_issuance_cash_core126_2nd_v127_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_z(ncfcommon, 12), 4), 4))
def cg_f033_equity_issuance_cash_core127_2nd_v128_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(ncfcommon + ncff, 4), 4))
def cg_f033_equity_issuance_cash_core128_2nd_v129_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_pct_change(ncfcommon, 4), 4), 4))
def cg_f033_equity_issuance_cash_core129_2nd_v130_signal(ncfcommon, ncff, sharesbas):
    return _clean(_diff(_mean(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 4))
def cg_f033_equity_issuance_cash_core130_2nd_v131_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(ncfcommon, 4), 4), 8))
def cg_f033_equity_issuance_cash_core131_2nd_v132_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(ncff, 4), 4), 8))
def cg_f033_equity_issuance_cash_core132_2nd_v133_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 4), 8))
def cg_f033_equity_issuance_cash_core133_2nd_v134_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f033_equity_issuance_cash_core134_2nd_v135_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_diff(ncfcommon, 4), 4), 4), 8))
def cg_f033_equity_issuance_cash_core135_2nd_v136_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_slope(ncfcommon, 8), 4), 4), 8))
def cg_f033_equity_issuance_cash_core136_2nd_v137_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_z(ncfcommon, 12), 4), 4), 8))
def cg_f033_equity_issuance_cash_core137_2nd_v138_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(ncfcommon + ncff, 4), 4), 8))
def cg_f033_equity_issuance_cash_core138_2nd_v139_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_pct_change(ncfcommon, 4), 4), 4), 8))
def cg_f033_equity_issuance_cash_core139_2nd_v140_signal(ncfcommon, ncff, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f033_equity_issuance_cash_core140_2nd_v141_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(ncfcommon, 4), 4), 12))
def cg_f033_equity_issuance_cash_core141_2nd_v142_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(ncff, 4), 4), 12))
def cg_f033_equity_issuance_cash_core142_2nd_v143_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(ncfcommon, ncff.abs() + 1.0), 4), 4), 12))
def cg_f033_equity_issuance_cash_core143_2nd_v144_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(ncfcommon, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f033_equity_issuance_cash_core144_2nd_v145_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_diff(ncfcommon, 4), 4), 4), 12))
def cg_f033_equity_issuance_cash_core145_2nd_v146_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_slope(ncfcommon, 8), 4), 4), 12))
def cg_f033_equity_issuance_cash_core146_2nd_v147_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_z(ncfcommon, 12), 4), 4), 12))
def cg_f033_equity_issuance_cash_core147_2nd_v148_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(ncfcommon + ncff, 4), 4), 12))
def cg_f033_equity_issuance_cash_core148_2nd_v149_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_pct_change(ncfcommon, 4), 4), 4), 12))
def cg_f033_equity_issuance_cash_core149_2nd_v150_signal(ncfcommon, ncff, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(ncff, sharesbas.abs() + 1.0), 4), 4), 12))