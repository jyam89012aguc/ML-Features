import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f030_asset_liability_gap_core00_2nd_v001_signal(assets, liabilities, equity):
    return _clean(_slope(assets - liabilities, 4))
def cg_f030_asset_liability_gap_core01_2nd_v002_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(assets, liabilities.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core02_2nd_v003_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(equity, assets.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core03_2nd_v004_signal(assets, liabilities, equity):
    return _clean(_slope(assets - liabilities - equity, 4))
def cg_f030_asset_liability_gap_core04_2nd_v005_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(assets - liabilities, equity.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core05_2nd_v006_signal(assets, liabilities, equity):
    return _clean(_slope(_log((assets - liabilities).abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core06_2nd_v007_signal(assets, liabilities, equity):
    return _clean(_slope(assets, 4))
def cg_f030_asset_liability_gap_core07_2nd_v008_signal(assets, liabilities, equity):
    return _clean(_slope(liabilities, 4))
def cg_f030_asset_liability_gap_core08_2nd_v009_signal(assets, liabilities, equity):
    return _clean(_slope(equity, 4))
def cg_f030_asset_liability_gap_core09_2nd_v010_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(liabilities, assets.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core10_2nd_v011_signal(assets, liabilities, equity):
    return _clean(_slope(assets - liabilities, 8))
def cg_f030_asset_liability_gap_core11_2nd_v012_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(assets, liabilities.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core12_2nd_v013_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(equity, assets.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core13_2nd_v014_signal(assets, liabilities, equity):
    return _clean(_slope(assets - liabilities - equity, 8))
def cg_f030_asset_liability_gap_core14_2nd_v015_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(assets - liabilities, equity.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core15_2nd_v016_signal(assets, liabilities, equity):
    return _clean(_slope(_log((assets - liabilities).abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core16_2nd_v017_signal(assets, liabilities, equity):
    return _clean(_slope(assets, 8))
def cg_f030_asset_liability_gap_core17_2nd_v018_signal(assets, liabilities, equity):
    return _clean(_slope(liabilities, 8))
def cg_f030_asset_liability_gap_core18_2nd_v019_signal(assets, liabilities, equity):
    return _clean(_slope(equity, 8))
def cg_f030_asset_liability_gap_core19_2nd_v020_signal(assets, liabilities, equity):
    return _clean(_slope(_safe_div(liabilities, assets.abs() + 1.0), 8))
def cg_f030_asset_liability_gap_core20_2nd_v021_signal(assets, liabilities, equity):
    return _clean(_diff(assets - liabilities, 4))
def cg_f030_asset_liability_gap_core21_2nd_v022_signal(assets, liabilities, equity):
    return _clean(_diff(_safe_div(assets, liabilities.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core22_2nd_v023_signal(assets, liabilities, equity):
    return _clean(_diff(_safe_div(equity, assets.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core23_2nd_v024_signal(assets, liabilities, equity):
    return _clean(_diff(assets - liabilities - equity, 4))
def cg_f030_asset_liability_gap_core24_2nd_v025_signal(assets, liabilities, equity):
    return _clean(_diff(_safe_div(assets - liabilities, equity.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core25_2nd_v026_signal(assets, liabilities, equity):
    return _clean(_diff(_log((assets - liabilities).abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core26_2nd_v027_signal(assets, liabilities, equity):
    return _clean(_diff(assets, 4))
def cg_f030_asset_liability_gap_core27_2nd_v028_signal(assets, liabilities, equity):
    return _clean(_diff(liabilities, 4))
def cg_f030_asset_liability_gap_core28_2nd_v029_signal(assets, liabilities, equity):
    return _clean(_diff(equity, 4))
def cg_f030_asset_liability_gap_core29_2nd_v030_signal(assets, liabilities, equity):
    return _clean(_diff(_safe_div(liabilities, assets.abs() + 1.0), 4))
def cg_f030_asset_liability_gap_core30_2nd_v031_signal(assets, liabilities, equity):
    return _clean(_z(_slope(assets - liabilities, 4), 8))
def cg_f030_asset_liability_gap_core31_2nd_v032_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(assets, liabilities.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core32_2nd_v033_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core33_2nd_v034_signal(assets, liabilities, equity):
    return _clean(_z(_slope(assets - liabilities - equity, 4), 8))
def cg_f030_asset_liability_gap_core34_2nd_v035_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core35_2nd_v036_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_log((assets - liabilities).abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core36_2nd_v037_signal(assets, liabilities, equity):
    return _clean(_z(_slope(assets, 4), 8))
def cg_f030_asset_liability_gap_core37_2nd_v038_signal(assets, liabilities, equity):
    return _clean(_z(_slope(liabilities, 4), 8))
def cg_f030_asset_liability_gap_core38_2nd_v039_signal(assets, liabilities, equity):
    return _clean(_z(_slope(equity, 4), 8))
def cg_f030_asset_liability_gap_core39_2nd_v040_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(liabilities, assets.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core40_2nd_v041_signal(assets, liabilities, equity):
    return _clean(_z(_slope(assets - liabilities, 8), 12))
def cg_f030_asset_liability_gap_core41_2nd_v042_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(assets, liabilities.abs() + 1.0), 8), 12))
def cg_f030_asset_liability_gap_core42_2nd_v043_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(equity, assets.abs() + 1.0), 8), 12))
def cg_f030_asset_liability_gap_core43_2nd_v044_signal(assets, liabilities, equity):
    return _clean(_z(_slope(assets - liabilities - equity, 8), 12))
def cg_f030_asset_liability_gap_core44_2nd_v045_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(assets - liabilities, equity.abs() + 1.0), 8), 12))
def cg_f030_asset_liability_gap_core45_2nd_v046_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_log((assets - liabilities).abs() + 1.0), 8), 12))
def cg_f030_asset_liability_gap_core46_2nd_v047_signal(assets, liabilities, equity):
    return _clean(_z(_slope(assets, 8), 12))
def cg_f030_asset_liability_gap_core47_2nd_v048_signal(assets, liabilities, equity):
    return _clean(_z(_slope(liabilities, 8), 12))
def cg_f030_asset_liability_gap_core48_2nd_v049_signal(assets, liabilities, equity):
    return _clean(_z(_slope(equity, 8), 12))
def cg_f030_asset_liability_gap_core49_2nd_v050_signal(assets, liabilities, equity):
    return _clean(_z(_slope(_safe_div(liabilities, assets.abs() + 1.0), 8), 12))
def cg_f030_asset_liability_gap_core50_2nd_v051_signal(assets, liabilities, equity):
    return _clean(_z(_diff(assets - liabilities, 4), 8))
def cg_f030_asset_liability_gap_core51_2nd_v052_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_safe_div(assets, liabilities.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core52_2nd_v053_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core53_2nd_v054_signal(assets, liabilities, equity):
    return _clean(_z(_diff(assets - liabilities - equity, 4), 8))
def cg_f030_asset_liability_gap_core54_2nd_v055_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core55_2nd_v056_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_log((assets - liabilities).abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core56_2nd_v057_signal(assets, liabilities, equity):
    return _clean(_z(_diff(assets, 4), 8))
def cg_f030_asset_liability_gap_core57_2nd_v058_signal(assets, liabilities, equity):
    return _clean(_z(_diff(liabilities, 4), 8))
def cg_f030_asset_liability_gap_core58_2nd_v059_signal(assets, liabilities, equity):
    return _clean(_z(_diff(equity, 4), 8))
def cg_f030_asset_liability_gap_core59_2nd_v060_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_safe_div(liabilities, assets.abs() + 1.0), 4), 8))
def cg_f030_asset_liability_gap_core60_2nd_v061_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(assets - liabilities, 4), 12))
def cg_f030_asset_liability_gap_core61_2nd_v062_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_safe_div(assets, liabilities.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core62_2nd_v063_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core63_2nd_v064_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(assets - liabilities - equity, 4), 12))
def cg_f030_asset_liability_gap_core64_2nd_v065_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core65_2nd_v066_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_log((assets - liabilities).abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core66_2nd_v067_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(assets, 4), 12))
def cg_f030_asset_liability_gap_core67_2nd_v068_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(liabilities, 4), 12))
def cg_f030_asset_liability_gap_core68_2nd_v069_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(equity, 4), 12))
def cg_f030_asset_liability_gap_core69_2nd_v070_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_safe_div(liabilities, assets.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core70_2nd_v071_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(assets - liabilities, 4), 12))
def cg_f030_asset_liability_gap_core71_2nd_v072_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(_safe_div(assets, liabilities.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core72_2nd_v073_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core73_2nd_v074_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(assets - liabilities - equity, 4), 12))
def cg_f030_asset_liability_gap_core74_2nd_v075_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core75_2nd_v076_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(_log((assets - liabilities).abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core76_2nd_v077_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(assets, 4), 12))
def cg_f030_asset_liability_gap_core77_2nd_v078_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(liabilities, 4), 12))
def cg_f030_asset_liability_gap_core78_2nd_v079_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(equity, 4), 12))
def cg_f030_asset_liability_gap_core79_2nd_v080_signal(assets, liabilities, equity):
    return _clean(_rank(_diff(_safe_div(liabilities, assets.abs() + 1.0), 4), 12))
def cg_f030_asset_liability_gap_core80_2nd_v081_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(assets - liabilities, 4), 4))
def cg_f030_asset_liability_gap_core81_2nd_v082_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(_safe_div(assets, liabilities.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core82_2nd_v083_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core83_2nd_v084_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(assets - liabilities - equity, 4), 4))
def cg_f030_asset_liability_gap_core84_2nd_v085_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core85_2nd_v086_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(_log((assets - liabilities).abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core86_2nd_v087_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(assets, 4), 4))
def cg_f030_asset_liability_gap_core87_2nd_v088_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(liabilities, 4), 4))
def cg_f030_asset_liability_gap_core88_2nd_v089_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(equity, 4), 4))
def cg_f030_asset_liability_gap_core89_2nd_v090_signal(assets, liabilities, equity):
    return _clean(_mean(_slope(_safe_div(liabilities, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core90_2nd_v091_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(assets - liabilities, 4), 4))
def cg_f030_asset_liability_gap_core91_2nd_v092_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(_safe_div(assets, liabilities.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core92_2nd_v093_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core93_2nd_v094_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(assets - liabilities - equity, 4), 4))
def cg_f030_asset_liability_gap_core94_2nd_v095_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core95_2nd_v096_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(_log((assets - liabilities).abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core96_2nd_v097_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(assets, 4), 4))
def cg_f030_asset_liability_gap_core97_2nd_v098_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(liabilities, 4), 4))
def cg_f030_asset_liability_gap_core98_2nd_v099_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(equity, 4), 4))
def cg_f030_asset_liability_gap_core99_2nd_v100_signal(assets, liabilities, equity):
    return _clean(_mean(_diff(_safe_div(liabilities, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core100_2nd_v101_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(assets - liabilities, 4), 4))
def cg_f030_asset_liability_gap_core101_2nd_v102_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(assets, liabilities.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core102_2nd_v103_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core103_2nd_v104_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(assets - liabilities - equity, 4), 4))
def cg_f030_asset_liability_gap_core104_2nd_v105_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core105_2nd_v106_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_log((assets - liabilities).abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core106_2nd_v107_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f030_asset_liability_gap_core107_2nd_v108_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(liabilities, 4), 4))
def cg_f030_asset_liability_gap_core108_2nd_v109_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(equity, 4), 4))
def cg_f030_asset_liability_gap_core109_2nd_v110_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(liabilities, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core110_2nd_v111_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(assets - liabilities, 8), 8))
def cg_f030_asset_liability_gap_core111_2nd_v112_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(assets, liabilities.abs() + 1.0), 8), 8))
def cg_f030_asset_liability_gap_core112_2nd_v113_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(equity, assets.abs() + 1.0), 8), 8))
def cg_f030_asset_liability_gap_core113_2nd_v114_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(assets - liabilities - equity, 8), 8))
def cg_f030_asset_liability_gap_core114_2nd_v115_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(assets - liabilities, equity.abs() + 1.0), 8), 8))
def cg_f030_asset_liability_gap_core115_2nd_v116_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_log((assets - liabilities).abs() + 1.0), 8), 8))
def cg_f030_asset_liability_gap_core116_2nd_v117_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(assets, 8), 8))
def cg_f030_asset_liability_gap_core117_2nd_v118_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(liabilities, 8), 8))
def cg_f030_asset_liability_gap_core118_2nd_v119_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(equity, 8), 8))
def cg_f030_asset_liability_gap_core119_2nd_v120_signal(assets, liabilities, equity):
    return _clean(_slope(_mean(_safe_div(liabilities, assets.abs() + 1.0), 8), 8))
