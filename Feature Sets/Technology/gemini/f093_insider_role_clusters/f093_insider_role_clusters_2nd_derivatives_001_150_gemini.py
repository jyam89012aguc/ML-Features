import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f093_insider_role_clusters_core00_2nd_v001_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector, 4))
def cg_f093_insider_role_clusters_core01_2nd_v002_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isofficer, 4))
def cg_f093_insider_role_clusters_core02_2nd_v003_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(istenpercentowner, 4))
def cg_f093_insider_role_clusters_core03_2nd_v004_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector + isofficer, 4))
def cg_f093_insider_role_clusters_core04_2nd_v005_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector + istenpercentowner, 4))
def cg_f093_insider_role_clusters_core05_2nd_v006_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isofficer + istenpercentowner, 4))
def cg_f093_insider_role_clusters_core06_2nd_v007_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector + isofficer + istenpercentowner, 4))
def cg_f093_insider_role_clusters_core07_2nd_v008_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_to_num(isdirector), 4))
def cg_f093_insider_role_clusters_core08_2nd_v009_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_to_num(isofficer), 4))
def cg_f093_insider_role_clusters_core09_2nd_v010_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_to_num(istenpercentowner), 4))
def cg_f093_insider_role_clusters_core10_2nd_v011_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector, 8))
def cg_f093_insider_role_clusters_core11_2nd_v012_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isofficer, 8))
def cg_f093_insider_role_clusters_core12_2nd_v013_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(istenpercentowner, 8))
def cg_f093_insider_role_clusters_core13_2nd_v014_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector + isofficer, 8))
def cg_f093_insider_role_clusters_core14_2nd_v015_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector + istenpercentowner, 8))
def cg_f093_insider_role_clusters_core15_2nd_v016_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isofficer + istenpercentowner, 8))
def cg_f093_insider_role_clusters_core16_2nd_v017_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(isdirector + isofficer + istenpercentowner, 8))
def cg_f093_insider_role_clusters_core17_2nd_v018_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_to_num(isdirector), 8))
def cg_f093_insider_role_clusters_core18_2nd_v019_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_to_num(isofficer), 8))
def cg_f093_insider_role_clusters_core19_2nd_v020_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_to_num(istenpercentowner), 8))
def cg_f093_insider_role_clusters_core20_2nd_v021_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(isdirector, 4))
def cg_f093_insider_role_clusters_core21_2nd_v022_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(isofficer, 4))
def cg_f093_insider_role_clusters_core22_2nd_v023_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(istenpercentowner, 4))
def cg_f093_insider_role_clusters_core23_2nd_v024_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(isdirector + isofficer, 4))
def cg_f093_insider_role_clusters_core24_2nd_v025_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(isdirector + istenpercentowner, 4))
def cg_f093_insider_role_clusters_core25_2nd_v026_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(isofficer + istenpercentowner, 4))
def cg_f093_insider_role_clusters_core26_2nd_v027_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(isdirector + isofficer + istenpercentowner, 4))
def cg_f093_insider_role_clusters_core27_2nd_v028_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_to_num(isdirector), 4))
def cg_f093_insider_role_clusters_core28_2nd_v029_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_to_num(isofficer), 4))
def cg_f093_insider_role_clusters_core29_2nd_v030_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_to_num(istenpercentowner), 4))
def cg_f093_insider_role_clusters_core30_2nd_v031_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector, 4), 8))
def cg_f093_insider_role_clusters_core31_2nd_v032_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isofficer, 4), 8))
def cg_f093_insider_role_clusters_core32_2nd_v033_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core33_2nd_v034_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector + isofficer, 4), 8))
def cg_f093_insider_role_clusters_core34_2nd_v035_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core35_2nd_v036_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isofficer + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core36_2nd_v037_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector + isofficer + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core37_2nd_v038_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_to_num(isdirector), 4), 8))
def cg_f093_insider_role_clusters_core38_2nd_v039_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_to_num(isofficer), 4), 8))
def cg_f093_insider_role_clusters_core39_2nd_v040_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_to_num(istenpercentowner), 4), 8))
def cg_f093_insider_role_clusters_core40_2nd_v041_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector, 8), 12))
def cg_f093_insider_role_clusters_core41_2nd_v042_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isofficer, 8), 12))
def cg_f093_insider_role_clusters_core42_2nd_v043_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(istenpercentowner, 8), 12))
def cg_f093_insider_role_clusters_core43_2nd_v044_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector + isofficer, 8), 12))
def cg_f093_insider_role_clusters_core44_2nd_v045_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector + istenpercentowner, 8), 12))
def cg_f093_insider_role_clusters_core45_2nd_v046_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isofficer + istenpercentowner, 8), 12))
def cg_f093_insider_role_clusters_core46_2nd_v047_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(isdirector + isofficer + istenpercentowner, 8), 12))
def cg_f093_insider_role_clusters_core47_2nd_v048_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_to_num(isdirector), 8), 12))
def cg_f093_insider_role_clusters_core48_2nd_v049_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_to_num(isofficer), 8), 12))
def cg_f093_insider_role_clusters_core49_2nd_v050_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_to_num(istenpercentowner), 8), 12))
def cg_f093_insider_role_clusters_core50_2nd_v051_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(isdirector, 4), 8))
def cg_f093_insider_role_clusters_core51_2nd_v052_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(isofficer, 4), 8))
def cg_f093_insider_role_clusters_core52_2nd_v053_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core53_2nd_v054_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(isdirector + isofficer, 4), 8))
def cg_f093_insider_role_clusters_core54_2nd_v055_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(isdirector + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core55_2nd_v056_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(isofficer + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core56_2nd_v057_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(isdirector + isofficer + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core57_2nd_v058_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_to_num(isdirector), 4), 8))
def cg_f093_insider_role_clusters_core58_2nd_v059_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_to_num(isofficer), 4), 8))
def cg_f093_insider_role_clusters_core59_2nd_v060_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_to_num(istenpercentowner), 4), 8))
def cg_f093_insider_role_clusters_core60_2nd_v061_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(isdirector, 4), 12))
def cg_f093_insider_role_clusters_core61_2nd_v062_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(isofficer, 4), 12))
def cg_f093_insider_role_clusters_core62_2nd_v063_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core63_2nd_v064_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(isdirector + isofficer, 4), 12))
def cg_f093_insider_role_clusters_core64_2nd_v065_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(isdirector + istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core65_2nd_v066_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(isofficer + istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core66_2nd_v067_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(isdirector + isofficer + istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core67_2nd_v068_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_to_num(isdirector), 4), 12))
def cg_f093_insider_role_clusters_core68_2nd_v069_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_to_num(isofficer), 4), 12))
def cg_f093_insider_role_clusters_core69_2nd_v070_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_to_num(istenpercentowner), 4), 12))
def cg_f093_insider_role_clusters_core70_2nd_v071_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(isdirector, 4), 12))
def cg_f093_insider_role_clusters_core71_2nd_v072_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(isofficer, 4), 12))
def cg_f093_insider_role_clusters_core72_2nd_v073_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core73_2nd_v074_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(isdirector + isofficer, 4), 12))
def cg_f093_insider_role_clusters_core74_2nd_v075_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(isdirector + istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core75_2nd_v076_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(isofficer + istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core76_2nd_v077_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(isdirector + isofficer + istenpercentowner, 4), 12))
def cg_f093_insider_role_clusters_core77_2nd_v078_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_to_num(isdirector), 4), 12))
def cg_f093_insider_role_clusters_core78_2nd_v079_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_to_num(isofficer), 4), 12))
def cg_f093_insider_role_clusters_core79_2nd_v080_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_to_num(istenpercentowner), 4), 12))
def cg_f093_insider_role_clusters_core80_2nd_v081_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(isdirector, 4), 4))
def cg_f093_insider_role_clusters_core81_2nd_v082_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(isofficer, 4), 4))
def cg_f093_insider_role_clusters_core82_2nd_v083_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core83_2nd_v084_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(isdirector + isofficer, 4), 4))
def cg_f093_insider_role_clusters_core84_2nd_v085_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(isdirector + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core85_2nd_v086_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core86_2nd_v087_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(isdirector + isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core87_2nd_v088_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_to_num(isdirector), 4), 4))
def cg_f093_insider_role_clusters_core88_2nd_v089_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_to_num(isofficer), 4), 4))
def cg_f093_insider_role_clusters_core89_2nd_v090_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_to_num(istenpercentowner), 4), 4))
def cg_f093_insider_role_clusters_core90_2nd_v091_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(isdirector, 4), 4))
def cg_f093_insider_role_clusters_core91_2nd_v092_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(isofficer, 4), 4))
def cg_f093_insider_role_clusters_core92_2nd_v093_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core93_2nd_v094_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(isdirector + isofficer, 4), 4))
def cg_f093_insider_role_clusters_core94_2nd_v095_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(isdirector + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core95_2nd_v096_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core96_2nd_v097_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(isdirector + isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core97_2nd_v098_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_to_num(isdirector), 4), 4))
def cg_f093_insider_role_clusters_core98_2nd_v099_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_to_num(isofficer), 4), 4))
def cg_f093_insider_role_clusters_core99_2nd_v100_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_to_num(istenpercentowner), 4), 4))
def cg_f093_insider_role_clusters_core100_2nd_v101_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector, 4), 4))
def cg_f093_insider_role_clusters_core101_2nd_v102_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isofficer, 4), 4))
def cg_f093_insider_role_clusters_core102_2nd_v103_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core103_2nd_v104_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector + isofficer, 4), 4))
def cg_f093_insider_role_clusters_core104_2nd_v105_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core105_2nd_v106_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core106_2nd_v107_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector + isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core107_2nd_v108_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(_to_num(isdirector), 4), 4))
def cg_f093_insider_role_clusters_core108_2nd_v109_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(_to_num(isofficer), 4), 4))
def cg_f093_insider_role_clusters_core109_2nd_v110_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(_to_num(istenpercentowner), 4), 4))
def cg_f093_insider_role_clusters_core110_2nd_v111_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector, 8), 8))
def cg_f093_insider_role_clusters_core111_2nd_v112_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isofficer, 8), 8))
def cg_f093_insider_role_clusters_core112_2nd_v113_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(istenpercentowner, 8), 8))
def cg_f093_insider_role_clusters_core113_2nd_v114_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector + isofficer, 8), 8))
def cg_f093_insider_role_clusters_core114_2nd_v115_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector + istenpercentowner, 8), 8))
def cg_f093_insider_role_clusters_core115_2nd_v116_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isofficer + istenpercentowner, 8), 8))
def cg_f093_insider_role_clusters_core116_2nd_v117_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(isdirector + isofficer + istenpercentowner, 8), 8))
def cg_f093_insider_role_clusters_core117_2nd_v118_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(_to_num(isdirector), 8), 8))
def cg_f093_insider_role_clusters_core118_2nd_v119_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(_to_num(isofficer), 8), 8))
def cg_f093_insider_role_clusters_core119_2nd_v120_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_mean(_to_num(istenpercentowner), 8), 8))
def cg_f093_insider_role_clusters_core120_2nd_v121_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(isdirector, 4), 4))
def cg_f093_insider_role_clusters_core121_2nd_v122_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(isofficer, 4), 4))
def cg_f093_insider_role_clusters_core122_2nd_v123_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core123_2nd_v124_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(isdirector + isofficer, 4), 4))
def cg_f093_insider_role_clusters_core124_2nd_v125_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(isdirector + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core125_2nd_v126_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core126_2nd_v127_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(isdirector + isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core127_2nd_v128_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(_to_num(isdirector), 4), 4))
def cg_f093_insider_role_clusters_core128_2nd_v129_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(_to_num(isofficer), 4), 4))
def cg_f093_insider_role_clusters_core129_2nd_v130_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_mean(_to_num(istenpercentowner), 4), 4))
def cg_f093_insider_role_clusters_core130_2nd_v131_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(isdirector, 4), 4), 8))
def cg_f093_insider_role_clusters_core131_2nd_v132_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(isofficer, 4), 4), 8))
def cg_f093_insider_role_clusters_core132_2nd_v133_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core133_2nd_v134_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(isdirector + isofficer, 4), 4), 8))
def cg_f093_insider_role_clusters_core134_2nd_v135_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(isdirector + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core135_2nd_v136_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(isofficer + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core136_2nd_v137_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(isdirector + isofficer + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core137_2nd_v138_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(_to_num(isdirector), 4), 4), 8))
def cg_f093_insider_role_clusters_core138_2nd_v139_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(_to_num(isofficer), 4), 4), 8))
def cg_f093_insider_role_clusters_core139_2nd_v140_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_mean(_to_num(istenpercentowner), 4), 4), 8))
def cg_f093_insider_role_clusters_core140_2nd_v141_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(isdirector, 4), 4), 12))
def cg_f093_insider_role_clusters_core141_2nd_v142_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(isofficer, 4), 4), 12))
def cg_f093_insider_role_clusters_core142_2nd_v143_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core143_2nd_v144_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(isdirector + isofficer, 4), 4), 12))
def cg_f093_insider_role_clusters_core144_2nd_v145_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(isdirector + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core145_2nd_v146_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(isofficer + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core146_2nd_v147_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(isdirector + isofficer + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core147_2nd_v148_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(_to_num(isdirector), 4), 4), 12))
def cg_f093_insider_role_clusters_core148_2nd_v149_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(_to_num(isofficer), 4), 4), 12))
def cg_f093_insider_role_clusters_core149_2nd_v150_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_mean(_to_num(istenpercentowner), 4), 4), 12))