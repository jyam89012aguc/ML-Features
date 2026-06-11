import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f009_free_cash_flow_core00_3rd_v001_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(fcf, 4), 4))
def cg_f009_free_cash_flow_core01_3rd_v002_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(fcfps, 4), 4))
def cg_f009_free_cash_flow_core02_3rd_v003_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(ncfo, 4), 4))
def cg_f009_free_cash_flow_core03_3rd_v004_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(capex, 4), 4))
def cg_f009_free_cash_flow_core04_3rd_v005_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_safe_div(fcf, ncfo), 4), 4))
def cg_f009_free_cash_flow_core05_3rd_v006_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core06_3rd_v007_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core07_3rd_v008_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(fcf - ncfo, 4), 4))
def cg_f009_free_cash_flow_core08_3rd_v009_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core09_3rd_v010_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core10_3rd_v011_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(fcf, 4), 8))
def cg_f009_free_cash_flow_core11_3rd_v012_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(fcfps, 4), 8))
def cg_f009_free_cash_flow_core12_3rd_v013_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(ncfo, 4), 8))
def cg_f009_free_cash_flow_core13_3rd_v014_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(capex, 4), 8))
def cg_f009_free_cash_flow_core14_3rd_v015_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_safe_div(fcf, ncfo), 4), 8))
def cg_f009_free_cash_flow_core15_3rd_v016_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 8))
def cg_f009_free_cash_flow_core16_3rd_v017_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 8))
def cg_f009_free_cash_flow_core17_3rd_v018_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(fcf - ncfo, 4), 8))
def cg_f009_free_cash_flow_core18_3rd_v019_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_log(fcf.abs() + 1.0), 4), 8))
def cg_f009_free_cash_flow_core19_3rd_v020_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8))
def cg_f009_free_cash_flow_core20_3rd_v021_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(fcf, 4), 4))
def cg_f009_free_cash_flow_core21_3rd_v022_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(fcfps, 4), 4))
def cg_f009_free_cash_flow_core22_3rd_v023_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(ncfo, 4), 4))
def cg_f009_free_cash_flow_core23_3rd_v024_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(capex, 4), 4))
def cg_f009_free_cash_flow_core24_3rd_v025_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(_safe_div(fcf, ncfo), 4), 4))
def cg_f009_free_cash_flow_core25_3rd_v026_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(_safe_div(fcf, capex.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core26_3rd_v027_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(_safe_div(ncfo, capex.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core27_3rd_v028_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(fcf - ncfo, 4), 4))
def cg_f009_free_cash_flow_core28_3rd_v029_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(_log(fcf.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core29_3rd_v030_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f009_free_cash_flow_core30_3rd_v031_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(fcf, 4), 4), 8))
def cg_f009_free_cash_flow_core31_3rd_v032_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(fcfps, 4), 4), 8))
def cg_f009_free_cash_flow_core32_3rd_v033_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(ncfo, 4), 4), 8))
def cg_f009_free_cash_flow_core33_3rd_v034_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(capex, 4), 4), 8))
def cg_f009_free_cash_flow_core34_3rd_v035_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(_safe_div(fcf, ncfo), 4), 4), 8))
def cg_f009_free_cash_flow_core35_3rd_v036_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core36_3rd_v037_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core37_3rd_v038_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(fcf - ncfo, 4), 4), 8))
def cg_f009_free_cash_flow_core38_3rd_v039_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core39_3rd_v040_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core40_3rd_v041_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(fcf, 4), 8), 12))
def cg_f009_free_cash_flow_core41_3rd_v042_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(fcfps, 4), 8), 12))
def cg_f009_free_cash_flow_core42_3rd_v043_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(ncfo, 4), 8), 12))
def cg_f009_free_cash_flow_core43_3rd_v044_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(capex, 4), 8), 12))
def cg_f009_free_cash_flow_core44_3rd_v045_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_safe_div(fcf, ncfo), 4), 8), 12))
def cg_f009_free_cash_flow_core45_3rd_v046_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core46_3rd_v047_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core47_3rd_v048_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(fcf - ncfo, 4), 8), 12))
def cg_f009_free_cash_flow_core48_3rd_v049_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_log(fcf.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core49_3rd_v050_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core50_3rd_v051_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(fcf, 4), 4), 8))
def cg_f009_free_cash_flow_core51_3rd_v052_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(fcfps, 4), 4), 8))
def cg_f009_free_cash_flow_core52_3rd_v053_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(ncfo, 4), 4), 8))
def cg_f009_free_cash_flow_core53_3rd_v054_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(capex, 4), 4), 8))
def cg_f009_free_cash_flow_core54_3rd_v055_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(_safe_div(fcf, ncfo), 4), 4), 8))
def cg_f009_free_cash_flow_core55_3rd_v056_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core56_3rd_v057_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core57_3rd_v058_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(fcf - ncfo, 4), 4), 8))
def cg_f009_free_cash_flow_core58_3rd_v059_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(_log(fcf.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core59_3rd_v060_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4), 8))
def cg_f009_free_cash_flow_core60_3rd_v061_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(fcf, 4), 4), 12))
def cg_f009_free_cash_flow_core61_3rd_v062_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(fcfps, 4), 4), 12))
def cg_f009_free_cash_flow_core62_3rd_v063_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(ncfo, 4), 4), 12))
def cg_f009_free_cash_flow_core63_3rd_v064_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(capex, 4), 4), 12))
def cg_f009_free_cash_flow_core64_3rd_v065_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(_safe_div(fcf, ncfo), 4), 4), 12))
def cg_f009_free_cash_flow_core65_3rd_v066_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core66_3rd_v067_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core67_3rd_v068_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(fcf - ncfo, 4), 4), 12))
def cg_f009_free_cash_flow_core68_3rd_v069_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core69_3rd_v070_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core70_3rd_v071_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(fcf, 4), 8), 12))
def cg_f009_free_cash_flow_core71_3rd_v072_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(fcfps, 4), 8), 12))
def cg_f009_free_cash_flow_core72_3rd_v073_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(ncfo, 4), 8), 12))
def cg_f009_free_cash_flow_core73_3rd_v074_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(capex, 4), 8), 12))
def cg_f009_free_cash_flow_core74_3rd_v075_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(_safe_div(fcf, ncfo), 4), 8), 12))
def cg_f009_free_cash_flow_core75_3rd_v076_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core76_3rd_v077_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core77_3rd_v078_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(fcf - ncfo, 4), 8), 12))
def cg_f009_free_cash_flow_core78_3rd_v079_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(_log(fcf.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core79_3rd_v080_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8), 12))
def cg_f009_free_cash_flow_core80_3rd_v081_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(fcf, 4), 4), 12))
def cg_f009_free_cash_flow_core81_3rd_v082_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(fcfps, 4), 4), 12))
def cg_f009_free_cash_flow_core82_3rd_v083_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(ncfo, 4), 4), 12))
def cg_f009_free_cash_flow_core83_3rd_v084_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(capex, 4), 4), 12))
def cg_f009_free_cash_flow_core84_3rd_v085_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(_safe_div(fcf, ncfo), 4), 4), 12))
def cg_f009_free_cash_flow_core85_3rd_v086_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core86_3rd_v087_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core87_3rd_v088_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(fcf - ncfo, 4), 4), 12))
def cg_f009_free_cash_flow_core88_3rd_v089_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(_log(fcf.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core89_3rd_v090_signal(fcf, fcfps, ncfo, capex):
    return _clean(_rank(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4), 12))
def cg_f009_free_cash_flow_core90_3rd_v091_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(fcf, 4), 4), 4))
def cg_f009_free_cash_flow_core91_3rd_v092_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(fcfps, 4), 4), 4))
def cg_f009_free_cash_flow_core92_3rd_v093_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core93_3rd_v094_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(capex, 4), 4), 4))
def cg_f009_free_cash_flow_core94_3rd_v095_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(_safe_div(fcf, ncfo), 4), 4), 4))
def cg_f009_free_cash_flow_core95_3rd_v096_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core96_3rd_v097_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core97_3rd_v098_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(fcf - ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core98_3rd_v099_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core99_3rd_v100_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core100_3rd_v101_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(fcf, 4), 8), 4))
def cg_f009_free_cash_flow_core101_3rd_v102_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(fcfps, 4), 8), 4))
def cg_f009_free_cash_flow_core102_3rd_v103_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(ncfo, 4), 8), 4))
def cg_f009_free_cash_flow_core103_3rd_v104_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(capex, 4), 8), 4))
def cg_f009_free_cash_flow_core104_3rd_v105_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(_safe_div(fcf, ncfo), 4), 8), 4))
def cg_f009_free_cash_flow_core105_3rd_v106_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 8), 4))
def cg_f009_free_cash_flow_core106_3rd_v107_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 8), 4))
def cg_f009_free_cash_flow_core107_3rd_v108_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(fcf - ncfo, 4), 8), 4))
def cg_f009_free_cash_flow_core108_3rd_v109_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(_log(fcf.abs() + 1.0), 4), 8), 4))
def cg_f009_free_cash_flow_core109_3rd_v110_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8), 4))
def cg_f009_free_cash_flow_core110_3rd_v111_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(fcf, 4), 4), 4))
def cg_f009_free_cash_flow_core111_3rd_v112_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(fcfps, 4), 4), 4))
def cg_f009_free_cash_flow_core112_3rd_v113_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core113_3rd_v114_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(capex, 4), 4), 4))
def cg_f009_free_cash_flow_core114_3rd_v115_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(_safe_div(fcf, ncfo), 4), 4), 4))
def cg_f009_free_cash_flow_core115_3rd_v116_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core116_3rd_v117_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core117_3rd_v118_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(fcf - ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core118_3rd_v119_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(_log(fcf.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core119_3rd_v120_signal(fcf, fcfps, ncfo, capex):
    return _clean(_mean(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core120_3rd_v121_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(fcf, 4), 4), 4))
def cg_f009_free_cash_flow_core121_3rd_v122_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(fcfps, 4), 4), 4))
def cg_f009_free_cash_flow_core122_3rd_v123_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core123_3rd_v124_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(capex, 4), 4), 4))
def cg_f009_free_cash_flow_core124_3rd_v125_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(_safe_div(fcf, ncfo), 4), 4), 4))
def cg_f009_free_cash_flow_core125_3rd_v126_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core126_3rd_v127_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core127_3rd_v128_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(fcf - ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core128_3rd_v129_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core129_3rd_v130_signal(fcf, fcfps, ncfo, capex):
    return _clean(_slope(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core130_3rd_v131_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(fcf, 4), 4), 4))
