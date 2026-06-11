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


# 21d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_21d_base_v076_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 21) * _f44_winner_take_all_dominance(ev, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_63d_base_v077_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 63) * _f44_winner_take_all_dominance(ev, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_252d_base_v078_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _f44_winner_take_all_dominance(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap × ev dominance composite
def f44wta_f44_winner_take_all_signal_mcevdom_504d_base_v079_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 504) * _f44_winner_take_all_dominance(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a value × marketcap winner composite
def f44wta_f44_winner_take_all_signal_sf3awin_21d_base_v080_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_value, 21) * _f44_winner_take_all_dominance(marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value × marketcap winner composite
def f44wta_f44_winner_take_all_signal_sf3awin_252d_base_v081_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_value, 252) * _f44_winner_take_all_dominance(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value × marketcap winner composite
def f44wta_f44_winner_take_all_signal_sf3bwin_504d_base_v082_signal(sf3b_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3b_value, 504) * _f44_winner_take_all_dominance(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_21d_base_v083_signal(marketcap, revenue):
    result = _f44_winner_take_all_growth_excess(marketcap, 21) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap excess growth × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_63d_base_v084_signal(marketcap, revenue):
    result = _f44_winner_take_all_growth_excess(marketcap, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_252d_base_v085_signal(marketcap, revenue):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × revenue
def f44wta_f44_winner_take_all_signal_mcexgxrev_504d_base_v086_signal(marketcap, revenue):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth × ebitda
def f44wta_f44_winner_take_all_signal_mcexgxeb_21d_base_v087_signal(marketcap, ebitda):
    result = _f44_winner_take_all_growth_excess(marketcap, 21) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × ebitda
def f44wta_f44_winner_take_all_signal_mcexgxeb_252d_base_v088_signal(marketcap, ebitda):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × ebitda
def f44wta_f44_winner_take_all_signal_mcexgxeb_504d_base_v089_signal(marketcap, ebitda):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × netinc
def f44wta_f44_winner_take_all_signal_mcexgxni_252d_base_v090_signal(marketcap, netinc):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * netinc
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × fcf
def f44wta_f44_winner_take_all_signal_mcexgxfcf_504d_base_v091_signal(marketcap, fcf):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × marketcap squared (super-size dominance)
def f44wta_f44_winner_take_all_signal_domxmcsq_21d_base_v092_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 21) * marketcap * marketcap.abs() / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × marketcap squared
def f44wta_f44_winner_take_all_signal_domxmcsq_252d_base_v093_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * marketcap * marketcap.abs() / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × marketcap squared
def f44wta_f44_winner_take_all_signal_domxmcsq_504d_base_v094_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 504) * marketcap * marketcap.abs() / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev dominance × ev squared
def f44wta_f44_winner_take_all_signal_evdomxevsq_21d_base_v095_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 21) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev dominance × ev squared
def f44wta_f44_winner_take_all_signal_evdomxevsq_252d_base_v096_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 252) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev dominance × ev squared
def f44wta_f44_winner_take_all_signal_evdomxevsq_504d_base_v097_signal(ev, marketcap):
    result = _f44_winner_take_all_dominance(ev, 504) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap level × log marketcap
def f44wta_f44_winner_take_all_signal_levellog_21d_base_v098_signal(marketcap):
    result = _f44_winner_take_all_mc_level(marketcap, 21) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap level × log marketcap
def f44wta_f44_winner_take_all_signal_levellog_252d_base_v099_signal(marketcap):
    result = _f44_winner_take_all_mc_level(marketcap, 252) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap level × log marketcap
