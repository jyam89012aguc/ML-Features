import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f040_asset_base_core00_2nd_v001_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assets, 4))
def cg_f040_asset_base_core01_2nd_v002_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assetsavg, 4))
def cg_f040_asset_base_core02_2nd_v003_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assetsc, 4))
def cg_f040_asset_base_core03_2nd_v004_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_diff(assets, 4), 4))
def cg_f040_asset_base_core04_2nd_v005_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_pct_change(assets, 4), 4))
def cg_f040_asset_base_core05_2nd_v006_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_slope(assets, 8), 4))
def cg_f040_asset_base_core06_2nd_v007_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_z(assets, 12), 4))
def cg_f040_asset_base_core07_2nd_v008_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_safe_div(assets, assetsavg.abs() + 1.0), 4))
def cg_f040_asset_base_core08_2nd_v009_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assets - assetsc, 4))
def cg_f040_asset_base_core09_2nd_v010_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f040_asset_base_core10_2nd_v011_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assets, 8))
def cg_f040_asset_base_core11_2nd_v012_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assetsavg, 8))
def cg_f040_asset_base_core12_2nd_v013_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assetsc, 8))
def cg_f040_asset_base_core13_2nd_v014_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_diff(assets, 4), 8))
def cg_f040_asset_base_core14_2nd_v015_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_pct_change(assets, 4), 8))
def cg_f040_asset_base_core15_2nd_v016_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_slope(assets, 8), 8))
def cg_f040_asset_base_core16_2nd_v017_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_z(assets, 12), 8))
def cg_f040_asset_base_core17_2nd_v018_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_safe_div(assets, assetsavg.abs() + 1.0), 8))
def cg_f040_asset_base_core18_2nd_v019_signal(assets, assetsavg, assetsc):
    return _clean(_slope(assets - assetsc, 8))
def cg_f040_asset_base_core19_2nd_v020_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assets, 4), 8))
def cg_f040_asset_base_core20_2nd_v021_signal(assets, assetsavg, assetsc):
    return _clean(_diff(assets, 4))
def cg_f040_asset_base_core21_2nd_v022_signal(assets, assetsavg, assetsc):
    return _clean(_diff(assetsavg, 4))
def cg_f040_asset_base_core22_2nd_v023_signal(assets, assetsavg, assetsc):
    return _clean(_diff(assetsc, 4))
def cg_f040_asset_base_core23_2nd_v024_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_diff(assets, 4), 4))
def cg_f040_asset_base_core24_2nd_v025_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_pct_change(assets, 4), 4))
def cg_f040_asset_base_core25_2nd_v026_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_slope(assets, 8), 4))
def cg_f040_asset_base_core26_2nd_v027_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_z(assets, 12), 4))
def cg_f040_asset_base_core27_2nd_v028_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_safe_div(assets, assetsavg.abs() + 1.0), 4))
def cg_f040_asset_base_core28_2nd_v029_signal(assets, assetsavg, assetsc):
    return _clean(_diff(assets - assetsc, 4))
