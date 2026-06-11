import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f031_shares_basic_core00_2nd_v001_signal(sharesbas, sharefactor):
    return _clean(_slope(sharesbas, 4))
def cg_f031_shares_basic_core01_2nd_v002_signal(sharesbas, sharefactor):
    return _clean(_slope(sharefactor, 4))
def cg_f031_shares_basic_core02_2nd_v003_signal(sharesbas, sharefactor):
    return _clean(_slope(sharesbas * sharefactor, 4))
def cg_f031_shares_basic_core03_2nd_v004_signal(sharesbas, sharefactor):
    return _clean(_slope(_diff(sharesbas, 4), 4))
def cg_f031_shares_basic_core04_2nd_v005_signal(sharesbas, sharefactor):
    return _clean(_slope(_pct_change(sharesbas, 4), 4))
def cg_f031_shares_basic_core05_2nd_v006_signal(sharesbas, sharefactor):
    return _clean(_slope(_slope(sharesbas, 8), 4))
def cg_f031_shares_basic_core06_2nd_v007_signal(sharesbas, sharefactor):
    return _clean(_slope(_z(sharesbas, 12), 4))
def cg_f031_shares_basic_core07_2nd_v008_signal(sharesbas, sharefactor):
    return _clean(_slope(_diff(sharefactor, 4), 4))
def cg_f031_shares_basic_core08_2nd_v009_signal(sharesbas, sharefactor):
    return _clean(_slope(sharesbas / (sharefactor + 1.0), 4))
def cg_f031_shares_basic_core09_2nd_v010_signal(sharesbas, sharefactor):
    return _clean(_slope(_log(sharesbas + 1.0), 4))
def cg_f031_shares_basic_core10_2nd_v011_signal(sharesbas, sharefactor):
    return _clean(_slope(sharesbas, 8))
def cg_f031_shares_basic_core11_2nd_v012_signal(sharesbas, sharefactor):
    return _clean(_slope(sharefactor, 8))
def cg_f031_shares_basic_core12_2nd_v013_signal(sharesbas, sharefactor):
    return _clean(_slope(sharesbas * sharefactor, 8))
def cg_f031_shares_basic_core13_2nd_v014_signal(sharesbas, sharefactor):
    return _clean(_slope(_diff(sharesbas, 4), 8))
def cg_f031_shares_basic_core14_2nd_v015_signal(sharesbas, sharefactor):
    return _clean(_slope(_pct_change(sharesbas, 4), 8))
def cg_f031_shares_basic_core15_2nd_v016_signal(sharesbas, sharefactor):
    return _clean(_slope(_slope(sharesbas, 8), 8))
def cg_f031_shares_basic_core16_2nd_v017_signal(sharesbas, sharefactor):
    return _clean(_slope(_z(sharesbas, 12), 8))
def cg_f031_shares_basic_core17_2nd_v018_signal(sharesbas, sharefactor):
    return _clean(_slope(_diff(sharefactor, 4), 8))
def cg_f031_shares_basic_core18_2nd_v019_signal(sharesbas, sharefactor):
    return _clean(_slope(sharesbas / (sharefactor + 1.0), 8))
def cg_f031_shares_basic_core19_2nd_v020_signal(sharesbas, sharefactor):
    return _clean(_slope(_log(sharesbas + 1.0), 8))
def cg_f031_shares_basic_core20_2nd_v021_signal(sharesbas, sharefactor):
    return _clean(_diff(sharesbas, 4))
def cg_f031_shares_basic_core21_2nd_v022_signal(sharesbas, sharefactor):
    return _clean(_diff(sharefactor, 4))
def cg_f031_shares_basic_core22_2nd_v023_signal(sharesbas, sharefactor):
    return _clean(_diff(sharesbas * sharefactor, 4))
def cg_f031_shares_basic_core23_2nd_v024_signal(sharesbas, sharefactor):
    return _clean(_diff(_diff(sharesbas, 4), 4))
def cg_f031_shares_basic_core24_2nd_v025_signal(sharesbas, sharefactor):
    return _clean(_diff(_pct_change(sharesbas, 4), 4))
def cg_f031_shares_basic_core25_2nd_v026_signal(sharesbas, sharefactor):
    return _clean(_diff(_slope(sharesbas, 8), 4))
def cg_f031_shares_basic_core26_2nd_v027_signal(sharesbas, sharefactor):
    return _clean(_diff(_z(sharesbas, 12), 4))
def cg_f031_shares_basic_core27_2nd_v028_signal(sharesbas, sharefactor):
    return _clean(_diff(_diff(sharefactor, 4), 4))
