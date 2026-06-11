import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f021_stock_based_compensation_core00_2nd_v001_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(sbcomp, 4))
def cg_f021_stock_based_compensation_core01_2nd_v002_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core02_2nd_v003_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core03_2nd_v004_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, opex), 4))
def cg_f021_stock_based_compensation_core04_2nd_v005_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, sharesbas), 4))
def cg_f021_stock_based_compensation_core05_2nd_v006_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(rnd + sgna, opex), 4))
def cg_f021_stock_based_compensation_core06_2nd_v007_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_log(sbcomp.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core07_2nd_v008_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4))
def cg_f021_stock_based_compensation_core08_2nd_v009_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core09_2nd_v010_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4))
def cg_f021_stock_based_compensation_core10_2nd_v011_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(sbcomp, 8))
def cg_f021_stock_based_compensation_core11_2nd_v012_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core12_2nd_v013_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core13_2nd_v014_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, opex), 8))
def cg_f021_stock_based_compensation_core14_2nd_v015_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, sharesbas), 8))
def cg_f021_stock_based_compensation_core15_2nd_v016_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(rnd + sgna, opex), 8))
def cg_f021_stock_based_compensation_core16_2nd_v017_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_log(sbcomp.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core17_2nd_v018_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 8))
def cg_f021_stock_based_compensation_core18_2nd_v019_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 8))
def cg_f021_stock_based_compensation_core19_2nd_v020_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 8))
def cg_f021_stock_based_compensation_core20_2nd_v021_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(sbcomp, 4))
def cg_f021_stock_based_compensation_core21_2nd_v022_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core22_2nd_v023_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core23_2nd_v024_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, opex), 4))
def cg_f021_stock_based_compensation_core24_2nd_v025_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, sharesbas), 4))
def cg_f021_stock_based_compensation_core25_2nd_v026_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(rnd + sgna, opex), 4))
def cg_f021_stock_based_compensation_core26_2nd_v027_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_log(sbcomp.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core27_2nd_v028_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4))
def cg_f021_stock_based_compensation_core28_2nd_v029_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4))
def cg_f021_stock_based_compensation_core29_2nd_v030_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4))
def cg_f021_stock_based_compensation_core30_2nd_v031_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(sbcomp, 4), 8))
def cg_f021_stock_based_compensation_core31_2nd_v032_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core32_2nd_v033_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core33_2nd_v034_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, opex), 4), 8))
def cg_f021_stock_based_compensation_core34_2nd_v035_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, sharesbas), 4), 8))
def cg_f021_stock_based_compensation_core35_2nd_v036_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(rnd + sgna, opex), 4), 8))
def cg_f021_stock_based_compensation_core36_2nd_v037_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_log(sbcomp.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core37_2nd_v038_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 8))
def cg_f021_stock_based_compensation_core38_2nd_v039_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core39_2nd_v040_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core40_2nd_v041_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(sbcomp, 8), 12))
def cg_f021_stock_based_compensation_core41_2nd_v042_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 8), 12))
def cg_f021_stock_based_compensation_core42_2nd_v043_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 8), 12))
def cg_f021_stock_based_compensation_core43_2nd_v044_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, opex), 8), 12))
def cg_f021_stock_based_compensation_core44_2nd_v045_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, sharesbas), 8), 12))
def cg_f021_stock_based_compensation_core45_2nd_v046_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(rnd + sgna, opex), 8), 12))
def cg_f021_stock_based_compensation_core46_2nd_v047_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_log(sbcomp.abs() + 1.0), 8), 12))
def cg_f021_stock_based_compensation_core47_2nd_v048_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 8), 12))
def cg_f021_stock_based_compensation_core48_2nd_v049_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 8), 12))
def cg_f021_stock_based_compensation_core49_2nd_v050_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 8), 12))
def cg_f021_stock_based_compensation_core50_2nd_v051_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(sbcomp, 4), 8))
def cg_f021_stock_based_compensation_core51_2nd_v052_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core52_2nd_v053_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core53_2nd_v054_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, opex), 4), 8))
def cg_f021_stock_based_compensation_core54_2nd_v055_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, sharesbas), 4), 8))
def cg_f021_stock_based_compensation_core55_2nd_v056_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(rnd + sgna, opex), 4), 8))
def cg_f021_stock_based_compensation_core56_2nd_v057_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_log(sbcomp.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core57_2nd_v058_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 8))
def cg_f021_stock_based_compensation_core58_2nd_v059_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core59_2nd_v060_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 8))
def cg_f021_stock_based_compensation_core60_2nd_v061_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(sbcomp, 4), 12))
def cg_f021_stock_based_compensation_core61_2nd_v062_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core62_2nd_v063_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core63_2nd_v064_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, opex), 4), 12))
def cg_f021_stock_based_compensation_core64_2nd_v065_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, sharesbas), 4), 12))
def cg_f021_stock_based_compensation_core65_2nd_v066_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(rnd + sgna, opex), 4), 12))
def cg_f021_stock_based_compensation_core66_2nd_v067_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_log(sbcomp.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core67_2nd_v068_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 12))
def cg_f021_stock_based_compensation_core68_2nd_v069_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core69_2nd_v070_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core70_2nd_v071_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(sbcomp, 4), 12))
def cg_f021_stock_based_compensation_core71_2nd_v072_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core72_2nd_v073_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core73_2nd_v074_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, opex), 4), 12))
def cg_f021_stock_based_compensation_core74_2nd_v075_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, sharesbas), 4), 12))
def cg_f021_stock_based_compensation_core75_2nd_v076_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(rnd + sgna, opex), 4), 12))
def cg_f021_stock_based_compensation_core76_2nd_v077_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_log(sbcomp.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core77_2nd_v078_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 12))
def cg_f021_stock_based_compensation_core78_2nd_v079_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core79_2nd_v080_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 12))
def cg_f021_stock_based_compensation_core80_2nd_v081_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(sbcomp, 4), 4))
def cg_f021_stock_based_compensation_core81_2nd_v082_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core82_2nd_v083_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core83_2nd_v084_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, opex), 4), 4))
def cg_f021_stock_based_compensation_core84_2nd_v085_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, sharesbas), 4), 4))
def cg_f021_stock_based_compensation_core85_2nd_v086_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(rnd + sgna, opex), 4), 4))
def cg_f021_stock_based_compensation_core86_2nd_v087_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core87_2nd_v088_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4))
def cg_f021_stock_based_compensation_core88_2nd_v089_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core89_2nd_v090_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_slope(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core90_2nd_v091_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(sbcomp, 4), 4))
def cg_f021_stock_based_compensation_core91_2nd_v092_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core92_2nd_v093_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core93_2nd_v094_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, opex), 4), 4))
def cg_f021_stock_based_compensation_core94_2nd_v095_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, sharesbas), 4), 4))
def cg_f021_stock_based_compensation_core95_2nd_v096_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(rnd + sgna, opex), 4), 4))
def cg_f021_stock_based_compensation_core96_2nd_v097_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core97_2nd_v098_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4))
def cg_f021_stock_based_compensation_core98_2nd_v099_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core99_2nd_v100_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_mean(_diff(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core100_2nd_v101_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(sbcomp, 4), 4))
def cg_f021_stock_based_compensation_core101_2nd_v102_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core102_2nd_v103_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core103_2nd_v104_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, opex), 4), 4))
def cg_f021_stock_based_compensation_core104_2nd_v105_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, sharesbas), 4), 4))
def cg_f021_stock_based_compensation_core105_2nd_v106_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(rnd + sgna, opex), 4), 4))
def cg_f021_stock_based_compensation_core106_2nd_v107_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core107_2nd_v108_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4))
def cg_f021_stock_based_compensation_core108_2nd_v109_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core109_2nd_v110_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core110_2nd_v111_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(sbcomp, 8), 8))
def cg_f021_stock_based_compensation_core111_2nd_v112_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, rnd.abs() + 1.0), 8), 8))
def cg_f021_stock_based_compensation_core112_2nd_v113_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, sgna.abs() + 1.0), 8), 8))
def cg_f021_stock_based_compensation_core113_2nd_v114_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, opex), 8), 8))
def cg_f021_stock_based_compensation_core114_2nd_v115_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, sharesbas), 8), 8))
def cg_f021_stock_based_compensation_core115_2nd_v116_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(rnd + sgna, opex), 8), 8))
def cg_f021_stock_based_compensation_core116_2nd_v117_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_log(sbcomp.abs() + 1.0), 8), 8))
def cg_f021_stock_based_compensation_core117_2nd_v118_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, _mean(sbcomp, 8)), 8), 8))
def cg_f021_stock_based_compensation_core118_2nd_v119_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, opex.abs() + 1.0), 8), 8))
def cg_f021_stock_based_compensation_core119_2nd_v120_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_slope(_mean(_safe_div(sbcomp, rnd + sgna + 1.0), 8), 8))
def cg_f021_stock_based_compensation_core120_2nd_v121_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(sbcomp, 4), 4))
def cg_f021_stock_based_compensation_core121_2nd_v122_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core122_2nd_v123_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core123_2nd_v124_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, opex), 4), 4))
def cg_f021_stock_based_compensation_core124_2nd_v125_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, sharesbas), 4), 4))
def cg_f021_stock_based_compensation_core125_2nd_v126_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(rnd + sgna, opex), 4), 4))
def cg_f021_stock_based_compensation_core126_2nd_v127_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_log(sbcomp.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core127_2nd_v128_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4))
def cg_f021_stock_based_compensation_core128_2nd_v129_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core129_2nd_v130_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_diff(_mean(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4))
def cg_f021_stock_based_compensation_core130_2nd_v131_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(sbcomp, 4), 4), 8))
def cg_f021_stock_based_compensation_core131_2nd_v132_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core132_2nd_v133_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core133_2nd_v134_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, opex), 4), 4), 8))
def cg_f021_stock_based_compensation_core134_2nd_v135_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, sharesbas), 4), 4), 8))
def cg_f021_stock_based_compensation_core135_2nd_v136_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(rnd + sgna, opex), 4), 4), 8))
def cg_f021_stock_based_compensation_core136_2nd_v137_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_log(sbcomp.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core137_2nd_v138_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 8))
def cg_f021_stock_based_compensation_core138_2nd_v139_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core139_2nd_v140_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 8))
def cg_f021_stock_based_compensation_core140_2nd_v141_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(sbcomp, 4), 4), 12))
def cg_f021_stock_based_compensation_core141_2nd_v142_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, rnd.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core142_2nd_v143_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, sgna.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core143_2nd_v144_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, opex), 4), 4), 12))
def cg_f021_stock_based_compensation_core144_2nd_v145_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, sharesbas), 4), 4), 12))
def cg_f021_stock_based_compensation_core145_2nd_v146_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(rnd + sgna, opex), 4), 4), 12))
def cg_f021_stock_based_compensation_core146_2nd_v147_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_log(sbcomp.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core147_2nd_v148_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, _mean(sbcomp, 8)), 4), 4), 12))
def cg_f021_stock_based_compensation_core148_2nd_v149_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, opex.abs() + 1.0), 4), 4), 12))
def cg_f021_stock_based_compensation_core149_2nd_v150_signal(sbcomp, rnd, sgna, opex, sharesbas):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, rnd + sgna + 1.0), 4), 4), 12))