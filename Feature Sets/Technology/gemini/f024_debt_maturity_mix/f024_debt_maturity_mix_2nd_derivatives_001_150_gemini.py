import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f024_debt_maturity_mix_core00_2nd_v001_signal(debtc, debtnc, debt):
    return _clean(_slope(debtc, 4))
def cg_f024_debt_maturity_mix_core01_2nd_v002_signal(debtc, debtnc, debt):
    return _clean(_slope(debtnc, 4))
def cg_f024_debt_maturity_mix_core02_2nd_v003_signal(debtc, debtnc, debt):
    return _clean(_slope(debt, 4))
def cg_f024_debt_maturity_mix_core03_2nd_v004_signal(debtc, debtnc, debt):
    return _clean(_slope(_safe_div(debtc, debt), 4))
def cg_f024_debt_maturity_mix_core04_2nd_v005_signal(debtc, debtnc, debt):
    return _clean(_slope(_safe_div(debtnc, debt), 4))
def cg_f024_debt_maturity_mix_core05_2nd_v006_signal(debtc, debtnc, debt):
    return _clean(_slope(_safe_div(debtc, debtnc.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core06_2nd_v007_signal(debtc, debtnc, debt):
    return _clean(_slope(debtc + debtnc, 4))
def cg_f024_debt_maturity_mix_core07_2nd_v008_signal(debtc, debtnc, debt):
    return _clean(_slope(debt - (debtc + debtnc), 4))
def cg_f024_debt_maturity_mix_core08_2nd_v009_signal(debtc, debtnc, debt):
    return _clean(_slope(_log(debtc.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core09_2nd_v010_signal(debtc, debtnc, debt):
    return _clean(_slope(_log(debtnc.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core10_2nd_v011_signal(debtc, debtnc, debt):
    return _clean(_slope(debtc, 8))
def cg_f024_debt_maturity_mix_core11_2nd_v012_signal(debtc, debtnc, debt):
    return _clean(_slope(debtnc, 8))
def cg_f024_debt_maturity_mix_core12_2nd_v013_signal(debtc, debtnc, debt):
    return _clean(_slope(debt, 8))
def cg_f024_debt_maturity_mix_core13_2nd_v014_signal(debtc, debtnc, debt):
    return _clean(_slope(_safe_div(debtc, debt), 8))
def cg_f024_debt_maturity_mix_core14_2nd_v015_signal(debtc, debtnc, debt):
    return _clean(_slope(_safe_div(debtnc, debt), 8))
def cg_f024_debt_maturity_mix_core15_2nd_v016_signal(debtc, debtnc, debt):
    return _clean(_slope(_safe_div(debtc, debtnc.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core16_2nd_v017_signal(debtc, debtnc, debt):
    return _clean(_slope(debtc + debtnc, 8))
def cg_f024_debt_maturity_mix_core17_2nd_v018_signal(debtc, debtnc, debt):
    return _clean(_slope(debt - (debtc + debtnc), 8))
def cg_f024_debt_maturity_mix_core18_2nd_v019_signal(debtc, debtnc, debt):
    return _clean(_slope(_log(debtc.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core19_2nd_v020_signal(debtc, debtnc, debt):
    return _clean(_slope(_log(debtnc.abs() + 1.0), 8))
def cg_f024_debt_maturity_mix_core20_2nd_v021_signal(debtc, debtnc, debt):
    return _clean(_diff(debtc, 4))
def cg_f024_debt_maturity_mix_core21_2nd_v022_signal(debtc, debtnc, debt):
    return _clean(_diff(debtnc, 4))
def cg_f024_debt_maturity_mix_core22_2nd_v023_signal(debtc, debtnc, debt):
    return _clean(_diff(debt, 4))
def cg_f024_debt_maturity_mix_core23_2nd_v024_signal(debtc, debtnc, debt):
    return _clean(_diff(_safe_div(debtc, debt), 4))
def cg_f024_debt_maturity_mix_core24_2nd_v025_signal(debtc, debtnc, debt):
    return _clean(_diff(_safe_div(debtnc, debt), 4))
def cg_f024_debt_maturity_mix_core25_2nd_v026_signal(debtc, debtnc, debt):
    return _clean(_diff(_safe_div(debtc, debtnc.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core26_2nd_v027_signal(debtc, debtnc, debt):
    return _clean(_diff(debtc + debtnc, 4))
def cg_f024_debt_maturity_mix_core27_2nd_v028_signal(debtc, debtnc, debt):
    return _clean(_diff(debt - (debtc + debtnc), 4))
def cg_f024_debt_maturity_mix_core28_2nd_v029_signal(debtc, debtnc, debt):
    return _clean(_diff(_log(debtc.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core29_2nd_v030_signal(debtc, debtnc, debt):
    return _clean(_diff(_log(debtnc.abs() + 1.0), 4))
def cg_f024_debt_maturity_mix_core30_2nd_v031_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debtc, 4), 8))
def cg_f024_debt_maturity_mix_core31_2nd_v032_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debtnc, 4), 8))
def cg_f024_debt_maturity_mix_core32_2nd_v033_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debt, 4), 8))
def cg_f024_debt_maturity_mix_core33_2nd_v034_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_safe_div(debtc, debt), 4), 8))
def cg_f024_debt_maturity_mix_core34_2nd_v035_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_safe_div(debtnc, debt), 4), 8))
def cg_f024_debt_maturity_mix_core35_2nd_v036_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_safe_div(debtc, debtnc.abs() + 1.0), 4), 8))
def cg_f024_debt_maturity_mix_core36_2nd_v037_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debtc + debtnc, 4), 8))
def cg_f024_debt_maturity_mix_core37_2nd_v038_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debt - (debtc + debtnc), 4), 8))
def cg_f024_debt_maturity_mix_core38_2nd_v039_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_log(debtc.abs() + 1.0), 4), 8))
def cg_f024_debt_maturity_mix_core39_2nd_v040_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_log(debtnc.abs() + 1.0), 4), 8))
def cg_f024_debt_maturity_mix_core40_2nd_v041_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debtc, 8), 12))
def cg_f024_debt_maturity_mix_core41_2nd_v042_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debtnc, 8), 12))
def cg_f024_debt_maturity_mix_core42_2nd_v043_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debt, 8), 12))
def cg_f024_debt_maturity_mix_core43_2nd_v044_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_safe_div(debtc, debt), 8), 12))
def cg_f024_debt_maturity_mix_core44_2nd_v045_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_safe_div(debtnc, debt), 8), 12))
def cg_f024_debt_maturity_mix_core45_2nd_v046_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_safe_div(debtc, debtnc.abs() + 1.0), 8), 12))
def cg_f024_debt_maturity_mix_core46_2nd_v047_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debtc + debtnc, 8), 12))
def cg_f024_debt_maturity_mix_core47_2nd_v048_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(debt - (debtc + debtnc), 8), 12))
def cg_f024_debt_maturity_mix_core48_2nd_v049_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_log(debtc.abs() + 1.0), 8), 12))
def cg_f024_debt_maturity_mix_core49_2nd_v050_signal(debtc, debtnc, debt):
    return _clean(_z(_slope(_log(debtnc.abs() + 1.0), 8), 12))
