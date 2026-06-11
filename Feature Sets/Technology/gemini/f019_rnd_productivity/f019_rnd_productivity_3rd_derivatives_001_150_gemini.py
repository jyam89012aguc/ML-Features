import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f019_rnd_productivity_core00_3rd_v001_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(rnd, 4), 4))
def cg_f019_rnd_productivity_core01_3rd_v002_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core02_3rd_v003_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core03_3rd_v004_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_safe_div(gp, revenue), 4), 4))
def cg_f019_rnd_productivity_core04_3rd_v005_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(revenue - rnd, 4), 4))
def cg_f019_rnd_productivity_core05_3rd_v006_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(gp - rnd, 4), 4))
def cg_f019_rnd_productivity_core06_3rd_v007_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core07_3rd_v008_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_log(gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core08_3rd_v009_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_safe_div(revenue, gp), 4), 4))
def cg_f019_rnd_productivity_core09_3rd_v010_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core10_3rd_v011_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(rnd, 4), 8))
def cg_f019_rnd_productivity_core11_3rd_v012_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core12_3rd_v013_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core13_3rd_v014_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_safe_div(gp, revenue), 4), 8))
def cg_f019_rnd_productivity_core14_3rd_v015_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(revenue - rnd, 4), 8))
def cg_f019_rnd_productivity_core15_3rd_v016_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(gp - rnd, 4), 8))
def cg_f019_rnd_productivity_core16_3rd_v017_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_log(revenue.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core17_3rd_v018_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_log(gp.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core18_3rd_v019_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_safe_div(revenue, gp), 4), 8))
def cg_f019_rnd_productivity_core19_3rd_v020_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 8))
def cg_f019_rnd_productivity_core20_3rd_v021_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(rnd, 4), 4))
def cg_f019_rnd_productivity_core21_3rd_v022_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core22_3rd_v023_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core23_3rd_v024_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_safe_div(gp, revenue), 4), 4))
def cg_f019_rnd_productivity_core24_3rd_v025_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(revenue - rnd, 4), 4))
def cg_f019_rnd_productivity_core25_3rd_v026_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(gp - rnd, 4), 4))
def cg_f019_rnd_productivity_core26_3rd_v027_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_log(revenue.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core27_3rd_v028_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_log(gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core28_3rd_v029_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_safe_div(revenue, gp), 4), 4))
def cg_f019_rnd_productivity_core29_3rd_v030_signal(revenue, gp, rnd):
    return _clean(_diff(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 4))