def f44wta_f44_winner_take_all_signal_levellog_504d_base_v100_signal(marketcap):
    result = _f44_winner_take_all_mc_level(marketcap, 504) * np.log(marketcap.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × pe
def f44wta_f44_winner_take_all_signal_domxpe_21d_base_v101_signal(marketcap, pe):
    result = _f44_winner_take_all_dominance(marketcap, 21) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × evebit
def f44wta_f44_winner_take_all_signal_domxevebit_252d_base_v102_signal(marketcap, evebit):
    result = _f44_winner_take_all_dominance(marketcap, 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × evebitda
def f44wta_f44_winner_take_all_signal_domxevebitda_504d_base_v103_signal(marketcap, evebitda):
    result = _f44_winner_take_all_dominance(marketcap, 504) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × pb
def f44wta_f44_winner_take_all_signal_domxpb_252d_base_v104_signal(marketcap, pb):
    result = _f44_winner_take_all_dominance(marketcap, 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × ps
def f44wta_f44_winner_take_all_signal_domxps2_252d_base_v105_signal(marketcap, ps):
    result = _f44_winner_take_all_dominance(marketcap, 252) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth × pe
def f44wta_f44_winner_take_all_signal_exgxpe_252d_base_v106_signal(marketcap, pe):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × evebit
def f44wta_f44_winner_take_all_signal_exgxevebit_252d_base_v107_signal(marketcap, evebit):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × ps
def f44wta_f44_winner_take_all_signal_exgxps_504d_base_v108_signal(marketcap, ps):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a shares dominance × sf3a value (institutional concentration)
def f44wta_f44_winner_take_all_signal_sf3aconc_21d_base_v109_signal(sf3a_shares, sf3a_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_shares, 21) * _mean(sf3a_value, 21) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a shares dominance × sf3a value
def f44wta_f44_winner_take_all_signal_sf3aconc_252d_base_v110_signal(sf3a_shares, sf3a_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3a_shares, 252) * _mean(sf3a_value, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3b shares dominance × sf3b value
def f44wta_f44_winner_take_all_signal_sf3bconc_252d_base_v111_signal(sf3b_shares, sf3b_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3b_shares, 252) * _mean(sf3b_value, 252) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b shares dominance × sf3b value
def f44wta_f44_winner_take_all_signal_sf3bconc_504d_base_v112_signal(sf3b_shares, sf3b_value, marketcap):
    result = _f44_winner_take_all_dominance(sf3b_shares, 504) * _mean(sf3b_value, 504) * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev excess growth × marketcap × ev composite
def f44wta_f44_winner_take_all_signal_evexgxmc_21d_base_v113_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 21) * marketcap * ev / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev excess growth × marketcap × ev composite
def f44wta_f44_winner_take_all_signal_evexgxmc_252d_base_v114_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 252) * marketcap * ev / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev excess growth × marketcap × ev composite
def f44wta_f44_winner_take_all_signal_evexgxmc_504d_base_v115_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 504) * marketcap * ev / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth × log marketcap
def f44wta_f44_winner_take_all_signal_exgxlogmc_21d_base_v116_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 21) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth × log marketcap
def f44wta_f44_winner_take_all_signal_exgxlogmc_252d_base_v117_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth × log marketcap
def f44wta_f44_winner_take_all_signal_exgxlogmc_504d_base_v118_signal(marketcap):
    result = _f44_winner_take_all_growth_excess(marketcap, 504) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × marketcap × revenue
def f44wta_f44_winner_take_all_signal_winnerops_21d_base_v119_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 21) * marketcap * revenue / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × marketcap × revenue
def f44wta_f44_winner_take_all_signal_winnerops_252d_base_v120_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 252) * marketcap * revenue / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × marketcap × revenue
def f44wta_f44_winner_take_all_signal_winnerops_504d_base_v121_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 504) * marketcap * revenue / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap excess growth squared × ev (super-acceleration)
def f44wta_f44_winner_take_all_signal_exgsq_21d_base_v122_signal(marketcap, ev):
    g = _f44_winner_take_all_growth_excess(marketcap, 21)
    result = g * g.abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth squared × ev
def f44wta_f44_winner_take_all_signal_exgsq_252d_base_v123_signal(marketcap, ev):
    g = _f44_winner_take_all_growth_excess(marketcap, 252)
    result = g * g.abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap excess growth squared × ev
def f44wta_f44_winner_take_all_signal_exgsq_504d_base_v124_signal(marketcap, ev):
    g = _f44_winner_take_all_growth_excess(marketcap, 504)
    result = g * g.abs() * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap excess growth squared × marketcap
