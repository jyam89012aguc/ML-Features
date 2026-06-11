import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f086_daily_market_metrics_core00_3rd_v001_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(marketcap, 4), 4))
def cg_f086_daily_market_metrics_core01_3rd_v002_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(ev, 4), 4))
def cg_f086_daily_market_metrics_core02_3rd_v003_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(price, 4), 4))
def cg_f086_daily_market_metrics_core03_3rd_v004_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(pb, 4), 4))
def cg_f086_daily_market_metrics_core04_3rd_v005_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(pe, 4), 4))
def cg_f086_daily_market_metrics_core05_3rd_v006_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(ps, 4), 4))
def cg_f086_daily_market_metrics_core06_3rd_v007_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_safe_div(ev, marketcap), 4), 4))
def cg_f086_daily_market_metrics_core07_3rd_v008_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_safe_div(price, pb), 4), 4))
def cg_f086_daily_market_metrics_core08_3rd_v009_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_safe_div(price, pe), 4), 4))
def cg_f086_daily_market_metrics_core09_3rd_v010_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_safe_div(price, ps), 4), 4))
def cg_f086_daily_market_metrics_core10_3rd_v011_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(marketcap, 4), 8))
def cg_f086_daily_market_metrics_core11_3rd_v012_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(ev, 4), 8))
def cg_f086_daily_market_metrics_core12_3rd_v013_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(price, 4), 8))
def cg_f086_daily_market_metrics_core13_3rd_v014_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(pb, 4), 8))
def cg_f086_daily_market_metrics_core14_3rd_v015_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(pe, 4), 8))
def cg_f086_daily_market_metrics_core15_3rd_v016_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(ps, 4), 8))
def cg_f086_daily_market_metrics_core16_3rd_v017_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_safe_div(ev, marketcap), 4), 8))
def cg_f086_daily_market_metrics_core17_3rd_v018_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_safe_div(price, pb), 4), 8))
def cg_f086_daily_market_metrics_core18_3rd_v019_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_safe_div(price, pe), 4), 8))
def cg_f086_daily_market_metrics_core19_3rd_v020_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_safe_div(price, ps), 4), 8))
def cg_f086_daily_market_metrics_core20_3rd_v021_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(marketcap, 4), 4))
def cg_f086_daily_market_metrics_core21_3rd_v022_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(ev, 4), 4))
def cg_f086_daily_market_metrics_core22_3rd_v023_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(price, 4), 4))
def cg_f086_daily_market_metrics_core23_3rd_v024_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(pb, 4), 4))
def cg_f086_daily_market_metrics_core24_3rd_v025_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(pe, 4), 4))
def cg_f086_daily_market_metrics_core25_3rd_v026_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(ps, 4), 4))
def cg_f086_daily_market_metrics_core26_3rd_v027_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(_safe_div(ev, marketcap), 4), 4))
def cg_f086_daily_market_metrics_core27_3rd_v028_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(_safe_div(price, pb), 4), 4))
def cg_f086_daily_market_metrics_core28_3rd_v029_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(_safe_div(price, pe), 4), 4))
def cg_f086_daily_market_metrics_core29_3rd_v030_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_slope(_safe_div(price, ps), 4), 4))
def cg_f086_daily_market_metrics_core30_3rd_v031_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(marketcap, 4), 4), 8))
def cg_f086_daily_market_metrics_core31_3rd_v032_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(ev, 4), 4), 8))
def cg_f086_daily_market_metrics_core32_3rd_v033_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(price, 4), 4), 8))
def cg_f086_daily_market_metrics_core33_3rd_v034_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(pb, 4), 4), 8))
def cg_f086_daily_market_metrics_core34_3rd_v035_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(pe, 4), 4), 8))
def cg_f086_daily_market_metrics_core35_3rd_v036_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(ps, 4), 4), 8))
def cg_f086_daily_market_metrics_core36_3rd_v037_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(_safe_div(ev, marketcap), 4), 4), 8))
def cg_f086_daily_market_metrics_core37_3rd_v038_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(_safe_div(price, pb), 4), 4), 8))
def cg_f086_daily_market_metrics_core38_3rd_v039_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(_safe_div(price, pe), 4), 4), 8))
def cg_f086_daily_market_metrics_core39_3rd_v040_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_diff(_safe_div(price, ps), 4), 4), 8))
def cg_f086_daily_market_metrics_core40_3rd_v041_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(marketcap, 4), 8), 12))
def cg_f086_daily_market_metrics_core41_3rd_v042_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(ev, 4), 8), 12))
def cg_f086_daily_market_metrics_core42_3rd_v043_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(price, 4), 8), 12))
def cg_f086_daily_market_metrics_core43_3rd_v044_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(pb, 4), 8), 12))
def cg_f086_daily_market_metrics_core44_3rd_v045_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(pe, 4), 8), 12))
def cg_f086_daily_market_metrics_core45_3rd_v046_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(ps, 4), 8), 12))
def cg_f086_daily_market_metrics_core46_3rd_v047_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_safe_div(ev, marketcap), 4), 8), 12))
def cg_f086_daily_market_metrics_core47_3rd_v048_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_safe_div(price, pb), 4), 8), 12))
def cg_f086_daily_market_metrics_core48_3rd_v049_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_safe_div(price, pe), 4), 8), 12))
def cg_f086_daily_market_metrics_core49_3rd_v050_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_safe_div(price, ps), 4), 8), 12))
def cg_f086_daily_market_metrics_core50_3rd_v051_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(marketcap, 4), 4), 8))
def cg_f086_daily_market_metrics_core51_3rd_v052_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(ev, 4), 4), 8))
def cg_f086_daily_market_metrics_core52_3rd_v053_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(price, 4), 4), 8))
def cg_f086_daily_market_metrics_core53_3rd_v054_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(pb, 4), 4), 8))
def cg_f086_daily_market_metrics_core54_3rd_v055_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(pe, 4), 4), 8))
def cg_f086_daily_market_metrics_core55_3rd_v056_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(ps, 4), 4), 8))
def cg_f086_daily_market_metrics_core56_3rd_v057_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(_safe_div(ev, marketcap), 4), 4), 8))
def cg_f086_daily_market_metrics_core57_3rd_v058_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(_safe_div(price, pb), 4), 4), 8))
def cg_f086_daily_market_metrics_core58_3rd_v059_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(_safe_div(price, pe), 4), 4), 8))
def cg_f086_daily_market_metrics_core59_3rd_v060_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_slope(_safe_div(price, ps), 4), 4), 8))
def cg_f086_daily_market_metrics_core60_3rd_v061_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(marketcap, 4), 4), 12))
def cg_f086_daily_market_metrics_core61_3rd_v062_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(ev, 4), 4), 12))
def cg_f086_daily_market_metrics_core62_3rd_v063_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(price, 4), 4), 12))
def cg_f086_daily_market_metrics_core63_3rd_v064_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(pb, 4), 4), 12))
def cg_f086_daily_market_metrics_core64_3rd_v065_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(pe, 4), 4), 12))
def cg_f086_daily_market_metrics_core65_3rd_v066_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(ps, 4), 4), 12))
def cg_f086_daily_market_metrics_core66_3rd_v067_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(_safe_div(ev, marketcap), 4), 4), 12))
def cg_f086_daily_market_metrics_core67_3rd_v068_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(_safe_div(price, pb), 4), 4), 12))
def cg_f086_daily_market_metrics_core68_3rd_v069_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(_safe_div(price, pe), 4), 4), 12))
def cg_f086_daily_market_metrics_core69_3rd_v070_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_diff(_safe_div(price, ps), 4), 4), 12))
def cg_f086_daily_market_metrics_core70_3rd_v071_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(marketcap, 4), 8), 12))
def cg_f086_daily_market_metrics_core71_3rd_v072_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(ev, 4), 8), 12))
def cg_f086_daily_market_metrics_core72_3rd_v073_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(price, 4), 8), 12))
def cg_f086_daily_market_metrics_core73_3rd_v074_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(pb, 4), 8), 12))
def cg_f086_daily_market_metrics_core74_3rd_v075_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(pe, 4), 8), 12))
def cg_f086_daily_market_metrics_core75_3rd_v076_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(ps, 4), 8), 12))
def cg_f086_daily_market_metrics_core76_3rd_v077_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(_safe_div(ev, marketcap), 4), 8), 12))
def cg_f086_daily_market_metrics_core77_3rd_v078_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(_safe_div(price, pb), 4), 8), 12))
def cg_f086_daily_market_metrics_core78_3rd_v079_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(_safe_div(price, pe), 4), 8), 12))
def cg_f086_daily_market_metrics_core79_3rd_v080_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_diff(_safe_div(price, ps), 4), 8), 12))
def cg_f086_daily_market_metrics_core80_3rd_v081_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(marketcap, 4), 4), 12))
def cg_f086_daily_market_metrics_core81_3rd_v082_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(ev, 4), 4), 12))
def cg_f086_daily_market_metrics_core82_3rd_v083_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(price, 4), 4), 12))
def cg_f086_daily_market_metrics_core83_3rd_v084_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(pb, 4), 4), 12))
def cg_f086_daily_market_metrics_core84_3rd_v085_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(pe, 4), 4), 12))
def cg_f086_daily_market_metrics_core85_3rd_v086_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(ps, 4), 4), 12))
def cg_f086_daily_market_metrics_core86_3rd_v087_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(_safe_div(ev, marketcap), 4), 4), 12))
def cg_f086_daily_market_metrics_core87_3rd_v088_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(_safe_div(price, pb), 4), 4), 12))
def cg_f086_daily_market_metrics_core88_3rd_v089_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(_safe_div(price, pe), 4), 4), 12))
def cg_f086_daily_market_metrics_core89_3rd_v090_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_slope(_safe_div(price, ps), 4), 4), 12))
def cg_f086_daily_market_metrics_core90_3rd_v091_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(marketcap, 4), 4), 4))
def cg_f086_daily_market_metrics_core91_3rd_v092_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(ev, 4), 4), 4))
def cg_f086_daily_market_metrics_core92_3rd_v093_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(price, 4), 4), 4))
def cg_f086_daily_market_metrics_core93_3rd_v094_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(pb, 4), 4), 4))
def cg_f086_daily_market_metrics_core94_3rd_v095_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(pe, 4), 4), 4))
def cg_f086_daily_market_metrics_core95_3rd_v096_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(ps, 4), 4), 4))
def cg_f086_daily_market_metrics_core96_3rd_v097_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(_safe_div(ev, marketcap), 4), 4), 4))
def cg_f086_daily_market_metrics_core97_3rd_v098_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(_safe_div(price, pb), 4), 4), 4))
def cg_f086_daily_market_metrics_core98_3rd_v099_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(_safe_div(price, pe), 4), 4), 4))
def cg_f086_daily_market_metrics_core99_3rd_v100_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_diff(_safe_div(price, ps), 4), 4), 4))
def cg_f086_daily_market_metrics_core100_3rd_v101_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(marketcap, 4), 8), 4))
def cg_f086_daily_market_metrics_core101_3rd_v102_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(ev, 4), 8), 4))
def cg_f086_daily_market_metrics_core102_3rd_v103_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(price, 4), 8), 4))
def cg_f086_daily_market_metrics_core103_3rd_v104_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(pb, 4), 8), 4))
def cg_f086_daily_market_metrics_core104_3rd_v105_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(pe, 4), 8), 4))
def cg_f086_daily_market_metrics_core105_3rd_v106_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(ps, 4), 8), 4))
def cg_f086_daily_market_metrics_core106_3rd_v107_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(_safe_div(ev, marketcap), 4), 8), 4))
def cg_f086_daily_market_metrics_core107_3rd_v108_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(_safe_div(price, pb), 4), 8), 4))
def cg_f086_daily_market_metrics_core108_3rd_v109_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(_safe_div(price, pe), 4), 8), 4))
def cg_f086_daily_market_metrics_core109_3rd_v110_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_diff(_safe_div(price, ps), 4), 8), 4))
def cg_f086_daily_market_metrics_core110_3rd_v111_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(marketcap, 4), 4), 4))
def cg_f086_daily_market_metrics_core111_3rd_v112_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(ev, 4), 4), 4))
def cg_f086_daily_market_metrics_core112_3rd_v113_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(price, 4), 4), 4))
def cg_f086_daily_market_metrics_core113_3rd_v114_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(pb, 4), 4), 4))
def cg_f086_daily_market_metrics_core114_3rd_v115_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(pe, 4), 4), 4))
def cg_f086_daily_market_metrics_core115_3rd_v116_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(ps, 4), 4), 4))
def cg_f086_daily_market_metrics_core116_3rd_v117_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(_safe_div(ev, marketcap), 4), 4), 4))
def cg_f086_daily_market_metrics_core117_3rd_v118_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(_safe_div(price, pb), 4), 4), 4))
def cg_f086_daily_market_metrics_core118_3rd_v119_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(_safe_div(price, pe), 4), 4), 4))
def cg_f086_daily_market_metrics_core119_3rd_v120_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_slope(_safe_div(price, ps), 4), 4), 4))
def cg_f086_daily_market_metrics_core120_3rd_v121_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(marketcap, 4), 4), 4))
def cg_f086_daily_market_metrics_core121_3rd_v122_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(ev, 4), 4), 4))
def cg_f086_daily_market_metrics_core122_3rd_v123_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(price, 4), 4), 4))
def cg_f086_daily_market_metrics_core123_3rd_v124_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(pb, 4), 4), 4))
def cg_f086_daily_market_metrics_core124_3rd_v125_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(pe, 4), 4), 4))
def cg_f086_daily_market_metrics_core125_3rd_v126_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(ps, 4), 4), 4))
def cg_f086_daily_market_metrics_core126_3rd_v127_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(_safe_div(ev, marketcap), 4), 4), 4))
def cg_f086_daily_market_metrics_core127_3rd_v128_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(_safe_div(price, pb), 4), 4), 4))
def cg_f086_daily_market_metrics_core128_3rd_v129_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(_safe_div(price, pe), 4), 4), 4))
def cg_f086_daily_market_metrics_core129_3rd_v130_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_diff(_diff(_safe_div(price, ps), 4), 4), 4))
def cg_f086_daily_market_metrics_core130_3rd_v131_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(marketcap, 4), 4), 4))
def cg_f086_daily_market_metrics_core131_3rd_v132_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(ev, 4), 4), 4))
def cg_f086_daily_market_metrics_core132_3rd_v133_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(price, 4), 4), 4))
def cg_f086_daily_market_metrics_core133_3rd_v134_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(pb, 4), 4), 4))
def cg_f086_daily_market_metrics_core134_3rd_v135_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(pe, 4), 4), 4))
def cg_f086_daily_market_metrics_core135_3rd_v136_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(ps, 4), 4), 4))
def cg_f086_daily_market_metrics_core136_3rd_v137_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(_safe_div(ev, marketcap), 4), 4), 4))
def cg_f086_daily_market_metrics_core137_3rd_v138_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(_safe_div(price, pb), 4), 4), 4))
def cg_f086_daily_market_metrics_core138_3rd_v139_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(_safe_div(price, pe), 4), 4), 4))
def cg_f086_daily_market_metrics_core139_3rd_v140_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_diff(_diff(_safe_div(price, ps), 4), 4), 4))
def cg_f086_daily_market_metrics_core140_3rd_v141_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(marketcap, 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core141_3rd_v142_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(ev, 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core142_3rd_v143_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(price, 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core143_3rd_v144_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(pb, 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core144_3rd_v145_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(pe, 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core145_3rd_v146_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(ps, 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core146_3rd_v147_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(ev, marketcap), 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core147_3rd_v148_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(price, pb), 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core148_3rd_v149_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(price, pe), 4), 4), 4), 8))
def cg_f086_daily_market_metrics_core149_3rd_v150_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_diff(_diff(_safe_div(price, ps), 4), 4), 4), 8))