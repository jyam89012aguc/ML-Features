import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff(s, w):
    return s.diff(periods=w) / (s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


# ===== folder domain primitives =====
def _f44_winner_take_all_dominance(marketcap, w):
    base_ = marketcap.rolling(w, min_periods=max(1, w // 2)).mean()
    return base_ / base_.rolling(w * 2, min_periods=max(1, w)).mean().replace(0, np.nan)


def _f44_winner_take_all_growth_excess(marketcap, w):
    g = _diff(np.log(marketcap.replace(0, np.nan)), w)
    bench = g.rolling(w * 2, min_periods=max(1, w)).mean()
    return g - bench


def _f44_winner_take_all_mc_level(marketcap, w):
    return marketcap.rolling(w, min_periods=max(1, w // 2)).mean()


# 5d slope of 21d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_21d_slope_v001_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_21d_slope_v002_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 21) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_63d_slope_v003_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_63d_slope_v004_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 63) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_126d_slope_v005_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 126) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_126d_slope_v006_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 126) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_252d_slope_v007_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_252d_slope_v008_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_504d_slope_v009_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 504) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap dominance × marketcap
def f44wta_f44_winner_take_all_signal_dom_504d_slope_v010_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_21d_slope_v011_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_63d_slope_v012_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_252d_slope_v013_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_504d_slope_v014_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_21d_slope_v015_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_63d_slope_v016_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_252d_slope_v017_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_504d_slope_v018_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexg_21d_slope_v019_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexg_63d_slope_v020_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexg_252d_slope_v021_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexg_504d_slope_v022_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d marketcap level
def f44wta_f44_winner_take_all_signal_level_21d_slope_v023_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 21) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap level
def f44wta_f44_winner_take_all_signal_level_252d_slope_v024_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap level
def f44wta_f44_winner_take_all_signal_level_504d_slope_v025_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 504) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log mc dominance
def f44wta_f44_winner_take_all_signal_logmcdom_252d_slope_v026_signal(marketcap):
    base = np.log(marketcap.replace(0, np.nan)) * _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log ev dominance
def f44wta_f44_winner_take_all_signal_logevdom_252d_slope_v027_signal(ev, marketcap):
    base = np.log(ev.replace(0, np.nan)) * _f44_winner_take_all_dominance(ev, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d marketcap z × marketcap
def f44wta_f44_winner_take_all_signal_mcz_21d_slope_v028_signal(marketcap):
    base = _z(marketcap, 21) * marketcap + _f44_winner_take_all_dominance(marketcap, 21) * 0.0
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap z × marketcap
def f44wta_f44_winner_take_all_signal_mcz_63d_slope_v029_signal(marketcap):
    base = _z(marketcap, 63) * marketcap + _f44_winner_take_all_dominance(marketcap, 63) * 0.0
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap z × marketcap
def f44wta_f44_winner_take_all_signal_mcz_252d_slope_v030_signal(marketcap):
    base = _z(marketcap, 252) * marketcap + _f44_winner_take_all_dominance(marketcap, 252) * 0.0
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d marketcap z × marketcap
def f44wta_f44_winner_take_all_signal_mcz_504d_slope_v031_signal(marketcap):
    base = _z(marketcap, 504) * marketcap + _f44_winner_take_all_dominance(marketcap, 504) * 0.0
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pe winner composite
def f44wta_f44_winner_take_all_signal_pewin_252d_slope_v032_signal(pe, marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * pe * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pb winner composite
def f44wta_f44_winner_take_all_signal_pbwin_252d_slope_v033_signal(pb, marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * pb * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ps winner composite
def f44wta_f44_winner_take_all_signal_pswin_252d_slope_v034_signal(ps, marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * ps * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evebit winner composite
def f44wta_f44_winner_take_all_signal_evebitwin_252d_slope_v035_signal(evebit, marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * evebit * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evebitda winner composite
def f44wta_f44_winner_take_all_signal_evebitdawin_252d_slope_v036_signal(evebitda, marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * evebitda * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sf3a value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3adom_21d_slope_v037_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3a_value, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3a value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3adom_252d_slope_v038_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3a_value, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3b value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3bdom_252d_slope_v039_signal(sf3b_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3b_value, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d sf3b value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3bdom_504d_slope_v040_signal(sf3b_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3b_value, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3a shares dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3ashdom_252d_slope_v041_signal(sf3a_shares, marketcap):
    base = _f44_winner_take_all_dominance(sf3a_shares, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d sf3b shares dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3bshdom_504d_slope_v042_signal(sf3b_shares, marketcap):
    base = _f44_winner_take_all_dominance(sf3b_shares, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_21d_slope_v043_signal(marketcap, ev):
    base = _f44_winner_take_all_growth_excess(marketcap, 21) * ev
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_63d_slope_v044_signal(marketcap, ev):
    base = _f44_winner_take_all_growth_excess(marketcap, 63) * ev
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_252d_slope_v045_signal(marketcap, ev):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_504d_slope_v046_signal(marketcap, ev):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3a value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexg_252d_slope_v047_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3a_value, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d sf3b value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3bexg_504d_slope_v048_signal(sf3b_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3b_value, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ev level × marketcap
def f44wta_f44_winner_take_all_signal_evlevel_252d_slope_v049_signal(ev, marketcap):
    base = _f44_winner_take_all_mc_level(ev, 252) * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ev level × marketcap
def f44wta_f44_winner_take_all_signal_evlevel_504d_slope_v050_signal(ev, marketcap):
    base = _f44_winner_take_all_mc_level(ev, 504) * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap level × ev
def f44wta_f44_winner_take_all_signal_mcxev_252d_slope_v051_signal(marketcap, ev):
    base = _f44_winner_take_all_mc_level(marketcap, 252) * ev / marketcap.replace(0, np.nan).abs()
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap level × ev
def f44wta_f44_winner_take_all_signal_mcxev_504d_slope_v052_signal(marketcap, ev):
    base = _f44_winner_take_all_mc_level(marketcap, 504) * ev / marketcap.replace(0, np.nan).abs()
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log dominance
def f44wta_f44_winner_take_all_signal_logdom_21d_slope_v053_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 21) * np.log(marketcap.replace(0, np.nan))
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log dominance
def f44wta_f44_winner_take_all_signal_logdom_252d_slope_v054_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * np.log(marketcap.replace(0, np.nan))
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d log dominance
def f44wta_f44_winner_take_all_signal_logdom_504d_slope_v055_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 504) * np.log(marketcap.replace(0, np.nan))
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sf3a value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexg_21d_slope_v056_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3a_value, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sf3a value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexg_63d_slope_v057_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3a_value, 63) * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3a shares excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3ashexg_252d_slope_v058_signal(sf3a_shares, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3a_shares, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sf3b shares excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3bshexg_252d_slope_v059_signal(sf3b_shares, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3b_shares, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d dom × revenue
def f44wta_f44_winner_take_all_signal_domxrev_21d_slope_v060_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 21) * _mean(revenue, 21) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dom × revenue
def f44wta_f44_winner_take_all_signal_domxrev_252d_slope_v061_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _mean(revenue, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dom × revenue
def f44wta_f44_winner_take_all_signal_domxrev_504d_slope_v062_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 504) * _mean(revenue, 504) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dom × netinc
def f44wta_f44_winner_take_all_signal_domxni_252d_slope_v063_signal(marketcap, netinc):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _mean(netinc, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dom × ebitda
def f44wta_f44_winner_take_all_signal_domxeb_252d_slope_v064_signal(marketcap, ebitda):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _mean(ebitda, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dom × fcf
def f44wta_f44_winner_take_all_signal_domxfcf_252d_slope_v065_signal(marketcap, fcf):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _mean(fcf, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dom × ev volatility
def f44wta_f44_winner_take_all_signal_domxevvol_63d_slope_v066_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 63) * _std(ev, 63)
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dom × ev volatility
def f44wta_f44_winner_take_all_signal_domxevvol_252d_slope_v067_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _std(ev, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dom × ev volatility
def f44wta_f44_winner_take_all_signal_domxevvol_504d_slope_v068_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 504) * _std(ev, 504)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d dom EWM × marketcap
def f44wta_f44_winner_take_all_signal_domewm_63d_slope_v069_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 63).ewm(span=63, adjust=False).mean() * marketcap
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d dom EWM × marketcap
def f44wta_f44_winner_take_all_signal_domewm_252d_slope_v070_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252).ewm(span=126, adjust=False).mean() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dom EWM × marketcap
def f44wta_f44_winner_take_all_signal_domewm_504d_slope_v071_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 504).ewm(span=252, adjust=False).mean() * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d excess growth EWM × marketcap
def f44wta_f44_winner_take_all_signal_exgewm_252d_slope_v072_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 252).ewm(span=126, adjust=False).mean() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × ps × marketcap
def f44wta_f44_winner_take_all_signal_domxps_252d_slope_v073_signal(marketcap, ps):
    base = _f44_winner_take_all_dominance(marketcap, 252) * ps * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ev dom × pe × marketcap
def f44wta_f44_winner_take_all_signal_evdomxpe_504d_slope_v074_signal(ev, pe, marketcap):
    base = _f44_winner_take_all_dominance(ev, 504) * pe * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev dom × pb × marketcap
def f44wta_f44_winner_take_all_signal_evdomxpb_252d_slope_v075_signal(ev, pb, marketcap):
    base = _f44_winner_take_all_dominance(ev, 252) * pb * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mexg × ev × marketcap
def f44wta_f44_winner_take_all_signal_megxevxmc_504d_slope_v076_signal(marketcap, ev):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * ev * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom squared × ev
def f44wta_f44_winner_take_all_signal_domsq_252d_slope_v077_signal(marketcap, ev):
    d = _f44_winner_take_all_dominance(marketcap, 252)
    base = d * d.abs() * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dom squared × ev (504d)
def f44wta_f44_winner_take_all_signal_domsq_504d_slope_v078_signal(marketcap, ev):
    d = _f44_winner_take_all_dominance(marketcap, 504)
    base = d * d.abs() * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × sf3a value
def f44wta_f44_winner_take_all_signal_domxsf3a_252d_slope_v079_signal(marketcap, sf3a_value):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _mean(sf3a_value, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × sf3b value
def f44wta_f44_winner_take_all_signal_domxsf3b_252d_slope_v080_signal(marketcap, sf3b_value):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _mean(sf3b_value, 252)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_21d_slope_v081_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 21) * _f44_winner_take_all_dominance(ev, 21) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_252d_slope_v082_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _f44_winner_take_all_dominance(ev, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_504d_slope_v083_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 504) * _f44_winner_take_all_dominance(ev, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3a × marketcap winner composite
def f44wta_f44_winner_take_all_signal_sf3awin_252d_slope_v084_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3a_value, 252) * _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of sf3b × marketcap winner composite
def f44wta_f44_winner_take_all_signal_sf3bwin_504d_slope_v085_signal(sf3b_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3b_value, 504) * _f44_winner_take_all_dominance(marketcap, 504) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d mcexg × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_21d_slope_v086_signal(marketcap, revenue):
    base = _f44_winner_take_all_growth_excess(marketcap, 21) * revenue
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d mcexg × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_63d_slope_v087_signal(marketcap, revenue):
    base = _f44_winner_take_all_growth_excess(marketcap, 63) * revenue
    result = _slope_diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d mcexg × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_252d_slope_v088_signal(marketcap, revenue):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * revenue
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d mcexg × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_504d_slope_v089_signal(marketcap, revenue):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * revenue
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mcexg × ebitda
def f44wta_f44_winner_take_all_signal_mcexgxeb_252d_slope_v090_signal(marketcap, ebitda):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * ebitda
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mcexg × ebitda 504d
def f44wta_f44_winner_take_all_signal_mcexgxeb_504d_slope_v091_signal(marketcap, ebitda):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * ebitda
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mcexg × netinc
def f44wta_f44_winner_take_all_signal_mcexgxni_252d_slope_v092_signal(marketcap, netinc):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * netinc
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mcexg × fcf
def f44wta_f44_winner_take_all_signal_mcexgxfcf_504d_slope_v093_signal(marketcap, fcf):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * fcf
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of dom × marketcap squared
def f44wta_f44_winner_take_all_signal_domxmcsq_21d_slope_v094_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 21) * marketcap * marketcap.abs() / 1e9
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × marketcap squared 252d
def f44wta_f44_winner_take_all_signal_domxmcsq_252d_slope_v095_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * marketcap * marketcap.abs() / 1e9
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dom × marketcap squared 504d
def f44wta_f44_winner_take_all_signal_domxmcsq_504d_slope_v096_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 504) * marketcap * marketcap.abs() / 1e9
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ev dom × ev squared 21d
def f44wta_f44_winner_take_all_signal_evdomxevsq_21d_slope_v097_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 21) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev dom × ev squared 252d
def f44wta_f44_winner_take_all_signal_evdomxevsq_252d_slope_v098_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 252) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ev dom × ev squared 504d
def f44wta_f44_winner_take_all_signal_evdomxevsq_504d_slope_v099_signal(ev, marketcap):
    base = _f44_winner_take_all_dominance(ev, 504) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of level × log mc 21d
def f44wta_f44_winner_take_all_signal_levellog_21d_slope_v100_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 21) * np.log(marketcap.replace(0, np.nan))
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of level × log mc 252d
def f44wta_f44_winner_take_all_signal_levellog_252d_slope_v101_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 252) * np.log(marketcap.replace(0, np.nan))
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of level × log mc 504d
def f44wta_f44_winner_take_all_signal_levellog_504d_slope_v102_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 504) * np.log(marketcap.replace(0, np.nan))
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of dom × pe 21d
def f44wta_f44_winner_take_all_signal_domxpe_21d_slope_v103_signal(marketcap, pe):
    base = _f44_winner_take_all_dominance(marketcap, 21) * pe * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × evebit 252d
def f44wta_f44_winner_take_all_signal_domxevebit_252d_slope_v104_signal(marketcap, evebit):
    base = _f44_winner_take_all_dominance(marketcap, 252) * evebit * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dom × evebitda 504d
def f44wta_f44_winner_take_all_signal_domxevebitda_504d_slope_v105_signal(marketcap, evebitda):
    base = _f44_winner_take_all_dominance(marketcap, 504) * evebitda * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × pb 252d
def f44wta_f44_winner_take_all_signal_domxpb_252d_slope_v106_signal(marketcap, pb):
    base = _f44_winner_take_all_dominance(marketcap, 252) * pb * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × ps 252d
def f44wta_f44_winner_take_all_signal_domxps2_252d_slope_v107_signal(marketcap, ps):
    base = _f44_winner_take_all_dominance(marketcap, 252) * ps * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of exg × pe 252d
def f44wta_f44_winner_take_all_signal_exgxpe_252d_slope_v108_signal(marketcap, pe):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * pe * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of exg × evebit 252d
def f44wta_f44_winner_take_all_signal_exgxevebit_252d_slope_v109_signal(marketcap, evebit):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * evebit * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of exg × ps 504d
def f44wta_f44_winner_take_all_signal_exgxps_504d_slope_v110_signal(marketcap, ps):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * ps * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of sf3a concentration 21d
def f44wta_f44_winner_take_all_signal_sf3aconc_21d_slope_v111_signal(sf3a_shares, sf3a_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3a_shares, 21) * _mean(sf3a_value, 21) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3a concentration 252d
def f44wta_f44_winner_take_all_signal_sf3aconc_252d_slope_v112_signal(sf3a_shares, sf3a_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3a_shares, 252) * _mean(sf3a_value, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3b concentration 252d
def f44wta_f44_winner_take_all_signal_sf3bconc_252d_slope_v113_signal(sf3b_shares, sf3b_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3b_shares, 252) * _mean(sf3b_value, 252) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of sf3b concentration 504d
def f44wta_f44_winner_take_all_signal_sf3bconc_504d_slope_v114_signal(sf3b_shares, sf3b_value, marketcap):
    base = _f44_winner_take_all_dominance(sf3b_shares, 504) * _mean(sf3b_value, 504) * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ev exg × marketcap × ev 21d
def f44wta_f44_winner_take_all_signal_evexgxmc_21d_slope_v115_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 21) * marketcap * ev / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev exg × marketcap × ev 252d
def f44wta_f44_winner_take_all_signal_evexgxmc_252d_slope_v116_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 252) * marketcap * ev / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ev exg × marketcap × ev 504d
def f44wta_f44_winner_take_all_signal_evexgxmc_504d_slope_v117_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 504) * marketcap * ev / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of exg × log mc 21d
def f44wta_f44_winner_take_all_signal_exgxlogmc_21d_slope_v118_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 21) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of exg × log mc 252d
def f44wta_f44_winner_take_all_signal_exgxlogmc_252d_slope_v119_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of exg × log mc 504d
def f44wta_f44_winner_take_all_signal_exgxlogmc_504d_slope_v120_signal(marketcap):
    base = _f44_winner_take_all_growth_excess(marketcap, 504) * np.log(marketcap.replace(0, np.nan)) * marketcap
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of winner ops 21d (dom × revenue × marketcap)
def f44wta_f44_winner_take_all_signal_winops_21d_slope_v121_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 21) * marketcap * revenue / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of winner ops 252d
def f44wta_f44_winner_take_all_signal_winops_252d_slope_v122_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 252) * marketcap * revenue / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of winner ops 504d
def f44wta_f44_winner_take_all_signal_winops_504d_slope_v123_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 504) * marketcap * revenue / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of exg squared × ev 21d
def f44wta_f44_winner_take_all_signal_exgsq_21d_slope_v124_signal(marketcap, ev):
    g = _f44_winner_take_all_growth_excess(marketcap, 21)
    base = g * g.abs() * ev
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of exg squared × ev 252d
def f44wta_f44_winner_take_all_signal_exgsq_252d_slope_v125_signal(marketcap, ev):
    g = _f44_winner_take_all_growth_excess(marketcap, 252)
    base = g * g.abs() * ev
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of exg squared × ev 504d
def f44wta_f44_winner_take_all_signal_exgsq_504d_slope_v126_signal(marketcap, ev):
    g = _f44_winner_take_all_growth_excess(marketcap, 504)
    base = g * g.abs() * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of exg squared × marketcap 252d
