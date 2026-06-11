import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f099_sec_8k_event_density_core00_3rd_v001_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core01_3rd_v002_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(eventcodes.abs(), 4), 4))
def cg_f099_sec_8k_event_density_core02_3rd_v003_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core03_3rd_v004_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_to_num(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core04_3rd_v005_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_clean(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core05_3rd_v006_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(eventcodes * 1.0, 4), 4))
def cg_f099_sec_8k_event_density_core06_3rd_v007_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(eventcodes * eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core07_3rd_v008_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core08_3rd_v009_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_mean(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core09_3rd_v010_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_std(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core10_3rd_v011_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core11_3rd_v012_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(eventcodes.abs(), 4), 8))
def cg_f099_sec_8k_event_density_core12_3rd_v013_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_log(eventcodes.abs() + 1.0), 4), 8))
def cg_f099_sec_8k_event_density_core13_3rd_v014_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_to_num(eventcodes), 4), 8))
def cg_f099_sec_8k_event_density_core14_3rd_v015_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_clean(eventcodes), 4), 8))
def cg_f099_sec_8k_event_density_core15_3rd_v016_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(eventcodes * 1.0, 4), 8))
def cg_f099_sec_8k_event_density_core16_3rd_v017_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(eventcodes * eventcodes, 4), 8))
def cg_f099_sec_8k_event_density_core17_3rd_v018_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 8))
def cg_f099_sec_8k_event_density_core18_3rd_v019_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_mean(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core19_3rd_v020_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_std(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core20_3rd_v021_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core21_3rd_v022_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(eventcodes.abs(), 4), 4))
def cg_f099_sec_8k_event_density_core22_3rd_v023_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(_log(eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core23_3rd_v024_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(_to_num(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core24_3rd_v025_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(_clean(eventcodes), 4), 4))
def cg_f099_sec_8k_event_density_core25_3rd_v026_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(eventcodes * 1.0, 4), 4))
def cg_f099_sec_8k_event_density_core26_3rd_v027_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(eventcodes * eventcodes, 4), 4))
def cg_f099_sec_8k_event_density_core27_3rd_v028_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4))
def cg_f099_sec_8k_event_density_core28_3rd_v029_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(_mean(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core29_3rd_v030_signal(ticker, date, eventcodes):
    return _clean(_diff(_slope(_std(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core30_3rd_v031_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core31_3rd_v032_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(eventcodes.abs(), 4), 4), 8))
def cg_f099_sec_8k_event_density_core32_3rd_v033_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4), 8))
def cg_f099_sec_8k_event_density_core33_3rd_v034_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(_to_num(eventcodes), 4), 4), 8))
def cg_f099_sec_8k_event_density_core34_3rd_v035_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(_clean(eventcodes), 4), 4), 8))
def cg_f099_sec_8k_event_density_core35_3rd_v036_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(eventcodes * 1.0, 4), 4), 8))
def cg_f099_sec_8k_event_density_core36_3rd_v037_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(eventcodes * eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core37_3rd_v038_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 8))
def cg_f099_sec_8k_event_density_core38_3rd_v039_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(_mean(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core39_3rd_v040_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_diff(_std(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core40_3rd_v041_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(eventcodes, 4), 8), 12))
def cg_f099_sec_8k_event_density_core41_3rd_v042_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(eventcodes.abs(), 4), 8), 12))
def cg_f099_sec_8k_event_density_core42_3rd_v043_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_log(eventcodes.abs() + 1.0), 4), 8), 12))
def cg_f099_sec_8k_event_density_core43_3rd_v044_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_to_num(eventcodes), 4), 8), 12))
def cg_f099_sec_8k_event_density_core44_3rd_v045_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_clean(eventcodes), 4), 8), 12))
def cg_f099_sec_8k_event_density_core45_3rd_v046_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(eventcodes * 1.0, 4), 8), 12))
def cg_f099_sec_8k_event_density_core46_3rd_v047_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(eventcodes * eventcodes, 4), 8), 12))
def cg_f099_sec_8k_event_density_core47_3rd_v048_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 8), 12))
def cg_f099_sec_8k_event_density_core48_3rd_v049_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_mean(eventcodes, 4), 4), 8), 12))
def cg_f099_sec_8k_event_density_core49_3rd_v050_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_std(eventcodes, 4), 4), 8), 12))
def cg_f099_sec_8k_event_density_core50_3rd_v051_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core51_3rd_v052_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(eventcodes.abs(), 4), 4), 8))
def cg_f099_sec_8k_event_density_core52_3rd_v053_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(_log(eventcodes.abs() + 1.0), 4), 4), 8))
def cg_f099_sec_8k_event_density_core53_3rd_v054_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(_to_num(eventcodes), 4), 4), 8))
def cg_f099_sec_8k_event_density_core54_3rd_v055_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(_clean(eventcodes), 4), 4), 8))
def cg_f099_sec_8k_event_density_core55_3rd_v056_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(eventcodes * 1.0, 4), 4), 8))
def cg_f099_sec_8k_event_density_core56_3rd_v057_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(eventcodes * eventcodes, 4), 4), 8))
def cg_f099_sec_8k_event_density_core57_3rd_v058_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 8))
def cg_f099_sec_8k_event_density_core58_3rd_v059_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(_mean(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core59_3rd_v060_signal(ticker, date, eventcodes):
    return _clean(_z(_diff(_slope(_std(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core60_3rd_v061_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core61_3rd_v062_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(eventcodes.abs(), 4), 4), 12))
def cg_f099_sec_8k_event_density_core62_3rd_v063_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4), 12))
def cg_f099_sec_8k_event_density_core63_3rd_v064_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(_to_num(eventcodes), 4), 4), 12))
def cg_f099_sec_8k_event_density_core64_3rd_v065_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(_clean(eventcodes), 4), 4), 12))
def cg_f099_sec_8k_event_density_core65_3rd_v066_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(eventcodes * 1.0, 4), 4), 12))
def cg_f099_sec_8k_event_density_core66_3rd_v067_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(eventcodes * eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core67_3rd_v068_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 12))
def cg_f099_sec_8k_event_density_core68_3rd_v069_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(_mean(eventcodes, 4), 4), 4), 12))
def cg_f099_sec_8k_event_density_core69_3rd_v070_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_diff(_std(eventcodes, 4), 4), 4), 12))
def cg_f099_sec_8k_event_density_core70_3rd_v071_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(eventcodes, 4), 8), 12))
def cg_f099_sec_8k_event_density_core71_3rd_v072_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(eventcodes.abs(), 4), 8), 12))
def cg_f099_sec_8k_event_density_core72_3rd_v073_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(_log(eventcodes.abs() + 1.0), 4), 8), 12))
def cg_f099_sec_8k_event_density_core73_3rd_v074_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(_to_num(eventcodes), 4), 8), 12))
def cg_f099_sec_8k_event_density_core74_3rd_v075_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(_clean(eventcodes), 4), 8), 12))
def cg_f099_sec_8k_event_density_core75_3rd_v076_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(eventcodes * 1.0, 4), 8), 12))
def cg_f099_sec_8k_event_density_core76_3rd_v077_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(eventcodes * eventcodes, 4), 8), 12))
def cg_f099_sec_8k_event_density_core77_3rd_v078_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 8), 12))
def cg_f099_sec_8k_event_density_core78_3rd_v079_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(_mean(eventcodes, 4), 4), 8), 12))
def cg_f099_sec_8k_event_density_core79_3rd_v080_signal(ticker, date, eventcodes):
    return _clean(_rank(_slope(_diff(_std(eventcodes, 4), 4), 8), 12))
