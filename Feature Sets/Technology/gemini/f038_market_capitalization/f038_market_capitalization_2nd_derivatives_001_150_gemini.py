import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f038_market_capitalization_core00_2nd_v001_signal(marketcap, sharesbas, close):
    return _clean(_slope(marketcap, 4))
def cg_f038_market_capitalization_core01_2nd_v002_signal(marketcap, sharesbas, close):
    return _clean(_slope(sharesbas * close, 4))
def cg_f038_market_capitalization_core02_2nd_v003_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(marketcap, 4), 4))
def cg_f038_market_capitalization_core03_2nd_v004_signal(marketcap, sharesbas, close):
    return _clean(_slope(_pct_change(marketcap, 4), 4))
def cg_f038_market_capitalization_core04_2nd_v005_signal(marketcap, sharesbas, close):
    return _clean(_slope(_slope(marketcap, 8), 4))
def cg_f038_market_capitalization_core05_2nd_v006_signal(marketcap, sharesbas, close):
    return _clean(_slope(_z(marketcap, 12), 4))
def cg_f038_market_capitalization_core06_2nd_v007_signal(marketcap, sharesbas, close):
    return _clean(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4))
def cg_f038_market_capitalization_core07_2nd_v008_signal(marketcap, sharesbas, close):
    return _clean(_slope(close, 4))
def cg_f038_market_capitalization_core08_2nd_v009_signal(marketcap, sharesbas, close):
    return _clean(_slope(_log(marketcap + 1.0), 4))
def cg_f038_market_capitalization_core09_2nd_v010_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(marketcap, 4), 4))
def cg_f038_market_capitalization_core10_2nd_v011_signal(marketcap, sharesbas, close):
    return _clean(_slope(marketcap, 8))
def cg_f038_market_capitalization_core11_2nd_v012_signal(marketcap, sharesbas, close):
    return _clean(_slope(sharesbas * close, 8))
def cg_f038_market_capitalization_core12_2nd_v013_signal(marketcap, sharesbas, close):
    return _clean(_slope(_diff(marketcap, 4), 8))
def cg_f038_market_capitalization_core13_2nd_v014_signal(marketcap, sharesbas, close):
    return _clean(_slope(_pct_change(marketcap, 4), 8))
def cg_f038_market_capitalization_core14_2nd_v015_signal(marketcap, sharesbas, close):
    return _clean(_slope(_slope(marketcap, 8), 8))
def cg_f038_market_capitalization_core15_2nd_v016_signal(marketcap, sharesbas, close):
    return _clean(_slope(_z(marketcap, 12), 8))
def cg_f038_market_capitalization_core16_2nd_v017_signal(marketcap, sharesbas, close):
    return _clean(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 8))
def cg_f038_market_capitalization_core17_2nd_v018_signal(marketcap, sharesbas, close):
    return _clean(_slope(close, 8))
def cg_f038_market_capitalization_core18_2nd_v019_signal(marketcap, sharesbas, close):
    return _clean(_slope(_log(marketcap + 1.0), 8))
def cg_f038_market_capitalization_core19_2nd_v020_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(marketcap, 4), 8))
def cg_f038_market_capitalization_core20_2nd_v021_signal(marketcap, sharesbas, close):
    return _clean(_diff(marketcap, 4))
def cg_f038_market_capitalization_core21_2nd_v022_signal(marketcap, sharesbas, close):
    return _clean(_diff(sharesbas * close, 4))
def cg_f038_market_capitalization_core22_2nd_v023_signal(marketcap, sharesbas, close):
    return _clean(_diff(_diff(marketcap, 4), 4))
def cg_f038_market_capitalization_core23_2nd_v024_signal(marketcap, sharesbas, close):
    return _clean(_diff(_pct_change(marketcap, 4), 4))
def cg_f038_market_capitalization_core24_2nd_v025_signal(marketcap, sharesbas, close):
    return _clean(_diff(_slope(marketcap, 8), 4))
