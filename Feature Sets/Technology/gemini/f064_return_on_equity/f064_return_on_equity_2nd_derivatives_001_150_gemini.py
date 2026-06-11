import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f064_return_on_equity_core00_2nd_v001_signal(netinc, equity):
    return _clean(_slope(netinc, 4))
def cg_f064_return_on_equity_core01_2nd_v002_signal(netinc, equity):
    return _clean(_slope(equity, 4))
def cg_f064_return_on_equity_core02_2nd_v003_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core03_2nd_v004_signal(netinc, equity):
    return _clean(_slope(_diff(netinc, 4), 4))
def cg_f064_return_on_equity_core04_2nd_v005_signal(netinc, equity):
    return _clean(_slope(_pct_change(netinc, 4), 4))
def cg_f064_return_on_equity_core05_2nd_v006_signal(netinc, equity):
    return _clean(_slope(_diff(equity, 4), 4))
def cg_f064_return_on_equity_core06_2nd_v007_signal(netinc, equity):
    return _clean(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4))
def cg_f064_return_on_equity_core07_2nd_v008_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core08_2nd_v009_signal(netinc, equity):
    return _clean(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core09_2nd_v010_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4))
def cg_f064_return_on_equity_core10_2nd_v011_signal(netinc, equity):
    return _clean(_slope(netinc, 8))
def cg_f064_return_on_equity_core11_2nd_v012_signal(netinc, equity):
    return _clean(_slope(equity, 8))
def cg_f064_return_on_equity_core12_2nd_v013_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core13_2nd_v014_signal(netinc, equity):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f064_return_on_equity_core14_2nd_v015_signal(netinc, equity):
    return _clean(_slope(_pct_change(netinc, 4), 8))
def cg_f064_return_on_equity_core15_2nd_v016_signal(netinc, equity):
    return _clean(_slope(_diff(equity, 4), 8))
def cg_f064_return_on_equity_core16_2nd_v017_signal(netinc, equity):
    return _clean(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 8))
def cg_f064_return_on_equity_core17_2nd_v018_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core18_2nd_v019_signal(netinc, equity):
    return _clean(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 8))
def cg_f064_return_on_equity_core19_2nd_v020_signal(netinc, equity):
    return _clean(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 8))
def cg_f064_return_on_equity_core20_2nd_v021_signal(netinc, equity):
    return _clean(_diff(netinc, 4))
def cg_f064_return_on_equity_core21_2nd_v022_signal(netinc, equity):
    return _clean(_diff(equity, 4))
def cg_f064_return_on_equity_core22_2nd_v023_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core23_2nd_v024_signal(netinc, equity):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f064_return_on_equity_core24_2nd_v025_signal(netinc, equity):
    return _clean(_diff(_pct_change(netinc, 4), 4))
def cg_f064_return_on_equity_core25_2nd_v026_signal(netinc, equity):
    return _clean(_diff(_diff(equity, 4), 4))
def cg_f064_return_on_equity_core26_2nd_v027_signal(netinc, equity):
    return _clean(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4))
def cg_f064_return_on_equity_core27_2nd_v028_signal(netinc, equity):
    return _clean(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core28_2nd_v029_signal(netinc, equity):
    return _clean(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4))
def cg_f064_return_on_equity_core29_2nd_v030_signal(netinc, equity):
    return _clean(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4))
def cg_f064_return_on_equity_core30_2nd_v031_signal(netinc, equity):
    return _clean(_z(_slope(netinc, 4), 8))
def cg_f064_return_on_equity_core31_2nd_v032_signal(netinc, equity):
    return _clean(_z(_slope(equity, 4), 8))