def cg_f099_sec_8k_event_density_core80_3rd_v081_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core81_3rd_v082_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(eventcodes.abs(), 4), 4), 12))
def cg_f099_sec_8k_event_density_core82_3rd_v083_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(_log(eventcodes.abs() + 1.0), 4), 4), 12))
def cg_f099_sec_8k_event_density_core83_3rd_v084_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(_to_num(eventcodes), 4), 4), 12))
def cg_f099_sec_8k_event_density_core84_3rd_v085_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(_clean(eventcodes), 4), 4), 12))
def cg_f099_sec_8k_event_density_core85_3rd_v086_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(eventcodes * 1.0, 4), 4), 12))
def cg_f099_sec_8k_event_density_core86_3rd_v087_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(eventcodes * eventcodes, 4), 4), 12))
def cg_f099_sec_8k_event_density_core87_3rd_v088_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 12))
def cg_f099_sec_8k_event_density_core88_3rd_v089_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(_mean(eventcodes, 4), 4), 4), 12))
def cg_f099_sec_8k_event_density_core89_3rd_v090_signal(ticker, date, eventcodes):
    return _clean(_rank(_diff(_slope(_std(eventcodes, 4), 4), 4), 12))
def cg_f099_sec_8k_event_density_core90_3rd_v091_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core91_3rd_v092_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(eventcodes.abs(), 4), 4), 4))
def cg_f099_sec_8k_event_density_core92_3rd_v093_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core93_3rd_v094_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(_to_num(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core94_3rd_v095_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(_clean(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core95_3rd_v096_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(eventcodes * 1.0, 4), 4), 4))
def cg_f099_sec_8k_event_density_core96_3rd_v097_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(eventcodes * eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core97_3rd_v098_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core98_3rd_v099_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(_mean(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core99_3rd_v100_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_diff(_std(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core100_3rd_v101_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(eventcodes, 4), 8), 4))
def cg_f099_sec_8k_event_density_core101_3rd_v102_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(eventcodes.abs(), 4), 8), 4))
def cg_f099_sec_8k_event_density_core102_3rd_v103_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(_log(eventcodes.abs() + 1.0), 4), 8), 4))
def cg_f099_sec_8k_event_density_core103_3rd_v104_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(_to_num(eventcodes), 4), 8), 4))
def cg_f099_sec_8k_event_density_core104_3rd_v105_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(_clean(eventcodes), 4), 8), 4))
def cg_f099_sec_8k_event_density_core105_3rd_v106_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(eventcodes * 1.0, 4), 8), 4))
def cg_f099_sec_8k_event_density_core106_3rd_v107_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(eventcodes * eventcodes, 4), 8), 4))
def cg_f099_sec_8k_event_density_core107_3rd_v108_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 8), 4))
def cg_f099_sec_8k_event_density_core108_3rd_v109_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(_mean(eventcodes, 4), 4), 8), 4))
def cg_f099_sec_8k_event_density_core109_3rd_v110_signal(ticker, date, eventcodes):
    return _clean(_mean(_slope(_diff(_std(eventcodes, 4), 4), 8), 4))
