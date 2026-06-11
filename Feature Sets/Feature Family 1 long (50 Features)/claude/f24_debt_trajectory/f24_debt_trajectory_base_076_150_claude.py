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
def _f24_debt_traj(debt, w):
    base = debt.rolling(w, min_periods=max(1, w // 2)).mean()
    return base.diff(periods=w) / base.abs().shift(w).replace(0, np.nan)


def _f24_debt_growth(debt, w):
    return debt.diff(periods=w) / debt.abs().rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)


def _f24_leverage_traj(debt, equity, w):
    lev = debt / equity.replace(0, np.nan)
    return lev.diff(periods=w) / lev.abs().shift(w).replace(0, np.nan)


# 252d debt growth × gp
def f24dt_f24_debt_trajectory_debtgrowthxgp_252d_base_v076_signal(debt, gp, closeadj):
    result = _f24_debt_growth(debt, 252) * gp
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × gp
def f24dt_f24_debt_trajectory_debtgrowthxgp_63d_base_v077_signal(debt, gp, closeadj):
    result = _f24_debt_growth(debt, 63) * gp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × opinc
def f24dt_f24_debt_trajectory_debtgrowthxopinc_252d_base_v078_signal(debt, opinc, closeadj):
    result = _f24_debt_growth(debt, 252) * opinc
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × opinc
def f24dt_f24_debt_trajectory_debtgrowthxopinc_63d_base_v079_signal(debt, opinc, closeadj):
    result = _f24_debt_growth(debt, 63) * opinc
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × ncfo
def f24dt_f24_debt_trajectory_debtgrowthxncfo_252d_base_v080_signal(debt, ncfo, closeadj):
    result = _f24_debt_growth(debt, 252) * ncfo
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × fcf
def f24dt_f24_debt_trajectory_debtgrowthxfcf_252d_base_v081_signal(debt, fcf, closeadj):
    result = _f24_debt_growth(debt, 252) * fcf
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × eps × close
def f24dt_f24_debt_trajectory_debtgrowthxeps_252d_base_v082_signal(debt, eps, closeadj):
    result = _f24_debt_growth(debt, 252) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × eps × close
def f24dt_f24_debt_trajectory_debttrajxeps_63d_base_v083_signal(debt, eps, closeadj):
    result = _f24_debt_traj(debt, 63) * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × workingcapital
def f24dt_f24_debt_trajectory_debtgrowthxwc_252d_base_v084_signal(debt, workingcapital, closeadj):
    result = _f24_debt_growth(debt, 252) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × workingcapital
def f24dt_f24_debt_trajectory_debttrajxwc_63d_base_v085_signal(debt, workingcapital, closeadj):
    result = _f24_debt_traj(debt, 63) * workingcapital
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × currentratio × close
def f24dt_f24_debt_trajectory_debtgrowthxcr_21d_base_v086_signal(debt, currentratio, closeadj):
    result = _f24_debt_growth(debt, 21) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × currentratio × close
def f24dt_f24_debt_trajectory_debtgrowthxcr_252d_base_v087_signal(debt, currentratio, closeadj):
    result = _f24_debt_growth(debt, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj × currentratio × close
def f24dt_f24_debt_trajectory_debttrajxcr_252d_base_v088_signal(debt, currentratio, closeadj):
    result = _f24_debt_traj(debt, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × liabilities
def f24dt_f24_debt_trajectory_debtgrowthxliab_63d_base_v089_signal(debt, liabilities, closeadj):
    result = _f24_debt_growth(debt, 63) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × liabilities
def f24dt_f24_debt_trajectory_debtgrowthxliab_252d_base_v090_signal(debt, liabilities, closeadj):
    result = _f24_debt_growth(debt, 252) * liabilities
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × retearn
def f24dt_f24_debt_trajectory_debttrajxre_63d_base_v091_signal(debt, retearn, closeadj):
    result = _f24_debt_traj(debt, 63) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × retained earnings
def f24dt_f24_debt_trajectory_debtgrowthxre_252d_base_v092_signal(debt, retearn, closeadj):
    result = _f24_debt_growth(debt, 252) * retearn
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × intexp (interest cost trend)
def f24dt_f24_debt_trajectory_debttrajxintexp_63d_base_v093_signal(debt, intexp, closeadj):
    result = _f24_debt_traj(debt, 63) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × intexp
def f24dt_f24_debt_trajectory_debtgrowthxintexp_252d_base_v094_signal(debt, intexp, closeadj):
    result = _f24_debt_growth(debt, 252) * intexp
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × taxexp
def f24dt_f24_debt_trajectory_debtgrowthxtax_252d_base_v095_signal(debt, taxexp, closeadj):
    result = _f24_debt_growth(debt, 252) * taxexp
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt traj squared × close
def f24dt_f24_debt_trajectory_debttrajsq_21d_base_v096_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 21)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj squared × close
def f24dt_f24_debt_trajectory_debttrajsq_252d_base_v097_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    result = g * g.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj area × close
def f24dt_f24_debt_trajectory_debttrajarea_63d_base_v098_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 21).abs()
    result = g.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj area × close
def f24dt_f24_debt_trajectory_debttrajarea_252d_base_v099_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt traj area × close
def f24dt_f24_debt_trajectory_debttrajarea_504d_base_v100_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252).abs()
    result = g.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth - 252d ncfo growth (net debt change vs cash)
