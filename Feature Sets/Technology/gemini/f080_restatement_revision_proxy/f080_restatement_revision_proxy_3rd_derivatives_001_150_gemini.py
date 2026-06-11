import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f080_restatement_revision_proxy_core00_3rd_v001_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core01_3rd_v002_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_to_num(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core02_3rd_v003_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core03_3rd_v004_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_event_flag(dimension), 4), 4))
def cg_f080_restatement_revision_proxy_core04_3rd_v005_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_event_count(datekey, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core05_3rd_v006_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_event_count(lastupdated, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core06_3rd_v007_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_event_rate(reportperiod, 8), 4), 4))
def cg_f080_restatement_revision_proxy_core07_3rd_v008_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core08_3rd_v009_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core09_3rd_v010_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_event_flag(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core10_3rd_v011_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_to_num(datekey), 4), 8))
def cg_f080_restatement_revision_proxy_core11_3rd_v012_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_to_num(lastupdated), 4), 8))
def cg_f080_restatement_revision_proxy_core12_3rd_v013_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_to_num(reportperiod), 4), 8))
def cg_f080_restatement_revision_proxy_core13_3rd_v014_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_event_flag(dimension), 4), 8))
def cg_f080_restatement_revision_proxy_core14_3rd_v015_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_event_count(datekey, 4), 4), 8))
def cg_f080_restatement_revision_proxy_core15_3rd_v016_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_event_count(lastupdated, 4), 4), 8))
def cg_f080_restatement_revision_proxy_core16_3rd_v017_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_event_rate(reportperiod, 8), 4), 8))
def cg_f080_restatement_revision_proxy_core17_3rd_v018_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 8))
def cg_f080_restatement_revision_proxy_core18_3rd_v019_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 8))
def cg_f080_restatement_revision_proxy_core19_3rd_v020_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_event_flag(lastupdated), 4), 8))
def cg_f080_restatement_revision_proxy_core20_3rd_v021_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core21_3rd_v022_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_to_num(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core22_3rd_v023_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core23_3rd_v024_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_event_flag(dimension), 4), 4))
def cg_f080_restatement_revision_proxy_core24_3rd_v025_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_event_count(datekey, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core25_3rd_v026_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_event_count(lastupdated, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core26_3rd_v027_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_event_rate(reportperiod, 8), 4), 4))
def cg_f080_restatement_revision_proxy_core27_3rd_v028_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core28_3rd_v029_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core29_3rd_v030_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_slope(_event_flag(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core30_3rd_v031_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_to_num(datekey), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core31_3rd_v032_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_to_num(lastupdated), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core32_3rd_v033_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_to_num(reportperiod), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core33_3rd_v034_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_event_flag(dimension), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core34_3rd_v035_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_event_count(datekey, 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core35_3rd_v036_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_event_count(lastupdated, 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core36_3rd_v037_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_event_rate(reportperiod, 8), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core37_3rd_v038_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core38_3rd_v039_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core39_3rd_v040_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_diff(_event_flag(lastupdated), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core40_3rd_v041_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_to_num(datekey), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core41_3rd_v042_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_to_num(lastupdated), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core42_3rd_v043_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_to_num(reportperiod), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core43_3rd_v044_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_event_flag(dimension), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core44_3rd_v045_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_event_count(datekey, 4), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core45_3rd_v046_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_event_count(lastupdated, 4), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core46_3rd_v047_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_event_rate(reportperiod, 8), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core47_3rd_v048_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core48_3rd_v049_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core49_3rd_v050_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_event_flag(lastupdated), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core50_3rd_v051_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_to_num(datekey), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core51_3rd_v052_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_to_num(lastupdated), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core52_3rd_v053_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_to_num(reportperiod), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core53_3rd_v054_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_event_flag(dimension), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core54_3rd_v055_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_event_count(datekey, 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core55_3rd_v056_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_event_count(lastupdated, 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core56_3rd_v057_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_event_rate(reportperiod, 8), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core57_3rd_v058_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core58_3rd_v059_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core59_3rd_v060_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_slope(_event_flag(lastupdated), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core60_3rd_v061_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_to_num(datekey), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core61_3rd_v062_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_to_num(lastupdated), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core62_3rd_v063_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_to_num(reportperiod), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core63_3rd_v064_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_event_flag(dimension), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core64_3rd_v065_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_event_count(datekey, 4), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core65_3rd_v066_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_event_count(lastupdated, 4), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core66_3rd_v067_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_event_rate(reportperiod, 8), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core67_3rd_v068_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core68_3rd_v069_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core69_3rd_v070_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_diff(_event_flag(lastupdated), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core70_3rd_v071_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_to_num(datekey), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core71_3rd_v072_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_to_num(lastupdated), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core72_3rd_v073_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_to_num(reportperiod), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core73_3rd_v074_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_event_flag(dimension), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core74_3rd_v075_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_event_count(datekey, 4), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core75_3rd_v076_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_event_count(lastupdated, 4), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core76_3rd_v077_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_event_rate(reportperiod, 8), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core77_3rd_v078_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core78_3rd_v079_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core79_3rd_v080_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_diff(_event_flag(lastupdated), 4), 8), 12))
def cg_f080_restatement_revision_proxy_core80_3rd_v081_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_to_num(datekey), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core81_3rd_v082_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_to_num(lastupdated), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core82_3rd_v083_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_to_num(reportperiod), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core83_3rd_v084_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_event_flag(dimension), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core84_3rd_v085_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_event_count(datekey, 4), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core85_3rd_v086_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_event_count(lastupdated, 4), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core86_3rd_v087_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_event_rate(reportperiod, 8), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core87_3rd_v088_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core88_3rd_v089_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core89_3rd_v090_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_slope(_event_flag(lastupdated), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core90_3rd_v091_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core91_3rd_v092_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_to_num(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core92_3rd_v093_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core93_3rd_v094_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_event_flag(dimension), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core94_3rd_v095_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_event_count(datekey, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core95_3rd_v096_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_event_count(lastupdated, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core96_3rd_v097_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_event_rate(reportperiod, 8), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core97_3rd_v098_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core98_3rd_v099_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core99_3rd_v100_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_diff(_event_flag(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core100_3rd_v101_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_to_num(datekey), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core101_3rd_v102_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_to_num(lastupdated), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core102_3rd_v103_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_to_num(reportperiod), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core103_3rd_v104_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_event_flag(dimension), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core104_3rd_v105_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_event_count(datekey, 4), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core105_3rd_v106_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_event_count(lastupdated, 4), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core106_3rd_v107_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_event_rate(reportperiod, 8), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core107_3rd_v108_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core108_3rd_v109_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core109_3rd_v110_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_diff(_event_flag(lastupdated), 4), 8), 4))
def cg_f080_restatement_revision_proxy_core110_3rd_v111_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core111_3rd_v112_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_to_num(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core112_3rd_v113_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core113_3rd_v114_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_event_flag(dimension), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core114_3rd_v115_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_event_count(datekey, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core115_3rd_v116_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_event_count(lastupdated, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core116_3rd_v117_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_event_rate(reportperiod, 8), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core117_3rd_v118_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core118_3rd_v119_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core119_3rd_v120_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_slope(_event_flag(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core120_3rd_v121_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core121_3rd_v122_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_to_num(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core122_3rd_v123_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core123_3rd_v124_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_event_flag(dimension), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core124_3rd_v125_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_event_count(datekey, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core125_3rd_v126_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_event_count(lastupdated, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core126_3rd_v127_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_event_rate(reportperiod, 8), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core127_3rd_v128_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core128_3rd_v129_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core129_3rd_v130_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_diff(_diff(_event_flag(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core130_3rd_v131_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core131_3rd_v132_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_to_num(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core132_3rd_v133_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core133_3rd_v134_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_event_flag(dimension), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core134_3rd_v135_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_event_count(datekey, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core135_3rd_v136_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_event_count(lastupdated, 4), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core136_3rd_v137_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_event_rate(reportperiod, 8), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core137_3rd_v138_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core138_3rd_v139_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core139_3rd_v140_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_diff(_diff(_event_flag(lastupdated), 4), 4), 4))
def cg_f080_restatement_revision_proxy_core140_3rd_v141_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_to_num(datekey), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core141_3rd_v142_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastupdated), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core142_3rd_v143_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_to_num(reportperiod), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core143_3rd_v144_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_event_flag(dimension), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core144_3rd_v145_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_event_count(datekey, 4), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core145_3rd_v146_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_event_count(lastupdated, 4), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core146_3rd_v147_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_event_rate(reportperiod, 8), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core147_3rd_v148_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core148_3rd_v149_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core149_3rd_v150_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_diff(_diff(_event_flag(lastupdated), 4), 4), 4), 8))