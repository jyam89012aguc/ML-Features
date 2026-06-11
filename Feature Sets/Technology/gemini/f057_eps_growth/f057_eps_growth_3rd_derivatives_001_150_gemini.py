import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f057_eps_growth_core00_3rd_v001_signal(eps, epsdil):
    return _clean(_diff(_diff(eps, 4), 4))
def cg_f057_eps_growth_core01_3rd_v002_signal(eps, epsdil):
    return _clean(_diff(_diff(epsdil, 4), 4))
def cg_f057_eps_growth_core02_3rd_v003_signal(eps, epsdil):
    return _clean(_diff(_diff(_pct_change(eps, 4), 4), 4))
def cg_f057_eps_growth_core03_3rd_v004_signal(eps, epsdil):
    return _clean(_diff(_diff(_pct_change(epsdil, 4), 4), 4))
def cg_f057_eps_growth_core04_3rd_v005_signal(eps, epsdil):
    return _clean(_diff(_diff(_pct_change(eps, 8), 4), 4))
def cg_f057_eps_growth_core05_3rd_v006_signal(eps, epsdil):
    return _clean(_diff(_diff(_pct_change(epsdil, 8), 4), 4))
def cg_f057_eps_growth_core06_3rd_v007_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4))
def cg_f057_eps_growth_core07_3rd_v008_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4))
def cg_f057_eps_growth_core08_3rd_v009_signal(eps, epsdil):
    return _clean(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4))
def cg_f057_eps_growth_core09_3rd_v010_signal(eps, epsdil):
    return _clean(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4))
def cg_f057_eps_growth_core10_3rd_v011_signal(eps, epsdil):
    return _clean(_slope(_diff(eps, 4), 8))
def cg_f057_eps_growth_core11_3rd_v012_signal(eps, epsdil):
    return _clean(_slope(_diff(epsdil, 4), 8))
def cg_f057_eps_growth_core12_3rd_v013_signal(eps, epsdil):
    return _clean(_slope(_diff(_pct_change(eps, 4), 4), 8))
def cg_f057_eps_growth_core13_3rd_v014_signal(eps, epsdil):
    return _clean(_slope(_diff(_pct_change(epsdil, 4), 4), 8))
def cg_f057_eps_growth_core14_3rd_v015_signal(eps, epsdil):
    return _clean(_slope(_diff(_pct_change(eps, 8), 4), 8))
def cg_f057_eps_growth_core15_3rd_v016_signal(eps, epsdil):
    return _clean(_slope(_diff(_pct_change(epsdil, 8), 4), 8))
def cg_f057_eps_growth_core16_3rd_v017_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_pct_change(eps, 4), 4), 4), 8))
def cg_f057_eps_growth_core17_3rd_v018_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 8))
def cg_f057_eps_growth_core18_3rd_v019_signal(eps, epsdil):
    return _clean(_slope(_diff(_z(_pct_change(eps, 4), 8), 4), 8))
def cg_f057_eps_growth_core19_3rd_v020_signal(eps, epsdil):
    return _clean(_slope(_diff(_z(_pct_change(epsdil, 4), 8), 4), 8))
def cg_f057_eps_growth_core20_3rd_v021_signal(eps, epsdil):
    return _clean(_diff(_slope(eps, 4), 4))
def cg_f057_eps_growth_core21_3rd_v022_signal(eps, epsdil):
    return _clean(_diff(_slope(epsdil, 4), 4))
def cg_f057_eps_growth_core22_3rd_v023_signal(eps, epsdil):
    return _clean(_diff(_slope(_pct_change(eps, 4), 4), 4))
def cg_f057_eps_growth_core23_3rd_v024_signal(eps, epsdil):
    return _clean(_diff(_slope(_pct_change(epsdil, 4), 4), 4))
def cg_f057_eps_growth_core24_3rd_v025_signal(eps, epsdil):
    return _clean(_diff(_slope(_pct_change(eps, 8), 4), 4))
def cg_f057_eps_growth_core25_3rd_v026_signal(eps, epsdil):
    return _clean(_diff(_slope(_pct_change(epsdil, 8), 4), 4))
def cg_f057_eps_growth_core26_3rd_v027_signal(eps, epsdil):
    return _clean(_diff(_slope(_diff(_pct_change(eps, 4), 4), 4), 4))
