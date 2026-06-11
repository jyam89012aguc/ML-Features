import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def cg_f086_daily_market_metrics_core00_mean_4q_v001_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(date, 4))
def cg_f086_daily_market_metrics_core01_mean_4q_v002_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(ticker, 4))
def cg_f086_daily_market_metrics_core02_mean_4q_v003_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(marketcap, 4))
def cg_f086_daily_market_metrics_core03_mean_4q_v004_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(ev, 4))
def cg_f086_daily_market_metrics_core04_mean_4q_v005_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(price, 4))
def cg_f086_daily_market_metrics_core05_mean_4q_v006_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(pb, 4))
def cg_f086_daily_market_metrics_core06_mean_4q_v007_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(pe, 4))
def cg_f086_daily_market_metrics_core07_mean_4q_v008_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(ps, 4))
def cg_f086_daily_market_metrics_core08_mean_8q_v009_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(date, 8))
def cg_f086_daily_market_metrics_core09_mean_8q_v010_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(ticker, 8))
def cg_f086_daily_market_metrics_core10_mean_8q_v011_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(marketcap, 8))
def cg_f086_daily_market_metrics_core11_mean_8q_v012_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(ev, 8))
def cg_f086_daily_market_metrics_core12_mean_8q_v013_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(price, 8))
def cg_f086_daily_market_metrics_core13_mean_8q_v014_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(pb, 8))
def cg_f086_daily_market_metrics_core14_mean_8q_v015_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(pe, 8))
def cg_f086_daily_market_metrics_core15_mean_8q_v016_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_mean(ps, 8))
def cg_f086_daily_market_metrics_core16_z_8q_v017_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(date, 8))
def cg_f086_daily_market_metrics_core17_z_8q_v018_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(ticker, 8))
def cg_f086_daily_market_metrics_core18_z_8q_v019_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(marketcap, 8))
def cg_f086_daily_market_metrics_core19_z_8q_v020_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(ev, 8))
def cg_f086_daily_market_metrics_core20_z_8q_v021_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(price, 8))
def cg_f086_daily_market_metrics_core21_z_8q_v022_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(pb, 8))
def cg_f086_daily_market_metrics_core22_z_8q_v023_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(pe, 8))
def cg_f086_daily_market_metrics_core23_z_8q_v024_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(ps, 8))
def cg_f086_daily_market_metrics_core24_z_20q_v025_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(date, 20))
def cg_f086_daily_market_metrics_core25_z_20q_v026_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(ticker, 20))
def cg_f086_daily_market_metrics_core26_z_20q_v027_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(marketcap, 20))
def cg_f086_daily_market_metrics_core27_z_20q_v028_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(ev, 20))
def cg_f086_daily_market_metrics_core28_z_20q_v029_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(price, 20))
def cg_f086_daily_market_metrics_core29_z_20q_v030_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(pb, 20))
def cg_f086_daily_market_metrics_core30_z_20q_v031_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(pe, 20))
def cg_f086_daily_market_metrics_core31_z_20q_v032_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_z(ps, 20))
def cg_f086_daily_market_metrics_core32_rank_12q_v033_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(date, 12))
def cg_f086_daily_market_metrics_core33_rank_12q_v034_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(ticker, 12))
def cg_f086_daily_market_metrics_core34_rank_12q_v035_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(marketcap, 12))
def cg_f086_daily_market_metrics_core35_rank_12q_v036_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(ev, 12))
def cg_f086_daily_market_metrics_core36_rank_12q_v037_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(price, 12))
def cg_f086_daily_market_metrics_core37_rank_12q_v038_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(pb, 12))
def cg_f086_daily_market_metrics_core38_rank_12q_v039_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(pe, 12))
def cg_f086_daily_market_metrics_core39_rank_12q_v040_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(ps, 12))
def cg_f086_daily_market_metrics_core40_rank_20q_v041_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(date, 20))
def cg_f086_daily_market_metrics_core41_rank_20q_v042_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(ticker, 20))
def cg_f086_daily_market_metrics_core42_rank_20q_v043_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(marketcap, 20))
def cg_f086_daily_market_metrics_core43_rank_20q_v044_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(ev, 20))
def cg_f086_daily_market_metrics_core44_rank_20q_v045_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(price, 20))
def cg_f086_daily_market_metrics_core45_rank_20q_v046_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(pb, 20))
def cg_f086_daily_market_metrics_core46_rank_20q_v047_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(pe, 20))
def cg_f086_daily_market_metrics_core47_rank_20q_v048_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_rank(ps, 20))
def cg_f086_daily_market_metrics_core48_pct_1q_v049_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(date, 1))
def cg_f086_daily_market_metrics_core49_pct_1q_v050_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(ticker, 1))
def cg_f086_daily_market_metrics_core50_pct_1q_v051_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(marketcap, 1))
def cg_f086_daily_market_metrics_core51_pct_1q_v052_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(ev, 1))
def cg_f086_daily_market_metrics_core52_pct_1q_v053_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(price, 1))
def cg_f086_daily_market_metrics_core53_pct_1q_v054_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(pb, 1))
def cg_f086_daily_market_metrics_core54_pct_1q_v055_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(pe, 1))
def cg_f086_daily_market_metrics_core55_pct_1q_v056_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(ps, 1))
def cg_f086_daily_market_metrics_core56_pct_4q_v057_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(date, 4))
def cg_f086_daily_market_metrics_core57_pct_4q_v058_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(ticker, 4))
def cg_f086_daily_market_metrics_core58_pct_4q_v059_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(marketcap, 4))
def cg_f086_daily_market_metrics_core59_pct_4q_v060_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(ev, 4))
def cg_f086_daily_market_metrics_core60_pct_4q_v061_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(price, 4))
def cg_f086_daily_market_metrics_core61_pct_4q_v062_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(pb, 4))
def cg_f086_daily_market_metrics_core62_pct_4q_v063_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(pe, 4))
def cg_f086_daily_market_metrics_core63_pct_4q_v064_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_pct_change(ps, 4))
def cg_f086_daily_market_metrics_core64_slope_4q_v065_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(date, 4))
def cg_f086_daily_market_metrics_core65_slope_4q_v066_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ticker, 4))
def cg_f086_daily_market_metrics_core66_slope_4q_v067_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(marketcap, 4))
def cg_f086_daily_market_metrics_core67_slope_4q_v068_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ev, 4))
def cg_f086_daily_market_metrics_core68_slope_4q_v069_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(price, 4))
def cg_f086_daily_market_metrics_core69_slope_4q_v070_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(pb, 4))
def cg_f086_daily_market_metrics_core70_slope_4q_v071_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(pe, 4))
def cg_f086_daily_market_metrics_core71_slope_4q_v072_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ps, 4))
def cg_f086_daily_market_metrics_core72_slope_8q_v073_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(date, 8))
def cg_f086_daily_market_metrics_core73_slope_8q_v074_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(ticker, 8))
def cg_f086_daily_market_metrics_core74_slope_8q_v075_signal(date, ticker, marketcap, ev, price, pb, pe, ps):
    return _clean(_slope(marketcap, 8))