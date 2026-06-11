import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f092_insider_transaction_flow_core00_2nd_v001_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionshares, 4))
def cg_f092_insider_transaction_flow_core01_2nd_v002_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionvalue, 4))
def cg_f092_insider_transaction_flow_core02_2nd_v003_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionpricepershare, 4))
def cg_f092_insider_transaction_flow_core03_2nd_v004_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_safe_div(transactionvalue, transactionshares), 4))
def cg_f092_insider_transaction_flow_core04_2nd_v005_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_log(transactionshares.abs() + 1.0), 4))
def cg_f092_insider_transaction_flow_core05_2nd_v006_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_log(transactionvalue.abs() + 1.0), 4))
def cg_f092_insider_transaction_flow_core06_2nd_v007_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionshares * transactionpricepershare, 4))
def cg_f092_insider_transaction_flow_core07_2nd_v008_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_safe_div(transactionshares, transactionpricepershare), 4))
def cg_f092_insider_transaction_flow_core08_2nd_v009_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_log(transactionpricepershare + 1.0), 4))
def cg_f092_insider_transaction_flow_core09_2nd_v010_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionvalue - (transactionshares * transactionpricepershare), 4))
def cg_f092_insider_transaction_flow_core10_2nd_v011_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionshares, 8))
def cg_f092_insider_transaction_flow_core11_2nd_v012_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionvalue, 8))
def cg_f092_insider_transaction_flow_core12_2nd_v013_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionpricepershare, 8))
def cg_f092_insider_transaction_flow_core13_2nd_v014_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_safe_div(transactionvalue, transactionshares), 8))
def cg_f092_insider_transaction_flow_core14_2nd_v015_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_log(transactionshares.abs() + 1.0), 8))
def cg_f092_insider_transaction_flow_core15_2nd_v016_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_log(transactionvalue.abs() + 1.0), 8))
def cg_f092_insider_transaction_flow_core16_2nd_v017_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionshares * transactionpricepershare, 8))
def cg_f092_insider_transaction_flow_core17_2nd_v018_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_safe_div(transactionshares, transactionpricepershare), 8))
def cg_f092_insider_transaction_flow_core18_2nd_v019_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_log(transactionpricepershare + 1.0), 8))
def cg_f092_insider_transaction_flow_core19_2nd_v020_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(transactionvalue - (transactionshares * transactionpricepershare), 8))
def cg_f092_insider_transaction_flow_core20_2nd_v021_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(transactionshares, 4))
def cg_f092_insider_transaction_flow_core21_2nd_v022_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(transactionvalue, 4))
def cg_f092_insider_transaction_flow_core22_2nd_v023_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(transactionpricepershare, 4))
def cg_f092_insider_transaction_flow_core23_2nd_v024_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_safe_div(transactionvalue, transactionshares), 4))
def cg_f092_insider_transaction_flow_core24_2nd_v025_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_log(transactionshares.abs() + 1.0), 4))
def cg_f092_insider_transaction_flow_core25_2nd_v026_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_log(transactionvalue.abs() + 1.0), 4))
def cg_f092_insider_transaction_flow_core26_2nd_v027_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(transactionshares * transactionpricepershare, 4))
def cg_f092_insider_transaction_flow_core27_2nd_v028_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_safe_div(transactionshares, transactionpricepershare), 4))
def cg_f092_insider_transaction_flow_core28_2nd_v029_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_log(transactionpricepershare + 1.0), 4))
def cg_f092_insider_transaction_flow_core29_2nd_v030_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(transactionvalue - (transactionshares * transactionpricepershare), 4))
def cg_f092_insider_transaction_flow_core30_2nd_v031_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionshares, 4), 8))
def cg_f092_insider_transaction_flow_core31_2nd_v032_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionvalue, 4), 8))
def cg_f092_insider_transaction_flow_core32_2nd_v033_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionpricepershare, 4), 8))
def cg_f092_insider_transaction_flow_core33_2nd_v034_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_safe_div(transactionvalue, transactionshares), 4), 8))
def cg_f092_insider_transaction_flow_core34_2nd_v035_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_log(transactionshares.abs() + 1.0), 4), 8))
def cg_f092_insider_transaction_flow_core35_2nd_v036_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_log(transactionvalue.abs() + 1.0), 4), 8))
def cg_f092_insider_transaction_flow_core36_2nd_v037_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionshares * transactionpricepershare, 4), 8))
def cg_f092_insider_transaction_flow_core37_2nd_v038_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_safe_div(transactionshares, transactionpricepershare), 4), 8))
def cg_f092_insider_transaction_flow_core38_2nd_v039_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_log(transactionpricepershare + 1.0), 4), 8))
def cg_f092_insider_transaction_flow_core39_2nd_v040_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionvalue - (transactionshares * transactionpricepershare), 4), 8))
def cg_f092_insider_transaction_flow_core40_2nd_v041_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionshares, 8), 12))
def cg_f092_insider_transaction_flow_core41_2nd_v042_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionvalue, 8), 12))
def cg_f092_insider_transaction_flow_core42_2nd_v043_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionpricepershare, 8), 12))
def cg_f092_insider_transaction_flow_core43_2nd_v044_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_safe_div(transactionvalue, transactionshares), 8), 12))
def cg_f092_insider_transaction_flow_core44_2nd_v045_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_log(transactionshares.abs() + 1.0), 8), 12))
def cg_f092_insider_transaction_flow_core45_2nd_v046_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_log(transactionvalue.abs() + 1.0), 8), 12))
def cg_f092_insider_transaction_flow_core46_2nd_v047_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionshares * transactionpricepershare, 8), 12))
def cg_f092_insider_transaction_flow_core47_2nd_v048_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_safe_div(transactionshares, transactionpricepershare), 8), 12))
def cg_f092_insider_transaction_flow_core48_2nd_v049_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(_log(transactionpricepershare + 1.0), 8), 12))
def cg_f092_insider_transaction_flow_core49_2nd_v050_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_slope(transactionvalue - (transactionshares * transactionpricepershare), 8), 12))
def cg_f092_insider_transaction_flow_core50_2nd_v051_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(transactionshares, 4), 8))
def cg_f092_insider_transaction_flow_core51_2nd_v052_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(transactionvalue, 4), 8))
def cg_f092_insider_transaction_flow_core52_2nd_v053_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(transactionpricepershare, 4), 8))
def cg_f092_insider_transaction_flow_core53_2nd_v054_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_safe_div(transactionvalue, transactionshares), 4), 8))
def cg_f092_insider_transaction_flow_core54_2nd_v055_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_log(transactionshares.abs() + 1.0), 4), 8))
def cg_f092_insider_transaction_flow_core55_2nd_v056_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_log(transactionvalue.abs() + 1.0), 4), 8))
def cg_f092_insider_transaction_flow_core56_2nd_v057_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(transactionshares * transactionpricepershare, 4), 8))
def cg_f092_insider_transaction_flow_core57_2nd_v058_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_safe_div(transactionshares, transactionpricepershare), 4), 8))
def cg_f092_insider_transaction_flow_core58_2nd_v059_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_log(transactionpricepershare + 1.0), 4), 8))
def cg_f092_insider_transaction_flow_core59_2nd_v060_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(transactionvalue - (transactionshares * transactionpricepershare), 4), 8))
def cg_f092_insider_transaction_flow_core60_2nd_v061_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(transactionshares, 4), 12))
def cg_f092_insider_transaction_flow_core61_2nd_v062_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(transactionvalue, 4), 12))
def cg_f092_insider_transaction_flow_core62_2nd_v063_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(transactionpricepershare, 4), 12))
def cg_f092_insider_transaction_flow_core63_2nd_v064_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_safe_div(transactionvalue, transactionshares), 4), 12))
def cg_f092_insider_transaction_flow_core64_2nd_v065_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_log(transactionshares.abs() + 1.0), 4), 12))
def cg_f092_insider_transaction_flow_core65_2nd_v066_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_log(transactionvalue.abs() + 1.0), 4), 12))
def cg_f092_insider_transaction_flow_core66_2nd_v067_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(transactionshares * transactionpricepershare, 4), 12))
def cg_f092_insider_transaction_flow_core67_2nd_v068_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_safe_div(transactionshares, transactionpricepershare), 4), 12))
def cg_f092_insider_transaction_flow_core68_2nd_v069_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_log(transactionpricepershare + 1.0), 4), 12))
def cg_f092_insider_transaction_flow_core69_2nd_v070_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(transactionvalue - (transactionshares * transactionpricepershare), 4), 12))
def cg_f092_insider_transaction_flow_core70_2nd_v071_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(transactionshares, 4), 12))
def cg_f092_insider_transaction_flow_core71_2nd_v072_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(transactionvalue, 4), 12))
def cg_f092_insider_transaction_flow_core72_2nd_v073_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(transactionpricepershare, 4), 12))
def cg_f092_insider_transaction_flow_core73_2nd_v074_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(_safe_div(transactionvalue, transactionshares), 4), 12))
def cg_f092_insider_transaction_flow_core74_2nd_v075_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(_log(transactionshares.abs() + 1.0), 4), 12))
def cg_f092_insider_transaction_flow_core75_2nd_v076_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(_log(transactionvalue.abs() + 1.0), 4), 12))
def cg_f092_insider_transaction_flow_core76_2nd_v077_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(transactionshares * transactionpricepershare, 4), 12))
def cg_f092_insider_transaction_flow_core77_2nd_v078_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(_safe_div(transactionshares, transactionpricepershare), 4), 12))
def cg_f092_insider_transaction_flow_core78_2nd_v079_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(_log(transactionpricepershare + 1.0), 4), 12))
def cg_f092_insider_transaction_flow_core79_2nd_v080_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_diff(transactionvalue - (transactionshares * transactionpricepershare), 4), 12))
def cg_f092_insider_transaction_flow_core80_2nd_v081_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(transactionshares, 4), 4))
def cg_f092_insider_transaction_flow_core81_2nd_v082_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(transactionvalue, 4), 4))
def cg_f092_insider_transaction_flow_core82_2nd_v083_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core83_2nd_v084_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(_safe_div(transactionvalue, transactionshares), 4), 4))
def cg_f092_insider_transaction_flow_core84_2nd_v085_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core85_2nd_v086_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(_log(transactionvalue.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core86_2nd_v087_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(transactionshares * transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core87_2nd_v088_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(_safe_div(transactionshares, transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core88_2nd_v089_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(_log(transactionpricepershare + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core89_2nd_v090_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_slope(transactionvalue - (transactionshares * transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core90_2nd_v091_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(transactionshares, 4), 4))
def cg_f092_insider_transaction_flow_core91_2nd_v092_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(transactionvalue, 4), 4))
def cg_f092_insider_transaction_flow_core92_2nd_v093_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core93_2nd_v094_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(_safe_div(transactionvalue, transactionshares), 4), 4))
def cg_f092_insider_transaction_flow_core94_2nd_v095_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core95_2nd_v096_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(_log(transactionvalue.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core96_2nd_v097_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(transactionshares * transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core97_2nd_v098_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(_safe_div(transactionshares, transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core98_2nd_v099_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(_log(transactionpricepershare + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core99_2nd_v100_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_mean(_diff(transactionvalue - (transactionshares * transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core100_2nd_v101_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionshares, 4), 4))
def cg_f092_insider_transaction_flow_core101_2nd_v102_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionvalue, 4), 4))
def cg_f092_insider_transaction_flow_core102_2nd_v103_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core103_2nd_v104_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_safe_div(transactionvalue, transactionshares), 4), 4))
def cg_f092_insider_transaction_flow_core104_2nd_v105_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core105_2nd_v106_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_log(transactionvalue.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core106_2nd_v107_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionshares * transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core107_2nd_v108_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_safe_div(transactionshares, transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core108_2nd_v109_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_log(transactionpricepershare + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core109_2nd_v110_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionvalue - (transactionshares * transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core110_2nd_v111_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionshares, 8), 8))
def cg_f092_insider_transaction_flow_core111_2nd_v112_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionvalue, 8), 8))
def cg_f092_insider_transaction_flow_core112_2nd_v113_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionpricepershare, 8), 8))
def cg_f092_insider_transaction_flow_core113_2nd_v114_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_safe_div(transactionvalue, transactionshares), 8), 8))
def cg_f092_insider_transaction_flow_core114_2nd_v115_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_log(transactionshares.abs() + 1.0), 8), 8))
def cg_f092_insider_transaction_flow_core115_2nd_v116_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_log(transactionvalue.abs() + 1.0), 8), 8))
def cg_f092_insider_transaction_flow_core116_2nd_v117_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionshares * transactionpricepershare, 8), 8))
def cg_f092_insider_transaction_flow_core117_2nd_v118_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_safe_div(transactionshares, transactionpricepershare), 8), 8))
def cg_f092_insider_transaction_flow_core118_2nd_v119_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(_log(transactionpricepershare + 1.0), 8), 8))
def cg_f092_insider_transaction_flow_core119_2nd_v120_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_slope(_mean(transactionvalue - (transactionshares * transactionpricepershare), 8), 8))
def cg_f092_insider_transaction_flow_core120_2nd_v121_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(transactionshares, 4), 4))
def cg_f092_insider_transaction_flow_core121_2nd_v122_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(transactionvalue, 4), 4))
def cg_f092_insider_transaction_flow_core122_2nd_v123_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core123_2nd_v124_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(_safe_div(transactionvalue, transactionshares), 4), 4))
def cg_f092_insider_transaction_flow_core124_2nd_v125_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(_log(transactionshares.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core125_2nd_v126_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(_log(transactionvalue.abs() + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core126_2nd_v127_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(transactionshares * transactionpricepershare, 4), 4))
def cg_f092_insider_transaction_flow_core127_2nd_v128_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(_safe_div(transactionshares, transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core128_2nd_v129_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(_log(transactionpricepershare + 1.0), 4), 4))
def cg_f092_insider_transaction_flow_core129_2nd_v130_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_diff(_mean(transactionvalue - (transactionshares * transactionpricepershare), 4), 4))
def cg_f092_insider_transaction_flow_core130_2nd_v131_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(transactionshares, 4), 4), 8))
def cg_f092_insider_transaction_flow_core131_2nd_v132_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(transactionvalue, 4), 4), 8))
def cg_f092_insider_transaction_flow_core132_2nd_v133_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(transactionpricepershare, 4), 4), 8))
def cg_f092_insider_transaction_flow_core133_2nd_v134_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(_safe_div(transactionvalue, transactionshares), 4), 4), 8))
def cg_f092_insider_transaction_flow_core134_2nd_v135_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(_log(transactionshares.abs() + 1.0), 4), 4), 8))
def cg_f092_insider_transaction_flow_core135_2nd_v136_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(_log(transactionvalue.abs() + 1.0), 4), 4), 8))
def cg_f092_insider_transaction_flow_core136_2nd_v137_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(transactionshares * transactionpricepershare, 4), 4), 8))
def cg_f092_insider_transaction_flow_core137_2nd_v138_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(_safe_div(transactionshares, transactionpricepershare), 4), 4), 8))
def cg_f092_insider_transaction_flow_core138_2nd_v139_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(_log(transactionpricepershare + 1.0), 4), 4), 8))
def cg_f092_insider_transaction_flow_core139_2nd_v140_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_z(_diff(_mean(transactionvalue - (transactionshares * transactionpricepershare), 4), 4), 8))
def cg_f092_insider_transaction_flow_core140_2nd_v141_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(transactionshares, 4), 4), 12))
def cg_f092_insider_transaction_flow_core141_2nd_v142_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(transactionvalue, 4), 4), 12))
def cg_f092_insider_transaction_flow_core142_2nd_v143_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(transactionpricepershare, 4), 4), 12))
def cg_f092_insider_transaction_flow_core143_2nd_v144_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(_safe_div(transactionvalue, transactionshares), 4), 4), 12))
def cg_f092_insider_transaction_flow_core144_2nd_v145_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(_log(transactionshares.abs() + 1.0), 4), 4), 12))
def cg_f092_insider_transaction_flow_core145_2nd_v146_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(_log(transactionvalue.abs() + 1.0), 4), 4), 12))
def cg_f092_insider_transaction_flow_core146_2nd_v147_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(transactionshares * transactionpricepershare, 4), 4), 12))
def cg_f092_insider_transaction_flow_core147_2nd_v148_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(_safe_div(transactionshares, transactionpricepershare), 4), 4), 12))
def cg_f092_insider_transaction_flow_core148_2nd_v149_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(_log(transactionpricepershare + 1.0), 4), 4), 12))
def cg_f092_insider_transaction_flow_core149_2nd_v150_signal(transactioncode, transactionshares, transactionvalue, transactionpricepershare):
    return _clean(_rank(_slope(_mean(transactionvalue - (transactionshares * transactionpricepershare), 4), 4), 12))