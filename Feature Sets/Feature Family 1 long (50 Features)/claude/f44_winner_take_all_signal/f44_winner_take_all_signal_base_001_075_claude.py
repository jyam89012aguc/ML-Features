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


# 21d marketcap dominance ratio × marketcap
def f44wta_f44_winner_take_all_signal_dom_21d_base_v001_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap dominance ratio × marketcap
def f44wta_f44_winner_take_all_signal_dom_63d_base_v002_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 126d marketcap dominance ratio × marketcap
def f44wta_f44_winner_take_all_signal_dom_126d_base_v003_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance ratio × marketcap
def f44wta_f44_winner_take_all_signal_dom_252d_base_v004_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance ratio × marketcap
def f44wta_f44_winner_take_all_signal_dom_504d_base_v005_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_21d_base_v006_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_63d_base_v007_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_252d_base_v008_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev dominance × marketcap
def f44wta_f44_winner_take_all_signal_evdom_504d_base_v009_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_21d_base_v010_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_63d_base_v011_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_252d_base_v012_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × marketcap
def f44wta_f44_winner_take_all_signal_excessg_504d_base_v013_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexcessg_21d_base_v014_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexcessg_63d_base_v015_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexcessg_252d_base_v016_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev excess growth × marketcap
def f44wta_f44_winner_take_all_signal_evexcessg_504d_base_v017_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap level × marketcap (level dominance)
def f44wta_f44_winner_take_all_signal_mclevel_21d_base_v018_signal(marketcap):
    result = _f44_winner_take_all_mc_level(marketcap, 21) * marketcap / marketcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap level × marketcap
def f44wta_f44_winner_take_all_signal_mclevel_252d_base_v019_signal(marketcap):
    result = _f44_winner_take_all_mc_level(marketcap, 252) * marketcap / marketcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap level × marketcap
def f44wta_f44_winner_take_all_signal_mclevel_504d_base_v020_signal(marketcap):
    result = _f44_winner_take_all_mc_level(marketcap, 504) * marketcap / marketcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# log marketcap × dominance 252d
def f44wta_f44_winner_take_all_signal_logmcdom_252d_base_v021_signal(marketcap):
    result = np.log(marketcap.replace(0, np.nan)) * _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# log ev × dominance 252d × marketcap
def f44wta_f44_winner_take_all_signal_logevdom_252d_base_v022_signal(ev, marketcap):
    result = np.log(ev.replace(0, np.nan)) * _f44_winner_take_all_dominance(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap zscore × marketcap level
def f44wta_f44_winner_take_all_signal_mcz_21d_base_v023_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 21)
    result = _z(marketcap, 21) * base
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap zscore × marketcap
def f44wta_f44_winner_take_all_signal_mcz_63d_base_v024_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 63)
    result = _z(marketcap, 63) * base
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap zscore × marketcap
def f44wta_f44_winner_take_all_signal_mcz_252d_base_v025_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 252)
    result = _z(marketcap, 252) * base
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap zscore × marketcap
def f44wta_f44_winner_take_all_signal_mcz_504d_base_v026_signal(marketcap):
    base = _f44_winner_take_all_mc_level(marketcap, 504)
    result = _z(marketcap, 504) * base
    return result.replace([np.inf, -np.inf], np.nan)


