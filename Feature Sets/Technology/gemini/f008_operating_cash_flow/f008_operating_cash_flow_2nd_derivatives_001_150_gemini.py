import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f008_operating_cash_flow_core00_2nd_v001_signal(ncfo, cashneq, assets):
    return _clean(_slope(ncfo, 4))
def cg_f008_operating_cash_flow_core01_2nd_v002_signal(ncfo, cashneq, assets):
    return _clean(_slope(cashneq, 4))
def cg_f008_operating_cash_flow_core02_2nd_v003_signal(ncfo, cashneq, assets):
    return _clean(_slope(assets, 4))
def cg_f008_operating_cash_flow_core03_2nd_v004_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(ncfo, assets), 4))
def cg_f008_operating_cash_flow_core04_2nd_v005_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(ncfo, cashneq), 4))
def cg_f008_operating_cash_flow_core05_2nd_v006_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(cashneq, assets), 4))
def cg_f008_operating_cash_flow_core06_2nd_v007_signal(ncfo, cashneq, assets):
    return _clean(_slope(ncfo - cashneq, 4))
def cg_f008_operating_cash_flow_core07_2nd_v008_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(ncfo - cashneq, assets), 4))
def cg_f008_operating_cash_flow_core08_2nd_v009_signal(ncfo, cashneq, assets):
    return _clean(_slope(_log(ncfo.abs() + 1.0), 4))
def cg_f008_operating_cash_flow_core09_2nd_v010_signal(ncfo, cashneq, assets):
    return _clean(_slope(_log(assets.abs() + 1.0), 4))
def cg_f008_operating_cash_flow_core10_2nd_v011_signal(ncfo, cashneq, assets):
    return _clean(_slope(ncfo, 8))
def cg_f008_operating_cash_flow_core11_2nd_v012_signal(ncfo, cashneq, assets):
    return _clean(_slope(cashneq, 8))
def cg_f008_operating_cash_flow_core12_2nd_v013_signal(ncfo, cashneq, assets):
    return _clean(_slope(assets, 8))
def cg_f008_operating_cash_flow_core13_2nd_v014_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(ncfo, assets), 8))
def cg_f008_operating_cash_flow_core14_2nd_v015_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(ncfo, cashneq), 8))
def cg_f008_operating_cash_flow_core15_2nd_v016_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(cashneq, assets), 8))
def cg_f008_operating_cash_flow_core16_2nd_v017_signal(ncfo, cashneq, assets):
    return _clean(_slope(ncfo - cashneq, 8))
def cg_f008_operating_cash_flow_core17_2nd_v018_signal(ncfo, cashneq, assets):
    return _clean(_slope(_safe_div(ncfo - cashneq, assets), 8))
def cg_f008_operating_cash_flow_core18_2nd_v019_signal(ncfo, cashneq, assets):
    return _clean(_slope(_log(ncfo.abs() + 1.0), 8))
def cg_f008_operating_cash_flow_core19_2nd_v020_signal(ncfo, cashneq, assets):
    return _clean(_slope(_log(assets.abs() + 1.0), 8))
def cg_f008_operating_cash_flow_core20_2nd_v021_signal(ncfo, cashneq, assets):
    return _clean(_diff(ncfo, 4))
def cg_f008_operating_cash_flow_core21_2nd_v022_signal(ncfo, cashneq, assets):
    return _clean(_diff(cashneq, 4))
def cg_f008_operating_cash_flow_core22_2nd_v023_signal(ncfo, cashneq, assets):
    return _clean(_diff(assets, 4))
def cg_f008_operating_cash_flow_core23_2nd_v024_signal(ncfo, cashneq, assets):
    return _clean(_diff(_safe_div(ncfo, assets), 4))
def cg_f008_operating_cash_flow_core24_2nd_v025_signal(ncfo, cashneq, assets):
    return _clean(_diff(_safe_div(ncfo, cashneq), 4))
def cg_f008_operating_cash_flow_core25_2nd_v026_signal(ncfo, cashneq, assets):
    return _clean(_diff(_safe_div(cashneq, assets), 4))
def cg_f008_operating_cash_flow_core26_2nd_v027_signal(ncfo, cashneq, assets):
    return _clean(_diff(ncfo - cashneq, 4))