def f44wta_f44_winner_take_all_signal_exgsqxmc_252d_slope_v127_signal(marketcap):
    g = _f44_winner_take_all_growth_excess(marketcap, 252)
    base = g * g.abs() * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of winrev 21d
def f44wta_f44_winner_take_all_signal_winrev_21d_slope_v128_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 21) * revenue * marketcap / 1e9
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of winrev 252d
def f44wta_f44_winner_take_all_signal_winrev_252d_slope_v129_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 252) * revenue * marketcap / 1e9
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of winrev 504d
def f44wta_f44_winner_take_all_signal_winrev_504d_slope_v130_signal(marketcap, revenue):
    base = _f44_winner_take_all_dominance(marketcap, 504) * revenue * marketcap / 1e9
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compwin 252d
def f44wta_f44_winner_take_all_signal_compwin_252d_slope_v131_signal(marketcap):
    base = _f44_winner_take_all_dominance(marketcap, 252) * _f44_winner_take_all_growth_excess(marketcap, 252) * marketcap
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of compwin 504d × ev
def f44wta_f44_winner_take_all_signal_compwin_504d_slope_v132_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 504) * _f44_winner_take_all_growth_excess(marketcap, 504) * ev
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of sf3a exg × value 21d
def f44wta_f44_winner_take_all_signal_sf3aexgxv_21d_slope_v133_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3a_value, 21) * sf3a_value * marketcap / sf3a_value.replace(0, np.nan).abs()
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of sf3a exg × value 252d
def f44wta_f44_winner_take_all_signal_sf3aexgxv_252d_slope_v134_signal(sf3a_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3a_value, 252) * sf3a_value * marketcap / sf3a_value.replace(0, np.nan).abs()
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of sf3b exg × value 504d
def f44wta_f44_winner_take_all_signal_sf3bexgxv_504d_slope_v135_signal(sf3b_value, marketcap):
    base = _f44_winner_take_all_growth_excess(sf3b_value, 504) * sf3b_value * marketcap / sf3b_value.replace(0, np.nan).abs()
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of winev2 252d
def f44wta_f44_winner_take_all_signal_winev2_252d_slope_v136_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 252) * ev * ev / 1e9
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of winev2 504d
def f44wta_f44_winner_take_all_signal_winev2_504d_slope_v137_signal(marketcap, ev):
    base = _f44_winner_take_all_dominance(marketcap, 504) * ev * ev / 1e9
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ev exg × ev × marketcap 21d
def f44wta_f44_winner_take_all_signal_evexgxev_21d_slope_v138_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 21) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ev exg × ev × marketcap 252d
def f44wta_f44_winner_take_all_signal_evexgxev_252d_slope_v139_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 252) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of ev exg × ev × marketcap 504d
def f44wta_f44_winner_take_all_signal_evexgxev_504d_slope_v140_signal(ev, marketcap):
    base = _f44_winner_take_all_growth_excess(ev, 504) * ev * marketcap / ev.replace(0, np.nan).abs()
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of dom × debt 21d
def f44wta_f44_winner_take_all_signal_domxdebt_21d_slope_v141_signal(marketcap, debt):
    base = _f44_winner_take_all_dominance(marketcap, 21) * debt
    result = _slope_diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × debt 252d