def cg_f038_market_capitalization_core25_2nd_v026_signal(marketcap, sharesbas, close):
    return _clean(_diff(_z(marketcap, 12), 4))
def cg_f038_market_capitalization_core26_2nd_v027_signal(marketcap, sharesbas, close):
    return _clean(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4))
def cg_f038_market_capitalization_core27_2nd_v028_signal(marketcap, sharesbas, close):
    return _clean(_diff(close, 4))
def cg_f038_market_capitalization_core28_2nd_v029_signal(marketcap, sharesbas, close):
    return _clean(_diff(_log(marketcap + 1.0), 4))
def cg_f038_market_capitalization_core29_2nd_v030_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(marketcap, 4), 4))
def cg_f038_market_capitalization_core30_2nd_v031_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(marketcap, 4), 8))
def cg_f038_market_capitalization_core31_2nd_v032_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(sharesbas * close, 4), 8))
def cg_f038_market_capitalization_core32_2nd_v033_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core33_2nd_v034_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_pct_change(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core34_2nd_v035_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_slope(marketcap, 8), 4), 8))
def cg_f038_market_capitalization_core35_2nd_v036_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_z(marketcap, 12), 4), 8))
def cg_f038_market_capitalization_core36_2nd_v037_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 8))
def cg_f038_market_capitalization_core37_2nd_v038_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(close, 4), 8))
def cg_f038_market_capitalization_core38_2nd_v039_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_log(marketcap + 1.0), 4), 8))
def cg_f038_market_capitalization_core39_2nd_v040_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_mean(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core40_2nd_v041_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(marketcap, 8), 12))
def cg_f038_market_capitalization_core41_2nd_v042_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(sharesbas * close, 8), 12))
def cg_f038_market_capitalization_core42_2nd_v043_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_diff(marketcap, 4), 8), 12))
def cg_f038_market_capitalization_core43_2nd_v044_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_pct_change(marketcap, 4), 8), 12))
def cg_f038_market_capitalization_core44_2nd_v045_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_slope(marketcap, 8), 8), 12))
def cg_f038_market_capitalization_core45_2nd_v046_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_z(marketcap, 12), 8), 12))
def cg_f038_market_capitalization_core46_2nd_v047_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 8), 12))
def cg_f038_market_capitalization_core47_2nd_v048_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(close, 8), 12))
def cg_f038_market_capitalization_core48_2nd_v049_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_log(marketcap + 1.0), 8), 12))
def cg_f038_market_capitalization_core49_2nd_v050_signal(marketcap, sharesbas, close):
    return _clean(_z(_slope(_mean(marketcap, 4), 8), 12))
