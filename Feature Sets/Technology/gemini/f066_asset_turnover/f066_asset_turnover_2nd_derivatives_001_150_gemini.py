import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f066_asset_turnover_core00_2nd_v001_signal(revenue, assetsavg):
    return _clean(_slope(revenue, 4))
def cg_f066_asset_turnover_core01_2nd_v002_signal(revenue, assetsavg):
    return _clean(_slope(assetsavg, 4))
def cg_f066_asset_turnover_core02_2nd_v003_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, assetsavg), 4))
def cg_f066_asset_turnover_core03_2nd_v004_signal(revenue, assetsavg):
    return _clean(_slope(_diff(revenue, 4), 4))
def cg_f066_asset_turnover_core04_2nd_v005_signal(revenue, assetsavg):
    return _clean(_slope(_pct_change(revenue, 4), 4))
def cg_f066_asset_turnover_core05_2nd_v006_signal(revenue, assetsavg):
    return _clean(_slope(_diff(assetsavg, 4), 4))
def cg_f066_asset_turnover_core06_2nd_v007_signal(revenue, assetsavg):
    return _clean(_slope(_z(_safe_div(revenue, assetsavg), 8), 4))
def cg_f066_asset_turnover_core07_2nd_v008_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(revenue, assetsavg), 4), 4))
def cg_f066_asset_turnover_core08_2nd_v009_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(_diff(revenue, 4), assetsavg), 4))
def cg_f066_asset_turnover_core09_2nd_v010_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4))
def cg_f066_asset_turnover_core10_2nd_v011_signal(revenue, assetsavg):
    return _clean(_slope(revenue, 8))
def cg_f066_asset_turnover_core11_2nd_v012_signal(revenue, assetsavg):
    return _clean(_slope(assetsavg, 8))
def cg_f066_asset_turnover_core12_2nd_v013_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, assetsavg), 8))
def cg_f066_asset_turnover_core13_2nd_v014_signal(revenue, assetsavg):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f066_asset_turnover_core14_2nd_v015_signal(revenue, assetsavg):
    return _clean(_slope(_pct_change(revenue, 4), 8))
def cg_f066_asset_turnover_core15_2nd_v016_signal(revenue, assetsavg):
    return _clean(_slope(_diff(assetsavg, 4), 8))
def cg_f066_asset_turnover_core16_2nd_v017_signal(revenue, assetsavg):
    return _clean(_slope(_z(_safe_div(revenue, assetsavg), 8), 8))
def cg_f066_asset_turnover_core17_2nd_v018_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(revenue, assetsavg), 4), 8))
def cg_f066_asset_turnover_core18_2nd_v019_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(_diff(revenue, 4), assetsavg), 8))
def cg_f066_asset_turnover_core19_2nd_v020_signal(revenue, assetsavg):
    return _clean(_slope(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 8))
def cg_f066_asset_turnover_core20_2nd_v021_signal(revenue, assetsavg):
    return _clean(_diff(revenue, 4))
def cg_f066_asset_turnover_core21_2nd_v022_signal(revenue, assetsavg):
    return _clean(_diff(assetsavg, 4))
def cg_f066_asset_turnover_core22_2nd_v023_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, assetsavg), 4))
def cg_f066_asset_turnover_core23_2nd_v024_signal(revenue, assetsavg):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f066_asset_turnover_core24_2nd_v025_signal(revenue, assetsavg):
    return _clean(_diff(_pct_change(revenue, 4), 4))
def cg_f066_asset_turnover_core25_2nd_v026_signal(revenue, assetsavg):
    return _clean(_diff(_diff(assetsavg, 4), 4))
def cg_f066_asset_turnover_core26_2nd_v027_signal(revenue, assetsavg):
    return _clean(_diff(_z(_safe_div(revenue, assetsavg), 8), 4))
