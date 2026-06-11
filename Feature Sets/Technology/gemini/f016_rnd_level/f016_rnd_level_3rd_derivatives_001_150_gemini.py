import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f016_rnd_level_core00_3rd_v001_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(rnd, 4), 4))
def cg_f016_rnd_level_core01_3rd_v002_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_safe_div(rnd, assets), 4), 4))
def cg_f016_rnd_level_core02_3rd_v003_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_safe_div(rnd, marketcap), 4), 4))
def cg_f016_rnd_level_core03_3rd_v004_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4))
def cg_f016_rnd_level_core04_3rd_v005_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4))
def cg_f016_rnd_level_core05_3rd_v006_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(rnd / (marketcap + 1.0), 4), 4))
def cg_f016_rnd_level_core06_3rd_v007_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_z(rnd, 20), 4), 4))
def cg_f016_rnd_level_core07_3rd_v008_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4))
def cg_f016_rnd_level_core08_3rd_v009_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_rank(rnd, 20), 4), 4))
def cg_f016_rnd_level_core09_3rd_v010_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_log(assets), 4), 4))
def cg_f016_rnd_level_core10_3rd_v011_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(rnd, 4), 8))
def cg_f016_rnd_level_core11_3rd_v012_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_safe_div(rnd, assets), 4), 8))
def cg_f016_rnd_level_core12_3rd_v013_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_safe_div(rnd, marketcap), 4), 8))
def cg_f016_rnd_level_core13_3rd_v014_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8))
def cg_f016_rnd_level_core14_3rd_v015_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_safe_div(rnd, assets + marketcap), 4), 8))
def cg_f016_rnd_level_core15_3rd_v016_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(rnd / (marketcap + 1.0), 4), 8))
def cg_f016_rnd_level_core16_3rd_v017_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_z(rnd, 20), 4), 8))
def cg_f016_rnd_level_core17_3rd_v018_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 8))
def cg_f016_rnd_level_core18_3rd_v019_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_rank(rnd, 20), 4), 8))
def cg_f016_rnd_level_core19_3rd_v020_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_log(assets), 4), 8))
def cg_f016_rnd_level_core20_3rd_v021_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(rnd, 4), 4))
def cg_f016_rnd_level_core21_3rd_v022_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_safe_div(rnd, assets), 4), 4))
def cg_f016_rnd_level_core22_3rd_v023_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_safe_div(rnd, marketcap), 4), 4))
def cg_f016_rnd_level_core23_3rd_v024_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4))
def cg_f016_rnd_level_core24_3rd_v025_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_safe_div(rnd, assets + marketcap), 4), 4))
def cg_f016_rnd_level_core25_3rd_v026_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(rnd / (marketcap + 1.0), 4), 4))
def cg_f016_rnd_level_core26_3rd_v027_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_z(rnd, 20), 4), 4))
def cg_f016_rnd_level_core27_3rd_v028_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 4))
def cg_f016_rnd_level_core28_3rd_v029_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_rank(rnd, 20), 4), 4))
def cg_f016_rnd_level_core29_3rd_v030_signal(rnd, assets, marketcap):
    return _clean(_diff(_slope(_log(assets), 4), 4))
def cg_f016_rnd_level_core30_3rd_v031_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(rnd, 4), 4), 8))
def cg_f016_rnd_level_core31_3rd_v032_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(rnd, assets), 4), 4), 8))
def cg_f016_rnd_level_core32_3rd_v033_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(rnd, marketcap), 4), 4), 8))
def cg_f016_rnd_level_core33_3rd_v034_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f016_rnd_level_core34_3rd_v035_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4), 8))
def cg_f016_rnd_level_core35_3rd_v036_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(rnd / (marketcap + 1.0), 4), 4), 8))
def cg_f016_rnd_level_core36_3rd_v037_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_z(rnd, 20), 4), 4), 8))
def cg_f016_rnd_level_core37_3rd_v038_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 8))
def cg_f016_rnd_level_core38_3rd_v039_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_rank(rnd, 20), 4), 4), 8))
def cg_f016_rnd_level_core39_3rd_v040_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_diff(_log(assets), 4), 4), 8))
def cg_f016_rnd_level_core40_3rd_v041_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(rnd, 4), 8), 12))
def cg_f016_rnd_level_core41_3rd_v042_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(rnd, assets), 4), 8), 12))
def cg_f016_rnd_level_core42_3rd_v043_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(rnd, marketcap), 4), 8), 12))
def cg_f016_rnd_level_core43_3rd_v044_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 12))
def cg_f016_rnd_level_core44_3rd_v045_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(rnd, assets + marketcap), 4), 8), 12))
def cg_f016_rnd_level_core45_3rd_v046_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(rnd / (marketcap + 1.0), 4), 8), 12))
def cg_f016_rnd_level_core46_3rd_v047_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_z(rnd, 20), 4), 8), 12))
def cg_f016_rnd_level_core47_3rd_v048_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 8), 12))
def cg_f016_rnd_level_core48_3rd_v049_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_rank(rnd, 20), 4), 8), 12))
def cg_f016_rnd_level_core49_3rd_v050_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_log(assets), 4), 8), 12))
def cg_f016_rnd_level_core50_3rd_v051_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(rnd, 4), 4), 8))
def cg_f016_rnd_level_core51_3rd_v052_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(rnd, assets), 4), 4), 8))
def cg_f016_rnd_level_core52_3rd_v053_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(rnd, marketcap), 4), 4), 8))
def cg_f016_rnd_level_core53_3rd_v054_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 8))
def cg_f016_rnd_level_core54_3rd_v055_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(rnd, assets + marketcap), 4), 4), 8))
def cg_f016_rnd_level_core55_3rd_v056_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(rnd / (marketcap + 1.0), 4), 4), 8))
def cg_f016_rnd_level_core56_3rd_v057_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_z(rnd, 20), 4), 4), 8))
def cg_f016_rnd_level_core57_3rd_v058_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 8))
def cg_f016_rnd_level_core58_3rd_v059_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_rank(rnd, 20), 4), 4), 8))
def cg_f016_rnd_level_core59_3rd_v060_signal(rnd, assets, marketcap):
    return _clean(_z(_diff(_slope(_log(assets), 4), 4), 8))
