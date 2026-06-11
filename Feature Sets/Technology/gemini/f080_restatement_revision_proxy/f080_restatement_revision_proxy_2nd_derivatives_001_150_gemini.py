import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f080_restatement_revision_proxy_core00_2nd_v001_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(datekey), 4))
def cg_f080_restatement_revision_proxy_core01_2nd_v002_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(lastupdated), 4))
def cg_f080_restatement_revision_proxy_core02_2nd_v003_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(reportperiod), 4))
def cg_f080_restatement_revision_proxy_core03_2nd_v004_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_flag(dimension), 4))
def cg_f080_restatement_revision_proxy_core04_2nd_v005_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_count(datekey, 4), 4))
def cg_f080_restatement_revision_proxy_core05_2nd_v006_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_count(lastupdated, 4), 4))
def cg_f080_restatement_revision_proxy_core06_2nd_v007_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_rate(reportperiod, 8), 4))
def cg_f080_restatement_revision_proxy_core07_2nd_v008_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(lastupdated) - _to_num(datekey), 4))
def cg_f080_restatement_revision_proxy_core08_2nd_v009_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(datekey) - _to_num(reportperiod), 4))
def cg_f080_restatement_revision_proxy_core09_2nd_v010_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_flag(lastupdated), 4))
def cg_f080_restatement_revision_proxy_core10_2nd_v011_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(datekey), 8))
def cg_f080_restatement_revision_proxy_core11_2nd_v012_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(lastupdated), 8))
def cg_f080_restatement_revision_proxy_core12_2nd_v013_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(reportperiod), 8))
def cg_f080_restatement_revision_proxy_core13_2nd_v014_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_flag(dimension), 8))
def cg_f080_restatement_revision_proxy_core14_2nd_v015_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_count(datekey, 4), 8))
def cg_f080_restatement_revision_proxy_core15_2nd_v016_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_count(lastupdated, 4), 8))
def cg_f080_restatement_revision_proxy_core16_2nd_v017_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_rate(reportperiod, 8), 8))
def cg_f080_restatement_revision_proxy_core17_2nd_v018_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(lastupdated) - _to_num(datekey), 8))
def cg_f080_restatement_revision_proxy_core18_2nd_v019_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_to_num(datekey) - _to_num(reportperiod), 8))
def cg_f080_restatement_revision_proxy_core19_2nd_v020_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_event_flag(lastupdated), 8))
def cg_f080_restatement_revision_proxy_core20_2nd_v021_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(datekey), 4))
def cg_f080_restatement_revision_proxy_core21_2nd_v022_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(lastupdated), 4))
def cg_f080_restatement_revision_proxy_core22_2nd_v023_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(reportperiod), 4))
def cg_f080_restatement_revision_proxy_core23_2nd_v024_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_event_flag(dimension), 4))
def cg_f080_restatement_revision_proxy_core24_2nd_v025_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_event_count(datekey, 4), 4))
def cg_f080_restatement_revision_proxy_core25_2nd_v026_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_event_count(lastupdated, 4), 4))
def cg_f080_restatement_revision_proxy_core26_2nd_v027_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_event_rate(reportperiod, 8), 4))
def cg_f080_restatement_revision_proxy_core27_2nd_v028_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(lastupdated) - _to_num(datekey), 4))
def cg_f080_restatement_revision_proxy_core28_2nd_v029_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_to_num(datekey) - _to_num(reportperiod), 4))
def cg_f080_restatement_revision_proxy_core29_2nd_v030_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_event_flag(lastupdated), 4))
def cg_f080_restatement_revision_proxy_core30_2nd_v031_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(datekey), 4), 8))
def cg_f080_restatement_revision_proxy_core31_2nd_v032_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(lastupdated), 4), 8))
def cg_f080_restatement_revision_proxy_core32_2nd_v033_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(reportperiod), 4), 8))
def cg_f080_restatement_revision_proxy_core33_2nd_v034_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_flag(dimension), 4), 8))
def cg_f080_restatement_revision_proxy_core34_2nd_v035_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_count(datekey, 4), 4), 8))
def cg_f080_restatement_revision_proxy_core35_2nd_v036_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_count(lastupdated, 4), 4), 8))
def cg_f080_restatement_revision_proxy_core36_2nd_v037_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_rate(reportperiod, 8), 4), 8))
def cg_f080_restatement_revision_proxy_core37_2nd_v038_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 8))
def cg_f080_restatement_revision_proxy_core38_2nd_v039_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 8))
def cg_f080_restatement_revision_proxy_core39_2nd_v040_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_flag(lastupdated), 4), 8))
def cg_f080_restatement_revision_proxy_core40_2nd_v041_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(datekey), 8), 12))
def cg_f080_restatement_revision_proxy_core41_2nd_v042_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(lastupdated), 8), 12))
def cg_f080_restatement_revision_proxy_core42_2nd_v043_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(reportperiod), 8), 12))
def cg_f080_restatement_revision_proxy_core43_2nd_v044_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_flag(dimension), 8), 12))
def cg_f080_restatement_revision_proxy_core44_2nd_v045_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_count(datekey, 4), 8), 12))
def cg_f080_restatement_revision_proxy_core45_2nd_v046_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_count(lastupdated, 4), 8), 12))
def cg_f080_restatement_revision_proxy_core46_2nd_v047_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_rate(reportperiod, 8), 8), 12))
def cg_f080_restatement_revision_proxy_core47_2nd_v048_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(lastupdated) - _to_num(datekey), 8), 12))
def cg_f080_restatement_revision_proxy_core48_2nd_v049_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_to_num(datekey) - _to_num(reportperiod), 8), 12))
def cg_f080_restatement_revision_proxy_core49_2nd_v050_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_slope(_event_flag(lastupdated), 8), 12))
def cg_f080_restatement_revision_proxy_core50_2nd_v051_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_to_num(datekey), 4), 8))
def cg_f080_restatement_revision_proxy_core51_2nd_v052_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_to_num(lastupdated), 4), 8))
def cg_f080_restatement_revision_proxy_core52_2nd_v053_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_to_num(reportperiod), 4), 8))
def cg_f080_restatement_revision_proxy_core53_2nd_v054_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_event_flag(dimension), 4), 8))
def cg_f080_restatement_revision_proxy_core54_2nd_v055_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_event_count(datekey, 4), 4), 8))
def cg_f080_restatement_revision_proxy_core55_2nd_v056_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_event_count(lastupdated, 4), 4), 8))
def cg_f080_restatement_revision_proxy_core56_2nd_v057_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_event_rate(reportperiod, 8), 4), 8))
def cg_f080_restatement_revision_proxy_core57_2nd_v058_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 8))
def cg_f080_restatement_revision_proxy_core58_2nd_v059_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 8))
def cg_f080_restatement_revision_proxy_core59_2nd_v060_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_event_flag(lastupdated), 4), 8))
def cg_f080_restatement_revision_proxy_core60_2nd_v061_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_to_num(datekey), 4), 12))
def cg_f080_restatement_revision_proxy_core61_2nd_v062_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_to_num(lastupdated), 4), 12))
def cg_f080_restatement_revision_proxy_core62_2nd_v063_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_to_num(reportperiod), 4), 12))
def cg_f080_restatement_revision_proxy_core63_2nd_v064_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_event_flag(dimension), 4), 12))
def cg_f080_restatement_revision_proxy_core64_2nd_v065_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_event_count(datekey, 4), 4), 12))
def cg_f080_restatement_revision_proxy_core65_2nd_v066_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_event_count(lastupdated, 4), 4), 12))
def cg_f080_restatement_revision_proxy_core66_2nd_v067_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_event_rate(reportperiod, 8), 4), 12))
def cg_f080_restatement_revision_proxy_core67_2nd_v068_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 12))
def cg_f080_restatement_revision_proxy_core68_2nd_v069_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 12))
def cg_f080_restatement_revision_proxy_core69_2nd_v070_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_event_flag(lastupdated), 4), 12))
def cg_f080_restatement_revision_proxy_core70_2nd_v071_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_to_num(datekey), 4), 12))
def cg_f080_restatement_revision_proxy_core71_2nd_v072_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_to_num(lastupdated), 4), 12))
def cg_f080_restatement_revision_proxy_core72_2nd_v073_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_to_num(reportperiod), 4), 12))
def cg_f080_restatement_revision_proxy_core73_2nd_v074_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_event_flag(dimension), 4), 12))
def cg_f080_restatement_revision_proxy_core74_2nd_v075_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_event_count(datekey, 4), 4), 12))
def cg_f080_restatement_revision_proxy_core75_2nd_v076_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_event_count(lastupdated, 4), 4), 12))
def cg_f080_restatement_revision_proxy_core76_2nd_v077_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_event_rate(reportperiod, 8), 4), 12))
def cg_f080_restatement_revision_proxy_core77_2nd_v078_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 12))
def cg_f080_restatement_revision_proxy_core78_2nd_v079_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 12))
def cg_f080_restatement_revision_proxy_core79_2nd_v080_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_diff(_event_flag(lastupdated), 4), 12))
def cg_f080_restatement_revision_proxy_core80_2nd_v081_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core81_2nd_v082_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_to_num(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core82_2nd_v083_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core83_2nd_v084_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_event_flag(dimension), 4), 4))
def cg_f080_restatement_revision_proxy_core84_2nd_v085_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_event_count(datekey, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core85_2nd_v086_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_event_count(lastupdated, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core86_2nd_v087_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_event_rate(reportperiod, 8), 4), 4))
def cg_f080_restatement_revision_proxy_core87_2nd_v088_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_to_num(lastupdated) - _to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core88_2nd_v089_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_to_num(datekey) - _to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core89_2nd_v090_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_slope(_event_flag(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core90_2nd_v091_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core91_2nd_v092_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_to_num(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core92_2nd_v093_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core93_2nd_v094_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_event_flag(dimension), 4), 4))
def cg_f080_restatement_revision_proxy_core94_2nd_v095_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_event_count(datekey, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core95_2nd_v096_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_event_count(lastupdated, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core96_2nd_v097_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_event_rate(reportperiod, 8), 4), 4))
def cg_f080_restatement_revision_proxy_core97_2nd_v098_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_to_num(lastupdated) - _to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core98_2nd_v099_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_to_num(datekey) - _to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core99_2nd_v100_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_mean(_diff(_event_flag(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core100_2nd_v101_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core101_2nd_v102_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core102_2nd_v103_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core103_2nd_v104_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_flag(dimension), 4), 4))
def cg_f080_restatement_revision_proxy_core104_2nd_v105_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_count(datekey, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core105_2nd_v106_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_count(lastupdated, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core106_2nd_v107_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_rate(reportperiod, 8), 4), 4))
def cg_f080_restatement_revision_proxy_core107_2nd_v108_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(lastupdated) - _to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core108_2nd_v109_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(datekey) - _to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core109_2nd_v110_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_flag(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core110_2nd_v111_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(datekey), 8), 8))
def cg_f080_restatement_revision_proxy_core111_2nd_v112_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(lastupdated), 8), 8))
def cg_f080_restatement_revision_proxy_core112_2nd_v113_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(reportperiod), 8), 8))
def cg_f080_restatement_revision_proxy_core113_2nd_v114_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_flag(dimension), 8), 8))
def cg_f080_restatement_revision_proxy_core114_2nd_v115_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_count(datekey, 4), 8), 8))
def cg_f080_restatement_revision_proxy_core115_2nd_v116_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_count(lastupdated, 4), 8), 8))
def cg_f080_restatement_revision_proxy_core116_2nd_v117_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_rate(reportperiod, 8), 8), 8))
def cg_f080_restatement_revision_proxy_core117_2nd_v118_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(lastupdated) - _to_num(datekey), 8), 8))
def cg_f080_restatement_revision_proxy_core118_2nd_v119_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_to_num(datekey) - _to_num(reportperiod), 8), 8))
def cg_f080_restatement_revision_proxy_core119_2nd_v120_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_slope(_mean(_event_flag(lastupdated), 8), 8))
def cg_f080_restatement_revision_proxy_core120_2nd_v121_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core121_2nd_v122_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_to_num(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core122_2nd_v123_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core123_2nd_v124_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_event_flag(dimension), 4), 4))
def cg_f080_restatement_revision_proxy_core124_2nd_v125_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_event_count(datekey, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core125_2nd_v126_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_event_count(lastupdated, 4), 4), 4))
def cg_f080_restatement_revision_proxy_core126_2nd_v127_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_event_rate(reportperiod, 8), 4), 4))
def cg_f080_restatement_revision_proxy_core127_2nd_v128_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_to_num(lastupdated) - _to_num(datekey), 4), 4))
def cg_f080_restatement_revision_proxy_core128_2nd_v129_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_to_num(datekey) - _to_num(reportperiod), 4), 4))
def cg_f080_restatement_revision_proxy_core129_2nd_v130_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_diff(_mean(_event_flag(lastupdated), 4), 4))
def cg_f080_restatement_revision_proxy_core130_2nd_v131_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_to_num(datekey), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core131_2nd_v132_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_to_num(lastupdated), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core132_2nd_v133_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_to_num(reportperiod), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core133_2nd_v134_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_event_flag(dimension), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core134_2nd_v135_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_event_count(datekey, 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core135_2nd_v136_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_event_count(lastupdated, 4), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core136_2nd_v137_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_event_rate(reportperiod, 8), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core137_2nd_v138_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_to_num(lastupdated) - _to_num(datekey), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core138_2nd_v139_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_to_num(datekey) - _to_num(reportperiod), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core139_2nd_v140_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_z(_diff(_mean(_event_flag(lastupdated), 4), 4), 8))
def cg_f080_restatement_revision_proxy_core140_2nd_v141_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_to_num(datekey), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core141_2nd_v142_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_to_num(lastupdated), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core142_2nd_v143_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_to_num(reportperiod), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core143_2nd_v144_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_event_flag(dimension), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core144_2nd_v145_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_event_count(datekey, 4), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core145_2nd_v146_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_event_count(lastupdated, 4), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core146_2nd_v147_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_event_rate(reportperiod, 8), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core147_2nd_v148_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_to_num(lastupdated) - _to_num(datekey), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core148_2nd_v149_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_to_num(datekey) - _to_num(reportperiod), 4), 4), 12))
def cg_f080_restatement_revision_proxy_core149_2nd_v150_signal(datekey, lastupdated, reportperiod, dimension):
    return _clean(_rank(_slope(_mean(_event_flag(lastupdated), 4), 4), 12))