def cg_f031_shares_basic_core28_2nd_v029_signal(sharesbas, sharefactor):
    return _clean(_diff(sharesbas / (sharefactor + 1.0), 4))
def cg_f031_shares_basic_core29_2nd_v030_signal(sharesbas, sharefactor):
    return _clean(_diff(_log(sharesbas + 1.0), 4))
def cg_f031_shares_basic_core30_2nd_v031_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharesbas, 4), 8))
def cg_f031_shares_basic_core31_2nd_v032_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharefactor, 4), 8))
def cg_f031_shares_basic_core32_2nd_v033_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharesbas * sharefactor, 4), 8))
def cg_f031_shares_basic_core33_2nd_v034_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_diff(sharesbas, 4), 4), 8))
def cg_f031_shares_basic_core34_2nd_v035_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_pct_change(sharesbas, 4), 4), 8))
def cg_f031_shares_basic_core35_2nd_v036_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_slope(sharesbas, 8), 4), 8))
def cg_f031_shares_basic_core36_2nd_v037_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_z(sharesbas, 12), 4), 8))
def cg_f031_shares_basic_core37_2nd_v038_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_diff(sharefactor, 4), 4), 8))
def cg_f031_shares_basic_core38_2nd_v039_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharesbas / (sharefactor + 1.0), 4), 8))
def cg_f031_shares_basic_core39_2nd_v040_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_log(sharesbas + 1.0), 4), 8))
def cg_f031_shares_basic_core40_2nd_v041_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharesbas, 8), 12))
def cg_f031_shares_basic_core41_2nd_v042_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharefactor, 8), 12))
def cg_f031_shares_basic_core42_2nd_v043_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharesbas * sharefactor, 8), 12))
def cg_f031_shares_basic_core43_2nd_v044_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_diff(sharesbas, 4), 8), 12))
def cg_f031_shares_basic_core44_2nd_v045_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_pct_change(sharesbas, 4), 8), 12))
def cg_f031_shares_basic_core45_2nd_v046_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_slope(sharesbas, 8), 8), 12))
def cg_f031_shares_basic_core46_2nd_v047_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_z(sharesbas, 12), 8), 12))
def cg_f031_shares_basic_core47_2nd_v048_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_diff(sharefactor, 4), 8), 12))
def cg_f031_shares_basic_core48_2nd_v049_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(sharesbas / (sharefactor + 1.0), 8), 12))
def cg_f031_shares_basic_core49_2nd_v050_signal(sharesbas, sharefactor):
    return _clean(_z(_slope(_log(sharesbas + 1.0), 8), 12))
def cg_f031_shares_basic_core50_2nd_v051_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(sharesbas, 4), 8))
def cg_f031_shares_basic_core51_2nd_v052_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(sharefactor, 4), 8))
def cg_f031_shares_basic_core52_2nd_v053_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(sharesbas * sharefactor, 4), 8))
def cg_f031_shares_basic_core53_2nd_v054_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_diff(sharesbas, 4), 4), 8))
def cg_f031_shares_basic_core54_2nd_v055_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_pct_change(sharesbas, 4), 4), 8))
def cg_f031_shares_basic_core55_2nd_v056_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_slope(sharesbas, 8), 4), 8))
def cg_f031_shares_basic_core56_2nd_v057_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_z(sharesbas, 12), 4), 8))
def cg_f031_shares_basic_core57_2nd_v058_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_diff(sharefactor, 4), 4), 8))
def cg_f031_shares_basic_core58_2nd_v059_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(sharesbas / (sharefactor + 1.0), 4), 8))
def cg_f031_shares_basic_core59_2nd_v060_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_log(sharesbas + 1.0), 4), 8))
def cg_f031_shares_basic_core60_2nd_v061_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(sharesbas, 4), 12))
def cg_f031_shares_basic_core61_2nd_v062_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(sharefactor, 4), 12))
def cg_f031_shares_basic_core62_2nd_v063_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(sharesbas * sharefactor, 4), 12))
def cg_f031_shares_basic_core63_2nd_v064_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_diff(sharesbas, 4), 4), 12))
def cg_f031_shares_basic_core64_2nd_v065_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_pct_change(sharesbas, 4), 4), 12))
def cg_f031_shares_basic_core65_2nd_v066_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_slope(sharesbas, 8), 4), 12))
def cg_f031_shares_basic_core66_2nd_v067_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_z(sharesbas, 12), 4), 12))
def cg_f031_shares_basic_core67_2nd_v068_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_diff(sharefactor, 4), 4), 12))
def cg_f031_shares_basic_core68_2nd_v069_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(sharesbas / (sharefactor + 1.0), 4), 12))
def cg_f031_shares_basic_core69_2nd_v070_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_log(sharesbas + 1.0), 4), 12))
def cg_f031_shares_basic_core70_2nd_v071_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(sharesbas, 4), 12))
def cg_f031_shares_basic_core71_2nd_v072_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(sharefactor, 4), 12))
def cg_f031_shares_basic_core72_2nd_v073_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(sharesbas * sharefactor, 4), 12))
def cg_f031_shares_basic_core73_2nd_v074_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(_diff(sharesbas, 4), 4), 12))
def cg_f031_shares_basic_core74_2nd_v075_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(_pct_change(sharesbas, 4), 4), 12))
def cg_f031_shares_basic_core75_2nd_v076_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(_slope(sharesbas, 8), 4), 12))
def cg_f031_shares_basic_core76_2nd_v077_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(_z(sharesbas, 12), 4), 12))
def cg_f031_shares_basic_core77_2nd_v078_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(_diff(sharefactor, 4), 4), 12))
def cg_f031_shares_basic_core78_2nd_v079_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(sharesbas / (sharefactor + 1.0), 4), 12))
def cg_f031_shares_basic_core79_2nd_v080_signal(sharesbas, sharefactor):
    return _clean(_rank(_diff(_log(sharesbas + 1.0), 4), 12))
