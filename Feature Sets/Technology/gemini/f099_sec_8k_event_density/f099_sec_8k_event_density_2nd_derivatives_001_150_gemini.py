import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f099_sec_8k_event_density_core00_2nd_v001_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes, 4))
def cg_f099_sec_8k_event_density_core01_2nd_v002_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes.abs(), 4))
def cg_f099_sec_8k_event_density_core02_2nd_v003_signal(ticker, date, eventcodes):
    return _clean(_slope(_log(eventcodes.abs() + 1.0), 4))
def cg_f099_sec_8k_event_density_core03_2nd_v004_signal(ticker, date, eventcodes):
    return _clean(_slope(_to_num(eventcodes), 4))
def cg_f099_sec_8k_event_density_core04_2nd_v005_signal(ticker, date, eventcodes):
    return _clean(_slope(_clean(eventcodes), 4))
def cg_f099_sec_8k_event_density_core05_2nd_v006_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes * 1.0, 4))
def cg_f099_sec_8k_event_density_core06_2nd_v007_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes * eventcodes, 4))
def cg_f099_sec_8k_event_density_core07_2nd_v008_signal(ticker, date, eventcodes):
    return _clean(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4))
def cg_f099_sec_8k_event_density_core08_2nd_v009_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core09_2nd_v010_signal(ticker, date, eventcodes):
    return _clean(_slope(_std(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core10_2nd_v011_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes, 8))
def cg_f099_sec_8k_event_density_core11_2nd_v012_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes.abs(), 8))
def cg_f099_sec_8k_event_density_core12_2nd_v013_signal(ticker, date, eventcodes):
    return _clean(_slope(_log(eventcodes.abs() + 1.0), 8))
def cg_f099_sec_8k_event_density_core13_2nd_v014_signal(ticker, date, eventcodes):
    return _clean(_slope(_to_num(eventcodes), 8))
def cg_f099_sec_8k_event_density_core14_2nd_v015_signal(ticker, date, eventcodes):
    return _clean(_slope(_clean(eventcodes), 8))
def cg_f099_sec_8k_event_density_core15_2nd_v016_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes * 1.0, 8))
def cg_f099_sec_8k_event_density_core16_2nd_v017_signal(ticker, date, eventcodes):
    return _clean(_slope(eventcodes * eventcodes, 8))
def cg_f099_sec_8k_event_density_core17_2nd_v018_signal(ticker, date, eventcodes):
    return _clean(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 8))
