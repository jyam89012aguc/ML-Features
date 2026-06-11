import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f051_gross_margin_power_core00_2nd_v001_signal(gp, grossmargin, revenue):
    return _clean(_slope(gp, 4))
def cg_f051_gross_margin_power_core01_2nd_v002_signal(gp, grossmargin, revenue):
    return _clean(_slope(grossmargin, 4))
def cg_f051_gross_margin_power_core02_2nd_v003_signal(gp, grossmargin, revenue):
    return _clean(_slope(revenue, 4))
def cg_f051_gross_margin_power_core03_2nd_v004_signal(gp, grossmargin, revenue):
    return _clean(_slope(_safe_div(gp, revenue), 4))
def cg_f051_gross_margin_power_core04_2nd_v005_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core05_2nd_v006_signal(gp, grossmargin, revenue):
    return _clean(_slope(_pct_change(gp, 4), 4))
def cg_f051_gross_margin_power_core06_2nd_v007_signal(gp, grossmargin, revenue):
    return _clean(_slope(_slope(grossmargin, 8), 4))
def cg_f051_gross_margin_power_core07_2nd_v008_signal(gp, grossmargin, revenue):
    return _clean(_slope(_z(grossmargin, 12), 4))
def cg_f051_gross_margin_power_core08_2nd_v009_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core09_2nd_v010_signal(gp, grossmargin, revenue):
    return _clean(_slope(_safe_div(gp, revenue.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core10_2nd_v011_signal(gp, grossmargin, revenue):
    return _clean(_slope(gp, 8))
def cg_f051_gross_margin_power_core11_2nd_v012_signal(gp, grossmargin, revenue):
    return _clean(_slope(grossmargin, 8))
def cg_f051_gross_margin_power_core12_2nd_v013_signal(gp, grossmargin, revenue):
    return _clean(_slope(revenue, 8))
def cg_f051_gross_margin_power_core13_2nd_v014_signal(gp, grossmargin, revenue):
    return _clean(_slope(_safe_div(gp, revenue), 8))
def cg_f051_gross_margin_power_core14_2nd_v015_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core15_2nd_v016_signal(gp, grossmargin, revenue):
    return _clean(_slope(_pct_change(gp, 4), 8))
def cg_f051_gross_margin_power_core16_2nd_v017_signal(gp, grossmargin, revenue):
    return _clean(_slope(_slope(grossmargin, 8), 8))
def cg_f051_gross_margin_power_core17_2nd_v018_signal(gp, grossmargin, revenue):
    return _clean(_slope(_z(grossmargin, 12), 8))
def cg_f051_gross_margin_power_core18_2nd_v019_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core19_2nd_v020_signal(gp, grossmargin, revenue):
    return _clean(_slope(_safe_div(gp, revenue.abs() + 1.0), 8))
def cg_f051_gross_margin_power_core20_2nd_v021_signal(gp, grossmargin, revenue):
    return _clean(_diff(gp, 4))
def cg_f051_gross_margin_power_core21_2nd_v022_signal(gp, grossmargin, revenue):
    return _clean(_diff(grossmargin, 4))
def cg_f051_gross_margin_power_core22_2nd_v023_signal(gp, grossmargin, revenue):
    return _clean(_diff(revenue, 4))
def cg_f051_gross_margin_power_core23_2nd_v024_signal(gp, grossmargin, revenue):
    return _clean(_diff(_safe_div(gp, revenue), 4))
def cg_f051_gross_margin_power_core24_2nd_v025_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core25_2nd_v026_signal(gp, grossmargin, revenue):
    return _clean(_diff(_pct_change(gp, 4), 4))
def cg_f051_gross_margin_power_core26_2nd_v027_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(grossmargin, 8), 4))
def cg_f051_gross_margin_power_core27_2nd_v028_signal(gp, grossmargin, revenue):
    return _clean(_diff(_z(grossmargin, 12), 4))
def cg_f051_gross_margin_power_core28_2nd_v029_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core29_2nd_v030_signal(gp, grossmargin, revenue):
    return _clean(_diff(_safe_div(gp, revenue.abs() + 1.0), 4))
def cg_f051_gross_margin_power_core30_2nd_v031_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(gp, 4), 8))
def cg_f051_gross_margin_power_core31_2nd_v032_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core32_2nd_v033_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f051_gross_margin_power_core33_2nd_v034_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_safe_div(gp, revenue), 4), 8))
def cg_f051_gross_margin_power_core34_2nd_v035_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core35_2nd_v036_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_pct_change(gp, 4), 4), 8))
def cg_f051_gross_margin_power_core36_2nd_v037_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_slope(grossmargin, 8), 4), 8))
def cg_f051_gross_margin_power_core37_2nd_v038_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_z(grossmargin, 12), 4), 8))
def cg_f051_gross_margin_power_core38_2nd_v039_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_mean(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core39_2nd_v040_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 8))
def cg_f051_gross_margin_power_core40_2nd_v041_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(gp, 8), 12))
def cg_f051_gross_margin_power_core41_2nd_v042_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(grossmargin, 8), 12))
def cg_f051_gross_margin_power_core42_2nd_v043_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f051_gross_margin_power_core43_2nd_v044_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_safe_div(gp, revenue), 8), 12))
def cg_f051_gross_margin_power_core44_2nd_v045_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(grossmargin, 4), 8), 12))
def cg_f051_gross_margin_power_core45_2nd_v046_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_pct_change(gp, 4), 8), 12))
def cg_f051_gross_margin_power_core46_2nd_v047_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_slope(grossmargin, 8), 8), 12))
def cg_f051_gross_margin_power_core47_2nd_v048_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_z(grossmargin, 12), 8), 12))
def cg_f051_gross_margin_power_core48_2nd_v049_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_mean(grossmargin, 4), 8), 12))
def cg_f051_gross_margin_power_core49_2nd_v050_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_safe_div(gp, revenue.abs() + 1.0), 8), 12))
def cg_f051_gross_margin_power_core50_2nd_v051_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(gp, 4), 8))
def cg_f051_gross_margin_power_core51_2nd_v052_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core52_2nd_v053_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f051_gross_margin_power_core53_2nd_v054_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_safe_div(gp, revenue), 4), 8))
def cg_f051_gross_margin_power_core54_2nd_v055_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core55_2nd_v056_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_pct_change(gp, 4), 4), 8))
def cg_f051_gross_margin_power_core56_2nd_v057_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(grossmargin, 8), 4), 8))
def cg_f051_gross_margin_power_core57_2nd_v058_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_z(grossmargin, 12), 4), 8))
def cg_f051_gross_margin_power_core58_2nd_v059_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core59_2nd_v060_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 8))
def cg_f051_gross_margin_power_core60_2nd_v061_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(gp, 4), 12))
def cg_f051_gross_margin_power_core61_2nd_v062_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(grossmargin, 4), 12))
def cg_f051_gross_margin_power_core62_2nd_v063_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f051_gross_margin_power_core63_2nd_v064_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_safe_div(gp, revenue), 4), 12))
def cg_f051_gross_margin_power_core64_2nd_v065_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core65_2nd_v066_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_pct_change(gp, 4), 4), 12))
def cg_f051_gross_margin_power_core66_2nd_v067_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_slope(grossmargin, 8), 4), 12))
def cg_f051_gross_margin_power_core67_2nd_v068_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_z(grossmargin, 12), 4), 12))
def cg_f051_gross_margin_power_core68_2nd_v069_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core69_2nd_v070_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 12))
def cg_f051_gross_margin_power_core70_2nd_v071_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(gp, 4), 12))
def cg_f051_gross_margin_power_core71_2nd_v072_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(grossmargin, 4), 12))
def cg_f051_gross_margin_power_core72_2nd_v073_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f051_gross_margin_power_core73_2nd_v074_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_safe_div(gp, revenue), 4), 12))
def cg_f051_gross_margin_power_core74_2nd_v075_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core75_2nd_v076_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_pct_change(gp, 4), 4), 12))
def cg_f051_gross_margin_power_core76_2nd_v077_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(grossmargin, 8), 4), 12))
def cg_f051_gross_margin_power_core77_2nd_v078_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_z(grossmargin, 12), 4), 12))
def cg_f051_gross_margin_power_core78_2nd_v079_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_mean(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core79_2nd_v080_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 12))
def cg_f051_gross_margin_power_core80_2nd_v081_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(gp, 4), 4))
def cg_f051_gross_margin_power_core81_2nd_v082_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core82_2nd_v083_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f051_gross_margin_power_core83_2nd_v084_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_safe_div(gp, revenue), 4), 4))
def cg_f051_gross_margin_power_core84_2nd_v085_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core85_2nd_v086_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_pct_change(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core86_2nd_v087_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_slope(grossmargin, 8), 4), 4))
def cg_f051_gross_margin_power_core87_2nd_v088_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_z(grossmargin, 12), 4), 4))
def cg_f051_gross_margin_power_core88_2nd_v089_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_mean(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core89_2nd_v090_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 4))
def cg_f051_gross_margin_power_core90_2nd_v091_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(gp, 4), 4))
def cg_f051_gross_margin_power_core91_2nd_v092_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core92_2nd_v093_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f051_gross_margin_power_core93_2nd_v094_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_safe_div(gp, revenue), 4), 4))
def cg_f051_gross_margin_power_core94_2nd_v095_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core95_2nd_v096_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_pct_change(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core96_2nd_v097_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(grossmargin, 8), 4), 4))
def cg_f051_gross_margin_power_core97_2nd_v098_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_z(grossmargin, 12), 4), 4))
def cg_f051_gross_margin_power_core98_2nd_v099_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_mean(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core99_2nd_v100_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4))
def cg_f051_gross_margin_power_core100_2nd_v101_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(gp, 4), 4))
def cg_f051_gross_margin_power_core101_2nd_v102_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core102_2nd_v103_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f051_gross_margin_power_core103_2nd_v104_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_safe_div(gp, revenue), 4), 4))
def cg_f051_gross_margin_power_core104_2nd_v105_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core105_2nd_v106_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_pct_change(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core106_2nd_v107_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_slope(grossmargin, 8), 4), 4))
def cg_f051_gross_margin_power_core107_2nd_v108_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_z(grossmargin, 12), 4), 4))
def cg_f051_gross_margin_power_core108_2nd_v109_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_mean(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core109_2nd_v110_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_safe_div(gp, revenue.abs() + 1.0), 4), 4))
def cg_f051_gross_margin_power_core110_2nd_v111_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(gp, 8), 8))
def cg_f051_gross_margin_power_core111_2nd_v112_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(grossmargin, 8), 8))
def cg_f051_gross_margin_power_core112_2nd_v113_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f051_gross_margin_power_core113_2nd_v114_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_safe_div(gp, revenue), 8), 8))
def cg_f051_gross_margin_power_core114_2nd_v115_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_diff(grossmargin, 4), 8), 8))
def cg_f051_gross_margin_power_core115_2nd_v116_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_pct_change(gp, 4), 8), 8))
def cg_f051_gross_margin_power_core116_2nd_v117_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_slope(grossmargin, 8), 8), 8))
def cg_f051_gross_margin_power_core117_2nd_v118_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_z(grossmargin, 12), 8), 8))
def cg_f051_gross_margin_power_core118_2nd_v119_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_mean(grossmargin, 4), 8), 8))
def cg_f051_gross_margin_power_core119_2nd_v120_signal(gp, grossmargin, revenue):
    return _clean(_slope(_mean(_safe_div(gp, revenue.abs() + 1.0), 8), 8))
