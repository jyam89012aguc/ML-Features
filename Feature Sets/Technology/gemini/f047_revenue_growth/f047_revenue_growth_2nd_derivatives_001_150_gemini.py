import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f047_revenue_growth_core00_2nd_v001_signal(revenue, revenueusd):
    return _clean(_slope(revenue, 4))
def cg_f047_revenue_growth_core01_2nd_v002_signal(revenue, revenueusd):
    return _clean(_slope(revenueusd, 4))
def cg_f047_revenue_growth_core02_2nd_v003_signal(revenue, revenueusd):
    return _clean(_slope(_pct_change(revenue, 4), 4))
def cg_f047_revenue_growth_core03_2nd_v004_signal(revenue, revenueusd):
    return _clean(_slope(_pct_change(revenueusd, 4), 4))
def cg_f047_revenue_growth_core04_2nd_v005_signal(revenue, revenueusd):
    return _clean(_slope(_diff(revenue, 4), 4))
def cg_f047_revenue_growth_core05_2nd_v006_signal(revenue, revenueusd):
    return _clean(_slope(_diff(revenueusd, 4), 4))
def cg_f047_revenue_growth_core06_2nd_v007_signal(revenue, revenueusd):
    return _clean(_slope(_slope(revenue, 8), 4))
def cg_f047_revenue_growth_core07_2nd_v008_signal(revenue, revenueusd):
    return _clean(_slope(_z(revenue, 12), 4))
def cg_f047_revenue_growth_core08_2nd_v009_signal(revenue, revenueusd):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f047_revenue_growth_core09_2nd_v010_signal(revenue, revenueusd):
    return _clean(_slope(_safe_div(revenue, revenueusd), 4))
def cg_f047_revenue_growth_core10_2nd_v011_signal(revenue, revenueusd):
    return _clean(_slope(revenue, 8))
def cg_f047_revenue_growth_core11_2nd_v012_signal(revenue, revenueusd):
    return _clean(_slope(revenueusd, 8))
def cg_f047_revenue_growth_core12_2nd_v013_signal(revenue, revenueusd):
    return _clean(_slope(_pct_change(revenue, 4), 8))
def cg_f047_revenue_growth_core13_2nd_v014_signal(revenue, revenueusd):
    return _clean(_slope(_pct_change(revenueusd, 4), 8))
def cg_f047_revenue_growth_core14_2nd_v015_signal(revenue, revenueusd):
    return _clean(_slope(_diff(revenue, 4), 8))
def cg_f047_revenue_growth_core15_2nd_v016_signal(revenue, revenueusd):
    return _clean(_slope(_diff(revenueusd, 4), 8))
def cg_f047_revenue_growth_core16_2nd_v017_signal(revenue, revenueusd):
    return _clean(_slope(_slope(revenue, 8), 8))
def cg_f047_revenue_growth_core17_2nd_v018_signal(revenue, revenueusd):
    return _clean(_slope(_z(revenue, 12), 8))
def cg_f047_revenue_growth_core18_2nd_v019_signal(revenue, revenueusd):
    return _clean(_slope(_mean(revenue, 4), 8))
def cg_f047_revenue_growth_core19_2nd_v020_signal(revenue, revenueusd):
    return _clean(_slope(_safe_div(revenue, revenueusd), 8))
def cg_f047_revenue_growth_core20_2nd_v021_signal(revenue, revenueusd):
    return _clean(_diff(revenue, 4))
def cg_f047_revenue_growth_core21_2nd_v022_signal(revenue, revenueusd):
    return _clean(_diff(revenueusd, 4))
def cg_f047_revenue_growth_core22_2nd_v023_signal(revenue, revenueusd):
    return _clean(_diff(_pct_change(revenue, 4), 4))
def cg_f047_revenue_growth_core23_2nd_v024_signal(revenue, revenueusd):
    return _clean(_diff(_pct_change(revenueusd, 4), 4))
def cg_f047_revenue_growth_core24_2nd_v025_signal(revenue, revenueusd):
    return _clean(_diff(_diff(revenue, 4), 4))
def cg_f047_revenue_growth_core25_2nd_v026_signal(revenue, revenueusd):
    return _clean(_diff(_diff(revenueusd, 4), 4))
def cg_f047_revenue_growth_core26_2nd_v027_signal(revenue, revenueusd):
    return _clean(_diff(_slope(revenue, 8), 4))
def cg_f047_revenue_growth_core27_2nd_v028_signal(revenue, revenueusd):
    return _clean(_diff(_z(revenue, 12), 4))
