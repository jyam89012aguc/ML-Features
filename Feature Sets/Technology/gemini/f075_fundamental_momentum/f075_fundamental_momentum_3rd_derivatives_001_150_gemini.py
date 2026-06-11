import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f075_fundamental_momentum_core00_3rd_v001_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f075_fundamental_momentum_core01_3rd_v002_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(rnd, 4), 4))
def cg_f075_fundamental_momentum_core02_3rd_v003_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(ncfo, 4), 4))
def cg_f075_fundamental_momentum_core03_3rd_v004_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(fcf, 4), 4))
def cg_f075_fundamental_momentum_core04_3rd_v005_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f075_fundamental_momentum_core05_3rd_v006_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(opinc, 4), 4))
def cg_f075_fundamental_momentum_core06_3rd_v007_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_safe_div(fcf, revenue), 4), 4))
def cg_f075_fundamental_momentum_core07_3rd_v008_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_safe_div(ncfo, revenue), 4), 4))
def cg_f075_fundamental_momentum_core08_3rd_v009_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_safe_div(netinc, revenue), 4), 4))
def cg_f075_fundamental_momentum_core09_3rd_v010_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_safe_div(opinc, revenue), 4), 4))
def cg_f075_fundamental_momentum_core10_3rd_v011_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f075_fundamental_momentum_core11_3rd_v012_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(rnd, 4), 8))
def cg_f075_fundamental_momentum_core12_3rd_v013_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(ncfo, 4), 8))
def cg_f075_fundamental_momentum_core13_3rd_v014_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(fcf, 4), 8))
def cg_f075_fundamental_momentum_core14_3rd_v015_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f075_fundamental_momentum_core15_3rd_v016_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(opinc, 4), 8))
def cg_f075_fundamental_momentum_core16_3rd_v017_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_safe_div(fcf, revenue), 4), 8))
def cg_f075_fundamental_momentum_core17_3rd_v018_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_safe_div(ncfo, revenue), 4), 8))
def cg_f075_fundamental_momentum_core18_3rd_v019_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_safe_div(netinc, revenue), 4), 8))
def cg_f075_fundamental_momentum_core19_3rd_v020_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_safe_div(opinc, revenue), 4), 8))
def cg_f075_fundamental_momentum_core20_3rd_v021_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(revenue, 4), 4))
def cg_f075_fundamental_momentum_core21_3rd_v022_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(rnd, 4), 4))
def cg_f075_fundamental_momentum_core22_3rd_v023_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(ncfo, 4), 4))
def cg_f075_fundamental_momentum_core23_3rd_v024_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(fcf, 4), 4))
def cg_f075_fundamental_momentum_core24_3rd_v025_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(netinc, 4), 4))
def cg_f075_fundamental_momentum_core25_3rd_v026_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(opinc, 4), 4))
def cg_f075_fundamental_momentum_core26_3rd_v027_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(_safe_div(fcf, revenue), 4), 4))
def cg_f075_fundamental_momentum_core27_3rd_v028_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(_safe_div(ncfo, revenue), 4), 4))
def cg_f075_fundamental_momentum_core28_3rd_v029_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(_safe_div(netinc, revenue), 4), 4))
def cg_f075_fundamental_momentum_core29_3rd_v030_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_slope(_safe_div(opinc, revenue), 4), 4))
def cg_f075_fundamental_momentum_core30_3rd_v031_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f075_fundamental_momentum_core31_3rd_v032_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(rnd, 4), 4), 8))
def cg_f075_fundamental_momentum_core32_3rd_v033_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(ncfo, 4), 4), 8))
def cg_f075_fundamental_momentum_core33_3rd_v034_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(fcf, 4), 4), 8))
def cg_f075_fundamental_momentum_core34_3rd_v035_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f075_fundamental_momentum_core35_3rd_v036_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(opinc, 4), 4), 8))
def cg_f075_fundamental_momentum_core36_3rd_v037_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(_safe_div(fcf, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core37_3rd_v038_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core38_3rd_v039_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core39_3rd_v040_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_diff(_safe_div(opinc, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core40_3rd_v041_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f075_fundamental_momentum_core41_3rd_v042_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(rnd, 4), 8), 12))
def cg_f075_fundamental_momentum_core42_3rd_v043_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(ncfo, 4), 8), 12))
def cg_f075_fundamental_momentum_core43_3rd_v044_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(fcf, 4), 8), 12))
def cg_f075_fundamental_momentum_core44_3rd_v045_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f075_fundamental_momentum_core45_3rd_v046_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(opinc, 4), 8), 12))
def cg_f075_fundamental_momentum_core46_3rd_v047_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_safe_div(fcf, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core47_3rd_v048_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core48_3rd_v049_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_safe_div(netinc, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core49_3rd_v050_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_safe_div(opinc, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core50_3rd_v051_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(revenue, 4), 4), 8))
def cg_f075_fundamental_momentum_core51_3rd_v052_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(rnd, 4), 4), 8))
def cg_f075_fundamental_momentum_core52_3rd_v053_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(ncfo, 4), 4), 8))
def cg_f075_fundamental_momentum_core53_3rd_v054_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(fcf, 4), 4), 8))
def cg_f075_fundamental_momentum_core54_3rd_v055_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(netinc, 4), 4), 8))
def cg_f075_fundamental_momentum_core55_3rd_v056_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(opinc, 4), 4), 8))
def cg_f075_fundamental_momentum_core56_3rd_v057_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(_safe_div(fcf, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core57_3rd_v058_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core58_3rd_v059_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(_safe_div(netinc, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core59_3rd_v060_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_diff(_slope(_safe_div(opinc, revenue), 4), 4), 8))
def cg_f075_fundamental_momentum_core60_3rd_v061_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f075_fundamental_momentum_core61_3rd_v062_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(rnd, 4), 4), 12))
def cg_f075_fundamental_momentum_core62_3rd_v063_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(ncfo, 4), 4), 12))
def cg_f075_fundamental_momentum_core63_3rd_v064_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(fcf, 4), 4), 12))
def cg_f075_fundamental_momentum_core64_3rd_v065_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f075_fundamental_momentum_core65_3rd_v066_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(opinc, 4), 4), 12))
def cg_f075_fundamental_momentum_core66_3rd_v067_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(_safe_div(fcf, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core67_3rd_v068_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core68_3rd_v069_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core69_3rd_v070_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_diff(_safe_div(opinc, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core70_3rd_v071_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(revenue, 4), 8), 12))
def cg_f075_fundamental_momentum_core71_3rd_v072_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(rnd, 4), 8), 12))
def cg_f075_fundamental_momentum_core72_3rd_v073_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(ncfo, 4), 8), 12))
def cg_f075_fundamental_momentum_core73_3rd_v074_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(fcf, 4), 8), 12))
def cg_f075_fundamental_momentum_core74_3rd_v075_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(netinc, 4), 8), 12))
def cg_f075_fundamental_momentum_core75_3rd_v076_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(opinc, 4), 8), 12))
def cg_f075_fundamental_momentum_core76_3rd_v077_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(_safe_div(fcf, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core77_3rd_v078_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core78_3rd_v079_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(_safe_div(netinc, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core79_3rd_v080_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_slope(_diff(_safe_div(opinc, revenue), 4), 8), 12))
def cg_f075_fundamental_momentum_core80_3rd_v081_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(revenue, 4), 4), 12))
def cg_f075_fundamental_momentum_core81_3rd_v082_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(rnd, 4), 4), 12))
def cg_f075_fundamental_momentum_core82_3rd_v083_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(ncfo, 4), 4), 12))
def cg_f075_fundamental_momentum_core83_3rd_v084_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(fcf, 4), 4), 12))
def cg_f075_fundamental_momentum_core84_3rd_v085_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(netinc, 4), 4), 12))
def cg_f075_fundamental_momentum_core85_3rd_v086_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(opinc, 4), 4), 12))
def cg_f075_fundamental_momentum_core86_3rd_v087_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(_safe_div(fcf, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core87_3rd_v088_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core88_3rd_v089_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(_safe_div(netinc, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core89_3rd_v090_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_rank(_diff(_slope(_safe_div(opinc, revenue), 4), 4), 12))
def cg_f075_fundamental_momentum_core90_3rd_v091_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f075_fundamental_momentum_core91_3rd_v092_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(rnd, 4), 4), 4))
def cg_f075_fundamental_momentum_core92_3rd_v093_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(ncfo, 4), 4), 4))
def cg_f075_fundamental_momentum_core93_3rd_v094_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(fcf, 4), 4), 4))
def cg_f075_fundamental_momentum_core94_3rd_v095_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core95_3rd_v096_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(opinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core96_3rd_v097_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(_safe_div(fcf, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core97_3rd_v098_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core98_3rd_v099_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core99_3rd_v100_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_diff(_safe_div(opinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core100_3rd_v101_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(revenue, 4), 8), 4))
def cg_f075_fundamental_momentum_core101_3rd_v102_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(rnd, 4), 8), 4))
def cg_f075_fundamental_momentum_core102_3rd_v103_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(ncfo, 4), 8), 4))
def cg_f075_fundamental_momentum_core103_3rd_v104_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(fcf, 4), 8), 4))
def cg_f075_fundamental_momentum_core104_3rd_v105_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(netinc, 4), 8), 4))
def cg_f075_fundamental_momentum_core105_3rd_v106_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(opinc, 4), 8), 4))
def cg_f075_fundamental_momentum_core106_3rd_v107_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(_safe_div(fcf, revenue), 4), 8), 4))
def cg_f075_fundamental_momentum_core107_3rd_v108_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, revenue), 4), 8), 4))
def cg_f075_fundamental_momentum_core108_3rd_v109_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(_safe_div(netinc, revenue), 4), 8), 4))
def cg_f075_fundamental_momentum_core109_3rd_v110_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_slope(_diff(_safe_div(opinc, revenue), 4), 8), 4))
def cg_f075_fundamental_momentum_core110_3rd_v111_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(revenue, 4), 4), 4))
def cg_f075_fundamental_momentum_core111_3rd_v112_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(rnd, 4), 4), 4))
def cg_f075_fundamental_momentum_core112_3rd_v113_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(ncfo, 4), 4), 4))
def cg_f075_fundamental_momentum_core113_3rd_v114_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(fcf, 4), 4), 4))
def cg_f075_fundamental_momentum_core114_3rd_v115_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(netinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core115_3rd_v116_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(opinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core116_3rd_v117_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(_safe_div(fcf, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core117_3rd_v118_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core118_3rd_v119_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core119_3rd_v120_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_mean(_diff(_slope(_safe_div(opinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core120_3rd_v121_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(revenue, 4), 4), 4))
def cg_f075_fundamental_momentum_core121_3rd_v122_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(rnd, 4), 4), 4))
def cg_f075_fundamental_momentum_core122_3rd_v123_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(ncfo, 4), 4), 4))
def cg_f075_fundamental_momentum_core123_3rd_v124_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(fcf, 4), 4), 4))
def cg_f075_fundamental_momentum_core124_3rd_v125_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core125_3rd_v126_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(opinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core126_3rd_v127_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(_safe_div(fcf, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core127_3rd_v128_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core128_3rd_v129_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core129_3rd_v130_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_slope(_diff(_diff(_safe_div(opinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core130_3rd_v131_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(revenue, 4), 4), 4))
def cg_f075_fundamental_momentum_core131_3rd_v132_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(rnd, 4), 4), 4))
def cg_f075_fundamental_momentum_core132_3rd_v133_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(ncfo, 4), 4), 4))
def cg_f075_fundamental_momentum_core133_3rd_v134_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(fcf, 4), 4), 4))
def cg_f075_fundamental_momentum_core134_3rd_v135_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core135_3rd_v136_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(opinc, 4), 4), 4))
def cg_f075_fundamental_momentum_core136_3rd_v137_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(_safe_div(fcf, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core137_3rd_v138_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core138_3rd_v139_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core139_3rd_v140_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_diff(_diff(_diff(_safe_div(opinc, revenue), 4), 4), 4))
def cg_f075_fundamental_momentum_core140_3rd_v141_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(revenue, 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core141_3rd_v142_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(rnd, 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core142_3rd_v143_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(ncfo, 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core143_3rd_v144_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(fcf, 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core144_3rd_v145_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core145_3rd_v146_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(opinc, 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core146_3rd_v147_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(fcf, revenue), 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core147_3rd_v148_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, revenue), 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core148_3rd_v149_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(netinc, revenue), 4), 4), 4), 8))
def cg_f075_fundamental_momentum_core149_3rd_v150_signal(revenue, rnd, ncfo, fcf, netinc, opinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(opinc, revenue), 4), 4), 4), 8))