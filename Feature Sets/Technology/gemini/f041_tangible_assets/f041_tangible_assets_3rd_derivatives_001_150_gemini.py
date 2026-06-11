import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f041_tangible_assets_core00_3rd_v001_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(tangibles, 4), 4))
def cg_f041_tangible_assets_core01_3rd_v002_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(intangibles, 4), 4))
def cg_f041_tangible_assets_core02_3rd_v003_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_safe_div(tangibles, assets), 4), 4))
def cg_f041_tangible_assets_core03_3rd_v004_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_safe_div(intangibles, assets), 4), 4))
def cg_f041_tangible_assets_core04_3rd_v005_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_safe_div(tangibles, equity), 4), 4))
def cg_f041_tangible_assets_core05_3rd_v006_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_safe_div(intangibles, equity), 4), 4))
def cg_f041_tangible_assets_core06_3rd_v007_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(assets - tangibles, 4), 4))
def cg_f041_tangible_assets_core07_3rd_v008_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(tangibles + intangibles, 4), 4))
def cg_f041_tangible_assets_core08_3rd_v009_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core09_3rd_v010_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_pct_change(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core10_3rd_v011_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(tangibles, 4), 8))
def cg_f041_tangible_assets_core11_3rd_v012_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(intangibles, 4), 8))
def cg_f041_tangible_assets_core12_3rd_v013_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_safe_div(tangibles, assets), 4), 8))
def cg_f041_tangible_assets_core13_3rd_v014_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_safe_div(intangibles, assets), 4), 8))
def cg_f041_tangible_assets_core14_3rd_v015_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_safe_div(tangibles, equity), 4), 8))
def cg_f041_tangible_assets_core15_3rd_v016_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_safe_div(intangibles, equity), 4), 8))
def cg_f041_tangible_assets_core16_3rd_v017_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(assets - tangibles, 4), 8))
def cg_f041_tangible_assets_core17_3rd_v018_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(tangibles + intangibles, 4), 8))
def cg_f041_tangible_assets_core18_3rd_v019_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(tangibles, 4), 4), 8))
def cg_f041_tangible_assets_core19_3rd_v020_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_pct_change(tangibles, 4), 4), 8))
def cg_f041_tangible_assets_core20_3rd_v021_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(tangibles, 4), 4))
def cg_f041_tangible_assets_core21_3rd_v022_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(intangibles, 4), 4))
def cg_f041_tangible_assets_core22_3rd_v023_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(_safe_div(tangibles, assets), 4), 4))
def cg_f041_tangible_assets_core23_3rd_v024_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(_safe_div(intangibles, assets), 4), 4))
def cg_f041_tangible_assets_core24_3rd_v025_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(_safe_div(tangibles, equity), 4), 4))
def cg_f041_tangible_assets_core25_3rd_v026_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(_safe_div(intangibles, equity), 4), 4))
def cg_f041_tangible_assets_core26_3rd_v027_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(assets - tangibles, 4), 4))
def cg_f041_tangible_assets_core27_3rd_v028_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(tangibles + intangibles, 4), 4))
def cg_f041_tangible_assets_core28_3rd_v029_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(_diff(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core29_3rd_v030_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_slope(_pct_change(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core30_3rd_v031_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(tangibles, 4), 4), 8))
def cg_f041_tangible_assets_core31_3rd_v032_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(intangibles, 4), 4), 8))
def cg_f041_tangible_assets_core32_3rd_v033_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(_safe_div(tangibles, assets), 4), 4), 8))
def cg_f041_tangible_assets_core33_3rd_v034_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 8))
def cg_f041_tangible_assets_core34_3rd_v035_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(_safe_div(tangibles, equity), 4), 4), 8))
def cg_f041_tangible_assets_core35_3rd_v036_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(_safe_div(intangibles, equity), 4), 4), 8))
def cg_f041_tangible_assets_core36_3rd_v037_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(assets - tangibles, 4), 4), 8))
def cg_f041_tangible_assets_core37_3rd_v038_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(tangibles + intangibles, 4), 4), 8))
def cg_f041_tangible_assets_core38_3rd_v039_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(_diff(tangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core39_3rd_v040_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_diff(_pct_change(tangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core40_3rd_v041_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(tangibles, 4), 8), 12))
def cg_f041_tangible_assets_core41_3rd_v042_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(intangibles, 4), 8), 12))
def cg_f041_tangible_assets_core42_3rd_v043_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_safe_div(tangibles, assets), 4), 8), 12))
def cg_f041_tangible_assets_core43_3rd_v044_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_safe_div(intangibles, assets), 4), 8), 12))
def cg_f041_tangible_assets_core44_3rd_v045_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_safe_div(tangibles, equity), 4), 8), 12))
def cg_f041_tangible_assets_core45_3rd_v046_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_safe_div(intangibles, equity), 4), 8), 12))
def cg_f041_tangible_assets_core46_3rd_v047_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(assets - tangibles, 4), 8), 12))
def cg_f041_tangible_assets_core47_3rd_v048_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(tangibles + intangibles, 4), 8), 12))
def cg_f041_tangible_assets_core48_3rd_v049_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(tangibles, 4), 4), 8), 12))
def cg_f041_tangible_assets_core49_3rd_v050_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_pct_change(tangibles, 4), 4), 8), 12))
def cg_f041_tangible_assets_core50_3rd_v051_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(tangibles, 4), 4), 8))
def cg_f041_tangible_assets_core51_3rd_v052_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(intangibles, 4), 4), 8))
def cg_f041_tangible_assets_core52_3rd_v053_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(_safe_div(tangibles, assets), 4), 4), 8))
def cg_f041_tangible_assets_core53_3rd_v054_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(_safe_div(intangibles, assets), 4), 4), 8))
def cg_f041_tangible_assets_core54_3rd_v055_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(_safe_div(tangibles, equity), 4), 4), 8))
def cg_f041_tangible_assets_core55_3rd_v056_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(_safe_div(intangibles, equity), 4), 4), 8))
def cg_f041_tangible_assets_core56_3rd_v057_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(assets - tangibles, 4), 4), 8))
def cg_f041_tangible_assets_core57_3rd_v058_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(tangibles + intangibles, 4), 4), 8))
def cg_f041_tangible_assets_core58_3rd_v059_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(_diff(tangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core59_3rd_v060_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_diff(_slope(_pct_change(tangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core60_3rd_v061_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(tangibles, 4), 4), 12))
def cg_f041_tangible_assets_core61_3rd_v062_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(intangibles, 4), 4), 12))
def cg_f041_tangible_assets_core62_3rd_v063_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(_safe_div(tangibles, assets), 4), 4), 12))
def cg_f041_tangible_assets_core63_3rd_v064_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 12))
def cg_f041_tangible_assets_core64_3rd_v065_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(_safe_div(tangibles, equity), 4), 4), 12))
def cg_f041_tangible_assets_core65_3rd_v066_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(_safe_div(intangibles, equity), 4), 4), 12))
def cg_f041_tangible_assets_core66_3rd_v067_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(assets - tangibles, 4), 4), 12))
def cg_f041_tangible_assets_core67_3rd_v068_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(tangibles + intangibles, 4), 4), 12))
def cg_f041_tangible_assets_core68_3rd_v069_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(_diff(tangibles, 4), 4), 4), 12))
def cg_f041_tangible_assets_core69_3rd_v070_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_diff(_pct_change(tangibles, 4), 4), 4), 12))
def cg_f041_tangible_assets_core70_3rd_v071_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(tangibles, 4), 8), 12))
def cg_f041_tangible_assets_core71_3rd_v072_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(intangibles, 4), 8), 12))
def cg_f041_tangible_assets_core72_3rd_v073_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(_safe_div(tangibles, assets), 4), 8), 12))
def cg_f041_tangible_assets_core73_3rd_v074_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(_safe_div(intangibles, assets), 4), 8), 12))
def cg_f041_tangible_assets_core74_3rd_v075_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(_safe_div(tangibles, equity), 4), 8), 12))
def cg_f041_tangible_assets_core75_3rd_v076_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(_safe_div(intangibles, equity), 4), 8), 12))
def cg_f041_tangible_assets_core76_3rd_v077_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(assets - tangibles, 4), 8), 12))
def cg_f041_tangible_assets_core77_3rd_v078_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(tangibles + intangibles, 4), 8), 12))
def cg_f041_tangible_assets_core78_3rd_v079_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(_diff(tangibles, 4), 4), 8), 12))
def cg_f041_tangible_assets_core79_3rd_v080_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_slope(_diff(_pct_change(tangibles, 4), 4), 8), 12))
def cg_f041_tangible_assets_core80_3rd_v081_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(tangibles, 4), 4), 12))
def cg_f041_tangible_assets_core81_3rd_v082_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(intangibles, 4), 4), 12))
def cg_f041_tangible_assets_core82_3rd_v083_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(_safe_div(tangibles, assets), 4), 4), 12))
def cg_f041_tangible_assets_core83_3rd_v084_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(_safe_div(intangibles, assets), 4), 4), 12))
def cg_f041_tangible_assets_core84_3rd_v085_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(_safe_div(tangibles, equity), 4), 4), 12))
def cg_f041_tangible_assets_core85_3rd_v086_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(_safe_div(intangibles, equity), 4), 4), 12))
def cg_f041_tangible_assets_core86_3rd_v087_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(assets - tangibles, 4), 4), 12))
def cg_f041_tangible_assets_core87_3rd_v088_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(tangibles + intangibles, 4), 4), 12))
def cg_f041_tangible_assets_core88_3rd_v089_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(_diff(tangibles, 4), 4), 4), 12))
def cg_f041_tangible_assets_core89_3rd_v090_signal(tangibles, intangibles, assets, equity):
    return _clean(_rank(_diff(_slope(_pct_change(tangibles, 4), 4), 4), 12))