def cg_f038_market_capitalization_core50_2nd_v051_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(marketcap, 4), 8))
def cg_f038_market_capitalization_core51_2nd_v052_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(sharesbas * close, 4), 8))
def cg_f038_market_capitalization_core52_2nd_v053_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_diff(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core53_2nd_v054_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_pct_change(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core54_2nd_v055_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_slope(marketcap, 8), 4), 8))
def cg_f038_market_capitalization_core55_2nd_v056_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_z(marketcap, 12), 4), 8))
def cg_f038_market_capitalization_core56_2nd_v057_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 8))
def cg_f038_market_capitalization_core57_2nd_v058_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(close, 4), 8))
def cg_f038_market_capitalization_core58_2nd_v059_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_log(marketcap + 1.0), 4), 8))
def cg_f038_market_capitalization_core59_2nd_v060_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core60_2nd_v061_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(marketcap, 4), 12))
def cg_f038_market_capitalization_core61_2nd_v062_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(sharesbas * close, 4), 12))
def cg_f038_market_capitalization_core62_2nd_v063_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_diff(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core63_2nd_v064_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_pct_change(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core64_2nd_v065_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_slope(marketcap, 8), 4), 12))
def cg_f038_market_capitalization_core65_2nd_v066_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_z(marketcap, 12), 4), 12))
def cg_f038_market_capitalization_core66_2nd_v067_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 12))
def cg_f038_market_capitalization_core67_2nd_v068_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(close, 4), 12))
def cg_f038_market_capitalization_core68_2nd_v069_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_log(marketcap + 1.0), 4), 12))
def cg_f038_market_capitalization_core69_2nd_v070_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core70_2nd_v071_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(marketcap, 4), 12))
def cg_f038_market_capitalization_core71_2nd_v072_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(sharesbas * close, 4), 12))
def cg_f038_market_capitalization_core72_2nd_v073_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_diff(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core73_2nd_v074_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_pct_change(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core74_2nd_v075_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_slope(marketcap, 8), 4), 12))
def cg_f038_market_capitalization_core75_2nd_v076_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_z(marketcap, 12), 4), 12))
def cg_f038_market_capitalization_core76_2nd_v077_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 12))
def cg_f038_market_capitalization_core77_2nd_v078_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(close, 4), 12))
def cg_f038_market_capitalization_core78_2nd_v079_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_log(marketcap + 1.0), 4), 12))
def cg_f038_market_capitalization_core79_2nd_v080_signal(marketcap, sharesbas, close):
    return _clean(_rank(_diff(_mean(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core80_2nd_v081_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(marketcap, 4), 4))
def cg_f038_market_capitalization_core81_2nd_v082_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(sharesbas * close, 4), 4))
def cg_f038_market_capitalization_core82_2nd_v083_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core83_2nd_v084_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_pct_change(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core84_2nd_v085_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_slope(marketcap, 8), 4), 4))
def cg_f038_market_capitalization_core85_2nd_v086_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_z(marketcap, 12), 4), 4))
def cg_f038_market_capitalization_core86_2nd_v087_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4))
def cg_f038_market_capitalization_core87_2nd_v088_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(close, 4), 4))
def cg_f038_market_capitalization_core88_2nd_v089_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_log(marketcap + 1.0), 4), 4))
def cg_f038_market_capitalization_core89_2nd_v090_signal(marketcap, sharesbas, close):
    return _clean(_mean(_slope(_mean(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core90_2nd_v091_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(marketcap, 4), 4))
def cg_f038_market_capitalization_core91_2nd_v092_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(sharesbas * close, 4), 4))
def cg_f038_market_capitalization_core92_2nd_v093_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core93_2nd_v094_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_pct_change(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core94_2nd_v095_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_slope(marketcap, 8), 4), 4))
def cg_f038_market_capitalization_core95_2nd_v096_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_z(marketcap, 12), 4), 4))
def cg_f038_market_capitalization_core96_2nd_v097_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4))
def cg_f038_market_capitalization_core97_2nd_v098_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(close, 4), 4))
def cg_f038_market_capitalization_core98_2nd_v099_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_log(marketcap + 1.0), 4), 4))
def cg_f038_market_capitalization_core99_2nd_v100_signal(marketcap, sharesbas, close):
    return _clean(_mean(_diff(_mean(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core100_2nd_v101_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(marketcap, 4), 4))
def cg_f038_market_capitalization_core101_2nd_v102_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(sharesbas * close, 4), 4))
def cg_f038_market_capitalization_core102_2nd_v103_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core103_2nd_v104_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_pct_change(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core104_2nd_v105_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_slope(marketcap, 8), 4), 4))
def cg_f038_market_capitalization_core105_2nd_v106_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_z(marketcap, 12), 4), 4))
def cg_f038_market_capitalization_core106_2nd_v107_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4))
def cg_f038_market_capitalization_core107_2nd_v108_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(close, 4), 4))
def cg_f038_market_capitalization_core108_2nd_v109_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_log(marketcap + 1.0), 4), 4))
def cg_f038_market_capitalization_core109_2nd_v110_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_mean(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core110_2nd_v111_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(marketcap, 8), 8))
def cg_f038_market_capitalization_core111_2nd_v112_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(sharesbas * close, 8), 8))
def cg_f038_market_capitalization_core112_2nd_v113_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_diff(marketcap, 4), 8), 8))
def cg_f038_market_capitalization_core113_2nd_v114_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_pct_change(marketcap, 4), 8), 8))
def cg_f038_market_capitalization_core114_2nd_v115_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_slope(marketcap, 8), 8), 8))
def cg_f038_market_capitalization_core115_2nd_v116_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_z(marketcap, 12), 8), 8))
def cg_f038_market_capitalization_core116_2nd_v117_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_safe_div(marketcap, sharesbas.abs() + 1.0), 8), 8))
def cg_f038_market_capitalization_core117_2nd_v118_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(close, 8), 8))
def cg_f038_market_capitalization_core118_2nd_v119_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_log(marketcap + 1.0), 8), 8))
def cg_f038_market_capitalization_core119_2nd_v120_signal(marketcap, sharesbas, close):
    return _clean(_slope(_mean(_mean(marketcap, 4), 8), 8))