def cg_f099_sec_8k_event_density_core18_2nd_v019_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core19_2nd_v020_signal(ticker, date, eventcodes):
    return _clean(_slope(_std(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core20_2nd_v021_signal(ticker, date, eventcodes):
    return _clean(_diff(eventcodes, 4))
def cg_f099_sec_8k_event_density_core21_2nd_v022_signal(ticker, date, eventcodes):
    return _clean(_diff(eventcodes.abs(), 4))
def cg_f099_sec_8k_event_density_core22_2nd_v023_signal(ticker, date, eventcodes):
    return _clean(_diff(_log(eventcodes.abs() + 1.0), 4))
def cg_f099_sec_8k_event_density_core23_2nd_v024_signal(ticker, date, eventcodes):
    return _clean(_diff(_to_num(eventcodes), 4))
def cg_f099_sec_8k_event_density_core24_2nd_v025_signal(ticker, date, eventcodes):
    return _clean(_diff(_clean(eventcodes), 4))
def cg_f099_sec_8k_event_density_core25_2nd_v026_signal(ticker, date, eventcodes):
    return _clean(_diff(eventcodes * 1.0, 4))
def cg_f099_sec_8k_event_density_core26_2nd_v027_signal(ticker, date, eventcodes):
    return _clean(_diff(eventcodes * eventcodes, 4))
def cg_f099_sec_8k_event_density_core27_2nd_v028_signal(ticker, date, eventcodes):
    return _clean(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4))
def cg_f099_sec_8k_event_density_core28_2nd_v029_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core29_2nd_v030_signal(ticker, date, eventcodes):
    return _clean(_diff(_std(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core30_2nd_v031_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core31_2nd_v032_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes.abs(), 4), 8))
def cg_f099_sec_8k_event_density_core32_2nd_v033_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_log(eventcodes.abs() + 1.0), 4), 8))
def cg_f099_sec_8k_event_density_core33_2nd_v034_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_to_num(eventcodes), 4), 8))
def cg_f099_sec_8k_event_density_core34_2nd_v035_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_clean(eventcodes), 4), 8))
def cg_f099_sec_8k_event_density_core35_2nd_v036_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes * 1.0, 4), 8))
def cg_f099_sec_8k_event_density_core36_2nd_v037_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes * eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core37_2nd_v038_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 8))
def cg_f099_sec_8k_event_density_core38_2nd_v039_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_mean(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core39_2nd_v040_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_std(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core40_2nd_v041_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes, 8), 12))
def cg_f099_sec_8k_event_density_core41_2nd_v042_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes.abs(), 8), 12))
def cg_f099_sec_8k_event_density_core42_2nd_v043_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_log(eventcodes.abs() + 1.0), 8), 12))
def cg_f099_sec_8k_event_density_core43_2nd_v044_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_to_num(eventcodes), 8), 12))
def cg_f099_sec_8k_event_density_core44_2nd_v045_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_clean(eventcodes), 8), 12))
def cg_f099_sec_8k_event_density_core45_2nd_v046_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes * 1.0, 8), 12))
def cg_f099_sec_8k_event_density_core46_2nd_v047_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(eventcodes * eventcodes, 8), 12))
def cg_f099_sec_8k_event_density_core47_2nd_v048_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 8), 12))
def cg_f099_sec_8k_event_density_core48_2nd_v049_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_mean(eventcodes, 4), 8), 12))
def cg_f099_sec_8k_event_density_core49_2nd_v050_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_std(eventcodes, 4), 8), 12))
def cg_f099_sec_8k_event_density_core50_2nd_v051_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core51_2nd_v052_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(eventcodes.abs(), 4), 8))
def cg_f099_sec_8k_event_density_core52_2nd_v053_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_log(eventcodes.abs() + 1.0), 4), 8))
def cg_f099_sec_8k_event_density_core53_2nd_v054_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_to_num(eventcodes), 4), 8))
def cg_f099_sec_8k_event_density_core54_2nd_v055_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_clean(eventcodes), 4), 8))
def cg_f099_sec_8k_event_density_core55_2nd_v056_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(eventcodes * 1.0, 4), 8))
def cg_f099_sec_8k_event_density_core56_2nd_v057_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(eventcodes * eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core57_2nd_v058_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 8))
def cg_f099_sec_8k_event_density_core58_2nd_v059_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core59_2nd_v060_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_std(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core60_2nd_v061_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(eventcodes, 4), 12))
def cg_f099_sec_8k_event_density_core61_2nd_v062_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(eventcodes.abs(), 4), 12))
def cg_f099_sec_8k_event_density_core62_2nd_v063_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_log(eventcodes.abs() + 1.0), 4), 12))
def cg_f099_sec_8k_event_density_core63_2nd_v064_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_to_num(eventcodes), 4), 12))
def cg_f099_sec_8k_event_density_core64_2nd_v065_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_clean(eventcodes), 4), 12))
def cg_f099_sec_8k_event_density_core65_2nd_v066_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(eventcodes * 1.0, 4), 12))
def cg_f099_sec_8k_event_density_core66_2nd_v067_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(eventcodes * eventcodes, 4), 12))
def cg_f099_sec_8k_event_density_core67_2nd_v068_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 12))
def cg_f099_sec_8k_event_density_core68_2nd_v069_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core69_2nd_v070_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_std(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core70_2nd_v071_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(eventcodes, 4), 12))
def cg_f099_sec_8k_event_density_core71_2nd_v072_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(eventcodes.abs(), 4), 12))
def cg_f099_sec_8k_event_density_core72_2nd_v073_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_log(eventcodes.abs() + 1.0), 4), 12))
def cg_f099_sec_8k_event_density_core73_2nd_v074_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_to_num(eventcodes), 4), 12))
def cg_f099_sec_8k_event_density_core74_2nd_v075_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_clean(eventcodes), 4), 12))
def cg_f099_sec_8k_event_density_core75_2nd_v076_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(eventcodes * 1.0, 4), 12))
def cg_f099_sec_8k_event_density_core76_2nd_v077_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(eventcodes * eventcodes, 4), 12))
def cg_f099_sec_8k_event_density_core77_2nd_v078_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 12))
def cg_f099_sec_8k_event_density_core78_2nd_v079_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_mean(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core79_2nd_v080_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_std(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core80_2nd_v081_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core81_2nd_v082_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(eventcodes.abs(), 4), 4))
def cg_f099_sec_8k_event_density_core82_2nd_v083_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_log(eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core83_2nd_v084_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_to_num(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core84_2nd_v085_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_clean(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core85_2nd_v086_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(eventcodes * 1.0, 4), 4))
def cg_f099_sec_8k_event_density_core86_2nd_v087_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(eventcodes * eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core87_2nd_v088_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core88_2nd_v089_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_mean(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core89_2nd_v090_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_std(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core90_2nd_v091_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core91_2nd_v092_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(eventcodes.abs(), 4), 4))
def cg_f099_sec_8k_event_density_core92_2nd_v093_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_log(eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core93_2nd_v094_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_to_num(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core94_2nd_v095_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_clean(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core95_2nd_v096_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(eventcodes * 1.0, 4), 4))
def cg_f099_sec_8k_event_density_core96_2nd_v097_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(eventcodes * eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core97_2nd_v098_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core98_2nd_v099_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_mean(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core99_2nd_v100_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_std(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core100_2nd_v101_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core101_2nd_v102_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes.abs(), 4), 4))
def cg_f099_sec_8k_event_density_core102_2nd_v103_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_log(eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core103_2nd_v104_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_to_num(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core104_2nd_v105_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_clean(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core105_2nd_v106_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes * 1.0, 4), 4))
def cg_f099_sec_8k_event_density_core106_2nd_v107_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes * eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core107_2nd_v108_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core108_2nd_v109_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_mean(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core109_2nd_v110_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_std(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core110_2nd_v111_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes, 8), 8))
def cg_f099_sec_8k_event_density_core111_2nd_v112_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes.abs(), 8), 8))
def cg_f099_sec_8k_event_density_core112_2nd_v113_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_log(eventcodes.abs() + 1.0), 8), 8))
def cg_f099_sec_8k_event_density_core113_2nd_v114_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_to_num(eventcodes), 8), 8))
def cg_f099_sec_8k_event_density_core114_2nd_v115_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_clean(eventcodes), 8), 8))
def cg_f099_sec_8k_event_density_core115_2nd_v116_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes * 1.0, 8), 8))
def cg_f099_sec_8k_event_density_core116_2nd_v117_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(eventcodes * eventcodes, 8), 8))
def cg_f099_sec_8k_event_density_core117_2nd_v118_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_safe_div(1.0, eventcodes.abs() + 1.0), 8), 8))
def cg_f099_sec_8k_event_density_core118_2nd_v119_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_mean(eventcodes, 4), 8), 8))
def cg_f099_sec_8k_event_density_core119_2nd_v120_signal(ticker, date, eventcodes):
    return _clean(_slope(_mean(_std(eventcodes, 4), 8), 8))
