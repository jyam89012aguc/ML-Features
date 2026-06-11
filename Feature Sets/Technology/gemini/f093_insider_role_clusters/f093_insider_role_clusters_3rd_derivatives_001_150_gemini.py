import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f093_insider_role_clusters_core00_3rd_v001_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(isdirector, 4), 4))
def cg_f093_insider_role_clusters_core01_3rd_v002_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(isofficer, 4), 4))
def cg_f093_insider_role_clusters_core02_3rd_v003_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core03_3rd_v004_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(isdirector + isofficer, 4), 4))
def cg_f093_insider_role_clusters_core04_3rd_v005_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(isdirector + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core05_3rd_v006_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core06_3rd_v007_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core07_3rd_v008_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_to_num(isdirector), 4), 4))
def cg_f093_insider_role_clusters_core08_3rd_v009_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_to_num(isofficer), 4), 4))
def cg_f093_insider_role_clusters_core09_3rd_v010_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_to_num(istenpercentowner), 4), 4))
def cg_f093_insider_role_clusters_core10_3rd_v011_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(isdirector, 4), 8))
def cg_f093_insider_role_clusters_core11_3rd_v012_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(isofficer, 4), 8))
def cg_f093_insider_role_clusters_core12_3rd_v013_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core13_3rd_v014_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(isdirector + isofficer, 4), 8))
def cg_f093_insider_role_clusters_core14_3rd_v015_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(isdirector + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core15_3rd_v016_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(isofficer + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core16_3rd_v017_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(isdirector + isofficer + istenpercentowner, 4), 8))
def cg_f093_insider_role_clusters_core17_3rd_v018_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_to_num(isdirector), 4), 8))
def cg_f093_insider_role_clusters_core18_3rd_v019_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_to_num(isofficer), 4), 8))
def cg_f093_insider_role_clusters_core19_3rd_v020_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_to_num(istenpercentowner), 4), 8))
def cg_f093_insider_role_clusters_core20_3rd_v021_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(isdirector, 4), 4))
def cg_f093_insider_role_clusters_core21_3rd_v022_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(isofficer, 4), 4))
def cg_f093_insider_role_clusters_core22_3rd_v023_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core23_3rd_v024_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(isdirector + isofficer, 4), 4))
def cg_f093_insider_role_clusters_core24_3rd_v025_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(isdirector + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core25_3rd_v026_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core26_3rd_v027_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(isdirector + isofficer + istenpercentowner, 4), 4))
def cg_f093_insider_role_clusters_core27_3rd_v028_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(_to_num(isdirector), 4), 4))
def cg_f093_insider_role_clusters_core28_3rd_v029_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(_to_num(isofficer), 4), 4))
def cg_f093_insider_role_clusters_core29_3rd_v030_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_slope(_to_num(istenpercentowner), 4), 4))
def cg_f093_insider_role_clusters_core30_3rd_v031_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(isdirector, 4), 4), 8))
def cg_f093_insider_role_clusters_core31_3rd_v032_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(isofficer, 4), 4), 8))
def cg_f093_insider_role_clusters_core32_3rd_v033_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core33_3rd_v034_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(isdirector + isofficer, 4), 4), 8))
def cg_f093_insider_role_clusters_core34_3rd_v035_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(isdirector + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core35_3rd_v036_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(isofficer + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core36_3rd_v037_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core37_3rd_v038_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(_to_num(isdirector), 4), 4), 8))
def cg_f093_insider_role_clusters_core38_3rd_v039_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(_to_num(isofficer), 4), 4), 8))
def cg_f093_insider_role_clusters_core39_3rd_v040_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_diff(_to_num(istenpercentowner), 4), 4), 8))
def cg_f093_insider_role_clusters_core40_3rd_v041_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(isdirector, 4), 8), 12))
def cg_f093_insider_role_clusters_core41_3rd_v042_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(isofficer, 4), 8), 12))
def cg_f093_insider_role_clusters_core42_3rd_v043_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core43_3rd_v044_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(isdirector + isofficer, 4), 8), 12))
def cg_f093_insider_role_clusters_core44_3rd_v045_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(isdirector + istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core45_3rd_v046_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(isofficer + istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core46_3rd_v047_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(isdirector + isofficer + istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core47_3rd_v048_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_to_num(isdirector), 4), 8), 12))
def cg_f093_insider_role_clusters_core48_3rd_v049_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_to_num(isofficer), 4), 8), 12))
def cg_f093_insider_role_clusters_core49_3rd_v050_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_to_num(istenpercentowner), 4), 8), 12))
def cg_f093_insider_role_clusters_core50_3rd_v051_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(isdirector, 4), 4), 8))
def cg_f093_insider_role_clusters_core51_3rd_v052_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(isofficer, 4), 4), 8))
def cg_f093_insider_role_clusters_core52_3rd_v053_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core53_3rd_v054_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(isdirector + isofficer, 4), 4), 8))
def cg_f093_insider_role_clusters_core54_3rd_v055_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(isdirector + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core55_3rd_v056_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(isofficer + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core56_3rd_v057_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(isdirector + isofficer + istenpercentowner, 4), 4), 8))
def cg_f093_insider_role_clusters_core57_3rd_v058_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(_to_num(isdirector), 4), 4), 8))
def cg_f093_insider_role_clusters_core58_3rd_v059_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(_to_num(isofficer), 4), 4), 8))
def cg_f093_insider_role_clusters_core59_3rd_v060_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_diff(_slope(_to_num(istenpercentowner), 4), 4), 8))
def cg_f093_insider_role_clusters_core60_3rd_v061_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(isdirector, 4), 4), 12))
def cg_f093_insider_role_clusters_core61_3rd_v062_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(isofficer, 4), 4), 12))
def cg_f093_insider_role_clusters_core62_3rd_v063_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core63_3rd_v064_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(isdirector + isofficer, 4), 4), 12))
def cg_f093_insider_role_clusters_core64_3rd_v065_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(isdirector + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core65_3rd_v066_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(isofficer + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core66_3rd_v067_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core67_3rd_v068_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(_to_num(isdirector), 4), 4), 12))
def cg_f093_insider_role_clusters_core68_3rd_v069_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(_to_num(isofficer), 4), 4), 12))
def cg_f093_insider_role_clusters_core69_3rd_v070_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_diff(_to_num(istenpercentowner), 4), 4), 12))
def cg_f093_insider_role_clusters_core70_3rd_v071_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(isdirector, 4), 8), 12))
def cg_f093_insider_role_clusters_core71_3rd_v072_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(isofficer, 4), 8), 12))
def cg_f093_insider_role_clusters_core72_3rd_v073_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core73_3rd_v074_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(isdirector + isofficer, 4), 8), 12))
def cg_f093_insider_role_clusters_core74_3rd_v075_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(isdirector + istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core75_3rd_v076_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(isofficer + istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core76_3rd_v077_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(isdirector + isofficer + istenpercentowner, 4), 8), 12))
def cg_f093_insider_role_clusters_core77_3rd_v078_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(_to_num(isdirector), 4), 8), 12))
def cg_f093_insider_role_clusters_core78_3rd_v079_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(_to_num(isofficer), 4), 8), 12))
def cg_f093_insider_role_clusters_core79_3rd_v080_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_slope(_diff(_to_num(istenpercentowner), 4), 8), 12))
def cg_f093_insider_role_clusters_core80_3rd_v081_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(isdirector, 4), 4), 12))
def cg_f093_insider_role_clusters_core81_3rd_v082_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(isofficer, 4), 4), 12))
def cg_f093_insider_role_clusters_core82_3rd_v083_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core83_3rd_v084_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(isdirector + isofficer, 4), 4), 12))
def cg_f093_insider_role_clusters_core84_3rd_v085_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(isdirector + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core85_3rd_v086_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(isofficer + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core86_3rd_v087_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(isdirector + isofficer + istenpercentowner, 4), 4), 12))
def cg_f093_insider_role_clusters_core87_3rd_v088_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(_to_num(isdirector), 4), 4), 12))
def cg_f093_insider_role_clusters_core88_3rd_v089_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(_to_num(isofficer), 4), 4), 12))
def cg_f093_insider_role_clusters_core89_3rd_v090_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_rank(_diff(_slope(_to_num(istenpercentowner), 4), 4), 12))
def cg_f093_insider_role_clusters_core90_3rd_v091_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(isdirector, 4), 4), 4))
def cg_f093_insider_role_clusters_core91_3rd_v092_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core92_3rd_v093_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core93_3rd_v094_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(isdirector + isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core94_3rd_v095_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(isdirector + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core95_3rd_v096_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core96_3rd_v097_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core97_3rd_v098_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(_to_num(isdirector), 4), 4), 4))
def cg_f093_insider_role_clusters_core98_3rd_v099_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(_to_num(isofficer), 4), 4), 4))
def cg_f093_insider_role_clusters_core99_3rd_v100_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_diff(_to_num(istenpercentowner), 4), 4), 4))
def cg_f093_insider_role_clusters_core100_3rd_v101_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(isdirector, 4), 8), 4))
def cg_f093_insider_role_clusters_core101_3rd_v102_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(isofficer, 4), 8), 4))
def cg_f093_insider_role_clusters_core102_3rd_v103_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(istenpercentowner, 4), 8), 4))
def cg_f093_insider_role_clusters_core103_3rd_v104_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(isdirector + isofficer, 4), 8), 4))
def cg_f093_insider_role_clusters_core104_3rd_v105_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(isdirector + istenpercentowner, 4), 8), 4))
def cg_f093_insider_role_clusters_core105_3rd_v106_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(isofficer + istenpercentowner, 4), 8), 4))
def cg_f093_insider_role_clusters_core106_3rd_v107_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(isdirector + isofficer + istenpercentowner, 4), 8), 4))
def cg_f093_insider_role_clusters_core107_3rd_v108_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(_to_num(isdirector), 4), 8), 4))
def cg_f093_insider_role_clusters_core108_3rd_v109_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(_to_num(isofficer), 4), 8), 4))
def cg_f093_insider_role_clusters_core109_3rd_v110_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_slope(_diff(_to_num(istenpercentowner), 4), 8), 4))
def cg_f093_insider_role_clusters_core110_3rd_v111_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(isdirector, 4), 4), 4))
def cg_f093_insider_role_clusters_core111_3rd_v112_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core112_3rd_v113_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core113_3rd_v114_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(isdirector + isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core114_3rd_v115_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(isdirector + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core115_3rd_v116_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core116_3rd_v117_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(isdirector + isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core117_3rd_v118_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(_to_num(isdirector), 4), 4), 4))
def cg_f093_insider_role_clusters_core118_3rd_v119_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(_to_num(isofficer), 4), 4), 4))
def cg_f093_insider_role_clusters_core119_3rd_v120_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_mean(_diff(_slope(_to_num(istenpercentowner), 4), 4), 4))
def cg_f093_insider_role_clusters_core120_3rd_v121_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(isdirector, 4), 4), 4))
def cg_f093_insider_role_clusters_core121_3rd_v122_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core122_3rd_v123_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core123_3rd_v124_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(isdirector + isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core124_3rd_v125_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(isdirector + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core125_3rd_v126_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core126_3rd_v127_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core127_3rd_v128_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(_to_num(isdirector), 4), 4), 4))
def cg_f093_insider_role_clusters_core128_3rd_v129_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(_to_num(isofficer), 4), 4), 4))
def cg_f093_insider_role_clusters_core129_3rd_v130_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_slope(_diff(_diff(_to_num(istenpercentowner), 4), 4), 4))
def cg_f093_insider_role_clusters_core130_3rd_v131_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(isdirector, 4), 4), 4))
def cg_f093_insider_role_clusters_core131_3rd_v132_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core132_3rd_v133_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core133_3rd_v134_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(isdirector + isofficer, 4), 4), 4))
def cg_f093_insider_role_clusters_core134_3rd_v135_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(isdirector + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core135_3rd_v136_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core136_3rd_v137_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4), 4))
def cg_f093_insider_role_clusters_core137_3rd_v138_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(_to_num(isdirector), 4), 4), 4))
def cg_f093_insider_role_clusters_core138_3rd_v139_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(_to_num(isofficer), 4), 4), 4))
def cg_f093_insider_role_clusters_core139_3rd_v140_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_diff(_diff(_diff(_to_num(istenpercentowner), 4), 4), 4))
def cg_f093_insider_role_clusters_core140_3rd_v141_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(isdirector, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core141_3rd_v142_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(isofficer, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core142_3rd_v143_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(istenpercentowner, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core143_3rd_v144_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(isdirector + isofficer, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core144_3rd_v145_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(isdirector + istenpercentowner, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core145_3rd_v146_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(isofficer + istenpercentowner, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core146_3rd_v147_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(isdirector + isofficer + istenpercentowner, 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core147_3rd_v148_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(_to_num(isdirector), 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core148_3rd_v149_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(_to_num(isofficer), 4), 4), 4), 8))
def cg_f093_insider_role_clusters_core149_3rd_v150_signal(ownername, officertitle, isdirector, isofficer, istenpercentowner, transactiondate):
    return _clean(_z(_slope(_diff(_diff(_to_num(istenpercentowner), 4), 4), 4), 8))