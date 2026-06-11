import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f085_indicator_availability_core00_2nd_v001_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(table), 4))
def cg_f085_indicator_availability_core01_2nd_v002_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(indicator), 4))
def cg_f085_indicator_availability_core02_2nd_v003_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(title), 4))
def cg_f085_indicator_availability_core03_2nd_v004_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(description), 4))
def cg_f085_indicator_availability_core04_2nd_v005_signal(table, indicator, title, description):
    return _clean(_slope(_event_count(table, 4), 4))
def cg_f085_indicator_availability_core05_2nd_v006_signal(table, indicator, title, description):
    return _clean(_slope(_event_count(indicator, 4), 4))
def cg_f085_indicator_availability_core06_2nd_v007_signal(table, indicator, title, description):
    return _clean(_slope(_event_rate(table, 8), 4))
def cg_f085_indicator_availability_core07_2nd_v008_signal(table, indicator, title, description):
    return _clean(_slope(_event_rate(indicator, 8), 4))
def cg_f085_indicator_availability_core08_2nd_v009_signal(table, indicator, title, description):
    return _clean(_slope(_to_num(table == 'SEP'), 4))
def cg_f085_indicator_availability_core09_2nd_v010_signal(table, indicator, title, description):
    return _clean(_slope(_to_num(table == 'SF1'), 4))
def cg_f085_indicator_availability_core10_2nd_v011_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(table), 8))
def cg_f085_indicator_availability_core11_2nd_v012_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(indicator), 8))
def cg_f085_indicator_availability_core12_2nd_v013_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(title), 8))
def cg_f085_indicator_availability_core13_2nd_v014_signal(table, indicator, title, description):
    return _clean(_slope(_event_flag(description), 8))
def cg_f085_indicator_availability_core14_2nd_v015_signal(table, indicator, title, description):
    return _clean(_slope(_event_count(table, 4), 8))
def cg_f085_indicator_availability_core15_2nd_v016_signal(table, indicator, title, description):
    return _clean(_slope(_event_count(indicator, 4), 8))
def cg_f085_indicator_availability_core16_2nd_v017_signal(table, indicator, title, description):
    return _clean(_slope(_event_rate(table, 8), 8))
def cg_f085_indicator_availability_core17_2nd_v018_signal(table, indicator, title, description):
    return _clean(_slope(_event_rate(indicator, 8), 8))
def cg_f085_indicator_availability_core18_2nd_v019_signal(table, indicator, title, description):
    return _clean(_slope(_to_num(table == 'SEP'), 8))
def cg_f085_indicator_availability_core19_2nd_v020_signal(table, indicator, title, description):
    return _clean(_slope(_to_num(table == 'SF1'), 8))
def cg_f085_indicator_availability_core20_2nd_v021_signal(table, indicator, title, description):
    return _clean(_diff(_event_flag(table), 4))
def cg_f085_indicator_availability_core21_2nd_v022_signal(table, indicator, title, description):
    return _clean(_diff(_event_flag(indicator), 4))
def cg_f085_indicator_availability_core22_2nd_v023_signal(table, indicator, title, description):
    return _clean(_diff(_event_flag(title), 4))
def cg_f085_indicator_availability_core23_2nd_v024_signal(table, indicator, title, description):
    return _clean(_diff(_event_flag(description), 4))
def cg_f085_indicator_availability_core24_2nd_v025_signal(table, indicator, title, description):
    return _clean(_diff(_event_count(table, 4), 4))
def cg_f085_indicator_availability_core25_2nd_v026_signal(table, indicator, title, description):
    return _clean(_diff(_event_count(indicator, 4), 4))
def cg_f085_indicator_availability_core26_2nd_v027_signal(table, indicator, title, description):
    return _clean(_diff(_event_rate(table, 8), 4))
def cg_f085_indicator_availability_core27_2nd_v028_signal(table, indicator, title, description):
    return _clean(_diff(_event_rate(indicator, 8), 4))
def cg_f085_indicator_availability_core28_2nd_v029_signal(table, indicator, title, description):
    return _clean(_diff(_to_num(table == 'SEP'), 4))
def cg_f085_indicator_availability_core29_2nd_v030_signal(table, indicator, title, description):
    return _clean(_diff(_to_num(table == 'SF1'), 4))