def cg_f047_revenue_growth_core28_2nd_v029_signal(revenue, revenueusd):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f047_revenue_growth_core29_2nd_v030_signal(revenue, revenueusd):
    return _clean(_diff(_safe_div(revenue, revenueusd), 4))
def cg_f047_revenue_growth_core30_2nd_v031_signal(revenue, revenueusd):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f047_revenue_growth_core31_2nd_v032_signal(revenue, revenueusd):
    return _clean(_z(_slope(revenueusd, 4), 8))
def cg_f047_revenue_growth_core32_2nd_v033_signal(revenue, revenueusd):
    return _clean(_z(_slope(_pct_change(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core33_2nd_v034_signal(revenue, revenueusd):
    return _clean(_z(_slope(_pct_change(revenueusd, 4), 4), 8))
def cg_f047_revenue_growth_core34_2nd_v035_signal(revenue, revenueusd):
    return _clean(_z(_slope(_diff(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core35_2nd_v036_signal(revenue, revenueusd):
    return _clean(_z(_slope(_diff(revenueusd, 4), 4), 8))
def cg_f047_revenue_growth_core36_2nd_v037_signal(revenue, revenueusd):
    return _clean(_z(_slope(_slope(revenue, 8), 4), 8))
def cg_f047_revenue_growth_core37_2nd_v038_signal(revenue, revenueusd):
    return _clean(_z(_slope(_z(revenue, 12), 4), 8))
def cg_f047_revenue_growth_core38_2nd_v039_signal(revenue, revenueusd):
    return _clean(_z(_slope(_mean(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core39_2nd_v040_signal(revenue, revenueusd):
    return _clean(_z(_slope(_safe_div(revenue, revenueusd), 4), 8))
def cg_f047_revenue_growth_core40_2nd_v041_signal(revenue, revenueusd):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f047_revenue_growth_core41_2nd_v042_signal(revenue, revenueusd):
    return _clean(_z(_slope(revenueusd, 8), 12))
def cg_f047_revenue_growth_core42_2nd_v043_signal(revenue, revenueusd):
    return _clean(_z(_slope(_pct_change(revenue, 4), 8), 12))
def cg_f047_revenue_growth_core43_2nd_v044_signal(revenue, revenueusd):
    return _clean(_z(_slope(_pct_change(revenueusd, 4), 8), 12))
def cg_f047_revenue_growth_core44_2nd_v045_signal(revenue, revenueusd):
    return _clean(_z(_slope(_diff(revenue, 4), 8), 12))
def cg_f047_revenue_growth_core45_2nd_v046_signal(revenue, revenueusd):
    return _clean(_z(_slope(_diff(revenueusd, 4), 8), 12))
def cg_f047_revenue_growth_core46_2nd_v047_signal(revenue, revenueusd):
    return _clean(_z(_slope(_slope(revenue, 8), 8), 12))
def cg_f047_revenue_growth_core47_2nd_v048_signal(revenue, revenueusd):
    return _clean(_z(_slope(_z(revenue, 12), 8), 12))
def cg_f047_revenue_growth_core48_2nd_v049_signal(revenue, revenueusd):
    return _clean(_z(_slope(_mean(revenue, 4), 8), 12))
def cg_f047_revenue_growth_core49_2nd_v050_signal(revenue, revenueusd):
    return _clean(_z(_slope(_safe_div(revenue, revenueusd), 8), 12))
def cg_f047_revenue_growth_core50_2nd_v051_signal(revenue, revenueusd):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f047_revenue_growth_core51_2nd_v052_signal(revenue, revenueusd):
    return _clean(_z(_diff(revenueusd, 4), 8))
def cg_f047_revenue_growth_core52_2nd_v053_signal(revenue, revenueusd):
    return _clean(_z(_diff(_pct_change(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core53_2nd_v054_signal(revenue, revenueusd):
    return _clean(_z(_diff(_pct_change(revenueusd, 4), 4), 8))
def cg_f047_revenue_growth_core54_2nd_v055_signal(revenue, revenueusd):
    return _clean(_z(_diff(_diff(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core55_2nd_v056_signal(revenue, revenueusd):
    return _clean(_z(_diff(_diff(revenueusd, 4), 4), 8))
def cg_f047_revenue_growth_core56_2nd_v057_signal(revenue, revenueusd):
    return _clean(_z(_diff(_slope(revenue, 8), 4), 8))
def cg_f047_revenue_growth_core57_2nd_v058_signal(revenue, revenueusd):
    return _clean(_z(_diff(_z(revenue, 12), 4), 8))
def cg_f047_revenue_growth_core58_2nd_v059_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core59_2nd_v060_signal(revenue, revenueusd):
    return _clean(_z(_diff(_safe_div(revenue, revenueusd), 4), 8))
def cg_f047_revenue_growth_core60_2nd_v061_signal(revenue, revenueusd):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f047_revenue_growth_core61_2nd_v062_signal(revenue, revenueusd):
    return _clean(_rank(_slope(revenueusd, 4), 12))
def cg_f047_revenue_growth_core62_2nd_v063_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_pct_change(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core63_2nd_v064_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_pct_change(revenueusd, 4), 4), 12))
def cg_f047_revenue_growth_core64_2nd_v065_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_diff(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core65_2nd_v066_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_diff(revenueusd, 4), 4), 12))
def cg_f047_revenue_growth_core66_2nd_v067_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_slope(revenue, 8), 4), 12))
def cg_f047_revenue_growth_core67_2nd_v068_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_z(revenue, 12), 4), 12))
def cg_f047_revenue_growth_core68_2nd_v069_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core69_2nd_v070_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_safe_div(revenue, revenueusd), 4), 12))
def cg_f047_revenue_growth_core70_2nd_v071_signal(revenue, revenueusd):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f047_revenue_growth_core71_2nd_v072_signal(revenue, revenueusd):
    return _clean(_rank(_diff(revenueusd, 4), 12))
def cg_f047_revenue_growth_core72_2nd_v073_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_pct_change(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core73_2nd_v074_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_pct_change(revenueusd, 4), 4), 12))
def cg_f047_revenue_growth_core74_2nd_v075_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_diff(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core75_2nd_v076_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_diff(revenueusd, 4), 4), 12))
def cg_f047_revenue_growth_core76_2nd_v077_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_slope(revenue, 8), 4), 12))
def cg_f047_revenue_growth_core77_2nd_v078_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_z(revenue, 12), 4), 12))
def cg_f047_revenue_growth_core78_2nd_v079_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_mean(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core79_2nd_v080_signal(revenue, revenueusd):
    return _clean(_rank(_diff(_safe_div(revenue, revenueusd), 4), 12))
def cg_f047_revenue_growth_core80_2nd_v081_signal(revenue, revenueusd):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f047_revenue_growth_core81_2nd_v082_signal(revenue, revenueusd):
    return _clean(_mean(_slope(revenueusd, 4), 4))
def cg_f047_revenue_growth_core82_2nd_v083_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core83_2nd_v084_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_pct_change(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core84_2nd_v085_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_diff(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core85_2nd_v086_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_diff(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core86_2nd_v087_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_slope(revenue, 8), 4), 4))
def cg_f047_revenue_growth_core87_2nd_v088_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_z(revenue, 12), 4), 4))
def cg_f047_revenue_growth_core88_2nd_v089_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_mean(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core89_2nd_v090_signal(revenue, revenueusd):
    return _clean(_mean(_slope(_safe_div(revenue, revenueusd), 4), 4))
def cg_f047_revenue_growth_core90_2nd_v091_signal(revenue, revenueusd):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f047_revenue_growth_core91_2nd_v092_signal(revenue, revenueusd):
    return _clean(_mean(_diff(revenueusd, 4), 4))
def cg_f047_revenue_growth_core92_2nd_v093_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core93_2nd_v094_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_pct_change(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core94_2nd_v095_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_diff(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core95_2nd_v096_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_diff(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core96_2nd_v097_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_slope(revenue, 8), 4), 4))
def cg_f047_revenue_growth_core97_2nd_v098_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_z(revenue, 12), 4), 4))
def cg_f047_revenue_growth_core98_2nd_v099_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_mean(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core99_2nd_v100_signal(revenue, revenueusd):
    return _clean(_mean(_diff(_safe_div(revenue, revenueusd), 4), 4))
def cg_f047_revenue_growth_core100_2nd_v101_signal(revenue, revenueusd):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f047_revenue_growth_core101_2nd_v102_signal(revenue, revenueusd):
    return _clean(_slope(_mean(revenueusd, 4), 4))
def cg_f047_revenue_growth_core102_2nd_v103_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core103_2nd_v104_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_pct_change(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core104_2nd_v105_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_diff(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core105_2nd_v106_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_diff(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core106_2nd_v107_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_slope(revenue, 8), 4), 4))
def cg_f047_revenue_growth_core107_2nd_v108_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_z(revenue, 12), 4), 4))
def cg_f047_revenue_growth_core108_2nd_v109_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_mean(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core109_2nd_v110_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_safe_div(revenue, revenueusd), 4), 4))
def cg_f047_revenue_growth_core110_2nd_v111_signal(revenue, revenueusd):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f047_revenue_growth_core111_2nd_v112_signal(revenue, revenueusd):
    return _clean(_slope(_mean(revenueusd, 8), 8))