def cg_f066_asset_turnover_core27_2nd_v028_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_safe_div(revenue, assetsavg), 4), 4))
def cg_f066_asset_turnover_core28_2nd_v029_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(_diff(revenue, 4), assetsavg), 4))
def cg_f066_asset_turnover_core29_2nd_v030_signal(revenue, assetsavg):
    return _clean(_diff(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4))
def cg_f066_asset_turnover_core30_2nd_v031_signal(revenue, assetsavg):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f066_asset_turnover_core31_2nd_v032_signal(revenue, assetsavg):
    return _clean(_z(_slope(assetsavg, 4), 8))
def cg_f066_asset_turnover_core32_2nd_v033_signal(revenue, assetsavg):
    return _clean(_z(_slope(_safe_div(revenue, assetsavg), 4), 8))
def cg_f066_asset_turnover_core33_2nd_v034_signal(revenue, assetsavg):
    return _clean(_z(_slope(_diff(revenue, 4), 4), 8))
def cg_f066_asset_turnover_core34_2nd_v035_signal(revenue, assetsavg):
    return _clean(_z(_slope(_pct_change(revenue, 4), 4), 8))
def cg_f066_asset_turnover_core35_2nd_v036_signal(revenue, assetsavg):
    return _clean(_z(_slope(_diff(assetsavg, 4), 4), 8))
def cg_f066_asset_turnover_core36_2nd_v037_signal(revenue, assetsavg):
    return _clean(_z(_slope(_z(_safe_div(revenue, assetsavg), 8), 4), 8))
def cg_f066_asset_turnover_core37_2nd_v038_signal(revenue, assetsavg):
    return _clean(_z(_slope(_mean(_safe_div(revenue, assetsavg), 4), 4), 8))
def cg_f066_asset_turnover_core38_2nd_v039_signal(revenue, assetsavg):
    return _clean(_z(_slope(_safe_div(_diff(revenue, 4), assetsavg), 4), 8))
def cg_f066_asset_turnover_core39_2nd_v040_signal(revenue, assetsavg):
    return _clean(_z(_slope(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 8))
def cg_f066_asset_turnover_core40_2nd_v041_signal(revenue, assetsavg):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f066_asset_turnover_core41_2nd_v042_signal(revenue, assetsavg):
    return _clean(_z(_slope(assetsavg, 8), 12))
def cg_f066_asset_turnover_core42_2nd_v043_signal(revenue, assetsavg):
    return _clean(_z(_slope(_safe_div(revenue, assetsavg), 8), 12))
def cg_f066_asset_turnover_core43_2nd_v044_signal(revenue, assetsavg):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f066_asset_turnover_core44_2nd_v045_signal(revenue, assetsavg):
    return _clean(_z(_slope(_pct_change(revenue, 4), 8), 12))
def cg_f066_asset_turnover_core45_2nd_v046_signal(revenue, assetsavg):
    return _clean(_z(_slope(_diff(assetsavg, 4), 8), 12))
def cg_f066_asset_turnover_core46_2nd_v047_signal(revenue, assetsavg):
    return _clean(_z(_slope(_z(_safe_div(revenue, assetsavg), 8), 8), 12))
def cg_f066_asset_turnover_core47_2nd_v048_signal(revenue, assetsavg):
    return _clean(_z(_slope(_mean(_safe_div(revenue, assetsavg), 4), 8), 12))
def cg_f066_asset_turnover_core48_2nd_v049_signal(revenue, assetsavg):
    return _clean(_z(_slope(_safe_div(_diff(revenue, 4), assetsavg), 8), 12))
def cg_f066_asset_turnover_core49_2nd_v050_signal(revenue, assetsavg):
    return _clean(_z(_slope(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 8), 12))
def cg_f066_asset_turnover_core50_2nd_v051_signal(revenue, assetsavg):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f066_asset_turnover_core51_2nd_v052_signal(revenue, assetsavg):
    return _clean(_z(_diff(assetsavg, 4), 8))
def cg_f066_asset_turnover_core52_2nd_v053_signal(revenue, assetsavg):
    return _clean(_z(_diff(_safe_div(revenue, assetsavg), 4), 8))
def cg_f066_asset_turnover_core53_2nd_v054_signal(revenue, assetsavg):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f066_asset_turnover_core54_2nd_v055_signal(revenue, assetsavg):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f066_asset_turnover_core55_2nd_v056_signal(revenue, assetsavg):
    return _clean(_z(_diff(_diff(assetsavg, 4), 4), 8))
def cg_f066_asset_turnover_core56_2nd_v057_signal(revenue, assetsavg):
    return _clean(_z(_diff(_z(_safe_div(revenue, assetsavg), 8), 4), 8))
def cg_f066_asset_turnover_core57_2nd_v058_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_safe_div(revenue, assetsavg), 4), 4), 8))
def cg_f066_asset_turnover_core58_2nd_v059_signal(revenue, assetsavg):
    return _clean(_z(_diff(_safe_div(_diff(revenue, 4), assetsavg), 4), 8))
