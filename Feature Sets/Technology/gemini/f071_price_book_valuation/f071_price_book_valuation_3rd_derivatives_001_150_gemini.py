import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f071_price_book_valuation_core00_3rd_v001_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(marketcap, 4), 4))
def cg_f071_price_book_valuation_core01_3rd_v002_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(equity, 4), 4))
def cg_f071_price_book_valuation_core02_3rd_v003_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(bvps, 4), 4))
def cg_f071_price_book_valuation_core03_3rd_v004_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(tbvps, 4), 4))
def cg_f071_price_book_valuation_core04_3rd_v005_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_safe_div(marketcap, equity), 4), 4))
def cg_f071_price_book_valuation_core05_3rd_v006_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4))
def cg_f071_price_book_valuation_core06_3rd_v007_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4))
def cg_f071_price_book_valuation_core07_3rd_v008_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(marketcap - equity, 4), 4))
def cg_f071_price_book_valuation_core08_3rd_v009_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4))
def cg_f071_price_book_valuation_core09_3rd_v010_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4))
def cg_f071_price_book_valuation_core10_3rd_v011_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(marketcap, 4), 8))
def cg_f071_price_book_valuation_core11_3rd_v012_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(equity, 4), 8))
def cg_f071_price_book_valuation_core12_3rd_v013_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(bvps, 4), 8))
def cg_f071_price_book_valuation_core13_3rd_v014_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(tbvps, 4), 8))
def cg_f071_price_book_valuation_core14_3rd_v015_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_safe_div(marketcap, equity), 4), 8))
def cg_f071_price_book_valuation_core15_3rd_v016_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_safe_div(marketcap, tbvps), 4), 8))
def cg_f071_price_book_valuation_core16_3rd_v017_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 8))
def cg_f071_price_book_valuation_core17_3rd_v018_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(marketcap - equity, 4), 8))
def cg_f071_price_book_valuation_core18_3rd_v019_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 8))
def cg_f071_price_book_valuation_core19_3rd_v020_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 8))
def cg_f071_price_book_valuation_core20_3rd_v021_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(marketcap, 4), 4))
def cg_f071_price_book_valuation_core21_3rd_v022_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(equity, 4), 4))
def cg_f071_price_book_valuation_core22_3rd_v023_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(bvps, 4), 4))
def cg_f071_price_book_valuation_core23_3rd_v024_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(tbvps, 4), 4))
def cg_f071_price_book_valuation_core24_3rd_v025_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(_safe_div(marketcap, equity), 4), 4))
def cg_f071_price_book_valuation_core25_3rd_v026_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(_safe_div(marketcap, tbvps), 4), 4))
def cg_f071_price_book_valuation_core26_3rd_v027_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4), 4))
def cg_f071_price_book_valuation_core27_3rd_v028_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(marketcap - equity, 4), 4))
def cg_f071_price_book_valuation_core28_3rd_v029_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4))
def cg_f071_price_book_valuation_core29_3rd_v030_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_slope(_safe_div(equity, marketcap.abs() + 1.0), 4), 4))
def cg_f071_price_book_valuation_core30_3rd_v031_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(marketcap, 4), 4), 8))
def cg_f071_price_book_valuation_core31_3rd_v032_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(equity, 4), 4), 8))
def cg_f071_price_book_valuation_core32_3rd_v033_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(bvps, 4), 4), 8))
def cg_f071_price_book_valuation_core33_3rd_v034_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(tbvps, 4), 4), 8))
def cg_f071_price_book_valuation_core34_3rd_v035_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(_safe_div(marketcap, equity), 4), 4), 8))
def cg_f071_price_book_valuation_core35_3rd_v036_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4), 8))
def cg_f071_price_book_valuation_core36_3rd_v037_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 8))
def cg_f071_price_book_valuation_core37_3rd_v038_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(marketcap - equity, 4), 4), 8))
def cg_f071_price_book_valuation_core38_3rd_v039_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 8))
def cg_f071_price_book_valuation_core39_3rd_v040_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f071_price_book_valuation_core40_3rd_v041_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(marketcap, 4), 8), 12))
def cg_f071_price_book_valuation_core41_3rd_v042_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(equity, 4), 8), 12))
def cg_f071_price_book_valuation_core42_3rd_v043_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(bvps, 4), 8), 12))
def cg_f071_price_book_valuation_core43_3rd_v044_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(tbvps, 4), 8), 12))
def cg_f071_price_book_valuation_core44_3rd_v045_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_safe_div(marketcap, equity), 4), 8), 12))
def cg_f071_price_book_valuation_core45_3rd_v046_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_safe_div(marketcap, tbvps), 4), 8), 12))
def cg_f071_price_book_valuation_core46_3rd_v047_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 8), 12))
def cg_f071_price_book_valuation_core47_3rd_v048_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(marketcap - equity, 4), 8), 12))
def cg_f071_price_book_valuation_core48_3rd_v049_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 8), 12))
def cg_f071_price_book_valuation_core49_3rd_v050_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f071_price_book_valuation_core50_3rd_v051_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(marketcap, 4), 4), 8))
def cg_f071_price_book_valuation_core51_3rd_v052_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(equity, 4), 4), 8))
def cg_f071_price_book_valuation_core52_3rd_v053_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(bvps, 4), 4), 8))
def cg_f071_price_book_valuation_core53_3rd_v054_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(tbvps, 4), 4), 8))
def cg_f071_price_book_valuation_core54_3rd_v055_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(_safe_div(marketcap, equity), 4), 4), 8))
def cg_f071_price_book_valuation_core55_3rd_v056_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(_safe_div(marketcap, tbvps), 4), 4), 8))
def cg_f071_price_book_valuation_core56_3rd_v057_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 8))
def cg_f071_price_book_valuation_core57_3rd_v058_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(marketcap - equity, 4), 4), 8))
def cg_f071_price_book_valuation_core58_3rd_v059_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 8))
def cg_f071_price_book_valuation_core59_3rd_v060_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_diff(_slope(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 8))
def cg_f071_price_book_valuation_core60_3rd_v061_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(marketcap, 4), 4), 12))
def cg_f071_price_book_valuation_core61_3rd_v062_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(equity, 4), 4), 12))
def cg_f071_price_book_valuation_core62_3rd_v063_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(bvps, 4), 4), 12))
def cg_f071_price_book_valuation_core63_3rd_v064_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(tbvps, 4), 4), 12))
def cg_f071_price_book_valuation_core64_3rd_v065_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(_safe_div(marketcap, equity), 4), 4), 12))
def cg_f071_price_book_valuation_core65_3rd_v066_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4), 12))
def cg_f071_price_book_valuation_core66_3rd_v067_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 12))
def cg_f071_price_book_valuation_core67_3rd_v068_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(marketcap - equity, 4), 4), 12))
def cg_f071_price_book_valuation_core68_3rd_v069_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 12))
def cg_f071_price_book_valuation_core69_3rd_v070_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f071_price_book_valuation_core70_3rd_v071_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(marketcap, 4), 8), 12))
def cg_f071_price_book_valuation_core71_3rd_v072_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(equity, 4), 8), 12))
def cg_f071_price_book_valuation_core72_3rd_v073_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(bvps, 4), 8), 12))
def cg_f071_price_book_valuation_core73_3rd_v074_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(tbvps, 4), 8), 12))
def cg_f071_price_book_valuation_core74_3rd_v075_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(_safe_div(marketcap, equity), 4), 8), 12))
def cg_f071_price_book_valuation_core75_3rd_v076_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(_safe_div(marketcap, tbvps), 4), 8), 12))
def cg_f071_price_book_valuation_core76_3rd_v077_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 8), 12))
def cg_f071_price_book_valuation_core77_3rd_v078_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(marketcap - equity, 4), 8), 12))
def cg_f071_price_book_valuation_core78_3rd_v079_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 8), 12))
def cg_f071_price_book_valuation_core79_3rd_v080_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_slope(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 8), 12))
def cg_f071_price_book_valuation_core80_3rd_v081_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(marketcap, 4), 4), 12))
def cg_f071_price_book_valuation_core81_3rd_v082_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(equity, 4), 4), 12))
def cg_f071_price_book_valuation_core82_3rd_v083_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(bvps, 4), 4), 12))
def cg_f071_price_book_valuation_core83_3rd_v084_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(tbvps, 4), 4), 12))
def cg_f071_price_book_valuation_core84_3rd_v085_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(_safe_div(marketcap, equity), 4), 4), 12))
def cg_f071_price_book_valuation_core85_3rd_v086_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(_safe_div(marketcap, tbvps), 4), 4), 12))
def cg_f071_price_book_valuation_core86_3rd_v087_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 12))
def cg_f071_price_book_valuation_core87_3rd_v088_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(marketcap - equity, 4), 4), 12))
def cg_f071_price_book_valuation_core88_3rd_v089_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 12))
def cg_f071_price_book_valuation_core89_3rd_v090_signal(marketcap, equity, bvps, tbvps):
    return _clean(_rank(_diff(_slope(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 12))
def cg_f071_price_book_valuation_core90_3rd_v091_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(marketcap, 4), 4), 4))
def cg_f071_price_book_valuation_core91_3rd_v092_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(equity, 4), 4), 4))
def cg_f071_price_book_valuation_core92_3rd_v093_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(bvps, 4), 4), 4))
def cg_f071_price_book_valuation_core93_3rd_v094_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(tbvps, 4), 4), 4))
def cg_f071_price_book_valuation_core94_3rd_v095_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(_safe_div(marketcap, equity), 4), 4), 4))
def cg_f071_price_book_valuation_core95_3rd_v096_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4), 4))
def cg_f071_price_book_valuation_core96_3rd_v097_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core97_3rd_v098_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(marketcap - equity, 4), 4), 4))
def cg_f071_price_book_valuation_core98_3rd_v099_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 4))
def cg_f071_price_book_valuation_core99_3rd_v100_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core100_3rd_v101_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(marketcap, 4), 8), 4))
def cg_f071_price_book_valuation_core101_3rd_v102_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(equity, 4), 8), 4))
def cg_f071_price_book_valuation_core102_3rd_v103_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(bvps, 4), 8), 4))
def cg_f071_price_book_valuation_core103_3rd_v104_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(tbvps, 4), 8), 4))
def cg_f071_price_book_valuation_core104_3rd_v105_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(_safe_div(marketcap, equity), 4), 8), 4))
def cg_f071_price_book_valuation_core105_3rd_v106_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(_safe_div(marketcap, tbvps), 4), 8), 4))
def cg_f071_price_book_valuation_core106_3rd_v107_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 8), 4))
def cg_f071_price_book_valuation_core107_3rd_v108_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(marketcap - equity, 4), 8), 4))
def cg_f071_price_book_valuation_core108_3rd_v109_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 8), 4))
def cg_f071_price_book_valuation_core109_3rd_v110_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_slope(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 8), 4))
def cg_f071_price_book_valuation_core110_3rd_v111_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(marketcap, 4), 4), 4))
def cg_f071_price_book_valuation_core111_3rd_v112_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(equity, 4), 4), 4))
def cg_f071_price_book_valuation_core112_3rd_v113_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(bvps, 4), 4), 4))
def cg_f071_price_book_valuation_core113_3rd_v114_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(tbvps, 4), 4), 4))
def cg_f071_price_book_valuation_core114_3rd_v115_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(_safe_div(marketcap, equity), 4), 4), 4))
def cg_f071_price_book_valuation_core115_3rd_v116_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(_safe_div(marketcap, tbvps), 4), 4), 4))
def cg_f071_price_book_valuation_core116_3rd_v117_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core117_3rd_v118_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(marketcap - equity, 4), 4), 4))
def cg_f071_price_book_valuation_core118_3rd_v119_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 4))
def cg_f071_price_book_valuation_core119_3rd_v120_signal(marketcap, equity, bvps, tbvps):
    return _clean(_mean(_diff(_slope(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core120_3rd_v121_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(marketcap, 4), 4), 4))
def cg_f071_price_book_valuation_core121_3rd_v122_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(equity, 4), 4), 4))
def cg_f071_price_book_valuation_core122_3rd_v123_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(bvps, 4), 4), 4))
def cg_f071_price_book_valuation_core123_3rd_v124_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(tbvps, 4), 4), 4))
def cg_f071_price_book_valuation_core124_3rd_v125_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(_safe_div(marketcap, equity), 4), 4), 4))
def cg_f071_price_book_valuation_core125_3rd_v126_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4), 4))
def cg_f071_price_book_valuation_core126_3rd_v127_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core127_3rd_v128_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(marketcap - equity, 4), 4), 4))
def cg_f071_price_book_valuation_core128_3rd_v129_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 4))
def cg_f071_price_book_valuation_core129_3rd_v130_signal(marketcap, equity, bvps, tbvps):
    return _clean(_slope(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core130_3rd_v131_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(marketcap, 4), 4), 4))