def cg_f057_eps_growth_core27_3rd_v028_signal(eps, epsdil):
    return _clean(_diff(_slope(_diff(_pct_change(epsdil, 4), 4), 4), 4))
def cg_f057_eps_growth_core28_3rd_v029_signal(eps, epsdil):
    return _clean(_diff(_slope(_z(_pct_change(eps, 4), 8), 4), 4))
def cg_f057_eps_growth_core29_3rd_v030_signal(eps, epsdil):
    return _clean(_diff(_slope(_z(_pct_change(epsdil, 4), 8), 4), 4))
def cg_f057_eps_growth_core30_3rd_v031_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(eps, 4), 4), 8))
def cg_f057_eps_growth_core31_3rd_v032_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(epsdil, 4), 4), 8))
def cg_f057_eps_growth_core32_3rd_v033_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_pct_change(eps, 4), 4), 4), 8))
def cg_f057_eps_growth_core33_3rd_v034_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 8))
def cg_f057_eps_growth_core34_3rd_v035_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_pct_change(eps, 8), 4), 4), 8))
def cg_f057_eps_growth_core35_3rd_v036_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_pct_change(epsdil, 8), 4), 4), 8))
def cg_f057_eps_growth_core36_3rd_v037_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core37_3rd_v038_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core38_3rd_v039_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4), 8))
def cg_f057_eps_growth_core39_3rd_v040_signal(eps, epsdil):
    return _clean(_z(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4), 8))
def cg_f057_eps_growth_core40_3rd_v041_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(eps, 4), 8), 12))
def cg_f057_eps_growth_core41_3rd_v042_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(epsdil, 4), 8), 12))
def cg_f057_eps_growth_core42_3rd_v043_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_pct_change(eps, 4), 4), 8), 12))
def cg_f057_eps_growth_core43_3rd_v044_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_pct_change(epsdil, 4), 4), 8), 12))
def cg_f057_eps_growth_core44_3rd_v045_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_pct_change(eps, 8), 4), 8), 12))
def cg_f057_eps_growth_core45_3rd_v046_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_pct_change(epsdil, 8), 4), 8), 12))
def cg_f057_eps_growth_core46_3rd_v047_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_pct_change(eps, 4), 4), 4), 8), 12))
def cg_f057_eps_growth_core47_3rd_v048_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 8), 12))
def cg_f057_eps_growth_core48_3rd_v049_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_z(_pct_change(eps, 4), 8), 4), 8), 12))
def cg_f057_eps_growth_core49_3rd_v050_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_z(_pct_change(epsdil, 4), 8), 4), 8), 12))
def cg_f057_eps_growth_core50_3rd_v051_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(eps, 4), 4), 8))
def cg_f057_eps_growth_core51_3rd_v052_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(epsdil, 4), 4), 8))
def cg_f057_eps_growth_core52_3rd_v053_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_pct_change(eps, 4), 4), 4), 8))
def cg_f057_eps_growth_core53_3rd_v054_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_pct_change(epsdil, 4), 4), 4), 8))
def cg_f057_eps_growth_core54_3rd_v055_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_pct_change(eps, 8), 4), 4), 8))
def cg_f057_eps_growth_core55_3rd_v056_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_pct_change(epsdil, 8), 4), 4), 8))
def cg_f057_eps_growth_core56_3rd_v057_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_diff(_pct_change(eps, 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core57_3rd_v058_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_diff(_pct_change(epsdil, 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core58_3rd_v059_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_z(_pct_change(eps, 4), 8), 4), 4), 8))
def cg_f057_eps_growth_core59_3rd_v060_signal(eps, epsdil):
    return _clean(_z(_diff(_slope(_z(_pct_change(epsdil, 4), 8), 4), 4), 8))
def cg_f057_eps_growth_core60_3rd_v061_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(eps, 4), 4), 12))
def cg_f057_eps_growth_core61_3rd_v062_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(epsdil, 4), 4), 12))
def cg_f057_eps_growth_core62_3rd_v063_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_pct_change(eps, 4), 4), 4), 12))
def cg_f057_eps_growth_core63_3rd_v064_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 12))
def cg_f057_eps_growth_core64_3rd_v065_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_pct_change(eps, 8), 4), 4), 12))
def cg_f057_eps_growth_core65_3rd_v066_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_pct_change(epsdil, 8), 4), 4), 12))
def cg_f057_eps_growth_core66_3rd_v067_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 12))
def cg_f057_eps_growth_core67_3rd_v068_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 12))
def cg_f057_eps_growth_core68_3rd_v069_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4), 12))
def cg_f057_eps_growth_core69_3rd_v070_signal(eps, epsdil):
    return _clean(_rank(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4), 12))