def cg_f066_asset_turnover_core59_2nd_v060_signal(revenue, assetsavg):
    return _clean(_z(_diff(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 8))
def cg_f066_asset_turnover_core60_2nd_v061_signal(revenue, assetsavg):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f066_asset_turnover_core61_2nd_v062_signal(revenue, assetsavg):
    return _clean(_rank(_slope(assetsavg, 4), 12))
def cg_f066_asset_turnover_core62_2nd_v063_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_safe_div(revenue, assetsavg), 4), 12))
def cg_f066_asset_turnover_core63_2nd_v064_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_diff(revenue, 4), 4), 12))
def cg_f066_asset_turnover_core64_2nd_v065_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_pct_change(revenue, 4), 4), 12))
def cg_f066_asset_turnover_core65_2nd_v066_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_diff(assetsavg, 4), 4), 12))
def cg_f066_asset_turnover_core66_2nd_v067_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_z(_safe_div(revenue, assetsavg), 8), 4), 12))
def cg_f066_asset_turnover_core67_2nd_v068_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, assetsavg), 4), 4), 12))
def cg_f066_asset_turnover_core68_2nd_v069_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_safe_div(_diff(revenue, 4), assetsavg), 4), 12))
def cg_f066_asset_turnover_core69_2nd_v070_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 12))
def cg_f066_asset_turnover_core70_2nd_v071_signal(revenue, assetsavg):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f066_asset_turnover_core71_2nd_v072_signal(revenue, assetsavg):
    return _clean(_rank(_diff(assetsavg, 4), 12))
