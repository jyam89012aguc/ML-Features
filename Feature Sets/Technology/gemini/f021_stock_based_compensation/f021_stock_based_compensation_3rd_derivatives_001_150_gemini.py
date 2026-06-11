import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f021_stock_based_compensation_core00_3rd_v001_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(sbcomp, 4), 4))
def cg_f021_stock_based_compensation_core01_3rd_v002_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core02_3rd_v003_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core03_3rd_v004_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, opex), 4), 4))
def cg_f021_stock_based_compensation_core04_3rd_v005_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4))
def cg_f021_stock_based_compensation_core05_3rd_v006_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4))
def cg_f021_stock_based_compensation_core06_3rd_v007_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core07_3rd_v008_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4))
def cg_f021_stock_based_compensation_core08_3rd_v009_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core09_3rd_v010_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core10_3rd_v011_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(sbcomp, 4), 8))
def cg_f021_stock_based_compensation_core11_3rd_v012_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core12_3rd_v013_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core13_3rd_v014_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, opex), 4), 8))
def cg_f021_stock_based_compensation_core14_3rd_v015_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, sharesbas), 4), 8))
def cg_f021_stock_based_compensation_core15_3rd_v016_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(rnd + sgna, opex), 4), 8))
def cg_f021_stock_based_compensation_core16_3rd_v017_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core17_3rd_v018_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 8))
def cg_f021_stock_based_compensation_core18_3rd_v019_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core19_3rd_v020_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core20_3rd_v021_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(sbcomp, 4), 4))
def cg_f021_stock_based_compensation_core21_3rd_v022_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core22_3rd_v023_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core23_3rd_v024_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, opex), 4), 4))
def cg_f021_stock_based_compensation_core24_3rd_v025_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, sharesbas), 4), 4))
def cg_f021_stock_based_compensation_core25_3rd_v026_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(rnd + sgna, opex), 4), 4))
def cg_f021_stock_based_compensation_core26_3rd_v027_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core27_3rd_v028_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4))
def cg_f021_stock_based_compensation_core28_3rd_v029_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core29_3rd_v030_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core30_3rd_v031_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(sbcomp, 4), 4), 8))
def cg_f021_stock_based_compensation_core31_3rd_v032_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core32_3rd_v033_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core33_3rd_v034_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, opex), 4), 4), 8))
def cg_f021_stock_based_compensation_core34_3rd_v035_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4), 8))
def cg_f021_stock_based_compensation_core35_3rd_v036_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4), 8))
def cg_f021_stock_based_compensation_core36_3rd_v037_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core37_3rd_v038_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 8))
def cg_f021_stock_based_compensation_core38_3rd_v039_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core39_3rd_v040_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core40_3rd_v041_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f021_stock_based_compensation_core41_3rd_v042_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core42_3rd_v043_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core43_3rd_v044_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, opex), 4), 8), 12))
def cg_f021_stock_based_compensation_core44_3rd_v045_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, sharesbas), 4), 8), 12))
def cg_f021_stock_based_compensation_core45_3rd_v046_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(rnd + sgna, opex), 4), 8), 12))
def cg_f021_stock_based_compensation_core46_3rd_v047_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core47_3rd_v048_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 8), 12))
def cg_f021_stock_based_compensation_core48_3rd_v049_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core49_3rd_v050_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core50_3rd_v051_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(sbcomp, 4), 4), 8))
def cg_f021_stock_based_compensation_core51_3rd_v052_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core52_3rd_v053_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core53_3rd_v054_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, opex), 4), 4), 8))
def cg_f021_stock_based_compensation_core54_3rd_v055_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, sharesbas), 4), 4), 8))
def cg_f021_stock_based_compensation_core55_3rd_v056_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(rnd + sgna, opex), 4), 4), 8))
def cg_f021_stock_based_compensation_core56_3rd_v057_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core57_3rd_v058_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 8))
def cg_f021_stock_based_compensation_core58_3rd_v059_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core59_3rd_v060_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core60_3rd_v061_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(sbcomp, 4), 4), 12))
def cg_f021_stock_based_compensation_core61_3rd_v062_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core62_3rd_v063_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core63_3rd_v064_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, opex), 4), 4), 12))
def cg_f021_stock_based_compensation_core64_3rd_v065_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4), 12))
def cg_f021_stock_based_compensation_core65_3rd_v066_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4), 12))
def cg_f021_stock_based_compensation_core66_3rd_v067_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core67_3rd_v068_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 12))
def cg_f021_stock_based_compensation_core68_3rd_v069_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core69_3rd_v070_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core70_3rd_v071_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f021_stock_based_compensation_core71_3rd_v072_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core72_3rd_v073_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core73_3rd_v074_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, opex), 4), 8), 12))
def cg_f021_stock_based_compensation_core74_3rd_v075_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, sharesbas), 4), 8), 12))
def cg_f021_stock_based_compensation_core75_3rd_v076_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(rnd + sgna, opex), 4), 8), 12))
def cg_f021_stock_based_compensation_core76_3rd_v077_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core77_3rd_v078_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 8), 12))
def cg_f021_stock_based_compensation_core78_3rd_v079_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core79_3rd_v080_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 8), 12))
def cg_f021_stock_based_compensation_core80_3rd_v081_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(sbcomp, 4), 4), 12))
def cg_f021_stock_based_compensation_core81_3rd_v082_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core82_3rd_v083_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core83_3rd_v084_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, opex), 4), 4), 12))
def cg_f021_stock_based_compensation_core84_3rd_v085_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, sharesbas), 4), 4), 12))
def cg_f021_stock_based_compensation_core85_3rd_v086_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(rnd + sgna, opex), 4), 4), 12))
def cg_f021_stock_based_compensation_core86_3rd_v087_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core87_3rd_v088_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 12))
def cg_f021_stock_based_compensation_core88_3rd_v089_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core89_3rd_v090_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core90_3rd_v091_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f021_stock_based_compensation_core91_3rd_v092_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core92_3rd_v093_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core93_3rd_v094_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core94_3rd_v095_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4), 4))
def cg_f021_stock_based_compensation_core95_3rd_v096_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core96_3rd_v097_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core97_3rd_v098_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 4))
def cg_f021_stock_based_compensation_core98_3rd_v099_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core99_3rd_v100_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core100_3rd_v101_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(sbcomp, 4), 8), 4))
def cg_f021_stock_based_compensation_core101_3rd_v102_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 8), 4))
def cg_f021_stock_based_compensation_core102_3rd_v103_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 8), 4))
def cg_f021_stock_based_compensation_core103_3rd_v104_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, opex), 4), 8), 4))
def cg_f021_stock_based_compensation_core104_3rd_v105_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, sharesbas), 4), 8), 4))
def cg_f021_stock_based_compensation_core105_3rd_v106_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(rnd + sgna, opex), 4), 8), 4))
def cg_f021_stock_based_compensation_core106_3rd_v107_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_log(sbcomp.abs() + 1.0), 4), 8), 4))
def cg_f021_stock_based_compensation_core107_3rd_v108_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 8), 4))
def cg_f021_stock_based_compensation_core108_3rd_v109_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 8), 4))
def cg_f021_stock_based_compensation_core109_3rd_v110_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 8), 4))
def cg_f021_stock_based_compensation_core110_3rd_v111_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(sbcomp, 4), 4), 4))
def cg_f021_stock_based_compensation_core111_3rd_v112_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core112_3rd_v113_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core113_3rd_v114_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core114_3rd_v115_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, sharesbas), 4), 4), 4))
def cg_f021_stock_based_compensation_core115_3rd_v116_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(rnd + sgna, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core116_3rd_v117_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core117_3rd_v118_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 4))
def cg_f021_stock_based_compensation_core118_3rd_v119_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core119_3rd_v120_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core120_3rd_v121_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f021_stock_based_compensation_core121_3rd_v122_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core122_3rd_v123_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core123_3rd_v124_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core124_3rd_v125_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4), 4))
def cg_f021_stock_based_compensation_core125_3rd_v126_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core126_3rd_v127_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core127_3rd_v128_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 4))
def cg_f021_stock_based_compensation_core128_3rd_v129_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core129_3rd_v130_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core130_3rd_v131_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f021_stock_based_compensation_core131_3rd_v132_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core132_3rd_v133_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core133_3rd_v134_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core134_3rd_v135_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4), 4))
def cg_f021_stock_based_compensation_core135_3rd_v136_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4), 4))
def cg_f021_stock_based_compensation_core136_3rd_v137_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core137_3rd_v138_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 4))
def cg_f021_stock_based_compensation_core138_3rd_v139_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core139_3rd_v140_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 4))
def cg_f021_stock_based_compensation_core140_3rd_v141_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(sbcomp, 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core141_3rd_v142_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core142_3rd_v143_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core143_3rd_v144_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, opex), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core144_3rd_v145_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, sharesbas), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core145_3rd_v146_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd + sgna, opex), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core146_3rd_v147_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_log(sbcomp.abs() + 1.0), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core147_3rd_v148_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core148_3rd_v149_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 4), 8))
def cg_f021_stock_based_compensation_core149_3rd_v150_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 4), 8))