# pe-to-marketcap ratio composite
def f44wta_f44_winner_take_all_signal_pewinner_252d_base_v027_signal(pe, marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * pe * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# pb-to-marketcap composite
def f44wta_f44_winner_take_all_signal_pbwinner_252d_base_v028_signal(pb, marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * pb * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# ps-to-marketcap composite
def f44wta_f44_winner_take_all_signal_pswinner_252d_base_v029_signal(ps, marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * ps * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# evebit-winner composite × marketcap
def f44wta_f44_winner_take_all_signal_evebitwin_252d_base_v030_signal(evebit, marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * evebit * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda-winner composite × marketcap
def f44wta_f44_winner_take_all_signal_evebitdawin_252d_base_v031_signal(evebitda, marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * evebitda * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a value dominance × marketcap (institutional concentration)
def f44wta_f44_winner_take_all_signal_sf3adom_21d_base_v032_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_value, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3adom_252d_base_v033_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3bdom_252d_base_v034_signal(sf3b_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3b_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3bdom_504d_base_v035_signal(sf3b_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3b_value, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a shares dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3ashdom_252d_base_v036_signal(sf3a_shares, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_shares, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b shares dominance × marketcap
def f44wta_f44_winner_take_all_signal_sf3bshdom_504d_base_v037_signal(sf3b_shares, marketcap):
    result = _f44_winner_take_all_dominance(sf3b_shares, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_21d_base_v038_signal(marketcap, ev):
    result = _f44_winner_take_all_growth_excess(marketcap, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_63d_base_v039_signal(marketcap, ev):
    result = _f44_winner_take_all_growth_excess(marketcap, 63) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_252d_base_v040_signal(marketcap, ev):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × ev
def f44wta_f44_winner_take_all_signal_mcgxev_504d_base_v041_signal(marketcap, ev):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexg_252d_base_v042_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3a_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3bexg_504d_base_v043_signal(sf3b_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3b_value, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev level × marketcap (winner-size composite)
def f44wta_f44_winner_take_all_signal_evlevel_252d_base_v044_signal(ev, marketcap):
    result = _f44_winner_take_all_mc_level(ev, 252) * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev level × marketcap
def f44wta_f44_winner_take_all_signal_evlevel_504d_base_v045_signal(ev, marketcap):
    result = _f44_winner_take_all_mc_level(ev, 504) * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap level × ev (size-dominance composite)
def f44wta_f44_winner_take_all_signal_mcxev_252d_base_v046_signal(marketcap, ev):
    result = _f44_winner_take_all_mc_level(marketcap, 252) * ev / marketcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap level × ev
def f44wta_f44_winner_take_all_signal_mcxev_504d_base_v047_signal(marketcap, ev):
    result = _f44_winner_take_all_mc_level(marketcap, 504) * ev / marketcap.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × log marketcap
def f44wta_f44_winner_take_all_signal_logdom_21d_base_v048_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 21) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × log marketcap
def f44wta_f44_winner_take_all_signal_logdom_252d_base_v049_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × log marketcap
def f44wta_f44_winner_take_all_signal_logdom_504d_base_v050_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 504) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexg_21d_base_v051_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3a_value, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d sf3a value excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexg_63d_base_v052_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3a_value, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a shares excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3ashexg_252d_base_v053_signal(sf3a_shares, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3a_shares, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b shares excess growth × marketcap
def f44wta_f44_winner_take_all_signal_sf3bshexg_252d_base_v054_signal(sf3b_shares, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3b_shares, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × revenue mean
def f44wta_f44_winner_take_all_signal_domxrev_21d_base_v055_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 21) * _mean(revenue, 21) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × revenue mean
def f44wta_f44_winner_take_all_signal_domxrev_252d_base_v056_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _mean(revenue, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × revenue mean
def f44wta_f44_winner_take_all_signal_domxrev_504d_base_v057_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 504) * _mean(revenue, 504) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × netinc mean
def f44wta_f44_winner_take_all_signal_domxni_252d_base_v058_signal(marketcap, netinc):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _mean(netinc, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × ebitda mean
def f44wta_f44_winner_take_all_signal_domxeb_252d_base_v059_signal(marketcap, ebitda):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _mean(ebitda, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × fcf mean
def f44wta_f44_winner_take_all_signal_domxfcf_252d_base_v060_signal(marketcap, fcf):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _mean(fcf, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × ev volatility
def f44wta_f44_winner_take_all_signal_domxevvol_63d_base_v061_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 63) * _std(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × ev volatility
def f44wta_f44_winner_take_all_signal_domxevvol_252d_base_v062_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _std(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × ev volatility
def f44wta_f44_winner_take_all_signal_domxevvol_504d_base_v063_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 504) * _std(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance EWM × marketcap
def f44wta_f44_winner_take_all_signal_domewm_63d_base_v064_signal(marketcap):
    base_ = _f44_winner_take_all_dominance(marketcap, 63)
    result = base_.ewm(span=63, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance EWM × marketcap
def f44wta_f44_winner_take_all_signal_domewm_252d_base_v065_signal(marketcap):
    base_ = _f44_winner_take_all_dominance(marketcap, 252)
    result = base_.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance EWM × marketcap
def f44wta_f44_winner_take_all_signal_domewm_504d_base_v066_signal(marketcap):
    base_ = _f44_winner_take_all_dominance(marketcap, 504)
    result = base_.ewm(span=252, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth EWM × marketcap
def f44wta_f44_winner_take_all_signal_exgewm_252d_base_v067_signal(marketcap):
    base_ = _f44_winner_take_all_growth_excess(marketcap, 252)
    result = base_.ewm(span=126, adjust=False).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × ps
def f44wta_f44_winner_take_all_signal_domxps_252d_base_v068_signal(marketcap, ps):
    result = _f44_winner_take_all_dominance(marketcap, 252) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev dominance × pe
def f44wta_f44_winner_take_all_signal_evdomxpe_504d_base_v069_signal(ev, pe, marketcap):
    result = _f44_winner_take_all_dominance(ev, 504) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev dominance × pb
def f44wta_f44_winner_take_all_signal_evdomxpb_252d_base_v070_signal(ev, pb, marketcap):
    result = _f44_winner_take_all_dominance(ev, 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × ev × marketcap composite
def f44wta_f44_winner_take_all_signal_megxevxmc_504d_base_v071_signal(marketcap, ev):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * ev * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance squared × ev (super-winner)
def f44wta_f44_winner_take_all_signal_domsq_252d_base_v072_signal(marketcap, ev):
    d = _f44_winner_take_all_dominance(marketcap, 252)
    result = d * d.abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance squared × ev
def f44wta_f44_winner_take_all_signal_domsq_504d_base_v073_signal(marketcap, ev):
    d = _f44_winner_take_all_dominance(marketcap, 504)
    result = d * d.abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × sf3a value (smart-money confirmed winner)
def f44wta_f44_winner_take_all_signal_domxsf3a_252d_base_v074_signal(marketcap, sf3a_value):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _mean(sf3a_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × sf3b value (smart-money winner)
def f44wta_f44_winner_take_all_signal_domxsf3b_252d_base_v075_signal(marketcap, sf3b_value):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _mean(sf3b_value, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44wta_f44_winner_take_all_signal_dom_21d_base_v001_signal,
    f44wta_f44_winner_take_all_signal_dom_63d_base_v002_signal,
    f44wta_f44_winner_take_all_signal_dom_126d_base_v003_signal,
    f44wta_f44_winner_take_all_signal_dom_252d_base_v004_signal,
    f44wta_f44_winner_take_all_signal_dom_504d_base_v005_signal,
    f44wta_f44_winner_take_all_signal_evdom_21d_base_v006_signal,
    f44wta_f44_winner_take_all_signal_evdom_63d_base_v007_signal,
    f44wta_f44_winner_take_all_signal_evdom_252d_base_v008_signal,
    f44wta_f44_winner_take_all_signal_evdom_504d_base_v009_signal,
    f44wta_f44_winner_take_all_signal_excessg_21d_base_v010_signal,
    f44wta_f44_winner_take_all_signal_excessg_63d_base_v011_signal,
    f44wta_f44_winner_take_all_signal_excessg_252d_base_v012_signal,
    f44wta_f44_winner_take_all_signal_excessg_504d_base_v013_signal,
    f44wta_f44_winner_take_all_signal_evexcessg_21d_base_v014_signal,
    f44wta_f44_winner_take_all_signal_evexcessg_63d_base_v015_signal,
    f44wta_f44_winner_take_all_signal_evexcessg_252d_base_v016_signal,
    f44wta_f44_winner_take_all_signal_evexcessg_504d_base_v017_signal,
    f44wta_f44_winner_take_all_signal_mclevel_21d_base_v018_signal,
    f44wta_f44_winner_take_all_signal_mclevel_252d_base_v019_signal,
    f44wta_f44_winner_take_all_signal_mclevel_504d_base_v020_signal,
    f44wta_f44_winner_take_all_signal_logmcdom_252d_base_v021_signal,
    f44wta_f44_winner_take_all_signal_logevdom_252d_base_v022_signal,
    f44wta_f44_winner_take_all_signal_mcz_21d_base_v023_signal,
    f44wta_f44_winner_take_all_signal_mcz_63d_base_v024_signal,
    f44wta_f44_winner_take_all_signal_mcz_252d_base_v025_signal,
    f44wta_f44_winner_take_all_signal_mcz_504d_base_v026_signal,
    f44wta_f44_winner_take_all_signal_pewinner_252d_base_v027_signal,
    f44wta_f44_winner_take_all_signal_pbwinner_252d_base_v028_signal,
    f44wta_f44_winner_take_all_signal_pswinner_252d_base_v029_signal,
    f44wta_f44_winner_take_all_signal_evebitwin_252d_base_v030_signal,
    f44wta_f44_winner_take_all_signal_evebitdawin_252d_base_v031_signal,
    f44wta_f44_winner_take_all_signal_sf3adom_21d_base_v032_signal,
    f44wta_f44_winner_take_all_signal_sf3adom_252d_base_v033_signal,
    f44wta_f44_winner_take_all_signal_sf3bdom_252d_base_v034_signal,
    f44wta_f44_winner_take_all_signal_sf3bdom_504d_base_v035_signal,
    f44wta_f44_winner_take_all_signal_sf3ashdom_252d_base_v036_signal,
    f44wta_f44_winner_take_all_signal_sf3bshdom_504d_base_v037_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_21d_base_v038_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_63d_base_v039_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_252d_base_v040_signal,
    f44wta_f44_winner_take_all_signal_mcgxev_504d_base_v041_signal,
    f44wta_f44_winner_take_all_signal_sf3aexg_252d_base_v042_signal,
    f44wta_f44_winner_take_all_signal_sf3bexg_504d_base_v043_signal,
    f44wta_f44_winner_take_all_signal_evlevel_252d_base_v044_signal,
    f44wta_f44_winner_take_all_signal_evlevel_504d_base_v045_signal,
    f44wta_f44_winner_take_all_signal_mcxev_252d_base_v046_signal,
    f44wta_f44_winner_take_all_signal_mcxev_504d_base_v047_signal,
    f44wta_f44_winner_take_all_signal_logdom_21d_base_v048_signal,
    f44wta_f44_winner_take_all_signal_logdom_252d_base_v049_signal,
    f44wta_f44_winner_take_all_signal_logdom_504d_base_v050_signal,
    f44wta_f44_winner_take_all_signal_sf3aexg_21d_base_v051_signal,
    f44wta_f44_winner_take_all_signal_sf3aexg_63d_base_v052_signal,
    f44wta_f44_winner_take_all_signal_sf3ashexg_252d_base_v053_signal,
    f44wta_f44_winner_take_all_signal_sf3bshexg_252d_base_v054_signal,
    f44wta_f44_winner_take_all_signal_domxrev_21d_base_v055_signal,
    f44wta_f44_winner_take_all_signal_domxrev_252d_base_v056_signal,
    f44wta_f44_winner_take_all_signal_domxrev_504d_base_v057_signal,
    f44wta_f44_winner_take_all_signal_domxni_252d_base_v058_signal,
    f44wta_f44_winner_take_all_signal_domxeb_252d_base_v059_signal,
    f44wta_f44_winner_take_all_signal_domxfcf_252d_base_v060_signal,
    f44wta_f44_winner_take_all_signal_domxevvol_63d_base_v061_signal,
    f44wta_f44_winner_take_all_signal_domxevvol_252d_base_v062_signal,
    f44wta_f44_winner_take_all_signal_domxevvol_504d_base_v063_signal,
    f44wta_f44_winner_take_all_signal_domewm_63d_base_v064_signal,
    f44wta_f44_winner_take_all_signal_domewm_252d_base_v065_signal,
    f44wta_f44_winner_take_all_signal_domewm_504d_base_v066_signal,
    f44wta_f44_winner_take_all_signal_exgewm_252d_base_v067_signal,
    f44wta_f44_winner_take_all_signal_domxps_252d_base_v068_signal,
    f44wta_f44_winner_take_all_signal_evdomxpe_504d_base_v069_signal,
    f44wta_f44_winner_take_all_signal_evdomxpb_252d_base_v070_signal,
    f44wta_f44_winner_take_all_signal_megxevxmc_504d_base_v071_signal,
    f44wta_f44_winner_take_all_signal_domsq_252d_base_v072_signal,
    f44wta_f44_winner_take_all_signal_domsq_504d_base_v073_signal,
    f44wta_f44_winner_take_all_signal_domxsf3a_252d_base_v074_signal,
    f44wta_f44_winner_take_all_signal_domxsf3b_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_WINNER_TAKE_ALL_SIGNAL_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f44_winner_take_all_signal_base_001_075_claude: {n_features} features pass")
