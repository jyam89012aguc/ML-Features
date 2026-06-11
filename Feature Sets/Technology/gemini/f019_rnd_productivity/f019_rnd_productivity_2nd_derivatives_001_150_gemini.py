import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f019_rnd_productivity_core00_2nd_v001_signal(revenue, gp, rnd):
    return _clean(_slope(rnd, 4))
def cg_f019_rnd_productivity_core01_2nd_v002_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core02_2nd_v003_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(gp, rnd.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core03_2nd_v004_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(gp, revenue), 4))
def cg_f019_rnd_productivity_core04_2nd_v005_signal(revenue, gp, rnd):
    return _clean(_slope(revenue - rnd, 4))
def cg_f019_rnd_productivity_core05_2nd_v006_signal(revenue, gp, rnd):
    return _clean(_slope(gp - rnd, 4))
def cg_f019_rnd_productivity_core06_2nd_v007_signal(revenue, gp, rnd):
    return _clean(_slope(_log(revenue.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core07_2nd_v008_signal(revenue, gp, rnd):
    return _clean(_slope(_log(gp.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core08_2nd_v009_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(revenue, gp), 4))
def cg_f019_rnd_productivity_core09_2nd_v010_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(rnd, gp.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core10_2nd_v011_signal(revenue, gp, rnd):
    return _clean(_slope(rnd, 8))
def cg_f019_rnd_productivity_core11_2nd_v012_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(revenue, rnd.abs() + 1.0), 8))
def cg_f019_rnd_productivity_core12_2nd_v013_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(gp, rnd.abs() + 1.0), 8))
def cg_f019_rnd_productivity_core13_2nd_v014_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(gp, revenue), 8))
def cg_f019_rnd_productivity_core14_2nd_v015_signal(revenue, gp, rnd):
    return _clean(_slope(revenue - rnd, 8))
def cg_f019_rnd_productivity_core15_2nd_v016_signal(revenue, gp, rnd):
    return _clean(_slope(gp - rnd, 8))
def cg_f019_rnd_productivity_core16_2nd_v017_signal(revenue, gp, rnd):
    return _clean(_slope(_log(revenue.abs() + 1.0), 8))
def cg_f019_rnd_productivity_core17_2nd_v018_signal(revenue, gp, rnd):
    return _clean(_slope(_log(gp.abs() + 1.0), 8))
def cg_f019_rnd_productivity_core18_2nd_v019_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(revenue, gp), 8))
def cg_f019_rnd_productivity_core19_2nd_v020_signal(revenue, gp, rnd):
    return _clean(_slope(_safe_div(rnd, gp.abs() + 1.0), 8))
def cg_f019_rnd_productivity_core20_2nd_v021_signal(revenue, gp, rnd):
    return _clean(_diff(rnd, 4))
def cg_f019_rnd_productivity_core21_2nd_v022_signal(revenue, gp, rnd):
    return _clean(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core22_2nd_v023_signal(revenue, gp, rnd):
    return _clean(_diff(_safe_div(gp, rnd.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core23_2nd_v024_signal(revenue, gp, rnd):
    return _clean(_diff(_safe_div(gp, revenue), 4))
def cg_f019_rnd_productivity_core24_2nd_v025_signal(revenue, gp, rnd):
    return _clean(_diff(revenue - rnd, 4))
def cg_f019_rnd_productivity_core25_2nd_v026_signal(revenue, gp, rnd):
    return _clean(_diff(gp - rnd, 4))
def cg_f019_rnd_productivity_core26_2nd_v027_signal(revenue, gp, rnd):
    return _clean(_diff(_log(revenue.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core27_2nd_v028_signal(revenue, gp, rnd):
    return _clean(_diff(_log(gp.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core28_2nd_v029_signal(revenue, gp, rnd):
    return _clean(_diff(_safe_div(revenue, gp), 4))
def cg_f019_rnd_productivity_core29_2nd_v030_signal(revenue, gp, rnd):
    return _clean(_diff(_safe_div(rnd, gp.abs() + 1.0), 4))
def cg_f019_rnd_productivity_core30_2nd_v031_signal(revenue, gp, rnd):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f019_rnd_productivity_core31_2nd_v032_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core32_2nd_v033_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core33_2nd_v034_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(gp, revenue), 4), 8))
def cg_f019_rnd_productivity_core34_2nd_v035_signal(revenue, gp, rnd):
    return _clean(_z(_slope(revenue - rnd, 4), 8))
def cg_f019_rnd_productivity_core35_2nd_v036_signal(revenue, gp, rnd):
    return _clean(_z(_slope(gp - rnd, 4), 8))
def cg_f019_rnd_productivity_core36_2nd_v037_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_log(revenue.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core37_2nd_v038_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_log(gp.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core38_2nd_v039_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(revenue, gp), 4), 8))
def cg_f019_rnd_productivity_core39_2nd_v040_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core40_2nd_v041_signal(revenue, gp, rnd):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f019_rnd_productivity_core41_2nd_v042_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(revenue, rnd.abs() + 1.0), 8), 12))
def cg_f019_rnd_productivity_core42_2nd_v043_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(gp, rnd.abs() + 1.0), 8), 12))
def cg_f019_rnd_productivity_core43_2nd_v044_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(gp, revenue), 8), 12))
def cg_f019_rnd_productivity_core44_2nd_v045_signal(revenue, gp, rnd):
    return _clean(_z(_slope(revenue - rnd, 8), 12))
