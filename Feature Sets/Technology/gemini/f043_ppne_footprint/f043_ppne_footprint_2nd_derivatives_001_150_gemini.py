import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f043_ppne_footprint_core00_2nd_v001_signal(ppnenet, capex, assets):
    return _clean(_slope(ppnenet, 4))
def cg_f043_ppne_footprint_core01_2nd_v002_signal(ppnenet, capex, assets):
    return _clean(_slope(capex, 4))
def cg_f043_ppne_footprint_core02_2nd_v003_signal(ppnenet, capex, assets):
    return _clean(_slope(_safe_div(ppnenet, assets), 4))
def cg_f043_ppne_footprint_core03_2nd_v004_signal(ppnenet, capex, assets):
    return _clean(_slope(_safe_div(capex, assets), 4))
def cg_f043_ppne_footprint_core04_2nd_v005_signal(ppnenet, capex, assets):
    return _clean(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core05_2nd_v006_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core06_2nd_v007_signal(ppnenet, capex, assets):
    return _clean(_slope(_pct_change(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core07_2nd_v008_signal(ppnenet, capex, assets):
    return _clean(_slope(_slope(ppnenet, 8), 4))
def cg_f043_ppne_footprint_core08_2nd_v009_signal(ppnenet, capex, assets):
    return _clean(_slope(_z(ppnenet, 12), 4))
def cg_f043_ppne_footprint_core09_2nd_v010_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core10_2nd_v011_signal(ppnenet, capex, assets):
    return _clean(_slope(ppnenet, 8))
def cg_f043_ppne_footprint_core11_2nd_v012_signal(ppnenet, capex, assets):
    return _clean(_slope(capex, 8))
def cg_f043_ppne_footprint_core12_2nd_v013_signal(ppnenet, capex, assets):
    return _clean(_slope(_safe_div(ppnenet, assets), 8))
def cg_f043_ppne_footprint_core13_2nd_v014_signal(ppnenet, capex, assets):
    return _clean(_slope(_safe_div(capex, assets), 8))
def cg_f043_ppne_footprint_core14_2nd_v015_signal(ppnenet, capex, assets):
    return _clean(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 8))
def cg_f043_ppne_footprint_core15_2nd_v016_signal(ppnenet, capex, assets):
    return _clean(_slope(_diff(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core16_2nd_v017_signal(ppnenet, capex, assets):
    return _clean(_slope(_pct_change(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core17_2nd_v018_signal(ppnenet, capex, assets):
    return _clean(_slope(_slope(ppnenet, 8), 8))
def cg_f043_ppne_footprint_core18_2nd_v019_signal(ppnenet, capex, assets):
    return _clean(_slope(_z(ppnenet, 12), 8))
def cg_f043_ppne_footprint_core19_2nd_v020_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core20_2nd_v021_signal(ppnenet, capex, assets):
    return _clean(_diff(ppnenet, 4))
def cg_f043_ppne_footprint_core21_2nd_v022_signal(ppnenet, capex, assets):
    return _clean(_diff(capex, 4))
def cg_f043_ppne_footprint_core22_2nd_v023_signal(ppnenet, capex, assets):
    return _clean(_diff(_safe_div(ppnenet, assets), 4))
def cg_f043_ppne_footprint_core23_2nd_v024_signal(ppnenet, capex, assets):
    return _clean(_diff(_safe_div(capex, assets), 4))
def cg_f043_ppne_footprint_core24_2nd_v025_signal(ppnenet, capex, assets):
    return _clean(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4))
def cg_f043_ppne_footprint_core25_2nd_v026_signal(ppnenet, capex, assets):
    return _clean(_diff(_diff(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core26_2nd_v027_signal(ppnenet, capex, assets):
    return _clean(_diff(_pct_change(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core27_2nd_v028_signal(ppnenet, capex, assets):
    return _clean(_diff(_slope(ppnenet, 8), 4))
def cg_f043_ppne_footprint_core28_2nd_v029_signal(ppnenet, capex, assets):
    return _clean(_diff(_z(ppnenet, 12), 4))
def cg_f043_ppne_footprint_core29_2nd_v030_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core30_2nd_v031_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core31_2nd_v032_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(capex, 4), 8))
def cg_f043_ppne_footprint_core32_2nd_v033_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_safe_div(ppnenet, assets), 4), 8))
def cg_f043_ppne_footprint_core33_2nd_v034_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_safe_div(capex, assets), 4), 8))
def cg_f043_ppne_footprint_core34_2nd_v035_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8))
def cg_f043_ppne_footprint_core35_2nd_v036_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core36_2nd_v037_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_pct_change(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core37_2nd_v038_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_slope(ppnenet, 8), 4), 8))
def cg_f043_ppne_footprint_core38_2nd_v039_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_z(ppnenet, 12), 4), 8))
def cg_f043_ppne_footprint_core39_2nd_v040_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_mean(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core40_2nd_v041_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(ppnenet, 8), 12))
def cg_f043_ppne_footprint_core41_2nd_v042_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(capex, 8), 12))
def cg_f043_ppne_footprint_core42_2nd_v043_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_safe_div(ppnenet, assets), 8), 12))
def cg_f043_ppne_footprint_core43_2nd_v044_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_safe_div(capex, assets), 8), 12))
def cg_f043_ppne_footprint_core44_2nd_v045_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 8), 12))
def cg_f043_ppne_footprint_core45_2nd_v046_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_diff(ppnenet, 4), 8), 12))
def cg_f043_ppne_footprint_core46_2nd_v047_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_pct_change(ppnenet, 4), 8), 12))
def cg_f043_ppne_footprint_core47_2nd_v048_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_slope(ppnenet, 8), 8), 12))
def cg_f043_ppne_footprint_core48_2nd_v049_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_z(ppnenet, 12), 8), 12))
def cg_f043_ppne_footprint_core49_2nd_v050_signal(ppnenet, capex, assets):
    return _clean(_z(_slope(_mean(ppnenet, 4), 8), 12))
