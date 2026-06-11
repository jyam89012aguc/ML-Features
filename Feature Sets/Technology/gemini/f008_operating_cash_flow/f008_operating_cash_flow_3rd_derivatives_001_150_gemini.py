import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f008_operating_cash_flow_core00_3rd_v001_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(ncfo, 4), 4))
def cg_f008_operating_cash_flow_core01_3rd_v002_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(cashneq, 4), 4))
def cg_f008_operating_cash_flow_core02_3rd_v003_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(assets, 4), 4))
def cg_f008_operating_cash_flow_core03_3rd_v004_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_safe_div(ncfo, assets), 4), 4))
def cg_f008_operating_cash_flow_core04_3rd_v005_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4))
def cg_f008_operating_cash_flow_core05_3rd_v006_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_safe_div(cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core06_3rd_v007_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(ncfo - cashneq, 4), 4))
def cg_f008_operating_cash_flow_core07_3rd_v008_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core08_3rd_v009_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core09_3rd_v010_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_log(assets.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core10_3rd_v011_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(ncfo, 4), 8))
def cg_f008_operating_cash_flow_core11_3rd_v012_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(cashneq, 4), 8))
def cg_f008_operating_cash_flow_core12_3rd_v013_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(assets, 4), 8))
def cg_f008_operating_cash_flow_core13_3rd_v014_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_safe_div(ncfo, assets), 4), 8))
def cg_f008_operating_cash_flow_core14_3rd_v015_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_safe_div(ncfo, cashneq), 4), 8))
def cg_f008_operating_cash_flow_core15_3rd_v016_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_safe_div(cashneq, assets), 4), 8))
def cg_f008_operating_cash_flow_core16_3rd_v017_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(ncfo - cashneq, 4), 8))
def cg_f008_operating_cash_flow_core17_3rd_v018_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_safe_div(ncfo - cashneq, assets), 4), 8))
def cg_f008_operating_cash_flow_core18_3rd_v019_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8))
def cg_f008_operating_cash_flow_core19_3rd_v020_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_log(assets.abs() + 1.0), 4), 8))
def cg_f008_operating_cash_flow_core20_3rd_v021_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(ncfo, 4), 4))
def cg_f008_operating_cash_flow_core21_3rd_v022_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(cashneq, 4), 4))
def cg_f008_operating_cash_flow_core22_3rd_v023_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(assets, 4), 4))
def cg_f008_operating_cash_flow_core23_3rd_v024_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(_safe_div(ncfo, assets), 4), 4))
def cg_f008_operating_cash_flow_core24_3rd_v025_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(_safe_div(ncfo, cashneq), 4), 4))
def cg_f008_operating_cash_flow_core25_3rd_v026_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(_safe_div(cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core26_3rd_v027_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(ncfo - cashneq, 4), 4))
def cg_f008_operating_cash_flow_core27_3rd_v028_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(_safe_div(ncfo - cashneq, assets), 4), 4))
def cg_f008_operating_cash_flow_core28_3rd_v029_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core29_3rd_v030_signal(ncfo, cashneq, assets):
    return _clean(_diff(_slope(_log(assets.abs() + 1.0), 4), 4))
def cg_f008_operating_cash_flow_core30_3rd_v031_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(ncfo, 4), 4), 8))
def cg_f008_operating_cash_flow_core31_3rd_v032_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(cashneq, 4), 4), 8))
def cg_f008_operating_cash_flow_core32_3rd_v033_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(assets, 4), 4), 8))
def cg_f008_operating_cash_flow_core33_3rd_v034_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core34_3rd_v035_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4), 8))
def cg_f008_operating_cash_flow_core35_3rd_v036_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core36_3rd_v037_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(ncfo - cashneq, 4), 4), 8))
def cg_f008_operating_cash_flow_core37_3rd_v038_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core38_3rd_v039_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 8))
def cg_f008_operating_cash_flow_core39_3rd_v040_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_diff(_log(assets.abs() + 1.0), 4), 4), 8))
def cg_f008_operating_cash_flow_core40_3rd_v041_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(ncfo, 4), 8), 12))
def cg_f008_operating_cash_flow_core41_3rd_v042_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(cashneq, 4), 8), 12))
def cg_f008_operating_cash_flow_core42_3rd_v043_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(assets, 4), 8), 12))
def cg_f008_operating_cash_flow_core43_3rd_v044_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, assets), 4), 8), 12))
def cg_f008_operating_cash_flow_core44_3rd_v045_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_safe_div(ncfo, cashneq), 4), 8), 12))
def cg_f008_operating_cash_flow_core45_3rd_v046_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_safe_div(cashneq, assets), 4), 8), 12))
def cg_f008_operating_cash_flow_core46_3rd_v047_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(ncfo - cashneq, 4), 8), 12))
def cg_f008_operating_cash_flow_core47_3rd_v048_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_safe_div(ncfo - cashneq, assets), 4), 8), 12))
def cg_f008_operating_cash_flow_core48_3rd_v049_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8), 12))
def cg_f008_operating_cash_flow_core49_3rd_v050_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_log(assets.abs() + 1.0), 4), 8), 12))
def cg_f008_operating_cash_flow_core50_3rd_v051_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(ncfo, 4), 4), 8))
def cg_f008_operating_cash_flow_core51_3rd_v052_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(cashneq, 4), 4), 8))
def cg_f008_operating_cash_flow_core52_3rd_v053_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(assets, 4), 4), 8))
def cg_f008_operating_cash_flow_core53_3rd_v054_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core54_3rd_v055_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(_safe_div(ncfo, cashneq), 4), 4), 8))
def cg_f008_operating_cash_flow_core55_3rd_v056_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(_safe_div(cashneq, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core56_3rd_v057_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(ncfo - cashneq, 4), 4), 8))
def cg_f008_operating_cash_flow_core57_3rd_v058_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(_safe_div(ncfo - cashneq, assets), 4), 4), 8))
def cg_f008_operating_cash_flow_core58_3rd_v059_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4), 8))
def cg_f008_operating_cash_flow_core59_3rd_v060_signal(ncfo, cashneq, assets):
    return _clean(_z(_diff(_slope(_log(assets.abs() + 1.0), 4), 4), 8))
