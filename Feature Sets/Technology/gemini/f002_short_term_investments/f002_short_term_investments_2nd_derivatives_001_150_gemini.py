import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f002_short_term_investments_core00_2nd_v001_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(investmentsc, 4))
def cg_f002_short_term_investments_core01_2nd_v002_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(investments, 4))
def cg_f002_short_term_investments_core02_2nd_v003_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(cashneq, 4))
def cg_f002_short_term_investments_core03_2nd_v004_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(assets, 4))
def cg_f002_short_term_investments_core04_2nd_v005_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investmentsc, assets), 4))
def cg_f002_short_term_investments_core05_2nd_v006_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investments, assets), 4))
def cg_f002_short_term_investments_core06_2nd_v007_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(cashneq, assets), 4))
def cg_f002_short_term_investments_core07_2nd_v008_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investmentsc, investments + 1.0), 4))
def cg_f002_short_term_investments_core08_2nd_v009_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investmentsc, cashneq + 1.0), 4))
def cg_f002_short_term_investments_core09_2nd_v010_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investments, cashneq + 1.0), 4))

def cg_f002_short_term_investments_core10_2nd_v011_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(investmentsc, 8))
def cg_f002_short_term_investments_core11_2nd_v012_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(investments, 8))
def cg_f002_short_term_investments_core12_2nd_v013_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(cashneq, 8))
def cg_f002_short_term_investments_core13_2nd_v014_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(assets, 8))
def cg_f002_short_term_investments_core14_2nd_v015_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investmentsc, assets), 8))
def cg_f002_short_term_investments_core15_2nd_v016_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investments, assets), 8))
def cg_f002_short_term_investments_core16_2nd_v017_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(cashneq, assets), 8))
def cg_f002_short_term_investments_core17_2nd_v018_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investmentsc, investments + 1.0), 8))
def cg_f002_short_term_investments_core18_2nd_v019_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investmentsc, cashneq + 1.0), 8))
def cg_f002_short_term_investments_core19_2nd_v020_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_safe_div(investments, cashneq + 1.0), 8))

def cg_f002_short_term_investments_core20_2nd_v021_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(investmentsc, 4))
def cg_f002_short_term_investments_core21_2nd_v022_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(investments, 4))
def cg_f002_short_term_investments_core22_2nd_v023_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(cashneq, 4))
def cg_f002_short_term_investments_core23_2nd_v024_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(assets, 4))
def cg_f002_short_term_investments_core24_2nd_v025_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_safe_div(investmentsc, assets), 4))
def cg_f002_short_term_investments_core25_2nd_v026_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_safe_div(investments, assets), 4))
def cg_f002_short_term_investments_core26_2nd_v027_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_safe_div(cashneq, assets), 4))
def cg_f002_short_term_investments_core27_2nd_v028_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_safe_div(investmentsc, investments + 1.0), 4))
def cg_f002_short_term_investments_core28_2nd_v029_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_safe_div(investmentsc, cashneq + 1.0), 4))
def cg_f002_short_term_investments_core29_2nd_v030_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_safe_div(investments, cashneq + 1.0), 4))

def cg_f002_short_term_investments_core30_2nd_v031_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(investmentsc, 4), 8))
def cg_f002_short_term_investments_core31_2nd_v032_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(investments, 4), 8))
def cg_f002_short_term_investments_core32_2nd_v033_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f002_short_term_investments_core33_2nd_v034_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(assets, 4), 8))
def cg_f002_short_term_investments_core34_2nd_v035_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investmentsc, assets), 4), 8))
def cg_f002_short_term_investments_core35_2nd_v036_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investments, assets), 4), 8))
def cg_f002_short_term_investments_core36_2nd_v037_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(cashneq, assets), 4), 8))
def cg_f002_short_term_investments_core37_2nd_v038_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investmentsc, investments + 1.0), 4), 8))
def cg_f002_short_term_investments_core38_2nd_v039_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investmentsc, cashneq + 1.0), 4), 8))
def cg_f002_short_term_investments_core39_2nd_v040_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investments, cashneq + 1.0), 4), 8))

def cg_f002_short_term_investments_core40_2nd_v041_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(investmentsc, 8), 12))
def cg_f002_short_term_investments_core41_2nd_v042_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(investments, 8), 12))
def cg_f002_short_term_investments_core42_2nd_v043_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f002_short_term_investments_core43_2nd_v044_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(assets, 8), 12))
def cg_f002_short_term_investments_core44_2nd_v045_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investmentsc, assets), 8), 12))
def cg_f002_short_term_investments_core45_2nd_v046_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investments, assets), 8), 12))
def cg_f002_short_term_investments_core46_2nd_v047_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(cashneq, assets), 8), 12))
def cg_f002_short_term_investments_core47_2nd_v048_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investmentsc, investments + 1.0), 8), 12))
def cg_f002_short_term_investments_core48_2nd_v049_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investmentsc, cashneq + 1.0), 8), 12))
def cg_f002_short_term_investments_core49_2nd_v050_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_slope(_safe_div(investments, cashneq + 1.0), 8), 12))

