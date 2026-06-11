import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f086_daily_market_metrics_core00_2nd_v001_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(marketcap, 4))
def cg_f086_daily_market_metrics_core01_2nd_v002_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ev, 4))
def cg_f086_daily_market_metrics_core02_2nd_v003_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(price, 4))
def cg_f086_daily_market_metrics_core03_2nd_v004_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(pb, 4))
def cg_f086_daily_market_metrics_core04_2nd_v005_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(pe, 4))
def cg_f086_daily_market_metrics_core05_2nd_v006_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ps, 4))
def cg_f086_daily_market_metrics_core06_2nd_v007_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(ev, marketcap), 4))
def cg_f086_daily_market_metrics_core07_2nd_v008_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(price, pb), 4))
def cg_f086_daily_market_metrics_core08_2nd_v009_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(price, pe), 4))
def cg_f086_daily_market_metrics_core09_2nd_v010_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(price, ps), 4))
def cg_f086_daily_market_metrics_core10_2nd_v011_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(marketcap, 8))
def cg_f086_daily_market_metrics_core11_2nd_v012_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ev, 8))
def cg_f086_daily_market_metrics_core12_2nd_v013_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(price, 8))
def cg_f086_daily_market_metrics_core13_2nd_v014_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(pb, 8))
def cg_f086_daily_market_metrics_core14_2nd_v015_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(pe, 8))
def cg_f086_daily_market_metrics_core15_2nd_v016_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ps, 8))
def cg_f086_daily_market_metrics_core16_2nd_v017_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(ev, marketcap), 8))
def cg_f086_daily_market_metrics_core17_2nd_v018_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(price, pb), 8))
def cg_f086_daily_market_metrics_core18_2nd_v019_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(price, pe), 8))
def cg_f086_daily_market_metrics_core19_2nd_v020_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_safe_div(price, ps), 8))
def cg_f086_daily_market_metrics_core20_2nd_v021_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(marketcap, 4))
def cg_f086_daily_market_metrics_core21_2nd_v022_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(ev, 4))
def cg_f086_daily_market_metrics_core22_2nd_v023_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(price, 4))
def cg_f086_daily_market_metrics_core23_2nd_v024_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(pb, 4))
def cg_f086_daily_market_metrics_core24_2nd_v025_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(pe, 4))
def cg_f086_daily_market_metrics_core25_2nd_v026_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(ps, 4))
def cg_f086_daily_market_metrics_core26_2nd_v027_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_safe_div(ev, marketcap), 4))
def cg_f086_daily_market_metrics_core27_2nd_v028_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_safe_div(price, pb), 4))
def cg_f086_daily_market_metrics_core28_2nd_v029_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_safe_div(price, pe), 4))
def cg_f086_daily_market_metrics_core29_2nd_v030_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_safe_div(price, ps), 4))
def cg_f086_daily_market_metrics_core30_2nd_v031_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(marketcap, 4), 8))
def cg_f086_daily_market_metrics_core31_2nd_v032_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(ev, 4), 8))
def cg_f086_daily_market_metrics_core32_2nd_v033_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(price, 4), 8))
def cg_f086_daily_market_metrics_core33_2nd_v034_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(pb, 4), 8))
def cg_f086_daily_market_metrics_core34_2nd_v035_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(pe, 4), 8))
def cg_f086_daily_market_metrics_core35_2nd_v036_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(ps, 4), 8))
def cg_f086_daily_market_metrics_core36_2nd_v037_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(ev, marketcap), 4), 8))
def cg_f086_daily_market_metrics_core37_2nd_v038_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(price, pb), 4), 8))
def cg_f086_daily_market_metrics_core38_2nd_v039_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(price, pe), 4), 8))
def cg_f086_daily_market_metrics_core39_2nd_v040_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(price, ps), 4), 8))
def cg_f086_daily_market_metrics_core40_2nd_v041_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(marketcap, 8), 12))
def cg_f086_daily_market_metrics_core41_2nd_v042_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(ev, 8), 12))
def cg_f086_daily_market_metrics_core42_2nd_v043_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(price, 8), 12))
def cg_f086_daily_market_metrics_core43_2nd_v044_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(pb, 8), 12))
def cg_f086_daily_market_metrics_core44_2nd_v045_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(pe, 8), 12))
def cg_f086_daily_market_metrics_core45_2nd_v046_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(ps, 8), 12))
def cg_f086_daily_market_metrics_core46_2nd_v047_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(ev, marketcap), 8), 12))
def cg_f086_daily_market_metrics_core47_2nd_v048_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(price, pb), 8), 12))
def cg_f086_daily_market_metrics_core48_2nd_v049_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(price, pe), 8), 12))
def cg_f086_daily_market_metrics_core49_2nd_v050_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_slope(_safe_div(price, ps), 8), 12))
def cg_f086_daily_market_metrics_core50_2nd_v051_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(marketcap, 4), 8))
def cg_f086_daily_market_metrics_core51_2nd_v052_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(ev, 4), 8))
def cg_f086_daily_market_metrics_core52_2nd_v053_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(price, 4), 8))
def cg_f086_daily_market_metrics_core53_2nd_v054_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(pb, 4), 8))
def cg_f086_daily_market_metrics_core54_2nd_v055_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(pe, 4), 8))
def cg_f086_daily_market_metrics_core55_2nd_v056_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(ps, 4), 8))
def cg_f086_daily_market_metrics_core56_2nd_v057_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_safe_div(ev, marketcap), 4), 8))
def cg_f086_daily_market_metrics_core57_2nd_v058_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_safe_div(price, pb), 4), 8))
def cg_f086_daily_market_metrics_core58_2nd_v059_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_safe_div(price, pe), 4), 8))
def cg_f086_daily_market_metrics_core59_2nd_v060_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_safe_div(price, ps), 4), 8))
def cg_f086_daily_market_metrics_core60_2nd_v061_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(marketcap, 4), 12))
def cg_f086_daily_market_metrics_core61_2nd_v062_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(ev, 4), 12))
def cg_f086_daily_market_metrics_core62_2nd_v063_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(price, 4), 12))
def cg_f086_daily_market_metrics_core63_2nd_v064_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(pb, 4), 12))
def cg_f086_daily_market_metrics_core64_2nd_v065_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(pe, 4), 12))
def cg_f086_daily_market_metrics_core65_2nd_v066_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(ps, 4), 12))
def cg_f086_daily_market_metrics_core66_2nd_v067_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_safe_div(ev, marketcap), 4), 12))
def cg_f086_daily_market_metrics_core67_2nd_v068_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_safe_div(price, pb), 4), 12))
def cg_f086_daily_market_metrics_core68_2nd_v069_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_safe_div(price, pe), 4), 12))
def cg_f086_daily_market_metrics_core69_2nd_v070_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_safe_div(price, ps), 4), 12))
def cg_f086_daily_market_metrics_core70_2nd_v071_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(marketcap, 4), 12))
def cg_f086_daily_market_metrics_core71_2nd_v072_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(ev, 4), 12))
def cg_f086_daily_market_metrics_core72_2nd_v073_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(price, 4), 12))
def cg_f086_daily_market_metrics_core73_2nd_v074_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(pb, 4), 12))
def cg_f086_daily_market_metrics_core74_2nd_v075_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(pe, 4), 12))
def cg_f086_daily_market_metrics_core75_2nd_v076_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(ps, 4), 12))
def cg_f086_daily_market_metrics_core76_2nd_v077_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_safe_div(ev, marketcap), 4), 12))
def cg_f086_daily_market_metrics_core77_2nd_v078_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_safe_div(price, pb), 4), 12))
def cg_f086_daily_market_metrics_core78_2nd_v079_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_safe_div(price, pe), 4), 12))
def cg_f086_daily_market_metrics_core79_2nd_v080_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_diff(_safe_div(price, ps), 4), 12))
def cg_f086_daily_market_metrics_core80_2nd_v081_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(marketcap, 4), 4))
def cg_f086_daily_market_metrics_core81_2nd_v082_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(ev, 4), 4))
def cg_f086_daily_market_metrics_core82_2nd_v083_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(price, 4), 4))
def cg_f086_daily_market_metrics_core83_2nd_v084_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(pb, 4), 4))
def cg_f086_daily_market_metrics_core84_2nd_v085_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(pe, 4), 4))
def cg_f086_daily_market_metrics_core85_2nd_v086_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(ps, 4), 4))
def cg_f086_daily_market_metrics_core86_2nd_v087_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_safe_div(ev, marketcap), 4), 4))
def cg_f086_daily_market_metrics_core87_2nd_v088_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_safe_div(price, pb), 4), 4))
def cg_f086_daily_market_metrics_core88_2nd_v089_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_safe_div(price, pe), 4), 4))
def cg_f086_daily_market_metrics_core89_2nd_v090_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_slope(_safe_div(price, ps), 4), 4))
def cg_f086_daily_market_metrics_core90_2nd_v091_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(marketcap, 4), 4))
def cg_f086_daily_market_metrics_core91_2nd_v092_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(ev, 4), 4))
def cg_f086_daily_market_metrics_core92_2nd_v093_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(price, 4), 4))
def cg_f086_daily_market_metrics_core93_2nd_v094_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(pb, 4), 4))
def cg_f086_daily_market_metrics_core94_2nd_v095_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(pe, 4), 4))
def cg_f086_daily_market_metrics_core95_2nd_v096_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(ps, 4), 4))
def cg_f086_daily_market_metrics_core96_2nd_v097_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_safe_div(ev, marketcap), 4), 4))
def cg_f086_daily_market_metrics_core97_2nd_v098_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_safe_div(price, pb), 4), 4))
def cg_f086_daily_market_metrics_core98_2nd_v099_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_safe_div(price, pe), 4), 4))
def cg_f086_daily_market_metrics_core99_2nd_v100_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(_diff(_safe_div(price, ps), 4), 4))
def cg_f086_daily_market_metrics_core100_2nd_v101_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(marketcap, 4), 4))
def cg_f086_daily_market_metrics_core101_2nd_v102_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(ev, 4), 4))
def cg_f086_daily_market_metrics_core102_2nd_v103_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(price, 4), 4))
def cg_f086_daily_market_metrics_core103_2nd_v104_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(pb, 4), 4))
def cg_f086_daily_market_metrics_core104_2nd_v105_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(pe, 4), 4))
def cg_f086_daily_market_metrics_core105_2nd_v106_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(ps, 4), 4))
def cg_f086_daily_market_metrics_core106_2nd_v107_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(ev, marketcap), 4), 4))
def cg_f086_daily_market_metrics_core107_2nd_v108_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(price, pb), 4), 4))
def cg_f086_daily_market_metrics_core108_2nd_v109_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(price, pe), 4), 4))
def cg_f086_daily_market_metrics_core109_2nd_v110_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(price, ps), 4), 4))
def cg_f086_daily_market_metrics_core110_2nd_v111_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(marketcap, 8), 8))
def cg_f086_daily_market_metrics_core111_2nd_v112_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(ev, 8), 8))
def cg_f086_daily_market_metrics_core112_2nd_v113_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(price, 8), 8))
def cg_f086_daily_market_metrics_core113_2nd_v114_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(pb, 8), 8))
def cg_f086_daily_market_metrics_core114_2nd_v115_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(pe, 8), 8))
def cg_f086_daily_market_metrics_core115_2nd_v116_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(ps, 8), 8))
def cg_f086_daily_market_metrics_core116_2nd_v117_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(ev, marketcap), 8), 8))
def cg_f086_daily_market_metrics_core117_2nd_v118_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(price, pb), 8), 8))
def cg_f086_daily_market_metrics_core118_2nd_v119_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(price, pe), 8), 8))
def cg_f086_daily_market_metrics_core119_2nd_v120_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(_mean(_safe_div(price, ps), 8), 8))
def cg_f086_daily_market_metrics_core120_2nd_v121_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(marketcap, 4), 4))
def cg_f086_daily_market_metrics_core121_2nd_v122_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(ev, 4), 4))
def cg_f086_daily_market_metrics_core122_2nd_v123_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(price, 4), 4))
def cg_f086_daily_market_metrics_core123_2nd_v124_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(pb, 4), 4))
def cg_f086_daily_market_metrics_core124_2nd_v125_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(pe, 4), 4))
def cg_f086_daily_market_metrics_core125_2nd_v126_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(ps, 4), 4))
def cg_f086_daily_market_metrics_core126_2nd_v127_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(_safe_div(ev, marketcap), 4), 4))
def cg_f086_daily_market_metrics_core127_2nd_v128_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(_safe_div(price, pb), 4), 4))
def cg_f086_daily_market_metrics_core128_2nd_v129_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(_safe_div(price, pe), 4), 4))
def cg_f086_daily_market_metrics_core129_2nd_v130_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_diff(_mean(_safe_div(price, ps), 4), 4))
def cg_f086_daily_market_metrics_core130_2nd_v131_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(marketcap, 4), 4), 8))
def cg_f086_daily_market_metrics_core131_2nd_v132_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(ev, 4), 4), 8))
def cg_f086_daily_market_metrics_core132_2nd_v133_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(price, 4), 4), 8))
def cg_f086_daily_market_metrics_core133_2nd_v134_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(pb, 4), 4), 8))
def cg_f086_daily_market_metrics_core134_2nd_v135_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(pe, 4), 4), 8))
def cg_f086_daily_market_metrics_core135_2nd_v136_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(ps, 4), 4), 8))
def cg_f086_daily_market_metrics_core136_2nd_v137_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(_safe_div(ev, marketcap), 4), 4), 8))
def cg_f086_daily_market_metrics_core137_2nd_v138_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(_safe_div(price, pb), 4), 4), 8))
def cg_f086_daily_market_metrics_core138_2nd_v139_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(_safe_div(price, pe), 4), 4), 8))
def cg_f086_daily_market_metrics_core139_2nd_v140_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(_diff(_mean(_safe_div(price, ps), 4), 4), 8))
def cg_f086_daily_market_metrics_core140_2nd_v141_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(marketcap, 4), 4), 12))
def cg_f086_daily_market_metrics_core141_2nd_v142_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(ev, 4), 4), 12))
def cg_f086_daily_market_metrics_core142_2nd_v143_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(price, 4), 4), 12))
def cg_f086_daily_market_metrics_core143_2nd_v144_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(pb, 4), 4), 12))
def cg_f086_daily_market_metrics_core144_2nd_v145_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(pe, 4), 4), 12))
def cg_f086_daily_market_metrics_core145_2nd_v146_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(ps, 4), 4), 12))
def cg_f086_daily_market_metrics_core146_2nd_v147_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(_safe_div(ev, marketcap), 4), 4), 12))
def cg_f086_daily_market_metrics_core147_2nd_v148_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(_safe_div(price, pb), 4), 4), 12))
def cg_f086_daily_market_metrics_core148_2nd_v149_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(_safe_div(price, pe), 4), 4), 12))
def cg_f086_daily_market_metrics_core149_2nd_v150_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(_slope(_mean(_safe_div(price, ps), 4), 4), 12))