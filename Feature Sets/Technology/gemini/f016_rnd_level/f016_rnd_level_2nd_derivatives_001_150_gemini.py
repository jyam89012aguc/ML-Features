import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f016_rnd_level_core00_2nd_v001_signal(rnd, assets, marketcap):
    return _clean(_slope(rnd, 4))
def cg_f016_rnd_level_core01_2nd_v002_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, assets), 4))
def cg_f016_rnd_level_core02_2nd_v003_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, marketcap), 4))
def cg_f016_rnd_level_core03_2nd_v004_signal(rnd, assets, marketcap):
    return _clean(_slope(_log(rnd.abs() + 1.0), 4))
def cg_f016_rnd_level_core04_2nd_v005_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, assets + marketcap), 4))
def cg_f016_rnd_level_core05_2nd_v006_signal(rnd, assets, marketcap):
    return _clean(_slope(rnd / (marketcap + 1.0), 4))
def cg_f016_rnd_level_core06_2nd_v007_signal(rnd, assets, marketcap):
    return _clean(_slope(_z(rnd, 20), 4))
def cg_f016_rnd_level_core07_2nd_v008_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, _mean(rnd, 4)), 4))
def cg_f016_rnd_level_core08_2nd_v009_signal(rnd, assets, marketcap):
    return _clean(_slope(_rank(rnd, 20), 4))
def cg_f016_rnd_level_core09_2nd_v010_signal(rnd, assets, marketcap):
    return _clean(_slope(_log(assets), 4))
def cg_f016_rnd_level_core10_2nd_v011_signal(rnd, assets, marketcap):
    return _clean(_slope(rnd, 8))
def cg_f016_rnd_level_core11_2nd_v012_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, assets), 8))
def cg_f016_rnd_level_core12_2nd_v013_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, marketcap), 8))
def cg_f016_rnd_level_core13_2nd_v014_signal(rnd, assets, marketcap):
    return _clean(_slope(_log(rnd.abs() + 1.0), 8))
def cg_f016_rnd_level_core14_2nd_v015_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, assets + marketcap), 8))
def cg_f016_rnd_level_core15_2nd_v016_signal(rnd, assets, marketcap):
    return _clean(_slope(rnd / (marketcap + 1.0), 8))
def cg_f016_rnd_level_core16_2nd_v017_signal(rnd, assets, marketcap):
    return _clean(_slope(_z(rnd, 20), 8))
def cg_f016_rnd_level_core17_2nd_v018_signal(rnd, assets, marketcap):
    return _clean(_slope(_safe_div(rnd, _mean(rnd, 4)), 8))
def cg_f016_rnd_level_core18_2nd_v019_signal(rnd, assets, marketcap):
    return _clean(_slope(_rank(rnd, 20), 8))
def cg_f016_rnd_level_core19_2nd_v020_signal(rnd, assets, marketcap):
    return _clean(_slope(_log(assets), 8))
def cg_f016_rnd_level_core20_2nd_v021_signal(rnd, assets, marketcap):
    return _clean(_diff(rnd, 4))
def cg_f016_rnd_level_core21_2nd_v022_signal(rnd, assets, marketcap):
    return _clean(_diff(_safe_div(rnd, assets), 4))
def cg_f016_rnd_level_core22_2nd_v023_signal(rnd, assets, marketcap):
    return _clean(_diff(_safe_div(rnd, marketcap), 4))
def cg_f016_rnd_level_core23_2nd_v024_signal(rnd, assets, marketcap):
    return _clean(_diff(_log(rnd.abs() + 1.0), 4))
def cg_f016_rnd_level_core24_2nd_v025_signal(rnd, assets, marketcap):
    return _clean(_diff(_safe_div(rnd, assets + marketcap), 4))
def cg_f016_rnd_level_core25_2nd_v026_signal(rnd, assets, marketcap):
    return _clean(_diff(rnd / (marketcap + 1.0), 4))
def cg_f016_rnd_level_core26_2nd_v027_signal(rnd, assets, marketcap):
    return _clean(_diff(_z(rnd, 20), 4))
def cg_f016_rnd_level_core27_2nd_v028_signal(rnd, assets, marketcap):
    return _clean(_diff(_safe_div(rnd, _mean(rnd, 4)), 4))