def cg_f024_debt_maturity_mix_core50_2nd_v051_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(debtc, 4), 8))
def cg_f024_debt_maturity_mix_core51_2nd_v052_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(debtnc, 4), 8))
def cg_f024_debt_maturity_mix_core52_2nd_v053_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(debt, 4), 8))
def cg_f024_debt_maturity_mix_core53_2nd_v054_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_safe_div(debtc, debt), 4), 8))
def cg_f024_debt_maturity_mix_core54_2nd_v055_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_safe_div(debtnc, debt), 4), 8))
def cg_f024_debt_maturity_mix_core55_2nd_v056_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_safe_div(debtc, debtnc.abs() + 1.0), 4), 8))
def cg_f024_debt_maturity_mix_core56_2nd_v057_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(debtc + debtnc, 4), 8))
def cg_f024_debt_maturity_mix_core57_2nd_v058_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(debt - (debtc + debtnc), 4), 8))
def cg_f024_debt_maturity_mix_core58_2nd_v059_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_log(debtc.abs() + 1.0), 4), 8))
def cg_f024_debt_maturity_mix_core59_2nd_v060_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_log(debtnc.abs() + 1.0), 4), 8))
def cg_f024_debt_maturity_mix_core60_2nd_v061_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(debtc, 4), 12))
def cg_f024_debt_maturity_mix_core61_2nd_v062_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(debtnc, 4), 12))
def cg_f024_debt_maturity_mix_core62_2nd_v063_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(debt, 4), 12))
def cg_f024_debt_maturity_mix_core63_2nd_v064_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_safe_div(debtc, debt), 4), 12))
def cg_f024_debt_maturity_mix_core64_2nd_v065_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_safe_div(debtnc, debt), 4), 12))
def cg_f024_debt_maturity_mix_core65_2nd_v066_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_safe_div(debtc, debtnc.abs() + 1.0), 4), 12))
def cg_f024_debt_maturity_mix_core66_2nd_v067_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(debtc + debtnc, 4), 12))
def cg_f024_debt_maturity_mix_core67_2nd_v068_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(debt - (debtc + debtnc), 4), 12))
def cg_f024_debt_maturity_mix_core68_2nd_v069_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_log(debtc.abs() + 1.0), 4), 12))
def cg_f024_debt_maturity_mix_core69_2nd_v070_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_log(debtnc.abs() + 1.0), 4), 12))
def cg_f024_debt_maturity_mix_core70_2nd_v071_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(debtc, 4), 12))
def cg_f024_debt_maturity_mix_core71_2nd_v072_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(debtnc, 4), 12))
def cg_f024_debt_maturity_mix_core72_2nd_v073_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(debt, 4), 12))
def cg_f024_debt_maturity_mix_core73_2nd_v074_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(_safe_div(debtc, debt), 4), 12))
def cg_f024_debt_maturity_mix_core74_2nd_v075_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(_safe_div(debtnc, debt), 4), 12))
def cg_f024_debt_maturity_mix_core75_2nd_v076_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(_safe_div(debtc, debtnc.abs() + 1.0), 4), 12))
def cg_f024_debt_maturity_mix_core76_2nd_v077_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(debtc + debtnc, 4), 12))
def cg_f024_debt_maturity_mix_core77_2nd_v078_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(debt - (debtc + debtnc), 4), 12))
def cg_f024_debt_maturity_mix_core78_2nd_v079_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(_log(debtc.abs() + 1.0), 4), 12))
def cg_f024_debt_maturity_mix_core79_2nd_v080_signal(debtc, debtnc, debt):
    return _clean(_rank(_diff(_log(debtnc.abs() + 1.0), 4), 12))
