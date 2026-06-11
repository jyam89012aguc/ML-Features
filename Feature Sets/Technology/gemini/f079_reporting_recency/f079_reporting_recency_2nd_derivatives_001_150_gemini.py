import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f079_reporting_recency_core00_2nd_v001_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(calendardate), 4))
def cg_f079_reporting_recency_core01_2nd_v002_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(reportperiod), 4))
def cg_f079_reporting_recency_core02_2nd_v003_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(datekey), 4))
def cg_f079_reporting_recency_core03_2nd_v004_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(lastupdated), 4))
def cg_f079_reporting_recency_core04_2nd_v005_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_flag(calendardate), 4))
def cg_f079_reporting_recency_core05_2nd_v006_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_flag(reportperiod), 4))
def cg_f079_reporting_recency_core06_2nd_v007_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_count(datekey, 4), 4))
def cg_f079_reporting_recency_core07_2nd_v008_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_rate(lastupdated, 8), 4))
def cg_f079_reporting_recency_core08_2nd_v009_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_autocorr(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core09_2nd_v010_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_to_num(lastupdated), 1), 4))
def cg_f079_reporting_recency_core10_2nd_v011_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(calendardate), 8))
def cg_f079_reporting_recency_core11_2nd_v012_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(reportperiod), 8))
def cg_f079_reporting_recency_core12_2nd_v013_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(datekey), 8))
def cg_f079_reporting_recency_core13_2nd_v014_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_to_num(lastupdated), 8))
def cg_f079_reporting_recency_core14_2nd_v015_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_flag(calendardate), 8))
def cg_f079_reporting_recency_core15_2nd_v016_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_flag(reportperiod), 8))
def cg_f079_reporting_recency_core16_2nd_v017_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_count(datekey, 4), 8))
def cg_f079_reporting_recency_core17_2nd_v018_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_event_rate(lastupdated, 8), 8))
def cg_f079_reporting_recency_core18_2nd_v019_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_autocorr(_to_num(datekey), 4), 8))
def cg_f079_reporting_recency_core19_2nd_v020_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_to_num(lastupdated), 1), 8))
def cg_f079_reporting_recency_core20_2nd_v021_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(calendardate), 4))
def cg_f079_reporting_recency_core21_2nd_v022_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(reportperiod), 4))
def cg_f079_reporting_recency_core22_2nd_v023_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(datekey), 4))
def cg_f079_reporting_recency_core23_2nd_v024_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_to_num(lastupdated), 4))
def cg_f079_reporting_recency_core24_2nd_v025_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_event_flag(calendardate), 4))
def cg_f079_reporting_recency_core25_2nd_v026_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_event_flag(reportperiod), 4))
def cg_f079_reporting_recency_core26_2nd_v027_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_event_count(datekey, 4), 4))
def cg_f079_reporting_recency_core27_2nd_v028_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_event_rate(lastupdated, 8), 4))
def cg_f079_reporting_recency_core28_2nd_v029_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_autocorr(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core29_2nd_v030_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_to_num(lastupdated), 1), 4))
def cg_f079_reporting_recency_core30_2nd_v031_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(calendardate), 4), 8))
def cg_f079_reporting_recency_core31_2nd_v032_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(reportperiod), 4), 8))
def cg_f079_reporting_recency_core32_2nd_v033_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(datekey), 4), 8))
def cg_f079_reporting_recency_core33_2nd_v034_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(lastupdated), 4), 8))
def cg_f079_reporting_recency_core34_2nd_v035_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_flag(calendardate), 4), 8))
def cg_f079_reporting_recency_core35_2nd_v036_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_flag(reportperiod), 4), 8))
def cg_f079_reporting_recency_core36_2nd_v037_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_count(datekey, 4), 4), 8))
def cg_f079_reporting_recency_core37_2nd_v038_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_rate(lastupdated, 8), 4), 8))
def cg_f079_reporting_recency_core38_2nd_v039_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_autocorr(_to_num(datekey), 4), 4), 8))
def cg_f079_reporting_recency_core39_2nd_v040_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_to_num(lastupdated), 1), 4), 8))
def cg_f079_reporting_recency_core40_2nd_v041_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(calendardate), 8), 12))
def cg_f079_reporting_recency_core41_2nd_v042_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(reportperiod), 8), 12))
def cg_f079_reporting_recency_core42_2nd_v043_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(datekey), 8), 12))
def cg_f079_reporting_recency_core43_2nd_v044_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_to_num(lastupdated), 8), 12))
def cg_f079_reporting_recency_core44_2nd_v045_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_flag(calendardate), 8), 12))
def cg_f079_reporting_recency_core45_2nd_v046_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_flag(reportperiod), 8), 12))
def cg_f079_reporting_recency_core46_2nd_v047_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_count(datekey, 4), 8), 12))
def cg_f079_reporting_recency_core47_2nd_v048_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_event_rate(lastupdated, 8), 8), 12))
def cg_f079_reporting_recency_core48_2nd_v049_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_autocorr(_to_num(datekey), 4), 8), 12))
def cg_f079_reporting_recency_core49_2nd_v050_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_to_num(lastupdated), 1), 8), 12))
def cg_f079_reporting_recency_core50_2nd_v051_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_to_num(calendardate), 4), 8))
def cg_f079_reporting_recency_core51_2nd_v052_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_to_num(reportperiod), 4), 8))
def cg_f079_reporting_recency_core52_2nd_v053_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_to_num(datekey), 4), 8))
def cg_f079_reporting_recency_core53_2nd_v054_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_to_num(lastupdated), 4), 8))
def cg_f079_reporting_recency_core54_2nd_v055_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_event_flag(calendardate), 4), 8))
def cg_f079_reporting_recency_core55_2nd_v056_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_event_flag(reportperiod), 4), 8))
def cg_f079_reporting_recency_core56_2nd_v057_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_event_count(datekey, 4), 4), 8))
def cg_f079_reporting_recency_core57_2nd_v058_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_event_rate(lastupdated, 8), 4), 8))
def cg_f079_reporting_recency_core58_2nd_v059_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_autocorr(_to_num(datekey), 4), 4), 8))
def cg_f079_reporting_recency_core59_2nd_v060_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_to_num(lastupdated), 1), 4), 8))
def cg_f079_reporting_recency_core60_2nd_v061_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_to_num(calendardate), 4), 12))
def cg_f079_reporting_recency_core61_2nd_v062_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_to_num(reportperiod), 4), 12))
def cg_f079_reporting_recency_core62_2nd_v063_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_to_num(datekey), 4), 12))
def cg_f079_reporting_recency_core63_2nd_v064_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_to_num(lastupdated), 4), 12))
def cg_f079_reporting_recency_core64_2nd_v065_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_event_flag(calendardate), 4), 12))
def cg_f079_reporting_recency_core65_2nd_v066_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_event_flag(reportperiod), 4), 12))
def cg_f079_reporting_recency_core66_2nd_v067_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_event_count(datekey, 4), 4), 12))
def cg_f079_reporting_recency_core67_2nd_v068_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_event_rate(lastupdated, 8), 4), 12))
def cg_f079_reporting_recency_core68_2nd_v069_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_autocorr(_to_num(datekey), 4), 4), 12))
def cg_f079_reporting_recency_core69_2nd_v070_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_to_num(lastupdated), 1), 4), 12))
def cg_f079_reporting_recency_core70_2nd_v071_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_to_num(calendardate), 4), 12))
def cg_f079_reporting_recency_core71_2nd_v072_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_to_num(reportperiod), 4), 12))
def cg_f079_reporting_recency_core72_2nd_v073_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_to_num(datekey), 4), 12))
def cg_f079_reporting_recency_core73_2nd_v074_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_to_num(lastupdated), 4), 12))
def cg_f079_reporting_recency_core74_2nd_v075_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_event_flag(calendardate), 4), 12))
def cg_f079_reporting_recency_core75_2nd_v076_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_event_flag(reportperiod), 4), 12))
def cg_f079_reporting_recency_core76_2nd_v077_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_event_count(datekey, 4), 4), 12))
def cg_f079_reporting_recency_core77_2nd_v078_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_event_rate(lastupdated, 8), 4), 12))
def cg_f079_reporting_recency_core78_2nd_v079_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_autocorr(_to_num(datekey), 4), 4), 12))
def cg_f079_reporting_recency_core79_2nd_v080_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_to_num(lastupdated), 1), 4), 12))
def cg_f079_reporting_recency_core80_2nd_v081_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_to_num(calendardate), 4), 4))
def cg_f079_reporting_recency_core81_2nd_v082_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_to_num(reportperiod), 4), 4))
def cg_f079_reporting_recency_core82_2nd_v083_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core83_2nd_v084_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_to_num(lastupdated), 4), 4))
def cg_f079_reporting_recency_core84_2nd_v085_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_event_flag(calendardate), 4), 4))
def cg_f079_reporting_recency_core85_2nd_v086_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_event_flag(reportperiod), 4), 4))
def cg_f079_reporting_recency_core86_2nd_v087_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_event_count(datekey, 4), 4), 4))
def cg_f079_reporting_recency_core87_2nd_v088_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_event_rate(lastupdated, 8), 4), 4))
def cg_f079_reporting_recency_core88_2nd_v089_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_autocorr(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core89_2nd_v090_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_to_num(lastupdated), 1), 4), 4))
def cg_f079_reporting_recency_core90_2nd_v091_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_to_num(calendardate), 4), 4))
def cg_f079_reporting_recency_core91_2nd_v092_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_to_num(reportperiod), 4), 4))
def cg_f079_reporting_recency_core92_2nd_v093_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core93_2nd_v094_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_to_num(lastupdated), 4), 4))
def cg_f079_reporting_recency_core94_2nd_v095_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_event_flag(calendardate), 4), 4))
def cg_f079_reporting_recency_core95_2nd_v096_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_event_flag(reportperiod), 4), 4))
def cg_f079_reporting_recency_core96_2nd_v097_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_event_count(datekey, 4), 4), 4))
def cg_f079_reporting_recency_core97_2nd_v098_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_event_rate(lastupdated, 8), 4), 4))
def cg_f079_reporting_recency_core98_2nd_v099_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_autocorr(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core99_2nd_v100_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_to_num(lastupdated), 1), 4), 4))
def cg_f079_reporting_recency_core100_2nd_v101_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(calendardate), 4), 4))
def cg_f079_reporting_recency_core101_2nd_v102_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(reportperiod), 4), 4))
def cg_f079_reporting_recency_core102_2nd_v103_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core103_2nd_v104_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(lastupdated), 4), 4))
def cg_f079_reporting_recency_core104_2nd_v105_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_flag(calendardate), 4), 4))
def cg_f079_reporting_recency_core105_2nd_v106_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_flag(reportperiod), 4), 4))
def cg_f079_reporting_recency_core106_2nd_v107_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_count(datekey, 4), 4), 4))
def cg_f079_reporting_recency_core107_2nd_v108_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_rate(lastupdated, 8), 4), 4))
def cg_f079_reporting_recency_core108_2nd_v109_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_autocorr(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core109_2nd_v110_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_diff(_to_num(lastupdated), 1), 4), 4))
def cg_f079_reporting_recency_core110_2nd_v111_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(calendardate), 8), 8))
def cg_f079_reporting_recency_core111_2nd_v112_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(reportperiod), 8), 8))
def cg_f079_reporting_recency_core112_2nd_v113_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(datekey), 8), 8))
def cg_f079_reporting_recency_core113_2nd_v114_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_to_num(lastupdated), 8), 8))
def cg_f079_reporting_recency_core114_2nd_v115_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_flag(calendardate), 8), 8))
def cg_f079_reporting_recency_core115_2nd_v116_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_flag(reportperiod), 8), 8))
def cg_f079_reporting_recency_core116_2nd_v117_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_count(datekey, 4), 8), 8))
def cg_f079_reporting_recency_core117_2nd_v118_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_event_rate(lastupdated, 8), 8), 8))
def cg_f079_reporting_recency_core118_2nd_v119_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_autocorr(_to_num(datekey), 4), 8), 8))
def cg_f079_reporting_recency_core119_2nd_v120_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_mean(_diff(_to_num(lastupdated), 1), 8), 8))
def cg_f079_reporting_recency_core120_2nd_v121_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_to_num(calendardate), 4), 4))
def cg_f079_reporting_recency_core121_2nd_v122_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_to_num(reportperiod), 4), 4))
def cg_f079_reporting_recency_core122_2nd_v123_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core123_2nd_v124_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_to_num(lastupdated), 4), 4))
def cg_f079_reporting_recency_core124_2nd_v125_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_event_flag(calendardate), 4), 4))
def cg_f079_reporting_recency_core125_2nd_v126_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_event_flag(reportperiod), 4), 4))
def cg_f079_reporting_recency_core126_2nd_v127_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_event_count(datekey, 4), 4), 4))
def cg_f079_reporting_recency_core127_2nd_v128_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_event_rate(lastupdated, 8), 4), 4))
def cg_f079_reporting_recency_core128_2nd_v129_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_autocorr(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core129_2nd_v130_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_mean(_diff(_to_num(lastupdated), 1), 4), 4))
def cg_f079_reporting_recency_core130_2nd_v131_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_to_num(calendardate), 4), 4), 8))
def cg_f079_reporting_recency_core131_2nd_v132_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_to_num(reportperiod), 4), 4), 8))
def cg_f079_reporting_recency_core132_2nd_v133_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_to_num(datekey), 4), 4), 8))
def cg_f079_reporting_recency_core133_2nd_v134_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_to_num(lastupdated), 4), 4), 8))
def cg_f079_reporting_recency_core134_2nd_v135_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_event_flag(calendardate), 4), 4), 8))
def cg_f079_reporting_recency_core135_2nd_v136_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_event_flag(reportperiod), 4), 4), 8))
def cg_f079_reporting_recency_core136_2nd_v137_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_event_count(datekey, 4), 4), 4), 8))
def cg_f079_reporting_recency_core137_2nd_v138_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_event_rate(lastupdated, 8), 4), 4), 8))
def cg_f079_reporting_recency_core138_2nd_v139_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_autocorr(_to_num(datekey), 4), 4), 4), 8))
def cg_f079_reporting_recency_core139_2nd_v140_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_mean(_diff(_to_num(lastupdated), 1), 4), 4), 8))
def cg_f079_reporting_recency_core140_2nd_v141_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_to_num(calendardate), 4), 4), 12))
def cg_f079_reporting_recency_core141_2nd_v142_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_to_num(reportperiod), 4), 4), 12))
def cg_f079_reporting_recency_core142_2nd_v143_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_to_num(datekey), 4), 4), 12))
def cg_f079_reporting_recency_core143_2nd_v144_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_to_num(lastupdated), 4), 4), 12))
def cg_f079_reporting_recency_core144_2nd_v145_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_event_flag(calendardate), 4), 4), 12))
def cg_f079_reporting_recency_core145_2nd_v146_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_event_flag(reportperiod), 4), 4), 12))
def cg_f079_reporting_recency_core146_2nd_v147_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_event_count(datekey, 4), 4), 4), 12))
def cg_f079_reporting_recency_core147_2nd_v148_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_event_rate(lastupdated, 8), 4), 4), 12))
def cg_f079_reporting_recency_core148_2nd_v149_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_autocorr(_to_num(datekey), 4), 4), 4), 12))
def cg_f079_reporting_recency_core149_2nd_v150_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_mean(_diff(_to_num(lastupdated), 1), 4), 4), 12))