def cg_f016_rnd_level_core28_2nd_v029_signal(rnd, assets, marketcap):
    return _clean(_diff(_rank(rnd, 20), 4))
def cg_f016_rnd_level_core29_2nd_v030_signal(rnd, assets, marketcap):
    return _clean(_diff(_log(assets), 4))
def cg_f016_rnd_level_core30_2nd_v031_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f016_rnd_level_core31_2nd_v032_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, assets), 4), 8))
def cg_f016_rnd_level_core32_2nd_v033_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, marketcap), 4), 8))
def cg_f016_rnd_level_core33_2nd_v034_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_log(rnd.abs() + 1.0), 4), 8))
def cg_f016_rnd_level_core34_2nd_v035_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, assets + marketcap), 4), 8))
def cg_f016_rnd_level_core35_2nd_v036_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(rnd / (marketcap + 1.0), 4), 8))
def cg_f016_rnd_level_core36_2nd_v037_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_z(rnd, 20), 4), 8))
def cg_f016_rnd_level_core37_2nd_v038_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 8))
def cg_f016_rnd_level_core38_2nd_v039_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_rank(rnd, 20), 4), 8))
def cg_f016_rnd_level_core39_2nd_v040_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_log(assets), 4), 8))
def cg_f016_rnd_level_core40_2nd_v041_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f016_rnd_level_core41_2nd_v042_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, assets), 8), 12))
def cg_f016_rnd_level_core42_2nd_v043_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, marketcap), 8), 12))
def cg_f016_rnd_level_core43_2nd_v044_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_log(rnd.abs() + 1.0), 8), 12))
def cg_f016_rnd_level_core44_2nd_v045_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, assets + marketcap), 8), 12))
def cg_f016_rnd_level_core45_2nd_v046_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(rnd / (marketcap + 1.0), 8), 12))
def cg_f016_rnd_level_core46_2nd_v047_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_z(rnd, 20), 8), 12))
def cg_f016_rnd_level_core47_2nd_v048_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_safe_div(rnd, _mean(rnd, 4)), 8), 12))
def cg_f016_rnd_level_core48_2nd_v049_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_rank(rnd, 20), 8), 12))
def cg_f016_rnd_level_core49_2nd_v050_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_log(assets), 8), 12))
def cg_f016_rnd_level_core50_2nd_v051_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f016_rnd_level_core51_2nd_v052_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_safe_div(rnd, assets), 4), 8))
def cg_f016_rnd_level_core52_2nd_v053_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_safe_div(rnd, marketcap), 4), 8))
def cg_f016_rnd_level_core53_2nd_v054_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_log(rnd.abs() + 1.0), 4), 8))
def cg_f016_rnd_level_core54_2nd_v055_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_safe_div(rnd, assets + marketcap), 4), 8))
def cg_f016_rnd_level_core55_2nd_v056_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(rnd / (marketcap + 1.0), 4), 8))
def cg_f016_rnd_level_core56_2nd_v057_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_z(rnd, 20), 4), 8))
def cg_f016_rnd_level_core57_2nd_v058_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 8))
def cg_f016_rnd_level_core58_2nd_v059_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_rank(rnd, 20), 4), 8))
def cg_f016_rnd_level_core59_2nd_v060_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_log(assets), 4), 8))
def cg_f016_rnd_level_core60_2nd_v061_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f016_rnd_level_core61_2nd_v062_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_safe_div(rnd, assets), 4), 12))
def cg_f016_rnd_level_core62_2nd_v063_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_safe_div(rnd, marketcap), 4), 12))
def cg_f016_rnd_level_core63_2nd_v064_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_log(rnd.abs() + 1.0), 4), 12))
def cg_f016_rnd_level_core64_2nd_v065_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_safe_div(rnd, assets + marketcap), 4), 12))
def cg_f016_rnd_level_core65_2nd_v066_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(rnd / (marketcap + 1.0), 4), 12))
def cg_f016_rnd_level_core66_2nd_v067_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_z(rnd, 20), 4), 12))
def cg_f016_rnd_level_core67_2nd_v068_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 12))
def cg_f016_rnd_level_core68_2nd_v069_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_rank(rnd, 20), 4), 12))
def cg_f016_rnd_level_core69_2nd_v070_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_log(assets), 4), 12))
def cg_f016_rnd_level_core70_2nd_v071_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f016_rnd_level_core71_2nd_v072_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_safe_div(rnd, assets), 4), 12))
def cg_f016_rnd_level_core72_2nd_v073_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_safe_div(rnd, marketcap), 4), 12))
def cg_f016_rnd_level_core73_2nd_v074_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_log(rnd.abs() + 1.0), 4), 12))
def cg_f016_rnd_level_core74_2nd_v075_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_safe_div(rnd, assets + marketcap), 4), 12))
def cg_f016_rnd_level_core75_2nd_v076_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(rnd / (marketcap + 1.0), 4), 12))
def cg_f016_rnd_level_core76_2nd_v077_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_z(rnd, 20), 4), 12))
def cg_f016_rnd_level_core77_2nd_v078_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 12))
def cg_f016_rnd_level_core78_2nd_v079_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_rank(rnd, 20), 4), 12))
def cg_f016_rnd_level_core79_2nd_v080_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_log(assets), 4), 12))
def cg_f016_rnd_level_core80_2nd_v081_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f016_rnd_level_core81_2nd_v082_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_safe_div(rnd, assets), 4), 4))
def cg_f016_rnd_level_core82_2nd_v083_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_safe_div(rnd, marketcap), 4), 4))
def cg_f016_rnd_level_core83_2nd_v084_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_log(rnd.abs() + 1.0), 4), 4))
def cg_f016_rnd_level_core84_2nd_v085_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_safe_div(rnd, assets + marketcap), 4), 4))
def cg_f016_rnd_level_core85_2nd_v086_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(rnd / (marketcap + 1.0), 4), 4))
def cg_f016_rnd_level_core86_2nd_v087_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_z(rnd, 20), 4), 4))
def cg_f016_rnd_level_core87_2nd_v088_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 4))
def cg_f016_rnd_level_core88_2nd_v089_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_rank(rnd, 20), 4), 4))
def cg_f016_rnd_level_core89_2nd_v090_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_log(assets), 4), 4))
def cg_f016_rnd_level_core90_2nd_v091_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f016_rnd_level_core91_2nd_v092_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_safe_div(rnd, assets), 4), 4))
def cg_f016_rnd_level_core92_2nd_v093_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_safe_div(rnd, marketcap), 4), 4))
def cg_f016_rnd_level_core93_2nd_v094_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_log(rnd.abs() + 1.0), 4), 4))
def cg_f016_rnd_level_core94_2nd_v095_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_safe_div(rnd, assets + marketcap), 4), 4))
def cg_f016_rnd_level_core95_2nd_v096_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(rnd / (marketcap + 1.0), 4), 4))
def cg_f016_rnd_level_core96_2nd_v097_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_z(rnd, 20), 4), 4))
def cg_f016_rnd_level_core97_2nd_v098_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4))
def cg_f016_rnd_level_core98_2nd_v099_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_rank(rnd, 20), 4), 4))
def cg_f016_rnd_level_core99_2nd_v100_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_log(assets), 4), 4))
def cg_f016_rnd_level_core100_2nd_v101_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f016_rnd_level_core101_2nd_v102_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, assets), 4), 4))
def cg_f016_rnd_level_core102_2nd_v103_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, marketcap), 4), 4))
def cg_f016_rnd_level_core103_2nd_v104_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_log(rnd.abs() + 1.0), 4), 4))
def cg_f016_rnd_level_core104_2nd_v105_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, assets + marketcap), 4), 4))
def cg_f016_rnd_level_core105_2nd_v106_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(rnd / (marketcap + 1.0), 4), 4))
def cg_f016_rnd_level_core106_2nd_v107_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_z(rnd, 20), 4), 4))
def cg_f016_rnd_level_core107_2nd_v108_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, _mean(rnd, 4)), 4), 4))
def cg_f016_rnd_level_core108_2nd_v109_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_rank(rnd, 20), 4), 4))
def cg_f016_rnd_level_core109_2nd_v110_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_log(assets), 4), 4))
def cg_f016_rnd_level_core110_2nd_v111_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f016_rnd_level_core111_2nd_v112_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, assets), 8), 8))
def cg_f016_rnd_level_core112_2nd_v113_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, marketcap), 8), 8))
def cg_f016_rnd_level_core113_2nd_v114_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_log(rnd.abs() + 1.0), 8), 8))
def cg_f016_rnd_level_core114_2nd_v115_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, assets + marketcap), 8), 8))
def cg_f016_rnd_level_core115_2nd_v116_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(rnd / (marketcap + 1.0), 8), 8))
def cg_f016_rnd_level_core116_2nd_v117_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_z(rnd, 20), 8), 8))
def cg_f016_rnd_level_core117_2nd_v118_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_safe_div(rnd, _mean(rnd, 4)), 8), 8))
def cg_f016_rnd_level_core118_2nd_v119_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_rank(rnd, 20), 8), 8))
def cg_f016_rnd_level_core119_2nd_v120_signal(rnd, assets, marketcap):
    return _clean(_slope(_mean(_log(assets), 8), 8))