def cg_f024_debt_maturity_mix_core80_2nd_v081_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(debtc, 4), 4))
def cg_f024_debt_maturity_mix_core81_2nd_v082_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core82_2nd_v083_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(debt, 4), 4))
def cg_f024_debt_maturity_mix_core83_2nd_v084_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(_safe_div(debtc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core84_2nd_v085_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(_safe_div(debtnc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core85_2nd_v086_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(_safe_div(debtc, debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core86_2nd_v087_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(debtc + debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core87_2nd_v088_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(debt - (debtc + debtnc), 4), 4))
def cg_f024_debt_maturity_mix_core88_2nd_v089_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(_log(debtc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core89_2nd_v090_signal(debtc, debtnc, debt):
    return _clean(_mean(_slope(_log(debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core90_2nd_v091_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(debtc, 4), 4))
def cg_f024_debt_maturity_mix_core91_2nd_v092_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core92_2nd_v093_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(debt, 4), 4))
def cg_f024_debt_maturity_mix_core93_2nd_v094_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(_safe_div(debtc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core94_2nd_v095_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(_safe_div(debtnc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core95_2nd_v096_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(_safe_div(debtc, debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core96_2nd_v097_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(debtc + debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core97_2nd_v098_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(debt - (debtc + debtnc), 4), 4))
def cg_f024_debt_maturity_mix_core98_2nd_v099_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(_log(debtc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core99_2nd_v100_signal(debtc, debtnc, debt):
    return _clean(_mean(_diff(_log(debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core100_2nd_v101_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debtc, 4), 4))
def cg_f024_debt_maturity_mix_core101_2nd_v102_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core102_2nd_v103_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debt, 4), 4))
def cg_f024_debt_maturity_mix_core103_2nd_v104_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_safe_div(debtc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core104_2nd_v105_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_safe_div(debtnc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core105_2nd_v106_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_safe_div(debtc, debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core106_2nd_v107_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debtc + debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core107_2nd_v108_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debt - (debtc + debtnc), 4), 4))
def cg_f024_debt_maturity_mix_core108_2nd_v109_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_log(debtc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core109_2nd_v110_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_log(debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core110_2nd_v111_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debtc, 8), 8))
def cg_f024_debt_maturity_mix_core111_2nd_v112_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debtnc, 8), 8))
def cg_f024_debt_maturity_mix_core112_2nd_v113_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debt, 8), 8))
def cg_f024_debt_maturity_mix_core113_2nd_v114_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_safe_div(debtc, debt), 8), 8))
def cg_f024_debt_maturity_mix_core114_2nd_v115_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_safe_div(debtnc, debt), 8), 8))
def cg_f024_debt_maturity_mix_core115_2nd_v116_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_safe_div(debtc, debtnc.abs() + 1.0), 8), 8))
def cg_f024_debt_maturity_mix_core116_2nd_v117_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debtc + debtnc, 8), 8))
def cg_f024_debt_maturity_mix_core117_2nd_v118_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(debt - (debtc + debtnc), 8), 8))
def cg_f024_debt_maturity_mix_core118_2nd_v119_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_log(debtc.abs() + 1.0), 8), 8))
def cg_f024_debt_maturity_mix_core119_2nd_v120_signal(debtc, debtnc, debt):
    return _clean(_slope(_mean(_log(debtnc.abs() + 1.0), 8), 8))