def f44wta_f44_winner_take_all_signal_domxdebt_252d_slope_v142_signal(marketcap, debt):
    base = _f44_winner_take_all_dominance(marketcap, 252) * debt
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dom × debt 504d
def f44wta_f44_winner_take_all_signal_domxdebt_504d_slope_v143_signal(marketcap, debt):
    base = _f44_winner_take_all_dominance(marketcap, 504) * debt
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × equity 252d
def f44wta_f44_winner_take_all_signal_domxeq_252d_slope_v144_signal(marketcap, equity):
    base = _f44_winner_take_all_dominance(marketcap, 252) * equity
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dom × equity 504d
def f44wta_f44_winner_take_all_signal_domxeq_504d_slope_v145_signal(marketcap, equity):
    base = _f44_winner_take_all_dominance(marketcap, 504) * equity
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of dom × assets 252d
def f44wta_f44_winner_take_all_signal_domxat_252d_slope_v146_signal(marketcap, assets):
    base = _f44_winner_take_all_dominance(marketcap, 252) * assets
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of dom × assets 504d
def f44wta_f44_winner_take_all_signal_domxat_504d_slope_v147_signal(marketcap, assets):
    base = _f44_winner_take_all_dominance(marketcap, 504) * assets
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evdom × revenue × marketcap 252d
def f44wta_f44_winner_take_all_signal_evdomxrev_252d_slope_v148_signal(ev, revenue, marketcap):
    base = _f44_winner_take_all_dominance(ev, 252) * revenue * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of evdom × ebitda × marketcap 504d