def cg_f016_rnd_level_core60_3rd_v061_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(rnd, 4), 4), 12))
def cg_f016_rnd_level_core61_3rd_v062_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, assets), 4), 4), 12))
def cg_f016_rnd_level_core62_3rd_v063_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, marketcap), 4), 4), 12))
def cg_f016_rnd_level_core63_3rd_v064_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f016_rnd_level_core64_3rd_v065_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4), 12))
def cg_f016_rnd_level_core65_3rd_v066_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(rnd / (marketcap + 1.0), 4), 4), 12))
def cg_f016_rnd_level_core66_3rd_v067_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_z(rnd, 20), 4), 4), 12))
def cg_f016_rnd_level_core67_3rd_v068_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 12))
def cg_f016_rnd_level_core68_3rd_v069_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_rank(rnd, 20), 4), 4), 12))
def cg_f016_rnd_level_core69_3rd_v070_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_diff(_log(assets), 4), 4), 12))
def cg_f016_rnd_level_core70_3rd_v071_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(rnd, 4), 8), 12))
def cg_f016_rnd_level_core71_3rd_v072_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, assets), 4), 8), 12))
def cg_f016_rnd_level_core72_3rd_v073_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, marketcap), 4), 8), 12))
def cg_f016_rnd_level_core73_3rd_v074_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 12))
def cg_f016_rnd_level_core74_3rd_v075_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, assets + marketcap), 4), 8), 12))
def cg_f016_rnd_level_core75_3rd_v076_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(rnd / (marketcap + 1.0), 4), 8), 12))
def cg_f016_rnd_level_core76_3rd_v077_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_z(rnd, 20), 4), 8), 12))
def cg_f016_rnd_level_core77_3rd_v078_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 8), 12))
def cg_f016_rnd_level_core78_3rd_v079_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_rank(rnd, 20), 4), 8), 12))
def cg_f016_rnd_level_core79_3rd_v080_signal(rnd, assets, marketcap):
    return _clean(_rank(_slope(_diff(_log(assets), 4), 8), 12))
def cg_f016_rnd_level_core80_3rd_v081_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(rnd, 4), 4), 12))
def cg_f016_rnd_level_core81_3rd_v082_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, assets), 4), 4), 12))
def cg_f016_rnd_level_core82_3rd_v083_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, marketcap), 4), 4), 12))
def cg_f016_rnd_level_core83_3rd_v084_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 12))
def cg_f016_rnd_level_core84_3rd_v085_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, assets + marketcap), 4), 4), 12))
def cg_f016_rnd_level_core85_3rd_v086_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(rnd / (marketcap + 1.0), 4), 4), 12))
def cg_f016_rnd_level_core86_3rd_v087_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_z(rnd, 20), 4), 4), 12))
def cg_f016_rnd_level_core87_3rd_v088_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 12))
def cg_f016_rnd_level_core88_3rd_v089_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_rank(rnd, 20), 4), 4), 12))
def cg_f016_rnd_level_core89_3rd_v090_signal(rnd, assets, marketcap):
    return _clean(_rank(_diff(_slope(_log(assets), 4), 4), 12))