def cg_f019_rnd_productivity_core45_2nd_v046_signal(revenue, gp, rnd):
    return _clean(_z(_slope(gp - rnd, 8), 12))
def cg_f019_rnd_productivity_core46_2nd_v047_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_log(revenue.abs() + 1.0), 8), 12))
def cg_f019_rnd_productivity_core47_2nd_v048_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_log(gp.abs() + 1.0), 8), 12))
def cg_f019_rnd_productivity_core48_2nd_v049_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(revenue, gp), 8), 12))
def cg_f019_rnd_productivity_core49_2nd_v050_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_safe_div(rnd, gp.abs() + 1.0), 8), 12))
def cg_f019_rnd_productivity_core50_2nd_v051_signal(revenue, gp, rnd):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f019_rnd_productivity_core51_2nd_v052_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core52_2nd_v053_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core53_2nd_v054_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_safe_div(gp, revenue), 4), 8))
def cg_f019_rnd_productivity_core54_2nd_v055_signal(revenue, gp, rnd):
    return _clean(_z(_diff(revenue - rnd, 4), 8))
def cg_f019_rnd_productivity_core55_2nd_v056_signal(revenue, gp, rnd):
    return _clean(_z(_diff(gp - rnd, 4), 8))
def cg_f019_rnd_productivity_core56_2nd_v057_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_log(revenue.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core57_2nd_v058_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_log(gp.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core58_2nd_v059_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_safe_div(revenue, gp), 4), 8))
def cg_f019_rnd_productivity_core59_2nd_v060_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core60_2nd_v061_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f019_rnd_productivity_core61_2nd_v062_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core62_2nd_v063_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core63_2nd_v064_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_safe_div(gp, revenue), 4), 12))
def cg_f019_rnd_productivity_core64_2nd_v065_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(revenue - rnd, 4), 12))
def cg_f019_rnd_productivity_core65_2nd_v066_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(gp - rnd, 4), 12))
def cg_f019_rnd_productivity_core66_2nd_v067_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_log(revenue.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core67_2nd_v068_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_log(gp.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core68_2nd_v069_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_safe_div(revenue, gp), 4), 12))
def cg_f019_rnd_productivity_core69_2nd_v070_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core70_2nd_v071_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f019_rnd_productivity_core71_2nd_v072_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core72_2nd_v073_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core73_2nd_v074_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_safe_div(gp, revenue), 4), 12))
def cg_f019_rnd_productivity_core74_2nd_v075_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(revenue - rnd, 4), 12))
def cg_f019_rnd_productivity_core75_2nd_v076_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(gp - rnd, 4), 12))
def cg_f019_rnd_productivity_core76_2nd_v077_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_log(revenue.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core77_2nd_v078_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_log(gp.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core78_2nd_v079_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_safe_div(revenue, gp), 4), 12))
def cg_f019_rnd_productivity_core79_2nd_v080_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 12))
def cg_f019_rnd_productivity_core80_2nd_v081_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f019_rnd_productivity_core81_2nd_v082_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core82_2nd_v083_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core83_2nd_v084_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_safe_div(gp, revenue), 4), 4))
def cg_f019_rnd_productivity_core84_2nd_v085_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(revenue - rnd, 4), 4))
def cg_f019_rnd_productivity_core85_2nd_v086_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(gp - rnd, 4), 4))
def cg_f019_rnd_productivity_core86_2nd_v087_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_log(revenue.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core87_2nd_v088_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_log(gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core88_2nd_v089_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_safe_div(revenue, gp), 4), 4))
def cg_f019_rnd_productivity_core89_2nd_v090_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core90_2nd_v091_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f019_rnd_productivity_core91_2nd_v092_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core92_2nd_v093_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core93_2nd_v094_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_safe_div(gp, revenue), 4), 4))
def cg_f019_rnd_productivity_core94_2nd_v095_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(revenue - rnd, 4), 4))
def cg_f019_rnd_productivity_core95_2nd_v096_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(gp - rnd, 4), 4))
def cg_f019_rnd_productivity_core96_2nd_v097_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_log(revenue.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core97_2nd_v098_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_log(gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core98_2nd_v099_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_safe_div(revenue, gp), 4), 4))
def cg_f019_rnd_productivity_core99_2nd_v100_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core100_2nd_v101_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f019_rnd_productivity_core101_2nd_v102_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(revenue, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core102_2nd_v103_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(gp, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core103_2nd_v104_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(gp, revenue), 4), 4))
def cg_f019_rnd_productivity_core104_2nd_v105_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(revenue - rnd, 4), 4))
def cg_f019_rnd_productivity_core105_2nd_v106_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(gp - rnd, 4), 4))
def cg_f019_rnd_productivity_core106_2nd_v107_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_log(revenue.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core107_2nd_v108_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_log(gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core108_2nd_v109_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(revenue, gp), 4), 4))
def cg_f019_rnd_productivity_core109_2nd_v110_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(rnd, gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core110_2nd_v111_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f019_rnd_productivity_core111_2nd_v112_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(revenue, rnd.abs() + 1.0), 8), 8))
def cg_f019_rnd_productivity_core112_2nd_v113_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(gp, rnd.abs() + 1.0), 8), 8))
def cg_f019_rnd_productivity_core113_2nd_v114_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(gp, revenue), 8), 8))
def cg_f019_rnd_productivity_core114_2nd_v115_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(revenue - rnd, 8), 8))
def cg_f019_rnd_productivity_core115_2nd_v116_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(gp - rnd, 8), 8))
def cg_f019_rnd_productivity_core116_2nd_v117_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_log(revenue.abs() + 1.0), 8), 8))
def cg_f019_rnd_productivity_core117_2nd_v118_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_log(gp.abs() + 1.0), 8), 8))
def cg_f019_rnd_productivity_core118_2nd_v119_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(revenue, gp), 8), 8))
def cg_f019_rnd_productivity_core119_2nd_v120_signal(revenue, gp, rnd):
    return _clean(_slope(_mean(_safe_div(rnd, gp.abs() + 1.0), 8), 8))
