import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f064_return_on_equity_core00_3rd_v001_signal(netinc, equity):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f064_return_on_equity_core01_3rd_v002_signal(netinc, equity):
    return _clean(_diff(_diff(equity, 4), 4))
def cg_f064_return_on_equity_core02_3rd_v003_signal(netinc, equity):
    return _clean(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core03_3rd_v004_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core04_3rd_v005_signal(netinc, equity):
    return _clean(_diff(_diff(_pct_change(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core05_3rd_v006_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core06_3rd_v007_signal(netinc, equity):
    return _clean(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4))
def cg_f064_return_on_equity_core07_3rd_v008_signal(netinc, equity):
    return _clean(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core08_3rd_v009_signal(netinc, equity):
    return _clean(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core09_3rd_v010_signal(netinc, equity):
    return _clean(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core10_3rd_v011_signal(netinc, equity):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f064_return_on_equity_core11_3rd_v012_signal(netinc, equity):
    return _clean(_slope(_diff(equity, 4), 8))
def cg_f064_return_on_equity_core12_3rd_v013_signal(netinc, equity):
    return _clean(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core13_3rd_v014_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core14_3rd_v015_signal(netinc, equity):
    return _clean(_slope(_diff(_pct_change(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core15_3rd_v016_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(equity, 4), 4), 8))
def cg_f064_return_on_equity_core16_3rd_v017_signal(netinc, equity):
    return _clean(_slope(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 8))
def cg_f064_return_on_equity_core17_3rd_v018_signal(netinc, equity):
    return _clean(_slope(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core18_3rd_v019_signal(netinc, equity):
    return _clean(_slope(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core19_3rd_v020_signal(netinc, equity):
    return _clean(_slope(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 8))
def cg_f064_return_on_equity_core20_3rd_v021_signal(netinc, equity):
    return _clean(_diff(_slope(netinc, 4), 4))
def cg_f064_return_on_equity_core21_3rd_v022_signal(netinc, equity):
    return _clean(_diff(_slope(equity, 4), 4))
def cg_f064_return_on_equity_core22_3rd_v023_signal(netinc, equity):
    return _clean(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core23_3rd_v024_signal(netinc, equity):
    return _clean(_diff(_slope(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core24_3rd_v025_signal(netinc, equity):
    return _clean(_diff(_slope(_pct_change(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core25_3rd_v026_signal(netinc, equity):
    return _clean(_diff(_slope(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core26_3rd_v027_signal(netinc, equity):
    return _clean(_diff(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4))
def cg_f064_return_on_equity_core27_3rd_v028_signal(netinc, equity):
    return _clean(_diff(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core28_3rd_v029_signal(netinc, equity):
    return _clean(_diff(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core29_3rd_v030_signal(netinc, equity):
    return _clean(_diff(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4))
def cg_f064_return_on_equity_core30_3rd_v031_signal(netinc, equity):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core31_3rd_v032_signal(netinc, equity):
    return _clean(_z(_diff(_diff(equity, 4), 4), 8))
def cg_f064_return_on_equity_core32_3rd_v033_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core33_3rd_v034_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core34_3rd_v035_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_pct_change(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core35_3rd_v036_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_diff(equity, 4), 4), 4), 8))
def cg_f064_return_on_equity_core36_3rd_v037_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 8))
def cg_f064_return_on_equity_core37_3rd_v038_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f064_return_on_equity_core38_3rd_v039_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core39_3rd_v040_signal(netinc, equity):
    return _clean(_z(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core40_3rd_v041_signal(netinc, equity):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f064_return_on_equity_core41_3rd_v042_signal(netinc, equity):
    return _clean(_z(_slope(_diff(equity, 4), 8), 12))
def cg_f064_return_on_equity_core42_3rd_v043_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core43_3rd_v044_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 8), 12))
def cg_f064_return_on_equity_core44_3rd_v045_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_pct_change(netinc, 4), 4), 8), 12))
def cg_f064_return_on_equity_core45_3rd_v046_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(equity, 4), 4), 8), 12))
def cg_f064_return_on_equity_core46_3rd_v047_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 8), 12))
def cg_f064_return_on_equity_core47_3rd_v048_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8), 12))
def cg_f064_return_on_equity_core48_3rd_v049_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core49_3rd_v050_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core50_3rd_v051_signal(netinc, equity):
    return _clean(_z(_diff(_slope(netinc, 4), 4), 8))
def cg_f064_return_on_equity_core51_3rd_v052_signal(netinc, equity):
    return _clean(_z(_diff(_slope(equity, 4), 4), 8))
def cg_f064_return_on_equity_core52_3rd_v053_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core53_3rd_v054_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_diff(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core54_3rd_v055_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_pct_change(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core55_3rd_v056_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_diff(equity, 4), 4), 4), 8))
def cg_f064_return_on_equity_core56_3rd_v057_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 8))
def cg_f064_return_on_equity_core57_3rd_v058_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f064_return_on_equity_core58_3rd_v059_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core59_3rd_v060_signal(netinc, equity):
    return _clean(_z(_diff(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 8))
def cg_f064_return_on_equity_core60_3rd_v061_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core61_3rd_v062_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(equity, 4), 4), 12))
def cg_f064_return_on_equity_core62_3rd_v063_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core63_3rd_v064_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_diff(netinc, 4), 4), 4), 12))
def cg_f064_return_on_equity_core64_3rd_v065_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_pct_change(netinc, 4), 4), 4), 12))
def cg_f064_return_on_equity_core65_3rd_v066_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_diff(equity, 4), 4), 4), 12))
def cg_f064_return_on_equity_core66_3rd_v067_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 12))
def cg_f064_return_on_equity_core67_3rd_v068_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 12))
def cg_f064_return_on_equity_core68_3rd_v069_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core69_3rd_v070_signal(netinc, equity):
    return _clean(_rank(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core70_3rd_v071_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(netinc, 4), 8), 12))