def cg_f043_ppne_footprint_core50_2nd_v051_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(ppnenet, 4), 8))
def cg_f043_ppne_footprint_core51_2nd_v052_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(capex, 4), 8))
def cg_f043_ppne_footprint_core52_2nd_v053_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_safe_div(ppnenet, assets), 4), 8))
def cg_f043_ppne_footprint_core53_2nd_v054_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_safe_div(capex, assets), 4), 8))
def cg_f043_ppne_footprint_core54_2nd_v055_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 8))
def cg_f043_ppne_footprint_core55_2nd_v056_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_diff(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core56_2nd_v057_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_pct_change(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core57_2nd_v058_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_slope(ppnenet, 8), 4), 8))
def cg_f043_ppne_footprint_core58_2nd_v059_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_z(ppnenet, 12), 4), 8))
def cg_f043_ppne_footprint_core59_2nd_v060_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core60_2nd_v061_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(ppnenet, 4), 12))
def cg_f043_ppne_footprint_core61_2nd_v062_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(capex, 4), 12))
def cg_f043_ppne_footprint_core62_2nd_v063_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_safe_div(ppnenet, assets), 4), 12))
def cg_f043_ppne_footprint_core63_2nd_v064_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_safe_div(capex, assets), 4), 12))
def cg_f043_ppne_footprint_core64_2nd_v065_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 12))
def cg_f043_ppne_footprint_core65_2nd_v066_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_diff(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core66_2nd_v067_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_pct_change(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core67_2nd_v068_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_slope(ppnenet, 8), 4), 12))
def cg_f043_ppne_footprint_core68_2nd_v069_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_z(ppnenet, 12), 4), 12))
def cg_f043_ppne_footprint_core69_2nd_v070_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core70_2nd_v071_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(ppnenet, 4), 12))
def cg_f043_ppne_footprint_core71_2nd_v072_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(capex, 4), 12))
def cg_f043_ppne_footprint_core72_2nd_v073_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_safe_div(ppnenet, assets), 4), 12))
def cg_f043_ppne_footprint_core73_2nd_v074_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_safe_div(capex, assets), 4), 12))
def cg_f043_ppne_footprint_core74_2nd_v075_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 12))
def cg_f043_ppne_footprint_core75_2nd_v076_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_diff(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core76_2nd_v077_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_pct_change(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core77_2nd_v078_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_slope(ppnenet, 8), 4), 12))
def cg_f043_ppne_footprint_core78_2nd_v079_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_z(ppnenet, 12), 4), 12))
def cg_f043_ppne_footprint_core79_2nd_v080_signal(ppnenet, capex, assets):
    return _clean(_rank(_diff(_mean(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core80_2nd_v081_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core81_2nd_v082_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(capex, 4), 4))
def cg_f043_ppne_footprint_core82_2nd_v083_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_safe_div(ppnenet, assets), 4), 4))
def cg_f043_ppne_footprint_core83_2nd_v084_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_safe_div(capex, assets), 4), 4))
def cg_f043_ppne_footprint_core84_2nd_v085_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f043_ppne_footprint_core85_2nd_v086_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core86_2nd_v087_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_pct_change(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core87_2nd_v088_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_slope(ppnenet, 8), 4), 4))
def cg_f043_ppne_footprint_core88_2nd_v089_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_z(ppnenet, 12), 4), 4))
def cg_f043_ppne_footprint_core89_2nd_v090_signal(ppnenet, capex, assets):
    return _clean(_mean(_slope(_mean(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core90_2nd_v091_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core91_2nd_v092_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(capex, 4), 4))
def cg_f043_ppne_footprint_core92_2nd_v093_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_safe_div(ppnenet, assets), 4), 4))
def cg_f043_ppne_footprint_core93_2nd_v094_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_safe_div(capex, assets), 4), 4))
def cg_f043_ppne_footprint_core94_2nd_v095_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f043_ppne_footprint_core95_2nd_v096_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core96_2nd_v097_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_pct_change(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core97_2nd_v098_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_slope(ppnenet, 8), 4), 4))
def cg_f043_ppne_footprint_core98_2nd_v099_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_z(ppnenet, 12), 4), 4))
def cg_f043_ppne_footprint_core99_2nd_v100_signal(ppnenet, capex, assets):
    return _clean(_mean(_diff(_mean(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core100_2nd_v101_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core101_2nd_v102_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(capex, 4), 4))
def cg_f043_ppne_footprint_core102_2nd_v103_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_safe_div(ppnenet, assets), 4), 4))
def cg_f043_ppne_footprint_core103_2nd_v104_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_safe_div(capex, assets), 4), 4))
def cg_f043_ppne_footprint_core104_2nd_v105_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f043_ppne_footprint_core105_2nd_v106_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core106_2nd_v107_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_pct_change(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core107_2nd_v108_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_slope(ppnenet, 8), 4), 4))
def cg_f043_ppne_footprint_core108_2nd_v109_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_z(ppnenet, 12), 4), 4))
def cg_f043_ppne_footprint_core109_2nd_v110_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_mean(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core110_2nd_v111_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(ppnenet, 8), 8))
def cg_f043_ppne_footprint_core111_2nd_v112_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(capex, 8), 8))
def cg_f043_ppne_footprint_core112_2nd_v113_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_safe_div(ppnenet, assets), 8), 8))
def cg_f043_ppne_footprint_core113_2nd_v114_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_safe_div(capex, assets), 8), 8))
def cg_f043_ppne_footprint_core114_2nd_v115_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 8), 8))
def cg_f043_ppne_footprint_core115_2nd_v116_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_diff(ppnenet, 4), 8), 8))
def cg_f043_ppne_footprint_core116_2nd_v117_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_pct_change(ppnenet, 4), 8), 8))
def cg_f043_ppne_footprint_core117_2nd_v118_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_slope(ppnenet, 8), 8), 8))
def cg_f043_ppne_footprint_core118_2nd_v119_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_z(ppnenet, 12), 8), 8))
def cg_f043_ppne_footprint_core119_2nd_v120_signal(ppnenet, capex, assets):
    return _clean(_slope(_mean(_mean(ppnenet, 4), 8), 8))
