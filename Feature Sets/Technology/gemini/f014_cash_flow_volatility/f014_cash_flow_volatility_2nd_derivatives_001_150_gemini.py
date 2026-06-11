import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f014_cash_flow_volatility_core00_2nd_v001_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfo, 4))
def cg_f014_cash_flow_volatility_core01_2nd_v002_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(fcf, 4))
def cg_f014_cash_flow_volatility_core02_2nd_v003_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfi, 4))
def cg_f014_cash_flow_volatility_core03_2nd_v004_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncff, 4))
def cg_f014_cash_flow_volatility_core04_2nd_v005_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4))
def cg_f014_cash_flow_volatility_core05_2nd_v006_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfo + ncfi, 4))
def cg_f014_cash_flow_volatility_core06_2nd_v007_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfo + ncff, 4))
def cg_f014_cash_flow_volatility_core07_2nd_v008_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfi + ncff, 4))
def cg_f014_cash_flow_volatility_core08_2nd_v009_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4))
def cg_f014_cash_flow_volatility_core09_2nd_v010_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_log(ncfo.abs() + 1.0), 4))
def cg_f014_cash_flow_volatility_core10_2nd_v011_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfo, 8))
def cg_f014_cash_flow_volatility_core11_2nd_v012_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(fcf, 8))
def cg_f014_cash_flow_volatility_core12_2nd_v013_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfi, 8))
def cg_f014_cash_flow_volatility_core13_2nd_v014_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncff, 8))
def cg_f014_cash_flow_volatility_core14_2nd_v015_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 8))
def cg_f014_cash_flow_volatility_core15_2nd_v016_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfo + ncfi, 8))
def cg_f014_cash_flow_volatility_core16_2nd_v017_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfo + ncff, 8))
def cg_f014_cash_flow_volatility_core17_2nd_v018_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(ncfi + ncff, 8))
def cg_f014_cash_flow_volatility_core18_2nd_v019_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 8))
def cg_f014_cash_flow_volatility_core19_2nd_v020_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_log(ncfo.abs() + 1.0), 8))
def cg_f014_cash_flow_volatility_core20_2nd_v021_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(ncfo, 4))
def cg_f014_cash_flow_volatility_core21_2nd_v022_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(fcf, 4))
def cg_f014_cash_flow_volatility_core22_2nd_v023_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(ncfi, 4))
def cg_f014_cash_flow_volatility_core23_2nd_v024_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(ncff, 4))
def cg_f014_cash_flow_volatility_core24_2nd_v025_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4))
def cg_f014_cash_flow_volatility_core25_2nd_v026_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(ncfo + ncfi, 4))
def cg_f014_cash_flow_volatility_core26_2nd_v027_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(ncfo + ncff, 4))
def cg_f014_cash_flow_volatility_core27_2nd_v028_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(ncfi + ncff, 4))
def cg_f014_cash_flow_volatility_core28_2nd_v029_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4))
def cg_f014_cash_flow_volatility_core29_2nd_v030_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_log(ncfo.abs() + 1.0), 4))
def cg_f014_cash_flow_volatility_core30_2nd_v031_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f014_cash_flow_volatility_core31_2nd_v032_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(fcf, 4), 8))
def cg_f014_cash_flow_volatility_core32_2nd_v033_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfi, 4), 8))
def cg_f014_cash_flow_volatility_core33_2nd_v034_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncff, 4), 8))
def cg_f014_cash_flow_volatility_core34_2nd_v035_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4), 8))
def cg_f014_cash_flow_volatility_core35_2nd_v036_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfo + ncfi, 4), 8))
def cg_f014_cash_flow_volatility_core36_2nd_v037_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfo + ncff, 4), 8))
def cg_f014_cash_flow_volatility_core37_2nd_v038_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfi + ncff, 4), 8))
def cg_f014_cash_flow_volatility_core38_2nd_v039_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4), 8))
def cg_f014_cash_flow_volatility_core39_2nd_v040_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(_log(ncfo.abs() + 1.0), 4), 8))
def cg_f014_cash_flow_volatility_core40_2nd_v041_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f014_cash_flow_volatility_core41_2nd_v042_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(fcf, 8), 12))
def cg_f014_cash_flow_volatility_core42_2nd_v043_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfi, 8), 12))
def cg_f014_cash_flow_volatility_core43_2nd_v044_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncff, 8), 12))
def cg_f014_cash_flow_volatility_core44_2nd_v045_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 8), 12))
def cg_f014_cash_flow_volatility_core45_2nd_v046_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfo + ncfi, 8), 12))
def cg_f014_cash_flow_volatility_core46_2nd_v047_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfo + ncff, 8), 12))
def cg_f014_cash_flow_volatility_core47_2nd_v048_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(ncfi + ncff, 8), 12))
def cg_f014_cash_flow_volatility_core48_2nd_v049_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 8), 12))
def cg_f014_cash_flow_volatility_core49_2nd_v050_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_slope(_log(ncfo.abs() + 1.0), 8), 12))
def cg_f014_cash_flow_volatility_core50_2nd_v051_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f014_cash_flow_volatility_core51_2nd_v052_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(fcf, 4), 8))
def cg_f014_cash_flow_volatility_core52_2nd_v053_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(ncfi, 4), 8))
def cg_f014_cash_flow_volatility_core53_2nd_v054_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(ncff, 4), 8))
def cg_f014_cash_flow_volatility_core54_2nd_v055_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4), 8))
def cg_f014_cash_flow_volatility_core55_2nd_v056_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(ncfo + ncfi, 4), 8))
def cg_f014_cash_flow_volatility_core56_2nd_v057_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(ncfo + ncff, 4), 8))
def cg_f014_cash_flow_volatility_core57_2nd_v058_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(ncfi + ncff, 4), 8))
def cg_f014_cash_flow_volatility_core58_2nd_v059_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4), 8))
def cg_f014_cash_flow_volatility_core59_2nd_v060_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_log(ncfo.abs() + 1.0), 4), 8))
def cg_f014_cash_flow_volatility_core60_2nd_v061_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f014_cash_flow_volatility_core61_2nd_v062_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(fcf, 4), 12))
def cg_f014_cash_flow_volatility_core62_2nd_v063_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(ncfi, 4), 12))
def cg_f014_cash_flow_volatility_core63_2nd_v064_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(ncff, 4), 12))
def cg_f014_cash_flow_volatility_core64_2nd_v065_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4), 12))
def cg_f014_cash_flow_volatility_core65_2nd_v066_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(ncfo + ncfi, 4), 12))
def cg_f014_cash_flow_volatility_core66_2nd_v067_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(ncfo + ncff, 4), 12))
def cg_f014_cash_flow_volatility_core67_2nd_v068_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(ncfi + ncff, 4), 12))
def cg_f014_cash_flow_volatility_core68_2nd_v069_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4), 12))
def cg_f014_cash_flow_volatility_core69_2nd_v070_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_log(ncfo.abs() + 1.0), 4), 12))
def cg_f014_cash_flow_volatility_core70_2nd_v071_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f014_cash_flow_volatility_core71_2nd_v072_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(fcf, 4), 12))
def cg_f014_cash_flow_volatility_core72_2nd_v073_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(ncfi, 4), 12))
def cg_f014_cash_flow_volatility_core73_2nd_v074_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(ncff, 4), 12))
def cg_f014_cash_flow_volatility_core74_2nd_v075_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4), 12))
def cg_f014_cash_flow_volatility_core75_2nd_v076_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(ncfo + ncfi, 4), 12))
def cg_f014_cash_flow_volatility_core76_2nd_v077_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(ncfo + ncff, 4), 12))
def cg_f014_cash_flow_volatility_core77_2nd_v078_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(ncfi + ncff, 4), 12))
def cg_f014_cash_flow_volatility_core78_2nd_v079_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4), 12))
def cg_f014_cash_flow_volatility_core79_2nd_v080_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_diff(_log(ncfo.abs() + 1.0), 4), 12))
def cg_f014_cash_flow_volatility_core80_2nd_v081_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f014_cash_flow_volatility_core81_2nd_v082_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(fcf, 4), 4))
def cg_f014_cash_flow_volatility_core82_2nd_v083_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core83_2nd_v084_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(ncff, 4), 4))
def cg_f014_cash_flow_volatility_core84_2nd_v085_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core85_2nd_v086_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(ncfo + ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core86_2nd_v087_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(ncfo + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core87_2nd_v088_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(ncfi + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core88_2nd_v089_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core89_2nd_v090_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_slope(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core90_2nd_v091_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f014_cash_flow_volatility_core91_2nd_v092_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(fcf, 4), 4))
def cg_f014_cash_flow_volatility_core92_2nd_v093_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core93_2nd_v094_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(ncff, 4), 4))
def cg_f014_cash_flow_volatility_core94_2nd_v095_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core95_2nd_v096_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(ncfo + ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core96_2nd_v097_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(ncfo + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core97_2nd_v098_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(ncfi + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core98_2nd_v099_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core99_2nd_v100_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_mean(_diff(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core100_2nd_v101_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f014_cash_flow_volatility_core101_2nd_v102_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(fcf, 4), 4))
def cg_f014_cash_flow_volatility_core102_2nd_v103_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core103_2nd_v104_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncff, 4), 4))
def cg_f014_cash_flow_volatility_core104_2nd_v105_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core105_2nd_v106_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfo + ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core106_2nd_v107_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfo + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core107_2nd_v108_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfi + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core108_2nd_v109_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core109_2nd_v110_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core110_2nd_v111_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f014_cash_flow_volatility_core111_2nd_v112_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(fcf, 8), 8))
def cg_f014_cash_flow_volatility_core112_2nd_v113_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfi, 8), 8))
def cg_f014_cash_flow_volatility_core113_2nd_v114_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncff, 8), 8))
def cg_f014_cash_flow_volatility_core114_2nd_v115_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 8), 8))
def cg_f014_cash_flow_volatility_core115_2nd_v116_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfo + ncfi, 8), 8))
def cg_f014_cash_flow_volatility_core116_2nd_v117_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfo + ncff, 8), 8))
def cg_f014_cash_flow_volatility_core117_2nd_v118_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(ncfi + ncff, 8), 8))
def cg_f014_cash_flow_volatility_core118_2nd_v119_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 8), 8))
def cg_f014_cash_flow_volatility_core119_2nd_v120_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_slope(_mean(_log(ncfo.abs() + 1.0), 8), 8))
def cg_f014_cash_flow_volatility_core120_2nd_v121_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f014_cash_flow_volatility_core121_2nd_v122_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(fcf, 4), 4))
def cg_f014_cash_flow_volatility_core122_2nd_v123_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core123_2nd_v124_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(ncff, 4), 4))
def cg_f014_cash_flow_volatility_core124_2nd_v125_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core125_2nd_v126_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(ncfo + ncfi, 4), 4))
def cg_f014_cash_flow_volatility_core126_2nd_v127_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(ncfo + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core127_2nd_v128_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(ncfi + ncff, 4), 4))
def cg_f014_cash_flow_volatility_core128_2nd_v129_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core129_2nd_v130_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_diff(_mean(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f014_cash_flow_volatility_core130_2nd_v131_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f014_cash_flow_volatility_core131_2nd_v132_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(fcf, 4), 4), 8))
def cg_f014_cash_flow_volatility_core132_2nd_v133_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(ncfi, 4), 4), 8))
def cg_f014_cash_flow_volatility_core133_2nd_v134_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(ncff, 4), 4), 8))
def cg_f014_cash_flow_volatility_core134_2nd_v135_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4), 8))
def cg_f014_cash_flow_volatility_core135_2nd_v136_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(ncfo + ncfi, 4), 4), 8))
def cg_f014_cash_flow_volatility_core136_2nd_v137_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(ncfo + ncff, 4), 4), 8))
def cg_f014_cash_flow_volatility_core137_2nd_v138_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(ncfi + ncff, 4), 4), 8))
def cg_f014_cash_flow_volatility_core138_2nd_v139_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4), 8))
def cg_f014_cash_flow_volatility_core139_2nd_v140_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_z(_diff(_mean(_log(ncfo.abs() + 1.0), 4), 4), 8))
def cg_f014_cash_flow_volatility_core140_2nd_v141_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f014_cash_flow_volatility_core141_2nd_v142_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(fcf, 4), 4), 12))
def cg_f014_cash_flow_volatility_core142_2nd_v143_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(ncfi, 4), 4), 12))
def cg_f014_cash_flow_volatility_core143_2nd_v144_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(ncff, 4), 4), 12))
def cg_f014_cash_flow_volatility_core144_2nd_v145_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(_safe_div(fcf, ncfo.abs() + 1.0), 4), 4), 12))
def cg_f014_cash_flow_volatility_core145_2nd_v146_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(ncfo + ncfi, 4), 4), 12))
def cg_f014_cash_flow_volatility_core146_2nd_v147_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(ncfo + ncff, 4), 4), 12))
def cg_f014_cash_flow_volatility_core147_2nd_v148_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(ncfi + ncff, 4), 4), 12))
def cg_f014_cash_flow_volatility_core148_2nd_v149_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, fcf.abs() + 1.0), 4), 4), 12))
def cg_f014_cash_flow_volatility_core149_2nd_v150_signal(ncfo, fcf, ncfi, ncff):
    return _clean(_rank(_slope(_mean(_log(ncfo.abs() + 1.0), 4), 4), 12))