def cg_f009_free_cash_flow_core131_3rd_v132_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(fcfps, 4), 4), 4))
def cg_f009_free_cash_flow_core132_3rd_v133_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core133_3rd_v134_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(capex, 4), 4), 4))
def cg_f009_free_cash_flow_core134_3rd_v135_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(_safe_div(fcf, ncfo), 4), 4), 4))
def cg_f009_free_cash_flow_core135_3rd_v136_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core136_3rd_v137_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core137_3rd_v138_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(fcf - ncfo, 4), 4), 4))
def cg_f009_free_cash_flow_core138_3rd_v139_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core139_3rd_v140_signal(fcf, fcfps, ncfo, capex):
    return _clean(_diff(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f009_free_cash_flow_core140_3rd_v141_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(fcf, 4), 4), 4), 8))
def cg_f009_free_cash_flow_core141_3rd_v142_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(fcfps, 4), 4), 4), 8))
def cg_f009_free_cash_flow_core142_3rd_v143_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(ncfo, 4), 4), 4), 8))
def cg_f009_free_cash_flow_core143_3rd_v144_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(capex, 4), 4), 4), 8))
def cg_f009_free_cash_flow_core144_3rd_v145_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(fcf, ncfo), 4), 4), 4), 8))
def cg_f009_free_cash_flow_core145_3rd_v146_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(fcf, capex.abs() + 1.0), 4), 4), 4), 8))
def cg_f009_free_cash_flow_core146_3rd_v147_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, capex.abs() + 1.0), 4), 4), 4), 8))
def cg_f009_free_cash_flow_core147_3rd_v148_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(fcf - ncfo, 4), 4), 4), 8))
def cg_f009_free_cash_flow_core148_3rd_v149_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(_log(fcf.abs() + 1.0), 4), 4), 4), 8))
def cg_f009_free_cash_flow_core149_3rd_v150_signal(fcf, fcfps, ncfo, capex):
    return _clean(_z(_slope(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4), 8))