def cg_f047_revenue_growth_core112_2nd_v113_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_pct_change(revenue, 4), 8), 8))
def cg_f047_revenue_growth_core113_2nd_v114_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_pct_change(revenueusd, 4), 8), 8))
def cg_f047_revenue_growth_core114_2nd_v115_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_diff(revenue, 4), 8), 8))
def cg_f047_revenue_growth_core115_2nd_v116_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_diff(revenueusd, 4), 8), 8))
def cg_f047_revenue_growth_core116_2nd_v117_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_slope(revenue, 8), 8), 8))
def cg_f047_revenue_growth_core117_2nd_v118_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_z(revenue, 12), 8), 8))
def cg_f047_revenue_growth_core118_2nd_v119_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_mean(revenue, 4), 8), 8))
def cg_f047_revenue_growth_core119_2nd_v120_signal(revenue, revenueusd):
    return _clean(_slope(_mean(_safe_div(revenue, revenueusd), 8), 8))
def cg_f047_revenue_growth_core120_2nd_v121_signal(revenue, revenueusd):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f047_revenue_growth_core121_2nd_v122_signal(revenue, revenueusd):
    return _clean(_diff(_mean(revenueusd, 4), 4))
def cg_f047_revenue_growth_core122_2nd_v123_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_pct_change(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core123_2nd_v124_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_pct_change(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core124_2nd_v125_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_diff(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core125_2nd_v126_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_diff(revenueusd, 4), 4), 4))
def cg_f047_revenue_growth_core126_2nd_v127_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_slope(revenue, 8), 4), 4))
def cg_f047_revenue_growth_core127_2nd_v128_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_z(revenue, 12), 4), 4))
def cg_f047_revenue_growth_core128_2nd_v129_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_mean(revenue, 4), 4), 4))
def cg_f047_revenue_growth_core129_2nd_v130_signal(revenue, revenueusd):
    return _clean(_diff(_mean(_safe_div(revenue, revenueusd), 4), 4))