def cg_f024_debt_maturity_mix_core120_2nd_v121_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(debtc, 4), 4))
def cg_f024_debt_maturity_mix_core121_2nd_v122_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core122_2nd_v123_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(debt, 4), 4))
def cg_f024_debt_maturity_mix_core123_2nd_v124_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(_safe_div(debtc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core124_2nd_v125_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(_safe_div(debtnc, debt), 4), 4))
def cg_f024_debt_maturity_mix_core125_2nd_v126_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(_safe_div(debtc, debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core126_2nd_v127_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(debtc + debtnc, 4), 4))
def cg_f024_debt_maturity_mix_core127_2nd_v128_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(debt - (debtc + debtnc), 4), 4))
def cg_f024_debt_maturity_mix_core128_2nd_v129_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(_log(debtc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core129_2nd_v130_signal(debtc, debtnc, debt):
    return _clean(_diff(_mean(_log(debtnc.abs() + 1.0), 4), 4))
def cg_f024_debt_maturity_mix_core130_2nd_v131_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(debtc, 4), 4), 8))
def cg_f024_debt_maturity_mix_core131_2nd_v132_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(debtnc, 4), 4), 8))
def cg_f024_debt_maturity_mix_core132_2nd_v133_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(debt, 4), 4), 8))
def cg_f024_debt_maturity_mix_core133_2nd_v134_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(_safe_div(debtc, debt), 4), 4), 8))
def cg_f024_debt_maturity_mix_core134_2nd_v135_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(_safe_div(debtnc, debt), 4), 4), 8))
def cg_f024_debt_maturity_mix_core135_2nd_v136_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(_safe_div(debtc, debtnc.abs() + 1.0), 4), 4), 8))
def cg_f024_debt_maturity_mix_core136_2nd_v137_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(debtc + debtnc, 4), 4), 8))
def cg_f024_debt_maturity_mix_core137_2nd_v138_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(debt - (debtc + debtnc), 4), 4), 8))
def cg_f024_debt_maturity_mix_core138_2nd_v139_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(_log(debtc.abs() + 1.0), 4), 4), 8))
def cg_f024_debt_maturity_mix_core139_2nd_v140_signal(debtc, debtnc, debt):
    return _clean(_z(_diff(_mean(_log(debtnc.abs() + 1.0), 4), 4), 8))
def cg_f024_debt_maturity_mix_core140_2nd_v141_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(debtc, 4), 4), 12))
def cg_f024_debt_maturity_mix_core141_2nd_v142_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(debtnc, 4), 4), 12))
def cg_f024_debt_maturity_mix_core142_2nd_v143_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(debt, 4), 4), 12))
def cg_f024_debt_maturity_mix_core143_2nd_v144_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(_safe_div(debtc, debt), 4), 4), 12))
def cg_f024_debt_maturity_mix_core144_2nd_v145_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(_safe_div(debtnc, debt), 4), 4), 12))
def cg_f024_debt_maturity_mix_core145_2nd_v146_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(_safe_div(debtc, debtnc.abs() + 1.0), 4), 4), 12))
def cg_f024_debt_maturity_mix_core146_2nd_v147_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(debtc + debtnc, 4), 4), 12))
def cg_f024_debt_maturity_mix_core147_2nd_v148_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(debt - (debtc + debtnc), 4), 4), 12))
def cg_f024_debt_maturity_mix_core148_2nd_v149_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(_log(debtc.abs() + 1.0), 4), 4), 12))
def cg_f024_debt_maturity_mix_core149_2nd_v150_signal(debtc, debtnc, debt):
    return _clean(_rank(_slope(_mean(_log(debtnc.abs() + 1.0), 4), 4), 12))