def cg_f057_eps_growth_core70_3rd_v071_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(eps, 4), 8), 12))
def cg_f057_eps_growth_core71_3rd_v072_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(epsdil, 4), 8), 12))
def cg_f057_eps_growth_core72_3rd_v073_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_pct_change(eps, 4), 4), 8), 12))
def cg_f057_eps_growth_core73_3rd_v074_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_pct_change(epsdil, 4), 4), 8), 12))
def cg_f057_eps_growth_core74_3rd_v075_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_pct_change(eps, 8), 4), 8), 12))
def cg_f057_eps_growth_core75_3rd_v076_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_pct_change(epsdil, 8), 4), 8), 12))
def cg_f057_eps_growth_core76_3rd_v077_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_diff(_pct_change(eps, 4), 4), 4), 8), 12))
def cg_f057_eps_growth_core77_3rd_v078_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 8), 12))
def cg_f057_eps_growth_core78_3rd_v079_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_z(_pct_change(eps, 4), 8), 4), 8), 12))
def cg_f057_eps_growth_core79_3rd_v080_signal(eps, epsdil):
    return _clean(_rank(_slope(_diff(_z(_pct_change(epsdil, 4), 8), 4), 8), 12))
def cg_f057_eps_growth_core80_3rd_v081_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(eps, 4), 4), 12))
def cg_f057_eps_growth_core81_3rd_v082_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(epsdil, 4), 4), 12))
def cg_f057_eps_growth_core82_3rd_v083_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_pct_change(eps, 4), 4), 4), 12))
def cg_f057_eps_growth_core83_3rd_v084_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_pct_change(epsdil, 4), 4), 4), 12))
def cg_f057_eps_growth_core84_3rd_v085_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_pct_change(eps, 8), 4), 4), 12))
def cg_f057_eps_growth_core85_3rd_v086_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_pct_change(epsdil, 8), 4), 4), 12))
def cg_f057_eps_growth_core86_3rd_v087_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_diff(_pct_change(eps, 4), 4), 4), 4), 12))
def cg_f057_eps_growth_core87_3rd_v088_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_diff(_pct_change(epsdil, 4), 4), 4), 4), 12))
def cg_f057_eps_growth_core88_3rd_v089_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_z(_pct_change(eps, 4), 8), 4), 4), 12))
def cg_f057_eps_growth_core89_3rd_v090_signal(eps, epsdil):
    return _clean(_rank(_diff(_slope(_z(_pct_change(epsdil, 4), 8), 4), 4), 12))
def cg_f057_eps_growth_core90_3rd_v091_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(eps, 4), 4), 4))
def cg_f057_eps_growth_core91_3rd_v092_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(epsdil, 4), 4), 4))
def cg_f057_eps_growth_core92_3rd_v093_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_pct_change(eps, 4), 4), 4), 4))
def cg_f057_eps_growth_core93_3rd_v094_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4))
def cg_f057_eps_growth_core94_3rd_v095_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_pct_change(eps, 8), 4), 4), 4))
def cg_f057_eps_growth_core95_3rd_v096_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_pct_change(epsdil, 8), 4), 4), 4))
def cg_f057_eps_growth_core96_3rd_v097_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core97_3rd_v098_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core98_3rd_v099_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core99_3rd_v100_signal(eps, epsdil):
    return _clean(_mean(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core100_3rd_v101_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(eps, 4), 8), 4))
