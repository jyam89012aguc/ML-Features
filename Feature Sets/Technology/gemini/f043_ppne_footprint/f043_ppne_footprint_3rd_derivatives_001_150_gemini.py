import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f043_ppne_footprint_core00_3rd_v001_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core01_3rd_v002_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(capex, 4), 4))
def cg_f043_ppne_footprint_core02_3rd_v003_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_safe_div(ppnenet, assets), 4), 4))
def cg_f043_ppne_footprint_core03_3rd_v004_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_safe_div(capex, assets), 4), 4))
def cg_f043_ppne_footprint_core04_3rd_v005_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f043_ppne_footprint_core05_3rd_v006_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core06_3rd_v007_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_pct_change(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core07_3rd_v008_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_slope(ppnenet, 8), 4), 4))
def cg_f043_ppne_footprint_core08_3rd_v009_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_z(ppnenet, 12), 4), 4))
def cg_f043_ppne_footprint_core09_3rd_v010_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_mean(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core10_3rd_v011_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core11_3rd_v012_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(capex, 4), 8))
def cg_f043_ppne_footprint_core12_3rd_v013_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_safe_div(ppnenet, assets), 4), 8))
def cg_f043_ppne_footprint_core13_3rd_v014_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_safe_div(capex, assets), 4), 8))
def cg_f043_ppne_footprint_core14_3rd_v015_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8))
def cg_f043_ppne_footprint_core15_3rd_v016_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core16_3rd_v017_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_pct_change(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core17_3rd_v018_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_slope(ppnenet, 8), 4), 8))
def cg_f043_ppne_footprint_core18_3rd_v019_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_z(ppnenet, 12), 4), 8))
def cg_f043_ppne_footprint_core19_3rd_v020_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_mean(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core20_3rd_v021_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core21_3rd_v022_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(capex, 4), 4))
def cg_f043_ppne_footprint_core22_3rd_v023_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_safe_div(ppnenet, assets), 4), 4))
def cg_f043_ppne_footprint_core23_3rd_v024_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_safe_div(capex, assets), 4), 4))
def cg_f043_ppne_footprint_core24_3rd_v025_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f043_ppne_footprint_core25_3rd_v026_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core26_3rd_v027_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_pct_change(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core27_3rd_v028_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_slope(ppnenet, 8), 4), 4))
def cg_f043_ppne_footprint_core28_3rd_v029_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_z(ppnenet, 12), 4), 4))
def cg_f043_ppne_footprint_core29_3rd_v030_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(_mean(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core30_3rd_v031_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core31_3rd_v032_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(capex, 4), 4), 8))
def cg_f043_ppne_footprint_core32_3rd_v033_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_safe_div(ppnenet, assets), 4), 4), 8))
def cg_f043_ppne_footprint_core33_3rd_v034_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_safe_div(capex, assets), 4), 4), 8))
def cg_f043_ppne_footprint_core34_3rd_v035_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 8))
def cg_f043_ppne_footprint_core35_3rd_v036_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_diff(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core36_3rd_v037_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_pct_change(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core37_3rd_v038_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_slope(ppnenet, 8), 4), 4), 8))
def cg_f043_ppne_footprint_core38_3rd_v039_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_z(ppnenet, 12), 4), 4), 8))
def cg_f043_ppne_footprint_core39_3rd_v040_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(_mean(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core40_3rd_v041_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(ppnenet, 4), 8), 12))
def cg_f043_ppne_footprint_core41_3rd_v042_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(capex, 4), 8), 12))
def cg_f043_ppne_footprint_core42_3rd_v043_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_safe_div(ppnenet, assets), 4), 8), 12))
def cg_f043_ppne_footprint_core43_3rd_v044_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_safe_div(capex, assets), 4), 8), 12))
def cg_f043_ppne_footprint_core44_3rd_v045_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8), 12))
def cg_f043_ppne_footprint_core45_3rd_v046_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(ppnenet, 4), 4), 8), 12))
def cg_f043_ppne_footprint_core46_3rd_v047_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_pct_change(ppnenet, 4), 4), 8), 12))
def cg_f043_ppne_footprint_core47_3rd_v048_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_slope(ppnenet, 8), 4), 8), 12))
def cg_f043_ppne_footprint_core48_3rd_v049_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_z(ppnenet, 12), 4), 8), 12))
def cg_f043_ppne_footprint_core49_3rd_v050_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_mean(ppnenet, 4), 4), 8), 12))
def cg_f043_ppne_footprint_core50_3rd_v051_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core51_3rd_v052_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(capex, 4), 4), 8))
def cg_f043_ppne_footprint_core52_3rd_v053_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_safe_div(ppnenet, assets), 4), 4), 8))
def cg_f043_ppne_footprint_core53_3rd_v054_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_safe_div(capex, assets), 4), 4), 8))
def cg_f043_ppne_footprint_core54_3rd_v055_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 8))
def cg_f043_ppne_footprint_core55_3rd_v056_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_diff(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core56_3rd_v057_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_pct_change(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core57_3rd_v058_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_slope(ppnenet, 8), 4), 4), 8))
def cg_f043_ppne_footprint_core58_3rd_v059_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_z(ppnenet, 12), 4), 4), 8))
def cg_f043_ppne_footprint_core59_3rd_v060_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(_mean(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core60_3rd_v061_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core61_3rd_v062_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(capex, 4), 4), 12))
def cg_f043_ppne_footprint_core62_3rd_v063_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(ppnenet, assets), 4), 4), 12))
def cg_f043_ppne_footprint_core63_3rd_v064_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(capex, assets), 4), 4), 12))
def cg_f043_ppne_footprint_core64_3rd_v065_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 12))
def cg_f043_ppne_footprint_core65_3rd_v066_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_diff(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core66_3rd_v067_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_pct_change(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core67_3rd_v068_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_slope(ppnenet, 8), 4), 4), 12))
def cg_f043_ppne_footprint_core68_3rd_v069_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_z(ppnenet, 12), 4), 4), 12))
def cg_f043_ppne_footprint_core69_3rd_v070_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(_mean(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core70_3rd_v071_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(ppnenet, 4), 8), 12))
def cg_f043_ppne_footprint_core71_3rd_v072_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(capex, 4), 8), 12))
def cg_f043_ppne_footprint_core72_3rd_v073_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(ppnenet, assets), 4), 8), 12))
def cg_f043_ppne_footprint_core73_3rd_v074_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(capex, assets), 4), 8), 12))
def cg_f043_ppne_footprint_core74_3rd_v075_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8), 12))
def cg_f043_ppne_footprint_core75_3rd_v076_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_diff(ppnenet, 4), 4), 8), 12))
def cg_f043_ppne_footprint_core76_3rd_v077_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_pct_change(ppnenet, 4), 4), 8), 12))
def cg_f043_ppne_footprint_core77_3rd_v078_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_slope(ppnenet, 8), 4), 8), 12))
def cg_f043_ppne_footprint_core78_3rd_v079_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_z(ppnenet, 12), 4), 8), 12))
def cg_f043_ppne_footprint_core79_3rd_v080_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(_mean(ppnenet, 4), 4), 8), 12))
def cg_f043_ppne_footprint_core80_3rd_v081_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core81_3rd_v082_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(capex, 4), 4), 12))
def cg_f043_ppne_footprint_core82_3rd_v083_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(ppnenet, assets), 4), 4), 12))
def cg_f043_ppne_footprint_core83_3rd_v084_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(capex, assets), 4), 4), 12))
def cg_f043_ppne_footprint_core84_3rd_v085_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 12))
def cg_f043_ppne_footprint_core85_3rd_v086_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_diff(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core86_3rd_v087_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_pct_change(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core87_3rd_v088_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_slope(ppnenet, 8), 4), 4), 12))
def cg_f043_ppne_footprint_core88_3rd_v089_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_z(ppnenet, 12), 4), 4), 12))
def cg_f043_ppne_footprint_core89_3rd_v090_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(_mean(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core90_3rd_v091_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core91_3rd_v092_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(capex, 4), 4), 4))
def cg_f043_ppne_footprint_core92_3rd_v093_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(ppnenet, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core93_3rd_v094_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(capex, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core94_3rd_v095_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 4))
def cg_f043_ppne_footprint_core95_3rd_v096_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_diff(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core96_3rd_v097_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_pct_change(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core97_3rd_v098_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_slope(ppnenet, 8), 4), 4), 4))
def cg_f043_ppne_footprint_core98_3rd_v099_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_z(ppnenet, 12), 4), 4), 4))
def cg_f043_ppne_footprint_core99_3rd_v100_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(_mean(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core100_3rd_v101_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(ppnenet, 4), 8), 4))
def cg_f043_ppne_footprint_core101_3rd_v102_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(capex, 4), 8), 4))
def cg_f043_ppne_footprint_core102_3rd_v103_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(ppnenet, assets), 4), 8), 4))
def cg_f043_ppne_footprint_core103_3rd_v104_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(capex, assets), 4), 8), 4))
def cg_f043_ppne_footprint_core104_3rd_v105_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8), 4))
def cg_f043_ppne_footprint_core105_3rd_v106_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_diff(ppnenet, 4), 4), 8), 4))
def cg_f043_ppne_footprint_core106_3rd_v107_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_pct_change(ppnenet, 4), 4), 8), 4))
def cg_f043_ppne_footprint_core107_3rd_v108_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_slope(ppnenet, 8), 4), 8), 4))
def cg_f043_ppne_footprint_core108_3rd_v109_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_z(ppnenet, 12), 4), 8), 4))
def cg_f043_ppne_footprint_core109_3rd_v110_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(_mean(ppnenet, 4), 4), 8), 4))
def cg_f043_ppne_footprint_core110_3rd_v111_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core111_3rd_v112_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(capex, 4), 4), 4))
def cg_f043_ppne_footprint_core112_3rd_v113_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(ppnenet, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core113_3rd_v114_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(capex, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core114_3rd_v115_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 4))
def cg_f043_ppne_footprint_core115_3rd_v116_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_diff(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core116_3rd_v117_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_pct_change(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core117_3rd_v118_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_slope(ppnenet, 8), 4), 4), 4))
def cg_f043_ppne_footprint_core118_3rd_v119_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_z(ppnenet, 12), 4), 4), 4))
def cg_f043_ppne_footprint_core119_3rd_v120_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(_mean(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core120_3rd_v121_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core121_3rd_v122_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(capex, 4), 4), 4))
def cg_f043_ppne_footprint_core122_3rd_v123_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(ppnenet, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core123_3rd_v124_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(capex, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core124_3rd_v125_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 4))
def cg_f043_ppne_footprint_core125_3rd_v126_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_diff(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core126_3rd_v127_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_pct_change(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core127_3rd_v128_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_slope(ppnenet, 8), 4), 4), 4))
def cg_f043_ppne_footprint_core128_3rd_v129_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_z(ppnenet, 12), 4), 4), 4))
def cg_f043_ppne_footprint_core129_3rd_v130_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(_diff(_mean(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core130_3rd_v131_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core131_3rd_v132_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(capex, 4), 4), 4))
def cg_f043_ppne_footprint_core132_3rd_v133_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(ppnenet, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core133_3rd_v134_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(capex, assets), 4), 4), 4))
def cg_f043_ppne_footprint_core134_3rd_v135_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 4))
def cg_f043_ppne_footprint_core135_3rd_v136_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_diff(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core136_3rd_v137_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_pct_change(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core137_3rd_v138_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_slope(ppnenet, 8), 4), 4), 4))
def cg_f043_ppne_footprint_core138_3rd_v139_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_z(ppnenet, 12), 4), 4), 4))
def cg_f043_ppne_footprint_core139_3rd_v140_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(_diff(_mean(ppnenet, 4), 4), 4), 4))
def cg_f043_ppne_footprint_core140_3rd_v141_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core141_3rd_v142_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(capex, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core142_3rd_v143_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ppnenet, assets), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core143_3rd_v144_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(capex, assets), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core144_3rd_v145_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core145_3rd_v146_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_diff(ppnenet, 4), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core146_3rd_v147_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_pct_change(ppnenet, 4), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core147_3rd_v148_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_slope(ppnenet, 8), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core148_3rd_v149_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_z(ppnenet, 12), 4), 4), 4), 8))
def cg_f043_ppne_footprint_core149_3rd_v150_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(_diff(_mean(ppnenet, 4), 4), 4), 4), 8))