def cg_f002_short_term_investments_core50_2nd_v051_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(investmentsc, 4), 8))
def cg_f002_short_term_investments_core51_2nd_v052_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(investments, 4), 8))
def cg_f002_short_term_investments_core52_2nd_v053_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f002_short_term_investments_core53_2nd_v054_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(assets, 4), 8))
def cg_f002_short_term_investments_core54_2nd_v055_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_safe_div(investmentsc, assets), 4), 8))
def cg_f002_short_term_investments_core55_2nd_v056_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_safe_div(investments, assets), 4), 8))
def cg_f002_short_term_investments_core56_2nd_v057_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_safe_div(cashneq, assets), 4), 8))
def cg_f002_short_term_investments_core57_2nd_v058_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_safe_div(investmentsc, investments + 1.0), 4), 8))
def cg_f002_short_term_investments_core58_2nd_v059_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_safe_div(investmentsc, cashneq + 1.0), 4), 8))
def cg_f002_short_term_investments_core59_2nd_v060_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_safe_div(investments, cashneq + 1.0), 4), 8))

def cg_f002_short_term_investments_core60_2nd_v061_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(investmentsc, 4), 12))
def cg_f002_short_term_investments_core61_2nd_v062_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(investments, 4), 12))
def cg_f002_short_term_investments_core62_2nd_v063_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f002_short_term_investments_core63_2nd_v064_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(assets, 4), 12))
def cg_f002_short_term_investments_core64_2nd_v065_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(investmentsc, assets), 4), 12))
def cg_f002_short_term_investments_core65_2nd_v066_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(investments, assets), 4), 12))
def cg_f002_short_term_investments_core66_2nd_v067_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(cashneq, assets), 4), 12))
def cg_f002_short_term_investments_core67_2nd_v068_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(investmentsc, investments + 1.0), 4), 12))
def cg_f002_short_term_investments_core68_2nd_v069_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(investmentsc, cashneq + 1.0), 4), 12))
def cg_f002_short_term_investments_core69_2nd_v070_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(investments, cashneq + 1.0), 4), 12))

def cg_f002_short_term_investments_core70_2nd_v071_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(investmentsc, 4), 12))
def cg_f002_short_term_investments_core71_2nd_v072_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(investments, 4), 12))
def cg_f002_short_term_investments_core72_2nd_v073_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f002_short_term_investments_core73_2nd_v074_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(assets, 4), 12))
def cg_f002_short_term_investments_core74_2nd_v075_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(investmentsc, assets), 4), 12))
def cg_f002_short_term_investments_core75_2nd_v076_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(investments, assets), 4), 12))
def cg_f002_short_term_investments_core76_2nd_v077_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(cashneq, assets), 4), 12))
def cg_f002_short_term_investments_core77_2nd_v078_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(investmentsc, investments + 1.0), 4), 12))
def cg_f002_short_term_investments_core78_2nd_v079_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(investmentsc, cashneq + 1.0), 4), 12))
def cg_f002_short_term_investments_core79_2nd_v080_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(investments, cashneq + 1.0), 4), 12))

def cg_f002_short_term_investments_core80_2nd_v081_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(investmentsc, 4), 4))
def cg_f002_short_term_investments_core81_2nd_v082_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(investments, 4), 4))
def cg_f002_short_term_investments_core82_2nd_v083_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f002_short_term_investments_core83_2nd_v084_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(assets, 4), 4))
def cg_f002_short_term_investments_core84_2nd_v085_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(investmentsc, assets), 4), 4))
def cg_f002_short_term_investments_core85_2nd_v086_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(investments, assets), 4), 4))
def cg_f002_short_term_investments_core86_2nd_v087_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(cashneq, assets), 4), 4))
def cg_f002_short_term_investments_core87_2nd_v088_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(investmentsc, investments + 1.0), 4), 4))
def cg_f002_short_term_investments_core88_2nd_v089_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(investmentsc, cashneq + 1.0), 4), 4))
def cg_f002_short_term_investments_core89_2nd_v090_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(investments, cashneq + 1.0), 4), 4))

def cg_f002_short_term_investments_core90_2nd_v091_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(investmentsc, 4), 4))
def cg_f002_short_term_investments_core91_2nd_v092_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(investments, 4), 4))
def cg_f002_short_term_investments_core92_2nd_v093_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f002_short_term_investments_core93_2nd_v094_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(assets, 4), 4))
def cg_f002_short_term_investments_core94_2nd_v095_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(investmentsc, assets), 4), 4))
def cg_f002_short_term_investments_core95_2nd_v096_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(investments, assets), 4), 4))
def cg_f002_short_term_investments_core96_2nd_v097_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(cashneq, assets), 4), 4))
def cg_f002_short_term_investments_core97_2nd_v098_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(investmentsc, investments + 1.0), 4), 4))
def cg_f002_short_term_investments_core98_2nd_v099_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(investmentsc, cashneq + 1.0), 4), 4))
def cg_f002_short_term_investments_core99_2nd_v100_signal(investmentsc, investments, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(investments, cashneq + 1.0), 4), 4))