def cg_f016_rnd_level_core90_3rd_v091_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(rnd, 4), 4), 4))
def cg_f016_rnd_level_core91_3rd_v092_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4))
def cg_f016_rnd_level_core92_3rd_v093_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, marketcap), 4), 4), 4))
def cg_f016_rnd_level_core93_3rd_v094_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core94_3rd_v095_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4), 4))
def cg_f016_rnd_level_core95_3rd_v096_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(rnd / (marketcap + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core96_3rd_v097_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_z(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core97_3rd_v098_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 4))
def cg_f016_rnd_level_core98_3rd_v099_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_rank(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core99_3rd_v100_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_diff(_log(assets), 4), 4), 4))
def cg_f016_rnd_level_core100_3rd_v101_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(rnd, 4), 8), 4))
def cg_f016_rnd_level_core101_3rd_v102_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, assets), 4), 8), 4))
def cg_f016_rnd_level_core102_3rd_v103_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, marketcap), 4), 8), 4))
def cg_f016_rnd_level_core103_3rd_v104_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_log(rnd.abs() + 1.0), 4), 8), 4))
def cg_f016_rnd_level_core104_3rd_v105_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, assets + marketcap), 4), 8), 4))
def cg_f016_rnd_level_core105_3rd_v106_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(rnd / (marketcap + 1.0), 4), 8), 4))
def cg_f016_rnd_level_core106_3rd_v107_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_z(rnd, 20), 4), 8), 4))
def cg_f016_rnd_level_core107_3rd_v108_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 8), 4))
def cg_f016_rnd_level_core108_3rd_v109_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_rank(rnd, 20), 4), 8), 4))
def cg_f016_rnd_level_core109_3rd_v110_signal(rnd, assets, marketcap):
    return _clean(_mean(_slope(_diff(_log(assets), 4), 8), 4))
def cg_f016_rnd_level_core110_3rd_v111_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(rnd, 4), 4), 4))
def cg_f016_rnd_level_core111_3rd_v112_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, assets), 4), 4), 4))
def cg_f016_rnd_level_core112_3rd_v113_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, marketcap), 4), 4), 4))
def cg_f016_rnd_level_core113_3rd_v114_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core114_3rd_v115_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, assets + marketcap), 4), 4), 4))
def cg_f016_rnd_level_core115_3rd_v116_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(rnd / (marketcap + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core116_3rd_v117_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_z(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core117_3rd_v118_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 4))
def cg_f016_rnd_level_core118_3rd_v119_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_rank(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core119_3rd_v120_signal(rnd, assets, marketcap):
    return _clean(_mean(_diff(_slope(_log(assets), 4), 4), 4))
def cg_f016_rnd_level_core120_3rd_v121_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(rnd, 4), 4), 4))
def cg_f016_rnd_level_core121_3rd_v122_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4))
def cg_f016_rnd_level_core122_3rd_v123_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, marketcap), 4), 4), 4))
def cg_f016_rnd_level_core123_3rd_v124_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core124_3rd_v125_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4), 4))
def cg_f016_rnd_level_core125_3rd_v126_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(rnd / (marketcap + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core126_3rd_v127_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_z(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core127_3rd_v128_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 4))
def cg_f016_rnd_level_core128_3rd_v129_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_rank(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core129_3rd_v130_signal(rnd, assets, marketcap):
    return _clean(_slope(_diff(_diff(_log(assets), 4), 4), 4))
def cg_f016_rnd_level_core130_3rd_v131_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(rnd, 4), 4), 4))
def cg_f016_rnd_level_core131_3rd_v132_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4))
def cg_f016_rnd_level_core132_3rd_v133_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, marketcap), 4), 4), 4))
def cg_f016_rnd_level_core133_3rd_v134_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core134_3rd_v135_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4), 4))
def cg_f016_rnd_level_core135_3rd_v136_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(rnd / (marketcap + 1.0), 4), 4), 4))
def cg_f016_rnd_level_core136_3rd_v137_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_z(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core137_3rd_v138_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 4))
def cg_f016_rnd_level_core138_3rd_v139_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_rank(rnd, 20), 4), 4), 4))
def cg_f016_rnd_level_core139_3rd_v140_signal(rnd, assets, marketcap):
    return _clean(_diff(_diff(_diff(_log(assets), 4), 4), 4))
def cg_f016_rnd_level_core140_3rd_v141_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(rnd, 4), 4), 4), 8))
def cg_f016_rnd_level_core141_3rd_v142_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, assets), 4), 4), 4), 8))
def cg_f016_rnd_level_core142_3rd_v143_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, marketcap), 4), 4), 4), 8))
def cg_f016_rnd_level_core143_3rd_v144_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_log(rnd.abs() + 1.0), 4), 4), 4), 8))
def cg_f016_rnd_level_core144_3rd_v145_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, assets + marketcap), 4), 4), 4), 8))
def cg_f016_rnd_level_core145_3rd_v146_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(rnd / (marketcap + 1.0), 4), 4), 4), 8))
def cg_f016_rnd_level_core146_3rd_v147_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_z(rnd, 20), 4), 4), 4), 8))
def cg_f016_rnd_level_core147_3rd_v148_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_safe_div(rnd, _mean(rnd, 4)), 4), 4), 4), 8))
def cg_f016_rnd_level_core148_3rd_v149_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_rank(rnd, 20), 4), 4), 4), 8))
def cg_f016_rnd_level_core149_3rd_v150_signal(rnd, assets, marketcap):
    return _clean(_z(_slope(_diff(_diff(_log(assets), 4), 4), 4), 8))