def cg_f030_asset_liability_gap_core120_2nd_v121_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(assets - liabilities, 4), 4))
def cg_f030_asset_liability_gap_core121_2nd_v122_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(_safe_div(assets, liabilities.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core122_2nd_v123_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core123_2nd_v124_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(assets - liabilities - equity, 4), 4))
def cg_f030_asset_liability_gap_core124_2nd_v125_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core125_2nd_v126_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(_log((assets - liabilities).abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core126_2nd_v127_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f030_asset_liability_gap_core127_2nd_v128_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(liabilities, 4), 4))
def cg_f030_asset_liability_gap_core128_2nd_v129_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(equity, 4), 4))
def cg_f030_asset_liability_gap_core129_2nd_v130_signal(assets, liabilities, equity):
    return _clean(_diff(_mean(_safe_div(liabilities, assets.abs() + 1.0), 4), 4))
def cg_f030_asset_liability_gap_core130_2nd_v131_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(assets - liabilities, 4), 4), 8))
def cg_f030_asset_liability_gap_core131_2nd_v132_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(_safe_div(assets, liabilities.abs() + 1.0), 4), 4), 8))
def cg_f030_asset_liability_gap_core132_2nd_v133_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4), 8))
def cg_f030_asset_liability_gap_core133_2nd_v134_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(assets - liabilities - equity, 4), 4), 8))
def cg_f030_asset_liability_gap_core134_2nd_v135_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 4), 8))
def cg_f030_asset_liability_gap_core135_2nd_v136_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(_log((assets - liabilities).abs() + 1.0), 4), 4), 8))
def cg_f030_asset_liability_gap_core136_2nd_v137_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f030_asset_liability_gap_core137_2nd_v138_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(liabilities, 4), 4), 8))
def cg_f030_asset_liability_gap_core138_2nd_v139_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(equity, 4), 4), 8))
def cg_f030_asset_liability_gap_core139_2nd_v140_signal(assets, liabilities, equity):
    return _clean(_z(_diff(_mean(_safe_div(liabilities, assets.abs() + 1.0), 4), 4), 8))