def cg_f008_operating_cash_flow_core60_3rd_v061_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(ncfo, 4), 4), 12))
def cg_f008_operating_cash_flow_core61_3rd_v062_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(cashneq, 4), 4), 12))
def cg_f008_operating_cash_flow_core62_3rd_v063_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(assets, 4), 4), 12))
def cg_f008_operating_cash_flow_core63_3rd_v064_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core64_3rd_v065_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4), 12))
def cg_f008_operating_cash_flow_core65_3rd_v066_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core66_3rd_v067_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(ncfo - cashneq, 4), 4), 12))
def cg_f008_operating_cash_flow_core67_3rd_v068_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core68_3rd_v069_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 12))
def cg_f008_operating_cash_flow_core69_3rd_v070_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_diff(_log(assets.abs() + 1.0), 4), 4), 12))
def cg_f008_operating_cash_flow_core70_3rd_v071_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(ncfo, 4), 8), 12))
def cg_f008_operating_cash_flow_core71_3rd_v072_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(cashneq, 4), 8), 12))
def cg_f008_operating_cash_flow_core72_3rd_v073_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(assets, 4), 8), 12))
def cg_f008_operating_cash_flow_core73_3rd_v074_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, assets), 4), 8), 12))
def cg_f008_operating_cash_flow_core74_3rd_v075_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo, cashneq), 4), 8), 12))
def cg_f008_operating_cash_flow_core75_3rd_v076_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(_safe_div(cashneq, assets), 4), 8), 12))
def cg_f008_operating_cash_flow_core76_3rd_v077_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(ncfo - cashneq, 4), 8), 12))
def cg_f008_operating_cash_flow_core77_3rd_v078_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(_safe_div(ncfo - cashneq, assets), 4), 8), 12))
def cg_f008_operating_cash_flow_core78_3rd_v079_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8), 12))
def cg_f008_operating_cash_flow_core79_3rd_v080_signal(ncfo, cashneq, assets):
    return _clean(_rank(_slope(_diff(_log(assets.abs() + 1.0), 4), 8), 12))
def cg_f008_operating_cash_flow_core80_3rd_v081_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(ncfo, 4), 4), 12))
def cg_f008_operating_cash_flow_core81_3rd_v082_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(cashneq, 4), 4), 12))
def cg_f008_operating_cash_flow_core82_3rd_v083_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(assets, 4), 4), 12))
def cg_f008_operating_cash_flow_core83_3rd_v084_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core84_3rd_v085_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo, cashneq), 4), 4), 12))
def cg_f008_operating_cash_flow_core85_3rd_v086_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(_safe_div(cashneq, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core86_3rd_v087_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(ncfo - cashneq, 4), 4), 12))
def cg_f008_operating_cash_flow_core87_3rd_v088_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(_safe_div(ncfo - cashneq, assets), 4), 4), 12))
def cg_f008_operating_cash_flow_core88_3rd_v089_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4), 12))
def cg_f008_operating_cash_flow_core89_3rd_v090_signal(ncfo, cashneq, assets):
    return _clean(_rank(_diff(_slope(_log(assets.abs() + 1.0), 4), 4), 12))