def cg_f099_sec_8k_event_density_core120_2nd_v121_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core121_2nd_v122_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(eventcodes.abs(), 4), 4))
def cg_f099_sec_8k_event_density_core122_2nd_v123_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(_log(eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core123_2nd_v124_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(_to_num(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core124_2nd_v125_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(_clean(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core125_2nd_v126_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(eventcodes * 1.0, 4), 4))
def cg_f099_sec_8k_event_density_core126_2nd_v127_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(eventcodes * eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core127_2nd_v128_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core128_2nd_v129_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(_mean(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core129_2nd_v130_signal(ticker, date, eventcodes):
    return _clean(_diff(_mean(_std(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core130_2nd_v131_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core131_2nd_v132_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(eventcodes.abs(), 4), 4), 8))
def cg_f099_sec_8k_event_density_core132_2nd_v133_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(_log(eventcodes.abs() + 1.0), 4), 4), 8))
def cg_f099_sec_8k_event_density_core133_2nd_v134_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(_to_num(eventcodes), 4), 4), 8))
def cg_f099_sec_8k_event_density_core134_2nd_v135_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(_clean(eventcodes), 4), 4), 8))
def cg_f099_sec_8k_event_density_core135_2nd_v136_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(eventcodes * 1.0, 4), 4), 8))
def cg_f099_sec_8k_event_density_core136_2nd_v137_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(eventcodes * eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core137_2nd_v138_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 8))
def cg_f099_sec_8k_event_density_core138_2nd_v139_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(_mean(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core139_2nd_v140_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_mean(_std(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core140_2nd_v141_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core141_2nd_v142_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(eventcodes.abs(), 4), 4), 12))
def cg_f099_sec_8k_event_density_core142_2nd_v143_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(_log(eventcodes.abs() + 1.0), 4), 4), 12))
def cg_f099_sec_8k_event_density_core143_2nd_v144_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(_to_num(eventcodes), 4), 4), 12))
def cg_f099_sec_8k_event_density_core144_2nd_v145_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(_clean(eventcodes), 4), 4), 12))
def cg_f099_sec_8k_event_density_core145_2nd_v146_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(eventcodes * 1.0, 4), 4), 12))
def cg_f099_sec_8k_event_density_core146_2nd_v147_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(eventcodes * eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core147_2nd_v148_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 12))
def cg_f099_sec_8k_event_density_core148_2nd_v149_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(_mean(eventcodes, 4), 4), 4), 12))
def cg_f099_sec_8k_event_density_core149_2nd_v150_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_mean(_std(eventcodes, 4), 4), 4), 12))