def cg_f043_ppne_footprint_core120_2nd_v121_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(ppnenet, 4), 4))
def cg_f043_ppne_footprint_core121_2nd_v122_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(capex, 4), 4))
def cg_f043_ppne_footprint_core122_2nd_v123_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_safe_div(ppnenet, assets), 4), 4))
def cg_f043_ppne_footprint_core123_2nd_v124_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_safe_div(capex, assets), 4), 4))
def cg_f043_ppne_footprint_core124_2nd_v125_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4))
def cg_f043_ppne_footprint_core125_2nd_v126_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_diff(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core126_2nd_v127_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_pct_change(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core127_2nd_v128_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_slope(ppnenet, 8), 4), 4))
def cg_f043_ppne_footprint_core128_2nd_v129_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_z(ppnenet, 12), 4), 4))
def cg_f043_ppne_footprint_core129_2nd_v130_signal(ppnenet, capex, assets):
    return _clean(_diff(_mean(_mean(ppnenet, 4), 4), 4))
def cg_f043_ppne_footprint_core130_2nd_v131_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(ppnenet, 4), 4), 8))
def cg_f043_ppne_footprint_core131_2nd_v132_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(capex, 4), 4), 8))
def cg_f043_ppne_footprint_core132_2nd_v133_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_safe_div(ppnenet, assets), 4), 4), 8))
def cg_f043_ppne_footprint_core133_2nd_v134_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_safe_div(capex, assets), 4), 4), 8))
def cg_f043_ppne_footprint_core134_2nd_v135_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 8))
def cg_f043_ppne_footprint_core135_2nd_v136_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_diff(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core136_2nd_v137_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_pct_change(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core137_2nd_v138_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_slope(ppnenet, 8), 4), 4), 8))
def cg_f043_ppne_footprint_core138_2nd_v139_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_z(ppnenet, 12), 4), 4), 8))
def cg_f043_ppne_footprint_core139_2nd_v140_signal(ppnenet, capex, assets):
    return _clean(_z(_diff(_mean(_mean(ppnenet, 4), 4), 4), 8))
def cg_f043_ppne_footprint_core140_2nd_v141_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(ppnenet, 4), 4), 12))
def cg_f043_ppne_footprint_core141_2nd_v142_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(capex, 4), 4), 12))
def cg_f043_ppne_footprint_core142_2nd_v143_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(ppnenet, assets), 4), 4), 12))
def cg_f043_ppne_footprint_core143_2nd_v144_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(capex, assets), 4), 4), 12))
def cg_f043_ppne_footprint_core144_2nd_v145_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_safe_div(capex, ppnenet.abs() + 1.0), 4), 4), 12))
def cg_f043_ppne_footprint_core145_2nd_v146_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_diff(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core146_2nd_v147_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_pct_change(ppnenet, 4), 4), 4), 12))
def cg_f043_ppne_footprint_core147_2nd_v148_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_slope(ppnenet, 8), 4), 4), 12))
def cg_f043_ppne_footprint_core148_2nd_v149_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_z(ppnenet, 12), 4), 4), 12))
def cg_f043_ppne_footprint_core149_2nd_v150_signal(ppnenet, capex, assets):
    return _clean(_rank(_slope(_mean(_mean(ppnenet, 4), 4), 4), 12))