def cg_f085_indicator_availability_core30_2nd_v031_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(table), 4), 8))
def cg_f085_indicator_availability_core31_2nd_v032_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(indicator), 4), 8))
def cg_f085_indicator_availability_core32_2nd_v033_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(title), 4), 8))
def cg_f085_indicator_availability_core33_2nd_v034_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(description), 4), 8))
def cg_f085_indicator_availability_core34_2nd_v035_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_count(table, 4), 4), 8))
def cg_f085_indicator_availability_core35_2nd_v036_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_count(indicator, 4), 4), 8))
def cg_f085_indicator_availability_core36_2nd_v037_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_rate(table, 8), 4), 8))
def cg_f085_indicator_availability_core37_2nd_v038_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_rate(indicator, 8), 4), 8))
def cg_f085_indicator_availability_core38_2nd_v039_signal(table, indicator, title, description):
    return _clean(_z(_slope(_to_num(table == 'SEP'), 4), 8))
def cg_f085_indicator_availability_core39_2nd_v040_signal(table, indicator, title, description):
    return _clean(_z(_slope(_to_num(table == 'SF1'), 4), 8))
def cg_f085_indicator_availability_core40_2nd_v041_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(table), 8), 12))
def cg_f085_indicator_availability_core41_2nd_v042_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(indicator), 8), 12))
def cg_f085_indicator_availability_core42_2nd_v043_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(title), 8), 12))
def cg_f085_indicator_availability_core43_2nd_v044_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_flag(description), 8), 12))
def cg_f085_indicator_availability_core44_2nd_v045_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_count(table, 4), 8), 12))
def cg_f085_indicator_availability_core45_2nd_v046_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_count(indicator, 4), 8), 12))
def cg_f085_indicator_availability_core46_2nd_v047_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_rate(table, 8), 8), 12))
def cg_f085_indicator_availability_core47_2nd_v048_signal(table, indicator, title, description):
    return _clean(_z(_slope(_event_rate(indicator, 8), 8), 12))
def cg_f085_indicator_availability_core48_2nd_v049_signal(table, indicator, title, description):
    return _clean(_z(_slope(_to_num(table == 'SEP'), 8), 12))
def cg_f085_indicator_availability_core49_2nd_v050_signal(table, indicator, title, description):
    return _clean(_z(_slope(_to_num(table == 'SF1'), 8), 12))
def cg_f085_indicator_availability_core50_2nd_v051_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_flag(table), 4), 8))
def cg_f085_indicator_availability_core51_2nd_v052_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_flag(indicator), 4), 8))
def cg_f085_indicator_availability_core52_2nd_v053_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_flag(title), 4), 8))
def cg_f085_indicator_availability_core53_2nd_v054_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_flag(description), 4), 8))
def cg_f085_indicator_availability_core54_2nd_v055_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_count(table, 4), 4), 8))
def cg_f085_indicator_availability_core55_2nd_v056_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_count(indicator, 4), 4), 8))
def cg_f085_indicator_availability_core56_2nd_v057_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_rate(table, 8), 4), 8))
def cg_f085_indicator_availability_core57_2nd_v058_signal(table, indicator, title, description):
    return _clean(_z(_diff(_event_rate(indicator, 8), 4), 8))
def cg_f085_indicator_availability_core58_2nd_v059_signal(table, indicator, title, description):
    return _clean(_z(_diff(_to_num(table == 'SEP'), 4), 8))
def cg_f085_indicator_availability_core59_2nd_v060_signal(table, indicator, title, description):
    return _clean(_z(_diff(_to_num(table == 'SF1'), 4), 8))
