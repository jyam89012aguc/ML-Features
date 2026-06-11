import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f076_fundamental_volatility_core00_2nd_v001_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(revenue, 4))
def cg_f076_fundamental_volatility_core01_2nd_v002_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(ncfo, 4))
def cg_f076_fundamental_volatility_core02_2nd_v003_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(rnd, 4))
def cg_f076_fundamental_volatility_core03_2nd_v004_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(netinc, 4))
def cg_f076_fundamental_volatility_core04_2nd_v005_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(opinc, 4))
def cg_f076_fundamental_volatility_core05_2nd_v006_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_std(revenue, 4), 4))
def cg_f076_fundamental_volatility_core06_2nd_v007_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_std(ncfo, 4), 4))
def cg_f076_fundamental_volatility_core07_2nd_v008_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_std(netinc, 4), 4))
def cg_f076_fundamental_volatility_core08_2nd_v009_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core09_2nd_v010_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core10_2nd_v011_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(revenue, 8))
def cg_f076_fundamental_volatility_core11_2nd_v012_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(ncfo, 8))
def cg_f076_fundamental_volatility_core12_2nd_v013_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(rnd, 8))
def cg_f076_fundamental_volatility_core13_2nd_v014_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(netinc, 8))
def cg_f076_fundamental_volatility_core14_2nd_v015_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(opinc, 8))
def cg_f076_fundamental_volatility_core15_2nd_v016_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_std(revenue, 4), 8))
def cg_f076_fundamental_volatility_core16_2nd_v017_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_std(ncfo, 4), 8))
def cg_f076_fundamental_volatility_core17_2nd_v018_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_std(netinc, 4), 8))
def cg_f076_fundamental_volatility_core18_2nd_v019_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core19_2nd_v020_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 8))
def cg_f076_fundamental_volatility_core20_2nd_v021_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(revenue, 4))
def cg_f076_fundamental_volatility_core21_2nd_v022_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(ncfo, 4))
def cg_f076_fundamental_volatility_core22_2nd_v023_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(rnd, 4))
def cg_f076_fundamental_volatility_core23_2nd_v024_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(netinc, 4))
def cg_f076_fundamental_volatility_core24_2nd_v025_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(opinc, 4))
def cg_f076_fundamental_volatility_core25_2nd_v026_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_std(revenue, 4), 4))
def cg_f076_fundamental_volatility_core26_2nd_v027_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_std(ncfo, 4), 4))
def cg_f076_fundamental_volatility_core27_2nd_v028_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_std(netinc, 4), 4))
def cg_f076_fundamental_volatility_core28_2nd_v029_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core29_2nd_v030_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4))
def cg_f076_fundamental_volatility_core30_2nd_v031_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(revenue, 4), 8))
def cg_f076_fundamental_volatility_core31_2nd_v032_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f076_fundamental_volatility_core32_2nd_v033_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(rnd, 4), 8))
def cg_f076_fundamental_volatility_core33_2nd_v034_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(netinc, 4), 8))
def cg_f076_fundamental_volatility_core34_2nd_v035_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(opinc, 4), 8))
def cg_f076_fundamental_volatility_core35_2nd_v036_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_std(revenue, 4), 4), 8))
def cg_f076_fundamental_volatility_core36_2nd_v037_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_std(ncfo, 4), 4), 8))
def cg_f076_fundamental_volatility_core37_2nd_v038_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_std(netinc, 4), 4), 8))
def cg_f076_fundamental_volatility_core38_2nd_v039_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 8))
def cg_f076_fundamental_volatility_core39_2nd_v040_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 8))
def cg_f076_fundamental_volatility_core40_2nd_v041_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(revenue, 8), 12))
def cg_f076_fundamental_volatility_core41_2nd_v042_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f076_fundamental_volatility_core42_2nd_v043_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(rnd, 8), 12))
def cg_f076_fundamental_volatility_core43_2nd_v044_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(netinc, 8), 12))
def cg_f076_fundamental_volatility_core44_2nd_v045_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(opinc, 8), 12))
def cg_f076_fundamental_volatility_core45_2nd_v046_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_std(revenue, 4), 8), 12))
def cg_f076_fundamental_volatility_core46_2nd_v047_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_std(ncfo, 4), 8), 12))
def cg_f076_fundamental_volatility_core47_2nd_v048_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_std(netinc, 4), 8), 12))
def cg_f076_fundamental_volatility_core48_2nd_v049_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 8), 12))
def cg_f076_fundamental_volatility_core49_2nd_v050_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_slope(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 8), 12))
def cg_f076_fundamental_volatility_core50_2nd_v051_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(revenue, 4), 8))
def cg_f076_fundamental_volatility_core51_2nd_v052_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f076_fundamental_volatility_core52_2nd_v053_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(rnd, 4), 8))
def cg_f076_fundamental_volatility_core53_2nd_v054_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(netinc, 4), 8))
def cg_f076_fundamental_volatility_core54_2nd_v055_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(opinc, 4), 8))
def cg_f076_fundamental_volatility_core55_2nd_v056_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_std(revenue, 4), 4), 8))
def cg_f076_fundamental_volatility_core56_2nd_v057_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_std(ncfo, 4), 4), 8))
def cg_f076_fundamental_volatility_core57_2nd_v058_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_std(netinc, 4), 4), 8))
def cg_f076_fundamental_volatility_core58_2nd_v059_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 8))
def cg_f076_fundamental_volatility_core59_2nd_v060_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 8))
def cg_f076_fundamental_volatility_core60_2nd_v061_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(revenue, 4), 12))
def cg_f076_fundamental_volatility_core61_2nd_v062_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f076_fundamental_volatility_core62_2nd_v063_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(rnd, 4), 12))
def cg_f076_fundamental_volatility_core63_2nd_v064_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(netinc, 4), 12))
def cg_f076_fundamental_volatility_core64_2nd_v065_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(opinc, 4), 12))
def cg_f076_fundamental_volatility_core65_2nd_v066_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_std(revenue, 4), 4), 12))
def cg_f076_fundamental_volatility_core66_2nd_v067_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_std(ncfo, 4), 4), 12))
def cg_f076_fundamental_volatility_core67_2nd_v068_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_std(netinc, 4), 4), 12))
def cg_f076_fundamental_volatility_core68_2nd_v069_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 12))
def cg_f076_fundamental_volatility_core69_2nd_v070_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 12))
def cg_f076_fundamental_volatility_core70_2nd_v071_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(revenue, 4), 12))
def cg_f076_fundamental_volatility_core71_2nd_v072_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f076_fundamental_volatility_core72_2nd_v073_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(rnd, 4), 12))
def cg_f076_fundamental_volatility_core73_2nd_v074_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(netinc, 4), 12))
def cg_f076_fundamental_volatility_core74_2nd_v075_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(opinc, 4), 12))
def cg_f076_fundamental_volatility_core75_2nd_v076_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(_std(revenue, 4), 4), 12))
def cg_f076_fundamental_volatility_core76_2nd_v077_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(_std(ncfo, 4), 4), 12))
def cg_f076_fundamental_volatility_core77_2nd_v078_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(_std(netinc, 4), 4), 12))
def cg_f076_fundamental_volatility_core78_2nd_v079_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 12))
def cg_f076_fundamental_volatility_core79_2nd_v080_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_diff(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 12))
def cg_f076_fundamental_volatility_core80_2nd_v081_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(revenue, 4), 4))
def cg_f076_fundamental_volatility_core81_2nd_v082_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f076_fundamental_volatility_core82_2nd_v083_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(rnd, 4), 4))
def cg_f076_fundamental_volatility_core83_2nd_v084_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(netinc, 4), 4))
def cg_f076_fundamental_volatility_core84_2nd_v085_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(opinc, 4), 4))
def cg_f076_fundamental_volatility_core85_2nd_v086_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(_std(revenue, 4), 4), 4))
def cg_f076_fundamental_volatility_core86_2nd_v087_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(_std(ncfo, 4), 4), 4))
def cg_f076_fundamental_volatility_core87_2nd_v088_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(_std(netinc, 4), 4), 4))
def cg_f076_fundamental_volatility_core88_2nd_v089_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core89_2nd_v090_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_slope(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core90_2nd_v091_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(revenue, 4), 4))
def cg_f076_fundamental_volatility_core91_2nd_v092_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f076_fundamental_volatility_core92_2nd_v093_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(rnd, 4), 4))
def cg_f076_fundamental_volatility_core93_2nd_v094_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(netinc, 4), 4))
def cg_f076_fundamental_volatility_core94_2nd_v095_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(opinc, 4), 4))
def cg_f076_fundamental_volatility_core95_2nd_v096_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(_std(revenue, 4), 4), 4))
def cg_f076_fundamental_volatility_core96_2nd_v097_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(_std(ncfo, 4), 4), 4))
def cg_f076_fundamental_volatility_core97_2nd_v098_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(_std(netinc, 4), 4), 4))
def cg_f076_fundamental_volatility_core98_2nd_v099_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core99_2nd_v100_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_mean(_diff(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core100_2nd_v101_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(revenue, 4), 4))
def cg_f076_fundamental_volatility_core101_2nd_v102_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f076_fundamental_volatility_core102_2nd_v103_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(rnd, 4), 4))
def cg_f076_fundamental_volatility_core103_2nd_v104_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(netinc, 4), 4))
def cg_f076_fundamental_volatility_core104_2nd_v105_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(opinc, 4), 4))
def cg_f076_fundamental_volatility_core105_2nd_v106_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_std(revenue, 4), 4), 4))
def cg_f076_fundamental_volatility_core106_2nd_v107_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_std(ncfo, 4), 4), 4))
def cg_f076_fundamental_volatility_core107_2nd_v108_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_std(netinc, 4), 4), 4))
def cg_f076_fundamental_volatility_core108_2nd_v109_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core109_2nd_v110_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core110_2nd_v111_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(revenue, 8), 8))
def cg_f076_fundamental_volatility_core111_2nd_v112_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f076_fundamental_volatility_core112_2nd_v113_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(rnd, 8), 8))
def cg_f076_fundamental_volatility_core113_2nd_v114_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(netinc, 8), 8))
def cg_f076_fundamental_volatility_core114_2nd_v115_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(opinc, 8), 8))
def cg_f076_fundamental_volatility_core115_2nd_v116_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_std(revenue, 4), 8), 8))
def cg_f076_fundamental_volatility_core116_2nd_v117_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_std(ncfo, 4), 8), 8))
def cg_f076_fundamental_volatility_core117_2nd_v118_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_std(netinc, 4), 8), 8))
def cg_f076_fundamental_volatility_core118_2nd_v119_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 8), 8))
def cg_f076_fundamental_volatility_core119_2nd_v120_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_slope(_mean(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 8), 8))
def cg_f076_fundamental_volatility_core120_2nd_v121_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(revenue, 4), 4))
def cg_f076_fundamental_volatility_core121_2nd_v122_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f076_fundamental_volatility_core122_2nd_v123_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(rnd, 4), 4))
def cg_f076_fundamental_volatility_core123_2nd_v124_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(netinc, 4), 4))
def cg_f076_fundamental_volatility_core124_2nd_v125_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(opinc, 4), 4))
def cg_f076_fundamental_volatility_core125_2nd_v126_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(_std(revenue, 4), 4), 4))
def cg_f076_fundamental_volatility_core126_2nd_v127_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(_std(ncfo, 4), 4), 4))
def cg_f076_fundamental_volatility_core127_2nd_v128_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(_std(netinc, 4), 4), 4))
def cg_f076_fundamental_volatility_core128_2nd_v129_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core129_2nd_v130_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_diff(_mean(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 4))
def cg_f076_fundamental_volatility_core130_2nd_v131_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(revenue, 4), 4), 8))
def cg_f076_fundamental_volatility_core131_2nd_v132_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f076_fundamental_volatility_core132_2nd_v133_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(rnd, 4), 4), 8))
def cg_f076_fundamental_volatility_core133_2nd_v134_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(netinc, 4), 4), 8))
def cg_f076_fundamental_volatility_core134_2nd_v135_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(opinc, 4), 4), 8))
def cg_f076_fundamental_volatility_core135_2nd_v136_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(_std(revenue, 4), 4), 4), 8))
def cg_f076_fundamental_volatility_core136_2nd_v137_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(_std(ncfo, 4), 4), 4), 8))
def cg_f076_fundamental_volatility_core137_2nd_v138_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(_std(netinc, 4), 4), 4), 8))
def cg_f076_fundamental_volatility_core138_2nd_v139_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 4), 8))
def cg_f076_fundamental_volatility_core139_2nd_v140_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_z(_diff(_mean(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 4), 8))
def cg_f076_fundamental_volatility_core140_2nd_v141_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(revenue, 4), 4), 12))
def cg_f076_fundamental_volatility_core141_2nd_v142_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f076_fundamental_volatility_core142_2nd_v143_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(rnd, 4), 4), 12))
def cg_f076_fundamental_volatility_core143_2nd_v144_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(netinc, 4), 4), 12))
def cg_f076_fundamental_volatility_core144_2nd_v145_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(opinc, 4), 4), 12))
def cg_f076_fundamental_volatility_core145_2nd_v146_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(_std(revenue, 4), 4), 4), 12))
def cg_f076_fundamental_volatility_core146_2nd_v147_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(_std(ncfo, 4), 4), 4), 12))
def cg_f076_fundamental_volatility_core147_2nd_v148_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(_std(netinc, 4), 4), 4), 12))
def cg_f076_fundamental_volatility_core148_2nd_v149_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(_safe_div(_std(revenue, 4), _mean(revenue, 4).abs() + 1.0), 4), 4), 12))
def cg_f076_fundamental_volatility_core149_2nd_v150_signal(revenue, ncfo, rnd, netinc, opinc):
    return _clean(_rank(_slope(_mean(_safe_div(_std(ncfo, 4), _mean(ncfo, 4).abs() + 1.0), 4), 4), 12))