def cg_f040_asset_base_core29_2nd_v030_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f040_asset_base_core30_2nd_v031_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assets, 4), 8))
def cg_f040_asset_base_core31_2nd_v032_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assetsavg, 4), 8))
def cg_f040_asset_base_core32_2nd_v033_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assetsc, 4), 8))
def cg_f040_asset_base_core33_2nd_v034_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_diff(assets, 4), 4), 8))
def cg_f040_asset_base_core34_2nd_v035_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_pct_change(assets, 4), 4), 8))
def cg_f040_asset_base_core35_2nd_v036_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_slope(assets, 8), 4), 8))
def cg_f040_asset_base_core36_2nd_v037_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_z(assets, 12), 4), 8))
def cg_f040_asset_base_core37_2nd_v038_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_safe_div(assets, assetsavg.abs() + 1.0), 4), 8))
def cg_f040_asset_base_core38_2nd_v039_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assets - assetsc, 4), 8))
def cg_f040_asset_base_core39_2nd_v040_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_mean(assets, 4), 4), 8))
def cg_f040_asset_base_core40_2nd_v041_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assets, 8), 12))
def cg_f040_asset_base_core41_2nd_v042_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assetsavg, 8), 12))
def cg_f040_asset_base_core42_2nd_v043_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assetsc, 8), 12))
def cg_f040_asset_base_core43_2nd_v044_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_diff(assets, 4), 8), 12))
def cg_f040_asset_base_core44_2nd_v045_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_pct_change(assets, 4), 8), 12))
def cg_f040_asset_base_core45_2nd_v046_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_slope(assets, 8), 8), 12))
def cg_f040_asset_base_core46_2nd_v047_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_z(assets, 12), 8), 12))
def cg_f040_asset_base_core47_2nd_v048_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_safe_div(assets, assetsavg.abs() + 1.0), 8), 12))
def cg_f040_asset_base_core48_2nd_v049_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(assets - assetsc, 8), 12))
def cg_f040_asset_base_core49_2nd_v050_signal(assets, assetsavg, assetsc):
    return _clean(_z(_slope(_mean(assets, 4), 8), 12))
def cg_f040_asset_base_core50_2nd_v051_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(assets, 4), 8))
def cg_f040_asset_base_core51_2nd_v052_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(assetsavg, 4), 8))
def cg_f040_asset_base_core52_2nd_v053_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(assetsc, 4), 8))
def cg_f040_asset_base_core53_2nd_v054_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_diff(assets, 4), 4), 8))
def cg_f040_asset_base_core54_2nd_v055_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_pct_change(assets, 4), 4), 8))
def cg_f040_asset_base_core55_2nd_v056_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_slope(assets, 8), 4), 8))
def cg_f040_asset_base_core56_2nd_v057_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_z(assets, 12), 4), 8))
def cg_f040_asset_base_core57_2nd_v058_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_safe_div(assets, assetsavg.abs() + 1.0), 4), 8))
def cg_f040_asset_base_core58_2nd_v059_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(assets - assetsc, 4), 8))
def cg_f040_asset_base_core59_2nd_v060_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f040_asset_base_core60_2nd_v061_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(assets, 4), 12))
def cg_f040_asset_base_core61_2nd_v062_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(assetsavg, 4), 12))
def cg_f040_asset_base_core62_2nd_v063_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(assetsc, 4), 12))
def cg_f040_asset_base_core63_2nd_v064_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_diff(assets, 4), 4), 12))
def cg_f040_asset_base_core64_2nd_v065_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_pct_change(assets, 4), 4), 12))
def cg_f040_asset_base_core65_2nd_v066_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_slope(assets, 8), 4), 12))
def cg_f040_asset_base_core66_2nd_v067_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_z(assets, 12), 4), 12))
def cg_f040_asset_base_core67_2nd_v068_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_safe_div(assets, assetsavg.abs() + 1.0), 4), 12))
def cg_f040_asset_base_core68_2nd_v069_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(assets - assetsc, 4), 12))
def cg_f040_asset_base_core69_2nd_v070_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f040_asset_base_core70_2nd_v071_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(assets, 4), 12))
def cg_f040_asset_base_core71_2nd_v072_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(assetsavg, 4), 12))
def cg_f040_asset_base_core72_2nd_v073_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(assetsc, 4), 12))
def cg_f040_asset_base_core73_2nd_v074_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(_diff(assets, 4), 4), 12))
def cg_f040_asset_base_core74_2nd_v075_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(_pct_change(assets, 4), 4), 12))
def cg_f040_asset_base_core75_2nd_v076_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(_slope(assets, 8), 4), 12))
def cg_f040_asset_base_core76_2nd_v077_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(_z(assets, 12), 4), 12))
def cg_f040_asset_base_core77_2nd_v078_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(_safe_div(assets, assetsavg.abs() + 1.0), 4), 12))
def cg_f040_asset_base_core78_2nd_v079_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(assets - assetsc, 4), 12))
def cg_f040_asset_base_core79_2nd_v080_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_diff(_mean(assets, 4), 4), 12))
def cg_f040_asset_base_core80_2nd_v081_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(assets, 4), 4))
def cg_f040_asset_base_core81_2nd_v082_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(assetsavg, 4), 4))
def cg_f040_asset_base_core82_2nd_v083_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(assetsc, 4), 4))
def cg_f040_asset_base_core83_2nd_v084_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(_diff(assets, 4), 4), 4))
def cg_f040_asset_base_core84_2nd_v085_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(_pct_change(assets, 4), 4), 4))
def cg_f040_asset_base_core85_2nd_v086_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(_slope(assets, 8), 4), 4))
def cg_f040_asset_base_core86_2nd_v087_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(_z(assets, 12), 4), 4))
def cg_f040_asset_base_core87_2nd_v088_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(_safe_div(assets, assetsavg.abs() + 1.0), 4), 4))
def cg_f040_asset_base_core88_2nd_v089_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(assets - assetsc, 4), 4))
def cg_f040_asset_base_core89_2nd_v090_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_slope(_mean(assets, 4), 4), 4))
def cg_f040_asset_base_core90_2nd_v091_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(assets, 4), 4))
def cg_f040_asset_base_core91_2nd_v092_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(assetsavg, 4), 4))
def cg_f040_asset_base_core92_2nd_v093_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(assetsc, 4), 4))
def cg_f040_asset_base_core93_2nd_v094_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(_diff(assets, 4), 4), 4))
def cg_f040_asset_base_core94_2nd_v095_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(_pct_change(assets, 4), 4), 4))
def cg_f040_asset_base_core95_2nd_v096_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(_slope(assets, 8), 4), 4))
def cg_f040_asset_base_core96_2nd_v097_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(_z(assets, 12), 4), 4))
def cg_f040_asset_base_core97_2nd_v098_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(_safe_div(assets, assetsavg.abs() + 1.0), 4), 4))
def cg_f040_asset_base_core98_2nd_v099_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(assets - assetsc, 4), 4))
def cg_f040_asset_base_core99_2nd_v100_signal(assets, assetsavg, assetsc):
    return _clean(_mean(_diff(_mean(assets, 4), 4), 4))
