import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f097_specialist_and_quality_fund_exposure_core00_2nd_v001_signal(investorname, value, units, securitytype):
    return _clean(_slope(value, 4))
def cg_f097_specialist_and_quality_fund_exposure_core01_2nd_v002_signal(investorname, value, units, securitytype):
    return _clean(_slope(units, 4))
def cg_f097_specialist_and_quality_fund_exposure_core02_2nd_v003_signal(investorname, value, units, securitytype):
    return _clean(_slope(_safe_div(value, units), 4))
def cg_f097_specialist_and_quality_fund_exposure_core03_2nd_v004_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(value + 1.0), 4))
def cg_f097_specialist_and_quality_fund_exposure_core04_2nd_v005_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(units + 1.0), 4))
def cg_f097_specialist_and_quality_fund_exposure_core05_2nd_v006_signal(investorname, value, units, securitytype):
    return _clean(_slope(value.abs(), 4))
def cg_f097_specialist_and_quality_fund_exposure_core06_2nd_v007_signal(investorname, value, units, securitytype):
    return _clean(_slope(units.abs(), 4))
def cg_f097_specialist_and_quality_fund_exposure_core07_2nd_v008_signal(investorname, value, units, securitytype):
    return _clean(_slope(_safe_div(units, value), 4))
def cg_f097_specialist_and_quality_fund_exposure_core08_2nd_v009_signal(investorname, value, units, securitytype):
    return _clean(_slope(value * units, 4))
def cg_f097_specialist_and_quality_fund_exposure_core09_2nd_v010_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(value * units + 1.0), 4))
def cg_f097_specialist_and_quality_fund_exposure_core10_2nd_v011_signal(investorname, value, units, securitytype):
    return _clean(_slope(value, 8))
def cg_f097_specialist_and_quality_fund_exposure_core11_2nd_v012_signal(investorname, value, units, securitytype):
    return _clean(_slope(units, 8))
def cg_f097_specialist_and_quality_fund_exposure_core12_2nd_v013_signal(investorname, value, units, securitytype):
    return _clean(_slope(_safe_div(value, units), 8))
def cg_f097_specialist_and_quality_fund_exposure_core13_2nd_v014_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(value + 1.0), 8))
def cg_f097_specialist_and_quality_fund_exposure_core14_2nd_v015_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(units + 1.0), 8))
def cg_f097_specialist_and_quality_fund_exposure_core15_2nd_v016_signal(investorname, value, units, securitytype):
    return _clean(_slope(value.abs(), 8))
def cg_f097_specialist_and_quality_fund_exposure_core16_2nd_v017_signal(investorname, value, units, securitytype):
    return _clean(_slope(units.abs(), 8))
def cg_f097_specialist_and_quality_fund_exposure_core17_2nd_v018_signal(investorname, value, units, securitytype):
    return _clean(_slope(_safe_div(units, value), 8))
def cg_f097_specialist_and_quality_fund_exposure_core18_2nd_v019_signal(investorname, value, units, securitytype):
    return _clean(_slope(value * units, 8))
def cg_f097_specialist_and_quality_fund_exposure_core19_2nd_v020_signal(investorname, value, units, securitytype):
    return _clean(_slope(_log(value * units + 1.0), 8))
def cg_f097_specialist_and_quality_fund_exposure_core20_2nd_v021_signal(investorname, value, units, securitytype):
    return _clean(_diff(value, 4))
def cg_f097_specialist_and_quality_fund_exposure_core21_2nd_v022_signal(investorname, value, units, securitytype):
    return _clean(_diff(units, 4))
def cg_f097_specialist_and_quality_fund_exposure_core22_2nd_v023_signal(investorname, value, units, securitytype):
    return _clean(_diff(_safe_div(value, units), 4))
def cg_f097_specialist_and_quality_fund_exposure_core23_2nd_v024_signal(investorname, value, units, securitytype):
    return _clean(_diff(_log(value + 1.0), 4))