def cg_f066_asset_turnover_core72_2nd_v073_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_safe_div(revenue, assetsavg), 4), 12))
def cg_f066_asset_turnover_core73_2nd_v074_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f066_asset_turnover_core74_2nd_v075_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 12))
def cg_f066_asset_turnover_core75_2nd_v076_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_diff(assetsavg, 4), 4), 12))
def cg_f066_asset_turnover_core76_2nd_v077_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_z(_safe_div(revenue, assetsavg), 8), 4), 12))
def cg_f066_asset_turnover_core77_2nd_v078_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_mean(_safe_div(revenue, assetsavg), 4), 4), 12))
def cg_f066_asset_turnover_core78_2nd_v079_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_safe_div(_diff(revenue, 4), assetsavg), 4), 12))
def cg_f066_asset_turnover_core79_2nd_v080_signal(revenue, assetsavg):
    return _clean(_rank(_diff(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 12))
def cg_f066_asset_turnover_core80_2nd_v081_signal(revenue, assetsavg):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f066_asset_turnover_core81_2nd_v082_signal(revenue, assetsavg):
    return _clean(_mean(_slope(assetsavg, 4), 4))
def cg_f066_asset_turnover_core82_2nd_v083_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_safe_div(revenue, assetsavg), 4), 4))
def cg_f066_asset_turnover_core83_2nd_v084_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_diff(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core84_2nd_v085_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_pct_change(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core85_2nd_v086_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_diff(assetsavg, 4), 4), 4))
def cg_f066_asset_turnover_core86_2nd_v087_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_z(_safe_div(revenue, assetsavg), 8), 4), 4))
def cg_f066_asset_turnover_core87_2nd_v088_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_mean(_safe_div(revenue, assetsavg), 4), 4), 4))
def cg_f066_asset_turnover_core88_2nd_v089_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_safe_div(_diff(revenue, 4), assetsavg), 4), 4))
def cg_f066_asset_turnover_core89_2nd_v090_signal(revenue, assetsavg):
    return _clean(_mean(_slope(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 4))
def cg_f066_asset_turnover_core90_2nd_v091_signal(revenue, assetsavg):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f066_asset_turnover_core91_2nd_v092_signal(revenue, assetsavg):
    return _clean(_mean(_diff(assetsavg, 4), 4))
def cg_f066_asset_turnover_core92_2nd_v093_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_safe_div(revenue, assetsavg), 4), 4))
def cg_f066_asset_turnover_core93_2nd_v094_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core94_2nd_v095_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core95_2nd_v096_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_diff(assetsavg, 4), 4), 4))
def cg_f066_asset_turnover_core96_2nd_v097_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_z(_safe_div(revenue, assetsavg), 8), 4), 4))
def cg_f066_asset_turnover_core97_2nd_v098_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_mean(_safe_div(revenue, assetsavg), 4), 4), 4))
def cg_f066_asset_turnover_core98_2nd_v099_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_safe_div(_diff(revenue, 4), assetsavg), 4), 4))
def cg_f066_asset_turnover_core99_2nd_v100_signal(revenue, assetsavg):
    return _clean(_mean(_diff(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 4))
def cg_f066_asset_turnover_core100_2nd_v101_signal(revenue, assetsavg):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f066_asset_turnover_core101_2nd_v102_signal(revenue, assetsavg):
    return _clean(_slope(_mean(assetsavg, 4), 4))
def cg_f066_asset_turnover_core102_2nd_v103_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(revenue, assetsavg), 4), 4))
def cg_f066_asset_turnover_core103_2nd_v104_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_diff(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core104_2nd_v105_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_pct_change(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core105_2nd_v106_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_diff(assetsavg, 4), 4), 4))
def cg_f066_asset_turnover_core106_2nd_v107_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_z(_safe_div(revenue, assetsavg), 8), 4), 4))
def cg_f066_asset_turnover_core107_2nd_v108_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_mean(_safe_div(revenue, assetsavg), 4), 4), 4))
def cg_f066_asset_turnover_core108_2nd_v109_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(_diff(revenue, 4), assetsavg), 4), 4))
def cg_f066_asset_turnover_core109_2nd_v110_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 4))
def cg_f066_asset_turnover_core110_2nd_v111_signal(revenue, assetsavg):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f066_asset_turnover_core111_2nd_v112_signal(revenue, assetsavg):
    return _clean(_slope(_mean(assetsavg, 8), 8))
def cg_f066_asset_turnover_core112_2nd_v113_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(revenue, assetsavg), 8), 8))
def cg_f066_asset_turnover_core113_2nd_v114_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_diff(revenue, 4), 8), 8))
def cg_f066_asset_turnover_core114_2nd_v115_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_pct_change(revenue, 4), 8), 8))
def cg_f066_asset_turnover_core115_2nd_v116_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_diff(assetsavg, 4), 8), 8))
def cg_f066_asset_turnover_core116_2nd_v117_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_z(_safe_div(revenue, assetsavg), 8), 8), 8))
def cg_f066_asset_turnover_core117_2nd_v118_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_mean(_safe_div(revenue, assetsavg), 4), 8), 8))
def cg_f066_asset_turnover_core118_2nd_v119_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(_diff(revenue, 4), assetsavg), 8), 8))
def cg_f066_asset_turnover_core119_2nd_v120_signal(revenue, assetsavg):
    return _clean(_slope(_mean(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 8), 8))