def cg_f064_return_on_equity_core71_3rd_v072_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(equity, 4), 8), 12))
def cg_f064_return_on_equity_core72_3rd_v073_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core73_3rd_v074_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_diff(netinc, 4), 4), 8), 12))
def cg_f064_return_on_equity_core74_3rd_v075_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_pct_change(netinc, 4), 4), 8), 12))
def cg_f064_return_on_equity_core75_3rd_v076_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_diff(equity, 4), 4), 8), 12))
def cg_f064_return_on_equity_core76_3rd_v077_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 8), 12))
def cg_f064_return_on_equity_core77_3rd_v078_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8), 12))
def cg_f064_return_on_equity_core78_3rd_v079_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core79_3rd_v080_signal(netinc, equity):
    return _clean(_rank(_slope(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 8), 12))
def cg_f064_return_on_equity_core80_3rd_v081_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(netinc, 4), 4), 12))
def cg_f064_return_on_equity_core81_3rd_v082_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(equity, 4), 4), 12))
def cg_f064_return_on_equity_core82_3rd_v083_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core83_3rd_v084_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_diff(netinc, 4), 4), 4), 12))
def cg_f064_return_on_equity_core84_3rd_v085_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_pct_change(netinc, 4), 4), 4), 12))
def cg_f064_return_on_equity_core85_3rd_v086_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_diff(equity, 4), 4), 4), 12))
def cg_f064_return_on_equity_core86_3rd_v087_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 12))
def cg_f064_return_on_equity_core87_3rd_v088_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 12))
def cg_f064_return_on_equity_core88_3rd_v089_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core89_3rd_v090_signal(netinc, equity):
    return _clean(_rank(_diff(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 12))
def cg_f064_return_on_equity_core90_3rd_v091_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core91_3rd_v092_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core92_3rd_v093_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core93_3rd_v094_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_diff(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core94_3rd_v095_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_pct_change(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core95_3rd_v096_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_diff(equity, 4), 4), 4), 4))
def cg_f064_return_on_equity_core96_3rd_v097_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 4))
def cg_f064_return_on_equity_core97_3rd_v098_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 4))
def cg_f064_return_on_equity_core98_3rd_v099_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core99_3rd_v100_signal(netinc, equity):
    return _clean(_mean(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core100_3rd_v101_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(netinc, 4), 8), 4))