def cg_f057_eps_growth_core101_3rd_v102_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(epsdil, 4), 8), 4))
def cg_f057_eps_growth_core102_3rd_v103_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_pct_change(eps, 4), 4), 8), 4))
def cg_f057_eps_growth_core103_3rd_v104_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_pct_change(epsdil, 4), 4), 8), 4))
def cg_f057_eps_growth_core104_3rd_v105_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_pct_change(eps, 8), 4), 8), 4))
def cg_f057_eps_growth_core105_3rd_v106_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_pct_change(epsdil, 8), 4), 8), 4))
def cg_f057_eps_growth_core106_3rd_v107_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_diff(_pct_change(eps, 4), 4), 4), 8), 4))
def cg_f057_eps_growth_core107_3rd_v108_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 8), 4))
def cg_f057_eps_growth_core108_3rd_v109_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_z(_pct_change(eps, 4), 8), 4), 8), 4))
def cg_f057_eps_growth_core109_3rd_v110_signal(eps, epsdil):
    return _clean(_mean(_slope(_diff(_z(_pct_change(epsdil, 4), 8), 4), 8), 4))
def cg_f057_eps_growth_core110_3rd_v111_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(eps, 4), 4), 4))
def cg_f057_eps_growth_core111_3rd_v112_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(epsdil, 4), 4), 4))
def cg_f057_eps_growth_core112_3rd_v113_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_pct_change(eps, 4), 4), 4), 4))
def cg_f057_eps_growth_core113_3rd_v114_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_pct_change(epsdil, 4), 4), 4), 4))
def cg_f057_eps_growth_core114_3rd_v115_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_pct_change(eps, 8), 4), 4), 4))
def cg_f057_eps_growth_core115_3rd_v116_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_pct_change(epsdil, 8), 4), 4), 4))
def cg_f057_eps_growth_core116_3rd_v117_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_diff(_pct_change(eps, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core117_3rd_v118_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_diff(_pct_change(epsdil, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core118_3rd_v119_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_z(_pct_change(eps, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core119_3rd_v120_signal(eps, epsdil):
    return _clean(_mean(_diff(_slope(_z(_pct_change(epsdil, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core120_3rd_v121_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(eps, 4), 4), 4))
def cg_f057_eps_growth_core121_3rd_v122_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(epsdil, 4), 4), 4))
def cg_f057_eps_growth_core122_3rd_v123_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_pct_change(eps, 4), 4), 4), 4))
def cg_f057_eps_growth_core123_3rd_v124_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4))
def cg_f057_eps_growth_core124_3rd_v125_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_pct_change(eps, 8), 4), 4), 4))
def cg_f057_eps_growth_core125_3rd_v126_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_pct_change(epsdil, 8), 4), 4), 4))
def cg_f057_eps_growth_core126_3rd_v127_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core127_3rd_v128_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core128_3rd_v129_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core129_3rd_v130_signal(eps, epsdil):
    return _clean(_slope(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core130_3rd_v131_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(eps, 4), 4), 4))
def cg_f057_eps_growth_core131_3rd_v132_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(epsdil, 4), 4), 4))
def cg_f057_eps_growth_core132_3rd_v133_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4))
def cg_f057_eps_growth_core133_3rd_v134_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4))
def cg_f057_eps_growth_core134_3rd_v135_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_pct_change(eps, 8), 4), 4), 4))
def cg_f057_eps_growth_core135_3rd_v136_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_pct_change(epsdil, 8), 4), 4), 4))
def cg_f057_eps_growth_core136_3rd_v137_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core137_3rd_v138_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 4))
def cg_f057_eps_growth_core138_3rd_v139_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core139_3rd_v140_signal(eps, epsdil):
    return _clean(_diff(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4), 4))
def cg_f057_eps_growth_core140_3rd_v141_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(eps, 4), 4), 4), 8))
def cg_f057_eps_growth_core141_3rd_v142_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(epsdil, 4), 4), 4), 8))
def cg_f057_eps_growth_core142_3rd_v143_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core143_3rd_v144_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core144_3rd_v145_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_pct_change(eps, 8), 4), 4), 4), 8))
def cg_f057_eps_growth_core145_3rd_v146_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_pct_change(epsdil, 8), 4), 4), 4), 8))
def cg_f057_eps_growth_core146_3rd_v147_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_diff(_pct_change(eps, 4), 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core147_3rd_v148_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_diff(_pct_change(epsdil, 4), 4), 4), 4), 4), 8))
def cg_f057_eps_growth_core148_3rd_v149_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_z(_pct_change(eps, 4), 8), 4), 4), 4), 8))
def cg_f057_eps_growth_core149_3rd_v150_signal(eps, epsdil):
    return _clean(_z(_slope(_diff(_diff(_z(_pct_change(epsdil, 4), 8), 4), 4), 4), 8))