def cg_f019_rnd_productivity_core30_3rd_v031_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core31_3rd_v032_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core32_3rd_v033_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core33_3rd_v034_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_safe_div(gp, revenue), 4), 4), 8))
def cg_f019_rnd_productivity_core34_3rd_v035_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(revenue - rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core35_3rd_v036_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(gp - rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core36_3rd_v037_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core37_3rd_v038_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_log(gp.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core38_3rd_v039_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_safe_div(revenue, gp), 4), 4), 8))
def cg_f019_rnd_productivity_core39_3rd_v040_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core40_3rd_v041_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(rnd, 4), 8), 12))
def cg_f019_rnd_productivity_core41_3rd_v042_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core42_3rd_v043_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core43_3rd_v044_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_safe_div(gp, revenue), 4), 8), 12))
def cg_f019_rnd_productivity_core44_3rd_v045_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(revenue - rnd, 4), 8), 12))
def cg_f019_rnd_productivity_core45_3rd_v046_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(gp - rnd, 4), 8), 12))
def cg_f019_rnd_productivity_core46_3rd_v047_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_log(revenue.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core47_3rd_v048_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_log(gp.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core48_3rd_v049_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_safe_div(revenue, gp), 4), 8), 12))
def cg_f019_rnd_productivity_core49_3rd_v050_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core50_3rd_v051_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core51_3rd_v052_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core52_3rd_v053_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core53_3rd_v054_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_safe_div(gp, revenue), 4), 4), 8))
def cg_f019_rnd_productivity_core54_3rd_v055_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(revenue - rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core55_3rd_v056_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(gp - rnd, 4), 4), 8))
def cg_f019_rnd_productivity_core56_3rd_v057_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_log(revenue.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core57_3rd_v058_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_log(gp.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core58_3rd_v059_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_safe_div(revenue, gp), 4), 4), 8))
def cg_f019_rnd_productivity_core59_3rd_v060_signal(revenue, gp, rnd):
    return _clean(_z(_diff(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 8))
def cg_f019_rnd_productivity_core60_3rd_v061_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core61_3rd_v062_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core62_3rd_v063_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core63_3rd_v064_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(gp, revenue), 4), 4), 12))
def cg_f019_rnd_productivity_core64_3rd_v065_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(revenue - rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core65_3rd_v066_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(gp - rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core66_3rd_v067_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core67_3rd_v068_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_log(gp.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core68_3rd_v069_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(revenue, gp), 4), 4), 12))
def cg_f019_rnd_productivity_core69_3rd_v070_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core70_3rd_v071_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(rnd, 4), 8), 12))
def cg_f019_rnd_productivity_core71_3rd_v072_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core72_3rd_v073_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core73_3rd_v074_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(gp, revenue), 4), 8), 12))
def cg_f019_rnd_productivity_core74_3rd_v075_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(revenue - rnd, 4), 8), 12))
def cg_f019_rnd_productivity_core75_3rd_v076_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(gp - rnd, 4), 8), 12))
def cg_f019_rnd_productivity_core76_3rd_v077_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_log(revenue.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core77_3rd_v078_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_log(gp.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core78_3rd_v079_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(revenue, gp), 4), 8), 12))
def cg_f019_rnd_productivity_core79_3rd_v080_signal(revenue, gp, rnd):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 8), 12))
def cg_f019_rnd_productivity_core80_3rd_v081_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core81_3rd_v082_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core82_3rd_v083_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core83_3rd_v084_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(gp, revenue), 4), 4), 12))
def cg_f019_rnd_productivity_core84_3rd_v085_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(revenue - rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core85_3rd_v086_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(gp - rnd, 4), 4), 12))
def cg_f019_rnd_productivity_core86_3rd_v087_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_log(revenue.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core87_3rd_v088_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_log(gp.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core88_3rd_v089_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(revenue, gp), 4), 4), 12))
def cg_f019_rnd_productivity_core89_3rd_v090_signal(revenue, gp, rnd):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 12))
def cg_f019_rnd_productivity_core90_3rd_v091_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core91_3rd_v092_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core92_3rd_v093_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core93_3rd_v094_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4))
def cg_f019_rnd_productivity_core94_3rd_v095_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(revenue - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core95_3rd_v096_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(gp - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core96_3rd_v097_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core97_3rd_v098_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_log(gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core98_3rd_v099_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(revenue, gp), 4), 4), 4))
def cg_f019_rnd_productivity_core99_3rd_v100_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core100_3rd_v101_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(rnd, 4), 8), 4))
def cg_f019_rnd_productivity_core101_3rd_v102_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 8), 4))
def cg_f019_rnd_productivity_core102_3rd_v103_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 8), 4))
def cg_f019_rnd_productivity_core103_3rd_v104_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(gp, revenue), 4), 8), 4))
def cg_f019_rnd_productivity_core104_3rd_v105_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(revenue - rnd, 4), 8), 4))
def cg_f019_rnd_productivity_core105_3rd_v106_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(gp - rnd, 4), 8), 4))
def cg_f019_rnd_productivity_core106_3rd_v107_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_log(revenue.abs() + 1.0), 4), 8), 4))
def cg_f019_rnd_productivity_core107_3rd_v108_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_log(gp.abs() + 1.0), 4), 8), 4))
def cg_f019_rnd_productivity_core108_3rd_v109_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(revenue, gp), 4), 8), 4))
def cg_f019_rnd_productivity_core109_3rd_v110_signal(revenue, gp, rnd):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 8), 4))
def cg_f019_rnd_productivity_core110_3rd_v111_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core111_3rd_v112_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core112_3rd_v113_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core113_3rd_v114_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(gp, revenue), 4), 4), 4))
def cg_f019_rnd_productivity_core114_3rd_v115_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(revenue - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core115_3rd_v116_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(gp - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core116_3rd_v117_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_log(revenue.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core117_3rd_v118_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_log(gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core118_3rd_v119_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(revenue, gp), 4), 4), 4))
def cg_f019_rnd_productivity_core119_3rd_v120_signal(revenue, gp, rnd):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core120_3rd_v121_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core121_3rd_v122_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core122_3rd_v123_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core123_3rd_v124_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4))
def cg_f019_rnd_productivity_core124_3rd_v125_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(revenue - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core125_3rd_v126_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(gp - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core126_3rd_v127_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core127_3rd_v128_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_log(gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core128_3rd_v129_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(revenue, gp), 4), 4), 4))
def cg_f019_rnd_productivity_core129_3rd_v130_signal(revenue, gp, rnd):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core130_3rd_v131_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core131_3rd_v132_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core132_3rd_v133_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core133_3rd_v134_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4))
def cg_f019_rnd_productivity_core134_3rd_v135_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(revenue - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core135_3rd_v136_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(gp - rnd, 4), 4), 4))
def cg_f019_rnd_productivity_core136_3rd_v137_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core137_3rd_v138_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_log(gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core138_3rd_v139_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(revenue, gp), 4), 4), 4))
def cg_f019_rnd_productivity_core139_3rd_v140_signal(revenue, gp, rnd):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 4))
def cg_f019_rnd_productivity_core140_3rd_v141_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(rnd, 4), 4), 4), 8))
def cg_f019_rnd_productivity_core141_3rd_v142_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(revenue, rnd.abs() + 1.0), 4), 4), 4), 8))
def cg_f019_rnd_productivity_core142_3rd_v143_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(gp, rnd.abs() + 1.0), 4), 4), 4), 8))
def cg_f019_rnd_productivity_core143_3rd_v144_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4), 8))
def cg_f019_rnd_productivity_core144_3rd_v145_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(revenue - rnd, 4), 4), 4), 8))
def cg_f019_rnd_productivity_core145_3rd_v146_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(gp - rnd, 4), 4), 4), 8))
def cg_f019_rnd_productivity_core146_3rd_v147_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_log(revenue.abs() + 1.0), 4), 4), 4), 8))
def cg_f019_rnd_productivity_core147_3rd_v148_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_log(gp.abs() + 1.0), 4), 4), 4), 8))
def cg_f019_rnd_productivity_core148_3rd_v149_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(revenue, gp), 4), 4), 4), 8))
def cg_f019_rnd_productivity_core149_3rd_v150_signal(revenue, gp, rnd):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, gp.abs() + 1.0), 4), 4), 4), 8))