def cg_f040_asset_base_core100_2nd_v101_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f040_asset_base_core101_2nd_v102_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assetsavg, 4), 4))
def cg_f040_asset_base_core102_2nd_v103_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assetsc, 4), 4))
def cg_f040_asset_base_core103_2nd_v104_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_diff(assets, 4), 4), 4))
def cg_f040_asset_base_core104_2nd_v105_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_pct_change(assets, 4), 4), 4))
def cg_f040_asset_base_core105_2nd_v106_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_slope(assets, 8), 4), 4))
def cg_f040_asset_base_core106_2nd_v107_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_z(assets, 12), 4), 4))
def cg_f040_asset_base_core107_2nd_v108_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_safe_div(assets, assetsavg.abs() + 1.0), 4), 4))
def cg_f040_asset_base_core108_2nd_v109_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assets - assetsc, 4), 4))
def cg_f040_asset_base_core109_2nd_v110_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_mean(assets, 4), 4), 4))
def cg_f040_asset_base_core110_2nd_v111_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assets, 8), 8))
def cg_f040_asset_base_core111_2nd_v112_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assetsavg, 8), 8))
def cg_f040_asset_base_core112_2nd_v113_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assetsc, 8), 8))
def cg_f040_asset_base_core113_2nd_v114_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_diff(assets, 4), 8), 8))
def cg_f040_asset_base_core114_2nd_v115_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_pct_change(assets, 4), 8), 8))
def cg_f040_asset_base_core115_2nd_v116_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_slope(assets, 8), 8), 8))
def cg_f040_asset_base_core116_2nd_v117_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_z(assets, 12), 8), 8))
def cg_f040_asset_base_core117_2nd_v118_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_safe_div(assets, assetsavg.abs() + 1.0), 8), 8))
def cg_f040_asset_base_core118_2nd_v119_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(assets - assetsc, 8), 8))
def cg_f040_asset_base_core119_2nd_v120_signal(assets, assetsavg, assetsc):
    return _clean(_slope(_mean(_mean(assets, 4), 8), 8))