def cg_f099_sec_8k_event_density_core110_3rd_v111_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core111_3rd_v112_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(eventcodes.abs(), 4), 4), 4))
def cg_f099_sec_8k_event_density_core112_3rd_v113_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(_log(eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core113_3rd_v114_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(_to_num(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core114_3rd_v115_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(_clean(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core115_3rd_v116_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(eventcodes * 1.0, 4), 4), 4))
def cg_f099_sec_8k_event_density_core116_3rd_v117_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(eventcodes * eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core117_3rd_v118_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core118_3rd_v119_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(_mean(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core119_3rd_v120_signal(ticker, date, eventcodes):
    return _clean(_mean(_diff(_slope(_std(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core120_3rd_v121_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core121_3rd_v122_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(eventcodes.abs(), 4), 4), 4))
def cg_f099_sec_8k_event_density_core122_3rd_v123_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core123_3rd_v124_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(_to_num(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core124_3rd_v125_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(_clean(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core125_3rd_v126_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(eventcodes * 1.0, 4), 4), 4))
def cg_f099_sec_8k_event_density_core126_3rd_v127_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(eventcodes * eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core127_3rd_v128_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core128_3rd_v129_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(_mean(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core129_3rd_v130_signal(ticker, date, eventcodes):
    return _clean(_slope(_diff(_diff(_std(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core130_3rd_v131_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core131_3rd_v132_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(eventcodes.abs(), 4), 4), 4))
def cg_f099_sec_8k_event_density_core132_3rd_v133_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core133_3rd_v134_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(_to_num(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core134_3rd_v135_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(_clean(eventcodes), 4), 4), 4))
def cg_f099_sec_8k_event_density_core135_3rd_v136_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(eventcodes * 1.0, 4), 4), 4))
def cg_f099_sec_8k_event_density_core136_3rd_v137_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(eventcodes * eventcodes, 4), 4), 4))
def cg_f099_sec_8k_event_density_core137_3rd_v138_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 4))
def cg_f099_sec_8k_event_density_core138_3rd_v139_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(_mean(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core139_3rd_v140_signal(ticker, date, eventcodes):
    return _clean(_diff(_diff(_diff(_std(eventcodes, 4), 4), 4), 4))
def cg_f099_sec_8k_event_density_core140_3rd_v141_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core141_3rd_v142_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(eventcodes.abs(), 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core142_3rd_v143_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(_log(eventcodes.abs() + 1.0), 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core143_3rd_v144_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(_to_num(eventcodes), 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core144_3rd_v145_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(_clean(eventcodes), 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core145_3rd_v146_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(eventcodes * 1.0, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core146_3rd_v147_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(eventcodes * eventcodes, 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core147_3rd_v148_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(_safe_div(1.0, eventcodes.abs() + 1.0), 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core148_3rd_v149_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(_mean(eventcodes, 4), 4), 4), 4), 8))
def cg_f099_sec_8k_event_density_core149_3rd_v150_signal(ticker, date, eventcodes):
    return _clean(_z(_slope(_diff(_diff(_std(eventcodes, 4), 4), 4), 4), 8))