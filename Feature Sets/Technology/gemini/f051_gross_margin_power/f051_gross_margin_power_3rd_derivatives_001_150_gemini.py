import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f051_gross_margin_power_core00_3rd_v001_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(gp, 4), 4))
def cg_f051_gross_margin_power_core01_3rd_v002_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core02_3rd_v003_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f051_gross_margin_power_core03_3rd_v004_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_safe_div(gp, revenue), 4), 4))
def cg_f051_gross_margin_power_core04_3rd_v005_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core05_3rd_v006_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_pct_change(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core06_3rd_v007_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_slope(grossmargin, 8), 4), 4))
def cg_f051_gross_margin_power_core07_3rd_v008_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_z(grossmargin, 12), 4), 4))
def cg_f051_gross_margin_power_core08_3rd_v009_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_mean(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core09_3rd_v010_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4))
def cg_f051_gross_margin_power_core10_3rd_v011_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(gp, 4), 8))
def cg_f051_gross_margin_power_core11_3rd_v012_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(grossmargin, 4), 8))
def cg_f051_gross_margin_power_core12_3rd_v013_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f051_gross_margin_power_core13_3rd_v014_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_safe_div(gp, revenue), 4), 8))
def cg_f051_gross_margin_power_core14_3rd_v015_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core15_3rd_v016_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_pct_change(gp, 4), 4), 8))
def cg_f051_gross_margin_power_core16_3rd_v017_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_slope(grossmargin, 8), 4), 8))
def cg_f051_gross_margin_power_core17_3rd_v018_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_z(grossmargin, 12), 4), 8))
def cg_f051_gross_margin_power_core18_3rd_v019_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_mean(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core19_3rd_v020_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 8))
def cg_f051_gross_margin_power_core20_3rd_v021_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(gp, 4), 4))
def cg_f051_gross_margin_power_core21_3rd_v022_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(grossmargin, 4), 4))
def cg_f051_gross_margin_power_core22_3rd_v023_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(revenue, 4), 4))
def cg_f051_gross_margin_power_core23_3rd_v024_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_safe_div(gp, revenue), 4), 4))
def cg_f051_gross_margin_power_core24_3rd_v025_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core25_3rd_v026_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_pct_change(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core26_3rd_v027_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_slope(grossmargin, 8), 4), 4))
def cg_f051_gross_margin_power_core27_3rd_v028_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_z(grossmargin, 12), 4), 4))
def cg_f051_gross_margin_power_core28_3rd_v029_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_mean(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core29_3rd_v030_signal(gp, grossmargin, revenue):
    return _clean(_diff(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 4))
def cg_f051_gross_margin_power_core30_3rd_v031_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(gp, 4), 4), 8))
def cg_f051_gross_margin_power_core31_3rd_v032_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core32_3rd_v033_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f051_gross_margin_power_core33_3rd_v034_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_safe_div(gp, revenue), 4), 4), 8))
def cg_f051_gross_margin_power_core34_3rd_v035_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_diff(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core35_3rd_v036_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_pct_change(gp, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core36_3rd_v037_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_slope(grossmargin, 8), 4), 4), 8))
def cg_f051_gross_margin_power_core37_3rd_v038_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_z(grossmargin, 12), 4), 4), 8))
def cg_f051_gross_margin_power_core38_3rd_v039_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_mean(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core39_3rd_v040_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 8))
def cg_f051_gross_margin_power_core40_3rd_v041_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(gp, 4), 8), 12))
def cg_f051_gross_margin_power_core41_3rd_v042_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(grossmargin, 4), 8), 12))
def cg_f051_gross_margin_power_core42_3rd_v043_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f051_gross_margin_power_core43_3rd_v044_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_safe_div(gp, revenue), 4), 8), 12))
def cg_f051_gross_margin_power_core44_3rd_v045_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(grossmargin, 4), 4), 8), 12))
def cg_f051_gross_margin_power_core45_3rd_v046_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_pct_change(gp, 4), 4), 8), 12))
def cg_f051_gross_margin_power_core46_3rd_v047_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_slope(grossmargin, 8), 4), 8), 12))
def cg_f051_gross_margin_power_core47_3rd_v048_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_z(grossmargin, 12), 4), 8), 12))
def cg_f051_gross_margin_power_core48_3rd_v049_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_mean(grossmargin, 4), 4), 8), 12))
def cg_f051_gross_margin_power_core49_3rd_v050_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 8), 12))
def cg_f051_gross_margin_power_core50_3rd_v051_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(gp, 4), 4), 8))
def cg_f051_gross_margin_power_core51_3rd_v052_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(grossmargin, 4), 4), 8))
def cg_f051_gross_margin_power_core52_3rd_v053_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(revenue, 4), 4), 8))
def cg_f051_gross_margin_power_core53_3rd_v054_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_safe_div(gp, revenue), 4), 4), 8))
def cg_f051_gross_margin_power_core54_3rd_v055_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_diff(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core55_3rd_v056_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_pct_change(gp, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core56_3rd_v057_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_slope(grossmargin, 8), 4), 4), 8))
def cg_f051_gross_margin_power_core57_3rd_v058_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_z(grossmargin, 12), 4), 4), 8))
def cg_f051_gross_margin_power_core58_3rd_v059_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_mean(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core59_3rd_v060_signal(gp, grossmargin, revenue):
    return _clean(_z(_diff(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 8))
def cg_f051_gross_margin_power_core60_3rd_v061_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(gp, 4), 4), 12))
def cg_f051_gross_margin_power_core61_3rd_v062_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core62_3rd_v063_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f051_gross_margin_power_core63_3rd_v064_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_safe_div(gp, revenue), 4), 4), 12))
def cg_f051_gross_margin_power_core64_3rd_v065_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_diff(grossmargin, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core65_3rd_v066_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_pct_change(gp, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core66_3rd_v067_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_slope(grossmargin, 8), 4), 4), 12))
def cg_f051_gross_margin_power_core67_3rd_v068_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_z(grossmargin, 12), 4), 4), 12))
def cg_f051_gross_margin_power_core68_3rd_v069_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_mean(grossmargin, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core69_3rd_v070_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 12))
def cg_f051_gross_margin_power_core70_3rd_v071_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(gp, 4), 8), 12))
def cg_f051_gross_margin_power_core71_3rd_v072_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(grossmargin, 4), 8), 12))
def cg_f051_gross_margin_power_core72_3rd_v073_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(revenue, 4), 8), 12))
def cg_f051_gross_margin_power_core73_3rd_v074_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_safe_div(gp, revenue), 4), 8), 12))
def cg_f051_gross_margin_power_core74_3rd_v075_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_diff(grossmargin, 4), 4), 8), 12))
def cg_f051_gross_margin_power_core75_3rd_v076_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_pct_change(gp, 4), 4), 8), 12))
def cg_f051_gross_margin_power_core76_3rd_v077_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_slope(grossmargin, 8), 4), 8), 12))
def cg_f051_gross_margin_power_core77_3rd_v078_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_z(grossmargin, 12), 4), 8), 12))
def cg_f051_gross_margin_power_core78_3rd_v079_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_mean(grossmargin, 4), 4), 8), 12))
def cg_f051_gross_margin_power_core79_3rd_v080_signal(gp, grossmargin, revenue):
    return _clean(_rank(_slope(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 8), 12))