def f44wta_f44_winner_take_all_signal_exgsqxmc_252d_base_v125_signal(marketcap):
    g = _f44_winner_take_all_growth_excess(marketcap, 252)
    result = g * g.abs() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × revenue × marketcap (winner-rev composite)
def f44wta_f44_winner_take_all_signal_winrev_21d_base_v126_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 21) * revenue * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × revenue × marketcap
def f44wta_f44_winner_take_all_signal_winrev_252d_base_v127_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 252) * revenue * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × revenue × marketcap
def f44wta_f44_winner_take_all_signal_winrev_504d_base_v128_signal(marketcap, revenue):
    result = _f44_winner_take_all_dominance(marketcap, 504) * revenue * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite winner: dominance × excess growth × marketcap
def f44wta_f44_winner_take_all_signal_compwin_252d_base_v129_signal(marketcap):
    result = _f44_winner_take_all_dominance(marketcap, 252) * _f44_winner_take_all_growth_excess(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite winner: dominance × excess growth × ev
def f44wta_f44_winner_take_all_signal_compwin_504d_base_v130_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 504) * _f44_winner_take_all_growth_excess(marketcap, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sf3a value excess growth × sf3a value × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexgxv_21d_base_v131_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3a_value, 21) * sf3a_value * marketcap / sf3a_value.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value excess growth × sf3a value × marketcap
def f44wta_f44_winner_take_all_signal_sf3aexgxv_252d_base_v132_signal(sf3a_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3a_value, 252) * sf3a_value * marketcap / sf3a_value.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value excess growth × sf3b value × marketcap
def f44wta_f44_winner_take_all_signal_sf3bexgxv_504d_base_v133_signal(sf3b_value, marketcap):
    result = _f44_winner_take_all_growth_excess(sf3b_value, 504) * sf3b_value * marketcap / sf3b_value.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × ev squared (winner-EV super)
def f44wta_f44_winner_take_all_signal_winev2_252d_base_v134_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 252) * ev * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × ev squared
def f44wta_f44_winner_take_all_signal_winev2_504d_base_v135_signal(marketcap, ev):
    result = _f44_winner_take_all_dominance(marketcap, 504) * ev * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev excess growth × ev × marketcap composite
def f44wta_f44_winner_take_all_signal_evexgxev_21d_base_v136_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 21) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev excess growth × ev × marketcap
def f44wta_f44_winner_take_all_signal_evexgxev_252d_base_v137_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 252) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev excess growth × ev × marketcap
def f44wta_f44_winner_take_all_signal_evexgxev_504d_base_v138_signal(ev, marketcap):
    result = _f44_winner_take_all_growth_excess(ev, 504) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × debt
def f44wta_f44_winner_take_all_signal_domxdebt_21d_base_v139_signal(marketcap, debt):
    result = _f44_winner_take_all_dominance(marketcap, 21) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × debt
