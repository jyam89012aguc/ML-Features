import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f100_index_membership_and_relative_context_core00_3rd_v001_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(marketcap, 4), 4))
def cg_f100_index_membership_and_relative_context_core01_3rd_v002_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_log(marketcap + 1.0), 4), 4))
def cg_f100_index_membership_and_relative_context_core02_3rd_v003_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_z(marketcap, 20), 4), 4))
def cg_f100_index_membership_and_relative_context_core03_3rd_v004_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_rank(marketcap, 20), 4), 4))
def cg_f100_index_membership_and_relative_context_core04_3rd_v005_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_mean(marketcap, 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core05_3rd_v006_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(marketcap.abs(), 4), 4))
def cg_f100_index_membership_and_relative_context_core06_3rd_v007_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4))
def cg_f100_index_membership_and_relative_context_core07_3rd_v008_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4))
def cg_f100_index_membership_and_relative_context_core08_3rd_v009_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_to_num(marketcap), 4), 4))
def cg_f100_index_membership_and_relative_context_core09_3rd_v010_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_clean(marketcap), 4), 4))
def cg_f100_index_membership_and_relative_context_core10_3rd_v011_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(marketcap, 4), 8))
def cg_f100_index_membership_and_relative_context_core11_3rd_v012_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_log(marketcap + 1.0), 4), 8))
def cg_f100_index_membership_and_relative_context_core12_3rd_v013_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_z(marketcap, 20), 4), 8))
def cg_f100_index_membership_and_relative_context_core13_3rd_v014_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_rank(marketcap, 20), 4), 8))
def cg_f100_index_membership_and_relative_context_core14_3rd_v015_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_mean(marketcap, 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core15_3rd_v016_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(marketcap.abs(), 4), 8))
def cg_f100_index_membership_and_relative_context_core16_3rd_v017_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_safe_div(marketcap, 1e9), 4), 8))
def cg_f100_index_membership_and_relative_context_core17_3rd_v018_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_log(marketcap / 1e6 + 1.0), 4), 8))
def cg_f100_index_membership_and_relative_context_core18_3rd_v019_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_to_num(marketcap), 4), 8))
def cg_f100_index_membership_and_relative_context_core19_3rd_v020_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_clean(marketcap), 4), 8))
def cg_f100_index_membership_and_relative_context_core20_3rd_v021_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(marketcap, 4), 4))
def cg_f100_index_membership_and_relative_context_core21_3rd_v022_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_log(marketcap + 1.0), 4), 4))
def cg_f100_index_membership_and_relative_context_core22_3rd_v023_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_z(marketcap, 20), 4), 4))
def cg_f100_index_membership_and_relative_context_core23_3rd_v024_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_rank(marketcap, 20), 4), 4))
def cg_f100_index_membership_and_relative_context_core24_3rd_v025_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_mean(marketcap, 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core25_3rd_v026_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(marketcap.abs(), 4), 4))
def cg_f100_index_membership_and_relative_context_core26_3rd_v027_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_safe_div(marketcap, 1e9), 4), 4))
def cg_f100_index_membership_and_relative_context_core27_3rd_v028_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_log(marketcap / 1e6 + 1.0), 4), 4))
def cg_f100_index_membership_and_relative_context_core28_3rd_v029_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_to_num(marketcap), 4), 4))
def cg_f100_index_membership_and_relative_context_core29_3rd_v030_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_slope(_clean(marketcap), 4), 4))
def cg_f100_index_membership_and_relative_context_core30_3rd_v031_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(marketcap, 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core31_3rd_v032_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_log(marketcap + 1.0), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core32_3rd_v033_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_z(marketcap, 20), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core33_3rd_v034_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_rank(marketcap, 20), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core34_3rd_v035_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_mean(marketcap, 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core35_3rd_v036_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(marketcap.abs(), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core36_3rd_v037_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core37_3rd_v038_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core38_3rd_v039_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_to_num(marketcap), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core39_3rd_v040_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_diff(_clean(marketcap), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core40_3rd_v041_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(marketcap, 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core41_3rd_v042_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_log(marketcap + 1.0), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core42_3rd_v043_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_z(marketcap, 20), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core43_3rd_v044_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_rank(marketcap, 20), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core44_3rd_v045_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_mean(marketcap, 4), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core45_3rd_v046_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(marketcap.abs(), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core46_3rd_v047_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(marketcap, 1e9), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core47_3rd_v048_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_log(marketcap / 1e6 + 1.0), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core48_3rd_v049_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_to_num(marketcap), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core49_3rd_v050_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_clean(marketcap), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core50_3rd_v051_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(marketcap, 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core51_3rd_v052_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_log(marketcap + 1.0), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core52_3rd_v053_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_z(marketcap, 20), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core53_3rd_v054_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_rank(marketcap, 20), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core54_3rd_v055_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_mean(marketcap, 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core55_3rd_v056_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(marketcap.abs(), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core56_3rd_v057_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(marketcap, 1e9), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core57_3rd_v058_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_log(marketcap / 1e6 + 1.0), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core58_3rd_v059_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_to_num(marketcap), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core59_3rd_v060_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_diff(_slope(_clean(marketcap), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core60_3rd_v061_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(marketcap, 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core61_3rd_v062_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_log(marketcap + 1.0), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core62_3rd_v063_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_z(marketcap, 20), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core63_3rd_v064_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_rank(marketcap, 20), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core64_3rd_v065_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_mean(marketcap, 4), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core65_3rd_v066_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(marketcap.abs(), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core66_3rd_v067_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core67_3rd_v068_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core68_3rd_v069_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_to_num(marketcap), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core69_3rd_v070_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_diff(_clean(marketcap), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core70_3rd_v071_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(marketcap, 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core71_3rd_v072_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_log(marketcap + 1.0), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core72_3rd_v073_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_z(marketcap, 20), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core73_3rd_v074_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_rank(marketcap, 20), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core74_3rd_v075_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_mean(marketcap, 4), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core75_3rd_v076_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(marketcap.abs(), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core76_3rd_v077_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(marketcap, 1e9), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core77_3rd_v078_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_log(marketcap / 1e6 + 1.0), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core78_3rd_v079_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_to_num(marketcap), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core79_3rd_v080_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_slope(_diff(_clean(marketcap), 4), 8), 12))
def cg_f100_index_membership_and_relative_context_core80_3rd_v081_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(marketcap, 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core81_3rd_v082_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_log(marketcap + 1.0), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core82_3rd_v083_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_z(marketcap, 20), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core83_3rd_v084_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_rank(marketcap, 20), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core84_3rd_v085_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_mean(marketcap, 4), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core85_3rd_v086_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(marketcap.abs(), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core86_3rd_v087_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(marketcap, 1e9), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core87_3rd_v088_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_log(marketcap / 1e6 + 1.0), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core88_3rd_v089_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_to_num(marketcap), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core89_3rd_v090_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_rank(_diff(_slope(_clean(marketcap), 4), 4), 12))
def cg_f100_index_membership_and_relative_context_core90_3rd_v091_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(marketcap, 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core91_3rd_v092_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core92_3rd_v093_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_z(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core93_3rd_v094_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_rank(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core94_3rd_v095_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_mean(marketcap, 4), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core95_3rd_v096_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(marketcap.abs(), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core96_3rd_v097_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core97_3rd_v098_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core98_3rd_v099_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_to_num(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core99_3rd_v100_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_diff(_clean(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core100_3rd_v101_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(marketcap, 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core101_3rd_v102_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_log(marketcap + 1.0), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core102_3rd_v103_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_z(marketcap, 20), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core103_3rd_v104_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_rank(marketcap, 20), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core104_3rd_v105_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_mean(marketcap, 4), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core105_3rd_v106_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(marketcap.abs(), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core106_3rd_v107_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(marketcap, 1e9), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core107_3rd_v108_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_log(marketcap / 1e6 + 1.0), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core108_3rd_v109_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_to_num(marketcap), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core109_3rd_v110_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_slope(_diff(_clean(marketcap), 4), 8), 4))
def cg_f100_index_membership_and_relative_context_core110_3rd_v111_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(marketcap, 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core111_3rd_v112_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_log(marketcap + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core112_3rd_v113_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_z(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core113_3rd_v114_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_rank(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core114_3rd_v115_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_mean(marketcap, 4), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core115_3rd_v116_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(marketcap.abs(), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core116_3rd_v117_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(marketcap, 1e9), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core117_3rd_v118_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_log(marketcap / 1e6 + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core118_3rd_v119_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_to_num(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core119_3rd_v120_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_mean(_diff(_slope(_clean(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core120_3rd_v121_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(marketcap, 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core121_3rd_v122_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core122_3rd_v123_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_z(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core123_3rd_v124_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_rank(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core124_3rd_v125_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_mean(marketcap, 4), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core125_3rd_v126_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(marketcap.abs(), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core126_3rd_v127_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core127_3rd_v128_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core128_3rd_v129_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_to_num(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core129_3rd_v130_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_slope(_diff(_diff(_clean(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core130_3rd_v131_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(marketcap, 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core131_3rd_v132_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core132_3rd_v133_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_z(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core133_3rd_v134_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_rank(marketcap, 20), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core134_3rd_v135_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_mean(marketcap, 4), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core135_3rd_v136_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(marketcap.abs(), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core136_3rd_v137_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core137_3rd_v138_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core138_3rd_v139_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_to_num(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core139_3rd_v140_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_diff(_diff(_diff(_clean(marketcap), 4), 4), 4))
def cg_f100_index_membership_and_relative_context_core140_3rd_v141_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(marketcap, 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core141_3rd_v142_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_log(marketcap + 1.0), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core142_3rd_v143_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_z(marketcap, 20), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core143_3rd_v144_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_rank(marketcap, 20), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core144_3rd_v145_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_mean(marketcap, 4), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core145_3rd_v146_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(marketcap.abs(), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core146_3rd_v147_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(marketcap, 1e9), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core147_3rd_v148_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_log(marketcap / 1e6 + 1.0), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core148_3rd_v149_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_to_num(marketcap), 4), 4), 4), 8))
def cg_f100_index_membership_and_relative_context_core149_3rd_v150_signal(date, action, ticker, sector, industry, marketcap):
    return _clean(_z(_slope(_diff(_diff(_clean(marketcap), 4), 4), 4), 8))