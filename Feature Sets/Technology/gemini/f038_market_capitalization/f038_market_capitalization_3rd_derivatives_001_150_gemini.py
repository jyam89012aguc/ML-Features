import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f038_market_capitalization_core00_3rd_v001_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(marketcap, 4), 4))
def cg_f038_market_capitalization_core01_3rd_v002_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(sharesbas * close, 4), 4))
def cg_f038_market_capitalization_core02_3rd_v003_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core03_3rd_v004_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_pct_change(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core04_3rd_v005_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_slope(marketcap, 8), 4), 4))
def cg_f038_market_capitalization_core05_3rd_v006_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_z(marketcap, 12), 4), 4))
def cg_f038_market_capitalization_core06_3rd_v007_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4))
def cg_f038_market_capitalization_core07_3rd_v008_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(close, 4), 4))
def cg_f038_market_capitalization_core08_3rd_v009_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_log(marketcap + 1.0), 4), 4))
def cg_f038_market_capitalization_core09_3rd_v010_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_mean(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core10_3rd_v011_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(marketcap, 4), 8))
def cg_f038_market_capitalization_core11_3rd_v012_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(sharesbas * close, 4), 8))
def cg_f038_market_capitalization_core12_3rd_v013_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core13_3rd_v014_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_pct_change(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core14_3rd_v015_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_slope(marketcap, 8), 4), 8))
def cg_f038_market_capitalization_core15_3rd_v016_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_z(marketcap, 12), 4), 8))
def cg_f038_market_capitalization_core16_3rd_v017_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 8))
def cg_f038_market_capitalization_core17_3rd_v018_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(close, 4), 8))
def cg_f038_market_capitalization_core18_3rd_v019_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_log(marketcap + 1.0), 4), 8))
def cg_f038_market_capitalization_core19_3rd_v020_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_mean(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core20_3rd_v021_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(marketcap, 4), 4))
def cg_f038_market_capitalization_core21_3rd_v022_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(sharesbas * close, 4), 4))
def cg_f038_market_capitalization_core22_3rd_v023_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core23_3rd_v024_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_pct_change(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core24_3rd_v025_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_slope(marketcap, 8), 4), 4))
def cg_f038_market_capitalization_core25_3rd_v026_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_z(marketcap, 12), 4), 4))
def cg_f038_market_capitalization_core26_3rd_v027_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4))
def cg_f038_market_capitalization_core27_3rd_v028_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(close, 4), 4))
def cg_f038_market_capitalization_core28_3rd_v029_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_log(marketcap + 1.0), 4), 4))
def cg_f038_market_capitalization_core29_3rd_v030_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(_mean(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core30_3rd_v031_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core31_3rd_v032_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(sharesbas * close, 4), 4), 8))
def cg_f038_market_capitalization_core32_3rd_v033_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_diff(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core33_3rd_v034_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_pct_change(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core34_3rd_v035_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_slope(marketcap, 8), 4), 4), 8))
def cg_f038_market_capitalization_core35_3rd_v036_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_z(marketcap, 12), 4), 4), 8))
def cg_f038_market_capitalization_core36_3rd_v037_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f038_market_capitalization_core37_3rd_v038_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(close, 4), 4), 8))
def cg_f038_market_capitalization_core38_3rd_v039_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_log(marketcap + 1.0), 4), 4), 8))
def cg_f038_market_capitalization_core39_3rd_v040_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(_mean(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core40_3rd_v041_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(marketcap, 4), 8), 12))
def cg_f038_market_capitalization_core41_3rd_v042_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(sharesbas * close, 4), 8), 12))
def cg_f038_market_capitalization_core42_3rd_v043_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(marketcap, 4), 4), 8), 12))
def cg_f038_market_capitalization_core43_3rd_v044_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_pct_change(marketcap, 4), 4), 8), 12))
def cg_f038_market_capitalization_core44_3rd_v045_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_slope(marketcap, 8), 4), 8), 12))
def cg_f038_market_capitalization_core45_3rd_v046_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_z(marketcap, 12), 4), 8), 12))
def cg_f038_market_capitalization_core46_3rd_v047_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f038_market_capitalization_core47_3rd_v048_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(close, 4), 8), 12))
def cg_f038_market_capitalization_core48_3rd_v049_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_log(marketcap + 1.0), 4), 8), 12))
def cg_f038_market_capitalization_core49_3rd_v050_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_mean(marketcap, 4), 4), 8), 12))
def cg_f038_market_capitalization_core50_3rd_v051_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core51_3rd_v052_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(sharesbas * close, 4), 4), 8))
def cg_f038_market_capitalization_core52_3rd_v053_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_diff(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core53_3rd_v054_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_pct_change(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core54_3rd_v055_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_slope(marketcap, 8), 4), 4), 8))
def cg_f038_market_capitalization_core55_3rd_v056_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_z(marketcap, 12), 4), 4), 8))
def cg_f038_market_capitalization_core56_3rd_v057_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f038_market_capitalization_core57_3rd_v058_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(close, 4), 4), 8))
def cg_f038_market_capitalization_core58_3rd_v059_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_log(marketcap + 1.0), 4), 4), 8))
def cg_f038_market_capitalization_core59_3rd_v060_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(_mean(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core60_3rd_v061_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core61_3rd_v062_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(sharesbas * close, 4), 4), 12))
def cg_f038_market_capitalization_core62_3rd_v063_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_diff(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core63_3rd_v064_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_pct_change(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core64_3rd_v065_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_slope(marketcap, 8), 4), 4), 12))
def cg_f038_market_capitalization_core65_3rd_v066_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_z(marketcap, 12), 4), 4), 12))
def cg_f038_market_capitalization_core66_3rd_v067_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f038_market_capitalization_core67_3rd_v068_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(close, 4), 4), 12))
def cg_f038_market_capitalization_core68_3rd_v069_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_log(marketcap + 1.0), 4), 4), 12))
def cg_f038_market_capitalization_core69_3rd_v070_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(_mean(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core70_3rd_v071_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(marketcap, 4), 8), 12))
def cg_f038_market_capitalization_core71_3rd_v072_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(sharesbas * close, 4), 8), 12))
def cg_f038_market_capitalization_core72_3rd_v073_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_diff(marketcap, 4), 4), 8), 12))
def cg_f038_market_capitalization_core73_3rd_v074_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_pct_change(marketcap, 4), 4), 8), 12))
def cg_f038_market_capitalization_core74_3rd_v075_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_slope(marketcap, 8), 4), 8), 12))
def cg_f038_market_capitalization_core75_3rd_v076_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_z(marketcap, 12), 4), 8), 12))
def cg_f038_market_capitalization_core76_3rd_v077_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 8), 12))
def cg_f038_market_capitalization_core77_3rd_v078_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(close, 4), 8), 12))
def cg_f038_market_capitalization_core78_3rd_v079_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_log(marketcap + 1.0), 4), 8), 12))
def cg_f038_market_capitalization_core79_3rd_v080_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(_mean(marketcap, 4), 4), 8), 12))
def cg_f038_market_capitalization_core80_3rd_v081_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core81_3rd_v082_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(sharesbas * close, 4), 4), 12))
def cg_f038_market_capitalization_core82_3rd_v083_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_diff(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core83_3rd_v084_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_pct_change(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core84_3rd_v085_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_slope(marketcap, 8), 4), 4), 12))
def cg_f038_market_capitalization_core85_3rd_v086_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_z(marketcap, 12), 4), 4), 12))
def cg_f038_market_capitalization_core86_3rd_v087_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f038_market_capitalization_core87_3rd_v088_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(close, 4), 4), 12))
def cg_f038_market_capitalization_core88_3rd_v089_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_log(marketcap + 1.0), 4), 4), 12))
def cg_f038_market_capitalization_core89_3rd_v090_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(_mean(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core90_3rd_v091_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core91_3rd_v092_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(sharesbas * close, 4), 4), 4))
def cg_f038_market_capitalization_core92_3rd_v093_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_diff(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core93_3rd_v094_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_pct_change(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core94_3rd_v095_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_slope(marketcap, 8), 4), 4), 4))
def cg_f038_market_capitalization_core95_3rd_v096_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_z(marketcap, 12), 4), 4), 4))
def cg_f038_market_capitalization_core96_3rd_v097_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core97_3rd_v098_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(close, 4), 4), 4))
def cg_f038_market_capitalization_core98_3rd_v099_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core99_3rd_v100_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(_mean(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core100_3rd_v101_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(marketcap, 4), 8), 4))
def cg_f038_market_capitalization_core101_3rd_v102_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(sharesbas * close, 4), 8), 4))
def cg_f038_market_capitalization_core102_3rd_v103_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_diff(marketcap, 4), 4), 8), 4))
def cg_f038_market_capitalization_core103_3rd_v104_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_pct_change(marketcap, 4), 4), 8), 4))
def cg_f038_market_capitalization_core104_3rd_v105_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_slope(marketcap, 8), 4), 8), 4))
def cg_f038_market_capitalization_core105_3rd_v106_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_z(marketcap, 12), 4), 8), 4))
def cg_f038_market_capitalization_core106_3rd_v107_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 8), 4))
def cg_f038_market_capitalization_core107_3rd_v108_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(close, 4), 8), 4))
def cg_f038_market_capitalization_core108_3rd_v109_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_log(marketcap + 1.0), 4), 8), 4))
def cg_f038_market_capitalization_core109_3rd_v110_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(_mean(marketcap, 4), 4), 8), 4))
def cg_f038_market_capitalization_core110_3rd_v111_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core111_3rd_v112_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(sharesbas * close, 4), 4), 4))
def cg_f038_market_capitalization_core112_3rd_v113_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_diff(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core113_3rd_v114_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_pct_change(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core114_3rd_v115_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_slope(marketcap, 8), 4), 4), 4))
def cg_f038_market_capitalization_core115_3rd_v116_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_z(marketcap, 12), 4), 4), 4))
def cg_f038_market_capitalization_core116_3rd_v117_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core117_3rd_v118_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(close, 4), 4), 4))
def cg_f038_market_capitalization_core118_3rd_v119_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_log(marketcap + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core119_3rd_v120_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(_mean(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core120_3rd_v121_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core121_3rd_v122_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(sharesbas * close, 4), 4), 4))
def cg_f038_market_capitalization_core122_3rd_v123_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_diff(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core123_3rd_v124_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_pct_change(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core124_3rd_v125_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_slope(marketcap, 8), 4), 4), 4))
def cg_f038_market_capitalization_core125_3rd_v126_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_z(marketcap, 12), 4), 4), 4))
def cg_f038_market_capitalization_core126_3rd_v127_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core127_3rd_v128_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(close, 4), 4), 4))
def cg_f038_market_capitalization_core128_3rd_v129_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core129_3rd_v130_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(_diff(_mean(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core130_3rd_v131_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core131_3rd_v132_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(sharesbas * close, 4), 4), 4))
def cg_f038_market_capitalization_core132_3rd_v133_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_diff(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core133_3rd_v134_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_pct_change(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core134_3rd_v135_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_slope(marketcap, 8), 4), 4), 4))
def cg_f038_market_capitalization_core135_3rd_v136_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_z(marketcap, 12), 4), 4), 4))
def cg_f038_market_capitalization_core136_3rd_v137_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core137_3rd_v138_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(close, 4), 4), 4))
def cg_f038_market_capitalization_core138_3rd_v139_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4))
def cg_f038_market_capitalization_core139_3rd_v140_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(_diff(_mean(marketcap, 4), 4), 4), 4))
def cg_f038_market_capitalization_core140_3rd_v141_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core141_3rd_v142_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(sharesbas * close, 4), 4), 4), 8))
def cg_f038_market_capitalization_core142_3rd_v143_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_diff(marketcap, 4), 4), 4), 4), 8))
def cg_f038_market_capitalization_core143_3rd_v144_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_pct_change(marketcap, 4), 4), 4), 4), 8))
def cg_f038_market_capitalization_core144_3rd_v145_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_slope(marketcap, 8), 4), 4), 4), 8))
def cg_f038_market_capitalization_core145_3rd_v146_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_z(marketcap, 12), 4), 4), 4), 8))
def cg_f038_market_capitalization_core146_3rd_v147_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 4), 8))
def cg_f038_market_capitalization_core147_3rd_v148_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(close, 4), 4), 4), 8))
def cg_f038_market_capitalization_core148_3rd_v149_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4), 8))
def cg_f038_market_capitalization_core149_3rd_v150_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(_diff(_mean(marketcap, 4), 4), 4), 4), 8))