def cg_f008_operating_cash_flow_core27_2nd_v028_signal(ncfo, cashneq, assets):
    return _clean(_diff(_safe_div(ncfo - cashneq, assets), 4))
def cg_f008_operating_cash_flow_core28_2nd_v029_signal(ncfo, cashneq, assets):
    return _clean(_diff(_log(ncfo.abs() + 1.0), 4))
def cg_f008_operating_cash_flow_core29_2nd_v030_signal(ncfo, cashneq, assets):
    return _clean(_diff(_log(assets.abs() + 1.0), 4))
def cg_f008_operating_cash_flow_core30_2nd_v031_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(ncfo, 4), 8))
def cg_f008_operating_cash_flow_core31_2nd_v032_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(cashneq, 4), 8))
def cg_f008_operating_cash_flow_core32_2nd_v033_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(assets, 4), 8))
def cg_f008_operating_cash_flow_core33_2nd_v034_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(ncfo, assets), 4), 8))
def cg_f008_operating_cash_flow_core34_2nd_v035_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(ncfo, cashneq), 4), 8))
def cg_f008_operating_cash_flow_core35_2nd_v036_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(cashneq, assets), 4), 8))
def cg_f008_operating_cash_flow_core36_2nd_v037_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(ncfo - cashneq, 4), 8))
def cg_f008_operating_cash_flow_core37_2nd_v038_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(ncfo - cashneq, assets), 4), 8))
def cg_f008_operating_cash_flow_core38_2nd_v039_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_log(ncfo.abs() + 1.0), 4), 8))
def cg_f008_operating_cash_flow_core39_2nd_v040_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_log(assets.abs() + 1.0), 4), 8))
def cg_f008_operating_cash_flow_core40_2nd_v041_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(ncfo, 8), 12))
def cg_f008_operating_cash_flow_core41_2nd_v042_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(cashneq, 8), 12))
def cg_f008_operating_cash_flow_core42_2nd_v043_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(assets, 8), 12))
def cg_f008_operating_cash_flow_core43_2nd_v044_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(ncfo, assets), 8), 12))
def cg_f008_operating_cash_flow_core44_2nd_v045_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(ncfo, cashneq), 8), 12))
def cg_f008_operating_cash_flow_core45_2nd_v046_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(cashneq, assets), 8), 12))
def cg_f008_operating_cash_flow_core46_2nd_v047_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(ncfo - cashneq, 8), 12))
def cg_f008_operating_cash_flow_core47_2nd_v048_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_safe_div(ncfo - cashneq, assets), 8), 12))
def cg_f008_operating_cash_flow_core48_2nd_v049_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_log(ncfo.abs() + 1.0), 8), 12))
def cg_f008_operating_cash_flow_core49_2nd_v050_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_log(assets.abs() + 1.0), 8), 12))
def cg_f008_operating_cash_flow_core50_2nd_v051_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(ncfo, 4), 8))
def cg_f008_operating_cash_flow_core51_2nd_v052_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(cashneq, 4), 8))
def cg_f008_operating_cash_flow_core52_2nd_v053_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(assets, 4), 8))
def cg_f008_operating_cash_flow_core53_2nd_v054_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_safe_div(ncfo, assets), 4), 8))
def cg_f008_operating_cash_flow_core54_2nd_v055_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_safe_div(ncfo, cashneq), 4), 8))
def cg_f008_operating_cash_flow_core55_2nd_v056_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_safe_div(cashneq, assets), 4), 8))
def cg_f008_operating_cash_flow_core56_2nd_v057_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(ncfo - cashneq, 4), 8))
def cg_f008_operating_cash_flow_core57_2nd_v058_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_safe_div(ncfo - cashneq, assets), 4), 8))
def cg_f008_operating_cash_flow_core58_2nd_v059_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_log(ncfo.abs() + 1.0), 4), 8))
def cg_f008_operating_cash_flow_core59_2nd_v060_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_log(assets.abs() + 1.0), 4), 8))
def cg_f008_operating_cash_flow_core60_2nd_v061_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(ncfo, 4), 12))
def cg_f008_operating_cash_flow_core61_2nd_v062_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(cashneq, 4), 12))
def cg_f008_operating_cash_flow_core62_2nd_v063_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(assets, 4), 12))
def cg_f008_operating_cash_flow_core63_2nd_v064_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(ncfo, assets), 4), 12))
def cg_f008_operating_cash_flow_core64_2nd_v065_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(ncfo, cashneq), 4), 12))
def cg_f008_operating_cash_flow_core65_2nd_v066_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(cashneq, assets), 4), 12))
def cg_f008_operating_cash_flow_core66_2nd_v067_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(ncfo - cashneq, 4), 12))
def cg_f008_operating_cash_flow_core67_2nd_v068_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_safe_div(ncfo - cashneq, assets), 4), 12))
def cg_f008_operating_cash_flow_core68_2nd_v069_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_log(ncfo.abs() + 1.0), 4), 12))
def cg_f008_operating_cash_flow_core69_2nd_v070_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_log(assets.abs() + 1.0), 4), 12))
def cg_f008_operating_cash_flow_core70_2nd_v071_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(ncfo, 4), 12))
def cg_f008_operating_cash_flow_core71_2nd_v072_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(cashneq, 4), 12))
def cg_f008_operating_cash_flow_core72_2nd_v073_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(assets, 4), 12))
def cg_f008_operating_cash_flow_core73_2nd_v074_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(ncfo, assets), 4), 12))
def cg_f008_operating_cash_flow_core74_2nd_v075_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(ncfo, cashneq), 4), 12))
def cg_f008_operating_cash_flow_core75_2nd_v076_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(cashneq, assets), 4), 12))
def cg_f008_operating_cash_flow_core76_2nd_v077_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(ncfo - cashneq, 4), 12))
def cg_f008_operating_cash_flow_core77_2nd_v078_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_safe_div(ncfo - cashneq, assets), 4), 12))
def cg_f008_operating_cash_flow_core78_2nd_v079_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_log(ncfo.abs() + 1.0), 4), 12))
def cg_f008_operating_cash_flow_core79_2nd_v080_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_log(assets.abs() + 1.0), 4), 12))
def cg_f008_operating_cash_flow_core80_2nd_v081_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(ncfo, 4), 4))
def cg_f008_operating_cash_flow_core81_2nd_v082_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(cashneq, 4), 4))
def cg_f008_operating_cash_flow_core82_2nd_v083_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(assets, 4), 4))
def cg_f008_operating_cash_flow_core83_2nd_v084_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(ncfo, assets), 4), 4))
def cg_f008_operating_cash_flow_core84_2nd_v085_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(ncfo, cashneq), 4), 4))
def cg_f008_operating_cash_flow_core85_2nd_v086_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core86_2nd_v087_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(ncfo - cashneq, 4), 4))
def cg_f008_operating_cash_flow_core87_2nd_v088_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_safe_div(ncfo - cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core88_2nd_v089_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core89_2nd_v090_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_log(assets.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core90_2nd_v091_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(ncfo, 4), 4))
def cg_f008_operating_cash_flow_core91_2nd_v092_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(cashneq, 4), 4))
def cg_f008_operating_cash_flow_core92_2nd_v093_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(assets, 4), 4))
def cg_f008_operating_cash_flow_core93_2nd_v094_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(ncfo, assets), 4), 4))
def cg_f008_operating_cash_flow_core94_2nd_v095_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(ncfo, cashneq), 4), 4))
def cg_f008_operating_cash_flow_core95_2nd_v096_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core96_2nd_v097_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(ncfo - cashneq, 4), 4))
def cg_f008_operating_cash_flow_core97_2nd_v098_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_safe_div(ncfo - cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core98_2nd_v099_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core99_2nd_v100_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_log(assets.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core100_2nd_v101_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(ncfo, 4), 4))
def cg_f008_operating_cash_flow_core101_2nd_v102_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(cashneq, 4), 4))
def cg_f008_operating_cash_flow_core102_2nd_v103_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(assets, 4), 4))
def cg_f008_operating_cash_flow_core103_2nd_v104_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(ncfo, assets), 4), 4))
def cg_f008_operating_cash_flow_core104_2nd_v105_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(ncfo, cashneq), 4), 4))
def cg_f008_operating_cash_flow_core105_2nd_v106_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core106_2nd_v107_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(ncfo - cashneq, 4), 4))
def cg_f008_operating_cash_flow_core107_2nd_v108_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(ncfo - cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core108_2nd_v109_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core109_2nd_v110_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_log(assets.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core110_2nd_v111_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(ncfo, 8), 8))
def cg_f008_operating_cash_flow_core111_2nd_v112_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(cashneq, 8), 8))
def cg_f008_operating_cash_flow_core112_2nd_v113_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(assets, 8), 8))
def cg_f008_operating_cash_flow_core113_2nd_v114_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(ncfo, assets), 8), 8))
def cg_f008_operating_cash_flow_core114_2nd_v115_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(ncfo, cashneq), 8), 8))
def cg_f008_operating_cash_flow_core115_2nd_v116_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(cashneq, assets), 8), 8))
def cg_f008_operating_cash_flow_core116_2nd_v117_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(ncfo - cashneq, 8), 8))
def cg_f008_operating_cash_flow_core117_2nd_v118_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_safe_div(ncfo - cashneq, assets), 8), 8))
def cg_f008_operating_cash_flow_core118_2nd_v119_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_log(ncfo.abs() + 1.0), 8), 8))
def cg_f008_operating_cash_flow_core119_2nd_v120_signal(ncfo, cashneq, assets):
    return _clean(_slope(_mean(_log(assets.abs() + 1.0), 8), 8))