def cg_f041_tangible_assets_core90_3rd_v091_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core91_3rd_v092_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core92_3rd_v093_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(_safe_div(tangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core93_3rd_v094_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core94_3rd_v095_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(_safe_div(tangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core95_3rd_v096_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(_safe_div(intangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core96_3rd_v097_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(assets - tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core97_3rd_v098_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(tangibles + intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core98_3rd_v099_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(_diff(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core99_3rd_v100_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_diff(_pct_change(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core100_3rd_v101_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(tangibles, 4), 8), 4))
def cg_f041_tangible_assets_core101_3rd_v102_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(intangibles, 4), 8), 4))
def cg_f041_tangible_assets_core102_3rd_v103_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(_safe_div(tangibles, assets), 4), 8), 4))
def cg_f041_tangible_assets_core103_3rd_v104_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(_safe_div(intangibles, assets), 4), 8), 4))
def cg_f041_tangible_assets_core104_3rd_v105_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(_safe_div(tangibles, equity), 4), 8), 4))
def cg_f041_tangible_assets_core105_3rd_v106_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(_safe_div(intangibles, equity), 4), 8), 4))
def cg_f041_tangible_assets_core106_3rd_v107_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(assets - tangibles, 4), 8), 4))
def cg_f041_tangible_assets_core107_3rd_v108_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(tangibles + intangibles, 4), 8), 4))
def cg_f041_tangible_assets_core108_3rd_v109_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(_diff(tangibles, 4), 4), 8), 4))
def cg_f041_tangible_assets_core109_3rd_v110_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_slope(_diff(_pct_change(tangibles, 4), 4), 8), 4))
def cg_f041_tangible_assets_core110_3rd_v111_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core111_3rd_v112_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core112_3rd_v113_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(_safe_div(tangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core113_3rd_v114_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core114_3rd_v115_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(_safe_div(tangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core115_3rd_v116_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(_safe_div(intangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core116_3rd_v117_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(assets - tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core117_3rd_v118_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(tangibles + intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core118_3rd_v119_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(_diff(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core119_3rd_v120_signal(tangibles, intangibles, assets, equity):
    return _clean(_mean(_diff(_slope(_pct_change(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core120_3rd_v121_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core121_3rd_v122_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core122_3rd_v123_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(_safe_div(tangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core123_3rd_v124_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core124_3rd_v125_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(_safe_div(tangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core125_3rd_v126_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(_safe_div(intangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core126_3rd_v127_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(assets - tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core127_3rd_v128_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(tangibles + intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core128_3rd_v129_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(_diff(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core129_3rd_v130_signal(tangibles, intangibles, assets, equity):
    return _clean(_slope(_diff(_diff(_pct_change(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core130_3rd_v131_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core131_3rd_v132_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core132_3rd_v133_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(_safe_div(tangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core133_3rd_v134_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4))
def cg_f041_tangible_assets_core134_3rd_v135_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(_safe_div(tangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core135_3rd_v136_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(_safe_div(intangibles, equity), 4), 4), 4))
def cg_f041_tangible_assets_core136_3rd_v137_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(assets - tangibles, 4), 4), 4))
def cg_f041_tangible_assets_core137_3rd_v138_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(tangibles + intangibles, 4), 4), 4))
def cg_f041_tangible_assets_core138_3rd_v139_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(_diff(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core139_3rd_v140_signal(tangibles, intangibles, assets, equity):
    return _clean(_diff(_diff(_diff(_pct_change(tangibles, 4), 4), 4), 4))
def cg_f041_tangible_assets_core140_3rd_v141_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(tangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core141_3rd_v142_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(intangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core142_3rd_v143_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(tangibles, assets), 4), 4), 4), 8))
def cg_f041_tangible_assets_core143_3rd_v144_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(intangibles, assets), 4), 4), 4), 8))
def cg_f041_tangible_assets_core144_3rd_v145_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(tangibles, equity), 4), 4), 4), 8))
def cg_f041_tangible_assets_core145_3rd_v146_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(intangibles, equity), 4), 4), 4), 8))
def cg_f041_tangible_assets_core146_3rd_v147_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(assets - tangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core147_3rd_v148_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(tangibles + intangibles, 4), 4), 4), 8))
def cg_f041_tangible_assets_core148_3rd_v149_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(_diff(tangibles, 4), 4), 4), 4), 8))
def cg_f041_tangible_assets_core149_3rd_v150_signal(tangibles, intangibles, assets, equity):
    return _clean(_z(_slope(_diff(_diff(_pct_change(tangibles, 4), 4), 4), 4), 8))