def cg_f051_gross_margin_power_core120_2nd_v121_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(gp, 4), 4))
def cg_f051_gross_margin_power_core121_2nd_v122_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core122_2nd_v123_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f051_gross_margin_power_core123_2nd_v124_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_safe_div(gp, revenue), 4), 4))
def cg_f051_gross_margin_power_core124_2nd_v125_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core125_2nd_v126_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_pct_change(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core126_2nd_v127_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_slope(grossmargin, 8), 4), 4))
def cg_f051_gross_margin_power_core127_2nd_v128_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_z(grossmargin, 12), 4), 4))
def cg_f051_gross_margin_power_core128_2nd_v129_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_mean(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core129_2nd_v130_signal(gp, grossmargin, revenue):
    return _clean(_diff(_mean(_safe_div(gp, revenue.abs() + 1.0), 4), 4))
def cg_f051_gross_margin_power_core130_2nd_v131_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(gp, 4), 4), 8))
def cg_f051_gross_margin_power_core131_2nd_v132_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core132_2nd_v133_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f051_gross_margin_power_core133_2nd_v134_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_safe_div(gp, revenue), 4), 4), 8))
def cg_f051_gross_margin_power_core134_2nd_v135_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_diff(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core135_2nd_v136_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_pct_change(gp, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core136_2nd_v137_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_slope(grossmargin, 8), 4), 4), 8))
def cg_f051_gross_margin_power_core137_2nd_v138_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_z(grossmargin, 12), 4), 4), 8))
def cg_f051_gross_margin_power_core138_2nd_v139_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_mean(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core139_2nd_v140_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_mean(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 8))
def cg_f051_gross_margin_power_core140_2nd_v141_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(gp, 4), 4), 12))
def cg_f051_gross_margin_power_core141_2nd_v142_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core142_2nd_v143_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f051_gross_margin_power_core143_2nd_v144_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(gp, revenue), 4), 4), 12))
def cg_f051_gross_margin_power_core144_2nd_v145_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_diff(grossmargin, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core145_2nd_v146_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_pct_change(gp, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core146_2nd_v147_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_slope(grossmargin, 8), 4), 4), 12))
def cg_f051_gross_margin_power_core147_2nd_v148_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_z(grossmargin, 12), 4), 4), 12))
def cg_f051_gross_margin_power_core148_2nd_v149_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_mean(grossmargin, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core149_2nd_v150_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_mean(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 12))