def cg_f002_short_term_investments_core100_2nd_v101_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(investmentsc, 4), 4))
def cg_f002_short_term_investments_core101_2nd_v102_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(investments, 4), 4))
def cg_f002_short_term_investments_core102_2nd_v103_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f002_short_term_investments_core103_2nd_v104_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f002_short_term_investments_core104_2nd_v105_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investmentsc, assets), 4), 4))
def cg_f002_short_term_investments_core105_2nd_v106_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investments, assets), 4), 4))
def cg_f002_short_term_investments_core106_2nd_v107_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(cashneq, assets), 4), 4))
def cg_f002_short_term_investments_core107_2nd_v108_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investmentsc, investments + 1.0), 4), 4))
def cg_f002_short_term_investments_core108_2nd_v109_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investmentsc, cashneq + 1.0), 4), 4))
def cg_f002_short_term_investments_core109_2nd_v110_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investments, cashneq + 1.0), 4), 4))

def cg_f002_short_term_investments_core110_2nd_v111_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(investmentsc, 8), 8))
def cg_f002_short_term_investments_core111_2nd_v112_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(investments, 8), 8))
def cg_f002_short_term_investments_core112_2nd_v113_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f002_short_term_investments_core113_2nd_v114_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(assets, 8), 8))
def cg_f002_short_term_investments_core114_2nd_v115_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investmentsc, assets), 8), 8))
def cg_f002_short_term_investments_core115_2nd_v116_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investments, assets), 8), 8))
def cg_f002_short_term_investments_core116_2nd_v117_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(cashneq, assets), 8), 8))
def cg_f002_short_term_investments_core117_2nd_v118_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investmentsc, investments + 1.0), 8), 8))
def cg_f002_short_term_investments_core118_2nd_v119_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investmentsc, cashneq + 1.0), 8), 8))
def cg_f002_short_term_investments_core119_2nd_v120_signal(investmentsc, investments, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(investments, cashneq + 1.0), 8), 8))

def cg_f002_short_term_investments_core120_2nd_v121_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(investmentsc, 4), 4))
def cg_f002_short_term_investments_core121_2nd_v122_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(investments, 4), 4))
def cg_f002_short_term_investments_core122_2nd_v123_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f002_short_term_investments_core123_2nd_v124_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f002_short_term_investments_core124_2nd_v125_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(investmentsc, assets), 4), 4))
def cg_f002_short_term_investments_core125_2nd_v126_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(investments, assets), 4), 4))
def cg_f002_short_term_investments_core126_2nd_v127_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(cashneq, assets), 4), 4))
def cg_f002_short_term_investments_core127_2nd_v128_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(investmentsc, investments + 1.0), 4), 4))
def cg_f002_short_term_investments_core128_2nd_v129_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(investmentsc, cashneq + 1.0), 4), 4))
def cg_f002_short_term_investments_core129_2nd_v130_signal(investmentsc, investments, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(investments, cashneq + 1.0), 4), 4))

def cg_f002_short_term_investments_core130_2nd_v131_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(investmentsc, 4), 4), 8))
def cg_f002_short_term_investments_core131_2nd_v132_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(investments, 4), 4), 8))
def cg_f002_short_term_investments_core132_2nd_v133_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f002_short_term_investments_core133_2nd_v134_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f002_short_term_investments_core134_2nd_v135_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(investmentsc, assets), 4), 4), 8))
def cg_f002_short_term_investments_core135_2nd_v136_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(investments, assets), 4), 4), 8))
def cg_f002_short_term_investments_core136_2nd_v137_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f002_short_term_investments_core137_2nd_v138_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(investmentsc, investments + 1.0), 4), 4), 8))
def cg_f002_short_term_investments_core138_2nd_v139_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(investmentsc, cashneq + 1.0), 4), 4), 8))
def cg_f002_short_term_investments_core139_2nd_v140_signal(investmentsc, investments, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(investments, cashneq + 1.0), 4), 4), 8))

def cg_f002_short_term_investments_core140_2nd_v141_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(investmentsc, 4), 4), 12))
def cg_f002_short_term_investments_core141_2nd_v142_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(investments, 4), 4), 12))
def cg_f002_short_term_investments_core142_2nd_v143_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f002_short_term_investments_core143_2nd_v144_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f002_short_term_investments_core144_2nd_v145_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(investmentsc, assets), 4), 4), 12))
def cg_f002_short_term_investments_core145_2nd_v146_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(investments, assets), 4), 4), 12))
def cg_f002_short_term_investments_core146_2nd_v147_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f002_short_term_investments_core147_2nd_v148_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(investmentsc, investments + 1.0), 4), 4), 12))
def cg_f002_short_term_investments_core148_2nd_v149_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(investmentsc, cashneq + 1.0), 4), 4), 12))
def cg_f002_short_term_investments_core149_2nd_v150_signal(investmentsc, investments, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(investments, cashneq + 1.0), 4), 4), 12))