def cg_f030_asset_liability_gap_core140_2nd_v141_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(assets - liabilities, 4), 4), 12))
def cg_f030_asset_liability_gap_core141_2nd_v142_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(_safe_div(assets, liabilities.abs() + 1.0), 4), 4), 12))
def cg_f030_asset_liability_gap_core142_2nd_v143_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(_safe_div(equity, assets.abs() + 1.0), 4), 4), 12))
def cg_f030_asset_liability_gap_core143_2nd_v144_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(assets - liabilities - equity, 4), 4), 12))
def cg_f030_asset_liability_gap_core144_2nd_v145_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(_safe_div(assets - liabilities, equity.abs() + 1.0), 4), 4), 12))
def cg_f030_asset_liability_gap_core145_2nd_v146_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(_log((assets - liabilities).abs() + 1.0), 4), 4), 12))
def cg_f030_asset_liability_gap_core146_2nd_v147_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f030_asset_liability_gap_core147_2nd_v148_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(liabilities, 4), 4), 12))
def cg_f030_asset_liability_gap_core148_2nd_v149_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(equity, 4), 4), 12))
def cg_f030_asset_liability_gap_core149_2nd_v150_signal(assets, liabilities, equity):
    return _clean(_rank(_slope(_mean(_safe_div(liabilities, assets.abs() + 1.0), 4), 4), 12))