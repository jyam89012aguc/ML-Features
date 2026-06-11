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
def _f45_network_growth_compound(marketcap, w):
    return _diff(np.log(marketcap.replace(0, np.nan)), w) / float(w)


def _f45_network_growth_superlinear(marketcap, revenue, w):
    mg = _diff(np.log(marketcap.replace(0, np.nan)), w)
    rg = _diff(np.log(revenue.replace(0, np.nan)), w)
    return mg - rg


def _f45_network_growth_acceleration(marketcap, w):
    g = _diff(np.log(marketcap.replace(0, np.nan)), w)
    return _diff(g, w)


# 21d compound × pe (rich growth network)
def f45nge_f45_network_growth_engine_compxpe_21d_base_v076_signal(marketcap, pe):
    result = _f45_network_growth_compound(marketcap, 21) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × pe
def f45nge_f45_network_growth_engine_compxpe_252d_base_v077_signal(marketcap, pe):
    result = _f45_network_growth_compound(marketcap, 252) * pe * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × evebit
def f45nge_f45_network_growth_engine_compxevebit_252d_base_v078_signal(marketcap, evebit):
    result = _f45_network_growth_compound(marketcap, 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × evebitda
def f45nge_f45_network_growth_engine_compxevebitda_252d_base_v079_signal(marketcap, evebitda):
    result = _f45_network_growth_compound(marketcap, 252) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × pb
def f45nge_f45_network_growth_engine_compxpb_252d_base_v080_signal(marketcap, pb):
    result = _f45_network_growth_compound(marketcap, 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ps
def f45nge_f45_network_growth_engine_compxps_252d_base_v081_signal(marketcap, ps):
    result = _f45_network_growth_compound(marketcap, 252) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration × marketcap
def f45nge_f45_network_growth_engine_accxmc_21d_base_v082_signal(marketcap):
    result = _f45_network_growth_acceleration(marketcap, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration × marketcap
def f45nge_f45_network_growth_engine_accxmc_252d_base_v083_signal(marketcap):
    result = _f45_network_growth_acceleration(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration × marketcap
def f45nge_f45_network_growth_engine_accxmc_504d_base_v084_signal(marketcap):
    result = _f45_network_growth_acceleration(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev acceleration × marketcap
def f45nge_f45_network_growth_engine_evaccxmc_21d_base_v085_signal(ev, marketcap):
    result = _f45_network_growth_acceleration(ev, 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev acceleration × marketcap
def f45nge_f45_network_growth_engine_evaccxmc_252d_base_v086_signal(ev, marketcap):
    result = _f45_network_growth_acceleration(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev acceleration × marketcap
def f45nge_f45_network_growth_engine_evaccxmc_504d_base_v087_signal(ev, marketcap):
    result = _f45_network_growth_acceleration(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sf3a value acceleration × marketcap
def f45nge_f45_network_growth_engine_sf3aaccxmc_252d_base_v088_signal(sf3a_value, marketcap):
    result = _f45_network_growth_acceleration(sf3a_value, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d sf3b value acceleration × marketcap
def f45nge_f45_network_growth_engine_sf3baccxmc_504d_base_v089_signal(sf3b_value, marketcap):
    result = _f45_network_growth_acceleration(sf3b_value, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × debt (leverage-fueled network)
def f45nge_f45_network_growth_engine_compxdebt_21d_base_v090_signal(marketcap, debt):
    result = _f45_network_growth_compound(marketcap, 21) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × debt
def f45nge_f45_network_growth_engine_compxdebt_252d_base_v091_signal(marketcap, debt):
    result = _f45_network_growth_compound(marketcap, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × debt
def f45nge_f45_network_growth_engine_compxdebt_504d_base_v092_signal(marketcap, debt):
    result = _f45_network_growth_compound(marketcap, 504) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × equity
def f45nge_f45_network_growth_engine_compxeq_21d_base_v093_signal(marketcap, equity):
    result = _f45_network_growth_compound(marketcap, 21) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × equity
def f45nge_f45_network_growth_engine_compxeq_252d_base_v094_signal(marketcap, equity):
    result = _f45_network_growth_compound(marketcap, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × equity
def f45nge_f45_network_growth_engine_compxeq_504d_base_v095_signal(marketcap, equity):
    result = _f45_network_growth_compound(marketcap, 504) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × assets
def f45nge_f45_network_growth_engine_compxat_252d_base_v096_signal(marketcap, assets):
    result = _f45_network_growth_compound(marketcap, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × assets
def f45nge_f45_network_growth_engine_compxat_504d_base_v097_signal(marketcap, assets):
    result = _f45_network_growth_compound(marketcap, 504) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 252d superlinear × debt
def f45nge_f45_network_growth_engine_supxdebt_252d_base_v098_signal(marketcap, revenue, debt):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d superlinear × equity
def f45nge_f45_network_growth_engine_supxeq_252d_base_v099_signal(marketcap, revenue, equity):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * equity
    return result.replace([np.inf, -np.inf], np.nan)


# 252d superlinear × assets
def f45nge_f45_network_growth_engine_supxat_252d_base_v100_signal(marketcap, revenue, assets):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * assets
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × ncfo (cash-fueled growth)
def f45nge_f45_network_growth_engine_compxncfo_21d_base_v101_signal(marketcap, ncfo):
    result = _f45_network_growth_compound(marketcap, 21) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ncfo
def f45nge_f45_network_growth_engine_compxncfo_252d_base_v102_signal(marketcap, ncfo):
    result = _f45_network_growth_compound(marketcap, 252) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × ncfo
def f45nge_f45_network_growth_engine_compxncfo_504d_base_v103_signal(marketcap, ncfo):
    result = _f45_network_growth_compound(marketcap, 504) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev compound × ev (network ev compounding)
def f45nge_f45_network_growth_engine_evcompxev_21d_base_v104_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 21) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev compound × ev
def f45nge_f45_network_growth_engine_evcompxev_252d_base_v105_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 252) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev compound × ev
def f45nge_f45_network_growth_engine_evcompxev_504d_base_v106_signal(ev, marketcap):
    result = _f45_network_growth_compound(ev, 504) * ev * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × marketcap × revenue (compound + sales)
def f45nge_f45_network_growth_engine_compxmcxrev_252d_base_v107_signal(marketcap, revenue):
    result = _f45_network_growth_compound(marketcap, 252) * marketcap * revenue / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d superlinear × marketcap × revenue
def f45nge_f45_network_growth_engine_supxmcxrev_504d_base_v108_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap * revenue / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration × ev × marketcap
def f45nge_f45_network_growth_engine_accxev_252d_base_v109_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 252) * ev * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration × ev × marketcap
def f45nge_f45_network_growth_engine_accxev_504d_base_v110_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 504) * ev * marketcap / marketcap.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × sf3a shares
def f45nge_f45_network_growth_engine_compxsf3ash_252d_base_v111_signal(marketcap, sf3a_shares):
    result = _f45_network_growth_compound(marketcap, 252) * _mean(sf3a_shares, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × sf3b shares
def f45nge_f45_network_growth_engine_compxsf3bsh_504d_base_v112_signal(marketcap, sf3b_shares):
    result = _f45_network_growth_compound(marketcap, 504) * _mean(sf3b_shares, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ev × revenue
def f45nge_f45_network_growth_engine_compxevxrev_252d_base_v113_signal(marketcap, ev, revenue):
    result = _f45_network_growth_compound(marketcap, 252) * ev * revenue / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d superlinear × ev × revenue
def f45nge_f45_network_growth_engine_supxevxrev_504d_base_v114_signal(marketcap, revenue, ev):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * ev * revenue / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d compound × marketcap × ev (network engine triple)
def f45nge_f45_network_growth_engine_triplecomp_21d_base_v115_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 21) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d triple compound network
def f45nge_f45_network_growth_engine_triplecomp_252d_base_v116_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d triple compound network
def f45nge_f45_network_growth_engine_triplecomp_504d_base_v117_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 504) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × log marketcap × ev
def f45nge_f45_network_growth_engine_complogev_252d_base_v118_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × log marketcap × ev
def f45nge_f45_network_growth_engine_complogev_504d_base_v119_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 504) * np.log(marketcap.replace(0, np.nan)) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 21d super-linear vs ncfo × marketcap
def f45nge_f45_network_growth_engine_supvsncfo_21d_base_v120_signal(marketcap, ncfo, ev):
    result = _f45_network_growth_superlinear(marketcap, ncfo, 21) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d super-linear vs ncfo × ev
def f45nge_f45_network_growth_engine_supvsncfo_252d_base_v121_signal(marketcap, ncfo, ev):
    result = _f45_network_growth_superlinear(marketcap, ncfo, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d super-linear vs ncfo × ev
def f45nge_f45_network_growth_engine_supvsncfo_504d_base_v122_signal(marketcap, ncfo, ev):
    result = _f45_network_growth_superlinear(marketcap, ncfo, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × evebit (rich growth premium network)
def f45nge_f45_network_growth_engine_compxevebit_504d_base_v123_signal(marketcap, evebit):
    result = _f45_network_growth_compound(marketcap, 504) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × evebitda
def f45nge_f45_network_growth_engine_compxevebitda_504d_base_v124_signal(marketcap, evebitda):
    result = _f45_network_growth_compound(marketcap, 504) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × pb
def f45nge_f45_network_growth_engine_compxpb_504d_base_v125_signal(marketcap, pb):
    result = _f45_network_growth_compound(marketcap, 504) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × ps
def f45nge_f45_network_growth_engine_compxps_504d_base_v126_signal(marketcap, ps):
    result = _f45_network_growth_compound(marketcap, 504) * ps * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × revenue × marketcap composite
def f45nge_f45_network_growth_engine_compxrevxmc_252d_base_v127_signal(marketcap, revenue):
    result = _f45_network_growth_compound(marketcap, 252) * revenue * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × ebitda × marketcap composite
def f45nge_f45_network_growth_engine_compxebxmc_504d_base_v128_signal(marketcap, ebitda):
    result = _f45_network_growth_compound(marketcap, 504) * ebitda * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d superlinear × marketcap × ev (network premium x size)
def f45nge_f45_network_growth_engine_supxmcxev_252d_base_v129_signal(marketcap, revenue, ev):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d superlinear × marketcap × ev
def f45nge_f45_network_growth_engine_supxmcxev_504d_base_v130_signal(marketcap, revenue, ev):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × log ev × marketcap
def f45nge_f45_network_growth_engine_complogevxmc_252d_base_v131_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * np.log(ev.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × log ev × marketcap
def f45nge_f45_network_growth_engine_complogevxmc_504d_base_v132_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 504) * np.log(ev.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × sqrt(mc * ev)
def f45nge_f45_network_growth_engine_compxsqrt_252d_base_v133_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * np.sqrt(marketcap.abs() * ev.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d superlinear × sqrt(mc * ev)
def f45nge_f45_network_growth_engine_supxsqrt_504d_base_v134_signal(marketcap, revenue, ev):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * np.sqrt(marketcap.abs() * ev.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound z-score × marketcap
def f45nge_f45_network_growth_engine_compz_252d_base_v135_signal(marketcap):
    base_ = _f45_network_growth_compound(marketcap, 252)
    result = _z(base_, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound z-score × marketcap
def f45nge_f45_network_growth_engine_compz_504d_base_v136_signal(marketcap):
    base_ = _f45_network_growth_compound(marketcap, 504)
    result = _z(base_, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d superlinear z × marketcap
def f45nge_f45_network_growth_engine_supz_252d_base_v137_signal(marketcap, revenue):
    base_ = _f45_network_growth_superlinear(marketcap, revenue, 252)
    result = _z(base_, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration z × marketcap
def f45nge_f45_network_growth_engine_accz_504d_base_v138_signal(marketcap):
    base_ = _f45_network_growth_acceleration(marketcap, 504)
    result = _z(base_, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × volume of sf3a value × marketcap
def f45nge_f45_network_growth_engine_compxsf3aval_252d_base_v139_signal(marketcap, sf3a_value):
    result = _f45_network_growth_compound(marketcap, 252) * sf3a_value
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ev z (rich engine)
def f45nge_f45_network_growth_engine_compxevz_252d_base_v140_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * _z(ev, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × ev z (rich engine 504d)
def f45nge_f45_network_growth_engine_compxevz_504d_base_v141_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 504) * _z(ev, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × marketcap z
def f45nge_f45_network_growth_engine_compxmcz_252d_base_v142_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 252) * _z(marketcap, 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × marketcap z
def f45nge_f45_network_growth_engine_compxmcz_504d_base_v143_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 504) * _z(marketcap, 504) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration × log marketcap
def f45nge_f45_network_growth_engine_accxlogmc_252d_base_v144_signal(marketcap):
    result = _f45_network_growth_acceleration(marketcap, 252) * np.log(marketcap.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration × log ev
def f45nge_f45_network_growth_engine_accxlogev_504d_base_v145_signal(marketcap, ev):
    result = _f45_network_growth_acceleration(marketcap, 504) * np.log(ev.replace(0, np.nan)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d compound × ev std (volatile network)
def f45nge_f45_network_growth_engine_compxevstd_252d_base_v146_signal(marketcap, ev):
    result = _f45_network_growth_compound(marketcap, 252) * _std(ev, 252) * marketcap / ev.replace(0, np.nan).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d compound × marketcap std
def f45nge_f45_network_growth_engine_compxmcstd_504d_base_v147_signal(marketcap):
    result = _f45_network_growth_compound(marketcap, 504) * _std(marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d superlinear × marketcap squared
def f45nge_f45_network_growth_engine_supxmcsq_252d_base_v148_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 252) * marketcap * marketcap.abs() / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d superlinear × marketcap squared
def f45nge_f45_network_growth_engine_supxmcsq_504d_base_v149_signal(marketcap, revenue):
    result = _f45_network_growth_superlinear(marketcap, revenue, 504) * marketcap * marketcap.abs() / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite engine: compound × superlinear × marketcap × ev
def f45nge_f45_network_growth_engine_compositeengine_252d_base_v150_signal(marketcap, revenue, ev):
    c = _f45_network_growth_compound(marketcap, 252)
    s = _f45_network_growth_superlinear(marketcap, revenue, 252)
    result = c * s * marketcap * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45nge_f45_network_growth_engine_compxpe_21d_base_v076_signal,
    f45nge_f45_network_growth_engine_compxpe_252d_base_v077_signal,
    f45nge_f45_network_growth_engine_compxevebit_252d_base_v078_signal,
    f45nge_f45_network_growth_engine_compxevebitda_252d_base_v079_signal,
    f45nge_f45_network_growth_engine_compxpb_252d_base_v080_signal,
    f45nge_f45_network_growth_engine_compxps_252d_base_v081_signal,
    f45nge_f45_network_growth_engine_accxmc_21d_base_v082_signal,
    f45nge_f45_network_growth_engine_accxmc_252d_base_v083_signal,
    f45nge_f45_network_growth_engine_accxmc_504d_base_v084_signal,
    f45nge_f45_network_growth_engine_evaccxmc_21d_base_v085_signal,
    f45nge_f45_network_growth_engine_evaccxmc_252d_base_v086_signal,
    f45nge_f45_network_growth_engine_evaccxmc_504d_base_v087_signal,
    f45nge_f45_network_growth_engine_sf3aaccxmc_252d_base_v088_signal,
    f45nge_f45_network_growth_engine_sf3baccxmc_504d_base_v089_signal,
    f45nge_f45_network_growth_engine_compxdebt_21d_base_v090_signal,
    f45nge_f45_network_growth_engine_compxdebt_252d_base_v091_signal,
    f45nge_f45_network_growth_engine_compxdebt_504d_base_v092_signal,
    f45nge_f45_network_growth_engine_compxeq_21d_base_v093_signal,
    f45nge_f45_network_growth_engine_compxeq_252d_base_v094_signal,
    f45nge_f45_network_growth_engine_compxeq_504d_base_v095_signal,
    f45nge_f45_network_growth_engine_compxat_252d_base_v096_signal,
    f45nge_f45_network_growth_engine_compxat_504d_base_v097_signal,
    f45nge_f45_network_growth_engine_supxdebt_252d_base_v098_signal,
    f45nge_f45_network_growth_engine_supxeq_252d_base_v099_signal,
    f45nge_f45_network_growth_engine_supxat_252d_base_v100_signal,
    f45nge_f45_network_growth_engine_compxncfo_21d_base_v101_signal,
    f45nge_f45_network_growth_engine_compxncfo_252d_base_v102_signal,
    f45nge_f45_network_growth_engine_compxncfo_504d_base_v103_signal,
    f45nge_f45_network_growth_engine_evcompxev_21d_base_v104_signal,
    f45nge_f45_network_growth_engine_evcompxev_252d_base_v105_signal,
    f45nge_f45_network_growth_engine_evcompxev_504d_base_v106_signal,
    f45nge_f45_network_growth_engine_compxmcxrev_252d_base_v107_signal,
    f45nge_f45_network_growth_engine_supxmcxrev_504d_base_v108_signal,
    f45nge_f45_network_growth_engine_accxev_252d_base_v109_signal,
    f45nge_f45_network_growth_engine_accxev_504d_base_v110_signal,
    f45nge_f45_network_growth_engine_compxsf3ash_252d_base_v111_signal,
    f45nge_f45_network_growth_engine_compxsf3bsh_504d_base_v112_signal,
    f45nge_f45_network_growth_engine_compxevxrev_252d_base_v113_signal,
    f45nge_f45_network_growth_engine_supxevxrev_504d_base_v114_signal,
    f45nge_f45_network_growth_engine_triplecomp_21d_base_v115_signal,
    f45nge_f45_network_growth_engine_triplecomp_252d_base_v116_signal,
    f45nge_f45_network_growth_engine_triplecomp_504d_base_v117_signal,
    f45nge_f45_network_growth_engine_complogev_252d_base_v118_signal,
    f45nge_f45_network_growth_engine_complogev_504d_base_v119_signal,
    f45nge_f45_network_growth_engine_supvsncfo_21d_base_v120_signal,
    f45nge_f45_network_growth_engine_supvsncfo_252d_base_v121_signal,
    f45nge_f45_network_growth_engine_supvsncfo_504d_base_v122_signal,
    f45nge_f45_network_growth_engine_compxevebit_504d_base_v123_signal,
    f45nge_f45_network_growth_engine_compxevebitda_504d_base_v124_signal,
    f45nge_f45_network_growth_engine_compxpb_504d_base_v125_signal,
    f45nge_f45_network_growth_engine_compxps_504d_base_v126_signal,
    f45nge_f45_network_growth_engine_compxrevxmc_252d_base_v127_signal,
    f45nge_f45_network_growth_engine_compxebxmc_504d_base_v128_signal,
    f45nge_f45_network_growth_engine_supxmcxev_252d_base_v129_signal,
    f45nge_f45_network_growth_engine_supxmcxev_504d_base_v130_signal,
    f45nge_f45_network_growth_engine_complogevxmc_252d_base_v131_signal,
    f45nge_f45_network_growth_engine_complogevxmc_504d_base_v132_signal,
    f45nge_f45_network_growth_engine_compxsqrt_252d_base_v133_signal,
    f45nge_f45_network_growth_engine_supxsqrt_504d_base_v134_signal,
    f45nge_f45_network_growth_engine_compz_252d_base_v135_signal,
    f45nge_f45_network_growth_engine_compz_504d_base_v136_signal,
    f45nge_f45_network_growth_engine_supz_252d_base_v137_signal,
    f45nge_f45_network_growth_engine_accz_504d_base_v138_signal,
    f45nge_f45_network_growth_engine_compxsf3aval_252d_base_v139_signal,
    f45nge_f45_network_growth_engine_compxevz_252d_base_v140_signal,
    f45nge_f45_network_growth_engine_compxevz_504d_base_v141_signal,
    f45nge_f45_network_growth_engine_compxmcz_252d_base_v142_signal,
    f45nge_f45_network_growth_engine_compxmcz_504d_base_v143_signal,
    f45nge_f45_network_growth_engine_accxlogmc_252d_base_v144_signal,
    f45nge_f45_network_growth_engine_accxlogev_504d_base_v145_signal,
    f45nge_f45_network_growth_engine_compxevstd_252d_base_v146_signal,
    f45nge_f45_network_growth_engine_compxmcstd_504d_base_v147_signal,
    f45nge_f45_network_growth_engine_supxmcsq_252d_base_v148_signal,
    f45nge_f45_network_growth_engine_supxmcsq_504d_base_v149_signal,
    f45nge_f45_network_growth_engine_compositeengine_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F45_NETWORK_GROWTH_ENGINE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f45_network_growth_compound", "_f45_network_growth_superlinear",
                         "_f45_network_growth_acceleration")
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
    print(f"OK f45_network_growth_engine_base_076_150_claude: {n_features} features pass")