def cg_f066_asset_turnover_core120_2nd_v121_signal(revenue, assetsavg):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f066_asset_turnover_core121_2nd_v122_signal(revenue, assetsavg):
    return _clean(_diff(_mean(assetsavg, 4), 4))
def cg_f066_asset_turnover_core122_2nd_v123_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_safe_div(revenue, assetsavg), 4), 4))
def cg_f066_asset_turnover_core123_2nd_v124_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_diff(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core124_2nd_v125_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_pct_change(revenue, 4), 4), 4))
def cg_f066_asset_turnover_core125_2nd_v126_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_diff(assetsavg, 4), 4), 4))
def cg_f066_asset_turnover_core126_2nd_v127_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_z(_safe_div(revenue, assetsavg), 8), 4), 4))
def cg_f066_asset_turnover_core127_2nd_v128_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_mean(_safe_div(revenue, assetsavg), 4), 4), 4))
def cg_f066_asset_turnover_core128_2nd_v129_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_safe_div(_diff(revenue, 4), assetsavg), 4), 4))
def cg_f066_asset_turnover_core129_2nd_v130_signal(revenue, assetsavg):
    return _clean(_diff(_mean(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 4))
def cg_f066_asset_turnover_core130_2nd_v131_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f066_asset_turnover_core131_2nd_v132_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(assetsavg, 4), 4), 8))
def cg_f066_asset_turnover_core132_2nd_v133_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_safe_div(revenue, assetsavg), 4), 4), 8))
def cg_f066_asset_turnover_core133_2nd_v134_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_diff(revenue, 4), 4), 4), 8))
def cg_f066_asset_turnover_core134_2nd_v135_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_pct_change(revenue, 4), 4), 4), 8))
def cg_f066_asset_turnover_core135_2nd_v136_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_diff(assetsavg, 4), 4), 4), 8))
def cg_f066_asset_turnover_core136_2nd_v137_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_z(_safe_div(revenue, assetsavg), 8), 4), 4), 8))
def cg_f066_asset_turnover_core137_2nd_v138_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_mean(_safe_div(revenue, assetsavg), 4), 4), 4), 8))
def cg_f066_asset_turnover_core138_2nd_v139_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_safe_div(_diff(revenue, 4), assetsavg), 4), 4), 8))
def cg_f066_asset_turnover_core139_2nd_v140_signal(revenue, assetsavg):
    return _clean(_z(_diff(_mean(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 4), 8))
def cg_f066_asset_turnover_core140_2nd_v141_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f066_asset_turnover_core141_2nd_v142_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(assetsavg, 4), 4), 12))
def cg_f066_asset_turnover_core142_2nd_v143_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, assetsavg), 4), 4), 12))
def cg_f066_asset_turnover_core143_2nd_v144_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_diff(revenue, 4), 4), 4), 12))
def cg_f066_asset_turnover_core144_2nd_v145_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_pct_change(revenue, 4), 4), 4), 12))
def cg_f066_asset_turnover_core145_2nd_v146_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_diff(assetsavg, 4), 4), 4), 12))
def cg_f066_asset_turnover_core146_2nd_v147_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_z(_safe_div(revenue, assetsavg), 8), 4), 4), 12))
def cg_f066_asset_turnover_core147_2nd_v148_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_mean(_safe_div(revenue, assetsavg), 4), 4), 4), 12))
def cg_f066_asset_turnover_core148_2nd_v149_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_safe_div(_diff(revenue, 4), assetsavg), 4), 4), 12))
def cg_f066_asset_turnover_core149_2nd_v150_signal(revenue, assetsavg):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, _diff(assetsavg, 4).abs() + 1.0), 4), 4), 12))