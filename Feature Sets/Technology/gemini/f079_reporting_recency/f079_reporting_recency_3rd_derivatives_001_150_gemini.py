import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f079_reporting_recency_core00_3rd_v001_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_to_num(calendardate), 4), 4))
def cg_f079_reporting_recency_core01_3rd_v002_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_to_num(reportperiod), 4), 4))
def cg_f079_reporting_recency_core02_3rd_v003_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core03_3rd_v004_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_to_num(lastupdated), 4), 4))
def cg_f079_reporting_recency_core04_3rd_v005_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_event_flag(calendardate), 4), 4))
def cg_f079_reporting_recency_core05_3rd_v006_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_event_flag(reportperiod), 4), 4))
def cg_f079_reporting_recency_core06_3rd_v007_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_event_count(datekey, 4), 4), 4))
def cg_f079_reporting_recency_core07_3rd_v008_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_event_rate(lastupdated, 8), 4), 4))
def cg_f079_reporting_recency_core08_3rd_v009_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core09_3rd_v010_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4))
def cg_f079_reporting_recency_core10_3rd_v011_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_to_num(calendardate), 4), 8))
def cg_f079_reporting_recency_core11_3rd_v012_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_to_num(reportperiod), 4), 8))
def cg_f079_reporting_recency_core12_3rd_v013_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_to_num(datekey), 4), 8))
def cg_f079_reporting_recency_core13_3rd_v014_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_to_num(lastupdated), 4), 8))
def cg_f079_reporting_recency_core14_3rd_v015_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_event_flag(calendardate), 4), 8))
def cg_f079_reporting_recency_core15_3rd_v016_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_event_flag(reportperiod), 4), 8))
def cg_f079_reporting_recency_core16_3rd_v017_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_event_count(datekey, 4), 4), 8))
def cg_f079_reporting_recency_core17_3rd_v018_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_event_rate(lastupdated, 8), 4), 8))
def cg_f079_reporting_recency_core18_3rd_v019_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_autocorr(_to_num(datekey), 4), 4), 8))
def cg_f079_reporting_recency_core19_3rd_v020_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_to_num(lastupdated), 1), 4), 8))
def cg_f079_reporting_recency_core20_3rd_v021_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_to_num(calendardate), 4), 4))
def cg_f079_reporting_recency_core21_3rd_v022_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_to_num(reportperiod), 4), 4))
def cg_f079_reporting_recency_core22_3rd_v023_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_to_num(datekey), 4), 4))
def cg_f079_reporting_recency_core23_3rd_v024_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_to_num(lastupdated), 4), 4))
def cg_f079_reporting_recency_core24_3rd_v025_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_event_flag(calendardate), 4), 4))
def cg_f079_reporting_recency_core25_3rd_v026_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_event_flag(reportperiod), 4), 4))
def cg_f079_reporting_recency_core26_3rd_v027_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_event_count(datekey, 4), 4), 4))
def cg_f079_reporting_recency_core27_3rd_v028_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_event_rate(lastupdated, 8), 4), 4))
def cg_f079_reporting_recency_core28_3rd_v029_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_autocorr(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core29_3rd_v030_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_slope(_diff(_to_num(lastupdated), 1), 4), 4))
def cg_f079_reporting_recency_core30_3rd_v031_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_to_num(calendardate), 4), 4), 8))
def cg_f079_reporting_recency_core31_3rd_v032_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_to_num(reportperiod), 4), 4), 8))
def cg_f079_reporting_recency_core32_3rd_v033_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_to_num(datekey), 4), 4), 8))
def cg_f079_reporting_recency_core33_3rd_v034_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_to_num(lastupdated), 4), 4), 8))
def cg_f079_reporting_recency_core34_3rd_v035_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_event_flag(calendardate), 4), 4), 8))
def cg_f079_reporting_recency_core35_3rd_v036_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_event_flag(reportperiod), 4), 4), 8))
def cg_f079_reporting_recency_core36_3rd_v037_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_event_count(datekey, 4), 4), 4), 8))
def cg_f079_reporting_recency_core37_3rd_v038_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_event_rate(lastupdated, 8), 4), 4), 8))
def cg_f079_reporting_recency_core38_3rd_v039_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4), 8))
def cg_f079_reporting_recency_core39_3rd_v040_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4), 8))
def cg_f079_reporting_recency_core40_3rd_v041_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_to_num(calendardate), 4), 8), 12))
def cg_f079_reporting_recency_core41_3rd_v042_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_to_num(reportperiod), 4), 8), 12))
def cg_f079_reporting_recency_core42_3rd_v043_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_to_num(datekey), 4), 8), 12))
def cg_f079_reporting_recency_core43_3rd_v044_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_to_num(lastupdated), 4), 8), 12))
def cg_f079_reporting_recency_core44_3rd_v045_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_event_flag(calendardate), 4), 8), 12))
def cg_f079_reporting_recency_core45_3rd_v046_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_event_flag(reportperiod), 4), 8), 12))
def cg_f079_reporting_recency_core46_3rd_v047_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_event_count(datekey, 4), 4), 8), 12))
def cg_f079_reporting_recency_core47_3rd_v048_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_event_rate(lastupdated, 8), 4), 8), 12))
def cg_f079_reporting_recency_core48_3rd_v049_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_autocorr(_to_num(datekey), 4), 4), 8), 12))
def cg_f079_reporting_recency_core49_3rd_v050_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastupdated), 1), 4), 8), 12))
def cg_f079_reporting_recency_core50_3rd_v051_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_to_num(calendardate), 4), 4), 8))
def cg_f079_reporting_recency_core51_3rd_v052_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_to_num(reportperiod), 4), 4), 8))
def cg_f079_reporting_recency_core52_3rd_v053_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_to_num(datekey), 4), 4), 8))
def cg_f079_reporting_recency_core53_3rd_v054_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_to_num(lastupdated), 4), 4), 8))
def cg_f079_reporting_recency_core54_3rd_v055_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_event_flag(calendardate), 4), 4), 8))
def cg_f079_reporting_recency_core55_3rd_v056_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_event_flag(reportperiod), 4), 4), 8))
def cg_f079_reporting_recency_core56_3rd_v057_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_event_count(datekey, 4), 4), 4), 8))
def cg_f079_reporting_recency_core57_3rd_v058_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_event_rate(lastupdated, 8), 4), 4), 8))
def cg_f079_reporting_recency_core58_3rd_v059_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_autocorr(_to_num(datekey), 4), 4), 4), 8))
def cg_f079_reporting_recency_core59_3rd_v060_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_diff(_slope(_diff(_to_num(lastupdated), 1), 4), 4), 8))
def cg_f079_reporting_recency_core60_3rd_v061_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_to_num(calendardate), 4), 4), 12))
def cg_f079_reporting_recency_core61_3rd_v062_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_to_num(reportperiod), 4), 4), 12))
def cg_f079_reporting_recency_core62_3rd_v063_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_to_num(datekey), 4), 4), 12))
def cg_f079_reporting_recency_core63_3rd_v064_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_to_num(lastupdated), 4), 4), 12))
def cg_f079_reporting_recency_core64_3rd_v065_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_event_flag(calendardate), 4), 4), 12))
def cg_f079_reporting_recency_core65_3rd_v066_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_event_flag(reportperiod), 4), 4), 12))
def cg_f079_reporting_recency_core66_3rd_v067_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_event_count(datekey, 4), 4), 4), 12))
def cg_f079_reporting_recency_core67_3rd_v068_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_event_rate(lastupdated, 8), 4), 4), 12))
def cg_f079_reporting_recency_core68_3rd_v069_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4), 12))
def cg_f079_reporting_recency_core69_3rd_v070_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4), 12))
def cg_f079_reporting_recency_core70_3rd_v071_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_to_num(calendardate), 4), 8), 12))
def cg_f079_reporting_recency_core71_3rd_v072_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_to_num(reportperiod), 4), 8), 12))
def cg_f079_reporting_recency_core72_3rd_v073_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_to_num(datekey), 4), 8), 12))
def cg_f079_reporting_recency_core73_3rd_v074_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_to_num(lastupdated), 4), 8), 12))
def cg_f079_reporting_recency_core74_3rd_v075_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_event_flag(calendardate), 4), 8), 12))
def cg_f079_reporting_recency_core75_3rd_v076_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_event_flag(reportperiod), 4), 8), 12))
def cg_f079_reporting_recency_core76_3rd_v077_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_event_count(datekey, 4), 4), 8), 12))
def cg_f079_reporting_recency_core77_3rd_v078_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_event_rate(lastupdated, 8), 4), 8), 12))
def cg_f079_reporting_recency_core78_3rd_v079_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_autocorr(_to_num(datekey), 4), 4), 8), 12))
def cg_f079_reporting_recency_core79_3rd_v080_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_slope(_diff(_diff(_to_num(lastupdated), 1), 4), 8), 12))
def cg_f079_reporting_recency_core80_3rd_v081_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_to_num(calendardate), 4), 4), 12))
def cg_f079_reporting_recency_core81_3rd_v082_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_to_num(reportperiod), 4), 4), 12))
def cg_f079_reporting_recency_core82_3rd_v083_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_to_num(datekey), 4), 4), 12))
def cg_f079_reporting_recency_core83_3rd_v084_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_to_num(lastupdated), 4), 4), 12))
def cg_f079_reporting_recency_core84_3rd_v085_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_event_flag(calendardate), 4), 4), 12))
def cg_f079_reporting_recency_core85_3rd_v086_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_event_flag(reportperiod), 4), 4), 12))
def cg_f079_reporting_recency_core86_3rd_v087_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_event_count(datekey, 4), 4), 4), 12))
def cg_f079_reporting_recency_core87_3rd_v088_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_event_rate(lastupdated, 8), 4), 4), 12))
def cg_f079_reporting_recency_core88_3rd_v089_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_autocorr(_to_num(datekey), 4), 4), 4), 12))
def cg_f079_reporting_recency_core89_3rd_v090_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_rank(_diff(_slope(_diff(_to_num(lastupdated), 1), 4), 4), 12))
def cg_f079_reporting_recency_core90_3rd_v091_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_to_num(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core91_3rd_v092_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_to_num(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core92_3rd_v093_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core93_3rd_v094_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_to_num(lastupdated), 4), 4), 4))
def cg_f079_reporting_recency_core94_3rd_v095_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_event_flag(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core95_3rd_v096_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_event_flag(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core96_3rd_v097_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_event_count(datekey, 4), 4), 4), 4))
def cg_f079_reporting_recency_core97_3rd_v098_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_event_rate(lastupdated, 8), 4), 4), 4))
def cg_f079_reporting_recency_core98_3rd_v099_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4), 4))
def cg_f079_reporting_recency_core99_3rd_v100_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4), 4))
def cg_f079_reporting_recency_core100_3rd_v101_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_to_num(calendardate), 4), 8), 4))
def cg_f079_reporting_recency_core101_3rd_v102_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_to_num(reportperiod), 4), 8), 4))
def cg_f079_reporting_recency_core102_3rd_v103_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_to_num(datekey), 4), 8), 4))
def cg_f079_reporting_recency_core103_3rd_v104_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_to_num(lastupdated), 4), 8), 4))
def cg_f079_reporting_recency_core104_3rd_v105_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_event_flag(calendardate), 4), 8), 4))
def cg_f079_reporting_recency_core105_3rd_v106_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_event_flag(reportperiod), 4), 8), 4))
def cg_f079_reporting_recency_core106_3rd_v107_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_event_count(datekey, 4), 4), 8), 4))
def cg_f079_reporting_recency_core107_3rd_v108_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_event_rate(lastupdated, 8), 4), 8), 4))
def cg_f079_reporting_recency_core108_3rd_v109_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_autocorr(_to_num(datekey), 4), 4), 8), 4))
def cg_f079_reporting_recency_core109_3rd_v110_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_slope(_diff(_diff(_to_num(lastupdated), 1), 4), 8), 4))
def cg_f079_reporting_recency_core110_3rd_v111_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_to_num(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core111_3rd_v112_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_to_num(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core112_3rd_v113_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core113_3rd_v114_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_to_num(lastupdated), 4), 4), 4))
def cg_f079_reporting_recency_core114_3rd_v115_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_event_flag(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core115_3rd_v116_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_event_flag(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core116_3rd_v117_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_event_count(datekey, 4), 4), 4), 4))
def cg_f079_reporting_recency_core117_3rd_v118_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_event_rate(lastupdated, 8), 4), 4), 4))
def cg_f079_reporting_recency_core118_3rd_v119_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_autocorr(_to_num(datekey), 4), 4), 4), 4))
def cg_f079_reporting_recency_core119_3rd_v120_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_mean(_diff(_slope(_diff(_to_num(lastupdated), 1), 4), 4), 4))
def cg_f079_reporting_recency_core120_3rd_v121_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_to_num(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core121_3rd_v122_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_to_num(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core122_3rd_v123_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core123_3rd_v124_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_to_num(lastupdated), 4), 4), 4))
def cg_f079_reporting_recency_core124_3rd_v125_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_event_flag(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core125_3rd_v126_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_event_flag(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core126_3rd_v127_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_event_count(datekey, 4), 4), 4), 4))
def cg_f079_reporting_recency_core127_3rd_v128_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_event_rate(lastupdated, 8), 4), 4), 4))
def cg_f079_reporting_recency_core128_3rd_v129_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4), 4))
def cg_f079_reporting_recency_core129_3rd_v130_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_slope(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4), 4))
def cg_f079_reporting_recency_core130_3rd_v131_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_to_num(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core131_3rd_v132_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_to_num(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core132_3rd_v133_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_to_num(datekey), 4), 4), 4))
def cg_f079_reporting_recency_core133_3rd_v134_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_to_num(lastupdated), 4), 4), 4))
def cg_f079_reporting_recency_core134_3rd_v135_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_event_flag(calendardate), 4), 4), 4))
def cg_f079_reporting_recency_core135_3rd_v136_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_event_flag(reportperiod), 4), 4), 4))
def cg_f079_reporting_recency_core136_3rd_v137_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_event_count(datekey, 4), 4), 4), 4))
def cg_f079_reporting_recency_core137_3rd_v138_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_event_rate(lastupdated, 8), 4), 4), 4))
def cg_f079_reporting_recency_core138_3rd_v139_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4), 4))
def cg_f079_reporting_recency_core139_3rd_v140_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_diff(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4), 4))
def cg_f079_reporting_recency_core140_3rd_v141_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_to_num(calendardate), 4), 4), 4), 8))
def cg_f079_reporting_recency_core141_3rd_v142_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_to_num(reportperiod), 4), 4), 4), 8))
def cg_f079_reporting_recency_core142_3rd_v143_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_to_num(datekey), 4), 4), 4), 8))
def cg_f079_reporting_recency_core143_3rd_v144_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastupdated), 4), 4), 4), 8))
def cg_f079_reporting_recency_core144_3rd_v145_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_event_flag(calendardate), 4), 4), 4), 8))
def cg_f079_reporting_recency_core145_3rd_v146_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_event_flag(reportperiod), 4), 4), 4), 8))
def cg_f079_reporting_recency_core146_3rd_v147_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_event_count(datekey, 4), 4), 4), 4), 8))
def cg_f079_reporting_recency_core147_3rd_v148_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_event_rate(lastupdated, 8), 4), 4), 4), 8))
def cg_f079_reporting_recency_core148_3rd_v149_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_autocorr(_to_num(datekey), 4), 4), 4), 4), 8))
def cg_f079_reporting_recency_core149_3rd_v150_signal(calendardate, reportperiod, datekey, lastupdated):
    return _clean(_z(_slope(_diff(_diff(_diff(_to_num(lastupdated), 1), 4), 4), 4), 8))