def cg_f064_return_on_equity_core32_2nd_v033_signal(netinc, equity):
    return _clean(_z(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core33_2nd_v034_signal(netinc, equity):
    return _clean(_z(_slope(_diff(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core34_2nd_v035_signal(netinc, equity):
    return _clean(_z(_slope(_pct_change(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core35_2nd_v036_signal(netinc, equity):
    return _clean(_z(_slope(_diff(equity, 4), 4), 8))
def cg_f064_return_on_equity_core36_2nd_v037_signal(netinc, equity):
    return _clean(_z(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 8))
def cg_f064_return_on_equity_core37_2nd_v038_signal(netinc, equity):
    return _clean(_z(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core38_2nd_v039_signal(netinc, equity):
    return _clean(_z(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core39_2nd_v040_signal(netinc, equity):
    return _clean(_z(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core40_2nd_v041_signal(netinc, equity):
    return _clean(_z(_slope(netinc, 8), 12))
def cg_f064_return_on_equity_core41_2nd_v042_signal(netinc, equity):
    return _clean(_z(_slope(equity, 8), 12))
def cg_f064_return_on_equity_core42_2nd_v043_signal(netinc, equity):
    return _clean(_z(_slope(_safe_div(netinc, equity.abs() + 1.0), 8), 12))
def cg_f064_return_on_equity_core43_2nd_v044_signal(netinc, equity):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f064_return_on_equity_core44_2nd_v045_signal(netinc, equity):
    return _clean(_z(_slope(_pct_change(netinc, 4), 8), 12))
def cg_f064_return_on_equity_core45_2nd_v046_signal(netinc, equity):
    return _clean(_z(_slope(_diff(equity, 4), 8), 12))
def cg_f064_return_on_equity_core46_2nd_v047_signal(netinc, equity):
    return _clean(_z(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 8), 12))
def cg_f064_return_on_equity_core47_2nd_v048_signal(netinc, equity):
    return _clean(_z(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core48_2nd_v049_signal(netinc, equity):
    return _clean(_z(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 8), 12))
def cg_f064_return_on_equity_core49_2nd_v050_signal(netinc, equity):
    return _clean(_z(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 8), 12))
def cg_f064_return_on_equity_core50_2nd_v051_signal(netinc, equity):
    return _clean(_z(_diff(netinc, 4), 8))
def cg_f064_return_on_equity_core51_2nd_v052_signal(netinc, equity):
    return _clean(_z(_diff(equity, 4), 8))
def cg_f064_return_on_equity_core52_2nd_v053_signal(netinc, equity):
    return _clean(_z(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core53_2nd_v054_signal(netinc, equity):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core54_2nd_v055_signal(netinc, equity):
    return _clean(_z(_diff(_pct_change(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core55_2nd_v056_signal(netinc, equity):
    return _clean(_z(_diff(_diff(equity, 4), 4), 8))
def cg_f064_return_on_equity_core56_2nd_v057_signal(netinc, equity):
    return _clean(_z(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 8))
def cg_f064_return_on_equity_core57_2nd_v058_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core58_2nd_v059_signal(netinc, equity):
    return _clean(_z(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core59_2nd_v060_signal(netinc, equity):
    return _clean(_z(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core60_2nd_v061_signal(netinc, equity):
    return _clean(_rank(_slope(netinc, 4), 12))
def cg_f064_return_on_equity_core61_2nd_v062_signal(netinc, equity):
    return _clean(_rank(_slope(equity, 4), 12))
def cg_f064_return_on_equity_core62_2nd_v063_signal(netinc, equity):
    return _clean(_rank(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 12))
def cg_f064_return_on_equity_core63_2nd_v064_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core64_2nd_v065_signal(netinc, equity):
    return _clean(_rank(_slope(_pct_change(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core65_2nd_v066_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(equity, 4), 4), 12))
def cg_f064_return_on_equity_core66_2nd_v067_signal(netinc, equity):
    return _clean(_rank(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 12))
def cg_f064_return_on_equity_core67_2nd_v068_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core68_2nd_v069_signal(netinc, equity):
    return _clean(_rank(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 12))
def cg_f064_return_on_equity_core69_2nd_v070_signal(netinc, equity):
    return _clean(_rank(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 12))
def cg_f064_return_on_equity_core70_2nd_v071_signal(netinc, equity):
    return _clean(_rank(_diff(netinc, 4), 12))
def cg_f064_return_on_equity_core71_2nd_v072_signal(netinc, equity):
    return _clean(_rank(_diff(equity, 4), 12))
def cg_f064_return_on_equity_core72_2nd_v073_signal(netinc, equity):
    return _clean(_rank(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 12))
def cg_f064_return_on_equity_core73_2nd_v074_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core74_2nd_v075_signal(netinc, equity):
    return _clean(_rank(_diff(_pct_change(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core75_2nd_v076_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(equity, 4), 4), 12))
def cg_f064_return_on_equity_core76_2nd_v077_signal(netinc, equity):
    return _clean(_rank(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 12))
def cg_f064_return_on_equity_core77_2nd_v078_signal(netinc, equity):
    return _clean(_rank(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core78_2nd_v079_signal(netinc, equity):
    return _clean(_rank(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 12))
def cg_f064_return_on_equity_core79_2nd_v080_signal(netinc, equity):
    return _clean(_rank(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 12))
def cg_f064_return_on_equity_core80_2nd_v081_signal(netinc, equity):
    return _clean(_mean(_slope(netinc, 4), 4))
def cg_f064_return_on_equity_core81_2nd_v082_signal(netinc, equity):
    return _clean(_mean(_slope(equity, 4), 4))
def cg_f064_return_on_equity_core82_2nd_v083_signal(netinc, equity):
    return _clean(_mean(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core83_2nd_v084_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core84_2nd_v085_signal(netinc, equity):
    return _clean(_mean(_slope(_pct_change(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core85_2nd_v086_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core86_2nd_v087_signal(netinc, equity):
    return _clean(_mean(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4))
def cg_f064_return_on_equity_core87_2nd_v088_signal(netinc, equity):
    return _clean(_mean(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core88_2nd_v089_signal(netinc, equity):
    return _clean(_mean(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core89_2nd_v090_signal(netinc, equity):
    return _clean(_mean(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core90_2nd_v091_signal(netinc, equity):
    return _clean(_mean(_diff(netinc, 4), 4))
def cg_f064_return_on_equity_core91_2nd_v092_signal(netinc, equity):
    return _clean(_mean(_diff(equity, 4), 4))
def cg_f064_return_on_equity_core92_2nd_v093_signal(netinc, equity):
    return _clean(_mean(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core93_2nd_v094_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core94_2nd_v095_signal(netinc, equity):
    return _clean(_mean(_diff(_pct_change(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core95_2nd_v096_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core96_2nd_v097_signal(netinc, equity):
    return _clean(_mean(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4))
def cg_f064_return_on_equity_core97_2nd_v098_signal(netinc, equity):
    return _clean(_mean(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core98_2nd_v099_signal(netinc, equity):
    return _clean(_mean(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core99_2nd_v100_signal(netinc, equity):
    return _clean(_mean(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core100_2nd_v101_signal(netinc, equity):
    return _clean(_slope(_mean(netinc, 4), 4))
def cg_f064_return_on_equity_core101_2nd_v102_signal(netinc, equity):
    return _clean(_slope(_mean(equity, 4), 4))
def cg_f064_return_on_equity_core102_2nd_v103_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core103_2nd_v104_signal(netinc, equity):
    return _clean(_slope(_mean(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core104_2nd_v105_signal(netinc, equity):
    return _clean(_slope(_mean(_pct_change(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core105_2nd_v106_signal(netinc, equity):
    return _clean(_slope(_mean(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core106_2nd_v107_signal(netinc, equity):
    return _clean(_slope(_mean(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4))
def cg_f064_return_on_equity_core107_2nd_v108_signal(netinc, equity):
    return _clean(_slope(_mean(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core108_2nd_v109_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core109_2nd_v110_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core110_2nd_v111_signal(netinc, equity):
    return _clean(_slope(_mean(netinc, 8), 8))
def cg_f064_return_on_equity_core111_2nd_v112_signal(netinc, equity):
    return _clean(_slope(_mean(equity, 8), 8))
def cg_f064_return_on_equity_core112_2nd_v113_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 8), 8))
def cg_f064_return_on_equity_core113_2nd_v114_signal(netinc, equity):
    return _clean(_slope(_mean(_diff(netinc, 4), 8), 8))
def cg_f064_return_on_equity_core114_2nd_v115_signal(netinc, equity):
    return _clean(_slope(_mean(_pct_change(netinc, 4), 8), 8))
def cg_f064_return_on_equity_core115_2nd_v116_signal(netinc, equity):
    return _clean(_slope(_mean(_diff(equity, 4), 8), 8))
def cg_f064_return_on_equity_core116_2nd_v117_signal(netinc, equity):
    return _clean(_slope(_mean(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 8), 8))
def cg_f064_return_on_equity_core117_2nd_v118_signal(netinc, equity):
    return _clean(_slope(_mean(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 8))
def cg_f064_return_on_equity_core118_2nd_v119_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 8), 8))
def cg_f064_return_on_equity_core119_2nd_v120_signal(netinc, equity):
    return _clean(_slope(_mean(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 8), 8))
def cg_f064_return_on_equity_core120_2nd_v121_signal(netinc, equity):
    return _clean(_diff(_mean(netinc, 4), 4))
def cg_f064_return_on_equity_core121_2nd_v122_signal(netinc, equity):
    return _clean(_diff(_mean(equity, 4), 4))
def cg_f064_return_on_equity_core122_2nd_v123_signal(netinc, equity):
    return _clean(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core123_2nd_v124_signal(netinc, equity):
    return _clean(_diff(_mean(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core124_2nd_v125_signal(netinc, equity):
    return _clean(_diff(_mean(_pct_change(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core125_2nd_v126_signal(netinc, equity):
    return _clean(_diff(_mean(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core126_2nd_v127_signal(netinc, equity):
    return _clean(_diff(_mean(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4))
def cg_f064_return_on_equity_core127_2nd_v128_signal(netinc, equity):
    return _clean(_diff(_mean(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core128_2nd_v129_signal(netinc, equity):
    return _clean(_diff(_mean(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core129_2nd_v130_signal(netinc, equity):
    return _clean(_diff(_mean(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core130_2nd_v131_signal(netinc, equity):
    return _clean(_z(_diff(_mean(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core131_2nd_v132_signal(netinc, equity):
    return _clean(_z(_diff(_mean(equity, 4), 4), 8))
def cg_f064_return_on_equity_core132_2nd_v133_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core133_2nd_v134_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_diff(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core134_2nd_v135_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_pct_change(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core135_2nd_v136_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_diff(equity, 4), 4), 4), 8))
def cg_f064_return_on_equity_core136_2nd_v137_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 8))
def cg_f064_return_on_equity_core137_2nd_v138_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f064_return_on_equity_core138_2nd_v139_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core139_2nd_v140_signal(netinc, equity):
    return _clean(_z(_diff(_mean(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core140_2nd_v141_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core141_2nd_v142_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(equity, 4), 4), 12))
def cg_f064_return_on_equity_core142_2nd_v143_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core143_2nd_v144_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_diff(netinc, 4), 4), 4), 12))
def cg_f064_return_on_equity_core144_2nd_v145_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_pct_change(netinc, 4), 4), 4), 12))
def cg_f064_return_on_equity_core145_2nd_v146_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_diff(equity, 4), 4), 4), 12))
def cg_f064_return_on_equity_core146_2nd_v147_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 12))
def cg_f064_return_on_equity_core147_2nd_v148_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 12))
def cg_f064_return_on_equity_core148_2nd_v149_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core149_2nd_v150_signal(netinc, equity):
    return _clean(_rank(_slope(_mean(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 12))