def cg_f008_operating_cash_flow_core90_3rd_v091_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(ncfo, 4), 4), 4))
def cg_f008_operating_cash_flow_core91_3rd_v092_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core92_3rd_v093_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(assets, 4), 4), 4))
def cg_f008_operating_cash_flow_core93_3rd_v094_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core94_3rd_v095_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4), 4))
def cg_f008_operating_cash_flow_core95_3rd_v096_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core96_3rd_v097_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(ncfo - cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core97_3rd_v098_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core98_3rd_v099_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core99_3rd_v100_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_diff(_log(assets.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core100_3rd_v101_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(ncfo, 4), 8), 4))
def cg_f008_operating_cash_flow_core101_3rd_v102_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(cashneq, 4), 8), 4))
def cg_f008_operating_cash_flow_core102_3rd_v103_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(assets, 4), 8), 4))
def cg_f008_operating_cash_flow_core103_3rd_v104_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, assets), 4), 8), 4))
def cg_f008_operating_cash_flow_core104_3rd_v105_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo, cashneq), 4), 8), 4))
def cg_f008_operating_cash_flow_core105_3rd_v106_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(_safe_div(cashneq, assets), 4), 8), 4))
def cg_f008_operating_cash_flow_core106_3rd_v107_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(ncfo - cashneq, 4), 8), 4))
def cg_f008_operating_cash_flow_core107_3rd_v108_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(_safe_div(ncfo - cashneq, assets), 4), 8), 4))
def cg_f008_operating_cash_flow_core108_3rd_v109_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(_log(ncfo.abs() + 1.0), 4), 8), 4))
def cg_f008_operating_cash_flow_core109_3rd_v110_signal(ncfo, cashneq, assets):
    return _clean(_mean(_slope(_diff(_log(assets.abs() + 1.0), 4), 8), 4))
def cg_f008_operating_cash_flow_core110_3rd_v111_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(ncfo, 4), 4), 4))
def cg_f008_operating_cash_flow_core111_3rd_v112_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core112_3rd_v113_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(assets, 4), 4), 4))
def cg_f008_operating_cash_flow_core113_3rd_v114_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core114_3rd_v115_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo, cashneq), 4), 4), 4))
def cg_f008_operating_cash_flow_core115_3rd_v116_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core116_3rd_v117_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(ncfo - cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core117_3rd_v118_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(_safe_div(ncfo - cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core118_3rd_v119_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core119_3rd_v120_signal(ncfo, cashneq, assets):
    return _clean(_mean(_diff(_slope(_log(assets.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core120_3rd_v121_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(ncfo, 4), 4), 4))
def cg_f008_operating_cash_flow_core121_3rd_v122_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core122_3rd_v123_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(assets, 4), 4), 4))
def cg_f008_operating_cash_flow_core123_3rd_v124_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core124_3rd_v125_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4), 4))
def cg_f008_operating_cash_flow_core125_3rd_v126_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core126_3rd_v127_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(ncfo - cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core127_3rd_v128_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core128_3rd_v129_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core129_3rd_v130_signal(ncfo, cashneq, assets):
    return _clean(_slope(_diff(_diff(_log(assets.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core130_3rd_v131_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(ncfo, 4), 4), 4))
def cg_f008_operating_cash_flow_core131_3rd_v132_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core132_3rd_v133_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(assets, 4), 4), 4))
def cg_f008_operating_cash_flow_core133_3rd_v134_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core134_3rd_v135_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4), 4))
def cg_f008_operating_cash_flow_core135_3rd_v136_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core136_3rd_v137_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(ncfo - cashneq, 4), 4), 4))
def cg_f008_operating_cash_flow_core137_3rd_v138_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4), 4))
def cg_f008_operating_cash_flow_core138_3rd_v139_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core139_3rd_v140_signal(ncfo, cashneq, assets):
    return _clean(_diff(_diff(_diff(_log(assets.abs() + 1.0), 4), 4), 4))
def cg_f008_operating_cash_flow_core140_3rd_v141_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(ncfo, 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core141_3rd_v142_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(cashneq, 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core142_3rd_v143_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(assets, 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core143_3rd_v144_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, assets), 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core144_3rd_v145_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo, cashneq), 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core145_3rd_v146_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(cashneq, assets), 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core146_3rd_v147_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(ncfo - cashneq, 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core147_3rd_v148_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ncfo - cashneq, assets), 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core148_3rd_v149_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(_log(ncfo.abs() + 1.0), 4), 4), 4), 8))
def cg_f008_operating_cash_flow_core149_3rd_v150_signal(ncfo, cashneq, assets):
    return _clean(_z(_slope(_diff(_diff(_log(assets.abs() + 1.0), 4), 4), 4), 8))