def cg_f085_indicator_availability_core60_2nd_v061_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_flag(table), 4), 12))
def cg_f085_indicator_availability_core61_2nd_v062_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_flag(indicator), 4), 12))
def cg_f085_indicator_availability_core62_2nd_v063_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_flag(title), 4), 12))
def cg_f085_indicator_availability_core63_2nd_v064_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_flag(description), 4), 12))
def cg_f085_indicator_availability_core64_2nd_v065_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_count(table, 4), 4), 12))
def cg_f085_indicator_availability_core65_2nd_v066_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_count(indicator, 4), 4), 12))
def cg_f085_indicator_availability_core66_2nd_v067_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_rate(table, 8), 4), 12))
def cg_f085_indicator_availability_core67_2nd_v068_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_event_rate(indicator, 8), 4), 12))
def cg_f085_indicator_availability_core68_2nd_v069_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_to_num(table == 'SEP'), 4), 12))
def cg_f085_indicator_availability_core69_2nd_v070_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_to_num(table == 'SF1'), 4), 12))
def cg_f085_indicator_availability_core70_2nd_v071_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_flag(table), 4), 12))
def cg_f085_indicator_availability_core71_2nd_v072_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_flag(indicator), 4), 12))
def cg_f085_indicator_availability_core72_2nd_v073_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_flag(title), 4), 12))
def cg_f085_indicator_availability_core73_2nd_v074_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_flag(description), 4), 12))
def cg_f085_indicator_availability_core74_2nd_v075_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_count(table, 4), 4), 12))
def cg_f085_indicator_availability_core75_2nd_v076_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_count(indicator, 4), 4), 12))
def cg_f085_indicator_availability_core76_2nd_v077_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_rate(table, 8), 4), 12))
def cg_f085_indicator_availability_core77_2nd_v078_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_event_rate(indicator, 8), 4), 12))
def cg_f085_indicator_availability_core78_2nd_v079_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_to_num(table == 'SEP'), 4), 12))
def cg_f085_indicator_availability_core79_2nd_v080_signal(table, indicator, title, description):
    return _clean(_rank(_diff(_to_num(table == 'SF1'), 4), 12))
def cg_f085_indicator_availability_core80_2nd_v081_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_flag(table), 4), 4))
def cg_f085_indicator_availability_core81_2nd_v082_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_flag(indicator), 4), 4))
def cg_f085_indicator_availability_core82_2nd_v083_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_flag(title), 4), 4))
def cg_f085_indicator_availability_core83_2nd_v084_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_flag(description), 4), 4))
def cg_f085_indicator_availability_core84_2nd_v085_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_count(table, 4), 4), 4))
def cg_f085_indicator_availability_core85_2nd_v086_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_count(indicator, 4), 4), 4))
def cg_f085_indicator_availability_core86_2nd_v087_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_rate(table, 8), 4), 4))
def cg_f085_indicator_availability_core87_2nd_v088_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_event_rate(indicator, 8), 4), 4))
def cg_f085_indicator_availability_core88_2nd_v089_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_to_num(table == 'SEP'), 4), 4))
def cg_f085_indicator_availability_core89_2nd_v090_signal(table, indicator, title, description):
    return _clean(_mean(_slope(_to_num(table == 'SF1'), 4), 4))
def cg_f085_indicator_availability_core90_2nd_v091_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_flag(table), 4), 4))
def cg_f085_indicator_availability_core91_2nd_v092_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_flag(indicator), 4), 4))
def cg_f085_indicator_availability_core92_2nd_v093_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_flag(title), 4), 4))
def cg_f085_indicator_availability_core93_2nd_v094_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_flag(description), 4), 4))
def cg_f085_indicator_availability_core94_2nd_v095_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_count(table, 4), 4), 4))
def cg_f085_indicator_availability_core95_2nd_v096_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_count(indicator, 4), 4), 4))
def cg_f085_indicator_availability_core96_2nd_v097_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_rate(table, 8), 4), 4))
def cg_f085_indicator_availability_core97_2nd_v098_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_event_rate(indicator, 8), 4), 4))
def cg_f085_indicator_availability_core98_2nd_v099_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_to_num(table == 'SEP'), 4), 4))
def cg_f085_indicator_availability_core99_2nd_v100_signal(table, indicator, title, description):
    return _clean(_mean(_diff(_to_num(table == 'SF1'), 4), 4))
def cg_f085_indicator_availability_core100_2nd_v101_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(table), 4), 4))
def cg_f085_indicator_availability_core101_2nd_v102_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(indicator), 4), 4))
def cg_f085_indicator_availability_core102_2nd_v103_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(title), 4), 4))
def cg_f085_indicator_availability_core103_2nd_v104_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(description), 4), 4))
def cg_f085_indicator_availability_core104_2nd_v105_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_count(table, 4), 4), 4))
def cg_f085_indicator_availability_core105_2nd_v106_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_count(indicator, 4), 4), 4))
def cg_f085_indicator_availability_core106_2nd_v107_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_rate(table, 8), 4), 4))
def cg_f085_indicator_availability_core107_2nd_v108_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_rate(indicator, 8), 4), 4))
def cg_f085_indicator_availability_core108_2nd_v109_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_to_num(table == 'SEP'), 4), 4))
def cg_f085_indicator_availability_core109_2nd_v110_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_to_num(table == 'SF1'), 4), 4))
def cg_f085_indicator_availability_core110_2nd_v111_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(table), 8), 8))
def cg_f085_indicator_availability_core111_2nd_v112_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(indicator), 8), 8))
def cg_f085_indicator_availability_core112_2nd_v113_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(title), 8), 8))
def cg_f085_indicator_availability_core113_2nd_v114_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_flag(description), 8), 8))
def cg_f085_indicator_availability_core114_2nd_v115_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_count(table, 4), 8), 8))
def cg_f085_indicator_availability_core115_2nd_v116_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_count(indicator, 4), 8), 8))
def cg_f085_indicator_availability_core116_2nd_v117_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_rate(table, 8), 8), 8))
def cg_f085_indicator_availability_core117_2nd_v118_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_event_rate(indicator, 8), 8), 8))
def cg_f085_indicator_availability_core118_2nd_v119_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_to_num(table == 'SEP'), 8), 8))
def cg_f085_indicator_availability_core119_2nd_v120_signal(table, indicator, title, description):
    return _clean(_slope(_mean(_to_num(table == 'SF1'), 8), 8))