def cg_f019_rnd_productivity_core120_2nd_v121_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f019_rnd_productivity_core121_2nd_v122_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_safe_div(revenue, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core122_2nd_v123_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_safe_div(gp, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core123_2nd_v124_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_safe_div(gp, revenue), 4), 4))
def cg_f019_rnd_productivity_core124_2nd_v125_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(revenue - rnd, 4), 4))
def cg_f019_rnd_productivity_core125_2nd_v126_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(gp - rnd, 4), 4))
def cg_f019_rnd_productivity_core126_2nd_v127_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_log(revenue.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core127_2nd_v128_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_log(gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core128_2nd_v129_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_safe_div(revenue, gp), 4), 4))
def cg_f019_rnd_productivity_core129_2nd_v130_signal(revenue, gp, rnd):
    return _clean(_diff(_mean(_safe_div(rnd, gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core130_2nd_v131_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core131_2nd_v132_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core132_2nd_v133_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core133_2nd_v134_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_safe_div(gp, revenue), 4), 4), 8))
def cg_f019_rnd_productivity_core134_2nd_v135_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(revenue - rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core135_2nd_v136_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(gp - rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core136_2nd_v137_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_log(revenue.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core137_2nd_v138_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_log(gp.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core138_2nd_v139_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_safe_div(revenue, gp), 4), 4), 8))
def cg_f019_rnd_productivity_core139_2nd_v140_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_mean(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core140_2nd_v141_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core141_2nd_v142_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core142_2nd_v143_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core143_2nd_v144_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(gp, revenue), 4), 4), 12))
def cg_f019_rnd_productivity_core144_2nd_v145_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(revenue - rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core145_2nd_v146_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(gp - rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core146_2nd_v147_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_log(revenue.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core147_2nd_v148_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_log(gp.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core148_2nd_v149_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, gp), 4), 4), 12))
def cg_f019_rnd_productivity_core149_2nd_v150_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 12))