def cg_f040_asset_base_core120_2nd_v121_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f040_asset_base_core121_2nd_v122_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(assetsavg, 4), 4))
def cg_f040_asset_base_core122_2nd_v123_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(assetsc, 4), 4))
def cg_f040_asset_base_core123_2nd_v124_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(_diff(assets, 4), 4), 4))
def cg_f040_asset_base_core124_2nd_v125_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(_pct_change(assets, 4), 4), 4))
def cg_f040_asset_base_core125_2nd_v126_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(_slope(assets, 8), 4), 4))
def cg_f040_asset_base_core126_2nd_v127_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(_z(assets, 12), 4), 4))
def cg_f040_asset_base_core127_2nd_v128_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(_safe_div(assets, assetsavg.abs() + 1.0), 4), 4))
def cg_f040_asset_base_core128_2nd_v129_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(assets - assetsc, 4), 4))
def cg_f040_asset_base_core129_2nd_v130_signal(assets, assetsavg, assetsc):
    return _clean(_diff(_mean(_mean(assets, 4), 4), 4))
def cg_f040_asset_base_core130_2nd_v131_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f040_asset_base_core131_2nd_v132_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(assetsavg, 4), 4), 8))
def cg_f040_asset_base_core132_2nd_v133_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(assetsc, 4), 4), 8))
def cg_f040_asset_base_core133_2nd_v134_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(_diff(assets, 4), 4), 4), 8))
def cg_f040_asset_base_core134_2nd_v135_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(_pct_change(assets, 4), 4), 4), 8))
def cg_f040_asset_base_core135_2nd_v136_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(_slope(assets, 8), 4), 4), 8))
def cg_f040_asset_base_core136_2nd_v137_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(_z(assets, 12), 4), 4), 8))
def cg_f040_asset_base_core137_2nd_v138_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(_safe_div(assets, assetsavg.abs() + 1.0), 4), 4), 8))
def cg_f040_asset_base_core138_2nd_v139_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(assets - assetsc, 4), 4), 8))
def cg_f040_asset_base_core139_2nd_v140_signal(assets, assetsavg, assetsc):
    return _clean(_z(_diff(_mean(_mean(assets, 4), 4), 4), 8))
def cg_f040_asset_base_core140_2nd_v141_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f040_asset_base_core141_2nd_v142_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(assetsavg, 4), 4), 12))
def cg_f040_asset_base_core142_2nd_v143_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(assetsc, 4), 4), 12))
def cg_f040_asset_base_core143_2nd_v144_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(_diff(assets, 4), 4), 4), 12))
def cg_f040_asset_base_core144_2nd_v145_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(_pct_change(assets, 4), 4), 4), 12))
def cg_f040_asset_base_core145_2nd_v146_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(_slope(assets, 8), 4), 4), 12))
def cg_f040_asset_base_core146_2nd_v147_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(_z(assets, 12), 4), 4), 12))
def cg_f040_asset_base_core147_2nd_v148_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(_safe_div(assets, assetsavg.abs() + 1.0), 4), 4), 12))
def cg_f040_asset_base_core148_2nd_v149_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(assets - assetsc, 4), 4), 12))
def cg_f040_asset_base_core149_2nd_v150_signal(assets, assetsavg, assetsc):
    return _clean(_rank(_slope(_mean(_mean(assets, 4), 4), 4), 12))