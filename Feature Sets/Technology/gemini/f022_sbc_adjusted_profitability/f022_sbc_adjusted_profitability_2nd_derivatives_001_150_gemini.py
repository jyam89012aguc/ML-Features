import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f022_sbc_adjusted_profitability_core00_2nd_v001_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core01_2nd_v002_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(opinc, 4))
def cg_f022_sbc_adjusted_profitability_core02_2nd_v003_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(fcf, 4))
def cg_f022_sbc_adjusted_profitability_core03_2nd_v004_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(netinc, 4))
def cg_f022_sbc_adjusted_profitability_core04_2nd_v005_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(opinc - sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core05_2nd_v006_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(netinc - sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core06_2nd_v007_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(fcf - sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core07_2nd_v008_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core08_2nd_v009_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core09_2nd_v010_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core10_2nd_v011_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(sbcomp, 8))
def cg_f022_sbc_adjusted_profitability_core11_2nd_v012_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(opinc, 8))
def cg_f022_sbc_adjusted_profitability_core12_2nd_v013_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(fcf, 8))
def cg_f022_sbc_adjusted_profitability_core13_2nd_v014_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(netinc, 8))
def cg_f022_sbc_adjusted_profitability_core14_2nd_v015_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(opinc - sbcomp, 8))
def cg_f022_sbc_adjusted_profitability_core15_2nd_v016_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(netinc - sbcomp, 8))
def cg_f022_sbc_adjusted_profitability_core16_2nd_v017_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(fcf - sbcomp, 8))
def cg_f022_sbc_adjusted_profitability_core17_2nd_v018_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core18_2nd_v019_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core19_2nd_v020_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 8))
def cg_f022_sbc_adjusted_profitability_core20_2nd_v021_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core21_2nd_v022_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(opinc, 4))
def cg_f022_sbc_adjusted_profitability_core22_2nd_v023_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(fcf, 4))
def cg_f022_sbc_adjusted_profitability_core23_2nd_v024_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(netinc, 4))
def cg_f022_sbc_adjusted_profitability_core24_2nd_v025_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(opinc - sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core25_2nd_v026_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(netinc - sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core26_2nd_v027_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(fcf - sbcomp, 4))
def cg_f022_sbc_adjusted_profitability_core27_2nd_v028_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core28_2nd_v029_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core29_2nd_v030_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4))
def cg_f022_sbc_adjusted_profitability_core30_2nd_v031_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core31_2nd_v032_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(opinc, 4), 8))
def cg_f022_sbc_adjusted_profitability_core32_2nd_v033_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(fcf, 4), 8))
def cg_f022_sbc_adjusted_profitability_core33_2nd_v034_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(netinc, 4), 8))
def cg_f022_sbc_adjusted_profitability_core34_2nd_v035_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(opinc - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core35_2nd_v036_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(netinc - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core36_2nd_v037_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(fcf - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core37_2nd_v038_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core38_2nd_v039_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core39_2nd_v040_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core40_2nd_v041_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(sbcomp, 8), 12))
def cg_f022_sbc_adjusted_profitability_core41_2nd_v042_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(opinc, 8), 12))
def cg_f022_sbc_adjusted_profitability_core42_2nd_v043_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(fcf, 8), 12))
def cg_f022_sbc_adjusted_profitability_core43_2nd_v044_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(netinc, 8), 12))
def cg_f022_sbc_adjusted_profitability_core44_2nd_v045_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(opinc - sbcomp, 8), 12))
def cg_f022_sbc_adjusted_profitability_core45_2nd_v046_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(netinc - sbcomp, 8), 12))
def cg_f022_sbc_adjusted_profitability_core46_2nd_v047_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(fcf - sbcomp, 8), 12))
def cg_f022_sbc_adjusted_profitability_core47_2nd_v048_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 8), 12))
def cg_f022_sbc_adjusted_profitability_core48_2nd_v049_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 8), 12))
def cg_f022_sbc_adjusted_profitability_core49_2nd_v050_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 8), 12))
def cg_f022_sbc_adjusted_profitability_core50_2nd_v051_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core51_2nd_v052_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(opinc, 4), 8))
def cg_f022_sbc_adjusted_profitability_core52_2nd_v053_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(fcf, 4), 8))
def cg_f022_sbc_adjusted_profitability_core53_2nd_v054_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(netinc, 4), 8))
def cg_f022_sbc_adjusted_profitability_core54_2nd_v055_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(opinc - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core55_2nd_v056_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(netinc - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core56_2nd_v057_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(fcf - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core57_2nd_v058_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core58_2nd_v059_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core59_2nd_v060_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core60_2nd_v061_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core61_2nd_v062_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(opinc, 4), 12))
def cg_f022_sbc_adjusted_profitability_core62_2nd_v063_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(fcf, 4), 12))
def cg_f022_sbc_adjusted_profitability_core63_2nd_v064_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(netinc, 4), 12))
def cg_f022_sbc_adjusted_profitability_core64_2nd_v065_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(opinc - sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core65_2nd_v066_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(netinc - sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core66_2nd_v067_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(fcf - sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core67_2nd_v068_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 12))
def cg_f022_sbc_adjusted_profitability_core68_2nd_v069_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 12))
def cg_f022_sbc_adjusted_profitability_core69_2nd_v070_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 12))
def cg_f022_sbc_adjusted_profitability_core70_2nd_v071_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core71_2nd_v072_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(opinc, 4), 12))
def cg_f022_sbc_adjusted_profitability_core72_2nd_v073_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(fcf, 4), 12))
def cg_f022_sbc_adjusted_profitability_core73_2nd_v074_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(netinc, 4), 12))
def cg_f022_sbc_adjusted_profitability_core74_2nd_v075_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(opinc - sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core75_2nd_v076_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(netinc - sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core76_2nd_v077_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(fcf - sbcomp, 4), 12))
def cg_f022_sbc_adjusted_profitability_core77_2nd_v078_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 12))
def cg_f022_sbc_adjusted_profitability_core78_2nd_v079_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 12))
def cg_f022_sbc_adjusted_profitability_core79_2nd_v080_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 12))
def cg_f022_sbc_adjusted_profitability_core80_2nd_v081_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core81_2nd_v082_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(opinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core82_2nd_v083_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(fcf, 4), 4))
def cg_f022_sbc_adjusted_profitability_core83_2nd_v084_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(netinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core84_2nd_v085_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(opinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core85_2nd_v086_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(netinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core86_2nd_v087_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(fcf - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core87_2nd_v088_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core88_2nd_v089_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core89_2nd_v090_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core90_2nd_v091_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core91_2nd_v092_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(opinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core92_2nd_v093_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(fcf, 4), 4))
def cg_f022_sbc_adjusted_profitability_core93_2nd_v094_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(netinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core94_2nd_v095_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(opinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core95_2nd_v096_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(netinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core96_2nd_v097_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(fcf - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core97_2nd_v098_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core98_2nd_v099_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core99_2nd_v100_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core100_2nd_v101_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core101_2nd_v102_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(opinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core102_2nd_v103_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(fcf, 4), 4))
def cg_f022_sbc_adjusted_profitability_core103_2nd_v104_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(netinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core104_2nd_v105_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(opinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core105_2nd_v106_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(netinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core106_2nd_v107_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(fcf - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core107_2nd_v108_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core108_2nd_v109_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core109_2nd_v110_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core110_2nd_v111_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(sbcomp, 8), 8))
def cg_f022_sbc_adjusted_profitability_core111_2nd_v112_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(opinc, 8), 8))
def cg_f022_sbc_adjusted_profitability_core112_2nd_v113_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(fcf, 8), 8))
def cg_f022_sbc_adjusted_profitability_core113_2nd_v114_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(netinc, 8), 8))
def cg_f022_sbc_adjusted_profitability_core114_2nd_v115_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(opinc - sbcomp, 8), 8))
def cg_f022_sbc_adjusted_profitability_core115_2nd_v116_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(netinc - sbcomp, 8), 8))
def cg_f022_sbc_adjusted_profitability_core116_2nd_v117_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(fcf - sbcomp, 8), 8))
def cg_f022_sbc_adjusted_profitability_core117_2nd_v118_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(_safe_div(sbcomp, opinc.abs() + 1.0), 8), 8))
def cg_f022_sbc_adjusted_profitability_core118_2nd_v119_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 8), 8))
def cg_f022_sbc_adjusted_profitability_core119_2nd_v120_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_mean(_safe_div(sbcomp, fcf.abs() + 1.0), 8), 8))
def cg_f022_sbc_adjusted_profitability_core120_2nd_v121_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core121_2nd_v122_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(opinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core122_2nd_v123_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(fcf, 4), 4))
def cg_f022_sbc_adjusted_profitability_core123_2nd_v124_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(netinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core124_2nd_v125_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(opinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core125_2nd_v126_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(netinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core126_2nd_v127_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(fcf - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core127_2nd_v128_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core128_2nd_v129_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core129_2nd_v130_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_mean(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core130_2nd_v131_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core131_2nd_v132_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(opinc, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core132_2nd_v133_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(fcf, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core133_2nd_v134_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(netinc, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core134_2nd_v135_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(opinc - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core135_2nd_v136_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(netinc - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core136_2nd_v137_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(fcf - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core137_2nd_v138_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core138_2nd_v139_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core139_2nd_v140_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_mean(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core140_2nd_v141_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core141_2nd_v142_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(opinc, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core142_2nd_v143_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(fcf, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core143_2nd_v144_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(netinc, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core144_2nd_v145_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(opinc - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core145_2nd_v146_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(netinc - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core146_2nd_v147_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(fcf - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core147_2nd_v148_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core148_2nd_v149_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core149_2nd_v150_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_mean(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 12))