def cg_f085_indicator_availability_core120_2nd_v121_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_flag(table), 4), 4))
def cg_f085_indicator_availability_core121_2nd_v122_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_flag(indicator), 4), 4))
def cg_f085_indicator_availability_core122_2nd_v123_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_flag(title), 4), 4))
def cg_f085_indicator_availability_core123_2nd_v124_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_flag(description), 4), 4))
def cg_f085_indicator_availability_core124_2nd_v125_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_count(table, 4), 4), 4))
def cg_f085_indicator_availability_core125_2nd_v126_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_count(indicator, 4), 4), 4))
def cg_f085_indicator_availability_core126_2nd_v127_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_rate(table, 8), 4), 4))
def cg_f085_indicator_availability_core127_2nd_v128_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_event_rate(indicator, 8), 4), 4))
def cg_f085_indicator_availability_core128_2nd_v129_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_to_num(table == 'SEP'), 4), 4))
def cg_f085_indicator_availability_core129_2nd_v130_signal(table, indicator, title, description):
    return _clean(_diff(_mean(_to_num(table == 'SF1'), 4), 4))
def cg_f085_indicator_availability_core130_2nd_v131_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_flag(table), 4), 4), 8))
def cg_f085_indicator_availability_core131_2nd_v132_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_flag(indicator), 4), 4), 8))
def cg_f085_indicator_availability_core132_2nd_v133_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_flag(title), 4), 4), 8))
def cg_f085_indicator_availability_core133_2nd_v134_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_flag(description), 4), 4), 8))
def cg_f085_indicator_availability_core134_2nd_v135_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_count(table, 4), 4), 4), 8))
def cg_f085_indicator_availability_core135_2nd_v136_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_count(indicator, 4), 4), 4), 8))
def cg_f085_indicator_availability_core136_2nd_v137_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_rate(table, 8), 4), 4), 8))
def cg_f085_indicator_availability_core137_2nd_v138_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_event_rate(indicator, 8), 4), 4), 8))
def cg_f085_indicator_availability_core138_2nd_v139_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_to_num(table == 'SEP'), 4), 4), 8))
def cg_f085_indicator_availability_core139_2nd_v140_signal(table, indicator, title, description):
    return _clean(_z(_diff(_mean(_to_num(table == 'SF1'), 4), 4), 8))
def cg_f085_indicator_availability_core140_2nd_v141_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_flag(table), 4), 4), 12))
def cg_f085_indicator_availability_core141_2nd_v142_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_flag(indicator), 4), 4), 12))
def cg_f085_indicator_availability_core142_2nd_v143_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_flag(title), 4), 4), 12))
def cg_f085_indicator_availability_core143_2nd_v144_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_flag(description), 4), 4), 12))
def cg_f085_indicator_availability_core144_2nd_v145_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_count(table, 4), 4), 4), 12))
def cg_f085_indicator_availability_core145_2nd_v146_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_count(indicator, 4), 4), 4), 12))
def cg_f085_indicator_availability_core146_2nd_v147_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_rate(table, 8), 4), 4), 12))
def cg_f085_indicator_availability_core147_2nd_v148_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_event_rate(indicator, 8), 4), 4), 12))
def cg_f085_indicator_availability_core148_2nd_v149_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_to_num(table == 'SEP'), 4), 4), 12))
def cg_f085_indicator_availability_core149_2nd_v150_signal(table, indicator, title, description):
    return _clean(_rank(_slope(_mean(_to_num(table == 'SF1'), 4), 4), 12))