def cg_f047_revenue_growth_core130_2nd_v131_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f047_revenue_growth_core131_2nd_v132_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(revenueusd, 4), 4), 8))
def cg_f047_revenue_growth_core132_2nd_v133_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_pct_change(revenue, 4), 4), 4), 8))
def cg_f047_revenue_growth_core133_2nd_v134_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_pct_change(revenueusd, 4), 4), 4), 8))
def cg_f047_revenue_growth_core134_2nd_v135_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_diff(revenue, 4), 4), 4), 8))
def cg_f047_revenue_growth_core135_2nd_v136_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_diff(revenueusd, 4), 4), 4), 8))
def cg_f047_revenue_growth_core136_2nd_v137_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_slope(revenue, 8), 4), 4), 8))
def cg_f047_revenue_growth_core137_2nd_v138_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_z(revenue, 12), 4), 4), 8))
def cg_f047_revenue_growth_core138_2nd_v139_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_mean(revenue, 4), 4), 4), 8))
def cg_f047_revenue_growth_core139_2nd_v140_signal(revenue, revenueusd):
    return _clean(_z(_diff(_mean(_safe_div(revenue, revenueusd), 4), 4), 8))
def cg_f047_revenue_growth_core140_2nd_v141_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f047_revenue_growth_core141_2nd_v142_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(revenueusd, 4), 4), 12))
def cg_f047_revenue_growth_core142_2nd_v143_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_pct_change(revenue, 4), 4), 4), 12))
def cg_f047_revenue_growth_core143_2nd_v144_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_pct_change(revenueusd, 4), 4), 4), 12))
def cg_f047_revenue_growth_core144_2nd_v145_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_diff(revenue, 4), 4), 4), 12))
def cg_f047_revenue_growth_core145_2nd_v146_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_diff(revenueusd, 4), 4), 4), 12))
def cg_f047_revenue_growth_core146_2nd_v147_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_slope(revenue, 8), 4), 4), 12))
def cg_f047_revenue_growth_core147_2nd_v148_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_z(revenue, 12), 4), 4), 12))
def cg_f047_revenue_growth_core148_2nd_v149_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_mean(revenue, 4), 4), 4), 12))
def cg_f047_revenue_growth_core149_2nd_v150_signal(revenue, revenueusd):
    return _clean(_rank(_slope(_mean(_safe_div(revenue, revenueusd), 4), 4), 12))