def f24dt_f24_debt_trajectory_debtminusncfo_252d_base_v101_signal(debt, ncfo, closeadj):
    a = _f24_debt_growth(debt, 252)
    b = ncfo.diff(periods=252) / ncfo.abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth - 63d fcf growth
def f24dt_f24_debt_trajectory_debtminusfcf_63d_base_v102_signal(debt, fcf, closeadj):
    a = _f24_debt_growth(debt, 63)
    b = fcf.diff(periods=63) / fcf.abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth + 252d leverage traj
def f24dt_f24_debt_trajectory_debtpluslev_252d_base_v103_signal(debt, equity, closeadj):
    result = (_f24_debt_growth(debt, 252) + _f24_leverage_traj(debt, equity, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding worst (max) debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthworst_504d_base_v104_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    result = g.expanding(min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding best (min) debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthbest_504d_base_v105_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    result = g.expanding(min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max debt traj in 63d
def f24dt_f24_debt_trajectory_debttrajmax_63d_base_v106_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 21).rolling(63, min_periods=21).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max debt traj in 252d
def f24dt_f24_debt_trajectory_debttrajmax_252d_base_v107_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 63).rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min debt traj in 63d (deepest paydown)
def f24dt_f24_debt_trajectory_debttrajmin_63d_base_v108_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 21).rolling(63, min_periods=21).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min debt traj in 252d
def f24dt_f24_debt_trajectory_debttrajmin_252d_base_v109_signal(debt, closeadj):
    result = _f24_debt_traj(debt, 63).rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthemaebitda_21d_base_v110_signal(debt, ebitda, closeadj):
    g = _f24_debt_growth(debt, 21)
    result = g.ewm(span=21, adjust=False).mean() * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of debt growth × ebitda
def f24dt_f24_debt_trajectory_debtgrowthemaebitda_252d_base_v111_signal(debt, ebitda, closeadj):
    g = _f24_debt_growth(debt, 252)
    result = g.ewm(span=252, adjust=False).mean() * ebitda
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth area × mcap
def f24dt_f24_debt_trajectory_debtgrowthareaxmcap_252d_base_v112_signal(debt, closeadj, sharesbas):
    g = _f24_debt_growth(debt, 63).abs()
    result = g.rolling(252, min_periods=63).sum() * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj anomaly × close
def f24dt_f24_debt_trajectory_debttrajanom_63d_base_v113_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    base = _mean(_f24_debt_traj(debt, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj anomaly × close
def f24dt_f24_debt_trajectory_debttrajanom_252d_base_v114_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    base = _mean(_f24_debt_traj(debt, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth anomaly × close
def f24dt_f24_debt_trajectory_debtgrowthanom_63d_base_v115_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 63)
    base = _mean(_f24_debt_growth(debt, 252), 252)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth anomaly × close
def f24dt_f24_debt_trajectory_debtgrowthanom_252d_base_v116_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    base = _mean(_f24_debt_growth(debt, 504), 504)
    result = (g - base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × revenue × close
def f24dt_f24_debt_trajectory_debtgrowthxrevxprice_21d_base_v117_signal(debt, revenue, closeadj):
    result = _f24_debt_growth(debt, 21) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × revenue × close
def f24dt_f24_debt_trajectory_debtgrowthxrevxprice_252d_base_v118_signal(debt, revenue, closeadj):
    result = _f24_debt_growth(debt, 252) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d leverage traj × marketcap
def f24dt_f24_debt_trajectory_levtrajxmcap_252d_base_v119_signal(debt, equity, closeadj, sharesbas):
    result = _f24_leverage_traj(debt, equity, 252) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d leverage traj × marketcap
def f24dt_f24_debt_trajectory_levtrajxmcap_63d_base_v120_signal(debt, equity, closeadj, sharesbas):
    result = _f24_leverage_traj(debt, equity, 63) * (closeadj * sharesbas)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth × debt level × close
def f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_21d_base_v121_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 21) * debt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × debt level × close
def f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_252d_base_v122_signal(debt, closeadj):
    result = _f24_debt_growth(debt, 252) * debt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj × ebitda × close
def f24dt_f24_debt_trajectory_debttrajxebitdaprice_252d_base_v123_signal(debt, ebitda, closeadj):
    result = _f24_debt_traj(debt, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × ebitda × close
def f24dt_f24_debt_trajectory_debtgrowthxebitdaprice_252d_base_v124_signal(debt, ebitda, closeadj):
    result = _f24_debt_growth(debt, 252) * ebitda * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × (ebitda - capex) (debt service margin)
def f24dt_f24_debt_trajectory_debtgrowthxebitdacapex_252d_base_v125_signal(debt, ebitda, capex, closeadj):
    result = _f24_debt_growth(debt, 252) * (ebitda - capex.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj × (assets - liabilities)
def f24dt_f24_debt_trajectory_debttrajxnet_252d_base_v126_signal(debt, assets, liabilities, closeadj):
    result = _f24_debt_traj(debt, 252) * (assets - liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthema_21d_base_v127_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of debt traj × close
def f24dt_f24_debt_trajectory_debttrajema_21d_base_v128_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 21)
    result = g.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth rank over 252d × close
def f24dt_f24_debt_trajectory_debtgrowthrank_252d_base_v129_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 21)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj rank over 252d × close
def f24dt_f24_debt_trajectory_debttrajrank_252d_base_v130_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    result = g.rolling(252, min_periods=63).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × cumulative paydown count (negative growth)
def f24dt_f24_debt_trajectory_debtpaydowncount_252d_base_v131_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 63) < 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt growth × cumulative spike count (>5%)
def f24dt_f24_debt_trajectory_debtspikecount_504d_base_v132_signal(debt, closeadj):
    flag = (_f24_debt_growth(debt, 63) > 0.05).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of leverage trajectory contraction
def f24dt_f24_debt_trajectory_levtrajcontrcount_252d_base_v133_signal(debt, equity, closeadj):
    flag = (_f24_leverage_traj(debt, equity, 63) < -0.02).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × std of debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthxvol_252d_base_v134_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    sd = _std(_f24_debt_growth(debt, 63), 252)
    result = g * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × std of debt traj × close
def f24dt_f24_debt_trajectory_debttrajxvol_63d_base_v135_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 63)
    sd = _std(_f24_debt_traj(debt, 21), 63)
    result = g * sd * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# composite debt score: 252d debt growth + 252d debt traj + leverage traj
def f24dt_f24_debt_trajectory_compositescore_252d_base_v136_signal(debt, equity, closeadj):
    a = _f24_debt_growth(debt, 252)
    b = _f24_debt_traj(debt, 252)
    c = _f24_leverage_traj(debt, equity, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × revenue per share
def f24dt_f24_debt_trajectory_debtgrowthxsales_63d_base_v137_signal(debt, revenue, closeadj):
    result = _f24_debt_growth(debt, 63) * (revenue / closeadj.replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × netinc × close
def f24dt_f24_debt_trajectory_debtgrowthxni_252d_base_v138_signal(debt, netinc, closeadj):
    result = _f24_debt_growth(debt, 252) * netinc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt traj × netinc × close
def f24dt_f24_debt_trajectory_debttrajxnini_21d_base_v139_signal(debt, netinc, closeadj):
    result = _f24_debt_traj(debt, 21) * netinc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding mean debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthexp_252d_base_v140_signal(debt, closeadj):
    g = _f24_debt_growth(debt, 252)
    result = g.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# expanding mean debt traj × close
def f24dt_f24_debt_trajectory_debttrajexp_252d_base_v141_signal(debt, closeadj):
    g = _f24_debt_traj(debt, 252)
    result = g.expanding(min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt growth × current ratio × close
def f24dt_f24_debt_trajectory_debtgrowthcrprice_63d_base_v142_signal(debt, currentratio, closeadj):
    result = _f24_debt_growth(debt, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt traj × workingcapital × close
def f24dt_f24_debt_trajectory_debttrajwcprice_21d_base_v143_signal(debt, workingcapital, closeadj):
    result = _f24_debt_traj(debt, 21) * workingcapital * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt growth / 252d debt growth × close
def f24dt_f24_debt_trajectory_debtgrowthratio_21v252_base_v144_signal(debt, closeadj):
    a = _f24_debt_growth(debt, 21)
    b = _f24_debt_growth(debt, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt traj / 504d debt traj × close
def f24dt_f24_debt_trajectory_debttrajratio_252v504_base_v145_signal(debt, closeadj):
    a = _f24_debt_traj(debt, 252)
    b = _f24_debt_traj(debt, 504).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × (assets - debt)
def f24dt_f24_debt_trajectory_debtgrowthxnet_252d_base_v146_signal(debt, assets, closeadj):
    result = _f24_debt_growth(debt, 252) * (assets - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt traj × (revenue - capex)
def f24dt_f24_debt_trajectory_debttrajxrevcapex_63d_base_v147_signal(debt, revenue, capex, closeadj):
    result = _f24_debt_traj(debt, 63) * (revenue - capex.abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × (gp - opinc) × close
def f24dt_f24_debt_trajectory_debtgrowthxgpopgap_252d_base_v148_signal(debt, gp, opinc, closeadj):
    result = _f24_debt_growth(debt, 252) * (gp - opinc) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt growth × (equity - debt) (net leverage trajectory weighted)
def f24dt_f24_debt_trajectory_debtgrowthxneteq_252d_base_v149_signal(debt, equity, closeadj):
    result = _f24_debt_growth(debt, 252) * (equity - debt)
    return result.replace([np.inf, -np.inf], np.nan)


# composite trajectory: (debt growth + leverage traj) × revenue × close
def f24dt_f24_debt_trajectory_compositetraj_252d_base_v150_signal(debt, equity, revenue, closeadj):
    result = (_f24_debt_growth(debt, 252) + _f24_leverage_traj(debt, equity, 252)) * revenue * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f24dt_f24_debt_trajectory_debtgrowthxgp_252d_base_v076_signal,
    f24dt_f24_debt_trajectory_debtgrowthxgp_63d_base_v077_signal,
    f24dt_f24_debt_trajectory_debtgrowthxopinc_252d_base_v078_signal,
    f24dt_f24_debt_trajectory_debtgrowthxopinc_63d_base_v079_signal,
    f24dt_f24_debt_trajectory_debtgrowthxncfo_252d_base_v080_signal,
    f24dt_f24_debt_trajectory_debtgrowthxfcf_252d_base_v081_signal,
    f24dt_f24_debt_trajectory_debtgrowthxeps_252d_base_v082_signal,
    f24dt_f24_debt_trajectory_debttrajxeps_63d_base_v083_signal,
    f24dt_f24_debt_trajectory_debtgrowthxwc_252d_base_v084_signal,
    f24dt_f24_debt_trajectory_debttrajxwc_63d_base_v085_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcr_21d_base_v086_signal,
    f24dt_f24_debt_trajectory_debtgrowthxcr_252d_base_v087_signal,
    f24dt_f24_debt_trajectory_debttrajxcr_252d_base_v088_signal,
    f24dt_f24_debt_trajectory_debtgrowthxliab_63d_base_v089_signal,
    f24dt_f24_debt_trajectory_debtgrowthxliab_252d_base_v090_signal,
    f24dt_f24_debt_trajectory_debttrajxre_63d_base_v091_signal,
    f24dt_f24_debt_trajectory_debtgrowthxre_252d_base_v092_signal,
    f24dt_f24_debt_trajectory_debttrajxintexp_63d_base_v093_signal,
    f24dt_f24_debt_trajectory_debtgrowthxintexp_252d_base_v094_signal,
    f24dt_f24_debt_trajectory_debtgrowthxtax_252d_base_v095_signal,
    f24dt_f24_debt_trajectory_debttrajsq_21d_base_v096_signal,
    f24dt_f24_debt_trajectory_debttrajsq_252d_base_v097_signal,
    f24dt_f24_debt_trajectory_debttrajarea_63d_base_v098_signal,
    f24dt_f24_debt_trajectory_debttrajarea_252d_base_v099_signal,
    f24dt_f24_debt_trajectory_debttrajarea_504d_base_v100_signal,
    f24dt_f24_debt_trajectory_debtminusncfo_252d_base_v101_signal,
    f24dt_f24_debt_trajectory_debtminusfcf_63d_base_v102_signal,
    f24dt_f24_debt_trajectory_debtpluslev_252d_base_v103_signal,
    f24dt_f24_debt_trajectory_debtgrowthworst_504d_base_v104_signal,
    f24dt_f24_debt_trajectory_debtgrowthbest_504d_base_v105_signal,
    f24dt_f24_debt_trajectory_debttrajmax_63d_base_v106_signal,
    f24dt_f24_debt_trajectory_debttrajmax_252d_base_v107_signal,
    f24dt_f24_debt_trajectory_debttrajmin_63d_base_v108_signal,
    f24dt_f24_debt_trajectory_debttrajmin_252d_base_v109_signal,
    f24dt_f24_debt_trajectory_debtgrowthemaebitda_21d_base_v110_signal,
    f24dt_f24_debt_trajectory_debtgrowthemaebitda_252d_base_v111_signal,
    f24dt_f24_debt_trajectory_debtgrowthareaxmcap_252d_base_v112_signal,
    f24dt_f24_debt_trajectory_debttrajanom_63d_base_v113_signal,
    f24dt_f24_debt_trajectory_debttrajanom_252d_base_v114_signal,
    f24dt_f24_debt_trajectory_debtgrowthanom_63d_base_v115_signal,
    f24dt_f24_debt_trajectory_debtgrowthanom_252d_base_v116_signal,
    f24dt_f24_debt_trajectory_debtgrowthxrevxprice_21d_base_v117_signal,
    f24dt_f24_debt_trajectory_debtgrowthxrevxprice_252d_base_v118_signal,
    f24dt_f24_debt_trajectory_levtrajxmcap_252d_base_v119_signal,
    f24dt_f24_debt_trajectory_levtrajxmcap_63d_base_v120_signal,
    f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_21d_base_v121_signal,
    f24dt_f24_debt_trajectory_debtgrowthxdebtlvl_252d_base_v122_signal,
    f24dt_f24_debt_trajectory_debttrajxebitdaprice_252d_base_v123_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitdaprice_252d_base_v124_signal,
    f24dt_f24_debt_trajectory_debtgrowthxebitdacapex_252d_base_v125_signal,
    f24dt_f24_debt_trajectory_debttrajxnet_252d_base_v126_signal,
    f24dt_f24_debt_trajectory_debtgrowthema_21d_base_v127_signal,
    f24dt_f24_debt_trajectory_debttrajema_21d_base_v128_signal,
    f24dt_f24_debt_trajectory_debtgrowthrank_252d_base_v129_signal,
    f24dt_f24_debt_trajectory_debttrajrank_252d_base_v130_signal,
    f24dt_f24_debt_trajectory_debtpaydowncount_252d_base_v131_signal,
    f24dt_f24_debt_trajectory_debtspikecount_504d_base_v132_signal,
    f24dt_f24_debt_trajectory_levtrajcontrcount_252d_base_v133_signal,
    f24dt_f24_debt_trajectory_debtgrowthxvol_252d_base_v134_signal,
    f24dt_f24_debt_trajectory_debttrajxvol_63d_base_v135_signal,
    f24dt_f24_debt_trajectory_compositescore_252d_base_v136_signal,
    f24dt_f24_debt_trajectory_debtgrowthxsales_63d_base_v137_signal,
    f24dt_f24_debt_trajectory_debtgrowthxni_252d_base_v138_signal,
    f24dt_f24_debt_trajectory_debttrajxnini_21d_base_v139_signal,
    f24dt_f24_debt_trajectory_debtgrowthexp_252d_base_v140_signal,
    f24dt_f24_debt_trajectory_debttrajexp_252d_base_v141_signal,
    f24dt_f24_debt_trajectory_debtgrowthcrprice_63d_base_v142_signal,
    f24dt_f24_debt_trajectory_debttrajwcprice_21d_base_v143_signal,
    f24dt_f24_debt_trajectory_debtgrowthratio_21v252_base_v144_signal,
    f24dt_f24_debt_trajectory_debttrajratio_252v504_base_v145_signal,
    f24dt_f24_debt_trajectory_debtgrowthxnet_252d_base_v146_signal,
    f24dt_f24_debt_trajectory_debttrajxrevcapex_63d_base_v147_signal,
    f24dt_f24_debt_trajectory_debtgrowthxgpopgap_252d_base_v148_signal,
    f24dt_f24_debt_trajectory_debtgrowthxneteq_252d_base_v149_signal,
    f24dt_f24_debt_trajectory_compositetraj_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F24_DEBT_TRAJECTORY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
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
        "ncfo": ncfo, "equity": equity, "debt": debt, "assets": assets,
        "ebitda": ebitda, "capex": capex, "eps": eps, "sharesbas": sharesbas,
        "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
        "currentratio": currentratio, "intexp": intexp, "retearn": retearn,
        "liabilities": liabilities, "taxexp": taxexp,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f24_debt_traj", "_f24_debt_growth", "_f24_leverage_traj")
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
    print(f"OK f24_debt_trajectory_base_076_150_claude: {n_features} features pass")