def f44wta_f44_winner_take_all_signal_evdomxeb_504d_slope_v149_signal(ev, ebitda, marketcap):
    base = _f44_winner_take_all_dominance(ev, 504) * ebitda * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of super winner composite 252d
def f44wta_f44_winner_take_all_signal_superwin_252d_slope_v150_signal(marketcap, ev):
    d = _f44_winner_take_all_dominance(marketcap, 252)
    g = _f44_winner_take_all_growth_excess(marketcap, 252)
    base = d * g * ev * marketcap / marketcap.replace(0, np.nan)
    result = _slope_diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44wta_f44_winner_take_all_signal_dom_21d_slope_v001_signal,
    f44wta_f44_winner_take_all_signal_dom_21d_slope_v002_signal,
    f44wta_f44_winner_take_all_signal_dom_63d_slope_v003_signal,
    f44wta_f44_winner_take_all_signal_dom_63d_slope_v004_signal,
    f44wta_f44_winner_take_all_signal_dom_126d_slope_v005_signal,
    f44wta_f44_winner_take_all_signal_dom_126d_slope_v006_signal,
    f44wta_f44_winner_take_all_signal_dom_252d_slope_v007_signal,
    f44wta_f44_winner_take_all_signal_dom_252d_slope_v008_signal,
    f44wta_f44_winner_take_all_signal_dom_504d_slope_v009_signal,
    f44wta_f44_winner_take_all_signal_dom_504d_slope_v010_signal,
    f44wta_f44_winner_take_all_signal_evdom_21d_slope_v011_signal,
    f44wta_f44_winner_take_all_signal_evdom_63d_slope_v012_signal,
    f44wta_f44_winner_take_all_signal_evdom_252d_slope_v013_signal,
    f44wta_f44_winner_take_all_signal_evdom_504d_slope_v014_signal,
    f44wta_f44_winner_take_all_signal_excessg_21d_slope_v015_signal,
    f44wta_f44_winner_take_all_signal_excessg_63d_slope_v016_signal,
    f44wta_f44_winner_take_all_signal_excessg_252d_slope_v017_signal,
    f44wta_f44_winner_take_all_signal_excessg_504d_slope_v018_signal,
    f44wta_f44_winner_take_all_signal_evexg_21d_slope_v019_signal,
    f44wta_f44_winner_take_all_signal_evexg_63d_slope_v020_signal,
    f44wta_f44_winner_take_all_signal_evexg_252d_slope_v021_signal,
    f44wta_f44_winner_take_all_signal_evexg_504d_slope_v022_signal,
    f44wta_f44_winner_take_all_signal_level_21d_slope_v023_signal,
    f44wta_f44_winner_take_all_signal_level_252d_slope_v024_signal,
    f44wta_f44_winner_take_all_signal_level_504d_slope_v025_signal,
    f44wta_f44_winner_take_all_signal_logmcdom_252d_slope_v026_signal,
    f44wta_f44_winner_take_all_signal_logevdom_252d_slope_v027_signal,
    f44wta_f44_winner_take_all_signal_mcz_21d_slope_v028_signal,
    f44wta_f44_winner_take_all_signal_mcz_63d_slope_v029_signal,
    f44wta_f44_winner_take_all_signal_mcz_252d_slope_v030_signal,
    f44wta_f44_winner_take_all_signal_mcz_504d_slope_v031_signal,
    f44wta_f44_winner_take_all_signal_pewin_252d_slope_v032_signal,
    f44wta_f44_winner_take_all_signal_pbwin_252d_slope_v033_signal,
    f44wta_f44_winner_take_all_signal_pswin_252d_slope_v034_signal,
    f44wta_f44_winner_take_all_signal_evebitwin_252d_slope_v035_signal,
    f44wta_f44_winner_take_all_signal_evebitdawin_252d_slope_v036_signal,
    f44wta_f44_winner_take_all_signal_sf3adom_21d_slope_v037_signal,
    f44wta_f44_winner_take_all_signal_sf3adom_252d_slope_v038_signal,
    f44wta_f44_winner_take_all_signal_sf3bdom_252d_slope_v039_signal,
    f44wta_f44_winner_take_all_signal_sf3bdom_504d_slope_v040_signal,
    f44wta_f44_winner_take_all_signal_sf3ashdom_252d_slope_v041_signal,
    f44wta_f44_winner_take_all_signal_sf3bshdom_504d_slope_v042_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_21d_slope_v043_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_63d_slope_v044_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_252d_slope_v045_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_504d_slope_v046_signal,
    f44wta_f44_winner_take_all_signal_sf3aexg_252d_slope_v047_signal,
    f44wta_f44_winner_take_all_signal_sf3bexg_504d_slope_v048_signal,
    f44wta_f44_winner_take_all_signal_evlevel_252d_slope_v049_signal,
    f44wta_f44_winner_take_all_signal_evlevel_504d_slope_v050_signal,
    f44wta_f44_winner_take_all_signal_mcxev_252d_slope_v051_signal,
    f44wta_f44_winner_take_all_signal_mcxev_504d_slope_v052_signal,
    f44wta_f44_winner_take_all_signal_logdom_21d_slope_v053_signal,
    f44wta_f44_winner_take_all_signal_logdom_252d_slope_v054_signal,
    f44wta_f44_winner_take_all_signal_logdom_504d_slope_v055_signal,
    f44wta_f44_winner_take_all_signal_sf3aexg_21d_slope_v056_signal,
    f44wta_f44_winner_take_all_signal_sf3aexg_63d_slope_v057_signal,
    f44wta_f44_winner_take_all_signal_sf3ashexg_252d_slope_v058_signal,
    f44wta_f44_winner_take_all_signal_sf3bshexg_252d_slope_v059_signal,
    f44wta_f44_winner_take_all_signal_domxrev_21d_slope_v060_signal,
    f44wta_f44_winner_take_all_signal_domxrev_252d_slope_v061_signal,
    f44wta_f44_winner_take_all_signal_domxrev_504d_slope_v062_signal,
    f44wta_f44_winner_take_all_signal_domxni_252d_slope_v063_signal,
    f44wta_f44_winner_take_all_signal_domxeb_252d_slope_v064_signal,
    f44wta_f44_winner_take_all_signal_domxfcf_252d_slope_v065_signal,
    f44wta_f44_winner_take_all_signal_domxevvol_63d_slope_v066_signal,
    f44wta_f44_winner_take_all_signal_domxevvol_252d_slope_v067_signal,
    f44wta_f44_winner_take_all_signal_domxevvol_504d_slope_v068_signal,
    f44wta_f44_winner_take_all_signal_domewm_63d_slope_v069_signal,
    f44wta_f44_winner_take_all_signal_domewm_252d_slope_v070_signal,
    f44wta_f44_winner_take_all_signal_domewm_504d_slope_v071_signal,
    f44wta_f44_winner_take_all_signal_exgewm_252d_slope_v072_signal,
    f44wta_f44_winner_take_all_signal_domxps_252d_slope_v073_signal,
    f44wta_f44_winner_take_all_signal_evdomxpe_504d_slope_v074_signal,
    f44wta_f44_winner_take_all_signal_evdomxpb_252d_slope_v075_signal,
    f44wta_f44_winner_take_all_signal_megxevxmc_504d_slope_v076_signal,
    f44wta_f44_winner_take_all_signal_domsq_252d_slope_v077_signal,
    f44wta_f44_winner_take_all_signal_domsq_504d_slope_v078_signal,
    f44wta_f44_winner_take_all_signal_domxsf3a_252d_slope_v079_signal,
    f44wta_f44_winner_take_all_signal_domxsf3b_252d_slope_v080_signal,
    f44wta_f44_winner_take_all_signal_mcevdom_21d_slope_v081_signal,
    f44wta_f44_winner_take_all_signal_mcevdom_252d_slope_v082_signal,
    f44wta_f44_winner_take_all_signal_mcevdom_504d_slope_v083_signal,
    f44wta_f44_winner_take_all_signal_sf3awin_252d_slope_v084_signal,
    f44wta_f44_winner_take_all_signal_sf3bwin_504d_slope_v085_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_21d_slope_v086_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_63d_slope_v087_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_252d_slope_v088_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_504d_slope_v089_signal,
    f44wta_f44_winner_take_all_signal_mcexgxeb_252d_slope_v090_signal,
    f44wta_f44_winner_take_all_signal_mcexgxeb_504d_slope_v091_signal,
    f44wta_f44_winner_take_all_signal_mcexgxni_252d_slope_v092_signal,
    f44wta_f44_winner_take_all_signal_mcexgxfcf_504d_slope_v093_signal,
    f44wta_f44_winner_take_all_signal_domxmcsq_21d_slope_v094_signal,
    f44wta_f44_winner_take_all_signal_domxmcsq_252d_slope_v095_signal,
    f44wta_f44_winner_take_all_signal_domxmcsq_504d_slope_v096_signal,
    f44wta_f44_winner_take_all_signal_evdomxevsq_21d_slope_v097_signal,
    f44wta_f44_winner_take_all_signal_evdomxevsq_252d_slope_v098_signal,
    f44wta_f44_winner_take_all_signal_evdomxevsq_504d_slope_v099_signal,
    f44wta_f44_winner_take_all_signal_levellog_21d_slope_v100_signal,
    f44wta_f44_winner_take_all_signal_levellog_252d_slope_v101_signal,
    f44wta_f44_winner_take_all_signal_levellog_504d_slope_v102_signal,
    f44wta_f44_winner_take_all_signal_domxpe_21d_slope_v103_signal,
    f44wta_f44_winner_take_all_signal_domxevebit_252d_slope_v104_signal,
    f44wta_f44_winner_take_all_signal_domxevebitda_504d_slope_v105_signal,
    f44wta_f44_winner_take_all_signal_domxpb_252d_slope_v106_signal,
    f44wta_f44_winner_take_all_signal_domxps2_252d_slope_v107_signal,
    f44wta_f44_winner_take_all_signal_exgxpe_252d_slope_v108_signal,
    f44wta_f44_winner_take_all_signal_exgxevebit_252d_slope_v109_signal,
    f44wta_f44_winner_take_all_signal_exgxps_504d_slope_v110_signal,
    f44wta_f44_winner_take_all_signal_sf3aconc_21d_slope_v111_signal,
    f44wta_f44_winner_take_all_signal_sf3aconc_252d_slope_v112_signal,
    f44wta_f44_winner_take_all_signal_sf3bconc_252d_slope_v113_signal,
    f44wta_f44_winner_take_all_signal_sf3bconc_504d_slope_v114_signal,
    f44wta_f44_winner_take_all_signal_evexgxmc_21d_slope_v115_signal,
    f44wta_f44_winner_take_all_signal_evexgxmc_252d_slope_v116_signal,
    f44wta_f44_winner_take_all_signal_evexgxmc_504d_slope_v117_signal,
    f44wta_f44_winner_take_all_signal_exgxlogmc_21d_slope_v118_signal,
    f44wta_f44_winner_take_all_signal_exgxlogmc_252d_slope_v119_signal,
    f44wta_f44_winner_take_all_signal_exgxlogmc_504d_slope_v120_signal,
    f44wta_f44_winner_take_all_signal_winops_21d_slope_v121_signal,
    f44wta_f44_winner_take_all_signal_winops_252d_slope_v122_signal,
    f44wta_f44_winner_take_all_signal_winops_504d_slope_v123_signal,
    f44wta_f44_winner_take_all_signal_exgsq_21d_slope_v124_signal,
    f44wta_f44_winner_take_all_signal_exgsq_252d_slope_v125_signal,
    f44wta_f44_winner_take_all_signal_exgsq_504d_slope_v126_signal,
    f44wta_f44_winner_take_all_signal_exgsqxmc_252d_slope_v127_signal,
    f44wta_f44_winner_take_all_signal_winrev_21d_slope_v128_signal,
    f44wta_f44_winner_take_all_signal_winrev_252d_slope_v129_signal,
    f44wta_f44_winner_take_all_signal_winrev_504d_slope_v130_signal,
    f44wta_f44_winner_take_all_signal_compwin_252d_slope_v131_signal,
    f44wta_f44_winner_take_all_signal_compwin_504d_slope_v132_signal,
    f44wta_f44_winner_take_all_signal_sf3aexgxv_21d_slope_v133_signal,
    f44wta_f44_winner_take_all_signal_sf3aexgxv_252d_slope_v134_signal,
    f44wta_f44_winner_take_all_signal_sf3bexgxv_504d_slope_v135_signal,
    f44wta_f44_winner_take_all_signal_winev2_252d_slope_v136_signal,
    f44wta_f44_winner_take_all_signal_winev2_504d_slope_v137_signal,
    f44wta_f44_winner_take_all_signal_evexgxev_21d_slope_v138_signal,
    f44wta_f44_winner_take_all_signal_evexgxev_252d_slope_v139_signal,
    f44wta_f44_winner_take_all_signal_evexgxev_504d_slope_v140_signal,
    f44wta_f44_winner_take_all_signal_domxdebt_21d_slope_v141_signal,
    f44wta_f44_winner_take_all_signal_domxdebt_252d_slope_v142_signal,
    f44wta_f44_winner_take_all_signal_domxdebt_504d_slope_v143_signal,
    f44wta_f44_winner_take_all_signal_domxeq_252d_slope_v144_signal,
    f44wta_f44_winner_take_all_signal_domxeq_504d_slope_v145_signal,
    f44wta_f44_winner_take_all_signal_domxat_252d_slope_v146_signal,
    f44wta_f44_winner_take_all_signal_domxat_504d_slope_v147_signal,
    f44wta_f44_winner_take_all_signal_evdomxrev_252d_slope_v148_signal,
    f44wta_f44_winner_take_all_signal_evdomxeb_504d_slope_v149_signal,
    f44wta_f44_winner_take_all_signal_superwin_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_WINNER_TAKE_ALL_SIGNAL_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")
    sf3a_shares = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="sf3a_shares")
    sf3a_value = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0005, 0.012, n))), name="sf3a_value")
    sf3b_shares = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.006, n))), name="sf3b_shares")
    sf3b_value = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0004, 0.013, n))), name="sf3b_value")

    cols = {
        "closeadj": closeadj, "marketcap": marketcap, "revenue": revenue,
        "netinc": netinc, "fcf": fcf, "ncfo": ncfo, "equity": equity,
        "debt": debt, "assets": assets, "ebitda": ebitda, "opinc": opinc,
        "sharesbas": sharesbas, "ev": ev, "evebit": evebit, "evebitda": evebitda,
        "pe": pe, "pb": pb, "ps": ps,
        "sf3a_shares": sf3a_shares, "sf3a_value": sf3a_value,
        "sf3b_shares": sf3b_shares, "sf3b_value": sf3b_value,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f44_winner_take_all_dominance", "_f44_winner_take_all_growth_excess",
                         "_f44_winner_take_all_mc_level")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f44_winner_take_all_signal_2nd_derivatives_001_150_claude: {n_features} features pass")