def cg_f064_return_on_equity_core101_3rd_v102_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(equity, 4), 8), 4))
def cg_f064_return_on_equity_core102_3rd_v103_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 8), 4))
def cg_f064_return_on_equity_core103_3rd_v104_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_diff(netinc, 4), 4), 8), 4))
def cg_f064_return_on_equity_core104_3rd_v105_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_pct_change(netinc, 4), 4), 8), 4))
def cg_f064_return_on_equity_core105_3rd_v106_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_diff(equity, 4), 4), 8), 4))
def cg_f064_return_on_equity_core106_3rd_v107_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 8), 4))
def cg_f064_return_on_equity_core107_3rd_v108_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 8), 4))
def cg_f064_return_on_equity_core108_3rd_v109_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 8), 4))
def cg_f064_return_on_equity_core109_3rd_v110_signal(netinc, equity):
    return _clean(_mean(_slope(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 8), 4))
def cg_f064_return_on_equity_core110_3rd_v111_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core111_3rd_v112_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(equity, 4), 4), 4))
def cg_f064_return_on_equity_core112_3rd_v113_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core113_3rd_v114_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_diff(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core114_3rd_v115_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_pct_change(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core115_3rd_v116_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_diff(equity, 4), 4), 4), 4))
def cg_f064_return_on_equity_core116_3rd_v117_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 4))
def cg_f064_return_on_equity_core117_3rd_v118_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 4))
def cg_f064_return_on_equity_core118_3rd_v119_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core119_3rd_v120_signal(netinc, equity):
    return _clean(_mean(_diff(_slope(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core120_3rd_v121_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core121_3rd_v122_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core122_3rd_v123_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core123_3rd_v124_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_diff(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core124_3rd_v125_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_pct_change(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core125_3rd_v126_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_diff(equity, 4), 4), 4), 4))
def cg_f064_return_on_equity_core126_3rd_v127_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 4))
def cg_f064_return_on_equity_core127_3rd_v128_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 4))
def cg_f064_return_on_equity_core128_3rd_v129_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core129_3rd_v130_signal(netinc, equity):
    return _clean(_slope(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core130_3rd_v131_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f064_return_on_equity_core131_3rd_v132_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(equity, 4), 4), 4))
def cg_f064_return_on_equity_core132_3rd_v133_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core133_3rd_v134_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_diff(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core134_3rd_v135_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_pct_change(netinc, 4), 4), 4), 4))
def cg_f064_return_on_equity_core135_3rd_v136_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_diff(equity, 4), 4), 4), 4))
def cg_f064_return_on_equity_core136_3rd_v137_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 4))
def cg_f064_return_on_equity_core137_3rd_v138_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 4))
def cg_f064_return_on_equity_core138_3rd_v139_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core139_3rd_v140_signal(netinc, equity):
    return _clean(_diff(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 4))
def cg_f064_return_on_equity_core140_3rd_v141_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f064_return_on_equity_core141_3rd_v142_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(equity, 4), 4), 4), 8))
def cg_f064_return_on_equity_core142_3rd_v143_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f064_return_on_equity_core143_3rd_v144_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_diff(netinc, 4), 4), 4), 4), 8))
def cg_f064_return_on_equity_core144_3rd_v145_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_pct_change(netinc, 4), 4), 4), 4), 8))
def cg_f064_return_on_equity_core145_3rd_v146_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_diff(equity, 4), 4), 4), 4), 8))
def cg_f064_return_on_equity_core146_3rd_v147_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_z(_safe_div(netinc, equity.abs() + 1.0), 8), 4), 4), 4), 8))
def cg_f064_return_on_equity_core147_3rd_v148_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_mean(_safe_div(netinc, equity.abs() + 1.0), 4), 4), 4), 4), 8))
def cg_f064_return_on_equity_core148_3rd_v149_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(_diff(netinc, 4), equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f064_return_on_equity_core149_3rd_v150_signal(netinc, equity):
    return _clean(_z(_slope(_diff(_diff(_safe_div(netinc, _diff(equity, 4).abs() + 1.0), 4), 4), 4), 8))