def f44wta_f44_winner_take_all_signal_domxdebt_252d_base_v140_signal(marketcap, debt):
    result = _f44_winner_take_all_dominance(marketcap, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × debt
def f44wta_f44_winner_take_all_signal_domxdebt_504d_base_v141_signal(marketcap, debt):
    result = _f44_winner_take_all_dominance(marketcap, 504) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × equity
def f44wta_f44_winner_take_all_signal_domxeq_21d_base_v142_signal(marketcap, equity):
    result = _f44_winner_take_all_dominance(marketcap, 21) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × equity
def f44wta_f44_winner_take_all_signal_domxeq_252d_base_v143_signal(marketcap, equity):
    result = _f44_winner_take_all_dominance(marketcap, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × equity
def f44wta_f44_winner_take_all_signal_domxeq_504d_base_v144_signal(marketcap, equity):
    result = _f44_winner_take_all_dominance(marketcap, 504) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap dominance × assets
def f44wta_f44_winner_take_all_signal_domxat_21d_base_v145_signal(marketcap, assets):
    result = _f44_winner_take_all_dominance(marketcap, 21) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap dominance × assets
def f44wta_f44_winner_take_all_signal_domxat_252d_base_v146_signal(marketcap, assets):
    result = _f44_winner_take_all_dominance(marketcap, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap dominance × assets
def f44wta_f44_winner_take_all_signal_domxat_504d_base_v147_signal(marketcap, assets):
    result = _f44_winner_take_all_dominance(marketcap, 504) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev dominance × revenue × marketcap
def f44wta_f44_winner_take_all_signal_evdomxrev_252d_base_v148_signal(ev, revenue, marketcap):
    result = _f44_winner_take_all_dominance(ev, 252) * revenue * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev dominance × ebitda × marketcap
def f44wta_f44_winner_take_all_signal_evdomxeb_504d_base_v149_signal(ev, ebitda, marketcap):
    result = _f44_winner_take_all_dominance(ev, 504) * ebitda * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite super-winner: dom × excess × ev × marketcap
def f44wta_f44_winner_take_all_signal_superwin_252d_base_v150_signal(marketcap, ev):
    d = _f44_winner_take_all_dominance(marketcap, 252)
    g = _f44_winner_take_all_growth_excess(marketcap, 252)
    result = d * g * ev * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44wta_f44_winner_take_all_signal_mcevdom_21d_base_v076_signal,
    f44wta_f44_winner_take_all_signal_mcevdom_63d_base_v077_signal,
    f44wta_f44_winner_take_all_signal_mcevdom_252d_base_v078_signal,
    f44wta_f44_winner_take_all_signal_mcevdom_504d_base_v079_signal,
    f44wta_f44_winner_take_all_signal_sf3awin_21d_base_v080_signal,
    f44wta_f44_winner_take_all_signal_sf3awin_252d_base_v081_signal,
    f44wta_f44_winner_take_all_signal_sf3bwin_504d_base_v082_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_21d_base_v083_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_63d_base_v084_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_252d_base_v085_signal,
    f44wta_f44_winner_take_all_signal_mcexgxrev_504d_base_v086_signal,
    f44wta_f44_winner_take_all_signal_mcexgxeb_21d_base_v087_signal,
    f44wta_f44_winner_take_all_signal_mcexgxeb_252d_base_v088_signal,
    f44wta_f44_winner_take_all_signal_mcexgxeb_504d_base_v089_signal,
    f44wta_f44_winner_take_all_signal_mcexgxni_252d_base_v090_signal,
    f44wta_f44_winner_take_all_signal_mcexgxfcf_504d_base_v091_signal,
    f44wta_f44_winner_take_all_signal_domxmcsq_21d_base_v092_signal,
    f44wta_f44_winner_take_all_signal_domxmcsq_252d_base_v093_signal,
    f44wta_f44_winner_take_all_signal_domxmcsq_504d_base_v094_signal,
    f44wta_f44_winner_take_all_signal_evdomxevsq_21d_base_v095_signal,
    f44wta_f44_winner_take_all_signal_evdomxevsq_252d_base_v096_signal,
    f44wta_f44_winner_take_all_signal_evdomxevsq_504d_base_v097_signal,
    f44wta_f44_winner_take_all_signal_levellog_21d_base_v098_signal,
    f44wta_f44_winner_take_all_signal_levellog_252d_base_v099_signal,
    f44wta_f44_winner_take_all_signal_levellog_504d_base_v100_signal,
    f44wta_f44_winner_take_all_signal_domxpe_21d_base_v101_signal,
    f44wta_f44_winner_take_all_signal_domxevebit_252d_base_v102_signal,
    f44wta_f44_winner_take_all_signal_domxevebitda_504d_base_v103_signal,
    f44wta_f44_winner_take_all_signal_domxpb_252d_base_v104_signal,
    f44wta_f44_winner_take_all_signal_domxps2_252d_base_v105_signal,
    f44wta_f44_winner_take_all_signal_exgxpe_252d_base_v106_signal,
    f44wta_f44_winner_take_all_signal_exgxevebit_252d_base_v107_signal,
    f44wta_f44_winner_take_all_signal_exgxps_504d_base_v108_signal,
    f44wta_f44_winner_take_all_signal_sf3aconc_21d_base_v109_signal,
    f44wta_f44_winner_take_all_signal_sf3aconc_252d_base_v110_signal,
    f44wta_f44_winner_take_all_signal_sf3bconc_252d_base_v111_signal,
    f44wta_f44_winner_take_all_signal_sf3bconc_504d_base_v112_signal,
    f44wta_f44_winner_take_all_signal_evexgxmc_21d_base_v113_signal,
    f44wta_f44_winner_take_all_signal_evexgxmc_252d_base_v114_signal,
    f44wta_f44_winner_take_all_signal_evexgxmc_504d_base_v115_signal,
    f44wta_f44_winner_take_all_signal_exgxlogmc_21d_base_v116_signal,
    f44wta_f44_winner_take_all_signal_exgxlogmc_252d_base_v117_signal,
    f44wta_f44_winner_take_all_signal_exgxlogmc_504d_base_v118_signal,
    f44wta_f44_winner_take_all_signal_winnerops_21d_base_v119_signal,
    f44wta_f44_winner_take_all_signal_winnerops_252d_base_v120_signal,
    f44wta_f44_winner_take_all_signal_winnerops_504d_base_v121_signal,
    f44wta_f44_winner_take_all_signal_exgsq_21d_base_v122_signal,
    f44wta_f44_winner_take_all_signal_exgsq_252d_base_v123_signal,
    f44wta_f44_winner_take_all_signal_exgsq_504d_base_v124_signal,
    f44wta_f44_winner_take_all_signal_exgsqxmc_252d_base_v125_signal,
    f44wta_f44_winner_take_all_signal_winrev_21d_base_v126_signal,
    f44wta_f44_winner_take_all_signal_winrev_252d_base_v127_signal,
    f44wta_f44_winner_take_all_signal_winrev_504d_base_v128_signal,
    f44wta_f44_winner_take_all_signal_compwin_252d_base_v129_signal,
    f44wta_f44_winner_take_all_signal_compwin_504d_base_v130_signal,
    f44wta_f44_winner_take_all_signal_sf3aexgxv_21d_base_v131_signal,
    f44wta_f44_winner_take_all_signal_sf3aexgxv_252d_base_v132_signal,
    f44wta_f44_winner_take_all_signal_sf3bexgxv_504d_base_v133_signal,
    f44wta_f44_winner_take_all_signal_winev2_252d_base_v134_signal,
    f44wta_f44_winner_take_all_signal_winev2_504d_base_v135_signal,
    f44wta_f44_winner_take_all_signal_evexgxev_21d_base_v136_signal,
    f44wta_f44_winner_take_all_signal_evexgxev_252d_base_v137_signal,
    f44wta_f44_winner_take_all_signal_evexgxev_504d_base_v138_signal,
    f44wta_f44_winner_take_all_signal_domxdebt_21d_base_v139_signal,
    f44wta_f44_winner_take_all_signal_domxdebt_252d_base_v140_signal,
    f44wta_f44_winner_take_all_signal_domxdebt_504d_base_v141_signal,
    f44wta_f44_winner_take_all_signal_domxeq_21d_base_v142_signal,
    f44wta_f44_winner_take_all_signal_domxeq_252d_base_v143_signal,
    f44wta_f44_winner_take_all_signal_domxeq_504d_base_v144_signal,
    f44wta_f44_winner_take_all_signal_domxat_21d_base_v145_signal,
    f44wta_f44_winner_take_all_signal_domxat_252d_base_v146_signal,
    f44wta_f44_winner_take_all_signal_domxat_504d_base_v147_signal,
    f44wta_f44_winner_take_all_signal_evdomxrev_252d_base_v148_signal,
    f44wta_f44_winner_take_all_signal_evdomxeb_504d_base_v149_signal,
    f44wta_f44_winner_take_all_signal_superwin_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_WINNER_TAKE_ALL_SIGNAL_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f44_winner_take_all_signal_base_076_150_claude: {n_features} features pass")
