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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f23_cashflow_traj(s, w):
    return s.diff(periods=w) / s.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f23_fcf_growth(fcf, w):
    base = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f23_fcf_acceleration(fcf, w):
    g1 = _f23_fcf_growth(fcf, w)
    return g1.diff(periods=w)


# 252d FCF growth scaled by current debt
def f23cft_f23_cash_flow_trajectory_fcfgrowthxdebt_252d_base_v076_signal(fcf, debt, closeadj):
    result = _f23_fcf_growth(fcf, 252) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory scaled by current debt
def f23cft_f23_cash_flow_trajectory_ncfotrajxdebt_63d_base_v077_signal(ncfo, debt, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * debt
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth scaled by gross profit
def f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_252d_base_v078_signal(fcf, gp, closeadj):
    result = _f23_fcf_growth(fcf, 252) * gp
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth scaled by gross profit
def f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_63d_base_v079_signal(fcf, gp, closeadj):
    result = _f23_fcf_growth(fcf, 63) * gp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth scaled by opinc
def f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_252d_base_v080_signal(fcf, opinc, closeadj):
    result = _f23_fcf_growth(fcf, 252) * opinc
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth scaled by opinc
def f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_63d_base_v081_signal(fcf, opinc, closeadj):
    result = _f23_fcf_growth(fcf, 63) * opinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × eps
def f23cft_f23_cash_flow_trajectory_fcfgrowthxeps_252d_base_v082_signal(fcf, eps, closeadj):
    result = _f23_fcf_growth(fcf, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory × eps
def f23cft_f23_cash_flow_trajectory_ncfotrajxeps_63d_base_v083_signal(ncfo, eps, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × workingcapital
def f23cft_f23_cash_flow_trajectory_fcfgrowthxwc_252d_base_v084_signal(fcf, workingcapital, closeadj):
    result = _f23_fcf_growth(fcf, 252) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory × workingcapital
def f23cft_f23_cash_flow_trajectory_ncfotrajxwc_63d_base_v085_signal(ncfo, workingcapital, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth × current ratio
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_21d_base_v086_signal(fcf, currentratio, closeadj):
    result = _f23_fcf_growth(fcf, 21) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × current ratio
def f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_252d_base_v087_signal(fcf, currentratio, closeadj):
    result = _f23_fcf_growth(fcf, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory × current ratio
def f23cft_f23_cash_flow_trajectory_ncfotrajxcr_252d_base_v088_signal(ncfo, currentratio, closeadj):
    result = _f23_cashflow_traj(ncfo, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth × liabilities
def f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_63d_base_v089_signal(fcf, liabilities, closeadj):
    result = _f23_fcf_growth(fcf, 63) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × liabilities
def f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_252d_base_v090_signal(fcf, liabilities, closeadj):
    result = _f23_fcf_growth(fcf, 252) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory × retearn
def f23cft_f23_cash_flow_trajectory_ncfotrajxre_63d_base_v091_signal(ncfo, retearn, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × retained earnings
def f23cft_f23_cash_flow_trajectory_fcfgrowthxre_252d_base_v092_signal(fcf, retearn, closeadj):
    result = _f23_fcf_growth(fcf, 252) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory × intexp (interest cost context)
def f23cft_f23_cash_flow_trajectory_ncfotrajxintexp_63d_base_v093_signal(ncfo, intexp, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × intexp
def f23cft_f23_cash_flow_trajectory_fcfgrowthxintexp_252d_base_v094_signal(fcf, intexp, closeadj):
    result = _f23_fcf_growth(fcf, 252) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × taxexp
def f23cft_f23_cash_flow_trajectory_fcfgrowthxtax_252d_base_v095_signal(fcf, taxexp, closeadj):
    result = _f23_fcf_growth(fcf, 252) * taxexp
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo trajectory squared (severity)
def f23cft_f23_cash_flow_trajectory_ncfotrajsq_21d_base_v096_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory squared
def f23cft_f23_cash_flow_trajectory_ncfotrajsq_252d_base_v097_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory area
def f23cft_f23_cash_flow_trajectory_ncfotrajarea_63d_base_v098_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 21).abs()
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory area
def f23cft_f23_cash_flow_trajectory_ncfotrajarea_252d_base_v099_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncfo trajectory area
def f23cft_f23_cash_flow_trajectory_ncfotrajarea_504d_base_v100_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth - 252d ncfo trajectory (FCF advantage)
def f23cft_f23_cash_flow_trajectory_fcfminusncfo_252d_base_v101_signal(fcf, ncfo, closeadj):
    result = (_f23_fcf_growth(fcf, 252) - _f23_cashflow_traj(ncfo, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth - 63d ncfo trajectory
def f23cft_f23_cash_flow_trajectory_fcfminusncfo_63d_base_v102_signal(fcf, ncfo, closeadj):
    result = (_f23_fcf_growth(fcf, 63) - _f23_cashflow_traj(ncfo, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth + 252d ncfo trajectory composite
def f23cft_f23_cash_flow_trajectory_fcfplusncfo_252d_base_v103_signal(fcf, ncfo, closeadj):
    result = (_f23_fcf_growth(fcf, 252) + _f23_cashflow_traj(ncfo, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst (most negative) FCF growth × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthworst_504d_base_v104_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    result = g.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding best FCF growth × close
def f23cft_f23_cash_flow_trajectory_fcfgrowthbest_504d_base_v105_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    result = g.expanding(min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max ncfo trajectory in 63d
def f23cft_f23_cash_flow_trajectory_ncfotrajmax_63d_base_v106_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max ncfo trajectory in 252d
def f23cft_f23_cash_flow_trajectory_ncfotrajmax_252d_base_v107_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min ncfo trajectory in 63d (worst contraction)
def f23cft_f23_cash_flow_trajectory_ncfotrajmin_63d_base_v108_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 21).rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min ncfo trajectory in 252d
def f23cft_f23_cash_flow_trajectory_ncfotrajmin_252d_base_v109_signal(ncfo, closeadj):
    result = _f23_cashflow_traj(ncfo, 63).rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth EMA × ebitda (smoothed FCF level)
def f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_21d_base_v110_signal(fcf, ebitda, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    result = g.ewm(span=21, adjust=False).mean() * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth EMA × ebitda
def f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_252d_base_v111_signal(fcf, ebitda, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    result = g.ewm(span=252, adjust=False).mean() * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d cumulative FCF growth area scaled by mcap
def f23cft_f23_cash_flow_trajectory_fcfgrowthareaxmcap_252d_base_v112_signal(fcf, closeadj, sharesbas):
    g = _f23_fcf_growth(fcf, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory anomaly (vs 252d mean)
def f23cft_f23_cash_flow_trajectory_ncfotrajanom_63d_base_v113_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    base = _mean(_f23_cashflow_traj(ncfo, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory anomaly (vs 504d mean)
def f23cft_f23_cash_flow_trajectory_ncfotrajanom_252d_base_v114_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    base = _mean(_f23_cashflow_traj(ncfo, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth anomaly (vs 252d mean)
def f23cft_f23_cash_flow_trajectory_fcfgrowthanom_63d_base_v115_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 63)
    base = _mean(_f23_fcf_growth(fcf, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth anomaly (vs 504d mean)
def f23cft_f23_cash_flow_trajectory_fcfgrowthanom_252d_base_v116_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    base = _mean(_f23_fcf_growth(fcf, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth × revenue × closeadj (revenue-weighted growth)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_21d_base_v117_signal(fcf, revenue, closeadj):
    result = _f23_fcf_growth(fcf, 21) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × revenue × closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_252d_base_v118_signal(fcf, revenue, closeadj):
    result = _f23_fcf_growth(fcf, 252) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF acceleration × marketcap proxy
def f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_252d_base_v119_signal(fcf, closeadj, sharesbas):
    result = _f23_fcf_acceleration(fcf, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF acceleration × marketcap proxy
def f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_63d_base_v120_signal(fcf, closeadj, sharesbas):
    result = _f23_fcf_acceleration(fcf, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth × ncfo × closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_21d_base_v121_signal(fcf, ncfo, closeadj):
    result = _f23_fcf_growth(fcf, 21) * ncfo * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × ncfo × closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_252d_base_v122_signal(fcf, ncfo, closeadj):
    result = _f23_fcf_growth(fcf, 252) * ncfo * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory × ebitda × closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajxebitdaprice_252d_base_v123_signal(ncfo, ebitda, closeadj):
    result = _f23_cashflow_traj(ncfo, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × ebitda × closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthxebitdaprice_252d_base_v124_signal(fcf, ebitda, closeadj):
    result = _f23_fcf_growth(fcf, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × ebitda - 252d capex (FCF generation gap)
def f23cft_f23_cash_flow_trajectory_fcfgapxebitda_252d_base_v125_signal(fcf, ebitda, capex, closeadj):
    result = _f23_fcf_growth(fcf, 252) * (ebitda - capex.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo trajectory × (assets - liabilities)  net asset traj
def f23cft_f23_cash_flow_trajectory_ncfotrajxnet_252d_base_v126_signal(ncfo, assets, liabilities, closeadj):
    result = _f23_cashflow_traj(ncfo, 252) * (assets - liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth EMA scaled by closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthema_21d_base_v127_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo trajectory EMA scaled by closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajema_21d_base_v128_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth ranked over 252d window times closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthrank_252d_base_v129_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 21)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory ranked over 252d times closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajrank_252d_base_v130_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of FCF growth above 5%
def f23cft_f23_cash_flow_trajectory_fcfgrowthhighcount_252d_base_v131_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 63) > 0.05).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of FCF growth below -5%
def f23cft_f23_cash_flow_trajectory_fcfgrowthlowcount_504d_base_v132_signal(fcf, closeadj):
    flag = (_f23_fcf_growth(fcf, 63) < -0.05).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of ncfo growth in expansion (>2%)
def f23cft_f23_cash_flow_trajectory_ncfotrajexpcount_252d_base_v133_signal(ncfo, closeadj):
    flag = (_f23_cashflow_traj(ncfo, 63) > 0.02).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth std times 252d FCF growth (vol-weighted level)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxvol_252d_base_v134_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    sd = _std(_f23_fcf_growth(fcf, 63), 252)
    result = g * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo traj std times 63d ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajxvol_63d_base_v135_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 63)
    sd = _std(_f23_cashflow_traj(ncfo, 21), 63)
    result = g * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite cashflow score: 252d FCF growth + 252d ncfo trajectory + accel
def f23cft_f23_cash_flow_trajectory_compositescore_252d_base_v136_signal(fcf, ncfo, closeadj):
    a = _f23_fcf_growth(fcf, 252)
    b = _f23_cashflow_traj(ncfo, 252)
    c = _f23_fcf_acceleration(fcf, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth scaled by closeadj × revenue (sales-quality)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxsales_63d_base_v137_signal(fcf, revenue, closeadj):
    result = _f23_fcf_growth(fcf, 63) * (revenue / closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth scaled by netinc trend
def f23cft_f23_cash_flow_trajectory_fcfgrowthxni_252d_base_v138_signal(fcf, netinc, closeadj):
    result = _f23_fcf_growth(fcf, 252) * netinc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo traj × netinc × closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajxnini_21d_base_v139_signal(ncfo, netinc, closeadj):
    result = _f23_cashflow_traj(ncfo, 21) * netinc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding cumulative FCF growth from start of period
def f23cft_f23_cash_flow_trajectory_fcfgrowthexp_252d_base_v140_signal(fcf, closeadj):
    g = _f23_fcf_growth(fcf, 252)
    result = g.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding cumulative ncfo trajectory mean × closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajexp_252d_base_v141_signal(ncfo, closeadj):
    g = _f23_cashflow_traj(ncfo, 252)
    result = g.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF growth × current ratio × closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthcrprice_63d_base_v142_signal(fcf, currentratio, closeadj):
    result = _f23_fcf_growth(fcf, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo traj × workingcapital × closeadj
def f23cft_f23_cash_flow_trajectory_ncfotrajwcprice_21d_base_v143_signal(ncfo, workingcapital, closeadj):
    result = _f23_cashflow_traj(ncfo, 21) * workingcapital * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF growth divided by 252d FCF growth times closeadj
def f23cft_f23_cash_flow_trajectory_fcfgrowthratio_21v252_base_v144_signal(fcf, closeadj):
    a = _f23_fcf_growth(fcf, 21)
    b = _f23_fcf_growth(fcf, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo traj divided by 504d ncfo traj
def f23cft_f23_cash_flow_trajectory_ncfotrajratio_252v504_base_v145_signal(ncfo, closeadj):
    a = _f23_cashflow_traj(ncfo, 252)
    b = _f23_cashflow_traj(ncfo, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth weighted by net asset position (assets - debt)
def f23cft_f23_cash_flow_trajectory_fcfgrowthxnet_252d_base_v146_signal(fcf, assets, debt, closeadj):
    result = _f23_fcf_growth(fcf, 252) * (assets - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo trajectory × (revenue - capex)
def f23cft_f23_cash_flow_trajectory_ncfotrajxrevcapex_63d_base_v147_signal(ncfo, revenue, capex, closeadj):
    result = _f23_cashflow_traj(ncfo, 63) * (revenue - capex.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × (gp - opinc) margin spread
def f23cft_f23_cash_flow_trajectory_fcfgrowthxgpopgap_252d_base_v148_signal(fcf, gp, opinc, closeadj):
    result = _f23_fcf_growth(fcf, 252) * (gp - opinc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF growth × (equity - debt) leverage net
def f23cft_f23_cash_flow_trajectory_fcfgrowthxneteq_252d_base_v149_signal(fcf, equity, debt, closeadj):
    result = _f23_fcf_growth(fcf, 252) * (equity - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# composite trajectory: (FCF growth + ncfo traj) × (revenue) × closeadj
def f23cft_f23_cash_flow_trajectory_compositetraj_252d_base_v150_signal(fcf, ncfo, revenue, closeadj):
    result = (_f23_fcf_growth(fcf, 252) + _f23_cashflow_traj(ncfo, 252)) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23cft_f23_cash_flow_trajectory_fcfgrowthxdebt_252d_base_v076_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxdebt_63d_base_v077_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_252d_base_v078_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxgp_63d_base_v079_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_252d_base_v080_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxopinc_63d_base_v081_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxeps_252d_base_v082_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxeps_63d_base_v083_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxwc_252d_base_v084_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxwc_63d_base_v085_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_21d_base_v086_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxcr_252d_base_v087_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxcr_252d_base_v088_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_63d_base_v089_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxliab_252d_base_v090_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxre_63d_base_v091_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxre_252d_base_v092_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxintexp_63d_base_v093_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxintexp_252d_base_v094_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxtax_252d_base_v095_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajsq_21d_base_v096_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajsq_252d_base_v097_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajarea_63d_base_v098_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajarea_252d_base_v099_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajarea_504d_base_v100_signal,
    f23cft_f23_cash_flow_trajectory_fcfminusncfo_252d_base_v101_signal,
    f23cft_f23_cash_flow_trajectory_fcfminusncfo_63d_base_v102_signal,
    f23cft_f23_cash_flow_trajectory_fcfplusncfo_252d_base_v103_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthworst_504d_base_v104_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthbest_504d_base_v105_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmax_63d_base_v106_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmax_252d_base_v107_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmin_63d_base_v108_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajmin_252d_base_v109_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_21d_base_v110_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthemaebitda_252d_base_v111_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthareaxmcap_252d_base_v112_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajanom_63d_base_v113_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajanom_252d_base_v114_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthanom_63d_base_v115_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthanom_252d_base_v116_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_21d_base_v117_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxrevxprice_252d_base_v118_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_252d_base_v119_signal,
    f23cft_f23_cash_flow_trajectory_fcfaccelxmcap_63d_base_v120_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_21d_base_v121_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxncfolvl_252d_base_v122_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxebitdaprice_252d_base_v123_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxebitdaprice_252d_base_v124_signal,
    f23cft_f23_cash_flow_trajectory_fcfgapxebitda_252d_base_v125_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnet_252d_base_v126_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthema_21d_base_v127_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajema_21d_base_v128_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthrank_252d_base_v129_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajrank_252d_base_v130_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthhighcount_252d_base_v131_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthlowcount_504d_base_v132_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajexpcount_252d_base_v133_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxvol_252d_base_v134_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxvol_63d_base_v135_signal,
    f23cft_f23_cash_flow_trajectory_compositescore_252d_base_v136_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxsales_63d_base_v137_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxni_252d_base_v138_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxnini_21d_base_v139_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthexp_252d_base_v140_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajexp_252d_base_v141_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthcrprice_63d_base_v142_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajwcprice_21d_base_v143_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthratio_21v252_base_v144_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajratio_252v504_base_v145_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxnet_252d_base_v146_signal,
    f23cft_f23_cash_flow_trajectory_ncfotrajxrevcapex_63d_base_v147_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxgpopgap_252d_base_v148_signal,
    f23cft_f23_cash_flow_trajectory_fcfgrowthxneteq_252d_base_v149_signal,
    f23cft_f23_cash_flow_trajectory_compositetraj_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_CASH_FLOW_TRAJECTORY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    ncff = pd.Series(-2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="ncff")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="intexp")
    retearn = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="retearn")
    liabilities = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    taxexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="taxexp")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "ncff": ncff, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "eps": eps, "sharesbas": sharesbas,
        "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
        "currentratio": currentratio, "intexp": intexp, "retearn": retearn,
        "liabilities": liabilities, "taxexp": taxexp,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_cashflow_traj", "_f23_fcf_growth", "_f23_fcf_acceleration")
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
    print(f"OK f23_cash_flow_trajectory_base_076_150_claude: {n_features} features pass")