def cg_f051_gross_margin_power_core80_3rd_v081_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(gp, 4), 4), 12))
def cg_f051_gross_margin_power_core81_3rd_v082_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(grossmargin, 4), 4), 12))
def cg_f051_gross_margin_power_core82_3rd_v083_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(revenue, 4), 4), 12))
def cg_f051_gross_margin_power_core83_3rd_v084_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_safe_div(gp, revenue), 4), 4), 12))
def cg_f051_gross_margin_power_core84_3rd_v085_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_diff(grossmargin, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core85_3rd_v086_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_pct_change(gp, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core86_3rd_v087_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_slope(grossmargin, 8), 4), 4), 12))
def cg_f051_gross_margin_power_core87_3rd_v088_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_z(grossmargin, 12), 4), 4), 12))
def cg_f051_gross_margin_power_core88_3rd_v089_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_mean(grossmargin, 4), 4), 4), 12))
def cg_f051_gross_margin_power_core89_3rd_v090_signal(gp, grossmargin, revenue):
    return _clean(_rank(_diff(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 12))
def cg_f051_gross_margin_power_core90_3rd_v091_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core91_3rd_v092_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core92_3rd_v093_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f051_gross_margin_power_core93_3rd_v094_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4))
def cg_f051_gross_margin_power_core94_3rd_v095_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_diff(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core95_3rd_v096_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_pct_change(gp, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core96_3rd_v097_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_slope(grossmargin, 8), 4), 4), 4))
def cg_f051_gross_margin_power_core97_3rd_v098_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_z(grossmargin, 12), 4), 4), 4))
def cg_f051_gross_margin_power_core98_3rd_v099_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_mean(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core99_3rd_v100_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 4))
def cg_f051_gross_margin_power_core100_3rd_v101_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(gp, 4), 8), 4))
def cg_f051_gross_margin_power_core101_3rd_v102_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(grossmargin, 4), 8), 4))
def cg_f051_gross_margin_power_core102_3rd_v103_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(revenue, 4), 8), 4))
def cg_f051_gross_margin_power_core103_3rd_v104_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_safe_div(gp, revenue), 4), 8), 4))
def cg_f051_gross_margin_power_core104_3rd_v105_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_diff(grossmargin, 4), 4), 8), 4))
def cg_f051_gross_margin_power_core105_3rd_v106_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_pct_change(gp, 4), 4), 8), 4))
def cg_f051_gross_margin_power_core106_3rd_v107_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_slope(grossmargin, 8), 4), 8), 4))
def cg_f051_gross_margin_power_core107_3rd_v108_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_z(grossmargin, 12), 4), 8), 4))
def cg_f051_gross_margin_power_core108_3rd_v109_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_mean(grossmargin, 4), 4), 8), 4))
def cg_f051_gross_margin_power_core109_3rd_v110_signal(gp, grossmargin, revenue):
    return _clean(_mean(_slope(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 8), 4))