def cg_f031_shares_basic_core80_2nd_v081_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(sharesbas, 4), 4))
def cg_f031_shares_basic_core81_2nd_v082_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(sharefactor, 4), 4))
def cg_f031_shares_basic_core82_2nd_v083_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(sharesbas * sharefactor, 4), 4))
def cg_f031_shares_basic_core83_2nd_v084_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(_diff(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core84_2nd_v085_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(_pct_change(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core85_2nd_v086_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(_slope(sharesbas, 8), 4), 4))
def cg_f031_shares_basic_core86_2nd_v087_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(_z(sharesbas, 12), 4), 4))
def cg_f031_shares_basic_core87_2nd_v088_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(_diff(sharefactor, 4), 4), 4))
def cg_f031_shares_basic_core88_2nd_v089_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(sharesbas / (sharefactor + 1.0), 4), 4))
def cg_f031_shares_basic_core89_2nd_v090_signal(sharesbas, sharefactor):
    return _clean(_mean(_slope(_log(sharesbas + 1.0), 4), 4))
def cg_f031_shares_basic_core90_2nd_v091_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(sharesbas, 4), 4))
def cg_f031_shares_basic_core91_2nd_v092_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(sharefactor, 4), 4))
def cg_f031_shares_basic_core92_2nd_v093_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(sharesbas * sharefactor, 4), 4))
def cg_f031_shares_basic_core93_2nd_v094_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(_diff(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core94_2nd_v095_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(_pct_change(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core95_2nd_v096_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(_slope(sharesbas, 8), 4), 4))
def cg_f031_shares_basic_core96_2nd_v097_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(_z(sharesbas, 12), 4), 4))
def cg_f031_shares_basic_core97_2nd_v098_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(_diff(sharefactor, 4), 4), 4))
def cg_f031_shares_basic_core98_2nd_v099_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(sharesbas / (sharefactor + 1.0), 4), 4))
def cg_f031_shares_basic_core99_2nd_v100_signal(sharesbas, sharefactor):
    return _clean(_mean(_diff(_log(sharesbas + 1.0), 4), 4))
def cg_f031_shares_basic_core100_2nd_v101_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharesbas, 4), 4))
def cg_f031_shares_basic_core101_2nd_v102_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharefactor, 4), 4))
def cg_f031_shares_basic_core102_2nd_v103_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharesbas * sharefactor, 4), 4))
def cg_f031_shares_basic_core103_2nd_v104_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_diff(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core104_2nd_v105_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_pct_change(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core105_2nd_v106_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_slope(sharesbas, 8), 4), 4))
def cg_f031_shares_basic_core106_2nd_v107_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_z(sharesbas, 12), 4), 4))
def cg_f031_shares_basic_core107_2nd_v108_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_diff(sharefactor, 4), 4), 4))
def cg_f031_shares_basic_core108_2nd_v109_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharesbas / (sharefactor + 1.0), 4), 4))
def cg_f031_shares_basic_core109_2nd_v110_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_log(sharesbas + 1.0), 4), 4))
def cg_f031_shares_basic_core110_2nd_v111_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharesbas, 8), 8))
def cg_f031_shares_basic_core111_2nd_v112_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharefactor, 8), 8))
def cg_f031_shares_basic_core112_2nd_v113_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharesbas * sharefactor, 8), 8))
def cg_f031_shares_basic_core113_2nd_v114_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_diff(sharesbas, 4), 8), 8))
def cg_f031_shares_basic_core114_2nd_v115_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_pct_change(sharesbas, 4), 8), 8))
def cg_f031_shares_basic_core115_2nd_v116_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_slope(sharesbas, 8), 8), 8))
def cg_f031_shares_basic_core116_2nd_v117_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_z(sharesbas, 12), 8), 8))
def cg_f031_shares_basic_core117_2nd_v118_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_diff(sharefactor, 4), 8), 8))
def cg_f031_shares_basic_core118_2nd_v119_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(sharesbas / (sharefactor + 1.0), 8), 8))
def cg_f031_shares_basic_core119_2nd_v120_signal(sharesbas, sharefactor):
    return _clean(_slope(_mean(_log(sharesbas + 1.0), 8), 8))