def cg_f097_specialist_and_quality_fund_exposure_core24_2nd_v025_signal(investorname, value, units, securitytype):
    return _clean(_diff(_log(units + 1.0), 4))
def cg_f097_specialist_and_quality_fund_exposure_core25_2nd_v026_signal(investorname, value, units, securitytype):
    return _clean(_diff(value.abs(), 4))
def cg_f097_specialist_and_quality_fund_exposure_core26_2nd_v027_signal(investorname, value, units, securitytype):
    return _clean(_diff(units.abs(), 4))
def cg_f097_specialist_and_quality_fund_exposure_core27_2nd_v028_signal(investorname, value, units, securitytype):
    return _clean(_diff(_safe_div(units, value), 4))
def cg_f097_specialist_and_quality_fund_exposure_core28_2nd_v029_signal(investorname, value, units, securitytype):
    return _clean(_diff(value * units, 4))
def cg_f097_specialist_and_quality_fund_exposure_core29_2nd_v030_signal(investorname, value, units, securitytype):
    return _clean(_diff(_log(value * units + 1.0), 4))
def cg_f097_specialist_and_quality_fund_exposure_core30_2nd_v031_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(value, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core31_2nd_v032_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(units, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core32_2nd_v033_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_safe_div(value, units), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core33_2nd_v034_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_log(value + 1.0), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core34_2nd_v035_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_log(units + 1.0), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core35_2nd_v036_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(value.abs(), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core36_2nd_v037_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(units.abs(), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core37_2nd_v038_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_safe_div(units, value), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core38_2nd_v039_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(value * units, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core39_2nd_v040_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_log(value * units + 1.0), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core40_2nd_v041_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(value, 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core41_2nd_v042_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(units, 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core42_2nd_v043_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_safe_div(value, units), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core43_2nd_v044_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_log(value + 1.0), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core44_2nd_v045_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_log(units + 1.0), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core45_2nd_v046_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(value.abs(), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core46_2nd_v047_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(units.abs(), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core47_2nd_v048_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_safe_div(units, value), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core48_2nd_v049_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(value * units, 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core49_2nd_v050_signal(investorname, value, units, securitytype):
    return _clean(_z(_slope(_log(value * units + 1.0), 8), 12))
def cg_f097_specialist_and_quality_fund_exposure_core50_2nd_v051_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(value, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core51_2nd_v052_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(units, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core52_2nd_v053_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_safe_div(value, units), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core53_2nd_v054_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_log(value + 1.0), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core54_2nd_v055_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_log(units + 1.0), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core55_2nd_v056_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(value.abs(), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core56_2nd_v057_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(units.abs(), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core57_2nd_v058_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_safe_div(units, value), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core58_2nd_v059_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(value * units, 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core59_2nd_v060_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_log(value * units + 1.0), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core60_2nd_v061_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(value, 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core61_2nd_v062_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(units, 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core62_2nd_v063_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_safe_div(value, units), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core63_2nd_v064_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_log(value + 1.0), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core64_2nd_v065_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_log(units + 1.0), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core65_2nd_v066_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(value.abs(), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core66_2nd_v067_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(units.abs(), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core67_2nd_v068_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_safe_div(units, value), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core68_2nd_v069_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(value * units, 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core69_2nd_v070_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_log(value * units + 1.0), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core70_2nd_v071_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(value, 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core71_2nd_v072_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(units, 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core72_2nd_v073_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(_safe_div(value, units), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core73_2nd_v074_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(_log(value + 1.0), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core74_2nd_v075_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(_log(units + 1.0), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core75_2nd_v076_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(value.abs(), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core76_2nd_v077_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(units.abs(), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core77_2nd_v078_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(_safe_div(units, value), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core78_2nd_v079_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(value * units, 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core79_2nd_v080_signal(investorname, value, units, securitytype):
    return _clean(_rank(_diff(_log(value * units + 1.0), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core80_2nd_v081_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(value, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core81_2nd_v082_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core82_2nd_v083_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(_safe_div(value, units), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core83_2nd_v084_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(_log(value + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core84_2nd_v085_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(_log(units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core85_2nd_v086_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(value.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core86_2nd_v087_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(units.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core87_2nd_v088_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(_safe_div(units, value), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core88_2nd_v089_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(value * units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core89_2nd_v090_signal(investorname, value, units, securitytype):
    return _clean(_mean(_slope(_log(value * units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core90_2nd_v091_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(value, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core91_2nd_v092_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core92_2nd_v093_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(_safe_div(value, units), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core93_2nd_v094_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(_log(value + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core94_2nd_v095_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(_log(units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core95_2nd_v096_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(value.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core96_2nd_v097_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(units.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core97_2nd_v098_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(_safe_div(units, value), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core98_2nd_v099_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(value * units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core99_2nd_v100_signal(investorname, value, units, securitytype):
    return _clean(_mean(_diff(_log(value * units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core100_2nd_v101_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(value, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core101_2nd_v102_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core102_2nd_v103_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_safe_div(value, units), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core103_2nd_v104_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_log(value + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core104_2nd_v105_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_log(units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core105_2nd_v106_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(value.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core106_2nd_v107_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(units.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core107_2nd_v108_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_safe_div(units, value), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core108_2nd_v109_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(value * units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core109_2nd_v110_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_log(value * units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core110_2nd_v111_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(value, 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core111_2nd_v112_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(units, 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core112_2nd_v113_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_safe_div(value, units), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core113_2nd_v114_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_log(value + 1.0), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core114_2nd_v115_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_log(units + 1.0), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core115_2nd_v116_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(value.abs(), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core116_2nd_v117_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(units.abs(), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core117_2nd_v118_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_safe_div(units, value), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core118_2nd_v119_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(value * units, 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core119_2nd_v120_signal(investorname, value, units, securitytype):
    return _clean(_slope(_mean(_log(value * units + 1.0), 8), 8))
def cg_f097_specialist_and_quality_fund_exposure_core120_2nd_v121_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(value, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core121_2nd_v122_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core122_2nd_v123_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(_safe_div(value, units), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core123_2nd_v124_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(_log(value + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core124_2nd_v125_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(_log(units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core125_2nd_v126_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(value.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core126_2nd_v127_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(units.abs(), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core127_2nd_v128_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(_safe_div(units, value), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core128_2nd_v129_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(value * units, 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core129_2nd_v130_signal(investorname, value, units, securitytype):
    return _clean(_diff(_mean(_log(value * units + 1.0), 4), 4))
def cg_f097_specialist_and_quality_fund_exposure_core130_2nd_v131_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(value, 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core131_2nd_v132_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(units, 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core132_2nd_v133_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(_safe_div(value, units), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core133_2nd_v134_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(_log(value + 1.0), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core134_2nd_v135_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(_log(units + 1.0), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core135_2nd_v136_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(value.abs(), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core136_2nd_v137_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(units.abs(), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core137_2nd_v138_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(_safe_div(units, value), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core138_2nd_v139_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(value * units, 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core139_2nd_v140_signal(investorname, value, units, securitytype):
    return _clean(_z(_diff(_mean(_log(value * units + 1.0), 4), 4), 8))
def cg_f097_specialist_and_quality_fund_exposure_core140_2nd_v141_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(value, 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core141_2nd_v142_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(units, 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core142_2nd_v143_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(_safe_div(value, units), 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core143_2nd_v144_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(_log(value + 1.0), 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core144_2nd_v145_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(_log(units + 1.0), 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core145_2nd_v146_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(value.abs(), 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core146_2nd_v147_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(units.abs(), 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core147_2nd_v148_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(_safe_div(units, value), 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core148_2nd_v149_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(value * units, 4), 4), 12))
def cg_f097_specialist_and_quality_fund_exposure_core149_2nd_v150_signal(investorname, value, units, securitytype):
    return _clean(_rank(_slope(_mean(_log(value * units + 1.0), 4), 4), 12))