def cg_f071_price_book_valuation_core131_3rd_v132_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(equity, 4), 4), 4))
def cg_f071_price_book_valuation_core132_3rd_v133_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(bvps, 4), 4), 4))
def cg_f071_price_book_valuation_core133_3rd_v134_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(tbvps, 4), 4), 4))
def cg_f071_price_book_valuation_core134_3rd_v135_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(_safe_div(marketcap, equity), 4), 4), 4))
def cg_f071_price_book_valuation_core135_3rd_v136_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4), 4))
def cg_f071_price_book_valuation_core136_3rd_v137_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core137_3rd_v138_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(marketcap - equity, 4), 4), 4))
def cg_f071_price_book_valuation_core138_3rd_v139_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 4))
def cg_f071_price_book_valuation_core139_3rd_v140_signal(marketcap, equity, bvps, tbvps):
    return _clean(_diff(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 4))
def cg_f071_price_book_valuation_core140_3rd_v141_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(marketcap, 4), 4), 4), 8))
def cg_f071_price_book_valuation_core141_3rd_v142_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(equity, 4), 4), 4), 8))
def cg_f071_price_book_valuation_core142_3rd_v143_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(bvps, 4), 4), 4), 8))
def cg_f071_price_book_valuation_core143_3rd_v144_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(tbvps, 4), 4), 4), 8))
def cg_f071_price_book_valuation_core144_3rd_v145_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(marketcap, equity), 4), 4), 4), 8))
def cg_f071_price_book_valuation_core145_3rd_v146_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(marketcap, tbvps), 4), 4), 4), 8))
def cg_f071_price_book_valuation_core146_3rd_v147_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(marketcap, equity.abs() + 1.0), 4), 4), 4), 8))
def cg_f071_price_book_valuation_core147_3rd_v148_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(marketcap - equity, 4), 4), 4), 8))
def cg_f071_price_book_valuation_core148_3rd_v149_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(bvps, tbvps.abs() + 0.01), 4), 4), 4), 8))
def cg_f071_price_book_valuation_core149_3rd_v150_signal(marketcap, equity, bvps, tbvps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(equity, marketcap.abs() + 1.0), 4), 4), 4), 8))