def cg_f016_rnd_level_core120_2nd_v121_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f016_rnd_level_core121_2nd_v122_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_safe_div(rnd, assets), 4), 4))
def cg_f016_rnd_level_core122_2nd_v123_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_safe_div(rnd, marketcap), 4), 4))
def cg_f016_rnd_level_core123_2nd_v124_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_log(rnd.abs() + 1.0), 4), 4))
def cg_f016_rnd_level_core124_2nd_v125_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_safe_div(rnd, assets + marketcap), 4), 4))
def cg_f016_rnd_level_core125_2nd_v126_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(rnd / (marketcap + 1.0), 4), 4))
def cg_f016_rnd_level_core126_2nd_v127_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_z(rnd, 20), 4), 4))
def cg_f016_rnd_level_core127_2nd_v128_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_safe_div(rnd, _mean(rnd, 4)), 4), 4))
def cg_f016_rnd_level_core128_2nd_v129_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_rank(rnd, 20), 4), 4))
def cg_f016_rnd_level_core129_2nd_v130_signal(rnd, assets, marketcap):
    return _clean(_diff(_mean(_log(assets), 4), 4))
def cg_f016_rnd_level_core130_2nd_v131_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f016_rnd_level_core131_2nd_v132_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(rnd, assets), 4), 4), 8))
def cg_f016_rnd_level_core132_2nd_v133_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(rnd, marketcap), 4), 4), 8))
def cg_f016_rnd_level_core133_2nd_v134_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f016_rnd_level_core134_2nd_v135_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(rnd, assets + marketcap), 4), 4), 8))
def cg_f016_rnd_level_core135_2nd_v136_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(rnd / (marketcap + 1.0), 4), 4), 8))
def cg_f016_rnd_level_core136_2nd_v137_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_z(rnd, 20), 4), 4), 8))
def cg_f016_rnd_level_core137_2nd_v138_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 8))
def cg_f016_rnd_level_core138_2nd_v139_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_rank(rnd, 20), 4), 4), 8))
def cg_f016_rnd_level_core139_2nd_v140_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_mean(_log(assets), 4), 4), 8))
def cg_f016_rnd_level_core140_2nd_v141_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f016_rnd_level_core141_2nd_v142_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, assets), 4), 4), 12))
def cg_f016_rnd_level_core142_2nd_v143_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, marketcap), 4), 4), 12))
def cg_f016_rnd_level_core143_2nd_v144_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f016_rnd_level_core144_2nd_v145_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, assets + marketcap), 4), 4), 12))
def cg_f016_rnd_level_core145_2nd_v146_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(rnd / (marketcap + 1.0), 4), 4), 12))
def cg_f016_rnd_level_core146_2nd_v147_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_z(rnd, 20), 4), 4), 12))
def cg_f016_rnd_level_core147_2nd_v148_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 12))
def cg_f016_rnd_level_core148_2nd_v149_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_rank(rnd, 20), 4), 4), 12))
def cg_f016_rnd_level_core149_2nd_v150_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_mean(_log(assets), 4), 4), 12))