def cg_f031_shares_basic_core120_2nd_v121_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(sharesbas, 4), 4))
def cg_f031_shares_basic_core121_2nd_v122_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(sharefactor, 4), 4))
def cg_f031_shares_basic_core122_2nd_v123_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(sharesbas * sharefactor, 4), 4))
def cg_f031_shares_basic_core123_2nd_v124_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(_diff(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core124_2nd_v125_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(_pct_change(sharesbas, 4), 4), 4))
def cg_f031_shares_basic_core125_2nd_v126_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(_slope(sharesbas, 8), 4), 4))
def cg_f031_shares_basic_core126_2nd_v127_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(_z(sharesbas, 12), 4), 4))
def cg_f031_shares_basic_core127_2nd_v128_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(_diff(sharefactor, 4), 4), 4))
def cg_f031_shares_basic_core128_2nd_v129_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(sharesbas / (sharefactor + 1.0), 4), 4))
def cg_f031_shares_basic_core129_2nd_v130_signal(sharesbas, sharefactor):
    return _clean(_diff(_mean(_log(sharesbas + 1.0), 4), 4))
def cg_f031_shares_basic_core130_2nd_v131_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(sharesbas, 4), 4), 8))
def cg_f031_shares_basic_core131_2nd_v132_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(sharefactor, 4), 4), 8))
def cg_f031_shares_basic_core132_2nd_v133_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(sharesbas * sharefactor, 4), 4), 8))
def cg_f031_shares_basic_core133_2nd_v134_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(_diff(sharesbas, 4), 4), 4), 8))
def cg_f031_shares_basic_core134_2nd_v135_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(_pct_change(sharesbas, 4), 4), 4), 8))
def cg_f031_shares_basic_core135_2nd_v136_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(_slope(sharesbas, 8), 4), 4), 8))
def cg_f031_shares_basic_core136_2nd_v137_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(_z(sharesbas, 12), 4), 4), 8))
def cg_f031_shares_basic_core137_2nd_v138_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(_diff(sharefactor, 4), 4), 4), 8))
def cg_f031_shares_basic_core138_2nd_v139_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(sharesbas / (sharefactor + 1.0), 4), 4), 8))
def cg_f031_shares_basic_core139_2nd_v140_signal(sharesbas, sharefactor):
    return _clean(_z(_diff(_mean(_log(sharesbas + 1.0), 4), 4), 8))
def cg_f031_shares_basic_core140_2nd_v141_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(sharesbas, 4), 4), 12))
def cg_f031_shares_basic_core141_2nd_v142_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(sharefactor, 4), 4), 12))
def cg_f031_shares_basic_core142_2nd_v143_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(sharesbas * sharefactor, 4), 4), 12))
def cg_f031_shares_basic_core143_2nd_v144_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(_diff(sharesbas, 4), 4), 4), 12))
def cg_f031_shares_basic_core144_2nd_v145_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(_pct_change(sharesbas, 4), 4), 4), 12))
def cg_f031_shares_basic_core145_2nd_v146_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(_slope(sharesbas, 8), 4), 4), 12))
def cg_f031_shares_basic_core146_2nd_v147_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(_z(sharesbas, 12), 4), 4), 12))
def cg_f031_shares_basic_core147_2nd_v148_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(_diff(sharefactor, 4), 4), 4), 12))
def cg_f031_shares_basic_core148_2nd_v149_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(sharesbas / (sharefactor + 1.0), 4), 4), 12))
def cg_f031_shares_basic_core149_2nd_v150_signal(sharesbas, sharefactor):
    return _clean(_rank(_slope(_mean(_log(sharesbas + 1.0), 4), 4), 12))