def cg_f051_gross_margin_power_core110_3rd_v111_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core111_3rd_v112_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core112_3rd_v113_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(revenue, 4), 4), 4))
def cg_f051_gross_margin_power_core113_3rd_v114_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_safe_div(gp, revenue), 4), 4), 4))
def cg_f051_gross_margin_power_core114_3rd_v115_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_diff(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core115_3rd_v116_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_pct_change(gp, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core116_3rd_v117_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_slope(grossmargin, 8), 4), 4), 4))
def cg_f051_gross_margin_power_core117_3rd_v118_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_z(grossmargin, 12), 4), 4), 4))
def cg_f051_gross_margin_power_core118_3rd_v119_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_mean(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core119_3rd_v120_signal(gp, grossmargin, revenue):
    return _clean(_mean(_diff(_slope(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 4))
def cg_f051_gross_margin_power_core120_3rd_v121_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core121_3rd_v122_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core122_3rd_v123_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(revenue, 4), 4), 4))
def cg_f051_gross_margin_power_core123_3rd_v124_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4))
def cg_f051_gross_margin_power_core124_3rd_v125_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_diff(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core125_3rd_v126_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_pct_change(gp, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core126_3rd_v127_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_slope(grossmargin, 8), 4), 4), 4))
def cg_f051_gross_margin_power_core127_3rd_v128_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_z(grossmargin, 12), 4), 4), 4))
def cg_f051_gross_margin_power_core128_3rd_v129_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_mean(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core129_3rd_v130_signal(gp, grossmargin, revenue):
    return _clean(_slope(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 4))
def cg_f051_gross_margin_power_core130_3rd_v131_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(gp, 4), 4), 4))
def cg_f051_gross_margin_power_core131_3rd_v132_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(grossmargin, 4), 4), 4))
def cg_f051_gross_margin_power_core132_3rd_v133_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(revenue, 4), 4), 4))
def cg_f051_gross_margin_power_core133_3rd_v134_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4))
def cg_f051_gross_margin_power_core134_3rd_v135_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_diff(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core135_3rd_v136_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_pct_change(gp, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core136_3rd_v137_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_slope(grossmargin, 8), 4), 4), 4))
def cg_f051_gross_margin_power_core137_3rd_v138_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_z(grossmargin, 12), 4), 4), 4))
def cg_f051_gross_margin_power_core138_3rd_v139_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_mean(grossmargin, 4), 4), 4), 4))
def cg_f051_gross_margin_power_core139_3rd_v140_signal(gp, grossmargin, revenue):
    return _clean(_diff(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 4))
def cg_f051_gross_margin_power_core140_3rd_v141_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(gp, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core141_3rd_v142_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(grossmargin, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core142_3rd_v143_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(revenue, 4), 4), 4), 8))
def cg_f051_gross_margin_power_core143_3rd_v144_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_safe_div(gp, revenue), 4), 4), 4), 8))
def cg_f051_gross_margin_power_core144_3rd_v145_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_diff(grossmargin, 4), 4), 4), 4), 8))
def cg_f051_gross_margin_power_core145_3rd_v146_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_pct_change(gp, 4), 4), 4), 4), 8))
def cg_f051_gross_margin_power_core146_3rd_v147_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_slope(grossmargin, 8), 4), 4), 4), 8))
def cg_f051_gross_margin_power_core147_3rd_v148_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_z(grossmargin, 12), 4), 4), 4), 8))
def cg_f051_gross_margin_power_core148_3rd_v149_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_mean(grossmargin, 4), 4), 4), 4), 8))
def cg_f051_gross_margin_power_core149_3rd_v150_signal(gp, grossmargin, revenue):
    return _clean(_z(_slope(_diff(_diff(_safe_div(gp, revenue.abs() + 1.0), 4), 4), 4), 8))