def cg_f008_operating_cash_flow_core120_2nd_v121_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(ncfo, 4), 4))
def cg_f008_operating_cash_flow_core121_2nd_v122_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(cashneq, 4), 4))
def cg_f008_operating_cash_flow_core122_2nd_v123_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(assets, 4), 4))
def cg_f008_operating_cash_flow_core123_2nd_v124_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(ncfo, assets), 4), 4))
def cg_f008_operating_cash_flow_core124_2nd_v125_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(ncfo, cashneq), 4), 4))
def cg_f008_operating_cash_flow_core125_2nd_v126_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core126_2nd_v127_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(ncfo - cashneq, 4), 4))
def cg_f008_operating_cash_flow_core127_2nd_v128_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(_safe_div(ncfo - cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core128_2nd_v129_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core129_2nd_v130_signal(ncfo, cashneq, assets):
    return _clean(_diff(_mean(_log(assets.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core130_2nd_v131_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(ncfo, 4), 4), 8))
def cg_f008_operating_cash_flow_core131_2nd_v132_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(cashneq, 4), 4), 8))
def cg_f008_operating_cash_flow_core132_2nd_v133_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(assets, 4), 4), 8))
def cg_f008_operating_cash_flow_core133_2nd_v134_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core134_2nd_v135_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(ncfo, cashneq), 4), 4), 8))
def cg_f008_operating_cash_flow_core135_2nd_v136_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core136_2nd_v137_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(ncfo - cashneq, 4), 4), 8))
def cg_f008_operating_cash_flow_core137_2nd_v138_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(_safe_div(ncfo - cashneq, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core138_2nd_v139_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(_log(ncfo.abs() + 1.0), 4), 4), 8))
def cg_f008_operating_cash_flow_core139_2nd_v140_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_mean(_log(assets.abs() + 1.0), 4), 4), 8))
def cg_f008_operating_cash_flow_core140_2nd_v141_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(ncfo, 4), 4), 12))
def cg_f008_operating_cash_flow_core141_2nd_v142_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(cashneq, 4), 4), 12))
def cg_f008_operating_cash_flow_core142_2nd_v143_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(assets, 4), 4), 12))
def cg_f008_operating_cash_flow_core143_2nd_v144_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core144_2nd_v145_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo, cashneq), 4), 4), 12))
def cg_f008_operating_cash_flow_core145_2nd_v146_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core146_2nd_v147_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(ncfo - cashneq, 4), 4), 12))
def cg_f008_operating_cash_flow_core147_2nd_v148_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(_safe_div(ncfo - cashneq, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core148_2nd_v149_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(_log(ncfo.abs() + 1.0), 4), 4), 12))
def cg_f008_operating_cash_flow_core149_2nd_v150_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_mean(_log(assets.abs() + 1.0), 4), 4), 12))