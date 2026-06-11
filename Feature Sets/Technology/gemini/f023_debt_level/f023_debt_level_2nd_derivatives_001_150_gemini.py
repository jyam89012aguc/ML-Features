import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f023_debt_level_core00_2nd_v001_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(debt, 4))
def cg_f023_debt_level_core01_2nd_v002_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(debtusd, 4))
def cg_f023_debt_level_core02_2nd_v003_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debt, assets), 4))
def cg_f023_debt_level_core03_2nd_v004_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debt, equity), 4))
def cg_f023_debt_level_core04_2nd_v005_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debt, marketcap), 4))
def cg_f023_debt_level_core05_2nd_v006_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debtusd, assets), 4))
def cg_f023_debt_level_core06_2nd_v007_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debtusd, marketcap), 4))
def cg_f023_debt_level_core07_2nd_v008_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(debt - debtusd, 4))
def cg_f023_debt_level_core08_2nd_v009_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_log(debt.abs() + 1.0), 4))
def cg_f023_debt_level_core09_2nd_v010_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(assets, equity), 4))
def cg_f023_debt_level_core10_2nd_v011_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(debt, 8))
def cg_f023_debt_level_core11_2nd_v012_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(debtusd, 8))
def cg_f023_debt_level_core12_2nd_v013_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debt, assets), 8))
def cg_f023_debt_level_core13_2nd_v014_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debt, equity), 8))
def cg_f023_debt_level_core14_2nd_v015_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debt, marketcap), 8))
def cg_f023_debt_level_core15_2nd_v016_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debtusd, assets), 8))
def cg_f023_debt_level_core16_2nd_v017_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(debtusd, marketcap), 8))
def cg_f023_debt_level_core17_2nd_v018_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(debt - debtusd, 8))
def cg_f023_debt_level_core18_2nd_v019_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_log(debt.abs() + 1.0), 8))
def cg_f023_debt_level_core19_2nd_v020_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_safe_div(assets, equity), 8))
def cg_f023_debt_level_core20_2nd_v021_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(debt, 4))
def cg_f023_debt_level_core21_2nd_v022_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(debtusd, 4))
def cg_f023_debt_level_core22_2nd_v023_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_safe_div(debt, assets), 4))
def cg_f023_debt_level_core23_2nd_v024_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_safe_div(debt, equity), 4))
def cg_f023_debt_level_core24_2nd_v025_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_safe_div(debt, marketcap), 4))
def cg_f023_debt_level_core25_2nd_v026_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_safe_div(debtusd, assets), 4))
def cg_f023_debt_level_core26_2nd_v027_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_safe_div(debtusd, marketcap), 4))
def cg_f023_debt_level_core27_2nd_v028_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(debt - debtusd, 4))
def cg_f023_debt_level_core28_2nd_v029_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_log(debt.abs() + 1.0), 4))
def cg_f023_debt_level_core29_2nd_v030_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_safe_div(assets, equity), 4))
def cg_f023_debt_level_core30_2nd_v031_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(debt, 4), 8))
def cg_f023_debt_level_core31_2nd_v032_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(debtusd, 4), 8))
def cg_f023_debt_level_core32_2nd_v033_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debt, assets), 4), 8))
def cg_f023_debt_level_core33_2nd_v034_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debt, equity), 4), 8))
def cg_f023_debt_level_core34_2nd_v035_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debt, marketcap), 4), 8))
def cg_f023_debt_level_core35_2nd_v036_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debtusd, assets), 4), 8))
def cg_f023_debt_level_core36_2nd_v037_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debtusd, marketcap), 4), 8))
def cg_f023_debt_level_core37_2nd_v038_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(debt - debtusd, 4), 8))
def cg_f023_debt_level_core38_2nd_v039_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_log(debt.abs() + 1.0), 4), 8))
def cg_f023_debt_level_core39_2nd_v040_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(assets, equity), 4), 8))
def cg_f023_debt_level_core40_2nd_v041_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(debt, 8), 12))
def cg_f023_debt_level_core41_2nd_v042_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(debtusd, 8), 12))
def cg_f023_debt_level_core42_2nd_v043_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debt, assets), 8), 12))
def cg_f023_debt_level_core43_2nd_v044_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debt, equity), 8), 12))
def cg_f023_debt_level_core44_2nd_v045_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debt, marketcap), 8), 12))
def cg_f023_debt_level_core45_2nd_v046_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debtusd, assets), 8), 12))
def cg_f023_debt_level_core46_2nd_v047_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(debtusd, marketcap), 8), 12))
def cg_f023_debt_level_core47_2nd_v048_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(debt - debtusd, 8), 12))
def cg_f023_debt_level_core48_2nd_v049_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_log(debt.abs() + 1.0), 8), 12))
def cg_f023_debt_level_core49_2nd_v050_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_slope(_safe_div(assets, equity), 8), 12))
def cg_f023_debt_level_core50_2nd_v051_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(debt, 4), 8))
def cg_f023_debt_level_core51_2nd_v052_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(debtusd, 4), 8))
def cg_f023_debt_level_core52_2nd_v053_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_safe_div(debt, assets), 4), 8))
def cg_f023_debt_level_core53_2nd_v054_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_safe_div(debt, equity), 4), 8))
def cg_f023_debt_level_core54_2nd_v055_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_safe_div(debt, marketcap), 4), 8))
def cg_f023_debt_level_core55_2nd_v056_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_safe_div(debtusd, assets), 4), 8))
def cg_f023_debt_level_core56_2nd_v057_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_safe_div(debtusd, marketcap), 4), 8))
def cg_f023_debt_level_core57_2nd_v058_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(debt - debtusd, 4), 8))
def cg_f023_debt_level_core58_2nd_v059_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_log(debt.abs() + 1.0), 4), 8))
def cg_f023_debt_level_core59_2nd_v060_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_safe_div(assets, equity), 4), 8))
def cg_f023_debt_level_core60_2nd_v061_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(debt, 4), 12))
def cg_f023_debt_level_core61_2nd_v062_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(debtusd, 4), 12))
def cg_f023_debt_level_core62_2nd_v063_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_safe_div(debt, assets), 4), 12))
def cg_f023_debt_level_core63_2nd_v064_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_safe_div(debt, equity), 4), 12))
def cg_f023_debt_level_core64_2nd_v065_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_safe_div(debt, marketcap), 4), 12))
def cg_f023_debt_level_core65_2nd_v066_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_safe_div(debtusd, assets), 4), 12))
def cg_f023_debt_level_core66_2nd_v067_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_safe_div(debtusd, marketcap), 4), 12))
def cg_f023_debt_level_core67_2nd_v068_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(debt - debtusd, 4), 12))
def cg_f023_debt_level_core68_2nd_v069_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_log(debt.abs() + 1.0), 4), 12))
def cg_f023_debt_level_core69_2nd_v070_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_safe_div(assets, equity), 4), 12))
def cg_f023_debt_level_core70_2nd_v071_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(debt, 4), 12))
def cg_f023_debt_level_core71_2nd_v072_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(debtusd, 4), 12))
def cg_f023_debt_level_core72_2nd_v073_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_safe_div(debt, assets), 4), 12))
def cg_f023_debt_level_core73_2nd_v074_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_safe_div(debt, equity), 4), 12))
def cg_f023_debt_level_core74_2nd_v075_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_safe_div(debt, marketcap), 4), 12))
def cg_f023_debt_level_core75_2nd_v076_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_safe_div(debtusd, assets), 4), 12))
def cg_f023_debt_level_core76_2nd_v077_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_safe_div(debtusd, marketcap), 4), 12))
def cg_f023_debt_level_core77_2nd_v078_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(debt - debtusd, 4), 12))
def cg_f023_debt_level_core78_2nd_v079_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_log(debt.abs() + 1.0), 4), 12))
def cg_f023_debt_level_core79_2nd_v080_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_diff(_safe_div(assets, equity), 4), 12))
def cg_f023_debt_level_core80_2nd_v081_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(debt, 4), 4))
def cg_f023_debt_level_core81_2nd_v082_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(debtusd, 4), 4))
def cg_f023_debt_level_core82_2nd_v083_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_safe_div(debt, assets), 4), 4))
def cg_f023_debt_level_core83_2nd_v084_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_safe_div(debt, equity), 4), 4))
def cg_f023_debt_level_core84_2nd_v085_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_safe_div(debt, marketcap), 4), 4))
def cg_f023_debt_level_core85_2nd_v086_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_safe_div(debtusd, assets), 4), 4))
def cg_f023_debt_level_core86_2nd_v087_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_safe_div(debtusd, marketcap), 4), 4))
def cg_f023_debt_level_core87_2nd_v088_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(debt - debtusd, 4), 4))
def cg_f023_debt_level_core88_2nd_v089_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_log(debt.abs() + 1.0), 4), 4))
def cg_f023_debt_level_core89_2nd_v090_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_slope(_safe_div(assets, equity), 4), 4))
def cg_f023_debt_level_core90_2nd_v091_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(debt, 4), 4))
def cg_f023_debt_level_core91_2nd_v092_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(debtusd, 4), 4))
def cg_f023_debt_level_core92_2nd_v093_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_safe_div(debt, assets), 4), 4))
def cg_f023_debt_level_core93_2nd_v094_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_safe_div(debt, equity), 4), 4))
def cg_f023_debt_level_core94_2nd_v095_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_safe_div(debt, marketcap), 4), 4))
def cg_f023_debt_level_core95_2nd_v096_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_safe_div(debtusd, assets), 4), 4))
def cg_f023_debt_level_core96_2nd_v097_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_safe_div(debtusd, marketcap), 4), 4))
def cg_f023_debt_level_core97_2nd_v098_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(debt - debtusd, 4), 4))
def cg_f023_debt_level_core98_2nd_v099_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_log(debt.abs() + 1.0), 4), 4))
def cg_f023_debt_level_core99_2nd_v100_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_mean(_diff(_safe_div(assets, equity), 4), 4))
def cg_f023_debt_level_core100_2nd_v101_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(debt, 4), 4))
def cg_f023_debt_level_core101_2nd_v102_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(debtusd, 4), 4))
def cg_f023_debt_level_core102_2nd_v103_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debt, assets), 4), 4))
def cg_f023_debt_level_core103_2nd_v104_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debt, equity), 4), 4))
def cg_f023_debt_level_core104_2nd_v105_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debt, marketcap), 4), 4))
def cg_f023_debt_level_core105_2nd_v106_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debtusd, assets), 4), 4))
def cg_f023_debt_level_core106_2nd_v107_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debtusd, marketcap), 4), 4))
def cg_f023_debt_level_core107_2nd_v108_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(debt - debtusd, 4), 4))
def cg_f023_debt_level_core108_2nd_v109_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_log(debt.abs() + 1.0), 4), 4))
def cg_f023_debt_level_core109_2nd_v110_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(assets, equity), 4), 4))
def cg_f023_debt_level_core110_2nd_v111_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(debt, 8), 8))
def cg_f023_debt_level_core111_2nd_v112_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(debtusd, 8), 8))
def cg_f023_debt_level_core112_2nd_v113_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debt, assets), 8), 8))
def cg_f023_debt_level_core113_2nd_v114_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debt, equity), 8), 8))
def cg_f023_debt_level_core114_2nd_v115_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debt, marketcap), 8), 8))
def cg_f023_debt_level_core115_2nd_v116_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debtusd, assets), 8), 8))
def cg_f023_debt_level_core116_2nd_v117_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(debtusd, marketcap), 8), 8))
def cg_f023_debt_level_core117_2nd_v118_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(debt - debtusd, 8), 8))
def cg_f023_debt_level_core118_2nd_v119_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_log(debt.abs() + 1.0), 8), 8))
def cg_f023_debt_level_core119_2nd_v120_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_slope(_mean(_safe_div(assets, equity), 8), 8))
def cg_f023_debt_level_core120_2nd_v121_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(debt, 4), 4))
def cg_f023_debt_level_core121_2nd_v122_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(debtusd, 4), 4))
def cg_f023_debt_level_core122_2nd_v123_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_safe_div(debt, assets), 4), 4))
def cg_f023_debt_level_core123_2nd_v124_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_safe_div(debt, equity), 4), 4))
def cg_f023_debt_level_core124_2nd_v125_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_safe_div(debt, marketcap), 4), 4))
def cg_f023_debt_level_core125_2nd_v126_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_safe_div(debtusd, assets), 4), 4))
def cg_f023_debt_level_core126_2nd_v127_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_safe_div(debtusd, marketcap), 4), 4))
def cg_f023_debt_level_core127_2nd_v128_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(debt - debtusd, 4), 4))
def cg_f023_debt_level_core128_2nd_v129_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_log(debt.abs() + 1.0), 4), 4))
def cg_f023_debt_level_core129_2nd_v130_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_diff(_mean(_safe_div(assets, equity), 4), 4))
def cg_f023_debt_level_core130_2nd_v131_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(debt, 4), 4), 8))
def cg_f023_debt_level_core131_2nd_v132_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(debtusd, 4), 4), 8))
def cg_f023_debt_level_core132_2nd_v133_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(debt, assets), 4), 4), 8))
def cg_f023_debt_level_core133_2nd_v134_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(debt, equity), 4), 4), 8))
def cg_f023_debt_level_core134_2nd_v135_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(debt, marketcap), 4), 4), 8))
def cg_f023_debt_level_core135_2nd_v136_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(debtusd, assets), 4), 4), 8))
def cg_f023_debt_level_core136_2nd_v137_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(debtusd, marketcap), 4), 4), 8))
def cg_f023_debt_level_core137_2nd_v138_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(debt - debtusd, 4), 4), 8))
def cg_f023_debt_level_core138_2nd_v139_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_log(debt.abs() + 1.0), 4), 4), 8))
def cg_f023_debt_level_core139_2nd_v140_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_z(_diff(_mean(_safe_div(assets, equity), 4), 4), 8))
def cg_f023_debt_level_core140_2nd_v141_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(debt, 4), 4), 12))
def cg_f023_debt_level_core141_2nd_v142_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(debtusd, 4), 4), 12))
def cg_f023_debt_level_core142_2nd_v143_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(debt, assets), 4), 4), 12))
def cg_f023_debt_level_core143_2nd_v144_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(debt, equity), 4), 4), 12))
def cg_f023_debt_level_core144_2nd_v145_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(debt, marketcap), 4), 4), 12))
def cg_f023_debt_level_core145_2nd_v146_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(debtusd, assets), 4), 4), 12))
def cg_f023_debt_level_core146_2nd_v147_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(debtusd, marketcap), 4), 4), 12))
def cg_f023_debt_level_core147_2nd_v148_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(debt - debtusd, 4), 4), 12))
def cg_f023_debt_level_core148_2nd_v149_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_log(debt.abs() + 1.0), 4), 4), 12))
def cg_f023_debt_level_core149_2nd_v150_signal(debt, debtusd, assets, equity, marketcap):
    return _clean(_rank(_slope(_mean(_safe_div(assets, equity), 4), 4), 12))