def cg_f038_market_capitalization_core120_2nd_v121_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(marketcap, 4), 4))
def cg_f038_market_capitalization_core121_2nd_v122_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(sharesbas * close, 4), 4))
def cg_f038_market_capitalization_core122_2nd_v123_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_diff(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core123_2nd_v124_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_pct_change(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core124_2nd_v125_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_slope(marketcap, 8), 4), 4))
def cg_f038_market_capitalization_core125_2nd_v126_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_z(marketcap, 12), 4), 4))
def cg_f038_market_capitalization_core126_2nd_v127_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4))
def cg_f038_market_capitalization_core127_2nd_v128_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(close, 4), 4))
def cg_f038_market_capitalization_core128_2nd_v129_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_log(marketcap + 1.0), 4), 4))
def cg_f038_market_capitalization_core129_2nd_v130_signal(marketcap, sharesbas, close):
    return _clean(_diff(_mean(_mean(marketcap, 4), 4), 4))
def cg_f038_market_capitalization_core130_2nd_v131_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(marketcap, 4), 4), 8))
def cg_f038_market_capitalization_core131_2nd_v132_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(sharesbas * close, 4), 4), 8))
def cg_f038_market_capitalization_core132_2nd_v133_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_diff(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core133_2nd_v134_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_pct_change(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core134_2nd_v135_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_slope(marketcap, 8), 4), 4), 8))
def cg_f038_market_capitalization_core135_2nd_v136_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_z(marketcap, 12), 4), 4), 8))
def cg_f038_market_capitalization_core136_2nd_v137_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 8))
def cg_f038_market_capitalization_core137_2nd_v138_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(close, 4), 4), 8))
def cg_f038_market_capitalization_core138_2nd_v139_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_log(marketcap + 1.0), 4), 4), 8))
def cg_f038_market_capitalization_core139_2nd_v140_signal(marketcap, sharesbas, close):
    return _clean(_z(_diff(_mean(_mean(marketcap, 4), 4), 4), 8))
def cg_f038_market_capitalization_core140_2nd_v141_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(marketcap, 4), 4), 12))
def cg_f038_market_capitalization_core141_2nd_v142_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(sharesbas * close, 4), 4), 12))
def cg_f038_market_capitalization_core142_2nd_v143_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_diff(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core143_2nd_v144_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_pct_change(marketcap, 4), 4), 4), 12))
def cg_f038_market_capitalization_core144_2nd_v145_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_slope(marketcap, 8), 4), 4), 12))
def cg_f038_market_capitalization_core145_2nd_v146_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_z(marketcap, 12), 4), 4), 12))
def cg_f038_market_capitalization_core146_2nd_v147_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_safe_div(marketcap, sharesbas.abs() + 1.0), 4), 4), 12))
def cg_f038_market_capitalization_core147_2nd_v148_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(close, 4), 4), 12))
def cg_f038_market_capitalization_core148_2nd_v149_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_log(marketcap + 1.0), 4), 4), 12))
def cg_f038_market_capitalization_core149_2nd_v150_signal(marketcap, sharesbas, close):
    return _clean(_rank(_slope(_mean(_mean(marketcap, 4), 4), 4), 12))