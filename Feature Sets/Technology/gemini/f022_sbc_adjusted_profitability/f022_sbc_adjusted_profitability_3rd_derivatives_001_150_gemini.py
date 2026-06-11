import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f022_sbc_adjusted_profitability_core00_3rd_v001_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core01_3rd_v002_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(opinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core02_3rd_v003_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(fcf, 4), 4))
def cg_f022_sbc_adjusted_profitability_core03_3rd_v004_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(netinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core04_3rd_v005_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(opinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core05_3rd_v006_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(netinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core06_3rd_v007_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(fcf - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core07_3rd_v008_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core08_3rd_v009_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core09_3rd_v010_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core10_3rd_v011_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core11_3rd_v012_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(opinc, 4), 8))
def cg_f022_sbc_adjusted_profitability_core12_3rd_v013_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(fcf, 4), 8))
def cg_f022_sbc_adjusted_profitability_core13_3rd_v014_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(netinc, 4), 8))
def cg_f022_sbc_adjusted_profitability_core14_3rd_v015_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(opinc - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core15_3rd_v016_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(netinc - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core16_3rd_v017_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(fcf - sbcomp, 4), 8))
def cg_f022_sbc_adjusted_profitability_core17_3rd_v018_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core18_3rd_v019_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core19_3rd_v020_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 8))
def cg_f022_sbc_adjusted_profitability_core20_3rd_v021_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core21_3rd_v022_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(opinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core22_3rd_v023_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(fcf, 4), 4))
def cg_f022_sbc_adjusted_profitability_core23_3rd_v024_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(netinc, 4), 4))
def cg_f022_sbc_adjusted_profitability_core24_3rd_v025_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(opinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core25_3rd_v026_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(netinc - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core26_3rd_v027_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(fcf - sbcomp, 4), 4))
def cg_f022_sbc_adjusted_profitability_core27_3rd_v028_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core28_3rd_v029_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core29_3rd_v030_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4))
def cg_f022_sbc_adjusted_profitability_core30_3rd_v031_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core31_3rd_v032_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(opinc, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core32_3rd_v033_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(fcf, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core33_3rd_v034_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(netinc, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core34_3rd_v035_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(opinc - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core35_3rd_v036_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(netinc - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core36_3rd_v037_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(fcf - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core37_3rd_v038_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core38_3rd_v039_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core39_3rd_v040_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core40_3rd_v041_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core41_3rd_v042_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(opinc, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core42_3rd_v043_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(fcf, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core43_3rd_v044_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(netinc, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core44_3rd_v045_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(opinc - sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core45_3rd_v046_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(netinc - sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core46_3rd_v047_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(fcf - sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core47_3rd_v048_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core48_3rd_v049_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core49_3rd_v050_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core50_3rd_v051_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core51_3rd_v052_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(opinc, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core52_3rd_v053_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(fcf, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core53_3rd_v054_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(netinc, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core54_3rd_v055_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(opinc - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core55_3rd_v056_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(netinc - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core56_3rd_v057_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(fcf - sbcomp, 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core57_3rd_v058_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core58_3rd_v059_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core59_3rd_v060_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_diff(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core60_3rd_v061_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core61_3rd_v062_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(opinc, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core62_3rd_v063_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(fcf, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core63_3rd_v064_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(netinc, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core64_3rd_v065_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(opinc - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core65_3rd_v066_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(netinc - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core66_3rd_v067_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(fcf - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core67_3rd_v068_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core68_3rd_v069_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core69_3rd_v070_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core70_3rd_v071_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core71_3rd_v072_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(opinc, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core72_3rd_v073_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(fcf, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core73_3rd_v074_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(netinc, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core74_3rd_v075_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(opinc - sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core75_3rd_v076_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(netinc - sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core76_3rd_v077_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(fcf - sbcomp, 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core77_3rd_v078_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core78_3rd_v079_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core79_3rd_v080_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_slope(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 8), 12))
def cg_f022_sbc_adjusted_profitability_core80_3rd_v081_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core81_3rd_v082_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(opinc, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core82_3rd_v083_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(fcf, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core83_3rd_v084_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(netinc, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core84_3rd_v085_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(opinc - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core85_3rd_v086_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(netinc - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core86_3rd_v087_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(fcf - sbcomp, 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core87_3rd_v088_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core88_3rd_v089_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core89_3rd_v090_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_rank(_diff(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 12))
def cg_f022_sbc_adjusted_profitability_core90_3rd_v091_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core91_3rd_v092_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(opinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core92_3rd_v093_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(fcf, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core93_3rd_v094_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(netinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core94_3rd_v095_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(opinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core95_3rd_v096_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(netinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core96_3rd_v097_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(fcf - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core97_3rd_v098_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core98_3rd_v099_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core99_3rd_v100_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core100_3rd_v101_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(sbcomp, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core101_3rd_v102_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(opinc, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core102_3rd_v103_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(fcf, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core103_3rd_v104_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(netinc, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core104_3rd_v105_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(opinc - sbcomp, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core105_3rd_v106_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(netinc - sbcomp, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core106_3rd_v107_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(fcf - sbcomp, 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core107_3rd_v108_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core108_3rd_v109_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core109_3rd_v110_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_slope(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 8), 4))
def cg_f022_sbc_adjusted_profitability_core110_3rd_v111_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core111_3rd_v112_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(opinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core112_3rd_v113_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(fcf, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core113_3rd_v114_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(netinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core114_3rd_v115_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(opinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core115_3rd_v116_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(netinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core116_3rd_v117_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(fcf - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core117_3rd_v118_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core118_3rd_v119_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core119_3rd_v120_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_mean(_diff(_slope(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core120_3rd_v121_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core121_3rd_v122_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(opinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core122_3rd_v123_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(fcf, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core123_3rd_v124_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(netinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core124_3rd_v125_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(opinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core125_3rd_v126_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(netinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core126_3rd_v127_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(fcf - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core127_3rd_v128_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core128_3rd_v129_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core129_3rd_v130_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_slope(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core130_3rd_v131_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core131_3rd_v132_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(opinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core132_3rd_v133_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(fcf, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core133_3rd_v134_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(netinc, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core134_3rd_v135_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(opinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core135_3rd_v136_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(netinc - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core136_3rd_v137_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(fcf - sbcomp, 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core137_3rd_v138_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core138_3rd_v139_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core139_3rd_v140_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_diff(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 4))
def cg_f022_sbc_adjusted_profitability_core140_3rd_v141_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(sbcomp, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core141_3rd_v142_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(opinc, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core142_3rd_v143_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(fcf, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core143_3rd_v144_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(netinc, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core144_3rd_v145_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(opinc - sbcomp, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core145_3rd_v146_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(netinc - sbcomp, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core146_3rd_v147_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(fcf - sbcomp, 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core147_3rd_v148_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, opinc.abs() + 1.0), 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core148_3rd_v149_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, netinc.abs() + 1.0), 4), 4), 4), 8))
def cg_f022_sbc_adjusted_profitability_core149_3rd_v150_signal(sbcomp, opinc, fcf, netinc):
    return _clean(_z(_slope(_diff(_diff(_safe_div(sbcomp, fcf.abs() + 1.0), 4), 4), 4), 8))